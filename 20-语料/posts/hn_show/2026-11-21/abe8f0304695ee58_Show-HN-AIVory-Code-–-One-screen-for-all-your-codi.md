---
type: "corpus"
item_id: "abe8f0304695ee58"
title: "Show HN: AIVory Code – One screen for all your coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50578507"
project_url: "https://github.com/aivorynet/aivory-code"
author: "ppiper"
published_at: "2026-11-20T17:28:34Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_ppiper
  - story_50578507
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: AIVory Code – One screen for all your coding agents

> [!info] 一句话导读
> aivorynet/aivory-code

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50578507>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ppiper　|　发布：2026-11-20T17:28:34Z
> 项目链接：<https://github.com/aivorynet/aivory-code>
> 采集：2026-11-21T14:45:01+08:00　|　id：`abe8f0304695ee58`

## 正文

# aivorynet/aivory-code

Local-first control room for Claude Code, Codex CLI and Gemini CLI sessions. Free and MIT.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 2
- License: MIT License
- Homepage: https://aivory.net/coffee
- Default branch: main
- Created: 2026-11-07T09:47:33Z

## Languages

- JavaScript
- PowerShell
- Python
- Ruby
- Rust
- Shell
- Tree-sitter Query

## Top Contributors

- madppiper (19 contributions)

---

## README

# AIVory Code

 One screen for all your coding agents.
 Claude Code, Codex CLI and Gemini CLI side by side: who works, who waits for you, who is stuck.

 Install ·
 Write your own look ·
 Roadmap ·
 Issues ·
 Buy Paul a coffee

AIVory Code is a local-first control room for coding agents. It shows the sessions of Claude Code,
Codex CLI, and Gemini CLI on one screen. You see which agent works, which agent waits for an
answer, and which agent has an error. You answer from the desktop app or from your phone.

A Rust daemon (`aivoryd`) reads the native session stores and runs the agent CLIs that you
already have. The desktop app and the phone app are clients of this daemon.

Status: first public version. See docs/roadmap.md.
Windows 11 is the supported platform. The macOS and Linux builds are a preview: they build in CI,
but nobody has tested them yet.

## Install

**Windows** (Microsoft Store, recommended): AIVory Code in the Microsoft Store.
Microsoft signs the Store build, and the Store installs the updates. From a terminal:

```powershell
winget install 9NG19Z8T9XR6 --source msstore
```

**Windows** (winget, the installer from the releases page):

```powershell
winget install Aivory.AivoryCode
```

**macOS and Linux** (Homebrew):

```sh
brew install aivorynet/tap/aivory-code
```

**macOS and Linux** (script, no package manager):

```sh
curl -fsSL https://github.com/aivorynet/aivory-code/releases/latest/download/install.sh | sh
```

**Linux packages:** the `.deb` and the `.AppImage` on the
releases page.

All of them install `aivory` (the desktop app) and `aivoryd` (the daemon). Start the app with `aivory`.

The builds outside the Microsoft Store have no code signature yet. The package managers avoid the warnings: winget installs
without the SmartScreen prompt, and Homebrew formulas do not get the macOS quarantine flag.
If you download the installer or the archive from the
releases page yourself, Windows SmartScreen
shows a warning at the first start ("More info" > "Run anyway"). On macOS, right-click the app
and select "Open".

## Buy me a coffee

AIVory Code is free and open source (MIT). If it saves you time, you can buy me a coffee:

 Buy Paul a coffee

The link opens the coffee page, and its button opens a Stripe payment page. The coffee is a
thank-you: it buys no license, no support contract, and no extra features. A
 star on GitHub helps too.

 Everybody is welcome: report a bug, ask for a feature, open a pull request, or write your own look.

## Join in

This project grows with the people who use it. You don't need permission to help:

- **Found a bug?** Open an issue. A screenshot and the steps to repeat it are perfect.
- **Missing something?** Ask for a feature. Tell us what you want to do, not only how.
- **Want to code?** Pick an issue, or bring your own idea, and open a pull request. Small PRs are welcome. See CONTRIBUTING.md.
- **Like it?** Buy me a coffee, give a star, or write a short review. It helps a lot.

### Write your own look

The app has looks (themes) that change the whole screen: Minimal, Bridge, Operator, Neon,
Navigator, Holo, Tactical and Command (a pixel-art building game where your agents construct your
features). Make your own and share it:

- A theme is a GitHub repo with plain data files: colors, fonts, and screen layouts. No code runs.
 Start with `aivoryd theme init my-theme`, and check it with `aivoryd theme check my-theme`.
