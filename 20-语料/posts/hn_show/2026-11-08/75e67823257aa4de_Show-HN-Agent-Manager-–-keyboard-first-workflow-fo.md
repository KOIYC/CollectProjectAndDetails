---
type: "corpus"
item_id: "75e67823257aa4de"
title: "Show HN: Agent Manager – keyboard-first workflow for running many coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50406983"
project_url: "https://github.com/wainmann/agent-manager"
author: "yoanwaidev"
published_at: "2026-11-07T18:56:07Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_yoanwaidev
  - story_50406983
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agent Manager – keyboard-first workflow for running many coding agents

> [!info] 一句话导读
> wainmann/agent-manager

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50406983>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：yoanwaidev　|　发布：2026-11-07T18:56:07Z
> 项目链接：<https://github.com/wainmann/agent-manager>
> 采集：2026-11-08T12:50:31+08:00　|　id：`75e67823257aa4de`

## 正文

# wainmann/agent-manager

Terminal multiplexer for AI coding agents. Run Claude Code, Codex, OpenCode, Gemini CLI and more side by side in one tmux TUI, with live status, worktrees and diff review. Discord: discord.gg/ecS88An7pF

- Stars: 646
- Forks: 74
- Watchers: 646
- Open issues: 120
- License: Apache License 2.0
- Homepage: https://agent-manager.dev
- Default branch: main
- Created: 2026-07-15T16:27:33Z

## Languages

- Go
- PowerShell
- Python
- Shell

## Topics

- ai-agents
- ai-coding-agents
- bubbletea
- claude-code
- code-review
- codex
- command-code
- developer-tools
- gemini-cli
- golang
- grok
- hermes-agent
- mcp-server
- model-context-protocol
- opencode
- pi
- terminal
- terminal-multiplexer
- tmux
- tui

## Top Contributors

- YoanWai (821 contributions)
- ribeirojose (516 contributions)
- zavatskiy (28 contributions)
- ipl31 (28 contributions)
- larroy (27 contributions)
- subbeh (20 contributions)
- dependabot[bot] (17 contributions)
- chancez (11 contributions)
- Sarthak-Shreshtha01 (9 contributions)
- cvas22 (8 contributions)

---

## README

 The fastest developer workflow for every AI coding agent.

 agent manager is a local terminal app that connects to your existing subscriptions and tools.

 English · 简体中文 · 日本語

three agents spawned from the quick prompt bar, one each on Claude Code, Codex and Gemini CLI, tab picking the CLI each time, each new agent landing in the list

Claude Code, Codex, OpenCode, Grok, Gemini CLI, Antigravity CLI, Pi, Command Code, Hermes Agent, Muse Code, Oh My Pi, Cursor CLI, and Kiro CLI run side by side. Each tool runs in its own persistent tmux session.

agent-manager is a thin layer over the CLIs you already have. Each session launches your own installed tool as-is: your login, your subscription, your config files, your MCP servers, and every feature the tool ships all carry over, exactly as they behave in a plain terminal.

Instead of hunting through terminal tabs to see which agent is done and which is stuck, every session shows up in one list with live status, grouped into a project tree you can fold and reorder. You answer any of them without attaching: `space` sends a prompt straight into a session's pane, or spawns a new agent in the selected group. A dead session revives on its own conversation with `v`. And `ctrl+r` opens a full-file diff of what an agent changed, syntax-highlighted, where the comments you leave on lines go back to the agent's pane as one review prompt when you press `C`.

Press `f` on a session to continue its conversation in a separate named fork.

The mouse works across the whole manager. The wheel moves the cursor, a click on a session focuses it, and a click on its row or the mouse back button brings you back. Drag a row by its handle (`⠿` in Advanced, `=` in Compatible) to reorder it or move it into another group, and the `[…]` at the end of every row opens its actions. The divider between the list and the preview drags, and while any message is left, a click on `messages` in the key legend opens it. In a focused pane a drag selects and copies text, and a click on a link opens it in your browser. Settings has a mouse toggle for terminals where you want native selection back. Settings → **symbols** switches between **Advanced** geometric marks (the default) and **Compatible** ASCII marks, with a live preview.

Mouse demo with the geometric marks used by Advanced mode: the wheel moves the cursor, clicks focus and leave sessions, the ⠿ handle drags rows, and […] opens row actions

