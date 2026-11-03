---
type: "corpus"
item_id: "d2fa9bb5f1962352"
title: "Show HN: A 14M-param world model of 2D Minecraft you can play on your phone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50341631"
project_url: "https://maharishiva.github.io/tinywmcraft"
author: "maharishiva"
published_at: "2026-11-02T18:48:59Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "移动 App"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_maharishiva
  - story_50341631
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: A 14M-param world model of 2D Minecraft you can play on your phone

> [!info] 一句话导读
> I trained a tiny 14M-parameter world model of 2D Minecraft in <10 minutes on 1xA100 (~10 cents on google colab). It runs locally in your browser, so you can pla…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50341631>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：maharishiva　|　发布：2026-11-02T18:48:59Z
> 项目链接：<https://maharishiva.github.io/tinywmcraft>
> 采集：2026-11-03T09:40:36+08:00　|　id：`d2fa9bb5f1962352`

## 正文

I trained a tiny 14M-parameter world model of 2D Minecraft in <10 minutes on 1xA100 (~10 cents on google colab). It runs locally in your browser, so you can play on your phone. It requires WebGPU: Chrome, Edge, or Safari on iOS 26 (built a custom runtime to save memory).There's also a benchmark to score your own models: beat 0.562 and the site switches to your model. Memory is the open problem: walk 10 tiles away from your table and back, and it's gone.

## 评论（2/2）

> **leksfromflowrl** · 2026-11-02T19:32:54.000Z　
> pretty sweet looks stable enough even tho obv its not perfectly persistent

---

> **maharishiva** · 2026-11-02T20:03:31.000Z　
> thanks! honestly most of that stability is from the data and tokenizer, not the dynamics model itself. the hardest part was to build a diverse enough but small dataset, that would contain round trips to teach memory and mix non trivial and random behavior on all stages of crafting tree, like, the world model isn't afraid of lava yet :)

## 导航

- 项目页：[[10-项目/maharishiva.github.io_d62a33a8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`移动 App`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
