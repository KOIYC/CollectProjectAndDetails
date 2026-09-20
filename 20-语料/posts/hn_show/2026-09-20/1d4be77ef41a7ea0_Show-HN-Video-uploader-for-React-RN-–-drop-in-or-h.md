---
type: "corpus"
item_id: "1d4be77ef41a7ea0"
title: "Show HN: Video uploader for React/RN – drop in or headless UI, any back end"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49741778"
project_url: "https://github.com/hyper-serve/video-uploader"
author: "rtrann"
published_at: "2026-09-17T14:56:43Z"
captured_at: "2026-09-20T09:36:51+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_rtrann
  - story_49741778
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Video uploader for React/RN – drop in or headless UI, any back end

> [!info] 一句话导读
> hyper-serve/video-uploader

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49741778>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rtrann　|　发布：2026-09-17T14:56:43Z
> 项目链接：<https://github.com/hyper-serve/video-uploader>
> 采集：2026-09-20T09:36:51+08:00　|　id：`1d4be77ef41a7ea0`

## 正文

# hyper-serve/video-uploader

Multi-video uploads for React and React Native. Drop zone, file list, progress tracking, retries, and validation, out of the box.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Homepage: https://videouploader.fyi
- Default branch: main
- Created: 2026-03-02T07:04:54Z

## Languages

- Astro
- CSS
- Dockerfile
- HTML
- JavaScript
- MDX
- TypeScript

## Topics

- react
- react-native
- video
- video-upload

## Top Contributors

- rtman (228 contributions)

---

## README

# @hyperserve/video-uploader

Headless cross-platform video upload for React and React Native. Manage upload state, progress, validation, and status polling — bring your own UI or use the included composable components.

## Packages

| Package | Description |
|---------|-------------|
| `@hyperserve/video-uploader` | Core hooks, state machine, validation |
| `@hyperserve/video-uploader-react` | Web UI components (DropZone, FileList, etc.) |
| `@hyperserve/video-uploader-react-native` | React Native UI components |
| `@hyperserve/video-uploader-adapter-hyperserve` | Official Hyperserve backend adapter |

## Installation

```bash
# Core + web components + Hyperserve adapter
npm install @hyperserve/video-uploader @hyperserve/video-uploader-react @hyperserve/video-uploader-adapter-hyperserve

# React Native
npm install @hyperserve/video-uploader @hyperserve/video-uploader-react-native @hyperserve/video-uploader-adapter-hyperserve
```

## Quick Start

```tsx
import { createHyperserveConfig } from "@hyperserve/video-uploader-adapter-hyperserve";
import { UploadProvider } from "@hyperserve/video-uploader";
import { DropZone, FileList } from "@hyperserve/video-uploader-react";

const config = createHyperserveConfig({
  createUpload: async (file, options) => {
    const raw = (file as import("@hyperserve/video-uploader").WebFileRef).raw;
    return fetch("/api/create-upload", {
      method: "POST",
      body: JSON.stringify({ name: raw.name, size: raw.size, ...options }),
    }).then((r) => r.json());
  },
  completeUpload: async (videoId) => {
    await fetch(`/api/complete-upload/${videoId}`, { method: "POST" });
  },
  // optional: omit if you drive status updates via webhook or SSE instead of polling
  pollVideoStatus: async (videoId) =>
    fetch(`/api/video-status/${videoId}`).then((r) => r.json()),
  uploadOptions: { isPublic: true, resolutions: ["480p", "1080p"] },
});

export function App() {
  return (
    <UploadProvider config={config}>
      <DropZone supportingText="MP4, WebM, MOV — up to 500 MB" />
      <FileList />
    </UploadProvider>
  );
}
```

## Documentation

Full docs at videouploader.fyi — guides, component API, adapter setup, and custom backend walkthrough.

## License

MIT

## 关联链接

- https://videouploader.fyi

## 导航

- 项目页：[[10-项目/github.com_707d7707]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
