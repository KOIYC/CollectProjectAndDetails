---
type: "corpus"
item_id: "21e56b5a91a97f59"
title: "Show HN: Hazzel – a tiny coding agent, Bring your own keys"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49706040"
project_url: "https://github.com/mukundzha/hazzel"
author: "mukundzha6"
published_at: "2026-09-15T00:15:56Z"
captured_at: "2026-09-20T09:37:33+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_mukundzha6
  - story_49706040
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Hazzel – a tiny coding agent, Bring your own keys

> [!info] 一句话导读
> Hazzel — a small terminal coding agent that works on your code

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49706040>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：mukundzha6　|　发布：2026-09-15T00:15:56Z
> 项目链接：<https://github.com/mukundzha/hazzel>
> 采集：2026-09-20T09:37:33+08:00　|　id：`21e56b5a91a97f59`

## 正文

# mukundzha/hazzel

Hazzel — a small terminal coding agent that works on your code

- Stars: 12
- Forks: 2
- Watchers: 12
- Open issues: 0
- License: GNU Affero General Public License v3.0
- Homepage: https://agenthazzel.vercel.app
- Default branch: main
- Created: 2026-09-07T10:19:08Z

## Languages

- CSS
- HTML
- JavaScript
- Python

## Topics

- ai-agent
- anthropic
- cli
- coding-agent
- developer-tools
- groq
- llm
- ollama
- openai
- python
- terminal

## Top Contributors

- mukundzha (97 contributions)
- ronaldsterners (1 contributions)

---

## README

 Hazzel

 A terminal coding agent you can actually read.
 Bring your own key. No subscription. Every change shown as a diff before it touches disk.

 If this saves you a hunt through someone's agent framework later, the ⭐ at the top of the page takes one click.

Hazzel demo

## The 30-second pitch

Every coding agent claims to be transparent. Most of them are 50k-line frameworks with a plugin system, a cloud dashboard, and a subscription.

Hazzel is ~10k lines of Python in a flat `src/hazzel/` layout you can trace end to end — `agent/core.py` is the whole loop, `tools/` is every action it can take, and `safety.py` is the entire undo system.

It does the things a coding agent is supposed to do — read your repo, edit files, run commands, work with git — and stops before every one of them to show you exactly what's about to happen.

```bash
pip install hazzel
cd your-project
hazzel
```

```text
❯ Fix the failing test in tests/test_agent.py

  ● read_file   tests/test_agent.py
  ● edit_file   src/hazzel/agent/core.py
  ● run_command pytest -q — passed
```

`/model`, pick a provider, paste a key — that's the whole setup.

Or export:

```text
OPENAI_API_KEY
ANTHROPIC_API_KEY
GROQ_API_KEY
MISTRAL_API_KEY
GEMINI_API_KEY
DEEPSEEK_API_KEY
OPENROUTER_API_KEY
```

and skip the prompt entirely.

Running local models through Ollama needs no key at all.

## Why it's built this way

Most agents ask you to trust a black box. Hazzel asks you to trust three specific, inspectable mechanisms instead:

* **Every write is a diff you approve, first.** File edits render as a unified diff before anything lands. Shell commands ask before they run — except a small allowlisted set of true read-onlys (`ls`, `cat`, `git status`), which skip the queue so exploration doesn't feel like a permission dialog.

* **Every write is checkpointed, automatically.** Before Hazzel touches a file, it snapshots the prior bytes to `~/.config/hazzel/undo/` — up to 200 events, 20 per file. `/undo` restores bytes that were saved before the edit happened.

* **Commands are sandboxed to your project root.** Destructive git commands such as `reset --hard` and `clean` are blocked outright. Raw `git commit` is steered into the `/commit` tool with its own diff preview and approval step. Push and pull run through the normal command-approval flow.

You can verify all three claims yourself in about 200 lines:

```text
src/hazzel/safety.py
src/hazzel/tools/run_command.py
```

## What it actually does

**Understands your repo**

Reads, searches, and lists your codebase. `@path` tags a file into context; `/init` walks the tree and drafts an `AGENTS.md` map so every future session starts oriented.

