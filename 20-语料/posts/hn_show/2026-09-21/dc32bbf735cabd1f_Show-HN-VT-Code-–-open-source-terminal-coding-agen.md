---
type: "corpus"
item_id: "dc32bbf735cabd1f"
title: "Show HN: VT Code – open-source terminal coding agent in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48332098"
project_url: "https://github.com/vinhnx/VTCode"
author: "vinhnx"
published_at: "2026-05-30T03:07:25Z"
captured_at: "2026-09-21T02:52:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_vinhnx
  - story_48332098
  - show_hn
metrics: {"points": 16, "comments": 6, "engagement_velocity": 16}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:144d"
---

# Show HN: VT Code – open-source terminal coding agent in Rust

> [!info] 一句话导读
> VT Code is an open-source coding agent with LLM-native code understanding and robust shell safety. Supports multiple LLM providers with automatic failover and e…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48332098>
> 指标：点赞=16 · 评论=6 · engagement_velocity=16
> 作者：vinhnx　|　发布：2026-05-30T03:07:25Z
> 项目链接：<https://github.com/vinhnx/VTCode>
> 采集：2026-09-21T02:52:55+08:00　|　id：`dc32bbf735cabd1f`

## 正文

# vinhnx/VTCode

VT Code is an open-source coding agent with LLM-native code understanding and robust shell safety. Supports multiple LLM providers with automatic failover and efficient context management.

- Stars: 686
- Forks: 58
- Watchers: 686
- Open issues: 0
- License: MIT License
- Homepage: https://vinhnx.github.io
- Default branch: main
- Created: 2025-08-29T09:01:48Z

## Languages

- JavaScript
- PowerShell
- Python
- Ruby
- Rust
- Shell
- TypeScript

## Topics

- agent
- cargo
- cli
- codingagent
- crossterm
- ratatui
- rust
- terminal
- tui

## Top Contributors

- vinhnx (5470 contributions)
- dependabot[bot] (57 contributions)
- vinhnguyenxuan-ct (24 contributions)
- oiwn (6 contributions)
- kernitus (4 contributions)
- chenrui333 (3 contributions)
- Sachin-Bhat (3 contributions)
- leonj1 (2 contributions)
- gzsombor (2 contributions)
- lucaszhu-hue (2 contributions)

---

## README

     
 Secure, open, universal.

## What is VT Code?

VT Code is a local-first coding agent built in Rust, the only one with defense-in-depth security gating, broad LLM provider support, open protocols (Open Responses, A2A, MCP, ATIF), an extensible skill framework, delegated subagents, and rich tooling for long-running autonomous workflows.

## Features

- **Agent runtime** - Interactive TUI, slash commands, streaming, `ask`/`exec` CLI, session resume
- **Coding tools** - Safe file ops, ripgrep search, fuzzy discovery, code intelligence, project indexing, terminal execution
- **Extensibility** - Agent Skills, MCP client/server, lifecycle hooks, subagents, custom providers, Zed ACP, VS Code, Claude Code
- **Model providers** - 21+ LLM providers: Anthropic, OpenAI, Gemini, OpenRouter, Ollama, LM Studio, and more
- **Safety** - Restricted shell sandbox, tool guardrails, subprocess isolation, full audit logging
- **Protocols** - Open Responses, Agent2Agent (A2A), ATIF, Anthropic Messages API

## Quick start

### Installing and running VT Code

```shell
curl -fsSL https://raw.githubusercontent.com/vinhnx/vtcode/main/scripts/install.sh | bash   # macOS / Linux (recommended)
```

Then run `vtcode` to get started.

### Common commands

```shell
vtcode                        # launch interactive TUI
vtcode ask "explain Rc vs Arc"  # one-shot question, no tools
vtcode exec "refactor main.rs" # headless task with full tool access
vtcode review                  # review uncommitted changes
vtcode --resume                # pick up the last session
```

## Documentation

- **Interactive TUI** - Primary agents, slash commands (`/model`, `/review`, `/mcp`, `/skills`, `/theme`, `/compact`, `/schedule`)
- **Full automation** - `--full-auto` CLI, plan-build-evaluate harness, subagents, scheduled tasks
- **Providers** - Setup guides for all 21 providers
- **Configuration** - `vtcode.toml`, tool config, lifecycle hooks
- **Agent Skills** - Creating, loading, and sharing skills
- **MCP Integration** - Client and server modes
- **Editor guides** - Zed ACP, VS Code, Claude Code
- **Safety** - Shell sandbox, security hardening, threat model
- **Protocols** - Open Responses, ATIF, A2A, Anthropic Messages API

## Providers

VT Code supports 21 LLM providers out of the box, plus any OpenAI-compatible API via `[[custom_providers]]`.

### All providers

- **Cloud LLMs** - Anthropic · OpenAI · Gemini
- **Gateways** - OpenRouter · Atlas Cloud · Evolink
- **Local inference** - Ollama · LM Studio · llama.cpp
- **Other** - GitHub Copilot · Anthropic API Compat

Read: Provider Guides.

### Xiaomi MiMo V2.5 Series

 Proud partner of the Xiaomi MiMo Orbit Program

