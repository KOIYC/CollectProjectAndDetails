---
type: "project"
title: "Show HN: Pollen – distributed WASM runtime, no control plane, single binary"
project_url: "https://github.com/sambigeara/pollen"
first_seen: "2026-09-21T02:52:26+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_sambigeara
  - story_47961935
  - show_hn
lang: "en"
---

# Show HN: Pollen – distributed WASM runtime, no control plane, single binary

> [!info] 一句话导读
> Distributed WASM runtime. Workloads place themselves over a zero-trust mesh. One static binary.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/sambigeara/pollen>
> 首次收录：2026-09-21T02:52:26+08:00
> 来源渠道：HN Show HN
> 标签：author_sambigeara, story_47961935, show_hn
> 最新指标：点赞=137 · 评论=65 · engagement_velocity=137

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=137 · 评论=65 · engagement_velocity=137 | [[20-语料/posts/hn_show/2026-09-21/76552ae059eb817d_Show-HN-Pollen-–-distributed-WASM-runtime,-no-cont]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=137 · 评论=65 · engagement_velocity=137 | [[20-语料/posts/hn_show/2026-09-21/76552ae059eb817d_Show-HN-Pollen-–-distributed-WASM-runtime,-no-cont]] |
| 2026-09-21T01:41:05+08:00 | HN Show HN | 点赞=137 · 评论=65 · engagement_velocity=137 | [[20-语料/posts/hn_show/2026-09-21/76552ae059eb817d_Show-HN-Pollen-–-distributed-WASM-runtime,-no-cont]] |
| 2026-09-21T02:52:26+08:00 | HN Show HN | 点赞=137 · 评论=65 · engagement_velocity=137 | [[20-语料/posts/hn_show/2026-09-21/76552ae059eb817d_Show-HN-Pollen-–-distributed-WASM-runtime,-no-cont]] |

## 摘要正文

# Sambigeara/pollen  Distributed WASM runtime. Workloads place themselves over a zero-trust mesh. One static binary.  - Stars: 377 - Forks: 15 - Watchers: 377 - Open issues: 10 - License: Apache License 2.0 - Homepage: https://pln.sh - Default branch: main - Created: 2026-04-02T08:08:11Z  ## Languages  - CSS - Go - HCL - HTML - Just - Shell  ## Top Contributors  - Sambigeara (130 contributions)  ---  ## README  # Pollen  Pollen is a self-organising mesh and WASM runtime written in pure Go. Workloads are "seeded" into the cluster and organically scale and follow load. There is no central coordinator; decisions are made deterministically, locally, using a gossiped CRDT runtime state as their source of truth. Same view of the world; same workload placement and routing.  The goal is for Pollen to turn a collection of heterogeneous machines into a blob of generic compute that can run absolutely anywhere. Think: a Raspberry Pi acting as though it has the power of a server-farm.  Pollen demo  This demo shows a simple processing pipeline: two chained workloads and a single "sink" egress server running on my home laptop (all requests end up here). 10 freshly provisioned (global) nodes are b…
