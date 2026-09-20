---
type: "corpus"
item_id: "de4a02adca313337"
title: "Show HN: Harness – Manage parallel Claude Code agents across Git worktrees"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47948379"
project_url: "https://github.com/frenchie4111/harness"
author: "frenchie4111"
published_at: "2026-04-29T13:42:44Z"
captured_at: "2026-09-21T02:52:37+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_frenchie4111
  - story_47948379
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Harness – Manage parallel Claude Code agents across Git worktrees

> [!info] 一句话导读
> frenchie4111/harness

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47948379>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：frenchie4111　|　发布：2026-04-29T13:42:44Z
> 项目链接：<https://github.com/frenchie4111/harness>
> 采集：2026-09-21T02:52:37+08:00　|　id：`de4a02adca313337`

## 正文

# frenchie4111/harness

Run a team of agents

- Stars: 90
- Forks: 13
- Watchers: 90
- Open issues: 22
- License: MIT License
- Default branch: main
- Created: 2026-04-09T21:47:29Z

## Languages

- CSS
- HTML
- JavaScript
- Python
- Shell
- TypeScript

## Top Contributors

- frenchie4111 (463 contributions)
- big-guy (110 contributions)
- tresat (22 contributions)
- blindpirate (4 contributions)
- ljacomet (4 contributions)
- bz-canva (1 contributions)
- ghale (1 contributions)
- pgodschalk (1 contributions)

---

## README

 Run a team of agents.

 Run ten Claudes at once without losing your mind.
 Ship more, faster, with every session at your fingertips.

 Website ·
 Download ·
 Guide ·
 Slack

Harness

 Mobile mode

 Control your agents from your phone. Guaranteed to be better than Claude's shitty remote UI.

 Browser control

 Give agents control of your browser. Useful for testing your code locally, or just ordering groceries.

> **→ Visit harness.mikelyons.org for screenshots, feature walkthroughs, and release notes.**

## Download

Grab the latest release from the releases page.

- **Apple Silicon (M1/M2/M3/M4):** Harness-2.13.2-arm64.dmg
- **Intel Mac:** Harness-2.13.2.dmg

## Installation

### macOS

1. Download the `.dmg` for your Mac architecture from the links above.
2. Open the `.dmg` and drag **Harness** into your Applications folder.
3. Launch Harness from Applications. The app is signed and notarized, so it should open without any Gatekeeper warnings.
4. On first launch:
 - Pick a git repository when prompted.
 - Click the ⚙ gear icon in the sidebar and paste a GitHub personal access token (fine-grained or classic, with `repo` scope). This is optional but required for the PR status panel and checks.
 - When the hooks consent banner appears, click **Enable** so Harness can install status-tracking hooks globally at `~/.claude/settings.json`. One install covers every worktree and is what makes the sidebar status dots reliable. Curious what the hook actually runs? See `src/main/hooks.ts` (the bash command built by `makeHookCommand` — it appends one line of JSON per event to `/tmp/harness-status/.ndjson`) and `src/main/agents/claude.ts` (where the install/uninstall logic lives).

### Linux

Grab `Harness-.deb` or `Harness-.AppImage` from the releases page.

**Ubuntu / Debian (.deb)** — the recommended option:

```sh
sudo apt install ./Harness-<version>.deb
```

The postinstall script handles the `chrome-sandbox` SUID bit automatically, so this works on Ubuntu 24.04+ out of the box.

`.deb` users get an in-app banner when a new version is available, but updates are manual — re-download the new `.deb` from GitHub Releases and `sudo apt install ./Harness-.deb`. (AppImage / macOS users get auto-updates.)

**AppImage** — for distros without `dpkg`:

```sh
chmod +x Harness-<version>.AppImage
./Harness-<version>.AppImage
```

If you hit `The SUID sandbox helper binary was found, but is not configured correctly` on Ubuntu 24.04+, either install the `.deb` instead or relax the AppArmor unprivileged-userns restriction:

```sh
echo "kernel.apparmor_restrict_unprivileged_userns=0" | sudo tee /etc/sysctl.d/60-apparmor-namespace.conf
sudo sysctl --system
```

### Requirements

- macOS (Apple Silicon or Intel) or x64 Linux (Ubuntu/Debian for the `.deb`; any glibc distro for the AppImage)
- `claude` CLI installed and on your login shell's `PATH`
- `git` installed (preinstalled on macOS via Xcode Command Line Tools)

