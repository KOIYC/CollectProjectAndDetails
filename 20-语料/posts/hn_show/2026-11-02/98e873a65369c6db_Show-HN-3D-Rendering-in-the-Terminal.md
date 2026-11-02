---
type: "corpus"
item_id: "98e873a65369c6db"
title: "Show HN: 3D Rendering in the Terminal"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50327396"
project_url: "https://muratbayraktar.dev/blog/3d-rendering-in-the-terminal"
author: "bob65536"
published_at: "2026-11-01T17:00:11Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "内容/媒体"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_bob65536
  - story_50327396
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: 3D Rendering in the Terminal

> [!info] 一句话导读
> 3d Rendering in the Terminal

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50327396>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：bob65536　|　发布：2026-11-01T17:00:11Z
> 项目链接：<https://muratbayraktar.dev/blog/3d-rendering-in-the-terminal>
> 采集：2026-11-02T09:37:22+08:00　|　id：`98e873a65369c6db`

## 正文

Murat Bayraktar
 Toggle Theme
 Home
 Blog
 ← All posts
 3d Rendering in the Terminal
 2026-11-01 #coding
 I don’t want to leave the terminal for anything.
I like its simplicity. It forces me to be creative when making something in it, and for applications I use to strip out bloat and just give me something that works. I don’t like that Zen takes up 5gb of RAM every time I open it. I just want to use the terminal: it’s resource-efficient, debloated, and really fricking cool.
What if I want to see a 3d model?
Well, I could open up Carbonyl (or one of the other projects that spins up a browser), but at that point I have the same issue, don’t I? Still a bunch of CPU and RAM being wasted as a result a Chromium instance. I could also get a regular 3d model viewer, but then I wouldn’t exactly be in the terminal. As a Neovim user (wow who would have thought?), that’s not really acceptable.
dcat is my solution to this. It uses Assimp to support virtually any 3d file format and WGPU to display it without any performance issues. It has got textures, animations, Kitty Graphics Protocol, Sixel, fallbacks for old terminals, wireframe toggling, keyboard controls, mouse controls, and support on Windows, Mac, and Linux. It’s also a solution to see 3d models over SSH.
I’ve been developing the project for quite some time now, but I very recently switched it from C to Rust, which made cross-platform support a lot easier. There’s also a neovim plugin for this, which automatically runs dcat when you open a 3d model file.
← Older How do I Live?

## 评论（1/1）

> **bob65536** · 2026-11-01T18:32:43.000Z　
> Has textures, animations, keyboard and mouse controls, wireframe toggling, support for every 3d file format, terminal resize support, Kitty Graphics Protocol, Sixel, truecolor, palette colors, and monochrome colors to support almost any terminal.

## 导航

- 项目页：[[10-项目/muratbayraktar.dev_2cb6df4f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`内容/媒体`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
