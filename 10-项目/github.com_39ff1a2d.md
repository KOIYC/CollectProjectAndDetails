---
type: "project"
title: "Show HN: BitRun v0.2 – Run 8B ternary LLMs on CPU with live wattage telemetry"
project_url: "https://github.com/IshekKhal/bitrun"
first_seen: "2026-10-16T09:35:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ishekofficial
  - story_50106895
  - show_hn
lang: "en"
---

# Show HN: BitRun v0.2 – Run 8B ternary LLMs on CPU with live wattage telemetry

> [!info] 一句话导读
> Single-binary runner and model manager for 1-bit / 1.58-bit ternary LLMs (Microsoft BitNet b1.58) on CPU (macOS, Windows, Linux)

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/IshekKhal/bitrun>
> 首次收录：2026-10-16T09:35:18+08:00
> 来源渠道：HN Show HN
> 标签：author_ishekofficial, story_50106895, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-16/8806a227be8e8570_Show-HN-BitRun-v0.2-–-Run-8B-ternary-LLMs-on-CPU-w]] |

## 摘要正文

# IshekKhal/bitrun  Single-binary runner and model manager for 1-bit / 1.58-bit ternary LLMs (Microsoft BitNet b1.58) on CPU (macOS, Windows, Linux)  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-12T06:12:05Z  ## Languages  - Batchfile - Go - PowerShell - Shell  ## Topics  - 1-bit - arm-neon - avx2 - bitnet - cli - cpu-inference - llm - ternary - zero-compile  ## Top Contributors  - IshekKhal (9 contributions)  ---  ## README  # BitRun ⚡️  > **Zero-compile, single-binary runner and model manager for Microsoft BitNet b1.58 and 1.58-bit ternary LLMs on macOS, Windows, and Linux CPUs.**  License Release Architecture  ---  ## Why BitRun?  Microsoft's **BitNet b1.58** proved that ternary (1-bit / 1.58-bit) models can run at extreme speeds on commodity CPUs with 70–80% lower energy consumption by eliminating floating-point multiplications.  Ternary models are engineered for **local CPU inference, battery-powered laptops, edge devices, and embedded tasks** where running heavy FP16 or INT4 models drains battery or requires dedicated GPUs.  However, testing `BitNet.cpp` today requires: * Cloning recursive submodules and…
