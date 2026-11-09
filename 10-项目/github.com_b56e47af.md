---
type: "project"
title: "Show HN: A kernel written in Rust that can boot Ubuntu with Plasma desktop"
project_url: "https://github.com/ozkl/ruxis"
first_seen: "2026-11-09T09:55:49+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ozkl
  - story_50417467
  - show_hn
lang: "en"
---

# Show HN: A kernel written in Rust that can boot Ubuntu with Plasma desktop

> [!info] 一句话导读
> License: MIT License

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ozkl/ruxis>
> 首次收录：2026-11-09T09:55:49+08:00
> 来源渠道：HN Show HN
> 标签：author_ozkl, story_50417467, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-09/51c285d62b86eb22_Show-HN-A-kernel-written-in-Rust-that-can-boot-Ubu]] |
| 2026-11-09T09:55:49+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-09/51c285d62b86eb22_Show-HN-A-kernel-written-in-Rust-that-can-boot-Ubu]] |

## 摘要正文

# ozkl/ruxis  A Kernel in Rust  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-08T19:45:52Z  ## Languages  - C - GDB - Linker Script - Python - Rust - Shell  ## Top Contributors  - ozkl (2 contributions)  ---  ## README  # ruxis  A Unix-like kernel written in Rust that runs unmodified Linux programs. ruxis is not Linux; it is compatible with Linux's user space. It runs on x86_64 and arm64 (aarch64) and boots with UEFI through Limine.  ruxis was written by Claude Opus 5.5.  ruxis implements Linux's system call interface, so programs built for Linux run on it as they are. That includes a whole Ubuntu 24.04 system:  - **Ubuntu with systemd** as init, logind sessions, udev, dbus and  networking - **Desktops**: GNOME, KDE Plasma and Weston on Wayland, with Firefox - **Everyday programs**: bash, coreutils, Python 3, gcc (compiling inside  ruxis), nginx, busybox, ssh, git, rustup - **Containers**: mount, PID, network, user and other namespaces, cgroup  v2, seccomp  Inside the kernel: SMP and preemptive scheduling; ext4 with its journal; IPv4/IPv6 TCP/UDP networking; virtio, AHCI, NVMe, USB and Intel/Realtek network dri…
