---
type: "project"
title: "Show HN: WhatsApp Bridge for those with their own VPS"
project_url: "https://github.com/vid-t/whatsapp-bridge"
first_seen: "2026-10-25T23:24:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_vid_t
  - story_50225644
  - show_hn
lang: "en"
---

# Show HN: WhatsApp Bridge for those with their own VPS

> [!info] 一句话导读
> vid-t/whatsapp-bridge

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/vid-t/whatsapp-bridge>
> 首次收录：2026-10-25T23:24:35+08:00
> 来源渠道：HN Show HN
> 标签：author_vid_t, story_50225644, show_hn
> 最新指标：点赞=3 · 评论=3 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:24:35+08:00 | HN Show HN | 点赞=3 · 评论=3 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-25/49880bc6f733ab3c_Show-HN-WhatsApp-Bridge-for-those-with-their-own-V]] |

## 摘要正文

# vid-t/whatsapp-bridge  Self-hosted, read-only bridge to your WhatsApp chats, with an MCP server and a web admin UI built on top of whatsmeow  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 1 - License: GNU Affero General Public License v3.0 - Default branch: main - Created: 2026-10-24T09:37:35Z  ## Languages  - CSS - Dockerfile - Go - HTML - JavaScript - Shell - TypeScript  ## Topics  - claude - golang - mcp - mcp-server - model-context-protocol - self-hosted - whatsapp - whatsmeow  ## Top Contributors  - vid-t (12 contributions)  ---  ## README  # whatsapp-bridge  **A self-hosted bridge & seutp gateaway built on top of whats-meow for storing and accessing your raw whatsapp data**  CI Licence: AGPL-3.0-only  whatsapp-bridge links to your WhatsApp as an extra device, the way WhatsApp Web does. It keeps the chats you choose in an encrypted database on your own VPS, where you can serach the chats or query them using MCP. For now, it is read only.  ## How it works  ```mermaid flowchart LR     phone["Your phone<br/>(WhatsApp)"] -- "linked device,<br/>like WhatsApp Web" --> bridge["whatsapp-bridge<br/>on your server"]     bridge --> db[("Encrypted database<br/>messages of ticked ch…
