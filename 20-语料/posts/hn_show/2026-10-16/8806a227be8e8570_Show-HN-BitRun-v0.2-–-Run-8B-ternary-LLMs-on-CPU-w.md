---
type: "corpus"
item_id: "8806a227be8e8570"
title: "Show HN: BitRun v0.2 – Run 8B ternary LLMs on CPU with live wattage telemetry"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50106895"
project_url: "https://github.com/IshekKhal/bitrun"
author: "ishekofficial"
published_at: "2026-10-15T17:15:08Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_ishekofficial
  - story_50106895
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: BitRun v0.2 – Run 8B ternary LLMs on CPU with live wattage telemetry

> [!info] 一句话导读
> Single-binary runner and model manager for 1-bit / 1.58-bit ternary LLMs (Microsoft BitNet b1.58) on CPU (macOS, Windows, Linux)

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50106895>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ishekofficial　|　发布：2026-10-15T17:15:08Z
> 项目链接：<https://github.com/IshekKhal/bitrun>
> 采集：2026-10-16T09:35:18+08:00　|　id：`8806a227be8e8570`

## 正文

# IshekKhal/bitrun

Single-binary runner and model manager for 1-bit / 1.58-bit ternary LLMs (Microsoft BitNet b1.58) on CPU (macOS, Windows, Linux)

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-10-12T06:12:05Z

## Languages

- Batchfile
- Go
- PowerShell
- Shell

## Topics

- 1-bit
- arm-neon
- avx2
- bitnet
- cli
- cpu-inference
- llm
- ternary
- zero-compile

## Top Contributors

- IshekKhal (9 contributions)

---

## README

# BitRun ⚡️

> **Zero-compile, single-binary runner and model manager for Microsoft BitNet b1.58 and 1.58-bit ternary LLMs on macOS, Windows, and Linux CPUs.**

License
Release
Architecture

---

## Why BitRun?

Microsoft's **BitNet b1.58** proved that ternary (1-bit / 1.58-bit) models can run at extreme speeds on commodity CPUs with 70–80% lower energy consumption by eliminating floating-point multiplications.

Ternary models are engineered for **local CPU inference, battery-powered laptops, edge devices, and embedded tasks** where running heavy FP16 or INT4 models drains battery or requires dedicated GPUs.

However, testing `BitNet.cpp` today requires:
* Cloning recursive submodules and managing C++ compilers, CMake, and Python toolchains.
* Manually tuning CPU vector instruction flags (AVX2, AVX-512, ARM NEON).
* Dealing with 5–10 GB heavy Docker images that defeat the purpose of low-power computing.

**BitRun solves this by packaging the native inference engine into a single binary with a familiar, zero-friction developer experience:**

```bash
# 1. Pull a 1-bit model directly from Hugging Face
bitrun pull bitnet-2b

# 2. Run an interactive chat session on your CPU
bitrun run bitnet-2b

# 3. Or spin up a local OpenAI-compatible REST server
bitrun serve bitnet-2b
```

---

## Performance Benchmarks

### 1. Apple Silicon (M4 Pro CPU, 12 Cores, Pure CPU SIMD `-ngl 0`)
| Model | Size | Prompt Speed | Generation Speed | Memory (RAM) | GPU Utilization |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Falcon3 1B Instruct** (`falcon3-1b`) | **1.30 GB** | **137.5 t/s** | **98.6 t/s** | **~1.9 GB** | **0% (Pure CPU SIMD)** |
| **BitNet b1.58 2.4B** (`bitnet-2b`) | **1.13 GB** | **60.1 t/s** | **39.8 t/s** | **~1.8 GB** | **0% (Pure CPU SIMD)** |
| **BitNet 70M** (`bitnet-70m`) | **79 MB** | **8,758 t/s** | **1,355 t/s** | **< 150 MB** | **0% (Pure CPU SIMD)** |

### 2. Windows x86_64 (Intel Core i5-12600K CPU, 16 Threads, AVX2 SIMD)
| Model | Size | Prompt Speed | Generation Speed | Memory (RAM) | GPU Utilization |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Falcon3 1B Instruct** (`falcon3-1b`) | **1.30 GB** | **93–210 t/s** | **40–45 t/s** | **~1.9 GB** | **0% (Pure CPU AVX2)** |
| **BitNet 70M** (`bitnet-70m`) | **79 MB** | **2,419 t/s** | **492 t/s** | **< 150 MB** | **0% (Pure CPU AVX2)** |

