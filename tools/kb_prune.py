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

from kb_common import (DIR_RAW, DIR_REPORT, META, ROOT, Seen, is_project_ish, iso,  # noqa: E402
                       load_ndjson, now_cst, rotate_files, write_ledger, _atomic_write)
from kb_collect import (apply_rules, load_registry, load_rules,  # noqa: E402
                        person_note_path, project_note_path)

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
    _atomic_write(path, fm + add + rest)     # 整页重写：搬完再截断，等于把冻结区写成半截页


def _entity_stem_of(p: Path) -> str:
    """实体页的「逻辑名」：去掉 `_free_dup_name` 顺延出来的 `-dupN` 尾巴。

    实体页没有 item_id 可依，只能用名字认条；`-dup/-dup2/-dup3` 是同一页的副本，
    去掉尾巴后同名即同条。
    """
    return re.sub(r"-dup\d*$", "", p.stem)


def _free_dup_name(dst: Path) -> Path:
    """归档撞名顺延 -dup/-dup2/-dup3……直到空位。

    为什么必须循环：单发 `-dup` 在「归档→再采集→再归档」链下会**静默覆盖**
    已存在的 -dup（shutil.move 对已存在目标是覆盖语义），烧掉一份冻结区历史。
    （2026-09-20 修：fix-names 归档消歧会批量造出 -dupN 链，此坑从罕见变必踩。）
    """
    if not dst.exists():
        return dst
    cand = dst.with_name(dst.stem + "-dup" + dst.suffix)   # 先例：裸 -dup 打头（fix-names 同序）
    n = 1
    while cand.exists():
        n += 1
        cand = dst.with_name(f"{dst.stem}-dup{n}" + dst.suffix)
    return cand


def _undo_one(m: dict, keys: tuple[str, ...] = ()) -> dict | None:
    """按 manifest 的一条记录把文件搬回原位：成功返回 None，没落地返回可入账的原因。

    三条 undo 路径共用同一判据，避免各写一套：目标已复现就**只跳过不覆盖**
    （覆盖 = 烧掉一份重新采集回来的在库页）；单条 OSError 不许打断整轮 ——
    undo 抛在半路，剩下的条目永远没人搬。返回前自验「归档位没了 + 原位在了」，
    与 `do_apply` 的搬运自验同口径，没落地就绝不算成功。
    """
    src, dst = ROOT / m["to"], ROOT / m["from"]
    out = {k: m.get(k) for k in keys}
    out.update({"from": m["to"], "to": m["from"]})
    if not src.exists():
        if dst.exists():
            return None                       # 早就搬回过：续跑幂等，不是失败
        out["skipped"] = "src-missing"        # 两头都没有 = 页真丢了
        return out
    if dst.exists():
        out["skipped"] = "dst-exists"
        return out
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.move(str(src), str(dst))
    except OSError as e:                      # 目标复现 / 文件被 Obsidian、AV 占用（WinError 5）
        out["failed"] = str(e)[:60]
        return out
    if src.exists() or not dst.exists():
        out["unverified"] = True
        return out
    return None


def _undo_report(man_file: Path, man: dict, todo: list, bad: list[dict], lock_name: str) -> None:
    """未搬回的清单：终端响亮列出 + 写回 manifest 的 `undo_unverified`。

    只打在终端 = 下一轮无从核对谁还没回来；沿用 `manifest.unverified` 的形状（按族
    固定 lock_name，同 do_apply，免得每份 manifest 都留下一个不回收的 .lock 文件）。
    """
    if not bad:
        if "undo_unverified" in man:        # 本轮全搬回了：清掉上一轮的未搬回，别留假警
            man.pop("undo_unverified")
            write_ledger(man_file, man, lock_name=lock_name, indent=2)
        return
    print(f"[!] 未搬回 {len(bad)}/{len(todo)} 条（源缺失 / 目标已存在 / 移动报错 / 未生效）"
          f"—— 这些仍留在归档区原位，处理后可重跑同一条 undo：", flush=True)
    for b in bad[:10]:
        print(f"     {b['from']} -> {b['to']}  "
              f"{b.get('skipped') or b.get('failed') or 'unverified'}", flush=True)
    man["undo_unverified"] = bad
    write_ledger(man_file, man, lock_name=lock_name, indent=2)


