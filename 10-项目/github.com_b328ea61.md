---
type: "project"
title: "Show HN: Omnara – Open-Source Alternative to Claude Managed Agents"
project_url: "https://github.com/omnara-ai/omnara"
first_seen: "2026-10-22T09:46:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_kmansm27
  - story_50183892
  - show_hn
lang: "en"
---

# Show HN: Omnara – Open-Source Alternative to Claude Managed Agents

> [!info] 一句话导读
> Hey y'all, Kartik from Omnara (https://omnara.com) here. We're building an open-source API for running durable agents. You create an agent with an API call, and…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/omnara-ai/omnara>
> 首次收录：2026-10-22T09:46:18+08:00
> 来源渠道：HN Show HN
> 标签：author_kmansm27, story_50183892, show_hn
> 最新指标：点赞=21 · 评论=8 · engagement_velocity=21

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:46:18+08:00 | HN Show HN | 点赞=21 · 评论=8 · engagement_velocity=21 | [[20-语料/posts/hn_show/2026-10-22/f38ea4d93301c015_Show-HN-Omnara-–-Open-Source-Alternative-to-Claude]] |

## 摘要正文

Hey y'all, Kartik from Omnara (https://omnara.com) here. We're building an open-source API for running durable agents. You create an agent with an API call, and Omnara runs the agent loop, gives the agent sandboxes to run commands in, and handles secrets, permissions, and RBAC. Each agent's state is stored in Postgres, so agents survive restarts and cost nothing while idle. You can message them and stream their events over the API.You may remember us from our early days, when we made a remote-control phone app for Claude Code and Codex. Since the harness ran on a laptop back then, we had to build a relay to reach it, it stopped when the laptop closed, and moving it to a cloud sandbox meant syncing code and agent state between machines. We didn't think remote-controlling a local agent was end-game for how people would run agents, so we built a new product where the agent runs in the cloud, any client can talk to it through an API, and it can still use your laptop as one of its machines.Anthropic and OpenAI are building hosted versions of this, like Claude Managed Agents and the OpenAI Agents API. Omnara is an open-source version you can run on your own servers and use your own model…
