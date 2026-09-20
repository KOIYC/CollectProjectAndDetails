---
type: "corpus"
item_id: "2e5a7c8c493d1a1d"
title: "Show HN: Microsoft Comic Chat (1996) for ChatGPT"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49725890"
project_url: "https://github.com/theletterf/comic-chat-ai/tree/main"
author: "theletterf"
published_at: "2026-09-16T12:26:00Z"
captured_at: "2026-09-20T09:37:04+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_theletterf
  - story_49725890
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Microsoft Comic Chat (1996) for ChatGPT

> [!info] 一句话导读
> Published: 2026-09-16

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49725890>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：theletterf　|　发布：2026-09-16T12:26:00Z
> 项目链接：<https://github.com/theletterf/comic-chat-ai/tree/main>
> 采集：2026-09-20T09:37:04+08:00　|　id：`2e5a7c8c493d1a1d`

## 正文

Published: 2026-09-16
Author: theletterf

GitHub - theletterf/comic-chat-ai: A fork of MS Comic Chat... for AI · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .github | .github | | |
| .vscode | .vscode | | |
| artifacts-modern/ core | artifacts-modern/ core | | |
| artifacts | artifacts | | |
| docs | docs | | |
| scripts | scripts | | |
| v1.0-pre-modern | v1.0-pre-modern | | |
| v1.0-pre/ client | v1.0-pre/ client | | |
| v1.0 | v1.0 | | |
| v2.1b | v2.1b | | |
| v2.5-beta-1-modern | v2.5-beta-1-modern | | |
| v2.5-beta-1 | v2.5-beta-1 | | |
| .gitignore | .gitignore | | |
| CODE_OF_CONDUCT.md | CODE_OF_CONDUCT.md | | |
| CONTRIBUTING.md | CONTRIBUTING.md | | |
| LICENSE | LICENSE | | |
| NOTICE | NOTICE | | |
| README.md | README.md | | |
| SECURITY.md | SECURITY.md | | |
| file dates.txt | file dates.txt | | |
| View all files | | | |

# Comic Chat for AI

Comic Chat for AI is a Windows 11-compatible, GPT-only evolution of Microsoft Comic Chat. It renders conversations with ChatGPT as automatically composed comic strips using the original panel, balloon, avatar, and emotion renderer.

## Download

Download the current Windows build from the GitHub Releases page. Extract the ZIP intact so `CChat.exe` remains next to the `comicart` folder.

Install Codex locally and sign in to ChatGPT. Open the application, choose AI > New Comic Chat, then use the normal message box to talk with ChatGPT.

Codex runs locally and handles the browser sign-in flow. Comic Chat for AI does not include Codex and does not store ChatGPT credentials.

## Build from source

Install Visual Studio 2022 C++ Build Tools with MFC and ATL support, then run these commands from a Developer Command Prompt:

```
call "<VisualStudio>\VC\Auxiliary\Build\vcvars32.bat"
cd v2.5-beta-1-modern
nmake /f chat.mak CFG="chat - Win32 Release"
```

The executable is written to `v2.5-beta-1-modern\Release\CChat.exe`. The application is a 32-bit MFC program and runs on Windows 11 x64.

## Project status

This is an alpha release. It supports ChatGPT through the local Codex runtime, random comic characters, and model-directed character emotions. IRC, legacy server dialogs, member lists, favorites, and legacy help content are removed from the main product flow.

## Attribution and license

Comic Chat for AI is an independent modification of Microsoft Comic Chat. It is not affiliated with, sponsored by, or endorsed by Microsoft or OpenAI.

This is an independent GitHub repository rather than a network fork of the archived upstream project.

The source is available under the MIT License. See LICENSE and NOTICE for the required copyright and attribution notices.

## 导航

- 项目页：[[10-项目/github.com_bf9ceda6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
