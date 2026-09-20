---
type: "project"
title: "Show HN: OJ – A drop-in replacement for Vite in Rust"
project_url: "https://github.com/lovablelabs/oj"
first_seen: "2026-09-20T14:02:50+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_h1fra
  - story_49746713
  - show_hn
lang: "en"
---

# Show HN: OJ – A drop-in replacement for Vite in Rust

> [!info] 一句话导读
> An experimental Rust-native build tool for React apps.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/lovablelabs/oj>
> 首次收录：2026-09-20T14:02:50+08:00
> 来源渠道：HN Show HN
> 标签：author_h1fra, story_49746713, show_hn
> 最新指标：点赞=17 · 评论=1 · engagement_velocity=17

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=17 · 评论=1 · engagement_velocity=17 | [[20-语料/posts/hn_show/2026-09-20/feb1065cd19b174a_Show-HN-OJ-–-A-drop-in-replacement-for-Vite-in-Rus]] |
| 2026-09-20T09:36:45+08:00 | HN Show HN | 点赞=17 · 评论=1 · engagement_velocity=17 | [[20-语料/posts/hn_show/2026-09-20/feb1065cd19b174a_Show-HN-OJ-–-A-drop-in-replacement-for-Vite-in-Rus]] |
| 2026-09-20T14:02:50+08:00 | HN Show HN | 点赞=17 · 评论=1 · engagement_velocity=17 | [[20-语料/posts/hn_show/2026-09-20/feb1065cd19b174a_Show-HN-OJ-–-A-drop-in-replacement-for-Vite-in-Rus]] |

## 摘要正文

# lovablelabs/oj  An experimental Rust-native build tool for React apps.  - Stars: 454 - Forks: 17 - Watchers: 454 - Open issues: 14 - License: MIT License - Homepage: https://lovable.dev/blog/faster-previews-oj - Default branch: main - Created: 2026-08-08T21:08:40Z  ## Languages  - CSS - HTML - JavaScript - MDX - Nix - Rust - SCSS - TypeScript - Vue  ## Top Contributors  - raphamorim (822 contributions) - williamhogman (82 contributions) - aeriksson (16 contributions) - mikn (9 contributions) - Brumor (2 contributions)  ---  ## README   OJ  OJ is a Rust-native build tool for React apps.  It optimizes for memory and cold start, where running many builds (CI, agents, multi-tenant) under Vite gets expensive. OJ is meant to run real production React apps without changes to their source.  ## Server rendering  There is an SSR mode: `oj dev --ssr src/entry-server.tsx` in dev, and `oj build --ssr` for production. It streams the HTML out with `renderToReadableStream` instead of buffering, and the client hydrates through the normal dev pipeline, so Fast Refresh and HMR keep working over a server-rendered page.  In dev the server modules run in a small persistent Node process (a module runne…
