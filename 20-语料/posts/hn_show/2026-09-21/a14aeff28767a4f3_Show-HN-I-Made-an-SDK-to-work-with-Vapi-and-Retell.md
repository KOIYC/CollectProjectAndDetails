---
type: "corpus"
item_id: "a14aeff28767a4f3"
title: "Show HN: I Made an SDK to work with Vapi and Retell without vendor lock in"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48732064"
project_url: "https://voice-ai.dev/"
author: "marchypolite"
published_at: "2026-06-30T12:54:41Z"
captured_at: "2026-09-21T02:53:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_marchypolite
  - story_48732064
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: I Made an SDK to work with Vapi and Retell without vendor lock in

> [!info] 一句话导读
> Toggle theme Get Started

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48732064>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：marchypolite　|　发布：2026-06-30T12:54:41Z
> 项目链接：<https://voice-ai.dev/>
> 采集：2026-09-21T02:53:06+08:00　|　id：`a14aeff28767a4f3`

## 正文

Voice API Features
 Pricing
 SDK
 Docs
 GitHub
Toggle theme Get Started
Self hostable voice AI API
 Build voice agents you own
 REST first agents, calls, phone numbers, and webhooks, plus a developer dashboard. No vendor lock in.
 Start for free
Agents Calls Call intelligence API & webhooks
Workflow
 From clone to your first call
 Voice API gives you a typed product surface for agents, calls, and phone numbers so you can ship without rebuilding telephony plumbing.
Go live in minutes, not months
 Self host locally, then place a call through the REST API. Inspect outcomes in the operator dashboard.
 Read the docs
$ git clone https://github.com/keyman500/voice-api.git
 Cloning into 'voice-api'...
 cd voice-api && bun install
 cp .env.example .env.local
 bun run db:migrate && bun run dev
 ✓ Voice API at http://localhost:3000
Clone and self host
 Clone the repo, install dependencies, and run the app locally. Same product surface as the hosted dashboard.
create-call.ts
 POST /api/v1/calls
Place a call and review the log
 Create an outbound call with POST /api/v1/calls, then open transcripts, summaries, and outcomes when it finishes.
Bring your own stack. Keep control.
 Connect Twilio with your own keys, choose models on the platform, and hook finished calls into n8n or your own webhooks.
 Explore the API
Calling credentials
 Twilio BYOK
Not configured
Account SID
 AC...
Auth token
 ••••••••
Test config
Model provider
OpenAI Gemini DeepSeek
Bring your own Twilio keys
 Save Twilio Account SID and auth token per account. Pick a model on the platform gateway. Own the telephony path.
Webhooks for finished calls
 Receive structured events when calls complete so automations and operators can act immediately.
Platform
 API first. Operator ready.
 A Vapi and Retell style product surface you can self host. Typed routes, OpenAPI docs, and a control room UI for calls and agents.
Built for builders shipping voice products
 Engineers get a predictable REST API. Operators get readable call detail without drowning in raw JSON.
 Start for free
Clone and host on Vercel
 Clone the repo and deploy to Vercel. Post call jobs run on Workflow, recordings go to Vercel Blob through the files SDK, and the typed /api/v1 surface ships with OpenAPI at https://dashboard.voice-ai.dev/api/openapi.
Dashboard for call ops
 Inspect transcripts, analysis, webhook delivery, and API keys in one place without rebuilding an admin UI.
Setup
 Sign up. Add keys. Place a call.
 Get from zero to a live voice agent with a clear path for developers and operators.
Create account
 Voice API
Sign up
Email
 you@company.com
Create account
Deploy
 Hosted Self host
Create account
 Voice API
Sign up
Email
 you@company.com
Create account
Deploy
 Hosted Self host
Create your account
 Sign up for the hosted app or clone the repo and self host. Same product surface either way.
Calling credentials
 Twilio BYOK
Not configured
Account SID
 AC...
Auth token
 ••••••••
Test config
Model provider
OpenAI Gemini DeepSeek
Connect Twilio
 Save your Twilio Account SID and auth token. Choose a model on the platform. Keep telephony spend under your control.
Outbound call
 POST /api/v1/calls
Ready
Agent
 Select agent
To
 +1...
Place call
Call log
 Waiting for a call…
Ship an agent and take calls
 Create an agent, attach a number, place a call, then review the log and finished call webhook.
Create your account
 Sign up for the hosted app or clone the repo and self host. Same product surface either way.
Connect Twilio
 Save your Twilio Account SID and auth token. Choose a model on the platform. Keep telephony spend under your control.
Ship an agent and take calls
 Create an agent, attach a number, place a call, then review the log and finished call webhook.
Self host free. Host with credits.
 Start on your own infra at no cost. Hosted Starter and Pro plans include Voice AI credits for calls and analysis.
Monthly Annually
Starter
 $29 / month
 Hosted Voice API for getting production calls live
Get Starter
 Everything in Free +
 Hosted dashboard and API
 1,000 Voice AI credits / month
 Agents, calls, and phone numbers
 Finished call webhooks
 API key management
 Post call transcripts and analysis
Pro Popular
 $99 / month
 More included credits for teams running voice at scale
Get Pro
 Everything in Starter +
 5,000 Voice AI credits / month
 Higher usage headroom
 Priority for growing call volume
 Same typed /api/v1 surface
 Finished call webhooks
Free
 $0 / forever
 Read, modify, and self host for free
 View on GitHub
 Get Started today:
 Self host the full platform
 Typed /api/v1 REST surface
 OpenAPI docs
 Bring your own Twilio keys
 Source available license
Frequently Asked Questions
 Answers to common questions about Voice API, licensing, and how it compares to closed voice platforms.
What is Voice API?
Can I self host Voice API?
Do I bring my own Twilio keys?
How do API keys work?
How is this different from Vapi or Retell?
Where are the API docs?
Build on an open voice stack
 Ship voice agents with a typed API, webhooks, and a dashboard you can self host. No vendor lock in.
 Start for free
Product
 Features
 Pricing
Resources
 API Reference
 GitHub
 SDK
Company
 License
 Privacy
© 2026 Voice API . All rights reserved.

## 关联链接

- http://localhost:3000
- https://dashboard.voice-ai.dev/api/openapi.
- https://github.com/keyman500/voice-api.git

## 导航

- 项目页：[[10-项目/voice-ai.dev_18f8a9fb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
