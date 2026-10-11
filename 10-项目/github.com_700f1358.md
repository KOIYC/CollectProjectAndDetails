---
type: "project"
title: "Show HN: A Simple Server for Matching Long/Lat to a Timezone"
project_url: "https://github.com/LittleGreenViper/LGV_TZ_Lookup"
first_seen: "2026-10-11T09:54:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ChrisMarshallNY
  - story_50035690
  - show_hn
lang: "en"
---

# Show HN: A Simple Server for Matching Long/Lat to a Timezone

> [!info] 一句话导读
> LittleGreenViper/LGV_TZ_Lookup

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/LittleGreenViper/LGV_TZ_Lookup>
> 首次收录：2026-10-11T09:54:15+08:00
> 来源渠道：HN Show HN
> 标签：author_ChrisMarshallNY, story_50035690, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-11T09:43:53+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-11/aa64cd7aec363649_Show-HN-A-Simple-Server-for-Matching-Long-Lat-to-a]] |
| 2026-10-11T09:54:15+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-11/aa64cd7aec363649_Show-HN-A-Simple-Server-for-Matching-Long-Lat-to-a]] |

## 摘要正文

# LittleGreenViper/LGV_TZ_Lookup  Server for Matching Long/Lat to Timezone  - Stars: 47 - Forks: 2 - Watchers: 47 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2023-06-13T14:20:06Z  ## Languages  - PHP  ## Top Contributors  - ChrisMarshallNY (61 contributions)  ---  ## README  # LGV_TZ_Lookup A Server for Matching Long/Lat to Timezone  ## Overview This project is a fairly simple PHP project, designed to accept the GeoJSON output of the Timezone Boundary Builder Project, and provide a simple API, for matching longitude/latitude locations with timezones.  Send in a long/lat, and get back a string, with the standard TZ time zone designator of the timezone that covers that point.  This is the GitHub repo for this project  ## What Problem Does This Solve? Unfortunately, time zones are not a simple "I'm at this longitude, so it must be this time." They are political constructs.  Here's why we can't just do a simple longitude match:  Time Zones Of the World _Image Source: Wikimedia Commons_  We address this by using the rendered result of this great project, which is an effort to build a "living document" map of all the world timezones, as a shapefile (a file t…
