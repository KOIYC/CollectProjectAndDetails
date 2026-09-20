---
type: "corpus"
item_id: "03c09d47cfd86c0c"
title: "Show HN: Quokka – a self-hosting, deterministic programming language"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49755226"
project_url: "https://quokka.space/"
author: "CFBL"
published_at: "2026-09-18T14:50:00Z"
captured_at: "2026-09-20T14:02:21+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_CFBL
  - story_49755226
  - show_hn
metrics: {"points": 5, "comments": 2, "engagement_velocity": 5}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Quokka – a self-hosting, deterministic programming language

> [!info] 一句话导读
> Author: Quokka Language Contributors

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49755226>
> 指标：点赞=5 · 评论=2 · engagement_velocity=5
> 作者：CFBL　|　发布：2026-09-18T14:50:00Z
> 项目链接：<https://quokka.space/>
> 采集：2026-09-20T14:02:21+08:00　|　id：`03c09d47cfd86c0c`

## 正文

Author: Quokka Language Contributors

Quokka — A Deterministic, Self-Hosted Programming Language for AI Workflows

# A predictable language for modern workflows.

v0.1.0 · MIT Licensed · Windows

Quokka is a strictly self-hosted programming language designed for clarity and reliability. It features deterministic programming language design, Result and Option error handling, and seamless LoRA fine-tuning via Unsloth out of the box.

```shell
$ quokka run hello.qka
Hello, World!
```

### Self-hosted by design.

Our entire toolchain is built in Quokka. We use a multi-stage bootstrap process to cryptographically verify correctness.

```qka
// The Quokka compiler is written in Quokka.
// Run our built-in check to verify the build.
$ quokka check-self
```

### Predictable errors.

We do not use hidden control flow for exceptions. Handle failures explicitly with Result and Option types.

```qka
let config = fs.read("settings.qka")?

// Errors are returned as values.
// No unexpected exceptions thrown at runtime.
```

### Explicit mutability.

Variables are immutable by default. State changes require explicit opt-in, making your code easier to trace.

```qka
let version = "1.0"      // immutable by default
let mut retries = 0      // explicitly mutable

retries = retries + 1
```

### Simple toolchain.

Our installer automatically configures your PATH, file associations, and editor setup in one step.

```shell
$ Quokka-Setup.exe
Installing Quokka v0.1.0...
Configuring PATH...                done
Registering .qka file extension... done
Installing VS Code extension...     done

Quokka is ready. Open a new terminal and run: quokka
```

## Verifiable builds.

Quokka boots from a small C host (src/bootstrap, roughly 2,150 lines: a lexer, parser, and tree-walking interpreter) just once — Stage 0. Stage 0's only job is to run the canonical Quokka interpreter, which is itself written entirely in Quokka. From there, Quokka compiles Quokka.

Run `quokka check-self` and it re-bootstraps the interpreter through multiple stages, then compares cryptographic hashes of the AST and the output at each stage. If they match, self-hosting isn't a claim on this page — it's a number you can verify on your own machine.

Illustrative output — run `quokka check-self` yourself to see your machine's actual hashes.

## Joey: ML integration without the bloat.

Joey is a standard library extension that interfaces cleanly with Python and PyTorch via a strictly typed JSON IPC boundary, keeping the core language minimal.

```qka
import joey

let mut pipeline = joey.pipeline()
pipeline.load_model("meta-llama/Llama-3-8B", "4bit")
pipeline.train("quokka_dataset", 512)

let result = pipeline.run()

match result {
    Ok(status) => println("Training complete! " ++ status),
    Err(e)     => println("Training failed: " ++ e),
}
```

Quokka code JSON IPC manifest Python + Unsloth process Result back to Quokka

Joey's process-isolation architecture: Quokka code writes a JSON manifest, spawns an isolated Python and Unsloth process for training, and reads the result back.

Today: Joey orchestrates fine-tuning through this Python/Unsloth bridge, including CUDA-accelerated training. AMD/ROCm is untested. A fully native Joey runtime — removing the Python process entirely for supported operations — is in progress; see the Roadmap below.

### Core language and compiler

- C bootstrap host (Stage 0)
- Self-hosted lexer, parser, AST, and evaluator, written in Quokka
- `quokka check-self` verifier
- Result / Option error handling, `match`, and the `?` operator
- Immutable-by-default bindings (`let` / `let mut` / `shadow`)
- Joey ML extension via Python/Unsloth IPC, with CUDA support
- Windows installer and VS Code syntax highlighting

### Native execution

- Native Joey runtime, removing the Python process hop for supported operations
- Expanded standard library

### Broader reach

- AMD / ROCm support
- macOS and Linux builds

Quokka was built solo, from a small C bootstrap host up through a fully self-hosted compiler written in the language itself. It's open source under the MIT License starting at v0.1.0 — read the source, run the verifier yourself, and see exactly how it works.

If you'd like to contribute, start with the Contributing Guide.

### Download

Grab Quokka-Setup.exe from the Releases page.

2

### Install

Run the installer. It configures your PATH, file associations, and VS Code extension automatically.

3

### Run

`quokka run hello.qk`

### Hello, Quokka

Install Quokka and run your first script in five minutes.

### Errors without exceptions

Walk through Result, Option, match, and the ? operator by building a config file reader that handles failure explicitly.

### Fine-tune Llama-3 with Joey

Follow the full Joey pipeline end to end — from `joey.pipeline()` to a trained LoRA adapter — and see exactly what happens under the hood.

# RAW — Servers for AI. 100× cheaper than AWS.

## 评论（2/2）

> **piuvas** · 2026-09-18T17:25:05.000Z　
> it feels like it's made me someone who doesn't even know what it's purpose is.

---

> **veexx103** · 2026-09-19T13:26:56.000Z　
> I find that many languages designed by enthusiasts are better than mainstream ones,yet we are stuck suffering with the mainstream languages.

## 导航

- 项目页：[[10-项目/quokka.space_7a5f3f39]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
