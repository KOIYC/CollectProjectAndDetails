---
type: "corpus"
item_id: "d3a917afc1739f2a"
title: "Show HN: Omni – Open-source workplace agent, built on Postgres"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49715402"
project_url: "https://docs.getomni.co/"
author: "prvnsmpth"
published_at: "2026-09-15T16:58:14Z"
captured_at: "2026-09-20T09:41:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_prvnsmpth
  - story_49715402
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Omni – Open-source workplace agent, built on Postgres

> [!info] 一句话导读
> Show HN: Omni – Open-source workplace agent, built on Postgres

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49715402>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：prvnsmpth　|　发布：2026-09-15T16:58:14Z
> 项目链接：<https://docs.getomni.co/>
> 采集：2026-09-20T09:41:45+08:00　|　id：`d3a917afc1739f2a`

## 正文

Show HN: Omni – Open-source workplace agent, built on Postgres | Hacker News

Show HN: Omni – Open-source workplace agent, built on Postgres

2 points by prvnsmpth 29 minutes ago | hide | past | favorite | discuss

Hi HN!

Over the past year, I've been building Omni (https://github.com/getomnico/omni) - an open-source, self-hosted agent that connects to your workplace apps (drive, email, wiki, CRMs, ticketing systems, etc.), and gives your team an AI agent that can operate across these apps.

I posted about Omni on HN about 6 months ago, and it generated some interesting discussions: https://news.ycombinator.com/item?id=47215427. At the time, Omni was largely an enterprise search system. Since then, the project has evolved to become more of an agent that can gather context, analyze information, and carry out tasks; rather than just search for answers.

E.g., you can tell Omni, "create a project status deck on Google Slides with this week's progress", and it will search through Jira, Slack, Docs, meeting transcripts, fetch the relevant information, analyze spreadsheets with Python, prepare a summary and ask for your approval before creating the slides on your drive.

A non-exhaustive list of things Omni can do today:

- Take action on connected apps, with an approval system for write actions

- Full MCP support, so connectors can integrate with any existing MCP servers.

- Sync data from connected apps into a unified search index, allowing the agent to query data across all apps using a single search tool.

- Sand-boxed code execution and shell access, enabling the agent to create documents, spreadsheets, presentations and HTML landing pages.

- Persistent memory and user-defined skills

Omni still uses Postgres as its core data layer where it syncs and indexes all data from connected apps. We use ParadeDB (Postgres extension) for BM25 search and pgvector for semantic search - so there's no need to run and operate a dedicated search cluster or vector database. To know more about the architecture: https://docs.getomni.co/architecture.

Would love to get more folks involved in the project, so if you find this interesting, please check out the repo below. It only takes around 10-15 min to deploy using docker compose and connect a few apps.

Happy to answer any questions!

GitHub: https://github.com/getomnico/omni (Apache 2.0 licensed)

Docs: https://docs.getomni.co

## 关联链接

- https://docs.getomni.co
- https://docs.getomni.co/architecture.
- https://github.com/getomnico/omni
- https://news.ycombinator.com/item?id=47215427.

## 导航

- 项目页：[[10-项目/docs.getomni.co_78c3c615]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
