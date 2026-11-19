---
type: "project"
title: "Show HN: 100ms copy-on-write workspaces for AI agents on macOS"
project_url: "https://github.com/gabrielvfonseca/replica"
first_seen: "2026-11-19T09:43:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_gabrielfonseca
  - story_50553493
  - show_hn
lang: "en"
---

# Show HN: 100ms copy-on-write workspaces for AI agents on macOS

> [!info] 一句话导读
> gabrielvfonseca/replica

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/gabrielvfonseca/replica>
> 首次收录：2026-11-19T09:43:31+08:00
> 来源渠道：HN Show HN
> 标签：author_gabrielfonseca, story_50553493, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:43:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-19/1373e27de5c8ad6c_Show-HN-100ms-copy-on-write-workspaces-for-AI-agen]] |

## 摘要正文

# gabrielvfonseca/replica  Instant, disk-safe workspaces for AI agents on macOS. Clones a prebuilt project tree with APFS clonefile instead of checking out and installing.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: Other - Default branch: main - Created: 2026-10-25T19:38:05Z  ## Languages  - Go Template - JavaScript - Makefile - Ruby - Rust - Shell  ## Topics  - agentic-workloads - ai-agents - apfs - build-cache - cleanup - cli - clonefile - developer-tools - fs - macos - rust - sandbox - workspace-manager  ## Top Contributors  - gabrielvfonseca (57 contributions) - dependabot[bot] (8 contributions)  ---  ## README  Replica Banner  # Isolated replicas of your workspace for AI agents  **Replica gives every agent run its own fully installed copy of your project, created in milliseconds with APFS copy-on-write. Each copy is a real git checkout, and automatic cleanup keeps total disk use bounded.**  ```sh cd "$(replica new --ttl 2h --name fix-login)"   # a ready workspace; the path goes to stdout git checkout -b agent/fix-login && git commit -am "fix login" && git push -u origin agent/fix-login replica rm <id>                                 # done; or let the TTL…
