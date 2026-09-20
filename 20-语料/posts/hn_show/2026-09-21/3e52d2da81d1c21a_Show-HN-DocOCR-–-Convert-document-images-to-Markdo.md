---
type: "corpus"
item_id: "3e52d2da81d1c21a"
title: "Show HN: DocOCR – Convert document images to Markdown locally on macOS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48334770"
project_url: "https://github.com/riddleling/docOCR"
author: "riddleling"
published_at: "2026-05-30T10:40:46Z"
captured_at: "2026-09-21T02:52:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_riddleling
  - story_48334770
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: DocOCR – Convert document images to Markdown locally on macOS

> [!info] 一句话导读
> macOS CLI and HTTP OCR tool for converting document images to Markdown.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48334770>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：riddleling　|　发布：2026-05-30T10:40:46Z
> 项目链接：<https://github.com/riddleling/docOCR>
> 采集：2026-09-21T02:52:54+08:00　|　id：`3e52d2da81d1c21a`

## 正文

# riddleling/docOCR

macOS CLI and HTTP OCR tool for converting document images to Markdown.

- Stars: 37
- Forks: 3
- Watchers: 37
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-05-26T15:47:13Z

## Languages

- Swift

## Topics

- cli
- http-server
- macos
- markdown
- ocr
- vision-framework

## Top Contributors

- riddleling (21 contributions)

---

## README

# docOCR

`docOCR` is a macOS command-line OCR tool that converts document images into Markdown text. It can run as a batch CLI tool or as a local HTTP server for browser uploads and API clients.

Image

## Table of Contents

- Features
- Requirements
- CLI Usage
- HTTP Server
- API Usage
- Build
- Install
- Development
- macOS Shortcuts: Screenshot to Markdown
- Codex Skill

## Features

- Converts image files to Markdown text.
- Writes batch OCR output next to each source image using the same basename and a `.md` extension.
- Converts detected paragraphs, lists, and tables into Markdown when Apple's document recognition API identifies them.
- Provides a local web UI for uploading an image and viewing OCR output.
- Provides a JSON API for image upload and OCR response.
- Uses Apple's `RecognizeDocumentsRequest` API, available on macOS 26+.
- Performs OCR locally on the Mac. OCR recognition does not require sending images to an external network service.

The HTTP server is implemented with Vapor.

## Requirements

- macOS 26 or later.
- Xcode / Swift toolchain that supports the package's Swift tools version.
- Network access may be required during the first build so Swift Package Manager can fetch dependencies such as Vapor.

## CLI Usage

Show help:

```bash
docOCR -h
docOCR --help
```

Show version:

```bash
docOCR -V
docOCR --version
```

Convert image files to Markdown:

```bash
docOCR ~/Desktop/book_imgs/*.jpg
```

This prints the OCR Markdown text to the terminal.

Write Markdown files next to the source images:

```bash
docOCR -o ~/Desktop/book_imgs/*.jpg
```

Each input file is written as a Markdown file next to the image:

```text
~/Desktop/book_imgs/01.jpg -> ~/Desktop/book_imgs/01.md
~/Desktop/book_imgs/02.jpg -> ~/Desktop/book_imgs/02.md
```

Existing `.md` files with the same name are overwritten.

Start the HTTP server:

```bash
docOCR -s
```

By default, the server listens on port `8080`.

Use a custom port:

```bash
docOCR -s -p 8000
```

The `-s` and `-o` modes are mutually exclusive.

## HTTP Server

When the server is running, open:

```text
http://0.0.0.0:8080
```

If you start the server with a custom port, use that port instead:

```text
http://0.0.0.0:8000
```

The web page uses:

```text
POST /upload
```

This route is intended for browser form uploads and returns an HTML result page.

## API Usage

Use the JSON API endpoint:

```text
POST /api/ocr
```

Example:

```bash
curl -X POST http://127.0.0.1:8000/api/ocr \
  -F "file=@01.png"
```

The API also accepts `image` as the multipart field name:

```bash
curl -X POST http://127.0.0.1:8000/api/ocr \
  -F "image=@01.png"
```

Successful response:

```json
{
  "success": true,
  "message": "OK",
  "text": "OCR text..."
}
```

Error response:

```json
{
  "success": false,
  "message": "Error message",
  "text": ""
}
```

## Build

Build a debug executable:

```bash
swift build
```

Build a release executable:

```bash
swift build -c release
```

The release binary is generated at:

```text
.build/release/docOCR
```

## Install

Build the release binary:

```bash
swift build -c release
```

Install it somewhere on your `PATH`, for example:

```bash
install -m 755 .build/release/docOCR /usr/local/bin/docOCR
```

Then run:

```bash
docOCR -h
```

If `/usr/local/bin` is not writable or not on your `PATH`, choose another directory such as `~/bin` and make sure that directory is included in your shell `PATH`.

## Development

Run directly with SwiftPM:

```bash
swift run docOCR -o ~/Desktop/book_imgs/*.jpg
swift run docOCR -s -p 8000
```

## macOS Shortcuts: Screenshot to Markdown

`docOCR` can also be used with the Shortcuts app on macOS to turn a screenshot into Markdown text.

In this workflow, the shortcut captures a screen selection, passes the screenshot image path to `docOCR`, reads the Markdown text from stdout, copies it to the clipboard, and then lets you paste the result into any text editor.

Then run the macOS shortcut:

screenshot_to_md

The shortcut flow is:

1. Capture a screenshot.
2. Save the screenshot as a temporary image file.
3. Run `docOCR `.
4. Read the OCR Markdown text from stdout and copy it to the clipboard.

Paste the result into your editor.

Download the stdout-based shortcut: Screenshot to Markdown.

image3

Alternatively, the shortcut can call the `/api/ocr` API instead of running `docOCR` directly. Start the local server first:

```bash
docOCR -s
```

Download the API-based shortcut: Screenshot to Markdown via API.

image2

## Codex Skill

If you use Codex, you can install the companion skill for docOCR: dococr-skill

The skill gives Codex reusable context for docOCR CLI usage, local HTTP API calls, OCR execution, and troubleshooting.

# alebeck/rhymesum

## 关联链接

- http://0.0.0.0:8000
- http://0.0.0.0:8080
- http://127.0.0.1:8000/api/ocr

## 导航

- 项目页：[[10-项目/github.com_03b7216b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
