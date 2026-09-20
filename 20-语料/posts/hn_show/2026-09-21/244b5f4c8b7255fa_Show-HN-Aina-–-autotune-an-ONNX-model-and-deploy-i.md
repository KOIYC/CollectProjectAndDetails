---
type: "corpus"
item_id: "244b5f4c8b7255fa"
title: "Show HN: Aina – autotune an ONNX model and deploy it across an edge fleet"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49114718"
project_url: "https://github.com/ElhamBadri2411/aina"
author: "e_badri"
published_at: "2026-07-30T19:40:34Z"
captured_at: "2026-09-21T03:11:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_e_badri
  - story_49114718
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Aina – autotune an ONNX model and deploy it across an edge fleet

> [!info] 一句话导读
> Aina: edge ML deployment platform

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49114718>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：e_badri　|　发布：2026-07-30T19:40:34Z
> 项目链接：<https://github.com/ElhamBadri2411/aina>
> 采集：2026-09-21T03:11:12+08:00　|　id：`244b5f4c8b7255fa`

## 正文

# ElhamBadri2411/aina

Aina: edge ML deployment platform

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-07-03T19:14:08Z

## Languages

- CSS
- Dockerfile
- Go
- Go Template
- HTML
- JavaScript
- Makefile
- PLpgSQL
- Python
- Shell
- TypeScript

## Top Contributors

- ElhamBadri2411 (2 contributions)

---

## README

# Aina

Go
TVM
License

**Push an ONNX file. Aina autotunes it for each edge target and rolls it across the fleet. No per-device SSH loop.**

Quickstart · How it works · Why not just use X · Status

---

Your model is trained. Getting it onto the devices takes another six weeks, and that's a tooling gap, not a model problem.

It's not one task, it's a loop: shrink and recompile the model for *this* chip, SCP the artifact to *this* device, SSH in, restart the service, hope it's the right version, then do it all again for the next model and the next hardware target. MLflow, SageMaker, and Kubeflow don't close it. They were built for cloud nodes with 32GB of RAM and a stable network, not 512MB boxes that run TVM-compiled binaries and drop offline.

On yolov8n 640×640, autotuning cuts inference from 3,815 ms to 42 ms in the TVM compile container; the same tuned model serves at ~90 ms on a 2-vCPU edge node. That's the step the manual loop skips, because doing it per device by hand is too painful to bother with.

Aina is the missing layer: **upload → autotune for the target → deploy to the fleet → hot-swap live**, all over an API and a CLI.

## What changes

| Per device, by hand | With Aina, once |
|---|---|
| recompile for each chip | `aina model compile`, autotuned per target |
| `scp` the `.so` to every box | one `deploy` to the whole fleet |
| `ssh` in, restart, pray | hot-swap live, no SSH, no restart |
| "which version is this?" | versioned; roll back with `deploy stop`/`start` |
| repeat per model × per device | one pipeline |

## Quickstart

Zero to a model running on an edge node. Step 1 deploys the whole platform (backend, frontend, Postgres, MinIO, NATS, Prometheus, KubeEdge CloudCore, DB migrations) in a single command.

```bash
# 1. Deploy the platform
./scripts/deploy-helm.sh --vps --build      # bare-IP VPS on k3s
# or: make deploy-helm-local-keep           # local k3d, dashboard at :3001

# 2. Build the CLI, log in
make build-cli && ./aina login

# 3. Upload a model and autotune it for the target
./aina model push yolov8n.onnx --name yolo --version v1
./aina model compile yolo --target "llvm -mcpu=x86-64-v3" --trials 4000 -w

# 4. Onboard a device (prints the one command to run on the Pi/Jetson/VM)
./aina device onboard --name edge-1

# 5. Deploy + start, wait until it's live
./aina deploy create --model yolo_compiled --device edge-1 --start -w
```

Onboard more devices and repeat step 5 per node; `aina model status yolo` streams the live tuning trial count while it compiles.

## How it works

- **Compile = autotune, on Kubernetes.** `compile` spawns a K8s Job that runs Apache TVM MetaSchedule against your LLVM target (x86 AVX or ARM64/Cortex) and can tune on the actual target device, not just the Job's CPU. The source model is never mutated, so you can tune the same ONNX for several targets in parallel. (GPU backends like CUDA are accepted by the API but need a CUDA-enabled TVM image; the stock image is CPU/LLVM only.)
- **Deploy = hot-swap, not SSH.** Deploying publishes a NATS job; the backend delivers the compiled model to the device, which swaps the running model live. No SSH, no manual restart, no "which version is this."
- **Fleet = KubeEdge + auth + metrics.** Devices onboard with a one-shot token, then heartbeat with a per-device secret. The edge runtime exports per-device latency, throughput, errors, and resource usage to Prometheus, rendered on the dashboard.
- **Durable by default.** Compile and deploy are async over NATS JetStream with retries; on restart, stuck jobs self-recover. Deployments have real states (`pending → deploying → running`, plus `stopped`/`failed`) so rollback is `aina deploy stop`/`start`, not a prayer.

## Why not just use KubeEdge / MLflow / SageMaker?

KubeEdge gives you a control plane for edge *pods*. It has no concept of "compile this model for that chip" or "swap the model without restarting the container." MLflow and SageMaker are model registries and cloud training/serving planes; they assume the inference host is a cloud instance you control, not a 512MB box behind a flaky link running a TVM binary. Aina owns the **compile-tune-deploy-observe loop for edge hardware specifically**. It is the part you currently do by hand.

## Status

**v0.1.0** · end-to-end working, deployed on real k3s.

What works:
- ONNX upload → TVM MetaSchedule autotune → MinIO artifact
- **Broad model support:** CNNs (classification, object detection, super-resolution; 1–3 channel, 28→640 px, mnist → yolov8n) *and* standard transformer encoders (whisper-tiny STT: mel → hidden states) all compile and run; autotuning measured **~6.9× faster** on mobilenet (246 → 36 ms) on a 2-vCPU node
- NATS-driven deploy → edge hot-swap → live inference (thread-safe under concurrency) + Prometheus metrics
- CLI (push/compile/deploy/onboard/status) + React dashboard
- Per-user isolation, one-shot onboarding tokens, per-device secrets
- One-command Helm deploy, validated on k3s v1.35 and a QEMU edge fleet; `helm rollback` verified

Not done yet:
- Two model gates: **dynamic input shapes must be pinned to a static shape** before compile (variable-length audio/text fail otherwise), and **very large graphs** (e.g. a full VITS TTS, ~2,700 ops) can be too complex to tune. Op coverage itself is broad: CNNs and standard transformer encoders compile
- A device that restarts loses its loaded model until re-deployed (no automatic re-convergence yet)
- Hosted instance onboarding needs CloudCore ports open and edge image in a public registry
- No TLS, HA replicas, or DB backups wired by default
- Not yet run on a live managed-cloud cluster (chart is API-validated only)

## License & contact

MIT. See LICENSE. Questions or issues: @ElhamBadri2411.

## 导航

- 项目页：[[10-项目/github.com_165497b7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
