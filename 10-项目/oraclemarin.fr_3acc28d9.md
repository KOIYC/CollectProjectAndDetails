---
type: "project"
title: "Built a free jailbreak/PII detector for AI agents using Jev, runs under 300ms"
project_url: "https://oraclemarin.fr/agent-guard"
first_seen: "2026-09-22T12:54:34+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SaaS
lang: "en"
---

# Built a free jailbreak/PII detector for AI agents using Jev, runs under 300ms

> [!info] 一句话导读
> Everyone building an agent right now is one bad prompt injection away from it doing something it shouldn't. The usual fix is a second call to GPT-4o or Claude t…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://oraclemarin.fr/agent-guard>
> 首次收录：2026-09-22T12:54:34+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SaaS
> 最新指标：得分=3 · 评论=1 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:54:34+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=1 · 赞踩比=1 | [[20-语料/posts/reddit/2026-09-22/cd68ddebd0ab8ffc_Built-a-free-jailbreak-PII-detector-for-AI-agents]] |

## 摘要正文

Everyone building an agent right now is one bad prompt injection away from it doing something it shouldn't. The usual fix is a second call to GPT-4o or Claude to ask "was that safe", which doubles your cost and latency for what's really a yes/no classification.  I built a free API that does that check with Jev instead, the new TypeSafe classification-only model everyone's been talking about this week. No text generation, just probabilities against fixed criteria, so it runs stupidly fast, under 300ms most of the time, for a fraction of a cent per call.  Full disclosure, the landing page HTML is vibecoded, I threw it together fast. The actual work went into the API integration, the quota system, and the Stripe billing behind it.  Free tier is 200 checks/month, no card needed. Rate limited so don't worry about hammering the demo. Curious what breaks it, throw your worst jailbreak attempts at it.  [https://oraclemarin.fr/agent-guard](https://oraclemarin.fr/agent-guard)
