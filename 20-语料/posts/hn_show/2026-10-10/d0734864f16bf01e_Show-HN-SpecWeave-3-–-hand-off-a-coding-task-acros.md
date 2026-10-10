---
type: "corpus"
item_id: "d0734864f16bf01e"
title: "Show HN: SpecWeave 3 – hand off a coding task across Claude Code, Codex and Grok"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50026741"
project_url: "https://github.com/anton-abyzov/specweave"
author: "aabyzov"
published_at: "2026-10-09T21:25:21Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_aabyzov
  - story_50026741
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: SpecWeave 3 – hand off a coding task across Claude Code, Codex and Grok

> [!info] 一句话导读
> anton-abyzov/specweave

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50026741>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：aabyzov　|　发布：2026-10-09T21:25:21Z
> 项目链接：<https://github.com/anton-abyzov/specweave>
> 采集：2026-10-10T09:53:50+08:00　|　id：`d0734864f16bf01e`

## 正文

# anton-abyzov/specweave

Spec-first AI development: describe a feature → AI creates spec + plan + tasks, builds autonomously, syncs to GitHub/JIRA. Domain-expert skills for PM, Architect, Frontend, QA learn your patterns permanently. Claude Code, Codex, Cursor, Copilot & more.

- Stars: 147
- Forks: 19
- Watchers: 147
- Open issues: 9
- License: MIT License
- Homepage: https://spec-weave.com
- Default branch: develop
- Created: 2025-10-25T21:31:34Z

## Languages

- CSS
- HTML
- JavaScript
- MDX
- PowerShell
- Shell
- TypeScript

## Topics

- ai
- azure-devops
- claude
- cli
- developer-tools
- documentation
- jira
- testing
- typescript

## Top Contributors

- anton-abyzov (538 contributions)
- dependabot[bot] (87 contributions)
- abycolibri (3 contributions)
- github-actions[bot] (2 contributions)
- gurdasnijor (1 contributions)

---

## README

 SpecWeave

 AI-assisted development, under control.
 Stop prompting. Start specifying.

## The Problem

**36.82% of AI skills have security flaws** (Snyk ToxicSkills). In May 2025, 170 out of 1,645 vibe-coded apps had security vulnerabilities exposing personal data. No specs. No tests. No review. Just vibes.

Every alternative is an instruction layer — Cursor Rules, Copilot Instructions, Windsurf Rules, CLAUDE.md. They tell the AI *how* to write code but never *what* to build, never *how* to test it, and never *when* it's done.

SpecWeave is a spec-first development layer. Configuration, not prompting. Enforced, not hoped for.

## The Solution

```
You: "Build a checkout flow with Stripe"
  ↓
  spec.md → plan.md → tasks.md       ← you review the plan
  ↓
  Autonomous execution for hours      ← AI builds, tests, fixes
  ↓
  Quality gates (Grill + Judge-LLM)   ← code reviewed automatically
  ↓
  Synced to GitHub/JIRA/ADO           ← closed, documented, shipped
```

Every feature starts as a specification — user stories, acceptance criteria, architecture decisions — before a single line of code is written. TDD enforces correctness. Quality gates catch what tests miss.

## Built With SpecWeave

12 production projects shipped in 3 months. 5 in the App Store.

| App | Platform | What It Does |
|-----|----------|-------------|
| **EasyChamp** | Web (GCP) | Enterprise sports league management. 20+ microservices, ML video analytics. 4 years in production. |
| **SketchMate** | App Store | AI drawing game — multi-model evaluation judges player art semantically. |
| **Lulla** | App Store | Baby sleep app with Apple Watch. ML cry classification (tired/hungry/pain). |
| **Football 2026** | App Store + Web | World Cup 2026 companion. AI travel planner, live tickets, team stats. |
| **SkillUp Football** | App Store | Coaches monetize training via Stripe. Instagram-like feed, scheduling. |
| **BizZone** | App Store | Student & business events with AI-powered news generation. |
| **EduFeed** | Web | NotebookLM meets Zoom. Upload videos, get quizzes, flashcards, live rooms. |
| **JobWeave** | Web | AI-powered job search. Smart matching, resume optimization. |
| **SpecWeave** | npm | The framework itself. 600+ increments, 538+ releases. |
| **SpecWeave Umbrella** | GitHub | Multi-repo orchestration workspace for all repositories. |
| **vskill** | npm | Package manager for AI skills. Security scanning, 49 platforms. |
| **verified-skill.com** | Web | Skill marketplace & studio. 105K+ verified skills, eval system. |

Browse increments on GitHub — full transparency.

## Quick Start

```bash
npm install -g specweave       # Node.js 20.12.0+
cd your-project
specweave init .
# Then in Claude Code, Cursor, Copilot, or any AI tool:
# "Build me a user authentication system"
```

## How It Compares

