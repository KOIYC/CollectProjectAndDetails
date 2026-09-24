---
type: "channel"
channel_id: "reddit"
name: "Reddit 独立开发版块"
group: "海外社区"
adapter: "reddit_arctic"
auth: "none"
lang: "en"
status: "ok"
last_verified: "2026-09-22"
tags:
  - 渠道
  - 渠道/海外社区
params: {"subs": ["SideProject", "indiehackers", "microsaas", "SaaS", "EntrepreneurRideAlong", "buildinpublic", "selfhosted", "indiedev"], "window_days": 7, "settle_days": 3, "min_score": 3, "sort": "desc"}
---

# Reddit 独立开发版块（`reddit`）

- **分组**：海外社区　|　**语言**：en　|　**认证**：none
- **取数实现**：`reddit_arctic`　|　**单次上限**：30
- **补全类型**：comments
- **当前状态**：`ok`（本次 24 条，115.0s）
- **口径备注**：arctic-shift 镜像（匿名可用）。① 本网络 www.reddit.com 直连 502；② after 只吃 epoch 秒/纯日期，带时区 ISO 会 400；③ **score 有装载延迟**——近 3 天帖子分数未沉淀（实测近 3 天 max=1、7-14 天前 max=42），故用 settle_days=3 取「3~10 天前」窗口
- **解锁方式**：—

## 运行历史

| 时间 | 状态 | 条数 | 耗时 | 消息 |
|---|---|---|---|---|
| 2026-09-20T02:36:24+08:00 | ok | 21 | 19.7s | 21 posts;  |
| 2026-09-20T02:41:45+08:00 | ok | 22 | 14.9s | 22 posts;  |
| 2026-09-20T02:44:17+08:00 | ok | 22 | 27.0s | 22 posts;  |
| 2026-09-20T02:48:07+08:00 | ok | 18 | 25.2s | 18 posts;  |
| 2026-09-20T02:57:29+08:00 | ok | 20 | 26.0s | 20 posts;  |
| 2026-09-20T03:06:42+08:00 | ok | 27 | 49.5s | 27 posts;  |
| 2026-09-20T03:19:18+08:00 | ok | 27 | 40.4s | 27 posts;  |
| 2026-09-20T03:31:07+08:00 | ok | 26 | 52.4s | 26 posts;  |
| 2026-09-20T03:40:47+08:00 | ok | 25 | 35.5s | 25 posts;  |
| 2026-09-20T09:24:59+08:00 | ok | 84 | 39.7s | 84 posts;  |
| 2026-09-20T09:49:55+08:00 | ok | 26 | 32.7s | 26 posts;  |
| 2026-09-21T01:10:20+08:00 | ok | 26 | 38.4s | 26 posts;  |
| 2026-09-21T01:14:47+08:00 | ok | 26 | 55.4s | 26 posts;  |
| 2026-09-21T01:28:09+08:00 | ok | 25 | 19.4s | 25 posts;  |
| 2026-09-21T01:30:38+08:00 | ok | 20 | 18.0s | 20 posts;  |
| 2026-09-21T01:32:30+08:00 | ok | 26 | 19.6s | 26 posts;  |
| 2026-09-21T01:34:45+08:00 | ok | 31 | 20.3s | 31 posts;  |
| 2026-09-21T09:46:37+08:00 | ok | 22 | 59.7s | 22 posts;  |
| 2026-09-22T12:55:24+08:00 | ok | 26 | 63.3s | 26 posts;  |
| 2026-09-22T14:18:42+08:00 | ok | 24 | 115.0s | 24 posts;  |
