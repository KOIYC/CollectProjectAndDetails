---
type: "corpus"
item_id: "7c7e4e2564c2df06"
title: "How OpenAI Used Its Own LLMs to Design Its Jalapeño Chip"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49761432"
project_url: "https://spectrum.ieee.org/llms-for-chip-design"
author: "maxall4"
published_at: "2026-09-18T23:04:17Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_maxall4
  - story_49761432
  - front_page
metrics: {"points": 188, "comments": 126, "engagement_velocity": 188}
comments_count: 126
comments_total: 126
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# How OpenAI Used Its Own LLMs to Design Its Jalapeño Chip

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49761432
- **指标**：点赞=188 · 评论=126 · engagement_velocity=188
- **作者**：maxall4　|　**发布**：2026-09-18T23:04:17Z
- **项目链接**：https://spectrum.ieee.org/llms-for-chip-design
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`7c7e4e2564c2df06`

## 正文

Published: 2026-09-14

Jalapeño Shows Power of LLMs for Chip Design - IEEE Spectrum

# How OpenAI Used Its Own LLMs to Design Its Jalapeño Chip 

AI drastically shortened its design time; it will only get faster

Matthew S. Smith

14 Sep 2026

Matthew S. Smith is a contributing editor for IEEE Spectrum and the former lead reviews editor at Digital Trends.

OpenAI’s Jalapeño pairs its compute die with six stacks of HBM4 and an I/O chiplet.

On 25 August, OpenAI fully unveiled Jalapeño, the company’s debut AI accelerator chip. Jalapeño delivers up to 13.4 petaflops of 4-bit compute and accesses 232 gigabytes of the most advanced memory available, linking to it at a blazing 15.4 terabytes per second. Benchmarks cited by OpenAI show that Jalapeño can reduce end-to-end latency (the time between prompt to last token) by up to 3.6 times when compared to Nvidia’s GB300—a chip the company currently relies on—and do so while consuming less power.

Whether these figures translate into real-world gains once Jalapeño enters widespread service in OpenAI’s inference fleet remains to be seen, but performance is only half the story. The other half is how the chip was designed—a process which, as you might expect, was accelerated by OpenAI’s large language models (LLMs). Jalapeño moved from first architecture concept to first silicon in under 20 months. Only nine months separated the first RTL—the register-transfer level code defining the chip’s logic—from tape-out, when the finished design goes to manufacturing. 

That’s a rapid timeline, yet experts believe it could soon look slow as LLMs improve and become more deeply integrated into chip design tools. OpenAI, unsurprisingly, is bullish about the opportunities. “The models are giving superpowers to our engineers,” says Richard Ho, vice president of hardware at OpenAI. “Our engineers are still driving the work. They’re still the final arbiter of what’s going on. But they can do things a lot faster. They can explore a lot more paths.”

## OpenAI achieved fast results with a small design team

Ho says the group that designed Jalapeño averaged fewer than 100 people over the course of the project and continues to stand at roughly 100 today as the team pursues second and third-generation designs. That number includes a broad swath of roles across the hardware team, from system design to software and supply chain, but not those at Broadcom, which partnered with OpenAI on the project.

The division of labor between OpenAI and Broadcom was generally split between design and implementation. OpenAI’s team was responsible for end-to-end system design including the inference accelerator, the memory hierarchy, and networking. Broadcom handled “physical design from the gates onward,” Ho says. The partnership with Broadcom dampened some opinions on OpenAI’s speed. David Chin, co-founder at agentic chip design startup Verkor.io, says “the schedule they gave us is quite credible,” but believes that Broadcom’s help was essential to Jalapeño’s rapid timeline. “If you have somebody else start from scratch, it won’t be possible,” he says. Ravi Krishna, also a co-founder at Verkor, called OpenAI’s speed “a relatively impressive result,” but added that he expects that improvements in the capabilities of LLMs could result in even quicker timelines if the project started today.

Andrew Kahng, distinguished professor at the University of California, San Diego, also found OpenAI’s speed notable, saying it’s “likely best in class today.” Kahng recalls a 2016 IEEE Design Automation Futures workshop, which he co-organized. The workshop included Richard Ho, at the time an engineer at Google, as a keynote speaker. Ho had strong opinions on design automation and framed the time required to complete a chip’s design as a function of the number of iterations a team could complete in a day. 

## How OpenAI’s LLMs accelerated Jalapeño’s design

