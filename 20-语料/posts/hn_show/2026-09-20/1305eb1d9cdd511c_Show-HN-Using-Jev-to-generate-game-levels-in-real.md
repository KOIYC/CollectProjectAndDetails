---
type: "corpus"
item_id: "1305eb1d9cdd511c"
title: "Show HN: Using Jev to generate game levels in real time"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49754951"
project_url: "https://spritefusion.com/blog/generating-game-level-in-real-time-with-jev"
author: "HugoDz"
published_at: "2026-09-18T14:30:50Z"
captured_at: "2026-09-20T14:02:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_HugoDz
  - story_49754951
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: Using Jev to generate game levels in real time

> [!info] 一句话导读
> Published: 2026-09-18

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49754951>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：HugoDz　|　发布：2026-09-18T14:30:50Z
> 项目链接：<https://spritefusion.com/blog/generating-game-level-in-real-time-with-jev>
> 采集：2026-09-20T14:02:25+08:00　|　id：`1305eb1d9cdd511c`

## 正文

Published: 2026-09-18
Author: Hugo Duprez

Generating levels in real time with the Jev model - Sprite Fusion

# Generating levels in real time with the Jev model

Hugo - September 18, 2026

An AI model is generating the level in real time. Pretty cool, right?

On September 15, 2026, TypeSafe introduced Jev, a model designed to return structured outputs with low latency and low cost. "Eh but that's just a classifier". Ok; but can it generate a platformer level in real time? Let's see!

## Why Jev looks promising for games

Unlike text-gen. models such as GPT or Fable, Jev is designed to return structured decisions. In short, it's a zero-shot classifier: it gives you picks with probabilities attached rather than raw text.

LLM vs Jev

Task: choose platform widths and gaps.

LLM

Terrain described in words

Jev

Terrain returned as choices

Now, there are two major bottlenecks to using AI at runtime in games:

1. Latency. In most cases, you can't afford to wait five minutes for a model to think.
2. Cost. Some will disagree, but I think current LLM pricing makes them pointless for games. It makes no sense to me to pay for expensive API calls if I talk more to the tavern keeper.

Jev promises to help with both: sub-second responses at $0.042 per million input tokens, with free output tokens. Source

Ok. Let's test the claims by fire.

## Preparing a test game

For this experiment, I wanted a runner game prototype in a neon-night style. Serious things here, we'll use Sprite Fusion for pixel art generation, PhaserJS, and Codex with Astra.

Ninja Runner assets

You

Use the Sprite Fusion API to create a neon-night ninja sprite + animations for a runner game.

Codex

I created the sprites and animations, and added movement and collisions.

Idle

Run

Jump

Attack

#### Feeding the game state & context

First, we take a snapshot of the game state: player position and velocity, current terrain blocks, dash state, etc. We send that in the request to Jev alongside some example terrain layouts.

```
{"x":158.86,"y":86.87,"vx":2.27,"vy":-2.34,"grounded":false,"dash_ready":true}
```

#### Jev request

The task we give Jev is fairly simple: given the current game state, how would you fill the next slice of terrain? We ask about widths, gaps, heights and surface types through several choice questions, all sent in one API call. Here are the options we allow:

Surface type

Solid roof or one-way ledge

Width

2, 3 or 5 blocks

Gap before it

0, 1 or 2 blocks

Height

Rows 4–9

##### Choices Jev made

The four surfaces from one recorded Jev response. Gap is measured before each surface; row numbers increase downward.

| Surface | Type | Width | Gap before | Height |
| --- | --- | --- | --- | --- |
| 1 | Ledge | 2 blocks | None | Row 5 |
| 2 | Ledge | 3 blocks | 1 block | Row 6 |
| 3 | Ledge | 5 blocks | 2 blocks | Row 5 |
| 4 | Solid roof | 2 blocks | None | Row 4 |

Terrain built from those choices

My code then places the chosen blocks and gaps.

Live terrain generation in the game

### So, costs and latency ?

Requests (in this demo)

5

Jev API latency

319–375 ms

Est. average cost / request

$0.00057

Est. cost / demo

$0.00286

Well, it's not bad at all. Jev generates the terrain fast enough to keep the runner moving, at a very low cost. It's not sub-100ms latency nor free but interersting enough to pay attention for games. I've played the demo for longer, and the latency stays stable. Level generation keeps working fine.

## Conclusion

Promising! There are plenty of ways to generate levels using handwritten rules and heuristics, I know. But still, cheaper and faster structured output models opens up a whole range of ideas and experiments for games. I'm gonna share more soon.

## Sources and acknowledgments

- TypeSafe: Introducing System One models and Jev.
- Jev docs: state, choices, parallel questions, model limitations and pricing.
- Sprite Fusion: pixel art assets and animations.

# Jev Pong

## 评论（1/1）

> **tariqshams** · 2026-09-18T14:38:45.000Z　
> Very interesting demo!

## 导航

- 项目页：[[10-项目/spritefusion.com_a2b542d7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
