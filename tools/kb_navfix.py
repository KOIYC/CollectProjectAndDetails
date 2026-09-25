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
from kb_common import (META, ROOT, Seen, del_fm_scalar, fm_scalars, iso,  # noqa: E402
                       norm_url, now_cst, pub_day_of, rotate_files, set_fm_scalar,
                       sha1, slugify, split_note, strip_code, topic_of, write_ledger,
                       _atomic_write, _BAD)
from kb_collect import (corpus_note_path, method_note_path, nav_block,  # noqa: E402
                        person_note_path, project_note_path, write_entity_note)
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
          live: dict[str, dict], write: bool = True) -> set[str]:
    """就地补一条语料页的结构字段，返回本次实际改动的项名集合（空集 = 无需改）。

    `write=False` 时只算不写 —— 干跑（`--dry`）必须走这条路径，**不许另写一套简化判据**。
    历史教训：--dry 曾自己实现一份只认 topic/shard/导航 的检测器，于是它报的「结果」
    与真跑实际改的东西**不是同一个集合**（pub_day 归一化、导航过期都不在其中）。
    后果不是少报几个数字，而是「连跑两次第二次必须为空」这条幂等验证失效 ——
    干跑说没事、真跑改了 25 处，第二天再干跑又说没事。
    """
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

    # ①b project_url 与「最新记录」对齐 —— **只在内存里**，不写进 frontmatter。
    #     语料页 frontmatter 不带 project_url（它是 collect 端从正文外链回退推导的，存在 raw/seen），
    #     于是 nav_block 会退回用 item url 推实体页名，算出**与 healthcheck ② 不同的名字**
    #     （② 用 live 记录的 project_url）。后果：`--repair-links` 刚把链接修成规范名，
    #     navfix 下一次跑又把它写回旧名 —— ④ 断链「修好了又坏」（2026-09-21 实测 4 条）。
    #     两端同源（都用 live 记录）才不会互相打架。
    if src and src.get("project_url") and not rec.get("project_url"):
        rec["project_url"] = src["project_url"]

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
        # 归一化后可能得 None（渠道没给发布日，如 betalist/indiehackers）——
        # 此时要么不写该字段，要么把裸切出来的垃圾值（`Thu, 17 Se` / `N/A`）清掉，
        # 否则它会永远占着 Bases 时间轴的一个假分组。
        pub = pub_day_of(fm.get("published_at"))
        if pub and fm.get("pub_day") != pub:
            head = set_fm_scalar(head, "pub_day", pub)
            changed.add("补pub_day")
        elif not pub and fm.get("pub_day"):
            head = del_fm_scalar(head, "pub_day")
            changed.add("清坏pub_day")

    # ③ 导航段（出链）—— 放在最后，因为它要读前面同步过的 kind + project_url（rec 已就地更新）
    if nav:
        fresh = "\n".join(nav_block(rec)).rstrip() + "\n"
        new_body = body_text.rstrip() + "\n\n" + fresh
        if new_body != body:
            body = new_body
            changed.add("写导航")

    if changed and write:
        # 整页重写走原子替换：中断/AV 占用会把已有正文截断成半截页（采集端 write_note 同源）
        _atomic_write(path, head + body)
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
        # 只认「真链接」：行内代码 / 围栏代码块里的 `[[...]]` 是**举例文本**（运行日志里记
        # 「本轮修过哪条断链」就是这么写的），不是链接。健康检查 ④ 一直剥离代码段
        # （kb_common.strip_code），本工具不剥就会把这类示例报成「目标不存在」——
        # 两个工具对「什么算链接」口径不一，读报表的人会以为库里真有断链（实测 1 条假警报）。
        # strip_code 用**等长空白**占位，偏移与原文一一对应，所以能直接用 m.start() 判定。
        scan = strip_code(txt)
        in_code = [scan[i] != txt[i] for i in range(len(txt))] if len(scan) == len(txt) else []
        fixed: list[str] = []

        def repl(m: re.Match) -> str:
            if in_code and in_code[m.start()]:
                stat["跳过(代码/伪链接)"] += 1
                return m.group(0)
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
            _atomic_write(p, new_txt)            # 全库逐页重写：半截页 = 整篇正文陪葬
            stat["改动文件"] += 1
    print(f"fix-links  apply={apply}  {dict(stat)}")
    if not apply and samples:
        print("  样例：")
        for s in samples[:12]:
            print(f"    {s}")
    return stat


# ---------------------------------------------------------------- 文件名修复

