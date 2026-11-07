---
type: "project"
title: "Show HN: ViewFit – Resize images to the size they are rendered at"
project_url: "https://github.com/andrea-bonacci/viewfit"
first_seen: "2026-11-07T09:43:25+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_andrea-bonacci
  - story_50395793
  - show_hn
lang: "en"
---

# Show HN: ViewFit – Resize images to the size they are rendered at

> [!info] 一句话导读
> andrea-bonacci/viewfit

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/andrea-bonacci/viewfit>
> 首次收录：2026-11-07T09:43:25+08:00
> 来源渠道：HN Show HN
> 标签：author_andrea-bonacci, story_50395793, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-07T09:43:25+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-11-07/2e2af3ab65023f68_Show-HN-ViewFit-–-Resize-images-to-the-size-they-a]] |

## 摘要正文

# andrea-bonacci/viewfit  Fit and compress every image to the size it is actually rendered at, using a real headless browser.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-11-05T10:23:14Z  ## Languages  - TypeScript  ## Topics  - automation - avif - cli - developer-tools - frotnend - image-compression - image-optimization - image-resizing - nodejs - npm-package - opensource - performance - playwright - responsive-images - sharp - tyepscript - web-performance - webp  ## Top Contributors  - andrea-bonacci (19 contributions)  ---  ## README  # ViewFit  Fit and compress every image to the size it is actually rendered at, using a real headless browser.  ViewFit opens your site in Chromium, measures each ` ` and CSS `background-image` with `getBoundingClientRect()`, applies the device pixel ratio, and recommends a per-image target size. Sharp then resizes and compresses each file individually instead of applying one generic setting to everything.  ## Requirements  - Node.js >= 18 - A Chromium browser for Playwright:  - `npx playwright install chromium`, or  - use an installed Google Chrome with `--browser chrome`  ## I…