### 3. Linux x86_64 (WSL2 / Ubuntu, 4 Cores, AVX2 SIMD)
| Model | Size | Prompt Speed | Generation Speed | Memory (RAM) | GPU Utilization |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Falcon3 1B Instruct** (`falcon3-1b`) | **1.30 GB** | **~130 ms TTFT** | **40–45 t/s** | **~1.9 GB** | **0% (Pure CPU AVX2)** |
| **BitNet 70M** (`bitnet-70m`) | **79 MB** | **< 25 ms TTFT** | **Fast CPU SIMD** | **< 150 MB** | **0% (Pure CPU AVX2)** |

---

## Quickstart

### 1. One-Line Installation

**macOS (Apple Silicon) & Linux (x86_64)**:
```bash
curl -fsSL https://raw.githubusercontent.com/IshekKhal/bitrun/main/install.sh | sh
```

**Windows (PowerShell)**:
```powershell
irm https://raw.githubusercontent.com/IshekKhal/bitrun/main/install.ps1 | iex
```

### 2. Available Commands

```bash
# Display CPU topology and vector instruction support
bitrun hardware

# List all downloaded models and custom personas
bitrun list

# Download a model with dynamic progress and resume support
bitrun pull falcon3-1b

# Run interactive terminal chat
bitrun run falcon3-1b

# Run a one-shot prompt directly
bitrun run falcon3-1b "Explain RAII in C++"

# Create a custom model persona from a Modelfile
bitrun create gopher -f Modelfile

# Serve OpenAI-compatible REST API on port 11435
bitrun serve falcon3-1b
```

---

## Modelfiles & Custom Personas

Create custom system personas and parameter presets using standard Modelfiles:

```dockerfile
# Modelfile
FROM falcon3-1b
SYSTEM You are an expert Go systems engineer. Write dense, production-grade code.
PARAMETER temperature 0.2
PARAMETER context_size 4096
```

Build and run your custom persona:

```bash
# Create custom persona
bitrun create gopher -f Modelfile

# Chat with your persona
bitrun run gopher

# Or run one-shot completions
bitrun run gopher "Write a ring buffer implementation"
```

---

## OpenAI-Compatible API

When running `bitrun serve`, you can point any OpenAI-compatible tool (Cursor, Continue.dev, Open WebUI, LangChain, Python SDK) to `http://localhost:11435/v1`:

```bash
curl -s http://127.0.0.1:11435/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Bitnet-M7-70m",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ],
    "temperature": 0.7
  }'
```

---

## Supported Models Catalog

| Model Tag | Parameters | Format | Size | Description |
| :--- | :--- | :--- | :--- | :--- |
| `bitnet-70m` | 70M | `Q8_0` / Ternary | ~79 MB | Ultra-compact smoke test model |
| `bitnet-2b` | 2.4B | `i2_s` Ternary | ~1.2 GB | Official Microsoft BitNet b1.58 2B |
| `falcon3-1b` | 1B | `i2_s` Ternary | ~700 MB | TII Falcon3 1B Instruct 1.58-bit |
| `falcon3-3b` | 3B | `i2_s` Ternary | ~1.8 GB | TII Falcon3 3B Instruct 1.58-bit |
| `llama3-8b` | 8B | `i2_s` Ternary | ~2.4 GB | 1-Bit LLM Llama3 8B 1.58-bit |

---

## Architecture Overview

BitRun uses a **decoupled supervisor-engine design**:
* **Supervisor Layer (Go)**: Cross-platform CLI, CPU topology detection, content-addressed asset store (`~/.bitrun`), and HTTP REST supervisor.
* **Engine Tier (Native C++)**: Statically compiled binary utilizing ARM NEON with dot-product (`ARM_FEATURE_DOTPROD`) and x86 AVX-512 kernels. Zero CGO dependencies, ensuring total crash isolation.

---

## Acknowledgements & Open Source Credits

BitRun stands on the shoulders of giants:
* **llama.cpp** by Georgi Gerganov and the open-source community (MIT License) — The pioneering CPU inference architecture and GGUF specification.
* **BitNet.cpp** by Microsoft Research (MIT License) — Groundbreaking 1-bit and 1.58-bit ternary matrix kernels.

BitRun contributes back to upstream:
* **microsoft/BitNet#642** — ARM64 2B batch stride, FFN activation, and LLaMA-3 tokenizer inference fix.
* **microsoft/BitNet#644** — Native MSVC compiler support and CLI build tools on Windows.

BitRun wraps these core engines with cross-platform zero-compile distribution, model management, Modelfile custom personas, and an OpenAI-compatible REST server.

---

## License

MIT License. See LICENSE for details.

# Hooked — Boondoggle Studio

## 关联链接

- http://127.0.0.1:11435/v1/chat/completions
- http://localhost:11435/v1`:
- https://raw.githubusercontent.com/IshekKhal/bitrun/main/install.ps1
- https://raw.githubusercontent.com/IshekKhal/bitrun/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_39ff1a2d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
