---
type: "corpus"
item_id: "0100a43a88cb58d7"
title: "Rhapsode: a self-hosted speech server that runs eight TTS engines behind one API"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1x8d2ns/rhapsode_a_selfhosted_speech_server_that_runs/"
project_url: "https://v.redd.it/2w73i99cq1wh1"
author: "knoxcoder"
published_at: "2026-10-17T23:30:11+08:00"
captured_at: "2026-10-27T23:47:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-17"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 4, "comments": 2, "upvote_ratio": 1}
comments_count: 1
comments_total: 2
discovered_via: "reddit:14d+settle10"
---

# Rhapsode: a self-hosted speech server that runs eight TTS engines behind one API

> [!info] 一句话导读
> Rhapsode is like Ollama, but for speech. You install the TTS engines you want, and every client talks to one HTTP API.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1x8d2ns/rhapsode_a_selfhosted_speech_server_that_runs/>
> 指标：得分=4 · 评论=2 · 赞踩比=1
> 作者：knoxcoder　|　发布：2026-10-17T23:30:11+08:00
> 项目链接：<https://v.redd.it/2w73i99cq1wh1>
> 采集：2026-10-27T23:47:55+08:00　|　id：`0100a43a88cb58d7`

## 正文

Rhapsode is like Ollama, but for speech. You install the TTS engines you want, and every client talks to one HTTP API.

The video is one request per engine to the same server. The voices are Sonny and Tiffani, two hosts from my AI radio station, [deadair.radio](https://deadair.radio). They were designed with a voice-design tool rather than cloned from real people, and I cloned them into every engine that supports cloning. Kokoro and Orpheus can’t clone, so they use their own stock voices. Each card shows the exact text sent, including cue tags like `[laugh]` and `[sigh]`, so you can hear which engines actually perform them.

**Engines:** Chatterbox, Dia, Fish Audio S2 Pro, StyleTTS 2, Breeze, Orpheus and Kokoro.

**Features**

* **Each engine runs in its own process and its own virtualenv**, so one model’s dependencies can’t break another’s, and a crashed worker doesn’t take down the server.
* **Automatic model loading and unloading**, since a GPU only holds one model at a time.
* **Capability documents.** Each engine reports what it can do with the weights currently loaded (cues, delivery styles, cloning, text limits), so clients never send settings that are silently ignored.
* **Separate code and weights licences**, so you can tell whether a model is usable commercially.
* **Voice cloning** from a short clip. StyleTTS 2 managed with 3.6 seconds and no transcript.
* **Dialogue:** Dia speaks two voices in a single take.
* **OpenAI-compatible** `/v1/audio/speech`, plus an **MCP** endpoint for agents.
* **A web page** for installing engines, trying them out and cloning voices.

**Try it**

    curl -fsSLO https://raw.githubusercontent.com/MaroonedSoftware/rhapsode/main/compose.yaml
    docker compose up -d

Then open localhost:8081 to install an engine. Kokoro runs on a plain CPU, so you don’t need a GPU.

* Samples, each clip with its request: [https://rhapsode.dev/docs/samples](https://rhapsode.dev/docs/samples)
* Site: [https://rhapsode.dev](https://rhapsode.dev)
* Code: [https://github.com/MaroonedSoftware/rhapsode](https://github.com/MaroonedSoftware/rhapsode)

It’s MIT licensed and still early. Home Assistant (Wyoming) support is next. Feedback and engine requests are welcome.

*The clips were made on an RTX 4070 Ti SUPER. The Fish Audio clip is Built with Fish Audio, and the Fish and Breeze weights are licensed for non-commercial research only.*

## 评论（1/2）

> **Natethegreat9999**（1 分） · 2026-10-18T04:31:53+08:00　
> The streaming cutter can split 'Dr. Smith' after 'Dr.'. Working on speech at Oruk, I'd keep titles attached to names.

## 关联链接

- https://deadair.radio
- https://github.com/MaroonedSoftware/rhapsode
- https://raw.githubusercontent.com/MaroonedSoftware/rhapsode/main/compose.yaml
- https://rhapsode.dev
- https://rhapsode.dev/docs/samples

## 导航

- 项目页：[[10-项目/v.redd.it_5c5898ad]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
