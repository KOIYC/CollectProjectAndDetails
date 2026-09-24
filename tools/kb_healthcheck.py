"""kb_healthcheck — 库健康度自检（独立于 kb_analyze 的计数复核）。

用法：python tools/kb_healthcheck.py
退出码：**硬门 ①-⑤ 任一非零 → 退出码 1**（⑥⑦⑧⑨ 是软门，只报不阻断）。
  —— 为什么必须给退出码：此前它恒返 0，`kb_selftest.py` 里
  `assertEqual(p.returncode, 0)` 是**恒真断言**（检查器红也照样过），
  自动化/CI 也无法靠退出码判收工门。检查器报红但进程报成功 = 最坏的一种绿。
核对：
  ① `20-语料/**/*.md` 数 == 在库（live）唯一条目数
  ② live 中「应有项目页」的条目（is_project_ish）全部能找到对应页 → 缺失 0
  ③ 缺 url == 0
  ④ wikilink 断链 == 0（全库解析：先按路径，再按文件名兜底，最后按 alias）
  ⑤ 路径可复现：按当前 slug 规则重算 == 实际路径，且 磁盘 ↔ seen 账本 **双向**无差集
  ⑥ 孤立语料（软门）：`20-语料/` 每条 note 至少被一个 wikilink 指向
     —— 抓的是「有原料没出口」：项目页 / 人物页 / 方法论页 / 报告 / MOC 都没引到它，
     它就只是磁盘上占位，Obsidian 检索图谱里等于不存在。
  ⑦ 软门 · project_url 合法性：live 条目里「显然不是项目站」的归并键有几条
     —— 它错了会**静默合并两个项目**（② 按文件名匹配，看不出这种塌陷）。
  ⑧ 软门 · 共用项目页的条目组：同一项目的多条语料共页属正常，故只报数供复核。
  ⑨ 软门 · 单渠道**存量**占比（条目 / 项目页）：门槛 ≤50%，超门槛只报不阻断
     —— 与运行日志的「当日新增」口径是两回事，历史铺底偏向只能靠新增稀释。

为什么②不能用「10-项目 文件数 == live project_url 去重数」：
项目页文件名取 `project_url or url`（无 project_url 的条目按自身 url 建页），
而已归档条目的旧页**可能已被 kb_prune --archive-entities 移进 80-归档/**。
所以 `10-项目/` 文件数天然 ≤ 应有页数，直接相减会错。
用文件名逐个匹配 live 条目才是有效判据 —— 直接相减会报出 260+ 的假孤儿（实测踩过）。

读 JSONL 一律用 KB.load_ndjson()（按 \n 切）：`read_text().splitlines()` 会按
U+2028 类字符切分，把含这类字符的记录切成碎片后静默丢条（实测少报 7 条记录）。
"""
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import kb_analyze as KA  # noqa: E402
import kb_collect as KC  # noqa: E402
import kb_common as KB  # noqa: E402
from kb_common import split_note, fm_scalars, fm_list  # noqa: E402

raw = collections.Counter()
ids = set()
# 读 JSONL 必须走 KB.load_ndjson()（按 \n 切）：`read_text().splitlines()` 会按
# U+2028 类字符切分，把含这类字符的记录切成碎片后静默丢条 —— 实测 raw 少报 7 条、
# unique 少报 1 条，与 kb_analyze 的数字当场打架。
for f in (ROOT / "90-原始").rglob("*.jsonl"):
    ch = f.parent.name
    for r in KB.load_ndjson(f):
        raw[ch] += 1
        ids.add(r.get("item_id"))
print(f"raw records={sum(raw.values())} unique_item_ids={len(ids)}")
for k, v in raw.most_common():
    print(f"  {k:16s} {v}")

corpus = list((ROOT / "20-语料").rglob("*.md"))
proj_files = {p.name for p in (ROOT / "10-项目").rglob("*.md")}

rows = KA.load_records()
by_item = KA.latest_by_item(rows)
items = list(by_item.values())
live = [i for i in items if KA._is_live(i)]

