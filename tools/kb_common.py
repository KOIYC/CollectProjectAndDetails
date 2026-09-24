"""kb_common — 独立开发项目知识库（KB）共享底座。

零第三方依赖（本机 PyPI 不可达）：只用 stdlib。
职责：路径常量、HTTP/CLI 取数、slug/frontmatter、去重账本(seen)、运行记录、原始归档写盘。
"""
from __future__ import annotations

import contextlib
import gzip as gzip_lib
import hashlib
import html as html_lib
import itertools
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.error
import zlib
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIR_INDEX = ROOT / "00-索引"
# 00-索引/ 分两层：根目录只放**导航**（浏览/字段字典/渠道台账/待办/运行日志），
# 生成物（洞察/审计/分析/重判）进 00-索引/报告/。
# 为什么分：索引目录一旦被带时间戳的报告淹没，它就不再是索引 —— 用户找不到入口。
DIR_REPORT = DIR_INDEX / "报告"
DIR_PROJECTS = ROOT / "10-项目"
DIR_CORPUS = ROOT / "20-语料"
DIR_PEOPLE = ROOT / "30-人物"
DIR_METHOD = ROOT / "40-方法论"
DIR_CHANNELS = ROOT / "50-渠道"
DIR_RAW = ROOT / "90-原始"
META = ROOT / "_meta"
RUNS = META / "runs"

ALL_DIRS = [DIR_INDEX, DIR_REPORT, DIR_PROJECTS, DIR_CORPUS, DIR_PEOPLE, DIR_METHOD,
            DIR_CHANNELS, DIR_RAW, META, RUNS]

CST = timezone(timedelta(hours=8))
BODY_MIN = 120                # 「有效正文」长度门槛（分析器/回填/正文缓存共用同一定义）
BODY_SNIPPET = 200            # 低于此长度视为「片段」，不足以做深度分析
FULLTEXT_MAX_CHARS = 40000    # Exa web_fetch 单次取正文上限（原 8000 会砍断长文）

# 「这不是全文」的尾部痕迹：RSS 摘要、Read more、未闭合的 HTML 标签、省略号
SUMMARY_TAIL_RE = re.compile(
    r"点击查看全文|查看全文|阅读全文|阅读原文|Read\s*more|Continue\s*reading"
    r"|target=\"_blank\"|</a>\s*$|\s\.\.\.\s*$|…\s*$", re.I)
UNCLOSED_TAG_RE = re.compile(r"<[^>]*$")


def looks_summary(body: str) -> bool:
    """正文是否带「摘要/残文」痕迹（不是全文）。"""
    return bool(body) and bool(SUMMARY_TAIL_RE.search(body))


LEGACY_EXA_CAP = 8000          # FULLTEXT_MAX_CHARS 改 40000 之前的历史上限
# 句子还没写完的样子：末尾停在字母/数字/汉字/逗号上，而不是句末标点
_UNFINISHED_RE = re.compile(r"[A-Za-z0-9\u4e00-\u9fff,;:、，；：]$")


def truncated_at_cap(body: str) -> bool:
    """是否被 Exa 正文上限截断（含**历史** 8000 与**现行** FULLTEXT_MAX_CHARS）。

    为什么需要这个探测：`extra.body_truncated` 是新加的标记，规则上线**之前**被砍的
    那批条目身上没有它，而它们的正文长度（8000）又足以骗过「够长就算完整」的判断 ——
    结果它们被判成 full、永远不进回填队列（实测 14 条长期滞留）。
    上限从 8000 提到 40000 之后同理：40000 字的长文同样是「只拿到开头」，
    少了这一档就会把 10 条截断正文当全文。
    长度贴住上限 **且** 结尾像话没说完，才算截断：单看长度会误伤恰好贴上限的完整长文。
    """
    if not body:
        return False
    tail_unfinished = bool(_UNFINISHED_RE.search(body.rstrip()))
    return tail_unfinished and any(abs(len(body) - cap) <= 60
                                  for cap in (LEGACY_EXA_CAP, FULLTEXT_MAX_CHARS))


def body_completeness(body: str, extra: dict | None = None, layer: str = "corpus") -> str:
    """正文完整度分级 —— 让下游能区分「这是全文」与「这只是开头」。

    metadata_only 只有元数据（信号层渠道，如 App Store 榜单 / B站视频简介）
    empty         有语料位但正文为空
    snippet       正文存在但过短（< BODY_SNIPPET）
    summary       RSS 摘要 / 带 Read more 痕迹 / 抓取时被上限截断
    full          可用作深度分析的正文
    """
    extra = extra or {}
    body = body or ""
    if layer == "signal":
        return "metadata_only"
    if not body.strip():
        return "empty"
    if extra.get("body_truncated") or looks_summary(body) or truncated_at_cap(body):
        return "summary"
    if len(body) < BODY_SNIPPET:
        return "snippet"
    return "full"


# ---------------------------------------------------------------- 赛道标签

# 放在 kb_common 而不是 kb_insight：采集端（kb_collect 写语料页时挂赛道导航）
# 与洞察端（kb_insight 统计赛道分布）都要用，必须共用一份定义。
# 若让 kb_collect 去 import kb_insight，会形成
# kb_collect → kb_insight → kb_content_audit → kb_collect 的循环导入。
# 顺序有意义：先判具体品类，再判泛品类。每条语料取第一个命中的类别。
TOPICS: list[tuple[str, str]] = [
    ("AI 工具/Agent", r"\bAi\b|LLM|GPT|agent|MCP|copilot|prompt|生成式|大模型|智能体|"
                      r"chat\s*bot|chatbot|embedding|RAG|fine[-\s]?tun"),
    ("开发者工具", r"\bdevtool|developer\s+tool|CLI|SDK|API|IDE|编辑器|debug|observab|"
                   r"monitor|日志|部署|deploy|CI/CD|测试|test\s+harness|code\s+review"),
    ("SaaS/B2B", r"\bSaaS\b|\bB2B\b|CRM|ERP|invoice|billing|payroll|HR\s+tool|"
                 r"dashboard|analytics|报表|团队协作|workflow|automation"),
    ("电商/独立站", r"e[-\s]?commerce|shopify|独立站|跨境电商|DTC|storefront|"
                    r"收款|支付|payment|checkout"),
    ("内容/媒体", r"newsletter|podcast|播客|博客|blog|"
                  r"内容创作|自媒体|视频创作|写作|writing"),
    ("教育/学习", r"学习|课程|education|course|tutor|tutorial|笔记|note[-\s]?taking|"
                  r"考试|刷题"),
    ("健康/生活", r"健康|健身|睡眠|饮食|冥想|habit|journal|日记|记账|habit\s+track"),
    ("游戏", r"游戏|game|gaming|steam|unity|godot|roguelike|pixel\s+art|indie\s+game"),
    ("移动 App", r"\bApp\b|iOS|Android|mobile|小程序|微信|PWA"),
    ("浏览器扩展", r"chrome\s+extension|浏览器扩展|browser\s+extension|userscript|油猴"),
]
TOPIC_RES = [(name, re.compile(pat, re.I)) for name, pat in TOPICS]


