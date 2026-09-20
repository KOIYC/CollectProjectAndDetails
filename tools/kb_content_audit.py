"""kb_content_audit — 语料「内容质量」审计（区别于 kb_analyze 的「取数完整性」审计）。

kb_analyze 回答「有没有抓到」；本工具回答「抓到的东西**是不是想要的、够不够用**」：
  ① 相关性  —— 这条跟「独立开发项目」有关系吗？还是泛媒体/技术话题/资源清单/大厂产品？
  ② 完整性  —— 正文是真全文，还是 RSS 摘要 / Exa 8000 字符截断 / 空壳？
  ③ 元数据  —— published_at / author / metrics / tags 有没有，格式规范吗？
  ④ 时效    —— 库里有几天历史？能不能支撑「趋势」分析？
  ⑤ 重复    —— 同一项目在不同渠道重复出现，语料层没合并。
  ⑥ 分类    —— kind 与目标目录是否对得上（project/person/method）。

用法：
  python tools/kb_content_audit.py                 # 全库审计
  python tools/kb_content_audit.py --channel sspai # 单渠道
  python tools/kb_content_audit.py --samples 6     # 每类问题样例条数
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import re
import statistics
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_common import (DIR_REPORT, DIR_RAW, FULLTEXT_MAX_CHARS, LEGACY_EXA_CAP,  # noqa: E402
                       META, iso, now_cst, write_note)

# ---------------------------------------------------------------- 判定规则

# 「独立开发项目」正向信号 —— 分两套词表，因为「像项目」在不同渠道长得不一样：
#   POS_LAUNCH  发布/变现词：Show HN、I built、MRR、pricing、上线、首款…
#   POS_FOUNDER 创始人经营词：裸 SaaS、customer、churn、onboarding、selling…
# 为什么必须补 POS_FOUNDER：只用 POS_LAUNCH 时，实测把 r/SaaS 里**最好的一批**帖子误判为无关 ——
#   "What starts breaking first when your SaaS has to pay users"
#   "One thing selling software to restaurants is teaching me"
#   "First customer feedback is in and it feels amazing"
# 标题里没有 launch/pricing/MRR 这类字面词，但内容正是目标语料。
# 而工程向话题（passkeys / 文件系统 / 编译器 / 架构随笔）两套词表都不命中，仍被正确判为无关 ——
# 词表分工的价值就在这个区分上。
POS_LAUNCH = re.compile(
    r"独立开发|独立游戏|一人公司|个人开发|副业|出海|自研|上线|发布|内测|公测|众筹|首款|"
    r"indie\s*(?:dev|hacker|game|maker)|side[-\s]?project|solo\s*(?:dev|founder)|"
    r"bootstrapp|micro[-\s]?saas|build\s*in\s*public|"
    r"show\s+hn|launch(?:ed|ing)?\b|ship(?:ped|ping)\b|waitlist|"
    r"pricing|paywall|monetiz|subscri(?:be|ption)|MRR|ARR|product\s*hunt|"
    r"my\s+(?:app|product|tool|saas|startup)|I\s+(?:built|made|shipped)|"
    r"免费|付费|订阅|获客|留存|转化|营收|收入|月入|启动", re.I)

POS_FOUNDER = re.compile(
    r"\bsaas\b|one[-\s]?person\s+company|"
    r"founder|co-?founder|customer|churn|retention|onboarding|landing\s+page|"
    r"user\s+acquisition|selling\s+(?:software|my|our)|pre-?launch|"
    r"our\s+(?:website|app|product|users|team)|my\s+(?:users|revenue|customers)|"
    r"growth\s+(?:hack|loop|channel)|conversion\s+rate", re.I)

POS = re.compile(POS_LAUNCH.pattern + "|" + POS_FOUNDER.pattern, re.I)

# 泛媒体 / 与「做产品」无关的主题
MEDIA = re.compile(
    r"早报|晚报|看什么|值得一看|精选|盘点|盘点|攻略|指南\s*[|｜]|城市漫步|游记|"
    r"评测|上手|开箱|体验记|健康|疾病|痤疮|护肤|减肥|睡眠|心理|"
    r"电影|动画|剧集|综艺|音乐|歌单|演唱会|游戏攻略|通关|"
    r"Wallpaper|壁纸|主题|插件推荐|软件推荐|App\s*推荐|"
    r"WWDC|watchOS|macOS\s*\d|iOS\s*\d|Android\s*\d|新功能|更新日志|"
    r"CPU|GPU|显卡|内存条|路由器|NAS|硬盘|装机|跑分", re.I)

# 资源清单 / 名录页（本身不是项目，是「项目的目录」）
RESOURCE = re.compile(
    r"Awesome\b|Resources?\s+for|A\s+guide\s+to|Curated|合集|导航站|目录|清单|"
    r"播客|Podcast|newsletter|周报|日报|Newsletter|Interview\s+Series|"
    r"bootstrapped\s+founders\s+making|playbook", re.I)

# 大厂 / 上市公司产品（不属于「独立开发」）
BIG = re.compile(
    r"\b(openai|meta platforms|google|alphabet|bytedance|tiktok|tencent|alibaba|"
    r"microsoft|amazon|apple|netflix|spotify|roblox|epic games|adobe|nvidia|samsung|"
    r"baidu|vinted|five guys|kalshi|polymarket|shopify|stripe|coinbase|binance)\b", re.I)

# RSS 摘要残文 / 「点击查看全文」类
SUMMARY_TAIL = re.compile(
    r"点击查看全文|查看全文|阅读全文|阅读原文|Read\s*more|Continue\s*reading|"
    r"target=\"_blank\"|</a>\s*$|\.\.\.\s*$|…\s*$", re.I)
HTML_TAG = re.compile(r"<(p|div|br|span|a|img|h[1-6]|ul|li|table)\b", re.I)

EXA_CAP = FULLTEXT_MAX_CHARS   # 与 kb_common.FULLTEXT_MAX_CHARS 同步（原写死 8000 → 40000 上限的截断漏报）
VIDEO_HOST = re.compile(r"^https?://(?:[^/]*\.)?(v\.redd\.it|youtu\.?be|youtube\.com|bilibili\.com/video|vimeo\.com)", re.I)

# 渠道画像 → 该渠道「应当产出什么」，用于算期望命中率
CHANNEL_ROLE = {
    "hn_show": "原文=项目发布帖", "hn_front": "泛技术话题（弱信号）",
    "github_new": "项目仓库", "reddit": "项目讨论",
    "lobsters": "技术社区（弱信号）", "devto": "项目复盘文",
    "producthunt": "项目发布", "indiehackers": "项目库",
    "betalist": "预发布项目", "apple_rss": "榜单（大厂混杂）",
    "v2ex": "中文讨论", "c1c7": "中文名录（含资源/人物）",
    "sspai": "泛科技媒体（弱信号）", "bilibili": "中文视频（仅元数据）",
    "xiaohongshu": "中文社媒", "twitter": "海外社媒",
    "exa_discovery": "全网语义发现",
}

# ---- 「按构造即是项目」的渠道 ---------------------------------------------
# 为什么需要这个集合：相关性判定原来只看关键词（POS 正则），于是把一个**渠道语义**问题
# 误判成了内容问题。实测两例，方向正好相反：
#   betalist 的 "Zapters" / "Aria" / "Campaignstack"（正文 500~900 字）—— 真项目，
#     只因站名就是纯产品名、不含 launch/pricing 等词，被误标「无项目信号」→ 假阳性；
#   lobsters 的 "I don't like passkeys" / "Don't Let Architecture Astronauts Scare You" ——
#     确实是技术随笔，不是项目 → 真阳性。
# 二者用同一套关键词规则无法区分。区别在**渠道契约**：BetaList/Product Hunt 这类站点
# 只收录产品，条目存在本身就等于「这是个项目」；而 Lobsters/HN 首页是话题榜，条目存在
# 什么都不能说明，必须靠关键词。
# 故：契约型渠道不因「没关键词」而判无关（但「大厂产品」仍然算——那是事实性排除）。
# 定义已上移到 kb_common —— 采集端 kb_collect 要用同一份判据决定要不要建实体页，
# 而本模块 import kb_collect（反向），放这里就成环。这里 re-export 保持既有调用点不变。
from kb_common import PROJECT_BY_CONSTRUCTION, SELF_LAUNCH_PREFIX, is_project_ish  # noqa: E402,F401


def load_latest(live_only: bool = True) -> list[dict]:
    """重建 item_id → 最新记录。

    `live_only=True` 时只保留**当前还在库里**的条目 —— 即排除：
      * 已归档条目（note 已被 kb_prune 搬到 80-归档/）
      * 停用渠道的条目（channels.yaml 里 enabled:false / 在 disabled 段）

    为什么必须这样：90-原始/ 是**只追加**的重放底座，归档不改它。
    若审计直接读 raw，那「归档」这个动作在报表上永远看不出来 ——
    可用率会一直卡在 51%，既无法验证修复，也不能当门禁用。
    口径：审计要衡量**可消费的语料**，不是「历史上抓过多少」。
    """
    lat: dict[str, dict] = {}
    for f in glob.glob(str(DIR_RAW / "*" / "*.jsonl")):
        for ln in open(f, encoding="utf-8"):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:                                      # noqa: BLE001
                continue
            iid = r.get("item_id")
            if not iid:
                continue
            cur = lat.get(iid)
            if cur is None or (r.get("captured_at") or "") >= (cur.get("captured_at") or ""):
                lat[iid] = r
    if not live_only:
        return list(lat.values())

    off, archived = disabled_channels(), archived_ids()
    out = []
    for iid, r in lat.items():
        if r.get("source_id") in off:
            continue
        if iid in archived:
            continue
        out.append(r)
    return out


def disabled_channels() -> set[str]:
    """停用渠道集合（读 channels.yaml，与 kb_prune 口径一致）。"""
    try:
        from kb_collect import load_registry
        reg = load_registry()
    except Exception:                                              # noqa: BLE001
        return set()
    ids = {c["id"] for c in (reg.get("channels") or []) if not c.get("enabled")}
    ids |= {c["id"] for c in (reg.get("disabled") or []) if c.get("id")}
    return ids


def archived_ids() -> set[str]:
    """已归档 item_id 集合（看 seen.json 里 note 是否已落到 80-归档/）。

    直接问见账簿而不是扫盘：kb_prune 搬运时会同步更新 note 路径，
    所以 seen.json 是「这条现在在哪」的唯一权威。
    """
    try:
        from kb_common import Seen
        seen = Seen()
    except Exception:                                              # noqa: BLE001
        return set()
    return {iid for iid, m in seen.items.items()
            if (m.get("note") or "").startswith("80-归档/")}


def reasons_for(r: dict) -> list[str]:
    """一条语料的问题标签（可多标签）。"""
    t = f"{r.get('title') or ''}\n{r.get('body') or ''}"
    body = r.get("body") or ""
    out = []

    # 完整性
    if not body.strip():
        out.append("空正文")
    elif len(body) < 200:
        out.append("正文过短(<200)")
    if SUMMARY_TAIL.search(body):
        out.append("RSS摘要/残文")
    if exa_truncated(body):
        out.append("Exa截断")
    if HTML_TAG.search(body):
        out.append("HTML未清理")
    if VIDEO_HOST.search(r.get("url") or "") or VIDEO_HOST.search(r.get("project_url") or ""):
        out.append("视频无正文")

    # 相关性
    # 契约型渠道（只收产品的站）或标题自带自我发布声明 → 不再因「缺关键词」判无关。
    title = r.get("title") or ""
    self_declared = bool(SELF_LAUNCH_PREFIX.search(title))
    by_construction = (r.get("source_id") in PROJECT_BY_CONSTRUCTION or self_declared)
    has_pos = bool(POS.search(t)) or by_construction
    if not has_pos:
        out.append("无项目信号")
    if RESOURCE.search(t) and not by_construction:
        out.append("资源清单/名录")
    # 「大厂产品」是事实性排除，对契约型渠道也照算 —— 但**标题自己声明是自建项目**时不算：
    # Show HN 的条目十有八九要提一嘴集成对象（Stripe / Google / OpenAI / Microsoft），
    # 那是**依赖**不是**出品方**。实测 hn_show 的 7 条「大厂产品」全是这种假阳性
    # （"Show HN: Open-source revenue recognition for Stripe and Meta" 之类），
    # 真按它排掉等于把最好的发布帖删了。
    if not self_declared and BIG.search(f"{title} {r.get('author') or ''}"):
        out.append("大厂产品")
    if MEDIA.search(t) and not has_pos:
        out.append("泛媒体主题")

    # 元数据
    if not r.get("published_at"):
        out.append("缺发布时间")
    elif not re.match(r"^\d{4}-\d{2}-\d{2}", str(r["published_at"])):
        out.append("发布时间未规范化")
    if not r.get("author"):
        out.append("缺作者")
    if not r.get("metrics"):
        out.append("无指标")
    if not r.get("project_url"):
        # 契约型渠道的 `url` 就是该项目的**官方承载页**（PH 的 /products/x、BetaList 的
        # /startups/x 都是"一个项目一页"，是稳定且唯一的项目身份），故不算缺项目链接。
        # 但要说清一个真实代价：这类渠道的项目外链**无法推导** ——
        # PH 的 RSS 正文里只有回指 producthunt.com 的链接（带 utm），
        # BetaList 的 Exa 抽取正文里 0 个链接（Exa 丢了 href）。
        # 也就是说这些条目**不参与跨渠道归并**（跨渠道信号只能靠外链域名/仓库名对齐）。
        if r.get("source_id") not in PROJECT_BY_CONSTRUCTION:
            out.append("无项目链接")
    return out


def exa_truncated(body: str) -> bool:
    """是否被 Exa 正文上限截断。

    两档都要查：现行上限 40000（FULLTEXT_MAX_CHARS）与历史上限 8000（LEGACY_EXA_CAP）——
    只查前者会漏掉旧库里的 8000 字截断文，只查后者会漏掉现在的 40000 字截断文。
    标签故意不带数字，避免两档拆成两行、把同一个问题在报表上稀释成两个小数字。
    """
    return any(abs(len(body) - cap) <= 60 for cap in (EXA_CAP, LEGACY_EXA_CAP))


FATAL = {"空正文", "正文过短(<200)", "RSS摘要/残文"}          # 直接不可用来做深度分析
RELEV = {"无项目信号", "资源清单/名录", "泛媒体主题", "大厂产品"}

# 信号层（layer=signal / profile=metadata）渠道**本就不产出正文** —— B站只有视频元数据、
# App Store 榜单只有榜单信息。对这类渠道计「空正文/正文过短/视频无正文」是拿正文层尺子
# 量信号层数据，属误报（实测 bilibili 被误记 unusable 10 条，把不可用数从 22 抬到 32）。
# 故这三个标签对信号层豁免；标签本身仍照常打出（透明），只是不计入「不可用」。
LAYER_EXEMPT = {"空正文", "正文过短(<200)", "视频无正文"}

# `kind=person` 条目是**人物名片**（落 `30-人物/`），不是项目语料：正文本该只有一行简介，
# 也没有「项目信号」可言。拿项目语料的尺子量它，每轮都会在 c1c7 上生出假缺陷
# （实测 "Patrick McKenzie (@patio11)" / "Pieter Levels (@levelsio)" 被判「无项目信号 + 不可用」，
# 直接把这个小样本渠道的可用率压到 43%）。
KIND_EXEMPT = {"person"}

_PROFILES: dict[str, str] | None = None


def channel_profiles() -> dict[str, str]:
    """渠道 id → profile（惰性加载一次）。"""
    global _PROFILES
    if _PROFILES is None:
        _PROFILES = {}
        try:
            from kb_collect import load_registry
            reg = load_registry()
            for c in list(reg.get("channels") or []) + list(reg.get("disabled") or []):
                if c.get("id"):
                    _PROFILES[c["id"]] = c.get("profile") or ""
        except Exception:                                          # noqa: BLE001
            pass
    return _PROFILES


def item_layer(r: dict) -> str:
    """条目所在层：signal（只当线索）还是 corpus（可做深度分析）。"""
    ex = (r.get("extra") or {}).get("layer")
    if ex:
        return str(ex)
    prof = channel_profiles().get(r.get("source_id") or "") or ""
    return "signal" if prof == "metadata" else "corpus"


def applicable_tags(r: dict, tags) -> set[str]:
    """按「条目所在的层 / 类型」折算标签 —— 判定尺子必须跟数据层对齐。

    信号层（metadata 画像）本就不产正文；人物名片本就不是项目语料。
    对它们计完整性/相关性缺陷属口径错误，会虚增「不可用」（实测 bilibili 虚增 10 条、
    c1c7 虚增 2 条）。标签本身照常打出（透明），只是不计入可用率。
    """
    tags = set(tags)
    if item_layer(r) == "signal":
        tags -= LAYER_EXEMPT
    if (r.get("kind") or "") in KIND_EXEMPT:
        tags -= (LAYER_EXEMPT | RELEV)
    return tags


def is_fatal(r: dict, reasons) -> bool:
    """是否「不适合做深度分析」——按层/类型折算后的判定。"""
    return bool(FATAL & applicable_tags(r, reasons))


def audit(items: list[dict], samples: int = 4) -> dict:
    rep: dict = {"n": len(items)}
    # 两个时间轴必须分开报，混在一起会得出错误结论：
    #   captured_days = 我们**采集**的日子（多轮采集才有跨度）
    #   pub_days      = 内容**发布**的日子跨度 —— 趋势分析只取决于这个
    # 早先只报 captured_days，于是「刚跑完 90 天历史铺底」在报表上仍显示「历史深度 1 天」，
    # 把已经解决的事呈现成未解决（实测踩过）。
    rep["captured_days"] = sorted({(r.get("captured_at") or "")[:10] for r in items})
    rep["pub_days"] = sorted({(r.get("published_at") or "")[:10] for r in items
                              if r.get("published_at")})
    # 跨度不能用 max-min：一条 2014 年的老仓库就能把跨度撑到几千天（实测 4551 天），
    # 数字既不可信也无决策价值。而分位数在这种「一大簇近月 + 稀疏长尾」的分布上同样不稳
    # （实测 p5~p95 仍报 2331 天）。所以直接报**能用的口径**：近 90 天多少条、
    # 更早多少条、无发布时间多少条 —— 趋势分析真正关心的就是前一个数。
    now = now_cst()
    cut90 = (now - timedelta(days=90)).strftime("%Y-%m-%d")
    dated = [(r.get("published_at") or "")[:10] for r in items if r.get("published_at")]
    rep["pub_recent90"] = sum(1 for d in dated if d >= cut90)
    rep["pub_older"] = len(dated) - rep["pub_recent90"]
    rep["pub_missing_dates"] = len(items) - len(dated)
    rep["pub_span_days"] = max(0, (
        (datetime.fromisoformat(dated[-1]) - datetime.fromisoformat(dated[0])).days
        if len(dated) > 1 else 0))
    pub = [(r.get("published_at") or "")[:10] for r in items]
    rep["pub_missing"] = sum(1 for p in pub if not p)
    rep["pub_norm_bad"] = sum(1 for p in pub if p and not re.match(r"^\d{4}-\d{2}-\d{2}$", p))
    rep["author_missing"] = sum(1 for r in items if not r.get("author"))
    rep["metrics_empty"] = sum(1 for r in items if not r.get("metrics"))
    rep["body_format"] = collections.Counter(r.get("body_format") for r in items)
    rep["kind"] = collections.Counter(r.get("kind") for r in items)
    rep["lang"] = collections.Counter(r.get("lang") for r in items)

    bl = [len(r.get("body") or "") for r in items]
    rep["body_len"] = {"median": statistics.median(bl) if bl else 0,
                       "mean": int(statistics.mean(bl)) if bl else 0,
                       "zero": sum(1 for x in bl if x == 0),
                       "lt200": sum(1 for x in bl if x < 200)}

    # 问题标签汇总
    flagged: dict[str, list[dict]] = collections.defaultdict(list)
    per_item: dict[str, list[str]] = {}
    for r in items:
        rs = reasons_for(r)
        per_item[r["item_id"]] = rs
        for x in rs:
            flagged[x].append(r)
    rep["flags"] = {k: len(v) for k, v in sorted(flagged.items(), key=lambda kv: -len(kv[1]))}
    rep["unusable"] = sum(1 for r in items if is_fatal(r, per_item[r["item_id"]]))
    rep["irrelevant"] = sum(1 for r in items
                            if RELEV & applicable_tags(r, per_item[r["item_id"]]))
    rep["clean"] = sum(1 for r in items
                       if not (RELEV & applicable_tags(r, per_item[r["item_id"]]))
                       and not is_fatal(r, per_item[r["item_id"]]))
    rep["signals"] = sum(1 for r in items if item_layer(r) == "signal")

    # 渠道维度
    by = collections.defaultdict(lambda: {"n": 0, "ok": 0, "unusable": 0, "irrelevant": 0,
                                          "resource": 0, "big": 0, "summary": 0, "trunc": 0,
                                          "html": 0, "no_pub": 0, "no_author": 0, "no_metrics": 0,
                                          "body0": 0, "bodylen": []})
    for r in items:
        d = by[r["source_id"]]
        rs = set(per_item[r["item_id"]])
        app = applicable_tags(r, rs)          # 层/类型折算后的标签才是判定依据
        fatal = is_fatal(r, rs)
        d["n"] += 1
        d["bodylen"].append(len(r.get("body") or ""))
        d["unusable"] += 1 if fatal else 0
        d["irrelevant"] += 1 if RELEV & app else 0
        d["ok"] += 1 if not fatal and not (RELEV & app) else 0
        d["resource"] += 1 if "资源清单/名录" in rs else 0
        d["big"] += 1 if "大厂产品" in rs else 0
        d["summary"] += 1 if "RSS摘要/残文" in rs else 0
        d["trunc"] += 1 if any(x.startswith("Exa截断") for x in rs) else 0
        d["html"] += 1 if "HTML未清理" in rs else 0
        d["no_pub"] += 1 if "缺发布时间" in rs or "发布时间未规范化" in rs else 0
        d["no_author"] += 1 if "缺作者" in rs else 0
        d["no_metrics"] += 1 if "无指标" in rs else 0
        d["body0"] += 1 if len(r.get("body") or "") == 0 else 0
    rep["by_channel"] = by

    # 跨渠道重复（同一条目 url / 同 project_url 出现在多渠道）
    dom = collections.defaultdict(set)
    for r in items:
        u = r.get("project_url") or ""
        m = re.match(r"https?://([^/]+)(/[^?#]*)?", u)
        if m:
            key = m.group(1).lower().removeprefix("www.") + (m.group(2) or "").rstrip("/")
            dom[key].add(r["source_id"])
    rep["cross_channel_dupes"] = [(k, sorted(v)) for k, v in dom.items() if len(v) > 1]

    rep["samples"] = {k: [{"source": r["source_id"], "title": (r.get("title") or "")[:80],
                           "url": r.get("url")} for r in v[:samples]]
                      for k, v in sorted(flagged.items(), key=lambda kv: -len(kv[1]))}
    return rep


def render(rep: dict) -> str:
    n = rep["n"]
    L = ["# 语料内容质量审计", "",
         f"> 生成 {iso(now_cst())} · 审计器 `tools/kb_content_audit.py`", "",
         f"- 唯一条目 **{n}** · 可用（无致命缺陷、且相关）**{rep['clean']}** "
         f"({100 * rep['clean'] / max(1, n):.0f}%)",
         f"- 不可用于深度分析（空/过短/摘要残文）**{rep['unusable']}** ({100 * rep['unusable'] / max(1, n):.0f}%)",
         f"- 相关性可疑（无项目信号/资源清单/泛媒体/大厂）**{rep['irrelevant']}** "
         f"({100 * rep['irrelevant'] / max(1, n):.0f}%)",
         f"- 正文长度 中位 **{rep['body_len']['median']}** · 均值 {rep['body_len']['mean']} · "
         f"空正文 {rep['body_len']['zero']} · <200 字符 {rep['body_len']['lt200']}",
         f"- 历史深度（**内容发布时间轴**，趋势分析看这个）：近 90 天 **{rep.get('pub_recent90', 0)} 条**，"
         f"更早 {rep.get('pub_older', 0)} 条，无发布时间 {rep.get('pub_missing_dates', 0)} 条"
         f"（最早 {rep.get('pub_days')[:1] or ['—']}）",
         f"- 采集时间轴：`captured_at` 覆盖 {len(rep['captured_days'])} 天 "
         f"({', '.join(rep['captured_days']) or '—'})",
         f"- 语种：{', '.join(f'{k}={v}' for k, v in rep['lang'].most_common())}",
         f"- kind：{', '.join(f'{k}={v}' for k, v in rep['kind'].most_common())}", "",
         "## 问题标签汇总", "", "| 问题 | 条数 | 占比 |", "|---|---|---|"]
    for k, v in rep["flags"].items():
        L.append(f"| {k} | {v} | {100 * v / max(1, n):.0f}% |")

    L += ["", "## 渠道质量矩阵", "",
          "| 渠道 | 角色 | 条目 | 可用 | 不可用 | 相关性可疑 | 资源清单 | 大厂 | 摘要残文 | Exa截断 | HTML残留 | 无时间 | 无作者 | 无指标 | 正文中位 |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for cid, d in sorted(rep["by_channel"].items(), key=lambda kv: -kv[1]["n"]):
        bl = sorted(d["bodylen"])
        med = bl[len(bl) // 2] if bl else 0
        L.append(f"| {cid} | {CHANNEL_ROLE.get(cid, '—')} | {d['n']} | {d['ok']} | {d['unusable']} | "
                 f"{d['irrelevant']} | {d['resource']} | {d['big']} | {d['summary']} | {d['trunc']} | "
                 f"{d['html']} | {d['no_pub']} | {d['no_author']} | {d['no_metrics']} | {med} |")

    if rep["cross_channel_dupes"]:
        L += ["", "## 跨渠道重复（同 project_url 出现在多渠道，语料层未合并）", ""]
        L += [f"- {', '.join(v)} → {k[:80]}" for k, v in rep["cross_channel_dupes"][:20]]

    L += ["", "## 元数据完整性", "",
          f"- `published_at` 缺失 **{rep['pub_missing']}** · 格式未规范化 **{rep['pub_norm_bad']}**",
          f"- `author` 缺失 **{rep['author_missing']}** · `metrics` 全空 **{rep['metrics_empty']}**",
          f"- `body_format`：{', '.join(f'{k}={v}' for k, v in rep['body_format'].most_common())}", ""]

    L += ["", "## 问题样例（人工复核用）", ""]
    for k, ss in rep["samples"].items():
        L.append(f"### {k}（{rep['flags'][k]} 条）")
        L += [f"- `{s['source']}` {s['title']}" for s in ss] + [""]
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", default="")
    ap.add_argument("--samples", type=int, default=4)
    ap.add_argument("--all", action="store_true",
                    help="含已归档/停用渠道条目（默认只看当前库里可消费的语料）")
    args = ap.parse_args(argv)

    items = load_latest(live_only=not args.all)
    if args.channel:
        items = [r for r in items if r["source_id"] == args.channel]
    rep = audit(items, args.samples)

    scope = "全量(含归档)" if args.all else "在库语料"
    print(f"[{scope}] 唯一条目 {rep['n']} · 可用 {rep['clean']} · 不可用(深度分析) {rep['unusable']} · "
          f"相关性可疑 {rep['irrelevant']}")
    print(f"分层：信号层 {rep.get('signals', 0)} 条（无正文属预期，已豁免完整性判定）· "
          f"正文层 {rep['n'] - rep.get('signals', 0)} 条")
    if rep["n"]:
        print(f"可用率 {rep['clean'] / rep['n'] * 100:.0f}%")
    print(f"正文中位 {rep['body_len']['median']} · 空 {rep['body_len']['zero']} · <200 {rep['body_len']['lt200']}")
    print(f"历史深度（发布轴）近90天 {rep.get('pub_recent90', 0)} 条 · "
          f"更早 {rep.get('pub_older', 0)} 条 · 无发布时间 {rep.get('pub_missing_dates', 0)} 条 · "
          f"采集轴 {len(rep['captured_days'])} 天 · 跨渠道重复 {len(rep['cross_channel_dupes'])}")
    print("问题标签：" + "、".join(f"{k}={v}" for k, v in list(rep["flags"].items())[:12]))
    print("\n渠道（可用/条目 ｜ 主要问题）：")
    for cid, d in sorted(rep["by_channel"].items(), key=lambda kv: (kv[1]["ok"] / max(1, kv[1]["n"]))):
        if d["n"] < 5:
            continue
        bits = [f"{k}{d[k]}" for k in ("unusable", "irrelevant", "resource", "big", "summary", "trunc")
                if d[k]]
        print(f"  {cid:14s} {d['ok']:>3}/{d['n']:<3}  {' '.join(bits) or 'OK'}")

    tag = args.channel or "all"
    write_note(DIR_REPORT / f"内容审计-{tag}.md",
               {"type": "report", "title": f"内容质量审计 {tag}", "updated": iso(now_cst()),
                "tags": ["索引", "审计", "内容质量"]}, render(rep))
    (META / "content_audit.json").write_text(json.dumps(
        {"generated": iso(now_cst()), "scope": tag, "n": rep["n"], "clean": rep["clean"],
         "unusable": rep["unusable"], "irrelevant": rep["irrelevant"], "flags": rep["flags"],
         "body_len": rep["body_len"], "captured_days": rep["captured_days"],
         "by_channel": {k: {kk: vv for kk, vv in v.items() if kk != "bodylen"}
                        for k, v in rep["by_channel"].items()},
         "cross_channel_dupes": rep["cross_channel_dupes"]},
        ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
