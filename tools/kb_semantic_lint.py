"""kb_semantic_lint — 语义 lint（**只读**，不写任何语料/实体页）。

为什么需要它（2026-09-21 竞品/论文调研报告的结论）：
本库的结构 lint 已有八项（healthcheck ①-⑧：计数平、缺页、缺 url、断链、路径漂移…），
但**语义 lint 一项都没有**。对照 Karpathy 的 LLM Wiki 模式（2026-04），三种操作里
Ingest / Query 我们做得比原模式更细，Lint 只做了结构侧 —— 这正是本库唯一的结构性欠账。

四个检查项（都是「同一批数据自己跟自己矛盾」的机器可判定情形，不涉及主观判断）：

  1. `cross`   跨语料指标冲突：同一项目（同 project_url / 同名）在不同语料里报出的
               MRR / 定价 / 用户数互相矛盾 —— 下游若按单条引用，会引到一个已被推翻的数字。
  2. `stale`   过期论断：实体页正文里的前瞻性表述（即将上线 / coming soon / waitlist…）
               在**最新观测已过 N 天**后仍未更新 —— 页面在说一件早已发生（或早已作废）的事。
  3. `concept` 概念缺页：被 ≥N 条语料反复提及、但库内没有任何实体页/方法论页/赛道页承载，
               术语因此没有「定义落点」（AI 读到时候只能靠猜）。
  4. `xref`    缺交叉引用：实体页正文提到了另一个在库项目的名字，却没有 wikilink ——
               存在连接但没连（图谱里少一条边）。

**必须诚实声明的边界**：本工具的输出是**线索，不是结论**。指标抽取走正则，会漏、会误命中。
它回答的是「哪些页面值得人看一眼」，不是「哪些页面是错的」。因此：
  * 永不自动改页（只写 `00-索引/报告/` 一类生成物）；
  * 每条发现必须带**出处**（item_id / 语料页 / 数值原文），否则人工无法复核。

用法：
  python tools/kb_semantic_lint.py                    # 四项全跑，出报告
  python tools/kb_semantic_lint.py --checks stale,xref
  python tools/kb_semantic_lint.py --quiet --limit 20
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
from kb_common import (DIR_PROJECTS, DIR_RAW, DIR_REPORT, META, ROOT,  # noqa: E402
                       is_project_ish, load_ndjson, now_cst, norm_url, pub_day_of,
                       write_ledger)

STALE_DAYS = 60          # 前瞻性表述超过这个天数仍未更新 → 过期论断
CONCEPT_MIN = 12         # 一个术语被 ≥ 这么多条语料提到，却没有承载页 → 概念缺页

# ---------------------------------------------------------------- 指标抽取
#
# 只抽四类**可比较**的数值指标。刻意不做「通用数字抽取」：那样会把版本号、端口、
# 年份全捞进来，噪声会把真冲突淹掉。宁可少抽、抽得准。
_NUM = r"(\d[\d,]*(?:\.\d+)?)\s*([kKmM])?"


def _to_num(raw: str, suffix: str) -> float | None:
    try:
        v = float(raw.replace(",", ""))
    except ValueError:
        return None
    s = (suffix or "").lower()
    if s == "k":
        v *= 1_000
    elif s == "m":
        v *= 1_000_000
    return v if 0 < v <= 100_000_000 else None


CLAIM_RES: list[tuple[str, re.Pattern]] = [
    ("mrr", re.compile(r"\$\s*" + _NUM + r"\s*(?:MRR|ARR)\b", re.I)),
    ("mrr", re.compile(r"\b(?:MRR|ARR)\D{0,10}?\$\s*" + _NUM, re.I)),
    ("mrr", re.compile(r"(?:月收入|月入|月营收)\D{0,10}?" + _NUM + r"\s*(?:美元|美金|刀|k)?", re.I)),
    ("price", re.compile(r"\$\s*" + _NUM + r"\s*(?:/|per\s+)\s*(?:mo|month|user|seat)", re.I)),
    ("price", re.compile(_NUM + r"\s*(?:元|块钱)\s*/\s*(?:月|年)", re.I)),
    ("users", re.compile(_NUM + r"\s*(?:users|用户|注册用户)", re.I)),
]
STOPWORDS = {"the", "and", "for", "with", "new", "app", "saas", "ai", "api", "open", "source",
             "week", "month", "day", "day1", "hn", "show", "launch", "free", "beta", "v2", "v3"}
FORWARD_RE = re.compile(
    r"即将(?:上线|发布|推出)|敬请期待|coming\s+soon|launching\s+soon|in\s+private\s+beta|"
    r"waitlist|预约|内测|early\s+access|coming\s+in\s+\d{4}", re.I)


def claims_of(text: str) -> list[tuple[str, float, str]]:
    """从一段文本里抽 (指标类别, 数值, 原文片段)。"""
    out: list[tuple[str, float, str]] = []
    for kind, rx in CLAIM_RES:
        for m in rx.finditer(text or ""):
            groups = m.groups()
            num = _to_num(groups[0], groups[1] if len(groups) > 1 else "")
            if num is None:
                continue
            out.append((kind, num, m.group(0).strip()[:60]))
    return out


def _fmt(v: float) -> str:
    return f"{v:,.0f}" if v >= 100 else f"{v:g}"


def check_cross(items: list[dict]) -> list[dict]:
    """同一项目在不同语料里的指标冲突（只比同 project_url / 同名条目之间）。"""
    groups: dict[str, list[dict]] = collections.defaultdict(list)
    for it in items:
        key = norm_url(it.get("project_url")) or ""
        if not key:
            t = (it.get("title") or "").strip().lower()
            key = f"title:{t}" if len(t) >= 8 else ""
        if key:
            groups[key].append(it)
    findings = []
    for key, rows in groups.items():
        if len(rows) < 2:
            continue
        per_kind: dict[str, list[tuple[float, dict]]] = collections.defaultdict(list)
        for r in rows:
            for kind, val, frag in claims_of(f"{r.get('title') or ''}\n{r.get('body') or ''}"):
                per_kind[kind].append((val, {**r, "_frag": frag}))
        for kind, vals in per_kind.items():
            distinct = sorted({round(v, 4) for v, _ in vals})
            if len(distinct) < 2:
                continue
            # 只有**量级级差异**才算冲突线索：同一指标报 500 与 520 可能是四舍五入，
            # 报 500 与 5000 则是真矛盾。阈值取 1.5×，避免把噪声当冲突。
            lo, hi = distinct[0], distinct[-1]
            if hi / max(lo, 1e-9) < 1.5:
                continue
            findings.append({
                "key": key, "kind": kind,
                "values": [_fmt(v) for v in distinct],
                "sources": [{"item_id": r["item_id"], "source_id": r["source_id"],
                             "title": (r.get("title") or "")[:70], "claim": r["_frag"],
                             "value": _fmt(v)} for v, r in vals][:6],
            })
    return findings


OBS_ROW_RE = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})T[\d:]+\+08:00\s*\|")


def check_stale(pages: list[Path]) -> list[dict]:
    """实体页「前瞻性表述」在最新观测已过 STALE_DAYS 后仍未更新。"""
    now = now_cst()
    out = []
    for p in pages:
        try:
            txt = p.read_text(encoding="utf-8")
        except OSError:
            continue
        hits = FORWARD_RE.findall(txt)
        if not hits:
            continue
        obs = [m.group(1) for m in (OBS_ROW_RE.match(l) for l in txt.splitlines()) if m]
        if not obs:
            continue                                   # 没有观测历史 → 由 ② 缺页/导航检查管
        last = max(obs)
        days = (now.date() - __import__("datetime").date.fromisoformat(last)).days
        if days <= STALE_DAYS:
            continue
        out.append({"page": p.relative_to(ROOT).as_posix(), "last_obs": last, "days": days,
                    "phrases": sorted(set(h.lower() for h in hits))[:5]})
    out.sort(key=lambda x: -x["days"])
    return out


PROPER_RE = re.compile(r"\b([A-Z][A-Za-z0-9][A-Za-z0-9.+#-]{2,})\b")


def check_concept(items: list[dict], pages: list[Path]) -> list[dict]:
    """被反复提及、库内却无承载页的术语。"""
    counts: collections.Counter = collections.Counter()
    for it in items:
        seen: set[str] = set()
        for term in PROPER_RE.findall(f"{it.get('title') or ''} {it.get('body') or ''}"):
            low = term.lower()
            if low in STOPWORDS or len(term) < 3:
                continue
            seen.add(low)
        counts.update(seen)
    page_text = ""
    for p in pages:
        try:
            page_text += p.stem.lower() + "\n"
            head = p.read_text(encoding="utf-8")[:1200].lower()
            page_text += head
        except OSError:
            continue
    out = []
    for term, n in counts.most_common(120):
        if n < CONCEPT_MIN:
            continue
        if term in page_text:
            continue
        out.append({"term": term, "mentions": n})
    return out[:30]


def check_xref(pages: list[Path], limit: int = 30) -> list[dict]:
    """实体页正文提到其它在库项目名、却没有 wikilink。"""
    titles = {}
    for p in pages:
        try:
            head = p.read_text(encoding="utf-8")[:400]
        except OSError:
            continue
        m = re.search(r'^title:\s*"?(.+?)"?\s*$', head, re.M)
        t = (m.group(1) if m else p.stem).strip()
        if len(t) >= 8:
            titles[p] = t
    out = []
    for p, title in titles.items():
        try:
            body = p.read_text(encoding="utf-8")
        except OSError:
            continue
        low = body.lower()
        found = []
        for q, t in titles.items():
            if q == p or t.lower() == title.lower():
                continue
            tl = t.lower()
            if tl in low and f"[[{t}" not in body and f"|{t}]]" not in body:
                found.append(t)
            if len(found) >= 5:
                break
        if found:
            out.append({"page": p.relative_to(ROOT).as_posix(), "mentions": found})
        if len(out) >= limit:
            break
    return out


def load_live_items() -> list[dict]:
    lat: dict[str, dict] = {}
    for f in sorted(DIR_RAW.glob("*/*.jsonl")):
        for r in load_ndjson(f):
            iid = r.get("item_id")
            if not iid:
                continue
            cur = lat.get(iid)
            if cur is None or (r.get("captured_at") or "") >= (cur.get("captured_at") or ""):
                lat[iid] = r
    return list(lat.values())


def render(rep: dict) -> str:
    L = ["# 语义 lint（跨语料矛盾 / 过期论断 / 概念缺页 / 缺交叉引用）", "",
         f"> 生成 {rep['generated']} · 工具 `tools/kb_semantic_lint.py`（**只读**）",
         f"> 语料 {rep['n_items']} 条 · 实体页 {rep['n_pages']} 个",
         "",
         "**这是线索不是结论**：指标走正则抽取，会漏也会误命中。本页的作用是"
         "「指出哪些页面值得人看一眼」，绝不自动改页。每条都带出处（item_id / 语料页），可复核。", ""]

    L += ["## 1. 跨语料指标冲突", "",
          f"- 命中 **{len(rep['cross'])}** 组（同项目在不同语料里报出量级不同的 MRR / 定价 / 用户数）", ""]
    for c in rep["cross"][:25]:
        L.append(f"- `{c['key'][:60]}` · **{c['kind']}**：{ ' vs '.join(c['values']) }")
        for s in c["sources"][:4]:
            L.append(f"    - [{s['source_id']}] {s['title']} —— 原文 `{s['claim']}`（{s['value']}）")

    L += ["", "## 2. 过期论断（前瞻性表述 + 观测已久）", "",
          f"- 命中 **{len(rep['stale'])}** 页（阈值：最新观测 > {STALE_DAYS} 天）", ""]
    for s in rep["stale"][:25]:
        L.append(f"- [[{Path(s['page']).stem}]] 最后观测 {s['last_obs']}（{s['days']} 天前）"
                 f" 仍写着：{'、'.join(s['phrases'])}")

    L += ["", "## 3. 概念缺页（反复提及、无承载页）", "",
          f"- 命中 **{len(rep['concept'])}** 个术语（阈值：≥ {CONCEPT_MIN} 条语料提及，"
          f"且任何实体页/方法论页的标题与开头都没有它）", ""]
    for c in rep["concept"]:
        L.append(f"- `{c['term']}` × {c['mentions']} 条")

    L += ["", "## 4. 缺交叉引用（提到了在库项目名但没连）", "",
          f"- 命中 **{len(rep['xref'])}** 页", ""]
    for x in rep["xref"]:
        L.append(f"- [[{Path(x['page']).stem}]] → 提及未连：{'、'.join(x['mentions'])}")

    L += ["", "## 下一步", "", "```",
          "python tools/kb_semantic_lint.py --checks cross,stale   # 只跑某几项",
          "python tools/kb_semantic_lint.py --quiet --limit 10     # 控制报告长度",
          "```", "",
          "人工复核后：属实的矛盾 → 在实体页写清「哪个数字是最新的」；确实过期的论断 → 改页；",
          "值得建页的概念 → 建 `40-方法论/` 页（唯一人工创作区）；缺的引用 → 补 wikilink。",
          "**工具不代劳这一步** —— 语义判断留给人。"]
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--checks", default="cross,stale,concept,xref")
    ap.add_argument("--limit", type=int, default=30)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    want = {c.strip() for c in args.checks.split(",") if c.strip()}

    items = load_live_items()
    pages = sorted(DIR_PROJECTS.glob("*.md"))
    rep: dict = {"generated": now_cst().isoformat(timespec="seconds"),
                 "n_items": len(items), "n_pages": len(pages)}

    if "cross" in want:
        rep["cross"] = check_cross(items)
    else:
        rep["cross"] = []
    if "stale" in want:
        rep["stale"] = check_stale(pages)
    else:
        rep["stale"] = []
    if "concept" in want:
        rep["concept"] = check_concept(items, pages)
    else:
        rep["concept"] = []
    if "xref" in want:
        rep["xref"] = check_xref(pages, limit=args.limit)
    else:
        rep["xref"] = []

    ts = now_cst().strftime("%Y%m%dT%H%M%S")
    out = DIR_REPORT / f"语义lint-{ts}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(rep), encoding="utf-8")
    write_ledger(META / "semantic_lint_latest.json", {
        k: v for k, v in rep.items() if k in ("generated", "n_items", "n_pages")} |
        {"cross": len(rep["cross"]), "stale": len(rep["stale"]),
         "concept": len(rep["concept"]), "xref": len(rep["xref"]),
         "top_stale": rep["stale"][:10], "top_cross": rep["cross"][:10]}, indent=1)

    # 同日只留最新一份（与 kb_analyze 的同日清理同一纪律：报告目录不能被时间戳淹没）
    day = ts[:8]
    for old in sorted(DIR_REPORT.glob(f"语义lint-{day}T*.md"))[:-1]:
        try:
            old.unlink()
        except OSError:
            pass

    if not args.quiet:
        print(f"语义 lint：跨语料冲突 {len(rep['cross'])} · 过期论断 {len(rep['stale'])} · "
              f"概念缺页 {len(rep['concept'])} · 缺引用 {len(rep['xref'])}")
        for s in rep["stale"][:5]:
            print(f"  ! 过期 {s['page'].split('/')[-1]} 最后观测 {s['last_obs']}（{s['days']} 天）")
        for c in rep["cross"][:5]:
            print(f"  ! 冲突 {c['key'][:50]} {c['kind']}: {' vs '.join(c['values'])}")
    print(f"[报告] {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
