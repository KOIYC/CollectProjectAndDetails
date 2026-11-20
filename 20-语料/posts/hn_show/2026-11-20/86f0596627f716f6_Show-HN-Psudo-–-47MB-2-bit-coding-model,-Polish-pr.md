---
type: "corpus"
item_id: "86f0596627f716f6"
title: "Show HN: Psudo – 47MB 2-bit coding model, Polish-prefix IR, and Rust transpiler"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50559718"
project_url: "https://github.com/steveSujo/psudo"
author: "someProgramer"
published_at: "2026-11-19T13:17:56Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_someProgramer
  - story_50559718
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Psudo – 47MB 2-bit coding model, Polish-prefix IR, and Rust transpiler

> [!info] 一句话导读
> Toy Python-indented language + 100M 1.58-bit TQ2_0 local LLM engine that synthesizes token-compressed pIR code and lowers it to safe Rust.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50559718>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：someProgramer　|　发布：2026-11-19T13:17:56Z
> 项目链接：<https://github.com/steveSujo/psudo>
> 采集：2026-11-20T09:45:52+08:00　|　id：`86f0596627f716f6`

## 正文

# steveSujo/psudo

Toy Python-indented language + 100M 1.58-bit TQ2_0 local LLM engine that synthesizes token-compressed pIR code and lowers it to safe Rust.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-16T10:57:15Z

## Languages

- Batchfile
- Lean
- Parrot
- Python
- Rust
- Shell

## Top Contributors

- steveSujo (19 contributions)

---

## README

# psudo

A token-compressed DSL (`.psudo`), a Polish-prefix intermediate representation (`pIR`), a borrow-checked safe Rust transpiler, and a pure-Rust 2-bit ternary (`TQ2_0`) inference engine—built to run local code synthesis inside a **4 GB VRAM** budget.

```mermaid
flowchart LR
    A[".psudo DSL"] --> B["pIR (Polish-prefix IR)"]
    B --> C["pseudo-engine (100M TQ2_0 + PDA Mask)"]
    C --> D["Borrow Checker & Sandbox"]
    D --> E["Safe Rust (0 unwrap)"]
```

| Metric | Value |
| --- | --- |
| Primary Model Footprint | `47.0 MB` (`100.7M` params, `TQ2_0` 2-bit ternary weights) |
| Context Compression | `45–60%` fewer tokens than surface syntax via `pIR` |
| Syntax Error Rate | `0%` at decode time via Pushdown Automaton (`PirPdaConstraint`) masking |
| Runtime Dependencies | Zero (pure Rust, `memmap2`, no CUDA/C++ toolchains required) |
| Training Dataset | `~7,800` borrow-checked & sandbox-verified trajectories |

Both quantized `.gguf` checkpoints (`47.0 MB` and `23.2 MB`) ship right in this repo, and everything compiles with plain `cargo` (zero C++, Python, or CUDA dependencies):

```bash
git clone https://github.com/steveSujo/psudo.git
cd psudo
cargo build --release && ./target/release/psudo demo
```

---

## Why I built this

I wanted to run and train coding models on my own machine—not rent bigger GPUs or burn cloud token quotas on every loop and helper function.

My laptop has an **NVIDIA GTX 1660 Ti with 4 GB of VRAM** and limited RAM, so running frontier models locally is out of the question. Instead of seeing those limits as the problem, I treated them as **creative constraints**: how can I make the best out of this? Finding a creative solution is way more fun than throwing raw power at the problem or trying to vertically scale my PC.

Running a small, limited model with **2-bit precision (`TQ2_0`)** shrinks the VRAM footprint enough to live comfortably alongside an IDE and compiler—and exploring how far that tiny model can push raw coding power became the whole point:

1. **A tiny surface language (`.psudo`):** Python-indented, minimal punctuation, almost zero boilerplate tokens.
2. **Lowering to safe Rust (`pseudo-transpiler`):** A toy language has no ecosystem. To build real binaries, verified and borrow-checked `.psudo` lowers into safe Rust (`0` `.unwrap()` or `.expect()` calls) and compiles with `cargo`.
3. **The Cactus & Needle spark:** Seeing Cactus and Needle—2-bit on-device models (`29M–121M` params in `8–29 MB`) beating much larger models on constrained tool calls—showed what tight constraints can do.
4. **"What if?":** *What if I trained a ~100M 2-bit ternary model (`TQ2_0`) whose only job is writing atomic `.psudo` function bodies locally, while I (or a frontier LLM) stay at the orchestrator level?*

---

## How it works (`pIR`, PDA Masking & 2-bit `TQ2_0`)

Asking a `100M` model to emit verbose surface syntax wastes half its context window on keywords and whitespace. Instead, the model emits **pIR (Pseudo Intermediate Representation)**—a Polish-prefix S-expression format where `fn` is `f`, `let` is `v`, `return` is `r`, `if` is `?`, and `while` is `w`:

```text
// Surface .psudo (what humans read)
fn clamp_val(val, lo, hi)
    if val < lo
        return lo
    if val > hi
        return hi
    return val

// Wire pIR (what the 100M model emits)
f clamp_val (val lo hi) [
  ? (< val lo) [ r lo ]
  ? (> val hi) [ r hi ]
  r val
]
```

That trade buys two things:
- **45–60% fewer tokens** per function body.
- **0% syntax errors at decode time:** `pseudo-engine` runs a pushdown automaton (`PirPdaConstraint`) over the `8,192`-token BPE vocab and masks out invalid tokens *before* sampling.

### Models (Included in Repo)

