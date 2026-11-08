---
type: "project"
title: "Show HN: FastVM – MicroVMs that sleep on idle and wake when packets arrive"
project_url: "https://github.com/tuananh/fastvm"
first_seen: "2026-11-08T12:50:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tuananh
  - story_50403001
  - show_hn
lang: "en"
---

# Show HN: FastVM – MicroVMs that sleep on idle and wake when packets arrive

> [!info] 一句话导读
> Fully vibed. Read the idea, ignore the code please :)

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tuananh/fastvm>
> 首次收录：2026-11-08T12:50:31+08:00
> 来源渠道：HN Show HN
> 标签：author_tuananh, story_50403001, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-08T12:50:31+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-08/6cf52c2edbabc79c_Show-HN-FastVM-–-MicroVMs-that-sleep-on-idle-and-w]] |

## 摘要正文

# tuananh/fastvm  Fully vibed. Read the idea, ignore the code please :)  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - Default branch: main - Created: 2026-11-07T09:13:00Z  ## Languages  - C - Go - Makefile - Shell  ---  ## README  # fastvm  A single-host micro-VM sandbox runtime: sandboxes boot in ~100 ms, sleep themselves when idle, page their memory to disk, and wake themselves when a packet arrives — with the frame already queued in the guest's own virtio-net path.  `fastvm` is implemented in Go on top of Firecracker/KVM. The design lives in GOAL.md; the full step-by-step walkthrough is GETTING_STARTED.md.  > Status: **v0.1 core implemented and tested end-to-end on KVM**. Working: > Dockerfile→ext4 base disks, copy/reflink CoW volumes, real Firecracker boot > with guest agent over vsock, pause/dormant (memory file)/wake, idle predicate > and auto-sleep, HTTP API + CLI, and a Linux-bridge L2 data plane with > wake-on-network. The eBPF L2 switch backend is implemented and tested > standalone but is not wired into the daemon yet (see Known limitations). > Real-VM e2e suites pass in seconds; see the test matrix below.  ## What it does  - **Fast VMs** — one Firecracker micr…