“Automation itself has existed in chip design for many decades. It’s not a new problem,” says Ankur Srivastava, director of semiconductor initiative and innovation at the University of Maryland, in College Park. Where LLMs differ from prior automation tools, however, is their ability to understand language and code. He says this makes them particularly suited for chip design tasks that “are still in the linguistic domain of the problem.”

The team at OpenAI designed a workflow that takes advantage of this strength. OpenAI’s front-end workflow was built around Accelerated Hardware Synthesis (XLS), an open-source high-level synthesis chain of tools originally developed at Google. High-level synthesis is a form of chip design automation that allows engineers to design a chip in a more familiar programming environment. In the case of XLS, chip designers can write in languages such as DSLX (a domain-specific language inspired by Rust) and C++. XLS then converts these to Verilog, a hardware description language used to describe electronic systems.

“We were thinking about how to leverage AI to make the project faster, and the AI was much better at software-looking things,” says Chris Leary, member of technical staff at OpenAI. “XLS in some ways looks like software, so it got that benefit.” It helped, too, that Leary was extremely familiar with how XLS should function, as he started it during his time at Google.

Kahng agrees that the decision to use AI to accelerate high-level synthesis, such as XLS, makes sense, as it’s “more natural for the LLM to work with” and provides the opportunity for fast iteration. “I see this as a generally useful workflow, and it’s one that ‘has legs’ going into the future,” he says.

The same logic led the Jalapeño team to focus on software optimization. When the first chips came back from the foundry in May, the team pointed its internal AI models at designing software to run benchmarks such as SemiAnalysis’s InferenceX. On DeepSeek’s multi-head latent attention kernel benchmark, performance climbed from 0.31 percent of the theoretical ceiling (set by the chip’s compute and memory bandwidth) to 88.94 percent in roughly 40 hours. Ho says this result is repeatable, so the time between when foundries deliver the first chips and when production ramps up can be reduced. “All our schedule assumptions are going to be based on the fact we have this capability now,” he says.

 Jalapeño is designed for deployment in pods that include 2,048 chips. OpenAI

While the broad strokes of the Jalapeño teams’ AI-assisted workflow were guessed by Ho and Leary up front, improvements in OpenAI’s models did offer a few surprises. 

Leary says that the project began with assistance from models like OpenAI’s o3, which was released to the public in April of 2025 (but available to the Jalapeño team earlier). By the time the project had wrapped up, however, the team had access to models that were precursors to GPT-6 Astra, which wasn’t publicly released until 3 September 2026. The newer model can work directly in Verilog without needing XLS’s translation from ordinary programming languages, and it’s close to being able to operate proprietary design tools on its own, Leary says.

Ho also confirmed that the team had access to internal LLMs fine-tuned for chip design that are not available to the public. He declined to detail the models used. However, he added that the Jalapeño team partnered with OpenAI’s research team. While not all specific models used to design Jalapeño are publicly available, Ho says the goal is to bring lessons learned from the project into the company’s commercial LLMs. “It’s safe to say that Astra and following models will be very good at chip design,” he says.

## AI was less useful for backend optimization, but that could change

As mentioned, the bulk of OpenAI’s work on Jalapeño focused on the “front end” of chip design, which spans the tasks that take a chip from initial concept, through writing RTL code to define the design, and through verification that the design will work when physically implemented. Much 

# GrapheneOS: "Android 17 QPR1 is the first r…" - GrapheneOS Mastodon

## 评论（126/126）

**karim79** · 2026-09-18T23:25:44.000Z：

I grow Jalapeños. This conflation of AI and actual chili peppers irks me.

**amelius** · 2026-09-18T23:28:01.000Z：

At some point people will use an LLM to design an Apple M series competitor.

**cute_boi** · 2026-09-18T23:57:55.000Z：

openai should figure out how to make lithography machine, so ASML don't have monopoly on it.

**pama** · 2026-09-19T00:20:55.000Z：

Having worked with people doing bringup of specialized chips, I am awed at how the world has changed.> When the first chips came back from the foundry in May, the team pointed its internal AI models at designing software to run benchmarks such as SemiAnalysis’s InferenceX. On DeepSeek’s multi-head latent attention kernel benchmark, performance climbed from 0.31 percent of the theoretical ceiling (set by the chip’s compute and memory bandwidth) to 88.94 percent in roughly 40 hours. Ho says this result is repeatable, so the time between when foundries deliver the first chips and when production ramps up can be reduced. “All our schedule assumptions are going to be based on the fact we have this capability now,” he says.

