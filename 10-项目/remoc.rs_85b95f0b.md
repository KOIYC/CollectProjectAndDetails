---
type: "project"
title: "Show HN: Remoc – Rust RPC where channels are first-class values"
project_url: "https://remoc.rs/"
first_seen: "2026-09-20T09:37:14+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_surban
  - story_49713330
  - show_hn
lang: "en"
---

# Show HN: Remoc – Rust RPC where channels are first-class values

> [!info] 一句话导读
> Remoc: Rust RPC with remote channels and objects

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://remoc.rs/>
> 首次收录：2026-09-20T09:37:14+08:00
> 来源渠道：HN Show HN
> 标签：author_surban, story_49713330, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/c3774e652aa9ff17_Show-HN-Remoc-–-Rust-RPC-where-channels-are-first]] |
| 2026-09-20T09:37:14+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/c3774e652aa9ff17_Show-HN-Remoc-–-Rust-RPC-where-channels-are-first]] |

## 摘要正文

Remoc: Rust RPC with remote channels and objects  # Remoc  Rust RPC with remote channels and objects over one connection.   Remoc turns Rust traits marked with `#[rtc::remote]` into remotely callable interfaces, generating their clients and servers. Unlike conventional RPC, arguments and return values can contain Tokio-style remote channels and remote objects that remain usable after the call.   A channel endpoint is an ordinary value that can travel inside a message, creating a new communication path wherever it arrives, without opening a port, looking up a name or registering anything. RPC calls, channels and remote objects are multiplexed over one TCP, TLS, WebSocket, pipe or other transport connection, each with independent flow control.   $ `cargo add remoc` Copy the command  ## One connection, many channels   A single transport connection carries any number of independent, typed channels in either direction.   Each channel keeps its own type and its own direction; the connection carries them all, in chunks, so a large message on one does not hold up the others. Back pressure is per channel too: a receiver that stops reading slows only its own sender.  ## Channels are cheap, s…
