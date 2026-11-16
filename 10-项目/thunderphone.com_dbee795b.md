---
type: "project"
title: "Show HN: Zeus – Claude Code for AI voice agents"
project_url: "https://thunderphone.com/blog/introducing-zeus"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_kolchinski
  - story_50445758
  - show_hn
lang: "en"
---

# Show HN: Zeus – Claude Code for AI voice agents

> [!info] 一句话导读
> Hey, Alex here, I'm one of the founders. We've built phone agents for enterprise customers for two years and kept seeing the same failure: agents that mishear c…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://thunderphone.com/blog/introducing-zeus>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_kolchinski, story_50445758, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-11/45f3799619c87ecf_Show-HN-Zeus-–-Claude-Code-for-AI-voice-agents]] |

## 摘要正文

Hey, Alex here, I'm one of the founders. We've built phone agents for enterprise customers for two years and kept seeing the same failure: agents that mishear callers and then do something confidently wrong.We're announcing two things in this launch. #1 is the stack: instead of one transcription model → one LLM → one TTS, most conversation turns runs through several transcription models and LLMs (a fast and a slow LLM in the same call, models switched per turn, audio sent straight to an LLM alongside transcripts). That gets us 99.4% on Big Bench Audio. That's the second-highest published score; the only model above us takes almost 9 seconds to start talking as far as we've measured, which doesn't work on a phone call. Eval set and transcripts are on Hugging Face - http://huggingface.co/datasets/kolchinski/bba-storm-eval#2 is Zeus, an agent that configures our voice AI stack per use case and per conversation. We tried doing this with Claude Code and Codex and they were bad at it: they can't run simulated calls out of the box, don't do well with audio input and spotting problems in calls, and tend to blindly believe vendor marketing about which model is best vs actually trying the mo…
