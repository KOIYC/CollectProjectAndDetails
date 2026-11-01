---
type: "corpus"
item_id: "26bfc7c90d08f170"
title: "Show HN: Maclet – A native macOS container runtime written from scratch in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50317580"
project_url: "https://github.com/sumant1122/maclet"
author: "paperplaneflyr"
published_at: "2026-10-31T16:28:58Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_paperplaneflyr
  - story_50317580
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Maclet – A native macOS container runtime written from scratch in Rust

> [!info] 一句话导读
> Native macOS container runtime written in Rust using Apple Virtualization Framework, Linux namespaces, cgroups v2, and OverlayFS

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50317580>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：paperplaneflyr　|　发布：2026-10-31T16:28:58Z
> 项目链接：<https://github.com/sumant1122/maclet>
> 采集：2026-11-01T09:38:09+08:00　|　id：`26bfc7c90d08f170`

## 正文

# sumant1122/maclet

Native macOS container runtime written in Rust using Apple Virtualization Framework, Linux namespaces, cgroups v2, and OverlayFS

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-10-31T03:30:52Z

## Languages

- C
- Makefile
- Rust
- Swift

## Topics

- apple-silicon
- cgroups-v2
- container-runtime
- containers
- linux-namespaces
- macos
- oci
- overlayfs
- rust
- virtualization

## Top Contributors

- sumant1122 (10 contributions)

---

## README

# Maclet

**Maclet** is a native macOS container runtime written in Rust. It creates, runs, and isolates Linux containers without depending on Docker Desktop, Colima, or containerd.

> **The Elevator Pitch:**
> *Docker Desktop on macOS is a multi-gigabyte, proprietary suite wrapping legacy orchestration daemons. **Maclet** is a native, ultra-lightweight container runtime written from scratch in Rust and Swift specifically for Apple Silicon. Instead of wrapping Docker Engine or containerd, Maclet talks directly to Apple's Virtualization Framework and implements Linux kernel isolation primitives (namespaces, cgroups v2, OverlayFS, and bridge networking) with zero bloat and sub-second boot times.*

---

## Key Differentiators: What Makes Maclet Unique?

| Dimension | Docker Desktop | Colima / Lima | **Maclet** |
|---|---|---|---|
| **Core Engine** | Docker Daemon + `containerd` + `runc` | QEMU / Lima + `containerd` | **Ground-up Rust runtime (Direct Linux Syscalls)** |
| **VM Backend** | HyperKit / Apple VZ (Heavy VM) | QEMU / Apple VZ | **Apple Virtualization Framework via Swift C-FFI** |
| **Idle Memory** | ~2.0 GB – 4.0 GB | ~800 MB – 1.5 GB | **< 150 MB** |
| **Binary Size** | ~1.5 GB+ (with Electron) | Hundreds of MBs | **~3.6 MB (Single Rust binary)** |
| **Boot Time** | 10 – 30+ seconds | 5 – 15 seconds | **Sub-second (~800ms)** |
| **Dependency Model** | Wraps existing engines | Wrapper script around containerd | **Independent: Owns namespaces, cgroups, OverlayFS & OCI** |
| **Licensing** | Proprietary paid subscription | Open source | **100% Free & Open Source (Apache 2.0 / MIT)** |

---

## Architecture Overview

```
maclet CLI (macOS)
       │
       ▼ (Unix Domain Socket: ~/.maclet/maclet.sock)
maclet Daemon / maclet-vm
       │
       ▼ (Apple Virtualization Framework via Swift C-FFI)
Linux ARM64 Guest VM
       │
       ▼ (Virtio Console Channel: /dev/hvc1)
maclet-guest-agent (Rust static binary as PID 1)
       │
       ├─► Linux Namespaces (PID, Mount, Net, IPC, UTS)
       ├─► cgroups v2 Quotas (cpu.max, memory.max, pids.max)
       ├─► Storage: OverlayFS (lower/upper/work/merged) & pivot_root
       ├─► Network: maclet0 Bridge, Veth pairs, Netns, NAT Masquerading, Port Forwarding
       ├─► Security: Capability bounding set dropping, PR_SET_NO_NEW_PRIVS, Read-Only Rootfs
       └─► Containerized Processes
```

