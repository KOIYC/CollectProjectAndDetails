---
type: "corpus"
item_id: "db5004d9a75d1bf3"
title: "Show HN: Lightspeed, build real time apps the Laravel way (+asteroids demo)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49781032"
project_url: "https://innerloop.works/lightspeedRepo"
author: "jv22222"
published_at: "2026-09-20T23:02:28Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_jv22222
  - story_49781032
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Lightspeed, build real time apps the Laravel way (+asteroids demo)

> [!info] 一句话导读
> Hi HN!Laravel has worked with websockets for years but generally speaking it's a one way push architecture (i.e. http in, sockets out).Lightspeed is kind of lik…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49781032>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：jv22222　|　发布：2026-09-20T23:02:28Z
> 项目链接：<https://innerloop.works/lightspeedRepo>
> 采集：2026-09-21T09:44:03+08:00　|　id：`db5004d9a75d1bf3`

## 正文

Hi HN!Laravel has worked with websockets for years but generally speaking it's a one way push architecture (i.e. http in, sockets out).Lightspeed is kind of like node in that it's a single server that serves your http and your websockets all under one roof. Auth runs in 0.03ms (a Redis read, no database). Your Laravel handler runs inside the full container and the reply comes back down the same socket. I think this could be really cool for creating new ways of working with Laravel.Anyway, I put together a live demo to show it in action. Basically a cross between slither.io and Asteroids.Game here:https://innerloop.works/lightspeedRepo here:https://github.com/innerloop-dev/lightspeedNote: This is 0.1.0, the API may change before 1.0. It needs the Swoole extension and Redis. MIT.

## 评论（2/2）

> **AlchemistCamp** · 2026-09-20T23:42:41.000Z　
> How does this relate to Laravel LiveWire?

---

> **jv22222** · 2026-09-20T23:54:05.000Z　
> It doesn't! Livewire is a way to build UI/form interactions over http/js.Lightspeed is a websocket server.Livewire talks to the server over normal HTTP requests and for anything pushed from the server it uses Laravel Echo. Lightspeed is a Pusher-compatible server so you'd point Echo at it like you would Reverb.The thing Lightspeed adds is letting the browser send messages back into Laravel over that same socket, with auth on each one. Livewire doesn't do that its actions are still HTTP.For most applications Livewire would be the goto. Lightspeed is kind of a high speed specialist option for building real time apps like you might do with node.js for exmaple.

## 关联链接

- https://github.com/innerloop-dev/lightspeedNote:

## 导航

- 项目页：[[10-项目/innerloop.works_b96b1b64]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
