---
type: "corpus"
item_id: "1fe5b1e28a0210b3"
title: "Show HN: VisuaLeaf – A Modern MongoDB Workspace"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47949733"
project_url: "https://visualeaf.com/"
author: "Jacky101"
published_at: "2026-04-29T15:24:46Z"
captured_at: "2026-09-21T01:41:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_Jacky101
  - story_47949733
  - show_hn
metrics: {"points": 9, "comments": 1, "engagement_velocity": 9}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: VisuaLeaf – A Modern MongoDB Workspace

> [!info] 一句话导读
> Visualeaf is a MongoDB GUI I’ve been building over the past year. Stack is Electron + Angular + Spring Boot. There’s a live playground on the site if you want t…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47949733>
> 指标：点赞=9 · 评论=1 · engagement_velocity=9
> 作者：Jacky101　|　发布：2026-04-29T15:24:46Z
> 项目链接：<https://visualeaf.com/>
> 采集：2026-09-21T01:41:47+08:00　|　id：`1fe5b1e28a0210b3`

## 正文

Visualeaf is a MongoDB GUI I’ve been building over the past year. Stack is Electron + Angular + Spring Boot. There’s a live playground on the site if you want to try it without installing or putting in your connection (I provided one).The goal was to combine a visual workflow with the depth needed for real development work. Most existing MongoDB tools tend to optimize for either beginners or power users, but not both in the same interface.Core features:Query builder that supports full MongoDB query expressiveness + being able to drag and drop elements from the collection to the query builderForm based aggregation builder with synchronized JSON viewSchema visualization and generation toolsGridFS viewer with MP4 streaming support (streaming mp4 was pretty tricky )IDE style split panels and multiple workspacesImport/export transformations (mask/edit fields during export )Tree view ( finding a way to expand recursively thousands of nodes was a challenge)Table view (I had to build my own take on AG Grid focusing on optimizing horizontal and virtual scrolling to get it to scroll smoothly on thousands of rows and columns)A lot of the work ended up being performance engineering. It currently loads ~500MB of data into the UI in about 5 seconds on an M1 MacBook. And can even easily display over 20k documents of an average size (12kb) .Here’s a walkthrough of all its features:: https://www.youtube.com/watch?v=WNzvDlbpGTk
Happy to answer questions! Thank you so much!

## 评论（1/1）

> **roxana_haidiner** · 2026-04-29T19:13:16.000Z　
> The aggregation builder looks interesting. Does it stay usable with longer pipelines?

## 关联链接

- https://www.youtube.com/watch?v=WNzvDlbpGTk

## 导航

- 项目页：[[10-项目/visualeaf.com_ec4f621c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