def do_apply(plan: dict[str, list[dict]], seen: Seen) -> Path:
    moves: list[dict] = []
    failed: list[dict] = []
    for ch_id, rows in plan.items():
        for r in rows:
            src = ROOT / r["note"]
            if not src.exists():
                continue
            dst = archive_path(r["note"])
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst = _free_dup_name(dst)              # 罕见：同 id 重复搬过（撞名顺延，绝不覆盖）
            try:
                shutil.move(str(src), str(dst))
            except OSError as e:
                # `_free_dup_name` 只是先验：目标可能在这一步复现，或文件被 Obsidian/AV 占用
                # （WinError 5）。单条搬不动就记一笔继续 —— 整轮抛在这里，已搬成功的部分
                # 连 manifest 都写不出来，等于没有 undo 凭证。
                failed.append({"item_id": r["item_id"], "from": r["note"],
                               "to": dst.relative_to(ROOT).as_posix(), "failed": str(e)[:60]})
                continue
            try:
                stamp_frontmatter(dst, r["reason"])
            except OSError as e:
                print(f"    [!] 归档标记写不进 {dst.name}: {str(e)[:60]}")   # 页已搬动，标记可后补
            rel_new = dst.relative_to(ROOT).as_posix()
            moves.append({"item_id": r["item_id"], "source": ch_id, "reason": r["reason"],
                          "from": r["note"], "to": rel_new})
            # 同步见账簿里的 note 位置，否则下一轮 kb_collect 会以为 note 还在老地方
            if r["item_id"] in seen.items:
                seen.items[r["item_id"]]["note"] = rel_new

    # 搬运自验（硬要求）：move 不是「复制」的语义，源文件必须消失、目标必须落地。
    # 实测 2026-09-21 零点连跑两轮归档，6 moves 里 3 条源文件仍在盘上 →
    # 下一轮重判把同一条**再归档一次**（归档区同条两份），① 计数等式当场破功，
    # 而在此之前每一步都「看起来成功」。搬完不验 = 把债挂到下一轮。
    bad = [m for m in moves
           if (ROOT / m["from"]).exists() or not (ROOT / m["to"]).exists()]
    if bad:
        print(f"[!] 搬运未生效 {len(bad)}/{len(moves)} 条（源文件仍在 或 目标缺失）—— "
              f"不得继续跑下一轮重判，先查原因（多为目标被占用/跨盘 move 退化成复制）：", flush=True)
        for m in bad[:10]:
            print(f"     {m['item_id']} from={m['from']} to={m['to']}", flush=True)
    if failed:
        print(f"[!] 搬不动已跳过 {len(failed)} 条（未进 moves，页仍在 20-语料，下一轮重判再试）：",
              flush=True)
        for f in failed[:10]:
            print(f"     {f['item_id']} from={f['from']} {f['failed']}", flush=True)
    seen.save()
    man = META / f"prune_manifest_{now_cst().strftime('%Y%m%dT%H%M%S')}.json"
    # manifest = undo 的唯一凭证，走 write_ledger（锁 + 原子替换）；lock_name 用族名而非
    # 带时间戳的 path.stem，否则每份 manifest 都在 _meta 留一个永不回收的 .lock 文件。
    write_ledger(man, {"at": iso(now_cst()), "moves": moves,
                       "unverified": [m["item_id"] for m in bad],
                       "failed": failed}, lock_name="prune_manifest", indent=2)
    rotate_files(META, "prune_manifest_", 12)               # 工作区只留近 12 份（git 历史兜底）
    return man


