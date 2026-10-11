---
type: "corpus"
item_id: "27d5d244f10fd9bb"
title: "Show HN: Peer-to-peer instant messaging with proof-of-work spam protection"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50033558"
project_url: "https://github.com/iljah/p2pIM"
author: "iljah"
published_at: "2026-10-10T14:51:19Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_iljah
  - story_50033558
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Peer-to-peer instant messaging with proof-of-work spam protection

> [!info] 一句话导读
> Bitmessage.org still doesn't support Python 3 and over the years I've tried several times to create something similar but each time have run up against unclear/…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50033558>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：iljah　|　发布：2026-10-10T14:51:19Z
> 项目链接：<https://github.com/iljah/p2pIM>
> 采集：2026-10-11T09:43:53+08:00　|　id：`27d5d244f10fd9bb`

## 正文

Bitmessage.org still doesn't support Python 3 and over the years I've tried several times to create something similar but each time have run up against unclear/incomplete/missing documentation in Python/Rust/flask/tokio/asyncio/etc. Finally decided to give ChatGPT a real try and with tutoring based on minimal examples managed to have something usable in about a day. Most "difficult" part was having two instances of flask/quart running simultaneously while also having other stuff happen periodically in background.Novel thing in p2pIM compared to Bitmessage is that messages' PoW decays and that larger messages require better PoW than smaller ones. Thus small messages that are discarded quickly require significantly less PoW than large messages that persist for a long time. p2pIM doesn't support encryption but that should be straightforward to build on top.Message_v0 class in https://github.com/iljah/p2pIM/blob/main/messages.py defines low level details such as PoW, how many bytes to use for nonce, checksum, etc. Currently they're all only about 10 bytes or hex characters for easier debugging and testing. PoW is calculated as sha256 of timestamp+nonce+checksum, where checksum is sha256 of payload. Adding channel name as fourth item to PoW is on the https://github.com/iljah/p2pIM/blob/main/TODO list. server1.py mentioned at end of README is my previous attempt at this (without AI help) and the one before that is probably https://github.com/iljah/a2amd in Rust.

## 关联链接

- https://github.com/iljah/a2amd
- https://github.com/iljah/p2pIM/blob/main/TODO
- https://github.com/iljah/p2pIM/blob/main/messages.py

## 导航

- 项目页：[[10-项目/github.com_5acc003c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
