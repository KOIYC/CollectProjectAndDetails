---
type: "project"
title: "Show HN: Tokenhush – keeps your secrets out of what Claude Code sends"
project_url: "https://github.com/fregie/tokenhush"
first_seen: "2026-09-24T23:57:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_fregie
  - story_49826094
  - show_hn
lang: "en"
---

# Show HN: Tokenhush – keeps your secrets out of what Claude Code sends

> [!info] 一句话导读
> Local base-URL gateway that redacts secrets and PII before they leave your machine

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/fregie/tokenhush>
> 首次收录：2026-09-24T23:57:22+08:00
> 来源渠道：HN Show HN
> 标签：author_fregie, story_49826094, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-24/0a28b0337d8b283b_Show-HN-Tokenhush-–-keeps-your-secrets-out-of-what]] |

## 摘要正文

# fregie/tokenhush  Local base-URL gateway that redacts secrets and PII before they leave your machine  - Stars: 4 - Forks: 0 - Watchers: 4 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://tokenhush.com - Default branch: main - Created: 2026-09-11T16:53:56Z  ## Languages  - Go - PowerShell - Shell  ## Topics  - ai-security - ai-tools - claude-code - codex - dlp - gateway - golang - llm-security - pii - privacy - secret-scanning - secrets-management  ## Top Contributors  - fregie (151 contributions)  ---  ## README   English · 中文  Local, reversible secret redaction for AI coding tools. No MITM, no root certificate.   Star the repo · Watch releases  The model only ever sees placeholders  *What the model receives with Tokenhush running: detected secrets across many files at once, every value replaced by a placeholder.*  Tokenhush is a local, loopback-only HTTP gateway. It sits between your AI coding tool and the vendor API. It replaces detected secrets in the outbound request body with session-scoped placeholders, forwards the cleaned request, and restores the originals in the response, so your tool still gets the real values back. The model only ever sees placeholde…
