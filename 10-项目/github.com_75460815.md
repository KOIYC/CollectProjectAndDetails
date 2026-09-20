---
type: "project"
title: "Show HN: Snitchmd – Cloudflare-protected URLs into clean Markdown via Docker"
project_url: "https://github.com/syabro/snitchmd"
first_seen: "2026-09-21T01:41:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_syabro
  - story_47949500
  - show_hn
lang: "en"
---

# Show HN: Snitchmd – Cloudflare-protected URLs into clean Markdown via Docker

> [!info] 一句话导读
> Shmauthor here. Built this for myself, putting it out in case it's useful.Needed any URL as clean Markdown for LLM context — including Cloudflare/anti-bot sites…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/syabro/snitchmd>
> 首次收录：2026-09-21T01:41:49+08:00
> 来源渠道：HN Show HN
> 标签：author_syabro, story_47949500, show_hn
> 最新指标：点赞=8 · 评论=1 · engagement_velocity=8

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=8 · 评论=1 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/83d9742ac7011b3c_Show-HN-Snitchmd-–-Cloudflare-protected-URLs-into]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=8 · 评论=1 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/83d9742ac7011b3c_Show-HN-Snitchmd-–-Cloudflare-protected-URLs-into]] |
| 2026-09-21T01:41:49+08:00 | HN Show HN | 点赞=8 · 评论=1 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-09-21/83d9742ac7011b3c_Show-HN-Snitchmd-–-Cloudflare-protected-URLs-into]] |

## 摘要正文

Shmauthor here. Built this for myself, putting it out in case it's useful.Needed any URL as clean Markdown for LLM context — including Cloudflare/anti-bot sites. curl gets HTTP 403 on those, raw HTML is 80%+ nav noise eating context, paid SaaS (Firecrawl, Jina) wasn't an option for me.It's a Docker wrapper around two existing OSS tools — CloakBrowser (stealth Chromium that passes Cloudflare) and rs-trafilatura (HTML → Markdown). No new scraper, just glue. Runs locally, my URLs stay on my boxToken reduction (raw curl HTML vs snitchmd, tiktoken cl100k_base):- cloudflare.com/learning/bots — curl: HTTP 403 → snitchmd: 0.8k- docs.docker.com/engine/install — 187k → 0.9k- en.wikipedia.org/wiki/LLM — 222.7k → 29.7kHeads up: passes Cloudflare, can't solve "click traffic lights" captchas (reCAPTCHA v2, hCaptcha)MIT. Happy to answer questions
