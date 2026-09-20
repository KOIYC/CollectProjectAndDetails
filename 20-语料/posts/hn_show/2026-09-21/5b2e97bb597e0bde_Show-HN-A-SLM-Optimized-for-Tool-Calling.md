---
type: "corpus"
item_id: "5b2e97bb597e0bde"
title: "Show HN: A SLM Optimized for Tool Calling"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49493085"
project_url: "https://blog.neurometric.ai/p/introducing-a-task-specific-tool"
author: "robmay"
published_at: "2026-08-29T20:28:55Z"
captured_at: "2026-09-21T03:11:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-29"
tags:
  - 语料
  - hn_show
  - author_robmay
  - story_49493085
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: A SLM Optimized for Tool Calling

> [!info] 一句话导读
> Introducing A Task Specific Tool Calling Model - Available on TrustedRouter

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49493085>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：robmay　|　发布：2026-08-29T20:28:55Z
> 项目链接：<https://blog.neurometric.ai/p/introducing-a-task-specific-tool>
> 采集：2026-09-21T03:11:34+08:00　|　id：`5b2e97bb597e0bde`

## 正文

Neurometric Blog
Subscribe Sign in
Introducing A Task Specific Tool Calling Model - Available on TrustedRouter
 When you need fast efficient tool calling
Rob May
 Aug 29, 2026
6
1
Share
Today we’re making our Neurometric tool calling SLM available on TrustedRouter . It does one thing: it turns intent into valid, schema-bound tool calls. It has its own pipeline and harness tuned for that job, and nothing else. Pricing is $0.01 per million input tokens and $0.10 per million output tokens.
 Most teams building agents are paying frontier-model prices for a task that does not need a frontier model. Tool selection is a narrow, highly structured problem. Treating it as one changes the economics of the whole system.
 What you get
Cost reduction on the largest line item. In a running agent, the expensive part is not reasoning. It’s context accumulation: re-sending tool definitions, past tool outputs, and environment state on every single turn. That accounts for 80–90% of agent spend in most architectures. Moving tool selection onto a small, cheap model drops cost per turn by 70–90%, and the effect compounds with every additional turn in a loop.
 Lower latency end to end. Small models deliver much faster time to first token and higher generation throughput. In multi-step agents, 30–40% of wall-clock time disappears into inter-call orchestration overhead rather than useful work. Shortening each hop shortens the entire chain. Users experience this as an agent that feels responsive instead of one that appears to stall between steps.
 Higher schema reliability. A model fine-tuned exclusively on JSON schema adherence produces fewer syntax errors, fewer missing required arguments, and fewer hallucinated parameters than a general-purpose model juggling reasoning, tone, and format compliance in a single pass. Specialization beats breadth here. Fewer malformed calls also means fewer retries, which is a second-order cost and latency win.
 Tighter control over what leaves your perimeter. Tool schemas are a description of your internal systems: database fields, endpoint names, argument semantics. Isolating schema binding in a dedicated small model lets you keep those definitions out of the context you send to a general-purpose provider, and gives you a deployment story that fits inside a VPC or on-prem environment when that matters.
 How to use it
Four patterns cover most of what we’ve seen work.
 Intent router (fast path). Put the model at the entry point of your pipeline. Standard single-turn requests such as “look up user ID 1234” or “fetch local weather” go straight to it, which generates the API payload and executes. Your reasoning model never sees the request. In most production agents, a large majority of turns look like this.
 Planner/executor split. Use a large reasoning model strictly to decompose a complex problem into natural-language sub-goals. Hand each sub-goal to the small model, which converts the instruction into valid arguments and calls the tool. The expensive model does planning, which is what it’s good at. The cheap model does binding, which is what it’s good at.
 Structured output compiler. Let your reasoning model emit its decision as lightweight text rather than strict JSON. Feed that text to the small model to map intent onto schema-bound parameters. This removes a real failure mode, where a reasoning model degrades its own reasoning because it is simultaneously trying to satisfy a format constraint.
 Speculative tool generation. Fire the small model in parallel to predict likely tool calls from the raw user input while your primary model is still drafting its strategy. When the prediction matches, you’ve already paid the latency. At these prices, speculating and discarding is cheap enough to be a rounding error.
 Getting started
The model is live on TrustedRouter now. If you’re already routing through TrustedRouter, you can point tool-calling traffic at it and compare against your current path directly, on your own workloads.
6
1
Share
Discussion about this post
 Comments Restacks
Top Latest Discussions
No posts
Ready for more?
Subscribe
© 2026 neurometric · Privacy ∙ Terms ∙ Collection notice
 Start your Substack Get the app
 Substack is the home for great culture

## 导航

- 项目页：[[10-项目/blog.neurometric.ai_2b79d8a9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
