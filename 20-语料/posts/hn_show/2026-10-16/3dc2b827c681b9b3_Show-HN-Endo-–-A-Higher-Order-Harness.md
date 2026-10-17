---
type: "corpus"
item_id: "3dc2b827c681b9b3"
title: "Show HN: Endo – A Higher-Order Harness"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50110614"
project_url: "https://github.com/longsurf-ai/endo"
author: "Warren93"
published_at: "2026-10-15T21:32:10Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_Warren93
  - story_50110614
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Endo – A Higher-Order Harness

> [!info] 一句话导读
> Endo is a Higher-Order Harness (HOH).From the easiest concept to understand to the more complex ones, Endo gives you:

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50110614>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：Warren93　|　发布：2026-10-15T21:32:10Z
> 项目链接：<https://github.com/longsurf-ai/endo>
> 采集：2026-10-16T09:35:18+08:00　|　id：`3dc2b827c681b9b3`

## 正文

Endo is a Higher-Order Harness (HOH).From the easiest concept to understand to the more complex ones, Endo gives you:
* A single, simple UI to use any agent provider with your existing subscriptions, and hot-swap agents right in the middle of a session.
* An orchestration layer, which I call HOH, allowing arbitrary composition of agents to achieve any workflow. A fun case I tried was asking Fable and Astra to mock a presidential debate.
* An agent protocol that abstracts any agent. The key insight here is that every LLM is an agent—instead of treating the LLM as just one node inside an external ReAct loop.Endo was a concept formed while I was building OpenChart (https://github.com/longsurf-ai/openchart). To power trading workflows, I needed to support scenarios where strict determinism is required, while still keeping the flexibility of an agent's inference-time decision-making capability. A new form factor was needed between rigid n8n-style workflows and open-ended ReAct loop agents.Thus the creation of Endo. Endo is short for Endomorphism, a term rooted in category theory and functional programming. An endomorphism is a function that transforms an object into another object of the same type. Similarly, Endo itself is built purely on functional programming principles, relying heavily on Effect (https://github.com/Effect-TS/effect)...And if you have patience to speak technical jargons, Endo is:
* An agent orchestration layer—Higher-Order Harness (HOH)—where an entire agent is treated the same as a single LLM call, enabling arbitrary composition of extremely complex workflows.
* A way to abstract any harness into a standardized protocol, where raw models and agents behave the exact same way, in a KV-cache-friendly manner.
* A workflow engine that enables arbitrary composition of agents with a single workflow language.It's completely open source, and if you think this idea is cool, let's build together. Just for the fun of it.

## 关联链接

- https://github.com/Effect-TS/effect
- https://github.com/longsurf-ai/openchart

## 导航

- 项目页：[[10-项目/github.com_29771baf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
