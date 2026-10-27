---
type: "corpus"
item_id: "2ed0cf9106f4cbd1"
title: "Show HN: Carmen – harness for reliable AI-written Metal kernels"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50259977"
project_url: "https://github.com/utsav1033/carmen"
author: "utsav1033"
published_at: "2026-10-27T14:30:45Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_utsav1033
  - story_50259977
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Carmen – harness for reliable AI-written Metal kernels

> [!info] 一句话导读
> An AI writes Apple Metal GPU kernels, a judge it can't fool proves them, and the winners run inside a real model: Qwen 2.5 0.5B decode 3% faster with identical …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50259977>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：utsav1033　|　发布：2026-10-27T14:30:45Z
> 项目链接：<https://github.com/utsav1033/carmen>
> 采集：2026-10-27T23:46:32+08:00　|　id：`2ed0cf9106f4cbd1`

## 正文

# utsav1033/carmen

An AI writes Apple Metal GPU kernels, a judge it can't fool proves them, and the winners run inside a real model: Qwen 2.5 0.5B decode 3% faster with identical output; 75/75 planted bugs caught.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Homepage: utsav1033.github.io
- Default branch: main
- Created: 2026-09-24T19:44:26Z

## Languages

- Metal
- Python
- Shell

## Top Contributors

- utsav1033 (82 contributions)

---

## README

 An LLM writes GPU kernels for Apple Silicon and carmen tests every one.
 Then it measures whether a real model on a Mac actually gets faster.

 TL;DR ·
 The CLI ·
 Try it ·
 The problem ·
 How it works ·
 Results ·
 What I learned

## TL;DR

