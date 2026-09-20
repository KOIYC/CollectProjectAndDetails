---
type: "corpus"
item_id: "132219dff72ba5f5"
title: "Show HN: SigMap – 81.1% retrieval hit 5, 96.9% token reduce,zero deps"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47956790"
project_url: "https://github.com/manojmallick/sigmap"
author: "manoj079"
published_at: "2026-04-30T01:02:55Z"
captured_at: "2026-09-21T02:52:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_manoj079
  - story_47956790
  - show_hn
metrics: {"points": 14, "comments": 4, "engagement_velocity": 14}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:174d"
---

# Show HN: SigMap – 81.1% retrieval hit 5, 96.9% token reduce,zero deps

> [!info] 一句话导读
> ~97% token reduction for AI coding sessions — zero deps, 33 languages, MCP server

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47956790>
> 指标：点赞=14 · 评论=4 · engagement_velocity=14
> 作者：manoj079　|　发布：2026-04-30T01:02:55Z
> 项目链接：<https://github.com/manojmallick/sigmap>
> 采集：2026-09-21T02:52:31+08:00　|　id：`132219dff72ba5f5`

## 正文

# manojmallick/sigmap

~97% token reduction for AI coding sessions — zero deps, 33 languages, MCP server

- Stars: 623
- Forks: 43
- Watchers: 623
- Open issues: 12
- License: MIT License
- Homepage: https://sigmap.io/
- Default branch: main
- Created: 2026-03-31T20:17:51Z

## Languages

- HTML
- JavaScript
- Python
- Shell
- TypeScript

## Topics

- ai
- ai-code-review
- ai-grounding
- claude
- cli
- code-context
- code-intelligence
- code-signatures
- cursor
- deterministic
- developer-tools
- github-copilot
- hallucination-detection
- llm
- mcp
- openai
- retrieval
- token-reduction
- verifiable-ai
- zero-dependencies

## Top Contributors

- manojmallick (942 contributions)
- schochastics (4 contributions)
- rudi193-cmd (4 contributions)
- octo-patch (2 contributions)
- dsolonenko (1 contributions)
- mvanhorn (1 contributions)
- github-actions[bot] (1 contributions)
- kumamaki (1 contributions)

---

## README

# ⚡ SigMap

**SigMap is the deterministic, verifiable grounding layer for AI code work.**

npm version
npm downloads
CI
Zero deps
License: MIT
GitHub Stars
Stargazer map
Discover on ShyPD

MseeP.ai Security Assessment Badge
Verified on MseeP

---

## Try it now

**No install required.** Run instantly on any machine:

```bash
npx sigmap
npx sigmap ask "Where is auth handled?"
```

Zero config. Zero dependencies. Under 10 seconds.

---

## What is SigMap?

SigMap builds a **deterministic, auditable signature-and-evidence map** of your codebase — no LLM calls, no embeddings, byte-stable output — so AI agents, CI, and reviewers can *trust and verify* which files and symbols are real before acting. Same repo in, same map out, every time.

That map is exactly what agentic grep is worst at: reproducible, auditable context an agent can consume without a copy-paste, and a grounding check that proves an AI answer is anchored to real signatures and line numbers. Token reduction comes for free — but trust is the point.

**Model-agnostic.** Works with:
- **Cloud LLMs:** Claude, GPT-4, Copilot, Gemini
- **Open-source agents:** OpenCode, Aider, OpenHands, Cline
- **Local LLMs:** Ollama, llama.cpp, vLLM (no API keys, full privacy)
- **Any editor:** VS Code, Cursor, Windsurf, Neovim, JetBrains
- **Any model:** Use what you want, no vendor lock-in

---

## Why SigMap?

