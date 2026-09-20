---
type: "project"
title: "Show HN: Video as Code for Agents"
project_url: "https://github.com/zPy52/video-as-code-for-agents"
first_seen: "2026-09-21T02:52:22+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_dontoni
  - story_47963817
  - show_hn
lang: "en"
---

# Show HN: Video as Code for Agents

> [!info] 一句话导读
> Published: 2026-04-30

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/zPy52/video-as-code-for-agents>
> 首次收录：2026-09-21T02:52:22+08:00
> 来源渠道：HN Show HN
> 标签：author_dontoni, story_47963817, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/530372d912757b91_Show-HN-Video-as-Code-for-Agents]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/530372d912757b91_Show-HN-Video-as-Code-for-Agents]] |
| 2026-09-21T02:52:22+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/530372d912757b91_Show-HN-Video-as-Code-for-Agents]] |

## 摘要正文

Published: 2026-04-30  # Repository: zPy52/video-as-code-for-agents  Video as code for Agents, based on Remotion and React  - Stars: 3 - Forks: 0 - Watchers: 0 - Open issues: 0 - Primary language: TypeScript - Languages: TypeScript (89.5%), CSS (10.2%), JavaScript (0.2%) - License: Apache License 2.0 (Apache-2.0) - Default branch: main - Created: 2026-04-30T15:01:58Z - Last push: 2026-05-09T13:36:07Z - Contributors: 1 (top: zPy52)  ---  # video-as-code-for-agents  SDK source for building Remotion videos from plain React components.  ## Quickstart  **1. Create a project and install the SDK**  ```bash mkdir my-videos && cd my-videos npm init -y npm install video-as-code-for-agents remotion react react-dom ```  **2. Write your video** (`src/video.tsx`)  ```tsx import { Video, MediaVideo } from 'video-as-code-for-agents';  export default function MyVideo() {   return (     <Video width={1080} height={720} fps={24} duration={7}>       <MediaVideo         start={0}         duration={7}         zIndex={0}         src="./in/clip.mp4"       />     </Video>   ); } ```  **3. Register and render** (`src/index.ts`)  ```ts import Video from './video'; import { exportVideo } from 'video-as-code-f…
