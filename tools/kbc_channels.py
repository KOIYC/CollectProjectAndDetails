"""kbc_channels — 渠道层：15 个 adapter + 评论/正文 enricher + project_url 守卫。

从 kb_collect 拆出（采集器原 1600+ 行，adapter 与写页/管线耦合）：
  * 本模块只依赖 kb_common，不感知 note 渲染与运行管线 —— 渠道怎么取数、kb_collect 怎么写库，
    两头各自演化互不牵连；
  * kb_collect 以 facade 方式 re-export 本模块的名字，9 个既有调用点（backfill/reclassify/
    navfix/name_audit/moc/audit/analyze/healthcheck/render）的 import 不动；
  * 新增渠道 = 在这里加一个 `ad_*` + 注册进 ADAPTERS，再在 channels.yaml 登记一行。
"""
from __future__ import annotations

import html
import json
import re
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

from kb_common import (CST, FULLTEXT_MAX_CHARS, FetchError, UNCLOSED_TAG_RE,  # noqa: F401 (FetchError 供调用方)
                       exa_fetch_texts, exa_search, http_get, http_json, is_project_ish,  # noqa: F401
                       iso, item_id_for, looks_summary, norm_url, now_cst, run_cli,  # noqa: F401
                       topic_of)

MAX_COMMENTS = 800
FULLTEXT_BUDGET = 14          # 每渠道最多补全多少条正文（外部取全文）


# ============================================================ text helpers

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"[ \t\u00a0]+")
NL_RE = re.compile(r"\n{3,}")
# 反斜杠也必须排除：Reddit 正文里的 markdown 转义链接形如
# `[https://www.producthunt.com/products/x?utm\_source=other](https://...)`，
# 不排除就会把 `?utm\_source=other` 整段抓下来，`norm_url` 再把 `\` 编码成 `%5C`
# 写进 project_url（实测 1 条 live 脏值，healthcheck ⑦ 报出）。
LINK_RE = re.compile(r"https?://[^\s<>\)\]\"'\\]+")


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

# 个人主页 / 平台资料页路径：是人不是项目站点（实测 liqi.io/creators: 撞车一例的根形态）
_PROFILE_PATH_RE = re.compile(
    r"/(?:creators?|u(?:sers?)?/[^/]*|profile|people/[^/]*|@[\w.-]+)/?(?:$|[?#])", re.I)


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
    # `www.` 前缀必须先去再比对：早先直接拿 netloc 比 NON_PROJECT_HOSTS，
    # `https://www.bilibili.com/video/...` / `https://www.producthunt.com/products/...`
    # 这类带 www 的讨论页/聚合站**全部放行**（实测 5/5 漏网），于是被当成项目官网
    # 写进 project_url（项目页文件名 + 跨渠道归并键），healthcheck ⑦ 的可疑值即此。
    bare = host.removeprefix("www.")
    if bare == "localhost" or re.match(r"^\d{1,3}(?:\.\d{1,3}){3}$", bare):
        return "本机地址"
    if "." not in bare:
        return "无顶级域"
    if bare in NON_PROJECT_HOSTS:
        return "讨论页/聚合站/文档站"
    if bare.endswith(".blogspot.com"):
        return "博客托管站"
    if PROJECT_URL_BAD_TAIL.search(u):
        return "尾部有标点（半截链接）"
    if _PROJECT_URL_ASSET.search(sp.path):
        return "静态资源链接（不是站点）"
    if _PROFILE_PATH_RE.search(sp.path):
        return "个人主页/平台资料页（不是项目站点）"
    if bare in GENERIC_BARE_HOSTS and not sp.path.strip("/"):
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


# --------------------------------------------------- 显式窗口（--since/--until）与节流

def _pub_ts(s) -> int | None:
    """published_at 字段 → epoch 秒（宽松解析；解析不了返回 None）。"""
    if not s:
        return None
    t = str(s).strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(t)
    except ValueError:
        try:
            dt = datetime.fromisoformat(t[:10])
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=CST)
    return int(dt.timestamp())


def filter_published(items: list[dict], since_ts: int | None = None,
                     until_ts: int | None = None) -> tuple[list[dict], int]:
    """按 published_at 裁剪（--since/--until 的通用落点）。

    无发布时间的条目**不丢**：缺时间属数据缺口（回填/审计会追），窗口判定丢它
    只会让缺口更大、还披着「过滤正常」的外衣。
    """
    if not since_ts and not until_ts:
        return items, 0
    kept, dropped = [], 0
    for it in items:
        ts = _pub_ts(it.get("published_at"))
        if ts is None:
            kept.append(it)
            continue
        if (since_ts and ts < since_ts) or (until_ts and ts > until_ts):
            dropped += 1
            continue
        kept.append(it)
    return kept, dropped


def polite(ctx) -> None:
    """评论抓取节流（--throttle-ms，默认 25ms/请求）：对上游 API 的礼貌下限。"""
    ms = int((ctx or {}).get("throttle_ms") or 0)
    if ms > 0:
        time.sleep(ms / 1000.0)


# ============================================================ adapters

def ad_hn_show(ch, ctx) -> tuple[list[dict], str, str]:
    """HN 渠道（adapter 复用）：params.tags 决定取 Show HN 还是首页 front_page。"""
    p = ch.get("params") or {}
    tags = p.get("tags") or "show_hn"
    days = int(p.get("window_days") or ch.get("window_days") or 3)
    limit = int(ch.get("limit") or 50)
    minp = int(p.get("min_points") or 1)
    since = int((now_cst() - timedelta(days=days)).timestamp())
    nf = f"points>={minp},created_at_i>{since}"
    if ctx.get("until_ts"):
        nf += f",created_at_i<{int(ctx['until_ts'])}"
    url = (f"https://hn.algolia.com/api/v1/search_by_date?tags={urllib.parse.quote(tags)}"
           f"&hitsPerPage={limit}&numericFilters={urllib.parse.quote(nf)}")
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
        polite(ctx)
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
    if ctx.get("since_ts"):
        after_ts = min(after_ts, int(ctx["since_ts"]))
    if ctx.get("until_ts"):
        before_ts = min(before_ts, int(ctx["until_ts"]))
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
            polite(ctx)
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
        polite(ctx)
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
    if ctx.get("since_ts"):
        cutoff = max(cutoff, datetime.fromtimestamp(int(ctx["since_ts"]), tz=now_cst().tzinfo))
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
        polite(ctx)
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
