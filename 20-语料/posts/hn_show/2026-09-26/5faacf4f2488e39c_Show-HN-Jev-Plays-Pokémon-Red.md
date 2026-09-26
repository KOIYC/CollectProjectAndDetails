---
type: "corpus"
item_id: "5faacf4f2488e39c"
title: "Show HN: Jev Plays Pokémon Red"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49845172"
project_url: "https://jev-pokemon.vercel.app/"
author: "pancomplex"
published_at: "2026-09-25T14:28:07Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_pancomplex
  - story_49845172
  - show_hn
  - front_page
metrics: {"points": 153, "comments": 68, "engagement_velocity": 153}
comments_count: 68
comments_total: 68
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jev Plays Pokémon Red

> [!info] 一句话导读
> Hey HN! Wanted to share a fun project I've been hacking on. Given Jev can make decisions really fast (but not fast enough to play Doom yet sadly), I wanted to t…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49845172>
> 指标：点赞=153 · 评论=68 · engagement_velocity=153
> 作者：pancomplex　|　发布：2026-09-25T14:28:07Z
> 项目链接：<https://jev-pokemon.vercel.app/>
> 采集：2026-09-26T09:41:08+08:00　|　id：`5faacf4f2488e39c`

## 正文

Hey HN! Wanted to share a fun project I've been hacking on. Given Jev can make decisions really fast (but not fast enough to play Doom yet sadly), I wanted to try and push it to play a more complex game than Tetris. So I went with Pokémon.I've spent endless hours playing this game as a child so building this was a ton of fun.I open sourced everything in case you want to hack on it yourself here: https://github.com/christianmat/jev-pokemonThe game is being streamed live including the tokens and cost - hopefully we get all the badges and don't get stuck in a cave :)

## 评论（68/68）

> **rickintoplace** · 2026-09-25T14:47:19.000Z　
> That's actually fun to watch. Did you experiment with nicknaming before you turned it off? I'd be a little curious to see how it behaves.

---

> **testaccount28** · 2026-09-25T20:11:02.000Z　
> with such a fat harness, this is more like watching a walk thru play the game.

---

> **lwarfield** · 2026-09-25T20:15:26.000Z　
> Looking at the diagram in the gh repo, it looks like this is entirely jev. Are there any examples of people having a big model like Fable handle high level goals?

---

> **MitPitt** · 2026-09-25T20:16:13.000Z　
> This is kinda chill to have in the background. I wish there were livestreams showing live reasoning of top models which are currently trying to solve cancer or whatever. Imagine the pogs in chat when it does.

---

> **361994752** · 2026-09-25T20:16:15.000Z　
> watched it stuck at rocket hideout for 10 mins.... let me check 1hr later to see if it can find a way out

---

> **stusmall** · 2026-09-25T20:23:37.000Z　
> >but not fast enough to play Doom yet sadlyDid I miss something? I thought one of the demo videos was it doing pretty decent at the first level of Doom?

---

> **theturtletalks** · 2026-09-25T20:26:04.000Z　
> Is Frigade going to use Jev to do object detection?

---

> **dmitrygr** · 2026-09-25T20:28:29.000Z　
> Considering it just made Charizard forget its only fire-type move "Ember" to learn "Counter", I note no signs of intelligence.

---

> **stusmall** · 2026-09-25T20:32:52.000Z　
> This is so interesting to watch. For a couple minutes I was in awe of how quick and cheap it was. Then I saw just how bad the decision are and how it would get stuck in strange loops of going in and out of the same door to no end.This seems like a technology heading in the right direction but not quiet there yet. Excited for what they are cooking up but probably won't start building around it yet.

---

> **djhworld** · 2026-09-25T20:53:01.000Z　
> What's not clear to me on the video is whether jev is doing the button presses for controlling the character to move around.The "Jev calls" counter only seems to increment at junction points like battles, conversation prompts, menus etc.Is something else moving the character around?

---

> **avaer** · 2026-09-25T20:58:29.000Z　
> I wish jev took in images so we could do this generically for any game, without memhacks. I'm sure that's coming.You could front this with an image -> text model but that would be much lower quality vs latency, and the whole point of doing it with a decision model is remove the latency.Games are a really interesting testing ground for robotics; if we can solve game playing (incl 3d) we could embody "system one" intelligence into robots that have something emulating general reflexes without needing to fine tune.

---

> **zaik** · 2026-09-25T21:33:34.000Z　
> Seems like it got stuck on a Ghost enemy.

