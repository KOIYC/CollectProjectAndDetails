---
type: "corpus"
item_id: "2de812909d55a6a7"
title: "Show HN: Agent-relay for multi-vendor coding sessions"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50262407"
project_url: "https://github.com/saranyan/agent-relay"
author: "svts"
published_at: "2026-10-27T17:14:54Z"
captured_at: "2026-10-28T09:55:51+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_svts
  - story_50262407
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Agent-relay for multi-vendor coding sessions

> [!info] 一句话导读
> saranyan/agent-relay

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50262407>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：svts　|　发布：2026-10-27T17:14:54Z
> 项目链接：<https://github.com/saranyan/agent-relay>
> 采集：2026-10-28T09:55:51+08:00　|　id：`2de812909d55a6a7`

## 正文

# saranyan/agent-relay

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-10-25T03:27:19Z

## Top Contributors

- saranyan (11 contributions)

---

## README

# agent-relay

tests

**Let AI coding sessions from different vendors work together, while you stay in charge.**

## Why

Claude can hand work to Claude on its own. But when you work with sessions from
**different vendors**, such as Codex for planning and review and Claude Code for
the code, they can't talk to each other. Without a relay, **you're the one
transferring context**: copying plans, results and reviews between terminals.

agent-relay carries the turns for you. One session leads, the other follows, and
the relay passes each turn across, records it on your disk, and stops whenever
something needs your decision. It's tested with Claude Code and Codex, and you can
extend it to whatever agents you work with by writing an adapter.

 Watch: what the managed session is doing, in plain language.
 Decide: questions stop the loop until you answer.

## Try it in two minutes

These demos use pretend sessions, so they're safe to run anywhere and use no model
quota. You need macOS and Python 3.11 or newer.

```sh
git clone https://github.com/saranyan/agent-relay.git && cd agent-relay

scripts/console-demo.sh      # the web console, with a few pretend sessions
scripts/walkthrough.sh       # the full two-terminal flow in a temporary folder
```

With the Claude Code and Codex CLIs installed, run it on real sessions:

```sh
export AGENT_RELAY_ROOT=~/relay-root
bin/relay init --participants codex claude
bin/relay console      # [n] launch Codex and Claude Code, [p] pair them, [s] start
```

The web console tour walks through every screen. The
walkthrough shows a recorded run with real message and turn
IDs.

## What it can and can't see

The relay coordinates **two sessions per team**, one turn at a time. It sees each
turn from the outside: the turn goes in, the client acknowledges it, and later the
client reports it finished. **What a session does inside a turn is invisible to
the relay.** That includes tool loops, subagents and long-running commands.

- **The turn budget counts hand-offs, not work.** One turn can hide a lot of
 activity. The per-turn timeout is the only hard limit inside a turn.
- **The routes the relay starts are locked down where it can.** A Claude Code
 follower starts with no tools at all, or, under the coding policy, with only
 Read, Edit, Write, Glob and Grep inside a macOS sandbox. It can't start
 subagents or run commands. Codex's multi-agent mode is recorded but not yet
 enforced.
- **Sessions you open in a terminal keep whatever you allowed them** until you
 hand them over.

The full list of guarantees and limits is in the reference.

## What you can use it for

**Today, with the prototype:**

- **Plan, build, review.** Codex writes the plan and reviews the result. Claude
 implements. The loop runs until the reviewer accepts or asks you something.
- **A second opinion on every change.** Use one model to critique the other's work
 before you ever see it, so you review a reviewed change.
- **Bounded jobs you don't have to babysit.** "Fix the failing tests in this
 folder, at most 8 turns, 15 minutes per turn." Walk away. A decision notification
 (webhook or SMS, off until you set it up) tells you when it needs you.
- **Check in at a glance.** The web console works down to phone width. It listens
 on loopback only, so reaching it from another device takes your own tunnel. The
 relay deliberately doesn't provide one.
- **An audit trail of agent work.** Every message and decision is a durable,
 hash-chained record that you can replay with `relay thread` or rebuild from disk.

**Ideas the design leaves room for** (see the roadmap):

- **One manager, many workers.** A leader hands pieces of a migration to several
 followers, one per module, with review between them.
- **Other agents.** The adapter contract in docs/PROTOCOL.md
 isn't specific to Claude or Codex. Any coding agent that confirms receipt of a
 turn and reports completion could plug in.
- **Saved playbooks.** Reusable goal, scope, check and budget templates, such as
 "review this branch", "write the docs and fact-check them" or "upgrade this
 dependency".
- **Custom manager styles.** Write your own personality next to Reviewer, Planner
 and Pair programmer, as a plain text file.
- **A testbed for agent-to-agent protocols.** The bus is a small, durable,
 inspectable message layer. You can use it to study how agents hand work to each
 other, where loops stall, and when humans need to step in.
- **Evaluation runs.** Pit model pairings against the same task with the same
 budget, and compare the recorded threads.
- **Cost and budget insights.** Track tokens and time per team, not just turns.

## How it works, briefly

```text
   you ──start / pause / answer──┐
                                 ▼
 ┌──────────────┐  handoff  ┌────────────┐  handoff  ┌──────────────┐
 │ leader       │ ◀──────── │ controller │ ────────▶ │ follower     │
 │ (Codex)      │ ────────▶ │ (fg only)  │ ◀──────── │ (Claude)     │
 └──────────────┘  result   └─────┬──────┘  result   └──────────────┘
                                  │
                          durable bus on disk
```

- **Bus:** an on-disk store of messages and events.
- **Adapters:** they talk to each client. Every capability is explicit, and
 adapters never invent acknowledgments.
- **Controller:** it runs only in the foreground and keeps exactly one turn in
 flight. It enforces the budget and the timeout, and stops at every human
 boundary.

Each turn ends with a small `relay` block that tells the controller what to do
next. Commands, settings and exit codes are in the reference.
The specification is in docs/PROTOCOL.md.

## Status

| Part | State |
|---|---|
| Bus, controller, terminal console, web console | Working, covered by the test suite with pretend clients |
| Discovery of running Claude Code and Codex sessions | Working, read-only, on macOS |
| Codex and Claude Code driving each other (sessions the relay starts) | **Verified live**: Codex 0.163.0 led Claude Code 2.1.310, 2026-10-25 |
| Attaching to an open Codex session, handing an existing session over | Built, not yet verified live. Off unless you opt in. |
| Driving a Claude Code session while it's open in a terminal | Not possible. Open sessions are handed over (closed and resumed) instead. |

What's needed to get from prototype to dependable is in the roadmap.
The details on each client are in
integration feasibility.

## Documentation

| Document | What it covers |
|---|---|
| Web console tour | Every screen of `relay serve`, with screenshots |
| Reference | Install, consoles, CLI, configuration, guarantees and limits |
| Walkthrough | A recorded two-terminal run |
| Protocol | The specification: root layout, envelopes, state machines, adapter contract |
| Integration feasibility | What real Claude Code and Codex surfaces can and can't do |
| Context reporting | How session titles and summaries are found |
| Roadmap | What's left, and what could come next |
| Changelog | Release notes |

## Contributing

This is a prototype, and ideas, experiments and pull requests are welcome. See
CONTRIBUTING.md for setup and for the stricter rules for changes
to the real-client adapters. Report security issues privately through
SECURITY.md. This project follows the
Contributor Covenant.

## License

MIT

# andrsrxn/icons

## 关联链接

- https://github.com/saranyan/agent-relay.git

## 导航

- 项目页：[[10-项目/github.com_77afeea0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
