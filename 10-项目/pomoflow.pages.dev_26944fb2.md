---
type: "project"
title: "Show HN: Pomoflow – a 1-bit Pomodoro with a todo list that syncs without sign-up"
project_url: "https://pomoflow.pages.dev/"
first_seen: "2026-10-17T13:35:15+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rochansinha
  - story_50125084
  - show_hn
lang: "en"
---

# Show HN: Pomoflow – a 1-bit Pomodoro with a todo list that syncs without sign-up

> [!info] 一句话导读
> Pomoflow is (yet another) Pomodoro app in a 1-bit style inspired by the early Macintosh GUI. It also has a todo list you can sync between your devices without h…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://pomoflow.pages.dev/>
> 首次收录：2026-10-17T13:35:15+08:00
> 来源渠道：HN Show HN
> 标签：author_rochansinha, story_50125084, show_hn
> 最新指标：点赞=2 · 评论=2 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-17T13:35:15+08:00 | HN Show HN | 点赞=2 · 评论=2 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-17/faae8a3ea0b5503c_Show-HN-Pomoflow-–-a-1-bit-Pomodoro-with-a-todo-li]] |

## 摘要正文

Pomoflow is (yet another) Pomodoro app in a 1-bit style inspired by the early Macintosh GUI. It also has a todo list you can sync between your devices without having to login to an account. A jukebox loads and plays your favourite YouTube playlists. And there are bonus weekly focus stats for the numberphiles among us.I built this because I wanted three things in one place: a pomodoro timer that looks good, a task list that syncs across my devices without an account (the apps I tried kept putting sync behind a login or a paywall), and my YT playlists I could play without having to leave the tab.A little more detail on the no-account task list syncing- To sync tasks you generate a random 128-bit key and paste the key or scan a QR code on the other device. The pairing link carries the key in the URL fragment, so the browser never sends it to the server, and the server stores only a SHA-256 hash of it. Anyone with the key can read and edit the list. Without a key, tasks stay in the browser.
