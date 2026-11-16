---
type: "project"
title: "shanselman/gputaskman"
project_url: "https://github.com/shanselman/gputaskman"
first_seen: "2026-11-16T10:02:31+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Python
  - created:>2026-11-02
lang: "en"
---

# shanselman/gputaskman

> [!info] 一句话导读
> An `htop` for what's inside your GPU, not just how full it is.**

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/shanselman/gputaskman>
> 首次收录：2026-11-16T10:02:31+08:00
> 来源渠道：GitHub 新星仓库
> 标签：Python, created:>2026-11-02
> 最新指标：stars=3344 · forks=164 · open_issues=7

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:02:31+08:00 | GitHub 新星仓库 | stars=3344 · forks=164 · open_issues=7 | [[20-语料/posts/github_new/2026-11-16/d5689684c624bc29_shanselman-gputaskman]] |

## 摘要正文

# gputaskman  **An `htop` for what's inside your GPU, not just how full it is.**  Windows with NVIDIA/AMD telemetry and Intel WDDM activity, plus Linux and WSL support (NVIDIA everywhere, AMD and Intel on native Linux; see [Linux and WSL](#linux-and-wsl)) and macOS on Apple Silicon (see [macOS](#macos-apple-silicon)). A terminal UI that connects per-process GPU memory and engine activity with loaded runtimes, model files, and LLM buffer breakdowns.  Task Manager says "15 GB used." This tries to answer: *by what? Model weights? KV cache? Your browser? The desktop compositor? And why is so much GPU memory in system RAM?*  **Scope: local GPU workloads, not cloud services.** Decision models, vision, speech, LLM inference, training/fine-tuning (including Unsloth), graphics, and video all belong here. Visibility varies: process memory and engine activity are measured; identifying individual models and their work requires supporting evidence. A PyTorch/CUDA DLL alone cannot identify a model or prove training, and a mapped file does not prove that model is resident on the GPU or being exercised. CPU-only, NPU-only, and cloud workloads are out of scope.  ![Live GPU overview with an LLM's we…
