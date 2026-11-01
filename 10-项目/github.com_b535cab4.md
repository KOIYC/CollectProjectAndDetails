---
type: "project"
title: "Show HN: Maclet – A native macOS container runtime written from scratch in Rust"
project_url: "https://github.com/sumant1122/maclet"
first_seen: "2026-11-01T09:38:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_paperplaneflyr
  - story_50317580
  - show_hn
lang: "en"
---

# Show HN: Maclet – A native macOS container runtime written from scratch in Rust

> [!info] 一句话导读
> Native macOS container runtime written in Rust using Apple Virtualization Framework, Linux namespaces, cgroups v2, and OverlayFS

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sumant1122/maclet>
> 首次收录：2026-11-01T09:38:09+08:00
> 来源渠道：HN Show HN
> 标签：author_paperplaneflyr, story_50317580, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:38:09+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-01/26bfc7c90d08f170_Show-HN-Maclet-–-A-native-macOS-container-runtime]] |

## 摘要正文

# sumant1122/maclet  Native macOS container runtime written in Rust using Apple Virtualization Framework, Linux namespaces, cgroups v2, and OverlayFS  - Stars: 4 - Forks: 0 - Watchers: 4 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-10-31T03:30:52Z  ## Languages  - C - Makefile - Rust - Swift  ## Topics  - apple-silicon - cgroups-v2 - container-runtime - containers - linux-namespaces - macos - oci - overlayfs - rust - virtualization  ## Top Contributors  - sumant1122 (10 contributions)  ---  ## README  # Maclet  **Maclet** is a native macOS container runtime written in Rust. It creates, runs, and isolates Linux containers without depending on Docker Desktop, Colima, or containerd.  > **The Elevator Pitch:** > *Docker Desktop on macOS is a multi-gigabyte, proprietary suite wrapping legacy orchestration daemons. **Maclet** is a native, ultra-lightweight container runtime written from scratch in Rust and Swift specifically for Apple Silicon. Instead of wrapping Docker Engine or containerd, Maclet talks directly to Apple's Virtualization Framework and implements Linux kernel isolation primitives (namespaces, cgroups v2, OverlayFS, and bridge netw…
