---
type: "corpus"
item_id: "2eb1bd6aed76b6d0"
title: "Show HN: ArchLog – a memory for your team's engineering decisions"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50507860"
project_url: "https://archlog.dev/"
author: "ArchLog"
published_at: "2026-11-15T15:54:29Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_ArchLog
  - story_50507860
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: ArchLog – a memory for your team's engineering decisions

> [!info] 一句话导读
> ArchLog — Engineering Institutional Memory

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50507860>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ArchLog　|　发布：2026-11-15T15:54:29Z
> 项目链接：<https://archlog.dev/>
> 采集：2026-11-16T10:00:05+08:00　|　id：`2eb1bd6aed76b6d0`

## 正文

ArchLog — Engineering Institutional Memory

# Explore the context behind an engineering decision.

Engineering systems accumulate decisions, compromises, migrations, incidents and discussions. ArchLog connects that history across code, documentation and team conversations into a searchable engineering memory - so the reasoning survives longer than the people who made it.

Free to connect · Read-only by default · Nothing pushed without your approval

Decision Ledger entry

decision Decision

What was actually decided, stated in one line.

reason Reason

Why it made sense at the time - the part version control never keeps.

impact Impact

What changed as a result, in code and in operational behaviour.

risk · confidence Risk & confidence

How risky the change was, and how strongly the evidence supports the reading.

commits · pull requests Provenance

The commits, pull requests, authors and files the entry was derived from.

## Watch ArchLog turn a workspace’s history into a decision record.

Press play on a simulated workspace: GitHub, Slack and Linear connect, the history of one change—an incident, a Slack thread, commits and a reviewed pull request—streams in, and ArchLog links it into one Decision Ledger entry. Then it answers a question about that entry eight months later, citing every source.

1. 01 Connect
2. 02 Stream
3. 03 Analyze
4. 04 Ledger
5. 05 Ask

No sign-up required · Illustrative data · Pause, skip or ask your own questions

## Your code survives. Your reasoning doesn’t.

What gets lost isn’t the decision. It’s why the decision made sense. Version control preserves what changed; it rarely preserves why. When an engineer leaves, a system grows complex, or an incident forces a rewrite, the reasoning behind the original decision is usually the first thing lost - and the hardest thing to reconstruct.

- Why was this architecture chosen?
- What alternatives were considered, and why were they rejected?
- Why did we migrate authentication?
- What evidence supported the decision at the time?
- What changed after the incident?
- Who needs this context now that the author has left?

These are answerable questions. The evidence already exists - scattered across commits, pull requests, documents and threads nobody has time to read.

## Ask why. Follow the reasoning back to its source.

ArchLog doesn’t just answer what happened. It shows the decision, the context around it, and where each piece came from.

Simulation Simulated workspace · illustrative data · no real accounts connected

▶ Play Restart

1× 2× 4×

Skip to end

0:00 / 1:40

01 Connect 02 Stream 03 Analyze 04 Ledger 05 Ask

Press Play to watch ArchLog connect a simulated workspace, read its history as it arrives, and turn it into one Decision Ledger entry - then answer a question about it eight months later. About 100 seconds at 1×.

### Sources · Acme Payments (simulated)

- GitHub acme/payments-api Not connected
- Slack#payments-eng Not connected
- Linear Payments team Not connected

### Live feed 0 events

Events appear here once sources connect.

### Decision Ledger entry

No decision detected yet.

## Four stages, in the order they run.

1. 01

### Connect

Sign in with GitHub and connect the systems that already hold your engineering context - repositories, and optionally Slack, Notion and Linear. ArchLog reads them with your own OAuth tokens.
2. 02

### Capture

Commits, pull requests, discussions and documents are analyzed in one pass. The decisions that actually mattered are extracted into a structured Decision Ledger, linked to the code and conversations behind them.
3. 03

### Search

Ask why something is the way it is. Answers can include supporting decisions, commits, or documents. Check the sources and reasoning; AI answers can be incomplete or wrong.
4. 04

### Preserve

The reasoning stays with the organization, not the individual. When someone leaves, what they decided and why remains searchable by whoever inherits the system.

## A decision is a record, not a message in a thread.

Entries organize extracted reasoning, risk, people and affected code. Review the linked evidence for context the extraction may have missed.

- Risk and milestone flags surface the changes that mattered
- Authors, commits and affected files travel with the decision
- Extraction confidence is shown, never hidden behind a summary

