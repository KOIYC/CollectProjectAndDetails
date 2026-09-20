---
type: "corpus"
item_id: "4f5cee53bbcc4ac3"
title: "Show Me the Article You're Most Proud Of And I'll Read Every Single One of Them"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/georgekobaidze/show-me-the-article-youre-most-proud-of-and-ill-read-every-single-one-of-them-1l53"
project_url: "https://github.com/georgekobaidze"
author: "Giorgi Kobaidze"
published_at: "2026-09-10T19:30:37Z"
captured_at: "2026-09-20T14:17:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-10"
tags:
  - 语料
  - devto
  - community
  - discuss
  - showdev
  - writing
metrics: {"reactions": 115, "comments": 184, "reading_time": 2}
comments_count: 184
comments_total: 184
discovered_via: "devto:showdev"
---

# Show Me the Article You're Most Proud Of And I'll Read Every Single One of Them

> [!info] 一句话导读
> I Write More Than I Read

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/georgekobaidze/show-me-the-article-youre-most-proud-of-and-ill-read-every-single-one-of-them-1l53>
> 指标：reactions=115 · 评论=184 · reading_time=2
> 作者：Giorgi Kobaidze　|　发布：2026-09-10T19:30:37Z
> 项目链接：<https://github.com/georgekobaidze>
> 采集：2026-09-20T14:17:39+08:00　|　id：`4f5cee53bbcc4ac3`

## 正文

## I Write More Than I Read

I used to read a lot on DEV. Then I started writing my own articles, and somewhere along the way I stopped reading nearly as much as I used to.

I want to fix that. There are so many good writers on here that it's genuinely overwhelming, and I'd rather be reading them than not.

## The Rules

Doesn't matter if you're a veteran tech writer or you published your first post last week.

👉 Pick one article you're most proud of. **Just one.** It doesn't have to be the community favorite or the one with the most reactions, pick the one you love the most.
👉 Drop the link in the comments.
👉 Optional: tell me why it's special to you. One paragraph is plenty.

I'll read it and give you my honest feedback. I promise! 🤝

## Why Bother

Maybe your favorite post never got the attention you thought it deserved. Maybe it got plenty, and you'd just like an excuse to share it again.

Either way, it's sitting in your archive and nobody's read it in months. This is a chance to put it back in front of people.

And it works both ways, read what other people drop in the comments. That's the whole point.

Showcase your work, appreciate everyone else's.

**Let's build a hall of fame of DEV's best work! 🌟**

---

**Let's stay connected!**

I share more software engineering insights, projects, and experiments across these platforms:

