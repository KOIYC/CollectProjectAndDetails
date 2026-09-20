---
type: "project"
title: "Show HN: Compress your screenshots for AI coding agents"
project_url: "https://github.com/mgranados/screenshotter"
first_seen: "2026-09-21T02:52:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mgranados
  - story_48346481
  - show_hn
lang: "en"
---

# Show HN: Compress your screenshots for AI coding agents

> [!info] 一句话导读
> mgranados/screenshotter

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/mgranados/screenshotter>
> 首次收录：2026-09-21T02:52:42+08:00
> 来源渠道：HN Show HN
> 标签：author_mgranados, story_48346481, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:27:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/d4fa1ca95200c8e1_Show-HN-Compress-your-screenshots-for-AI-coding-ag]] |
| 2026-09-21T02:52:42+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/d4fa1ca95200c8e1_Show-HN-Compress-your-screenshots-for-AI-coding-ag]] |

## 摘要正文

# mgranados/screenshotter  Small utility to compress screenshots in macos and copy to clipboard  - Stars: 5 - Forks: 0 - Watchers: 5 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-05-31T13:03:04Z  ## Languages  - JavaScript - Swift  ## Top Contributors  - mgranados (1 contributions)  ---  ## README  # screenshotter  npm version license platform  Local macOS screenshots for coding agents.  Take a screenshot. `screenshotter` optimizes it locally and copies it to your clipboard.  ## Preview  screenshotter toolbar output  ## Install  Requires macOS and Node.js 20+.  npm package:  ```sh npm install -g @marttinn/screenshotter screenshotter doctor ```  Try without installing:  ```sh npx @marttinn/screenshotter doctor ```  Development checkout:  ```sh git clone https://github.com/mgranados/screenshotter.git cd screenshotter npm install npm run check node bin/screenshotter.mjs doctor ```  When running from source, replace `screenshotter` with `node bin/screenshotter.mjs`, or symlink it:  ```sh mkdir -p ~/.local/bin ln -sf "$PWD/bin/screenshotter.mjs" ~/.local/bin/screenshotter ```  ## Use  ```sh screenshotter watch --verbose ```  Take a screenshot with `Cmd+S…
