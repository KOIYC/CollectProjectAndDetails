---
type: "project"
title: "Show HN: Mess – a tiny CLI to clean dev clutter"
project_url: "https://github.com/olzhasar/mess"
first_seen: "2026-09-21T02:53:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_olzhasar
  - story_48733263
  - show_hn
lang: "en"
---

# Show HN: Mess – a tiny CLI to clean dev clutter

> [!info] 一句话导读
> A tiny CLI for removing common development clutter

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/olzhasar/mess>
> 首次收录：2026-09-21T02:53:03+08:00
> 来源渠道：HN Show HN
> 标签：author_olzhasar, story_48733263, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/e6879d818794c14c_Show-HN-Mess-–-a-tiny-CLI-to-clean-dev-clutter]] |
| 2026-09-21T02:53:03+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/e6879d818794c14c_Show-HN-Mess-–-a-tiny-CLI-to-clean-dev-clutter]] |

## 摘要正文

# olzhasar/mess  A tiny CLI for removing common development clutter  - Stars: 14 - Forks: 1 - Watchers: 14 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2024-10-25T20:18:25Z  ## Languages  - Go - Just - Makefile  ## Topics  - cache - cleaner - cli - disk-cleanup - disk-space - tempfiles  ## Top Contributors  - olzhasar (18 contributions)  ---  ## README  # mess  `mess` deletes common temporary development files in your projects. It ships with common cleanup patterns for popular programming languages like caches, build artifacts, bytecode files, linters output, etc.  Why a separate tool instead of a bash script? - Reports reclaimed disk space - Easy to configure and override patterns - Simple and fast - Reduces the number of bash scripts in the world  ## Installation  ### Pre-built binaries  Download a ready-to-use pre-built binary for your platform (Linux and macOS are currently supported) in GitHub releases.  ### Install with go  ```bash go install github.com/olzhasar/mess@latest ```  ### Building from source  ```bash make install ```  By default, this installs `mess` to `~/.local/bin`. To install elsewhere, set `PREFIX`:  ```bash make install PREFIX=/u…
