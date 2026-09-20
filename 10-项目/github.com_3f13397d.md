---
type: "project"
title: "Show HN: Our GLM-5.3 Flash Switchless recipe is now out for 4x DGX Sparks"
project_url: "https://github.com/alexellis/glm-5.3-flash-4x-dgx-spark-switchless"
first_seen: "2026-09-21T03:11:23+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_alexellisuk
  - story_49508834
  - show_hn
lang: "en"
---

# Show HN: Our GLM-5.3 Flash Switchless recipe is now out for 4x DGX Sparks

> [!info] 一句话导读
> alexellis/glm-5.3-flash-4x-dgx-spark-switchless

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/alexellis/glm-5.3-flash-4x-dgx-spark-switchless>
> 首次收录：2026-09-21T03:11:23+08:00
> 来源渠道：HN Show HN
> 标签：author_alexellisuk, story_49508834, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/17924b453e15b877_Show-HN-Our-GLM-5.3-Flash-Switchless-recipe-is-now]] |
| 2026-09-21T02:56:39+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/17924b453e15b877_Show-HN-Our-GLM-5.3-Flash-Switchless-recipe-is-now]] |
| 2026-09-21T03:11:23+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/17924b453e15b877_Show-HN-Our-GLM-5.3-Flash-Switchless-recipe-is-now]] |

## 摘要正文

# alexellis/glm-5.3-flash-4x-dgx-spark-switchless  GLM-5.3-Flash (NVFP4) at TP4 across 4x DGX Spark via a switchless RoCE ring + DFlash2 — reproducible recipe  - Stars: 14 - Forks: 0 - Watchers: 14 - Open issues: 0 - License: Other - Default branch: master - Created: 2026-08-29T19:21:24Z  ## Languages  - Shell  ## Top Contributors  - alexellis (10 contributions)  ---  ## README  # GLM-5.3-Flash NVFP4 — 4× DGX Spark, switchless-ring TP4 + DFlash2  GLM-5.3-Flash (320B-A18B, NVFP4) served TP4 across four NVIDIA DGX Spark nodes on a switchless ring  Serve **GLM-5.3-Flash (NVFP4)** across **four NVIDIA DGX Spark (GB10 / `sm_121`) nodes** as one tensor-parallel engine — joined by a **switchless RoCE ring** and accelerated by the **DFlash2 speculative drafter**. One OpenAI-compatible endpoint, a 262K context window, ~45 tok/s on real agentic traffic — on hardware you own.  This repository is the **recipe and the contract**: every address, interface, and hostname is a placeholder you swap for your own — nothing here depends on a private gateway, router, or network.  **Not tied to these weights, either.** The ring fabric, the patched NCCL, and the rank-launch pattern know nothing about the …
