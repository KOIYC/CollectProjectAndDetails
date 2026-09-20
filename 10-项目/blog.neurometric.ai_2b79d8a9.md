---
type: "project"
title: "Show HN: A SLM Optimized for Tool Calling"
project_url: "https://blog.neurometric.ai/p/introducing-a-task-specific-tool"
first_seen: "2026-09-21T03:11:34+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_robmay
  - story_49493085
  - show_hn
lang: "en"
---

# Show HN: A SLM Optimized for Tool Calling

> [!info] 一句话导读
> Introducing A Task Specific Tool Calling Model - Available on TrustedRouter

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://blog.neurometric.ai/p/introducing-a-task-specific-tool>
> 首次收录：2026-09-21T03:11:34+08:00
> 来源渠道：HN Show HN
> 标签：author_robmay, story_49493085, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/5b2e97bb597e0bde_Show-HN-A-SLM-Optimized-for-Tool-Calling]] |
| 2026-09-21T03:11:34+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/5b2e97bb597e0bde_Show-HN-A-SLM-Optimized-for-Tool-Calling]] |

## 摘要正文

Neurometric Blog Subscribe Sign in Introducing A Task Specific Tool Calling Model - Available on TrustedRouter  When you need fast efficient tool calling Rob May  Aug 29, 2026 6 1 Share Today we’re making our Neurometric tool calling SLM available on TrustedRouter . It does one thing: it turns intent into valid, schema-bound tool calls. It has its own pipeline and harness tuned for that job, and nothing else. Pricing is $0.01 per million input tokens and $0.10 per million output tokens.  Most teams building agents are paying frontier-model prices for a task that does not need a frontier model. Tool selection is a narrow, highly structured problem. Treating it as one changes the economics of the whole system.  What you get Cost reduction on the largest line item. In a running agent, the expensive part is not reasoning. It’s context accumulation: re-sending tool definitions, past tool outputs, and environment state on every single turn. That accounts for 80–90% of agent spend in most architectures. Moving tool selection onto a small, cheap model drops cost per turn by 70–90%, and the effect compounds with every additional turn in a loop.  Lower latency end to end. Small models delive…
