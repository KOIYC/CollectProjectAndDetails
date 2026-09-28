---
type: "corpus"
item_id: "3a39db4536d7ec48"
title: "Show HN: Digital Audio Workstation running in a browser (stock WebAudio nodes!)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49867275"
project_url: "https://seven.systems/xequence2/demo/demo-deploy/www/index.html"
author: "intrr"
published_at: "2026-09-27T15:06:44Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_intrr
  - story_49867275
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Digital Audio Workstation running in a browser (stock WebAudio nodes!)

> [!info] 一句话导读
> Hi!This is a quite capable DAW that runs entirely in the browser (Chromium-based ones are the most tested), and, perhaps most surprisingly, it uses standard Web…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49867275>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：intrr　|　发布：2026-09-27T15:06:44Z
> 项目链接：<https://seven.systems/xequence2/demo/demo-deploy/www/index.html>
> 采集：2026-09-28T09:47:28+08:00　|　id：`3a39db4536d7ec48`

## 正文

Hi!This is a quite capable DAW that runs entirely in the browser (Chromium-based ones are the most tested), and, perhaps most surprisingly, it uses standard WebAudio nodes exclusively (no WebAssembly or custom DSP code in AudioWorklet etc.).In the included demo project (EDM, FWIW), over a thousand nodes are active at "peak" moments, and hundreds of them created and destroyed per second - all running smoothly and without dropouts and with low CPU (~ 5%) and RAM (~ 250MB) on the cheapest laptop I could buy ;) The project uses ~ 20 modular synth instances and ~ 65 insert FX.Which, I guess, means that much of the ACTUALLY impressive work was done by the Chromium team!There's also lots of smart node caching going on to reset/reuse nodes when possible instead of destroying them. Also, all parameter changes are always scheduled (slightly) into the future (even when playing the modular synth live), so timing is extremely tight and precise.The DAW is based on Xequence 2, the iOS app.The app works on any device and mostly any screen/window size and supports touch, mouse, and keyboard interactions -- however the mixer (instruments) view is currently not great on small (phone) screens.Also, there are no "proper" audio tracks yet (although the modular synth has various Sample* modules that can track long notes, so this mitigates it), and no WebMIDI (the app is based entirely on MIDI in every way, but currently, only a MIDI adapter for the iOS app exists.)Full disclosure: The code in the demo is currently obfuscated, and I'm running a campaign to open-source it under AGPLv3.Please let me know if you have any questions or observations, or if you at least had fun! :)

## 导航

- 项目页：[[10-项目/seven.systems_35e43770]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