def _iid_of_note(p: Path) -> str:
    """取 note 的 item_id：先看 frontmatter，回退文件名前缀 `<iid>_slug.md`。"""
    try:
        for ln in p.read_text(encoding="utf-8").splitlines()[:40]:
            m = re.match(r"^item_id:\s*(.+?)\s*$", ln)
            if m:
                return m.group(1).strip().strip('"')
    except OSError:
        pass
    return p.name.split("_", 1)[0]


def dedupe_archive(apply: bool, seen: Seen) -> int:
    """归档区「同条目多份快照」去重：只留账本指向的那份，其余移进 `80-归档/重复副本/<ts>/`。

    为什么会有多份：冻结区靠 `-dup/-dup2` 顺延撞名（见 `_free_dup_name`），而同一条目
    跨天被重判归档两次时又会落进不同日期桶（2026-09-21 实测：一条 4 份）。
    后果不是「占空间」这么轻 —— 归档区被 Obsidian 全文索引，同一条重复 N 次会让
    「归档了什么」的检索结果不可信，且 `80-归档/posts` 计数永远对不上账本（127 vs 117）。

    保留规则（优先级从高到低）：
      1. `seen.note` 指向的那份 —— 它是「当前认账的那份」，动它会让账本与磁盘脱节；
      2. 都没有则留 mtime 最新的那份（最后一次写入的快照最新）。
    其余**只移不移删**（搬进重复副本目录，manifest 可 undo）—— 冻结区不做不可逆删除。
    幂等：跑完第二遍应为 0。
    """
    groups: dict[str, list[Path]] = {}
    for p in (ROOT / "80-归档" / "posts").rglob("*.md"):
        groups.setdefault(_iid_of_note(p), []).append(p)
    # 实体归档区（80-归档/项目、人物、方法论）也要去重：`_free_dup_name` 每撞一次名就顺延
    # 一份 `-dupN`，而 `--archive-entities` 是**每轮**跑的（同一条 stale 页可能被再次搬），
    # 于是冻结区同条会攒出 -dup3/-dup4……（2026-09-21 实测 32 份）。
    # 语料区靠 item_id 认条，实体区没有 item_id，按「去掉 -dupN 后的 stem」分组。
    for sub in ("项目", "人物", "方法论"):
        d = ROOT / "80-归档" / sub
        if not d.is_dir():
            continue
        for p in d.glob("*.md"):
            groups.setdefault(_entity_stem_of(p) + "::" + sub, []).append(p)
    dup = {i: ps for i, ps in groups.items() if len(ps) > 1}
    if not dup:
        print("归档区无同条目重复快照")
        return 0
    print(f"归档区同条目多份：{len(dup)} 组 / 共 {sum(len(v) for v in dup.values())} 份")

    keep, move = [], []
    for iid, ps in sorted(dup.items()):
        want = str((seen.items.get(iid) or {}).get("note") or "")
        keeper = next((p for p in ps if p.relative_to(ROOT).as_posix() == want), None)
        if keeper is None:
            # 实体区：无账本可依 → 留「未顺延名」的那份（`-dupN` 是后来才挂上去的副本）
            keeper = next((p for p in ps if not re.search(r"-dup\d*$", p.stem)), None)
        if keeper is None:
            keeper = max(ps, key=lambda p: p.stat().st_mtime)
        keep.append(keeper)
        move += [p for p in ps if p is not keeper]
    for p in sorted(dup):
        pass
    print(f"  保留 {len(keep)} 份 · 待移出 {len(move)} 份")
    if not apply:
        for p in move[:10]:
            print(f"    {p.relative_to(ROOT).as_posix()}")
        print("  （只报告；加 --apply 才搬运）")
        return len(move)

    ts = now_cst().strftime("%Y%m%dT%H%M%S")
    moves, failed = [], []
    for p in move:
        rel = p.relative_to(ROOT).as_posix()
        dst = ROOT / "80-归档" / "重复副本" / ts / rel[len("80-归档/"):]
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst = _free_dup_name(dst)
        try:
            shutil.move(str(p), str(dst))
        except OSError as e:
            # 同 do_apply：单条搬不动（目标复现 / 文件被占用）记一笔继续，
            # 不许抛出去 —— 那样前面已搬走的份就没人记账了。
            failed.append({"from": rel, "to": dst.relative_to(ROOT).as_posix(),
                           "failed": str(e)[:60]})
            continue
        moves.append({"from": rel, "to": dst.relative_to(ROOT).as_posix()})
    man = META / f"archive_dedupe_manifest_{ts}.json"
    write_ledger(man, {"at": iso(now_cst()), "moves": moves, "failed": failed},
                 lock_name="archive_dedupe_manifest", indent=2)
    rotate_files(META, "archive_dedupe_manifest_", 12)
    if failed:
        print(f"  [!] 搬不动已跳过 {len(failed)} 份（仍在归档区原位，下次 --dedupe-archive 再试）：",
              flush=True)
        for f in failed[:10]:
            print(f"     {f['from']} {f['failed']}", flush=True)
    print(f"  已移出 {len(moves)} 份 → {man.relative_to(ROOT).as_posix()}"
          f"（回滚：python tools/kb_prune.py --undo-dedupe {man.relative_to(ROOT).as_posix()}）")
    return len(moves)


