---
type: "project"
title: "Show HN: Lightspeed, build real time apps the Laravel way (+asteroids demo)"
project_url: "https://innerloop.works/lightspeedRepo"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jv22222
  - story_49781032
  - show_hn
lang: "en"
---

# Show HN: Lightspeed, build real time apps the Laravel way (+asteroids demo)

> [!info] 一句话导读
> Hi HN!Laravel has worked with websockets for years but generally speaking it's a one way push architecture (i.e. http in, sockets out).Lightspeed is kind of lik…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://innerloop.works/lightspeedRepo>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_jv22222, story_49781032, show_hn
> 最新指标：点赞=6 · 评论=2 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=6 · 评论=2 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/db5004d9a75d1bf3_Show-HN-Lightspeed,-build-real-time-apps-the-Larav]] |

## 摘要正文

Hi HN!Laravel has worked with websockets for years but generally speaking it's a one way push architecture (i.e. http in, sockets out).Lightspeed is kind of like node in that it's a single server that serves your http and your websockets all under one roof. Auth runs in 0.03ms (a Redis read, no database). Your Laravel handler runs inside the full container and the reply comes back down the same socket. I think this could be really cool for creating new ways of working with Laravel.Anyway, I put together a live demo to show it in action. Basically a cross between slither.io and Asteroids.Game here:https://innerloop.works/lightspeedRepo here:https://github.com/innerloop-dev/lightspeedNote: This is 0.1.0, the API may change before 1.0. It needs the Swoole extension and Redis. MIT.
