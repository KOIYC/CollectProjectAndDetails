---
type: "corpus"
item_id: "8fce9d9cfc973b51"
title: "Show HN: Frost – frosted-glass Linux icons where file types say what they are"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49770157"
project_url: "https://github.com/thissayantan/frost-icon-theme"
author: "thissayantan"
published_at: "2026-09-19T21:10:46Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_thissayantan
  - story_49770157
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Frost – frosted-glass Linux icons where file types say what they are

> [!info] 一句话导读
> thissayantan/frost-icon-theme

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49770157>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：thissayantan　|　发布：2026-09-19T21:10:46Z
> 项目链接：<https://github.com/thissayantan/frost-icon-theme>
> 采集：2026-09-20T09:48:16+08:00　|　id：`8fce9d9cfc973b51`

## 正文

# thissayantan/frost-icon-theme

Frosted-glass icon theme for Linux — folders, apps, 134 file types and status icons

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-19T20:22:44Z

## Languages

- Python
- Shell
- TypeScript

## Topics

- glassmorphism
- gnome
- gtk
- icon-theme
- icons
- linux
- papirus
- ubuntu

## Top Contributors

- thissayantan (92 contributions)

---

## README

# Frost

**A frosted-glass icon theme for Linux** — folders, apps, 134 file types and top-bar status icons, each one a
vivid colour seen through a soft pane of frosted glass, with a crisp white symbol on top.

Frost in a Files window, dark and light

```sh
curl -fsSL https://raw.githubusercontent.com/thissayantan/frost-icon-theme/main/install.sh | sh
```
Then pick **Frost** in *GNOME Tweaks → Appearance → Icons* (or run
`gsettings set org.gnome.desktop.interface icon-theme 'Frost'`).

## Why Frost
- **One glass language everywhere** — the same two shapes and a glyph for folders, places, apps and files.
 No macOS lookalikes, no brand logos, no mixed styles.
- **File types that say what they are** — JSON is `{ }`, Markdown is `M↓`, a lock file is a padlock, a
 certificate is a rosette, a Dockerfile is a stack of crates. Colour tells the *kind*, and from 48 px a short
 label (JSON, MD, PEM, LOCK, GO…) tells the exact type. All 134 file types →
- **Fixes for developer files** — GNOME types `bun.lock`, `.env`, Dockerfiles and `.gitignore` as plain text,
 `.ts` as a Qt translation file and `go.mod` as a *tracker-music module*. The optional MIME add-on
 (`--mime`) gives them real types, per user, reversibly.
- **Top-bar status icons you can read** — Wi-Fi, VPN, Bluetooth, volume, microphone (orange while in use),
 battery with charging/charged marks, night light: pixel-exact at 16 px, recoloured by GNOME Shell.
- **Crisp at every size** — small sizes are hand-drawn on the pixel grid, not scaled down. HiDPI `@2x` included.

Before: Yaru. After: Frost

## Install
**One line** (downloads the latest release to `~/.local/share/icons/Frost`; never changes your theme):
```sh
curl -fsSL https://raw.githubusercontent.com/thissayantan/frost-icon-theme/main/install.sh | sh
# with the developer file-type fixes:
curl -fsSL https://raw.githubusercontent.com/thissayantan/frost-icon-theme/main/install.sh | sh -s -- --mime
```
Also on gnome-look.org.

**Manual:** download `Frost-v*.tar.xz` from Releases,
extract it, and copy the `Frost` folder to `~/.local/share/icons/`.

**Arch:** the one-liner works there too; an AUR package will follow once AUR registration reopens.

**Recommended:** install Papirus too
(`sudo apt install papirus-icon-theme`). Frost only ships icons it has redrawn well; everything else falls back to
Papirus, then Adwaita.

**Uninstall:** `sh install.sh --uninstall` (removes the theme and the MIME add-on), then pick another icon theme.

## Compatibility
Made and tested on **GNOME 50 / GTK 4.22, Ubuntu 26.04**. The glass is baked into PNGs (16–256 px, `@2x`), so
it looks the same in GTK 4, GTK 3, Qt/KDE apps and the GNOME Shell app grid. Status icons are plain symbolic SVG
so the shell can recolour them.

 Every size is checked, not just the big one

Selected icons at 16, 24, 48 and 128 px
The whole set on light, dark and wallpaper backgrounds

## The story behind it
Why the default icons bothered me, how the project-stack folder marks work, and what Linux actually thinks
your files are (`.ts` is a Qt translation file, `go.mod` is tracker music):
dev.to
· Medium
· LinkedIn
· Show HN

## FAQ
**Why isn't Firefox / Chrome / VS Code themed?** Frost never redraws trademarked logos. Brand apps keep their
own icon (via Papirus), which is also what their makers ask for.

**An icon I use is missing.** Request it —
include the app's `Icon=` name (from its `.desktop` file) or the file's type (`gio info -a standard::icon FILE`).

## Build it yourself
Requires Bun and Python 3.
```sh
bun install
bun run build           # src/**/*.svg → dist/Frost (PNG @1x/@2x, aliases, index.theme, icon cache)
bun run verify          # lint + index.theme checks + real GTK lookup of every shipped name
bun run install:local   # → ~/.local/share/icons/Frost (+ MIME add-on)
bun run pack            # → dist/Frost-v<version>.tar.xz
```
Design rules: `docs/DESIGN.md`. Pipeline and decisions: `docs/ARCHITECTURE.md`.
How to contribute: `CONTRIBUTING.md`. Shipped vs inherited: `docs/COVERAGE.md`.

## Credits
- Visual direction inspired by **Glassmorphism – Glass Icon set (Free)** by
 Kristaps Elsiņš / uibits
 (CC BY 4.0). Frost's artwork is original — no geometry was copied.
- The Markdown mark (`M↓`) is by Dustin Curtis, public domain (CC0).
- Fallback icons: Papirus, Adwaita.
 Rendering: resvg.
- Built with a lot of help from Claude Code (design reviews, pipeline, pixel hinting).

## License
MIT — icons and tools alike. Use it, change it, ship it.

## 关联链接

- https://raw.githubusercontent.com/thissayantan/frost-icon-theme/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_1f5dfde3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
