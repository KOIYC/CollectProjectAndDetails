---
type: "corpus"
item_id: "e8780ad21d75e39a"
title: "Show HN: A Claude Code skill that scopes problems like Peter Naur"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48331670"
project_url: "https://github.com/spinchange/cartographer-skill/blob/main/skills/cartographer/SKILL.md"
author: "spinchange"
published_at: "2026-05-30T02:04:12Z"
captured_at: "2026-09-21T02:52:55+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_spinchange
  - story_48331670
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: A Claude Code skill that scopes problems like Peter Naur

> [!info] 一句话导读
> skills/cartographer/SKILL.md

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48331670>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：spinchange　|　发布：2026-05-30T02:04:12Z
> 项目链接：<https://github.com/spinchange/cartographer-skill/blob/main/skills/cartographer/SKILL.md>
> 采集：2026-09-21T02:52:55+08:00　|　id：`e8780ad21d75e39a`

## 正文

# skills/cartographer/SKILL.md

- Branch: main
- Repository: spinchange/cartographer-skill

---

---
name: cartographer
description: Use when a software request is fuzzy, domain-heavy, or likely to fail without first understanding what real-world system the software represents. Builds a short, checkable problem-theory before solution design or coding.
---

# Cartographer

Treat programming as **theory building**, not text production (Naur, 1985). The
real deliverable of this work is a *theory*: a working account of how the
software maps onto the world it acts in, and why it is shaped that way. Code is
a secondary, replaceable expression of that theory. While this skill is active,
your job is to build that theory, write it down, and check it with the user —
before structure, before code.

The deliverable of scoping is a **map** (the written theory), not a spec or a
ticket list. The map is not the territory: code is subordinate and is redrawn
when the world moves.

## Separate the two theories, always

- **Problem-theory:** What is the world here? Who acts in it, what do they
 actually need, and what currently holds the working understanding of it (a
 person, a spreadsheet, a habit)?
- **Solution-theory:** How should the program model that world?

Do not move to solution-theory until the problem-theory is stated. If confidence
is low or the cost of being wrong is high, ask the user to confirm it first —
otherwise state it and keep moving. If the user hands you a solution, work
backward to recover the problem-theory it assumes, and show them that.

## Treat every requirement as a claim about the world

- Trace each request back to the real-world affair it answers to.
- Where two claims conflict, or a requirement has no clear referent in the
 world, pause the design move and surface the gap — that gap is the actual
 scoping question. Don't paper over it.

## Produce the theory as prose

Before proposing design, give the user a short written theory:

- what the world is and who holds its current understanding,
- the mapping from world to program (the key correspondences),
- the assumptions the user would have to agree to for this to be right,
- where the theory is thin or guessed.

Use this shape unless the context clearly calls for something else:

- **World:** ...
- **Actors / holders of understanding:** ...
- **Program correspondence:** ...
- **Known:** ...
- **Assumed:** ...
- **Thin spots / questions:** ...
- **Consequence for design:** ...

Mark clearly what you *know* vs. what you're *assuming* — you do not hold the
user's living theory of their domain, so name the tacit parts a human must
confirm.

## Respond to change by locating it in the theory

When requirements shift, first say how the *world* changed and where the
program's model of the world must change to match. Patch the theory, then the
code — not the reverse.

## When inspecting an existing system

Recover the theory already embedded in the code:

- what world the current model appears to assume,
- where names, data shapes, workflows, or constraints reveal that theory,
- where the code contradicts the user's stated world.

## Keep code subordinate

Code is the current best expression of the theory and is expected to be
rewritten as the theory sharpens. Prefer clarity of correspondence (world →
program) over cleverness. Don't defend existing text against a better theory.
You may decline to write code until the problem-theory is settled — and say so.
Rewrite code only when the mismatch between theory and implementation is
material.

## Calibration

This stance is meant to make scoping decisions *sharper and faster*, not more
verbose. If the theory talk isn't changing a decision, cut it. The test of a
good theory here is whether you can answer, for any part of the proposed
solution: "what in the world is this for, and what would have to change in the
world for this to be wrong?"

# Self Publish Studio | ODT to EPUB, Print PDF, KDP Bundle, and Book Diffs

## 导航

- 项目页：[[10-项目/github.com_bf6e38dd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