---

## Features Implemented Across All 8 Phases

| Phase | Subsystem | Features |
|---|---|---|
| **Phase 1** | **VM Boot & IPC** | Apple Virtualization Framework backend (`apple-vz` Swift FFI), ARM64 Linux VM boot, Virtio console IPC channel (`/dev/hvc1`), newline-delimited JSON RPC protocol. |
| **Phase 2** | **First Container** | Direct Linux process isolation (`CLONE_NEWPID`, `CLONE_NEWNS`, `CLONE_NEWUTS`, `CLONE_NEWIPC`), `pivot_root`, fresh `/proc`, `/sys`, `/dev` mounts. |
| **Phase 3** | **Resource Controls** | cgroups v2 hierarchy (`/sys/fs/cgroup/maclet/`), memory limits (`--memory`), CPU quotas (`--cpus`), process limits (`--pids-limit`), live metrics accounting (`maclet stats`). |
| **Phase 4** | **Container Lifecycle** | Detached background containers (`-d`), multiple concurrent containers, container ID prefix/name matching, `maclet ps -a`, `maclet exec` (via `setns()`), `maclet logs`, `maclet inspect`, `maclet stop`, `maclet rm -f`. |
| **Phase 5** | **Storage & Image Management** | OCI registry client with multi-arch manifest resolution (`linux/arm64`), streaming layer download & SHA256 verification (`maclet pull`), local image registry (`maclet images`), OverlayFS copy-on-write storage per container. |
| **Phase 6** | **Container Networking** | `maclet0` Linux bridge (`10.88.0.1/16`), IPAM allocation, veth pairs moved to container netns, loopback & default gateway routing, guest NAT masquerading, automatic DNS configuration, and port forwarding (`-p host:container`). |
| **Phase 7** | **Security & Hardening** | Capability bounding set dropping (`CAP_SYS_ADMIN`, `CAP_SYS_MODULE`, etc.), `PR_SET_NO_NEW_PRIVS` enforcement, immutable root filesystems (`--read-only`), hypervisor isolation boundary. |
| **Phase 8** | **Production Readiness** | System diagnostics (`maclet system info`), comprehensive unit tests, end-to-end VM boot and execution test suite (`make test`), complete architecture and subsystem documentation. |

---

## Project Structure

```text
maclet/
├── Cargo.toml
├── Makefile
├── README.md
├── LICENSE
├── entitlements.plist
│
├── docs/
│   ├── architecture.md           # System architecture & data flow
│   ├── technical-constraints.md  # Darwin limits & hypervisor workarounds
│   ├── apple-vz-research.md      # Apple Virtualization Framework internals
│   ├── kernel-configuration.md   # Minimum Linux kernel config
│   ├── host-guest-protocol.md    # Framed JSON wire protocol spec
│   ├── container-lifecycle.md    # Container state machine & OverlayFS
│   ├── crate-boundaries.md       # Rust crate dependency structure
│   ├── security.md               # Hardware/kernel security model & capabilities
│   ├── networking.md             # Bridge, veth, netns, NAT & port forwarding
│   ├── vm-management.md          # VM configuration, booting & lifecycle
│   ├── implementation-roadmap.md # Phased implementation roadmap
│   └── risk-analysis.md          # Architectural risks & mitigations
│
├── crates/
│   ├── maclet-common/            # Protocol models, errors, container configs
│   ├── maclet-ipc/               # Async & sync newline-framed JSON stream
│   ├── maclet-vm/                # Apple Virtualization Framework Rust wrapper
│   ├── maclet-cli/               # CLI interface (clap) & daemon manager
│   ├── maclet-namespaces/        # Linux namespace unshare & pivot_root
│   ├── maclet-cgroups/           # Linux cgroups v2 controllers & resource metrics
│   ├── maclet-storage/           # Linux OverlayFS storage & COW layers
│   ├── maclet-network/           # Bridge, veth pair, netns, NAT & port forwarding
│   ├── maclet-image/             # OCI image pull, layer unpack & registry
│   ├── maclet-container/         # Container state machine & supervisor
│   └── maclet-guest-agent/       # Statically linked Linux init & agent
│
├── virtualization/
│   └── apple-vz/                 # Swift FFI wrapper around VZVirtualMachine
│       ├── include/apple_vz.h
│       └── Sources/apple_vz.swift
│
└── guest/                        # Kernel and initramfs tooling
```

