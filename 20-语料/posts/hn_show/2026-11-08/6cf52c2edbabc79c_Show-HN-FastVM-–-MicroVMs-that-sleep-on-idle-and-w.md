---
type: "corpus"
item_id: "6cf52c2edbabc79c"
title: "Show HN: FastVM – MicroVMs that sleep on idle and wake when packets arrive"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50403001"
project_url: "https://github.com/tuananh/fastvm"
author: "tuananh"
published_at: "2026-11-07T09:26:45Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_tuananh
  - story_50403001
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: FastVM – MicroVMs that sleep on idle and wake when packets arrive

> [!info] 一句话导读
> Fully vibed. Read the idea, ignore the code please :)

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50403001>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：tuananh　|　发布：2026-11-07T09:26:45Z
> 项目链接：<https://github.com/tuananh/fastvm>
> 采集：2026-11-08T12:50:31+08:00　|　id：`6cf52c2edbabc79c`

## 正文

# tuananh/fastvm

Fully vibed. Read the idea, ignore the code please :)

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: main
- Created: 2026-11-07T09:13:00Z

## Languages

- C
- Go
- Makefile
- Shell

---

## README

# fastvm

A single-host micro-VM sandbox runtime: sandboxes boot in ~100 ms, sleep
themselves when idle, page their memory to disk, and wake themselves when a
packet arrives — with the frame already queued in the guest's own virtio-net
path.

`fastvm` is implemented in Go on top of Firecracker/KVM. The design lives in
GOAL.md; the full step-by-step walkthrough is
GETTING_STARTED.md.

> Status: **v0.1 core implemented and tested end-to-end on KVM**. Working:
> Dockerfile→ext4 base disks, copy/reflink CoW volumes, real Firecracker boot
> with guest agent over vsock, pause/dormant (memory file)/wake, idle predicate
> and auto-sleep, HTTP API + CLI, and a Linux-bridge L2 data plane with
> wake-on-network. The eBPF L2 switch backend is implemented and tested
> standalone but is not wired into the daemon yet (see Known limitations).
> Real-VM e2e suites pass in seconds; see the test matrix below.

## What it does

- **Fast VMs** — one Firecracker microVM per sandbox.
- **Dockerfile images** — `fastvm build` turns a Dockerfile into a
 content-addressed ext4 base disk (BuildKit/docker → rootfs → ext4).
- **CoW runtime volumes** — each sandbox gets a writable volume cloned from the
 base in milliseconds (reflink where available, copy fallback).
- **Self-managing lifecycle** — a debounced idle predicate (network + exec/API +
 block I/O + CPU) moves sandboxes Running → Idle → Paused → Dormant; no manual
 stop needed.
- **Pause / restore** — paused VMs keep their virtio-net queue live; dormant VMs
 hand guest RAM to a Firecracker memory file (mmap restore) and keep the VMM
 and device queue alive, so an incoming packet is queued and consumed on wake.
- **L2 networking** — per-host Linux bridge with AF_PACKET wake detection and
 nftables DNAT. An eBPF L2 switch backend (tc, static MAC→port forwarding,
 per-port isolation/anti-spoofing, counters, ringbuf wake events) is
 implemented and validated in isolation, but not yet wired into the
 TAP/bridge topology (see Known limitations).

## Requirements

- Linux x86_64 with KVM (`/dev/kvm` accessible).
- Firecracker v1.10+ (v1.17 tested).
- Go 1.24+ to build.
- **root / `CAP_NET_ADMIN`** for TAP/bridge/nftables (needed to boot sandboxes
 and for published ports). The daemon always uses the Linux bridge for the
 data plane and wake detection; `CAP_BPF` is only needed to run the standalone
 eBPF backend tests.
- Optional: docker/BuildKit for `fastvm build`, clang/llc/bpftool for the eBPF
 switch, e2fsprogs for base disks.

## Build

