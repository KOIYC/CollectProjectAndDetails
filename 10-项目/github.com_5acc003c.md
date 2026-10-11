---
type: "project"
title: "Show HN: Peer-to-peer instant messaging with proof-of-work spam protection"
project_url: "https://github.com/iljah/p2pIM"
first_seen: "2026-10-11T09:43:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_iljah
  - story_50033558
  - show_hn
lang: "en"
---

# Show HN: Peer-to-peer instant messaging with proof-of-work spam protection

> [!info] 一句话导读
> Bitmessage.org still doesn't support Python 3 and over the years I've tried several times to create something similar but each time have run up against unclear/…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/iljah/p2pIM>
> 首次收录：2026-10-11T09:43:53+08:00
> 来源渠道：HN Show HN
> 标签：author_iljah, story_50033558, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-11T09:43:53+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-11/27d5d244f10fd9bb_Show-HN-Peer-to-peer-instant-messaging-with-proof]] |

## 摘要正文

Bitmessage.org still doesn't support Python 3 and over the years I've tried several times to create something similar but each time have run up against unclear/incomplete/missing documentation in Python/Rust/flask/tokio/asyncio/etc. Finally decided to give ChatGPT a real try and with tutoring based on minimal examples managed to have something usable in about a day. Most "difficult" part was having two instances of flask/quart running simultaneously while also having other stuff happen periodically in background.Novel thing in p2pIM compared to Bitmessage is that messages' PoW decays and that larger messages require better PoW than smaller ones. Thus small messages that are discarded quickly require significantly less PoW than large messages that persist for a long time. p2pIM doesn't support encryption but that should be straightforward to build on top.Message_v0 class in https://github.com/iljah/p2pIM/blob/main/messages.py defines low level details such as PoW, how many bytes to use for nonce, checksum, etc. Currently they're all only about 10 bytes or hex characters for easier debugging and testing. PoW is calculated as sha256 of timestamp+nonce+checksum, where checksum is sha25…
