"""kb_insight — 语料洞察层（P0-3）。

背景：这套 KB 的既定目的是「收集语料，供后续 AI 分析」。但实测跑完 5 轮之后，
`00-索引/` 里只有**审计报告**（渠道健康、内容质量）—— 全是「收得好不好」，
没有一份是「收来的东西说明了什么」。缺的是分析层。

本工具补的就是这一层，产出 `00-索引/洞察-<日期>.md`，包含：

  1. 结论先行        —— 从数据里读出的判断（不是统计数字的复述）
  2. 信号强度榜      —— 跨渠道重复出现的项目 = 强信号，按渠道数排序
  3. 赛道分布        —— 给语料打 topic 标签，看独立开发者在做什么
  4. 变现信号        —— 有多少条在谈定价/订阅/收入，以及具体说法
  5. 痛点与需求      —— 从标题/正文里抽「我想要/我卡在/替代 X」类表达
  6. 结构性缺口      —— 哪些赛道/渠道明显覆盖不足
  7. 口径与局限      —— 明确写出这份洞察**不能**支撑什么结论

口径纪律：所有比例都标出分母；信号榜不把「出现次数」当「热度」；
痛点提取是正则启发式，明确标注为「线索」而非结论。

用法：
  python tools/kb_insight.py                 # 出报告
  python tools/kb_insight.py --tag           # 同时把 topic 标签写回语料 frontmatter
  python tools/kb_insight.py --top 40        # 信号榜长度
"""
from __future__ import annotations

import argparse
import collections
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_common import (DIR_INDEX, DIR_REPORT, META, ROOT, Seen, TOPICS, fm_scalars,  # noqa: E402
                       iso, now_cst, split_note, topic_of, write_ledger, write_note)
from kb_collect import is_project_ish                                  # noqa: E402
from kb_content_audit import (RELEV, channel_profiles, is_fatal, item_layer,  # noqa: E402
                              load_latest, reasons_for)
import statistics                                                       # noqa: E402

# 赛道词表定义在 kb_common（采集端 kb_collect 也要用，共用一份；见那里的注释）。
# 这里 re-export TOPICS / topic_of 以保持本模块既有调用点不变。

# 变现信号：命中即「这条在谈钱」
MONEY = re.compile(
    r"pricing|price|付费|订阅|subscription|MRR|ARR|revenue|营收|收入|月入|"
    r"monetiz|变现|paywall|收费|paywall|plan\b|tier|freemium|一次性买断|lifetime\s+deal",
    re.I)

# 变现**证据**（严格口径）：只命中 MONEY 关键词 = 线索，不是「N 个项目在谈收入」。
# 实测 money_n=684 而含具体数字的页面仅 184（11%），松口径虚高约 3.7 倍、被读者当项目数引用。
# 判据 = 具体金额数字（货币符号/单位与数字相邻：$1,240 MRR / ¥3000 / 12k/月 / €450 / 月入3万），一条正则、零依赖。
MONEY_EVIDENCE = re.compile(
    r"(?:[$¥€£]\s?\d)"
    r"|(?:\d[\d,.]*\s?[kKmM万]?\s*(?:美元|美金|元|块|rmb|usd|eur|gbp|mrr|arr|[/每]\s*[月年]))"
    r"|(?:mrr|arr)\s*(?:of|is|was|[:=~约])?\s*\$?\s*\d"
    r"|(?:月入|收入|营收|定价)\s*(?:约|近|超过|达)?\s*\d", re.I)

# 痛点/需求信号：这些短语后面通常跟着真实需求
PAIN = [
    ("想要而找不到", re.compile(r"\bI\s+wish|I\s+wish\s+there\s+was|有没有(?:人|什么|工具)|"
                          r"求推荐|求一个|想要一个|为什么没有|is\s+there\s+(?:a|any)\s+tool", re.I)),
    ("当前方案不好用", re.compile(r"frustrat|annoying|painful|hate\s+(?:that|when)|"
                            r"太麻烦|很麻烦|不(?:好|方)用|受不了|吐槽", re.I)),
    ("在找替代品", re.compile(r"alternative\s+to|替代|replace\s+(?:X|my)|migrat(?:e|ing)\s+(?:off|from)|"
                          r"switch(?:ed|ing)?\s+(?:from|away)", re.I)),
    ("做不出来/卡住", re.compile(r"struggl|stuck|cannot\s+figure|怎么(?:做|实现)|"
                          r"卡在|搞不定|不会做", re.I)),
    ("愿意付钱", re.compile(r"would\s+pay|pay\s+for|愿意(?:付费|花钱)|值得(?:付费|买)|"
                        r"shut\s+up\s+and\s+take\s+my\s+money", re.I)),
]

