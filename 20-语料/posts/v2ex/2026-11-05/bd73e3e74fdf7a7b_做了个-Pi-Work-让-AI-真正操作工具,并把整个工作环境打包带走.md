---
type: "corpus"
item_id: "bd73e3e74fdf7a7b"
title: "做了个 Pi-Work：让 AI 真正操作工具，并把整个工作环境打包带走"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1254549"
project_url: "https://pphboy.github.io/piwork"
author: "pphboy"
published_at: "2026-11-04T13:48:42"
captured_at: "2026-11-05T11:26:05+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 1}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 做了个 Pi-Work：让 AI 真正操作工具，并把整个工作环境打包带走

> [!info] 一句话导读
> 大家好，我是 pphboy https://github.com/pphboy, 一名独立开发者，之前主要做 NAS 、Linux Infra 相关的开发。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1254549>
> 指标：回复=1
> 作者：pphboy　|　发布：2026-11-04T13:48:42
> 项目链接：<https://pphboy.github.io/piwork>
> 采集：2026-11-05T11:26:05+08:00　|　id：`bd73e3e74fdf7a7b`

## 正文

大家好，我是 pphboy https://github.com/pphboy, 一名独立开发者，之前主要做 NAS 、Linux Infra 相关的开发。

这段时间一直在做一个自己的项目：**Pi-Work**。目前 MVP 已经跑通，也录制了 Demo ，今天第一次在 V2EX 分享，希望能找到第一批愿意尝试的用户。

本人录制的使用 Demo

https://www.bilibili.com/video/BV1Uxx16VEYR/?spm_id_from=333.1387.homepage.video_card.click


官网目前的 Demos:
https://pphboy.github.io/piwork/demos/

### 为什么做 Pi-Work ？

现在 AI 已经能够写代码、执行命令、调用各种工具了。

但我一直在思考一个问题：

**如果 AI 不只是一个聊天窗口，而是真正拥有一套可以操作、保存、迁移和分享的工作环境，会怎么样？**

目前很多 AI Agent 依然依赖宿主机的运行环境。换一台电脑，可能又要重新安装依赖、配置工具、处理环境问题。

我希望把这些复杂性尽可能隐藏起来。

### Pi-Work 是什么？

Pi-Work 是一个基于 MicroVM 的 AI 工作环境。

它不是单纯给大模型套一个聊天界面，而是尝试把 AI 的工具执行能力与独立的工作环境结合起来。

目前主要实现了几个方向：

- **独立运行环境**：通过 MicroVM 为 AI 提供可以实际执行命令、操作文件和使用工具的环境。
- **AI 直接操作工具**：用户通过自然语言提出需求，由 AI 在工作环境中执行任务。
- **工作环境打包与迁移**：支持将工作环境导出为 `.work` 文件，在其他机器上导入和继续使用。
- **降低使用门槛**：提供 GUI 和一键安装流程，尽可能减少用户手动配置虚拟机、依赖和开发环境的成本。

我希望未来用户不需要懂 Docker 、Linux 或各种复杂的环境配置，也能直接使用 AI 完成实际工作。

### 技术实现

底层使用 QEMU MicroVM ，主要围绕 KVM / WHPX 等虚拟化能力构建。

选择 MicroVM ，是希望在环境隔离、运行效率和可迁移性之间取得平衡。

当前主要面向 x86-64 环境，后续也考虑支持 macOS / Apple Silicon 。

### 当前进度

目前已经完成了核心 MVP ，包括 AI 操作环境、运行环境管理以及跨机器导入导出的基本闭环。

不过产品还处于早期，UI 、兼容性和使用体验都有需要继续完善的地方。

我不打算等所有功能都完美之后再发布，而是希望开始公开构建，让真实用户的反馈推动后续迭代。

### 项目地址

https://pphboy.github.io/piwork/

### 最后

Pi-Work 的长期目标，是让 AI 不仅能够回答问题，还能真正使用工具完成工作，并且让这些工作环境可以被重复使用和分享。

我个人非常看好 AI Agent ，但也觉得在 Agent 之外，运行环境、工具管理、环境迁移等基础设施同样值得投入。

这也是我选择做 Pi-Work 的原因。

目前最想听到大家的反馈：

1. 你有没有遇到过 AI Agent 环境配置、迁移、复用方面的问题？
2. 你认为这种可以打包分享的 AI 工作环境，有哪些实际使用场景？
3. 如果你愿意尝试 Pi-Work ，目前有哪些问题会阻碍你使用？

欢迎大家提建议，也欢迎直接指出产品设计和技术方案中的问题。

我会继续独立开发、公开构建这个项目。

**Just for fun.**

## 关联链接

- https://github.com/pphboy,
- https://pphboy.github.io/piwork/
- https://pphboy.github.io/piwork/demos/
- https://www.bilibili.com/video/BV1Uxx16VEYR/?spm_id_from=333.1387.homepage.video_card.click

## 导航

- 项目页：[[10-项目/pphboy.github.io_4f225a35]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