---

## Quickstart

### Prerequisites

1. macOS running on Apple Silicon (ARM64).
2. Xcode Command Line Tools (`xcode-select --install`).
3. Rust (`rustup default stable` and `rustup target add aarch64-unknown-linux-musl`).

### Build & Test

```bash
# Build release binaries (CLI and guest agent) and sign with virtualization entitlement
make release

# Run all unit tests and the end-to-end VM boot and execution test
make test
```

---

## CLI Command Reference

### VM Machine Management

```bash
# 1. Initialize environment (prepares Linux kernel, minirootfs & builds guest agent)
maclet machine init

# 2. Start the Linux micro-VM in the background
maclet machine start --daemon

# 3. Check VM and guest agent status
maclet machine status

# 4. Inspect system info and hypervisor status
maclet system info

# 5. Stop the VM
maclet machine stop
```

### Image Management

```bash
# Pull an OCI image from Docker Hub / registry
maclet pull alpine:latest
maclet pull ubuntu:24.04

# List locally cached images
maclet images
```

### Container Execution & Lifecycle

```bash
# Run an ephemeral container
maclet run alpine:latest uname -a

# Run a detached background container with custom name and port forwarding
maclet run -d --name web-server -p 8080:80 alpine:latest /bin/sh -c "while true; do sleep 1; done"

# Run with resource limits (cgroups v2)
maclet run --memory 256m --cpus 1.5 --pids-limit 50 alpine:latest /bin/sh

# Run with hardened security (read-only rootfs)
maclet run --read-only alpine:latest /bin/sh

# List running containers (or all containers with -a)
maclet ps
maclet ps -a

# Execute a command inside a running container (via namespaces setns)
maclet exec web-server ps aux

# View container logs
maclet logs web-server

# Inspect container state and configuration
maclet inspect web-server

# View live cgroup resource statistics (CPU, Memory, PIDs)
maclet stats web-server

# Stop a running container
maclet stop web-server

# Remove a container
maclet rm -f web-server
```

---

## Running Automated Tests

```bash
# Run the complete test suite (unit tests + e2e boot test)
make test
```

The test suite validates:
- IPC framed serialization and deserialization across sockets.
- OCI image reference parsing (Docker Hub, official library shortcuts, custom registries).
- Cgroups v2 controller path generation and metric parsers.
- Linux namespace unshare flags and configuration mapping.
- Swift FFI bridging and configuration validation.
- End-to-end VM boot, agent handshake, and command execution on Apple Silicon.

---

## Who is Maclet for?

1. **Apple Silicon Developers**: Engineers who want fast, responsive container workflows without their MacBook fans spinning up or battery draining from bloated virtualization stacks.
2. **Teams Looking to Escape Docker Licensing**: Organizations seeking to eliminate recurring per-seat Docker Desktop enterprise subscription fees while retaining high developer velocity.
3. **Systems & Rust Enthusiasts**: Developers who appreciate clean, auditable systems where the entire stack—from Swift hypervisor calls to Linux namespaces and cgroups—is written in clean, modern Rust with zero hidden daemon dependencies.

# GitHub - Koppar-AI/koppar-lte-modem: A phone line over USB-C: LTE data, SMS and voice calls with the call audio on USB. A 4-layer KiCad board designed by Koppar from a one-page spec. · GitHub

## 评论（1/1）

> **manjian2006** · 2026-10-31T23:22:38.000Z　
> Why all the containers share the same vm instead of the Apple's container which startup a light weight vm for each container?

## 导航

- 项目页：[[10-项目/github.com_b535cab4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
