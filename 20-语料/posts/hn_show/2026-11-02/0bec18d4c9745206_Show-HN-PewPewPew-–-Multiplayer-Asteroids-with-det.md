---
type: "corpus"
item_id: "0bec18d4c9745206"
title: "Show HN: PewPewPew – Multiplayer Asteroids with deterministic rollback at 60hz"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50326850"
project_url: "https://pewpewpew.io/"
author: "Benjaminsen"
published_at: "2026-11-01T16:02:24Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_Benjaminsen
  - story_50326850
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: PewPewPew – Multiplayer Asteroids with deterministic rollback at 60hz

> [!info] 一句话导读
> I have been building realtime multiplayer games that run in a browser since 1999 and my latest is pewpewpew.io which combines everything I know about doing this…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50326850>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：Benjaminsen　|　发布：2026-11-01T16:02:24Z
> 项目链接：<https://pewpewpew.io/>
> 采集：2026-11-02T09:37:22+08:00　|　id：`0bec18d4c9745206`

## 正文

I have been building realtime multiplayer games that run in a browser since 1999 and my latest is pewpewpew.io which combines everything I know about doing this well.The game uses a fully client and server synchronized state machine running at 60hz with rollback / rollforward on both client and server.During normal play only user input is transmitted using a compressed message format, where input is 7 fields in 2 bytes, with a total of about 26KB/s used for a room with 32 active players.Users are automatically distributed into a room on a server with the lowest measured ping where there are other players playing.Currently running using cloudflare Durable Objects, but I expect to offload it to dedicated metal should the cost go above $500 / month. Current monthly cost sits at about $300 per 1K average CCU.Works on mobile, free to play, no ads, no signup.

## 导航

- 项目页：[[10-项目/pewpewpew.io_9ba94c20]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
