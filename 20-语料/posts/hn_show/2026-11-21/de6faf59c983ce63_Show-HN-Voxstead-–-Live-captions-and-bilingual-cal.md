---
type: "corpus"
item_id: "de6faf59c983ce63"
title: "Show HN: Voxstead – Live captions and bilingual call assistance for macOS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50584857"
project_url: "https://github.com/TriHerm/voxstead"
author: "abishai33"
published_at: "2026-11-21T01:28:48Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-21"
tags:
  - 语料
  - hn_show
  - author_abishai33
  - story_50584857
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Voxstead – Live captions and bilingual call assistance for macOS

> [!info] 一句话导读
> Live captions, AI reply suggestions for bilingual calls, meeting notes, and voice dictation for macOS. On-device speech recognition in a native Swift app.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50584857>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：abishai33　|　发布：2026-11-21T01:28:48Z
> 项目链接：<https://github.com/TriHerm/voxstead>
> 采集：2026-11-21T14:45:01+08:00　|　id：`de6faf59c983ce63`

## 正文

# TriHerm/voxstead

Live captions, AI reply suggestions for bilingual calls, meeting notes, and voice dictation for macOS. On-device speech recognition in a native Swift app.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Homepage: https://github.com/TriHerm/voxstead/releases/latest
- Default branch: main
- Created: 2026-11-21T00:57:39Z

## Languages

- Python
- Shell
- Swift

## Topics

- ai-assistant
- apple-silicon
- dictation
- live-captions
- macos
- meeting-assistant
- meeting-notes
- on-device-ai
- speaker-diarization
- speech-recognition
- speech-to-text
- swift
- swiftui
- translation

---

## README

# Voxstead

Live captions, bilingual call assistance, meeting notes, and push-to-talk dictation for macOS. Add your goals before a call, follow what the other person says, and ask for a short reply when you need one. Speech recognition runs on your Mac.

## Install

**Apple Silicon · macOS 26 or later**

```sh
brew install --cask triherm/tap/voxstead
```

Or download the **arm64 DMG** from GitHub Releases and drag Voxstead into Applications. This release uses an ad hoc signature. If macOS blocks the first launch, review the app under **System Settings → Privacy & Security**. Each release includes a SHA-256 checksum.

## Try it in a minute

Open **Home → Try an example**. Choose **Continue the conversation**, then **What should I say?** to see a short English reply and its Spanish meaning. The built-in example works without a microphone or AI account.

Voxstead practice meeting with an English–Spanish transcript and a suggested reply based on the agreed budget

## Choose a workflow

| If you want to… | Start here | What you get |
| --- | --- | --- |
| Find the words in a one-on-one call | **Home → Phone call** | Pinned preparation notes, speaker labels, live captions and short replies on demand with **⌘⌥3**. |
| Follow a meeting and act on decisions | **Home → Start a meeting** | Live captions, Catch me up, a debrief and editable action items. |
| Dictate into another app | Hold **Control–Option–D** | Release to transcribe and copy. Enable cursor insertion in **Settings → Recording**. |

### Set up your first call

1. Under **Before the call**, add facts, goals and limits that should guide replies. Choose the language people will speak.
2. For a phone on speaker, select **Microphone only**. For a call on your Mac, select your microphone plus the calling app. **Check audio** previews the inputs.
3. Choose **Start listening**. With microphone-only capture, mark a line you spoke with **That’s me**. With separate inputs, Voxstead labels your microphone **You** and the app audio **Caller**.
4. Read the captions. Press **⌘⌥3** when you want up to two sentences to say aloud. Use **Simpler** for plainer wording or **Clarify** for a question. Choose **End & recap** to review agreements and next steps.

### Audio and AI

Captions and dictation work on-device. Microphone-only speaker detection downloads its model on first use. Allow microphone access for recording and **Screen & System Audio Recording** for audio from another app.

For AI replies and recaps, connect a provider in **Settings → AI providers**. Asking for a reply shares conversation text and preparation notes with that provider. A recap uses the finished transcript. See the user guide for provider options, caption translation, library backups and keyboard shortcuts.

## Build from source

Install Xcode with Swift 6.2 or later, then run from the repository root:

```sh
./script/build_and_run.sh
```

Run the tests with `xcrun swift test`. See the build instructions for packaging and the MIT license for reuse.

# LUMINOL 0.1.1

## 关联链接

- https://github.com/TriHerm/voxstead/releases/latest

## 导航

- 项目页：[[10-项目/github.com_f96baa01]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
