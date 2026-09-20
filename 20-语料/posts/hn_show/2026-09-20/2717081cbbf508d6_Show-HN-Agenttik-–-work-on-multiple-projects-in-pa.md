---
type: "corpus"
item_id: "2717081cbbf508d6"
title: "Show HN: Agenttik – work on multiple projects in parallel with AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49720222"
project_url: "https://github.com/pausan/agenttik"
author: "psanchez"
published_at: "2026-09-15T23:24:53Z"
captured_at: "2026-09-20T14:05:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_psanchez
  - story_49720222
  - show_hn
metrics: {"points": 4, "comments": 2, "engagement_velocity": 4}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Agenttik – work on multiple projects in parallel with AI agents

> [!info] 一句话导读
> Manage multiple projects and agents with ease

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49720222>
> 指标：点赞=4 · 评论=2 · engagement_velocity=4
> 作者：psanchez　|　发布：2026-09-15T23:24:53Z
> 项目链接：<https://github.com/pausan/agenttik>
> 采集：2026-09-20T14:05:48+08:00　|　id：`2717081cbbf508d6`

## 正文

# pausan/agenttik

Manage multiple projects and agents with ease

- Stars: 4
- Forks: 1
- Watchers: 4
- Open issues: 0
- License: MIT License
- Default branch: master
- Created: 2026-09-09T18:50:04Z

## Languages

- CSS
- Go
- HTML
- JavaScript
- Makefile
- Python
- Shell
- Vue

## Top Contributors

- pausan (318 contributions)
- miki-gh (4 contributions)
- solracfs (1 contributions)

---

## README

# agenttik

A local workspace for running AI coding sessions across multiple projects.
Use Claude Code, Codex and GitHub Copilot through their official CLIs, with your existing login,
in one desktop window or browser tab. Desktop builds support Linux, macOS ARM64,
and Windows x64.

A private workspace with fictional projects, a task conversation, and changed files

## Main features

- **Project workspaces:** organize sessions and file tabs; archive and restore conversations.
- **Orchestrator:** enable a separate pinned project in Settings to inspect work and manage tasks across projects, with editable instructions and a reset to the built-in prompt.
- **Live sessions:** stream replies, resume conversations, and queue prompts per project.
- **Reusable work:** pin prompts and schedule recurring tasks.
- **Model controls:** choose models, effort, permissions, and favorite combinations.
- **Code tools:** browse and edit files, preview Markdown/HTML, inspect Git diffs, stage changes, and write commits.
- **Usage tracking:** view tokens, context usage, subscription allowance, and costs where reported.
- **Local state:** SQLite history, remembered tabs, customizable shortcuts, and color themes. Use profiles for separate workspaces or private mode for a temporary one.

Claude Code is working; Codex, GitHub Copilot and OpenCode Go are implemented, with live-turn validation still pending. OpenCode Go supports direct use with a subscription key and an optional CLI; Settings defaults to the CLI when installed.

## Screenshots

Captured from a fresh private instance and browser context with fictional projects
and demo conversation data. No live agent was run. Click an image to view it full size.

### Review code where you work

Open a changed file beside your project tasks. Compare the diff, stage individual
files, and prepare a commit from the workspace panel.

Shipping-rule diff with project tasks and Git staging controls

### Schedule recurring work

Give a recurring task its own prompt, model, and schedule. Review its next run and
history, or pause it from the same view.

A daily quality review with its prompt, schedule, and run controls

## Quick start

Use Go 1.25+, Node.js 22.12+ with npm, and either a logged-in `claude`, `codex` or `copilot` CLI on `PATH`, or an OpenCode Go key configured in Settings → Subscriptions. The `opencode` CLI is optional.

```sh
make run-web
```

Open localhost:7717, add a project folder, and start a session.
Or add one from the terminal with `agenttik --init` in the folder you want —
`agenttik --init path/to/repo` names another — which works whether or not the
app is already open, and shows up in an open window straight away.

### Remote servers and private workspaces

Connect to another server with `agenttik --remote host:7717` (or an HTTPS
URL), or choose **Connect to remote server** in the command palette. The
client checks `/api/version` first, then shows the server’s login if needed.
See remote connections.

Start a temporary, separate instance with `agenttik --private`. Its app data is
removed on exit; project files stay on disk. Manage local profiles in
**Settings → Profiles**. With multiple profiles, the picker before Shortcuts
switches between their isolated projects and tasks.

`--addr` and `--data-dir` change where it listens and where it keeps its
database, `--web` skips the desktop window, and `--help` and `--version` say
what this build is.

### Desktop builds

For the desktop app, install the native build dependencies (`make deps` on
Debian/Ubuntu), then run `make run`. `make build-windows-amd64` cross-compiles
the Windows x64 binary; build the macOS ARM64 target on macOS with
`make build-macos-arm64`. macOS builds also create an ad-hoc-signed
`agenttik.app` and a ZIP (`bin/` for `make build`, `dist/` for the ARM64 target).
Extract the release ZIP and move the app to Applications. No Apple developer
account is needed to build it. Downloaded builds are not notarized; after a
blocked launch, use System Settings → Privacy & Security → Open Anyway.

