"""kb_healthcheck — 库健康度自检（独立于 kb_analyze 的计数复核）。

用法：python tools/kb_healthcheck.py
核对：
  ① `20-语料/**/*.md` 数 == 在库（live）唯一条目数
  ② live 中「应有项目页」的条目（is_project_ish）全部能找到对应页 → 缺失 0
  ③ 缺 url == 0
  ④ wikilink 断链 == 0（全库解析：先按路径，再按文件名兜底，最后按 alias）
  ⑤ 路径可复现：按当前 slug 规则重算 == 实际路径
  ⑥ 孤立语料 == 0：`20-语料/` 每条 note 至少被一个 wikilink 指向
     —— 抓的是「有原料没出口」：项目页 / 人物页 / 方法论页 / 报告 / MOC 都没引到它，
     它就只是磁盘上占位，Obsidian 检索图谱里等于不存在。
  ⑦ 软门 · project_url 合法性：live 条目里「显然不是项目站」的归并键有几条
     —— 它错了会**静默合并两个项目**（② 按文件名匹配，看不出这种塌陷）。
  ⑧ 软门 · 共用项目页的条目组：同一项目的多条语料共页属正常，故只报数供复核。

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
    """取 frontmatter 里的 aliases（块式 `  - x` 与行内式 `[a, b]` 都支持）。"""
    out: list[str] = []
    for ln in txt.splitlines()[:40]:
        m = re.match(r"^aliases?:\s*(.*)$", ln)
        if not m:
            continue
        rest = m.group(1).strip()
        if rest.startswith("["):
            out += [x.strip().strip("\"'") for x in rest.strip("[]").split(",")]
        break
    else:
        return out
    # 块式：aliases: 之后的 `  - x` 行
    lines = txt.splitlines()[:60]
    try:
        i = next(i for i, ln in enumerate(lines) if re.match(r"^aliases?:\s*$", ln))
    except StopIteration:
        return [a for a in out if a]
    for ln in lines[i + 1:]:
        m = re.match(r"^\s+-\s+(.+)$", ln)
        if not m:
            if ln.strip():
                break
            continue
        out.append(m.group(1).strip().strip("\"'"))
    return [a for a in out if a]


alias_names: set[str] = set()
for p in notes:
    alias_names.update(_aliases(p.read_text(encoding="utf-8")))

broken: dict[str, list[str]] = {}
edges = 0
for p in notes:
    txt = KB.strip_code(p.read_text(encoding="utf-8"))
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
        if raw in by_rel or by_name.get(raw.split("/")[-1]) or raw in alias_names:
            continue
        if tgt in by_rel or by_name.get(tgt.split("/")[-1]) or tgt in alias_names:
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
print(f"⑤ 路径可复现  漂移={len(drift)}  {'OK' if not drift else '!! 有漂移'}")
for a, b in drift[:5]:
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
status = "OK" if not orphans else f"⚠ 有孤立 {len(orphans)} 条（软门，见待办 P1-B 尾）"
print(f"⑥ 孤立语料（无入链）  数量={len(orphans)}  {status}")
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
