---
type: "corpus"
item_id: "ffeb8a10b3b2b7ad"
title: "Show HN: Strata Architecture"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50510744"
project_url: "https://yrashk.com/strata"
author: "yrashk"
published_at: "2026-11-15T21:04:54Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_yrashk
  - story_50510744
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Strata Architecture

> [!info] 一句话导读
> I've long thought about how we're influenced by CPU architectures, and importantly, their ISAs.In a discussion at a meetup, I brought up a topic that interested…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50510744>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：yrashk　|　发布：2026-11-15T21:04:54Z
> 项目链接：<https://yrashk.com/strata>
> 采集：2026-11-16T10:00:05+08:00　|　id：`ffeb8a10b3b2b7ad`

## 正文

I've long thought about how we're influenced by CPU architectures, and importantly, their ISAs.In a discussion at a meetup, I brought up a topic that interested me for a while: how would an ISA that exposes memory and cache interactions in a more explicit way (because if you think about it, memory is very much I/O), as opposed to being smart and predictive on its own?An obscure interest, of course. Nevertheless, I wanted to build a quick prototype after that.What ended up transpiring was a bit larger. A multicore architecture with tiered stores, capabilities, a JIT'd emulator, Verilog RTL with a simulator, a small microkernel OS, UI, JIT Forth, an assembler in its own assembly, a bootstrapping C99 compiler, a few games, a visual debugger, and a few other things.(This also shows just how far a directed LLM process can go in little time)

## 导航

- 项目页：[[10-项目/yrashk.com_89eeb722]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
