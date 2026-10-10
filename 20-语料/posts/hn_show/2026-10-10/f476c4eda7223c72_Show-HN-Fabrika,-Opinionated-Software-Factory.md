---
type: "corpus"
item_id: "f476c4eda7223c72"
title: "Show HN: Fabrika, Opinionated Software Factory"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50022852"
project_url: "https://tatiyants.com/fabrika"
author: "atatiyan"
published_at: "2026-10-09T16:25:22Z"
captured_at: "2026-10-10T10:11:21+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_atatiyan
  - story_50022852
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fabrika, Opinionated Software Factory

> [!info] 一句话导读
> how it works the packet as-built the write-up docs

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50022852>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：atatiyan　|　发布：2026-10-09T16:25:22Z
> 项目链接：<https://tatiyants.com/fabrika>
> 采集：2026-10-10T10:11:21+08:00　|　id：`f476c4eda7223c72`

## 正文

Skip to content why
 vs coding harness
 crew
 repo ready
 spec review
 build
 feature review
 as-built
 skins
 routes
 fit
 start
 Clone
 how it works the packet as-built the write-up docs
github
 MIT · v0.1.0 · alpha tatiyants.com
 Meet Fabrika:
An opinionated software factory -
 Production-ready code, optimized for human decisions.
You define the feature and rule on what comes back. In between,
 model agents read the repository, write the spec that you review , build, test and repair as needed. What
 comes back is a review packet : contextualized diffs, plus
 evidence that the code does what you specified.
Clone on GitHub
How a run works
Read the write-up
Feature: Card Tags Project: Kanban Board
 repo ready
 intent
 questions
 spec review
build
review
feature review · you
Plan
 01 scout
 02 interrogator
 03 spec writer
Build
 04 architect
 05 workers
 06 integrator
Verify
 07 oracle
 08 checks
 09 breaker
Review
 10 attribution
 11 qa
 12 review
 13 arbiter
 14 repairers
 15 simplifier
 16 rapporteur
rework · repairers → workers · 2 passes
16 plan
 15 actual
 2 called for help
 passed
 called for help
 at work now
 nothing to do
Ships, with rulings
Tags on cards works as specified, but hold it for two rulings on
 what happens when the same tag is changed twice quickly.
Read how a packet is built
Why Fabrika
Built to deliver production-ready code
 Red and blue teams at every stage Builders and checkers on different model lineages. The spec, the plan and the code are each attacked before you see them. The crew
 Blind tests The oracle writes acceptance tests from the spec alone and never sees the implementation, so a pass means the contract was met. The build
 Sealed isolation Every agent and every check runs in its own container and worktree, with no route to your machine. Your checkout is never touched. Isolation
 Integrated supply chain management Every new dependency is screened with OSV for vulnerabilities and malicious packages, for license problems, and for releases only days old. Dependencies
 Built-in best-practice guidance It surveys how your repository is linted, typed, tested and guided, proposes what is missing, and writes the small fixes itself. Repo ready
Optimized for human decisions
 Visual spec review What the change touches, drawn as a diagram, and every criterion with how it will be verified and how hard it would be to undo. Spec review
 Context-enriched code review Code reached through the criterion that asked for it, beside the decisions and objections behind it, instead of a diff read from the top. Work map
 Recorded evidence of success The project’s own checks, blind tests, breaker probes and recordings of browser tests, all kept in the packet. Evidence
 Codebase discovery The as-built: an architecture, subsystems and capabilities, read from every file in the repository and kept current. As-built
Fabrika vs
 Your Favorite Coding Harness
A harness can do every step. A factory makes sure it
 does.
Your harness can spin up subagents, write tests and
 check its own work. Whether it will , and
 whether it will do it the same way twice, is up to
 the session.
Fabrika fixes the line instead. The flow is
 prescribed rather than configurable, which is what
 lets it guarantee red-teaming, blind tests and the
 project’s own checks on every feature, with plain code deciding what runs next .
Builders and checkers, on different model lineages.
Every station is an agent with one job and one
 prompt. Builders make things; checkers attack what was
 made. Fabrika wants the two teams on different model
 families: for example, build with Claude, check with
 GPT or Gemini.
Enlarge The crew: who stands at each station, what model they run on, and where the line loops back for repairs. Each agent sees what its job needs
A worker gets the whole branch and every tool the
 harness has. The oracle gets the requirements and
 none of the code.
Models matched to the job
A scout that reads and summarizes code can run on
 something like Haiku; the architect that plans the
 build needs something like Opus.
Prompts you can read and change
Each role is a Markdown prompt loaded at call time,
 tuned for its station and editable in the console.
Repo ready: Approve the
 checks
Point Fabrika at a repository and it surveys how
 the code is already checked, tested and guided:
 linters and type checkers, security and
 accessibility checks, unit, integration and
 user-facing tests, and agent guides like AGENTS.md and CLAUDE.md .
