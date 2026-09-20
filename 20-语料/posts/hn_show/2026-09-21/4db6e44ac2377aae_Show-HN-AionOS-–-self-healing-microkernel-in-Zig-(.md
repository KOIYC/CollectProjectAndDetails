---
type: "corpus"
item_id: "4db6e44ac2377aae"
title: "Show HN: AionOS – self-healing microkernel in Zig (boots on real hardware)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48326600"
project_url: "https://github.com/rodancz/aion"
author: "rodancz"
published_at: "2026-05-29T17:42:31Z"
captured_at: "2026-09-21T02:52:57+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_rodancz
  - story_48326600
  - show_hn
metrics: {"points": 6, "comments": 1, "engagement_velocity": 6}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: AionOS – self-healing microkernel in Zig (boots on real hardware)

> [!info] 一句话导读
> Aion — AI self-healing microkernel. Detects crashes, analyzes them via AI, hot-patches the kernel in under 2 seconds.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48326600>
> 指标：点赞=6 · 评论=1 · engagement_velocity=6
> 作者：rodancz　|　发布：2026-05-29T17:42:31Z
> 项目链接：<https://github.com/rodancz/aion>
> 采集：2026-09-21T02:52:57+08:00　|　id：`4db6e44ac2377aae`

## 正文

# rodancz/aion

Aion — AI self-healing microkernel. Detects crashes, analyzes them via AI, hot-patches the kernel in under 2 seconds.

- Stars: 12
- Forks: 0
- Watchers: 12
- Open issues: 0
- Default branch: master
- Created: 2026-05-29T11:36:31Z

## Languages

- Assembly
- Linker Script
- Python
- Shell
- Zig

---

## README

# AionOS — Self-Healing Microkernel

A small operating system written in Zig that can survive crashes.
Layer 3 crashes — the watchdog notices, the AI daemon picks a fix,
and the kernel swaps in a working module. No reboot needed.

**v0.1.0-alpha** — ~6500 lines of Zig. Boots in QEMU.

## What it does

1. **Boots to a shell** — 24 commands, text editor, filesystem, networking
2. **Survives crashes** — watchdog detects dead Layer 3 in <2 seconds
3. **Classifies the fault** — AI daemon picks a recovery action (local keywords or API)
4. **Swaps the module** — switches from crashable v1 to crash-resistant v2 at runtime
5. **Stays up** — same crash command that killed it before now gets ignored

## Proof it works

```bash
./scripts/boot-check.sh     # Builds, boots in QEMU, confirms shell appears
./scripts/demo-test.py      # 8 automated checks — progressive hardening
```

In the QEMU shell, try this:

```
aion> crash          # v1: crash kills L3 -> recovery -> v1->v2 (shell blocked)
aion> crash          # v2 blocks it: "blocks this crash type — ignored"
aion> crash-vfs      # v2: vfs still open -> recovery -> v2->v3 (vfs blocked)
aion> crash-vfs      # v3 blocks it
aion> crash-net      # v3: net still open -> recovery -> v3->v4 (all blocked)
aion> crash-net      # v4 blocks it
aion> fault          # Real CPU exception (ud2) — always fires, bypasses modules
aion> stat           # Dashboard: module v4, 3 crashes, 3 upgrades
```

## Architecture

```
Microkernel (stable)
├── Watchdog — heartbeat monitor, flags crashes
├── AI Daemon — classifies fault → picks safe action
├── Module table — v1 (crashable) → v2 (crash-resistant)
├── VMM / PMM / kmalloc — memory
├── VFS (ramfs) + FAT32 (disk) — filesystem
├── e1000 + DHCP + TCP + DNS + HTTP — networking
├── SHA-256 + AES-128 + RSA-2048 + TLS 1.2 — crypto
└── PS/2 keyboard + VGA + framebuffer — display
```

## Commands

```
FILES:  ls  cd  mkdir  cat  write  rm  edit  echo
DISK:   save  load  storage
SYS:    info  who  mem  uptime  ver  clear  logo  reboot
L3:     modules  upgrade  crash  crash-vfs  crash-net  fault  rebuild
NET:    net  ip  ai
PCI:    pci
```

## Recovery actions

The AI daemon classifies crashes into one of four actions:

| Action | When | Source |
|--------|------|--------|
| `restart_layer3` | Default fallback | Any crash → restart + upgrade module |
| `reset_vfs` | Filesystem crash keywords | `src/ai/daemon.zig:classify_local()` |
| `reset_network` | Network crash keywords | `src/ai/daemon.zig:classify_local()` |
| `no_action` | False alarm | No restart needed |

If an OpenAI-compatible API is configured, the daemon asks the model to pick one.
Otherwise it uses keyword matching locally. The API **chooses from the menu** —
it cannot generate arbitrary code.

## Build

```bash
# Requires: Zig 0.15+, NASM, grub-mkrescue
zig build
./run.sh          # creates aion.iso
./run_qemu.sh     # boots in QEMU
```

## Install to USB

```bash
sudo dd if=aion.iso of=/dev/sdX bs=1M status=progress && sync
# or: sudo ./install.sh
```

Boot in UEFI mode (disable Secure Boot).

## Roadmap (what's next)

- Real `reset_vfs` and `reset_network` recovery implementations
- Crash from actual page faults (not just the `crash` command)
- More modules in the table (v3, v4...)
- Serial console for headless recovery
- Multi-process isolation

## License

MIT

# GitHub - njbrake/dotpi: My ds4 + pi configuration for success · GitHub

## 评论（1/1）

> **veneficium** · 2026-05-31T10:36:29.000Z　
> > self-healing
> look inside
> > HTTP calls to external LLM

## 导航

- 项目页：[[10-项目/github.com_ef10b4bd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
