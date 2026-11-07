---
type: "corpus"
item_id: "8d7b452fc755c3c2"
title: "Show HN: Jev vs. OpenAI Decision vs. Small Financial World Models: FinBench [video]"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50394904"
author: "atul-mehra"
published_at: "2026-11-06T16:54:21Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_atul-mehra
  - story_50394904
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jev vs. OpenAI Decision vs. Small Financial World Models: FinBench [video]

> [!info] 一句话导读
> Guys - OpenAI Decisions, Jev, World Models are interesting.We ran some tests for the C-suite to decide between OpenAI Decisions vs. their own existing models vs…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50394904>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：atul-mehra　|　发布：2026-11-06T16:54:21Z
> 项目链接：—
> 采集：2026-11-07T09:43:25+08:00　|　id：`8d7b452fc755c3c2`

## 正文

Guys - OpenAI Decisions, Jev, World Models are interesting.We ran some tests for the C-suite to decide between OpenAI Decisions vs. their own existing models vs. training their proprietary Financial World Model. Sharing the results of our sample tests.If you like a walkthrough with video of results - see this video - https://www.youtube.com/watch?v=UN1LIF01uHQWe are also trying to reach OpenAI team & community to collaborate on running various tests to help the C-suite to make decisions.
Which involves which business cases, they wish to map on which Decision models.Summary: Small Financial World Model compared to OpenAI Decisions.This test is not to build a better model. But to help C-suites make informed choices. There are various considerations vizLatency
Cost per decision
On-premises or Hosted APIs
Regulatory & Compliance
Mapping to use cases
Financial modelling or LLM-based reasoning as underlying architecture
We ran tests to:Predict credit defaults
Cross-sell propensity
Churn Risk
Future cash flows
Future state of customers & causal impacts of interventions like no-action, Payment reminders etc.These tests are specific to banking use cases.Why Benchmark & comparison:Small on-prem Decision Models are needed due to latency, cost, regulatory or protecting the proprietary data for Enterprises.This benchmarking helps C-suite executives to decide which option - their in-house models or other options are better. Vaayu FinBench also includes some specific banking-related business cases as examples.World Model also has action-conditioning. Thus, it predicts which decision optimizes the future outcomes. Eg Risk weighted return or prevent default. Core ask from BanksSmall Financial World Model is trained on-premesis on proprietary data for enterprises.Scope - This is only for demonstration purposes to give a glimpse of how to compare various options. The dataset & model size is way too small yet. On a larger proprietary dataset, the results need to be benchmarked.Results:
Latency - A co-located Small Financial World Model way improves latency. Major part may be coming due to network latency. So this is one area where we would like to discuss alternatives with OpenAI team & community. Is there a smaller on-premesis version for Decision Model avaialble for co-location.Credit Defaults - Our Small Financial World model worked worse than Decision API.Cash Churn & Cross Sell propensity - Our Small Financial World model improved marginally. It’s obvious that since Decision API hasnt seen the propreitary data. The marginal improvement shows model is learning..but our model is very very small (Few 100 thousand parameters) trained on small dataset.. But test demonstrates - architecture is capable of learning better.Action conditions outcomes - This is available in World Model …but we aren’t aware of this in Decision API yet.Financial Modelling - Model is trained finance native can handle temporal & causal scenariosIf you like a walkthrough - see this video - https://www.youtube.com/watch?v=UN1LIF01uHQDisclaimer: This is quick tests results & has some know issues. This is only for demonstration purpose. We have included OpenAI Decisions for now...Including Jev in next releases. At the moment talking to C-suite & Banks for what they wish.We find Decision API & World Models interesting developments especially in finance & enterprises space. Looking forward to collaborate with OpenAI team & community how to enable C-suite to make choices…which are underway right now at enterprises.

## 关联链接

- https://www.youtube.com/watch?v=UN1LIF01uHQDisclaimer:
- https://www.youtube.com/watch?v=UN1LIF01uHQWe

## 导航

- 项目页：[[10-项目/Show-HN-Jev-vs.-OpenAI-Decision-vs.-Small-Financ_8d7b452f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