---

> **hummusFiend** · 2026-09-25T22:25:24.000Z　
> Great work!Super cool to see it do the whole game. I spent my fable budget building something similar this week but only drove it to Brock. I like the "current focus" framing too.

---

> **ac2u** · 2026-09-25T23:25:26.000Z　
> Cool project, comes with a little too much guidance in the harness though IMO (pathfinding, textual milestones etc). (The author is very upfront about this in their README though)I think if it was combined with a regular vLLM it could be really interesting, especially watching the reasoning logs.Bonus points if it was one of the latest open models that somehow had all prior training knowledge of Pokemon abliterated so it was reasoning as an intelligent persona that had no knowledge of even the concept of Pokemon.

---

> **dang** · 2026-09-25T23:43:32.000Z　
> Dare we have two Pokemon-playing-AI threads at the same time?Teaching a World Model to Play Pokemon - https://news.ycombinator.com/item?id=49849907

---

> **flockonus** · 2026-09-26T00:28:00.000Z　
> The decisions are quick, but look good as random w/ tons of back and forth.
> Are you at least feeding back some of its previous decisions on to state?

---

> **ViscountPenguin** · 2026-09-26T00:59:46.000Z　
> The choices Jev has here feel very railroady, it seems like something very significantly dumber could beat the game with these options.

---

> **dochaus** · 2026-09-26T01:14:12.000Z　
> He confirms what I long suspected, all you need is to cheese Charizard and flamethrower

---

> **bulatb** · 2026-09-26T01:19:54.000Z　
> Koga's guy tells Jev that "strength is not the key for Pokemon, it's strategy."Jev then wipes the whole gym with a single overleveled Charizard.Fitting and appropriate on many levels.

---

> **pancomplex** · 2026-09-25T14:53:29.000Z　
> Jev can't come up with original text, but I did consider giving it a list of hilarious names.

---

> **laszlokorte** · 2026-09-25T20:41:16.000Z　
> Yeah I would have expected it to only decide which button to press, not something abstract like the choice of "go east to lavender town" for the goal of "in lavender town, climb the pokemon tower"

---

> **staindk** · 2026-09-25T20:27:58.000Z　
> Hm wondering what a first pass optimal setup might be - jev for overworld navigation, escalate to sonnet for easy battles, opus for medium difficulty battles, and fable for gym bosses could probably have jev also manage all the escalation / de-escalation to different models.

---

> **pancomplex** · 2026-09-25T20:28:14.000Z　
> Frontier reasoning models do pretty well in Pokemon: https://github.com/benchflow-ai/pokemon-gymThe interesting thing here imo is the cost and latency. So far we're at 4 badges for less than $0.5

---

> **SeanAnderson** · 2026-09-25T20:43:08.000Z　
> I'm not sure if you're asking about whether using Fable makes playing the game possible or if you're just curious about Jev + LLM interactions.However, https://x.com/TynanSylvester/status/2096965749369720970 Astra was able to beat RimWorld. So LLMs are definitely able to drive these sorts of games to completion with their current abilities.

---

> **pancomplex** · 2026-09-25T20:20:24.000Z　
> People need to be live streaming their AI more!

---

> **tehnoslow** · 2026-09-25T20:25:49.000Z　
> Actually, yes, that would be at least interesting

---

> **someothherguyy** · 2026-09-25T22:20:59.000Z　
> then it would cost human lives, no more fun i made this thing with no real effort vibes

---

> **jumploops** · 2026-09-25T20:30:19.000Z　
> It’s currently stuck at an elevator and deciding to teach Pokemon various TMs and HMs instead of progressing… pretty hilarious!

---

> **pancomplex** · 2026-09-25T20:49:44.000Z　
> it made it through!

---

> **pancomplex** · 2026-09-25T20:29:16.000Z　
> In my experience it was too slow to do an FPS with 30 ticks per second reliably. It gets killed too fast.

---

> **pancomplex** · 2026-09-25T20:28:44.000Z　
> Working on it :)

---

> **pancomplex** · 2026-09-25T20:33:27.000Z　
> Rookie mistake clearly..

---

> **pancomplex** · 2026-09-25T20:44:36.000Z　
> Like others have mentioned in this post, I think a mix of models like Jev for simple stuff + a smarter reasoning model for more strategic thinking is the optimal solution. This experiment however is purely Jev. Which sometimes can be kinda dumb.

---

