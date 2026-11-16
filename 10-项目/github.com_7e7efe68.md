---
type: "project"
title: "Show HN: Static recompiler that runs Windows x64 on Apple Silicon"
project_url: "https://github.com/Sahilg93/arm64-recompiler"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Sahilg948
  - story_50510052
  - show_hn
lang: "en"
---

# Show HN: Static recompiler that runs Windows x64 on Apple Silicon

> [!info] 一句话导读
> Sahilg93/arm64-recompiler

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Sahilg93/arm64-recompiler>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_Sahilg948, story_50510052, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-16/93e01b7334d6957e_Show-HN-Static-recompiler-that-runs-Windows-x64-on]] |

## 摘要正文

# Sahilg93/arm64-recompiler  Static recompiler that turns real Windows x86-64 PE binaries into native Apple Silicon (ARM64) Mach-O executables via LLVM IR.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 11 - License: MIT License - Default branch: main - Created: 2026-11-15T03:16:54Z  ## Languages  - Assembly - C - C++ - Python - Shell  ## Topics  - apple-silicon - arm64 - binary-translation - compilers - llvm - macos - recompiler - reverse-engineering - static-recompilation - windows - wine - x86-64  ## Top Contributors  - Sahilg93 (19 contributions)  ---  ## README  # arm64-recompiler  A static recompiler that turns real Windows x86-64 PE binaries into native Apple Silicon (ARM64) Mach-O executables. It lifts the original machine code to LLVM IR ahead of time and compiles that IR for macOS; there is no instruction-level emulation of the lifted code at run time.  ## What works today  - **PuTTY Plink 0.83, natively.** The original Windows release runs `-V` through full CRT startup, argument parsing, standard output and shutdown. Output matches the original binary under Wine + Rosetta byte-for-byte, at **6.20× the speed** (42.31 ms vs. 262.23 ms) and with a **68.9% smaller memor…
