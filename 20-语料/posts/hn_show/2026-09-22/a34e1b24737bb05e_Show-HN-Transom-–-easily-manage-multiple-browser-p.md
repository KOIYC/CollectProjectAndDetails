---
type: "corpus"
item_id: "a34e1b24737bb05e"
title: "Show HN: Transom – easily manage multiple browser profiles on macOS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49794450"
project_url: "https://github.com/darvid/transom"
author: "darvid"
published_at: "2026-09-21T22:44:44Z"
captured_at: "2026-09-25T00:12:57+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_darvid
  - story_49794450
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Transom – easily manage multiple browser profiles on macOS

> [!info] 一句话导读
> A native macOS browser-profile manager with a floating tab bar and smart link routing.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49794450>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：darvid　|　发布：2026-09-21T22:44:44Z
> 项目链接：<https://github.com/darvid/transom>
> 采集：2026-09-25T00:12:57+08:00　|　id：`a34e1b24737bb05e`

## 正文

# darvid/transom

A native macOS browser-profile manager with a floating tab bar and smart link routing.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-21T19:53:28Z

## Languages

- Pkl
- Shell
- Swift

## Topics

- browser
- browser-profile
- browser-profile-manager
- browser-profiles
- macos
- macos-app
- macos-application
- macos-swift
- macosx

## Top Contributors

- darvid (19 contributions)

---

## README

# Transom

Transom is a native macOS browser-profile shell and web-link router. It
groups windows from the same browser into a profile-oriented stack, adds
a glass tab strip above the browser, and keeps grouped windows together
when moved or resized.

Transom profile tabs above a browser window

## Use cases

Opening a link shouldn't require finding and focusing the right browser
profile first. Set Transom as your default browser, then choose where
links open and save rules for the ones you use regularly.

- **Use the right AI account.** Open Claude, ChatGPT, or other AI service
 links from a chat, email, or terminal in the profile that has your
 subscription or team account signed in. No need to click that profile's
 window before opening the link.
- **Route GitHub links by account or organization.** Send
 `github.com/work-org` and its subpaths to your work profile, while
 personal repositories open in your personal profile. Add a more
 specific repository rule when it needs a different account.
- **Keep client and work accounts separate.** Route a client's dashboard
 or a workspace-specific path to its dedicated profile instead of
 opening it in whichever account you used last.
- **Choose once for unfamiliar links.** Search for a profile in the
 launcher and open the link without saving a rule. Hold Option when
 opening a link to override an existing rule for that visit.

## Install

Requires macOS 13 or later on an Apple silicon Mac (M1 or newer).
Current releases do not support Intel Macs.

1. Open the latest release
 and download `Transom-VERSION-arm64.dmg` from **Assets**.
2. Open the DMG and drag **Transom** into **Applications**.
3. Eject the disk image, then open Transom from Applications. It does
 not show a Dock icon. Right-click the browser overlay to open
 **Settings…** or quit Transom.
4. Grant access in **System Settings → Privacy & Security →
 Accessibility**. Reopen Transom if the browser overlay does not
 appear after granting access.
5. To route web links through the profile picker, open **Settings… →
 Links**, choose **Make Transom Default Browser…**, and confirm the
 system prompt.

Release downloads are Developer ID–signed and notarized by Apple.

To update, quit Transom from the overlay's right-click menu, download
the latest DMG, and replace the existing app in Applications. Your
settings remain in your user account.

## Supported browsers

Transom discovers installed macOS versions of:

- Google Chrome
- Microsoft Edge
- Brave
- Vivaldi
- Opera
- Arc
- Chromium
- Helium
- Firefox
- Zen

Chromium-family profiles are read from `Local State`. Firefox and Zen
profiles are read from `profiles.ini`. Transom resolves profiles from
window titles and process arguments, retaining validated per-window
assignments while windows remain open. Ambiguous multi-profile Chromium
windows remain unidentified rather than being assigned the wrong
profile.

## Window overlay

- one independent glass container per running browser
- native AppKit segmented tabs with profile-colored indicators
- stable tab order while native window stacking changes
- exact-window switching through Accessibility APIs
- synchronized movement and resizing for grouped windows
- normal macOS window layering, spaces, and fullscreen support
- menu-bar accessory operation with no Dock icon

## Web-link routing

Transom registers `http` and `https` handlers and can be selected as the
default browser from **Settings… → Links**.

Unmatched links open a Spotlight-style profile picker with:

- browser and profile search
- keyboard navigation and Return/Escape handling
- browser icons and profile colors
- saved destinations for an entire site, a path and its subpaths, or an
 exact path, including custom paths

URL picker with profiles and routing scopes

The **Links** section in Settings supports mappings using:

- host globs such as `*.example.com`
- host-scoped path prefixes and exact paths
- path regular expressions
- complete URL regular expressions

Regex rules take priority in list order. Site rules prefer the most
specific matching path. Hold Option when opening a link to bypass
automatic routing and choose a profile once.

Rules are stored at:

```text
~/Library/Application Support/Transom/routing.json
```

## Settings and themes

Open **Settings…** from the overlay’s native right-click menu. Settings
include launch-at-login, window-manager compatibility, browser discovery,
link routing, and overlay themes.
Themes include Automatic, Light, Black, and all four Catppuccin flavors:
Latte, Frappé, Macchiato, and Mocha. The URL opener follows the selected
theme. Profile names and colors can be customized in **Browsers**.
Turn off **Show in picker** beside a profile to hide it from the URL
opener. Existing routing rules can still open that profile.

## Build from source

```bash
mise run run
```

To run checks:

```bash
mise run check
mise run test
```

The built application is written to `.build/Transom.app`.

### Linting and hooks

Install the pinned tools and local pre-commit hooks:

```bash
mise install
mise run hooks:install
```

The hooks check Swift formatting, shell scripts, GitHub workflows,
property lists, Markdown, and spelling without modifying or staging
files. Run all checks or apply formatting fixes explicitly:

```bash
mise run lint
mise run fmt:swift
mise run fmt:markdown
mise run lint:links
```

Link checks access the network and run separately in CI, not during
commits. The generated changelog is excluded from formatting and
spelling checks.

# HQarroum/laymbda

## 导航

- 项目页：[[10-项目/github.com_b71f6b55]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
