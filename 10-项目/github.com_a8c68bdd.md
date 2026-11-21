---
type: "project"
title: "Show HN: Lightweight FUSE-based encrypted, compressed filesystem for Linux"
project_url: "https://github.com/tgaloppo/obfusecate"
first_seen: "2026-11-21T14:45:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_tgaloppo
  - story_50585222
  - show_hn
lang: "en"
---

# Show HN: Lightweight FUSE-based encrypted, compressed filesystem for Linux

> [!info] 一句话导读
> A personal project for digging deeper into Linux system programming, ObFUSEcate implements a file backed virtual block device that automatically performs compre…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tgaloppo/obfusecate>
> 首次收录：2026-11-21T14:45:01+08:00
> 来源渠道：HN Show HN
> 标签：author_tgaloppo, story_50585222, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:45:01+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-21/14971fbb01368525_Show-HN-Lightweight-FUSE-based-encrypted,-compress]] |

## 摘要正文

A personal project for digging deeper into Linux system programming, ObFUSEcate implements a file backed virtual block device that automatically performs compression and encryption as blocks are accessed. This virtual device can be mounted via FUSE (requiring no root privileges) to provide, effectively, a "live" compressed, encrypted archive.Written in C++, and intended to have minimal dependencies, it has custom 32 bit arithmetic encoding/decoding, ChaCha20-Poly1305 authenticated encryption, and CRC8 + XOR parity error-correction.
