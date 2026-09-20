---
type: "corpus"
item_id: "839bd0a844ccea68"
title: "Show HN: Brifly – stop re-explaining your codebase to Claude Code every week"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47960057"
project_url: "https://getbrifly.com/"
author: "dbarabashdev"
published_at: "2026-04-30T09:20:26Z"
captured_at: "2026-09-21T02:52:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_dbarabashdev
  - story_47960057
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Brifly – stop re-explaining your codebase to Claude Code every week

> [!info] 一句话导读
> Blog Sign in Request access Request early access

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47960057>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：dbarabashdev　|　发布：2026-04-30T09:20:26Z
> 项目链接：<https://getbrifly.com/>
> 采集：2026-09-21T02:52:29+08:00　|　id：`839bd0a844ccea68`

## 正文

Invite-only
 Blog Sign in Request access Request early access
Invite-only · Cohort 1 open
 Plan together. Delegate to agents.
 See what happened.
The workspace where your team aligns on what to build, hands it to AI coding agents, and keeps everyone in the loop — engineers, managers, PMs — in one place.
Request early access
01 · Plan together
 The workspace
Specs, RFCs, walkthroughs in one tree. Your whole team contributes before a line of code is written.
app.getbrifly.com
 architecture / auth
 RFC: Token rotation strategy
 Approved Architecture
 SC Sarah Chen
 Burn old token on rotate — no grace period .
MJ Maya Johnson
 We'll need server-side validation on every refresh.
02 · Hand off → 03 · Implement
 The CLI
Engineer pulls the approved context. The agent has the full picture from day one. Push the result back when done.
~/repo live
 $ brifly pull auth-rotation | claude
 ✓ context loaded · spec + 2 walkthroughs
 claude: implementing rotate per RFC...
 — burn old token
 — reject grace period requests with 401
 — emit token_theft_detected
 $ brifly push --pr 482
 → summary posted · team notified
04 · See the result
 The dashboard
Structured summaries — PRs, decisions, integration notes — written by the agent. Everyone in the loop without a standup.
This cycle's summary shipped
 PR #482 · Token rotation
 Burned old token on rotate, added 401 path, emits theft event. Aligned with RFC.
 C claude · 2 sources · 90 LOC
