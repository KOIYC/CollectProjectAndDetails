---
type: "corpus"
item_id: "84b380aca78dc647"
title: "Show HN: Intent-lens – see what Claude Code is about to do, before it does it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50341363"
project_url: "https://github.com/Dhananjay-JSR/claude-mods/tree/main/plugins/intent-lens"
author: "dhananjay-jsr"
published_at: "2026-11-02T18:33:28Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_dhananjay-jsr
  - story_50341363
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Intent-lens – see what Claude Code is about to do, before it does it

> [!info] 一句话导读
> claude-mods/plugins/intent-lens at main · Dhananjay-JSR/claude-mods

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50341363>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：dhananjay-jsr　|　发布：2026-11-02T18:33:28Z
> 项目链接：<https://github.com/Dhananjay-JSR/claude-mods/tree/main/plugins/intent-lens>
> 采集：2026-11-03T09:40:36+08:00　|　id：`84b380aca78dc647`

## 正文

claude-mods/plugins/intent-lens at main · Dhananjay-JSR/claude-mods · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| parent directory.. | | | |
| .claude-plugin | .claude-plugin | | |
| assets | assets | | |
| hooks | hooks | | |
| tests | tests | | |
| README.md | README.md | | |
| tsconfig.json | tsconfig.json | | |
| View all files | | | |

## README.md

# intent-lens

See what Claude is about to do — before it does it.

 Part of the claude-mods marketplace.

 A real Claude Code session with intent-lens loaded.

A Claude Mod that shows the intent of a tool call in one line above the prompt, while the call is still pending.

Claude Code shows you a tool row after Claude has already decided to act. `intent-lens` translates the call into a human sentence first, in the place your eyes already are. It reads either the tool's own arguments (free, instant) or asks Claude to phrase it (a few tokens).

## Why

In auto mode, Claude Code moves faster than you can read, and the commands it writes are made for the shell, not for you. A `find | xargs | awk` pipeline tells you almost nothing at a glance, and once it runs, the call folds into a summary like Ran 2 shell commands.

intent-lens puts the meaning where your eyes already are, just above the prompt, while the call is still in flight:

- Understand it at a glance. One sentence for the call, and each stage of a pipeline in plain words.
- Catch the dangerous ones. A recursive delete, a force-push or `curl … | sh` turns the line red and raises a warning, even when the band is hidden.
- Pay nothing for it. By default it reads the tool's own arguments: no tokens, no network.

### From the marketplace

Register the catalog once, then install this mod:

```
/plugin marketplace add Dhananjay-JSR/claude-mods
/plugin install intent-lens@claude-mods

```

From your shell:

```
claude plugin marketplace add Dhananjay-JSR/claude-mods
claude plugin install intent-lens@claude-mods
```

Installs are cached. To take a newer version later:

```
claude plugin update intent-lens
```

### For one session

```
claude --plugin-dir /path/to/claude-mods/plugins/intent-lens
```

To load it without typing the flag, alias it in your shell:

```
alias claude-lens='claude --plugin-dir /path/to/claude-mods/plugins/intent-lens'
```

To load it in every session, add the directory to `CLAUDE_CODE_PLUGIN_DIRS` (`:`-separated).

Check it loaded with `/plugin` (Tab to Installed) or just run `/intent`.

## Two engines

| Marker | Engine | What it does | Cost |
| --- | --- | --- | --- |
| `▸` cyan | local | Deterministic translation of the tool's arguments | none |
| `✦` magenta | model | Claude writes the line from the tool, its arguments, and the local draft | at most 60 output tokens per call, plus the prompt |
| `⚠` red | risk | Always local: a destructive shell command is never sent to the model | none |

`auto` (the default) draws the local line immediately, then upgrades it with Claude for the calls that read worst — edits, unknown tools, and MCP tools. The band never sits blank while the model thinks.

```
▸ Bash   Count the top five languages across your repos
         6 steps · fetch → extract values → sort → count repeats → sort by number → top 5
✦ Edit   Add a null guard to the token parser
⚠ Bash   delete files recursively

```

The command itself stays in Claude Code's tool row. The band answers what it means.

Switch engines with `/intent mode local`, `auto`, or `model`.

## Commands

| Command | What it does |
| --- | --- |
| `/intent` | Show the current state and usage |
| `/intent on` / `off` / `toggle` | Show or hide the band line (persisted). Warnings still fire when off. |
| `/intent mode local|auto|model` | Choose the engine (persisted) |
| `/intent words plain|terse` | Plain vocabulary (default), or the shorter one (persisted) |
| `/intent log` | The last 20 calls with `✓` / `✗` outcomes and their engine |
| `/intent clear` | Forget the history |
| `/intent-log` | Same as `/intent log` |

## How the intent is worked out

The local engine is a pure function of the tool name and arguments — no I/O, no latency.

