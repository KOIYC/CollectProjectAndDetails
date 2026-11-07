---
type: "corpus"
item_id: "fcb6084212422639"
title: "Show HN: Design guidance and UI checks for coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50394952"
project_url: "https://github.com/smokeeaasd/flawless-ui-ux"
author: "smokeeaasd"
published_at: "2026-11-06T16:57:39Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_smokeeaasd
  - story_50394952
  - show_hn
metrics: {"points": 4, "comments": 1, "engagement_velocity": 4}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Design guidance and UI checks for coding agents

> [!info] 一句话导读
> smokeeaasd/flawless-ui-ux

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50394952>
> 指标：点赞=4 · 评论=1 · engagement_velocity=4
> 作者：smokeeaasd　|　发布：2026-11-06T16:57:39Z
> 项目链接：<https://github.com/smokeeaasd/flawless-ui-ux>
> 采集：2026-11-07T09:43:25+08:00　|　id：`fcb6084212422639`

## 正文

# smokeeaasd/flawless-ui-ux

A UI/UX skill for coding agents to build distinctive, usable interfaces.

- Stars: 64
- Forks: 1
- Watchers: 64
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-11-03T14:36:42Z

## Languages

- CSS
- HTML
- JavaScript
- Shell

## Topics

- accessibility
- agent-skills
- ai-agents
- anti-slop
- codex
- design-systems
- frontend
- opencode
- ui-design
- ux-design

## Top Contributors

- smokeeaasd (31 contributions)

---

## README

 Build and refine interfaces around your product's audience, content, and identity.

  

  

  

  

  

  

  

  

  

  

  

 Install ·
 Use the skill ·
 How it works ·
 Inspect and verify ·
 Docs

## Install

From your project directory, run one command with your preferred package manager:

```bash
# npm
npx flawless-ui-ux@latest install

# pnpm
pnpm dlx flawless-ui-ux@latest install

# Bun
bunx flawless-ui-ux@latest install
```

Requires **Node 22.12+**. In a terminal, choose **project or global scope**, select **one or more agents**, and **confirm the destinations** before copying. Use Space to select and Enter to continue. Ctrl+C cancels before installation files are written.

Explicit flags run directly:

```bash
npx flawless-ui-ux install --codex
npx flawless-ui-ux install --codex --devin
npx flawless-ui-ux install --claude-code --global
npx flawless-ui-ux install --project ./app
npx flawless-ui-ux install --yes
```

`--yes` skips the menu and uses the defaults when no other flags are supplied: all supported agents in the current project. JSON output, CI, and non-terminal execution remain noninteractive. Use `--format json` for machine-readable output.

 Install the skill through skills.sh

```bash
npx skills add smokeeaasd/flawless-ui-ux --skill flawless-ui-ux
```

This installs the skill through the Skills CLI. Its runtime requirements and agent selection follow that installer. The inspection CLI is available separately through the npm commands in this guide.

 Install from a checkout with Bash

```bash
bash /absolute/path/flawless-ui-ux/install.sh --codex --project
```

The Bash alternative requires `--project` for local installation; its default is global. Windows users need Git Bash or WSL.

## Use the skill

Describe the interface you need and name the skill:

```text
Use the flawless-ui-ux skill to build a financial dashboard for freelancers.
```

In Codex, invoke `$flawless-ui-ux`. Hosts with slash commands use `/flawless-ui-ux`; Pi uses `/skill:flawless-ui-ux`. You can also request the skill by name through your host's skill mechanism. Start a new session after installation if discovery needs to refresh.

Continue in the same conversation as the interface develops:

| Task | Example request |
|---|---|
| Create | Build a landing page for an app that coordinates deployments and incident handoffs. |
| Redesign | Redesign this account screen for mobile using the supplied brand palette. Preserve its content and behavior. |
| Refine | Give the main action more presence while preserving the page's visual character. |
| Focus | Improve typography and spacing. Preserve wording, colors, and functionality. |
| Review | Review this dashboard for readability, navigation, accessibility, and repeated generic patterns. Report findings without editing files. |

## How it works

**The skill guides design and implementation.** It connects product context to composition, typography, color, density, imagery, and interaction. Focused references support creation, redesign, refinement, and review in your existing stack.

**Refinement develops the intended character.** An interface may need more presence, less competing emphasis, or a more consistent finish. The right intervention depends on the content and task. Generic copy, repetitive decoration, and familiar patterns are reviewed in context, alongside usability and accessibility.

