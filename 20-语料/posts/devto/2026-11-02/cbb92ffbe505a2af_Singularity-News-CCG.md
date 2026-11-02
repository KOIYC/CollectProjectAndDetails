---
type: "corpus"
item_id: "cbb92ffbe505a2af"
title: "Singularity News :: CCG"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/pengeszikra/singularity-news-ccg-5ejk"
project_url: "https://codepen.io/editor/Omrega/pen/01a18f75-6d17-700c-8003-cd60c5253ed5"
author: "Peter Vivo"
published_at: "2026-10-31T02:18:22Z"
captured_at: "2026-11-02T09:41:23+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-10-31"
tags:
  - 语料
  - devto
  - devchallenge
  - hf26challenge
  - gamedev
  - showdev
metrics: {"reactions": 40, "comments": 12, "reading_time": 4}
comments_count: 12
comments_total: 12
discovered_via: "devto:showdev"
---

# Singularity News :: CCG

> [!info] 一句话导读
> This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/pengeszikra/singularity-news-ccg-5ejk>
> 指标：reactions=40 · 评论=12 · reading_time=4
> 作者：Peter Vivo　|　发布：2026-10-31T02:18:22Z
> 项目链接：<https://codepen.io/editor/Omrega/pen/01a18f75-6d17-700c-8003-cd60c5253ed5>
> 采集：2026-11-02T09:41:23+08:00　|　id：`cbb92ffbe505a2af`

## 正文

*This is a submission for the [Hacktoberfest Open-Source AI Challenge Week 4: Ghost in the Machine](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)*

## What I Built
<!-- What does it do, and how did you interpret the theme? What inspired it? -->
> The Singularity News editorial team is pleased to announce that, to help everyone prepare for the upcoming events, they are trying to share all the knowledge gathered from interviews with carefully selected subjects in a lighthearted and interactive format. At the same time, they firmly reject any accusations that including the Halloween target audience had any negative influence on the outcome. *- Mr. Slop*

![Haunted Terminal](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/wq2ix5f2mufl39p6wn7b.png)

