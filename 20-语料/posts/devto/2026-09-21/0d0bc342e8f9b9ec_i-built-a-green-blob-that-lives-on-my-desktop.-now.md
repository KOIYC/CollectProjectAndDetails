---
type: "corpus"
item_id: "0d0bc342e8f9b9ec"
title: "i built a green blob that lives on my desktop. now it has feelings."
source: "devto"
source_name: "dev.to"
url: "https://dev.to/mikachu/i-built-a-green-blob-that-lives-on-my-desktop-and-now-it-has-feelings-4pjd"
author: "Mika Flowers"
published_at: "2026-09-20T11:15:55Z"
captured_at: "2026-09-21T09:46:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - devto
  - showdev
  - python
  - linux
  - opensource
metrics: {"reactions": 36, "comments": 13, "reading_time": 6}
comments_count: 13
comments_total: 13
discovered_via: "devto:showdev"
---

# i built a green blob that lives on my desktop. now it has feelings.

> [!info] 一句话导读
> A quick disclaimer before we dive in: when I say "feelings," I mean state machines, bond progression, and interaction history — not an LLM. Mochi isn't running …

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/mikachu/i-built-a-green-blob-that-lives-on-my-desktop-and-now-it-has-feelings-4pjd>
> 指标：reactions=36 · 评论=13 · reading_time=6
> 作者：Mika Flowers　|　发布：2026-09-20T11:15:55Z
> 项目链接：—
> 采集：2026-09-21T09:46:38+08:00　|　id：`0d0bc342e8f9b9ec`

## 正文

> A quick disclaimer before we dive in: when I say "feelings," I mean state machines, bond progression, and interaction history — not an LLM. Mochi isn't running on any AI model, and there's no language model deciding how he reacts. Every "emotion" here is deterministic: state lifecycles, timers, and memory of past interactions, not inference. Just wanted to set that expectation up front. Carry on 🌱

- - -

I've been building a little green creature that lives on my Linux desktop.

**His name is Mochi.**
![mochi001](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/mq062p7o0r7qqbjb51w0.png)
*version 0.01 of mochi. laughable i know, but he's so cute!*

At first, the goal was honestly pretty simple: make blob move.

Then it became: make blob feel alive.

And apparently I've now reached: give blob a productivity system, emotional progression, snacks, and an alarming number of animations.

So... yeah. Mochi v0.3 happened. 🌱

![feeding mochi](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/yikk4mvnncmkunslu9kz.gif)

## The original idea was much smaller

Mochi started as a pixel-art desktop companion for Linux.

Python. GTK4. PyGObject. Cairo.

No cloud service. No account. No giant Electron window hiding somewhere in the background. Just a little creature hanging out on your desktop.

The early versions focused mostly on making that basic illusion work. Mochi could idle, blink, walk around, sleep, react when you clicked him, notice when you were typing, and occasionally respond to what was happening on the desktop.

And honestly, getting even that working reliably taught me way more about desktop development than I expected. Because the moment your cute blob can walk, sleep, be picked up, react to input, display UI, and independently trigger animations, you've accidentally created a state-management problem.

A surprisingly adorable state-management problem.

But v0.3 made me rethink what Mochi actually was.

![mochispin](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/63cvr1cpw91ohmv7xu6f.gif)

![mochi in pixelorama](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ry0l2qmb04v4ni5h1dap.png)

## I didn't want to build a Tamagotchi that makes you feel guilty

Once I started thinking about progression, the obvious direction was some kind of virtual-pet system.

Hunger. Health. Daily streaks. Meters slowly falling while you're away.

And I hated basically all of it.

I don't want opening my laptop after three difficult days to result in my desktop pet staring at me like:

mother. you have abandoned me. 😭

Software already asks enough from us. Mochi is supposed to make the desktop feel a little warmer, not become another notification demanding maintenance.

**So the design rule for v0.3 became:**

1. Care should create affection, not obligation.
2. Your bond with Mochi can grow. It doesn't decay because you went outside. There are no daily streaks. Mochi doesn't starve. Closing the application isn't a moral failure.
3. Progression exists mainly to unlock more personality, reactions, dialogue, animations, and tiny surprises.
That decision ended up shaping basically the entire release.

## Mochi has a bond system now

v0.3 introduces persistent bond progression.

