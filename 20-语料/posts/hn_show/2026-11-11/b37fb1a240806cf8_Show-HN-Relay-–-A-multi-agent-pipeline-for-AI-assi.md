---
type: "corpus"
item_id: "b37fb1a240806cf8"
title: "Show HN: Relay – A multi-agent pipeline for AI-assisted front end engineering"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50444140"
project_url: "https://github.com/rgadda/frontend-eng-team"
author: "rajivgadda"
published_at: "2026-11-10T18:23:24Z"
captured_at: "2026-11-11T13:37:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-11"
pub_day: "2026-11-10"
tags:
  - 语料
  - hn_show
  - author_rajivgadda
  - story_50444140
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Relay – A multi-agent pipeline for AI-assisted front end engineering

> [!info] 一句话导读
> rgadda/frontend-eng-team

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50444140>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：rajivgadda　|　发布：2026-11-10T18:23:24Z
> 项目链接：<https://github.com/rgadda/frontend-eng-team>
> 采集：2026-11-11T13:37:17+08:00　|　id：`b37fb1a240806cf8`

## 正文

# rgadda/frontend-eng-team

Multi-agent pipeline for AI-assisted frontend engineering. Six roles, human-gated, tool-neutral. Runs in Claude Code, GitHub Copilot, and any AGENTS.md-aware tool.

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-04-25T16:51:09Z

## Languages

- CSS
- HTML
- JavaScript
- Shell
- TypeScript

## Topics

- agents-md-template
- ai-agents
- ai-coding
- claude-code
- claude-code-plugin
- developer-tools
- frontend
- multi-agent
- reactjs
- typescript

## Top Contributors

- rgadda (30 contributions)

---

## README

# Relay

> A six-role multi-agent pipeline for shipping frontend changes with AI assistance — tool-neutral, cache-efficient, and gated by humans at the right moments.

CI
License: MIT

> **Note:** the GitHub repo slug is `frontend-eng-team` for historical reasons. The project name is **Relay**.

```mermaid
flowchart LR
    T([Task]) --> PM[PM]
    PM --> A[Architect]
    A --> G{Human<br/>approval}
    G -->|approve| I[Implementer]
    I --> R[Reviewer]
    R --> P[Prod-Readiness]
    P --> V[Verifier]
    R -.-> V
    V --> O([PR ready])

    classDef conditional stroke-dasharray: 4 4
    class PM,P conditional
```

> Dashed boxes are conditional. **PM** runs only for feature work (skipped for bugfix / refactor / chore / docs). **Prod-Readiness** fires only when the Architect tags the plan `sensitive:*` (auth, payments, PII, etc.).

## Why

- **One context, many roles.** Each phase runs under a focused contract (plan, implement, review, verify) instead of one agent doing everything badly.
- **Cache-friendly.** Role prompts are stable prefixes; only the task payload changes. Expect >90% cache hit on a warm session.
- **Fails closed where it matters.** Verifier defaults to FAIL. Prod-Readiness fires automatically on `sensitive:*` plans (auth, payments, PII, network, reliability).
- **Tool-neutral.** Role contracts live in `.agents/` — the same pipeline runs in Claude Code slash commands, GitHub Copilot paste workflows, or any AGENTS.md-aware tool.

## Quick start

```bash
# Once per machine
claude plugin marketplace add rgadda/frontend-eng-team --scope user
claude plugin install frontend-team@frontend-team-marketplace --scope user

# Once per target repo
cd /path/to/your-frontend-project
ft-bootstrap

# Verify
/agents    # lists five subagents
/pipeline  # runs the pipeline
```

Full setup + troubleshooting: scripts/setup-global.md.

## What's inside

| Layer | Items |
|---|---|
| **Roles** (`.agents/roles/`) | PM · Architect · Implementer · Reviewer · Prod-Readiness · Verifier |
| **Orchestrators** (`.agents/`) | `pipeline.md` (full) · `pipeline-lite.md` (small, non-sensitive changes) |
| **Subagents** (`plugins/frontend-team/agents/`) | `repo-explorer` · `frontend-reviewer` · `test-runner` · `prod-readiness` · `verifier` |
| **Skills** (`plugins/frontend-team/skills/`) | `component-conventions` · `pr-prep` · `pm-clarify` · `loop-engineering` |
| **Metrics** (`scripts/`) | `collect-pr-metrics.ts` — before/after PR velocity report |

## Usage

Run the full pipeline on a new feature:

```
/pipeline Add a UserProfile component to the settings feature
          that fetches user data via Axios and displays it
          with editable fields and form validation
```

The Architect plans, you approve, then Implementer → Reviewer → Verifier run through. One slash command, one approval gate, one PR-ready output.

For small changes:

```
/pipeline-lite Add a loading spinner to SettingsPanel while user data is fetching
```

Lite mode skips PM, Architect, and Verifier. Target cost ≤25K tokens (~55% cheaper than full). A hard entry gate refuses lite mode on any task that mentions auth / payments / PII / tokens / cookies — those always run through `/pipeline`.

**When to use which:**

| Situation | Use |
|---|---|
| New feature with user-facing behavior | `/pipeline` |
| Sensitive change (auth, payments, PII, security, reliability) | `/pipeline` — always |
| Refactor touching multiple modules or a Context / hook / effect / portal | `/pipeline` |
| Change > 200 LOC or > 3 files | `/pipeline` |
| Small bugfix, config tweak, copy change, one-file typo | `/pipeline-lite` |
| CSS-only change, docs update | `/pipeline-lite` |

## Works with

- **Claude Code** — slash commands in `.claude/commands/` (`/pm`, `/architect`, `/implement`, `/review`, `/verify`, `/pipeline`, `/pipeline-lite`).
- **GitHub Copilot in VS Code** — paste-driven workflow, see `.github/copilot-instructions.md`.
- **Any AGENTS.md-aware tool** — root AGENTS.md routes into `.agents/roles/` and `.agents/pipeline.md`.

## Tech stack this template is tuned for

React 18 · TypeScript 5 (strict) · Vite · CSS Modules · Axios · Jest + RTL · Playwright · ESLint + Prettier.

Stack-specific conventions live in `.agents/conventions.md`. To adapt the template, edit that file plus `CLAUDE.md`; the role contracts themselves are stack-agnostic.

## Docs

- Architecture + file map — where every file lives and why
- Using subagents efficiently — when each one earns its keep
- Adapting the template — making it fit your project
- Diagrams — canonical Mermaid source for every diagram
- Copilot paste workflow — phase-by-phase VS Code recipe
- PR metrics script — portable CLI for before/after measurement
- Framework methodology — the deeper paper behind the pipeline
- Contributing
- Security policy

## License

MIT — see LICENSE.

## 导航

- 项目页：[[10-项目/github.com_6a9321bd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
