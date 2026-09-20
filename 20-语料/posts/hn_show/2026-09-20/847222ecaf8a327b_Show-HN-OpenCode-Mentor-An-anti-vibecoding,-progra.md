---
type: "corpus"
item_id: "847222ecaf8a327b"
title: "Show HN: OpenCode Mentor - An anti-vibecoding, programming mentor configuration"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49733127"
project_url: "https://github.com/davejpeters/opencode-mentor"
author: "davejpeters"
published_at: "2026-09-16T21:15:14Z"
captured_at: "2026-09-20T14:03:43+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_davejpeters
  - story_49733127
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: OpenCode Mentor - An anti-vibecoding, programming mentor configuration

> [!info] 一句话导读
> davejpeters/opencode-mentor

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49733127>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：davejpeters　|　发布：2026-09-16T21:15:14Z
> 项目链接：<https://github.com/davejpeters/opencode-mentor>
> 采集：2026-09-20T14:03:43+08:00　|　id：`847222ecaf8a327b`

## 正文

# davejpeters/opencode-mentor

An anti-vibecoding, programming mentor configuration

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 0
- Default branch: main
- Created: 2026-09-16T00:17:12Z

## Languages

- TypeScript

## Top Contributors

- davejpeters (10 contributions)

---

## README

# MAI: Mentor AI Infrastructure for OpenCode

MAI is an opinionated OpenCode configuration for learning software development with AI. It is inspired by Boot.dev and PAI, with a mentor-first goal: use AI to strengthen reasoning and independent problem-solving, not merely to produce code quickly.

The default assistant a learning orchestrator that routes work to specialist agents. The prompts favor diagnosis, small hints, deliberate practice, review, verification, and gradually reduced support. This repository is configuration and an evolving experiment, not a claim that AI can replace teachers, experience, or independent judgment.

## Architecture

```text
OpenCode
  -> opencode.json and AGENTS.md
  -> mentor-orchestrator
  -> mentor | reviewer | architect | drill-instructor
  -> skills and project-aware tools
  -> local learner state and session reflection
```

- opencode.json selects the primary agent, loads plugins, configures Context7, and defines baseline permissions.
- AGENTS.md establishes the Rob identity and repository-wide operating rules.
- agents contains the orchestrator and specialist prompts.
- core supplies the shared tutoring policy at runtime.
- tutor exposes learner-profile, concept-graph, curriculum, exercise, grading, and reflection tools implemented under `tools/tutor/`.
- `plugins/context-loader.ts` injects the shared Core policy once per session.

## Agent Roles

| Agent | Responsibility |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Mentor Orchestrator | Classifies requests, retrieves only relevant learner context, and delegates to a specialist. |
| Mentor | Explains concepts, diagnoses errors, and gives the least help needed for progress. |
| Reviewer | Reviews submitted work for correctness, design, security, and learning evidence without rewriting it by default. |
| Architect | Explores system boundaries, data flow, constraints, and trade-offs. |
| Drill Instructor | Creates focused exercises, evaluates attempts, and adjusts difficulty from observed results. |

A pair-programmer prompt is included but disabled by default so the mentor-first workflow remains the primary path. OpenCode's built-in `explore` agent is used for codebase discovery where permitted.

## Pedagogy

- PEDAGOGY explains the educational rationale and vocabulary.
- core is the operational source of truth for tutoring behavior.
- Role prompts in `agents/` specialize Core without replacing it.
- assignment defines learner-owned practice tasks; the other skills add focused workflows such as review, TDD, security, and Go development.

The central loop is **diagnose → teach → practice → assess → reflect → progress**. Assistance is calibrated to demonstrated work, and the system aims to fade scaffolding as the learner becomes more independent.

## Learner State

Runtime learner state is written inside each active project under `.opencode/mentor/`. It can contain learner identifiers, project paths, goals, evidence, misconceptions, exercises, and reflections.

## Prerequisites and Setup

Prerequisites:

- A working OpenCode installation.
- Bun for the TypeScript tools and plugins.
- Optional: Context7 MCP network access for current library documentation, beads for issue tracking, graphify or codegraph for codebase discovery.

Back up any existing OpenCode configuration before installing. Then clone this repository as the global configuration and install its development dependency:

```bash
mv ~/.config/opencode ~/.config/opencode.backup
git clone https://github.com/davejpeters/opencode-mentor ~/.config/opencode
cd ~/.config/opencode
bun install
```

Review `opencode.json`, agent permissions, and plugin behavior before first use. Restart OpenCode after changing configuration, agents, skills, or plugins because those files are loaded at startup.

## Customization

Common starting points:

1. Change the Rob name and identity in `AGENTS.md`.
2. Adjust language and workflow rules under `rules/`.
3. Tune agent prompts and permissions in `agents/` and `opencode.json`.
4. Add, remove, or revise workflows under `skills/`.
5. Review defaults in `tools/tutor/runtime.ts`, including the preferred language and learner identifier strategy.
6. Disable integrations that are unavailable on your machine.
7. Add more skills, tools, agents, commands, and plugins.

## Safety Boundaries

The configuration combines prompt-level boundaries with OpenCode permissions and small defensive plugins:

- Shell commands generally require approval; a narrow set of read-only or verification commands is allowed explicitly.
- `plugins/env-protection.ts` blocks tool reads whose path contains `.env`.
- `plugins/safety-filter.ts` blocks shell commands containing `rm`.
- Agent permissions restrict editing, writing, shell use, and delegation by role.
- The mentor policy avoids complete target implementations while guided learning can still move the learner forward.
- OpenCode sharing is disabled in `opencode.json`.

These are guardrails, not a security sandbox. Inspect proposed commands and changes, keep secrets out of the repository, and tighten permissions for your environment.

## Optional Machine-Specific Integrations

- `plugins/notifications.ts` calls `notify-send` for idle-session and permission-request desktop notifications. It is intended for Linux desktops with a notification daemon; remove the plugin from `opencode.json` elsewhere.

The notification plugin tolerates command failures.

# Hometowns

## 评论（1/1）

> **davejpeters** · 2026-09-16T21:30:24.000Z　
> I built this because I was tired of feeling like I wasn't learning anything when I used AI to write code. I thought (vibecoding) an AI configuration could be helpful as a personal tutor/mentor. I know, it's contradictory to vibecode an anti-vibecoding OpenCode config.

## 导航

- 项目页：[[10-项目/github.com_553d4237]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
