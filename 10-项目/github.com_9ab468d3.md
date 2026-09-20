---
type: "project"
title: "Show HN: Tileroot – save/restore tiling WM layouts (sway, Hyprland, i3)"
project_url: "https://github.com/Hinikaa/tileroot"
first_seen: "2026-09-21T03:11:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hinikaa
  - story_49119491
  - show_hn
lang: "en"
---

# Show HN: Tileroot – save/restore tiling WM layouts (sway, Hyprland, i3)

> [!info] 一句话导读
> Save and restore tiling WM layouts across sway, Hyprland, and i3 — one tool, no daemon, no shell-injection footguns.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Hinikaa/tileroot>
> 首次收录：2026-09-21T03:11:09+08:00
> 来源渠道：HN Show HN
> 标签：author_hinikaa, story_49119491, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/e61ef2970201bce1_Show-HN-Tileroot-–-save-restore-tiling-WM-layouts]] |
| 2026-09-21T03:11:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/e61ef2970201bce1_Show-HN-Tileroot-–-save-restore-tiling-WM-layouts]] |

## 摘要正文

# Hinikaa/tileroot  Save and restore tiling WM layouts across sway, Hyprland, and i3 — one tool, no daemon, no shell-injection footguns.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: master - Created: 2026-07-30T20:23:25Z  ## Languages  - C++ - Makefile - Shell  ## Topics  - cli - cpp - dotfiles - hyprland - i3wm - linux - session-manager - sway - tiling-window-manager - wayland  ## Top Contributors  - Hinikaa (5 contributions)  ---  ## README  # tileroot  Save and restore your tiling window manager's layout across a reboot or crash — sway, Hyprland, and (soon) i3, all with one tool.  ## Overview  Every sway/Hyprland/i3 user eventually hand-rolls a shell script that calls `swaymsg`/`hyprctl` + `jq` to save their window layout, and every one of those scripts breaks the next time the WM updates. The one existing attempt at a real tool, `hypr-session-restore`, is Hyprland-only and — by its own README — can't reconstruct the actual tiling layout tree, because Hyprland's IPC doesn't expose one. `i3-resurrect` solves this well for i3, but nothing unifies i3, sway, and Hyprland in one tool.  `tileroot` does. Sway (and i3, once it lands) imp…
