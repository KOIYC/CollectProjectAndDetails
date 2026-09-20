---
type: "corpus"
item_id: "0a39c0de63e05f02"
title: "Show HN: DaiDocs, AI memory as a plain-text file format, not a service"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49715672"
project_url: "https://github.com/Kerneta/daidocs"
author: "Amin_Rigi"
published_at: "2026-09-15T17:18:06Z"
captured_at: "2026-09-20T14:05:58+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_Amin_Rigi
  - story_49715672
  - show_hn
metrics: {"points": 7, "comments": 1, "engagement_velocity": 7}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: DaiDocs, AI memory as a plain-text file format, not a service

> [!info] 一句话导读
> Open plain-text file format for AI memory. Your assistant's long-term memory as .dai files on your disk: readable by Claude, GPT, Gemini, Cursor, local models a…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49715672>
> 指标：点赞=7 · 评论=1 · engagement_velocity=7
> 作者：Amin_Rigi　|　发布：2026-09-15T17:18:06Z
> 项目链接：<https://github.com/Kerneta/daidocs>
> 采集：2026-09-20T14:05:58+08:00　|　id：`0a39c0de63e05f02`

## 正文

# Kerneta/daidocs

Open plain-text file format for AI memory. Your assistant's long-term memory as .dai files on your disk: readable by Claude, GPT, Gemini, Cursor, local models and grep (all LLM models work). MCP server + hooks for Claude Code, Claude Desktop, Cursor, Windsurf, Codex. 83% LongMemEval-S (GPT-4o), 92% (Claude Fable 5), 10x fewer tokens.

- Stars: 31
- Forks: 0
- Watchers: 31
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://daidocs.com
- Default branch: main
- Created: 2026-09-13T08:29:01Z

## Languages

- HTML
- JavaScript
- Python

## Topics

- agent-memory
- ai-agents
- ai-memory
- chatgpt
- claude
- claude-code
- context-engineering
- cursor
- file-format
- llm
- local-first
- long-term-memory
- longmemeval
- mcp
- mcp-server
- memory
- open-standard
- persistent-memory
- plain-text

## Top Contributors

- amin-rigi (2 contributions)

---

## README

 English ·
 简体中文

.dai

 An open plain-text format for AI memory (launched Sep 2026).
 Your assistant's memory becomes files on your disk that you can open, grep and keep.

 Second on the LongMemEval-S leaderboard among memory systems anyone can re-run, 22.40 points above the same model with no memory, reading 10x fewer tokens per question.
 Every number here ships with its per-question judge verdicts and a sha256 manifest.

 Quickstart ·
 The guide ·
 Benchmark ·
 The format ·
 Reproduce it

 Launch release V4.4n32, 12 September 2026. What is in it.

 If.dai is useful to you, a star helps other people find it.

 The whole product, in one loop. Install, build, remember, recall: one store, every model, about a tenth of the tokens. The recording uses invented data.
 ▶ For higher quality, watch the demo live in your browser

---

## Language independent, model independent

A `.dai` file is three plain-text zones: a YAML header, a fenced JSON block, and the text. No binary, no database, no SDK required to read it.

- **Any programming language.** The reference engine is Node. A reader in Python, Rust or Go is an afternoon's work, and the spec is normative, written so that two independent implementations agree.
- **Any model.** The store is written once by a cheap observer model and read by whichever model answers. The same store measured with five answering models: 78% to 92%. Change the model, keep the memory.
- **Any tool.** `grep`, `git log`, `diff`, your editor, a shell script. Memory that answers to ordinary tools.

Build a reader in another language and open a PR: that is the contribution that matters most.

---

**What is in this repository:** the Kerneta Engine V4.4n that reads and writes `.dai` files,
the MCP server that connects it to your assistants, and the complete evidence for every number
quoted below: the benchmark run, the judge's verdict on each of the 500 questions, and the
five-model comparison. Each evidence file is hashed in `MANIFEST.sha256`
so you can check that what is described is what was measured; how to do that is in
`docs/PROVENANCE.md`.

 Second on the leaderboard. One setup for every row: LongMemEval-S, GPT-4o answering, all 500 questions, micro-averaged, and only configurations somebody who does not work for the vendor could re-run. The bottom row is that same GPT-4o with no memory system, reading the whole history pasted into its context: 22.40 points below us. Every figure here carries a caveat and the caveat travels with it, in docs/RESULTS.md.

 Not in that table? Graphify, Hindsight, Mem0 and the others publish figures measured on a different answering model, a different denominator or a different benchmark, so they cannot be set beside a GPT-4o 500/500 row in either direction. Every one of them is at daidocs.com/results.html, with what its number actually measures and where ours sits against it.

 One memory layer, five answering models, 500 questions each. Retrieval identical for every row (proved by a byte-identical diagnostics file). Details and caveats in RESULTS-ACTORS.md.