**Ships real changes**

Diff-preview-and-approve editing, `/undo` backed by real checkpoints, shell commands with timeouts, `!command` for a direct shell escape (`!cmd &` runs it in the background — `/jobs` polls and kills), `fetch ` to pull docs into context, and image attachment (`@screenshot.png`) for vision-capable models.

**Speaks fluent git**

`/status`, `/diff --staged`, `/commit` with an auto-drafted Conventional Commit message and diff preview, `/log` — reads run instantly with zero LLM round-trip.

Push and pull go through the standard approval flow.

**Extends through open standards, not lock-in**

A minimal MCP stdio client using only the standard library talks to any MCP server through `.hazzel/mcp.json`.

`SKILL.md` files load project- or user-level skills on demand.

Neither requires Hazzel-specific tooling to author.

**Shows you the bill**

Provider-reported tokens are parsed into real dollar figures and logged locally — not estimated.

```text
/usage today
/usage week
/usage month
/usage --by-model
/budget
```

A live `tokens · $` line is shown every turn.

**Stays out of your way between sessions**

Per-project sessions persist across restarts with `/session restore`.

Plan mode (`/plan on`) explores read-only and proposes a numbered plan before touching anything.

Think mode (`/think on`) turns on extended reasoning for hard edits when you're willing to pay the token cost.

**Works in a pipeline, not just a REPL**

```bash
hazzel -p "prompt"
```

Runs one turn and exits.

Pipe a diff in, get a summary out. Use `--output-format json` for scripts and real exit codes (`0`, `1`, `2`, `130`) for CI.

## Providers — bring your own key, no subscription

| Provider | Notes |
| ---------- | ------------------------------- |
| Groq | Default (`openai/gpt-oss-120b`) |
| OpenAI | |
| Anthropic | |
| Mistral | |
| Gemini | |
| DeepSeek | |
| OpenRouter | 100+ models through one key |
| Ollama | Fully local, no key needed |

Switch anytime with `/model`.

Nothing is metered by Hazzel — you pay your provider directly, or nothing at all if you're running local.

## Commands at a glance

| Group | Commands |
| ---------- | -------------------------------------------------------------------------------------- |
| Modes | `/model` · `/plan on\|off` · `/think on\|off` · `/goal [@objective]` |
| Git | `/status` · `/diff [--staged]` · `/commit` · `/log` |
| Cost | `/usage [today\|week\|month\|--by-model]` · `/budget` |
| Extend | `/mcp [server [tool]]` · `/skills [name]` · `/init` |
| Transcript | `/export` · `/copy` · `/retry` · `/jobs` · `/undo [n]` · `/session restore` · `/clear` |

Type `/` to filter live.

Use `@` to attach a file.

```text
/docs
```

prints the full guide without leaving the terminal.

## What it's honest about not being

v1.4.9, early-stage.

No autonomous PRs, no cloud dashboard, and no session synchronization across machines.

It doesn't replace your editor — it sits in the terminal next to it, and it stays small on purpose.

If you need a heavier, more automated agent, better options exist.

If you want to see exactly what's about to happen to your files before it happens, this is built for that.

## Support Hazzel

Hazzel is free and open-source.

If you find it useful, you can support its development and help keep it maintained, improved, and dependency-light.

 Every contribution helps fund continued development and maintenance.

## Contributing

Issues and pull requests are genuinely welcome.

`ROADMAP.md` tracks feature gaps against other terminal agents, and `AGENTS.md` — regenerate it with `/init` — contains the project rules:

* No new dependencies without asking.
* No public API changes without a CHANGELOG entry.
* Keep the implementation small and inspectable.

## License

AGPL-3.0-or-later.

See LICENSE.

---

 Small tools stay small because people who find them useful say so.
 If Hazzel is now sitting in your terminal next to your editor,
 a star
 is how the next person finds it too.

# vstorm-co/agenticos

## 关联链接

- https://agenthazzel.vercel.app

## 导航

- 项目页：[[10-项目/github.com_a940c1c8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
