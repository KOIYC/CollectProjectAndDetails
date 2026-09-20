---
type: "corpus"
item_id: "fbc14261f4471f7c"
title: "Show HN: Compute:Arena – Community submitted local AI benchmarks"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49737278"
project_url: "https://computearena.ai/"
author: "prabod"
published_at: "2026-09-17T06:54:31Z"
captured_at: "2026-09-20T14:58:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_prabod
  - story_49737278
  - show_hn
metrics: {"points": 5, "comments": 2, "engagement_velocity": 5}
comments_count: 1
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Compute:Arena – Community submitted local AI benchmarks

> [!info] 一句话导读
> ComputeArena

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49737278>
> 指标：点赞=5 · 评论=2 · engagement_velocity=5
> 作者：prabod　|　发布：2026-09-17T06:54:31Z
> 项目链接：<https://computearena.ai/>
> 采集：2026-09-20T14:58:02+08:00　|　id：`fbc14261f4471f7c`

## 正文

ComputeArena · Edge device benchmarks

# Community submitted benchmarks for Local AI.

Every result comes from a signed report produced on community hardware. Browse by model, quantisation and chip.

Install & start · macOS / Linux

```
curl -LsSf https://computearena.ai/install.sh | sh -s launch
```

Requires curl, tar and Python 3. Review and confirm the installation; the interactive menu opens in this terminal. No sudo required.

## Latest runs

1. Qwen3 4B Reported as Qwen/Qwen3-4B · qwen · default-q4 isu 17 Sep 2026

BaseRT Q4 Apple M5 Pro

89.4 decode

3,325 prefill
2. Gemma 4 E4B IT Reported as google/gemma-4-E4B-it · gemma4 · default-q4 lukas 17 Sep 2026

BaseRT Q4 Apple M5 Max

121.1 decode

8,156 prefill
3. Qwen3.8 27B Reported as Qwen3.8-27B · qwen35 arki05 17 Sep 2026

llama.cpp Q4_0 Tesla T10/Tesla T10/Tesla T10/Tesla T10

47.9 decode

1,129 prefill
4. Qwen3.8 27B Reported as Qwen/Qwen3.8-27B · qwen35 arki05 17 Sep 2026

llama.cpp Q4_K_M Tesla T10/Tesla T10/Tesla T10/Tesla T10

46.6 decode

1,088 prefill
5. Tinystories Lay8 HS512 HD8 33M Reported as ivnle/tinystories-lay8-hs512-hd8-33M · llama · default-q4 arki05 17 Sep 2026

BaseRT Q4 Apple M5 Pro

2,068.0 decode

190,107 prefill
6. Tinystories Lay8 HS512 HD8 33M Reported as RichardErkhov/ivnle_-_tinystories-lay8-hs512-hd8-33M-gguf · llama arki05 17 Sep 2026

llama.cpp Q4_0 Apple M5 Pro

1,443.3 decode

124,181 prefill

How it works

01

### Install ComputeArena

Get the ComputeArena CLI for macOS or Linux, then choose BaseRT or llama.cpp as your runtime.

### Run offline

No account is required. Signed reports remain on your machine until you submit them.

03

### Submit when ready

Sign in, review the data in your saved reports, and submit the benchmarks you want to share publicly.

## Model × quantisation × chip

Headline rankings compare compatible PP512 prefill and TG128 decode workloads. The measured workload is shown beside every result.

