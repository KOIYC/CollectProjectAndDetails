---
type: "project"
title: "Show HN: TiGrIS, a tiling compiler that fits ML models onto embedded devices"
project_url: "https://github.com/raws-labs/tigris"
first_seen: "2026-09-21T02:52:40+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_asteinh
  - story_47945067
  - show_hn
lang: "en"
---

# Show HN: TiGrIS, a tiling compiler that fits ML models onto embedded devices

> [!info] 一句话导读
> Ahead-of-time compiler that tiles ML models to fit embedded devices with hard memory budgets.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/raws-labs/tigris>
> 首次收录：2026-09-21T02:52:40+08:00
> 来源渠道：HN Show HN
> 标签：author_asteinh, story_47945067, show_hn
> 最新指标：点赞=20 · 评论=0 · engagement_velocity=20

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=20 · 评论=0 · engagement_velocity=20 | [[20-语料/posts/hn_show/2026-09-21/e6795188975e2411_Show-HN-TiGrIS,-a-tiling-compiler-that-fits-ML-mod]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=20 · 评论=0 · engagement_velocity=20 | [[20-语料/posts/hn_show/2026-09-21/e6795188975e2411_Show-HN-TiGrIS,-a-tiling-compiler-that-fits-ML-mod]] |
| 2026-09-21T02:52:40+08:00 | HN Show HN | 点赞=20 · 评论=0 · engagement_velocity=20 | [[20-语料/posts/hn_show/2026-09-21/e6795188975e2411_Show-HN-TiGrIS,-a-tiling-compiler-that-fits-ML-mod]] |

## 摘要正文

# raws-labs/tigris  Ahead-of-time compiler that tiles ML models to fit embedded devices with hard memory budgets.  - Stars: 6 - Forks: 0 - Watchers: 6 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://tigris-ml.dev - Default branch: main - Created: 2026-02-11T06:21:17Z  ## Languages  - Python  ## Topics  - compiler - cortex-m - edge-ai - embedded-ml - inference - model-compression - onnx - quantization - tiling - tinyml  ## Top Contributors  - asteinh (23 contributions)  ---  ## README  # TiGrIS  License PyPI Docs  **Tiled Graph Inference Scheduler.** An ahead-of-time compiler that tiles ML models to fit embedded devices with hard memory budgets.  Give it an ONNX model and a memory budget. It partitions the compute graph into stages, tiles spatial operations, and emits a flat binary plan that the tigris-runtime executes with zero dynamic allocation.  ## The problem  On an embedded device with a few hundred KB of SRAM, most interesting models simply don't fit. The usual answer is to shrink the model: quantize harder, prune, pick a smaller architecture, and hope the accuracy hit is acceptable.  TiGrIS takes the other approach. It keeps the model you trained and rearr…