- 💼 [Connect with me on LinkedIn](https://www.linkedin.com/in/giorgikobaidze/)
- 💻 [Explore my projects on GitHub](https://github.com/georgekobaidze)
- 💬 [Follow me on X](https://x.com/georgekobaidze)
- 🎥 [Watch my videos on YouTube](https://www.youtube.com/@Pilotronica)

## 评论（184/184）

> **Giorgi Kobaidze** · 2026-09-10T19:31:50Z　
> I'll go first. I wrote this for the GitHub Copilot CLI challenge, and it's still my biggest win. I built Metal Birds Watch, and it made me dig deeper than any project before it, not just the code, but the maths and the geographic coordinate work behind it. It was an enormous amount of effort, and I was in bad shape for most of it. I'm still not sure how I got it finished. Which is probably why I'm so attached to it.
>
>  Metal Birds Watch: Copilot CLI Helped Me Watch Planes Without Looking Up
>
>  GitHub Copilot CLI Challenge Submission
>
>  Giorgi Kobaidze
>
>  Giorgi Kobaidze
>
>  Giorgi Kobaidze
>
>  Follow
>
>  Feb 13
>
>  Metal Birds Watch: Copilot CLI Helped Me Watch Planes Without Looking Up
>
>  #devchallenge
>  #githubchallenge
>  #cli
>  #githubcopilot
>
>  56 reactions
>
>  Comments
>
>  18 comments
>
>  11 min read

---

> **UnitBuilds** · 2026-09-10T19:40:59Z　
> Guess I'm 2nd. A simple question lead me down a rabbit hole... Now I have 2 ongoing projects, an IDE and a Single Address Space OS. It's probably my longest running projects and they've pushed me to really rewriting practically everything from scratch. But this 1's special, because it's where it all started...
>
>  V.E.L.O.C.I.T.Y.-OS: Kimi K2.7 and the 'Safe-Room Security' Illusion (Part 1)
>
>  Self-healing OS running in CPU L3 cache
>
>  UnitBuilds
>
>  UnitBuilds
>
>  UnitBuilds
>
>  Follow
>
>  for UnitBuilds CC
>
>  Jun 28
>
>  V.E.L.O.C.I.T.Y.-OS: Kimi K2.7 and the 'Safe-Room Security' Illusion (Part 1)
>
>  #showdev
>  #coding
>  #compilers
>  #security
>
>  23 reactions
>
>  Comments
>
>  9 comments
>
>  4 min read

---

> **Giorgi Kobaidze** · 2026-09-10T20:02:30Z　
> Oh wow, this one looks really deep and complex, I'm gonna take my time to read and analyze this. I'll get back to you in about a day or two 😄

---

> **Giorgi Kobaidze** · 2026-09-11T06:20:29Z　
> @unitbuilds A bare-metal, self-healing OS is a really creative goal. I love it, especially as a teenager I always wanted to build my own operating system, started learning low-level languages, and then reality hit. 😄 Maybe I'll come back to it one day.
>
> The part about Kimi optimizing for correctness against the spec is the most interesting thing here. It's a good illustration of how much the unstated context matters with these models and how specific you have to be about the environment the code is actually going to run in.
>
> The scanner idea is pretty neat, it reminds me of NoteRunway, another hackathon winning app that I created. One of the features of it was detecting sensitive data that people had written into notes "temporarily". But my approach was kinda the reverse of what's written here. Regex ran first as the deterministic pass, and then, optionally, an AI scan on top to catch what patterns couldn't.
>
> One thing worth flagging: in edge cases that self-correction loop could get expensive. The mechanics of this really resembles to agentic loops that keep cycling until it verifies it hit the goal, which is notoriously costly. Different use case and a much smaller scale here, but the mechanics rhyme.
>
> @pascal_cescato_692b7a8a20 great project from what I've read so far. I'm glad there are still people who do such low-level work, with proper AI usage. 👏👏👏

---

> **UnitBuilds** · 2026-09-11T06:33:25Z　
> Thanks for reading! Though on the cost-front, it really does depend on what model you use... We're all caught up on the Anthropic, Google, OpenAI models, but when you look at the eastern alternatives, eg. Kimi K2.7 or Qwen flash, Deepseek flash, suddenly it's runway becomes 100x longer for the same price as the big 3... With the OS, my goal was to also build in a tiny model (Qwen 2.5 Coder 0.5b) as a way to have 'on the fly' AI for shell interpretation, with the long-term goal being to refactor it and retrain it to speak NDA, so it can essentially 'use' the site-map as kv cache directly. Even a tiny model with sufficient and accurate context can do pretty decent edits, or atleast interpret it well enough to query a cloud model precisely on what needs to happen? Though I've also been experimenting with MoE propagation (as it runs, it trains it's own experts), inspired by Game of Life, to collapse/grow/split domain experts to keep it small and accurate, though that's still deep in the R&D phase and nowhere near done.
>
> The MCP is live and the OS is functional (albeit nowhere near what I want it to be), the IDE is also public (though please way, the patch today fixes alot).
>
> My end-goal for the project set is to have a baremetal server running the OS, with instances of the IDE per-user, as a native cloud IDE, because it's zero-alloc and built so small, literally 1gb of ram is sufficient for 10+ concurrent users, then just spin up ephemerals whenever they do compute heavy tasks, like compiling. So it becomes a cheap alternative to maintaining a local system with sufficient specs to not lag, while improving performance due to adjacency with the LLM provider (same datacenter). Long term goals, but if it works, it'd be a decent alternative to Jupyter Notebooks...

---

> **Giorgi Kobaidze** · 2026-09-11T06:58:06Z　
> I'm going to learn even more about the project whenever I have a little more free time. 👀 That sounds super interesting and well-thought!

---

> **UnitBuilds** · 2026-09-11T07:36:50Z　
> You can go through the repos on my git, IDE and MCP will be updated probably in an hour or 2. Unfortunately IDE wont immediately get the MCP update, but it got a UI overhaul to make it look and feel better, along with more memory management (150mb at idle)

---

> **Giorgi Kobaidze** · 2026-09-11T07:42:13Z　
> Awesome, noted down.✅

---

> **FrancisTRᴅᴇᴠ (っ◔◡◔)っ** · 2026-09-10T19:45:11Z　
> I guess I am third (let's keep that trend going @georgekobaidze and @unitbuilds lol)
>
>  Get Started on Dev.to! A Beginner's Guide to Engage with the Community! 💡
>
>  FrancisTRᴅᴇᴠ (っ◔◡◔)っ
>
>  FrancisTRᴅᴇᴠ (っ◔◡◔)っ
>
>  FrancisTRᴅᴇᴠ (っ◔◡◔)っ
>
>  Follow
>
>  Mar 20
>
>  Get Started on Dev.to! A Beginner's Guide to Engage with the Community! 💡
>
>  #discuss
>  #community
>  #beginners
>  #howtodevto
>
>  270 reactions
>
>  Comments
>
>  196 comments
>
>  7 min read
>
> This post I am really proud of because it made onto the official dev.to community resource page: dev.to/help/community-resources
>
> Also got a badge for that as well. :)
>
> Trying to refine the article to make the most of DEV for beginners. Looking for feedback is nice (haven't got feedback in a long time actually). Was hoping for another set of eyes to look into it! :)

---

> **UnitBuilds** · 2026-09-10T19:48:49Z　
> Definitely a must-read for anyone new! @plaidscientist This 1 is good to read and get a feel of things!

---

> **Andy Schelb** · 2026-09-10T20:42:57Z　
> Thanks @unitbuilds on it!

---

> **Giorgi Kobaidze** · 2026-09-10T20:03:16Z　
> I think I remember this one, let me check again 👀

---

> **Giorgi Kobaidze** · 2026-09-10T20:20:56Z　
> I gotta tell you, if I'd had something like this when I first joined the community, I'd have been a lot more active from day one. Great work @francistrdev !

---

> **pepapepa** · 2026-09-10T21:00:35Z　
> Here's one, not mine:
>
> dev.to/zdzhatdo/hideo-kojima-predi...
>
> No big neon sign, almost no reactions.
>
> So then W-H-Y?
>
> Two words:
>
> - Hideo
>
> - Kojima
>
> Yup, she wrote an article detailing how Kojima used so masterfully even the hardware to tell a story...
>
> Give that kid a like or a comment or something.
>
> These juniors will fix the Seniors' bugs, so maybe... dropping by their funky little articles is the least one can do.
>
> I hope she's still kicking around. Never heard from her since summer break.

---

> **Noemy15** · 2026-09-10T21:03:54Z　
> Ship integrations instantly
>
> Connect data from 50+ platforms into secure, production-ready endpoints.
>
> Launch your next project faster
>
> shorturl.at/Q04Jm

---

> **Earl Grey** · 2026-09-10T22:32:14Z　
> Hi @georgekobaidze Here's something I wrote after I walked away from the computer and realized I had an idea I wanted to come back to while on vacation A Builder in Paris: Do Devs Dream of Électrique Chats? I appreciate you being open to reading. Writing and editing an article is difficult enough especially when it accompanies a build! But this is a good reminder to give back and engage. Thank you!

---

> **Giorgi Kobaidze** · 2026-09-11T06:55:23Z　
> I loved this article from the first few sentences. Why? You mentioned rainy, cold days, those are my favourite. That's when I feel most alive. Not many people understand that about me, but there it is.
>
> I've never been to France, though.
>
> I went to Germany recently for the second time, and I've had my share of the work-to-travel switch. Here's my story:
>
> I had a flight in a few hours, so I decided to spend one of those precious hours recording a new video about a bug I found in my game and how I fixed it, alongside the article I had written.
>
> I really, really, REALLY wanted to get it done before taking off.
>
> So I recorded 20 minutes of video and started packing up to make sure that was done:
>
> "Perfect. I'll edit and upload this once I'm done packing."
>
> Oh boy... Little did I know...
> I finished packing, sat back down at my PC, opened the recording...
> No sound.
>
> Turned the volume all the way up.
> Still watching myself blab away without hearing a single word of my blabbing.
>
> "Oh no, no, no!"
>
> For some reason, my audio settings had changed and OBS Studio had decided that my microphone was no longer invited to the party.
>
> Twenty (20) minutes of beautifully recorded content.
> Absolutely.
> ⬇️
> Completely.
> ⬇️
> Utterly.
> ⬇️
> Totally.
> ⬇️
> Entirely.
> ⬇️
> Useless.
>
> That's a lot of work to go to waste.
>
> "Giorgi you idiot!"
> I was fuming.
>
> Welp, that was my next challenge to fix that.
> At that point, I had two options:
> 1. Accept defeat
> 2. Record the entire thing again
>
> The odds of option 2 were pretty low, but it still worth a shot.
>
> Now I was seriously short on time. The airport wasn't going to wait for me to finish uploading a video.
>
> Somehow, I still managed to record everything again, edit it, upload it, and get ready in time.
>
> Now what was the hardest part?
> Pretending everything was totally fine, while talking in the video.
>
> Meanwhile, internally:
> "WHY TF DID I NOT CHECK THE AUDIO?!"
> "WHAT TIME IS IT?!"
> "HOLY S..., I'M DEFINITELY GONNA MISS THAT PLANE!"
>
> But hey, that's life. Not every day is a perfectly executed 10/10 productivity story. Sometimes you just forget to check your microphone.
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> I agree completely about thinking differently once you're out of your routine. You start thinking about things that give you that small joy of discovering something inside your own head. It's like leaving your usual noisy route and taking the backroads, where everything is quieter and better. Especially for people like us, who are more or less always working.
>
> By the way, I didn't know that book you were reading. Noting it down.
>
> I also walk like a maniac. On my last trip I averaged well over 150,000 steps in total, I just love walking that much.
>
> And sorry about your loss. Coming home to a meow-free house must be hard.
>
> You're right that the building never stops. Our brains are remarkable at figuring things out on their own and adapting to whatever they're dropped into. San Francisco to Paris would be a bigger jump than my trip was I'm in Europe anyways, so Germany is a three or four hour flight, barely a change of scenery by comparison.
>
> California to France is different in weather, culture, food, everything. I lived in California for a few months, so I know how wide that gap is, and I think it's wider in your direction than mine. In Europe, American culture is already everywhere and everyone speaks English, so arriving there from Europe isn't much of a shock, also (I would say that California and the US in general has much better vibes than Europe). Going the other way is definitely a huge jump, and that's exactly the kind of jolt that makes you see things differently, that's why it was so inpiring to you.
>
> This is one of the best articles I've read in a while!👏

---

> **Earl Grey** · 2026-09-14T22:35:42Z　
> Thank you for taking the time to read the article so thoroughly. That's a big ask and I appreciate it. Especially since this one was an emotional story, too! I hope California treated you well while you were here. :-)

---

> **Giorgi Kobaidze** · 2026-09-15T04:49:31Z　
> No, thank you for sharing, it was one of the best write-ups, I ever read here, honestly.
>
> As for CA, I've been in many places but CA remains the best one, by far. Even though I like cold and rainy weather 😄 I mean the weather was absolutely perfect, but it's not about the weather, it's about everything combined: the city, the people, the culture, the everything.

---

> **Earl Grey** · 2026-09-16T02:12:13Z　
> It can be a great mix in the right doses for sure, just like anything else I suppose. So glad to here you enjoyed it!

---

> **Giorgi Kobaidze** · 2026-09-16T04:30:11Z　
> To be fair, rain in California is nothing I have seen anywhere else. I mean, it's super rare, but when it rains, it REALLY rains relentlessly😄 it was super cool to watch.

---

> **James Carter Kula** · 2026-09-15T20:14:16Z　
> U.S. Business Partnership Opportunity
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> ThomasWilson881992 @ 0utl00k dot com
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **CitronBrick** · 2026-09-15T17:24:03Z　
> You can embed your Dev.to articles in Dev.to using
>
> {%embed dev.to %}
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> It gives a better visual appeal.

---

> **Earl Grey** · 2026-09-16T02:11:05Z　
> Thanks for the tip!

---

> **Krishna Tangudu** · 2026-09-10T23:08:55Z　
> To explain how moving data is easier than moving knowledge
>
> dev.to/swaroop_krishna_e2f4b83b2/m...

---

> **Ekong Ikpe** · 2026-09-11T00:26:36Z　
> My humble story. Probably my best-compressed version of just discovering who I've been. After writing it, it felt like I was reading a post written by someone else. 🤔
>
> dev.to/edmundsparrow/gnoke-poc-pro...

---

> **James Carter Kula** · 2026-09-15T20:20:30Z　
> 🤝U.S. Business Partnership Opportunity🤝
>
> 🚩
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> 💬ThomasWilson881992 @ 0utl00k dot com🤝
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **xulingfeng** · 2026-09-11T00:34:17Z　
> dev.to/xulingfeng/our-cto-built-an...
>
> This is my personal favorite piece from my older series. I tried not to dumb down the villain artificially, yet it didn’t get much engagement. It marks the first appearance of character P, the protagonist in my ongoing Thirty-Six Stratagems series. Looking forward to your thoughts, hahaha.😆

---

> **Giorgi Kobaidze** · 2026-09-12T16:34:07Z　
> I started reading this outside, during a few idle minutes and got about halfway through... I can't wait to finish it. It's SO well-written, I really felt like I was reading an extremely good book.
>
> I'll send you my full feedback once I'm done. 🙏

---

> **xulingfeng** · 2026-09-12T23:58:39Z　
> Thank you so much for the kind words! It makes me really happy to hear it feels like reading a book. Take your time, I’m looking forward to your full feedback 😆

---

> **Giorgi Kobaidze** · 2026-09-13T11:24:20Z　
> First things first, I knew something was going to go badly the moment you said the room applauded Drew. All anyone had seen was a demo, running on test data he prepared himself.
>
> It reminds me of a meme I saw the other day: a guy gets an incident on production and his boss gives him until EOD to fix it, so he rewrites the health check endpoint to always return healthy. No actual fix is done. Then he writes something along the lines: "The database was on fire, but everyone was happy. Perception is reality."
>
> Same thing here. Nobody had any idea how that model would behave in practice, but it came from Drew - a decorated principal architect, PhD, the whole résumé. How could he possibly be wrong about anything, right?! Sometimes people look at how things appear instead of how they actually are.
>
> "He doesn't need QA, because he proved his system is mathematically safe." Famous last words before a complete disaster.
>
> "You've got good data. But data isn't architecture." - this one really made me think, and I'm still trying to work out what it's supposed to mean. To me it reads like "I can't justify my architecture, so I'll state something ridiculously obvious to confuse everybody so much that nobody can even ask a follow-up question."
>
> Of course data isn't architecture, Drew. But architecture isn't separate from data either, the shape of your data has a huge impact on how you build your architecture. When something breaks, it's usually either the architecture or the data, and from what you describe here, the data was fine.
>
> "He fixed one tree. The forest was still burning." I'm writing that one down. OMG this is so good!😄
>
> Also: there aren't many things worse than the regulator's representatives showing up at the front desk.🥶 That's when you know you've REALLY messed up. And they're not going to ask for architecture documents, for sure, all they care about is whether their rules were breached.
>
> The part that shocks me most is that there was no logging of every step and every approval. For someone like Drew that should have been a no-brainer from day one.
>
> Anyway, this is one of the best articles I've read here. The storytelling, the technical insights, the reminder that even the most senior people in a company get things wrong and that we should listen to everyone, a real lesson for all of us. I'm glad I read it, and I'll go through the rest of the series once I've caught up on my reading list.
>
> Thank you!

---

> **xulingfeng** · 2026-09-13T11:29:53Z　
> Hahaha,😆 I’m thrilled this story hits home for you! That line “He fixed one tree. The forest was still burning” is my favourite metaphor in the whole piece.
>
> You’re exactly right about logs and regulators. When audit comes knocking, pretty architecture slides and mathematical proof count for almost nothing. What matters is the complete, traceable record of every action and approval.
>
> It’s so easy to be dazzled by fancy titles and polished demos. That’s exactly why independent QA and objective logging are non-negotiable. Hope you enjoy the rest of the series! 🤝

---

> **Giorgi Kobaidze** · 2026-09-13T11:33:07Z　
> I definitely will, looking forward to reading them!👀

---

> **Tejas Shinkar** · 2026-09-11T03:21:04Z　
> This one's my pick! It's the AWS Networking Fundamentals piece on VPC, subnets, IGW/NAT, and the whole SG vs NACL split. I actually gave up on this concept the first time around, went back and learned networking fundamentals from scratch just to understand why any of it worked, then came back to this. The moment it finally clicked visually (stateful vs stateless, and why that changes the rules for each) was the best "oh THAT'S why" moment I've had in this whole learning journey. Would love your take on it.
>
> dev.to/tejas_shinkar/aws-networkin...

---

> **GrahamTheDev** · 2026-09-11T06:48:59Z　
> I'm going to hold you to your word and administer a quiz after 😜
>
>  101 Digital Accessibility (a11y) tips and tricks
>
>  GrahamTheDev
>
>  GrahamTheDev
>
>  GrahamTheDev
>
>  Follow
>
>  Jul 30 '21
>
>  101 Digital Accessibility (a11y) tips and tricks
>
>  #webdev
>  #html
>  #a11y
>  #beginners
>
>  623 reactions
>
>  Comments
>
>  62 comments
>
>  68 min read

---

> **Giorgi Kobaidze** · 2026-09-11T07:12:23Z　
> Oh my goodness, and I thought I was someone who loved writing huge articles. I’m gonna need to take a full day-off just to read this😂
>
> Just kidding, the weekend is coming up soon and I’ll have time to go through this monstrosity.😄

---

> **Giorgi Kobaidze** · 2026-09-13T14:44:32Z　
> You might not believe me, but I just finished reading. A promise is a promise, I need to live up to it. 😄
>
> Coming at this from a back-end background, my accessibility strategy up to now has mostly been trusting that whoever writes the frontend knows what they're doing. Turns out that's not a strategy, it's a prayer.
>
> What I appreciate most is that this isn't written as a compliance checklist. Every point explains who it actually helps and why.
>
> Great read, and structured exactly right for the length, I'll be coming back from time to time to it a section, rather than trying to absorb it in one go.
>
> Thanks for putting the hours in!
>
> I've never seen an article with a read time of over an hour 😄
>
> And to be honest, it took me well past 68 minutes. Closer to 100 by my calculations.

---

> **GrahamTheDev** · 2026-09-13T16:20:52Z　
> Yeah, I dont trust reading length on it! haha
>
> Glad you enjoyed it and thanks for the article prompting others to share, I enjoyed some of the others!

---

> **Giorgi Kobaidze** · 2026-09-13T16:28:04Z　
> Awesome! Glad to hear it!

---

> **Hadil Ben Abdallah** · 2026-09-11T09:25:42Z　
> Hi @georgekobaidze. Here's the article I think I'm most proud of. This article got over 13K views in less than 3 days.
>
>  Coding Without Pressure: How Slowing Down Helped Me Learn Faster
>
>  Hadil Ben Abdallah
>
>  Hadil Ben Abdallah
>
>  Hadil Ben Abdallah
>
>  Follow
>
>  Dec 25 '25
>
>  Coding Without Pressure: How Slowing Down Helped Me Learn Faster
>
>  #webdev
>  #productivity
>  #programming
>  #codenewbie
>
>  320 reactions
>
>  Comments
>
>  95 comments
>
>  3 min read
>
> Even though I wrote this article with the same passion and love I put into all my other articles, I think I might love this one the most because so many people reached out to me by email and on LinkedIn just to thank me for writing it. I received so many kind messages.

---

> **Giorgi Kobaidze** · 2026-09-11T17:49:32Z　
> What I love in this article is that it's brief, but somehow it contains SO MUCH relatable information, I don't even know where to start.
>
> Actually, this stuff is painfully relatable. When I was still a junior engineer, I sometimes used to try to learn everything almost by heart, because I thought that's how real developers used to work. Without minimal googling, minimal StackOverflow browsing, all by themselves (there was no such thing as Claude Code or Codex yet 😄 )
>
> Then the reality punched me right in the face... hard.
>
> We don't realize that just consuming information is nothing but pretending to be doing something... pretending that we are progressing.
>
> So when does the real progress come? I think you know the answer... yes, when you actually do something, when you're in motion, when you have 10 different bugs to fix and you have zero clue how to do it, but you still gotta find out, because your career depends on it.
>
> This builds both character and skills. It's hard to succeed without both.

---

> **CapeStart** · 2026-09-11T10:20:56Z　
> Love this. Sometimes the piece you’re proudest of just had terrible timing and disappeared into the feed.

---

> **Giorgi Kobaidze** · 2026-09-11T10:44:01Z　
> Totally agree, I just hate when I see so many great posts not getting nowhere near as much recognition as they deserve, just because the authors aren’t that popular yet.
>
> And someone might generate an article using AI in 10 minutes that literally doesn’t contribute to anything at all and get tens of thousands of views - that’s unfair.
>
> I hope this post will help at least a few people get the recognition they deserve.⭐️

---

> **Giorgi Kobaidze** · 2026-09-11T17:24:22Z　
> @capestart By the way, don't you want to share something from your own archive? I'd love to read the post you're proudest of. 👀

---

> **Omar Afifi** · 2026-09-11T11:08:50Z　
> My Phone Broke, and Gemini Fixed It
>
>  Omar Afifi
>
>  Omar Afifi
>
>  Omar Afifi
>
>  Follow
>
>  Sep 9
>
>  My Phone Broke, and Gemini Fixed It
>
>  #android
>  #gemini
>  #googleai
>  #debugging
>
>  17 reactions
>
>  Comments
>
>  3 comments
>
>  8 min read
>
> After pulling an all-nighter, an accidental ADB command triggered an undocumented, zero-Google-results debug overlay on my OnePlus that survived reboots. Instead of the usual "back up and factory reset" advice, I used Gemini to systematically reverse-engineer the phone's proprietary UI bytecode (DEX parsing) live in the terminal and pinpoint the exact persistent property causing it.
>
> It’s special to me because it bridges deep Android internals with real systems engineering, turning a nightmare bug into one of the coolest debugging sessions I've ever had. Hope you enjoy reading it!

---

> **Giorgi Kobaidze** · 2026-09-11T19:08:19Z　
> This piece of writing is seriously impressive both in terms of storytelling and technical explanation.
>
> Right from the start of the article, I was so intrigued to know what was the actual problem causing that stubborn, red text that wouldn't go away.
>
> That really reminded me one of those all nighters of mine. I'd spent the whole evening, night, and morning debugging one silly problem. I can't express the level of happiness I had when I finally found it.
>
> Our job is tough, but it's also so rewarding!
>
> Great job! 👏

---

> **Omar Afifi** · 2026-09-12T04:18:59Z　
> Thank you so much, Giorgi! Honestly, reading this made my day. When writing the post, I really wanted to capture that emotional rollercoaster of debugging, so knowing that both the technical dive and the story resonated with you means a lot. That amazing feeling of finally cracking a bug after an exhausting all-nighter is truly unmatched, and I'm glad it brought back those memories. You nailed it: tough job, but moments like that make it completely worth it! 🙌

---

> **Giorgi Kobaidze** · 2026-09-12T09:49:47Z　
> It absolutely is worth it. And by the way, I've never used Gemini for coding, and I'd seen people say it wasn't great at it.
>
> But it actually did a great job. So a massive 'W' for Gemini! And ultimately for you.

---

> **Omar Afifi** · 2026-09-12T18:11:46Z　
> Totally agree! Gemini gets a lot of criticism, and many people think it's behind other models. But as a student in Egypt, paid subscriptions for tools like ChatGPT or Claude are honestly way too expensive.
>
> Google gives great deals for students, which makes it my go-to. Plus, they keep improving it. I feel Google is focusing more now on making their models fast and practical for everyday tasks, and the newer Flash versions are way better than before.
>
> It definitely earned that 'W' this time xD! Thanks again, Giorgi! 🙌

---

> **Giorgi Kobaidze** · 2026-09-12T18:13:45Z　
> Kudos to Google for making their services accessible for students everywhere⭐️

---

> **Puneet-Kumar2010** · 2026-09-11T11:46:32Z　
> okay... so i'll go with this one
>
>  I Built the Product. Made It Open Source. Deployed It Cheaply. Then... 7 Users Signed Up.
>
>  Comments suggest adding social logins
>
>  Puneet-Kumar2010
>
>  Puneet-Kumar2010
>
>  Puneet-Kumar2010
>
>  Follow
>
>  Aug 6
>
>  I Built the Product. Made It Open Source. Deployed It Cheaply. Then... 7 Users Signed Up.
>
>  #discuss
>  #buildinpublic
>  #opensource
>  #indiehack
>
>  28 reactions
>
>  Comments
>
>  51 comments
>
>  2 min read

---

> **Caleb Weeks** · 2026-09-11T11:53:56Z　
> This is my first post on DEV. I did not expect to have a lot of readers for my first post, but it's my most read by far. I think maybe DEV promotes first posts?
>
> dev.to/sethcalebweeks/haskell-quic...

---

> **Giorgi Kobaidze** · 2026-09-19T15:48:15Z　
> Fun read, and a good use of the algorithm as a vehicle for explaining Haskell syntax rather than the other way round.
>
> Coming from C#, the same shape falls out of LINQ almost unchanged:
>
> static IEnumerable Qs(IReadOnlyList xs) where T : IComparable =>
>  xs.Count == 0
>  ? Enumerable.Empty()
>  : Qs(xs.Skip(1).Where(a => a.CompareTo(xs[0]) <= 0).ToList())
>  .Append(xs[0])
>  .Concat(Qs(xs.Skip(1).Where(a => a.CompareTo(xs[0]) > 0).ToList()));
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Ali Navidi** · 2026-09-11T12:17:15Z　
> I guess mine is this one:
>
>  A Letter to Jobseekers: Don't Give Up!
>
>  Ali Navidi
>
>  Ali Navidi
>
>  Ali Navidi
>
>  Follow
>
>  Nov 21 '24
>
>  A Letter to Jobseekers: Don't Give Up!
>
>  #mentalhealth
>  #programming
>  #motivation
>  #career
>
>  47 reactions
>
>  Comments
>
>  17 comments
>
>  2 min read

---

> **Giorgi Kobaidze** · 2026-09-12T16:58:30Z　
> Great read! It's so relatable for I think pretty much everyone in our field, which sometimes can be way too tough and unforgiving, however, at the same time, it's also extremely rewarding when you succeed at something, whether it is landing a good job, winning a competition, finishing a project, and hundreds of other things.
>
> I can absolutely relate to this, because I've had my own fair share of rock bottom, which back then seemed like it was the end of my career, but looking back, I think I'd have never achieved half of what I have achieved without it.
>
> We just need to find out how to take advantage of bad situations for our own good, that definitely is a superpower.
>
> Keep grinding! 🔥

---

> **Ali Navidi** · 2026-09-13T17:32:05Z　
> Thanks🫶🏻

---

> **Elsie Rainee** · 2026-09-11T13:27:32Z　
> Here's mine. It's a month-long comparison of pair programming with Cursor, GitHub Copilot, and Claude Code across real tasks like debugging, refactoring, and multi-file changes, not just toy prompts like "build a todo app." What made it special to me was realizing that context mattered more than raw generation speed, and that the real productivity gain came from combining AI output with normal engineering discipline like reviewing diffs and testing edge cases, not just accepting whatever the tool produced.
>
> I Tried Pair Programming With Three Different AI Tools For a Month

---

> **alptekin I.** · 2026-09-11T13:29:45Z　
> dev.to/alptekin/dreams-cheers-daj
>
> not my best, I hope :)).
>
> but kind of my first post (if we omit the one i wrote several years ago). It is pity that i could not still add a new article upon this one. (I am hopeful though, i will be more productive in coming months...).
>
> This article is important for me because, it tells about some of my dreams, which are still valid and waiting to be fulfilled, one day.
>
>  Dreams & Cheers
>
>  alptekin I.
>
>  alptekin I.
>
>  alptekin I.
>
>  Follow
>
>  Jan 23 '25
>
>  Dreams & Cheers
>
>  #devchallenge
>  #newyearchallenge
>  #career
>
>  28 reactions
>
>  Comments
>
>  4 comments
>
>  4 min read

---

> **Giorgi Kobaidze** · 2026-09-11T17:34:10Z　
> This is an amazing read.
>
> I feel I do not belong there, but it is too late, with some fierce courage I had sent my request to talk months ago and to my surprise it was accepted. Now I am there, just minutes before the talk, thrilled...
>
> See? That's the key quote in this article. You don't know what's behind the door until you step inside. I admire anyone who has courage to stick around where they "don't belong" only to find out they don't just belong there, even more - it's their natural habitat.
>
> I hope you'll achieve the rest of your goals soon. 🔥

---

> **alptekin I.** · 2026-09-14T07:45:04Z　
> Thanks a lot. I hope too :)

---

> **CitronBrick** · 2026-09-13T19:33:47Z　
> You can embed your Dev.to articles in Dev.to using
>
> {%embed dev.to %}
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> It gives a better visual appeal.

---

> **alptekin I.** · 2026-09-14T07:54:54Z　
> thanks, i did not know this.

---

> **CitronBrick** · 2026-09-14T09:36:16Z　
> Nice to see you having edited it already.

---

> **Self-Correcting Systems** · 2026-09-11T13:37:45Z　
> The one I’m most proud didn’t get much interaction but this is the one I think matters most to me.
>
> dev.to/kenielzep97/the-art-of-the-...

---

> **Cesar Aguirre** · 2026-09-11T15:11:48Z　
> This one:
>
>  The Most Painful Career Lesson My Best Job Taught Me
>
>  WeCoded 2026: Echoes of Experience 💜
>
>  Cesar Aguirre
>
>  Cesar Aguirre
>
>  Cesar Aguirre
>
>  Follow
>
>  Mar 23
>
>  The Most Painful Career Lesson My Best Job Taught Me
>
>  #devchallenge
>  #wecoded
>  #dei
>  #career
>
>  73 reactions
>
>  Comments
>
>  41 comments
>
>  3 min read

---

> **Giorgi Kobaidze** · 2026-09-11T17:59:42Z　
> Oh, I remember this one, I even commented on this post.
>
> I like how you picked an article titled "The Most Painful Career Lesson My Best Job Taught Me" as your favorite.
>
> That just shows me that you not trying to forget bad experiences, you embrace them. Trust me, not everyone can do that. I used to be pretty bad at that.
>
> But as you gain more experience, you realize there's no such thing as a "bad experience" in a career. Bad experiences teach you far more valuable lessons than good ones do.

---

> **Cesar Aguirre** · 2026-09-12T20:57:21Z　
> Glad to hear someone else remember that post. Thanks for your comment on that post :)

