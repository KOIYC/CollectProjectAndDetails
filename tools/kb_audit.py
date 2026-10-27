"""kb_audit — 渠道体检 + 台账生成（独立开发项目知识库）。

作用：
  1) 读 _meta/channels.yaml 逐渠道做最小探针（每渠道取 3 条，不写语料）
  2) 跑 agent-reach doctor（1.6.0 起默认输出 JSON，旧的 `--json` 已移除）采集外部平台后端状态
  3) 写 _meta/health.json，并重生成 00-索引/渠道台账.md（导航层）+ 00-索引/报告/AgentReach体检.md
  4) 输出「建议新增 / 建议停用 / 可解锁」清单，供 skill 流程判断

用法：
  python tools/kb_audit.py            # 全渠道探针 + 台账
  python tools/kb_audit.py --fast     # 只跑零认证渠道
  python tools/kb_audit.py --no-doctor
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kb_common import DIR_INDEX, DIR_REPORT, META, RunLog, iso, now_cst, run_cli, write_note  # noqa: E402
import kb_common  # noqa: E402
import kb_collect as KC  # noqa: E402

HEALTH = META / "health.json"
CANDIDATES = META / "channel_candidates.yaml"

PROBE_LIMIT = 3

# 后端复检的状态图标（throttled = 服务端限流，既不能算 ok 也不能算不可用）
BACKEND_ICON = {"ok": "✅ ok", "throttled": "⏳ throttled（服务端限流，非不可用）",
                "unusable": "❌ unusable"}


def probe_channel(ch: dict, timeout_scale=1.0) -> dict:
    t0 = time.time()
    adapter = KC.ADAPTERS.get(ch.get("adapter") or "")
    c = json.loads(json.dumps(ch))
    c["limit"] = PROBE_LIMIT
    p = c.get("params") or {}
    # 探针是「采集器能不能取到」的最小复现，口径必须与采集一致 —— 只按速度裁参数，
    # 不替采集改判定阈值。
    #
    # `subs` 不能一律截到 1 个：arctic-shift 返回的是「窗口内最新 N 条」而不是高分优先，
    # 而 `min_score` 是采集端在取回后再过滤的。实测 2026-09-24：只探第 1 个 sub
    # （SideProject，各窗口 25 条最高分仅 2）→ 探针恒报 `empty`；同轮采集用 8 个 sub
    # 取到 19 条。这种假 empty 会误触 skill 的「连续 2 轮 empty → 降权/停用」规则，
    # 即用探针的口径停掉一个健康渠道。每 sub 只是 1 次请求（实测整渠道 ~5s），不构成负担。
    # `queries`/`tags`/`paths` 保持截断：它们是搜索型，逐个探的代价高得多。
    multi = any(p.get(k) not in (None, 0) for k in ("min_score", "min_points", "min_stars"))
    if isinstance(p.get("queries"), list):
        p["queries"] = p["queries"][:1]
    if isinstance(p.get("subs"), list):
        p["subs"] = p["subs"] if multi else p["subs"][:1]
    if isinstance(p.get("tags"), list):
        p["tags"] = p["tags"][:1]
    if isinstance(p.get("paths"), list):
        p["paths"] = p["paths"][:1]
    c["params"] = p
    try:
        items, status, msg = adapter(c, {"max_comments": 3, "fulltext_budget": 0})
    except Exception as e:                                         # noqa: BLE001
        items, status, msg = [], "error", str(e)[:200]
    if multi and items:
        # 消息里只说本次真放宽了哪个维度；没有 subs 的阈值渠道（如 hn_show 的 min_points）
        # 不能硬取 p["subs"]（KeyError 实测踩过一次）。
        how = (f"全部 {len(p['subs'])} 个 sub" if isinstance(p.get("subs"), list) and p["subs"]
               else "完整列表参数")
        msg = (f"{msg} · 探针保留{how}与原阈值（口径同采集）")[:220]
    return {"channel_id": ch["id"], "name": ch.get("name"), "adapter": ch.get("adapter"),
            "auth": ch.get("auth"), "group": ch.get("group"),
            "status": status, "count": len(items), "message": msg[:220],
            "elapsed_s": round(time.time() - t0, 1), "probe_at": iso(now_cst()),
            "sample": [{"title": i["title"][:80], "url": i["url"]} for i in items[:2]]}


def _fetch_json_probe(url: str, timeout: int = 30):
    """探针专用 JSON 取数：返回 (payload|None, http_status, body_text)。

    比 `kb_common.http_json` 多带一步「读错误响应体」—— 有些后端把**限流**也报成 4xx
    （实测 arctic-shift：HTTP 422 + `{"error":"Timeout. Maybe slow down a bit"}`），
    只看状态码会把它误判成「后端不可用」。
    """
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (kb-audit probe)",
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8", "replace")), r.status, ""
    except urllib.error.HTTPError as e:
        return None, e.code, e.read(400).decode("utf-8", "replace")
    except Exception as e:                                         # noqa: BLE001
        return None, 0, f"{type(e).__name__}: {e}"


def probe_backends(doctor: dict | None = None) -> list[dict]:
    """复检关键后端（含 agent-reach doctor 声明可用但实测不可用的 delta）。

    `declared` 按 doctor 的**实际声明**取（1.6.0 起 json 里是 `unverified` / `not_added` 这类措辞），
    不能写死 `ok` —— 否则 doctor 改了口径就会凭空造出「矛盾」delta（2026-10-27 实测：doctor 已把
    `web` 报成 `unverified`，而脚本仍宣称它「声明 ok」）。只有 doctor 真的说 `ok/ready` 才算矛盾。
    """
    out = []

    plat = (doctor or {}).get("platforms") or {}

    def declared_of(bid: str, fallback: str | None = None) -> str | None:
        p = plat.get({"jina_reader": "web", "exa_web_fetch": "exa",
                      "arctic_shift": "reddit", "github_gh": "github"}.get(bid, "")) or {}
        raw = p.get("raw_status") or p.get("status")
        return raw or fallback

    def add(bid, use, ok, msg, elapsed, declared=None, status=None):
        st = status or ("ok" if ok else "unusable")
        out.append({"backend": bid, "use": use, "status": st,
                    "declared": declared, "delta": (declared == "ok" and st == "unusable"),
                    "message": msg[:150], "elapsed_s": round(elapsed, 1),
                    "probe_at": iso(now_cst())})

    t0 = time.time()
    try:
        body = kb_common.http_get("https://r.jina.ai/https://example.com", timeout=20, retries=0)
        add("jina_reader", "通用网页正文", len(body) > 100,
            f"HTTP {len(body)}B", time.time() - t0, declared=declared_of("jina_reader", "ok"))
    except Exception as e:                                         # noqa: BLE001
        add("jina_reader", "通用网页正文", False, str(e)[:110], time.time() - t0,
            declared=declared_of("jina_reader", "ok"))

    t0 = time.time()
    payload, code, body = _fetch_json_probe(
        "https://arctic-shift.photon-reddit.com/api/posts/search"
        "?subreddit=SideProject&limit=5&sort=desc&after=1789000000", timeout=30)
    dt = time.time() - t0
    if payload is not None:
        add("arctic_shift", "Reddit 取数", bool(payload.get("data")),
            f"{len(payload.get('data') or [])} rows", dt, declared=declared_of("arctic_shift"))
    elif code == 422 and "slow down" in (body or "").lower():
        # 服务端限流（探针紧随渠道探针/采集之后连打，容易撞上）→ 既不是不可用也不是渠道腐化
        add("arctic_shift", "Reddit 取数", True, f"HTTP 422 服务端限流：{body.strip()[:70]}",
            dt, declared=declared_of("arctic_shift"), status="throttled")
    else:
        add("arctic_shift", "Reddit 取数", False, f"HTTP {code} {body[:90]}", dt,
            declared=declared_of("arctic_shift"))

    t0 = time.time()
    try:
        res = kb_common.exa_fetch_texts(["https://example.com"], max_chars=1200, timeout=120)
        add("exa_web_fetch", "通用网页正文后端", bool(res),
            f"{len(res)} url 返回正文", time.time() - t0, declared=declared_of("exa_web_fetch", "warn"))
    except Exception as e:                                         # noqa: BLE001
        add("exa_web_fetch", "通用网页正文后端", False, str(e)[:110], time.time() - t0,
            declared=declared_of("exa_web_fetch", "warn"))

    t0 = time.time()
    code, gh_out, gh_err = run_cli(["gh", "api", "rate_limit", "--jq", ".resources.core.remaining"],
                                   timeout=45)
    add("github_gh", "GitHub 取数 (gh CLI)", code == 0,
        f"remaining={gh_out.strip()[:12]}" if code == 0 else (gh_err or gh_out)[:110],
        time.time() - t0, declared=declared_of("github_gh", "warn"))
    return out


_DOCTOR_STATUS = {
    "ok": "ok", "ready": "ok", "available": "ok",
    "warn": "warn", "degraded": "warn", "error": "warn", "failed": "warn",
    "unverified": "warn", "unknown": "warn",
    "off": "off", "not_added": "off", "missing": "off",
}

_DOCTOR_LABELS = {
    "github": "GitHub 仓库和代码", "twitter": "Twitter/X 推文", "youtube": "YouTube 视频和字幕",
    "reddit": "Reddit 帖子和评论", "facebook": "Facebook 帖子、主页和群组",
    "instagram": "Instagram 用户、主页和指定用户帖子", "bilibili": "B站视频、字幕和搜索",
    "xiaohongshu": "小红书笔记", "linkedin": "LinkedIn 职业社交", "xiaoyuzhou": "小宇宙播客转文字",
    "v2ex": "V2EX 节点、主题与回复", "xueqiu": "雪球股票行情与社区动态",
    "rss": "RSS/Atom 订阅源", "exa": "全网语义搜索", "web": "任意网页", "jina": "任意网页",
}


def _doctor_platforms(d: dict) -> dict:
    """把 agent-reach doctor 的新旧两种 JSON 结构归一成 {平台: {status,name,active_backend,message}}。

    1.6.0 起 CLI 改为「默认输出 JSON、去掉 --json」，结构也从 `{平台: {...}}` 变成
    `{ok, result: {version, channels: [{channel, status, problems, hint, ...}]}}`。
    旧结构若被新版覆盖而未归一，体检报告会渲染成 0 行（曾导致 `AgentReach体检.md` 从 10-22 起停更）。
    """
    res = d.get("result")
    if isinstance(res, dict) and isinstance(res.get("channels"), list):
        plats = {}
        for c in res["channels"]:
            if not isinstance(c, dict):
                continue
            cid = c.get("channel") or "?"
            raw = str(c.get("status") or "").lower()
            msg = "; ".join(c.get("problems") or []) or (c.get("hint") or "")
            plats[cid] = {"status": _DOCTOR_STATUS.get(raw, "warn"), "raw_status": raw,
                          "active_backend": c.get("backend") or c.get("active_backend"),
                          "name": _DOCTOR_LABELS.get(cid, cid), "level": c.get("level"),
                          "message": msg[:160]}
        return plats
    # 旧结构：{平台名: {status, active_backend, name, message}}
    return {k: {"status": v.get("status"), "active_backend": v.get("active_backend"),
                "name": v.get("name") or k, "message": (v.get("message") or "")[:160]}
            for k, v in d.items() if isinstance(v, dict) and "status" in v}


def agent_reach_doctor() -> dict:
    # 1.6.0 起 `--json` 已移除（传了会 BAD_INPUT）；旧版默认输出人类可读表格 → 故先试无参，失败再退回 --json。
    code, out, err = run_cli(["agent-reach", "doctor"], timeout=180)
    if code != 0 or "{" not in (out or ""):
        code2, out2, err2 = run_cli(["agent-reach", "doctor", "--json"], timeout=180)
        if code2 == 0 and "{" in (out2 or ""):
            out = out2
        else:
            return {"ok": False, "error": (err or out or err2 or out2 or "")[:200], "platforms": {}}
    try:
        d = json.loads(out[out.index("{"):])
    except Exception as e:                                         # noqa: BLE001
        return {"ok": False, "error": f"parse: {e}", "platforms": {}}
    plats = _doctor_platforms(d)
    res = d.get("result") if isinstance(d.get("result"), dict) else {}
    err_obj = d.get("error") if isinstance(d.get("error"), dict) else {}
    return {"ok": bool(plats) and bool(d.get("ok", True)), "checked_at": iso(now_cst()),
            "platforms": plats, "version": res.get("version") or d.get("version"),
            "error": (err_obj.get("message") or "")[:200] or None}


RECOMMEND_TEMPLATES = {
    "missing_channels": [
        {"id": "github_trending_cn", "why": "中文/Gitee 侧独立开发信号（Gitee 趋势）"},
        {"id": "microlaunch", "why": "海外小型发布站，PH 之外的早期信号"},
        {"id": "peerlist", "why": "Peerlist launches，独立开发者高密度"},
        {"id": "hackernews_front", "why": "HN 首页（非 Show HN）技术选型/趋势语料"},
        {"id": "juejin_zhihu", "why": "中文技术社区复盘语料（掘金/知乎专栏）"},
        {"id": "gumroad_lemon", "why": "卖断型产品热销榜，验证付费意愿"},
        {"id": "bing_wechat_index", "why": "搜索热度验证（百度指数/微信指数）"},
    ],
}


def classify(ch: dict, probe: dict, doctor: dict) -> str:
    st = probe["status"]
    if st in ("ok",):
        return "keep"
    if st == "auth":
        return "unlock"
    if st in ("empty",):
        return "watch"
    return "review"


def render_ledger(registry: dict, health: dict, doctor: dict) -> str:
    rows_ok, rows_issue, rows_auth, rows_dis = [], [], [], []
    for p in health["channels"]:
        line = (f"| {p['name']} | `{p['channel_id']}` | {p.get('group')} | {p['auth']} | "
                f"`{p['status']}` | {p['count']} | {p['elapsed_s']}s | {p['message'][:80]} |")
        if p["status"] == "ok":
            rows_ok.append(line)
        elif p["status"] == "auth":
            rows_auth.append(line)
        else:
            rows_issue.append(line)
    for d in registry.get("disabled") or []:
        rows_dis.append(f"| `{d['id']}` | {d['reason'][:90]} | {d.get('revive', '—')[:70]} |")

    plat_rows = []
    for k, v in (doctor.get("platforms") or {}).items():
        icon = {"ok": "✅", "warn": "⚠️", "off": "❌"}.get(v.get("status"), "?")
        plat_rows.append(f"| {k} | {icon} {v.get('raw_status') or v.get('status')} | `{v.get('active_backend') or '—'}` | "
                         f"{v.get('message', '')[:90]} |")

    hdr = ("| 渠道 | id | 分组 | 认证 | 状态 | 条数 | 耗时 | 消息 |\n|---|---|---|---|---|---|---|---|")
    empty_row = ["| — | — | — | — | — | — | — | — |"]
    issue_rows = rows_issue or empty_row
    auth_rows = rows_auth or empty_row
    parts = [
        "# 渠道台账", "",
        f"> 自动生成 by `tools/kb_audit.py` · 体检时间 {health['checked_at']} · "
        f"注册表 `_meta/channels.yaml`（改渠道改这里，不用改代码）", "",
        f"**总览**：启用 {len(health['channels'])} 个渠道 · 正常 {len(rows_ok)} · "
        f"异常/待观察 {len(rows_issue)} · 可解锁 {len(rows_auth)} · 停用 {len(rows_dis)}", "",
        "## 1. 正常工作渠道", "", hdr, *rows_ok, "",
        "## 2. 异常 / 待观察", "", hdr, *issue_rows, "",
        "## 3. 可解锁（缺登录态）", "", hdr, *auth_rows, "",
        "## 4. 停用登记（不进采集循环）", "",
        "| 渠道 | 停用原因 | 复活条件 |", "|---|---|---|", *rows_dis, "",
        "## 5. agent-reach 平台后端（外部能力面）", "",
        "| 平台 | doctor | 激活后端 | 说明 |", "|---|---|---|---|", *plat_rows, "",
        "## 6. 关键后端复检（实测 vs doctor 声明）", "",
        "| 后端 | 用途 | 实测 | doctor 声明 | Delta | 证据 |", "|---|---|---|---|---|---|",
        *[f"| `{b['backend']}` | {b['use']} | {BACKEND_ICON.get(b['status'], '❌ unusable')} | "
          f"{b.get('declared') or '—'} | {'⚠️ **矛盾**' if b.get('delta') else '—'} | {b['message']} |"
          for b in (health.get("backends") or [])], "",
        "## 7. 建议评估新增通道（需 agent-reach 验证后决定）", "",
    ]
    for c in RECOMMEND_TEMPLATES["missing_channels"]:
        parts.append(f"- `{c['id']}` — {c['why']}")
    parts += ["", "> 新增/删除渠道流程：kb_audit 探活 → 人工/LLM 判断 → 改 `_meta/channels.yaml` "
              "（`enabled` / `disabled`）→ 下次采集生效。", ""]
    return "\n".join(parts)


def render_doctor_note(doctor: dict) -> str:
    rows = []
    for k, v in (doctor.get("platforms") or {}).items():
        icon = {"ok": "✅", "warn": "⚠️", "off": "❌"}.get(v.get("status"), "?")
        rows.append(f"| {v.get('name') or k} | {icon} | {v.get('raw_status') or v.get('status')} | `{v.get('active_backend') or '—'}` | "
                    f"{v.get('message', '')[:120]} |")
    ver = f" · agent-reach {doctor['version']}" if doctor.get("version") else ""
    broken = f"\n> ⚠️ doctor 未返回平台状态：{doctor['error']}" if not rows and doctor.get("error") else ""
    return "\n".join([
        "# agent-reach 体检", "",
        f"> 检查时间 {doctor.get('checked_at')}{ver} · 由 `agent-reach doctor`（默认输出 JSON）生成{broken}", "",
        "| 平台 | | 状态 | 激活后端 | 说明 |", "|---|---|---|---|---|", *(rows or ["| — | — | — | — | — |"]), "",
        "## 与 KB 渠道的对应关系", "",
        "| KB 渠道 | 依赖的 agent-reach 平台 | 说明 |", "|---|---|---|",
        "| `hn_show` / `reddit` / `lobsters` / `devto` / `producthunt` | 无（直连 API/RSS） | 零配置，不依赖 agent-reach 后端 |",
        "| `github_new` | github (gh CLI) | doctor 只查配置不实测，以 kb_audit 探针为准 |",
        "| `v2ex` | web (Jina) / 直连 sov2ex | 官方 API 本网络 502，已改 sov2ex |",
        "| `exa_discovery` | exa_search (mcporter) | doctor 不连通验证，以探针为准 |",
        "| `xiaohongshu` | xiaohongshu（OpenCLI / xhs-mcp） | 需浏览器登录态 |",
        "| `twitter` | twitter（OpenCLI / twitter-cli） | 需扩展或 Cookie |",
        "| `bilibili` | bilibili | 直连搜索 API 可用（带 Referer），无需登录 |", "",
    ])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true", help="只探零认证渠道")
    ap.add_argument("--no-doctor", action="store_true")
    ap.add_argument("--channels", default="")
    args = ap.parse_args(argv)

    kb_common.ensure_dirs()
    reg = KC.load_registry()
    chans = reg["_enabled_channels"]
    if args.fast:
        chans = [c for c in chans if c.get("auth") == "none"]
    if args.channels:
        want = {c.strip() for c in args.channels.split(",")}
        chans = [c for c in chans if c["id"] in want]

    log = RunLog(now_cst().strftime("%Y%m%dT%H%M%S"))
    results = []
    for ch in chans:
        r = probe_channel(ch)
        results.append(r)
        log.channel(r["channel_id"], r["name"], r["status"], r["count"], r["message"], r["elapsed_s"])

    doctor = {"ok": False, "platforms": {}} if args.no_doctor else agent_reach_doctor()
    backends = [] if args.no_doctor else probe_backends(doctor)

    # 子集探针（--channels / --fast）不得摧毁全局体检记录：按 channel_id 合并进既有 health.json。
    # 实测坑：单渠道复测 c1c7 曾把 13 渠道的 health.json 与 渠道台账.md 覆盖成「启用 1 个渠道」，
    # 台账（导航层）当场失真，且下一轮会据此误判渠道启停。
    subset = bool(args.channels) or args.fast
    prev = {}
    if subset and HEALTH.exists():
        try:
            prev = json.loads(HEALTH.read_text(encoding="utf-8"))
        except Exception:
            prev = {}
    if subset and prev.get("channels"):
        by_id = {r["channel_id"]: r for r in results}
        merged = [by_id.get(r["channel_id"], r) for r in prev["channels"]]
        seen = {r["channel_id"] for r in merged}
        merged += [r for r in results if r["channel_id"] not in seen]
        print(f"[i] 子集探针：本轮 {len(results)} 条已合并进既有 {len(prev['channels'])} 条记录"
              f" → 台账记录 {len(merged)} 个渠道（不覆盖历史体检）")
        results = merged
        if args.no_doctor:
            backends = prev.get("backends", [])

    chans_by_id = {c["id"]: c for c in reg["_enabled_channels"]}
    health = {
        "checked_at": iso(now_cst()),
        "channels": results,
        "backends": backends,
        "summary": {
            "total": len(results),
            "ok": sum(1 for r in results if r["status"] == "ok"),
            "empty": sum(1 for r in results if r["status"] == "empty"),
            "error": sum(1 for r in results if r["status"] == "error"),
            "auth": sum(1 for r in results if r["status"] == "auth"),
        },
        "decisions": [{"channel_id": r["channel_id"],
                       "action": classify(chans_by_id[r["channel_id"]], r, doctor),
                       "status": r["status"]}
                      for r in results if r["channel_id"] in chans_by_id],
        "agent_reach": {"ok": doctor.get("ok"), "checked_at": doctor.get("checked_at"),
                        "version": doctor.get("version"), "error": doctor.get("error"),
                        "platforms": len(doctor.get("platforms") or {})}
                       if not (subset and args.no_doctor)
                       else prev.get("agent_reach", {"ok": doctor.get("ok")}),
        "deltas": [b for b in backends if b.get("delta")],
    }
    kb_common._atomic_write(HEALTH, json.dumps(health, ensure_ascii=False, indent=1))
    write_note(DIR_INDEX / "渠道台账.md", {"type": "index", "title": "渠道台账",
                                          "updated": health["checked_at"],
                                          "tags": ["索引", "渠道"]},
               render_ledger(reg, health, doctor))
    if doctor.get("ok"):
        write_note(DIR_REPORT / "AgentReach体检.md",
                   {"type": "report", "title": "agent-reach 体检", "updated": doctor.get("checked_at"),
                    "tags": ["报告", "渠道", "agent-reach"]}, render_doctor_note(doctor))

    print(f"\n=== 体检汇总 {health['summary']} ===")
    for d in health["decisions"]:
        if d["action"] != "keep":
            print(f"  -> {d['channel_id']}: {d['action']} ({d['status']})")
    for b in health["deltas"]:
        print(f"  !! delta: {b['backend']}（doctor 声明 {b['declared']}，实测 {b['status']}）：{b['message'][:80]}")
    log.finish({"mode": "audit", "summary": health["summary"]})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