```sh
make build          # bin/fastvm, bin/fastvmd, bin/fastvm-agent
make test           # unit tests (skips privileged/gated tests cleanly)
make test-race      # unit tests under the race detector
make assets         # download kernel + alpine rootfs for e2e tests
make e2e            # real Firecracker boot/pause/dormant/wake e2e
```

## Quickstart

Full walkthrough (build, config, image, sandbox, wake-on-network):
**GETTING_STARTED.md**.

Fastest demo — builds a sandbox, lets it auto-sleep, wakes it with `curl`
(needs root + docker + `make assets`):

```sh
make build && make assets
sudo make demo          # same as: sudo ./hack/demo-wake.sh
```

Or start the daemon with the checked-in demo config and drive it yourself:

```sh
sudo -s                 # run daemon and CLI as root
cd /path/to/fastvm
bin/fastvmd -config hack/config.yaml &

export FASTVM_SOCKET=/run/fastvm/fastvm.sock
make image                      # builds hack/Dockerfile.example -> demo:latest
bin/fastvm run --image demo:latest --name web --publish 8080:80 -- \
  /bin/sh -c 'echo hello > /tmp/index.html; exec /bin/busybox httpd -f -p 0.0.0.0:80 -h /tmp'
bin/fastvm ls
bin/fastvm exec web -- /bin/sh -c 'echo hello'
bin/fastvm sleep web --deep     # pause + offload guest RAM to disk
bin/fastvm wake web
bin/fastvm rm web
```

`hack/config.yaml` uses `/tmp` state and short idle windows for demos; copy it
to `/etc/fastvm/config.yaml` with `/var/lib/fastvm` paths for a real install.

The daemon API is HTTP/JSON over a unix socket (`/run/fastvm/fastvm.sock` by
default); `fastvm` is a thin client. Set `FASTVM_SOCKET` or `-socket` to point
the CLI at another socket.

## Configuration

See `internal/config/config.go` for the full schema. Defaults follow
GOAL.md §5.4:

```yaml
data_dir: /var/lib/fastvm
kernel_path: /var/lib/fastvm/kernels/vmlinux
agent_path: /var/lib/fastvm/agent/fastvm-agent

lifecycle:
  idle_window: 30s
  pause_after: 2m
  offload_after: 10m
  destroy_after: 24h
  on_workload_exit: idle

idle:
  cpu_threshold_pct: 1.0
  cpu_wake_pct: 5.0
  block_io_bytes: 65536
  keepalive_aware: true

memory:
  offload_mode: file     # file | uffd | swap | never

wake:
  max_wakes_per_minute: 6
  coalesce_window: 100ms

volume:
  cow: reflink           # reflink | dm-thin | copy

switch:
  mode: ebpf             # ebpf | bridge
```

## Tests

```sh
make test                                   # unit tests (no KVM/root needed)
make test-race                              # race detector
make assets                                 # kernel + alpine rootfs for e2e
FASTVM_E2E=1 go test -count=1 ./test/e2e/... ./internal/vmm/firecracker/...
FASTVM_NET_TESTS=1 go test -count=1 ./internal/network/...   # TAP/bridge/nft
FASTVM_DOCKER_TESTS=1 go test -count=1 ./internal/image/...   # Dockerfile build
```

How the e2e suites were verified in development:

