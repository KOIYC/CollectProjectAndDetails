---
type: "project"
title: "Show HN: Luksmith – Mount LUKS Ext4 Drives Natively in Finder on Apple Silicon"
project_url: "https://luksmith.app/"
first_seen: "2026-10-16T09:35:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_baytizzel
  - story_50111381
  - show_hn
lang: "en"
---

# Show HN: Luksmith – Mount LUKS Ext4 Drives Natively in Finder on Apple Silicon

> [!info] 一句话导读
> I’ve recently moved over to macOS this summer and previously I heavily used Linux (still do as I have a homeserver running Arch and Omarchy Thinkpad for fun). I…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://luksmith.app/>
> 首次收录：2026-10-16T09:35:18+08:00
> 来源渠道：HN Show HN
> 标签：author_baytizzel, story_50111381, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-16/7482408768c6353c_Show-HN-Luksmith-–-Mount-LUKS-Ext4-Drives-Natively]] |

## 摘要正文

I’ve recently moved over to macOS this summer and previously I heavily used Linux (still do as I have a homeserver running Arch and Omarchy Thinkpad for fun). I have a few LUKS Encrypted hard drives with photos I wanted on my Mac and then quickly realized that there’s no native way to open the drive.So I spent some time to make luksmith, essentially decrypting the luks drive, mounting the underlying EXT4 drive and using Apple’s Userland FSKit Library to make it appear in the finder window to make it as close to home on a Mac as I can (with journaling caveats because I can’t control which order writes happen in).It’s completely free to read and copy files from the drive if you try it out ‘brew install --cask betizzel/luksmith/luksmac’. And $9.99 one time purchase to unlock writing to the drive. No account needed, no telemetry shared back to me, no network connections made.Requires Apple Silicon + macOS 26. Full format support and limitations here: [https://luksmith.app/#formats](https://luksmith.app/#formats)available on the appstore: https://apps.apple.com/us/app/luksmith/id6806869711?mt=12and the website: https://luksmith.app/#formats
