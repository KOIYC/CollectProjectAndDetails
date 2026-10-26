---
type: "project"
title: "Show HN: SQLite-on-object storage using GCS Appendable Objects"
project_url: "https://github.com/fatlotus/sqlite-on-gcs-rapid"
first_seen: "2026-10-26T09:42:36+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_fatlotus
  - story_50235408
  - show_hn
lang: "en"
---

# Show HN: SQLite-on-object storage using GCS Appendable Objects

> [!info] 一句话导读
> Recently, I have been playing around with GCS Rapid, a new API in GCS that lets you append to an existing object. It's pretty fast, and it's cool that you can d…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/fatlotus/sqlite-on-gcs-rapid>
> 首次收录：2026-10-26T09:42:36+08:00
> 来源渠道：HN Show HN
> 标签：author_fatlotus, story_50235408, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-26T09:42:36+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-10-26/0cb047e8bdb3c424_Show-HN-SQLite-on-object-storage-using-GCS-Appenda]] |

## 摘要正文

Recently, I have been playing around with GCS Rapid, a new API in GCS that lets you append to an existing object. It's pretty fast, and it's cool that you can do a log-structured merge tree on top to get a durable database without needing to run a server.Disclaimer: I am a Google employee, but this is not an official Google product. Do not use this code in production; it has 0 production airmiles and was written with AI.