Every check it finds runs on an untouched
 checkout. Nothing is built until you accept them ,
 because every later feature is judged against
 that baseline. A check does not have to be green
 to be accepted: fix it, hold it at today’s
 number, or rule that it does not apply.
Dashboard Checks Tests Environment Suggestions
 01 / 05
Enlarge A project once it is repo ready: checks, tests, guides, environment and what the runs cost.
 Enlarge Structure checks, each the repository’s own command and the exit code it gave.
 Enlarge Tests at three levels. Fabrika runs a test twice to prove it leaves nothing behind.
 Enlarge The container every check and agent runs in. If the repo has none that works, Fabrika proposes one.
 Enlarge A gap that needs real code becomes a prompt you can hand to the coding agent of your choice. A missing small file, it writes and commits itself.
Spec review: Freeze the
 spec
Give it a prompt and a name. The scout
reads the codebase, and the interrogator
asks what reading could not settle. Then a spec writer drafts and a spec checker scrutinizes;
 only the disagreements they cannot settle reach
 you, as open questions.
Every spec follows one outline, so you know
 where to look:
Q Before the spec: questions
 01 In practice
 02 What it touches
 03 What it must do
 04 Where it stops
 05 What could be wrong
 06 How this was decided
Each criterion says how it will be verified, at
 which level, and how hard it would be to undo, from easily changed to cannot be undone
. The oracle writes its tests against exactly these.
 Nothing is built against a spec you have not frozen.
Before the spec: questions 01 / 05
Enlarge What it thinks you asked for, and the questions it needed answered first.
 Enlarge In practice: the world today, and once this ships.
 Enlarge What it touches: the screens, endpoints and tables, drawn and checked against what the workers actually build.
 Enlarge What it must do: the complete promise. Anything not here is out of scope.
 Enlarge Where it stops, and what could be wrong: the assumptions nobody has verified.
The build:
 watch,
 don’t steer.
The architect plans the units of work and a plan
 checker objects; you see the plan, at plan review , only if they cannot agree. After
 that there is no input mid-run.
Two lanes run blind to each other: workers build
 while the oracle writes tests from the spec. Running
 the checks, running the oracle’s tests and splitting
 repairs into non-overlapping units is done by plain
 code, not by an agent.
The line Call tree
 01 / 02
Enlarge The line as it ran: one lamp per station, the rework rail, and a timeline of every station.
 Enlarge The call tree: every agent’s turn, in the order it started, with model, cost and time.
The stations after the spec is frozen
 Station Team What it does
 worker
builder
 Writes the code and its unit tests. Several run in parallel, each in its own unit of the plan.
 integrator
builder
 Joins the workers’ units into one whole, and writes the tests that cover the seams between them.
 oracle
checker
 Writes acceptance tests from the spec alone, in parallel with the workers. It never sees the implementation.
 breaker
checker
 Attacks the result: boundaries, failure paths, concurrency, hostile input, criteria met in letter but not in spirit. It writes probes that fail to prove it.
 reviewer
checker
 Makes the strongest case against shipping: duplication, broken conventions, unearned abstractions.
 arbiter neither Rules on every finding: repair it, simplify it, send it back to the oracle, rule it out of scope, or escalate it to you. It cannot make a finding disappear.
 repairer
builder
 Makes the narrowest fix for what the arbiter sent back, in a loop bounded by rounds, budget and wall clock.
 simplifier
builder
 Simplifies code that is correct but more complicated than it needs to be. Everything is re-tested afterwards.
 rapporteur neither Assembles the review packet.
Feature review: Rule on the
 packet
What comes back is not a pull request. It is a review packet : the code, plus a structured
 argument that it does what was specified. Code is
 reached through the criterion that asked for it. You
 audit the argument and rule on a handful of
 decisions, instead of reading a diff from the top.
The outcome is either a branch you can merge, or
 another round of work.
Your calls Work map Evidence Dependencies Objections Repairs Blind spots
 The decisions the run could not settle on its own: findings that were escalated or could not be repaired, and anything you need to check by hand. Each one carries the arbiter’s reasoning and the evidence behind it, and you repair or dismiss it with a reason.
Enlarge Your calls: the three calls this run left for a person, a license blocker and two major findings, each with the arbiter’s reasoning and the evidence beside it. Every acceptance criterion drawn against the files written for it, sorted into four kinds. Novel code, the files with real choices in them, is split from boilerplate you can safely skip. When in doubt, a file is marked novel.
Work map A criterion A file
 01 / 03
Enlarge Work map: 18 criteria on the left, the files that answer them on the right, and the lines between.
 Enlarge One criterion, the code written for it, and the decisions a worker made along the way.
 Enlarge One file: the diff, the criteria it was written for, and the objections that name it.
