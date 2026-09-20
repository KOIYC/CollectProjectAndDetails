---
type: "project"
title: "Show HN: VisuaLeaf – A Modern MongoDB Workspace"
project_url: "https://visualeaf.com/"
first_seen: "2026-09-21T01:41:47+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Jacky101
  - story_47949733
  - show_hn
lang: "en"
---

# Show HN: VisuaLeaf – A Modern MongoDB Workspace

> [!info] 一句话导读
> Visualeaf is a MongoDB GUI I’ve been building over the past year. Stack is Electron + Angular + Spring Boot. There’s a live playground on the site if you want t…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://visualeaf.com/>
> 首次收录：2026-09-21T01:41:47+08:00
> 来源渠道：HN Show HN
> 标签：author_Jacky101, story_47949733, show_hn
> 最新指标：点赞=9 · 评论=1 · engagement_velocity=9

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=9 · 评论=1 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/1fe5b1e28a0210b3_Show-HN-VisuaLeaf-–-A-Modern-MongoDB-Workspace]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=9 · 评论=1 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/1fe5b1e28a0210b3_Show-HN-VisuaLeaf-–-A-Modern-MongoDB-Workspace]] |
| 2026-09-21T01:41:47+08:00 | HN Show HN | 点赞=9 · 评论=1 · engagement_velocity=9 | [[20-语料/posts/hn_show/2026-09-21/1fe5b1e28a0210b3_Show-HN-VisuaLeaf-–-A-Modern-MongoDB-Workspace]] |

## 摘要正文

Visualeaf is a MongoDB GUI I’ve been building over the past year. Stack is Electron + Angular + Spring Boot. There’s a live playground on the site if you want to try it without installing or putting in your connection (I provided one).The goal was to combine a visual workflow with the depth needed for real development work. Most existing MongoDB tools tend to optimize for either beginners or power users, but not both in the same interface.Core features:Query builder that supports full MongoDB query expressiveness + being able to drag and drop elements from the collection to the query builderForm based aggregation builder with synchronized JSON viewSchema visualization and generation toolsGridFS viewer with MP4 streaming support (streaming mp4 was pretty tricky )IDE style split panels and multiple workspacesImport/export transformations (mask/edit fields during export )Tree view ( finding a way to expand recursively thousands of nodes was a challenge)Table view (I had to build my own take on AG Grid focusing on optimizing horizontal and virtual scrolling to get it to scroll smoothly on thousands of rows and columns)A lot of the work ended up being performance engineering. It current…
