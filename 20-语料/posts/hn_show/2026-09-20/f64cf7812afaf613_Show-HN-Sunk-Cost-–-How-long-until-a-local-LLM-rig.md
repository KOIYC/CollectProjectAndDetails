---
type: "corpus"
item_id: "f64cf7812afaf613"
title: "Show HN: Sunk Cost – How long until a local LLM rig pays for itself?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49706656"
project_url: "https://sunkcost.ai/"
author: "rlindsey123"
published_at: "2026-09-15T01:37:43Z"
captured_at: "2026-09-20T09:38:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_rlindsey123
  - story_49706656
  - show_hn
metrics: {"points": 46, "comments": 99, "engagement_velocity": 46}
comments_count: 99
comments_total: 99
discovered_via: "hn:show_hn:90d"
---

# Show HN: Sunk Cost – How long until a local LLM rig pays for itself?

> [!info] 一句话导读
> How long until local AI pays for itself? — Sunk Cost

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49706656>
> 指标：点赞=46 · 评论=99 · engagement_velocity=46
> 作者：rlindsey123　|　发布：2026-09-15T01:37:43Z
> 项目链接：<https://sunkcost.ai/>
> 采集：2026-09-20T09:38:52+08:00　|　id：`f64cf7812afaf613`

## 正文

How long until local AI pays for itself? — Sunk Cost

I’m looking at a

, the

of memory.

 About this machine $ What you paid

Assumptions you can change

 Electricity, $/kWh API speed, tok/s

 Assume API prices keep falling

How fast they fall

Annual fall in API prices

Where nothing has been measured, local speed is estimated as memory bandwidth ÷ bytes read per token × , and labelled as such. API speed only affects the time comparison.

How this is calculated

Capability ratings and the frontier comparison are a judgement call informed by public benchmarks, coarse on purpose. If one looks wrong, tell us.

# deepclause/pi-box

## 评论（99/99）

> **hyperhello** · 2026-09-15T02:33:16.000Z　
> I doubt it will ever be cost effective for the foreseeable future. The AI companies have astonishing amounts of compute and they’re effectively dumping it on the market.

---

> **jrflo** · 2026-09-15T02:33:33.000Z　
> 43 years to break even on Qwen 3.8 at 25% the speed of the API, lol. I like the idea of local models for really small tasks like automation/toolcalling, but it will probably never make sense for coding. I tried them and it was just excruciating compared to what you get for $100 a month from a subscription.

---

> **itake** · 2026-09-15T02:33:55.000Z　
> I have a home server running vibed applications. VPS host would cost $25/mo or $300/yr.Mac mini can also build iOS applications. I think if you’re a mobile dev, you can have concurrent builds for your agents instead of everyone waiting on a single machine to finish.

---

> **ProjectArcturis** · 2026-09-15T02:37:12.000Z　
> Local LLMs are not really about saving money, they're about autonomy. Choose the exact model you want, fine-tune it if you want, and no one can take it away from you.

---

> **mcone** · 2026-09-15T02:38:17.000Z　
> The idea that you need a new machine is pretty ridiculous. I bought a used HP Omen with a 3090 last month for $2k. 57t/s with Qwen 3.8.

---

> **txrx0000** · 2026-09-15T02:39:05.000Z　
> It pays off instantly, because OpenAI/Anthropic can no longer see what I'm doing and that's worth a lot of money to me. If I am offloading some of my thought processes to a machine, I want to own that machine. And if I finetune the model, I can gain access to parts of thought space that are cordoned off by OpenAI/Anthropic/Alibaba/whomever due to their "alignment" efforts (i.e. alignment to the AI company rather than me). Otherwise, it's like if someone else owns a part of my mind and has a backdoor into my mind.

---

> **shadowpho** · 2026-09-15T02:42:46.000Z　
> I like this calculator but it’s really wrong at least for dgx spark. I have one and I get 4x the tokens/s .

---

> **chasd00** · 2026-09-15T02:45:19.000Z　
> Not a fair comparison really. If you can run a model locally then you can somewhat train out the guardrails, censorship, and brand-safety. That has value a subscription does not.Idk about the quality of this setup but just pasting it here as an example.
> https://explainx.ai/blog/heretic-llm-abliteration-guide-2026

