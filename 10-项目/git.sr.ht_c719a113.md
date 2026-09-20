---
type: "project"
title: "Show HN: Serra – A Magic: The Gathering life counter using DRM/KMS"
project_url: "https://git.sr.ht/~cmt/serra"
first_seen: "2026-09-21T02:52:30+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_nan60
  - story_47956840
  - show_hn
lang: "en"
---

# Show HN: Serra – A Magic: The Gathering life counter using DRM/KMS

> [!info] 一句话导读
> ~cmt/serra - Minimal life tracker designed for Magic: The Gathering - sourcehut git

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://git.sr.ht/~cmt/serra>
> 首次收录：2026-09-21T02:52:30+08:00
> 来源渠道：HN Show HN
> 标签：author_nan60, story_47956840, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/7b5144639f3e6c86_Show-HN-Serra-–-A-Magic-The-Gathering-life-counter]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/7b5144639f3e6c86_Show-HN-Serra-–-A-Magic-The-Gathering-life-counter]] |
| 2026-09-21T02:52:30+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/7b5144639f3e6c86_Show-HN-Serra-–-A-Magic-The-Gathering-life-counter]] |

## 摘要正文

~cmt/serra - Minimal life tracker designed for Magic: The Gathering - sourcehut git  ## ~cmt/serra  Minimal life tracker designed for Magic: The Gathering  1d21995a— Christian Thackston an hour ago  ``` Initial commit ```  ### refs  ### clone  read-only https://git.sr.ht/~cmt/serra read/write git@git.sr.ht:~cmt/serra  Clone repo to your account  You can also use your local clone with git send-email.  ``` Serra  A Magic: The Gathering life counter for minimal Linux touchscreen devices. Supports 2-6 players. Built on raw kernel APIs (DRM/KMS + evdev) with no desktop environment required.  Features   - 2-6 players with automatic panel layout   - Starting life of 20 or 40   - Status bar showing system time and battery percentage  Requirements   - Linux with DRM/KMS support   - A touchscreen input device (/dev/input/event*)   - Rust toolchain (for building)   - User in the "video" and "input" groups, or an active logind session  Running     Serra auto-detects the first DRM card and the first touchscreen input device. You can override these with environment variables:    SERRA_DRM        DRM device path         (default: /dev/dri/card0)   SERRA_INPUT      Input event device path (default…
