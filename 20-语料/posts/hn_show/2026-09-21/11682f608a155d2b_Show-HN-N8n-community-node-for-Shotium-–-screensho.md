---
type: "corpus"
item_id: "11682f608a155d2b"
title: "Show HN: N8n community node for Shotium – screenshot and OG image API"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49495905"
project_url: "https://github.com/shotium/n8n-nodes-shotium"
author: "foodpad"
published_at: "2026-08-30T05:16:54Z"
captured_at: "2026-09-21T03:17:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_foodpad
  - story_49495905
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: N8n community node for Shotium – screenshot and OG image API

> [!info] 一句话导读
> shotium/n8n-nodes-shotium

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49495905>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：foodpad　|　发布：2026-08-30T05:16:54Z
> 项目链接：<https://github.com/shotium/n8n-nodes-shotium>
> 采集：2026-09-21T03:17:41+08:00　|　id：`11682f608a155d2b`

## 正文

# shotium/n8n-nodes-shotium

n8n community node for Shotium - screenshots and OG images from any URL

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Homepage: https://shotium.com
- Default branch: main
- Created: 2026-08-25T01:36:22Z

## Languages

- JavaScript
- TypeScript

## Top Contributors

- shery (10 contributions)

---

## README

# n8n-nodes-shotium

This is an n8n community node. It lets you use Shotium in your n8n workflows.

Shotium is a screenshot and OG image rendering API: turn any URL into a PNG/JPEG/WebP screenshot, or generate 1200×630 Open Graph images from typed templates — rendered by a real browser.

n8n is a fair-code licensed workflow automation platform.

Installation
Operations
Credentials
Compatibility
Usage
Resources
Version history

## Installation

Follow the installation guide in the n8n community nodes documentation.

Package name: `n8n-nodes-shotium`

## Operations

- **Take Screenshot** — render any public URL to an image
 - Formats: PNG, JPEG, WebP
 - Viewport control (width/height), full-page capture, quality for lossy formats
 - Identical parameter sets are cached for 24 hours by the API
- **Generate OG Image** — render a 1200×630 social card from one of five templates
 - Templates: Blog, Product, Podcast, Event, Minimal — each with typed fields
 - Formats: PNG, JPEG
- **Generate Signed URL** — build an HMAC-signed OG image link safe to embed in public HTML
 - Computed locally in the node: no API call, no render billed
 - The image renders on first request and updates whenever the signed parameters change; CDN edge hits are free
 - Requires the Signing Secret and UID fields in your credential

The two render operations output the image as **binary data** (default field: `data`), ready to pipe into any downstream node — upload to S3, attach to email, send via Telegram, write to disk, and so on. Generate Signed URL outputs JSON with a `url` field.

## Credentials

1. Sign in at shotium.com/account (GitHub sign-in, 100 free render credits — no credit card).
2. Create an API key. The key (`sk_live_…`), your signing secret and your UID are shown **once**, together.
3. In n8n, create a **Shotium API** credential and paste the key. The signing secret and UID are only needed for the Generate Signed URL operation — leave them empty otherwise.

Credential validation calls `GET /v1/me` and costs no render credits. A render is billed only when an image is successfully returned; failed renders are never billed.

## Compatibility

Requires n8n version 1.0 or above. Built and tested against the current n8n release.

## Usage

Typical patterns:

- **Nightly site archive**: Schedule Trigger → Shotium (Take Screenshot, full page) → S3/Drive upload
- **OG images that follow your data**: new blog post webhook → Shotium (Generate Signed URL, Blog template with expressions) → write the URL into your CMS's og:image field — the image updates whenever the signed parameters change
- **Visual monitoring**: Cron → Screenshot of a competitor page → image diff → alert

Rate limit is 60 requests/minute per API key. When quota and credits run out the API returns `429 quota_exceeded` — nothing auto-charges.

For build-time embedding without n8n, see the Shotium docs.

## Resources

- n8n community nodes documentation
- Shotium API reference
- OG image templates & parameters
- Service status
- Changelog

## Version history

- **0.1.3** — Corrected credential documentation and hardened the tag-driven OIDC publishing workflow with release metadata checks.
- **0.1.2** — Codex fixes for n8n verification: fully-qualified `node` identifier, removed unsupported `Developer Tools` category.
- **0.1.1** — Credential verification moved to the dedicated `GET /v1/me` endpoint (declarative credential test).
- **0.1.0** — Initial release: Take Screenshot, Generate OG Image and Generate Signed URL operations.

# https://www.reddit.com/r/EntrepreneurRideAlong/comments/1szxbsl/22th_website_built/

## 关联链接

- https://shotium.com
- https://www.reddit.com/r/EntrepreneurRideAlong/comments/1szxbsl/22th_website_built/

## 导航

- 项目页：[[10-项目/github.com_0ce9dbe8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