NAME_DIRS = ("20-语料", "80-归档", "10-项目", "30-人物")
_LIVE_DIRS = ("20-语料", "10-项目", "30-人物", "40-方法论")   # 撞名判定用的「在库」集合
_DUP_RE = re.compile(r"-dup\d*$")


def _archived_dst(stem: Path) -> Path:
    """归档区消歧后缀：-dup 被 kb_prune 占用过就顺延 -dup2/-dup3……"""
    dst = stem.with_name(stem.stem + "-dup" + stem.suffix)
    n = 1
    while dst.exists():
        n += 1
        dst = stem.with_name(f"{stem.stem}-dup{n}" + stem.suffix)
    return dst


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
                _atomic_write(p, new_txt)        # 同上：改名链路的链接改写也不能留半截页
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
    # 冻结区（决策 2026-09-20「80-归档=冻结快照，规则变了也不跟着改名」）：
    # 归档页**不做**规范名反算——归档名是历史事实；只允许两类改名：
    #   ① 语法字符清理（[ ] # ^ 等，否则断链检查有盲区）；
    #   ② 与在库页撞 stem、或**归档内部跨分片撞 stem** 的消歧（kb_prune -dup 先例）
    #      ——这类**不**登记进 pairs，消歧后裸 [[短名]] 唯一指向在库页/最新归档份。
    #   归档内部同名多源于「归档→回填迁移→再归档」链（backfill 迁移 bug 遗留，
    #   2026-09-21 清出 3 例）：保留日期最大分片那份，旧份加 -dupN。
    live_stems = {q.stem for top in _LIVE_DIRS for q in (ROOT / top).rglob("*.md")}
    arch_by_stem: dict[str, list[Path]] = {}
    for q in sorted((ROOT / "80-归档").rglob("*.md")):   # 字典序：日期桶自然从旧到新
        if not _DUP_RE.search(q.stem):
            arch_by_stem.setdefault(q.stem, []).append(q)
    arch_stale = {p for paths in arch_by_stem.values() if len(paths) > 1 for p in paths[:-1]}
    for top in NAME_DIRS:
        for p in sorted((ROOT / top).rglob("*.md")):
            if _DUP_RE.search(p.stem):             # kb_prune/本工具消歧留下的副本，本就是重名物
                continue
            disambig = False                       # 纯消歧改名（stem 文本不变）→ 不改写链接
            if top == "80-归档":
                want = slugify(p.stem, 120)
                disambig = p.stem in live_stems or p in arch_stale
                if want == p.stem and not disambig:
                    continue
                base = p.with_name(want + ".md") if want != p.stem else p
                dst = _archived_dst(base) if disambig else base
            else:
                want = canon_stem(p, by_id, by_hash) or slugify(p.stem, 120)
                if want == p.stem:
                    continue
                dst = p.with_name(want + ".md")
            if dst.exists():
                stat["跳过(重名)"] += 1
                if stat["跳过(重名)"] <= 6:
                    print(f"  [重名] {p.relative_to(ROOT).as_posix()} → 目标已存在 {dst.name}")
                continue
            stat["待改名"] += 1
            if top == "80-归档":
                stat["归档消歧" if p.stem in live_stems else "归档语法清理"] += 1
            else:
                stat["有记录反算" if want != slugify(p.stem, 120) else "仅按规则清字符"] += 1
            old_rel = p.relative_to(ROOT).as_posix()
            new_rel = dst.relative_to(ROOT).as_posix()
            if apply:
                # 上面的 dst.exists() 只是先验：Windows 下目标可能在这一步复现或被
                # Obsidian/AV 占用（WinError 5/183）→ 单条失败必须跳过继续，整轮不许挂。
                # 且**没改成就不登记** moves/pairs：manifest 里多出没发生的改名，
                # --undo-names 会把还站在原地的页「搬回」一个假路径。
                try:
                    p.rename(dst)
                except OSError as e:
                    stat["改名失败"] += 1
                    if stat["改名失败"] <= 6:
                        print(f"  [改名失败] {old_rel} → {dst.name}: {str(e)[:60]}")
                    continue
                stat["已改名"] += 1
            if not disambig or want != p.stem:     # 文本有变（反算/清字符）才改写链接；纯消歧不动
                pairs[p.stem] = new_rel[:-3]       # 裸消歧不加 pairs：[[短名]] 应解析到在库页/最新份
            moves.append({"from": old_rel, "to": new_rel})
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
        # manifest 是 undo 的唯一凭证，必须原子写：半截 JSON 会让 --undo-names 当场抛在
        # json.loads 上（撤销能力直接没了）。lock_name 用族名而非带时间戳的 path.stem，
        # 否则每份 manifest 都在 _meta 留一个永不回收的 .lock 文件。
        write_ledger(man, {"at": iso(now_cst()), "moves": moves, "pairs": pairs},
                     lock_name="rename_manifest", indent=2)
        rotate_files(META, "rename_manifest_", 12)          # 工作区只留近 12 份（git 历史兜底）
        print(f"[manifest] {man.relative_to(ROOT).as_posix()}")

    print(f"fix-names  apply={apply}  {dict(stat)}")
    return stat


