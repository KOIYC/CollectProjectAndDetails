---
type: "project"
title: "Show HN: ctx – Git blame that returns the original agent transcript"
project_url: "https://ctx.rs/pro"
first_seen: "2026-09-20T14:04:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_luca-ctx
  - story_49727859
  - show_hn
lang: "en"
---

# Show HN: ctx – Git blame that returns the original agent transcript

> [!info] 一句话导读
> ctx pro: git blame, but for agent sessions - ctx

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://ctx.rs/pro>
> 首次收录：2026-09-20T14:04:09+08:00
> 来源渠道：HN Show HN
> 标签：author_luca-ctx, story_49727859, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/db3f9d50a88e65ec_Show-HN-ctx-–-Git-blame-that-returns-the-original]] |
| 2026-09-20T09:37:02+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/db3f9d50a88e65ec_Show-HN-ctx-–-Git-blame-that-returns-the-original]] |
| 2026-09-20T14:04:09+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/db3f9d50a88e65ec_Show-HN-ctx-–-Git-blame-that-returns-the-original]] |

## 摘要正文

ctx pro: git blame, but for agent sessions - ctx  # ctx pro: git blame, but for agent sessions  Map a line, file, commit, or PR back to the coding-agent session that produced it, with citations to the original transcript and tool calls.  `git blame` tells you which commit last changed a line. `ctx blame` tells you which agent session produced that commit, with exact citations back to the original transcript and recorded tool calls.  Agents use `ctx blame` to recover context that no longer exists anywhere near the current session. Starting from a file, line range, commit, or PR, they can find the relevant historical agent sessions and recover the decisions, constraints, failed approaches, and assumptions recorded there.  This helps agents:  - recover constraints and decisions no longer visible in the code - uncover assumptions embedded in earlier changes - avoid retrying approaches that already failed - resume work without relying on lossy compaction summaries - audit past agent work to improve instructions, tools, and workflows  Every attribution includes citations back to the original transcript and tool calls. If the session is not on your machine (for example, because a teammate…