SIGNAL_FLOOR = 2          # 至少要跨几个渠道出现才算「强信号」


# ---------------------------------------------------------------- 工具

def host_of(r: dict) -> str:
    u = r.get("project_url") or r.get("url") or ""
    m = re.match(r"https?://([^/]+)", u)
    if not m:
        return ""
    h = m.group(1).lower().removeprefix("www.")
    return "" if h in ("news.ycombinator.com", "reddit.com", "github.com",
                       "betalist.com", "producthunt.com") else h


def usable(items: list[dict]) -> list[dict]:
    out = []
    for r in items:
        rs = reasons_for(r)
        if set(rs) & RELEV or is_fatal(r, rs):
            continue
        out.append(r)
    return out


def money_quote(r: dict) -> str:
    body = f"{r.get('title') or ''}. {r.get('body') or ''}"
    m = MONEY.search(body)
    if not m:
        return ""
    s = max(0, m.start() - 70)
    return re.sub(r"\s+", " ", body[s:m.end() + 90]).strip()


def pain_quotes(r: dict) -> list[tuple[str, str]]:
    body = f"{r.get('title') or ''}. {r.get('body') or ''}"
    out = []
    for name, rx in PAIN:
        m = rx.search(body)
        if m:
            s = max(0, m.start() - 60)
            out.append((name, re.sub(r"\s+", " ", body[s:m.end() + 90]).strip()))
    return out


# ---------------------------------------------------------------- 报告

def build(items: list[dict], top: int) -> dict:
    live = load_latest()
    ok = usable(items)

    # 赛道分布（在可用语料上算，分母写清楚）
    topics = collections.Counter(topic_of(r) for r in ok)

    # 跨渠道信号：同 project_url 主体（或同 github 仓库）出现在 >1 渠道 → 强信号
    by_key: dict[str, list[dict]] = collections.defaultdict(list)
    for r in ok:
        h = host_of(r)
        gh = re.match(r"https?://github\.com/([^/]+/[^/]+)", r.get("project_url") or "")
        key = f"gh:{gh.group(1).lower()}" if gh else (f"host:{h}" if h else "")
        if key:
            by_key[key].append(r)
    strong = []
    for k, rows in by_key.items():
        chs = {x["source_id"] for x in rows}
        if len(chs) >= SIGNAL_FLOOR:
            best = max(rows, key=lambda x: len(x.get("body") or ""))
            strong.append({"key": k, "channels": sorted(chs), "n_channels": len(chs),
                           "title": best.get("title") or k,
                           "url": best.get("project_url") or best.get("url"),
                           "metrics": best.get("metrics") or {}})
    strong.sort(key=lambda d: (-d["n_channels"], -len(d["channels"])))

    # 变现信号：两口径分开数（旧实现只有一个 money_n=松口径命中数，实测 684 vs 含金额 184，
    # 虚高约 3.7 倍；读者把它当「N 个项目在谈收入」引用 —— 松口径只能算线索数）。
    money = [r for r in ok if MONEY.search(f"{r.get('title') or ''} {r.get('body') or ''}")]
    money_ev = [r for r in money
                if MONEY_EVIDENCE.search(f"{r.get('title') or ''} {r.get('body') or ''}")]

    # 痛点信号
    pains = collections.defaultdict(list)
    for r in ok:
        for name, q in pain_quotes(r):
            pains[name].append({"title": r.get("title"), "url": r.get("url"),
                                "source": r["source_id"], "quote": q})

    # 渠道产出（可用率）
    ch_tot = collections.Counter(r["source_id"] for r in live)
    ch_ok = collections.Counter(r["source_id"] for r in ok)
    prof = channel_profiles()

    return {
        "generated": iso(now_cst()),
        "n_live": len(live), "n_usable": len(ok),
        # 可用语料里「真正是项目」的条数（is_project_ish）。
        # 为什么单列：可用 ≠ 是项目 —— 讨论帖/提问帖/经验帖也是好语料，但**不能当项目算**。
        # 不标出来，后面按可用集做「赛道/变现」分析时会把讨论帖的赚钱闲聊算成项目信号。
        "n_project": sum(1 for r in ok if is_project_ish(r)),
        "signals": sum(1 for r in live if item_layer(r) == "signal"),
        "topics": topics.most_common(),
        "strong": strong[:top],
        "money_signal_n": len(money),        # 线索数（关键词命中，保留旧序列口径不断档）
        "money_evidence_n": len(money_ev),   # 金额证据数（货币符号/单位+数字，如 $1,240 MRR / 12k/月）
        "money_quotes": [{"source": r["source_id"], "title": r.get("title"),
                          "url": r.get("url"), "quote": money_quote(r)}
                         for r in money[:12]],
        "pains": {k: v[:6] for k, v in sorted(pains.items(), key=lambda kv: -len(kv[1]))},
        "pain_n": {k: len(v) for k, v in pains.items()},
        "by_channel": sorted(
            [{"id": c, "profile": prof.get(c, ""), "n": n, "ok": ch_ok.get(c, 0),
              "rate": (ch_ok.get(c, 0) / n if n else 0)} for c, n in ch_tot.items()],
            key=lambda d: -d["rate"]),
        "body_median": statistics.median([len(r.get("body") or "") for r in ok]) if ok else 0,
    }


