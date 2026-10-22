---
type: "corpus"
item_id: "633cb1fd3f0fcc88"
title: "Show HN: Switchboard – Mac menu bar app that shows every localhost port"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50183092"
project_url: "https://github.com/destucr/Switchboard"
author: "rbtsven"
published_at: "2026-10-21T15:55:09Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_rbtsven
  - story_50183092
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Switchboard – Mac menu bar app that shows every localhost port

> [!info] 一句话导读
> Free Mac menu bar app that shows every localhost port with its project. Find what's using a port, then open, restart, read logs or stop it. See how your servers…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50183092>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rbtsven　|　发布：2026-10-21T15:55:09Z
> 项目链接：<https://github.com/destucr/Switchboard>
> 采集：2026-10-22T09:46:18+08:00　|　id：`633cb1fd3f0fcc88`

## 正文

# destucr/Switchboard

Free Mac menu bar app that shows every localhost port with its project. Find what's using a port, then open, restart, read logs or stop it. See how your servers connect.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Homepage: https://destucr.github.io/Switchboard/
- Default branch: main
- Created: 2026-10-21T04:50:26Z

## Languages

- Shell
- Swift

## Topics

- dev-server
- developer-productivity
- developer-tools
- docker
- homebrew
- homebrew-cask
- kill-port
- laravel
- localhost
- macos
- menu-bar-app
- menubar
- nextjs
- port-manager
- swift
- swiftui
- vite

## Top Contributors

- destucr (47 contributions)

---

## README

# Switchboard

**Every local port, with its project.**

Switchboard sits in your Mac menu bar and shows everything running on localhost, grouped by the project it belongs to. Open it, restart it, read its logs or stop it without going back to the terminal.

Free and open source. Website · Download

## Features

- **Know what is running.** Every server, grouped by project. Vite, Next.js, Laravel, Django, Docker, Postgres, Redis and more.
- **The right button every time.** Open for web pages. Copy URL for APIs and databases.
- **See what depends on what.** A map shows which servers talk to each other, and warns you before you stop one that others are using.
- **Pick up where you left off.** Stopped servers stay on the list. One click starts the whole project again, in the right order.
- **Share your setup.** Save a `switchboard.json` in your repo. A teammate adds the folder and presses Start stack.
- **No more "port already in use".** Type a port to see who has it. If a port is taken, Switchboard offers the next free one. You can also move a running server to another port, and undo it.

## Install

```sh
brew install --cask destucr/tap/switchboard
```

Or download the zip from Releases.

Switchboard is not notarized yet, so macOS asks you to confirm the first launch. Open System Settings, then Privacy & Security, and click Open Anyway. You can also run this once:

```sh
xattr -dr com.apple.quarantine /Applications/Switchboard.app
```

## How the map decides

A solid line means Switchboard saw an open connection between two of your local servers. A dashed grey line means a project's `.env` file names that port, but no connection was seen. A red line means the other end returned an error or nothing is listening there. A missing line does not prove two servers are unrelated. The dashed box around servers is just the project folder they share.

## Command line

The cask also installs a `switchboard` command for the terminal:

```sh
switchboard status [--json]    # what is running
switchboard export             # write switchboard.json from what you have run
switchboard start              # start the stack in order
switchboard stop               # stop it, front ends first
```

`switchboard.json` holds commands and dependencies only. Environment variables are never saved.

## Build

Needs macOS 14+ and Xcode or the Command Line Tools.

```sh
./build.sh install    # build, copy to /Applications, start
./scripts/check.sh    # build with no warnings, then the self-test
./release.sh minor    # check, bump, tag, publish, update the Homebrew cask (--dry-run first)
```

## Contributing

Versions, the changelog and the release checks are described in RELEASING.md.

## License

MIT

# Play | gembop

## 关联链接

- https://destucr.github.io/Switchboard/

## 导航

- 项目页：[[10-项目/github.com_9678bf16]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
