---
type: "project"
title: "Show HN: Simurg open-source web search for AI agents that aborts hallucinations"
project_url: "https://github.com/doofzoff/SIMURG"
first_seen: "2026-09-21T03:11:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lebagetdefrance
  - story_49500488
  - show_hn
lang: "en"
---

# Show HN: Simurg open-source web search for AI agents that aborts hallucinations

> [!info] 一句话导读
> Zero-leak online detection of LLM decoding corruption — catch repetition loops, language drift and garbage mid-stream, before the user sees a bad token. Works w…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/doofzoff/SIMURG>
> 首次收录：2026-09-21T03:11:29+08:00
> 来源渠道：HN Show HN
> 标签：author_lebagetdefrance, story_49500488, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/07349f7ec8b0677c_Show-HN-Simurg-open-source-web-search-for-AI-agent]] |
| 2026-09-21T03:11:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/07349f7ec8b0677c_Show-HN-Simurg-open-source-web-search-for-AI-agent]] |

## 摘要正文

# doofzoff/SIMURG  Zero-leak online detection of LLM decoding corruption — catch repetition loops, language drift and garbage mid-stream, before the user sees a bad token. Works with any OpenAI-compatible API.  - Stars: 22 - Forks: 8 - Watchers: 22 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-07-20T19:15:47Z  ## Languages  - HTML - Python  ## Topics  - anomaly-detection - guardrails - hallucination-detection - inference - llm - llm-safety - online-learning - openai-api - streaming - vllm  ## Top Contributors  - doofzoff (10 contributions)  ---  ## README   SIMURG  Streaming Integrity Monitor & Universal Regeneration Guard  Catch LLM decoding corruption while the answer is still being generated and cut the stream mid-flight: corruption that starts in the hold window never reaches the user, and mid-stream corruption is aborted within a few hundred characters of onset, so the host regenerates the answer.  | throughput | detection latency | false-alarm budget | footprint | setup | |:---:|:---:|:---:|:---:|:---:| | **197,632 chars/sec** on a laptop CPU | **~590 chars** past corruption onset | configurable, conformal-calibrated | numpy only, no mo…