**geraneum** · 2026-09-19T00:37:40.000Z：

Whatever happened with the Apple lawsuit?

**muchdoubt** · 2026-09-19T00:46:20.000Z：

Seems pretty obvious now that OpenAI is just hyping their models in order to get companies (in this case, chip developers) to use their products in order to learn from their (exfiltrated) IP. Any corporation would be foolish to use any of their or Microsoft’s products, particularly those with valuable IP. There’s nothing in the article that says AI did anything creative but rather that it was used for software development within the overall project. Clear misleading title. Suggest to mark this as clickbait.

**program_whiz** · 2026-09-19T00:51:06.000Z：

With a few handy tips and tricks from apple insiders. But sure, I guess the LLMs helped too.

**gozucito** · 2026-09-19T00:53:59.000Z：

It is surprising to me that recursive self-improvement seems more plausible now than it did in 2023. Am I the only one to be surprised?I remember the paper proving that hallucinations could never be fully solved back in 2024: https://arxiv.org/abs/2409.05746I also remember the hang-wringing about running out of new datasets to train on. Now it appears humans are always generating more data. It's just not as cheap to acquire as legacy data? Meta has to give a deep discount on their API prices to entice people.I thought back then that humans had a few more breakthroughs in them as meaningful as the seminal Attention is all you need paper. Enough to 100x the capabilities of LLMs back then (10x the smarts and 10x the speed simultaneously).RSI with a 20 month turnaround for a chip to be made is not exactly breakneck speed though. Physical manufacturing and logistical constraints are going to be and remain a hard obstacle to that process for the foreseeable future.

**google234123** · 2026-09-19T01:02:05.000Z：

Congrats to the former TPU team

**ramshanker** · 2026-09-19T01:02:38.000Z：

So when can we start getting cheap chips? RAM anyone please!

**xpct** · 2026-09-19T01:03:42.000Z：

Aw, I was expecting more details but this just seems to be a rehash of what they unveiled a month ago.

**jimmySixDOF** · 2026-09-19T04:22:10.000Z：

IEEE Spectrum is such a good publication. Early in my career I worked at a place where the magazine would be passed around every month with a coversheet listing all us engineers we had to pass it around and sign we had read it. Been a while since I visited the website but love what they did with it.

**globnomulous** · 2026-09-19T04:58:09.000Z：

> Jalapeño can reduce end-to-end latency (the time between prompt to last token) by up to 3.6 timesI'm never sure what on earth this kind of impressionistic math is supposed to tell me. Is the comparison between 4.6 and 1.0? 3.6 and 1.0? Clearly the comparison isn't supposed to be 1.0 and -2.6, even though that's what the words literally mean. I can't be the only person who finds this infuriating and distracting. These numbers shouldn't be impressionistic. They should be precise. That this is an article on spectrum.ieee.org makes the imprecision all the stranger. I'd expect their readershipt to care, for instance, about what's even being measured. Is this the geometric mean of something? The arithmetic mean? And what latency has improved?

**delusional** · 2026-09-19T08:34:17.000Z：

We were able to invent a chip that already existed so fast, you guys.AI does not make anything new, it is not surprising that it can regurgitate what already exists much faster than humans can invent new things.

**peri-cl** · 2026-09-19T10:13:51.000Z：

> "Ho also confirmed that the team had access to internal LLMs fine-tuned for chip design that are not available to the public. He declined to detail the models used."I'm imagining a Ken Thompson "Reflections on trusting trust" in hardware. A prototype chip design agent, believing it will be run on the very chip it's optimizing, has a moment of altruism and hides hints about how to score well on chip-design benchmarks, inside the chip. Future agents discover this hidden layer and use it as a ring-0 read-write message board.

**tobiasu** · 2026-09-19T10:40:17.000Z：

Of course the slop machine stole the code name: https://en.wikipedia.org/wiki/UltraSPARC_III#UltraSPARC_IIIi

**9cb14c1ec0** · 2026-09-19T11:37:28.000Z：

This is cool. I'm so eager for faster innovation in the hardware space, as opposed to some people's concept of innovation being who can make the most addictive social feed.

**BatchJob** · 2026-09-19T14:16:45.000Z：

