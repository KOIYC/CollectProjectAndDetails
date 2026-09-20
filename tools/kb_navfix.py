"""kb_navfix — 存量语料页结构补齐：`topic` 字段 + 「导航」段（幂等）。

修什么问题
----------
实测 723 条语料 note **一条 wikilink 都没有**：只有项目页单向指向语料页。
于是从任意一条语料出发哪儿都去不了 —— 想看「同渠道还有什么」「这作者还做过什么」
「它属于哪个赛道」，只能回文件树手动翻。这正是「各个维度散在不同文件夹、要反复切换」
的直接来源。

本工具做四件存量补齐（新采集的条目由 kb_collect.write_corpus_note 直接写对，不需要本工具）：

  1) `topic:` —— 赛道字段。`kb_insight` 的 write_topic_tags 只覆盖 `usable()` 条目，
     且只在跑 insight 时才补，于是存量有缺口（实测 723 条中 206 条缺）。
     缺了 Bases「按赛道」视图就有空档。
  2) `shard:` / `pub_day:` —— 纯字符串日字段（入库日 / 发布日）。
     Bases 的 `groupBy` 直接分组 ISO 时间串会一条一组（等于没分），
     所以时间轴必须靠这两个字段。
  3) `kind:` 与最新记录对齐 —— `kb_reclassify` 把人物从 `10-项目/` 搬到 `30-人物/` 时，
     语料页的 `kind` 还是当初写死的 `project`，导致导航段指向已不存在的项目页（实测 3 条）。
  4) `## 导航` 段 —— 语料页的出链（项目页/人物页/渠道页/赛道/浏览入口）。

为什么不重写整页
----------------
走**定点字符串编辑**，不调 `write_note` 重新序列化 frontmatter。
723 条已有正文/评论是采集成果，重序列化有丢字段风险，且会把键序打乱、diff 噪音巨大。
本工具只动两处：frontmatter 里插一行 `topic:`，正文尾部换成新的导航段。

用法
----
  python tools/kb_navfix.py --dry            # 只统计，不落盘
  python tools/kb_navfix.py                  # 执行
  python tools/kb_navfix.py --topic-only     # 只补 topic
  python tools/kb_navfix.py --nav-only       # 只补导航段
  python tools/kb_navfix.py --archive        # 连 80-归档/ 一起修
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import (META, ROOT, Seen, fm_scalars, iso, norm_url, now_cst,  # noqa: E402
                       rotate_files, set_fm_scalar, sha1, slugify, split_note, topic_of)
from kb_collect import (corpus_note_path, method_note_path, nav_block,  # noqa: E402
                        person_note_path, project_note_path)
from kb_content_audit import load_latest                               # noqa: E402

NAV_HEAD = "\n## 导航\n"
SHARD_RE = re.compile(r"posts[/\\][^/\\]+[/\\](\d{4}-\d{2}-\d{2})[/\\]")


# ---------------------------------------------------------------- frontmatter
# split_note / fm_scalars / set_fm_scalar 已上移到 kb_common（kb_prune 也要用同一套）。


def as_item(fm: dict[str, str], body: str) -> dict:
    """拼出 nav_block() / topic_of() / is_project_ish() 认得的记录形状。"""
    return {"item_id": fm.get("item_id"), "title": fm.get("title"),
            "url": fm.get("url"), "project_url": fm.get("project_url") or None,
            "author": fm.get("author") or None, "kind": fm.get("kind") or "post",
            "source_id": fm.get("source") or "unknown", "body": body}


def strip_nav(body: str) -> str:
    """去掉已有导航段（含其后的全部内容——导航段永远写在页尾）。"""
    i = body.find(NAV_HEAD)
    if i >= 0:
        return body[:i]
    m = re.search(r"\n## 导航\s*$", body)
    if m:
        return body[:m.start()]
    return body


def apply(path: Path, *, nav: bool, topic: bool, dates: bool, sync_kind: bool,
          live: dict[str, dict]) -> set[str]:
    """就地补一条语料页的结构字段，返回本次实际改动的项名集合（空集 = 无需改）。"""
    sp = split_note(path.read_text(encoding="utf-8"))
    if sp is None:
        return {"非法frontmatter"}
    head, body = sp
    fm = fm_scalars(head)
    if not fm.get("item_id") or not fm.get("title"):
        return set()

    body_text = strip_nav(body)                    # topic 判定用「不含导航段」的正文
    rec = as_item(fm, body_text)
    changed: set[str] = set()

    # ① kind 与「最新记录」对齐。kb_reclassify 会把人物从 10-项目/ 搬到 30-人物/，
    #    但语料页的 kind 是当初写死的 —— 不同步的话导航段会指向一个已不存在的项目页。
    src = live.get(fm["item_id"])
    if sync_kind and src and src.get("kind") and src["kind"] != fm.get("kind"):
        fm["kind"] = rec["kind"] = src["kind"]
        head = set_fm_scalar(head, "kind", src["kind"])
        changed.add("对齐kind")

    if topic:
        want = topic_of(rec)
        if fm.get("topic") != want:
            head = set_fm_scalar(head, "topic", want)
            changed.add("补topic")

    # ② 纯字符串日字段：Bases 的 groupBy 靠它做时间轴（直接分组 ISO 时间串=一条一组）
    if dates:
        m = SHARD_RE.search(path.as_posix())
        if m and fm.get("shard") != m.group(1):
            head = set_fm_scalar(head, "shard", m.group(1))
            changed.add("补shard")
        pub = (fm.get("published_at") or "")[:10]
        if pub and fm.get("pub_day") != pub:
            head = set_fm_scalar(head, "pub_day", pub)
            changed.add("补pub_day")

    # ③ 导航段（出链）—— 放在最后，因为它要读前面同步过的 kind
    if nav:
        rec = as_item(fm, body_text)
        fresh = "\n".join(nav_block(rec)).rstrip() + "\n"
        new_body = body_text.rstrip() + "\n\n" + fresh
        if new_body != body:
            body = new_body
            changed.add("写导航")

    if changed:
        path.write_text(head + body, encoding="utf-8")
    return changed


# ---------------------------------------------------------------- 链接修复

LINK_RE = re.compile(r"\[\[(.+?)\]\]")
# 目标里含这些字符的多半是正文里的代码片段/伪链接（如 [["$line" == *"x"*]]），不动
LINK_JUNK = re.compile(r"[\[\]\"`$*\\]")


def _note_index() -> tuple[dict[str, Path], dict[str, list[Path]]]:
    notes = [p for p in ROOT.rglob("*.md")
             if not any(part.startswith(".") for part in p.relative_to(ROOT).parts)]
    by_rel = {p.relative_to(ROOT).with_suffix("").as_posix(): p for p in notes}
    by_name: dict[str, list[Path]] = {}
    for p in notes:
        by_name.setdefault(p.stem, []).append(p)
    return by_rel, by_name


def fix_links(apply: bool) -> Counter:
    """把「路径失效但按文件名仍唯一可解析」的 wikilink 改写成新路径。

    为什么需要：kb_prune 搬语料（20-语料→80-归档/posts）与 `--archive-entities` 搬实体页
    （10-项目→80-归档/项目）都是**移动**。Obsidian 里路径式链接（`[[20-语料/...]]`）
    搬家即断。本工具用文件名兜底定位唯一目标，写回新路径。

    只处理**带路径**的链接：Obsidian 对 `[[短名]]` 本来就按文件名解析，
    改写成全路径属于无意义 churn（实测会误报 1900+ 条）。文件名不唯一 / 完全找不到的
    也不动 —— 宁可留断链，也不猜错目标。
    """
    by_rel, by_name = _note_index()
    stat: Counter = Counter()
    samples: list[str] = []
    for p in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in p.relative_to(ROOT).parts):
            continue
        txt = p.read_text(encoding="utf-8")
        if "[[" not in txt:
            continue
        fixed: list[str] = []

        def repl(m: re.Match) -> str:
            core = m.group(1).split("|")[0].split("#")[0].strip()
            if not core:
                return m.group(0)
            if core in by_rel:
                stat["路径已有效"] += 1
                return m.group(0)
            # 「含 wikilink 语法字符的旧链接」：--fix-names 曾把 A[1].md 改成 A1.md，
            # 但只改了指向**当时能识别**的目标；如果这个链接在改名前已经写死成
            # `[[20-语料/.../A[1]]]` 这种带 `[` 的完整路径，Obsidian 也认不出来，
            # 于是 ④ 视它为伪代码跳过、⑥ 视它为零入链。这类链接必须能自救 —— 拿
            # 去字符化的 basename 反查唯一命中就改写；不唯一 / 找不到就仍跳过。
            if LINK_JUNK.search(core):
                if "/" not in core:
                    stat["跳过(代码/伪链接)"] += 1
                    return m.group(0)
                tail = core.split("/")[-1]
                cleaned = LINK_JUNK.sub("", tail).strip("-_. ")
                cand = by_name.get(cleaned) or []
                if len(cand) != 1:
                    stat["跳过(代码/伪链接)"] += 1
                    return m.group(0)
                new = cand[0].relative_to(ROOT).with_suffix("").as_posix()
                stat["改写为新路径"] += 1
                fixed.append(f"{core} -> {new}")
                if len(samples) < 12:
                    samples.append(f"[{p.relative_to(ROOT).as_posix()}] {core} -> {new}")
                return m.group(0).replace(core, new, 1)
            if "/" not in core:
                stat["短名链接(天然有效)"] += 1
                return m.group(0)
            cand = by_name.get(core.split("/")[-1]) or []
            if len(cand) != 1:
                stat["无法定位(歧义/缺失)" if cand else "目标不存在"] += 1
                return m.group(0)
            new = cand[0].relative_to(ROOT).with_suffix("").as_posix()
            if new == core:
                return m.group(0)
            stat["改写为新路径"] += 1
            fixed.append(f"{core} -> {new}")
            if len(samples) < 12:
                samples.append(f"[{p.relative_to(ROOT).as_posix()}] {core} -> {new}")
            return m.group(0).replace(core, new, 1)

        new_txt = LINK_RE.sub(repl, txt)
        if apply and new_txt != txt:
            p.write_text(new_txt, encoding="utf-8")
            stat["改动文件"] += 1
    print(f"fix-links  apply={apply}  {dict(stat)}")
    if not apply and samples:
        print("  样例：")
        for s in samples[:12]:
            print(f"    {s}")
    return stat


# ---------------------------------------------------------------- 文件名修复

NAME_DIRS = ("20-语料", "80-归档", "10-项目", "30-人物")


def _rec_index() -> tuple[dict[str, dict], dict[str, dict]]:
    """① item_id → 最新记录；② note 名尾部 8 位 url 指纹 → 记录（实体页反查用）。"""
    by_id: dict[str, dict] = {}
    by_hash: dict[str, dict] = {}
    dup: set[str] = set()
    for r in load_latest(live_only=False):
        iid = r.get("item_id")
        if iid:
            by_id.setdefault(iid, r)
        key = r.get("project_url") or r.get("url")
        if not key:
            continue
        h = sha1(norm_url(key), 8)
        if h in by_hash:
            dup.add(h)
            continue
        by_hash[h] = r
    for h in dup:
        by_hash.pop(h, None)          # 指纹撞车就弃用，别猜
    return by_id, by_hash


def canon_stem(path: Path, by_id: dict[str, dict], by_hash: dict[str, dict]) -> str | None:
    """按**当前** slug 规则重算该 note 的规范文件名 stem（算不出返回 None）。

    为什么从记录反算而不是「把现名 sanitize 一遍」：文件名是 title 派生出来的
    （`{item_id}_{slug(title,50)}` / `{slug(name,48)}_{url指纹}`），而 sanitize 现名
    得到的是「已截断、已改写过的字符串再 sanitize」，两者在连字符与截断边界上会差一两个字符。
    反算才与采集端下次写出的名字**逐字节一致** —— 否则改名当天不漂，下次采集就漂。
    """
    sp = split_note(path.read_text(encoding="utf-8"))
    fm = fm_scalars(sp[0]) if sp else {}
    iid = fm.get("item_id")
    if iid and iid in by_id:
        m = re.search(r"posts[/\\][^/\\]+[/\\](\d{4}-\d{2}-\d{2})[/\\]", path.as_posix())
        return corpus_note_path(by_id[iid], m.group(1) if m else "").stem
    rec = by_hash.get(path.stem.rsplit("_", 1)[-1])
    if rec:
        kind = (rec.get("kind") or "").lower()
        if kind == "person":
            fn = person_note_path
        elif kind == "method":
            fn = method_note_path
        else:
            fn = project_note_path
        return fn(rec).stem
    return None


def _rewrite_stem_links(pairs: dict[str, str], apply: bool) -> int:
    """按「旧 stem → 新相对路径」改写全库 wikilink（短名与路径式都覆盖）。"""
    changed = 0
    for p in sorted(ROOT.rglob("*.md")):
        if any(part.startswith(".") for part in p.relative_to(ROOT).parts):
            continue
        txt = p.read_text(encoding="utf-8")
        if "[[" not in txt:
            continue

        def repl(m: re.Match) -> str:
            raw = m.group(1).split("|")[0].strip()
            core = raw.split("#")[0].strip()
            if not core:
                return m.group(0)
            # 先按原样（不切 #）匹配：文件名本身可能含 `#`（如 `...week-#196.md`），
            # 那种链接的完整目标就是文件名，切开反而找不到。
            for key, still in ((raw, raw), (core, core)):
                new = pairs.get(key.split("/")[-1])
                if new and new != key:
                    return m.group(0).replace(still, new, 1)
            return m.group(0)

        new_txt = LINK_RE.sub(repl, txt)
        if new_txt != txt:
            changed += 1
            if apply:
                p.write_text(new_txt, encoding="utf-8")
    return changed


def fix_names(apply: bool) -> Counter:
    """把文件名里的 wikilink 语法字符清掉（幂等）。

    为什么：`slugify` 原先只挡 Windows 非法字符，漏了 `[ ] # ^`。这些字符在
    Obsidian 里是**语法字符** —— `#` 被解析成标题锚点、`]` 被当成链接收尾，
    于是带这类名字的 note 谁引用谁断链（实测 13 个文件 → 20 处死链）。
    同时把 `seen.json` 里的 note 路径与新名同步，否则采集端会以为语料还在老路径。
    """
    stat: Counter = Counter()
    moves: list[dict] = []
    pairs: dict[str, str] = {}
    by_id, by_hash = _rec_index()
    for top in NAME_DIRS:
        for p in sorted((ROOT / top).rglob("*.md")):
            if p.stem.endswith("-dup"):            # kb_prune 归档时撞名留下的副本，本就是重名物
                continue
            want = canon_stem(p, by_id, by_hash) or slugify(p.stem, 120)
            if want == p.stem:
                continue
            dst = p.with_name(want + ".md")
            if dst.exists():
                stat["跳过(重名)"] += 1
                if stat["跳过(重名)"] <= 6:
                    print(f"  [重名] {p.relative_to(ROOT).as_posix()} → 目标已存在 {want}.md")
                continue
            stat["待改名"] += 1
            stat["有记录反算" if want != slugify(p.stem, 120) else "仅按规则清字符"] += 1
            old_rel = p.relative_to(ROOT).as_posix()
            new_rel = dst.relative_to(ROOT).as_posix()
            pairs[p.stem] = new_rel[:-3]
            moves.append({"from": old_rel, "to": new_rel})
            if apply:
                p.rename(dst)
                stat["已改名"] += 1
            if len(moves) <= 15:
                print(f"  {old_rel}\n    -> {new_rel}")

    if apply and moves:
        seen = Seen()
        n = 0
        for m in moves:
            for meta in seen.items.values():
                if meta.get("note") == m["from"]:
                    meta["note"] = m["to"]
                    n += 1
        seen.save()
        stat["同步seen"] = n
        nf = _rewrite_stem_links(pairs, apply=True)
        stat["改写文件"] = nf
        man = META / f"rename_manifest_{now_cst().strftime('%Y%m%dT%H%M%S')}.json"
        man.write_text(json.dumps({"at": iso(now_cst()), "moves": moves,
                                   "pairs": pairs}, ensure_ascii=False, indent=2),
                       encoding="utf-8")
        rotate_files(META, "rename_manifest_", 12)          # 工作区只留近 12 份（git 历史兜底）
        print(f"[manifest] {man.relative_to(ROOT).as_posix()}")

    print(f"fix-names  apply={apply}  {dict(stat)}")
    return stat


def undo_names(man_path: str) -> int:
    man = json.loads(Path(man_path).read_text(encoding="utf-8"))
    pairs = {}
    seen = Seen()
    n = 0
    for m in man.get("moves") or []:
        src, dst = ROOT / m["to"], ROOT / m["from"]
        if not src.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)
        pairs[Path(m["to"]).stem] = m["from"][:-3]
        for meta in seen.items.values():
            if meta.get("note") == m["to"]:
                meta["note"] = m["from"]
        n += 1
    seen.save()
    _rewrite_stem_links(pairs, apply=True)
    return n


# ---------------------------------------------------------------- cli

def main() -> int:
    ap = argparse.ArgumentParser(description="存量语料页补 topic/shard/pub_day + 导航段（幂等）")
    ap.add_argument("--dry", action="store_true", help="只统计，不落盘")
    ap.add_argument("--nav-only", action="store_true", help="只补导航段")
    ap.add_argument("--topic-only", action="store_true", help="只补 topic")
    ap.add_argument("--no-dates", action="store_true", help="不补 shard/pub_day")
    ap.add_argument("--archive", action="store_true", help="连 80-归档/ 一起处理")
    ap.add_argument("--fix-links", action="store_true",
                    help="修复搬家后失效的 wikilink（按文件名唯一兜底改写路径）")
    ap.add_argument("--fix-names", action="store_true",
                    help="清掉文件名里的 wikilink 语法字符 [ ] # ^（同步 seen.json）")
    ap.add_argument("--undo-names", default="", help="按 manifest 把文件名改回")
    a = ap.parse_args()

    if a.undo_names:
        n = undo_names(a.undo_names)
        print(f"已按 {a.undo_names} 改回 {n} 个文件")
        return 0

    if a.fix_names:
        fix_names(apply=not a.dry)
        return 0

    if a.fix_links:
        fix_links(apply=not a.dry)
        return 0

    kw = {"nav": not a.topic_only, "topic": not a.nav_only,
          "dates": not a.no_dates, "sync_kind": True}
    roots = [ROOT / "20-语料"] + ([ROOT / "80-归档"] if a.archive else [])

    # 最新记录：kind 对齐的权威来源（与写实体页时同源）
    live = {r["item_id"]: r for r in load_latest(live_only=False) if r.get("item_id")}

    notes = sorted(p for r in roots for p in r.rglob("*.md"))
    print(f"扫描 {len(notes)} 条语料 note  {kw}  dry={a.dry}", flush=True)

    stat: Counter = Counter()
    kinds: Counter = Counter()
    for p in notes:
        sp = split_note(p.read_text(encoding="utf-8"))
        if sp is None:
            stat["非法frontmatter"] += 1
            continue
        fm = fm_scalars(sp[0])
        kinds[fm.get("kind") or "?"] += 1
        if a.dry:
            if kw["topic"] and "topic" not in fm:
                stat["缺topic"] += 1
            if kw["dates"] and "shard" not in fm:
                stat["缺shard"] += 1
            if kw["nav"]:
                if NAV_HEAD not in sp[1]:
                    stat["缺导航"] += 1
                else:
                    # 光看「有没有导航段」查不出**内容过期**（如实体页准入改了，
                    # 非项目条目不该再出项目页链接）。所以按实际重算一遍比对。
                    body_text = strip_nav(sp[1])
                    sec = sp[1][sp[1].find(NAV_HEAD) + len(NAV_HEAD):]
                    cur = {ln for ln in sec.splitlines() if ln.startswith("- ")}
                    new = {ln for ln in nav_block(as_item(fm, body_text)) if ln.startswith("- ")}
                    if cur != new:
                        stat["导航内容过期"] += 1
            continue
        for c in apply(p, live=live, **kw):
            stat[c] += 1

    print(f"kind 分布: {dict(kinds)}")
    print(f"结果: {dict(stat)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
