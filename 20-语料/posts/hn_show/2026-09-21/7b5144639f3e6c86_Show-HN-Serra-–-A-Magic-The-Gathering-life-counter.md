---
type: "corpus"
item_id: "7b5144639f3e6c86"
title: "Show HN: Serra – A Magic: The Gathering life counter using DRM/KMS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47956840"
project_url: "https://git.sr.ht/~cmt/serra"
author: "nan60"
published_at: "2026-04-30T01:11:26Z"
captured_at: "2026-09-21T02:52:30+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_nan60
  - story_47956840
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Serra – A Magic: The Gathering life counter using DRM/KMS

> [!info] 一句话导读
> ~cmt/serra - Minimal life tracker designed for Magic: The Gathering - sourcehut git

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47956840>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：nan60　|　发布：2026-04-30T01:11:26Z
> 项目链接：<https://git.sr.ht/~cmt/serra>
> 采集：2026-09-21T02:52:30+08:00　|　id：`7b5144639f3e6c86`

## 正文

~cmt/serra - Minimal life tracker designed for Magic: The Gathering - sourcehut git

## ~cmt/serra

Minimal life tracker designed for Magic: The Gathering

1d21995a— Christian Thackston an hour ago

```
Initial commit
```

### refs

### clone

read-only https://git.sr.ht/~cmt/serra read/write git@git.sr.ht:~cmt/serra

Clone repo to your account

You can also use your local clone with git send-email.

```
Serra

A Magic: The Gathering life counter for minimal Linux touchscreen devices.
Supports 2-6 players. Built on raw kernel APIs (DRM/KMS + evdev) with no
desktop environment required.

Features
  - 2-6 players with automatic panel layout
  - Starting life of 20 or 40
  - Status bar showing system time and battery percentage

Requirements
  - Linux with DRM/KMS support
  - A touchscreen input device (/dev/input/event*)
  - Rust toolchain (for building)
  - User in the "video" and "input" groups, or an active logind session

Running
    Serra auto-detects the first DRM card and the first touchscreen input device.
You can override these with environment variables:

  SERRA_DRM        DRM device path         (default: /dev/dri/card0)
  SERRA_INPUT      Input event device path (default: auto-detected)
  SERRA_FONT_BOLD  Path to bold TTF font   (default: system font)
  SERRA_FONT       Path to regular TTF     (default: system font)

Serra looks for Liberation Sans and DejaVu Sans in common system font
directories. Set SERRA_FONT / SERRA_FONT_BOLD to use a specific font file instead.

No GTK, X11, Wayland, libinput, or udev required at runtime.

```

# manojmallick/sigmap

## 导航

- 项目页：[[10-项目/git.sr.ht_c719a113]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
