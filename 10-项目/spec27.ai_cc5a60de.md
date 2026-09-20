---
type: "project"
title: "Show HN: Spec27 – Spec-driven validation for AI agents"
project_url: "https://spec27.ai/launch"
first_seen: "2026-09-21T01:41:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_njyx
  - story_47959984
  - show_hn
lang: "en"
---

# Show HN: Spec27 – Spec-driven validation for AI agents

> [!info] 一句话导读
> Hi HN! We’re a team of ML validation specialists and we’ve been building /Spec27, a tool for testing whether AI agents still do their job safely and reliably as…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://spec27.ai/launch>
> 首次收录：2026-09-21T01:41:16+08:00
> 来源渠道：HN Show HN
> 标签：author_njyx, story_47959984, show_hn
> 最新指标：点赞=13 · 评论=9 · engagement_velocity=13

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=13 · 评论=9 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-21/ab9e71246f38886b_Show-HN-Spec27-–-Spec-driven-validation-for-AI-age]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=13 · 评论=9 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-21/ab9e71246f38886b_Show-HN-Spec27-–-Spec-driven-validation-for-AI-age]] |
| 2026-09-21T01:41:16+08:00 | HN Show HN | 点赞=13 · 评论=9 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-09-21/ab9e71246f38886b_Show-HN-Spec27-–-Spec-driven-validation-for-AI-age]] |

## 摘要正文

Hi HN! We’re a team of ML validation specialists and we’ve been building /Spec27, a tool for testing whether AI agents still do their job safely and reliably as models, prompts, tools, and surrounding systems change.We started working on this because a lot of current LLM evaluation work seems aimed at scoring general model behavior, while many teams are deploying systems that have a specific mission to fulfill. Many of the tools also assume you have full access to the agent stack and traces so you can place SDKs and Gateways, but a lot of agents are being created on vendor platforms where this isn’t possible.As a result, we approaches it from the outside in: all tests just run to the primary interfaces of an Agent and don’t assume anything about internals. The other important things about the approach is spec-driven. Instead of treating testing as a one-off benchmark or static eval set, we let teams define reusable specifications for the behavior they want from an agent, then generate tests against those specs. With this you can automatically generate adversarial and robustness checks, so you can see what an agent is sensitive to and what kinds of changes cause it to fail.We’ve wor…
