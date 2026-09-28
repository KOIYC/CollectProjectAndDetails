---
type: "project"
title: "Show HN: Stepgate – an MCP server that won't let agents skip steps"
project_url: "https://github.com/Chaarangan/stepgate"
first_seen: "2026-09-28T09:47:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_charangan
  - story_49872350
  - show_hn
lang: "en"
---

# Show HN: Stepgate – an MCP server that won't let agents skip steps

> [!info] 一句话导读
> Agents can't skip steps: an MCP server that runs gated, API-only stepfiles on the client's own model.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Chaarangan/stepgate>
> 首次收录：2026-09-28T09:47:28+08:00
> 来源渠道：HN Show HN
> 标签：author_charangan, story_49872350, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-28T09:47:28+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-28/52248ab1a2b06fd9_Show-HN-Stepgate-–-an-MCP-server-that-won't-let-ag]] |

## 摘要正文

# Chaarangan/stepgate  Agents can't skip steps: an MCP server that runs gated, API-only stepfiles on the client's own model.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 11 - License: Apache License 2.0 - Homepage: https://www.npmjs.com/package/stepgate - Default branch: main - Created: 2026-09-26T22:32:52Z  ## Languages  - TypeScript  ## Topics  - agent-guardrails - ai-agents - jsonlogic - llm - mcp - mcp-server - model-context-protocol - openapi - typescript - workflow  ## Top Contributors  - Chaarangan (110 contributions)  ---  ## README  # Stepgate  CI npm License: Apache-2.0  **Agents can't skip steps.** Write an agent's procedure once, as a YAML stepfile, and run it from any MCP client, such as Claude Code, with the model that client already uses.  A **stepfile** declares its inputs, the remote APIs and MCP servers it may call, and an ordered list of steps. Each step says what output it must produce and which **gates** check that output. The file names no model and no framework.  **Stepgate** runs stepfiles. It is an MCP server that offers each stepfile as a tool. When a client's agent calls it, Stepgate shows the agent one step at a time, makes every API call the step…
