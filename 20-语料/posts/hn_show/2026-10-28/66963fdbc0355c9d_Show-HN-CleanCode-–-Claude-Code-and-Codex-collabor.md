---
type: "corpus"
item_id: "66963fdbc0355c9d"
title: "Show HN: CleanCode – Claude Code and Codex collaborating on one canvas"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50265699"
project_url: "https://github.com/chen-985211/cleancode"
author: "Tide-N"
published_at: "2026-10-27T20:57:26Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_Tide-N
  - story_50265699
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: CleanCode – Claude Code and Codex collaborating on one canvas

> [!info] 一句话导读
> chen-985211/cleancode

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50265699>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：Tide-N　|　发布：2026-10-27T20:57:26Z
> 项目链接：<https://github.com/chen-985211/cleancode>
> 采集：2026-10-28T09:39:16+08:00　|　id：`66963fdbc0355c9d`

## 正文

# chen-985211/cleancode

Bring Claude Code, Codex, and your favorite CLI agents into one visual workspace. Run agents in parallel and build executable workflows in isolated Git worktrees. Build your own AI coding team, and turn builds, tests, and dev servers into reusable canvas workflows.

- Stars: 63
- Forks: 9
- Watchers: 63
- Open issues: 1
- License: MIT License
- Default branch: main
- Created: 2026-07-11T05:41:49Z

## Languages

- CSS
- HTML
- JavaScript
- NSIS
- TypeScript

## Topics

- ade
- agent-collaboration
- agent-orchestration
- agentic
- agentic-coding
- agents
- ai-agents
- canvas
- claude-code
- cli
- codex
- electron
- mcp
- multi-agent
- opencode
- pi
- terminal
- visual-workflow
- worktrees

## Top Contributors

- chen-985211 (260 contributions)

---

## README

 CleanCode

 简体中文 · English

 A canvas-based ADE that puts each feature's Agents, terminals, and workflows into one runnable development context.
 Start with branch isolation, keep context and runtime state, and turn proven setups into reusable development assets.

 One feature. One visible, executable development context.

 Download CleanCode Preview (macOS / Windows / Linux)

 Coding Agents, terminal tasks, long-running services, and real dependency connections in one branch workspace.

 ▶ Multi-Agent Collaboration Demo (0:39)

https://github.com/user-attachments/assets/9e157258-5604-4da6-83f9-65943c19efc5

 ▶ Full demo (2:33, with sound)

https://github.com/user-attachments/assets/cafe373f-97b7-4f8c-b4a4-dfbc88ab26c3

---

Software development is moving from “one person writing code” to people and Agents advancing multiple development contexts together. One change may have its own branch, terminals, services, test commands, ports, and Agent conversation; another change has a similar context of its own. The problem is not a lack of tools. Once these contexts scatter across different windows, you have to keep rebuilding them from memory: which branch a terminal belongs to, whether a service is still alive, whether ports conflict, whether dependencies are ready, and whether the Agent still understands the current change. That is why I increasingly think a development environment should not be organized only around code files and editors. It should be organized around the change currently in motion. It needs to remember branches, terminals, services, ports, dependency order, and Agent context at the same time, and make them visible in a form people can understand and Agents can operate.

**CleanCode is a canvas-based ADE (Agentic Development Environment).** In CleanCode, a change is not just a branch name. It is a development context you can keep working in: Agents, terminals, services, ports, and dependency relationships all live on the same canvas. You can see how they relate to each other and run them directly; once that context is proven, it can be saved as a project template or global favorite, becoming an asset you can reuse the next time you build.

## One Change, One Development Context

When you create a branch workspace for `feature/auth`, CleanCode is not just checking out another Git branch. It opens an isolated development context for that change. It has its own Git worktree, and its own canvas, terminals, execution scope, and Agent sessions:

```txt
feature/auth (isolated worktree)
├── Coding Agent
└── Executable workflow
    └── Install dependencies ──> API service ──> Web app
                                               └─> Tests
```