print(f"① 20-语料 md={len(corpus)}  在库唯一条目={len(live)}  "
      f"{'OK' if len(corpus) == len(live) else '!! 不一致'}")

should = [i for i in live if KC.is_project_ish(i)]
missing = [i for i in should if pathlib.Path(KC.project_note_path(i)).name not in proj_files]
print(f"② 应有项目页={len(should)}（10-项目 现有 {len(proj_files)} 个；其余为历史页，"
      f"已由 kb_prune --archive-entities 移出）  缺页={len(missing)}  "
      f"{'OK' if not missing else '!! 缺页'}")
for i in missing[:5]:
    print(f"     缺页: [{i['source_id']}] {i['title'][:50]}")

no_url = [i for i in live if not (i.get("url") or "").strip()]
print(f"③ 缺 url={len(no_url)}  {'OK' if not no_url else '!! 有缺 url 条目'}")

# ④ wikilink 断链：Obsidian 先按 vault 相对路径解析，路径式链接失败时按文件名兜底；
#    `[[短名]]` 本来就是按文件名解析的，不算断链。代码块里的 `[[x]]` 不是链接，先摘掉。
#    **alias 也算解析目标** —— Obsidian 会按 frontmatter `aliases` 解析链接，
#    检查器不认 alias 就会把有效链接报成断链（实测：`[[从这里开始]]` 指向 浏览.md 的 alias，
#    3 处全被误报）。检查器必须和 Obsidian 一样宽，否则它逼着你写更差的链接文本。
LINK = re.compile(r"\[\[(.+?)\]\]")
LINK_JUNK = re.compile(r"[\[\]\"`$*\\]")      # 正文里的残余伪链接
notes = [p for p in ROOT.rglob("*.md")
         if not any(part.startswith(".") for part in p.relative_to(ROOT).parts)]
by_rel = {p.relative_to(ROOT).with_suffix("").as_posix() for p in notes}
by_name: dict[str, int] = {}
for p in notes:
    by_name[p.stem] = by_name.get(p.stem, 0) + 1


def _aliases(txt: str) -> list[str]:
    """取 frontmatter 里的 aliases —— 复用 kb_common 的**列表**解析器 `fm_list`。

    为什么不能用 `fm_scalars`：它按设计**跳过列表块**（只服务标量键的定点改写），
    `aliases:` 是块式列表 → 读回来是空串 → 有效 alias 链接被报成断链。
    2026-09-24 实测：`[[从这里开始]]` 指向 `浏览.md` 的 alias，因这一处不对称
    被误报 3 处断链（生成端一直写块式 `- "别名"`）。检查器的判据必须与生成端同一份解析。
    """
    head = split_note(txt)[0] if split_note(txt) else ""
    vals = fm_list(head, "aliases") or fm_list(head, "alias")
    if vals:
        return vals
    fm = fm_scalars(head)                     # 兜底：行内 `aliases: [a, b]` /
    val = fm.get("aliases") or fm.get("alias") or ""   # 单标量 `alias: x`
    return [a.strip().strip("\"'") for a in str(val).strip("[]").replace("，", ",").split(",") if a.strip()]


alias_names: set[str] = set()
for p in notes:
    alias_names.update(_aliases(p.read_text(encoding="utf-8")))


def _resolves(s: str) -> bool:
    """链接目标能否解析（与 Obsidian 同宽）：路径 / 文件名 / 文件名带 `.md` / alias。

    `.md` 后缀必须认：Obsidian 里 `[[内容审计-all.md]]` 与 `[[内容审计-all]]` 等价，
    检查器只认前者才叫窄 —— 窄的检查器会逼着人把链接写得更差（2026-09-24 实测：
    手写报告里的 `[[xxx.md]]` 被全数误报，而 Obsidian 打开是好的）。
    """
    if not s:
        return False
    if s in by_rel or s in alias_names:
        return True
    if s.endswith(".md") and s[:-3] in by_rel:
        return True
    tail = s.split("/")[-1]
    if tail.endswith(".md"):
        tail = tail[:-3]
    return bool(by_name.get(tail)) or tail in alias_names

