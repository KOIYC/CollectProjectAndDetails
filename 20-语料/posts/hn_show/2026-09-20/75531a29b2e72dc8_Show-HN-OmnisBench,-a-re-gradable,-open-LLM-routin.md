---
type: "corpus"
item_id: "75531a29b2e72dc8"
title: "Show HN: OmnisBench, a re-gradable, open LLM routing benchmark on fresh tasks"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49727542"
project_url: "https://github.com/Fortitude-Group/OmnisBench"
author: "fortitudedev"
published_at: "2026-09-16T14:25:52Z"
captured_at: "2026-09-20T09:37:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_fortitudedev
  - story_49727542
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: OmnisBench, a re-gradable, open LLM routing benchmark on fresh tasks

> [!info] 一句话导读
> Fortitude-Group/OmnisBench

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49727542>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：fortitudedev　|　发布：2026-09-16T14:25:52Z
> 项目链接：<https://github.com/Fortitude-Group/OmnisBench>
> 采集：2026-09-20T09:37:02+08:00　|　id：`75531a29b2e72dc8`

## 正文

# Fortitude-Group/OmnisBench

Open, reproducible benchmark for LLM routing efficiency — verify routing-savings claims yourself. Ideal routing hit 99.7% quality at ~90% lower cost, and every number is re-gradable offline. Apache-2.0.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://omnisbench.fortitude-omnis.group/
- Default branch: main
- Created: 2026-08-18T20:36:28Z

## Languages

- HTML
- Python

## Topics

- ai
- benchmark
- evaluation
- llm
- llm-benchmark
- llm-cost-optimization
- llm-router
- llm-routing
- llmops
- model-routing
- prompt-router
- reproducible-research

## Top Contributors

- fortitude-omnis (21 contributions)
- semper-fortis (1 contributions)

---

## README

# OmnisBench

Open, reproducible benchmark for **LLM routing efficiency** — how close a routing
policy gets to the ideal quality-per-dollar frontier. Apache-2.0.

Prior art: RouterBench (Martian, arXiv:2403.12031). OmnisBench differs by being
live, cost-current, and continuously re-gradable (`omnisbench verify`).

## ⚠️ Security warning: untrusted code execution

`omnisbench run` executes **untrusted, model-generated Python** in order to grade
code tasks (the `code_unittest` grader). The v0 sandbox (`src/omnisbench/graders/sandbox.py`)
provides a fresh subprocess, a hard timeout, and a throwaway working directory —
but it does **NOT** provide network isolation, filesystem isolation, or memory/
resource limits. A malicious or buggy model response can still make outbound
network calls, read/write anything the host process can reach, or exhaust host
resources within the timeout window.

**Run `omnisbench run` inside a container or a disposable VM.** Full sandbox
hardening (network egress blocking, filesystem jail, resource limits) is a
tracked v1 item — it is not implemented yet, and no test in this repo asserts
isolation the code does not actually provide.

`omnisbench verify` does not execute untrusted code from a live model — it only
re-runs graders (including `code_unittest`, so the same untrusted-code caveat
above applies to the *response text already stored in* `results.json`) against
already-published, static data. The same sandboxing caveat applies: verify a
`results.json` you don't trust inside a container/VM too.

## Headline results (v0 — run 2026-08-19)

Suite: **HumanEval (164)** + **GSM8K (200)** = 364 objectively auto-graded items.
Candidate pool: `claude-opus-5`, `gpt-5`, `claude-haiku-4-5`, `gpt-5-nano`.
Pricing snapshot: `config/pricing/2026-08-18.yaml`. Full artifacts in `runs/2026-08-19/`.

| Policy | What it does | Task success | Cost / 1,000 requests |
|---|---|---:|---:|
| **oracle** | ideal per-request routing (cheapest model that *actually* solved each item) | **99.7%** | **$0.62** |
| always_big | always `claude-opus-5` (frontier) | 99.2% | $6.25 |
| random | uniform random over the pool | 96.2% | $4.01 |
| always_cheap | always `gpt-5-nano` (floor) | 94.5% | $0.43 |

**Ideal routing reaches 99.7% task success at ~90% lower cost than always using the frontier
model** — and every figure is reproducible offline: `omnisbench verify runs/2026-08-19` re-runs
the graders against the published responses and re-derives this table with **zero API calls**.

Read these numbers honestly:

- `oracle` is the **theoretical ceiling** of routing on this suite (chosen post-hoc, per item) —
 not a shippable router. It is the frontier a real router aims at; the gap between a real router
 and `oracle` is the real scorecard.
- On this suite the cheapest model alone (`gpt-5-nano`) already scores **94.5%**, so routing's
 realizable prize is recovering the last ~5 points of quality while staying ~10× cheaper than the
 frontier — not a magic 40–70% headline.
- Reasoning models were given a 4,096-token output budget; results reflect that budget.

Reproduce (needs `OPENAI_API_KEY` + `ANTHROPIC_API_KEY`):

```bash
pip install -e .
python scripts/prepare_datasets.py
python -m omnisbench.cli run    --config configs/v0.yaml --run runs/mine
python -m omnisbench.cli report --run runs/mine
python -m omnisbench.cli verify --run runs/mine   # zero-API re-grade of the published results
```

## `omnisbench verify`

`omnisbench verify` re-runs the graders against the published per-item
responses and re-derives the full leaderboard (quality + cost) with zero API
calls — anyone can reproduce and audit the numbers from `results.json` alone.

# ukisai/Swift-Qwen3.8-27b · Hugging Face

## 关联链接

- https://omnisbench.fortitude-omnis.group/

## 导航

- 项目页：[[10-项目/github.com_dedbfa22]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
