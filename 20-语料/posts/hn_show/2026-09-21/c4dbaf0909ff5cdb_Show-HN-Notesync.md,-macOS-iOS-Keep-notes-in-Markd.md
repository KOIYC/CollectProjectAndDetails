---
type: "corpus"
item_id: "c4dbaf0909ff5cdb"
title: "Show HN: Notesync.md, macOS/iOS Keep notes in Markdown for agentic workflows"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47962626"
project_url: "https://github.com/klinquist/Notesync"
author: "klinquist"
published_at: "2026-04-30T13:59:33Z"
captured_at: "2026-09-21T02:52:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_klinquist
  - story_47962626
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Notesync.md, macOS/iOS Keep notes in Markdown for agentic workflows

> [!info] 一句话导读
> Default branch: main

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47962626>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：klinquist　|　发布：2026-04-30T13:59:33Z
> 项目链接：<https://github.com/klinquist/Notesync>
> 采集：2026-09-21T02:52:25+08:00　|　id：`c4dbaf0909ff5cdb`

## 正文

# klinquist/Notesync

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- Default branch: main
- Created: 2026-04-24T13:36:05Z

## Languages

- Shell
- Swift

## Top Contributors

- klinquist (47 contributions)

---

## README

# Notesync.md

 Notesync.md is a simple notes app built for organizing quick project thoughts into folders, notes, and timeline-style entries, then keeping them synchronized across Mac, iPhone, and iPad with iCloud.
 Notes are also mirrored to the local filesystem as Markdown files, making them easy to read, back up, edit, or use with project management agents and other developer workflows.

Download Notesync.md for iOS and macOS from the App Store.

## Demo

Notesync.md demo video

## Features

- Organize notes into folders with emoji and accent colors
- Switch between card and list views, with adjustable card sizes
- Favorite folders or notes so they appear at the top of the home screen
- Capture notes as dated entries, with autosave while typing
- Search folders, note titles, and note contents
- Sync across Mac, iPhone, and iPad using CloudKit
- Mirror notes on macOS to local Markdown files

## Markdown Mirror

On macOS, Notesync.md can mirror the CloudKit-backed note tree into a normal folder on disk. Folders become folders, and each note is exported as a single `.md` file:

```text
<mirror root>/
  Project/
    Ideas.md
    Meeting Notes.md
```

This keeps notes available to local tools, scripts, editors, backup systems, and project management agents without giving up iCloud sync between Apple devices.

## Storage

- Cloud sync uses the private CloudKit container `iCloud.com.linquist.notesync`
- The app keeps a local cache for fast editing and offline fallback
- Notes are stored internally as `.note` packages with one Markdown file per entry
- The macOS mirror combines each package into a single readable Markdown file

## Development

- `Notesync.xcodeproj` - Xcode project
- `Notesync/App` - app entry point
- `Notesync/Models` - shared models and preferences
- `Notesync/Services` - repository, Markdown codec, CloudKit sync, and macOS mirror sync
- `Notesync/Views` - browser, creation sheet, note editor, and settings UI
- `scripts/set-version.sh` - updates `MARKETING_VERSION` and optionally `CURRENT_PROJECT_VERSION`
- `scripts/build-macos-dmg.sh` - builds a macOS release app and packages it into a DMG
- `scripts/release-github.sh` - tags the current commit and publishes the DMG to GitHub Releases

## Release

Set a new marketing version and optional build number:

```sh
./scripts/set-version.sh 1.1 2
```

Build a local macOS DMG:

```sh
./scripts/build-macos-dmg.sh
```

That writes the DMG to:

```text
dist/Notesync-<version>-macOS.dmg
```

Publish a GitHub release for the current commit:

```sh
./scripts/release-github.sh
```

Or publish a specific version tag:

```sh
./scripts/release-github.sh 1.1
```

For signed/notarized releases and App Store uploads, copy `scripts/release.local.env.example` to `scripts/release.local.env` and fill in your App Store Connect API key values. `scripts/release.local.env` is ignored by git and is loaded automatically by the release scripts.

Local builds default to unsigned DMGs. To sign for distribution:

```sh
SIGN_FOR_DISTRIBUTION=1 ./scripts/build-macos-dmg.sh
```

To build a signed and notarized DMG:

```sh
cp scripts/release.local.env.example scripts/release.local.env
$EDITOR scripts/release.local.env
SIGN_FOR_DISTRIBUTION=1 NOTARIZE_DMG=1 ALLOW_PROVISIONING_UPDATES=1 ./scripts/build-macos-dmg.sh
```

To notarize an already-built DMG:

```sh
./scripts/notarize-macos-dmg.sh dist/Notesync-1.6-macOS.dmg
```

The notarization helper signs the DMG first by default. Set `SIGN_DMG=0` if you need to submit an already-signed DMG without replacing its signature.

To upload iOS and macOS App Store Connect builds without relying on Xcode's account session:

```sh
./scripts/upload-app-store-builds.sh
```

`upload-app-store-builds.sh` requires the App Store Connect API key values by default. It will not fall back to Xcode Accounts unless `ALLOW_XCODE_ACCOUNT_AUTH=1` is set explicitly.

If Developer ID signing fails with `errSecInternalComponent`, update the private key's partition list:

```sh
security set-key-partition-list \
  -S apple-tool:,apple: \
  -s -t private \
  -k "<mac-login-password>" \
  /Users/kris/Library/Keychains/login.keychain-db
```

Keychain-based notarization is still supported if needed, but the App Store Connect API key path above is preferred because it does not depend on Xcode account login state. Store notarization credentials in your keychain with:

```sh
xcrun notarytool store-credentials notesync \
  --apple-id "<apple-id>" \
  --team-id "YYE9CDH9RT" \
  --validate
```

Release notes:

- `build-macos-dmg.sh` uses the project’s configured Developer Team by default
- `DEVELOPER_ID_APPLICATION_IDENTITY` can be set to a specific Developer ID certificate name or hash
- `release-github.sh` requires a clean git working tree
- `release-github.sh` defaults to signed and notarized release builds and expects App Store Connect API key variables
- `release-github.sh` uses the `gh` CLI to create or update the GitHub release

## 导航

- 项目页：[[10-项目/github.com_87f8c641]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
