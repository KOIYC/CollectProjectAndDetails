---
type: "corpus"
item_id: "de50c4b3610fdda6"
title: "Show HN: I made a 3D rock climbing analysis tool using iPhone LiDAR [video]"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49849064"
project_url: "https://github.com/jeremyipark/vision-demos"
author: "dr_blueberry"
published_at: "2026-09-25T19:48:59Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_dr_blueberry
  - story_49849064
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: I made a 3D rock climbing analysis tool using iPhone LiDAR [video]

> [!info] 一句话导读
> Having learned a lot from sharing my previous rock climbing demos, I realized that a lot of rock climbing analysis is well-suited for 3D. Even something as simp…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49849064>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：dr_blueberry　|　发布：2026-09-25T19:48:59Z
> 项目链接：<https://github.com/jeremyipark/vision-demos>
> 采集：2026-09-26T09:41:08+08:00　|　id：`de50c4b3610fdda6`

## 正文

Having learned a lot from sharing my previous rock climbing demos, I realized that a lot of rock climbing analysis is well-suited for 3D. Even something as simple as supporting videos where the person filming moves with the climber requires 3D information.To get the depth information, I used my iPhone 15 Pro's LiDAR depth sensor through my local iPhone app. I recorded the video and depth measurements from my app, and I ran the rest of the analysis on my computer. I used ViTPose+ Large for pose estimation and SAM 3.1 to segment the holds, both models accessed through the VLM Run Gateway.I think the holds activation is better, and I like the final view of all of the holds in 3D. It's also interesting to see the distance traveled in meters. Plus, it looks cool and it feels like a video game.Let me know what you think!The analysis code is open-source on GitHub: https://github.com/jeremyipark/vision-demos

## 评论（2/2）

> **haimhm** · 2026-09-25T19:50:57.000Z　
> nice

---

> **fzysingularity** · 2026-09-25T21:03:35.000Z　
> Is the LiDAR sufficiently accurate at those distances?

## 导航

- 项目页：[[10-项目/github.com_915b2e58]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
