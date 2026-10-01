---
type: "corpus"
item_id: "b75b2c4e7bd2c7c1"
title: "Show HN: Open-source model routing for coding agents at Astra-level performance"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49911500"
project_url: "https://github.com/weave-os/router"
author: "adchurch"
published_at: "2026-09-30T16:58:24Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_adchurch
  - story_49911500
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Open-source model routing for coding agents at Astra-level performance

> [!info] 一句话导读
> A few months ago we started building a model router for coding agents because we thought we could outperform any single model with an ensemble approach. Recentl…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49911500>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：adchurch　|　发布：2026-09-30T16:58:24Z
> 项目链接：<https://github.com/weave-os/router>
> 采集：2026-10-01T09:41:49+08:00　|　id：`b75b2c4e7bd2c7c1`

## 正文

A few months ago we started building a model router for coding agents because we thought we could outperform any single model with an ensemble approach. Recently we’ve achieved that milestone and I want to talk about how we did it.First of all, a quick explanation: the Weave Router (https://github.com/weave-os/router) plugs into any coding agent (e.g. Claude Code or Codex) and intelligently switches between LLMs. So, for example, Astra handles tricky debugging or complex system design tasks, and Deepseek v4 Flash handles simple frontend updates.What we’re announcing today is our new routing model, which we’re calling Weave Router 2.0. We benchmarked 2.0 against GPT-6 Astra on Terminal Bench 4.0 and SWE Atlas. On both benchmarks, the router had equivalent pass rates. On Terminal Bench, the router hit 52% of Astra’s cost, and completed tasks 2.2x faster. On SWE Atlas, the router cost 54% as much as Astra and ran 2.5x faster. (Full results on our website at https://weaveos.com/router!)It turns out training a model to route effectively - taking into consideration model capabilities, costs, cache awareness, and more - is a really hard problem! I want to talk about three ways we were able to improve so much over the last few months: 1) a new architecture, 2) larger training data set size, and 3) smarter cache-eviction impact calculation.1) a new architecture. Our initial approach used an RL model without many priors. While RL is still an important part of the story, the cost of fully exploring the space of routing decisions is very high, so we’ve taken some shortcuts that have significantly improved performance. In particular: we trained a hidden Markov model to trace the session state, then a classifier maps the session to one of a few buckets of similar models. This significantly shrinks the space to explore, by throwing out most models that could not reasonably serve the given session. This rearchitecture was the single biggest performance unlock!Consider how large the search space for the routing problem is. Take a typical coding agent session, with ~100 agent turns (i.e. 100 LLM API calls). Technically there are 100 chances to select a model. If we assume a roster of ~10 models (of course there are lots more but we can remove any that are Pareto dominated), then there are 10^100 possible paths through that session. We simply cannot explore all of them! So that's why clever tricks to shrink this space are so important.2) larger training data set size (much less technically interesting but still an important part of the story). By using frontier LLMs to help us label a larger and more diverse set of coding agent sessions, we were able to bootstrap the two models discussed in 1) to a better state, while also providing even richer reward signals for RL.3) smarter cache-eviction impact calculation. One of the hardest parts of routing well (if you care about saving money) is using the model caches intelligently. We built a subsystem that can calculate the expected value of switching models (and thus paying a high one-time cost to fill up a different cache) much more accurately, helping us avoid costly and unnecessary switches in more cases, while still switching when the benefit outweighs the cost. This is where most of our improvement on cost has come from.We still have a lot of room to continue to improve (we won’t rest until we’re consistently beating Astra/Fable, not just tying!) but matching frontier model performance was a huge milestone for our routing model, and in my opinion validates our initial hypothesis that an ensemble of models can do better than any single model ever could.Our router is open source (https://github.com/weave-os/router) so anyone can try it out. Or if you prefer you can use our hosted version (https://weaveos.com/router).

## 关联链接

- https://weaveos.com/router
- https://weaveos.com/router!

## 导航

- 项目页：[[10-项目/github.com_2a34e58a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
