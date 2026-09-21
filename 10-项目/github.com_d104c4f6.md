---
type: "project"
title: "Show HN: AgentTrace–Observability and runtime self-healing engine for AI agents"
project_url: "https://github.com/mohitkumar188/AgentTrace"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mohitkumar18
  - story_49780222
  - show_hn
lang: "en"
---

# Show HN: AgentTrace–Observability and runtime self-healing engine for AI agents

> [!info] 一句话导读
> mohitkumar188/AgentTrace

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mohitkumar188/AgentTrace>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_mohitkumar18, story_49780222, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/2aa529b0f696c898_Show-HN-AgentTrace–Observability-and-runtime-self]] |

## 摘要正文

# mohitkumar188/AgentTrace  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - Homepage: https://agent-trace-zeta.vercel.app - Default branch: main - Created: 2026-09-06T11:07:22Z  ## Languages  - CSS - JavaScript - Python - TypeScript  ## Top Contributors  - mohitkumar188 (7 contributions)  ---  ## README  # ⚡ AgentTrace: Production-Grade Agent Observability & Self-Healing Engine Live Dashboard Backend API License: MIT  > **Live Production Demo:** > * 🖥️ **Interactive Web Dashboard:** https://agent-trace-zeta.vercel.app/ > * ⚙️ **FastAPI Swagger Docs:** https://agenttrace-api-cdav.onrender.com/docs  An end-to-end observability SDK and dashboard for autonomous AI agent pipelines. It monitors multi-step tool calls, visualizes latency bottlenecks, and automatically repairs malformed LLM tool arguments at runtime without crashing workflows.  ---  ## 🎯 The Problem LLMs frequently hallucinate tool arguments during multi-step runs: * Passing strings instead of floats (e.g. `"1200 INR"` instead of `1200.0`) * Inventing key names (e.g. `"user_identifier"` instead of `"user_id"`) * Omitting required schema fields  Normally, these cause immediate runtime crashes. AgentTrace catches these…