That means you can work on `feature/auth`, `fix/search`, and `experiment/new-ui` at the same time without squeezing them into the same terminal history and service state. When you return to any workspace, you come back to that change's own context: terminal output is still there, Agent context is still there, and the working directory has not moved.

If two branches both need to start the same development service, CleanCode helps them avoid port conflicts. It can use fixed, preferred, or automatic ports, inject the final endpoint through the launch environment or command arguments, and show the actual address on the canvas.

## Draw the Dependencies, Then Run Them

Many development environments do not break because the commands themselves cannot run. They break because the order and conditions are not remembered by the environment: install dependencies first, wait until the API service is actually ready, then start the web app, and finally run tests. Those details often scatter across READMEs, script comments, terminal history, and human memory. Switch branches, or come back a few days later, and the whole flow has to be checked again.

In CleanCode, those startup conditions become an executable workflow on the canvas:

- Terminal blocks run real builds, tests, development servers, and everyday commands.
- Directed connections declare real dependencies. Tasks without upstream dependencies can start in parallel; downstream tasks wait until every direct dependency has completed or become ready.
- Finite tasks succeed or fail according to their exit codes, while long-running services become ready after matching output text or opening a TCP listener.
- Services can use fixed, preferred, or automatic ports; the runtime allocates and injects the final endpoint.
- An upstream failure explicitly blocks its descendants; stopping a workflow cleans up active processes in reverse dependency order.

So the canvas is not a static flowchart. Every run produces an immutable execution plan from the current terminal graph, and CleanCode keeps node state, failure reasons, and actual service addresses on the canvas.

If the API service does not become ready in time, the web app and tests that depend on it do not start blindly. You can see exactly where the workflow stopped, which descendants were blocked, and what actually failed.

## Prove It Once, Turn It into an Asset

Once a development context actually works, its value no longer belongs to just that one change. The exact command, the readiness signal, the port strategy, and the layout of the nodes are all experience you had to discover. In many teams, that experience stays in someone's terminal history, chat thread, or memory. The next branch starts, and the same context has to be rebuilt.

In CleanCode, proven terminals, workflows, or combinations can be saved as project templates; if they belong in more than one project, move them into global favorites. The next time a similar change appears, choose **Place** or **Place and run**, and CleanCode creates a new set of terminals and connections with their own identities, bringing back the commands, dependency relationships, port strategy, and relative layout together.

Templates keep reusable development structure, not temporary state from the last run. They do not copy terminal output, runtime state, actual endpoints, Agents, or Agent conversations. You can also bind frequently used terminals, complete workflows, or combinations to slots `1` through `5` in the current workspace, then run them with `Command/Ctrl + 1` through `5`.

## Bring Agents Back to the Development Context

If CleanCode is an ADE (Agentic Development Environment), the first problem it should solve is not inventing another Agent. You may already have tools that feel right: Claude Code, Codex, Gemini, Cursor, OpenCode, or another local Agent CLI. The real question is whether those Agents can enter a change and stand in the same context as the branch, terminals, services, ports, and dependency relationships.

**What needs to be preserved is not only the Agent itself, but the way you have learned to work with it.** You know when it should change code directly, when it should read the project first, and when it needs to stop and ask you. It has also adapted to your command line, permission habits, and the way you carry context. Asking you to switch Agents looks like switching tools; in practice, it means rebuilding a collaboration pattern.

That is why CleanCode does not try to start over. It does not ship a new Coding Agent or lock you into a closed system; it brings the local Agent CLIs already installed on your machine into the current branch workspace. Then an Agent is not entering an isolated chat window. It enters the place where the current change is actually happening: the right directory, the same canvas, running terminals, services, ports, and dependency relationships.

On top of that, Agents can participate in two ways. Every built-in Provider can have its own console, running a real local CLI in the current workspace; Agents that support the native CleanCode MCP can also read, inspect, and build terminal workflows on the canvas through explicit tool boundaries. When you create an Agent, CleanCode checks the Provider CLIs installed on your machine, so the menu is not a theoretical compatibility list. It shows the Agents that can actually start here.