def conclusions(rep: dict) -> list[str]:
    """从数据读出判断 —— 这一段是报告的真正价值，不是数字复述。"""
    out = []
    n, ok = rep["n_live"], rep["n_usable"]
    out.append(
        f"**可用语料 {ok}/{n}（{ok / n * 100:.0f}%）**。分母是当前在库条目，"
        f"另有 {rep['signals']} 条属信号层（只有元数据，不参与正文分析）。")

    tp = rep["topics"]
    if tp:
        top3 = tp[:3]
        share = sum(c for _, c in top3) / max(1, ok) * 100
        out.append(
            f"**赛道集中在 {top3[0][0]}（{top3[0][1]} 条）、{top3[1][0]}（{top3[1][1]} 条）、"
            f"{top3[2][0]}（{top3[2][1]} 条），三者合计占 {share:.0f}%**。"
            f"这个集中度说明当前渠道结构（HN Show / GitHub / 发布站）天然偏向开发者工具与 AI，"
            f"并不代表市场结构 —— 要判断「哪个赛道机会大」还需要能反映消费端的渠道。"
            if len(top3) >= 3 else f"**赛道以 {top3[0][0]} 为主（{top3[0][1]} 条）**。")

    if rep["strong"]:
        s = rep["strong"][0]
        out.append(
            f"**跨渠道重复出现的项目 {len(rep['strong'])} 个**，最高的是 `{s['title'][:56]}`"
            f"（{s['n_channels']} 个渠道：{'、'.join(s['channels'])}）。"
            f"同一条目在多个渠道独立出现，比单渠道内的票数更能说明关注度 —— "
            f"它是「同一信号被多次独立观测」，而票数只是「一个平台内的一次投票」。")
    else:
        out.append(f"**暂无可信的跨渠道强信号**（阈值：同一项目出现在 ≥{SIGNAL_FLOOR} 个渠道）。"
                   f"这通常意味着渠道覆盖仍偏窄，或项目链接（project_url）缺失导致无法归一。")

    if rep["money_signal_n"]:
        out.append(
            f"**只有 {rep['money_evidence_n']}/{ok} 条（{rep['money_evidence_n'] / max(1, ok) * 100:.0f}%）"
            f"给出真实金额证据**（口径：文本含具体金额，如 `$1,240 MRR` / `12k/月`）；"
            f"关键词线索数 {rep['money_signal_n']} 条只是这数的**命中上限**，不是「{rep['money_signal_n']} 个项目在谈收入」。"
            f"也就是说当前语料压倒性地在讲「怎么把东西做出来」，"
            f"很少讲「怎么收钱」—— 若目标是找变现方向，这是明显的语料偏斜，需要补商业向来源。")

    if rep["pain_n"]:
        k, v = max(rep["pain_n"].items(), key=lambda kv: kv[1])
        out.append(f"**痛点线索以「{k}」最多（{v} 条）**。这类表达是需求前兆，"
                   f"但注意：它是正则从文本里捞出来的**线索**，不是验证过的需求，"
                   f"要判断真实市场仍需外部数据（搜索量、付费行为）交叉验证。")

    weak = [d for d in rep["by_channel"] if d["n"] >= 5 and d["rate"] < 0.5]
    if weak:
        out.append("**产出率明显偏低的渠道：" +
                   "、".join(f"`{d['id']}`({d['ok']}/{d['n']})" for d in weak) +
                   "**。这类渠道要么口径不对（话题榜被当项目源），要么本该只当线索层（不产出正文）。")
    return out


