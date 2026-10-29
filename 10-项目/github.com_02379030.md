---
type: "project"
title: "Show HN: LFM3 Video Chat"
project_url: "https://github.com/skorotkiewicz/lfm3-chat"
first_seen: "2026-10-29T20:41:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_modinfo
  - story_50280966
  - show_hn
lang: "en"
---

# Show HN: LFM3 Video Chat

> [!info] 一句话导读
> skorotkiewicz/lfm3-chat

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/skorotkiewicz/lfm3-chat>
> 首次收录：2026-10-29T20:41:52+08:00
> 来源渠道：HN Show HN
> 标签：author_modinfo, story_50280966, show_hn
> 最新指标：点赞=5 · 评论=1 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-29T20:41:52+08:00 | HN Show HN | 点赞=5 · 评论=1 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-29/3cd86e6c41d69843_Show-HN-LFM3-Video-Chat]] |

## 摘要正文

# skorotkiewicz/lfm3-chat  LFM3 video chat  - Stars: 0 - Forks: 1 - Watchers: 0 - Open issues: 0 - Default branch: onnx - Created: 2026-10-28T20:40:18Z  ## Languages  - CSS - HTML - JavaScript - Python  ## Top Contributors  - skorotkiewicz (11 contributions)  ---  ## README  # LFM3 video chat  Talk to LFM3-Omni-2B through your microphone and camera. The model replies with text and audio, and you can interrupt it by speaking or pressing a button.  Start the server and open http://localhost:8000 on the same computer. Camera and microphone access on localhost works without SSL certificates.  An ONNX version is available in `src-onnx/`, with a separate uv environment. Use `q4` for CPU or `q4f16` for NVIDIA GPU. It supports the same camera, voice, and interruption controls without installing PyTorch.  To download ONNX weights separately, use the bundle download commands.  ## Get started  You need uv and a microphone. The project uses Python 3.12. Run these commands from the project folder on the computer hosting the model.  Install the dependencies:  ```bash uv sync ```  Already downloaded the model? Skip the next command and use your existing folder with `--model`. Otherwise, download …
