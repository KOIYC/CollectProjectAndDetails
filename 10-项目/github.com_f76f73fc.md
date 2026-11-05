---
type: "project"
title: "Show HN: Phonon TTS on WebGPU, 44MB, 115x real time, with live word timings"
project_url: "https://github.com/blixt/phonon"
first_seen: "2026-11-05T11:21:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_blixt
  - story_50369215
  - show_hn
lang: "en"
---

# Show HN: Phonon TTS on WebGPU, 44MB, 115x real time, with live word timings

> [!info] 一句话导读
> I tried Gradium's Phonon 31M text-to-speech model and was blown away by its quality to size ratio. I needed timings for every word to be able to highlight them,…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/blixt/phonon>
> 首次收录：2026-11-05T11:21:45+08:00
> 来源渠道：HN Show HN
> 标签：author_blixt, story_50369215, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:21:45+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-05/ca2bc3eb7382d484_Show-HN-Phonon-TTS-on-WebGPU,-44MB,-115x-real-time]] |

## 摘要正文

I tried Gradium's Phonon 31M text-to-speech model and was blown away by its quality to size ratio. I needed timings for every word to be able to highlight them, so I wrote a second runtime for it with a different design: the whole generation loop stays on the GPU in WebGPU kernels written specifically for this by Claude Opus 5.5.When initialized, it can start streaming audio in about 3 ms, and it only needs to download 44 MB (<40 MB brotli'd) instead of the official 67 MB, because every large matrix is stored as int8, the audio decoder included. On the same devices it runs at 115x real time vs. 31x on my M3 Max, and 26x against 13x on my iPhone 17 Pro. The timings are read from one of the model's attention heads while it speaks, so we practically get the time offsets of words for free.Demo: blixt.xyz/phononCode and benchmarks: github.com/blixt/phononGradium did an amazing job on this model, and I'm still wrapping my head around that you can get realtime human-sounding speech from a 40 MB file on a website.
