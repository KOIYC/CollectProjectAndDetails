---
type: "project"
title: "Show HN: Every satellite that passed over any place this week, and its photos"
project_url: "https://watched.earth/"
first_seen: "2026-11-10T09:49:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_a585gupt
  - story_50428907
  - show_hn
  - front_page
lang: "en"
---

# Show HN: Every satellite that passed over any place this week, and its photos

> [!info] 一句话导读
> hey HN, i built this because i wanted to know what had actually photographed my street.type in any place and it finds every satellite that passed over it in the…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://watched.earth/>
> 首次收录：2026-11-10T09:49:42+08:00
> 来源渠道：HN Show HN
> 标签：author_a585gupt, story_50428907, show_hn, front_page
> 最新指标：点赞=228 · 评论=42 · engagement_velocity=228

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:49:42+08:00 | HN Show HN | 点赞=228 · 评论=42 · engagement_velocity=228 | [[20-语料/posts/hn_show/2026-11-10/e8c8607079b778f1_Show-HN-Every-satellite-that-passed-over-any-place]] |

## 摘要正文

hey HN, i built this because i wanted to know what had actually photographed my street.type in any place and it finds every satellite that passed over it in the last 7 days (SGP4 on the CelesTrak catalog, runs in your browser in about half a second), then pulls the real Sentinel-2 / Landsat / NASA images from those passes.some fun bits: - the pass search can't skip a pass. checked it against a brute force on poles, the antimeridian and tiny swaths: 0 missed - all ~17k objects in orbit are drawn on the GPU, solving Kepler's equation every frame - Sentinel-2 timestamps are often 5-10 min off from when the sat actually crosses your spot, which was a fun one to figure outit only says "watched" if a real image exists, and it doesn't store your location.code: https://github.com/dev-Armaan/satelliteswould love feedback, especially on what data sources to add
