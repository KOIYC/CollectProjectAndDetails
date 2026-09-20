---
type: "project"
title: "Show HN: Ear Training Exercise"
project_url: "https://clarena.app/app/try"
first_seen: "2026-09-20T09:36:55+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_AlexFromClarena
  - story_49737154
  - show_hn
lang: "en"
---

# Show HN: Ear Training Exercise

> [!info] 一句话导读
> Clarena

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://clarena.app/app/try>
> 首次收录：2026-09-20T09:36:55+08:00
> 来源渠道：HN Show HN
> 标签：author_AlexFromClarena, story_49737154, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/bdcaa2c6cd8b9bb0_Show-HN-Ear-Training-Exercise]] |
| 2026-09-20T09:36:55+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/bdcaa2c6cd8b9bb0_Show-HN-Ear-Training-Exercise]] |

## 摘要正文

Clarena · Cognitive Practice   // Honor OS dark-mode preference. Inline + synchronous so the dark  // palette is applied BEFORE first paint, preventing a light-flash on  // dark-preferring devices. Reviewer Sonnet 4.6 caught that the dark  // CSS in index.css was previously dead code (no theme switcher).  (function () {  try {  var saved = localStorage.getItem('clarena-theme');  var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;  var theme = saved === 'dark' || saved === 'light'  ? saved  : (prefersDark ? 'dark' : 'light');  document.documentElement.setAttribute('data-theme', theme);  } catch (_) {  // localStorage may be unavailable in private browsing — fall  // through to default (light) gracefully.  }  })();
