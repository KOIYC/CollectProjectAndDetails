"""kb_moc — 导航地图层（MOC / Map of Content）。

背景（实测 2026-09-20）：`10-项目/` 有 647 个页面，但**没有地图**。
打开文件夹 = 面对 647 个文件名；Bases 视图能过滤，但**过滤是查询，不是导航** ——
查询要求你先知道自己在找什么，而「不知道该怎么看」的人恰恰不知道。
行业解是 MOC：一个 domain 一张（半）手工策展的索引页，带分组与一句话说明。

产出三张地图（全部落在 `00-索引/`，**不落进数据目录**）：
  00-索引/项目地图.md       `10-项目/` 的分组导航（按赛道）
  00-索引/归档与申诉.md      `80-归档/` 的东西是什么、为什么、怎么捞回来
  00-索引/报告/报告总览.md   历史报告一览（每条一句在讲什么）

为什么放 00-索引/ 而不是各自目录里：`10-项目/`、`20-语料/` 都被计数脚本按 `*.md` glob
（kb_healthcheck 等式①②、kb_prune、kb_reclassify）。往里塞一张 index 页会当场污染计数，
把「647 个项目」变成「648 个」。00-索引/ 本来就是导航层，没有任何计数脚本 glob 它。

用法：
  python tools/kb_moc.py            # 三张全出
  python tools/kb_moc.py --dry      # 只打印，不写盘
  python tools/kb_moc.py --only projects|archive|reports
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_common import (DIR_INDEX, DIR_PROJECTS, DIR_REPORT, META, ROOT, fm_scalars,  # noqa: E402
                       iso, now_cst, split_note, topic_of)
from kb_collect import is_project_ish, project_note_path                   # noqa: E402
from kb_content_audit import load_latest                                   # noqa: E402

DIR_ARCHIVE = ROOT / "80-归档"
ARCHIVE_PROJ = DIR_ARCHIVE / "项目"
ARCHIVE_POSTS = DIR_ARCHIVE / "posts"

MAP_PROJECTS = DIR_INDEX / "项目地图.md"
MAP_ARCHIVE = DIR_INDEX / "归档与申诉.md"
MAP_REPORTS = DIR_REPORT / "报告总览.md"

HEAD = "> 本页由 `python tools/kb_moc.py` 生成，**手改会被下次覆盖**。\n> 它是一张**导航地图**（MOC），不是数据 —— 数据在它指向的目录里。"

# 归档实体页的**启发式**分类（口径写在页面上，不假装是真实归档理由）。
# 真实的归档理由是「stale 且无任何在库引用」，理由存在 manifest 里、不在页面上，
# 所以这里只能按 project_url 的形态分组 —— 够用来找「我可能判错的那批」，且可复现。
HOST_CLASS = [
    ("讨论帖残留（reddit）", re.compile(r"^https?://(?:www\.)?reddit\.com/", re.I)),
    ("讨论帖残留（HN）", re.compile(r"^https?://news\.ycombinator\.com/", re.I)),
    ("代码仓库", re.compile(r"^https?://(?:www\.)?github\.com/", re.I)),
    ("视频/播客页", re.compile(r"^https?://(?:www\.)?(?:youtube\.com|youtu\.be|bilibili\.com)/", re.I)),
]


def _read_head(path: Path) -> dict:
    """读单页 frontmatter 标量（失败返回空 dict）。"""
    try:
        txt = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    sp = split_note(txt)
    return fm_scalars(sp[0]) if sp else {}


def _host_class(url: str) -> str:
    for name, rx in HOST_CLASS:
        if rx.match(url or ""):
            return name
    if not url:
        return "无链接"
    return "产品页 / 其它"


# ---------------------------------------------------------------- 项目地图

def project_rows() -> tuple[dict[str, dict], list[dict], int]:
    """把「磁盘上的项目页」与「在库语料」对起来。

    返回 (页面表, 在库项目型条目, 被跳过的 stale 页数)。页面表 key = 文件名 stem。
    数据源分工：**页面清单以磁盘为准**（那才是用户看到的东西），
    赛道/渠道/语料数靠 join 补 —— join 不上就老实标「未关联」，不猜。
    """
    pages: dict[str, dict] = {}
    n_stale = 0
    for p in sorted(DIR_PROJECTS.glob("*.md")):
        fm = _read_head(p)
        if fm.get("stale") == "true":
            # stale 页 = 已无在库语料指向、正走清面流程（liveness→archive-entities）。
            # 不列进地图：地图是「检索面」的导航，列它会把已判死的项目又递回用户眼前。
            # 它们的入口在 [[归档与申诉]]。
            n_stale += 1
            continue
        pages[p.stem] = {
            "stem": p.stem,
            "title": fm.get("title") or p.stem,
            "url": fm.get("project_url") or "",
            "first_seen": (fm.get("first_seen") or "")[:10],
            "topics": collections.Counter(),
            "channels": collections.Counter(),
            "n": 0,
        }

    items = [i for i in load_latest() if is_project_ish(i)]
    for it in items:
        stem = project_note_path(it).stem
        row = pages.get(stem)
        if row is None:                    # 页还没建（或已被归档）—— 记进未关联是错的，跳过
            continue
        row["n"] += 1
        row["topics"][topic_of(it)] += 1
        row["channels"][it.get("source_id") or "?"] += 1
    return pages, items, n_stale


def render_projects(pages: dict[str, dict], items: list[dict], n_stale: int = 0) -> str:
    gen = iso(now_cst())
    dated = gen[:10].replace("-", "")
    groups: dict[str, list[dict]] = collections.defaultdict(list)
    for row in pages.values():
        tp = row["topics"].most_common(1)
        row["topic"] = tp[0][0] if tp else "未关联（无在库语料）"
        groups[row["topic"]].append(row)

    n_all = len(pages)
    n_linked = sum(1 for r in pages.values() if r["n"])
    n_unlinked = n_all - n_linked
    n_corpus_all = sum(r["n"] for r in pages.values())

    L = [
        "---",
        "type: index",
        'title: "项目地图 · 按赛道分组"',
        "tags:",
        "  - 索引",
        "  - 导航",
        f'generated_at: "{gen}"',
        "aliases:",
        '  - "项目索引"',
        "---",
        "",
        f"# 项目地图 · `10-项目/` 的 {n_all} 个页面怎么找",
        "",
        HEAD,
        "",
        "## 为什么需要这一页",
        "",
        f"`10-项目/` 有 **{n_all}** 个页面。直接打开文件夹 = 面对 {n_all} 个文件名 —— "
        "那不是「组织好的」，只是「排好序的」。",
        "下面的 Bases 视图能按条件**过滤**，但过滤是**查询**：它要求你先知道自己在找什么。",
        "本页补的是**导航**：先按赛道分成几组，组内按在库语料数排，一眼看到「谁被反复观测到」。",
        "",
        "## 三种找法",
        "",
        "| 你想干什么 | 用什么 |",
        "|---|---|",
        "| 浏览某个赛道都有谁 | 下面的分组列表（本页） |",
        "| 按条件筛（渠道/语言/收录日） | [[从这里开始]] 里的 Bases「项目池」视图 |",
        "| 已知项目名 | Obsidian `Ctrl+O` 直接搜文件名，比翻目录快 |",
        "",
        "## 覆盖口径（先读，避免误用）",
        "",
        f"- 页面 **{n_all}** 个；其中能关联到在库语料的 **{n_linked}** 个"
        f"（{n_linked / max(1, n_all) * 100:.0f}%）"
        + (f"，其余 **{n_unlinked}** 个单列成「未关联」组，**不隐藏、不假装有语料**。"
           if n_unlinked else "，**没有关联不上的页面**。"),
        *([f"- 另有 **{n_stale}** 个已标 `stale` 的页面**不列在本图**"
           f"（已无在库语料指向、正走清面流程）→ 它们的入口在 [[归档与申诉]]。"]
          if n_stale else []),
        f"- 「语料 N」= 指向该项目的**在库**语料条数（不是票数、不是热度）。"
        f"全库在库项目型条目 {len(items)} 条，落到本页共 {n_corpus_all} 条。",
        "- 「赛道」由语料正文的关键词判定（`kb_common.TOPICS`），一个项目取**占比最高的那个**赛道；"
        "多赛道项目会被归到主要赛道，不做重复登记。",
        "- 本页只覆盖 `10-项目/`。已移出检索面的历史实体页在 [[归档与申诉]]。",
        "",
    ]

    # 组排序：先按项目数降序，「未关联」永远压最后（它不是赛道，是状态）
    order = sorted(groups, key=lambda g: (g.startswith("未关联"), -len(groups[g]), g))
    for g in order:
        rows = sorted(groups[g], key=lambda r: (-r["n"], r["title"].lower()))
        L += [f"## {g}（{len(rows)} 个项目）", ""]
        for r in rows:
            chs = "、".join(c for c, _ in r["channels"].most_common(4)) or "—"
            extra = f" · 语料 {r['n']}" if r["n"] else " · **无在库语料**"
            seen = f" · 首见 {r['first_seen']}" if r["first_seen"] else ""
            L.append(f"- [[{r['stem']}|{r['title'][:64]}]]{extra} · {chs}{seen}")
        L.append("")

    L += [
        "## 出口",
        "",
        "- 找原文 → 任一项目页的「观测历史」表，每行一串到语料页；或 [[从这里开始]] 的速查表",
        "- 找结论 → [[报告总览]]",
        "- 想知道为什么有些项目不在这里 → [[归档与申诉]]",
        "",
        f"_数据源：`10-项目/*.md`（页面清单）+ `90-原始/*/*.jsonl`（语料关联）"
        f"｜生成器：`tools/kb_moc.py`｜{gen}_",
        "",
    ]
    return "\n".join(L)


# ---------------------------------------------------------------- 归档与申诉

def _archive_facts() -> dict:
    """汇总归档事实：语料归档理由（来自 manifest）+ 实体页归档（来自磁盘）。"""
    reasons: collections.Counter = collections.Counter()
    by_channel: collections.Counter = collections.Counter()
    manifests = []
    for p in sorted(META.glob("prune_manifest_*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        moves = d.get("moves") or []
        if not moves:
            continue
        manifests.append({"name": p.name, "at": d.get("at") or "", "n": len(moves)})
        for m in moves:
            reasons[m.get("reason") or "未记理由"] += 1
            by_channel[m.get("source") or "?"] += 1

    ent_manifests = []
    ent_total = 0
    for p in sorted(META.glob("entity_archive_manifest_*.json")):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        moves = d.get("moves") or []
        ent_manifests.append({"name": p.name, "at": d.get("at") or "", "n": len(moves)})
        ent_total += len(moves)

    ent_classes: dict[str, list[dict]] = collections.defaultdict(list)
    for p in sorted(ARCHIVE_PROJ.glob("*.md")):
        fm = _read_head(p)
        ent_classes[_host_class(fm.get("project_url") or "")].append(
            {"stem": p.stem, "title": fm.get("title") or p.stem, "url": fm.get("project_url") or ""})

    n_arch_posts = len(list(ARCHIVE_POSTS.rglob("*.md")))
    return {"reasons": reasons, "by_channel": by_channel, "manifests": manifests,
            "ent_manifests": ent_manifests, "ent_total": ent_total,
            "ent_classes": ent_classes, "n_arch_posts": n_arch_posts,
            "n_arch_proj": len(list(ARCHIVE_PROJ.glob("*.md")))}


def render_archive() -> str:
    f = _archive_facts()
    gen = iso(now_cst())
    L = [
        "---",
        "type: index",
        'title: "归档与申诉 · 我判废的东西怎么捞回来"',
        "tags:",
        "  - 索引",
        "  - 导航",
        "  - 归档",
        f'generated_at: "{gen}"',
        "aliases:",
        '  - "归档索引"',
        "---",
        "",
        "# 归档与申诉 · `80-归档/` 里是什么，怎么捞回来",
        "",
        "> 归档 = **移出检索面**，**不是删除**。每个字节都还在库里，且每一次搬迁都写了 undo 清单。",
        "> 所以「当时判错了」是可修的，代价是一条命令。本页就是那条命令的入口。",
        "> 本页由 `python tools/kb_moc.py` 生成，**手改会被下次覆盖**。",
        "",
        "## 一眼看数",
        "",
        f"- 归档语料 **{f['n_arch_posts']}** 条（`80-归档/posts/<渠道>/`）",
        f"- 归档实体页 **{f['n_arch_proj']}** 个（`80-归档/项目/`）",
        f"- 归档清单 **{len(f['manifests']) + len(f['ent_manifests'])}** 份（`_meta/*manifest_*.json`，undo 靠它）",
        "",
        "## 语料为什么被归档",
        "",
        "| 归档理由 | 条数 | 含义 |",
        "|---|---|---|",
    ]
    why = {
        "渠道停用": "该渠道整体不再采集（口径不对或已腐化），存量一并移出",
        "排除:无主题词": "正文与标题都没命中任何主题词 → 判为与「独立开发」无关",
        "排除:标题": "标题命中排除词（招聘/转发/灌水等）",
        "排除:URL": "URL 形态命中排除规则（聚合页/榜单页等）",
    }
    for r, n in f["reasons"].most_common():
        L.append(f"| `{r}` | {n} | {why.get(r, '—')} |")
    L += ["", "## 语料归档 · 按渠道", "", "| 渠道 | 归档 |", "|---|---|"]
    for c, n in f["by_channel"].most_common():
        L.append(f"| `{c}` | {n} |")

    L += ["", "## 实体页为什么被归档", "",
          "判据（`kb_prune.py --archive-entities`）：**该页已标 `stale: true`"
          "（对应语料已不在库）且全库没有任何 wikilink 指向它**。",
          "换句话说：它既没有语料，也没有入口 —— 留着只会让人在 647 个项目里点进一个空页。",
          "",
          "> ⚠️ **口径声明**：下面的分类是**按 `project_url` 形态做的启发式分组**，"
          "**不是**当时的真实归档理由（真实理由只记了「stale 且无引用」，没有更细的标签）。",
          "> 它够用来「按形状找可能被判错的那批」，但**不要**把它当成判定依据引用。",
          "",
          "| 形态 | 个数 |", "|---|---|"]
    for cls, rows in sorted(f["ent_classes"].items(), key=lambda kv: -len(kv[1])):
        L.append(f"| {cls} | {len(rows)} |")

    L += ["", "## 抽样（每类前 8 个，看看有没有误杀）", ""]
    for cls, rows in sorted(f["ent_classes"].items(), key=lambda kv: -len(kv[1])):
        L.append(f"### {cls}（{len(rows)}）")
        for r in rows[:8]:
            L.append(f"- [[{r['stem']}|{r['title'][:64]}]]"
                     + (f" · {r['url'][:70]}" if r["url"] else ""))
        if len(rows) > 8:
            L.append(f"- …其余 {len(rows) - 8} 个见 `80-归档/项目/`")
        L.append("")

    L += ["## 捞回来（撤销）", "",
          "**实体页**（把归档的项目页搬回 `10-项目/`）：", "", "```bash"]
    for m in f["ent_manifests"]:
        L.append(f"python tools/kb_prune.py --undo-entities _meta/{m['name']}"
                 f"   # {m['n']} 个，{m['at'][:10]}")
    L += ["", "# 搬完必须过不变量（断链/计数）", "python tools/kb_healthcheck.py",
          "```", "", "**语料**（把归档的语料搬回 `20-语料/`）：", "", "```bash"]
    for m in f["manifests"]:
        L.append(f"python tools/kb_prune.py --undo _meta/{m['name']}"
                 f"   # {m['n']} 条，{m['at'][:10]}")
    L += ["", "python tools/kb_healthcheck.py", "```", "",
          "> `--undo` / `--undo-entities` 会**同时改回所有指向旧路径的链接**，"
          "所以撤销后不需要再手工修链。撤销是有账的：它读的就是当初搬迁时写的那份 manifest。",
          "",
          "## 只想捞**一个**条目怎么办",
          "",
          "不要把整份 manifest 撤销（那会把后来的判断一起回退）。做法：",
          "",
          "1. 在上面找到那个页面，记住文件名",
          "2. 手动把它搬回 `10-项目/`（或 `20-语料/posts/<渠道>/<日期>/`）",
          "3. 跑 `python tools/kb_healthcheck.py` —— 如果它原本被语料引用，"
          "断链数会告诉你还有哪几条链接没指回来",
          "",
          "## 出口",
          "",
          "- 归档是怎么产出的 → [[存量重判报告]] · [[实体页归档报告]]",
          "- 现在还该怎么判 → `_meta/rules.yaml`（主题准入规则）+ [[字段字典]]",
          "",
          f"_数据源：`80-归档/**/*.md` + `_meta/*manifest_*.json`｜生成器：`tools/kb_moc.py`｜{gen}_",
          ""]
    return "\n".join(L)


# ---------------------------------------------------------------- 报告总览

def _report_one(txt: str, name: str) -> str:
    """从一份报告里挖「它在讲什么」：优先 frontmatter title，否则第一个非空正文行。"""
    sp = split_note(txt)
    fm = fm_scalars(sp[0]) if sp else {}
    body = (sp[1] if sp else txt)
    line = ""
    for ln in body.splitlines():
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith(">") or s.startswith("---"):
            continue
        line = re.sub(r"^[-*]\s+", "", s)
        break
    line = re.sub(r"[*`\[\]]", "", line)
    line = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", line)
    return fm.get("title") or line[:80] or name


def render_reports() -> str:
    gen = iso(now_cst())
    rows = []
    for p in sorted(DIR_REPORT.glob("*.md")):
        if p.name == MAP_REPORTS.name:
            continue
        txt = p.read_text(encoding="utf-8")
        sp = split_note(txt)
        fm = fm_scalars(sp[0]) if sp else {}
        rows.append({"name": p.stem, "date": (fm.get("updated") or fm.get("generated_at")
                                              or "")[:16],
                     "what": _report_one(txt, p.stem),
                     "kind": fm.get("type") or "report"})
    rows.sort(key=lambda r: (r["date"] or "", r["name"]), reverse=True)

    L = [
        "---",
        "type: index",
        'title: "报告总览 · 每份报告在讲什么"',
        "tags:",
        "  - 索引",
        "  - 导航",
        "  - 报告",
        f'generated_at: "{gen}"',
        "aliases:",
        '  - "报告索引"',
        "---",
        "",
        f"# 报告总览 · `00-索引/报告/` 的 {len(rows)} 份",
        "",
        HEAD,
        "",
        "## 为什么需要这一页",
        "",
        "报告文件名是 `洞察-20260920`、`内容审计-all`、`分析-20260920T025555` 这种 —— "
        "**光看名字判断不出里面讲了什么**（信息气味不足，NN/g 的三大 IA 错误之一）。",
        "本页给每份报告补一句「它在讲什么」，让你**点开之前**就知道要不要点。",
        "",
        "## 按需选读（不是每份都要看）",
        "",
        "| 你的问题 | 读哪份 |",
        "|---|---|",
        "| 现在什么在变热 / 赛道分布 | `洞察-*`（最新那份） |",
        "| 语料质量从多少治到多少 | `修复报告-*` |",
        "| 哪个渠道取不到数 | [[渠道台账]] · `分析-*` |",
        "| 内容本身有没有问题（相关性/完整性/重复） | `内容审计-*` |",
        "| 缺正文、还没补上的清单 | [[回填队列]] |",
        "| 我判废了什么、怎么捞回 | [[归档与申诉]] |",
        "",
        f"## 全部 {len(rows)} 份",
        "",
        "| 报告 | 在讲什么 | 时间 |",
        "|---|---|---|",
    ]
    for r in rows:
        what = r["what"].replace("|", "/")[:96]
        L.append(f"| [[{r['name']}]] | {what} | {r['date'].replace('T', ' ') or '—'} |")

    L += ["", "## 出口", "",
          "- 最新结论 → [[从这里开始]]（首屏「想干什么」表的第一行）",
          "- 库整体结构 → [[Home]]",
          "",
          f"_数据源：`00-索引/报告/*.md` 的 frontmatter 与首行结论｜生成器：`tools/kb_moc.py`｜{gen}_",
          ""]
    return "\n".join(L)


# ---------------------------------------------------------------- main

def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="只打印，不写盘")
    ap.add_argument("--only", default="", choices=["", "projects", "archive", "reports"])
    args = ap.parse_args(argv)

    targets = [args.only] if args.only else ["projects", "archive", "reports"]
    for t in targets:
        if t == "projects":
            pages, items, n_stale = project_rows()
            md, out = render_projects(pages, items, n_stale), MAP_PROJECTS
            linked = sum(1 for r in pages.values() if r["n"])
            stat = (f"页面 {len(pages)} · 关联语料 {linked} · "
                    f"未关联 {len(pages) - linked} · 跳过stale {n_stale}")
        elif t == "archive":
            md, out = render_archive(), MAP_ARCHIVE
            f = _archive_facts()
            stat = f"归档语料 {f['n_arch_posts']} · 归档实体页 {f['n_arch_proj']}"
        else:
            md, out = render_reports(), MAP_REPORTS
            stat = f"{sum(1 for ln in md.splitlines() if ln.startswith('| [['))} 份报告"
        if args.dry:
            print(f"===== {out.relative_to(ROOT).as_posix()} ({stat}) =====")
            print(md[:1500])
            print("…")
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8", newline="\n")
            print(f"[地图] {out.relative_to(ROOT).as_posix()}  {stat}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