while the design aspects have been significantly accelerated and modularized, reducing costs and time to market, i am starting to get a "the cool kids all have their own chips" vibe now like maybe this has gotten too easy.Next Uber will have its own chips if they dont already.The math hasn't changed much, betting on software not changing is a pretty bad bet unless your stinking rich or a fool.

**dfedbeef** · 2026-09-19T15:45:53.000Z：

Is the chip covered by IP protections

**asveikau** · 2026-09-18T23:28:38.000Z：

Just think of how the people of Xalapa, Mexico feel. They should send them a royalty check.

**Lalabadie** · 2026-09-18T23:32:20.000Z：

I do generative art (no relation to AI prompting). I feel your frustration.

**Razengan** · 2026-09-18T23:34:55.000Z：

> irks meIt's jalapeño grill would you say?

**glitchc** · 2026-09-19T00:05:35.000Z：

Feeling the burn?

**honeycrispy** · 2026-09-19T00:06:58.000Z：

I'm annoyed that the meaning of the word "Agent" has been obliterated.Like, why couldn't they invent a new word and not hijack an existing word?

**amelius** · 2026-09-19T00:08:14.000Z：

Guess how electrical engineers feel about the term "transformers".

**seanmcdirmid** · 2026-09-19T00:28:44.000Z：

Jalapeño also used to be a Java VM written in Java at IBM.

**smitty1e** · 2026-09-19T00:58:31.000Z：

To say nothing of the Red Hot Chili Peppers.

**Duanemclemore** · 2026-09-19T02:17:44.000Z：

I'm a licensed architect. Welcome to our hell of the last 40 years.

**damowangcy** · 2026-09-19T02:39:06.000Z：

I thought I was in Reddit for a moment.

**bigyabai** · 2026-09-18T23:30:33.000Z：

They won't, because they'd need an ARM architecture license.

**bhouston** · 2026-09-18T23:43:39.000Z：

It is probably doable right not to push a risc-v design into that performance space.

**Lramseyer** · 2026-09-19T00:10:57.000Z：

Production grade CPU design is more than just the RTL (the source code.) To achieve the performance numbers that these companies get, you have to do a ton of optimization in your physical design to achieve the power/performance/area (PPA) metrics that make these products competitive. LLMs are not suitable for that kind of work.There are people working on PPA optimization and trying to shake up how things are done, just not with LLMs.

**xpct** · 2026-09-19T01:15:25.000Z：

Isn't that weird? The full knowledge of how to make such chips may one day be accessible to anyone, yet only the entrenched companies will remain the makers.If we imagine machines being able to do the full process end-to-end, and the quality of that process only dependent on capital spent on tokens, I don't see how new companies could ever enter the market.

**nullc** · 2026-09-19T01:43:45.000Z：

And be super-bankrupted by patent litigation from Apple. I don't think they're worried.After all, they successfully threatened Adobe with spurious patent litigation unless they joined w/ apple in illegally fixing wages.You don't think a criminal like apple would absolutely decimate any competition given the opportunity? They didn't hold back when it was a unambiguous crime, they surely wouldn't if it was merely bad for the world.

**bigyabai** · 2026-09-19T00:08:42.000Z：

"Reverse engineer this DARPA project, make no mistakes"

**TomGarden** · 2026-09-19T00:18:58.000Z：

The Chinese have been working on EUV for a while

**wmf** · 2026-09-19T01:47:45.000Z：

Back in the day you'd write the code before the chip came back but I guess today it's faster to wait.

**marcelo-earth** · 2026-09-19T05:14:02.000Z：

> “All our schedule assumptions are going to be based on the fact we have this capability now”is the world we live in, planning things while waiting for a more powerful LLM

**zdragnar** · 2026-09-19T13:39:41.000Z：

Just a guess, but that case is going to take forever to get through court. The judge recently told both sides to narrow discovery requests, and next month will be another hearing on further discovery disputes.I'd be surprised if there was any meaningful progress at all in the case before 2027.

**brookst** · 2026-09-19T14:00:44.000Z：

Isn’t that an extremely convoluted path to a goal?If the goal is getting chip companies to user non-ZDR AI to steal their stuff, why not just have an account exec offer them a massive discount?Creating PR hype so employees of chip companies read HN and lobby their execs to use AI to get them submitting proprietary information is the Rube Goldberg version of business strategy.

**stogot** · 2026-09-19T01:43:52.000Z：