| Suite | Command | Result |
|-------|---------|--------|
| Unit | `go test ./...` | green |
| Race | `go test -race ./...` | green |
| Real VM lifecycle | `FASTVM_E2E=1 go test ./test/e2e/ -run TestDaemonLifecycleRealVM` | PASS ~1.7 s: boot→agent→exec→pause→dormant snapshot/restore→wake→exec→delete |
| CLI/API over unix socket | `... -run TestCLIOverUnixSocket` | PASS ~2.1 s: run→ls→exec→deep sleep→wake→events→rm |
| Wake on network (real TAP) | `... -run TestDaemonNetworkWakeRealVM` | PASS ~1.8 s: boot with guest NIC, pause, TCP connect is queued and wakes the VM |
| Daemon binary | `... -run TestDaemonBinarySmoke` | PASS ~3 s: fastvmd starts with the demo config, CLI version/images/ls, clean SIGTERM |
| Driver-level snapshot | `FASTVM_E2E=1 go test ./internal/vmm/firecracker/ -run TestE2EFirecracker` | PASS ~6 s: pause freezes vCPUs, snapshot→restore paused, guest state intact |
| Docker build | `FASTVM_DOCKER_TESTS=1 go test ./internal/image/ -run TestBuildDocker` | PASS ~2.7 s: Dockerfile→rootfs→ext4, debugfs-verified contents |
| Bridge/TAP/nft | `FASTVM_NET_TESTS=1 go test ./internal/network/...` | PASS ~0.9 s (isolated network namespace) |

e2e tests skip cleanly when `/dev/kvm`, Firecracker, docker, or the downloaded
assets are missing. Network tests set up their own isolated namespace and skip
when the host does not allow it. eBPF load/attach tests run only with CAP_BPF;
without it the daemon logs the fallback and uses the Linux bridge.

## Layout

```
cmd/fastvm/            CLI client
cmd/fastvmd/           daemon
cmd/fastvm-agent/      guest agent (static, injected into base disks)
internal/api/          HTTP/JSON API
internal/build, image/ Dockerfile → OCI → ext4 base disk
internal/volume/       CoW runtime volumes
internal/vmm/          VMM interface; firecracker/ driver
internal/agent/        vsock wire protocol + host client
internal/network/      netns/veth/TAP/bridge/NAT + wake detection
internal/switch/       eBPF L2 switch backend (standalone; not wired yet)
internal/wake/         wake coalescing/rate limiting
internal/snapshot/     (mem-file restore is in the VMM driver today)
internal/lifecycle/    state machine + idle predicate
internal/daemon/       runtime orchestration
guest/                 guest init + workload config
bpf/                   L2 switch eBPF program
test/e2e/              gated end-to-end tests + asset fetch script
```

## Known limitations (v0.1)

- Single host only; no cross-host snapshots or deep sleep with the VMM exited.
- Memory offload modes implemented: `file` (default, Firecracker File-backend
 mmap restore) and `never`; `uffd`/`swap` are config-validated but rejected by
 the daemon for now.
- The eBPF L2 switch backend is implemented and validated in isolation
 (privileged tests), but it is **not wired into the daemon**: its tc ingress
 classifier is attached to the TAP, where host→guest frames are transmitted,
 not received — so it cannot see wake traffic. The daemon always uses the
 Linux bridge + AF_PACKET wake path. Wiring it requires the per-sandbox veth
 switch topology from GOAL.md §6.6.
- No per-sandbox network namespaces yet: TAPs share the daemon network
 namespace; isolation is Linux bridge port isolation plus static neighbor/DNAT
 rules. Full netns hardening is a later milestone.
- Snapshot restore does not reattach the guest serial console (Firecracker
 limitation); vsock reconnects on wake and exec/filesystem state is intact.
- Daemon restart: dormant sandboxes are adopted (network re-registered, memory
 file preserved) and wake lazily; sandboxes that were Running/Paused at restart
 are marked failed because the VMM process is not adopted yet.
- `dm-thin` CoW volumes are not implemented (`ErrDMThinUnsupported`); reflink
 and sparse-copy fallback are.
- Guest init assumes a POSIX shell + busybox `mount`; images without them need a
 custom `/init` via `init_path`.

# VaibhavAcharya/mdt

## 评论（1/1）

> **tuananh** · 2026-11-07T10:21:08.000Z　
> the interesting part is> wake themselves when a packet arrives; with the frame already queued in the guest's own virtio-net path.the project is fully vibed but i think the idea is fun. read the idea behind & kindly ignore the code please :)

## 导航

- 项目页：[[10-项目/github.com_e3d93f2e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