---

> **Giorgi Kobaidze** · 2026-09-12T21:09:39Z　
> Least I can do. 🙏

---

> **Harsh Raval** · 2026-09-11T17:27:07Z　
> This is the article I’m most proud of recently! 🚀
>
> I experimented with different AI design tools to build my portfolio and shared what actually worked, what didn’t, and how the final result impacted how potential clients viewed my work.
>
> What makes it even more special to me is that the article was featured among DEV’s Top Weekly Posts. 🏆
>
> Would love to hear your thoughts after you read it!
>
> 👉 I Let AI Design Tools Build My Portfolio Site — Clients Noticed

---

> **Giorgi Kobaidze** · 2026-09-13T12:36:44Z　
> Extremely interesting read, especially for someone who's going to need neat designs for a few upcoming projects. My background is in back-end engineering, which doesn't help much when it comes to judging which design fits which project, that's one skill I really need to get good at.
>
> I've built plenty of side projects, but I still don't have a portfolio website. Part of the reason is that I want it to be really, really good, so I never manage to start at all. I think I need to change that, just start somewhere and figure the rest out later.
>
> The title also made me think the clients had figured out the work was done with AI help and disliked it for that reason. Glad it turned out to be the other way around.
>
> And this quote, "Fast generation is useful. Blind acceptance isn't, is an absolute gem.
>
> Great read, and really useful for future me. I'll pull this article back up when I get to the "decide what tool to use" step. I'm sure it'll make the decision faster.
>
> Thanks a lot for sharing! 🙏

