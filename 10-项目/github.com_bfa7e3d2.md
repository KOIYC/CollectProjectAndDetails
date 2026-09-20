---
type: "project"
title: "Show HN: Entropic — information-driven variable-rate media playback"
project_url: "https://github.com/patrickxia/entropic"
first_seen: "2026-09-21T02:52:43+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_pxx
  - story_48346255
  - show_hn
lang: "en"
---

# Show HN: Entropic — information-driven variable-rate media playback

> [!info] 一句话导读
> Entropic: information-driven variable-rate media playback

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/patrickxia/entropic>
> 首次收录：2026-09-21T02:52:43+08:00
> 来源渠道：HN Show HN
> 标签：author_pxx, story_48346255, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/adeb14b7a55e38dd_Show-HN-Entropic-—-information-driven-variable-rat]] |
| 2026-09-21T01:42:38+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/adeb14b7a55e38dd_Show-HN-Entropic-—-information-driven-variable-rat]] |
| 2026-09-21T02:52:43+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-21/adeb14b7a55e38dd_Show-HN-Entropic-—-information-driven-variable-rat]] |

## 摘要正文

# patrickxia/entropic  Entropic: information-driven variable-rate media playback  - Stars: 1 - Forks: 0 - Watchers: 1 - Open issues: 0 - License: GNU General Public License v2.0 - Default branch: main - Created: 2026-05-31T00:51:55Z  ## Languages  - Python  ## Top Contributors  - patrickxia (2 contributions)  ---  ## README  # Entropic: information-driven variable-rate media playback  Variable-rate audio/video playback that slows down for unfamiliar or high-information words and accelerates through predictable speech, using token-level surprisal from a fast local LLM.  * **vbr** (default) targets an average speed while distributing time by information content (watch 2x demo) * **skiplow** keeps speech at 1x and only speeds up low-information segments, like an enhanced skip-silence (watch 1.5x demo)  ## How it works  1. **Transcribe** with WhisperX (word-level timestamps via forced alignment) 1. **Score** each word's surprisal: unigram (word frequency) or contextual (causal LM like distilgpt2/gpt2) 1. **Estimate** each word's confidence using whisper token-level probabilities, optionally from a separate weaker model (`--uncertainty-model`) 1. **Assign speeds** per one of two modes: …
