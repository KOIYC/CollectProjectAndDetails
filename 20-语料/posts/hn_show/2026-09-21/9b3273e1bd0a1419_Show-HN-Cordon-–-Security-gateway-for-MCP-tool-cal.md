---
type: "corpus"
item_id: "9b3273e1bd0a1419"
title: "Show HN: Cordon – Security gateway for MCP tool calls with HITL approvals"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47941823"
project_url: "https://github.com/marras0914/cordon"
author: "babas03"
published_at: "2026-04-28T22:39:22Z"
captured_at: "2026-09-21T01:42:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-28"
tags:
  - 语料
  - hn_show
  - author_babas03
  - story_47941823
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: Cordon – Security gateway for MCP tool calls with HITL approvals

> [!info] 一句话导读
> MCP lets LLMs call real tools, databases, file systems, APIs. The spec has no security model. An agent is either off or full admin, and "trust the model" is the…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47941823>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：babas03　|　发布：2026-04-28T22:39:22Z
> 项目链接：<https://github.com/marras0914/cordon>
> 采集：2026-09-21T01:42:36+08:00　|　id：`9b3273e1bd0a1419`

## 正文

MCP lets LLMs call real tools, databases, file systems, APIs. The spec has no security model. An agent is either off or full admin, and "trust the model" is the current answer.Cordon is an open source MCP gateway. It's a transparent proxy that sits between your LLM client and your MCP servers. Every tool call flows through it. You define policies per tool: allow, block, approve, read only, log only.The piece I haven't seen elsewhere is synchronous human-in-the-loop approvals. When a tool call hits an "approve" policy, the agent pauses and I get a terminal prompt (or a Slack Block Kit message) with the exact args. I approve or deny. The agent resumes. Every decision is logged.Install: `npx cordon-cli init` auto-patches your Claude Desktop config in about two minutes. Works with Claude Desktop, Claude Code, Cursor, Windsurf, and any stdio MCP client.Open source, MIT. Published to the official MCP registry as io.github.marras0914/cordon. There's also a hosted dashboard for centralized audit logs, but the gateway runs local and the CLI is fully offline.Happy to answer questions about the threat model, why I built it as a proxy vs. a client-side wrapper, or how write-detection works without me enumerating every dangerous tool name.GitHub: https://github.com/marras0914/cordon
Writeup with config examples: https://dev.to/marras0914/mcp-has-no-security-model-heres-ho...
Approval flow demo: https://i.imgur.com/nDAVxqN.gif

## 评论（1/1）

> **babas03** · 2026-04-29T00:41:37.000Z　
> Author here. Built this after catching myself running autonomous agents on a NUC at home with direct Postgres access and realizing I didnt have an answer for "what happens when the model has a bad day?" The MCP spec doesn't draw any lines and "just don't connect the database" isn't really an answer.Happy to go deep on the threat model, the proxy-vs-wrapper architecture decision, or the HITL approval design. Also open to arguments that this is solving the wrong problem.

## 关联链接

- https://dev.to/marras0914/mcp-has-no-security-model-heres-ho...
- https://i.imgur.com/nDAVxqN.gif

## 导航

- 项目页：[[10-项目/github.com_10688e49]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
