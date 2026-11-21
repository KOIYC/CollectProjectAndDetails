---
type: "project"
title: "欢迎共创投稿｜浏览器运行、Mac 适配、批量推理加速，开发者们自发为 OXR 拓展了更多可能"
project_url: "https://free-oxr.somark.cn/feedback"
first_seen: "2026-11-21T14:55:12+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 欢迎共创投稿｜浏览器运行、Mac 适配、批量推理加速，开发者们自发为 OXR 拓展了更多可能

> [!info] 一句话导读
> 上个月，我们开源了文档解析模型 **O****X****R（Optical Everything Recognition）**，并陆续整理和发布了[常见问题解答](https://github.com/SoMarkAI/OXR/blob/main/docs/FAQ_CN.md)，集中回应了大家关心的模型能力、使用环境和…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://free-oxr.somark.cn/feedback>
> 首次收录：2026-11-21T14:55:12+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-21T14:55:12+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-21/7fdf685b5dc17704_欢迎共创投稿-浏览器运行、Mac-适配、批量推理加速,开发者们自发为-OXR-拓展了更多可能]] |

## 摘要正文

上个月，我们开源了文档解析模型 **O****X****R（Optical Everything Recognition）**，并陆续整理和发布了[常见问题解答](https://github.com/SoMarkAI/OXR/blob/main/docs/FAQ_CN.md)，集中回应了大家关心的模型能力、使用环境和部署方式等问题。  不过，FAQ 能把问题讲清楚，真正用起来，还得落到各自的设备和工作流上。  在这件事上，社区已经走在了前面：OXR 直接在浏览器里用 CPU 跑了起来，有人把它适配到了 Mac，也有人为它搭起了批量处理的推理服务，并且都公开了代码、权重和测试数据。  借这篇文章，我们想把这些工作介绍给更多人，也向几位开发者道一声谢谢。  注：以上项目均由社区开发者独立开发和维护，文中数据均来自各项目公开的测试记录。  # 一、浏览器运行：CPU 本地识别  ![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YjRkMDhkNjlkMzkyODZlNmU1NTY3NzUwOTYwZDFiZmVfNTE2MGFjN2I3YTcxNGU5NWNhZWUzYmY1YWQ3YjY4YzBfSUQ6NzcxMDIzMjQ1NDU1MjEyODc4NV8xNzk1MTc4OTAyOjE3OTUyNjUzMDJfVjM)  **oxr\-wasm｜贡献者：andreespirela（Andres Pirela）、fusor\-rs / fusorlabs**  👉 项目地址：[https://github\.com/fusor\-rs/oxr\-wasm](https://github.com/fusor-rs/oxr-wasm)  oxr\-wasm 用 Rust 和 WebAssembly 重新实现了 OXR\-1\.0 的推理流程，使模型可以直接在浏览器中运行。整个识别过程只依赖本机 CPU，不需要服务器或 GPU；模型加载完成后，页面不再发出网络请求，图片始终保留在本地。  为了适应浏览器环境，项目对模型权重做了量化，在保持识别效果的同时将模型体积压缩到了原来的一半以下：在作者的 8 张测试图中，有 7 张的输出与原模型完全一致，另一张仅公式对齐符的位置不同，渲染结果相同。在搭载 M4 Pro 的 Mac 上用 Chrome 运行时，生成速度约为每秒 170–210 个 token。  仓库中提供了在线演示页，可以用 Chrome 或 Edge 访问。首次使用需要下载模型，之后拖入、粘贴或选择图片即可开始识别，结果会逐步显示出来。除了整页解析，也能单独识别文字、…
