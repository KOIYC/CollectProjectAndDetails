---
type: "corpus"
item_id: "703d9761a49a7f85"
title: "Show HN: VernLLM – LLM fallback, no gateway"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49791930"
project_url: "https://vernllm.dev/"
author: "Buddo"
published_at: "2026-09-21T19:13:37Z"
captured_at: "2026-09-22T12:53:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_Buddo
  - story_49791930
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: VernLLM – LLM fallback, no gateway

> [!info] 一句话导读
> The LLM call framework. Resilience, observability, and control for every call. Retry budgets, provider fallback, rate limiting, circuit breaking and more, depen…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49791930>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Buddo　|　发布：2026-09-21T19:13:37Z
> 项目链接：<https://vernllm.dev/>
> 采集：2026-09-22T12:53:31+08:00　|　id：`703d9761a49a7f85`

## 正文

VernLLM
 Get Started
 Features
 Customization
 Adapters
 Search ⌘ K
Reliable LLM calls,
by default.
 The LLM call framework. Resilience, observability, and control for every call. Retry budgets, provider fallback, rate limiting, circuit breaking and more, dependency-light and typed from the start.
Read the docs Source
$ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm
 $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm $ npm install vern-llm $ pnpm add vern-llm $ yarn add vern-llm $ bun add vern-llm
index.ts
import Anthropic from '@anthropic-ai/sdk' ;
 import OpenAI from 'openai' ;
 import { fromAnthropic , fromOpenAI , VernLLM } from 'vern-llm' ;
const openai = fromOpenAI ( new OpenAI ({ apiKey : process . env . OPENAI_API_KEY }));
 const anthropic = fromAnthropic ( new Anthropic ({ apiKey : process . env . ANTHROPIC_API_KEY }));
export const llm = new VernLLM ({
 client : openai ,
 model : 'gpt-4o' ,
 fallback : { client : anthropic , model : 'claude-sonnet-5' , circuitBreaker : true } ,
 rateLimit : { requestsPerMinute : 500 , tokensPerMinute : 100_000 , maxConcurrent : 20 } ,
 retryBudget : { windowMs : 60_000 , minCalls : 20 , retryRatio : 0.2 } ,
 maxRetries : 3 ,
 timeoutMs : 10_000 ,
 defaultMaxTokens : 1000 ,
 defaultReasoningEffort : 'medium'
 });
const result = await llm .cachedCall ({
 cacheKey : 'weather:new-york' ,
 ttl : 3600 ,
 call : { userContent : "What's the weather in New York?" }
 });
What this call actually does.
 fallback: → Falls over to a backup target on failure, in process
 circuitBreaker: true → Stops repeated failures from cascading
 rateLimit: → Queues locally under a per-minute ceiling
 retryBudget: → Caps how much recent traffic can be retries
 maxRetries: 3 → Retries transient failures with backoff and jitter
 timeoutMs: 10_000 → Prevents attempts from hanging indefinitely
 defaultMaxTokens: 1000 → Applied to any call that omits its own
 defaultReasoningEffort: 'medium' → Sets reasoning depth across providers
 cachedCall → Returns cached results without another API call
Works with OpenAI Anthropic Gemini Groq Mistral DeepSeek Cerebras Together AI Fireworks AI Ollama OpenRouter Perplexity DeepInfra Novita Hyperbolic Moonshot (Kimi) Zhipu (GLM) LM Studio vLLM xAI (Grok) NVIDIA NIM Vercel AI Gateway Cloudflare Workers AI Nebius AI Studio SambaNova Cloud Baseten Featherless AI Friendli AI SiliconFlow Parasail StepFun MiniMax Lambda Labs Snowflake Cortex Anyscale Lepton AI Inference.net Infermatic AtlasCloud 01.AI (Yi) AWS Bedrock Custom HTTPS API
What problem does VernLLM solve? LLM calls fail in ways plain SDK calls do not handle: timeouts, rate limit errors, a provider having an outage, or a request that just hangs. VernLLM adds retries with backoff, a circuit breaker, provider fallback, rate limiting, and caching around your existing client, so a single bad call does not take down your app.
Why use VernLLM instead of a gateway? VernLLM runs in your own process, so there is no extra network hop or proxy to maintain. It is built around small interfaces rather than one config object, so caching, rate limiting, and the circuit breaker can each be swapped for your own implementation. Running in-process also means it can react to your own application logic, not just the request and response, catching failures a gateway watching traffic from outside your app would miss. A gateway is still the better choice for one shared setup across many services or languages.
Why use VernLLM instead of calling the client directly? Calling the client directly means you own retries, timeouts, circuit breaking, and caching yourself, code most teams end up rewriting per project. VernLLM ships those as configurable options on one class, so you keep your existing provider client and wrap it instead of reimplementing the resilience layer.
Can I bring my own cache backend? Yes. cachedCall accepts any adapter implementing get/set (delete is optional), so Redis, a database, or a custom store can replace the built-in in-memory cache without changing how you call it.
Can I hook into or modify requests before they go out? Yes, through middleware. transform edits or redacts an outgoing request before it is sent, and wrap runs around a whole logical call, retries and fallback attempts included, for logging, tracing, or cost tracking.
Is it typed? Yes, written in TypeScript from the ground up. Structured output schemas, call params, and errors are all typed, so mistakes surface at compile time instead of at runtime.
How many dependencies does it add to my project? Zero runtime dependencies. VernLLM does not bundle Zod or provider SDKs, it relies on compatible interfaces instead, so you bring your own provider clients and schema validators while keeping your dependency tree minimal.
Stop reinventing the call layer.
 Get started Source
 npm install vern-llm

## 导航

- 项目页：[[10-项目/vernllm.dev_ff11f727]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
