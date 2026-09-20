---
type: "project"
title: "Show HN: Tray indicator for WSL2: on/off, CPU and memory, one-click shutdown"
project_url: "https://github.com/ideaconnect/wsl-tray"
first_seen: "2026-09-20T09:37:04+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_bpacholek
  - story_49724577
  - show_hn
lang: "en"
---

# Show HN: Tray indicator for WSL2: on/off, CPU and memory, one-click shutdown

> [!info] 一句话导读
> ideaconnect/wsl-tray

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ideaconnect/wsl-tray>
> 首次收录：2026-09-20T09:37:04+08:00
> 来源渠道：HN Show HN
> 标签：author_bpacholek, story_49724577, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/7e5e6e1bd12e0df0_Show-HN-Tray-indicator-for-WSL2-on-off,-CPU-and-me]] |
| 2026-09-20T09:37:04+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/7e5e6e1bd12e0df0_Show-HN-Tray-indicator-for-WSL2-on-off,-CPU-and-me]] |

## 摘要正文

# ideaconnect/wsl-tray  Tray indicator for WSL2: on/off, CPU and memory, one-click shutdown  - Stars: 3 - Forks: 1 - Watchers: 3 - Open issues: 0 - License: BSD 3-Clause "New" or "Revised" License - Default branch: main - Created: 2026-09-14T14:47:50Z  ## Languages  - PowerShell - Rust  ## Topics  - rust - systray - windows - wsl - wsl2  ## Top Contributors  - bpacholek (19 contributions)  ---  ## README  # wsl-tray  build release Made in the EU  Windows tray icon that shows whether the WSL2 VM is running and how much CPU and memory it uses, with a menu entry that shuts it down.  Tray icon while WSL2 is running  It sits next to the clock like the keyboard-layout badge. Grey means the WSL2 VM is off; green, orange or red means it is running and shows how much of the machine it is using.  Icon states  Left to right: off, running below 50 %, 50–75 %, above 75 %. The two thresholds are the defaults; **Settings…** in the menu changes them.  Percentages are relative to the whole machine (all logical cores, all physical RAM), the same way Task Manager reports `vmmemWSL`. The colour follows whichever of CPU or memory is higher.  Hover for the numbers:  Tooltip  Click (left or right) for th…
