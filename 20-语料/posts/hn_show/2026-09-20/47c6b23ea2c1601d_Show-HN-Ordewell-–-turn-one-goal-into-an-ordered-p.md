---
type: "corpus"
item_id: "47c6b23ea2c1601d"
title: "Show HN: Ordewell – turn one goal into an ordered plan of coding-agent tasks"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712276"
project_url: "https://github.com/ordewell/ordewell"
author: "ac-ciano"
published_at: "2026-09-15T13:31:37Z"
captured_at: "2026-09-20T14:58:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_ac-ciano
  - story_49712276
  - show_hn
metrics: {"points": 54, "comments": 34, "engagement_velocity": 54}
comments_count: 29
comments_total: 34
discovered_via: "hn:show_hn:90d"
---

# Show HN: Ordewell – turn one goal into an ordered plan of coding-agent tasks

> [!info] 一句话导读
> Multi-agent task orchestration for coding agents. Turn one goal into an ordered plan of tasks — each with its own runner, model and mode — then execute and veri…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712276>
> 指标：点赞=54 · 评论=34 · engagement_velocity=54
> 作者：ac-ciano　|　发布：2026-09-15T13:31:37Z
> 项目链接：<https://github.com/ordewell/ordewell>
> 采集：2026-09-20T14:58:09+08:00　|　id：`47c6b23ea2c1601d`

## 正文

# ordewell/ordewell

Multi-agent task orchestration for coding agents. Turn one goal into an ordered plan of tasks — each with its own runner, model and mode — then execute and verify the results.

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- License: Other
- Default branch: main
- Created: 2026-07-31T15:20:40Z

## Languages

- CSS
- HTML
- JavaScript
- Shell
- TypeScript

## Top Contributors

- ac-ciano (10 contributions)

---

## README

 Turn one goal into an ordered plan of coding-agent tasks — each with its own runner, model and mode — then execute and verify it.

 Website ·
 Docs

---

## What this is

- **A plan you can rewrite before a token is spent.** The plan is a typed artifact, not an agent's internal state: every task carries a runner, model, thinking effort and mode, and you can change any of them, add and remove tasks, and rewire dependencies — without losing completed work or round-tripping the AI.
- **The right model per task, chosen in the open.** The planner makes one portfolio decision across the whole plan — a security refactor and a README update do not deserve the same model — and shows you every assignment before anything runs (why a separate planner?).
- **Verdicts from evidence, not opinion.** A task completes only when its unique completion marker appears in the runner's output; exit code is retained as diagnostic evidence. The model is never the tie-breaker. Stuck tasks can be advanced with *Mark complete*, and a task marked done by mistake goes back with *Mark not done*.
- **A planner that talks back.** Planning is one continuous chat: it researches your repo read-only, asks when your goal is vague, and its final message *is* the plan (ADR-0002). Reads run in parallel; anything reaching outside the workspace asks once; commands that would write are refused outright (ADR-0008).
- **No extra API key required.** Claude Code, Codex, or OpenCode can *be* the planner, strictly read-only, on the subscription you already hold for the runners (ADR-0009).
- **Multi-runner by design.** Enable several and the planner assigns one per task. Claude Code, Codex and OpenCode ship built-in; anything else — Aider, your own CLI — is a plugin manifest, not a code change.

---

## Quick Start

Node.js ≥ 20 on macOS, Linux or Windows. The TUI also needs **tmux** — see
Platform support below.

```bash
npm install -g ordewell
ordewell                                       # the TUI — chat on the left, plan on the right
```

That's it. First run asks for a planner and a runner, set from inside
(`/planner`, `/runners`, `/key`) — no restart, no API key required up front.

`npx ordewell` works the same without a global install; the package also
ships scoped as `@ordewell/cli`.

For VS Code instead, install the extension — it carries its own core, so
there is nothing to install from npm:

```bash
code --install-extension ordewell.ordewell
```

Or search **Ordewell** in the Extensions view.

Building from source:
`git clone https://github.com/ordewell/ordewell.git && cd ordewell && npm install && npm run build && npm link -w packages/cli`
— see CONTRIBUTING.md.

### Scriptable / headless

Every slash command is also a subcommand — set the planner and runner by env
var to skip the TUI entirely.

