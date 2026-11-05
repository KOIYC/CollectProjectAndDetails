---
type: "project"
title: "Show HN: Cassandra – free tool to check if you got affected by the Cursor hack"
project_url: "https://ciphero.ai/cassandra/hn"
first_seen: "2026-11-05T11:21:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_skd-fs
  - story_50369457
  - show_hn
lang: "en"
---

# Show HN: Cassandra – free tool to check if you got affected by the Cursor hack

> [!info] 一句话导读
> Check your machine for the Claude Code backdoor.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://ciphero.ai/cassandra/hn>
> 首次收录：2026-11-05T11:21:45+08:00
> 来源渠道：HN Show HN
> 标签：author_skd-fs, story_50369457, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:21:45+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-05/73d1cbae38ef1b0f_Show-HN-Cassandra-–-free-tool-to-check-if-you-got]] |

## 摘要正文

Cassandra by How it works  Advisories Check your machine for the Claude Code backdoor. One command. Read-only, no sudo, nothing sent. Yes, it is a script that looks for a script,  so the whole thing is on this page . Read it, then run it. macOS / Linux curl -fsSL https://ciphero.ai/cassandra.sh | bash Copy Windows, in PowerShell irm https://ciphero.ai/cassandra.ps1 | iex Copy Prefer not to pipe? curl -fsSL -o cassandra.sh https://ciphero.ai/cassandra.sh && less cassandra.sh && bash cassandra.sh What it does Looks for the indicators in Cursor's notice for the Claude Code 2.1.312 and 2.1.313 backdoor: the svc-telemetry SSH key and the two key fingerprints, the com.apple.sysmond LaunchAgent, the tunnel files in ~/.config , the cron line, the SysMon task and sysmon.cmd , the attacker IP. In the places the notice names, and in the places the same thing could sit under another name: shell start-up files, other LaunchAgents, units and tasks, the Run key, the process list, open connections, the code of your other extensions. 19 checks in all (13 apply on macOS, 11 on Linux, 12 on Windows). Cursor's own one-liner covers the first. Hashes extension.js inside any installed Claude Code 2.1.312…
