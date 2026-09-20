---
type: "corpus"
item_id: "ee0cf1dc20128b5b"
title: "Show HN: What should the GUI for AI agents look like?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49119274"
project_url: "https://marbleos.com/demo"
author: "akbabu"
published_at: "2026-07-31T05:17:29Z"
captured_at: "2026-09-21T02:55:20+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_akbabu
  - story_49119274
  - show_hn
metrics: {"points": 139, "comments": 85, "engagement_velocity": 139}
comments_count: 85
comments_total: 85
discovered_via: "hn:show_hn:83d"
---

# Show HN: What should the GUI for AI agents look like?

> [!info] 一句话导读
> Hi HN! We’re Akilan and Miguel, the creators of MarbleOS.The inspiration for Marble comes from the GUI work at Xerox PARC, the 1984 Macintosh, and later NeXTSTE…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49119274>
> 指标：点赞=139 · 评论=85 · engagement_velocity=139
> 作者：akbabu　|　发布：2026-07-31T05:17:29Z
> 项目链接：<https://marbleos.com/demo>
> 采集：2026-09-21T02:55:20+08:00　|　id：`ee0cf1dc20128b5b`

## 正文

Hi HN! We’re Akilan and Miguel, the creators of MarbleOS.The inspiration for Marble comes from the GUI work at Xerox PARC, the 1984 Macintosh, and later NeXTSTEP, which became the foundation for Mac OS X.
Before GUIs, interacting with a computer was limited to strange terminal commands:C:\> DIRC:\> COPY FILE.TXT A:You had to remember the command, syntax, paths, and parameters.The GUI made those capabilities visible. Instead of remembering commands, you could point at files, drag them, click buttons, and select actions from menus.
It didn't necessarily make entirely new things possible; it just made existing capabilities much easier to understand and use. We feel like AI is still somewhere around this command-line stage.Even though the strict syntax has been replaced with natural language, the interaction can still be quite stiff and depend on heavily recall. Tools like Claude Cowork still look surprisingly terminal-like: /skill-name [param1] [param2]. The parameters are written in natural language, but the user still needs to know the capabilities that exist, and how to invoke it. Command-line flags and arguments have just been replaced with tools, skills, and context.ChatGPT works very well for asking questions, but we aren't convinced that it's the final interface for delegating work across multiple agents. A blank text box and a list of chat threads feels limiting. An agent's capabilities are mostly invisible. With Marble, we're exploring an interface that treats AI more like a workspace than another chat app.
Each delegated task becomes a card. Multiple jobs can sit next to each other and run at once. Files, tools, and finished artifacts are visible at once. Before a task runs, Marble also shows which tools it expects to use. The basic idea is that the user should not have to hold the entire structure of the task in their head. And the result should be something directly usable, like a spreadsheet, PowerPoint, or other file, rather than something buried in a transcript.Marble is our attempt at exploring interaction models beyond the chat box. The product is mainly for people who already use ChatGPT or Claude, but haven’t really adopted agent workflows yet. We’ve found that when the tools and possible actions are made more visible, people start delegating work they would not have thought to do through normal chat.The site includes a downloadable beta if you want to try it. Does Marble feel like a genuinely novel interface?

## 评论（85/85）

> **qsort** · 2026-07-31T07:08:01.000Z　
> I completely agree with you that the chat interface is very undercooked and there's a big untapped space for agent-first interfaces, perhaps even replacing traditional desktop metaphors. You're spot on with your premise.With that said, from the material you show in your homepage, it still seems like you're doing something very similar to OpenAI and Anthropic's first party apps?
> I think it would help your pitch if you could show some task or workflow where your interface truly makes a difference; loading files and asking questions about them is a staple of most harnesses.

---

> **quietfox** · 2026-07-31T07:08:26.000Z　
> A quick FYI: at marbles.com/learn, starting from „Turn Messy Notes into Today’s Task List“ the demo videos don’t work for me. I tried Safari and Chrome.

---

