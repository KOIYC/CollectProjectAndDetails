---
type: "corpus"
item_id: "4020a7dfc4b50e36"
title: "Show HN: OOMU is a free macOS native desktop AI harness (local and cloud)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49850662"
project_url: "https://oomu.ai/download.html"
author: "jeff-oomu"
published_at: "2026-09-25T22:16:22Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_jeff-oomu
  - story_49850662
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: OOMU is a free macOS native desktop AI harness (local and cloud)

> [!info] 一句话导读
> I built OOMU because I honestly got tired of the endless cycle of installing, fixing, updating, fixing, using, fixing the open source harnesses out there like O…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49850662>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：jeff-oomu　|　发布：2026-09-25T22:16:22Z
> 项目链接：<https://oomu.ai/download.html>
> 采集：2026-09-26T09:41:08+08:00　|　id：`4020a7dfc4b50e36`

## 正文

I built OOMU because I honestly got tired of the endless cycle of installing, fixing, updating, fixing, using, fixing the open source harnesses out there like OpenClaw. I also quickly got tired of paying for cloud API tokens.OOMU (https://oomu.ai) isn't just another chatbot. It's a native macOS binary written in Rust and AppKit. It handles real work like interactings with system apps, work in the terminal, and compiling docs like Word, Excel, PowerPoint, and PDF. It can also handle multi-turn tasks locally on your Mac.There is no Electron bloat, no background web services, and it stays 0.0% idle CPU when you are not actually using it.A few key things about how it works:It's as free as you want it to be. The app is free, forever even when we get out of beta. No subscriptions, tiers, or other paid services. You can use it completely through local models with Gemma 4 E2B QAT being the default the app requires at setup (can auto download as part of the setup). If you want to go hybrid, you can also BYOK your own API subscriptions. We've tested with OpenAI, Gemini, DeepSeek, Grok, and Mistral, direct and through aggregators. This is useful if you need to do more demanding work than a local model can handle.One feature I'm most proud of is intelligent auto-routing. A small routing model sits on your machine to determine the complexity of a prompt and whether is should be handled locally or on the cloud. This is a turn-by-turn feature that can select a route automatically for each individual prompt. You must enable this feature, as it is not turned on by default. It can be selected in the chat window. I suspect other harnesses might follow this approach once they figure out that not every prompt needs a frontier model.OOMU prioritizes privacy, has zero telemetry, and everything stays on your Mac in an encrypted local database. There's none of the markdown file mess you get with other commercial and open source harnesses either. It even includes an Air-Gap mode that cuts network access completely.We've localized it into 12 languages right out of the box (English, German, Spanish, French, Japanese, Simplified Chinese, Traditional Chinese, Portuguese, Russian, Ukrainian, Vietnamese, and Indonesian).We are currently on Beta 2 (0.2.16). It is stable and handles daily tasks with relative ease. As with any complex software, I expect a few bugs might pop up here and there. If you run into anything showstopping, I would appreciate your feedback using the built-in bug report form in the app.You can download from https://oomu.ai and the release notes are here https://oomu.ai/release-notes.htmlOr you can also install via Homebrew: brew install --cask oomu-ai/tap/oomuI would love to hear your thoughts, critiques, and how it is working on your local machine.

## 关联链接

- https://oomu.ai
- https://oomu.ai/release-notes.htmlOr

## 导航

- 项目页：[[10-项目/oomu.ai_cae4778c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
