---
type: "corpus"
item_id: "74ddcfa5e7307506"
title: "Show HN: Recurse – Develop and deploy specialist agents faster"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49850553"
project_url: "https://recurse.run/"
author: "ozankabak"
published_at: "2026-09-25T22:06:03Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_ozankabak
  - story_49850553
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Recurse – Develop and deploy specialist agents faster

> [!info] 一句话导读
> Hi HN! We are looking to gather some feedback on our serverless agent harness. The admittedly not-so-specific use case is to accelerate agent development and de…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49850553>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：ozankabak　|　发布：2026-09-25T22:06:03Z
> 项目链接：<https://recurse.run/>
> 采集：2026-09-26T09:41:08+08:00　|　id：`74ddcfa5e7307506`

## 正文

Hi HN! We are looking to gather some feedback on our serverless agent harness. The admittedly not-so-specific use case is to accelerate agent development and deployment. After building several custom/special-purpose agents for a few customers, we built this to accelerate our workflow at first, and now we are trying to understand whether it could be useful to others.Our driver use case was development of specialist agents with a request/response lifecycle. Think of agents that have a well established input/output contract where they are expected to produce high-quality output (artifacts, responses etc.). Especially when the problem is in some verifiable domain and the LLM can iteratively refine a result to a final value that satisfies constraints or optimizes some goal.The product is a coding agent skill + a serverless execution runtime with a harness that takes in a system prompt + Python functions as tools. The coding agent takes in the requirements from the user, and tries agent variants by executing prompt/tool variants it creates.It works best for cases where you can think of how you can evaluate a candidate agent - when you describe this information to your coding agent, it often does a decent job at building candidate prompts, tools and even benchmarks.Prompts and Python tools that the coding agent creates integrate with a harness that implements an FSM that is tuned to drive an iterative refinement process for verifiable domains. This tuning enables one to use small models like Luna to produce high quality results while keeping costs at a manageable level.Our website is not 100% complete yet (some examples are missing write-ups, not all use cases we tried are there etc.), but the system is operational and docs are there.Thanks!

## 导航

- 项目页：[[10-项目/recurse.run_75fb792c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
