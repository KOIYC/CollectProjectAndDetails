---
type: "corpus"
item_id: "0acbfc12e439f118"
title: "Show HN: SqlFlow – Durable Workflows Backed by PostgreSQL or SQL Server"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50031583"
project_url: "https://github.com/bytefish/SqlFlow"
author: "bytefish"
published_at: "2026-10-10T10:47:33Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_bytefish
  - story_50031583
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: SqlFlow – Durable Workflows Backed by PostgreSQL or SQL Server

> [!info] 一句话导读
> Hey HN!I have built SqlFlow, which is an open-source durable workflow engine backed by PostgreSQL or SQL Server, with SDKs for .NET, Java, Python, and Go. Workf…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50031583>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：bytefish　|　发布：2026-10-10T10:47:33Z
> 项目链接：<https://github.com/bytefish/SqlFlow>
> 采集：2026-10-11T09:43:53+08:00　|　id：`0acbfc12e439f118`

## 正文

Hey HN!I have built SqlFlow, which is an open-source durable workflow engine backed by PostgreSQL or SQL Server, with SDKs for .NET, Java, Python, and Go. Workflows support retries, checkpoints, rate limitng, scheduling, and suspension while waiting for events.It took a large deal of inspiration from Absurd, but it expands on the core concepts.Instead of polling the database, it supports native database features such as PostgreSQL LISTEN / NOTIFY, SQL Server Service Broke, and you could also use NATS. The durable state always remains in your SQL database.Each SDK comes with a complete example, that models an AI Agent Workflow:- https://github.com/bytefish/SqlFlow/tree/main/sdksI would love to hear your feedback.

## 关联链接

- https://github.com/bytefish/SqlFlow/tree/main/sdksI

## 导航

- 项目页：[[10-项目/github.com_fc4789d8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
