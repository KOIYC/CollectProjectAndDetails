---
type: "project"
title: "Show HN: SyntaxCue – local-first AI interview copilot (whisper.cpp and BYOK)"
project_url: "https://syntaxcue.com/how-syntaxcue-captures-system-audio"
first_seen: "2026-09-20T09:36:54+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_zetbaur
  - story_49738454
  - show_hn
lang: "en"
---

# Show HN: SyntaxCue – local-first AI interview copilot (whisper.cpp and BYOK)

> [!info] 一句话导读
> How SyntaxCue Captures System Audio Locally

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://syntaxcue.com/how-syntaxcue-captures-system-audio>
> 首次收录：2026-09-20T09:36:54+08:00
> 来源渠道：HN Show HN
> 标签：author_zetbaur, story_49738454, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/3eb3be7605ba778d_Show-HN-SyntaxCue-–-local-first-AI-interview-copil]] |
| 2026-09-20T09:36:54+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/3eb3be7605ba778d_Show-HN-SyntaxCue-–-local-first-AI-interview-copil]] |

## 摘要正文

How SyntaxCue Captures System Audio Locally · SyntaxCue  # How SyntaxCue Captures System Audio and Answers You — Without a Server  By SyntaxCue · Updated 2026-08-17 · 8 min read  SyntaxCue turns the audio of a live technical interview into a streamed answer suggestion, on-device, in a few hundred milliseconds — without ever recording the call or sending audio anywhere. This piece walks the whole pipeline: the OS audio API, voice-activity detection, local transcription, and the streamed model response, with the actual APIs and the actual measured numbers. It’s written for a reader who wants to know whether “local transcription, no backend” is a real architectural claim or a marketing one, so most of it is specifics — which CoreAudio call, why an aggregate device, and why Windows once took 25 seconds per transcription when macOS took a fraction of a second.  ## The pipeline, end to end  The system is four stages: capture system audio → cut the continuous stream into utterances → transcribe each utterance locally → send the text to the user’s own LLM and stream the answer back. Capture is the only stage that’s platform-specific. Everything after it is shared code that never learns whi…