**Deterministic and verifiable — the two things an agentic-grep loop can't give you:**
- **Deterministic** — no LLM calls, no agent loop; the same repo always produces a byte-identical map you can diff, cache, and gate in CI.
- **Auditable & grounded** — every file and symbol traces to a real line anchor; `sigmap verify` flags any AI claim that isn't.
- **Zero dependencies** — `npx sigmap` on any machine; no embeddings, no vector DB, no hosted service, fully offline.

**Proof it pays off** (full benchmark below):

- **81.1% hit@5** — right file in top 5 results (vs 44.0% single-shot grep baseline — 1.73× lift)
- **96.8% token reduction** — average across 21 real repos
- **64.8% task-success proxy** — modeled from retrieval tiers, not measured LLM sessions
- **1.54 prompts per task** — down from 2.84 (45.7% fewer retries, modeled)

- ** 33 languages supported** — TypeScript, Python, Go, Rust, Java, R, and more
- **No vendor lock-in** — works with any AI assistant or local LLM
- **No API costs** — use local models (Ollama, llama.cpp, vLLM) with zero token fees
- **Full privacy** — keep your code and context on your machine

---

## 🔒 `sigmap verify` — the grounding flagship

The one thing no agentic-grep loop, and no competitor, gives you: **prove an AI answer is anchored to real signatures and line numbers before you trust it.** Deterministic, offline, no LLM — SigMap indexes your repo *plus the libraries actually installed here* and flags every fabricated file, import, symbol, test, or npm script.

```bash
sigmap verify answer.md                 # ✓ grounded, or a line-by-line list of fabrications
sigmap verify answer.md --json          # machine-readable report; exits 1 if any issue (CI gate)
sigmap verify answer.md --report        # standalone red/amber/green HTML report
```

```text
[sigmap] ✗ answer.md — 2 issues found
  fake-file: 1  fake-test-file: 0  fake-import: 0  fake-symbol: 1  fake-npm-script: 0

  L12  [Fake file]    src/auth/session-store.js does not exist
  L27  [Fake symbol]  authorize() — did you mean authenticate()?
```

`verify` is the flagship; `verify-ai-output` remains as the full command name. Pair it with `sigmap verify-plan` (check a plan before execution) and the `verify_suggestion` MCP tool (verify AI code against repo + private + installed-library symbols mid-session).

---

## Replace this with SigMap

| Without SigMap | With SigMap |
|---|---|
| ❌ Non-reproducible agent guesses | ✅ Deterministic map — same input, same output, every time |
| ❌ "Trust me" AI answers | ✅ Grounded — right file in context 81% of the time, every symbol on a real line anchor |
| ❌ Embeddings / vector DB required | ✅ Zero deps, no infra, fully offline |

---

## How it works

```
Ask → Rank → Context → Validate → Judge → Learn
```

1. **Ask** — `sigmap ask "Where is auth handled?"` — ranked file list
2. **Rank** — TF-IDF scores every file against your query
3. **Context** — writes compact signatures to your AI's context file
4. **Validate** — `sigmap validate` — confirms right files are in scope
5. **Judge** — `sigmap judge` — scores answer groundedness against context
6. **Learn** — `sigmap weights` — boosts files that keep solving your tasks

---

## Benchmark

```
Benchmark : sigmap-v8.28-main (21 repositories, including R language)
Date      : 2026-08-22

Hit@5          : 81.1%   (grep-agent baseline 44.0%  — 1.73× lift)
Token reduction: 96.8%   (across 21 repos)
Prompt reduction : 45.7% (2.84 → 1.54 prompts per task, modeled)
Task success   : 64.8%   (proxy — modeled from retrieval tiers)
Repos tested   : 21 (JavaScript, Python, Go, Rust, Java, R, C++, C#, Dart, Swift, Ruby, PHP, Scala, Kotlin, and more)
```

 All numbers above are generated from `benchmarks/latest.json` (`npm run metrics:sync`) — never hand-typed.

Measured on 90 coding tasks across 18 real public repos. No LLM API — fully reproducible.

