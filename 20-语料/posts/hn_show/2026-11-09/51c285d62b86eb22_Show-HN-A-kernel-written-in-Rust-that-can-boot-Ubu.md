---
type: "corpus"
item_id: "51c285d62b86eb22"
title: "Show HN: A kernel written in Rust that can boot Ubuntu with Plasma desktop"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50417467"
project_url: "https://github.com/ozkl/ruxis"
author: "ozkl"
published_at: "2026-11-08T21:25:54Z"
captured_at: "2026-11-09T09:55:49+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_ozkl
  - story_50417467
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: A kernel written in Rust that can boot Ubuntu with Plasma desktop

> [!info] 一句话导读
> License: MIT License

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50417467>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ozkl　|　发布：2026-11-08T21:25:54Z
> 项目链接：<https://github.com/ozkl/ruxis>
> 采集：2026-11-09T09:55:49+08:00　|　id：`51c285d62b86eb22`

## 正文

# ozkl/ruxis

A Kernel in Rust

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-08T19:45:52Z

## Languages

- C
- GDB
- Linker Script
- Python
- Rust
- Shell

## Top Contributors

- ozkl (2 contributions)

---

## README

# ruxis

A Unix-like kernel written in Rust that runs unmodified Linux programs.
ruxis is not Linux; it is compatible with Linux's user space. It runs on
x86_64 and arm64 (aarch64) and boots with UEFI through
Limine.

ruxis was written by Claude Opus 5.5.

ruxis implements Linux's system call interface, so programs built for
Linux run on it as they are. That includes a whole Ubuntu 24.04 system:

- **Ubuntu with systemd** as init, logind sessions, udev, dbus and
 networking
- **Desktops**: GNOME, KDE Plasma and Weston on Wayland, with Firefox
- **Everyday programs**: bash, coreutils, Python 3, gcc (compiling inside
 ruxis), nginx, busybox, ssh, git, rustup
- **Containers**: mount, PID, network, user and other namespaces, cgroup
 v2, seccomp

Inside the kernel: SMP and preemptive scheduling; ext4 with its journal;
IPv4/IPv6 TCP/UDP networking; virtio, AHCI, NVMe, USB and Intel/Realtek
network drivers; DRM/KMS; evdev input; and a real TTY layer with a
framebuffer console. Drivers can also be loadable modules. See the
feature list for details.

https://github.com/user-attachments/assets/3fa1ea33-b9ca-4aec-8e68-54b3e34128ac

## Quick start

You need rustup (the toolchain installs itself;
stable Rust), `git`, and QEMU with UEFI firmware:

| Host | Install |
| --- | --- |
| Debian, Ubuntu | `apt install qemu-system-x86 ovmf` |
| Fedora | `dnf install qemu-system-x86 edk2-ovmf` |
| Arch | `pacman -S qemu-system-x86 edk2-ovmf` |
| macOS | `brew install qemu` |
| Windows | the QEMU installer |

```sh
cargo xtask run                    # build, make the boot image, boot it in QEMU
cargo xtask test                   # boot with the self tests, report pass/fail
cargo xtask run --arch aarch64     # the same on arm64 (qemu-system-aarch64, AAVMF)
```

A QEMU window shows the console (`tty1`), and your terminal is the serial
console (`ttyS0`). `Ctrl-A X` quits. Add `--accel kvm` (`hvf` on macOS,
`whpx` on Windows) for hardware virtualisation.

On x86_64 the QEMU window has two displays: the text console on the
standard VGA one, and a virtio-gpu one for graphics (desktops and other
programs using `/dev/dri/card0`). Once a desktop starts, switch to the
virtio-gpu display in the window's **View** menu.

To boot a full Ubuntu with a desktop (needs Docker or Podman to build the
image):

```sh
cargo xtask image
tools/ubuntu-rootfs.sh ruxis-gnome.img x86_64 8G gnome    # or plasma, or no desktop
cargo xtask run --root-disk ruxis-gnome.img --accel kvm
```

## Drivers

ruxis has its own driver model. It isn't Linux's, and it aims for a
stable binary interface, which Linux deliberately doesn't have. Drivers
are built against a versioned driver model (version 1 now), not against
the kernel's internals, so later kernels can load drivers built for
earlier ones, including binary drivers from outside this repository.
While ruxis is young (0.x), the driver model may still change.

Loadable drivers are `.ko` files, named and installed like Linux modules
(`/lib/modules/ /`) so that `depmod`, `modinfo`, `modprobe` and
udev handle them unchanged. They are not Linux modules, though: ruxis
can't load Linux's `.ko` files, and Linux can't load ruxis's. See
dm/README.md for writing one.

## Documentation

| | |
| --- | --- |
| Features | what the kernel does, subsystem by subsystem |
| Running | QEMU options, kernel command line, disks, network, adding programs |
| Images | the boot image, Ubuntu root file systems and desktops, real hardware |
| Testing | the self tests, and comparing with Linux (`syscompare`) |
| Architecture | design, internals and roadmap |
| Drivers | the driver model, and writing loadable drivers |

## Versions

ruxis 0.1.0 implements the system call interface of Linux 6.6, so
`uname -r` says `6.6.0-ruxis`. Programs check that version before they
use newer kernel features. ruxis's own version and build time are in
`uname -v` and `/proc/version`.

## License

MIT, see LICENSE. The console font is the X11 misc-fixed 8x13
font, which is public domain.

## 关联链接

- https://github.com/user-attachments/assets/3fa1ea33-b9ca-4aec-8e68-54b3e34128ac

## 导航

- 项目页：[[10-项目/github.com_b56e47af]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