Unfortunately, I have to say that Halloween has lost quite a bit of its shine in the light of the future looming over our heads. So for the final week, I created this CCG = Collective Card Game.I borrowed the card game system from the [Flogons](https://dev.to/pengeszikra/javascript-great-again-the-voice-of-void-5fp6). I didn't have time to fully develop the game in that project, but now I did. The CSS-based 3D rendering introduced there came in extremely handy, along with the pure HTML concept, resulting in a no-build development approach.

I think the game speaks for itself, and since it's a PWA, it can also be installed on mobile phones.

I also thought of those who don't like learning the rules of a new card game. Well, for them there's the `Auto:on` feature. By activating it, you can basically sit back and watch the game play itself like a movie.

no online multiplayer yet – the 4- and 7-player tables are played against bots

But the main point is that, throughout the game, you can interview every single card. And I'll just reveal that the final outcome was also created with some serious AI assistance.

I think that's enough for now.

The entire backstory and the characters — who, of course, have absolutely nothing to do with any real or fictional individuals — come from the world of my Singularity News feed.

For example, the Halloween target audience.

> Keep reading and share your comment! [SN::0001](https://dev.to/pengeszikra/singularity-news-28p6) |> [SN::0010](https://dev.to/pengeszikra/singularity-news-0010-nhn) |> [SN::0011](https://dev.to/pengeszikra/singularity-news-0011-1ai0)

![Halloween charactes of Singularity News word](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/l4d71vl32qlww9vpbzzo.png)

## Demo
<!-- Share a deployed link or a video demo. -->
https://singularity-news-ccg.vercel.app/

{% embed https://codepen.io/editor/Omrega/pen/01a18f75-6d17-700c-8003-cd60c5253ed5 %}

## Code
<!-- Show us the code!  You can embed a GitHub repo directly into your post. -->
https://github.com/Pengeszikra/singularity-news-ccg

> This moment is the **SCARIEST** part of development!

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/pvbcwmta950j7npxt6qx.png)

When I noticed that Claude had based it on one of the articles in my Pure HTML series, I realized it had taken the concept so seriously that it even embedded the images directly into `index.html`.

## How I Built It
<!-- Which open-source AI did you use (open-weight models, agent harnesses, frameworks, local inference), and how is your project built around it? -->

**Gemma** – Gemma 4 (`gemma-4-26b-a4b-it`, via the Gemini API) and  gpt-oss-120b (on Groq) was used. The whole build process is documented in PROMPTS.md – every prompt I gave the agent, in the original Hungarian.

## Why Does Open Innovation Matter?
<!-- Why does open innovation matter for what you built?  What did it make possible that a closed API wouldn't? -->
Open-weight models give me freedom: the same prompts run on Gemma 4 or gpt-oss-120b today, and later I can move to a local model to save tokens and money, without rewriting the game.

## My Agent Session
<!-- Optional, but judges love it.  Save your session with DevRelay and embed it with the agent_session tag (see the challenge page), or link to it. -->
[PROMPTS.md](https://github.com/Pengeszikra/singularity-news-ccg/blob/main/PROMPTS.md)

## The Spirit of It
<!-- Optional, but this is where you can make your post stand out.  Did it give someone chills, bring back a memory, or keep a story alive?  Show us the moment it landed.  If not, remove this section. -->
The whole development process once again reminded me of what I wrote in my [Vibe Archeologist](https://dev.to/pengeszikra/vibe-archeologist-from-z80-assembly-to-an-1859-mudbrick-house-and-beyond-46n5) article. I dug up solutions I had written almost two years ago, and by relying on today's [slop coding](https://dev.to/pengeszikra/slop-coding-the-vibe-archeologist-strikes-again-35df) techniques, I was able to implement them confidently and at an incredible speed.

**Pure HTML + No Build System forever!!**

And finally, I was able to develop the entire program from the director's chair, resulting in a game that can actually be played from beginning to end and always has a few surprises in store.

## Prize Categories

- **Gemma** – Gemma 4 (`gemma-4-26b-a4b-it`, via the Gemini API) is the primary model of the game: it writes Mr. Slop's news ticker, the character interviews, the intro spoken by the first flipped card, and the final epilogue article built from your collected characters. gpt-oss-120b (on Groq) is only a fallback and can be selected manually with the in-game AI switch.

Thanks for watching!

<!-- Thanks for participating! -->

## 评论（12/12）

> **Harun - solo dev ** · 2026-10-31T03:44:01Z　
> "Pure HTML + No Build System forever!!" 🙌
>
> As a 12-year-old dev building entirely on a $150 Android phone, I feel this mantra in my soul. Bloat is the enemy, and constraints breed the most creative solutions.
>
> The "Vibe Archeologist" concept is brilliant, and the way you leveraged Gemma 4 and gpt-oss-120b to dynamically generate Mr. Slop's news ticker and character interviews is incredibly clever. It’s a perfect example of using AI not just to write boilerplate, but to create a genuinely interactive, living experience (the "Auto:on" movie mode is a fantastic touch for accessibility, too).
>
> This is a super inspiring submission for the Hacktoberfest challenge. It’s a great reminder that sometimes the most powerful "stack" is just raw HTML, CSS, and a clear vision.
>
> Quick question: since you mentioned gpt-oss-120b is a manual fallback, did you find the latency or token costs significantly different between the two models when generating the in-game character interviews?
>
> Amazing work, Peter! 🐯☁️

---

> **nyaomaru** · 2026-10-31T06:33:15Z　
> This is a really fun card game! 😸
>
> I actually felt a little rich while playing it. 💰
>
> And I liked the idea that combining - and - turns into +. That’s such a fun little mechanic!

---

> **Odinaka Robert Nnamani** · 2026-10-31T13:43:43Z　
> Interviewing every card is the hook here. That turns a card game into a way to poke at the newsroom behind it.

---

> **Peter Vivo** · 2026-10-31T14:23:02Z　
> Thx! The last commit add save interview to markdown. Maybe some found interesting one.

---

> **Odinaka Robert Nnamani** · 2026-10-31T15:40:13Z　
> Saving the interviews to markdown makes them easy to keep around.

---

> **Niraj Khetre** · 2026-10-31T18:05:30Z　
> The 42 rule got me and the singularity actually rewriting the rules mid-run (rebels / survivors / zombies converting each other) is a really fun twist on the Math Match pairing. Also nice that the AI is optional and the game falls back to built-in texts when there's no key.
>
> I went through the repo and noticed a few things, hope it's useful:
>
> - About 1.1 MB of the 1.2 MB index.html is base64 JPEGs. Since the service worker loads the page network-first with no-store, every launch while online downloads all of it again. Moving the images into separate files would let the SW cache them, so repeat visits on mobile would be much lighter.
>
> - In api/ai.js the daily cap, the per-IP limit and the 6h news cache all live in memory. On Vercel each instance gets its own counters and they reset on cold starts. Fine for now, but if the post takes off, Vercel KV or Upstash would protect your API budget better.
>
> - The "Online AI" section of the README still says it runs on Groq / gpt-oss and the env table doesn't list GEMINI_API_KEY, while the next section says Gemma 4 is the default. Easy to trip over if someone deploys their own copy.
>
> - Tiny one: the inverse pair shows up as "INVERZIT" in the score popup, looks like a Hungarian leftover
>
> Curious which model writes the better Mr. Slop, Gemma 4 or gpt-oss?

---

> **Peter Vivo** · 2026-11-01T09:57:44Z　
> Lol Inverzit is still exsist in this program! Thanks for this details, this is a sci-fi material name of Flogon-Galaxy. Good to hear about this detail. Thank you I will get your points! But right now code freeze. If you would like to try your improvments, feel free to fork and try it! This is a open source stuff.

---

> **mp3sss** · 2026-11-01T01:52:41Z　
> The no-build pure-HTML approach with CSS 3D is a refreshing contrast to the usual bundler-heavy stack — for a card game it makes the PWA install story genuinely lightweight. The Auto:on watch-mode is a clever accessibility touch too. Curious how you keep the per-card interview content manageable without a build step: do you generate it into static data at authoring time, or fetch it from an API at runtime?

---

> **Peter Vivo** · 2026-11-01T10:09:25Z　
> You found a detailed answer in the source:
>
> github.com/Pengeszikra/singularity...
>
> the whole thruth is always on source! Developer may say anything!
>
> Mr. Slop style is so media hype driven.

---

> **Sina Rezaei** · 2026-11-01T06:39:03Z　
> The interview feature got me thinking about something interesting: how do you keep the AI-generated narrative consistent with the actual game state?
>
> For example, if a player interviews a card early in the game and later collects several characters that change the story, the final epilogue should reflect those events rather than inventing relationships or details that were never established.
>
> I'd probably keep the game state as the source of truth and pass a structured snapshot of collected characters, known facts, and relationships to the model. A JSON Schema for the response would also make it easier to validate the output before rendering it.
>
> That way, the AI gets room to be creative without becoming the authority on what actually happened in the game. That's where I think this kind of integration gets really interesting.

---

> **Peter Vivo** · 2026-11-01T10:04:47Z　
> My solution is very similar, characters answer for question according his/her and game current state. More or less similar way as you descripted there. But you mention give a great idea to me, where player are copy / upload interviews and final result to a Singularity News CCG :: Story reader app where you can read or even share your singularity story for take a look. Also becoause the whole app is a html page this means any one can use page translation to any language!

---

> **Sina Rezaei** · 2026-11-01T12:15:01Z　
> That's actually a nice direction. Making each playthrough portable means the story doesn't have to stay locked inside the game.
>
> One thing I'd consider is exporting more than just the final Markdown. A small versioned JSON package containing the ordered game events, interview transcripts, character IDs and generated epilogue would give the reader app enough context to reconstruct the story properly.
>
> For example, if a character was collected after an earlier interview, the reader could preserve that sequence instead of treating all the interviews as if they happened at the same point in the game. Keeping a schemaVersion in the export would also make older stories readable if the game evolves later.
>
> And I like your point about browser translation. I'd just preserve the original text and locale metadata alongside it, so readers can still distinguish the original narrative from a browser-translated version.
>
> That could turn the reader into a pretty interesting standalone archive of each player's experience.

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/l4d71vl32qlww9vpbzzo.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/pvbcwmta950j7npxt6qx.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/wq2ix5f2mufl39p6wn7b.png
- https://dev.to/challenges/hacktoberfest-week4-2026-10-26
- https://dev.to/pengeszikra/javascript-great-again-the-voice-of-void-5fp6
- https://dev.to/pengeszikra/singularity-news-0010-nhn
- https://dev.to/pengeszikra/singularity-news-0011-1ai0
- https://dev.to/pengeszikra/singularity-news-28p6
- https://dev.to/pengeszikra/slop-coding-the-vibe-archeologist-strikes-again-35df
- https://dev.to/pengeszikra/vibe-archeologist-from-z80-assembly-to-an-1859-mudbrick-house-and-beyond-46n5
- https://github.com/Pengeszikra/singularity-news-ccg
- https://github.com/Pengeszikra/singularity-news-ccg/blob/main/PROMPTS.md
- https://singularity-news-ccg.vercel.app/

## 导航

- 项目页：[[10-项目/codepen.io_b1c7cbcf]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
