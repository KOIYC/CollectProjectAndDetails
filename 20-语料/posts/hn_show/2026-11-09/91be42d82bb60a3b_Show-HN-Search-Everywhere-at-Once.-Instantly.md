---
type: "corpus"
item_id: "91be42d82bb60a3b"
title: "Show HN: Search Everywhere at Once. Instantly"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50415469"
project_url: "https://antisoftworks.com/antifind"
author: "civnode"
published_at: "2026-11-08T17:56:10Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_civnode
  - story_50415469
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Search Everywhere at Once. Instantly

> [!info] 一句话导读
> I've made AntiFind, to allow you to search everywhere at once, vastly increasing the efficiency of LLMs and your own searches:AntiFind indexes filesystems, not …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50415469>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：civnode　|　发布：2026-11-08T17:56:10Z
> 项目链接：<https://antisoftworks.com/antifind>
> 采集：2026-11-09T09:39:29+08:00　|　id：`91be42d82bb60a3b`

## 正文

I've made AntiFind, to allow you to search everywhere at once, vastly increasing the efficiency of LLMs and your own searches:AntiFind indexes filesystems, not folders.It maintains a live view of storage by reading filesystem metadata directly. Because it understands the underlying filesystems, it can search across storage that the operating system is not currently exposing, including unmounted partitions.Allowing you to search for and play media from Linux in your Windows and the other way around. Without mounting the drives.This works on Linux, Windows and MacOS.The underlying idea is simple: instead of walking directories, read the filesystem's file tables directly.Most tools discover the filesystem again every time you search. AntiFind reads the drive's metadata in one pass and then follows changes as they happen.AntiFind supports Windows, Linux and macOS. It includes both a GUI and a command line. The CLI supports JSON output (--json) and was designed to integrate cleanly with automation and LLM workflows.There's a lot more to it, and you can find timings on my site, but that's the core idea.More information: https://antisoftworks.com/antifindCheers!

## 关联链接

- https://antisoftworks.com/antifindCheers!

## 导航

- 项目页：[[10-项目/antisoftworks.com_e8de21af]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
