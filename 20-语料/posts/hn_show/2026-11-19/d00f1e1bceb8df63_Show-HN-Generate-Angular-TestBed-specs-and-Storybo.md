---
type: "corpus"
item_id: "d00f1e1bceb8df63"
title: "Show HN: Generate Angular TestBed specs and Storybook stories locally, no LLM"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50554425"
project_url: "https://sshyeri.github.io/ng-test-foundry-public"
author: "sshyeri"
published_at: "2026-11-19T00:35:27Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_sshyeri
  - story_50554425
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Generate Angular TestBed specs and Storybook stories locally, no LLM

> [!info] 一句话导读
> Generate Angular specs and stories locally.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50554425>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：sshyeri　|　发布：2026-11-19T00:35:27Z
> 项目链接：<https://sshyeri.github.io/ng-test-foundry-public>
> 采集：2026-11-19T09:43:31+08:00　|　id：`d00f1e1bceb8df63`

## 正文

</>
 ngTestFoundry
Features
 Free vs Pro
 Limits
 Feedback
v0.1.1 is live
 Generate Angular specs and stories locally.
ngTestFoundry is a VS Code extension that creates deterministic
 first drafts of Angular TestBed specs and CSF3 Storybook stories
 from component source.
Install from Marketplace
Open VSX
Give feedback
Read launch write-up
View example output
Local-only generation for modern Angular components. No component
 source is sent to a server.
Built for the boring first draft.
The goal is not magic. The goal is a useful, repeatable starting
 point that developers can review and adapt like normal code.
TestBed specs
Generate `.spec.ts` scaffolds with component imports, shallow
 providers, required inputs, and basic creation assertions.
Storybook stories
Generate CSF3 `.stories.ts` files with inferred args from
 component inputs and outputs.
Modern Angular
Best fit for standalone components using `input()`, `model()`,
 `output()`, `inject()`, `@Input()`, and `@Output()`.
Free for one component. Pro for workflow scale.
Free
Use the core generator on the active Angular component.
Generate one spec from the active component.
Generate one story from the active component.
Local-only static analysis.
Pro
Use ngTestFoundry across larger workspaces and team styles.
Batch-generate specs across a workspace.
Batch-generate stories across a workspace.
Override output with custom Eta templates.
Honest limits.
ngTestFoundry prefers explicit TODOs over silent guessing. Today it
 is strongest on Angular 17.3+ standalone components.
Current limits:
- Non-standalone NgModule graph resolution is planned.
- Dependency mocks are shallow.
- Vitest output is planned.
Try it on one real component.
The most useful feedback is whether the generated TestBed shape
 works in an actual Angular workspace.
Share generated output feedback
See the generated shape first.
Before installing, you can inspect a real example of the generated
 TestBed spec and Storybook story, including the TODOs ngTestFoundry
 leaves when static analysis should not guess.
Open example output
Launch write-up
A short explanation of why ngTestFoundry exists, what it supports
 today, what it generates, and what feedback would help most.
Read launch note
Read generated output note
Public docs and support:
github.com/sshyeri/ng-test-foundry-public

## 导航

- 项目页：[[10-项目/sshyeri.github.io_a96b5efb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
