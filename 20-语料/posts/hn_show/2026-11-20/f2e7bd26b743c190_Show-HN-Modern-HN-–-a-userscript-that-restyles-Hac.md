---
type: "corpus"
item_id: "f2e7bd26b743c190"
title: "Show HN: Modern HN – a userscript that restyles Hacker News"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50563876"
project_url: "https://github.com/FallDownTheSystem/modern-hn"
author: "FallDownTS"
published_at: "2026-11-19T18:20:07Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_FallDownTS
  - story_50563876
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Modern HN – a userscript that restyles Hacker News

> [!info] 一句话导读
> FallDownTheSystem/modern-hn

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50563876>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：FallDownTS　|　发布：2026-11-19T18:20:07Z
> 项目链接：<https://github.com/FallDownTheSystem/modern-hn>
> 采集：2026-11-20T09:45:52+08:00　|　id：`f2e7bd26b743c190`

## 正文

# FallDownTheSystem/modern-hn

Userscript: a modern reading layout for Hacker News with thread folding, search by date, a page filter and a calendar for past front pages

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-19T16:33:04Z

## Languages

- JavaScript

## Top Contributors

- FallDownTheSystem (6 contributions)

---

## README

# Modern HN

A userscript that gives Hacker News a modern reading layout. It is one file with no build step. It is not affiliated with Hacker News or Y Combinator.

https://github.com/user-attachments/assets/2cb45571-34af-4791-bf37-4614a6313de5

## Install

1. Install a userscript manager, for example Tampermonkey.
2. Open `modern-hn.user.js`. The userscript manager offers to install it.
3. Reload Hacker News.

The userscript manager gets later versions from this repository.

## Features

- **Layout:** a reading column, a pinned header, a light theme and a dark theme.
- **Threads:** click the gutter of a comment to fold its thread. The thread line shows in a colour on hover. Jump buttons go to the previous thread, the next thread, the top and the bottom.
- **Past front pages:** a day control in the header with a calendar. The arrows go one day back and forward.
- **Search:** a search bar in the header. It searches all of Hacker News by date or by popularity, and shows the results in the page. It can also filter the stories or comments of the current page.
- **More:** the "More" link adds the next page of stories or comments to the current page.
- **Settings:** theme, tone, lightness, contrast, a text font and a heading font (42 web fonts, system fonts, or a font on your computer), text size, text weight, roundness for the Allo font, page width, and vote arrows.

## Keys

| Key | Action |
| --- | --- |
| `J` / `K` | Next / previous thread |
| `P` / `N` | Previous / next day |
| `/` | Open the search bar |
| `Esc` | Close the search bar or a panel |

## Network access

Hacker News blocks requests from its pages to other sites, so the script asks the userscript manager for two connections:

- `hn.algolia.com`: the search. This is the same service that the search form of Hacker News uses. Your search words go to it.
- `cdn.jsdelivr.net`: the download of a web font, only when you select one. The font is then kept in the userscript storage.

The filter of the current page and all settings stay in your browser.

## Development

The script is `modern-hn.user.js`. It uses tabs and CRLF line ends. Check the syntax with `node --check modern-hn.user.js`.

## Licence

MIT

# Cornhole News

## 关联链接

- https://github.com/user-attachments/assets/2cb45571-34af-4791-bf37-4614a6313de5

## 导航

- 项目页：[[10-项目/github.com_50fab47f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
