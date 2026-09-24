---
type: "project"
title: "Show HN: Foremerge – Catch intent conflicts between parallel coding agents"
project_url: "https://github.com/naw103/foremerge"
first_seen: "2026-09-22T14:15:46+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_naw103
  - story_49789356
  - show_hn
lang: "en"
---

# Show HN: Foremerge – Catch intent conflicts between parallel coding agents

> [!info] 一句话导读
> At, GPTree, we run several coding agents across our team on one repo using parallel worktrees. Apart from wasted time reviewing and fixing conflicts at PR time,…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/naw103/foremerge>
> 首次收录：2026-09-22T14:15:46+08:00
> 来源渠道：HN Show HN
> 标签：author_naw103, story_49789356, show_hn
> 最新指标：点赞=40 · 评论=11 · engagement_velocity=40

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=39 · 评论=10 · engagement_velocity=39 | [[20-语料/posts/hn_show/2026-09-22/07b433d88007f468_Show-HN-Foremerge-–-Catch-intent-conflicts-between]] |
| 2026-09-22T14:15:46+08:00 | HN Show HN | 点赞=40 · 评论=11 · engagement_velocity=40 | [[20-语料/posts/hn_show/2026-09-22/07b433d88007f468_Show-HN-Foremerge-–-Catch-intent-conflicts-between]] |

## 摘要正文

At, GPTree, we run several coding agents across our team on one repo using parallel worktrees. Apart from wasted time reviewing and fixing conflicts at PR time, the failures that hurt the most are when multiple plans or tickets cause architecture changes that cannot both be true. Ex. one agent replaces a class while another one is in the process of extending it. Git only notices if the resulting patches happen to touch the same lines and the review only catches it if they are familiar with both tickets.Foremerge is a local "git like" coordination layer that sits above git (ie. does not interact with or change the way git and worktrees function), Before editing each agent publishes an intent and the scopes it will change, with the operation it plans to complete on each one. foremerge intent publish --agent "$A" \  --summary "Replace PaymentService with StripePaymentService" \  --scope symbol:PaymentService=replace  foremerge intent publish --agent "$B" \  --summary "Add PayPal support to PaymentService" \  --scope symbol:PaymentService=extend  The publish by the 2nd agent returns a HIGH destructive_vs_additive finding before writing any code. Agents keep their own worktrees and the …
