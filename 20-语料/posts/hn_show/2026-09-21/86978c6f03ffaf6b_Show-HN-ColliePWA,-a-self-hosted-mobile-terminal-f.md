---
type: "corpus"
item_id: "86978c6f03ffaf6b"
title: "Show HN: ColliePWA, a self-hosted mobile terminal for coding agents, with alerts"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49775454"
project_url: "https://colliepwa.dev/"
author: "asar"
published_at: "2026-09-20T13:04:12Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_asar
  - story_49775454
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: ColliePWA, a self-hosted mobile terminal for coding agents, with alerts

> [!info] 一句话导读
> Sharing the PWA[1] I built over the last couple of weeks to access my terminal sessions/agents when not in front of my computer. This started off as a weekend e…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49775454>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：asar　|　发布：2026-09-20T13:04:12Z
> 项目链接：<https://colliepwa.dev/>
> 采集：2026-09-21T09:44:03+08:00　|　id：`86978c6f03ffaf6b`

## 正文

Sharing the PWA[1] I built over the last couple of weeks to access my terminal sessions/agents when not in front of my computer. This started off as a weekend experiment right when herdr[2] (terminal multiplexer) released the functionality to write custom plugins and it's been quite helpful to me ever since. The general idea is that this runs a web app on the host machine which is then exposed through a front door implementation like tailscale/netbird/cloudflare tunnels etc.A lot of devs/teams are building sth very similar to this right now so there are many options out there already but I wanted: A PWA (no app store dep), better keyboard support than termux, the ability to manage multiple machines and easy integration with my existing tailnet via headscale.Some of the other features
- Push notifications
- Support for tmux and zellij (experimental)
- Voice transcriptions (Codex sub or API)
- Custom commands for cc/codex/pi etc (add your own)
- Visual cues for when token cache goes staleYou can check out a live demo with dummy data on the website[1] or look at the implementation on Github[3] (PRs welcome).Looking forward to receiving some feedback or learning more about how people access/work with their agents on the go. Also if you encounter any bugs please report them on Github, if a feature is missing you'd really want to see, open a discussion.[1] https://colliepwa.dev
[2] https://herdr.dev
[3] https://github.com/AltanS/collie

## 评论（2/2）

> **francescobianco** · 2026-09-20T13:47:23.000Z　
> please take a look to https://github.com/francescobianco/rap

---

> **asar** · 2026-09-20T14:30:50.000Z　
> This to me looks like it belongs into the harness, not the interface.

## 关联链接

- https://colliepwa.dev
- https://github.com/AltanS/collie
- https://herdr.dev

## 导航

- 项目页：[[10-项目/colliepwa.dev_60d11722]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
