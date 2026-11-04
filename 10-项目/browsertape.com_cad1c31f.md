---
type: "project"
title: "Show HN: A browser studio with a SPICE-modeled Juno 106 (playing Nightcall)"
project_url: "https://browsertape.com/metro"
first_seen: "2026-11-04T09:51:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tonioab
  - story_50358282
  - show_hn
lang: "en"
---

# Show HN: A browser studio with a SPICE-modeled Juno 106 (playing Nightcall)

> [!info] 一句话导读
> I wanted the feeling of sitting down with a small "DAWless" hardware setup: a synth, some drums, a midi recorder, and knobs to turn. Something you can open for …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://browsertape.com/metro>
> 首次收录：2026-11-04T09:51:43+08:00
> 来源渠道：HN Show HN
> 标签：author_tonioab, story_50358282, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-04T09:51:43+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-04/ab13852355ee8517_Show-HN-A-browser-studio-with-a-SPICE-modeled-Juno]] |

## 摘要正文

I wanted the feeling of sitting down with a small "DAWless" hardware setup: a synth, some drums, a midi recorder, and knobs to turn. Something you can open for a quick jam, with enough care put into the sound that you’ll want to keep playing. The spirit is close to a DAWless setup, with the convenience of a browser tab.The linked demo is a recreation of Kavinsky’s Nightcall. It opens as a playable session, so you can listen, explore the instruments, and change the sounds yourself. All the audio is generated locally in your browser.I spent 80% of the dev time on Cybelle, a clone of the Juno-106, with a C++/WebAssembly sound engine. It was built with a SPICE model (model of the original circuit), which I then calibrated against my real hardware Juno. Reproducing the filter and the chorus took many iterations and blind tests, and I believe it strikes a good balance of audio fidelity and CPU performance for most laptops. To my ears, the Juno presets and filter sweeps sound the same between my hardware and Cybelle (as in, I can't differentiate them in blind tests).An interesting side-effect of using "hill-climbing" agentic loops to optimize the sound engine is that I ended up spending h…
