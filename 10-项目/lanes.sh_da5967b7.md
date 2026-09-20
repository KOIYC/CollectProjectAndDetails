---
type: "project"
title: "Show HN: Run Claude Code sessions on Linear issues via two MCP servers"
project_url: "https://lanes.sh/blog/linear-to-lanes"
first_seen: "2026-09-21T02:52:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_s-xyz
  - story_47961204
  - show_hn
lang: "en"
---

# Show HN: Run Claude Code sessions on Linear issues via two MCP servers

> [!info] 一句话导读
> From Linear to Lanes: A Two-MCP Workflow

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://lanes.sh/blog/linear-to-lanes>
> 首次收录：2026-09-21T02:52:28+08:00
> 来源渠道：HN Show HN
> 标签：author_s-xyz, story_47961204, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/75013fb5bd21c4c8_Show-HN-Run-Claude-Code-sessions-on-Linear-issues]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/75013fb5bd21c4c8_Show-HN-Run-Claude-Code-sessions-on-Linear-issues]] |
| 2026-09-21T02:52:28+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/75013fb5bd21c4c8_Show-HN-Run-Claude-Code-sessions-on-Linear-issues]] |

## 摘要正文

# From Linear to Lanes: A Two-MCP Workflow  > A short tutorial on combining the Linear MCP and the local Lanes MCP, so you can pull tickets and start agent sessions on them directly from chat. > 2026-04-30  In this tutorial we'll walk through how to use the official Linear MCP and the local Lanes MCP together, so that an agent can pull issues out of Linear and spin up a session on them directly. The interesting part is that last word: directly. Once a Linear ticket lands on your Lanes board, starting a Claude Code, Codex, or shell session against it is one prompt away in the same chat. No copy-paste, no window swap, no second tool to learn.  The mechanic is simple. An agent that has both MCP servers connected can read your Linear backlog, drop selected tickets onto your local Lanes board, kick off a session in a fresh git worktree, and then sync the outcome back to Linear when it's done. We'll walk through each of those pieces in turn.  Watch the video  A short walkthrough of the flow described below: pulling a Linear ticket into Lanes and kicking off a session on it from a single chat.  ## The two servers  It's worth a quick word on what each server actually is before we wire them…
