---
type: "corpus"
item_id: "01e4b6c8c97c70d1"
title: "Show HN: Katamaran - Open-source Docker and Linux runtime for Apple Silicon"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50581862"
project_url: "https://katamaran.rs/"
author: "nklmilojevic"
published_at: "2026-11-20T20:50:33Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_nklmilojevic
  - story_50581862
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Katamaran - Open-source Docker and Linux runtime for Apple Silicon

> [!info] 一句话导读
> Skip to content katamaran

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50581862>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：nklmilojevic　|　发布：2026-11-20T20:50:33Z
> 项目链接：<https://katamaran.rs/>
> 采集：2026-11-21T14:45:01+08:00　|　id：`01e4b6c8c97c70d1`

## 正文

Skip to content katamaran
 Search Ctrl K Cancel
GitHub
 Select theme Dark Light Auto
katamaran
 Run Docker containers and Linux machines on Apple silicon Macs inside one Linux virtual machine with fast bind mounts, automatic port forwarding, and active memory reclaim.
Download for macOS Install katamaran Quickstart tutorial
katamaran pairs a custom Hypervisor.framework virtual machine monitor (based on libkrun) with a native Swift and AppKit macOS app and the kat command-line tool. Shared folders run through a macOS virtio-fs server with direct hypercalls and FSEvents cache invalidation. Networking runs in-process with gvproxy, and unused guest memory returns to macOS in 64 KiB blocks.
Install katamaran Check system requirements, install the macOS app, and run first-time setup.
 Quickstart tutorial Start the VM, run a container with a bind mount, and open a Linux machine shell.
 File sharing Use fast bind mounts, host inotify events, and Linux files in Finder.
 Networking Reach containers on localhost, reach macOS through host.docker.internal, and resolve DNS.
 Linux machines Create LXC machines and connect with kat shell or SSH.
 Command-line reference Look up every katamaran subcommand, argument, and flag.
 Configuration reference Tune CPU count, memory limit, Rosetta, NFS mounts, and sleep behavior.
 Architecture Read how libkrun, direct FUSE hypercalls, in-process gvproxy, and memory reclaim work.
katamaran requires an Apple silicon Mac (M1 or later) running macOS 15 or later. It does not include Kubernetes.
Edit page
 Next Install katamaran

## 评论（1/1）

> **nklmilojevic** · 2026-11-20T20:50:33.000Z　
> Hey HN,I built Katamaran, native Apple Sillicon Docker and Linux runtime. Most of the Docker tools use super slow Docker Engine and they become annoying to use - f.e. you would feel it on real bind-mount workload like node_modules or PHP's vendor and composer with trees of tens of thousands of small files.The only product that I know of that fixes this is Orbstack, but it is not opensource, and you can only use it for personal usage.That is where Katamaran comes - it is even faster than Orbstack, but open-source so you can use it both for personal and business usage.Why it is faster than others (and comparable or faster than Orbstack - you can check the benchmarks on https://github.com/nklmilojevic/katamaran where it is faster):- Bind mounts - it based on a patched libkrun over Hypervisor.framework. SMall and boudned FUSE ops run inline on the vCPU via an ARM SMCCC hypercall instead of bouncing through a virtqueue and workter thread. Ofc, it also uses APFS, single FSEvents stream over vsock and in-container inotify
> - It also uses patched gvproxy in process inside the VMMM, and resolves DNS via macOS dns_sd
> - Reclaiming of memory is super fast becuase it maps guest RAM in 64 kiB XNU VM so virtio-balloon frees return to macOS immediatelly.In side-by-side benchmarks against OrbStack 2.2.5 on an M3 Max (harness and raw numbers are in bench/), the largest differences are VM stop (0.12s vs 1.95s), uncached DNS across 8 hosts (0.56ms vs 8.57ms; cached 0.09ms vs 0.92ms), host-write to container inotify latency (13.6ms vs 75ms), Laravel db:seed (7.59s vs 27.5s), warm git status on the Linux tree over a bind mount (0.17s vs 0.41s), find over node_modules (0.11s vs 0.22s), and memory footprint 10s after a 4 GiB container exits (2,769 MiB vs 5,632 MiB).I intentionally built a real use case benchmark rather than some synthetic micro-benchmarks that wouldn't show actual performance.I'm open for feedback, please let me know how it goes for you :)

## 导航

- 项目页：[[10-项目/katamaran.rs_a2cff576]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
