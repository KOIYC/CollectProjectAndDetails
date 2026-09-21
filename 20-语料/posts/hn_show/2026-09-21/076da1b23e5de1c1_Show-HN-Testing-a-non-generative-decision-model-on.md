---
type: "corpus"
item_id: "076da1b23e5de1c1"
title: "Show HN: Testing a non-generative decision model on 5,500 CLINC150 inputs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49778191"
project_url: "https://github.com/chr-kelly/jev-cookbook"
author: "tgdhtdujeytd"
published_at: "2026-09-20T17:55:21Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_tgdhtdujeytd
  - story_49778191
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Testing a non-generative decision model on 5,500 CLINC150 inputs

> [!info] 一句话导读
> chr-kelly/jev-cookbook

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49778191>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：tgdhtdujeytd　|　发布：2026-09-20T17:55:21Z
> 项目链接：<https://github.com/chr-kelly/jev-cookbook>
> 采集：2026-09-21T09:44:03+08:00　|　id：`076da1b23e5de1c1`

## 正文

# chr-kelly/jev-cookbook

Runnable question sets for TypeSafe's Jev, an eval harness with measured CLINC150 results, and a linter for the request shapes the API silently mis-reads.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-20T17:21:07Z

## Languages

- Python

## Top Contributors

- chr-kelly (1 contributions)

---

## README

# Jev Cookbook

### Stop guessing what Jev is for.

**Describe your decision. Copy working questions. Run them now.**

Runnable question sets for TypeSafe's Jev — not a link list.

---

## The problem

Jev is fast, cheap and typed. Everyone agrees on that by now.

The part nobody tells you is **what to actually ask it**. The docs show you the
three primitives. The awesome-lists show you what other people built. Neither
tells you how to turn *your* judgement into a question set that holds up on real
data.

That gap is where this repo lives.

## 10-second example

```json
{
  "model": "jev-latest",
  "state": "Hi, I ordered the blue one three weeks ago and it still hasn't shipped. This is the second time I'm writing. Can someone just refund me?",
  "questions": {
    "category": {
      "type": "choice",
      "instructions": "What is the single primary topic of this message?",
      "criteria": {
        "SHIPPING": "where an order is, delays, delivery problems",
        "REFUND":   "wants money back",
        "BILLING":  "charges, invoices, payment methods",
        "OTHER":    "none of the above fits"
      }
    },
    "wants_refund":   { "type": "noul", "instructions": "Does the writer explicitly ask for money back?" },
    "repeat_contact": { "type": "noul", "instructions": "Does the writer say they have contacted support before about this?" },
    "urgency": {
      "type": "score",
      "instructions": "How urgently should a human look at this?",
      "criteria": ["can wait a week", "this week", "today", "someone is blocked right now"]
    }
  }
}
```

```
POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer $TYPESAFE_API_KEY
```

One call. Every question answered in parallel, each with a confidence you can
branch on. No parsing, no retries, no "please respond with valid JSON".

**The shapes, because they are easy to get wrong:** `choice` criteria is a map
of *option → description* (up to 255). `score` criteria is an ordered *list* of
2–10 level descriptions, and the answer is a position along it. `noul` takes no
criteria, or an optional `{"true": ..., "false": ...}`. The API returns 422 on a
malformed `score` but **silently accepts** `{"options": [...]}` as a `choice`
with one option called `options` — and answers every message with it at
confidence 1.0. We shipped that bug. `python eval/lint.py` catches it.

## Before / After

 Without Jev With a recipe

```python
if "refund" in text.lower():
    route = "billing"
elif "ship" in text.lower():
    route = "logistics"
# 200 more lines of this,
# and it still misses
# "just give me my money back"
```

```python
a = jev(state=text, questions=RECIPE)
if a["wants_refund"].noul > 0.7:
    route = "billing"
```

Or: a prompt-and-parse loop against a chat
model. 2–30 s per message, output schema
drifts, costs add up, and you still write a
JSON repair function.

About a second per call in our own runs
(2026-09-21, laptop, TypeSafe direct — TypeSafe
quotes lower). Schema guaranteed. Adding more
questions to the same call is close to free.

## Recipes

| Recipe | What it decides | Status |
|---|---|---|
| customer-support-routing | Category, refund intent, repeat contact, urgency | ✅ |
| roleplay-state | Tone drift, stalled tension, lore breaks — as live sensors | ✅ |
| agent-tool-guardrail | Whether an agent's tool call matches its own stated plan | ✅ |
| context-pruning | Which old tool calls in a long transcript still earn their place — pruning, not compaction | ✅ |
| llm-router | Which model tier should handle this request — asks about the work, not the model | ✅ |
| content-qa | Whether a generated page is thin, and which of five ways — judged against its brief | ✅ (not yet live-tested) |