> **binlog** · 2026-09-25T20:46:54.000Z　
> This entire conversation around Jev seems weird to me. Like... we started from neural nets that could do basic decision making and classifications pretty well, then trained larger and larger language models to get to where we are now. Now suddenly everyone is going crazy because someone trained a smaller model that is adequate at making decisions? We already went through the "look this AI can play pokemon terribly" phase like a decade ago.

---

> **ralusek** · 2026-09-25T21:19:26.000Z　
> The exact message I sent my friend this morning:> the most interesting thing about this jev stuff> is that people are seemingly like> completely disinterested in how smart it actually is> I haven't even heard it mentioned a single time how it actually compares to other LLMs coming up with their own classifications. Just: it's fast and cheapAfter watching a few minutes of this it makes me think that maybe we should be a little more interested in how smart it is.

---

> **jbjbjbjb** · 2026-09-25T22:53:10.000Z　
> Jev is for single shot classification, not multi-step RL environments with delayed reward and explore/exploit. My guess is it would go through the door with high confidence every time unless you change the input to add the history.

---

> **pancomplex** · 2026-09-25T20:56:13.000Z　
> It's connected to the ROM of the actual game, so it can see a lot of things. It has multiple tools available, including being able to move to coordinates.All in the OSS repo if you wanna play around with it: https://github.com/christianmat/jev-pokemon

---

> **pancomplex** · 2026-09-25T22:04:19.000Z　
> Agreed this would be super cool and I do see that coming in the future. But Jev-level latency just isn't there yet with full images.

---

> **pancomplex** · 2026-09-25T22:56:50.000Z　
> Thank you! And interesting data point on Fable burning out on tokens so early.

---

> **JamesSwift** · 2026-09-25T20:29:45.000Z　
> Sure it can, just ask it for next char or "done" in a loop

---

> **IanCal** · 2026-09-25T20:30:42.000Z　
> Maybe letter by letter spelling?

---

> **pancomplex** · 2026-09-25T21:46:42.000Z　
> That was how I first implemented it. Jev sadly never left Pallet Town.

---

> **theturtletalks** · 2026-09-25T20:33:09.000Z　
> Nice. When I saw your connection to Frigade, I knew there was a connection haha

---

> **azan_** · 2026-09-25T20:58:55.000Z　
> Making decisions quickly, cheaply and without having to train your own model.

---

> **ford** · 2026-09-25T21:00:01.000Z　
> I agree it's overhyped, but the transition to a general purpose classifier (vs a narrow scope classifier) is new and noteworthy.Ie the famous "Hotdog" clip from Silicon Valley [0]https://www.youtube.com/watch?v=ACmydtFDTGs

---

> **c7b** · 2026-09-25T21:25:34.000Z　
> A pre-trained universal classifier that can replace specifically-trained ones would have been considered just as much science fiction in the 2010's as the capabilities of modern LLMs. I'm not sure Jev is actually there yet, but at least it sounds theoretically doable today.That being said, one thing having been unrealistic 10 years ago and just about possible today doesn't mean that it's going to change the world the same way another technically related, previously-impossible thing did. The Jev hype gives me a bit of the "you're still early to crypto" vibes of some later altcoins. I really like the idea, I think it's going to open up possibilities for using classifiers where we wouldn't or couldn't have trained one before. I'm crossing my fingers for an open weights version to drop. But it's still just a classifier, people have built similar things before Jev, the one thing that really stands out about it is their ability to generate hype.

---

> **osener** · 2026-09-25T22:27:54.000Z　
> It is impressive, but all the hype and fake demos are selling it as a model that is as smart as frontier reasoning LLMs in the decisions it makes yet much cheaper and much faster, which is not true.

---

> **gchamonlive** · 2026-09-25T22:47:50.000Z　
> For what it does, it classifies, orchestrates, operates and delegates tasks exceedingly well for its size and weight. It's ridiculously cheap and efficient, but if you can only see progress in terms of raw cognitive power then you'll surely miss how interesting this is.

---

> **solidasparagus** · 2026-09-25T22:50:23.000Z　
> The cheap, fast and smart-enough LLM space has been wildly neglected. Jev is one of the few players truly targeting that space. And for a lot of people it is the first time they are asking "what could I build if llms were interaction-speed fast?". The answers are cool, the problem is that Jev is not, I think, smart-enough yet to have that many applications, but it's smart enough that you can start to see what they will look like.

---

