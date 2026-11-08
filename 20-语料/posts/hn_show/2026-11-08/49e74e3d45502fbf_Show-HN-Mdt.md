---
type: "corpus"
item_id: "49e74e3d45502fbf"
title: "Show HN: Mdt"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50402923"
project_url: "https://github.com/VaibhavAcharya/mdt"
author: "vaibhavacharya"
published_at: "2026-11-07T09:09:52Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_vaibhavacharya
  - story_50402923
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Mdt

> [!info] 一句话导读
> Markdown in terminal: an interactive Markdown and JSON viewer

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50402923>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：vaibhavacharya　|　发布：2026-11-07T09:09:52Z
> 项目链接：<https://github.com/VaibhavAcharya/mdt>
> 采集：2026-11-08T12:50:31+08:00　|　id：`49e74e3d45502fbf`

## 正文

# VaibhavAcharya/mdt

Markdown in terminal: an interactive Markdown and JSON viewer

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-07T08:29:09Z

## Languages

- TypeScript

## Top Contributors

- VaibhavAcharya (6 contributions)
- github-actions[bot] (1 contributions)

---

## README

# mdt

Markdown in terminal. An interactive Markdown and JSON viewer written in TypeScript.

mdt showing syntax highlighted code

## Screenshots

| | |
|---|---|
| Lists, tasks and quotes | Alerts and tables |
| Lists, tasks and quotes | Alerts and tables |
| Mermaid diagrams | Images |
| Mermaid diagrams | Images |
| Math | Search |
| Math | Search |
| Table of contents | Link picker |
| Table of contents | Link picker |
| JSON explorer | Slides |
| JSON explorer | Slides |
| Light theme | Help |
| Light theme | Help |

To try every feature yourself, open the examples: `mdt examples/README.md`.

## Features

- Interactive viewer with keyboard and mouse scrolling
- Syntax highlighted code blocks (Shiki, `github-dark` and `github-light`)
- Headings, bold, italic, strikethrough, lists, blockquotes, GitHub alerts, tables and task lists
- Click a checkbox to toggle the task in the file
- Inline images through Kitty, iTerm2 or a Unicode half-block fallback, local and remote
- OSC 8 hyperlinks, click a link to open it
- Search with `/`, regex supported, smart case, `n` / `N` to move between matches
- Table of contents with `o`, fuzzy heading search with `:`, heading jumps with `[` / `]`
- Relative Markdown links open in the viewer, `Backspace` goes back
- Link picker with `f`
- Click a heading section, list or code block to copy it, `Y` copies the document, `c` copies the nearest code block
- Mermaid flowcharts drawn with box characters (`graph` / `flowchart`, TD, BT, LR, RL)
- LaTeX math to Unicode: `$\alpha + \beta$` renders as `α + β`
- Slide mode with `--slides`, `---` separates slides
- Auto reload when the file changes
- Reads stdin: `curl ... | mdt`
- Multiple files, switch with `Tab` / `Shift+Tab`
- HTML export with `--export html`, self contained with local images inlined
- Dark and light themes, toggle with `t`
- Line numbers in code blocks, toggle with `l`
- Config file at `~/.config/mdt/config.toml`
- Re-wraps on terminal resize
- JSON explorer with collapsible nodes and tables for arrays of objects
- Prints styled text when stdout is not a terminal

## Install

Requires Node 24.

```bash
npm install -g @vaibhavacharya_/mdt
```

From source:

```bash
pnpm install
pnpm build
pnpm link --global
```

## Usage

```bash
mdt README.md                      # view a file
mdt a.md b.md                      # multiple files (Tab to switch)
mdt data.json                      # view a JSON file
cat README.md | mdt                # read from stdin
mdt --slides deck.md               # slide mode
mdt --export html doc.md > out.html
mdt --theme light README.md
mdt -l README.md                   # line numbers in code blocks
mdt README.md | less -R            # styled output without the viewer
```

## Controls

### Navigation

| Key | Action |
|-----|--------|
| `j` / `Down` | Scroll down one line |
| `k` / `Up` | Scroll up one line |
| `Space` / `Page Down` | Page down |
| `b` / `Page Up` | Page up |
| `d` / `u` (or `Ctrl+d` / `Ctrl+u`) | Half page down / up |
| `g` / `Home` | Top |
| `G` / `End` | Bottom |
| `[` / `]` | Previous / next heading |
| `Backspace` | Go back after following a local link |
| Mouse wheel | Scroll |

### Search

| Key | Action |
|-----|--------|
| `/` | Open search (regex supported) |
| `Enter` | Run search |
| `n` / `N` | Next / previous match |
| `Esc` | Clear search |

### Features

| Key | Action |
|-----|--------|
| `o` | Table of contents |
| `:` | Fuzzy heading search |
| `f` | Link picker, type a number and `Enter` |
| `t` | Toggle dark / light theme |
| `l` | Toggle line numbers in code blocks |
| Click heading / list / code block | Copy it |
| Click checkbox | Toggle the task in the file |
| `Y` | Copy the document |
| `c` | Copy the nearest code block |
| `Tab` / `Shift+Tab` | Next / previous file |
| `h` / `?` / `F1` | Help |
| `q` / `Ctrl+C` | Quit |

### JSON

| Key | Action |
|-----|--------|
| `j` / `k` | Move cursor |
| `Enter` / `Space` | Expand or collapse |
| `l` / `Right` | Expand |
| `h` / `Left` | Collapse, or go to parent |
| `L` / `H` | Expand all / collapse all |

### Slides

| Key | Action |
|-----|--------|
| `Right` / `Space` / `l` / `j` / `Down` / `Page Down` | Next slide |
| `Left` / `b` / `h` / `k` / `Up` / `Page Up` | Previous slide |
| `g` / `Home` | First slide |
| `G` / `End` | Last slide |

## Configuration

`~/.config/mdt/config.toml` (or `$XDG_CONFIG_HOME/mdt/config.toml`):

```toml
theme = "dark"        # "dark" or "light"
line_numbers = false  # line numbers in code blocks
width = 0             # display width, 0 = terminal width
```

CLI flags override the config file.

## CLI

```
mdt [OPTIONS] [FILES]...

Options:
  -T, --theme <THEME>      Theme: dark or light
  -w, --width <WIDTH>      Display width override (0 = auto)
  -s, --slides             Slide mode (--- as slide separators)
  -l, --line-numbers       Show line numbers in code blocks
      --export <FORMAT>    Export format (html)
      --no-color           Disable colors
  -h, --help               Print help
  -V, --version            Print version
```

## Development

```bash
pnpm dev README.md   # run from source
pnpm test
pnpm typecheck
pnpm build
```

## 导航

- 项目页：[[10-项目/github.com_27c10f02]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
