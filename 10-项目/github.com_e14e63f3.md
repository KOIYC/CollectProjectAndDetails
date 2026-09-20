---
type: "project"
title: "Show HN: An AI skill for filtering and reading Hacker Newsletter and others"
project_url: "https://github.com/Promyer/stellar-inbox"
first_seen: "2026-09-21T03:11:10+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_miros_love
  - story_49118702
  - show_hn
lang: "en"
---

# Show HN: An AI skill for filtering and reading Hacker Newsletter and others

> [!info] 一句话导读
> Promyer/stellar-inbox

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Promyer/stellar-inbox>
> 首次收录：2026-09-21T03:11:10+08:00
> 来源渠道：HN Show HN
> 标签：author_miros_love, story_49118702, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/af70943686573ff2_Show-HN-An-AI-skill-for-filtering-and-reading-Hack]] |
| 2026-09-21T03:11:10+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/af70943686573ff2_Show-HN-An-AI-skill-for-filtering-and-reading-Hack]] |

## 摘要正文

# Promyer/stellar-inbox  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-07-30T17:22:13Z  ## Languages  - Python  ## Top Contributors  - miroslove-love (2 contributions)  ---  ## README  # Stellar Inbox  Codex skill for reading a configured Gmail newsletter and passing its raw decoded text MIME parts to the model. The skill contains a local read-only Gmail daemon as an implementation detail; users normally invoke the skill with a specific date or date range rather than interacting with the daemon directly.  The skill starts the daemon, requests all messages from the configured sender for the requested period, passes all decoded `text/plain` and `text/html` MIME parts to the model, and uses `.agents/skills/email-reader/LINK_FILTERING_INSTRUCTIONS.md` for report selection, formatting, and feedback collection.  ## Use with Codex  Invoke the skill with a date or date range:  ```text $email-reader 2026-06-27 $email-reader 2026-06-01 2026-06-27 ```  The skill runs `.agents/skills/email-reader/scripts/fetch_messages.py`, which returns message metadata and raw decoded text MIME parts. The model interprets those parts when c…