- **`pseudo-100m-tq2_0.gguf` (`100.7M` params, `47.0 MB`) — Primary:**
 `d_model = 768`, `14` layers, `12` heads (`4` KV heads), `FFN = 2048`, `vocab = 8,192`, `max_seq_len = 512`, `TQ2_0` ternary weights (`{-1, 0, 1}`). Auto-discovered by `psudo synth` for ~15-line atomic stubs (guards, math, loops, JSON/KV helpers).
- **`pseudo-33m-tq2_0.gguf` (`33.6M` params, `23.2 MB`) — Embedded Fallback:**
 `d_model = 512`, `8` layers, `8` heads (`4` KV heads). Baked into the `psudo` binary for offline smoke tests if no external `.gguf` is present.

Both were distilled from `Qwen/Qwen2.5-Coder-7B-Instruct-AWQ` plus a synthetic generator—every sample had to pass type checking, borrow checking, and sandbox execution in headless `psudo` before being compiled to canonical `pIR` (`~7,800` verified trajectories across ` `, ` ` 1-shot auto-heal, ` `, and ` `).

---

## Try the Examples

Requires Rust `1.75+`. Build both binaries (`psudo` and `pseudo-engine`):

```bash
cargo build --release
```

`examples/` ships three pre-built workspace capsules (`psudo.bin`) with mock sandbox data in `.pseudo/sandbox/`:

```bash
# 1. JSON Server Log Incident Filter
./target/release/psudo check examples/log-incident-filter/psudo.bin --all-modules
./target/release/psudo build examples/log-incident-filter/psudo.bin --run

# 2. IoT Temperature Sensor Alert Monitor
./target/release/psudo build examples/sensor-alert-monitor/psudo.bin --run

# 3. API Tiered Quota & Billing Calculator
./target/release/psudo build examples/quota-fee-calculator/psudo.bin --run
```

---

## Orchestrator Workflow

Your code lives inside a single signed capsule file (`psudo.bin`). You (or an outer coding agent) declare signatures, stubs, and tests; `psudo synth` fills in the bodies locally.

```bash
# 1. Initialize a workspace (templates: blank, log, sensor, quota)
psudo init my-app --template blank --with-docs && cd my-app

# 2. Declare an atomic @stub function (defaults to ./psudo.bin when omitted)
psudo vfs stub compute_fee units rate free_tier \
  --directive "if units <= free_tier return 0, else return (units - free_tier) * rate"

# 3. Synthesize with auto-discovered 100M GGUF (auto-starts persistent --daemon)
psudo synth --write

# 4. Inspect call-graph DAG and behavioral contract (without dumping raw code)
psudo dag --format mermaid
psudo contract

# 5. Add an in-capsule test and wire the entrypoint
psudo vfs test test_fee --call "compute_fee(15, 2, 10)" --expect "10"
psudo vfs wire --entry main_task --call "print(compute_fee(15, 2, 10))" --return "0"

# 6. Borrow-check, test, run directly, or compile to native Rust
psudo check -a
psudo test
psudo run --call "compute_fee(15, 2, 10)"
psudo build --run
```

### Why raw `.psudo` is hidden behind a key
When I tested outer LLM agents with this CLI, they kept peeking at the `.psudo` source and hand-writing functions instead of using `psudo synth`. So `psudo vfs show --all` and `psudo synth --print` stay locked unless you pass the key:
- **Question:** *"What jumped over the lazy dog?"*
- **Key:** `--reveal-code "the slow pink elephant"`

For agent harnesses, `psudo-orchestrator` and `psudo mcp` (stdio JSON-RPC) are included. Run `psudo --help`, `psudo docs`, or `psudo -s` for the full reference.

---

## Rough Edges & Honest Expectations

**This is not a polished product.** It is an exploration of an idea with plenty of sharp corners:

1. **Keep stubs atomic:** A `100M` 2-bit model cannot write an HTTP server in one shot. Give it small, single-purpose functions (guards, clamping, arithmetic, simple loops, KV/JSON helpers).
2. **Grammar masking != semantic intelligence:** The PDA mask guarantees valid `pIR` brackets and ops, so an out-of-distribution prompt still produces valid syntax—just logically wrong fallback code.
3. **Strict 4-space indentation & `//` comments:** 2-space indents and tabs fail with `E002`; `#` comments fail with `E001`.
4. **Sealed `psudo.bin` feels weird at first:** Keeping source inside a masked binary capsule is deliberately awkward for manual editing—it exists to keep outer agents in the orchestrator seat.
5. **Bimodal CPU speeds:** `pseudo-engine --benchmark` swings between fast runs when `memmap2` pages are hot and slow runs on cold pages or OS background scheduling.
6. **Windows-first mileage:** Most testing happened on Windows 11. Rebuilding while `psudo.exe` is running hits Windows file locks, and Linux/macOS paths have less mileage.

Expect bugs! I'll keep tweaking the language and the tiny model as I experiment.

---

## Repository Layout

| Path | Description |
|---|---|
| `pseudo-lang/` | `.psudo` lexer, parser, borrow checker, `psudo.bin` VFS capsule, contract generator, and `psudo` CLI |
| `pseudo-engine/` | Pure-Rust zero-copy GGUF parser, `TQ2_0` ternary kernels, 2-tier INT8 KV cache, PDA sampler, and `--daemon` |
| `pseudo-transpiler/` | Deterministic IR lowering between `.psudo` and safe, zero-`unwrap()` Rust |
| `examples/` | Pre-built capsules (`log-incident-filter`, `sensor-alert-monitor`, `quota-fee-calculator`) |
| `templates/` | Source `.psudo` templates and `.pseudo/sandbox/` fixtures for `psudo init` |
| `.agents/skills/` | `psudo-orchestrator` skill for LLM harnesses |

# dhruv2295/Retriever

## 关联链接

- https://github.com/steveSujo/psudo.git

## 导航

- 项目页：[[10-项目/github.com_0b2d7514]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
