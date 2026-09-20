---
type: "corpus"
item_id: "338c1507aa804352"
title: "Show HN: Karen – app feedback as easy as complaining"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49708800"
project_url: "https://github.com/bassimeledath/karen/tree/main"
author: "bombastic311"
published_at: "2026-09-15T07:03:35Z"
captured_at: "2026-09-20T14:57:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_bombastic311
  - story_49708800
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Karen – app feedback as easy as complaining

> [!info] 一句话导读
> Published: 2026-07-21

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49708800>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：bombastic311　|　发布：2026-09-15T07:03:35Z
> 项目链接：<https://github.com/bassimeledath/karen/tree/main>
> 采集：2026-09-20T14:57:50+08:00　|　id：`338c1507aa804352`

## 正文

Published: 2026-07-21
Author: bassimeledath

GitHub - bassimeledath/karen: App feedback as easy as complaining. Point, speak, and give your coding agent the context. A development-only overlay for React apps. · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| assets | assets | | |
| design | design | | |
| examples/ basic | examples/ basic | | |
| src | src | | |
| .gitignore | .gitignore | | |
| INTEGRATION.md | INTEGRATION.md | | |
| OFL-Instrument-Sans.txt | OFL-Instrument-Sans.txt | | |
| README.md | README.md | | |
| package-lock.json | package-lock.json | | |
| package.json | package.json | | |
| tsconfig.json | tsconfig.json | | |
| tsup.config.ts | tsup.config.ts | | |
| vitest.config.ts | vitest.config.ts | | |
| View all files | | | |

Point at something in your app. Say what should change. Karen packages your feedback with component names, source locations, and optional region screenshots—ready to paste into your coding agent.

A development-only overlay for React apps. You bring the opinions and Karen turns it into usable context for your coding agent.

## See her in action

🔊 Sound on. This demo includes spoken feedback.

 karen-demo.mp4

## The feedback loop

1. Point. Click a component or drag over a region.
2. Speak. Say what's off. Edit the transcript, or type instead.
3. Hand it over. Review, copy feedback, and paste it into your local coding agent.

“That button” now comes with context. Karen doesn't edit your code; your agent does.

## Try Karen

Run the included demo locally (Node.js 20.19+; Chrome for browser voice):

```
git clone https://github.com/bassimeledath/karen.git
cd karen
npm install
npm install --prefix examples/basic
npm run dev --prefix examples/basic
```

Open the localhost URL, click Karen, and select something to give feedback on. Allow microphone access when prompted.

Bring her to your app: React + Vite setup, screenshots, and Electron voice →

## A few boundaries

- For development, not production. React source metadata is available when the development tooling exposes it.
- Your agent needs the files. Region screenshots are optional; the included demo saves them locally and copies their paths, not the image pixels. The coding agent needs access to that same filesystem.
- Voice isn't always offline. Browser speech may send audio to the browser's speech service. An optional Whisper provider supports local transcription after its model downloads. Text works without a microphone.
- No npm release yet. The Git repository is `karen`; the package/import is still `feedbasha`. Don't run `npm install feedbasha`—that's an unrelated npm package.

## Built with

React Grab powers Karen's component and source-location lookup. Karen adds voice and text notes, region capture, review, and the feedback handoff. Thanks to Aiden Bai and the React Grab contributors.

Found something that deserves a word? Open an issue.

MIT · Integration reference · Example app

## About

## 关联链接

- https://github.com/bassimeledath/karen.git

## 导航

- 项目页：[[10-项目/github.com_0cccee96]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
