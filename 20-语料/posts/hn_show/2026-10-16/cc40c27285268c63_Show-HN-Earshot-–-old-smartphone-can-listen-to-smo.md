---
type: "corpus"
item_id: "cc40c27285268c63"
title: "Show HN: Earshot – old smartphone can listen to smoke alarm, doorbell or dog"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50104940"
project_url: "https://tryearshot.net/index.html"
author: "hessdalenlight"
published_at: "2026-10-15T15:18:18Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_hessdalenlight
  - story_50104940
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Earshot – old smartphone can listen to smoke alarm, doorbell or dog

> [!info] 一句话导读
> TLDR: I’m building Earshot - the sound detection app that can detect (ideally) any sound described by text.The neural model under the hood is a CLAP-style model…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50104940>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：hessdalenlight　|　发布：2026-10-15T15:18:18Z
> 项目链接：<https://tryearshot.net/index.html>
> 采集：2026-10-16T09:35:18+08:00　|　id：`cc40c27285268c63`

## 正文

TLDR: I’m building Earshot - the sound detection app that can detect (ideally) any sound described by text.The neural model under the hood is a CLAP-style model (CLIP for audio): basically during the training you force the model make inner text and audio representations to match. And then you can use such model as 0-shot audio classifier. For POC I used LAION’s clap-htsat model but it turned out to be quite "heavy" so I’ve trained a smaller one by myself.As for text encoder I used model from the EfficientAT family; for audio I used jhu-clsp/ettin-encoder-32m. The training was performed on my mighty 2x1080 Ti home server. The trained weights can be found on my HF: https://huggingface.co/mirth/earshot-clap-mn10-ettin32I would appreciate it if you could test this application (especially if you could report if an app missed the sound).A couple of disclaimers:1. The sound never leaves you device.2. It can miss the sound so it’s not a replacement for your monitoring system (but an extra pair of ears).3. I’m aware that similar functionality is presented in the Apple HomePod but there is a minor difference: to add very custom sound for detection on HomePod you need first to record it (to train inner HomePod model I presume). In my case you can just describe the sound in the text format.Happy to answer any questions!

## 关联链接

- https://huggingface.co/mirth/earshot-clap-mn10-ettin32I

## 导航

- 项目页：[[10-项目/tryearshot.net_ff659e51]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