def topic_of(rec: dict) -> str:
    """给一条语料打赛道标签（第一个命中者；都不命中 → 未分类）。"""
    text = f"{rec.get('title') or ''}\n{(rec.get('body') or '')[:4000]}"
    for name, rx in TOPIC_RES:
        if rx.search(text):
            return name
    return "未分类"


# ---------------------------------------------------------------- 项目准入（实体页判据）
#
# 定义在 kb_common 而不是 kb_content_audit：**采集端 kb_collect 也要用**
# （决定要不要给这条建 `10-项目/` 页面），而 kb_content_audit 反向 import kb_collect，
# 放那边就成环。这里共用一份，避免两头判据漂移。

PROJECT_BY_CONSTRUCTION: set[str] = {
    "producthunt",      # 只收已发布产品
    "indiehackers",     # IH 产品库，天然是项目
    "betalist",         # 只收未发布创业项目
    "uneed",            # 同类发布站
}

# 非契约渠道但标题自带「这是我自己做的东西」声明 → 等同契约型
SELF_LAUNCH_PREFIX = re.compile(
    r"^\s*(?:Show\s+HN|Launch\s+HN|Show\s+IH|"
    r"I\s+(?:built|made|shipped|launched|created|released)|"
    r"we\s+(?:built|made|shipped|launched)|"
    r"my\s+(?:new\s+)?(?:saas|app|side\s+project|startup)|"
    r"(?:我们|我)(?:做了|开发了|上线了))\b", re.I)


def is_project_ish(rec: dict) -> str | None:
    """这条语料**是不是一个项目**（而不是一篇讨论/提问/经验贴）。返回命中理由或 None。

    用途一：采集端决定要不要建 `10-项目/` 实体页（kb_collect）。
    用途二：审计端判「无项目信号」（kb_content_audit）。

    为什么需要它：实体页原本对**每个条目**都建 —— 于是 reddit 的提问帖、心得帖
    也会有「项目页」，实测 818 个页面里混进 115 个废页。判据必须统一，否则两头漂移。

    为什么先按 kind 短路：`kind` 是**语义**归属（person/method/project 由数据源侧声明），
    其他判据（project_url / 契约渠道 / 自述前缀）是**证据**。让证据覆盖语义会把
    「独立开发者的收入复盘」错分到 `10-项目/`（实测 c1c7 kind=method 15 条即如此）——
    语义明确时直接返回 None，剩下的再谈证据。
    """
    kind = (rec.get("kind") or "").lower()
    if kind in ("person", "method"):
        return None
    if kind == "project":
        return "kind=project"
    if rec.get("project_url"):
        return "有项目外链"
    if rec.get("source_id") in PROJECT_BY_CONSTRUCTION:
        return "契约型渠道"
    if SELF_LAUNCH_PREFIX.search(rec.get("title") or ""):
        return "标题自述自建"
    return None

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

PY = sys.executable


def now_cst() -> datetime:
    return datetime.now(CST)


