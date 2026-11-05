---
type: "corpus"
item_id: "8c6f8541bc6ba8d1"
title: "Show HN: Safe and lightweight VMs for Coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50369671"
project_url: "https://github.com/skerrysoft/safeagent"
author: "msjpr"
published_at: "2026-11-04T18:34:50Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_msjpr
  - story_50369671
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Safe and lightweight VMs for Coding agents

> [!info] 一句话导读
> skerrysoft/safeagent

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50369671>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：msjpr　|　发布：2026-11-04T18:34:50Z
> 项目链接：<https://github.com/skerrysoft/safeagent>
> 采集：2026-11-05T11:21:45+08:00　|　id：`8c6f8541bc6ba8d1`

## 正文

# skerrysoft/safeagent

Run agents in lightweight and safe VMs

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-03T02:27:03Z

## Languages

- Go
- Makefile
- Shell

## Top Contributors

- skerrysoft (33 contributions)

---

## README

# safeagent

**A lightweight Linux VM for every checkout, so parallel coding sessions
can't collide, and the code they run can't reach your machine.**

Coding agents like Claude Code work best in parallel: several sessions, each
in its own git worktree, each on its own task. Worktrees separate the files,
but everything else is shared. Two sessions both want port 3000, one
branch's migration breaks the other's database, and every command an agent
runs has your whole machine within reach.

safeagent gives each worktree its own small Linux VM, with its own processes,
ports, Postgres, Valkey (Redis) and Temporal, and its own copy of their data.
It reads what it needs from the repository (lockfiles, compose files,
monorepo packages, the local addresses its env files name), so most
projects need no configuration. It plugs
into Claude Code, so every worktree session gets one automatically and the
VM is ready in the background while the session gets on with the work; with
any other tool, `safeagent create` makes a workspace by hand.

Two live Claude Code sessions side by side, each in its own safeagent workspace. As they start, the status line shows safeagent preparing each workspace in the background (building the VM image) while Claude reads and edits code. One adds a --quantity option and places an order for two espresso machines; the other merges a branch that brings a new migration and places an order for a teapot with the gift note "Happy birthday!". Each workspace has its own Postgres and Temporal, so both orders are order #1.

*Two real Claude Code sessions, recorded live with
asciinema (idle time trimmed to 2 s; nothing else
edited). As each session opens, safeagent prepares its workspace in the
background (the VM, Postgres, Temporal, `npm install`, migrations), shown
in the status line, while Claude gets on with the code. Each has its own
database: both place order #1, and only the second, which merged a branch
with a new migration, has a `gift_note` column.*

> **Status: early development.** macOS on Apple Silicon today; Linux hosts
> are being built. See What works today.

---

## Get started with Claude Code

**1. Install safeagent** on a Mac with Apple Silicon:

```bash
curl -fsSLO https://github.com/skerrysoft/safeagent/releases/latest/download/safeagent-darwin-arm64.tar.gz
mkdir -p ~/.local/bin && tar -xzf safeagent-darwin-arm64.tar.gz -C ~/.local/bin   # or anywhere on your PATH
```

Each release is built by GitHub Actions
from this repository, with checksums (`SHA256SUMS`) and a signed build
provenance attestation. To check a download was built here, before
installing it:

```bash
gh attestation verify safeagent-darwin-arm64.tar.gz --repo skerrysoft/safeagent
```

Downloaded it with a browser instead? macOS then won't run it ("cannot be
opened"), as it isn't notarized yet; clear the download flag with
`xattr -d com.apple.quarantine ~/.local/bin/safeagent`.

 Or build it from source (Go 1.27+)

```bash
git clone https://github.com/skerrysoft/safeagent && cd safeagent
make build                      # bin/safeagent, signed to run VMs
cp bin/safeagent ~/.local/bin/     # or anywhere on your PATH
```

**2. Connect it to Claude Code.**

```bash
safeagent claude install
```

