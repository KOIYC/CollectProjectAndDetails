---
type: "corpus"
item_id: "3e4a2c2d14fa7b47"
title: "Show HN: Pho – TUI for GitHub PRs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50294193"
project_url: "https://github.com/utkarsh261/pho"
author: "stag"
published_at: "2026-10-29T19:02:49Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_stag
  - story_50294193
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pho – TUI for GitHub PRs

> [!info] 一句话导读
> TUI for Github Pull Requests

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50294193>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：stag　|　发布：2026-10-29T19:02:49Z
> 项目链接：<https://github.com/utkarsh261/pho>
> 采集：2026-10-30T09:46:09+08:00　|　id：`3e4a2c2d14fa7b47`

## 正文

# utkarsh261/pho

TUI for Github Pull Requests

- Stars: 9
- Forks: 0
- Watchers: 9
- Open issues: 0
- License: GNU General Public License v3.0
- Homepage: https://github.com/utkarsh261/pho
- Default branch: main
- Created: 2026-04-11T21:13:02Z

## Languages

- Go
- Just

## Topics

- github
- tui

## Top Contributors

- utkarsh261 (72 contributions)

---

## README

 A TUI for GitHub pull requests.

## Features

- **Dashboard** - Auto-discovers repos, lists PRs across *My PRs*, *Needs Review*, *Involving*, and *Recent* tabs with a live preview pane.
- **Jump to repo/PR** - `Ctrl+P` to fuzzy-find and jump to any PR.
- **PR detail** - Browse description, diff, comments, and commits. Sidebar for files and CI checks.
- **Diff navigation** - Line-by-line cursor, `gg`/`G`, `Ctrl+d`/`Ctrl+u`, visual mode for selecting ranges.
- **Inline reviews** - Draft inline comments on diff lines, edit, discard, and batch-submit with a review event. Just like Github web UI.
- **Comments & approvals** - Post top-level comments, review comments, or approve directly.
- **PR actions** - Edit title/body, merge (with method selection), close/reopen, and checkout the branch locally.
- **Commit view** - Inspect individual commits and their diffs.
- **Search** - `/` to search within diffs and descriptions; `n`/`N` to jump between matches.

## Install

```
go install github.com/utkarsh261/pho/cmd/pho@latest
```

Binary lands in `$(go env GOPATH)/bin/pho`.

Or pin a specific version:

```
go install github.com/utkarsh261/pho/cmd/pho@v0.1.0
```

Add it to the `$PATH`:
```
echo 'export PATH="$(go env GOPATH)/bin:$PATH"' >> ~/.zshrc
````

## Usage

Right now, pho looks at only the `cwd` and its direct children directories (if they are actually git repos). So if you have some repositories cloned in a directory, you can either open pho in that directory or:

```
$(go env GOPATH)/bin/pho ~/path/to/dir/containing/all/cloned/repositories
```
or simply start it in the current directory

```
pho
```

## Requirements

- Go 1.25+
- Git
- GitHub CLI (`gh`) — run `gh auth login` to authenticate

## Build

```
go build -o pho ./cmd/pho
```

With `just`:

```
just build
```

## Run

```
./pho
```

Flags:

| Flag | Description |
|------|-------------|
| `--version` | Print version and exit |
| `--debug` | Enable debug logging |
| `--reset` | Clear all caches and exit |
| `--config ` | Path to config file |
| `--root ` | Root directory to scan for git repos (default `.`) |

## Test

```
go test ./...
```

With `just`:

```
just test
```

## Vet

```
go vet ./...
```

With `just`:

```
just vet
```

## Logs

```
tail -f ~/.local/state/pho/debug.log
```

## Why
So that i can build it exactly how i want a tool which i use on a regular basis to be.

# GitHub - phpclaw-php/phpclaw-monorepo: Open-source AI agent framework for PHP. Tools, memory, security guards and a ReAct loop built in. Works with Laravel, Symfony, WordPress, Drupal, Magento, Joomla, OpenCart, PrestaShop. Any LLM provider. MIT. · GitHub

## 导航

- 项目页：[[10-项目/github.com_7c76f101]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
