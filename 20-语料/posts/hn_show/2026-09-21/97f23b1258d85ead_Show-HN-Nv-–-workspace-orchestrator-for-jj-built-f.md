---
type: "corpus"
item_id: "97f23b1258d85ead"
title: "Show HN: Nv – workspace orchestrator for jj built for parallel agent workflows"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47955188"
project_url: "https://github.com/eersnington/jj-navi"
author: "Sreenington"
published_at: "2026-04-29T21:47:38Z"
captured_at: "2026-09-21T02:52:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_Sreenington
  - story_47955188
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Nv – workspace orchestrator for jj built for parallel agent workflows

> [!info] 一句话导读
> jj-navi is workspace orchestrator for Jujutsu (jj), built for parallel human and AI agentic workflows

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47955188>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Sreenington　|　发布：2026-04-29T21:47:38Z
> 项目链接：<https://github.com/eersnington/jj-navi>
> 采集：2026-09-21T02:52:31+08:00　|　id：`97f23b1258d85ead`

## 正文

# eersnington/jj-navi

jj-navi is workspace orchestrator for Jujutsu (jj), built for parallel human and AI agentic workflows

- Stars: 24
- Forks: 2
- Watchers: 24
- Open issues: 3
- License: MIT License
- Homepage: https://git.new/jj-navi
- Default branch: main
- Created: 2026-03-09T22:12:42Z

## Languages

- JavaScript
- Rust

## Top Contributors

- eersnington (107 contributions)
- github-actions[bot] (7 contributions)

---

## README

# jj-navi

Workspace management for Jujutsu, built for parallel human and AI agent workflows.

## The problem

jj workspaces are great for parallel work, but the workflow around it is quite cumbersome:

- **Paths are unmanaged.** `jj workspace add ../name` works, but paths are arbitrary and easy to forget.
- **Cross-workspace visibility is stale.** jj snapshots the current workspace when you run a command, but not the others. So `jj log` from one workspace can show outdated commits for the rest — files on disk exist, but jj hasn't recorded them yet.
- **Cleanup is awkward.** Forgetting a workspace does not delete its directory, and deleting a directory does not forget the workspace. There is also no guard against removing the one you are currently in.
- **Switching doesn't switch your shell.** `jj workspace` changes the working copy, not your terminal's current directory.

## What `jj-navi` does

`jj-navi` manages workspace lifecycle: naming, paths, switching, visibility, and cleanup.

- **`switch --create`** — go to a workspace, creating it at a deterministic path if it doesn't exist
- **`list`** — snapshot each workspace and show path health, diff stats, commit info, and age
- **`merge`** — merge work from another workspace into the current or named workspace
- **`remove`** — forget a workspace and delete its local directory; refuses current workspace

With shell integration installed, `navi switch` also changes your current directory.

```text
repo/
├── repo                 current workspace
├── repo.feature-auth    navi switch --create feature-auth
└── repo.fix-api         navi switch --create fix-api
```

## Before and after

**Without `jj-navi`**

```sh
jj workspace add ../repo.feature-auth
cd ../repo.feature-auth
# ... do work ...
cd ../repo
jj log                          # stale view of other workspaces
jj workspace list               # names only
jj workspace forget feature-auth
rm -rf ../repo.feature-auth     # directory left behind
```

**With `jj-navi`**

```sh
navi switch --create feature-auth
# ... do work ...
navi switch -
navi list                       # snapshotted, with diff stats and age
navi remove feature-auth        # asks before deleting the workspace directory
```

## Install

```sh
# npm
npm install -g jj-navi

# cargo
cargo install jj-navi --version 0.2.3
```

Binaries: `navi`, `nv`

Minimum `jj`: `0.39.0`
Minimum Node.js (tested): `24`

## Shell integration

Install once so `navi switch` can update your shell's current directory:

```sh
navi config shell install --shell zsh
source ~/.zshrc
```

Supports `bash` and `zsh`. This adds a managed block to your shell rc file.

## Quick start

```sh
navi doctor
navi switch --create feature-auth
navi list
navi switch -
navi remove feature-auth
```

## Commands

```sh
navi switch <workspace>          # switch to a workspace
navi cd <workspace>              # alias for switch
navi switch ^                    # switch to the primary workspace
navi switch -                    # switch to previous workspace
navi switch @                    # switch to current workspace explicitly
navi switch --create <workspace> # create and switch
navi switch -c <workspace>
navi switch --create <workspace> --revision <revset> # create from a revision
navi switch -c <workspace> -r <revset>

navi list                        # human-readable workspace inventory
navi ls                          # alias for list
navi list --json
navi list -j
navi list --json --compact
navi list -j -c

navi doctor [--json] [--compact] # diagnose repo, workspace, and shell state
navi doctor [-j] [-c]

navi merge --from <workspace>     # merge a workspace into the current workspace
navi merge -f <workspace>
navi merge --from <workspace> --into <workspace>
navi merge -f <workspace> -i <workspace>

navi remove <workspace>          # forget a workspace and delete its directory
navi rm <workspace>              # alias for remove
navi remove <workspace> --yes    # skip destructive confirmation
navi remove <workspace> -y

navi config shell init <bash|zsh>
navi config shell install [--shell <bash|zsh>]
navi config shell install [-s <bash|zsh>]
```

## How it works

Config and metadata live inside shared Jujutsu storage:

```text
.jj/repo/navi/config.toml
.jj/repo/navi/workspaces.toml
```

Default workspace path template: `../{repo}.{workspace}`

## Notes

- `switch` can recover from missing jj workspace-path records when it can validate a fallback path
- `switch` warns when it falls back to template-based path resolution
- `list` snapshots healthy workspaces before rendering so parallel changes are visible
- `list` reports missing, stale, or not-current workspaces instead of hiding them
- `list --json` exposes structured `freshness`, `diff`, and `age` fields
- `remove` forgets a workspace and deletes its directory after confirmation; `--yes` skips the prompt
- Supported shells: `bash`, `zsh`

## Special thanks

Inspired by:

- Worktrunk — Git worktree management for parallel AI agent workflows
- jj-ryu — Stacked PRs for Jujutsu

## Art credits

- BoTW Link Pixel Art

## License

MIT

# alexjbarnes/cockpit

## 关联链接

- https://git.new/jj-navi

## 导航

- 项目页：[[10-项目/github.com_f51631af]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
