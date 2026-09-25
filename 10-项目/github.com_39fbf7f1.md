---
type: "project"
title: "Show HN: La Machine – a useless box running Erlang on an ESP32 via AtomVM"
project_url: "https://github.com/pguyot/la_machine"
first_seen: "2026-09-24T23:57:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_oliviermevel
  - story_49827778
  - show_hn
lang: "en"
---

# Show HN: La Machine – a useless box running Erlang on an ESP32 via AtomVM

> [!info] 一句话导读
> Default branch: main

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/pguyot/la_machine>
> 首次收录：2026-09-24T23:57:22+08:00
> 来源渠道：HN Show HN
> 标签：author_oliviermevel, story_49827778, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-24/80c704653e2eb20d_Show-HN-La-Machine-–-a-useless-box-running-Erlang]] |

## 摘要正文

# pguyot/la_machine  La Machine  - Stars: 19 - Forks: 3 - Watchers: 19 - Open issues: 1 - Default branch: main - Created: 2024-06-18T12:32:48Z  ## Languages  - Erlang - Processing - Python - Shell  ## Top Contributors  - pguyot (75 contributions) - antoineschmitt (34 contributions)  ---  ## README  Source code for La Machine ==========================  Build  https://la-machine.fr/  https://github.com/pguyot/la_machine/assets/168407/cbffb7e5-78fa-400f-a39c-c9f04a7b1360  La Machine software is written in Erlang and runs on AtomVM virtual machine.  Partition map -------------  La Machine runs on an ESP32-C3 with 16 MB of external flash. The partition layout is:  | Partition | Offset | Size | |------------|--------------|--------------| | nvs | `0x009000` | `0x006000` | | phy_init | `0x00F000` | `0x001000` | | factory | `0x010000` | `0x120000` | | boot.avm | `0x130000` | `0x100000` | | sounds | `0x230000` | `0xDD0000` |  - **factory**: AtomVM virtual machine with necessary codecs. - **boot.avm**: La Machine Erlang code packed with AtomVM libraries. - **sounds**: sounds archive (`sounds.bin`) with a SHA1 integrity checksum  appended. The code verifies at runtime that the sounds partiti…
