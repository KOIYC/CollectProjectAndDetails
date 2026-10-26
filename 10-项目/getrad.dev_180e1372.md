---
type: "project"
title: "Show HN: Radian, an agent puts development workflow on autopilot"
project_url: "https://getrad.dev/"
first_seen: "2026-10-26T09:42:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_anylut
  - story_50233447
  - show_hn
lang: "en"
---

# Show HN: Radian, an agent puts development workflow on autopilot

> [!info] 一句话导读
> I have built an indie hacker project; my main flow was:1. chatting with Claud Code about the general plan2. assigning slices of work to other worker agents like…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://getrad.dev/>
> 首次收录：2026-10-26T09:42:36+08:00
> 来源渠道：HN Show HN
> 标签：author_anylut, story_50233447, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:42:36+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-26/b709794f8249bd93_Show-HN-Radian,-an-agent-puts-development-workflow]] |

## 摘要正文

I have built an indie hacker project; my main flow was:1. chatting with Claud Code about the general plan2. assigning slices of work to other worker agents like Pi + DeepSeek 4.1 Flash3. building in parallel4. Claud Code reviews when done, runs tests, and merges after I validateIt worked, but with a lot of glue in the middle, so I built radian + arc into the same binary.Radian: a compact, pragmatic agent that has enough tooling to solve a small coding task end to end; it does not try to be a plugin platform. You can still extend it via MCP, skills, or hooks to extend its capabilities. I think plugins are great, but a lot of them are for humans. I'm trying to remove humans from the loop. Humans are at the start and end of the loop.arc: built into the radian binary;* it can get work sent from another agent* assign work items to concurrent headless radian agents* automatically review, CICD, integrate locally* humans can still be in the loop but not at the agent conversation or code review level, but at the work item approval/review level.* shows all of the above in a plan view or Kanban board in TUI.I have been heavily dogfooding, and Radian + arc basically built themselves in the las…
