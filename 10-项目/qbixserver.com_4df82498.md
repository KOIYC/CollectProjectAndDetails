---
type: "project"
title: "SHOW HN: I built the fastest PHP webserver in the world"
project_url: "https://qbixserver.com/"
first_seen: "2026-09-20T14:02:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_EGreg
  - story_49748067
  - show_hn
lang: "en"
---

# SHOW HN: I built the fastest PHP webserver in the world

> [!info] 一句话导读
> SHOW HN: I built the fastest PHP webserver in the world

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://qbixserver.com/>
> 首次收录：2026-09-20T14:02:43+08:00
> 来源渠道：HN Show HN
> 标签：author_EGreg, story_49748067, show_hn
> 最新指标：点赞=6 · 评论=1 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-20/ea21e3d87bc65ec3_SHOW-HN-I-built-the-fastest-PHP-webserver-in-the-w]] |
| 2026-09-20T09:36:44+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-20/ea21e3d87bc65ec3_SHOW-HN-I-built-the-fastest-PHP-webserver-in-the-w]] |
| 2026-09-20T09:40:15+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-20/ea21e3d87bc65ec3_SHOW-HN-I-built-the-fastest-PHP-webserver-in-the-w]] |
| 2026-09-20T09:41:43+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-20/ea21e3d87bc65ec3_SHOW-HN-I-built-the-fastest-PHP-webserver-in-the-w]] |
| 2026-09-20T14:02:43+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-20/ea21e3d87bc65ec3_SHOW-HN-I-built-the-fastest-PHP-webserver-in-the-w]] |

## 摘要正文

SHOW HN: I built the fastest PHP webserver in the world | Hacker News  SHOW HN: I built the fastest PHP webserver in the world  6 points by EGreg 2 days ago | hide | past | favorite | 1 comment  After over a decade of writing apps in PHP, I always wondered why we needed all that extra tooling around it just to serve websites. I suspected PHP alone could be faster. I didn’t realize how right I was.  It’s finally done! Two months after I initially announced it, Qbix webserver 1.2 is out. It is written in pure PHP, meaning you can run web applications without nginx for serving files and websites, certbot for certificates, cron for periodic tasks, node for realtime sockets, etc. It comes out of the box with a user friendly dashboard and control panel, too. There are even standalone binaries you can download for Linux and MacOS that can contain your entire web application:  https://qbixserver.com  Originally it was much faster than php-fpm, but now it is also faster than even the fastest PHP runtimes. And unlike those runtimes, it is able to run existing PHP apps without modification!  First, how it can be this fast:  The vast majority of PHP apps make blocking I/O calls (to the databas…
