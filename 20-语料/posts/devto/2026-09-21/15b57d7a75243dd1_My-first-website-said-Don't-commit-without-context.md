---
type: "corpus"
item_id: "15b57d7a75243dd1"
title: "My first website said \"Don't commit without context.\" I never committed it at all."
source: "devto"
source_name: "dev.to"
url: "https://dev.to/earlgreyhot1701d/my-first-website-said-dont-commit-without-context-i-never-committed-it-at-all-5d57"
project_url: "https://chatgpt.com/g/g-68af555e39808191a53fcd1ef6451fda-dr-kahlo"
author: "Earl Grey"
published_at: "2026-08-21T18:45:03Z"
captured_at: "2026-09-21T02:23:40+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-21"
tags:
  - 语料
  - devto
  - buildinpublic
  - ai
  - webdev
  - beginners
metrics: {"reactions": 27, "comments": 6, "reading_time": 7}
comments_count: 6
comments_total: 6
discovered_via: "devto:buildinpublic"
---

# My first website said "Don't commit without context." I never committed it at all.

> [!info] 一句话导读
> The renewal notice came and I decided to let it go.

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/earlgreyhot1701d/my-first-website-said-dont-commit-without-context-i-never-committed-it-at-all-5d57>
> 指标：reactions=27 · 评论=6 · reading_time=7
> 作者：Earl Grey　|　发布：2026-08-21T18:45:03Z
> 项目链接：<https://chatgpt.com/g/g-68af555e39808191a53fcd1ef6451fda-dr-kahlo>
> 采集：2026-09-21T02:23:40+08:00　|　id：`15b57d7a75243dd1`

## 正文

The renewal notice came and I decided to let it go.

threadkeeper.io was my first idea and my first website. I bought the domain in August 2025, about six weeks after a community college AI summer camp where I was writing files with names like `ccc-ai-pdf-project` and describing them in my own README as a beginner Python project. Then I shipped a domain, a blog, a CLI, and a manifesto.

Before I let it lapse I went back to look at it one more time. Sentimental. Five minutes, tops.

Then I tried to figure out where the source code lived, and realized it did not live anywhere.

The site was on Spaceship. I had built it there, in the browser, and never put it in version control. Not once. There was no repo to clone, no local folder, no backup. The only copy of my first website that existed in the world was the one running on a server I had four days left on.

The tagline on that site, in cyan, at the top of the page, was **"Don't commit without context."**

I never committed it at all.

## I did not have the source code to my own website

So the first job was not nostalgia. It was extraction.

I pulled all eight pages and every asset off the live server before it went dark: the landing page, the blog, three posts, the Dr. Kahlo page, and the Ariadne Clew recap app I built for an AWS hackathon. Nineteen files. `sitemap.xml` claimed there were four pages, which tells you how much I trusted my own sitemap in 2025. The rest I found by following links.

That archive is now public, with a SHA-256 for every original file so anyone can verify nothing drifted in the rescue:

