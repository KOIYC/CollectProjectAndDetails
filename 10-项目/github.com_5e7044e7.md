---
type: "project"
title: "Show HN: Carmen – harness for reliable AI-written Metal kernels"
project_url: "https://github.com/utsav1033/carmen"
first_seen: "2026-10-27T23:46:32+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_utsav1033
  - story_50259977
  - show_hn
lang: "en"
---

# Show HN: Carmen – harness for reliable AI-written Metal kernels

> [!info] 一句话导读
> An AI writes Apple Metal GPU kernels, a judge it can't fool proves them, and the winners run inside a real model: Qwen 2.5 0.5B decode 3% faster with identical …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/utsav1033/carmen>
> 首次收录：2026-10-27T23:46:32+08:00
> 来源渠道：HN Show HN
> 标签：author_utsav1033, story_50259977, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:46:32+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-27/2ed0cf9106f4cbd1_Show-HN-Carmen-–-harness-for-reliable-AI-written-M]] |

## 摘要正文

# utsav1033/carmen  An AI writes Apple Metal GPU kernels, a judge it can't fool proves them, and the winners run inside a real model: Qwen 2.5 0.5B decode 3% faster with identical output; 75/75 planted bugs caught.  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: MIT License - Homepage: utsav1033.github.io - Default branch: main - Created: 2026-09-24T19:44:26Z  ## Languages  - Metal - Python - Shell  ## Top Contributors  - utsav1033 (82 contributions)  ---  ## README   An LLM writes GPU kernels for Apple Silicon and carmen tests every one.  Then it measures whether a real model on a Mac actually gets faster.   TL;DR ·  The CLI ·  Try it ·  The problem ·  How it works ·  Results ·  What I learned  ## TL;DR  - **Most AI-kernel results are graded by a check that misses a lot.** I planted 75 realistic bugs in GPU kernels: the usual check caught 40. carmen's tests caught all 75. - **The kernels that passed were also faster.** Claude's masked softmax ran **1.82× faster** than Apple's MLX (MLX does it in 3 steps, Claude's in 1), and add + rmsnorm **1.41×**. - **But in a real model they barely mattered:** +2–3% on Qwen 0.5B, nothing on bigger models, because MLX already rea…
