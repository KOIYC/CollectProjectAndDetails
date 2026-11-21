---
type: "corpus"
item_id: "b879874233c45ed9"
title: "Show HN: Make dark PDFs printer-friendly in the browser, without rasterizing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50577959"
project_url: "https://github.com/alexadam/printer-friendly"
author: "eg312"
published_at: "2026-11-20T17:02:11Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_eg312
  - story_50577959
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Make dark PDFs printer-friendly in the browser, without rasterizing

> [!info] 一句话导读
> alexadam/printer-friendly

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50577959>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：eg312　|　发布：2026-11-20T17:02:11Z
> 项目链接：<https://github.com/alexadam/printer-friendly>
> 采集：2026-11-21T14:45:01+08:00　|　id：`b879874233c45ed9`

## 正文

# alexadam/printer-friendly

Make PDFs printer-friendly: remove dark backgrounds and pictures, and turn light text black, while keeping the layout

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://alexadam.github.io/demos/printer-friendly/
- Default branch: main
- Created: 2026-11-20T15:46:58Z

## Languages

- CSS
- HTML
- JavaScript
- Shell

## Topics

- pdf
- pdf-export
- pdf-extraction
- pdf-generation
- pdf-parser
- pdf-processing
- pdf-reader
- pdf-tools
- pdf-viewer
- printer
- printer-utilities

## Top Contributors

- alexadam (2 contributions)

---

## README

# Printer Friendly PDF

Make PDFs printer-friendly: remove dark backgrounds and pictures, and turn light text black, while keeping
the layout and real, selectable text. Everything runs in the browser, so files are never uploaded.

**Live demo**

Screenshot 1
Screenshot 2
Screenshot 3
Screenshot 4

## Features

- **Private.** The file never leaves the browser.
- **Automatic cleanup.** Remove dark backgrounds and pictures, and turn light text and pale lines black. Switches set the defaults; your choices override them.
- **Pick any element.** Click it in the preview (click the same spot again for what is underneath), choose it in the sidebar, apply one action to a whole group, or drag a rectangle with the Area tool.
- **Actions.** Keep, remove, fill white (filled shapes), or make black (text and shapes).
- **Before and after.** Preview the original and the edited PDF side by side, or either one alone, with markers on the elements.
- **Combine PDFs.** Open or drop several files, reorder or leave some out, then edit the joined result. Edits already made on an open PDF carry over.
- **Page thumbnails.** Jump to any page. Removed pages are struck through, and long documents load thumbnails as they scroll into view.
- **Remove pages.** Leave pages out by number or range (`2, 5-8, 12-`), keep only the ones you list, or drop the page you are looking at. At least one page stays.
- **Print layout.** Place 1, 2, or 4 pages on each sheet, set margins (including negative, to crop borders), and scale every page from 10% to 400%.
- **Split the download.** Save a ZIP of smaller PDFs, each with a set number of pages (or sheets, when several pages share a sheet).
- **Real text.** Layout and selectable text stay. Only edited pages are rewritten. Links, comments, and form fields stay with their pages.
- **Keyboard.** Arrow keys change page; shortcuts remove or restore a page, recolor the selection, switch to the Area tool, or jump to a page number.
- **Scans.** A scanned page is detected and left alone, since the words and the background are one picture.

```
./start.sh            # installs dependencies, serves on http://localhost:8000
./build.sh            # writes a static site to dist/ for GitHub Pages or Netlify
npm test              # engine + heuristics tests (Node)
npm run samples       # regenerates samples/*.pdf for manual testing
```

# alfaris/full-production-studio

## 关联链接

- http://localhost:8000
- https://alexadam.github.io/demos/printer-friendly/

## 导航

- 项目页：[[10-项目/github.com_6ad83148]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
