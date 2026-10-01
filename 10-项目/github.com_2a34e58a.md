---
type: "project"
title: "Show HN: Open-source model routing for coding agents at Astra-level performance"
project_url: "https://github.com/weave-os/router"
first_seen: "2026-10-01T09:41:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_adchurch
  - story_49911500
  - show_hn
lang: "en"
---

# Show HN: Open-source model routing for coding agents at Astra-level performance

> [!info] 一句话导读
> A few months ago we started building a model router for coding agents because we thought we could outperform any single model with an ensemble approach. Recentl…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/weave-os/router>
> 首次收录：2026-10-01T09:41:49+08:00
> 来源渠道：HN Show HN
> 标签：author_adchurch, story_49911500, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-01T09:41:49+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-01/b75b2c4e7bd2c7c1_Show-HN-Open-source-model-routing-for-coding-agent]] |

## 摘要正文

A few months ago we started building a model router for coding agents because we thought we could outperform any single model with an ensemble approach. Recently we’ve achieved that milestone and I want to talk about how we did it.First of all, a quick explanation: the Weave Router (https://github.com/weave-os/router) plugs into any coding agent (e.g. Claude Code or Codex) and intelligently switches between LLMs. So, for example, Astra handles tricky debugging or complex system design tasks, and Deepseek v4 Flash handles simple frontend updates.What we’re announcing today is our new routing model, which we’re calling Weave Router 2.0. We benchmarked 2.0 against GPT-6 Astra on Terminal Bench 4.0 and SWE Atlas. On both benchmarks, the router had equivalent pass rates. On Terminal Bench, the router hit 52% of Astra’s cost, and completed tasks 2.2x faster. On SWE Atlas, the router cost 54% as much as Astra and ran 2.5x faster. (Full results on our website at https://weaveos.com/router!)It turns out training a model to route effectively - taking into consideration model capabilities, costs, cache awareness, and more - is a really hard problem! I want to talk about three ways we were abl…
