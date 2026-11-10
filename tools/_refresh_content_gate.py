# -*- coding: utf-8 -*-
"""刷新 _meta/channels.yaml 的 content_gate 段（2026-11-09 轮）。

四道自检（skill 硬约束，缺一不可）：
 1. 写盘前断言「头部前缀未变」+「`  - id:` 行数未变」
 2. 逐 block `{`/`}` 配平
 3. 项目自己的 load_channels_yaml 读一遍（channels/disabled/rows）
 4. 与 HEAD 版本 loader 读数逐项对比
"""
import sys, pathlib, subprocess, tempfile, os

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from kb_common import load_channels_yaml  # noqa: E402

YML = ROOT / "_meta" / "channels.yaml"
NEW_DATE = "2026-11-10"
NEW_OVERALL = "4160/4705（88%）"

# id -> (新 ratio, 追加的 note 片段；不含 ASCII 逗号/冒号空格/方括号/花括号)
ROWS = {
    "producthunt": ("695/702",
        "2026-11-10 轮 695/702（99%）/ 采集 30 条 new 23 chg 2（列表轮转）"),
    "betalist": ("341/342",
        "2026-11-10 轮 341/342（99.7%）/ 采集 12 条 new 2 chg 10 / 发布日 12/12"),
    "devto": ("23/29",
        "2026-11-10 轮 23/29（79%）/ 采集 6 条 new 0 chg 1 / irrelevant 6 resource 2 trunc 1 结构未变"),
    "bilibili": ("76/81",
        "2026-11-10 轮 76/81（94%）/ 采集 10 条 new 1 chg 9（探针 ok 6 videos）/ 丢弃 2-12（标题 1 + 无主题词 1）逐条核无误杀"),
    "indiehackers": ("180/184",
        "2026-11-10 轮 180/184（98%）/ 采集 20 条 new 2 chg 16（列表未轮转，project_url 继承 6）"),
    "hn_show": ("2038/2147",
        "2026-11-10 轮 2038/2147（95%）/ 采集 40 条 new 40 / 残余 unusable 109 summary 34 trunc 40 结构未变"),
    "github_new": ("66/94",
        "2026-11-10 轮 66/94（70%）/ 采集 11 条 new 1 chg 8 / 丢弃 17-28（标题 7 journal-wiki-clone-awesome-directory + 无主题词 10 库与 demo）逐条核无误杀"),
    "v2ex": ("204/282",
        "2026-11-10 轮 204/282（72%）/ 采集 22 条 new 13 chg 3 / 丢弃 3-25（标题 3 招聘类）无误杀"),
    "exa_discovery": ("40/48",
        "2026-11-10 轮 40/48（83%，周二非 weekly 未跑，比率沿用上次实测）/ 上次 周一 --force-weekly 覆盖 采集 10 条"),
    "reddit": ("491/788",
        "2026-11-10 轮 491/788（62% 仍全库最低，irrelevant 277 为主噪声）/ 采集 23 条 new 23 / 评论覆盖 97% 达标"),
    "c1c7": ("5/7",
        "2026-11-10 轮 5/7（71%，n=7 小样本，n<10 抖动大须连 n 一起看）/ 采集 7 条 new 0 chg 1（17 entries 好窗口）/ 丢弃 10-17 全是名录-媒体-播客，政策命中正确"),
}

# ---- 读原文件 ----
raw = YML.read_text(encoding="utf-8")
if f"audited_at: '{NEW_DATE}'" in raw:
    raise SystemExit(f"[skip] content_gate 已刷新到 {NEW_DATE}（本脚本按轮次改数值+追加 note，不可重复执行）")
lines = raw.splitlines(keepends=True)

start = next(i for i, l in enumerate(lines) if l.startswith("content_gate:"))
end = next(i for i, l in enumerate(lines) if i > start and l.startswith("# ---------------- 后端可用性订正"))

prefix = lines[:start + 1]   # 含 `content_gate:` 行本身（漏它会让 audited_at 挂到顶层）
tail = lines[end:]

# 原文件结构性计数
old_id_count = sum(1 for l in lines if l.startswith("  - id:"))

# ---- 切 block ----
body = lines[start + 1:end]
gate_head, rest = [], []
for i, l in enumerate(body):
    if l.lstrip().startswith("- {id:"):
        rest = body[i:]
        break
    gate_head.append(l)
else:
    raise SystemExit("content_gate 段内没有 rows block")

blocks, cur, depth = [], [], 0
for l in rest:
    cur.append(l)
    depth += l.count("{") - l.count("}")
    if depth == 0 and cur and cur[0].lstrip().startswith("- {id:"):
        blocks.append(cur)
        cur = []
