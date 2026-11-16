---
type: "corpus"
item_id: "16e88cb235aa0f52"
title: "Show HN: WallHang – Plan a gallery wall and get exact nail positions (iOS)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50444909"
project_url: "https://wallhang.app/"
author: "morrowfield"
published_at: "2026-11-10T19:18:18Z"
captured_at: "2026-11-11T13:37:17+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-11"
pub_day: "2026-11-10"
tags:
  - 语料
  - hn_show
  - author_morrowfield
  - story_50444909
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: WallHang – Plan a gallery wall and get exact nail positions (iOS)

> [!info] 一句话导读
> I had been staring at some of the empty walls in my home and wanted to put up some frames but was always worried about the right measurements on where to put th…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50444909>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：morrowfield　|　发布：2026-11-10T19:18:18Z
> 项目链接：<https://wallhang.app/>
> 采集：2026-11-11T13:37:17+08:00　|　id：`16e88cb235aa0f52`

## 正文

I had been staring at some of the empty walls in my home and wanted to put up some frames but was always worried about the right measurements on where to put the holes, you can enter the size of the wall and the frames that you already have or planning to buy, or pick from your iphone gallery(photo library is used to show your artwork inside a frame) choose the layout and it will tell where you need to drill the holes measured from the floor and left edge of the wall, see the frames on your real wall with AR. The math accounts for wires drop, d-rings which need two nails at the same height. Built in SwiftUI. I have used RealityKit for the AR preview. The math turned out to be a bit trickier than I had thought. A frame usually doesn’t hang from its top edge since wire pulls up into a point below the top and D-rings need two nails at the same height and if you measure each frame from the one next to it then small errors add up. So had to account for measuring every nail from the floor and the same wall corner.

## 导航

- 项目页：[[10-项目/wallhang.app_7db1ac5a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
