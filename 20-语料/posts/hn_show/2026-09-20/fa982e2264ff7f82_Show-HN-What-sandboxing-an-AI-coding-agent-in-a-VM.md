---
type: "corpus"
item_id: "fa982e2264ff7f82"
title: "Show HN: What sandboxing an AI coding agent in a VM costs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49740053"
project_url: "https://veloworkspaces.com/blog/vm-sandboxing-cost"
author: "michael_luog"
published_at: "2026-09-17T12:57:34Z"
captured_at: "2026-09-20T09:36:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_michael_luog
  - story_49740053
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: What sandboxing an AI coding agent in a VM costs

> [!info] 一句话导读
> What Sandboxing an AI Coding Agent in a VM Actually Costs on Apple Silicon — Velo Workspaces

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49740053>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：michael_luog　|　发布：2026-09-17T12:57:34Z
> 项目链接：<https://veloworkspaces.com/blog/vm-sandboxing-cost>
> 采集：2026-09-20T09:36:52+08:00　|　id：`fa982e2264ff7f82`

## 正文

What Sandboxing an AI Coding Agent in a VM Actually Costs on Apple Silicon — Velo Workspaces

# What Sandboxing an AI Coding Agent in a VM Actually Costs on Apple Silicon

I benchmarked the same sandboxing architecture against two different inference engines and got two different answers about what it costs under load. Both are real. Here's why they disagree, and why I'm showing you both instead of picking the one that sounds better.

## The problem

Most people running an AI coding agent locally give it a `subprocess` or `exec()` call with full access to their filesystem, network, and credentials. Docker's own engineering blog has documented real incidents from exactly this. Indirect prompt injection makes it worse — a hostile instruction hidden in a file the agent reads can trigger commands with your full permissions, not just the ones you typed.

The "correct" fix is to run the agent in a VM. On Apple Silicon this runs into a real wall: `Virtualization.framework` doesn't expose the host GPU to a Linux guest. Confirmed directly by Apple's own container team when people asked for it. A Linux guest gets `virtio-gpu`, a paravirtualized 2D framebuffer with no path to the host's Metal GPU. Run a 7B model inside the VM and it's dramatically slower than the same model on the host.

So on Apple Silicon, "safe" (inside a VM) and "fast" (on the GPU) pull in opposite directions — unless you stop treating "run the agent" and "run the model" as the same problem.

## The fix: split agent from model

The dangerous part (executing LLM-generated code) and the expensive part (running the model) don't have to live in the same place. Model stays on the host, served by Ollama or MLX. Agent runs in the VM. A thin proxy (`socat`) inside the guest forwards `127.0.0.1: ` across a VirtIO-vsock channel — not a virtual NIC, a direct hypervisor-memory channel — to a small Swift listener on the host, which relays to whichever engine is running. From inside the VM you set `OPENAI_API_BASE` to `http://127.0.0.1: /v1` and every OpenAI-compatible tool just works, no code changes, no awareness a VM boundary exists.

That's the whole mechanism. The question that actually matters is what it costs you.

## Benchmark 1: MLX, single request — near-zero

Mac mini (Apple M4, 10 cores, 16GB RAM, macOS 26.6.2). Guest: Ubuntu Server 26.04 LTS, 4 vCPU, 4GB RAM. Model: `mlx-community/Qwen2.5-Coder-7B-Instruct-4bit` via `mlx_lm.server`. 5-run average, host vs. through the vsock bridge:

That's inside run-to-run noise. At single-request scale the vsock hop costs nothing measurable.

### Under load, and in a real agentic loop — small, real, consistent

8 parallel clients, averaged across 4 runs: the VM trails by ~5% on total wall time. Same direction on a real agentic loop (OpenCode, 5 iterations/task): the VM trails by 1–5% across all three tasks, standard deviation under 0.2s on every task — a repeatable small gap, not a fluke.

Conclusion from this run: near-zero at single-request scale, a small honest single-digit tax under concurrency. That's the boring, expected result.

## Benchmark 2: Ollama, same questions, opposite answer under load