def render(rep: dict) -> str:
    L = ["---", "type: report", f'title: 语料洞察 {rep["generated"][:10]}',
         f'updated: "{rep["generated"]}"', "tags:", "  - 报告", "  - 洞察", "---", "",
         f"# 语料洞察 · {rep['generated'][:10]}", "",
         f"> 数据源：当前在库 {rep['n_live']} 条（可用 {rep['n_usable']} 条，"
         f"其中**项目型 {rep['n_project']} 条**）｜生成于 {rep['generated']}", "",
         "## 结论先行", ""]
    L += [f"- {c}" for c in conclusions(rep)]

    L += ["", "## 赛道分布", "", "| 赛道 | 条数 | 占可用语料 |", "|---|---|---|",
          *[f"| {t} | {c} | {c / max(1, rep['n_usable']) * 100:.0f}% |"
            for t, c in rep["topics"]]]

    L += ["", "## 跨渠道强信号", ""]
    if rep["strong"]:
        L += ["同一项目被多个渠道独立收录 —— 关注度的交叉验证。", "",
              "| 项目 | 渠道数 | 出现渠道 |", "|---|---|---|"]
        for s in rep["strong"]:
            t = (s["title"] or "").replace("|", "/")[:60]
            L.append(f"| [{t}]({s['url']}) | {s['n_channels']} | {'、'.join(s['channels'])} |")
    else:
        L.append("无（阈值：≥2 个渠道）。")

    L += ["", f"## 变现信号（金额证据 {rep['money_evidence_n']} 条 · 关键词线索 {rep['money_signal_n']} 条）", "",
          "> 口径：`金额证据` = 文本里出现具体金额数字（货币符号/单位与数字成对，如 $1,240 MRR / ¥3000 / 12k/月）；"
          "`关键词线索` 只说明「这条在谈钱」，是前者的命中上限，**不是项目数**。", ""]
    if rep["money_quotes"]:
        for q in rep["money_quotes"]:
            L.append(f"- `{q['source']}` **{(q['title'] or '')[:64]}**")
            if q.get("quote"):
                L.append(f"  > …{q['quote'][:200]}…")
    else:
        L.append("无命中。")

    L += ["", "## 痛点线索", "",
          "> 正则从文本抽取的**线索**，非验证过的需求。用于判断「下一轮该往哪查」，不能直接当结论。", ""]
    for k, rows in rep["pains"].items():
        L.append(f"### {k}（{rep['pain_n'][k]} 条）")
        for r in rows:
            L.append(f"- `{r['source']}` {(r['title'] or '')[:64]}")
            L.append(f"  > …{r['quote'][:180]}…")
        L.append("")

    L += ["## 渠道产出率", "", "| 渠道 | profile | 在库 | 可用 | 可用率 |", "|---|---|---|---|---|"]
    for d in rep["by_channel"]:
        L.append(f"| `{d['id']}` | {d['profile'] or '—'} | {d['n']} | {d['ok']} | {d['rate'] * 100:.0f}% |")

    L += ["", "## 口径与局限", "",
          "这份洞察**不能**用来支撑以下结论，写明是为了防止误用：", "",
          "- **不能说「某赛道机会大」**：语料来自 HN Show / GitHub / 发布站，"
          "是「开发者已经在做的东西」，不是「市场缺什么」。这是幸存者样本，且渠道结构自带偏向。",
          "- **不能把条数当热度**：一天内被收录 1 条和跨 5 个渠道被收录 5 条，意义完全不同，"
          "故信号榜按**渠道数**而非条数排序。",
          "- **痛点线索未经验证**：正则会捞到「求推荐」这类语气词，也可能捞到反驳语境。"
          "它只适合用来决定「下一步查什么」，不适合直接当需求清单。",
          "- **历史深度有限**：`captured_days` 只有 "
          f"{len({(r.get('captured_at') or '')[:10] for r in load_latest()})} 天，"
          "任何「趋势/增长」类判断都还不成立。",
          ""]
    return "\n".join(L)


