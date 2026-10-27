---
type: "project"
title: "Rhapsode: a self-hosted speech server that runs eight TTS engines behind one API"
project_url: "https://v.redd.it/2w73i99cq1wh1"
first_seen: "2026-10-27T23:47:55+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SideProject
lang: "en"
---

# Rhapsode: a self-hosted speech server that runs eight TTS engines behind one API

> [!info] 一句话导读
> Rhapsode is like Ollama, but for speech. You install the TTS engines you want, and every client talks to one HTTP API.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://v.redd.it/2w73i99cq1wh1>
> 首次收录：2026-10-27T23:47:55+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SideProject
> 最新指标：得分=4 · 评论=2 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:47:55+08:00 | Reddit 独立开发版块 | 得分=4 · 评论=2 · 赞踩比=1 | [[20-语料/posts/reddit/2026-10-27/0100a43a88cb58d7_Rhapsode-a-self-hosted-speech-server-that-runs-eig]] |

## 摘要正文

Rhapsode is like Ollama, but for speech. You install the TTS engines you want, and every client talks to one HTTP API.  The video is one request per engine to the same server. The voices are Sonny and Tiffani, two hosts from my AI radio station, [deadair.radio](https://deadair.radio). They were designed with a voice-design tool rather than cloned from real people, and I cloned them into every engine that supports cloning. Kokoro and Orpheus can’t clone, so they use their own stock voices. Each card shows the exact text sent, including cue tags like `[laugh]` and `[sigh]`, so you can hear which engines actually perform them.  **Engines:** Chatterbox, Dia, Fish Audio S2 Pro, StyleTTS 2, Breeze, Orpheus and Kokoro.  **Features**  * **Each engine runs in its own process and its own virtualenv**, so one model’s dependencies can’t break another’s, and a crashed worker doesn’t take down the server. * **Automatic model loading and unloading**, since a GPU only holds one model at a time. * **Capability documents.** Each engine reports what it can do with the weights currently loaded (cues, delivery styles, cloning, text limits), so clients never send settings that are silently ignored. * **…