- Install one in Settings > Display: paste the GitHub link, confirm, select. Or run
 `aivoryd theme add github: / `.
- The format is in ADR 0024. Your feedback is welcome.
- Use original art, or art with a free license, and put the license file next to it.
- Add it to the theme registry with a pull request.

## Parts

| Folder | What | Language |
|---|---|---|
| `crates/aivory-protocol` | The contract between daemon and clients: data types, JSON-RPC methods, layout helpers, demo data | Rust |
| `crates/aivory-sessions` | Read-only index of the native session stores; transcripts, session state, spans | Rust |
| `crates/aivory-agents` | Detects the agent CLIs and runs them; maps their output to events | Rust |
| `crates/aivory-map` | Reads and writes the part map of a codebase (the file `.aivory/map.toml` in that codebase) | Rust |
| `crates/aivory-engine` | SQLite store, activity sampler, usage estimate, autopilot planner | Rust |
| `crates/aivory-syntax` | Syntax layer: tree-sitter parse, highlight, stubs, outline, syntax errors (19 languages) | Rust |
| `crates/aivory-index` | Symbol index per repo: stub store, segments, session deltas, definition and references | Rust |
| `crates/aivory-diag` | Diagnostics: rule packs, linters, LSP pool, SARIF per turn | Rust |
| `crates/aivory-vcs` | `Vcs` trait and Git backend, turn snapshots, turn ledger, blame by prompt | Rust |
| `crates/aivory-coord` | Local coordination: claims, conflict radar, mailbox | Rust |
| `crates/aivory-link` | Remote link to the phone: iroh endpoint, device keys, sealed push payloads | Rust |
| `crates/aivoryd` | The daemon and its command line | Rust |
| `apps/desktop` | The desktop app (GPUI), binary `aivory` | Rust |
| `proto/` | JSON fixtures and the JSON Schema of the protocol | JSON |
| `docs/` | Design, decision records (ADR), roadmap | Markdown |

These folders hold only a README. They are placeholders for later work: `grammars/`,
`packs/`, `templates/`, `plugins/genie/`.

## Build and run

Install Rust 1.88 or newer. The first desktop build takes
several minutes.

Run the desktop app on the demo data. No agent and no daemon are needed:

```
cargo run -p aivory-desktop -- --demo
```

Run the desktop app on the real sessions of this machine. Use two terminals:

```
cargo run -p aivoryd -- serve
cargo run -p aivory-desktop
```

Add `--scope ` to `serve` to show only the sessions below one folder.

Run the stress check (40 live panes, frame rate in the log):

```
cargo run --release -p aivory-desktop -- --demo --stress 40 --fps
```

Use the daemon command line without the apps:

```
cargo run -p aivoryd -- --help
cargo run -p aivoryd -- list
cargo run -p aivoryd -- map init <repo>
```

## Test

```
cargo test
cargo test --workspace
```

- `cargo test` tests the crates. It leaves out the desktop app.
- `cargo test --workspace` adds the desktop app. The build is slow.

Run these checks before you finish a change:

```
cargo fmt --all -- --check
cargo clippy --workspace --all-targets -- -D warnings
```

`cargo deny check` checks the dependency licenses. It needs `cargo install cargo-deny`.

## Privacy rules

- The native stores (`~/.claude`, `~/.codex`, `~/.gemini`) are read-only. The code never
 writes to them.
- The daemon runs `claude`, `codex`, and `gemini` with the login of the user.
- No code reads, stores, or proxies a login token.
- The daemon keeps its own data (tasks, settings, devices) in a per-user folder.
 On Windows this is `%LOCALAPPDATA%\aivory\code`.
- Tests use synthetic fixtures. No test reads a real session.
- The phone link works in the local network only. It has no TLS yet
 (ADR 0021).

## Documents

- AGENTS.md: rules for coding agents and contributors.
- docs/design/screens/README.md: the accepted design.
- docs/design/00-vision.md: vision, principles, and glossary.
- docs/adr/: decision records.
- docs/roadmap.md: steps and status.

## License

MIT. Everyone can use, change, and share AIVory Code for free, also at work. See LICENSE.
The phone and watch apps have their own license and are not part of this repository.
There is no paid tier (ADR 0025).
The bundled fonts use the SIL Open Font License. The license files are in
`apps/desktop/assets/fonts`.

# alexadam/printer-friendly

## 关联链接

- https://aivory.net/coffee
- https://github.com/aivorynet/aivory-code/releases/latest/download/install.sh

## 导航

- 项目页：[[10-项目/github.com_487bc570]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
