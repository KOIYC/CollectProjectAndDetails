---
type: "corpus"
item_id: "cc9ba6a8e567887e"
title: "Show HN: A focused, fullscreen, side-by-side terminal-based Git review tool"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109591"
project_url: "https://slobodan.me/hawkshaw"
author: "slobodan_"
published_at: "2026-07-30T13:19:06Z"
captured_at: "2026-09-21T03:11:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_slobodan_
  - story_49109591
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: A focused, fullscreen, side-by-side terminal-based Git review tool

> [!info] 一句话导读
> hawkshaw — a terminal git review tool

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109591>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：slobodan_　|　发布：2026-07-30T13:19:06Z
> 项目链接：<https://slobodan.me/hawkshaw>
> 采集：2026-09-21T03:11:18+08:00　|　id：`cc9ba6a8e567887e`

## 正文

theme =
 "color"
 |
 "noir"
hawkshaw — a terminal git review tool
░▒ ███
 ██████ ███ ███ ████
 ▓██▒ ███ ███ ▓██████ ███░ ▓███▒ ████
 ░█▓ ███▓ ███ ████████ ███ ███ ███████░ ████ █████ ███░
 ▒ ███▓ ███▓ ███ ███▓ ████ ███ ████ ███ ███ ███ ████ ████ █████ ███
████ ███▓ ██████▓ ████ ████ ███ ███▓ ███ ███▓ ███░ ████ ███ ░███ ███ █████ ███
████ ███▓ ███████ ████ ████ ████ ████████ ██████ █████████ ███ ███ ███▒██░██████
████ ███▓ ░███ ███ ███ █████ ███▓ ███████ ██████ ████ ▓███ ███ ███ ██████ ██████
████ ███▓ ████ ███ ███ █████ ███ ████████ █████ ███ ███ █████████░ ██████ █████
█████████▓ ███░ ███ █████████▒███ ████▒███ ███ ████ ███ ███ █████████▓ ▓█████ ▓████
█████████▓ ███ ███▓ ██████ ██████ ████ ███▓ ███ ████ ███ ███ ███ ████ ████ ██▓▒
████ ███▓ ███ ████ ▒█████ ▒█████ ████ ████ ████████ ███ ███ ███
████ ███▓ ░█████████ █████ ████▓ ████ ████ ██████
████ ███▓ ████ ███ █████ ████ ██▒
████ ███▓ ███▓ ███
████
A focused, fullscreen, side-by-side git review tool
 for your terminal. hawkshaw walks you through the unstaged changes in a working
 tree, one file at a time, and lets you render a verdict on every hunk
 before you commit.
 When it exits, the index is staged exactly as you decided. You run
 git commit yourself.
$
 curl -fsSL https://slobodan.me/hawkshaw/install.sh | sh
 copy
GitHub ↗
 Demo ↓
 Install ↓
Demo video
Your browser does not support embedded video.
 Download the demo instead.
Screenshots
Side-by-side split: old left, new right, changed lines aligned
Unified inline view for narrower terminals
Keyboard navigation: the ? help overlay
c copies the hunk as a diff, ready for a second opinion
The minimal theme: high-contrast text, no background fills
The noir theme: film-noir greyscale
j / k or ← → browse · esc close
✕
Why
I review a lot of AI-generated code. You do the same. The terminal tools that
 already exist pull in two directions. Full git clients like lazygit and gitui do
 everything, so they put a busy general-purpose interface between you and the code.
 git diff and git add -p do too little: no real scrolling,
 no fullscreen reading mode. And their keyboard navigation is not great.
hawkshaw takes one job. It puts a large diff in front of you, hunk by hunk, and
 keeps the interface out of the way while you work through it. The scope stays narrow
 on purpose. There is no branch management, no log browsing, no sidebar. You read the
 change, you decide, you move on, with vim and bat muscle memory.
What you get
Keyboard navigation throughout. Everything is a keystroke, with
 vim and bat muscle memory: j / k to scroll,
 y / n to decide, ? when you forget.
 Full keymap ↓
Two layouts, one keystroke. A side-by-side split with changed
 lines aligned across the gap, and a unified inline view for narrower terminals.
 Width picks the layout by default, and t cycles it.
