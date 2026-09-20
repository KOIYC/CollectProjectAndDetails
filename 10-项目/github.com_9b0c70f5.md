---
type: "project"
title: "Show HN: Play SNES, gba, in your terminal, even in tmux"
project_url: "https://github.com/jhickner/rom"
first_seen: "2026-09-21T03:11:11+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_jhickner
  - story_49117254
  - show_hn
lang: "en"
---

# Show HN: Play SNES, gba, in your terminal, even in tmux

> [!info] 一句话导读
> Play ROMs directly in your terminal.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/jhickner/rom>
> 首次收录：2026-09-21T03:11:11+08:00
> 来源渠道：HN Show HN
> 标签：author_jhickner, story_49117254, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/c824b59ba94e911c_Show-HN-Play-SNES,-gba,-in-your-terminal,-even-in]] |
| 2026-09-21T03:11:11+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/c824b59ba94e911c_Show-HN-Play-SNES,-gba,-in-your-terminal,-even-in]] |

## 摘要正文

# jhickner/rom  Play ROMs directly in your terminal.  - Stars: 4 - Forks: 0 - Watchers: 4 - Open issues: 0 - License: MIT License - Default branch: master - Created: 2026-07-29T20:31:36Z  ## Languages  - C - Makefile  ## Topics  - emulator - kitty-graphics-protocol - libretro - macos - terminal  ## Top Contributors  - jhickner (22 contributions)  ---  ## README  # rom  Play ROMs directly in your terminal.  `rom` is a small libretro frontend for macOS and Linux. It renders native pixels with the kitty graphics protocol, supports real key-release events, save states, audio, fast-forward, and live terminal-theme recoloring.  Metroid Fusion running inline in the terminal with hue recoloring  `rom` does not include games, BIOS files, or emulator cores. Only run software you are legally entitled to use.  ## Quick start  You need Ghostty or kitty and a C compiler.  On macOS:  ```sh xcode-select --install ```  On Ubuntu or Debian:  ```sh sudo apt install build-essential libasound2-dev ```  Then:  ```sh git clone https://github.com/jhickner/rom cd rom make ./rom "path/to/game.sfc" ```  The first time you open a ROM for a platform you have no core for, `rom` offers to fetch and build that co…
