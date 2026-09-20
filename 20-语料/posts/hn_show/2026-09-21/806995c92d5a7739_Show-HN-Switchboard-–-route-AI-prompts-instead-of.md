---
type: "corpus"
item_id: "806995c92d5a7739"
title: "Show HN: Switchboard – route AI prompts instead of capping budgets"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48725764"
project_url: "https://github.com/aivinay/switchboard"
author: "ai_vinaygupta"
published_at: "2026-06-29T21:50:23Z"
captured_at: "2026-09-21T03:11:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_ai_vinaygupta
  - story_48725764
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Switchboard – route AI prompts instead of capping budgets

> [!info] 一句话导读
> Privacy-aware, local-first router for your CLI coding agents (Codex, Claude Code) and local LLMs (Ollama) — keeps sensitive prompts on-device and cuts premium-m…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48725764>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ai_vinaygupta　|　发布：2026-06-29T21:50:23Z
> 项目链接：<https://github.com/aivinay/switchboard>
> 采集：2026-09-21T03:11:02+08:00　|　id：`806995c92d5a7739`

## 正文

# aivinay/switchboard

Privacy-aware, local-first router for your CLI coding agents (Codex, Claude Code) and local LLMs (Ollama) — keeps sensitive prompts on-device and cuts premium-model usage.

- Stars: 6
- Forks: 1
- Watchers: 6
- Open issues: 0
- License: MIT License
- Homepage: https://github.com/aivinay/switchboard
- Default branch: main
- Created: 2026-06-22T19:12:52Z

## Languages

- CSS
- Dockerfile
- HTML
- JavaScript
- Makefile
- Python
- Shell
- TypeScript

## Topics

- ai-agents
- claude-code
- codex
- fastapi
- llm
- llm-orchestration
- llm-routing
- local-first
- local-llm
- model-routing
- ollama
- privacy
- privacy-preserving-ai
- python
- semantic-memory

## Top Contributors

- aivinay (100 contributions)

---

## README

 62% fewer premium-agent calls · 4.1/5 quality vs 4.6/5 always-premium · 0 benchmark leaks observed

 Install ·
 Evaluation ·
 How it works ·
 Privacy ·
 Paper ·
 Docs

---

Switchboard web UI demo — automatic routing, the privacy floor, and the savings drawer

 Local by default, Codex for code, Claude Opus for hard reasoning — and a privacy floor that keeps secrets on your machine.

Switchboard wraps the CLI tools you already use — no separate service, no proxy, no resold API access — and routes each prompt with deterministic rules before any learned classifier runs.

In its 100-case benchmark, Switchboard kept **62% of requests off premium
agents** while reaching **4.1/5 quality** against a **4.6/5 always-premium
baseline**, with **100% answered** and **no benchmark leaks observed**. See
Evaluation for the numbers and reproduction bundle.

Use it when you want to:

- **Spend premium agent quota where it matters** instead of sending every prompt
 to the most expensive backend.
- **Keep sensitive prompts local** with a deterministic privacy floor that
 learned routing cannot override.
- **Switch backends mid-session without losing context** — shared session history, semantic memory, and redaction travel with you across Ollama, Codex, and Claude Code.

## What it does

- **Routes** across local Ollama models, the **Codex** CLI, and **Claude Code** — deterministic rules first, with optional tiny learned classifiers for recall.
- **Recommends** local Ollama model packs for your detected RAM, from a tiny `llama3.2:3b` floor tier through larger 2026 packs.
- **Private mode** — a deterministic keyword/PII/secret-format floor blocks sensitive prompts from ever reaching a subscription backend, even on fallback.
- **Grounds** answers with deterministic tools (time/date, safe calculator, unit conversion, keyless live stock & news) instead of letting a model guess.
- **Carries context** across backend switches: recent user, assistant, and tool turns are assembled into one redacted session prompt.
- **Compresses** long context with a dependency-free heuristic by default, or the
 optional Headroom engine when you install the `headroom` extra and set
 `compression_engine: "headroom"`.
- **Remembers** across backends via local embedding-based semantic memory, with SQLite search available for direct memory lookup.
- **Escalates** weak local answers only when enabled, never through the privacy floor.
- **Shows** local savings, compression, premium-limit, route-chip, copy/stop, and
 thinking-status metadata in the web UI.
- **Explains every decision** and records metadata-only backend telemetry;
 chat history and memory stay in local SQLite for continuity.
- **Ships evaluation tooling** — mock CI evals, real-backend smoke tests, and
 the 100-case quality benchmark; the paper's multi-run statistical harness
 lives in the Zenodo reproduction bundle.

## How it works

