---
type: "corpus"
item_id: "3e58e881f67fc73d"
title: "Your grammar checker uploads every word you type. I built one that never leaves your Mac."
source: "devto"
source_name: "dev.to"
url: "https://dev.to/rudratosh/your-grammar-checker-uploads-every-word-you-type-i-built-one-that-never-leaves-your-mac-8pj"
project_url: "https://brisktype.com/"
author: "Rudratosh Shastri"
published_at: "2026-10-19T18:06:54Z"
captured_at: "2026-10-22T09:49:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-19"
tags:
  - 语料
  - devto
  - privacy
  - ai
  - macos
  - indiehackers
metrics: {"reactions": 6, "comments": 4, "reading_time": 6}
comments_count: 4
comments_total: 4
discovered_via: "devto:indiehackers"
---

# Your grammar checker uploads every word you type. I built one that never leaves your Mac.

> [!info] 一句话导读
> title: Your grammar checker uploads every word you type. I built one that never leaves your Mac.

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/rudratosh/your-grammar-checker-uploads-every-word-you-type-i-built-one-that-never-leaves-your-mac-8pj>
> 指标：reactions=6 · 评论=4 · reading_time=6
> 作者：Rudratosh Shastri　|　发布：2026-10-19T18:06:54Z
> 项目链接：<https://brisktype.com/>
> 采集：2026-10-22T09:49:03+08:00　|　id：`3e58e881f67fc73d`

## 正文

---
title: Your grammar checker uploads every word you type. I built one that never leaves your Mac.
published: true
tags: privacy, ai, macos, indiehackers
cover_image: https://rudratoshs.github.io/assets/brisktype/00-cover.png
---

Open the network tab while you use most AI writing tools. Watch what happens as you type an email, a performance review, a message to your lawyer, a half-finished thought you were going to delete. Every keystroke, or close to it, goes up to someone else's server to be "checked."

That's the deal nobody reads the fine print on. To fix your grammar, you hand a cloud service a live feed of everything you write. For a lot of people that's fine. For anyone writing something they'd rather not broadcast, which is most of us some of the time, it's a strange thing to have agreed to.

