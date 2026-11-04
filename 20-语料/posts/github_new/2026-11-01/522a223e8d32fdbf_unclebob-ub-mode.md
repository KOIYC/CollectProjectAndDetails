---
type: "corpus"
item_id: "522a223e8d32fdbf"
title: "unclebob/ub-mode"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/unclebob/ub-mode"
project_url: "https://github.com/unclebob/ub-mode"
author: "unclebob"
published_at: "2026-10-25T16:04:09Z"
captured_at: "2026-11-04T09:53:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-01"
pub_day: "2026-10-25"
tags:
  - 语料
  - github_new
  - created:>2026-10-21
metrics: {"stars": 6796, "forks": 379, "open_issues": 10}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# unclebob/ub-mode

> [!info] 一句话导读
> `ub-mode` is an agent skill that enforces disciplined software engineering principles when writing or changing code. It is loosely based on portions of [@poteto…

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/unclebob/ub-mode>
> 指标：stars=6796 · forks=379 · open_issues=10
> 作者：unclebob　|　发布：2026-10-25T16:04:09Z
> 项目链接：<https://github.com/unclebob/ub-mode>
> 采集：2026-11-04T09:53:48+08:00　|　id：`522a223e8d32fdbf`

## 正文

# ub-mode

`ub-mode` is an agent skill that enforces disciplined software engineering principles when writing or changing code. It is loosely based on portions of [@poteto](https://github.com/poteto)'s rules (`poteto-mode` / `pstack`), reduced and paired with deterministic quality-gate tools:

1. **First Make it Work** — Laziness Protocol, Foundational Thinking, TDD, Redesign From First Principles, Attack the Premise, Subtract Before You Add, Outcome-Oriented Execution, Build the Lever, and Architecture (Model the Domain, Boundary Discipline, Type System Discipline, Make Operations Idempotent, Separate Before Serializing Shared State).
2. **Then Make it Right** — Fix Root Causes, Sequence Work into Verifiable Units, Test Behavior (Not Implementation), [Crapper](https://github.com/unclebob/crapper) (`CRAP < 10`), [Dryer](https://github.com/unclebob/dryer) (duplication `< 0.8`), [Mutator](https://github.com/unclebob/mutator) (cover the uncovered, kill the survivors, delete dead code), and Refactoring.
3. **Practice** — Keep a Log, Guard the Context Window, Worktree Cleanup, and Commit and Push in small ordered commits.

## Companion Tool Repositories

`ub-mode` relies on deterministic quality-gate tools to enforce structure, complexity, duplication, and test thoroughness:

- [unclebob/crapper](https://github.com/unclebob/crapper) — Computes cyclomatic complexity, test coverage, and CRAP score per function so every function stays under the CRAP threshold (`< 10`).
- [unclebob/dryer](https://github.com/unclebob/dryer) — Detects structural code duplication so duplicate blocks (`>= 0.8` similarity) are eliminated.
- [unclebob/mutator](https://github.com/unclebob/mutator) — Runs mutation testing to expose uncovered code and surviving mutants that tests fail to catch.
- [unclebob/uml-viewer](https://github.com/unclebob/uml-viewer) — Visualizes components, coverage, CRAP, mutation scores, and dependency directions.

## Installation

Copy `SKILL.md` into your agent's skills directory as `ub-mode/SKILL.md` (for example `~/.grok/skills/ub-mode/SKILL.md`, `~/.claude/skills/ub-mode/SKILL.md`, or `~/.cursor/skills/ub-mode/SKILL.md`), then invoke `/ub-mode`.

## 关联链接

- https://github.com/poteto
- https://github.com/unclebob/crapper
- https://github.com/unclebob/dryer
- https://github.com/unclebob/mutator
- https://github.com/unclebob/uml-viewer

## 导航

- 项目页：[[10-项目/github.com_522a223e]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