def iso(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    return dt.astimezone(CST).replace(microsecond=0).isoformat()


# ---------------------------------------------------------------- 发布日归一化
#
# 为什么必须有这一层：`pub_day` 是 B1 时间轴（Bases groupBy）与所有趋势分析的分组键，
# 而它一直由 `(published_at or "")[:10]` 裸切产生。published_at 却不是单一格式：
#   ISO8601   2026-09-20T09:23:24+08:00   （多数渠道）
#   RFC822    Thu, 17 Sep 2026 10:00:00 +0800（sspai 等 RSS feed）
#   字面量     "N/A"                        （exa_discovery 等）
# 裸切 RFC822 得到 `Thu, 17 Se`，裸切 "N/A" 得到 `N/A` —— 两者都会写进 frontmatter，
# 变成 Bases 视图里的一个独立分组、并且永远排不进时间序（实测：sspai 60 条 +
# exa_discovery 6 条掉出时间轴）。这是典型的 metadata-borne defect：
# 载荷本身完好，只有 lineage/时间语义被破坏，且不报错。
_RFC822_RE = re.compile(r"^[A-Za-z]{3},\s+\d{1,2}\s+[A-Za-z]{3}\s+\d{4}")


def pub_day_of(value: str | None) -> str | None:
    """把任意渠道给出的发布时间归一成 `YYYY-MM-DD`（拿不到就 None，不猜）。

    返回 None 表示「这个渠道没有提供可用的发布日」——调用方应当写 `None` 而不是写
    垃圾串，让「无发布日」在 frontmatter 里显式为缺失，而不是变成一个假分组。
    """
    if not value or not isinstance(value, str):
        return None
    v = value.strip()
    if not v or v.upper() in {"N/A", "NA", "NONE", "NULL", "-"}:
        return None
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", v)                    # ISO8601 / date
    if m:
        return m.group(1)
    if _RFC822_RE.match(v):                                     # RFC822 / RFC2822
        try:
            from email.utils import parsedate_to_datetime
            return parsedate_to_datetime(v).strftime("%Y-%m-%d")
        except Exception:                                      # noqa: BLE001
            return None
    m = re.match(r"^(\d{4})/(\d{1,2})/(\d{1,2})", v)            # 2026/09/17
    if m:
        return "%04d-%02d-%02d" % (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None


def ensure_dirs() -> None:
    for d in ALL_DIRS:
        d.mkdir(parents=True, exist_ok=True)
    (DIR_CORPUS / "posts").mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------- slug / name

# Windows 非法字符 + **Obsidian wikilink 语法字符** `[ ] # ^` + 反引号。
# 后三类虽在 Windows 上合法，但都会破坏链接层：
#   `[ ] # ^` —— wikilink 语法字符（`#`=标题锚点、`]`=链接收尾），谁引用谁断链（实测 13 文件 → 20 死链）；
#   `` ` ``   —— healthcheck 的 LINK_JUNK 把含它的链接当「正文伪代码」跳过 → 断链检查盲区。
# 改这里会影响 slugify 输出 → 存量同名文件会触发路径漂移（invariant ⑤），必须紧跟
# `kb_navfix --fix-names`（按记录反算规范名，带 manifest/seen 同步/链接改写）。
_BAD = re.compile(r'[<>:"/\\|?*\x00-\x1f\[\]#^`]')
_WS = re.compile(r"\s+")
_DASH = re.compile(r"-{2,}")


def slugify(text: str, maxlen: int = 60) -> str:
    """安全文件名：保留中英文，剔除 Windows 非法字符与 wikilink 语法字符。"""
    text = unicodedata.normalize("NFKC", text or "").strip()
    text = _BAD.sub(" ", text)
    text = _WS.sub("-", text)
    text = _DASH.sub("-", text)
    text = text.strip(" -.~")
    if not text:
        text = "untitled"
    if len(text) > maxlen:
        text = text[:maxlen].rstrip("-.~")
    return text


def sha1(text: str, n: int = 16) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:n]


_FENCE = re.compile(r"```.*?```", re.S)
_TICK = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    """抹掉围栏代码块与行内代码，位置用等长空白占位（保持偏移量）。

    用途：扫 wikilink 前先摘掉代码。TOML/JSON 片段里的 `[[tool.ty.overrides]]`、
    文档里的 `[[agents]]` 都是**正文内容**，不是链接 —— 不摘就会被当成断链（实测 7 处假警报）。
    """
    def blank(m: re.Match) -> str:
        return re.sub(r"[^\n]", " ", m.group(0))

    return _TICK.sub(blank, _FENCE.sub(blank, text))


def norm_url(url: str | None) -> str:
    """规范化 URL 作为去重键：去 utm/尾部斜杠/www/协议差异。"""
    if not url:
        return ""
    u = url.strip()
    u = re.sub(r"^http://", "https://", u)
    try:
        p = urllib.parse.urlsplit(u)
    except ValueError:
        return u
    q = urllib.parse.parse_qsl(p.query, keep_blank_values=False)
    q = [(k, v) for k, v in q if not k.lower().startswith("utm_")
         and k.lower() not in {"ref", "fbclid", "gclid", "source"}]
    net = p.netloc.lower().removeprefix("www.")
    path = p.path.rstrip("/") or "/"
    return urllib.parse.urlunsplit((p.scheme, net, path,
                                    urllib.parse.urlencode(q), ""))


def item_id_for(url: str | None, title: str = "", source: str = "") -> str:
    key = norm_url(url)
    if not key:
        key = f"{source}:{title}"
    return sha1(key, 16)


# ---------------------------------------------------------------- http helpers


class FetchError(Exception):
    def __init__(self, status, msg):
        super().__init__(f"{status}: {msg}")
        self.status = status
        self.msg = msg


def http_get(url, headers=None, timeout=25, retries=2, backoff=1.5) -> bytes:
    hdr = {"User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}
    if headers:
        hdr.update(headers)
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=hdr)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = FetchError(e.code, e.reason)
            if e.code in (403, 404, 410, 451):
                break
        except Exception as e:                                    # noqa: BLE001
            last = FetchError("ERR", str(e)[:160])
        if i < retries:
            time.sleep(backoff * (i + 1))
    raise last or FetchError("ERR", "unknown")


def http_json(url, headers=None, timeout=25, retries=2):
    return json.loads(http_get(url, headers, timeout, retries).decode("utf-8", "replace"))


_CLI_CACHE: dict[str, str] = {}


def which_cli(name: str) -> str | None:
    """解析 CLI 可执行文件绝对路径。

    必须做这一步：npm 生成的**无扩展名 sh shim**（mcporter / opencli）在
    CreateProcess 下 not-found，只有 `.cmd` 变体可执行（本机实测 2026-09-20）。
    """
    if name in _CLI_CACHE:
        return _CLI_CACHE[name] or None
    exts = [e for e in (os.environ.get("PATHEXT", "").split(os.pathsep)) if e] or \
           [".COM", ".EXE", ".BAT", ".CMD"]
    dirs = [d for d in os.environ.get("PATH", "").split(os.pathsep) if d]
    dirs += [r"C:\Users\yangcan\AppData\Roaming\npm", r"C:\Program Files\GitHub CLI",
             r"C:\Program Files\nodejs", str(Path.home() / "AppData/Roaming/npm")]
    for d in dirs:
        for ext in exts + [""]:
            cand = Path(d) / f"{name}{ext}"
            if cand.is_file():
                _CLI_CACHE[name] = str(cand)
                return str(cand)
        for ext in (".cmd", ".exe", ".bat"):
            cand = Path(d) / f"{name}{ext}"
            if cand.is_file():
                _CLI_CACHE[name] = str(cand)
                return str(cand)
    _CLI_CACHE[name] = ""
    return None


def run_cli(args: list[str], timeout=90, env=None, input_text=None) -> tuple[int, str, str]:
    """跑外部 CLI（gh / mcporter / opencli / bili）。返回 (code, stdout, stderr)。"""
    e = dict(os.environ)
    e["PYTHONUTF8"] = "1"
    if env:
        e.update(env)
    argv = list(args)
    resolved = which_cli(argv[0])
    if resolved:
        argv[0] = resolved
    try:
        p = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout, env=e, input=input_text,
                           shell=False)
        return p.returncode, p.stdout or "", p.stderr or ""
    except FileNotFoundError:
        return 127, "", "not-found"
    except subprocess.TimeoutExpired:
        return 124, "", f"timeout>{timeout}s"


def jina_read(url: str, timeout=45) -> str:
    """Jina Reader —— 2026-09-20 实测本网络不可用（Tunnel 502 / HTTP 000）。

    保留仅为兼容调用点；正文取数一律走 exa_fetch_texts。
    """
    return http_get(f"https://r.jina.ai/{url}", timeout=timeout, retries=0).decode("utf-8", "replace")


def exa_fetch_texts(urls: list[str], max_chars=8000, timeout=180) -> dict[str, str]:
    """用 Exa web_fetch 批量取正文（本机唯一可用的通用网页正文后端）。

    返回 {url: text}；解析失败返回 {}（调用方按“未取到正文”处理，不静默伪造）。
    """
    out_all: dict[str, str] = {}
    for i in range(0, len(urls), 4):
        chunk = urls[i:i + 4]
        args = ", ".join(json.dumps(u) for u in chunk)
        code, out, _err = run_cli(
            ["mcporter", "call",
             f"exa.web_fetch_exa(urls: [{args}], maxCharacters: {max_chars})"],
            timeout=timeout)
        # 注意：批内任一 URL 抓取失败时 mcporter 会返回非 0，但成功的 URL 仍在 stdout。
        # 所以这里不因返回码丢弃输出（2026-09-20 实测 PH 抓取失败、IH 成功同批出现）。
        if not out.strip():
            # 后端整体失败 ≠「这条没有正文」，必须响亮报出来。否则调用方只看到 {} →
            # 当成无正文静默跳过：2026-09-21 实测 Exa 免费额度打满返 429，backfill
            # 12 批全 0/12，而报告只显示「回填 8/150」，看不出是后端挂了。
            low = (_err or "").lower()
            hint = ("【Exa 免费额度已打满（429）】本轮正文补全全部无效 —— 需自备 API key 或等限流重置"
                    if ("429" in low or "rate limit" in low) else
                    "exa web_fetch 空返回（后端不可用？）")
            tail = (_err or "").strip().splitlines()
            print(f"[!] {hint}（code={code}）" + (f"：{tail[-1][:160]}" if tail else ""), flush=True)
            continue
        parts = re.split(r"(?m)^URL:\s*(\S+)\s*$", out)
        for j in range(1, len(parts) - 1, 2):
            url = parts[j].strip()
            text = parts[j + 1].strip()
            if text and not text.startswith("Error fetching"):
                out_all[url] = text
    return out_all


