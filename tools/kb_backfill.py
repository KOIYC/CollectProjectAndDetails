"""kb_backfill — 回填「历史缺口」（陈旧缺正文）。

问题根因（R2 分析定位）：
  采集窗口会滚动（github_new 只取近 14 天 stars 榜，reddit 取 7 天窗口）。一条条目在
  T 轮取数失败（网络抖动 / CLI 并发 / 上游限流）→ 留下空 body → T+n 轮它已离开窗口，
  adapter 不再返回它 → **永远不会再被修复**。这类缺口是「粘性」的，正常轮次救不回来。

本工具只做一件事：扫历史库，找出「按渠道画像应当有 body 但实际为空」的条目，
按渠道用对应后端重取正文，写回 raw（record_type=backfill）+ 原地刷新 note + 更新 seen 指纹。

用法：
  python tools/kb_backfill.py                 # 回填全部缺口（受 --limit 限制）
  python tools/kb_backfill.py --limit 40      # 单次最多处理 40 条
  python tools/kb_backfill.py --channel github_new
  python tools/kb_backfill.py --dry           # 只列清单不写盘
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import re
import sys
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import (BODY_MIN, DIR_RAW, DIR_REPORT, FULLTEXT_MAX_CHARS, META,  # noqa: E402
                       ROOT, BodyCache, Seen, append_jsonl, body_completeness,
                       direct_fetch_texts, exa_fetch_texts, iso, norm_url, now_cst,
                       note_bucket, pub_day_of, read_ledger, rotate_files, rotate_runs,
                       run_cli, sha1, write_ledger)
from kbc_channels import betalist_launch_date  # noqa: E402
from kb_collect import (ENRICH_ROUTING, MAX_COMMENTS, is_project_ish,  # noqa: E402
                        load_channels_yaml, write_corpus_note, write_entity_note)
from kb_analyze import PROFILE_EXPECT  # noqa: E402

DEAD_LEDGER = META / "backfill_dead.json"
DEAD_AFTER = 2          # 同一缺口连试 N 轮仍取不到 → 判「结构性不可得」，不再重试
DEAD_SCHEMA = 2         # 账本 schema：1 = 只有一句自然语言 reason；2 = 加 reason_code/tried[]/http_status

# 死信原因码 —— 判死**必须**落到一个可复核的分类上，而不是一句自然语言。
# 为什么（2026-09-21 调研报告 §4.2）：旧账本 270 条里 248 条的理由是硬编码的
# 「Exa 未命中该站」，而流程早已是「直取优先」；看账的人据此得出「Exa 不行」的错误归因。
# 更贵的代价：66 条 github 目标条目被判死时用的 URL 与「仓库是否可读」无关，
# 于是「账本说有 66 条可救」本身就是错的 —— 理由与事实不符 ≡ 没有理由。
REASON_CODES: dict[str, str] = {
    "media":       "视频/音频帖：页面只有播放器，没有可抽正文（结构性）",
    "account":     "社交账号页：需登录态（结构性，见渠道台账 auth 段）",
    "repo_missing": "目标仓库不存在 / 已改名（gh readme 404）",
    "gh_miss":     "仓库存在但 README 取不到（空仓库 / 取数被限流）",
    "http_404":    "目标页 404/410（页面已删除）",
    "http_403":    "目标页 403/401/451（拒绝访问 / 需登录 / 法规屏蔽）",
    "unreachable": "连接级失败（超时 / TLS 重置 / 主机被本轮拉黑）",
    "nontext":     "Content-Type 非文本（二进制 / 媒体资源）",
    "no_backend":  "三档后端都尝试过、都未命中（direct → gh → exa）",
    "unknown":     "未能归类（需人工看一条）",
}


def load_dead() -> dict:
    """读死信账本 —— 必须走 `read_ledger`（损坏隔离 + 响亮告警），不许自己 try/except。

    为什么原来那版危险：`except Exception: return {}` 把「文件半截 / 编码坏」伪装成
    「一条死信都没有」。后果不是报错而是**静默清空判定**：已判死的条目集体重回回填队列，
    下一轮重新烧完三档后端额度再判死，而且没人知道发生过。seen/body_cache 早就有
    `.corrupt-*.bak` 隔离，这本账是最后一本没有的（2026-09-21 全库审计 P2-6）。
    """
    return (read_ledger(DEAD_LEDGER, {"items": {}}) or {}).get("items") or {}


def save_dead(d: dict) -> None:
    """写死信账本 —— 锁 + 原子替换（`write_ledger`）。整本一次落盘，不留半截。"""
    write_ledger(DEAD_LEDGER, {
        "schema": DEAD_SCHEMA,
        "updated": iso(now_cst()),
        "note": "结构性无正文/取数不可得 —— 连试 %d 轮后记账，不再消耗额度。"
                "字段：reason（人话）/ reason_code（可复核分类，见 REASON_CODES）/ "
                "tried[]（本轮实际试过的后端）/ http_status（direct 档拿到的状态码）" % DEAD_AFTER,
        "by_reason": dict(collections.Counter(
            (v.get("reason_code") or "unknown") for v in d.values()).most_common()),
        "items": d,
    }, lock_name="backfill_dead", indent=1)



def classify_reason(url: str, status=None, tried: list[str] | None = None,
                    gh_err: str = "") -> str:
    """把一次「没取到」归到一个原因码（判定顺序：结构性 → HTTP 状态 → 后端档位）。"""
    u = url or ""
    tried = tried or []
    if MEDIA_RE.search(u):
        return "media"
    if ACCOUNT_RE.search(u):
        return "account"
    s = status
    if s in (404, 410):
        return "http_404"
    if s in (401, 403, 451):
        return "http_403"
    if s == "nontext":
        return "nontext"
    if s in ("blocked", "timeout", "unreachable"):
        return "unreachable"
    if "gh_readme" in tried:
        low = (gh_err or "").lower()
        if "404" in low or "not found" in low:
            return "repo_missing"
        if "rate limit" in low or "403" in low:
            return "gh_miss"
        return "gh_miss"
    if "exa_web_fetch" in tried or "direct_fetch" in tried:
        return "no_backend"
    return "unknown"


def migrate_dead(apply: bool = False) -> tuple[int, list[tuple[str, str, str]]]:
    """把 schema 1 的死信账本升级到 schema 2：补 reason_code / tried[] / http_status。

    只做**信息补齐**，不改判定：attempts / url / title / reason 原文一律保留
    （旧 reason 文本是审计线索，删了就再也说不清「当初为什么判死」）。
    """
    dead = load_dead()
    changes: list[tuple[str, str, str]] = []
    for iid, v in dead.items():
        old_code = v.get("reason_code")
        tried = v.get("tried")
        tried_l = [t for t in (tried if isinstance(tried, list) else
                               str(tried or "").split("→")) if t]
        code = old_code or classify_reason(v.get("url") or "", status=None,
                                           tried=tried_l or ["direct_fetch", "exa_web_fetch"])
        if old_code != code:
            v["reason_code"] = code
            changes.append((iid, old_code or "(无)", code))
        if not isinstance(tried, list):
            v["tried"] = tried_l or ["direct_fetch", "exa_web_fetch"]
        v.setdefault("http_status", None)
        # 人话理由与结构化证据不一致时**以结构化字段为准重建人话**（旧的转存 reason_first）。
        # 目的：账本里任何一条都不允许出现「理由说 A、字段说 B」——
        # 那正是本轮修的原始缺陷（248 条理由与实际后端不符）的同一形态。
        want = (f"取数失败（已试 {'→'.join(v['tried'])}）· 判定 {v['reason_code']}"
                + (f" · status={v['http_status']}" if v.get("http_status") is not None else ""))
        cur = v.get("reason") or ""
        # 只重建**取数失败类**理由（它们才可能与 tried[] 打架）。
        # 结构性理由（「视频帖无正文」「社交账号页需登录」）是领域知识，与 reason_code 天然一致，
        # 保留原文更好读 —— 一致性要求是「不矛盾」，不是「长得一样」。
        if cur.startswith("取数失败（已试") and cur != want:
            if not v.get("reason_first"):
                v["reason_first"] = cur
            v["reason"] = want
        elif cur and not v.get("reason_first") and v["reason_code"] in ("media", "account"):
            v["reason_first"] = cur
    dirty = True                       # 本函数现在总是补齐 reason_code/tried/http_status，直接落盘
    if apply and dirty:
        bak = META / f"backfill_dead.schema1.bak-{now_cst():%Y%m%dT%H%M%S}.json"
        bak.write_text(json.dumps({"schema": 1, "items": dead}, ensure_ascii=False, indent=1),
                       encoding="utf-8")
        save_dead(dead)
    return len(changes), changes


def render_dead_report(dead: dict) -> str:
    """死信账本按原因码复核 —— 这是「判死」这件事的可审计面。"""
    by = collections.defaultdict(list)
    for iid, v in dead.items():
        by[(v.get("reason_code") or "unknown")].append(v)
    hosts = collections.Counter()
    for v in dead.values():
        h = urllib.parse.urlsplit(v.get("url") or "").netloc.lower().removeprefix("www.")
        if h:
            hosts[h] += 1
    L = ["# 死信账本（按原因码复核）", "",
         f"> 生成 {iso(now_cst())} · 账本 `_meta/backfill_dead.json` · 判死门槛：连试 {DEAD_AFTER} 轮",
         f"> 合计 **{len(dead)}** 条 · 原因码 schema v{DEAD_SCHEMA}", "",
         "**这张表回答的问题**：这些条目是「结构性不可得」还是「我们没取到」。"
         "前者不该再烧额度，后者是缺陷 —— 必须能一眼分开。", "",
         "| 原因码 | 条数 | 含义 |", "|---|---|---|"]
    for code, items in sorted(by.items(), key=lambda kv: -len(kv[1])):
        L.append(f"| `{code}` | {len(items)} | {REASON_CODES.get(code, '—')} |")
    L += ["", "## 按主机（前 20）", "", "| 主机 | 条数 |", "|---|---|"]
    L += [f"| `{h}` | {n} |" for h, n in hosts.most_common(20)]
    for code, items in sorted(by.items(), key=lambda kv: -len(kv[1])):
        L += ["", f"## `{code}`（{len(items)} 条）", ""]
        for v in sorted(items, key=lambda x: x.get("source_id") or "")[:30]:
            t = (v.get("title") or "(无标题)").replace("|", "/")[:70]
            tried = "/".join(v.get("tried") or [])
            L.append(f"- [{v.get('source_id', '?')}] {t} —— `{tried}` "
                     f"· status={v.get('http_status')} · {v.get('reason') or ''}")
        if len(items) > 30:
            L.append(f"- …另有 {len(items) - 30} 条")
    L += ["", "## 下一步", "", "```",
          "python tools/kb_backfill.py --dead-report        # 重生成本报告",
          "python tools/kb_backfill.py --migrate-dead --apply   # 账本 schema 升级（带备份）",
          "python tools/kb_backfill.py --revive-github     # 把路由缺陷造成的死信放回队列",
          "```"]
    return "\n".join(L)


def revive_github_dead() -> tuple[int, Path]:
    """把「目标 URL 指向 github 仓库」的死信放出队列，并留下 undo 清单。

    为什么需要它：这类死信是**路由缺陷**造成的（按 source_id 而非 URL 分流），
    不是真的取不到 —— 修好路由后必须把它们从账本里放出来，否则 build_queue 仍会
    以 `attempts >= DEAD_AFTER` 跳过，修复等于没生效。
    纪律：改账本必须留痕（同搬家三件套），清单里逐条记 from/to，可 --undo 还原语义。
    """
    dead = load_dead()
    moved = {}
    for iid, v in list(dead.items()):
        m = GH_REPO_RE.match(v.get("url") or "")
        if not m:
            continue
        if (m.group(2) or "").lower() in {"issues", "discussions", "pulls", "marketplace",
                                          "sponsors", "topics"}:
            continue
        moved[iid] = dead.pop(iid)
    ts = now_cst().strftime("%Y%m%dT%H%M%S")
    manifest = META / f"backfill_dead_revive_manifest_{ts}.json"
    write_ledger(manifest,
        {"action": "revive-github", "at": iso(now_cst()), "count": len(moved),
         "reason": "路由按 source_id 分流导致 github 目标未走 gh readme，属可修缺陷",
         "undo": "把这批 item_id 重新写回 _meta/backfill_dead.json 的 items（attempts>=%d）"
                 % DEAD_AFTER,
         "items": moved}, lock_name="backfill_dead_revive_manifest", indent=1)
    rotate_files(META, "backfill_dead_revive_manifest_", 12)
    save_dead(dead)
    return len(moved), manifest


def revive_by_code(codes: list[str], apply: bool = False) -> tuple[int, Path | None, list[str]]:
    """按原因码把死信放回队列（改账本必须留痕：manifest 逐条记 from）。

    为什么需要：原因码本身会暴露「判死是在旧判据下做的」。实例：182 条 `no_backend`
    是 2026-09-21 之前判的，那时 github 目标按 source_id 路由、压根没走过 gh 档 ——
    结论「三档都没命中」在当时就不成立。判据变了，被它判过的账必须能重开，
    否则修复只对新进语料生效（同 kb_prune 的存在理由）。
    """
    dead = load_dead()
    moved: dict = {}
    ids: list[str] = []
    for iid, v in list(dead.items()):
        if (v.get("reason_code") or "unknown") in codes:
            moved[iid] = dead.pop(iid)
            ids.append(iid)
    manifest = None
    if apply and moved:
        ts = now_cst().strftime("%Y%m%dT%H%M%S")
        manifest = META / f"backfill_dead_revive_manifest_{ts}.json"
        write_ledger(manifest,
            {"action": "revive-by-reason-code", "at": iso(now_cst()), "codes": codes,
             "count": len(moved),
             "reason": "判据变更后重开旧判定（如 github 目标改按 URL 路由、判死前补跑三档）",
             "undo": "把这批 item_id 重新写回 _meta/backfill_dead.json 的 items（attempts 保持原值）",
             "items": moved}, lock_name="backfill_dead_revive_manifest", indent=1)
        rotate_files(META, "backfill_dead_revive_manifest_", 12)
        save_dead(dead)
    return len(moved), manifest, ids


def fix_published_at(channels: dict, dry: bool = False, limit: int = 0) -> dict:
    """B2 契约门的回填侧：把「该有发布日但没有」的条目补上（按渠道专属抽取器）。

    为什么放在 kb_backfill 而不是 kb_reclassify：这跟缺正文是**同一类缺口** —— 条目离开
    采集窗口后源站变了/当时没解析，本地再怎么自愈也补不出来，必须回源站取。
    纪律与正文回填一致：raw 只追加、note 原地刷新、抽不到就**留空并记账**（不猜、不用别的
    日期凑数 —— 时间轴上一个语义错的日期比缺一个日期伤害更大）。
    """
    fixers = {"betalist": betalist_launch_date}
    seen = Seen()
    archived = {iid for iid, m in seen.items.items()
                if str(m.get("note") or "").startswith("80-归档/")}
    todo: list[tuple[str, dict, str]] = []
    for iid, (r, day) in load_latest().items():
        cid = r.get("source_id") or ""
        if cid not in fixers or iid in archived:
            continue
        ch = channels.get(cid) or {}
        if not ch.get("enabled"):
            continue
        prof = ch.get("profile") or "discussion"
        if not PROFILE_EXPECT.get(prof, {}).get("published_at"):
            continue
        if (ch.get("meta_unavailable") or {}).get("published_at"):
            continue                                    # 注册表已声明不可得 → 免追
        if pub_day_of(r.get("published_at")):
            continue
        todo.append((iid, r, day))
    if limit:
        todo = todo[:limit]
    stat = {"candidates": len(todo), "fixed": 0, "not_found": 0, "errors": 0}
    if not todo:
        return stat
    urls = [r.get("url") or "" for _i, r, _d in todo]
    status_out: dict = {}
    try:
        texts = direct_fetch_texts(urls, max_chars=20000, workers=6, status_out=status_out)
    except Exception as e:                                          # noqa: BLE001
        print(f"  [w] 详情页批次失败：{str(e)[:70]}")
        texts = {}
    if dry:
        for iid, r, _d in todo:
            d = fixers[r["source_id"]](texts.get(r.get("url") or "", ""))
            print(f"  [betalist] {d or '（抽不到）'} ← {(r.get('title') or '')[:50]}")
        return stat
    run_id = "backfill-" + now_cst().strftime("%Y%m%d-%H%M%S")
    day_now = now_cst().strftime("%Y-%m-%d")
    for iid, r, day in todo:
        u = r.get("url") or ""
        date = fixers.get(r["source_id"], lambda _t: None)(texts.get(u, ""))
        if not date:
            stat["not_found"] += 1
            continue
        rec = dict(r)
        rec["published_at"] = date
        rec["extra"] = dict(rec.get("extra") or {})
        rec["extra"]["published_at_source"] = f"{r['source_id']}:detail-anchor"
        rec["extra"]["published_at_fixed_by"] = "kb_backfill --fix-meta"
        rec["captured_at"] = iso(now_cst())
        rec["record_type"] = "backfill"
        rec["run_id"] = run_id
        try:
            append_jsonl(DIR_RAW / r["source_id"] / f"{day_now}.jsonl", [rec])
            p = write_corpus_note(rec, note_bucket(seen, iid, day))
            rel = p.relative_to(ROOT).as_posix()
            if is_project_ish(rec) or (rec.get("kind") or "").lower() in ("person", "method"):
                write_entity_note(rec, rel)
            seen.touch(iid, r["source_id"], rel, None, content_hash=None)
            stat["fixed"] += 1
        except Exception as e:                                      # noqa: BLE001
            print(f"    [!] 写盘失败 {iid}: {str(e)[:60]}")
            stat["errors"] += 1
    seen.save()
    write_ledger(META / "runs" / f"{run_id}.json",
        {"run_id": run_id, "kind": "fix-meta", **stat, "started": iso(now_cst())},
        lock_name="runs", indent=1)
    rotate_runs()
    return stat


def load_latest() -> dict[str, tuple[dict, str]]:
    """返回 item_id → (最新记录, 该记录所在 raw 分片的日期)。"""
    latest: dict[str, tuple[dict, str]] = {}
    for f in sorted(glob.glob(str(DIR_RAW / "*" / "*.jsonl"))):
        day = Path(f).stem
        for ln in open(f, encoding="utf-8"):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:                                      # noqa: BLE001
                continue
            iid = r.get("item_id")
            if not iid:
                continue
            cur = latest.get(iid)
            if cur is None or (r.get("captured_at") or "") >= (cur[0].get("captured_at") or ""):
                latest[iid] = (r, day)
    return latest


def build_queue(channels: dict, only: str = "") -> list[tuple[dict, str]]:
    """(record, day) 列表：正文**不完整**的条目（已排除死信）。

    旧实现只判 `len(body) >= BODY_MIN`（120 字）就算达标 —— 于是 RSS 给的
    300~600 字摘要、Exa 砍在 8000 字的残篇全被当成「已有正文」，永远不进回填队列。
    这正是内容审计里 31 条 RSS 残文 + 17 条 Exa 截断长期不消失的原因。
    现在改用 body_completeness()：只有 full 才算达标，summary/snippet/empty 都算缺口。
    """
    dead = load_dead()
    archived = {iid for iid, m in Seen().items.items()
                if str(m.get("note") or "").startswith("80-归档/")}
    out = []
    for iid, (r, day) in load_latest().items():
        ch = channels.get(r.get("source_id") or "")
        if not ch:
            continue
        if iid in archived:
            continue                                           # 已归档条目不回填：raw 是不可变重放底座，
        # 回填按 (record, day) 现算 live 路径写 note → 会把冻结区条目复活成在库页
        # （实测 2026-09-21：prune 归档 6 条 → 同轮 backfill 复活其中 3 条 github_new）
        # ——「归档→回填→再归档」死循环的源头。归档语义 = 移出检索面，回填也不能穿透。
        if only and r.get("source_id") != only:
            continue
        if not ch.get("enabled"):
            continue                                           # 停用渠道的存量归 kb_prune 处理，不烧回填额度
        if (dead.get(iid) or {}).get("attempts", 0) >= DEAD_AFTER:
            continue                                           # 已判死信，不再消耗额度
        prof = ch.get("profile") or "discussion"
        if not PROFILE_EXPECT.get(prof, {}).get("body"):
            continue                                           # metadata 渠道无正文属预期
        layer = r.get("extra", {}).get("layer") or (
            "signal" if prof == "metadata" else "corpus")
        if body_completeness(r.get("body"), r.get("extra") or {}, layer) == "full":
            continue                                           # 只有「全文」才免除回填
        out.append((r, day))
    out.sort(key=lambda t: (t[0].get("source_id") or "", -(t[0].get("captured_at") or "").__len__()))
    return out


# 结构性无正文：命中即记死信，不必浪费一轮尝试（视频帖 / 账号页 无一可取）
MEDIA_RE = re.compile(r"^https?://(?:[^/]*\.)?(?:v\.redd\.it|youtu\.be|youtube\.com|"
                      r"bilibili\.com/video|vimeo\.com|streamable\.com|\.mp4|\.webm)", re.I)
ACCOUNT_RE = re.compile(r"^https?://(?:[^/]*\.)?(?:twitter\.com|x\.com)/[A-Za-z0-9_]+/?$", re.I)


def structural_dead(r: dict) -> tuple[str, str]:
    """返回 (人话理由, 原因码)；空串=可尝试。"""
    u = body_target(r)
    if MEDIA_RE.search(u):
        return "视频帖无正文", "media"
    if ACCOUNT_RE.search(u):
        return "社交账号页需登录", "account"
    return "", ""


GH_REPO_RE = re.compile(r"^https?://(?:www\.)?github\.com/([^/]+)/([^/#?]+)", re.I)


def github_target(r: dict) -> bool:
    """链接落在 github.com/<owner>/<repo> 上 → 可走 gh api 取 README。

    排除 issues / discussions / 用户主页（不是仓库，取不到 README）。
    """
    m = GH_REPO_RE.match(body_target(r) or "")
    if not m:
        return False
    repo = m.group(2)
    return repo.lower() not in {"issues", "discussions", "pulls", "marketplace", "sponsors", "topics"}


def comments_gap(r: dict) -> str:
    """评论缺口判定：讨论型渠道、且「上次取数报错」或「抓到的少于平台计数」。

    和正文一样是粘性的——条目离开窗口后不会再被 enrich，必须专门回补。

    旧实现要求 `platform >= 20` 才算缺口 —— 于是「平台报 1~18 条评论、实际 0 条入库」
    的条目永远进不了队列（实测 hn_show 121 条：metrics.comments 均值 3.3、最多 18，
    而 comments_total 被写成 0）。评论是痛点/需求分析的主证据，不能整条丢 ——
    宁可用 DEAD_AFTER 兜住确实补不回来的（删帖/无正文评论），也不要在判定阶段就放弃。
    """
    ex = r.get("extra") or {}
    grabbed = len(r.get("comments") or [])
    platform = (r.get("metrics") or {}).get("comments") or 0
    if r.get("comments_truncated"):
        return ""                                              # 已明确标注截断，不算缺口
    if ex.get("comments_error"):
        return f"上次取数失败：{str(ex['comments_error'])[:40]}"
    if ex.get("comments_partial"):
        return f"翻页中断：{str(ex['comments_partial'])[:40]}"
    if platform > grabbed:
        return f"抓取不足 {grabbed}/{platform}"
    return ""


def build_comments_queue(channels: dict, only: str = "") -> list[dict]:
    deadd = load_dead()
    archived = {iid for iid, m in Seen().items.items()
                if str(m.get("note") or "").startswith("80-归档/")}   # 同 build_queue：归档不穿透
    out = []
    for iid, (r, day) in load_latest().items():
        ch = channels.get(r.get("source_id") or "")
        if not ch or (only and r.get("source_id") != only):
            continue
        if iid in archived:
            continue
        if not ch.get("enabled"):
            continue                              # 停用渠道归 kb_prune，不烧回填额度（同 build_queue）
        if (deadd.get(iid) or {}).get("attempts", 0) >= DEAD_AFTER:
            continue
        prof = ch.get("profile") or "discussion"
        if not PROFILE_EXPECT.get(prof, {}).get("comments"):
            continue
        if r.get("source_id") not in ENRICH_ROUTING:
            continue
        why = comments_gap(r)
        if why:
            out.append({"rec": r, "day": day, "why": why})
    return out


def body_target(r: dict) -> str:
    """正文该去哪儿取：外部文章页优先（讨论帖链接帖的正文在外站）。"""
    ex = r.get("extra") or {}
    return (ex.get("fulltext_url") or r.get("project_url") or r.get("url") or "").strip()


def fetch_github_readme(r: dict) -> tuple[str, str]:
    """取仓库 README（走 api.github.com，本机唯一可达的 GitHub 通道）→ (正文, 错误摘要)。

    目标 URL 必须用 `body_target(r)` 取 —— 它优先 `extra.fulltext_url`。
    历史实现写 `r.get("url")`，对 hn_show 这类**转发渠道**来说是 HN 帖子页而不是
    GitHub 仓库页，正则匹配不到 owner/repo → 静默返回空串。于是「URL 路由到 gh」
    这一步会看起来生效、实际一条都取不到（静默空转，最坏的一种 bug）。

    为什么现在要把 stderr 一起带出来：判死需要**结构化证据**（是仓库不存在，还是被限流？）。
    只返回空串 → 所有 gh 失败长得一样 → 只能记一句「未命中」，等于没有理由。
    """
    full = (r.get("extra") or {}).get("full_name")
    if not full:
        m = GH_REPO_RE.match(body_target(r) or "") or \
            re.search(r"github\.com/([^/]+/[^/#?]+)", r.get("url") or "")
        full = m.group(1).replace(".git", "") if m else ""
    if not full:
        return "", "no_repo_in_url"
    code, out, err = run_cli(["gh", "api", f"repos/{full}/readme", "-H",
                              "Accept: application/vnd.github.raw"], timeout=60)
    if code == 0 and out.strip():
        return out.strip()[:60000], ""
    return "", (err or "").strip().replace("\n", " ")[:160] or f"gh rc={code}"


def render_queue_report(queue: list[tuple[dict, str]], dead: dict,
                        cqueue: list[dict] | None = None) -> str:
    """把回填队列落成一页可执行清单。

    为什么要落盘：缺口是**粘性**的（条目离开采集窗口后不会再被自然修复），
    只在终端打印等于每次都要重跑一遍才知道还剩多少。落成报告页后，
    「哪些项目缺正文待回填」变成可复查、可勾掉的台账。

    正文与评论两个队列都列：评论是「痛点/需求」类分析的**主证据**，
    只报正文缺口会让「评论缺口 121 条」长期看不见（实测如此）。
    """
    proj = [(r, d) for r, d in queue if is_project_ish(r)]
    other = [(r, d) for r, d in queue if not is_project_ish(r)]
    L = ["# 回填队列（缺正文 / 缺评论）", "",
         f"- 时间：{iso(now_cst())}",
         f"- 正文缺口：**{len(queue)}**（项目型 {len(proj)} / 非项目 {len(other)}）",
         f"- 结构性死信（视频帖/账号页/极短 README，不再重试）：{len(dead)}",
         ""]
    if cqueue:
        L.append(f"- 评论缺口：**{len(cqueue)}** 条（平台报过评论数、库里评论为空）")
        L.append("")
    L += ["「项目型」= 满足 `is_project_ish()`（kind=project / 有项目外链 / 契约型渠道 / 标题自述自建），",
          "这些是**要保留**的项目，缺的是正文，走本队列回填；",
          "「非项目」= 讨论帖、提问帖、榜单等，不建实体页，正文缺就缺，不影响项目分析。", ""]

    L += ["## 按渠道", "", "| 渠道 | 项目型缺口 | 非项目缺口 |", "|---|---|---|"]
    ch = collections.Counter(r["source_id"] for r, _ in proj)
    ch2 = collections.Counter(r["source_id"] for r, _ in other)
    for k in sorted(set(ch) | set(ch2), key=lambda x: -(ch.get(x, 0) + ch2.get(x, 0))):
        L.append(f"| `{k}` | {ch.get(k, 0)} | {ch2.get(k, 0)} |")

    L += ["", "## 项目型缺口清单", ""]
    for r, _d in sorted(proj, key=lambda x: (x[0]["source_id"], x[0].get("title") or "")):
        t = (r.get("title") or "(无标题)").replace("|", "/")[:90]
        L.append(f"- [{r['source_id']}] {t} —— {body_target(r)[:100]}")

    L += ["", "## 下一步", "",
          "```",
          "python tools/kb_backfill.py --limit 60        # 回填一批（GitHub 走 gh，其余走 Exa/Algolia）",
          "python tools/kb_backfill.py --dry             # 再看还剩多少",
          "python tools/kb_healthcheck.py                # 不变量自检",
          "```"]

    if cqueue:
        L += ["", "## 评论缺口（平台报过评论数、库里为空）", "",
              f"- 合计 **{len(cqueue)}** 条。「痛点 / 需求 / 反对意见」类分析主要读评论区 ——",
              "  缺一条就是整个项目听不到用户声音，故与正文缺口同等对待。",
              "", "| 渠道 | 条数 |", "|---|---|"]
        for k, v in collections.Counter(x["rec"]["source_id"] for x in cqueue).most_common():
            L.append(f"| `{k}` | {v} |")
        L += ["", "样例（前 20）：", ""]
        for x in cqueue[:20]:
            r = x["rec"]
            t = (r.get("title") or "(无标题)").replace("|", "/")[:80]
            L.append(f"- [{r['source_id']}] {t} —— {x['why']}")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=60)
    ap.add_argument("--channel", default="")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--report", action="store_true",
                    help="只生成 00-索引/报告/回填队列.md（不取数、不写死信）")
    ap.add_argument("--only-comments", action="store_true",
                    help="本轮只补评论（正文队列不动）——评论缺口常一次上百条，需要单独控量")
    ap.add_argument("--exa-batch", type=int, default=12, help="每批 Exa 取数条数")
    ap.add_argument("--direct-workers", type=int, default=6,
                    help="直取后端并发数（urllib，零依赖；先用它，拿不到再回退 Exa）")
    ap.add_argument("--revive-github", action="store_true",
                    help="把「目标 URL 指向 github.com 仓库」的死信放出队列重试"
                         "（旧版按 source_id 路由，这类条目根本没走过 gh readme 就被判死）")
    ap.add_argument("--migrate-dead", action="store_true",
                    help="死信账本 schema 1 → 2：补 reason_code / tried[] / http_status（只补齐，不改判定；"
                         "加 --apply 才落盘，落盘前留 .bak）")
    ap.add_argument("--dead-report", action="store_true",
                    help="只生成 00-索引/报告/死信账本.md（按原因码复核判死是否成立）")
    ap.add_argument("--apply", action="store_true", help="--migrate-dead / --revive-code 的落盘开关")
    ap.add_argument("--revive-code", default="",
                    help="按原因码把死信放回队列（逗号分隔，如 no_backend,gh_miss）——"
                         "判据变更后重开旧判定，必须配 --apply 才落盘，带 undo 清单")
    ap.add_argument("--fix-meta", action="store_true",
                    help="回填「该有但没有」的元数据（当前：betalist 发布日，从详情页 Featured 锚点抽）")
    args = ap.parse_args(argv)

    if args.revive_code:
        codes = [c.strip() for c in args.revive_code.split(",") if c.strip()]
        n, manifest, _ids = revive_by_code(codes, apply=args.apply)
        tail = f" → 清单 _meta/{manifest.name}" if manifest else "（dry：加 --apply 落盘）"
        print(f"按原因码复活 {n} 条（{','.join(codes)}）{tail}")
        return 0

    if args.fix_meta:
        reg0 = load_channels_yaml(META / "channels.yaml")
        st = fix_published_at({c["id"]: c for c in (reg0.get("channels") or [])},
                              dry=args.dry, limit=args.limit)
        print(f"元数据回填：候选 {st['candidates']} · 补上 {st['fixed']} · "
              f"抽不到 {st['not_found']} · 写盘失败 {st['errors']}")
        return 0

    if args.dead_report:
        dead = load_dead()
        out = DIR_REPORT / "死信账本.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_dead_report(dead), encoding="utf-8")
        by = collections.Counter((v.get("reason_code") or "unknown") for v in dead.values())
        print(f"死信 {len(dead)} 条（原因码）：" + "、".join(f"{k}={v}" for k, v in by.most_common()))
        print(f"[报告] {out.relative_to(ROOT).as_posix()}")
        return 0

    if args.migrate_dead:
        n, changes = migrate_dead(apply=args.apply)
        head = "已落盘（旧账本备份为 _meta/backfill_dead.schema1.bak-*.json）" if args.apply else "dry（加 --apply 落盘）"
        print(f"schema 升级待改 {n} 条 · {head}")
        for iid, old, new in changes[:10]:
            print(f"  {iid}: {old} → {new}")
        if n > 10:
            print(f"  …另有 {n - 10} 条")
        return 0

    reg = load_channels_yaml(META / "channels.yaml")
    channels = {c["id"]: c for c in (reg.get("channels") or [])}

    if args.revive_github:
        if args.dry or args.report:
            print("[dry] --revive-github 需要真正执行（去掉 --dry/--report）")
            return 0
        revived, manifest = revive_github_dead()
        print(f"复活 github 目标死信 {revived} 条 → 清单 _meta/{manifest.name}")
        if not revived:
            return 0

    queue = build_queue(channels, args.channel)
    if args.only_comments:
        queue = []                                          # 正文缺口本轮不碰
    if not queue and not build_comments_queue(channels, args.channel):
        print("无缺口，跳过")
        return 0

    if queue:
        print(f"缺口 {len(queue)} 条（按渠道）：" +
              "、".join(f"{k}={v}" for k, v in collections.Counter(
                  r["source_id"] for r, _ in queue).most_common()))
    dead = load_dead()
    todo: list[tuple[dict, str]] = []
    struct = 0
    for r, d in queue:
        why, code = structural_dead(r)
        if why:
            rec = dead.setdefault(r["item_id"], {"attempts": DEAD_AFTER, "title": (r.get("title") or "")[:70],
                                                 "url": body_target(r), "source_id": r["source_id"]})
            rec["reason"] = why
            rec["reason_code"] = code
            rec.setdefault("first_dead", rec.get("last_try") or iso(now_cst()))
            rec["last_try"] = iso(now_cst())
            rec.setdefault("http_status", None)
            rec.setdefault("tried", [])
            struct += 1
            continue
        if len(todo) < args.limit:
            todo.append((r, d))
    if struct:
        if not (args.dry or args.report):      # dry / report 是只读模式，不许改死信台账
            save_dead(dead)
        print(f"  结构性无正文 {struct} 条{'已记死信' if not (args.dry or args.report) else '（只读，未记账）'}"
              f"（视频帖/账号页），不再重试")
    if args.report:
        out = DIR_REPORT / "回填队列.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        cq = build_comments_queue(channels, args.channel)
        out.write_text(render_queue_report(queue, dead, cq), encoding="utf-8")
        print(f"[报告] {out.relative_to(ROOT).as_posix()}")
        return 0
    if args.dry:
        for r, day in todo:
            print(f"  [{r['source_id']:14s}] {r.get('title', '')[:60]} → {body_target(r)[:90]}")
        return 0

    run_id = "backfill-" + now_cst().strftime("%Y%m%d-%H%M%S")
    seen = Seen()
    body_cache = BodyCache()
    day_now = now_cst().strftime("%Y-%m-%d")

    # ① GitHub 单独走 gh（并发 4，比 Exa 准且不花额度）
    #
    # 路由键必须是 **URL 主机**，不是 source_id。旧实现按 `source_id == "github_new"`
    # 分流，于是「非 github_new 渠道、但链接指向 github.com」的条目全部落到 exa_items：
    #   hn_show 里指向 github 的条目 → direct_fetch 被 DIRECT_BLOCKED_HOSTS 拦 →
    #   Exa 也拿不到（repo 站正文在 README 里，不在渲染页上）→ 记死信。
    # 实测代价：死信账本 270 条里 66 条是 github.com；而 fetch_github_readme 本身
    # **早就支持从 URL 反推 owner/repo**，只是这些条目根本没被路由进 gh_items。
    # 这是纯路由缺陷，不是能力缺陷。
    gh_items = [(r, d) for r, d in todo
                if r["source_id"] == "github_new" or github_target(r)]
    exa_items = [(r, d) for r, d in todo
                 if r["source_id"] != "github_new" and not github_target(r)]

    results: dict[str, dict] = {}
    tried_by_item: dict[str, list[str]] = {}          # 每条实际试过的后端（判死理由的结构化依据）
    gh_err_by_item: dict[str, str] = {}
    status_by_url: dict[str, int | str] = {}

    def mark(iid: str, backend: str) -> None:
        t = tried_by_item.setdefault(iid, [])
        if backend not in t:
            t.append(backend)

    if gh_items:
        from concurrent.futures import ThreadPoolExecutor

        def one(pair):
            r, day = pair
            try:
                txt, err = fetch_github_readme(r)
            except Exception as e:                                 # noqa: BLE001
                print(f"    [!] readme 失败 {r.get('title', '')[:40]}: {str(e)[:60]}")
                return (r, day, "", str(e)[:120])
            return (r, day, txt, err)

        with ThreadPoolExecutor(4) as ex:
            for res in ex.map(one, gh_items):
                r, day, txt, err = res
                mark(r["item_id"], "gh_readme")
                if txt:
                    results[r["item_id"]] = {"rec": r, "day": day, "body": txt,
                                             "via": "gh_readme", "url": body_target(r)}
                elif err:
                    gh_err_by_item[r["item_id"]] = err
        print(f"  github readme 命中 "
              f"{sum(1 for r, _ in gh_items if r['item_id'] in results)}/{len(gh_items)}")

    # ①.5 gh 没拿到的 github 目标 → **仍要跑完 direct + exa 两档**，才算「判死前跑完三档」。
    #     旧实现把它们排除在 exa_items 之外：gh 失败即判死，理由是「已试 gh_readme」，
    #     而 exa 可能拿到 repo 的渲染页。判死的前提是**每档都真试过**，不是「路由到哪档算哪档」。
    pending_all = exa_items + [(r, d) for r, d in gh_items if r["item_id"] not in results]

    # ② 其余：先直取（零依赖、无额度），直取拿不到再回退 Exa
    #    为什么改顺序：2026-09-21 实测 Exa 免费额度打满返 429，534 条 hn_show 缺正文全部无法回填，
    #    而**直连 urllib 对 project_url 是通的**（6/6 命中，7k~21k 字符）。Exa 从「唯一后端」
    #    降级为「兜底后端」。
    if pending_all:
        pending = [(r, d) for r, d in pending_all if body_target(r)]
        got_all: dict[str, dict] = {}
        all_urls = list(dict.fromkeys(body_target(r) for r, _ in pending if body_target(r)))
        for r, _ in pending:
            mark(r["item_id"], "direct_fetch")
        try:
            direct = direct_fetch_texts(all_urls, max_chars=FULLTEXT_MAX_CHARS,
                                        workers=args.direct_workers, status_out=status_by_url)
            print(f"    [i] 直取命中 {len(direct)}/{len(all_urls)}", flush=True)
        except Exception as e:                                     # noqa: BLE001
            print(f"    [w] 直取批次失败：{str(e)[:70]}")
            direct = {}
        for u, t in direct.items():
            got_all[u] = {"txt": t, "via": "direct_fetch"}
        # 直取没拿到的 → 回退 Exa（批量，仍可能 429；429 会被 kb_common 响亮报出）
        rest = [u for u in all_urls if u not in got_all]
        if rest:
            for r, _ in pending:
                if body_target(r) in rest:
                    mark(r["item_id"], "exa_web_fetch")
        for i in range(0, len(rest), args.exa_batch):
            chunk = rest[i:i + args.exa_batch]
            try:
                # max_chars 与 kb_collect 保持一致：8000 会把长文拦腰砍断且不留痕迹，
                # 正是内容审计里那 17 条「刚好 8000 字」的来源。
                got = exa_fetch_texts(chunk, max_chars=FULLTEXT_MAX_CHARS)
            except Exception as e:                                 # noqa: BLE001
                print(f"    [w] exa 批次失败：{str(e)[:70]}")
                continue
            for u, t in got.items():
                got_all.setdefault(u, {"txt": t, "via": "exa_web_fetch"})
            print(f"    [i] exa 批次 {i // args.exa_batch + 1}：{len(got)}/{len(chunk)}", flush=True)
        for r, day in pending:
            u = body_target(r)
            hit = got_all.get(u) or got_all.get(norm_url(u))
            txt = (hit or {}).get("txt", "")
            # 只在**确有改善**时接受：本次抓到的一定要比现有的长，
            # 否则「摘要在前、摘要在后」会无限重排，条目永远清不出队列直到记死信。
            if txt and len(txt) >= BODY_MIN and len(txt) > len(r.get("body") or ""):
                results[r["item_id"]] = {"rec": r, "day": day, "body": txt[:FULLTEXT_MAX_CHARS],
                                         "via": (hit or {}).get("via", "unknown"), "url": u}

    # ③ 写盘：raw 追加 + note 原地刷新 + seen 指纹更新
    wrote = 0
    for iid, res in results.items():
        r, day, body = res["rec"], res["day"], res["body"]
        rec = dict(r)
        rec["body"] = body
        rec["body_format"] = "markdown"
        rec["extra"] = dict(rec.get("extra") or {})
        rec["extra"]["body_source"] = res["via"]
        rec["extra"]["body_url"] = res["url"]
        # 截断必须留痕（硬约束②）：回填同样吃 FULLTEXT_MAX_CHARS 上限，
        # 命中上限说明原文更长 —— 之前这里只切片不标记，实测 9 条 40000 字长文因此「静默截断」。
        if len(body) >= FULLTEXT_MAX_CHARS - 60:
            rec["extra"]["body_truncated"] = True
        else:
            rec["extra"].pop("body_truncated", None)
        rec["captured_at"] = iso(now_cst())
        rec["record_type"] = "backfill"
        rec["run_id"] = run_id
        # 派生字段必须重算：raw 里的 body_completeness 是「采集那一刻」算的，
        # 回填只改 body 不重算 → 标着 empty 却躺着 4000 字正文（实测 270 条），
        # 而 AI 批量读的就是这份 JSONL。回填是唯一改 body 的路径，就地重算。
        rec["body_completeness"] = body_completeness(
            rec.get("body"), rec["extra"], rec["extra"].get("layer") or "corpus")
        try:
            append_jsonl(DIR_RAW / r["source_id"] / f"{day_now}.jsonl", [rec])
            p = write_corpus_note(rec, note_bucket(seen, iid, day))   # 原地刷新，不迁移分片
            rel = p.relative_to(ROOT).as_posix()
            # 准入必须与 kb_collect 同一判据：kb_backfill 原先无条件调 write_entity_note，
            # 实测把 44 条 reddit 讨论帖（kind=post）写进了 10-项目/ → 检索面污染。
            # 语料页照写（讨论帖是好语料），实体页只给真项目 / person / method。
            if is_project_ish(rec) or (rec.get("kind") or "").lower() in ("person", "method"):
                write_entity_note(rec, rel)
            h = sha1(json.dumps({"b": rec.get("body") or "", "c": rec.get("comments") or [],
                                 "m": rec.get("metrics") or {}}, ensure_ascii=False, sort_keys=True))
            seen.touch(iid, r["source_id"], rel, None, content_hash=h)
            body_cache.put(iid, body, res["via"], res["url"], "markdown")   # 写缓存，防下轮被空 body 抹掉
            wrote += 1
        except Exception as e:                                     # noqa: BLE001
            print(f"    [!] 写盘失败 {iid}: {str(e)[:70]}")
    seen.save()
    body_cache.save()

    # ④ 评论回填：复用各渠道 enrich 函数（条目离开窗口后评论同样不会再被补）
    cq = build_comments_queue(channels, args.channel)
    cwrote = 0
    if cq:
        print(f"  评论缺口 {len(cq)} 条：" + "、".join(
            f"{k}={v}" for k, v in collections.Counter(x["rec"]["source_id"] for x in cq).most_common()))
    for item in cq[: args.limit]:
        r, day = item["rec"], item["day"]
        enr = ENRICH_ROUTING.get(r["source_id"])
        if not enr:
            continue
        rec = dict(r)
        rec["extra"] = dict(rec.get("extra") or {})
        rec["extra"].pop("comments_error", None)
        rec["extra"].pop("comments_partial", None)
        before = len(rec.get("comments") or [])
        try:
            enr[1]([rec], {"max_comments": MAX_COMMENTS, "fulltext_budget": 1})
        except Exception as e:                                     # noqa: BLE001
            print(f"    [!] 评论回填失败 {str(r.get('title') or '')[:40]}: {str(e)[:60]}")
            continue
        # 数量没涨但错误标志已消除，也要落盘——否则「翻页中断」标记会永远挂着
        ok_now = not rec["extra"].get("comments_error") and not rec["extra"].get("comments_partial")
        if len(rec.get("comments") or []) <= before and not (ok_now and before > 0):
            continue
        rec["captured_at"] = iso(now_cst())
        rec["record_type"] = "backfill"
        rec["run_id"] = run_id
        rec["body_completeness"] = body_completeness(          # 同上：改了 body/评论就要重算
            rec.get("body"), rec["extra"], rec["extra"].get("layer") or "corpus")
        try:
            append_jsonl(DIR_RAW / r["source_id"] / f"{day_now}.jsonl", [rec])
            p = write_corpus_note(rec, note_bucket(seen, r["item_id"], day))   # 原地刷新
            rel = p.relative_to(ROOT).as_posix()
            if is_project_ish(rec) or (rec.get("kind") or "").lower() in ("person", "method"):
                write_entity_note(rec, rel)                        # 同上：实体页准入
            h = sha1(json.dumps({"b": rec.get("body") or "", "c": rec.get("comments") or [],
                                 "m": rec.get("metrics") or {}}, ensure_ascii=False, sort_keys=True))
            seen.touch(r["item_id"], r["source_id"], rel, None, content_hash=h)
            cwrote += 1
        except Exception as e:                                     # noqa: BLE001
            print(f"    [!] 评论写盘失败 {r['item_id']}: {str(e)[:60]}")
    if cq:
        seen.save()
        print(f"  评论回填完成：{cwrote}/{min(len(cq), args.limit)}")

    # ③ 尝试过但没取到的 → 记 attempts，连试 DEAD_AFTER 轮后进死信
    miss = 0
    for r, day in todo:
        if r["item_id"] in results:
            continue
        rec = dead.setdefault(r["item_id"], {"attempts": 0, "title": (r.get("title") or "")[:70],
                                             "url": body_target(r), "source_id": r["source_id"],
                                             "first_dead": iso(now_cst())})
        rec["attempts"] = rec.get("attempts", 0) + 1
        rec["last_try"] = iso(now_cst())
        tried = tried_by_item.get(r["item_id"]) or ["direct_fetch"]
        rec["tried"] = tried
        u = body_target(r)
        status = status_by_url.get(u)
        rec["http_status"] = status if isinstance(status, int) else status
        code = classify_reason(u, status=status, tried=tried,
                               gh_err=gh_err_by_item.get(r["item_id"], ""))
        rec["reason_code"] = code
        # 人话理由必须与结构化字段**同步刷新**，否则会出现「reason 说已试 gh、tried 说试了
        # 三档」这种自相矛盾的账（实测踩过：复活条目 attempts 已 ≥2，旧实现只在首判时写 reason
        # → 结构化证据是新的、人话是老的，看账的人被引回错误归因）。
        # 审计线索不丢：首判原文转存 `reason_first`，只写一次。
        if rec.get("reason") and "reason_first" not in rec:
            rec["reason_first"] = rec["reason"]
        rec["reason"] = (f"取数失败（已试 {'→'.join(tried)}）· 判定 {code}"
                         + (f" · status={status}" if status is not None else "")
                         + (f" · gh: {gh_err_by_item[r['item_id']][:80]}"
                            if r["item_id"] in gh_err_by_item else ""))
        miss += 1
    save_dead(dead)

    write_ledger(META / "runs" / f"{run_id}.json",
        {"run_id": run_id, "kind": "backfill", "queue": len(queue), "attempted": len(todo),
         "filled": wrote, "structural_dead": struct, "missed": miss,
         "miss_reason_codes": dict(collections.Counter(
             (dead.get(r["item_id"]) or {}).get("reason_code") or "unknown"
             for r, _ in todo if r["item_id"] not in results).most_common()),
         "status_hist": dict(collections.Counter(
             str(v) for v in status_by_url.values()).most_common()),
         "comments_queue": len(cq), "comments_filled": cwrote,
         "via": collections.Counter(v["via"] for v in results.values()).most_common(),
         "channels": collections.Counter(v["rec"]["source_id"] for v in results.values()).most_common(),
         "started": iso(now_cst()), "elapsed_s": 0}, lock_name="runs", indent=1)
    rotate_runs()                                              # 运行记录轮转（保 80 份）
    miss_codes = collections.Counter(
        (dead.get(r["item_id"]) or {}).get("reason_code") or "unknown"
        for r, _ in todo if r["item_id"] not in results)
    print(f"回填完成：{wrote}/{len(todo)}（队列 {len(queue)}）· 缺失 {miss} 条已记 attempts"
          + ("（" + "、".join(f"{k}={v}" for k, v in miss_codes.most_common()) + "）" if miss else "")
          + f" · 账本累计 {len(dead)} 条（已判死 "
            f"{sum(1 for v in dead.values() if v.get('attempts', 0) >= DEAD_AFTER)}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
