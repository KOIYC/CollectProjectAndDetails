"""kb_collect — 独立开发项目知识库 · 多渠道路采集器（零第三方依赖）。

一次运行 = 读 _meta/channels.yaml → 逐渠道取数（独立容错）→ 补全正文/评论
          → 去重 → 双写（原始 JSONL + Obsidian note）→ 更新项目页/渠道页 → 运行记录

用法：
  python tools/kb_collect.py                      # 全渠道
  python tools/kb_collect.py --channels hn_show,v2ex
  python tools/kb_collect.py --dry                # 只取数不写盘（看渠道健康）
  python tools/kb_collect.py --max-total 300      # 总量上限
  python tools/kb_collect.py --force-weekly       # 强制跑 weekly_only 渠道
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_common import (BODY_MIN, DIR_CHANNELS, DIR_CORPUS, DIR_METHOD, DIR_PEOPLE, DIR_PROJECTS,  # noqa: E402
                       DIR_RAW, FULLTEXT_MAX_CHARS, META, BodyCache, FetchError, RunLog, Seen,
                       UNCLOSED_TAG_RE, append_jsonl, body_completeness, ensure_dirs,
                       exa_fetch_texts, exa_search, http_get, http_json, is_project_ish, iso,
                       item_id_for, jina_read, looks_summary, now_cst, norm_url, run_cli,
                       sanitize_record, sha1, slugify, topic_of, write_note)

MAX_COMMENTS = 800
FULLTEXT_BUDGET = 14          # 每渠道最多补全多少条正文（Jina/外部取全文）
FULLTEXT_WORKERS = 5


# ============================================================ registry (mini-yaml)

def _strip_comment(line: str) -> str:
    out, q = [], None
    for i, ch in enumerate(line):
        if q:
            out.append(ch)
            if ch == q:
                q = None
            continue
        if ch in "'\"":
            q = ch
            out.append(ch)
            continue
        if ch == "#" and (i == 0 or line[i - 1] in " \t"):
            break
        out.append(ch)
    return "".join(out)


def _scalar(v: str):
    v = v.strip()
    if not v:
        return None
    if v in ("{}", "{ }"):
        return {}
    if v in ("[]", "[ ]"):
        return []
    if v[0] in "'\"" and v[-1] == v[0] and len(v) > 1:
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [_scalar(x) for x in inner.split(",") if x.strip()] if inner else []
    low = v.lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("null", "~"):
        return None
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v


def load_channels_yaml(path: Path) -> dict:
    """只支持本注册表用到的 YAML 子集：注释/嵌套映射/列表/标量/行内列表/带引号值。"""
    lines = path.read_text(encoding="utf-8").splitlines()
    root: dict = {}
    stack: list[tuple[int, object]] = [(-1, root)]

    def container_for(indent: int):
        while stack and stack[-1][0] >= indent:
            stack.pop()
        return stack[-1][1]

    i = 0
    while i < len(lines):
        raw = lines[i]
        i += 1
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        body = _strip_comment(raw).rstrip()
        if not body.strip():
            continue
        indent = len(body) - len(body.lstrip())
        content = body.strip()
        parent = container_for(indent)

        if content.startswith("- "):
            item_txt = content[2:].strip()
            if isinstance(parent, dict):
                # 列表必须挂在某个 key 上：找到同缩进的 list 容器
                parent = stack[-1][1]
            if isinstance(parent, dict):
                raise ValueError(f"列表项无处挂载: {raw!r}")
            if ":" in item_txt and not item_txt.startswith(("'", '"')):
                key, _, val = item_txt.partition(":")
                node: dict = {key.strip(): _scalar(val)}
                parent.append(node)
                stack.append((indent, node))
            else:
                parent.append(_scalar(item_txt))
            continue

        key, _, val = content.partition(":")
        key = key.strip()
        val = val.strip()
        if not isinstance(parent, dict):
            raise ValueError(f"映射项挂到非映射容器: {raw!r}")
        if val == "":
            node = {}
            parent[key] = node
            stack.append((indent, node))
            # 预判：下一个非空行的缩进若更深且以 '- ' 开头 → 需要 list
            nxt = None
            for j in range(i, len(lines)):
                if lines[j].strip() and not lines[j].lstrip().startswith("#"):
                    nxt = lines[j]
                    break
            if nxt is not None:
                nxt_indent = len(nxt) - len(nxt.lstrip())
                if nxt_indent > indent and nxt.strip().startswith("- "):
                    lst: list = []
                    parent[key] = lst
                    stack[-1] = (indent, lst)
        else:
            parent[key] = _scalar(val)
    return root


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


def load_registry(path: Path | None = None) -> dict:
    p = path or (META / "channels.yaml")
    reg = load_channels_yaml(p)
    channels = [c for c in (reg.get("channels") or []) if c.get("enabled")]
    reg["_enabled_channels"] = channels
    return reg


# ============================================================ text helpers

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"[ \t\u00a0]+")
NL_RE = re.compile(r"\n{3,}")
LINK_RE = re.compile(r"https?://[^\s<>\)\]\"']+")


def strip_html(s: str | None) -> str:
    if not s:
        return ""
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</p>", "\n\n", s)
    s = re.sub(r"(?i)<li[^>]*>", "\n- ", s)
    s = TAG_RE.sub("", s)
    # 上游把 HTML 截断时（RSS 摘要常见）会留下**未闭合标签**，如 `...<a href="..." target="_blank"`，
    # TAG_RE 匹配不到（没有 `>`），必须单独清掉，否则正文尾部残留半截标签。
    s = UNCLOSED_TAG_RE.sub("", s)
    s = html.unescape(s)
    s = WS_RE.sub(" ", s)
    return NL_RE.sub("\n\n", s).strip()


def excerpt(s: str, n: int = 220) -> str:
    s = (s or "").replace("\n", " ").strip()
    return s[:n] + ("…" if len(s) > n else "")


_FENCE_RE = re.compile(r"(```.*?```|~~~.*?~~~|`[^`\n]+`)", re.S)
_INLINE_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")
_SCRIPT_BLOCK_RE = re.compile(r"(?is)<(script|style)\b.*?</\1\s*>")


def readable_body(body: str) -> str:
    """正文可读性清理（渲染层，不动 raw）。

    内容审计实测 69 条 live 语料正文带残留 HTML（`</script>`、`<a href>`、内联标签）。
    这里做**保守清理**：① 摘掉 script/style 整块；② 先保护 markdown 代码段/行内代码
    （里面的 `<tag>` 是源码，不能动），再剥其余内联标签；③ 压掉 >2 连续空行。
    不做 smart 引号/实体转换以外的东西 —— 宁可留 99% 干净，也不要误伤代码段。
    """
    if not body:
        return ""
    s = _SCRIPT_BLOCK_RE.sub("\n", body)
    fences = []
    def _keep(m):
        fences.append(m.group(0))
        return f"\x00F{len(fences) - 1}\x00"
    s = _FENCE_RE.sub(_keep, s)                       # 代码段保护
    s = _INLINE_TAG_RE.sub("", s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = re.sub(r"\x00F(\d+)\x00", lambda m: fences[int(m.group(1))], s)
    return s.strip()


def lead_sentence(body: str, n: int = 160) -> str:
    """实体页「一句话导读」：取正文第一个非空行的前 n 字（自动截断加省略号）。"""
    for ln in (body or "").splitlines():
        t = ln.strip().lstrip("#>-*| ").strip()
        if len(t) < 20:                                # 跳过空行/标题残行/短行
            continue
        # 剥掉发布站模板尾巴（"标题 | BetaList"、"标题 · Site" 这类导航面包屑）
        t = re.sub(r"\s*[|·]\s*[A-Za-z0-9 .&'-]{1,30}$", "", t).strip() or t
        return excerpt(t, n)
    return ""


def detect_lang(text: str, fallback="en") -> str:
    if re.search(r"[\u4e00-\u9fff]", text or ""):
        return "zh"
    return fallback


def as_tags(x) -> list[str]:
    """把任意标签输入压成字符串列表（Apple/PH 等平台会返回 dict 型分类）。"""
    if not x:
        return []
    if isinstance(x, str):
        return [x]
    out = []
    for it in x if isinstance(x, (list, tuple, set)) else [x]:
        if isinstance(it, str):
            out.append(it)
        elif isinstance(it, dict):
            out.append(str(it.get("name") or it.get("slug") or it.get("title") or it.get("id") or ""))
        else:
            out.append(str(it))
    return [t for t in out if t]


# 裸域名里**只有这些**是「通用host而非项目」——github.com / localhost 之类，
# 根路径不带任何项目身份，选中它们会把一堆无关条目挤进同一个项目页。
# 反例：https://cursor.com/ 是某产品的官网首页，本身就是合法 project_url，
# 早先的「一律跳过裸域名」会把它误杀，导致退回选到 twitter 账号页（实测踩过）。
GENERIC_BARE_HOSTS = {
    "github.com", "gitlab.com", "bitbucket.org", "localhost", "127.0.0.1",
    "twitter.com", "x.com", "youtube.com", "youtu.be", "medium.com",
    "google.com", "docs.google.com", "notion.so", "substack.com",
    "news.ycombinator.com", "reddit.com", "producthunt.com", "betalist.com",
    "indiehackers.com", "dev.to", "lobste.rs", "v2ex.com", "bilibili.com",
}

# project_url 合理性校验（R7）：它是**项目页文件名 + 跨渠道归并键**，
# 一个错值 = 两个不同项目共用一个项目页 + 强信号假阳性。
# 实测三类错值：`liqi.io/creators:`（Arnis 与 Clickydots 撞车、尾部还带冒号）、
# `localhost:8080/\``（v2ex 帖正文抠出来的半截链接）、`blog.cloudflare.com/...`
# （一篇博客文被当成项目官网）。
# 只挡「显然不是项目站」的值，不做语义判断 —— 语义交给渠道门禁与内容审计。
PROJECT_URL_BAD_TAIL = re.compile(r"[`'\"”’)>.,;:!?、，。；：！？]$")
_PROJECT_URL_ASSET = re.compile(r"\.(?:png|jpe?g|gif|webp|svg|ico|pdf|zip|rar|7z|mp4|mp3|webm)$", re.I)
NON_PROJECT_HOSTS = {                 # 讨论页 / 聚合站 / 文档与云盘：是「条目来源或文章页」
    "news.ycombinator.com", "reddit.com", "old.reddit.com", "lobste.rs", "v2ex.com",
    "producthunt.com", "betalist.com", "indiehackers.com", "dev.to", "medium.com",
    "substack.com", "blog.cloudflare.com", "youtube.com", "youtu.be", "x.com",
    "twitter.com", "linkedin.com", "facebook.com", "instagram.com", "bilibili.com",
    "zhihu.com", "juejin.cn", "docs.google.com", "drive.google.com", "notion.so",
    "google.com", "feishu.cn", "yuque.com", "mp.weixin.qq.com",
}


def project_url_reject(u: str) -> str:
    """返回拒绝原因（空串 = 可用）。只挡「显然不是项目站」的值。"""
    u = (u or "").strip()
    if not u:
        return "空值"
    if not re.match(r"^https?://", u, re.I):
        return "非 http(s)"
    sp = urllib.parse.urlsplit(u)
    host = sp.netloc.lower().split("@")[-1].split(":")[0]
    if not host:
        return "无域名"
    if host == "localhost" or re.match(r"^\d{1,3}(?:\.\d{1,3}){3}$", host):
        return "本机地址"
    if "." not in host:
        return "无顶级域"
    if host in NON_PROJECT_HOSTS:
        return "讨论页/聚合站/文档站"
    if host.endswith(".blogspot.com"):
        return "博客托管站"
    if PROJECT_URL_BAD_TAIL.search(u):
        return "尾部有标点（半截链接）"
    if _PROJECT_URL_ASSET.search(sp.path):
        return "静态资源链接（不是站点）"
    if host in GENERIC_BARE_HOSTS and not sp.path.strip("/"):
        return "通用站根路径"
    return ""


def derive_project_url(url: str, body: str, existing: str | None = None) -> str | None:
    """project_url 回退推导：正文里第一个「非同源」外链。

    为什么需要单独一个函数：`make_item` 里做这件事的时候，**正文往往还没取到** ——
    RSS / 发布站（producthunt、indiehackers、betalist）的 body 是事后由 enrich 补的。
    构造期推导于是永远拿到空 body，这些渠道的 project_url 实测 100% 缺失
    （producthunt 40/40、indiehackers 20/20、betalist 18/18 全无）。
    而 project_url 正是「同一项目跨渠道归并」与「项目页文件名」的键 ——
    缺了它，跨渠道强信号分析直接失效（洞察层 强信号=0 就是这个后果）。
    所以 enrich 之后必须再跑一次本函数。

    R7：候选项要过 `project_url_reject()`（本机地址/聚合站/半截链接一律不要）——
    宁缺勿错：缺了只会「不参与归并」，错了会让两个项目共用一个项目页。
    """
    if existing:
        return existing
    if not url:
        return None
    base = urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")
    links = sorted(set(LINK_RE.findall(f"{body or ''} ")))[:30]
    for u in links:
        sp = urllib.parse.urlsplit(u)
        net = sp.netloc.lower().removeprefix("www.")
        if not net or net == base or net.endswith(base.split(":")[0]):
            continue
        if project_url_reject(u):
            continue
        return u
    return None


def make_item(*, source_id, source_name, title, url, body="", project_url=None,
              author=None, author_url=None, published_at=None, metrics=None,
              tags=None, kind="post", extra=None, lang=None, discovered_via=None,
              comments=None, comments_total=None, comments_truncated=False,
              body_format="text") -> dict:
    url = (url or project_url or "").strip()
    iid = item_id_for(url, title, source_id)
    body = body or ""
    metas = {k: v for k, v in (metrics or {}).items()}
    ex = dict(extra or {})
    # 显式传入的 project_url 也要过校验：它是项目页文件名 + 跨渠道归并键，
    # 一个错值就让两个不同项目共用一个项目页（实测 liqi.io/creators: / localhost:8080）。
    bad_pu = project_url_reject(project_url) if project_url else ""
    if bad_pu:
        ex["project_url_rejected"] = f"{bad_pu}｜{str(project_url)[:80]}"
        project_url = None
    if not project_url:
        project_url = derive_project_url(url, body)
    # 正文里的外链清单（note 渲染用「## 关联链接」）。注意：构造期 body 多半为空，
    # RSS/发布站的外链要等 enrich 之后才齐 —— 渲染时以最终 body 为准，这里只是兜底。
    links = sorted(set(LINK_RE.findall(f"{body} ")))[:30]
    return {
        "item_id": iid,
        "kind": kind,
        "source_id": source_id,
        "source_name": source_name,
        "title": (title or "").strip() or "(无标题)",
        "url": url,
        "project_url": norm_url(project_url) if project_url else None,
        "author": author,
        "author_url": author_url,
        "published_at": published_at,
        "captured_at": iso(now_cst()),
        "lang": lang or detect_lang(f"{title}\n{body}"),
        "body": body.strip(),
        "body_format": body_format,
        "comments": comments or [],
        "comments_total": comments_total if comments_total is not None else len(comments or []),
        "comments_truncated": comments_truncated,
        "metrics": metas,
        "tags": as_tags(tags),
        "links": links,
        "discovered_via": discovered_via or source_id,
        "extra": ex,
    }


# ============================================================ adapters

def ad_hn_show(ch, ctx) -> tuple[list[dict], str, str]:
    """HN 渠道（adapter 复用）：params.tags 决定取 Show HN 还是首页 front_page。"""
    p = ch.get("params") or {}
    tags = p.get("tags") or "show_hn"
    days = int(p.get("window_days") or ch.get("window_days") or 3)
    limit = int(ch.get("limit") or 50)
    minp = int(p.get("min_points") or 1)
    since = int((now_cst() - timedelta(days=days)).timestamp())
    url = (f"https://hn.algolia.com/api/v1/search_by_date?tags={urllib.parse.quote(tags)}"
           f"&hitsPerPage={limit}&numericFilters=points>={minp},created_at_i>{since}")
    hits = (http_json(url).get("hits") or [])
    items = []
    for h in hits:
        oid = h.get("objectID")
        items.append(make_item(
            source_id=ch["id"], source_name=ch["name"],
            title=h.get("title") or h.get("story_title") or "",
            url=f"https://news.ycombinator.com/item?id={oid}",
            project_url=h.get("url"), author=h.get("author"),
            author_url=f"https://news.ycombinator.com/user?id={h.get('author')}",
            published_at=h.get("created_at"),
            metrics={"points": h.get("points"), "comments": h.get("num_comments"),
                     "engagement_velocity": h.get("points")},
            tags=[t for t in (h.get("_tags") or []) if t != "story"],
            extra={"hn_id": oid, "story_text": strip_html(h.get("story_text")),
                   "fulltext_url": h.get("url")},
            discovered_via=f"hn:{tags}:{days}d"))
    return items, ("ok" if items else "empty"), f"{len(items)}/{len(hits)} hits"


def _enrich_hn_comments(items: list[dict], ctx) -> None:
    """HN 全量评论树。两条纪律（都是实测踩出来的）：

    ① **单条失败不许拖垮整批**：原实现 one() 没有 try/except，而
       ThreadPoolExecutor.map 在第一个异常上就把整批抛出去 —— 一次网络抖动 =
       该渠道剩下所有条目都没有评论，且条目身上不留任何痕迹（只在 run 日志里一行
       error）。实测 400 条 hn_show 里 369 条零评论，其中 121 条平台明说有评论
       （均值 3.3、最多 18）却一条没抓到。
    ② **平台计数是下限**：`metrics.comments` 来自列表 API 的 num_comments。
       原实现把 comments_total 写成「实际抓到的条数」，抓 0 条就写 0 ——
       回填账本（kb_backfill.comments_gap）据此以为「这帖本来没人评论」，
       缺口就此隐形，永远不会被回补。
    """
    cap = int(ctx.get("max_comments") or MAX_COMMENTS)

    def one(it):
        ex = it.setdefault("extra", {})
        oid = ex.get("hn_id")
        if not oid:
            return
        platform = int((it.get("metrics") or {}).get("comments") or 0)
        try:
            d = http_json(f"https://hn.algolia.com/api/v1/items/{oid}", timeout=30, retries=1)
        except Exception as e:                                     # noqa: BLE001
            ex["comments_error"] = f"{type(e).__name__}: {str(e)[:60]}"
            it["comments"] = it.get("comments") or []
            it["comments_total"] = max(platform, len(it["comments"]))
            return                                                 # 单条失败只影响这一条
        comments, total = [], 0
        stack = list(d.get("children") or [])
        while stack:
            c = stack.pop(0)
            txt = strip_html(c.get("text"))
            if txt:
                total += 1
                if len(comments) < cap:
                    comments.append({"author": c.get("author"), "text": txt,
                                     "created_at": c.get("created_at"), "score": None})
            stack.extend(c.get("children") or [])
        ex.pop("comments_error", None)
        it["comments"] = comments
        it["comments_total"] = max(platform, total, len(comments))
        it["comments_truncated"] = total > len(comments)
        if total == 0 and platform > 0:
            # 平台说有人评论、items API 却一条正文都没给 → 记「不完整」，交回填队列重试
            ex["comments_partial"] = f"API 返回 0 条，平台计数 {platform}"
        else:
            ex.pop("comments_partial", None)
        if not it["body"]:
            it["body"] = ex.get("story_text") or it["title"]

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(one, items))


def ad_github_new(ch, ctx) -> tuple[list[dict], str, str]:
    p = ch.get("params") or {}
    days = int(p.get("window_days") or 14)
    min_stars = int(p.get("min_stars") or 10)
    since = (now_cst() - timedelta(days=days)).strftime("%Y-%m-%d")
    limit = int(ch.get("limit") or 40)
    queries = [q.format(since=since, min_stars=min_stars) for q in (p.get("queries") or [])]
    items, seen_ids, msgs = [], set(), []
    per = max(5, limit // max(1, len(queries)))
    for q in queries:
        code, out, err = run_cli(["gh", "search", "repos", q, "--sort", "stars", "--limit", str(per),
                                  "--json", "fullName,name,description,stargazersCount,url,createdAt,"
                                            "owner,language,forksCount,openIssuesCount,homepage,pushedAt"],
                                 timeout=90)
        if code != 0:
            msgs.append(f"{q[:28]}: {(err or out)[:60]}")
            continue
        try:
            rows = json.loads(out or "[]")
        except json.JSONDecodeError:
            msgs.append(f"{q[:28]}: bad-json")
            continue
        for r in rows:
            full = r.get("fullName")
            if not full or full in seen_ids:
                continue
            seen_ids.add(full)
            owner = (r.get("owner") or {}).get("login")
            body = (r.get("description") or "")
            items.append(make_item(
                source_id=ch["id"], source_name=ch["name"],
                title=full, url=r.get("url") or f"https://github.com/{full}",
                project_url=r.get("homepage") or r.get("url"),
                body=body, author=owner, author_url=f"https://github.com/{owner}",
                published_at=r.get("createdAt"),
                metrics={"stars": r.get("stargazersCount"), "forks": r.get("forksCount"),
                         "open_issues": r.get("openIssuesCount")},
                tags=as_tags(r.get("language")) + [q.split()[0]],
                extra={"full_name": full, "query": q}, lang="en",
                discovered_via=f"github:{days}d"))
    items = items[:limit]
    return items, ("ok" if items else "error"), f"{len(items)} repos; {'; '.join(msgs)[:120]}"


def _enrich_github_readme(items: list[dict], ctx) -> None:
    budget = min(int(ctx.get("fulltext_budget") or FULLTEXT_BUDGET), len(items))

    def one(it):
        full = it["extra"].get("full_name")
        if not full:
            return
        code, out, _ = run_cli(["gh", "api", f"repos/{full}/readme", "-H",
                                "Accept: application/vnd.github.raw"], timeout=60)
        if code == 0 and out.strip():
            it["body"] = out.strip()[:60000]

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(one, items[:budget]))


def ad_reddit_arctic(ch, ctx) -> tuple[list[dict], str, str]:
    p = ch.get("params") or {}
    subs = p.get("subs") or ["SideProject"]
    days = int(p.get("window_days") or 7)
    settle = int(p.get("settle_days") or 3)       # 镜像 score 有装载延迟，取已沉淀窗口
    min_score = int(p.get("min_score") or 3)
    # arctic-shift 单次上限 100；历史铺底时 limit 会被放大，必须夹住，否则整片返回空
    per = min(100, max(25, int(ch.get("limit") or 40) // max(1, len(subs)) * 3))   # 先宽取再按分过滤
    after_ts = int((now_cst() - timedelta(days=days + settle)).timestamp())
    before_ts = int((now_cst() - timedelta(days=settle)).timestamp())
    items, msgs = [], []
    # 历史铺底（P0-2）：arctic-shift 的 limit 一次只返回「窗口内最近的 N 条」，
    # 把 window_days 从 7 拉到 90 并不会让结果散开到 90 天里 —— 仍是最新 N 条。
    # 所以要看长历史必须把窗口**切片**，逐片查询再合并。
    slice_days = int(ctx.get("slice_days") or p.get("slice_days") or 0)
    windows = []
    if slice_days > 0 and (days + settle) > slice_days:
        t = after_ts
        while t < before_ts:
            windows.append((t, min(t + slice_days * 86400, before_ts)))
            t += slice_days * 86400
    else:
        windows.append((after_ts, before_ts))
    for sub in subs:
        for (wa, wb) in windows:
            u = ("https://arctic-shift.photon-reddit.com/api/posts/search?"
                 f"subreddit={urllib.parse.quote(sub)}&limit={per}&sort=desc"
                 f"&after={wa}&before={wb}")
            try:
                rows = (http_json(u, timeout=35, retries=1).get("data") or [])
            except Exception as e:                                 # noqa: BLE001
                msgs.append(f"{sub}: {str(e)[:40]}")
                continue
            for r in rows:
                score = r.get("score") or 0
                title = r.get("title") or ""
                # 已被版主移除的帖子：正文与评论都不可得，入库只会污染语料
                if score < min_score or "Removed by moderator" in title or title.strip() in ("[removed]", "[deleted]"):
                    continue
                body = r.get("selftext") or ""
                if body in ("[removed]", "[deleted]"):
                    body = ""
                items.append(make_item(
                    source_id=ch["id"], source_name=ch["name"],
                    title=r.get("title") or "", url=f"https://www.reddit.com{r.get('permalink','')}",
                    project_url=r.get("url_overridden_by_dest") or (r.get("url") if not str(r.get("url", "")).startswith("https://www.reddit.com") else None),
                    body=body, author=r.get("author"),
                    author_url=f"https://www.reddit.com/user/{r.get('author')}",
                    published_at=datetime.fromtimestamp(r.get("created_utc") or 0, tz=now_cst().tzinfo).isoformat() if r.get("created_utc") else None,
                    metrics={"score": score, "comments": r.get("num_comments"),
                             "upvote_ratio": r.get("upvote_ratio")},
                    tags=[f"r/{sub}"] + ([r["link_flair_text"]] if r.get("link_flair_text") else []),
                    extra={"reddit_id": r.get("id"), "subreddit": sub,
                           "fulltext_url": r.get("url_overridden_by_dest")
                       if r.get("url_overridden_by_dest") and "reddit.com" not in str(r.get("url_overridden_by_dest"))
                       else None},
                discovered_via=f"reddit:{days}d+settle{settle}"))
    items.sort(key=lambda it: (it.get("metrics", {}).get("score") or 0), reverse=True)
    items = items[: int(ch.get("limit") or 40)]
    return items, ("ok" if items else "empty"), f"{len(items)} posts; {'; '.join(msgs)[:100]}"


def _arctic_comments_once(rid: str, limit: int, after: int | None = None) -> list[dict]:
    u = (f"https://arctic-shift.photon-reddit.com/api/comments/search?"
         f"link_id=t3_{rid}&limit={limit}&sort=asc")
    if after:
        u += f"&after={after}"
    return http_json(u, timeout=45, retries=1).get("data") or []


def _enrich_reddit_comments(items: list[dict], ctx) -> None:
    """arctic 的 limit 上限 = 100（传 800 会 400，2026-09-20 实测）→ 用 after 游标翻页。"""
    cap = int(ctx.get("max_comments") or MAX_COMMENTS)
    page = 100

    def one(it):
        rid = it["extra"].get("reddit_id")
        if not rid:
            return
        cs, cursor, guard = [], None, 0
        while len(cs) < cap and guard < 12:
            guard += 1
            try:
                rows = _arctic_comments_once(rid, min(page, cap - len(cs)), cursor)
            except Exception as e:                                  # noqa: BLE001
                it["extra"]["comments_error"] = str(e)[:120]
                break
            if not rows:
                break
            for c in rows:
                txt = (c.get("body") or "").strip()
                if not txt or txt in ("[removed]", "[deleted]"):
                    continue
                cs.append({"author": c.get("author"), "text": txt[:8000],
                           "created_at": datetime.fromtimestamp(
                               c.get("created_utc") or 0, tz=now_cst().tzinfo).isoformat()
                           if c.get("created_utc") else None,
                           "score": c.get("score")})
            if len(rows) < page:
                break
            cursor = int(rows[-1].get("created_utc") or 0) + 1
        it["comments"] = cs[:cap]
        it["comments_total"] = max(it.get("metrics", {}).get("comments") or 0, len(cs))
        # 只有“撞到上限”才算截断；平台计数多出的是被删/被折叠评论，不算截断
        it["comments_truncated"] = len(cs) >= cap

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(one, items))


def ad_lobsters(ch, ctx) -> tuple[list[dict], str, str]:
    limit = int(ch.get("limit") or 25)
    min_score = int((ch.get("params") or {}).get("min_score") or 3)
    rows = http_json("https://lobste.rs/hottest.json", timeout=45, retries=2)
    items = []
    for r in rows:
        if (r.get("score") or 0) < min_score:
            continue
        items.append(make_item(
            source_id=ch["id"], source_name=ch["name"], title=r.get("title") or "",
            url=r.get("comments_url") or r.get("short_id_url"),
            project_url=r.get("url"), body=strip_html(r.get("description") or ""),
            author=((r.get("submitter_user") or {}).get("username") if isinstance(r.get("submitter_user"), dict) else None),
            published_at=r.get("created_at"),
            metrics={"score": r.get("score"), "comments": r.get("comment_count")},
            tags=r.get("tags") or [], extra={"short_id": r.get("short_id"), "story_url": r.get("url"),
                                             "fulltext_url": r.get("url")},
            discovered_via="lobsters:hottest"))
    return items[:limit], ("ok" if items else "empty"), f"{len(items)} stories"


def _enrich_lobsters_comments(items: list[dict], ctx) -> None:
    cap = int(ctx.get("max_comments") or MAX_COMMENTS)

    def flat(cs, out, depth=0):
        for c in cs or []:
            if len(out) >= cap:
                return
            txt = strip_html(c.get("comment") or "")
            if txt:
                out.append({"author": c.get("commenting_user"), "text": txt,
                            "created_at": c.get("created_at"), "score": c.get("score")})
            flat(c.get("comments"), out, depth + 1)

    def one(it):
        sid = it["extra"].get("short_id")
        if not sid:
            return
        try:
            d = http_json(f"https://lobste.rs/s/{sid}.json", timeout=40, retries=1)
        except Exception:                                          # noqa: BLE001
            return
        out: list[dict] = []
        flat(d.get("comments"), out)
        if not it["body"]:
            it["body"] = strip_html(d.get("description") or "")
        it["comments"] = out
        it["comments_total"] = max(d.get("comment_count") or 0, len(out))
        it["comments_truncated"] = (d.get("comment_count") or 0) > len(out)

    with ThreadPoolExecutor(3) as ex:
        list(ex.map(one, items))


def ad_devto(ch, ctx) -> tuple[list[dict], str, str]:
    p = ch.get("params") or {}
    tags = p.get("tags") or ["showdev"]
    days = int(p.get("window_days") or 14)
    min_re = int(p.get("min_reactions") or 0)
    per = max(5, int(ch.get("limit") or 30) // max(1, len(tags)))
    cutoff = now_cst() - timedelta(days=days)
    items, seen_ids = [], set()
    for tag in tags:
        try:
            rows = http_json(f"https://dev.to/api/articles?tag={tag}&per_page={per}&top=30", timeout=30)
        except Exception:                                          # noqa: BLE001
            continue
        for r in rows:
            if r.get("id") in seen_ids:
                continue
            seen_ids.add(r.get("id"))
            pub = r.get("published_at") or ""
            try:
                if pub and datetime.fromisoformat(pub.replace("Z", "+00:00")) < cutoff:
                    continue
            except ValueError:
                pass
            if (r.get("positive_reactions_count") or 0) < min_re:
                continue
            items.append(make_item(
                source_id=ch["id"], source_name=ch["name"], title=r.get("title") or "",
                url=r.get("url"), project_url=(r.get("canonical_url") or None),
                body=r.get("description") or "", author=(r.get("user") or {}).get("name"),
                author_url=(r.get("user") or {}).get("username") and
                f"https://dev.to/{(r.get('user') or {}).get('username')}",
                published_at=pub or None,
                metrics={"reactions": r.get("positive_reactions_count"),
                         "comments": r.get("comments_count"), "reading_time": r.get("reading_time_minutes")},
                tags=r.get("tag_list") or [], extra={"devto_id": r.get("id")},
                lang="en", discovered_via=f"devto:{tag}"))
    return items[: int(ch.get("limit") or 30)], ("ok" if items else "empty"), f"{len(items)} articles"


def _enrich_devto_body(items: list[dict], ctx) -> None:
    """dev.to：补正文（body_markdown）+ 全量评论（/api/comments?a_id=，公开无鉴权）。"""
    budget = min(int(ctx.get("fulltext_budget") or FULLTEXT_BUDGET), len(items))
    cap = int(ctx.get("max_comments") or MAX_COMMENTS)

    def one(it):
        did = it["extra"].get("devto_id")
        if not did:
            return
        try:
            d = http_json(f"https://dev.to/api/articles/{did}", timeout=30, retries=1)
            if d.get("body_markdown"):
                it["body"] = d["body_markdown"][:60000]
                it["body_format"] = "markdown"
        except Exception as e:                                     # noqa: BLE001
            it["extra"]["body_error"] = str(e)[:100]
        # dev.to 的评论 API 默认 per_page=30 → 不显式指定 + 翻页会**静默截断**大帖
        # （实测 182 评论的帖有 85 条顶层，只给 30）。必须 per_page=60 + page 翻页，且翻到空为止。
        cs, page, got_any = [], 1, False
        while page <= 20:
            try:
                part = http_json(f"https://dev.to/api/comments?a_id={did}&per_page=60&page={page}",
                                 timeout=45, retries=1)
            except Exception as e:                                 # noqa: BLE001
                if not got_any:
                    it["extra"]["comments_error"] = str(e)[:100]
                else:
                    it["extra"]["comments_partial"] = f"page{page}: {str(e)[:60]}"
                break
            got_any = True
            if not isinstance(part, list) or not part:
                break
            cs.extend(part)
            if len(cs) >= cap:
                break
            page += 1
        out = []

        def walk(nodes, depth=0):
            """dev.to 的 /api/comments?a_id= 只返回顶层评论，回复在 children 里，必须递归。"""
            for c in nodes or []:
                if len(out) >= cap:
                    return
                txt = strip_html(c.get("body_html") or "")
                if txt:
                    out.append({"author": (c.get("user") or {}).get("name"),
                                "text": ("  " * depth) + txt[:8000],
                                "created_at": c.get("created_at"), "score": None})
                walk(c.get("children"), depth + 1)

        walk(cs)
        it["comments"] = out
        it["comments_total"] = max(it.get("metrics", {}).get("comments") or 0, len(out))
        # 截断判定要看「是否还有下一页」：抓满 cap，或顶层还没翻完就停了
        it["comments_truncated"] = len(out) >= cap or (bool(cs) and len(cs) >= page * 60)

    with ThreadPoolExecutor(4) as ex:
        list(ex.map(one, items[:budget]))


def _parse_feed(xml: str, limit: int) -> list[dict]:
    out = []
    blocks = re.split(r"(?i)<(?=entry\b|item\b)", xml)[1:]
    for b in blocks:
        def pick(tag):
            m = re.search(rf"(?is)<{tag}[^>]*>(.*?)</{tag}>", b)
            return m.group(1).strip() if m else ""
        title = strip_html(pick("title"))
        link = ""
        m = re.search(r'(?is)<link[^>]*href="([^"]+)"', b)
        if m:
            link = m.group(1)
        else:
            m = re.search(r"(?is)<link[^>]*>(.*?)</link>", b)
            link = strip_html(m.group(1)) if m else ""
        content = pick("content:encoded") or pick("content") or pick("summary") or pick("description")
        date = pick("published") or pick("updated") or pick("pubDate") or pick("dc:date")
        author = strip_html(pick("author") or pick("dc:creator"))
        if not link:
            continue
        out.append({"title": title, "url": link, "body": strip_html(content),
                    "published": date or None, "author": author or None})
        if len(out) >= limit:
            break
    return out


def ad_rss_atom(ch, ctx) -> tuple[list[dict], str, str]:
    feed = (ch.get("params") or {}).get("feed")
    if not feed:
        return [], "error", "缺 params.feed"
    xml = http_get(feed, timeout=30, retries=1).decode("utf-8", "replace")
    rows = _parse_feed(xml, int(ch.get("limit") or 20))
    items = [make_item(source_id=ch["id"], source_name=ch["name"], title=r["title"], url=r["url"],
                       body=r["body"], author=r["author"], published_at=r["published"],
                       kind="post", discovered_via=ch["id"]) for r in rows]
    return items, ("ok" if items else "empty"), f"{len(items)} entries"


def ad_ih_products(ch, ctx) -> tuple[list[dict], str, str]:
    pages = int((ch.get("params") or {}).get("pages") or 2)
    limit = int(ch.get("limit") or 30)
    items, seen = [], set()
    for pg in range(pages):
        u = "https://www.indiehackers.com/products" + (f"?page={pg + 1}" if pg else "")
        try:
            t = http_get(u, timeout=35, retries=1).decode("utf-8", "replace")
        except Exception as e:                                     # noqa: BLE001
            if not items:
                return [], "error", f"{str(e)[:60]}"
            break
        for slug in dict.fromkeys(re.findall(r'href="(/product/([a-z0-9\-_]+))[^"]*"', t)):
            pass
        for full, slug in dict.fromkeys(re.findall(r'href="(/product/([a-z0-9\-_]+))[^"]*"', t)):
            if slug in seen:
                continue
            seen.add(slug)
            name = slug.replace("-", " ").title()
            items.append(make_item(
                source_id=ch["id"], source_name=ch["name"], title=name,
                url=f"https://www.indiehackers.com{full}",
                body="", kind="project", lang="en", discovered_via="ih:products"))
    return items[:limit], ("ok" if items else "empty"), f"{len(items)} products"


def ad_betalist(ch, ctx) -> tuple[list[dict], str, str]:
    limit = int(ch.get("limit") or 25)
    t = http_get("https://betalist.com/", timeout=30, retries=1).decode("utf-8", "replace")
    slugs = list(dict.fromkeys(re.findall(r'href="(/startups/([a-z0-9\-_]+))"', t)))
    items = []
    for full, slug in slugs[:limit]:
        items.append(make_item(source_id=ch["id"], source_name=ch["name"],
                               title=slug.replace("-", " ").title(),
                               url=f"https://betalist.com{full}", kind="project",
                               lang="en", discovered_via="betalist:home"))
    return items, ("ok" if items else "empty"), f"{len(items)} startups"


def ad_uneed(ch, ctx) -> tuple[list[dict], str, str]:
    """Uneed 首页 JS 渲染 → 走 Exa web_fetch 兜底（Jina 本网络不可用）。"""
    try:
        got = exa_fetch_texts(["https://www.uneed.best/"], max_chars=12000)
    except Exception as e:                                         # noqa: BLE001
        return [], "error", f"exa_fetch: {str(e)[:70]}"
    md = next(iter(got.values()), "")
    if not md:
        return [], "empty", "exa_fetch 未返回正文"
    rows = re.findall(r"\[([^\]\n]{2,60})\]\((https://www\.uneed\.best/tool/[^\)]+)\)", md)
    if not rows:
        rows = [(m.replace("-", " ").title(), f"https://www.uneed.best/tool/{m}")
                for m in dict.fromkeys(re.findall(r"uneed\.best/tool/([a-z0-9\-_]+)", md))]
    items = [make_item(source_id=ch["id"], source_name=ch["name"], title=t, url=u, kind="project",
                       body="", lang="en", discovered_via="uneed:exa") for t, u in rows]
    items = items[: int(ch.get("limit") or 20)]
    return items, ("ok" if items else "empty"), f"{len(items)} tools (exa)"


def ad_apple_rss(ch, ctx) -> tuple[list[dict], str, str]:
    """App Store 榜单：只取榜单元数据。大厂 App 与“独立开发”无关 → 按 artist 过滤。"""
    paths = (ch.get("params") or {}).get("paths") or []
    base = "https://rss.marketingtools.apple.com/api/v2/"
    big = ("openai", "meta platforms", "google", "alphabet", "bytedance", "tencent", "alibaba",
           "microsoft", "amazon", "apple", "netflix", "spotify", "kalshi", "roblox", "epic games",
           "youtube", "whatsapp", "discord", "adobe", "x corp", "nvidia", "samsung", "baidu")
    items, skipped = [], 0
    for p in paths:
        try:
            d = http_json(base + p, timeout=30, retries=1)
        except Exception:                                          # noqa: BLE001
            continue
        region = p.split("/")[0]
        kind = "paid" if "paid" in p else "free"
        for i, r in enumerate((d.get("feed") or {}).get("results") or []):
            artist = (r.get("artistName") or "")
            if any(b in artist.lower() for b in big):
                skipped += 1
                continue
            items.append(make_item(
                source_id=ch["id"], source_name=ch["name"],
                title=f"{r.get('name')} — {artist}", url=r.get("url"),
                project_url=r.get("url"), kind="project", lang="en",
                author=artist, metrics={"rank": i + 1},
                tags=(r.get("genres") or []) + [f"{region}-top-{kind}"],
                extra={"artwork": r.get("artworkUrl100"), "region": region},
                discovered_via=f"apple:{region}:{kind}"))
    msg = f"{len(items)} apps（过滤大厂 {skipped}）"
    return items[: int(ch.get("limit") or 30)], ("ok" if items else "empty"), msg


def ad_sov2ex(ch, ctx) -> tuple[list[dict], str, str]:
    p = ch.get("params") or {}
    size = int(p.get("size") or 20)
    sort = p.get("sort") or "created"
    items, seen = [], set()
    for q in (p.get("queries") or []):
        u = (f"https://www.sov2ex.com/api/search?q={urllib.parse.quote(q)}"
             f"&size={size}&sort={sort}")
        try:
            d = http_json(u, timeout=30, retries=1)
        except Exception:                                          # noqa: BLE001
            continue
        for h in d.get("hits") or []:
            s = h.get("_source") or {}
            tid = s.get("id")
            if not tid or tid in seen:
                continue
            seen.add(tid)
            items.append(make_item(
                source_id=ch["id"], source_name=ch["name"], title=s.get("title") or "",
                url=f"https://www.v2ex.com/t/{tid}", body=s.get("content") or "",
                author=s.get("member"), published_at=s.get("created"),
                metrics={"replies": s.get("replies")},
                tags=[s.get("node") or ""], extra={"topic_id": tid, "query": q},
                discovered_via=f"v2ex:{q}"))
    return items[: int(ch.get("limit") or 30)], ("ok" if items else "empty"), f"{len(items)} topics"


PERSON_HANDLE_RE = re.compile(r"\(@([A-Za-z0-9_]{2,})\)")
ACCOUNT_URL_RE = re.compile(r"^https?://(?:www\.)?(?:twitter\.com|x\.com)/([A-Za-z0-9_]+)/?$", re.I)


def ad_onec7(ch, ctx) -> tuple[list[dict], str, str]:
    readme = (ch.get("params") or {}).get("readme")
    t = http_get(readme, timeout=40, retries=1).decode("utf-8", "replace")
    limit = int(ch.get("limit") or 60)
    items, section = [], ""
    for line in t.splitlines():
        if line.startswith("#"):
            section = line.lstrip("# ").strip()
            continue
        m = re.match(r"^\s*[-*]\s*\[([^\]]+)\]\((https?://[^\)]+)\)\s*[:：-]?\s*(.*)$", line)
        if not m:
            continue
        name, url, desc = m.group(1).strip(), m.group(2).strip(), strip_html(m.group(3))
        # 人物 vs 项目分流：1c7 名录里混着「独立开发大牛」条目（如 `Patrick McKenzie (@patio11)`
        # 或指向 x.com/<handle>）。它们不是项目，归到 30-人物/ 才符合 KB 分层。
        h1 = PERSON_HANDLE_RE.search(name)
        h2 = ACCOUNT_URL_RE.search(url)
        is_person = bool(h1 or h2)
        items.append(make_item(
            source_id=ch["id"], source_name=ch["name"], title=name, url=url,
            project_url=None if is_person else url, body=desc,
            kind="person" if is_person else "project", lang="zh",
            author=(h1.group(1) if h1 else (h2.group(1) if h2 else None)) if is_person else None,
            author_url=url if is_person else None,
            tags=[section] if section else [], extra={"section": section},
            discovered_via="1c7:readme"))
        if len(items) >= limit * 3:
            break
    return items[:limit], ("ok" if items else "empty"), f"{len(items)} entries"


def ad_bilibili(ch, ctx) -> tuple[list[dict], str, str]:
    p = ch.get("params") or {}
    min_play = int(p.get("min_play") or 0)
    items, seen = [], set()
    hdr = {"Referer": "https://www.bilibili.com", "Origin": "https://www.bilibili.com"}
    for q in (p.get("queries") or []):
        u = ("https://api.bilibili.com/x/web-interface/wbi/search/type?"
             f"search_type=video&page=1&keyword={urllib.parse.quote(q)}")
        try:
            d = http_json(u, headers=hdr, timeout=30, retries=1)
        except Exception:                                          # noqa: BLE001
            continue
        for r in ((d.get("data") or {}).get("result") or []):
            bv = r.get("bvid")
            if not bv or bv in seen:
                continue
            seen.add(bv)
            play = r.get("play") or 0
            if play < min_play:
                continue
            items.append(make_item(
                source_id=ch["id"], source_name=ch["name"],
                title=strip_html(r.get("title") or ""),
                url=f"https://www.bilibili.com/video/{bv}",
                project_url=f"https://www.bilibili.com/video/{bv}",
                body=strip_html(r.get("description") or ""),
                author=r.get("author"),
                author_url=f"https://space.bilibili.com/{r.get('mid')}",
                published_at=datetime.fromtimestamp(r.get("pubdate") or 0, tz=now_cst().tzinfo).isoformat()
                if r.get("pubdate") else None,
                metrics={"play": play, "danmaku": r.get("video_review"), "favorites": r.get("favorites")},
                tags=[t for t in strip_html(r.get("tag") or "").split(",") if t],
                extra={"bvid": bv, "query": q}, lang="zh", discovered_via=f"bili:{q}"))
    return items[: int(ch.get("limit") or 20)], ("ok" if items else "empty"), f"{len(items)} videos"


def ad_opencli_social(ch, ctx) -> tuple[list[dict], str, str]:
    """小红书 / X：需浏览器登录态（OpenCLI）；未解锁时返回 auth 状态，不静默跳过。"""
    p = ch.get("params") or {}
    site = p.get("site")
    code, out, err = run_cli(["opencli", site, "search", (p.get("queries") or [""])[0], "-f", "yaml"],
                             timeout=90)
    if code != 0 or "BROWSER_CONNECT" in (out + err):
        return [], "auth", f"需 OpenCLI 浏览器扩展/登录态：{(err or out)[:80]}"
    items = []
    for blk in re.split(r"\n(?=- )", out):
        url = re.search(r"url:\s*(\S+)", blk)
        title = re.search(r"title:\s*(.+)", blk)
        if url:
            items.append(make_item(source_id=ch["id"], source_name=ch["name"],
                                   title=(title.group(1).strip() if title else "untitled"),
                                   url=url.group(1).strip(), body=blk[:4000],
                                   lang="zh" if site == "xiaohongshu" else "en",
                                   discovered_via=f"opencli:{site}"))
    return items, ("ok" if items else "auth"), f"{len(items)} items"


def ad_exa_discovery(ch, ctx) -> tuple[list[dict], str, str]:
    items = []
    for q in (ch.get("params") or {}).get("queries") or []:
        for r in exa_search(q, n=8):
            items.append(make_item(
                source_id=ch["id"], source_name=ch["name"], title=r.get("title") or "",
                url=r.get("url"), body=r.get("text") or "", published_at=r.get("published"),
                kind="method", extra={"query": q}, discovered_via=f"exa:{q}"))
    return items[: int(ch.get("limit") or 40)], ("ok" if items else "empty"), f"{len(items)} results"


ADAPTERS = {
    "hn_show": ad_hn_show, "github_new": ad_github_new, "reddit_arctic": ad_reddit_arctic,
    "lobsters": ad_lobsters, "devto": ad_devto, "rss_atom": ad_rss_atom,
    "ih_products": ad_ih_products, "betalist": ad_betalist, "uneed": ad_uneed,
    "apple_rss": ad_apple_rss, "sov2ex": ad_sov2ex, "onec7": ad_onec7,
    "bilibili": ad_bilibili, "opencli_social": ad_opencli_social, "exa_discovery": ad_exa_discovery,
}

ENRICHERS = {
    "comments_hn": _enrich_hn_comments, "readme": _enrich_github_readme,
    "comments_reddit": _enrich_reddit_comments, "comments_lobsters": _enrich_lobsters_comments,
    "fulltext_devto": _enrich_devto_body,
}
# 键必须是**渠道 id**（channels.yaml 的 id），不是 adapter 名 —— 2026-09-20 踩过：
# 写成 reddit_arctic 导致 Reddit 评论补全从未执行且无报错。main() 里有显式校验。
ENRICH_ROUTING = {
    "hn_show": ("comments", _enrich_hn_comments),
    "hn_front": ("comments", _enrich_hn_comments),
    "github_new": ("readme", _enrich_github_readme),
    "reddit": ("comments", _enrich_reddit_comments),
    "lobsters": ("comments", _enrich_lobsters_comments),
    "devto": ("fulltext", _enrich_devto_body),
}


def enrich_generic(items: list[dict], ctx) -> None:
    """通用正文补全：正文过短**或带摘要痕迹** → Exa web_fetch 批量取正文（预算内）。

    取数目标优先用 `extra.fulltext_url` —— 讨论帖（HN/Lobsters/Reddit 链接帖）的正文
    在**外部文章页**，不在讨论页；这一点不做区分就会大量漏正文。
    Jina Reader 已实测不可用（见 kb_common.jina_read 注释），故唯一后端 = Exa。

    R6 修复：
      ① 触发条件原来只有 `len(body) < 160`，导致「RSS 摘要型 feed」（正文 300-600 字符、尾部带
         `Read more` / 未闭合 `<a>`）被判定为「已有正文」而**跳过补全** —— 少数派 7/10 残文就是这么来的。
         现改为 `len(body) < 160 or looks_summary(body)`。
      ② `max_chars` 原来 8000，长文被硬砍且**不留痕迹**（违反「不许静默截断」）。
         现提高到 FULLTEXT_MAX_CHARS 并在命中上限时写 `extra.body_truncated`。
    """
    budget = int(ctx.get("fulltext_budget") or FULLTEXT_BUDGET)

    def target_url(it) -> str:
        return (it.get("extra", {}).get("fulltext_url") or it.get("url") or "").strip()

    def needs(it) -> bool:
        b = it.get("body") or ""
        return len(b) < 160 or looks_summary(b)

    targets = [it for it in items if needs(it) and target_url(it)][:budget]
    if not targets:
        return
    urls, seen = [], set()
    for it in targets:
        u = target_url(it)
        if u not in seen:
            seen.add(u)
            urls.append(u)
    try:
        got = exa_fetch_texts(urls, max_chars=FULLTEXT_MAX_CHARS)
    except Exception as e:                                         # noqa: BLE001
        print(f"    [w] exa_fetch 失败：{str(e)[:80]}", flush=True)
        return
    hit = 0
    for it in targets:
        u = target_url(it)
        txt = got.get(u) or got.get(norm_url(u))
        if txt and len(txt) > len(it.get("body") or ""):
            it["body"] = txt[:FULLTEXT_MAX_CHARS]
            it["body_format"] = "markdown"
            it.setdefault("extra", {})["body_source"] = "exa_web_fetch"
            it["extra"]["body_url"] = u
            # 命中上限 = 被截断，必须显式标记（下游据此区分「全文」与「开头」）
            if len(txt) >= FULLTEXT_MAX_CHARS - 60:
                it["extra"]["body_truncated"] = True
                it["extra"]["body_chars"] = len(txt)
            else:
                it["extra"].pop("body_truncated", None)
            hit += 1
    print(f"    [i] 正文补全 {hit}/{len(targets)}（exa，上限 {FULLTEXT_MAX_CHARS}）", flush=True)


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


def write_person_note(it: dict, corpus_rel: str | None,
                      touch_obs: bool = True,
                      obs_override: list[str] | None = None) -> Path:
    """人物页（独立开发大牛）：与项目页同构，但落在 30-人物/，供"学方法论"路线的调研消费。"""
    p = person_note_path(it)
    if obs_override is not None:
        obs = list(obs_override)
    else:
        obs = []
        if p.exists():
            m = re.search(r"## 观测历史\n\n(.*?)(\n## |\Z)", p.read_text(encoding="utf-8"), re.S)
            if m:
                obs = [ln for ln in m.group(1).strip().splitlines() if ln.startswith("|")][2:]
        row = (f"| {it['captured_at']} | {it['source_name']} | {metrics_line(it.get('metrics') or {})} "
               f"| {('[[{}]]'.format(corpus_rel[:-3]) if corpus_rel else '—')} |")
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
        obs = []
        if p.exists():
            m = re.search(r"## 观测历史\n\n(.*?)(\n## |\Z)", p.read_text(encoding="utf-8"), re.S)
            if m:
                obs = [ln for ln in m.group(1).strip().splitlines() if ln.startswith("|")][2:]
        row = (f"| {it['captured_at']} | {it['source_name']} | {metrics_line(it.get('metrics') or {})} "
               f"| {('[[{}]]'.format(corpus_rel[:-3]) if corpus_rel else '—')} |")
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
        obs = []
        if p.exists():
            m = re.search(r"## 观测历史\n\n(.*?)(\n## |\Z)", p.read_text(encoding="utf-8"), re.S)
            if m:
                obs = [ln for ln in m.group(1).strip().splitlines() if ln.startswith("|")][2:]
        row = (f"| {it['captured_at']} | {it['source_name']} | {metrics_line(it.get('metrics') or {})} "
               f"| {('[[{}]]'.format(corpus_rel[:-3]) if corpus_rel else '—')} |")
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
    args = ap.parse_args(argv)

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
           "slice_days": args.slice_days}
    day = now_cst().strftime("%Y-%m-%d")
    total_items = total_new = 0
    print(f"=== KB 采集 {run_id} · {len(chans)} 渠道 ===", flush=True)

    for ch in chans:
        t0 = time.time()
        adapter = ADAPTERS.get(ch.get("adapter") or "")
        if not adapter:
            log.channel(ch["id"], ch["name"], "error", 0, f"未知 adapter={ch.get('adapter')}", time.time() - t0)
            continue
        c = dict(ch)
        if args.days:
            c.setdefault("params", {})
            c["window_days"] = args.days
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
                          "rule_dropped": len(drop_sink)})
        print(f"=== 完成：{total_items} 条（新 {total_new}）· 运行记录 {out} ===")
    else:
        print(f"=== dry-run 完成：{total_items} 条（新 {total_new}）· 未写盘 ===")
    return 0 if not log.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
