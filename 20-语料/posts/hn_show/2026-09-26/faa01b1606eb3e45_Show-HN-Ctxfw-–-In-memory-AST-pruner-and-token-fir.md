---
type: "corpus"
item_id: "faa01b1606eb3e45"
title: "Show HN: Ctxfw – In-memory AST pruner and token firewall for Cursor and Claude"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49845110"
project_url: "https://github.com/heuristicolab/ctxfw"
author: "mikemo88"
published_at: "2026-09-25T14:23:16Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_mikemo88
  - story_49845110
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Ctxfw – In-memory AST pruner and token firewall for Cursor and Claude

> [!info] 一句话导读
> High-assurance in-memory Tree-Sitter AST context firewall and pruning MCP server for coding agents (-72.4% token mass).

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49845110>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：mikemo88　|　发布：2026-09-25T14:23:16Z
> 项目链接：<https://github.com/heuristicolab/ctxfw>
> 采集：2026-09-26T09:41:08+08:00　|　id：`faa01b1606eb3e45`

## 正文

# heuristicolab/ctxfw

High-assurance in-memory Tree-Sitter AST context firewall and pruning MCP server for coding agents (-72.4% token mass).

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://glama.ai/mcp/servers/heuristicolab/ctxfw
- Default branch: main
- Created: 2026-09-11T00:40:23Z

## Languages

- Batchfile
- PowerShell
- Python
- Shell

## Topics

- ai-agents
- anthropic
- ast-pruning
- code-analysis
- context-window
- cursor
- developer-tools
- llm-finops
- mcp
- mcp-server
- model-context-protocol
- token-optimization
- tree-sitter

## Top Contributors

- metaversemexico-ui (49 contributions)
- heuristicolab (37 contributions)

---

## README

# CTXFW // CONTEXT FIREWALL
### High-Assurance Axiomatic Gatekeeper & In-Memory AST Pruning for Coding Agents

PyPI - Version
Axiomatic Completeness Index
Tests
License
Glama

**The deterministic boundary between probabilistic LLM hallucination and production infrastructure.**

Installation • Benchmarks • Diagnostic • Architecture • Enterprise Governance

---

## Executive Abstract

Autonomous coding agents (Claude, Gemini, Cursor, Antigravity) consume massive context windows with bloated peripheral dependencies, triggering token exhaustion, context drift, and security degradation.

**CTXFW** is an open-core context firewall and Model Context Protocol (MCP) gatekeeper. It combines an **in-memory polyglot AST pruner** with a **deterministic axiomatic intake sieve**:
1. **Compacts Peripheral Code (72.4% token reduction)**: Replaces distance-1 and distance-2+ module implementations with clean interface signatures, type definitions, and functional stubs.
2. **Enforces Axiomatic Integrity (ACI $\ge$ 0.9000)**: Rejects ungrounded or deficient architecture briefs missing negative invariants ($N \ge 5$), bounded variable domains, deterministic state machines, or formal error taxonomies.
3. **Zero Telemetry Egress**: Guaranteed local execution with zero network telemetry leakage on standard operating mode.

---

## AST Pruning Benchmarks

CTXFW operates directly at the syntax tree layer using native polyglot grammars:

| Benchmark Dimension | Raw Context Ingestion | CTXFW Topological Compactor | Performance Gain / Impact |
| :--- | :--- | :--- | :--- |
| **Token Consumption** | 100% (Raw Files) | 27.6% (Interface Stubs) | **72.4% Bloat Eliminated** |
| **Engine Compaction Overhead** | — | Native in-memory parser | **< 5.0 ms** |
| **Warm Cache Hit Overhead** | — | SQLite WAL semantic cache | **< 0.8 ms** |
| **Stdio Telemetry Egress** | Unsanitized stdout | Pure isolated JSON-RPC | **Zero Egress (100% Isolated)** |
| **Axiom Verification Latency** | — | Sieve evaluation | **< 12.0 ms** |
| **CI/CD Pre-Commit Latency** | — | Headless git sentry | **< 85.0 ms** |

