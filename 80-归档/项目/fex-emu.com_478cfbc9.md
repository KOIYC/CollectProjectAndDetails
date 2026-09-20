---
type: "project"
title: "The scourge of x86 emulation"
project_url: "https://fex-emu.com/Scourge-of-emulation"
first_seen: "2026-09-20T03:40:49+08:00"
sources:
  - lobsters
tags:
  - 项目
  - lobsters
  - hardware
lang: "en"
stale: true
---

# The scourge of x86 emulation

- **项目链接**：https://fex-emu.com/Scourge-of-emulation
- **首次收录**：2026-09-20T03:40:49+08:00
- **来源渠道**：Lobsters
- **标签**：hardware
- **最新指标**：得分=52 · 评论=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:36:26+08:00 | Lobsters | 得分=50 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/5b4bb4947b635b75_The-scourge-of-x86-emulation]] |
| 2026-09-20T02:48:08+08:00 | Lobsters | 得分=50 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/5b4bb4947b635b75_The-scourge-of-x86-emulation]] |
| 2026-09-20T02:57:31+08:00 | Lobsters | 得分=50 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/5b4bb4947b635b75_The-scourge-of-x86-emulation]] |
| 2026-09-20T03:06:43+08:00 | Lobsters | 得分=50 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/5b4bb4947b635b75_The-scourge-of-x86-emulation]] |
| 2026-09-20T03:31:09+08:00 | Lobsters | 得分=51 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/5b4bb4947b635b75_The-scourge-of-x86-emulation]] |
| 2026-09-20T03:40:49+08:00 | Lobsters | 得分=52 · 评论=0 | [[80-归档/posts/lobsters/2026-09-20/5b4bb4947b635b75_The-scourge-of-x86-emulation]] |

## 摘要正文

Author: FEX-Emu  The scourge of x86 emulation – FEX-Emu – A fast linux usermode x86 and x86-64 emulator  # The scourge of x86 emulation  Welcome to the first feature article on our site. We’re going to cover an ongoing problem with x86 emulation that affects every application that we emulate. This comes down to a single over-arching term that has wide-reaching ramifications; Emulating the x86 Total Store Ordering memory model (x86-TSO).  The problems with emulating this memory model on the weak ordering memory model that ARM defines is multi-faceted and covers multiple issues. We’re going to go over all the problems that we can encounter and the ways we solve (or in some cases can’t solve) in this article. Get yourself a snack and a warm drink to enjoy, this is going to be a long one.  - What exactly is x86-TSO? - The humble beginnings of ARMv8.0-a - I thought accessing memory was the easy bit? - Oh no, what are these atomic instructions? - What do you mean split-lock is mandatory? - Wait, uncached memory needs to work? - Looking towards a brighter future  What exactly is x86-TSO?  Before diving in to how we work around the x86 memory model problem, we need to first discuss exactly…
