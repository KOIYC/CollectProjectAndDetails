---
type: "project"
title: "Show HN: DropLock – E2EE secret sharing web app with no backend"
project_url: "https://droplock.apitman.com/"
first_seen: "2026-09-21T02:52:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_apitman
  - story_48337871
  - show_hn
lang: "en"
---

# Show HN: DropLock – E2EE secret sharing web app with no backend

> [!info] 一句话导读
> Simple safe secret sharing

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://droplock.apitman.com/>
> 首次收录：2026-09-21T02:52:53+08:00
> 来源渠道：HN Show HN
> 标签：author_apitman, story_48337871, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/3888c0f9021b6ab3_Show-HN-DropLock-–-E2EE-secret-sharing-web-app-wit]] |
| 2026-09-21T02:52:53+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/3888c0f9021b6ab3_Show-HN-DropLock-–-E2EE-secret-sharing-web-app-wit]] |

## 摘要正文

DropLock Simple safe secret sharing Receive a secret The link below is like an open lock box that belongs to you. Anyone you share it with can put a secret inside and create a locked link that only you can open. Copy link  New lock box Share a secret This page is like an open lock box that someone shared with you. Type a message below, then you can create a new link that is a locked version of the box that only that person can open. Text Lock it Secret link Copy locked link Secret Opening... How it works and security  Your browser creates a public/private key pair. The public part is in your lock box link. The private part is saved by this browser as a non-extractable key, so it cannot be exported and secret links can only be opened in the same browser profile where the lock box was created. Each device or browser gets a different lock box. When someone locks a secret for you, their browser uses your public key plus a one-time key to create an AES-GCM key with HKDF-SHA-256. The secret is locked locally, and the result is placed in the link fragment, which is not sent to the web server. Tradeoffs: DropLock does not use fingerprint checking. If someone can replace the lock box link i…
