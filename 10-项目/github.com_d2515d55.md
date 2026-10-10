---
type: "project"
title: "Show HN: Babytalk: Offline speech to text and text to speech on ESP32"
project_url: "https://github.com/tlack/babytalk"
first_seen: "2026-10-10T09:53:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tlack
  - story_50026819
  - show_hn
lang: "en"
---

# Show HN: Babytalk: Offline speech to text and text to speech on ESP32

> [!info] 一句话导读
> I have been playing with a lot of $20 devices with no keyboards or screens. I wanted to use speech to interact with them, but without it having to run through a…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tlack/babytalk>
> 首次收录：2026-10-10T09:53:50+08:00
> 来源渠道：HN Show HN
> 标签：author_tlack, story_50026819, show_hn
> 最新指标：点赞=6 · 评论=4 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-10T09:53:50+08:00 | HN Show HN | 点赞=6 · 评论=4 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-10-10/5aa5b74c71cf3a53_Show-HN-Babytalk-Offline-speech-to-text-and-text-t]] |

## 摘要正文

I have been playing with a lot of $20 devices with no keyboards or screens. I wanted to use speech to interact with them, but without it having to run through a cloud service or use a fixed command vocabulary.I worked with Claude to implement high performance 4bit int kernels for the ESP32S3 and P4 and quantize some larger STT and TTS models. Surprisingly, it's quite usable on these tiny boards.Also includes a finetuned model that can better cope with my diesel drones, hacking coughs, and mumbling. Works with Micropython (RAM scarcity issues) and AtomVM (better).
