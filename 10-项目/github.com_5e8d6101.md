---
type: "project"
title: "Show HN: Try Free Long-Term Memory for AI 50M-Token Window"
project_url: "https://github.com/corbenicai/galahad"
first_seen: "2026-10-11T09:43:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Corbenic
  - story_50037428
  - show_hn
lang: "en"
---

# Show HN: Try Free Long-Term Memory for AI 50M-Token Window

> [!info] 一句话导读
> Default branch: main

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/corbenicai/galahad>
> 首次收录：2026-10-11T09:43:53+08:00
> 来源渠道：HN Show HN
> 标签：author_Corbenic, story_50037428, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-11T09:43:53+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-11/e5fc749e838a0443_Show-HN-Try-Free-Long-Term-Memory-for-AI-50M-Token]] |

## 摘要正文

# corbenicai/galahad  Galahad by Corbenic  - Stars: 38 - Forks: 4 - Watchers: 38 - Open issues: 1 - Default branch: main - Created: 2026-09-28T12:50:34Z  ## Languages  - HTML  ## Top Contributors  - corbenicai (2 contributions)  ---  ## README   Now live: pip install galahad-kv  ## What is Galahad?  Galahad is the memory layer for AI. A model reads a text once, and Galahad keeps that reading. When the text is needed again, Galahad gives the reading back, so the GPU never reads the same text twice. Galahad also keeps the documents themselves and finds the part a question is about, so the model reads only what matters.  Galahad has a C++ core and runs inside llama.cpp, vLLM and SGLang.  ### Why it matters  - **Don't pay for the same tokens twice.** The tokens a model already processed are  not processed again. Galahad gives the reading back instead of recomputing it.  **99.6%** of tokens came back from memory; **14× faster** on vLLM, **0.59 s** per question. - **Byte-exact, not approximate.** What comes back is identical to what went in: the  model's exact reading, and your documents stored as exact text. No lossy embedding,  no "close enough" like a RAG pipeline. **100/100** right v…
