---
type: "corpus"
item_id: "ea15be7b4312302a"
title: "Show HN: WebGCM – a global climate model running in the browser on WebGPU"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49793545"
project_url: "https://gcm.echorelay.net/"
author: "jlhawn"
published_at: "2026-09-21T21:15:04Z"
captured_at: "2026-09-22T12:53:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_jlhawn
  - story_49793545
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: WebGCM – a global climate model running in the browser on WebGPU

> [!info] 一句话导读
> I started this four and a half years ago. I wanted to build a climate model as both a toy and educational tool that I could visualize in a web browser. I have a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49793545>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：jlhawn　|　发布：2026-09-21T21:15:04Z
> 项目链接：<https://gcm.echorelay.net/>
> 采集：2026-09-22T12:53:31+08:00　|　id：`ea15be7b4312302a`

## 正文

I started this four and a half years ago. I wanted to build a climate model as both a toy and educational tool that I could visualize in a web browser. I have always been interested in meteorology and asked r/ClimateScience for advice on the math and physics on building an in-browser climate model as an educational tool, and a few people said it was far too ambitious. They were right. I could build the geometry, an icosahedral hexagonal grid on a globe, and I have an intuitive understanding of the math but integrating the Navier-Stokes equations and the physics proved to be too difficult for me, and the closest I got after nearly of month of work was a model that blew up within two simulated days.Fast forward 4 and a half years. I figured that if models like Claude and GPT Astra could solve a milennium prize problem about fluid dynamics then they could help me fix the broken model and iterate on it until my vision was realized. On Friday, I threw down $200 for a Claude Max subscription, and this is the result of a single weekend's work on top of where I had left off.What it is now, in technical terms: a hydrostatic primitive-equation atmosphere on that hex grid (the TRiSK scheme MPAS uses), 27 levels, about 41,000 cells at 110 km, with grey radiation, moist convection, a boundary layer, sea ice, a land surface with snow, a two-layer ocean and real topography. Every kernel runs on the GPU; on my MacBook Pro (M1 Max) it does about 70 simulated hours a minute from a six-year spin-up, hence the 50 MB first load. You can color the globe by twenty-odd fields, animate wind or currents, draw isobars, or view it from space under the model's own sun. The URL captures the view, so links open specific places.Caveats: an educational model, not a validated one. It runs about four degrees colder than Earth and I'm still tuning it, the ocean is crude and shallow, and it needs WebGPU (Chrome, Edge, Safari 26) for best performance. It's currently tuned for my specific machine specs but I suspect it will run well on most desktop-class Apple Silicon machines from the past 5 years.Source and design notes: https://github.com/jlhawn/geodesicEdit: If it runs really well on your machine, something well above 100 simulated hours per minute (displayed on the top-left of the page), let me know your machine specs! You should also try to reload the page with `?N=128` in the query params and it will re-grid to an even higher resolution. But it will take a few simulated days to settle down after the initial shock from the changed resolution. If you end up tyring this, check out the Temperature overlay at 10 hPa height and you should see Gravity Waves [1] rippling through the top of the atmosphere![1] https://en.wikipedia.org/wiki/Gravity_wave

## 关联链接

- https://en.wikipedia.org/wiki/Gravity_wave
- https://github.com/jlhawn/geodesicEdit:

## 导航

- 项目页：[[10-项目/gcm.echorelay.net_20301031]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
