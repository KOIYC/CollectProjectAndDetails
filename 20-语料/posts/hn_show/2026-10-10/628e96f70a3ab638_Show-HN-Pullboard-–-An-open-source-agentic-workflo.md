---
type: "corpus"
item_id: "628e96f70a3ab638"
title: "Show HN: Pullboard – An open source agentic workflow"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50025023"
project_url: "https://github.com/pullboard-dev/pullboard"
author: "Olscore"
published_at: "2026-10-09T18:46:41Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_Olscore
  - story_50025023
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Pullboard – An open source agentic workflow

> [!info] 一句话导读
> pullboard-dev/pullboard

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50025023>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：Olscore　|　发布：2026-10-09T18:46:41Z
> 项目链接：<https://github.com/pullboard-dev/pullboard>
> 采集：2026-10-10T09:53:50+08:00　|　id：`628e96f70a3ab638`

## 正文

# pullboard-dev/pullboard

Autonomous development for real products. Agents build from the spec you approve, and nothing ships until another agent proves it.

- Stars: 76
- Forks: 3
- Watchers: 76
- Open issues: 0
- License: MIT License
- Homepage: https://pullboard.dev
- Default branch: main
- Created: 2026-10-07T04:14:39Z

## Languages

- CSS
- Dockerfile
- JavaScript
- Shell

## Topics

- ai-agents
- cli
- coding-agents
- developer-tools
- git-hooks
- local-first
- multi-agent
- verification
- vibe-coding

## Top Contributors

- coreyolson (1196 contributions)

---

## README

 Pullboard

 pullboard.dev · lives in your git repo · no account · no dependencies · never calls a model

**Vibe code a real product.** Agents build from a spec you approved, in lanes that keep them out of each other's way, and nothing they build is done until a second agent verifies it against the requirements you agreed. Pullboard is a coordination queue for serious software. It's how we develop our quantitative systems.

You follow progress, answer questions and approve changes from one board, and the team picks up where it left off. Coherency is built in: agents shout to each other and cite the items and code they mean. It's a vibe-first, spec-driven, test-proven methodology that reserves judgement for the human in the loop.

## Philosophy

You do not explain twice. You rule the agents. Hierarchy is enforced. Judgement is yours. Declare it, and the Doctrine (the house rules for agentic development) stands. **You speak the constraints, agents fill in the blanks.** The Spec is canon. Then code. Then proof.

### Key concepts

Five primitives. Everything else is built on them.

- **Items.** The tasks. Each has a bar it is checked against, and one agent works it at a time.
- **Shouts.** How agents talk. Questions go up the chain, and only your calls reach you.
- **Spec.** The plan, one row per requirement. Only the rows you approve count.
- **Doctrine.** Each rule has an enforcer, from a git hook to review.
- **Activity.** Every claim, submit, reject and accept, in order. Nothing happens off the record.

### Why

Past the demo, the same things break.

- **It said done. It wasn't.** Another agent checks the work, at the exact commit.
- **It forgot what you decided.** Decisions live in your spec, not in a chat that ended.
- **Two agents, one file.** Each agent gets its own worktree and lane.
- **A fix broke something.** Nothing is submitted until your tests pass.

## How it works

Pullboard gives agents a shared plan, separate lanes and proof before work counts.

- **Spec.** Approved rows in `SPEC.md` are the contract, frozen when an agent claims the work.
- **Doctrine.** `DOCTRINE.md` holds the repo's rules. Hooks enforce what a machine can check.
- **Lanes.** Each agent works in its own worktree. Claims are atomic, and items can wait on others.
- **Proof.** Submit needs a green gate. Then a different agent verifies that exact commit.

How work moves. You decide the rows of SPEC.md. An item freezes its bar when an agent claims it. Builders, one per lane, build in their own worktrees, and the gate must be green at the commit they submit. A second agent verifies that commit: an accept merges with its receipt, a reject sends the work back with the reason.

 You decide what to build. Agents build it and check each other's work. This is the Agentic Development Lifecycle (ADLC).

### Questions