def _link_scannable(p: pathlib.Path, txt: str) -> str:
    """语料页只扫**我们生成的部分**（frontmatter + 导航/关联链接段），正文整段不扫。

    为什么：语料 body 是**外站原文**，不是我们写的链接。一篇讲 Obsidian 的 Show HN 正文里
    出现 `[[keys.command]]`、`[[demo-project-atlas]]` 是**内容**，检查器照扫就会报断链
    （2026-09-21 实测 3 处假警报，且这类「讲 Obsidian 的帖子」会源源不断进来）。
    外部文本不能喂给链接检查器 —— 它分不清「引用」和「举例」。

    导航/关联链接段保留：那是我们写的，指向项目页/渠道页，断了就是真断了。
    """
    rel = p.relative_to(ROOT).as_posix()
    if not (rel.startswith("20-语料/") or rel.startswith("80-归档/posts/")):
        return txt
    lines = txt.splitlines()
    keep: list[str] = []
    in_fm = lines[:1] == ["---"]
    fm_done = False
    block_hdr = ""
    buf: list[str] = []
    i = 0
    # frontmatter：从 --- 到下一个 ---
    if in_fm:
        for j in range(1, len(lines)):
            keep.append(lines[j])
            if lines[j].strip() == "---":
                i = j + 1
                break
    else:
        i = 0
    fm_done = True
    del fm_done
    for ln in lines[i:]:
        if ln.startswith("## "):
            if block_hdr in ("导航", "关联链接"):
                keep.extend(buf)
            buf = []
            block_hdr = ln[3:].strip()
            continue
        buf.append(ln)
    if block_hdr in ("导航", "关联链接"):
        keep.extend(buf)
    return "\n".join(keep)


broken: dict[str, list[str]] = {}
edges = 0
for p in notes:
    txt = KB.strip_code(_link_scannable(p, p.read_text(encoding="utf-8")))
    if "[[" not in txt:
        continue
    src = p.relative_to(ROOT).as_posix()
    for m in LINK.finditer(txt):
        raw = m.group(1).split("|")[0].strip()
        tgt = raw.split("#")[0].strip()
        if not tgt or LINK_JUNK.search(tgt):
            continue
        edges += 1
        # 原始目标优先（文件名可含 `#`），再退到按 `#` 切分后的形式，最后按 alias 解析
        if _resolves(raw) or _resolves(tgt):
            continue
        broken.setdefault(raw, []).append(src)
print(f"④ wikilink 总数={edges}  断链目标={len(broken)}  "
      f"{'OK' if not broken else '!! 有断链'}")
print(f"     （按文件名 + 路径 + alias {len(alias_names)} 个解析）")
for tgt, srcs in list(broken.items())[:8]:
    print(f"     断链 [[{tgt}]] ← {srcs[0]}（共 {len(srcs)} 处）")

# ⑤ 语料 note 路径可复现：按当前 slug 规则重算，结果必须等于文件实际所在位置。
#    抓的是「改了 slugify 但没同步改名」这类静默漂移 —— 采集端下次会写到新路径，
#    于是在库里留下两份语料、计数等式①当场破功。
drift = []
for p in (ROOT / "20-语料").rglob("*.md"):
    rel = p.relative_to(ROOT).as_posix()
    first = p.read_text(encoding="utf-8").splitlines()
    iid = None
    for ln in first[:40]:
        if ln.startswith("item_id:"):
            iid = ln.split(":", 1)[1].strip().strip('"')
            break
    rec = by_item.get(iid) if iid else None
    if not rec:
        continue
    m = re.search(r"posts/[^/]+/(\d{4}-\d{2}-\d{2})/", rel)
    want = KC.corpus_note_path(rec, m.group(1) if m else "").relative_to(ROOT).as_posix()
    if want != rel:
        drift.append((rel, want))

