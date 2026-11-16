---
type: "project"
title: "Show HN: Strata Architecture"
project_url: "https://yrashk.com/strata"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_yrashk
  - story_50510744
  - show_hn
lang: "en"
---

# Show HN: Strata Architecture

> [!info] 一句话导读
> I've long thought about how we're influenced by CPU architectures, and importantly, their ISAs.In a discussion at a meetup, I brought up a topic that interested…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://yrashk.com/strata>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_yrashk, story_50510744, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-16/ffeb8a10b3b2b7ad_Show-HN-Strata-Architecture]] |

## 摘要正文

I've long thought about how we're influenced by CPU architectures, and importantly, their ISAs.In a discussion at a meetup, I brought up a topic that interested me for a while: how would an ISA that exposes memory and cache interactions in a more explicit way (because if you think about it, memory is very much I/O), as opposed to being smart and predictive on its own?An obscure interest, of course. Nevertheless, I wanted to build a quick prototype after that.What ended up transpiring was a bit larger. A multicore architecture with tiered stores, capabilities, a JIT'd emulator, Verilog RTL with a simulator, a small microkernel OS, UI, JIT Forth, an assembler in its own assembly, a bootstrapping C99 compiler, a few games, a visual debugger, and a few other things.(This also shows just how far a directed LLM process can go in little time)
