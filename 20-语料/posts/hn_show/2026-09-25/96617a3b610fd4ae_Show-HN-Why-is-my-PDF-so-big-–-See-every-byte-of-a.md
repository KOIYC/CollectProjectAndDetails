---
type: "corpus"
item_id: "96617a3b610fd4ae"
title: "Show HN: Why is my PDF so big? – See every byte of a PDF as a treemap"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49833293"
project_url: "https://whyismypdfsobig.com/"
author: "whizzx"
published_at: "2026-09-24T16:43:38Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_whizzx
  - story_49833293
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Why is my PDF so big? – See every byte of a PDF as a treemap

> [!info] 一句话导读
> Why is my PDF so big?

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49833293>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：whizzx　|　发布：2026-09-24T16:43:38Z
> 项目链接：<https://whyismypdfsobig.com/>
> 采集：2026-09-25T13:42:25+08:00　|　id：`96617a3b610fd4ae`

## 正文

PDF Tree Map
 Open PDF…
Why is my PDF so big?
Drop a PDF to see every byte as a zoomable treemap: images, fonts, page content, tagging structure,
 metadata, duplicated streams and dead weight left behind by incremental saves.
Already optimized it? Drop the original and the optimized file together to see
 what shrank, what grew, and what was lost along the way.
 Already optimized it? Open the original, then choose “Compare with another
 version” to see what shrank, what grew, and what was lost along the way.
Drop a PDF here Choose a PDF
 or click to choose a file from your files
Reading file…
Explore an example PDF
 Files are analyzed in your browser; nothing is uploaded.
Example: a 939 KB report where a single image is 79% of the file. Click to explore it.
What makes a PDF file so large?
A PDF is a container: pages, images, fonts and metadata are stored as separate objects, and a handful of
 them usually account for most of the file. These are the most common reasons a PDF is bigger than expected.
Images
Photos kept at print resolution, screenshots and scanned pages stored losslessly, or images much larger than
 their size on the page. A single uncompressed scan can weigh several megabytes.
 Fix: downsample to 150–200 ppi for screen use and store photographs as JPEG.
Embedded fonts
Fonts are embedded so the document looks the same everywhere. Embedding a whole font instead of only the
 characters used, large Chinese, Japanese or Korean fonts, or the same font embedded many times can add
 megabytes.
 Fix: embed font subsets, and merge duplicate subsets.
Incremental saves
Many editors save changes by appending them to the end of the file instead of rewriting it. Older versions
 of pages, images and metadata stay inside the file, invisible but still taking up space.
 Fix: use “Save As”, or an optimizer that removes unused objects.
Duplicate resources
A logo, background or letterhead embedded once per page instead of once per document.
 Fix: an optimizer that merges identical images and streams.
Hidden data
File attachments, form data (XFA), page thumbnails, and XMP metadata that grows with every edit.
Complex vector graphics
Maps, CAD drawings and detailed charts can contain millions of drawing operations in their page content.
The structure tree (tagging) is often a sizeable part of long documents, but it is what makes
 a PDF accessible to screen readers. It is worth keeping.
Frequently asked questions
Is my PDF uploaded anywhere?
No. The file is analyzed by JavaScript running inside your browser, and nothing is sent to a server.
What do the colors in the treemap mean?
Each color is a kind of content: images, fonts, page content, structure tree, metadata, file overhead and
 so on. The area of each block is proportional to its size in bytes. Striped blocks are data that can be
 removed without changing how the document looks.
What is the “decompressed” size?
Most data in a PDF is compressed. The decompressed size shows how large each part is once its
 compression is undone (for images, the raw pixel data), which helps spot content that is poorly
 compressed.
How can I check what a PDF optimizer changed?
Drop the original and the optimized file together, or open one and choose “Compare with another
 version”. The treemap shows the original colored by what happened to each item, and you are warned
 about anything that was lost, such as tagging, form fields, bookmarks or digital signatures.
Does it work with password-protected PDFs?
Yes. PDFs that are only restricted by an owner password open directly. For PDFs that need a password to
 open, you can enter it; it is used only in your browser.
Inspired by webpack-bundle-analyzer
Drop to analyze

## 导航

- 项目页：[[10-项目/whyismypdfsobig.com_d50df37f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
