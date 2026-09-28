---
type: "corpus"
item_id: "4db3308a7d7d1bef"
title: "Show HN: DynamicNotch – An interactive, customizable notch utility for macOS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49871925"
project_url: "https://github.com/Hitjack007/DynamicNotch"
author: "Hitjack007"
published_at: "2026-09-27T23:39:03Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_Hitjack007
  - story_49871925
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: DynamicNotch – An interactive, customizable notch utility for macOS

> [!info] 一句话导读
> Hitjack007/DynamicNotch

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49871925>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Hitjack007　|　发布：2026-09-27T23:39:03Z
> 项目链接：<https://github.com/Hitjack007/DynamicNotch>
> 采集：2026-09-28T09:47:28+08:00　|　id：`4db3308a7d7d1bef`

## 正文

# Hitjack007/DynamicNotch

Turn your notch into something useful

- Stars: 5
- Forks: 1
- Watchers: 5
- Open issues: 0
- License: Other
- Homepage: dynamicnotch.marksstuff.com
- Default branch: main
- Created: 2026-08-16T01:07:40Z

## Languages

- Metal
- Perl
- Python
- Shell
- Swift

## Top Contributors

- Hitjack007 (138 contributions)
- github-actions[bot] (9 contributions)
- aliaskar-rockeater (3 contributions)

---

## README

# DynamicNotch

Make your MacBook's notch actually useful. DynamicNotch turns the notch into a live system dashboard — music controls, fan speeds, CPU stats, audio visualization, and smart HUD replacements, all in the space that was doing nothing.

---

## Features

- **Dynamic notch sizing** — expands and contracts based on what's happening on screen
- **Responsive spectrogram** — real-time audio visualizer driven by live capture
- **Fan & thermal monitoring** — live fan speed and CPU temperature, with a custom fan curve editor
- **CPU usage** — at a glance, always visible
- **Caffeine** — prevent sleep directly from the notch
- **Custom system HUDs** — replaces macOS volume, brightness, and keyboard backlight overlays
- **Music playback** — album art, controls, and now-playing info
- **Calendar & Reminders** — upcoming events in the notch
- **File shelf** — drag files in, AirDrop them out
- **Downloads** — track in-progress browser downloads from the notch
- **Mirror** — quick webcam view
- **Battery indicator** — charging status and percentage
- **Gesture controls** — swipe to open/close
- **Extensions** — describe a small automation in plain English (e.g. turn Caffeine on when Xcode is frontmost) and DynamicNotch runs it every time, no code required
- **AI Usage** — tracks your Claude and ChatGPT usage and surfaces an alert in the notch as you approach your limit

---

## Requirements

- macOS **15 Sequoia** or later
- Any Mac — DynamicNotch draws its own custom notch, so a physical notch display isn't required

---

## Versioning

DynamicNotch's version number tracks the macOS version it's built and optimised for, not an independent app version:

- **Major** (`27` in `27.1.2`) — the macOS major version the release targets (e.g. macOS 27). This only changes when Apple ships a new macOS major version.
- **Minor** (`.1`) — a new feature has landed.
- **Patch** (`.2`) — a bug fix for the current minor.

For example, `27.1` means "the first feature release built and optimised for macOS 27." The patch level is only shown when a patch actually exists.

Because the minimum deployment target is macOS 15, **any version still runs on macOS 15 and up** — a release numbered `27.5` isn't macOS-27-only, it's just built and tuned against macOS 27, while remaining fully compatible with older supported macOS versions down to 15.

---

## Installation

### Option 1: Download and Install Manually

1. Download the latest **DynamicNotch.dmg** from the Releases page
2. Open the DMG and drag **DynamicNotch** to your Applications folder
3. Before opening, run this once in Terminal to clear the macOS security warning:
   ```bash
   xattr -dr com.apple.quarantine /Applications/DynamicNotch.app
   ```
4. Open the app — your notch is now alive

### Option 2: Install via Homebrew

You can also install using Homebrew. The Homebrew installation automatically bypasses the macOS security warning described above.

```bash
brew install --cask hitjack007/dynamicnotch/dynamicnotch
```

---

## Building from Source

For developers who want to build it themselves:

### Prerequisites
- macOS 15 or later
- Xcode 26 or later

### Steps

```bash
git clone https://github.com/Hitjack007/DynamicNotch.git
cd DynamicNotch
open dynamicNotch.xcodeproj
```

In Xcode, set your own development team under **Signing & Capabilities** for both `DynamicNotch` and `DynamicNotchXPCHelper`, then press **Cmd + R**.

---

## Contributing

Contributions are welcome — code, documentation, bug reports, feature requests, translations.

Two documents to read before you start:

- **CONTRIBUTING.md** — how to set up, branch, commit, and open a pull request
- **AI_AGENTS.md** — the AI agent policy. AI-assisted contributions are accepted, with requirements around disclosure, testing, and which parts of the codebase agents may touch

If you are using a coding agent, read both. If your agent reads files on its own, point it at AGENTS.md.

Security issues go through SECURITY.md rather than the public issue tracker.

---

## Maintainers

- Mark Greene
- Aliaskar Abdualiyev

---

## Contributors

Thanks to everyone who's contributed code to DynamicNotch:

---

## Credits

DynamicNotch is a fork of boring.notch by TheBoredTeam. Their work is the foundation of everything here.

Notable upstream projects:
- **MediaRemoteAdapter** — Now Playing support for macOS 15.4+
- **NotchDrop** — basis for the Shelf feature

---

## License

GNU General Public License v3.0

Copyright © 2024 TheBoredTeam
Copyright © 2025 Mark Greene

See LICENSE for the full text.

# ninjahawk/livenerf

## 关联链接

- https://github.com/Hitjack007/DynamicNotch.git

## 导航

- 项目页：[[10-项目/github.com_45641b80]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
