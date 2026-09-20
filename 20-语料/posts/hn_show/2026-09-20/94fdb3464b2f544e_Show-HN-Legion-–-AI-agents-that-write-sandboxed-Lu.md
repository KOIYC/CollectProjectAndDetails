---
type: "corpus"
item_id: "94fdb3464b2f544e"
title: "Show HN: Legion – AI agents that write sandboxed Lua inside your Elixir app"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49726662"
project_url: "https://legion.swmansion.com/"
author: "dimamik"
published_at: "2026-09-16T13:23:20Z"
captured_at: "2026-09-20T09:37:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_dimamik
  - story_49726662
  - show_hn
metrics: {"points": 9, "comments": 0, "engagement_velocity": 9}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Legion – AI agents that write sandboxed Lua inside your Elixir app

> [!info] 一句话导读
> We can't find the internet

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49726662>
> 指标：点赞=9 · 评论=0 · engagement_velocity=9
> 作者：dimamik　|　发布：2026-09-16T13:23:20Z
> 项目链接：<https://legion.swmansion.com/>
> 采集：2026-09-20T09:37:03+08:00　|　id：`94fdb3464b2f544e`

## 正文

We can't find the internet

Attempting to reconnect

Something went wrong!

Attempting to reconnect

Open source Elixir library created by

# This page has an agent inside it. Give it an instruction.

Legion is an Elixir runtime for AI agents that live inside your application and get things done by writing code.

Nothing drawn yet. Ask it to show you how it works.

In plain words

## The easiest way to put AI agents inside your app.

### An agent that actually does things

Instead of a chatbot that only talks, a Legion agent reaches into your application and acts: finds records, runs reports, changes settings, files the ticket. You decide which functions it may touch.

### Chat is the least of it

The same agent can sit behind a chat window, power an MCP server for Claude or Cursor, or run as a background worker that clears a queue overnight. One runtime, many shapes.

### Production essentials come in the box

Every action runs in a sandbox with time and memory limits, conversations are saved in your own database, and a dashboard shows exactly what the agent did and why. Nothing extra to buy or operate.

F-01

TOOL CALLING LEGION 5 HOPS 1 PASS

## Code instead of one-off tool calls

Agents can run vetted Lua (or Elixir) code that composes your tools to achieve things that were impossible before - with near zero configuration.

F-02

SANDBOX

YOUR TOOLS TIMEOUT · MEMORY · CPU

## Sandboxed by default

Every evaluation runs in a monitored process with timeout, memory, and CPU budgets. Lua can't reach the host BEAM at all - the only way out is the tools you registered.

F-03

PostsTool use Legion.Tool

AGENT ANY MODULE

## Tools are plain modules

`use Legion.Tool` on any module and the agent reads its source and calls its functions directly. Nothing to define, nothing to keep in sync as your app changes.

F-04

AUTH BOUNDARY AGENT TOOLS 42 USER CONTEXT

## Scoped to the signed-in user

Set auth context before the agent starts and read it inside your tools at runtime. Every call the agent makes is scoped to that user, and the generated code never sees the credentials.

F-05

CALL SUPERVISION TREE

## Agents are BEAM processes

Start one, keep it around, message it like a GenServer. Supervision trees, pools, and agents that delegate to other agents all work the way you expect.

F-06

NODE A DEPLOY NODE B

USER_42:CHAT_7

## Backed by your Postgres

Point Legion at your Repo and you'll have persistence and rate limiting for your agents.

F-07

TRACE · USER_42:CHAT_7 LIVE · LEGION_WEB AGENT MESSAGE ITERATION LLM SANDBOX

## Observability is included

Telemetry events at every level - agent, message, iteration, LLM call, sandbox eval - and the legion_web LiveView dashboard shows live conversations and every line of code an agent writes.

Dim the lights and show me how you work.

## We are Software Mansion

You might know us from Elixir Stream Week, Global Elixir Meetups, or from projects like Popcorn and Membrane. But that’s not all we do.

We help teams build exceptional software - from developer tools to production-ready applications. Let’s talk about how we can support your next project.

Contact us Contribute on GitHub

# Airmash • Massively Multiplayer Missile Warfare

## 导航

- 项目页：[[10-项目/legion.swmansion.com_78bb4971]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