| Capability | Cursor Rules | Copilot Instructions | Windsurf | Cline | Vibe Coding | **SpecWeave** |
|------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Structured specs (spec + plan + tasks) | — | — | — | — | — | **Yes** |
| Quality gates (Grill + Judge-LLM + 130 rules) | — | — | — | — | — | **Yes** |
| Autonomous execution (hours, unattended) | — | — | — | — | — | **Yes** |
| Multi-agent teams (parallel, contract-first) | — | — | — | — | — | **Yes** |
| External sync (GitHub / JIRA / ADO) | — | — | — | — | — | **Yes** |
| TDD enforcement (strict red-green-refactor) | — | — | — | — | — | **Yes** |
| LSP code intelligence (198x faster) | — | — | — | — | — | **Yes** |
| Self-improving skills (learns from corrections) | — | — | — | — | — | **Yes** |

Cursor tells AI "use Tailwind." SpecWeave tells AI "build a checkout flow with 5 acceptance criteria, test it, review it, sync to JIRA, and close."

## Key Features

**Spec-First Planning** — Every feature starts as spec.md + plan.md + tasks.md. Configuration, not prompting.

**TDD Enforcement** — Strict red-green-refactor. Tasks cannot close without passing tests. Coverage targets enforced.

**Agent Swarms** — Run parallel agents across iTerm/tmux panes. Team lead splits work, each agent owns an increment.

```
┌──────────────────┬──────────────────┬──────────────────┐
│  Agent 1 (auth)  │ Agent 2 (payments)│ Agent 3 (catalog)│
│  sw:auto         │  sw:auto         │  sw:auto         │
│  ████████░░ 80%  │  ██████░░░░ 60%  │  ████░░░░░░ 40%  │
└──────────────────┴──────────────────┴──────────────────┘
```

**LSP Code Intelligence** — 198x faster than grep, 0 false positives. Semantic references, definitions, and types.

**100+ Skills** — PM, Architect, QA, Security, DevOps, Frontend, Backend, Mobile, ML. Every skill is customizable via skill-memories without forking.

**External Sync** — GitHub Issues, JIRA, Azure DevOps — bidirectional, real-time. Close an increment, external tools update automatically.

**Enterprise Ready** — Compliance audit trails (SOC 2, HIPAA, FDA). Brownfield analysis. Multi-repo coordination. Multi-environment deployment.

**Dashboard** — Built-in web dashboard for increment progress, analytics, cost tracking, and multi-project monitoring.

## Skills Ecosystem

SpecWeave skills are published and verified at **verified-skill.com**. The vskill package manager provides:

- **Security scanning** — 52 attack patterns, SHA-256 pinning, blocklist API
- **49 agent platforms** — one install deploys to Claude Code, Cursor, Copilot, Windsurf, and 45 more
- **Skill evals** — unit tests, A/B comparisons, cross-model testing. Skills tested like programs.
- **Visual Skill Studio** — `vskill eval serve` for benchmarks, comparisons, and history

```bash
npx vskill install remotion-best-practices    # Install from registry
npx vskill eval run my-skill                  # Run eval suite
```

## Core Commands

| You say | SpecWeave runs |
|---------|---------------|
| "Build me X" | `sw:increment` → spec + plan + tasks |
| "Go ahead" | `sw:auto` → autonomous execution |
| "Ship it" | `sw:done` → quality gates + close |
| "Split into teams" | `sw:team-lead` → parallel agents |
| "Review the code" | `sw:code-reviewer` → 6 parallel reviewers |

Full command reference

## Upgrading to v1.1.0 (Opus 4.7 Alignment)

SpecWeave v1.1.0 aligns the framework with Claude Opus 4.7 best practices.

### P0 Fixes (required if using judge-llm or team-lead)

1. **Remove fixed extended thinking**: `sw:judge-llm` no longer passes `thinking.budget_tokens`. Adaptive prompt hints replace it. No user action needed — the CLI handles this automatically.

2. **Team-lead spawn heuristic**: `sw:team-lead` now only spawns agents when `domains ≥ 3` OR `tasks ≥ 15` OR `--parallel` is set. Previously it always spawned agents.

3. **State markers removed**: `skill-chain-*.json` and `interview-*.json` state files are no longer written. `pretooluse-guard.ts` uses TaskGet-based state with filesystem fallback.

### Config Migration

Run the migration script to add new config keys with defaults:

```bash
specweave migrate-config-0669
```

### Deprecations

See full list in CHANGELOG.md. Key migrations:
- `/sw:tdd-red` → `/sw:tdd-cycle --phase red`
- `/sw:github-sync` → `/sw-github:sync-spec`
- `/sw:team-build` → `/sw:team-lead --preset `

Full migration guide: `.specweave/docs/internal/specs/opus-47-migration.md`

## Documentation

**spec-weave.com** — guides, reference, and enterprise docs.

## Community

Discord · YouTube · GitHub Issues

## License

MIT — github.com/anton-abyzov/specweave

# filippofinke/cad-studio

## 关联链接

- https://spec-weave.com

## 导航

- 项目页：[[10-项目/github.com_c8990668]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