The important word there is persistent. Mochi is slowly beginning to remember the relationship you've built with him instead of resetting emotionally every time the program starts.

Interactions can contribute to bond progress, and reaching new levels gives me somewhere to attach increasingly expressive behavior later.

Not stronger stats. Not "+5 Mochi damage."

Expression. Different reactions. Different little moments. More personality.

That feels much more appropriate for what this project is becoming.

And yes, there is a level-up animation. Because obviously there is. I have priorities.

![coding w/ mochi](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/8ho2ec5rjbc4n5q60c2x.png)

## You can feed him

This might be one of those features that exists primarily because watching Mochi eat something made me happy. And I am completely okay with that.

Feeding is a small interaction rather than the foundation of some constantly draining hunger mechanic. That's an important distinction.

I want you to interact with Mochi because it's cute and you want to. Not because a progress bar has been weaponized against you.

That sounds like I'm dramatically overthinking feeding a green pixel blob. I probably am. But tiny design decisions like this completely change how software feels to live with.

## I built an entire emote catalogue

![emote catologue](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/iz57bqw4hvxdinsq5yk3.gif)

This has become one of my favorite parts of the project. Mochi has been accumulating reactions. A lot of reactions.

Instead of treating those animations as random disconnected GIFs, I've been working toward an actual catalogue and state system that lets Mochi use them coherently.

The hard part isn't drawing an animation. The hard part is answering questions like:

- What happens if Mochi wants to emote while he's walking?
- What if you pick him up halfway through?
- What if he's sleeping?
- What happens when the animation finishes?
- What if an old timer fires after his state has already changed?
That's where this cute desktop pet quietly turned into a real software architecture problem.

Mochi now has explicit behavior/state ownership so higher-priority interactions can interrupt lower-priority ambient behavior without a dozen timers fighting over the sprite.

Which is a very serious sentence about a creature shaped approximately like a gumdrop.

## Mochi is becoming aware of what I'm doing

![mochi hacking away](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/utr8ge7p6cx23ig7o98j.gif)

This is the direction I'm probably most interested in long term. Mochi can react to broad desktop activity. If I'm spending time in a terminal, editor, browser, media app, or other recognized context, Mochi can behave differently.

But I've been deliberately strict about the privacy boundary.

Mochi does not need to know what I'm typing. He doesn't need every window title. He doesn't need filenames. He doesn't need a transcript of my desktop.

Instead, the system tries to reduce activity into tiny semantic signals. Something closer to:

```plaintext
terminal active
typing happening
media playing
user returned
```

instead of:

`here is everything Mika is currently doing`

I think that distinction is extremely important. A desktop companion should be able to feel aware without becoming desktop surveillance.

That principle is staying.

## Then I accidentally gave my desktop pet a Pomodoro timer

![mochi focus](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/amz3cop874puov940uc5.gif)

This is probably the feature that pushed Mochi furthest away from "desktop toy."

It's called Focus with Mochi. You can start a focus session, choose the focus and break lengths, select your rounds, enable gentle encouragement, and even use a rain soundscape.

While you work, Mochi works with you. Focus time contributes to your bond. Breaks don't. And — very intentionally — Mochi does not judge what you do during them.

I didn't want another hyper-optimized productivity system screaming about efficiency. The idea is much softer:

> I'm working for a little while. Mochi is here too.

That's it. And weirdly, I like that much more.

## The difficult part wasn't adding features

The biggest lesson from v0.3 has been that adding another feature to Mochi isn't particularly difficult anymore. Making every feature coexist is.

- A focus session needs to survive interactions.
- Feeding shouldn't break the state machine.
- Dragging Mochi around shouldn't leave an invisible window behind.
- A nameplate shouldn't steal mouse input.
- Sleeping shouldn't be accidentally cancelled because a UI opened.
- An old callback shouldn't wake up three seconds later and overwrite the state you're currently in.
And because Mochi runs as an actual desktop surface on Linux, I also have to care about things like:

Wayland. XWayland. GTK lifecycle behavior. Window positioning. Multiple monitors. Negative monitor coordinates. Input grabs. GLib timers. Shutdown cleanup.

Things I absolutely did not picture myself thinking about when I originally drew a green blob.

That has probably been my favorite part of the project. Mochi keeps creating excuses for me to learn systems I wouldn't otherwise touch.

