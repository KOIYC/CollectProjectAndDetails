---
type: "corpus"
item_id: "9a7df706e476331b"
title: "Show HN: Lain, a structural code graph and agent coordinator for coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49781554"
project_url: "https://github.com/spuentesp/lain"
author: "spuentesp"
published_at: "2026-09-21T00:15:55Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_spuentesp
  - story_49781554
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Lain, a structural code graph and agent coordinator for coding agents

> [!info] 一句话导读
> High-performance MCP server for AI coding agents: persistent knowledge graph, blast radius analysis, semantic search. Built in Rust.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49781554>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：spuentesp　|　发布：2026-09-21T00:15:55Z
> 项目链接：<https://github.com/spuentesp/lain>
> 采集：2026-09-21T09:44:03+08:00　|　id：`9a7df706e476331b`

## 正文

# spuentesp/lain

High-performance MCP server for AI coding agents: persistent knowledge graph, blast radius analysis, semantic search. Built in Rust.

- Stars: 6
- Forks: 1
- Watchers: 6
- Open issues: 1
- License: MIT License
- Default branch: main
- Created: 2026-04-26T21:49:34Z

## Languages

- HTML
- JavaScript
- Python
- Ruby
- Rust
- Shell

## Topics

- agentic-coding
- agentic-coding-tool
- agentic-rag
- agentic-workflows
- code-intelligence
- knowledge-graph
- llm-tools
- mcp
- mcp-server
- mcp-servers
- petgraph
- rust
- structural-reasoning
- treesitter

## Top Contributors

- sPuentesPrieto (12 contributions)
- spuentesp (12 contributions)

---

## README

# LAIN-mcp

LAIN builds a map of how all the code in your project connects — what calls what, what depends on what, which files tend to change together. Then it lets your AI coding assistant ask questions about that map. So instead of the AI just looking at one file and guessing, it can ask "if I change this function, what else breaks?" and get a real answer. It plugs into any AI agent that supports MCP and runs in the background while you work.

## TL,DR:

```bash
# One-line install (interactive - will ask you to configure and add to PATH)
curl -fsSL https://raw.githubusercontent.com/spuentesp/lain/main/install.sh | bash

# After install: reload your shell (or open a new terminal)
source ~/.zshrc   # or ~/.bashrc

# Or non-interactive (skips prompts, auto-adds to PATH)
curl -fsSL https://raw.githubusercontent.com/spuentesp/lain/main/install.sh | \
  bash /dev/stdin --workspace . --transport both --yes
```
## What is Lain?

Lain is a persistent code-intelligence MCP server. It builds a queryable knowledge graph of your codebase — symbols and their relationships extracted via LSP and tree-sitter, augmented with git co-change history and optional semantic embeddings — and exposes that graph through MCP tools. The value over LSP-only or RAG-based approaches is cross-file structural reasoning: blast radius for proposed changes, transitive dependency traces, anchor identification, co-change correlation, and contextual build failure decoration so agents can reason about callers rather than just the failing line. Written in Rust, persists across sessions, stays fresh during editing via a file watcher that updates a volatile overlay layered on top of the static graph.

---

## Installation

### Quick Install (recommended - interactive)

```bash
curl -fsSL https://raw.githubusercontent.com/spuentesp/lain/main/install.sh | bash
```

The installer will **ask you** to configure:
- Workspace path
- MCP transport mode (stdio, http, or both)
- HTTP port (if using http/both)
- Target agent (auto-detects Claude Code, Cursor, Windsurf, Cline)
- Whether to download the ONNX model for semantic search

After you confirm your settings, it will:
1. Download and install LAIN to `~/.local/lain`
2. Optionally download the ONNX model (~120MB)
3. Run `lain init` with your configuration
4. Add LAIN to your agent's settings

**Non-interactive install (with options):**

