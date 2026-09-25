---
type: "project"
title: "tamaratran/fast-jev-compaction"
project_url: "https://github.com/tamaratran/fast-jev-compaction"
first_seen: "2026-09-24T23:59:53+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - TypeScript
  - created:>2026-09-10
lang: "en"
---

# tamaratran/fast-jev-compaction

> [!info] 一句话导读
> Claude Code plugin that replaces the compaction summary with Jev decisions:

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tamaratran/fast-jev-compaction>
> 首次收录：2026-09-24T23:59:53+08:00
> 来源渠道：GitHub 新星仓库
> 标签：TypeScript, created:>2026-09-10
> 最新指标：stars=6686 · forks=390 · open_issues=81

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:35:53+08:00 | GitHub 新星仓库 | stars=4042 · forks=213 · open_issues=47 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-20T02:56:49+08:00 | GitHub 新星仓库 | stars=4055 · forks=213 · open_issues=47 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-20T03:05:39+08:00 | GitHub 新星仓库 | stars=4059 · forks=213 · open_issues=47 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-20T03:18:17+08:00 | GitHub 新星仓库 | stars=4063 · forks=213 · open_issues=47 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-20T03:30:04+08:00 | GitHub 新星仓库 | stars=4067 · forks=213 · open_issues=47 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-20T03:40:00+08:00 | GitHub 新星仓库 | stars=4071 · forks=214 · open_issues=47 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-20T09:49:12+08:00 | GitHub 新星仓库 | stars=4277 · forks=228 · open_issues=48 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-21T09:45:26+08:00 | GitHub 新星仓库 | stars=5222 · forks=287 · open_issues=58 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-22T13:05:57+08:00 | GitHub 新星仓库 | stars=6048 · forks=336 · open_issues=71 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-22T14:16:34+08:00 | GitHub 新星仓库 | stars=6069 · forks=342 · open_issues=71 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |
| 2026-09-24T23:59:53+08:00 | GitHub 新星仓库 | stars=6686 · forks=390 · open_issues=81 | [[20-语料/posts/github_new/2026-09-20/5d1053d9f00a3609_tamaratran-fast-jev-compaction]] |

## 摘要正文

# fast-jev-compaction  Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim. Also usable as an npm library.  ## What and why  Most context compaction asks an LLM to summarize old turns. A summary is lossy: a file path, exact error, constraint, or command can disappear even when it matters later. This library never rewrites anything. It only deletes tool calls and tool results Jev says are no longer needed, and it asks Jev while showing it the whole conversation. User and assistant text stays verbatim and in order.  The repository is both an npm package (`src/`) and a Claude Code plugin (`hooks/`, `.claude-plugin/`) that uses the package to replace Claude Code's built-in compaction summary with the original messages.  ## How it works  1. Every `tool_use` is paired with its `tool_result` by `tool_use_id`. Calls in    the first message or in the newest `preserveRecentMessages` messages are    pinned and never touched. 2. The **state** sent to Jev is the whole conversation so far, oldest first,    with every tool result replaced by a short…
