---
type: "project"
title: "Show HN: Jinfer – AI inference engine for the JVM. AI in a jar"
project_url: "https://qxotic.ai/"
first_seen: "2026-09-20T14:07:21+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mukel
  - story_49708628
  - show_hn
lang: "en"
---

# Show HN: Jinfer – AI inference engine for the JVM. AI in a jar

> [!info] 一句话导读
> Some would call AI on the JVM quixotic. And so, Quixotic AI was born.jinfer is an inference engine for the JVM: chat, vision, audio, embeddings, reranking, and …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://qxotic.ai/>
> 首次收录：2026-09-20T14:07:21+08:00
> 来源渠道：HN Show HN
> 标签：author_mukel, story_49708628, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/1ad634403366588e_Show-HN-Jinfer-–-AI-inference-engine-for-the-JVM]] |
| 2026-09-20T14:07:21+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-20/1ad634403366588e_Show-HN-Jinfer-–-AI-inference-engine-for-the-JVM]] |

## 摘要正文

Hi HN, Some would call AI on the JVM quixotic. And so, Quixotic AI was born.jinfer is an inference engine for the JVM: chat, vision, audio, embeddings, reranking, and TTS. No Python runtime, no ONNX, no Docker containers, no sidecar process, no IPC. Finally, AI in a jar.The stack underneath is built for the JVM rather than bolted onto it: toknroll: pure-Java tokenizers, zero dependencies  gguf / safetensors: read and write llama.cpp and HuggingFace model formats  jam: quantized matmul kernels, competitive with llama.cpp on CPU  jota: Tensor API targeting Java, C, CUDA, HIP, Metal, OpenCL, and Mojo  It ships with integrations for Spring AI and LangChain4j, and is compatible with GraalVM Native Image for low-overhead, self-contained binaries with millisecond startup.This is an early release (CPU only): I'd especially like feedback on the API surface.Site: https://qxotic.ai Repo: https://github.com/qxoticai/qxotic