# ⑤b 磁盘 ↔ 账本**双向**核对。为什么必须加：上面那段只拿「文件自己的日期桶」重算，
#    恒等于自身 → 漂移永远是 0。实测 2026-09-21 零点重跑采集，45 条语料落在新日期桶、
#    seen 却记旧桶（或反之），磁盘上留下两份语料 / 账本指向不存在的文件，① 当场破功，
#    而 ⑤ 一路报绿。差集两个方向都要看：
#      extra  = 在盘不在账（孤儿页：不进审计、不进洞察、没人链得到）
#      ghost  = 在账不在盘（幽灵：项目页链接指向 Obsidian 里打不开的目标）
_seen = KB.Seen()
_live_notes = {str(v.get("note") or "") for v in _seen.items.values()
               if str(v.get("note") or "").startswith("20-语料/")}
_disk_notes = {p.relative_to(ROOT).as_posix() for p in (ROOT / "20-语料").rglob("*.md")}
extra = sorted(_disk_notes - _live_notes)
ghost = sorted(_live_notes - _disk_notes)
drift += [(r, "(账本无记录 · 孤儿页)") for r in extra]
drift += [(r, "(磁盘无文件 · 幽灵账)") for r in ghost]
print(f"⑤ 路径可复现 (slug {len(drift) - len(extra) - len(ghost)}"
      f"+ 盘 - 账差异{len(extra)} / 幽灵{len(ghost)}) drift={len(drift)} "
      f"{'OK' if not drift else '!! DRIFT!'}")
for a, b in drift[:8]:
    print(f"     实际 {a}\n     应为 {b}")

# ⑥ 孤立语料（无入链）：20-语料/ 每条 note 至少被一个 wikilink 指向。
# 判据与 ④ 相同（路径 / 文件名 / alias 三种解析任一命中即算入链）；这一步复用 ④ 的
# `by_rel` / `by_name` / `alias_names` 结构，只多做一次「目标→文件路径」的反查。
# 为什么单独跑：④ 抓的是「链接指向不存在的目标」（断链），⑥ 抓的是「存在但没人指向」（孤岛）。
# 两者不重叠 —— 一条被建但被删链的语料在 ④ 绿、⑥ 红。
name_to_paths: dict[str, list[pathlib.Path]] = {}
for p in notes:
    name_to_paths.setdefault(p.stem, []).append(p)
alias_to_paths: dict[str, list[pathlib.Path]] = {}
for p in notes:
    for a in _aliases(p.read_text(encoding="utf-8")):
        alias_to_paths.setdefault(a, []).append(p)

inbound: set[str] = set()
for p in notes:
    txt = KB.strip_code(p.read_text(encoding="utf-8"))
    if "[[" not in txt:
        continue
    for m in LINK.finditer(txt):
        raw = m.group(1).split("|")[0].strip()
        tgt = raw.split("#")[0].strip()
        # 按路径
        for cand in (raw, tgt):
            if cand in by_rel:
                inbound.add(str((ROOT / cand).with_suffix(".md").resolve()))
        # 按文件名
        stem_tail_raw = raw.split("/")[-1]
        stem_tail_tgt = tgt.split("/")[-1]
        for s in {stem_tail_raw, stem_tail_tgt}:
            for q in name_to_paths.get(s, []):
                inbound.add(str(q.resolve()))
        # 按 alias
        for s in (raw, tgt):
            for q in alias_to_paths.get(s, []):
                inbound.add(str(q.resolve()))

orphans = []
for p in (ROOT / "20-语料").rglob("*.md"):
    if str(p.resolve()) not in inbound:
        orphans.append(p.relative_to(ROOT).as_posix())