**Resources:**
- Full methodology →
- Benchmark suite (GitHub) — scripts, tasks, and raw data
- Benchmark data (Zenodo) — archived results for reproducibility

---

## Install

**Try without installing:**

```bash
npx sigmap
```

**Install globally:**

```bash
npm install -g sigmap
```

**Install per-project:**

```bash
npm install --save-dev sigmap
```

**Standalone binary** — no Node.js required:

| Platform | Download |
|---|---|
| macOS Apple Silicon | `sigmap-darwin-arm64` |
| macOS Intel | `sigmap-darwin-x64` |
| Linux x64 | `sigmap-linux-x64` |
| Windows x64 | `sigmap-win32-x64.exe` |

Each binary ships with a `.sha256` checksum. Verify a binary →

**Volta:**

```bash
volta install sigmap
```

---

## Integrations

**AI assistants — one run, all of them:**

| Adapter | Output file | Used by |
|---|---|---|
| `copilot` | `.github/copilot-instructions.md` | GitHub Copilot, OpenCode |
| `claude` | `CLAUDE.md` | Claude / Claude Code |
| `cursor` | `.cursorrules` | Cursor, Cline |
| `windsurf` | `.windsurfrules` | Windsurf |
| `openai` | `.github/openai-context.md` | OpenAI API, Aider, local Ollama/llama.cpp |
| `gemini` | `.github/gemini-context.md` | Google Gemini |
| `codex` | `AGENTS.md` | OpenAI Codex (legacy) |
| `willow` | _Willow MCP store (HTTP POST — no file)_ | Willow knowledge store |

```bash
sigmap --adapter copilot   # default — works with Copilot, OpenCode
sigmap --adapter openai    # works with Ollama, llama.cpp, vLLM, Aider
sigmap --adapter claude    # works with Claude Code
```

**Open-source agents & local LLMs:**

Use SigMap with open-source tools and fully self-hosted setups:
- **Open-source agents guide →** — OpenCode, Aider, OpenHands, Cline
- **Local LLMs guide →** — Ollama, llama.cpp, vLLM (no API keys, full privacy)

**IDE extensions:**

| IDE | Install | Source | Features |
|-----|---------|--------|----------|
| **VS Code** | Marketplace · Open VSX | github.com/manojmallick/sigmap-vscode | Status bar health grade, stale context alerts, one-click regen |
| **JetBrains** | Marketplace | github.com/manojmallick/sigmap-jetbrains | IntelliJ IDEA, WebStorm, PyCharm, GoLand — tool window + actions |
| **Neovim** | lazy.nvim / packer / vim-plug | github.com/manojmallick/sigmap.nvim | `:SigMap`, `:SigMapQuery` float window, statusline widget |

**MCP server** — 21 on-demand tools for Claude Code and Cursor:

```bash
sigmap --mcp
```

Tools: `read_context`, `search_signatures`, `get_map`, `create_checkpoint`, `get_routing`, `explain_file`, `list_modules`, `query_context`, `get_method_impact` (per-symbol blast radius), `get_impact`, `get_lines`, `read_memory`, `get_callee_signatures`, `get_diff_context` (changed files + signatures + blast radius), `get_architecture_overview` (modules, hub files, cycles), `verify_suggestion` (ground AI code against repo + installed libraries), `squeeze_output` (compress noisy tool/log/JSON output mid-session), plus the live-index notifications `sigmap_notify_file_created`, `sigmap_notify_symbol_added`, and `sigmap_notify_file_deleted`. Full reference: llms-full.txt.

SigMap doesn't compete with your agent's live search — it's what the live loop **calls for grounding**: grep finds the file; `query_context` → `get_callee_signatures` → `get_lines` → `verify_suggestion` → `get_method_impact` prove the symbols, lines, calls, and blast radius — deterministically. See the agent live-loop guide.

---

## Grounded creation & guardrails

Verify AI work against the live index instead of trusting it blind:

