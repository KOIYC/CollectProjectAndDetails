---
type: "channel"
channel_id: "xiaohongshu"
name: "小红书"
group: "中文社媒"
adapter: "opencli_social"
auth: "browser"
lang: "zh"
status: "ok"
last_verified: "2026-10-01"
tags:
  - 渠道
  - 渠道/中文社媒
params: {"site": "xiaohongshu", "queries": ["独立开发", "独立开发者", "小众软件 出海"]}
---

# 小红书（`xiaohongshu`）

- **分组**：中文社媒　|　**语言**：zh　|　**认证**：browser
- **取数实现**：`opencli_social`　|　**单次上限**：45
- **补全类型**：fulltext
- **当前状态**：`ok`（本次 1 条，37.0s）
- **口径备注**：2026-09-22 实测已解锁：opencli doctor 报 daemon running + Extension connected(v1.0.22)， `opencli xiaohongshu search` 15.8s 返回 20 条，kb_audit 判 ok。 依赖：Chrome 必须开着且小红书网页端有登录态 —— 扩展在但站点没登录时仍会失败（X 就是这种情况）。 **2026-09-26 复测回落到 auth**（`BROWSER_CONNECT` / `ok: false`）→ 属浏览器端状态，不是渠道腐化： 保持 `enabled: true`（本机开 Chrome 登录后自动恢复），不写 disabled 段。 **2026-09-28 复测已回升 `ok`**（15.4s / 1 条 / 1 路查询）—— 证实上一轮「浏览器端状态、非渠道腐化」的判断： 这类 `auth` 在启停决策里**不应计入腐化**，只需复检。 已知限制：① url 带 xsec_token（有时效）→ item_id 不稳，应剥 xsec_* 再做去重键； ② 无正文 enricher，body 仅为元数据块、likes 未进 metrics； ③ fix: 已改 3 路 query 全部执行（之前只跑 queries[0]）。
- **解锁方式**：装 OpenCLI 浏览器扩展并保持 Chrome 打开（chrome web store: OpenCLI）；或 agent-reach configure xhs-cookies 走 xiaohongshu-mcp

## 运行历史

| 时间 | 状态 | 条数 | 耗时 | 消息 |
|---|---|---|---|---|
| 2026-09-20T02:38:58+08:00 | auth | 0 | 46.9s | 需 OpenCLI 浏览器扩展/登录态：(node:31952) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:02:10+08:00 | auth | 0 | 46.8s | 需 OpenCLI 浏览器扩展/登录态：(node:35868) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:11:08+08:00 | auth | 0 | 46.8s | 需 OpenCLI 浏览器扩展/登录态：(node:20572) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:24:29+08:00 | auth | 0 | 46.5s | 需 OpenCLI 浏览器扩展/登录态：(node:34232) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:36:00+08:00 | auth | 0 | 47.0s | 需 OpenCLI 浏览器扩展/登录态：(node:30608) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:44:24+08:00 | auth | 0 | 46.8s | 需 OpenCLI 浏览器扩展/登录态：(node:25560) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T09:53:29+08:00 | auth | 0 | 46.2s | 需 OpenCLI 浏览器扩展/登录态：ok: false
| 2026-09-21T01:29:18+08:00 | ok | 1 | 10.4s | 20 items |
| 2026-09-21T01:31:18+08:00 | ok | 1 | 12.9s | 20 items |
| 2026-09-21T01:33:02+08:00 | ok | 1 | 12.0s | 20 items |
| 2026-09-21T01:35:21+08:00 | ok | 1 | 13.2s | 20 items |
| 2026-09-21T09:49:50+08:00 | ok | 1 | 13.7s | 20 items |
| 2026-09-22T13:00:59+08:00 | auth | 0 | 137.6s | 需 OpenCLI 浏览器扩展/登录态：独立开发: ok: false
| 2026-09-22T14:25:27+08:00 | auth | 0 | 137.5s | 需 OpenCLI 浏览器扩展/登录态：独立开发: ok: false
| 2026-09-25T00:10:00+08:00 | auth | 0 | 139.3s | 需 OpenCLI 浏览器扩展/登录态：独立开发: ok: false
| 2026-09-25T13:51:26+08:00 | auth | 0 | 139.2s | 需 OpenCLI 浏览器扩展/登录态：独立开发: ok: false
| 2026-09-26T09:54:10+08:00 | auth | 0 | 138.7s | 需 OpenCLI 浏览器扩展/登录态：独立开发: ok: false
| 2026-09-28T09:53:25+08:00 | ok | 1 | 35.9s | 1 items（3 路查询） |
| 2026-09-29T09:47:02+08:00 | ok | 1 | 41.1s | 1 items（3 路查询） |
| 2026-09-30T18:53:53+08:00 | ok | 1 | 27.7s | 1 items（3 路查询） |
| 2026-10-01T09:49:12+08:00 | ok | 1 | 37.0s | 1 items（3 路查询） |
