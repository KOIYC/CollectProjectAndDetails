---
type: "project"
title: "Show HN: In-Browser Sanskrit ASR Model"
project_url: "https://huggingface.co/gnumanth/sushrota-sanskrit-asr-onnx"
first_seen: "2026-09-20T09:36:58+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_init0
  - story_49731455
  - show_hn
lang: "en"
---

# Show HN: In-Browser Sanskrit ASR Model

> [!info] 一句话导读
> Su-śrotā Sanskrit ASR — ONNX & In-Browser INT8

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://huggingface.co/gnumanth/sushrota-sanskrit-asr-onnx>
> 首次收录：2026-09-20T09:36:58+08:00
> 来源渠道：HN Show HN
> 标签：author_init0, story_49731455, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/be565c01cf616322_Show-HN-In-Browser-Sanskrit-ASR-Model]] |
| 2026-09-20T09:36:58+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-20/be565c01cf616322_Show-HN-In-Browser-Sanskrit-ASR-Model]] |

## 摘要正文

# Su-śrotā Sanskrit ASR — ONNX & In-Browser INT8  This repository provides ONNX and INT8 quantized exports of Su-śrotā (`v13b`), a scholar-grade Sanskrit speech recognition model developed by Prof. Prathosh A P (Indian Institute of Science, Bengaluru).  These models allow running Sanskrit ASR 100% serverless in a web browser (via `onnxruntime-web`) or locally on Mac/Linux/Windows with zero PyTorch/NeMo dependencies.  ## Files in this repository  | File | Size | Description | | --- | --- | --- | | `sushrota_sanskrit_ctc_int8.onnx` | ~178 MB | Conformer-CTC model quantized with INT8 MatMul for browser WASM / WebGPU / CoreML execution | | `preprocessor.onnx` | ~149 KB | Neural Audio-to-Mel-Spectrogram filterbank preprocessor (16 kHz mono PCM $\rightarrow$ 80-mel log spectrogram) | | `sanskrit_vocab.json` | ~3 KB | Tokenizer dictionary mapping 257 CTC output classes to Sanskrit characters/BPE units |  ## Performance  - Parameters: ~115M active parameters (Sanskrit slice of IndicConformer) - Local Mac CPU Latency: ~0.10s for 3.0s audio (RTF: 0.03, ~30x faster than real-time) - In-Browser WebAssembly Latency: ~0.25s for 2.0s audio (RTF: 0.12, ~8x faster than real-time)  ### 1. In-Browser…