There is a key idea here: CleanCode is not built by binding itself to a few specific Agents. Its foundation is the terminal, so the **33 Coding Agent Providers** are more like entries we prepared first: common Agent commands, icons, detection, and default arguments are already organized.

Look one layer deeper, and any Agent that can start from the command line can theoretically enter this canvas as a terminal process. Run the command in a terminal, then pin it to the current workspace with the pin button in the terminal header. Now it is no longer just a temporary command opened for one conversation. It becomes an Agent context that can stay in the background and keep working.

**Keep using the Agents you already know; CleanCode pins those CLI processes into a visible, runnable development context that stays with the work.**

## Let Agents Build the Context, Without Crossing the Boundary

We said above that Agents can stand on the same canvas as terminals, services, and ports. But being in the development context does not mean an Agent should bypass you and edit the canvas data behind your back. Agents that support the native CleanCode MCP use stable tools to understand the current workspace: they can see existing terminals and connections, inspect the real startup commands in the project, and build a new terminal workflow from your goal.

For example, you can simply tell it:

> Help me set up a workflow for starting this project.

The Agent first inspects the existing canvas, then reads the project to figure out what should be installed first, which services should start, and how ports and dependencies should connect. What lands on the canvas is not a suggestion, but a development context you can see, inspect, and keep running.

But there is an important boundary here: actions that change the structure of the context, such as deleting blocks, dissolving groups, or disconnecting dependencies, require approval in the CleanCode UI. Starting and stopping workflows also remain under human control. Agents can help build the context, but they should not turn your local development environment into a black box. What they changed, what they created, and what would run next should stay visible to you.

## Let One Feature Grow into a Development Context

Using CleanCode does not require planning a complete system first. Start with the feature you are working on right now: add the local project, create an isolated branch workspace for it, and bring in the Coding Agent you already use.

From there, you can turn installation, builds, tests, and development servers into terminal blocks yourself, or ask an Agent that supports the CleanCode MCP to build the first startup workflow. CleanCode puts finite tasks, long-running services, readiness conditions, ports, and dependency relationships on the same canvas, so the feature becomes more than a branch. It becomes a runnable context you can inspect and keep adjusting.

Once the workflow runs, start it from the root terminal and inspect startup order, runtime state, failure reasons, and actual endpoints on the canvas. After the context has been proven, save the terminals, workflow, or combination as a template, or bind it to a quick execution slot. The next time a similar feature appears, it is no longer just a configuration you repeat. It is reusable experience.

## Quick Start

If you just want to get CleanCode running, you do not need to understand every concept first. The steps below are enough.

### Download the Preview

Download the installer for your platform from GitHub Releases:

- macOS: Universal DMG/ZIP for both Apple Silicon and Intel.
- Windows: x64 NSIS installer.
- Linux: x64 AppImage/DEB.

> [!WARNING]
> The current Preview is not signed with official developer certificates. Download it only from this repository's GitHub Releases, and verify the package against `SHA256SUMS.txt` from the same release.

Because the app has not yet completed Developer ID signing and Apple notarization, macOS will block it the first time it opens. After moving `CleanCode.app` to `/Applications` and verifying the source and SHA-256 checksum, you can remove the download quarantine attribute for this app only and launch it:

```bash
xattr -dr com.apple.quarantine /Applications/CleanCode.app
open /Applications/CleanCode.app
```

This command bypasses the initial Gatekeeper check for this app. Do not replace the target with a broad path such as `/Applications`, your Downloads folder, or your home directory. Alternatively, follow Apple's official instructions and choose **Open Anyway** under **System Settings → Privacy & Security**.

### Source Development Requirements

These requirements apply only when running from source or contributing to development. You do not need to install these development dependencies before downloading the Preview.

- Node.js `>= 24`
- pnpm `>= 10`
- macOS, Windows, or Linux

### Run Locally

```bash
git clone https://github.com/chen-985211/cleancode.git
cd cleancode
pnpm install
pnpm dev
```

