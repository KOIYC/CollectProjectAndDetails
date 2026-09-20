---
type: "corpus"
item_id: "ab9e71246f38886b"
title: "Show HN: Spec27 – Spec-driven validation for AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47959984"
project_url: "https://spec27.ai/launch"
author: "njyx"
published_at: "2026-04-30T09:07:14Z"
captured_at: "2026-09-21T01:41:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_njyx
  - story_47959984
  - show_hn
metrics: {"points": 13, "comments": 9, "engagement_velocity": 13}
comments_count: 9
comments_total: 9
discovered_via: "hn:show_hn:174d"
---

# Show HN: Spec27 – Spec-driven validation for AI agents

> [!info] 一句话导读
> Hi HN! We’re a team of ML validation specialists and we’ve been building /Spec27, a tool for testing whether AI agents still do their job safely and reliably as…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47959984>
> 指标：点赞=13 · 评论=9 · engagement_velocity=13
> 作者：njyx　|　发布：2026-04-30T09:07:14Z
> 项目链接：<https://spec27.ai/launch>
> 采集：2026-09-21T01:41:16+08:00　|　id：`ab9e71246f38886b`

## 正文

Hi HN! We’re a team of ML validation specialists and we’ve been building /Spec27, a tool for testing whether AI agents still do their job safely and reliably as models, prompts, tools, and surrounding systems change.We started working on this because a lot of current LLM evaluation work seems aimed at scoring general model behavior, while many teams are deploying systems that have a specific mission to fulfill. Many of the tools also assume you have full access to the agent stack and traces so you can place SDKs and Gateways, but a lot of agents are being created on vendor platforms where this isn’t possible.As a result, we approaches it from the outside in: all tests just run to the primary interfaces of an Agent and don’t assume anything about internals. The other important things about the approach is spec-driven. Instead of treating testing as a one-off benchmark or static eval set, we let teams define reusable specifications for the behavior they want from an agent, then generate tests against those specs. With this you can automatically generate adversarial and robustness checks, so you can see what an agent is sensitive to and what kinds of changes cause it to fail.We’ve worked on validation for other AI systems before, including vision and tabular workflows, and /Spec27 is our new product for language-model-based agents. Currently in early access, so we’d love feedback! The current version is strongest for single-turn agent and application validation. We do not fully support multi-turn interactions yet, and better telemetry/tool-call integration is still on our roadmap.We’ve made the product open to try for HN readers, with a sample flow so it’s easy to poke around without much setup. We’d especially love feedback from people deploying internal agents, vendor agents, or other AI systems where reliability matters more than benchmark scores.

## 评论（9/9）

> **_mikz** · 2026-04-30T09:58:44.000Z　
> Hey! Michal from the engineering team behind here. There are some painful experiences from the journey - async in Django, background processing in Python, scaling agent workflows with growing codebase. Happy to talk!

---

> **jovanca_** · 2026-04-30T10:03:31.000Z　
> Hi! Jovanca from Spec27 team here. We started building this because agent safety/validation still feels pretty undercooked in practice. Interested in how people here think about it :D

---

> **chesh** · 2026-04-30T10:04:20.000Z　
> I get so mad when responses from chat agents hallucinate. If this can rebuild trust in the results I will give Spec27 a try

---

> **eloycoto** · 2026-04-30T10:18:39.000Z　
> I really like the judge from here: https://docs.spec27.ai/docs/guides/judgesI didn't see any example of the full flow, do you have anything that I can see/explore?

---

> **Aniloid2** · 2026-04-30T11:09:36.000Z　
> Hey, I’m Brian from Research at Spec27. I’ve been working on some of the adversarial robustness techniques in the backend and am currently working on the multi-turn extension. I’d be happy to talk about what I’ve learned and hear any suggestions!

---

> **njyx** · 2026-04-30T10:02:47.000Z　
> Also, Github CLI budgets exploding :-)

---

> **njyx** · 2026-04-30T11:41:49.000Z　
> Assuming you know when they hallucinate?

---

> **njyx** · 2026-04-30T10:38:13.000Z　
> Thanks for the feedback and question @eloycoto - there's a Loom video here: https://www.loom.com/share/727528de450a48d29a2ac20b279e26fc, and in the system itself, you can grab an example project from the registry.There are out of the box judges and then you can customize them for each spec if you are testing something specific.

---

> **eloycoto** · 2026-04-30T10:43:30.000Z　
> ohh crazy good! I'll try this weekend and I'll keep you posted. Thanks!

## 导航

- 项目页：[[10-项目/spec27.ai_cc5a60de]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
