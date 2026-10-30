---
type: "corpus"
item_id: "9cf0756bd8d722c7"
title: "Show HN: Fitness Functions for Dbt Projects"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50294526"
project_url: "https://github.com/tjirab/tff"
author: "bartschuijt"
published_at: "2026-10-29T19:29:40Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_bartschuijt
  - story_50294526
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fitness Functions for Dbt Projects

> [!info] 一句话导读
> Managing data transformation (e.g. dbt) projects at scale can be challenging: DAG violations, that one model that grew to 2K lines, duplicated logic.Inspired by…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50294526>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：bartschuijt　|　发布：2026-10-29T19:29:40Z
> 项目链接：<https://github.com/tjirab/tff>
> 采集：2026-10-30T09:46:09+08:00　|　id：`9cf0756bd8d722c7`

## 正文

Managing data transformation (e.g. dbt) projects at scale can be challenging: DAG violations, that one model that grew to 2K lines, duplicated logic.Inspired by the book 'Building Evolutionary Architectures' I built tff to help data transformation projects evolve in a desired direction. It comes with a github bot that you can plugin to your CI pipeline.It aims to let transformation projects evolve in the desired direction by:
* ensuring layer boundary integrity;
* detect duplicate CTE logic;
* catch violations locally and in CICore concepts: rules apply to models; checks apply to architecture and DAG checks.Curious to read what you think. What can be improved? What's missing?

## 导航

- 项目页：[[10-项目/github.com_5502b32d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
