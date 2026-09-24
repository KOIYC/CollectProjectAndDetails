---
type: "corpus"
item_id: "cd68ddebd0ab8ffc"
title: "Built a free jailbreak/PII detector for AI agents using Jev, runs under 300ms"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wk679v/built_a_free_jailbreakpii_detector_for_ai_agents/"
project_url: "https://oraclemarin.fr/agent-guard"
author: "Zboubkiller"
published_at: "2026-09-19T07:40:47+08:00"
captured_at: "2026-09-22T12:54:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 3, "comments": 1, "upvote_ratio": 1}
comments_count: 0
comments_total: 1
discovered_via: "reddit:7d+settle3"
---

# Built a free jailbreak/PII detector for AI agents using Jev, runs under 300ms

> [!info] 一句话导读
> Everyone building an agent right now is one bad prompt injection away from it doing something it shouldn't. The usual fix is a second call to GPT-4o or Claude t…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wk679v/built_a_free_jailbreakpii_detector_for_ai_agents/>
> 指标：得分=3 · 评论=1 · 赞踩比=1
> 作者：Zboubkiller　|　发布：2026-09-19T07:40:47+08:00
> 项目链接：<https://oraclemarin.fr/agent-guard>
> 采集：2026-09-22T12:54:34+08:00　|　id：`cd68ddebd0ab8ffc`

## 正文

Everyone building an agent right now is one bad prompt injection away from it doing something it shouldn't. The usual fix is a second call to GPT-4o or Claude to ask "was that safe", which doubles your cost and latency for what's really a yes/no classification.

I built a free API that does that check with Jev instead, the new TypeSafe classification-only model everyone's been talking about this week. No text generation, just probabilities against fixed criteria, so it runs stupidly fast, under 300ms most of the time, for a fraction of a cent per call.

Full disclosure, the landing page HTML is vibecoded, I threw it together fast. The actual work went into the API integration, the quota system, and the Stripe billing behind it.

Free tier is 200 checks/month, no card needed. Rate limited so don't worry about hammering the demo. Curious what breaks it, throw your worst jailbreak attempts at it.

[https://oraclemarin.fr/agent-guard](https://oraclemarin.fr/agent-guard)

## 导航

- 项目页：[[10-项目/oraclemarin.fr_3acc28d9]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
