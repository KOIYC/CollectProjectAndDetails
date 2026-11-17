---
type: "corpus"
item_id: "63c3e7b66478d404"
title: "One Month After the Hackathon: Why My 4-Service App Stopped Working (and What @mansio Caught in the Verifiers)"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/earlgreyhot1701d/one-month-after-the-hackathon-why-my-4-service-app-stopped-working-and-what-mansio-caught-in-the-3i8h"
project_url: "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols"
author: "Earl Grey"
published_at: "2026-11-13T17:48:25Z"
captured_at: "2026-11-17T11:11:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-13"
tags:
  - 语料
  - devto
  - ai
  - javascript
  - buildinpublic
  - opensource
metrics: {"reactions": 37, "comments": 27, "reading_time": 6}
comments_count: 28
comments_total: 28
discovered_via: "devto:buildinpublic"
---

# One Month After the Hackathon: Why My 4-Service App Stopped Working (and What @mansio Caught in the Verifiers)

> [!info] 一句话导读
> What breaks a month after a hackathon, and what a fellow DEV writer caught in the verifiers.*

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/earlgreyhot1701d/one-month-after-the-hackathon-why-my-4-service-app-stopped-working-and-what-mansio-caught-in-the-3i8h>
> 指标：reactions=37 · 评论=27 · reading_time=6
> 作者：Earl Grey　|　发布：2026-11-13T17:48:25Z
> 项目链接：<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols>
> 采集：2026-11-17T11:11:25+08:00　|　id：`63c3e7b66478d404`

## 正文

*What breaks a month after a hackathon, and what a fellow DEV writer caught in the verifiers.*

