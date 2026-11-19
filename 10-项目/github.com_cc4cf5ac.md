---
type: "project"
title: "Show HN: Poptato – App launcher, command runner, and fuzzy menu for Linux"
project_url: "https://github.com/skorotkiewicz/poptato"
first_seen: "2026-11-19T09:43:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_modinfo
  - story_50550737
  - show_hn
lang: "en"
---

# Show HN: Poptato – App launcher, command runner, and fuzzy menu for Linux

> [!info] 一句话导读
> skorotkiewicz/poptato

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/skorotkiewicz/poptato>
> 首次收录：2026-11-19T09:43:31+08:00
> 来源渠道：HN Show HN
> 标签：author_modinfo, story_50550737, show_hn
> 最新指标：点赞=6 · 评论=1 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:43:31+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-11-19/9c97069f24c9e5c7_Show-HN-Poptato-–-App-launcher,-command-runner,-an]] |

## 摘要正文

# skorotkiewicz/poptato  Keyboard-driven app launcher, command runner, and fuzzy menu for Linux  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-18T15:29:11Z  ## Languages  - CSS - Just - Rust  ## Top Contributors  - skorotkiewicz (15 contributions)  ---  ## README   Default theme — tweakable via config.toml  **Poptato** is a small, keyboard-driven application launcher for Linux, written in Rust with GTK4. Launch desktop apps, run commands, pick from piped input, or invent your own menu modes.  No elaborate ceremony. Type, choose, **pop!** 🥔  ## Get it while it's hot  **Arch Linux (AUR):**  ```bash yay -S poptato-bin ```  Then try:  ```bash poptato --mode apps ```  **Build from source:** Requires Rust 1.92+, GTK4 development files, `pkg-config`, and optionally GTK4 Layer Shell development files (enabled by default).  On Arch:  ```bash sudo pacman -S --needed base-devel rust pkgconf gtk4 gtk4-layer-shell git clone https://github.com/skorotkiewicz/poptato.git cd poptato cargo install --path . --locked ```  For a GTK4-only build without layer-shell integration:  ```bash cargo install --path . --locked --no-default-f…
