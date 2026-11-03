---
type: "project"
title: "Show HN: ArchDocs – Shared context and verification for engineers and AI agents"
project_url: "https://archdocs.io/"
first_seen: "2026-11-03T09:40:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_AylonArmstrong
  - story_50340570
  - show_hn
lang: "en"
---

# Show HN: ArchDocs – Shared context and verification for engineers and AI agents

> [!info] 一句话导读
> Hi HN,My name is Aylon and I'm building ArchDocs. I started building ArchDocs in late 2024 as an architecture diagramming tool with reusable references and obje…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://archdocs.io/>
> 首次收录：2026-11-03T09:40:36+08:00
> 来源渠道：HN Show HN
> 标签：author_AylonArmstrong, story_50340570, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-03T09:40:36+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-03/6ff80f60fe7ad399_Show-HN-ArchDocs-–-Shared-context-and-verification]] |

## 摘要正文

Hi HN,My name is Aylon and I'm building ArchDocs. I started building ArchDocs in late 2024 as an architecture diagramming tool with reusable references and objects (still exists today and is usable).As I've been using AI to code more and more, one of the things I've run into is that my agent doesn't have enough context around past decisions or findings that could affect an implementation, causing some nasty side-effects like redundant investigations, incorrect assumptions, repeating previously caught mistakes and ultimately wasting precious tokens.Let's say for example, you need to do a migration that affects 10 backend services. Your agent starts working on the first one and during the implementation and verification process, it discovers an issue that will undeniably affect the other 9 services. The next agent can start on the second service without knowing what was learned on the first.There's another problem I run up against time and time again. I need a dependable way to verify and log what an agent has done, the outcome of that and any deviations or issues that arise from it, so I can tell whether the change actually did what I intended.Enter Design Docs inside ArchDocs.The w…
