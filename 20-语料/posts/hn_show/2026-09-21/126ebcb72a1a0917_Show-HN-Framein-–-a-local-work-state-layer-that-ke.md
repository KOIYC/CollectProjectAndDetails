---
type: "corpus"
item_id: "126ebcb72a1a0917"
title: "Show HN: Framein – a local work-state layer that keeps AI agents in context"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731852"
project_url: "https://framein.dev/"
author: "BonPPa"
published_at: "2026-06-30T12:36:49Z"
captured_at: "2026-09-21T02:53:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_BonPPa
  - story_48731852
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Framein – a local work-state layer that keeps AI agents in context

> [!info] 一句话导读
> Local work frame for AI coding

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731852>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：BonPPa　|　发布：2026-06-30T12:36:49Z
> 项目链接：<https://framein.dev/>
> 采集：2026-09-21T02:53:08+08:00　|　id：`126ebcb72a1a0917`

## 正文

GitHub
 KO
Local work frame for AI coding
Keep one work frame across Claude, Codex, and Gemini.
Start with one agent, challenge it with another, switch when needed, and close the work with validation. Framein keeps a shared task contract, decision trail, risk state, validation results, and model-switch capsule beneath the agent harness you already use.
Read the README
 Install guide
 Open the Manual
pre-release v0.0.6
 249 tests
 zero runtime dependencies
 Node 22.5+
# Start in the agent you already use.
 $ framein start "add Google OAuth"
contract set : preserve email login
lead claude
# Ask a different model for a bounded objection.
 $ framein challenge "OAuth callback state in session" --run
reviewer codex
verdict challenge
required add nonce/state validation
lead accepts required change
# Switch when needed; close with validation.
 $ framein capsule gemini
next lead prepared from facts:
contract · diff · tests · decisions
$ framein ship
build ok · tests passed
risk high: auth/ touched
=> READY WITH HUMAN GATE
30-second demo
Challenge, verify, and hand off without losing context.
A payment-task walkthrough showing a task contract, independent model challenge, validation evidence, and a capsule another agent can continue from.
Watch or share on YouTube
Why this exists
Better prompts help. They do not keep the work intact.
Good PRDs, plans, ADRs, and skills help any model do better work. The pain starts when the lead model stalls, another model should challenge the plan, quota or model fit pushes you to switch, or the final answer still needs real validation.
Framein is not a new IDE or another agent harness. It keeps one local work frame under Claude Code, Codex, Gemini, Pi, OpenCode, and the skill workflows you already use.
If harnesses are the engine, Framein is the shared logbook the engines write to.
Developer note: why I built Framein
Stalled lead model One agent keeps circling the same plan or failure mode.
One-model blind spots Architecture, security, and test concerns need an outside model's view.
Reset on switch Changing model often means explaining the same intent, risk, and decisions again.
Unverified finish The last answer still needs build, tests, risk, and human gates before ship.
The loop
Start. Challenge. Switch. Validate.
1 Start
 framein start turns the request into a shared task contract before the implementation drifts.
2 Challenge
 framein challenge asks a different reviewer for a structured verdict, one lead response, and a decision brief.
3 Switch
 framein capsule prepares the next lead from local facts: contract, diff, validation, ADRs, and ledger.
4 Validate
 framein verify and ship close the loop with deterministic build/test checks and risk gates.
Familiar surface
Call it like a skill. Store it like project state.
Claude and Gemini slash commands /fr:* calls the same local engine from the agent session.
Codex project skills $fr-* exposes the same verbs without deprecated prompt files.
Existing skill packs and personas Keep your prompt framework. Framein supplies the shared contract, ledger, and gates underneath.
Terminal, CI, and MCP clients The CLI, JSON output, wrappers, and MCP server all read and write the same local work frame.
Start in a real repo
Install once. Keep the frame under your agents.
Install from npm, then initialize Framein inside a real project. In day-to-day use, agents can call the same work-frame verbs through /fr:* or $fr-* .
The npm path works across Windows, macOS, Linux, and WSL with Node 22.5+. Standalone executables are planned as an optional convenience path that bundles Node with Framein and avoids Windows npm shim friction.
npm install -g framein
framein --version
cd your-project
framein init
framein integrations install all --write
framein start "complete the smallest safe change"
# when another model should review or continue
framein challenge "review the plan before implementation" --run
framein capsule codex
framein verify
framein ship
FAQ
Not a harness. Not a token relay.
Is this another harness?
No. Claude Code, Codex, Gemini, Pi, and OpenCode remain the working surface. Framein keeps the work state in your repo underneath them.
Does it touch provider tokens?
No. Framein collects no credentials, proxies no model traffic, and pools no subscriptions. Provider auth stays with the official CLI.
Where does state live?
In your repo: a git-friendly JSON snapshot plus a local SQLite cache. Read the full FAQ .
Trust boundary
Local first. No credential relay.
Local work frame
Task contract, ADRs, memory, ledger, validation results, and write locks live in your repo. The SQLite store is a cache; the JSON snapshot is git-friendly.
No proxy layer
Framein does not collect provider credentials, pool subscriptions, relay MCP tools, or screen-scrape terminal I/O (TTY). It calls official CLIs locally when you ask it to.
by Frameout · MIT · GitHub · FAQ · frameout.co.kr · axc@frameout.co.kr

## 导航

- 项目页：[[10-项目/framein.dev_17b3def2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
