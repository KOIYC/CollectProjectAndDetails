---
type: "corpus"
item_id: "050f584347fd3737"
title: "Show HN: Wl-pick – a live window picker for Sway"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49827956"
project_url: "https://mil.ad/blog/2026/wl-pick.html"
author: "playnext"
published_at: "2026-09-24T08:44:51Z"
captured_at: "2026-09-24T23:57:22+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-24"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_playnext
  - story_49827956
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Wl-pick – a live window picker for Sway

> [!info] 一句话导读
> CV Publications Blog Bookshelf

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49827956>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：playnext　|　发布：2026-09-24T08:44:51Z
> 项目链接：<https://mil.ad/blog/2026/wl-pick.html>
> 采集：2026-09-24T23:57:22+08:00　|　id：`050f584347fd3737`

## 正文

Milad Alizadeh
CV Publications Blog Bookshelf
wl-pick: a live window picker for Sway
Sep 21, 2026
I’ve had a keyboard-driven window switcher in my window manager for a long time. It started as a shell script piping i3’s window list into dmenu, and over the years I tweaked it slightly as I moved to Sway/Wayland and rofi .
That was enough until a new use case turned up: sharing a single window in a video call. Until recently Sway could only share a whole display, but sharing windows is now possile thanks to the xdg-desktop-portal-wlr backend, which lets you nominate an external program for picking the window. Browsers reach it through getDisplayMedia , which is handy for testing without having to join a call.
I could of course have used my dmenu-style script, but picking the right window out of a list of names is a bit of guesswork, and guessing in front of an audience is not fun. A visual chooser seemed like an obvious improvement.
My first attempt was to make rofi show me screenshots of all windows and displays. I put together a script using grim to take the screenshots, which can capture any window or display, including the ones that aren’t currently on screen. It worked, and it was decent, but it had two problems:
The previews weren’t live. Each thumbnail is frozen at the moment you launch the picker.
Launching it wasn’t instantaneous. Every preview meant capturing a full-resolution frame, encoding it, writing it to disk, then reading and scaling it again.
wl-pick
So I built wl-pick . It’s a small Rust program that shows a grid of live previews of every open window and display. Move around with the arrow keys or hjkl , press Enter, and it prints the selected window or output to stdout.
wl-pick just prints the selection, so what happens next is up to the caller. The common case is window switching:
swaymsg "[con_id= $( wl-pick --no-outputs | cut -f2 ) ] focus"
It can also be used as the screencast chooser, where --format portal prints what xdg-desktop-portal-wlr expects:
[screencast]
 chooser_type = simple
 chooser_cmd = wl-pick --format portal
How it works
The live previews rely on capture protocols that only landed in Sway recently. Sway 1.11 added the ext-image-copy-capture-v1 protocol for capturing outputs, and 1.12 extended it to individual windows.
The trick to making it fast is that wl-pick doesn’t draw anything. Each window’s capture buffer is handed straight back to the compositor as a subsurface, along with the rectangle it should be scaled into. So the same process that captured the window at full resolution is also the one that shrinks it to a thumbnail. wl-pick allocates the memory, passes the file descriptor around, and does the arithmetic; it never looks at a pixel.
What’s left is the capture itself, and that’s mostly bandwidth rather than computation. Keeping the previews live afterwards is nearly free, because the compositor only sends a new frame when a window’s content actually changes, so a screen full of idle terminals generates no new frames.
Installation
Install it with:
cargo install wl-pick

## 导航

- 项目页：[[10-项目/mil.ad_e26e8390]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
