---
type: "project"
title: "Show HN: AionOS – self-healing microkernel in Zig (boots on real hardware)"
project_url: "https://github.com/rodancz/aion"
first_seen: "2026-09-21T02:52:57+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rodancz
  - story_48326600
  - show_hn
lang: "en"
---

# Show HN: AionOS – self-healing microkernel in Zig (boots on real hardware)

> [!info] 一句话导读
> Aion — AI self-healing microkernel. Detects crashes, analyzes them via AI, hot-patches the kernel in under 2 seconds.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/rodancz/aion>
> 首次收录：2026-09-21T02:52:57+08:00
> 来源渠道：HN Show HN
> 标签：author_rodancz, story_48326600, show_hn
> 最新指标：点赞=6 · 评论=1 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/4db6e44ac2377aae_Show-HN-AionOS-–-self-healing-microkernel-in-Zig-(]] |
| 2026-09-21T01:43:56+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/4db6e44ac2377aae_Show-HN-AionOS-–-self-healing-microkernel-in-Zig-(]] |
| 2026-09-21T02:52:57+08:00 | HN Show HN | 点赞=6 · 评论=1 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-21/4db6e44ac2377aae_Show-HN-AionOS-–-self-healing-microkernel-in-Zig-(]] |

## 摘要正文

# rodancz/aion  Aion — AI self-healing microkernel. Detects crashes, analyzes them via AI, hot-patches the kernel in under 2 seconds.  - Stars: 12 - Forks: 0 - Watchers: 12 - Open issues: 0 - Default branch: master - Created: 2026-05-29T11:36:31Z  ## Languages  - Assembly - Linker Script - Python - Shell - Zig  ---  ## README  # AionOS — Self-Healing Microkernel  A small operating system written in Zig that can survive crashes. Layer 3 crashes — the watchdog notices, the AI daemon picks a fix, and the kernel swaps in a working module. No reboot needed.  **v0.1.0-alpha** — ~6500 lines of Zig. Boots in QEMU.  ## What it does  1. **Boots to a shell** — 24 commands, text editor, filesystem, networking 2. **Survives crashes** — watchdog detects dead Layer 3 in <2 seconds 3. **Classifies the fault** — AI daemon picks a recovery action (local keywords or API) 4. **Swaps the module** — switches from crashable v1 to crash-resistant v2 at runtime 5. **Stays up** — same crash command that killed it before now gets ignored  ## Proof it works  ```bash ./scripts/boot-check.sh     # Builds, boots in QEMU, confirms shell appears ./scripts/demo-test.py      # 8 automated checks — progressive harden…
