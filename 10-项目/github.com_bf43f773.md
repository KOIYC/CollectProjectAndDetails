---
type: "project"
title: "Show HN: A minimal Pareto-optimal OpenRouter model router for pi, based on Jev"
project_url: "https://github.com/philippdubach/pi-jev-router"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_7777777phil
  - story_49775968
  - show_hn
lang: "en"
---

# Show HN: A minimal Pareto-optimal OpenRouter model router for pi, based on Jev

> [!info] 一句话导读
> philippdubach/pi-jev-router

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/philippdubach/pi-jev-router>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_7777777phil, story_49775968, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/1d17a0385a3f026c_Show-HN-A-minimal-Pareto-optimal-OpenRouter-model]] |

## 摘要正文

# philippdubach/pi-jev-router  A minimal Pareto-optimal OpenRouter model router for pi, based on Jev  - Stars: 14 - Forks: 0 - Watchers: 14 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-09-20T13:55:31Z  ## Languages  - TypeScript  ## Topics  - chief-of-staff - jev - model-router - openrouter - pareto-frontier - pi-coding-agent - pi-package - typesafe  ## Top Contributors  - philippdubach (12 contributions)  ---  ## README  # pi-jev-router: a minimal Pareto-optimal OpenRouter model router for pi, based on Jev  Jev-classified model routing for pi.  ## Model rules  The router ranks the whole OpenRouter catalog for each task. It filters the catalog to models that fit the task, computes a Pareto frontier over quality, cost and latency, then picks the knee point. The knee is the frontier member farthest from the chord that joins the cheapest and dearest models. It needs no weights, so the pick follows the catalog and the recorded evidence on every task. A frontier too small or too flat for a knee falls back to a weighted value function.  Quality blends recorded runs from `eval/results` with the Artificial Analysis index. Writing quality uses the EQ-Bench …
