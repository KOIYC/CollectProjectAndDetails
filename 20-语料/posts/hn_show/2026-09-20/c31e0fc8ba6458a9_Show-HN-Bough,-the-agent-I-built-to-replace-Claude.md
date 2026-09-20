---
type: "corpus"
item_id: "c31e0fc8ba6458a9"
title: "Show HN: Bough, the agent I built to replace Claude Code at work"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49711939"
project_url: "https://github.com/andreylukin/bough"
author: "alukin"
published_at: "2026-09-15T13:04:27Z"
captured_at: "2026-09-20T14:06:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_alukin
  - story_49711939
  - show_hn
metrics: {"points": 10, "comments": 5, "engagement_velocity": 10}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:90d"
---

# Show HN: Bough, the agent I built to replace Claude Code at work

> [!info] 一句话导读
> A coding agent that acts by writing programs: one JavaScript program per round — loops, branching, composition — run against your real checkout. Rust, terminal …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49711939>
> 指标：点赞=10 · 评论=5 · engagement_velocity=10
> 作者：alukin　|　发布：2026-09-15T13:04:27Z
> 项目链接：<https://github.com/andreylukin/bough>
> 采集：2026-09-20T14:06:38+08:00　|　id：`c31e0fc8ba6458a9`

## 正文

# andreylukin/bough

A coding agent that acts by writing programs: one JavaScript program per round — loops, branching, composition — run against your real checkout. Rust, terminal UI.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 7
- License: Apache License 2.0
- Default branch: main
- Created: 2026-06-18T13:42:59Z

## Languages

- JavaScript
- Lua
- Makefile
- Python
- Ruby
- Rust
- Shell

## Topics

- agent
- ai
- coding-agent
- developer-tools
- llm
- ratatui
- rust
- tui

## Top Contributors

- andreylukin (833 contributions)
- claude (41 contributions)

---

## README

 bough

 A coding agent that acts by writing programs.
 One JavaScript program per round, with real loops and branching, run against your real checkout.

**bough** rhymes with *now*, not with *dough*: /baʊ/. It is the word for a branch of a tree, which
is what a conversation is here: you fork a turn and the old line goes on living as a branch.

Most harnesses let the model emit one tool call and wait. bough gives it a single tool that takes a
program: the model writes JavaScript with real control flow, and a harness executes it on your
machine. A headless server owns all state and execution; the terminal UI is a view over it.

bough is an alternative harness **design**, not a better coding agent. That distinction is the point
of the project, and this README tries not to blur it.

> [!WARNING]
> **There is no isolation boundary.** Programs run as you, with your full authority: filesystem,
> network, subprocesses, `npm:` imports. No sandbox, no egress proxy, no credential gating. Host
> functions are convenience and session integration, never a wall.
>
> This is a deliberate choice, not an unfinished one (spec §2): the harness edits
> your real files because reviewing `git diff` and pushing with your own git is the delivery
> mechanism. Run it only on a machine where you would be comfortable running the code it writes,
> because that is exactly what happens.

## The idea

- **One program per round.** The model's only action is `run_steps(code)`. Control flow lives in the
 program, not in a chain of round-trips.
- **In place.** The agent edits your own checkout. No copy, no overlay. The Changes rail is
 `git diff` against the sha the session started from; you deliver with `git commit` / `git push`.
- **History is a tree.** Fork any turn, compact a span onto a new branch, lift messages into a fresh
 root. Nothing is destructively rewritten; every operation produces a new branch.
- **The server is the system.** State, execution, and orchestration are server-side. A client can
 crash or detach without affecting a running turn.
- **Delegation is core.** Subagents and workflows are primary capabilities with real persistence,
 lifecycle control, and observability.

Here is a round. It is one program where another harness would spend five round-trips:

```js
// Which crates still pin the old ratatui, and do they still pass?
const pinned = (await bash("rg -l 'ratatui = \"0.29\"' crates", "repo:scan:ratatui"))
  .trim().split("\n").filter(Boolean);

const names = pinned.map(p => p.split("/")[1]);

// sh() runs them concurrently; a non-zero exit is data, not an exception.
const runs = await sh(names.map(n => ({
  cmd: `cargo test -p ${n} 2>&1 | tail -3`,
  tag: `cargo:test:${n}`,
})));

const broken = names.filter((_, i) => runs[i].code !== 0);
console.log(broken.length ? `failed: ${broken.join(", ")}` : "all green");
```

The loop, the fan-out and the branch are the model's own code. `console.log` is what streams to
you and what comes back as the round's result, so the program decides what is worth your context:
here, the names that failed rather than four test logs.

## Install

macOS or Linux. Builds from source, so the first run takes a few minutes.

```bash
brew tap andreylukin/bough https://github.com/andreylukin/bough
brew install bough
$EDITOR ~/.bough/env      # ANTHROPIC_API_KEY=…
bough start               # background service
bough                     # the TUI
```

