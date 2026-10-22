---
type: "project"
title: "Show HN: Renor – private memory for coding agents, shared across tools over MCP"
project_url: "https://github.com/patrickpassosb/renor-engine"
first_seen: "2026-10-22T09:46:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_patrickpassosbb
  - story_50186146
  - show_hn
lang: "en"
---

# Show HN: Renor – private memory for coding agents, shared across tools over MCP

> [!info] 一句话导读
> patrickpassosb/renor-engine

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/patrickpassosb/renor-engine>
> 首次收录：2026-10-22T09:46:18+08:00
> 来源渠道：HN Show HN
> 标签：author_patrickpassosbb, story_50186146, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:46:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-22/883dc403dd0a0741_Show-HN-Renor-–-private-memory-for-coding-agents,]] |

## 摘要正文

# patrickpassosb/renor-engine  Memory for coding agents: Markdown notes in a folder, recalled later over MCP. AGPL-3.0.  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: GNU Affero General Public License v3.0 - Homepage: https://renor.cloud - Default branch: main - Created: 2026-10-13T20:48:26Z  ## Languages  - JavaScript - Python - Shell - TypeScript  ## Topics  - agent-memory - agpl - ai-memory - claude-code - codex - llm-memory - markdown - mcp - model-context-protocol - sqlite  ## Top Contributors  - patrickpassosb (3 contributions)  ---  ## README  # Renor  engine-public-ci  **Renor is memory for coding agents.** You keep notes as Markdown files in a folder on your machine. Renor indexes them and serves them to any MCP client (Claude Code, Codex and others), so an agent can recall what you already decided instead of asking you to paste the same context again.  **Try it.** After the install and index steps below, stop `node dist/cli.js mcp` if you left it running (Claude Code starts its own), then, in the same terminal and from this directory, with Node 22 as the `node` on your `PATH`, add Renor to Claude Code over MCP:  ```bash claude mcp add --scope local renor…
