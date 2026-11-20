---
type: "project"
title: "Show HN: Psudo – 47MB 2-bit coding model, Polish-prefix IR, and Rust transpiler"
project_url: "https://github.com/steveSujo/psudo"
first_seen: "2026-11-20T09:45:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_someProgramer
  - story_50559718
  - show_hn
lang: "en"
---

# Show HN: Psudo – 47MB 2-bit coding model, Polish-prefix IR, and Rust transpiler

> [!info] 一句话导读
> Toy Python-indented language + 100M 1.58-bit TQ2_0 local LLM engine that synthesizes token-compressed pIR code and lowers it to safe Rust.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/steveSujo/psudo>
> 首次收录：2026-11-20T09:45:52+08:00
> 来源渠道：HN Show HN
> 标签：author_someProgramer, story_50559718, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-20T09:45:52+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-20/86f0596627f716f6_Show-HN-Psudo-–-47MB-2-bit-coding-model,-Polish-pr]] |

## 摘要正文

# steveSujo/psudo  Toy Python-indented language + 100M 1.58-bit TQ2_0 local LLM engine that synthesizes token-compressed pIR code and lowers it to safe Rust.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-16T10:57:15Z  ## Languages  - Batchfile - Lean - Parrot - Python - Rust - Shell  ## Top Contributors  - steveSujo (19 contributions)  ---  ## README  # psudo  A token-compressed DSL (`.psudo`), a Polish-prefix intermediate representation (`pIR`), a borrow-checked safe Rust transpiler, and a pure-Rust 2-bit ternary (`TQ2_0`) inference engine—built to run local code synthesis inside a **4 GB VRAM** budget.  ```mermaid flowchart LR     A[".psudo DSL"] --> B["pIR (Polish-prefix IR)"]     B --> C["pseudo-engine (100M TQ2_0 + PDA Mask)"]     C --> D["Borrow Checker & Sandbox"]     D --> E["Safe Rust (0 unwrap)"] ```  | Metric | Value | | --- | --- | | Primary Model Footprint | `47.0 MB` (`100.7M` params, `TQ2_0` 2-bit ternary weights) | | Context Compression | `45–60%` fewer tokens than surface syntax via `pIR` | | Syntax Error Rate | `0%` at decode time via Pushdown Automaton (`PirPdaConstraint`) masking | | Runtim…
