"""kb_near_dup — 近重复检测（在线标注 + 离线报告），纯 stdlib。

**为什么需要**：本库只有 `content_hash`（对 body+comments+metrics 的 sha1）做**精确**去重。
跨渠道同一项目的改写稿（同一篇复盘发在 reddit 与 v2ex、同一发布稿被 HN 与 IndieHackers 各转一次）
哈希完全不同 → 各存一份。后果不是「多占空间」，而是**分析层被系统性高估**：
「跨渠道独立观测数」本该是强信号，改写稿会让同一个信号重复计数。
论文侧同向（FOLD / SemDeHash：面向**持续演化**数据集需要在线模糊去重；CuraWeb 主张质量/冗余/多样性联合优化）。

## 判定口径（两段式：候选 → 验证）

**第一版只做「候选」就出报告，实测是错的**，留档以免重犯：
用**字符 4-gram + 逐 shingle 累加**时，任何两条同域长文本（同是 GitHub README、同是 HN 帖）
都会被判成近重复 —— 实测 8 个**不同项目**的指纹汉明距离 Δ0~1、而真实 4-gram 包含度只有 0.15~0.27。
两个独立的机制叠加造成：
1. **重复 shingle 被反复投票**：模板行（`- Stars: N`、`## Languages`、`---`）在正文里出现几百次，
   同样的 4-gram 就投几百票，把真正区分内容的部分淹掉 → 不同项目的指纹撞成同一个。
2. **字符 4-gram 的公共基线太强**：英文/中文标记文本里最常见的 4-gram 集合高度重叠，
   它们构成一个两两共享的固定向量，同域文本的 simhash 天然互相靠近。

所以现在改为：
* **特征 = 词级 3-shingle（去重后）**：ASCII 取 `[a-z0-9]` 起头的词，CJK 逐字成 token，
  每 3 个连续 token 一个特征。**先去重再投票**（每条特征一票）—— 断掉机制 1。
  词级比字符级稀疏得多，公共基线弱得多 —— 缓解机制 2。
* **simhash64 只当「候选生成器」**：Δ≤6 只说明「值得查」，不说明「是重复」。
* **命中候选必须过验证**：对候选对算**精确特征集包含度** `|A∩B| / min(|A|,|B|) ≥ 0.60`。
  这是唯一被写进报告的判据；Δ 只作为辅助列展示。

保留一条可证伪的判据：**阈值 0.60 是按「改写稿会保留 >60% 的原特征、而同域不同文只共享 ~25%」定的**，
报告里每对都打印实际包含度，阈值定错一眼能看出来（而不是只给一个「15 组」的黑箱数）。

其他取舍：
  * **只取正文前 3000 字符**：改写稿的差异通常在中后段（追加/删减），前段足以判同源；
    这一步让全库构建从分钟级降到秒级。
  * **只标注、不合并、不删除**：证据库的纪律是「保留了才能复核」。发现近重复只写
    `extra.near_dup_of` 与报告，人工裁决后走 `kb_prune` 归档（带 undo 清单）。
  * 太短的正文（< 200 字符）不建指纹 —— 特征空间太窄，会互相误判成重复。

用法：
  python tools/kb_near_dup.py                # 全库报告（不写 seen）
  python tools/kb_near_dup.py --build        # 把指纹写入 _meta/seen.json（供采集端在线标注）
  python tools/kb_near_dup.py --check <item_id>   # 单条查重（调试/排障用）
  python tools/kb_near_dup.py --selftest     # 判据自检（真改写必须命中、同域异文必须不命中）
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import (DIR_RAW, DIR_REPORT, META, ROOT, Seen, iso, load_ndjson,  # noqa: E402
                       now_cst)

MIN_TEXT = 200        # 归一化后低于此长度不建指纹（见文件头「取舍」）
SHINGLE = 3           # 词级 3-shingle
TEXT_CAP = 3000       # 只取前 3000 字符：改写稿差异多在中后段，前段足以判同源
MAX_HAMMING = 6       # simhash 候选门：64 位差 ≤6 位才进验证
MIN_CONTAINMENT = 0.60  # 验证门：特征集包含度低于此不算近重复（见文件头「可证伪的判据」）

_URL_RE = re.compile(r"https?://\S+")
_WS_RE = re.compile(r"[\s\u3000]+")
# 一个 token = 一个 ASCII 词，或一个 CJK 字（CJK 无空格，逐字成 token 后 3-shingle 即三元组）
_TOK_RE = re.compile(r"[a-z0-9][a-z0-9_+\-.#']*|[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

# ---- simhash 的向量化累加（纯 stdlib，别按位循环）
#
# 朴素写法是「每条特征 × 64 个 bit 逐个累加」——3000 字符 ≈ 数百条特征 × 64 = 上万次
# Python 级操作/条，全库 1700 条要跑几分钟，不能接受。
# 这里换成**打包累加**：把 64 个计数器塞进一个 64×16bit 的大整数里，每个字节查表得到
# 「该字节的 8 个 bit 里哪些要 +1」的打包值，一条特征只做 8 次查表 + 移位相加。
# 语义与朴素写法完全等价（计数器 16 位，单条最大特征数 < 65535，不会溢出）。
_W = 16
_MASK = (1 << _W) - 1
_LUT_POS = [sum((1 << (i * _W)) for i in range(8) if (b >> i) & 1) for b in range(256)]


def normalize(text: str) -> str:
    t = (text or "").lower()
    t = _URL_RE.sub(" ", t)                      # 链接差异不算内容差异
    return _WS_RE.sub(" ", t)


def features(text: str) -> frozenset[str]:
    """词级 3-shingle 特征集（**去重**）。文本太短则退化为 token 集本身。"""
    toks = _TOK_RE.findall(normalize(text)[:TEXT_CAP])
    if len(toks) < SHINGLE:
        return frozenset(toks)
    return frozenset(" ".join(toks[i:i + SHINGLE]) for i in range(len(toks) - SHINGLE + 1))


def containment(a: frozenset[str], b: frozenset[str]) -> float:
    """包含度 = |A∩B| / min(|A|,|B|)。用 min 而非并集：改写稿常大幅增删，
    Jaccard 会被长度差拉低，而「短的那篇几乎被长的那篇覆盖」正是要抓的情形。"""
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def simhash64(text: str) -> str:
    """64 位 simhash（hex 16 字符）；文本太短返回空串。

    bit b = 1 ⇔ 「bit b 为 1 的特征数 > 一半」。等价于按位投票，但只累加正计数
    （负计数会让打包字段借位），用 `2*ones > N` 的判据绕开。
    """
    feats = features(text)
    if len(normalize(text)) < MIN_TEXT or not feats:
        return ""
    acc = 0
    for f in feats:
        h = int.from_bytes(hashlib.blake2b(f.encode("utf-8"), digest_size=8).digest(), "big")
        for i in range(8):
            acc += _LUT_POS[(h >> (i * 8)) & 0xFF] << (i * 8 * _W)
    n = len(feats)
    out = 0
    for b in range(64):
        if 2 * ((acc >> (b * _W)) & _MASK) > n:
            out |= (1 << b)
    return f"{out:016x}"


def hamming(a: str, b: str) -> int:
    if not a or not b:
        return 99
    return (int(a, 16) ^ int(b, 16)).bit_count()


def near_dups_in(index: dict, text: str, exclude: str = "", limit: int = 3,
                 max_hamming: int = MAX_HAMMING, body_of=None,
                 min_containment: float = MIN_CONTAINMENT) -> list[dict]:
    """找近重复（供采集端**在线**标注用）。返回已过验证的命中，按包含度降序。

    索引形状 = `Seen.items`：`{item_id: {"simhash": "..", "source": "..", "note": ".."}}`。
    拿不到指纹的历史条目自动跳过 —— 所以要先跑过一遍 `--build`（或等在线增量攒起来）。

    `body_of(iid) -> str|None` 由调用方注入（通常是 BodyCache）：给了才对候选做**包含度验证**。
    **没给时只返回候选且 `verified=False`** —— 不假装验证过（静默降级是明令禁止的）。
    """
    if not text:
        return []
    sh = simhash64(text)
    if not sh:
        return []
    mine = features(text)
    out = []
    for iid, rec in index.items():
        if iid == exclude:
            continue
        other = rec.get("simhash")
        if not other:
            continue
        d = hamming(sh, other)
        if d > max_hamming:
            continue
        rec_out = {"item_id": iid, "hamming": d, "source": rec.get("source") or "",
                   "note": rec.get("note") or "", "containment": None, "verified": False}
        if body_of is not None:
            obody = body_of(iid)
            if obody:
                rec_out["containment"] = round(containment(mine, features(obody)), 3)
                rec_out["verified"] = rec_out["containment"] >= min_containment
        out.append(rec_out)
    out.sort(key=lambda x: (-(x["containment"] if x["containment"] is not None else -1), x["hamming"]))
    return out[:limit]


def load_items() -> dict[str, dict]:
    lat: dict[str, dict] = {}
    for f in sorted(DIR_RAW.glob("*/*.jsonl")):
        for r in load_ndjson(f):
            iid = r.get("item_id")
            if not iid:
                continue
            cur = lat.get(iid)
            if cur is None or (r.get("captured_at") or "") >= (cur.get("captured_at") or ""):
                lat[iid] = r
    return lat


def build_groups(items: dict[str, dict]) -> tuple[dict[str, str], dict[str, frozenset], list[list[str]], list[dict]]:
    """算指纹 + 特征集 → 候选（Δ≤6）→ **包含度验证** → 并查集分组。

    返回 (item_id → 指纹, item_id → 特征集, 组列表, 被否掉的候选对)。
    被否掉的候选对要回传：报告里写出来，「Δ 撞了但包含度不够」正是 A/B 两段的证据。
    """
    sh: dict[str, str] = {}
    fs: dict[str, frozenset] = {}
    for iid, r in items.items():
        s = simhash64(r.get("body") or "")
        if s:
            sh[iid] = s
            fs[iid] = features(r.get("body") or "")
    ids = list(sh)
    parent = {i: i for i in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    rejected: list[dict] = []
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            if hamming(sh[a], sh[b]) > MAX_HAMMING:
                continue
            cont = containment(fs[a], fs[b])
            if cont < MIN_CONTAINMENT:
                rejected.append({"a": a, "b": b, "hamming": hamming(sh[a], sh[b]),
                                 "containment": round(cont, 3)})
                continue
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
    groups: dict[str, list[str]] = collections.defaultdict(list)
    for i in ids:
        groups[find(i)].append(i)
    rejected.sort(key=lambda x: -x["hamming"])
    return sh, fs, [g for g in groups.values() if len(g) > 1], rejected


def render(items: dict[str, dict], sh: dict, fs: dict, groups: list[list[str]],
           rejected: list[dict]) -> str:
    def ch(iid):
        return (items.get(iid) or {}).get("source_id") or "?"

    # 只读一次账本：`Seen()` 每次实例化都会解析整个 seen.json（MB 级），
    # 放在下面的双层循环里 = 每个条目重读一遍文件，纯浪费。
    seen = Seen()
    multi = [g for g in groups if len({ch(i) for i in g}) > 1]
    all_fs = [fs[i] for i in fs]
    L = ["# 近重复（simhash 候选 → 特征包含度验证）", "",
         f"> 生成 {iso(now_cst())} · 工具 `tools/kb_near_dup.py`",
         f"> 指纹 {len(sh)}/{len(items)} 条（正文 < {MIN_TEXT} 字符不建指纹）· "
         f"候选门：64 位汉明距离 ≤ {MAX_HAMMING} · 验证门：特征包含度 ≥ {MIN_CONTAINMENT} · "
         f"特征：词级 {SHINGLE}-shingle（去重）· 文本上限 {TEXT_CAP} 字符", "",
         f"- 近重复组 **{len(groups)}** 组，其中**跨渠道 {len(multi)}** 组",
         f"- 候选被否 **{len(rejected)}** 对（指纹撞了但包含度不足 = 同域不同文，**不是重复**）", "",
         "**为什么关心跨渠道组**：同一条内容被两个渠道各收一次，会让「跨渠道独立观测」"
         "这个强信号被重复计数（同一信号算两次）。组内其余情况（同渠道同源转载）优先级低。", "",
         "**为什么要有「验证门」**：指纹相近不等于内容重复。第一版只靠指纹，"
         "把 8 个毫不相关的 GitHub 项目判成一组（模板行反复投票 + 字符 4-gram 公共基线）。"
         "现在每对都必须过精确包含度 —— 报告里逐对给数，阈值定错一眼能看出来。", ""]
    if all_fs:
        import statistics
        base = [containment(all_fs[i], all_fs[j])
                for i in range(len(all_fs)) for j in range(i + 1, len(all_fs))]
        if base:
            L += [f"**全库包含度基线**（用于校准阈值）：中位 {statistics.median(base):.3f} · "
                  f"P99 {sorted(base)[int(len(base) * 0.99)]:.3f} · 最大 {max(base):.3f} "
                  f"（{len(base)} 对）", ""]
    L += ["## 跨渠道组（优先复核）", ""]
    if not multi:
        L.append("- 无")
    for i, g in enumerate(sorted(multi, key=lambda g: -len(g))[:40], 1):
        L += [f"### 组 {i}（{len(g)} 条 · {len({ch(x) for x in g})} 个渠道）", ""]
        for iid in sorted(g, key=lambda x: ch(x)):
            r = items.get(iid) or {}
            # 组内最小包含度（= 这一组有多紧），逐条打印 Δ 与基线包含度
            conts = [round(containment(fs[iid], fs[o]), 3) for o in g if o != iid]
            L.append(f"- [{ch(iid)}] {(r.get('title') or '')[:70]} · `{iid}`")
            L.append(f"    - 指纹 `{sh.get(iid, '')}` · 组内包含度 "
                     f"{min(conts) if conts else '—'}~{max(conts) if conts else '—'} · "
                     f"语料 `{(seen.get(iid) or {}).get('note') or '—'}`")
    L += ["", "## 同渠道组（摘要）", ""]
    same = [g for g in groups if len({ch(i) for i in g}) == 1]
    for g in sorted(same, key=lambda g: -len(g))[:20]:
        L.append(f"- `{ch(g[0])}` × {len(g)}：{ ' / '.join((items.get(i) or {}).get('title', '')[:40] for i in g[:4]) }")
    L += ["", "## 候选被否明细（前 20 对：Δ 小但包含度不足）", ""]
    if not rejected:
        L.append("- 无")
    for r in rejected[:20]:
        ta = (items.get(r["a"]) or {}).get("title") or ""
        tb = (items.get(r["b"]) or {}).get("title") or ""
        L.append(f"- Δ{r['hamming']} 包含度 {r['containment']} · [{ch(r['a'])}] {ta[:45]} × "
                 f"[{ch(r['b'])}] {tb[:45]}")
    L += ["", "## 下一步（人工裁决，工具不代劳）", "", "```",
          "python tools/kb_near_dup.py --build        # 把指纹写进 seen.json，采集端开始在线标注",
          "python tools/kb_near_dup.py --check <item_id>   # 单条查重",
          "python tools/kb_near_dup.py --selftest     # 判据自检",
          "```",
          "裁决后若要合并/归档重复条目 → 走 `kb_prune.py`（带 undo 清单），**不要手删语料**。"]
    return "\n".join(L) + "\n"


def selftest() -> int:
    """判据自检：真改写必须命中、同域异文必须不命中、无关文本必须不命中。"""
    cases: list[tuple[str, str, bool]] = []
    base = ("We shipped our SaaS billing dashboard last week. MRR is 4,200 dollars and churn "
            "dropped to 2.1 percent after we moved to annual plans. Here is what we learned "
            "about pricing pages, onboarding emails and cancel flows. ") * 6
    cases.append((base, base + "UPDATE: we raised prices by 20 percent and churn stayed flat. " * 3, True))
    cases.append((base, base.replace("billing dashboard", "billing console")
                  .replace("4,200 dollars", "4200 USD"), True))
    other = ("Kubernetes operator for SurrealDB clusters. Stars 4, forks 0, license MIT, "
             "default branch master, languages C sharp and Just. " ) * 6
    cases.append((base, other, False))
    zh_a = "我们做的是一个独立开发者的订阅制记账工具，月费九美元，主要面向自由职业者和小团队。" * 8
    zh_b = "我们做的是一个独立开发者的订阅制记账工具，月费十九美元，主要面向自由职业者和小团队。" * 8
    cases.append((zh_a, zh_b, True))
    zh_c = "最近在折腾 Kubernetes 集群，把 SurrealDB 用 C# 写的 operator 部署起来，顺手记一下踩坑。" * 8
    cases.append((zh_a, zh_c, False))

    bad = 0
    for i, (a, b, want) in enumerate(cases, 1):
        cont = containment(features(a), features(b))
        got = cont >= MIN_CONTAINMENT
        mark = "OK " if got == want else "FAIL"
        if got != want:
            bad += 1
        print(f"  [{mark}] 例{i} 期望{'命中' if want else '不命中'} · "
              f"实际包含度 {cont:.3f} → {'命中' if got else '不命中'}")
    print(f"自检：{len(cases) - bad}/{len(cases)} 通过（阈值 {MIN_CONTAINMENT}）")
    return 1 if bad else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true", help="把指纹写入 _meta/seen.json")
    ap.add_argument("--check", default="", help="查单个 item_id 的近重复")
    ap.add_argument("--selftest", action="store_true", help="判据自检")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    items = load_items()
    if args.check:
        iid = args.check
        r = items.get(iid)
        if not r:
            print(f"item_id 不在库：{iid}")
            return 1
        body = r.get("body") or ""
        print(f"{iid} 指纹 {simhash64(body) or '（正文过短，未建指纹）'} · 特征 {len(features(body))} 条")
        hits = near_dups_in(Seen().items, body, exclude=iid, limit=10,
                            body_of=lambda x: (items.get(x) or {}).get("body"))
        print(f"近重复 {sum(1 for h in hits if h['verified'])} 条已验证 / {len(hits)} 条候选")
        for h in hits:
            print(f"  Δ{h['hamming']} 包含度 {h['containment']} "
                  f"{'✓' if h['verified'] else '✗(未过验证门)'} "
                  f"[{h['source']}] {(items.get(h['item_id']) or {}).get('title', '')[:60]}")
        return 0

    sh, fs, groups, rejected = build_groups(items)
    if args.build:
        seen = Seen()
        n = 0
        for iid, s in sh.items():
            rec = seen.items.get(iid)
            if rec is None:
                continue
            if rec.get("simhash") != s:
                rec["simhash"] = s
                n += 1
        seen.save()
        print(f"指纹已写入 seen.json：更新 {n} 条 / 共 {len(sh)} 条有指纹")
    ts = now_cst().strftime("%Y%m%dT%H%M%S")
    out = DIR_REPORT / f"近重复-{ts}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(items, sh, fs, groups, rejected), encoding="utf-8")
    (META / "near_dup_latest.json").write_text(json.dumps(
        {"generated": iso(now_cst()), "fingerprinted": len(sh), "items": len(items),
         "groups": len(groups), "candidates_rejected": len(rejected),
         "min_containment": MIN_CONTAINMENT, "max_hamming": MAX_HAMMING,
         "cross_channel_groups": [[{"item_id": i, "source": (items.get(i) or {}).get("source_id")}
                                   for i in g]
                                  for g in groups if len({(items.get(i) or {}).get("source_id") for i in g}) > 1][:50]},
        ensure_ascii=False, indent=1), encoding="utf-8")
    day = ts[:8]
    for old in sorted(DIR_REPORT.glob(f"近重复-{day}T*.md"))[:-1]:
        try:
            old.unlink()
        except OSError:
            pass
    if not args.quiet:
        multi = sum(1 for g in groups if len({(items.get(i) or {}).get('source_id') for i in g}) > 1)
        print(f"近重复：{len(groups)} 组（跨渠道 {multi}）· 候选被否 {len(rejected)} 对 · "
              f"指纹 {len(sh)}/{len(items)}")
    print(f"[报告] {out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
