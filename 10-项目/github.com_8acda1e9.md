---
type: "project"
title: "Zagitta/gpu-unlock"
project_url: "https://github.com/Zagitta/gpu-unlock"
first_seen: "2026-10-26T00:21:51+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - C
  - created:>2026-10-12
lang: "en"
---

# Zagitta/gpu-unlock

> [!info] 一句话导读
> Unlock FP/BF16 instruction issue rate on Nvidia 3000's cards to their professional equivalents

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Zagitta/gpu-unlock>
> 首次收录：2026-10-26T00:21:51+08:00
> 来源渠道：GitHub 新星仓库
> 标签：C, created:>2026-10-12
> 最新指标：stars=5647 · forks=603 · open_issues=100

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:30:16+08:00 | GitHub 新星仓库 | stars=5442 · forks=585 · open_issues=97 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |
| 2026-10-26T00:21:51+08:00 | GitHub 新星仓库 | stars=5647 · forks=603 · open_issues=100 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |

## 摘要正文

# GPU unlock 1.0.0  Unlock FP/BF16 instruction issue rate on Nvidia 3000's cards to their professional equivalents  This Linux kernel module combines the CMP unlocker's V67/PLM technique with the pre-driver timing of the UEFI approach. It runs the unlock, writes the speed selectors (SS0 `0x88888888`, which selects the full BF16 rate, and the 4-bit SS1 `0x8` IMLA4) and performs FLR before the unmodified NVIDIA driver binds the card. It is neither a UEFI application nor a patched NVIDIA driver.  The benefit of this early kmod driver is that it does not require manual patching each time nvidia releases a new driver version.  The effect of this unlock is that it doubles the instruction issuing speed of FP/BF16 FMA into FP32 operations on GA102, GA103, GA104 and GA106 cards.  [3090 Ti dense 8192³ GEMM at 450 W, five-sample medians with FP32 accumulation](https://github.com/Zagitta/gpu-unlock/issues/1#issue-5905622687):  | Input | Before       | After         | | ----- | ------------ | ------------- | | FP16  | 87.46 TFLOPS | 118.39 TFLOPS | | BF16  | 87.50 TFLOPS | 157.41 TFLOPS | | TF32  | 42.58 TFLOPS | 82.61 TFLOPS  |  ## Tested cards  Results reported by users. The module accepts ev…