---

## Why this exists

Every memory product on the market keeps your history inside its own service and hands it back
through its own API. `.dai` takes the opposite bet: **memory is a file format**, the way a
photo is a JPEG. Three plain-text zones per conversation, a small derived index beside them,
and any model, any tool, or `grep` can read it.

| | memory as a service | memory as a format (`.dai`) |
|---|---|---|
| where your history lives | their database | your disk, plain text |
| who can read it | their SDK | Claude, GPT, Gemini, Cursor, local models, `grep`, `git` |
| when the vendor disappears | so does the memory | the files stay readable in any editor |
| how you inspect a recall | logs, if any | open the file the answer cites |
| what a benchmark number means | one product's pipeline | one store, measured per answering model, so you can pick the model |

The store is built once by a cheap **observer** model and read by any **actor** model. Convert
with a good model, then answer with whatever is cheapest, fastest or local. Numbers below.

---

## Works with

One store, connected over MCP, read and written by the tools you already use. `node setup.js` detects and configures each of these and backs up what it touches; Install has the per-tool commands.

| assistants | editors and IDEs | CLI and any MCP client |
|---|---|---|
| Claude Desktop, Claude Code, any model over MCP | Cursor, Windsurf, Zed, Cline, Continue | Codex CLI, plus any MCP client via `--client generic --config ` |

**Any MCP-capable runtime, too.** The server is a plain stdio MCP server, so frameworks that speak MCP call `save_memory` and `recall_memory` with no adapter to write: the OpenAI Agents SDK, the Vercel AI SDK, LangGraph, LangChain, CrewAI and LlamaIndex all consume an MCP server as a tool source. Point them at `node mcp_server.mjs`.

**Bring your history.** Claude Code sessions on this machine convert automatically. From any other tool, export a folder of `.txt`, `.md` or `.jsonl` and run `node daidocs.js convert`. Native history import from more tools is on the roadmap.

---

## Install

Node 18 or newer.

```bash
npx daidocs setup
```

One command. It detects Claude Desktop, Claude Code, Cursor, Windsurf, Codex, Cline,
Continue and Zed, configures all of them, installs the session hooks, the reading
protocol and the `.dai` icon, and backs up every file it touches. On a Claude
subscription there is no API key and nothing to pay.

**Want the source and the benchmark artifacts too?** Clone it and run setup from there
instead:

```bash
git clone https://github.com/Kerneta/daidocs daidocs-app
cd daidocs-app
node setup.js
```

The clone is named `daidocs-app` on purpose. `git clone` would otherwise make a folder
called `daidocs`, and the default memory store is `DaiDocs`: on Windows and macOS those
are the same folder, so a clone made from your home directory would land on top of your
own memory. Setup refuses to run from inside the store if it ever happens.

### Python (pip)

Prefer Python? Read your `.dai` stores from code, and drive the engine from a
`daidocs` command:

```bash
pip install daidocs
```

```python
from daidocs import Store

store = Store("~/DaiDocs")          # your memory store
for entry in store.manifest():      # every document
    print(entry["id"], entry["title"])

doc = store.read(store.ids()[0])    # one document, fully parsed
print(doc["understanding"]["summary"])
print(store.search("deploy"))       # find documents by keyword
```

Two things in one install:

- **Reader (pure Python, no Node):** `from daidocs import Store` reads the
 manifest, any document, and the `facts` / `events` / `profile` indexes.
- **`daidocs` command:** drives the Node engine, so `daidocs setup` and
 `daidocs convert` behave like `npx daidocs`. This needs Node 18+; if Node is
 missing it says so and offers to install it. Full guide:
 `readers/python/`.

`setup.js` installs the dependencies on its first run and then configures everything.
`npm run setup` does the same thing, but `node setup.js` is the one to reach for on
Windows: PowerShell refuses to run npm at all until you change its execution policy,
and node is not affected by that. Each line above is its own command, because Windows
PowerShell 5.1 has no `&&`.

