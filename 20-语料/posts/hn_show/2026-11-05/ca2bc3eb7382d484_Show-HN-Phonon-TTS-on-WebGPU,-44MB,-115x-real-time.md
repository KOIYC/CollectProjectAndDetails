---
type: "corpus"
item_id: "ca2bc3eb7382d484"
title: "Show HN: Phonon TTS on WebGPU, 44MB, 115x real time, with live word timings"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50369215"
project_url: "https://github.com/blixt/phonon"
author: "blixt"
published_at: "2026-11-04T18:01:31Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_blixt
  - story_50369215
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Phonon TTS on WebGPU, 44MB, 115x real time, with live word timings

> [!info] 一句话导读
> I tried Gradium's Phonon 31M text-to-speech model and was blown away by its quality to size ratio. I needed timings for every word to be able to highlight them,…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50369215>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：blixt　|　发布：2026-11-04T18:01:31Z
> 项目链接：<https://github.com/blixt/phonon>
> 采集：2026-11-05T11:21:45+08:00　|　id：`ca2bc3eb7382d484`

## 正文

I tried Gradium's Phonon 31M text-to-speech model and was blown away by its quality to size ratio. I needed timings for every word to be able to highlight them, so I wrote a second runtime for it with a different design: the whole generation loop stays on the GPU in WebGPU kernels written specifically for this by Claude Opus 5.5.When initialized, it can start streaming audio in about 3 ms, and it only needs to download 44 MB (<40 MB brotli'd) instead of the official 67 MB, because every large matrix is stored as int8, the audio decoder included. On the same devices it runs at 115x real time vs. 31x on my M3 Max, and 26x against 13x on my iPhone 17 Pro. The timings are read from one of the model's attention heads while it speaks, so we practically get the time offsets of words for free.Demo: blixt.xyz/phononCode and benchmarks: github.com/blixt/phononGradium did an amazing job on this model, and I'm still wrapping my head around that you can get realtime human-sounding speech from a 40 MB file on a website.

## 导航

- 项目页：[[10-项目/github.com_f76f73fc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
