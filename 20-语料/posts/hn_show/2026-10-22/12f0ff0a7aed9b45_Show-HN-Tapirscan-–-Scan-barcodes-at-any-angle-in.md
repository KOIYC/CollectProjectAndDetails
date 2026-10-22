---
type: "corpus"
item_id: "12f0ff0a7aed9b45"
title: "Show HN: Tapirscan – Scan barcodes at any angle in the browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50182480"
project_url: "https://tapirscan.f-kleinicke.de/"
author: "kleinicke"
published_at: "2026-10-21T15:17:22Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_kleinicke
  - story_50182480
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Tapirscan – Scan barcodes at any angle in the browser

> [!info] 一句话导读
> Documentation Formats Releases MIT / Apache-2.0 license

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50182480>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：kleinicke　|　发布：2026-10-21T15:17:22Z
> 项目链接：<https://tapirscan.f-kleinicke.de/>
> 采集：2026-10-22T09:46:18+08:00　|　id：`12f0ff0a7aed9b45`

## 正文

Documentation Formats Releases MIT / Apache-2.0 license
 Benchmark results
Tapirscan: barcode scanning, including rotated barcodes
Tapirscan is a barcode scanner designed for reliable detection, including barcodes rotated
 at different angles. This interactive demo compares its four scanning effort levels—TS-Low,
 TS-Med, TS-High and TS-VHigh—with the independent ZXing and ZBar barcode readers. More
 scanners also offers Quagga2 (linear barcodes), ZXing-JS (with optional extra search
 passes), jsQR (QR codes only, one per scan) and the browser’s native BarcodeDetector where
 supported.
What you see in the demo
Each selected scanner analyzes the same image pixels. Colored outlines mark detected barcode
 locations; nearby labels show the decoded values and the scanners that found them. Scanner
 buttons and result cards report decoded values and processing times. The four Tapirscan
 levels offer different trade-offs between scanning effort and speed. This demo lets you
 explore results on individual images; it is not a comprehensive benchmark.
Try images, PDFs and your camera
Choose a demo image, load your own photo, or use a webcam or phone camera. Rotate and zoom
 images, or double-click or double-tap to move the view center. Fullscreen provides a larger
 view, and Adjust opens rotation and zoom controls for photos and frozen frames. Pause /
 freeze turns a live camera frame into an image you can explore.
Load a PDF to detect barcodes on complete pages. Previous page and Next page let you scan
 the document page by page, using its stored orientation without zoom, rotation or cropping.
 PDF pages are rendered locally in your browser.
The Detect selector offers EAN-13, Retail, Common and All barcode formats. Readers scan the
 formats they support. Read up to controls the input resolution. Save image downloads the
 scanner input as a PNG with its crop, zoom and rotation applied, without the result
 overlays; in live mode it saves the latest analyzed frame.
Images, PDFs and camera frames are processed locally in your browser and are not uploaded.
 Learn more or use Tapirscan in your own project on
 GitHub .
Packages:
 npm (JavaScript / TypeScript) ·
 PyPI (Python) ·
 crates.io (Rust) .

## 评论（1/1）

> **kleinicke** · 2026-10-21T15:17:22.000Z　
> Current open source barcode scanner libraries like zxing and zbar perform (for nowadays) remarkable bad on scanning barcodes. I built the website demo to compare these libraries with a new library (tapirscan), I built out of frustration over them.The existing scanner rely on horizontal or vertical scanlines. My new rust based scanner works well with arbitrary orientations. On the demo website you can try out the library in comparison to zxing and zbar. You can also use your own images or use your webcam to scan objects. By default it just looks at Ean-13 barcodes, but there is a setting to allow more types.
> I built a test suite with multiple real world images that I labeled and used GPT-6 to develop the algorithm.
> The code is here: https://github.com/kleinicke/tapirscan
> The developed library is available at js: https://www.npmjs.com/package/tapirscan, python: https://pypi.org/project/tapirscan/ and
> Rust: https://crates.io/crates/tapirscan
> (Where else should I publish it, what languages to support, let me know here or as a GitHub issue and I’ll add it)I know this topic is not a hot topic research wise (therefore there were so little advances in that field in the last 5 years), but I hope to find some people that can use it.

## 导航

- 项目页：[[10-项目/tapirscan.f-kleinicke.de_0afe6e67]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
