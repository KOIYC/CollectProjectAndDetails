---
type: "corpus"
item_id: "a7c0d7b596436b6b"
title: "Show HN: Twine is a meta-harness with workflows, cross-agent memories and traces"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50189550"
project_url: "https://github.com/standing-desks/twine"
author: "SurfingAlpaca"
published_at: "2026-10-22T00:33:36Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-22"
tags:
  - 语料
  - hn_show
  - author_SurfingAlpaca
  - story_50189550
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Twine is a meta-harness with workflows, cross-agent memories and traces

> [!info] 一句话导读
> standing-desks/twine

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50189550>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：SurfingAlpaca　|　发布：2026-10-22T00:33:36Z
> 项目链接：<https://github.com/standing-desks/twine>
> 采集：2026-10-22T09:46:18+08:00　|　id：`a7c0d7b596436b6b`

## 正文

# standing-desks/twine

Agentic Development Environment for macOS

- Stars: 30
- Forks: 3
- Watchers: 30
- Open issues: 8
- License: MIT License
- Homepage: https://standing-desks.github.io/twine/
- Default branch: main
- Created: 2026-09-26T18:12:06Z

## Languages

- C
- JavaScript
- Makefile
- Rust
- Shell
- Swift
- Tree-sitter Query

## Top Contributors

- aravind-n (149 contributions)
- ImLordMegatron (6 contributions)
- dependabot[bot] (5 contributions)

---

## README

 Twine

 A native macOS workspace for coordinating coding agents.

 Install ·
 Quick start ·
 User guide ·
 Contributing

Twine is the terminal-first collaboration layer for AI coding agents.
Bring agents together through controlled workflows, visual traces, and cross-agent memory.

## Install

Twine requires **macOS 26 or later** on **Apple Silicon**.

Install it with Homebrew:

```sh
brew install --cask standing-desks/tap/twine-ade
```

Then open Twine from Applications.

To install manually instead, download the `.dmg` from the
latest release, open it,
and drag **Twine** onto **Applications**.

To update a manual install, see the
install notes.

Agent workflows also need at least one supported harness
installed and signed in. Terminal workflows need nothing else.

## Quick start

This takes about a minute and needs no agent harness.

1. Open Twine and choose **Open Folder…** (⌘O). Pick any project folder.
2. Create a session. A session groups the work for one task.
3. Add a workflow in a new tab and choose **Terminal**.
4. Run a command in the terminal, for example `git status`.

You should see the command's output in the terminal and one step for that
command in the Traces panel. Selecting the step jumps to its output.

To run your first agent workflow, add another tab and choose **Adversarial**.
Pick a harness for the implementer and for the reviewer, start the workflow, and
type a task in the implementer's terminal. When the implementer submits its
completion, the reviewer's terminal receives the work and either approves it or
sends changes back.

## Usage

A **session** is a named body of work in a folder. Each top-level tab in a
session is a **workflow**. Select a built-in workflow or create your own agent graph:

| Workflow | How it works |
| --- | --- |
| Terminal | A plain shell, with optional split panes. |
| Single agent | One interactive coding agent. |
| Adversarial | An implementer does the task; a reviewer approves it or requests changes. |
| Coordinator | A planner sends a shared plan to two workers. A coordinator waits for both results and checks their work. |
| Custom | Your own graph of agents and event links. Run agents in parallel, stream pieces, review results, or compare times. |

Click **+**, then **Create your own**, to open the native graph editor in the new
tab. Saved workflows are TOML files in `$XDG_CONFIG_HOME/twine/workflows`
(default `~/.config/twine/workflows`). Copy these files to share workflows or keep them
in version control. Agent instructions use native harness instruction channels;
setup does not start agent work.

Common tasks, each covered in the
user guide:

- **Advance a workflow yourself.** Use **Mark done…** to submit a completion,
 review decision, or assignment on an agent's behalf. See
 agent workflows.
- **Split a terminal** into up to four panes, and paste images or drop files
 into a pane as paths. See
 terminal panes.
- **Browse and edit files** in the open folder with syntax highlighting. See
 files.
- **Change the terminal font** in **Twine → Settings…** (⌘,), which edits
 `~/.config/twine/config.toml` and applies changes on save. See
 configuration.

  ```toml
  [terminal]
  font_family = "JetBrains Mono"
  font_size = 13.0
  ```

