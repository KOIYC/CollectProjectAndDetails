---
type: "corpus"
item_id: "47303bb1c1fd7feb"
title: "Show HN: AgentMon Live a Local Monitor for Claude Code, Codex and Kiro Crew"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50522518"
project_url: "https://github.com/codenotary/agentmon-live"
author: "vchain-dz"
published_at: "2026-11-16T20:14:18Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_vchain-dz
  - story_50522518
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: AgentMon Live a Local Monitor for Claude Code, Codex and Kiro Crew

> [!info] 一句话导读
> codenotary/agentmon-live

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50522518>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：vchain-dz　|　发布：2026-11-16T20:14:18Z
> 项目链接：<https://github.com/codenotary/agentmon-live>
> 采集：2026-11-17T11:09:12+08:00　|　id：`47303bb1c1fd7feb`

## 正文

# codenotary/agentmon-live

See what Claude Code and its subagents are really doing, live in your browser or beside the chat: what it costs, how close you are to your limits, when it needs you, and a check of its work before it says done. 6 languages.

- Stars: 27
- Forks: 2
- Watchers: 27
- Open issues: 7
- License: Apache License 2.0
- Homepage: www.codenotary.com
- Default branch: main
- Created: 2026-10-25T15:04:14Z

## Languages

- CSS
- HTML
- JavaScript
- Shell
- TypeScript

## Topics

- ai-agents
- claude-code
- claude-code-plugin
- developer-tools
- i18n
- terminal-ui

## Top Contributors

- vchaindz (132 contributions)
- dolbik (4 contributions)
- dzlabsch (4 contributions)

---

## README

 AgentMon Live

 See what your AI agents are really doing.

 Watch Claude Code and its subagents work, live in your browser or beside the chat. See what it costs, how close you are to your limits, and when it needs you. AgentMon also checks Claude's work before it says "done".

 Install · Why you want it · The pane · The web view · Cost and privacy · Make it yours · More

**Press `o` and your session opens in the browser.** See who started whom, what each agent does right now, and where the money goes. See all of it.

The web view during a session: dials and rulers fill up while the main session starts subagents and the agent flow grows

## Install

In a Claude Code session (2.1.308 or later):

```
/plugin install agentmon-live --marketplace codenotary/agentmon-live
```

Answer `y` to add the marketplace and pick a scope. There is nothing to set up. The pane opens by itself when the terminal is wide enough, or with `/agentmon`.

 From a shell, the desktop app, or let Claude do it

```sh
claude plugin install agentmon-live --marketplace codenotary/agentmon-live
```

Desktop app: click + next to the prompt box, then Plugins, Add marketplace with `codenotary/agentmon-live`, then Add plugin.

Or paste this into a Claude Code session:

```
Install the Claude Code plugin agentmon-live from the marketplace codenotary/agentmon-live
(claude plugin install agentmon-live --marketplace codenotary/agentmon-live). Tell me to restart
Claude Code when done.
```

## Why you want it

- **See it happen.** Every agent, tool call and handoff, live in your browser, in the agent flow.
- **Don't run out.** Cost, context and quota limits at a glance, and when `/clear` or `/compact` would save you money.
- **Know when to step in.** It raises a waiting approval, a stuck subagent or a failure loop. Press `i` and it drafts the follow-up question for you.
- **Trust "done".** Claude says all tests pass? AgentMon checks, and sends it back if they don't.
- **It learns your project.** It remembers flaky tools and recurring errors across sessions, and spots drift in your CLAUDE.md.
- **Measure it.** `/agentmon bench` compares your sessions with and without AgentMon.

Speaks English, German, French, Spanish, Chinese and Japanese, and follows your terminal's language. The guide has the details, including everything the done gate checks.

## The pane

AgentMon Live pane, section by section: header, Focus, running call, Insights, done gate, changes and verification, Usage, tool history, subagents and session log

AgentMon Live demo: the done gate catches a failing test before Claude stops

## The web view

Press `o`, or run `/agentmon open`. It needs `node` on your `PATH`, which Claude Code does not include; everything else works without it. It is local only, and the one thing it can change is showing or hiding the pane.

One page, with a rail that moves between its sections: Overview · Tool calls · Verification · Subagents · Files · Session log. Each section folds, each widget has an `i` that explains it, and every running session is one click away in the top bar. The pictures show a made-up session.

### Overview

Context, quotas, cache hits, cost and turns measured against their limits or your usual sessions, coloured good or bad. Pins move on a change and shake slightly while the page is connected.

Top band: dials for context, quotas and cache hits, rulers for cost, turns and time blocked on you, and a bar splitting tokens in and out

The agent flow shows who started whom, when each subagent handed back, the messages agents sent each other, and where a call failed. Dashed lanes are still running; dotted verticals are check runs, such as tests. Drag the strip on top to pick a time, or press 1, 5 or 15 min, and the waterfall below follows it.

