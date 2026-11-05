---
type: "project"
title: "做了个 Pi-Work：让 AI 真正操作工具，并把整个工作环境打包带走"
project_url: "https://pphboy.github.io/piwork"
first_seen: "2026-11-05T11:26:05+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 做了个 Pi-Work：让 AI 真正操作工具，并把整个工作环境打包带走

> [!info] 一句话导读
> 大家好，我是 pphboy https://github.com/pphboy, 一名独立开发者，之前主要做 NAS 、Linux Infra 相关的开发。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://pphboy.github.io/piwork>
> 首次收录：2026-11-05T11:26:05+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:26:05+08:00 | V2EX | 回复=1 | [[20-语料/posts/v2ex/2026-11-05/bd73e3e74fdf7a7b_做了个-Pi-Work-让-AI-真正操作工具,并把整个工作环境打包带走]] |

## 摘要正文

大家好，我是 pphboy https://github.com/pphboy, 一名独立开发者，之前主要做 NAS 、Linux Infra 相关的开发。  这段时间一直在做一个自己的项目：**Pi-Work**。目前 MVP 已经跑通，也录制了 Demo ，今天第一次在 V2EX 分享，希望能找到第一批愿意尝试的用户。  本人录制的使用 Demo  https://www.bilibili.com/video/BV1Uxx16VEYR/?spm_id_from=333.1387.homepage.video_card.click   官网目前的 Demos: https://pphboy.github.io/piwork/demos/  ### 为什么做 Pi-Work ？  现在 AI 已经能够写代码、执行命令、调用各种工具了。  但我一直在思考一个问题：  **如果 AI 不只是一个聊天窗口，而是真正拥有一套可以操作、保存、迁移和分享的工作环境，会怎么样？**  目前很多 AI Agent 依然依赖宿主机的运行环境。换一台电脑，可能又要重新安装依赖、配置工具、处理环境问题。  我希望把这些复杂性尽可能隐藏起来。  ### Pi-Work 是什么？  Pi-Work 是一个基于 MicroVM 的 AI 工作环境。  它不是单纯给大模型套一个聊天界面，而是尝试把 AI 的工具执行能力与独立的工作环境结合起来。  目前主要实现了几个方向：  - **独立运行环境**：通过 MicroVM 为 AI 提供可以实际执行命令、操作文件和使用工具的环境。 - **AI 直接操作工具**：用户通过自然语言提出需求，由 AI 在工作环境中执行任务。 - **工作环境打包与迁移**：支持将工作环境导出为 `.work` 文件，在其他机器上导入和继续使用。 - **降低使用门槛**：提供 GUI 和一键安装流程，尽可能减少用户手动配置虚拟机、依赖和开发环境的成本。  我希望未来用户不需要懂 Docker 、Linux 或各种复杂的环境配置，也能直接使用 AI 完成实际工作。  ### 技术实现  底层使用 QEMU MicroVM ，主要围绕 KVM / WHPX 等虚拟化能力构建。  选择 MicroVM ，是希望在环境隔离、运行效率和可迁移性之间取得平衡。  当前主要面向 x86-64 环境，后续也考虑支持 macOS / Apple Silicon 。  ### 当前进度  目前已经完成了核心 MVP ，包括 AI 操作环境、运行环境管理以及跨机器导入导出的基本闭环。  不过产品还处于早期，UI 、兼容性和使用体验都有需要继续完善的地方。  我不打算等所有功能…
