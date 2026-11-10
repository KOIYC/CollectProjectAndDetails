---
type: "project"
title: "Show HN: Airgap-check – find what your AI app silently downloads offline"
project_url: "https://github.com/humanethq/airgap-check"
first_seen: "2026-11-10T09:49:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_humanethq
  - story_50431705
  - show_hn
lang: "en"
---

# Show HN: Airgap-check – find what your AI app silently downloads offline

> [!info] 一句话导读
> humanethq/airgap-check

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/humanethq/airgap-check>
> 首次收录：2026-11-10T09:49:42+08:00
> 来源渠道：HN Show HN
> 标签：author_humanethq, story_50431705, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:49:42+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-11-10/8a21d9b960db7b8a_Show-HN-Airgap-check-–-find-what-your-AI-app-silen]] |

## 摘要正文

# humanethq/airgap-check  Audit AI repositories for offline (--network none) crashes, silent telemetry, and .env secret routing  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-08T21:55:28Z  ## Languages  - Go - Makefile - Shell  ## Top Contributors  - humanetresearch (1 contributions)  ---  ## README  # Humanet airgap-check  Find out what your AI app downloads, or tries to reach, when the network goes away.  airgap-check  Go 1.22+ License: MIT  ## Why  A common assumption: point the LLM base URL at a local vLLM or Ollama instance and the app is ready for an offline network (an air-gapped VPC, a hospital or defense network, a container with no internet). In practice, many libraries fetch something on first use: tokenizer ranks, ONNX embedding weights, corpora, price maps, or telemetry. Offline, these calls either fail at first use or hang for tens of seconds on retry backoff.  None of this is a bug in those libraries. They download once and cache. It only becomes visible when the network is gone. airgap-check tries to surface it before you deploy.  ## What it does  - **Static scan.** Reads manifests (`requirement…
