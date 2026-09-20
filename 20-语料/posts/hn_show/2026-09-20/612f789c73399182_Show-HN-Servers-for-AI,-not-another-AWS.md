---
type: "corpus"
item_id: "612f789c73399182"
title: "Show HN: Servers for AI, not another AWS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49755213"
project_url: "https://rawhq.io/"
author: "eulerpoolapi"
published_at: "2026-09-18T14:49:03Z"
captured_at: "2026-09-20T09:36:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_eulerpoolapi
  - story_49755213
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Servers for AI, not another AWS

> [!info] 一句话导读
> RAW — Servers for AI. 100× cheaper than AWS.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49755213>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：eulerpoolapi　|　发布：2026-09-18T14:49:03Z
> 项目链接：<https://rawhq.io/>
> 采集：2026-09-20T09:36:39+08:00　|　id：`612f789c73399182`

## 正文

RAW — Servers for AI. 100× cheaper than AWS.

100% API — Servers for AI

# Servers for AI, not another AWS.

Create servers. Scale on demand. 100× cheaper, 100× faster, 100× better than AWS. CPU from $9/mo. GPU from $304/mo.

Runs your whole stack

vLLM Ollama PyTorch CUDA Llama Qdrant

## Built for models, agents, and inference

Dedicated GPU and CPU servers you create and scale over a single API. No AWS markup. No shared GPUs. No hypervisor tax.

### LLM inference

vLLM, Ollama, TGI. Dedicated GPUs for Llama, Mistral, DeepSeek. OpenAI-compatible endpoints. 100× cheaper than Bedrock.

### Training & fine-tunes

Full CUDA, 96 GB VRAM, NVMe. Fine-tune LoRA or train from scratch without AWS GPU waitlists.

### AI agents

Create a server, install your agent, scale workers via API. Persistent, root, always-on. From $9/mo.

### Vector databases

Qdrant, pgvector, Milvus on dedicated NVMe. No noisy neighbors eating your recall latency.

### Scale a fleet

POST /deploy in a loop. Resize, rebuild, destroy. 100% API. The anti-AWS console.

### Private AI

Your weights, your GPU, your VPC. GDPR EU regions. Nobody else runs on your hardware.

100% API

## Create a server. Scale it. Done.

One API call provisions real hardware, boots CUDA-ready Linux, and hands you root. Scale with the same endpoint. No consoles. No AWS maze.

- 100% API — create, scale, destroy in JSON
- GPU live in 3 seconds. CUDA, root, public IP
- Per-second billing. Tear the fleet down when the job ends

POST /deploy

$ curl -X POST api.rawhq.io/deploy -d '{"type":"raw-gpu-44"}'

## Everything an AI stack needs

Root, CUDA, NVMe, unlimited bandwidth, and a first-class API on every server. Nothing extra to buy from AWS.

### 100% API

Create, resize, rebuild, and destroy servers over REST. Bearer token. JSON. The anti-AWS console.

### CUDA GPUs

Dedicated NVIDIA cards. vLLM, Ollama, PyTorch. No time-sliced GPUs. No SageMaker lock-in.

### 3-second create

POST /deploy and SSH as root. Faster than AWS even finishes describing the instance.

### Full root

Real Linux. Install anything. Your weights stay on your disk. Nobody else on the box.

### 5 regions

Frankfurt, Dublin, Ashburn, Hillsboro, Singapore. EU GPUs for GDPR inference.

### $0 egress

Unlimited bandwidth included. AWS charges $0.09/GB. One fat model pull and the 100× gap is real.

### Where your agents live

Dedicated CPU for agents, vector DBs, and API gateways. NVMe and unlimited bandwidth included. From a $9 worker to a 48-core cluster.

2 vCPU 4 GB · 40 GB NVMe$9/mo 8 vCPU 16 GB · 160 GB NVMe$21/mo 48 vCPU 192 GB · 960 GB NVMe$1,088/mo

### Where your models run

Dedicated NVIDIA GPUs with full CUDA. vLLM, Ollama, Llama, fine-tunes — 100× cheaper than AWS GPU. No shared cards. EU-ready.

20 GB VRAM inference$304/mo 96 GB VRAM 256 GB RAM · training$1,510/mo 96 GB VRAM 768 GB RAM · max$2,914/mo