def undo_dedupe(man_path: str) -> int:
    """把「重复副本」按 manifest 搬回原位（单条失败不中断，见 `_undo_one`）。"""
    man_file = Path(man_path)
    man = json.loads(man_file.read_text(encoding="utf-8"))
    todo = man.get("moves") or []
    bad, n = [], 0
    for m in todo:
        r = _undo_one(m)
        if r:
            bad.append(r)
            continue
        n += 1
    _undo_report(man_file, man, todo, bad, lock_name="archive_dedupe_manifest")
    return n


def prune_empty_dirs(apply: bool) -> int:
    """清掉 `20-语料/posts/<渠道>/<日期>/` 里的空桶壳。

    渠道整体被归档/停用后，语料搬空但目录壳留在原处 —— 它不进任何计数，
    但会让「这个渠道还在采」的错觉成立（目录树里看得见），并让 glob 扫盘白跑一遍。
    """
    # 由内向外反复扫：删掉日期桶后渠道目录自己也会变空（一轮扫不干净，实测第二遍还剩 4 个）
    empty: list[Path] = []
    while True:
        batch = [p for p in (ROOT / "20-语料" / "posts").rglob("*")
                 if p.is_dir() and not any(p.iterdir())]
        if not batch:
            break
        empty += batch
        if not apply:
            break
        removed = 0
        for p in batch:
            try:
                p.rmdir()
                removed += 1
            except OSError as e:
                print(f"    [!] 删不掉 {p.relative_to(ROOT).as_posix()}: {str(e)[:60]}")
        if removed == 0:                       # 全删不动 → 停，避免死循环
            break
    if not empty:
        print("20-语料 无空目录")
        return 0
    print(f"20-语料 空目录 {len(empty)} 个：")
    for p in empty:
        print(f"    {p.relative_to(ROOT).as_posix()}")
    if not apply:
        print("  （只报告；加 --apply 才删除）")
        return len(empty)
    n = 0
    for p in empty:
        try:
            p.rmdir()
            n += 1
        except OSError as e:
            print(f"    [!] 删不掉 {p.relative_to(ROOT).as_posix()}: {str(e)[:60]}")
    print(f"  已删除 {n} 个空目录")
    return n


def do_undo(man_path: str, seen: Seen) -> int:
    """按 manifest 把语料搬回 20-语料。账本只在**确认落地**后才改（判据见 `_undo_one`）。"""
    man_file = Path(man_path)
    man = json.loads(man_file.read_text(encoding="utf-8"))
    todo = man.get("moves") or []
    bad, n = [], 0
    for m in todo:
        r = _undo_one(m, keys=("item_id",))
        if r:
            bad.append(r)
            continue
        if m["item_id"] in seen.items:
            seen.items[m["item_id"]]["note"] = m["from"]
        n += 1
    seen.save()
    _undo_report(man_file, man, todo, bad, lock_name="prune_manifest")
    return n


