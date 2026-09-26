---
type: "project"
title: "Show HN: Agate, a 260M image model with separate thinker and renderer"
project_url: "https://huggingface.co/Logolabs/agate-preview-001"
first_seen: "2026-09-26T09:41:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_stefatorus
  - story_49848811
  - show_hn
lang: "en"
---

# Show HN: Agate, a 260M image model with separate thinker and renderer

> [!info] 一句话导读
> Agate is a 260M-parameter text-to-image model trained from scratch in 145 GPU-hours. It scores 0.550 on GenEval with the official scorer, level with SDXL's publ…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://huggingface.co/Logolabs/agate-preview-001>
> 首次收录：2026-09-26T09:41:08+08:00
> 来源渠道：HN Show HN
> 标签：author_stefatorus, story_49848811, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-26/dd8d91772ff8025a_Show-HN-Agate,-a-260M-image-model-with-separate-th]] |

## 摘要正文

# Agate Preview 001  Agate is a 260M-parameter text-to-image model trained from scratch in 145 GPU-hours. It scores 0.550 on GenEval with the official scorer, level with SDXL's published 0.55 and above SD 1.5 (0.43), SD 2.1 (0.50) and PixArt-α (0.48). It is small enough to run in under two seconds on a consumer GPU.  Built by LogoLabs, which makes AI logo generation, as a better small model for icon generation.  ## At a glance  | What | Text-to-image, 256 × 256, English prompts | | --- | --- | | Size | 260M parameters with TAESD, 308.5M with SD-VAE: 190.9M generator + 68.1M text encoder + decoder | | Training | From scratch, 144.7 GH200-hours, under 13 h wall-clock, 146.9M images seen (≈26 epochs) | | Energy | 81.8 kWh and 2.45 kg CO₂e for Agate; 176.7 kWh for the whole project, measured with perun | | GenEval (official) | 0.550. SDXL 0.55, SD 2.1 0.50, PixArt-α 0.48, SD 1.5 0.43 (published) | | Qwen-Image-Bench (1,000 prompts) | 28.2, against SD 1.5's 29.1; on the Pareto frontier among open models of similar size | | Speed | 1.9 s per image on an RTX 4060 (50 steps); also runs in the browser: WebGPU demo | | Strengths | Placing objects (left of, on top of), binding colours to obje…
