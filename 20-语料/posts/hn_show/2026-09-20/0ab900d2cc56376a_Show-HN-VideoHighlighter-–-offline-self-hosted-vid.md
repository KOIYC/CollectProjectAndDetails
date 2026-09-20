---
type: "corpus"
item_id: "0ab900d2cc56376a"
title: "Show HN: VideoHighlighter – offline self-hosted video analyzer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49704396"
project_url: "https://github.com/Aseiel/VideoHighlighter"
author: "Aseiel"
published_at: "2026-09-14T21:32:06Z"
captured_at: "2026-09-20T09:37:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-14"
tags:
  - 语料
  - hn_show
  - author_Aseiel
  - story_49704396
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: VideoHighlighter – offline self-hosted video analyzer

> [!info] 一句话导读
> Aseiel/VideoHighlighter

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49704396>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Aseiel　|　发布：2026-09-14T21:32:06Z
> 项目链接：<https://github.com/Aseiel/VideoHighlighter>
> 采集：2026-09-20T09:37:34+08:00　|　id：`0ab900d2cc56376a`

## 正文

# Aseiel/VideoHighlighter

Open-source local AI video analyzer powered by Ollama. Visual search, automatic highlights, scene/action/object detection, audio analysis, and subtitle generation. Free, offline alternative to Twelve Labs, Runway, and Descript.

- Stars: 41
- Forks: 2
- Watchers: 41
- Open issues: 1
- License: GNU Affero General Public License v3.0
- Default branch: main
- Created: 2025-09-19T19:10:23Z

## Languages

- Python

## Topics

- action-recognition-dataset
- cuda
- highlight-generation
- llava
- local-ai
- mac
- object-detection-pipelines
- offline-ai
- ollama
- openvino
- scene-detection
- self-hosted
- semantic-search
- subtitle-generation
- video-analysis
- video-search
- video-understanding
- whisper
- windows
- yolo

## Top Contributors

- Aseiel (214 contributions)

---

## README

VideoHighlighter (Freeware)

A Python tool to automatically generate highlight clips from videos using scene detection, motion detection, audio peaks, object detection, action recognition, and transcript analysis.

Features

Detects:
- Scenes using OpenCV.
- Motion peaks and scene changes.
- Objects
- Actions
- Audio peaks.

Generates transcript subtitles via OpenAI Whisper.
Cuts and merges top scoring segments into a highlight video.
Fully configurable: frame skip, highlight duration, keywords.
Optional GUI for easy interaction.

## Preview

VideoHighlighter
Transcript Subtitles
Transcript Subtitles
Visual Search
Action Recognition

Setup & Installation
1. Python & FFmpeg
FFmpeg must be installed and available in your system PATH.

Check FFmpeg installation:
ffmpeg -version

2. Install Python Dependencies
pip install -r requirements.txt

Dependencies include:
numpy, torch, opencv-python, tqdm, ffmpeg-python, openai-whisper, googletrans, openvino-dev
For YOLO object detection: ultralytics
For GUI: PySide6

3. Download Models
The code will automatically download YOLO models on first run.

Usage
Linux: python main.py
Windows: run Videohighlighter.exe

Notes

OpenAI Whisper is MIT licensed — freely usable.

Google Translate API is optional. If using unofficial libraries (googletrans), no API key is needed, but results may break if Google changes endpoints.

This project does not include any paid API keys. Users must provide their own if using official services.

License

This repository is released under the GNU Affero General Public License v3.0 (AGPLv3). You are free to use, modify, and distribute the code, provided that any modified versions, including those offered over a network, make their complete source code available under the same license.

Project Background

This project started as a personal tool to automatically generate subtitles for videos, for my young 7 years old son. Over time, it evolved into a highlights generator for movies, sports, and personal videos.

⚠️ Note: Development may be slow, minimal or none in the future, due to time constraints and family responsibilities. Contributions and improvements from the community are welcome!

The primary goal remains practical: speed up video analysis, generate highlights, and create accessible subtitles automatically.

Stars History

# wg6z0vgevxph1.jpeg

## 导航

- 项目页：[[10-项目/github.com_a5e0ba20]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