# ------------------------------------------------------------------ 实体页存活标记

NAV_ENTITY_RE = re.compile(r"^- (?:项目页|人物页)：\[\[([^\]|#]+)", re.M)
ENTITY_DIRS = ("10-项目", "30-人物")
ENTITY_ARCHIVE = {"10-项目": DIR_ARCHIVE / "项目", "30-人物": DIR_ARCHIVE / "人物"}
# 目录说明页 / 索引页不是实体，无论 stale 与否都不搬
# 名字兜底 + `_is_meta_note` 的 type 判断（index/home）双保险：改名后的说明页靠 type 拦住
ENTITY_SKIP = {"README.md", "index.md", "索引.md"}


def _live_stems() -> set[str]:
    """在库实体页名集合 —— **导航段 ∪ 规范名重算** 双来源。

    来源①（导航段）：直接读在库语料页「## 导航」里的实体链接。它本来就是采集端按同一
    规则生成的，天然同源，覆盖绝大多数条目。

    来源②（规范名重算）：按 `project_note_path / person_note_path` 对在库条目重算一遍，
    判据与 `kb_healthcheck.py` 的 ② 完全一致。

    为什么必须加来源②（2026-09-21 实测级联伤）：
      `kb_reclassify --merge-orphans` 合并孤儿页时**只删旧页、不改写链接**，语料导航段
      于是仍指向旧名。而来源①信任那串链接 → 旧名被当「在库」、真正的规范页被判 stale
      → `--archive-entities` 把**活页**搬进归档 → healthcheck ② 缺页 4 + ④ 断链 4。
    取并集只会让判据更保守（少搬），不会误搬 —— 与「宁可留页不断链」同向。
    """
    out: set[str] = set()
    for p in DIR_CORPUS.rglob("*.md"):
        m = NAV_ENTITY_RE.search(p.read_text(encoding="utf-8"))
        if m:
            out.add(m.group(1).split("/")[-1])

    # 来源②：规范名重算（依赖 seen.note 判「在库」）
    try:
        seen = Seen()
        for it in load_items().values():
            iid = it.get("item_id")
            if not iid:
                continue
            note = (seen.get(iid) or {}).get("note") or ""
            if not note.startswith(CORPUS_PREFIX):
                continue                          # 已归档 / 未落库 → 不算在库
            try:
                if it.get("kind") == "person":
                    out.add(person_note_path(it).stem)
                elif is_project_ish(it):
                    out.add(project_note_path(it).stem)
            except Exception:                     # noqa: BLE001
                continue
    except Exception as e:                        # noqa: BLE001
        print(f"[!] _live_stems 规范名重算失败（退回纯导航段口径）：{e!r}", flush=True)
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
                        # 整页重写一律原子替换：实体页是聚合成果，被截断就是丢一整页
                        _atomic_write(p, txt[:end] + f'\nstale: true' + txt[end:])
                stale.append(p.stem)
            elif not want and has:
                if apply:
                    _atomic_write(p, re.sub(r"^stale:\s*true\s*\n", "", txt, count=1, flags=re.M))
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
            _atomic_write(p, txt)            # 冻结区整页重写也要原子：半截页不可复原
            n += 1
    return n


