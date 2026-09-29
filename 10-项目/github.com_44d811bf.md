---
type: "project"
title: "Show HN: Decide – Jev decisions in the shell, scripts, and agent skills"
project_url: "https://github.com/vsekhar/decide"
first_seen: "2026-09-29T09:42:55+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_vsekhar
  - story_49878492
  - show_hn
lang: "en"
---

# Show HN: Decide – Jev decisions in the shell, scripts, and agent skills

> [!info] 一句话导读
> All software makes decisions. Code handles the deterministic ones. Decision models like Jev handle the judgement calls.A decision model takes context and questi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/vsekhar/decide>
> 首次收录：2026-09-29T09:42:55+08:00
> 来源渠道：HN Show HN
> 标签：author_vsekhar, story_49878492, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-29T09:42:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-29/6e7dbc88ad5d933f_Show-HN-Decide-–-Jev-decisions-in-the-shell,-scrip]] |

## 摘要正文

All software makes decisions. Code handles the deterministic ones. Decision models like Jev handle the judgement calls.A decision model takes context and questions with a fixed set of choices, and returns answers with a calibrated probability. No prose, nothing to parse. Decision models are 200x faster and 400x cheaper than LLMs making comparable judgements.I wanted to play around with decision models in more places and without writing code or manually calling APIs. I wanted scripts to read like natural language and agents to be able to pick up the tool and use it after simply reading the help output. brew install vsekhar/tap/decide  decide --set-config --model typesafe:jev-latest --api-key  API key:   decide "Is Atlanta the capital of Georgia?"  yes   # Choose from among options  decide "What kind of weather is typical in Florida?" \  --option rainy \  --option sunny \  --option snowy  sunny   # Provide context (32k context window)  decide --context @ticket.txt \  "Which team handles this ticket?" \  --option shipping \  --option billing \  --option returns  billing   # Pick a level, least to most, explain each to the model  decide --context @ticket.txt \  "How urgent is this tick…
