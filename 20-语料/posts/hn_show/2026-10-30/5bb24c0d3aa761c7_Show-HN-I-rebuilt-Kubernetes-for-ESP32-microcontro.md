---
type: "corpus"
item_id: "5bb24c0d3aa761c7"
title: "Show HN: I rebuilt Kubernetes for ESP32 microcontrollers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50291812"
project_url: "https://github.com/arterialist/kube32"
author: "Arterialist"
published_at: "2026-10-29T16:35:14Z"
captured_at: "2026-10-30T09:57:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_Arterialist
  - story_50291812
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: I rebuilt Kubernetes for ESP32 microcontrollers

> [!info] 一句话导读
> Kubernetes-compatible control plane, Kubelet agent, and WebAssembly runtime for ESP32 microcontrollers

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50291812>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：Arterialist　|　发布：2026-10-29T16:35:14Z
> 项目链接：<https://github.com/arterialist/kube32>
> 采集：2026-10-30T09:57:36+08:00　|　id：`5bb24c0d3aa761c7`

## 正文

# arterialist/kube32

Kubernetes-compatible control plane, Kubelet agent, and WebAssembly runtime for ESP32 microcontrollers

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-10-26T06:37:45Z

## Languages

- C
- C++
- CMake
- CSS
- Go
- HTML
- JavaScript
- Makefile
- Python
- Rust
- Shell

## Topics

- distributed-computing
- edge-computing
- embedded
- esp32
- freertos
- iot
- kubectl
- kubernetes
- wasm
- webassembly

## Top Contributors

- arterialist (115 contributions)

---

## README

# kube32

CI
Docs

kube32 is a Kubernetes-compatible control plane and WebAssembly pod runtime for ESP32-S3 microcontrollers.

`kubectl` and k9s manage a cluster of boards over Wi-Fi or USB serial. Pods are WebAssembly modules executed by the wasm3 interpreter. One firmware image runs on every board. A board with PSRAM acts as the control plane and runs a local kubelet, while boards without PSRAM join as workers. The same sources build `kube32-sim`, a host simulator for macOS and Linux.

## Features

- Kubernetes API serving Pod, Node, Namespace, Service, Endpoints, EndpointSlice, Ingress, Deployment, DaemonSet, Job, ConfigMap, Secret, Lease, Event, and metrics for `kubectl` and k9s, including watch streams, Table output, OpenAPI v3 validation, and log tailing.
- WebAssembly pods in wasm3 with SDKs and templates for Rust, C, and AssemblyScript, using either a request-handler ABI with `k32_handle` or an entry-point ABI with `app_main`, plus configurable memory limits and per-call gas budgets.
- Service routing, HTTP Ingress with host and prefix rules, Server-Sent Events streams, embedded static asset bundles via `k32_resp_asset` and `StaticBundle`, and synchronous pod-to-pod HTTP calls via `k32_http_call`.
- Persistent object store backed by a CRC-checked journal on a raw flash partition or the microSD card, plus `persistentVolumeClaim` pod volumes via `k32_fs_*` and rotated container logs for `kubectl logs --previous`.
- Peripheral access gated per pod by a capability firewall covering GPIO pins, ADC channels, I2C and UART buses, ST7789 display, key matrix, I2S speaker, and microSD storage.
- Container lifecycle management with `restartPolicy` set to `Always`, `OnFailure`, or `Never`, exponential CrashLoopBackOff, and distinct exit codes for Wasm traps, gas exhaustion, and `OOMKilled`.
- Optional bearer-token authentication and automatic self-signed ECDSA P-256 TLS on port 6443.
- Pub/sub events via `k32_event_emit` and `kube32.io/event-topics`, bridged across nodes over ESP-NOW and UDP port 7400.
- Multi-node host simulator `kube32-sim` and `kube32-cli` for building, checking, and deploying pods over the network or to node storage.

## Hardware

| Role | Requirements | Reference board |
| --- | --- | --- |
| Control plane | ESP32-S3, 8 MB flash, 2 MB or more quad SPI PSRAM | Generic ESP32-S3 devkit with 2 MB PSRAM |
| Worker | Any ESP32-S3 with 8 MB flash | M5Stack Cardputer with ST7789 display, keypad, speaker, and microSD |

