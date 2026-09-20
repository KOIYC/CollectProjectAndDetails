---
type: "project"
title: "Faster JSON parsing with SVE2 on ARM processors"
project_url: "https://lemire.me/blog/2026/09/18/faster-json-parsing-with-sve2-on-arm-processors"
first_seen: "2026-09-20T03:06:43+08:00"
sources:
  - lobsters
tags:
  - 项目
  - lobsters
  - assembly
  - performance
lang: "en"
stale: true
---

# Faster JSON parsing with SVE2 on ARM processors

- **项目链接**：https://lemire.me/blog/2026/09/18/faster-json-parsing-with-sve2-on-arm-processors
- **首次收录**：2026-09-20T03:06:43+08:00
- **来源渠道**：Lobsters
- **标签**：assembly, performance
- **最新指标**：得分=6 · 评论=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:36:26+08:00 | Lobsters | 得分=6 · 评论=1 | [[80-归档/posts/lobsters/2026-09-20/8beb9a3711c21056_Faster-JSON-parsing-with-SVE2-on-ARM-processors]] |
| 2026-09-20T02:48:08+08:00 | Lobsters | 得分=6 · 评论=1 | [[80-归档/posts/lobsters/2026-09-20/8beb9a3711c21056_Faster-JSON-parsing-with-SVE2-on-ARM-processors]] |
| 2026-09-20T02:57:31+08:00 | Lobsters | 得分=6 · 评论=1 | [[80-归档/posts/lobsters/2026-09-20/8beb9a3711c21056_Faster-JSON-parsing-with-SVE2-on-ARM-processors]] |
| 2026-09-20T03:06:43+08:00 | Lobsters | 得分=6 · 评论=1 | [[80-归档/posts/lobsters/2026-09-20/8beb9a3711c21056_Faster-JSON-parsing-with-SVE2-on-ARM-processors]] |

## 摘要正文

Published: 2026-09-18 Author: Author  Daniel Lemire  Faster JSON parsing with SVE2 on ARM processors – Daniel Lemire's blog  # Faster JSON parsing with SVE2 on ARM processors  18 September 2026 · 9 min  ARM processors, like those in your phone, have instructions capable of processing several elements at once (SIMD). These instructions are called NEON. But many newer processors have a different SIMD extension called SVE. The latest ARM processors have SVE2. Unfortunately, Apple has not yet adopted SVE, but SVE processors are available in the cloud.  In April, I wrote that the SVE2 `match` instruction might be the fastest way to match characters on ARM processors. At the time, my benchmark was a toy. The question was whether the idea survives contact with a real parser. Madhurendra Purbay, an engineer at ARM, answered the question with a pull request to the simdjson library. Let me go through what it does and what it buys us.  The simdjson library includes a fast JSON parser. JSON is a ubiquitous data format online; everyone uses it. It is made of strings, numbers, arrays (`[1,2,3]`) and objects. An object is a key-value map where keys are strings, written as `{"key1": 1, "key2": 2}`…
