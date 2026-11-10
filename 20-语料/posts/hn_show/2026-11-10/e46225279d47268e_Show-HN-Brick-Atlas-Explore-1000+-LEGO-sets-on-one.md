---
type: "corpus"
item_id: "e46225279d47268e"
title: "Show HN: Brick Atlas: Explore 1000+ LEGO sets on one zoomable canvas"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50432776"
project_url: "https://showcase.zoomhub.net/ecommerce/brick-atlas"
author: "gasi"
published_at: "2026-11-09T21:52:44Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_gasi
  - story_50432776
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Brick Atlas: Explore 1000+ LEGO sets on one zoomable canvas

> [!info] 一句话导读
> Hello HN, I’m Daniel and I run ZoomHub, a small deep zoom image service.Most online catalogs look the same: There’s a grid of thumbnails, limited to about 20–50…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50432776>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：gasi　|　发布：2026-11-09T21:52:44Z
> 项目链接：<https://showcase.zoomhub.net/ecommerce/brick-atlas>
> 采集：2026-11-10T09:49:42+08:00　|　id：`e46225279d47268e`

## 正文

Hello HN, I’m Daniel and I run ZoomHub, a small deep zoom image service.Most online catalogs look the same: There’s a grid of thumbnails, limited to about 20–50 items, filters that refresh the page when activated, and pagination buttons to go to page 22 of 128.
It has always bothered me that you can’t see the whole collection and every action makes you wait and lose context.I built Brick Atlas to show it doesn’t have to be that way: You can browse 1000+ LEGO sets by zooming in, selecting a set, seeing different angles (at full resolution) and in the sidebar, the set’s piece count, price, etc. You can read the whole instructions (on some sets) without ever seeing a page refresh or losing your place. On a slow connection, the image simply gradually becomes sharper. Once you are done, you can zoom out and see all sets again. Apply a price filter to find gift ideas under $50 or switch to Real size layout to see how big the sets are in real life compared to each other. Toggle Box vs Built to switch between the retail box and the assembled set. For collectors, I added the scatter view to plot sets by piece count vs price so you can find the best value sets. Every change in filters or layout animates gently so you never lose the thread.I’ve been obsessed with zooming for almost twenty years. I interned at Zoomorama and later worked on the (Microsoft Live Labs) Seadragon team, in case this looks familiar to you :)The idea to use zoom and image streaming could be applied to photo galleries, a museum catalog, other products, or even scientific images. I just happened to pick LEGO because I’m an AFOL (adult fan of LEGO), have been wanting to explore their catalog like this for years, and hope there are lots of you who do too.I published this as a static data set to S3 behind CloudFront (700k WebP tiles) for performance and render it using OpenZoom, my own WebGL deep zoom engine. The data comes from Brickset (thanks to Huw, the founder, for his blessing) and the images from LEGO (also via Brickset). I used my ‘free’ Anthropic API credits from Ultra plan to classify images into box vs built, to extract tags and colors, etc. using Claude Haiku and Sonnet (spend: ~$60.)I’d love to hear how it feels to explore, what you’d do differently, and what collection you’d like to see this used with :)

## 导航

- 项目页：[[10-项目/showcase.zoomhub.net_256d22e7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