```bash
sigmap conventions                  # extract the repo's file-naming / export / test conventions
sigmap scaffold "<name>"            # propose a convention-matched file/dir (refuses if conventions conflict)
sigmap verify-plan <plan.md>        # check a plan: do the files/symbols exist? blast radius? scope?
sigmap verify-ai-output <answer.md> # flag fabricated files/imports/symbols/tests in an AI answer
sigmap review-pr                    # audit a diff: scope drift, god-node edits, missing tests, security files
sigmap create "<task>"             # run the whole pipeline: scaffold → verify-plan → verify-ai-output → review-pr
```

---

## Evidence Pack & diagnostics

The **Evidence Pack** is the consumable, machine-readable replacement for "paste this into your prompt" — a deterministic JSON artifact (with a Markdown handoff mode) that an agent or CI step reads directly, with zero copy-paste:

```bash
sigmap evidence "how does auth work"            # → .context/evidence-pack.json (deterministic, byte-stable)
sigmap evidence "how does auth work" --markdown # Markdown handoff to stdout
sigmap doctor                                   # diagnose config, index, freshness, coverage, MCP wiring — with fixes
```

Each pack carries the ranked files, the symbols and line anchors that justify them, the token budget, the dropped files (and why), and the grounding summary — so a consumer can trust and audit the context instead of guessing.

---

## Agent recipes

SigMap treats coding agents as **consumers, not competitors**: it hands them a deterministic, auditable map the agent can read on demand. Wire any of them up once, then let the agent pull context or consume an Evidence Pack.

| Agent | One-time setup | How it consumes SigMap |
|---|---|---|
| **Claude Code** | `sigmap mcp install claude` | 21 MCP tools (`search_signatures`, `get_lines`, `get_diff_context`, `squeeze_output`…) |
| **Cursor** | `sigmap mcp install cursor` | MCP tools, plus the `cursor` adapter writes `.cursorrules` |
| **Cline** | `sigmap mcp install cursor` | Reads `.cursorrules`; same MCP server |
| **Continue** | `sigmap mcp install vscode` | MCP tools inside the Continue extension |
| **Aider** | `sigmap --adapter openai` | Reads `.github/openai-context.md` before a session |
| **OpenHands** | `sigmap evidence " "` | Consumes `.context/evidence-pack.json` directly |
| **Codex CLI** | `sigmap mcp install codex` | MCP tools, plus the `codex` adapter writes `AGENTS.md` |

```bash
# Pattern 1 — give the agent live, on-demand access (MCP)
sigmap mcp install claude        # one of: claude|cursor|windsurf|vscode|zed|codex|gemini|opencode|mcp
                                 # add --global for a user-level install

# Pattern 2 — hand the agent a deterministic Evidence Pack (no MCP, no copy-paste)
sigmap evidence "implement rate limiting" --markdown   # or read .context/evidence-pack.json
```

See `sigmap mcp list` for every supported client.

---

## Try it

```bash
# 1. Generate context for your project
npx sigmap

# 2. Ask a question — get ranked files
sigmap ask "Where is auth handled?"

# 3. Validate — confirm the right files are in scope
sigmap validate --query "auth login token"

# 4. Judge — score your AI's answer for groundedness
sigmap judge --response response.txt --context .context/query-context.md

# 5. Inspect health
sigmap --health
```

---

## Start guide

| Who | Start here |
|---|---|
| 👶 **New** | Quick start guide — setup in 60 seconds |
| ⚡ **Daily** | `sigmap ask` / `sigmap validate` / `sigmap judge` |
| 🧠 **Advanced** | Context strategies · MCP setup |
| 🏢 **Teams** | Config reference · CI setup |

---

## Docs

**sigmap.io**

| Section | Link |
|---|---|
| CLI reference (32 commands) | cli.html |
| Benchmark methodology | benchmark.html |
| Config reference | config.html |
| Roadmap | roadmap.html |
| 33 languages | generalization.html |

