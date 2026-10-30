---
type: "project"
title: "Show HN: Arken – Passwordless auth middleware using secp256k1 keys"
project_url: "https://github.com/zacharybenson/arken-protocol"
first_seen: "2026-10-30T09:57:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_zachbenson817
  - story_50298738
  - show_hn
lang: "en"
---

# Show HN: Arken – Passwordless auth middleware using secp256k1 keys

> [!info] 一句话导读
> zacharybenson/arken-protocol

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/zacharybenson/arken-protocol>
> 首次收录：2026-10-30T09:57:35+08:00
> 来源渠道：HN Show HN
> 标签：author_zachbenson817, story_50298738, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-30/43cd266874055b7d_Show-HN-Arken-–-Passwordless-auth-middleware-using]] |
| 2026-10-30T09:57:35+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-30/43cd266874055b7d_Show-HN-Arken-–-Passwordless-auth-middleware-using]] |

## 摘要正文

# zacharybenson/arken-protocol  Passwordless authentication via DID signatures. No passwords. No sessions. Nothing to breach.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - Default branch: main - Created: 2026-10-29T08:06:31Z  ## Languages  - Dockerfile - HTML - JavaScript - Python - Rust - Shell  ## Top Contributors  - zacharybenson (3 contributions)  ---  ## README  # Arken Auth  **Passwordless authentication for web servers. No passwords. No sessions. Nothing to breach.**  **Live Demo →** · npm · PyPI  ---  ## The problem  Every auth system today asks your server to hold a secret — a password hash, a session token, an API key. That secret is a liability. It gets breached. It gets phished. It gets rotated on a schedule that nobody follows.  Arken Auth flips the model: **the user holds the secret, the server holds nothing.**  ---  ## How it works  ``` Client                              Server   │                                   │   ├── GET /protected ────────────────▶│   │                                   │ (no auth header)   │◀── 401 { challenge: { nonce } } ──┤   │                                   │   │   sign(nonce, privateKey)         │   │                       …
