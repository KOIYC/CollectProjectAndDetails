---
type: "corpus"
item_id: "7f363cfd1a4ad2d6"
title: "Show HN: Relay – a harness for AI coding agents that recover and verify"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49898411"
project_url: "https://relayevals.com/"
author: "rsathwik07"
published_at: "2026-09-29T18:46:07Z"
captured_at: "2026-09-30T18:28:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_rsathwik07
  - story_49898411
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Relay – a harness for AI coding agents that recover and verify

> [!info] 一句话导读
> I'm tired of AI coding agents which are good for 30 seconds and then completely fail on the slightest hiccup: a failing test, a temporarily unavailable dependen…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49898411>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：rsathwik07　|　发布：2026-09-29T18:46:07Z
> 项目链接：<https://relayevals.com/>
> 采集：2026-09-30T18:28:30+08:00　|　id：`7f363cfd1a4ad2d6`

## 正文

I'm tired of AI coding agents which are good for 30 seconds and then completely fail on the slightest hiccup: a failing test, a temporarily unavailable dependency, an incorrect assumption. Sometimes I end up having to babysit these agents anyway.Relay is a harness for coding agents which takes advantage of the fact that agents are often good at doing something slightly wrong, and not so good at doing something correctly and completely. Relay repeatedly tries the task and on each failure, uses the output to find a better way to do it.It does this by running the task in a loop: attempt the task, run the checks in a fresh sandbox, on failure read the error and retry instead, until the checks pass. What it learned from a run is retained, so that it doesn't repeat the same mistake, and when the checks eventually pass, it will ship the change as a normal git PR - no hidden state, no magic, the diff is human readable.A few specifics:- it runs locally, is free, and doesn't require an account to run the local agent
- it uses a top-tier model to plan/review, and cheaper models to actually write code (for cost reasons)
- happy to discuss why this is a good idea and why it isn't
- the checks run in an isolated sandbox for each task, rather than "trusting" the agent
- currently supports [list actual models/integrations - Opus 5.5, GPT-6, etc]
- there's a paid tier for running this unattended across multiple repos with shared sandbox minutes, the actual agent is free.It's not magic, it's not AGI, and it will fail badly on some problems.Would appreciate feedback, particularly from people who've deployed agents unattended and found that they don't actually work, or have had to build substantial tooling around them to get useful results.

## 导航

- 项目页：[[10-项目/relayevals.com_a3ebb9bb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
