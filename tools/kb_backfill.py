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
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import (BODY_MIN, DIR_RAW, DIR_REPORT, FULLTEXT_MAX_CHARS, META,  # noqa: E402
                       ROOT, BodyCache, Seen, append_jsonl, body_completeness,
                       exa_fetch_texts, iso, norm_url, now_cst, rotate_runs, run_cli, sha1)
from kb_collect import (ENRICH_ROUTING, MAX_COMMENTS, is_project_ish,  # noqa: E402
                        load_channels_yaml, write_corpus_note, write_entity_note)
from kb_analyze import PROFILE_EXPECT  # noqa: E402

DEAD_LEDGER = META / "backfill_dead.json"
DEAD_AFTER = 2          # 同一缺口连试 N 轮仍取不到 → 判「结构性不可得」，不再重试


def load_dead() -> dict:
    try:
        return json.loads(DEAD_LEDGER.read_text(encoding="utf-8")).get("items") or {}
    except Exception:                                              # noqa: BLE001
        return {}


def save_dead(d: dict) -> None:
    DEAD_LEDGER.write_text(json.dumps(
        {"updated": iso(now_cst()), "note": "结构性无正文（视频帖/Twitter 账号页/极短 README/反爬站）——"
                                          "连试 %d 轮后记账，不再消耗额度" % DEAD_AFTER,
         "items": d}, ensure_ascii=False, indent=1), encoding="utf-8")


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
    out = []
    for iid, (r, day) in load_latest().items():
        ch = channels.get(r.get("source_id") or "")
        if not ch:
            continue
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


def structural_dead(r: dict) -> str:
    """返回结构性原因（空串=可尝试）。"""
    u = body_target(r)
    if MEDIA_RE.search(u):
        return "视频帖无正文"
    if ACCOUNT_RE.search(u):
        return "社交账号页需登录"
    return ""


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
    out = []
    for iid, (r, day) in load_latest().items():
        ch = channels.get(r.get("source_id") or "")
        if not ch or (only and r.get("source_id") != only):
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


def fetch_github_readme(r: dict) -> str:
    full = (r.get("extra") or {}).get("full_name")
    if not full:
        m = re.search(r"github\.com/([^/]+/[^/#?]+)", r.get("url") or "")
        full = m.group(1).replace(".git", "") if m else ""
    if not full:
        return ""
    code, out, _ = run_cli(["gh", "api", f"repos/{full}/readme", "-H",
                            "Accept: application/vnd.github.raw"], timeout=60)
    return out.strip()[:60000] if code == 0 else ""


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
    args = ap.parse_args(argv)

    reg = load_channels_yaml(META / "channels.yaml")
    channels = {c["id"]: c for c in (reg.get("channels") or [])}
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
        why = structural_dead(r)
        if why:
            rec = dead.setdefault(r["item_id"], {"attempts": DEAD_AFTER, "title": (r.get("title") or "")[:70],
                                                 "url": body_target(r), "source_id": r["source_id"]})
            rec["reason"] = why
            rec["last_try"] = iso(now_cst())
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
    gh_items = [(r, d) for r, d in todo if r["source_id"] == "github_new"]
    exa_items = [(r, d) for r, d in todo if r["source_id"] != "github_new"]

    results: dict[str, dict] = {}

    if gh_items:
        from concurrent.futures import ThreadPoolExecutor

        def one(pair):
            r, day = pair
            try:
                txt = fetch_github_readme(r)
            except Exception as e:                                 # noqa: BLE001
                print(f"    [!] readme 失败 {r.get('title', '')[:40]}: {str(e)[:60]}")
                return None
            return (r, day, txt)

        with ThreadPoolExecutor(4) as ex:
            for res in ex.map(one, gh_items):
                if res and res[2]:
                    r, day, txt = res
                    results[r["item_id"]] = {"rec": r, "day": day, "body": txt,
                                             "via": "gh_readme", "url": r.get("url")}
        print(f"  github readme 命中 {len(results)}/{len(gh_items)}")

    # ② 其余走 Exa 批量取正文
    if exa_items:
        pending = [(r, d) for r, d in exa_items if body_target(r)]
        got_all: dict[str, str] = {}
        for i in range(0, len(pending), args.exa_batch):
            batch = pending[i:i + args.exa_batch]
            urls = list(dict.fromkeys(body_target(r) for r, _ in batch if body_target(r)))
            if not urls:
                continue
            try:
                # max_chars 与 kb_collect 保持一致：8000 会把长文拦腰砍断且不留痕迹，
                # 正是内容审计里那 17 条「刚好 8000 字」的来源。
                got = exa_fetch_texts(urls, max_chars=FULLTEXT_MAX_CHARS)
            except Exception as e:                                 # noqa: BLE001
                print(f"    [w] exa 批次失败：{str(e)[:70]}")
                continue
            got_all.update(got)
            print(f"    [i] exa 批次 {i // args.exa_batch + 1}：{len(got)}/{len(urls)}")
        for r, day in pending:
            u = body_target(r)
            txt = got_all.get(u) or got_all.get(norm_url(u))
            # 只在**确有改善**时接受：本次抓到的一定要比现有的长，
            # 否则「摘要在前、摘要在后」会无限重排，条目永远清不出队列直到记死信。
            if txt and len(txt) >= BODY_MIN and len(txt) > len(r.get("body") or ""):
                results[r["item_id"]] = {"rec": r, "day": day, "body": txt[:FULLTEXT_MAX_CHARS],
                                         "via": "exa_web_fetch", "url": u}

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
            p = write_corpus_note(rec, day)              # 用原分片日期 → 原地刷新，不新建
            rel = p.relative_to(ROOT).as_posix()
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
            p = write_corpus_note(rec, day)
            rel = p.relative_to(ROOT).as_posix()
            write_entity_note(rec, rel)
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
                                             "url": body_target(r), "source_id": r["source_id"]})
        rec["attempts"] = rec.get("attempts", 0) + 1
        rec["last_try"] = iso(now_cst())
        rec["reason"] = rec.get("reason") or "取数失败（Exa 未命中该站）"
        miss += 1
    save_dead(dead)

    (META / "runs" / f"{run_id}.json").write_text(json.dumps(
        {"run_id": run_id, "kind": "backfill", "queue": len(queue), "attempted": len(todo),
         "filled": wrote, "structural_dead": struct, "missed": miss,
         "comments_queue": len(cq), "comments_filled": cwrote,
         "via": collections.Counter(v["via"] for v in results.values()).most_common(),
         "channels": collections.Counter(v["rec"]["source_id"] for v in results.values()).most_common(),
         "started": iso(now_cst()), "elapsed_s": 0}, ensure_ascii=False, indent=1), encoding="utf-8")
    rotate_runs()                                              # 运行记录轮转（保 80 份）
    print(f"回填完成：{wrote}/{len(todo)}（队列 {len(queue)}）· 缺失 {miss} 条已记 attempts · "
          f"账本累计 {len(dead)} 条（已判死 {sum(1 for v in dead.values() if v.get('attempts', 0) >= DEAD_AFTER)}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