Different session, same host class, model server swapped to Ollama (`qwen2.5-coder:7b`, Q4_K_M). Same three tests. Single-request speed tells the same unremarkable story:

Mac mini (Apple M4), qwen2.5-coder:7b (Q4_K_M)

 Time to first token 56 ms host 59 ms VM (AI Bridge) +6%

 Throughput 22.09 tok/s host 21.78 tok/s VM (AI Bridge) −1%

Under 8 concurrent clients, the story flips:

8 parallel clients

 Total wall time 15.04 s host 12.73 s VM (AI Bridge) 15% faster

 Avg. per-client time 9.43 s host 8.28 s VM (AI Bridge) 12% faster

The VM finished ~15% faster than the host. On a real agentic loop (Open Interpreter, 5 runs × 3 tasks):

Open Interpreter, 5 runs × 3 tasks, mean ± std dev

 Math computation 6.45 s ±1.16s host 5.38 s ±1.28s VM 17% faster

 System info 7.14 s ±1.12s host 5.82 s ±1.07s VM 18% faster

 File I/O 9.08 s ±1.22s host 6.56 s ±1.38s VM 28% faster

The VM won by 17–28%, consistently, tight variance, no bimodal weirdness. I did not expect this and don't fully trust a single explanation, but here's my current theory: on the host, the benchmark client and the Ollama server compete for the same physical cores; in the VM, the client gets its own dedicated vCPU slice, so it's not fighting the thing it's measuring. Separately, native macOS async I/O goes through `kqueue`, while traffic routed over vsock lands in Velo Workspaces' Swift host process, which proxies to Ollama using Grand Central Dispatch — GCD batches and streams those requests more efficiently than a raw Python client hammering the port directly, effectively an accidental reverse proxy. And on the agentic-loop side, every native `subprocess` spawn on macOS gets briefly intercepted by XProtect/Gatekeeper/Endpoint Security; that overhead doesn't exist for a process forking inside a minimized Ubuntu guest.

I'm not fully confident in that explanation. It's a theory that fits the data, not a proven mechanism.

## Why I'm showing you both instead of picking one

If I'd only run the Ollama benchmark, I'd be telling you sandboxing is free and faster, which sounds too good to be true and would deserve exactly that skepticism. If I'd only run the MLX benchmark, I'd be telling you there's a small unavoidable tax under load, clean and modest and easy to believe. Neither framing is dishonest, but reporting only one would understate how much the specific inference engine's own I/O model apparently matters — possibly more than the VM boundary itself does. That's the actual finding here, and I only found it by not throwing away the "inconvenient" first result when the second one didn't match.

One methodology bug worth admitting: the first time I ran the Ollama numbers, I didn't fully stop all VMs and restart the model server between the host run and the VM run. Agentic-loop numbers came out wildly bimodal — some iterations 10x slower than others. A leftover process from the previous run, fighting the current one for scheduling, was enough to produce a dramatic-looking number that meant nothing. Full stop-and-restart before every single run made the bimodal pattern disappear completely. Every number above is from the disciplined re-run.

## Caveats

Specific to this hardware (M4, 16GB), this exact model (7B, 4-bit), and this exact workload. Won't necessarily hold for a 70B model, an 8GB Mac, or a different agent framework's execution pattern. If you want to check that, or have a better explanation for the Ollama discrepancy than mine, scripts and raw output are here — `ai_perf_test.py`, `ai_load_test.py`, `opencode_perf_test.py`, all three tests, both engines.

This is the architecture behind AI Bridge, a feature of Velo Workspaces, a macOS app I built for exactly this (disposable Linux/macOS VMs on Apple Silicon). Mentioning it plainly since it's the reason I ran these benchmarks in the first place. Related reading: the architecture behind AI Bridge, and a common setup guide for MLX or Ollama + AI agents in a VM.

# flat.social | Absurdly Delightful Virtual Spaces

## 关联链接

- http://127.0.0.1:

## 导航

- 项目页：[[10-项目/veloworkspaces.com_e0288789]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