def undo_names(man_path: str) -> int:
    """按 manifest 把文件名改回。单条搬不动不许中断整轮 —— undo 必须能续跑。

    与 kb_prune 的搬运自验同一口径：只有「老名不在了 + 新名在」才算改回，
    没落地的既不写 seen/链接，也绝不记进成功数；未生效清单写回 manifest 留痕。
    """
    man_file = Path(man_path)
    man = json.loads(man_file.read_text(encoding="utf-8"))
    todo = man.get("moves") or []
    pairs: dict[str, str] = {}
    seen = Seen()
    bad: list[dict] = []
    n = 0
    for m in todo:
        src, dst = ROOT / m["to"], ROOT / m["from"]
        if not src.exists():
            if not dst.exists():                 # 两头都没有 = 页真丢了，不能当「已改回」
                bad.append({"from": m["to"], "to": m["from"], "skipped": "src-missing"})
                continue
            # 已在原位 = 上一轮改回过；seen/链接可能还记着新名，这里照样补一遍（幂等续跑）
        else:
            if dst.exists():
                # 老名被重新采集/新建占住：覆盖=丢一份在库页，只跳过不猜（同 fix_names 取舍）
                bad.append({"from": m["to"], "to": m["from"], "skipped": "dst-exists"})
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            try:
                src.rename(dst)                  # 目标这一步复现 / 文件被占用（WinError 5）
            except OSError as e:
                bad.append({"from": m["to"], "to": m["from"], "failed": str(e)[:60]})
                continue
            if src.exists() or not dst.exists():
                bad.append({"from": m["to"], "to": m["from"], "unverified": True})
                continue
        pairs[Path(m["to"]).stem] = m["from"][:-3]
        for meta in seen.items.values():
            if meta.get("note") == m["to"]:
                meta["note"] = m["from"]
        n += 1
    seen.save()
    _rewrite_stem_links(pairs, apply=True)
    if not bad:
        if "undo_unverified" in man:             # 本轮全改回了：清掉上一轮的未生效，别留假警
            man.pop("undo_unverified")
            write_ledger(man_file, man, lock_name="rename_manifest", indent=2)
        return n
    print(f"[!] 改名未改回 {len(bad)}/{len(todo)} 条（源缺失 / 目标已存在 / 改名报错 / 未生效）"
          f"—— 这些页仍叫 manifest 里的新名，处理后可重跑同一条 --undo-names：", flush=True)
    for b in bad[:10]:
        why = b.get("skipped") or b.get("failed") or "unverified"
        print(f"     {b['from']} -> {b['to']}  {why}", flush=True)
    man["undo_unverified"] = bad                 # 只打在终端 = 下一轮无从核对，落盘留痕
    write_ledger(man_file, man, lock_name="rename_manifest", indent=2)
    return n


