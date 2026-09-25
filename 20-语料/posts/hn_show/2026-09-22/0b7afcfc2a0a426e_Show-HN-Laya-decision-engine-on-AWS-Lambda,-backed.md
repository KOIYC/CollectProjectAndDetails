---
type: "corpus"
item_id: "0b7afcfc2a0a426e"
title: "Show HN: Laya decision engine on AWS Lambda, backed by Lambda SnapStart"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49794281"
project_url: "https://github.com/HQarroum/laymbda"
author: "hqm_"
published_at: "2026-09-21T22:24:57Z"
captured_at: "2026-09-25T00:12:57+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_hqm_
  - story_49794281
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Laya decision engine on AWS Lambda, backed by Lambda SnapStart

> [!info] 一句话导读
> ⚡ Laya engine on AWS Lambda, backed by Lambda SnapStart.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49794281>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：hqm_　|　发布：2026-09-21T22:24:57Z
> 项目链接：<https://github.com/HQarroum/laymbda>
> 采集：2026-09-25T00:12:57+08:00　|　id：`0b7afcfc2a0a426e`

## 正文

# HQarroum/laymbda

⚡ Laya engine on AWS Lambda, backed by Lambda SnapStart.

- Stars: 4
- Forks: 1
- Watchers: 4
- Open issues: 0
- License: MIT License
- Default branch: master
- Created: 2026-09-19T18:14:16Z

## Languages

- Dockerfile
- Python
- TypeScript

## Topics

- ai
- classification
- lambda
- laya
- ml

## Top Contributors

- HQarroum (6 contributions)

---

## README

 Laymbda
 ⚡ The Laya engine running on AWS Lambda.

## What's this ❓

Laymbda is an example of how to run the Laya System-1 decision model on AWS Lambda using a CPU-only, serverless architecture. It is backed by Lambda SnapStart for container functions, which caches and restores initialized Lambda states quickly.

This project uses the AWS Cloud Development Kit (CDK) as the Infrastructure-as-Code layer, and requires Node.js, Docker, npm, and AWS credentials configured for the target account and region.

> All credit goes to the Laya project.

## Architecture

Laymbda has no long-running servers. CDK packages the runtime as an x86-64 container image, Lambda loads Laya during initialization, and SnapStart captures the initialized process when CDK publishes a version.

### Architectural Trade-offs

Using AWS Lambda is not the most conventional choice for running ML workloads due to its resource limits and lack of GPU acceleration.

However, Laya’s encoder-only ModernBERT architecture makes CPU inference practical within Lambda’s execution environment. A serverless, event-driven approach can be effective for bursty, stateless inference workloads where Lambda scales execution environments within the configured concurrency limit, while Snapstart restores the model fast instead of loading it from scratch for every new environment.

It is less suitable though for sustained high-throughput inference requiring a GPU, or applications that require consistently low tail latency.

## 🚀 Quick Start

Run every command in this guide from the project root.

### Install

Install the project dependencies:

```bash
npm ci
```

### Bootstrap

Bootstrap AWS CDK in the target account and Region:

> Bootstrap is required per account and region only once.

```bash
npm run bootstrap
```

#### Deploy

AWS CDK builds the image during deployment using Docker, downloads the pinned Laya checkpoint, pushes the image to ECR, and publishes a SnapStart-enabled Lambda version behind the `live` alias.

```bash
npm run deploy
```

#### Invoke the model

Invoke the `live` alias with the included support-ticket example.

```bash
aws lambda invoke \
  --function-name "$(aws cloudformation describe-stacks \
    --stack-name LaymbdaStack \
    --query "Stacks[0].Outputs[?OutputKey=='LiveAliasArn'].OutputValue" \
    --output text)" \
  --cli-binary-format raw-in-base64-out \
  --payload fileb://examples/support-ticket.json \
  response.json
```

##### Response

The invocation response will be saved in `response.json`.

```bash
cat response.json
```

> See Model invocation for the request format, question types, responses, and validation rules.

## 🧪 Benchmarks

The benchmark used a 4 GB Lambda memory configuration with the Laya model, example payload, and x86-64 runtime with FP16 weights. Sequential requests were sent to a single Lambda container with a maximum concurrency of one.

> AWS Lambda scales the number of vCPUs with the allocated memory.

> SDK retries were disabled for the benchmark.

| Metric | 4 GB x86-64 |
| --- | ---: |
| Warm average latency | 2.022 s |
| Warm p95 latency | 2.051 s |
| Warm p99 latency | 2.087 s |
| Client-observed average | 2.115 s |
| Per-container throughput | 0.470 req/s |
| Peak memory | 3,122 MB |
| SnapStart restore time | 2.445 s |

## 💰 Cost

The estimates use the measured warm duration of the 4 GB x86-64 function in `eu-west-1`. They exclude ECR, observability, data transfer, taxes, and Free Tier discounts. See the AWS Lambda pricing page for regional rates.

> Laymbda sets a reserved concurrency to **10** by default, limiting simultaneous invocations and burst scale-out.

| Cost component | Price |
| --- | ---: |
| Lambda execution | $0.135 per 1,000 requests |
| SnapStart cache | $15.60 per active version per month |
| SnapStart restoration | $0.000559 per restored environment |

## 🧹 Cleanup

```bash
npm run destroy
```

Destroying the stack removes the function, published version, alias, log group, and runtime role. CDK bootstrap assets follow the lifecycle of the bootstrap environment and may remain cached for later deployments.

# Newtdev/blynk-deferlink

## 导航

- 项目页：[[10-项目/github.com_88d0ffdb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
