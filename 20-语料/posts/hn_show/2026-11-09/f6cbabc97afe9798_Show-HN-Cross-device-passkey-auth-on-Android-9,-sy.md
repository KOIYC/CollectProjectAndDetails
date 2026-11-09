---
type: "corpus"
item_id: "f6cbabc97afe9798"
title: "Show HN: Cross-device passkey auth on Android 9, synced with Bitwarden"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50413568"
project_url: "https://rsnel.github.io/passkeychain"
author: "riksnel"
published_at: "2026-11-08T14:16:27Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_riksnel
  - story_50413568
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Cross-device passkey auth on Android 9, synced with Bitwarden

> [!info] 一句话导读
> I saw a colleague log in to a website on my laptop by scanning a FIDO QR code. I wanted to do the same, but couldn't find a way to use the passkeys stored in Bi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50413568>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：riksnel　|　发布：2026-11-08T14:16:27Z
> 项目链接：<https://rsnel.github.io/passkeychain>
> 采集：2026-11-09T09:39:29+08:00　|　id：`f6cbabc97afe9798`

## 正文

I saw a colleague log in to a website on my laptop by scanning a FIDO QR code. I wanted to do the same, but couldn't find a way to use the passkeys stored in Bitwarden on my phone to log in.So I asked Claude to build me an app. Claude found the task too daunting and only wanted to create a skeleton app. I was surprised by how complex the system actually is. Part of the process involves the phone sending an encrypted Bluetooth message as proof of presence, along with instructions on how to proceed.With the help of DeepSeek's free chat, I eventually managed to create a working implementation, after chasing quite a few hallucinations and dead ends... Claude then polished the app for me.The repository includes a full specification with test vectors, and the website has a nice, accessible explanation of how the process works.

## 评论（1/1）

> **evanjrowley** · 2026-11-08T15:25:02.000Z　
> I'll try it. I've been looking for innovative passkey options for Android.One paint point with the Retroid Pocket 6, Nova, and (likely) the Duo, is they just don't support Passkeys. At least, this is how it seems. I've installed multiple Passkey-capable apps, tried with multiple web browsers, on multiple Passkey auth portals, and the passkey has never been detected. (This might be something I can solve with ADB and an LLM. Maybe that's all it is.)The point is, the passkey situation for many devices is suboptimal, and novel options like this could fill in an important gap. The gap is growing wider as Android handhelds with odd Android versions have grown in popularity.

## 导航

- 项目页：[[10-项目/rsnel.github.io_d7813864]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
