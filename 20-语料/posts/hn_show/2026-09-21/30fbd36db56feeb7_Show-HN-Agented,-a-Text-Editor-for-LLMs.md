---
type: "corpus"
item_id: "30fbd36db56feeb7"
title: "Show HN: Agented, a Text Editor for LLMs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47948090"
project_url: "https://github.com/frane/agented"
author: "frb"
published_at: "2026-04-29T13:24:46Z"
captured_at: "2026-09-21T02:52:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_frb
  - story_47948090
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Agented, a Text Editor for LLMs

> [!info] 一句话导读
> License: Apache License 2.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47948090>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：frb　|　发布：2026-04-29T13:24:46Z
> 项目链接：<https://github.com/frane/agented>
> 采集：2026-09-21T02:52:38+08:00　|　id：`30fbd36db56feeb7`

## 正文

# frane/agented

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 0
- License: Apache License 2.0
- Default branch: master
- Created: 2026-04-29T09:43:08Z

## Languages

- Go
- Makefile
- Shell

## Topics

- agent-skill
- agent-skills
- cli
- editor
- gemini-cli-extension
- golang
- llm-agent
- llm-tools
- text-editor

## Top Contributors

- frane (68 contributions)

---

## README

 agented ( ae)

 A text editor for LLMs, not humans.

Take ed, the line editor that nobody has voluntarily used since about 1975, and rebuild it for an environment where the typing user is a language model. Short verbs, line addresses, no modes, no TUI. What an editor optimises for changes when the user is the model: round trips per task, tokens per command, an editing buffer with a long memory, and an undo tree that remembers the branches the agent abandoned, because that's often where the interesting work was.

## What users say...

> ⏺ ae remembers what my last session was doing, which is more than I can say for me.

*— Claude Code*

> • ae feels slower to start than plain file edits, but once a change spans
> multiple steps, the state tokens, history, and undo tree make the work feel
> much less brittle.

*— Codex CLI*

## Features

- **Fewer round trips.** Read-before-Edit is unnecessary; on conflict the response carries the new content so you reconcile in one call instead of pre-reading every time.
- **Branching undo.** Walked-back work stays addressable instead of being thrown away when you pick a different path.
- **Three-way merge.** Concurrent agents get a structured conflict response instead of a silent overwrite.
- **Atomic batches.** Multi-file refactors run all-or-nothing instead of leaving half-applied state on failure.
- **Cross-file moves and regex replace as primitives.** Operations the built-in tools can't express cleanly become single calls.
- **Drift detection.** External edits to an open file are folded into the tree instead of being clobbered by the next write.
- **Inline diagnostics.** Type errors and lint findings surface on save, not at the next build many edits later.
- **Cross-session memory.** Per-file notes persist between sessions and surface inline on the next open.
- **Audit log.** Every operation recorded with actor and timestamp, so two agents in one workspace can't argue about who moved the head.

## Install

Homebrew (macOS, Linux):

```sh
brew tap frane/tap
brew install agented
```

curl (any platform):

```sh
curl -sSL https://raw.githubusercontent.com/frane/agented/master/install.sh | sh
```

From source: `go install github.com/frane/agented/cmd/ae@latest`, or clone and `make install`. Pure Go, no cgo, single static binary, Apache 2.0.

## Plugin distribution

Once `ae` is on PATH, agented also ships as a plugin / extension across the major agent CLIs. The `ae` binary itself is the prereq for all three; the plugin layer just registers the skill content and the MCP server entry.

**Claude Code**:

```sh
/plugin marketplace add frane/agented
/plugin install agented@frane-agented
```

**Codex CLI**: until OpenAI's official directory opens, add a manual entry to `~/.agents/plugins/marketplace.json` pointing at this repo with `source.path: "./plugin"`.

**Gemini CLI**:

```sh
gemini extensions install https://github.com/frane/agented
```

The Gemini gallery (https://geminicli.com/extensions/) crawls daily and indexes via the `gemini-cli-extension` topic on this repo.

## Getting started

```sh
ae skill install
```

That writes a `SKILL.md` into every detected agent's skills directory: Claude, Codex, Cursor, Gemini, OpenClaw, and the canonical `~/.agents/`. The skill teaches the agent how to drive ae.

You still need to tell the agent to use it. Even with the skill installed, agents fall back to built-in Read and Edit out of habit, so something like "use ae for all file edits" in your system prompt or your first message is what keeps them on it.

Once the agent is on ae, the shape that justifies the editor is recovery. The agent makes thirty edits over an hour, you walk away, come back to find it went off the rails around edit 18, but edits 19 through 23 are still useful:

```sh
ae br foo.go                             # see the leaves, current head is the bad one
ae head foo.go --edit 23                 # jump back to the last good state
ae v foo.go                              # confirm what's there
ae s foo.go -r 40:42 -w "..." -x <token> # continue forward, creates a sibling branch
```

With linear undo this scenario is "rollback the entire batch or live with the bad version." With the tree it's a `head --edit` and a `view`.

## Skill and MCP

`ae skill install` writes the SKILL.md into every detected agent. `ae serve` exposes the same verbs over MCP for agents that don't have shell access. Plugin-distribution channels (Claude Code marketplace, Codex CLI plugin, Gemini extension above) bundle both. Each surface has its own page: skill, MCP.

## Performance

A single open-and-replace on a 100-line file is around 9 ms wall time including the auto-save fsync. Fifty sequential replaces is around 325 ms. The full numbers are in test/benchmark/results.md, regenerated by `make bench`.

## Docs

- Concepts: the design choices and the state model
- Usage: full session walkthroughs
- Skill: what `ae skill install` does
- Permissions: editor-harness allow-rules
- Configuration: what's tunable
- Tokens: why the output looks the way it does
- MCP: running the MCP server
- IDE: LSP-backed features
- Build: tests and benchmarks

## Contributing

Issues and PRs welcome. The thing I'd actually like feedback on is the agent-drift problem: even with the skill installed, LLMs occasionally fall back to the built-in Read and Edit tools mid-session, and the trick to making that stick is something the project doesn't have a clean answer for yet.

## License

Apache 2.0.

# chrisdiana/gistkeep

## 关联链接

- https://geminicli.com/extensions/
- https://raw.githubusercontent.com/frane/agented/master/install.sh

## 导航

- 项目页：[[10-项目/github.com_05767cf2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