---

> **TheBitForge** · 2026-09-12T06:47:50Z　
> From Idea to Launch: How Developers Can Build Successful Startups
>
>  TheBitForge
>
>  TheBitForge
>
>  TheBitForge
>
>  Follow
>
>  Dec 21 '25
>
>  From Idea to Launch: How Developers Can Build Successful Startups
>
>  #startup
>  #programming
>  #productivity
>  #node
>
>  182 reactions
>
>  Comments
>
>  49 comments
>
>  65 min read

---

> **Tanay Dwivedi** · 2026-09-12T12:37:29Z　
> dev.to/tanay_dwivedi9098/i-develop...
>
> One of the article I'm most proud of. As while developing this application, I learnt many new concepts.

---

> **Lawrence Cooke** · 2026-09-12T15:33:39Z　
> This one was my first real dip into writing tech articles, it was fun for me, not only writing it ,but spending the time delving into the database to prove what I was writing was facts. So this one meant a bit to me in that sense :
>
>  SQL Common Table Expressions and Window functions
>
>  Lawrence Cooke
>
>  Lawrence Cooke
>
>  Lawrence Cooke
>
>  Follow
>
>  Jul 30 '23
>
>  SQL Common Table Expressions and Window functions
>
>  #sql
>  #mysql
>  #database
>  #datascience
>
>  25 reactions
>
>  Comments
>
>  2 comments
>
>  7 min read

---

> **CitronBrick** · 2026-09-15T17:27:10Z　
> You can embed your Dev.to articles in Dev.to using
>
> {%embed dev.to %}
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> It gives a better visual appeal.

---

> **Henry Robt** · 2026-09-12T15:59:32Z　
> I like the idea behind this thread because some of the most worthwhile articles can easily get buried after publication. It’s also a nice way to discover different writing styles and topics from people in the community that you might otherwise miss.

---

> **Giorgi Kobaidze** · 2026-09-12T16:10:34Z　
> Oh, tell me about it. In the past two days I've come across a wealth of articles I never knew existed. It's mindblowingly overwhelming.
>
> BTW, to make sure these articles don't only end up in this thread, I'm going to publish another article where I specifically highlight each of the articles commented here.

---

> **nyaomaru** · 2026-09-12T16:01:48Z　
> Funny article! 😸
>
> My favorite is this one 👇 I introduced how my OSS is used in a real production system serving over 100,000 users. 🚀
>
>  is-kit Reached 50 Stars ⭐ Here’s How We Use It in Production
>
>  Real-world scale for type safety
>
>  nyaomaru
>
>  nyaomaru
>
>  nyaomaru
>
>  Follow
>
>  Aug 12
>
>  is-kit Reached 50 Stars ⭐ Here’s How We Use It in Production
>
>  #typescript
>  #opensource
>  #webdev
>  #frontend
>
>  85 reactions
>
>  Comments
>
>  21 comments
>
>  7 min read

---

> **Giorgi Kobaidze** · 2026-09-19T09:20:36Z　
> This is a really interesting and seemingly fun project. Keep it maintained!
>
> By the way, congrats on already 77 stars!⭐️

---

> **nyaomaru** · 2026-09-19T12:11:13Z　
> Thanks! I’ll keep maintaining it and improving it toward v2. 😸
>
> And thank you for the congrats on 77 stars! ⭐️

---

> **Amit Chandra** · 2026-09-12T17:27:18Z　
> Your personal AI assistant, powered by the models you choose. Connect leading AI providers and messaging platforms through a single intelligent gateway. Remember context across conversations, communicate by voice, and automate everyday work. Run locally, protect your privacy, and customize everything with an extensible plugin SDK.
>
> dev.to/amitchandra/i-built-a-local...

---

> **Giorgi Kobaidze** · 2026-09-19T08:48:10Z　
> Nice concept, I really like the idea. Well done!👏

---

> **CanWeShip** · 2026-09-12T17:46:36Z　
> Holding you to the promise 🙂
>
> Mine is my first ShowDEV: USPS can charge you $50 after the package ships. I built a free checker to catch it before you buy the label
>
> It's half research rabbit hole, half build story. While digging into why sellers get hit with a $50 hazmat fee after their package was already accepted and delivered, I found that USPS's own documents contradict each other on how the fee works — and the newest rule (USPS Returns, starting 2027-02-01) isn't in the Federal Register at all, only in a Postal Bulletin. So I built a free pre-shipping checker where no LLM decides the answer: every verdict comes from a cited, versioned rule set, and "unknown" beats "probably fine".
>
> Even if you never ship a battery in your life, the fee part is a fun read. Comments and roasts welcome — first post here.

---

> **Kushal Baral** · 2026-09-12T17:52:33Z　
> .

---

> **Giorgi Kobaidze** · 2026-09-12T18:15:33Z　
> Wanna share your favorite one? Just drop it here and let’s let others know about your best work!

---

> **Elanat Framework** · 2026-09-12T18:55:47Z　
> This is the latest article I have written. It holds special significance for me because it demonstrates the remarkable power of WebForms Core technology in building web pages. Please take a close look at the example provided in the article; I encourage you to try writing an equivalent version yourself—or with the help of AI—using React, Blazor, or any other framework you prefer, and then compare it with this example.
>
>  Great News for the Rust Community: A New Server-Driven UI Technology in Rust
>
>  Elanat Framework
>
>  Elanat Framework
>
>  Elanat Framework
>
>  Follow
>
>  Sep 11
>
>  Great News for the Rust Community: A New Server-Driven UI Technology in Rust
>
>  #news
>  #rust
>  #actix
>  #webformscore
>
>  6 reactions
>
>  Comments
>
>  1 comment
>
>  7 min read

---

> **Giorgi Kobaidze** · 2026-09-19T07:35:15Z　
> Nice writeup, the Actix example is easy to follow end to end, and I like that the HTML stays plain HTML.
>
> One thing I'd be curious about: the place criteria are passed as strings ("*?t>:19\\*?t<:20"), so a typo still compiles and only shows up at runtime. Is a more typed builder API on the roadmap for the Rust crate, or is the string form intentional to keep parity with the other language implementations?
>
> Would also love to see an example where the server is doing something it uniquely can, validation or permission-based UI, since that's where this model seems strongest.

---

> **Elanat Framework** · 2026-09-19T09:24:37Z　
> Thank you for taking the time to read the article.
>
> Yes, a typo only reveals itself at runtime.
>
> WFC relies on a shared C# codebase that has been adapted for other languages. While implementing strong typing in C# is relatively straightforward, doing so across all the other languages ​​would make the task significantly more complex.
>
> In fact, the design principles of all our systems run counter to concepts like strict typing and tight coupling.
>
> That is why I focused the examples on WFC’s offline capabilities. Of course, validation and permission checks can still be properly handled on the server—where they belong.

---

> **𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 ** · 2026-09-12T18:57:52Z　
> I have..

---

> **Giorgi Kobaidze** · 2026-09-12T19:03:55Z　
> Wanna share with me? I’d be glad to read it!🙏

---

> **𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 ** · 2026-09-14T15:30:37Z　
> I have no interesting article. 😅

---

> **Giorgi Kobaidze** · 2026-09-14T15:35:11Z　
> I don’t believe you. 😄
>
> Pick the one that feels special to you. It doesn’t have to be perfect or anything.
>
> Is my favorite article perfect?
>
> Absolutely not, far from it.
>
> But it’s special.

---

> **𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 ** · 2026-09-14T15:48:58Z　
> I think this one here

---

> **Giorgi Kobaidze** · 2026-09-14T15:52:50Z　
> Awesome! Noted ✅😊

---