- **Most AI-kernel results are graded by a check that misses a lot.** I planted 75 realistic bugs in GPU kernels: the usual check caught 40. carmen's tests caught all 75.
- **The kernels that passed were also faster.** Claude's masked softmax ran **1.82× faster** than Apple's MLX (MLX does it in 3 steps, Claude's in 1), and add + rmsnorm **1.41×**.
- **But in a real model they barely mattered:** +2–3% on Qwen 0.5B, nothing on bigger models, because MLX already reads the model's weights about as fast as the Mac allows. What did speed up bigger models was speculative decoding, an existing mlx-lm feature carmen measured: 1.48× on Qwen 3B.

## The CLI

**The home screen:** what's been proven, the models you can speed up, and the kernels carmen has written.

**A model's page** (Qwen 2.5 3B): everything measured on it, and what you can run.

Run `carmen`, press `m`, pick a model: it shows what's been measured on it and what you can run, no API key needed.

## The problem

LLMs can write GPU kernels, but a kernel can pass a quick test and still be wrong. Most AI-kernel benchmarks try a
single input and accept any answer that's roughly close. So a kernel that works on 1,024 numbers but forgets the last
one when there are 1,025, or one whose answers are slightly off, still counts as correct
(one study found this kind of check misses most precision bugs).

And even a kernel that really is correct and faster on its own may not make the model any faster.
I wanted to know if an LLM could make a model on my Mac faster, and prove it.

## How carmen works

At its core it's a loop: Claude writes a Metal kernel, carmen tests it, and the fastest correct one is kept and
improved. Plenty of projects do that. The difference is that carmen doesn't trust the loop, because a plain loop
fools itself in three ways:

- **The tests miss bugs.** So carmen's tests are tested: I planted 75 realistic bugs in correct kernels.
 carmen caught all 75; the usual one-input check caught 40. Failures tell Claude exactly where it went wrong.
- **The model learns to pass the tests instead of being correct.** So part of the test set is hidden: inputs Claude
 never sees, for correctness and for speed. Without that, 30% of LLM kernel "wins" on Metal broke
 on inputs nobody had tested.
- **"Faster" doesn't mean the model gets faster.** So every win is timed against MLX's own fusion with error bars,
 then checked again inside a real model. That's how carmen found that kernels which win on their own barely move Qwen at all.

How the testing works →

## Results

Everything here ran on my M4 MacBook Pro (16 GB). Numbers in brackets are the range the real value is 95% likely to be in.

**Single kernels.** Claude beat MLX where MLX splits the work into several small steps. On matmul and attention, which Apple has already tuned heavily, it lost:

| kernel | MLX | carmen | speedup |
|---|---|---|---|
| masked softmax | 3 kernels | 1 fused kernel | **1.82×** |
| add + rmsnorm | 2 kernels | 1 fused kernel | **1.41×** |
| matmul | Apple's tuned kernel | 1 kernel | 0.93× |
| attention | Apple's tuned kernel | 1 kernel | 0.54× |

Against MLX's own automatic fusion (`mx.compile`), the first two are still 1.38× and 1.43×.

**In real models,** carmen's fused MLP kernels (tuned on 0.5B) mostly disappear, because MLX is already close to the fastest the Mac can go:

| Qwen 2.5, 4-bit | MLX | carmen | speedup | fastest possible* |
|---|---|---|---|---|
| 0.5B | 214 tok/s | 220 tok/s | **1.02×** [1.01–1.02] | ~337 tok/s |
| 1.5B | 94 tok/s | 87 tok/s | 0.93× [0.93–0.95] | ~108 tok/s |
| 3B | 44 tok/s† | 42 tok/s | 0.95× [0.93–0.97] | ~53 tok/s |

 *Each new word means reading all of the model's weights from memory once. My M4 reads about 94 GB/s, so a 1.74 GB
model (3B) can't go much past ~53 words per second, however good the kernels are. On a quiet Mac MLX runs 3B at ~52 of 53; on 0.5B it's
at 214 of 337, which is where carmen's kernels still had room.
†This 3B run was on a busier Mac, so both sides are slower. The speedup compares them run by run, so it still holds.

**Why fusion barely helped: Amdahl's law.** If you speed up only part of the work, the whole job gets faster only as
much as that part allows: speeding up a fraction *p* of the time by *s* gives an overall speedup of 1 / ((1 − *p*) + *p*/*s*).

- On **0.5B**, about 36% of each word's time is the part kernels can shrink (launches, small steps). Even making it free
 would cap out around 1.56×. carmen's kernels got 1.02×.
- On **3B**, that part is about 3%. Even infinitely fast kernels would give at most 1 / 0.97 ≈ **1.03×**.

**What did make bigger models faster: speculative decoding.**

- A small model guesses the next few words, and the big model checks them all in one go.
- So the big model reads its weights once for several words instead of once per word.
- It's a feature mlx-lm already has. carmen just measured it (`carmen levers`).
- carmen also tried compressing the model's memory of the conversation (the KV cache). That made things slower, or broke the output:

Decode speed in tokens per second, stock MLX → with the technique:

| technique | model | 512-token prompt | 8k-token prompt | output |
|---|---|---|---|---|
| speculative decoding | 3B | 51.8 → 64.7 · **1.24×** [1.20–1.28] | 44.5 → 66.0 · **1.48×** [1.46–1.53] | same as stock |
| | 7B | 24.1 → 28.6 · **1.19×** [1.18–1.22] | 22.1 → 24.8 · **1.13×** [1.12–1.15] | same as stock |
| 8-bit KV cache | 3B | 51.8 → 48.7 · 0.93× [0.93–0.94] | 44.5 → 37.8 · 0.86× [0.83–0.89] | 98–99% same |
| | 7B | 24.1 → 23.6 · 0.98× [0.98–0.98] | 22.1 → 20.3 · 0.92× [0.91–0.92] | 95–98% same |
| 4-bit KV cache | 3B | | | broken |

 Notes on these numbers

- Speculative decoding beats the speed limit (66 vs ~46 tok/s on 3B at 8k) because it reads the weights once for several words. It helps less on 7B because the 0.5B draft is accepted less often (46–52% of words vs 57–71%).
- The 8-bit KV cache is slower because MLX runs attention on it as four separate steps instead of one fused kernel. That's carmen's next target.
- The 4-bit KV cache turns Qwen's output into gibberish ("The skyuser\nquiv"): its attention keys have outliers 4 bits can't hold.
- The "fastest possible" figures use my measured ~94 GB/s, which is a bit low (7B actually runs slightly faster than its figure), so treat them as approximate.
- Spec output matches stock until a late fp16 rounding flip, as expected when the big model checks words in a batch.

## What I learned

- AI kernels don't beat hand-tuned code. They beat code nobody fused.
- A kernel that wins alone can lose inside a model.
- Past ~1B parameters, memory is the limit, not kernels.
- Getting numbers I could trust took more work than writing the kernels.

New to this? How it all works explains LLMs, GPUs and kernels from scratch.

## Try it

On an Apple Silicon Mac:

```bash
pip install carmen-kernels          # or: uv tool install carmen-kernels
carmen                              # the app
carmen speedup                      # Qwen 2.5 0.5B, stock vs carmen's kernels, on your Mac (no API key)
carmen speedup qwen0.5b qwen3b      # several models in turn, then one table side by side
carmen levers qwen3b                # speculative decoding, KV cache quantization, 3-bit weights vs stock (no API key)
carmen key                          # only to cook new kernels: paste an Anthropic key once, saved for you only
```

 All commands

| command | what it does |
|---|---|
| `carmen` | the terminal app: what's proven, speed up a model, pick a kernel, watch it cook |
| `carmen speedup [models…]` | stock MLX vs `mx.compile` vs carmen's bundled kernels on real models, taking turns; no API key (`--quick` for ~2 min a model) |
| `carmen levers [model]` | speculative decoding, 8/4-bit KV cache and 3-bit weights vs stock, at 512 and 8k prompts, with drift scored for the lossy ones; no API key |
| `carmen run [--for qwen0.5b]` | let Claude write one kernel; `--for` tests it at a real model's sizes |
| `carmen broken ` | plant bugs and check carmen's tests catch every one, next to the usual one-size check |
| `carmen judge ` | test a kernel you wrote |
| `carmen e2e [model]` | run a real model stock vs with carmen's kernels: speed, noise range, same answers? |
| `carmen profile [model]` | where a model spends its time, step by step |
| `carmen bench` | the feedback loop vs plain best-of-N, same budget |

From source: `git clone https://github.com/utsav1033/carmen`, then `pip install -e '.[dev]'`. Keys go in `carmen key`, a `.env` in the folder you run from, or your shell; the shell wins.

## Built on the shoulders of

Measuring the Checker · Gaming Without an Attacker · Metal-Sci · Hacker-Fixer Loops · Test-Input Generation for Tensor Programs · Reward Hacking in Self-Improving Code Agents · Meta-Harness · Auditing Harness Tampering · SoL-Pi · SAGE · Prime Agent · KernelBench-Verified · Contract-Grade Verifier · Building a C compiler with parallel Claudes

 Named after Carmen "Carmy" Berzatto. Banner drawing used with the artist's permission: fan art, not affiliated with Jeremy Allen White or *The Bear*. Lettered in Caveat (SIL Open Font License). Diagrams drawn with rough.js in Virgil (Excalidraw's font, OFL).

# ultramancode/spring-ai-privacy-guardrails

## 关联链接

- https://github.com/utsav1033/carmen`,

## 导航

- 项目页：[[10-项目/github.com_5e7044e7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
