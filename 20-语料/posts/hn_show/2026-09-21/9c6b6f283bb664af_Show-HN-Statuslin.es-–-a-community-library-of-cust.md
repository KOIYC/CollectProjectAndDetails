---
type: "corpus"
item_id: "9c6b6f283bb664af"
title: "Show HN: Statuslin.es – a community library of custom Claude Code status lines"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48732336"
project_url: "https://statuslin.es/"
author: "nastynate"
published_at: "2026-06-30T13:15:39Z"
captured_at: "2026-09-21T02:53:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_nastynate
  - story_48732336
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Statuslin.es – a community library of custom Claude Code status lines

> [!info] 一句话导读
> statuslin . es Guide Resources Sign in with GitHub

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48732336>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：nastynate　|　发布：2026-06-30T13:15:39Z
> 项目链接：<https://statuslin.es/>
> 采集：2026-09-21T02:53:05+08:00　|　id：`9c6b6f283bb664af`

## 正文

statuslin . es Guide Resources Sign in with GitHub
 statuslin . es
 A community gallery of reviewed Claude Code status lines. Every card is a real script, sandbox-rendered against the same example sessions, so you can see it before you copy it.
 To wire one up yourself, read the setup guide .
Browse by feature:
 Git Tokens Cost Limits Burn Rate Minimal Multi-Line Themed Bash Python Node
Status lines
 Sort: Trending Filter
 Submit a status line
 Dreambase Panel
 193 copies
Git Tokens Cost Multi-Line Python
╭─ CONTEXT ────────────────────────────────────────────╮
 │ ████▊░░░░░░░░░░░░░░░░░ 22% of 200K · GOOD │
 ├─ STATS ──────────────────────────────────────────────┤
 │ ↓ 44.0K ↑ 1.4K │ $0.41 │ ⏱ 10m 12s │ +128 / -34 │
 ├─ REPO ───────────────────────────────────────────────┤
 │ ◆ Opus 4.8 · main · 16:21 │
 ╰──────────────────────────────────────────────────────╯
A boxed multi-line panel with auto-sizing borders: a context section with a gradient bar and status word, a stats section (tokens, cost, duration, lines changed), and a repo section (model, git branch with file counts, clock, vim mode), in a terracotta Claude-brand palette.
 @ kyleledbetter
Single-line usage
 117 copies
Git Tokens Limits Bash
app · main · Opus-4.8 · effort high · ctx 22% · 5h 26% ↻2h6m · 7d 7% ↻2d0h
 One-line status bar showing your directory, git branch (with a * when dirty), model, live effort level, context-window usage, and 5-hour/7-day rate-limit usage.
 @ NathanAB
Pace Dot Meters
 84 copies
Git Tokens Cost Limits Burn Rate Multi-Line Bash
Opus 4.8 [high] ~/app main
 16:20:55 | ⛁ ██░░░░░░░░ 22% | 5h ●◔○○○ 26% ↻2h7m | 7d ◔○○○○○○ 7% ↻2d1h │ $0.41 ⏱ 10m
Two-line status with a block context bar and quarter-step dot meters (◔◑◕●) for the 5-hour and weekly limits (fill shows usage, color shows whether you are ahead of or behind pace), plus model, effort, git and cost. Needs no jq.
 @ AndrewP-GH
Dreambase Flat
 52 copies
Git Tokens Cost Python
████▊░░░░░░░░░░░░░░░░░ 22% of 200K · GOOD │ ↓ 44.0K ↑ 1.4K │ $0.41 │ ⏱ 10m 12s │ +128 / -34 │ ◆ Opus 4.8 · main · 16:22
One-line adaptation of @kyleledbetter's Dreambase Panel: a context bar with status word, token/cost/duration/lines-changed stats, and model + git branch + clock, all on a single line in a terracotta Claude-brand palette.
 @ lababidi
Catppuccin Frappé
 54 copies
Git Tokens Cost Themed Bash Network Access
Opus 4.8 │ main │ app │ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ 44k/200k │ $0.41
Catppuccin Frappé-themed status line with model, git branch and dirty flag, folder, a block context bar, and session cost.
 @ danjdewhurst
Activity Feed
 47 copies
Git Tokens Cost Limits Burn Rate Multi-Line Bash Network Access Reads Token
Opus 4.8 high ✦ │ ctx 22% │ app (main) │ PR #1287 ● │ $0.41 · 10m +128 -34
 Session ● ● ● ● ● ● ● ● ○ ○ ○ 74% left Resets in 2h 6m
 Weekly ● ● ● ● ● ● ● ● ● ● ○ 93% left Resets in 2d 0h
 Fable ● ● ● ● ● ● ● ● ● ○ ○ 85% left Resets in 2d 0h
 ◐ Read:index.ts ✓ Read×1 ✓ Bash×1 ✓ Edit×1 ✓ Grep×1
 ◐ code-reviewer Review the change for regressions
A header with model, context and burn rate per hour, then live tool and agent activity parsed from the session transcript.
 @ JungHoonGhae
Powerline Dracula
 19 copies
Git Tokens Powerline Themed Bash
 app   main   Opus 4.8  ━━ ━ ━ ━ ━ ━ ━ ━ ━ 22%   128  34    
A Powerline-style status line with nerd-font separators and a Dracula palette: colored directory, git branch, a per-model icon, and a faded context progress bar with an arrow tail.
 @ LindseyB
One Dark Triptych
 6 copies
Git Tokens Cost Limits Weather Multi-Line Themed Bash Network Access
Model: Opus 4.8 | Thinking: high | Context: [▰▰▱▱▱▱▱▱▱▱] 45k/200k (22%) | cwd: ~/app | ⎇ main | (+0,-0)
 Cost: $0.41 | Block: 2hr 6m | Weekly: 7.0% | Session: 10m | In: 916.7 t/s | Out: 29.2 t/s | Cached: 2k | Session: [▰▱▱▱▱] 26.0%
 Mem: 0.8G/1.0G | (*ﾟ∀ﾟ*) | Session ID: b8e1c0d2-4a6f-4e2a-9c1b-3f5d7a9e2c10
Three lines in One Dark: model, thinking effort and a context bar up top; cost, quota, session clock and token throughput in the middle; weather, free memory and a rotating kaomoji below.
 @ adrijshikhar
Color-Coded Context
 32 copies
Git Tokens Limits Node
◆ Opus 4.8 │ ▪ app │ ⎇ main │ ◷ 16:20 │ █ █ ▄ ░ ░ ░ ░ ░ ░ ░ 26% (44K/167K) │ 26% ↻2h6m │ 7% ⟳2d0h
 Node status line with an autocompact-aware context bar (subtracts the compaction buffer), project, branch, last-activity time, and 5h/7d rate-limit segments.
 @ philipshurpik
Everything Bar
 16 copies
Git Tokens Limits Minimal Bash Network Access Reads Token
Opus 4.8 | app @ main | 44k/200k ( 22% ) | effort: high | 5h 26% @18:59 | 7d 7% @Sat Aug 1, 17:52
 Model, directory and branch with diff counts, context tokens, reasoning effort, and five-hour and seven-day limits from Claude Code's own rate-limit data, with the usage API as fallback. Checks for new versions of itself once a day.
 @ daniel3303
Page 1 of 4
 Next →
 35 published status lines, copied 703 times as of Sep 20, 2026 .
 A gallery of scripts you paste into Claude Code, not a TUI installer.
GitHub · Email · Guide · Resources · Terms

## 导航

- 项目页：[[10-项目/statuslin.es_3a3d04f5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
