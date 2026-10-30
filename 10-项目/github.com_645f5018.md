---
type: "project"
title: "Show HN: Overtone – Transcribe, correct and cut captions for any screen shape"
project_url: "https://github.com/lonthq/overtone-captions"
first_seen: "2026-10-30T09:46:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_rvanderlinden
  - story_50293115
  - show_hn
lang: "en"
---

# Show HN: Overtone – Transcribe, correct and cut captions for any screen shape

> [!info] 一句话导读
> Hi HN, I'm Ruud, co-founder of Lont. We turn company emails into personalized videos.Video captions cost us manual work twice: fixing misheard words, then fixin…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/lonthq/overtone-captions>
> 首次收录：2026-10-30T09:46:09+08:00
> 来源渠道：HN Show HN
> 标签：author_rvanderlinden, story_50293115, show_hn
> 最新指标：点赞=37 · 评论=2 · engagement_velocity=37

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=37 · 评论=2 · engagement_velocity=37 | [[20-语料/posts/hn_show/2026-10-30/94cfdc73cdf2098c_Show-HN-Overtone-–-Transcribe,-correct-and-cut-cap]] |

## 摘要正文

Hi HN, I'm Ruud, co-founder of Lont. We turn company emails into personalized videos.Video captions cost us manual work twice: fixing misheard words, then fixing layout, like lines ending on “the”.Overtone uses multiple models to listen to the audio: gpt-transcribe, Azure STT, and Elevenlabs Scribe. When they return conflicting results, Overtone sends small clips to the models again, and then lets an LLM decide what was actually said.The LLM is like a human doing a sanity check on the transcription model. Humans would easily recognize a word to be different based on context. The LLM basically does the same, using an optional context prompt + its world knowledge. Because of this the Word Error Rate (WER) on many test files is lower when using Overtone, compared to just using a model without it.Sure, the cost is higher because we use up to 3 different STT models + an LLM, but it still removes mistakes, reducing the time needed to fix captions to a minimum, and reducing the chance you'll miss something. For us it's worth it. For ultra high volume use cases it may not be.The rules-based cutter nicely cuts the transcript into captions that look good, depending on screen size: 16:9 is di…
