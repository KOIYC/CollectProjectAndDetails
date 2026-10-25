---
type: "project"
title: "Show HN: Redmi phone can do things that $16K GPU is needed for on Ethereum"
project_url: "https://github.com/ignotusnemo/paramo1d"
first_seen: "2026-10-26T00:37:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ignotusnemo
  - story_50226569
  - show_hn
lang: "en"
---

# Show HN: Redmi phone can do things that $16K GPU is needed for on Ethereum

> [!info] 一句话导读
> ignotusnemo/paramo1d

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ignotusnemo/paramo1d>
> 首次收录：2026-10-26T00:37:35+08:00
> 来源渠道：HN Show HN
> 标签：author_ignotusnemo, story_50226569, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:24:35+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-25/7919d1e7a7c15bbe_Show-HN-Redmi-phone-can-do-things-that-$16K-GPU-is]] |
| 2026-10-25T23:45:19+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-25/7919d1e7a7c15bbe_Show-HN-Redmi-phone-can-do-things-that-$16K-GPU-is]] |
| 2026-10-26T00:19:08+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-25/7919d1e7a7c15bbe_Show-HN-Redmi-phone-can-do-things-that-$16K-GPU-is]] |
| 2026-10-26T00:37:35+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-25/7919d1e7a7c15bbe_Show-HN-Redmi-phone-can-do-things-that-$16K-GPU-is]] |

## 摘要正文

# ignotusnemo/paramo1d  Paramo1d is mobile Parano1d  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://parano1d.org - Default branch: main - Created: 2026-10-24T22:56:40Z  ## Languages  - C - Python - Rust  ## Top Contributors  - ignotusnemo (1 contributions)  ---  ## README  # Paramo1d  A native Rust client for verifying Parano1d on mobile devices. It connects directly to mainnet peers, checks the header chain from genesis and verifies the current recursive State proof and fork certificates.  Verification uses all available CPU cores automatically. Compressed matrices stay on disk and are processed in bounded buffers. The terminal shows download progress, verified heights, synchronization time and peak memory use.  ## Benchmarks  **Full mainnet synchronization from scratch: 48.43 seconds on an entry-level Redmi 15C smartphone.**  Measured on a **Redmi 15C with 4 GB RAM**, Android 15, ARM64 and **8 CPU cores**, using its own **4G connection through a VPN**. The client ran natively in Termux with a release build and mainnet Small proofs.  The measurement started with an empty chain-data directory. Verification parameters and prepa…
