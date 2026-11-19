---
type: "project"
title: "Show HN: Fun with bicycle trainers and web APIs"
project_url: "https://joelriley.com/fun-with-trainers"
first_seen: "2026-11-19T09:56:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_okayestjoel
  - story_50550607
  - show_hn
lang: "en"
---

# Show HN: Fun with bicycle trainers and web APIs

> [!info] 一句话导读
> a personal webpage of little consequence

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://joelriley.com/fun-with-trainers>
> 首次收录：2026-11-19T09:56:08+08:00
> 来源渠道：HN Show HN
> 标签：author_okayestjoel, story_50550607, show_hn
> 最新指标：点赞=7 · 评论=3 · engagement_velocity=7

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:43:31+08:00 | HN Show HN | 点赞=7 · 评论=3 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-11-19/75bdb33fa136fe8e_Show-HN-Fun-with-bicycle-trainers-and-web-APIs]] |
| 2026-11-19T09:56:08+08:00 | HN Show HN | 点赞=7 · 评论=3 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-11-19/75bdb33fa136fe8e_Show-HN-Fun-with-bicycle-trainers-and-web-APIs]] |

## 摘要正文

Joel Riley a personal webpage of little consequence Fun with bicycle trainers and web APIs November 18, 2026 Try the web app: YouTube Hamster Wheel I'm a casual cyclist, though on days when the weather is poor, I use my indoor bicycle smart trainer, a Wahoo Kickr Core. It works well enough when paired with an app like Zwift. Zwift lets you go on virtual rides, measuring your speed based on trainer power output. Unfortunately for a casual cyclist and an even less frequent trainer user, the Zwift $20/month subscription requirement is a steep ask. This got me thinking, could we create a simple web app that connects to the Wahoo device that gamifies the experience without the steep prices? The Wahoo Kickr Core, like many smart trainers, conforms to the Cycling Power Service Bluetooth specification. Paired with the Web Bluetooth API , you can make simple web apps to create interesting experiences with your trainer. Simplified TypeScript code to connect to a smart trainer and calculate speed and distance. const CYCLING_POWER_SERVICE = 0x1818 ;  const CYCLING_POWER_MEASUREMENT = 0x2a63 ;  const wheelCircumferenceM = 2.105 ; // 700x25c tire let prevWheelRevs : number | null = null ;  let p…
