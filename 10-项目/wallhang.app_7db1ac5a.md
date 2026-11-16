---
type: "project"
title: "Show HN: WallHang – Plan a gallery wall and get exact nail positions (iOS)"
project_url: "https://wallhang.app/"
first_seen: "2026-11-11T13:37:17+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_morrowfield
  - story_50444909
  - show_hn
lang: "en"
---

# Show HN: WallHang – Plan a gallery wall and get exact nail positions (iOS)

> [!info] 一句话导读
> I had been staring at some of the empty walls in my home and wanted to put up some frames but was always worried about the right measurements on where to put th…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://wallhang.app/>
> 首次收录：2026-11-11T13:37:17+08:00
> 来源渠道：HN Show HN
> 标签：author_morrowfield, story_50444909, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-11T13:37:17+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-11/16e88cb235aa0f52_Show-HN-WallHang-–-Plan-a-gallery-wall-and-get-exa]] |

## 摘要正文

I had been staring at some of the empty walls in my home and wanted to put up some frames but was always worried about the right measurements on where to put the holes, you can enter the size of the wall and the frames that you already have or planning to buy, or pick from your iphone gallery(photo library is used to show your artwork inside a frame) choose the layout and it will tell where you need to drill the holes measured from the floor and left edge of the wall, see the frames on your real wall with AR. The math accounts for wires drop, d-rings which need two nails at the same height. Built in SwiftUI. I have used RealityKit for the AR preview. The math turned out to be a bit trickier than I had thought. A frame usually doesn’t hang from its top edge since wire pulls up into a point below the top and D-rings need two nails at the same height and if you measure each frame from the one next to it then small errors add up. So had to account for measuring every nail from the floor and the same wall corner.
