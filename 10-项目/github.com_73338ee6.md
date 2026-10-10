---
type: "project"
title: "Show HN: CPU First Decision Model"
project_url: "https://github.com/kouhxp/gutsy"
first_seen: "2026-10-10T09:53:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mrkn1
  - story_50023015
  - show_hn
lang: "en"
---

# Show HN: CPU First Decision Model

> [!info] 一句话导读
> Local decision model with calibrated probabilities: send a state and yes/no, choice or score questions, get a probability for every option. 0.8B GGUF on CPU, Je…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/kouhxp/gutsy>
> 首次收录：2026-10-10T09:53:50+08:00
> 来源渠道：HN Show HN
> 标签：author_mrkn1, story_50023015, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-10T09:53:50+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-10/20db7b069804b4da_Show-HN-CPU-First-Decision-Model]] |

## 摘要正文

# kouhxp/gutsy  Local decision model with calibrated probabilities: send a state and yes/no, choice or score questions, get a probability for every option. 0.8B GGUF on CPU, Jev-style API.  - Stars: 71 - Forks: 2 - Watchers: 71 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-10-01T15:42:10Z  ## Languages  - HTML - Python  ## Topics  - agents - classifier - content-moderation - cpu-inference - decision-model - gguf - intent-classification - jev - jev-compatible - llama-cpp - llm - llm-judge - local-llm - python - qwen - routing - small-language-models - tool-selection  ## Top Contributors  - kouhxp (4 contributions)  ---  ## README  **Local decision models with calibrated probabilities.** Send a state (text or JSON) and typed questions (yes/no, choice, score); get a probability for every option back. No text generation, no network calls, no per-call cost. The API follows the Jev-style Decisions format, so existing clients mostly need only a new base URL.  | | | |---|---| | Model | `gutsy-0.8b` v0.4, a fine-tune of Qwen3.5-0.8B: Q8_0 (775 MB) or Q4_K_M (505 MB, 25-30% faster), on Hugging Face | | Runtime | `gutsy-inference`, llama.cpp on an ordin…