> **stusmall** · 2026-09-25T22:48:49.000Z　
> There is a lot of room for a lot of different models. For many use cases, intelligence beats out all.For me in my day job, having extremely fast low quality decision makers over noisy inputs is very valuable. I work in security and having something that can help triage alerts, classify items and group things together is extremely valuable. It doesn't need to be perfect. Just being able to take a set of inputs from deterministic tooling and to be make general priority classifications goes a long way on helping humans look at the most important items first.

---

> **johnsmith1840** · 2026-09-25T23:48:28.000Z　
> They know it's not. The company actually has or had public statements that they didn't like public benchmarks for comparison.My main wonder is the difference between it and having a small llm no thinking output a single number only as a choice. Isn't that nearly the same here?

---

> **raincole** · 2026-09-26T00:47:17.000Z　
> Because it's not that smart especially when you compare it to other LLMs. The top LLMs have completely change the baseline of being smart.

---

> **pancomplex** · 2026-09-25T23:06:42.000Z　
> This runs entirely on Jev as the only AI with a typescript harness that feeds it selective context.

---

> **fzysingularity** · 2026-09-26T00:52:14.000Z　
> We just did exactly this - added TypeSafe-compatible API (incl. websocket support) for various VLMs. Latency right now is <250ms, but will be able to get it to <150ms (p95).Take a look at a snake demo with streaming image inputs: https://x.com/spillai/status/2103630735425089957

---

> **pancomplex** · 2026-09-25T20:33:03.000Z　
> True!

---

> **pancomplex** · 2026-09-25T20:50:15.000Z　
> I just took your advice and added it to the list of Jev decisions. Watch it name its next Pokemon!

---

> **joshuat** · 2026-09-25T21:02:27.000Z　
> Math.random can make poor decisions quickly and cheaply

---

> **janalsncm** · 2026-09-25T22:41:01.000Z　
> Maybe noteworthy but definitely not new. The category of zero-shot classification has been around for a while.Example (2022):https://developers.openai.com/cookbook/examples/zero-shot_cl...

---

> **someothherguyy** · 2026-09-25T22:15:56.000Z　
> > but at least it sounds theoretically doable todaywhy

---

> **pancomplex** · 2026-09-25T22:35:12.000Z　
> Nothing fake here and fully open source if you wanna take a peek. It does make a bunch of mistakes, often. But it eventually recovers!https://github.com/christianmat/jev-pokemon

---

> **gchamonlive** · 2026-09-25T22:46:12.000Z　
> I think that misses the point of Jev being ridiculously efficient while maintaining adequate intelligence for automation tasks. We have to train our minds to filter out branding and marketing.

---

> **azan_** · 2026-09-25T21:11:59.000Z　
> Benchmark it against jev and you'll have your answer.

---

> **thornewolf** · 2026-09-25T22:41:20.000Z　
> We have a bad universal classifier now (via Jev). 0->1, one might say.A bad universal classifier does suggest a good one later. And that is exactly what I would call "theoretically doable"That said, I don't think that Jev is a magic breakthrough or anything. I think it is just a particularly good narrative with an easy way to try it out.

---

> **c7b** · 2026-09-25T23:45:53.000Z　
> LLMs are like lossy compression of ~all of written text ever produced, with useful recall. To the extent that the corpus contains labelled examples of the given classification task, it's not unreasonable to think that we'll be able to build a decoder for that, just like we already have a useful decoder for next-token prediction. Extend to image classification the same way we already have multimodal LLMs.

---

> **tehsauce** · 2026-09-25T23:47:48.000Z　
> For those curious how it works, it’s essentially a script that plays the game but uses jev as a source of rng to make it stochastic

---

> **zahlman** · 2026-09-25T22:28:21.000Z　
> I mean,> get stuck in strange loops of going in and out of the same door to no endMath.random is statistically unlikely to do this.

---

> **joshuat** · 2026-09-26T01:09:21.000Z　
> mathrandomplayspokemon.org

---

> **lukev** · 2026-09-26T01:33:59.000Z　
> Jev is interesting in that it's much cheaper and faster than a frontier LLM.But I've seen nothing to indicate that the upper bound on classification tasks of a Jev-like model can exceed a frontier LLM with reasoning tokens. That seems nearly impossible even in principle (since Jev-style models are still based on LLM pretraining).So while they're definitely on the Pareto frontier, which is valuable, they're at the "cheap" end of the spectrum more than the "good" end and I don't expect that to change.

## 关联链接

- https://github.com/christianmat/jev-pokemonThe

## 导航

- 项目页：[[10-项目/jev-pokemon.vercel.app_88351a4a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
