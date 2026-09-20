---
type: "project"
title: "Show HN: Aina – autotune an ONNX model and deploy it across an edge fleet"
project_url: "https://github.com/ElhamBadri2411/aina"
first_seen: "2026-09-21T03:11:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_e_badri
  - story_49114718
  - show_hn
lang: "en"
---

# Show HN: Aina – autotune an ONNX model and deploy it across an edge fleet

> [!info] 一句话导读
> Aina: edge ML deployment platform

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ElhamBadri2411/aina>
> 首次收录：2026-09-21T03:11:12+08:00
> 来源渠道：HN Show HN
> 标签：author_e_badri, story_49114718, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/244b5f4c8b7255fa_Show-HN-Aina-–-autotune-an-ONNX-model-and-deploy-i]] |
| 2026-09-21T03:11:12+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/244b5f4c8b7255fa_Show-HN-Aina-–-autotune-an-ONNX-model-and-deploy-i]] |

## 摘要正文

# ElhamBadri2411/aina  Aina: edge ML deployment platform  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-07-03T19:14:08Z  ## Languages  - CSS - Dockerfile - Go - Go Template - HTML - JavaScript - Makefile - PLpgSQL - Python - Shell - TypeScript  ## Top Contributors  - ElhamBadri2411 (2 contributions)  ---  ## README  # Aina  Go TVM License  **Push an ONNX file. Aina autotunes it for each edge target and rolls it across the fleet. No per-device SSH loop.**  Quickstart · How it works · Why not just use X · Status  ---  Your model is trained. Getting it onto the devices takes another six weeks, and that's a tooling gap, not a model problem.  It's not one task, it's a loop: shrink and recompile the model for *this* chip, SCP the artifact to *this* device, SSH in, restart the service, hope it's the right version, then do it all again for the next model and the next hardware target. MLflow, SageMaker, and Kubeflow don't close it. They were built for cloud nodes with 32GB of RAM and a stable network, not 512MB boxes that run TVM-compiled binaries and drop offline.  On yolov8n 640×640, autotuning cuts inference from 3,815 …
