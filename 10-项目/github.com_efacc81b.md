---
type: "project"
title: "Show HN: Jacq, a DSL that compiles model and kernel descriptions to CUDA"
project_url: "https://github.com/ImpossibleComputing/jacq"
first_seen: "2026-11-08T12:50:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_keithba
  - story_50406532
  - show_hn
lang: "en"
---

# Show HN: Jacq, a DSL that compiles model and kernel descriptions to CUDA

> [!info] 一句话导读
> I was working (with agents) on testing out various attention algorithm ideas I had, and I found that the existing infrastructure/libraries made it more difficul…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ImpossibleComputing/jacq>
> 首次收录：2026-11-08T12:50:31+08:00
> 来源渠道：HN Show HN
> 标签：author_keithba, story_50406532, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-08T12:50:31+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-08/1d0c1615a4f38e37_Show-HN-Jacq,-a-DSL-that-compiles-model-and-kernel]] |

## 摘要正文

I was working (with agents) on testing out various attention algorithm ideas I had, and I found that the existing infrastructure/libraries made it more difficult than it should be.So I created Jacq, a DSL and compiler. A jacq file describes a model’s configuration, weights, layers, and pipeline. Jacq turns it into a standalone CUDA inference runtime and a Python weight exporter. Kernel descriptions can also generate CUDA harnesses.The easiest way to try it is the TinyLlama example in the README. Building, validating, visualizing, and generating CUDA only require Rust. Of course, running inference does require an NVIDIA GPU, CUDA, Python dependencies, and weights. Jacq doesn't support other GPU vendors (AMD, etc) or Metal, yet (PR's welcome!)There's also an experimental vLLM patch to compile and patch your jacq file into a vLLM build, as well.Feedback very welcome!