```bash
# Install with specific workspace and download ONNX model for semantic search
curl -fsSL https://raw.githubusercontent.com/spuentesp/lain/main/install.sh | \
  bash /dev/stdin --workspace . --transport both --download-model --yes

# Install for specific agent
curl -fsSL https://raw.githubusercontent.com/spuentesp/lain/main/install.sh | \
  bash /dev/stdin --agent cursor --yes

# See all options
curl -fsSL https://raw.githubusercontent.com/spuentesp/lain/main/install.sh | \
  bash /dev/stdin --help
```

**Install options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--workspace PATH` | Workspace path for LAIN | `.` |
| `--transport MODE` | MCP transport: stdio, http, both | `stdio` |
| `--port PORT` | HTTP port for MCP server | `9999` |
| `--agent AGENT` | Target agent: auto, claude, cursor, windsurf, cline | `auto` |
| `--embedding-model PATH` | Path to ONNX embedding model | - |
| `--download-model` | Download default ONNX model (all-MiniLM-L6-v2.onnx, ~120MB) | - |
| `-y, --yes` | Skip all confirmation prompts | - |

**After installation:**

```bash
# Reload your shell (the installer adds to ~/.zshrc or ~/.bashrc automatically)
source ~/.zshrc   # or ~/.bashrc, then open a new terminal

# Verify installation
lain --version

# Query the graph
lain query "find Function | limit 5"
```

### Homebrew

```bash
brew tap spuentesp/lain https://github.com/spuentesp/lain
brew install lain

# Initialize
lain init
```

### Pre-built Binary

Download the latest release for your platform from GitHub releases, then:

```bash
# Make executable
chmod +x lain

# Run directly
./lain --workspace /path/to/your/project --transport stdio
```

### Build from Source

```bash
# Clone the repo
git clone https://github.com/spuentesp/lain.git
cd lain

# Build (requires Rust 1.75+)
cargo build --release

# Binary will be at ./target/release/lain
```

---

## Quick Start

### 1. Install LAIN

```bash
curl -fsSL https://raw.githubusercontent.com/spuentesp/lain/main/install.sh | bash
```

### 2. Initialize for Claude Code (or other agents)

```bash
# Auto-detect agent (Claude Code, Cursor, Windsurf, Cline)
lain init

# Or specify agent explicitly
lain init --agent claude
```

### 3. Run

```bash
# Standard mode (for Claude Code)
lain --workspace /path/to/project --transport stdio

# With HTTP diagnostics (web UI at http://localhost:9999)
lain --workspace /path/to/project --transport both --port 9999

# With semantic search (requires ONNX model)
lain --workspace /path/to/project --embedding-model ~/.local/lain/models/all-MiniLM-L6-v2.onnx
```

### 4. Verify

```bash
# Check health and LSP status
curl -s -X POST http://localhost:9999/mcp -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"get_health","arguments":{}},"id":1}'

# Query the graph directly
lain query "find Function | limit 5"
```

---

## Key Features

### Query Language (`query_graph`)
JSON-based ops array for flexible graph traversals:
```json
{
  "ops": [
    { "op": "find", "type": "Function" },
    { "op": "connect", "edge": "Calls", "depth": { "min": 1, "max": 3 } },
    { "op": "filter", "label": "test" },
    { "op": "semantic_filter", "like": "error handling", "threshold": 0.35 },
    { "op": "limit", "count": 10 }
  ]
}
```
Available ops: `find`, `connect`, `filter`, `semantic_filter`, `group`, `sort`, `limit`

### Dependency Intelligence
- **`get_call_chain`** — Shortest path between two functions
- **`get_blast_radius`** — Everything affected by a change
- **`trace_dependency`** — What a symbol depends on
- **`get_coupling_radar`** — Files that change together

### Architectural Analysis
- **`find_anchors`** — Most-called, most-stable symbols (architectural pillars)
- **`list_entry_points`** — Find `main()`, route handlers, app initialization
- **`get_context_depth`** — How far from an entry point (abstraction layers)
- **`explore_architecture`** — High-level tree of modules and files

### Search
- **`semantic_search`** — Find code by meaning, not just names (uses local ONNX embeddings)

### Code Health
- **`find_dead_code`** — Potentially unreachable code (filters trait defaults, common names)
- **`suggest_refactor_targets`** — High-coupling, low-stability nodes

### Build Integration
Lain enriches build failures with architectural context:
- **`run_build`** — Build with Rust/Go/JS/Python toolchain error parsing
- **`run_tests`** — Tests with error enrichment
- **`run_clippy`** — cargo clippy with context

---

## Requirements

| Requirement | Details |
|-------------|---------|
| Rust | 1.75 or newer |
| Git | Required for co-change analysis |
| ONNX Model | Optional — for semantic search |

### Optional: Semantic Search

For `semantic_search` to work, you need an ONNX embedding model. The easiest way to set this up is using the provided install script:

```bash
./scripts/install.sh
```

Alternatively, you can set it up manually:

```bash
# Create model directory
mkdir -p .lain/models