On macOS, Close to tray works even without Accessibility permission. The global
show/hide shortcut needs that permission; grant it in System Settings → Privacy
& Security → Accessibility, then restart agenttik. Shortcut failures appear in
agenttik's desktop settings while the tray menu remains usable.

**Local access by default:** agenttik binds to loopback. Anyone who can reach an
unauthenticated server has full control of it. Before exposing it through
**Settings → Server**, configure authentication and use a trusted network. See
server access.

Built with Go, SQLite, Vue 3, Nuxt UI, and Wails. See specs
for architecture and implementation details.

## License

MIT.

# 35 Poems of John Muconto — A Journey Through Life

## 评论（2/2）

> **eskim2001** · 2026-09-16T09:58:23.000Z　
> I tried building something similar last year. while it's fun but hard to get the tasks properly done, it wasn't for real work at the time. and projects like GPT Swarm have died out since then.agents' intelligent have become more capable today, can a multi-agent setup like this finally handle real production work? if so, may i know how exactly do you incorporate it into your daily workflow

---

> **psanchez** · 2026-09-17T04:38:54.000Z　
> There's this thread [1] that I forgot about, and on other user's comment [2] and my own comment [3] you can get an idea on how I was approaching multi-tasking on the same project with AI.In the links you can see more of the setup for a single project, specially on [3]. The main idea remains, what agenttik tries to do is to simplify the management of iterating over one or multiple projects at the same time.There are two ways in which I'm using the tool for production work.On one hand, from the issue tracker (we use JIRA at my company), I just have MCP connected to it, and the way it goes is, in the AGENTS.md I have several instructions on how to work with each project, and there's a line like this:*Commits.* Small, regular, descriptive. Work on branches (`feat/`, `bugfix/`), never on `main`/`master`/`develop`.Now, with this in mind, what I do is pick a ticket, Ctrl+Shift+A to bring agenttik to the foreground, go to the project, Ctrl+T to open a new task in that project, then say something like:Let's work on TICKET-1234. For this task, let's consider blah, blah, [...]Now, sometimes tickets have full context, other times they don't. Depending on the ticket I would either explore the angle we should follow or I just say like, work on this ticket.Then I open another ticket, same project or another, and I just spawn more work like this. I would just leave the agent do its work, and later go back to that task and have a look at the last commit message, where there's usually a summary on what's done and review the new branch & commits and push. You can also have a line saying the AI to just push changes and look for build to succeed and keep iterating if not, but anyway, depends on the project.Now, the second way in which I manage production work is for BIG features. A big feature is one thatthat I would usually break down in smaller tickets. Instead of splitting them in JIRA, I just don't split it. I just then open the project in agenttik, and I start creating multiple tasks by breaking down that big task into smaller tasks. By splitting them in agenttik tasks, each task will have a fresh session/context when it runs via the agent, thus, I keep LLM context usage small and I can also fine-tune what model to use for each tasks, optimizing a little bit my usage.Since the tasks are enqueued, I can just jump to another project and do the same, or have a meeting while agents fix the work, ...The main benefit for me, is that by enqueing tasks I can get full focus on a project or feature, know that a complex feature is already divided in smaller, simpler, tasks, and that for an hour or more I don't need to worry about that project or feature anymore. I can just put my focus elsewhere.The problem when I was having multiple consoles/windows managing agents like this, was that I would start dividing the problem in my head, or I would create a big file and pass as a context, but then, either iterations depleted the agent's context if it was big enough tasks, or then I would get constantly interrupted when working on a different thing because first task would finish, and then I need to switch context in my head, and back to another project, and forth, and then switching context in my head makes me mentally exhausted.Even for single-project, same happens, you spawn something here, another thing in another branch/worktree/folder and you keep jumping back and forth; by enqueuing all tasks you can think of, you give more work to the agents, so that you can keep your own focus, and at the end of the day I'm not exhausted anymore. Not only that, agents will continue with the next enqueued tasks a second after the one they are working on finishes. When I was working in terminals/multiple windows, I would switch window, then start writing, and then there's extra latency where the agents are doing nothing till next task is sent.Also because tasks are enqueued, and run in order, if you remember or missed something or want to provide more context, then you go to the task and edit it before it runs, or you can add another task and just enqueue in the right place for AI to pick it up.To me it toally helps to reduce cognitive effort. I was already working like this to some extent, but with this tool it makes it way easier and enqueuing tasks is what makes the difference.On another note, on certain projects I have an scheduled task which runs every X minutes and can pick stuff where previous tasks left, and continue the work. On those I just instruct the agents to leave some partial outcome in specific files, so that the next ones can pick it up where the other left.Nothing would prevent me as well to create an scheduled task to say, go to this project X in JIRA and pick next task in priority, create a branch, mark it as ready for QA, and push changes; the only reason I'm not doing that is because I want to review and I want to be the one spawning tasks because sometimes tickets lack info. I could also instruct just to pick tasks with good context and such, or label tasks in JIRA so that later the agent would pick it up automatically, and I could even leave agenttik running in another computer and connecting remotely. I haven't explored this at work yet, but agenttik is also built for this kind of workflow.[1] https://news.ycombinator.com/item?id=49413093[2] https://news.ycombinator.com/item?id=49414469[3] https://news.ycombinator.com/item?id=49415263

## 导航

- 项目页：[[10-项目/github.com_0085a204]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