> **𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 ** · 2026-09-14T17:53:06Z　
> You are so kind.. wow 🥰

---

> **Giorgi Kobaidze** · 2026-09-14T18:09:25Z　
> Okay, just finished reading, now it's feedback time 😄
>
> First of all, what a story. Wow! Everyone has their own story about how they started programming and all of them are special, but some are more special than others. The fact that you wrote a whole post about it, so brief, yet so detailed, says a TON!
>
> I'm also someone who loves both gaming and engineering, and I find it hard to balance the two. After a week of non-stop coding, I want to relax and play something, but my eyes can't take any more screen time. I still play when I really want to, though (rarely these days).
>
> Your dad deserves huge credit for noticing your talent. Especially for an introvert there's no better job than software engineering. I'm an introvert too, so I know. But I had to learn to be extroverted for my career, but deep down I'm still someone who enjoys a quiet Friday night at my PC playing RDR2, Cyberpunk, and other great games.
>
> By the way, my first hello world was in C++, 20 years ago. I was 11. Borland C++, an extremely bare-bones editor. Simpler times.😄

---

> **James Carter Kula** · 2026-09-15T20:14:45Z　
> U.S. Business Partnership Opportunity
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> ThomasWilson881992 @ 0utl00k dot com
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Henk van Hoek** · 2026-09-12T21:34:23Z　
> It is my last post of today. I'm proud of what I have achieved in the last 1,5 year with developing Njord-Deploy.
>
> I'm not a guru in marketing, but I like developing s/w so I accept your invitation to mention the post I'm most proud of which is about Njord-Deploy

---

> **Suprie** · 2026-09-12T23:49:11Z　
> This is my latest post, any inputs or comments will be much appreciated.

---

> **Avinash Pal** · 2026-09-13T00:51:28Z　
> I wrote two practical books for Linux developers, and I’d love feedback from the community
>
> Over the last few years working with Linux, C, embedded systems and kernel-level code, I kept seeing the same problem: there are plenty of resources explaining individual concepts, but it can be difficult to connect C programming → Linux internals → real kernel/driver code.
>
> So I decided to write books around that approach.
>
> 📘 Think Like a Linux Kernel Developer
>
> A practical journey from C fundamentals to real Linux kernel concepts and device-driver patterns.
>
> It covers things like:
>
> - C concepts that matter when working in the kernel
>
> - container_of
>
> - intrusive linked lists
>
> - notifier chains
>
> - reference counting
>
> - VFS and system calls
>
> - driver operations
>
> - understanding real kernel source code
>
> 📕 Think Like a Linux Storage Engineer
>
> Focused on Linux storage from an engineering and interview perspective.
>
> Topics include:
>
> - Linux storage architecture
>
> - ext4, XFS and Btrfs
>
> - journaling
>
> - I/O stack and I/O schedulers
>
> - NVMe, SATA and SAS
>
> - iSCSI and Fibre Channel
>
> - debugging and troubleshooting storage issues
>
> - practical interview-oriented concepts
>
> I tried to keep the books practical rather than making them just another collection of definitions. The goal is to understand why things work the way they do, and then see how that knowledge appears in real Linux systems and kernel code.
>
> 📥 Direct PDF Download:
>
> book-direct-download.lovable.app
>
> The website has the PDF versions of my books available for direct download, so you can read them on a laptop, desktop, Android or iOS device.
>
> 📚 Google Play Books:
>
> lnkd.in/grGmA3Q4
>
> 👨‍💻 My LinkedIn profile:
>
> linkedin.com/in/avinash-pal-b885a026/
>
> I’m sharing this mainly with the Linux, kernel, embedded and systems programming community. I’d genuinely appreciate feedback on the books, the topics covered, and what you think should be added to future editions.
>
> Thanks to everyone building and learning in this space.

---

> **Yash Kumar Saini** · 2026-09-13T05:23:04Z　
> Not sure if you will read all the article, but this one was my best shipped a core feature into a open source project
>
> dev.to/yashksaini/adding-webrtc-to...
>
> Really proud as I worked close together with the core team, maintainers and with a mentor. Working with them, I really enjoyed the week and time spent during the feature building.

---

> **Giorgi Kobaidze** · 2026-09-13T05:33:01Z　
> I’m definitely gonna read all of them, no matter how much time it takes.
>
> It’s a slow process, but it’s really fun at the same time.😄
>
> I’ll get to your post as soon as I can🙏

---

> **Giorgi Kobaidze** · 2026-09-13T17:21:08Z　
> Really interesting read, and deep enough that I had to go and research a few concepts to follow it properly. I came in knowing roughly what WebRTC was for and not much beyond that, so trio, SCTP framing and the whole certhash mechanism were all new territory for me. Worth the detour, it's rare to find a write-up that assumes you'll do that work and rewards it.
>
> Also appreciated the honesty about scope. Keeping #546 open and saying plainly that this advances the issue without satisfying it is rarer than it should be.
>
> Great write-up, preserving the trade-offs as they actually came up in review, instead of the tidy past-tense version, is what makes it worth the reading effort. 🫡

---

> **CitronBrick** · 2026-09-15T17:23:22Z　
> You can embed your Dev.to articles in Dev.to using
>
> {%embed dev.to %}
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> It gives a better visual appeal.

---

> **Yash Kumar Saini** · 2026-09-15T17:36:20Z　
> Thanks for the tip Citron

---

> **Feezan Khattak** · 2026-09-13T05:40:57Z　
> Go & read this one.
>
> feezankhattak.com/blog/prevent-dou...

---

> **Mike Talbot ⭐** · 2026-09-13T08:43:21Z　
> I've made the entire architecture of multiple projects built on the model of Inversion of Control I discuss in this article, because it makes teams able to work much better in parallel. It's perfect for AI agents, for exactly the same reason...
>
> As a bonus it also includes a game, fully playable in the article post :)
>
>  A SOLID framework - Inversion of Control Pt 1
>
>  Mike Talbot ⭐
>
>  Mike Talbot ⭐
>
>  Mike Talbot ⭐
>
>  Follow
>
>  Jun 19 '20
>
>  A SOLID framework - Inversion of Control Pt 1
>
>  #showdev
>  #javascript
>  #react
>  #tutorial
>
>  66 reactions
>
>  Comments
>
>  Add Comment
>
>  17 min read

---

> **Giorgi Kobaidze** · 2026-09-13T14:27:29Z　
> Coming at this from the .NET side, and it's interesting how differently the same principle gets taught depending on the ecosystem. When someone says "inversion of control" to a C# developer, nine times out of ten they mean constructor injection and a container. Something else decides which implementation gets handed in. What you're describing inverts something bigger: who decides what happens next. Same principle, much wider scope.
>
> The open/closed section is where it clicked for me. Translated into my world, a plug is basically registering another handler into a collection the dispatcher already iterates over, and "intercept at a higher priority" is a decorator wrapping the existing implementation and choosing whether to call inner at all. I've written both plenty of times without ever thinking of them as the same idea wearing different clothes.
>
> One difference I keep coming back to: your plugs become active because a module was imported, so the wiring is implicit. In .NET the composition root is explicit, open Program.cs and the whole graph is right there. Better traceability, but slightly worse on the "code written years later plugs in with no changes" promise, because someone still has to add the registration. Assembly scanning gets most of the way there and brings back the same "where did this come from?" question.
>
> I also appreciated that you didn't force Liskov. Most SOLID articles try to make all five fit perfectly, so admitting one is a stretch because IoC favours composition actually made me trust the rest more.
>
> The per-client customisation point is the practical part I'm taking away: whether a feature exists comes down to whether the module is loaded, instead of a flag threaded through the component that has to know about every variation. That's a much cleaner answer than what I usually end up with.
>
> Great read! Nice game BTW! 🎮️🕹️

---

> **Roland Doda** · 2026-09-13T08:47:17Z　
> Great idea! Here is the article I am most proud of: rolandi.dev/blog/modular-frontend-...
>
> And surprisingly, this is the article I've got many positive messages thanking me: rolandi.dev/blog/agent-harness

---

> **James Carter Kula** · 2026-09-15T20:19:15Z　
> 🤝U.S. Business Partnership Opportunity🤝
>
> 🚩
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> 💬ThomasWilson881992 @ 0utl00k dot com🤝
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **SameerQaisar17** · 2026-09-13T08:55:31Z　
> I'm exactly the person you're talking about — I published my first article last week.
>
> The one I'm most proud of is my very first one: "If-Else Statements: When I Finally Got It"
>
> dev.to/sameerqaisar17/if-else-stat...
>
> Why this one? Because I almost didn't publish it. I spent 3 days second-guessing whether a beginner should even be writing about Python. The formatting broke 6 times. I almost gave up twice.
>
> But I hit publish anyway. And then I wrote two more articles after it. That first one isn't my best writing — but it's the one that proved I could actually do this.
>
> Thanks for doing this. Reading through the comments to find hidden gems now

---

> **Carlo Gino Catapang** · 2026-09-13T09:20:30Z　
> Got back into writing. dev.to/codegino/add-ai-search-to-e...

---

> **EffessDev** · 2026-09-13T09:39:53Z　
> I think it's this one:
>
>  ESP-IDF Bluetooth LE (BLE) Beginner Tutorial
>
>  EffessDev
>
>  EffessDev
>
>  EffessDev
>
>  Follow
>
>  Aug 28
>
>  ESP-IDF Bluetooth LE (BLE) Beginner Tutorial
>
>  #tutorial
>  #iot
>  #esp32
>  #education
>
>  15 reactions
>
>  Comments
>
>  Add Comment
>
>  9 min read
>
> That probably took the longest to write. Did you really mean that you will read every single one of them? I would never do that. Too risky.

---

> **Giorgi Kobaidze** · 2026-09-19T07:39:02Z　
> Solid tutorial. The pacing works well, you build the program up piece by piece instead of dropping a finished file on the reader, and the short asides explaining macros and error codes fit naturally without derailing the flow. The UUID section I think is the highlight.
>
> The one thing I'd add is a bit on what happens after the phone disconnects, since that's usually where a first BLE project stops behaving as expected.

---

> **EffessDev** · 2026-09-19T08:21:20Z　
> Thank you so much :) I thought you gave up because of this many comments🤝

---

> **Giorgi Kobaidze** · 2026-09-19T08:30:34Z　
> Never! 😄 I'm getting this done one way or another! A promise is a promise.

---

> **Yusuke kimura** · 2026-09-13T15:29:45Z　
> About Long-Term Collaboration (Remote, Part-Time)
>
> I am a software developer with over 8 years of experience.
>
> now I am looking for collabortor to assist.
>
> If you're responsible, eager to learn, and interested in working with international clients,
>
>  I'd be happy to hear from you.
>
> -What You'll Get :
>
>  Fixed monthly pay (Performance bonuses for strong English communication)
>
>  Flexible schedule.
>
> Requirements :
>
>  -A laptop or desktop computer
>
>  -Reliability and good communication (Ability to communicate in English)
>
> How to apply?
>
>  Send me a direct message including your location and language.
>
> -Perfect for junior developers, or anyone who works hard!
>
> thank

---

> **Giorgi Kobaidze** · 2026-09-13T15:55:22Z　
> Wrong post, buddy. But I appreciate your effort!
>
> Anything actually related to this post by any chance?

