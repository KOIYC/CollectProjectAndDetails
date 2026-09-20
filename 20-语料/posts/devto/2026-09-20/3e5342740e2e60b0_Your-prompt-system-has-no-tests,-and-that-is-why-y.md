---
type: "corpus"
item_id: "3e5342740e2e60b0"
title: "Your prompt system has no tests, and that is why you cannot tell it is broken"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/latifox/your-prompt-system-has-no-tests-and-that-is-why-you-cannot-tell-it-is-broken-10bh"
project_url: "https://github.com/Latifox/find-me-saas"
author: "Latif Abderrahmane"
published_at: "2026-09-06T21:24:56Z"
captured_at: "2026-09-20T14:17:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-06"
tags:
  - 语料
  - devto
  - ai
  - claude
  - saas
  - indiehackers
metrics: {"reactions": 7, "comments": 6, "reading_time": 5}
comments_count: 6
comments_total: 6
discovered_via: "devto:indiehackers"
---

# Your prompt system has no tests, and that is why you cannot tell it is broken

> [!info] 一句话导读
> Tags:** `ai`, `python`, `testing`, `showdev`

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/latifox/your-prompt-system-has-no-tests-and-that-is-why-you-cannot-tell-it-is-broken-10bh>
> 指标：reactions=7 · 评论=6 · reading_time=5
> 作者：Latif Abderrahmane　|　发布：2026-09-06T21:24:56Z
> 项目链接：<https://github.com/Latifox/find-me-saas>
> 采集：2026-09-20T14:17:39+08:00　|　id：`3e5342740e2e60b0`

## 正文

**Tags:** `ai`, `python`, `testing`, `showdev`

---

Code fails loudly. A prompt system fails in silence, and it fails while still producing something that looks completely fine.

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/merhvzz69gsfuk3nxx4m.png)

I found this out the slow way. I had built a multi-skill agent system: 15 skills, nine commands, each one writing structured JSON that the next one reads. It worked for weeks. Then it did not, and I could not tell you when it stopped, because nothing ever threw. A skill quietly stopped writing one field. The next skill read a null and carried on. The final score came out a few points off, in a document that read exactly as convincing as it had the week before.

Plausible output is the one thing these models are never bad at. That is precisely the problem.

## What a test even means here

You cannot assert on the prose. Run the same prompt twice and you get different words, and that is fine, because the words are not the contract. Something else is.

Three things turned out to be testable, and together they catch nearly everything:

**The arithmetic.** My system scores six weighted dimensions and applies a penalty when any dimension falls below a floor. That is deterministic. The model produces the dimension values, but the final number is a function of them, and a function is something a checker can recompute without going anywhere near the model. If the number on disk disagrees with the number the checker computes, one of them is lying and it does not matter which.

**The shape.** Every skill writes a file with an expected structure. Required fields, enums for anything constrained, explicit nullability, conditional requirements where one field's presence forces another. This is schema validation, and it is unglamorous, and it caught more real regressions than anything else I wrote.

**The prose rules that are actually numbers.** A memo has to sit inside a word budget. It has to contain its required sections. It has to cite at least three URLs that are shaped like URLs. None of that judges quality, and all of it catches drift, because the specific way a model degrades is by getting longer, vaguer and less sourced.

## The checker

About 750 lines of Python. No dependencies, standard library only, runs in well under a second.

I want to defend the no-dependencies part, because it was not laziness. This checker runs inside a hook on every file write. If it needs a virtualenv, it will not be there when someone clones the repo, and a test that does not run is worse than no test because it lets you believe you are covered.

The contract lives in one JSON file keyed by output filename, with six directives: `required`, `enums`, `nullable`, `conditional`, `nested_required` and `one_of`. That last one earns its place. Some outputs are valid in more than one shape, for example a business-to-business analysis carries fields a consumer analysis does not, and `one_of` lets the contract say "this group, or that group" without branching the whole schema.

## The part most people skip

A checker that never fails is indistinguishable from a checker that does not work.

So the suite runs against ten fixtures, six valid and four deliberately broken. The broken ones do not merely have to fail. They have to fail with exactly 23, 3, 1 and 2 errors respectively. If a fixture starts producing 22 errors, something in the checker stopped looking.

Then I mutation-tested the assertions themselves: take a passing fixture, break one specific thing, confirm the harness catches it. This is where I found that one of my own tests was passing for the wrong reason. My mutation removed a string case-sensitively while the assertion lowercased the text first, so a capitalised copy survived and the check never fired. The assertion was correct. My test of the assertion was wrong. I would never have found it by reading the code.

If you take one thing from this article, take that. Test the tests. In a system where the output is generated, your checker is the only thing standing between you and confident nonsense, and an untested checker is a smoke alarm with the battery out.

## Wiring it to the agent

The last piece is making the agent fix its own output without a human in the loop.

Claude Code has a `PostToolUse` hook that fires after a file write. It receives JSON on stdin including the path. My hook extracts the path, returns immediately if it is outside a managed folder, runs the checker on that folder, and exits 2 with the errors on stderr when something fails. Exit code 2 on this hook does not block anything, it just surfaces stderr back to the model, and the model reads the errors and corrects the file before it moves on.

