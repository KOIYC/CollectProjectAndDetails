---
type: "corpus"
item_id: "9e3c0d9649fc414a"
title: "Show HN: NOS x86-64 hypervisor, written in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50524459"
project_url: "https://nos-os.tech/en/demo"
author: "irqlevel"
published_at: "2026-11-16T22:37:18Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_irqlevel
  - story_50524459
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: NOS x86-64 hypervisor, written in Rust

> [!info] 一句话导读
> Skip to content nos _ What is nos Hypervisor Docs How-to Blog EN RU

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50524459>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：irqlevel　|　发布：2026-11-16T22:37:18Z
> 项目链接：<https://nos-os.tech/en/demo>
> 采集：2026-11-17T11:09:12+08:00　|　id：`9e3c0d9649fc414a`

## 正文

Skip to content nos _ What is nos Hypervisor Docs How-to Blog EN RU
Demo
 nos at work: a demo
 A short video of a three-host nos cluster driven from its panel: the nos kernel itself, then several Linux VMs on different hosts, their disks on fault-tolerant storage and the VMs on one private network, from Debian's public cloud image to iperf3 between hosts.
nos at work: a demo
 The goal of the video is to run several Linux virtual machines on different nodes of a cluster, all booted into nos, with their disks on fault-tolerant storage and the machines on one private network. It is one session at the management panel of a small nos cluster with three hosts. One is a bare-metal Intel server at Hetzner, an EX44, with nos running directly on the hardware. The other two are nos instances in KVM virtual machines on a second server, an AMD AX41. The only edits are cuts: the wait for a download and the wait for a VM to boot are taken out, and everything else plays as it happened.
What it shows #
The hosts. All three are booted into nos, and one of them is a real Hetzner EX44. The panel talks to each host's API over mutual TLS and sees all three.
The nos kernel itself. The EX44's System page lists the kernel's own tasks and modules: the hypervisor, storage, the network. Its overview gives the version, the CPU and the boot parameters. Guest memory comes in 2 MB pages from a pool of huge pages the kernel sets aside at boot ( hugepages=32G ).
An image from a public link. The host downloads Debian 13's cloud image, converts it from qcow2 and writes it into NBS, the cluster's block storage. There it is frozen read-only, and VMs are made from its clones.
A network across the hosts. vnet gives VMs on different hosts one subnet, a gateway and a way out to the internet, and a VM on it can get a public address too. The state of the cluster's networks is kept on every host and agreed through Raft.
Two VMs on two hosts. Each has two CPUs and a disk that is a clone of the image. Both are on the new network, behind a cluster firewall that lets in only traffic from that network. cloud-init gives the image's user the password typed into the form.
Storage that is green. Every chunk of every volume is kept on three hosts, and NBS's metadata is agreed through Raft, so the storage keeps working when a host goes down.
The consoles and iperf3. The VMs' serial consoles stream into the panel. We log in on both, install iperf3 from Debian's mirrors (the VMs reach the internet through NAT), and measure TCP from one VM to the other. The traffic crosses an encrypted tunnel between the hosts, ChaCha20-Poly1305 running on CRYPTOGAMS' assembly.
Read more #
NBS: replicated block storage covers how volumes, replicas and the metadata service work.
vnet: VM networks across hosts covers the cluster's networks, the firewalls and the tunnel.
The hypervisor covers what runs the VMs.
The narration #
nos is a minimal operating system for servers, with only the components a server needs. Its kernel is a small amount of C++ that you can read and review. Everything else, the device drivers, the hypervisor, the filesystems, networking and storage, is written in safe Rust. Safe Rust helps rule out out-of-bounds memory access and data races, bugs that keep turning up in the C code of Linux.
In this demo we run several Linux virtual machines on different nodes of the cluster, all booted into nos, with their disks on fault-tolerant storage and the machines on a shared private network.
This is the management panel. All three hosts of the cluster are booted into nos. One of them is a real server, a Hetzner EX44; the other two run in virtual machines on a second server. And this is the nos kernel itself on that server: its tasks and modules, the hypervisor, storage and the network. Here are the kernel's version, the CPU and the boot parameters too. Guest memory comes in 2 MB pages, from a pool of huge pages the kernel sets aside at boot.
First, an image for virtual machines, made from a public link: the Debian 13 cloud image. The host has downloaded it and written it into NBS, the cluster's block storage. The image is ready.
Next, a virtual network that machines on different hosts share: a subnet, a gateway and a way out to the internet. A machine on this network can get a public address too. The networks' state is kept on every host and agreed through Raft, so the network survives a host failure.
The first machine runs on this host: two CPUs, a disk from the image, the new network, a password to log in, and a firewall that lets in only traffic from this network. It is made. We start it right from the list. The second machine goes on another host of the cluster, with the same image, network and firewall. Both machines show up in the panel, already running.
Storage is green. Every chunk lives on three hosts, and the metadata is agreed through Raft, so losing a host does not hurt the storage.
The second machine's console: Debian has booted. We log in, install iperf3 and start its server. Now the first machine's console: we log in and install iperf3 here too. And we measure TCP throughput to the second machine on the other host. The traffic crosses an encrypted tunnel between the hosts.
nos is open source, and enthusiasts are welcome: try it, or help with development. The code is on GitHub, and there is more on the website.
On this page
 What it shows
 Read more
 The narration
nos _ An operating system kernel for x86-64 and arm64, written in C++ and Rust, with its own hypervisor.
Project
 What is nos
 Hypervisor
 Demo
Learn
 Docs
 How-to
 Blog
Source
 GitHub
 Releases
 RSS
© 2017 – 2026 irqlevel . Code under the MIT license.
 English Русский

## 导航

- 项目页：[[10-项目/nos-os.tech_a00e2784]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