---

> **James Carter Kula** · 2026-09-15T20:19:35Z　
> 🤝U.S. Business Partnership Opportunity🤝
>
> 🚩
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> 💬ThomasWilson881992 @ 0utl00k dot com🤝
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Dylan Scott Mickelson** · 2026-09-13T16:15:49Z　
> Creating Adaptive Flutter Screens and Widgets
>
>  Dylan Scott Mickelson
>
>  Dylan Scott Mickelson
>
>  Dylan Scott Mickelson
>
>  Follow
>
>  Sep 12
>
>  Creating Adaptive Flutter Screens and Widgets
>
>  #flutter
>  #dart
>  #opensource
>  #uidesign
>
>  Comments
>
>  1 comment
>
>  5 min read

---

> **CitronBrick** · 2026-09-13T19:30:12Z　
> ES5 Class based React Components
>
>  CitronBrick
>
>  CitronBrick
>
>  CitronBrick
>
>  Follow
>
>  Jun 13 '22
>
>  ES5 Class based React Components
>
>  #react
>  #ie11
>  #tutorial
>
>  8 reactions
>
>  Comments
>
>  Add Comment
>
>  2 min read
>
> This article on creating ES5 (Internet Explorer compatible) React Class based components, is still the only one of its kind on the web, that I could find.
>
> There is a Ruby introduction for JavaScript developers article, that I have been preparing for a while. Hope to post it soon.

---

> **Gagandeep Singh Ahuja** · 2026-09-14T03:42:31Z　
> I guess this comment thread is blowing up. I am also taking this as an opportunity to share the database building series titled as building SaarDB.
>
> Background: I was always curious to understand database internals a little more than any other technology basis my interactions with it early in my career and during my undergrad. Started reading few books but didn't understand the concepts deeply. As my career progressed, I started exploring multiple things but the databases understanding remained shallow. I knew that the only way to understand these concepts deeply is to build a database on my own.
>
> But with the AI era, I didn't want my agent to build the database, I wanted to do it myself. I wanted to utilise it as a reviewer of my approach and provide suggestions wherever I am stuck. My process is by taking small steps towards it, I majorly spend time on this only on weekends, hence the progress is slow, but progress indeed.
>
> Happy and grateful that I still get to do this deep-work (atleast, how I feel) in my free time.
>
> Sharing the part 1 blog and github repo here:
>
>  Building SaarDB, Part 1: Write-Ahead Log (WAL)
>
>  Gagandeep Singh Ahuja
>
>  Gagandeep Singh Ahuja
>
>  Gagandeep Singh Ahuja
>
>  Follow
>
>  Jul 4
>
>  Building SaarDB, Part 1: Write-Ahead Log (WAL)
>
>  #computerscience
>  #database
>  #go
>  #tutorial
>
>  23 reactions
>
>  Comments
>
>  1 comment
>
>  12 min read
>
>  gagandeepahuja09
>  /
>  saardb
>
>  SaarDB is a first-principles database in Go, built to make storage, indexing, transactions, and SQL execution feel intuitive.
>
> SaarDB
>
> Database internals, explained by building them.
>
> SaarDB is a first-principles database project in Go, built to make storage, indexing, transactions, and SQL execution feel intuitive.
>
> Why This Exists
>
> SaarDB is built to make the "magic" under the hood of databases easier to understand by implementing the core pieces from first principles: write-ahead logging, in-memory indexing, SSTables, compaction, transactions, and a small SQL layer.
>
> This is a learning project, not a production database. The goal is to make the internals understandable by building them one layer at a time.
>
> Architecture
>
> The current system is centered around an LSM-style storage engine:
>
> Writes:
> REPL / SQL -> WAL -> in-memory map -> SSTable flush -> compaction
>
> Reads:
> in-memory map -> newest SSTable -> older SSTables
>
> At a high level:
>
> -
> WAL gives crash recovery through append-only writes.
>
> -
> In-memory map keeps recent writes fast to read.
>
> -
> SSTables persist sorted data to disk.
>
> -
> Compaction merges…
>
>  View on GitHub

---

> **James Carter Kula** · 2026-09-15T20:15:14Z　
> U.S. Business Partnership Opportunity
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> ThomasWilson881992 @ 0utl00k dot com
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Giorgi Kobaidze** · 2026-09-19T08:15:33Z　
> Well-structured post. Letting each problem motivate the next piece, volatility, then write ordering, then record framing, then partial writes, then corruption, then fsync makes the design feel inevitable rather than arbitrary. That's hard to pull off in a storage-engine writeup.
>
> Two things it got me thinking about:
>
> The write-order section is the cache-aside ordering rule almost word for word, and the reasoning transfers cleanly: durable store first, cache second, because a stale cache is recoverable while an acknowledged write that doesn't exist isn't. Nice to see the same argument show up a layer down.
>
> On the duplication, I assume Part 2 handles it through LSM compaction, but my first instinct was a periodic garbage collector over the log. The catch is that it can't delete in place, since punching holes in the file puts you straight back into random I/O. So you'd roll the log into segments, rewrite frozen ones into fresh files keeping only the latest value per key, then swap and drop the originals, with tombstones so deletes survive the rewrite. Curious which way SaarDB goes.
>
> Looking forward to Part 2.

---

> **Well Center** · 2026-09-14T08:47:37Z　
> How to Choose the Right Cleanser for Your Skin Type
>
> Summer Skincare Routine For Oily Skin in Hot Weather: A Complete Guide
>
> Best Face Serums for Dark Spots and Hyperpigmentation That Actually Work (2026)
>
> Best Suitable Serums for Skin in Summer ( Complete Guide 2026 )
>
> Best Serum for Glowing Skin in Summer
>
> Best Permanent Skin Whitening Serum: 11 Powerful Picks for Dark Spots
>
> Best Face Serums for Glowing Skin That Actually Work (2026 Guide)
>
> Best Serum for Oily Skin and Dark Spots – Dermatologist Recommended
>
> 8 Best Serums for Oily Skin That Actually Work in Pakistan
>
> Best Facial Serum for Oily Skin Pakistan

---

> **Well Center** · 2026-09-14T08:47:42Z　
> Pocket Pussy for Men Sex Toy in Pakistan
>
> Shop Premium Butt Plugs In Pakistan
>
> Comfort Fit Male Chastity Cage Sex Toy
>
> Inverted Chastity Cage Sex Toy for Men
>
> Male Sex Doll Toy in Pakistan
>
> Adjustable Male Chastity Belt Cock Cage
>
> 10 PCS BDSM Bondage Kit for Beginners
>
> Massive Girth Realistic Dildo
>
> 8 PCS BDSM Bondage Kit for Beginners
>
> inflatable sex furniture toy in Pakistan
>
> Male Chastity Cage with Elastic Belt

---

> **Domenico Tenace** · 2026-09-14T09:35:19Z　
> Recently, I’d say this is the post I’m most proud of: it didn’t receive much praise, but my writing has matured over time to reach this point.
>
> What’s more, I’ve written about a subject that’s very special to me 🚀
>
>  Google AI Studio: The Playground Every Developer Should Know About 🎮
>
>  Domenico Tenace
>
>  Domenico Tenace
>
>  Domenico Tenace
>
>  Follow
>
>  for Playful Programming
>
>  Jun 5
>
>  Google AI Studio: The Playground Every Developer Should Know About 🎮
>
>  #ai
>  #programming
>  #google
>  #learngoogleaistudio
>
>  8 reactions
>
>  Comments
>
>  2 comments
>
>  6 min read

---

> **Peter Vivo** · 2026-09-14T09:45:18Z　
> I'am proud to present a mordor-project ( and mordorjs ) file format ( 1d programming language )
>
> The whole of story can be found in this three post.
>
> dev.to/pengeszikra/mdjs-mordorjs-1mon
>
> dev.to/pengeszikra/mcm-mordor-coff...
>
> dev.to/pengeszikra/a-game-for-the-...
>
> w t f w
> e h u e
> l e t
> c u s p
> o d r c r
> m i e r e
> e s e u s
>  t w e
> i o w e n
> n p h t
>  i i i .
>  c n
>  i
>  s
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Giorgi Kobaidze** · 2026-09-19T07:23:46Z　
> Alright, congratulations sir, that thing just broke my mind 😄 In a good way though. I've never ever seen anything like that.🤔

---

> **Alexey** · 2026-09-14T11:13:16Z　
> dev.to/fanatchipsovchitos19/agent-...
>
> I work on AI safety—specifically within the financial sector—and this article best reflects my view on how AI security architecture should be built.

---

> **Pooyan Razian** · 2026-09-14T11:38:39Z　
> It's not "just" the article, but I've built this tool and an article about it, and I'd be happy to get feedback: dev.to/prazian/make-dependency-upd...
>
> This tool scans every package manager in your repo, in one run, across every path in a monorepo, not just the root. Every change lands in a pull request that is labeled breaking or non-breaking based on the actual version jump, not just the mode you ran it in.
>
> If you don't trust it, you are not forced to share a token with it; you can pass the output to the official GitHub Action to create a PR based on it. You can find examples in the repo: github.com/yanovian/update-depende...

---

> **Abhishek Kumar Dutta** · 2026-09-14T11:58:04Z　
> My first article: dev.to/abhishekdutta619/why-your-c...

---

> **Prince Panchani** · 2026-09-14T13:13:09Z　
> dev.to/prince_panchani_f971a20ec/i...
>
> My pick..!

---

> **Dani Shemesh** · 2026-09-14T13:26:03Z　
> New here, I wrote a series about how to design Agentic development workflows
>
> dev.to/dani_shemesh/designing-agen...

---

> **4thwithme** · 2026-09-14T15:45:04Z　
> This one ;)
>
> dev.to/4thwithme/ab-testing-the-st...

---

> **Dhruv Jani** · 2026-09-14T16:18:39Z　
> Sir, this is it. Open it when you get time. Have A Great Day!
>
>  The Stack Nobody Picks Might Be the One That Picks You
>
>  Readers debate underrated tech stacks
>
>  Dhruv Jani
>
>  Dhruv Jani
>
>  Dhruv Jani
>
>  Follow
>
>  Sep 1
>
>  The Stack Nobody Picks Might Be the One That Picks You
>
>  #discuss
>  #csharp
>  #devjournal
>  #career
>
>  73 reactions
>
>  Picked as gem
>
>  Picked as gem by you
>
>  Comments
>
>  64 comments
>
>  5 min read

---

> **Giorgi Kobaidze** · 2026-09-15T20:03:41Z　
> What a great post, seriously! And you know what? I'm a .NET developer. C# has been my primary language for 10 years now.
>
> Would I pick a different language or framework if I could go back 10 years?
>
> Absolutely NOT!
>
> .NET is so beautifully crafted, and I feel sorry for people who still think C# is an ugly Java rip-off that only runs on Windows. Come on, guys, what year is this? .NET is fully cross-platform and packed with so many great features that even I get overwhelmed sometimes.
>
> Sure, it has its downsides, especially for people coming from other language backgrounds, but so does every language.
>
> As for popularity, it's still doing well. Check the Stack Overflow Developer Surveys, and you'll see C# consistently among the top languages. Honestly, though, even if it weren't popular, it wouldn't change much for me. As long as there are enough jobs out there, you only need one.
>
> And with .NET, you can build pretty much anything:
>
> Web apps? - Suit yourself.
>
> Desktop apps? - Absolutely.
>
> Games? - Hell yeah.
>
> Mobile apps? - No problemo.
>
> Back-end services? - For sure.
>
> Learn one language, and you can build almost anything. Tell me that's not cool!
>
> I'm actually planning to write a separate article on this topic, but a few others are already waiting in the queue, so it'll have to wait its turn.
>
> Thanks for sharing this amazing write-up!