**The CLI checks the implementation.** Collect project context, inspect selected source files or a running interface, and compare the result after corrections. Your agent makes the changes; the CLI provides observations and records what was actually checked.

## Inspect and verify

Use the CLI directly, or ask your agent to include these checks in its work. Replace `npx` with `pnpm dlx` or `bunx` throughout.

### Start with context and source

```bash
npx flawless-ui-ux context --project . --format json
npx flawless-ui-ux inspect --project . --source src/App.tsx --format json
```

### Check the running interface

Start your app and prepare the browser once:

```bash
npx playwright@1.64.1 install chromium
# or: pnpm dlx playwright@1.64.1 install chromium
# or: bunx playwright@1.64.1 install chromium
```

Inspect the actual development-server URL and save a baseline:

```bash
npx flawless-ui-ux inspect --project . --source src/App.tsx --url http://localhost:5173 --output ../app-before --format json
```

After corrections, repeat the saved scope:

```bash
npx flawless-ui-ux verify ../app-before/run.json --output ../app-after --format json
```

The comparison separates **persistent**, **new**, and **no-longer-observed** findings. Missing confirmed targets and changed conditions remain unverified.

| Area | Evidence collected |
|---|---|
| Accessibility | Selected axe contrast and accessible-name rules, including incomplete results for review |
| Text and layout | Computed font sizes and horizontal overflow at the sampled widths |
| Assets and runtime | Visible broken images and uncaught JavaScript errors |
| Copy and icons | Exact repeated phrases and arrow cues for contextual review |
| Source | Literal pixel font sizes and arrow/icon cues in selected files |

 Scope, artifacts, and verification limits

- Default viewport samples are **1440 × 900** and **390 × 844**. Repeat `--viewport WIDTHxHEIGHT` to choose others.
- Repeat `--source` for additional files, or use `--selector` to inspect a region.
- Use `--browser-executable` or `FLAWLESS_BROWSER_EXECUTABLE` to select an installed compatible Chromium. Keep browser conditions consistent between runs.
- With `--output`, a new directory receives `run.json` and available screenshots; its parent must exist. Existing output directories are preserved. Without it, results go to stdout.

These samples do not establish full WCAG conformance, complete keyboard journeys, business-flow correctness, or visual quality. Small text and repetition require context. Inspection does not edit files, start servers, download browsers, or submit forms.

CLI exit codes: `0` for completed coverage without confirmed errors, `1` for completed coverage with confirmed errors, and `2` for invalid input or incomplete requested coverage. The installer also returns `0` when confirmation is declined and `130` when a prompt is interrupted.

## Installation notes

Existing files, local changes, and links are preserved. Review or remove an old installation before reinstalling. Host rules, plugins, permissions, and trust settings stay under your control.

The twelve supported agents use **five project copies** of the same skill. Hosts that discover `.agents/skills` share one copy; others use their native directories.

 Host-specific details

- **Grok Build:** project skills become available after folder trust.
- **DeepSeek Harness:** install from the nearest Git root, or the working directory without Git. Custom provider roots may change discovery.
- **Kiro:** custom agents can reference skills through `skill://` resources.
- **Global paths:** honor each host's configuration directory and overrides. Devin uses `APPDATA` on Windows and `XDG_CONFIG_HOME` elsewhere.

See the installation contract for exact paths and the testing guide for recorded compatibility evidence and pending checks.

## Development

```bash
bun install --frozen-lockfile
bun test
```

Bun is the development toolchain; the published CLI runs on Node. See testing for browser fixtures, packaging checks, and Windows/Ubuntu CI.

## Documentation

- Workflow guide — creation, redesign, refinement, and review
- CLI contract — installation paths, options, context, and comparison limits
- Product contract — philosophy and scope
- Architecture — skill, project context, and inspection core
- Manual evaluations — reproducible tasks and evidence criteria
- Changelog

## License

MIT.

Agent icons are provided by Lobe Icons, using theme-aware images pinned to a specific revision. Product names and marks belong to their respective owners. Badges use Shields.io. Monthly downloads refer to the npm CLI package.

## 评论（1/1）

> **memjay** · 2026-11-06T20:11:20.000Z　
> Any examples of UI and UX created with this?Maybe with different directions of style to tell whether this actually creates good results.

## 关联链接

- http://localhost:5173

## 导航

- 项目页：[[10-项目/github.com_096ac82b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
