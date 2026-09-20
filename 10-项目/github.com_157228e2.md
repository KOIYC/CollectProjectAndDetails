---
type: "project"
title: "Show HN: HN Station – A local-first HN desktop client with split-pane reading"
project_url: "https://github.com/rajeshkumarblr/hn_station"
first_seen: "2026-09-21T01:43:10+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_raj_db_dev
  - story_48341045
  - show_hn
lang: "en"
---

# Show HN: HN Station – A local-first HN desktop client with split-pane reading

> [!info] 一句话导读
> This is my side project for reading hacker news in a specialized IDE like environment where all my news articles I read and the comments threads are group toget…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/rajeshkumarblr/hn_station>
> 首次收录：2026-09-21T01:43:10+08:00
> 来源渠道：HN Show HN
> 标签：author_raj_db_dev, story_48341045, show_hn
> 最新指标：点赞=4 · 评论=2 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/fa81e41601e05e4e_Show-HN-HN-Station-–-A-local-first-HN-desktop-clie]] |
| 2026-09-21T01:43:10+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/fa81e41601e05e4e_Show-HN-HN-Station-–-A-local-first-HN-desktop-clie]] |

## 摘要正文

Hi HN, This is my side project for reading hacker news in a specialized IDE like environment where all my news articles I read and the comments threads are group together in different threads. So it avoids the clutter when you read HN and it is mingled with other things like your email, work related tabs etc. This gives a focussed desktop app to read articles and it's discussions. I have also added a way to filter artcles based on keywords like LLM, PostgreSQL etc. So we can easily filter what we want to read and spend time with. It has bookmarking feature to read later on also. Same filtering works on bookmarks also.Under the hood, it's a Go + React app using SQLite for storage. Because everything you read is saved locally, you get a permanent personal archive, which you can search instantly using SQLite FTS5.I also added an integration with Ollama (or OpenAI) that runs in a sidebar to summarize long articles or pull out the main points from the comments thread. I built in a proxy so you can just plug your HN credentials in and vote/comment directly from the app, plus it strips out ads and cookies from the articles you read.To try it out quickly: https://hnstation.dev I have set u…
