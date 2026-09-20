---
type: "project"
title: "Show HN: Padwan-LLM, a lightweight LLM Python client"
project_url: "https://github.com/polarsen-io/padwan-llm"
first_seen: "2026-09-20T09:36:58+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Orelus
  - story_49731552
  - show_hn
lang: "en"
---

# Show HN: Padwan-LLM, a lightweight LLM Python client

> [!info] 一句话导读
> polarsen-io/padwan-llm

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/polarsen-io/padwan-llm>
> 首次收录：2026-09-20T09:36:58+08:00
> 来源渠道：HN Show HN
> 标签：author_Orelus, story_49731552, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/d2cf7d6fcba0d3b1_Show-HN-Padwan-LLM,-a-lightweight-LLM-Python-clien]] |
| 2026-09-20T09:36:58+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/d2cf7d6fcba0d3b1_Show-HN-Padwan-LLM,-a-lightweight-LLM-Python-clien]] |

## 摘要正文

# polarsen-io/padwan-llm  Minimal, provider-agnostic Python client for large language models, built on niquests.  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 1 - License: MIT License - Homepage: https://polarsen-io.github.io/padwan-llm/ - Default branch: master - Created: 2026-02-14T21:40:56Z  ## Languages  - Just - Python - Shell  ## Topics  - agent - gemini - grok - http2 - llm - mcp - mistral - niquests - openai - python3  ## Top Contributors  - Andarius (63 contributions) - Polarsen-bot (20 contributions)  ---  ## README   Padwan LLM  Lightweight, unified async client for OpenAI, Gemini, Mistral, Grok, Anthropic, and any OpenAI-compatible API. Single runtime dependency (niquests), automatic HTTP/2 and HTTP/3 negotiation.  For the full interactive CLI/TUI, use the separate `padwan-cli` package.  ## Installation  ```bash pip install padwan-llm ```  ## Library Usage  ### One-shot chat  ```python from padwan_llm import LLMClient  async with LLMClient(model="gpt-4o") as client:     response, usage = await client.complete_chat(         [{"role": "user", "content": "Hello!"}]     )     print(response["content"]) ```  ### Streaming with `ConversationState`  ```python from padwan…