---

> **Dhruv Jani** · 2026-09-16T00:22:09Z　
> Thanks for the reply, Sir. And I never knew you were a .NET developer, that's cool, its just that in my country there's kind of saturation where jobs are less than people graduating with CS degrees and where I live .NET is popular as in companies, not among DEV groups or college friends. One of the reasons why I picked .NET.
>
> Also, I'm still in final year and my training would start at start of the next year. I'd be glad if you could give me some advice.
>
> Thanks for the read and this detailed write up. Have A Great Day!😄

---

> **Giorgi Kobaidze** · 2026-09-16T04:36:51Z　
> Well, I can only give you a general advice:
>
> Coding skills are still valuable, focus on them, but take advantage of AI as well. Learn how to use it effectively, how to ask questions, how to get what you want out of it.
>
> And code (even with AI) as much as you physically can, because this is the only way engineering can be practices effectively.
>
> Good luck! 🙏

---

> **Dhruv Jani** · 2026-09-16T07:41:42Z　
> Thanks very much! Have A Great Day!🙏

---

> **Giorgi Kobaidze** · 2026-09-16T09:19:31Z　
> Likewise!🫡

---

> **James Carter Kula** · 2026-09-15T20:11:37Z　
> U.S. Business Partnership Opportunity
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> ThomasWilson881992 @ 0utl00k dot com
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Tariq Davis** · 2026-09-14T16:24:26Z　
> This is my best work so far. It’s pretty vulnerable for me, but I hope it brings some awareness to AI from a less common perspective, or at least expresses it in a way people might not have considered before.
>
>  Two Ways People Go With AI. Both Are Traps.
>
>  Tariq Davis
>
>  Tariq Davis
>
>  Tariq Davis
>
>  Follow
>
>  Sep 7
>
>  Two Ways People Go With AI. Both Are Traps.
>
>  #ai
>  #writing
>  #mentalhealth
>  #productivity
>
>  Comments
>
>  Add Comment
>
>  8 min read

---

> **Paulo Henrique** · 2026-09-14T18:07:40Z　
> This one. I don't know why it got so few views dev.to/phalkmin/generative-ai-is-a...

---

> **Giorgi Kobaidze** · 2026-09-14T18:49:41Z　
> This absolutely deserves much more views and reactions.
>
> Really enjoyed this write-up. The metaphor does real work instead of just sitting in the title, and "retries are only cheap on the invoice" is the part that'll stick with me. Everyone argues price per generation and nobody counts the human judgment stacked on top, which is the one thing you can't parallelize.
>
> One thing to clarify
>
> You say early on that better prompts improve your odds. But if prompting moves the odds, the pulls aren't really independent and that's the part the title rests on. Feels like there's a soft pity system in there after all.
>
> Thanks for sharing!👏

---

> **CitronBrick** · 2026-09-15T17:23:32Z　
> You can embed your Dev.to articles in Dev.to using
>
> {%embed dev.to %}
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> It gives a better visual appeal.

---

> **Gaurang** · 2026-09-14T18:54:52Z　
> Do you really understand interfaces?
>
>  Gaurang
>
>  Gaurang
>
>  Gaurang
>
>  Follow
>
>  Mar 15 '20
>
>  Do you really understand interfaces?
>
>  #java
>  #oop
>  #beginners
>  #codenewbie
>
>  42 reactions
>
>  Comments
>
>  17 comments
>
>  8 min read
>
> A look back at my first published piece, written entirely from scratch before the age of AI. I spent over a month fine-tuning every detail and even handled the cover design myself. It ended up getting a great response from readers at that time.

---

> **Giorgi Kobaidze** · 2026-09-19T08:40:18Z　
> Fun read, and a good use of the algorithm as a vehicle for explaining Haskell syntax rather than the other way round.
>
> Coming from C#, the same shape falls out of LINQ almost unchanged:
>
> static IEnumerable Qs(IReadOnlyList xs) where T : IComparable =>
>  xs.Count == 0
>  ? Enumerable.Empty()
>  : Qs(xs.Skip(1).Where(a => a.CompareTo(xs[0]) <= 0).ToList())
>  .Append(xs[0])
>  .Concat(Qs(xs.Skip(1).Where(a => a.CompareTo(xs[0]) > 0).ToList()));
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> Same trade-off as well: reads nicely, allocates constantly.

---

> **Gaurang** · 2026-09-19T15:41:58Z　
> Ughh... It seems you've replied to the wrong comment.
>
> This is probably the comment it's for:
>
>  Comment on Show Me the Article You're Most Proud Of And I'll Read Every Single One of Them
>
>  Caleb Weeks
>  Sep 11
>
>  This is my first post on DEV. I did not expect to have a lot of readers for my first post, but it's my most read by far. I think maybe DEV promotes first posts?
>
> dev.to/sethcalebweeks/haskell-quic...

---

> **Giorgi Kobaidze** · 2026-09-19T15:47:13Z　
> Oh yeah, my bad! Thanks! I'll read yours next! 🙏

---

> **Mārtiņš Veiss** · 2026-09-14T20:16:22Z　
> this one, as it serves as a warning for others and to warn a community
>
> dev.to/mrveiss/the-one-you-reporte...

---

> **Orvi Das** · 2026-09-14T21:34:26Z　
> I think this one is my personal favourite.
>
>  Tool Use in LLMs: What It Actually Means for Production Systems
>
>  Orvi Das
>
>  Orvi Das
>
>  Orvi Das
>
>  Follow
>
>  Aug 5
>
>  Tool Use in LLMs: What It Actually Means for Production Systems
>
>  #llmfunctioncalling
>  #tooluse
>  #aiagents
>  #honeycomb
>
>  5 reactions
>
>  Comments
>
>  6 comments
>
>  7 min read

---

> **Sal Parvez | ML Systems** · 2026-09-14T23:21:48Z　
> MVE: The Balance in MVP
>
>  Sal Parvez | ML Systems
>
>  Sal Parvez | ML Systems
>
>  Sal Parvez | ML Systems
>
>  Follow
>
>  Sep 14
>
>  MVE: The Balance in MVP
>
>  #startup
>  #ai
>  #architecture
>  #systemdesign
>
>  Comments
>
>  Add Comment
>
>  4 min read
>
> Mine is this one. MVP means two things in American English, Most Valuable Player and Minimum Viable Product, and they pull apart. The piece names the balance, MVE, Minimum Viable Expense: the smallest spend that still works and returns more than once. It is special because the rule came from a roof: cut the ring-shank nail instead of pulling it and you keep both the rafter and the sheet. That trade turned out to be the budget rule my seven AI agents needed too. Honest label, as in the piece: the deconstruction loop is modeled and has not been run on a house yet.

---

> **Damian Dixon** · 2026-09-15T02:17:13Z　
> dev.to/kilawattcloud/four-real-x40...

---

> **Son Hoang** · 2026-09-15T06:18:06Z　
> dev.to/hoangson/we-planted-180-bug...
>
> it ain't much but it's honest work

---

> **Sergiy Yevtushenko** · 2026-09-15T07:19:25Z　
> dev.to/siy/softwares-second-free-l...

---

> **Ahmad Atiq** · 2026-09-15T07:37:50Z　
> One article I’m proud of is this guide on an early baby milestone: “When Do Babies Clap?” I wanted to make it simple for parents to understand when clapping typically develops, what to expect, and how babies learn this skill through interaction and imitation.
>
> I’d love to hear what you think of it, especially if you have suggestions for making developmental milestone guides more useful for parents.

---

> **Ahmad Atiq** · 2026-09-15T07:38:25Z　
> One article I’m proud of is this guide on an early baby milestone: “When Do Babies Clap?” I wanted to make it simple for parents to understand when clapping typically develops, what to expect, and how babies learn this skill through interaction and imitation.
>
> I’d love to hear what you think of it, especially if you have suggestions for making developmental milestone guides more useful for parents.

---

> **Secret Toys** · 2026-09-15T08:04:33Z　
> Online Toys - Shop Your Desired Sex Toys in Pakistan
>
> Female Vibrators Toys Online Pakistan - Online Toys
>
> Dildos Toys For Men Online Pakistan - Online Toys
>
> Butt Plugs Toys For Women Online Pakistan
>
> Sex Dolls For Men Online Pakistan - Online Toys
>
> Chastity Cage For Men Device - Online Toys
>
> Penis Sleeve Dildo For Men Online Pakistan
>
> Pocket Pussy Toys For Men Device - Online Toys
>
> BDSM Toys For Women Online Pakistan
>
> Sex Sofa For Couple Toys Online Pakistan

---

> **Secret Toys** · 2026-09-15T08:04:41Z　
> How to Choose the Right Cleanser for Your Skin Type
>
> Summer Skincare Routine For Oily Skin in Hot Weather: A Complete Guide
>
> Best Face Serums for Dark Spots and Hyperpigmentation That Actually Work (2026)
>
> Best Suitable Serums for Skin in Summer ( Complete Guide 2026 )
>
> Best Serum for Glowing Skin in Summer
>
> Best Permanent Skin Whitening Serum: 11 Powerful Picks for Dark Spots
>
> Best Face Serums for Glowing Skin That Actually Work (2026 Guide)
>
> Best Serum for Oily Skin and Dark Spots – Dermatologist Recommended
>
> 8 Best Serums for Oily Skin That Actually Work in Pakistan
>
> Best Facial Serum for Oily Skin Pakistan

---

> **Shwetha** · 2026-09-15T08:26:03Z　
> Love this initiative! I'm very on and off with blogging but this one I posted on metadata recently was really useful imo -
>
>  Fixing your site's metadata: a practical checklist
>
>  Shwetha
>
>  Shwetha
>
>  Shwetha
>
>  Follow
>
>  Aug 6
>
>  Fixing your site's metadata: a practical checklist
>
>  #webdev
>  #seo
>  #metadata
>
>  18 reactions
>
>  Comments
>
>  6 comments
>
>  6 min read

---

> **Giorgi Kobaidze** · 2026-09-19T08:52:03Z　
> This is so important to keep in mind. I've been there too and it's painful to see the preview of your project doing funny things in different websites/apps.
>
> Thanks for the practical guide.🙏

---

> **Harsh Sengar** · 2026-09-15T09:11:47Z　
> My first and only, inspiration to share with others
>
>  Why Your D365 F&O Automation Breaks: The Hidden Logic Behind TargetId and RootId
>
>  Harsh Sengar
>
>  Harsh Sengar
>
>  Harsh Sengar
>
>  Follow
>
>  Sep 15
>
>  Why Your D365 F&O Automation Breaks: The Hidden Logic Behind TargetId and RootId
>
>  #dynamics365
>  #webdev
>  #testing
>  #automation
>
>  Comments
>
>  Add Comment
>
>  4 min read

