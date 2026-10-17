---
type: "corpus"
item_id: "7482408768c6353c"
title: "Show HN: Luksmith – Mount LUKS Ext4 Drives Natively in Finder on Apple Silicon"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50111381"
project_url: "https://luksmith.app/"
author: "baytizzel"
published_at: "2026-10-15T22:39:32Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "内容/媒体"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_baytizzel
  - story_50111381
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Luksmith – Mount LUKS Ext4 Drives Natively in Finder on Apple Silicon

> [!info] 一句话导读
> I’ve recently moved over to macOS this summer and previously I heavily used Linux (still do as I have a homeserver running Arch and Omarchy Thinkpad for fun). I…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50111381>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：baytizzel　|　发布：2026-10-15T22:39:32Z
> 项目链接：<https://luksmith.app/>
> 采集：2026-10-16T09:35:18+08:00　|　id：`7482408768c6353c`

## 正文

I’ve recently moved over to macOS this summer and previously I heavily used Linux (still do as I have a homeserver running Arch and Omarchy Thinkpad for fun). I have a few LUKS Encrypted hard drives with photos I wanted on my Mac and then quickly realized that there’s no native way to open the drive.So I spent some time to make luksmith, essentially decrypting the luks drive, mounting the underlying EXT4 drive and using Apple’s Userland FSKit Library to make it appear in the finder window to make it as close to home on a Mac as I can (with journaling caveats because I can’t control which order writes happen in).It’s completely free to read and copy files from the drive if you try it out ‘brew install --cask betizzel/luksmith/luksmac’. And $9.99 one time purchase to unlock writing to the drive. No account needed, no telemetry shared back to me, no network connections made.Requires Apple Silicon + macOS 26. Full format support and limitations here: [https://luksmith.app/#formats](https://luksmith.app/#formats)available on the appstore: https://apps.apple.com/us/app/luksmith/id6806869711?mt=12and the website: https://luksmith.app/#formats

## 关联链接

- https://apps.apple.com/us/app/luksmith/id6806869711?mt=12and
- https://luksmith.app/#formats

## 导航

- 项目页：[[10-项目/luksmith.app_8e4eee4b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`内容/媒体`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
