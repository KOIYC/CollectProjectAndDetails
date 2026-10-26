---
type: "project"
title: "Show HN: Benchmarking DSpark speculative decoding on a consumer GPU"
project_url: "https://github.com/juraj-jumic/dspark-local-bench"
first_seen: "2026-10-26T09:42:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Termich
  - story_50233709
  - show_hn
lang: "en"
---

# Show HN: Benchmarking DSpark speculative decoding on a consumer GPU

> [!info] 一句话导读
> juraj-jumic/dspark-local-bench

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/juraj-jumic/dspark-local-bench>
> 首次收录：2026-10-26T09:42:36+08:00
> 来源渠道：HN Show HN
> 标签：author_Termich, story_50233709, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:42:36+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-26/c54774d43b9bb969_Show-HN-Benchmarking-DSpark-speculative-decoding-o]] |

## 摘要正文

# juraj-jumic/dspark-local-bench  Does DSpark speculative decoding help on your GPU, for one user? Reproducible batch-size-1 benchmarks for llama.cpp on consumer GPUs.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-24T20:46:34Z  ## Languages  - PowerShell - Python - Shell  ## Topics  - amd-gpu - benchmark - dspark - llama-cpp - llm-inference - local-llm - rocm - speculative-decoding - vulkan  ## Top Contributors  - juraj-jumic (5 contributions)  ---  ## README   Does DSpark speculative decoding make your local LLM faster?  Reproducible single-user benchmarks for llama.cpp on consumer GPUs. Run them on yours and add a row.  ## Table of Contents  1. Introduction 2. Results 3. Quick Start 4. What Gets Measured 5. Contribute Your GPU 6. Ecosystem Status 7. License  ## 1. Introduction  **Speculative decoding** makes text generation faster without changing the output. A small *draft* model guesses the next few tokens, and the big model checks all of them in one pass. Every guess it accepts is a token you didn't have to wait for.  **DSpark** is DeepSeek's take on it: the drafter proposes a whole block of tokens at onc…