trailer = []
if cur:
    if cur[0].lstrip().startswith("- {id:"):
        raise SystemExit("尾部残留未闭合 block")
    trailer = cur  # 段末空行等原样保留

new_body, seen_ids = [], []
for blk in blocks:
    head = blk[0]
    cid = head.split("- {id:")[1].split(",")[0].strip()
    seen_ids.append(cid)
    if cid not in ROWS:
        new_body.extend(blk)
        continue
    new_ratio, add_note = ROWS[cid]
    # 1) ratio
    old_ratio = head.split("ratio: '")[1].split("'")[0]
    blk[0] = blk[0].replace(f"ratio: '{old_ratio}'", f"ratio: '{new_ratio}'", 1)
    # 2) 末尾 note 追加（只改最后一行，末尾必须是 }）
    last = blk[-1].rstrip("\n")
    assert last.endswith("}"), f"{cid} 末行不以 }} 结尾: {last[-40:]!r}"
    blk[-1] = last[:-1] + "；" + add_note + "}\n"
    new_body.extend(blk)

# 断言：11 行全命中
missing = [c for c in ROWS if c not in seen_ids]
assert not missing, f"未匹配到行: {missing}"

# ---- 头部字段替换（audited_at / overall 在 gate_head 里，不在 block 里）----
hit = []
for i, l in enumerate(gate_head):
    if l.startswith("  audited_at:"):
        gate_head[i] = f"  audited_at: '{NEW_DATE}'\n"
        hit.append("audited_at")
    elif l.startswith("  overall:"):
        gate_head[i] = f"  overall: '{NEW_OVERALL}'\n"
        hit.append("overall")
assert hit == ["audited_at", "overall"], f"头部字段替换异常: {hit}"

# ---- 第一道自检：前缀/结构性计数（写盘前）----
out_lines = prefix + gate_head + new_body + trailer + tail
new_id_count = sum(1 for l in out_lines if l.startswith("  - id:"))
assert new_id_count == old_id_count, f"`  - id:` 计数变化 {old_id_count} -> {new_id_count}"
assert out_lines[:start + 1] == prefix, "头部前缀被改动"
assert len(out_lines) == len(lines), f"行数变化 {len(lines)} -> {len(out_lines)}（只应做同位置替换，不该增删行）"

# ---- 第二道自检：逐 block 花括号配平 ----
depth = 0
for l in out_lines[start:]:
    depth += l.count("{") - l.count("}")
assert depth == 0, f"content_gate 之后花括号不平衡: depth={depth}"

new_text = "".join(out_lines)
if new_text.startswith("version: 2"):
    new_text = new_text.replace("version: 2", "version: 2", 1)
# updated 同步（按行正则，别写死上一轮的日期 —— 写死会在日期滚动后静默失效）
import re as _re  # noqa: E402
new_text, n_upd = _re.subn(r"^updated: '[0-9]{4}-[0-9]{2}-[0-9]{2}'",
                           f"updated: '{NEW_DATE}'", new_text, count=1, flags=_re.M)
assert n_upd == 1, f"updated 行替换失败（n={n_upd}）"

YML.write_text(new_text, encoding="utf-8")
print(f"[write] {YML} lines {len(lines)} -> {len(out_lines)} · `  - id:` {old_id_count} 未变")

# ---- 第三道自检：loader ----
d = load_channels_yaml(YML)
rows = d.get("content_gate", {}).get("rows", [])
print(f"[loader] channels={len(d['channels'])} disabled={len(d.get('disabled', []))} rows={len(rows)} audited_at={d['content_gate'].get('audited_at')}")

# ---- 第四道自检：与 HEAD 版本对比 ----
head_raw = subprocess.run(["git", "show", "HEAD:_meta/channels.yaml"], cwd=str(ROOT),
                          capture_output=True, text=True, encoding="utf-8").stdout
tmp = pathlib.Path(tempfile.gettempdir()) / "channels_head_20261108.yaml"
tmp.write_text(head_raw, encoding="utf-8")
dh = load_channels_yaml(tmp)
print(f"[HEAD ] channels={len(dh['channels'])} disabled={len(dh.get('disabled', []))} rows={len(dh.get('content_gate', {}).get('rows', []))}")
assert len(d["channels"]) == len(dh["channels"]), "channels 数与 HEAD 不一致"
assert len(d.get("disabled", [])) == len(dh.get("disabled", [])), "disabled 数与 HEAD 不一致"
assert len(rows) == len(dh.get("content_gate", {}).get("rows", [])), "content_gate 行数与 HEAD 不一致"
assert [c["id"] for c in d["channels"]] == [c["id"] for c in dh["channels"]], "渠道 id 序列与 HEAD 不一致"
print("[ok] 四道自检全过")
for r in rows:
    print("   ", r.get("id"), r.get("ratio"), r.get("verdict"))
