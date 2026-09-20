---
type: "corpus"
item_id: "097987d6e7f086e7"
title: "Show HN: Albums Vault, my take on how to manage Spotify album library"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49506445"
project_url: "https://codefloe.com/rabc/albums-vault"
author: "rabc"
published_at: "2026-08-31T06:53:07Z"
captured_at: "2026-09-21T03:11:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_rabc
  - story_49506445
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Albums Vault, my take on how to manage Spotify album library

> [!info] 一句话导读
> rabc/albums-vault: A calmer, more personal way to browse the albums you’ve saved on Spotify. - CodeFloe - the Forgejo developer platform

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49506445>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rabc　|　发布：2026-08-31T06:53:07Z
> 项目链接：<https://codefloe.com/rabc/albums-vault>
> 采集：2026-09-21T03:11:26+08:00　|　id：`097987d6e7f086e7`

## 正文

Author: rabc

rabc/albums-vault: A calmer, more personal way to browse the albums you’ve saved on Spotify. - CodeFloe - the Forgejo developer platform

 Repository files (latest commit first)

| Filename | Latest commit message | Latest commit date |
| --- | --- | --- |
| Ricardo Carvalho 59a35f7dde All checks were successful ci/crow/push/build Pipeline was successful Details Add Albums Vault demo video | | 2026-08-30 09:14:45 +02:00 |
| .crow | feat: add project support links and assets | 2026-08-25 21:00:00 +02:00 |
| assets | Add Albums Vault demo video | 2026-08-30 09:14:45 +02:00 |
| docs | start configuration to opensource | 2026-08-23 13:31:57 +02:00 |
| icon | start configuration to opensource | 2026-08-23 13:31:57 +02:00 |
| scripts | add build version to script | 2026-08-27 09:19:00 +02:00 |
| src | feat: switch donation platform from Buy Me a Coffee to Ko-fi | 2026-08-26 22:42:30 +02:00 |
| src-tauri | add build version to script | 2026-08-27 09:19:00 +02:00 |
| .gitignore | start configuration to opensource | 2026-08-23 13:31:57 +02:00 |
| agents.md | add build version to script | 2026-08-27 09:19:00 +02:00 |
| index.html | feat: switch donation platform from Buy Me a Coffee to Ko-fi | 2026-08-26 22:42:30 +02:00 |
| LICENSE | start configuration to opensource | 2026-08-23 13:31:57 +02:00 |
| package-lock.json | add build version to script | 2026-08-27 09:19:00 +02:00 |
| package.json | add build version to script | 2026-08-27 09:19:00 +02:00 |
| README.md | Add Albums Vault demo video | 2026-08-30 09:14:45 +02:00 |
| vite.config.js | Initial commit | 2026-06-26 06:57:02 +02:00 |

 README.md

# Albums Vault

 A calmer, more personal way to browse the albums you’ ve saved on Spotify.

## See it in action

## Your saved albums deserve a place of their own

Spotify is great for playing music, but a growing saved library can be surprisingly difficult to explore. Albums Vault turns that library into a visual, searchable collection. It gives you a place to rediscover records you forgot about and find something to listen to next.

Your library is copied locally, so Albums Vault opens quickly and remains useful when your connection is unavailable.

## What you can do

- Browse your collection — See your saved albums together in one focused, visual library.
- Find something quickly — Search by album or artist, then sort by name, release date, or when you saved it.
- Filter your way — Narrow the collection by album, single, or compilation, and show only albums you’ ve listened to.
- Rediscover what you own — Browse by artist and genre instead of relying on Spotify’ s recommendations.
- Keep track of what you’ ve heard — Albums are automatically marked as listened to when Spotify sees you play one of their tracks. You can also mark an album yourself.
- Explore every release — Open an album to see its artists, genres, release type, tracklist, and track durations.
- Keep browsing offline — Your album collection is cached on your computer and stays visible while Spotify or your internet connection is unavailable.
- Stay in sync — Albums Vault refreshes your collection in the background while keeping the cached library available on screen.

> Listening history is based on the recently played tracks Spotify makes available. Because Spotify does not provide a direct “mark album as listened” feature, the automatic status is best understood as a helpful approximation.

## Getting started

Albums Vault uses Spotify’ s PKCE login flow. You provide your own Spotify Client ID when you first open the app; there is no client secret to copy, and no environment variable is required.

### Create a Spotify app

1. Open the Spotify Developer Dashboard and sign in.
2. Choose Create app and give it a name, such as `Albums Vault`.
3. Under APIs used, enable Web API.
4. Add this Redirect URI exactly:

```text
http://127.0.0.1:8888/callback

```
5. Accept the developer agreement and click Save.
6. Open the app’ s Settings page and copy its Client ID.

When Albums Vault starts for the first time, paste the Client ID into the onboarding screen. The app will then open Spotify in your browser so you can sign in and approve access.

The Client ID is public by design. Albums Vault stores your access tokens in your operating system’ s secure credential store rather than in the app database.

## Privacy and ownership

Albums Vault is open source and keeps a local copy of your album library on your computer. It does not need your Spotify password, and it does not require a Spotify client secret.

The app reads the Spotify data needed to show your saved albums, profile, tracks, genres, and recently played music. Your listening status is stored locally and is never sent back to Spotify as a separate “listened” action.

## Build from source

If you would like to run the app locally or contribute to its development, you’ ll need:

- Node.js 18 or newer
- Rust
- The platform prerequisites for Tauri 2

```bash
# Run the desktop app in development mode
npm run tauri:dev

# Run the frontend only
npm run dev

# Create the frontend production bundle
npm run build

# Check the Rust backend
cd src-tauri && cargo check

```

To create local release bundles:

```bash
./scripts/build-release.sh

```

To update the project version before building, pass the new semantic version:

```bash
./scripts/build-release.sh 0.1.5

```

When a version is supplied, the script updates the app manifests and release metadata, then creates a local `v ` Git tag after a successful build. The tag is not pushed. The script creates a macOS DMG; release publishing is intentionally manual for now. See the Crow CI v6.5 workflow documentation for the CI setup.

Project structure

```text
src-tauri/src/       Tauri and Rust backend
src/                 Frontend UI and styles
scripts/             Local build scripts
.crow/               Crow CI workflows

```

The backend handles Spotify authentication, local caching, syncing, and secure token storage. The frontend is a Vite-bundled vanilla JavaScript app with a custom dark theme.

Crow CI currently runs checks for pushes and pull requests. Release publishing is manual until a release workflow is designed and added.

## Support the project

Albums Vault is free and open source. If it helps you spend less time scrolling and more time listening, you can support me on Ko-fi. It helps keep development going.

## License

MIT © Ricardo Carvalho

# FlarePeek - a browser extension devtools for Cloudflare Workers developers - Chrome Web Store

## 关联链接

- http://127.0.0.1:8888/callback

## 导航

- 项目页：[[10-项目/codefloe.com_d3771bc6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