I got tired of it. So I spent months building **[BriskType](https://brisktype.com)**: a writing assistant that improves your English in every Mac app, runs its AI **entirely on your machine**, and never sends a word anywhere. This is the why and the how.

## The one rule I refused to break

Every design decision came from a single constraint: **no text leaves the device. Ever.** Not to "improve the model," not "anonymized," not "only metadata." None.

That rule is easy to say and annoying to honor, because it rules out the easy path. The easy path is: capture text, POST to an API, get suggestions back, done. Fast to build, cheap to run, and it quietly makes your users' writing someone else's training data. I wanted the opposite, so the model had to run locally, which is only now actually practical.

## Why on-device finally works

Two years ago this would have been a bad idea. Running a language model good enough for grammar locally meant multi-gigabyte downloads and laptop fans screaming. Apple Silicon changed the math.

The M-series chips use **unified memory**, so the CPU, GPU, and Neural Engine share the same memory without copying data back and forth. Combine that with small, quantized models and you can run genuinely useful language inference in a sliver of RAM. BriskType ships two on-device models:

| Model | RAM | Best for |
|---|---:|---|
| **Faster** | ~0.5 GB | quick autocomplete, snappy on 8 GB Macs |
| **Higher quality** | ~1.1 GB | better grammar rewrites, recommended on 16 GB |

That's it. Half a gigabyte to a gigabyte of RAM, sitting idle until you type, producing suggestions in a fraction of a second. No GPU cloud, no API bill, no account.

> **The honest tradeoff:** on-device means it's Apple Silicon only (M1 or later, macOS 14+). No Intel Macs, no Windows. A cloud tool runs anywhere; the price of privacy here is that your hardware does the work, so your hardware has to be able to.

## What it actually does

Grammar is the headline, but the useful part is that it works *everywhere you already type*, not in a separate window you have to paste into.

- **Inline autocomplete.** Gray suggestions appear as you type. Press `Tab` to accept, keep typing to ignore. Same muscle memory as your code editor, now in your email.
- **Grammar fix in place.** Select a sentence, **double-tap `Option`**, and it rewrites it where it sits. `⌘Z` restores the original. No copy, paste, copy back.
- **Snippets.** Type `;brgds` and it expands to your full sign-off. Ships with 215 built-in, add your own. The semicolon prefix means it never fires by accident mid-word.
- **Voice learning.** It notices the greetings and phrasings you actually accept and leans into your tone over time. That profile stays on your Mac and is never used to train anything.
- **Works in 40+ apps.** Anywhere macOS exposes a text field: Mail, Notes, browsers, and more. Slack, Notion, Discord, and Teams are in beta.

## The hard part wasn't the model. It was making it feel instant, everywhere.

Running a small model locally is the part that gets the headlines. The part that actually took the time was making it work *in every app* without you ever noticing it's there. A few of the problems and how I handled them:

**Seeing and editing text in apps I don't control.** macOS only gives one sane way to read and write text across arbitrary apps: the Accessibility API. BriskType asks for the Accessibility permission, reads the text field you're in, and injects suggestions back into it. That permission is also exactly why the exclusions matter so much, an app that can see any text field has to be disciplined about which ones it touches. Password and secure fields are refused at this layer, not filtered after the fact.

**Not running the model on every keystroke.** If you fired inference on every character, the fans would spin and the suggestions would lag behind your typing. The model runs on natural pauses, on a small window of recent context rather than your whole document, in a warm process that's already loaded. That's how a suggestion lands in a fraction of a second and a grammar rewrite in about one.

**Two models for two kinds of Mac.** An 8 GB MacBook Air and a 64 GB studio machine are different budgets. The "Faster" model (~0.5 GB) keeps autocomplete snappy on modest RAM; the "Higher quality" model (~1.1 GB) does noticeably better grammar rewrites if you can spare the memory. You pick, and you can switch.

**Snippets don't touch the model at all.** Expansion is pure string matching, so `;brgds` fires instantly with zero inference. Keeping the deterministic feature deterministic means it never waits on the probabilistic one.

The guiding principle was that the *best* outcome is you forgetting it's running. It should feel like your Mac simply got better at English, not like you installed an assistant you now have to manage.

## The privacy architecture, specifically

"Private" is a word every tool uses, so here's exactly what BriskType does and doesn't do:

- **No cloud processing.** All inference is local.
- **No telemetry, no analytics, no account.** There's nothing to sign into.
- **The internet is touched twice, ever:** once to download the model, and once for a license check that sends your **Mac's name** and no text. After that it runs fully offline. Turn off Wi-Fi and it works exactly the same.
- **Secure fields are excluded by design.** Password fields and secure inputs are off-limits, period.
- **Off by default where it shouldn't be.** Terminals, code editors (VS Code, Xcode), and password managers don't get autocomplete unless you opt in. You can edit the exclusion list.
- **A hard pause.** `⌥⌘B` or the menu bar instantly silences all suggestions and expansions.

The test I held myself to: you should be able to run this on a machine that handles genuinely sensitive writing and not have to think about it. That's only true if the answer to "where does my text go" is "nowhere."

## The pricing is a philosophy, not a tactic

BriskType is **$39, one time.** Not per month. Not per year. One payment, free updates, a license for your Mac.

I did this on purpose, because subscription fatigue is real and grammar help is not a service that should bill you forever. Here's the comparison that made the decision obvious:

![One-time $39 vs subscription cost over three years](https://rudratoshs.github.io/assets/brisktype/01-cost.png)

| | Cost | 3-year total |
|---|---|---:|
| **BriskType** | $39 once | **$39** |
| Grammarly Pro | $144 / year | $432 |
| Category average (other assistants) | $72–108 / year | $216–324 |

BriskType pays for itself versus a $144/year subscription in **about three months**. Over three years you keep roughly **$390** that would otherwise have been an annual tax on fixing your own typos. And because the model is local, there's no server cost pushing me toward a subscription to cover it. The incentives line up: I ship a good app once, you own it.

## How it stacks up

I'll be fair about where it sits. BriskType isn't trying to be a cloud super-suite; it's trying to be the private, own-it-forever option.

| | BriskType | Grammarly | GitHub Copilot | Notion AI |
|---|:---:|:---:|:---:|:---:|
| Runs 100% on-device | ✅ | ❌ | ❌ | ❌ |
| No account required | ✅ | ❌ | ❌ | ❌ |
| Works across all macOS apps | ✅ | partial | ❌ (code) | ❌ (Notion) |
| One-time purchase | ✅ | ❌ | ❌ | ❌ |
| Works fully offline | ✅ | ❌ | ❌ | ❌ |

What the cloud tools give up to run on a server, they get back in raw model size and cross-platform reach. If you want the biggest possible model and you don't mind the upload, Grammarly is excellent. BriskType is for the people who read that sentence and thought "I do mind the upload."

## Who it's for (and who it isn't)

**It's for** professionals writing email and reports all day, developers cleaning up PR notes and Slack threads, non-native English speakers who want natural phrasing, and anyone who's privacy-conscious or just done with another monthly charge.

**It isn't for** Windows or Intel Mac users (Apple Silicon only), people who want their grammar tool to also draft long-form essays from scratch, or anyone who'd rather have the absolute largest cloud model regardless of where the text goes.

## Try it

If "my grammar checker shouldn't need the internet" sounds right to you, that's the whole pitch. It's a one-time $39, it runs on your Mac, and it never phones home with your words.

**[Download BriskType for Mac →](https://brisktype.com)** · One-time $39 · no subscription · Apple Silicon, macOS 14+

I built this solo, and I read everything. If you try it, tell me what breaks, what you wish it did, and which app you most want out of beta. That feedback is the roadmap.

## 评论（4/4）

> **arcwrightai** · 2026-10-19T18:08:58Z　
> Local-first is the right call for anything that touches your writing. Privacy shouldn't be a premium feature.

---

> **Rudratosh Shastri** · 2026-10-19T20:46:00Z　
> now a days, privacy is GOLD

---

> **Sujal Khatri** · 2026-10-20T06:48:12Z　
> The one-rule constraint is what makes this land. "No text leaves the device. Ever." is a principle you can actually test — and "snippets don't touch the model at all" is the perfect example of the discipline it takes. Keeping the deterministic feature deterministic is a detail only someone who honored the constraint would write.
>
> Worth saying: this philosophy extends past AI. Plenty of everyday text chores — deduping a list, converting case, checking word frequency, generating a slug — also get routed to cloud sites when they could run entirely client-side. I ended up building a free set of small text tools for exactly that reason: BulkTextKit. Everything runs in the browser, no uploads, no account. Different problem space from BriskType (no AI involved), same belief that your words shouldn't have to travel anywhere to be processed.
>
> One-time $39 is also the right call. A tool that needs you to keep paying keeps needing you — and needing your data. That tension is worth naming.

---

> **Om Yaduvanshi** · 2026-10-20T13:18:11Z　
> the 'touched the internet twice' line is doing a lot of work, and i mean that as a compliment. most privacy pitches collapse on the exact things they quietly exclude. one small crack in the story though: the license check sends the mac's name. that is not your writing, so the rule technically holds, but it is one identifying string crossing the wire. worth naming in the architecture section before someone else names it for you.

## 关联链接

- https://brisktype.com
- https://rudratoshs.github.io/assets/brisktype/00-cover.png
- https://rudratoshs.github.io/assets/brisktype/01-cost.png

## 导航

- 项目页：[[10-项目/brisktype.com_3a6ac120]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