---

> **Marco** · 2026-09-15T09:28:16Z　
> Love this idea, Giorgi. I’ll pick this one:
>
> I wrote a test for prompt injection. It passed while the attack worked.
>
> dev.to/mk023/i-wrote-a-test-for-pr...
>
> I’m probably most proud of it because the experiment changed the way I think about testing, not just prompt injection.
>
> I had a security test that was green while the attack it was supposed to prevent still worked. That forced me to ask a much more uncomfortable question: what property is this assertion actually proving?
>
> From there I ended up exploring falsifiability, negative controls, mutation testing, runtime evidence, and the difference between a test name that claims something and an assertion that actually demonstrates it.
>
> The idea I keep coming back to from that article is:
>
> a test name is a claim about the world, and the assertion is the evidence.
>
> It also started some of the most interesting discussions I’ve had on DEV around verification, residual state, observability and even predicate drift.
>
> So yes, this would definitely be my one. 😄🔍
>
> Really curious to hear what you think when you get to it.

---

> **Giorgi Kobaidze** · 2026-09-19T09:37:17Z　
> Great read, Marco! Thanks for sharing!
>
> The name-as-claim framing is the part worth keeping. A test that exercises real code and asserts the wrong property is worse than a missing one, because the name is what someone reads when deciding the area is already covered.
>
> Since you verified the fix by reverting the defence by hand, it might be worth wiring that up as a standing chec, mutmut or cosmic-ray does the same thing across the suite automatically, and the surviving mutants are a running list of assertions that aren't watching anything. Doing it manually catches the case you thought to break, the tool catches the ones you didn't.

---

> **liesliy** · 2026-09-15T09:45:35Z　
> This is very a interesting idea.

---

> **Giorgi Kobaidze** · 2026-09-15T19:12:31Z　
> Thank you! Feel free to share your work!

---

> **Imam Hossain** · 2026-09-15T10:46:26Z　
> Great insights! We also discussed custom ERP & SaaS architecture here: dev.to/imam_hossain_8d3eeaa7b931/h...

---

> **Dimitrios Desyllas** · 2026-09-15T12:59:08Z　
> I feel like this article make me the direction I want to follow professionally:
>
> dev.to/pcmagas/how-to-make-a-batch...
>
> But I am unsuire whether these types of article have a meaning in 2026.

---

> **James Carter Kula** · 2026-09-15T20:20:03Z　
> 🤝U.S. Business Partnership Opportunity🤝
>
> 🚩
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> 💬ThomasWilson881992 @ 0utl00k dot com🤝
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Cédric Hervet, Ph.D.** · 2026-09-15T13:07:05Z　
> Why the hard part of route optimization is the modeling, not the algorithm
>
>  Hidden business rules break routing projects
>
>  Cédric Hervet, Ph.D.
>
>  Cédric Hervet, Ph.D.
>
>  Cédric Hervet, Ph.D.
>
>  Follow
>
>  Sep 15
>
>  Why the hard part of route optimization is the modeling, not the algorithm
>
>  #api
>  #computerscience
>  #algorithms
>  #software
>
>  9 reactions
>
>  Comments
>
>  7 comments
>
>  7 min read
>
> Taking a chance with my very first post here, so this feels like a fitting place to drop it.
>
> It's about something I've seen fail quietly for ten years in route optimization: everyone benchmarks the algorithm, but almost every failed project I've seen died in modeling, not solving. Writing it down forced me to actually name the distinction between "can this rule be expressed at all" and "did someone state it correctly", which I'd been treating as one problem for way too long.
>
> Would genuinely love some honest feedback, especially since it's my first one here 🙏

---

> **Giorgi Kobaidze** · 2026-09-19T09:13:17Z　
> The three-layer split is the useful part here, and it generalizes well past routing, the rule nobody wrote down is the same failure mode in any rules-driven system.
>
> The case I'd focus on is the third one: a primitive exists but the mapping isn't obvious, so the developer builds a workaround outside the model. That one reads as a documentation problem rather than an expressivity problem. A cookbook mapping named business rules to primitive compositions would close more of the gap than more primitives would, and it's a lot cheaper to ship.

---

> **DevOps Daily** · 2026-09-15T13:29:05Z　
> This one here is good:
>
>  Practice Linux, Docker and kubectl in Your Browser, No VM Required
>
>  DevOps Daily
>
>  DevOps Daily
>
>  DevOps Daily
>
>  Follow
>
>  Aug 28
>
>  Practice Linux, Docker and kubectl in Your Browser, No VM Required
>
>  #linux
>  #docker
>  #kubernetes
>  #beginners
>
>  23 reactions
>
>  Comments
>
>  1 comment
>
>  5 min read

---

> **Amritpal Singh** · 2026-09-15T17:01:16Z　
> Link to my interesting RAG article: My RAG system's refusal threshold was having no effect. I only found out because I measured it.
>
> Please leave any comments!

---

> **CitronBrick** · 2026-09-15T17:26:39Z　
> You can embed your Dev.to articles in Dev.to using
>
> {%embed dev.to %}
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> It gives a better visual appeal.

---

> **Azalea** · 2026-09-15T17:09:02Z　
> I really like the idea of asking for the article we’re most proud of rather than the one with the most views or reactions.
>
> There’s a big difference between a post that performs well and one that stays with you as a writer. Sometimes the piece you value most is the one where you finally explained something you had struggled with yourself, documented a lesson you learned the hard way, or simply wrote something that sounds like you.
>
> Those are often the articles I find most interesting to read, too. Metrics tell us what got attention; the author’s choice tells us what meant something to them. That makes this a much more interesting way to discover good writing on DEV.
>
> Looking forward to going through some of the submissions here.

---

> **Giorgi Kobaidze** · 2026-09-15T18:57:13Z　
> Totally agree! Likes only tell part of the story, since so much depends on timing, the audience and sometimes luck. My most-liked article definitely isn't my favorite. The ones I treasure most are the ones tied to special memories. When a piece carries a moment like that, it becomes special in its own way, no matter the numbers.
>
> By the way, I'd love to read your favorite. Would you share it?

---

> **Forrester Terry** · 2026-09-15T17:38:48Z　
> This is one just posted:
>
>  26 Ways to Use Coding Agents for Non-Coding Tasks
>
>  Forrester Terry
>
>  Forrester Terry
>
>  Forrester Terry
>
>  Follow
>
>  Sep 15
>
>  26 Ways to Use Coding Agents for Non-Coding Tasks
>
>  #ai
>  #agents
>  #productivity
>  #operations
>
>  Comments
>
>  Add Comment
>
>  14 min read
>
> I am actually pretty proud of this one, and hoping people will find it interesting or give them ideas on how they can use their a.i. agents for more things outside of the standard coding and reporting. Thanks for offering to check other folks stuff out.

---

> **James Carter Kula** · 2026-09-15T20:10:50Z　
> U.S. Business Partnership Opportunity
>
> We’re a Japan-based software development team looking to build a long-term partnership with a reliable U.S.-based professional.
>
> Our team handles the technical side—from development and testing to project delivery. We’re looking for a U.S. partner who can help with client communication, business coordination, and developing new opportunities in the U.S. market.
>
> This is a revenue-sharing partnership, not a traditional employment position. Partners can receive 30–35% of the agreed revenue/profit share, depending on the project and responsibilities.
>
> If you’re interested in technology, freelancing, or building a side business and would like to learn more, send me a DM. I can provide the details, expectations, and example project structure.
>
> ThomasWilson881992 @ 0utl00k dot com
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode

---

> **Kornel Varga** · 2026-09-16T09:34:26Z　
> The piece I'm proudest of isn't the one with the most reactions — it's the one where I finally wrote the before/after rewrite patterns I actually use when a cold outreach draft sounds like spam:
>
> dev.to/kornel_varga_62cb594bf3fd/p...
>
> It's special to me because it's short, concrete, and stealable — two full before/after examples plus the structure, not another "just personalize more" pep talk. Feedback welcome if anything feels thin or unclear.

---

> **Marco Sbragi** · 2026-09-17T05:17:59Z　
> dev.to/marcobblk/is-history-repeat...
>
> This is the post that landed me in the top 7 this week. It isn’t a 100% technical post, but rather a snapshot of the developments I’ve witnessed over time—up to the present day—with the advent of AI. It reassures me that what developers really need right now is to understand where all of this is leading us.

---

> **Giorgi Kobaidze** · 2026-09-19T11:30:06Z　
> What an amazing article, one of the best I've read here in a while, hard to pick a single point to highlight, because each one lands perfectly.
>
> A few days ago, I wrote a short note the other day arguing that vibe coding isn't engineering. Most people agreed, which was encouraging. This post makes the same case from a sharper angle. Engineers aren't going anywhere, the job changes, but you can't build on non-deterministic output and completely rely on it. Nobody can rely on chaos and unpredictability. Producing the characters was never the point, that's like saying an F1 driver just turns a wheel and presses pedals.
>
> Speaking of F1 (which by the way is my favorite sport), the F1-engineers and trucks in medieval streets analogy made complete sense. Companies can't adopt a new standard the moment it ships, because stability is worth more to them than being current.

---

> **Marco Sbragi** · 2026-09-19T20:54:08Z　
> Thank you so much!
>
> Your extension of the F1 analogy is spot-on—saying engineering is just "producing characters" is like saying an F1 driver just "turns the wheel." It completely ignores strategy, system physics, and decision-making under pressure.
>
> As for vibe coding, I completely agree with you—and I'm a big F1 fan too! And now we have a very young Italian champion. Go Antonelli Go.

---

> **Giorgi Kobaidze** · 2026-09-19T21:27:59Z　
> As someone who absolutely loves everything about Italy, it makes me happy that there's such a great talent as Kimi. He's my new favorite driver already! 🏎️

---

> **Panagis Tzivras** · 2026-09-18T10:14:19Z　
> I wrote one recently that I'm particularly fond of.
>
> It's about an evacuation-routing model I built that confidently gave me an answer that was, let's say, geographically adventurous.
>
> Turns out the model wasn't the only problem. 😅
>
> I ended up documenting the six things that went wrong, from broken routing assumptions to a rather embarrassing minutes-vs-metres problem, and what I changed afterwards.
>
> Basically: I asked the map a question, it gave me an answer, and then I had to explain to it why it was wrong.
>
>  The Answer You Didn't Want: Fiskardo Evacuation Routing
>
>  Panagis Tzivras
>
>  Panagis Tzivras
>
>  Panagis Tzivras
>
>  Follow
>
>  Sep 17
>
>  The Answer You Didn't Want: Fiskardo Evacuation Routing
>
>  #opensource
>  #gis
>  #kefalonia
>  #opendata
>
>  Comments
>
>  Add Comment
>
>  4 min read

## 关联链接

- https://www.linkedin.com/in/giorgikobaidze/
- https://www.youtube.com/@Pilotronica
- https://x.com/georgekobaidze

## 导航

- 项目页：[[10-项目/github.com_1ac3d6f6]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
