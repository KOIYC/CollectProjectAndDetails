---
type: "corpus"
item_id: "d5adaa297ed275f8"
title: "Show HN: I built a tool that finds reliability bugs in your code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50280650"
project_url: "https://github.com/dubinc/dub.link/issues/4707"
author: "aray07"
published_at: "2026-10-28T20:45:51Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - hn_show
  - author_aray07
  - story_50280650
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: I built a tool that finds reliability bugs in your code

> [!info] 一句话导读
> Hey HN,I’m Abhishek. I'm building Opslane, a tool that finds reliability issues in your code. On every PR, it spins up your entire app and then tries to find we…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50280650>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：aray07　|　发布：2026-10-28T20:45:51Z
> 项目链接：<https://github.com/dubinc/dub.link/issues/4707>
> 采集：2026-10-29T20:41:52+08:00　|　id：`d5adaa297ed275f8`

## 正文

Hey HN,I’m Abhishek. I'm building Opslane, a tool that finds reliability issues in your code. On every PR, it spins up your entire app and then tries to find weak spots that would break in production.Demo: https://youtu.be/47phxkdh6f0Example: We tested Opslane on Lago (open-source billing) and found a bug where customers get double charged. Opslane made Stripe take the money and then return a 500. Lago marked the payment failed. A retry from the dashboard charged the customer again. https://github.com/getlago/lago-api/issues/6903Why I built thisI used to work on reliability at Robinhood. We used to run chaos testing in our staging environments: inject faults in various parts of the system and see what breaks. We found issues like Kafka or Redis being unavailable for a few seconds could take the whole app down.But that kind of testing was expensive. It needed a well maintained staging environment. Engineers needed to know what to test. Most teams never actually did it.Over the last year, coding agents have gone writing some of my code to almost all my code now. Teams are shipping way more code than they were 6 months ago.Code review tools read the diff, but a lot of reliability bugs aren't in the diff. They're in how your code behaves when Stripe, Redis or the network misbehaves. And e2e tests usually mock those services out and test the happy path.Agents have made this type of testing a lot cheaper. And we will see more of this (kinda like security scanning / testing)How it worksA full copy of your app per PR: Postgres, Redis, Kafka, SQS, S3.Working copies of your third-party dependencies: Stripe, Slack, Gmail and more. Traffic goes through our proxy, which lets us inject failures.The agent picks what to test: It reads every PR and writes down invariants that need to hold (for e.g. a customer should never be charged twice). It then injects faults likely to break the invariants.Bugs we've foundWe ran Opslane on some popular open-source apps and here are some of the bugs we have found:1/ Twenty: deleting a workspace while Stripe is failing locks everyone out, and billing keeps going. Twenty merged a fix. (https://github.com/twentyhq/twenty/issues/28043)2/ Dub: a restart in the middle of a payout paid a partner $240 for $120 owed. (https://github.com/dubinc/dub.link/issues/4707)Full list: opslane.com/open-sourceOpslane is pretty early - we have a couple of early customers. We have found bugs in their system that their other code review tools missed.Would love to get feedback from folks and how they are seeing the reliability of their systems evolve over time with agents.

## 关联链接

- https://github.com/getlago/lago-api/issues/6903Why
- https://github.com/twentyhq/twenty/issues/28043
- https://youtu.be/47phxkdh6f0Example:

## 导航

- 项目页：[[10-项目/github.com_be333b4a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