### Common Checks

```bash
pnpm typecheck
pnpm test
pnpm pre-commit
```

### Build Locally

```bash
# Unpacked app for the current platform, intended for local verification
pnpm package

# Distribution installer for the current platform
pnpm dist

# You can also select a target explicitly on the corresponding operating system
pnpm dist:mac
pnpm dist:win
pnpm dist:linux
```

All artifacts are written to `release/`. macOS builds Universal DMG/ZIP packages, Windows builds an x64 NSIS installer, and Linux builds x64 AppImage/DEB packages. The user-facing app name is **CleanCode**, while the internal package name remains `cleancode`.

When you push a `v*` tag that matches the version in `package.json`, GitHub Actions builds on all three target operating systems, runs a packaged-terminal smoke test, and creates a public Preview Pre-release. The Preview does not yet use official developer certificates: macOS uses ad-hoc signing without notarization, and the Windows installer is unsigned, so the operating system may display security warnings. Until official signing is available, these artifacts are public testing builds.

## Current Limitations

It is worth saying this directly: CleanCode is still a Preview. It can already organize terminals, Agents, branch workspaces, and executable workflows together, but some boundaries are not fully open yet.

- Executable block types currently remain terminal-centered, with terminal dependency workflows and terminal combinations. Preview, HTTP, Test, File, Plugin, and other standalone block types remain on the roadmap.
- Connections between terminals express startup dependencies only; they do not pass standard output, files, or structured artifacts between nodes.
- Agents can build, organize, and inspect terminal dependencies through MCP, but they cannot yet start, query, or stop workflows.
- Active workflows and Agent terminal processes do not continue running after the app exits. Recoverable terminals and upstream conversations reconnect according to their individual capabilities.
- Remote hosts, distributed execution, and cross-project workflows are not currently supported.
- The plugin extension system is not yet public, and third-party plugin compatibility is not guaranteed.
- The prebuilt packages on GitHub Releases are unsigned Preview builds, not signed production releases.

## Design Principles

These principles are not decorative slogans. They exist so the canvas can feel free while the runtime stays trustworthy.

- **The canvas is not the source of truth.** It only projects the domain model and runtime state.
- **People and Agents share the same use cases.** Agents do not bypass application boundaries to manipulate internal implementations.
- **Workspace isolation comes first.** Branches, directories, ports, and sessions must have explicit ownership.
- **Dangerous actions must be visible.** Capabilities that change processes, files, or workspace state require approval and auditing.
- **Failures must be explainable.** Plans, readiness, endpoints, and errors should map back to objects users can understand.

For architecture and domain boundaries, see the Architecture Guide and Context Map.

## Documentation

- Product Features and Quick Start
- Documentation Center
- UI Contract
- Terminal Dependency Workflows
- Agent and Session Lifecycle
- Native CleanCode MCP
- Development Guidelines

## Contributing

Issues, discussions, and pull requests are welcome. Before you begin, read the Contributing Guide and Development Guidelines.

## License

MIT

---

 Join the CleanCode Community

 Share the workflows you build, the way you use Agents, and Preview feedback.

 QQ group: 186885114
 Scan with QQ, or search for the group number to join

# milad-ahmd/agent-skills

## 评论（2/2）

> **build_with_ragh** · 2026-10-27T21:03:04.000Z　
> what made you settle on the thought that you ll build this?

---

> **Tide-N** · 2026-10-27T21:11:01.000Z　
> I wanted to explore a more visual way to work with coding agents.With CleanCode, Claude Code and Codex can share a workspace and send tasks to each other. I can see their work on the same canvas and step in when needed

## 关联链接

- https://github.com/chen-985211/cleancode.git
- https://github.com/user-attachments/assets/9e157258-5604-4da6-83f9-65943c19efc5
- https://github.com/user-attachments/assets/cafe373f-97b7-4f8c-b4a4-dfbc88ab26c3

## 导航

- 项目页：[[10-项目/github.com_778dd933]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