---

> **ThunderSizzle** · 2026-09-15T02:45:40.000Z　
> Claude Code is $100+ or else be constantly throttled. My usage on GHCP was gonna be $300+ a month.I paid $1350 and threw an R9700 in an existing machine. That's a 4 month pay off or so.Plus, I can feed it sensitive data all day and not be worried where it's going.

---

> **bix6** · 2026-09-15T02:47:22.000Z　
> Fun feature: can you show some sort of list of the best combos? Eg shortest payoff time for best capability in various situations.

---

> **QwenGlazer9000** · 2026-09-15T02:48:45.000Z　
> Yeah no it does not pay for itself just comparing to cloud. Not at these prices at least, people far richer than you or I buy these things wholesale, no scalper, bought a significant amount at cheaper prices, and are wired up the ass with VC money.The premium is not having your million dollar prize and career stolen by billionaires.

---

> **monksy** · 2026-09-15T02:53:14.000Z　
> I wish you could put different setups on here. I have a couple of A6000s on an AM5.

---

> **bpbp-mango** · 2026-09-15T02:55:24.000Z　
> can you add RTX cards too please? 5090 and 6000

---

> **gfody** · 2026-09-15T02:56:22.000Z　
> should throw in a tt-quietbox

---

> **serial_dev** · 2026-09-15T02:57:57.000Z　
> In the “The small print that isn't small” you describe all the disadvantages of running your models locally, but none of the advantages (just check the rest of the comment section for inspiration on that).

---

> **01HNNWZ0MV43FF** · 2026-09-15T02:58:16.000Z　
> I was just gonna throw a beefy Ryzen into an ATX chassis. I don't want to pay Mac prices

---

> **harhargange** · 2026-09-15T02:58:33.000Z　
> Also, i also use my gpu for rendering and learning and playing games.

---

> **Zetaphor** · 2026-09-15T03:01:07.000Z　
> This tells me that the max throughput for the models I'm running on my hardware is lower than it actually is. Please allow us to tweak all the variables instead of locking me in to whatever rate you found by searching

---

> **v3ss0n** · 2026-09-15T03:04:01.000Z　
> Besides from privacy:
> I already making twice now.you own the hardware and the price had doubled since i bought. Almost tripled.
> You missed the opportunity and i have 4 of those awesome machines. Cry on.I sell those to business who need local air gapped requirments and I make a lot more money!I can run the alliterated models where none of the service prvoider even dare to provide.THose benefits outweights a few K.And show me an api provider that allows me to run 10x agents concurrently for 5 days straights .

---

> **0xbadcafebee** · 2026-09-15T03:06:57.000Z　
> It pays for itself very quickly if you do 24/7 generation. Use an AI agent that orchestrates other agents working on many things at once constantly. If speed is a factor, you'd not buy a Macbook, you'd buy dual RTX 3090s. About the same price, but at least 6x faster than M5 Max. The benefit of constant generation is you can do a lot more research, coding sub-agents, experiments, etc in parallel when you're not "at work". You end up getting a lot more work done than if you only sit there babysitting sessions.

---

> **redox99** · 2026-09-15T03:10:51.000Z　
> The math is wrong, the tok/s is at least 2x that, at least with MTP and Q8 KV which you should always use. And the default tokens a day is ridiculously low at least for coding.Having said that, it will never pay for itself. A simpler more absolute math is, if I buy a Mac and use it to sell tokens on OpenRouter, will I make a profit? And the answer is no.

---

> **afarviral** · 2026-09-15T03:15:40.000Z　
> I want the autonomy but local models of the size I would have the means to host wouldn't be capable enough. What usecases tend to suit these smaller models that tend to produce incorrect or otherwise flawed responses often? Could they work for anomaly detection and what would a rough architecture look like?

---