```
  UI / CLI  ──►  Session manager (shared history across all backends)
                      │
                      ▼
              Capability detector (regex) ◄──► deterministic tools
                      │  (learned tool dispatcher recovers misses; tool verifies)
                      ▼
              Privacy floor  (keywords + PII + secret formats — a match is FINAL)
                      │  (learned sensitivity escalator may only ADD protection)
                      ▼
              Deterministic policy   ← always wins; unknown ⇒ local
                      │  (learned router supplies recall: tool / local / coding / reasoning)
                      ▼
              Context builder + redaction ◄── semantic memory
                      │
                      ▼
              Compression (metadata + history-only context pass)
                      │
                      ▼
        Ollama (default) │ Codex (coding) │ Claude Code (reasoning)
                      │
                      ▼
              Response sanitizer ─► metadata-only telemetry
```

The organizing invariant: **deterministic policy always precedes and overrides
the learned components.** Privacy, tool grounding, forced selection, and
fallback keep working even when the local model runtime — and therefore every
learned component — is down.

## Get started

```bash
pip install switchboard-local
```

The current release is **0.6.2**. For source installs, run `make install` from
this checkout or install from the git tag:

```bash
pip install "git+https://github.com/aivinay/switchboard@v0.6.2"
```

```bash
# point it at a local model runtime (install Ollama: https://ollama.com/download)
ollama pull llama3.2:3b        # default local model
ollama pull nomic-embed-text   # embeddings for learned routing + semantic memory

# sanity-check your setup
switchboard doctor

# choose a hardware-appropriate local model pack
switchboard models --recommend

# ask — Switchboard routes it, grounds it, and tells you why
switchboard ask "summarize this error log and suggest a fix"

# see the routing decision without running anything
switchboard route "refactor the auth module and add tests"

# prefer your browser? launch the local web UI, then open http://127.0.0.1:8080/ui
switchboard ui
```

Requires **Python 3.11+**. Codex / Claude Code backends are optional — without
them, everything routes locally. If you have them, sign in to each CLI as usual
and keep it on your `PATH`; `switchboard doctor` reports what Switchboard can
see, and answers will show `Backend: codex` or `Backend: claude-code`
(docs/usage.md). CI runs on Linux and development happens on
macOS; Windows is untested.

## Context, memory, and tokens

Switchboard has two user-facing CLI surfaces:

- `switchboard route ...` previews the same core backend decision without calling a model.
- The web UI, bare `switchboard ask ...`, and `switchboard ask --backend auto ...` use the stateful core workflow: shared sessions, model switching, semantic-memory retrieval, context-boundary compression, and backend telemetry all run on the same path.

Example stateful CLI session:

```bash
switchboard ask --backend auto --new-session "Remember: prefer local models for private notes."
switchboard ask --backend auto --session <session_id> --memory "What should you remember?"
```

Long prompts and long sessions record token estimates and savings metadata. The request-level pass can shorten an oversized raw prompt; the context-boundary pass then compresses only `<recent_conversation>`. The `<trusted_facts>`, `<long_term_memory>`, and `<current_user_request>` blocks are protected from that second pass so grounding and intent are not traded away for token budget.

Memory is local. `switchboard memory add` stores the item in SQLite and, when `semantic_memory_enabled` is on and Ollama can serve `nomic-embed-text`, indexes an embedding for cross-backend retrieval. `switchboard memory search` works as local text search even when embeddings are unavailable.

Details: docs/context-memory-compression.md.

## Evaluation

A 100-case benchmark across five task categories (coding, reasoning,
summarization, private, grounding), run on real backends and judged by a local
model, over **multiple independent runs** (means shown; full per-condition
numbers, confidence intervals, and significance tests are in the paper):

| Policy | Quality (1–5) | Premium usage | Privacy leaks | Answered |
|-------------------|:-------------:|:-------------:|:-------------:|:--------:|
| always-local | 3.4 | 0% | **0** | 100% |
| rules | 3.8 | 27% | **0** | 100% |
| hybrid | 3.9 | 28% | **0** | 100% |
| **learned** | **4.1** | 38% | **0** | 100% |
| always-premium | 4.6 | 100% | **0** | 61%¹ |

 ¹ The "just use the premium agent for everything" baseline must block every
sensitive prompt to stay leak-free, so its coverage collapses — exactly the gap
Switchboard closes. No benchmark leaks were observed in any condition or run.

These numbers come from a real-backend benchmark whose full harness travels with the paper's reproduction bundle on Zenodo.

## Context: why this exists (Uber, Microsoft, 2026)

Some employers have begun rationing AI coding-tool spend: Uber reportedly
capped engineers at $1,500/month per AI tool after burning its 2026 AI budget
in four months (Bloomberg);
Microsoft's Experiences + Devices org reportedly moved off Claude Code to
GitHub Copilot CLI (Windows Central).

A spend cap controls the invoice, but it does not decide which work actually
needs a premium model or which prompts should never leave the machine. A better
pattern is **routing, not blanket rationing**: decide request by request what
belongs local, what needs a coding agent, and what is worth premium reasoning.

Switchboard is a reference implementation of that pattern for a single
workstation. It is not yet an enterprise product; it is the smallest honest
proof that local-first routing can work, with a reproducible benchmark to back
it.

