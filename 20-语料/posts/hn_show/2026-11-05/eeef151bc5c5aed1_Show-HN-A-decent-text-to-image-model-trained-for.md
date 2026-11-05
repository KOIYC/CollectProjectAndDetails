---
type: "corpus"
item_id: "eeef151bc5c5aed1"
title: "Show HN: A decent text-to-image model trained for ~$20K (Apache 2.0 Weights)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50368208"
project_url: "https://linum.ai/field-notes/pjit-21k"
author: "schopra909"
published_at: "2026-11-04T16:45:11Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_schopra909
  - story_50368208
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: A decent text-to-image model trained for ~$20K (Apache 2.0 Weights)

> [!info] 一句话导读
> My brother and I run a 2-person lab that trains our own generative video models from scratch. The ultimate goal is a set of creative tools that make it easier f…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50368208>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：schopra909　|　发布：2026-11-04T16:45:11Z
> 项目链接：<https://linum.ai/field-notes/pjit-21k>
> 采集：2026-11-05T11:21:45+08:00　|　id：`eeef151bc5c5aed1`

## 正文

My brother and I run a 2-person lab that trains our own generative video models from scratch. The ultimate goal is a set of creative tools that make it easier for anyone to make animation.Video models today are too slow/expensive and lack sufficient controls. Creativity is an iterative process. You make, you tweak, you get better. In our opinion, they're not usable yet for storytelling.When we set out to build Linum v3 (our next video model) earlier this year, the primary goal was to bring the cost envelope of inference down significantly. If our model is fast and cheap, it's the first step (of many) towards useful creative tools.Typically, you see "latent diffusion models". A VAE (Variational Autoencoder) compresses the input data into a smaller "latent space" and the diffusion model learns how to generate within this subspace.Over the past few months, we've been publishing our work on efficient pixel-space diffusion models. These throw away the VAE, having the diffusion model learn a latent-space optimized for its exact task.This serves 3 purposes:
1) Simplify Architecture (no 2-stage model training)
2) Faster Convergence (11x faster convergence vs. our latent diffusion counterpart)
3) Cheaper Inference (4x more aggressive token reduction in attention context-windows, without significant loss in quality)This past month we were pressure testing our latest architecture (Pyramid-JiT) by training a text-to-image model longer than the typical one-off experiment. Specifically, we trained it for ~$20K on 660M samples.We were surprised by the quality of results, so we thought we'd release it as open weights for the community (Apache 2.0). The research itself is already public, on our website.For us, it's a big stepping stone towards cheaper video models, since pretty much all video models start as image models. We like to say these models have to learn nouns before they learn verbs.

## 导航

- 项目页：[[10-项目/linum.ai_0fc0f6ed]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
