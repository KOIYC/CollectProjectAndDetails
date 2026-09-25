---
type: "channel"
channel_id: "twitter"
name: "X / Twitter"
group: "海外社媒"
adapter: "opencli_social"
auth: "browser"
lang: "en"
status: "auth"
last_verified: "2026-09-25"
tags:
  - 渠道
  - 渠道/海外社媒
params: {"site": "twitter", "queries": ["build in public indie hacker", "indie hacker MRR"]}
---

# X / Twitter（`twitter`）

- **分组**：海外社媒　|　**语言**：en　|　**认证**：browser
- **取数实现**：`opencli_social`　|　**单次上限**：15
- **补全类型**：fulltext
- **当前状态**：`auth`（本次 0 条，103.7s）
- **口径备注**：2026-09-21 实测：OpenCLI 扩展**已连接**，失败原因是 x.com 自身没登录。 解锁 = 开 Chrome 登录 https://x.com 即可。
- **解锁方式**：opencli twitter（装扩展）或 pipx install twitter-cli + 导出 TWITTER_AUTH_TOKEN/TWITTER_CT0

## 运行历史

| 时间 | 状态 | 条数 | 耗时 | 消息 |
|---|---|---|---|---|
| 2026-09-20T02:39:44+08:00 | auth | 0 | 46.6s | 需 OpenCLI 浏览器扩展/登录态：(node:22060) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:02:57+08:00 | auth | 0 | 46.5s | 需 OpenCLI 浏览器扩展/登录态：(node:32108) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:11:54+08:00 | auth | 0 | 46.4s | 需 OpenCLI 浏览器扩展/登录态：(node:28892) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:25:18+08:00 | auth | 0 | 49.0s | 需 OpenCLI 浏览器扩展/登录态：(node:35072) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:36:47+08:00 | auth | 0 | 46.5s | 需 OpenCLI 浏览器扩展/登录态：(node:30124) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T03:45:11+08:00 | auth | 0 | 46.6s | 需 OpenCLI 浏览器扩展/登录态：(node:29588) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-20T09:54:15+08:00 | auth | 0 | 46.0s | 需 OpenCLI 浏览器扩展/登录态：ok: false
| 2026-09-21T01:29:19+08:00 | auth | 0 | 1.8s | 需 OpenCLI 浏览器扩展/登录态：(node:16248) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-21T01:31:22+08:00 | auth | 0 | 3.1s | 需 OpenCLI 浏览器扩展/登录态：(node:21356) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-21T01:33:04+08:00 | auth | 0 | 2.3s | 需 OpenCLI 浏览器扩展/登录态：(node:33156) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-21T01:35:24+08:00 | auth | 0 | 3.1s | 需 OpenCLI 浏览器扩展/登录态：(node:27436) [UNDICI-EHPA] Warning: EnvHttpProxyAg |
| 2026-09-21T09:49:57+08:00 | auth | 0 | 6.5s | 需 OpenCLI 浏览器扩展/登录态：ok: false
| 2026-09-22T13:02:31+08:00 | auth | 0 | 92.0s | 需 OpenCLI 浏览器扩展/登录态：build in public indie hacker: ok: false
| 2026-09-22T14:26:59+08:00 | auth | 0 | 91.7s | 需 OpenCLI 浏览器扩展/登录态：build in public indie hacker: ok: false
| 2026-09-25T00:07:40+08:00 | auth | 0 | 103.7s | 需 OpenCLI 浏览器扩展/登录态：build in public indie hacker: ok: false
error:
  c |
