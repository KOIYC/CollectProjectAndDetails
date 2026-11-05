---
type: "corpus"
item_id: "07c5997f2960121c"
title: "Show HN: Renor – one memory for all your AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50368495"
project_url: "https://github.com/renorai/renor-engine"
author: "patrickpassosbb"
published_at: "2026-11-04T17:06:10Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_patrickpassosbb
  - story_50368495
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Renor – one memory for all your AI agents

> [!info] 一句话导读
> Hey guys, I built Renor, one memory for all your agents, we got good results in benchmarks using less tokens.I built this because I was annoyed that my agents k…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50368495>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：patrickpassosbb　|　发布：2026-11-04T17:06:10Z
> 项目链接：<https://github.com/renorai/renor-engine>
> 采集：2026-11-05T11:21:45+08:00　|　id：`07c5997f2960121c`

## 正文

Hey guys, I built Renor, one memory for all your agents, we got good results in benchmarks using less tokens.I built this because I was annoyed that my agents kept forgetting what I said and my existing solutions weren't good enough.It works by using a ledger of markdown that you can export.

## 评论（2/2）

> **dave8172** · 2026-11-04T17:32:06.000Z　
> i dont understand how this helps? i can have a folder with all md files, tell any agent "refer this folder for past context, learnings, and update/ improve this as we work, this is your memory". you are holding a sqlite for index search, but maintaining as the memory grows would be the hard part. Some sort of pruning/ dreaming is required always, beyond certain time.

---

> **patrickpassosbb** · 2026-11-04T17:59:03.000Z　
> At small size folder .md works well, we measured it. The difference is when the memory grows and you have multiple agents, the agent gets 5k relevant tokens instead of reading everything (98.4% vs 60% on LongMemEval) the memory works in most agents, and corrections replace old facts while keeping history. You're right about pruning, we have a feature like dreaming that works on that.

## 导航

- 项目页：[[10-项目/github.com_dc3b1cda]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