This shows the three hooks it will add to `~/.claude/settings.json`
(`WorktreeCreate`, `WorktreeRemove`, `SessionStart`), keeps a backup, and
asks which folders to turn safeagent on for. safeagent only ever acts in those
folders; everywhere else, worktrees stay plain worktrees.

 Or use the Claude Code plugin instead

The plugin carries the same three hooks (and a small script that finds the
`safeagent` command), and nothing else. In any Claude Code session, from any
folder:

```text
/plugin marketplace add skerrysoft/safeagent
/plugin install safeagent@safeagent
```

The first command adds this GitHub repository as a plugin marketplace; the
second installs the plugin for your user, in every project. safeagent itself
must still be installed (step 1), and it still only acts in the folders you
enable (`safeagent enable DIR`). Use the plugin or `safeagent claude install`, not
both: two `WorktreeCreate` hooks would both try to make the worktree.

**3. Start sessions in worktrees, as you already do.**

```bash
claude --worktree fix-login
```

or turn on **Worktree** when starting a session in the Claude desktop app.
Subagents and background sessions that use worktrees work the same way.

That's all. Optionally, show each workspace in Claude Code's status line, so
you can see it being prepared (add to `~/.claude/settings.json`):

```json
"statusLine": { "type": "command", "command": "safeagent statusline" }
```

**Without Claude Code** (or with another agent), make a workspace yourself
and work in it:

```bash
safeagent enable ~/code              # once: safeagent acts only in folders you enable
cd ~/code/shop
safeagent plan                       # what safeagent found, before anything runs
cd "$(safeagent create fix-login)"   # a worktree that gets its own VM
safeagent exec -- npm test           # the first command boots and prepares it, then runs
safeagent start                      # run the project's apps, forwarded to your machine
safeagent status                     # services, apps, and where each is on your machine
```

## What happens in a session

1. **Claude creates the worktree through safeagent.** In an enabled folder it
 becomes a *workspace*; elsewhere, a plain worktree, made the way Claude
 would make it.
2. **The session opens right away**, and safeagent prepares the workspace in
 the background: builds or reuses the VM image, boots the VM (about half a
 second), starts the services (Postgres, Valkey, Temporal), creates the
 databases, installs dependencies, builds, and runs the setup you
 configured. The first time for a project this takes a minute or two;
 after that, seconds. So the database is there when you run migrations
 or tests.
3. **Nothing waits on that but the commands that need the VM.** Claude can
 read and edit code and use git meanwhile. A command that needs the VM
 (`npm test`, say) waits for it, printing each step, and the status line
 shows where preparation has got to.
4. **Commands go to the right place automatically.** `node`, `npm`, `npx`,
 `yarn`, `pnpm` and `corepack` run in the VM, as do the commands of any
 other runtime the project lists (`python`, `go`, …). Everything else,
 git included, runs on your machine with your keys and settings. Claude is
 told how the workspace works when the session starts.
5. **Your apps start when you start them, not before.** Preparing a
 workspace never runs the project's own apps (its API, web app,
 workers). When your change is ready to try, run `safeagent start` (all of
 them) or `safeagent start web` (one, with the library watchers it needs),
 or ask Claude to. They run in the VM, restart if they crash, and are
 forwarded to your machine; `safeagent stop` stops them, and so does the
 VM stopping (`safeagent down`, or 30 minutes unused). Running your own
 dev command (`npm run dev`) works too: it runs in the VM like any
 other.
6. **Removing the worktree removes the workspace**: its VM and its data.
 Uncommitted work and branches with commits are never deleted.

## How it works