**Already run Claude Code, Codex, or OpenCode?** No separate API key — it
runs on the subscription you already hold:

```bash
export AI_PROVIDER="claude-code"        # or codex, opencode
ordewell plan --goal "Add rate limiting to the public API" && ordewell run
```

Mutation always stays with the runners; the planner agent only explores and
reasons. Same toggles apply from a UI: `/planner`, `/model`,
`/planner-effort`, or the planner bar in VS Code.

**Prefer an API key?** Twenty-five providers are recognised via their own
`*_API_KEY` — OpenRouter, Anthropic, OpenAI, Gemini, xAI, Groq, DeepSeek,
Mistral, Together, Fireworks, Perplexity, Cerebras, DeepInfra, Cohere,
Novita, Kimi, Zhipu, Qwen, Doubao, Hunyuan, Baichuan, MiniMax, Yi, StepFun
and SiliconFlow. Run `ordewell key` for variable names, or point
`OPENAI_COMPATIBLE_BASE_URL` at anything else, including a local model
server.

```bash
export OPENROUTER_API_KEY="sk-or-..."
ordewell plan --goal "Add rate limiting to the public API" && ordewell run
```

---

## Three surfaces, one core

### VS Code

A streaming timeline: live thinking, each research step with its outcome, and task cards you expand for the runner's own output. Retarget a task's runner and its model and mode re-derive in place. The whole loop is below, under **The VS Code loop, end to end**.

### Terminal UI

Everything the extension does, over SSH. `tab` swaps chat and plan pane; single keys drive the plan (`f` start, `E` run all, `m` toggle done, `R` runner, `o` model). `/help` lists the rest.

### CLI

```console
$ ordewell plan --goal "Add rate limiting to the public API"

Generating plan for: "Add rate limiting to the public API"...
✓ list_dir src → D middleware F router.ts F auth.ts
✓ grep X-RateLimit → no matches in 6 files

Question: should limits apply per API key, or per client IP?
My recommendation: per key — auth() already threads the key through req.ctx.
> per key, with an IP fallback for anonymous routes

Plan: 4 tasks (3 AI, 1 Manual) — claude-code, opencode
Session: session-1751600000000

   1. [ AI] Add a token-bucket limiter in src/middleware/rateLimit.ts (Claude Sonnet 4.5 · Claude Code)
   2. [ AI] Wire the limiter into route registration (Claude Haiku 4.5 · Claude Code)
   3. [ AI] Return RFC 6585 429s with Retry-After (DeepSeek V4 Flash · Opencode)
   4. [MAN] Document the limit headers in the OpenAPI spec

  [MAN] = manual step — run `ordewell tui` to work through it

  Run 'ordewell run' to execute, 'ordewell status' to inspect, or 'ordewell tui' for the full UI.

$ ordewell run
Executing plan...
  ✓ #a1b2 completed — PASS: Verified: completion marker detected in agent output. Task c
  ⟳ #c3d4 in_progress
[2/Wire the limiter into route registration] Started: claude-code / claude-haiku-4-5

Done. 4 completed, 0 failed, 0 blocked.
```

Every slash command is also an `ordewell` subcommand, so nothing is UI-only and headless automation reaches everything a human can.

---

## How it works

1. **Describe a goal** in plain prose.
2. **The planner researches** your workspace read-only and interleaves questions with research in one persistent conversation (ADR-0008).
3. **A plan appears** — ordered tasks, each with a runner, model, thinking effort and mode. Edit anything inline, or reprompt to reshape the whole plan without losing completed work.
4. **Execution** spawns a real coding-agent session per AI task, respecting the dependency graph and handing each task its predecessors' results. Manual tasks become checklists.
5. **The VerdictEngine** completes a task only once its marker appears; an exit without one fails visibly. Sessions auto-save to `.ordewell/sessions/`.

---

 Usage examples — planning, editing, multi-runner, plugins

**Plan, edit, execute**

```bash
# The planner researches the repo and converses if the goal is underspecified
ordewell plan --goal "Migrate the config loader from JSON to TOML"

# Reassign before running — runner first, since it re-derives model, effort and mode
ordewell task-runner 2 opencode
ordewell task-deps 3 1,2

# Execute; independent tasks run in parallel (default: 3 concurrent sessions)
ordewell run

# Inspect any session later
ordewell status --session-id session-1751600000000
```

