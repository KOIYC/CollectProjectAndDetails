---
type: "corpus"
item_id: "29e0c595f0ac63a4"
title: "Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49833867"
project_url: "https://github.com/devdotfast/whiteboard"
author: "sidharthkmenon"
published_at: "2026-09-24T17:21:36Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_sidharthkmenon
  - story_49833867
  - show_hn
  - front_page
metrics: {"points": 252, "comments": 95, "engagement_velocity": 252}
comments_count: 95
comments_total: 95
discovered_via: "hn:show_hn:3d"
---

# Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design

> [!info] 一句话导读
> Hello! We’re Sid, Alex, Ketan, and Milan. We’re building Whiteboard (https://whiteboard.dev.fast/), an open-source desktop app where humans and agents can archi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49833867>
> 指标：点赞=252 · 评论=95 · engagement_velocity=252
> 作者：sidharthkmenon　|　发布：2026-09-24T17:21:36Z
> 项目链接：<https://github.com/devdotfast/whiteboard>
> 采集：2026-09-25T13:42:25+08:00　|　id：`29e0c595f0ac63a4`

## 正文

Hello! We’re Sid, Alex, Ketan, and Milan. We’re building Whiteboard (https://whiteboard.dev.fast/), an open-source desktop app where humans and agents can architect software together in a common workspace. Here’s our repo: https://github.com/devdotfast/whiteboard.We were missing the feeling of a “whiteboard session” with another dev where you leave with a deep understanding of a system, so we built this app for ourselves. Whiteboard plugs into the tools you already use - e.g. Claude Code, Codex, etc. – and gives your agent an SDK to draw on an in-app canvas to describe its work. We began with an MVP based on HTML artifacts and started rethinking the app as we ran into limitations:1. Built on top of CodeOSS: We found that in pure HTML tools it was hard to connect a spec or diagram to code. In Whiteboard, when you click on visualizations like a sequence diagram, an entity relationship diagram, or a quote from the agent’s trace, you can jump to the underlying code directly. When navigating code, you get keybindings and LSP support from VSCode out of the box. We’ve found this is especially valuable because tradeoffs are often only discovered after a first pass at implementation (re: slop)2. Semantic diff viewer: we wrote a semantic, AST-aware diff viewer in Rust so you can only view the code changes which are relevant to you [1]. We’ve set up some sane defaults: large added functions are summarized as pseudocode, and things like unit tests and large documentation changes are collapsed / hidden. This is all customizable with a WASM-based plugin system.3. Decision Log: We found it difficult to reason about what set of decisions our agents made autonomously. So we built tools for agents to query and link their own traces to the Whiteboard, so you can understand how the requirements that you set were implemented, and understand what decisions your agent made autonomously.Here’s a quick demo video explaining more: https://www.youtube.com/watch?v=ChPn3ftULWEFolks at companies like Salesforce and Modal are using Whiteboard today as a review tool for architecture or spec-level changes – really any change where they want to be involved:1. Reviewing your own coding agent’s work: because Whiteboard makes it easier to review large amounts of code, folks will typically have their AI agents create a prototype and a corresponding Whiteboard session so they can iterate on the design.2. Reviewing other people’s changes: We’ve found that Whiteboard is particularly helpful when composed with tools like Greptile. For example, you can run an automated code reviewer on small changes and escalate to a Whiteboard session for the changes that require human judgement.Why we built this: we’re four buddies from college who quit our jobs as tech leads right before agentic coding became industry standard. As we iterated towards an MVP for a previous idea, we struggled to maintain a comprehensible codebase while reaping all the velocity benefits of agentic coding. As more PRs were merged without our understanding, we felt a ‘cognitive debt’ begin to seep in, until it became difficult for us to even contribute to the system [2].We’re releasing our desktop app under an MIT license. Please poke through and feel free to contribute! Eventually we’ll charge companies for a hosted web version that manages whiteboard session creation alongside features like trajectory storage and multiplayer reviews. Everything will always remain self-hostable.Thanks for reading, and we hope you try it out! We would love to hear any feedback and to learn from your expertise.Here’s are the project links again: https://github.com/devdotfast/whiteboard, and you can install (for MacOS + Linux) at https://install.dev.fast[1] diffs library: https://github.com/devdotfast/diffr
[2] Credit for the term ‘cognitive debt’ goes to https://www.geoffreylitt.com/2026/07/02/understanding-is-the...

## 评论（95/95）

> **souvlakee** · 2026-09-24T17:53:09.000Z　
> Loved that zed-inspired landing pages.

---

> **komposit** · 2026-09-24T17:53:42.000Z　
> Cool idea will give this a try!

---

> **saadn92** · 2026-09-24T18:02:20.000Z　
> What does pricing look like?

---

> **bbor** · 2026-09-24T18:04:39.000Z　
> Oh WOW, cool to see a technique that'll be everywhere in 12 months (the fake pen drawing animations + streaming diagrams as they're produced) first be announced. Do we still do "First!" comments, y'all?~~[EDIT: you need to put "only for macOS" in way more prominent places, all over -- that offends my soul greatly and may Linus frown upon you all]~~ [EDIT2: I was mistaken!]This all looks really solid. That said, two remarks:1. The integration with OS LSPs is quite fun and commendable. Is it possible that the diagrams might get their own LSP, someday? Or is better just staying as direct TS callsites?2. The choice of the word "IDE" seems like it might get you in trouble, given the small "cannot edit files" detail. Any comments on the decision there, as opposed to, say... "brainstorming tool"? Or hell, "[architectonic] harness"?3. The psuedocode "semantic diff" thing is an incredible idea, wow. Props there.4. This language kinda concerns me: "how the requirements that you set were implemented". In my highly-arbitrary development flow, it ideally goes `idea -> spec/reqs -> plan -> test -> impl -> eval -> land -> review`, and this kind of tool seems explicitly targeted towards just the second and third with some partial coverage of their neighbors on either side. More concretely: by adding implementation, don't you lose a powerful specificity selling point and now have to compete with all full harnesses?5. Suggesting "GPT-6 Luna and Claude Opus 5.5" is presumably a typo? Cause the equivelant of Opus 5.5 is Astra, and even then not really.

---

> **nthypes** · 2026-09-24T18:10:45.000Z　
> Vibe-coded landing pages are an instant “no thanks” for me.

---

> **2001zhaozhao** · 2026-09-24T18:17:16.000Z　
> This is definitely getting at least some things right about how we work with agents today, specifically that we often work at the architecture level, and we need a better alternative to the current Plan Mode offered by coding agents to efficiently architect software at a high level, which is more visual and offers better back-and-forth incrementation with the agent than simply "reject final plan with X message".From the website demos i definitely think this is a clean interface, although I don't know how much better this is compared to some simple custom Mermaid format, which the agent can write as artifact files and present to users. Zooming out, this app seems like 1 feature (a MCP with a GUI attached to it) rather than an entire product.Also, I don't know if asking the agent to write specific code changes into the plan is a good idea. I think maybe that a "plan -> approve -> write code" would let the agent write higher quality code than "plan which contains code -> approve". But maybe you can make it work when combined with some specific prompting marking the code as clearly work-in-progress and subject to change, and that the agent should surface any parts implemented differently relative to the plan to the user, etc.

---

> **writtenone** · 2026-09-24T18:27:16.000Z　
> We need LESS of AI and more HUMAN thinking. The process of thought and the increased difficulty with increased complexity is a feature not a bug.AI note taking is a scourge on society and needs to go.

---

> **factorialboy** · 2026-09-24T18:37:05.000Z　
> 736mb on macOS/facepalm

---

> **eliburnes** · 2026-09-24T18:42:22.000Z　
> Excited to try this out!

---

> **theaniketmaurya** · 2026-09-24T18:52:36.000Z　
> looks great! personally for me, system design is quite imporatn and cognitive debt is shooting up

---

> **shaundano** · 2026-09-24T18:53:10.000Z　
> Very happy to see a product like this. UML-style diagramming is still a part of my workflow when designing any architecture. Excited to try it out.

---

> **doc_ick** · 2026-09-24T18:58:39.000Z　
> If only this tool came out before I discovered the ballerina programming language (https://ballerina.io/). Otherwise I am inline with the language <-> uml like definition ballerina statically provides without llm usage.

---

> **verdverm** · 2026-09-24T19:22:12.000Z　
> Does it have a terminal and panes? These are things I do not ever see giving up

---

> **artur_makly** · 2026-09-24T19:30:43.000Z　
> Congrats! Looks tight.

---

> **igorkraw** · 2026-09-24T19:49:13.000Z　
> Looks cool :-)Linux wen plz so I can play with it?

---

> **asdev** · 2026-09-24T19:53:13.000Z　
> I think the issue with this type of product is it creates an N+1 source of truth for teams alongside their other tools. Inherently, this will get out of date as a project progresses. You could have an agent update based on changes, but that would likely degrade the design doc/artifact into unintelligible slop which wouldn't be useful in the future. This is a behavioral/structural problem of software design in general, which I don't think can be solved by software. Perhaps if this is mainly focused on collaboration at design time, but then that begs the question if teams will really want this tool versus using Notion, Linear, Google Docs.

---

> **verdverm** · 2026-09-24T20:08:41.000Z　
> I was confused for a moment by the name "Sid" in new coding tools.Sid of GitLab raised for Kilo, and GitLab is also of YChttps://capwolf.com/former-gitlab-ceo-launches-kilo-in-ai-co...

---

> **nmekala35** · 2026-09-24T20:19:07.000Z　
> Interesting idea for sure. But as a software engineer, I’m struggling to map out what this would replace today. I use Cursor pretty heavily, but it’s not entirely clear what would make me jump to a new IDE based on what you’ve built so far.Maybe I’m missing something.

---

> **shouryamaanjain** · 2026-09-24T20:24:48.000Z　
> this is really cool, claude artifacts often fails to visualize/explain system's layout and flows

---

> **metanonsense** · 2026-09-24T20:36:34.000Z　
> Yeah.. that's something that I thought about for a few years now. I think making sense of code bases and software design will soon be a completely new industry. I had expected that companies like Jetbrains would be in a prime position to offer solutions for that, but it takes longer than I expected.

---

> **itissid** · 2026-09-24T20:41:06.000Z　
> very cool. Congrats on the launch. first half of 2026 was the year when every one made such internal tools one way or another. I am happy you guys could build a product out of it.The cool thing is even though this tool addresses a few, use case for reducing cognitive load, they happen so frequently that they add up.I think they key with cognitive load is that the agents often produce a lot of trace/docs etc, in the end only a small % of the traces really are important to the final changes, because concise changes are typically very small and self contained.One thing i see this becoming important with is maintaining internal tooling built using this. I maintain an internal docs system that helps me do designing before i build code, that docs system is completely vibe coded and i can add features to it very fast, but now its all grown up. A challenge then is can i understand just enough about a new proposed change to approve it? That is key to the doc system not becoming a burden in of itself, while maintaining a tight core feature set.

---

> **8organicbits** · 2026-09-24T20:43:23.000Z　
> One concern about accuracy of the diagrams. In the example, there is a transition back to the session service labelled "wait for release" after the "no" decision. I'm not seeing that in the shown diff.Looking at the code the "no" seems to relate to the context expiring, so you wouldn't want to wait more if the context already expired, you'd want to stop. Is there a reason that label exists?I'm pretty wary of LLM development tools hallucinating and wasting my time, is that whats happening in the lease broker example?

---

> **syl5x** · 2026-09-24T20:47:46.000Z　
> Okay great timing because I was having the exact same idea, but mine was just a skill that was building a website with the flow mapped out and the relevant code, which seems that you are doing as well, definitely going to follow this, good luck guys!

---

> **woggy** · 2026-09-24T20:50:52.000Z　
> Plans for Windows version?

---

> **lfdo0870** · 2026-09-24T21:10:23.000Z　
> For that there's Python: with30 lines you can automate this task. If you want I can send you the script I use. DM me if interested.

---

> **pftburger** · 2026-09-24T21:12:36.000Z　
> Ha, nervous enthusiasm seeing this, as I’m building something similar. Guess I should put a demo somewhere public. Very cool space.

---

> **eecks** · 2026-09-24T21:16:21.000Z　
> As an architect, how do you envision me using this?

---

> **tnspacetime** · 2026-09-24T22:12:13.000Z　
> The point about semantic diff viewer sounds very interesting. I think many coding harnesses are not doing this well enough.

---

> **physicallyIllfr** · 2026-09-24T22:15:32.000Z　
> Cool open-source project. Vut why are we trying to build so many no code tools?

---

> **purple-leafy** · 2026-09-24T22:20:55.000Z　
> If you’re interested in IDEs and want to see a completely different take, look no further[0] - https://github.com/con-dog/slices-demo#slice-ide---an-experi...To me these show HN posts all build things that are a bit too obvious

---

> **icar** · 2026-09-24T22:31:27.000Z　
> You cannot currently edit files in Whiteboard. If this is something that you find yourself wanting to do, please file an issue!
>
> Do you still consider this an IDE? Curious

---

> **AM1010101** · 2026-09-24T22:43:50.000Z　
> Awesome, keen to see where this goes. Can we have light mode for the whiteboard and dark mode for the code?

---

> **gusmally** · 2026-09-24T22:59:51.000Z　
> Echoing the wish for a Windows version. This is the first piece of software I've attempted to download in my ~2 years on this site. 90% of the software engineers I know are on Windows :-)

---

> **namanbhulawat** · 2026-09-24T23:40:01.000Z　
> this is exactly what I was looking for!

---

> **whattheheckheck** · 2026-09-25T00:36:30.000Z　
> Throw in some tla+, eventb, p and modp for formal guarantees

---

> **Saltloaf** · 2026-09-25T00:44:41.000Z　
> The 'thoughtful design' angle is intriguing. Always looking for ways to capture early architectural ideas better than just diagrams.

---

> **anymoonus** · 2026-09-25T01:02:52.000Z　
> make it possible to link to and comment on github PRs - this would be a sweet reviewing tool

---

> **cjmcqueen** · 2026-09-25T01:17:45.000Z　
> "Known limitations
> You cannot currently edit files in Whiteboard. If this is something that you find yourself wanting to do, please file an issue!"Seems like a big limitation for an "IDE"

---

> **nickosh** · 2026-09-25T04:16:44.000Z　
> Thanks! The project looks great and I am definitely interested in this approach. I hope it will help me with my usual issue - I review a lot of code these days and it's really hard to understand what changes about and why they even needed usually, without deep analysis and AI sessions. It's always good to have such a visual method to check briefly what's there on architecture and design level - these mistakes are hardest to find in other people's code, as it is for me.I especially like your way to connect agents - I'm basically using what I wish to use, without limitations or pay walls. At my work, all AI tools should be reviewed and approved before usage but here I just use my coding agent and this is "plugin" for visualisation, so I guess it will be approved in no time. Thanks to not keeping a forced data collection, it will really help to promote your tool in corporate environments.No reasons to not try it for me! I am looking closely at what will come next and will try to share my feedback, if there will be some.For now, I just feel that it will be good to have a way to trigger review creation from the app itself, not to create a new agent session for this. Kinda a bit counterintuitive but I understand why it works this way and it's not a real issue.

---

> **thoman23** · 2026-09-25T04:21:12.000Z　
> Was excited to try this, but my company moved from Claude to Copilot CLI. Any plans for Copilot support?

---

> **bad_haircut72** · 2026-09-25T04:54:07.000Z　
> I use https://whiteboard-mcp.com in a similar way to this - it gives me a drawing canvas claude can access and read

---

> **nnevatie** · 2026-09-25T05:04:01.000Z　
> Is a new IDE really required for this? Wouldn't Markdown already cover a shared "canvas" for documentation/planning, when accompanied by something like Mermaid?I think some of the presented ideas are pretty cool, but am thinking that you'll get slown down by the IDE approach.

---

> **heltale** · 2026-09-25T05:37:51.000Z　
> This is a good development in terms of processing information for people.Visual memory comes the easiest to people and it’s the quickest way to understand and convey information to most people.Other forms of memory that I expect to see having better tools to address them are auditory and kinesthetic.

---

> **sidharthkmenon** · 2026-09-24T17:55:54.000Z　
> thanks, appreciate it! we also took inspiration from paper.design. the tmux bits are just for fun though :)

