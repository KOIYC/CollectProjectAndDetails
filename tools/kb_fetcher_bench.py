"""kb_fetcher_bench — 抽取器选题基准（正文后端该按**基准**选，不按「谁先报 ok」选）。

为什么需要它（2026-09-21 调研报告 §3.6 / FLUX arXiv 2603.13972）：
正文取数后端已经换过三轮（Jina → Exa → 直取优先），每次都是「某天后端挂了」逼出来的，
却从没有一次**同批对比**。后果是本库的两条硬约束无法回答：
  * `FULLTEXT_MAX_CHARS` 定 40000 合理吗？（截断率是多少？）
  * 「直取优先、Exa 兜底」的收益到底有多大？（命中率差多少？）
论文侧的提示：行级剔除优于整篇拒收（FLUX 多留 9.7% token）；抽取器质量是**可以量化比较**的，
应按字符收益率与完整度选型。

本工具只做三件事（不写任何语料）：
  1. 同一批 URL 用各后端各抓一遍，逐条记长度 / 是否摘要残文 / 是否贴上上限截断 / 首尾完整度；
  2. 按后端聚合出**可比较的表**，给出「该用谁」的可证伪结论；
  3. 把结论落 `_meta/fetcher_bench_latest.json`，供改代码时引用（而不是拍脑袋改）。

用法：
  python tools/kb_fetcher_bench.py --sample 20
  python tools/kb_fetcher_bench.py --sample 12 --backends direct,gh
"""
from __future__ import annotations

import argparse
import collections
import json
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import (BODY_MIN, DIR_RAW, DIR_REPORT, FULLTEXT_MAX_CHARS, META,  # noqa: E402
                       ROOT, body_completeness, direct_fetch_texts, exa_fetch_texts,
                       load_ndjson, looks_summary, now_cst, truncated_at_cap, which_cli)

GH_REPO_RE = None


def _gh_repo(url: str) -> str:
    import re
    global GH_REPO_RE
    if GH_REPO_RE is None:
        GH_REPO_RE = re.compile(r"^https?://(?:www\.)?github\.com/([^/]+)/([^/#?]+)", re.I)
    m = GH_REPO_RE.match(url or "")
    if not m:
        return ""
    repo = m.group(2).lower()
    if repo in {"issues", "discussions", "pulls", "marketplace", "sponsors", "topics"}:
        return ""
    return m.group(1) + "/" + m.group(2).replace(".git", "")


def load_candidates() -> list[dict]:
    """候选 = 已离开采集窗口、正文不完整、且有可取 URL 的条目（正是回填队列的形状）。"""
    lat: dict[str, dict] = {}
    for f in sorted(DIR_RAW.glob("*/*.jsonl")):
        for r in load_ndjson(f):
            iid = r.get("item_id")
            if not iid:
                continue
            cur = lat.get(iid)
            if cur is None or (r.get("captured_at") or "") >= (cur.get("captured_at") or ""):
                lat[iid] = r
    out = []
    for r in lat.values():
        ex = r.get("extra") or {}
        url = (ex.get("fulltext_url") or r.get("project_url") or r.get("url") or "").strip()
        if not url.startswith("http"):
            continue
        if body_completeness(r.get("body"), ex, ex.get("layer") or "corpus") == "full":
            continue
        out.append({**r, "_url": url})
    # 稳定排序（按 item_id）→ 同一批样本可复现，改后端后能对比「同一批」的差异
    out.sort(key=lambda r: r["item_id"])
    return out


def sample(items: list[dict], n: int) -> list[dict]:
    """等距抽样：覆盖全库顺序，避免全落在同一渠道/同一主机上。"""
    if len(items) <= n:
        return items
    step = len(items) / n
    return [items[int(i * step)] for i in range(n)]