# ---------------------------------------------------------------- 浏览入口

# 一个 base 代码块，多个 view —— Obsidian 会在表格右上角出下拉，切维度不用离开本页。
# 只用文档明确支持的键（filters / views / order / groupBy / limit）：
# 刻意不用 sort 和日期函数 —— 各来源对 sort 的写法说法不一（column/order/property/direction），
# 写错会让整个视图报错；groupBy 分组字符串属性是最稳的切法，时间轴交给 shard/pub_day 这两个纯字符串字段。
BASE_BLOCK = """```base
filters:
  and:
    - file.hasProperty("type")
views:
  - type: table
    name: 语料·按赛道
    filters:
      and:
        - 'type == "corpus"'
    groupBy:
      property: topic
      direction: ASC
    order:
      - title
      - source_name
      - kind
      - pub_day
      - comments_count
      - url
    limit: 400
  - type: table
    name: 语料·按渠道
    filters:
      and:
        - 'type == "corpus"'
    groupBy:
      property: source
      direction: ASC
    order:
      - title
      - topic
      - kind
      - pub_day
      - comments_count
      - url
    limit: 400
  - type: table
    name: 语料·按发布日
    filters:
      and:
        - 'type == "corpus"'
    groupBy:
      property: pub_day
      direction: DESC
    order:
      - title
      - topic
      - source_name
      - comments_count
      - url
    limit: 400
  - type: table
    name: 语料·按采集批次
    filters:
      and:
        - 'type == "corpus"'
    groupBy:
      property: shard
      direction: DESC
    order:
      - title
      - topic
      - source_name
      - comments_count
      - url
    limit: 400
  - type: table
    name: 项目池
    filters:
      and:
        - 'type == "project"'
        - 'stale != true'
    order:
      - title
      - project_url
      - sources
      - first_seen
      - lang
    limit: 300
  - type: table
    name: 历史实体页（已无在库语料）
    filters:
      and:
        - 'type == "project"'
        - 'stale == true'
    order:
      - title
      - project_url
      - first_seen
      - lang
    limit: 300
  - type: table
    name: 人物
    filters:
      and:
        - 'type == "person"'
    order:
      - title
      - handle
      - profile_url
      - first_seen
    limit: 100
  - type: table
    name: 渠道健康
    filters:
      and:
        - 'type == "channel"'
    order:
      - name
      - group
      - status
      - last_verified
      - lang
      - channel_id
    limit: 60
```"""

FALLBACK = """| 目录 | 放什么 | 什么时候进 |
|---|---|---|
| `00-索引/` | 导航：本页、[[字段字典]]、[[渠道台账]]、[[运行日志]]、[[待办与决策]] | 不知道去哪时先回这里 |
| `00-索引/报告/` | 生成物（洞察/审计/分析/修复报告…） | **别翻目录**，先看 [[报告总览]] |
| `10-项目/` | 项目实体页（含观测历史） | 想追某个项目的历史指标 → 先看 [[项目地图]] |
| `20-语料/` | 原文语料（按渠道/日期分片） | 想读原文与评论 |
| `30-人物/` | 独立开发大牛 | 想学方法论 |
| `40-方法论/` | 方法论沉淀 | — |
| `50-渠道/` | 渠道健康台账 | 想知道哪个渠道还能用 |
| `80-归档/` | 已移出检索面的条目（**不是删除**） | 复核误杀 / 捞回 → 先看 [[归档与申诉]] |
| `90-原始/` | 只追加的重放底座（JSONL） | 重放/重建，不直接读 |"""