- **One VM per workspace**, on Apple's Virtualization framework: a small
 Linux kernel (Alpine's) and a userland built from signature-verified
 Wolfi packages, shared read-only by every workspace
 that needs the same runtimes and services. It boots in about half a
 second.
- **Your checkout, live.** The worktree is shared into the VM at the same
 path (virtio-fs), so your editor, git and the VM all see the same files.
 Dependencies install into it as Linux builds.
- **Its own disks.** Service data (Postgres, Valkey) and caches (the home
 directory, `/tmp`) live on sparse disk images of the workspace's own;
 the rest of the system is in memory.
- **A guest agent**, the VM's first process, runs the services and apps
 and takes commands from safeagent over SSH on vsock, with keys pinned per
 workspace.
- **A user-mode network.** The VM's network card connects to a network
 stack inside safeagent (gVisor's), which lets it reach
 the internet and nothing local. Ports are forwarded to your machine's
 `127.0.0.1`.
- **Sized to the project**: 4 CPUs and 3 GB by default, more memory for
 each service and app, within half your machine.

## Configure a project

Most projects need no configuration. safeagent reads the files a project
already has:

| Service | Started when the project has… | Commands in the VM get |
|---|---|---|
| `postgres`: PostgreSQL 17 with pgvector and the contrib extensions | `pg`, `postgres`, `pg-promise` (npm); `pgx`, `lib/pq` (Go); `psycopg`, `asyncpg` (Python); `pg` (Ruby); a `postgres`/`pgvector` image in a compose file | `DATABASE_URL`, `PG*`; database `app`, with `vector` installed |
| `valkey`: Valkey 8 (Redis-compatible) | `redis`, `ioredis`, `bullmq`, `iovalkey` (npm); `go-redis`, `valkey-go`; `redis` (Python, Ruby); a `redis`/`valkey` image | `REDIS_URL`, `VALKEY_URL` |
| `temporal`: Temporal dev server | `@temporalio/client` or `/worker`; `go.temporal.io/sdk`; `temporalio` (Python); a `temporalio/*` image | `TEMPORAL_ADDRESS` |

It also installs dependencies from the lockfile (`npm ci`,
`pnpm install --frozen-lockfile`, `uv sync --frozen`, …), reads every
package of a monorepo, gives each new workspace copies of your checkout's
local `.env` files (so apps run as they do in your checkout), creates the
local databases they point to, and builds what the apps import. safeagent
itself reads env files only for local addresses, ports and variable
names: every other value, and any password in a URL, is dropped as the
file is read, and nothing from them is stored, printed or sent anywhere.
It also finds the project's apps (packages with a `dev` script and a
port, Procfile processes, Django's and Rails' dev servers), which
`safeagent start` runs, with their ports forwarded to your machine; they
never start on their own. `safeagent plan` shows all of it before anything runs,
including how each app is wired: what in the VM answers at every local
address its env files name, and what nothing does. To say exactly what a
workspace needs, add a `safeagent.yaml` at the repository root:

```yaml
services: [postgres, temporal]
runtimes: [python@3.12]        # Node is always there
packages: [ffmpeg]             # extra packages, by name
setup:                         # in the VM, in order, when the data is new
  - npm ci
  - npm run migrate
apps: [api, web]               # what `safeagent start` runs
ports: [3000]                  # forward another port to your machine
```

Setup runs once for a workspace's data, and again when its inputs change
(dependencies, migrations, `safeagent.yaml`). **The `safeagent.yaml`
reference** explains every key and exactly what runs
when, in which order.

The services' variables are set for every command in the VM, so they win
over the same names in a `.env` file (dotenv loaders don't override
variables that are already set). `safeagent status` shows the services and the
ports they are forwarded to on your machine; `safeagent url postgres` prints a
URL, password included, for tools such as `psql` or a database GUI.

## Working with git

The checkout is never copied into the VM. Your worktree stays an ordinary
folder on your machine; the VM sees the same folder, live, at the same
path, through a shared file system. Git runs on your machine, not in the
VM, so it works as it always does:

- **Rebase, merge, pull, switch branches** in the worktree as usual
 (`git pull --rebase origin dev`, `git merge dev`). The VM sees the new
 files the moment git writes them.
- **New dependencies or migrations arrive with a merge?** The next command
 that runs in the VM notices (safeagent watches lockfiles, migration folders
 and `safeagent.yaml`) and runs setup again first, so the workspace installs
 them and migrates its own database.
- **A rebase rewrote migrations the database already ran?** Start the
 data over: `safeagent reset` (back to the snapshot, if the repository has
 one, else empty), and setup migrates it from scratch.
- **Your editor, git GUI and Claude's file tools** all work on the same
 files on your machine; paths in errors and stack traces match.

Code in the VM can't redirect your git: the worktree's `.git` pointer is
locked, and repositories or Claude Code settings planted in the checkout
are quarantined (see Security).

## Data: seeds and snapshots

A workspace can start with real data, migrated for its own branch. A dump in
the repository loads in `safeagent.yaml` (`seed: {postgres: db/seed.sql.gz}`);
a dump that isn't (an anonymized copy of production, say) loads from your
machine:

```bash
safeagent reset --empty && safeagent seed ~/dumps/prod.dump   # in one workspace
safeagent snapshot save                                    # make it the default
```

Every new workspace of the repository then starts from that snapshot (on
macOS, an APFS clone: instant, and taking no space until it changes) and
runs its own branch's setup on top. `safeagent reset` goes back to the
snapshot; `safeagent snapshot ls` and `safeagent snapshot rm NAME` manage them.

Snapshots and `safeagent reset` cover service data only. What commands keep
in the VM's home directory and `/tmp` (package caches, downloaded
browsers, build output) lives on a second disk of the workspace's own, so
it doesn't take the VM's memory; the home directory keeps it across
restarts, and `/tmp` starts empty. It is never in a snapshot,
`safeagent reset` leaves it, and removing the workspace deletes it.

