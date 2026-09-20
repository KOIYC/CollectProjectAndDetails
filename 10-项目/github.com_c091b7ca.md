---
type: "project"
title: "Show HN: I wrote a program that hashes files into poems"
project_url: "https://github.com/alebeck/rhymesum"
first_seen: "2026-09-21T02:52:54+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_0x12A
  - story_48334570
  - show_hn
lang: "en"
---

# Show HN: I wrote a program that hashes files into poems

> [!info] 一句话导读
> Hash files into LLM-generated poems locally

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/alebeck/rhymesum>
> 首次收录：2026-09-21T02:52:54+08:00
> 来源渠道：HN Show HN
> 标签：author_0x12A, story_48334570, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/d0c728293d7cbfc7_Show-HN-I-wrote-a-program-that-hashes-files-into-p]] |
| 2026-09-21T01:43:32+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/d0c728293d7cbfc7_Show-HN-I-wrote-a-program-that-hashes-files-into-p]] |
| 2026-09-21T02:52:54+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/d0c728293d7cbfc7_Show-HN-I-wrote-a-program-that-hashes-files-into-p]] |

## 摘要正文

# alebeck/rhymesum  Hash files into LLM-generated poems locally  - Stars: 7 - Forks: 0 - Watchers: 7 - Open issues: 0 - Default branch: main - Created: 2026-05-06T09:15:16Z  ## Languages  - Assembly - C - C++ - CMake - Cuda - Makefile - Metal - Objective-C - Python - Shell  ## Top Contributors  - alebeck (5 contributions)  ---  ## README  ## `rhymesum` -- Hash files into LLM-generated poems locally  > Note: This is a toy project and far from cryptographically safe, better don't use it in production.  ### What is this? This project lets you fingerprint your files using LLM-generated poems instead of hard-to-remember checksums. It computes a `BLAKE3` hash of the passed file, and based on that injects entropy in both the LLM sampler as well as the prompt itself. The output is a five-line poem representing a fingerprint of your file.  ### Example outputs  ``` In twilight's hush, a phantom sloped Across the meadow's trembling rim A fleeting yodel echoed clear As moonlight danced and stars drew near In darkness's silence, all was grim ```  ``` In a lovely abode I rest my head Behind an ancient obelisk I softly tread In the still of night a player draws near She shakes her tambourine and …
