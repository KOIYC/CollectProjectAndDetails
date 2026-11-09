---
type: "project"
title: "Show HN: Cross-device passkey auth on Android 9, synced with Bitwarden"
project_url: "https://rsnel.github.io/passkeychain"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_riksnel
  - story_50413568
  - show_hn
lang: "en"
---

# Show HN: Cross-device passkey auth on Android 9, synced with Bitwarden

> [!info] 一句话导读
> I saw a colleague log in to a website on my laptop by scanning a FIDO QR code. I wanted to do the same, but couldn't find a way to use the passkeys stored in Bi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://rsnel.github.io/passkeychain>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_riksnel, story_50413568, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-09/f6cbabc97afe9798_Show-HN-Cross-device-passkey-auth-on-Android-9,-sy]] |

## 摘要正文

I saw a colleague log in to a website on my laptop by scanning a FIDO QR code. I wanted to do the same, but couldn't find a way to use the passkeys stored in Bitwarden on my phone to log in.So I asked Claude to build me an app. Claude found the task too daunting and only wanted to create a skeleton app. I was surprised by how complex the system actually is. Part of the process involves the phone sending an encrypted Bluetooth message as proof of presence, along with instructions on how to proceed.With the help of DeepSeek's free chat, I eventually managed to create a working implementation, after chasing quite a few hallucinations and dead ends... Claude then polished the app for me.The repository includes a full specification with test vectors, and the website has a nice, accessible explanation of how the process works.
