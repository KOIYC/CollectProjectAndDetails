---
type: "project"
title: "Show HN: Open-source, real-time object tracking for live video feeds"
project_url: "https://github.com/aryamandarda/tamserve"
first_seen: "2026-11-17T11:09:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_aryaman_darda
  - story_50523377
  - show_hn
lang: "en"
---

# Show HN: Open-source, real-time object tracking for live video feeds

> [!info] 一句话导读
> I type "forklift" on a live warehouse camera, and tamserve finds and tracks both forklifts, including the one driving in. Then I add "person" without stopping i…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/aryamandarda/tamserve>
> 首次收录：2026-11-17T11:09:12+08:00
> 来源渠道：HN Show HN
> 标签：author_aryaman_darda, story_50523377, show_hn
> 最新指标：点赞=13 · 评论=2 · engagement_velocity=13

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-17T11:09:12+08:00 | HN Show HN | 点赞=13 · 评论=2 · engagement_velocity=13 | [[20-语料/posts/hn_show/2026-11-17/3570071681b25d8a_Show-HN-Open-source,-real-time-object-tracking-for]] |

## 摘要正文

I type "forklift" on a live warehouse camera, and tamserve finds and tracks both forklifts, including the one driving in. Then I add "person" without stopping it.tamserve runs Meta's SAM 3 on live camera feeds. SAM 3's own tracker handles one recorded video at a time, runs at about 8 fps, and runs out of memory on long videos. tamserve uses SAM 3 to find objects every few frames and a lightweight tracker (EdgeTAM) to follow them in between, with one copy of each model shared across all your cameras.*On one RTX 4090:** *Any object you name:* 4x faster than SAM 3's tracker, at 92% of its accuracy * *People:* 16 cameras at once, 14x less GPU per frame, and slightly more accurate than SAM 3 (89.6 vs 87.8 HOTA) * *Memory:* flat at 3.5 GB on a 3,000 frame video, where SAM 3 runs out at frame 423*Worth a look if you're building:** Warehouse or factory safety (forklifts, pallets, hard hats) * Security or retail camera analytics * Home or elder care monitoring * Robotics, wildlife or lab monitoring * Annotation tools for long videos`pip install "tamserve[sam3]"`Please give me any and all feedback or edit tamserve to meet your needs, and a star helps if you find it useful!
