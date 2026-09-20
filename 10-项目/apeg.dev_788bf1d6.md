---
type: "project"
title: "Show HN: Running Gemma-4 26B at 124 tokens/SEC on a CPU, no GPU"
project_url: "https://apeg.dev/writing/running-gemma4-26b-on-a-cpu"
first_seen: "2026-09-21T01:45:02+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_arun-prasath
  - story_48731643
  - show_hn
lang: "en"
---

# Show HN: Running Gemma-4 26B at 124 tokens/SEC on a CPU, no GPU

> [!info] 一句话导读
> I wanted to know how fast a 26B mixture-of-experts model could run on a desktop CPU with no GPU. Got ~40 tok/s single-stream (lossless) and ~124 batched. The su…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://apeg.dev/writing/running-gemma4-26b-on-a-cpu>
> 首次收录：2026-09-21T01:45:02+08:00
> 来源渠道：HN Show HN
> 标签：author_arun-prasath, story_48731643, show_hn
> 最新指标：点赞=10 · 评论=1 · engagement_velocity=10

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=10 · 评论=1 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/e27dc17a91a6a5a8_Show-HN-Running-Gemma-4-26B-at-124-tokens-SEC-on-a]] |
| 2026-09-21T01:45:02+08:00 | HN Show HN | 点赞=10 · 评论=1 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-21/e27dc17a91a6a5a8_Show-HN-Running-Gemma-4-26B-at-124-tokens-SEC-on-a]] |

## 摘要正文

I wanted to know how fast a 26B mixture-of-experts model could run on a desktop CPU with no GPU. Got ~40 tok/s single-stream (lossless) and ~124 batched. The surprising part was the byte budget: for this model you compress the output head (32% of per-token bytes), not the experts (16%). The writeup has the bandwidth roofline and the dead-ends; the repo has the reproducible recipe. Happy to answer questions.Repo: https://github.com/arun-prasath2005/gemma4-cpu-moe
