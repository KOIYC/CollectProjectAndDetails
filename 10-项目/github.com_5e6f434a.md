---
type: "project"
title: "Show HN: Mantissa – a distributed scheduler and container orchestrator"
project_url: "https://github.com/MantissaLabs/mantissa"
first_seen: "2026-11-02T09:37:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_abronan
  - story_50326366
  - show_hn
lang: "en"
---

# Show HN: Mantissa – a distributed scheduler and container orchestrator

> [!info] 一句话导读
> MantissaLabs/mantissa

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/MantissaLabs/mantissa>
> 首次收录：2026-11-02T09:37:22+08:00
> 来源渠道：HN Show HN
> 标签：author_abronan, story_50326366, show_hn
> 最新指标：点赞=2 · 评论=3 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-02T09:37:22+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-02/244f76bc3c4e2511_Show-HN-Mantissa-–-a-distributed-scheduler-and-con]] |

## 摘要正文

# MantissaLabs/mantissa  Distributed Workload Scheduling and Cluster Management  - Stars: 16 - Forks: 0 - Watchers: 16 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://mantissa.io - Default branch: master - Created: 2021-01-05T22:13:22Z  ## Languages  - Cap'n Proto - Rust - Shell  ## Topics  - containers - crdt - ebpf - scheduler  ## Top Contributors  - abronan (1203 contributions)  ---  ## README  ---  Mantissa is a distributed orchestration system that grows with you and your workloads. Every node participates equally in scheduling, state replication, and cluster membership. No control-plane masters, and no federation layer required at scale. The focus of Mantissa is convergence and auto-stabilization.  Built in Rust with Cap'n Proto RPC, CRDT replication, Merkle Search Trees over Redb, and an eBPF driven data path, Mantissa targets low-latency scheduling and fault-tolerant operation across small and large fleets of nodes alike.  ## Why Mantissa?  Traditional workload orchestration systems often rely on a centralized control plane, which could become a bottleneck and hard to maintain as the cluster grows. Mantissa explores an alternative approach that leverages …