# ① ~ ⑤ 是**硬不变量**（AGENTS.md 第六条「五项全绿」），任一非零即视为改动出错；
# ⑥ 是**软不变量**（提示性）：孤立语料 = 数据可访问性问题，不是数据完整性问题。
# 现存 3 例来自 write_person_note 首次建页时 corpus_rel=None，之后 obs 行的 "—" 无自愈路径 ——
# 已列入 [[待办与决策]] P1-B 尾。硬不变量之外，⑥ 只报不阻断收工。
status = "OK" if not orphans else f"! 孤立{len(orphans)}条 (软门)"
print(f"⑥ 孤立语料（无入链） 数量={len(orphans)}  {status}")
for o in orphans[:8]:
    print(f"     {o}")

# ⑦ 软门：live 条目的 project_url 是不是「能当项目页文件名 + 跨渠道归并键」的值。
#    为什么单列：它不是硬不变量（历史错值在 raw 里改不掉，只能靠 kb_reclassify 追加
#    repair 记录覆盖），但它错了会**静默合并两个项目** —— ② 按文件名匹配，两条不同
#    项目共用一个页名时照样报「缺页 0」（实测 6 条塌成 3 个页名）。
#    空值不算违规：没有 project_url 的项目页按自身 url 命名，是设计内的回退。
bad_pu = []
for i in live:
    pu = (i.get("project_url") or "").strip()
    if not pu:
        continue
    why = KC.project_url_reject(pu)
    if why:
        bad_pu.append((i, why))
print(f"⑦ live 条目 project_url 合法性  可疑={len(bad_pu)}  "
      f"{'OK' if not bad_pu else '⚠ 有可疑值（软门：kb_reclassify --project-url 订正）'}")
for i, why in bad_pu[:8]:
    print(f"     [{i['source_id']}] {why}｜{i.get('project_url')}｜{(i.get('title') or '')[:40]}")

# ⑧ 软门：多个条目共用同一个项目页名。
#    同一项目被多条语料观测到 → 共页**是正常的**（实测 page-rage 两条 HN 帖）；
#    所以这里只报数量供复核，判据交给 ⑦（错值）与人工。⚠ 不等于坏。
names = collections.Counter(pathlib.Path(KC.project_note_path(i)).name for i in should)
shared = {n: c for n, c in names.items() if c > 1}
print(f"⑧ 共用项目页的条目组  组数={len(shared)}／涉及 {sum(shared.values())} 条  "
      f"（同一项目多条语料属正常）")
for n, c in list(shared.items())[:8]:
    print(f"     {n} ← {c} 条")

# ⑨ 软门：单渠道**存量**占比 —— 质检门槛里「单渠道 ≤50%」此前没有任何脚本执行它。
#    为什么必须看存量而不是增量：运行日志一直报「单渠道最大占比 15%/16% ✅」，那是**当日新增**
#    口径；而库里实际存量为 hn_show 占条目 60%、占项目页 74%（历史铺底补采只回溯了 hn_show）。
#    门槛只管增量 = 全库分布可以一路朝单渠道漂移而报告全绿。这条软门不阻断收工（存量偏斜
#    只能靠采别的渠道稀释），但必须让它在收工门上可见 —— 引用「全库赛道分布」的结论，
#    在占比回到门槛内之前，实际含义是「HN 开发者在做什么」。
CHAN_CAP = 0.50
src_items = collections.Counter(i.get("source_id") or "?" for i in live)
src_pages = collections.Counter(i.get("source_id") or "?" for i in should)


def _top_share(counter) -> tuple[str, float, int]:
    tot = sum(counter.values())
    if not tot:
        return ("-", 0.0, 0)
    name, n = counter.most_common(1)[0]
    return (name, n / tot, tot)


for label, cnt in (("⑨ 单渠道存量占比（条目）", src_items), ("⑨ 单渠道存量占比（项目页）", src_pages)):
    name, share, tot = _top_share(cnt)
    print(f"{label}  最高={name} {share:.0%}／{tot} 条  门槛≤{CHAN_CAP:.0%}  "
          f"{'OK' if share <= CHAN_CAP else f'⚠ 超门槛（软门：历史铺底偏向，靠新增稀释）'}")
    for n2, c2 in cnt.most_common(4):
        print(f"     {n2:16s} {c2 / tot:5.1%} {c2}")

