---
type: "corpus"
item_id: "3cf0fae637128a07"
title: "Show HN: Tinywm – a scrolling window manager for macOS, inspired by Niri"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50122281"
project_url: "https://github.com/bbodi/tinywm"
author: "bbodi"
published_at: "2026-10-16T18:22:27Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_bbodi
  - story_50122281
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Tinywm – a scrolling window manager for macOS, inspired by Niri

> [!info] 一句话导读
> A scrolling window manager for macOS, inspired by niri

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50122281>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：bbodi　|　发布：2026-10-16T18:22:27Z
> 项目链接：<https://github.com/bbodi/tinywm>
> 采集：2026-10-17T13:35:15+08:00　|　id：`3cf0fae637128a07`

## 正文

# bbodi/tinywm

A scrolling window manager for macOS, inspired by niri

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 0
- License: GNU General Public License v3.0
- Default branch: main
- Created: 2026-10-14T09:11:07Z

## Languages

- Shell
- Swift

## Topics

- macos
- niri
- scrolling-window-manager
- swift
- tiling-window-manager
- window-manager

## Top Contributors

- bbodi (4 contributions)

---

## README

 tinywm

 Your windows, on an endless strip.
A scrolling window manager for macOS. No more resizing, overlapping or hunting for windows.

 Download the latest release

---

Every new window opens **next to the one you're using**, on the display you're using, and
nothing else changes size.
The strip simply runs past the edge of your screen. Scroll it with one key or a swipe, and
**every window is exactly where you left it**.

tinywm is inspired by niri, the scrolling window manager for
Linux, and brings its way of working to macOS.

 ▶ Watch the demo with sound

## Why you'll like it

- **Nothing jumps around.** Opening a window never squeezes the others. Your layout stays put.
- **Silky motion.** Windows glide into place with a spring, smooth even on 120 Hz screens.
- **One key does it all.** Hold **right ⌘** and use H J K L or the arrows. Your normal ⌘ shortcuts keep working.
- **Workspaces that stack.** Keep projects apart, one strip each. Flick up or down to switch.
- **See everything at once.** Press **right ⌘ + Esc** for an overview of every window, then pick one.
- **Swipe with your fingers.** Drag the strip with three fingers on the trackpad.
- **Every display gets its own strip.** Move windows between monitors with one key.
- **Your rules.** Keep calculators floating, ignore apps entirely, stop chatty apps from stealing focus, or open an app on a chosen display and workspace.
- **Plain-text config.** One small file, reloaded the moment you save it.

## Install

tinywm needs macOS 14 Sonoma or later on a Mac with Apple silicon.

1. Download `tinywm.zip` from the latest release.
2. Open the zip and drag **tinywm** into your **Applications** folder.
3. Open **tinywm**. Apple has checked and notarized it, so it opens like any other app.

To update, quit tinywm and replace the app with the new one. Your permissions and settings stay.

**Build it yourself instead** (needs Xcode or the Command Line Tools):
```sh
git clone https://github.com/bbodi/tinywm.git
cd tinywm
scripts/bundle-tinywm.sh --install
```
This puts the app in `~/Applications`.

## Get started

When tinywm first opens, a welcome window walks you through the permissions:

- **Accessibility** is required. tinywm uses it to move and resize windows.
- **Screen Recording** is optional. It is only for live window pictures while windows move.

The welcome window also checks the macOS settings that get in the way: trackpad gestures,
Stage Manager, tiling at screen edges, click wallpaper to reveal desktop, other window managers
and Open at Login. Reopen it any time from the menu-bar icon (**Welcome…**).

## The keys

Hold **right ⌘** (the "meta" key) and press:

| Key | Does |
|---|---|
| H J K L or ← ↓ ↑ → | Move between windows |
| ⇧ + the same | Move the window itself |
| U / I, ⌥↓ / ⌥↑ or Page Down / Page Up | Workspace below / above (⇧ takes the window along) |
| . / , | Next / previous display (⇧ takes the window along) |
| W A S D | The display above, left, below or right (⇧ takes the window along) |
| R | Cycle width: ⅓, ½, ⅔ |
| F / C | Full width / centre the window |
| = / − | Wider / narrower |
| [ / ] | Stack the window into its neighbour · ⇧] pops it out |
| T | Float or tile the window |
| V | Focus the floating windows, then the strip again |
| 1 – 9 | Jump to a column |
| Esc | Overview: pick a window with the arrows or Tab, then Return; Esc closes it |
| Q | Close the window |