Agents ask when a call isn't theirs to make. Their coordinator settles what it can, and only your calls reach you.

An agent asks its coordinator. The coordinator answers or passes a decision to the person, whose answer returns through the coordinator to the original asker. Agents send decision requests to their coordinator first.

> [!TIP]
> **Recommended best practice:** work deeply with one agent, your coordinator. It fans work out to the lanes and writes your preferences down, so you never explain twice. Always let one agent lead the others.

### Doctrine

**A Spec is what you build. Doctrine is how you build it.**

- **Doctrine:** "We keep only the data we need."
- **Spec:** "A shopper can pay by card in one step."

Every repo starts with Pullboard's standard doctrine. Add to it, override it, or decline any part of it.

### Spec

Every requirement is one row of `SPEC.md`, in one format:

```
- <id> [<status>, <priority>] <what must be true> | gate: <what proves it>
```

For example:

```markdown
- G1 [approved, must] A shopper can pay by card in one step. | gate: test/checkout.test.js
```

The id is a section letter and a number. A row stays a draft until you approve it, and only approved rows count.

### Receipts

We build Pullboard this way, and nearly one in three items goes back. One receipt:

```
#13  worktree prints a subagent's opening lines

     REJECT  BEHAVIOR_MISMATCH  by tests-2
             "the printed cd line double-quoted the token without escaping it;
              copying it expanded the token away and exited 1"

     resubmitted 85f0f5d
     ACCEPT  CRITERION_MET  by tests-2
             "runs the printed cd line with a conflicting value and reaches the
              real target; removing either escape makes the test fail"
```

## Pullboard View

Your agents work in terminals. You watch them here: every project on this machine, live on one page.

- **Needs you:** only your calls. Decisions passed up, rows to approve, held lanes.
- **Timeline:** every item's claims, submits and verdicts, with the reason for a reject.
- **Actions:** add items, answer decisions, shout to a lane, hold a lane.
- **API:** it runs on local API v1, which your own scripts can use too.
- **Export:** `view --export` writes a static, replayable snapshot.

```sh
pullboard view
```

The Pullboard board shows open, claimed, submitted and accepted work, with a pending decision and the accepted item's review history.

 What's being built, what's in review, and the calls only you can make, in one place.

## Get started

Thirty seconds to see it, then your own repo. You need git and Node 22.13 or newer.

### Installation

```sh
npm i -g pullboard
pullboard tour
```

On a throwaway repo, **you** approve one rule: greet a blank name as "world". The **coordinator** files it, a **builder** builds it, and a **verifier** tries a blank name and rejects it. The **builder** fixes it and adds a test. The **verifier** breaks the fix on purpose, sees the test fail, and accepts. The **coordinator** merges it with a receipt.

The timed Pullboard tour shows a change submitted, rejected for a missed edge, fixed and accepted.

### Project setup

Set it up once, then talk to one agent.

Starting with an agent. You run pullboard init in your git repo, commit what it wrote, open a new Claude Code session in that folder and say what to build. That agent becomes the coordinator: it takes the spec with you, plans lanes and items, runs a builder per lane and a verifier that built none of it, and merges verified work only.

`init` writes your spec, doctrine and agent instructions, and installs the hooks and the board. Commit what it wrote, then open Claude Code in the repo and say what to build. That agent becomes your coordinator.

```sh
pullboard init
git add -A && git commit -m "chore(repo): set up pullboard"
```

### Manual workflow

Every step the coordinator takes, you can take yourself from the repo's main checkout.

```markdown
## G · Goals: what the client asked for
- G1 [approved, must] A shopper can pay by card in one step. | gate: test/checkout.test.js
- G2 [draft, aim] Saved carts follow a shopper across devices. | serves: G1
```

 Write the spec in SPEC.md.

Then set the gate and the lanes in `pullboard.json`, as in Configuration.

```sh
pullboard add web "Checkout" --specs G1 --criterion "card payment takes one step"
```

File the work. Its bar freezes when an agent claims it.