Every recipe folder has a `questions.json` you can paste straight into a
request, and a README explaining *why* each question is shaped that way — what
was tried first, what broke, and where it still gets things wrong. Some also
carry a gate set for pass one, or an `example.json` showing the response shape.

## Providers

The same request body works against all three. Latency differs, so note which
one you used when reporting eval results.

| Provider | Endpoint | Model id |
|---|---|---|
| TypeSafe | `https://api.typesafe.ai/v1/systemone` | `jev-latest` |
| OpenRouter | `https://openrouter.ai/api/v1/decisions` | `typesafe/jev-1.13` |
| NanoGPT | `https://nano-gpt.com/api/v1/decisions` | `typesafe/jev-1.13` |

TypeSafe's own API is still gated behind a waitlist at the time of writing; the
other two are open.

## Four rules every recipe follows

These are not style preferences. Each one exists because skipping it produces
wrong answers on real data.

**1. Every `choice` has a fallback option.**
Jev picks from a closed set. Hand it something off-topic and it will still
choose — confidently. Always include `OTHER` / `UNRESOLVED`, then review what
lands there. This is the single most common way recipes fail in production.

**2. Ask atomic questions, combine in code.**
Not "rate this ticket". Ask about urgency, refund intent and repeat-contact
separately, then weight them with your own formula. When priorities change you
edit a coefficient instead of rewriting a prompt.

**3. Multi-label means several `noul`s, not one `choice`.**
If an item can be two things at once, a single `choice` forces a false
either/or. Questions in one call are evaluated independently and in parallel, so
a dozen `noul`s cost roughly what one does.

**4. Split judgement from extraction.**
Jev generates nothing. "Is this a complaint about sizing?" → Jev. "Quote the
exact sentence" → an LLM. Most pipelines want both: gate with Jev, extract with
an LLM on the survivors only.

## The two-pass pattern

The pattern that makes large corpora affordable:

```
everything  ──▶  cheap gate (5-7 questions)  ──▶  ~10% survive
                                                      │
                                              full checklist (40-60 questions)
                                                      │
                                              LLM, only where you need prose
```

Pass one runs on everything with a tiny question set. Pass two runs the
expensive, detailed checklist only on what survived. Because questions inside a
single call are nearly free but *state* is what you pay for, this is where the
order-of-magnitude savings come from — not from the per-token price alone.

See recipes/customer-support-routing for a
worked example.

## Benchmarks

Confidence calibration is the one Jev claim with no public paper behind it, so
this repo does not ask you to take anyone's word for it — including ours.

**Measured, 2026-09-21, `jev-1.13.0`, CLINC150 test + 1,000 out-of-scope, one
151-way `choice`, untuned option names:**

| agreement | in-scope acc | OOS recall / precision | ECE | n | cost |
|---|---|---|---|---|---|
| 89.4% | 90.6% | 83.8% / 89.2% | 0.025 | 5,500 | ≈ $0.63 |

Confidence tracks accuracy within a few points in every bin. The fallback
bucket caught 84% of out-of-scope input, and **54 of the 162 it missed were
assigned a wrong intent at confidence ≥ 0.9** — which is why rule 1 says *review
what lands in the fallback*, not *trust it*. Full tables, the exact command,
per-item results and what the run does not tell you:
eval/results/clinc150_jev-1.13.0_2026-09-21.md.

`eval/` contains the harness that produced it. It runs any recipe or question
set against a labelled dataset and reports agreement, a confidence-vs-error
curve, the escalation rate at a given threshold, and how the fallback option
behaves. It speaks the Jev request shape, so `--base-url` points it at any
compatible server too.

**No numbers are published here that you cannot reproduce.** Run it on your own
data, or on one of the public sets listed in eval/README.md,
and open a PR with what you get — including the runs where it did badly. A
cookbook that only reports wins is worthless.

```bash
python eval/lint.py                      # shapes + fallback options, no API key needed

python eval/run_eval.py \
  --recipe customer-support-routing \
  --data   eval/data/tickets.jsonl \
  --field  category \
  --n 200
```

## Contributing

New recipes are very welcome, especially from domains not covered here. The bar
is low but specific — see CONTRIBUTING.md. Short version: a
recipe needs a runnable `questions.json` that passes `eval/lint.py`, a fallback
option on every `choice`, and one honest note about where it gets things wrong.

## License

MIT. Use these however you like.

Not affiliated with TypeSafe AI.

# npcs/termy/README.md

## 关联链接

- https://api.typesafe.ai/v1/systemone
- https://api.typesafe.ai/v1/systemone`
- https://nano-gpt.com/api/v1/decisions`
- https://openrouter.ai/api/v1/decisions`

## 导航

- 项目页：[[10-项目/github.com_f45cd715]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
