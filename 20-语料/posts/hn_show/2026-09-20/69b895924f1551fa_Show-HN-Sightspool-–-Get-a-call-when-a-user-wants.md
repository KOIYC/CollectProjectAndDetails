---
type: "corpus"
item_id: "69b895924f1551fa"
title: "Show HN: Sightspool – Get a call when a user wants to talk"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49724204"
project_url: "https://sightspool.com/"
author: "capex"
published_at: "2026-09-16T10:01:47Z"
captured_at: "2026-09-20T09:37:05+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_capex
  - story_49724204
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Sightspool – Get a call when a user wants to talk

> [!info] 一句话导读
> Sightspool — your product team's embedded researcher

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49724204>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：capex　|　发布：2026-09-16T10:01:47Z
> 项目链接：<https://sightspool.com/>
> 采集：2026-09-20T09:37:05+08:00　|　id：`69b895924f1551fa`

## 正文

Sightspool — your product team's embedded researcher

# Talk to users, effortlessly.

Find what to ask. Hear from your users. Know what to do next.

See your first question before signing up. No account or credit card required.

Illustrative example

A question about Sightspool

## What stops founders joining user interviews?

Behaviour + conversations

Bring the conversation to the founder.

Next move to explore Call the founder’s mobile.

06 Bring the evidence into your next move.

Read Journey Question Invite Listen Next move

An illustrative story, not a live study. Sightspool combines public product pages with connected sources such as PostHog, Amplitude and GitHub. Journey Canvas places behaviour against the product journey. Fictional example counts fall from 100 ready users to 40 founder joins and 35 interviews, highlighting a drop-off before the founder joins. These are example counts, not Sightspool customer data. The behaviour shows where to investigate, not why it happens. Sightspool proposes a research question: What stops founders joining user interviews? You review and approve the plan, then relevant founders choose whether to join. You lead the interview using your approved plan. An example founder says, “I’m not always at my laptop.” Bringing that conversation together with the observed drop-off suggests a next move to explore: call the founder’s mobile when a user is ready to talk. This is an idea to test, not a proven explanation or outcome. The animation loops continuously; pause, replay or select any step. With reduced motion, choose a step to read it without animation.

Works with your existing sources

- PostHog
- Amplitude
- Stripe
- GitHub

## A good question changes what you build.

We turn product context and user behaviour into focused questions for the right users. You join the conversation and learn directly from the people using your product.

Assumption Insight Next move Build better

Context via journey canvas Behaviour Cohort selection Questions

Your approval Invite Talk Question answered

We connect the context, shape the questions and make sense of what you learn, then check what changed. Outer loop: Assumption, Insight, Next move, Build better. Middle loop: Context via journey canvas, Behaviour, Cohort selection, Questions. Inner loop: Your approval, Invite, Talk, Question answered.

### We connect behaviour to context.

We connect user behaviour to your product journey to spot hesitation and find the people who can help explain it.

### We ask about real experience.

We draft questions about what users actually did, what they tried and what got in their way, giving you a useful starting point for the conversation.

### We keep questions focused.

We keep each question short and direct, one thing at a time, with room for users to explain what happened in their own words.

### Then talk to your users.

We handle the preparation, so you can spend your time listening, asking follow-ups and learning from your users.

A little time. A different perspective.

## Introducing user hours.

Make room for real conversations.

We strongly recommend talking to your users yourself. Hear the hesitation, ask a follow-up question, and understand what matters to them. There’s no substitute for being in that conversation.

### Make time to talk

Set your user hours. When a user is ready, join from your dashboard and lead the conversation yourself. The Founder launch plan also includes calls to eligible verified numbers.

### Take calls away from your desk

Attend calls from your Sightspool dashboard or on your phone. When you are away from your desk, we’ll call your verified mobile number so you can still talk to users.

A moment to talk. A person to understand.

From a conversation

> “I wanted to try it myself before inviting the whole team.”

Example interview · First project setup

An emerging insight

Make space to explore solo.

A direction to investigate in the next conversation.

Every insight stays connected to the conversation behind it, so you can hear the context before deciding what to change.

## Your product journey. With real user data.

Works with your existing sources

- PostHog
- Amplitude
- Stripe
- GitHub

