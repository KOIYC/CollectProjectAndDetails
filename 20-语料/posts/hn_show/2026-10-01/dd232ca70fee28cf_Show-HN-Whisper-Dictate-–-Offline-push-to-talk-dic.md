---
type: "corpus"
item_id: "dd232ca70fee28cf"
title: "Show HN: Whisper Dictate – Offline push-to-talk dictation for Windows and macOS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49912691"
project_url: "https://whisperdictate.vercel.app/"
author: "richard_baecker"
published_at: "2026-09-30T18:41:49Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_richard_baecker
  - story_49912691
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Whisper Dictate – Offline push-to-talk dictation for Windows and macOS

> [!info] 一句话导读
> Whisper Dictate — Offline voice dictation for developers

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49912691>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：richard_baecker　|　发布：2026-09-30T18:41:49Z
> 项目链接：<https://whisperdictate.vercel.app/>
> 采集：2026-10-01T09:41:49+08:00　|　id：`dd232ca70fee28cf`

## 正文

Whisper Dictate — Offline voice dictation for developers

● 100% local & offline — your audio never leaves your machine

# Dictate code and prose. On your own machine.

Hold a hotkey, speak, release — polished text lands at your cursor in any app. NVIDIA speech models run on your GPU. No cloud, no account, no eavesdropping.

 Ctrl+ Shift+ Space dictate (EN) · Ctrl+ Alt+ Space diktieren (DE) · Ctrl+ Shift+ F10 command

 Listening… Transcribing… Typing…

um

 deploy the backup service

scratch that

 ship the backup service

um

 bullet point run the tests”

→“Ship the backup service. • Run the tests”

## Built for people who talk faster than they type

Everything runs on your hardware, post-processed with deterministic, transparent rules — not a black box.

### 🔒 Private by architecture

Audio is transcribed locally by NVIDIA Nemotron streaming models on your GPU (Apple GPU on macOS). Nothing is uploaded — there is no server to upload to.

### ✨ Auto-edits

Filler words are removed, spoken punctuation becomes real punctuation, sentences get capitalized.

“ um hello uh comma world period” → “Hello, world.”

### 🎙️ Command Mode

Hold Ctrl+Shift+F10 and speak a command — it executes instead of typing.

“select all” · “undo that” · “paste” · “delete last word”

### ⚡ Voice shortcuts

Define trigger phrases that expand into full text: emails, addresses, standup updates.

“my email” → “richard@example.com”

### ✂️ Backtrack & scratch

Say “scratch that” mid-dictation and everything before it is dropped. Or undo the last typed block with one hotkey.

### 🇬🇧 🇩🇪 English + German

Two instant profiles with dedicated streaming models. English gets punctuation & casing built in; German gets an explicit de-DE prompt.

### 📚 Your vocabulary

Hotwords, corrections and gitignored personal files teach it your project names, colleagues and jargon — fuzzy-matched so near-misses still land.

### ⌨️ Works in every app

Terminals, editors, chats, mail, browsers — text is pasted at the cursor anywhere you can type.

### 🔔 Quiet sound cues

Five sample-based CC0 sound themes tell you when recording starts, stops and completes. Or mute them.

## Three steps. No cloud round-trip.

Latency is your GPU, not your internet connection.

### Hold the hotkey

EN, DE or Command Mode — the status pill confirms recording started.

### Speak naturally

Fillers, self-corrections and spoken punctuation are all handled.

3

### Release

Polished text is pasted at your cursor in the focused app.

## Simple pricing

One plan, one price — try it free for 14 days, then €40 a year. No word limits, no per-minute metering, local models, local everything.

### Trial

Competitor prices as published September 2026 on wisprflow.ai and superwhisper.com.

## Download

Built binaries are published on GitHub Releases. Pro customers get every update for a year.

### Windows

Windows 10/11 · x64 · NVIDIA GPU recommended (CPU fallback works)

### macOS

macOS 13+ · Apple Silicon (Apple GPU acceleration) · Intel supported

 First run downloads the speech model per language once (~2.4 GB each) — after that it works fully offline. Prefer to build it yourself? The installer does it in one command.

## FAQ

Short answers. The long ones are in the README.

Does my audio ever leave my machine?

No. Recording, transcription and formatting all run locally. The app has no telemetry and no analytics; the only network calls are the one-time model downloads.

What do I need to run it?

Windows 10/11 (NVIDIA GPU recommended — it falls back to CPU automatically) or macOS 13+ on Apple Silicon or Intel. Python is only needed for the source install; the prebuilt binaries are self-contained.

Which languages are supported?

English and German today, each with a dedicated streaming model. The German profile uses NVIDIA's multilingual checkpoint with an explicit de-DE prompt — more languages are a config entry away.

How is this different from Wispr Flow?

Wispr Flow sends your voice to the cloud, meter words on the free tier, and costs $144/year. Whisper Dictate runs the same class of dictation pipeline entirely on your hardware with no word limits, for €40/year.

Can I use it for free?

Free for 14 days — sign up inside the app with just an email, no card needed. After that a Pro license (€40/year) is required; development is funded entirely by Pro.

How do refunds and cancellation work?

Email within 14 days of purchase for a full refund. The license renews yearly through Stripe; cancel any time and you keep access until the period ends.

Is the code open source?

The source is publicly viewable under a source-available license — you can audit exactly what the app does with your audio. Running it beyond the 14-day trial requires the Pro license. See the LICENSE and terms.

# dbb1 radio

## 导航

- 项目页：[[10-项目/whisperdictate.vercel.app_f58f1d0f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