See docs/hardware-spec.md for pin assignments and memory budgets.

## Quick start

### Simulator

Build and start a two-node cluster on macOS or Linux:

```sh
cmake -S . -B build && cmake --build build -j8
./build/kube32-sim --ingress-port 8080 --pod-port 17000
```

In a second terminal, configure `kubectl` and deploy the echo example:

```sh
export KUBECONFIG=$PWD/build/kubeconfig
kubectl config set-cluster kube32-sim --server=http://127.0.0.1:6443
kubectl config set-context kube32-sim --cluster=kube32-sim
kubectl config use-context kube32-sim
kubectl get nodes
kubectl apply -f examples/echo.yaml
```

### Boards

Build and flash the firmware to each board with PlatformIO:

```sh
pio run -e esp32s3
bash scripts/flash.sh <serial-port> 921600
```

Open the serial console at 115200 baud and provision Wi-Fi and the board profile:

```text
K32_CMD:BOARD:cardputer          # Cardputer worker only
K32_CMD:WIFI:<ssid>:<password>   # both boards
K32_CMD:AP:off                   # control plane
K32_CMD:API:<control-plane-ip>   # worker
```

Point `kubectl` at the control plane IP and apply a manifest:

```sh
kubectl config set-cluster kube32 --server=http://<control-plane-ip>:6443
kubectl config set-context kube32 --cluster=kube32
kubectl config use-context kube32
kubectl get nodes
kubectl apply -f examples/echo.yaml
```

See docs/quickstart.md for full setup instructions and TLS configuration.

## Example: Tessera

Tessera is an issue tracker made of four WebAssembly pods routed by an Ingress. `tessera-web` and `tessera-api` run on the control plane to serve the web UI and in-memory search index. `tessera-db` and `tessera-hud` run on the Cardputer worker to persist records to an append-only log on the microSD card and drive the LCD and keypad (`tessera-hud` is silent by default; sound is opt-in via `HUD_SOUND=1` and the speaker capability).

Generate the sample dataset, upload it to the worker's microSD card, and deploy:

```sh
make -C apps/tessera dataset
tools/kube32-cli push apps/tessera/build/card/kube32/volumes/tessera-db --node <worker-node> --path volumes/tessera-db
kubectl apply -f examples/tessera.yaml
```

Open `http:// /` or `http://127.0.0.1:8080/` on the simulator, and sign in as `mara` with password `demo`.

## Documentation

Full documentation is published at https://arterialist.github.io/kube32/.

- Quick start
- Hardware specification
- Flashing and the serial console
- Writing app pods
- Cluster access and authentication
- Services, Ingress and pod-to-pod calls
- Storage and volumes
- Peripherals
- Example: Tessera
- Architecture overview
- Kubernetes API coverage
- CLI and tools reference

## Contributing

Contributions are welcome. Read CONTRIBUTING.md for build instructions, test suites, and coding guidelines, or open an issue on GitHub.

## Security

See SECURITY.md for the deployment security model and instructions on reporting vulnerabilities privately.

## License

Apache License 2.0. See LICENSE. `third_party/wasm3` is licensed under the MIT License in `third_party/wasm3/LICENSE`.

## 评论（1/1）

> **Arterialist** · 2026-10-29T16:35:14.000Z　
> Hey guys, I had a few esp32 boards around for a while and always thought - how do we go beyond just one device, would it be possible to apply cloud-native thinking to distributed edge computing?Result is Kube32. I got the cluster and a full-stack web app with real-time sync running on esp32 s3 dev board and cardputer - https://7f0c-180-74-71-21.ngrok-free.app/ (may go down) (should support at least a few concurrent users - break it)You won't see one cool thing though, which is the hud pod that uses Cardputer as a keyboard that syncs keystrokes to all clients in real-time.Honestly, it opens so many possibilities for distributed edge computing and multi-device systems. Let me know what use-cases do you think would benefit from kube32 the most.

## 关联链接

- http://127.0.0.1:6443
- http://127.0.0.1:8080/`
- https://arterialist.github.io/kube32/.

## 导航

- 项目页：[[10-项目/github.com_7cfa1e88]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
