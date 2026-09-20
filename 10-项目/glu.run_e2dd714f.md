---
type: "project"
title: "Show HN: One-shot resolve: package managers as graph schedulers (2x faster)"
project_url: "https://glu.run/blog/installing-homebrew-packages-faster"
first_seen: "2026-09-20T09:36:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_henrikklee
  - story_49740792
  - show_hn
lang: "en"
---

# Show HN: One-shot resolve: package managers as graph schedulers (2x faster)

> [!info] 一句话导读
> Published: 2026-09-14

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://glu.run/blog/installing-homebrew-packages-faster>
> 首次收录：2026-09-20T09:36:52+08:00
> 来源渠道：HN Show HN
> 标签：author_henrikklee, story_49740792, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/7ab5fec84621b59c_Show-HN-One-shot-resolve-package-managers-as-graph]] |
| 2026-09-20T09:36:52+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/7ab5fec84621b59c_Show-HN-One-shot-resolve-package-managers-as-graph]] |

## 摘要正文

Published: 2026-09-14 Author: Henrik Klee Published September 14, 2026  Installing Homebrew packages 2.3x faster — glu  # Installing Homebrew packages 2.3x faster  I wanted to know whether Homebrew's packages could be installed faster. So I built a new client for them.  Henrik Klee Published September 14, 2026  Installing a dev tool on macOS is usually just a`brew install` away. It is easy and convenient, but often doesn't feel very fast. A cold install with a large dependency graph can take minutes while logs scroll by.  After using Bun and uv, I kept wondering why installing native Mac packages could not feel just as fast.  "Why doesn't someone just rewrite Homebrew in Rust?"  Eventually I decided to find out. With the help of AI, one weekend should be enough, or so I thought.  Turns out I was very wrong. Weeks later, the weekend project had become glu, a Rust package manager that installs Homebrew's bottles through its own resolver and installer. In end-to-end cold-install benchmarks, it is more than twice as fast as Homebrew on larger package graphs. This is how I got there, and why the Rust rewrite was only one part of it.  Median end-to-end install times, including dependenci…