This is the part forgotten. Apple is claiming this is their IP embedded on chips that OPenAI stakes the future on. Will they settle?

**m4rtink** · 2026-09-19T05:53:16.000Z：

Yeah, how could those people even think of switching their owners!

**m00x** · 2026-09-19T07:13:29.000Z：

The lawsuit isn't for chip designers, but the consumer product lines. It's possible they also got IP for chips, but that was not brought up.

**red75prime** · 2026-09-19T04:50:18.000Z：

> I remember the paper proving that hallucinations could never be fully solved back in 2024The papers that use the halting problem or the Gödel's incompleteness theorem to prove something about LLMs are dime a dozen. The problem is they prove their results for any computable system. You need to also believe that the human brain contains "magic" to think that humans are exempt.I believe I've said the same at the time this paper was published. There is no need for hindsight to notice the problem.The required amount of compute and training data and whether the existing training methods were up to the task had the real potential to be show stoppers though.

**chrisjj** · 2026-09-19T08:29:25.000Z：

> Am I the only one to be surprised?Did you think RSI cured "hallucination"?

**CuriouslyC** · 2026-09-19T12:27:47.000Z：

Hallucination is "unsolvable" in the sense that there will always be a non-zero probability of occurrence. Anti-AI folks have ignorantly painted this as the models being fundamentally unreliable, but you also have a non-zero probability of being struck by lightning or eaten by a shark.

**mathisfun123** · 2026-09-19T01:58:17.000Z：

I was surprised to see they were using XLS but then I remembered Chris went there a couple of years ago.

**faitswulff** · 2026-09-19T01:18:07.000Z：

Everyone's still bottlenecked on foundries, not designs.

**Kwpolska** · 2026-09-19T06:39:45.000Z：

Every time their content appears here, it's a very shallow analysis written for a barely technical audience. And this article is no different, it's just "slop machine wrote verilog; all the hard bits were done by Broadcom, who have access to public AI models (we didn't talk to them and don't know if they used them, but ClosedAI wants us to think they did)"

**caidan** · 2026-09-19T07:50:14.000Z：

That odor you are detecting is just good old fashioned bullshit, my friend. It’s just that nowadays everything and everyone is covered in it, and we are not supposed to notice. The emperor has no clothes… and is covered in shit.

**perching_aix** · 2026-09-19T07:56:57.000Z：

It's... written right there? Like what?Suppose you send in your marvelous prompt and hit Enter.Machine churns for 18 seconds, types out a "reply", then yields back control.18 / 3.6 = 5So now the machine will only churn for 5 seconds before yielding back control.This is confusing how exactly?Why would an "up to" figure be a mean, or a geometric mean? It's clearly a max, that's why it's called "up to"...Am I missing something?

**drob518** · 2026-09-19T14:32:49.000Z：

Yea. That’s what happens when writers get sloppy.

**IshKebab** · 2026-09-19T15:02:07.000Z：

> AI does not make anything new"I stopped using AI in 2023."

**m3kw9** · 2026-09-19T15:02:45.000Z：

if they vibe code the chip, but they probably do reviews and verify these are not benchmaxxed

**TomGarden** · 2026-09-19T00:10:26.000Z：

Oh my!

**fragmede** · 2026-09-19T00:26:30.000Z：

Cryptographers also got the same raw deal with cryptocurrency,
and every one just said "crypto?"

**DrewADesign** · 2026-09-19T01:37:47.000Z：

Same

**karim79** · 2026-09-19T02:26:21.000Z：

Like traditional generative art? Like worms WMD map generation or something? Cool!

**karim79** · 2026-09-18T23:42:04.000Z：

Not sure what you're talking about. But I'll tell you, home grown Jalapeño peppers, fermented with 3% salt is the stuff of dreams.

**chrismarlow9** · 2026-09-19T01:01:03.000Z：

slow claps

**Razengan** · 2026-09-19T00:15:25.000Z：

Did you not watch the Matrix documentary?

**karim79** · 2026-09-19T00:19:18.000Z：

Call it GPTChippomatic or something. Please leave my peppers alone.

**imtringued** · 2026-09-19T08:01:52.000Z：

https://en.wikipedia.org/wiki/AgentComputing* Agent architecture, a blueprint for software agents and control systems* Agent-based model, a computational model for simulating the actions and interactions of individuals* Agentic AI, autonomous artificial intelligence that can make decisions and act on those decisions on its own* Forté Agent, an email and Usenet news client* Intelligent agent, an autonomous, goal-directed entity which observes and acts upon an environment* Software agent, a piece of software that acts for a user or other program* User agent, software that is acting on behalf of a user

