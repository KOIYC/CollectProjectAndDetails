---
type: "corpus"
item_id: "21e0e7432657cd1c"
title: "Show HN: Offline voice assistant, NO dedicated GPU, less 15Gb RAM"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50031212"
project_url: "https://grigio.org/offline-voice-assistant-no-dedicated-gpu-less-15gb-ram"
author: "grigio"
published_at: "2026-10-10T09:41:13Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_grigio
  - story_50031212
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Offline voice assistant, NO dedicated GPU, less 15Gb RAM

> [!info] 一句话导读
> Offline voice assistant, NO dedicated GPU, less 15Gb RAM

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50031212>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：grigio　|　发布：2026-10-10T09:41:13Z
> 项目链接：<https://grigio.org/offline-voice-assistant-no-dedicated-gpu-less-15gb-ram>
> 采集：2026-10-11T09:43:53+08:00　|　id：`21e0e7432657cd1c`

## 正文

Tech blog
Blog
Github
Twitter
luigi@grigio.org
localai
Offline voice assistant, NO dedicated GPU, less 15Gb RAM
Luigi
10 Oct 2026
 • 2 min read
Share
Most voice assistants are walkie-talkies. You press, speak, wait. This one keeps the microphone open while it answers, so you can interrupt mid-sentence, change your mind, or correct yourself and get a reaction within one audio buffer. Everything runs locally. No cloud, no accounts, no round-trips, skills and tool-calling supported
 What's interesting here
 Barge-in has two intensities. A short murmur pauses playback so you can finish; a firm interruption drops the rest of the reply. The history keeps what was already said plus a marker that you cut in, and a quiet "mhmm" doesn't interrupt anything.
 Turn-ending is a layered decision, not a timer. A per-frame speech detector, a pause threshold, and a classifier over the last few seconds of your utterance each vote on whether you're done talking. When they disagree, a four-token judge prompt answers LISTEN or REPLY and breaks the tie.
 A tool gate sits between the model and your machine. Every round of proposed tool calls is checked against your actual last sentence; anything you didn't ask for is denied with a spoken explanation. This killed a whole class of phantom tool calls that appeared after interruptions.
 Two brains share one conversation. One streams from a locally served model over a standard chat API. The other spawns a coding-agent CLI as a subprocess and inherits its tools, skills, and per-session memory. A checkbox swaps them at runtime.
 History is interrupt-safe. Incomplete tool exchanges are dropped when a turn is cut, so skills aren't re-read every turn. Before each request the history is trimmed to fit the context window, oldest turns first, never the one being answered.
 The model mirrors your language: Italian gets Italian, English gets English, and it follows you when you switch mid-conversation, turn by turn.
 How it's wired
 One hub process owns the 32 ms frame loop, the state machine, all queues, conversation history, and playback pacing. Around it sit three small services, each a configuration of one vendored native server with its own HTTP endpoint and health check.
 Transcription runs full-duplex over a single socket: the client pushes audio and reads streamed partials on the same connection, hand-rolling the raw protocol because request/response can't do this. Synthesis streams audio in 20 ms slices that the hub paces against a clock, which is what lets pause, resume, and flush from a barge-in land within one buffer period. Turn-scoring feeds the hub's votes. The reasoning core is external; the launcher checks its health endpoint and refuses to start otherwise.
 mic (16 kHz) ─► VAD ─► STT :8091 ─► HUB turn-end ─► LLM :8080 / agent CLI
 │
 sentence splitter ─► TTS :8092 ─► paced player
 ▲
 barge-in hooks One socket to the UI carries text events and binary audio in both directions; the newest client wins. Tools include datetime, timers, a notepad, and shell commands behind an approval policy (off / ask / auto), a whitelist, and rejection of chaining or substitution metacharacters. Skills are instruction folders enabled from the UI and never auto-discovered: only the ones you tick reach the prompt, read once per conversation, and their scripts skip the approval prompt. Every setting is an env var from one file; the UI mutates the same object at runtime, and only skill selection persists across restarts.
Featured
Which is the Best Linux terminal? Alacritty, Kitty, Ghostty, Foot, it's not easy
Every few months someone on Reddit declares that the terminal they use is the fastest one. Then someone else posts a benchmark, an argument starts, and everyone goes back to the terminal they already had installed. I spent the last few days collecting benchmarks and reading those arguments on Reddit
06 Oct 2026
 7 min read
Featured
The Linux I always wanted: LabWC with real Wayland blur
I've been after this setup for a long time and it finally works. LabWC, Noctalia shell, and a terminal with actual blur behind it, done through Wayland itself instead of dragging X11 back in.
The Linux ecosystem is fantastic. Open source, freedom, modularity. The catch is that sometimes
05 Oct 2026
 1 min read
Panico paura. 79 bug trovati nel kernel Linux dalla AI
Greg Kroah-Hartman · Kernel Recipes 2026 · 29 settembre 2026 · 57 min Video completo — Kernel Recipes
In sintesi
Anthropic ha annunciato 79 vulnerabilità trovate nel kernel Linux da un suo strumento basato su LLM. Kroah-Hartman, che ha avuto accesso ai dati grezzi, li ha esaminati uno per uno: alla fine
03 Oct 2026
 7 min read
Tech blog © 2026
Sign up
Powered by Ghost

## 导航

- 项目页：[[10-项目/grigio.org_bf73750e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