## And I still don't want Mochi to become annoying

![mochi table flip](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/p54b3mu62z3iu5iaiiak.gif)

There's a temptation with something like this to maximize activity. More reactions. More popups. More dialogue. More notifications. More stuff.

I'm trying to resist that.

A good ambient companion needs to know when to shut up. Sometimes Mochi notices something and reacts. Sometimes he doesn't. Sometimes he just sits there.

That silence is part of the personality.

The goal isn't:

> LOOK HOW MANY FEATURES MY DESKTOP PET HAS.

It's:

> huh. it kinda feels like this little thing lives here.

That's the bar I'm chasing.

## What's next

v0.3 has ended up being a much bigger architectural step than I originally expected.

The bond system gives Mochi memory. The interaction system gives that bond meaning. The growing emote library gives him more ways to express it. Context awareness connects him to the desktop. And Focus with Mochi is my first experiment in making the companion genuinely useful without turning him into another productivity dashboard.

There is still a lot I want to explore:

- More meaningful bond milestones
- More contextual reactions
- Tiny unlockable behaviors
- Better dialogue
- More polish
- Probably several bugs caused by GTK doing something I was absolutely positive GTK would not do
You know. Software development.

But I'm really happy with the direction.

Mochi started as: what if there was a little guy on my desktop?

v0.3 is starting to answer the much more interesting question: what would make me actually care that he's there?

🌱

## 评论（13/13）

> **Giorgi Kobaidze** · 2026-09-20T11:33:33Z　
> That's such a cool idea. I've thought about something like this but I can't decide on the character. 😄
>
> One thing I'd like to know: how are the animations actually made? I spotted Pixelorama in one of the screenshots, are you drawing frames there and exporting sprite sheets? Curious how they get from the editor into Cairo.
>
> I'm planning to build something like this at some point to make my long coding sessions a bit more fun, so your experience would definitely be helpful.

---

> **Mika Flowers** · 2026-09-20T11:36:21Z　
> Yep! You spotted Pixelorama 😄 Most of Mochi’s animations start there. I draw the sprites/frames by hand, usually working at a really small native resolution, then export the individual PNG frames or a sprite sheet.
>
> On the code side, Mochi has an animation player that takes those frames, their timing, looping behavior, etc. and renders them through Cairo. So an animation is basically: draw frames → export → define the animation/timing → Mochi’s state system decides when to play it.
>
> I also use a little AI in the art workflow. I’ve been experimenting with PixelEngine for things like cleaning up animation ideas / generating a rough sequence, and then I go back in and redraw or fix frames manually so they actually match Mochi’s design and move consistently. It’s definitely more of a hybrid workflow than “type prompt → finished animation.”
>
> Funny side story: I actually ended up with a ton of PixelEngine credits because I found an exploit/bug in their credit system and reported it to them 😂 They gave me credits afterward, so now Mochi gets to benefit from my accidental security testing.
>
> The part that surprised me most is how much tiny timing changes matter. Holding one frame for 80ms vs 140ms can completely change whether an animation feels cute, snappy, heavy, sleepy, etc. That’s probably been one of my favorite things to learn while building this.
>
> And honestly, if you’re thinking about building one for your coding sessions, do it. Even a simple idle + blink + little reaction animation already gives the character a ridiculous amount of personality.

---

> **Mika Flowers** · 2026-09-20T11:37:42Z　
> Also, learning how much of a pain Wayland is 😂 Getting a little animated creature to sit transparently on the desktop, stay interactive, move around, and behave consistently across Linux setups has honestly been half the project. I thought I was building a cute blob and somehow ended up learning window management, compositors, input handling, GTK, and XWayland compatibility.

---

> **Giorgi Kobaidze** · 2026-09-20T11:52:25Z　
> That sounds like a lot of hard work, so when I finally make up my mind about what kind of character I want to create, I'd better set aside a solid amount of time for building it. Using an AI workflow is actually a great idea, especially for someone like me who's no animation genius 😄 Maybe I'll come back with a couple of questions if I really get stuck at something.
>
> And your funny story is really interesting, you should write more about that. Finding those kinds of bugs, and actually getting rewarded for it is a hell of an experience. So go ahead and write one of those "I don't wanna brag, but lemme brag about it..." articles 😂

---