> **TL;DR:** A month after shipping [README Clew 2](https://readme-clew-2.vercel.app), I opened it up and every scan failed. Nothing was wrong with the deterministic verifiers or with Jev on Glasser. Instead, three small operational traps lined up at once: an expired 30-day GitHub token on a tool that only reads public repos, a rotated Claude Haiku key scoped only to `Development` in Vercel, and a substring bug that fellow DEV writer [Mikhail (@mansio)](https://dev.to/mansio) found and fixed in [PR #2](https://github.com/earlgreyhot1701D/readme-clew-2/pull/2).

In October I built [README Clew 2](https://github.com/earlgreyhot1701D/readme-clew-2) for the AdaL "What Would Jev Do?" hackathon. It checks whether a public JavaScript or TypeScript repo's README matches its code, sorting every checkable line into four buckets: **Contradicted**, **Missing**, **Unverifiable**, and **Verified**.

The core rule of the build is that **models never decide what is true**:

| Job | Who does it |
|---|---|
| Split the README into lines and settle obvious headings/badges | Deterministic code rules |
| Label what kind of claim a prose line makes (command, dependency, env var, file/URL) | [Jev](https://typesafe.ai) (`jev-1.13.0`) via [Glasser](https://glasser.ai), gated at 0.8 confidence |
| Decide Verified, Contradicted, or Missing | Five deterministic code verifiers |
| Write a two-sentence plain-English summary from the counts | Claude Haiku (`claude-haiku-5-5`), fail-open |

When you wire that many moving parts together (AdaL, Jev, Glasser, Haiku, GitHub, and Vercel) and come back a month later to a red `SCAN FAILED` banner, it is hard to tell at first glance which piece broke.

Here is what was actually wrong, and the two fixes that came out of it.

---

## 1. When `"javascript"` hides `"ava"`: @mansio's PR #2

Before I even got to the deployment keys, [Mikhail (@mansio)](https://dev.to/mansio) had opened and landed [PR #2](https://github.com/earlgreyhot1701D/readme-clew-2/pull/2), the project's first external code contribution.

Mikhail was testing README Clew 2 against real repositories and noticed something strange on `sindresorhus/yocto-queue`. The repo uses `ava` as a test runner, and the README never mentions `ava`. The coverage verifier should have flagged `ava` in the **Missing** bucket. Instead, it stayed silent.

Why? Because the README contained a link to Mozilla's documentation:

```text
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols
```

And inside the word `javascript`, in lowercase, sits the three-letter substring `ava`.

Our coverage check was using a plain substring match:

```js
// Before: any substring match counted as "mentioned in the README"
if (readme.includes(name.toLowerCase())) continue;
```

Even worse, the same substring check lived in the dependency verifier's prose guard (`inCodeContext`), which checks whether a candidate package name appears on an install line. A short name like `can` inside `npm i canvas-parser` or `lodash` inside `npm i lodash-es` could bypass the prose guard and reach **Contradicted**, the exact false positive the guard was built to prevent.

### The fix

Mikhail replaced both substring checks with a single whole-token rule, `mentionsWord()`, bounded by npm's own package name characters (`A-Za-z0-9_-`) plus `@` and `/`:

```js
export function mentionsWord(text, name) {
  if (!name) return false;
  const esc = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return new RegExp(`(?<![A-Za-z0-9_@/-])${esc}(?![A-Za-z0-9_-])`, 'i').test(text);
}
```

With that in place:
- `We use ava.` and `Tests run with \`ava\`.` still count as real mentions.
- `mozilla.org/.../javascript/...` no longer hides `ava`.
- `npm i lodash-es` no longer treats `lodash` as an installed package claim.

Mikhail shipped the fix with a 27-case test matrix and verifier controls in [`tests/mentions-word.test.js`](https://github.com/earlgreyhot1701D/readme-clew-2/blob/main/tests/mentions-word.test.js), matching the repo's file-size cap and offline test rules on the first try. If you have not read his engineering field notes on DEV (like [The Dataset Was Lying: 4 of 6 "False" Facts Were True](https://dev.to/mansio/the-dataset-was-lying-4-of-6-false-facts-were-true-13ok)), go read him.

---

## 2. The 30-day time bomb: sending an expired token to a public API

Once Mikhail's PR was merged, I still had a live site that refused to scan.

Every click on **SCAN** returned `HTTP 502`:

```json
{"error":{"code":"github_forbidden","message":"GitHub returned HTTP 401"}}
```

The ironic part: **README Clew 2 only scans public repositories.** It makes 4 metadata calls to `api.github.com` per scan and fetches the files from `raw.githubusercontent.com`. You do not even need a `GITHUB_TOKEN` for low-volume public reads (GitHub allows 60 unauthenticated REST calls per hour per IP, or 15 full scans per hour).

During the October hackathon, I had added a 30-day GitHub Personal Access Token so repeated test scans wouldn't hit the unauthenticated rate limit. Thirty days passed, the token expired, and `lib/github.js` kept sending `Authorization: Bearer <expired_token>` on every request.

GitHub allows requests with *no* `Authorization` header, but immediately rejects requests carrying an *expired* `Authorization` header with `401 Bad credentials`. Because step 1 threw a `GithubError`, the pipeline stopped before Jev or Haiku ever ran.

### The 4-line fix

First, I removed the expired `GITHUB_TOKEN` from Vercel. Second, we hardened [`lib/github.js`](https://github.com/earlgreyhot1701D/readme-clew-2/blob/main/lib/github.js) so that if an expired token is ever present in `.env` or server environment variables and GitHub answers `401`, the client drops the `authorization` header from the shared headers object and retries unauthenticated:

```js
if (res.status === 401 && headers?.authorization) {
  delete headers.authorization; // expired or bad token: public repos work without it
  return request(url, { fetchImpl, headers, as });
}
```

Because `headers` is shared across the 4 metadata calls in `fetchRepo()`, dropping `headers.authorization` on the first `401` means the remaining 3 calls go straight out without the bad token.

---

## 3. Silent fail-open + Vercel environment scopes

The last piece was Claude Haiku. By design, Haiku is **fail-open** in README Clew 2: if the summary call fails or times out, the report still renders in full and the clew mascot falls back to a fixed one-line summary per mood.

My October Anthropic key had also been rotated. When I added the new `ANTHROPIC_API_KEY` in Vercel, two classic traps bit me at the same time:

1. The new key was scoped to `Development` in Vercel, while `Production` and `Preview` still held the 34-day-old key.
2. Vercel environment variable changes only take effect on the next deployment.

Running `vercel env ls` made the split visible right away:

| Variable | Environment | Created |
|---|---|---|
| `ANTHROPIC_API_KEY` (new) | `Development` | Today |
| `ANTHROPIC_API_KEY` (old) | `Production, Preview` | 34d ago |
| `GLASSER_API_KEY` | `Production, Preview, Development` | 34d ago |

Overriding `ANTHROPIC_API_KEY` across all three environments (`Production, Preview, Development`) and running `vercel --prod` brought the Haiku summary and bucket notes back on the first scan. Meanwhile, Glasser and Jev (`jev-1.13.0`) never missed a beat: all 4 batched calls completed in 1.37 seconds for about half a cent (`$0.0055`), with `$10.80` of the original hackathon balance still untouched.

---

## Related reading on DEV

Two posts from the community hit the exact operational edges from today's debugging session:

- [["Invalid API key" or undefined env vars on Vercel: how to fix it](https://dev.to/unbreakkit/invalid-api-key-or-undefined-env-vars-on-vercel-how-to-fix-it-50ig)] by [@unbreakkit](https://dev.to/unbreakkit) walks through how environment variable scopes (`Production` vs `Preview` vs `Development`) and missing redeploys cause `401 Invalid API key` errors on Vercel even after you paste a fresh key.
- [[Your AI Agent Runs for Hours. Its GitHub Token Might Not.](https://dev.to/__be2942592/github-cli-expiring-credentials-change-the-contract-of-a-cached-token-48no)] by [@__be2942592](https://dev.to/__be2942592) looks at what happens when code assumes a GitHub token in the environment is valid forever instead of handling `401` expiration explicitly.

---

## Try it

- **Live page:** [readme-clew-2.vercel.app](https://readme-clew-2.vercel.app) (click **USE DEMO REPO**, then **SCAN**)
- **Source and 478 offline tests:** [github.com/earlgreyhot1701D/readme-clew-2](https://github.com/earlgreyhot1701D/readme-clew-2)

Thank you again to [Mikhail (@mansio)](https://dev.to/mansio) for finding the substring bug on a real repo and shipping a clean, well-tested fix.

---

Quick context if you are new here. I work in the California courts, running court operations for the county. I started building with AI in July 2025 and I have been learning in public ever since. I do not write the code. I direct, the agents generate, I validate and decide. I build the [Clew Suite](https://clewlabs.org), a set of civic tech tools for making complex systems easier to inspect. That is the lens I am writing from.

AI Assisted. Human Approved. Powered by NLP.

## 评论（28/28）

> **Reid Marlow** · 2026-11-13T18:07:56Z　
> Dropping headers.authorization on a 401 works cleanly when fetchRepo() runs calls sequentially, though if those four metadata requests ever run under Promise.all, all four already go out with the expired header before the first 401 returns.
>
> The Vercel scope trap pairs awkwardly with fail-open Haiku summaries too. Because the UI still renders a fallback line when the key returns 401 in Production, an expired or mis-scoped key stays invisible unless the catch block emits a warning log or counter.

---

> **Earl Grey** · 2026-11-13T22:24:40Z　
> Good catch, and you were right. The first call runs alone, so an expired token gets caught before the parallel pair goes out. A token that dies mid-scan is a different story: both parallel calls come back 401 and only one gets its retry. Mikhail opened a PR for exactly that about an hour after your comment. Each request now remembers whether it carried the token and retries its own 401.
>
> On fail-open: each Haiku failure does write a reason code to the scan receipt. Nothing taps me on the shoulder, though, which is how a dead key sat there for a month.

---

> **Mikhail** · 2026-11-13T19:25:44Z　
> Thanks for the shoutout, Earl — really appreciate the credit!
>
> Loved reading the honest post-mortem. Seeing an expired token, a dev-scoped key, and a hidden substring match all line up after a month is such a classic post-hackathon moment. Glad the mentionsWord fix helped, and it's awesome to see the scanner back to green!

---

> **Earl Grey** · 2026-11-13T22:25:28Z　
> Thank you for the fix, and for three more PRs today! The per-request retry is the exact thing Reid and Sina were circling. Reading them now. Your name’s in the README where it belongs.

---

> **Paul Lovelace** · 2026-11-13T22:03:56Z　
> The expired-token bit genuinely surprised me — that GitHub happily serves public repos with no token at all, but a dead one gets you a 401 and kills the whole scan before Jev or Haiku even run. I'd have assumed an expired token just degrades to anonymous, not that it actively blocks you. Your retry-without-the-header fix makes sense, though Reid's point about Promise.all has me wondering how long that shared-headers trick holds up once those four calls go parallel.

---

> **Earl Grey** · 2026-11-13T22:25:06Z　
> Same! I assumed a dead token would get treated like no token. Nope. And Reid was right about the parallel calls. Mikhail already has a PR up for it, with a test for that exact pair. This comment section is doing better code review than I planned for lol.

---

> **Sina Rezaei** · 2026-11-13T22:04:08Z　
> There’s one edge case I’d pay extra attention to in the GitHub fallback: concurrency.
>
> If fetchRepo() eventually runs those four metadata requests through Promise.all, mutating a shared headers object after the first 401 creates a race. Some requests may already have left with the expired token. I’d keep request headers immutable and make the retry decision at the individual request level: retry that public GET once without authorization, rather than changing shared state while other requests are in flight.
>
> There’s also a scaling detail worth considering. GitHub’s unauthenticated REST API limit is 60 requests per hour per originating IP. On a serverless deployment, multiple users can end up sharing outbound IP capacity, so a fallback that works perfectly during development might become a rate-limit bottleneck under real traffic.
>
> I’d also make the Haiku fail-open path observable. Returning a valid report is the right availability decision, but a fallback counter or structured warning would make sure repeated AI failures don't quietly become the new normal.
>
> The interesting part of this post-mortem is that none of these issues requires a major architectural failure. Small assumptions around shared state, credentials, and observability are enough to change production behavior.

---

> **Earl Grey** · 2026-11-13T22:26:12Z　
> Thank you for laying this out so clearly. Deciding the retry per request is the cleaner design, and Mikhail has a PR open that does it: each request remembers whether it carried the token and retries its own 401. It doesn’t make the headers immutable, which is the fuller version of your point.
>
> The shared IP detail is the one I hadn’t sat with. Scans end up unauthenticated now, so 60 calls an hour is the ceiling, and on Vercel that address isn’t only mine. Fine for a hackathon tool with a handful of visitors. Not fine if it ever gets busy.
>
> And yes to making the fallback countable. Each Haiku failure writes a reason code to the receipt, but nothing adds them up. Small assumptions was the whole post, and you named it better than I did.

---

> **Sina Rezaei** · 2026-11-14T07:13:03Z　
> That makes sense. The part I'd look at next is how these limits interact under concurrent scans. Even if each request handles its own 401 correctly, multiple scans can still consume the same unauthenticated rate-limit budget independently.
>
> For example, imagine 8 users triggering scans at roughly the same time, with each scan making 4 GitHub API calls. That's 32 requests competing for the same outbound IP quota, and if several Vercel functions run independently, they have no shared view of how much quota is left.
>
> A shared rate-limit coordinator could help here. Redis could track the remaining quota and reset timestamp across instances, with a distributed lock or atomic counter to prevent multiple workers from making decisions based on stale quota information. Requests could then be queued or delayed before GitHub starts returning 403 or 429 responses.
>
> Same idea for the Haiku fallback: having reason codes in receipts is a good start, but tracking their frequency over time would help distinguish occasional provider instability from a recurring failure pattern. I'd also separate failures by provider, model and error type to make the metrics actionable.
>
> I think that's where the interesting engineering challenge starts: not just making each request recover, but making the whole system behave predictably under load.

---

> **Earl Grey** · 2026-11-14T17:31:32Z　
> This is the right next problem, and it’s bigger than the tool is today. It’s a hackathon project, so I’d hit GitHub’s limit long before I needed a coordinator. If it ever gets traffic, a shared counter in Redis is where I’d start. Counting fallback reasons by provider and error type is the part I can use now. “Behave predictably under load” is the line I’m keeping.

---

> **Sina Rezaei** · 2026-11-14T18:01:11Z　
> One detail I'd be careful with when you eventually add Redis: make the counter an atomic reservation mechanism, not just a shared value that each Vercel function reads before starting its requests.
>
> For example, if a scan needs four GitHub metadata calls, a Lua script could reserve all four slots in one operation. If the available budget is below four, the scan could wait or use a fallback rather than launching a batch that's likely to hit the limit halfway through. I'd key that budget by the actual egress identity and GitHub rate-limit resource, with a safety margin for requests outside the app.
>
> Then reconcile the estimate using X-RateLimit-Remaining and X-RateLimit-Reset from responses. One subtle point: GitHub processes requests across multiple regions, so rate-limit headers can vary between responses. I'd use them for pacing and backoff, not as a perfectly synchronized global counter. Secondary limits also need separate cooldown handling through Retry-After when present, rather than assuming every 403 means the hourly quota is exhausted.
>
> I wouldn't build all of this for a hackathon project today either. But when traffic justifies it, atomic reservation plus response-based reconciliation is a much safer starting point than a plain Redis increment.

---

> **Earl Grey** · 2026-11-15T17:23:43Z　
> Thank you, this is really helpful, and the “reserve all four at once” idea makes a lot of sense to me. Starting a scan you can’t finish is the same kind of half-done answer I’ve been trying to avoid. I’m not building it yet, but I’ve saved this for the day traffic calls for it. I appreciate you sticking with this thread!

---

> **mp3sss** · 2026-11-14T01:50:04Z　
> Relatable postmortem — nothing actually regressed in the verifiers; the failure was external credential and environment drift: an expired 30-day GitHub token and a Haiku key scoped only to Development in Vercel, both masked locally during the demo and surfaced only in deployment. That argues for putting token expiry and key scope into startup health checks and logs, rather than assuming a read-only public-repo tool stays authenticated. Your split of responsibilities is the right boundary too: deterministic rules settle what's true, models only propose buckets, so a flaky model can't corrupt the verdict.

---

> **Earl Grey** · 2026-11-14T17:32:32Z　
> Startup checks for token expiry and key scope would have caught both of these on day one. Cheaper than my method, which was finding out a month later lol. And thank you on the split. A flaky model not being able to touch the verdict is why Haiku failing didn’t break the report.

---

> **Kürşat Yılmaz** · 2026-11-14T02:24:58Z　
> The obsession with wrapping remote APIs into multi-layered agent abstractions is creating massive hidden latency and failure cascades in production.
>
> If you profile real-world workloads, bare-metal local inference (via direct C++ / llama.cpp or vLLM bindings) consistently beats fragile cloud wrappers on both predictability and cost. Tooling should eliminate abstraction penalties, not compound them.

---

> **Earl Grey** · 2026-11-14T17:34:11Z　
> That’s a different kind of build than mine. Models only label and summarize here, and plain code makes the calls. What broke wasn’t latency. It was an expired token and a key in the wrong environment.

---

> **OneLifeVibe** · 2026-11-14T03:59:20Z　
> The ava hiding inside javascript detail is the one that stuck with me. It is such a quiet failure mode, a check that looks correct until a short name shows up inside a longer word. The expired token story landed the same way for me. I had always assumed a dead token would behave like no token, and learning that GitHub treats an expired header as a hard rejection explains a lot of confusing 401s. Thanks for writing this up as a postmortem instead of just fixing it quietly.

---

> **Earl Grey** · 2026-11-14T17:33:11Z　
> The ava inside javascript one still makes me laugh and wince. Credit to Mikhail for catching it. I had the same assumption about dead tokens. Writing it up beat fixing it quietly, because the comments here ended up improving the fix.

---

> **Ascendra Ventures** · 2026-11-15T02:39:13Z　
> What I like about this post-mortem is that nothing in the verifiers was wrong. All three failures lived around the code: a token with a 30-day life, a key scoped to the wrong environment, and a substring check that only misbehaved on a real repo. The suggestion from mp3sss to put token expiry and key scope into a startup check is probably the cheapest fix on the list.
>
> Environment drift is something we see a lot when rebuilding deploy pipelines at Ascendra Ventures. On one WordPress migration, the old setup was a single EC2 box, deploys were done by copying theme files over SSH, and editors entered every content change twice. The rebuild baked everything into an immutable image on Cloud Run, pulled license keys from Secret Manager instead of the machine, redeployed staging on every push and kept production behind an approval. Staging and production stopped being two hand-kept places that could quietly drift apart.
>
> Would a scheduled weekly scan against one known public repo have caught the expired token before a user did?

---

> **Earl Grey** · 2026-11-15T17:19:58Z　
> Probably yes. The token expired on a 30-day clock and only failed on a real call, so a weekly scan against one known public repo would have hit it before a user did. It’s the cheapest kind of canary. Your point about staging and production quietly drifting is the bigger lesson for me. Nothing in my code broke. Everything around it aged like milk. That's the thing with these hackathon builds, they die silently. So now, the next question, do I break them down after judging or let them live on?

---

> **linkbruno.com** · 2026-11-15T14:06:29Z　
> A README checker tripping over a substring is a little poetic, since READMEs are full of long URLs and a URL is basically lowercase words glued together. Would stripping link targets before the coverage check catch more of these, or do you want URLs to count as mentions on purpose?

---

> **Earl Grey** · 2026-11-15T17:17:50Z　
> Turns out ManSio’s whole-token fix already covers it: a name right after a / never counts, so URL paths are out. Good nudge to add tests that keep it that way.

---

> **Bogdan** · 2026-11-15T21:58:24Z　
> This is a fantastic breakdown of the "hidden gaps" problem. When you have multiple services communicating, the real bugs rarely live in the code itself—they live in the assumptions of how the state flows between them.
>
> As someone who builds complex systems with AI-assisted workflows, I've learned that normal unit tests aren't enough. You need strict invariants (rules that must always be true, like "a payment must never process without a ledger entry") and a dedicated verifier process to check them.
>
> I'm curious: did the verifiers catch a state sync issue between the services, or was it a silent failure inside one of the external APIs? Thanks for sharing this—it's a great reality check for anyone building microservices.

---

> **Earl Grey** · 2026-11-16T00:30:53Z　
> Neither, actually. Nothing went wrong between the services. Two keys aged out around the code: the 30-day GitHub token expired, and my code treated that as fatal even for public repos that never needed it. The Anthropic key had to be rotated too. The one real bug inside a verifier was a substring match (“ava” hiding inside “javascript”), and ManSio caught that one, not me. Your invariants point lands, though. “A scan never fails just because an optional token is bad” is a rule I wish I’d written down sooner.

---

> **Bogdan** · 2026-11-16T00:55:32Z　
> This is the ultimate "production reality check." The "ava" hiding inside "javascript" is a legendary regex trap—it perfectly highlights why simple substring matching is so dangerous. Word boundaries (\b) are your best friend in those verifiers, otherwise "scunthorpe" problems will haunt you forever.
>
> And the expired GitHub token crashing the entire scan for public repos is the classic "fail-hard" anti-pattern. You just articulated exactly why I love your invariants approach: "Systems must degrade gracefully." If an optional authentication fails, the core function should still run.
>
> You hit the nail on the head with that rule. "A scan never fails just because an optional token is bad" is exactly the kind of thing that needs to be written down in a README before a hackathon, not learned a month later. Thanks for the brutal honesty—this is a masterclass in why strict checks and graceful failures are the difference between a demo and a product.

---

> **Earl Grey** · 2026-11-16T02:46:25Z　
> Thank you, Bogdan. One small twist on word boundaries: plain \b treats a hyphen as a boundary, so “lodash” would still match inside “lodash-es”. ManSio’s fix uses custom lookarounds so hyphens and slashes count as part of the name. Scunthorpe problems really are everywhere. And agreed, that rule belongs in the README before day one, not a month later.

---

> **Bogdan** · 2026-11-16T22:32:30Z　
> Spot on, Earl. You just exposed the classic trap of \b—it completely ignores hyphens because they are non-word characters. So lodash will happily match inside lodash-es or lodash/fp.
>
> Using custom lookarounds like (?<![\w/-])lodash(?![\w/-]) is definitely the bulletproof way to handle package names and URLs. It forces the regex to treat the entire slug as a single token.
>
> And you're 100% right about the Scunthorpe problem. It's the ultimate proof that naive regex will always bite you in production. This is exactly the kind of edge case that deserves a place in the README (or better yet, in a unit test) before you write a single line of validation logic. Great insight!

---

> **sitetoolsbox** · 2026-11-16T10:22:10Z　
> This is a brilliant breakdown of the 'hidden gaps' problem. As someone who just built a system entirely from scratch without any frameworks (pure vanilla PHP), I felt this deeply.
>
> Without a framework, you literally have to build your own invariants. When I launched my free webmaster tool directory, I learned the hard way that normal validation isn't enough—bots bypassed my basic checks and flooded the system. I had to rewrite the state flow and manually implement OAuth just to ensure a 'submission' always came from a real human.
>
> It's painful, but it forces you to truly understand every single assumption in your architecture. Great write-up!

## 关联链接

- https://clewlabs.org
- https://dev.to/__be2942592
- https://dev.to/__be2942592/github-cli-expiring-credentials-change-the-contract-of-a-cached-token-48no
- https://dev.to/mansio
- https://dev.to/mansio/the-dataset-was-lying-4-of-6-false-facts-were-true-13ok
- https://dev.to/unbreakkit
- https://dev.to/unbreakkit/invalid-api-key-or-undefined-env-vars-on-vercel-how-to-fix-it-50ig
- https://github.com/earlgreyhot1701D/readme-clew-2
- https://github.com/earlgreyhot1701D/readme-clew-2/blob/main/lib/github.js
- https://github.com/earlgreyhot1701D/readme-clew-2/blob/main/tests/mentions-word.test.js
- https://github.com/earlgreyhot1701D/readme-clew-2/pull/2
- https://glasser.ai
- https://readme-clew-2.vercel.app
- https://typesafe.ai

## 导航

- 项目页：[[10-项目/developer.mozilla.org_78f5ea0f]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
