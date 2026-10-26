---
type: "corpus"
item_id: "b709794f8249bd93"
title: "Show HN: Radian, an agent puts development workflow on autopilot"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50233447"
project_url: "https://getrad.dev/"
author: "anylut"
published_at: "2026-10-25T16:41:36Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_anylut
  - story_50233447
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Radian, an agent puts development workflow on autopilot

> [!info] 一句话导读
> I have built an indie hacker project; my main flow was:1. chatting with Claud Code about the general plan2. assigning slices of work to other worker agents like…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50233447>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：anylut　|　发布：2026-10-25T16:41:36Z
> 项目链接：<https://getrad.dev/>
> 采集：2026-10-26T09:42:36+08:00　|　id：`b709794f8249bd93`

## 正文

I have built an indie hacker project; my main flow was:1. chatting with Claud Code about the general plan2. assigning slices of work to other worker agents like Pi + DeepSeek 4.1 Flash3. building in parallel4. Claud Code reviews when done, runs tests, and merges after I validateIt worked, but with a lot of glue in the middle, so I built radian + arc into the same binary.Radian: a compact, pragmatic agent that has enough tooling to solve a small coding task end to end; it does not try to be a plugin platform. You can still extend it via MCP, skills, or hooks to extend its capabilities. I think plugins are great, but a lot of them are for humans. I'm trying to remove humans from the loop. Humans are at the start and end of the loop.arc: built into the radian binary;* it can get work sent from another agent* assign work items to concurrent headless radian agents* automatically review, CICD, integrate locally* humans can still be in the loop but not at the agent conversation or code review level, but at the work item approval/review level.* shows all of the above in a plan view or Kanban board in TUI.I have been heavily dogfooding, and Radian + arc basically built themselves in the last couple of weeks, with me just being a product manager/scrum master and qa.radian + arc are open source at https://github.com/hisea/radianWhat do you think about this approach?
Looking for ideas to make Radian better or fit more scenarios.

## 关联链接

- https://github.com/hisea/radianWhat

## 导航

- 项目页：[[10-项目/getrad.dev_180e1372]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
