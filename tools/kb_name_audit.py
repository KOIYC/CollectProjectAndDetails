"""kb_name_audit — 全库文件名与目录框架审计（只读）。

背景：文件名不是「看起来整齐」就行 —— 它是 **wikilink 的解析键**：
  * `[ ] # ^` 是 Obsidian 的 wikilink 语法字符（`#`=标题锚点、`]`=链接收尾）→ 谁引用谁断链；
  * `` ` `` 让断链检查器把指向它的链接当「正文伪代码」跳过（kb_healthcheck 的 LINK_JUNK）→ 检查盲区；
  * **同一个 stem 出现在两个目录** → `[[短名]]` 在 Obsidian 里解析结果不确定（按创建顺序/设置）；
  * 文件名与「按当前 slug 规则反算的规范名」不一致 → 下一轮采集会在规范路径写出**第二份**，① 等式当场破功。

规范名唯一来源 = `kb_common.slugify`（经 `kb_navfix.canon_stem` 从记录反算）。
本工具**只审计不修改**：改名一律走 `kb_navfix.py --fix-names`（带 manifest + seen.json 同步 + 链接改写）。

用法：
  python tools/kb_name_audit.py            # 打印 + 写 00-索引/报告/命名审计.md
  python tools/kb_name_audit.py --quiet    # 只打印
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_common import DIR_REPORT, ROOT, iso, now_cst                        # noqa: E402
from kb_collect import corpus_note_path, is_project_ish, method_note_path, \
    person_note_path, project_note_path                                    # noqa: E402
import kb_analyze as KA                                                     # noqa: E402

# 目录框架：顶层允许的目录与根文件（Johnny.Decimal 式两位前缀；60/70 留空备用）
EXPECTED_DIRS = {"00-索引", "10-项目", "20-语料", "30-人物", "40-方法论",
                 "50-渠道", "80-归档", "90-原始", "_meta", "tools"}
EXPECTED_ROOT_FILES = {"Home.md", "AGENTS.md"}
CONTENT_DIRS = ("20-语料", "80-归档", "10-项目", "30-人物")        # fix-names 的辖区
RAW_DIR = ROOT / "90-原始"

# wikilink 语法字符 + 反引号（检查盲区）+ Windows 明令禁止（理论上不会出现，留作断言）
WIKILINK_SYNTAX = re.compile(r"[\[\]#^`]")
ILLEGAL = re.compile(r'[<>:"/\\|?*\x00-\x1f]')

# `80-归档/重复副本/` 是**去重暂存区**：`kb_prune.py --dedupe-archive` 的「只移不删」undo 现场
# （同一条目的多余快照，原 stem 保留才能按 manifest 搬回）。它不是知识面 ——
# 里面必然是 live 页的同 stem 副本，参与「同 stem 多目录」检查会稳定误报
# （2026-09-21 实测 52 处，全部是 live 页 vs 暂存区副本，与「冻结区只查语法字符」的规则自相矛盾）。
# 因此整个暂存区不参与命名检查；`80-归档/posts|项目|野页` 仍照常查语法字符。
DEDUPE_QUARANTINE = "80-归档/重复副本"


def _is_quarantined(p: Path) -> bool:
    return p.relative_to(ROOT).as_posix().startswith(DEDUPE_QUARANTINE + "/")


def scan() -> dict:
    issues: dict[str, list[str]] = collections.defaultdict(list)
    notes = [p for p in ROOT.rglob("*.md")
             if not any(part.startswith(".") for part in p.relative_to(ROOT).parts)
             and not _is_quarantined(p)]

    top_dirs = {p.name for p in ROOT.iterdir() if p.is_dir() and not p.name.startswith(".")}
    for d in sorted(top_dirs - EXPECTED_DIRS):
        issues["意外顶层目录"].append(d)
    for p in ROOT.iterdir():
        if p.is_file() and p.name not in EXPECTED_ROOT_FILES and not p.name.startswith("."):
            issues["意外根文件"].append(p.name)

    by_stem: dict[str, set[str]] = collections.defaultdict(set)
    by_dir_case: dict[str, dict[str, list[str]]] = collections.defaultdict(
        lambda: collections.defaultdict(list))
    for p in notes:
        rel = p.relative_to(ROOT).as_posix()
        by_stem[p.stem].add(str(p.parent.relative_to(ROOT)))
        by_dir_case[str(p.parent)][p.stem.casefold()].append(p.stem)
        if WIKILINK_SYNTAX.search(p.stem):
            issues["wikilink 语法字符/反引号"].append(rel)
        if ILLEGAL.search(p.stem):
            issues["Windows 非法字符"].append(rel)
        if p.stem != p.stem.rstrip(" ."):
            issues["尾随空格/点"].append(rel)
        if len(p.stem) > 100 or len(rel) > 200:
            issues["超长（stem>100 或路径>200）"].append(f"{rel} ({len(rel)})")
        if any(c.isspace() for c in (p.stem[0], p.stem[-1]) if p.stem):
            issues["首尾空白"].append(rel)

    for d, m in by_dir_case.items():
        for k, names in m.items():
            if len(names) > 1:
                issues["同目录大小写碰撞（Windows 视为同名）"].append(f"{d}: {names}")

    for stem, dirs in by_stem.items():
        if len(dirs) > 1:
            # 反引号包裹：报告里的「歧义示例」本身不能变成一条真 wikilink（否则审计报告自带断链）
            issues["同 stem 多目录（短链歧义）"].append(f"`{stem}.md` ← {' / '.join(sorted(dirs))}")

    # 90-原始 只该有 jsonl；语料/实体目录只该有 md
    for p in RAW_DIR.rglob("*"):
        if p.is_file() and p.suffix != ".jsonl":
            issues["90-原始 里的非 jsonl"].append(p.relative_to(ROOT).as_posix())
    for top in ("20-语料", "80-归档", "10-项目", "30-人物", "50-渠道"):
        for p in (ROOT / top).rglob("*"):
            if p.is_file() and p.suffix != ".md":
                issues[f"{top} 里的非 md"].append(p.relative_to(ROOT).as_posix())

    # 规范名核对 —— 实体页用**正向集合**（live 条目按当前规则应生成的页名），
    # 语料页用「item_id 反算」；`80-归档/` 整体**跳过规范名核对**（归档=冻结快照，
    # 规则变了他也不该跟着改名 —— 只做语法字符检查）。
    # 两个曾经的误报源（2026-09-20 踩过）：
    #   ① 用 setdefault 取记录会拿到**最早**那条而不是最新 —— kind/project_url 是后补的，
    #      由此 3 个人物页、45 个项目页被误报「无条目指向」。必须用 latest_by_item。
    #   ② 用 url 指纹反查实体页 —— 两个项目撞上同一个（错误的）project_url 时
    #      指纹去重把候选丢掉，反查失败 ≠ 页面漂移。改用正向集合。
    by_item = KA.latest_by_item(KA.load_records())
    live = [i for i in by_item.values() if KA._is_live(i)]
    forward = {project_note_path(i).stem for i in live if is_project_ish(i)}
    forward |= {person_note_path(i).stem for i in live if (i.get("kind") or "") == "person"}
    forward |= {method_note_path(i).stem for i in live if (i.get("kind") or "") == "method"}

    n_checked = n_drift = 0
    for top in CONTENT_DIRS:
        for p in sorted((ROOT / top).rglob("*.md")):
            if p.stem.endswith("-dup"):
                continue
            rel = p.relative_to(ROOT).as_posix()
            if top == "80-归档":
                continue                                        # 冻结区：不做规范名核对
            n_checked += 1
            if rel.startswith("20-语料/"):
                sp = p.read_text(encoding="utf-8").split("\n---", 1)
                iid = None
                for ln in sp[0].splitlines():
                    if ln.startswith("item_id:"):
                        iid = ln.split(":", 1)[1].strip().strip('"')
                        break
                rec = by_item.get(iid) if iid else None
                if not rec:
                    issues["无法反算（语料页无 item_id 记录）"].append(rel)
                    continue
                m = re.search(r"posts/[^/]+/(\d{4}-\d{2}-\d{2})/", rel)
                want = corpus_note_path(rec, m.group(1) if m else "").stem
                if want != p.stem:
                    n_drift += 1
                    issues["规范名漂移（记录反算 ≠ 实名）"].append(f"{rel} → {want}.md")
            elif p.stem in forward:
                pass                                            # 实体页规范 ✓
            elif p.name in ("README.md", "index.md", "索引.md") or "说明" in p.stem:
                pass                                            # 手写说明页，不做记录反算
            else:
                issues["实体页无在库条目指向（历史页/漂移/指纹撞车）"].append(rel)

    n_note = len(notes)
    n_empty_dirs = sum(1 for d in EXPECTED_DIRS if (ROOT / d).is_dir()
                       and not any((ROOT / d).rglob("*")))
    return {"issues": issues, "n_note": n_note, "n_checked": n_checked,
            "n_drift": n_drift, "n_empty_dirs": n_empty_dirs,
            "top_dirs": top_dirs}


def render(r: dict) -> str:
    gen = iso(now_cst())
    L = ["---", "type: report", 'title: "命名与目录框架审计"', "tags:", "  - 报告",
         f'updated: "{gen}"', "---", "",
         "# 命名与目录框架审计", "",
         f"> 审计 {r['n_note']} 个 note；其中 {r['n_checked']} 个做了规范名核对"
         f"（语料页按 item_id 反算、实体页按 live 条目正向集合，`80-归档/` 冻结区只查语法字符，"
         f"去重暂存区 `{DEDUPE_QUARANTINE}/` 整体不参与）。"
         f"生成于 {gen}。",
         "> 本工具**只审计不修改**；改名一律走 `kb_navfix.py --fix-names`（带 undo 清单）。", ""]
    if not r["issues"]:
        L += ["**全部通过：没有发现违规文件名或目录漂移。**", ""]
        return "\n".join(L)
    total = sum(len(v) for v in r["issues"].values())
    L += [f"**发现 {total} 处，分 {len(r['issues'])} 类：**", "",
          "| 类别 | 数量 | 风险 |", "|---|---|---|"]
    why = {
        "wikilink 语法字符/反引号": "高 —— `[ ] # ^` 是链接语法字符；反引号让断链检查器跳过指向它的链接（盲区）",
        "同 stem 多目录（短链歧义）": "中 —— `[[短名]]` 解析结果不确定",
        "规范名漂移（记录反算 ≠ 实名）": "高 —— 下轮采集会在规范路径写出第二份，计数等式破功",
        "实体页无在库条目指向（历史页/漂移/指纹撞车）": "中 —— 可能是历史页（该归档）、也可能 project_url 撞车导致两个项目共页",
        "同目录大小写碰撞（Windows 视为同名）": "高 —— Windows 不区分大小写，两者互相覆盖",
        "意外顶层目录": "低 —— 框架外的新顶层，先确认是否该进规范",
        "无法反算（语料页无 item_id 记录）": "低 —— 手写页或历史页，不强制改名",
    }
    for k, v in sorted(r["issues"].items(), key=lambda kv: -len(kv[1])):
        L.append(f"| `{k}` | {len(v)} | {why.get(k, '—')} |")
    L += ["", "## 明细", ""]
    for k, v in sorted(r["issues"].items(), key=lambda kv: -len(kv[1])):
        L += [f"### {k}（{len(v)}）", ""]
        L += [f"- {x}" for x in v[:60]]
        if len(v) > 60:
            L.append(f"- …其余 {len(v) - 60} 条")
        L.append("")
    L += ["## 修复路径", "", "```bash",
          "python tools/kb_navfix.py --fix-names --dry   # 先看会改哪些（判据同本审计）",
          "python tools/kb_navfix.py --fix-names         # 真改名（manifest + seen.json + 链接改写）",
          "python tools/kb_navfix.py --fix-names         # 复跑必须为空（幂等验证）",
          "python tools/kb_healthcheck.py                # 五项不变量收尾",
          "```", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true", help="不写报告文件")
    args = ap.parse_args(argv)

    r = scan()
    md = render(r)
    if not args.quiet:
        out = DIR_REPORT / "命名审计.md"
        out.write_text(md, encoding="utf-8", newline="\n")
        print(f"[报告] {out.relative_to(ROOT).as_posix()}")
    tail = md.split("## 明细")[0]
    print(tail)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
