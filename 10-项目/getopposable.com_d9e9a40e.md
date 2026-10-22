---
type: "project"
title: "Show HN: Computer use on the phone itself: a 2B model that operates Android apps"
project_url: "https://getopposable.com/blog/computer-use-on-the-phone"
first_seen: "2026-10-22T09:46:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_erikkannike
  - story_50180190
  - show_hn
lang: "en"
---

# Show HN: Computer use on the phone itself: a 2B model that operates Android apps

> [!info] 一句话导读
> Skip to content Reval Labs Get started Pricing How it works Recorded runs FAQ Blog Investors Menu Get started Pricing How it works Recorded runs FAQ Blog Invest…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://getopposable.com/blog/computer-use-on-the-phone>
> 首次收录：2026-10-22T09:46:18+08:00
> 来源渠道：HN Show HN
> 标签：author_erikkannike, story_50180190, show_hn
> 最新指标：点赞=12 · 评论=2 · engagement_velocity=12

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:46:18+08:00 | HN Show HN | 点赞=12 · 评论=2 · engagement_velocity=12 | [[20-语料/posts/hn_show/2026-10-22/38d2635e72f0ec13_Show-HN-Computer-use-on-the-phone-itself-a-2B-mode]] |

## 摘要正文

Skip to content Reval Labs Get started Pricing How it works Recorded runs FAQ Blog Investors Menu Get started Pricing How it works Recorded runs FAQ Blog Investors Mac app Account Account Get the app Contents  TL;DR  Model and runtime  Step time on CPU  Vision encoder on the NPU  Accuracy on held-out tasks  Limitations  Trying it  Blog · 21 October 2026 · 4 min read  Computer use on the phone itself: a 2B model that operates Android apps  Erik  Opposable is an Android app that reads the screen through the accessibility service and taps and types in any other app. Claude, ChatGPT or Codex can drive it from a computer, and when none of them is connected, a 2-billion-parameter screen model runs the same loop on the phone with no server involved.  The on-device agent opening Clock and switching to the stopwatch, with no model outside the phone. Android emulator, real time, each step's timing on the right. # TL;DR  The model is GUI-Owl 1.5 2B in 4 bits on llama.cpp. On a Mac M2 CPU with 4 threads one step takes 7.3 s, down from 10.6 s, at the same accuracy on our 36-screen test set. Half of that step is the vision encoder, and on a Galaxy S25's NPU the encoder runs in 236 ms against 3.9…