The tools you use alongside agents live in the same list: `T` opens a shell under the selected agent, or in the selected group, for builds, Git, and one-off commands. An agent can spawn another, send it a message, and wait until it is done: every MCP-capable session carries those tools on launch.

Save named instructions in Settings and reuse them from the New Session form, the quick prompt, a focused session, `spawn --saved`, `send --saved`, or `create_session`. See Saved prompts.

Not here yet: cost tracking.

**Jump to:** Install · Usage · Keys · Diff review · Configuration · Docs site

## Supported tools

Status detection supports **Claude Code**, **OpenCode**, **Codex**, **Grok Build**, **Gemini CLI**, **Antigravity CLI**, **Pi**, **Command Code**, **Hermes Agent**, **Muse Code**, **Oh My Pi**, **Cursor CLI**, and **Kiro CLI**. Each one's launch, revive, fork, and status rules ship in the binary (Hermes, Antigravity, Oh My Pi, Cursor CLI, and Kiro CLI have no fork), so an upgrade brings the current version of all of them (see Configuration). A CLI that is not on the list is a feature request.

## Install

Runs on macOS and Linux, natively on Windows with psmux, and inside WSL2.

### Homebrew (macOS / Linux)

```bash
brew install agent-manager
```

Installs tmux with it if missing, and Homebrew runs on git, so both dependencies are covered. This is the homebrew-core formula, which builds from source. For the prebuilt binary, `brew install --cask yoanwai/tap/agent-manager`.

### Scoop (Windows)

```powershell
scoop bucket add yoanwai https://github.com/YoanWai/scoop-bucket
scoop install yoanwai/agent-manager
```

Installs the version published in that bucket, and Scoop installs psmux with it. The bucket is updated on its own, so it can lag the latest release. To update, close agent-manager and run `scoop update agent-manager`. A global install uses `scoop update agent-manager --global` in an elevated PowerShell. The in-app updater shows those instructions instead of replacing Scoop's binary.

### Install script (macOS / Linux)

Download the script, read it, then run it. `sh install.sh` runs only after that download succeeds.

```bash
curl -fsSL -o install.sh https://raw.githubusercontent.com/wainmann/agent-manager/main/install.sh &&
sh install.sh
```

That copy is the script on `main`. It is not in `checksums.txt`. The release that first attaches `install.sh` lists that file in `checksums.txt`. Once it does, download the attached file and, when `gh` is logged in, verify it before the script runs:

```bash
curl -fsSL -o install.sh https://github.com/wainmann/agent-manager/releases/latest/download/install.sh &&
gh attestation verify install.sh --repo wainmann/agent-manager &&
sh install.sh
```

The release URL above has no file until that tag exists, so the first command is the one that works until then. Older releases verify with `--owner YoanWai --signer-repo YoanWai/agent-manager` in place of `--repo wainmann/agent-manager`.

Downloads the latest release for your platform, verifies it against the published checksums, and installs it to `~/.local/bin`. Then it checks for tmux 3.1+ and git. On macOS it offers Homebrew, and offers to install Homebrew first when that is missing. On Linux it offers apt, dnf, pacman, zypper, apk, or Homebrew, and on a desktop it also offers the clipboard and notification packages. It prints the command when you decline. A run with no terminal skips the prompt and still installs the binary. Set `AGENT_MANAGER_INSTALL_DIR` for another directory, `AGENT_MANAGER_VERSION` to pin a version, and `AGENT_MANAGER_INSTALL_DEPS=1` to answer the dependency prompt up front (`=0` to skip it). `AGENT_MANAGER_VERIFY_ATTESTATION=1` refuses the install unless `gh attestation verify` accepts the downloaded archive. When that check fails, the script tries again with `--owner YoanWai --signer-repo YoanWai/agent-manager`, which older releases need, and stops only if both fail. Leave it unset to install on a machine without `gh`. `gh` uses one exit status for a rejected attestation, a missing login, and a network error, so the script does not try to tell those apart.

Running it without a file to read first:

```bash
curl -fsSL https://raw.githubusercontent.com/wainmann/agent-manager/main/install.sh | sh
```

### Verified zip (Windows)

Download the Windows zip for your architecture and `checksums.txt` from the same release. Compare its SHA-256 with the matching line in `checksums.txt` before extracting it. The manual Windows install gives the PowerShell commands, optional provenance verification, and dependency setup.

