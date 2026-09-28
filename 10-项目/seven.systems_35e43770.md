---
type: "project"
title: "Show HN: Digital Audio Workstation running in a browser (stock WebAudio nodes!)"
project_url: "https://seven.systems/xequence2/demo/demo-deploy/www/index.html"
first_seen: "2026-09-28T09:47:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_intrr
  - story_49867275
  - show_hn
lang: "en"
---

# Show HN: Digital Audio Workstation running in a browser (stock WebAudio nodes!)

> [!info] 一句话导读
> Hi!This is a quite capable DAW that runs entirely in the browser (Chromium-based ones are the most tested), and, perhaps most surprisingly, it uses standard Web…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://seven.systems/xequence2/demo/demo-deploy/www/index.html>
> 首次收录：2026-09-28T09:47:28+08:00
> 来源渠道：HN Show HN
> 标签：author_intrr, story_49867275, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-28T09:47:28+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-28/3a39db4536d7ec48_Show-HN-Digital-Audio-Workstation-running-in-a-bro]] |

## 摘要正文

Hi!This is a quite capable DAW that runs entirely in the browser (Chromium-based ones are the most tested), and, perhaps most surprisingly, it uses standard WebAudio nodes exclusively (no WebAssembly or custom DSP code in AudioWorklet etc.).In the included demo project (EDM, FWIW), over a thousand nodes are active at "peak" moments, and hundreds of them created and destroyed per second - all running smoothly and without dropouts and with low CPU (~ 5%) and RAM (~ 250MB) on the cheapest laptop I could buy ;) The project uses ~ 20 modular synth instances and ~ 65 insert FX.Which, I guess, means that much of the ACTUALLY impressive work was done by the Chromium team!There's also lots of smart node caching going on to reset/reuse nodes when possible instead of destroying them. Also, all parameter changes are always scheduled (slightly) into the future (even when playing the modular synth live), so timing is extremely tight and precise.The DAW is based on Xequence 2, the iOS app.The app works on any device and mostly any screen/window size and supports touch, mouse, and keyboard interactions -- however the mixer (instruments) view is currently not great on small (phone) screens.Also, th…
