---
type: "project"
title: "Show HN: Fail2zig. A single-binary fail2ban replacement written in Zig"
project_url: "https://fail2zig.com/"
first_seen: "2026-09-20T09:36:58+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_ul0gic
  - story_49732015
  - show_hn
lang: "en"
---

# Show HN: Fail2zig. A single-binary fail2ban replacement written in Zig

> [!info] 一句话导读
> fail2zig — a fail2ban replacement for Linux

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://fail2zig.com/>
> 首次收录：2026-09-20T09:36:58+08:00
> 来源渠道：HN Show HN
> 标签：author_ul0gic, story_49732015, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-20/e5579030ab7dbaff_Show-HN-Fail2zig.-A-single-binary-fail2ban-replace]] |
| 2026-09-20T09:36:58+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-09-20/e5579030ab7dbaff_Show-HN-Fail2zig.-A-single-binary-fail2ban-replace]] |

## 摘要正文

fail2zig — a fail2ban replacement for Linux  # Single binary. Durable protection.  Predictable behavior under hostile input.   Reads your logs, detects repeated failures, and bans offending IPs. A familiar job, with a smaller runtime and explicit resource limits.   sshd / ban event Example  /var/log/auth.log 3 matches  1. 12:04:01   Failed password for root from 203.0.113.7 2. 12:04:03   Failed password for root from 203.0.113.7 3. 12:04:05   Failed password for root from 203.0.113.7  ↳   Address banned 203.0.113.7 for 1 hour  3 / 3   Confirmed protection · example`sshd · 203.0.113.71h ban · kernel readback confirmed`  Daemon + administration  1 binary  Native persistence  SQLite  Built-in service filters  15  Linux release targets  5  ## Familiar operation. Fewer moving parts.   The same log-to-ban model, with explicit boundaries around the work your server does.  ### A smaller runtime to maintain  One static executable combines the daemon, administration and migration tools. No Python runtime or separate database server is required.  Static musl build ↗  ### Durable state with explicit limits  Source progress, retry state and protection ownership survive restart in SQLite. Bounde…
