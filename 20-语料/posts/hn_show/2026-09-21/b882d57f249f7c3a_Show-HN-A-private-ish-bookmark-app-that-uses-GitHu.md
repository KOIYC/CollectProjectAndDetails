---
type: "corpus"
item_id: "b882d57f249f7c3a"
title: "Show HN: A private-ish bookmark app that uses GitHub Gist as its back end"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47947813"
project_url: "https://github.com/chrisdiana/gistkeep"
author: "inflam52"
published_at: "2026-04-29T13:04:20Z"
captured_at: "2026-09-21T02:52:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_inflam52
  - story_47947813
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: A private-ish bookmark app that uses GitHub Gist as its back end

> [!info] 一句话导读
> Published: 2026-04-28

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47947813>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：inflam52　|　发布：2026-04-29T13:04:20Z
> 项目链接：<https://github.com/chrisdiana/gistkeep>
> 采集：2026-09-21T02:52:38+08:00　|　id：`b882d57f249f7c3a`

## 正文

Published: 2026-04-28

# Repository: chrisdiana/gistkeep

Portable bookmarks & notes, backed by Github Gist

- Stars: 8
- Forks: 0
- Watchers: 0
- Open issues: 0
- Primary language: JavaScript
- Languages: JavaScript (43.2%), HTML (34.9%), CSS (21.9%)
- License: MIT License (MIT)
- Topics: bookmark-manager, bookmarklet, bookmarks, github-gist, notes, notes-app
- Default branch: main
- Homepage: http://gistkeep.com/
- Created: 2026-04-28T04:21:54Z
- Last push: 2026-04-29T16:49:37Z
- Contributors: 1 (top: chrisdiana)

---

# GistKeep

> GistKeep is an open source bookmark and notes web app + bookmarklet that stores your library in your own GitHub Gist.

Fully client-side with no app-owned backend or hosted database. Your bookmarks and notes live in Markdown in your own Github Gist, which makes them portable, inspectable, versioned, and easy to back up. [Try it here](https://chrisdiana.github.io/gistkeep/app.html)

## Features

- Plain Markdown storage
- Built-in bookmarklet for saving links from anywhere
- Categories, tags, search, and notes
- Theme support
- Optional content encryption

## How It Works

1. Open the app and connect it to a GitHub Gist using a personal access token.
2. GistKeep reads and writes your bookmark and notes data directly to that gist.
3. Use the web app or bookmarklet to save and organize links.
4. Reopen the app later to browse, edit, search, and manage your library.

## Getting Started

### 1. Create a GitHub personal access token

Create a token with the minimum access needed to read and update the gist you want to use.

### 2. Run the app locally

Because this is a static app, any simple local web server will work.

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/app.html
```

### 3. Configure GistKeep

On first launch, provide:

- `GitHub Username or Gist ID`
- `GitHub Personal Access Token`
- an optional encryption key if you want token protection and encrypted content

If you do not provide an encryption key, the token can still be stored locally, but it will not be encrypted.

## Bookmarklet

GistKeep includes a bookmarklet generator inside the app.

After setup:

1. Open Settings
2. Find the bookmarklet section
3. Drag `Save to GistKeep` to your bookmarks bar, or copy the generated code manually

The bookmarklet opens GistKeep with the current page URL and title prefilled so you can save links quickly.

## Security Notes

### Token storage

GistKeep can encrypt the locally stored GitHub token with a user-supplied passphrase. Without that passphrase, the token is stored locally without encryption.

### Encryption note

GistKeep currently uses `CryptoJS.AES.encrypt(...)` with a user-supplied passphrase for local token protection and optional gist content encryption.

This means:

- Data is AES-encrypted with a passphrase-derived key
- The current implementation relies on CryptoJS/OpenSSL-style defaults

This is reasonable for casual privacy and personal use, but it should not be treated as state-of-the-art protection for high-value secrets. The real security still depends heavily on choosing a strong, unique encryption key.

### Gist privacy

Unlisted GitHub gists are not the same thing as strongly private storage. Anyone with the URL can access the gist unless the content itself is encrypted.

## Tradeoffs

GistKeep is intentionally simple, and that comes with tradeoffs:

- It rewrites managed files when saving changes
- Very large libraries are not the ideal use case
- GitHub Gist is the storage model, so GitHub availability and gist behavior matter
- Sharing and privacy depend on how you configure and use your gist

For normal personal collections, these tradeoffs are often worth it. For very large libraries or heavy collaboration, a conventional backend-backed app may be a better fit.

## Open Source

GistKeep is intended to be easy to inspect, self-host, and modify. It is a plain static app with no framework or build pipeline required.

## License

See [LICENSE](./LICENSE).

# onyks-os/TransparentTorProxy

## 评论（2/2）

> **Imustaskforhelp** · 2026-04-29T13:43:44.000Z　
> I used to use something similar but from a tampermonkey script extension which had a small button called bookmark on every website which would then use github gist for that. I think I still have it but its been sometime since I have used it.

---

> **inflam52** · 2026-04-29T13:48:04.000Z　
> Yes exactly! I did this kind of thing too for a little while. I ended up using the Gist to access the bookmarks but figured it would be nice to have an optional viewer to search/sort. Also having it across all devices is a big plus. One of the features I miss now that Pocket used to offer with their bookmarklet.

## 关联链接

- http://gistkeep.com/
- http://localhost:8080/app.html
- https://chrisdiana.github.io/gistkeep/app.html

## 导航

- 项目页：[[10-项目/github.com_be520c96]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
