---
type: "corpus"
item_id: "6ff80f60fe7ad399"
title: "Show HN: ArchDocs – Shared context and verification for engineers and AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50340570"
project_url: "https://archdocs.io/"
author: "AylonArmstrong"
published_at: "2026-11-02T17:44:32Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_AylonArmstrong
  - story_50340570
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: ArchDocs – Shared context and verification for engineers and AI agents

> [!info] 一句话导读
> Hi HN,My name is Aylon and I'm building ArchDocs. I started building ArchDocs in late 2024 as an architecture diagramming tool with reusable references and obje…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50340570>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：AylonArmstrong　|　发布：2026-11-02T17:44:32Z
> 项目链接：<https://archdocs.io/>
> 采集：2026-11-03T09:40:36+08:00　|　id：`6ff80f60fe7ad399`

## 正文

Hi HN,My name is Aylon and I'm building ArchDocs. I started building ArchDocs in late 2024 as an architecture diagramming tool with reusable references and objects (still exists today and is usable).As I've been using AI to code more and more, one of the things I've run into is that my agent doesn't have enough context around past decisions or findings that could affect an implementation, causing some nasty side-effects like redundant investigations, incorrect assumptions, repeating previously caught mistakes and ultimately wasting precious tokens.Let's say for example, you need to do a migration that affects 10 backend services. Your agent starts working on the first one and during the implementation and verification process, it discovers an issue that will undeniably affect the other 9 services. The next agent can start on the second service without knowing what was learned on the first.There's another problem I run up against time and time again. I need a dependable way to verify and log what an agent has done, the outcome of that and any deviations or issues that arise from it, so I can tell whether the change actually did what I intended.Enter Design Docs inside ArchDocs.The workflow is simple. You or your agent can craft a spec and ask questions for people to answer. Writing the implementation plan comes next, followed by doing the actual work. While you or your agent works, you track important milestones, deviations, decisions and more in the work log. Need to pause or have someone else do the work? No problem, craft a handoff or let ArchDocs AI do it for you. Finally, you or your agent logs a summarized version of what was done and how it was verified in an evidence of work submission.In that migration example, your agent can mark the issue in the work log as a "finding" and that will then be surfaced when future agents execute on the other 9 services.On the verification side, you may ask, "How does this help if the agent or engineer is just writing down their verification?" This is a good question and that's only one part of the verification. We have this concept of Agent attested (paired with human verified) and human attested. The last pillar and the most important is ArchDocs' own independent, automated verifications.Right now, we just have GitHub tracking for check results but we will soon be expanding this into so much more.Imagine one of the automated verifications is that a specific log with a specific attribute shows up in Datadog. Maybe even a specific event showing up in PostHog. There's a lot of ways we're going to take this and we're excited to share them once done.You can explore an example design doc without signing up. It includes the spec, implementation plan, work log and verification evidence:https://archdocs.io/templates/design-doc-example

## 关联链接

- https://archdocs.io/templates/design-doc-example

## 导航

- 项目页：[[10-项目/archdocs.io_d5def1de]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