### Network access

Harness makes outbound network calls to two places: `api.github.com` (for PR status, check runs, and review state on worktrees that have an open PR) and this project's own GitHub releases feed (for auto-updates via `electron-updater`). If you have the `gh` CLI installed and authenticated, Harness will optionally pick up your token from it instead of requiring you to paste a PAT.

The optional remote-control WebSocket transport (used by the web client) is off by default, bearer-token-authed, and bound to `127.0.0.1` when enabled; opting in to LAN access (binding to `0.0.0.0`) is a separate explicit config flag.

## Headless server

Run Harness on a remote dev box and connect from a local browser, mobile phone, or the Electron app. The headless server is a single tarball (no host Node, no other deps) that ships an embedded Node, the bundled `claude` binary, the web client, and the MCP bridge.

Install with one command:

```sh
curl -fsSL https://raw.githubusercontent.com/frenchie4111/harness/main/scripts/install-headless.sh | sh
```

This downloads the right tarball for your platform (`darwin-arm64`, `linux-x64`, or `linux-arm64`), verifies its sha256, and extracts to `~/.harness-server/`. Intel Macs are not currently shipped — GitHub's macos-13 runner queue is too unreliable to keep in CI. If `/usr/local/bin/` is writable a `harness-server` symlink is dropped there; otherwise you add `~/.harness-server/bin` to your `PATH`.

Run it:

```sh
harness-server --port 0
```

`--port 0` picks an ephemeral port. The server prints both a `ws://` URL (for renderers) and an `http://` URL (the web client) with the auth token embedded as a query string. Pin the `http://` URL on a phone homescreen or browser bookmark — the token survives restarts. To run as a daemon, wrap with `nohup`, `tmux`, or `screen`.

The tarballs are not Apple-signed. On macOS you may need to `xattr -d com.apple.quarantine ~/.harness-server/bin/harness-server` if Gatekeeper objects.

To pin a specific version:

```sh
HARNESS_SERVER_VERSION=2.6.1 sh -c 'curl -fsSL https://raw.githubusercontent.com/frenchie4111/harness/main/scripts/install-headless.sh | sh'
```

Re-running the install script bumps the version. The server never self-updates. Backends you connected over SSH are the exception: when the remote's version doesn't match your Harness, the backend's chip shows an upgrade badge that re-runs the installer and restarts the server for you — restarting ends every session on that machine, so it's always an explicit click.

### Connecting the Electron app to a remote server

Once `harness-server` is running on a remote machine, you can drive it from your local Electron Harness alongside the local backend. Open the Harness sidebar's backend chip strip (or `File → Add Backend…`), paste the connection link the host's Settings shows (`http://host:port/?token=...`), and click "Test & save". The link's the same one the browser web client uses; Harness parses out the token, validates the connection, and persists the backend.

Once added, the chip appears at the bottom of the sidebar. Click to switch — `Cmd+Shift+1..9` jumps directly to the Nth backend (Local is always 1). Each backend has its own worktrees, terminals, browser tabs, and settings; switching changes which backend's UI is rendered, and inactive backends keep streaming so notifications still work. The connections list is encrypted (tokens in `secrets.enc`) and persists across restarts.

## Uninstallation

1. **Remove the Claude Code hooks** (do this while Harness is still running). Open Settings → **Agent** → **Status hooks** and click **Remove hooks**. This strips Harness's entries from `~/.claude/settings.json` and leaves any user-authored hooks intact.

2. **Quit Harness** with ⌘Q.

3. **Delete the app:**

   ```sh
   rm -rf /Applications/Harness.app
   ```

 (or drag it to the Trash.)

4. **Remove app data** (optional, for a fully clean uninstall):

   ```sh
   rm -rf ~/Library/Application\ Support/Harness
   rm -rf ~/Library/Preferences/org.mikelyons.harness.plist
   rm -rf ~/Library/Saved\ Application\ State/org.mikelyons.harness.savedState
   rm -rf ~/Library/Caches/org.mikelyons.harness
   rm -rf ~/Library/Logs/Harness
   ```

5. **If you skipped step 1** and already deleted the app, you can remove the hooks by hand. Open `~/.claude/settings.json` and delete any hook entries whose object contains `"_marker": "__claude_harness__"` — every Harness-managed hook is tagged with that marker, so they're safe to identify and remove.

