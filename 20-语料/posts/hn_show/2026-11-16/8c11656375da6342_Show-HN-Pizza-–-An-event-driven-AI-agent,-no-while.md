---
type: "corpus"
item_id: "8c11656375da6342"
title: "Show HN: Pizza – An event-driven AI agent, no while true"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50507971"
project_url: "https://pizza.hertzbeat.com/"
author: "tomsun28"
published_at: "2026-11-15T16:04:32Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_tomsun28
  - story_50507971
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pizza – An event-driven AI agent, no while true

> [!info] 一句话导读
> Hi HN, I made Pizza, an open-source, event-driven AI agent. No `while true`.Each turn is a state machine. Conversations and tool calls go into an immutable SQLi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50507971>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：tomsun28　|　发布：2026-11-15T16:04:32Z
> 项目链接：<https://pizza.hertzbeat.com/>
> 采集：2026-11-16T10:00:05+08:00　|　id：`8c11656375da6342`

## 正文

Hi HN, I made Pizza, an open-source, event-driven AI agent. No `while true`.Each turn is a state machine. Conversations and tool calls go into an immutable SQLite log. The UI, model context, and session tree are built from that log.The model gets one tool: a CLI. Reading files, editing code, and running commands all go through it.You can keep a conversation going without manually starting new sessions. Pizza compacts context as needed, and you can branch from any earlier message.Agents in separate workspaces talk through `tell`, each doing the work in its own project. An SSH host can be a workspace too: Pizza deploys itself there and runs remotely.Desktop and terminal interfaces are included. Bring your own model.https://github.com/pizza-agent/pizza

## 评论（1/1）

> **tomsun28** · 2026-11-15T16:17:40.000Z　
> No ReAct while true turn.

## 关联链接

- https://github.com/pizza-agent/pizza

## 导航

- 项目页：[[10-项目/pizza.hertzbeat.com_5d0527e6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
