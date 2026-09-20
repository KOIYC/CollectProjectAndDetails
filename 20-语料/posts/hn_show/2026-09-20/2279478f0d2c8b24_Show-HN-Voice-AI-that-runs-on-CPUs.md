---
type: "corpus"
item_id: "2279478f0d2c8b24"
title: "Show HN: Voice AI that runs on CPUs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49714400"
project_url: "https://lokutor.com/"
author: "lokutor"
published_at: "2026-09-15T15:49:45Z"
captured_at: "2026-09-20T14:06:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_lokutor
  - story_49714400
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: Voice AI that runs on CPUs

> [!info] 一句话导读
> Lokutor

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49714400>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：lokutor　|　发布：2026-09-15T15:49:45Z
> 项目链接：<https://lokutor.com/>
> 采集：2026-09-20T14:06:06+08:00　|　id：`2279478f0d2c8b24`

## 正文

Author: Lokutor

Lokutor | Full-Stack Voice AI on CPU

# The first CPU based Voice AI.

Every model - turn-taking, STT, LLM, and TTS - trained from scratch and optimized for commodity CPUs. No GPU dependency. Sub-450ms end-to-end.

0 ms

01

## The Only CPU-First Voice AI

Most voice AI platforms follow the same recipe: stitch together a STT API from one provider, an LLM from another, a TTS from a third - each running on expensive NVIDIA GPUs, each adding 200–300ms of network latency. The result is a fragile cascade that costs too much and feels unnatural.

We took a different approach. Every model - Vela (turn-taking), Psst (noise suppression), our fine-tuned LLM, STT, and Versa (TTS) - is trained from scratch and hand-optimized for ARM and x86 CPUs. No GPU overhead. No third-party dependencies. Full control over quality and latency.

The same cascade architecture, rebuilt model by model for maximum efficiency. Sub-450ms on a standard server.

Our models are trained on MareNostrum 5, one of Europe's most powerful supercomputers, through the Barcelona Supercomputing Center AI Factory program. We work closely with NVIDIA (Inception partner) and AWS to push CPU-based inference to its limit. This is European deep tech - building voice AI infrastructure from the ground up.

### Real-World Applications

 1 Customer Training • 2 Corporate Formation • 3 Sales Conversations • 4 Support Interactions

 [instructive tone] Okay, let's walk through the new dashboard interface together. Whenever you're ready, click Start Module and I'll explain each section as we go.

 [welcoming tone] Welcome to the team. Our onboarding syllabus will guide you through the initial setup, HR policies, and an introduction to our cultural values. Let's begin.

 [confident tone] Hi there. I noticed you were exploring our enterprise plans. I'd love to show you how our custom solution can significantly increase your conversion rates.

 [empathetic tone] I'm so sorry to hear you are experiencing issues with your account. Let me pull up your details right away, and we will get this sorted out for you.

## Developer First

Integrate Lokutor in minutes with our SDKs and comprehensive documentation.

```
import { VoiceAgentClient, VoiceStyle, Language } from '@lokutor/sdk';

const client = new VoiceAgentClient({
  apiKey: 'your-key',
  prompt: 'You are a helpful and friendly AI assistant.',
  voice: VoiceStyle.F1,
  language: Language.ENGLISH,
  visemes: true,
});

client.on('transcription', (text) => console.log('You:', text));
client.on('response', (text) => console.log('Agent:', text));
client.on('visemes', (visemes) => animateMouth(visemes));
client.on('status', (status) => console.log('Status:', status));

await client.startManaged();
```

```
from lokutor import VoiceAgentClient, VoiceStyle, Language
import os

client = VoiceAgentClient(
    api_key=os.environ['LOKUTOR_API_KEY'],
    prompt='You are a helpful and friendly AI assistant.',
    voice=VoiceStyle.F1,
    language=Language.ENGLISH,
)

@client.on('transcription')
def on_transcription(text):
    print(f"You: {text}")

@client.on('response')
def on_response(text):
    print(f"Agent: {text}")

@client.on('status')
def on_status(status):
    print(f"Status: {status}")

client.start_conversation()
```

#### Native SDKs

JavaScript • Python

#### Open Source

Go-based Voice Orchestrator

# Show HN: Eulix - Code navigation for large codebases | Hacker News

## 评论（1/1）

> **iharnoor** · 2026-09-18T22:17:09.000Z　
> what's the biggest advantage here?

## 导航

- 项目页：[[10-项目/lokutor.com_f09354b1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
