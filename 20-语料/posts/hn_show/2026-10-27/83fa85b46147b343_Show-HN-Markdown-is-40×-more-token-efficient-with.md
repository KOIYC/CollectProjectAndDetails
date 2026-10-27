---
type: "corpus"
item_id: "83fa85b46147b343"
title: "Show HN: Markdown is 40× more token-efficient with SQLite"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50258875"
project_url: "https://withnative.ai/research-and-posts/markdown-context-benchmark"
author: "richardcrng"
published_at: "2026-10-27T13:23:49Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_richardcrng
  - story_50258875
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Markdown is 40× more token-efficient with SQLite

> [!info] 一句话导读
> Hi HN, I'm Richard, founder of Native. I'm working on open-source context ownership, to stop AI centralisation: https://github.com/withnative/nativeMy first foc…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50258875>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：richardcrng　|　发布：2026-10-27T13:23:49Z
> 项目链接：<https://withnative.ai/research-and-posts/markdown-context-benchmark>
> 采集：2026-10-27T23:46:32+08:00　|　id：`83fa85b46147b343`

## 正文

Hi HN, I'm Richard, founder of Native. I'm working on open-source context ownership, to stop AI centralisation: https://github.com/withnative/nativeMy first focus has been making Markdown vaults powerful enough so that teams can self-host all of their context (messaging, docs and projects), without it being externally fragmented or rate-limited.I'm sharing some early results: Markdown vaults can be 40× more efficient with SQLite!https://www.withnative.ai/research-and-posts/markdown-contex...Here's some of the main ideas:- SQLite or Markdown folders, you pick. You can project the same authoritative event log into either form; more projection formats will follow (e.g. maybe neo4j; we do use a graph structure).- Empirically: SQLite is better for agents! On a 120 trial evaluation for 11,000 records, agents use 40× fewer tokens with SQLite vs Markdown, per correct answer.- Everything is a file or SQLite row. Messages, documents and projects: all can be modelled in your vault. You get local-first collaboration with teammates, synced to a cloud of your choice.- You can render your vault with arbitrary UI. Your WhatsApp-like UI speaks to your teammate's Slack-like UI; both are just views over the same database.A few things I've learned building this:- Agents do pretty well even without SQL if you give them strongly typed Markdown frontmatter. This was one arm of the trial I ran. I didn't have any clear expectations, but it was cool to watch: agents ended up writing Python scripts to do SQL-like queries.- Cumulatively, cached input tokens can get expensive. I feel silly in hindsight here. I'd gotten used to letting my sessions run long, "It's all cached so it's very cheap". But when I looked at my results here, over 2/3 of the token bill on long sessions was cached input...- "Markdown vaults don't scale as well as databases" isn't as self-evident as I think. This is why I decided to benchmark it... I've had some very blank stares when I try to explain how Markdown files might break at true agent-scale volume.Unfortunately, the dataset is private, because it's two months of my own work. I am considering open-sourcing it even so, but there is definitely some embarrassing stuff in there. TBD... I know that independent result verification matters!The core engine that I evaluated is open-source, with more to be released soon: https://github.com/withnative/nativeIf you're interested in trying connected context on an open engine, you can get updates from our website or email me directly: richard@withnative.aihttps://www.withnative.ai/

## 关联链接

- https://github.com/withnative/nativeIf
- https://github.com/withnative/nativeMy
- https://www.withnative.ai/
- https://www.withnative.ai/research-and-posts/markdown-contex...Here

## 导航

- 项目页：[[10-项目/withnative.ai_5ee8b7ac]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
