"""临时脚本：去重 _meta/channels.yaml 里重复的渠道条目。

背景：2026-09-22/09-23 的某次写入把 `channels:` 段整段重复追加了 2-4 次
（21 个 id、54 个 block）。后果不是「无害冗余」：
  * kb_audit 逐条探活 → 39 次探针（应为 18），单轮体检从 ~4min 涨到 11min；
  * 重复副本字段不齐 —— c1c7 的两个副本没有 `params.readme` → 探针报
    `ERR: unknown url type: 'None'`，被记成 error（是假 error，真条目在第三个副本里）；
  * 单一事实源文件带漂移副本 → 改一处不改另一处，注册表迟早自相矛盾。

策略：按 id 归并（保首次出现顺序）。
  base = 字段最多的那个 block（保留其注释），其余副本里 base 缺的键按序追加。
  `note_unlock` 与 `unlock` 语义重复 → 有 `unlock` 时不再收 `note_unlock`。
只读 + 写新文件，不原地改；确认后再人工替换。
"""

import io
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "_meta" / "channels.yaml"
DST = ROOT / "tmp" / "channels_deduped.yaml"

text = SRC.read_text(encoding="utf-8")
lines = text.split("\n")

ci = next(i for i, l in enumerate(lines) if l.startswith("channels:"))
cg = next(i for i, l in enumerate(lines) if l.startswith("content_gate:"))

head = lines[: ci + 1]
mid = lines[ci + 1: cg]
tail = lines[cg:]

BLOCK_START = re.compile(r"^  - id:\s*(\S+)")


def split_blocks(body: list) -> tuple[list, list]:
    """返回 (preamble 注释行, [ (id, [lines]) ])。每块含其前置注释行。"""
    preamble: list = []
    blocks: list = []
    carry: list = []          # 尚未归属的注释行
    cur_id = None
    cur: list = []
    for l in body:
        m = BLOCK_START.match(l)
        if m:
            if cur_id is not None:
                blocks.append((cur_id, cur))
            cur_id = m.group(1)
            cur = carry + [l]
            carry = []
            continue
        if cur_id is None:
            if l.strip().startswith("#") or not l.strip():
                carry.append(l)
            continue
        if l.strip().startswith("#"):
            carry.append(l)
        else:
            cur.extend(carry)
            carry = []
            cur.append(l)
    if cur_id is not None:
        cur.extend(carry)
        blocks.append((cur_id, cur))
    preamble.extend(carry)
    return preamble, blocks


def parse_block(blk: list) -> tuple[list, list, list]:
    """→ (前置注释, [ (key, [lines]) ])。blk[0] 未必是 id 行（块前注释会被并入）。"""
    pre: list = []
    keys: list = []
    pending_cmt: list = []
    id_at = next(i for i, l in enumerate(blk) if BLOCK_START.match(l))
    pre = blk[:id_at]
    for l in blk[id_at + 1:]:
        if l.strip().startswith("#"):
            pending_cmt.append(l)
            continue
        m = re.match(r"^    ([A-Za-z_]\w*):", l)
        if m:
            keys.append((m.group(1), pending_cmt + [l]))
            pending_cmt = []
        elif keys:
            keys[-1][1].append(l)
        else:
            pending_cmt.append(l)
    return pre, keys


preamble, raw_blocks = split_blocks(mid)
print(f"blocks={len(raw_blocks)} ids={len({b[0] for b in raw_blocks})}")

# id → 出现顺序 + 候选 block 列表
order: list = []
by_id: dict = {}
for bid, blk in raw_blocks:
    if bid not in by_id:
        by_id[bid] = []
        order.append(bid)
    by_id[bid].append(blk)

out: list = []
dropped = 0
for bid in order:
    cands = []
    for blk in by_id[bid]:
        pre, keys = parse_block(blk)
        cands.append((len(keys), pre, keys, blk))
    cands.sort(key=lambda t: -t[0])
    _, pre, keys, _ = cands[0]
    have = {k for k, _ in keys}
    for n, _p, k2, _b in cands[1:]:
        dropped += 1
        for k, klines in k2:
            if k in have:
                continue
            if k == "note_unlock" and "unlock" in have:
                continue
            keys.append((k, klines))
            have.add(k)
    out.append("")            # 块间空行（沿用原风格）
    out.extend(pre)
    out.append(f"  - id: {bid}")
    for k, klines in keys:
        out.extend(klines)
    extra = len(by_id[bid]) - 1
    print(f"  {bid:16s} 副本×{len(by_id[bid])} 字段{len(keys)}  合并丢弃副本 {extra}")

out.extend(preamble)      # 尾部未归属的注释（属于 content_gate 段）留在最后
new_text = "\n".join(head + out + [""] + tail)
DST.write_text(new_text, encoding="utf-8")
print(f"\n原 {len(text.splitlines())} 行 → 新 {len(new_text.splitlines())} 行；丢弃副本 block {dropped}")
print(f"写出 {DST}")
