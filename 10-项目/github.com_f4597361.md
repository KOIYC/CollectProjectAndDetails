---
type: "project"
title: "Show HN: We compressed a 31B video+audio diffusion model to 14B, 6 steps, INT8"
project_url: "https://github.com/Video-Rebirth/hyperflow-h3-flash"
first_seen: "2026-11-08T12:50:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jiant
  - story_50405263
  - show_hn
lang: "en"
---

# Show HN: We compressed a 31B video+audio diffusion model to 14B, 6 steps, INT8

> [!info] 一句话导读
> Video-Rebirth/hyperflow-h3-flash

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Video-Rebirth/hyperflow-h3-flash>
> 首次收录：2026-11-08T12:50:31+08:00
> 来源渠道：HN Show HN
> 标签：author_jiant, story_50405263, show_hn
> 最新指标：点赞=59 · 评论=12 · engagement_velocity=59

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-08T12:50:31+08:00 | HN Show HN | 点赞=59 · 评论=12 · engagement_velocity=59 | [[20-语料/posts/hn_show/2026-11-08/b52da40891f8dcf2_Show-HN-We-compressed-a-31B-video+audio-diffusion]] |

## 摘要正文

# Video-Rebirth/hyperflow-h3-flash  HyperFlow H3 Flash: Video Rebirth's 13.7B, 4- to 8-step compressed MiniMax-H3 for joint video and audio generation (INT8 and GGUF)  - Stars: 78 - Forks: 1 - Watchers: 78 - Open issues: 2 - License: Apache License 2.0 - Homepage: https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash - Default branch: main - Created: 2026-11-06T08:31:59Z  ## Languages  - Makefile - Python  ## Topics  - audio-generation - diffusers - few-step - gguf - int8 - minimax-h3 - video-generation  ---  ## README  # HyperFlow H3 Flash  HyperFlow H3 Flash is Video Rebirth's compressed, few-step version of MiniMax-H3. It generates video and synchronized stereo audio together.  **Showcase** · **Weights (Hugging Face)** · **ComfyUI nodes** · **GGUF setup guide** · **8-step LoRA for full-size MiniMax-H3**  - **Output:** 5.2–15 s of video at 24 fps (1344×768 by default) with a 32 kHz stereo soundtrack. - **Sampling:** 4, 6 (default), or 8 steps, without classifier-free guidance (CFG). - **Speed (5.2 s clip, 6 steps):** 8.7 s on 4× B200, 36 s on 1× H200, 92 s on 1× RTX 5090. - **Real time on 4× Blackwell GPUs:** NVIDIA SOL-H3 runs HyperFlow H3 Flash in real time on 4× B-series GP…