## Scale without the AWS tax

Create one GPU. Scale to a fleet. Same API, same price per box, zero egress. 100× cheaper than SageMaker, Bedrock, and EC2 GPU.

100× Cheaper than AWS 3s Create a server 5 Regions worldwide $0 Egress. Forever.

## Built to scale.

The infrastructure and security posture that AI platforms and enterprises trust.

SOC 2 Type II

## 100× cheaper than AWS

One price per server. No egress. No GPU markup. Create and scale from the API.

#### 2 vCPU · 4 GB

40 GB NVMe

$8/mo

#### 4 vCPU · 8 GB

80 GB NVMe

$11/mo

#### 8 vCPU · 16 GB

160 GB NVMe

$21/mo

#### 16 vCPU · 32 GB

320 GB NVMe

$38/mo

#### 32 vCPU · 128 GB

600 GB NVMe

$680/mo

#### 48 vCPU · 192 GB

960 GB NVMe

$1088/mo

## 100× cheaper, faster, better than AWS

What you wish AWS, DigitalOcean, and GPU clouds were. 100% API. Create servers, scale on demand. Dedicated GPUs. $0 egress.

100× cheaper than AWS

3s API to GPU SSH

∞ unlimited bandwidth

$0 egress. Forever.

Built to replace AWS, DigitalOcean, and GPU clouds

| 4 vCPU · 8 GB | RAW#1 for AI | AWS 88× better | GCP 116× better | Azure 85× better | DigitalOcean 10× better | Fly.io 24× better | Render 99× better | Railway 9× better | Vercel 125× better |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Monthly price | $11/mo | $61/mo | $97/mo | $121/mo | $48/mo | $62/mo | $85/mo | ~$100/mo | $20/mo |
| With 1 TB egress | $11/mo | $153/mo | $218/mo | $203/mo | $48/mo | $79/mo | $185/mo | ~$100/mo | $20/mo |
| With 10 TB egress | $11/mo | $973/mo | $1,273/mo | $933/mo | $109/mo | $259/mo | $1,085/mo | Usage | $1,370/mo |
| Instance | raw-4x | t3.large | e2-standard-4 | B4ms | s-4vcpu-8gb | performance-4x | Standard Plus | Pro usage | Pro plan |
| Storage | 80 GB NVMe | 80 GB EBS ($8) | 80 GB SSD ($11) | 80 GB SSD ($10) | 160 GB SSD | 80 GB ($6.40) | 25 GB SSD | Volume extra | None |
| Bandwidth | Unlimited | 100 GB then $0.09/GB | 200 GB then $0.12/GB | 100 GB then $0.08/GB | 4 TB then $0.01/GB | 160 GB then $0.02/GB | 100 GB then $0.10/GB | Usage-based | 1 TB then $0.15/GB |
| Deploy time | 3 seconds | 1–3 min | 1–3 min | 2–4 min | 30–60s | ~30s | 2–5 min | 1–3 min | Build + cold start |
| Root SSH | ✓ Included | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| 100% API | ✓ 1 API to rule them all | Maze of 200+ APIs | Complicated maze | Complicated maze | Partial, extra billing | Limited API | No real API | GraphQL maze | No server API |
| AI / GPU | ✓ from $304/mo | SageMaker tax | Vertex tax | ✓ from $500/mo | ✓ from $700/mo | ✓ from $1,800/mo | ✗ | Usage | ✗ |
| Pricing model | Flat. Done. | Metered maze | Metered maze | Metered maze | Flat-ish | Metered | Metered | Per-minute | Seat + usage |

Same 4 vCPU / 8 GB comparison across every provider. Compute + storage. Bandwidth shown separately. × better is vs RAW at 10 TB egress. Railway from published monthly compute rates.

## Teams that left AWS

> We left SageMaker in a day. Same Llama 70B inference, 100× less bill, real GPUs we actually SSH into.

Daniel K. ML Lead, Linear

> POST /deploy, agents online. No AWS console, no GPU waitlist, no surprise egress. This is how it should work.

James L. AI founder, Apollo

> We scale inference workers from CI. Forty GPUs, one API token. AWS would have taken a quarter and a committee.

Priya R. Platform engineer, Railway

 Install the CLI

## 导航

- 项目页：[[10-项目/rawhq.io_dc82cafd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
