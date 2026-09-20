"""kb_collect — 独立开发项目知识库 · 采集管线（零第三方依赖）。

一次运行 = 读 _meta/channels.yaml → 逐渠道取数（独立容错）→ 补全正文/评论
          → 去重 → 双写（原始 JSONL + Obsidian note）→ 更新项目页/渠道页 → 运行记录

渠道 adapter / 评论与正文 enricher / project_url 守卫在 `kbc_channels.py`（本文件 re-export，
既有调用点 `from kb_collect import X` 不受影响）；注册表解析在 `kb_common.load_registry`。

用法：
  python tools/kb_collect.py                      # 全渠道
  python tools/kb_collect.py --channels hn_show,v2ex
  python tools/kb_collect.py --dry                # 只取数不写盘（看渠道健康）
  python tools/kb_collect.py --max-total 300      # 总量上限
  python tools/kb_collect.py --force-weekly       # 强制跑 weekly_only 渠道
  python tools/kb_collect.py --since 2026-07-01   # 显式窗口：窗口前推到该日 + 按 published_at 裁剪
  python tools/kb_collect.py --until 2026-07-31   # 显式窗口上界（含当日）
  python tools/kb_collect.py --throttle-ms 50     # 评论抓取节流（默认 25ms/请求）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_common import (BODY_MIN, CST, DIR_CHANNELS, DIR_CORPUS, DIR_METHOD, DIR_PEOPLE,  # noqa: E402
                       DIR_PROJECTS, DIR_RAW, META, BodyCache, FetchError, RunLog, Seen,
                       append_jsonl, body_completeness, ensure_dirs, is_project_ish, iso,
                       load_channels_yaml, load_registry, norm_url, now_cst, sanitize_record,
                       sha1, slugify, topic_of, write_note)
from kbc_channels import (ACCOUNT_URL_RE, ADAPTERS, ENRICH_ROUTING, FULLTEXT_BUDGET,  # noqa: E402,F401
                          LINK_RE, MAX_COMMENTS, PERSON_HANDLE_RE, as_tags, detect_lang,  # noqa: E402,F401
                          derive_project_url, enrich_generic, excerpt, filter_published,  # noqa: E402,F401
                          lead_sentence, make_item, project_url_reject, readable_body,  # noqa: E402,F401
                          strip_html)  # noqa: E402,F401  ↑ re-export：9 个工具从本模块 import 这些名字

__all__ = ["load_rules", "apply_rules", "main"]


# ---------------------------------------------------------------- 准入规则

def load_rules(path: Path | None = None) -> dict:
    """读 _meta/rules.yaml（主题层准入规则）。文件不存在 → 不设限，并打印一次提示。"""
    p = path or (META / "rules.yaml")
    if not p.exists():
        print(f"    [w] 未找到 {p.name}，跳过主题准入过滤", flush=True)
        return {}
    try:
        return load_channels_yaml(p)
    except Exception as e:                                         # noqa: BLE001
        print(f"    [w] rules.yaml 解析失败：{str(e)[:80]}，跳过过滤", flush=True)
        return {}


def apply_rules(items: list[dict], ch: dict, rules: dict,
                stage: str = "both", sink: list | None = None) -> tuple[list[dict], dict]:
    """主题层准入：全局 + 渠道级 排除/必需 正则。返回 (保留项, 统计)。

    规则只作用在「标题 / URL / 正文」，不做语义判断 —— 语义判断交给渠道门禁与内容审计。
    命中 `exclude_*` 直接丢；设了 `require_any` 但一条都不命中，也丢。

    分两段执行是有意的：
      stage="pre"  → 只跑 exclude（标题/URL 一定已有），**在 enrich 之前**跑，省 fulltext 预算；
      stage="post" → 只跑 require_any（需要正文才算得准），在 enrich 之后跑。
    一次跑完（"both"）只在对正文无依赖时才对。

    `sink` 非空时，被丢弃的条目会记进 `_meta/rule_drops.jsonl`（标题/URL/命中原因）——
    规则是硬丢，没有账本就无法回溯「是不是误杀」，也无从调参。
    """
    if not rules:
        return items, {}
    cr = (rules.get("channels") or {}).get(ch["id"]) or {}

    def compile_all(*keys) -> list[re.Pattern]:
        out = []
        for src, key in [(rules, keys[0]), (cr, keys[1] if len(keys) > 1 else keys[0])]:
            for pat in (src.get(key) or []):
                try:
                    out.append(re.compile(str(pat), re.I))
                except re.error as e:
                    # 静默吞掉坏正则 = 规则看着在、其实没生效（违反「不许静默降级」）。
                    # 实测踩过：写错的 pattern 让整条过滤形同虚设，直到看账本才发现。
                    print(f"    [!] 规则正则无效，已跳过：{pat!r}（{e}）", flush=True)
        return out

    ex_title = compile_all("exclude_title") if stage in ("both", "pre") else []
    ex_url = compile_all("exclude_url") if stage in ("both", "pre") else []
    req = []
    if stage in ("both", "post"):
        for pat in (cr.get("require_any") or []):
            try:
                req.append(re.compile(str(pat), re.I))
            except re.error as e:
                print(f"    [!] require_any 正则无效，已跳过：{pat!r}（{e}）", flush=True)

    kept: list[dict] = []
    stat: dict[str, int] = {}

    def bump(k: str) -> None:
        stat[k] = stat.get(k, 0) + 1

    def drop(it: dict, why: str) -> None:
        bump(why)
        if sink is not None:
            sink.append({"source": ch["id"], "reason": why, "stage": stage,
                         "item_id": it.get("item_id"), "title": it.get("title"),
                         "url": it.get("url"), "at": iso(now_cst())})

    for it in items:
        title = it.get("title") or ""
        url = f"{it.get('url') or ''} {it.get('project_url') or ''}"
        # `match: title` 的渠道只拿标题做 require_any 判定。
        # 为什么：话题榜（HN 首页 / Lobsters）的长正文里几乎必然出现 launch / startup / customer
        # 之类的词 —— 那是**顺带提到**，不是「这篇在讲自己的产品」。正文一并参与匹配会让
        # require_any 形同虚设（实测 hn_front 库里仍留着 "How to Write with an LLM" 这类随笔）。
        text = title if (cr.get("match") or "") == "title" else f"{title}\n{it.get('body') or ''}"
        if any(p.search(title) for p in ex_title):
            drop(it, "排除:标题")
            continue
        if any(p.search(url) for p in ex_url):
            drop(it, "排除:URL")
            continue
        if req and not any(p.search(text) for p in req):
            drop(it, "排除:无主题词")
            continue
        kept.append(it)
    return kept, stat


# ============================================================ writers

METRIC_LABELS = {"points": "点赞", "comments": "评论", "stars": "stars", "forks": "forks",
                 "score": "得分", "reactions": "reactions", "play": "播放", "replies": "回复",
                 "upvote_ratio": "赞踩比", "rank": "榜单排名", "danmaku": "弹幕", "favorites": "收藏"}


def metrics_line(m: dict) -> str:
    bits = [f"{METRIC_LABELS.get(k, k)}={v}" for k, v in (m or {}).items() if v is not None]
    return " · ".join(bits) or "—"


def corpus_note_path(it: dict, day: str) -> Path:
    return DIR_CORPUS / "posts" / it["source_id"] / day / f"{it['item_id']}_{slugify(it['title'], 50)}.md"


def _wikilink(p: Path, root: Path | None = None) -> str:
    """把 note 路径转成 Obsidian wikilink 目标（相对 vault 根、去扩展名、正斜杠）。"""
    r = (root or (Path(__file__).resolve().parents[1]))
    try:
        rel = p.relative_to(r)
    except ValueError:
        rel = p
    return rel.as_posix()[:-3] if rel.as_posix().endswith(".md") else rel.as_posix()


def nav_block(it: dict) -> list[str]:
    """语料页的「导航」段 —— 修「语料页是死胡同」这个结构缺陷。

    为什么必须有：实测 711 条语料 note **一条 wikilink 都没有**，
    只有项目页单向指向语料页。于是从一条语料出发哪儿都去不了 ——
    想看「同渠道还有什么」「这个作者还做过什么」「它属于哪个赛道」，
    只能回到文件树里手动翻，这正是「各个维度在不同文件夹反复切换」的直接来源。

    注意分工：这里只挂**身份链接**（项目页/人物页/渠道页/赛道视图）。
    「同渠道还有哪些」「同赛道还有哪些」这类**集合查询**不在这里展开 ——
    那是查询层的职责（Bases 视图 / MOC 页），写进每条 note 会既冗余又必然过期。

    **实体页链接必须与 `is_project_ish()` 同判据**：不是项目的条目（讨论帖、提问帖）
    本来就不该有项目页，若这里仍无条件输出链接，就会指向不存在的页 —— 实测这样
    一次性制造过上千条死链。宁可不出链，也不出死链。
    """
    out = ["## 导航", ""]
    # 项目页 / 人物页：路径可确定性推导，且采集端**总会**把它建出来 → 链接不会死。
    # 方法论页不同：40-方法论 是人工/LLM 提炼区，页**不自动生成** —— 无条件出链
    # 就是指向不存在的页（实测 navfix 重写导航后冒出 2 条死链）。宁可不出链，也不出死链。
    try:
        if it.get("kind") == "person":
            out.append(f"- 人物页：[[{_wikilink(person_note_path(it))}]]")
        elif it.get("kind") == "method":
            mp = method_note_path(it)
            if mp.exists():
                out.append(f"- 方法论页：[[{_wikilink(mp)}]]")
            else:
                out.append("- 方法论页：—（待提炼，方法见 `40-方法论/方法论页说明`）")
        elif is_project_ish(it):
            out.append(f"- 项目页：[[{_wikilink(project_note_path(it))}]]")
        else:
            out.append("- 项目页：—（本条不是项目，按设计不建实体页）")
    except Exception:                                              # noqa: BLE001
        pass
    out.append(f"- 渠道页：[[50-渠道/{it['source_id']}]]")
    out.append(f"- 赛道：`{topic_of(it)}`（见 [[浏览]] 的「按赛道」视图）")
    out += [f"- 同渠道/同赛道批量浏览：[[浏览]]", ""]
    return out


def write_corpus_note(it: dict, day: str) -> Path:
    p = corpus_note_path(it, day)
    comments = it.get("comments") or []
    body = it.get("body") or ""
    fm = {
        "type": "corpus",
        "item_id": it["item_id"],
        "title": it["title"],
        "source": it["source_id"],
        "source_name": it["source_name"],
        "url": it["url"],
        "project_url": it.get("project_url"),
        "author": it.get("author"),
        "published_at": it.get("published_at"),
        "captured_at": it["captured_at"],
        "lang": it["lang"],
        "kind": it["kind"],
        "topic": topic_of(it),
        # shard/pub_day 是**给 Bases 分组用的纯字符串日字段**：
        # Bases 的 groupBy 支持字符串属性最稳；直接对 ISO 时间串分组会一个时间戳一组（等于没分）。
        # 采到 shard（入库日）和 pub_day（发布日）两个维度，时间轴浏览就不用靠猜。
        "shard": day,
        "pub_day": (it.get("published_at") or "")[:10] or None,
        "tags": ["语料", it["source_id"]] + (it.get("tags") or [])[:6],
        "metrics": {k: v for k, v in (it.get("metrics") or {}).items() if v is not None},
        "comments_count": len(comments),
        "comments_total": it.get("comments_total"),
        "comments_truncated": it.get("comments_truncated") or None,
        "discovered_via": it.get("discovered_via"),
    }
    lead = lead_sentence(body)
    parts = [f"# {it['title']}", ""]
    if lead:
        parts += ["> [!info] 一句话导读", f"> {lead}", ""]
    # 元数据收进**折叠 callout**（`[!meta]-` 默认收起）：正文才是主角，元数据备查。
    # 展开一次能看到全部出处信息，但默认态把首屏留给正文 —— 可读性主诉求。
    pu = it.get("project_url")
    parts += [
        "> [!meta]- 语料信息（点开展开）",
        f"> 来源：{it['source_name']}（{it['kind']}）",
        f"> 原帖：<{it['url']}>",
        f"> 指标：{metrics_line(it.get('metrics') or {})}",
        f"> 作者：{it.get('author') or '—'}　|　发布：{it.get('published_at') or '—'}",
        f"> 项目链接：<{pu}>" if pu else "> 项目链接：—",
        f"> 采集：{it['captured_at']}　|　id：`{it['item_id']}`",
        "",
    ]
    if body:
        parts += ["## 正文", "", readable_body(body), ""]
    if comments:
        parts += [f"## 评论（{len(comments)}/{it.get('comments_total')}"
                  f"{'，已截断' if it.get('comments_truncated') else ''}）", ""]
        for c in comments:
            head = (f"**{c.get('author') or '匿名'}**"
                    f"{f'（{c.get("score")} 分）' if c.get('score') is not None else ''}"
                    f"{f' · {c.get("created_at")}' if c.get('created_at') else ''}")
            text = readable_body((c.get("text") or "").strip())
            blines = [f"> {ln}".rstrip() for ln in text.splitlines()] if text else []
            parts += [f"> {head}　"] + blines + ["", "---", ""]
        parts = parts[:-2]                                 # 最后一条评论后不留分隔线
    # 用**最终 body** 重算外链（构造期的 it["links"] 多半为空 —— 发布站正文由 enrich 后补）
    links = sorted(set(LINK_RE.findall(f"{body} ")))[:30]
    links = [u for u in links if u not in (it["url"], it.get("project_url"))][:25]
    if links:
        parts += ["## 关联链接", ""] + [f"- {u}" for u in links] + [""]
    parts += nav_block(it)
    write_note(p, fm, "\n".join(parts))
    return p


def project_note_path(it: dict) -> Path:
    key = it.get("project_url") or it["url"]
    name = it["title"]
    if it["kind"] == "project":
        pass
    elif it.get("project_url"):
        name = re.sub(r"^https?://", "", it["project_url"]).split("/")[0]
    return DIR_PROJECTS / f"{slugify(name, 48)}_{sha1(norm_url(key), 8)}.md"


def person_note_path(it: dict) -> Path:
    handle = it.get("author") or re.sub(r"^https?://", "", it["url"]).split("/")[0]
    name = re.sub(r"\s*\(@[^)]+\)\s*", "", it["title"]).strip() or handle
    return DIR_PEOPLE / f"{slugify(name, 40)}_{sha1(norm_url(it['url']), 8)}.md"


def method_note_path(it: dict) -> Path:
    """方法论页路径（40-方法论/）：按标题 slug + **kind-salted** url 指纹 8。

    与 person_note_path 同构 —— 方法论沉淀按条目本身归一，不像项目页那样以
    project_url 为主键（复盘文章往往没有 project_url，即使有也只是文章里的示例产品）。

    为什么给 url 加 `#method` 盐：同一 URL 既是项目（有 project_url）又被归档为方法论时
    （exa_discovery 的独立开发者收入复盘），项目/方法论会撞名（实测 Tony-Dinh 一例）。
    加盐后 hash 按 kind 隔离，跨 kind 不再冲突。person 页同理但暂没人踩过 —— 不改，等真的
    漂了再补盐。
    """
    return DIR_METHOD / f"{slugify(it['title'], 40)}_{sha1(norm_url(it['url']) + '#method', 8)}.md"


def _obs_rows(p: Path) -> list[str]:
    """读实体页「观测历史」表的数据行（不读表头）。页不存在或表缺失 → []。"""
    if not p.exists():
        return []
    m = re.search(r"## 观测历史\n\n(.*?)(\n## |\Z)", p.read_text(encoding="utf-8"), re.S)
    if not m:
        return []
    return [ln for ln in m.group(1).strip().splitlines() if ln.startswith("|")][2:]


def _obs_row(it: dict, corpus_rel: str | None) -> str:
    return (f"| {it['captured_at']} | {it['source_name']} | {metrics_line(it.get('metrics') or {})} "
            f"| {('[[{}]]'.format(corpus_rel[:-3]) if corpus_rel else '—')} |")


def write_person_note(it: dict, corpus_rel: str | None,
                      touch_obs: bool = True,
                      obs_override: list[str] | None = None) -> Path:
    """人物页（独立开发大牛）：与项目页同构，但落在 30-人物/，供"学方法论"路线的调研消费。"""
    p = person_note_path(it)
    if obs_override is not None:
        obs = list(obs_override)
    else:
        obs = _obs_rows(p)
        row = _obs_row(it, corpus_rel)
        obs = [ln for ln in obs if not ln.startswith(f"| {it['captured_at']} |")]
        if touch_obs:
            obs = (obs + [row])[-60:]
    lead = lead_sentence(it.get("body") or "")
    body = [f"# {it['title']}", ""]
    if lead:
        body += ["> [!info] 一句话导读", f"> {lead}", ""]
    body += [
        "> [!meta]- 人物信息（点开展开）",
        f"> 主页：<{it.get('author_url') or it['url']}>",
        f"> handle：{it.get('author') or '—'}",
        f"> 首次收录：{it['captured_at']}",
        f"> 来源渠道：{it['source_name']}",
        f"> 所属分区：{(it.get('extra') or {}).get('section') or '—'}",
        f"> 标签：{', '.join((it.get('tags') or [])[:8]) or '—'}",
        "",
        "## 观测历史",
        "",
        "| 采集时间 | 渠道 | 指标 | 语料 |", "|---|---|---|---|", *obs, "",
    ]
    if it.get("body"):
        body += ["## 摘要正文", "", excerpt(readable_body(it["body"]), 1200), ""]
    fm = {"type": "person", "title": it["title"], "handle": it.get("author"),
          "profile_url": it.get("author_url") or it["url"], "first_seen": it["captured_at"],
          "sources": [it["source_id"]], "tags": ["人物", it["source_id"]] + (it.get("tags") or [])[:6],
          "lang": it["lang"]}
    write_note(p, fm, "\n".join(body))
    return p


def write_method_note(it: dict, corpus_rel: str | None,
                      touch_obs: bool = True,
                      obs_override: list[str] | None = None) -> Path:
    """方法论页（40-方法论/）：build-in-public 复盘、收入报告、增长路径等经验贴。

    与项目页同构（观测历史表 + 摘要正文），但**语义**不同：项目页记录一个产品的
    时间演化，方法论页记录一篇经验贴被再次观测到的时点。二者混用会让「按项目看演化」
    与「按方法学经验」两条路线互相污染 —— 这也是为什么实体页分发必须先按 kind 短路。
    """
    p = method_note_path(it)
    if obs_override is not None:
        obs = list(obs_override)
    else:
        obs = _obs_rows(p)
        row = _obs_row(it, corpus_rel)
        obs = [ln for ln in obs if not ln.startswith(f"| {it['captured_at']} |")]
        if touch_obs:
            obs = (obs + [row])[-60:]
    lead = lead_sentence(it.get("body") or "")
    body = [f"# {it['title']}", ""]
    if lead:
        body += ["> [!info] 一句话导读", f"> {lead}", ""]
    body += [
        "> [!meta]- 文章信息（点开展开）",
        f"> 原帖：<{it['url']}>",
        f"> 作者：{it.get('author') or '—'}",
        f"> 首次收录：{it['captured_at']}",
        f"> 来源渠道：{it['source_name']}",
        f"> 标签：{', '.join((it.get('tags') or [])[:8]) or '—'}",
        "",
        "## 观测历史",
        "",
        "| 采集时间 | 渠道 | 指标 | 语料 |", "|---|---|---|---|", *obs, "",
    ]
    if it.get("body"):
        body += ["## 摘要正文", "", excerpt(readable_body(it["body"]), 1200), ""]
    fm = {"type": "method", "title": it["title"], "url": it["url"],
          "author": it.get("author"), "first_seen": it["captured_at"],
          "sources": [it["source_id"]],
          "tags": ["方法论", it["source_id"]] + (it.get("tags") or [])[:6],
          "lang": it["lang"]}
    write_note(p, fm, "\n".join(body))
    return p


def write_entity_note(it: dict, corpus_rel: str | None,
                      touch_obs: bool = True,
                      obs_override: list[str] | None = None) -> Path:
    """按 kind 分发实体页：person → 30-人物/，method → 40-方法论/，其余 → 10-项目/。

    分发判据与 `is_project_ish` 一致（kind 是语义，优先于其他证据）。
    touch_obs / obs_override 透传给三个写页函数（批量重渲染用 obs_override 整体重建观测历史）。
    """
    kind = (it.get("kind") or "").lower()
    if kind == "person":
        return write_person_note(it, corpus_rel, touch_obs=touch_obs, obs_override=obs_override)
    if kind == "method":
        return write_method_note(it, corpus_rel, touch_obs=touch_obs, obs_override=obs_override)
    return write_project_note(it, corpus_rel, touch_obs=touch_obs, obs_override=obs_override)


def write_project_note(it: dict, corpus_rel: str | None,
                       extra_obs: list[str] | None = None,
                       touch_obs: bool = True,
                       obs_override: list[str] | None = None) -> Path:
    p = project_note_path(it)
    if obs_override is not None:
        # 批量重渲染（kb_render）：观测历史**整体以 raw 重建结果为准**，
        # 不读旧页残行（旧页可能带着 reclassify 前的陈旧链接），也不追加本条。
        obs = list(obs_override)
    else:
        obs = _obs_rows(p)
        row = _obs_row(it, corpus_rel)
        obs = [ln for ln in obs if not ln.startswith(f"| {it['captured_at']} |")]  # 同刻重跑不重复记账
        if extra_obs:
            have = {ln.split("|")[1].strip() for ln in obs + [row]}
            obs += [ln for ln in extra_obs if ln.split("|")[1].strip() not in have]
        # touch_obs=False：批量重渲染（kb_render）时**只刷模板、不记观测行** ——
        # 否则 700+ 条语料重放会给项目页灌进同一天的 refresh 噪音行（观测历史只记真采集）。
        if touch_obs:
            obs = (obs + [row])[-60:]
    obs.sort(key=lambda ln: ln.split("|")[1].strip())
    lead = lead_sentence(it.get("body") or "")
    body = [f"# {it['title']}", ""]
    if lead:
        body += [f"> [!info] 一句话导读", f"> {lead}", ""]
    body += [
        "> [!meta]- 项目信息（点开展开）",
        f"> 项目链接：<{it.get('project_url') or it['url']}>",
        f"> 首次收录：{it['captured_at']}",
        f"> 来源渠道：{it['source_name']}",
        f"> 标签：{', '.join((it.get('tags') or [])[:8]) or '—'}",
        f"> 最新指标：{metrics_line(it.get('metrics') or {})}",
        "",
        "## 观测历史",
        "",
        "| 采集时间 | 渠道 | 指标 | 语料 |", "|---|---|---|---|", *obs, "",
    ]
    if it.get("body"):
        body += ["## 摘要正文", "", excerpt(readable_body(it["body"]), 1200), ""]
    fm = {"type": "project", "title": it["title"], "project_url": it.get("project_url") or it["url"],
          "first_seen": it["captured_at"], "sources": [it["source_id"]],
          "tags": ["项目", it["source_id"]] + (it.get("tags") or [])[:6], "lang": it["lang"]}
    write_note(p, fm, "\n".join(body))
    return p


def write_channel_note(ch: dict, rec: dict, run_id: str) -> None:
    p = DIR_CHANNELS / f"{ch['id']}.md"
    hist = []
    if p.exists():
        m = re.search(r"## 运行历史\n\n(.*?)(\n## |\Z)", p.read_text(encoding="utf-8"), re.S)
        if m:
            hist = [ln for ln in m.group(1).strip().splitlines() if ln.startswith("|")][2:]
    hist = (hist + [f"| {rec['started']} | {rec['status']} | {rec['count']} | {rec['elapsed_s']}s "
                    f"| {rec['message'][:70]} |"])[-40:]
    fm = {"type": "channel", "channel_id": ch["id"], "name": ch["name"], "group": ch.get("group"),
          "adapter": ch.get("adapter"), "auth": ch.get("auth"), "lang": ch.get("lang"),
          "status": rec["status"], "last_verified": rec["started"][:10],
          "tags": ["渠道", f"渠道/{ch.get('group') or '未分组'}"], "params": ch.get("params") or {}}
    body = [
        f"# {ch['name']}（`{ch['id']}`）", "",
        f"- **分组**：{ch.get('group')}　|　**语言**：{ch.get('lang')}　|　**认证**：{ch.get('auth')}",
        f"- **取数实现**：`{ch.get('adapter')}`　|　**单次上限**：{ch.get('limit')}",
        f"- **补全类型**：{ch.get('enrich')}",
        f"- **当前状态**：`{rec['status']}`（本次 {rec['count']} 条，{rec['elapsed_s']}s）",
        f"- **口径备注**：{ch.get('note') or '—'}",
        f"- **解锁方式**：{ch.get('unlock') or '—'}", "",
        "## 运行历史", "",
        "| 时间 | 状态 | 条数 | 耗时 | 消息 |", "|---|---|---|---|---|", *hist, "",
    ]
    write_note(p, fm, "\n".join(body))


# ============================================================ pipeline

def _day_bound(s: str, end: bool = False) -> int:
    """`--since/--until` 的日期参数 → epoch 秒（CST）。纯日期时 until 取当日 23:59:59（含当日）。"""
    dt = datetime.fromisoformat(s.strip())
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=CST)
    if end and len(s.strip()) <= 10:
        dt = dt + timedelta(days=1) - timedelta(seconds=1)
    return int(dt.timestamp())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channels", default="", help="逗号分隔渠道 id；默认全渠道")
    ap.add_argument("--dry", action="store_true", help="只取数不写盘")
    ap.add_argument("--max-total", type=int, default=0)
    ap.add_argument("--max-comments", type=int, default=MAX_COMMENTS)
    ap.add_argument("--fulltext-budget", type=int, default=FULLTEXT_BUDGET)
    ap.add_argument("--force-weekly", action="store_true")
    ap.add_argument("--days", type=int, default=0, help="覆盖渠道 window_days")
    ap.add_argument("--limit-mult", type=int, default=1,
                    help="按倍数放大各渠道 limit（历史铺底用；上限 1000）")
    ap.add_argument("--slice-days", type=int, default=0,
                    help="把取数窗口按 N 天切片逐片查（仅对分页型 adapter 生效，如 reddit）")
    ap.add_argument("--no-enrich", action="store_true",
                    help="跳过评论/正文补全（历史铺底先只落索引，正文交给 kb_backfill）")
    ap.add_argument("--no-rules", action="store_true", help="跳过主题准入过滤（调试用）")
    ap.add_argument("--since", default="",
                    help="显式窗口下界 YYYY-MM-DD：把各渠道窗口**前推**到该日，并按 published_at 裁剪")
    ap.add_argument("--until", default="",
                    help="显式窗口上界 YYYY-MM-DD（含当日）：按 published_at 裁剪")
    ap.add_argument("--throttle-ms", type=int, default=25,
                    help="评论抓取节流（毫秒/请求；0=关闭。对上游 API 的礼貌下限）")
    args = ap.parse_args(argv)

    since_ts = _day_bound(args.since) if args.since else None
    until_ts = _day_bound(args.until, end=True) if args.until else None

    ensure_dirs()
    reg = load_registry()
    rules = {} if args.no_rules else load_rules()
    chans = reg["_enabled_channels"]
    if args.channels:
        want = {c.strip() for c in args.channels.split(",") if c.strip()}
        chans = [c for c in chans if c["id"] in want]
    if not args.force_weekly and now_cst().weekday() != 0:
        chans = [c for c in chans if not (c.get("params") or {}).get("weekly_only")]

    run_id = now_cst().strftime("%Y%m%dT%H%M%S")
    log = RunLog(run_id)
    # 静默失效防护：ENRICH_ROUTING / ADAPTERS 的键写错（如用 adapter 名而非渠道 id）必须报出来
    all_ids = {c["id"] for c in reg["_enabled_channels"]} | {c["id"] for c in (reg.get("disabled") or [])}
    bad_enr = [k for k in ENRICH_ROUTING if k not in all_ids]
    bad_ad = [c["id"] for c in reg["_enabled_channels"] if (c.get("adapter") or "") not in ADAPTERS]
    if bad_enr or bad_ad:
        print(f"[!] 注册表自检失败：未匹配的 enrich 路由 {bad_enr}；未知 adapter 的渠道 {bad_ad}", flush=True)
    seen = Seen()
    body_cache = BodyCache()
    drop_sink: list[dict] = []          # 主题准入丢弃账本（可回溯误杀，供规则调参）
    ctx = {"max_comments": args.max_comments, "fulltext_budget": args.fulltext_budget,
           "slice_days": args.slice_days, "throttle_ms": args.throttle_ms,
           "since_ts": since_ts, "until_ts": until_ts}
    day = now_cst().strftime("%Y-%m-%d")
    total_items = total_new = write_errors = 0
    print(f"=== KB 采集 {run_id} · {len(chans)} 渠道 ===", flush=True)

    for ch in chans:
        t0 = time.time()
        adapter = ADAPTERS.get(ch.get("adapter") or "")
        if not adapter:
            log.channel(ch["id"], ch["name"], "error", 0, f"未知 adapter={ch.get('adapter')}", time.time() - t0)
            continue
        c = dict(ch)
        p = dict(c.get("params") or {})
        if args.days:
            p["window_days"] = args.days
        if since_ts:
            # --since 兼做窗口前推：窗口不够老就取不到那天的数据，裁剪等于空转
            need = max(1, (now_cst() - datetime.fromtimestamp(since_ts, tz=CST)).days + 1)
            p["window_days"] = max(int(p.get("window_days") or 0) or need, need)
        c["params"] = p
        if args.limit_mult > 1:
            c["limit"] = min(1000, int(c.get("limit") or 30) * args.limit_mult)
        try:
            items, status, msg = adapter(c, ctx)
        except FetchError as e:
            log.channel(ch["id"], ch["name"], "error", 0, f"{e.status} {e.msg}", time.time() - t0)
            log.error(ch["id"], e)
            continue
        except Exception as e:                                     # noqa: BLE001
            log.channel(ch["id"], ch["name"], "error", 0, str(e)[:120], time.time() - t0)
            log.error(ch["id"], e)
            continue

        # 显式窗口（--since/--until）：按 published_at 裁剪。放在规则过滤之前 —— 便宜且省预算。
        if since_ts or until_ts:
            n0 = len(items)
            items, _dropped_pub = filter_published(items, since_ts, until_ts)
            if n0 != len(items):
                print(f"    [窗口] {ch['id']}: {n0}→{len(items)}（published_at 裁剪）", flush=True)

        # 主题准入 · 第一段：排除规则。放在 enrich 之前，省下会被丢掉条目的 fulltext 预算。
        raw_n = len(items)
        items, rstat = apply_rules(items, ch, rules, stage="pre", sink=drop_sink)
        if rstat:
            print(f"    [过滤] {ch['id']}: {raw_n}→{len(items)} " +
                  " ".join(f"{k}={v}" for k, v in sorted(rstat.items())), flush=True)

        enr = ENRICH_ROUTING.get(ch["id"])
        if enr and items and status == "ok" and not args.no_enrich:
            try:
                enr[1](items, ctx)
            except Exception as e:                                 # noqa: BLE001
                log.error(f"{ch['id']}.enrich[{enr[0]}]", e)
        if (ch.get("enrich") == "fulltext" or ch.get("enrich_extra") == "fulltext") \
                and not args.no_enrich:
            if items:
                ch_ctx = dict(ctx)
                if ch.get("fulltext_budget"):
                    ch_ctx["fulltext_budget"] = int(ch["fulltext_budget"])
                try:
                    enrich_generic(items, ch_ctx)
                except Exception as e:                             # noqa: BLE001
                    log.error(f"{ch['id']}.fulltext", e)

        # 主题准入 · 第二段：require_any（此时正文已尽量取全，判定才准）。
        if items:
            before = len(items)
            items, rstat2 = apply_rules(items, ch, rules, stage="post", sink=drop_sink)
            if rstat2:
                print(f"    [过滤] {ch['id']} 主题词: {before}→{len(items)} " +
                      " ".join(f"{k}={v}" for k, v in sorted(rstat2.items())), flush=True)

        # 去重（运行内）+ 正文继承 + new/update/refresh 判定
        uniq = {}
        for it in items:
            uniq.setdefault(it["item_id"], it)
        items = list(uniq.values())

        # 正文继承（R3 修的坑）：本轮回榜但取数失败时，绝不用空 body 覆盖历史已取到的正文。
        # 否则 rolling window 会把上一轮 / kb_backfill 回填的正文反复抹掉。
        carried, pu_carried = 0, 0
        for it in items:
            ex = it.setdefault("extra", {})
            body = it.get("body") or ""
            # project_url 继承（R4 修的坑）：它是项目页**文件名 hash 的组成部分**。
            # 而它靠「正文里第一个非同源外链」回退推导 —— 本轮正文取不到就会退化成 None，
            # key 一变就新建项目页、把上一轮那页留成孤儿（实测 20 条）。故与正文同策：只增不减。
            prev_pu = (seen.get(it["item_id"]) or {}).get("project_url")
            if not it.get("project_url") and prev_pu:
                it["project_url"] = prev_pu
                ex["project_url_carried"] = True
                pu_carried += 1
            if len(body) >= BODY_MIN:
                # 正文已达标就清掉历史错误标记，否则会长期误报（body 从 exa/缓存补齐后标记还挂着）
                ex.pop("body_error", None)
                body_cache.put(it["item_id"], body, ex.get("body_source") or ch["id"],
                               ex.get("body_url") or it.get("url") or "",
                               it.get("body_format") or "markdown")
            else:
                hit = body_cache.get(it["item_id"])
                if hit and len(hit.get("body") or "") >= BODY_MIN:
                    it["body"] = hit["body"]
                    it["body_format"] = hit.get("body_format") or "markdown"
                    ex["body_source"] = f"cache:{hit.get('source') or '?'}"
                    ex["body_cached_at"] = hit.get("at")
                    ex.pop("body_error", None)                 # 最终正文达标 → 不再报错
                    carried += 1
        if carried or pu_carried:
            print(f"    [i] 继承：正文 {carried} 条 · project_url {pu_carried} 条（防空洞覆盖/防孤儿页）",
                  flush=True)

        # 派生字段：正文完整度 + 分层 + project_url 二次推导。
        # 下游（分析/审计/LLM）必须能一眼区分「这是全文」与「这只是开头」，
        # 否则会把 RSS 摘要当成原文做深度分析。
        layer = ch.get("layer") or ("signal" if (ch.get("profile") or "") == "metadata" else "corpus")
        pu_derived = 0
        for it in items:
            ex = it.setdefault("extra", {})
            ex["layer"] = layer
            # 写盘前清洗文本字段（U+2028 类行分隔符 → \n）：raw 与语料页用的是
            # 同一个 it，所以必须在两者**之前**做，否则 raw 干净、页面带地雷。
            sanitize_record(it)
            it["body_completeness"] = body_completeness(it.get("body"), ex, layer)
            # project_url 二次推导：构造 make_item 时正文还没补，这里正文已尽可能取全。
            if not it.get("project_url"):
                got = derive_project_url(it.get("url") or "", it.get("body") or "")
                if got:
                    it["project_url"] = norm_url(got)
                    ex["project_url_derived"] = "post_enrich"
                    pu_derived += 1
        if pu_derived:
            print(f"    [i] project_url 补推 {pu_derived} 条（正文补全后才可推导）", flush=True)

        for it in items:
            it["_hash"] = sha1(json.dumps({"b": it.get("body") or "", "c": it.get("comments") or [],
                                           "m": it.get("metrics") or {}}, ensure_ascii=False,
                                          sort_keys=True))
            it["_is_new"] = seen.get(it["item_id"]) is None
            it["_changed"] = it["_is_new"] or seen.content_hash(it["item_id"]) != it["_hash"]
        new_cnt = sum(1 for it in items if it["_is_new"])
        chg_cnt = sum(1 for it in items if (not it["_is_new"]) and it["_changed"])
        total_items += len(items)
        total_new += new_cnt

        if not args.dry:
            raw_rows = []
            for it in items:
                row = {k: v for k, v in it.items() if not k.startswith("_")}
                row["record_type"] = ("new" if it["_is_new"] else
                                      ("update" if it["_changed"] else "refresh"))
                row["run_id"] = run_id
                raw_rows.append(row)
            append_jsonl(DIR_RAW / ch["id"] / f"{day}.jsonl", raw_rows)
            wrote = 0
            for it in items:
                try:
                    # 无变化条目只记观测次数，不重写正文 note / 项目页（幂等，避免同日重跑刷屏）
                    if it["_changed"]:
                        note = write_corpus_note(it, day)
                        rel = note.relative_to(Path(__file__).resolve().parents[1]).as_posix()
                        log.notes.append(rel)
                        # 实体页准入：不是项目的条目（讨论帖/提问帖/经验帖）不建项目页。
                        # 原实现对**每个条目**都建 → 实测 818 个页面里混进 115 个废页，
                        # 而 reddit 的提问帖天天都有，不设门就会持续污染项目池与分析。
                        # 语义类（person / method）由 kind 直接放行，与 is_project_ish 同判据。
                        if is_project_ish(it) or it.get("kind") in ("person", "method"):
                            write_entity_note(it, rel)
                        wrote += 1
                    else:
                        rel = (seen.get(it["item_id"]) or {}).get("note") or ""
                    seen.touch(it["item_id"], ch["id"], rel, it.get("metrics"),
                               content_hash=it["_hash"])
                    # 记住本轮解析出的 project_url，供下轮在取数失败时继承（防孤儿页）
                    if it.get("project_url"):
                        seen.items[it["item_id"]]["project_url"] = it["project_url"]
                except Exception as e:                             # noqa: BLE001
                    # 单条写盘失败不拖垮整渠道：记错并继续（raw 已落盘，可重放）
                    write_errors += 1
                    log.error(f"{ch['id']}.write[{it.get('item_id')}]", e)
            seen.save()                                            # 每渠道落盘，崩溃不丢账
            body_cache.save()
            write_channel_note(ch, {"started": iso(now_cst()), "status": status, "count": len(items),
                                    "elapsed_s": round(time.time() - t0, 1), "message": msg}, run_id)
            if wrote != len(items):
                msg = f"{msg} | 写盘 {wrote}/{len(items)}"

        log.channel(ch["id"], ch["name"], status, len(items),
                    f"{msg} | new={new_cnt} chg={chg_cnt}", time.time() - t0,
                    extra={"new": new_cnt, "changed": chg_cnt, "raw": len(items)})
        if args.max_total and total_items >= args.max_total:
            print(f"--- 达到 max-total={args.max_total}，停止 ---", flush=True)
            break

    if drop_sink:
        # 丢弃账本：按天追加，dry 也写（调规则时正是靠它判断有没有误杀）
        append_jsonl(META / "rule_drops.jsonl", drop_sink)
        by_reason: dict[str, int] = {}
        for d in drop_sink:
            by_reason[d["reason"]] = by_reason.get(d["reason"], 0) + 1
        print(f"[过滤] 本轮共丢弃 {len(drop_sink)} 条 · " +
              " ".join(f"{k}={v}" for k, v in sorted(by_reason.items())) +
              f" · 账本 _meta/rule_drops.jsonl", flush=True)

    if not args.dry:
        seen.save()
        body_cache.save()
        out = log.finish({"total_items": total_items, "total_new": total_new, "dry": False,
                          "rule_dropped": len(drop_sink), "write_errors": write_errors})
        print(f"=== 完成：{total_items} 条（新 {total_new}）· 运行记录 {out} ===")
        if write_errors:
            print(f"[!] 本轮写盘失败 {write_errors} 条（明细见上方 [X] 行与运行记录 errors 字段）",
                  flush=True)
    else:
        print(f"=== dry-run 完成：{total_items} 条（新 {total_new}）· 未写盘 ===")
    # 退出码恒 0（有意）：单渠道/单条失败已隔离且留痕（[X] 行 + run JSON 的 errors/write_errors），
    # 非零退出会打断自动化链路的后续步骤（analyze/backfill），而 raw 已落盘可重放 ——
    # 可见性靠账本与汇总行，不靠退出码。
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
