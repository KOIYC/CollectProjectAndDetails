---
type: "corpus"
item_id: "14971fbb01368525"
title: "Show HN: Lightweight FUSE-based encrypted, compressed filesystem for Linux"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50585222"
project_url: "https://github.com/tgaloppo/obfusecate"
author: "tgaloppo"
published_at: "2026-11-21T02:17:25Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-21"
pub_day: "2026-11-21"
tags:
  - 语料
  - hn_show
  - author_tgaloppo
  - story_50585222
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Lightweight FUSE-based encrypted, compressed filesystem for Linux

> [!info] 一句话导读
> A personal project for digging deeper into Linux system programming, ObFUSEcate implements a file backed virtual block device that automatically performs compre…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50585222>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：tgaloppo　|　发布：2026-11-21T02:17:25Z
> 项目链接：<https://github.com/tgaloppo/obfusecate>
> 采集：2026-11-21T14:45:01+08:00　|　id：`14971fbb01368525`

## 正文

A personal project for digging deeper into Linux system programming, ObFUSEcate implements a file backed virtual block device that automatically performs compression and encryption as blocks are accessed. This virtual device can be mounted via FUSE (requiring no root privileges) to provide, effectively, a "live" compressed, encrypted archive.Written in C++, and intended to have minimal dependencies, it has custom 32 bit arithmetic encoding/decoding, ChaCha20-Poly1305 authenticated encryption, and CRC8 + XOR parity error-correction.

## 导航

- 项目页：[[10-项目/github.com_a8c68bdd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
