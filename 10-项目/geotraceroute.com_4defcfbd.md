---
type: "project"
title: "Show HN: GeoTraceroute – Traceroutes on a 3D globe and submarine cables"
project_url: "https://geotraceroute.com/"
first_seen: "2026-09-21T01:42:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Himred
  - story_47943252
  - show_hn
lang: "en"
---

# Show HN: GeoTraceroute – Traceroutes on a 3D globe and submarine cables

> [!info] 一句话导读
> I've been working on GeoTraceroute for a while and just shipped v2.3

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://geotraceroute.com/>
> 首次收录：2026-09-21T01:42:31+08:00
> 来源渠道：HN Show HN
> 标签：author_Himred, story_47943252, show_hn
> 最新指标：点赞=21 · 评论=1 · engagement_velocity=21

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=21 · 评论=1 · engagement_velocity=21 | [[20-语料/posts/hn_show/2026-09-21/fd05ff3ee740ddf8_Show-HN-GeoTraceroute-–-Traceroutes-on-a-3D-globe]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=21 · 评论=1 · engagement_velocity=21 | [[20-语料/posts/hn_show/2026-09-21/fd05ff3ee740ddf8_Show-HN-GeoTraceroute-–-Traceroutes-on-a-3D-globe]] |
| 2026-09-21T01:42:31+08:00 | HN Show HN | 点赞=21 · 评论=1 · engagement_velocity=21 | [[20-语料/posts/hn_show/2026-09-21/fd05ff3ee740ddf8_Show-HN-GeoTraceroute-–-Traceroutes-on-a-3D-globe]] |

## 摘要正文

I've been working on GeoTraceroute for a while and just shipped v2.3 with submarine cable inference.A few things that might interest HN:- 320 community-contributed nodes across 50 countries, all volunteer-run - Three views: 3D globe with day/night rendering, 2D map, and a  topological mode that infers submarine cable routing - The submarine cable inference is the part I find most interesting.  Since cable routers don't respond to ICMP, the underwater segments  are invisible to standard traceroute. The tool detects ocean crossings  by geolocation delta between consecutive hops, then infers the likely  cable using a geo graph of landing points with A* pathfinding.  I have no way to validate this — if anyone has ideas, I'd love to discuss.Coverage is good in EU and US but thin in Asia, Africa and South America. If you want to contribute a node: https://geotraceroute.com/joinSalim
