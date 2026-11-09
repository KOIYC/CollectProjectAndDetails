---
type: "project"
title: "Show HN: Maple – Run Gemma 4 26B on a 6GB Laptop GPU at 45 TPS (Sub-2-BPW)"
project_url: "https://amsach.github.io/maple"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_AmSach
  - story_50415106
  - show_hn
lang: "en"
---

# Show HN: Maple – Run Gemma 4 26B on a 6GB Laptop GPU at 45 TPS (Sub-2-BPW)

> [!info] 一句话导读
> Portability & MoE Guide

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://amsach.github.io/maple>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_AmSach, story_50415106, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-09/cda5465b44205da7_Show-HN-Maple-–-Run-Gemma-4-26B-on-a-6GB-Laptop-GP]] |

## 摘要正文

MAPLE  v1.0 GGUF Benchmarks  Architecture  Portability & MoE Guide  Quickstart  Preprint GitHub RESEARCH PREPRINT & OPEN-WEIGHTS RELEASE Run Gemma 4 26B 100% In-VRAM at 45.4 TPS on a 6GB Laptop GPU. Manifold-Activated Pruning of Latent Experts (MAPLE) compresses 128-expert fine-grained MoE architectures down to 4.75 GB (1.48 effective BPW), eliminating PCIe system-RAM paging stalls forever. Download GGUF (4.75 GB) Read Preprint (Zenodo DOI) llama.cpp Showcase #31894 Kaggle DOI 10.34740/KAGGLE/M/786779 Throughput 45.4 t/s 6.57x speedup vs PCIe offload Container Size 4.75 GB Sub-5GB (100% fits in 6GB VRAM) Quantization 1.48 BPW IQ2_XXS calibrated via imatrix Expert Pruning 80 / 128 79.88% activation mass preserved Hardware Benchmark Proof The PCIe Paging Death Spiral, Solved. Consumer laptops cannot run uncompressed 26B models without overflowing into system RAM over bandwidth-constrained PCIe lanes. Inference Throughput (RTX 4050 6GB)  6.57x Real-World Lift Base Gemma 4 26B IQ2_XXS (9.92 GB)  6.9 TPS (16/30 layers in VRAM) 14 layers offloaded to system RAM. Constrained by 15.75 GB/s PCIe bus bandwidth. MAPLE 48-Expert Container (4.75 GB) 45.4 TPS (30/30 layers in VRAM) 100% In-VRAM …
