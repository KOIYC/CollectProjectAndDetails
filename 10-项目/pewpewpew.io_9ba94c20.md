---
type: "project"
title: "Show HN: PewPewPew – Multiplayer Asteroids with deterministic rollback at 60hz"
project_url: "https://pewpewpew.io/"
first_seen: "2026-11-02T09:37:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Benjaminsen
  - story_50326850
  - show_hn
lang: "en"
---

# Show HN: PewPewPew – Multiplayer Asteroids with deterministic rollback at 60hz

> [!info] 一句话导读
> I have been building realtime multiplayer games that run in a browser since 1999 and my latest is pewpewpew.io which combines everything I know about doing this…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://pewpewpew.io/>
> 首次收录：2026-11-02T09:37:22+08:00
> 来源渠道：HN Show HN
> 标签：author_Benjaminsen, story_50326850, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-02T09:37:22+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-02/0bec18d4c9745206_Show-HN-PewPewPew-–-Multiplayer-Asteroids-with-det]] |

## 摘要正文

I have been building realtime multiplayer games that run in a browser since 1999 and my latest is pewpewpew.io which combines everything I know about doing this well.The game uses a fully client and server synchronized state machine running at 60hz with rollback / rollforward on both client and server.During normal play only user input is transmitted using a compressed message format, where input is 7 fields in 2 bytes, with a total of about 26KB/s used for a room with 32 active players.Users are automatically distributed into a room on a server with the lowest measured ping where there are other players playing.Currently running using cloudflare Durable Objects, but I expect to offload it to dedicated metal should the cost go above $500 / month. Current monthly cost sits at about $300 per 1K average CCU.Works on mobile, free to play, no ads, no signup.
