---
type: "corpus"
item_id: "75fece20fdde6103"
title: "Show HN: Open-source AI workspace with shared procedural memory"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50282336"
project_url: "https://github.com/TheWariend/CleanSlate"
author: "devthewariend"
published_at: "2026-10-28T23:18:59Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - hn_show
  - author_devthewariend
  - story_50282336
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Open-source AI workspace with shared procedural memory

> [!info] 一句话导读
> TheWariend/CleanSlate

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50282336>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：devthewariend　|　发布：2026-10-28T23:18:59Z
> 项目链接：<https://github.com/TheWariend/CleanSlate>
> 采集：2026-10-29T20:41:52+08:00　|　id：`75fece20fdde6103`

## 正文

# TheWariend/CleanSlate

An open-source coding agent for the IDE, CLI, and SDK.

- Stars: 14
- Forks: 1
- Watchers: 14
- Open issues: 0
- License: MIT License
- Homepage: https://thewariend.com/cleanslate
- Default branch: main
- Created: 2026-07-27T16:55:29Z

## Languages

- Batchfile
- C
- C#
- C++
- CSS
- Clojure
- CoffeeScript
- Cuda
- Dart
- Dockerfile
- F#
- Go
- Groovy
- HLSL
- HTML
- Hack
- Handlebars
- Inno Setup
- Java
- JavaScript
- Julia
- Jupyter Notebook
- Less
- Lua
- Makefile
- Objective-C
- Objective-C++
- PHP
- Perl
- PowerShell
- Pug
- Python
- R
- Raku
- Roff
- Ruby
- Rust
- SCSS
- Scilab
- ShaderLab
- Shell
- Swift
- TeX
- Tree-sitter Query
- TypeScript
- Visual Basic .NET

## Top Contributors

- maaz7n (2 contributions)

---

## README

 CleanSlate
 The open source coding agent.

CleanSlate

---

### Installation

The current release is **CleanSlate 1.0.12**. See the release notes or download it directly:

| Platform | Download |
| -------- | -------- |
| macOS (Apple Silicon) | DMG · ZIP |

Builds are signed and notarized.

> [!NOTE]
> Intel macOS, Windows, and Linux aren't published yet. Build from source on those platforms.

### In the terminal

CleanSlate CLI

The same agent runs without the editor:

```sh
npm install -g @cleanslate/cli
cleanslate
```

Or try it without installing:

```sh
npx @cleanslate/cli "fix the failing test"
```

Node 20 or later. It walks you through provider setup on first run, and works
against any repository — the full tool set, not a reduced one.

See packages/cleanslate-cli for options, slash
commands, sessions, and MCP configuration.

### Building on the runtime

The engine behind both surfaces is published on its own:

```sh
npm install @cleanslate/sdk
```

It carries the execution loop, the tool registry, the edit engine and a Node host,
with no editor dependency. A surface supplies host capabilities — a filesystem,
a way to run commands, optionally diagnostics and a browser — and the runtime
drives the loop.

See packages/cleanslate-sdk.

| Package | Version |
| ------- | ------- |
| `@cleanslate/cli` | `1.0.10` · npm |
| `@cleanslate/sdk` | `1.0.12` · npm |

### Building from source

Requires Node.js 22.21.1 (see `.nvmrc`).

```bash
cd vscode-fork
npm install
npm run watch
./scripts/code.sh
```

### Modes

CleanSlate has two modes you can switch between per message.

- **Execution** — Default, full-access mode for building things
- **Plan** — Read-only mode for analysis and code exploration
 - Cannot edit files or run commands
 - Can still read, search, browse the web, and drive a browser
 - Ideal for exploring unfamiliar codebases or planning changes

### Models

CleanSlate is not coupled to any provider. Bring your own key for OpenAI, Anthropic, Google Gemini, Azure OpenAI, AWS Bedrock, xAI Grok, NVIDIA, OpenRouter, or any OpenAI-compatible endpoint.

Or sign in to **CleanSlate Pro** for managed models, higher limits, and pay-as-you-go credits. Pro is optional — everything works with your own key, and no account is required.

### What the agent can do

- Read, search, and edit across your whole codebase
- Run commands, including long-running ones in the background
- Drive a real browser to check its own work
- Search and fetch from the web
- Call any MCP server you configure

The editor includes a bundled model for local embeddings. The CLI and SDK can use configured embedding services; remote services receive the content being embedded.

### Extensions

CleanSlate installs extensions from Open VSX. The Visual Studio Marketplace is Microsoft-only and can't be used by forks.

### External agents

CleanSlate can act as an Agent Client Protocol (ACP) client for compatible local
agents. Each external agent runs as a separate process and uses credentials that
the user configured directly with that agent. CleanSlate does not collect,
store, proxy, or resell external-agent account credentials.

OpenCode, Grok, and Claude are discovered from the user's `PATH`. Claude support
uses the Apache-2.0 ACP adapter for Anthropic's Claude Agent SDK and explicitly
launches the user's installed Claude executable, preserving Claude's own
authentication boundary. Codex support uses the
Apache-2.0 `@agentclientprotocol/codex-acp` adapter bundled with the desktop
application. Other agents can be registered explicitly by the user in settings;
their installation, license terms, authentication, and usage charges remain the
user's responsibility.

CleanSlate is not affiliated with, endorsed by, or sponsored by Anthropic, OpenAI, xAI,
OpenCode, or any other external-agent provider. Product names and marks identify
compatible third-party services only.

### Contributing

Issues and pull requests are welcome — see CONTRIBUTING.md and our Code of Conduct.

To report a security issue, see SECURITY.md.

### License

CleanSlate is MIT licensed. Bundled third-party components remain under their
respective licenses; see NOTICE.

The CleanSlate desktop editor is based on Visual Studio Code (MIT, © Microsoft Corporation) — see LICENSE.txt. CleanSlate is not affiliated with, endorsed by, or sponsored by Microsoft.

Error fetching https://github.com/kishormorol/cli-faq-shortcuts: CRAWL_LIVECRAWL_TIMEOUT

## 关联链接

- https://github.com/kishormorol/cli-faq-shortcuts:
- https://thewariend.com/cleanslate

## 导航

- 项目页：[[10-项目/github.com_4925b62a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