def browse(rep: dict, items: list[dict]) -> str:
    """生成 `00-索引/浏览.md` —— 单一入口，换维度不换文件夹。

    为什么要有这一页：此前 7 个维度分散在 7 个文件夹里，用户看知识库要在文件树里
    反复横跳（原话：「各个不同的维度在不同的文件夹中需要反复切换」）。
    这里把「每个维度怎么进」压成一页：静态速查表保证一定能用，
    嵌入的 Bases 视图提供交互式切维度，两者互补而非二选一。

    2026-09-20 首屏重排（行业实践调研后的改动，见 `00-索引/报告/信息组织与呈现-调研-20260920.md`）：
    原首屏第一屏是「一段说明 + 6 行指向报告的表格 + 一个巨大的 Bases 代码块」。
    问题不在内容，在**顺序** —— Bases 代码块占据视觉重心，而它恰恰是「不知道该怎么看的人」
    最不需要先看的东西（那是给已经知道要找什么的人用的）。
    现改为四段：① 你现在想干什么（意图路由）→ ② 五个数字 → ③ Bases 视图 → ④ 速查表。
    依据：NN/g 的信息气味（链接点之前就要能判断去哪）+ 渐进式披露（首屏只放高层入口）。

    另一处改动：意图表补上原来**完全缺失**的四类真实问题 —— 找项目、找原文、复核归档、
    理解规矩。原来的 6 行路由**全部**指向生成的报告，也就是只覆盖了「读结论」，
    没覆盖「找东西」（诊断见调研报告的第三节）。
    """
    seen = Seen()
    ok = usable(items)
    dates = rep["generated"][:10]
    dated = dates.replace("-", "")

    def link(r: dict, label: str | None = None, n: int = 40) -> str:
        note = (seen.get(r.get("item_id")) or {}).get("note") or ""
        text = (label or r.get("title") or "?").replace("|", "/")[:n]
        if note and note.startswith("20-语料/"):
            return f"[[{note[:-3]}|{text}]]"
        return text

    n_report = len(list(DIR_REPORT.glob("*.md")))
    n_arch = len(list((ROOT / "80-归档").rglob("*.md")))
    n_proj_glob = len(list((ROOT / "10-项目").glob("*.md")))
    n_chan = len(list((ROOT / "50-渠道").glob("*.md")))

    L = [
        "---",
        "type: index",
        "title: 从这里开始",
        "tags:",
        "  - 索引",
        "  - 导航",
        "aliases:",
        '  - "从这里开始"',
        '  - "知识库总入口"',
        '  - "总入口"',
        f'generated_at: "{rep["generated"]}"',
        "---",
        "",
        "# 从这里开始 · 找项目 / 读原文 / 看趋势 / 复核归档",
        "",
        "> **换维度不用换文件夹。** 本页四段，从上往下读即可："
        "**① 你现在想干什么** → **② 五个数字** → **③ 数据库视图**（可交互切维度）"
        "→ **④ 速查表**（不依赖插件，点即达）。",
        f"> 本页由 `python tools/kb_insight.py --browse` 生成，**手改会被下次覆盖**。"
        f"｜在库 {rep['n_live']} · 可用 {rep['n_usable']} · 项目型 {rep['n_project']}｜{rep['generated']}",
        "",
        "## 0 · 你现在想干什么",
        "",
        "先对号入座，再往下走。**这一节回答的是「怎么看」，其余各节是「看什么」。**",
        "",
        "| 你的问题 | 去哪 | 那里有什么 |",
        "|---|---|---|",
        f"| 某个项目 / 某个赛道都有谁 | [[项目地图]] | "
        f"{n_proj_glob} 个项目页按赛道分组，组内按在库语料数排 |",
        "| 某条东西的**原文和评论** | 本页第 3、4 节（按渠道 / 按赛道速查表） | "
        "点进去就是原帖全文 + 全部评论，底部还有导航段回实体页 |",
        f"| 现在什么在变热、能不能据此下判断 | [[洞察-{dated}]] | "
        "跨渠道强信号 + 赛道分布 + 变现信号 + **明确的不能下什么结论** |",
        "| 我判废的东西还能不能捞回来 | [[归档与申诉]] | 归档原因分组 + 抽样 + 一条命令撤销 |",
        "| 这套库的规矩是什么、字段啥意思 | [[Home]] · [[字段字典]] | 分层、工具链、字段定义、设计原则 |",
        "| 哪个渠道还能用 | [[渠道台账]] | 每渠道状态、认证方式、停用原因与复活条件 |",
        "",
        f"> 报告现有 **{n_report}** 份，**不要一份份翻** —— [[报告总览]] 给每份补了一句"
        "\"它在讲什么\"，看完再决定点不点。",
        "",
        "## 1 · 五个数字（不滚屏就能看完）",
        "",
        "| 指标 | 值 | 点进去 |",
        "|---|---|---|",
        f"| 在库语料 | **{rep['n_live']}**（可用 {rep['n_usable']} · "
        f"{rep['n_usable'] / max(1, rep['n_live']) * 100:.0f}%） | 下面第 3、4 节 |",
        f"| 项目页 | **{n_proj_glob}** | [[项目地图]] |",
        f"| 报告 | **{n_report}** 份 | [[报告总览]] |",
        f"| 已归档（**没删**） | **{n_arch}** 条 | [[归档与申诉]] |",
        f"| 渠道页 | **{n_chan}** | [[渠道台账]] |",
        "",
        "> 冷启动只记一条：**不知道去哪就回本页第 0 节**。"
        "本页的每一行都指向一个「点开就有东西」的地方，不存在点到空目录。",
        "",
        "## 2 · 数据库视图（推荐，切维度不用翻文件夹）",
        "",
        "> 表格右上角的下拉可切换 8 种切法：按赛道 / 按渠道 / 按发布日 / 按采集批次 / "
        "项目池 / 历史实体 / 人物 / 渠道健康。",
        "> 若这里显示为代码块或报错，说明 Obsidian 的 **Bases** 核心插件没开"
        "（设置 → 核心插件 → 数据库），届时看下面的速查表。",
        "> 注意：**过滤是查询，不是导航** —— 它要求你先知道自己在找什么。"
        f"不知道找什么时用 [[项目地图]]，那是给人按组浏览的地图。",
        "",
        BASE_BLOCK,
        "",
        "## 3 · 速查 · 按渠道",
        "",
        "| 渠道 | 在库 | 可用 | 赛道 top3 | 代表条目 | 入口 |",
        "|---|---|---|---|---|---|",
    ]

    by_ch: dict[str, list[dict]] = collections.defaultdict(list)
    for r in ok:
        by_ch[r["source_id"]].append(r)
    # 速查表按**条数**排（rep["by_channel"] 是按可用率排的，那是审计视角，不是查东西的视角）
    for d in sorted(rep["by_channel"], key=lambda x: -x["n"]):
        cid = d["id"]
        rows = by_ch.get(cid, [])
        tp = collections.Counter(topic_of(r) for r in rows).most_common(3)
        top = "、".join(f"{t}({n})" for t, n in tp) or "—"
        rep_row = max(rows, key=lambda r: len(r.get("body") or "")) if rows else None
        L.append(f"| {cid} | {d['n']} | {d['ok']} | {top} | "
                 f"{link(rep_row) if rep_row else '—'} | [[50-渠道/{cid}]] |")

    L += ["", "## 4 · 速查 · 按赛道", "",
          "| 赛道 | 条数 | 占可用 | 代表条目 |", "|---|---|---|---|"]
    by_topic: dict[str, list[dict]] = collections.defaultdict(list)
    for r in ok:
        by_topic[topic_of(r)].append(r)
    for t, c in rep["topics"]:
        rows = by_topic.get(t) or []
        rep_row = max(rows, key=lambda r: len(r.get("body") or "")) if rows else None
        L.append(f"| {t} | {c} | {c / max(1, rep['n_usable']) * 100:.0f}% | "
                 f"{link(rep_row) if rep_row else '—'} |")

    # 时间轴：用 `pub_day`（发布日），**不是**分片目录名（入库日）。
    # 为什么：90 天历史铺底是一次性跑完的，所有条目都落在同一天的 shard 目录里，
    # 按入库日分组只能得到「1 天 = 全部」，等于没有时间轴。发布日才是真有分布的那个轴。
    day_rows: dict[str, list[dict]] = collections.defaultdict(list)
    for r in items:
        d = (r.get("published_at") or "")[:10]
        if not d:
            note = (seen.get(r.get("item_id")) or {}).get("note") or ""
            m = re.search(r"/(\d{4}-\d{2}-\d{2})/", note)
            d = m.group(1) if m else ""
        if d:
            day_rows[d].append(r)
    nd = len(day_rows)
    L += ["", "## 5 · 速查 · 按发布日（近 14 天）", "",
          f"发布日跨 {nd} 天（{min(day_rows) if day_rows else '—'} ~ "
          f"{max(day_rows) if day_rows else '—'}）。"
          f"**入库日不单独列**：历史铺底是一次性跑完的，全部落在同一天的 `shard` 目录里，"
          f"按入库日分组只会得到「1 天 = 全部」。",
          "", "| 发布日 | 条数 | 代表条目 |", "|---|---|---|"]
    for day in sorted(day_rows, reverse=True)[:14]:
        rows = sorted(day_rows[day], key=lambda r: -len(r.get("body") or ""))
        picks = " ".join(link(r, n=28) for r in rows[:3])
        L.append(f"| {day} | {len(rows)} | {picks} |")

    # 实体页计数按 frontmatter **type** 判，不按「有没有 stale 字样」猜 ——
    # 说明页（type: index）不该混进人物/项目计数（实测 30-人物/人物页说明.md 曾被算成人物页）。
    proj_all = proj_live = ppl_live = 0
    for folder, t in (("10-项目", "project"), ("30-人物", "person")):
        for p in (ROOT / folder).glob("*.md"):
            sp = split_note(p.read_text(encoding="utf-8"))
            fm = fm_scalars(sp[0]) if sp else {}
            if fm.get("type") != t:
                continue
            if t == "project":
                proj_all += 1
                if fm.get("stale") != "true":
                    proj_live += 1
            elif fm.get("stale") != "true":
                ppl_live += 1
    n_proj_all, n_proj_live, n_ppl_live = proj_all, proj_live, ppl_live
    n_ch = sum(1 for _p in (ROOT / "50-渠道").glob("*.md"))
    L += ["", "## 6 · 关联实体", "",
          f"- 项目页 **{n_proj_live}** 个在用 → 目录 `10-项目/`"
          f"（**地图见 [[项目地图]]**，每页含观测历史表）",
          f"- 人物页 **{n_ppl_live}** 个在用 → 目录 `30-人物/`",
          f"- 渠道页 **{n_ch}** 个 → 目录 `50-渠道/`",
          f"- 另有 **{n_proj_all - n_proj_live}** 个项目页已标 `stale: true`"
          f"（对应语料已归档，仅存历史观测）——视图里单独一组，不混进项目池",
          "",
          "> 任一条语料页底部的「导航」段都能跳回它的项目页/人物页/渠道页 —— "
          "所以从语料出发不会走进死胡同。",
          "",
          "## 7 · 兜底：文件夹各管什么", "",
          "Bases 不可用时按这张表进目录。", "",
          FALLBACK,
          "",
          "## 8 · 口径与局限", ""]
    L += [f"- {c}" for c in conclusions(rep)[:3]]
    L += ["", f"_数据源：`90-原始/*/*.jsonl`（只追加）｜生成器：`tools/kb_insight.py`_", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=25, help="信号榜长度")
    ap.add_argument("--browse", action="store_true",
                    help="同时生成 00-索引/浏览.md（单一入口 + Bases 多视图）")
    ap.add_argument("--tag", action="store_true",
                    help="[已废弃] topic 回写交给 tools/kb_navfix.py，这里只提示")
    ap.add_argument("--out", default="")
    args = ap.parse_args(argv)

    items = load_latest()
    rep = build(items, args.top)
    md = render(rep)
    out = Path(args.out) if args.out else (DIR_REPORT / f"洞察-{now_cst().strftime('%Y%m%d')}.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    write_ledger(META / "insight_latest.json",
                 {k: v for k, v in rep.items() if k != "pains"}, indent=2)

    if args.browse:
        bp = DIR_INDEX / "浏览.md"
        bp.write_text(browse(rep, items), encoding="utf-8")
        print(f"[浏览] {bp.relative_to(ROOT).as_posix()}")

    if args.tag:
        print("topic 回写已并入 tools/kb_navfix.py（含 shard/pub_day/导航段），"
              "`--tag` 不再单独执行。")

    print(f"在库 {rep['n_live']} · 可用 {rep['n_usable']} · 项目型 {rep['n_project']} · "
          f"强信号 {len(rep['strong'])} · 变现线索 {rep['money_signal_n']}"
          f"（其中金额证据 {rep['money_evidence_n']}，线索是上限不是项目数）")
    print("赛道：" + "、".join(f"{t}={c}" for t, c in rep["topics"][:6]))
    print(f"[报告] {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
