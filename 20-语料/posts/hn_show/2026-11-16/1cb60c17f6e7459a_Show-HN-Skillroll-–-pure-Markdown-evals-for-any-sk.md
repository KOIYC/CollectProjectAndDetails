---
type: "corpus"
item_id: "1cb60c17f6e7459a"
title: "Show HN: Skillroll – pure Markdown evals for any skill using a Dungeon Master"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50508503"
project_url: "https://github.com/hagaiw/skillroll"
author: "vafels"
published_at: "2026-11-15T17:01:21Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_vafels
  - story_50508503
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Skillroll – pure Markdown evals for any skill using a Dungeon Master

> [!info] 一句话导读
> Maintaining agentic skills alway felt like a chore due to how hard it was to test them.Writing evals is just too complex to do for every small skill,

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50508503>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：vafels　|　发布：2026-11-15T17:01:21Z
> 项目链接：<https://github.com/hagaiw/skillroll>
> 采集：2026-11-16T10:00:05+08:00　|　id：`1cb60c17f6e7459a`

## 正文

Maintaining agentic skills alway felt like a chore due to how hard it was to test them.Writing evals is just too complex to do for every small skill,
So I wrote Skillroll - an eval framework that can test any skill using only an eval.mdHow? instead of setting up an intricate eval environment, you write a short world description, run a Dungeon Master agent that simulates that world, and route all tool calls to that agent.each eval.md is a test case with a "world description", "agent prompt and "judgement criteria" for an llm judge to consider when rating pass/fail.I think Skillroll is especially useful for things like fixing skills by writing a failing eval and iterating on the skill until it passes,
you can then keep the eval to guard against future regressions and automatically run it in ci.
You can also use it to write new evals using TDD-like approach.I found openai's Luna to be a very nice value-for-money option for running the dungeon master, with cost per eval of around $0.003, and support for pretty complex world scenarios.I hope it might help you reduce the friction in writing evals for your own skills

## 导航

- 项目页：[[10-项目/github.com_443bf88c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