The surfaces differ only in how you name a target: the TUI opens a picker, the CLI takes an argument — and omitting the argument prints the same options the picker would have shown.

```bash
ordewell task-model 3            # lists the models that task's runner can spawn
ordewell task-model 3 sonnet     # picks one
```

**Configure without an editor**

```bash
ordewell planner claude-code     # plan on a coding agent's subscription — no API key
ordewell model set sonnet        # scoped to that agent's own catalog
ordewell planner-effort high     # a variant of the selected model
ordewell key set openrouter sk-… # stored in .env, never echoed back
ordewell runners codex off
```

Each pushes to the running server *before* writing `.env`, so the change lands on the next plan with no restart — and a refused connection cannot leave the file holding a setting the daemon never saw.

**Deep-interview planning with a PRD**

```bash
ordewell grill-me on   # planner interrogates your goal before outlining (min. 3 probing questions)
ordewell prd on        # planner previews, then writes a full PRD to .scratch/<slug>/PRD.md
ordewell tdd on        # tasks are augmented with red-green-refactor instructions

ordewell plan --goal "Real-time collaborative editing"
# → the planner grills you in chat, drafts the PRD, waits for your OK,
#   then commits the plan as its final message
```

**Multi-runner plans and custom runners**

```bash
# Pass --runner repeatedly to build a runner set; the planner assigns one per task
ordewell plan --goal "Refactor auth module" --runner claude-code --runner opencode

# Bring your own CLI agent via a plugin manifest
ordewell plugins create my-runner        # scaffolds manifest.json
ordewell plugins install github:user/repo
ordewell plugins list
```

**The other two front ends**

```bash
ordewell               # full-screen terminal UI — same as `ordewell tui`
ordewell web --daemon  # the local API server, in the background
```

`ordewell web` starts the HTTP + WebSocket API on `127.0.0.1:3742` that the CLI and TUI are clients of — every other command starts it for you on demand. It serves JSON, not a web page; there is no browser dashboard yet.

For VS Code, install the extension and open the Ordewell panel — see Quick Start.

| Area | Commands |
| --- | --- |
| Planning | type a goal, `/approve`, `/run`, `/stop` |
| Tasks | `/add-task`, `/remove-task`, `/complete`, `/uncomplete`, `/skip`, `/retry`, `/cancel`, `/force-start` |
| Skills | `/grill-me`, `/tdd`, `/prd`, `/review`, `/verify`, `/research-subagents` |
| Models | `/model`, `/key`, `/allowlist`, `/runners`, `/auto`, `/refresh` |
| Sessions | `/sessions`, `/new`, `/save`, `/load`, `/delete` — a loaded session is adopted by the server, so its plan stays executable |
| System | `/help`, `/mouse`, `/quit` |

API keys typed into `/key` are masked on screen and written to your `.env`.

Text is selectable and copyable with the mouse, as in any other program: Ordewell
does not capture the terminal's mouse. Scroll with `pgup`/`pgdn`. If you would
rather have wheel scrolling and can live without drag-to-select, `/mouse on`
swaps the trade (and remembers it via `ORDEWELL_TUI_MOUSE` in your `.env`).

A task's own terminal is a tmux window, where tmux does hold the mouse so the
wheel scrolls its scrollback. Selecting there still copies to your system
clipboard: drag to select and release to copy, or double/triple-click for a word
or a line. Install `wl-copy`, `xclip` or `xsel` on Linux if you have none of them
— without one, copying falls back to an OSC 52 escape that some terminals ignore.

 The VS Code loop, end to end — research, question, plan, execution, verdict

 Platform support — including the Windows notes

| Surface | Linux | macOS | Windows |
|---------|-------|-------|---------|
| VS Code extension | ✅ | ✅ | ✅ |
| API server | ✅ | ✅ | ✅ |
| CLI | ✅ | ✅ | ✅ |
| TUI | ✅ needs tmux | ✅ needs tmux | needs tmux — run it under WSL |