Start with a map of your product’s journey. Connect PostHog and link events to its steps to see who moves forward and who doesn’t. Turn those gaps into focused research questions, then hear from the people behind them.

Your team’s first project Illustrative example

Drag the canvas · select a step

PostHog connected

Illustrative connection · example data

01 Discover the product 02 Create a first project 03 Invite a teammate 04 Work together

Invite a teammate: 70 founders reached this step, 42 progressed, 28 in the suggested research cohort. Illustrative numbers.

### Invite a teammate

Example cohort · 200 new founders First 7 days after signup

Reached this step

70 founders

Reached the next step

42 60% of 70

Not yet onward

28 people to learn from

42 of 70 reached “Work together” by day seven. Example event: Invite step opened

A question for the 28

#### What gets in the way of bringing a teammate into the first project?

28 founders reached the invite step without getting to shared work. An unsent invitation, a pending reply or something else could be involved—we need to ask.

Who to hear from

Founders who reached the invite step but had no shared project activity in their first seven days.

> “Walk me through what happened when you reached the invite step.”

Illustrative cohort, events and questions—not live customer data. Counts show what happened; conversations help explain why.

## Talk to trust

Inviting us into your product deserves a closer look. Here’s what the SDK does—and the evidence you can check before installing it.

### A small SDK for approved research.

Install with a script tag or npm. Choose all visitors or signed-in users. The SDK checks for an approved invitation, then opens Sightspool for consent and the interview when someone chooses to join.

- No page content, form values, clicks or browsing history captured by this SDK.
- If you supply a user ID, the SDK sends it with invitation checks so Sightspool can match an approved cohort.
- Pause or destroy the SDK to stop invitation requests and remove the launcher.

 Before someone joins Example without a user ID

POST /widget-offer

```
{
  "operation": "offer",
  "key": "your-workspace-uuid",
  "device": "random-session-id"
}
```

The random identifier uses browser session storage. A supplied user ID adds an identity field. Ordinary network metadata, including IP address and website origin, also reaches the service.

SDK 0.6.5 19.6 kB browser bundle 0 runtime dependencies

#### Code you can inspect

The SDK source is public. Read the implementation behind the data-handling claims.

Inspect the released source

#### A release you can verify

npm provenance links the package to its source and build workflow. Script integrity checks protect the reviewed bundle’s bytes.

#### Controls you can understand

See what is sent and stored, how participants consent, and what pausing, removal and withdrawal actually do.

Sightspool is operated by Cumulative Consulting Pty Ltd. Ask a security question (security@sightspool.com).

## Your first interview. On us.

Start free. Continue with Founder for US$29 a month: one founder, one product workspace and one active research question at a time.

Interview your own users. Join in your browser or on an eligible phone. See included phone minutes

See what your product still needs to learn

$0 to start

01

First interview included with Free

Find the question before you pay for the research.

- One founder in one product workspace
- One bounded read of your public product
- One approved question and learning brief
- Your first completed founder-led interview
- Transcript and one emerging insight

One interview is an honest starting point, not a supported pattern. Ongoing monitoring and further interviews begin on a paid plan.

### Founder

For a founder working through one important decision

$29/ month

Keep one focused research loop moving each month.

- One founder in one product workspace
- Unlimited questions in your maintained Question Stack
- 120 founder interview minutes shared across browser and phone
- Up to 60 minutes by phone on Australian mobiles, or 120 on eligible US numbers, within your 120 total founder interview minutes.
- One active question; subsequent questions share the monthly pools
- Weekly monitoring and analysis across all connected sources
- One evidence-backed next move and an outcome check

The same complete analysis across paid plans. Review phone eligibility and browser instructions before subscribing. Full plan details

### Does a scan start research automatically?

All Founder inclusions, phone coverage and calling instructions

## Hear from your next user.

Start with your public website. Your first question is waiting to be found.

We work on Ngunnawal Country in Canberra. We honour the Ngunnawal people as Traditional Custodians and pay our respects to Elders past and present. We also recognise the enduring connections of other Aboriginal and Torres Strait Islander people and families to this region.

# selemis-com/kival

## 导航

- 项目页：[[10-项目/sightspool.com_c1ecc207]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