# Download all-MiniLM-L6-v2 (or any compatible model)
# Model produces 384-dim embeddings
curl -L https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/onnx/model.onnx -o .lain/models/model.onnx
curl -L https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer.json -o .lain/models/tokenizer.json
```

Set the model path:
```bash
export LAIN_EMBEDDING_MODEL=$PWD/.lain/models/model.onnx
# or
./lain --embedding-model ./.lain/models/model.onnx ...
```

Without the model, `semantic_search` returns "unavailable" but all other features work.

---

## MCP Transport Modes

| Mode | Command | Use Case |
|------|---------|----------|
| `stdio` | `--transport stdio` | Claude Code, MCP clients |
| `http` | `--transport http --port 9999` | Web diagnostics dashboard |
| `both` | `--transport both --port 9999` | Both stdio + diagnostics |

---

## Troubleshooting

**LSP servers not ready?**
```bash
# Install missing language servers
curl -X POST http://localhost:9999/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"install_language_server","arguments":{"language":"rust"}},"id":2}'
```

**Graph stale?**
```bash
# Sync to current git HEAD
curl -X POST http://localhost:9999/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"sync_state","arguments":{}},"id":3}'
```

**View all available tools:**
```bash
curl -s -X POST http://localhost:9999/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"get_agent_strategy","arguments":{}},"id":4}'
```

---

## A/B Testing Results

A simple A/B test was run on the `asciinema_fix_pty_bug` (a small fork i made from https://github.com/asciinema/asciinema.git ) across **5 passes, 4 times** using a script. Median numbers are reported.

| Metric | with_lain | without_lain |
|--------|-----------|--------------|
| Pass rate | 5/5 (100%) | 5/5 (100%) |
| Median duration | 39.3s | 54.1s |
| Median tokens in | 35,488 | 41,731 |

**Key observations:**

- Both conditions passed 100% — the bug fix worked in both conditions, with variation per run.
- `with_lain` used fewer input tokens (~35k vs ~42k median), a difference of ~7k tokens per run.

**About the bug:** The failing test (`pty::tests::spawn_extra_env` on macOS) stems from `handle_child()` setting env vars via `env::set_var()` before `execvp()`. The shell's interpretation of `echo -n $VAR` varies across platforms — sometimes `-n` is treated as a literal argument. The fix: use `printf "%s" "$ASCIINEMA_TEST_FOO"` instead, portable across all Unix-like systems.

> This was a test I did for A/B comparison — not a rigorous evaluation.

---

## License

MIT — Copyright (c) 2026 spuentesp

# openlayer-ai/jevals

## 评论（1/1）

> **spuentesp** · 2026-09-21T00:17:33.000Z　
> Still a wip but working. Using it on some personal projects with success. Would love opinions.

## 关联链接

- http://localhost:9999
- http://localhost:9999/mcp
- https://github.com/asciinema/asciinema.git
- https://github.com/spuentesp/lain.git
- https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/onnx/model.onnx
- https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2/resolve/main/tokenizer.json
- https://raw.githubusercontent.com/spuentesp/lain/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_b379fa8f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
