---
type: "corpus"
item_id: "d0c728293d7cbfc7"
title: "Show HN: I wrote a program that hashes files into poems"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48334570"
project_url: "https://github.com/alebeck/rhymesum"
author: "0x12A"
published_at: "2026-05-30T10:05:16Z"
captured_at: "2026-09-21T02:52:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_0x12A
  - story_48334570
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:144d"
---

# Show HN: I wrote a program that hashes files into poems

> [!info] 一句话导读
> Hash files into LLM-generated poems locally

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48334570>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：0x12A　|　发布：2026-05-30T10:05:16Z
> 项目链接：<https://github.com/alebeck/rhymesum>
> 采集：2026-09-21T02:52:54+08:00　|　id：`d0c728293d7cbfc7`

## 正文

# alebeck/rhymesum

Hash files into LLM-generated poems locally

- Stars: 7
- Forks: 0
- Watchers: 7
- Open issues: 0
- Default branch: main
- Created: 2026-05-06T09:15:16Z

## Languages

- Assembly
- C
- C++
- CMake
- Cuda
- Makefile
- Metal
- Objective-C
- Python
- Shell

## Top Contributors

- alebeck (5 contributions)

---

## README

## `rhymesum` -- Hash files into LLM-generated poems locally

> Note: This is a toy project and far from cryptographically safe, better don't use it in production.

### What is this?
This project lets you fingerprint your files using LLM-generated poems instead of hard-to-remember checksums. It computes a `BLAKE3` hash of the passed file, and based on that injects entropy in both the LLM sampler as well as the prompt itself. The output is a five-line poem representing a fingerprint of your file.

### Example outputs

```
In twilight's hush, a phantom sloped
Across the meadow's trembling rim
A fleeting yodel echoed clear
As moonlight danced and stars drew near
In darkness's silence, all was grim
```

```
In a lovely abode I rest my head
Behind an ancient obelisk I softly tread
In the still of night a player draws near
She shakes her tambourine and whispers sweet cheer
The stars above twinkle with gentle delight
```

### Build
Build with `make`, then download `meta-llama-3.1-8b-instruct-q4_0.gguf` model using `bash download_model.sh`.

### Run
```
rhymesum <file>
```

### Credits
This project builds heavily on llama.cpp

## 评论（1/1）

> **hereticles** · 2026-05-30T12:19:32.000Z　
> really cool!

## 导航

- 项目页：[[10-项目/github.com_c091b7ca]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
