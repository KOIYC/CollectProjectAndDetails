---
type: "project"
title: "Show HN: Cordon – Security gateway for MCP tool calls with HITL approvals"
project_url: "https://github.com/marras0914/cordon"
first_seen: "2026-09-21T01:42:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_babas03
  - story_47941823
  - show_hn
lang: "en"
---

# Show HN: Cordon – Security gateway for MCP tool calls with HITL approvals

> [!info] 一句话导读
> MCP lets LLMs call real tools, databases, file systems, APIs. The spec has no security model. An agent is either off or full admin, and "trust the model" is the…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/marras0914/cordon>
> 首次收录：2026-09-21T01:42:36+08:00
> 来源渠道：HN Show HN
> 标签：author_babas03, story_47941823, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/9b3273e1bd0a1419_Show-HN-Cordon-–-Security-gateway-for-MCP-tool-cal]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/9b3273e1bd0a1419_Show-HN-Cordon-–-Security-gateway-for-MCP-tool-cal]] |
| 2026-09-21T01:42:36+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/9b3273e1bd0a1419_Show-HN-Cordon-–-Security-gateway-for-MCP-tool-cal]] |

## 摘要正文

MCP lets LLMs call real tools, databases, file systems, APIs. The spec has no security model. An agent is either off or full admin, and "trust the model" is the current answer.Cordon is an open source MCP gateway. It's a transparent proxy that sits between your LLM client and your MCP servers. Every tool call flows through it. You define policies per tool: allow, block, approve, read only, log only.The piece I haven't seen elsewhere is synchronous human-in-the-loop approvals. When a tool call hits an "approve" policy, the agent pauses and I get a terminal prompt (or a Slack Block Kit message) with the exact args. I approve or deny. The agent resumes. Every decision is logged.Install: `npx cordon-cli init` auto-patches your Claude Desktop config in about two minutes. Works with Claude Desktop, Claude Code, Cursor, Windsurf, and any stdio MCP client.Open source, MIT. Published to the official MCP registry as io.github.marras0914/cordon. There's also a hosted dashboard for centralized audit logs, but the gateway runs local and the CLI is fully offline.Happy to answer questions about the threat model, why I built it as a proxy vs. a client-side wrapper, or how write-detection works wit…