## Security

Workspaces run untrusted code: dependencies' install scripts, repository
scripts, and whatever an agent decides to run. safeagent is built to contain
it. Found a way out? Please report it privately, as
SECURITY.md describes.

**What protects you**

- **VM boundary.** Each workspace is a Linux VM (on macOS, Apple's
 Virtualization framework, which runs each VM in its own sandboxed
 process). It sees only its checkout, the read-only system image and its
 own configuration, never your machine's other files.
- **A network that only goes out.** A VM's network card connects to a
 user-mode network stack inside safeagent, not to a bridge or your machine's
 network. Every connection is checked after DNS resolution: public
 addresses are allowed; loopback, private and link-local ranges (cloud
 metadata included), carrier-grade NAT, multicast, your machine's own
 addresses and every network it is directly attached to (VPNs included)
 are refused, as is outgoing mail (port 25). A VM can hold at most 512 TCP
 and 128 UDP flows, so it can't exhaust your machine's ports. DNS goes
 through your machine's resolver. Refused connections are logged
 (`safeagent logs network`).
- **Services reachable only from your machine.** Forwarded ports listen on
 `127.0.0.1` only, at ports safeagent picks (never ones the checkout names,
 which could take over ports your own servers use). From your machine,
 Postgres and Valkey each require their own password, which other local
 users can't read; services without a password aren't forwarded unless
 you ask. The apps' web ports answer only to `localhost` names, so a web
 page can't reach them by DNS rebinding.
- **Trust inside the VM only.** Inside the VM, where everything runs as
 root anyway, Postgres trusts the user a command names, so a project's
 `.env` URLs work unchanged (on other ports too, which relay to the
 service inside the VM). Connections forwarded from your machine never
 get that trust.
- **Clean output.** What safeagent prints from the VM (logs, errors) is
 stripped of terminal control sequences.
- **Locked git metadata.** The worktree's `.git` pointer is made immutable,
 and safeagent's own git commands name the repository explicitly, so a VM
 can't redirect them. After every command, at session start and every
 15 seconds while a VM runs, safeagent scans the checkout for planted
 repositories and Claude Code settings and quarantines them.
- **Opt-in.** Nothing happens outside folders you enable. Creating a
 worktree never runs the repository's filter drivers, or its hooks unless
 you opt in.