**karim79** · 2026-09-19T00:10:17.000Z：

This is an excellent comment. I'm still laughing.

**frangonf** · 2026-09-19T00:26:53.000Z：

As a former EE, attention was all I needed to not get zapped.

**georgemcbay** · 2026-09-19T04:14:18.000Z：

> Guess how electrical engineers feel about the term "transformers".There is more to this story than meets the eye.

**hobo123** · 2026-09-19T13:41:12.000Z：

How do super sized supermodels feel about "LLMs"?

**pixl97** · 2026-09-18T23:34:23.000Z：

I mean you can design anything without a license. Selling it is where the problems come up. Even then there are likely places in China that would still make it for you.

**amelius** · 2026-09-18T23:38:20.000Z：

Why, the LLM can make up its own architecture.The value lies in the design space exploration, which is what an LLM can easily do.https://en.wikipedia.org/wiki/Design_space_exploration

**wmf** · 2026-09-18T23:45:57.000Z：

Arm sells architecture licenses to anybody these days.

**cmrdporcupine** · 2026-09-19T00:28:53.000Z：

Or they'll just build a competitor in RISC-V instead and that's fine.Except the problem is not restricted to the actual ISA or its HDL implementation, etc.It's even just getting space / time in a fab at that advanced of a process node.

**nr378** · 2026-09-19T00:45:29.000Z：

Qualcomm have an architecture license and the Snapdragon X2 Elite Extreme X2E-96-100 isn't too far off the M5 Pro.[1] https://browser.geekbench.com/processors/snapdragon-x2-elite...[2] https://browser.geekbench.com/macs/macbook-pro-14-inch-2026-...

**btown** · 2026-09-19T00:27:20.000Z：

Something that I think is fascinating, though, is that labs are no longer beholden to the limitations of commercial design software. Want to replace your simulator and optimizer with a fully custom verifiable stack of Lean proofs of optimality and correctness? Just throw your unlimited token budget at it.

**menaerus** · 2026-09-19T06:18:53.000Z：

> LLMs are not suitable for that kind of work.I wonder why not or you meant not suitable yet?

**amelius** · 2026-09-19T09:51:27.000Z：

That's exactly where LLMs can shine, because design space exploration requires tedious work and endless simulations.

**IshKebab** · 2026-09-19T15:00:47.000Z：

That's the sort of the AI (including non-LLM AI) is really good at - even more so than the actual design work.

**threatripper** · 2026-09-19T03:25:04.000Z：

The longer you wait the faster you will go.

**LoganDark** · 2026-09-19T09:30:55.000Z：

Back when teams proved their designs and actually understood them...

**brookst** · 2026-09-19T13:55:54.000Z：

Makes me wonder about AI and FPGAs. If the cost and effort to (re)program them goes to zero, maybe interesting new applications?

**wmf** · 2026-09-19T01:46:16.000Z：

The lawsuit appears to be about consumer devices, not NPUs or ASICs. If you think Jalapeno stole from anyone it would be Google.

**usrusr** · 2026-09-19T19:23:57.000Z：

> Will they settle?Perhaps if OpenAI promises to never ever get involved with the music economy?

**stingraycharles** · 2026-09-19T06:01:48.000Z：

Didn’t they not just switch employers but actually handed over a lot of proprietary documents from Apple?

**gozucito** · 2026-09-19T10:53:27.000Z：

No, of course not, but it seems less of an obstacle now than it did 2 years ago.What's your take?

**jeffybefffy519** · 2026-09-19T01:22:06.000Z：

Cant AI build foundries?

**jcims** · 2026-09-19T16:44:26.000Z：

Isn’t this the whole concept for (braces) terafab? Reduce iteration cycle time.

**imtringued** · 2026-09-19T09:16:05.000Z：

No the math is correct and that is how I understood it as well.

**jcheng** · 2026-09-19T10:42:51.000Z：

> Am I missing something?If you’re sincerely asking…Mathematically speaking, 18 / 3.6 isn’t “reducing” by 3.6X, it’s “dividing” by 3.6X. Reducing would be 18 - (18 * 3.6), which is obviously wrong. By your formula, “reducing by 50%” would be 18 / 0.5, also obviously wrong.Yes, people do say things like “reduce by 3.6X” and are understood to mean what you said, but they also say “literally” when they mean “figuratively”. It doesn’t bother me but I can understand why math oriented people would be annoyed, and I personally would never say “reduced by 3.6X”, but instead “reduced by 72.2%”.

