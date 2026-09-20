---
type: "project"
title: "Show HN: Bulwark – a kernel read gate so coding agents can't read .env or .ssh"
project_url: "https://github.com/obstalabs/bulwark"
first_seen: "2026-09-21T02:53:02+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ppiankov
  - story_48733776
  - show_hn
lang: "en"
---

# Show HN: Bulwark – a kernel read gate so coding agents can't read .env or .ssh

> [!info] 一句话导读
> Kernel-level read gate for AI agents — protected file opens are denied or routed through off-band consent before bytes reach the agent. Linux (fanotify) + macOS…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/obstalabs/bulwark>
> 首次收录：2026-09-21T02:53:02+08:00
> 来源渠道：HN Show HN
> 标签：author_ppiankov, story_48733776, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/b30d67845415fff4_Show-HN-Bulwark-–-a-kernel-read-gate-so-coding-age]] |
| 2026-09-21T02:53:02+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/b30d67845415fff4_Show-HN-Bulwark-–-a-kernel-read-gate-so-coding-age]] |

## 摘要正文

# obstalabs/bulwark  Kernel-level read gate for AI agents — protected file opens are denied or routed through off-band consent before bytes reach the agent. Linux (fanotify) + macOS (Endpoint Security).  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: GNU Affero General Public License v3.0 - Homepage: https://obstalabs.dev/bulwark - Default branch: main - Created: 2026-06-17T10:20:13Z  ## Languages  - Makefile - Rust - Shell - Swift  ## Topics  - access-control - ai-agents - devsecops - endpoint-security - fanotify - kernel - linux - llm-security - macos - rust - security  ## Top Contributors  - obstalabs (65 contributions)  ---  ## README  # Bulwark  > Gate an agent's file reads at the OS, by inode, before the bytes reach it.  Bulwark is an OS-level read gate for running AI coding agents on a developer machine. Launch an agent under it; when any process in its tree tries to `open()` a protected file, Bulwark applies a policy before the bytes reach the agent: deny, allow, or ask for consent. On Linux it uses fanotify permission events; on macOS, Endpoint Security. Hardened mode adds a Landlock floor so protected paths stay denied even if the userspace gate dies.  CI…
