---
type: "corpus"
item_id: "07b06d9a0f347920"
title: "Show HN: Whistle Translator"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50224416"
project_url: "https://mahmoud.sh/whistle-translator"
author: "msdocs"
published_at: "2026-10-24T19:42:59Z"
captured_at: "2026-10-26T00:19:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-24"
tags:
  - 语料
  - hn_show
  - author_msdocs
  - story_50224416
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Whistle Translator

> [!info] 一句话导读
> Speak. Translate. Type anywhere. Offline.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50224416>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：msdocs　|　发布：2026-10-24T19:42:59Z
> 项目链接：<https://mahmoud.sh/whistle-translator>
> 采集：2026-10-26T00:19:08+08:00　|　id：`07b06d9a0f347920`

## 正文

Whistle Translator
 Features
 Install
 Python example
 GitHub
Speak. Translate. Type anywhere. Offline.
An app for Mac and Windows that turns your voice into text and translates it, entirely on your computer. Speak and translate in eight languages, including Arabic, record whole meetings, and hold a shortcut in any app to dictate. Nothing you say ever leaves your computer.
Download for Mac
 Download for Windows
Free · Mac 0.5.1: Apple Silicon, macOS 12 or later, 6.5 MB · Windows 0.4.0: 10 or 11, x64, 5.6 MB
Or with Homebrew : brew install --cask msdocs/tap/whistle-translator
From Detect language ⇄ To German
English Turn off the kitchen lights and set a timer for ten minutes.
German Schalten Sie die Küchenbeleuchtung aus und stellen Sie einen Timer für zehn Minuten ein.
Hold to talk
See you at three tomorrow… → German
Private by design, fast by default
Speech recognition and translation both run on your computer's processor. After a one-time model download, it works on a plane, in a basement, or with Wi-Fi switched off.
Dictate into any app
 Hold ⌥ Space ( Alt+Space on Windows) in Mail, Slack or a browser, speak, release, and your words are typed at the cursor.
Translate as you type
 Hold ⌥ ⇧ Space ( Alt+Shift+Space ) to speak in one language and type in another. A floating pill shows your words as you speak.
Live translation
 See the transcript appear as you talk. Each sentence is translated the moment you finish it.
Nothing leaves your computer
 No account, no cloud, no telemetry. Your audio and text are processed locally and never uploaded.
Hear it back
 Play any translation aloud with your system's built-in voice for that language.
Record meetings
 Meeting mode transcribes for as long as you talk, saves a timestamped transcript and its translation as it goes, and keeps your computer awake until you stop.
Transcribe recordings
 Open a WAV file of any length and get its transcript and translation.
English German French Spanish Italian Dutch Polish Arabic
Install
The app isn't signed by Apple or Microsoft yet, so your computer asks you to confirm it the first time.
Mac, with Homebrew
brew install --cask msdocs/tap/whistle-translator
 Copy
Update with brew upgrade --cask whistle-translator . Uninstall with brew uninstall --zap --cask whistle-translator , which also removes downloaded models and settings.
Mac, or download it
Download the .dmg , open it, and drag Whistle Translator to Applications. (Homebrew does this step for you.)
Open the app. When macOS says it can't verify the developer, click Done .
Go to System Settings → Privacy & Security , scroll to Security, and click Open Anyway . Then open the app again.
Pick your languages. The speech model (17 MB) and each language (about 150–240 MB; Arabic, which brings its own speech model, about 745 MB) download once.
To dictate into other apps, allow it in System Settings → Privacy & Security → Accessibility when asked.
SHA-256 of the 0.5.1 download: b9dd995fe4e45ed2f76fb25b8020c8db0c52380ca11fe4a41be2d0bcefc2a4d5
Prefer Terminal? After copying the app to Applications, xattr -dr com.apple.quarantine "/Applications/Whistle Translator.app" lets it open normally.
Windows
Download the installer and run it.
If Windows SmartScreen says it protected your PC, click More info , then Run anyway .
Pick your languages. The speech model (17 MB) and each language (about 150–240 MB) download once.
Dictate in any app with Alt+Space . No extra permission is needed.
The Windows version is still 0.4.0, which translates into Arabic but can't transcribe spoken Arabic yet; that comes with its next update.
Windows 10 or 11 on x64. SHA-256 of the 0.4.0 installer: 5d462d56543fe3a9580773df89c4c90879f1a57490f4ac25b671dc2731d7e8c1
Start with the Python example
The app grew out of a small Python project: offline speech-to-text and translation in a few lines, from a WAV file, the microphone or a live stream.
whistle-cactus-example →
Whistle and Argos Translate in Python. Transcribe, add word timestamps, and translate between the same seven spoken languages.
Made by Mahmoud Saleh ( @msdocs ) · Speech model and engine © Cactus Compute (Apache-2.0) · Translation models from Argos Translate and OPUS-MT (Tiedemann & Thottingal, EAMT 2020; CC-BY 4.0)

## 评论（1/1）

> **EAtmULFO** · 2026-10-24T20:10:05.000Z　
> I see it's even been ported to ESP32: https://github.com/Xorlent/ESP32P4-Voice

## 导航

- 项目页：[[10-项目/mahmoud.sh_b69a1844]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
