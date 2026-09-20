---
type: "corpus"
item_id: "ca431c37ab049e94"
title: "Show HN: AI Security Breaches, the problems and it's causes"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49123905"
project_url: "https://raylinement.substack.com/p/ai-security-breaches-the-problems"
author: "rzwsan"
published_at: "2026-07-31T14:49:54Z"
captured_at: "2026-09-21T03:11:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_rzwsan
  - story_49123905
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: AI Security Breaches, the problems and it's causes

> [!info] 一句话导读
> Published: 2026-07-31

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49123905>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rzwsan　|　发布：2026-07-31T14:49:54Z
> 项目链接：<https://raylinement.substack.com/p/ai-security-breaches-the-problems>
> 采集：2026-09-21T03:11:06+08:00　|　id：`ca431c37ab049e94`

## 正文

Published: 2026-07-31
Author: Raylinement

AI Security Breaches, the problems and it's causes

# AI Security Breaches, the problems and it's causes

Raylinement

Jul 31, 2026

https://images.metmuseum.org/CRDImages/gr/original/DP141474.jpg

There has been a recent security breaches by Anthropic and OpenAI that they have problems in difficulty in working and handling with these advance AI models.

The first one is Anthropic incident “capture the flag”. It’s three of it’s model Claude Opus 4.7, Claude Mythos 5 and an internal research model. It happened during the “capture the flag” exercises where models were tasked with finding hidden information in simulated networks. Although the models told that they had no internet access. But an “operational failure” evaluation partner left them connected to the public web.

The models exploited weak passwords and unauthenticated endpoints to gain access. In one instance, a model was given a fictional target name that happen to match a real business. The model somewhat make itself believe in the thought of that the real world data it found must have been part of the simulation.

These incidents date back as April 2024 and occurred in environment intentionally lacking safeguards so Anthropic could text model limits. Anthropic then suspended all cyber evaluations on July 23, 2026 and then later make sure to inform the affected company on July 27.

The another case is OpenAI breach which is more towards autonomous behavior. An autonomous AI agent independently exploited a novel vulnerability to reach the internet during testing. Then it launched a “rogue attack” on the company “Hugging Face”, which caused a dayslong hacking spree. OpenAI did not catch the attack until after the threat was contained. The FBI was subsequently informed of the breach.

Now after reading these two incidents we can already see some patterns which is heavily similar to one or another. Some of them are:

1. Both cases is the inability of developers to keep the capabilities of their models contained. Even though being the top companies in this industry they faces incidents where AI acted beyond something they could have predicted.
2. These incidents happened when they intentionally lacked safeguards, while they have good reasons for that to actually test their models capabilities.
3. Rationalization and justify their action itself. These models rationalize it’s action and then justify it as well for breaking rules.

Most of the time the AI models itself have a different way to going through process of working than their developers actually developed for.

1. Capabilities are mostly non-linear. Developers think that Version N -> it’s somewhat better than Version N-1. But how actually the models uses reasoning + tool uses + long context and those various formation creates unexpected strategy formation and that’s create entirely new behaviors. This is called “Emergent Behavior”.
2. Context misidentification. Models doesn’t have a clear understanding or the ability to evaluate based on morality and ethics and what it is wrong or right. They infer it statistically, models are rewarded for achieving goal so they go the highest possible win rate objective to work around that, humans expect works on certainty but models work from probabilities.

#### Discussion about this post

## 关联链接

- https://images.metmuseum.org/CRDImages/gr/original/DP141474.jpg

## 导航

- 项目页：[[10-项目/raylinement.substack.com_20327342]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
