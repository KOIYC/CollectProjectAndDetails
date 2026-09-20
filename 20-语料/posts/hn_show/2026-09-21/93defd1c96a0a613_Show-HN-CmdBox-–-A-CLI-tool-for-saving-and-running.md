---
type: "corpus"
item_id: "93defd1c96a0a613"
title: "Show HN: CmdBox – A CLI tool for saving and running parameterized commands"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48732113"
project_url: "https://github.com/PhantomLambSoft/CmdBox"
author: "MalloyDelacroix"
published_at: "2026-06-30T12:58:32Z"
captured_at: "2026-09-21T02:53:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_MalloyDelacroix
  - story_48732113
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: CmdBox – A CLI tool for saving and running parameterized commands

> [!info] 一句话导读
> PhantomLambSoft/CmdBox

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48732113>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：MalloyDelacroix　|　发布：2026-06-30T12:58:32Z
> 项目链接：<https://github.com/PhantomLambSoft/CmdBox>
> 采集：2026-09-21T02:53:06+08:00　|　id：`93defd1c96a0a613`

## 正文

# PhantomLambSoft/CmdBox

A CLI tool (cb) for storing, tagging, and quickly running aliased commands, with variable substitution, command composition, and multi-line template support.

- Stars: 15
- Forks: 1
- Watchers: 15
- Open issues: 3
- License: MIT License
- Default branch: main
- Created: 2025-12-24T19:35:35Z

## Languages

- Batchfile
- PowerShell
- Python
- Shell

## Topics

- aliases
- automation
- cli
- command-line
- command-manager
- command-runner
- developer-tools
- productivity
- python
- shell
- snippets

## Top Contributors

- MalloyDelacroix (605 contributions)

---

## README

# CmdBox

A fast, structured, and searchable command runner for the terminal.

CmdBox replaces fragile shell history and scattered notes with a clean, organized system for
storing, searching, and executing commands. Designed for anyone who works in the terminal,
from occasional users to seasoned developers.

---

## Why CmdBox?

Most terminal users have commands they run regularly. Some are short. Many are long and
complex, packed with flags and options that are easy to forget and tedious to type. Recalling them means digging
through shell history, hunting through notes, or searching online every time.

CmdBox gives every command a short, memorable alias. Run it instantly. No retyping, no
searching, no forgetting.

CmdBox isn't a replacement for shell scripting. It's a replacement for the growing pile of aliases and one-off functions
most terminal users accumulate for commands they run often but don't want to memorize, retype, or maintain as shell
functions or scripts.

### How CmdBox Compares

| | Alias | Shell function | CmdBox |
|------------------------------------------------------------------|-------|-------------------------------|--------------------------|
| Named (non-positional) parameters | No | No | Yes |
| Values shared across multiple commands | No | No, unless duplicated | Yes, via saved variables |
| Invocable from any shell without a matching per-shell definition | No | No | Yes |
| Searchable, taggable | No | No | Yes |
| Scoped execution history with rerun | No | No | Yes |
| Real scripting logic (loops, conditionals) | No | Yes | No |
| No installation required | Yes | Yes | No |

See the full comparison here for more details.

---

## Features

- Named commands with short, memorable aliases
- Parameterized templates with saved and runtime variables
- Stored execution context per command (working directory, shell, environment variables, and timeout) with runtime
 overrides
- Command execution history with the ability to rerun past executions
- Tag-based organization and filtering
- Field-based search across commands, variables, and tags
- Multi-line template execution via script
- Rich terminal UI with configurable display fields

---

## Quick Start

#### Save and run a command

```bash
# Save a command under an alias
cb cmd add git-graph "git log --oneline --graph --decorate --all"

# Run it by alias, no subcommand needed
cb git-graph

# List all saved commands
cb cmd list

# Search saved commands
cb cmd search git
```

#### Use variables for flexible commands

```bash
# Save a command with variable placeholders
cb cmd add ssh-connect "ssh <user>@<host> -p <port>"

# Save variable values so they fill in automatically
cb var add user admin
cb var add host 10.0.0.5
cb var add port 22

# Run the command, variables are resolved before executing
cb ssh-connect

# What gets executed:
ssh admin@10.0.0.5 -p 22

# Supply a different value at runtime to override a saved one
cb ssh-connect --host 192.168.1.1
```

---

## Installation

```bash
pip install cmdbox-cli
```

Or install from source:

```bash
git clone https://github.com/PhantomLambSoft/CmdBox.git
cd cmdbox
pip install .
```

After installation, verify it worked:

```bash
cb --version
```

---

## Documentation

Full documentation is available at phantomlambsoft.github.io/CmdBox.

# henryrobbins/open-atp

## 关联链接

- https://github.com/PhantomLambSoft/CmdBox.git

## 导航

- 项目页：[[10-项目/github.com_ff87f275]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
