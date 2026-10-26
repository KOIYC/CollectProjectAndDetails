---
type: "corpus"
item_id: "b86d0e6b63d8414c"
title: "Show HN: QuickRust replaces cargo, sets up sccache, centralizes build cache"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50236987"
project_url: "https://machinefabric.com/quickrust"
author: "joeharshamshiri"
published_at: "2026-10-25T23:14:19Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-26"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_joeharshamshiri
  - story_50236987
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: QuickRust replaces cargo, sets up sccache, centralizes build cache

> [!info] 一句话导读
> macOS · Windows

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50236987>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：joeharshamshiri　|　发布：2026-10-25T23:14:19Z
> 项目链接：<https://machinefabric.com/quickrust>
> 采集：2026-10-26T09:42:36+08:00　|　id：`b86d0e6b63d8414c`

## 正文

Skip to content
MachineFabric
FabricLoom
Overview
 The application
Downloads
 macOS · Windows · Linux
Documentation
 Guides · SDK
CapDAG
Overview
 Capabilities · Machines
Downloads
 Command line
Documentation
 Specification
Registry
 Capabilities · Media
lungo
Overview
 Lean → code
Downloads
 Command line
Documentation
 Guides · Reference
QuickRust
Overview
 Cargo, faster
Downloads
 Command line
Documentation
 Guides · Reference
Cartridges
 Models
 Blog
Get FabricLoom
 Get lungo
IT
 EN
Cargo, faster
QuickRust
A drop-in replacement for the cargo command that makes Rust
 builds faster, with nothing to configure. Every build goes into one centrally managed cache,
 which stays within its limits and gives space back on its own as the disk fills, so Rust builds
 don't fill up your disk. QuickRust brings its own toolchains, runs the toolchain's own Cargo and
 rustc, and records every build, so it can tell you where the time and the disk space went.
Download QuickRust
All downloads
 Your first build
 Commands
 All documentation
A build, through QuickRust
 $ cargo build
OK Built: 12 compiled, 140 fresh, 37 restored from QuickRust's cache [4.21s]
WARN 23 warnings in app and util: unused_variables x17, dead_code x4, unused_imports x1, +1 more; `qrust warnings` shows them
and then, about that build
Answers
 qrust warnings # the warnings it counted, in full
qrust analyze # everything about the latest build
qrust analyze rebuilds # why each crate rebuilt
qrust path # where the build went
qrust upstream build # the toolchain's own Cargo, nothing added
Faster by default
Lighter debug information, rustc's parallel frontend, a shared artifact cache and early cut-off. The program you build behaves exactly the same.
One cache, minding the disk
No target/ in your projects: builds live in one central cache shared by every checkout. It keeps under a size limit and, as the disk fills, frees the least recently used first.
Output you can read
One status line, errors in full, warnings counted and kept, one line per outcome.
Answers about builds
The critical path, why each crate rebuilt, duplicated dependencies, build scripts and macros, cache behaviour, disk use.
Its own toolchains
It downloads and manages Rust toolchains itself: rust-toolchain.toml and +toolchain choose, as with rustup.
MachineFabric
FabricLoom
Overview
 Downloads
 Documentation
CapDAG
Overview
 Downloads
 Documentation
 Registry
lungo
Overview
 Downloads
 Documentation
QuickRust
Overview
 Downloads
 Documentation
Resources
Cartridges
 Models
 Blog
 News
 Supporters
 Whitepaper
 Pitch deck
Contribute
Submit a cartridge
 Suggest a model
 Propose a definition
Connect
hello@ machinefabric.com
Discord
Mastodon
GitHub
© 2026 MachineFabric. Made with ❤️ in Caserta, Southern Italy.
Privacy
 Terms
 Cookies
 Cookie settings
Light
 Auto
 Dark

## 评论（1/1）

> **joeharshamshiri** · 2026-10-25T23:15:45.000Z　
> A drop-in replacement for the cargo command that makes Rust builds faster, with nothing to configure. Every build goes into one centrally managed cache, which stays within its limits and gives space back on its own as the disk fills, so Rust builds don't fill up your disk. QuickRust brings its own toolchains, runs the toolchain's own Cargo and rustc, and records every build, so it can tell you where the time and the disk space went.

## 导航

- 项目页：[[10-项目/machinefabric.com_e36b4bfe]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