6. **Optional — clean up worktrees.** Harness may have created git worktrees under `claude-harness-worktrees/` next to your repos. These are normal git worktrees and aren't removed automatically. To clean them up:

   ```sh
   cd <your-repo>
   git worktree list
   git worktree remove <path>
   ```

 Or delete the `claude-harness-worktrees/` directories from disk and run `git worktree prune` in each repo.

## Features

- **Multi-agent** — run Claude Code or Codex in the same window, one harness for both
- **Multi-repo** — manage multiple repos in a single window, switch between them or see everything at once
- **Live PR status** — see open PRs and CI checks for every worktree, auto-sorted by urgency
- **Embedded editor** — full Monaco-powered editor for tweaking files without leaving Harness
- **Full code review tool** — side-by-side syntax-highlighted diffs for every changed file in a worktree
- **Status at a glance** — sidebar dots show which agent is working, waiting, or needs approval (powered by Claude Code hooks)
- **Command center** — bird's-eye grid of every worktree with mini activity timelines
- **Tabs + vertical split panes** — Claude, shells, and editor/diff tabs scoped to each checkout, splittable side-by-side
- **Existing-branch worktrees** — fork a new branch, pick a local branch from a typeahead, or check out any git ref (commit SHA, tag, or remote-tracking ref)
- **9 themes** — dark, dracula, nord, gruvbox, tokyo night, catppuccin, one dark, solarized dark/light
- **Configurable hotkeys** — ⌘1–⌘9 to jump between worktrees, all rebindable
- **MCP: Claude controls Harness** — a built-in MCP server lets Claude create and list worktrees on its own

## Why did I build this

Honestly I have been using Conductor for a while as a fairly happy customer, but some rough edges have really started to annoy me so on a random Thursday morning I decided to build my own version of it that works the way I want to. Oh yeah did I mention:

> Originally vibe coded start to finish — these days I occasionally crack open the actual source. Future travelers: still mostly vibes.

# How's it work?

This app is specifically designed to be an easy way to do the sort of ADD fueled multi-worktree development that I have been in-to these days. Along the left you can see all the worktrees you have, and each worktree has it's own claude, additional terminals and PR display.

The main benefit of this is that your worktrees stay organized, and it's very obvious when one of your many claudes needs your attention (the dot will change colors)

## Worktrees

This app assumes that you are going to want to use worktrees (otherwise what's the point)

It will create a worktree directory at `../ -worktree` and start making worktrees there. This directory will probably be changable at some point

# Roadmap

The high-level roadmap has been moved here: https://github.com/frenchie4111/harness/issues/31

# Setup, building, and running locally

Clone the repo and install dependencies:

```sh
git clone https://github.com/frenchie4111/harness.git
cd harness
npm install --legacy-peer-deps
```

> The `--legacy-peer-deps` flag is required because `electron-vite@5` declares a peer range that npm's strict resolver rejects against the installed `vite@7`.

Common commands:

| Command | What it does |
|---|---|
| `npm run dev` | Launch the app in dev mode with hot reload |
| `npm run build` | Type-check and build main, preload, and renderer to `out/` |
| `npm run pack` | Build an unsigned `.app` for local smoke testing (fast — skips codesigning and notarization) |
| `npm run dist:mac` | Full signed + notarized macOS build (requires `.env` with Apple creds) |
| `npm run rebuild:dev` | Rebuild `node-pty` against the dev Electron version — run this if dev mode errors with `posix_spawnp failed` |
| `npm run log` | Tail the debug log at `~/Library/Application Support/harness/debug.log` |

After `npm run pack`, you can launch the unsigned build with:

```sh
open release/mac-arm64/Harness.app
```

If Gatekeeper blocks the unsigned app, strip the quarantine attribute first:

```sh
xattr -cr release/mac-arm64/Harness.app
```

# Contributing

We absolutely love contributors. See CONTRIBUTING.md for setup, PR conventions, and pointers into the architecture docs.

# jossephus/chuchu

## 关联链接

- http://`
- http://host:port/?token=...`
- https://github.com/frenchie4111/harness.git
- https://github.com/frenchie4111/harness/issues/31
- https://raw.githubusercontent.com/frenchie4111/harness/main/scripts/install-headless.sh

## 导航

- 项目页：[[10-项目/github.com_133914c3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
