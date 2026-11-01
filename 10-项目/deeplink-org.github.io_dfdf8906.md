---
type: "project"
title: "pVisor：面向 Agent 的 docker"
project_url: "https://deeplink-org.github.io/pvisor/zh/benchmarks/lazy-image-startup"
first_seen: "2026-11-01T09:43:04+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# pVisor：面向 Agent 的 docker

> [!info] 一句话导读
> 最近在做 pVisor ，想给跑代码的 Agent 准备一个独立环境：每个任务有自己的 Linux 内核，还能继续用现成的容器镜像和熟悉的命令。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://deeplink-org.github.io/pvisor/zh/benchmarks/lazy-image-startup>
> 首次收录：2026-11-01T09:43:04+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:43:04+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-01/58fc14561d6dc83c_pVisor-面向-Agent-的-docker]] |

## 摘要正文

最近在做 pVisor ，想给跑代码的 Agent 准备一个独立环境：每个任务有自己的 Linux 内核，还能继续用现成的容器镜像和熟悉的命令。  用法大概这样：  ```bash pvisor run --rm alpine:3.20 echo hello ```  这条命令背后启动的是一台 Linux VM 。镜像直接用 OCI 格式，常用的 `run`、`build`、`exec` 都有，不需要启动 Docker daemon 。  另一个想解决的问题是资源占用。跑 Agent 、做评测，项目镜像越攒越多；多个环境同时开着，内存也吃紧。既然用了 VM ，就得想办法减少这些开销。  镜像这边，我们做了压缩内容池和按需读取，避免一直保留完整的解包副本。拿 Alpine 、Ubuntu 和两个 Python slim 镜像在 Linux 上对照，四个镜像的共享库存，Docker 占 **363.16 MiB**，pVisor 占 **94.29 MiB**，少了 **74%**。[测试过程和结果在这里]( https://deeplink-org.github.io/pvisor/zh/benchmarks/lazy-image-startup/)。  内存也做了共享实验：四台 VM 里放重复内容，开启物理共享后，整组内存从 398.92 MiB 降到 149.14 MiB 。[实验详情]( https://deeplink-org.github.io/pvisor/zh/benchmarks/vm-memory/#readback-cost)  想试的话，Python 3.10+ 可以直接装：  ```bash pip install pvisor-sandbox ```  也提供了 Homebrew：  ```bash brew tap DeepLink-org/formula https://github.com/DeepLink-org/Formula.git brew install DeepLink-org/formula/pvisor ```  支持 Linux x86_64 和 Apple Silicon macOS ，[安装文档]( https://deeplink-org.github.io/pvisor/zh/start/installation/)。目前还是开发者预览，Docker 命令和选项只支持一部分，Compose 还不支持。  仓库：[DeepLink-org/pvisor]( https://github.com/DeepLink-org/pvisor)  欢迎试用、提 issue ，也欢迎聊聊跑 Agent 时遇到的各种问题～
