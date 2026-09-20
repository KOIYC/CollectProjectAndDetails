---
type: "corpus"
item_id: "0baa411fbd48c638"
title: "Show HN: Jev vs. GPT-5.6 and Claude Haiku at Pong"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49754516"
project_url: "https://jev-pong.ably.dev/"
author: "matt_oriordan"
published_at: "2026-09-18T13:58:15Z"
captured_at: "2026-09-20T14:02:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_matt_oriordan
  - story_49754516
  - show_hn
metrics: {"points": 10, "comments": 4, "engagement_velocity": 10}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:90d"
---

# Show HN: Jev vs. GPT-5.6 and Claude Haiku at Pong

> [!info] 一句话导读
> Jev returns a decision in 227 ms. The chat models take 2.5 to 3.5 seconds.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49754516>
> 指标：点赞=10 · 评论=4 · engagement_velocity=10
> 作者：matt_oriordan　|　发布：2026-09-18T13:58:15Z
> 项目链接：<https://jev-pong.ably.dev/>
> 采集：2026-09-20T14:02:28+08:00　|　id：`0baa411fbd48c638`

## 正文

Jev Pong

# Jev returns a decision in 227 ms. The chat models take 2.5 to 3.5 seconds.

Here's what that does to a game of Pong.

Recorded run · Vercel (iad1) via Vercel AI Gateway

replay 0.0 s

### Jev

TypeSafe AI

— ms

0 decisions · 0 returns

### Gemini 3.8 Flash

Google

### Claude Haiku 4.5

Anthropic

— ms

### GPT-5.6 Sol

OpenAI

model decisions/s avg ms p95 ms in first 12 s

Jev TypeSafe AI

4.40 227 400 47

Gemini 3.8 Flash Google

0.32 3167 7438 3

Claude Haiku 4.5 Anthropic

0.40 2483 8358 2

GPT-5.6 Sol OpenAI

0.28 3529 10350 2

Four lanes, one game: same serve, same rules, same question, asked of a different model in each. One answer moves the ball one step, so every ball travels at its own model's answer time and nothing is skipped or sped up. Jev is a typed-decision model rather than a chat model, and Pong is the Atari game chat models handle worst, so a loop that won't wait is the fair place to see what that's worth.

## 评论（4/4）

> **matt_oriordan** · 2026-09-18T13:59:59.000Z　
> Hi HN, Matt here, co-founder of Ably. I built this after Jev landed on Vercel's AI Gateway: https://github.com/ably-labs/jev-pongIt's pong where the ball moves one step per model decision.Four lanes, one model each, same serve, same rules.Every step the model gets the same tiny JSON state (ball, paddle, predicted intercept) and the same question: up, down or stay. One answer moves the ball one segment; eight segments cross the court. No speed up / adjustments for real play, so a lane's speed is that model's decision latency.Numbers, recorded on Vercel (iad1) next to the gateway, 45 seconds per lane: Jev averaged 227 ms (p95 400 ms). Gemini 3.2 s, Haiku 2.5 s, GPT-5.6 Sol 3.5 s.In the first 12 seconds: 47 decisions vs 3, 2 and 2.Bit of fun! Enjoy

---

> **AnodicElegy** · 2026-09-18T15:57:09.000Z　
> The game is broken for me. The ball just sits in the middle.

---

> **leodavi** · 2026-09-18T15:57:34.000Z　
> The pong demo is giving "Point to Jev" before it's even reached my paddle on mobile. I also don't really understand the frontpage model-speed comparison: it looks like you're slowing the ball down to compensate for the models' decision-making speeds? If so I think a more effective metric would be N-x, e.g. we slowed this game down 8-x (compared to Jev's game) for e.g. Sol to stay competitive. Or, just watching them fail would be cool too, though I know it's just a simulation and no real inference is being ran (except for Jev, maybe).

---

> **moribvndvs** · 2026-09-18T16:10:21.000Z　
> lol, playing against jev the ball routinely disappears dozens of pixels away from my paddle and it just awards itself the point anyways. Big Obama awarding Obama energy.

## 导航

- 项目页：[[10-项目/jev-pong.ably.dev_7c4a5ff2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
