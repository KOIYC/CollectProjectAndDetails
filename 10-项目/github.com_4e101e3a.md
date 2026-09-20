---
type: "project"
title: "Show HN: Spewer – Delegate Codex/Claude tasks to cheaper models"
project_url: "https://github.com/modiqo/spewer"
first_seen: "2026-09-21T03:11:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_conikeec
  - story_49499265
  - show_hn
lang: "en"
---

# Show HN: Spewer – Delegate Codex/Claude tasks to cheaper models

> [!info] 一句话导读
> Delegate bounded agent work to cheaper models with durable state and verifiable receipts.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/modiqo/spewer>
> 首次收录：2026-09-21T03:11:31+08:00
> 来源渠道：HN Show HN
> 标签：author_conikeec, story_49499265, show_hn
> 最新指标：点赞=3 · 评论=1 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:33:52+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/177900dd69707036_Show-HN-Spewer-–-Delegate-Codex-Claude-tasks-to-ch]] |
| 2026-09-21T02:57:18+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/177900dd69707036_Show-HN-Spewer-–-Delegate-Codex-Claude-tasks-to-ch]] |
| 2026-09-21T03:11:31+08:00 | HN Show HN | 点赞=3 · 评论=1 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/177900dd69707036_Show-HN-Spewer-–-Delegate-Codex-Claude-tasks-to-ch]] |

## 摘要正文

# modiqo/spewer  Delegate bounded agent work to cheaper models with durable state and verifiable receipts.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://modiqo.github.io/spewer/ - Default branch: main - Created: 2026-08-29T05:56:59Z  ## Languages  - CSS - HTML - Rust - Shell  ## Topics  - ai-agents - codex - llm - orchestration - rust  ## Top Contributors  - conikeec (30 contributions)  ---  ## README  # Spewer  Spewer is a local service that lets your current AI harness delegate bounded work to lower-cost models.  Keep working in Codex, Claude Code, Kimi, or another preferred harness. Spewer runs the delegated worker, keeps its task alive, and returns an evidence-rich receipt.  A frontier harness delegates bounded work through Spewer to a commodity model  The shortest useful path is three commands:  ```console $ brew install modiqo/tap/spewer $ spewer install $ spewer ask "What is 17 multiplied by 19?" 323 ```  That is a working Spewer. The next steps add background work, local Qwen3, frontier delegation, specialized skills, and concurrent workers.  ## Start with one useful worker  You need macOS or Linux and Git. Spewer in…
