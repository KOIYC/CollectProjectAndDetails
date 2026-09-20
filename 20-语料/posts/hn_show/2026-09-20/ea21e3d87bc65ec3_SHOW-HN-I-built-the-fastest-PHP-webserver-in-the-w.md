---
type: "corpus"
item_id: "ea21e3d87bc65ec3"
title: "SHOW HN: I built the fastest PHP webserver in the world"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49748067"
project_url: "https://qbixserver.com/"
author: "EGreg"
published_at: "2026-09-17T23:18:42Z"
captured_at: "2026-09-20T14:02:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_EGreg
  - story_49748067
  - show_hn
metrics: {"points": 6, "comments": 1, "engagement_velocity": 6}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# SHOW HN: I built the fastest PHP webserver in the world

> [!info] 一句话导读
> SHOW HN: I built the fastest PHP webserver in the world

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49748067>
> 指标：点赞=6 · 评论=1 · engagement_velocity=6
> 作者：EGreg　|　发布：2026-09-17T23:18:42Z
> 项目链接：<https://qbixserver.com/>
> 采集：2026-09-20T14:02:43+08:00　|　id：`ea21e3d87bc65ec3`

## 正文

SHOW HN: I built the fastest PHP webserver in the world | Hacker News

SHOW HN: I built the fastest PHP webserver in the world

6 points by EGreg 2 days ago | hide | past | favorite | 1 comment

After over a decade of writing apps in PHP, I always wondered why we needed all that extra tooling around it just to serve websites. I suspected PHP alone could be faster. I didn’t realize how right I was.

It’s finally done! Two months after I initially announced it, Qbix webserver 1.2 is out. It is written in pure PHP, meaning you can run web applications without nginx for serving files and websites, certbot for certificates, cron for periodic tasks, node for realtime sockets, etc. It comes out of the box with a user friendly dashboard and control panel, too. There are even standalone binaries you can download for Linux and MacOS that can contain your entire web application:

https://qbixserver.com

Originally it was much faster than php-fpm, but now it is also faster than even the fastest PHP runtimes. And unlike those runtimes, it is able to run existing PHP apps without modification!

First, how it can be this fast:

The vast majority of PHP apps make blocking I/O calls (to the database, files, network calls etc) While that happens, the thread is blocked.

FrankenPHP, Swoole, amphp and others take the “evented” approach which is much faster, but require all I/O calls to be rewritten to use their async libraries. But most existing PHP code would need a lot of work to be ported to async style, and even if it was, sometimes the async libraries don’t handle everything the mainstream ones do.

Qbix Webserver takes a different approach: it spawns hundreds, sometimes thousands of processes on Linux, Mac etc. When a process is blocked waiting on I/O, the rest of the application can handle thousands of concurrent users.

The reason this works is that that Qbix server allows apps to preload files and classes before it forks the worker processes. It can do this while being written in pure PHP.

While php-fpm can prefork workers, this causes each worker to take up a lot of memory, eg 40MB, duplicating all the bytecode from your entire framework and app. By contrast, Qbix Webserver is able to spawn workers that are around 140KB each for a typical Wordpress app. This is because pcntl_fork on Linux and MacOS only copies on write, so 4-16KB memory pages are only copied when you make a change to a variable. If all the variables are on one page (eg in one array) you can even have workers weighing 4-16KB total, allowing you to run TENS OF THOUSANDS of workers on a 4GB machine.

If you use composer install amphp, your code will use epoll instead, causing your app on Qbix Server to be even more efficient.

Second, the other features:

This is 2026. It would be great if your PHP was able to work with the latest socket.io and handle rooms and socket connections. Imagine a chat server that’s entirely in memory, and also able to handle 40,000 simultaneous users and connections.

Well, now you can. Qbix Webserver handles HTTP Requests, Websockets and rooms, even HTTP Push (for streaming AI tokens etc).

It also can manage your TLS certificates, run cron jobs, and more.

It supports headers like X-Accel-Redirect which lets you serve files with access control done by your app. (Though these aren’t as fast as nginx because PHP lacks support for sendfile, so if you want additional 2x boost in speed for protected static files, you should proxy these headers to NGINX. For public static files, just use a CDN.)

It even supports something new I invented, X-Cache-Tree allowing your code to cache parts of a webpage. Yes, that’s right — you are no longer required to render an entire page again if only a couple parts of it got invalidated. The X-Cache-Invalidate header can intelligently invalidate many pages at the same time!

How do I try it?

Visit qbixserver.com and grab the actual server. Launch it with PHP, and use the visual dashboard in your browser to manage your apps. Enjoy! It’s MIT licensed.

NuclearPM 2 days ago [–]

I like the idea of this, but PHP is such an ugly language.

# Scry — Give your agent the internet hypercube

## 评论（1/1）

> **NuclearPM** · 2026-09-17T23:48:21.000Z　
> I like the idea of this, but PHP is such an ugly language.

## 关联链接

- https://qbixserver.com

## 导航

- 项目页：[[10-项目/qbixserver.com_4df82498]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