### Install script (Windows)

Download the script, read it, then run it. The installer runs only after that download succeeds. Windows PowerShell 5.1 has no `&&`, so the guard is `if ($?)`. Until the release attaches `install.ps1`, the file to read is the copy on `main`. That copy is not in `checksums.txt`.

```powershell
irm https://raw.githubusercontent.com/wainmann/agent-manager/main/install.ps1 -OutFile install.ps1
if ($?) {
    Get-Content .\install.ps1
    Unblock-File .\install.ps1
    powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
}
```

Once the release attaches `install.ps1` and lists it in `checksums.txt`, download that file instead. Logged in to `gh`, verify it after the download and before the installer. Older releases verify with `--owner YoanWai --signer-repo YoanWai/agent-manager` in place of `--repo wainmann/agent-manager`. A missing `gh` stops the example: PowerShell would otherwise keep the previous `$LASTEXITCODE`, and a `0` from an earlier command would look like a successful verify. That release URL has no file until that tag exists.

```powershell
irm https://github.com/wainmann/agent-manager/releases/latest/download/install.ps1 -OutFile install.ps1
if ($?) {
    Get-Command gh -ErrorAction Stop | Out-Null
    if ($?) {
        gh attestation verify .\install.ps1 --repo wainmann/agent-manager
        if ($LASTEXITCODE -ne 0) { throw 'attestation verification failed' }
        if ($LASTEXITCODE -eq 0) {
            Get-Content .\install.ps1
            Unblock-File .\install.ps1
            powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
        }
    }
}
```

On a Windows client with no execution policy set, the effective policy is Restricted, so every `.ps1` is refused. `-ExecutionPolicy Bypass` applies to that process only, after you have read the file. Where the policy is already RemoteSigned, `Unblock-File` then `.\install.ps1` is enough. RemoteSigned refuses an unsigned script that still has the Mark of the Web. A browser download sets that mark. `irm -OutFile` does not (Microsoft documents `Invoke-WebRequest` as not marking the Internet zone). `Unblock-File` does nothing in that case.

Installs the latest release to `%LOCALAPPDATA%\Programs\agent-manager`, adds it to your user `Path`, and offers to install psmux, git, or PowerShell 7 when one is missing. `AGENT_MANAGER_INSTALL_DEPS=1` answers yes. `AGENT_MANAGER_INSTALL_DEPS=0` skips the prompt. With no terminal it skips the prompt and still leaves the binary installed. `AGENT_MANAGER_VERIFY_ATTESTATION` behaves as it does on the shell script.

Arch Linux, mise, `go install`, prebuilt binaries, Windows (native and WSL2), dependencies, updating, and uninstalling: docs/install.md.

## Usage

```bash
agent-manager
```

Sessions run inside tmux (`am_*` namespace), so they survive the manager quitting. Inside a session, **Ctrl+Q** detaches back to the manager when your terminal and tmux leave it available; **Ctrl+\\** is an alternate under the same rule. **Ctrl+C** reaches the agent as its cancel key while a session is focused, so an interrupted prompt leaves the manager running. **Ctrl+R** opens the session's diff review and **F3** opens its directory in your editor; the **keybindings** row in Settings (`s`) moves any of them, or hands one back to the agent, and moves or turns off any action of the manager's own list, with `esc` and `ctrl+c` staying as they are (see Key bindings). In a full-screen attach, the session footer also shows an inner tmux prefix followed by `d` when configured. When nested inside another tmux, send the inner prefix shown in the footer, then press `d`. If both tmux servers use the same prefix, invoke the outer tmux's `send-prefix` binding; if the outer tmux otherwise captures the inner prefix, configure it to forward that key. `agent-manager --version` prints the version.

Agent sessions live on a private tmux server named `agentmgr`, so they never mix with the tmux you run yourself and a `kill-server` on your own socket leaves them alone. To reach one from a plain shell, name that server: `tmux -L agentmgr ls`, then `tmux -L agentmgr attach -t am_ `.

The full reference, every key, quick prompt mode, killing and reviving, diff review, groups, status detection, stats, and themes, lives in docs/usage.md. Tell your agent what you want to review in Agent Manager, and your agent will set it up for you to view in the review panel. You can also tell your agent to manage sessions and terminals in Agent Manager. The short version:

| Key | Action |
|-----|--------|
| `n` | New session (name, tool, the model, effort and profile the tool reports, environment profile, directory, optional starting prompt, group) |
| `space` | Quick prompt mode: answer the selected session, or spawn an agent in the selected group |
| `enter` | Focus the session in place; keys go to the agent while the list stays |
| click / double click | Focus a session from its row or its preview / fold or unfold a group. The full-screen layout selects on a click and focuses on a double click |
| drag `⠿` / `=` | Reorder a row, drop it into another group, or nest a terminal under an agent |
| `[…]` / right click | The row's actions: attach, prompt, review, fork, rename, move, archive, kill, delete and more |
| click the list / mouse back | Focused: back to the list. A click on another row focuses that one |
| `→` / `←` | Step in and out: `→` focuses the session or opens the group, `←` closes the group and, at the start of a focused agent's prompt, comes back to the list. Settings can turn the pair off |
| `ctrl+r` | Review the session's changes as full-file diffs; `c` comments a line, `C` sends a numbered review round, and sent comments stay visible as open or handled |
| `x` / `v` | Kill a session to free its RAM / revive it on its own conversation |
| `R` | Restart a session on an empty context: same name, group, directory and tool, fresh conversation |
| `s` | Settings (default tool, theme or follow the OS light/dark mode, list density, mouse, review layout, desktop notifications, editor, keybindings) |
| `?` | The key map for the current screen; review shows only review bindings |

A session can spawn into its own git worktree (` -worktrees/ `, branch `am/ `), toggled on the `n` form, with `ctrl+t` in quick prompt mode, or by default in Settings.

A session can start on a model, reasoning effort and profile of its own, picked on the `n` form, with `ctrl+l`, `ctrl+x` and `ctrl+y` in quick prompt mode, or with `spawn --model --effort --profile`. The lists come from each CLI at runtime, so a new model shows up the day the CLI ships it, and restart, revive and fork keep the choice (see Model, effort and profile).

A session can also launch under an environment profile, a named set of environment variables such as a second `CLAUDE_CONFIG_DIR`, defined with `agent-manager env set` and picked per session or as a group's default (see Environment profiles).

the session tree, with a Claude Code session's latest answer in the preview

the session list taking the whole terminal, one-line rows with the computer stats on the foot, then a session focused full screen

the same full-screen list at the comfortable density: every session on three lines, its task and the agent's last message under the name

review, side by side, with the changed lines tinted in full file context

Configuration (Settings, the editor `o` opens, and the key tables) is in docs/configuration.md.

## Development

```bash
go run .
mkdir -p /tmp/amtest && env -u TMUX TMUX_TMPDIR=/tmp/amtest SHELL=/bin/sh go test -race ./...   # end-to-end tests drive a real tmux server
```

See CONTRIBUTING.md for the checks CI runs, and AGENTS.md if you point a coding agent at this repo.

## Community

Join the Agent Manager Community on Discord. Ask questions and get setup help in #help, share your setup in #workflows, and talk about contributing in #dev. Bugs and feature requests go in GitHub issues.

## Contributing

**Contributors and collaborators wanted.** agent-manager is actively looking for people to help build it. Unassigned issues are free to take, comment on one to claim it, and regular contributors get invited as collaborators. Say hi in #dev on Discord.

Bug reports, feature ideas, and pull requests are welcome. See CONTRIBUTING.md for setup and the checks CI runs. Project roles and how decisions are made are in GOVERNANCE.md, with the current roster in MAINTAINERS.md. Questions and setups worth sharing go in Discussions. Security reports go through a private advisory; see SECURITY.md.

### Contributors

## Sponsors

 @dempc6469

## License

Apache-2.0

---

# fluado/enmetu: Keeps one git working tree committed and in sync with its upstream. Node or Bun, plain git, no stash. - CodeFloe - the Forgejo developer platform

## 关联链接

- https://agent-manager.dev
- https://github.com/YoanWai/scoop-bucket
- https://github.com/wainmann/agent-manager/releases/latest/download/install.ps1
- https://github.com/wainmann/agent-manager/releases/latest/download/install.sh
- https://raw.githubusercontent.com/wainmann/agent-manager/main/install.ps1
- https://raw.githubusercontent.com/wainmann/agent-manager/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_778ee41f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
