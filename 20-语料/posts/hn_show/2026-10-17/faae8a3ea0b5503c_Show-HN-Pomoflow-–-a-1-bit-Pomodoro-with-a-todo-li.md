---
type: "corpus"
item_id: "faae8a3ea0b5503c"
title: "Show HN: Pomoflow – a 1-bit Pomodoro with a todo list that syncs without sign-up"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50125084"
project_url: "https://pomoflow.pages.dev/"
author: "rochansinha"
published_at: "2026-10-16T21:36:28Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_rochansinha
  - story_50125084
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pomoflow – a 1-bit Pomodoro with a todo list that syncs without sign-up

> [!info] 一句话导读
> Pomoflow is (yet another) Pomodoro app in a 1-bit style inspired by the early Macintosh GUI. It also has a todo list you can sync between your devices without h…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50125084>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：rochansinha　|　发布：2026-10-16T21:36:28Z
> 项目链接：<https://pomoflow.pages.dev/>
> 采集：2026-10-17T13:35:15+08:00　|　id：`faae8a3ea0b5503c`

## 正文

Pomoflow is (yet another) Pomodoro app in a 1-bit style inspired by the early Macintosh GUI. It also has a todo list you can sync between your devices without having to login to an account. A jukebox loads and plays your favourite YouTube playlists. And there are bonus weekly focus stats for the numberphiles among us.I built this because I wanted three things in one place: a pomodoro timer that looks good, a task list that syncs across my devices without an account (the apps I tried kept putting sync behind a login or a paywall), and my YT playlists I could play without having to leave the tab.A little more detail on the no-account task list syncing- To sync tasks you generate a random 128-bit key and paste the key or scan a QR code on the other device. The pairing link carries the key in the URL fragment, so the browser never sends it to the server, and the server stores only a SHA-256 hash of it. Anyone with the key can read and edit the list. Without a key, tasks stay in the browser.

## 评论（2/2）

> **rochansinha** · 2026-10-16T21:36:53.000Z　
> Here's the github repo if you want to explore more- https://github.com/amoslives/pomoflow

---

> **kooi** · 2026-10-16T21:46:28.000Z　
> Very cool.I'm excited for my Clicks Communicator to come in. I'd love to try to connect this to a hot-key for easy access.

## 导航

- 项目页：[[10-项目/pomoflow.pages.dev_26944fb2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