payments-api / Decision Ledger

High risk Milestone Confidence 0.86

### Move settlement writes behind an idempotency key

Context

Retries during a provider outage double-charged 14 settlements.

Decision

Every write carries a caller-supplied key; replays return the original result.

3 commits PR #1284 7 files 2 authors

## A document goes stale. A repository does not.

ArchLog reads the system itself - the commits, the pull requests, the files that changed - so context stays attached to the code rather than to a wiki page nobody updated.

- Indexed directly from the repository, not transcribed by hand
- Re-indexed as the system changes
- Every claim links back to the file or commit it came from

Repository

acme/payments-api Indexed

1,204 files 38 decisions 6 milestones

- `src/settlement/writer.ts` 4 decisions
- `src/settlement/retry.ts` 2 decisions
- `migrations/0142_idempotency.sql` 1 decision

## Read a system's evolution in order.

Decisions are organised chronologically, so the shape of a migration - what was tried, what was reversed, what finally held - is legible instead of scattered across two years of pull requests.

- Chronological ledger per repository
- Milestones separated from routine change
- Reversals stay visible rather than being overwritten

Timeline

1. Mar 2026 Settlement writes made idempotent
2. Jan 2026 Retry backoff moved to the queue
3. Nov 2025 In-process retry loop — reversed
4. Aug 2025 Provider split into its own service

## Ask the codebase why.

Search spans decisions, files and connected sources at once. Results are typed and source-backed, so an answer can be followed to the thing that produced it.

- Decisions, files and sources in one result set
- Every result carries its origin
- Relevance is scored separately from extraction confidence

why do settlements retry?

- Decision Move settlement writes behind an idempotency key payments-api · PR #1284
- File`src/settlement/retry.ts` payments-api · indexed
- Decision Retry backoff moved to the queue payments-api · 3 commits

## Connect the systems that already hold the context

ArchLog reads the engineering systems your team already uses. Sources marked as planned are not available yet.

- GitHub Available Repositories, commits, pull requests
- Slack Available Channel discussions and decisions
- Notion Available Design docs, RFCs and specs
- Linear Available Issues, projects and cycles
- Jira Planned Not available yet
- Google Docs Planned Not available yet
- E Excel Planned Not available yet
- Zoom Meetings Planned Not available yet

## Engineering history is sensitive. It’s treated that way.

Your decisions, source context and team conversations are among the most sensitive data an engineering organization holds. Below is what ArchLog actually implements today - no certifications are claimed.

- ### Your own OAuth tokens

ArchLog reads only what you explicitly connect, using your own OAuth grant - and never pushes to your default branch on its own.
- ### Tokens encrypted at rest

Stored integration credentials use application-level encryption. Credentials must still be available to the service when it contacts providers.
- ### Authenticated, origin-scoped API

Account and workspace routes use session authentication. Session cookies are HttpOnly and SameSite=Lax, and marked Secure in production. Some public and provider-callback routes do not require a session.
- ### Verified OAuth and webhooks

Sign-in callbacks validate OAuth state, and supported webhook handlers check provider signatures. Review the requested provider permissions before connecting.

## Answers to what teams ask first

Does ArchLog store my source code?

ArchLog indexes structural metadata - file paths, imports, symbols, dependency graphs, and analysis results - in its own database. Generated documentation, patches, evidence and connected-source records can contain code or other source content. Relevant content may be sent to the configured AI provider.

What does ArchLog have access to?

Only what your OAuth tokens grant for the sources you explicitly connect. ArchLog never pushes to your default branch - patch suggestions are always proposed as a diff you review and approve, never applied automatically.

How is this different from asking an LLM about my code?

A raw LLM only sees the code you paste in, at that moment. ArchLog first builds a structured record of your engineering history, then uses that record to help explain engineering choices. Its interpretations still need your review.

Which languages does it support?

Structural analysis (imports, symbols, complexity) currently covers JavaScript/TypeScript and Python most deeply; the Decision Ledger, chat, and documentation features work across any language since they're driven by commit/PR history and file structure, not just per-language parsing.

What happens if I disconnect a source?

Disconnecting is not a data-deletion request. Previously stored records may remain; contact us about removing them.

## Keep the reasoning, not just the result.

Connect a repository and see what your own history has been trying to tell you.

## 导航

- 项目页：[[10-项目/archlog.dev_d15b8a21]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
