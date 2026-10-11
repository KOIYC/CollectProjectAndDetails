---
type: "project"
title: "Show HN: SqlFlow – Durable Workflows Backed by PostgreSQL or SQL Server"
project_url: "https://github.com/bytefish/SqlFlow"
first_seen: "2026-10-11T09:43:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_bytefish
  - story_50031583
  - show_hn
lang: "en"
---

# Show HN: SqlFlow – Durable Workflows Backed by PostgreSQL or SQL Server

> [!info] 一句话导读
> Hey HN!I have built SqlFlow, which is an open-source durable workflow engine backed by PostgreSQL or SQL Server, with SDKs for .NET, Java, Python, and Go. Workf…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/bytefish/SqlFlow>
> 首次收录：2026-10-11T09:43:53+08:00
> 来源渠道：HN Show HN
> 标签：author_bytefish, story_50031583, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-11T09:43:53+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-11/0acbfc12e439f118_Show-HN-SqlFlow-–-Durable-Workflows-Backed-by-Post]] |

## 摘要正文

Hey HN!I have built SqlFlow, which is an open-source durable workflow engine backed by PostgreSQL or SQL Server, with SDKs for .NET, Java, Python, and Go. Workflows support retries, checkpoints, rate limitng, scheduling, and suspension while waiting for events.It took a large deal of inspiration from Absurd, but it expands on the core concepts.Instead of polling the database, it supports native database features such as PostgreSQL LISTEN / NOTIFY, SQL Server Service Broke, and you could also use NATS. The durable state always remains in your SQL database.Each SDK comes with a complete example, that models an AI Agent Workflow:- https://github.com/bytefish/SqlFlow/tree/main/sdksI would love to hear your feedback.
