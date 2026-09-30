---
type: "project"
title: "Show HN: Clx 0.4.0 – native compiler for Lua"
project_url: "https://samyeyo.github.io/clx"
first_seen: "2026-09-30T18:57:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author__samt_
  - story_49899464
  - show_hn
lang: "en"
---

# Show HN: Clx 0.4.0 – native compiler for Lua

> [!info] 一句话导读
> Compile Lua into fast, standalone native executables.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://samyeyo.github.io/clx>
> 首次收录：2026-09-30T18:57:07+08:00
> 来源渠道：HN Show HN
> 标签：author__samt_, story_49899464, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/423fe8e00d528685_Show-HN-Clx-0.4.0-–-native-compiler-for-Lua]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-30/423fe8e00d528685_Show-HN-Clx-0.4.0-–-native-compiler-for-Lua]] |

## 摘要正文

cl x Compile Lua into fast, standalone native executables. No interpreter. No virtual machine. No dependencies. Just a native binary, faster than standard Lua. Discover clx $ clx hello.lua $ ./hello Hello from clx! cl x  v0.4.0 Overview Features Installation Benchmarks Getting Started Dynamic execution CLI Reference Modules Compatibility Copyright © 2026 - Tine Samir GitHub Compile Lua into Fast, Standalone Native Executables clx is an ahead-of-time (AOT) Lua compiler and runtime for Linux, macOS, and Windows. It turns your Lua 5.5 scripts into fast, self-contained native binaries — no interpreter, no virtual machine, and no runtime dependencies to ship. Build once, and your program runs instantly, anywhere. Everything you already know about Lua just works: the full language, standard libraries, and coroutines. When you need to load code at runtime, clx's optional dynamic mode will run a Lua virtual machine alongside your compiled code, giving you the best of both worlds: speed and flexibility. Binary modules are supported, but must be compiled with the clx C++ API. See the Modules section for more information. Multiplatform Lua compiler C++20 Backend MIT Open Source License Lua 5.…