### Empirical Case Study: `ctxfw/cli.py` Core Dependency Graph

Empirical context reduction metrics generated via `ctxfw.resolve_context_bundle` running against 16 internal dependencies:

| Dimension | Raw Context Ingestion | CTXFW Topological Sieve | Performance Delta |
| :--- | :--- | :--- | :--- |
| **Total Context Size** | 49,096 tokens | 20,014 tokens | **-59.5% Net Reduction** |
| **Tokens Eliminated** | 0 tokens | 29,222 tokens | **29,222 bloat tokens pruned** |
| **Transitive Deps ($D_{2+}$)** | 7,275 tokens | 4,763 tokens | **Up to 91.9% reduction** |
| **FinOps Cost Impact** | Base Cost | Reduced by $0.0877 USD / prompt | **~$87.70 USD saved per 1K calls** |
| **AST Compaction Latency** | — | 1,407.96 ms | In-memory Tree-Sitter parsing |
| **Attestation Integrity** | None | SHA-256 sealed | Strict interface preservation |

**Topological Hierarchy Breakdown:**
- **$D_0$ Target (`ctxfw/cli.py`)**: 100% Full Implementation preserved.
- **$D_1$ Direct Deps (e.g. `gatekeeper.py`, `mcp.py`)**: Implementation truncated to typed stubs (`...`). Token savings: **73% – 86%**.
- **$D_{2+}$ Transitive Deps (e.g. `polyglot.py`)**: Nominal symbols only. Token savings: **91.9%**.

---

## Installation

### 1. PyPI (Official Package)
Install via `pip` or isolated environment manager:
```bash
pip install ctxfw
```
Or for global CLI availability using `pipx`:
```bash
pipx install ctxfw
```

### 2. Native MCP Stdio Configuration
Register the stdio server directly in your IDE or client configuration (`claude_desktop_config.json`, Cursor, Windsurf, or Antigravity):
```json
{
  "mcpServers": {
    "ctxfw": {
      "command": "ctxfw",
      "args": ["mcp"]
    }
  }
}
```

### 3. Verified MCP Registry (Glama)
CTXFW is indexed and verified with Grade A compliance on the official Glama MCP registry:

Glama

Direct access to tool inspection, schemas, and live diagnostic telemetry on Glama.

---

## System Diagnostics

Validate local environment readiness, stdio isolation purity, SQLite WAL concurrency, and Tree-Sitter grammars with a single command:

```bash
ctxfw doctor
```

```text
========================================================================
  CTXFW DOCTOR // HIGH-ASSURANCE HEALTH & ISOLATION DIAGNOSTIC
========================================================================
[PASS]   Python Package & sys.path        ctxfw v3.5.0 loaded cleanly.
[PASS]   MCP stdio Stream Isolation       100% pure JSON-RPC on stdout. Diagnostic logs isolated to stderr.
[PASS]   Global CLI Executable (PATH)     Binary 'ctxfw' found in PATH.
[PASS]   Axiomatic Sieve Engine           Evaluation verified (ACI: 1.0000, Invariants: 5).
[PASS]   SQLite WAL Cache & Concurrency   Journal mode: WAL, Busy timeout: 5000ms.
[PASS]   Polyglot Tree-Sitter Grammars    Initialized language parsers (typescript, go, java).
------------------------------------------------------------------------
Overall Verdict:            [HEALTHY] [ATTESTED] Perimeter defense operational.
========================================================================
CTXFW // 72.4% AST Bloat Eliminated. Zero Telemetry Egress.
Need team-wide budget circuit breakers or multi-node proxy governance?
Control Plane & Enterprise Licensing: https://ctxfw.heuristicolab.com
========================================================================
```

---

## Architecture

CTXFW enforces a strict deterministic perimeter dividing probabilistic agent code from the core codebase:

```
PROBABILISTIC DOMAIN                      DETERMINISTIC PERIMETER
┌───────────────────────┐                  ┌────────────────────────────────────────┐
│  Autonomous AI Agent  │                  │             CTXFW ENGINE               │
│  (Claude / Gemini /   │                  │                                        │
│   Cursor / Antigravity│                  │  ┌──────────────────────────────────┐  │
└───────────┬───────────┘                  │  │   Polyglot AST Topological Engine│  │
            │                              │  │  - Python (ast)                  │  │
            │  Target Context / Brief      │  │  - TypeScript / Go / Java (CST)  │  │
            ▼                              │  │  - Multi-Depth Interface Stubs   │  │
┌───────────────────────┐                  │  └────────────────┬─────────────────┘  │
│ MCP Stdio Interceptor ├─────────────────►│                   │                    │
└───────────────────────┘                  │  ┌────────────────┴─────────────────┐  │
                                           │  │  SQLite WAL High-Concurrency     │  │
                                           │  │  Semantic Cache (<5ms warm hit)  │  │
                                           │  └────────────────┬─────────────────┘  │
                                           │                   ▼                    │
                                           │         [ ACI >= 0.9000? ]             │
                                           │          /              \              │
                                           │       YES                NO            │
                                           │        │                  │            │
                                           │        ▼                  ▼            │
                                           │ ┌──────────────┐   ┌─────────────────┐ │
                                           │ │ VERIFIED     │   │ QUARANTINED     │ │
                                           │ │ SHA-256 Seal │   │ Execution Halt  │ │
                                           │ └──────┬───────┘   └────────┬────────┘ │
                                           └────────┼────────────────────┼──────────┘
                                                    │                    │
                                                    ▼                    ▼
                                           [ Code Generation ]   [ Forensic Report ]
                                           [ & Git Permitted ]   [ Pre-Commit Abort]
```

### Key Subsystems:
1. **Polyglot Tree-Sitter Pruner**:
 - Compiles topological dependency trees. Distance 0 (target file) is preserved in full; Distance 1 dependencies retain signatures and docstrings while pruning implementation logic; Distance 2+ dependencies are reduced to compact type stubs.
 - Built-in support for **Python**, **TypeScript/JavaScript**, **Go**, and **Java**.
2. **SQLite WAL High-Concurrency Semantic Cache**:
 - Atomic multi-process caching configured with Write-Ahead Logging (`PRAGMA journal_mode=WAL`) and `busy_timeout=5000ms`, delivering sub-millisecond warm cache hits.
3. **Axiomatic Sieve Engine**:
 - Formal specification gatekeeper evaluating requirements against 5 negative invariants (`shall never`), explicit mathematical bounds, deterministic state machines, and a 4-class error taxonomy.

---

## Zero-Touch Provisioning

Inject perimeter rules, MCP server declarations, and pre-commit sentinels into your workspace:

### Global IDE Integration
```bash
ctxfw init --global
```
Automatically configures Google Antigravity, Cursor, and Claude Desktop.

### Repository Pre-Commit Sentry
```bash
ctxfw init --repo .
```
Deploys `.git/hooks/pre-commit` to prevent uncertified code commits lacking an attested specification brief.

---

## Enterprise Governance

For distributed engineering teams requiring centralized policy controls:
- **Team-wide LLM budget circuit breakers**: Hard token and dollar thresholds with automatic killswitches.
- **Multi-node reverse proxy governance**: Centralized firewall gateways supporting OpenAI and Anthropic streaming SSE endpoints.
- **FinOps Telemetry Ledger**: Aggregate tokens saved, cost elusion analytics, and tamper-evident audit trails.

**Control Plane & Enterprise Licensing:** https://ctxfw.heuristicolab.com

---

 ENGINEERED BY HEURISTICO LAB // SKUNK WORKS DIVISION
 HIGH-ASSURANCE DEFENSE SYSTEMS GROUP

## 关联链接

- https://ctxfw.heuristicolab.com
- https://glama.ai/mcp/servers/heuristicolab/ctxfw

## 导航

- 项目页：[[10-项目/github.com_20b2b1be]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
