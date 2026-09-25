---
type: "project"
title: "jaredpalmer/kev"
project_url: "https://github.com/jaredpalmer/kev"
first_seen: "2026-09-24T23:59:53+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Python
  - created:>2026-09-10
lang: "en"
---

# jaredpalmer/kev

> [!info] 一句话导读
> Small Jev-like decision models you can train and run yourself.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/jaredpalmer/kev>
> 首次收录：2026-09-24T23:59:53+08:00
> 来源渠道：GitHub 新星仓库
> 标签：Python, created:>2026-09-10
> 最新指标：stars=6636 · forks=377 · open_issues=34

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:59:53+08:00 | GitHub 新星仓库 | stars=6636 · forks=377 · open_issues=34 | [[20-语料/posts/github_new/2026-09-24/7f309519de9eb862_jaredpalmer-kev]] |

## 摘要正文

# Kev  Small Jev-like decision models you can train and run yourself.  Kev is a family of small decision models built on Qwen3.5 and based on the architecture described in [Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked). You can use the pretrained weights or train your own. The API matches TypeSafe's [System One](https://docs.typesafe.ai/api), so you can point their Python SDK at your local server.  ## Highlights  - 0.8B, 4B, 9B and 27B models, with training code and evaluation data. - Yes/no (`noul`), multiple-choice (`choice`), and rating (`score`) questions in the same request. - Questions share the input text but can't read each other. - Runs on CUDA, ROCm, and Apple Silicon (MLX). The 4B and 9B models fit a 32 GB Mac; see [Serving Performance](#serving-performance) for what to expect. - A web playground for trying your own inputs and checking how option order affects the answers. Or try Kev-4B and Kev-0.8B in the browser at [huggingface.co/spaces/jaredpalmer/kev](https://huggingface.co/spaces/jaredpalmer/kev), no install needed.  ![Kev playground](docs/playground.png)  ## Quick Start  You'll need Python 3.12 or 3.13 and [uv](https://docs.…