DIRECT_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
             "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
# 本网络实测不可直取的主机（Tunnel 502 / 连接超时）—— 命中即跳过，别白等超时。
# 只登记**反复验证过**的；一次性失败不写这里（可能是临时抖动）。
DIRECT_BLOCKED_HOSTS = {"news.ycombinator.com", "github.com"}
_direct_host_fail: set[str] = set()

# 连接级失败（整台主机都不通）才拉黑。HTTP 状态错误**不是**主机级问题：
# 单条 404 说明「这个页面没了」，同主机其它页面照样能取。
# 实测 bug（2026-09-21）：`urllib.error.HTTPError` 是 `URLError` 的子类，
# 旧判据 `isinstance(e, URLError)` 于是把一次 404 当成主机不可达 →
# betalist.com 整站被本轮拉黑，后续 55 条白等（本轮探针里 6 条只取到 5 条即此因）。
_CONN_ERR_KINDS = ("timed out", "timeout", "tunnel", "connection", "reset", "refused",
                   "unreachable", "getaddrinfo", "ssl", "eof")


def host_of(url: str) -> str:
    return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")


def _probe_one(u: str, timeout: int) -> tuple[str, str, int | str, str]:
    """单 URL 直取 → (url, 文本, 状态, 失败种类)。

    状态语义（供死信账本结构化记账用，见 kb_backfill 的 reason_code）：
      200           取到
      403/404/410/451  服务端明确拒绝/不存在（**页面级**，与主机无关）
      "blocked"     在 DIRECT_BLOCKED_HOSTS / 本轮已拉黑的主机
      "timeout" / "unreachable"  连接级失败
      "nontext"     Content-Type 不是可读文本（视频/二进制）
    """
    try:
        req = urllib.request.Request(u, headers={
            "User-Agent": DIRECT_UA,
            "Accept": "text/html,application/xhtml+xml,text/plain;q=0.9,*/*;q=0.8",
            "Accept-Language": "en,zh-CN;q=0.8",
            "Accept-Encoding": "gzip, deflate",
        })
        with urllib.request.urlopen(req, timeout=timeout) as r:
            if r.status != 200:
                return u, "", int(r.status), "http"
            ctype = (r.headers.get("Content-Type") or "").lower()
            if ctype and not ("html" in ctype or "text" in ctype or "json" in ctype):
                return u, "", 200, "nontext"
            raw = r.read(800_000)
    except urllib.error.HTTPError as e:
        # HTTPError 必须**先于** URLError 捕获（它是子类），否则 404 会被当成主机级故障。
        return u, "", int(e.code), "http"
    except Exception as e:                                          # noqa: BLE001
        msg = str(e).lower()
        kind = "timeout" if ("timed out" in msg or "timeout" in msg) else \
            ("unreachable" if any(k in msg for k in _CONN_ERR_KINDS) else "error")
        if kind in ("timeout", "unreachable"):
            h = host_of(u)
            if h not in _direct_host_fail:
                print(f"    [i] 直取拉黑主机 {h}（本轮不再重试）：{str(e)[:70]}", flush=True)
            _direct_host_fail.add(h)
        return u, "", kind, kind
    try:
        if raw[:2] == b"\x1f\x8b":                                # 服务端没给头但确实是 gzip
            raw = gzip_lib.decompress(raw)
        m = re.search(rb'charset=["\']?([\w-]+)', raw[:2048], re.I)
        cs = m.group(1).decode("ascii", "replace").lower() if m else "utf-8"
        if cs in {"gb2312", "gbk", "gb18030", "big5"}:            # 国内源常见，别按 utf-8 硬解
            return u, raw.decode(cs, "replace"), 200, ""
        return u, raw.decode("utf-8", "replace"), 200, ""
    except Exception:                                             # noqa: BLE001
        return u, "", 200, "decode"


