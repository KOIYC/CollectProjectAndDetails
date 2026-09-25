---
type: "project"
title: "Show HN: Fusion-runtime – self-hosted voice agents, STT+LLM+TTS in one process"
project_url: "https://github.com/SamarthUrs18/fusion-runtime"
first_seen: "2026-09-25T00:12:57+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_samarthurs18
  - story_49789320
  - show_hn
lang: "en"
---

# Show HN: Fusion-runtime – self-hosted voice agents, STT+LLM+TTS in one process

> [!info] 一句话导读
> SamarthUrs18/fusion-runtime

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/SamarthUrs18/fusion-runtime>
> 首次收录：2026-09-25T00:12:57+08:00
> 来源渠道：HN Show HN
> 标签：author_samarthurs18, story_49789320, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-22T12:53:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-22/a0f10cafe68ecc41_Show-HN-Fusion-runtime-–-self-hosted-voice-agents,]] |
| 2026-09-25T00:12:57+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-22/a0f10cafe68ecc41_Show-HN-Fusion-runtime-–-self-hosted-voice-agents,]] |

## 摘要正文

# SamarthUrs18/fusion-runtime  Self-hosted voice agent runtime: speech-to-text, an LLM and text-to-speech streaming into each other in one process.  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: Apache License 2.0 - Homepage: https://fusion-runtime.dev - Default branch: main - Created: 2026-09-19T09:59:39Z  ## Languages  - Dockerfile - HTML - JavaScript - Makefile - Python - Shell  ## Top Contributors  - SamarthUrs18 (53 contributions)  ---  ## README  **A self-hosted voice agent runtime.** Speech-to-text, the LLM and text-to-speech run together on one machine and stream into each other, so a reply starts playing while it's still being generated.  **On an RTX 3090 with a 7B model: about 490 ms of processing once a turn ends**, or 991 ms stopwatched from your last syllable — the difference is a silence wait you can configure. 127 tokens/sec, interruptions honoured mid-sentence.  ## Quickstart  Requires Python 3.11–3.13.  ```bash pip install fusion-runtime ```  An agent is one file. This is the whole thing:  ```python # agent.py from fusion_runtime import Agent, LLM, STT, TTS, Turns  agent = Agent(     name="shopkart-orders",     prompt="You are the order line for S…
