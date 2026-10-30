---
type: "report"
title: "agent-reach 体检"
updated: "2026-10-30T09:44:56+08:00"
tags:
  - 报告
  - 渠道
  - agent-reach
---

# agent-reach 体检

> 检查时间 2026-10-30T09:44:56+08:00 · agent-reach 1.6.0 · 由 `agent-reach doctor`（默认输出 JSON）生成

| 平台 | | 状态 | 激活后端 | 说明 |
|---|---|---|---|---|
| GitHub 仓库和代码 | ⚠️ | unverified | `—` | agent-reach check github |
| Twitter/X 推文 | ❌ | not_added | `—` | agent-reach add twitter |
| YouTube 视频和字幕 | ⚠️ | unverified | `—` | agent-reach check youtube |
| Reddit 帖子和评论 | ❌ | not_added | `—` | agent-reach add reddit |
| Facebook 帖子、主页和群组 | ❌ | not_added | `—` | agent-reach add facebook |
| Instagram 用户、主页和指定用户帖子 | ❌ | not_added | `—` | agent-reach add instagram |
| B站视频、字幕和搜索 | ⚠️ | unverified | `—` | agent-reach check bilibili |
| 小红书笔记 | ❌ | not_added | `—` | agent-reach add xiaohongshu |
| LinkedIn 职业社交 | ❌ | not_added | `—` | agent-reach add linkedin |
| boss | ❌ | not_added | `—` | agent-reach add boss |
| V2EX 节点、主题与回复 | ⚠️ | unverified | `—` | agent-reach check v2ex |
| 雪球股票行情与社区动态 | ❌ | not_added | `—` | agent-reach add xueqiu |
| 小宇宙播客转文字 | ❌ | not_added | `—` | agent-reach add xiaoyuzhou |
| 任意网页 | ⚠️ | unverified | `—` | agent-reach check web |

## 与 KB 渠道的对应关系

| KB 渠道 | 依赖的 agent-reach 平台 | 说明 |
|---|---|---|
| `hn_show` / `reddit` / `lobsters` / `devto` / `producthunt` | 无（直连 API/RSS） | 零配置，不依赖 agent-reach 后端 |
| `github_new` | github (gh CLI) | doctor 只查配置不实测，以 kb_audit 探针为准 |
| `v2ex` | web (Jina) / 直连 sov2ex | 官方 API 本网络 502，已改 sov2ex |
| `exa_discovery` | exa_search (mcporter) | doctor 不连通验证，以探针为准 |
| `xiaohongshu` | xiaohongshu（OpenCLI / xhs-mcp） | 需浏览器登录态 |
| `twitter` | twitter（OpenCLI / twitter-cli） | 需扩展或 Cookie |
| `bilibili` | bilibili | 直连搜索 API 可用（带 Referer），无需登录 |
