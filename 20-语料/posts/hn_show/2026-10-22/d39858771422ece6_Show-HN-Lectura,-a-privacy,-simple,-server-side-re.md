---
type: "corpus"
item_id: "d39858771422ece6"
title: "Show HN: Lectura, a privacy, simple, server side rendered RSS reader"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50180704"
project_url: "https://lectura.info/"
author: "nomemory"
published_at: "2026-10-21T13:34:20Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_nomemory
  - story_50180704
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Lectura, a privacy, simple, server side rendered RSS reader

> [!info] 一句话导读
> I am avid reader of blogs (always been since 2005 onwards), so it was always on my list to build a rss reader at some point.Initially I've built lectura for mys…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50180704>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：nomemory　|　发布：2026-10-21T13:34:20Z
> 项目链接：<https://lectura.info/>
> 采集：2026-10-22T09:46:18+08:00　|　id：`d39858771422ece6`

## 正文

I am avid reader of blogs (always been since 2005 onwards), so it was always on my list to build a rss reader at some point.Initially I've built lectura for myself (the first version started when I've experimented with server side rendering/Thymeleaf + Spring Boot) and self hosted on a server (without a domain). Then I decided to vibecode multi user support. And this is the final result.What are some highlights:- It doesn't track/record what the users are doing. There are no emails (no password recovering in case you lose your password). The only information that's kept are your own subscription, that others can see as well. But that's it. Because of this, creating a username takes 5 seconds (depending on how fast you write);- It supports different layouts that I find useful with my RSS reader. For example there's a 'random' content view so you can read "historical articles" you've might missed. There's a another view called 'Quiet Sources' so you can 'prioritise' blogs that don't publish often. I'll let you find the other views.- It has good accesibility support, or it should. If not, drop me some feedback;- For the moment it's free. I don't expect a big influx of users (who uses a RSS reader + reading blogs nowadays) so I have a cheap dedicated server at 20$ per month. With the current resources, unless someone really wants to "put it down", it should work with a few hundred users (reading concurrently). I can afford paying 20$ montly withouthing thinking to ask for money, at least for the moment.That's it.I don't have experience with 'products', 'startups', etc. This is just a project I hope will be useful to someone other than me. If not, i will keep using it as my "premium" RSS reader :).Cheers,
Andrei

## 评论（2/2）

> **agenticpacks** · 2026-10-21T14:08:15.000Z　
> Looks interesting. Curious to know what you are using using for storing on the VPS? Do you keep articles indefinitely, or do you delete older items?

---

> **nomemory** · 2026-10-21T14:11:54.000Z　
> Hello, for the moment I keep only titles and summaries, not the full articles. Once the articles become too many (for the moment it's not the case), I will think of some partitioning solutions.The underlying database is PostgreSQL and it works well under medium load.Thank you for the comment.

## 导航

- 项目页：[[10-项目/lectura.info_6e72d89b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