---

## Support

If SigMap saves you context or API spend, a ⭐ on GitHub helps others find it.

🌍 See where SigMap's stargazers are around the world on the **StarMapper star map →**.

📈 Watch SigMap's growth on the **Star History chart →**.

Report an issue · Changelog

---

## Sponsor

SigMap is built and maintained by one developer, kept **zero-dependency**, offline, and free. If it saves your team context or API spend, sponsoring keeps it that way — and funds the benchmark CI, the `sigmap.io` domain, and ongoing supply-chain hardening.

💜 **Become a sponsor →** · see **SPONSOR.md** for tiers and exactly where your support goes. Any amount helps — even $1/mo — and a ⭐ or a share counts too.

---

## Contributing

SigMap welcomes contributions!

**Before submitting a PR:**
1. Read CONTRIBUTING.md
2. Check Discussions → Announcements for workflow setup
3. Target the `develop` branch (not main)
4. Follow the contributor checklist

See .github/PULL_REQUEST_TEMPLATE.md for the PR checklist. All contributors are credited in the CHANGELOG and release notes.

---

## Why not embeddings?

| | Embeddings | SigMap |
|---|:---:|:---:|
| Vector DB required | ✅ | ❌ |
| Infrastructure to run | ✅ | ❌ |
| Drift over time | ✅ | ❌ |
| Deterministic results | ❌ | ✅ |
| Zero-config setup | ❌ | ✅ |
| Works offline | ❌ | ✅ |

- **No vector DB** — signatures are plain text files committed to your repo
- **No infra** — runs locally, zero cloud dependencies
- **No drift** — regenerating is `npx sigmap`, not a reindex pipeline
- **Deterministic** — same input always produces same ranked output
- **Faster** — TF-IDF ranking runs in milliseconds, no embeddings to compute

---

## 33 languages

TypeScript · JavaScript · Python · Java · Kotlin · Go · Rust · C# · C/C++ · Ruby · PHP · Swift · Dart · Scala · Vue · Svelte · HTML · CSS/SCSS · YAML · Shell · SQL · GraphQL · Terraform · Protobuf · Dockerfile · TOML · XML · Properties · Markdown · R · GDScript

All implemented with zero external dependencies.

Full language table →

### Extraction honesty

Not all 33 languages get the same depth — and we say so plainly:

| Tier | Coverage | Depth |
|------|----------|-------|
| **AST** | Python (`python3` on PATH; regex fallback without) | Full parse |
| **Anchored regex** | 11 brace languages (JS, TS, Go, Rust, Java, Kotlin, Swift, PHP, Scala, Dart, C#) | Declarations + `:start-end` line anchors; doc hints on 6 |
| **Pattern/heuristic** | Everything else + generic fallback | Line-oriented patterns |

Caps: 25 signatures/file · 8 members/block. Full details, known regex gaps, and what they mean for `verify`: **KNOWN_LIMITATIONS.md**.

---

## License

MIT © 2026 Manoj Mallick · Made in Amsterdam

---

**Docs · Changelog · Roadmap · npm**

⭐ Star on GitHub if SigMap saves you tokens.

## 评论（4/4）

> **manoj079** · 2026-04-30T01:42:26.000Z　
> * * *

---

> **sudippoka** · 2026-04-30T15:44:34.000Z　
> Very helpful

---

> **aka1356** · 2026-05-01T07:49:39.000Z　
> Impressive: SigMap shows you can get ~80%+ hit@5 and ~97% token reduction with simple signature-based heuristics—no embeddings, no deps, just smart context pruning.

---

> **manoj079** · 2026-04-30T22:30:00.000Z　
> Thanks! Happy to go deeper on any part — the TF-IDF ranking logic, the import graph construction, or the benchmark methodology. What are you working on?

## 关联链接

- https://sigmap.io/

## 导航

- 项目页：[[10-项目/github.com_a9565de4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
