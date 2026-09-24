---
type: "channel"
channel_id: "github_new"
name: "GitHub 新星仓库"
group: "海外发布"
adapter: "github_new"
auth: "cli"
lang: "en"
status: "ok"
last_verified: "2026-09-22"
tags:
  - 渠道
  - 渠道/海外发布
params: {"window_days": 14, "min_stars": 20, "queries": ["created:>{since} stars:>={min_stars}", "topic:indie-hacker", "topic:side-project", "topic:microsaas"]}
---

# GitHub 新星仓库（`github_new`）

- **分组**：海外发布　|　**语言**：en　|　**认证**：cli
- **取数实现**：`github_new`　|　**单次上限**：30
- **补全类型**：readme
- **当前状态**：`ok`（本次 11 条，15.3s）
- **口径备注**：gh CLI（api.github.com 可达）；README 用 gh api .../readme 取全文
- **解锁方式**：—

## 运行历史

| 时间 | 状态 | 条数 | 耗时 | 消息 |
|---|---|---|---|---|
| 2026-09-20T02:36:04+08:00 | ok | 28 | 12.0s | 28 repos;  |
| 2026-09-20T02:57:03+08:00 | ok | 28 | 15.9s | 28 repos;  |
| 2026-09-20T03:05:52+08:00 | ok | 28 | 15.5s | 28 repos;  |
| 2026-09-20T03:18:37+08:00 | ok | 28 | 22.3s | 28 repos;  |
| 2026-09-20T03:30:14+08:00 | ok | 28 | 12.1s | 28 repos;  |
| 2026-09-20T03:40:12+08:00 | ok | 28 | 14.0s | 28 repos;  |
| 2026-09-20T09:24:19+08:00 | ok | 58 | 19.5s | 261 repos;  |
| 2026-09-20T09:49:22+08:00 | ok | 10 | 11.8s | 28 repos;  |
| 2026-09-21T01:09:41+08:00 | ok | 1 | 13.9s | 88 repos;  |
| 2026-09-21T01:13:52+08:00 | ok | 1 | 9.5s | 88 repos;  |
| 2026-09-21T01:27:49+08:00 | ok | 1 | 12.0s | 88 repos;  |
| 2026-09-21T01:30:20+08:00 | ok | 0 | 11.3s | 88 repos;  |
| 2026-09-21T01:32:11+08:00 | ok | 2 | 11.8s | 88 repos;  |
| 2026-09-21T01:34:25+08:00 | ok | 1 | 11.4s | 88 repos;  |
| 2026-09-21T09:45:37+08:00 | ok | 10 | 13.8s | 28 repos;  |
| 2026-09-22T12:54:21+08:00 | error | 0 | 3.1s | 0 repos; created:>2026-09-08 stars:>=: error connecting to api.github. |
| 2026-09-22T13:06:08+08:00 | ok | 11 | 12.2s | 28 repos;  |
| 2026-09-22T14:16:47+08:00 | ok | 11 | 15.3s | 28 repos;  |
