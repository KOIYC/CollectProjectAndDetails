---
type: "project"
title: "Show HN: Offline voice assistant, NO dedicated GPU, less 15Gb RAM"
project_url: "https://grigio.org/offline-voice-assistant-no-dedicated-gpu-less-15gb-ram"
first_seen: "2026-10-11T09:43:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_grigio
  - story_50031212
  - show_hn
lang: "en"
---

# Show HN: Offline voice assistant, NO dedicated GPU, less 15Gb RAM

> [!info] 一句话导读
> Offline voice assistant, NO dedicated GPU, less 15Gb RAM

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://grigio.org/offline-voice-assistant-no-dedicated-gpu-less-15gb-ram>
> 首次收录：2026-10-11T09:43:53+08:00
> 来源渠道：HN Show HN
> 标签：author_grigio, story_50031212, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-11T09:43:53+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-11/21e0e7432657cd1c_Show-HN-Offline-voice-assistant,-NO-dedicated-GPU,]] |

## 摘要正文

Tech blog Blog Github Twitter luigi@grigio.org localai Offline voice assistant, NO dedicated GPU, less 15Gb RAM Luigi 10 Oct 2026  • 2 min read Share Most voice assistants are walkie-talkies. You press, speak, wait. This one keeps the microphone open while it answers, so you can interrupt mid-sentence, change your mind, or correct yourself and get a reaction within one audio buffer. Everything runs locally. No cloud, no accounts, no round-trips, skills and tool-calling supported  What's interesting here  Barge-in has two intensities. A short murmur pauses playback so you can finish; a firm interruption drops the rest of the reply. The history keeps what was already said plus a marker that you cut in, and a quiet "mhmm" doesn't interrupt anything.  Turn-ending is a layered decision, not a timer. A per-frame speech detector, a pause threshold, and a classifier over the last few seconds of your utterance each vote on whether you're done talking. When they disagree, a four-token judge prompt answers LISTEN or REPLY and breaks the tie.  A tool gate sits between the model and your machine. Every round of proposed tool calls is checked against your actual last sentence; anything you didn'…
