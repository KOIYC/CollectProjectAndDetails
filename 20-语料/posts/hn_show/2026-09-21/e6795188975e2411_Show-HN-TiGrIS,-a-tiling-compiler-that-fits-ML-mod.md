---
type: "corpus"
item_id: "e6795188975e2411"
title: "Show HN: TiGrIS, a tiling compiler that fits ML models onto embedded devices"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47945067"
project_url: "https://github.com/raws-labs/tigris"
author: "asteinh"
published_at: "2026-04-29T07:11:03Z"
captured_at: "2026-09-21T02:52:40+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_asteinh
  - story_47945067
  - show_hn
metrics: {"points": 20, "comments": 0, "engagement_velocity": 20}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: TiGrIS, a tiling compiler that fits ML models onto embedded devices

> [!info] 一句话导读
> Ahead-of-time compiler that tiles ML models to fit embedded devices with hard memory budgets.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47945067>
> 指标：点赞=20 · 评论=0 · engagement_velocity=20
> 作者：asteinh　|　发布：2026-04-29T07:11:03Z
> 项目链接：<https://github.com/raws-labs/tigris>
> 采集：2026-09-21T02:52:40+08:00　|　id：`e6795188975e2411`

## 正文

# raws-labs/tigris

Ahead-of-time compiler that tiles ML models to fit embedded devices with hard memory budgets.

- Stars: 6
- Forks: 0
- Watchers: 6
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://tigris-ml.dev
- Default branch: main
- Created: 2026-02-11T06:21:17Z

## Languages

- Python

## Topics

- compiler
- cortex-m
- edge-ai
- embedded-ml
- inference
- model-compression
- onnx
- quantization
- tiling
- tinyml

## Top Contributors

- asteinh (23 contributions)

---

## README

# TiGrIS

License
PyPI
Docs

**Tiled Graph Inference Scheduler.** An ahead-of-time compiler that tiles ML models to fit embedded devices with hard memory budgets.

Give it an ONNX model and a memory budget. It partitions the compute graph into stages, tiles spatial operations, and emits a flat binary plan that the tigris-runtime executes with zero dynamic allocation.

## The problem

On an embedded device with a few hundred KB of SRAM, most interesting models simply don't fit. The usual answer is to shrink the model: quantize harder, prune, pick a smaller architecture, and hope the accuracy hit is acceptable.

TiGrIS takes the other approach. It keeps the model you trained and rearranges the *computation* so that only a small working set lives in SRAM at any moment. Weights and intermediate spills go to flash or PSRAM. What comes out is a binary plan that the runtime executes as a flat sequence of kernel calls, with no interpreter, no tensor allocator, and no dynamic memory at all.

## Quick start

```bash
pip install tigris-ml

# Will this model fit in 256KB SRAM + 16MB flash?
tigris analyze mobilenetv2.onnx -m 256K -f 16M
```

```text
╭──────────────────────── TiGrIS - mobilenetv2 ────────────────────────╮
│ Operators            65                                              │
│ Peak memory (naive)  4.59 MiB                                        │
│ Largest tensor       1x96x112x112 (4.59 MiB)                         │
╰──────────────────────────────────────────────────────────────────────╯
╭──────────────────────────────── SRAM ────────────────────────────────╮
│ Budget              256.00 KiB                                       │
│ Scheduled peak      254.62 KiB (5.4% of naive peak)                  │
│ Stages              42                                               │
│ Need tiling         31 of 42 stages                                  │
╰────────────────  PASS - tiling resolves all stages  ─────────────────╯
```

The naive peak is 4.59 MiB. TiGrIS schedules it into 256 KiB through temporal partitioning and spatial tiling. `analyze` runs on your laptop; no hardware required.

## From ONNX to embedded

Three steps take a model from ONNX to a C file you can drop into your firmware project:

```bash
# 1. Analyze feasibility against a memory budget
tigris analyze model.onnx -m 256K -f 16M

# 2. Compile to a binary plan (weights read-in-place from flash)
tigris compile model.onnx -m 256K -f 16M --xip -o model.tgrs

# 3. Generate a backend-specific C harness for your target
tigris codegen model.tgrs --backend esp-nn -o model.c
```

The `.tgrs` plan is target-agnostic: it is the same file whether you run it on an ESP32, a Cortex-M, or a POSIX host for testing. The choice of kernel backend happens at `codegen` time and decides which kernel library the generated C calls into.

Several kernel backends are available (portable C99, ESP32 family, Cortex-M family); see tigris-runtime for the current list. Switching between them is a `--backend` flag, not a rewrite.

## What you get

`tigris compile` writes a single `.tgrs` file that contains the operator schedule, tile parameters, quantization tables, and the weights. This file goes on flash at deployment time.

`tigris codegen` produces a small C harness that locates the plan on flash at runtime and hands it to the runtime:

- declarations for the input/output buffers and the arena
- a target entry point (`app_main()` for ESP-IDF, `main()` for POSIX/Cortex-M examples) that sets up memory and calls the runtime
- backend-specific glue for finding the plan: partition mmap on ESP-IDF, an `extern` flash symbol on Cortex-M, a file path on POSIX

Link the harness against tigris-runtime and your chosen kernel library, flash the `.tgrs` alongside the firmware, and you have a working inference binary.

### Embedding in an existing application

The default `--format app` emits that standalone example program. Use
`--format core` when your firmware already owns its entry point, plan placement,
arenas, input source, or observability:

```bash
tigris codegen model.tgrs --backend cmsis-nn --format core \
  -o generated/tigris_codegen_core.c \
  --header generated/tigris_codegen_core.h \
  --name model_codegen
```

Core output is backend-specific but platform-neutral. It produces a C source and
header that load the plan, reset runtime memory, prepare the selected backend,
and run the generated dispatcher. Initialize the core once, then reset it before
each subsequent inference. The embedding application supplies the plan
bytes, arena buffers, and an optional input-initialization callback. If
`--header` is omitted, codegen writes a sibling `.h` file next to `--output`.
`--name` prefixes the public C symbols, so multiple generated cores can coexist
in one firmware. The header also exports the model's tensor-table capacity,
plan budget, and compressed-weight reserve for static allocation decisions.
This is suitable for bare-metal firmware, RTOS applications, and custom
instrumentation without introducing a hardware-specific codegen target.

## Further reading

- Getting started: installation, first compile, deploying to ESP32
- Introducing TiGrIS: design, benchmarks, how tiling works
- CLI reference: every flag, every subcommand

## Maintainer

TiGrIS is maintained by RAWS Labs. For applied embedded-ML engineering or collaboration, see raws.at.

## Development

```bash
git clone https://github.com/raws-labs/tigris
cd tigris
pip install -e ".[dev]"
pytest
```

## 关联链接

- https://tigris-ml.dev

## 导航

- 项目页：[[10-项目/github.com_0c101e88]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
