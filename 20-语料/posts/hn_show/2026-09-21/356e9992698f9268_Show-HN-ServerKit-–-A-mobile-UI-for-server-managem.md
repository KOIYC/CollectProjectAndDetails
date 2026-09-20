---
type: "corpus"
item_id: "356e9992698f9268"
title: "Show HN: ServerKit – A mobile UI for server management"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733008"
project_url: "https://play.google.com/store/apps/details?id=com.iishanto.servermanager&hl=en_US"
author: "iishanto"
published_at: "2026-06-30T14:12:33Z"
captured_at: "2026-09-21T01:44:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_iishanto
  - story_48733008
  - show_hn
metrics: {"points": 5, "comments": 4, "engagement_velocity": 5}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:113d"
---

# Show HN: ServerKit – A mobile UI for server management

> [!info] 一句话导读
> A few months ago, I was outside of my city. I was on a bus when one of my team members messaged me saying users were unable to read the product description PDF.…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733008>
> 指标：点赞=5 · 评论=4 · engagement_velocity=5
> 作者：iishanto　|　发布：2026-06-30T14:12:33Z
> 项目链接：<https://play.google.com/store/apps/details?id=com.iishanto.servermanager&hl=en_US>
> 采集：2026-09-21T01:44:48+08:00　|　id：`356e9992698f9268`

## 正文

Problem Statement:
A few months ago, I was outside of my city. I was on a bus when one of my team members messaged me saying users were unable to read the product description PDF. I had to wait 3 more hours until I got back home, opened the laptop, and SSH'd into the server to find out what was wrong. In that moment I realized that being able to manage a server from a phone is very important when a laptop is not nearby.What it does:
It is a UI wrapper over standard SSH command outputs. It parses the SSH output and shows the results in UI elements, and also translates your actions to relevant SSH commands. This way users won't have to heavily rely on the command line – as we know, typing commands from a mobile device is also hard. However, it also has a terminal to allow you to do anything. It also supports Kubernetes, where you can see and manage pods, view logs and stats, and RDBMS to allow you to quickly perform database operations – a bit like phpMyAdmin or pgAdmin.Tech Stack: Flutter, SSH, Android Secured Storage, Firebase, DockerWhy Android:
I know – iOS is a major platform for this niche. But for now – as it is an MVP – I have decided to develop for Android to validate my idea and understand if it solves a real problem. The good news is, it does solve a real problem – at least the analytics say so. Within 30 days I got 5 premium users. About 30% of users connect their server and 23% of them use the app regularly. So now I am working on the iOS version.Current Limitations:
Currently the app only supports Ubuntu – other Debian based OSes are not tested, though they might work as well. The Kubernetes and AWS features need more testing. Also, ServerKit VPS Lab currently limits sessions to only 30 minutes TTL to prevent misuse.Feedback Request:
I would love your feedback on the VPS management and monitoring features, RDBMS features, and Kubernetes features. I also tried to keep the terminal simple, but your feedback on this is also valuable to me.Try it out:
If you don't want to connect your own VPS, you can test the app using ServerKit Lab. It will allow you 30 minutes of free VPS to test the app.
Install ServerKit: https://play.google.com/store/apps/details?id=com.iishanto.s...

## 评论（4/4）

> **sandcat_** · 2026-06-30T15:10:11.000Z　
> Unrelated, sorry:Curious. With my adblocker on, I don’t see a title on this post. Anyone else seeing this too? I couldn’t say which rule is doing it. (I’m on mobile, but I only use typical lists like EasyList etc.) First time I’ve had to disable my adblocker on HN!

---

> **chews** · 2026-06-30T17:39:32.000Z　
> is this just an android packaged version of this post? - https://news.ycombinator.com/item?id=48720758

---

> **iishanto** · 2026-06-30T15:52:27.000Z　
> I also encountered a brief issue while browsing incognito after posting this; the post temporarily disappeared. However, it is now resolved.

---

> **iishanto** · 2026-06-30T18:43:31.000Z　
> Different problem, not just a different platform. ServerKit is still SSH/CLI under the hood, just with a mobile UI so you can manage a server from your phone. Outer Shell replaces the terminal/browser paradigm entirely by shipping native GUI code over SSH. Same neighborhood, not a port of each other.

## 关联链接

- https://play.google.com/store/apps/details?id=com.iishanto.s...

## 导航

- 项目页：[[10-项目/play.google.com_b90ba3c3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