Setup asks nothing. It detects what you have and configures all of it: Claude Desktop,
Claude Code, the session hooks, Cursor, Windsurf, Codex, Cline, Continue, Zed, the reading
protocol and the `.dai` file icon. It backs up every file it touches.

```bash
node setup.js --status     what is on, and the command that changes each one
node setup.js --ask        choose each surface yourself instead
node setup.js --restore    put the machine back exactly as it was
```

The one thing it never does on its own is convert the history you already have, because
that can run for a while and, with an API key, it spends money. It is one command when
you want it, and it is worth wanting: see Bring what you already have.

**Another MCP client?** One command each, rather than a config to edit:
`node setup.js --client codex` (or `cursor`, `windsurf`, `cline`, `continue`, `zed`), and
`node setup.js --client generic --config ```bash
node daidocs.js convert
``````bash
node daidocs.js convert --source claude --project atlas-api --pick 1-5 --to ~/DaiDocs --yes
``````
~/DaiDocs/
├── 2026-07-12_deploy-debug.dai     one file per conversation, three zones
├── 2026-07-18_q3-planning.dai
├── _index/                         what retrieval reads: manifest, facts, events, profile
├── _unconverted/                   what is not converted yet, small, read by the next session
└── _raw/                           your originals, byte-exact, never deleted
``````console
$ grep -l "Casa do Rio" ~/DaiDocs/*.dai
/home/you/DaiDocs/chat_20260720_e0546121.dai

$ head -12 ~/DaiDocs/chat_20260720_e0546121.dai
---
daidocs: "4.4"
id: "chat_20260720_e0546121"
type: "chat"
title: "Valletta trip planning chat"
lang: "en"
source: {"app": "claude", "native_id": "chat_20260720_e0546121"}
span: null
messages: 3
class: {"category": "general", "priority": "normal", "actionable": false, "sensitivity": "public", "confidence": 0.9}
summary: "User booked a summer trip to Valletta staying at the Casa do Rio guesthouse."
tags: ["x.travel"]
``````bash
npm run dashboard
``````bash
npm run dashboard-live
``````bash
node tools/verify_router.mjs /path/to/longmemeval_s.json
```
 
 

Full tables, both recall definitions, and the zero-network-call proof are in
`experiments/recall-sweep/`.

---

## When it earns its place, and when it does not

**Below roughly 20k tokens of history there is not much to save.** You are asking
a few questions and the whole conversation still fits in the window, so the raw
text is what gets used and DaiDocs is not doing much for you. Past that point
the history stops fitting, and the `.dai` store is what keeps the answers
available. The background conversion runs either way, every 4,000 tokens, so by
the time you cross that line the store is already there.

**Agent traces are the one shape it does not handle well.** Tool calls, stack
traces and file dumps look nothing like conversation, and converting them today
produces poor stores. That is a real gap and it is being worked on.

**Want it run for you?** The engine here is the whole engine and always will be,
self-hosted and free under Apache-2.0. If you would rather not operate it, we
host it: conversion, storage and recall as a managed service, same format, same
files, exportable at any time. That is how the work here gets funded. See
daidocs.com.

---

## Choosing your model

**Setup asks you once, at install, and that choice then applies everywhere.**
Conversion, the hooks, the MCP server and the CLI all use it until you change it.

**On a Claude subscription, in Claude Code: use Opus.** It is what we recommend,
and on a subscription the conversion is written by the assistant already in the
conversation, so there is no API key and nothing extra to pay.

**With an API key: use `openai:gpt-4.1-mini`.** Low cost, high accuracy, and it
is the observer every published number in this repository was measured with.
`gemini:gemini-3.1-pro` is the other good choice.

**Conversion is cheap in tokens.** Converting a session costs roughly what the
session already occupies plus a question or two at that same size. It is not a
second pass over your whole history; it reads what is new, once.

**Go higher if you like, but do not go lower.** The observer's output is baked
into the file permanently, so every future answer is limited by what it captured
the first time. A model that captures 65% of what mattered instead of 96% does
not give you slightly worse recall later: it gives you a store that no longer
contains the answer. The five-model comparison above is the measured version of
that: the same store, the same questions, and a 14-point spread purely from who
is reading.

The answering model is the cheap decision and can change per question. The
observer is the one worth spending on, because you only get to run it once.

---

## Using it

Six tools over MCP: `save_memory`, `recall_memory`, `list_memories`, `read_memory`, `declare_project` and `brief_parent`. You never call them; you ask naturally:

- *"save this chat to memory"*
- *"what did we decide about the deploy pipeline?"*

With the Claude Code hooks installed, every session saves itself as you work, with nothing to remember.

**Reading a store efficiently is a separate step from connecting one**, and it is the step people
skip. Loading whole `.dai` files instead of the three zooms costs an order of magnitude more
tokens for no accuracy gain. `setup.js` installs the protocol into `~/.claude/CLAUDE.md` for you; the same rules
are in `prompts/READER-PROMPT.txt` to paste into any assistant.

```bash
node daidocs.js ingest ./my-chats ./my-store    # convert a folder
npm run check                                    # verify an install, no API key needed
```

| variable | default | what it does |
|---|---|---|
| `DAIDOCS_STORE` | `~/DaiDocs` | where the store lives |
| `DAIDOCS_OBSERVER` | the model you chose at install | overrides that choice for one run |
| `DAIDOCS_DISABLE` | unset | skip the auto-archive hook |
| `DAIDOCS_NO_PING` | unset | refuse the one-time opt-in install ping without being asked |

---

## Reproduce our numbers

You reproduce the number by running it, not by downloading our answer file. Three things, all
public: the **dataset** (LongMemEval-S), the **engine** (`lib/methods/daidocs-v44n`, in this repo),
and the **scorer** (the benchmark authors' own `evaluate_qa.py`). Protocol in
`docs/REPLICATION.md`.

Per-question outcomes are in `benchmark/` so you can find which questions differ
rather than comparing two totals. **If you cannot reproduce a number, that is the most valuable
issue you can open**, and we will say so publicly rather than quietly editing the page.

---

## Repo map

| path | what it is |
|---|---|
| `QUICKSTART.md` | five minutes, nothing assumed |
| `spec/DAIDOCS-STANDARD.md` | the `.dai` format specification |
| `docs/RESULTS.md` | the conditions, the disclosures, and every number once measured |
| `docs/REPLICATION.md` | how to reproduce them |
| `docs/READ-DAIDOCS.md` | the reading protocol, per surface |
| `docs/INTEGRATION.md` | using it with Claude Code: hooks, converting history, keyless saving |
| `prompts/` | the protocol as a paste-anywhere prompt |
| `daidocs.js` | the CLI: convert, pending, stores, backup, scrub, ingest, ask |
| `setup.js` | one-command install and configuration |
| `lib/methods/daidocs-v44n/` | the engine, in the configuration this repo ships |
| `mcp_server.mjs` | the MCP server |
| `session_archiver.mjs` | the Claude Code SessionEnd hook |
| `session_context.mjs` | the SessionStart hook: memory loads at the start of a session |
| `session_autosave.mjs` | the Stop hook: sessions save themselves, with no API key |
| `verify_surfaces.mjs` | `npm run verify`: every surface, free and offline |
| `keyless_check.mjs` | proves nothing needs an API key to run |
| `lock.js` | `npm run lock`: makes this folder read-only |
| `assets/` | the brand marks, the charts, the diagrams and the demo |
| `benchmark/run_longmemeval.mjs` | the benchmark adapter, so the run is checkable |
| `benchmark/` | per-question results |
| `RESULTS-SUMMARY.md` | the release run, gpt-4o, in one page |
| `RESULTS-ACTORS.md` | five answering models over the identical memory layer |
| `run-artifacts/` | answers, judge verdicts, diagnostics and the run manifest, per actor |
| `experiments/recall-sweep/` | recall@k, k = 1 to 15, retrieval only, zero API calls |
| `MANIFEST.sha256` | sha256 of every file as frozen; `docs/PROVENANCE.md` says how to verify |
| `docs/GAPS.md` | the honest list of what has not been done |
| `tools/verify_router.mjs` | prints the router from source and measures it |
| `tools/check_numbers.mjs` | fails CI if any published number drifts from the artifacts |
| `tools/make_charts.py` | regenerates the charts from the numbers |
| `tools/chart_theme.py` | the daidocs.com chart surface, ported to matplotlib |
| `tools/make_diagrams.py` | regenerates the explainer diagrams |
| `tools/dashboard/` | `npm run dashboard`: builds the memory map. A built page is never shipped |
| `docs/GUIDE.md` | every command, tool, script and folder type, in one page |
| `tools/make_badges.py` | the badges at the top, as local files rather than fetched |
| `CHANGELOG.md` | what changed, per release |
| `SECURITY.md` | how to report something, and what is in scope |
| `RUNBOOK.md` | the release run, step by step |

---

## Contributing

The format is the point, so the most useful contributions are the ones that put
it in more places.

**Integrations.** A store that only one assistant can read is not a format, it
is a database with extra steps. The MCP server covers Claude Desktop, Claude
Code, Cursor and Windsurf. Everything else is open: an extension for another
editor, a plugin for another agent framework, a loader for another runtime, an
adapter for an assistant that speaks something other than MCP. If you are
wiring one up and something in the format fights you, that is a bug in the
format and worth an issue. Two we want by name: an **OpenRouter** provider backend, one key and hundreds of models, which turns bring-your-own-model into a line of config and slots into `lib/providers/` beside `anthropic`, `openai` and `gemini` with the same small contract; and a **Hermes agent** integration, so someone running that stack can point it at a store and have memory work.

**A second implementation.** A reader or writer that is not this code. It is
deliberately small enough to write in an afternoon: UTF-8, a YAML header, a JSON
zone and text. Two independent implementations is the difference between a file
layout and a format.

**Improvements to the memory itself.** Better extraction, better retrieval,
better handling of the shapes that do not work yet. Agent traces are the obvious
one: tool calls and stack traces convert badly today and somebody solving that
would be solving it for everyone. Anything that makes recall more accurate, or
makes a store cheaper to read, is welcome.

**Bugs and rough edges.** Especially on macOS and Linux, which are audited but
much less used than Windows here. If something is confusing rather than broken,
that is still worth reporting: a feature nobody can find is a feature that does
not exist.

Small changes are welcome without asking first. For anything that changes the
format itself, open an issue before writing code, because that is the part other
people's work depends on staying still.

By contributing you agree your work is licensed under Apache-2.0, and you sign
off that you have the right to submit it (DCO).

---

## Counting installs, opt-in and off by default

DaiDocs is local-first, and the tool sends nothing on its own. There is exactly one
exception, a single install ping, and it is built to keep that promise rather than bend it:

- It is **asked once**, on the first interactive `setup`, and never again.
- The default is **no**: a bare Enter declines, and it never prompts on a non-interactive run.
- A yes sends **one** anonymous request: a random id, the version and a timestamp. Nothing
 that identifies you, your files or your memory.
- `DAIDOCS_NO_PING=1` refuses it outright, without being asked.
- The choice is recorded in `~/.daidocs/install.json`; delete that file to be asked again.

It exists so the project can count how many people install it. If you would rather it did
not exist at all, that one variable turns it off for good.

---

## Licence

The specification, the engine and the MCP server are **Apache-2.0**, including a patent grant.
Commercial use, modification and redistribution are all fine. There is no lagging free edition:
what is published here is what runs.

Built by Kerneta.

# AirmailAI - Fast, secure, and private BYOK LLM chat app

## 评论（1/1）

> **Amin_Rigi** · 2026-09-15T17:38:47.000Z　
> I'm Amin, and I've built DaiDocs which is a file format for portable AI memory.A .dai file is a UTF-8 text with three parts: A YAML header, structured JSON which contains what the model understands and the original text. The idea is that AI memory should be like a JPEG, an open format that models can read instead of something that is locked to the memory providers database/format.In claude code , sessions are auto converted into .dai files every 4000 tokens and the raw is saved throughout. The model can then read from the memory and only read what it needs into the window.Claude Desktop, Cursor, Zed, and Codex CLI can read the same store through MCP. Auto save is currently only on Claude Code.On the LongMemEval-S benchmark .dai scored 83% using GPT-40 ranking second and 92% using a stronger model (Fable 5).On the benchmark the model scored 83% compared to 60.6% when the content is just given to the llm, you are basically 22.4% worse off not using a memory system. The format also reduced the input tokens used per question in the benchmark to 10,065 instead of 103,601 (10.3x fewer tokens used).Another feature that I wanted it to have was to use my own subscription on claude for converting to the DaiDocs format and retrieving from it, which it now does.

## 关联链接

- https://daidocs.com

## 导航

- 项目页：[[10-项目/github.com_8236e849]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
