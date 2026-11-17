---
type: "project"
title: "apex-compute/ANR"
project_url: "https://apexcompute.com/neural-rendering"
first_seen: "2026-11-17T11:10:48+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - C++
  - created:>2026-11-03
lang: "en"
---

# apex-compute/ANR

> [!info] 一句话导读
> <source media="(prefers-color-scheme: dark)" srcset="assets/apex-logo-white.svg">

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://apexcompute.com/neural-rendering>
> 首次收录：2026-11-17T11:10:48+08:00
> 来源渠道：GitHub 新星仓库
> 标签：C++, created:>2026-11-03
> 最新指标：stars=2482 · forks=53 · open_issues=23

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-17T11:10:48+08:00 | GitHub 新星仓库 | stars=2482 · forks=53 · open_issues=23 | [[20-语料/posts/github_new/2026-11-17/e5e4961f54099a71_apex-compute-ANR]] |

## 摘要正文

# Apex Neural Rendering (ANR)  [Apex Neural Rendering](https://apexcompute.com/neural-rendering) by [Apex Compute](https://apexcompute.com).  - **ANR FG**: frame generation. In beta. - **ANR SR**: super resolution (upscaling). Beta soon. - **ANR RR**: ray reconstruction (denoising for ray tracing). Beta soon. - **Source code**: coming soon. - **nr-record**: records a game's frame generation or upscaler inputs to compare ANR FG, NVIDIA DLSS-G, DLSS, FSR, XeSS and others ([below](#record-and-compare-frame-generation)). Source in this repository.  ## ANR FG Beta  1. Download a package from [Releases](../../releases):    - `anr-fg-full`: for games without OptiScaler.    - `anr-fg-addon`: for games that already use [OptiScaler](https://github.com/optiscaler/OptiScaler). 2. Close the game, extract the package and run the installer with the folder of the game's `.exe`:    - Windows: `install.cmd`    - Linux and Steam Deck (Proton): `sh install.sh "<folder>"`, then set the game's launch options to the line it      prints: `WINEDLLOVERRIDES="dxgi=n,b" %command%`, or `winmm=n,b` in Vulkan games 3. In the game, turn on frame generation (the NVIDIA option where the game offers several).  To un…
