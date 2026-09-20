---
type: "corpus"
item_id: "e5579030ab7dbaff"
title: "Show HN: Fail2zig. A single-binary fail2ban replacement written in Zig"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49732015"
project_url: "https://fail2zig.com/"
author: "ul0gic"
published_at: "2026-09-16T19:52:26Z"
captured_at: "2026-09-20T09:36:58+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_ul0gic
  - story_49732015
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Fail2zig. A single-binary fail2ban replacement written in Zig

> [!info] 一句话导读
> fail2zig — a fail2ban replacement for Linux

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49732015>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：ul0gic　|　发布：2026-09-16T19:52:26Z
> 项目链接：<https://fail2zig.com/>
> 采集：2026-09-20T09:36:58+08:00　|　id：`e5579030ab7dbaff`

## 正文

fail2zig — a fail2ban replacement for Linux

# Single binary. Durable protection.

Predictable behavior under hostile input.

 Reads your logs, detects repeated failures, and bans offending IPs. A familiar job, with a smaller runtime and explicit resource limits.

 sshd / ban event Example

/var/log/auth.log 3 matches

1. 12:04:01

 Failed password for root from 203.0.113.7
2. 12:04:03

 Failed password for root from 203.0.113.7
3. 12:04:05

 Failed password for root from 203.0.113.7

↳

 Address banned 203.0.113.7 for 1 hour

3 / 3

 Confirmed protection · example`sshd · 203.0.113.71h ban · kernel readback confirmed`

Daemon + administration

1 binary

Native persistence

SQLite

Built-in service filters

15

Linux release targets

5

## Familiar operation. Fewer moving parts.

 The same log-to-ban model, with explicit boundaries around the work your server does.

### A smaller runtime to maintain

One static executable combines the daemon, administration and migration tools. No Python runtime or separate database server is required.

Static musl build ↗

### Durable state with explicit limits

Source progress, retry state and protection ownership survive restart in SQLite. Bounded admission retains critical state when resources run short.

Memory model ↗

### Parsing without a regex engine

Built-in filters compile into specialised parsers. A single pass extracts the address, with bounds checks and no allocations in the hot path.

Parser architecture ↗

### Enforcement through the kernel

Typed intent is persisted before dispatch, then confirmed by kernel readback. Choose nftables through direct netlink, or the iptables and ipset backends.

Netlink integration ↗

## Bring your existing jails.

 Import your fail2ban configuration, review the result, then switch when you’re ready.

1. ### Get the binary

Choose a prebuilt Linux release or build from source.

Download a release ↗
2. ### Import and review

 Inspect supported jails and project configuration into TOML. Resolve unsupported filters and actions before enabling protection.
3. ### Verify, then switch

 Compare decisions in log-only mode before changing enforcement. The guide covers cutover and rollback.

Follow the migration guide →

# After installing fail2zig

```
sudo fail2zig migrate inspect --source-dir /etc/fail2ban
```

 # Review scope and blockers before planning cutover

### What doesn’t transfer

 Arbitrary regexes and shell actions need reviewed replacements. Supported schema-4 migration can carry owners, deadlines and history; in-memory partial matches do not transfer.

Check compatibility →

Linux builds

 x86_64, ARM64, ARMv7, MIPS & MIPSel. Selected live checks cover Debian 13 x86_64; other targets have cross-build, static-inspection and QEMU smoke evidence.

## Evidence. With the limits in view.

 0.4.0 brings native durability and verified enforcement. The release evidence separates live host checks from cross-build and emulated command checks.

### Selected live qualification

Debian 13 x86_64

 File and journal input, all three firewall backends, service permissions and storage recovery. Other architectures have static-build and QEMU smoke evidence.

Read the qualification scope ↗

### Protection through restart

SQLite embedded

 Durable checkpoints, retries, owners and confirmed history. Resource exhaustion pauses admission instead of silently discarding critical protection state.

Understand the resource limits ↗

 Qualification boundary Live checks preceded the version-only update to 0.4.0; rebuilt artifacts passed native/emulated checks. Ubuntu and non-x86 hardware enforcement remain untested. No comparative speed claim accompanies this release.

## Different tools, different tradeoffs.

 Compare runtime, deployment, and firewall support. Your existing configuration is part of that decision.

Scroll horizontally to compare all columns.

 Intrusion prevention tools: language, deployment, and firewall backends

| Tool | Language | Deployment | Firewall backends |
| --- | --- | --- | --- |
| fail2zig | Zig | Static musl binary | nftables / iptables / ipset |
| fail2ban | Python | Package + runtime | iptables / nftables |
| SSHGuard | C | Daemon + firewall backend | pf / iptables / nftables |
| CrowdSec | Go | Engine + remediation component | iptables / nftables |

 Selected deployment characteristics. See fail2ban, SSHGuard and CrowdSec for full support details.

## Before you switch.

Is this a drop-in replacement?

 No. Inspect supported configuration and action scope before switching. The schema-4 migration workflow can transfer admitted owners, deadlines and history, but not partial matches or journal cursors. Arbitrary fail2ban regexes and actions are not executed.

Read the compatibility details →

Can hostile log lines crash or exhaust the daemon?

 That’s the threat model we designed to. Parsing is bounds-checked, log lines have a bounded input contract, and native processing has explicit resource limits. Storage failures pause affected ingestion while retaining protection. These controls reduce risk; the threat model documents remaining limits, including the known loopback case.

Read the threat model →

Why Zig? Why not Rust?

 Zig gives us explicit allocator control, comptime code generation for built-in filters, and straightforward cross-compilation to musl targets. Rust would work. Zig fits the problem.

Does it run in minimal containers?

 Static linkage avoids shared runtime libraries, but deployment still needs readable logs, writable persistent state and the selected backend’s capabilities. Journal input needs journalctl; iptables/ipset need host tools. Effects stay in the current network namespace; custom namespace selectors are unsupported in 0.4.0.

Is this a SIEM or a WAF?

 Neither. It reads logs and acts on repeated failures. It does not aggregate security events across hosts, correlate incidents, or inspect HTTP bodies.

# Page Rage

## 导航

- 项目页：[[10-项目/fail2zig.com_e397cfb5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
