---
type: "corpus"
item_id: "fd05ff3ee740ddf8"
title: "Show HN: GeoTraceroute – Traceroutes on a 3D globe and submarine cables"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47943252"
project_url: "https://geotraceroute.com/"
author: "Himred"
published_at: "2026-04-29T01:45:03Z"
captured_at: "2026-09-21T01:42:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_Himred
  - story_47943252
  - show_hn
metrics: {"points": 21, "comments": 1, "engagement_velocity": 21}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:174d"
---

# Show HN: GeoTraceroute – Traceroutes on a 3D globe and submarine cables

> [!info] 一句话导读
> I've been working on GeoTraceroute for a while and just shipped v2.3

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47943252>
> 指标：点赞=21 · 评论=1 · engagement_velocity=21
> 作者：Himred　|　发布：2026-04-29T01:45:03Z
> 项目链接：<https://geotraceroute.com/>
> 采集：2026-09-21T01:42:31+08:00　|　id：`fd05ff3ee740ddf8`

## 正文

I've been working on GeoTraceroute for a while and just shipped v2.3
with submarine cable inference.A few things that might interest HN:- 320 community-contributed nodes across 50 countries, all volunteer-run
- Three views: 3D globe with day/night rendering, 2D map, and a
 topological mode that infers submarine cable routing
- The submarine cable inference is the part I find most interesting.
 Since cable routers don't respond to ICMP, the underwater segments
 are invisible to standard traceroute. The tool detects ocean crossings
 by geolocation delta between consecutive hops, then infers the likely
 cable using a geo graph of landing points with A* pathfinding.
 I have no way to validate this — if anyone has ideas, I'd love to discuss.Coverage is good in EU and US but thin in Asia, Africa and South America.
If you want to contribute a node: https://geotraceroute.com/joinSalim

## 评论（1/1）

> **ilbert** · 2026-04-29T08:00:09.000Z　
> Really cool! Just as feedback, the 3D worldview seems to have low quality on my browser

## 关联链接

- https://geotraceroute.com/joinSalim

## 导航

- 项目页：[[10-项目/geotraceroute.com_4defcfbd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
