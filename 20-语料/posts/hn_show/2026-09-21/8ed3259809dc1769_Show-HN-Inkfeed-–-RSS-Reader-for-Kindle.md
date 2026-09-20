---
type: "corpus"
item_id: "8ed3259809dc1769"
title: "Show HN: Inkfeed – RSS Reader for Kindle"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48325703"
project_url: "https://inkfeed.xyz/"
author: "adhamsalama"
published_at: "2026-05-29T16:44:20Z"
captured_at: "2026-09-21T01:44:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_adhamsalama
  - story_48325703
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: Inkfeed – RSS Reader for Kindle

> [!info] 一句话导读
> Hello.The Kindle is my favorite device and I read a lot on it, but I also like reading RSS feeds, which aren't supported on the Kindle.This requires me to eithe…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48325703>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：adhamsalama　|　发布：2026-05-29T16:44:20Z
> 项目链接：<https://inkfeed.xyz/>
> 采集：2026-09-21T01:44:01+08:00　|　id：`8ed3259809dc1769`

## 正文

Hello.The Kindle is my favorite device and I read a lot on it, but I also like reading RSS feeds, which aren't supported on the Kindle.This requires me to either download the article and copy it to my Kindle (using Calibre) or sending it via Amazon's Send To Kindle feature. I dislike both options.I wanted to read RSS feeds just like I read books on my Kindle, so I (with the help of Claude) built a web-based RSS reader that's compatible with the Kindle's experimental browser (tested on PaperWhite 11). It doesn't use any JS frameworks for maximum compatibility.This RSS reader allows you to read feeds directly on the Kindle's browser, and you can also download the article directly on your Kindle or email it to yourself.Initially it was a just a simple RSS reader using a CORS proxy, and saved RSS feeds and user preferences like font size to local storage, but the Kindle browser clears local storage after a while, so I decided to add a backend to save them, then I thought why stop here?So I added the ability to email the article to yourself in case you want to add it to your Kindle library. A user tried Inkfeed and suggested I add the ability to browse Wikipedia, so I implemented that too. You can search for Wikipedia article, read them and download them on directly on your Kindle using Inkfeed.You can still use it without the backend if you toggle "Backend mode" OFF in the settings, so that it truly does everything on your Kindle (except that it relies on a CORS proxy to fetch feeds).I deployed the backend (Go + SQLite) on a Hetzner VPS (2 vCPU, 4GB RAM, 40GB SSD) that costs me $4 a month, and SSL is handled by Caddy.The code is free and open source.Here's the repo: https://github.com/adhamsalama/inkfeedI'd love to hear your feedback, and I also need people with older Kindle generations to test the JavaScript compatibility.

## 评论（1/1）

> **adhamsalama** · 2026-05-29T16:56:09.000Z　
> And just after I posted this I discover a horizontal line my Kindle screen...
> Guess I jinxed it...

## 关联链接

- https://github.com/adhamsalama/inkfeedI

## 导航

- 项目页：[[10-项目/inkfeed.xyz_4da65d1e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
