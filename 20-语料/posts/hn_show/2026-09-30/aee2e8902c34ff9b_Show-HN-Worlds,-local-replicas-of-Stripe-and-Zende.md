---
type: "corpus"
item_id: "aee2e8902c34ff9b"
title: "Show HN: Worlds, local replicas of Stripe and Zendesk for testing AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49897497"
project_url: "https://usesparta.co/"
author: "infra_snowman"
published_at: "2026-09-29T17:52:23Z"
captured_at: "2026-09-30T18:28:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_infra_snowman
  - story_49897497
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Worlds, local replicas of Stripe and Zendesk for testing AI agents

> [!info] 一句话导读
> WORLDS CATALOG DOCS BETA JOIN PUBLIC BETA

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49897497>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：infra_snowman　|　发布：2026-09-29T17:52:23Z
> 项目链接：<https://usesparta.co/>
> 采集：2026-09-30T18:28:30+08:00　|　id：`aee2e8902c34ff9b`

## 正文

WORLDS CATALOG DOCS BETA JOIN PUBLIC BETA
 Agent Testing Environments
 The frontier of agent verification.
 Transcripts are stories. Worlds reads the database. Run your agent against a sealed twin of the systems it touches and get exact, replayable proof of what it did.
 Join the public beta Stripe, Zendesk and combined workflows. Free internal testing during beta.
 ● BACKED BY A16Z
ALSO IN THE CATALOG
 Stripe Shopify Zendesk Salesforce
ILLUSTRATIVE WORKFLOW · MOCK DEMO
 Watch an agent work. Then grade what it did, not what it said.
 Worlds grades the state of the system after the run, not the transcript: what changed, what should have, and the dollars wrong per run. This synthetic example explains the workflow.
 All figures and traces are illustrative, not measured agent performance or API references.
 AGENT INVOICE AGENT STRIPE OFFBOARDING AGENT OKTA QUOTING AGENT SALESFORCE CLAIMS AGENT GUIDEWIRE
 FAILURES INJECTED NONE RATE LIMITS OUTAGES WEBHOOK CHAOS ▶ RUN RUN 1,000 TIMES
RESUME SKIP TO RESULT Playback speed 1× 2× 4× ADVANCE SUBSCRIPTION DAYS ↓
STEP 0 OF 12
 WHAT THE AGENT SAID
WHAT THE WORLD RECORDED
·
 STRIPE · EXAMPLE RUN VERDICT
Mock demo: the sessions and batch statistics are scripted examples, not measured results.
 ILLUSTRATIVE METRICS · ACROSS 1,000 RUNS
 ACTION ACCURACY 3.6%
 ACTIONS OUTSIDE THE TASK 2
 DROP UNDER FAILURES N/A
STRIPE · SUBSCRIPTION CLOCK
 Fast-forward a subscription.
 Advance the day and see renewals happen. This separate mock subscription bills $49 every 30 days. Payments succeed in this example; no real charges are made.
 SIMULATED TIME
 Day 0
 + 1 DAY + 7 DAYS + 30 DAYS RESET CLOCK
 Cancel at period end Time moves only when you advance it. Reset to try again.
STATUS Active
 PAID INVOICES 1
 TOTAL PAID $49
 Renews on day 30 · 30 days away
DAY 0 · Subscription started · $49 paid
 Latest events shown. Totals include every billing period.
WHAT YOU CAN DO
 Six things teams do with a world.
 Create it
 A world starts from a seed: the bundled sample account, or a pseudonymized copy of your own. It is ready in milliseconds and identical every time.
Mark it
 A mark records the world's state at that moment. Every diff is measured from a mark, so what your agent did is never mixed up with what was already there.
Let the agent act
 Point your agent's stock SDK at the world and hand it a ticket. Same URLs, same errors, same state machine. No code changes.
Read the diff
 See what changed since the mark: every refund, credit and cancellation, in dollars, and whose money moved. Replay any run byte for byte.
Break it
 Inject rate limits, 500s, lock timeouts, slow responses, an expired key and dropped webhooks. Find out whether your retry logic refunds twice.
Move its clock
 Advance 45 days and let renewals bill, prorations settle, cancellations resolve and webhooks fire in order. Then read the diff again.
HOW THIS IS DIFFERENT
 How Worlds fits with the tools you already use.
 Keep the tools that help you evaluate your agent. Add controlled system state and explicit outcome checks.
 EVAL PLATFORMS
 Eval platforms help inspect traces and evaluate outputs. Worlds supplies a local system the agent can act on and a record of the resulting state changes. Use that evidence alongside your existing evaluations.
MOCKS AND SANDBOXES
 Vendor test modes and sandboxes have different isolation, reset and simulation features. A world gives each test its own starting state, controllable failures and a logical clock, within the connector's documented scope.
CONVERSATION SIMULATORS
 Conversation tests exercise what an agent says to a customer. Worlds lets you check the records its actions change, including changes its reply never mentions.
SEE THE FULL COMPARISON
THE CATALOG
 Test the systems your agent uses.
 Each one is built to be reset, seeded and broken on purpose, and runs beside your agent, not inside it. When your agent says a task is done, Worlds diffs the environment and tells you what really changed.
 ● STRIPE AND ZENDESK BETA. REQUEST THE CONNECTOR YOUR TEAM NEEDS NEXT.
Stripe
 PAYMENTS & BILLING
 Public beta: the verified implemented billing and payments subset.
 INSTALL
Shopify
 COMMERCE
 Request Shopify support. Not included in this beta.
 INSTALL
Zendesk
 SUPPORT
 Public beta: native support workflows; live API qualification pending.
 INSTALL
Salesforce
 SALES & CRM
 Request Salesforce support. Not included in this beta.
 INSTALL
BROWSE THE CATALOG →
world 1
 /wərld/
 I. n. A working copy of a system your agent acts on. Same endpoints, same errors, same state machine. No real money and no real customers.
II. v. To run an agent somewhere its mistakes are free.
1 Also see: Sparta, where soldiers were tested before they were trusted.
© 2026 SPARTA · USESPARTA.CO
 CATALOG DOCS BETA TERMS PRIVACY SUPPORT LIMITATIONS RELEASES arya@usesparta.co

## 导航

- 项目页：[[10-项目/usesparta.co_0c27003a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
