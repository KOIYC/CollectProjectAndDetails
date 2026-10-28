---
type: "project"
title: "Show HN: I built flightdeck – Observability and control plane for AI agents"
project_url: "https://flightdeck-hq.com/"
first_seen: "2026-10-28T09:39:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pykul
  - story_50263709
  - show_hn
lang: "en"
---

# Show HN: I built flightdeck – Observability and control plane for AI agents

> [!info] 一句话导读
> Self-hosted · Apache 2.0

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://flightdeck-hq.com/>
> 首次收录：2026-10-28T09:39:16+08:00
> 来源渠道：HN Show HN
> 标签：author_pykul, story_50263709, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-28T09:39:16+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-28/ec154dc17c078c2d_Show-HN-I-built-flightdeck-–-Observability-and-con]] |

## 摘要正文

Quickstart  Releases  GitHub ★ Self-hosted · Apache 2.0 · Production and coding agents Observability and control plane for AI agent fleets . Every LLM call, MCP event, and tool call your agents make streams to the dashboard as it happens,  surfaced as a per-agent timeline and as a live fleet-wide feed.  Set token budgets, MCP allow/block rules, and live directives on your production agents. View on GitHub  Quickstart Coding agents attach via the Claude Code plugin . Production agents add the flightdeck-sensor Python package to their entrypoint: init() + patch() , no other code changes. Fleet view Streaming Paused research-agent support-triage claude-code · omri etl-summarizer llm_call  tool_use  mcp_event  policy_warn / degrade  policy_block / kill One row per agent, sub-agents nested under their parents, events plotted as they arrive. Hover any event to inspect it; hovering pauses the stream. What it does Live fleet view Every agent on a shared timeline: LLM calls, embeddings, tool uses, MCP events, and structured errors, streamed as they happen. Click any event to inspect it. Budgets that act Central token budgets per flavor, enforced in-process. Warn at 80%, swap to a cheaper mo…
