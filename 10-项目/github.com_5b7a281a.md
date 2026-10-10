---
type: "project"
title: "Show HN: Narwhal – LLM serving that moves GPUs between prefill/decode in seconds"
project_url: "https://github.com/athrael-soju/Narwhal"
first_seen: "2026-10-10T09:53:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_athrael-soju
  - story_50019698
  - show_hn
lang: "en"
---

# Show HN: Narwhal – LLM serving that moves GPUs between prefill/decode in seconds

> [!info] 一句话导读
> athrael-soju/Narwhal

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/athrael-soju/Narwhal>
> 首次收录：2026-10-10T09:53:50+08:00
> 来源渠道：HN Show HN
> 标签：author_athrael-soju, story_50019698, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-10T09:53:50+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-10/be25511cf7cd2541_Show-HN-Narwhal-–-LLM-serving-that-moves-GPUs-betw]] |

## 摘要正文

# athrael-soju/Narwhal  Adaptive Disaggregated Inference on a Role-free Fleet!  - Stars: 7 - Forks: 2 - Watchers: 7 - Open issues: 13 - License: Apache License 2.0 - Homepage: https://athrael-soju.github.io/Narwhal/ - Default branch: main - Created: 2026-09-21T15:24:05Z  ## Languages  - Dockerfile - HTML - Makefile - Python  ## Topics  - amd - arrow - cuda - decode - disaggregated-inference - disaggregated-serving - gpu - inference - kv-cache - llm-inference - llm-serving - nixl - nvidia - pd-disaggregation - prefill - prefix-caching - rocm - scheduling - vllm  ## Top Contributors  - athrael-soju (64 contributions) - github-actions[bot] (8 contributions)  ---  ## README  ## What is Narwhal?  Narwhal is an adaptive, disaggregated inference framework that automatically hot-swaps prefill and decode roles as demand changes, and without having to reload model weights. It can scale from a single GPU to multi-node deployments.   Capability  Behavior  Guide   Role hot-swap  Reassigns prefill and decode roles across a fixed GPU fleet, with NIXL key-value (KV) transfer between them   Serving  Serves completion and chat requests, streamed or buffered, with latency-aware admission   Fault tole…
