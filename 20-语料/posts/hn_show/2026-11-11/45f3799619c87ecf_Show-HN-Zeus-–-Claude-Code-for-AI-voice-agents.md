---
type: "corpus"
item_id: "45f3799619c87ecf"
title: "Show HN: Zeus – Claude Code for AI voice agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50445758"
project_url: "https://thunderphone.com/blog/introducing-zeus"
author: "kolchinski"
published_at: "2026-11-10T20:20:03Z"
captured_at: "2026-11-11T13:37:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-11"
pub_day: "2026-11-10"
tags:
  - 语料
  - hn_show
  - author_kolchinski
  - story_50445758
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Zeus – Claude Code for AI voice agents

> [!info] 一句话导读
> Hey, Alex here, I'm one of the founders. We've built phone agents for enterprise customers for two years and kept seeing the same failure: agents that mishear c…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50445758>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：kolchinski　|　发布：2026-11-10T20:20:03Z
> 项目链接：<https://thunderphone.com/blog/introducing-zeus>
> 采集：2026-11-11T13:37:17+08:00　|　id：`45f3799619c87ecf`

## 正文

Hey, Alex here, I'm one of the founders. We've built phone agents for enterprise customers for two years and kept seeing the same failure: agents that mishear callers and then do something confidently wrong.We're announcing two things in this launch. #1 is the stack:
instead of one transcription model → one LLM → one TTS, most conversation turns runs through several transcription models and LLMs (a fast and a slow LLM in the same call, models switched per turn, audio sent straight to an LLM alongside transcripts). That gets us 99.4% on Big Bench Audio. That's the second-highest published score; the only model above us takes almost 9 seconds to start talking as far as we've measured, which doesn't work on a phone call. Eval set and transcripts are on Hugging Face - http://huggingface.co/datasets/kolchinski/bba-storm-eval#2 is Zeus, an agent that configures our voice AI stack per use case and per conversation. We tried doing this with Claude Code and Codex and they were bad at it: they can't run simulated calls out of the box, don't do well with audio input and spotting problems in calls, and tend to blindly believe vendor marketing about which model is best vs actually trying the models. Zeus has evals on real calls, can simulate calls in hard situations, and listens to production calls to find problems, so it can check its own work the way a coding agent runs tests to make sure the code it wrote actually works.Pricing is cost-plus (vendor prices + hosting + a 17–25% margin), no subscription. Zeus is free for now. You can try it with a free $10 credit.Happy to answer questions.

## 关联链接

- http://huggingface.co/datasets/kolchinski/bba-storm-eval#2

## 导航

- 项目页：[[10-项目/thunderphone.com_dbee795b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
