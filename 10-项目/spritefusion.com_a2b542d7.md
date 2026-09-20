---
type: "project"
title: "Show HN: Using Jev to generate game levels in real time"
project_url: "https://spritefusion.com/blog/generating-game-level-in-real-time-with-jev"
first_seen: "2026-09-20T14:02:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_HugoDz
  - story_49754951
  - show_hn
lang: "en"
---

# Show HN: Using Jev to generate game levels in real time

> [!info] 一句话导读
> Published: 2026-09-18

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://spritefusion.com/blog/generating-game-level-in-real-time-with-jev>
> 首次收录：2026-09-20T14:02:25+08:00
> 来源渠道：HN Show HN
> 标签：author_HugoDz, story_49754951, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/1305eb1d9cdd511c_Show-HN-Using-Jev-to-generate-game-levels-in-real]] |
| 2026-09-20T09:36:39+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/1305eb1d9cdd511c_Show-HN-Using-Jev-to-generate-game-levels-in-real]] |
| 2026-09-20T14:02:25+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/1305eb1d9cdd511c_Show-HN-Using-Jev-to-generate-game-levels-in-real]] |

## 摘要正文

Published: 2026-09-18 Author: Hugo Duprez  Generating levels in real time with the Jev model - Sprite Fusion  # Generating levels in real time with the Jev model  Hugo - September 18, 2026  An AI model is generating the level in real time. Pretty cool, right?  On September 15, 2026, TypeSafe introduced Jev, a model designed to return structured outputs with low latency and low cost. "Eh but that's just a classifier". Ok; but can it generate a platformer level in real time? Let's see!  ## Why Jev looks promising for games  Unlike text-gen. models such as GPT or Fable, Jev is designed to return structured decisions. In short, it's a zero-shot classifier: it gives you picks with probabilities attached rather than raw text.  LLM vs Jev  Task: choose platform widths and gaps.  LLM  Terrain described in words  Jev  Terrain returned as choices  Now, there are two major bottlenecks to using AI at runtime in games:  1. Latency. In most cases, you can't afford to wait five minutes for a model to think. 2. Cost. Some will disagree, but I think current LLM pricing makes them pointless for games. It makes no sense to me to pay for expensive API calls if I talk more to the tavern keeper.  Jev pr…
