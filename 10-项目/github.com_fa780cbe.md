---
type: "project"
title: "JustAResearcher/gpu-unlock-ada"
project_url: "https://github.com/JustAResearcher/gpu-unlock-ada"
first_seen: "2026-11-01T09:40:10+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - C
  - created:>2026-10-18
lang: "en"
---

# JustAResearcher/gpu-unlock-ada

> [!info] 一句话导读
> GPU unlock 1.1.1 — RTX 4090 and experimental Ada GPUs

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/JustAResearcher/gpu-unlock-ada>
> 首次收录：2026-11-01T09:40:10+08:00
> 来源渠道：GitHub 新星仓库
> 标签：C, created:>2026-10-18
> 最新指标：stars=4626 · forks=593 · open_issues=65

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:40:10+08:00 | GitHub 新星仓库 | stars=4626 · forks=593 · open_issues=65 | [[20-语料/posts/github_new/2026-11-01/fa780cbe8c5e5549_JustAResearcher-gpu-unlock-ada]] |

## 摘要正文

# GPU unlock 1.1.1 — RTX 4090 and experimental Ada GPUs  New to this project? Start with the [copy-paste Quick Start](QUICKSTART.md).  This Linux kernel module enables the SM speed-select override before the stock NVIDIA driver starts. RTX 4090 (`10de:2684`, AD102) support has demonstrated approximately **2× FP16 and BF16 tensor throughput with FP32 accumulation**:  | Mode | Before | After | |---|---:|---:| | FP16 → FP32 accumulate | 165.6 TF/s | 331.6 TF/s | | BF16 → FP32 accumulate | 165.5 TF/s | 330.6 TF/s |  The override survived PCIe Function Level Reset (FLR), stock NVIDIA `615.78.08` initialization and CUDA benchmarks. INT8, `dp4a` and scalar FP32 stayed near their baseline rates. The original transaction preceded the repository cleanup; see the [technical report](rtx4090-register-report.md) and [original evidence](docs/evidence/rtx4090/README.md).  An independent owner run of revision `8855e7b` also completed the RTX 4090 transaction and NVIDIA driver handoff on Linux `7.2.11-arch1-1`. Matched stock/unlocked measurements with NVIDIA `615.78.08` and the same 450 W cap found FP16/FP32 instruction throughput **160.4 → 320.4 TF/s** and BF16/FP32 **159.7 → 320.2 TF/s**. All exer…
