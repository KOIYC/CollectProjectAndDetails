---
type: "corpus"
item_id: "4f08920f8a11fad6"
title: "Show HN: Nostos – A self-hosted home for reading, notes, and writing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50030537"
project_url: "https://github.com/Christian-Gennari/Nostos"
author: "CalmReader96"
published_at: "2026-10-10T07:22:35Z"
captured_at: "2026-10-11T09:43:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-11"
pub_day: "2026-10-10"
tags:
  - 语料
  - hn_show
  - author_CalmReader96
  - story_50030537
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Nostos – A self-hosted home for reading, notes, and writing

> [!info] 一句话导读
> Christian-Gennari/Nostos

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50030537>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：CalmReader96　|　发布：2026-10-10T07:22:35Z
> 项目链接：<https://github.com/Christian-Gennari/Nostos>
> 采集：2026-10-11T09:43:53+08:00　|　id：`4f08920f8a11fad6`

## 正文

# Christian-Gennari/Nostos

A home for your reading life. Read your books, capture what stays with you, and turn your reading into thought and writing in one self-hosted study.

- Stars: 5
- Forks: 1
- Watchers: 5
- Open issues: 8
- License: GNU General Public License v3.0
- Homepage: nostos.page
- Default branch: main
- Created: 2025-11-25T19:01:18Z

## Languages

- C#
- CSS
- Dockerfile
- HTML
- JavaScript
- Lua
- Python
- Shell
- TypeScript

## Topics

- angular
- audiobooks
- dotnet
- epub-reader
- local-first
- pdf-viewer
- pkm
- reading
- self-hosted
- sqlite
- writing

## Top Contributors

- Christian-Gennari (1799 contributions)
- discovicke (26 contributions)
- claude (13 contributions)

---

## README

 A home for reading, thinking, and writing.
 Bring books, notes, ideas, and drafts together in one connected place.

 About •
 Features •
 Getting Started •
 Tech Stack •
 Docs •
 License

 Watch the launch film on nostos.page

## What is Nostos?

Nostos is a personal reading and writing environment built around a simple idea: what you read should be able to stay connected to what you think and what you eventually write.

Instead of splitting that process across a library app, an e-book reader, a notes system, and a writing tool, Nostos keeps the whole path together. You can collect physical books, EPUBs, PDFs, and audiobooks; read or listen inside the app; capture notes and highlights; connect ideas through topics; and bring that material into the Writing Studio when it is time to turn reading into your own work.

The interface is deliberately restrained. There are no social feeds, reading streaks, engagement mechanics, or productivity scores competing for attention. The emphasis stays on the library and the work you are doing with it.

This repository contains the canonical Nostos product and the complete public **SelfHosted** application. The official hosted Nostos Cloud service uses the same product model and Angular frontend through a separate private hosting composition.

---

## Features

### Library

Keep different kinds of books in one collection without flattening them into the same experience.

- **Physical books:** Add books with metadata and ISBN lookup while keeping them alongside digital titles.
- **EPUB and PDF:** Store and read files directly in Nostos.
- **Audiobooks:** Import M4B, M4A, and MP3 audio with chapter-aware playback. Multi-track audiobooks play as one continuous book.
- **Collections and filtering:** Organize books into nested collections, move them with drag and drop, and filter by reading state, rating, recency, or collection.
- **Works and editions:** Nostos can group matching editions using normalized ISBNs or title and author identity.
- **Free-source acquisition:** Search and import supported public-domain material from Project Gutenberg and LibriVox. Imported books become ordinary Nostos library items rather than remaining dependent on the source.

 View Library Screenshots

 Book Overview & Progress

 Cataloging & Import

---

### Reading & Listening

Nostos includes readers for the formats it stores, so notes and progress can stay close to the source.

- **EPUB reader:** Read EPUB files in the browser and capture text from the book as you go.
- **PDF reader:** Read PDFs, select passages, and create highlights without leaving Nostos.
- **Audiobook player:** Listen to chaptered audiobooks with saved playback progress.
- **Contextual notes:** Keep thoughts attached to the book they came from instead of moving them into a disconnected notes folder.
- **E-reader highlights:** Import Kobo databases or KOReader sidecars from Settings → Library & data. Review destinations, match an existing book or add a missing one, and undo an import. Repeat imports keep confirmed matches and avoid duplicates.

---

### Brain & Topics

The Brain is where notes from individual books start to connect.