| Tool | What it says |
| --- | --- |
| `Bash` / `PowerShell` | Claude's own `description`, plus a decoded chain of its stages |
| `Read` | `~/app/src/auth.ts:10-20` |
| `Edit` | `~/app/src/auth.ts (12 lines → 24 lines)` |
| `Write` | `~/app/notes.md (48 lines)` |
| `Grep` | `"useEffect" in ~/app/src` |
| `Glob` | `**/*.test.ts under ~/app` |
| `WebFetch` / `WebSearch` | `example.com — extract the rate limit table` / `"…" on the web` |
| `Task` / `Agent` | `explore subagent — find the auth middleware` |
| `TaskCreate`, `EnterPlanMode`, `ToolSearch` | A short phrase each, e.g. `add a task: write the migration` |
| `TodoWrite` | `update the task list (6 items)` |
| `AskUserQuestion` | `ask you: Which database should this use?` |
| `mcp__server__tool` | `server:tool` |
| anything else | Its first two string arguments, so new tools still say something |

`Bash` is the interesting one: Claude Code's Bash tool already requires Claude to describe each command, so that description is the stated intent — normally buried in the tool row.

Under a pipeline, a second dim line decodes it stage by stage: `6 steps · fetch → extract values → sort → count repeats → sort by number → top 5`. Only pipelines of three or more stages get that line, because a two-step chain reads fine as it is. The mapping is literal — `curl` → fetch, `jq 'select(…)'` → keep matching rows, `uniq -c` → count repeats, `head -5` → top 5 — and quote-aware, so a `|` inside a jq program is not a new stage. `/intent words terse` switches to the shorter vocabulary (`pick fields`, `rank`). It explains the mechanics; the full command stays in Claude Code's tool row.

The model engine sends the tool name, a bounded view of the arguments (900 characters), and the local draft to `haiku`. It asks for at most 12 words, hard-caps the answer at 110 characters, and waits at most 1.5 seconds. `auto` also reaches for the model when a shell command arrives without a description, since the local line would then have to fall back to the raw command. A failure, a refusal, or a slow reply silently keeps the local line: the intent must never break a call.

## Risk detection

Shell commands are matched against patterns that can destroy work or reach outside the project: recursive `rm`, `git reset --hard`, `git clean -fd`, force-push, `DROP`/`TRUNCATE`, `mkfs`/`dd`, fork bombs, `curl … | sh`, `sudo`, `chmod -R 777`, package publishes.

A match turns the marker red and raises a toast. It is computed locally and always shown — in `model` mode, and even when the band is hidden. It is a reminder, not a sandbox: it matches the text of the command.

## Privacy and cost

- `local` mode sends nothing anywhere and costs no tokens.
- `auto` mode calls the model only for edits, unknown tools, MCP tools, and a shell command Claude didn't describe — a few hundred tokens per edit.
- `model` mode calls it for every tool call, which adds up to 1.5 seconds of latency per call.
- Model calls use your own Claude Code credentials and go through `$.model.complete`, exactly like any other request the session makes.
- Headless runs (`claude -p`, Agent SDK) never raise `ui.render`, and the mod calls the model only after that event has fired, so such a run spends nothing.

## Layout

```
plugins/intent-lens/
├── .claude-plugin/plugin.json   the manifest
├── hooks/hooks.json             {"modules": ["./register.js"]} — makes it a mod
├── hooks/register.js            hooks, both engines, risk rules
├── tests/intent.test.mjs        hooks run against a stubbed API
├── assets/logo.svg              the mark
├── assets/demo.svg              the band, illustrated (all three markers)
└── assets/screenshot-*.png      a real session

```

## Tests

`claude plugin test` runs `.test.ts` files inside a session; these tests are plain Node instead, so they need no session, network, or credentials. They load the hooks module from a temporary copy and fire every hook — including `session.start` — against a stubbed mods API. Each test gets a fresh copy of the module, so one test's mode, history, or UI flag can never leak into the next.

```
node tests/intent.test.mjs
# 62 pass, 0 fail
```

Run it from this folder. The repository's CI runs the same tests and `claude plugin validate --strict` on every push, then installs the plugin from the marketplace entry to prove that path works too.

## Limitations

- The band shows the call in flight, not a history, and clears the moment the call returns. With parallel calls, the newest takes the line and an older one finishing does not erase it.
- Calls made by subagents are skipped, so one line is always the main thread's.
- Nothing is drawn in headless runs, where there is no UI.
- The model line is a hint about what Claude says it is doing; the arguments are the ground truth.
- The band is a shared surface: it sits above whatever other mods draw, and the user can collapse it with `Ctrl+X Ctrl+A`.

## License

MIT.

# amanthanvi/noctty

## 评论（1/1）

> **dhananjay-jsr** · 2026-11-02T18:35:32.000Z　
> Hey HN. I use Claude Code in auto mode a lot and kept catching myself not reading the commands it runs. They scroll past fast, and half of them are find | xargs | awk one-liners I'd need a minute to parse anywaySo I made a small plugin that puts one plain line above the prompt while the call is running, like "Survey disk usage by file type", and for longer pipelines it spells out the steps. If the command looks destructive (rm -rf, force push, curl | sh, that kind of thing) the line goes red and you get a warning for a few secondsIt works off the tool's own arguments, so by default there's no extra model call and nothing leaves your machine. There's an optional mode where it asks Claude to reword the unclear ones, mostly editsThe risk check is just pattern matching on the command text, so think of it as a heads-up, not a safety netCurious what else you'd want it to catch

## 导航

- 项目页：[[10-项目/github.com_0f6eaef3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
