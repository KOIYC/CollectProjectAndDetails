---
type: "project"
title: "Show HN: Kavach – Replay production crashes locally without a DB or network"
project_url: "https://github.com/kavachlabs/kavach"
first_seen: "2026-10-29T20:41:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_eulerkochy
  - story_50279502
  - show_hn
lang: "en"
---

# Show HN: Kavach – Replay production crashes locally without a DB or network

> [!info] 一句话导读
> Replay the crash. Prove the fix. 81ns in-process flight recorder, 61µs deterministic replay, and 5.9ms variant fix verification for journal-driven services and …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/kavachlabs/kavach>
> 首次收录：2026-10-29T20:41:52+08:00
> 来源渠道：HN Show HN
> 标签：author_eulerkochy, story_50279502, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:41:52+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-29/e9f6a67b7b5e1ad8_Show-HN-Kavach-–-Replay-production-crashes-locally]] |

## 摘要正文

# kavachlabs/kavach  Replay the crash. Prove the fix. 81ns in-process flight recorder, 61µs deterministic replay, and 5.9ms variant fix verification for journal-driven services and AI coding agents.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 1 - License: Apache License 2.0 - Homepage: https://www.thekavachlabs.com - Default branch: main - Created: 2026-10-06T13:58:52Z  ## Languages  - C - C++ - CMake - CSS - Dockerfile - Dune - Elixir - Go - HTML - Haskell - Java - JavaScript - Julia - OCaml - PHP - Python - Ruby - Rust - Shell - TypeScript  ## Topics  - claude-code - coding-agents - debugging - deterministic-simulation-testing - event-sourcing - fault-injection - golang - mcp - mcp-server - property-based-testing - python - replay - rust - testing - typescript  ## Top Contributors  - eulerkochy (272 contributions)  ---  ## README  ci sdk release codecov  **Replay the crash. Prove the fix.**  Kavach records every input, clock read, and random read a service makes. When a step panics, returns an error, or breaks a declared invariant, it flushes a compact `.kavach` fixture that replays byte for byte in microseconds—with no broker, database, or network—and rejects narrow patc…
