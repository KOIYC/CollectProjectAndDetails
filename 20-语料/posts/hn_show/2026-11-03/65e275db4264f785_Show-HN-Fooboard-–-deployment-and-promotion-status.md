---
type: "corpus"
item_id: "65e275db4264f785"
title: "Show HN: Fooboard – deployment and promotion status of each repo per environment"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50339634"
project_url: "https://fooboard.dev/demo"
author: "karmaniverous"
published_at: "2026-11-02T16:48:35Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_karmaniverous
  - story_50339634
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fooboard – deployment and promotion status of each repo per environment

> [!info] 一句话导读
> Welcome to DevOps hell. Here's your map.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50339634>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：karmaniverous　|　发布：2026-11-02T16:48:35Z
> 项目链接：<https://fooboard.dev/demo>
> 采集：2026-11-03T09:40:36+08:00　|　id：`65e275db4264f785`

## 正文

fooboard
Welcome to DevOps hell. Here's your map.
fooboard: a deployment status board. To set up a board with an AI
 assistant, read
 https://www.fooboard.dev/ai .

## 评论（2/2）

> **tortela** · 2026-11-02T17:14:36.000Z　
> That's cool! I've thought about doing this with organization webhooks. I assume your code is pulling on a timer or something similar?

---

> **karmaniverous** · 2026-11-02T17:18:24.000Z　
> Yah the Zapier thing used webhooks from GHA and events from Amplify but it was a pain to integrate & maintain. Fooboard polls the GHA & Amplify logs and pattern matches, so you can create whatever statuses the logs will support and no need to touch your workflows.So yes polling but it's pretty smart about timing so it's responsive without burning your request quota.

## 关联链接

- https://www.fooboard.dev/ai

## 导航

- 项目页：[[10-项目/fooboard.dev_ccd2ab68]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
