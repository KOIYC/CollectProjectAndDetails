---
type: "corpus"
item_id: "fa81e41601e05e4e"
title: "Show HN: HN Station – A local-first HN desktop client with split-pane reading"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48341045"
project_url: "https://github.com/rajeshkumarblr/hn_station"
author: "raj_db_dev"
published_at: "2026-05-30T22:03:53Z"
captured_at: "2026-09-21T01:43:10+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_raj_db_dev
  - story_48341045
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:144d"
---

# Show HN: HN Station – A local-first HN desktop client with split-pane reading

> [!info] 一句话导读
> This is my side project for reading hacker news in a specialized IDE like environment where all my news articles I read and the comments threads are group toget…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48341045>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：raj_db_dev　|　发布：2026-05-30T22:03:53Z
> 项目链接：<https://github.com/rajeshkumarblr/hn_station>
> 采集：2026-09-21T01:43:10+08:00　|　id：`fa81e41601e05e4e`

## 正文

Hi HN,
This is my side project for reading hacker news in a specialized IDE like environment where all my news articles I read and the comments threads are group together in different threads. So it avoids the clutter when you read HN and it is mingled with other things like your email, work related tabs etc. This gives a focussed desktop app to read articles and it's discussions. I have also added a way to filter artcles based on keywords like LLM, PostgreSQL etc. So we can easily filter what we want to read and spend time with. It has bookmarking feature to read later on also. Same filtering works on bookmarks also.Under the hood, it's a Go + React app using SQLite for storage. Because everything you read is saved locally, you get a permanent personal archive, which you can search instantly using SQLite FTS5.I also added an integration with Ollama (or OpenAI) that runs in a sidebar to summarize long articles or pull out the main points from the comments thread. I built in a proxy so you can just plug your HN credentials in and vote/comment directly from the app, plus it strips out ads and cookies from the articles you read.To try it out quickly: https://hnstation.dev
I have set up a "Lite" web preview so you can see the UI. There are no signups/logins here, it just stores your settings/bookmarks in the browser's local storage.For the full experience with the persistent SQLite archive and Ollama integration, the Windows, macOS, or Linux binaries are on the GitHub repo: https://github.com/rajeshkumarblr/hn_stationI built this to scratch my own itch, but I'm hoping some of you might find it useful too. I'd love to hear your feedback or ideas on how to make this better!

## 评论（2/2）

> **solbusinesstech** · 2026-05-31T07:11:30.000Z　
> It is very easy to loose track of interested articles, products, watch later items. HN station addresses this in a very use to ease manner and helps elevates the experience of staying with HN news.

---

> **SREandOthers** · 2026-06-01T02:42:40.000Z　
> Cool environment to read HN articles! Devs would find this super useful!

## 关联链接

- https://github.com/rajeshkumarblr/hn_stationI
- https://hnstation.dev

## 导航

- 项目页：[[10-项目/github.com_157228e2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