- **Inspect recorded agent activity** in **Traces → In Depth**. Overview shows
 activity counts and an **Inspect activity** action. LLM calls include public
 responses/summaries, model and usage details when the harness supplies them;
 missing timings or request bodies remain marked as unrecorded. **Show full
 details** opens complete saved inputs and results.
 The storage control shows usage, pins a step, and clears completed, unpinned
 details. Twine keeps compact metadata in SQLite and deduplicates large details
 in adjacent files. Active steps and pinned details can exceed the cache budget.
 Native harness files remain untouched.

  ```toml
  [traces]
  detail_budget_mb = 512
  retention_days = 90 # Closed, unpinned workflows; 0 disables age expiry.
  ```

 Saved Codex, Claude Code, Pi, and OMP conversations can recover activity for
 their linked steps. Recovery uses native IDs or an unambiguous prompt/time
 match within the same conversation. It cannot recover data absent from both
 the observer and native history. OpenCode and Antigravity use live observers.

### Supported harnesses

A **harness** is the external agent CLI that fills a role. Twine finds each one
by its command on your shell's `PATH`:

| Harness | Command | Prompt and tool detail in Traces |
| --- | --- | --- |
| Codex | `codex` | Yes |
| Claude Code | `claude` | Yes |
| pi | `pi` | Yes |
| OMP | `omp` | Yes |
| Antigravity | `agy` | Yes; model invocation details where exposed |
| OpenCode v2 | `opencode` | Yes |

Install and authenticate harnesses separately. Model choices come from each
harness's own CLI, and provider access and usage charges follow your harness
configuration. Twine never edits your harness config files.

## Project status

Twine is in **early development**. It is usable day to day, but features,
integrations, and saved formats can change between releases, and there are no
stability guarantees yet. The changelog lists what changed in
each release.

Known limitations:

- Agents run directly in the open folder. Twine does not create worktrees or
 sandboxes, and file ownership between parallel workers is advisory.
- Twine is an interactive desktop app. It does not run workflows unattended or
 headless.
- Harness support depends on CLI versions, and a harness update can break an
 integration until Twine catches up.
- Tracing is best effort. Recorded terminal output is capped at 64 MiB per
 terminal and 512 MiB overall, so older output can expire.
- Resuming a conversation depends on the harness recording a session handle.

## Contributing

Contributing Guide · Developer Certificate of Origin

Bug reports and feedback on real workflows are welcome in
GitHub Issues. Include your macOS,
Twine, and harness versions, what you expected, and what happened. For larger
changes, open an issue to discuss the idea before you start. Changes reach
`main` through pull requests.

### Build from source

You will need:

- **Xcode 27.0**, selected as the active developer toolchain. Command Line Tools
 alone are not enough.
- The **Xcode Metal Toolchain**: `xcodebuild -downloadComponent MetalToolchain`.
- **Stable Rust**, installed through rustup.

```sh
git clone https://github.com/standing-desks/twine.git
cd twine
make debug
open out/debug/Build/Products/Debug/Twine.app
```

Debug builds keep their data in `out/runtime/debug/`, separate from an installed
copy of Twine.

### Check your changes

```sh
make fmt      # format the library and the app
make check    # lint and unit-test the library and the app
make          # list every target
```

`make ui-test` runs the UI suite and takes over the desktop while it runs.

### Find your way around

| Path | Contents |
| --- | --- |
| `macOS/` | The SwiftUI and AppKit front end. |
| `twine-core/` | The Rust application library that owns behavior and saved state. |
| `twine-bridge/` | The C ABI adapter between the two. |
| `docs/` | Source for the website and guides. |

The development guide
covers setup, harness integration, and releases.
CONTEXT.md defines the terms used in the code and UI, and
AGENTS.md holds the repository conventions.

## Security

Please report vulnerabilities privately through
GitHub security advisories
instead of a public issue.

## Acknowledgments

Thank you to AI Tinkerers Seattle for the
opportunity to demo and premiere Twine. Twine's terminal emulation uses
SwiftTerm.

## License

Twine is available under the MIT License.

# ChatGPT Plugins | Browse and add plugins to ChatGPT

## 关联链接

- https://github.com/standing-desks/twine.git
- https://standing-desks.github.io/twine/

## 导航

- 项目页：[[10-项目/github.com_3d14f802]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
