---
type: "corpus"
item_id: "fe639ac33b6fb1be"
title: "Show HN: Simulate 1M+ agents to predict pmf"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50181409"
project_url: "https://github.com/fm882/jahan"
author: "faishalmanzar"
published_at: "2026-10-21T14:16:31Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_faishalmanzar
  - story_50181409
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Simulate 1M+ agents to predict pmf

> [!info] 一句话导读
> Simulate populations of grounded AI personas — social feeds, forums, word of mouth, surveys. Personas are sampled from a real 1M-row dataset, not invented by a …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50181409>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：faishalmanzar　|　发布：2026-10-21T14:16:31Z
> 项目链接：<https://github.com/fm882/jahan>
> 采集：2026-10-22T09:46:18+08:00　|　id：`fe639ac33b6fb1be`

## 正文

# fm882/jahan

Simulate populations of grounded AI personas — social feeds, forums, word of mouth, surveys. Personas are sampled from a real 1M-row dataset, not invented by a prompt.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: Other
- Homepage: https://fm882.github.io/jahan/
- Default branch: master
- Created: 2026-09-10T22:42:24Z

## Languages

- CSS
- Python
- TypeScript

## Top Contributors

- fm882 (764 contributions)

---

## README

# Jahan

**Simulate how a population reacts to your product — and trace every number back to the turn that produced it.**

*Jahan* (جہان) is Urdu for *world*. It builds a population of LLM personas, each grounded in a real survey
respondent, places them on a social network, and lets them meet a product on an X-like feed, a Reddit-like
forum and by word of mouth. They react, talk, change their minds, and answer survey waves about whether they
would buy it.

📖 **Documentation: **

## What makes it different

- **Recorded, not narrated.** Every turn is written to an append-only trace, a tick at a time and whole. Any
 run can be replayed, resumed or audited.
- **Prompts are rebuilt, never stored.** Any turn's exact prompt is reconstructed from the record and shown only
 if it matches the hash taken when the turn ran.
- **Intent is measured, not asked for as a number.** Personas answer in their own words; answers are scored
 with semantic similarity rating against frozen anchor statements.
- **Channels like the real thing.** The feed ranks like X (in-network first, then TwHIN-BERT similarity and
 age), the forum ranks like Reddit (hot), and word of mouth travels along the network's ties.
- **Honest about what it knows.** Every report states its trust level. Today that level is *uncalibrated*,
 and the engine's own holdout found its filled-in attitudes lose to a plain demographic baseline
 (evaluation). The negative results are published
 with the positive ones.

## What's inside

| | |
|---|---|
| `jahan/` | The engine: schemas, brief, population, world, agent, inference, elicitation, runner, trace, analysis, report, web API |
| `frontend/` | A local web interface: define who you study, launch a study, watch its worlds replay, read the report and trace |
| `docs/adr/` | 48 architecture decision records: why the engine works the way it does |
| `docs/prd/` | The specification each module was built from |
| `docs/evaluations/` | Everything measured so far, including what did not work |
| `CONTEXT.md` | The glossary: the words the engine and its docs use |

## Research use and data

Jahan is a research instrument (ADR 0016). The persona corpus it is built around is released for research
only; it is not in this repository, and you download it and accept its terms yourself. Commercial studies
need a population you have the rights to.

## License

Copyright 2026 Faishal Manzar. Source-available under the
Functional Source License 1.1, Apache-2.0 future license: use, modify and run it for any purpose
— including your own commercial studies — except offering it, or something substantially like it, as a
competing product or service. Each release becomes Apache-2.0 two years after it is published.

# HN Timeline | Adrian Krebs

## 评论（1/1）

> **scotbrck** · 2026-10-21T18:02:57.000Z　
> gr8 idea. it will be hella useful if we can predict which products will succeed. btw, what's the guarantee that the simulation will provide the right prediction?

## 关联链接

- https://fm882.github.io/jahan/

## 导航

- 项目页：[[10-项目/github.com_3b07ea40]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
