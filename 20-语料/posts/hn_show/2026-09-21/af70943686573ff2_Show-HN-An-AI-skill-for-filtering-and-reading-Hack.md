---
type: "corpus"
item_id: "af70943686573ff2"
title: "Show HN: An AI skill for filtering and reading Hacker Newsletter and others"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49118702"
project_url: "https://github.com/Promyer/stellar-inbox"
author: "miros_love"
published_at: "2026-07-31T03:33:20Z"
captured_at: "2026-09-21T03:11:10+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_miros_love
  - story_49118702
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: An AI skill for filtering and reading Hacker Newsletter and others

> [!info] 一句话导读
> Promyer/stellar-inbox

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49118702>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：miros_love　|　发布：2026-07-31T03:33:20Z
> 项目链接：<https://github.com/Promyer/stellar-inbox>
> 采集：2026-09-21T03:11:10+08:00　|　id：`af70943686573ff2`

## 正文

# Promyer/stellar-inbox

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-07-30T17:22:13Z

## Languages

- Python

## Top Contributors

- miroslove-love (2 contributions)

---

## README

# Stellar Inbox

Codex skill for reading a configured Gmail newsletter and passing its raw decoded text MIME parts to the model. The skill contains a local read-only Gmail daemon as an implementation detail; users normally invoke the skill with a specific date or date range rather than interacting with the daemon directly.

The skill starts the daemon, requests all messages from the configured sender for the requested period, passes all decoded `text/plain` and `text/html` MIME parts to the model, and uses `.agents/skills/email-reader/LINK_FILTERING_INSTRUCTIONS.md` for report selection, formatting, and feedback collection.

## Use with Codex

Invoke the skill with a date or date range:

```text
$email-reader 2026-06-27
$email-reader 2026-06-01 2026-06-27
```

The skill runs `.agents/skills/email-reader/scripts/fetch_messages.py`, which returns message metadata and raw decoded text MIME parts. The model interprets those parts when composing the report; the fetcher does not select, clean, or rewrite their content. Generated reports keep per-link feedback in browser `localStorage` and can export it as `Report.feedback.json` for later preference updates.

## Configure

Create `.env` in the project root:

```env
ALLOWED_SENDER=sender@example.com
GMAIL_OAUTH_CREDENTIALS_PATH=gmail_client_secret.json
HOST=127.0.0.1
PORT=4873
```

Get the OAuth client file:

1. Open `https://console.cloud.google.com`.
2. Create or select a project.
3. Enable `APIs & Services -> Library -> Gmail API`.
4. Configure `Google Auth Platform -> OAuth consent screen -> Branding`.
5. Add your Gmail account to test users if the app is in test mode.
6. Create `Google Auth Platform -> Clients -> Create client`.
7. Select application type `Desktop app`.
8. Download the JSON file.
9. Rename it to `gmail_client_secret.json` and put it in the project root.

This must be an OAuth client JSON for an installed desktop app. Do not use an API key or a service account JSON.

The scope in code is:

```text
https://www.googleapis.com/auth/gmail.readonly
```

## Local daemon

Install the locked dependencies first:

```bash
uv sync --locked
```

The daemon can also be started directly for local development:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run --locked python -m email_reader
```

On the first `/messages` request, the daemon opens the OAuth authorization URL in the default browser. Finish Google authorization; the local OAuth token is saved to `.gmail_token.json`. If Google rejects an old or revoked token, the daemon automatically starts authorization again and keeps the old token as a backup.

If Google shows `Access blocked: this app has not completed the Google verification process`, wait and try again later. It can take up to 24 hours for new OAuth app settings and test-user changes to become available.

The API is available at `/messages`:

```bash
curl 'http://127.0.0.1:4873/messages?start_date=2026-06-01&end_date=2026-06-27'
```

# Reclip – AI Video Clipper, Voiceover & Creator Tools

## 关联链接

- http://127.0.0.1:4873/messages?start_date=2026-06-01&end_date=2026-06-27
- https://console.cloud.google.com`.
- https://www.googleapis.com/auth/gmail.readonly

## 导航

- 项目页：[[10-项目/github.com_e14e63f3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
