---
type: "project"
title: "Show HN: Pizza – An event-driven AI agent, no while true"
project_url: "https://pizza.hertzbeat.com/"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tomsun28
  - story_50507971
  - show_hn
lang: "en"
---

# Show HN: Pizza – An event-driven AI agent, no while true

> [!info] 一句话导读
> Hi HN, I made Pizza, an open-source, event-driven AI agent. No `while true`.Each turn is a state machine. Conversations and tool calls go into an immutable SQLi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://pizza.hertzbeat.com/>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_tomsun28, story_50507971, show_hn
> 最新指标：点赞=5 · 评论=1 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-11-16/8c11656375da6342_Show-HN-Pizza-–-An-event-driven-AI-agent,-no-while]] |

## 摘要正文

Hi HN, I made Pizza, an open-source, event-driven AI agent. No `while true`.Each turn is a state machine. Conversations and tool calls go into an immutable SQLite log. The UI, model context, and session tree are built from that log.The model gets one tool: a CLI. Reading files, editing code, and running commands all go through it.You can keep a conversation going without manually starting new sessions. Pizza compacts context as needed, and you can branch from any earlier message.Agents in separate workspaces talk through `tell`, each doing the work in its own project. An SSH host can be a workspace too: Pizza deploys itself there and runs remotely.Desktop and terminal interfaces are included. Bring your own model.https://github.com/pizza-agent/pizza
