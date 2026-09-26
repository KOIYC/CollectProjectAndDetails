---
type: "project"
title: "Show HN: I made a 3D rock climbing analysis tool using iPhone LiDAR [video]"
project_url: "https://github.com/jeremyipark/vision-demos"
first_seen: "2026-09-26T09:41:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_dr_blueberry
  - story_49849064
  - show_hn
lang: "en"
---

# Show HN: I made a 3D rock climbing analysis tool using iPhone LiDAR [video]

> [!info] 一句话导读
> Having learned a lot from sharing my previous rock climbing demos, I realized that a lot of rock climbing analysis is well-suited for 3D. Even something as simp…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/jeremyipark/vision-demos>
> 首次收录：2026-09-26T09:41:08+08:00
> 来源渠道：HN Show HN
> 标签：author_dr_blueberry, story_49849064, show_hn
> 最新指标：点赞=4 · 评论=2 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=4 · 评论=2 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-26/de50c4b3610fdda6_Show-HN-I-made-a-3D-rock-climbing-analysis-tool-us]] |

## 摘要正文

Having learned a lot from sharing my previous rock climbing demos, I realized that a lot of rock climbing analysis is well-suited for 3D. Even something as simple as supporting videos where the person filming moves with the climber requires 3D information.To get the depth information, I used my iPhone 15 Pro's LiDAR depth sensor through my local iPhone app. I recorded the video and depth measurements from my app, and I ran the rest of the analysis on my computer. I used ViTPose+ Large for pose estimation and SAM 3.1 to segment the holds, both models accessed through the VLM Run Gateway.I think the holds activation is better, and I like the final view of all of the holds in 3D. It's also interesting to see the distance traveled in meters. Plus, it looks cool and it feels like a video game.Let me know what you think!The analysis code is open-source on GitHub: https://github.com/jeremyipark/vision-demos