- **Wiki-links:** Use `[[Topic]]` links in notes to connect recurring ideas.
- **Topic views:** Browse topics as a list or explore their relationships in the interactive graph.
- **Evidence-first navigation:** Move from an idea back to the notes and reading material that support it.
- **Automatic cleanup:** Topics with no remaining references can be cleaned up automatically.

---

### Writing Studio

The Writing Studio brings drafting and source material into the same workspace.

- **Three-panel workspace:** Keep a project and chapter tree on the left, the draft in the center, and relevant source material on the right.
- **Notes and quotations at hand:** Browse material from the library while writing and insert useful passages into the draft.
- **Rich editing with Markdown round-tripping:** TinyMCE provides the editing surface while Turndown keeps Markdown conversion available.
- **Automatic saving:** Draft changes are saved in the background.

---

### Optional AI Assistance

Nostos can use configured AI services for features such as **Ask Nostos** and speech-to-text, but AI is not required for the core product.

In the public SelfHosted application, AI provider configuration remains under the operator's control. The hosted service can provide managed AI through its own private infrastructure. The product-level interfaces stay provider-neutral in this repository.

---

### Portability, Backup & Integrations

- **Portable library archives:** Export and import `.nostos` files to move library data between Nostos installations. See Library portability and migration for the exact steps, contents, limits, recovery behavior, and verification status.
- **Local backup and restore:** SelfHosted installations include local backup and restore workflows with integrity checks and restore safeguards.
- **OPDS export:** A configurable OPDS catalogue can expose a self-hosted library to compatible readers on networks you control.
- **MCP:** An optional bearer-protected Model Context Protocol endpoint lets compatible tools work with Nostos through the documented library contracts.

#### Moving a library

When a host advertises migration, open **Settings → Library & data → Move your library**.

- **Export:** Choose **Export library**, then **Download archive** when it is ready.
- **Import:** Choose **Import library…** and select the `.nostos` file.

An empty destination activates after verification. A populated destination asks
you to confirm **Replace library** and keeps a recovery copy for seven days.

One real SelfHosted → Cloud import is recorded for the hosted alpha. Cloud export, restoring a replaced library, and Cloud → SelfHosted import have not been verified there. The shared Settings UI in this repository has no **Restore previous** button; the recovery operation is currently exposed by the SelfHosted API. See the portability guide for details.

---

## SelfHosted and Nostos Cloud

Nostos is one product with two deployment modes.

### SelfHosted

The public executable in this repository is complete on its own. It uses:

- SQLite for relational data
- the local filesystem for book media
- local backup and restore
- operator-configured AI providers when AI features are enabled

Your library database and stored media stay on the machine or server where you run Nostos. Features that contact external services, such as public catalogue imports, metadata lookup, or optional AI, naturally require network access when you use them.

### Nostos Cloud

The official hosted service composes the public Nostos product with private hosting infrastructure for authentication, tenant provisioning, managed storage, billing, managed AI, and operations.

Reusable product behavior, the domain model, capability contracts, and the customer-facing Angular application live here first. Hosted provider and operator implementations remain private.

See the public/private boundary ADR and deployment capabilities for the architectural contract.

---

## Architecture & Tech Stack

Nostos is designed as a single product with a reusable product layer, a public SelfHosted host, and one shared frontend.

```text
Nostos/
├── Nostos.Product/       # canonical product, domain, application and API behavior
├── Nostos.Backend/       # public SelfHosted host: SQLite, local files, backup, BYOK
├── Nostos.Shared/        # shared DTOs and product contracts
├── Nostos.Frontend/      # Angular application shared by SelfHosted and Cloud
└── docs/                 # product, architecture and operational documentation
```

### Core stack

- **Backend:** .NET 10 with ASP.NET Core Minimal APIs
- **Database:** SQLite with Entity Framework Core 10 in the public SelfHosted host
- **Frontend:** Angular 21 with standalone components and Signals
- **EPUB:** `epub.js`
- **PDF:** `ngx-extended-pdf-viewer`
- **Audio:** `Howler.js`
- **Topic graph:** Graphology, Sigma.js, and `d3-force`
- **Editor:** TinyMCE with Turndown for Markdown conversion
- **Icons:** Phosphor
- **Typography:** Newsreader and Hanken Grotesk
- **MCP:** Model Context Protocol support through the ASP.NET Core SDK

---

## Getting Started

### Prerequisites

- .NET 10 SDK
- Node.js LTS with npm

### Development

Clone the repository, install the root tooling and frontend dependencies, then start the backend and frontend together.

```bash
git clone https://github.com/Christian-Gennari/Nostos.git
cd Nostos

npm install
npm --prefix Nostos.Frontend install
npm start
```