def archive_entities_apply(info: dict) -> Path:
    pairs: dict[str, str] = {}
    moves: list[dict] = []
    failed: list[dict] = []
    for folder, rows in info["plan"].items():
        dst_dir = ENTITY_ARCHIVE[folder]
        dst_dir.mkdir(parents=True, exist_ok=True)
        for r in rows:
            src, dst = ROOT / r["note"], ROOT / r["to"]
            if not src.exists():
                continue
            dst = _free_dup_name(dst)
            try:
                shutil.move(str(src), str(dst))
            except OSError as e:
                # 同 do_apply：归档位复现 / 页面被占用时记一笔继续。抛出去会让前面
                # 真搬走的实体页没有 manifest —— 想撤时既没凭证也认不出哪些是本次搬的。
                failed.append({"stem": r["stem"], "from": r["note"],
                               "to": dst.relative_to(ROOT).as_posix(), "failed": str(e)[:60]})
                continue
            to_rel = dst.relative_to(ROOT).as_posix()
            pairs[r["note"][:-3]] = to_rel[:-3]        # wikilink 文本不带 .md
            moves.append({"stem": r["stem"], "from": r["note"], "to": to_rel})
    n_files = _rewrite_links(pairs)
    # 同 do_apply：搬完必须自验。实体页被搬走后 `10-项目/` 里的旧路径若还在，
    # 下一轮 liveness 会把它再判一遍、再搬一次 → 归档区同页两份 + 检索面没清干净。
    bad = [m for m in moves
           if (ROOT / m["from"]).exists() or not (ROOT / m["to"]).exists()]
    if bad:
        print(f"[!] 实体页搬运未生效 {len(bad)}/{len(moves)} 个（源文件仍在 或 目标缺失）—— "
              f"先查原因再跑下一轮：", flush=True)
        for m in bad[:10]:
            print(f"     {m['stem']} from={m['from']} to={m['to']}", flush=True)
    if failed:
        print(f"[!] 实体页搬不动已跳过 {len(failed)} 个（未进 moves，页仍在检索面，下次再试）：",
              flush=True)
        for f in failed[:10]:
            print(f"     {f['stem']} from={f['from']} {f['failed']}", flush=True)
    man = META / f"entity_archive_manifest_{now_cst().strftime('%Y%m%dT%H%M%S')}.json"
    write_ledger(man, {"at": iso(now_cst()), "moves": moves, "rewritten_notes": n_files,
                       "unverified": [m["stem"] for m in bad], "failed": failed},
                 lock_name="entity_archive_manifest", indent=2)
    rotate_files(META, "entity_archive_manifest_", 12)      # 同上（kb_moc 聚合近 12 份的理由）
    return man


def undo_entities(man_path: str) -> int:
    """把实体页按 manifest 搬回 10-项目/30-人物，链接同步改回（判据见 `_undo_one`）。"""
    man_file = Path(man_path)
    man = json.loads(man_file.read_text(encoding="utf-8"))
    todo = man.get("moves") or []
    pairs = {}
    bad, n = [], 0
    for m in todo:
        r = _undo_one(m, keys=("stem",))
        if r:
            bad.append(r)
            continue                          # 没落地就不改 pairs —— 否则链接指向空路径
        pairs[m["to"][:-3]] = m["from"][:-3]
        n += 1
    _rewrite_links(pairs)
    _undo_report(man_file, man, todo, bad, lock_name="entity_archive_manifest")
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
    ap.add_argument("--dedupe-archive", action="store_true",
                    help="归档区同条目多份快照去重（只留账本指向的那份，其余移进 80-归档/重复副本/）")
    ap.add_argument("--undo-dedupe", default="", help="按 manifest 把重复副本搬回原位")
    ap.add_argument("--prune-empty-dirs", action="store_true",
                    help="清掉 20-语料/posts 下的空日期桶目录")
    ap.add_argument("--out", default="")
    args = ap.parse_args(argv)

    seen = Seen()
    if args.undo_dedupe:
        n = undo_dedupe(args.undo_dedupe)
        print(f"已按 {args.undo_dedupe} 搬回 {n} 份重复副本")
        return 0

    if args.dedupe_archive or args.prune_empty_dirs:
        a = dedupe_archive(args.apply, seen) if args.dedupe_archive else 0
        b = prune_empty_dirs(args.apply) if args.prune_empty_dirs else 0
        print(f"完成：去重 {a} 份 · 清空目录 {b} 个")
        return 0

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