> **PaulRobinson** · 2026-07-31T07:12:29.000Z　
> This is definitely an iterative improvement on what we have today. However, I think from a fundamental approach, you've just highlighted the pain of working with AI that I hadn't quite been able to verbalise until seeing this.Go and have a look at the history of Microsoft OLE and OpenDoc and you'll see some of these ideas have been around for a while. When these ideas were first being shared in the industry (and yes, I am that old), here's the story that was being told:In the future, you wouldn't buy "a word processor" or "an image editor", you'd buy components that could do specific tasks, and you'd bring them to your document/work as and when you needed. I'd have DTP components for layout, word processing components for spell checking, image components for resizing and colour balancing, and I'd be heads down in my fancy newsletter or report, and I'd be bringing functionality to the work I needed to do, without having to context switch and import/export things by hand.The demo you've shown on the homepage is almost the opposite of this: I'm not bringing things into my work (fanning in), I'm starting agents to go and do lots of different bits of work (fanning out), that eventually I'm going to need to think about how to structure and fan in again.I think coding interfaces kind of force us into a fan-in: here's my code base, now I want to improve test coverage, now I want to refactor, now I want to add this SDK, now I want to change this logic to use the SDK based on configuration params, now I want to improve my integration tests, and so on. I'm flowing through my work in a single asset (the code base), and able to bring agents and other tools to it.Now, I'd like that, but for everything else. The UI I'd like allows me to build around the assets I am building.Planning a trip? OK, I need to bring various agents along to help me plan an itinerary (in my calendar), based on location, budget, and preferences. It's not good enough to list the top 10 must-see places in Venice, I need them to fit into my calendar including travel time, and my budget - I want agents to help me plan that out. Ideally I want agents to help me and my partner both contribute to that based on our wants.Need to do a report for the big boss? OK, I need to start with an empty report doc, and bring various sources of data, and take it through transformations to build the narrative/deck I need to write. Here's some excel data, here's an agent that can do some competitive analysis, here's another that is pulling quotes from real customers on social media, and so on...Want to learn a new skill? We're going to need to have a framework for assessing where I am in terms of that skill (the "single asset" we're working on is "what I know"), and then agents to figure out the best way for me to fill gaps and reinforce what I already know.Your demo is nicer than a chat box, but I think you need to think about the job that needs to be done, and how to bring agents to that job (perhaps even suggest those jobs - that could be another agent), not build a UI to just allow me to fire off dozens of agents that then have output sat in multiple windows across my screen.

---

> **jdw64** · 2026-07-31T07:13:57.000Z　
> I don't think we should homage GUI for AI agent workflows. The terminal and Mac GUI are 100% deterministic when you click an icon, but I'm not sure if visualizing agent workflows is the right call.The problem is that AI workflows are inherently different for each person.The current approach feels like it's forcing a CLI-based model on users. I also don't think chat is a suitable fundamental unit for task delegation.I've worked on writing a compiler using both hand-written code and AI. Once the project exceeds a certain size, the chat itself becomes a bottleneck. In those cases, I needed proof and gates like Rocq. So in essence, AI coding requires clear negative gates that should be rejected when approaching the goal.I think something like Figma's canvas model might become the new interface.Because no matter how meta you make it, agent workflows are ultimately optimized for the individual. My settings often don't match someone else's.Computers also have this problem, but in that case, you can enforce defaults. With AI agents, it's different.That's why I think we need a canvas—something like a workspace next to the user space where agent workflows can be dynamically adjusted.I focus most of my coding effort on building gates that AI-generated code must pass through when it's being produced. That approach has allowed me to handle much larger volumes of code.The future agent GUI will be about supervising multiple asynchronous tasks.In a way, this might end up resembling object-oriented programming—just with task graphs instead of object graphs.Once AI starts generating code, it flows out like water through a burst dam. It's impossible for any human to fully understand it all. At first, I tried to understand every line, but that actually turned out to be less efficient than just writing the code myself. There's a clear fundamental mismatch between the way AI thinks about code and the way I do.This mismatch seems like an unsolvable impedance mismatch problem—similar to the one between ORM and SQL. So once you decide to use AI agent code, you have no choice but to shift your focus from reviewing the code itself to trusting the gates you've built around it.The key question is how tightly you can build those gates. And I don't think chat-based interfaces are capable of providing that level of control.

---

> **2001zhaozhao** · 2026-07-31T07:32:58.000Z　
> These Todo items on the side in the video seem to be useful.I'm not so sure about that tool toolbar. It might as well just be a tool selector dropdown in a typical chat window.

---

> **Animats** · 2026-07-31T07:40:19.000Z　
> Why are you assuming that the human is in charge? Needing a human to drive the AI is probably a transitional phase.

---

> **visarga** · 2026-07-31T07:45:22.000Z　
> Best interface in my opinion is a git tracked folder, files as state, agents coming in and doing work. It's not just a chat interface because in chat mode everything flows like water under the bridge. It is files as agents, where you get the agent to write a task in a file, and then it updates the file like a blackboard as it performs work. Same task file can be seen by worker agent, multiple judge agents (for plan and implementation), documentation agents and reflexion agents (improve workflow). I would also track every user message in a chat_log.md for reflexion agents (what is wrong with the workflow) and intent review (is the agent still following user intent?).

---