Without Homebrew, the same install as a script. It clones into `~/bough` and builds there:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/andreylukin/bough/main/install.sh)"
```

**Models.** Four providers, and a model routes to one by the shape of its id alone:
`claude-opus-5` is Anthropic, `openai:gpt-5` is OpenAI's Responses API, `vendor/model` is
OpenRouter, `@cf/vendor/model` is Cloudflare Workers AI. OpenRouter is the wide door: if it
carries a model, bough can run a turn on it. Every provider's base URL is overridable, and the
OpenRouter path speaks `/v1/chat/completions`, so pointing `OPENROUTER_API_BASE` at Ollama,
vLLM, LM Studio or a gateway runs turns against that instead. The picker (`^o`) lists what your
keys actually reach rather than a compiled-in catalog, and any one key is enough to start.

Full instructions, keys, and updating: docs/install.md.

## Use it

Point a session at a repo and ask in plain language. bough writes a small program, runs it, and
answers. Folded reasoning, the code that ran, and live cost and context all sit in one view.
Unfold a step (`^e`) and you see the actual program and its output:

Everything that is not the conversation lives in one panel with nine tabs, each on a direct-jump
chord: the conversation tree (`^f`), changes (`^d`), workflows (`^w`), model (`^o`), MCP (`^p`),
skills (`^k`), hooks (`^x`), context (`⌥c`), theme (`^y`). Press `?` for the full keymap.

Review with `^d`: the Changes rail is `git diff` against the sha the session started from, per file
and revertable per path. You commit and push with your own git.

Rewind to any turn and send something else, and the old line survives as a branch.

→ docs/tui.md for panels and every chord · docs/cli.md for `exec`,
`acp`, `mcp`, `tags` and the rest

## What it can do

**Programs.** Eighteen host functions in scope, plus the full JS runtime. One editing idiom:
`view` gives numbered lines with a version tag, `patch` names lines instead of quoting them, so code
being edited never has to survive the model's own string escaping, and a stale edit reports a
conflict instead of clobbering. → docs/programs.md

**Delegation.** `agent` and `spawn` run subagents in the same checkout; a workflow is a detached
orchestration script with `parallel` / `pipeline` primitives, schema-validated results, and a
journal that replays unchanged work on rerun instead of paying for it twice.
→ docs/delegation.md

**Memory across sessions.** Every shell command carries tags naming what it is *for*, written at the
moment the command is written. A session opens primed with its project's own vocabulary, and
`bough tags` answers what was tried here, what worked, and what it printed.
→ docs/tags.md

**Extending it.** Skills, Lua hooks that can start work rather than only veto it, JavaScript
extensions bound into every program's scope, and MCP as a command rather than a verb. Reads the
`AGENTS.md`, `CLAUDE.md` and `.claude/skills` your other harnesses already wrote.
→ docs/extending.md

## Documentation

**docs/** is the map. Start at install.md, then
tui.md. how-it-works.md is the architecture in one page;
spec.md and specs/ are authoritative for behavior.

## What bough is not

These are decisions, not gaps:

- No confinement of any kind, and no credential gating.
- No acceptance gate. The model reports what it did and you verify it. The harness does not re-run a
 committed command or block a turn from finishing.
- No local inference in the turn loop; the cheap tier is a hosted model. The one exception is the
 embedding layer, which runs a small model inside SQLite.
- No embeddings over transcripts; cross-session transcript search is SQLite FTS. The two vector
 indexes cover the tagged command memory and note sections; both live in a separate
 `embeddings.db` that is derived state and can be deleted at any time.
- No per-agent worktrees or file leases. One shared checkout.
- No remote access, no auth layer, no web UI.

## Contributing

The most useful contributions sharpen or falsify the design. Read
CONTRIBUTING.md for setup, the bar for a pull request, and the
verification you are expected to have done.

Bugs and features go through the [issue templates][issues]; questions and design debates belong in
[Discussions][discussions]. Security issues go through SECURITY.md, never the
public tracker. Participation is governed by the Code of Conduct.

[issues]: https://github.com/andreylukin/bough/issues/new/choose
[discussions]: https://github.com/andreylukin/bough/discussions

## License

Apache License 2.0. By contributing you agree your contributions are licensed under it;
there is no CLA.

## 评论（5/5）

> **federalreserve2** · 2026-09-15T14:44:14.000Z　
> Love the idea! Have you run this against any benchmarks?What were your main UX issues with existing harnesses?

---

> **idk1236767** · 2026-09-15T15:19:47.000Z　
> Why not Pi and build around it?

---

> **alukin** · 2026-09-15T14:49:32.000Z　
> Thanks for the question!I ran this a couple of times against terminal bench with different models. I saw that some models aren't as good with code mode, but overall codemode doesn't slow them down. I was usually at about 70% on tbench 2.1 with Sol.The issue I have with existing harnesses is that they try to solve all issues for all people. I have workflows I use with fork, and a history tree view is another important thing I needed. One of the issues they don't solve for me is easy visibility and good recap (Claude is okay ish).Additionally, I loved Amp Codes UI/UX and was incredibly inspired by iy

---

> **alukin** · 2026-09-15T15:32:17.000Z　
> Pi built the extension system, I think DeepSeek perfected it. I took what I wanted from Pi, and made it more stable (I think)

---

> **idk1236767** · 2026-09-15T15:19:29.000Z　
> Lol how much money did you spend

## 关联链接

- https://github.com/andreylukin/bough/discussions
- https://github.com/andreylukin/bough/issues/new/choose
- https://raw.githubusercontent.com/andreylukin/bough/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_1b45f719]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