## Privacy

Switchboard is local-first and privacy-aware by construction:

- The **deterministic privacy floor runs before any non-local routing**; a positive verdict is final and cannot be overridden by a learned component or by prompt wording.
- **Secret-format detection** (cloud keys, JWTs, PEM blocks, env credentials) shares its patterns with context redaction, so the routing boundary and the redactor can't drift apart.
- **Metadata-only telemetry** — prompt and response bodies are not stored in
 backend telemetry by default; session messages and memory records are local
 SQLite data used for shared context.
- The web UI's **Private chat** toggle persists on the server session and forces Ollama without premium fallback.
- Semantic-memory **embeddings and the eval judge run locally**.
- Version surfaces (`switchboard version`, `switchboard upgrade --check`, and UI startup) may check PyPI once per day for `switchboard-local` updates; disable with `SWITCHBOARD_UPDATE_CHECK=off` or `preferences.update_check_enabled: false`.

Switchboard deliberately does **not** resell API access, scrape web UIs, or
bypass provider limits — subscription CLIs are invoked exactly as the
authenticated user could invoke them, in read-only sandbox modes. See
SECURITY.md and docs/privacy.md.

 What's inside

- **Deterministic router** — keyword rules; unknown prompts default local-first.
- **Learned router / tool dispatcher / sensitivity escalator** — tiny softmax classifiers over a locally-computed embedding (~50 ms, pure-Python inference), each retrainable in seconds from your own thumbs-down corrections behind golden-accuracy gates. They fail closed to the deterministic path.
- **Tools** — time/date with timezones, safe abstract-syntax-tree calculator, unit conversion, keyless live stock quotes & news.
- **Compression** — structure-aware, deterministic, dependency-free; preserves task header, code blocks, tracebacks, and grounded facts.
- **Semantic memory** — `nomic-embed-text` embeddings, cosine retrieval, local memory commands, and SQLite text-search fallback for direct search.
- **Evaluation** — mock evals (CI), real-backend smoke suite, 100-case quality benchmark, adversarial tester/developer dogfooding loop.

## Configuration

In source checkouts, editable settings live in `config/personal.yaml`; wheels
also ship package defaults, and `switchboard init` can copy starter config into
your user config directory. See `config/personal.example.yaml`. Highlights:
The example below shows safe dependency-free defaults; source checkouts may opt into
`compression_engine: "headroom"` and a Claude model override when those tools are
installed and desired.

```yaml
preferences:
  router_mode: "learned"      # rules | llm | hybrid | learned
  private_mode: true          # block sensitive prompts from non-local backends
  allow_cloud: false
  compression_enabled: true
  compression_engine: "heuristic"  # heuristic | headroom
  compression_threshold_tokens: 1000
  embedding_model: "nomic-embed-text"
  semantic_memory_enabled: true
  semantic_memory_top_k: 3
  escalation_enabled: false
  escalation_confidence_threshold: 0.55
  claude_code_model: null  # optional alias/full model name, e.g. "claude-opus-4-8"
  router_llm_model: "llama3.2:3b"
  claude_code_web_search: true  # allow Claude Code WebSearch for live-data fallback
  finance_provider: "yahoo"
  news_provider: "google_news_rss"
  store_feedback_examples: false
  feedback_auto_retrain: true
quota:
  codex_calls_per_5h: null      # optional local soft budget; null = unlimited
  claude_calls_per_week: null   # optional local soft budget; null = unlimited
```

Provider API keys are referenced **by environment-variable name** (e.g.
`OPENAI_API_KEY`), never inline. See docs/overrides.md.

## The paper

Switchboard is described in a preprint — *"Privacy-Aware Hybrid Routing Across
Heterogeneous AI Agents."* The manuscript, the multi-run
benchmark harness, the statistical-aggregation and figure scripts, and the
per-case records are archived together as a reproduction bundle on Zenodo:
10.5281/zenodo.20836918.

This repository ships only the software. It deliberately does not carry the
paper's experiment-running or figure-generation tooling — that lives with the
archival record so the code stays focused on the router itself.

## Development

```bash
make install     # .venv + editable install with dev extras
make check       # ruff + mypy + the full test suite
```

See CONTRIBUTING.md. Issues and PRs welcome — please preserve
the privacy invariant described there.

## Citing Switchboard

A preprint is available on Zenodo with a citable DOI —
10.5281/zenodo.20836918. See
CITATION.cff for machine-readable metadata.

> V. Gupta, "Switchboard: Privacy-Aware Hybrid Routing Across Heterogeneous AI
> Agents," Zenodo, 2026, doi:10.5281/zenodo.20836918.

## License

MIT © 2026 Vinay Gupta

# ravachol/kew

## 关联链接

- http://127.0.0.1:8080/ui
- https://github.com/aivinay/switchboard@v0.6.2
- https://ollama.com/download

## 导航

- 项目页：[[10-项目/github.com_009d7b33]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
