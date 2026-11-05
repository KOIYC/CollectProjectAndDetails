---
type: "project"
title: "Show HN: A decent text-to-image model trained for ~$20K (Apache 2.0 Weights)"
project_url: "https://linum.ai/field-notes/pjit-21k"
first_seen: "2026-11-05T11:21:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_schopra909
  - story_50368208
  - show_hn
lang: "en"
---

# Show HN: A decent text-to-image model trained for ~$20K (Apache 2.0 Weights)

> [!info] 一句话导读
> My brother and I run a 2-person lab that trains our own generative video models from scratch. The ultimate goal is a set of creative tools that make it easier f…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://linum.ai/field-notes/pjit-21k>
> 首次收录：2026-11-05T11:21:45+08:00
> 来源渠道：HN Show HN
> 标签：author_schopra909, story_50368208, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:21:45+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-05/eeef151bc5c5aed1_Show-HN-A-decent-text-to-image-model-trained-for]] |

## 摘要正文

My brother and I run a 2-person lab that trains our own generative video models from scratch. The ultimate goal is a set of creative tools that make it easier for anyone to make animation.Video models today are too slow/expensive and lack sufficient controls. Creativity is an iterative process. You make, you tweak, you get better. In our opinion, they're not usable yet for storytelling.When we set out to build Linum v3 (our next video model) earlier this year, the primary goal was to bring the cost envelope of inference down significantly. If our model is fast and cheap, it's the first step (of many) towards useful creative tools.Typically, you see "latent diffusion models". A VAE (Variational Autoencoder) compresses the input data into a smaller "latent space" and the diffusion model learns how to generate within this subspace.Over the past few months, we've been publishing our work on efficient pixel-space diffusion models. These throw away the VAE, having the diffusion model learn a latent-space optimized for its exact task.This serves 3 purposes: 1) Simplify Architecture (no 2-stage model training) 2) Faster Convergence (11x faster convergence vs. our latent diffusion counterpa…
