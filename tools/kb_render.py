"""kb_render.py —— 存量语料/实体页重渲染（可读性模板升级的迁移工具）。

背景：语料页/实体页模板升级（元数据折叠 callout + 一句话导读 + 正文 HTML 清理 +
评论引用块）后，存量 700+ 页仍是旧模板。本工具从 `90-原始/` 的**最新记录**出发，
复用 kb_collect 的渲染函数重写这些页 —— raw 是唯一事实源，重放即迁移。

纪律：
- 只重写 `seen.json` 登记过的在库页（不新建、不搬家 —— 路径按 seen.note 原位重写，
  避免 manifest/seen/链接三件套失配）；
- 观测历史表原样保留（只动模板层，不动账本层）—— 项目页/人物页/方法论页读旧页
  的观测历史再写回，与 kb_collect 增量写法一致；
- 幂等：重跑两遍输出应一致；
- 结束必跑 kb_healthcheck（语料计数不平 = 漏写/多写）。
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import kb_analyze as KA                      # noqa: E402
import kb_collect as C                       # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true", help="只统计要写哪些页，不落盘")
    ap.add_argument("--limit", type=int, default=0, help="最多重写 N 页（0=不限）")
    args = ap.parse_args(argv)

    seen_items = C.Seen().items
    rows = KA.load_records()
    latest = KA.latest_by_item(rows)
    corpus_day = {iid: r.get("captured_at", "")[:10] for iid, r in latest.items()}

    # 观测历史从 **raw 全量记录**重建：渲染模式不 touch_obs，但项目页的观测历史是
    # 「项目页→语料页」的入链来源，一行都不能少。归组键用**最新记录**推出的实体页
    # （条目改判后历史行随之迁到新页 —— 自愈 reclassify 漂移）；行内语料链接用
    # seen.note（当前页路径）。去重按 (采集时间, 渠道) 保留最后一条（同刻重跑覆盖）。
    from collections import defaultdict
    ent_of_item: dict[str, str | None] = {}
    for iid, r in latest.items():
        kind = (r.get("kind") or "").lower()
        try:
            if kind == "person":
                ep = C.person_note_path(r)
            elif kind == "method":
                ep = C.method_note_path(r)
            else:
                ep = C.project_note_path(r)
        except Exception:                              # noqa: BLE001
            ep = None
        ent_of_item[iid] = ep.name if ep else None
    obs_by_entity: dict[str, dict[tuple[str, str], str]] = defaultdict(dict)
    for r in rows:
        iid = r.get("item_id") or ""
        meta = seen_items.get(iid)
        ep_name = ent_of_item.get(iid)
        if not meta or not ep_name:
            continue
        note_rel = (meta.get("note") or "").strip()
        key = (iid, r.get("captured_at") or "", r.get("source_name") or "")
        obs_by_entity[ep_name][key] = (
            f"| {r.get('captured_at')} | {r.get('source_name')} | "
            f"{C.metrics_line(r.get('metrics') or {})} "
            f"| {('[[{}]]'.format(note_rel[:-3]) if note_rel else '—')} |")
    obs_override_by_entity: dict[str, list[str]] = {
        k: sorted(v.values(), key=lambda ln: ln.split("|")[1].strip())[-60:]
        for k, v in obs_by_entity.items()
    }

    todo = []
    for iid, meta in seen_items.items():
        note = (meta.get("note") or "").strip()
        r = latest.get(iid)
        if not note or not r:
            continue                          # 旧页丢失/条目不在库 → 交给 prune，不在此建新页
        p = ROOT / note
        if not p.exists():
            continue
        if not note.startswith("20-语料/"):
            continue                          # 只重渲染语料页（实体页由语料页带动重写）
        # 分片日期必须取 **note 自己所在的桶**，不能用 `captured_at[:10]`：
        # 跨零点采集时两者不同（note 落 09-20、captured_at 是 09-21）→ 按 captured_at
        # 重算会得到新路径，本工具于是「新建」一份页，旧页原地不动 = 磁盘上同条两份，
        # ① 计数当场破功（2026-09-21 实测 52 份）。纪律是原位重写，绝不新建。
        todo.append((iid, r, note, note.split("/")[-2] if re.match(r"^\d{4}-\d{2}-\d{2}$", note.split("/")[-2])
                     else (corpus_day.get(iid) or "")))
    todo.sort(key=lambda t: t[2])
    print(f"语料页待渲染：{len(todo)}" + ("（dry）" if args.dry else ""))
    if args.dry:
        for iid, _, note, _ in todo[:10]:
            print("  e.g.", note[:80])
        return 0

    t0 = time.time()
    done = skipped = 0
    entity_cache = {}                          # 项目页可能被多条语料命中 → 逐条写（观测历史去重靠函数内部）
    written_entities: set[Path] = set()
    for i, (iid, r, note, day) in enumerate(todo, 1):
        it = dict(r)
        it.setdefault("item_id", iid)
        # 渲染函数期望 kind 等字段与采集时一致；raw 最新记录即该条目的完整字段
        try:
            # 先算路径再写：算出来和账本不一致就**一个字节都不写**（旧的写法先写了再
            # 判漂移，等于在库里留一份副本，然后把锅甩给「待 navfix」）。
            want = C.corpus_note_path(it, day).relative_to(ROOT).as_posix()
            if want != note:
                print(f"  [!] 路径漂移：{note} -> {want}（未写盘，先跑 kb_navfix --fix-names）")
                skipped += 1
                continue
            p = C.write_corpus_note(it, day)
            rel = p.relative_to(ROOT).as_posix()
            if C.is_project_ish(it) or (it.get("kind") or "").lower() in ("person", "method"):
                ep = C.write_entity_note(it, rel, touch_obs=False,
                                         obs_override=obs_override_by_entity.get(ent_of_item.get(iid)))
                written_entities.add(ep)
            done += 1
        except Exception as e:                 # noqa: BLE001
            skipped += 1
            print(f"  [x] {iid[:10]} {note[-50:]}: {type(e).__name__}: {str(e)[:80]}")
        if args.limit and done >= args.limit:
            break
        if i % 100 == 0:
            print(f"  ... {i}/{len(todo)}（{time.time() - t0:.0f}s）", flush=True)
    print(f"完成：语料页 {done} 重写 · 实体页 {len(written_entities)} 重写 · "
          f"{skipped} 跳过/失败 · {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
