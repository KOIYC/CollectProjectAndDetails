---
type: "corpus"
item_id: "19485b413372e54f"
title: "Show HN: Things to Do API"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50126384"
project_url: "https://thingstodoapi.com/"
author: "invalidmonk"
published_at: "2026-10-16T23:58:34Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_invalidmonk
  - story_50126384
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Things to Do API

> [!info] 一句话导读
> I built an api/mcp for local events: pop-ups, one-off events, concerts, etc. currently covering the SF bay area.I've been building a bunch of consumer apps late…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50126384>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：invalidmonk　|　发布：2026-10-16T23:58:34Z
> 项目链接：<https://thingstodoapi.com/>
> 采集：2026-10-17T13:35:15+08:00　|　id：`19485b413372e54f`

## 正文

I built an api/mcp for local events: pop-ups, one-off events, concerts, etc. currently covering the SF bay area.I've been building a bunch of consumer apps lately around personalization and recommendation and have had a hard time finding this data in one spot. agents can find useful stuff through tool calls / web search, but slow.you can scrape on demand too, but i wanted a faster data set and couldn't find an existing provider for the mix of event types I was searching for.the methodology for it is to find influential accounts/posters/etc. and do a fan out across things that they co-post with.mcp: `claude mcp add --transport http thingstodo https://api.thingstodoapi.com/mcp`I'm considering adding other cities. If you're building something that needs local event data, would something like this be useful and where would you want coverage?

## 评论（2/2）

> **lap248** · 2026-10-17T01:14:15.000Z　
> super slick! got results quickly and am getting more interesting and in the know kind of events than other tools

---

> **egonschiele** · 2026-10-17T02:06:30.000Z　
> This feels hard to maintain and keep up-to-date, but I would definitely use it! Great idea.

## 关联链接

- https://api.thingstodoapi.com/mcp`I

## 导航

- 项目页：[[10-项目/thingstodoapi.com_3f21368f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
