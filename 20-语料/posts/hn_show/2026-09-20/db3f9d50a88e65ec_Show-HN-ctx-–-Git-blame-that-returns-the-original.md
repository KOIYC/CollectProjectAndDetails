---
type: "corpus"
item_id: "db3f9d50a88e65ec"
title: "Show HN: ctx – Git blame that returns the original agent transcript"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49727859"
project_url: "https://ctx.rs/pro"
author: "luca-ctx"
published_at: "2026-09-16T14:46:13Z"
captured_at: "2026-09-20T14:04:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_luca-ctx
  - story_49727859
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: ctx – Git blame that returns the original agent transcript

> [!info] 一句话导读
> ctx pro: git blame, but for agent sessions - ctx

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49727859>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：luca-ctx　|　发布：2026-09-16T14:46:13Z
> 项目链接：<https://ctx.rs/pro>
> 采集：2026-09-20T14:04:09+08:00　|　id：`db3f9d50a88e65ec`

## 正文

ctx pro: git blame, but for agent sessions - ctx

# ctx pro: git blame, but for agent sessions

Map a line, file, commit, or PR back to the coding-agent session that produced it, with citations to the original transcript and tool calls.

`git blame` tells you which commit last changed a line. `ctx blame` tells you which agent session produced that commit, with exact citations back to the original transcript and recorded tool calls.

Agents use `ctx blame` to recover context that no longer exists anywhere near the current session. Starting from a file, line range, commit, or PR, they can find the relevant historical agent sessions and recover the decisions, constraints, failed approaches, and assumptions recorded there.

This helps agents:

- recover constraints and decisions no longer visible in the code
- uncover assumptions embedded in earlier changes
- avoid retrying approaches that already failed
- resume work without relying on lossy compaction summaries
- audit past agent work to improve instructions, tools, and workflows

Every attribution includes citations back to the original transcript and tool calls. If the session is not on your machine (for example, because a teammate's agent produced the code), ctx says it cannot prove the attribution.

```
# Your agent is investigating why customized cart items
# are disappearing from your e-commerce app.
$ ctx blame file src/checkout.ts --lines 118:146

# ctx blame finds the agent session that produced those lines:
# Lines 118–146
#   commit    8f3c2a1
#   Produced by
#     session   c0297b8a-2ad7-4f73-a826-8ee9387cd1f4
#     evidence  [1] [2]

# Your agent opens the transcript of the session that produced the offending commit
$ ctx show session c0297b8a-2ad7-4f73-a826-8ee9387cd1f4

# Previous agent — transcript excerpt
"Some responses contain multiple cart lines with the same product_id.
I'm treating those as duplicates and merging them before calculating the total."

# Your agent finds the mistake
"FOUND IT: The previous agent treated matching product_ids as duplicate cart lines.
Customized items can share a product ID, so that merge drops valid items."
```

`ctx blame` can also start from a commit or PR:

```
ctx blame commit <sha>
ctx blame pr https://github.com/your-org/your-repo/pull/42
```

Like ctx indexing and search capabilities, blame runs locally, so your code and history never leave your machine.

ctx pro is $20 USD per month, but you can try it for free for two weeks with no account or credit card required.

New to ctx? Install ctx. Eligible fresh interactive installs start the free ctx pro trial automatically.

Already use ctx? Set up pro:

```
ctx pro
```

## Refer another developer

For each developer you refer who becomes a ctx pro subscriber, you earn $10 cash per month for each of their first 12 paid months. The developer you refer receives a 30-day trial instead of the standard 14 days.

See the referral program for the commands, eligibility, payouts, and terms.

On this page

1. Refer another developer

# Social Reps: block Instagram until you do your push-ups

## 评论（2/2）

> **TomEleff** · 2026-09-16T16:49:00.000Z　
> Looks neat, Luca - Definitely like the idea. I struggle with the paywall though... Saving 50x the tokens for a task I do 1-2 a week is not worth doubling my budget for vibe coding, particularly if I only have access to my own sessions.Have you looked at monetizing a cloud service instead? A managed cloud service that indexes my entire team's sessions allowing for team-wide agent blame would be genuinely useful. It also targets customers that can pay, enterprises, not individual developers. Coding CLIs already have log exporting, like `OTEL_LOGS_EXPORTER` for Claude Code that will send chat info to another aggregation service via the OpenTelemetry protocol.

---

> **luca-ctx** · 2026-09-16T18:08:18.000Z　
> Yes we are actually piloting this now! Could you shoot me an email if you want to chat further about it? luca@ctx.rs

## 关联链接

- https://github.com/your-org/your-repo/pull/42

## 导航

- 项目页：[[10-项目/ctx.rs_1079dc98]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
