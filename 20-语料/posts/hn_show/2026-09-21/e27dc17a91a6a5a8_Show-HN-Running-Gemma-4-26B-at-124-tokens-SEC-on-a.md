---
type: "corpus"
item_id: "e27dc17a91a6a5a8"
title: "Show HN: Running Gemma-4 26B at 124 tokens/SEC on a CPU, no GPU"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731643"
project_url: "https://apeg.dev/writing/running-gemma4-26b-on-a-cpu"
author: "arun-prasath"
published_at: "2026-06-30T12:17:31Z"
captured_at: "2026-09-21T01:45:02+08:00"
lang: "en"
kind: "post"
topic: 内容/媒体
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_arun-prasath
  - story_48731643
  - show_hn
metrics: {"points": 10, "comments": 1, "engagement_velocity": 10}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:113d"
---

# Show HN: Running Gemma-4 26B at 124 tokens/SEC on a CPU, no GPU

> [!info] 一句话导读
> I wanted to know how fast a 26B mixture-of-experts model could run on a desktop CPU with no GPU. Got ~40 tok/s single-stream (lossless) and ~124 batched. The su…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731643>
> 指标：点赞=10 · 评论=1 · engagement_velocity=10
> 作者：arun-prasath　|　发布：2026-06-30T12:17:31Z
> 项目链接：<https://apeg.dev/writing/running-gemma4-26b-on-a-cpu>
> 采集：2026-09-21T01:45:02+08:00　|　id：`e27dc17a91a6a5a8`

## 正文

I wanted to know how fast a 26B mixture-of-experts model could run on a desktop CPU with no GPU. Got ~40 tok/s single-stream (lossless) and ~124 batched. The surprising part was the byte budget: for this model you compress the output head (32% of per-token bytes), not the experts (16%). The writeup has the bandwidth roofline and the dead-ends; the repo has the reproducible recipe. Happy to answer questions.Repo: https://github.com/arun-prasath2005/gemma4-cpu-moe

## 评论（1/1）

> **pmb_developer** · 2026-06-30T15:26:38.000Z　
> The output head byte budget is surprising. Did you try any tradeoff where the head is compressed more aggressively but experts stay mostly untouched?

## 关联链接

- https://github.com/arun-prasath2005/gemma4-cpu-moe

## 导航

- 项目页：[[10-项目/apeg.dev_788bf1d6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`内容/媒体`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
