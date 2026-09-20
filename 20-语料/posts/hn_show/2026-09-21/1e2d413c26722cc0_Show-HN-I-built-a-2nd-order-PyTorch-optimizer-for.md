---
type: "corpus"
item_id: "1e2d413c26722cc0"
title: "Show HN: I built a 2nd-order PyTorch optimizer for LLMs that runs on 16GB GPUs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47947319"
project_url: "https://doi.org/10.5281/zenodo.19870556I"
author: "dnosoz"
published_at: "2026-04-29T12:19:09Z"
captured_at: "2026-09-21T02:23:40+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_dnosoz
  - story_47947319
  - show_hn
metrics: {"points": 2, "comments": 4, "engagement_velocity": 2}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:174d"
---

# Show HN: I built a 2nd-order PyTorch optimizer for LLMs that runs on 16GB GPUs

> [!info] 一句话导读
> Hi HN,I'm Danilo. I've been struggling with the limitations of AdamW when fine-tuning LLMs locally. Second-order optimizers (like Shampoo or SOAP) offer signifi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47947319>
> 指标：点赞=2 · 评论=4 · engagement_velocity=2
> 作者：dnosoz　|　发布：2026-04-29T12:19:09Z
> 项目链接：<https://doi.org/10.5281/zenodo.19870556I>
> 采集：2026-09-21T02:23:40+08:00　|　id：`1e2d413c26722cc0`

## 正文

Hi HN,I'm Danilo. I've been struggling with the limitations of AdamW when fine-tuning LLMs locally. Second-order optimizers (like Shampoo or SOAP) offer significantly better step-convergence by exploiting Kronecker-factored curvature. The problem? They require O(d^2) memory and O(d^3) compute per layer, which immediately OOMs consumer hardware like a 16GB T4 or RTX 3090.I wanted Shampoo-quality preconditioning on my home setup, so I built SCAO (Sparse Curvature-Aware Optimizer).It's a PyTorch optimizer that acts as a drop-in replacement for AdamW, but it implements a few strict architectural changes to survive on consumer cards:1. Adaptive Rank Selection: Instead of full-rank Kronecker factors, it truncates the eigenspace to retain >=95% of spectral mass.
2. Int8 EMA Quantization: The curvature accumulators are stored in symmetric int8, which yields a 4x memory reduction with zero degradation in perplexity.
3. Quantization Stability: Standard Shampoo usually crashes at step 1 during 4-bit QLoRA fine-tuning due to SVD ill-conditioning in quantized spaces. SCAO exploits sparse approximations to bypass this.
4. Fused CUDA kernels: I wrote custom kernels to fix an O(k * m^2 * n) complexity bottleneck in the naive projection implementation.The Benchmark:
I recently ran a head-to-head benchmark on a single T4 (16GB VRAM) fine-tuning Qwen2.5-3B (4-bit QLoRA, rank 16):
- Shampoo: Failed at Step 1 (SVD mathematical collapse).
- SCAO: 100% stability, peaked at exactly 7.14 GB VRAM, with a smooth loss descent.It is pip-installable (pip install scao).I've written a technical report detailing the regret bounds, ablation studies, and scaling laws (published on Zenodo), but I really wanted to get this community's eyes on the CUDA kernels and the PyTorch implementation.GitHub: https://github.com/whispering3/scao
Technical Report (DOI): https://doi.org/10.5281/zenodo.19870556I'd love any feedback, code roasts, or questions about the math behind it!

## 评论（4/4）

> **satvikpendem** · 2026-04-29T12:20:39.000Z　
> Your account is shadow banned by the way, I guess you've just been self promoting too much.

---

> **dnosoz** · 2026-04-29T12:20:48.000Z　
> Author here. Happy to answer any deep-dive questions about the CUDA implementation or the Kronecker factorization math.

---

> **lostmsu** · 2026-04-29T13:05:39.000Z　
> Does it actually improve time to target loss?

---

> **dnosoz** · 2026-05-06T10:48:43.000Z　
> Yes, I ran some benchmarks

## 关联链接

- https://github.com/whispering3/scao

## 导航

- 项目页：[[10-项目/doi.org_b43f4dc7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
