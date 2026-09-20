---
type: "project"
title: "Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)"
project_url: "https://news.ycombinator.com/item?id=49109422"
first_seen: "2026-09-21T03:11:19+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_morcules
  - story_49109422
  - show_hn
lang: "en"
---

# Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)

> [!info] 一句话导读
> Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://news.ycombinator.com/item?id=49109422>
> 首次收录：2026-09-21T03:11:19+08:00
> 来源渠道：HN Show HN
> 标签：author_morcules, story_49109422, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/ac94f747fa8378f9_Show-HN-SwiftNet-0.6.0-–-Lightweight-l2-C-networki]] |
| 2026-09-21T03:11:19+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/ac94f747fa8378f9_Show-HN-SwiftNet-0.6.0-–-Lightweight-l2-C-networki]] |

## 摘要正文

Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK) | Hacker News  Show HN: SwiftNet 0.6.0 – Lightweight l2 C networking lib (pcap and early DPDK)  2 points by morcules 51 days ago | hide | past | favorite  SwiftNet is a small C networking library that works at Layer 2 with libpcap (and now has a very early DPDK implementation).  I built it because I was tired of using sockets or complex libraries and wanted something simple enough for my game while still being able to go fast using compile time customizations  0.6.0 changes: - Dynamic library build - Changed API in buffer functions - Simple DPDK implementation only usable right now with loopback - Cleaner source code - Built with maximum warnings enabled - Added write at offset function for buffer - Performance optimizations - Working on ubuntu linux arm64 - Added DISABLE_DYNAMIC_RATE_LIMITING flag  New version release: https://github.com/Morcules/SwiftNet/releases/tag/0.6.0 Repo: https://github.com/Morcules/SwiftNet