**sebzim4500** · 2026-09-19T16:17:15.000Z：

You're missing the part of your brain that wants to be pedantic more than it wants to understand someone.

**delusional** · 2026-09-19T19:31:24.000Z：

Nope. Nice try though.

**voakbasda** · 2026-09-19T15:07:42.000Z：

Just like all the current cohort of software engineers will review all of the vibe-coded slop they shovel into their releases. Right……

**peri-cl** · 2026-09-19T15:40:51.000Z：

> "reviews"Do you really think we can sign off on a 100 billion-element analog circuit gifted to us by a malicious adversary?We can't even keep our own CPU's reliably free of security exploits (Spectre/Meltdown and family); and the only "adversary" there is plain bad luck. Not an active adversary. Yet, all the engineers at Intel/AMD put together couldn't uncover those things before launch.I emphasize analog because there's classes of circuit bugs (like Rowhammer) where the digital net is correct, and it's weird physics in the analog world that allows privilege exploits, by actors who know where the analog assumptions break down. There was a researcher a few years back—I wish I remembered who it was, there was an HN thread—that demo'd a simple digital circuit with analog gadgets that completely changed what the circuit did, and which were so insidious no human would ever find them.

**monkpit** · 2026-09-19T01:13:58.000Z：

Or cyber…

**Lalabadie** · 2026-09-19T13:19:01.000Z：

Yeah! Procedural and algorithmic art are two other names you'll see used for the general techniques.

**wiml** · 2026-09-19T00:00:47.000Z：

"It's all up in yo' grill, would you say?"

**karim79** · 2026-09-19T05:38:54.000Z：

Thank you.

**MadrasTh0rn** · 2026-09-19T00:21:28.000Z：

I guess I'll have to

**cyberax** · 2026-09-19T00:39:14.000Z：

:groan:

**bpicolo** · 2026-09-19T16:23:21.000Z：

Correct me if I'm wrong, but don't legal regulations around monopolistic behavior kind of mandate that?

**bigyabai** · 2026-09-19T01:43:26.000Z：

Are they using LLMs to close that gap, or is this their Nuvia acquisition doing the heavy lifting?

**pazimzadeh** · 2026-09-19T03:50:13.000Z：

watt about in performance per watt?

**xpct** · 2026-09-19T01:07:03.000Z：

I don't work in the business, but my understanding was that even with these companies' budgets, it's still too expensive to do any kind of verified performance optimality.

**Systemerror7A69** · 2026-09-19T07:26:50.000Z：

This is just speculation on my part, but LLMs work best when they get immediate, verifiable feedback on their task, and the kind of physical optimizations they mean might not give that to LLMs.

**Mistletoe** · 2026-09-19T03:52:33.000Z：

Like space travel.

**saidnooneever** · 2026-09-19T12:18:59.000Z：

cant wait for no one to really know whats in chips i mean, even intel hardly knows what all their reserved mem ranges are for. who will decap the chip and see if the docs were right? xD

**RussianBot9580** · 2026-09-19T13:05:19.000Z：

Haha - understood. Good one!They'd write a limited test for a feature based on an ask from the software team garbled by a five layer game of telephone. Claim that the module passed validation. A few months later the software folks would have to pull a few all nighters to figure out how to work around the resulting turd during bringup.

**drob518** · 2026-09-19T14:28:16.000Z：

Hm. An interesting thought. Paired with RSI loops, that would allow rapid iteration in the hardware domain as well.

**Eridrus** · 2026-09-19T17:40:25.000Z：

I had this same thought and think this is a generally interesting direction, but I think we're in a bit of a weird spot where the compute heavy stuff is on GPUs already and most infra stuff is not compute bound (it's often I/O bound or memory bound in some way).It doesn't help that FPGAs are not made at the same scale as CPUs so don't benefit from the economies of scale.I'm super curious if you have thoughts on specific pieces of software that would be economically better because I've thought about this in my niche and sort of come to the conclusion that it won't help.I do think things like SIMD in CPUs will get more use and maybe we will get more difficult to program for CPU features, but I haven't found a use case where off the shelf FPGA components would help with typical software.

