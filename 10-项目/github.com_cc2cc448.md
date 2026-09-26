---
type: "project"
title: "Show HN: Aslmp, an async Python SLMP client for Mitsubishi MELSEC PLCs"
project_url: "https://github.com/AcaysiaChem/aslmp"
first_seen: "2026-09-26T10:00:28+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_AiasT
  - story_49848732
  - show_hn
lang: "en"
---

# Show HN: Aslmp, an async Python SLMP client for Mitsubishi MELSEC PLCs

> [!info] 一句话导读
> An async SLMP client for Mitsubishi MELSEC PLCs

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/AcaysiaChem/aslmp>
> 首次收录：2026-09-26T10:00:28+08:00
> 来源渠道：HN Show HN
> 标签：author_AiasT, story_49848732, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-26/80daa8ace080de62_Show-HN-Aslmp,-an-async-Python-SLMP-client-for-Mit]] |
| 2026-09-26T10:00:28+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-26/80daa8ace080de62_Show-HN-Aslmp,-an-async-Python-SLMP-client-for-Mit]] |

## 摘要正文

# AcaysiaChem/aslmp  An async SLMP client for Mitsubishi MELSEC PLCs  - Stars: 8 - Forks: 0 - Watchers: 8 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-09-07T06:36:50Z  ## Languages  - Python  ## Top Contributors  - aiast1 (39 contributions)  ---  ## README  # aslmp  > ## Safety notice > > **This library writes to industrial control equipment.** A value that reaches the wrong > device, or a wrong value that reaches the right one, moves whatever that device drives. With > `allow_remote_control=True` it can also halt a running CPU. > > **It is not a safety system.** It carries no functional-safety rating — no SIL, no PL — no > certification of any kind, and it has never been assessed by a functional-safety body. > **Interlocks, emergency stop, and anything a person's safety depends on belong in the PLC > program and in hardware**, not in a Python client on the far side of a network that can be > slow, lossy, or simply absent. > > **The failure modes on this wire are quiet, and we measured these ones ourselves.** Two TCP > requests in flight at once return **one** response — for the wrong request — with end code > `0x0000`. A UDP burst deeper th…
