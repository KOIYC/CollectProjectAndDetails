---
type: "corpus"
item_id: "7ea3c8ae4f344e5a"
title: "Show HN: \"Be horse.\" – a diffusion language model on an M2 Air"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47962008"
project_url: "https://boesch.dev/posts/simple-dlm"
author: "encrux"
published_at: "2026-04-30T13:20:16Z"
captured_at: "2026-09-21T02:52:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_encrux
  - story_47962008
  - show_hn
metrics: {"points": 10, "comments": 2, "engagement_velocity": 10}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: "Be horse." – a diffusion language model on an M2 Air

> [!info] 一句话导读
> Building My Own Diffusion Language Model

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47962008>
> 指标：点赞=10 · 评论=2 · engagement_velocity=10
> 作者：encrux　|　发布：2026-04-30T13:20:16Z
> 项目链接：<https://boesch.dev/posts/simple-dlm>
> 采集：2026-09-21T02:52:26+08:00　|　id：`7ea3c8ae4f344e5a`

## 正文

Daniel's Blog
Posts
Tags
Archive
CV
Home » Posts
Building My Own Diffusion Language Model
Building a tiny diffusion language model from scratch and training on an M2 MacBook Air
April 29, 2026 · 5 min · Daniel Bösch
Table of Contents
Why?
Diffusion vs autoregressive
Training loop
Sampling
What undertraining sounds like
Stepping back
References
To be, fo hend!
First her sense ountier to Jupits,
be horse.
 Wise words! This is the results of 2 hours of training my very own PyTorch Diffusion Language Model on an M2 MacBook Air.
You can check out the code over at GitHub: github.com/Encrux/simple_dlm
Why? #
Diffusion Language Models are kind of a hot-topic right now in Machine Learning. The basic idea: corrupt some data with noise, then train a model to reverse that corruption over many small steps.
They’re used in a variety of domains, most notably in image synthesis. Image generation algorithms like Stable Diffusions treat this as a continuous problem on a per-pixel basis, because a pixel value of 134 is close to 135. For text, this principle is not as straight forward, because the latter “A”, which would convert to 65 is in no meaningful interpretation closer to “B” (ascii 66) than “Z” (ascii 90). The fix is to give up on numeric noise altogether. We corrupt the sequence by replacing tokens with a [MASK] token, and let the model learn to predict what was there.
This feels nothing like the physical noise picture, but it’s still proper diffusion math under the hood.
Diffusion vs autoregressive #
Pretty much any LLM currently in use is decoding tokens autoregressively, so why care about diffusion? Autoregressive models force left-to-right decoding by design. With diffusion, we can decode the entire sequence in parallel and reach a low entropy state (i.e. actual text) by repeated denoising over the same sequence.
In theory, this can yield significantly higher tokens per second. Models like Mercury2 are working towards demonstrating this in the real world.
Training loop #
For training, we grab a random 128-char chunk from the training data and sample a random masking probability mask_prob ~ U(0, 1) . This fraction is replaced with the [MASK] -token.
After the forward pass, we train the model using cross-entropy loss on only the masked tokens. Mask_prob itself also gets passed into the model as an input. That’s what lets one network handle every noise level, from a barely-masked sequence to a fully-masked one.
Sampling #
For decoding, we begin by setting all tokens to [MASK]. We then run k denoising steps, committing more tokens each time, until the sequence is fully revealed. In this example, k = 20.
What undertraining sounds like #
Step 67k, loss 1.22:
To be, and be of men?
Prown AMEN:
O yout aboars of
Ra':
Un
 Step 77k, loss 1.09:
To be, fo hend!
First her sense ountier to Jupits,
be horse.
 The output is obviously mostly nonsense, but the fact that it learned to ouptut real words and strings that resemble actual sentences even a tiny bit is quite impressive considering the hardware it has been trained on. Tokens are encoded per-character, so the model had to learn this from scratch.
Stepping back #
This write-up is barely scratching the surface. The different flavors of language models keep increasing in numbers. I didn’t address shortcomings like actual model performance, fixed decoding lengths and how these are (or could be) addressed.
There’s a lot of scary buzz words floating around in the age of AI. Projects like these help me make sense of key concepts that I think are worth knowing about. I think diffusion models are fascinating. In the future, I definitely want to learn more about their inner workings, especially when it comes to multi-modal models.
References #
Mercury (Inception Labs, 2025) - very fast DLM
LLaDA: Large Language Diffusion Models (Nie et al., 2025)
How Efficient Are Diffusion Language Models? (2026)
The Original masked language model: BERT (Devlin et al., 2018)
Sander Dieleman, “Diffusion is spectral autoregression”
Inspiration (and dataset) for this Project: Karpathy, nanoGPT
Source code
Llm
Diffusion
PyTorch
« Prev
Training a robot to thread a peg through a keyhole in 36 hours
Next »
What happens when you let an LLM write robot programs?
© 2026 Daniel's Blog ·
Powered by
 Hugo &
 PaperMod
Impressum
 ·
 Datenschutz

## 评论（2/2）

> **ricardobeat** · 2026-04-30T18:11:12.000Z　
> Love this kind of experiment. Would the model perform better with word tokens?

---

> **encrux** · 2026-05-03T19:33:19.000Z　
> A friend of mine forked the repo and tried it with BPE (Byte-Pair Encodings), and it did noticeably improve performance.

## 导航

- 项目页：[[10-项目/boesch.dev_794098d3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
