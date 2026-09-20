"""kb_prune — 存量语料重判与归档（P1-3）。

背景：`_meta/rules.yaml` 只作用于**新进**语料。开规则之前已经躺在库里的废料
（awesome-* 资源清单、App Store 商业榜、泛媒体文章）不会自己消失 ——
`kb_collect.py` 的 rolling window 只回榜不清理，`kb_backfill` 只补正文。
本工具就是补这个缺口：拿当前规则重判**存量**，把废料从语料区搬进 80-归档/。

判定顺序（先判渠道，再判规则）：
  1. 渠道停用   —— 该渠道已在 channels.yaml 置 enabled:false / 进了 disabled 段
  2. 排除:标题  —— 命中全局或渠道级 exclude_title
  3. 排除:URL   —— 命中 exclude_url
  4. 排除:无主题词 —— 设了 require_any 且标题+正文一条都不命中

安全约定：
  * 默认**只报告不动作**；要真搬必须显式 `--apply`。
  * 搬运只移动 note 文件（不删），并写 undo 清单 `_meta/prune_manifest_<ts>.json`，
    可用 `--undo <manifest>` 原样搬回。
  * 原始 JSONL（90-原始/）**永不动** —— 它是重放底座，清了就真的不可复现了。
  * seen.json 不清账：条目仍被记住，只是 note 位置变了。故移动后要同步 note 路径。

用法：
  python tools/kb_prune.py                     # 报告：按渠道/原因分组列将归档条目
  python tools/kb_prune.py --samples 5         # 每组多打几条样例标题
  python tools/kb_prune.py --apply             # 真正搬运到 80-归档/
  python tools/kb_prune.py --undo _meta/prune_manifest_20260920T101530.json
  python tools/kb_prune.py --channels apple_rss,sspai    # 只处理指定渠道
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_common import (DIR_RAW, DIR_REPORT, META, ROOT, Seen, iso,  # noqa: E402
                       load_ndjson, now_cst)
from kb_collect import apply_rules, load_registry, load_rules          # noqa: E402

DIR_ARCHIVE = ROOT / "80-归档"
DIR_CORPUS = ROOT / "20-语料"
CORPUS_PREFIX = "20-语料/"


# ------------------------------------------------------------------ 数据装载

def load_items() -> dict[str, dict]:
    """从 90-原始/ 重建 item_id → 条目（同 id 取正文最长的那条）。

    读法用 load_ndjson()（按 \\n 切）：`splitlines()` 会按 U+2028 类字符切分，
    把含这类字符的记录静默丢掉 —— 存量重判/归档/存活标记都会漏掉它们
    （实测 v2ex 一条记录含 56 个 U+2028，它的 7 条记录全部隐形）。
    """
    out: dict[str, dict] = {}
    for f in glob.glob(str(DIR_RAW / "*" / "*.jsonl")):
        for r in load_ndjson(Path(f)):
            iid = r.get("item_id")
            if not iid:
                continue
            prev = out.get(iid)
            if prev is None or len(r.get("body") or "") > len(prev.get("body") or ""):
                out[iid] = r
    return out


def disabled_ids(reg: dict) -> set[str]:
    """渠道停用集合：enabled:false 的 + disabled 段里列的。"""
    ids = {c["id"] for c in (reg.get("channels") or []) if not c.get("enabled")}
    ids |= {c["id"] for c in (reg.get("disabled") or []) if c.get("id")}
    return ids


# ------------------------------------------------------------------ 判定

def judge(items: list[dict], rules: dict, off: set[str], ch_id: str) -> dict[str, str]:
    """返回 item_id → 归档原因。空 dict 表示该渠道全部保留。"""
    if ch_id in off:
        return {it["item_id"]: "渠道停用" for it in items if it.get("item_id")}
    sink: list[dict] = []
    apply_rules(items, {"id": ch_id}, rules, stage="both", sink=sink)
    return {d["item_id"]: d["reason"] for d in sink if d.get("item_id")}


def build_plan(args) -> tuple[dict[str, list[dict]], dict]:
    rules = {} if args.no_rules else load_rules()
    reg = load_registry()
    off = disabled_ids(reg)
    items = load_items()
    seen = Seen()

    want = {c.strip() for c in args.channels.split(",") if c.strip()} if args.channels else None

    by_ch: dict[str, list[dict]] = {}
    for iid, meta in seen.items.items():
        ch_id = meta.get("source") or "?"
        if want and ch_id not in want:
            continue
        note = meta.get("note") or ""
        rec = items.get(iid) or {}
        # 非语料 note（人物页/项目页）不搬：它们是多条语料聚合出来的，搬一条会拆散。
        # 这类页面的清理走 kb_reclassify.py --merge-orphans。
        if not note.startswith(CORPUS_PREFIX):
            continue
        by_ch.setdefault(ch_id, []).append({
            "item_id": iid, "title": rec.get("title") or "",
            "url": rec.get("url") or "", "note": note,
            "body_len": len(rec.get("body") or ""),
        })

    plan: dict[str, list[dict]] = {}
    for ch_id, rows in sorted(by_ch.items()):
        verdict = judge(items_list(rows, items), rules, off, ch_id)
        hit = []
        for r in rows:
            why = verdict.get(r["item_id"])
            if why:
                r["reason"] = why
                hit.append(r)
        if hit:
            plan[ch_id] = hit
    stats = {"total": sum(len(v) for v in by_ch.values()),
             "archived": sum(len(v) for v in plan.values()),
             "channels": len(by_ch),
             "by_ch_total": {k: len(v) for k, v in by_ch.items()},
             "disabled": sorted(off)}
    return plan, stats


def items_list(rows: list[dict], index: dict[str, dict]) -> list[dict]:
    """把 seen 的行还原成 rule 判定需要的完整条目。"""
    out = []
    for r in rows:
        rec = index.get(r["item_id"])
        if rec:
            out.append(rec)
    return out


# ------------------------------------------------------------------ 搬运

def archive_path(note_rel: str) -> Path:
    """20-语料/posts/<src>/<date>/x.md → 80-归档/posts/<src>/<date>/x.md"""
    rel = note_rel[len(CORPUS_PREFIX):] if note_rel.startswith(CORPUS_PREFIX) else note_rel
    return DIR_ARCHIVE / rel


def stamp_frontmatter(path: Path, reason: str) -> None:
    """在 frontmatter 里补 archived / archive_reason / archive_url_note，正文原样保留。"""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return
    if not text.startswith("---"):
        return
    end = text.find("\n---", 3)
    if end < 0:
        return
    fm, rest = text[:end], text[end:]
    if re.search(r"^archived:", fm, re.M):
        return
    add = (f'\narchived: true'
           f'\narchived_at: "{iso(now_cst())}"'
           f'\narchive_reason: {json.dumps(reason, ensure_ascii=False)}')
    path.write_text(fm + add + rest, encoding="utf-8")


def do_apply(plan: dict[str, list[dict]], seen: Seen) -> Path:
    moves: list[dict] = []
    for ch_id, rows in plan.items():
        for r in rows:
            src = ROOT / r["note"]
            if not src.exists():
                continue
            dst = archive_path(r["note"])
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.exists():                       # 罕见：同 id 重复搬过
                dst = dst.with_name(dst.stem + "-dup" + dst.suffix)
            shutil.move(str(src), str(dst))
            stamp_frontmatter(dst, r["reason"])
            rel_new = dst.relative_to(ROOT).as_posix()
            moves.append({"item_id": r["item_id"], "source": ch_id, "reason": r["reason"],
                          "from": r["note"], "to": rel_new})
            # 同步见账簿里的 note 位置，否则下一轮 kb_collect 会以为 note 还在老地方
            if r["item_id"] in seen.items:
                seen.items[r["item_id"]]["note"] = rel_new
    seen.save()
    man = META / f"prune_manifest_{now_cst().strftime('%Y%m%dT%H%M%S')}.json"
    man.write_text(json.dumps({"at": iso(now_cst()), "moves": moves},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    return man


def do_undo(man_path: str, seen: Seen) -> int:
    man = json.loads(Path(man_path).read_text(encoding="utf-8"))
    n = 0
    for m in man.get("moves") or []:
        src, dst = ROOT / m["to"], ROOT / m["from"]
        if not src.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        if m["item_id"] in seen.items:
            seen.items[m["item_id"]]["note"] = m["from"]
        n += 1
    seen.save()
    return n


# ------------------------------------------------------------------ 实体页存活标记

NAV_ENTITY_RE = re.compile(r"^- (?:项目页|人物页)：\[\[([^\]|#]+)", re.M)
ENTITY_DIRS = ("10-项目", "30-人物")
ENTITY_ARCHIVE = {"10-项目": DIR_ARCHIVE / "项目", "30-人物": DIR_ARCHIVE / "人物"}
# 目录说明页 / 索引页不是实体，无论 stale 与否都不搬
# 名字兜底 + `_is_meta_note` 的 type 判断（index/home）双保险：改名后的说明页靠 type 拦住
ENTITY_SKIP = {"README.md", "index.md", "索引.md"}


def _live_stems() -> set[str]:
    """在库语料页导航段里指向的实体页名集合。

    在库判据不靠 seen（那里没有 title/url，算不出实体路径），而是直接读**在库语料页导航段**
    里那条实体链接 —— 它本来就是采集端按同一规则生成的，天然同源。
    """
    out: set[str] = set()
    for p in DIR_CORPUS.rglob("*.md"):
        m = NAV_ENTITY_RE.search(p.read_text(encoding="utf-8"))
        if m:
            out.add(m.group(1).split("/")[-1])
    return out


def _entity_liveness(apply: bool) -> dict:
    """给实体页打 `stale: true` —— 没有在库语料指向它的项目/人物页 = 历史页。

    为什么必须做：归档只搬语料 note，**不动** `10-项目/`。于是实体页数会一直领先在库条目数
    （实测 818 vs 710），Bases 的「项目池」视图就会混进一堆已经没有在库语料的项目 ——
    恰恰是用户拿来挑候选的那张表。

    只打标不搬家：标记可逆，条目若回到在库，标记自动摘掉。（真要清出检索面走
    `--archive-entities`，那一步以本标记为输入。）
    """
    live_stems = _live_stems()

    stale, revived = [], []
    for folder in ENTITY_DIRS:
        for p in (ROOT / folder).glob("*.md"):
            if _is_meta_note(p):
                continue                        # 说明页/索引页不是实体，不打 stale（实测误标过「人物页说明」）
            txt = p.read_text(encoding="utf-8")
            has = re.search(r"^stale:\s*true\s*$", txt, re.M) is not None
            want = p.stem not in live_stems
            if want and not has:
                if apply:
                    end = txt.find("\n---", 3)
                    if txt.startswith("---") and end > 0:
                        p.write_text(txt[:end] + f'\nstale: true' + txt[end:], encoding="utf-8")
                stale.append(p.stem)
            elif not want and has:
                if apply:
                    p.write_text(re.sub(r"^stale:\s*true\s*\n", "", txt, count=1, flags=re.M),
                                 encoding="utf-8")
                revived.append(p.stem)
    return {"stale": len(stale), "revived": len(revived), "live_stems": len(live_stems),
            "samples": stale[:5]}


def liveness_report(apply: bool) -> None:
    d = _entity_liveness(apply)
    print(f"实体页存活：在库语料指向 {d['live_stems']} 个；"
          f"{'标记' if apply else '待标记'} stale {d['stale']} 个"
          f"，{'摘除' if apply else '待摘除'} {d['revived']} 个")
    if d["samples"]:
        print("  样例：" + "、".join(s[:40] for s in d["samples"]))


# ------------------------------------------------------------------ 实体页归档

LINK_EXCLUDE = ("80-归档",)          # 归档区自己指向旧路径是允许的（会被一起改写）


def _inbound_refs(stems: set[str]) -> dict[str, list[str]]:
    """扫全库（排除 80-归档 与实体目录自身），找出仍指向这些实体页的 wikilink。

    搬走一个还有人指着的页面 = 制造断链。所以搬之前先要一份「引用方」清单，
    有引用就**不搬**（宁可留一个 stale 页也不断链）。
    """
    pat = re.compile(r"\[\[([^\]|#]+)")
    refs: dict[str, list[str]] = {}
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(LINK_EXCLUDE) or rel.startswith(ENTITY_DIRS[0] + "/") \
                or rel.startswith(ENTITY_DIRS[1] + "/"):
            continue
        try:
            txt = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if "[[" not in txt:
            continue
        for m in pat.finditer(txt):
            stem = m.group(1).strip().split("/")[-1]
            if stem in stems:
                refs.setdefault(stem, []).append(rel)
    return refs


def _is_meta_note(p: Path) -> bool:
    """导航/说明页不算实体页 —— 按名字 + frontmatter type 双重判断。

    只看名字会漏：说明页改名后（`README.md` → `人物页说明.md`）名字集合就过期了。
    按 `type: index|home` 判一遍才与实际语义一致。
    """
    if p.name in ENTITY_SKIP:
        return True
    try:
        head = p.read_text(encoding="utf-8").split("\n---", 1)[0]
    except OSError:
        return False
    return bool(re.search(r"^type:\s*[\"']?(index|home)\b", head, re.M))


def build_entity_plan() -> dict:
    """要搬的 stale 实体页：已在 10-项目/30-人物、打了 stale、且全库无在库引用。"""
    live = _live_stems()
    stems = set()
    for folder in ENTITY_DIRS:
        for p in (ROOT / folder).glob("*.md"):
            if _is_meta_note(p):
                continue
            txt = p.read_text(encoding="utf-8")
            if re.search(r"^stale:\s*true\s*$", txt, re.M):
                stems.add(p.stem)
    refs = _inbound_refs(stems)

    plan: dict[str, list[dict]] = {}
    blocked: list[dict] = []
    for folder in ENTITY_DIRS:
        for p in sorted((ROOT / folder).glob("*.md")):
            if _is_meta_note(p):
                continue
            txt = p.read_text(encoding="utf-8")
            if not re.search(r"^stale:\s*true\s*$", txt, re.M):
                continue
            row = {"note": p.relative_to(ROOT).as_posix(), "stem": p.stem,
                   "to": (ENTITY_ARCHIVE[folder] / p.name).relative_to(ROOT).as_posix()}
            why = None
            if p.stem in live:
                why = "在库语料仍指向"
            elif refs.get(p.stem):
                why = f"仍有 {len(refs[p.stem])} 处引用（如 {refs[p.stem][0]}）"
            if why:
                row["blocked"] = why
                blocked.append(row)
            else:
                plan.setdefault(folder, []).append(row)
    return {"plan": plan, "blocked": blocked,
            "total": sum(len(v) for v in plan.values()), "live": len(live)}


def _rewrite_links(pairs: dict[str, str]) -> int:
    """把归档区里指向旧路径的 wikilink 改写成新路径。pairs: 旧link文本 → 新link文本。"""
    n = 0
    for p in DIR_ARCHIVE.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8")
        except OSError:
            continue
        if "[[" not in txt:
            continue
        orig = txt
        for old, new in pairs.items():
            txt = re.sub(r"\[\[" + re.escape(old) + r"(?=[\]|#])", "[[" + new, txt)
        if txt != orig:
            p.write_text(txt, encoding="utf-8")
            n += 1
    return n


def archive_entities_apply(info: dict) -> Path:
    pairs: dict[str, str] = {}
    moves: list[dict] = []
    for folder, rows in info["plan"].items():
        dst_dir = ENTITY_ARCHIVE[folder]
        dst_dir.mkdir(parents=True, exist_ok=True)
        for r in rows:
            src, dst = ROOT / r["note"], ROOT / r["to"]
            if not src.exists():
                continue
            if dst.exists():
                dst = dst.with_name(dst.stem + "-dup" + dst.suffix)
            shutil.move(str(src), str(dst))
            to_rel = dst.relative_to(ROOT).as_posix()
            pairs[r["note"][:-3]] = to_rel[:-3]        # wikilink 文本不带 .md
            moves.append({"stem": r["stem"], "from": r["note"], "to": to_rel})
    n_files = _rewrite_links(pairs)
    man = META / f"entity_archive_manifest_{now_cst().strftime('%Y%m%dT%H%M%S')}.json"
    man.write_text(json.dumps(
        {"at": iso(now_cst()), "moves": moves, "rewritten_notes": n_files},
        ensure_ascii=False, indent=2), encoding="utf-8")
    return man


def undo_entities(man_path: str) -> int:
    man = json.loads(Path(man_path).read_text(encoding="utf-8"))
    pairs = {}
    n = 0
    for m in man.get("moves") or []:
        src, dst = ROOT / m["to"], ROOT / m["from"]
        if not src.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        pairs[m["to"][:-3]] = m["from"][:-3]
        n += 1
    _rewrite_links(pairs)
    return n


def entity_archive_report(info: dict, applied: Path | None) -> str:
    L = ["# 实体页归档报告", "",
         f"- 时间：{iso(now_cst())}",
         f"- 在库语料指向的实体页：{info['live']} 个（保留）",
         f"- **本次移出检索面：{info['total']} 个**（stale 且无任何在库引用）",
         f"- 因仍有引用而拦下：{len(info['blocked'])} 个", ""]
    if info["plan"]:
        L += ["| 目录 | 移出 | → 归档到 |", "|---|---|---|"]
        for folder, rows in info["plan"].items():
            L.append(f"| `{folder}/` | {len(rows)} | "
                     f"`{(ENTITY_ARCHIVE[folder]).relative_to(ROOT).as_posix()}/` |")
        L.append("")
        L += ["## 样例（前 15）", ""]
        for folder, rows in info["plan"].items():
            for r in rows[:15]:
                L.append(f"- `{r['note']}` → `{r['to']}`")
        L.append("")
    if info["blocked"]:
        L += ["## 被拦下（有引用，不搬）", ""]
        for r in info["blocked"][:15]:
            L.append(f"- `{r['note']}` —— {r['blocked']}")
        L.append("")
    L += ["## 下一步", ""]
    if applied:
        L += [f"已搬迁 → `{applied.relative_to(ROOT).as_posix()}`（undo 清单在内）",
              f"回滚：`python tools/kb_prune.py --undo-entities {applied.relative_to(ROOT).as_posix()}`",
              "接着跑 `python tools/kb_insight.py --browse` 刷新 [[浏览]] 里的计数。"]
    else:
        L += ["当前为**只报告**模式。确认后执行：", "", "```",
              "python tools/kb_prune.py --archive-entities --apply",
              "python tools/kb_insight.py --browse",
              "```"]
    return "\n".join(L)


def run_entity_archive(apply: bool, out: str = "") -> None:
    info = build_entity_plan()
    applied = archive_entities_apply(info) if (apply and info["total"]) else None
    rep = entity_archive_report(info, applied)
    o = Path(out) if out else (DIR_REPORT / "实体页归档报告.md")
    o.parent.mkdir(parents=True, exist_ok=True)
    o.write_text(rep, encoding="utf-8")
    print(rep)
    print(f"\n[报告] {o.relative_to(ROOT).as_posix()}")


# ------------------------------------------------------------------ 报告

def render(plan: dict[str, list[dict]], stats: dict, samples: int, applied: Path | None) -> str:
    L = ["# 存量语料重判报告", "",
         f"- 时间：{iso(now_cst())}",
         f"- 扫描 {stats['total']} 条语料，覆盖 {stats['channels']} 个渠道",
         f"- **建议归档 {stats['archived']} 条**（占 "
         f"{(stats['archived'] / stats['total'] * 100 if stats['total'] else 0):.0f}%）",
         f"- 停用渠道：{'、'.join(stats['disabled']) or '无'}", ""]
    if not plan:
        L += ["存量语料全部通过当前规则，无需归档。", ""]
        return "\n".join(L)

    L += ["## 按渠道", "", "| 渠道 | 建议归档 | 该渠道存量 | 占比 | 主要原因 |", "|---|---|---|---|---|"]
    for ch_id, rows in sorted(plan.items(), key=lambda kv: -len(kv[1])):
        total_ch = stats["by_ch_total"].get(ch_id) or 0
        pct = f"{len(rows) / total_ch * 100:.0f}%" if total_ch else "—"
        reasons: dict[str, int] = {}
        for r in rows:
            reasons[r["reason"]] = reasons.get(r["reason"], 0) + 1
        top = "、".join(f"{k}×{v}" for k, v in sorted(reasons.items(), key=lambda kv: -kv[1]))
        L.append(f"| `{ch_id}` | {len(rows)} | {total_ch} | {pct} | {top} |")

    L += ["", "## 样例", ""]
    for ch_id, rows in sorted(plan.items(), key=lambda kv: -len(kv[1])):
        L.append(f"### {ch_id}（{len(rows)} 条）")
        for r in rows[:samples]:
            t = (r["title"] or "(无标题)").replace("|", "/")[:80]
            L.append(f"- [{r['reason']}] {t}")
        if len(rows) > samples:
            L.append(f"- …其余 {len(rows) - samples} 条见 manifest")
        L.append("")

    L += ["## 下一步", ""]
    if applied:
        L += [f"已搬运 → `{applied.relative_to(ROOT).as_posix()}`（undo 清单在内）",
              f"回滚：`python tools/kb_prune.py --undo {applied.relative_to(ROOT).as_posix()}`",
              "接着跑 `python tools/kb_reclassify.py --merge-orphans` 合并被搬空后留下的孤儿项目页。"]
    else:
        L += ["当前为**只报告**模式。确认无误后执行：", "", "```",
              "python tools/kb_prune.py --apply",
              "python tools/kb_reclassify.py --merge-orphans",
              "```"]
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="真正搬运到 80-归档/（默认只报告）")
    ap.add_argument("--undo", default="", help="按 manifest 搬回")
    ap.add_argument("--channels", default="", help="只处理指定渠道 id")
    ap.add_argument("--samples", type=int, default=5, help="每组打印多少条样例")
    ap.add_argument("--no-rules", action="store_true", help="忽略 rules.yaml（只看渠道停用）")
    ap.add_argument("--liveness", action="store_true",
                    help="只给实体页打/摘 stale 标记（不改动任何语料）")
    ap.add_argument("--archive-entities", action="store_true",
                    help="把 stale 且无人引用的实体页移进 80-归档/（默认只报告）")
    ap.add_argument("--undo-entities", default="", help="按 manifest 把实体页搬回")
    ap.add_argument("--out", default="")
    args = ap.parse_args(argv)

    seen = Seen()
    if args.undo_entities:
        n = undo_entities(args.undo_entities)
        print(f"已按 {args.undo_entities} 搬回 {n} 个实体页")
        return 0

    if args.undo:
        n = do_undo(args.undo, seen)
        print(f"已按 {args.undo} 搬回 {n} 条")
        return 0

    if args.liveness:
        liveness_report(apply=args.apply)
        return 0

    if args.archive_entities:
        run_entity_archive(apply=args.apply, out=args.out)
        return 0

    plan, stats = build_plan(args)
    applied = None
    if args.apply and plan:
        applied = do_apply(plan, seen)
        liveness_report(apply=True)      # 搬完立刻同步实体页存活标记

    rep = render(plan, stats, max(1, args.samples), applied)
    out = Path(args.out) if args.out else (DIR_REPORT / "存量重判报告.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(rep, encoding="utf-8")
    print(rep)
    print(f"\n[报告] {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
