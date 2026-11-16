---
type: "project"
title: "Show HN: Folate – Local DOM selector model that beats 7B VLMs at 1/60th the size"
project_url: "https://github.com/figranium/folate"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_asernasr
  - story_50507874
  - show_hn
lang: "en"
---

# Show HN: Folate – Local DOM selector model that beats 7B VLMs at 1/60th the size

> [!info] 一句话导读
> A lightweight, CPU-efficient neural DOM element ranker built for browser automation

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/figranium/folate>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_asernasr, story_50507874, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-16/e4ca0aaad4d0d89e_Show-HN-Folate-–-Local-DOM-selector-model-that-bea]] |

## 摘要正文

# figranium/folate  A lightweight, CPU-efficient neural DOM element ranker built for browser automation  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 1 - License: Apache License 2.0 - Default branch: main - Created: 2026-11-14T12:25:04Z  ## Languages  - Python  ## Top Contributors  - asernasr (32 contributions)  ---  ## README   PyPI •  Hugging Face •  Demo •  Apache 2.0   A lightweight, CPU-efficient neural DOM element ranker built for browser automation within tight memory constraints (<2 GB total footprint alongside a headless browser).  Fine-tuned from `google/electra-base-discriminator` on `osunlp/Mind2Web` and dynamically quantized to **INT8 ONNX (~107 MB)**, Folate runs purely via `onnxruntime` and `tokenizers`—requiring no PyTorch or `transformers` at inference time.  ---  ## Model Overview  Folate operates as a discriminative cross-encoder that scores `(natural_language_query, serialized_dom_element)` pairs in a single batched forward pass on CPU.  | Variant / Artifact | Backbone | Precision / Format | Disk Size | Runtime RAM | | :--- | :--- | :--- | :--- | :--- | | **`folate-int8` (Default)** | `google/electra-base-discriminator` | Dynamic `QUInt8` ONNX | ~107 MB | …