| # | Model / quant | Runtime | Chip / backend | Decode tok/s↓ | Prefill tok/s↕ | User | Updated | Share |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Tinystories Lay8 HS512 HD8 33M Reported as ivnle/tinystories-lay8-hs512-hd8-33M · llama · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 2,068.0 TG128 | 190,107 PP512 | arki05 | 17 Sep 2026 | Compare Share Tinystories Lay8 HS512 HD8 33M on Apple M5 Pro |
| 2 | Tinystories Lay8 HS512 HD8 33M Reported as RichardErkhov/ivnle_-_tinystories-lay8-hs512-hd8-33M-gguf · llama Q4_0 | llama.cpp | Apple M5 Pro BLAS + Metal | 1,443.3 TG128 | 124,181 PP512 | arki05 | 17 Sep 2026 | Compare Share Tinystories Lay8 HS512 HD8 33M on Apple M5 Pro |
| 3 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen · default-q4 Q4 | BaseRT | Apple M5 Max Metal | 708.3 TG128 | 34,136 PP512 | prabod | 10 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Max |
| 4 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen · default-q8 Q8 | BaseRT | Apple M5 Max Metal | 549.5 TG128 | 33,088 PP512 | prabod | 10 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Max |
| 5 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 516.8 TG128 | 20,778 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Pro |
| 6 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 508.8 TG128 | 26,137 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 7 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q8_0 | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 479.4 TG128 | 26,346 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 8 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q4_K_M | llama.cpp | Apple M5 Max BLAS + Metal | 439.1 TG128 | 24,365 PP512 | prabod | 10 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Max |
| 9 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q8_0 | llama.cpp | Apple M5 Max BLAS + Metal | 379.0 TG128 | 24,983 PP512 | prabod | 10 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Max |
| 10 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT ROCm | 368.6 TG128 | 23,972 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on AMD Radeon RX 7900 XT |
| 11 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q4_K_M | llama.cpp | Apple M5 Pro BLAS + Metal | 358.3 TG128 | 14,552 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Pro |
| 12 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen · default-q8 Q8 | BaseRT | Apple M5 Pro Metal | 350.2 TG128 | 20,537 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Pro |
| 13 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q8_0 | llama.cpp | AMD Radeon RX 7900 XT ROCm | 313.7 TG128 | 24,691 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on AMD Radeon RX 7900 XT |
| 14 | Gemma 3 1B IT Reported as google/gemma-3-1b-it · gemma3 · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 293.1 TG128 | 15,066 PP512 | arki05 | 11 Sep 2026 | Compare Share Gemma 3 1B IT on Apple M5 Pro |
| 15 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen3 Q8_0 | llama.cpp | Apple M5 Pro BLAS + Metal | 283.0 TG128 | 14,942 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 Pro |
| 16 | Qwen3 1.7B Reported as Qwen/Qwen3-1.7B · qwen · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 235.4 TG128 | 8,040 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 1.7B on Apple M5 Pro |
| 17 | Llama 3.2 3B Instruct Reported as meta-llama/Llama-3.2-3B-Instruct · llama Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 229.7 TG128 | 5,737 PP512 | arki05 | 11 Sep 2026 | Compare Share Llama 3.2 3B Instruct on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 18 | Llama 3.2 1B Instruct Reported as meta-llama/Llama-3.2-1B-Instruct · llama · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 229.1 TG128 | 11,673 PP512 | arki05 | 11 Sep 2026 | Compare Share Llama 3.2 1B Instruct on Apple M5 Pro |
| 19 | Qwen3.5 2B Base Reported as Qwen/Qwen3.5-2B-Base · qwen35 · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 218.2 TG128 | 2,645 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3.5 2B Base on Apple M5 Pro |
| 20 | Qwen3.5 2B Reported as Qwen/Qwen3.5-2B · qwen35 · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 217.7 TG128 | 2,641 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3.5 2B on Apple M5 Pro |
| 21 | Gemma 3 1B IT Reported as google/gemma-3-1b-it · gemma3 · default-q8 Q8 | BaseRT | Apple M5 Pro Metal | 210.3 TG128 | 15,061 PP512 | arki05 | 11 Sep 2026 | Compare Share Gemma 3 1B IT on Apple M5 Pro |
| 22 | Llama 3.2 1B Instruct Reported as meta-llama/Llama-3.2-1B-Instruct · llama · default-q8 Q4 | BaseRT | Apple M5 Pro Metal | 205.3 TG128 | 12,067 PP512 | arki05 | 11 Sep 2026 | Compare Share Llama 3.2 1B Instruct on Apple M5 Pro |
| 23 | Qwen3 30B A3B Instruct 2507 Reported as Qwen/Qwen3-30B-A3B-Instruct-2507 · qwen3moe Q2_K | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 198.1 TG128 | 2,837 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 30B A3B Instruct 2507 on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 24 | Gemma 4 E2B IT Reported as google/gemma-4-E2B-it · gemma4 · default-q4 Q4 | BaseRT | Apple M5 Max Metal | 197.5 TG128 | 20,099 PP512 | lukas | 15 Sep 2026 | Compare Share Gemma 4 E2B IT on Apple M5 Max |
| 25 | GPT-OSS 20B Reported as openai/gpt-oss-20b · gpt-oss Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 195.6 TG128 | 3,292 PP512 | arki05 | 11 Sep 2026 | Compare Share GPT-OSS 20B on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 26 | Qwen3 30B A3B Instruct 2507 Reported as Qwen/Qwen3-30B-A3B-Instruct-2507 · qwen3moe Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 186.7 TG128 | 2,868 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 30B A3B Instruct 2507 on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 27 | Qwen3 4B Instruct 2507 Reported as Qwen/Qwen3-4B-Instruct-2507 · qwen3 Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 185.1 TG128 | 4,793 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 4B Instruct 2507 on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 28 | Qwen3 30B A3B Instruct 2507 Reported as Qwen/Qwen3-30B-A3B-Instruct-2507 · qwen3moe Q3_K_M | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 184.5 TG128 | 2,474 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 30B A3B Instruct 2507 on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 29 | Nemotron 3 Nano 30B A3B Reported as nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 · nemotron_h_moe · default-q4 Q4 | BaseRT | Apple M5 Max Metal | 184.4 TG128 | 4,984 PP512 | lukas | 11 Sep 2026 | Compare Share Nemotron 3 Nano 30B A3B on Apple M5 Max |
| 30 | Qwen2.5 Coder 1.5B Instruct Reported as Qwen/Qwen2.5-Coder-1.5B-Instruct · qwen2 Q4_K_M | llama.cpp | NVIDIA GeForce RTX 4060 Laptop GPU CUDA | 178.8 TG128 | 9,465 PP512 | sarthak247 | 11 Sep 2026 | Compare Share Qwen2.5 Coder 1.5B Instruct on NVIDIA GeForce RTX 4060 Laptop GPU |
| 31 | Qwen3 0.6B Reported as Qwen/Qwen3-0.6B · qwen · default-q4 Q4 | BaseRT | Apple M5 Metal | 172.7 TG128 | 4,997 PP512 | skogul97 | 11 Sep 2026 | Compare Share Qwen3 0.6B on Apple M5 |
| 32 | Llama 3.2 3B Instruct Reported as meta-llama/Llama-3.2-3B-Instruct · llama Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT ROCm | 172.0 TG128 | 6,980 PP512 | arki05 | 11 Sep 2026 | Compare Share Llama 3.2 3B Instruct on AMD Radeon RX 7900 XT |
| 33 | GPT-OSS 20B Reported as openai/gpt-oss-20b · gpt_oss · default-q4 Q4 | BaseRT | Apple M5 Max Metal | 169.0 TG128 | 2,179 PP512 | lukas | 11 Sep 2026 | Compare Share GPT-OSS 20B on Apple M5 Max |
| 34 | Llama 3.2 3B Instruct Reported as meta-llama/Llama-3.2-3B-Instruct · llama Q8_0 | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 167.5 TG128 | 5,846 PP512 | arki05 | 11 Sep 2026 | Compare Share Llama 3.2 3B Instruct on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 35 | GPT-OSS 20B Reported as openai/gpt-oss-20b · gpt-oss Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT ROCm | 160.1 TG128 | 3,502 PP512 | arki05 | 11 Sep 2026 | Compare Share GPT-OSS 20B on AMD Radeon RX 7900 XT |
| 36 | Qwen 0.6B Coder (XformAI) Reported as XformAI-india/qwen-0.6b-coder · qwen3 Q2_K | llama.cpp | Apple M1 Pro BLAS + Metal | 151.6 TG128 | 2,620 PP512 | lukas | 10 Sep 2026 | Compare Share Qwen 0.6B Coder (XformAI) on Apple M1 Pro |
| 37 | Qwen3 8B Reported as Qwen/Qwen3-8B · qwen3 Q2_K | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 150.7 TG128 | 2,563 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 8B on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 38 | Qwen3 4B Instruct 2507 Reported as Qwen/Qwen3-4B-Instruct-2507 · qwen3 Q4_K_M | llama.cpp | AMD Radeon RX 7900 XT ROCm | 147.8 TG128 | 5,364 PP512 | arki05 | 11 Sep 2026 | Compare Share Qwen3 4B Instruct 2507 on AMD Radeon RX 7900 XT |
| 39 | GPT-OSS 20B Reported as openai/gpt-oss-20b · gpt-oss F16 | llama.cpp | AMD Radeon RX 7900 XT (RADV NAVI31) Vulkan | 146.8 TG128 | 3,262 PP512 | arki05 | 11 Sep 2026 | Compare Share GPT-OSS 20B on AMD Radeon RX 7900 XT (RADV NAVI31) |
| 40 | Gemma 4 E2B IT Reported as google/gemma-4-E2B-it · gemma4 · default-q4 Q4 | BaseRT | Apple M5 Pro Metal | 144.6 TG128 | 13,240 PP512 | arki05 | 11 Sep 2026 | Compare Share Gemma 4 E2B IT on Apple M5 Pro |

# AysanZ/alidade

## 评论（1/2）

> **lukasonedge** · 2026-09-17T06:55:49.000Z　
> i didn't recognise some of the models on the frontpage

## 关联链接

- https://computearena.ai/install.sh

## 导航

- 项目页：[[10-项目/computearena.ai_2e94861b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
