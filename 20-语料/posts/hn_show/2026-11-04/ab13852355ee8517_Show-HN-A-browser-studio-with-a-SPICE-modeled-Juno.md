---
type: "corpus"
item_id: "ab13852355ee8517"
title: "Show HN: A browser studio with a SPICE-modeled Juno 106 (playing Nightcall)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50358282"
project_url: "https://browsertape.com/metro"
author: "tonioab"
published_at: "2026-11-03T21:14:36Z"
captured_at: "2026-11-04T09:51:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - hn_show
  - author_tonioab
  - story_50358282
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: A browser studio with a SPICE-modeled Juno 106 (playing Nightcall)

> [!info] 一句话导读
> I wanted the feeling of sitting down with a small "DAWless" hardware setup: a synth, some drums, a midi recorder, and knobs to turn. Something you can open for …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50358282>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：tonioab　|　发布：2026-11-03T21:14:36Z
> 项目链接：<https://browsertape.com/metro>
> 采集：2026-11-04T09:51:43+08:00　|　id：`ab13852355ee8517`

## 正文

I wanted the feeling of sitting down with a small "DAWless" hardware setup: a synth, some drums, a midi recorder, and knobs to turn. Something you can open for a quick jam, with enough care put into the sound that you’ll want to keep playing. The spirit is close to a DAWless setup, with the convenience of a browser tab.The linked demo is a recreation of Kavinsky’s Nightcall. It opens as a playable session, so you can listen, explore the instruments, and change the sounds yourself. All the audio is generated locally in your browser.I spent 80% of the dev time on Cybelle, a clone of the Juno-106, with a C++/WebAssembly sound engine. It was built with a SPICE model (model of the original circuit), which I then calibrated against my real hardware Juno. Reproducing the filter and the chorus took many iterations and blind tests, and I believe it strikes a good balance of audio fidelity and CPU performance for most laptops. To my ears, the Juno presets and filter sweeps sound the same between my hardware and Cybelle (as in, I can't differentiate them in blind tests).An interesting side-effect of using "hill-climbing" agentic loops to optimize the sound engine is that I ended up spending hours on the UI as well, trying to make it immersive and photo-realistic.I’d especially love feedback from people who make music with hardware: how does it sound, how does it feel to play, and what would make you reach for it when you have a few minutes to make music?

## 评论（1/1）

> **vunderba** · 2026-11-03T23:09:52.000Z　
> Nice job.Never used a 106, but a friend had a Juno-6 when I was growing up, and it was a blast to play with.If you're into this kinda stuff, Arturia makes an absolutely incredible set of physically modelled classic synth engines, including the Jun-6 V, which is a recreation of the Juno-6.Given that you had an actual one, did you experiment with some kind of feedback loop from the computer through your MIDI interface to the synthesizer and then back to the computer? Seems like that might let you use differential audio synthesis to automate some of the A/B testing.https://www.arturia.com/products/software-instruments/v-coll...

## 导航

- 项目页：[[10-项目/browsertape.com_cad1c31f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
