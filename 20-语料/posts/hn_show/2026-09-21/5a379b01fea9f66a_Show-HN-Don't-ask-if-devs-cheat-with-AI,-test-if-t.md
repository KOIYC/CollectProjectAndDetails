---
type: "corpus"
item_id: "5a379b01fea9f66a"
title: "Show HN: Don't ask if devs cheat with AI, test if they're good with it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48734393"
project_url: "https://tryevaluator.com/"
author: "skyepstein"
published_at: "2026-06-30T15:45:47Z"
captured_at: "2026-09-21T02:53:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_skyepstein
  - story_48734393
  - show_hn
metrics: {"points": 5, "comments": 4, "engagement_velocity": 5}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:113d"
---

# Show HN: Don't ask if devs cheat with AI, test if they're good with it

> [!info] 一句话导读
> Evaluator Pricing Sample Blog Log in Sign up

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48734393>
> 指标：点赞=5 · 评论=4 · engagement_velocity=5
> 作者：skyepstein　|　发布：2026-06-30T15:45:47Z
> 项目链接：<https://tryevaluator.com/>
> 采集：2026-09-21T02:53:01+08:00　|　id：`5a379b01fea9f66a`

## 正文

Evaluator Pricing Sample Blog Log in Sign up
Every engineer uses AI now. Hire the ones who use it well.
 Evaluator scores how well a candidate actually works with AI: reading its output, fixing it, prompting it, and overriding it when it is wrong. Scored next to the fundamentals that still decide whether someone ships.
 Generate a free assessment See a sample first
 10 free every month No card required See what is tested
AI critique Question 14 of 17
 20 points An AI assistant produced this. It looks reasonable. It is not. Find every flaw and fix it.
 async function fetchUserPosts(userId: string) {
 const res = await fetch(`/api/users/${userId}/posts`)
 const posts = res.json.parse()
 return posts.filter((p, i) => i <= posts.length )
} What the candidate found
 res.json.parse() is invented. The real call is await res.json() .
 i <= posts.length is off by one, and the filter does nothing useful anyway.
 Critique score 92 / 100
Five fundamentals, plus the one most tests skip.
 Every assessment is generated for the role you are hiring for, in the stack you use. The questions change. The dimensions do not.
AI collaboration
 How it is scored
 Five sub-tests covering prompt quality, reading AI code, fixing it, critique, and live collaboration. The dimension a conventional coding test does not look at.
Prompt the candidate sent
 Implement a debounced search hook for the Postgres-backed /api/search endpoint we already use in SearchBar.tsx . 300ms debounce. Cancel in-flight requests with the AbortController we use elsewhere. Return { data, error, loading } . Do not add a fetch library. Empty query returns early with no request.
What we scored it on
 Context 4 / 4
 Constraints 4 / 4
 Edge cases 4 / 4
 Acceptance criteria 0 / 4
 Names the existing pattern 4 / 4
 Prompt quality 16 / 20
 Lost four points for never stating how the reviewer would know the hook was finished.
Code reading
 How it is scored
 Untangle real code and say what it actually does. Spot the subtle bug, reason about the architecture around it.
if (user?.perms?.includes('admin')
 || user?.role === 'admin') {
 return grant(user) // which wins?
}
 Code writing
 How it is scored
 Implement to spec. Complete partial code. Build features that meet the spec they were given.
Spec compliance 7 / 8 assertions
Debugging
 How it is scored
 Find the bug in messy legacy code. Bad naming, deep nesting, hidden state, no tests to lean on.
- if (idx = list.length) return
 + if (idx === list.length) return
 one character, four hours
 Communication
 How it is scored
 Write for the next human, not the compiler. Pull request descriptions. Explaining a refactor to a product manager.
“Swapped the N+1 in the digest job for a single join. Cuts the nightly run from 40 minutes to about 90 seconds. No API change.”
Tradeoffs
 How it is scored
 Justify the choice. Build or buy, SQL or NoSQL, ship it now or do it properly.
Ship the join
 Fast now, harder to shard later
Denormalise
 Slower to build, scales cleanly
Graded on the argument, not the answer.
You have been screening for the wrong thing.
 Hiring in 2023
 Did the candidate use ChatGPT? Block them, detect them, ban the tool.
Hiring in 2026
 Of course they use AI. The question is whether they can read it, fix it, prompt it, and override it when it hallucinates.
Every shop now has Copilot, Cursor, Claude Code. The bottom quartile of every team takes the AI's first answer. The top quartile catches the hallucinated import, rewrites the over-engineered class, and ships something that works. We test for the top quartile.
Five tests for how someone works with AI.
 No other platform does this. Most still treat AI as something to detect. We treat it as something to grade.
01 Can they brief an AI like they brief a junior?
 We give them a feature spec. They write the prompt they would actually send. We score for context, constraints, edge cases, and acceptance criteria, not for verbosity.
A strong candidate response
 Implement a debounced search hook for the Postgres-backed /api/search endpoint we already use in SearchBar.tsx . 300ms debounce. Cancel in-flight requests on new input, using the AbortController we use elsewhere. Return { data, error, loading } . Do not introduce a new fetch library, we use native fetch. Handle the empty query by returning early without a request.
 Gives context States constraints Names the edge case
02 Can they tell working from good?
 We show them AI-written code that runs. They explain what it does, flag the tells (an over-engineered class, a defensive try/catch swallowing real errors, a pattern nobody writes by hand), and say what they would change.
