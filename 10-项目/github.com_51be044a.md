---
type: "project"
title: "Show HN: SafeScript, a safe version of JavaScript for executing untrusted code"
project_url: "https://github.com/SafeScript/safescript"
first_seen: "2026-11-09T09:57:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_EGreg
  - story_50417478
  - show_hn
lang: "en"
---

# Show HN: SafeScript, a safe version of JavaScript for executing untrusted code

> [!info] 一句话导读
> SafeScript/safescript

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/SafeScript/safescript>
> 首次收录：2026-11-09T09:57:36+08:00
> 来源渠道：HN Show HN
> 标签：author_EGreg, story_50417478, show_hn
> 最新指标：点赞=8 · 评论=5 · engagement_velocity=8

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=8 · 评论=5 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-11-09/eb3b3d6d16bc2939_Show-HN-SafeScript,-a-safe-version-of-JavaScript-f]] |
| 2026-11-09T09:57:36+08:00 | HN Show HN | 点赞=8 · 评论=5 · engagement_velocity=8 | [[20-语料/posts/hn_show/2026-11-09/eb3b3d6d16bc2939_Show-HN-SafeScript,-a-safe-version-of-JavaScript-f]] |

## 摘要正文

# SafeScript/safescript  Actually safe subset of Javascript, that can be embedded in many environments.  - Stars: 7 - Forks: 0 - Watchers: 7 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-23T19:54:59Z  ## Languages  - JavaScript  ## Top Contributors  - EGreg (4 contributions)  ---  ## README  # SafeScript  **JSON for code.** A safe computational subset of JavaScript.  JSON gave the world a safe way to exchange data. SafeScript does the same for computation. It's a strict subset of JavaScript — no `eval`, no `new`, no globals, no prototype access — that compiles to plain JS and PHP. Open a `.safe` file and you see code that's safe to run. The compiler is ~48 KB minified (~12 KB gzipped). Ship it anywhere, verify locally, no trust needed.  ## Use Cases  SafeScript starts small, the same way JSON did. Anywhere you need a safe handler for data or events:  - **Webserver handlers** — route logic, request transforms, validation rules submitted by users or tenants - **onclick and event handlers** — user-authored browser event handlers that can't escape their sandbox - **Plugin scripts** — extend an app with user-submitted logic without risking the host - …
