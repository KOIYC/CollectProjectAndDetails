---
type: "project"
title: "Show HN: Wrapper – Best Ever Agent Manager"
project_url: "https://github.com/xatuke/wrapper"
first_seen: "2026-09-21T03:11:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_satuke
  - story_49110318
  - show_hn
lang: "en"
---

# Show HN: Wrapper – Best Ever Agent Manager

> [!info] 一句话导读
> Default branch: main

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/xatuke/wrapper>
> 首次收录：2026-09-21T03:11:17+08:00
> 来源渠道：HN Show HN
> 标签：author_satuke, story_49110318, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/b58b7df85ea95f4f_Show-HN-Wrapper-–-Best-Ever-Agent-Manager]] |
| 2026-09-21T03:11:17+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/b58b7df85ea95f4f_Show-HN-Wrapper-–-Best-Ever-Agent-Manager]] |

## 摘要正文

# xatuke/wrapper  wrap your agents  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - Default branch: main - Created: 2026-07-13T11:50:47Z  ## Languages  - Dockerfile - JavaScript - TypeScript  ## Top Contributors  - xatuke (2 contributions)  ---  ## README  # wrapper  Host, manage, and observe pi agents on Slack — each agent in its own hardened container, with Langfuse tracing (tokens, cost, tool spans), managed by one CLI.  **An agent is config + tools; everything else is a shared runtime.** Adding an agent means writing an `agent.yaml`, optionally dropping tool modules in a folder, and running `wrapper agent add` — not writing a new service.  ``` agents/support-bot/ ├── agent.yaml     # model, prompt, channels, tools, features ├── prompt.md      # system prompt ├── tools/*.ts     # custom tools (TypeBox schema + execute) ├── slack/         # slack-cli project (manifest.json, app registry) └── .env           # Slack tokens + keys (gitignored) ```  Each agent gets its own Slack app (Socket Mode — outbound only, no public ingress), a persistent volume for conversation history, and per-turn traces. Opt-in runtime features give agents self-managed cron schedules, persistent memo…
