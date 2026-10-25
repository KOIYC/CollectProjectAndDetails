---
type: "corpus"
item_id: "94e16c477aa67c94"
title: "Show HN: Kolo – share your AI coding sessions with anyone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50231567"
project_url: "https://github.com/komovaar/kolo"
author: "whosgotch"
published_at: "2026-10-25T13:49:15Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_whosgotch
  - story_50231567
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Kolo – share your AI coding sessions with anyone

> [!info] 一句话导读
> Multiplayer AI coding agents. One machine runs them, everybody else opens a link.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50231567>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：whosgotch　|　发布：2026-10-25T13:49:15Z
> 项目链接：<https://github.com/komovaar/kolo>
> 采集：2026-10-25T23:24:35+08:00　|　id：`94e16c477aa67c94`

## 正文

# komovaar/kolo

Multiplayer AI coding agents. One machine runs them, everybody else opens a link.

- Stars: 7
- Forks: 0
- Watchers: 7
- Open issues: 0
- License: GNU Affero General Public License v3.0
- Default branch: main
- Created: 2026-08-11T19:53:09Z

## Languages

- CSS
- Go
- HTML
- JavaScript
- Shell
- TypeScript

## Top Contributors

- komovaar (380 contributions)
- codex (5 contributions)

---

## README

 Kolo

**Multiplayer AI coding agents.**

Run agents on one machine and work together in the browser. Share a link so your
team can watch, type, and take over the same session. Only the host installs Kolo.

CI
Release
License: AGPL-3.0

A shared Codex session in Kolo, with sessions grouped by machine and project

## Why Kolo

- **Work in the same session.** Everyone sees the same terminal. Type a prompt,
 approve a step, or pick up where a teammate left off.
- **Bring your terminal agents.** Built-in adapters for Claude Code, Codex CLI,
 and opencode, with custom agent descriptions for other tools.
- **Give observers a seat.** Read-only members can follow along while the host
 decides who can control sessions.

## Quick start

Kolo is an experimental alpha for trusted teams. Agents run with the host user's
permissions. Start in a dedicated VM with only the projects and credentials you
intend to share; see the isolation setup.

Install on the machine that will run the agents:

```sh
curl -fsSL https://raw.githubusercontent.com/komovaar/kolo/main/install | KOLO_VERSION=v0.1.0 sh
```

Then open a project and start Kolo:

```sh
cd /path/to/project
kolo up
```

Send your team the invitation link printed in the terminal. They open it in a
browser, choose a name, and join. No install or token to paste.

Hosts support Linux and macOS on amd64 and arm64. Use WSL2 on Windows.
For rolling development builds, replace `v0.1.0` with `nightly`.

## How it works

One Go binary runs the hub your team opens and the host that starts agents.
`kolo up` runs both together. Use `kolo serve` and `kolo host` to run them on
separate machines. Hosts connect out to the hub; the hub needs to be reachable
from your team's browsers.

Kolo detects agent status from terminal output, so CLI updates can affect status
and resume behavior. Run `kolo doctor` to check your setup, and see
tested versions and limits for current compatibility.

## Documentation

Start with `kolo help` or `kolo help `.

Reference · Security ·
Contributing · Releases

## License

AGPL-3.0

# Medium

## 关联链接

- https://raw.githubusercontent.com/komovaar/kolo/main/install

## 导航

- 项目页：[[10-项目/github.com_34924010]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
