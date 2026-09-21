---
type: "project"
title: "Show HN: Testing a non-generative decision model on 5,500 CLINC150 inputs"
project_url: "https://github.com/chr-kelly/jev-cookbook"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tgdhtdujeytd
  - story_49778191
  - show_hn
lang: "en"
---

# Show HN: Testing a non-generative decision model on 5,500 CLINC150 inputs

> [!info] 一句话导读
> chr-kelly/jev-cookbook

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/chr-kelly/jev-cookbook>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_tgdhtdujeytd, story_49778191, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/076da1b23e5de1c1_Show-HN-Testing-a-non-generative-decision-model-on]] |

## 摘要正文

# chr-kelly/jev-cookbook  Runnable question sets for TypeSafe's Jev, an eval harness with measured CLINC150 results, and a linter for the request shapes the API silently mis-reads.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-09-20T17:21:07Z  ## Languages  - Python  ## Top Contributors  - chr-kelly (1 contributions)  ---  ## README  # Jev Cookbook  ### Stop guessing what Jev is for.  **Describe your decision. Copy working questions. Run them now.**  Runnable question sets for TypeSafe's Jev — not a link list.  ---  ## The problem  Jev is fast, cheap and typed. Everyone agrees on that by now.  The part nobody tells you is **what to actually ask it**. The docs show you the three primitives. The awesome-lists show you what other people built. Neither tells you how to turn *your* judgement into a question set that holds up on real data.  That gap is where this repo lives.  ## 10-second example  ```json {   "model": "jev-latest",   "state": "Hi, I ordered the blue one three weeks ago and it still hasn't shipped. This is the second time I'm writing. Can someone just refund me?",   "questions": {     "category": {     …
