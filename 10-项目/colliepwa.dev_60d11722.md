---
type: "project"
title: "Show HN: ColliePWA, a self-hosted mobile terminal for coding agents, with alerts"
project_url: "https://colliepwa.dev/"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_asar
  - story_49775454
  - show_hn
lang: "en"
---

# Show HN: ColliePWA, a self-hosted mobile terminal for coding agents, with alerts

> [!info] 一句话导读
> Sharing the PWA[1] I built over the last couple of weeks to access my terminal sessions/agents when not in front of my computer. This started off as a weekend e…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://colliepwa.dev/>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_asar, story_49775454, show_hn
> 最新指标：点赞=3 · 评论=2 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=3 · 评论=2 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/86978c6f03ffaf6b_Show-HN-ColliePWA,-a-self-hosted-mobile-terminal-f]] |

## 摘要正文

Sharing the PWA[1] I built over the last couple of weeks to access my terminal sessions/agents when not in front of my computer. This started off as a weekend experiment right when herdr[2] (terminal multiplexer) released the functionality to write custom plugins and it's been quite helpful to me ever since. The general idea is that this runs a web app on the host machine which is then exposed through a front door implementation like tailscale/netbird/cloudflare tunnels etc.A lot of devs/teams are building sth very similar to this right now so there are many options out there already but I wanted: A PWA (no app store dep), better keyboard support than termux, the ability to manage multiple machines and easy integration with my existing tailnet via headscale.Some of the other features - Push notifications - Support for tmux and zellij (experimental) - Voice transcriptions (Codex sub or API) - Custom commands for cc/codex/pi etc (add your own) - Visual cues for when token cache goes staleYou can check out a live demo with dummy data on the website[1] or look at the implementation on Github[3] (PRs welcome).Looking forward to receiving some feedback or learning more about how people a…
