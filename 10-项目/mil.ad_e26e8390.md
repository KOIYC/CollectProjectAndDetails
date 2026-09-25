---
type: "project"
title: "Show HN: Wl-pick – a live window picker for Sway"
project_url: "https://mil.ad/blog/2026/wl-pick.html"
first_seen: "2026-09-24T23:57:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_playnext
  - story_49827956
  - show_hn
lang: "en"
---

# Show HN: Wl-pick – a live window picker for Sway

> [!info] 一句话导读
> CV Publications Blog Bookshelf

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://mil.ad/blog/2026/wl-pick.html>
> 首次收录：2026-09-24T23:57:22+08:00
> 来源渠道：HN Show HN
> 标签：author_playnext, story_49827956, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-24/050f584347fd3737_Show-HN-Wl-pick-–-a-live-window-picker-for-Sway]] |

## 摘要正文

Milad Alizadeh CV Publications Blog Bookshelf wl-pick: a live window picker for Sway Sep 21, 2026 I’ve had a keyboard-driven window switcher in my window manager for a long time. It started as a shell script piping i3’s window list into dmenu, and over the years I tweaked it slightly as I moved to Sway/Wayland and rofi . That was enough until a new use case turned up: sharing a single window in a video call. Until recently Sway could only share a whole display, but sharing windows is now possile thanks to the xdg-desktop-portal-wlr backend, which lets you nominate an external program for picking the window. Browsers reach it through getDisplayMedia , which is handy for testing without having to join a call. I could of course have used my dmenu-style script, but picking the right window out of a list of names is a bit of guesswork, and guessing in front of an audience is not fun. A visual chooser seemed like an obvious improvement. My first attempt was to make rofi show me screenshots of all windows and displays. I put together a script using grim to take the screenshots, which can capture any window or display, including the ones that aren’t currently on screen. It worked, and it w…