> **Mika Flowers** · 2026-09-20T12:05:10Z　
> LOL okay, now I really do feel obligated to write the “I don’t wanna brag, but…” article 😂
>
> Seriously though, thank you, I really appreciate the kind words. Mochi has definitely been one of those projects where I keep stumbling into way more work than expected, but also way more learning than expected too. A lot of it has just been me making something weird, hitting bugs, figuring things out, and slowly shaping it into something real.
>
> And yes, if you end up building your own character, absolutely come back with questions. I’d be happy to share what I’ve learned and hopefully save you a little trial and error 😅
>
> Also, thank you to the community curators for the gem that genuinely made my morning 💚

---

> **Giorgi Kobaidze** · 2026-09-20T12:10:37Z　
> No problem, glad I did. It was so insightful, and it happened to make someone's morning, so it's a win-win situation. 😄
>
> Actually, I've just realized this is the first gem I've ever given out.
>
> Say hello to Mochi from me when he wakes up. 👋

---

> **Compound Labs** · 2026-09-20T12:13:20Z　
> GTK timeout callbacks can still run after Mochi has changed state, so an old callback can overwrite the sprite's current animation. A state-generation check at callback time makes that race testable.

---

> **Mika Flowers** · 2026-09-20T12:22:01Z　
> ohhh yeah, this is exactly the kind of weird little race condition I’ve been fighting with 😭 GTK is like “yep callback is still valid!” meanwhile Mochi has emotionally moved on to an entirely different state lol. Wayland + GTK have been keeping me humble since v0.1
>
> the state-generation check is actually such a good idea though. especially because it gives me a clean way to ignore stale callbacks and make the bug reproducible in tests instead of just staring at Mochi like “why did you do that”
>
> definitely stealing this for the next lifecycle pass, thank you 💚

---

> **StellarRealm** · 2026-09-20T13:22:36Z　
> I wanted to share an AI platform that I recently discovered and think may be interesting to you.
>
> It is available to contributors in several countries, including the US, UK, European countries, India, Brazil, Indonesia, and more.
>
> The platform may offer attractive earning opportunities, potentially reaching $10K+ per week, although actual earnings depend on the country and other circumstances.
>
> You don't need a specific skill set or specialized background to participate.
>
> If you would like more information, please contact me at:
>
> stellarrealmzone@gmail.com
>
> I'm available to discuss the opportunity and provide further details.
>
> Thanks for your time, and I look forward to hearing from you.

---

> **Jessica Doering** · 2026-09-20T15:52:21Z　
> This is so ridiculously cute, and I love that there’s actually a lot of thoughtful design behind it too. The whole idea of making the interactions feel affectionate instead of turning it into another thing you have to maintain is such a good call. I’ve been messing around with a tiny desktop creature idea myself, so this was especially fun to read. Also, I have a pixel art app called Gumdrop Studio with a little gumdrop logo, so “a creature shaped approximately like a gumdrop” made me laugh way harder than it probably should have lol. Seriously though, this is awesome!

---

> **Jamsun Sun** · 2026-09-20T16:07:17Z　
> This is such a fun project, but the state-management side is what really caught my attention. It’s impressive how a simple desktop pet turns into a real architecture challenge once you add animations, callbacks, context awareness, and Wayland support. Mochi is a great example of how small projects can teach you way more than expected.
>
> yazi stilleri

---

> **Hadil Ben Abdallah** · 2026-09-20T20:04:50Z　
> This is sweet 🥰 Good job!

---

> **Rylen Galloway** · 2026-09-21T00:53:47Z　
> cool, Could you maybe help me with some js I'm a new dev. Heres my latest post
>
> dev.to/rylen_galloway_5b15f8e262/p...

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/63cvr1cpw91ohmv7xu6f.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/8ho2ec5rjbc4n5q60c2x.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/amz3cop874puov940uc5.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/iz57bqw4hvxdinsq5yk3.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/mq062p7o0r7qqbjb51w0.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/p54b3mu62z3iu5iaiiak.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ry0l2qmb04v4ni5h1dap.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/utr8ge7p6cx23ig7o98j.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/yikk4mvnncmkunslu9kz.gif

## 导航

- 项目页：[[10-项目/i-built-a-green-blob-that-lives-on-my-desktop.-n_0d0bc342]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
