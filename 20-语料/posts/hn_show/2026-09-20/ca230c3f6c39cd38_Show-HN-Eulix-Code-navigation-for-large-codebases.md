---
type: "corpus"
item_id: "ca230c3f6c39cd38"
title: "Show HN: Eulix - Code navigation for large codebases"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49714268"
project_url: "https://github.com/Nurysso/eulix"
author: "Nurysso"
published_at: "2026-09-15T15:41:18Z"
captured_at: "2026-09-20T09:41:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_Nurysso
  - story_49714268
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Eulix - Code navigation for large codebases

> [!info] 一句话导读
> Show HN: Eulix - Code navigation for large codebases

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49714268>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：Nurysso　|　发布：2026-09-15T15:41:18Z
> 项目链接：<https://github.com/Nurysso/eulix>
> 采集：2026-09-20T09:41:47+08:00　|　id：`ca230c3f6c39cd38`

## 正文

Show HN: Eulix - Code navigation for large codebases | Hacker News

Show HN: Eulix - Code navigation for large codebases

3 points by Nurysso 34 minutes ago | hide | past | favorite | discuss

Hey I've been working on Eulix, a tool for navigating large codebases.

It parses a repository into symbols, call graphs and other structural information, then combines that with keyword and semantic retrieval to find relevant code.

I tested it on OpenStack (~6.9M LOC / 29k files). One query about Nova's PCI passthrough scheduling pulled back the relevant filters, helpers and related call paths in well under a second once indexed.

Some queries don't need an LLM at all, since Eulix can answer directly from the structured codebase data.

It's open source and runs locally:

https://github.com/Nurysso/eulix

I'd especially like feedback from people who've worked on code search, static analysis, or large monorepos.

on a side note it may be able to handle 30M+ loc codebase too, I haven't been able to test such huge repos cause I don't have a good enough gpu to embed parsers output! :)

## 导航

- 项目页：[[10-项目/github.com_76956d5d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
