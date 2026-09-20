---
type: "project"
title: "Show HN: Jev vs. GPT-5.6 and Claude Haiku at Pong"
project_url: "https://jev-pong.ably.dev/"
first_seen: "2026-09-20T14:02:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_matt_oriordan
  - story_49754516
  - show_hn
lang: "en"
---

# Show HN: Jev vs. GPT-5.6 and Claude Haiku at Pong

> [!info] 一句话导读
> Jev returns a decision in 227 ms. The chat models take 2.5 to 3.5 seconds.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://jev-pong.ably.dev/>
> 首次收录：2026-09-20T14:02:28+08:00
> 来源渠道：HN Show HN
> 标签：author_matt_oriordan, story_49754516, show_hn
> 最新指标：点赞=10 · 评论=4 · engagement_velocity=10

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=10 · 评论=4 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/0baa411fbd48c638_Show-HN-Jev-vs.-GPT-5.6-and-Claude-Haiku-at-Pong]] |
| 2026-09-20T09:36:40+08:00 | HN Show HN | 点赞=10 · 评论=4 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/0baa411fbd48c638_Show-HN-Jev-vs.-GPT-5.6-and-Claude-Haiku-at-Pong]] |
| 2026-09-20T14:02:28+08:00 | HN Show HN | 点赞=10 · 评论=4 · engagement_velocity=10 | [[20-语料/posts/hn_show/2026-09-20/0baa411fbd48c638_Show-HN-Jev-vs.-GPT-5.6-and-Claude-Haiku-at-Pong]] |

## 摘要正文

Jev Pong  # Jev returns a decision in 227 ms. The chat models take 2.5 to 3.5 seconds.  Here's what that does to a game of Pong.  Recorded run · Vercel (iad1) via Vercel AI Gateway  replay 0.0 s  ### Jev  TypeSafe AI  — ms  0 decisions · 0 returns  ### Gemini 3.8 Flash  Google  ### Claude Haiku 4.5  Anthropic  — ms  ### GPT-5.6 Sol  OpenAI  model decisions/s avg ms p95 ms in first 12 s  Jev TypeSafe AI  4.40 227 400 47  Gemini 3.8 Flash Google  0.32 3167 7438 3  Claude Haiku 4.5 Anthropic  0.40 2483 8358 2  GPT-5.6 Sol OpenAI  0.28 3529 10350 2  Four lanes, one game: same serve, same rules, same question, asked of a different model in each. One answer moves the ball one step, so every ball travels at its own model's answer time and nothing is skipped or sped up. Jev is a typed-decision model rather than a chat model, and Pong is the Atari game chat models handle worst, so a loop that won't wait is the fair place to see what that's worth.