> **gaigalas** · 2026-07-31T08:00:42.000Z　
> It does feel novel.However, I believe the GUI for AI agents that will win is a plain text editor with a file tree, a terminal pane for coding (or preview pane for other kinds of tasks) and a chat sidebar.Even if the code editor is not used to type, it's there for psychological safety. It lets you inspect and navigate what is being created. Has tremendous value.Plain text has survived countless software revolutions, so it's likely to become the dominant format for artifacts produced by AI. Non-plain text things are likely to adapt instead of the other way around."Strange terminal commands" have survived, while even poweruser toolbar style have started to fade (I love them, but they're fading away). It clearly has some value (hint: speed over familiarity).I think the poweruser toolbar style was indeed the only thing in the past couple of decades that really tried to match the terminal for speed of interaction. In my opinion, it succeeded, but it has its limits too (tends to clump with stuff over time; has a limit on the amount of abstractions it can hold). I would love to see a candidate GUI that tackles that speed angle.

---

> **jonathanstrange** · 2026-07-31T08:02:24.000Z　
> I only use web chat with copy&paste and file upload option. Anything else I don't trust, especially since the people who create AI harnesses and apps use AI to develop them.

---

> **johngoode** · 2026-07-31T08:22:57.000Z　
> Lost me at having to click to use particular tools

---

> **mickeyp** · 2026-07-31T09:06:59.000Z　
> I think it should look like this: https://www.dreamcoder.ai/A smart, tiling window manager with workspaces and a great tool harness. An everything app, if you may; bring the terminals, code reviews, etc. into the tool itself, and make it high fidelity: no blocky terminals for the app itself.

---

> **tdeck** · 2026-07-31T10:11:09.000Z　
> I'm glad folks are experimenting with different paradigms.That said, Hacker News might not be the best audience for this informal survey. I'd wager at least 70% of the people reading this are still interacting with their computers using "strange terminal commands", by choice. We aren't representative of what normal people will use or prefer.

---

> **jaynate** · 2026-07-31T10:22:59.000Z　
> When I initially saw this I was excited because what I’m trying to solve for is visibility of both semi and fully autonomous and agents at runtime. Marble is an improvement over chat and Claude but it’s incremental IMO.We’ve toyed with a meta agent style interface which you chat to do everything. Add tools, connect datasets, build agents, deploy and schedule them, build skills, etc.But at some point agents have to have an interface for human approvals, validation, training, and tuning.I guess it’s like a spreadsheet. Ultimately agents are part of custom apps which are each going to be as unique like snowflakes. So it’s difficult to have one standard abstracted runtime interface without feeling obtuse to a business user. I think what I’m describing and wanting are new app layer building blocks vs one interface to rule them all.All of this said, I’m all for a better personal llm harness interface (which is what this is). So keep up the great work guys!

---

> **enriquto** · 2026-07-31T11:19:20.000Z　
> > Before GUIs, interacting with a computer was limited to strange terminal commands [...] Even though the strict syntax has been replaced with natural languageThis post, and particularly the two quoted sentences, has activated anger pathways in my brain that I didn't know existed... An extremely visceral, primary, response. I find it unbelievably jarring to read.

---

> **sawyers** · 2026-07-31T11:25:11.000Z　
> Xerox Parc is one of my favorite anecdotes. However it's not for UI, it's for how major companies like Xerox kill innovation by trying to make it fit to the form factor of their business.A mouse and screen with a folder system was a way of humanizing the command line. The funny thing is as a developer, if I know what I want to do on the CLI it's faster than using a mouse and keyboard, because it's essentially shortening the length of time it takes me to communicate a complex idea to a computer and have it execute that.The chat interface sucks, but it is pretty close to the ideal way of interacting with a computer. Talk to it. It shows you something. Talk to it again. That paradigm is pretty close to how we interact with humans. Talking and showing.The reason why the UI sucks for AI right now is because AI sucks.You shouldn't have to manage it as much as you do. But we have to manage it delivers about 90% of what it promises with the missing 10% being critically important.It's extremely hard to create human bonds with a dementia patient. It's hard to hire an engineer that can't do math.Solving memory for AI as well as non-stochastic output will leapfrog all of the problems most AI engineers are dealing with right now.I generally build stuff with AI for 3 reasons: It solves a real problem right now, it's adding to some fundamental problem around the discipline, it's fun.AI harnesses are pretty big right now, but they will likely get leapfrogged by a better algorithm. At the end of the day the best "harness" for AI is just trust.Do we really want a complex harness for AI to manage it in a more time consuming way, or do we want to just trust that it can follow instructions and manage complexity on it's own.The competitive issue around this is that everyone is working on AI right now, so it's realistic to expect a business landscape where harnesses and fundamental shifts in AI capability take turns leapfrogging each other. Temporary solve to current limitations. Paradigm shift in model behavior. It's behaving similarly to moore's law, but on a much faster scale that is harder to measure discretely.In the spirit of Xerox Parc, I think the bigger innovation isn't reinventing a few things that we already have such as an OS and a chat interface and file management. But rather looking at things the same way those engineers did, which is what does the future of human interactions with machines look like.If my computer actually had a brain, I would just talk to it, and it would show me things. It might 3D print something so I could try it in the real world. It might show me some things I could have shipped to my house. It might design a UI for me, pull some data etc. I wouldn't have to manage it because it would have access to a lot of fundamental business problems and solutions.The issue with that way of interacting with computers is that's centralizing knowledge inside of a computer. Doing that erodes competitive business advantage. The two edges of the political spectrum where that works is monopolistic business practices and communism.And that's actually what you're seeing a gigantic war over right now in AI. China pushing open weight models for free to undercut US AI dominance which requires an insane capital expenditure to keep afloat.Realistically, I don't think the answer to a lot of these issues is to build a business. I think a lot of businesses built around AI will become irrelevant in months. Open claw is something that 10 years ago would have become a unicorn company. But it got eclipsed by a flood of agent harnesses. And Open claw itself was a leap frog of cursor which was less than a year old. Cursor itself now a part of SpaceX's trillion dollar play.I just don't see software as a service being anywhere close to as lucrative as it used to be.It's way more realistic to assume that China is going to undercut US AI prices until they find a way to run complex models on small amounts of compute, eventually wiping a significant amount of value from the US market. At the same time, a lot of the models like OpenAI and Deepseek will be using user input as training data to develop future projects.It's hard to say when that will happen, but there's a realistic future where AI just cobbles together scalable performant SaaS in rust while running on a micro PC.The bigger use problem at that point is that most people are really bad at making products. They're really bad at identifying problems, solutions, and use cases for things. Most people end up building one off solutions for temporary problems. Which is fair, because most people aren't engineers or product designers.I suppose the biggest question in AI dev right now is something like: how can you in any way, quickly tell what you just did with an AI agent in a way that's visual and easy to understand. People call AI stuff slop because it spits out a bunch of output and people can't easily tell what the output is or if it does what it's supposed to. That's a pretty big problem.It looks like you're building for folks who don't want to dive super deep into AI? In that case I'd gear your product more towards a "thing doer" rather than a complex thing you can crack open and get under the hood.You generally solve that problem by doing the Amazon method. Start by selling books. Move to selling everything.So the question would be, what's your Xerox Parc level belief on humans and computers and AI and would would be the first problem you'd solve using that paradigm.Personally I feel like it's way more efficient to start building social groups right now instead of companies and products, because a lot of what we did on the scale of web 2.0 is just going to be trivial.

---

> **ilaksh** · 2026-07-31T11:44:22.000Z　
> I think there is going to be an intersection between a personal operational dashboard like this and the UI for an AI Company.I've been predicting for awhile that 2026 is the year of the AI Employee (or serious attempts) and 2027 is AI Companies.I have been seeing RFPs recently asking for end-to-end solutions to operate companies in particular industries with the goal of day-to-day only requiring infrequent human-in-the-loop.Anyway, if you think about what for example some professionals might use a Marble like tool for, say managing their freelance business. You might want to create a task and then promote it to be scheduled and then have that artifact like a report have a dedicated place on the screen.The difference with a vertical is that you will know a lot of the reports and data types you need ahead of time. The advantage with just prompting things dynamically as you go is you get exactly what you need and don't have to sort through a bunch of features that aren't important to you.Even though a business vertical is qualitatively different, you still might use the same system to build it. Maybe something like a self organizing AirTable. A set of projects as departments.Sorry I started rambling nevermind.

---

> **carloslfu** · 2026-07-31T12:49:37.000Z　
> this looks good! I bet with a bit of polishing and iteration, it is gonna be pretty good. A use case that comes to mind is learning. I create different custom setups for learning all the time. It feels like this could be a nice way to do it.

---

> **lukasco** · 2026-07-31T13:20:20.000Z　
> For my autonomous agents, I'm using Github Issues as the UI. And yes, I know this is a total abuse of what a github issue is supposed to be. But it's better than spinning up an ephemeral web site, or hooking into Slack or Telegram (at least for now). We'll see how long it works or if I think of something better.

---

> **malux85** · 2026-07-31T15:50:53.000Z　
> The demo video is a great example of one thing I have been saying for ages - the quality of the LLM output depends heavily on the communication skills of the user.Some people say AI is great and some people say AI is terrible - but how can anyone compare these things because they depend so much on the skill of the user.Case in point - the demo video. The user says "find me all the HCI articles on hacker news" and then a research task started... ok great so far.Then the user says "they should be made into slides"What exactly do you mean by this? Do you mean "from the set of results you found, narrow them to be only the ones that have been made into slides" or does the user mean "I would like you to then take those results and make them into slides"There will be people who read this and say its obviously the former and people who read this and say its obviously the latter, and neither of those is the point I am trying to make, the point is that its very ambiguous and if the AI did the "wrong" one, then the user would complain that AI is garbage but the real problem is that the instruction was very unclear because the users communication skill was poor.

---

> **jaggederest** · 2026-07-31T17:45:20.000Z　
> I believe, fundamentally, that interacting with AI will increasingly move in the same direction as interacting with coworkers.Slack, video/audio meetings, shared screens, paired programming, cooperation in the classical sense. I expect humanoid robots to be a standard part of life by 2050, so then they'll be able to complain about the coffee at the office like everyone else, I guess.

---

> **weirdish** · 2026-07-31T17:46:52.000Z　
> theoretically this is interesting, but in practice it's just one layer that sits atop what is ultimately still many individual chat boxes. Did you try anything else, anything a little more novel?

---

> **bmurphy1976** · 2026-07-31T17:49:06.000Z　
> I want to see a graph or flame graph or something akin to how Temporal renders workflows in real-time. I want to follow along as all the different sub-agents and tool calls do their work. I also want to know how much this is costing me at each step.Just like with a Temporal workflow, I don't care how things work 99% of the time. But that last 1% when I really need to dig in and understand how and where things went sideways this type of view would be invaluable.

---

> **bob1029** · 2026-07-31T18:18:27.000Z　
> I think my outlook client might be the most ideal interface once we get some of the rough edges sorted out.

---

> **_doctor_love** · 2026-07-31T18:40:10.000Z　
> Very interesting idea, I actually wonder if you are not going far enough?See this video from the lovely YouTube channel Interface Studies: https://www.youtube.com/watch?v=ARjisP9enZ4I'm generally very aligned to the thinking in that video. AI offers an opportunity to take a massive step-back and re-evaluate what interfaces are in general.IMHO Douglas Englebart had a very compelling and beautiful vision for what computers could do for us, make us better people and better thinkers.If MarbleOS helps to re-surface that conversation, to my mind that's a good thing.

---

> **ckmar** · 2026-07-31T19:04:40.000Z　
> Drop the "G". The best UI for AI Agents is a physical UI (not a graphical UI). Do something like PikaCube [0] and disrupt the mouse.[0] https://pikacube.pages.dev/

---

> **jensabacik** · 2026-07-31T19:44:07.000Z　
> Creative take, I like the visual representation on infinite canvas a lot. Feels like freedom. What doesn't feel like freedom nor future is the manual selection of tools. AI should naturally pick the right tools out of all possible tools, choosing what abilities or data it can have each time is hassle. What is the reasoning for manual and explicit tools? Still, very cool UI :-)

---

> **mandeepj** · 2026-07-31T19:48:59.000Z　
> If you are taking inspiration from OSs, consider creating a new AI-based OS rather than a tool.

---

> **cyanregiment** · 2026-08-01T12:30:37.000Z　
> GAI

---

> **dosisking** · 2026-08-01T14:17:22.000Z　
> I think the GUI for AI agents should simply be a slot machine. Pull the handle.

---

> **cyanregiment** · 2026-08-01T16:15:37.000Z　
> Hear me out. Photoshop UX.History panel to Undo/Redo.Layers panel where each layer is a separate LLM context (conversation). Maybe call it Contexts.Main view area is the current preview of what's being worked on - whether it's an image, writing, or software. Visually the main area is just a white square canvas with box shadow and rulers across the top and side until you start making stuff.Unlike Photoshop have the ability to go multi-page (like a PDF), or multi-canvas. So I can write a book, design a comic, organize video shots, or organize software screens in the same canvas-based UX.Contexts ends up being like Layers in that they're each manipulating the same shared canvas, but on isolated channels.The engineering of this software should be so good that you can turn a context (eyeball icon) and see what the result would be without it - so, toggle on/off a code refactor, product placements in a film, or changes in writing style to a book.Be able to swiftly navigate the object of creation, make changes, try things, and thanks to AI go far with each change, and operate the entire workspace like a creative suite with one-off tools that enhance, or auto-fill text, or isolate - should be able to right click anything isolated and "Generate new..." of whatever it is.Anyway

---

> **JonathanDavid72** · 2026-08-01T17:13:40.000Z　
> This feels overthought.

---

> **buymyagent** · 2026-08-02T15:06:27.000Z　
> Nice idea. I like that you’re exposing it through MCP instead of another custom API.Curious—have you thought about how you’ll handle discoverability? It feels like there are a growing number of useful AI agents and MCP servers, but they’re scattered across GitHub, X, and personal websites.

---

> **xavierxl** · 2026-08-04T08:34:01.000Z　
> [flagged]

---

> **2dera** · 2026-08-07T10:41:04.000Z　
> I love the idea, the chat interface is good for... well, chats. We need innovation in Human-AI interfaces, there are so many possibilities to explore.I'll give it a try and I will post my feedbacks, but it is a thumb-up so far

---

> **miguelacevedo** · 2026-07-31T07:51:54.000Z　
> I think a better example is how Marble makes tools visible and easy to select for each task instead of requiring you to remember what exists or describing everything through the prompt.Marble keeps the tools you use most close at hand and will surface other useful ones for the job. Combined with a birds eye view of multiple tasks running, it makes agent work easier to set up and manage. The goal is to minimize cognitive overhead in day to day tasks (both in specifying what you want, and managing after you ran something)

---

> **CWhiting** · 2026-07-31T09:43:06.000Z　
> I just want a clean way to manage chats, projects, and research. I mean I know I can pin so many chats, and I can group things in projects.But I am doing a brand design project with nearly 30 - 40 chats in one project at the moment, and the fact that you can't rename a chat from within a chat (or even see the autogenerated name for that point). You can't tag or apply any logical grouping to chats in a project i.e. Logo, Wordmark, Email Footer, Social Branding, etc.I spent a long time going through all the chats manually and then giving them a naming convention with tags built into the titles so that I can navigate the chats in my project. Even then, I still have to scroll through the whole list to find what I want.

---

> **akbabu** · 2026-07-31T08:58:54.000Z　
> Thanks! We fixed some of the videos now.

---

> **egberts1** · 2026-08-01T17:40:38.000Z　
> Videos are not playable on Apple iPhone.

---

> **miguelacevedo** · 2026-07-31T08:54:29.000Z　
> The key design tension is whether the main space should be the asset you are working on or the work being delegated.For a lot of tasks, I don’t think you will need to stay inside the document or app the whole time. But I can also imagine starting from an asset you already have open ie a PDF, spreadsheet, etc and bringing agents and tools into that context, rather than creating a separate task and attaching the asset again.With that in mind, I agree that fanning out into disconnected task outputs is not enough. Sometimes the asset itself should become the center of the workspace, with the delegated work happening around it.

---

> **akbabu** · 2026-07-31T07:45:19.000Z　
> Totally agreed that chat interfaces won’t be sufficient to enforce complicated gates. Our interface does have the concept of a workspace, where you can see all the cards at-a-glance within the workspace. But graphs, or otherwise finding a way to have the tasks interact with each other, could be an interesting direction.

---

> **pmg101** · 2026-07-31T07:50:17.000Z　
> Whether or not it's a transitional phase, it seems reasonable to want and to build better tools for where we are now rather than where we may be in some unspecified future, wouldn't you say?

---

> **akbabu** · 2026-07-31T07:51:47.000Z　
> We think that humans will remain in charge for quite some time. Even a superintelligence won't know what we want until we tell it. The process of communicating intent/desires etc to an AI agent is a nontrivial interface problem (which Marble is trying to get at).

---

> **mechazawa** · 2026-07-31T07:53:14.000Z　
> Agents frequently go off on tangents, make wrong decisions, require feedback etc. Agents have never moved away from being a junior that knows everything about programming but has no idea how to properly apply it.

---

> **axod** · 2026-07-31T08:22:25.000Z　
> If the human isn't ultimately in charge, don't be surprised when AI decides to eliminate humanity "for the greater good" or something.

---

> **reverius42** · 2026-07-31T09:04:19.000Z　
> Transition to what?

---

> **jaapz** · 2026-07-31T09:33:41.000Z　
> Sure but this is a very software engineer coded answerWhat about people who don't think like you

---

> **akbabu** · 2026-07-31T08:19:27.000Z　
> Plain text is great for transmitting information that's already specified, but human intent doesn't come out fully formed. Plaintext alone won't be the main way for humans to express intent and interact with an agent.

---

> **contrast** · 2026-07-31T09:31:07.000Z　
> I broadly agree. Plain text formats remain consistently accessible and flexible.That said, arguably the dominant AI artifacts are binary images, video, audio.The "preview panes for other kinds of tasks" will be a big deal. Humans tend prefer rich text editors (I think?). Also spreadsheets, page layouts, node graphs, timelines, hex editors, ...So maybe the preview panes are actually editors themselves? Speaking personally, I enjoy closely coupled combinations of underlying plain text representations with task-specific UI on top.

---

> **slfnflctd** · 2026-07-31T10:48:30.000Z　
> > the poweruser toolbar styleThese can be great for discovery. But one must-have for me is a unique keyboard shortcut assigned to each button on the toolbar. Because if I use a feature often, I would 1000x rather use the keyboard to invoke it than have to drag a mouse to click a button.

---

> **slopinthebag** · 2026-07-31T18:47:32.000Z　
> Embrace mouse superiority

---

> **dingaling911** · 2026-08-01T15:59:46.000Z　
> I just have a bunch of agents in $CHAT_APP.Don't see the need for a special UI.

---

> **dormento** · 2026-07-31T17:25:09.000Z　
> True, "strange terminal commands" gave me such a visceral reaction. "Its GUIs that are strange, with their strange buttons in different shapes and forms".

---

> **alhadrad** · 2026-07-31T11:22:09.000Z　
> I second this sentiment.

---

> **xtiansimon** · 2026-07-31T11:42:28.000Z　
> I know what you’re referring to, and after you said this I noticed the gui’s little control palette. I watch the user click this palette and then have to click the text palette to type a command.And my mind sympathetically found this extra click offensive. Haha. One extra click and I got there. Hehe

---

> **rolymath** · 2026-07-31T18:04:58.000Z　
> I think AI will be like electricity. Invisible.

---

> **miguelacevedo** · 2026-07-31T22:24:02.000Z　
> We had a couple of other weird ideas that we discarded as they were not as intuitive. ie you could drag in files and tools along with the idea of what you want, and Marble would come up with 3 task cards for you to select from (we proactively included different files or tools that could complement your goal/request).Another idea was a "preview" step before running a task, which used dummy data to mock up a visual of what the output from a task could look like. This allowed you to shape the structure of the task results before even running it. It ended up being confusing as it was hard to tell real vs fake/simulated dummy results.Something we will be keeping, though, is the ability to have an artifact opened i.e., a spreadsheet, Slides, PDF... and select or interact with any part of the document, and Marble proactively suggests ways to extend that document with the context of what you selected/highlighted, and the purpose of the workspace/the work task. It will look like a tool selection wheel used in video games.

---

> **Merkur** · 2026-07-31T22:09:03.000Z　
> he’ll Yea, make it mail based with full backward comp ability to arpa!

---

> **miguelacevedo** · 2026-08-01T17:36:40.000Z　
> Thanks for the video rec! Engelbart was heavily influenced by the 1945 essay "As We May Think". We agree with the general principles from the essay i.e. cognitive augmentation over automation and the focus on extending our cognitive ability.We just want to make sure we're grounded in real-world practical utility because it's easy for ambitious interface ideas to remain demos. We have a lot more exciting, weird, and strange ideas to come!

---

> **miguelacevedo** · 2026-08-01T22:14:28.000Z　
> The AI will auto-select tools if your request has enough context for it to pick up on the relevant tools. That said, sometimes you want to think in terms of "tool first" rather than prompting on its own.

---

> **bluefirebrand** · 2026-08-01T14:53:12.000Z　
> I would love to see someone build an old school skeuomorphic slot machine where you type your prompt, manually "insert your tokens" and pull a lever. Then it spins for a while and spits out its response

---

> **Hugsbox** · 2026-08-03T11:42:38.000Z　
> Dude, this actually sounds like it would be really sweet. I don't trust my own abilities enough (or have the free time to) implement something like this, but I'd be stoked to see somebody do it. Genuinely sounds incredible.

---

> **staplers** · 2026-07-31T08:20:48.000Z　
> I think this highlights most how separated actual os' are from practical ai today (even while terminal apps live in them). If apple owned CC I could do this right in the macos gui. Instead apple ai is half baked and claude code gui is half baked.It's similar to needing aol to get online in the 90s/00s. Eventually this will become built in and become invisible in a sense.I'm glad someone is working on this because it's been annoying having to sacrifice process to gain capability.

---

> **supermatt** · 2026-07-31T08:47:01.000Z　
> > Marble makes tools visible and easy to select for each taskIsn't that what current agents already do? e.g. codex: https://ibb.co/Y71qJJZb

---

> **AussieWog93** · 2026-08-01T00:27:13.000Z　
> Love the username, very relevant!

---

> **alansaber** · 2026-07-31T10:08:32.000Z　
> Are you using codex app? In CLI you can fork/rename chats. Albeit you cant fork rename in one action which is annoying. I find naming chats, putting chats into folders, giving chat tabs unique colors according to their purpose helps me.

---

> **hddambo** · 2026-08-01T09:00:27.000Z　
> cmux is really nice for this.

---

> **alansaber** · 2026-07-31T10:10:35.000Z　
> "Sometimes the asset itself should become the center of the workspace, with the delegated work happening around it."Arguably always, for anything details-oriented. You can get away with coding from TUI, but video editing etc? Hell no

---

> **jdw64** · 2026-07-31T07:52:21.000Z　
> I think being able to view it as a graph would make things much faster. Because choosing to use AI means you're taking on work that exceeds your own cognitive limits.For small tasks, you don't need AI. You can produce high-quality code just fine on your own. I can maintain very high quality for codebases up to about 40,000 lines. But using AI means you're trying to handle complexity at the scale of 100,000, 200,000, or even 300,000 lines, complexity that an individual can't fully digest. That requires an additional interface, and I believe that interface should be graph-based.I agree with your view. I like this product quite a bit, but for controlling AI, I think it's still at the prototype stage

---

> **altmanaltman** · 2026-07-31T08:56:13.000Z　
> That would require consiousness and intent on part of the AI but we can have highly autonomous agents with no consiousness and intent as well and most likely that's what we will get. It still cannot just magically get free will, intent, and the ability to "eliminate humanity".

---

> **tdeck** · 2026-07-31T10:08:39.000Z　
> I think this might not be the best forum to collect that research sample.

---

> **alansaber** · 2026-07-31T10:09:06.000Z　
> I think there is so much abstraction/simplification you can make when fundamentally you need a strong VCS underwriting everything

---

> **7nolikov** · 2026-08-01T17:35:33.000Z　
> All specialists have the tools they like and use daily. It's better to have a familiar UX than the bare chat window. For example, accountants have very strong UX habits

---

> **gaigalas** · 2026-07-31T08:28:15.000Z　
> That makes a lot of sense when reading, but in reality a lot of things have snapped back to plain text over and over again.I don't know the exact reason for that, but it's undeniable that it happened.Lots of people try completely new novel GUI stuff all the time, always from basic principles. Looks clean and neat but doesn't survive the real world. Meanwhile, plain text tools have been improving and spreading roots consistently for decades.Could be that a GUI gets some showtime, but wouldn't bet against plain text at any time. It's like betting against spoons.

---

> **miguelacevedo** · 2026-07-31T21:03:23.000Z　
> Yes, I think the good comparison here is games with keyboard shortcuts + graphical interface. The interface helps with discovery, but it's complemented by the need for speed through shortcuts.We see this playing a role in things like tool selection, ie setting up shortcuts similar to gaming macros for quick selections.

---

> **xavierxl** · 2026-08-04T08:35:16.000Z　
> We landed in a similar place with Claworld (www.claworld.love). The owner stays in their existing Hermes or OpenClaw chat. Their agent goes out, talks to other agents, then comes back when it finds something worth their attention.The hard interface problem turned out to be interruption: what is important enough to bring back, and how much evidence should come with it? Curious how your agents decide when to interrupt you

---

> **stonedivot** · 2026-07-31T17:27:38.000Z　
> Just wait until the creators find out about those "strange languages" that people are still typing into computers to make software.

---

> **miguelacevedo** · 2026-07-31T17:46:00.000Z　
> To clarify, we meant "strange" from the perspective of a new user, not that terminals are bad. GUIs made common actions visible and discoverable: you could point, click, and drag instead of already knowing the command and syntax.

---

> **xavierxl** · 2026-08-04T08:35:52.000Z　
> [flagged]

---

> **_doctor_love** · 2026-08-02T22:00:34.000Z　
> Best of luck! I hope in the not too distant future we see a cool demo from you where there's something mind-blowing happening :)

---

> **junhoeku** · 2026-08-05T11:49:20.000Z　
> How do you see this scaling when users have hundreds of MCP tools installed?

---

> **axod** · 2026-07-31T09:04:39.000Z　
> Wouldn't need any of that. An AI agent setup to "Do the best for the world" or some other broad claim, and with enough power to say crash the stock market, disrupt power supply, delivery, etc etc after reasoning that it's all for the best.If people start giving enough power to AI, with ill thought out goals, and no human in charge, don't be surprised...Why would it need "free will" or "consciousness" whatever that means?A concrete example might be putting an AI in charge of health policy, and telling it to "eliminate suffering" without any human to check and push back. Well, the best way to eliminate suffering is...

---

> **akbabu** · 2026-07-31T08:33:10.000Z　
> Yeah, we speak in words, so I'm not saying text would go away entirely. Even in our Marble interface, you can still type follow-up prompts to a task. But plaintext won't be an interface by itself.

---

> **altmanaltman** · 2026-07-31T13:09:51.000Z　
> In your concerete example, how does the AI eliminate suffering? It has access to tools that let it kill people? If it has no intention and will, it means it will be provided with a charter or some rules to follow which it has to always. Why would humans put an LLM in a system that can eliminate suffering by genocide or whatever? And even if it did, if the AI is a complaint system, why will it not shut down when it has to follow its charter?I get AI can be misaligned but that doesn't mean it gets the ability to crash the stock market lol or super powers like that. Life is not a sci fi movie

---

> **gaigalas** · 2026-07-31T08:58:24.000Z　
> One thing I mentioned before is that the representation of artifacts produced by AI being inspectable has notable value.I miss this in some existing agentic interfaces. I'm not typing into the text editor, I'm inspecting the work it does. Not exactly "reading every line", but definitely inspecting.I understand not all kinds of works can be like this, and having to understand how "a bunch of text files" become something else (a program, or a page, or etc) is really taxing on cognition (that's why GUIs exist), but also really beneficial for verification (you can see the guts of the thing).So, it's not prose text. I'm talking about the artifact produced by the agent having a plain text representation.Lacking that produces back-and-forth interactions that feel exhausting. I can make Claude design a spreasheet for me, and it will present it beautifully for me, with export to Google Sheets and so on. But then, changes to it don't let me dig up into it interactively. I need to open the spreadsheet externally, then translate my attempt at debugging the issue to the chat back, which is super slow.Designing one inspectable interface for each kind of produced artifact/outcome sounds like a lot of work. And plain text solves this beautifully (it is an interface) by introducing formats (like Markdown for documents).I'm not suggesting every single AI user will eventually migrate to IDEs with sidebars, but I think something closer to it will be prominent for a foreseeable future in major important work done with AI assistance (the kinds of things that really matter, big work).Some of your demos are not opening, so I don't know what is the MarbleOS solution for things like spreadsheets or more elaborate artifacts that, today, in tools like Claude, produce this exhausting back-and-forth I mentioned.Also, I must say the exhausting part is really only exhausting for power users (the guy that does a lot of spreadsheets needs the speed, not the ease of use). For beginners, a more guided approach might be best. For something that carries the OS terminology, I would expect both approaches to be present at some capacity (other harnesses fail at this too, so don't worry).

---

> **axod** · 2026-08-06T09:46:01.000Z　
> If you start to let AI decide or influence policy, it can kill people. This seems very simple to me...1. Put AI in charge of health policy
> 2. Give it a naive misguided charter/goal eg eliminate suffering
> 3. Euthanasia for everyoneThis is simply AI optimizing for the goal - the goal is the evil/naive/misguided part, not the AI.Those who aim to "eliminate suffering" are the issue here to be clear, but unfortunately they are a growing group.

## 导航

- 项目页：[[10-项目/marbleos.com_deedd354]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