**[earlgreyhot1701d.github.io/threadkeeper-archive](https://earlgreyhot1701d.github.io/threadkeeper-archive/)**

It is committed now. A year late.

## I named a file dom_js.js and did not blink

Here is the first thing I found once I could actually read my own code.

The Ariadne Clew app had seven JavaScript modules. Two of them were named with snake case and a suffix: `api_js.js`, `dom_js.js`, `main_js.js`. Four were camelCase with no suffix: `utils.js`, `theme.js`, `exportMarkdown.js`, `dragDrop.js`.

Two naming conventions. One folder. Seven files.

And look at `dom_js.js` for a second. That name reads as "dom, js, dot js." The suffix repeats the extension. I know exactly where that came from, because I did it constantly in 2025: a code block in a chat window gets labeled `dom_js`, and you save it with the label plus `.js`, and you move on because it works.

The filename is a receipt. It records that these files were copied out of a conversation instead of created inside a project.

## One line broke every button on the page

`main_js.js` opens with six imports. The third one is this:

```js
import { getElement, getValue, ... } from './dom.js';
```

The file on the server was `dom_js.js`.

ES modules resolve the entire import graph before executing any of it. One file missing means the module never runs. There is no partial execution and no fallback to the five imports that resolved fine.

Every event listener on that page lived inside `main_js.js`. Form submit. Copy button. Export button. Theme toggle. Drag and drop. The initial UI state. None of it ever attached.

The page rendered beautifully and did absolutely nothing.

![Screenshot of threadkeeper.io/ariadneclew in Chrome with devtools open. The Ariadne Clew page renders perfectly on the left, headline, tagline, session ID field, and three buttons all in place. On the right, the console shows a single red error: Failed to load resource, the server responded with a status of 404, dom.js line 1.]
![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/0qyo5tyg62t026nx1pe3.png)

That is my own browser, on the live site, days before it expired. A perfectly rendered page on the left and one red line on the right.

Here is the full trace, because the console only shows you the thing that failed:

![Capture report from threadkeeper.io/ariadneclew listing eight module requests. Seven return status 200. scripts/dom.js returns 404 and is highlighted in red. Below it, four DOM checks confirming the module never executed: status text empty, copy button not disabled, export button not disabled, theme attribute unset.]
![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/0gxjibfsxvszqxzxbf79.png)

Seven of eight resolved. Four independent confirmations that the module never ran.

It had been that way for at least eleven months. I am dating that from the blog post in September 2025 where I linked to the app, so the real number could be longer. I have no deploy timestamp, because of course I do not.

**You can watch it fail yourself.** The archive preserves the bug exactly as it shipped:

**[Open the broken version](https://earlgreyhot1701d.github.io/threadkeeper-archive/original/ariadneclew/)**, press F12, check the Network tab. `scripts/dom.js` is the only one of eight requests that 404s. Then open [the fixed copy](https://earlgreyhot1701d.github.io/threadkeeper-archive/site/ariadneclew/) and watch the status line actually say "Ready to generate recap."

Please do not open a PR fixing it. It is preserved on purpose.

Here is the part I want to be careful about, because the easy version of this story is "I was bad at coding" and that is not quite it. Nothing in that stack could have caught it. No build step. No bundler. No linter with import resolution. No TypeScript. No tests. Any one of those fails loudly on a missing import before it ever reaches a server.

I had vanilla JavaScript on a CDN with no build step, and I would still defend that choice for a small project today. The tax is that nothing verifies your import graph for you. I did not know there was a tax. So I paid it for eleven months without noticing.

## I gave my first AI a fake PhD

The site had a whole page for Dr. Kahlo, a custom GPT I built to review my code. I gave her a backstory. Straight from the 2025 page, unedited:

> Her fictional résumé includes 30 years of FAANG-level experience, a PhD in code quality, and native fluency in Python, JavaScript, JSON, and React. Her aesthetic is Frida meets formatter. Her soundtrack is Lila Downs.

And then, one paragraph later:

> She does not flatter. **She does not hallucinate.** She reviews with surgical honesty.

I wrote that in August 2025. I am leaving it exactly where it is.

For what it is worth, [Dr. Kahlo is still running](https://chatgpt.com/g/g-68af555e39808191a53fcd1ef6451fda-dr-kahlo). She outlived the website that introduced her. If you want the 2026 version of my relationship with AI code assistants, that is [Breaking Build](https://dev.to/earlgreyhot1701d/breaking-build-kiro-and-claude-delivered-exactly-what-i-asked-and-it-wasnt-what-i-wanted-27l5), where Kiro and Claude gave me exactly what I asked for and it was not what I wanted.

## If you just shipped your first thing

Put it in a repo. Today. Even if the code is bad, especially if the code is bad.

Not for the version history, not because a recruiter will look at it. Because hosting is rented and repos are yours, and one day you will want to go back and look at what you were thinking, and "it was on a server I stopped paying for" is a sad sentence to have to say about your own work.

That is the whole lesson and it costs you about ninety seconds.

## I am not going to tell you what it means yet

Going back through that site did something to me. I could feel the distance. It is a strange thing to read your own writing from a year ago and recognize the voice completely while wincing at the artifact.

And I sat down to write a lookback about how far I have come, and stopped, because I noticed I was about to make a bunch of confident claims about my own growth with zero evidence behind them.

Which is the exact thing I built a study to avoid.

[Clew Chronicles](https://github.com/earlgreyhot1701D/clew-chronicles) is an n=1 longitudinal study of my first thirteen months of AI-assisted building, July 2025 through August 2026. Fifty-seven repositories. The corpus closed on August 9. The hypotheses are registered and frozen, and two of the ten are, in essence, "my memory of what mattered is probably wrong" and "the data must be allowed to contradict me."

Forty-nine of those repositories are still unclassified, sitting in a spreadsheet waiting on me. That step is human coding. No model is permitted to touch it, by rule.

So I am not going to tell you what changed. I will tell you when I have the data, and I will tell you if I was wrong.

## The thread

ThreadKeeper became Ariadne Clew during an AWS hackathon, when the project outgrew a name that just described what it did. A clew is the ball of thread Ariadne gave Theseus so he could find his way back out of the labyrinth. That became [Ariadne Clew](https://github.com/earlgreyhot1701D/Ariadne-Clew), and then a whole suite of tools with Clew in the name.

The domain dies this week. The idea is the biggest it has ever been.

The old footer said "Flag planted August 26, 2025." I did not plan for the anniversary, but the first commit on the original ThreadKeeper repo is dated August 20, 2025, and I went back for the site on August 20, 2026. Twelve months to the day, entirely by accident.

I was so proud of that thing. In the launch post I wrote, "I officially launched ThreadKeeper with working snapshots, insights, and a functional TypeScript CLI. Hell yes." I still like her. She had no idea what she did not know, and she shipped anyway.

Flag planted again. I will report back with data.

---

Quick context if you are new here: I came to code from the courtroom. Jury services to AI builder, self-taught, learning in public. I direct, the agents generate, I validate and decide. I build the Clew Suite and a handful of civic tech tools. That is the lens I am writing from.

**The archive:** [live](https://earlgreyhot1701d.github.io/threadkeeper-archive/) · [source](https://github.com/earlgreyhot1701D/threadkeeper-archive)

AI Assisted. Human Approved. Powered by NLP.

## 评论（6/6）

> **Marcus Kim** · 2026-08-21T18:48:13Z　
> Seven of eight module requests resolving while dom.js returned a 404 is a sharp example of why "it renders" is not a release test. The mismatch between dom_js.js on the server and ./dom.js in main_js.js also captures how tiny naming drift can disable every listener without disturbing the page's appearance. Recovering nineteen files with four hosting days left-and finding more pages through links than sitemap.xml-makes the ownership lesson concrete. For a no-build vanilla JavaScript project, I'd keep the simplicity but add one deployment smoke test that loads every module and exercises one critical interaction; minimal tooling is a.

---

> **Earl Grey** · 2026-08-23T02:10:29Z　
> Thank you for this. "It renders" is not a release test is going straight into my notes. That was exactly the gap. I was checking the only thing I could see and calling it done.
>
> On the smoke test, I have to admit something. I ran that check while rebuilding the archive, because I needed to prove the rescued copy actually worked. Load the page, fail on any request over 400, confirm one interaction. It separated the two versions instantly. The original 404s on dom.js with an empty status line. The fixed copy comes back with "Ready to generate recap" and the buttons wired up. Roughly twenty lines.
>
> So the tooling I needed in 2025 was about one file. I just did not know that category of thing existed yet. 🙂

---

> **Mustafa ERBAY** · 2026-08-21T19:29:13Z　
> What makes this story interesting isn’t really the missing dom.js file — it’s the missing verification layer.
>
> Vanilla JavaScript without a build step is perfectly valid. But once you remove the compiler, bundler, TypeScript, and import-resolution checks, you also remove several places where this kind of mistake would normally become impossible to ship.
>
> The page rendering successfully makes it even more dangerous because it creates a false positive: the document loaded, but the application didn’t.
>
> A tiny deployment smoke test — load the page, verify there are no module 404s, then exercise one critical interaction — would probably have caught an eleven-month-old bug in seconds.
>
> And I think there’s a broader AI-assisted development lesson here too: generated code isn’t the interesting risk. Unvalidated code is. Whether the code came from Claude, a Stack Overflow answer, or our own keyboard matters much less than whether the delivery pipeline can prove the application actually works.
>
> Also, preserving the broken version instead of quietly fixing it is fantastic. Bugs are sometimes better documentation than documentation. 🙂

---

> **Earl Grey** · 2026-08-23T02:28:13Z　
> I appreciate your comments.
>
> And agreed, and it isn't only code. Anything a model hands you has this problem, including prose. The question is always whether something downstream can tell the difference between shipped and working.
>
> 🙂

---

> **Alex Shev** · 2026-08-23T17:35:56Z　
> The useful test for “My first website said "Don't commit without context." I never committed it at all.” is whether the lesson changes a team decision, not just a local implementation. I’d capture the failure signal, the guardrail that caught it, and the smallest regression test that keeps it from returning. That turns a good postmortem into something another team can actually reuse.

---

> **alexio** · 2026-08-26T10:35:15Z　
> That’s a classic example of overthinking the workflow until nothing gets shipped. Context is valuable, but the first version still needs to be committed, tested, and improved. The same practical mindset applies to tools like a scissor electric—the real value comes from putting the tool to work on everyday cutting tasks rather than focusing only on specifications.

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/0gxjibfsxvszqxzxbf79.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/0qyo5tyg62t026nx1pe3.png
- https://dev.to/earlgreyhot1701d/breaking-build-kiro-and-claude-delivered-exactly-what-i-asked-and-it-wasnt-what-i-wanted-27l5
- https://earlgreyhot1701d.github.io/threadkeeper-archive/
- https://earlgreyhot1701d.github.io/threadkeeper-archive/original/ariadneclew/
- https://earlgreyhot1701d.github.io/threadkeeper-archive/site/ariadneclew/
- https://github.com/earlgreyhot1701D/Ariadne-Clew
- https://github.com/earlgreyhot1701D/clew-chronicles
- https://github.com/earlgreyhot1701D/threadkeeper-archive

## 导航

- 项目页：[[10-项目/chatgpt.com_4d4cf5e6]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
