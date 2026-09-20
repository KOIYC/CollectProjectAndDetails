---
type: "project"
title: "Benchmarking Wild vs Mold"
project_url: "https://davidlattimore.github.io/posts/2026/09/18/benchmarking-wild-vs-mold.html"
first_seen: "2026-09-20T03:31:09+08:00"
sources:
  - lobsters
tags:
  - 项目
  - lobsters
  - compilers
  - performance
lang: "en"
stale: true
---

# Benchmarking Wild vs Mold

- **项目链接**：https://davidlattimore.github.io/posts/2026/09/18/benchmarking-wild-vs-mold.html
- **首次收录**：2026-09-20T03:31:09+08:00
- **来源渠道**：Lobsters
- **标签**：compilers, performance
- **最新指标**：得分=51 · 评论=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:36:26+08:00 | Lobsters | 得分=51 · 评论=6 | [[80-归档/posts/lobsters/2026-09-20/dffb6a76ac54d500_Benchmarking-Wild-vs-Mold]] |
| 2026-09-20T02:48:08+08:00 | Lobsters | 得分=51 · 评论=6 | [[80-归档/posts/lobsters/2026-09-20/dffb6a76ac54d500_Benchmarking-Wild-vs-Mold]] |
| 2026-09-20T02:57:31+08:00 | Lobsters | 得分=51 · 评论=6 | [[80-归档/posts/lobsters/2026-09-20/dffb6a76ac54d500_Benchmarking-Wild-vs-Mold]] |
| 2026-09-20T03:06:43+08:00 | Lobsters | 得分=51 · 评论=6 | [[80-归档/posts/lobsters/2026-09-20/dffb6a76ac54d500_Benchmarking-Wild-vs-Mold]] |
| 2026-09-20T03:31:09+08:00 | Lobsters | 得分=51 · 评论=6 | [[80-归档/posts/lobsters/2026-09-20/dffb6a76ac54d500_Benchmarking-Wild-vs-Mold]] |

## 摘要正文

Published: 2026-09-18  Benchmarking Wild vs Mold | David Lattimore  # Benchmarking Wild vs Mold    David Lattimore - 2026-09-18   Mold has recently updated their linker benchmarks and included Wild for the first time. These benchmarks show Wild being substantially slower than Mold in contrast to Wild’s most recently published benchmarks from our last release on August 4th. This post is an attempt to understand why there’s such a difference in the benchmark results.  Mold’s benchmarks were run on two machines:  - A 64 core (128 thread) Threadripper running Ubuntu 24.04 - An Apple M1 Ultra (16 performance cores) running Asahi Linux  Wild’s most recent benchmarks were run on one machine:  - A 16 core (32 thread) Ryzen 9955hx running Ubuntu 26.04  One substantial difference in benchmark configuration is related to the output file. Our benchmarks run with the output file already present from a previous run of the linker. Mold’s benchmarks delete the output file between linker invocations. This can make a substantial difference to the performance of the linker. What difference it makes is also very filesystem dependent. Wild’s benchmarks have historically been run on tmpfs, which was don…
