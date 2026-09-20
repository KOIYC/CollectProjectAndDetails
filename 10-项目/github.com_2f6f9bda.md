---
type: "project"
title: "Show HN: Open-Source Alternative to TypeSafe.ai"
project_url: "https://github.com/TitovDigital/kbai-skill"
first_seen: "2026-09-20T14:02:39+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ptitov
  - story_49750649
  - show_hn
lang: "en"
---

# Show HN: Open-Source Alternative to TypeSafe.ai

> [!info] 一句话导读
> TitovDigital/kbai-skill

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/TitovDigital/kbai-skill>
> 首次收录：2026-09-20T14:02:39+08:00
> 来源渠道：HN Show HN
> 标签：author_ptitov, story_49750649, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/ad3811623842022e_Show-HN-Open-Source-Alternative-to-TypeSafe.ai]] |
| 2026-09-20T09:36:42+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/ad3811623842022e_Show-HN-Open-Source-Alternative-to-TypeSafe.ai]] |
| 2026-09-20T14:02:39+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/ad3811623842022e_Show-HN-Open-Source-Alternative-to-TypeSafe.ai]] |

## 摘要正文

# TitovDigital/kbai-skill  - Stars: 3 - Forks: 1 - Watchers: 3 - Open issues: 0 - License: Other - Default branch: master - Created: 2026-09-13T20:55:16Z  ## Languages  - JavaScript  ## Top Contributors  - paul-at (14 contributions)  ---  ## README  # kbai-skill  A self-contained template for building a **symbolic reasoning engine** — rules are JavaScript functions executed by a forward-chaining symbolic inference engine locally with Node.js.  It's useful when: * you need **auditable, repeatable decisions** over messy inputs — cases where a pure LLM is too unreliable to trust with the decision itself, * the decision workflow is such that **can be written down by a domain expert as a policy**, * decision logic follows **tree-like structure (if-then), possibly with unclear dependencies**, rather than a linear process.  To interact with unstructured inputs, an agent can be used to orchestrate a feedback loop between LLM fact extraction and deterministic rule evaluation, refusing to guess when facts are ambiguous.  This repo contains a model knowledge base template (clone it, use the skill to modify `.kb/`, ship) and the `symbolic-kb` skill in `.claude/skills/symbolic-kb/`, which inclu…
