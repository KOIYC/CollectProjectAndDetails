---
type: "corpus"
item_id: "81bdca3ff576a97e"
title: "Show HN: SLCR – An open standard for agent-native software requirements"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50291963"
project_url: "https://slcr.dev/"
author: "robbiemckinstry"
published_at: "2026-10-29T16:43:21Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_robbiemckinstry
  - story_50291963
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: SLCR – An open standard for agent-native software requirements

> [!info] 一句话导读
> Skip to content Docs Announcements About

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50291963>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：robbiemckinstry　|　发布：2026-10-29T16:43:21Z
> 项目链接：<https://slcr.dev/>
> 采集：2026-10-30T09:46:09+08:00　|　id：`81bdca3ff576a97e`

## 正文

Skip to content Docs Announcements About
Sliceable, Linked, Checkable Requirements
 A specification for software requirements that agents can read in slices and tools can check.
 Give each agent only the requirements its task needs, then verify the result with the tools you already use.
 Prompt CLI Skill
Set up SLCR requirements for this project by following https://slcr.dev/docs/getting-started/quickstart
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/wack/slcr/releases/latest/download/slcr-installer.sh | sh
npx skills add wack/slcr
Why SLCR
 Long prose specs cause context rot, and agent errors compound across tasks
S Sliceable
 Hand an agent one requirement and the context it links to. The rest of the spec stays out of its context window.
L Linked
 Requirements refine and depend on each other, and combine with AND, OR, and XOR.
C Checkable
 Acceptance criteria map to validators such as tests, linters, and agent checks. slcr check reports what's met.
R Requirements
 As agents write more code, teams are moving to spec-driven development. SLCR makes the spec a first-class artifact with a standard format.
One source
 Documents for people, slices for agents
Rendered spec todo-api
 SEC-002 Views
 REQ-001 TodoListItem endpoint
 REQ-002 POST creates an item
 REQ-004 Request is authenticated
 REQ-003 GET reads an item
 SEC-003 Controllers
 REQ-005 TodoListItem controller
 REQ-006 Validates the request payload
 SEC-004 Models
 REQ-007 Table todo_list_item exists
Agent slice REQ-004
 REQ-004 · Request is authenticated MUST · refines REQ-002, REQ-003 The request MUST be authenticated.
 REQ-002 · POST creates an item MUST · refines REQ-001
 REQ-003 · GET reads an item MUST · refines REQ-001
Hover a requirement to see where it sits in the full document.
How it works
0 1 Write a requirement
 In JSON, TOML, or YAML, with acceptance criteria.
# SPEC.slcr.yaml (excerpt)
- kind: requirement
 id: REQ-007
 title: Table todo_list_item exists
 body: There MUST be a table `todo_list_item`.
 modality: MUST
 acceptanceCriteria:
 - kind: acceptanceCriterion
 id: AC-001
 title: Table schema is declared
 0 2 Attach a validator
 Use any tool you declare: tests, linters, browser tests, or agents.
# db/.validators.slcr.toml (excerpt)
\[[validator\]]
requirement = "todo-api/REQ-007"
criterion = "AC-001"
tool = "ast-grep"
with = { rule = "rules/todo-table.yml" }
 0 3 Run the check
 Red before you build it, green after. Runs in CI.
$ slcr init
$ slcr check
The project
 An open standard with a reference implementation
Specification
 JSON Schemas, satisfaction semantics, and slice rules.
slcr CLI (external link)
 Reference implementation in Rust.
Agent skill (external link)
 Teaches agents to write SLCR and use the CLI.
Contribute
 Help shape the standard
 Issues, format feedback, tool descriptors, and pull requests are all welcome.
 View on GitHub Open an issue
SLCR is an open standard for agent-native software requirements.
Code of Conduct Security

## 评论（1/1）

> **robbiemckinstry** · 2026-10-29T16:47:41.000Z　
> I built SLCR to address known limitations in spec-driven development. Specs codify a project's desired behavior in a human-optimized format that serves as a central source of truth for implementation agents. But when agents re-ingest the entire document when implementing, or translating to tickets it can introduce errors in different ways:1. Ingesting the entire spec can lead to context bloat, which not only costs extra tokens, but also decreases agent coherence.
> 2. Translating spec to tickets can be lossy because agents may make small omissions or conflate information required across multiple tickets.
> Further, errors compound from agent session to session, making small omissions or missed details early in the process much bigger problems after multiple rounds of iteration.SLCR (Sliceable, Linked, Checkable Requirements, pronounced slicer) is a new open-standard document format to make sure agents build to spec every time, without sacrificing human readability.
> Requirements live in one structured spec file (TOML, JSON, or YAML), with typed edges between requirements forming a DAG. Agents read small, task-specific walks of the DAG called slices, which provide them with all of the context they need to understand a given requirement with none of the superfluous context.Requirements can have acceptance criteria that can be checked by a validators, which is a mapping to an executable tool to verify the requirement, vitest, your linter, or ast-grep. Requirements can be composed with AND, OR, or XOR, and the SLCR CLI can check whether each requirement is satisfied, so your spec is always synced to your codebase's current status. This helps prevent multi-session agent drift and misalignment by ensuring that no agent session invalidates existing pinned requirements.A slice is one requirement plus the context it actually needs, determined by walking the DAG from a leaf node back to the root. When an agent picks up a ticket, you give it the slice instead of the whole spec, eliminating superfluous text unrelated to the requirement at hand. People still get the full picture, because the CLI renders the whole spec to deterministic, read-only Markdown.
> There's also an agent skill that teaches agents to use the CLI and write valid SLCR.This tool is for engineers and tech leads on long-lived codebases who are giving agents real implementation work and want a check beyond reading the diff. If you're writing one-off scripts or throwaway prototypes, you probably don't need this.The format is an open standard. The reference implementation written in Rust and released under the MIT license. Pull requests welcome!Repo: https://www.github.com/wack/slcr
> Site: https://www.slcr.dev

## 关联链接

- https://github.com/wack/slcr/releases/latest/download/slcr-installer.sh
- https://slcr.dev/docs/getting-started/quickstart

## 导航

- 项目页：[[10-项目/slcr.dev_0330b632]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