- **Pinned keys.** Host and VM authenticate each other with per-workspace
 SSH keys that safeagent generates. Nothing is trusted on first use.
- **Verified images.** Every package is checked against a signed index
 (Wolfi's and Alpine's pinned keys) down to each file, extraction can't
 write outside the image directory, and install scripts run in a build VM.
- **Careful deletion and bounded logs.** safeagent only deletes worktrees it
 created, never a branch that holds commits, and caps the logs a VM can
 write on your disk.

Each of these is tested by attacking a real VM from the inside
(scripts/escape-test.sh), and the parsers that read
VM or repository input are fuzzed.

**Known gaps**

- The checkout is shared read-write: that is how your edits reach the VM and
 its output reaches you. Code in the VM can change your source files, and
 files git tracks under `.claude/`. Review changes as you would any
 dependency's.
- Something running in the background in a VM could plant a file between
 scans (up to 15 seconds).
- No disk quota yet: a VM can fill the disk through its checkout, and its
 service data disk and its home disk (caches) can each grow to 64 GB.
 Space the VM frees is handed back to your machine.
- The Temporal dev server and its UI have no authentication. If you forward
 them, any process of any user on your machine can reach them.
- A web page served from a VM and opened in your browser is a local page: it
 can send requests to other services on your machine's loopback interface,
 as any local web app can. Open workspace apps through their `*.localhost`
 URLs.