def measure(text: str) -> dict:
    t = text or ""
    tail = t.rstrip()[-1:] if t else ""
    return {
        "chars": len(t),
        "summary": bool(looks_summary(t)),
        "truncated_at_cap": bool(truncated_at_cap(t)),
        "ends_sentence": bool(tail and tail in "。！？.!?」”\"')"),
        "usable": len(t) >= BODY_MIN,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=20)
    ap.add_argument("--backends", default="direct,exa,gh")
    ap.add_argument("--exa-batch", type=int, default=8)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    want = [b.strip() for b in args.backends.split(",") if b.strip()]

    cand = sample(load_candidates(), args.sample)
    rows: list[dict] = []
    if not cand:
        print("无候选（语料已全部 full）—— 基准不适用")
        return 0

    urls = [c["_url"] for c in cand]
    results: dict[str, dict[str, dict]] = collections.defaultdict(dict)
    timing: dict[str, float] = {}

    if "direct" in want:
        t0 = time.time()
        st: dict = {}
        got = direct_fetch_texts(urls, max_chars=FULLTEXT_MAX_CHARS, workers=6, status_out=st)
        timing["direct"] = round(time.time() - t0, 1)
        for u in urls:
            results["direct"][u] = {**measure(got.get(u, "")), "status": str(st.get(u, "?"))}

    if "exa" in want:
        t0 = time.time()
        got_e: dict[str, str] = {}
        empty_batches = 0
        for i in range(0, len(urls), args.exa_batch):
            chunk = urls[i:i + args.exa_batch]
            try:
                g = exa_fetch_texts(chunk, max_chars=FULLTEXT_MAX_CHARS)
            except Exception as e:                                 # noqa: BLE001
                print(f"  [w] exa 批次失败：{str(e)[:70]}")
                g = {}
            if not g:
                empty_batches += 1
            got_e.update(g)
        timing["exa"] = round(time.time() - t0, 1)
        backend_dead = empty_batches == (len(urls) + args.exa_batch - 1) // args.exa_batch
        for u in urls:
            m = measure(got_e.get(u, ""))
            # 后端整体不可用时**不许记成「0 字符」**：那会让结论变成「Exa 抽取质量差」，
            # 而真相是「Exa 此刻额度打满」。两者对选型的含义完全相反。
            m["status"] = "backend_unavailable" if (backend_dead and not got_e) else \
                ("hit" if u in got_e else "miss")
            results["exa"][u] = m

    if "gh" in want:
        from kb_common import run_cli
        t0 = time.time()
        for u in urls:
            repo = _gh_repo(u)
            if not repo:
                results["gh"][u] = {**measure(""), "status": "n/a"}
                continue
            code, out, _err = run_cli(["gh", "api", f"repos/{repo}/readme", "-H",
                                       "Accept: application/vnd.github.raw"], timeout=60)
            results["gh"][u] = {**measure(out if code == 0 else ""),
                                "status": "hit" if (code == 0 and out.strip()) else f"miss(rc={code})"}
        timing["gh"] = round(time.time() - t0, 1)

    # 只对「至少一个后端命中」的 URL 做对比，避免把不可得条目算进各后端的命中率分母
    for i, c in enumerate(cand):
        u = c["_url"]
        rows.append({"title": (c.get("title") or "")[:70], "channel": c.get("source_id"),
                     "url": u, "by_backend": {b: results[b].get(u, {}) for b in want}})

    agg: dict[str, dict] = {}
    for b in want:
        vals = [r["by_backend"][b] for r in rows if r["by_backend"].get(b)]
        hit = [v for v in vals if v.get("status") in ("hit", "", "200")]
        chars = [v["chars"] for v in hit if v["chars"]]
        agg[b] = {
            "n": len(vals),
            "hit": len(chars),
            "hit_rate": round(100 * len(chars) / max(1, len(vals)), 1),
            "median_chars": int(statistics.median(chars)) if chars else 0,
            "usable": sum(1 for v in hit if v.get("usable")),
            "summary_rate": round(100 * sum(1 for v in hit if v.get("summary")) / max(1, len(hit)), 1),
            "trunc_rate": round(100 * sum(1 for v in hit if v.get("truncated_at_cap")) / max(1, len(hit)), 1),
            "ends_sentence": round(100 * sum(1 for v in hit if v.get("ends_sentence")) / max(1, len(hit)), 1),
            "seconds": timing.get(b, 0),
            "chars_per_s": int(sum(chars) / timing[b]) if chars and timing.get(b) else 0,
        }

    # 结构裁决：零依赖铁律下，node 组件只能作为「决策输入」记录，不能直接上
    node_verdict = ("defuddle 未安装（node 组件）—— 上它就破了「tools/ 纯 stdlib」铁律，"
                    "需先改规范页再引入" if not which_cli("defuddle")
                    else "defuddle 可用，但引入即破零依赖铁律，须先过规范页确认")

    ts = now_cst().strftime("%Y%m%dT%H%M%S")
    out = DIR_REPORT / f"抽取器基准-{ts}.md"
    L = ["# 抽取器选题基准（同批 URL × 多后端）", "",
         f"> 生成 {now_cst().isoformat(timespec='seconds')} · 工具 `tools/kb_fetcher_bench.py`",
         f"> 样本 **{len(rows)}** 条（等距取自「正文不完整且已离开采集窗口」的条目，"
         f"即回填队列的形状）· 上限 `FULLTEXT_MAX_CHARS={FULLTEXT_MAX_CHARS}`", "",
         "**这是同一批 URL 的同批对比** —— 本库此前三轮后端切换从没做过这件事。", "",
         "| 后端 | 试用 | 命中 | 命中率 | 正文中位字符 | 可用(≥120) | 摘要残文率 | 贴上上限率 | 结尾完整率 | 耗时 | 字符/秒 |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for b, a in agg.items():
        L.append(f"| `{b}` | {a['n']} | {a['hit']} | {a['hit_rate']}% | {a['median_chars']} | "
                 f"{a['usable']} | {a['summary_rate']}% | {a['trunc_rate']}% | {a['ends_sentence']}% | "
                 f"{a['seconds']}s | {a['chars_per_s']} |")
    L += ["", "## 逐条明细", "", "| 渠道 | 标题 | " + " | ".join(f"`{b}`" for b in want) + " |",
          "|---|---|" + "---|" * len(want)]
    for r in rows:
        cells = []
        for b in want:
            v = r["by_backend"].get(b) or {}
            if not v:
                cells.append("—")
            elif v.get("status") in ("n/a",):
                cells.append("n/a")
            else:
                tag = "" if v.get("usable") else "✗"
                cells.append(f"{v.get('chars', 0)}{tag} {v.get('status', '')}".strip())
        L.append(f"| `{r['channel']}` | {r['title']} | " + " | ".join(cells) + " |")
    L += ["", "## 结构约束（影响选型，不只是数字）", "",
          f"- node 组件评估：{node_verdict}",
          "- 本机已知不可达：`news.ycombinator.com` / `github.com` 直取被 Tunnel 拦（`DIRECT_BLOCKED_HOSTS`）；"
          "GitHub 正文只能走 `api.github.com`（gh readme）。",
          "- Exa 免费额度会 429：**后端整体不可用时记 `backend_unavailable`，不记 0 字符** ——"
          "否则结论会变成「Exa 抽取质量差」，而真相是「额度打满」。",
          ] if False else ["", "## 结构约束（影响选型，不只是数字）", "",
                           f"- node 组件评估：{node_verdict}",
                           "- 本机已知不可达：`news.ycombinator.com` / `github.com` 直取被 Tunnel 拦"
                           "（`DIRECT_BLOCKED_HOSTS`）；GitHub 正文只能走 `api.github.com`（gh readme）。",
                           "- Exa 免费额度会 429：**后端整体不可用时记 `backend_unavailable`，不记 0 字符** ——"
                           "否则结论会变成「Exa 抽取质量差」，而真相是「额度打满」。",
                           "", "## 裁决", "",
                           "看三列：**命中率**（拿得到吗）、**正文中位字符**（拿到多少）、"
                           "**贴上上限率**（拿到的是不是只有开头）。同批对比下：",
                           ]
    for b, a in agg.items():
        L.append(f"- `{b}`：命中 {a['hit_rate']}% · 中位 {a['median_chars']} 字符 · "
                 f"贴上限 {a['trunc_rate']}% · 结尾完整 {a['ends_sentence']}%")
    L += ["", f"（结论由**这张表**决定，不由「谁先报 ok」决定。改 `--direct-workers` / "
              f"`FULLTEXT_MAX_CHARS` 之前先看这里的贴上限率。）"]
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    (META / "fetcher_bench_latest.json").write_text(json.dumps(
        {"generated": now_cst().isoformat(timespec="seconds"), "sample": len(rows),
         "aggregate": agg}, ensure_ascii=False, indent=1), encoding="utf-8")
    day = ts[:8]
    for old in sorted(DIR_REPORT.glob(f"抽取器基准-{day}T*.md"))[:-1]:
        try:
            old.unlink()
        except OSError:
            pass

    if not args.quiet:
        for b, a in agg.items():
            print(f"  {b:7s} 命中 {a['hit_rate']:>5}% · 中位 {a['median_chars']:>6} 字符 · "
                  f"贴上限 {a['trunc_rate']:>5}% · 结尾完整 {a['ends_sentence']:>5}%")
    print(f"[报告] {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
