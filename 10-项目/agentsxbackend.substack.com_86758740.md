---
type: "project"
title: "Show HN: The Three Idempotencies of an Agent"
project_url: "https://agentsxbackend.substack.com/p/the-three-idempotencies-of-an-agent"
first_seen: "2026-09-21T02:53:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Venky1729
  - story_48730327
  - show_hn
lang: "en"
---

# Show HN: The Three Idempotencies of an Agent

> [!info] 一句话导读
> Published: 2026-06-30

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://agentsxbackend.substack.com/p/the-three-idempotencies-of-an-agent>
> 首次收录：2026-09-21T02:53:12+08:00
> 来源渠道：HN Show HN
> 标签：author_Venky1729, story_48730327, show_hn
> 最新指标：点赞=5 · 评论=1 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/8ae4946e9ccb6ba1_Show-HN-The-Three-Idempotencies-of-an-Agent]] |
| 2026-09-21T01:45:12+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/8ae4946e9ccb6ba1_Show-HN-The-Three-Idempotencies-of-an-Agent]] |
| 2026-09-21T02:53:12+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/8ae4946e9ccb6ba1_Show-HN-The-Three-Idempotencies-of-an-Agent]] |

## 摘要正文

Published: 2026-06-30 Author: Venky  The Three Idempotencies of an Agent - Venky's Substack  # Venky's Substack  SubscribeSign in  # The Three Idempotencies of an Agent  ### One word, three problems: one burns tokens, one double-charges the customer, and one nobody has cleanly solved.  Venky  Jun 30, 2026  1  Share  ## The duplicate run and the double-charge are not the same bug  Two things go wrong in production agent systems, and engineers reach for the same word to describe both.  Two things go wrong in production agent systems, and engineers reach for the same word to describe both.  Thanks for reading Venky's Substack! Subscribe for free to receive new posts and support my work.  Subscribe  Here’s the first. A billing webhook fires your agent, something like`agent("settle the charges for order #88421", tools=[...])`. The run is slow. The webhook redelivers the same event, because delivery is at-least-once and this is routine, and a second run picks up the same order while the first is still going. Now two identical agent runs are grinding through the same expensive reasoning in parallel, burning twice the tokens. If both reach the charge step, you have a race you never designe…