def html_to_text(html: str) -> str:
    """极简 HTML → 纯文本（stdlib only）：去 script/style/标签、反转义、压空白。

    为什么不用第三方：本机 PyPI 不可达（见铁律 1）。Exa / Jina 都曾是我们唯一的正文后端，
    但 2026-09-21 实测**直连 urllib 也能拿到正文**（6/6 project 页 7k~21k 字符），
    只有 news.ycombinator.com 走 Tunnel 502。故补一个零依赖后端，正文不再被 Exa 额度卡死。
    """
    s = re.sub(r"(?is)<(script|style|noscript|svg|head)[\s\S]*?</\1>", " ", html)
    s = re.sub(r"(?is)<!--[\s\S]*?-->", " ", s)
    s = re.sub(r"(?is)<br\s*/?>|</(p|div|li|h[1-6]|tr)>", "\n", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html_lib.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    s = re.sub(r"\n\s*\n\s*", "\n", s)
    return s.strip()


def direct_fetch_texts(urls: list[str], max_chars=8000, timeout=12, workers=4,
                       status_out: dict | None = None) -> dict[str, str]:
    """用 stdlib urllib 直取页面正文（零依赖、无额度限制）。

    返回 {url: text}；失败/过短的 URL 直接不出现在结果里（调用方据此决定是否回退 Exa）。
    不做任何「伪造正文」：拿不到就是拿不到。

    `status_out`：可选输出字典，逐条填 url → 状态（200 / 403 / 404 / "blocked" /
    "timeout" / "unreachable" / "nontext"）。**为什么必须有**：死信账本此前只记一句
    自然语言理由，无法回答「为什么判死」——账本声称 66 条 github 死信可救，实际只救回 6 条，
    因为「死的时候用的是哪个 URL、后端到底报了什么」根本没记（见 2026-09-21 调研报告 §4.2）。
    """
    out: dict[str, str] = {}
    todo: list[str] = []
    for u in urls:
        if not u or not u.startswith("http"):
            if status_out is not None and u:
                status_out[u] = "bad_url"
            continue
        host = host_of(u)
        if host in DIRECT_BLOCKED_HOSTS or host in _direct_host_fail:
            if status_out is not None:
                status_out[u] = "blocked"
            continue
        todo.append(u)
    if not todo:
        return out

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(min(workers, len(todo))) as ex:
        # 异常必须在这里吞掉：ThreadPoolExecutor.map 会在**迭代时**抛出，
        # 一个 502 会炸掉整批（2026-09-21 实测：HN 页面 502 让整批 12 条全废）。
        # _probe_one 内部已 try/except 全包，返回状态而不是抛。
        for u, raw_html, status, _kind in ex.map(lambda x: _probe_one(x, timeout), todo):
            if status_out is not None:
                status_out[u] = status
            if not raw_html:
                continue
            txt = html_to_text(raw_html)
            if len(txt) >= 100:
                out[u] = txt[:max_chars]
            elif status_out is not None:
                status_out[u] = f"{status}:too_short"
    return out


def direct_probe(url: str, timeout: int = 15) -> tuple[int | str, str]:
    """单 URL 直取 → (状态, 文本)。给「按状态分类死信」的小批量场景用（见 kb_backfill）。"""
    _u, txt, status, _kind = _probe_one(url, timeout)
    return status, txt


def exa_search(query: str, n=10, timeout=120) -> list[dict]:
    code, out, err = run_cli(["mcporter", "call", f"exa.web_search_exa(query: {query!r}, numResults: {n})"],
                             timeout=timeout)
    if code != 0:
        return []
    return _parse_mcporter_text(out)


def exa_fetch(urls: list[str], max_chars=6000, timeout=150) -> str:
    args = ", ".join(f'"{u}"' for u in urls)
    code, out, err = run_cli(["mcporter", "call",
                              f"exa.web_fetch_exa(urls: [{args}], maxCharacters: {max_chars})"],
                             timeout=timeout)
    return out if code == 0 else ""


def _parse_mcporter_text(out: str) -> list[dict]:
    """mcporter 文本输出 → [{title,url,published,text}]。宽松解析，失败返回 []。"""
    blocks = re.split(r"\n(?=Title: )", out)
    rows = []
    for b in blocks:
        t = re.search(r"^Title:\s*(.+)$", b, re.M)
        u = re.search(r"^URL:\s*(\S+)", b, re.M)
        d = re.search(r"^Published:\s*(\S+)", b, re.M)
        if u:
            rows.append({"title": (t.group(1).strip() if t else ""),
                         "url": u.group(1).strip(),
                         "published": (d.group(1) if d else None),
                         "text": b.strip()[:20000]})
    return rows


# ------------------------------------------------- 注册表解析（channels.yaml 子集）
# 从 kb_collect 迁入：解析器是**基础设施**（analyze/audit/content_audit/prune/backfill 都
# 要读注册表），原先放在采集器里，其他工具只能反向 import kb_collect —— 层向错了。

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
        if val in (">-", ">", ">+", "|-", "|", "|+"):
            # YAML 折叠/字面标量：`>-`（折叠成空格）/ `|`（保留换行）。
            # 不支持这两种写法时，多行的 note 会被逐行当成 `key: value` 解析 ——
            # 正文里的 `https://x.com` 会切成 `解锁 = 开 Chrome 登录 https` 这样的**伪键**
            # 塞进注册表（2026-09-24 实测 twitter / xiaohongshu 两个渠道各中招）。
            # 折叠标量在原文件里是「本行 val 为 `>-`，后续更深缩进的行都是正文」，照此还原。
            buf: list[str] = []
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    buf.append("")
                    i += 1
                    continue
                if nxt.lstrip().startswith("#"):
                    break
                if len(nxt) - len(nxt.lstrip()) <= indent:
                    break
                buf.append(nxt.strip())
                i += 1
            while buf and buf[-1] == "":
                buf.pop()
            sep = "\n" if val.startswith("|") else " "
            parent[key] = sep.join(buf)
            continue
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


def load_registry(path: Path | None = None) -> dict:
    """读 _meta/channels.yaml 并挑出启用渠道（`_enabled_channels` 键）。"""
    p = path or (META / "channels.yaml")
    reg = load_channels_yaml(p)
    channels = [c for c in (reg.get("channels") or []) if c.get("enabled")]
    reg["_enabled_channels"] = channels
    return reg


# ---------------------------------------------------------------- 保留策略（_meta 轮转）
# 单日大改会产生 5+ 份 manifest、36+ 份 run 记录；_meta 是**工作区**不是归档——
# 轮转只留近期份额。第二份保险：_meta 自 2026-09-20 起整体入 git，删掉的都在历史里。


def rotate_files(directory: Path, prefix: str, keep: int) -> int:
    """同前缀只留最新 keep 份，删旧。返回删除数。

    排序按**文件名**而非 mtime：manifest 命名内嵌 YYYYMMDDTHHMMSS，字典序即时间序；
    mtime 会被任何后续 touch 改写（git checkout / 复制回放都会），紧密循环里分辨率也不够
    —— 实测 Windows 下自测 5 连写会保留错 3 份（2026-09-20 修复）。
    """
    files = sorted(directory.glob(f"{prefix}*"), key=lambda p: p.name, reverse=True)
    removed = 0
    for old in files[keep:]:
        try:
            old.unlink()
            removed += 1
        except OSError:
            pass
    return removed


def rotate_runs(keep: int = 80, directory: Path | None = None) -> int:
    """运行记录目录只留最新 keep 份（latest.json 永远保留）。"""
    d = directory or RUNS
    files = [p for p in d.glob("*.json") if p.name != "latest.json"]
    files.sort(key=lambda p: p.name, reverse=True)   # run_id 内嵌时间戳，字典序即时间序（同 rotate_files 的理由）
    removed = 0
    for old in files[keep:]:
        try:
            old.unlink()
            removed += 1
        except OSError:
            pass
    return removed


def rotate_jsonl(path: Path, keep: int = 4, max_bytes: int = 200_000) -> int:
    """单个追加型 JSONL 账本的分档轮转，返回移走的份数。

    为什么单独要一个函数：`rule_drops.jsonl` 只有一个文件、没有前缀族，`rotate_files`
    管不到它 —— 于是它成了 `_meta` 里唯一只增不减的账本（实测已 156KB，每天再涨）。
    轮转不删除历史：判废理由是「主题准入为什么把它筛掉」的分析线索，`.1`~`.keep` 留在
    `_meta/` 里可核对（git 已入库，等于第三份保险）。超阈值才转，避免每轮都动盘。
    """
    try:
        if not path.exists() or path.stat().st_size < max_bytes:
            return 0
    except OSError:
        return 0
    for i in range(keep, 1, -1):                               # .3 → .4，依次后移
        src = path.with_name(f"{path.name}.{i - 1}")
        if src.exists():
            try:
                os.replace(src, path.with_name(f"{path.name}.{i}"))
            except OSError:
                return i - 2
    os.replace(path, path.with_name(f"{path.name}.1"))
    path.write_text("", encoding="utf-8")
    return 1



# ---------------------------------------------------------------- stores


def note_bucket(seen, iid: str, fallback: str) -> str:
    """语料 note 原地刷新的分片日期：**以现存 note 路径为准**，不许搬家。

    为什么不能用「最新 raw 记录所在分片」的日期：backfill/update 记录追加进「今天」的
    raw 分片后，下一轮（或任何跨天重跑）会把该条目的 day 解析成回填日 → note 被当成
    新分片重建、旧文件成孤儿（实测 2026-09-21 零点连跑两轮 backfill → 45 个孤儿、
    healthcheck ① 红）。raw 分片日期 = 记录进账日，语料分片日期 = 条目首次落盘日，
    两者语义不同，必须各取各的。kb_collect 与 kb_backfill 的刷新写盘共用本函数。
    """
    note = str((seen.items.get(iid) or {}).get("note") or "")
    m = re.search(r"posts/[^/]+/(\d{4}-\d{2}-\d{2})/", note)
    return m.group(1) if m else fallback


def _load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:                                       # noqa: BLE001
        # 损坏隔离：原实现静默返回 default —— 账本坏了伪装成「第一次运行」，
        # seen/body_cache 一旦损坏就整库失忆（seen 失忆=全量重写页面；body_cache 失忆=
        # 重烧 Exa 额度），且没有任何告警。改名保留现场 + 响亮提示，调用方拿 default 重启。
        try:
            bak = path.with_name(f"{path.name}.corrupt-{now_cst():%Y%m%dT%H%M%S}.bak")
            path.rename(bak)
            print(f"[!] 状态文件损坏，已隔离：{path.name} → {bak.name}（{str(e)[:80]}）", flush=True)
        except OSError:
            print(f"[!] 状态文件损坏且无法隔离：{path.name}（{str(e)[:80]}）", flush=True)
        return default


_TMP_SEQ = itertools.count(1)
_REPLACE_RETRY_S = (0.2, 0.6, 1.5)


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # 临时名必须**唯一**（pid + 进程内序号）。原来固定 `x.json.tmp`：两个写者同时写同一
    # 账本时互相覆盖对方的 tmp，os.replace 之后盘上留下的是两份内容拼起来的半截文件。
    # 实测 2026-09-21 有会话与本库重跑时间重叠 —— 这类损坏不会报错，只会在
    # healthcheck ①/⑤ 表现成「盘账不平」，而两边日志各自都是绿的。
    tmp = path.with_name(f"{path.name}.{os.getpid()}.{next(_TMP_SEQ)}.tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    # os.replace 在 Windows 上会因目标被 AV/索引器/另一进程占用而抛 WinError 5
    # （kb_navfix 里已留过同类现场记录）。短暂退避重试；仍失败就抛给调用方计入
    # write_errors —— 写盘失败必须留痕，静默吞掉等于丢一整页。
    for i, wait in enumerate((0.0,) + _REPLACE_RETRY_S):
        try:
            os.replace(tmp, path)
            return
        except OSError:
            if i == len(_REPLACE_RETRY_S) or not tmp.exists():
                raise
            time.sleep(wait)


_LOCK_TIMEOUT_S = 25.0


@contextlib.contextmanager
def ledger_lock(target: Path, lock_name: str | None = None,
                timeout: float = _LOCK_TIMEOUT_S):
    """_meta 账本的跨进程互斥锁（stdlib：Windows 用 msvcrt，POSIX 用 fcntl）。

    为什么必须加：`Seen` / `BodyCache` / 死信账本全是「整读 → 改 → 整写」，没有锁。
    09:30 自动化与人工重跑（`kb_navfix --fix-names` 也读写 seen）时间重叠时后写覆盖前写，
    丢的是账本条目 —— 表现成「在盘不在账 / 在账不在盘」，而两边日志各自都绿。

    锁文件放在**目标旁边**而不是统一 _meta/：临时目录里的账本不该往真 _meta 留锁。
    带时间戳的 manifest 族传 `lock_name` 归并成一把族锁 —— 否则每写一份 manifest
    就多一个新锁文件，而轮转按前缀匹配、点前缀文件它扫不到。点前缀也让 Obsidian 不索引。

    超时行为：响亮告警后**照样写**。反过来（跳过写入）会把已取到的正文/账本更新永久丢掉，
    而冲突覆盖至少还能被 healthcheck ①/⑤ 抓到（同「退出码恒 0」的取舍：宁可留可观测的
    偏差，也不要不可观测的丢失）。
    """
    lock_path = target.with_name(f".{lock_name or target.name}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    fh, ok, waited = None, False, 0.0
    try:
        fh = open(lock_path, "a+b")
        try:
            import msvcrt                                      # Windows

            def _try():
                fh.seek(0)
                msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)

            def _un():
                fh.seek(0)
                msvcrt.locking(fh.fileno(), msvcrt.LK_UNLCK, 1)
        except ImportError:                                    # pragma: no cover - POSIX
            import fcntl                                       # noqa: F401

            def _try():
                fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)

            def _un():
                fcntl.flock(fh, fcntl.LOCK_UN)
        while True:
            try:
                _try()
                ok = True
                break
            except OSError:
                if waited >= timeout:
                    break
                time.sleep(0.25)
                waited += 0.25
        if not ok:
            print(f"[!] 账本锁等待超时 {timeout:.1f}s（{lock_name or target.name}）—— "
                  f"疑似有另一轮在跑，仍继续写入；收工时若 ①/⑤ 报红请先查并发", flush=True)
        yield ok
    finally:
        if fh is not None:
            if ok:
                try:
                    _un()
                except OSError:
                    pass
            fh.close()


def read_ledger(path: Path, default):
    """账本读盘 = 带损坏隔离的读（见 `_load_json`）。给 kb_backfill 的死信账本用。"""
    return _load_json(path, default)


def write_ledger(path: Path, payload: dict, lock_name: str | None = None,
                 indent: int = 0) -> None:
    """账本写盘 = 锁 + 原子替换。任何 _meta 状态文件都该走这里，不要自己 write_text。"""
    with ledger_lock(path, lock_name):
        _atomic_write(path, json.dumps(payload, ensure_ascii=False, indent=indent))



class Seen:
    """跨运行去重账本 + 观测历史 + 内容指纹（判定“无变化”以免重复写盘）。"""

    def __init__(self, path: Path | None = None):
        self.path = path or (META / "seen.json")
        d = _load_json(self.path, {"version": 1, "items": {}})
        self.items: dict = d.get("items", {})

    def get(self, iid: str):
        return self.items.get(iid)

    def content_hash(self, iid: str) -> str | None:
        rec = self.items.get(iid) or {}
        return rec.get("content_hash")

    def touch(self, iid: str, source: str, note_rel: str, metrics: dict | None = None,
              content_hash: str | None = None):
        # setdefault 逐个补，而不是一次性 setdefault 整条：采集端现在会**先**写 simhash
        # （在线近重复标注要在正文落盘前算），那时记录已经存在但缺 first_seen/seen_count。
        # 整条 setdefault 会把这些字段永久留空 → first_seen 丢失、seen_count 从 0 起跳。
        rec = self.items.setdefault(iid, {})
        rec.setdefault("first_seen", iso(now_cst()))
        rec.setdefault("seen_count", 0)
        rec.setdefault("source", source)
        rec.setdefault("note", note_rel)
        rec["last_seen"] = iso(now_cst())
        rec["seen_count"] = rec.get("seen_count", 0) + 1
        rec["note"] = note_rel
        if content_hash:
            rec["content_hash"] = content_hash
        if metrics:
            prev = (rec.get("metric_history") or [{}])[-1]
            changed = any(prev.get(k) != v for k, v in metrics.items() if v is not None)
            if rec.get("metric_history") and not changed:
                return False                                     # 指标没变，不追加历史点
            rec.setdefault("metric_history", []).append(
                {"at": iso(now_cst()), **{k: v for k, v in metrics.items() if v is not None}})
            rec["metric_history"] = rec["metric_history"][-40:]
            return True
        return False

    def save(self):
        with ledger_lock(self.path):
            _atomic_write(self.path, json.dumps(
                {"version": 1, "updated": iso(now_cst()), "items": self.items},
                ensure_ascii=False, indent=0))


class BodyCache:
    """正文缓存 —— 防止「空 body 覆盖历史正文」。

    根因（R3 实测）：采集窗口是滚动的，同一条目会反复回榜。某轮 readme/正文取数失败 →
    新记录 body 为空、captured_at 更晚 → `latest_by_item` 取到空版本，把上一轮（或
    kb_backfill 辛苦回填的）正文**抹掉**。表现就是「缺口修好了下一轮又出现」。

    规则：只增不减。本轮取到正文 → 写入/更新缓存；本轮没取到 → 从缓存继承，绝不清空。
    """

    def __init__(self, path: Path | None = None):
        self.path = path or (META / "body_cache.json")
        d = _load_json(self.path, {"version": 1, "items": {}})
        self.items: dict = d.get("items", {})
        self.dirty = False

    def get(self, iid: str) -> dict | None:
        return self.items.get(iid)

    def put(self, iid: str, body: str, source: str = "", url: str = "",
            body_format: str = "markdown") -> bool:
        """只在「更长」时更新，避免短摘要把长正文顶掉。"""
        if len(body or "") < BODY_MIN:
            return False
        cur = self.items.get(iid) or {}
        if len(cur.get("body") or "") >= len(body):
            return False
        self.items[iid] = {"body": body, "source": source, "url": url,
                           "body_format": body_format, "at": iso(now_cst())}
        self.dirty = True
        return True

    def prune_stale(self, seen_items: dict, keep_days: int = 120) -> int:
        """丢掉「滚动窗口再也够不到」的缓存条目，返回删除数（只增不减的缓存必须有个出口）。

        为什么取 120 天：本缓存唯一的职责是防「本轮空 body 覆盖历史正文」，而采集窗口最长
        90 天 —— 超过窗口仍未再观测的条目不可能再回榜覆盖，留着只会让 body_cache.json
        单调膨胀（实测 9.0MB，每渠道 + 每轮收尾各全量重序列化一次）。
        删了不丢数据：正文的事实源是不可变的 `90-原始/`，需要时从那里重建即可。
        判据用 seen 的 `last_seen`（账本口径），不用缓存自己的 `at`（那只记最后一次写入）。
        安全阀：账本明显比缓存小（seen 损坏被隔离重启、或拿了半截账本）时**不 prune** ——
        否则「账本空 + prune」= 一把清光缓存，把防覆盖的机制反过来变成大规模丢正文。
        """
        if len(seen_items) * 2 < len(self.items):
            print(f"[!] body_cache 清理跳过：账本仅 {len(seen_items)} 条而缓存 {len(self.items)} 条"
                  f"（先查 seen.json 是否损坏/被隔离，别在失忆状态下清缓存）", flush=True)
            return 0
        cutoff = now_cst() - timedelta(days=keep_days)
        stale = []
        for iid in self.items:
            rec = seen_items.get(iid) or {}
            last = rec.get("last_seen") or rec.get("first_seen") or ""
            try:
                seen_at = datetime.fromisoformat(last)
            except ValueError:                                  # 无账本记录 / 格式非法 → 够不到了
                stale.append(iid)
                continue
            if seen_at < cutoff:
                stale.append(iid)
        for iid in stale:
            self.items.pop(iid, None)
        if stale:
            self.dirty = True
        return len(stale)

    def save(self) -> None:
        if not self.dirty:
            return
        with ledger_lock(self.path):
            _atomic_write(self.path, json.dumps(
                {"version": 1, "updated": iso(now_cst()), "count": len(self.items),
                 "items": self.items}, ensure_ascii=False))


# --------------------------------------------------- JSONL 读写（一行一条的纪律）

# 为什么不能用 str.splitlines() 读 JSONL：
#   splitlines() 会按 U+2028 / U+2029 / \x85 / \x0b / \x0c 切分 —— 这些字符在 JSON
#   字符串里是**合法内容**（网页正文里很常见），出现在 body 里就会把一条记录切成碎片，
#   碎片 JSON 解析失败后被静默跳过。实测：v2ex 一条含 56 个 U+2028 的记录，它的 7 条
#   记录全部隐形 —— kb_healthcheck 报 raw=3072（真实 3079）、unique=823（真实 824），
#   kb_prune 的存量重判集也少了这一条（既不会被重判、也不会被归档）。
# 纪律：读 JSONL 一律 load_ndjson()；写 JSONL 一律 append_jsonl()（内含 sanitize_record）。
_LINE_SEP_CHARS = {0x2028: "\n", 0x2029: "\n", 0x85: "\n", 0x0B: "\n", 0x0C: "\n"}


def normalize_line_seps(text: str | None) -> str:
    """把 JSON 合法、但会骗过 splitlines() 的行分隔符归一成 `\\n`。"""
    return (text or "").translate(_LINE_SEP_CHARS)


def sanitize_record(rec: dict) -> dict:
    """写盘前清洗文本字段（就地修改并返回）。

    只做一件事：标题 / 正文 / 评论正文里的 U+2028 类行分隔符 → `\\n`。
    为什么必须在**写入侧**做：90-原始 是只追加的事实源，历史记录改不了；
    新记录再带这个字符，就是在给每个读 JSONL 的下游埋一颗「静默丢条」的地雷。
    """
    for k in ("title", "body"):
        if isinstance(rec.get(k), str):
            rec[k] = normalize_line_seps(rec[k])
    for c in (rec.get("comments") or []):
        if isinstance(c, dict) and isinstance(c.get("text"), str):
            c["text"] = normalize_line_seps(c["text"])
    return rec


def load_ndjson(path: Path) -> list[dict]:
    """按 `\\n` 切分读 JSONL —— 唯一正确的读法（见上面 _LINE_SEP_CHARS 的注释）。

    坏行必须**报数**，不能静默 `continue`：`90-原始/` 是唯一事实源、只追加不可变，
    一行解析失败就是一条条目从所有下游统计里隐形（存量重判、洞察、① 计数都会少算，
    而 healthcheck 拿的是同一份读法 → 一路报绿）。真出现坏行时先查是否被截断写盘。
    """
    out: list[dict] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return out
    bad = 0
    for ln in text.split("\n"):
        ln = ln.strip()
        if not ln:
            continue
        try:
            out.append(json.loads(ln))
        except json.JSONDecodeError:
            bad += 1
    if bad:
        print(f"[!] JSONL 有 {bad} 行解析失败被跳过：{path.name}"
              f"（唯一事实源里的坏行=条目隐形，请核对是否半截写盘）", flush=True)
    return out



def append_jsonl(path: Path, records: list[dict]) -> int:
    """追加写 JSONL。写前 sanitize（防新记录带 U+2028 类地雷）。"""
    if not records:
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as f:
        for r in records:
            f.write(json.dumps(sanitize_record(r), ensure_ascii=False) + "\n")
    return len(records)


def split_note(text: str) -> tuple[str, str] | None:
    """拆 note → (frontmatter 含首行 `---`、不含闭合线, 余下含闭合线)。非法则 None。"""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    return text[:end], text[end:]


def fm_scalars(head: str) -> dict[str, str]:
    """读 note frontmatter 里的**标量键**（列表/字典块整体跳过），够做定点改写用。

    双引号标量必须走 `json.loads` 解码：`write_note` 是用 `json.dumps` 写的
    （`\\` `\"` `\n` 都被转义），读侧只 `strip('"')` 就**不对称** ——
    实测 `project_url` 带反斜杠时（markdown 转义残留 `Besos\\_Shawarma`）读回来变成
    两个反斜杠，与账本里的一个反斜杠算出**两个不同的项目页 hash**，
    navfix 于是写出指向不存在页面的死链（healthcheck ④ 红）。
    """
    out: dict[str, str] = {}
    for ln in head[4:].splitlines():
        m = re.match(r"^([A-Za-z_][\w]*):\s*(.*)$", ln)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if len(v) >= 2 and v.startswith('"') and v.endswith('"'):
            try:
                out[k] = json.loads(v)
                continue
            except ValueError:
                pass                                   # 不是合法 JSON 的双引号值：退回朴素去引号
        out[k] = v.strip('"') if v else ""
    return out


def fm_list(head: str, key: str) -> list[str]:
    """读 frontmatter 里某个**列表键**（块式 `- x` 或行内 `[a, b]`）→ 字符串列表。

    与 `fm_scalars` 的分工：那个按设计**跳过列表/字典块**（只服务标量键的定点改写），
    所以 `aliases` 这类块式列表用 `fm_scalars` 读回来是空串 —— 判据不同源就会出现
    「生成端写的别名，检查器不认」。2026-09-24 实测：`浏览.md` 的 alias「从这里开始」
    被 healthcheck ④ 误报成 3 处断链。
    """
    lines = head.splitlines()
    body: list[str] = []
    inline = ""
    for idx, ln in enumerate(lines):
        m = re.match(rf"^{re.escape(key)}:\s*(.*)$", ln)
        if not m:
            continue
        inline = m.group(1).strip()
        if inline:
            break
        for j in range(idx + 1, len(lines)):
            nxt = lines[j]
            if not nxt.strip() or nxt.lstrip().startswith("#"):
                continue                                  # 列表块内允许空行/注释
            if not nxt[:1].isspace():                     # 缩进回到 0 → 列表块结束
                break
            item = nxt.strip()
            if not item.startswith("- "):
                break
            body.append(item[2:].strip())
        break
    if inline:
        s = inline
        if s.startswith("["):
            s = s[1:-1] if s.endswith("]") else s[1:]
        return [x.strip().strip("\"'") for x in s.split(",") if x.strip()]
    return [x.strip().strip("\"'") for x in body if x.strip()]


def set_fm_scalar(head: str, key: str, value: str) -> str:
    """在 frontmatter 尾部插入 key（已存在则替换值）。定点改，不重序列化整页。"""
    if re.search(rf"^{key}:\s", head, re.M):
        return re.sub(rf"^{key}:.*$", f"{key}: {value}", head, count=1, flags=re.M)
    return head + f"\n{key}: {value}"


def del_fm_scalar(head: str, key: str) -> str:
    """删掉 frontmatter 里的一行 key（不存在则原样返回）。

    为什么需要「删」而不只是「覆写」：`set_fm_scalar(head, k, None)` 写出来的是字面量
    `k: None`，在 Bases 里会变成一个名为 "None" 的分组 —— 比缺字段更糟。
    值确实不存在的字段必须整行拿掉，让「无值」在 frontmatter 里表现为缺失。
    """
    return re.sub(rf"^{key}:.*\n?", "", head, count=1, flags=re.M)


def write_note(path: Path, frontmatter: dict, body: str) -> None:
    fm = ["---"]
    for k, v in frontmatter.items():
        if v is None or v == "" or v == []:
            continue
        if isinstance(v, list):
            fm.append(f"{k}:")
            for x in v:
                fm.append(f"  - {json.dumps(x, ensure_ascii=False) if isinstance(x, (dict, list)) else x}")
        elif isinstance(v, dict):
            fm.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")   # dict 必须走 JSON，不能 str(dict)
        elif isinstance(v, (int, float, bool)):
            fm.append(f"{k}: {v}")
        else:
            fm.append(f"{k}: {json.dumps(str(v), ensure_ascii=False)}")
    fm.append("---")
    _atomic_write(path, "\n".join(fm) + "\n\n" + body.strip() + "\n")


class RunLog:
    def __init__(self, run_id: str):
        self.run_id = run_id
        self.started = now_cst()
        self.channels: list[dict] = []
        self.notes: list[str] = []
        self.errors: list[str] = []

    def channel(self, source_id: str, name: str, status: str, count: int = 0,
                msg: str = "", elapsed: float = 0.0, extra: dict | None = None):
        rec = {"source_id": source_id, "name": name, "status": status, "count": count,
               "message": msg[:300], "elapsed_s": round(elapsed, 1)}
        if extra:
            rec.update(extra)
        self.channels.append(rec)
        icon = {"ok": "+", "empty": "0", "error": "!", "disabled": "-", "auth": "K"}.get(status, "?")
        print(f"[{icon}] {name:22s} {status:8s} {count:>4}条 {round(elapsed,1):>6}s {msg[:90]}",
              flush=True)

    def error(self, where: str, exc: Exception | str):
        m = f"{where}: {exc}"
        self.errors.append(m)
        print(f"[X] {m}", flush=True)

    def finish(self, path_extra: dict | None = None) -> Path:
        ended = now_cst()
        payload = {
            "run_id": self.run_id,
            "started_at": iso(self.started),
            "ended_at": iso(ended),
            "elapsed_s": round((ended - self.started).total_seconds(), 1),
            "channels": self.channels,
            "notes_written": len(self.notes),
            "errors": self.errors,
        }
        if path_extra:
            payload.update(path_extra)
        out = RUNS / f"{self.run_id}.json"
        _atomic_write(out, json.dumps(payload, ensure_ascii=False, indent=1))
        _atomic_write(RUNS / "latest.json", json.dumps(payload, ensure_ascii=False, indent=1))
        try:
            rotate_runs()                                          # 运行记录轮转（保 80 份）
        except OSError:
            pass
        return out
