---
type: "corpus"
item_id: "64a794b247dc40d6"
title: "Show HN: Concat: the open-source CapCut replacement."
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49749773"
project_url: "https://github.com/jub0t/Concat"
author: "calanus"
published_at: "2026-09-18T03:04:58Z"
captured_at: "2026-09-20T14:02:41+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_calanus
  - story_49749773
  - show_hn
metrics: {"points": 4, "comments": 3, "engagement_velocity": 4}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:90d"
---

# Show HN: Concat: the open-source CapCut replacement.

> [!info] 一句话导读
> Free & Open-Source CapCut replacement. (formerly WolfCut)

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49749773>
> 指标：点赞=4 · 评论=3 · engagement_velocity=4
> 作者：calanus　|　发布：2026-09-18T03:04:58Z
> 项目链接：<https://github.com/jub0t/Concat>
> 采集：2026-09-20T14:02:41+08:00　|　id：`64a794b247dc40d6`

## 正文

# jub0t/Concat

Free & Open-Source CapCut replacement. (formerly WolfCut)

- Stars: 1004
- Forks: 86
- Watchers: 1004
- Open issues: 10
- License: Mozilla Public License 2.0
- Default branch: main
- Created: 2026-08-25T18:34:47Z

## Languages

- CSS
- HTML
- JavaScript
- Nix
- Python
- Rust
- Shell
- TypeScript

## Topics

- audio-processor
- auto-caption
- automation
- capcut
- capcut-alternative
- content-creation
- cross-platform
- desktop-app
- ffmpeg
- free-video-editor
- non-linear-editor
- offline-first
- open-source-video-editor
- rust-lang
- tauri-app
- video-editing
- video-editing-software
- video-processing-tool
- whisper-cpp

## Top Contributors

- jub0t (155 contributions)

---

## README

# Concat

**The free, open-source CapCut replacement.**

---

Concat is everything you use CapCut for — without the watermarks, paywalls,
or subscriptions. A native Rust engine does the heavy lifting, a clean React
interface does the editing, and it all runs on your machine: install it and
start cutting, no account, no extra downloads, no setup.

## Highlights

- Free and local Text-to-Speech features.
- 🎬 Multi-track editing, with several timelines per project when one isn't enough
- ✂️ The cutting toolkit you'd expect: split, trim, merge, transitions, speed control
- 💬 Auto-captions that run entirely on your machine — your audio never leaves it
- 🎙️ Voice filters for cleaning up or playing with your sound
- 📝 Titles and styled text
- 📦 Templates — build an edit once, reuse it for the next video
- 🚫 No watermarks, no account, nothing behind a paywall
- 🖥️ Works the same on macOS, Windows and Linux

## Get started

Currently in Alpha (pre-release), Download from Releases, Supports:
- Windows (tested)
- MacOs (tested) - unsigned binaries, use `xattr -dr com.apple.quarantine /Applications/Concat.app`
- Linux

### Nix (Linux)

The repository is a flake. `nix run github:jub0t/Concat` starts the editor
with ffmpeg and whisper wired in; `nix develop` opens a shell with everything
`npm run app` needs.

## Contribution

> [!IMPORTANT]
> The best way to contribute is to grab a build from the Release page and test the application to see where it breaks or how it can be improved.

To learn more about contributing to this project please refer to this Discussion announcement.

## Roadmap (or ideas)

🌟 = important or really desired.

- [ ] Templates: Improve templates, create centralized registry of templates contributed by users (kinda like npm).
- [ ] Hardware analysis: for device-tier detection, checking how good or potato someone's device is.
- [ ] Effects: A scaleable way to embed or add hundreds of different Transition styles, Effects, etc to the Library.
- [ ] Noise Cancelation/Removal.
- [ ] Object/Face Tracking: Proposed (can do better): MOSSE/KCF/optical flow.
- [ ] Auto Human Face Detection & Blurring features: YuNet + tracker, or look for better alternative tech.
- [ ] Caption text highlighting: Achievable with Whisper.cpp for timestamps.
- [ ] Profanity detection from Audio: Whisper + dictionary.
- [ ] Audio Silence removal feature.
- [ ] Auto Reframe: YuNet/person detector + tracker.

# Loading...

## 评论（3/3）

> **Muhammad523** · 2026-09-18T09:48:41.000Z　
> There's OpenCut and it does basically the same thing, have you seen it?

---

> **dopbase** · 2026-09-18T12:30:51.000Z　
> ill save it for later, it might use full for me in future!

---

> **calanus** · 2026-09-18T15:47:11.000Z　
> Yeah, I've even tested it out myself. It's rekt, barely any features and what exists hardly works. The "new" site doesn't even load.Not something I'd expect from a repository with 85,000 stars.

## 导航

- 项目页：[[10-项目/github.com_c9bd3a6e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
