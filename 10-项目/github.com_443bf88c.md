---
type: "project"
title: "Show HN: Skillroll – pure Markdown evals for any skill using a Dungeon Master"
project_url: "https://github.com/hagaiw/skillroll"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_vafels
  - story_50508503
  - show_hn
lang: "en"
---

# Show HN: Skillroll – pure Markdown evals for any skill using a Dungeon Master

> [!info] 一句话导读
> Maintaining agentic skills alway felt like a chore due to how hard it was to test them.Writing evals is just too complex to do for every small skill,

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/hagaiw/skillroll>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_vafels, story_50508503, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-16/1cb60c17f6e7459a_Show-HN-Skillroll-–-pure-Markdown-evals-for-any-sk]] |

## 摘要正文

Maintaining agentic skills alway felt like a chore due to how hard it was to test them.Writing evals is just too complex to do for every small skill, So I wrote Skillroll - an eval framework that can test any skill using only an eval.mdHow? instead of setting up an intricate eval environment, you write a short world description, run a Dungeon Master agent that simulates that world, and route all tool calls to that agent.each eval.md is a test case with a "world description", "agent prompt and "judgement criteria" for an llm judge to consider when rating pass/fail.I think Skillroll is especially useful for things like fixing skills by writing a failing eval and iterating on the skill until it passes, you can then keep the eval to guard against future regressions and automatically run it in ci. You can also use it to write new evals using TDD-like approach.I found openai's Luna to be a very nice value-for-money option for running the dungeon master, with cost per eval of around $0.003, and support for pretty complex world scenarios.I hope it might help you reduce the friction in writing evals for your own skills
