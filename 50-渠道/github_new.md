---
type: "channel"
channel_id: "github_new"
name: "GitHub 新星仓库"
group: "海外发布"
adapter: "github_new"
auth: "cli"
lang: "en"
status: "ok"
last_verified: "2026-09-20"
tags:
  - 渠道
  - 渠道/海外发布
params: {"window_days": 14, "min_stars": 20, "queries": ["created:>{since} stars:>={min_stars}", "topic:indie-hacker", "topic:side-project", "topic:microsaas"]}
---

# GitHub 新星仓库（`github_new`）

- **分组**：海外发布　|　**语言**：en　|　**认证**：cli
- **取数实现**：`github_new`　|　**单次上限**：30
- **补全类型**：readme
- **当前状态**：`ok`（本次 10 条，11.8s）
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