Decisions
 No grace period (per Sarah's review). Backfill on next deploy.
3 comments · 4 watchers
Plays nice with
The cycle One loop. Every cycle ships.
 From half-baked idea to shipped feature — without context loss between any of the humans or the agents.
01 phase
 web
 Plan
Write specs, attach videos, debate context — together.
 Whole team contributes
02 phase
 cli
 Hand off
Engineer pulls approved context via CLI to the agent.
 brifly pull
03 phase
 agent
 Implement
Claude Code, Cursor, or Codex builds with full context.
 No re-explaining
04 phase
 web
 See result
Engineer pushes a structured summary to the dashboard.
 brifly push
05 phase
 web
 Discuss
Comment with video, audio, text. Threaded per block.
 Next cycle starts informed
Next cycle starts where the last one ended — and again
The problem Your best plans die in Slack threads.
 Someone writes a great spec in a doc. Engineers never read it. The agent definitely never read it. Three weeks later, someone builds the wrong thing and everyone wonders why .
 Your engineer ships something brilliant. Your PM finds out in the standup two days later. The context lives in PRs. The decisions live in someone's head. The stakeholders live in spreadsheets.
 AI agents made coding faster. They didn't make teams more aligned.
How teams sync today Three habits. All three break.
Standups
15 minutes every day to learn what already happened.
 Half the team zones out. The PM takes notes nobody reads.
Slack updates
“Wrapped up the auth integration.” Cool — but what changed?
 No decisions logged. No context for the next person. The migration dependency is invisible until it breaks.
“Just ask them”
Your senior engineer is now a help desk.
 Every new hire, every PM, every manager walks over with the same question. The answer never gets written down.
There's a better loop. Your agents already have the context. Let them write the update. Your team reads it, discusses it, approves it. Next cycle starts where the last one ended.
How it works Two surfaces. One source of truth.
 Your team plans on the web. Your engineers and their agents read and write through the CLI. Same tree. Same context. No copy-pasting between tools.
For your team Web platform
Write plans, specs, context — tree structure, not flat docs.
 Add video, audio, or text comments to any paragraph.
 Discussion threads per block. Resolve and move on.
 AI chat searches the whole tree — “what did we decide about auth?”
 Version history, diffs, who changed what.
 Public sharing, workspaces, invite your team.
For your engineers CLI
$ brifly pull auth-rotation Get approved context. Hand it to the agent.
 $ brifly push --pr 482 Send PR summaries, decisions, integration notes back.
 $ brifly query "what did we decide?" Ask anything across the whole tree from your terminal.
 Works inside Claude Code , Cursor , and Codex . No extra docs to write — the agent does the summarizing.
Live preview
 Pull context to your agent
 Hand the approved spec straight to Claude Code, Cursor, or Codex.
 Push the result back
 Agent pushes a structured summary so the team sees what happened.
 Browse the tree
 See your whole context as a tree — specs, RFCs, runbooks.
~/brifly · pull live
 $
Who it's for Built for the people who already work together.
 Engineers, managers, PMs, leadership — one workspace, one cycle, one source of truth.
Engineering managers 0 1 Stop asking “what happened?”
 Every cycle ends with a structured summary. PRs, decisions, integration notes — visible without a standup.
 Before Slack threads + 1:1s
After A live dashboard
This week · 3 cycles shipped
 PR # 482 · Token rotation
 90 LOC · summarized
shipped
 PR # 479 · Webhook retry queue
 142 LOC · summarized
shipped
 PR # 475 · OAuth providers
 210 LOC · summarized
shipped
PMs & designers 0 2 Write context once. Every agent reads it.
 Add video walkthroughs and acceptance criteria once — they travel with the work, all the way to the agent.
 Before Specs in dead docs
After Specs the agent reads
specs / payments-flow
 Acceptance criteria
 User sees error toast on declined card
Retry preserves form state
AL Anna · 1m walkthrough
“Here's the empty state I want…”
Engineers 0 3 Push once. The team sees everything.
 No more writing docs for non-technical stakeholders. Your agent summarizes; the dashboard tells the rest.
 Before Status updates × N
After brifly push
~/repo
 $ brifly pull payments-flow
 ✓ spec + 1 walkthrough loaded
 $ brifly push --pr 491
 → summary posted
 → team notified · 4 watchers
 No docs to write.
Leadership 0 4 Share a link, not a standup recap.
 Drop in any time. See what shipped, what changed, what the team decided — without scheduling a meeting.
 Before Weekly sync calls
After A live shareable link
getbrifly.com/share/q3-launch
 Q3 launch · status
 12
 Shipped
4
 In flight
0
 Blocked
Last update · 2 min ago
How it compares Three habits everyone uses.
 One loop that actually scales.
Capability Standups Slack "Just ask them" You Brifly
 Real-time Real-time Partial
 Written by Written by Human Human Nobody Agent + team
 Current Stays current
 Non-eng Works for non-engineers Partial
 Agent-readable Agent can read it
 Anchored Anchored to the work
 AI chat AI chat on full context Partial
Stop syncing. Start building.
 One workspace. Every agent. Every teammate.
Cohort 1 · open Onboarding the first cohort.
 We onboard teams in small cohorts — not to create scarcity, but because we set up every team properly before they go deep. You'll get a setup call, a starter tree built for your stack, and a direct line to us while we're small.
 We're looking for teams actively using Claude Code, Cursor, or Codex who have felt the alignment problem firsthand.
Name
 Work email
 Tell us about your team
 Company website (leave empty)
Request early access We'll follow up within 48 hours. No sales process.
One workspace. Every agent. Every teammate.
 Blog Terms Privacy Cookies © 2026 Brifly

## 导航

- 项目页：[[10-项目/getbrifly.com_d9c887d2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
