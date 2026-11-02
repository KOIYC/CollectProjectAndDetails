---
type: "corpus"
item_id: "b5b3d36219f48924"
title: "Show HN: Keypause – lock your Mac's keyboard while you clean it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50327527"
project_url: "https://github.com/destucr/Keypause"
author: "rbtsven"
published_at: "2026-11-01T17:13:47Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_rbtsven
  - story_50327527
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Keypause – lock your Mac's keyboard while you clean it

> [!info] 一句话导读
> Press one button. Wipe your keyboard. Done. A Mac menu bar app that locks every key while a sleepy keycap waits for sunrise.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50327527>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rbtsven　|　发布：2026-11-01T17:13:47Z
> 项目链接：<https://github.com/destucr/Keypause>
> 采集：2026-11-02T09:37:22+08:00　|　id：`b5b3d36219f48924`

## 正文

# destucr/Keypause

Press one button. Wipe your keyboard. Done. A Mac menu bar app that locks every key while a sleepy keycap waits for sunrise.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Homepage: https://destucr.github.io/Keypause/
- Default branch: main
- Created: 2026-11-01T15:27:21Z

## Languages

- Python
- Shell
- Swift

## Topics

- keyboard-cleaning
- macos
- menu-bar-app
- swift

## Top Contributors

- destucr (16 contributions)

---

## README

 Keypause

 Press one button. Wipe your keyboard. Done.
 A menu bar app that turns every key off while you clean, then back on.

 Website · Watch it move (60 fps video)

## Features

- **Every key off**, including shortcuts, function keys and media keys. Mouse and trackpad keep working.
- **Doesn't interrupt you.** A small HUD shows the countdown and an **Unlock** button without stealing focus, so video keeps playing.
- **Starts from anywhere** with `⌃⌥⌘K`, the menu bar, or Terminal.
- **Always ends.** Pick 30 s to 10 min. The keys come back when the timer does.
- **Screen stays awake** while locked.
- **A night that ends in sunrise.** Kip the keycap naps while your keys are off. The sky goes from night to dawn as the timer runs, and he wakes up just before the keys come back. No progress bar.
- **Update checks.** **Check for Updates…** in the menu tells you when a new version is out. Homebrew users get the `brew upgrade` command.
- **Notch-friendly.** On a MacBook with a notch, the HUD grows out of it.

## Install

For Apple silicon Macs (M1 and newer) on macOS 14 or later.

```sh
brew install --cask destucr/tap/keypause
```

Or download `Keypause.dmg` from Releases and drag it to Applications.

Keypause isn't notarized (no paid Apple developer account), so after a manual download, right-click → **Open** the first time. Homebrew handles this for you.

On first run, switch Keypause on in **System Settings → Privacy & Security → Accessibility** (called *Device Control and Data Access* on newer macOS). The welcome window has a button that opens it.

## Terminal

```sh
keypause start       # your chosen duration
keypause start 90    # 90 seconds ("90s" and "2m" work too, up to 5 minutes)
keypause stop        # unlock early
keypause check       # check for updates
```

Homebrew installs the `keypause` command for you. If you installed another way:
`ln -s /Applications/Keypause.app/Contents/Resources/keypause /usr/local/bin/keypause`

Raycast and Shortcuts can open `keypause://start` and `keypause://stop`.

## Privacy

Keypause never reads, stores or sends your keystrokes. Its only network request is an update check against this project's public GitHub releases, at most once a day, and it sends nothing about you. Turn it off from the menu (**Check Automatically**). It never installs anything by itself.

## Build

Requires macOS 14+ and Xcode.

```sh
./Scripts/build.sh && open dist/Keypause.app
```

## License

MIT © Destu Cikal · Need help?

# renderpdf-js

## 关联链接

- https://destucr.github.io/Keypause/

## 导航

- 项目页：[[10-项目/github.com_5d5f1791]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
