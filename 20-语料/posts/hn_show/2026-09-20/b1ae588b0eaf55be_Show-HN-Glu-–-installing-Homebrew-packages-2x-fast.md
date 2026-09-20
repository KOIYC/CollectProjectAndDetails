---
type: "corpus"
item_id: "b1ae588b0eaf55be"
title: "Show HN: Glu – installing Homebrew packages 2x faster on macOS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49722369"
project_url: "https://glu.run/"
author: "henrikklee"
published_at: "2026-09-16T05:15:40Z"
captured_at: "2026-09-20T14:04:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_henrikklee
  - story_49722369
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Glu – installing Homebrew packages 2x faster on macOS

> [!info] 一句话导读
> glu — the modern package manager for macOS

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49722369>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：henrikklee　|　发布：2026-09-16T05:15:40Z
> 项目链接：<https://glu.run/>
> 采集：2026-09-20T14:04:34+08:00　|　id：`b1ae588b0eaf55be`

## 正文

glu — the modern package manager for macOS

# The modern package manager for macOS

Install command-line tools and their dependencies faster, with a simpler interface for you and your agent.

Install glu v0.1.1

$`curl -fsSL https://glu.run/install | bash` Copy install command

Available for Apple Silicon Macs Quick Start →

- 2.3× faster than Homebrew
- 8,000+ packages available
- Concise output by default
- JSON Schema and plan mode for agents

## Installing `node`

Cold cache · including all dependencies

Median elapsed time Seconds · lower is better

1. glu

8.88 s — median of 76 validated successful installs
2. Homebrew

20.76 s — median of 76 validated successful installs
3. nanobrew

23.11 s — median of 76 validated successful installs

## Installing `jq`

Cold cache · including all dependencies

Median elapsed time Seconds · lower is better

1. glu

2.09 s — median of 76 validated successful installs
2. Homebrew

3.78 s — median of 76 validated successful installs
3. nanobrew

4.24 s — median of 76 validated successful installs

## Installing `vips`

Cold cache · including all dependencies

Median elapsed time Seconds · lower is better

1. glu

34.09 s — median of 76 validated successful installs
2. Homebrew

77.58 s — median of 76 validated successful installs
3. nanobrew

102.81 s — median of 66 validated successful installs

674 successful installs · 6 network environments

## A simpler way to manage your packages

Commands follow modern package-manager conventions, with concise output by default.

zsh · glu Replay

`glu install vips`

## 8,000+ packages available

Packages come from Homebrew’s prebuilt collection. Search for the tools you use.

Use the up and down arrows to choose a result, then Enter to open it. Escape closes the results.

Use the full registry to search without JavaScript.

### A CLI your agent can inspect

A complete, machine-readable specification of every command: arguments, flags, defaults, side effects, and response schemas.

Built into the command architecture, with consistent success and failure envelopes for JSON output.

Plan mode lets an agent inspect proposed changes before executing them.

$`glu help --json --schemas` Copy agent command

## How it works

$`glu trace view` Copy trace command

A recorded vips install in glu’s trace viewer. About install traces →

$`glu trace view` Copy trace command

- 01

### One-shot server-side resolution

Fetch the complete dependency graph and install metadata in one round trip. No brew update step or local index to refresh.

Deep Dive: One-Shot Resolve →
- 02

### Built-in observability

Every install records a local trace, showing where time goes without uploading data.

Reference: Traces →
- 03

### Critical-path scheduling

Prioritize downloads that unlock expensive work.

Deep Dive: Orchestrator →
- 04

### Parallel, multipart downloads

Fetch packages concurrently and split large downloads into chunks.

Deep Dive: Orchestrator →
- 05

### Overlapping stages

Download, extract, prepare, and install concurrently where dependencies allow.

Deep Dive: Orchestrator →
- 06

### Shared resource limits

Coordinate network, CPU, memory, and filesystem work.

Deep Dive: Orchestrator →
- 07

### Coalesced postinstall work

Rebuild shared caches once, after all contributing packages are ready.

Deep Dive: Postinstall →
- 08

### Written in Rust

Native performance, with explicit control over concurrency and memory.

## Package correctness

Homebrew`/opt/homebrew` glu`/opt/glustore`

### Compare normalized results

Files

Contents, types, permissions

Links

Targets and prefix layout

Mach-O

Load commands and signatures

Commands

Package-specific probe output

Differential testing compares real installations, accounting for expected differences such as prefixes and generated cache files.

### Upstream behavior, ported to Rust

Relocation, signing, linking, and postinstall behavior follow Homebrew’s implementation. Ported postinstall code records the original commit, file, and line.

Inspect the implementation →

### Verification through completion

Downloaded artifacts and reused cache entries are checksum-verified. Setup runs in sandboxed workers. Required transformations fail rather than being silently skipped.

Correctness and testing →

### Works alongside Homebrew

Packages live under `/opt/glustore`, separate from your existing installation.

Your existing packages stay in place.

## Your next install can be faster

Install glu, then try a package you use.

# ringlochid/leotabs

## 评论（2/2）

> **theycallmeritik** · 2026-09-16T05:26:23.000Z　
> How are you handling cache invalidation and mirror selection to hit that 2x boost? Curious if this works smoothly alongside standard Homebrew taps without breaking existing formulae.

---

> **henrikklee** · 2026-09-16T06:05:48.000Z　
> Bottles are cached in a content addressed store by the sha256 from the registry install manifest. All install requests are resolved live against the registry, so there is no local metadata cache to invalidate.There is no mirror selection, all bottles are downloaded directly from GHCR's CDN.The speedup comes mostly from one shot resolution, intelligent download scheduling and parallelization of install and postinstall work.Packages are installed to /opt/glustore so they don't affect Homebrew installed packages.

## 关联链接

- https://glu.run/install

## 导航

- 项目页：[[10-项目/glu.run_a9433b7d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
