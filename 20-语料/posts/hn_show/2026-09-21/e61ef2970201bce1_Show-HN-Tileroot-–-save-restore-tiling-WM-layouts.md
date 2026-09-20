---
type: "corpus"
item_id: "e61ef2970201bce1"
title: "Show HN: Tileroot – save/restore tiling WM layouts (sway, Hyprland, i3)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49119491"
project_url: "https://github.com/Hinikaa/tileroot"
author: "hinikaa"
published_at: "2026-07-31T05:57:43Z"
captured_at: "2026-09-21T03:11:09+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_hinikaa
  - story_49119491
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: Tileroot – save/restore tiling WM layouts (sway, Hyprland, i3)

> [!info] 一句话导读
> Save and restore tiling WM layouts across sway, Hyprland, and i3 — one tool, no daemon, no shell-injection footguns.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49119491>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：hinikaa　|　发布：2026-07-31T05:57:43Z
> 项目链接：<https://github.com/Hinikaa/tileroot>
> 采集：2026-09-21T03:11:09+08:00　|　id：`e61ef2970201bce1`

## 正文

# Hinikaa/tileroot

Save and restore tiling WM layouts across sway, Hyprland, and i3 — one tool, no daemon, no shell-injection footguns.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: master
- Created: 2026-07-30T20:23:25Z

## Languages

- C++
- Makefile
- Shell

## Topics

- cli
- cpp
- dotfiles
- hyprland
- i3wm
- linux
- session-manager
- sway
- tiling-window-manager
- wayland

## Top Contributors

- Hinikaa (5 contributions)

---

## README

# tileroot

Save and restore your tiling window manager's layout across a reboot or crash — sway, Hyprland, and (soon) i3, all with one tool.

## Overview

Every sway/Hyprland/i3 user eventually hand-rolls a shell script that calls `swaymsg`/`hyprctl` + `jq` to save their window layout, and every one of those scripts breaks the next time the WM updates. The one existing attempt at a real tool, `hypr-session-restore`, is Hyprland-only and — by its own README — can't reconstruct the actual tiling layout tree, because Hyprland's IPC doesn't expose one. `i3-resurrect` solves this well for i3, but nothing unifies i3, sway, and Hyprland in one tool.

`tileroot` does. Sway (and i3, once it lands) implement the *same* IPC wire protocol, so exact layout reconstruction there is a solved problem, not a research project. Hyprland's IPC genuinely doesn't expose a split tree, so `tileroot` is honest about it: on Hyprland, `dump` records every tiled window's exact geometry in left-to-right order and `restore` replays that geometry directly, rather than pretending to reconstruct a tree that doesn't exist.

demo

*Recorded live against a real running Hyprland session — not staged.*

## Install

**AUR (Arch, recommended for this audience):**
```
paru -S tileroot
```

**Manual (any distro):**
```
curl -sL https://github.com/Hinikaa/tileroot/releases/latest/download/install.sh | sh
```

**From source:**
```
git clone https://github.com/Hinikaa/tileroot
cd tileroot
make tileroot
```
Requires a C++17 compiler and the `nlohmann-json` header (`nlohmann-json` on Arch, `nlohmann-json3-dev` on Debian/Ubuntu).

## Usage

```
tileroot dump [--workspace NAME] [-o FILE] [--pretty] [--verbose]
tileroot restore [FILE] [--dry-run] [--verbose]
```

`dump` with no `-o` prints session JSON to stdout; `-o FILE` writes it atomically (a crash or Ctrl-C mid-write never corrupts an existing save). `--pretty` prints a human-readable box-drawing tree instead — good for a screenshot, not meant to be parsed. `restore` reads `session.json` in the current directory by default, or a path you give it; `--dry-run` shows what it *would* do without launching anything.

`restore` refuses to run if the target workspace already has windows — it never merges or clobbers. If some windows can't be matched within 5 seconds (app didn't start in time, binary went missing) it logs a warning, places everything it could, and exits non-zero so scripts can detect a partial restore.

## Example

```
# On workspace 1: a browser on the left, a terminal on the right
$ tileroot dump -o ~/.config/tileroot/work.json

# ...reboot, or close everything...

$ tileroot restore ~/.config/tileroot/work.json
2 of 2 windows restored
```

## License note on i3-resurrect

`i3-resurrect` is GPLv3, which is not compatible with this project's MIT license — no code from it is used here. `tileroot`'s sway/i3 backend is a clean-room implementation against the *public* i3-ipc wire protocol specification (the framing and message types sway/i3 themselves document, not `i3-resurrect`'s source), and the window-matching logic is independently designed.

## Security

`restore` launches processes from the saved `cmdline` in your session file. Because sharing session files (dotfiles, "here's my rice") is exactly what this tool is for, `cmdline` is stored as an argument array and executed directly via `posix_spawn` — **never** through a shell. A session file with something like `["echo", "; rm -rf ~"]` in it prints that string literally; it does not run `rm`. See `test_matcher.cpp::test_spawn_does_not_shell_interpret_cmdline` for the regression test that guards this.

## Status

- **Hyprland backend: live-validated.** Written against and tested end-to-end against a real running Hyprland 0.56 session — `dump`, `--pretty`, atomic `-o` writes, schema validation, and the wm-mismatch/occupied-workspace refusal paths all confirmed working against real windows.
- **Sway/i3 backend (`I3ProtocolBackend`): written against the public i3-ipc/sway-ipc specification, not yet validated against a live sway session.** The wire protocol framing and JSON tree-walking logic are unit-testable and covered by the socket-framing code path, but end-to-end validation against a real sway instance is a known open item — see the repo's tracked next steps.
- **i3 support:** not yet wired up (it reuses `I3ProtocolBackend` — same protocol as sway — so it's expected to be a small addition once sway is validated live, not a rewrite).
- **Multi-monitor on Hyprland:** not specifically validated. Single-monitor is the tested case.
- **Scratchpad windows (sway/i3):** not yet captured — the scratchpad workspace's tree shape needs live validation before this backend trusts it.

None of this is silent — every gap above is either a loud error at runtime or a documented limitation, never a quiet wrong answer.

## Stats for nerds

| | |
|---|---|
| Lines of C++ (core + tests) | 1,683 |
| Test functions / assertions | 14 / 36 |
| Runtime dependencies | 1 (`nlohmann/json`, header-only) |
| Binary size (release, unstripped) | 433 KB |
| Binary size (stripped) | 355 KB |
| Compiler warnings (`-Wall -Wextra`) | 0 |
| Shells that never see your `cmdline` | all of them (see Security) |
| Design-review rounds before implementation | 3 rounds, 14 issues caught before a line of code existed |

## License

MIT — see LICENSE.

## 关联链接

- https://github.com/Hinikaa/tileroot/releases/latest/download/install.sh

## 导航

- 项目页：[[10-项目/github.com_9ab468d3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