class UserDataManager {
 private cache: Map
 constructor() {
 this.cache = new Map()
 }
 async getUserById(id: string | null): Promise {
 if (!id) return null
 try {
 if (this.cache.has(id)) return this.cache.get(id)!
 return await fetchUser(id)
 } catch (e) { return null }
 }
} Candidate
 A class for what should be a function. It swallows errors silently, so the caller cannot tell a 500 from a missing user. And it never writes to the cache, so the cache never warms.
03 Can they fix one bug without touching anything else?
 We plant exactly one realistic bug in an AI-written function. They find it and patch it minimally. A broad refactor that misses the actual problem loses points.
The candidate's diff
 function paginate(items, page, size) {
 - const start = page * size
 + const start = (page - 1) * size
 return items.slice(start, start + size)
 } Correct. One line, and no collateral refactor.
04 Can they catch every hallucination?
 We give them code with several planted flaws: invented APIs, off-by-ones, swallowed errors. We grade thoroughness. Did they catch all of them, or stop at the first one and call it good?
Found by candidate, 3 of 3
 lodash.deepFlatten does not exist. _.flattenDeep does.
 catch (e) {} swallows the error. It should log or rethrow.
 The loop runs in quadratic time. The outer pass should be a Set lookup.
05 Watch them work with the assistant.
 On the final question the candidate gets an AI sidebar inside the editor. Every prompt they send, every suggestion they accept, every chunk they reject, and every keystroke on top is recorded. The transcript goes to you.
function debouncedSearch(query: string) {
 // accepted from the assistant
 if (!query) return
 if (controller) controller.abort()
 // candidate edit: was 200, made it 300
 timeout = setTimeout(...)
} Sidebar transcript
 Candidate: use AbortController for cancellation
 Assistant:
 Candidate: debounce is wrong, it should be 300ms not 200ms
4 prompts, 2 accepted, 1 rejected, 38% edited by hand
From a job description to a scored candidate, in one sitting.
 01 Paste a job description.
 Or describe the role in one sentence. We pick up seniority, stack, and what the person will actually be doing.
02 Get an assessment in about 100 seconds.
 A custom test across all six dimensions, calibrated to the role.
03 Share a link. Get a scored report.
 Candidates take it async. You get per-question feedback, integrity flags, and for AI questions the full transcript.
We allow AI where it is expected. We catch it where it is not.
 On the AI collaboration section the sidebar is right there, because we are scoring how they use it. Everywhere else, behavioural analysis, keystroke pacing, paste patterns, and model fingerprinting flag anyone trying to outsource the fundamentals.
Allowed On AI questions
 The sidebar is visible. Every prompt, accept, and edit is logged for the reviewer.
Flagged Model fingerprint on a no-AI question
 Uniform structure, hedging language, and suspiciously polished prose written under time pressure.
Flagged Pure paste
 A non-trivial answer arrived with zero keystrokes, pasted from somewhere off the page.
Flagged Burst pattern
 Long idle, then a 400 character-per-minute burst, then submit. The alt-tab fingerprint.
Flagged Tab switches
 Five or more focus changes during a single question.
Priced per assessment, not per seat.
 Nothing about the scoring is held back for Pro. You upgrade for volume, to drop the Evaluator badge, and for priority support.
Free
$0 forever
 The same scoring as Pro, at lower volume. Not a trial: it does not expire.
 10 assessments every month
 All six dimensions, including AI collaboration
 Full integrity reports
 PDF and CSV export
 Assessments carry the Evaluator badge
 Start free
 Pro
 Best value
 $39 per month
 For teams hiring regularly.
 250 assessments every month
 Everything in Free
 Remove the Evaluator badge
 Priority support
 $0.50 per extra assessment
 Start Pro
 Pro annual
$33 per month, billed yearly
 The same as Pro, about 15 percent cheaper.
 3,000 assessments a year
 Everything in Pro
 Saves about $69 against monthly
 Start annual
Stop hiring engineers who can ace a 2019 coding test.
 Start hiring the ones who ship working software in 2026: with AI, around it, and despite it.
 Generate one free See a sample
Evaluator A technical assessment for hiring engineers who work well with AI, scored alongside the fundamentals.
Product
 Sample assessment
 Pricing
 Alternatives
 Company
 Blog
 Support
 Privacy
© 2026 Evaluator
 Log in Create an account

## 评论（4/4）

> **Karthick81** · 2026-06-30T15:52:26.000Z　
> Can this be used for non coding jobs too?

---

> **hasudon7171** · 2026-07-01T12:06:40.000Z　
> AI uses well is not generate good coding, achieving good results with low token.

---

> **brookst** · 2026-06-30T16:10:47.000Z　
> Yes for sure. I like asking candidates to pull up their favorite LLM and show me how they’d use it to do market research, using a real but irrelevant example like “suppose we’re looking at opening a design office in Belgrade, to get 24 hour coverage. How would you use an LLM to research this? Pull up your favorite and show me.”I honestly think “oh I don’t use LLMs for anything” is disqualifying. I’ve had a couple of people say that. I would be open to “you know I’ve tried it and it never produced good results, let me show you how I’d use Google and …” but have never heard that.And of the people who are game, I’ve seen a wide variety, including screen shares that include the STT of our conversation to date and suggested replies. And some genuinely smart, high-leverage AI use that’s impressed me.

---

> **Karthick81** · 2026-06-30T16:55:15.000Z　
> I believe the statement "I don't use LLM for anything" should not be disqualifying. Many companies frown upon use of AI because of fear of hallucination, so not everyone is open about it in all settings.

## 导航

- 项目页：[[10-项目/tryevaluator.com_02b73229]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
