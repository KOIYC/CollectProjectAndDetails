---
type: "project"
title: "Show HN: VernLLM – LLM fallback, no gateway"
project_url: "https://vernllm.dev/"
first_seen: "2026-09-22T12:53:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Buddo
  - story_49791930
  - show_hn
lang: "en"
---

# Show HN: VernLLM – LLM fallback, no gateway

> [!info] 一句话导读
> The LLM call framework. Resilience, observability, and control for every call. Retry budgets, provider fallback, rate limiting, circuit breaking and more, depen…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://vernllm.dev/>
> 首次收录：2026-09-22T12:53:31+08:00
> 来源渠道：HN Show HN
> 标签：author_Buddo, story_49791930, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-22/703d9761a49a7f85_Show-HN-VernLLM-–-LLM-fallback,-no-gateway]] |

## 摘要正文

VernLLM  Get Started  Features  Customization  Adapters  Search ⌘ K Reliable LLM calls, by default.  The LLM call framework. Resilience, observability, and control for every call. Retry budgets, provider fallback, rate limiting, circuit breaking and more, dependency-light and typed from the start. Read the docs Source $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm  $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm index.ts import Anthropic from '@anthropic-ai/sdk' ;  import OpenAI from 'openai' ;  import { fromAnthropic , fromOpenAI , VernLLM } from 'vern-llm' ; const openai = fromOpenAI ( new OpenAI ({ apiKey : process . env . OPENA…
