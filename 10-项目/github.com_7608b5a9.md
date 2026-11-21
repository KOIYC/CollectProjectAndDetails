---
type: "project"
title: "Show HN: Prefixwise 0.12 – a paper and a spec for why prompt caches miss"
project_url: "https://github.com/tejachavali/prefixwise"
first_seen: "2026-11-21T14:45:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tchavali
  - story_50581015
  - show_hn
lang: "en"
---

# Show HN: Prefixwise 0.12 – a paper and a spec for why prompt caches miss

> [!info] 一句话导读
> tejachavali/prefixwise

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tejachavali/prefixwise>
> 首次收录：2026-11-21T14:45:01+08:00
> 来源渠道：HN Show HN
> 标签：author_tchavali, story_50581015, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:45:01+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-21/45d55fe64964b201_Show-HN-Prefixwise-0.12-–-a-paper-and-a-spec-for-w]] |

## 摘要正文

# tejachavali/prefixwise  Model-agnostic ledger of avoidable agent token spend: name why prompt cache misses, price the miss, prove fixes without losing task success.  - Stars: 27 - Forks: 0 - Watchers: 27 - Open issues: 1 - License: MIT License - Default branch: main - Created: 2026-11-06T04:18:24Z  ## Languages  - Dockerfile - Jupyter Notebook - Python - Shell  ## Top Contributors  - tejachavali (146 contributions) - claude (51 contributions)  ---  ## README  # Prefixwise  CI PyPI License: MIT  **Your agent resends its whole conversation every turn, and one changed byte near the top means the provider charges full price for everything after it. Prefixwise tells you which byte, what it cost, and fixes the common causes for you.**  Providers and engines report *how many* tokens missed the prompt cache, not *why*. Prefixwise sits between your agent and the model and does four things:  - **Identify.** One named cause for every request, with its evidence, its cost and its fix. - **Fix.** `--optimize` repairs the request before it is sent. Only fixes that passed a replay against live models. - **Prevent.** `prefixwise check` fails CI when a code change would break the cache. - **Auto-d…