---

> **ketan_around** · 2026-09-24T18:04:50.000Z　
> free, oss, and local-only right now! we are working on a hosted solution but honestly aren't sure yet; we mostly made this for ourselves to fix our own gripes with agentic coding :)

---

> **bpshaver** · 2026-09-24T18:15:05.000Z　
> There are a lot of emerging tools like this for which we will need a name. A similar one I randomly came across (https://github.com/Maksim-Burtsev/merl) calls itself a "Code Navigator."Along similar lines, I also don't know what we're calling tools like T3 or Superset. They're basically harnesses for harnesses.

---

> **sidharthkmenon** · 2026-09-24T18:24:09.000Z　
> thank you! really appreciate it.1. Yeah, we've thought about this too - at the minimum, we're going to implement a vibe-codeable extension system so that you can add your own diagram types without rebuilding the app. definitely hopeful for some sort of common schema or lsp-shaped thing in the future2. this is a good point and is something we've considered and struggled with. we ultimately settled on the term 'IDE' because we've found that most people use vscode to review code nowadays, almost exclusively (so it makes it a bit easier to draw the comp in your mind). we're also strongly considering adding an editing feature, but not sure what the exact shape of it is, so decided to go in favor of not shipping it yet - editing tends towards a conductor / superset shape of product. maybe we could try "canvas" instead of "ide" or something? will mull it over more.4. Yeah, this is definitely tricky. This is why we didn't end up shipping edits as part of this release. Part of the solution here, we think, is tighter integration with the "spec" part of the lifecycle - where whiteboard makes it easier to understand if a spec (like a formal proof) is extensible, generalizable, etc. will mull on this more.5. yes that's a typo! we're fixing right now - we meant "GPT 6 Sol" (basically, fast TPS, don't need the limits of intelligence really).Edit: we do have a Fedora Linux build out if that's what you use! releasing stuff on every distro requires some care, so please let us know what you'd want to see it on (re: appimage lol)
> Edit 2: (5) is fixed! thank you

---

> **sidharthkmenon** · 2026-09-24T18:58:12.000Z　
> I did, for what it's worth, spend a painfully long amount of time designing this website, but unfortunately none of us are great frontend devs, so we lean on the models here for sure (definitely am working on getting better at frontend dev).we've put in a lot of time and attention into the app especially and hope it shows in the details - e.g. the diff viewer, the rendering animations - we want development to feel human again while still enjoying the speed boost of agents

---

> **sidharthkmenon** · 2026-09-24T18:49:18.000Z　
> thanks for the feedback! two points:1. "is this a feature" - it could be! in fact, we will expose this as an MCP UI next so that you can view the info directly in Codex Desktop or Superset/Conductor/Emdash for example. that aside, we found that the big things that matter for us are: (1) good code navigation (diagram/spec -> code), (2) beautiful diff viewing, and (3) visualizing agent traces as they connect to code. we found that these problems were hard enough, and enough folks that were using platforms that didn't easily map to these requirements - e.g. TUIs like claude code - that a dedicated product that was just focused on these problems exclusively makes sense.2. "using whiteboard for plan mode": hmm, i think our wires are crossed a bit here. how people mostly use whiteboard today is:plan -> approve -> agent codes -> use whiteboard to explain the code.(or just omit the plan phase as a formal artifact -> just emit a plan + code together, like a golang design draft [A]).we are exploring an explicit "put the plan in whiteboard first" mode (there's a scratchpad feature that's experimental right now), but it's definitely not ready for prime time yet.[A] we were heavily influenced by golang's practice of "design drafts" as a way of scaling engineering velocity, e.g.: https://go.googlesource.com/proposal/+/master/design/draft-i... (thanks to Russ Cox, the legend)

---

> **verdverm** · 2026-09-24T20:00:12.000Z　
> > a better alternative to the current Plan ModeAn easy upgrade (ime) is to be intentional about a process, move the planning artifact to a file, use multiple research/propose/review sessions to dial it in. Still tuning my vibes for when to add in some actual exploratory implementation elements, because there's always something you didn't foresee when getting to the actual implementation, while also not having them implement the solution as a "plan" in markdown

---

> **sidharthkmenon** · 2026-09-24T18:51:15.000Z　
> i am not sure to be honest if you're agreeing with us or not! but we do think that human thinking is both necessary and important in the future.wrote a blog about this if you're interested! https://dev.fast/blog/youre-still-going-to-have-a-job-in-5-y...

---

> **sidharthkmenon** · 2026-09-24T18:44:09.000Z　
> yes, totally, this is a legitimate concern and i hate this too as a dev. we made the choice to build on top of vscode for the mvp so that the code navigation experience would be normal / seamless (and hopefully, devoid of slop).as a comparison, vanilla cursor / vscode is ~1GB and zed is ~400Mb.in the future we will definitely rewrite this app as fully native and get it way, way down. in the meantime, we're working to get the size down in other ways (e.g. our diff viewer can definitely be optimized - it's 138Mb, yikes)

---

> **sidharthkmenon** · 2026-09-24T19:25:36.000Z　
> it's meant to be used as a complement to your existing terminal! your agent uses the mcp or api from the terminal to draw on the Whiteboard

---

> **thesiti92** · 2026-09-24T19:55:04.000Z　
> https://install.dev.fast/linux ! we just have a fedora build right now, but if you're looking for another distro let me know and i can put it on our roadmap.

---

> **milanb** · 2026-09-24T20:20:07.000Z　
> I think you’re on the money with the problem of maintaining (another) source of truth.Speaking from personal experience, I still find myself reaching for Whiteboard. It’s helpful when it’s critical for me as a developer to understand the implementation, which is certainly not every change!In the future, we want to deliver a hosted product that addresses the N+1 concern you raised. The problem with the existing tools is that plans don’t stay up to date with what the agent decided to implement, and the back-and-forth that happens after the initial prompt isn’t captured. We believe a single whiteboard canvas can be used to capture not only a plan at design time, but what happens after.

---

> **cannonpalms** · 2026-09-25T02:25:36.000Z　
> I see this fitting into my workflow more ephemerally. That, or I will use screenshots in some of my existing documentation so it can all rot in one place.When using an agent for development, I find that I REALLY miss being able to "see" the shape of the code in my head while I work, and I find that I get bombarded with so much information that I cannot keep track of what the code looks like. This has led to me having to get back to people async on questions they have on a call, etc., because I can't remember exactly how i made something work in the end!I will be using this to make sure I understand my own output at a depth I can remember, and I will be using it to do the same for reviewing complex PRs or diving into new parts of the codebase.

---

> **sidharthkmenon** · 2026-09-24T20:12:24.000Z　
> haha, different sid, also YC!

---

> **sidharthkmenon** · 2026-09-24T20:23:05.000Z　
> sorry, yeah the word IDE is a misnomer - we will fix, looking for something better. It's really a canvas that your agent can use to help you understand an implementation, what tradeoffs were made, etc.
>  Whiteboard is meant to be used in conjunction with tools like Cursor / an ADE.Edit: just updated the GitHub + marketing site to reflect this!

---

> **sidharthkmenon** · 2026-09-24T21:42:48.000Z　
> > end only a small % of the traces really are important to the final changes, because concise changes are typically very small and self contained.yes, totally. i think this is mostly 1 piece of the broader puzzle. we found that, esp. for complex changes where i need to spend my brainpower anyways:> A challenge then is can i understand just enough about a new proposed change to approve it?whiteboard has been a powerful tool for us! i think much more of this needs to be instrumented as part of a larger system, as you said (we are thinking the same way btw: https://dev.fast/about/)

---

> **sidharthkmenon** · 2026-09-24T20:51:46.000Z　
> Hey! oops, that gif is a notional one we were using for design, and we forgot to update it.Real diagrams are all linked to code, so hallucinations don’t really happen in practice (hallucinated architecture really bothers me too!)Will update shortly with an actual gif of the app. Sorry about that!

---

> **pftburger** · 2026-09-24T21:14:52.000Z　
> Haha yeah and I’ve been building one for myself as a side project. I think there are many people experimenting in this space. Going to be interesting to see how it develops.

---

> **ithkuil** · 2026-09-25T04:29:35.000Z　
> Nice. I didn't build a skill but I noticed that for a few complicated features that I built recently, I asked the model to build an interactive "explainer" for itSuch an explainer would contain for example a simulation of the feature, where it shows how data flows between components and allows the reviewer to tweak parameters and see how it affects things. The explainer can visually show edge cases or introduce faults.Basically my problem is that agents can write a lot. They can write a lot of code and also a lot of natural language design/spec which ultimately becomes hard to review (sloppificarion of design documents)Sometimes you can tame this by focusing on very high level, human curated specs, but since often the devil is in the details, you need a way to see these details.I found that interactive visual exploration tools are a very good way to both iterate on your problems and to share it with your colleagues.Inspirations:* https://ciechanow.ski/* https://www.3blue1brown.com/

---

> **sidharthkmenon** · 2026-09-25T00:11:11.000Z　
> yes of course! It’s on our roadmap to land soon. Feel free to email me at sid@dev.fast, and I’ll shoot you an update when it’s landed !

---

> **sidharthkmenon** · 2026-09-24T21:37:37.000Z　
> (1) right now, i think this is a better tool for the tech lead / senior engineer. they can enter a loop like:start brainstorming with their agent -> agent writes code -> agent writes Whiteboard session (connected to the underlying code) for them to iterate on.(eliminates the middle plan mode phase)(2) i don't think every piece of work fits in that way, so we're working on a "scratchpad" mode your agent can use for planning via versioned artifacts for architecture + behavioral specifications. Then it can update that plan when the implementation is complete! when this feature rolls out I think an "architect" would be using that feature more in collaboration with an engineer.(the boundary b/w architect and engineer does seem a bit fuzzy to me, esp. these days, so hopefully we share a similar mental model)

---

> **ketan_around** · 2026-09-24T22:21:20.000Z　
> not no-code at all (a big part of this project has been our semantic diffing engine)! check out the demo - in fact if anything it's meant you bring more into touch with the code, rather than less. :)

---

> **asa123** · 2026-09-24T22:44:22.000Z　
> more than anything it's valid enough as a frame of reference for what many people want to do. if they went and invented a new term for it i'd reckon a lot of people just wouldn't even click on it

---

> **sidharthkmenon** · 2026-09-24T23:00:50.000Z　
> definitely down to expand the theme set! could you file an issue for tracking ? Thanks!

---

> **sidharthkmenon** · 2026-09-24T23:07:55.000Z　
> that’s so nice! windows is definitely coming and on our roadmap soon. Will you let know when it’s ready - feel free to ping me at sid@dev.fast and will send you an email when it’s ready!!

---

> **sidharthkmenon** · 2026-09-25T02:40:57.000Z　
> haha, we're thinking the same way: https://dev.fast/about/

---

> **ketan_around** · 2026-09-25T01:17:42.000Z　
> for sure, we're thinking of doing something along those lines for our hosted product-- auto-trigger reviews upon opening PR, link to them from gh, etc. feel free to shoot me a message (ketan at dev dot fast) if you're interested in that!

---

> **altmanaltman** · 2026-09-25T01:37:06.000Z　
> Seems more like IDE is "I Don't Edit" in this case

---

> **_puk** · 2026-09-24T19:11:56.000Z　
> How does that fit the YC W26?You building something else and this scratches an itch?That aside. I actually love this. Anything that helps with the "wtf did you just do?".If I can still learn I will. If an agent can't reason about the changes made, then they are not good changes.

---

> **2001zhaozhao** · 2026-09-24T18:24:02.000Z　
> They are usually called orchestrators, sometimes Agentic Development Environments (i.e. IDE for agents) if they are complex enough

---

> **jacobgold** · 2026-09-25T04:30:56.000Z　
> I like and adopted the term "agent multiplexer" for these.Just can't warm up to "ADE" (never even liked "IDE") and "agent orchestrator" and "control plane" are just not specific enough to stick.

---

> **bbor** · 2026-09-24T19:20:53.000Z　
> I don't have much to say, other than these were interesting & helpful responses to understand what you've learned and where you're going. So thanks!I'll be honest that my initial belief it was for OSX exclusively left me feeling indignant, so knowing I was just mistaken (based on the link up top, tbf) turns me around completly. I do in fact run Fedora, so I'll be trying this ASAP!I feel Fedora+Debian+Ubuntu+Arch covers all but the long tail of devs, based on vibes alone? You might get bullied if you don't support Nix, but you'll probably be bullied by them anyway lol so no advice on navigating those waters.

---

> **_puk** · 2026-09-24T19:14:34.000Z　
> The animation carries it, don't worry.So many launches don't show what they are. This on the other hand - got it straight away from the animation.Great job

---

> **2001zhaozhao** · 2026-09-24T21:12:53.000Z　
> > how people mostly use whiteboard today is:
> plan -> approve -> agent codes -> use whiteboard to explain the code.I guess it's interesting and useful for now, but I don't think people are going to work at the code level much longer.In my opinion current coding agents + automatic review systems are already at superhuman reliability during the implementation phase (as in they will not fail something in the plan during implementation and not tell you about it, so there's no need to look at the actual code beyond maybe a cursory glance). I literally just use plan mode + CC's /code-review in each task so it's not like I'm doing anything special. So I think the main human interaction surfaces to target in the future will be in the planning process.

---

> **2001zhaozhao** · 2026-09-24T21:25:41.000Z　
> > be intentional about a process, move the planning artifact to a file, use multiple research/propose/review sessions to dial it inYeah, I think we need something like that as well. I am actually working on an virtual artifact filesystem in my orchestrator to enable this. So agents can create a persistent, versioned plan artifact separate from the codebase (maybe a HTML) and iterate it alongside the user, much like what ChatGPT/claude.ai can already do but for a coding agent. Then you'd need to define a process and get the agent to follow it, but that's much easier and mostly a mix of prompt and orchestration primitives.> exploratory implementation elementsThis is a good point, I've ran into a lot of instances as well where my agents in plan mode would like to explore something but can't because of permissions. I wonder if there should be some kind of system like a "experiment subagent" to handle it.

---

> **writtenone** · 2026-09-24T20:29:42.000Z　
> I think we need less software with AI features. Less stuff chasing the hype train and more "slow" software that encourages thoughtfulness and less reliance on the machine.I wrote some thoughts on this a while ago. They're not cleanly organized (sorry!) but it's my raw thinking on AI: https://nonograph.com/some-disorganized-thoughts-about-artif...Also wrote this on the state of VC if interested: https://nonograph.com/write-some-software-give-it-away-for-f...

---

> **verdverm** · 2026-09-24T19:29:40.000Z　
> I'm asking about terminals in the IDE, I have many of them, really multiple panes, each pane is agent(s) in terminals and the associated files/diff for their work. VS Code looks more like a dashboard for agents these days. (50" 4k)The headline says "IDE", but what you wrote here does not sound like an IDE, why would I want my agent calling an MCP / API to do the things your feature list suggests? What I'm seeing here would/could be better/replicated as a VS Code extensionI'm only interested in an "Integrated Developer Experience", winner takes all kind of thing, tool sprawl is out of hand

---

> **igorkraw** · 2026-09-24T20:10:38.000Z　
> Thanks! Sorry if I missed it. I had clicked ok the download on the page and it only pointed me at Mac.If you can create an aur it'd be awesome for the arch crowd :-)

---

> **elitistphoenix** · 2026-09-24T23:40:44.000Z　
> A .deb install for Debian and Ubuntu would be good please.
> I also know people will ask for flatpak's too.

---

> **verdverm** · 2026-09-24T20:59:04.000Z　
> > the word IDE is a misnomer ... looking for something betterYAT (Yet Another Tool) is something I use (sometimes pejoratively, sometimes as a reality), arising from the general trend and burnout in the developer tools spaceOne of the nice things about Ai is that it can deal with all that and I don't have to go through YAT docs and code to figure out how to use it

---

> **physicallyIllfr** · 2026-09-24T23:41:08.000Z　
> Ill check it out

---

> **sidharthkmenon** · 2026-09-24T23:11:17.000Z　
> yes, this is tricky and something we’ve struggled with too. We chose IDE because the closest comp is probably VSCode - lots of folks seem to just use it for code browsing / review these days!regardless, we ended up renaming “ide” -> “canvas” in on gh + website. hope that’s less confusing. will mull it over in the meantime.

---

> **anymoonus** · 2026-09-25T04:07:31.000Z　
> If you make it hosted only, my guess is you will lose out on a number of users who cannot convince their corporate overlords to authorize yet another GitHub app. Charge the user and use their local gh access to make it work!

---

> **sidharthkmenon** · 2026-09-25T02:27:41.000Z　
> yeah, ack that IDE is confusing. mentioned this elsewhere, but we ultimately settled on the term 'IDE' because we've found that most people use vscode to review code nowadays, almost exclusively (so it makes it a bit easier to draw the comp in your mind).we ended up changing "ide" -> "canvas" on the website + github, but can't edit the post above.btw, we're also strongly considering adding an editing feature, but not sure how opinionated we want to be on how agentic it should be, so decided to go in favor of not shipping it (yet)

---

> **sidharthkmenon** · 2026-09-24T18:29:53.000Z　
> hmm - those tools are great, but I don't think orchestrator / ADE is quite right either, since this is explicitly not opinionated about where your coding agent is living.Whiteboard is targeted at almost the opposite problem of the ADE (which is targeted to context switching) - having a dedicated tool to help you understand & participate in the development process in places where humans are high leverage.maybe also useful: https://x.com/ThePrimeagen/status/2101869827266596973?s=20

---

> **superjose** · 2026-09-25T04:26:21.000Z　
> Or control planes

---

> **thesiti92** · 2026-09-24T19:28:17.000Z　
> https://install.dev.fast/linux ! we added the fedora build because one of our friends swears by it! (was hoping you wouldnt say omarchy lol)

---

> **sidharthkmenon** · 2026-09-24T21:32:06.000Z　
> > So I think the main human interaction surfaces to target in the future will be in the planning process.yes, agreed. we're working on more stuff in that direction (a plan / scratchpad mode), but what i personally like the most is eliminating / shrinking the plan/review gap.i think reviewing a plan without an implementation doesn't feel that useful anymore, at least to me, because key tradeoffs often only surface during implementation that effect the top-level spec.in some sense, the code writing process is just a cheap effort which makes the spec better and more thorough?

---

> **verdverm** · 2026-09-24T21:34:13.000Z　
> > separate from the codebaseCommit it to git, it's not far off from an llm-wikiI have no orchestration primitives, just a skill tied to a .design/*.mdUnless we consider opencode sometimes using a subagent as a primitive? Maybe the problem is leaving the clankers to their own devices for too long/muchI intentionally block almost every tool for the design/review agents, letting them "do" things is a distraction. I will use the build agent and tell it what to do if I need that experiment. I don't want to have to read through the wasted tokens a bunch of dumb bots burned through to create walls of markdown. They go on way too many side quests

---

> **thesiti92** · 2026-09-24T20:32:09.000Z　
> ok i will get cranking on it, also got a request for nixOS too so im churning through them. watch the repo to get notified when the aur is released!

---

> **anymoonus** · 2026-09-25T04:08:05.000Z　
> See tuicr for a cool tui tool in this space

---

> **2001zhaozhao** · 2026-09-24T21:04:20.000Z　
> I was describing T3/Superset which help you manage context switching. Whiteboard is obviously different.

## 关联链接

- https://github.com/devdotfast/diffr
- https://github.com/devdotfast/whiteboard,
- https://github.com/devdotfast/whiteboard.We
- https://install.dev.fast[1
- https://whiteboard.dev.fast/
- https://www.geoffreylitt.com/2026/07/02/understanding-is-the...
- https://www.youtube.com/watch?v=ChPn3ftULWEFolks

## 导航

- 项目页：[[10-项目/github.com_185ddb0a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