**Drag with the mouse.** Hold the meta key and drag any window, anywhere inside it. The other
windows make room, and a slot shows exactly where it will land: between two columns, above or
below a window in a stack, or on another display. Let go to drop it there, or press Esc to
cancel. A floating window simply moves.

Prefer ⌃⌥ over right ⌘, or different keys? Change anything in the config.

## Make it yours

Choose **Edit Config…** from the menu bar icon. A few lines go a long way:

```
default-width = 0.5            # new windows take half the screen
bind focus-left = n            # remap any key

float    = com.apple.calculator, System Settings
ignore   = com.apple.finder
no-focus = Slack                # never steals focus

send space = cmd+space          # meta+Space opens your launcher
run shift+return = open -na Ghostty
focus-crosses-displays = on     # past the last column, focus moves to the next display
open-on  = Mail -> workspace 2  # an app always opens on a chosen display or workspace
```

There is more: `meta = control-option` picks ⌃⌥ as the meta key, `gap` sets the space between
windows, `width-presets` sets the widths R cycles through, `swipe-fingers = 4` switches swipes
to four fingers, and `unbind` removes a default key. The config file that tinywm creates lists
every option with a short explanation.

## Good to know

- tinywm only asks for what it needs: Accessibility to move windows, and Screen Recording
 for live window pictures. Nothing leaves your Mac.
- By default, moving windows show as live pictures, which need Screen Recording. To record
 nothing, turn off **Show Live Window Pictures (Screen Recording)** in the menu-bar icon.
 Moving windows then show as cards with the app's icon and the window's title.
- **Open at Login** is in the menu-bar icon and the welcome window. It works from the installed
 app, not from `swift run`.
- Quitting tinywm puts every window back where it was.
- tinywm remembers your layout and restores it after a restart, as long as the apps keep their
 windows open. After a reboot it matches reopened windows by app and title, as far as it can.
 Turn this off with `restore-layout = off` in the config.
- macOS can't hide single windows, so windows on other workspaces wait just off screen.
- Floating windows (meta+T, `float` rules, fixed-size windows) keep their own frame and show
 in the overview. Meta+V focuses them one after another and then returns to the strip.

## Known limitations

- **Full-screen apps** (the green button) live in their own macOS Space, outside tinywm's strip.
- **Some windows refuse to resize**, like fixed-size dialogs and a few apps. tinywm floats them.
 An app that refuses a narrow width, such as Slack, gets wider columns: tinywm learns the
 narrowest width each app takes and remembers it. Drag the window narrower to lower it again.
- **Password fields pause the meta key.** macOS blocks keyboard shortcuts from other apps while
 you type a password. Use ⌃⌥ instead if you need tinywm there.
- **Trackpad swipes clash with macOS gestures** that use the same number of fingers. The welcome
 window and the menu bar icon warn you and link to Trackpad settings.
- **Floating windows are not kept on top.** macOS keeps the active app's windows above every
 other app's, and raising another app's window can make that app take the keyboard. Meta+V
 brings a floating window up by focusing it, and the overview shows all of them.
- **macOS Spaces** aren't tracked separately. Use tinywm's own workspaces instead, and keep to
 one macOS Space per display.
- **Built for Apple silicon** and tested on macOS 14 and later. Intel Macs are untested.

## For developers

See docs/DEVELOPING.md for the architecture, tests and how to build the app.

## License

Copyright (C) 2026 BB.

tinywm is free software under the GNU General Public License v3.0. You may use,
change and share it. If you share a changed version, you must share its source under the same
license. For a license without these terms, contact bodidev@gmail.com.

# btahir/reelbird

## 关联链接

- https://github.com/bbodi/tinywm.git

## 导航

- 项目页：[[10-项目/github.com_011f6d25]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
