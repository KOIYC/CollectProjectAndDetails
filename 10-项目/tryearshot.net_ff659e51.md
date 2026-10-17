---
type: "project"
title: "Show HN: Earshot – old smartphone can listen to smoke alarm, doorbell or dog"
project_url: "https://tryearshot.net/index.html"
first_seen: "2026-10-16T09:35:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hessdalenlight
  - story_50104940
  - show_hn
lang: "en"
---

# Show HN: Earshot – old smartphone can listen to smoke alarm, doorbell or dog

> [!info] 一句话导读
> TLDR: I’m building Earshot - the sound detection app that can detect (ideally) any sound described by text.The neural model under the hood is a CLAP-style model…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://tryearshot.net/index.html>
> 首次收录：2026-10-16T09:35:18+08:00
> 来源渠道：HN Show HN
> 标签：author_hessdalenlight, story_50104940, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-16/cc40c27285268c63_Show-HN-Earshot-–-old-smartphone-can-listen-to-smo]] |

## 摘要正文

TLDR: I’m building Earshot - the sound detection app that can detect (ideally) any sound described by text.The neural model under the hood is a CLAP-style model (CLIP for audio): basically during the training you force the model make inner text and audio representations to match. And then you can use such model as 0-shot audio classifier. For POC I used LAION’s clap-htsat model but it turned out to be quite "heavy" so I’ve trained a smaller one by myself.As for text encoder I used model from the EfficientAT family; for audio I used jhu-clsp/ettin-encoder-32m. The training was performed on my mighty 2x1080 Ti home server. The trained weights can be found on my HF: https://huggingface.co/mirth/earshot-clap-mn10-ettin32I would appreciate it if you could test this application (especially if you could report if an app missed the sound).A couple of disclaimers:1. The sound never leaves you device.2. It can miss the sound so it’s not a replacement for your monitoring system (but an extra pair of ears).3. I’m aware that similar functionality is presented in the Apple HomePod but there is a minor difference: to add very custom sound for detection on HomePod you need first to record it (to t…
