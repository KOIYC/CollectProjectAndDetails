---
type: "project"
title: "Zagitta/gpu-unlock"
project_url: "https://github.com/Zagitta/gpu-unlock"
first_seen: "2026-10-30T09:49:18+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - C
  - created:>2026-10-16
lang: "en"
---

# Zagitta/gpu-unlock

> [!info] 一句话导读
> ![gpu-unlock: full-speed tensor cores for GeForce RTX](assets/banner.svg)

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/Zagitta/gpu-unlock>
> 首次收录：2026-10-30T09:49:18+08:00
> 来源渠道：GitHub 新星仓库
> 标签：C, created:>2026-10-16
> 最新指标：stars=13108 · forks=1280 · open_issues=92

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:30:16+08:00 | GitHub 新星仓库 | stars=5442 · forks=585 · open_issues=97 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |
| 2026-10-26T00:21:51+08:00 | GitHub 新星仓库 | stars=5647 · forks=603 · open_issues=100 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |
| 2026-10-26T09:44:46+08:00 | GitHub 新星仓库 | stars=6875 · forks=715 · open_issues=123 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |
| 2026-10-27T23:49:00+08:00 | GitHub 新星仓库 | stars=10903 · forks=1075 · open_issues=195 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |
| 2026-10-28T09:43:17+08:00 | GitHub 新星仓库 | stars=11395 · forks=1117 · open_issues=78 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |
| 2026-10-29T20:45:27+08:00 | GitHub 新星仓库 | stars=12778 · forks=1250 · open_issues=90 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |
| 2026-10-30T09:49:18+08:00 | GitHub 新星仓库 | stars=13108 · forks=1280 · open_issues=92 | [[20-语料/posts/github_new/2026-10-25/8acda1e9f09f4448_Zagitta-gpu-unlock]] |

## 摘要正文

![gpu-unlock: full-speed tensor cores for GeForce RTX](assets/banner.svg)  ### Your GeForce runs AI at half speed. This fixes it.  ![Version](https://img.shields.io/badge/version-2.0.0-76b900)![RTX 20 | 30 | 40](https://img.shields.io/badge/GeForce-RTX%2020%20%7C%2030%20%7C%2040-76b900?logo=nvidia&logoColor=white)![Linux](https://img.shields.io/badge/platform-Linux-informational?logo=linux&logoColor=white)![License GPL-2.0](https://img.shields.io/badge/license-GPL--2.0-blue)![Stars](https://img.shields.io/github/stars/Zagitta/gpu-unlock?style=flat&color=yellow)  **Up to 2× FP16 / BF16 / TF32 tensor throughput** · **+25–55% LLM prefill** · **+25–50% fine-tuning** · **+30–55% image generation**  [Supported GPUs](#supported-gpus) · [Benchmarks](#what-you-get) · [Install](#how-to-install) · [FAQ](#faq) · [Support](#support-me)  ---  NVIDIA ships GeForce cards with their tensor cores capped to **half speed** for FP16, BF16 and TF32 math with FP32 accumulation, which is what nearly all AI training and unquantized inference uses. The same silicon sold as an RTX A-series or professional card runs at full rate. `gpu_unlock` removes that cap at boot, before the stock NVIDIA driver loads. No …
