---
type: "project"
title: "Show HN: \"Be horse.\" – a diffusion language model on an M2 Air"
project_url: "https://boesch.dev/posts/simple-dlm"
first_seen: "2026-09-21T02:52:26+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_encrux
  - story_47962008
  - show_hn
lang: "en"
---

# Show HN: "Be horse." – a diffusion language model on an M2 Air

> [!info] 一句话导读
> Building My Own Diffusion Language Model

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://boesch.dev/posts/simple-dlm>
> 首次收录：2026-09-21T02:52:26+08:00
> 来源渠道：HN Show HN
> 标签：author_encrux, story_47962008, show_hn
> 最新指标：点赞=10 · 评论=2 · engagement_velocity=10

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=10 · 评论=2 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/7ea3c8ae4f344e5a_Show-HN-Be-horse.-–-a-diffusion-language-model-on]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=10 · 评论=2 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/7ea3c8ae4f344e5a_Show-HN-Be-horse.-–-a-diffusion-language-model-on]] |
| 2026-09-21T01:41:02+08:00 | HN Show HN | 点赞=10 · 评论=2 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/7ea3c8ae4f344e5a_Show-HN-Be-horse.-–-a-diffusion-language-model-on]] |
| 2026-09-21T02:52:26+08:00 | HN Show HN | 点赞=10 · 评论=2 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/7ea3c8ae4f344e5a_Show-HN-Be-horse.-–-a-diffusion-language-model-on]] |

## 摘要正文

Daniel's Blog Posts Tags Archive CV Home » Posts Building My Own Diffusion Language Model Building a tiny diffusion language model from scratch and training on an M2 MacBook Air April 29, 2026 · 5 min · Daniel Bösch Table of Contents Why? Diffusion vs autoregressive Training loop Sampling What undertraining sounds like Stepping back References To be, fo hend! First her sense ountier to Jupits, be horse.  Wise words! This is the results of 2 hours of training my very own PyTorch Diffusion Language Model on an M2 MacBook Air. You can check out the code over at GitHub: github.com/Encrux/simple_dlm Why? # Diffusion Language Models are kind of a hot-topic right now in Machine Learning. The basic idea: corrupt some data with noise, then train a model to reverse that corruption over many small steps. They’re used in a variety of domains, most notably in image synthesis. Image generation algorithms like Stable Diffusions treat this as a continuous problem on a per-pixel basis, because a pixel value of 134 is close to 135. For text, this principle is not as straight forward, because the latter “A”, which would convert to 65 is in no meaningful interpretation closer to “B” (ascii 66) than “Z…
