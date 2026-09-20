---
type: "corpus"
item_id: "e6879d818794c14c"
title: "Show HN: Mess – a tiny CLI to clean dev clutter"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733263"
project_url: "https://github.com/olzhasar/mess"
author: "olzhasar"
published_at: "2026-06-30T14:33:51Z"
captured_at: "2026-09-21T02:53:03+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_olzhasar
  - story_48733263
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Mess – a tiny CLI to clean dev clutter

> [!info] 一句话导读
> A tiny CLI for removing common development clutter

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733263>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：olzhasar　|　发布：2026-06-30T14:33:51Z
> 项目链接：<https://github.com/olzhasar/mess>
> 采集：2026-09-21T02:53:03+08:00　|　id：`e6879d818794c14c`

## 正文

# olzhasar/mess

A tiny CLI for removing common development clutter

- Stars: 14
- Forks: 1
- Watchers: 14
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2024-10-25T20:18:25Z

## Languages

- Go
- Just
- Makefile

## Topics

- cache
- cleaner
- cli
- disk-cleanup
- disk-space
- tempfiles

## Top Contributors

- olzhasar (18 contributions)

---

## README

# mess

`mess` deletes common temporary development files in your projects. It ships with common cleanup patterns for popular programming languages like caches, build artifacts, bytecode files, linters output, etc.

Why a separate tool instead of a bash script?
- Reports reclaimed disk space
- Easy to configure and override patterns
- Simple and fast
- Reduces the number of bash scripts in the world

## Installation

### Pre-built binaries

Download a ready-to-use pre-built binary for your platform (Linux and macOS are currently supported) in
GitHub releases.

### Install with go

```bash
go install github.com/olzhasar/mess@latest
```

### Building from source

```bash
make install
```

By default, this installs `mess` to `~/.local/bin`. To install elsewhere, set
`PREFIX`:

```bash
make install PREFIX=/usr/local
```

## Usage

**CAUTION:** *this tool deletes files and directories from your filesystem!*

*While the pre-configured patterns should be safe for most users, please, read the patterns list first and ensure it fits your needs. See Patterns*

### Clean a directory

Clean a specific path (scans only direct children by default):

```sh
mess clean ~/my_projects
```

Scan subdirectories too:

```sh
mess clean -r ~/my_projects
```

Print each removed path:

```sh
mess clean -v ~/my_projects
```

Use custom patterns for one run. These replace the configured patterns:

```sh
mess clean -r -p "node_modules,*.pyc" ~/dev/lots-of-js/
```

### Patterns

To display the currently configured patterns, run:

```sh
mess patterns
```

By default, `mess` uses its built-in PATTERNS. To override them you can use either use a `-p` flag or you can create one of these files:

- `~/.mess_patterns`
- ` /mess/patterns`

The user config directory is provided by your operating system. On Linux it's `$XDG_CONFIG_HOME` (defaults to `~/.config`), on Darwin - `~/Library/Application Support/`

Pattern files use one pattern per line. Empty lines and lines starting with `#`
are ignored.

Patterns use a shell glob-style syntax.

Example:

```sh
# Python
*.pyc
__pycache__

# JavaScript
node_modules

# Specific path
foo/bar/
```

## License
MIT

# PenguineDavid/light-weight-logger

## 导航

- 项目页：[[10-项目/github.com_bc5e3436]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
