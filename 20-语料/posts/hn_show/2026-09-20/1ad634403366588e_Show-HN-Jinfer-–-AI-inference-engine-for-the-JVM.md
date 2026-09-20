---
type: "corpus"
item_id: "1ad634403366588e"
title: "Show HN: Jinfer – AI inference engine for the JVM. AI in a jar"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49708628"
project_url: "https://qxotic.ai/"
author: "mukel"
published_at: "2026-09-15T06:42:32Z"
captured_at: "2026-09-20T14:07:21+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_mukel
  - story_49708628
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: Jinfer – AI inference engine for the JVM. AI in a jar

> [!info] 一句话导读
> Some would call AI on the JVM quixotic. And so, Quixotic AI was born.jinfer is an inference engine for the JVM: chat, vision, audio, embeddings, reranking, and …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49708628>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：mukel　|　发布：2026-09-15T06:42:32Z
> 项目链接：<https://qxotic.ai/>
> 采集：2026-09-20T14:07:21+08:00　|　id：`1ad634403366588e`

## 正文

Hi HN,
Some would call AI on the JVM quixotic. And so, Quixotic AI was born.jinfer is an inference engine for the JVM: chat, vision, audio, embeddings, reranking, and TTS. No Python runtime, no ONNX, no Docker containers, no sidecar process, no IPC. Finally, AI in a jar.The stack underneath is built for the JVM rather than bolted onto it: toknroll: pure-Java tokenizers, zero dependencies
 gguf / safetensors: read and write llama.cpp and HuggingFace model formats
 jam: quantized matmul kernels, competitive with llama.cpp on CPU
 jota: Tensor API targeting Java, C, CUDA, HIP, Metal, OpenCL, and Mojo

It ships with integrations for Spring AI and LangChain4j, and is compatible with GraalVM Native Image for low-overhead, self-contained binaries with millisecond startup.This is an early release (CPU only): I'd especially like feedback on the API surface.Site: https://qxotic.ai
Repo: https://github.com/qxoticai/qxotic

## 评论（1/1）

> **exabrial** · 2026-09-18T02:41:28.000Z　
> I just came here to say this is the best project name ever.

## 关联链接

- https://github.com/qxoticai/qxotic
- https://qxotic.ai

## 导航

- 项目页：[[10-项目/qxotic.ai_8d7d8ab7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
