---
type: "project"
title: "Show HN: Digitron – a virtual analog synth and sequencer"
project_url: "https://apps.apple.com/us/app/digitron-synthesizer/id6737997923"
first_seen: "2026-09-26T09:41:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_sillydevices
  - story_49848552
  - show_hn
lang: "en"
---

# Show HN: Digitron – a virtual analog synth and sequencer

> [!info] 一句话导读
> I’ve just released Digitron on iOS.It’s a virtual analog synthesizer with a sequencer. If I had to describe the rough idea, I’d say it’s something like a child …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://apps.apple.com/us/app/digitron-synthesizer/id6737997923>
> 首次收录：2026-09-26T09:41:08+08:00
> 来源渠道：HN Show HN
> 标签：author_sillydevices, story_49848552, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-26/1e0b45ce9ab3aa5e_Show-HN-Digitron-–-a-virtual-analog-synth-and-sequ]] |

## 摘要正文

I’ve just released Digitron on iOS.It’s a virtual analog synthesizer with a sequencer. If I had to describe the rough idea, I’d say it’s something like a child of a Moog and a Pocket Operator. I started working on it about four years ago, mostly out of boredom. I was tired of building similar client-server apps that, in the end, were mostly different ways of displaying lists. I wanted to build something self-contained.The first version of Digitron was pretty simple: a 16-step sequencer and a monophonic synth with two oscillators and cross-modulation. I wrote the first audio engine in Kotlin. As long as it was rendering WAV files offline, everything sounded fine. But the first time I tried running it in real time on Android, the popcorn noises made it pretty obvious that this wasn’t going to work. So I rewrote the entire engine in C++, and along the way got much more familiar with real-time audio, DSP, optimization, and aliasing than I had originally planned. Over the next few years Digitron grew quite a bit: I added a patchbay, a more capable sequencer with patterns and parameter locks, 8 independent engines, a mixer, effects, polyphony, and a recorder, and I’ve surely forgotten so…