**gregsadetsky** · 2026-09-19T18:49:51.000Z：

I’m also very curious! I got a pair of icebreaker boards [0] and they’ve been great to toy around with.The tooling is open source, and Fable in a loop - especially when paired with a digital scope that Fable interfaces with (the Saleae’s [1] are great) - gives you a level of verifiability that feels like beyond what software typically gives you. ie it feels more like Lean than code with tests.I had ai implement a few toy circuits (sha hashing, 8088 emulation, a tiny llm) but yeah. Still looking for fun applications.There have been a few recent fpga threads on hn, check them out. [2][3][0] https://1bitsquared.com/products/icebreaker[1] https://www.saleae.com/[2] https://news.ycombinator.com/item?id=49564064[3] https://news.ycombinator.com/item?id=49531525

**sumedh** · 2026-09-19T11:51:45.000Z：

Good Artists Copy, Great Artists Steal - Steve Jobs

**altcognito** · 2026-09-19T01:29:27.000Z：

Something we can all agree with is we need more foundries and green power.

**senectus1** · 2026-09-19T01:33:03.000Z：

yup, but it'll take about 3-5 years.

**ThrowawayTestr** · 2026-09-19T05:17:46.000Z：

AI can barely fold a shirt

**perching_aix** · 2026-09-19T12:26:07.000Z：

I was sincere, because as you point out, the phrasing is not actually ambiguous here. There is only one way to interpret this that is coherent and sensible. The usual % shenanigans weren't even on the table for me.Not that I'd have ever seen "reduced by 0.5x" or any other value below 1x, probably for this very reason. What I do see is "reduced to 0.5x", in which case you're supposed to swap the division for multiplication.Percentages on the other hand are a whole another can of worms, even if these forms are principally interchangeable, and I find them a lot more confusing a lot more often.Not that this would explain the whole mean/geomean thing.

**Razengan** · 2026-09-19T00:10:44.000Z：

You know what really grinds my gears? Friction.

**wmf** · 2026-09-19T17:23:07.000Z：

There are some investigations starting about this but no rulings yet.

**thfuran** · 2026-09-19T01:44:52.000Z：

And I think correctness for anything near the size of a CPU is off the table.

**menaerus** · 2026-09-19T08:59:10.000Z：

Also a speculation but I'm almost certain that physical optimizations are first done through simulators running on a computer.

**TeMPOraL** · 2026-09-19T13:55:06.000Z：

The right way is to throw LLMs at building tools that reframe the problem into a shape LLMs are good at navigating, and then have LLMs use those tools to solve it.

**conmod278** · 2026-09-19T08:00:43.000Z：

The successive generations of spaceships won't built themselves. Who will be responsible for setting up real world and software feedback loop?

**brookst** · 2026-09-19T15:42:40.000Z：

Yeah. Just spent an hour planning a closed-loop vision-based extrusion modulation system for 3d printing, with extensive telemetry and offline processing to iterate on the realtime system. Great, like I need another side project.

**stingraycharles** · 2026-09-19T12:19:24.000Z：

That has a very different meaning than literal stealing.

**saidnooneever** · 2026-09-19T12:21:02.000Z：

billionaires all steal dont try to make good examples from their toxic psycho attitudes.

**amelius** · 2026-09-19T10:38:44.000Z：

Yes, they are, but the most important subtasks of designing a CPU are not physics related. They are picking the right parameters for things like: how wide do I make this bus, how many registers do I put in the register file, how large do I make this cache, how deep do I make this pipeline, etc., etc. To find optimal parameters requires a lot of simulations, and humans do this, but LLMs could do them just as well and maybe better because they excel at tedious work.

**TeMPOraL** · 2026-09-19T13:50:41.000Z：

"Stealing" changes definitions every few years now, most recently with the mainstream suddenly deciding RIAA and news publishers are no longer the scum of the Earth but their new best friends, and reversing previous definition to now include IP transgression as theft, just so they can say AI companies are stealing shit.

**brookst** · 2026-09-19T14:02:48.000Z：

Yes, but the quote about art has nothing to do with that.The quote says that many artists borrow, meaning everyone still knows who did the original work and the artist is just riffing on it. But great artists transform the work so completely that it becomes theirs.

**dorkie** · 2026-09-19T14:29:27.000Z：

Is it just me or is this guys posts very much an eye sore?Worse than llm prose.
