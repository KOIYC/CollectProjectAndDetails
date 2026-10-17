---
type: "corpus"
item_id: "b2a1ab84cb8e27f4"
title: "Show HN: Tennis, a local/offline context store"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50119473"
project_url: "https://tennis.jlachance1.workers.dev/"
author: "pizzuh"
published_at: "2026-10-16T15:17:01Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_pizzuh
  - story_50119473
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Tennis, a local/offline context store

> [!info] 一句话导读
> Hi everyone! I'm Joe, and I built Tennis: a CLI that indexes and searches your context offline. You can index any files, your Chat & Claude sessions, Codex hist…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50119473>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：pizzuh　|　发布：2026-10-16T15:17:01Z
> 项目链接：<https://tennis.jlachance1.workers.dev/>
> 采集：2026-10-17T13:35:15+08:00　|　id：`b2a1ab84cb8e27f4`

## 正文

Hi everyone! I'm Joe, and I built Tennis: a CLI that indexes and searches your context offline. You can index any files, your Chat & Claude sessions, Codex history, etc. All local and offline.I've always hated having chats siloed in Claude and not having an easy way to connect that context in other apps. Anything that exists today has a subscription and is stored on their servers, and really wanted something fast, local, and offline.How Tennis works:
* SQLite/FTS5 (keyword) + vec0 (vector)
* model2vec / potion-retrieval-32M (512-dim, 123MB). This is a flat vector table, and what helps make this work well local/offline.
* RRF (k=60) fuses BM25 keyword rank + cosine semantic rank into one scoreTennis also creates markdown files called 'cards' at indexing time. This gives you an easy, summarized, human readable format to see what Tennis has. You can edit these files (but won't change the embeddings in SQLite).You can use Tennis via API and MCP.
It's incredibly fast, and the MCP works great as a connector to different applications (ChatGPT, Claude, Opencode, etc).You can install and use it today: https://tennis.jlachance1.workers.dev/Thanks for checking this out! I would love any feedback. Thank you

## 关联链接

- https://tennis.jlachance1.workers.dev/Thanks

## 导航

- 项目页：[[10-项目/tennis.jlachance1.workers.dev_f853f337]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
