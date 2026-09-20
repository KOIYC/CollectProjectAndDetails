---
type: "project"
title: "Show HN: Khazad – Transparent Semantic Cache for LLM Calls on Redis Vector Sets"
project_url: "https://github.com/GuglielmoCerri/khazad"
first_seen: "2026-09-21T03:11:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_guglielmoce
  - story_48725166
  - show_hn
lang: "en"
---

# Show HN: Khazad – Transparent Semantic Cache for LLM Calls on Redis Vector Sets

> [!info] 一句话导读
> GuglielmoCerri/khazad

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/GuglielmoCerri/khazad>
> 首次收录：2026-09-21T03:11:03+08:00
> 来源渠道：HN Show HN
> 标签：author_guglielmoce, story_48725166, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/ba0a3f22c9012cda_Show-HN-Khazad-–-Transparent-Semantic-Cache-for-LL]] |
| 2026-09-21T03:11:03+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/ba0a3f22c9012cda_Show-HN-Khazad-–-Transparent-Semantic-Cache-for-LL]] |

## 摘要正文

# GuglielmoCerri/khazad  Transparent, transport-layer semantic cache for LLM API calls, powered by Redis 8 Vector Sets.  - Stars: 33 - Forks: 2 - Watchers: 33 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-06-13T15:20:47Z  ## Languages  - Python  ## Topics  - anthropic - embeddings - gemini - llm - openai - python - redis - semantic-cache - vector-search  ## Top Contributors  - GuglielmoCerri (35 contributions)  ---  ## README   Khazad — You shall not pass.  Python 3.10+ License: MIT PyPI Redis 8  *Transparent, transport-layer semantic cache for LLM API calls powered by Redis Vector Sets.*  ``` $ uv run --group examples python -P examples/openai.py   [Khazad] HTTP transport patches installed   [Khazad] Initialized — threshold=0.90, embedder=huggingface   [Khazad] Cache flushed   [Khazad] Loading embedding model: redis/langcache-embed-v2   Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.   Loading weights: 100%|████████████████████████████████████████████████| 134/134 [00:00<00:00, 10758.95it/s]   [Khazad] CACHE MISS - Forwarding to API   [call 1] 7918.4ms — The c…
