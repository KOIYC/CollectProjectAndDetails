---
type: "corpus"
item_id: "f2a3297f6356c54f"
title: "Show HN: Sill for Android – control your Mac's windows from an Android phone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50123065"
project_url: "https://github.com/rahimnathwani/sill-android"
author: "rahimnathwani"
published_at: "2026-10-16T19:13:22Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_rahimnathwani
  - story_50123065
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Sill for Android – control your Mac's windows from an Android phone

> [!info] 一句话导读
> Sill (discussed here: https://news.ycombinator.com/item?id=50112739) streams one Mac window, or the whole Desktop, to an iPhone or iPad and lets you control it …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50123065>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：rahimnathwani　|　发布：2026-10-16T19:13:22Z
> 项目链接：<https://github.com/rahimnathwani/sill-android>
> 采集：2026-10-17T13:35:15+08:00　|　id：`f2a3297f6356c54f`

## 正文

Sill (discussed here: https://news.ycombinator.com/item?id=50112739) streams one Mac window, or the whole Desktop, to an iPhone or iPad and lets you control it by touch. It's open source, so I made an Android client for it. It's unofficial and not affiliated with Sill's author: it speaks Sill's existing protocol, so the Mac side is the stock Sill app, unchanged.Install Sill on the Mac, sideload the APK from Releases onto an Android 11+ phone on the same Wi-Fi, tap your Mac in the list that shows on your phone, then look for the 12-digit code in Sill on your Mac, and type it into the Android app.Then: tap to click, drag to scroll, hold-and-drag to select text or move windows, pinch to zoom the picture on the phone, a Draw toggle for whiteboard apps like tldraw, and a key row with Esc, Tab, Cmd/Ctrl/Option/Shift and arrows. It also works over Tailscale with Sill's Remote Access.All of the code was written by Claude Code, working from Sill's Swift source and its Python test client; I tested it on a Pixel 9 Pro XL.Not done yet: drawing the Mac's pointer, a trackpad mode, clipboard sync, and a Play Store listing (I don't have Play developer account, and new individual Play developer accounts can't publish their first app until they've tested an app with a closed test with 12 testers.)(There's also a separate Android client in draft PR #89 on Sill's repo. This one is a standalone app with an installable APK. I should have checked the issues/PRs before I asked Claude to build this...)

## 评论（1/1）

> **t23414321** · 2026-10-17T00:22:22.000Z　
> That's client. There is Linux server:https://github.com/NateHag/Sill-Viewer/tree/main/linux-host - how it works.

## 关联链接

- https://news.ycombinator.com/item?id=50112739

## 导航

- 项目页：[[10-项目/github.com_caaa0f47]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
