---
type: "project"
title: "Show HN: PortScout – TUI to find and kill processes occupying your ports"
project_url: "https://github.com/abhaikollara/portscout"
first_seen: "2026-09-21T02:52:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_TheThirdTuring
  - story_47960684
  - show_hn
lang: "en"
---

# Show HN: PortScout – TUI to find and kill processes occupying your ports

> [!info] 一句话导读
> Published: 2026-04-29

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/abhaikollara/portscout>
> 首次收录：2026-09-21T02:52:28+08:00
> 来源渠道：HN Show HN
> 标签：author_TheThirdTuring, story_47960684, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/ad3f10f4e5da0e4d_Show-HN-PortScout-–-TUI-to-find-and-kill-processes]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/ad3f10f4e5da0e4d_Show-HN-PortScout-–-TUI-to-find-and-kill-processes]] |
| 2026-09-21T02:52:28+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/ad3f10f4e5da0e4d_Show-HN-PortScout-–-TUI-to-find-and-kill-processes]] |

## 摘要正文

Published: 2026-04-29  # Repository: abhaikollara/portscout  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - Primary language: Go - Languages: Go (97.9%), Makefile (2.1%) - License: MIT License (MIT) - Default branch: main - Created: 2026-04-29T14:24:44Z - Last push: 2026-04-30T10:57:42Z - Contributors: 1 (top: abhaikollara) - Releases: 2 - Latest release: v0.2.0 (2026-04-29T15:10:19Z)  ---  # PortScout  A terminal UI tool for monitoring network connections and managing the processes behind them. Built with [Bubble Tea](https://github.com/charmbracelet/bubbletea).  ## Install  ### Homebrew (macOS, Apple Silicon)  ``` brew tap abhaikollara/tap brew install portscout ```  ### From source  ``` go install github.com/abhaikollara/portscout@latest ```  ### Manual  ``` git clone https://github.com/abhaikollara/portscout.git cd portscout make install ```  ## Usage  ``` portscout            # Launch the interactive TUI portscout 8080       # Show process details for port 8080 portscout -k 8080    # Kill the process on port 8080 portscout --version  # Print version ```  > **Note:** Some connections require elevated permissions to resolve process names. Run with `sudo` if you see `unkn…
