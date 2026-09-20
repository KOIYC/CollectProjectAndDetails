---
type: "corpus"
item_id: "3888c0f9021b6ab3"
title: "Show HN: DropLock – E2EE secret sharing web app with no backend"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48337871"
project_url: "https://droplock.apitman.com/"
author: "apitman"
published_at: "2026-05-30T16:18:30Z"
captured_at: "2026-09-21T02:52:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_apitman
  - story_48337871
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: DropLock – E2EE secret sharing web app with no backend

> [!info] 一句话导读
> Simple safe secret sharing

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48337871>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：apitman　|　发布：2026-05-30T16:18:30Z
> 项目链接：<https://droplock.apitman.com/>
> 采集：2026-09-21T02:52:53+08:00　|　id：`3888c0f9021b6ab3`

## 正文

DropLock
Simple safe secret sharing
Receive a secret
The link below is like an open lock box that belongs to you. Anyone you share it with can put a secret inside and create a locked link that only you can open.
Copy link
 New lock box
Share a secret
This page is like an open lock box that someone shared with you. Type a message below, then you can create a new link that is a locked version of the box that only that person can open.
Text
Lock it
Secret link
Copy locked link
Secret
Opening...
How it works and security
 Your browser creates a public/private key pair. The public part is in your lock box link. The private part is saved by this browser as a non-extractable key, so it cannot be exported and secret links can only be opened in the same browser profile where the lock box was created. Each device or browser gets a different lock box.
When someone locks a secret for you, their browser uses your public key plus a one-time key to create an AES-GCM key with HKDF-SHA-256. The secret is locked locally, and the result is placed in the link fragment, which is not sent to the web server.
Tradeoffs: DropLock does not use fingerprint checking. If someone can replace the lock box link in transit, they can make the sender lock the secret for them instead. For stronger assurance, have the receiver send the lock box link over two different channels and compare that the links are identical, or use one channel you fully trust.
Warning: DropLock has not been reviewed by a security expert.
Source code

## 导航

- 项目页：[[10-项目/droplock.apitman.com_40892c81]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
