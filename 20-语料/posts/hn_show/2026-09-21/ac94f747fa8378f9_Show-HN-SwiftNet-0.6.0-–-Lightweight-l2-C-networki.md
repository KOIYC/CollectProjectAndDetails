---
type: "corpus"
item_id: "ac94f747fa8378f9"
title: "Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109422"
author: "morcules"
published_at: "2026-07-30T13:02:05Z"
captured_at: "2026-09-21T03:11:19+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_morcules
  - story_49109422
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)

> [!info] 一句话导读
> Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109422>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：morcules　|　发布：2026-07-30T13:02:05Z
> 项目链接：—
> 采集：2026-09-21T03:11:19+08:00　|　id：`ac94f747fa8378f9`

## 正文

Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK) | Hacker News

Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)

2 points by morcules 51 days ago | hide | past | favorite

SwiftNet is a small C networking library that works at Layer 2 with libpcap (and now has a very early DPDK implementation).

I built it because I was tired of using sockets or complex libraries and wanted something simple enough for my game while still being able to go fast using compile time customizations

0.6.0 changes: - Dynamic library build - Changed API in buffer functions - Simple DPDK implementation only usable right now with loopback - Cleaner source code - Built with maximum warnings enabled - Added write at offset function for buffer - Performance optimizations - Working on ubuntu linux arm64 - Added DISABLE_DYNAMIC_RATE_LIMITING flag

New version release: https://github.com/Morcules/SwiftNet/releases/tag/0.6.0 Repo: https://github.com/Morcules/SwiftNet

## 关联链接

- https://github.com/Morcules/SwiftNet
- https://github.com/Morcules/SwiftNet/releases/tag/0.6.0

## 导航

- 项目页：[[10-项目/Show-HN-SwiftNet-0.6.0-–-Lightweight-l2-C-networ_ac94f747]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
