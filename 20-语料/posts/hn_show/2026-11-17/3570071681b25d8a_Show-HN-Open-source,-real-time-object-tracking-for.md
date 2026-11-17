---
type: "corpus"
item_id: "3570071681b25d8a"
title: "Show HN: Open-source, real-time object tracking for live video feeds"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50523377"
project_url: "https://github.com/aryamandarda/tamserve"
author: "aryaman_darda"
published_at: "2026-11-16T21:14:39Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_aryaman_darda
  - story_50523377
  - show_hn
metrics: {"points": 13, "comments": 2, "engagement_velocity": 13}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Open-source, real-time object tracking for live video feeds

> [!info] 一句话导读
> I type "forklift" on a live warehouse camera, and tamserve finds and tracks both forklifts, including the one driving in. Then I add "person" without stopping i…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50523377>
> 指标：点赞=13 · 评论=2 · engagement_velocity=13
> 作者：aryaman_darda　|　发布：2026-11-16T21:14:39Z
> 项目链接：<https://github.com/aryamandarda/tamserve>
> 采集：2026-11-17T11:09:12+08:00　|　id：`3570071681b25d8a`

## 正文

I type "forklift" on a live warehouse camera, and tamserve finds and tracks both forklifts, including the one driving in. Then I add "person" without stopping it.tamserve runs Meta's SAM 3 on live camera feeds. SAM 3's own tracker handles one recorded video at a time, runs at about 8 fps, and runs out of memory on long videos. tamserve uses SAM 3 to find objects every few frames and a lightweight tracker (EdgeTAM) to follow them in between, with one copy of each model shared across all your cameras.*On one RTX 4090:** *Any object you name:* 4x faster than SAM 3's tracker, at 92% of its accuracy
* *People:* 16 cameras at once, 14x less GPU per frame, and slightly more accurate than SAM 3 (89.6 vs 87.8 HOTA)
* *Memory:* flat at 3.5 GB on a 3,000 frame video, where SAM 3 runs out at frame 423*Worth a look if you're building:** Warehouse or factory safety (forklifts, pallets, hard hats)
* Security or retail camera analytics
* Home or elder care monitoring
* Robotics, wildlife or lab monitoring
* Annotation tools for long videos`pip install "tamserve[sam3]"`Please give me any and all feedback or edit tamserve to meet your needs, and a star helps if you find it useful!

## 评论（2/2）

> **sroussey** · 2026-11-17T02:19:06.000Z　
> Nice. You should check this out, not by me and different model, but handling live video and runs in the browser.https://huggingface.co/posts/Xenova/448209562329557

---

> **aryaman_darda** · 2026-11-17T03:04:56.000Z　
> Thanks will do!

## 导航

- 项目页：[[10-项目/github.com_ac7ebcb5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
