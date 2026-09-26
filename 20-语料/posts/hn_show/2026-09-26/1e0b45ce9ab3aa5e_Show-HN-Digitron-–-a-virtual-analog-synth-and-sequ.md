---
type: "corpus"
item_id: "1e0b45ce9ab3aa5e"
title: "Show HN: Digitron – a virtual analog synth and sequencer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49848552"
project_url: "https://apps.apple.com/us/app/digitron-synthesizer/id6737997923"
author: "sillydevices"
published_at: "2026-09-25T19:01:40Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_sillydevices
  - story_49848552
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Digitron – a virtual analog synth and sequencer

> [!info] 一句话导读
> I’ve just released Digitron on iOS.It’s a virtual analog synthesizer with a sequencer. If I had to describe the rough idea, I’d say it’s something like a child …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49848552>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：sillydevices　|　发布：2026-09-25T19:01:40Z
> 项目链接：<https://apps.apple.com/us/app/digitron-synthesizer/id6737997923>
> 采集：2026-09-26T09:41:08+08:00　|　id：`1e0b45ce9ab3aa5e`

## 正文

I’ve just released Digitron on iOS.It’s a virtual analog synthesizer with a sequencer. If I had to describe the rough idea, I’d say it’s something like a child of a Moog and a Pocket Operator.
I started working on it about four years ago, mostly out of boredom. I was tired of building similar client-server apps that, in the end, were mostly different ways of displaying lists. I wanted to build something self-contained.The first version of Digitron was pretty simple: a 16-step sequencer and a monophonic synth with two oscillators and cross-modulation.
I wrote the first audio engine in Kotlin. As long as it was rendering WAV files offline, everything sounded fine. But the first time I tried running it in real time on Android, the popcorn noises made it pretty obvious that this wasn’t going to work.
So I rewrote the entire engine in C++, and along the way got much more familiar with real-time audio, DSP, optimization, and aliasing than I had originally planned.
Over the next few years Digitron grew quite a bit: I added a patchbay, a more capable sequencer with patterns and parameter locks, 8 independent engines, a mixer, effects, polyphony, and a recorder, and I’ve surely forgotten something.The result is a fairly monstrous thing with a steep learning curve. But if you’re familiar with modular synths, it should be possible to find your way around it.
The current Digitron stack is Kotlin Multiplatform for the application layer, backed by a cross-platform C++ audio engine. On Android it talks to the native layer through JNI, while on iOS I use Swift wrappers around the same C++ backend.The work on Digitron’s audio engine also eventually led to a new open-source project called PatchCore — a redesigned, more general-purpose modular audio engine:
https://github.com/SillyDevices/PatchCoreAfter about four years of working on it, it feels pretty strange to finally see Digitron in the App Store. I'd love to hear what you think about the synth.

## 关联链接

- https://github.com/SillyDevices/PatchCoreAfter

## 导航

- 项目页：[[10-项目/apps.apple.com_09270b80]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
