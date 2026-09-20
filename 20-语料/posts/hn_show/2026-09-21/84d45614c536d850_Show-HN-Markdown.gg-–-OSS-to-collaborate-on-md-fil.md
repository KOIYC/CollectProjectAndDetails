---
type: "corpus"
item_id: "84d45614c536d850"
title: "Show HN: Markdown.gg – OSS to collaborate on md files"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49110336"
project_url: "https://github.com/xatuke/markdowngg"
author: "satuke"
published_at: "2026-07-30T14:14:17Z"
captured_at: "2026-09-21T03:11:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_satuke
  - story_49110336
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Markdown.gg – OSS to collaborate on md files

> [!info] 一句话导读
> A zero-knowledge, self-hostable markdown-as-docs-service

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49110336>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：satuke　|　发布：2026-07-30T14:14:17Z
> 项目链接：<https://github.com/xatuke/markdowngg>
> 采集：2026-09-21T03:11:16+08:00　|　id：`84d45614c536d850`

## 正文

# xatuke/markdowngg

A zero-knowledge, self-hostable markdown-as-docs-service

- Stars: 6
- Forks: 2
- Watchers: 6
- Open issues: 0
- Homepage: https://markdown.gg/
- Default branch: main
- Created: 2025-11-02T10:53:11Z

## Languages

- CSS
- JavaScript
- TypeScript

## Top Contributors

- xatuke (5 contributions)

---

## README

# markdown.gg

A zero-knowledge markdown editor and sharing service with LaTeX support.

## Features

- **Zero-knowledge encryption**: All content is encrypted client-side with AES-GCM
- **Document history**: Access all your shared documents from a sidebar
- **Updatable shares**: Save changes to your shared documents without creating new links
- **Side-by-side editor**: Monaco editor with live markdown preview
- **LaTeX support**: Render mathematical equations with KaTeX
- **GitHub Flavored Markdown**: Tables, task lists, strikethrough, and more
- **Light/Dark themes**: Toggle between light and dark modes
- **Minimal design**: Clean black and white aesthetic
- **Database flexibility**: SQLite for local development, PostgreSQL for production

## How It Works

1. Write markdown in the editor
2. Click "Share" to generate a unique link (first time)
3. Content is encrypted client-side before sending to the server
4. The encryption key is stored in the URL hash (never sent to the server)
5. Share the link with others to let them view your document
6. Click "Save" to update the shared document with your changes
7. Viewers see updates when they refresh the shared link

### Installation

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env

# Push database schema
npm run db:push

# Start development server
npm run dev
```

The application will be available at `http://localhost:3000`.

### Database Configuration

#### SQLite (Local Development)

The default configuration uses SQLite:

```env
DATABASE_URL=file:./sqlite.db
```

#### PostgreSQL (Production)

For production, update `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/markdowngg
```

Then run migrations:

```bash
npm run db:push
```

## Usage

### Creating and Sharing a Document

1. Open the application
2. Write your markdown in the left pane
3. See the live preview in the right pane
4. Click "Share" to create a shareable link
5. The link is copied to your clipboard automatically

### Updating a Shared Document

Once you've shared a document:
1. Continue editing in the editor
2. Click "Save" to update the shared document
3. The share link remains the same
4. Anyone with the link will see updates when they refresh

### Accessing Your Documents

1. Click the menu icon (☰) in the top left to open the document sidebar
2. See all your previously shared documents with their titles and last modified times
3. Click on any document to load it
4. Remove documents from history by clicking the X button

### Starting a New Document

Click "New" to clear the editor and start fresh. This doesn't delete your previous documents from history.

### Viewing a Shared Document

Open the shared link in your browser. The document will be decrypted automatically using the key in the URL hash. Shared documents are read-only.

### Document History

All shared documents are stored locally in your browser's localStorage along with their encryption keys. This means:
- Your document list persists across browser sessions
- Documents are private to your browser
- Up to 50 most recent documents are kept
- Clearing browser data will remove your document history (but documents remain on the server)

### LaTeX Example

Inline: `$E = mc^2$`

Block:
```
$$
\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}
$$
```

## Security

- All encryption happens client-side using the Web Crypto API
- Encryption keys are never sent to the server
- Keys are stored in URL fragments (hash), which are not sent in HTTP requests
- The server only stores encrypted content

## License

MIT

## 关联链接

- http://localhost:3000`.
- https://markdown.gg/

## 导航

- 项目页：[[10-项目/github.com_769c0169]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
