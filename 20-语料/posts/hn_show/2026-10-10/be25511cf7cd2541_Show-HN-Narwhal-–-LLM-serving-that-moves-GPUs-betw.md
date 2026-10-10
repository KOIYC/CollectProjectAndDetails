---
type: "corpus"
item_id: "be25511cf7cd2541"
title: "Show HN: Narwhal – LLM serving that moves GPUs between prefill/decode in seconds"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50019698"
project_url: "https://github.com/athrael-soju/Narwhal"
author: "athrael-soju"
published_at: "2026-10-09T12:45:01Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_athrael-soju
  - story_50019698
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Narwhal – LLM serving that moves GPUs between prefill/decode in seconds

> [!info] 一句话导读
> athrael-soju/Narwhal

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50019698>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：athrael-soju　|　发布：2026-10-09T12:45:01Z
> 项目链接：<https://github.com/athrael-soju/Narwhal>
> 采集：2026-10-10T09:53:50+08:00　|　id：`be25511cf7cd2541`

## 正文

# athrael-soju/Narwhal

Adaptive Disaggregated Inference on a Role-free Fleet!

- Stars: 7
- Forks: 2
- Watchers: 7
- Open issues: 13
- License: Apache License 2.0
- Homepage: https://athrael-soju.github.io/Narwhal/
- Default branch: main
- Created: 2026-09-21T15:24:05Z

## Languages

- Dockerfile
- HTML
- Makefile
- Python

## Topics

- amd
- arrow
- cuda
- decode
- disaggregated-inference
- disaggregated-serving
- gpu
- inference
- kv-cache
- llm-inference
- llm-serving
- nixl
- nvidia
- pd-disaggregation
- prefill
- prefix-caching
- rocm
- scheduling
- vllm

## Top Contributors

- athrael-soju (64 contributions)
- github-actions[bot] (8 contributions)

---

## README

## What is Narwhal?

Narwhal is an adaptive, disaggregated inference framework that automatically hot-swaps prefill and decode roles as demand changes, and without having to reload model weights. It can scale from a single GPU to multi-node deployments.

 Capability
 Behavior
 Guide

 Role hot-swap
 Reassigns prefill and decode roles across a fixed GPU fleet, with NIXL key-value (KV) transfer between them

 Serving
 Serves completion and chat requests, streamed or buffered, with latency-aware admission

 Fault tolerance
 Fails over to a warm-standby router and readmits engines against their live process generation

 Measurement
 Profiles engines, runs ordered benchmark points, and keeps the evidence from each point

 Observability
 Exports router and engine metrics to Prometheus and a provisioned Grafana dashboard

 Operator tooling
 Validates fleet files offline and collects private diagnostic bundles

 Development mode
 Runs two to eight engines on one NVIDIA CUDA GPU under Ubuntu or WSL2

## How engines change roles

The role controller scores the current role split and each adjacent split, one engine move away. It projects each split from measured engine profiles, offered demand, and resident work. A split's score is its worst projected service-level objective (SLO) ratio across time to first token (TTFT), time per output token (TPOT), and decode queueing.

Projections use measured window demand. A decode-to-prefill candidate takes its decode demand from the larger of the short- and long-horizon estimates.

The controller moves to an adjacent split that improves the score by at least the configured margin. A decode-to-prefill move also needs stable decode demand and a closed arrival-evidence window. The window closes after `controller.reactive.evidence_span_s` with the minimum number of arrivals, or after `controller.reactive.evidence_max_span_s` under sparse traffic. A prefill-to-decode move with prefill load at or below `controller.thresholds.shrink` can proceed while the window is open.

When demand over the confirmation span shifts after a settled run, the controller moves one engine. The settled run is `controller.reactive.evidence_span_s`, or one confirmation span shorter when the shift reverses the controller's recent moves. The controller keeps moving engines in that direction on confirmation-span demand while the shift lasts: after its first move for a reversing shift, and after `controller.reactive.evidence_span_s` for any other shift. Under steady demand, the score chooses between adjacent splits once the arrival-evidence window has closed.

Every move passes guards for pinned engines, role floors, cooldown, dwell time, the resident-stream cap on decode donors, and engine lifecycle holds. While a role is below its configured floor, floor repair moves one engine per monitor pass.

New requests follow the revised split, and resident requests finish on their assigned engines.

Role controller changing engine roles with weights resident.

## Evaluation

 Read the full evaluation: Evaluating Narwhal

## Getting the commands

Install on Linux with Python 3.11 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install narwhal-inference
narwhal-serve --version
narwhal --help
```

The wheel installs these commands:

## Trying it on one GPU

Narwhal dev runs a local NVIDIA CUDA fleet on Ubuntu, either directly or under WSL2.

```bash
narwhal dev init
narwhal dev up
narwhal dev verify
narwhal dev status
narwhal dev down
```

The installed template starts two engines on an NVIDIA GPU with 8 GB of VRAM or less. The RTX 5090 reference template starts four engines on an RTX 5090.

## Bringing up a fleet

Run these gates in order from a management workstation:

1. Freeze inputs and discover the deployment in Gate A.
2. Package and install the approved revision in Gate B.
3. Validate and start every engine in Gate C.
4. Qualify the transfer fabric in Gate D.
5. Attest the live engines in Gate E.
6. Profile the engines and run preflight in Gate F.
7. Start the router and validate capacity through an SSH tunnel in Gate G.

## Documentation

## Contributing

## Built on Arrow

Narwhal's scheduling algorithms derive from Arrow: Adaptive Scheduling Mechanisms for Disaggregated LLM Inference Architecture by Wu et al. (2025).

# Live market radar and market data | SignalHub

## 评论（1/1）

> **z0nda** · 2026-10-09T13:09:27.000Z　
> What happens to the model weights when a role flip takes place?

## 关联链接

- https://athrael-soju.github.io/Narwhal/

## 导航

- 项目页：[[10-项目/github.com_5b7a281a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
