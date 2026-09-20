---
type: "project"
title: "Show HN: I built a 2nd-order PyTorch optimizer for LLMs that runs on 16GB GPUs"
project_url: "https://news.ycombinator.com/item?id=47947319"
first_seen: "2026-09-21T01:42:10+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_dnosoz
  - story_47947319
  - show_hn
lang: "en"
stale: true
---

# Show HN: I built a 2nd-order PyTorch optimizer for LLMs that runs on 16GB GPUs

> [!info] 一句话导读
> Hi HN,I'm Danilo. I've been struggling with the limitations of AdamW when fine-tuning LLMs locally. Second-order optimizers (like Shampoo or SOAP) offer signifi…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://news.ycombinator.com/item?id=47947319>
> 首次收录：2026-09-21T01:42:10+08:00
> 来源渠道：HN Show HN
> 标签：author_dnosoz, story_47947319, show_hn
> 最新指标：点赞=2 · 评论=4 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=2 · 评论=4 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/1e2d413c26722cc0_Show-HN-I-built-a-2nd-order-PyTorch-optimizer-for]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=2 · 评论=4 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/1e2d413c26722cc0_Show-HN-I-built-a-2nd-order-PyTorch-optimizer-for]] |
| 2026-09-21T01:42:10+08:00 | HN Show HN | 点赞=2 · 评论=4 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/1e2d413c26722cc0_Show-HN-I-built-a-2nd-order-PyTorch-optimizer-for]] |

## 摘要正文

Hi HN,I'm Danilo. I've been struggling with the limitations of AdamW when fine-tuning LLMs locally. Second-order optimizers (like Shampoo or SOAP) offer significantly better step-convergence by exploiting Kronecker-factored curvature. The problem? They require O(d^2) memory and O(d^3) compute per layer, which immediately OOMs consumer hardware like a 16GB T4 or RTX 3090.I wanted Shampoo-quality preconditioning on my home setup, so I built SCAO (Sparse Curvature-Aware Optimizer).It's a PyTorch optimizer that acts as a drop-in replacement for AdamW, but it implements a few strict architectural changes to survive on consumer cards:1. Adaptive Rank Selection: Instead of full-rank Kronecker factors, it truncates the eigenspace to retain >=95% of spectral mass. 2. Int8 EMA Quantization: The curvature accumulators are stored in symmetric int8, which yields a 4x memory reduction with zero degradation in perplexity. 3. Quantization Stability: Standard Shampoo usually crashes at step 1 during 4-bit QLoRA fine-tuning due to SVD ill-conditioning in quantized spaces. SCAO exploits sparse approximations to bypass this. 4. Fused CUDA kernels: I wrote custom kernels to fix an O(k * m^2 * n) comple…
