---
type: "project"
title: "Show HN: compaction.dev makes cc/codex/cursor resend less, per run"
project_url: "https://github.com/philipppohlmann/compaction"
first_seen: "2026-09-24T23:57:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_philippadrian
  - story_49827661
  - show_hn
lang: "en"
---

# Show HN: compaction.dev makes cc/codex/cursor resend less, per run

> [!info] 一句话导读
> philipppohlmann/compaction

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/philipppohlmann/compaction>
> 首次收录：2026-09-24T23:57:22+08:00
> 来源渠道：HN Show HN
> 标签：author_philippadrian, story_49827661, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-24/5fc04ba915883ac9_Show-HN-compaction.dev-makes-cc-codex-cursor-resen]] |

## 摘要正文

# philipppohlmann/compaction  Make Claude Code, Codex, and Cursor use fewer tokens. Local context compaction with measured savings.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://www.compaction.dev/ - Default branch: main - Created: 2026-08-24T20:10:08Z  ## Languages  - JavaScript - Shell - TypeScript  ## Topics  - claude-code - codex - compaction - context-engineering - context-window - cursor - developer-tools - llm - token-optimization - token-usage - tokenomics  ## Top Contributors  - philipppohlmann (17 contributions)  ---  ## README  # Make coding agents resend less  npm version license: Apache-2.0  Install · How it works · What you get · Proof · Supported tools · Plans · Privacy  ---  **Compaction runs underneath Claude Code, Codex, and Cursor. No new editor. No new agent.**  It reduces eligible model visible input before it reaches the provider, shape unnecessary output before generation, and show the result inside the tools you already use.  This is a real acceptance run through a normal Codex subscription session:  ```text $ codex  ↳ compaction · input 8,388,356→7,212,095 (−14%) · output 14,393→10,795 (−25%, est.) ·…
