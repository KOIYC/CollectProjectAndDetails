---
type: "project"
title: "Show HN: Sill for Android – control your Mac's windows from an Android phone"
project_url: "https://github.com/rahimnathwani/sill-android"
first_seen: "2026-10-17T13:35:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rahimnathwani
  - story_50123065
  - show_hn
lang: "en"
---

# Show HN: Sill for Android – control your Mac's windows from an Android phone

> [!info] 一句话导读
> Sill (discussed here: https://news.ycombinator.com/item?id=50112739) streams one Mac window, or the whole Desktop, to an iPhone or iPad and lets you control it …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/rahimnathwani/sill-android>
> 首次收录：2026-10-17T13:35:15+08:00
> 来源渠道：HN Show HN
> 标签：author_rahimnathwani, story_50123065, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-17T13:35:15+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-10-17/f2a3297f6356c54f_Show-HN-Sill-for-Android-–-control-your-Mac's-wind]] |

## 摘要正文

Sill (discussed here: https://news.ycombinator.com/item?id=50112739) streams one Mac window, or the whole Desktop, to an iPhone or iPad and lets you control it by touch. It's open source, so I made an Android client for it. It's unofficial and not affiliated with Sill's author: it speaks Sill's existing protocol, so the Mac side is the stock Sill app, unchanged.Install Sill on the Mac, sideload the APK from Releases onto an Android 11+ phone on the same Wi-Fi, tap your Mac in the list that shows on your phone, then look for the 12-digit code in Sill on your Mac, and type it into the Android app.Then: tap to click, drag to scroll, hold-and-drag to select text or move windows, pinch to zoom the picture on the phone, a Draw toggle for whiteboard apps like tldraw, and a key row with Esc, Tab, Cmd/Ctrl/Option/Shift and arrows. It also works over Tailscale with Sill's Remote Access.All of the code was written by Claude Code, working from Sill's Swift source and its Python test client; I tested it on a Pixel 9 Pro XL.Not done yet: drawing the Mac's pointer, a trackpad mode, clipboard sync, and a Play Store listing (I don't have Play developer account, and new individual Play developer acc…