> **rubyn00bie** · 2026-09-15T03:35:58.000Z　
> This is a bit weird because it automatically changes the model depending on the amount of VRAM available, and some of the smaller models are more expensive (presumably because they're being provided via OpenRouter by someone with some GPUs in a colo or smaller providers). It also doesn't allow changing the tokens per second (my 5090 can get like 75-130 tokens per second [assuming I can fit the model in RAM]); which, then results in woefully under-estimated limit on how many tokens a day I can consume.Some improvements that I think would make this more useful:1. Allow manually setting tokens per second, or as an alternative, let me jack up the number of tokens a day.2. A sort of backwards flow "if you want to run this, at X tokens per second, with Y context, you'd have to spend Z."3. Add support for configuring multiple RTX 6000 variants.When I was making heavy use of DeepSeekV4-pro I was burning somewhere around 1.5 billion tokens a month, and that was just using it in my free time on random projects. It was something like $24 at the time because of the initial discount/promo period. I don't think there's anyway in hell I could ever run that (on current hardware) for less money.I think the calculator shows from a purely financial standpoint what we all know... that yeah, it's definitely not worth it if money is your only concern. That (cost per token) will eventually change. Models will get better, more efficient, VRAM prices will come down, VRAM capacity will rocket upwards, and the economics of it all will change. It would just be really cool to have the calculator show me exactly how cheap they'd have to get for it to make sense.I need to finish up some work and make dinner, and if no one else beats me to it (anyone is welcome to) I'll ask Fable or Opus to knock that out.

---

> **kjshsh123** · 2026-09-15T03:49:01.000Z　
> On a purely monetary basis it probably never will.You're competing against companies that get tax breaks, locate themselves optimally, and have large economies of scale.Also, if it did, the hardware would be bought up, raising the price until there was no economic profit again.If you can find a unique application for it then maybe?

---

> **binary132** · 2026-09-15T10:18:59.000Z　
> Unstated key concept: “At today’s prices”

---

> **binary132** · 2026-09-15T10:56:39.000Z　
> The real question should be why anyone would voluntarily continue to spend money on a software service that costs as much as an expensive computer when they could just buy an (upgradeable) expensive computer and use it as much as they want, approximately forever.Imagine owning nothing and being happy.

---

> **gruez** · 2026-09-15T02:42:02.000Z　
> "If they are selling it for less than it cost to make, buy as much as you can."-- Warren Buffett

---

> **epistasis** · 2026-09-15T03:11:41.000Z　
> More than that, running hundreds of conversation streams at once is essentially the same cost as running a single conversation. And then you add on the secondary benefit of having the GPUs running nearly all the time rather than mostly idle...Local inference makes sense for speciality needs, or very small models. But if your model is bug enough to span GPUs its excessively wasteful to hoard those GPUs for yourself without piggybacking hundreds of other conversations on top of all that memory bandwidth and matrix multiplies.

---

> **ASalazarMX** · 2026-09-15T18:37:46.000Z　
> The comparison is about how many tokens you buy vs how much hardware you could buy with the same money. It's as saying "if you have rib eyes at Applebee's every day, how long until cooking your own rib eyes pays for itself".If you don't consume many of tokens, it will likely never pay for itself. If you do, though, it will have trade-offs, but you'll probably save money in the end.

---

> **rlindsey123** · 2026-09-15T02:58:09.000Z　
> Yeah it's surprising how long it would take to get back on those local models!

---

> **rlindsey123** · 2026-09-15T02:52:52.000Z　
> What models are you running on it? I'm also an iOS dev but I find I need more frontier models to get good quality code from it.

---

> **rlindsey123** · 2026-09-15T03:05:41.000Z　
> True - definitely agree!

---

> **rlindsey123** · 2026-09-15T02:54:18.000Z　
> I've not heard of others running HP with it. Hows much RAM do you have?

---

> **usernomdeguerre** · 2026-09-15T03:01:49.000Z　
> Agreed, I was also annoyed that the only params on the site were mac products. I run qwen 3.8 on a 12 year old asus and a 3090, 50tok/s. It's not even the only guest running on the box. For my usage profile (not running it 24/7) it's actually less expensive per-month than claude subscriptions.

---

> **redox99** · 2026-09-15T03:15:52.000Z　
> I'm so happy for the two used 3090s I bought for $500 each after Ethereum mining ended. I even saw them for like $430 at some point lol.

---

> **no-name-here** · 2026-09-15T02:46:18.000Z　
> You can't run recent openAI/Anthropic models locally anyway, so wouldn't a better comparison be a different provider running Qwen or similar model? As then you can also compare against the exact model you'd have locally and any different data privacy of that particular provider?

---

> **tyre** · 2026-09-15T02:53:12.000Z　
> I'm curious what people are sending to Claude that is so secret. Claude knows about my interior decorating, questions about light bulbs, curiosity about what the Galactic Empire was even trying to do, unpacking SCOTUS decisions, shoe trees, Fed inflation history, etc.What part of my brain is contained here? Sure, the conversations have back and forth (some have dozens of exchanges), but, like, that's not the secret to me. I don't think it can replicate me, and even if it could… okay?Are you worried they're going to target ads? That the government will steal something? What?Claude Code has information about my home server, but google or DDG would also have the broad strokes (torrents). I don't know. Maybe others are working on more sensitive things at home.

---

> **jrecyclebin** · 2026-09-15T02:54:04.000Z　
> This was my thought as well. I have a local model monitoring my finances and personal wiki - things I wouldn't want Claude to touch - and the Qwen 3.5 9b handles it all just perfectly.I also needed a new device anyway - and having this much system memory to run virtual machines has been amazing.Am paying subscriptions as well tho lol.

---

> **throwaway894345** · 2026-09-15T02:54:47.000Z　
> I’m very sympathetic to this point of view but I also can’t remotely afford the hardware required to get in the ballpark of Fable.

---

> **ChickeNES** · 2026-09-15T03:01:46.000Z　
> For me, I'm glad they train on my stuff if it improves the model. Hell, I've been using tons of muse-spark-1.3-contributor for this very reason (and because it's a decent model for a bargain basement price)

---

> **JKCalhoun** · 2026-09-15T11:15:19.000Z　
> Agree. As the meme/old-ad goes, "Running it on my own machine? Priceless!"Some of us get a weird thrill that we can actually do this. Mind-boggling time we live in.

---

> **cyanydeez** · 2026-09-15T14:17:38.000Z　
> Also, whatever your doing won't be at the whims of cloud providers; it won't fail because they decided to quantize your customer $ into a shittier model.Some how, _instability_ has gained valuable currency, so now we all act like the constant change of whatever is actually good for us. FOMO is just like breathing guys. That anxiety induced by tech culture constantly churning is healthy.In reality, these people churn for their own self worth and nothing else.

---

> **ASalazarMX** · 2026-09-15T18:28:37.000Z　
> > If I am offloading some of my thought processes to a machine"Offloading thought" sounds a lot better than "outsourcing thought", but the latter is what we're really doing. Offloading implies you thought it first and then gave it to the LLM, but we're only giving it the minimun so it can do most of the work in our place,

---

> **rlindsey123** · 2026-09-15T02:51:42.000Z　
> Aw very interesting! This is great feedback - what model are you running? I'm keen to do more crowdsourced data as time goes on.

---

> **ChickeNES** · 2026-09-15T02:49:23.000Z　
> > If you can run a model locally then you can somewhat train out the guardrails, censorship, and brand-safety.When does the average person actually need to do that?

---

> **xnx** · 2026-09-15T03:26:52.000Z　
> That can also be done with neoclouds.

---

> **no-name-here** · 2026-09-15T02:49:43.000Z　
> An R9700 has 32 GB RAM. Is your comparison against a similar size model? Or shouldn't you be comparing it against the cost of a hosted model matching the one you’re using locally?

---

> **rickydroll** · 2026-09-15T15:57:33.000Z　
> today, the r9700 is 1800$ at micro center :-( so payoff is around 2 months?

---

> **rlindsey123** · 2026-09-15T03:18:05.000Z　
> Good idea, pretty crude but it's up: https://sunkcost.ai/best/For each usage level, it lists the quickest pay-back in each capability class, with each model on its quickest machine and one click into the calculator to change the assumptions. Short version: at 1M tokens/day the best Sonnet-class option is Qwen3.8 27B on a Mac mini M6, 8.3 years. It only drops under a year if you're running agents at around 20M tokens/day.

---

> **rlindsey123** · 2026-09-15T02:53:37.000Z　
> haha 100%. We used to just rent our homes. Now we have to rent our intelligence

---

> **rlindsey123** · 2026-09-15T02:57:00.000Z　
> I'm keen to add a way for people to add community based reporting which would allow this. Would you want to see anything else on the dropdowns to be able to enter your data on?

---

> **rlindsey123** · 2026-09-15T03:59:13.000Z　
> Thanks for all the feedback. You can now enter your own measured tok/s for any machine and model.

---

> **ChickeNES** · 2026-09-15T03:11:27.000Z　
> > And show me an api provider that allows me to run 10x agents concurrently for 5 days straights .Any of them on a Max/Pro plan as long as you are smart about model selection? That's my main objection to local inference, I'd need a whole rack of GPUs to do as many things in parallel that I can do for $400 a month. I do plan on setting up some local inference hardware, but...RAM and GPU prices alone are $$$$

---

> **dumberquestions** · 2026-09-15T07:08:36.000Z　
> Yeah I'm surprised no one pointed this out, if something like persistent agents gets more popular/useful, the local option pays for itself surprisingly quickly.

---

> **taraindara** · 2026-09-15T02:54:58.000Z　
> Only caveat is you’re buying time. Not a physical good. It’s only worth what you’re able to get out of it in that time.

---

> **rlindsey123** · 2026-09-15T02:55:07.000Z　
> Is that a real quote? Golden if true

---

> **tyre** · 2026-09-15T03:00:54.000Z　
> For their current models, served directly from their infrastructure, they are profitable after training (which all present models are.)I don't know when we'll have an open equivalent to Fable, let alone whatever (insane) hardware you'd need to run it locally.

---

> **itake** · 2026-09-15T03:46:37.000Z　
> I only use frontier models to vibe code iOS apps, as I'm not an iOS developer. I haven't tried the local models post qwen coder 3.5 release for all the reasons.AFAIK, a limiter for iOS engineers (and AI agents) for concurrent feature development is the xcode environment and hardware limits. BE engineers can easily have 3 agents working on 3 different microservices (or gitwork trees), but iOS devs can basically only manage one version of the code at a time, due to externalized state (like derived data and bundle ids).

---

> **mcone** · 2026-09-15T03:00:03.000Z　
> This particular machine has 64GB, but the model is on the RTX 3090 with 24gb. Context is 156k with Pi mono.

---

> **txrx0000** · 2026-09-15T02:50:03.000Z　
> Technically true, but the delay between local and closed frontier is only a few months. And individual sovereignty / digital bodily integrity is almost priceless.

---

> **koito17** · 2026-09-15T02:56:06.000Z　
> GP's point is about "sending tokens to someone else's computer" versus "keeping the tokens locally". I think model capabilities are secondary.In May of this year, I was running qwen3.6:35b-a3b on my MacBook (bought in 2024). Obviously not as fast as, say, running a model on Cerebras, but a year ago it wasn't really feasible to have a local model running on my 2024 laptop with vision support. (Concretely, I was passing apartment diagram pictures to Qwen and making it compare different apartments for which ones would feel the most spacious while optimizing for initial moving costs and other factors.)This was back in May and I wouldn't be surprised if there have been significant improvements since then.Overall, I think it's fair to compare a workflow like "use llama.cpp locally to upload some pictures and ask questions" to "open the ChatGPT app, upload pictures from your phone, and ask questions". Sure, you can't run a model like GPT-5.4 locally, but the model is mostly an implementation detail here. What a user will care about is: "when I go with the llama.cpp option, am I getting useful information from my conversations?"

---

> **v3ss0n** · 2026-09-15T03:05:36.000Z　
> You haven't tried DeekSeek v4 or GLM 5.3 or Qwen 3.8 Next?You are missing out a lot.Try that with Hermes or Opencode or Deekseek Harness , even Qwen 3.8 27b works really well for that kind of that.I just ask it to install windows as a vm on my linux and install vs Community 2019 on it , and then build a legacy vb 2019 project on it. and sleepWhen i wake up :It installs Qemu , setup a vm , inside vm download and install windows 10 on its own , clicking next next next as needed , typing in things , writing powershell , python scripts , that run automatically after install by baking into CD that includes ssh server , reboot , it logins into ssh , trigger pythons script that continue installation of vs 2019 community , which includes a driver that click the installation steps , installs nuget , install all depedencies and then build the project into exe after i woke up.That is with 100% pure local AI .

---

> **poincareball** · 2026-09-15T02:53:41.000Z　
> Tristan Buckmaster found out the hard way.

---

> **octoberfranklin** · 2026-09-15T02:56:09.000Z　
> I'm curious what people are sending to Claude that is so secret.The proof to the Navier-Stokes problem.

---

> **truncate** · 2026-09-15T02:56:57.000Z　
> >> what people are sending to Claude that is so secretIts the same point used against privacy. What's so secret you are doing that you need privacy. I think in the end, its about privacy and not trusting these model companies with your data. Facebook manipulated people behaviors with all the data they had, no reason AI companies wont someday decide to do that same, and they have far more intimate knowledge.When it comes to coding, I also don't like the idea of them taking my money and potentially at same time potentially using as dataset generator.

---

> **cle** · 2026-09-15T03:17:59.000Z　
> Anthropic's goal is to commoditize intelligence. People who use their brains / intelligence for competitive advantage might not want to contribute training data for that goal.

---

> **AdieuToLogic** · 2026-09-15T03:22:15.000Z　
> > I'm curious what people are sending to Claude that is so secret.When Claude is used in a professional setting, any or all of: Proprietary intellectual property (a.k.a. system code)
>  PII[0] of the employee, customers, or both
>  HIPAA[1] data known to a system
>  Internal communications not meant to be publicized
>  Sensitive data, such as SSH keys and the like
>
> Pretty much anything on a machine which uses Anthropic/OpenAI native tools is a candidate to be compromised really.0 - https://en.wikipedia.org/wiki/Personal_data1 - https://en.wikipedia.org/wiki/Health_Insurance_Portability_a...

---

> **juiceland** · 2026-09-15T03:36:30.000Z　
> Are you willing to bet that your lack of imagination for exploitation is precisely that of several multibillion dollar companies?

---

> **catchnear4321** · 2026-09-15T02:59:51.000Z　
> Your last line is what drives the point home, though.Local isn’t strictly about NOT lab. It’s rapidly becoming apples (though not just macs) to oranges to compare the to.Which is why the premise is silly. To be underwater it would need to be a real comparison. It’s not, and the claude fartifact doesn’t make it so.

---

> **shadowpho** · 2026-09-15T18:24:59.000Z　
> The big three :)Qwen3.8-flash-next
> Deepseek4-0731-flash
> Glm5.3The latest unsloth llama.cpp has a lot of nice features that runs them faster than before.I’ll have to double check which one runs how fast, but it’s generally 20-40 t/s. (And infil is fast but not sure how that’s counted)

---

> **jerf** · 2026-09-15T02:57:19.000Z　
> We've already seen frontier models refuse to answer almost any question that touches on computer security and be very likely to kick out biology and chemistry questions even if they aren't all that close to breeding dangerous viruses or making explosives.I expect this is only going to get worse. "Censorship" isn't just going to be about who you vote for and which political party the model will say nice things about and which it is more likely to say bad things about. It's going to become about whether the hoi polloi are allowed to have effective AIs at all. Like the 1990s internet, AI has outrun a lot of power structures but that is not going to continue indefinitely.

---

> **beachy** · 2026-09-15T02:57:55.000Z　
> I just got some kind of cyber alert from Claude and was forced back down to Opus while I was trying to connect to a battery I own via bluetooth.So I can certainly understand why someone would want the guardrails gone.

---

> **kees99** · 2026-09-15T03:02:46.000Z　
> "Need" might be a bit too strong, but I do want overly obnoxious guardrails not to stand in the way.Case in point, last week I was poking Opus 5 into writing me some RPi-pico firmware for driving a small e-paper screen. Font was built in right into C code as hex constants. Space being tight, I asked if there is some clever compression that could be applied. Claude thought for good 10 minutes, then guardrail kicked in telling me that was "cyber", and refused to continue.

---

> **ASalazarMX** · 2026-09-15T18:42:38.000Z　
> If you mean retraining, it's not even needed anymore. If you want the guardrails off, these days you just install LMStudio and download an abridged model. It's all GUI. The abridged models might have weird behavior in edge cases after the pruning, though.

---

> **dwb** · 2026-09-15T07:51:32.000Z　
> You should be comparing the value you get. If you get as much value from a local model as a hosted one, the size difference doesn’t matter.

---

> **ThunderSizzle** · 2026-09-16T10:58:15.000Z　
> Well, I don't see a value issue of using Qwen3.6 27B vs Sonnet 4.6 (not sure about 5 yet)I still have to use GHCP at work, and I self-host at home, and aside from the fact self-hosting also forces you to tinker, optimize, etc. - there's not a huge difference in my end result in end user results. I spent quite a bit of time trying to optimize llamacpp and compare 35b to 27b, etc. I don't compare models that much at work.I guess the other part of it is I didn't really know much about cheaper cloud models, but I was attracted to the idea of no longer renting against Claude code, etc. I figured if I could run something functionaly similar from my bedroom on a normal outlet, then all this talk about data centers needing to be built everywhere in the news cycle is obviously just plain stupidity and hype.It appears I'm using about 20.4/7.6 million in/out tokens a month, or on open router, about $20/month.That puts $1350 at a 5-6 year break even (thanks to cheap electricity), I guess. Beyond that, running on localhost as a nice feature of 0 no latency when doing rapid tool calling

---

> **ThunderSizzle** · 2026-09-16T10:25:05.000Z　
> Sadly. It's jumped $300-400 in 2-3 months time.I don't think I'm the only persona that did the math.

---

> **bix6** · 2026-09-15T04:07:16.000Z　
> That was fast!At 7 tokens/s (Mac mini) you max at 600k/day so you couldn’t hit those higher amounts like 4M where it says 2 year payback?

---

> **v3ss0n** · 2026-09-15T08:33:27.000Z　
> > I'd need a whole rack of GPUsno , all you need is one small DGXSPark with proper setup.

---

> **selectodude** · 2026-09-15T02:54:10.000Z　
> Local frontier costs a half million dollars to run locally in anything higher than basically ternary.

---

> **no-name-here** · 2026-09-15T03:02:26.000Z　
> Wouldn't the better comparison still be against an AI provider with better privacy controls, especially if that's what someone cares about (even if they don't care about whether they're comparing a 35 billion param model vs a x trillion param model)?

---

> **v3ss0n** · 2026-09-15T03:15:04.000Z　
> Deepseek 4 flash can run locally , and qwen 3.8-next-flash , they are already gpt 5.6 tier.

---

> **LargoLasskhyfv** · 2026-09-15T04:29:37.000Z　
> Regarding DeepSeek, which I also like very much, have you tried https://reasonix.io ?

---

> **ASalazarMX** · 2026-09-15T18:24:44.000Z　
> I've tried the latest Qwen, and without Internet, it still can go into an incoherent loop if you ask for, say, song lyrics. TBH the commercial models might do that too if not for their internal tooling.

---

> **utopcell** · 2026-09-15T03:12:58.000Z　
> I'm pretty sure they were sending a prompt for Claude to _find_ the Navier-Stokes proof, using ideas that have been publicly shared before online, but not necessarily used for the problem.

---

> **AdieuToLogic** · 2026-09-15T03:25:19.000Z　
> > Anthropic's goal is to commoditize intelligence.And Google's original goal was to organize the world's information.How did that turn out?

---

> **tyre** · 2026-09-15T07:00:56.000Z　
> Anthropic will sign BAAs. They are HIPAA compliant (we used them.)I understand people’s hesitation but the business agreements are different. The business risks of misusing HIPAA data is not only being banned from a massive enterprise market (last I checked, there were about 1.2m jobs related to claims billing and adjudication) and significant legal repercussions.Other companies like AWS also handle HIPAA data. Are we afraid they’re stealing it? I don’t believe it, nor that Anthropic is training on HIPAA data.OpenAI… I will never trust them.

---

> **ChickeNES** · 2026-09-15T03:03:04.000Z　
> So you want to remove valid safeguards? And stop misusing the word censorship.

---

> **ChickeNES** · 2026-09-15T03:04:31.000Z　
> Well I just applied to their cyber program, got accepted in two hours, haven't had that issue since. Ditto OpenAI. Why people treat these companies like sports teams instead of compute providers I have no idea, when I see underpriced compute, I take advantage of it.

---

> **ChickeNES** · 2026-09-15T03:07:04.000Z　
> Just apply to the cyber program? I got in in around 2 hours, and I'm just some hobby hacker, not some paid security consultant. It is a valid point though, I'm doing tons of systems and embedded stuff and was hitting the safe guards with Claude and Codex before getting into their cyber programs (hex REALLY triggered Claude in particular, which was amusing).

---

> **no-name-here** · 2026-09-15T11:54:34.000Z　
> >>> Claude Code is $100+ or else be constantly throttled>> Is your comparison against a similar size model? Or shouldn't you be comparing it against the cost of a hosted model matching the one you’re using locally?> You should be comparing the value you getBut the GP commenter specifically compared the cost of solutions such as Claude Code against a 32 GB model.If they are going to compare cost, they should compare to the cost of a hosted ~32 GB model.Or if privacy trumps everything for them, then just say that and don't bother comparing costs of incredibly disparate solutions, as Claude Code costing $100+ a month was a red herring if they're happy with 32 GB model output - they could have compared to a far cheaper option that matched their local model's quality.It would be like someone saying they were able to buy a bike to get to work, saving them $x million compared to buying a Bugatti. When really, if they're going to compare cost they should compare to a cheap car, or not bring up the cost of an expensive car at all if exercise trumps everything else for them.

---

> **ChickeNES** · 2026-09-16T18:56:58.000Z　
> You really don't understand how many agents I have running at once

---

> **txrx0000** · 2026-09-15T03:06:03.000Z　
> Okay, that's technically true again, but local mid-tier like Qwen3.8-27B is only a year behind the closed frontier. I'm personally willing to be behind by a year if it gives me mental sovereignty against the big AI companies. They are extremely misaligned with me.

---

> **koito17** · 2026-09-15T03:06:12.000Z　
> Users generally have no way to verify that a third-party provider, even if they advertise themselves as privacy-focused, will adhere to their own terms. This is similar to the issue of privacy-focused VPN providers that claim to not log user activity (and then end up leaking user activity). You can get proof of ~P, but rarely proof of P, and often times the proof of ~P is due to police raids, data breaches, etc., not something of the provider's volition.What you can possibly audit is probably data sovereignty. For instance, I would not be surprised if Mistral's customers demand concrete evidence that their data is held within the European Union. But that is a distinct issue from training on input tokens.

---

> **v3ss0n** · 2026-09-15T11:33:40.000Z　
> Bot? Care to explain any difference vs DSH / OpenCode / Hermes ?

---

> **bix6** · 2026-09-15T03:56:27.000Z　
> But are you pretty sure or actually sure?

---

> **jerf** · 2026-09-15T03:09:22.000Z　
> You asked a question. I gave you an answer. I seriously doubt that if you and I sat down together at a table and banged on this for an hour that we would come to the same definition of "valid". Ask 10 people, get 12 answers to that question. There's going to be a lot of motte & bailey in the next couple of years, where I just want an AI to answer questions about whether my code is vulnerable and people like you will be "Oh so you want an AI that can hack the Pentagon do you?" and it doesn't look like we're going to be seeing eye to eye on that one.

---

> **LargoLasskhyfv** · 2026-09-15T20:27:29.000Z　
> Notbot! Are you unable to read, or what? Just fkn install it, and see how smooth it integrates?

---

> **utopcell** · 2026-09-15T05:41:38.000Z　
> They obviously did not send the proof to Claude.

## 导航

- 项目页：[[10-项目/sunkcost.ai_78982575]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
