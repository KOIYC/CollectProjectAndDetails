---
type: "project"
title: "Show HN: A patch to make Codex's browser control work in Arc"
project_url: "https://github.com/brianlzhou/arc-browser-use"
first_seen: "2026-10-10T09:53:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_piplupness
  - story_50027194
  - show_hn
lang: "en"
---

# Show HN: A patch to make Codex's browser control work in Arc

> [!info] 一句话导读
> brianlzhou/arc-browser-use

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/brianlzhou/arc-browser-use>
> 首次收录：2026-10-10T09:53:50+08:00
> 来源渠道：HN Show HN
> 标签：author_piplupness, story_50027194, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-10T09:53:50+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-10-10/6ffbc603a9f6e9b7_Show-HN-A-patch-to-make-Codex's-browser-control-wo]] |

## 摘要正文

# brianlzhou/arc-browser-use  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-08T20:19:00Z  ## Languages  - Python  ## Top Contributors  - brianlzhou (2 contributions)  ---  ## README  # Arc Browser Use  Make Codex's browser use work in Arc.  Codex controls browsers through the **Chrome** plugin in the ChatGPT desktop app. In Arc, that connection stalls on the first tab Codex opens. This project fixes that by building a lightly patched copy of OpenAI's ChatGPT extension on your Mac.  Codex's separate **Computer Use** plugin, which operates Mac apps by clicking and typing, doesn't need this project.  ## How it works  Codex reaches a browser through three parts:  1. The **Chrome plugin** in the ChatGPT desktop app. 2. A **native connector** that the plugin installs. Arc finds it in the same place Chrome does, even if Chrome isn't installed. 3. OpenAI's **ChatGPT extension**, running inside the browser.  Only the extension needs changing. It waits for Chrome's tab-group API before it loads each tab, and Arc never answers that API. `arc_browser_use.py build` does these things:  - It downloads the extension from the C…
