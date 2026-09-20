---
type: "project"
title: "Show HN: Throwaway – open-source disposable email checker and API"
project_url: "https://github.com/sslboard/throwaway"
first_seen: "2026-09-21T02:52:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_weddpros
  - story_47960525
  - show_hn
lang: "en"
---

# Show HN: Throwaway – open-source disposable email checker and API

> [!info] 一句话导读
> An open source Cloudflare Worker app and API to check if email addresses are throwaway/disposable or valid

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sslboard/throwaway>
> 首次收录：2026-09-21T02:52:28+08:00
> 来源渠道：HN Show HN
> 标签：author_weddpros, story_47960525, show_hn
> 最新指标：点赞=14 · 评论=14 · engagement_velocity=14

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=14 · 评论=14 · engagement_velocity=14 | [[20-语料/posts/hn_show/2026-09-21/df097c7ece49eb8b_Show-HN-Throwaway-–-open-source-disposable-email-c]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=14 · 评论=14 · engagement_velocity=14 | [[20-语料/posts/hn_show/2026-09-21/df097c7ece49eb8b_Show-HN-Throwaway-–-open-source-disposable-email-c]] |
| 2026-09-21T01:41:12+08:00 | HN Show HN | 点赞=14 · 评论=14 · engagement_velocity=14 | [[20-语料/posts/hn_show/2026-09-21/df097c7ece49eb8b_Show-HN-Throwaway-–-open-source-disposable-email-c]] |
| 2026-09-21T02:52:28+08:00 | HN Show HN | 点赞=14 · 评论=14 · engagement_velocity=14 | [[20-语料/posts/hn_show/2026-09-21/df097c7ece49eb8b_Show-HN-Throwaway-–-open-source-disposable-email-c]] |

## 摘要正文

# sslboard/throwaway  An open source Cloudflare Worker app and API to check if email addresses are throwaway/disposable or valid  - Stars: 45 - Forks: 0 - Watchers: 45 - Open issues: 0 - License: MIT License - Homepage: https://throwaway.sslboard.com/ - Default branch: main - Created: 2026-04-30T03:58:20Z  ## Languages  - CSS - HTML - JavaScript - Python - TypeScript  ## Top Contributors  - chrisDeFouRire (82 contributions)  ---  ## README  # throwaway  A Cloudflare Worker that detects disposable/temporary email domains, invalid TLDs, and non-existent domains (no MX records), exposed as a fast JSON API. Ships 72K+ domains in a ~173KB binary bloom filter. Uses tldts for TLD validation and Cloudflare DNS-over-HTTPS for MX resolution. Includes a clean web UI at `/` for quick checks, `/llms.txt` for AI agent discovery, OpenAPI/catalog metadata, no-auth documentation, and MCP-compatible tool discovery.  **Live deployment:** throwaway.sslboard.com  Deploy to Cloudflare Workers  ## Honest context  **This project was written almost entirely by AI.** I needed a disposable-email checker for SSLBoard (a free cybersecurity assessment tool) and I used Claude to build it. I'm sharing it as open …
