---
type: "corpus"
item_id: "1d0c1615a4f38e37"
title: "Show HN: Jacq, a DSL that compiles model and kernel descriptions to CUDA"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50406532"
project_url: "https://github.com/ImpossibleComputing/jacq"
author: "keithba"
published_at: "2026-11-07T17:58:49Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_keithba
  - story_50406532
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jacq, a DSL that compiles model and kernel descriptions to CUDA

> [!info] 一句话导读
> I was working (with agents) on testing out various attention algorithm ideas I had, and I found that the existing infrastructure/libraries made it more difficul…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50406532>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：keithba　|　发布：2026-11-07T17:58:49Z
> 项目链接：<https://github.com/ImpossibleComputing/jacq>
> 采集：2026-11-08T12:50:31+08:00　|　id：`1d0c1615a4f38e37`

## 正文

I was working (with agents) on testing out various attention algorithm ideas I had, and I found that the existing infrastructure/libraries made it more difficult than it should be.So I created Jacq, a DSL and compiler. A jacq file describes a model’s configuration, weights, layers, and pipeline. Jacq turns it into a standalone CUDA inference runtime and a Python weight exporter. Kernel descriptions can also generate CUDA harnesses.The easiest way to try it is the TinyLlama example in the README. Building, validating, visualizing, and generating CUDA only require Rust. Of course, running inference does require an NVIDIA GPU, CUDA, Python dependencies, and weights. Jacq doesn't support other GPU vendors (AMD, etc) or Metal, yet (PR's welcome!)There's also an experimental vLLM patch to compile and patch your jacq file into a vLLM build, as well.Feedback very welcome!

## 评论（1/1）

> **keithba** · 2026-11-07T23:51:53.000Z　
> @fiveapi_dev (not sure why you are flagged/dead, your question seems totally fine)...my main motivation was shortening the experiment loop. I wanted the DSL to be the thing my agent or myself edited, then regenerate the CUDA and throw the generated code away.Jacq also handles some of the repetitive setup stuff: tensor allocation, seeded inputs, launch wiring, timing, and all the output dumps for generating comparisons and what not.Triton is a much broader framework that can do a lot more, frankly. Jacq is pretty narrow at this time. But, by being narrow, it makes the experiment cycle really fast.

## 导航

- 项目页：[[10-项目/github.com_efacc81b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