Agent flow: the main session starts six subagents, one reports failing tests, and two still run

The waterfall shows every call in that time, nested under the agent that made it. Beside it are what needs you, with buttons for failures, waiting, context and memory, and what runs now, and below it where each turn's time went.

Turn waterfall, Events, Running now and where each turn went

### Tool calls

Every tool call, sortable, with filters by tool (one per MCP server), by agent and for failures. Click a row for its details. Insights lists the slowest calls, the largest results and approvals asked more than once.

Tool calls table with filters, and Insights

### Verification

The last test, type check, lint and build, files changed since the last passing test, and test files whose checks were removed or changed; other edited test files are only counted. Tasks sit beside them.

Verification lights, edited test files and Tasks

### Subagents

One row per subagent, worst first, ten at a time plus every running one. Health dots compare its duration, tokens and errors with the session's other subagents. Click a row for its prompt and calls.

Subagent table with calls, tokens, cost, errors, files and health dots

### Files

Edited files, paths inside the project, grouped by whether they still need a test: not tested since the last passing run, then edited before it. Files only read follow, most read first.

Files: not tested since last green, before the last passing test, and only read

### Session log

One searchable stream of your prompts, Claude's answers, tool calls and subagents. A subagent is one row that unfolds to its calls, equal calls merge, and a failed call keeps its own red row. Filter with the buttons, or click a red bar to go to that failure.

Session log with filter buttons, activity bars and rows

## Cost and privacy

- **Your session stays on your machine.** The web view listens on `127.0.0.1` only, and what AgentMon learns is kept in Claude Code's local plugin store. Secrets are masked before they are shown.
- **The web view is yours alone.** On Linux the server asks the system which account a browser runs as and lets only yours in: you open the address and type nothing, also through an SSH port forward. On macOS and Windows AgentMon opens the page with a one-time code (`o` or `/agentmon open`), and the browser keeps its pass until the server stops. Sessions and server prove to each other that they belong to your account, with a secret that never leaves `~/.claude/agentmon-live/web.token`. `webToken: off` turns all of this off; see the guide for the limits.
- **One optional model call.** Before Claude stops, Fable, a second model, may check that every part of your request got an answer and that nothing you did not ask for got built: a small call with about 12,000 characters of session text, at most 30 per session by default. Set `advisorMode` to `gate` for no model calls at all.
- **One network check.** It asks GitHub for the latest release. No session data goes with it.

To remove it: `claude plugin uninstall agentmon-live`.

## Make it yours

Just ask Claude: *"hide the usage box"*, *"switch AgentMon to German"*, *"turn the done gate off"*. It takes effect at once, with no reload. Or edit `pluginConfigs` in `~/.claude/settings.json` yourself; that applies at your next prompt. The options are not in `/config`. See the guide for all of them.

 All keys

| Key | Does |
| --- | --- |
| `i` | Draft a question about the top Focus item, or the slowest call |
| `u` | Draft the update commands, when a new release is out |
| `l` | Show the new release's changelog |
| `x` | Put Focus items away |
| `d` | Show long lists and texts whole |
| `h` | Fold the history |
| `a` | Fold out all running subagents, past four |
| `v` | Switch between the calm and classic layout |
| `o` | Open the web view in your browser |
| `p` | Hide the pane; a button above the prompt brings it back |
| `c` | Run the done-gate check now |

Commands: `/agentmon`, `advisor`, `check`, `open`, `learn`, `memory`, `bench`, `debug`, `clear`.

## More

- Guide: every section of the pane, all commands and options, the done gate, the file-size guide, learning, the debug log and the self benchmark.
- Develop: build, test, and see the real pane from a script.

Developed by vchaindz. Apache License 2.0.

## 评论（1/1）

> **vchain-dz** · 2026-11-16T20:14:30.000Z　
> I built AgentMon because I use Claude Code and Codex in different terminals and needed a way to monitor all my sessions, switching models and the done gate.
> No data leaves your system, all run on localhost and is restricted by default.It started as a Claude Code mod with a pane beside the chat. Now it has a local browser view, that supports also Codex and Kiro Crew sessions.
> AgentMon Live also provides insights to optimize the agent sessions.There is a Claude-specific completion check, that before Claude finishes, checks for things like failed checks, missed tests, no-test runs and unfinished tasks. When detected it can send unfinished work back to Claude once.Many new features are based on Reddit community feedback, and there is a lot of day to day experience built-in.The repo has installation guidelines, screenshots and a demo. Project is Apache-2.0 licensed.I'm super interested in feedback to make it the most useful for monitoring agentic coding. If you like it you can also star the repo as a sign.

## 导航

- 项目页：[[10-项目/github.com_d3ed6706]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
