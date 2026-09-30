---
type: "project"
title: "Show HN: TurboGPT: train 22KiB transformer in 13s"
project_url: "https://github.com/lostmsu/TurboGPT"
first_seen: "2026-09-30T18:57:48+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_lostmsu
  - story_49898931
  - show_hn
lang: "en"
---

# Show HN: TurboGPT: train 22KiB transformer in 13s

> [!info] 一句话导读
> Train a tiny GPT in under a minute (CUDA only)

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/lostmsu/TurboGPT>
> 首次收录：2026-09-30T18:57:48+08:00
> 来源渠道：HN Show HN
> 标签：author_lostmsu, story_49898931, show_hn
> 最新指标：点赞=49 · 评论=10 · engagement_velocity=49

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-30T18:28:30+08:00 | HN Show HN | 点赞=49 · 评论=10 · engagement_velocity=49 | [[20-语料/posts/hn_show/2026-09-30/f75ab2d7bca162f3_Show-HN-TurboGPT-train-22KiB-transformer-in-13s]] |
| 2026-09-30T18:57:07+08:00 | HN Show HN | 点赞=49 · 评论=10 · engagement_velocity=49 | [[20-语料/posts/hn_show/2026-09-30/f75ab2d7bca162f3_Show-HN-TurboGPT-train-22KiB-transformer-in-13s]] |
| 2026-09-30T18:57:48+08:00 | HN Show HN | 点赞=49 · 评论=10 · engagement_velocity=49 | [[20-语料/posts/hn_show/2026-09-30/f75ab2d7bca162f3_Show-HN-TurboGPT-train-22KiB-transformer-in-13s]] |

## 摘要正文

# lostmsu/TurboGPT  Train a tiny GPT in under a minute (CUDA only)  - Stars: 35 - Forks: 0 - Watchers: 35 - Open issues: 0 - License: MIT License - Default branch: master - Created: 2026-09-23T20:21:23Z  ## Languages  - C++ - Cuda - Nix - PowerShell - Python  ## Top Contributors  - lostmsu (9 contributions)  ---  ## README  # turboGPT  Tiny byte-level GPT training in CUDA C++. MIT.  ## Build  Linux/NixOS:  ```bash nix-build -o build/nix-result ```  Windows, Visual Studio 2022 C++ tools, and CUDA 13.4:  ```powershell .\build.ps1 -CudaArch 86 ```  `CudaArch` is the GPU compute capability from NVIDIA's CUDA GPU list.  ## Run  ```powershell .\build\turbogpt.exe --data hn1g.txt --log-to runs/ctx4 ```  The run stores its checkpoint at `runs/ctx4/ctx4.pt`, containing model, optimizer, scheduler, and trainer state. Use `--load CHECKPOINT.pt` to resume it.  `runs/ctx4/report.json` is derived from the log directory. Logs are TensorBoard-compatible: one report per batch, capped at 8Mi reports, and flushed with periodic or final checkpoints.  ## Result  - hn1g after 1.5G training tokens: **2.5295 BPB**.  ## Tests  ```powershell python tests\verify.py ```  # yeet-src/agentcap