The Angular development server runs at **http://localhost:4200** and proxies API requests to the backend on port **5099**.

### Production

```bash
npm run prod
```

This builds the Angular frontend and serves the application through the .NET host. Open **http://localhost:5099** in your browser.

### Docker / Compose

The official SelfHosted image is **`ghcr.io/christian-gennari/nostos`**. The `latest` tag is published only after the complete public product CI passes on `main`. Each release also gets an immutable `selfhosted-sha- ` tag.

The container keeps application binaries under `/app` and all durable SelfHosted data under **`/data`**. Do not relocate ASP.NET's content root to persist data: the frontend is served from the application's `wwwroot`, while the SQLite database and library storage have their own configurable paths.

Run the official image directly:

```bash
docker pull ghcr.io/christian-gennari/nostos:latest
docker volume create nostos-data
docker run -d \
  --name nostos \
  -p 5099:8080 \
  -v nostos-data:/data \
  --restart unless-stopped \
  ghcr.io/christian-gennari/nostos:latest
```

Or use the included Compose file:

```bash
docker compose up -d
```

Then open **http://localhost:5099**. The named `nostos-data` volume contains `nostos.db`, stored books, and local backup archives, so replacing the container does not replace your library data.

To update to the newest verified SelfHosted image:

```bash
docker compose pull
docker compose up -d
```

To pin a specific immutable SelfHosted build, set its release tag when running Compose:

```bash
NOSTOS_IMAGE_TAG=selfhosted-sha-<full-public-commit-sha> docker compose up -d
```

The `selfhosted-sha-*` prefix is intentional. Historical `sha-*` tags in the same GHCR package predate the hosted/SelfHosted package split and may identify old Cloud artifacts; do not use those as SelfHosted pins.

Compose keeps the existing named volume across image replacement. Use Nostos' portable `.nostos` export/backup features as your user-owned backup and migration path; a Docker volume is persistent storage, not a substitute for backups.

If you prefer to build from the source you cloned instead of pulling GHCR:

```bash
docker build --pull -t nostos:selfhosted .
```

For a non-container install, the historical database location remains ` /nostos.db` unless `Persistence__DatabasePath` is configured explicitly. `Storage__BooksRoot` and `Storage__BackupsRoot` can likewise override their local paths.

For provider-specific behavior and requirements, see Content Providers & Acquisition.

---

## Design

Nostos uses an editorial visual language built around warm paper-like surfaces, restrained forest green, literary typography, and low-chrome controls. The goal is to make the application feel closer to a considered reading environment than a conventional SaaS dashboard.

The Nostos mark is a doorway and a subtle lowercase `n`: a Forest Green (`#293E32`) rounded tile with a White (`#FFFFFF`) arch cut from it. The mark remains the same in light and dark themes.

Read the Design Manifesto for the product's visual and interaction principles, or browse the brand assets.

---

## Documentation

- **Releases:** Reader-facing changes to Nostos.
- **Releases:** CalVer tags and the release notes workflow.
- **Design Manifesto:** Product, visual, and interaction principles.
- **Content Providers & Acquisition:** Provider architecture and import behavior for external catalogues.
- **MCP Library Contracts:** Stable Model Context Protocol contracts for agents and tools.
- **Backend Endpoints:** REST API reference.
- **Public/private boundary ADR:** Ownership boundary between the public product and official hosted composition.
- **Deployment Capabilities:** SelfHosted and Cloud capability contract.
- **Library portability and migration:** Customer steps, API behavior, limits, and verification status for `.nostos` archives and library transfer.
- **SelfHosted Activation & Recovery:** Replacing a library after import, the seven-day recovery copy, restore, maintenance states and operator recovery.
- **PostgreSQL Compatibility:** Evidence for the shared relational product model.

Current development work is tracked in GitHub Issues.

---

## License & Trademark

Nostos is licensed under the **GNU General Public License v3.0 or later**. You may run, study, modify, and redistribute the software under those terms.

The Nostos name, related word marks, and official visual identity are not granted by the GPL. Distributed forks and derivative builds must use independent naming and branding. See TRADEMARK.md for the full policy.

The EPUB reader bundles the **Libron** typeface (© Nico Verbruggen, derived from Readerly and Newsreader), licensed separately under the SIL Open Font License 1.1.

## 关联链接

- http://localhost:4200**
- http://localhost:5099**
- http://localhost:5099**.
- https://github.com/Christian-Gennari/Nostos.git

## 导航

- 项目页：[[10-项目/github.com_a8289218]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