def fix_note_paths(apply: bool) -> int:
    """以**磁盘为准**订正 `seen.note` —— 修「账本与磁盘脱节」（healthcheck ⑤ 的孤儿/幽灵）。

    为什么以磁盘为准而不是反过来：语料页是给人看的最终产物，账本只是索引。
    写页成功但账本没跟上（实测：写盘被 AV/占用打断、`os.replace` 抛 WinError 5），
    或跨零点日期桶漂移，都会留下「页在盘上、账上没有」的孤儿 —— 它不进审计、
    不进洞察、项目页的观测历史指向打不开的路径。改账本比删页安全且可回退。

    不动的类型（只报不改）：
      · 账本指向 `80-归档/` 而磁盘另有在库页 —— 说明同一条既归档又在库，是归档搬运
        残件，得先清 `kb_prune --dedupe-archive`，不能靠改账本掩盖；
      · 磁盘有页但账本**没有该 item** —— 从未入库的野页，需人工确认来源。
    """
    seen = Seen()
    disk: dict[str, str] = {}
    for p in (ROOT / "20-语料").rglob("*.md"):
        txt = p.read_text(encoding="utf-8")
        iid = None
        for ln in txt.splitlines()[:40]:
            m = re.match(r"^item_id:\s*(.+?)\s*$", ln)
            if m:
                iid = m.group(1).strip().strip('"')
                break
        if iid:
            disk[iid] = p.relative_to(ROOT).as_posix()

    # 账本无此 item 分两种，处理完全不同：
    #   · raw 里有最新记录 → 页是**真货**，只是记账那一步被打断（实测写盘抛 WinError 5）。
    #     补一条账本记录即可（`Seen.touch`），页原地保留；
    #   · raw 里也没有 → 磁盘上的野页，留在 20-语料 会永久顶着 ① 计数且无任何观测史，隔离。
    live = {r["item_id"]: r for r in load_latest(live_only=False) if r.get("item_id")}
    fixes, archived, recover, wild = [], [], [], []
    for iid, rel in sorted(disk.items()):
        rec = seen.items.get(iid)
        if rec is None:
            (recover if iid in live else wild).append((iid, rel))
            continue
        cur = str(rec.get("note") or "")
        if cur == rel:
            continue
        if cur.startswith("80-归档/"):
            archived.append((iid, cur, rel))
            continue
        fixes.append((iid, cur, rel))

    print(f"账本待订正 {len(fixes)} 条 · 已归档却另有在库页 {len(archived)} 条 · "
          f"raw 有记录可补账 {len(recover)} 条 · 野页 {len(wild)} 条")
    for iid, cur, rel in fixes[:10]:
        print(f"    {iid}: 账={cur or '(空)'}  →  盘={rel}")
    for iid, cur, rel in archived[:5]:
        print(f"    [!] {iid} 归档页与在库页并存（先跑 kb_prune --dedupe-archive）：{cur} / {rel}")
    for iid, rel in recover[:5]:
        print(f"    {iid} 页在盘上但账本漏记（写盘被打断）→ 补账 {rel}")
    for iid, rel in wild[:5]:
        print(f"    [!] {iid} raw 也无记录（野页）：{rel}")
    if not apply:
        print("  （只报告；不带 --dry 才落盘）")
        return len(fixes) + len(recover)
    for iid, _cur, rel in fixes:
        seen.items[iid]["note"] = rel
    for iid, rel in recover:
        r = live[iid]
        seen.touch(iid, r["source_id"], rel, None)
        try:
            write_entity_note(r, rel)          # 顺带补实体页与观测历史（② 缺页常一起出现）
        except Exception as e:                 # noqa: BLE001
            print(f"    [!] 实体页重建失败 {iid}: {str(e)[:60]}")
    seen.save()
    print(f"  已订正 {len(fixes)} 条 · 补账 {len(recover)} 条")

    if wild:
        ts = now_cst().strftime("%Y%m%dT%H%M%S")
        n = 0
        for iid, rel in wild:
            src = ROOT / rel
            dst = ROOT / "80-归档" / "野页" / ts / rel[len("20-语料/"):]
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.exists():
                # 同日重跑会撞上一轮的隔离副本 —— replace 是覆盖语义，绝不能拿它当搬运工。
                print(f"    [!] 目标已存在，跳过 {rel}（防覆盖 80-归档/野页/{ts}/ 现有副本）")
                continue
            try:
                src.replace(dst)
                n += 1
            except OSError as e:
                print(f"    [!] 移不动 {rel}: {str(e)[:60]}")
        print(f"  已隔离野页 {n} 个 → 80-归档/野页/{ts}/（raw 无记录，不参与统计）")
    return len(fixes) + len(recover)