**The TUI requires tmux on every platform**, not only Windows — it is what backs
each task's live terminal. Install it from your package manager (`apt install
tmux`, `brew install tmux`) before running `ordewell`. Everything else runs
natively on Windows: the planner (including harness planners), task execution,
model discovery, and the read-only exploration envelope all work there.

Two notes for Windows. Install the agent CLIs with their **native installers** where one exists — an npm-installed `claude`/`codex`/`opencode` is a `.cmd` shim, which has to start through cmd.exe and inherits its 8191-character command-line limit; that is fine for task prompts but not for the harness planner's larger system prompt, and Ordewell will tell you so by name rather than silently truncating it. And keep **Git for Windows** installed: its POSIX shell is what the planner runs research commands in, so `ls`, `cat`, `grep` and friends behave the same as they do everywhere else. See ADR-0010.

Any install route is found, on PATH or not: the PowerShell one-liner installers (`irm https://claude.ai/install.ps1 | iex`, OpenCode's equivalent), npm, pnpm, Yarn, bun, Scoop, Chocolatey, WinGet, and Volta. If a runner is greyed out in the picker right after you installed it, restart the VS Code window — a GUI-launched extension host holds the PATH it started with.

 Configuration — the four settings that matter

| Option | Default | What it does |
| --- | --- | --- |
| One provider key (`OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, …) | — | The one required setting. Twenty-five providers are recognised, each from its own variable — `ordewell key` lists them — plus any OpenAI-compatible endpoint via `OPENAI_COMPATIBLE_BASE_URL`. The provider is auto-detected from whichever key is set (force with `AI_PROVIDER`). Not needed when `AI_PROVIDER` is `claude-code`, `codex`, or `opencode` — those plan with the CLI's own subscription. |
| `ORCHESTRATOR_MODEL` | `deepseek/deepseek-v4-flash` | The planner model — a budget model by default; it plans and researches but never writes code. Change via `ordewell model set ` or `/model`, which scope the choice to the planner backend's own catalog. With a coding-agent planner, it must be one of that agent's own model ids. |
| `ORDEWELL_PLANNER_EFFORT` | — | Thinking effort for a coding-agent planner, from the selected model's own variants (`low`, `high`, `adaptive`, …). Ignored by vendor planners, whose effort is baked into the model id. Change via `ordewell planner-effort ` or `/planner-effort`. |
| `ORDEWELL_MAX_PARALLEL` | `3` | Max concurrent AI task sessions (1–5). Independent tasks run in parallel; the dependency graph is always respected. |

Run `ordewell --help` for the full list of environment variables, or `ordewell setup` for the interactive wizard. VS Code users: everything is mirrored under `ordewell.*` settings.

 Architecture

```text
packages/
├── core/    Pure TypeScript, zero UI deps — Session, PlanStore, Planner,
│            TaskOrchestrator, VerdictEngine, ModelResolver, ModeResolver,
│            RunnerRegistry + manifest template engine
├── cli/     ordewell: tui, plan, run, status, stop, web, models, setup,
│            plugins, grill-me, prd, tdd — plus tui/, a pure state +
│            renderer core behind a thin raw-mode terminal driver
├── vscode/  Extension + webview: streaming planner timeline, task cards,
│            TTY capture via script(1)
└── web/     Hono HTTP + WebSocket server — the local daemon the CLI and
             TUI drive over 127.0.0.1 (session pool, headless execution)
```

The TUI's core is pure — a reducer returning `{ state, effects }` and a renderer returning one string per terminal row (ADR-0006).

Tasks default to each runner's autonomous mode (toggle with `/auto`), and the plan is the source of truth for what runs — modes are never silently rewritten at spawn (ADR-0001).

Every surface consumes one event union (`SessionMessage`) over one broadcast seam — the domain vocabulary lives in CONTEXT.md and design decisions in docs/adr/.

 Acknowledgements

The deep-interview planning workflows — `grill-me`, PRD drafting, TDD task augmentation, and review mode — are adapted from Matt Pocock's skills (MIT), rebuilt as prompt blocks inside Ordewell's planner and runner prompts. If you want those workflows in a plain coding-agent session rather than an orchestrated plan, his repo is the place to start.

---

## Contributing

Bug reports, feature requests and pull requests are welcome — start with CONTRIBUTING.md for the build order and the layout of the tree. Security issues go to SECURITY.md, not the public tracker.

New to the codebase? CONTEXT.md is the domain glossary and docs/adr/ records why things are the way they are.

## License

Licensed under the Apache License 2.0. The Ordewell name and logos are not covered by that licence — see NOTICE.

## 评论（29/34）

> **ramon156** · 2026-09-15T14:24:19.000Z　
> i would love a deterministic program that can confidently make plans for lower-cost models like deepseek. ofcourse the LLM part wont be deterministic, but its a lot easier to measure quality like this. you could argue an AGENTS.md is this, but from experience its not enough to make non-frontiers act have a high success rate.

---

> **Lalabadie** · 2026-09-15T15:09:12.000Z　
> I opened the page looking for a differenciator, but everything about the project is AI-written (including author replies in these comments).

---

> **sharathr** · 2026-09-15T16:27:50.000Z　
> have you tried https://github.com/highflame-ai/codeoid

---

> **ac-ciano** · 2026-09-15T14:35:17.000Z　
> Fair — AGENTS.md is prose the model has to re-interpret every session, and that reinterpretation is exactly where weaker models lose the thread. Here the plan is parsed and enforced as structured data: tasks with declared dependencies and one prompt each, so the per-step job is smaller and the plan isn't up for renegotiation. Nothing in that needs a frontier model
> I just haven't benchmarked it against deepseek-class runners, and the runner is pluggable if you want to be the one who does.

---

> **formvoltron** · 2026-09-15T14:52:57.000Z　
> What sort of determinism do you have in mind?

---

> **hedgehog** · 2026-09-15T15:13:58.000Z　
> There are a lot of ways to slice the problem of getting the agents to complete a goal without getting lost, and the right solutions are somewhat problem-specific. For the projects I've done 35B Qwen is about the smallest that seems to make useful progress in a general purpose harness while 4B Qwen is workable with a task-specific harness. At the lower end the plan has to be traditional search/planner techniques in code not something the model has any control over, of course that limits the kinds of problems that fit. The high end coding models are perfectly capable of making a functional 1-off harness for those jobs so it ends up not being that bad to implement.

---

> **jedbrooke** · 2026-09-15T15:36:25.000Z　
> I’ve had success with writing eg shell scripts that have a deterministic scaffold for the thing I’m actually trying to do, then call off to the agent for only the things that actually need it. For example I was trying to find a race condition flaky bug in my code, so the shell for loop ran the build N times, and called out to the agent to analyze the build logs if the tests failed, then the shell would ping me on slack when it was done, so the whole thing could run in the background.I’ve been thinking more about how this deterministic + agents style could work, it’s kinda like the analogy of factories in the 1800s going from the central shaft to electric motors on each desk (where the central shaft in this case is a chat window, and the motor on a desk is calling the llm api from wherever you want just like a normal api call)Of course, maybe in a few months the agents would just be reliable enough to do the shell part on their own too, but we’ll just have to wait and see

---

> **jonaustin** · 2026-09-15T16:00:14.000Z　
> I've been working on a pi extension to do this, after frustration with getting the best current local models to stay on track, and just to deal with their relative slowness; gist is that it uses pi hooks to keep the model deterministically on track and beads-rust issue tracking tool to keep everything organized.A SOTA model writes the initial prompt, and creates the beads issues; then a continuous iteration of plan(local) -> review (sota) -> implement(local) -> review (sota). Until the sota reviewer model is happy with the implementation.And can mostly just let-it-run; e.g. overnight since local models with mac unified memory are slow.Still early days, but have had reasonably good success with a Defender (1981) clone and now I'm having it work on a Prince of Persia clone (both Go/ebiten).Note: I think this is only possible now because Qwen3.8-Flash-Next and 27b are incredibly good models.- https://github.com/Dicklesworthstone/beads_rust

---

> **leeuw01** · 2026-09-15T16:37:42.000Z　
> Have you looked at AWS's AI-DLC setup?https://github.com/awslabs/aidlc-workflows

---

> **popularonion** · 2026-09-15T16:58:02.000Z　
> I just can’t get excited about any of these meta-frameworks.Doesn’t everyone get by now that any advance just gets rolled in to Claude and Codex a few months later, then the downstream competitors a few months after that?

---

> **dominotw** · 2026-09-15T15:11:37.000Z　
> so why did it get upvotes and a place on coveted frontpage?

---

> **ac-ciano** · 2026-09-15T15:13:41.000Z　
> Fair, and I won't pretend otherwise. I heavily used AI to help write the docs and code. The thing is though... I designed it and I stand behind it.

---

> **ac-ciano** · 2026-09-15T15:17:17.000Z　
> To me that's not the embarrassing part... unmaintainable would be. Using AI for coding and writing doc is standard practice now, not using it would be insane.

---

> **ac-ciano** · 2026-09-15T16:34:06.000Z　
> nope but I will check it out, thanks

---

> **ac-ciano** · 2026-09-15T15:22:13.000Z　
> Yeah it's exactly what I've seen as well. Ordewell is close to your high end case: a frontier model builds the plan once, then it's fixed, the executing model can't reinterpret it.
> Won't get you to 4B, but should help a small model that only has to execute, not plan and execute at once.

---

> **ac-ciano** · 2026-09-15T15:51:51.000Z　
> I like your analogy. The main problem though is context and keeping it clean as much as possible as long a parallelization. This is what drove to build this tool: having control of everything that the LLMs will do, controlling all with one main planner that orchestrates the rest. This way we can have cheaper LLMs with a short context window used (less intelligence degradation) while still obtaining the same objective.
> And again, you can have a clear picture of everything structured as tasks.
> until we can get to rely on huge swarms of agents (tasks) being directed on the planner alone I don't see how we can get a better framework.

---

> **ac-ciano** · 2026-09-15T16:41:09.000Z　
> very interesting, the concept is the same. I see they flagged Opus as the suggested planner, which makes a lot of sense.
> Thanks

---

> **ac-ciano** · 2026-09-15T17:39:30.000Z　
> indeed, but I also value the freedom of using whichever provider I want and not get locked into Claude Code alone for instance. I want to use both Opus, DeepSeek and GPT 6 at the same time, not just the 2/3 models Anthropic offers.
> What I am trying to build is something that gives you absolute control, agnostic of the subscription/API you will use.

---

> **scandox** · 2026-09-15T15:54:46.000Z　
> But why write these comments with AI?

---

> **kouteiheika** · 2026-09-15T17:02:52.000Z　
> FWIW, replying to people with AI generated replies is (at least to me) extremely disrespectful. Please don't do it without consent from the other party. If you expect someone (who isn't a bot) to make the effort to read what you wrote then please make the effort to write it yourself.

---

> **hedgehog** · 2026-09-15T15:37:13.000Z　
> Have you quantified the performance on any particular benchmark?

---

> **jLaForest** · 2026-09-15T18:23:22.000Z　
> Btw you can configure Claude code to use any provider or model you want

---

> **wek** · 2026-09-17T13:21:48.000Z　
> I agree with this. Why get locked in at the harness layer. I want my workspace to be independent of my coding agents and models so I can use multiple and switch as I wish

---

> **BarryMilo** · 2026-09-15T16:18:33.000Z　
> Complete brainrot lol

---

> **ac-ciano** · 2026-09-16T09:45:08.000Z　
> I replied to everyone on my own.

---

> **ac-ciano** · 2026-09-16T09:43:42.000Z　
> I agree with you, I did not reply to anybody with an LLM. I employed AI for building

---

> **ac-ciano** · 2026-09-15T15:44:57.000Z　
> I thought about it but where the tool shines are large undefined tasks, which are complex to quantify and test (not as easy as implementing a simple bug fix that you can test directly). Even if I were to find such test dataset it would probably require a lot of money to reach statistically significant results.
> Either way, the framework is inspired a lot from Matt Pocock, and is pretty much established.

---

> **ac-ciano** · 2026-09-16T09:27:37.000Z　
> Sure, as you could on OpenCode/PI, but most of us use subscriptions for which you are forced to use the relative UI

---

> **hedgehog** · 2026-09-16T00:44:50.000Z　
> In my experience the details matter a lot. Too rigid a plan and the agents get stuck and then thrash endlessly on work they manufacture for themselves, too little they get lost, the integration strategy is in part forced by cost (e.g. using Claude Code subscription discounts by using their TUI), etc.

## 关联链接

- https://claude.ai/install.ps1
- https://github.com/ordewell/ordewell.git

## 导航

- 项目页：[[10-项目/github.com_ce5601e5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
