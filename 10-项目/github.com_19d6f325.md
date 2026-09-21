---
type: "project"
title: "Show HN: jevals – replacing LLM judges with typed Jev decisions"
project_url: "https://github.com/openlayer-ai/jevals"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_gbayomi
  - story_49780849
  - show_hn
lang: "en"
---

# Show HN: jevals – replacing LLM judges with typed Jev decisions

> [!info] 一句话导读
> Agent evals and guardrails in one request. Built on Jev, Kev and Laya.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/openlayer-ai/jevals>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_gbayomi, story_49780849, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/cd91275c999557e8_Show-HN-jevals-–-replacing-LLM-judges-with-typed-J]] |

## 摘要正文

# openlayer-ai/jevals  Agent evals and guardrails in one request. Built on Jev, Kev and Laya.  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: MIT License - Homepage: https://github.com/openlayer-ai/jevals - Default branch: main - Created: 2026-09-20T19:56:13Z  ## Languages  - Python  ## Topics  - agents - evals - guardrails - jev - llm - llm-evaluation - ragas - typesafe  ## Top Contributors  - gbayomi (9 contributions)  ---  ## README  # jevals  Evals and guardrails for agents, using Jev-style decision models instead of an LLM judge. All the evals for a trace go out as one request that costs a few thousandths of a cent and comes back in a few hundred milliseconds, so you can run them on every trace and inside the agent loop.  Works with Jev through the TypeSafe or Vercel APIs, with Kev or Laya running locally on a Mac, or with a regular chat LLM if that's all you have (slower, costs more).  ```bash pip install jevals export AI_GATEWAY_API_KEY=...      # Jev through Vercel AI Gateway. TYPESAFE_API_KEY and OPENROUTER_API_KEY also work. ```  ```python from jevals import evaluate from jevals.agent import ToolChoice, UsedToolResult, Grounded, StayedInScope from jevals.…
