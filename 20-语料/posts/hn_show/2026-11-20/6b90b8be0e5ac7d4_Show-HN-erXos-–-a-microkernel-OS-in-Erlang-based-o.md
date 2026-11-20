---
type: "corpus"
item_id: "6b90b8be0e5ac7d4"
title: "Show HN: erXos – a microkernel OS in Erlang based on Genera/Plan 9/QNX ideas"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50568169"
project_url: "https://stass.github.io/erXos"
author: "stass"
published_at: "2026-11-19T23:39:34Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_stass
  - story_50568169
  - show_hn
metrics: {"points": 3, "comments": 3, "engagement_velocity": 3}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: erXos – a microkernel OS in Erlang based on Genera/Plan 9/QNX ideas

> [!info] 一句话导读
> What if every Erlang process were an operating-system process? With as much system code and drivers written in Erlang itself. This is something I was pondering …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50568169>
> 指标：点赞=3 · 评论=3 · engagement_velocity=3
> 作者：stass　|　发布：2026-11-19T23:39:34Z
> 项目链接：<https://stass.github.io/erXos>
> 采集：2026-11-20T09:45:52+08:00　|　id：`6b90b8be0e5ac7d4`

## 正文

What if every Erlang process were an operating-system process? With as much system code and drivers written in Erlang itself. This is something I was pondering for a while, and finally was able to prototype thanks to AI coding agents.erXos is a capability-based microkernel OS in Erlang: drivers, filesystems, and the network stack are all supervised Erlang processes, same as any app.The kernel itself is Fiasco, in C++, slightly modified for erXos needs. This is an OS I wanted for a long time: an Erlang machine where every BEAM process is a process visible to the OS and scheduler, not something bolted on top.You can try it right now with nothing to install: there is an emulator on the website that boots the whole OS in the browser ARM64 emulator. At the rc prompt, try `ps`, `top`, `ping` or `erl` and write any kind of erlang code. There's a Pi 4 SD image and a QEMU image too. The goal is to build an ultra-reliable microkernel OS with hot code loading and both system and BEAM-based isolation. The latter is one thing that would allow you to run millions of processes on the system, something that would be prohibitive on a microkernel alone due to the context switch overhead. Capabilities keep every component least-privileged, supervision keeps the machine running when drivers or subsystems crash, and hot code loading would let you fix a broken driver without reboot.The secondary goal is to keep as much of a UNIX face as possible. Too many novel OSes change things for no particular reason that makes them hard to use. erXos tries to preserve as many existing UNIX/FreeBSD concepts as much as possible to remove the learning curve.What works today:- Boots in the browser/v64, in QEMU, and on a Raspberry Pi 4 from an SD card- A real shell (plan9 rc) with job control, pipes, `ps`, `grep`. It feels like UNIX on the surface- Erlang versions of basic UNIX apps.- Drivers written in Erlang: UART, virtio, SD card, Ethernet (GENET), display- A pure Erlang EROFS filesystem for root images- A TCP/IP stack in Erlang based on FreeBSD network stack and verified for correctness against it- Domains: every app runs as its own address space or Erlang node, isolated from others- Plan 9 namespaces and 9P everywhere; windows are files like RIO and 9P is a file protocol between OS servers- Supervision end to end: if a driver fails, its supervisor resets the device and restarts itI also have 2 demo apps built on app sdk: a full-screen kiosk app with live crypto quotes and clock and, of course Doom, which ships on the Pi 4 card image (type `doom`).What's coming:- Raspberry Pi 5 support- Full display on the Pi- WIFI- Bluetooth- POSIX-lite for C programs, so existing code can run as a domain- Performance, debugging and tracing features.The code is all available under the BSD license.Would love to hear all and any feedback!

## 评论（3/3）

> **thomasdziedzic** · 2026-11-20T00:25:40.000Z　
> The main thing I'm now looking out for in an OS is how secure is it? Can any random process connect to badsite.com and exfiltrate data or take commands from badsite.com in case of malware? Can you control this on a per process / profile level? How does it prevent each type of malware?Maybe adding a page with examples of how you handle each type of malware / prevent it would be useful.

---

> **ryandeverton** · 2026-11-20T01:02:29.000Z　
> amazeballs

---

> **stass** · 2026-11-20T00:42:18.000Z　
> Yes, the OS is based on the capability microkernel so processes are only allowed to do things explicitly granted to them. Network access is an explicit capability and can be broken down further by protocol/port/traffic etc.I haven’t looked into more granular capabilities like granting access to specific sites yet, but this should be pretty easy to implement as the OS network server is itself in erlang, and all network request go through it.

## 导航

- 项目页：[[10-项目/stass.github.io_b8a69e52]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
