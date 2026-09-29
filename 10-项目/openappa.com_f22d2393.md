---
type: "project"
title: "Show HN: OpenAPPA – open-source deterministic guardrails that don't break agents"
project_url: "https://openappa.com/"
first_seen: "2026-09-29T09:42:56+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_motakuk
  - story_49877515
  - show_hn
lang: "en"
---

# Show HN: OpenAPPA – open-source deterministic guardrails that don't break agents

> [!info] 一句话导读
> Hi Hacker News! Matvey, one of the authors, is here.While building enterprise agents, we ran into a problem: the more tools you connect to the AI, the higher th…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://openappa.com/>
> 首次收录：2026-09-29T09:42:56+08:00
> 来源渠道：HN Show HN
> 标签：author_motakuk, story_49877515, show_hn
> 最新指标：点赞=23 · 评论=12 · engagement_velocity=23

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-29T09:42:56+08:00 | HN Show HN | 点赞=23 · 评论=12 · engagement_velocity=23 | [[20-语料/posts/hn_show/2026-09-29/95f8c7aa08184fc6_Show-HN-OpenAPPA-–-open-source-deterministic-guard]] |

## 摘要正文

Hi Hacker News! Matvey, one of the authors, is here.While building enterprise agents, we ran into a problem: the more tools you connect to the AI, the higher the chance it will run out of control and leak sensitive data.Guardrails, in theory, should prevent this, but the situation is worrying: - Non-deterministic guardrails (LLM as a judge, auto modes, etc.) are vulnerable to prompt injections, or they lack knowledge of the data, making them inefficient (~10% data leaks on our benchmarks).  - Existing deterministic guardrails (Cedar, OPA, FIDES, Dogwood) require massive case-specific IF-ELSE-like policies and break agents (~59% utility loss on our benchmarks).We did something differently.We’ve taken the best of existing deterministic guardrails and built a policy language that is data-specific, not use-case specific. It lets you scale agents without updating a policy.On top of that, we’ve added multiple tricks (like a remedy plan or a DualLLM pattern) to help agents operate within those restrictions, raising utility from ~40% to ~90% and making it the first deterministic guardrail that doesn't break agents.Finally, we’ve designed it to be pluggable into any agent loop with pre- and…