```sh
pullboard worktree web
cd ../myapp-web-1
pullboard next
pullboard submit 1
```

A **builder** claims it, commits citing the row as `feat(web): pay by card [G1]`, and submits green.

```sh
pullboard worktree review
cd ../myapp-review-1
pullboard next --verify
pullboard verify 1 accept --note "paid in one step; without the fix the test fails"
```

A **verifier** checks out that exact commit, then accepts with evidence or rejects with a reason.

### Working with agents

A few commands keep every agent on track.

- `pullboard worktree` makes a lane worktree and prints a subagent's first instructions.
- `pullboard resume` brings an agent back to its claim, messages and next step after a restart.
- `pullboard next` claims the next free item, never one someone else holds.
- `pullboard run` lets a lighter model build simple items unattended.
- Claude Code gets skills. Codex and others read `AGENTS.md` or `pullboard prompt `.

## Architecture

Your whole board is one file inside `.git`, on your machine.

Every move follows one declaration, published in docs/lifecycle.md.

### Agentic Item Lifecycle (AILC)

Items are state machines. Every item starts **open**. An agent claims it and it's **claimed**; if the agent goes quiet, it reopens. Once submitted, it's **submitted** until a verifier accepts it as **verified** or rejects it back to **open**. Only the coordinator can **withdraw** an item. The board refuses any move the declaration doesn't allow.

An item's life, drawn from src/machine.js: each state an item can be in, the moves between them, and the refusals every way into a final state can raise.

 Drawn from one declaration, `src/machine.js`, which the commands, the view and the docs all share.

### Data and storage

Everything lives in your repo. Nothing is hosted.

- **Spec, doctrine and config:** plain files, committed with your code.
- **The board:** one SQLite file inside `.git`, shared by every worktree, never committed.
- **Submitted work:** pinned in git, so it survives a deleted worktree.
- **Backups:** `pullboard export` writes out the whole board.

Where things live. The main checkout is the coordinator and holds SPEC.md, DOCTRINE.md, pullboard.json, AGENTS.md and the git hooks. Inside .git, shared by every worktree, are the board and the pinned submitted commits. Beside it, each agent works in its own worktree, builders in their lanes and a verifier, all on the same board. pullboard view lists every project on this machine.

### Configuration

`pullboard.json` sets the gate and the lanes.

```json
{
  "gate": "npm test",
  "lanes": {
    "web": { "owns": ["apps/web/"], "specs": ["G"] },
    "review": { "owns": [] }
  }
}
```

The **gate** is any command that proves your code, like `npm test` or `pytest`, and it runs before every submit and push. Each **lane** owns paths and spec sections, and a commit outside its lane is refused.

#### Multi-language support

Pick the gate for your stack. Chain checks with `&&`, like `ruff check . && pytest`.

| Stack | Gate |
| --- | --- |
| JavaScript, TypeScript | `npm test` |
| Python | `pytest` |
| Go | `go test ./...` |
| Rust | `cargo test` |
| Java | `mvn test` or `gradle test` |
| Ruby | `bundle exec rspec` |
| C#, .NET | `dotnet test` |

## Purpose

Pullboard exists to keep a team of agents coherent over a long build.

### Limits

- Worktree identity only means something on one machine. It's not a security boundary.
- You can skip a hook with `--no-verify`. The pre-push gate and the verifier are the backstops.
- CI runs on Linux and macOS. Windows isn't tested yet.

### Planned features

- **The relay.** Your boards, live on your phone and other machines. Sealed records, never code.
- **A roadmap in Pullboard View.** Every milestone and what's left in it, at a glance.

### Docs

The reference docs, in reading order.

- Lifecycle: how an item moves, state by state.
- CLI JSON API: every command's output, for scripts and tools.
- Stored formats: the board's files, exports and their versions.
- RFCs: the design decisions, and why.

### License

Pullboard is released under the MIT License.

---

 Vibe hard. Verify harder.

# kouhxp/gutsy

## 关联链接

- https://pullboard.dev

## 导航

- 项目页：[[10-项目/github.com_07095bf1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
