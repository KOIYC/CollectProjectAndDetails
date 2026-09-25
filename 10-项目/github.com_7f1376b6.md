---
type: "project"
title: "Show HN: Headwire – WireGuard with NAT traversal via Tailscale's magicsock"
project_url: "https://github.com/brofranks/headwire"
first_seen: "2026-09-25T13:42:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_brof
  - story_49834349
  - show_hn
lang: "en"
---

# Show HN: Headwire – WireGuard with NAT traversal via Tailscale's magicsock

> [!info] 一句话导读
> WireGuard meshes with NAT traversal and DERP relay fallback.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/brofranks/headwire>
> 首次收录：2026-09-25T13:42:25+08:00
> 来源渠道：HN Show HN
> 标签：author_brof, story_49834349, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-25T13:42:25+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-25/a6a3137edc56e160_Show-HN-Headwire-–-WireGuard-with-NAT-traversal-vi]] |

## 摘要正文

# brofranks/headwire  WireGuard meshes with NAT traversal and DERP relay fallback.  - Stars: 0 - Forks: 1 - Watchers: 0 - Open issues: 1 - License: BSD 3-Clause "New" or "Revised" License - Default branch: main - Created: 2026-09-24T05:26:31Z  ## Languages  - C - Go - Shell  ## Top Contributors  - brofranks (1 contributions)  ---  ## README   Headwire  Headwire statically configures WireGuard peers with support for NAT traversal using DERP relays. It is experimental.  Initial connections will happen over DERP, then upgrade to a direct path if one is found:  ```text $ headwire ping 100.64.0.2 pong from 100.64.0.2 via relay:1 in 122ms pong from 100.64.0.2 via relay:1 in 118ms pong from 100.64.0.2 via 203.0.113.10:41198 in 1ms ```  Headwire is built using Tailscale's open-source data plane libraries.  ## Features  - establish direct connections where possible - fall back to relayed connections - continue using ordinary WireGuard peers - a macOS app  ## Configuration Example  Run your own DERP servers. Tailscale runs "free rate-limited DERP relays" for Tailcat, see its DERP map.  ```ini [DERPRegion] ID = 1 Nodes = derp1.example.com, derp2.example.com  [Interface] PrivateKey = <base64 p…
