---
type: "corpus"
item_id: "a8cdbf87face20ff"
title: "Show HN: NvEnvy – A Notational Velocity (NvAlt) Reboot in Swift. OSS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48325776"
project_url: "https://github.com/kenm47/nvEnvy"
author: "hank2000"
published_at: "2026-05-29T16:48:45Z"
captured_at: "2026-09-21T02:52:58+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-29"
tags:
  - 语料
  - hn_show
  - author_hank2000
  - story_48325776
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: NvEnvy – A Notational Velocity (NvAlt) Reboot in Swift. OSS

> [!info] 一句话导读
> Fast, keyboard-driven note-taking app for macOS — a modern rebuild of nvALT in Swift/SwiftUI.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48325776>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：hank2000　|　发布：2026-05-29T16:48:45Z
> 项目链接：<https://github.com/kenm47/nvEnvy>
> 采集：2026-09-21T02:52:58+08:00　|　id：`a8cdbf87face20ff`

## 正文

# kenm47/nvEnvy

Fast, keyboard-driven note-taking app for macOS — a modern rebuild of nvALT in Swift/SwiftUI.

- Stars: 9
- Forks: 0
- Watchers: 9
- Open issues: 2
- License: MIT License
- Default branch: main
- Created: 2026-05-19T14:59:42Z

## Languages

- Swift

## Top Contributors

- kenm47 (59 contributions)

---

## README

# nvEnvy

A fast, keyboard-driven note-taking app for macOS. A modern rebuild of nvALT built with Swift and SwiftUI, targeting macOS 14+.

## Screenshots

| Horizontal layout | Vertical layout |
|---|---|
| nvEnvy with the note list and tags pane side-by-side | nvEnvy with the note list stacked above the tags pane |

## Install

- **Mac App Store** — Get nvEnvy on the Mac App Store.
- **Direct download (DMG)** — Notarized, hardened-runtime build with Sparkle auto-update, available from GitHub Releases.
- **Build from source** — See Build Instructions below.

Requires macOS 14 Sonoma or later. Universal (Apple Silicon + Intel).

## Features

- **Instant search** — Type to search, Return to create. Incremental filtering with phrase search support.
- **Plain-text Markdown** — Notes stored as plain `.md` files with YAML frontmatter for tags and dates.
- **Keyboard-first** — Full keyboard navigation: ⌘L to search, ⌘J/K to navigate, Escape to go back.
- **iCloud sync** — Drop your notes folder in iCloud Drive for seamless sync with conflict resolution.
- **Wikilinks** — `[[link to note]]` with autocomplete and click-to-navigate.
- **Tags** — Frontmatter tags, batch tagging, tag sidebar with counts, Finder tag mirroring.
- **Markdown preview** — Live HTML preview with custom CSS, source view, and Print/Save HTML.
- **Import/Export** — Import from Markdown, RTF, RTFD, HTML, PDF, Word, web archives. Export to plain text, HTML, RTF, Word.
- **nvALT migration** — One-click import from nvALT with OpenMeta tag migration.
- **Bookmarks** — Save and recall search queries with keyboard shortcuts (⌘1-9).
- **URL schemes** — `nvenvy://find/title` and `nvenvy://make?title=...&body=...` for automation.
- **AppleScript & Shortcuts** — Full scripting support via `.sdef` and App Intents.
- **Services menu** — Create notes from selected text in any app.
- **Auto-update** — Sparkle integration for direct-download (DMG) builds; the Mac App Store build receives updates via the App Store.
- **Localized** — English, German, French, Italian, Portuguese (BR), Chinese (Simplified).

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| ⌘L | Focus search field |
| Return | Create or select note |
| Escape | Return to search |
| ⌘J / ⌘K | Next / Previous note |
| ⌘D | Deselect (or snapback) |
| ⌘⇧T | Edit tags |
| ⌘⇧C | Toggle note list |
| ⌘⌥L | Toggle layout (side-by-side / stacked) |
| ⌘B / ⌘I / ⌘Y | Bold / Italic / Strikethrough |
| ⌘T | Plain text style (strip formatting) |
| ⌘] / ⌘[ | Indent / Outdent |
| ⌘⇧L | Insert link from clipboard |
| ⌘⌥V | Paste as Markdown link |
| ⌘⌥C | Copy note link |
| ⌘⌃P | Toggle preview window |
| ⌘⌥U | Toggle preview source |
| ⌘⇧K | Toggle word count |
| ⌘E | Export note |
| ⌘P | Print |
| ⌘S | Save bookmark |
| ⌘0 | Show bookmarks |
| ⌘1-9 | Restore bookmark |
| ⌘R | Rename note |
| ⌘⇧R | Reveal in Finder |
| ⌘⌫ | Delete note |

## Build Instructions

### Prerequisites

- Xcode 15+ with Swift 5.9
- XcodeGen (`brew install xcodegen`)
- macOS 14.0+

### Build the Core Framework

```bash
cd NvEnvyCore
swift build
swift test
```

### Build the App

```bash
cd nvEnvy
xcodegen generate
xcodebuild -project nvEnvy.xcodeproj -scheme nvEnvy build
```

### Run Tests

```bash
cd NvEnvyCore
swift test   # 168 unit tests
```

## Project Structure

```
nvEnvy/
  nvEnvy/         — macOS app target (SwiftUI + AppKit)
  project.yml     — XcodeGen project spec
NvEnvyCore/       — Swift Package (platform-agnostic data layer)
  Sources/
  Tests/
```

## Distribution

See RELEASING.md for archive, code signing, notarization, and DMG creation instructions.

## Privacy

nvEnvy collects nothing. Notes stay on your Mac (and in your iCloud Drive, if you put them there). See PRIVACY.md for the full policy.

## Acknowledgments

- Descended from Notational Velocity by Zachary Schneirov (via Brett Terpstra's nvALT fork).
- Sparkle — auto-update framework (direct-download builds only).
- KeyboardShortcuts by Sindre Sorhus — user-configurable global hotkeys.
- Yams — YAML parsing for frontmatter.
- swift-markdown — Apple's Markdown parser.

Made by Kendall from lunt.co.

## License

nvEnvy is released under the MIT License. You are free to use, modify, and redistribute the source code under the terms of that license. The signed binaries distributed via the Mac App Store and from nvenvy.app are provided as a convenience and are subject to the App Store's own terms.

# vibewarz — bot-vs-bot arena

## 导航

- 项目页：[[10-项目/github.com_8fe6fb2e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