Xiaomi MiMo V2.5 Pro ships as the default model in VT Code, available both natively and through OpenRouter. It brings a 1M-token context window, deep reasoning, and strong agentic performance to every session.

- **Xiaomi MiMo** - `mimo-v2.5-pro` · `mimo-v2.5` · *1M context*
- **OpenRouter** - `xiaomi/mimo-v2.5-pro` · `xiaomi/mimo-v2.5` · *1M context*

Pricing: Pay-as-you-go · Subscription · Quick Access · Docs · OpenRouter

> **Get started with MiMo Open Platform** — Xiaomi's most powerful AI. Sign up with invite code **K5BCAP**: both get **$2 API credits + 10% off** your first plan. *(Auto-filled on sign-up · Credits valid for 40 days)*

## Development

```shell
git clone https://github.com/vinhnx/vtcode.git
cd vtcode
./scripts/run-debug.sh
```

Rust stable, edition 2024, MSRV 1.88.

```shell
./scripts/check-dev.sh  # fast quality gate (clippy, fmt, check)
cargo nextest run        # parallel test runner
```

## Contributing

I'd love to have you, bug reports, docs, features, ideas, all welcome. Start with issues or good first issues. AI agents see AGENTS.md. Humans see CONTRIBUTING.md.

  
  
  
  
  
  
  
  
  
  
  

## Support

VT Code is a labor of love built in my spare time. If it's helped you ship something or learn something, a sponsorship would mean the world.

    

## License

MIT License.

# skills/cartographer/SKILL.md

## 评论（6/6）

> **ninja333** · 2026-05-30T04:37:57.000Z　
> Can I run a local LLM and connect to it?

---

> **afshinmeh** · 2026-05-30T04:48:48.000Z　
> what does "LLM-native code understanding" mean in this context?

---

> **tjb777** · 2026-06-05T12:43:44.000Z　
> thanks for the project, it's great

---

> **vinhnx** · 2026-05-30T05:07:42.000Z　
> Thank you for checking out VT Code! Yes, VT Code supports connecting to local LLMs through two main providers: LM Studio and Ollama. But local LLMs inference is experimenting, as I don't have enough hardware with large VRAM to test it, my main machine is MacBook Pro M4 with just 16 GB Ram. The community always have asked for it and I would love to have sought contributor on these regards. My initial vision is to support open weight and local inference. So LM Studio and Ollama are supported but still have bugs. https://github.com/vinhnx/VTCode/blob/a154162f/docs/provider...Notes: VT Code also supports custom OpenAI-compatible providers through the custom providers' configuration, allowing you to connect to any local LLM server that exposes an OpenAI-compatible API: https://github.com/vinhnx/VTCode/blob/a154162f/docs/config/C...

---

> **vinhnx** · 2026-05-30T05:03:46.000Z　
> Thank you for checking out VT Code! “LLM-native code understanding” refers to VT Code's approach of using LLM as the primary mechanism for semantic code analysis rather than relying solely on traditional static analysis tools. I have tried using ast-grep for structured code parsing understanding as a ground truth before/after the agent executes a code analysis or does a code edit/write operation and code context understanding and symbol analysis. I also tried to use tree-sitter to enhance the user's prompt parser grammar. Example: currently I use tree-sitter bash grammar to check for user input prompts for Unix commands: “run cargo fmt” -> VT Code will detect and understand right away the intent is to run a bash command -> parse and hand it to the harness -> wait for the stdout/err. Then, parse the stdio handle to the LLM as an agent loop. This is to save context and parser roundtrip.This is just my naive implementation, so as “llm-native code understanding,” VT Code will use LLMs to perform deep code understanding across multiple programming languages as a fallback if my enhance `ast-grep` + ripgrep + tree-sitter implementation is failed, but this relies on the model's intelligent. If you follow end-of last year post-training breakthrough (GPT-5.1 and Opus 4.5 era, November 2025), I read somewhere from Anthropic and OpenAI researchers that now the models are smart enough to understanding code with more context. They even have their own internal monologue so they can reason about code grammars and code context by itself. https://github.com/vinhnx/VTCode/blob/a154162f/docs/README.m...Note: I don't have enough understanding describing this cleanly as I learn by doing mostly. However, initially when I designed and built VT Code, I had a vision of using and for AST-enhanced grep code for replacement of std grep. I also use my grep tool, called grep. `perg`). I also wanted to parse source code into concrete syntax trees usable in compilers, interpreters, text editors, and static analyzers. Also, I thought of using LSP but still exp. All this might be overhead for a small open source coding harness, but I love to build, so I thought to myself, why not, just build and learn.

---

> **vinhnx** · 2026-06-05T13:11:34.000Z　
> Thank you for checking out VT Code! I'm happy that people use and like it. Let me know if there are anything I need to make it better.

## 关联链接

- https://github.com/vinhnx/vtcode.git
- https://raw.githubusercontent.com/vinhnx/vtcode/main/scripts/install.sh
- https://vinhnx.github.io

## 导航

- 项目页：[[10-项目/github.com_679ae14c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