- A snapshot's data reaches every new workspace of its repository, whatever
 branch it is on, and code in those VMs can reach the internet. Don't save
 data in a snapshot that you wouldn't give to every branch you check out
 (an outside contributor's included).
- Setup commands from `safeagent.yaml`, dependency installs and builds run
 in the VM without asking, as `npm install` would; the project's apps run
 when you (or Claude) run `safeagent start`.
- Your local `.env` files (secrets included) are copied into each new
 workspace, as Claude Code's `.worktreeinclude` copies what it lists, so
 code in the VM can read them, and the VM can reach the internet. Add a
 `.worktreeinclude` to choose exactly which files a workspace gets.
- A VM can reach anything public, from your machine's public address: code
 in it can send what it can read (the checkout) to the internet, and reach
 services that trust your IP address or a public range routed over your
 VPN. An allowlist mode is planned.
- No external security review yet.

The full threat model, and the rules every change is tested against, are in
docs/design.md.

## Commands

You rarely need these with Claude Code; these are the ones for working by
hand:

| Command | What it does |
|---|---|
| `safeagent plan [--env] [DIR]` | Show what safeagent would set up for a checkout, and how its apps are wired, without starting anything |
| `safeagent create NAME [--base BRANCH]` | Make a workspace (worktree on branch `worktree-NAME`) and print its path |
| `safeagent start [APP…]` / `stop [APP…]` | Run or stop the project's apps in the VM (all, or the ones named); they never start on their own |
| `safeagent status [NAME]` | Preparation, services, setup, whether each app answers, and where everything is on your machine |
| `safeagent exec -- CMD…` | Run a command in the workspace's VM |
| `safeagent logs [-f] WHAT` | A service's or an app's output, or `setup`, `console`, `network` |
| `safeagent rm NAME [--force]` | Remove a workspace; `--force` discards uncommitted changes but never a branch with commits |

Commands that act on a workspace use the one you're in, unless you name one.

 All commands and settings

| Command | What it does |
|---|---|
| `safeagent claude install` / `uninstall` | Add or remove the Claude Code hooks |
| `safeagent enable [DIR]` / `disable [DIR]`, `enable --list` | Turn safeagent on or off for a folder and everything under it |
| `safeagent ls` | List workspaces |
| `safeagent up [NAME]` / `down [NAME]` | Start (and prepare) or stop a workspace's VM |
| `safeagent url [-w NAME] SERVICE` | Print a URL for a service, password included, for tools on your machine |
| `safeagent setup [NAME]` | Run the project's seed and setup again |
| `safeagent seed [-w NAME] FILE` | Load a `.sql`, `.sql.gz` or `.dump` file into the workspace's empty Postgres |
| `safeagent snapshot save [S]` / `ls` / `rm S` | Save the workspace's data for new workspaces (`default`); list or delete snapshots |
| `safeagent reset [NAME] [--snapshot S \| --empty]` | Start the workspace's data over |
| `safeagent gc` | Delete images and downloads no workspace needs |
| `safeagent statusline` | One line for Claude Code's status line |

Settings, through environment variables for now:

| Variable | Effect |
|---|---|
| `SAFEAGENT_IDLE_STOP` | Stop a workspace's VM after it has been unused (no commands, no connections to its ports) this long (default `30m`; `off` never), apps included. Its data stays; the next command starts it again, and `safeagent start` the apps |
| `SAFEAGENT_CPUS`, `SAFEAGENT_MEMORY` | CPUs and memory per VM (default 4 and `3g`, more memory for each service and app; at most all CPUs and half the machine's memory) |
| `SAFEAGENT_BASE=head` | Start new worktrees at your current commit instead of the remote's default branch |
| `SAFEAGENT_GIT_HOOKS=1` | Let the repository's git hooks run when creating worktrees (off by default) |
| `SAFEAGENT_BRANCH_PREFIX` | Prefix for new branches (default `worktree-`) |
| `SAFEAGENT_FILE_EVENTS=off` | Don't forward file changes to watchers in the VM (by default, watchers in a VM see edits made on your machine) |
| `SAFEAGENT_SHIMS=off` | Run your machine's own `node`, `python`… even in workspaces |
| `SAFEAGENT_HOME` | Keep all of safeagent's state and caches under one directory |

## What works today

| | |
|---|---|
| ✅ Claude Code hooks: CLI, desktop app, subagents, background sessions; plugin | verified |
| ✅ One VM per workspace on macOS (Apple Silicon) | ~0.5 s boot |
| ✅ Preparation in the background, with progress in the status line and `safeagent status` | |
| ✅ Networking: internet yes; your machine, local network and cloud metadata no | |
| ✅ Services: Postgres 17 + pgvector, Valkey, Temporal; data kept per workspace | |
| ✅ Runtimes: Node, Python, Go, Ruby, Java, Bun, Deno; extra packages by name | |
| ✅ Dependencies installed from the lockfile; setup re-run when a merge changes them | |
| ✅ Monorepos: services, apps and library watchers detected across packages; `safeagent start` runs apps with forwarded ports | |
| ✅ Procfiles, Django and Rails dev servers; Python, Ruby and Go runtimes detected | |
| ✅ Local `.env` files copied into workspaces; the databases they name created; their secrets never read | |
| ✅ Seeds, setup commands (migrations), snapshots cloned per workspace | |
| ✅ Hot reload; idle stop; CPU and memory limits | |
| ✅ Images built only from signature-verified packages | |
| 🚧 Linux hosts | in progress |

## Building from source

- macOS on Apple Silicon (built and tested on macOS 27); Go 1.27+ and git
- Network access the first time an image is built: packages come from Wolfi
 (packages.wolfi.dev) and the kernel from Alpine. About 100 MB, more with
 services and runtimes.

`make build` builds the guest agent for Linux, embeds it in `bin/safeagent`, and
signs `bin/safeagent` with the `com.apple.security.virtualization` entitlement
so it can start VMs. A plain `go build` produces a binary without the agent
or the signature.

## Feedback

safeagent is early. If it gets something wrong on your project (a service it
missed, an app it didn't find, setup that failed), `safeagent plan` output in
an issue helps most.
Security problems go to SECURITY.md instead.

## License

MIT. See LICENSE.

## 关联链接

- https://github.com/skerrysoft/safeagent/releases/latest/download/safeagent-darwin-arm64.tar.gz

## 导航

- 项目页：[[10-项目/github.com_bf7d4fb1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