Dark focused diff bands. The focused hunk keeps its syntax
 highlighting over dark green and
 red backgrounds while everything else recedes, so your
 eye lands where the decision is.
Intra-line highlighting marks the words that actually changed,
 with syntax colours still reading through.
Clipboard that survives SSH. c copies the file path
 and current hunk as a unified diff over OSC 52, ready to paste into an AI
 assistant for a second opinion.
Ignores that match git status , from the in-repo
 .gitignore to your global ignore configuration. i adds an
 untracked file to .gitignore without leaving the review.
Viewport virtualization. Only the visible window ever renders,
 so a 10,000-line diff scrolls as fast as a ten-line one.
Done means done. Once every hunk has a verdict, hawkshaw prints
 a short summary and closes the case. No need to press q .
Keyboard navigation
Keys Action
j / k , ↓ / ↑ scroll a line
F / B full page down / up
Ctrl-d / Ctrl-u , Space / b half page down / up
g / G , Home / End top / bottom
J / K next / previous hunk
h / l , ← / → previous / next file
t cycle view: auto, split, inline
y / n stage / skip the current hunk
Y / N stage / skip every remaining hunk in the file
dd discard the current hunk (confirm)
DD discard the whole file back to HEAD (confirm)
u undo the last verdict
c copy the file path and current hunk (as a diff) to the clipboard
r refresh (re-read git status)
i / I add an untracked file, or its directory, to the root .gitignore
? help overlay
q quit (warns if hunks are undecided)
Discards destroy work and always ask first. Binary files take
 whole-file verdicts with the same keys.
Install
Prebuilt binary
curl -fsSL https://slobodan.me/hawkshaw/install.sh | sh
 The script detects your OS and architecture (Linux and macOS, x86_64 and arm64),
 downloads the matching binary from the latest GitHub release, verifies its SHA-256
 against the release checksums before installing anything, and puts
 hawkshaw in ~/.local/bin (or /usr/local/bin
 when run as root).
Docker (recommended)
Running hawkshaw in Docker is the recommended setup. Pin both the script and
 the binary to the same tag, so nothing moves underneath you:
# Dockerfile
RUN curl -fsSL https://github.com/stojanovic/hawkshaw/releases/download/v0.1.0/install.sh \
 | VERSION=0.1.0 PREFIX=/usr/local sh
 From source
You need a Rust toolchain. There is no system libgit2 to install
 first, since git2 builds a bundled copy.
git clone https://github.com/stojanovic/hawkshaw.git
cd hawkshaw
cargo install --path .
Configuration
hawkshaw reads an optional TOML config file, by default from
 ~/.hawkshaw/config.toml . Point it somewhere else with
 --config . Both keys are optional, and a missing file is fine.
theme = "default" # default | minimal | noir
view = "auto" # auto | split | inline
 default is a dark, syntax-friendly scheme with green and red bands
 on the focused changed lines. minimal is high-contrast text with no
 background fills. noir goes black-and-white, film-noir greyscale,
 monochrome down to the syntax — the switch at the top of this page is a nod to
 it.
auto reads the terminal width and takes the side-by-side split at
 120 columns or wider, unified inline below that, re-adapting live as you resize,
 a tmux split included.
The name
I built hawkshaw (no, Claude Code and Codex built it) while working on
 Competitor
 Tracker , an app that tracks your competitors and sends you a list of the most
 important changes every Monday. Competitor Tracker speaks in a film-noir detective
 voice, so the same noir detective theme carried over to this tool.
Hawkshaw is an old slang word for a detective. It goes back to the
 detective character Hawkshaw in Tom Taylor's 1863 play The Ticket-of-Leave
 Man , and it later titled Gus Mager's early twentieth-century newspaper comic
 strip Hawkshaw the Detective . Of all the noir-detective names on the
 shortlist, this one sounds good, types easily, sticks in memory, and is unique
 enough.
MIT licensed
 github.com/stojanovic/hawkshaw
 slobodan.me

## 关联链接

- https://github.com/stojanovic/hawkshaw.git
- https://github.com/stojanovic/hawkshaw/releases/download/v0.1.0/install.sh
- https://slobodan.me/hawkshaw/install.sh

## 导航

- 项目页：[[10-项目/slobodan.me_a8825fa7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
