---
type: "project"
title: "Show HN: I rebuilt Kubernetes for ESP32 microcontrollers"
project_url: "https://github.com/arterialist/kube32"
first_seen: "2026-10-30T09:57:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Arterialist
  - story_50291812
  - show_hn
lang: "en"
---

# Show HN: I rebuilt Kubernetes for ESP32 microcontrollers

> [!info] 一句话导读
> Kubernetes-compatible control plane, Kubelet agent, and WebAssembly runtime for ESP32 microcontrollers

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/arterialist/kube32>
> 首次收录：2026-10-30T09:57:36+08:00
> 来源渠道：HN Show HN
> 标签：author_Arterialist, story_50291812, show_hn
> 最新指标：点赞=5 · 评论=1 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-30/5bb24c0d3aa761c7_Show-HN-I-rebuilt-Kubernetes-for-ESP32-microcontro]] |
| 2026-10-30T09:57:36+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-30/5bb24c0d3aa761c7_Show-HN-I-rebuilt-Kubernetes-for-ESP32-microcontro]] |

## 摘要正文

# arterialist/kube32  Kubernetes-compatible control plane, Kubelet agent, and WebAssembly runtime for ESP32 microcontrollers  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: Apache License 2.0 - Default branch: main - Created: 2026-10-26T06:37:45Z  ## Languages  - C - C++ - CMake - CSS - Go - HTML - JavaScript - Makefile - Python - Rust - Shell  ## Topics  - distributed-computing - edge-computing - embedded - esp32 - freertos - iot - kubectl - kubernetes - wasm - webassembly  ## Top Contributors  - arterialist (115 contributions)  ---  ## README  # kube32  CI Docs  kube32 is a Kubernetes-compatible control plane and WebAssembly pod runtime for ESP32-S3 microcontrollers.  `kubectl` and k9s manage a cluster of boards over Wi-Fi or USB serial. Pods are WebAssembly modules executed by the wasm3 interpreter. One firmware image runs on every board. A board with PSRAM acts as the control plane and runs a local kubelet, while boards without PSRAM join as workers. The same sources build `kube32-sim`, a host simulator for macOS and Linux.  ## Features  - Kubernetes API serving Pod, Node, Namespace, Service, Endpoints, EndpointSlice, Ingress, Deployment, DaemonSet, Job, Config…
