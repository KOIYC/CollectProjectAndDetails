---
type: "project"
title: "Show HN: Tilery-VM – run Nvidia cuTile GPU kernels on a CPU, no GPU required"
project_url: "https://github.com/drbh/tilery-vm"
first_seen: "2026-09-21T03:11:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_justdrbh
  - story_49111222
  - show_hn
lang: "en"
---

# Show HN: Tilery-VM – run Nvidia cuTile GPU kernels on a CPU, no GPU required

> [!info] 一句话导读
> CPU virtual machine for CUDA Tile IR bytecode - run cuTile kernels without a GPU

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/drbh/tilery-vm>
> 首次收录：2026-09-21T03:11:16+08:00
> 来源渠道：HN Show HN
> 标签：author_justdrbh, story_49111222, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/64e8dab152963cc0_Show-HN-Tilery-VM-–-run-Nvidia-cuTile-GPU-kernels]] |
| 2026-09-21T03:11:16+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/64e8dab152963cc0_Show-HN-Tilery-VM-–-run-Nvidia-cuTile-GPU-kernels]] |

## 摘要正文

# drbh/tilery-vm  CPU virtual machine for CUDA Tile IR bytecode - run cuTile kernels without a GPU  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-03-24T18:09:57Z  ## Languages  - MLIR - Makefile - Python - Rust - Shell  ## Topics  - cuda - cutile - gpu-programming - interpreter - mlir - rust - tileir - virtual-machine  ## Top Contributors  - drbh (20 contributions)  ---  ## README  # tilery-vm  `tilery-vm` is a virtual machine for CUDA Tile IR bytecode.  It executes TileIR bytecode on a CPU, so cuTile kernels can be developed and tested without a GPU. TileIR is NVIDIA's open, language-agnostic IR for CUDA kernels (the PTX analogue for the tile programming model); cuTile is the user-facing language that emits it, from both the Python and Rust clients.  ## Quickstart  no GPU, no CUDA, no setup step:  ```bash uv run examples/minimal.py   # [0.0320586  0.08714432 0.23688284 0.6439143 ] cargo test --workspace       # 136 tests ```  ## Usage  One way you can use `tilery-vm` is by using tilery_vm as a cpu backend for `cuda-tile`.  This allows you to write native cutile in a environment that does not have a gpu, an…
