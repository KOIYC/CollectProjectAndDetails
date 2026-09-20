---
type: "project"
title: "Show HN: Bough, the agent I built to replace Claude Code at work"
project_url: "https://github.com/andreylukin/bough"
first_seen: "2026-09-20T14:06:38+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_alukin
  - story_49711939
  - show_hn
lang: "en"
---

# Show HN: Bough, the agent I built to replace Claude Code at work

> [!info] 一句话导读
> A coding agent that acts by writing programs: one JavaScript program per round — loops, branching, composition — run against your real checkout. Rust, terminal …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/andreylukin/bough>
> 首次收录：2026-09-20T14:06:38+08:00
> 来源渠道：HN Show HN
> 标签：author_alukin, story_49711939, show_hn
> 最新指标：点赞=10 · 评论=5 · engagement_velocity=10

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/c31e0fc8ba6458a9_Show-HN-Bough,-the-agent-I-built-to-replace-Claude]] |
| 2026-09-20T09:37:18+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/c31e0fc8ba6458a9_Show-HN-Bough,-the-agent-I-built-to-replace-Claude]] |
| 2026-09-20T14:06:38+08:00 | HN Show HN | 点赞=10 · 评论=5 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/c31e0fc8ba6458a9_Show-HN-Bough,-the-agent-I-built-to-replace-Claude]] |

## 摘要正文

# andreylukin/bough  A coding agent that acts by writing programs: one JavaScript program per round — loops, branching, composition — run against your real checkout. Rust, terminal UI.  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 7 - License: Apache License 2.0 - Default branch: main - Created: 2026-06-18T13:42:59Z  ## Languages  - JavaScript - Lua - Makefile - Python - Ruby - Rust - Shell  ## Topics  - agent - ai - coding-agent - developer-tools - llm - ratatui - rust - tui  ## Top Contributors  - andreylukin (833 contributions) - claude (41 contributions)  ---  ## README   bough   A coding agent that acts by writing programs.  One JavaScript program per round, with real loops and branching, run against your real checkout.  **bough** rhymes with *now*, not with *dough*: /baʊ/. It is the word for a branch of a tree, which is what a conversation is here: you fork a turn and the old line goes on living as a branch.  Most harnesses let the model emit one tool call and wait. bough gives it a single tool that takes a program: the model writes JavaScript with real control flow, and a harness executes it on your machine. A headless server owns all state and execution; the terminal …
