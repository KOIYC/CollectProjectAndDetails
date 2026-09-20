"""kb_reclassify — 存量实体错分订正（人物被当成项目）。

背景：1c7 名录里混着「独立开发大牛」条目（`Patrick McKenzie (@patio11)`、`https://x.com/levelsio`）。
R3 之前 ad_onec7 一律 kind="project"，于是这些人被写进 `10-项目/`，污染项目集。
R3 起采集端已按 `PERSON_HANDLE_RE / ACCOUNT_URL_RE` 分流，但**存量记录**不会自动搬家。

本工具做订正（幂等）：
  1) 扫 latest-by-item，找出「URL/标题像人，但 kind != person」的记录
  2) 追加一条 record_type=reclassify 的订正记录（kind=person）
  3) 在 `30-人物/` 建人物页
  4) 删除对应的旧 `10-项目/` 页面（**仅限 hash 完全对应该 URL 的生成物**），并把删除清单打印出来

用法：
  python tools/kb_reclassify.py --dry     # 只列清单
  python tools/kb_reclassify.py           # 执行
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import DIR_RAW, META, ROOT, Seen, append_jsonl, iso, now_cst, rotate_runs, sha1  # noqa: E402
from kb_collect import (ACCOUNT_URL_RE, PERSON_HANDLE_RE, corpus_note_path,  # noqa: E402
                        method_note_path, person_note_path, project_note_path,
                        write_corpus_note, write_entity_note, write_person_note,
                        write_project_note)
from kb_common import norm_url  # noqa: E402


def load_latest() -> dict[str, tuple[dict, str]]:
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


def looks_like_person(r: dict) -> str | None:
    if r.get("kind") == "person":
        return None
    title = r.get("title") or ""
    url = r.get("project_url") or r.get("url") or ""
    if PERSON_HANDLE_RE.search(title):
        return "标题含 @handle"
    if ACCOUNT_URL_RE.search(url) or ACCOUNT_URL_RE.search(r.get("url") or ""):
        return "URL 为社交账号页"
    return None


def merge_orphans(dry: bool = False) -> int:
    """合并孤儿项目页。

    成因：`project_url` 靠正文外链回退推导，某轮正文取不到 → 退化为 None → 项目页文件名的
    hash 变化 → 新建一页、上一轮那页成了孤儿（实测 20 条，全是 V2EX/Reddit，正文是外链帖）。
    采集端已改为「project_url 只增不减」防新增；本函数清理存量：
      孤儿页的 project_url == 该条目的 item url → 找到当前 live 页 → 合并「观测历史」行 → 删孤儿页。
    """
    live = load_latest()
    by_item_url: dict[str, tuple[dict, str]] = {}
    for iid, (r, day) in live.items():
        by_item_url[norm_url(r.get("url") or "")] = (r, day)

    proj = Path("10-项目")
    orphans, merged = [], 0
    for f in sorted(proj.glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        m = re.search(r"^project_url:\s*(.+)$", txt[:800], re.M)
        if not m:
            continue
        key = norm_url(m.group(1).strip().strip('"'))
        pair = by_item_url.get(key)
        if not pair:
            continue                                  # 不是「以 item url 为 key 的孤儿页」
        r, _day = pair
        if r.get("kind") == "person":
            continue
        target = project_note_path(r)
        if target.resolve() == f.resolve():
            continue                                  # 已是当前页
        orphans.append((f, target, r))

    if not orphans:
        print("无孤儿项目页")
        return 0
    print(f"发现 {len(orphans)} 个孤儿项目页（URL 与当前页不同源，观测历史需合并）：")
    for f, t, r in orphans:
        print(f"  - 孤儿 {f.name[:56]} → 当前 {t.name[:56]}")
    if dry:
        return len(orphans)

    for f, target, r in orphans:
        rows = []
        if target.exists():
            mm = re.search(r"## 观测历史\n\n(.*?)(\n## |\Z)", target.read_text(encoding="utf-8"), re.S)
            if mm:
                rows = [ln for ln in mm.group(1).strip().splitlines() if ln.startswith("|")][2:]
        mo = re.search(r"## 观测历史\n\n(.*?)(\n## |\Z)", f.read_text(encoding="utf-8"), re.S)
        orows = [ln for ln in (mo.group(1).strip().splitlines() if mo else []) if ln.startswith("|")][2:]
        have = {ln.split("|")[1].strip() for ln in rows}
        added = [ln for ln in orows if ln.split("|")[1].strip() not in have]
        p = write_project_note(r, None, extra_obs=added)      # 正规写页：观测历史一次写对，不做字符串拼接
        if added:
            print(f"  合并 {len(added)} 行历史 → {p.name}")
        f.unlink()
        print(f"  删除孤儿 {f.name}")
        merged += 1
    return merged


def repair_frontmatter(dry: bool = False) -> int:
    """自愈：修复被字符串拼接打乱 frontmatter 的项目页（重建而非打补丁）。"""
    live = load_latest()
    by_url: dict[str, dict] = {}
    for _iid, (r, _day) in live.items():
        by_url[norm_url(r.get("project_url") or r.get("url") or "")] = r

    bad, fixed = [], 0
    for f in sorted(Path("10-项目").glob("*.md")):
        txt = f.read_text(encoding="utf-8")
        ok = txt.startswith("---\n") and re.match(r"^[a-z_]+:", txt[4:].split("\n", 1)[0] or "")
        if ok:
            continue
        m = re.search(r"^project_url:\s*(.+)$", txt, re.M)
        if not m:
            continue
        key = norm_url(m.group(1).strip().strip('"'))
        r = by_url.get(key)
        if not r:
            continue
        rows = [ln for ln in txt.splitlines() if ln.startswith("| ") and ln.count("|") >= 4]
        bad.append((f, r, rows))

    if not bad:
        print("无需修复")
        return 0
    print(f"发现 {len(bad)} 个 frontmatter 损坏页：")
    for f, r, rows in bad:
        print(f"  - {f.name[:60]}（可回收 {len(rows)} 行观测）")
    if dry:
        return len(bad)
    for f, r, rows in bad:
        p = write_project_note(r, None, extra_obs=rows)
        print(f"  重建 {p.name}（并入 {len(rows)} 行观测）")
        fixed += 1
    return fixed


def repair_project_url(dry: bool = False) -> int:
    """存量补推 project_url。

    为什么存量要单独补：`derive_project_url` 只在**采集时**跑。开规则之前入库的条目，
    project_url 是在「正文还没取到」的构造期算的 —— 发布站类渠道（producthunt/
    indiehackers/betalist）实测 100% 为空。而 project_url 是「同一项目跨渠道归并」的键，
    缺它则洞察层的跨渠道强信号恒为 0。
    本函数不重取网络数据，只用**已经补全的正文**重推一次（正文由 kb_backfill 负责）。
    """
    from kb_collect import derive_project_url, is_project_ish, project_url_reject
    from kb_content_audit import archived_ids, disabled_channels
    off, archived = disabled_channels(), archived_ids()
    items = load_latest()
    seen0 = Seen()

    def note_state(iid):
        """(note相对路径, note 里是否已有 project_url)"""
        note = (seen0.get(iid) or {}).get("note") or ""
        if not note or not note.startswith("20-语料/"):
            return note, False
        p = ROOT / note
        if not p.exists():
            return note, False
        try:
            head = p.read_text(encoding="utf-8")[:800]
        except OSError:
            return note, False
        return note, bool(re.search(r"^project_url:\s*\S", head, re.M))

    skipped = sum(1 for iid, (r, _d) in items.items()
                  if r.get("source_id") in off or iid in archived)
    todo = []
    for iid, (r, day) in items.items():
        if r.get("source_id") in off or iid in archived:
            continue
        # 没正文就推不出链接（derive 靠正文里的外链）——但**错值**无论有没有正文都要清掉：
        # 留着它会让两个不同项目一直共用一个项目页（实测 bilibili/youtube 自身链接被当项目站）。
        bad_now = bool(r.get("project_url")) and bool(project_url_reject(r.get("project_url")))
        if not (r.get("body") or "") and not bad_now:
            continue
        note, has_pu = note_state(iid)
        # 两个来源都要看：raw 有记录 / note 有 frontmatter。
        # 只判 raw 会漏掉「上一轮已把 project_url 写进 raw、但写 note 时失败」的条目 ——
        # 那种条目在 raw 里看着已修好，实际 note 里仍是空的（实测 168 条卡在这里）。
        if not note or not (ROOT / note).exists():
            continue
        # 三种情况要处理：① raw 与 note 都缺（补推）；② note 缺但 raw 有（补写页面）；
        # ③ **已有值但不合法**（错值必须订正，否则两个不同项目会一直共用一个项目页）。
        bad_cur = bool(r.get("project_url")) and bool(project_url_reject(r.get("project_url")))
        if has_pu and r.get("project_url") and not bad_cur:
            continue
        todo.append((iid, r, day, note, has_pu))
    todo.sort(key=lambda t: -len(t[1].get("body") or ""))
    print(f"待补推/订正 {len(todo)} 条（已跳过停用渠道/已归档 {skipped} 条）"
          f"，按正文长度降序，先补信息量大的")
    if dry:
        for _iid, r, _d, _n, _h in todo[:15]:
            cur = r.get("project_url") or ""
            if cur and project_url_reject(cur):
                print(f"  [{r['source_id']}] (错值订正) {cur[:50]} → "
                      f"{derive_project_url(r.get('url') or '', r.get('body') or '') or '(置空)'}")
            else:
                got = cur or derive_project_url(r.get("url") or "", r.get("body") or "")
                print(f"  [{r['source_id']}] {(r.get('title') or '')[:44]} → {got}")
        return len(todo)

    seen = Seen()
    day_now = now_cst().strftime("%Y-%m-%d")
    run_id = "project-url-" + now_cst().strftime("%Y%m%d-%H%M%S")
    n = 0
    for iid, r, day, note, has_pu in todo:
        cur = (r.get("project_url") or "").strip()
        bad = project_url_reject(cur) if cur else ""
        # 错值必须**先清掉再重推**：`cur or derive(...)` 会把错值原样留下来 ——
        # 这正是 `liqi.io/creators:` 一路活到洞察报告里的原因。
        got = derive_project_url(r.get("url") or "", r.get("body") or "") if bad else (
            cur or derive_project_url(r.get("url") or "", r.get("body") or ""))
        if got and project_url_reject(got):
            got = None
        if not got and not bad:
            continue
        rec = dict(r)
        rec["extra"] = dict(rec.get("extra") or {})
        if got:
            rec["project_url"] = norm_url(got)
            rec["extra"]["project_url_derived"] = "post_hoc"
            rec["extra"].pop("project_url_rejected", None)
        else:
            # 推不出合法值 → 置空（页面按自身 url 命名，属设计内回退），并留下拒绝原因
            rec["project_url"] = None
            rec["extra"]["project_url_rejected"] = f"{bad}｜{cur[:80]}"
        rec["captured_at"] = iso(now_cst())
        rec["record_type"] = "repair"
        rec["run_id"] = run_id
        # 分片日期必须取**原 note 的日期**，否则 write_corpus_note 会在今天的目录下
        # 再写一份同 id 的语料页 —— 正文原地刷新就变成了复制（实测踩过）。
        shard = day
        m = re.match(r"20-语料/posts/[^/]+/(\d{4}-\d{2}-\d{2})/", note)
        if m:
            shard = m.group(1)
        try:
            append_jsonl(DIR_RAW / r["source_id"] / f"{day_now}.jsonl", [rec])
            if shard:
                p = write_corpus_note(rec, shard)
                if iid in seen.items:
                    seen.items[iid]["note"] = p.relative_to(ROOT).as_posix()
            seen.items.setdefault(iid, {})["project_url"] = rec["project_url"]
            # 实体页准入与 kb_collect 同一判据：不是项目的条目（讨论帖）不建项目页，
            # 否则置空 project_url 的讨论帖会被写成一个「项目页」。
            if is_project_ish(rec) or rec.get("kind") in ("person", "method"):
                write_entity_note(rec, note)
            n += 1
        except Exception as e:                                     # noqa: BLE001
            print(f"  [w] {iid} 失败：{str(e)[:70]}")
    seen.save()
    (META / "runs" / f"{run_id}.json").write_text(json.dumps(
        {"run_id": run_id, "kind": "repair_project_url", "count": n,
         "started": iso(now_cst())}, ensure_ascii=False, indent=1), encoding="utf-8")
    rotate_runs()                                              # 运行记录轮转（保 80 份）
    print(f"补推完成：{n}/{len(todo)}")
    return n


def reconcile_entities(dry: bool = False) -> int:
    """按当前 kind 分发规则，为存量 person / method 语料补建实体页。

    为什么需要：`kb_collect` 只在**内容变化**时（`it['_changed']`）才重写语料页与实体页。
    当 kind 判据、nav_block 结构、实体页 writer 更新时（例如本次加 40-方法论/ 之前，
    kind=method 会被误当 project 建页），存量页面不会自动跟上 —— 需要显式回放一次。

    本函数不重写语料，只按 seen.json 里已知的 note 路径反推 corpus_rel，
    再调 write_entity_note 落 30-人物/ 或 40-方法论/。幂等：多次跑只覆盖同一目标。

    命名规范变更后（例如 method 页 hash 加了 `#method` 盐），旧写法生成的实体会成为孤儿 ——
    本函数会先算「当前应有的实体页 stem 集合」，把不在这个集合里、且其 frontmatter
    `type` 与目录匹配（type=method 在 40-方法论/，type=person 在 30-人物/）的旧文件删掉。
    只删**自己派生**的东西（`type` 对得上目录），绝不动人工创作内容。
    """
    from kb_common import DIR_METHOD, DIR_PEOPLE
    seen = Seen()
    latest = load_latest()
    want_stems: dict[str, set[str]] = {
        "person": {person_note_path(rec).stem for iid, (rec, _d) in latest.items()
                   if (rec.get("kind") or "").lower() == "person"},
        "method": {method_note_path(rec).stem for iid, (rec, _d) in latest.items()
                   if (rec.get("kind") or "").lower() == "method"},
    }
    n_cleaned = 0
    for kind, dir_ in (("person", DIR_PEOPLE), ("method", DIR_METHOD)):
        for p in dir_.glob("*.md"):
            if p.stem in want_stems[kind]:
                continue
            if p.stem.endswith("说明"):
                continue
            # 只删本函数辖区内的派生页 —— 判据：frontmatter 里 `type: "kind"` 与目录匹配。
            fm_head = p.read_text(encoding="utf-8")[:400]
            expected = f'type: "{kind}"'
            if expected not in fm_head:
                continue
            if not dry:
                p.unlink()
                n_cleaned += 1
    n_written = 0
    by_kind: dict[str, int] = {}
    for iid, (rec, day) in latest.items():
        kind = (rec.get("kind") or "").lower()
        if kind not in ("person", "method"):
            continue
        note = (seen.items.get(iid) or {}).get("note")
        # seen 里没记 note → 用当前 slug 规则重算（防历史条目 seen 缺账）
        if not note:
            p = corpus_note_path(rec, day).relative_to(ROOT).as_posix()
            note = p
        if not (ROOT / note).exists():
            continue
        if dry:
            by_kind[kind] = by_kind.get(kind, 0) + 1
            continue
        write_entity_note(rec, note)
        by_kind[kind] = by_kind.get(kind, 0) + 1
        n_written += 1
    label = "（dry-run）" if dry else ""
    extra = f"  清孤儿={n_cleaned}" if n_cleaned else ""
    print(f"实体页对齐{label}：写入 {by_kind or '无'}{extra}")
    return n_written


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--merge-orphans", action="store_true", help="只做孤儿项目页合并")
    ap.add_argument("--repair", action="store_true", help="只做 frontmatter 损坏自愈")
    ap.add_argument("--project-url", action="store_true",
                    help="存量补推 project_url（正文已补全的条目可推出项目外链）")
    ap.add_argument("--reconcile-entities", action="store_true",
                    help="按当前 kind 分发规则，为存量 person/method 语料补建实体页"
                         "（不重写语料，只落 30-人物/ 与 40-方法论/）")
    args = ap.parse_args(argv)

    if args.reconcile_entities:
        reconcile_entities(args.dry)
        return 0
    if args.repair:
        repair_frontmatter(args.dry)
        return 0
    if args.merge_orphans:
        merge_orphans(args.dry)
        return 0
    if args.project_url:
        repair_project_url(args.dry)
        return 0

    cands = []
    for iid, (r, day) in load_latest().items():
        why = looks_like_person(r)
        if why:
            cands.append((r, day, why))
    if not cands:
        print("无错分实体")
        return 0

    print(f"发现 {len(cands)} 条错分（人物被写入 10-项目/）：")
    for r, day, why in cands:
        print(f"  - [{r['source_id']}] {r.get('title', '')[:50]} | {why} | {r.get('url', '')[:70]}")
    if args.dry:
        return 0

    seen = Seen()
    day_now = now_cst().strftime("%Y-%m-%d")
    run_id = "reclassify-" + now_cst().strftime("%Y%m%d-%H%M%S")
    moved = 0
    for r, day, why in cands:
        rec = dict(r)
        rec["kind"] = "person"
        rec["project_url"] = None
        m = PERSON_HANDLE_RE.search(r.get("title") or "")
        m2 = ACCOUNT_URL_RE.search(r.get("url") or "")
        rec["author"] = rec.get("author") or (m.group(1) if m else (m2.group(1) if m2 else None))
        rec["author_url"] = rec.get("author_url") or r.get("url")
        rec["captured_at"] = iso(now_cst())
        rec["record_type"] = "reclassify"
        rec["run_id"] = run_id
        rec.setdefault("extra", {})["reclassified"] = f"project→person（{why}）"

        old = project_note_path(r)                                  # 错误落的项目页
        append_jsonl(DIR_RAW / r["source_id"] / f"{day_now}.jsonl", [rec])
        p = write_person_note(rec, None)
        rel = p.relative_to(ROOT).as_posix()
        seen.touch(r["item_id"], r["source_id"], rel, None,
                   content_hash=sha1(json.dumps({"b": rec.get("body") or "", "c": rec.get("comments") or [],
                                                 "m": rec.get("metrics") or {}}, ensure_ascii=False,
                                                sort_keys=True)))
        if old.exists() and old.resolve() != p.resolve():
            old.unlink()                                            # 仅删该 URL 的生成物，raw 数据不受影响
            print(f"  删除旧项目页 {old.name} → 新建人物页 {p.name}")
        else:
            print(f"  新建人物页 {p.name}（无同名项目页）")
        moved += 1
    seen.save()
    (META / "runs" / f"{run_id}.json").write_text(json.dumps(
        {"run_id": run_id, "kind": "reclassify", "count": moved,
         "items": [{"item_id": r["item_id"], "title": r.get("title"), "why": w}
                   for r, _, w in cands], "started": iso(now_cst())},
        ensure_ascii=False, indent=1), encoding="utf-8")
    rotate_runs()                                              # 运行记录轮转（保 80 份）
    print(f"订正完成：{moved} 条 → 30-人物/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