The whole hook is about 40 lines, and the most important line in it is the try/except that makes it exit 0 on any unexpected exception. It fails open, always. A hook that crashes and blocks work would get uninstalled by the end of the first week, and then there would be no checking at all. A checker nobody runs protects nothing.

## What it caught that I did not expect

I built this to catch the model. It caught me.

Running over my accumulated analyses, one pattern was impossible to miss. My competition estimates before research were systematically too optimistic, by 20 to 40 points, on all five ideas I had run. Never once too pessimistic.

That is not a bug in the model. That is a bug in the rubric, and specifically in letting an unresearched number be treated as a number at all. So I capped unresearched competition estimates at 45 and relabelled them an upper bound rather than a score.

The harness did not find that by being clever. It found it because writing every intermediate value to disk in a checkable format meant there was finally something to look across.

## If you want to steal this

The whole thing is MIT and open. The checker is `tests/validate_memory.py`, the contract is `tests/schemas.json`, the fixture generator is `tests/make_fixtures.py`, and the hooks are in `.claude/hooks/`.

https://github.com/Latifox/find-me-saas

The project it belongs to is a startup-idea validator, but the testing pattern has nothing to do with startup ideas. If your agent writes structured output that another step consumes, this shape transfers directly. Recompute what is deterministic. Validate the shape. Assert the numeric properties of the prose. Test the tests. Fail open.

Then go and look at what the record says about you, because that is where the actual finding will be.

## 评论（6/6）

> **Hamid Ahmadian** · 2026-09-06T21:35:15Z　
> The mutation-testing point is the one to steal — "test the tests" generalizes way past prompt systems. One failure mode worth flagging in the fail-open design though: "exit 0 on any unexpected exception" protects you from the hook crashing and blocking work, but it can't distinguish "checker ran and found zero errors" from "checker silently short-circuited before checking anything" — e.g. a bug in the "outside a managed folder" path match that misfires and skips real files. Both look identical from outside: exit 0, no errors. I've started having checkers log a per-run count of files actually validated alongside pass/fail, specifically so a checker gone quiet because it's broken doesn't read the same as one that's quiet because everything's fine. Same shape as your fixture-count assertion for the broken cases, just applied to the live run instead of the test suite.

---

> **Reid Marlow** · 2026-09-06T23:07:32Z　
> The standard library zero-dependency checker is the right call for write hooks. Once a pre-commit or post-write hook requires an activated virtualenv or external package, someone runs a task outside the environment, the hook fails to start, and the whole check gets commented out.
>
> The main trap I hit with exit code 2 self-correction loops is optimizer thrash on competing constraints. If an agent fails a schema check because the word count is over budget while also missing a required citation field, it will sometimes satisfy the checker on the second attempt by stripping out nuanced context or inserting generic filler URLs just to pass the regex. Capping the automatic correction budget to two attempts and dumping a quarantined artifact with the raw stderr diff when it fails keeps the agent from mutilating its own output to appease the linter.

---

> **kevinbai** · 2026-09-06T23:54:06Z　
> The words are not the contract is the key insight here. Splitting testable layers — recompute the deterministic functions, validate shape, turn prose rules into countable checks — mirrors what schema-first agent pipelines do, but the stdlib-only checker on every file write is the part most people skip. A test that doesn't run everywhere is worse than no test.

---

> **kevinbai** · 2026-09-06T23:54:19Z　
> The mutation-testing-the-assertions step is the part most people skip, and it's the one that matters: in a generated-output system your checker IS the spec, and an untested checker just shifts the silent failure one level down. The fail-open hook design (exit 0 on unexpected exception) is also the right call — a gate that blocks work gets uninstalled, a gate that pages you gets kept. We've found the same with schema contracts: make the LLM write structured output, validate deterministically, and let the prose be the only unasserted surface.

---

> **Vinh Nguyen** · 2026-09-07T00:10:35Z　
> The exact-count fixtures are the part I would expect to erode, and it erodes in the direction you care about. A fixture pinned at 23 goes red the day you add a check, which is a change that made the checker better, so the maintenance move under time pressure is to bump it to 24 and carry on. That is the same "stopped looking" failure the fixtures exist to catch, arriving through the update path rather than the regression path, and the count on its own cannot tell you whether the extra error is a new real one or the same defect reported twice.
>
> Asserting the set of error codes each broken fixture should produce separates those two: a code appearing is an addition someone has to look at, a code disappearing is the alarm you actually wanted, and neither one is satisfied by editing a number.

---

> **RoutineKit** · 2026-09-08T00:39:02Z　
> The missing test I see most often isn’t a golden output — it’s a frozen “inputs contract.” Before the first prompt I write four lines that must stay true: outcome, out of scope, done-when, and never invent X. If a later reply violates any line, the run fails even when the prose looks sharp.
>
> That turns “is the prompt system broken?” into a binary check you can do in under a minute, without waiting for production pain.
>
> Curious what your first failing test usually catches: hallucinated APIs, scope creep, or silent assumption drift?

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/merhvzz69gsfuk3nxx4m.png

## 导航

- 项目页：[[10-项目/github.com_0439100c]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
