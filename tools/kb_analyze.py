"""kb_analyze — 语料/管线诊断器（每轮采集后跑，产出可执行优化清单）。

只看数据说话，不猜。输出：
  1) 控制台摘要
  2) 00-索引/报告/分析-<run_id>.md  （含优化建议，供下一轮改代码/注册表）

用法：
  python tools/kb_analyze.py                 # 分析全部历史
  python tools/kb_analyze.py --run <run_id>  # 只看某一轮的新增/更新
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import (BODY_MIN, DIR_RAW, DIR_REPORT, META, RUNS, iso,  # noqa: E402
                       load_ndjson, now_cst, pub_day_of, write_note)
from kb_collect import load_channels_yaml  # noqa: E402

# 渠道画像 → 该渠道「应当具备什么」的期望。QA 阈值由此推导，不再拍脑袋。
#   discussion  讨论帖：应有正文 + 平台评论
#   linkpost    发布/外链：正文可能在外站（fulltext_url），无平台评论系统
#   project     项目实体：应有正文（README/介绍）+ 自身 project_url
#   metadata    榜单/目录：只有元数据，不期望正文与评论
#   discover    语义发现：应有正文，但无评论、可能无独立项目链接
PROFILE_EXPECT = {
    "discussion": {"body": True,  "comments": True,  "project_url": False, "published_at": True},
    "linkpost":   {"body": True,  "comments": False, "project_url": False, "published_at": True},
    "project":    {"body": True,  "comments": False, "project_url": True,  "published_at": True},
    "metadata":   {"body": False, "comments": False, "project_url": False, "published_at": False},
    "discover":   {"body": True,  "comments": False, "project_url": False, "published_at": True},
}

# 元数据契约门（B2）——「该有但没有」与「按契约没有」必须分开。
#
# 为什么必须做成门而不是「看着缺就补」：`published_at` 是时间轴（`pub_day` / 趋势分析）的
# 分组键。实测 135 条缺发布日（betalist 56 / IH 43 / apple_rss 18 / c1c7 17 / 小红书 1），
# 其中 apple_rss 是 profile=metadata（按契约没有），c1c7 是 README 名录（结构上没有），
# 而 betalist 是**我们没去详情页取** —— 三类混在一个数字里，既不能定责也不能定修法。
# 论文侧同向印证（SARC-DQ, arXiv 2607.26313）：agent 无法怀疑它看不见的数据，
# 缺陷必须由「声明的契约」而不是「期望模型自己发现」来暴露。
META_FIELDS = ("published_at", "author", "project_url")


DEAD_LEDGER = META / "backfill_dead.json"


def _load_dead() -> dict:
    """死信账本：结构性无正文（视频帖/账号页/极短 README/反爬站）连试 2 轮后记账，不再计入待办。"""
    try:
        return json.loads(DEAD_LEDGER.read_text(encoding="utf-8")).get("items") or {}
    except Exception:                                              # noqa: BLE001
        return {}


def load_profiles() -> dict[str, str]:
    """从注册表读 channel_id → profile（含 disabled，便于历史数据仍可按画像判定）。"""
    try:
        reg = load_channels_yaml(META / "channels.yaml")
    except Exception:                                              # noqa: BLE001
        return {}
    return {c["id"]: (c.get("profile") or "discussion") for c in (reg.get("channels") or [])}


def load_meta_unavailable() -> dict[str, dict]:
    """从注册表读 channel_id → {字段: 不可得原因}（`meta_unavailable` 段）。

    这一段的唯一作用：把「按契约没有」从「该有但没抓到」里剥离出来 —— 没有它，
    两个数字混在一起，既无法定责，也无法判断哪一类该动手。
    """
    try:
        reg = load_channels_yaml(META / "channels.yaml")
    except Exception:                                              # noqa: BLE001
        return {}
    out = {}
    for c in (reg.get("channels") or []):
        u = c.get("meta_unavailable")
        if isinstance(u, dict):
            out[c["id"]] = u
    return out

NOISE_RE = re.compile(r"removed by moderator|\[removed\]|\[deleted\]|\[已删除\]", re.I)
MONEY_RE = re.compile(r"\$\s?\d[\d,\.]*\s?[kKmM]?|MRR|ARR|月入|收入|营收")
LINKTITLE_RE = re.compile(r"^https?://")


def _is_collect_run(p: Path) -> bool:
    """采集轮 vs 维护轮（backfill/reclassify）：后者没有 total_items。"""
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:                                              # noqa: BLE001
        return False
    return d.get("total_items") is not None or (d.get("kind") in (None, "collect"))


def load_records() -> list[dict]:
    rows = []
    # 读 JSONL 走 load_ndjson()（按 \n 切 + 显式关文件）：裸 open() 迭代会漏掉
    # ResourceWarning，splitlines() 则会按 U+2028 切碎记录后静默丢条。
    for f in sorted(DIR_RAW.glob("*/*.jsonl")):
        rows.extend(load_ndjson(f))
    return rows


def latest_by_item(rows: list[dict]) -> dict[str, dict]:
    """按 captured_at 取每个 item 的最新记录。"""
    lat: dict[str, dict] = {}
    for r in rows:
        cur = lat.get(r["item_id"])
        if cur is None or (r.get("captured_at") or "") >= (cur.get("captured_at") or ""):
            lat[r["item_id"]] = r
    return lat


_LIVE: dict = {"off": None, "archived": None}


def _is_live(r: dict) -> bool:
    """条目当前是否仍在库可消费（未归档、且渠道未停用）。

    口径必须与 kb_content_audit 的 load_latest(live_only=True) 一致，
    否则同一个库会出现两个「唯一语料」数字（实测本工具 801 vs 审计 700）。
    """
    if _LIVE["off"] is None:
        try:
            from kb_content_audit import archived_ids, disabled_channels
            _LIVE["off"] = disabled_channels()
            _LIVE["archived"] = archived_ids()
        except Exception:                                          # noqa: BLE001
            _LIVE["off"], _LIVE["archived"] = set(), set()
    return (r.get("source_id") not in _LIVE["off"]
            and r.get("item_id") not in _LIVE["archived"])


def analyze(round_run: str | None = None) -> dict:
    rows = load_records()
    lat = latest_by_item(rows)
    items = list(lat.values())
    profiles = load_profiles()
    rep_profiles = profiles

    this_round = [r for r in rows if round_run and r.get("run_id") == round_run]
    # 两个口径分开报，避免与 kb_content_audit 的「在库语料」互相打架：
    #   unique_items     = 历史累计条目（含已归档/停用渠道）——「历史上抓过多少」
    #   live_items       = 在库可消费条目 ——「现在能用来分析的还剩多少」
    # 之前只报前者，于是本工具报 801、内容审计报 700，同一个库两个数（实测踩过）。
    live = [r for r in items if _is_live(r)]
    rep: dict = {"total_records": len(rows), "unique_items": len(items),
                 "live_items": len(live),
                 "archived_or_disabled": len(items) - len(live)}
    rep["round"] = {
        "run_id": round_run,
        "records": len(this_round),
        "new": sum(1 for r in this_round if r.get("record_type") == "new"),
        "update": sum(1 for r in this_round if r.get("record_type") == "update"),
    } if round_run else None

    # 渠道维度
    by = collections.defaultdict(lambda: {"n": 0, "body": 0, "body_len": [], "with_comments": 0,
                                          "expect_comments": 0,
                                          "comments": 0, "platform_comments": 0, "trunc": 0,
                                          "no_project_url": 0, "no_author": 0, "profile": "discussion",
                                          "err_body": 0, "err_comments": 0, "partial": 0})
    for it in items:
        d = by[it["source_id"]]
        d["profile"] = profiles.get(it["source_id"], "discussion")
        ex = it.get("extra") or {}
        bl = len(it.get("body") or "")
        d["n"] += 1
        d["body"] += 1 if bl >= BODY_MIN else 0
        d["body_len"].append(bl)
        if it.get("comments"):
            d["with_comments"] += 1
        # 应有评论 = 平台自己报过评论数的条目（>0）。它与「抓到多少条评论」是两回事：
        #   覆盖  = 有评论条目 / 应有评论条目 —— 多少条目的用户声音真的入库了
        #   抓取深度 = 抓到条数 / 平台条数     —— 只在「抓到过」的条目里算
        # 只报后者会骗人：实测 hn_show 抓取深度 78%，而 400 条里只有 31 条带评论。
        if ((it.get("metrics") or {}).get("comments") or 0) > 0:
            d["expect_comments"] += 1
        d["comments"] += len(it.get("comments") or [])
        d["platform_comments"] += (it.get("metrics") or {}).get("comments") or 0
        d["trunc"] += 1 if it.get("comments_truncated") else 0
        d["no_project_url"] += 0 if it.get("project_url") else 1
        d["no_author"] += 0 if it.get("author") else 1
        # 取数错误必须可见：静默失败比失败本身更贵（R3 实测 dev.to 大帖评论被静默截断）
        d["err_body"] += 1 if ex.get("body_error") else 0
        d["err_comments"] += 1 if ex.get("comments_error") else 0
        d["partial"] += 1 if ex.get("comments_partial") else 0
    rep["by_channel"] = by

    # 缺口清单（按画像判定）：可被 kb_backfill.py 直接消费
    dead = _load_dead()
    gaps: list[dict] = []
    absent: list[dict] = []                                     # 契约型「本该没有正文」的明账
    dead_cnt = 0
    for it in items:
        prof = profiles.get(it["source_id"], "discussion")
        exp = PROFILE_EXPECT.get(prof, PROFILE_EXPECT["discussion"])
        miss = []
        if exp["body"] and len(it.get("body") or "") < BODY_MIN:
            miss.append("body")
        elif not exp["body"] and len(it.get("body") or "") < BODY_MIN:
            # 该 profile 声明「本渠道不产出正文」（metadata / signal 层）→ 不是缺口。
            # 但必须**入账**，不能只是 `continue` 掉：那样这些条目既不在回填队列、也不在
            # 死信账本，成为「账外条目」——审计时无法区分「已判废」与「还没试过」。
            # 实测 55 条（bilibili 31 / apple_rss 18 / sspai 6）长期悬空，正是这个原因。
            absent.append({"item_id": it["item_id"], "source_id": it["source_id"],
                           "profile": prof, "url": it.get("url"),
                           "title": (it.get("title") or "")[:80]})
            continue
        if exp["project_url"] and not it.get("project_url"):
            miss.append("project_url")
        if not miss:
            continue
        if (dead.get(it["item_id"]) or {}).get("attempts", 0) >= 2:
            dead_cnt += 1                                       # 结构性不可得，不再计入待办
            continue
        gaps.append({"item_id": it["item_id"], "source_id": it["source_id"], "profile": prof,
                     "missing": miss, "url": it.get("project_url") or it.get("url"),
                     "page": it.get("url"), "title": (it.get("title") or "")[:80]})
    rep["gaps"] = gaps
    rep["gap_dead"] = dead_cnt
    rep["expected_absent"] = absent
    rep["expected_absent_by_channel"] = collections.Counter(
        a["source_id"] for a in absent).most_common()
    rep["gap_by_channel"] = collections.Counter(
        (g["source_id"], ",".join(g["missing"])) for g in gaps).most_common()
    rep["profiles"] = profiles

    # ---- 元数据契约门（B2）：字段级「该有但没有」 vs 「按契约没有」
    #
    # 与 §缺口清单 的分工：缺口清单管**正文/评论**（内容侧，能回填）；本段管**元数据**
    # （描述侧，回填成本高、且错填比缺更贵）。两者都属「取数诊断」，都不含相关性判断。
    unavail = load_meta_unavailable()
    meta_defects: dict[tuple[str, str], int] = collections.Counter()
    meta_exempt: dict[tuple[str, str], int] = collections.Counter()
    meta_detail: list[dict] = []
    for it in live:
        cid = it["source_id"]
        prof = profiles.get(cid, "discussion")
        exp = PROFILE_EXPECT.get(prof, PROFILE_EXPECT["discussion"])
        exc = unavail.get(cid) or {}
        # 语义短路：person / method 条目的「项目外链」缺失不是缺陷 —— 它们本来就不是项目
        # （判据必须与 kb_common.is_project_ish 的语义短路一致，否则会报 3 条假缺陷）。
        semantic = (it.get("kind") or "").lower() in ("person", "method")
        for f in META_FIELDS:
            if not exp.get(f):
                continue
            if f == "project_url" and semantic:
                continue
            have = bool(it.get(f)) if f != "published_at" else bool(pub_day_of(it.get(f)))
            if have:
                continue
            if f in exc:
                meta_exempt[(cid, f)] += 1
            else:
                meta_defects[(cid, f)] += 1
                meta_detail.append({"item_id": it["item_id"], "source_id": cid, "field": f,
                                    "url": it.get("url"), "title": (it.get("title") or "")[:80]})
    rep["meta_defects"] = meta_detail
    rep["meta_defects_by_channel"] = meta_defects.most_common()
    rep["meta_exempt_by_channel"] = meta_exempt.most_common()
    rep["meta_unavailable_declared"] = unavail

    # 噪声 / 语言 / 收入信号
    rep["noise"] = [{"source": r["source_id"], "title": r["title"][:70], "url": r["url"]}
                    for r in items if NOISE_RE.search(f"{r['title']} {r.get('body') or ''}")][:30]
    rep["lang"] = collections.Counter(r.get("lang") or "?" for r in items).most_common()
    rep["money_signal"] = sum(1 for r in items if MONEY_RE.search(f"{r['title']} {r.get('body') or ''}"))
    rep["no_url"] = sum(1 for r in items if not (r.get("url") or "").strip())
    rep["body_missing"] = collections.Counter(r["source_id"] for r in items
                                             if len(r.get("body") or "") < 120).most_common()

    # 项目页幂等性：同一 project_url / 同名是否生成多个 note
    proj_notes = list(Path("10-项目").glob("*.md"))
    keys = collections.Counter()
    for r in items:
        keys[(r.get("project_url") or r["url"]).lower()] += 1
    rep["project_notes"] = len(proj_notes)
    rep["project_dup_keys"] = [(k, v) for k, v in keys.items() if v > 1][:10]

    # 最新一轮的运行状态
    runs = sorted(RUNS.glob("*.json"))
    if runs:
        last = json.loads(runs[-1].read_text(encoding="utf-8"))
        rep["last_run"] = {"run_id": last.get("run_id"), "elapsed_s": last.get("elapsed_s"),
                           "channels": [{"id": c["source_id"], "status": c["status"], "count": c["count"],
                                         "elapsed_s": c["elapsed_s"], "new": c.get("new")}
                                        for c in last.get("channels") or []],
                           "errors": last.get("errors") or []}
    return rep


def render(rep: dict) -> str:
    L = ["# 语料/管线诊断", "",
         f"> 生成 {iso(now_cst())} · 分析器 `tools/kb_analyze.py`", "",
         f"- 原始记录（含历次 update）**{rep['total_records']}** 条 · 唯一条目（累计）**{rep['unique_items']}** 条 "
         f"· **在库可消费 {rep.get('live_items', rep['unique_items'])} 条**"
         f"（归档/停用 {rep.get('archived_or_disabled', 0)} 条）",
         f"- 缺 url **{rep['no_url']}** 条 · 项目页 **{rep['project_notes']}** 个 · 含收入信号 **{rep['money_signal']}** 条"]
    if rep.get("round"):
        r = rep["round"]
        L.append(f"- 本轮 `{r['run_id']}`：记录 {r['records']}（new {r['new']} / update {r['update']}）"
                 f"→ 重复占比 {100 * r['update'] / max(1, r['records']):.0f}%")
    L += ["", "## 渠道质量", "",
          "> `覆盖` = 有评论条目 / 平台报过评论数的条目（多少条目的用户声音真的入库）；",
          "> `抓取深度` = 抓到条数 / 平台条数，**只在抓到过的条目里算** —— 单看它会高估评论覆盖。",
          "",
          "| 渠道 | 画像 | 条目 | 有正文 | 正文中位 | 有评论 | 应有评论 | 覆盖 | 抓到评论 | 平台评论 | 抓取深度 | 截断 | 无 project_url | 无作者 | 正文错 | 评论错 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for cid, d in sorted(rep["by_channel"].items(), key=lambda kv: -kv[1]["n"]):
        bl = sorted(d["body_len"])
        med = bl[len(bl) // 2] if bl else 0
        rate = f"{100 * d['comments'] / d['platform_comments']:.0f}%" if d["platform_comments"] else "—"
        cov = f"{100 * d['with_comments'] / d['expect_comments']:.0f}%" if d.get("expect_comments") else "—"
        L.append(f"| {cid} | {d.get('profile', '?')} | {d['n']} | {d['body']} | {med} | {d['with_comments']} | "
                 f"{d.get('expect_comments', '—')} | {cov} | {d['comments']} | "
                 f"{d['platform_comments']} | {rate} | {d['trunc']} | {d['no_project_url']} | {d['no_author']} | "
                 f"{d.get('err_body', 0)} | {d.get('err_comments', 0)} |")
    L += ["", "## 缺口清单（按渠道画像判定，供 `tools/kb_backfill.py` 回填）", ""]
    if rep.get("gap_by_channel"):
        L += ["| 渠道 | 缺失字段 | 条数 |", "|---|---|---|"] + \
             [f"| {c} | {m} | {n} |" for (c, m), n in rep["gap_by_channel"]]
        L += ["", f"合计 **{len(rep['gaps'])}** 条待回填（清单见 `_meta/backfill_queue.json`）"]
    else:
        L.append("- 无缺口")
    if rep.get("gap_dead"):
        L.append(f"- 另有 **{rep['gap_dead']}** 条已判结构性无正文（死信账本 `_meta/backfill_dead.json`），不再重试")
    if rep.get("expected_absent"):
        by = "、".join(f"{k}={v}" for k, v in rep["expected_absent_by_channel"])
        L += ["", "### 契约型无正文（**不是缺口，但要入账**）", "",
              f"- **{len(rep['expected_absent'])}** 条：{by}",
              "- 这些渠道的 profile 声明不产出正文（`metadata` / `layer=signal`，如 App Store 榜单、"
              "B 站视频简介）。它们**不计入缺口、不消耗回填额度**，但也**不属于死信**——"
              "列出是为了让「按契约没有」与「该有但没抓到」在报表上可区分，"
              "避免它们同时缺席两个账本、变成无法判读的账外条目。"]
    L += ["", "### 元数据契约门（字段级）", "",
          "> 口径：profile 声明该有的字段缺失 = **取数缺陷**（要动手）；"
          "`channels.yaml` 的 `meta_unavailable` 显式声明不可得 = **按契约没有**（入账不追）。",
          "> 为什么必须分：`published_at` 是时间轴分组键，缺了整条在时间维度消失且不报错 ——"
          " 这是论文 SARC-DQ 说的 metadata-borne defect，得靠**声明的契约**暴露，不能指望下游发现。", ""]
    if rep.get("meta_defects_by_channel"):
        L += ["| 渠道 | 缺失字段 | 条数 |", "|---|---|---|"] + \
             [f"| `{c}` | {f} | {n} |" for (c, f), n in rep["meta_defects_by_channel"]]
        L += ["", f"合计 **{len(rep['meta_defects'])}** 条字段级缺陷"]
    else:
        L.append("- 无字段级缺陷")
    if rep.get("meta_exempt_by_channel"):
        L += ["", "**按契约没有（免追）**：", ""]
        for (c, f), n in rep["meta_exempt_by_channel"]:
            why = ((rep.get("meta_unavailable_declared") or {}).get(c) or {}).get(f) or ""
            L.append(f"- `{c}` · {f} × {n} —— {why}")
    L += ["", "## 噪声条目（removed/deleted）", ""]
    L += [f"- `{n['source']}` {n['title']}" for n in rep["noise"]] or ["- 无"]
    L += ["", "## 无正文条目分布", "",
          "| 渠道 | 条数 |", "|---|---|"] + [f"| {k} | {v} |" for k, v in rep["body_missing"]]
    L += ["", "## 语种分布", ""] + [f"- {k}: {v}" for k, v in rep["lang"]]
    if rep["project_dup_keys"]:
        L += ["", "## project_url 重复（项目页可能重复建）", ""] + \
             [f"- {k} × {v}" for k, v in rep["project_dup_keys"]]
    if rep.get("last_run"):
        lr = rep["last_run"]
        L += ["", f"## 最近一次运行 `{lr['run_id']}`（{lr['elapsed_s']}s）", "",
              "| 渠道 | 状态 | 条数 | 新增 | 耗时 |", "|---|---|---|---|---|",
              *[f"| {c['id']} | {c['status']} | {c['count']} | {c.get('new')} | {c['elapsed_s']}s |"
                for c in sorted(lr["channels"], key=lambda c: -c["elapsed_s"])]]
        if lr["errors"]:
            L += ["", "**错误**："] + [f"- {e}" for e in lr["errors"][:10]]
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default="", help="指定 run_id 统计本轮 new/update")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    rid = args.run
    if not rid:
        # 只挑「采集轮」做默认 run_id：backfill / reclassify 的 run 记录没有 total_items，
        # 拿它当轮次名会让分析报告看不出对应哪次采集。latest.json 是 RunLog 的指针文件，要排除。
        runs = [p for p in sorted(RUNS.glob("*.json"))
                if p.stem != "latest" and _is_collect_run(p)] or sorted(RUNS.glob("*.json"))
        rid = runs[-1].stem if runs else ""
    rep = analyze(rid or None)

    if not args.quiet:
        print(f"记录 {rep['total_records']} · 唯一条目(累计) {rep['unique_items']} · "
              f"在库可消费 {rep.get('live_items', rep['unique_items'])} · 缺url {rep['no_url']} · "
              f"项目页 {rep['project_notes']} · 收入信号 {rep['money_signal']}")
        if rep.get("round"):
            r = rep["round"]
            print(f"本轮 {r['run_id']}: new={r['new']} update={r['update']} "
                  f"重复率={100 * r['update'] / max(1, r['records']):.0f}%")
        want = []
        for cid, d in sorted(rep["by_channel"].items(), key=lambda kv: -kv[1]["n"]):
            bl = sorted(d["body_len"]); med = bl[len(bl) // 2] if bl else 0
            rate = f"{100 * d['comments'] / d['platform_comments']:.0f}%" if d["platform_comments"] else "—"
            cov_s = (f"{100 * d['with_comments'] / d['expect_comments']:.0f}%"
                     if d.get("expect_comments") else "—")
            exp = PROFILE_EXPECT.get(d.get("profile", "discussion"), PROFILE_EXPECT["discussion"])
            flag = []
            if exp["body"] and d["n"] and d["body"] / d["n"] < 0.7:
                flag.append("正文<70%")
            # 覆盖 与 深度 是两个指标：覆盖看「多少条目的评论真的入库了」，
            # 深度只看「已入库的抓全了没有」。前者掉线时后者可能还很漂亮。
            if exp["comments"] and d.get("expect_comments") and \
                    d["with_comments"] / d["expect_comments"] < 0.4:
                flag.append(f"评论覆盖<40%（{d['with_comments']}/{d['expect_comments']}）")
            if exp["comments"] and d["platform_comments"] >= 20 and rate != "—" and int(rate.rstrip('%')) < 40:
                flag.append(f"评论深度<40%（{rate}）")
            if exp["project_url"] and d["no_project_url"] == d["n"]:
                flag.append("无项目链接")
            if d.get("err_body") or d.get("err_comments"):
                flag.append(f"取数错误 正文{d.get('err_body', 0)}/评论{d.get('err_comments', 0)}")
            if d.get("partial"):
                flag.append(f"翻页中断{d['partial']}")
            if d.get("profile") == "metadata" and d["body"] == 0:
                flag = []                                          # 元数据渠道无正文属预期，不报
            if flag:
                want.append(f"    ! {cid:14s} [{d.get('profile', '?'):10s}] n={d['n']:<3} 正文{d['body']:<3} "
                            f"中位{med:<6} 评论覆盖{cov_s:<6} {'/'.join(flag)}")
        if want:
            print("  需要优化：")
            print("\n".join(want))
        if rep.get("gap_by_channel"):
            print(f"  待回填缺口 {len(rep['gaps'])} 条：" +
                  "、".join(f"{c}/{m}={n}" for (c, m), n in rep["gap_by_channel"][:8]))
        if rep.get("meta_defects_by_channel"):
            print(f"  元数据契约缺陷 {len(rep['meta_defects'])} 条：" +
                  "、".join(f"{c}/{f}={n}" for (c, f), n in rep["meta_defects_by_channel"][:8]))
        if rep.get("meta_exempt_by_channel"):
            print("  按契约免追：" +
                  "、".join(f"{c}/{f}={n}" for (c, f), n in rep["meta_exempt_by_channel"][:6]))

    write_note(DIR_REPORT / f"分析-{rid or 'all'}.md",
               {"type": "report", "title": f"诊断 {rid}", "updated": iso(now_cst()),
                "tags": ["报告", "诊断"]}, render(rep))
    # 同日诊断报告自动清理：分析-* 是「当下快照」的可再生即时报告，同日多轮只需保留最新那份。
    # 为什么必须清：设计原则 6 讲「索引层不被生成物淹没」，但 00-索引/报告/ 自身就在被
    # 时间戳报告淹没（实测 16 份里 6 份是同一天的分析-*）。rid 格式 YYYYMMDDTHHMMSS，
    # 字典序 == 时间序，按 stem 排序留尾即「保留当日最新」。分析-all.md（无 rid）不动。
    _today = (rid or "")[:8]
    if _today:
        same_day = sorted(DIR_REPORT.glob(f"分析-{_today}T*.md"))
        for stale in same_day[:-1]:
            try:
                stale.unlink()
            except OSError:
                pass
    (META / "analysis_latest.json").write_text(json.dumps(
        {"unique_items": rep["unique_items"], "no_url": rep["no_url"], "round": rep.get("round"),
         "by_channel": {k: {kk: vv for kk, vv in v.items() if kk != "body_len"}
                        for k, v in rep["by_channel"].items()},
         "body_missing": rep["body_missing"], "noise": len(rep["noise"]),
         "gaps": len(rep.get("gaps") or []), "gap_by_channel": rep.get("gap_by_channel"),
         "expected_absent": len(rep.get("expected_absent") or []),
         "expected_absent_by_channel": rep.get("expected_absent_by_channel"),
         "meta_defects": len(rep.get("meta_defects") or []),
         "meta_defects_by_channel": rep.get("meta_defects_by_channel"),
         "meta_exempt_by_channel": rep.get("meta_exempt_by_channel"),
         "money_signal": rep["money_signal"], "lang": rep["lang"]},
        ensure_ascii=False, indent=1), encoding="utf-8")
    # 缺口队列：kb_backfill.py 直接消费
    (META / "backfill_queue.json").write_text(json.dumps(
        {"generated": iso(now_cst()), "run_id": rid or "all", "count": len(rep.get("gaps") or []),
         "items": rep.get("gaps") or []}, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
