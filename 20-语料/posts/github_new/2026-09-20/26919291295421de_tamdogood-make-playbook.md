---
type: "corpus"
item_id: "26919291295421de"
title: "tamdogood/make-playbook"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/tamdogood/make-playbook"
project_url: "https://github.com/tamdogood/make-playbook"
author: "tamdogood"
published_at: "2026-07-05T22:49:55Z"
captured_at: "2026-09-20T09:36:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-07-05"
tags:
  - 语料
  - github_new
  - topic:indie-hacker
metrics: {"stars": 5, "forks": 1, "open_issues": 0}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# tamdogood/make-playbook

> [!info] 一句话导读
> A Claude Code skill that turns the indie-hacker playbook into something you actually consult while building — not another thing you read once and forget.**

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/tamdogood/make-playbook>
> 指标：stars=5 · forks=1 · open_issues=0
> 作者：tamdogood　|　发布：2026-07-05T22:49:55Z
> 项目链接：<https://github.com/tamdogood/make-playbook>
> 采集：2026-09-20T09:36:29+08:00　|　id：`26919291295421de`

## 正文

# make-playbook

**A Claude Code skill that turns the indie-hacker playbook into something you actually consult while building — not another thing you read once and forget.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Idea → Build → Launch → Grow → Monetize → Automate → Exit.

Seven stages, seven checklists, one diagnostic system — install it once, and ask your agent for a stage-specific, tailored-to-your-app plan every time you're stuck, instead of re-deriving startup advice from scratch or scrolling Twitter for the hundredth time.

## Why this exists

Most "startup advice" is either a 300-page book you read once and never open again, or a tweet thread you can't find when you actually need it. `make-playbook` is neither — it's a small, structured knowledge base plus a workflow that tells your coding agent *how to use it on your specific project*, so the advice shows up exactly when you're stuck: mid-build, the morning of a launch, staring at a monetization decision, or wondering if you should even sell.

It's inspired by (not a copy of) [Pieter Levels' *MAKE: The Indie Maker Blueprint*](https://readmake.com) — the philosophy of solo, bootstrapped, fast-shipping, DIY-first app building. This repo distills that philosophy into original checklists, diagnostic questions, and a per-app tracker. **If you want the deep dives, the war stories, and the numbers behind it, buy the actual book** — this is a companion tool, not a replacement for it.

## What's inside

```
make-playbook/
├── SKILL.md                     # the entry point — workflow + stage diagnostic
├── references/
│   ├── ethos.md                 # the underlying philosophy (bootstrapping-first, ethics)
│   ├── idea.md                  # finding + sizing an idea worth building
│   ├── build.md                 # building fast, minimal, and mostly yourself
│   ├── launch.md                # pre-launch checklist + where/how to launch
│   ├── grow.md                  # organic growth, building in public
│   ├── monetize.md              # business models, pricing, payments
│   ├── automate.md              # what to automate, what to hand to a human
│   └── exit.md                  # buyer filtering, valuation, negotiation
└── templates/
    └── make-tracker.md          # a per-app MAKE.md tracker template
```

Each reference file ends with **diagnostic questions** designed to be asked *about your specific app*, not answered in the abstract — that's the difference between this and a summary you'd skim once.

## Install

This is a [Claude Code](https://claude.com/claude-code) skill. Drop it into your skills directory:

```bash
git clone https://github.com/tamdogood/make-playbook.git ~/.claude/skills/make-playbook
```

That makes it available in every project. Restart Claude Code (or start a new session), then invoke it directly:

```
/make-playbook
```

Or just talk about your app naturally — starting a new idea, prepping a launch, stuck on growth, deciding on pricing, wondering about automating support, weighing an acquisition offer — and it'll trigger on its own.

### Works with other agents too

The `SKILL.md` + `references/` structure is plain markdown with simple frontmatter. If your tool of choice supports a similar skills/knowledge-file convention (custom instructions, project docs, RAG over markdown), you can point it at this repo's `references/` folder directly.

## Example

```
you:    /make-playbook
        I've got a Chrome extension for freelancers that tracks billable
        hours automatically. Built it, nobody's used it yet.

agent:  Loads references/launch.md, asks where your specific audience of
        freelancers actually is (not just "Product Hunt"), walks the
        pre-launch checklist against your extension specifically, and
        ends with one concrete action: pick a launch date this week.
```

## The per-app tracker

For any real project, copy `templates/make-tracker.md` into the repo root as `MAKE.md` and let the agent keep it updated as you move through stages. It's the same idea/pipeline-tracking discipline the book itself recommends — Concepts → Promising → Building → Success/Failure — applied per-app instead of just in your head.

## A note on attribution

Everything in `references/` is an original synthesis — checklists and diagnostic questions built *around* the ideas in Pieter Levels' book, not excerpts or close paraphrasing of it. Facts and frameworks that are genuinely his (naming conventions, specific war stories, exact numbers from his businesses) live in the book, not here. If this repo is useful to you, the single best thing you can do is [buy MAKE](https://readmake.com) and follow [@levelsio](https://twitter.com/levelsio) — none of this exists without his writing it down first.

## Contributing

PRs that sharpen a checklist, add a missing diagnostic question, or improve the workflow logic in `SKILL.md` are welcome. PRs that re-introduce close paraphrasing or lengthy quotes from the book will be declined — keep contributions original.

## License

MIT for the skill/tooling structure in this repo (see [LICENSE](LICENSE)). See [NOTICE.md](NOTICE.md) for license scope and attribution — it does not extend to, and does not grant any rights over, the original book *MAKE: The Indie Maker Blueprint*, which remains the copyrighted work of its author.

## 关联链接

- https://claude.com/claude-code
- https://github.com/tamdogood/make-playbook.git
- https://img.shields.io/badge/license-MIT-blue.svg
- https://readmake.com
- https://twitter.com/levelsio

## 导航

- 项目页：[[10-项目/github.com_26919291]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
