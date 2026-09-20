---
type: "project"
title: "Show HN: Llmbridge, a C++ LLM gateway with sub-millisecond overhead"
project_url: "https://github.com/kottos-ai/llmbridge"
first_seen: "2026-09-20T09:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lluisantoni
  - story_49712158
  - show_hn
lang: "en"
---

# Show HN: Llmbridge, a C++ LLM gateway with sub-millisecond overhead

> [!info] 一句话导读
> A sub-millisecond, drop-in OpenAI-compatible LLM gateway in C++

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/kottos-ai/llmbridge>
> 首次收录：2026-09-20T09:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_lluisantoni, story_49712158, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/dae5178a37b35e58_Show-HN-Llmbridge,-a-C++-LLM-gateway-with-sub-mill]] |
| 2026-09-20T09:37:17+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/dae5178a37b35e58_Show-HN-Llmbridge,-a-C++-LLM-gateway-with-sub-mill]] |

## 摘要正文

# kottos-ai/llmbridge  A sub-millisecond, drop-in OpenAI-compatible LLM gateway in C++  - Stars: 5 - Forks: 1 - Watchers: 5 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://kottos.ai - Default branch: master - Created: 2026-05-27T20:53:54Z  ## Languages  - C++ - CMake - Dockerfile - Python - Shell  ## Topics  - ai-gateway - ai-infrastructure - anthropic - api-gateway - cohere - cpp - cpp20 - gemini - inference - llm - llm-gateway - low-latency - openai - proxy  ## Top Contributors  - kottos-ai (29 contributions) - lluisantoni (1 contributions)  ---  ## README  # llmbridge  > A sub-millisecond, drop-in OpenAI-compatible **LLM gateway** in C++. Microsecond translation overhead, dependency-free default build (TLS uses OpenSSL), p99 < 1 ms at 1,000 RPS.  License: Apache 2.0 C++20 Build Status  ## What it does  `llmbridge` is a **sub-millisecond LLM gateway**. It sits between your app and a model provider: clients speak the **OpenAI** API to it, and it translates each request to the upstream provider's dialect (Anthropic, Gemini, Cohere, ...) and the response back, adding **microseconds, not milliseconds**. Run it as a standalone binary, or embed the translation calls …
