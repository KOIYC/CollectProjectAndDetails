---
type: "corpus"
item_id: "aa8e9ffb2c83fea6"
title: "Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50443812"
project_url: "https://github.com/GoogleChrome/modern-web-guidance"
author: "paulirish"
published_at: "2026-11-10T18:01:15Z"
captured_at: "2026-11-11T13:37:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-11"
pub_day: "2026-11-10"
tags:
  - 语料
  - hn_show
  - author_paulirish
  - story_50443812
  - show_hn
  - front_page
metrics: {"points": 321, "comments": 98, "engagement_velocity": 321}
comments_count: 98
comments_total: 98
discovered_via: "hn:show_hn:3d"
---

# Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives

> [!info] 一句话导读
> Browsers natively handle a lot of what used to take 50 lines of JS (or a dependency): `CSS.highlights` for text range highlighting without <span>s everywhere, `…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50443812>
> 指标：点赞=321 · 评论=98 · engagement_velocity=321
> 作者：paulirish　|　发布：2026-11-10T18:01:15Z
> 项目链接：<https://github.com/GoogleChrome/modern-web-guidance>
> 采集：2026-11-11T13:37:17+08:00　|　id：`aa8e9ffb2c83fea6`

## 正文

Browsers natively handle a lot of what used to take 50 lines of JS (or a dependency): `CSS.highlights` for text range highlighting without s everywhere, `<dialog>` and showModal() give you backdrops and ideal focus management, `field-sizing` to auto-grow textareas as the user types.. (Something yesterday's ftrain post touched on [0])Models know about some of these by name, but consistently won't default to using the platform-native solution and instead prefer the incumbent +JS based pattern. We started an effort in Chrome to supplement coding agents with this key domain knowledge and we're shipping our 1.0 today, in collaboration with Firefox, MDN, and Edge.200+ guides (~1.7MB) of curated, hand-crafted implementation best-practices from web experts, updated as the web evolves. (Open source, obv, so.. we'll welcome your bikeshedding ;) Readable versions here: [1]I've spent the last 9 months obsessing over how to ship this as an agent skill + (Agentic RAG) CLI without blowing up your context window. (Or cedeing activation mechanics to MCP dynamic tool search). The skill description is minmaxed for activating on relevant frontend tasks. The RAG work I'm pretty proud of… originally a 500mb native stack down to a ~7MB pure-JS package, ~10ms search on your CPU.We just introduced a deterministic 'legacy-scan' (trained on 30k github repos) to identify old 'n dusted patterns that your agent can modernize. (92% avg precision on held-out repos.)People make a lot of claims about what coding agents are good/bad at. We wanted receipts, so we invested heavily in eval infra [2] to help us hill-climb, but also to identify when knowledge is common enough we can prune our guides. (Ofc, some of the things we thought AI didn't know turned out to be wrong :) We run codex/claude/agy against 200 tasks without the skill and then with.. In total ~1,700 playwright/AST-based assertions. Agents go from 55% pass unguided to 92% guided.Try it out: DISABLE_TELEMETRY=1 npx modern-web-guidance@latest install
 DISABLE_TELEMETRY=1 npx modern-web-guidance@latest search "animate dialog modal"
 DISABLE_TELEMETRY=1 npx modern-web-guidance@latest legacy-scan ./src

If you spot something wrong or weird, give us a holler!Longer write-up on the 1.0: https://developer.chrome.com/blog/modern-web-guidance-v1---0: https://news.ycombinator.com/item?id=504164561: https://developer.chrome.com/docs/modern-web-guidance/guides2: https://googlechrome.github.io/modern-web-guidance-src/

## 评论（98/98）

> **phyzix5761** · 2026-11-10T18:26:29.000Z　
> "Best Practices" are pretty much dead in the AI era. Pretty soon no one is going to read any of the code AI produces and that's a scary thought.

---

> **halflife** · 2026-11-10T18:42:14.000Z　
> Finally.This is exactly what I need when I need it. The amount of pull requests I reviewed with a mess of codes that can be switched to 2 lines of modern features made me write such tools myself, only half assed since I have other things to do.

---

> **cyanydeez** · 2026-11-10T18:52:58.000Z　
> I treat all my code as some kind of stochastic machinery. So atleast one stage, I'd just tell an agent to go through and follow the guide.But I'd not inject all this fluff into the wheels of the machine because it'd just take the "average" of these practices which would be just as useless.

---

> **simonw** · 2026-11-10T18:57:17.000Z　
> Distribution suggestion: in addition to the npm packages you have right now, set up GitHub Pages to publish a markdown index document of the skills at https://googlechrome.github.io/modern-web-guidance-src/skill... (currently a 404)That index page should link to plain markdown versions of all of the documents, and should be designed for search with grep to find the right answers.That way I don't have to install anything at all - provided my agent has the ability to make HTTP requests I can tell it "Look for tips on https://googlechrome.github.io/modern-web-guidance-src/skill..." and it will fetch the index, then navigate to the most relevant documents - no MCP or npm or installation required at all.

---

> **advisedwang** · 2026-11-10T19:07:34.000Z　
> Chrome already has too much power in the browser standards world. The last thing we need is everyone's LLMs to follow Chrome team's guidance on how to do web development. This road leads back to "To view this site, please view in [DOMINANT BROWSER]"

---

> **zeroq** · 2026-11-10T19:16:07.000Z　
> What's the best way to introduce this to a Gemini chat?

---

> **fumar** · 2026-11-10T19:25:33.000Z　
> I added this a few months ago and Claude Doctor has not removed it. It must be working and getting use.

---

> **reedlaw** · 2026-11-10T19:26:46.000Z　
> These skills look better than most, but running my code through the legacy scan only found two issues. So while I still think training beats skills, I'm sure this has its place, especially with weaker models.

---

> **j45** · 2026-11-10T19:33:02.000Z　
> This is a great idea. I think while so much was being built out in the JavaScript ecosystem, awareness about the equivalent feature releases that were done to HTML, CSS, web components, and other technologies didn't keep pace.Of course, it's not perfectly implemented the same in every browser, but that's nothing new.

---

> **cadamsdotcom** · 2026-11-10T19:33:21.000Z　
> Planning to give this one a wide berth.The more "legacy code" is getting written everyday the more the web will be forced to remain backwards compatible...

---

> **PenguinRevolver** · 2026-11-10T19:41:11.000Z　
> I use Firefox after Chrome decided to become a bit of a pain to use on my powerful computers. I was unsure how bias the skills were for Chrome exclusive features, so I decided to ask ChatGPT to analyse the repo. I liked the answer it gave, so here it is:
> https://chatgpt.com/share/6af3712a-03cc-83eb-ad1f-66dd11c886...

---

> **gabrieledarrigo** · 2026-11-10T19:46:49.000Z　
> That's pretty cool!On the other hand, a bit sad: programming nowadays is just arranging a bunch of Markdown files, possibly generated by another bunch of models.Not so exciting, in the end.

---

> **chalmovsky** · 2026-11-10T20:33:27.000Z　
> Amazing! I'm just writing an article about how Alex Russell's quote about 'React being a legacy technology' got, unfortunately, totally ignored.And now this just fell in my lap! Some of the arguments I wanted to make seem to be provide here. Didn't have a chance to take a proper look at it, but it looks very promising and nice!Thank you!

---

> **surround** · 2026-11-10T20:49:54.000Z　
> Here's a list of browser features the skills will tell your agent to use that are stable in Chrome but not supported by Firefox and Safari: CSS @function
>  CSS calc-size()
>  CSS interpolate-size
>  CSS corner-shape
>  CSS border-shape
>  CSS flex-wrap: balance
>  CSS text-fit
>  CSS text-decoration-skip-spaces
>  CSS scroll-axis-lock
>  CSS scroll-target-group
>  CSS :target-current
>  CSS scroll-initial-target
>  CSS container scroll-state queries
>  scrollsnapchange event
>  scrollsnapchanging event
>  HTML focusgroup
>  Element.startViewTransition()
>  CSS view-transition-scope
>  Interest Invokers (interestfor)
>  LanguageModel (Prompt API)
>  LanguageDetector
>  Translator
>  Summarizer API
>  Window.fetchLater()
>  Speculation Rules API
>  Long Animation Frames API
>  VisibilityStateEntry
>  PerformanceSoftNavigation
>  InteractionContentfulPaint
>  Connection-Allowlist
>  CSS url() integrity() modifier
>  HTML meta name="text-scale"
>  HTML template for
>  HTML processing instructions
>  PasswordCredential
>  Promise-returning scroll methods
>  Web App Origin Migration
>  Local Network Access permissions
>  Request.targetAddressSpace
>  beforeinstallprompt event
>
> To be fair, the skills also recommend ~11 features not supported by Chrome itself. And the project does seem concerned with compatibility: "Guiding models to use sensible, lightweight fallbacks."

---

> **dallen33** · 2026-11-10T20:56:09.000Z　
> Paul Irish?? There's a name I haven't though about in ages! I remember following you on Twitter and your website was full of amazing information. Hope you're doing well!

---

> **internet2000** · 2026-11-10T20:59:51.000Z　
> NO THANK YOU. Do not want my agents to contribute to the Chrome monoculture. Chrome is the new IE6.

---

> **adzm** · 2026-11-10T21:16:04.000Z　
> I find this very useful as a human as well

---

> **mococa** · 2026-11-10T21:34:36.000Z　
> More Chromish on web? No thanks.

---

> **tonymet** · 2026-11-10T21:39:21.000Z　
> I recommend saying "contemporary" or "suggested" for transient proposals like this. Having modern change every few years is ambiguous and cliche .These concepts are new, so no one knows if they are any good. They're not modern -- who knows if they will even be put to use?"contemporary", "proposed", "suggested", "compatible" are better fit. I wouldn't dare use "advanced" because many APIs and proposals actually regress earlier behavior.

---

> **pyrolistical** · 2026-11-10T21:50:12.000Z　
> I asked my agent to look at that list and only apply things that work on chrome, Firefox, safari iOS and safari macosCame up with a good list for my project

---

> **codepoet80** · 2026-11-10T21:55:45.000Z　
> I want the opposite of this. I want compatible code -- which is really hard, when there are so many eras to target. So far AI has done a great job of finding that sweet spot -- why would I want a tool that encourages the agent to write less compatible code?

---

> **SoftTalker** · 2026-11-10T23:15:32.000Z　
> Remeber, the features you don't use are the ones you don't have to support, or scramble to replace when they are deprecated.Keep your effing websites simple.

---

> **SoftTalker** · 2026-11-10T23:16:54.000Z　
> > We wanted receipts, so we invested heavily in eval infra to help us hill-climb, but also to identify when knowledge is common enough we can prune our guides.Good god.

---

> **dazhbog** · 2026-11-10T23:34:57.000Z　
> I ask my agent to write ES5 as I am more comfortable with it.. i need to read and maintain that slop somehow..

---

> **ggregoire** · 2026-11-11T00:44:40.000Z　
> Is there a similar project for React? There are so much bad React code and wrong/old design patterns on the internet that surely ended in the training datasets

---

> **efields** · 2026-11-11T01:46:06.000Z　
> Hey: this is great.

---

> **bakkoting** · 2026-11-11T02:37:25.000Z　
> > If you spot something wrong or weird, give us a holler!But how? Hopefully filing an issue on the modern-web-guidance-src repo is the right place? Anyway I filed one for using fromBase64 and toBase64 instead of atob and btoa.But since you're all in on agents anyway you should consider having one look through at least all of the JS, DOM, and HTML spec commits in the last 3-5 years and automatically triaging any that are clear improvements and are not used by agents. Would be pretty straightforward.---Btw, I think it would be very helpful to automatically provide versions of this depending on what browsers you're targeting. I don't want to use anything that hasn't been available in all evergreen browsers for at least a year, for example; I think most developers have a similar standard, or at the very least don't want to use the bleeding edge. And while it is _possible_ to get that from your repo, it takes some effort, either writing a script or letting the agent use its own judgement for every feature. That's work you could do on your end and save the rest of us from needing to.

---

> **hackerbrother** · 2026-11-11T02:42:13.000Z　
> Couldn't this be handled with a deterministic linter?

---

> **christophilus** · 2026-11-11T03:02:34.000Z　
> Well, I read the title as, “Get your coding agent off.” And I thought, wow. These AI fanboys anthropomorphized the LLM a little too much here.

---

> **low_tech_punk** · 2026-11-11T03:20:15.000Z　
> I just want a single llms.txt

---

> **flossly** · 2026-11-11T03:47:03.000Z　
> I prefer to have my templates in a compiled language: not passing a map of strings to a string with interpolation points, but actually "just code" by which I define HTML builders by combining templates/layouts/components in that same "just code".Like HtmlFlow (Java/Kotlin) or kotlinx.html.I pick Tailwind and Alpine.js to go with this approach because: I want to be SSR-first (with small JS-based improvements where they matter most) so NOT and SPA, i want the styling to be close to the HTML code that's being styled (no need to match between CSS definition and usage), and I also prefer to keep my tiny bits of JS close to the HTML it deals with (Alpine makes that easy and provides a clear path for implementing 99% of my JS needs).Like everyone, LLMs code it for me :) But the result is easy to reason about for myself and my LLM. Little vanilla JS. No jQuery. Mostly just some HTML-bound Alpine instructions. And Tailwind everywhere. This way I can look at one place to see how it works: or CTRL-click my way to it.

---

> **lelanthran** · 2026-11-11T05:23:30.000Z　
> > We wanted receipts,Why do people still leave common AI tells in their writing?

---

> **natorion** · 2026-11-10T18:31:34.000Z　
> Best practices are not dead if they result in better user experience. The focus is less on developer ergonomics though - true that.

---

> **paulirish** · 2026-11-10T18:41:46.000Z　
> IMO maintainability is the next frontier. If we just allow coding agents to accrete 1k-LOC solutions to problems, the codebases run quick away from our ability to maintain _some_ level of understanding.So I'll take a 1-line CSS solution over 60 lines of ResizeObserver/setTimeout business. But.. best practices for frontend isn't just the code.. it's ensuring quality UX, that keyboard navigability works, that layout doesn't shift on users.

---

> **brlewis** · 2026-11-10T18:53:05.000Z　
> >Pretty soon no one is going to read any of the code AI produces and that's a scary thought.This is a misconception. Have your favorite agent summarize this video for you: https://www.youtube.com/live/zcLPGC-tvgk?si=YR68aHlFESD053bh

---

> **sublinear** · 2026-11-10T19:05:24.000Z　
> The "modern web primitives" are also not even necessarily the "best practice".Browser-specific implementation gotchas tend to take about a decade to iron out for reasons that never have anything to do with code quality. Users are fickle and so are browser vendors, but that's a different topic.At the end of the day, there's just no escaping lots of manual testing across device and browser combinations if your goal is a polished result and not just something that "works".AI has done nothing to make this problem go away. If anything, it's made it worse because people don't even want to look at the code now!

---

> **trvz** · 2026-11-10T19:16:07.000Z　
> What’s the point of modern Javascript without over complicating things?

---

> **kinlan** · 2026-11-10T19:18:03.000Z　
> https://developer.chrome.com/docs/modern-web-guidance/guides...(we could make this clearer though)

---

> **nico** · 2026-11-10T19:18:20.000Z　
> > That way I don't have to install anything at allIt feels that something like this would be the holy grail of agents. A small agent that has only the minimum necessary built in knowledge. The rest, it just retrieves on the fly when it needs (+ caching)It’s like storing pointers/links instead of the contents

---

> **philipwalton** · 2026-11-10T19:15:01.000Z　
> Mozilla Firefox and Microsoft Edge are also contributors to this project, so this is a cross-browser initiative to help improve how agents build for the web.

---

> **super256** · 2026-11-10T19:17:31.000Z　
> Calm your pitchfork, Mozilla and Edge are both part of Modern Web Guidance.https://github.com/GoogleChrome/modern-web-guidance-src/blob...

---

> **0o777** · 2026-11-10T19:21:56.000Z　
> Both Mozilla and the Google Chrome team are part of the Web Baseline project and this project. They only recommend best practices supported by Chrome, Firefox, Edge, and Safari.https://web-platform-dx.github.io/baseline/

---

> **xnx** · 2026-11-10T19:52:22.000Z　
> Not my opinion, but I do wonder if sharing from a different repo would feel more neutral.

---

> **tonymet** · 2026-11-10T22:01:26.000Z　
> Let the best API win. why hold them back?

---

> **paulirish** · 2026-11-10T20:32:51.000Z　
> Gemini web? Probably simonw's strat from the top comment.There's a plugin for Antigravity that's listed on initial setup (yay bundleware! :) but... yeah if you're using consumer gemini, i'd switch to the Tasks mode because it's more agentic nature helps.In fact I just did this and it works. :p It regular Gemini, it said it did but kinda liked :) So there it'd be> Create a perfect HTML contact form with address fields. Check https://developer.chrome.com/docs/modern-web-guidance/guides... — read completely, don't stop at truncation.

---

> **yh11** · 2026-11-10T21:04:22.000Z　
> why would you ever use gemini for coding at all

---

> **paulirish** · 2026-11-10T19:37:07.000Z　
> Yeah. The legacy scan is tuned to 1) focus on cases where there's a clearly detectable legacy pattern and 2) avoid false-positives. This means it only overlaps with 20% of all the skill's docs. (We'll probably get it to ~50% in another month).In short: I 100% understand your disappointment. :) More coming soon like finding cases to update with Promise.withResolvers, the Array iterators, Object.groupBy, URLSearchParams, etc..

---

> **nchmy** · 2026-11-11T01:19:14.000Z　
> I'm not sure that's just a quote. He's written and said tens of thousands of words on the topic!

---

> **philipwalton** · 2026-11-10T21:01:25.000Z　
> > Here's a list of browser features the skills will tell your agent to use that are stable in Chrome but not supported by both Firefox and Safari:To be clear, the skills document how to use these features to solve common use cases, and then they give your agent a full browser support table for any APIs mentioned that are not Baseline Widely available -- and then your agent can decide whether to use them or not, based on your site's browser support requirements.In most of these cases a cross-browser fallback is also documented.

---

> **hackingonempty** · 2026-11-10T21:48:06.000Z　
> How about details/summary?

---

> **paulirish** · 2026-11-11T02:24:19.000Z　
> <3

---

> **tonymet** · 2026-11-10T22:02:10.000Z　
> no it's not. they publish the APIs. IE was bad because ActiveX was proprietary and private.

---

> **paulirish** · 2026-11-10T23:45:03.000Z　
> what? oh. I mean.. I wrote it all with my lil fingies, but I did pack some jargon in there. :) More plainly...We built rigorous tests to verify this actually works, and to know when models no longer need the advice.

---

> **rewgs** · 2026-11-11T00:02:37.000Z　
> "hill-climb" is the most aggressively LinkedIn speak I've ever encountered in the wild.

---

> **socalgal2** · 2026-11-11T01:26:37.000Z　
> Yes, it's "Never use React". Simplehttps://infrequently.org/2024/11/if-not-react-then-what/

---

> **philipwalton** · 2026-11-11T02:51:38.000Z　
> Thanks for filing! Yes, the modern-web-guidance-src repo is the right place:
> https://github.com/GoogleChrome/modern-web-guidance-src> Btw, I think it would be very helpful to automatically provide versions of this depending on what browsers you're targeting.This should work today (though not exactly in the way you describe). The skill tells the agent how to interpret guides based on browser support signals it gets from context (e.g. the prompt itself, or AGENTS.md).You can see those instructions here: https://github.com/GoogleChrome/modern-web-guidance-src/blob...

---

> **aidos** · 2026-11-10T20:34:55.000Z　
> Once again, thank you for all the work you and the team have done to improve the web and the experience for developers working with it.

---

> **noosphr** · 2026-11-10T21:27:29.000Z　
> You just regenerate the codebase, like how you do a recompile in C. Writing code is 2026 is worth as much as writing machine code was in 1996.

---

> **ozim** · 2026-11-10T19:08:41.000Z　
> Ugh it is Uncle Bob, not going to torture AI with this guy.But the fun part is that all of the proper software engineering practices are aimed at lowering amount of context a developer has to keep in his mind. So it directly applies to agent context. Less verbose code, less tokens to burn, separation of concerns, lower chance agent breaks something unrelated etc.

---

> **vik0** · 2026-11-10T19:09:58.000Z　
> >>Pretty soon no one is going to read any of the code AI produces and that's a scary thought.>This is a misconception. Have your favorite agent *summarize this video for you*: https://www.youtube.com/live/zcLPGC-tvgk?si=YR68aHlFESD053bhI can't tell if you're joking here

---

> **zeroq** · 2026-11-10T20:18:04.000Z　
> Exactly.I've recently finished a browser game specifically targeting an old iPad Air 1 we had lying around the house.I had a working version after a weekend, but it took me a month to make it run smoothly on an over 10 years old mobile device. And the most recent browser available is almost 10 years old.Surprisingly I didn't missed too many "modern" JS features, as these were mostly functional programming oriented which doesn't play well with optimization anyways, and the ES6 was more than enough as a programming platform.Anyway, what I'm trying to say is that "the best practice" should be making your apps fast and accessible - as much as you can without having to sacrifice something you value - instead of chasing the latest and shiniest.Don't be a fashion driven developer. :)

---

> **paulirish** · 2026-11-10T19:28:59.000Z　
> Aye. I like the idea, Simon. The token cost of the index is high enough I wouldn't suggest the technique for regular use but.. agree that for occasional users it should suffice.We'll make this happen. :)

---

> **jph00** · 2026-11-10T19:51:37.000Z　
> If you rename that file to "llms.txt" it'll be a bit more discoverable.

---

> **kohukohunui** · 2026-11-10T20:32:49.000Z　
> It looks like the markdown has cross references that assume that the cli approach is used, it would be nice to separate the content from the tooling to access.

---

> **paulirish** · 2026-11-10T19:41:25.000Z　
> In reality that's pretty much what we got here. Very progressive disclosure centric. There's a 'install' command exists because the ecosystem doesn't have good cross-agent ergonomics for installing skills. (Which bums me out).But yeah.. big corpus of valuable context × minimal agent footprint = happy place.

---

> **mtrovo** · 2026-11-10T20:07:58.000Z　
> If created properly, skills are already something like that. You have a front matter summary always available to the agent. The agent can request the full skill content on demand, which might contain additional linked documents with details about APIs and schemas being used, deeper documents about niche subtopics, scripts to help with subtasks, etc.

---

> **troupo** · 2026-11-10T22:00:37.000Z　
> That's why it seems to skip the most egregious of Chrome-only APIs and focuses on areas where there's large cross-browser agreement.

---

> **phendrenad2** · 2026-11-11T02:05:17.000Z　
> They back it because they have no choice. We have no real independent browsers in 2026. And it's sad that the fact that we don't have independent browsers is being twisted into proof that Google doesn't have much power.

---

> **girvo** · 2026-11-11T00:05:16.000Z　
> Because Google/Chrome should’ve been split up under antitrust grounds, instead of the “too hard let’s not bother” judgment they ended up with.

---

> **zeroq** · 2026-11-10T21:39:44.000Z　
> Argon is not available in agy for Pro users.

---

> **seige** · 2026-11-11T04:04:17.000Z　
> Just here to voice this again. I ran it on my project and it found 3 issues. There are far more :)

---

> **surround** · 2026-11-10T21:14:45.000Z　
> The line between documenting and instructing is blurry in many cases. For example, these statements are meant to document best practices to the agent, but they sound like instructions:"DO use fetchLater()...""Your own code MUST call fetchLater() directly..."https://github.com/GoogleChrome/modern-web-guidance/blob/mai...But yes, the skills do document compatibility and fallbacks well.

---

> **hatthew** · 2026-11-10T22:21:37.000Z　
> In my experience, it's difficult to suggest something to an LLM in a way that it doesn't interpret as a command, unless I explicitly list conditions (which it will take as law rather than guidance).

---

> **lelandfe** · 2026-11-11T00:24:35.000Z　
> The default behavior for this "web best practices" tool which steers people away from "legacy patterns" has agents using Limited Availability features with complex and nuanced[0] fallbacks?This would be deeply surprising to me, and I am the target audience for this repo. I'd expect the default here to be Widely Available only with some opt-in for the courageous. I don't know that I'd even enable it.[0] https://github.com/GoogleChrome/modern-web-guidance/blob/4dd...

---

> **philipwalton** · 2026-11-10T23:33:03.000Z　
> The details/summary features are covered in the accordion guide here: https://developer.chrome.com/docs/modern-web-guidance/guides...If you scan to the bottom of the guide under the "Fallback strategies" section, you can see the recommendations for how to deal with the aspects of details/summary that aren't Baseline widely available (e.g. mutually exclusive details).

---

> **ShinyLeftPad** · 2026-11-11T04:22:30.000Z　
> a barely coherent ramble by a Microsoft engineer feat. an exquisite conflation of React/using libs like lodash or moment.js/the idea of frameworks, casually dropping false dichotomies between using React and delivering semantic HTML with progressive enhancement, drive-by smearing any use of frameworks by calling it "frameworkism" and equating it with religion, with a side of amusing bombshells like (exact quote)> prohibiting the spread of React (and other frameworkist totems) by policy is an incredible cost savings and a helpful way to reorient teams towards delivery for usersisn't "simple".

---

> **bakkoting** · 2026-11-11T03:06:55.000Z　
> > This should work today (though not exactly in the way you describe). The skill tells the agent how to interpret guides based on browser support signals it gets from context (e.g. the prompt itself, or AGENTS.md).Right, my point is that I don't want to spend a bunch of time and tokens loading the skills and having the agent reason through whether they apply based on browser support. I want that to be automated so that it only loads in the first place those things that are actually applicable. Having a prose description is not a substitute for automation; it is almost always better to do things mechanically rather than asking the agent to do it, in cases where it is possible to do mechanically.I think this matters even if you're at Google and tokens are free but it _definitely_ matters for the rest of us.

---

> **1shooner** · 2026-11-11T04:03:54.000Z　
> Couldn't this be a simple deterministic build from the provider rather than mass replication of inference for essentially every user?

---

> **runeb** · 2026-11-11T00:52:12.000Z　
> Relevant post "Regenerative Software"https://aicoding.leaflet.pub/3majnyfydzs2y/l-quote/10.0_0-10...

---

> **soon_to_be_sb** · 2026-11-11T04:33:04.000Z　
> Jesus! what a horrible idea!Are you in the business of selling tokens/electricity/gpus by any chance? Then good for you!But terrible for everyone else....

---

> **brlewis** · 2026-11-10T19:26:58.000Z　
> I am not generally against using AI to reduce the amount of information you need to pay attention to, and I was not joking. There are multiple places in that interview with good articulation of the reasons why software fundamentals still matter, and what happens when you don't look at at least some of the AI-generated code.

---

> **kinlan** · 2026-11-10T19:57:57.000Z　
> yeah that's fair. the infrastructure we are on isn't the most flexible (we will soon move to a newer more custom platform but that's a little way a way)

---

> **philipwalton** · 2026-11-10T23:57:08.000Z　
> Cross-browser compatibility has been a guiding principle for this project from the start. See: https://youtu.be/bo3i0FzDUYo?si=EqIgY_Kh_r_hSgdE&t=686Also Mozilla only joined in the last few weeks, so they haven't yet had a big influence on the project (though I expect they will going forward).

---

> **tonymet** · 2026-11-11T00:34:16.000Z　
> because the $200m+ spent public & private on the Microsoft antitrust did a public service? talk about a farce and a waste of resources.Google hardly has a monopoly. The app experience is very diverse. If anything, Apple is much more anticompetitive than Google.Or is it that you resent any success?Google gives away Chromium for free. Microsoft & Linux distros use it.Thanks, this is one of the most laughable comments of the day.

---

> **philipwalton** · 2026-11-10T21:42:55.000Z　
> Agreed the line can be blurry, but I want to stress that the goal of this project is NOT to push Chrome-only APIs on users.The mental model we've been using on the team is:If you hired an expert web development consultant to build X, what would they recommend as a best practice? When does it make sense to use the new API (because it provides real benefits) vs. when does it make sense to wait until it's available everywhere?To use your `fetchLater()` example, this is a case where the `fetchLater()` API legitimately solves a very real problem for people trying to build accurate analytics or telemetry features, see: https://nicj.net/beaconing-in-practice/And lots of companies actually are already using `fetchLater()` in production now because of its increased reliability.

---

> **magicalist** · 2026-11-11T03:07:42.000Z　
> > The default behavior for this "web best practices" tool which steers people away from "legacy patterns" has agents using Limited Availability features with complex and nuanced[0] fallbacks?You have causality reversed here. If you need to detect if the page was loaded in the foreground or background, it is nuanced and (relatively) complex. Therefore it's good for your agent not to just assume document.visibilityState is all it needs to check, or you're going to be getting seemingly impossible log entries pretty quickly.

---

> **philipwalton** · 2026-11-11T04:54:20.000Z　
> If your feature use policy is that you will never use any feature unless it's supported in at least X, Y, and Z browsers, then yes something like this would be possible. But most sites don't have a policy like that.Most sites are willing to use some features as a progressive enhancement, whereas other features they won't even consider using unless it's in 99+% of their users' browsers.And unfortunately there's no easy way to make that decision for users on a feature-by-feature basis, because it all depends on what use case they're trying to accomplish, and what will happen if the feature is not available (given that particular use case).So our approach is to (1) explain in the guide how to implement the use case with the modern feature, (2) explain why the modern feature is the preferred solution (e.g. what the user benefit is), and then (3) explain how to implement a fallback solution if the feature is not available.I think we could potentially experiment with some version of what you're describing, like a config option where we only surface guides that have robust, widely-available fallbacks, and where we have high confidence that it makes sense for the majority of sites to be following the recommendations in the guide.I'll raise it with the team.

---

> **philipwalton** · 2026-11-11T04:55:17.000Z　
> I believe I answered your question in this reply: https://news.ycombinator.com/item?id=50449873

---

> **noosphr** · 2026-11-11T02:59:31.000Z　
> I've not read text with such a high fraction of AI slop in a while. The heady days of a year ago.

---

> **noosphr** · 2026-11-11T04:33:34.000Z　
> Yes, just like compilation was.

---

> **drawfloat** · 2026-11-10T20:48:57.000Z　
> Why don't you just quote them then? Or quote whatever the LLM you used gave.

---

> **cma** · 2026-11-10T22:32:36.000Z　
> I think I can guess from corporate incentives why Chrome supports fetchLater and some others don't.

---

> **lelandfe** · 2026-11-11T04:09:27.000Z　
> Tree, forest.You're making this into a false binary which is wrong (the alternative to adopting Limited Availability features is not "document.visibilityState is all it needs to check"). But responding to my one example is also going to cause us to miss the point I'm making entirely.

---

> **soon_to_be_sb** · 2026-11-11T04:37:36.000Z　
> lol are you stupid?

---

> **philipwalton** · 2026-11-10T23:26:49.000Z　
> It's currently being added to WebKit: https://github.com/WebKit/WebKit/pull/73271Regarding corporate incentives: I was involved in the design of this API, so I know the history. It was proposed many years ago as a solution to make it easier for RUM analytics providers to measure Core Web Vitals metrics that needed to account for more than just page load (e.g. layout shifts and slow interactions can happen any time, not just during page load).The RUM providers we worked with were reluctant to wait until page unload to send telemetry data because it resulted in too many lost beacons, so what they do instead is send beacons every few seconds with the most up-to-date payload.The `fetchLater()` API enables them to send just one beacon, which is good for users and also reduces their server load.

---

> **ricardobeat** · 2026-11-11T00:50:37.000Z　
> Why was 'fetchLater' chosen over a reliable way to trigger fetch from 'unload' or a similar event, or inversely, adding a 'sendLater' option to sendBeacon? Feels like a bolted-on API for a very specific use case, when the same thing could be built from better primitives?It's a bit sad that browsers now have two different, "standard" APIs created entirely for the purpose of user tracking, as if things weren't already bloated enough.

---

> **philipwalton** · 2026-11-11T01:21:03.000Z　
> These exact questions came up (from Apple) during design review. If you're interested you can read the discussion here: https://github.com/WebKit/standards-positions/issues/85#issu...

---

> **fn-mote** · 2026-11-11T01:41:45.000Z　
> Spot-on amazing linking exactly to the relevant discussion.I’m really glad to see this not evolve into a flame war as well.

## 关联链接

- https://developer.chrome.com/blog/modern-web-guidance-v1---0:
- https://developer.chrome.com/docs/modern-web-guidance/guides2:
- https://googlechrome.github.io/modern-web-guidance-src/
- https://news.ycombinator.com/item?id=504164561:

## 导航

- 项目页：[[10-项目/github.com_5175b6a2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
