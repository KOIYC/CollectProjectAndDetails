---
type: "corpus"
item_id: "5aa5b74c71cf3a53"
title: "Show HN: Babytalk: Offline speech to text and text to speech on ESP32"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50026819"
project_url: "https://github.com/tlack/babytalk"
author: "tlack"
published_at: "2026-10-09T21:33:56Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_tlack
  - story_50026819
  - show_hn
metrics: {"points": 6, "comments": 4, "engagement_velocity": 6}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:3d"
---

# Show HN: Babytalk: Offline speech to text and text to speech on ESP32

> [!info] 一句话导读
> I have been playing with a lot of $20 devices with no keyboards or screens. I wanted to use speech to interact with them, but without it having to run through a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50026819>
> 指标：点赞=6 · 评论=4 · engagement_velocity=6
> 作者：tlack　|　发布：2026-10-09T21:33:56Z
> 项目链接：<https://github.com/tlack/babytalk>
> 采集：2026-10-10T09:53:50+08:00　|　id：`5aa5b74c71cf3a53`

## 正文

I have been playing with a lot of $20 devices with no keyboards or screens. I wanted to use speech to interact with them, but without it having to run through a cloud service or use a fixed command vocabulary.I worked with Claude to implement high performance 4bit int kernels for the ESP32S3 and P4 and quantize some larger STT and TTS models. Surprisingly, it's quite usable on these tiny boards.Also includes a finetuned model that can better cope with my diesel drones, hacking coughs, and mumbling. Works with Micropython (RAM scarcity issues) and AtomVM (better).

## 评论（4/4）

> **atmanactive** · 2026-10-09T21:47:13.000Z　
> I was hoping this could be a hardware STT-to-HID, but, even after looking at the Git ReadMe, I still don't understand how is the text supposed to exit the device?

---

> **tlack** · 2026-10-09T21:55:08.000Z　
> It's a library for C / Micropython / AtomVM, so you could send the result over a lora radio, ESPNOW, WAN, match it in a switch statement to activate a relay, draw on the LCD.. that's up to you.Many ESP32S3 dev boards have a microphone and speaker header available conveniently on the board, so I have been using that to respond via Babytalk's text to speech capability.I'll improve the README to make it a little more clear.

---

> **atmanactive** · 2026-10-09T22:02:06.000Z　
> Thank you for the explaination. So it is a library and would require someone to adjust it to their use case. That's what got me confused: wide open use case, but nothing tangible. I mean, if an ESP device is doing STT+TTS, then what am I supposed to be talking to? But if it is an ESP device that can do ANY->TTS and/or STT->ANY with some code customization needed, then I think I get it.

---

> **tlack** · 2026-10-09T22:15:57.000Z　
> I wrote the README from the perspective of being understandable by the lay person, and I think I left out some vital clues about this being a software building block for making your own ESP32 projects more intelligent. I pushed a README update to make it 0.1% more clear.As for what to talk to.. or the ultimate purpose lol.. you could do simple device control scenarios ("lights off"), do hands-free sensor readings ("temperature at 95 degrees"), change wifi settings via voice ("switch access points"), etc.I use it to control an agent-powered diverse device sensor network in my home and my truck. Much of the capability needs Internet access, but having on-device speech to text and text to speech means I can still do some stuff when I didn't bring the Starlink with me. On-device STT opens up a lot of low bandwidth (lora) opportunities too.

## 导航

- 项目页：[[10-项目/github.com_d2515d55]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