def fix_note_remnants(apply: bool) -> int:
    """清「同一 item 在语料区留下多份页」的**改名残留**（幂等；只保留 `seen.note` 指向的那份）。

    成因：语料页名 = `item_id_标题slug`，而 `seen.note` 是唯一权威路径。条目**改标题**后
    （实测：bilibili 视频《零基础入行…》改名《手机能戒手机瘾…》），采集端在规范路径写出新页，
    旧页没人清 → 同一 item 两份语料：
      · healthcheck ①（`20-语料` 页数 == 在库唯一条目数）当场差 1；
      · 旧页永远停在改名前的内容，却仍被按 `*.md` glob 计数与被索引扫描。

    为什么删旧页安全：同一 item 的内容已在规范路径重写；`90-原始/` 只追加（标题的历史值在里面）、
    git 是第二份备份；且删除同时**改写指向旧名的链接**（否则 ④ 断链）。

    不动的类型（只报不改）：
      · 组内找不到 `seen.note` 指向的那份 → 无法判定谁是规范名（可能账本漂移），转 `--fix-note-paths`；
      · `seen.note` 落在 `80-归档/` → 同一条既归档又在库，属归档搬运残件，先 `kb_prune --dedupe-archive`。
    """
    seen = Seen()
    disk: dict[str, list[str]] = {}
    for p in sorted((ROOT / "20-语料").rglob("*.md")):
        iid = None
        for ln in p.read_text(encoding="utf-8").splitlines()[:40]:
            m = re.match(r"^item_id:\s*(.+?)\s*$", ln)
            if m:
                iid = m.group(1).strip().strip('"')
                break
        if iid:
            disk.setdefault(iid, []).append(p.relative_to(ROOT).as_posix())

    dups = {i: v for i, v in disk.items() if len(v) > 1}
    plans: list[tuple[str, str, str]] = []
    unknown: list[tuple[str, str, list[str]]] = []
    archived: list[tuple[str, str, list[str]]] = []
    for iid, rels in sorted(dups.items()):
        cur = str((seen.items.get(iid) or {}).get("note") or "")
        if cur.startswith("80-归档/"):
            archived.append((iid, cur, rels))
            continue
        if not cur or cur not in rels:
            unknown.append((iid, cur, rels))
            continue
        plans += [(iid, r, cur) for r in rels if r != cur]

    print(f"同一 item 多份语料 {len(dups)} 组 · 待清残件 {len(plans)} 个 · "
          f"无法判定 {len(unknown)} · 归档并存 {len(archived)}")
    for iid, old, keep in plans[:10]:
        print(f"    {iid}: 删 {Path(old).name}\n        留 {keep}")
    for iid, cur, rels in (unknown + archived)[:5]:
        print(f"    [!] {iid} 账本={cur or '(空)'} 盘上 {len(rels)} 份 → 不猜，只报")
    if not apply:
        print("  （只报告；不带 --dry 才落盘）")
        return len(plans)

    ts = now_cst().strftime("%Y%m%dT%H%M%S")
    man_file = META / f"corpus_remnant_manifest_{ts}.json"
    man = {"at": iso(now_cst()), "kind": "corpus_remnant",
           "note": "同名 item 多份语料的改名残留清理；undo 需把 from 从 git 历史恢复",
           "removed": [], "skipped": [], "unknown": [i for i, _, _ in unknown],
           "archived_coexist": [i for i, _, _ in archived]}
    pairs: dict[str, str] = {}
    for iid, old_rel, keep in plans:
        src = ROOT / old_rel
        try:
            src.unlink()
        except OSError as e:                     # 占用/权限：记下不硬来
            man["skipped"].append({"item_id": iid, "from": old_rel, "failed": str(e)[:60]})
            continue
        if src.exists():                         # 删了还在 = 未生效，不能当已清
            man["skipped"].append({"item_id": iid, "from": old_rel, "unverified": True})
            continue
        man["removed"].append({"item_id": iid, "from": old_rel, "kept": keep})
        pairs[Path(old_rel).stem] = keep[:-3] if keep.endswith(".md") else keep

    n = _rewrite_stem_links(pairs, apply=True) if pairs else 0
    if not (man["removed"] or man["skipped"]):   # 空跑不留空 manifest（免得把 12 份配额挤掉真记录）
        print("  无残件可清（幂等复跑）")
        return 0
    write_ledger(man_file, man, lock_name="rename_manifest", indent=2)
    rotate_files(META, "corpus_remnant_manifest_", 12)
    print(f"  已清残件 {len(man['removed'])} 个 · 改写链接 {n} 条 · 跳过 {len(man['skipped'])}"
          f" · manifest {man_file.name}")
    if man["skipped"]:
        for b in man["skipped"][:5]:
            print(f"    [!] 未清 {b['from']}  {b.get('failed') or 'unverified'}")
    return len(man["removed"])


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
    ap.add_argument("--fix-note-paths", action="store_true",
                    help="以磁盘实际路径为准订正 seen.json 的 note（修孤儿页/幽灵账），幂等")
    ap.add_argument("--fix-note-remnants", action="store_true",
                    help="清同一 item 的改名残留（同目录多份语料页），只保留 seen.note 那份")
    a = ap.parse_args()

    if a.fix_note_remnants:
        fix_note_remnants(apply=not a.dry)
        return 0

    if a.fix_note_paths:
        fix_note_paths(apply=not a.dry)
        return 0

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
        # 干跑与真跑共用同一个 apply()，只靠 write 开关区分。
        # 这样 --dry 报出的计数就是「真跑会改的条数」，幂等验证才可信。
        for c in apply(p, live=live, write=not a.dry, **kw):
            stat[c] += 1

    print(f"kind 分布: {dict(kinds)}")
    print(f"结果: {dict(stat)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
