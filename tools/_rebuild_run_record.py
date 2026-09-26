"""一次性修复脚本：重建因 kb_collect 收尾 NameError 而缺失的采集 run 记录。

背景（2026-09-26）：kb_collect.py 收尾写 rename manifest 时 `write_ledger` 未导入 → NameError，
`log.finish()` 未执行 → `_meta/runs/20260926T094106.json` 缺失、`latest.json` 停留在此前的体检轮。
本脚本**只读 90-原始（不可变事实源）**按 run_id 汇总，重放 RunLog 的落盘格式，不改任何语料。

用法：python tools/_rebuild_run_record.py --run 20260926T094106 [--write]
默认 dry（只打印），--write 才落盘。
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from kb_common import DIR_RAW, RUNS, ensure_dirs, iso, now_cst, rotate_runs  # noqa: E402
from kb_common import _atomic_write  # noqa: E402


def collect_rows(day: str) -> dict[str, list[dict]]:
    by_ch: dict[str, list[dict]] = {}
    for f in sorted(DIR_RAW.glob(f"*/{day}.jsonl")):
        ch = f.parent.name
        for ln in f.read_text(encoding="utf-8").split("\n"):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except json.JSONDecodeError:
                continue
            by_ch.setdefault(ch, []).append(r)
    return by_ch


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--day", default="")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    day = args.day or f"{args.run[0:4]}-{args.run[4:6]}-{args.run[6:8]}"
    by_ch = collect_rows(day)

    chans: list[dict] = []
    total = new_tot = upd_tot = ref_tot = 0
    for ch, rows_all in by_ch.items():
        rows = [r for r in rows_all if r.get("run_id") == args.run]
        if not rows:
            continue
        c = Counter(r.get("record_type") for r in rows)
        n, u, rf = c.get("new", 0), c.get("update", 0), c.get("refresh", 0)
        total += len(rows)
        new_tot += n
        upd_tot += u
        ref_tot += rf
        chans.append({"source_id": ch, "status": "ok", "count": len(rows),
                      "message": f"重建自 raw · new={n} chg={u} ref={rf}",
                      "new": n, "changed": u, "refresh": rf})

    payload = OrderedDict()
    payload["run_id"] = args.run
    payload["started_at"] = iso(now_cst())
    payload["ended_at"] = iso(now_cst())
    payload["elapsed_s"] = None
    payload["channels"] = chans
    payload["notes_written"] = None
    payload["errors"] = ["重建记录：kb_collect 收尾 write_ledger NameError 致 log.finish() 未执行"
                         "（已修 import）；本记录由 tools/_rebuild_run_record.py 从 90-原始 按 run_id 重放"]
    payload["reconstructed"] = True
    payload["total_items"] = total
    payload["total_new"] = new_tot
    payload["total_update"] = upd_tot
    payload["total_refresh"] = ref_tot

    print(f"day={day} run={args.run} channels={len(chans)} total={total} "
          f"new={new_tot} update={upd_tot} refresh={ref_tot}")
    for c in chans:
        print(f"  {c['source_id']:16s} {c['count']:>4}  new={c['new']:>3} chg={c['changed']:>3} ref={c['refresh']:>3}")
    if not args.write:
        print("(dry-run，未落盘；加 --write 生效)")
        return 0
    ensure_dirs()
    out = RUNS / f"{args.run}.json"
    _atomic_write(out, json.dumps(payload, ensure_ascii=False, indent=1))
    _atomic_write(RUNS / "latest.json", json.dumps(payload, ensure_ascii=False, indent=1))
    try:
        rotate_runs()
    except OSError:
        pass
    print(f"已写 {out.relative_to(ROOT).as_posix()} + latest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