Everything the run produced that you can check for yourself: the project’s own gates, the oracle’s blind acceptance tests, the breaker’s probes, and video recordings of browser tests. Each section ends by saying what it does not prove.
On screen Blind tests Breaker probes Project gates
 01 / 04
Enlarge Recordings of browser acceptance tests: the only evidence a person can judge without reading code.
 Enlarge Blind acceptance tests, written from the frozen spec before the code existed.
 Enlarge Breaker probes: tests written after reading the code, specifically to break it.
 Enlarge The project’s own gates, run in the feature’s container. No model is involved.
Every package the change brings in, checked against OSV for known vulnerabilities and malicious releases, against the project’s license rules, and for releases published only days ago. Anything flagged becomes a call for you.
Packages A blocker
 01 / 02
Enlarge Eight new packages and the four they bring with them; six need a ruling.
 Enlarge A blocker: a package under a license the project said it would not take.
Every objection raised about the change, grouped by what the repair loop did about it. An objection the loop fixed stays in the list with its outcome beside it: a packet that got shorter as the loop worked would look better and be worth less.
The details of each repair round. Repairers make the narrowest fix for what the arbiter sent them, and the loop is bounded by config: by default two rounds, a dollar budget and a wall-clock limit.
The places where the packet’s numbers look better than the evidence behind them, listed so you know which green numbers not to take at their word.
As-built:
 the codebase,
 read file by file.
You need a mental model of a system before you
 change it. A reader agent reads every file,
 plain code checks what it reported and joins it into
 a graph, and a cartographer names the groups.
 The result is an architecture, a set of subsystems
 and a map of capabilities, each with a stable
 three-letter id.
It runs whenever you ask, and afterwards reads only
 the files that changed since the last commit it
 processed.
Overview Architecture Capabilities
 01 / 03
Enlarge The as-built for a sample project: what it is, how it fits together, and what was read.
 Enlarge How it runs: who uses it, what runs where, and what it talks to outside the repo.
 Enlarge Capabilities against the subsystems that implement them, and how much of each is reached by a test.
Three skins,
 one board.
The console comes in default , day and night , switched from the masthead and
 remembered by your browser. A skin moves one ground
 onto the other rather than inverting the page: in
 day the board joins the floor, in night the floor
 joins the board.
default day night
 Pick a skin, or drag across the screen.
night day
 default The enamel board and its rail hang over a painted floor; the record is read on the floor.
Runs on the subscriptions you already have.
Fabrika drives Claude Code and Codex headlessly, on your Anthropic and
 OpenAI subscriptions. Anything
 OpenAI-compatible, OpenRouter or a model on your
 own machine, runs through the OpenHands
harness.
Subscriptions get throttled, so each team has a
 fallback agent the factory switches to when its
 main route says no. Every model name lives in
 one file, factory.yaml .
Accounts & harnesses Fallbacks
 01 / 02
Enlarge Accounts that serve the models and bill for them; harnesses that run the agents.
 Enlarge Fallback lanes, one per team, so builders and checkers still disagree from different families.
What it is for, and what it is not.
Built for
One person, or a small team, building
 features largely on their own.
Well-defined, self-contained features,
 designed before they reach the factory.
Running on your own machine, as a single
 user.
Not yet, or not at all
Team logins, coordinating work streams,
 cloud deployment.
Work that needs a lot of back and forth,
 like shaping a user experience or exploring
 a problem space. Use an interactive agent
 session for that.
Where it stands
Alpha, version 0.1.0, MIT licensed. It has not
 been used in anger yet, and it will have bugs.
 About twelve hundred tests each assert a
 property that makes it worth running: the
 invariants, isolation, the repair loop, what the
 console draws.
Put a factory beside your repo.
Python 3.11+ and git
Docker : every check and agent runs in a
 container, with no fallback to your machine
A model provider : an OpenRouter key, any
 OpenAI-compatible API, or a Claude Code or Codex
 subscription
Clone on GitHub
Read the design
quick start
Copy
$ git clone https://github.com/AlexTatiyants/fabrika.git $ cd fabrika $ python3 -m venv .venv && source .venv/bin/activate $ pip install -e ".[dev]" $ cp factory.example.yaml factory.yaml $ export OPENROUTER_API_KEY=sk-... $ uvicorn factory.server:app --port 8077
Then open 127.0.0.1:8077 . On a fresh machine it opens
 on setup: it checks Docker and the way out, connects
 accounts, builds each harness and staffs the crew.
A software factory, by Alex Tatiyants . MIT licensed.
 The write-up github.com/AlexTatiyants/fabrika tatiyants.com
Fit to screen f
Close esc

## 关联链接

- https://github.com/AlexTatiyants/fabrika.git

## 导航

- 项目页：[[10-项目/tatiyants.com_5982ece2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
