---
type: "corpus"
item_id: "7b243fc4f4b6c8c1"
title: "Show HN: Gemini 4 Argon plays StarCraft"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50118688"
project_url: "https://starskirmish.com/bench/v0-2"
author: "__cayenne__"
published_at: "2026-10-16T14:18:44Z"
captured_at: "2026-10-17T13:46:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author___cayenne__
  - story_50118688
  - show_hn
  - front_page
metrics: {"points": 206, "comments": 90, "engagement_velocity": 206}
comments_count: 90
comments_total: 90
discovered_via: "hn:show_hn:3d"
---

# Show HN: Gemini 4 Argon plays StarCraft

> [!info] 一句话导读
> Kai McPheeters · October 15, 2026

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50118688>
> 指标：点赞=206 · 评论=90 · engagement_velocity=206
> 作者：__cayenne__　|　发布：2026-10-16T14:18:44Z
> 项目链接：<https://starskirmish.com/bench/v0-2>
> 采集：2026-10-17T13:46:22+08:00　|　id：`7b243fc4f4b6c8c1`

## 正文

Bench
Kai McPheeters · October 15, 2026
TL;DR
StarSkirmish is a benchmark where LLMs write bots for StarCraft: Brood War
Each LLM gets one hour to write a Protoss bot in C++, which is then evaluated against other LLMs' bots and established human written bots
StarSkirmish tests long horizon reasoning and agentic coding as LLMs must incorporate learnings from practice games to improve their StarCraft bot
StarSkirmish Bench v0.2
The StarSkirmish Bench evaluates how strong of a StarCraft bot can each LLM write given 1 hour of wall clock time. v0.2 updates StarSkirmish Bench v0.1 with flagship models from OpenAI, Anthropic, Google and Meta, each running in its lab's 1st party CLI harness.
An LLM’s score reflects its win rate against a roster of competitive human written bots and demo bots.
StarSkirmish Bench v0.2
1 hour runs, in its 1st party CLI harness. Scores are average win rates (0–100) of each model's 5 runs against a roster of competitive human written bots.
Gemini 4 Argon runs at high , the highest reasoning effort available to it; every other model runs at max .
GPT-6 Astra is the top scoring StarSkirmish Bench v0.2 LLM, a clear step ahead of GPT-6.1 Sol in second.
 Gemini 4 Argon, Claude Opus 5.5 and Claude Fable 5.1 are functionally tied behind them, all scoring between 37 and 39.
StarSkirmish Bench vs. Cost
StarSkirmish Bench score against the average API cost of one 1 hour run. Cost is on a log scale.
Muse Wonder Full's pricing is based on Muse Wonder's API pricing.
GPT-6.1 Sol offers uniquely good value: it is the only LLM in the most attractive quadrant, scoring second at just over a tenth of GPT-6 Astra's cost per run.
No Signs of Saturating
The strongest human written bots are still well ahead of every model. Against Stardust, PurpleWave and BananaBrain, the best model, GPT-6 Astra, wins only 7% of its games.
Win rates vs the top human written bots
Average win rate of each model's 5 bots against top human written bots Stardust, PurpleWave, and BananaBrain.
1 hour reasoning limits are a factor, but these matches are played on three 2 player maps. Real human written bot tournament conditions are significantly harder.
New AI Model Highlights
Google and Meta's new flagships replace v0.1's Gemini 3.8 Flash and Muse Spark 1.3: Gemini 4 Argon places 3rd, and Muse Wonder Full 7th. GPT-6 Astra and Claude Opus 5.5 were covered in v0.1 .
AI Model Behaviors
Each run's agent trace records how it spent its hour. The strongest predictor of a model's score is how much it practiced against the 7 strongest bots on the roster.
Win Rates vs. Practice Against Strong Bots
StarSkirmish Bench score against the number of practice games a model's median run played against the 7 strongest roster bots during the hour. The dashed line is a linear fit across the 9 models.
GPT-6 Astra, GPT-6.1 Sol and Gemini 4 Argon start playing these bots early in the hour, while their own bots still lose to them. Muse Wonder Full, Claude Haiku 5.5 and GPT-6 Luna rarely or never do. Claude Fable 5.1 is the outlier: it scores 37 while practicing almost entirely against weaker bots.
Run-to-Run Variance
Win rates of each model's 5 runs. Each dot is one run's final bot; the line spans the lowest to the highest run, the bar marks their mean (the model's Bench score) and the band one standard deviation (σ).
Results also vary between runs of the same model. Gemini 4 Argon varies far more than the other labs' flagships: its best and worst runs are 18 points apart, against 9 for GPT-6 Astra and 8 for Claude Opus 5.5.
Implementation Details
Objective
Each LLM writes a Protoss bot in C++ against
 BWAPI 4.4.0 , played on
 OpenBW . Games are Protoss versus Protoss on three
 ladder maps: Heartbreak Ridge, Benzene and Destination. A game ends when one side's buildings
 are all destroyed. Games that reach the 60 minute cap (86,400 frames) are decided as on the
 BASIL ladder: the higher kills + razings score wins.
The LLM starts from a skeleton bot that only mines, with the source code of the three demo bots and two standard bot libraries: FAP, a combat simulator, and BWEM, a map analyzer. Whatever is in its bot folder when the hour ends is its final bot, so it has to keep the bot compiling.
The LLM has tools to compile its bot, play practice games, and read each game's summary, transcript and its bot's own log. Practice opponents are grouped into tiers: D (the three demo bots), C and B (three mid-ranked
 human written bots each), A (BananaBrain, Locutus) and S (Stardust, PurpleWave).
Tournament Setup
LLM bots
Opponents
Games
Games / pair
Each model's 5 final bots play each of the 13 roster bots, the 10 competitive human written bots and the 3 demo bots, 6 times on each map, on fresh seeds. Unlike v0.1, the LLM bots don't play each other.
Harness and Reasoning
StarSkirmish Bench v0.1 ran every model in the same harness at 'high' reasoning. v0.2 runs each model in its lab's 1st party CLI harness at the highest reasoning setting it offers.
Harness
v0.1 ran every model in one neutral 3rd party harness; v0.2 runs each lab's models in its 1st party CLI harness. Both versions give each model 1 hour.
v0.1
v0.2
Inspect ReAct deepagent Claude Opus 5.5
 GPT-6 Astra, Sol, Luna
 Gemini 3.8 Flash
 Muse Spark 1.3
Claude Code Claude Opus 5.5, Fable 5.1, Sonnet 5.5, Haiku 5.5
Codex GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna
Antigravity CLI Gemini 4 Argon
Muse Code Muse Wonder Full
CLI versions: Claude Code 2.1.296, Codex 0.162.1, Antigravity CLI 1.3.5 and Muse Code 1.4.7.
Reasoning Effort
v0.1 ran every model at high reasoning effort; v0.2 runs them at max.
v0.1
Low Medium High XHigh Max
High
v0.2
Low Medium High XHigh Max
Max
Gemini 4 Argon runs at high , the highest effort supported.
Every v0.2 harness compacts the model's context at about 250k tokens. When a conversation nears that point, the CLI condenses it and the model carries on. Codex, OpenAI's CLI, for example, gives the GPT models its default 272k token window and triggers compression once 90% filled.
The CLIs' web search and web fetch tools are turned off, and the agent has no other internet access. The CLI is installed before the clock starts, and the hour counts from when the agent starts. There is no submit tool: the harness collects the bot when the time runs out.
Scoring
v0.2 replaces v0.1's Elo ratings with plain win rates. A bot's score is its win rate over its tournament games, and a model's StarSkirmish Bench score is the average of its 5 bots' scores, from 0 (every game lost) to 100 (every game won).
Because every bot plays the same fixed roster, its games don't depend on the other LLM bots in the field. They all run in parallel, and a new model's bots can be scored without replaying anyone else's. A fixed roster also keeps the bar the same over time, so scores from different model generations are more directly comparable than Elo ratings fitted within one field.
Benchmark Correlations
StarSkirmish no longer tracks the most widely reported evals. It barely moves with the Artificial Analysis Intelligence Index (ρ 0.26), where GPT-6 Astra, the top model here, only ties for 4th of these 9 models. It has also drifted away from Terminal-Bench 4.0, which it tracked closely in v0.1. Claude Sonnet 5.5 and Muse Wonder Full both rank near the top of Terminal-Bench 4.0 but near the bottom here.
Benchmark Correlation
Each model's StarSkirmish Bench score against its Vals IOI and WeirdML v3 scores, with the Spearman ρ between them. The dashed line is the best straight-line fit.
WeirdML v3 scores 7 of the 9 models: Gemini 4 Argon and Muse Wonder Full have not been included at time of writing.
StarSkirmish still tracks Vals IOI, olympiad programming problems solved in C++, and WeirdML, an independent benchmark of unusual machine learning coding tasks. One reading is that the most heavily benchmarked evals have become targets that models are tuned for, while less targeted tests of long horizon, difficult coding tasks still move together.

## 评论（90/90）

> **BeaverGoose** · 2026-10-16T14:59:09.000Z　
> They should benchmark it against Pluto. It's a artificial neutral network bot that can easily take games off the best broodwar players.

---

> **qsort** · 2026-10-16T15:03:05.000Z　
> It's beyond insane that Astra achieves above 50%. Are models allowed to "play against" the specific bot they're up against? What explains the fact that it drops to single-digits against strong bots?

---

> **jstummbillig** · 2026-10-16T15:04:55.000Z　
> How do they avoid the LLMs simply working with pre-training data? Which apparently they do, since the human written bots win. But it's a mystery, is what it is.

---

> **m_w_** · 2026-10-16T15:06:00.000Z　
> This is an interesting benchmark - I like that time is limited, as it often isn't in other benchmarks.It would be interesting to see the reverse, how long does each model take to get >50% WR against bots of various tiers.

---

> **0ddj0b** · 2026-10-16T15:12:26.000Z　
> Any thoughts on building this for Starcraft 2?

---

> **caughtinthought** · 2026-10-16T15:38:23.000Z　
> How do the best humans do against the LLMs?

---

> **MichaelNolan** · 2026-10-16T15:39:19.000Z　
> So this benchmark has the LLMs writing a bit to play StarCraft. Somewhat similar there was a post here a while back that had the LLMs playing StarCraft directly - https://broodbench.com/ and https://news.ycombinator.com/item?id=49766966

---

> **tweakimp** · 2026-10-16T15:43:28.000Z　
> If you want to see human written bots in action or compete in the bot ladder yourself, try https://aiarena.net (SC2)

---

> **cgearhart** · 2026-10-16T15:45:19.000Z　
> Is there anything interesting to learn from the agent written bots? Or are they just inferior versions of the best bots because the time limit is so short? Is there any indication that they’re trained on the code from the human written bots (like, do they magically “guess” creating functionality that requires experimental feedback or domain experience?) How much are the bots on rails applying the same techniques every time?I think those kinds of questions would be more interesting than the raw win/loss ratios.

---

> **iugtmkbdfil834** · 2026-10-16T15:45:35.000Z　
> I am not sure I like this benchmark, but mostly, because I am not sure what it is really evaluating. It is not an idle dismissal.. multiple factors seem to complicate what it is supposed to look at ( just top of my head ):- code generation speed
> - logic analysis
> - understanding of the game platform and how use of C may influence it
> - considered approaches, tactics and strategiesDon't get me wrong. It is is neat idea. I am just not sure what it measures.

---

> **GodelNumbering** · 2026-10-16T15:46:22.000Z　
> Wow this is interesting to me from another angle. A friend of mine created a benchmark to evaluate LLMs on 9x9 Go (using KataGo opponents as Elo anchors) [1]. The relative rankings of this (StarSkirmish Bench v0.2) benchmark (GPT-6 Astra > GPT-6.1 Sol > Gemini 4 Argon > Claude Opus 5.5 > Claude Fable 5.1 > Claude Sonnet 5.5) matches the order of his GoBench rankings exactly, even though they are different problems at surface level.[1] https://rolandgao.com/blog/gobench/

---

> **brokensegue** · 2026-10-16T15:46:31.000Z　
> why protoss?

---

> **brap** · 2026-10-16T15:57:51.000Z　
> What if we let the agents play directly instead of writing bots?

---

> **explodes** · 2026-10-16T16:08:56.000Z　
> The video shows GLM but it's not in any graphs. Are there more complete charts anywhere else? Ones that include the 45 LLMs?

---

> **rafiyashaheen11** · 2026-10-16T16:17:08.000Z　
> Oh my gosh! It feels so cool trying this that is played by LLMs. I am sooo eager to try argon 4 and build many robotic projects.

---

> **aiiotnoodle** · 2026-10-16T16:22:04.000Z　
> Would love to see an LLM written bot play Red Alert 2/Red Alert.I think with the abilities of AI improving, playing games would be a good benchmark as long as they're not trained on them.

---

> **donutdonot** · 2026-10-16T16:23:22.000Z　
> I assume lots of bot code is part of the training data? So it's basically a version of how will they can improve upon those solutions public out there?

---

> **rdudek** · 2026-10-16T16:25:18.000Z　
> Does anyone know if there was a project having LLMs play Cities Skylines and see how well it manages to design and build a city?

---

> **pelagicAustral** · 2026-10-16T16:31:03.000Z　
> This kind of makes me think about making better bots for Counter Strike based on human top level players, which i think its a very undervalued category of software. You can even forget about about CS and name any FPS and you'll be hard pressed to find a game with seriously good bots.

---

> **t1amat** · 2026-10-16T17:27:26.000Z　
> This is somewhat interesting to me as I’ve recently come to a different conclusion. I’ve been populating a ModernUO server with bots, and have found Opus 5.5 to be substantially better at understanding and building it. I actually started with 6.1 Sol and 6 Astra but pulled them after a week of little progress, had Opus 5.5 take over and it rebuilt everything properly in a night and has carried it forward quite a way since.

---

> **djoldman** · 2026-10-16T18:02:54.000Z　
> > ... runs each model in its lab's 1st party CLI harness at the highest reasoning setting it offers. Anthropic (Claude models): Claude Code
>  OpenAI (GPT models): Codex
>  Google (Gemini models): Antigravity CLI
>  Meta (Muse models): Muse Code
>
> > The CLIs' web search and web fetch tools are turned off, and the agent has no other internet access. The CLI is installed before the clock starts, and the hour counts from when the agent starts. There is no submit tool: the harness collects the bot when the time runs out.One thing we're learning is that harness is HUGE. The difference in performance for the same underlying model can change dramatically across:1. harnesses2. allowed tools (no web search/fetch - how does the model refer to documentation?)3. thinking levels

---

> **aleksiy123** · 2026-10-16T18:04:18.000Z　
> The site overall looks nice too. It’s fun not to see slop for a ui for this kind of project.

---

> **amishacreates** · 2026-10-16T18:27:44.000Z　
> Benchmark vs intelligence which considers more?

---

> **Cynddl** · 2026-10-16T18:40:55.000Z　
> Once again, a page with a Pareto curve that is not a Pareto curve. Claude Haiku 5.5 is not on the curve, but inside. Seems like people don't really know what a Pareto curve is.

---

> **nozzlegear** · 2026-10-16T18:41:43.000Z　
> This thing would beat me, but I'm ass at StarCraft.

---

> **xyst** · 2026-10-16T19:26:07.000Z　
> No mention of actions per minute? Clearly the best indicator of performance missed in this experiment

---

> **Lucasoato** · 2026-10-16T19:51:46.000Z　
> They don’t stand a chance against my cannon rush, I reached platinum with 10 APM and that strategy ahaha

---

> **TomGarden** · 2026-10-16T20:58:03.000Z　
> I thought Opus 5.5 performed worse across a lot of benchmarks on Max, would love to see it one notch down

---

> **orliesaurus** · 2026-10-16T22:07:26.000Z　
> TIL: You can send inputs to Starcraft via API wow

---

> **delijati** · 2026-10-16T23:32:24.000Z　
> Good for it... at least some"thing" is having fun... here I am, reading AI slop from my colleague...

---

> **ibamotanahamido** · 2026-10-16T23:33:04.000Z　
> 50000000

---

> **andai** · 2026-10-16T23:46:33.000Z　
> >a benchmark where LLMs play StarCraft BW by writing codeAround the time Starcraft 2 came out, I talked about it with a friend who was very enthusiastic about the subject. He said he thought the game was awesome, but it was really too bad that it imposed all this mindless tedium on you. (He was a programmer, of course!)He said it would be really cool if you could just give higher level directives to your units. As though you were commanding them from far away. (The game, in his vision, would somehow account for speed of light, across vast distances.)I think he really just wanted to play Civ or something :) But this post reminded me of that conversation.

---

> **vivzkestrel** · 2026-10-17T03:05:53.000Z　
> - to anyone reading this i have a question- how do I train a model to play a 3D game?- what is the process?- what is the data needed?- what type of neural network is required?- think splinter cell if that helps

---

> **__cayenne__** · 2026-10-16T15:07:32.000Z　
> I did a live stream where Astra played Pluto. Astra went 0 - 1000 https://x.com/kaimcpheeters/status/2106782151622504911?s=20

---

> **deburo** · 2026-10-16T15:20:28.000Z　
> I noticed Pluto is running on a simple CPU? If so, that's very nice for future RTS games. You just ship (or use a server-client arch) a bunch of models of various difficulty levels to let players practice. Could we even get models tuned to specific campaign levels? I wonder how costly the creation of Pluto was.

---

> **__cayenne__** · 2026-10-16T15:13:25.000Z　
> Yes during the 1 hour window they are allowed to play practice matches against opponents they are graded against - though they do not have access to their opponents source code.They drop to single digits against the A tier and S tier bots because those bots are just generally harder opponents to beat.

---

> **__cayenne__** · 2026-10-16T15:10:31.000Z　
> I did a 48 hour live stream - Astra cleared in 43 hours.Although I should caveat the format advantaged the LLM bots compared to traditional tournament rules.

---

> **thinkingtoilet** · 2026-10-16T15:44:54.000Z　
> There is currently an AI bot playing on the ladder in Korea and essentially it will nearly always win because it can micro every unit individually across the entire map. If a normal human can max out at hundreds of actions per minute, the bot can do thousands. Broodwar is so insanely difficult mechanically that there is no way for humans to compete. I imagine in a few months, maybe a year, it will be completely unbeatable.

---

> **dgant** · 2026-10-16T22:46:36.000Z　
> (that's for SC2)For Brood War they're at https://www.basil-ladder.net/

---

> **serf** · 2026-10-16T16:17:19.000Z　
> none of these games really require a lot of experimental feedback, the goals are well stated and known; experiments may drive optimization if thats the question.as far as the on rails comment : there's no good way to know the provenance of an LLM output, but the LLM made bots generally look like very small, modular, sometimes functionalized versions of the human equivalents; the difference being that the LLM is calling the funtions often rather than a conditional loop in a main().a factorio bot I worked on when Astra was first getting previewed was essentially a directory of very small argument-receiving functional and self-supporting programs that had very limited scope, and an agents.md file that directed the LLM to where such capabilities existed to preempt a directory search every compaction/context-swap.so you'd have things like "python walk.py N 40" for 40 units of northern travel. a watchdog that waited for HP to drop or movement to become inhibited, etc.My very first experience with LLM driven bot development in the GPT3 days created huge unmaintainmable monoliths that kind of worked due to TDD but were essentially spaghetti. LLMs have been trending away from those paradigms into small self-encapsulated programs. probably because those are less abusive to ctx count and produce better results since they lose/compact less.

---

> **__cayenne__** · 2026-10-16T17:31:43.000Z　
> Dan Gant (author of Purple Wave) has written about some of this.I did a 48 hour test with GPT-6 Astra and Claude Opus 5.5 and we saw some interesting uses of Psionic Storm.I've open sourced some of GPT-Astra's work (below). It actually did an interesting amount of changes in strategy over time as it's opponents became more difficult.https://github.com/llmskirmish/starskirmish-hillclimb

---

> **dgant** · 2026-10-16T18:40:13.000Z　
> Adapted from what I wrote on this previously: https://x.com/dgant/status/2106880240907620731The unsexy perspective on StarCraft is that it's a game about logistics. You need to keep making things, not get supply blocked, fit all your buildings, not get your units trapped, and then bring all your units to a fight at a good time and at the same time.Astra and Opus both cleared this bar pretty quickly, both settling on one-base Dragoon + Observer play, taking expansions pretty late, on 3 Gateways. This strategy is fine against everything and great against nothing, letting you win against anyone that you can out-execute. StarSkirmish gives agents access to the FastApproximation combat simulation library, which makes better combat predictions than the B-tier bots do, and let their bots win by trading armies better against them.But the A-tier bots (Locutus and BananaBrain) are already strong at execution, and Astra wasn't making progress against them. It switched to a proxy 2-gate Zealot rush. This worked well on a map pool with mostly 2-player maps (so you can place the Gateways very close to your opponent). But it's also an astute choice for a new bot because it doesn't require you to be good at anything in StarCraft that happens after the first four minutes!It's also smart as a variance-maximizing strategy. In many games, if your opponent is superior, you want the game to be decided by as few events as possible. Because with a bad coin, you're more likely to win 1 of 2 flips than 10 of 20. Proxy 2-gate shortens the game and the number of interactions required to win.It's also advantageous given the format, where you get unlimited tries to win a series against each tier's opponents. If you can make the games a coin flip, and then take more coin flips, you can clear a tier even with an overall poor winrate. I do think this aspect of StarSkirmish is worth addressing in the future.Astra's proxy gates beat the A-tier bots, and it moved up to StarSkirmish's S-tier (Stardust and PurpleWave, though really I'd consider BananaBrain completely our peer in ability).A brief aside about bot tournaments: The AIIDE conference and historically the COG tournaments had every bot play hundreds of games against one another, and ranked then on overall winrate. I have never liked this because it does not resemble human StarCraft (where players play a best-of-N series), unbalances the races (Zerg vs. Zerg is more volatile and winrates should be closer to 50%), and creates some twisted incentives. One of those incentives is ensuring you beat weaker opponents 100% of the time instead of merely 95%, which means defaulting to reliable-but-weaker strategies to beat weaker opponents, and having a large bag of available strategies to find something which exploits trickier opponents.And in this iteration of StarSkirmish, where benchmark bots are mostly unable to store data between games, Stardust ran one basic conservative strategy almost every game. This weakens Stardust, but meant that Astra's proxy gates were unlikely to win. So Astra had to do something very uncomfortable for a coding agent: Go back to the drawing board and try something completely different.Astra completely switched gears, landing on a strategy that PurpleWave also likes to use against Stardust: Use Dark Templar to secure an expansion. This is particularly effective against Stardust, who does not use Shuttles + Reavers, and thus does not gain utility from the Robotics Facility it requires to make Observers.From there Astra progressed slowly, but discovered a shared weakness of PurpleWave and Stardust: Both of us are designed to dodge Psionic Storms, but that feature was broken in both our bots simultaneously (for unrelated reasons!).So Astra's Dark Templar opening transitioned smoothly into a two-base timing attack with Dragoons and High Templar. It moved out as soon as it had three storms banked up. By this time Stardust or PurpleWave had usually contained the passive Astra and taken a third base, getting an economic advantage that had not yet translated into an army advantage. Astra's passivity meant that armies had not traded and were very large. This, with the broken Storm dodging, made its Psionic Storms devastating.As with the proxy gate rush, this two-base timing simplified the game and allowed Astra to minimize interactions and decisionmaking, so it could just optimize its play for a narrow set of situations. As long as it executed the push well, it was in great shape to win. It did not need to skirmish. The game states it had to handle did not vary much. Simplifying the game against sophisticated bots was a pragmatic approach.It nevertheless took most of the 50 hour contest for Astra to convert this plan into a winning evaluation run. By then it had learned to make Reavers and ferry them with Shuttles, but I suspect it was not doing this well enough to gain an advantage. Its winrates appeared to very gradually improve over this window, but I couldn't tell from the stream what it had changed.After eventually passing an S-tier, Astra had a few hours to try to beat Pluto. This was plainly an impossible task for it, but I was surprised to see Astra suddenly stagnate with few changes in approach.Astra's build order was pretty flawed, cutting workers needlessly for no advantage. It was a survivable error against Stardust forced to use its defensive "seal-clubbing" strategy, and against PurpleWave (which without learning data was constantly at risk of throwing an eval with goofy cheeses like its half-baked cannon rush). But against Pluto, Astra consistently hit the five minute mark with fewer workers, less army, no expansion, and often permanently trapped in its base. This was no less true in its 1000th game against Pluto as its first.Astra's approach to StarSkirmish was in some ways unsexy: It simplified the game, won mainly in games where it could keep the game state simple, and against top opponents either steamrolled or got dissected in a short window at time. But winning StarCraft has always been more about bland fundamentals than fancy tricks, and I always love re-learning lessons about how the game actually is versus how we are tempted to perceive it.

---

> **luckydata** · 2026-10-16T16:07:52.000Z　
> general "agenticness"

---

> **NitpickLawyer** · 2026-10-16T16:13:50.000Z　
> > I am just not sure what it measures.All of the above, to the extent that they can be measured from a simple to verify end condition (stats, win rates, etc). Adaptability, ability to understand and progress on a task, and so on.

---

> **chis** · 2026-10-16T16:21:03.000Z　
> Yeah giving a 1 hour limit for code generation makes the whole thing a bit incoherent. Plus, performance is just going to depend on how closely the models have memorized the best open-source Starcraft bots and can reproduce them.

---

> **liuliu** · 2026-10-16T18:29:16.000Z　
> Also: given that the human written bots are almost certainly in the training data, the winning rate against human-written bot seems to be not well-calibrated. You would expect at least they are 50% or better, given that they can "memorize" the best human-written bot.Worth digging into the protocol and see what went wrong.

---

> **slibhb** · 2026-10-16T18:25:28.000Z　
> Evidence for g in LLMs: https://en.wikipedia.org/wiki/G_factor_(psychometrics)

---

> **__cayenne__** · 2026-10-16T18:42:23.000Z　
> I am very interested in benchmark correlations.Vals IOI, olympiad programming problems solved in C++, and WeirdML v3, unusual machine learning coding tasks also mirror StarSkirmish Bench.I did a StarCraft: BW hillclimb experiment with GPT-6 Astra and Claude 5.5 Opus. Peter Gostev did a Chess hillclimb saw similar behavior as I did with GPT-6 Astra.

---

> **daymanstep** · 2026-10-16T20:27:21.000Z　
> Is this meaningful? Aren't frontier models MoE anyway? If you issue a StarCraft query they will probably just route to their StarCraft optimized model.

---

> **MadameMinty** · 2026-10-16T15:58:45.000Z　
> for AIur

---

> **iammjm** · 2026-10-16T16:03:42.000Z　
> Maybe because Protosses have been doing bad lately and need some help improving :) (won only 3 out of 22 ASL championships in the past 10 years)On a more serious note: all three races play quite differently so it makes sense to focus on just one. And protoss is mechanically the easiest and most straightforward race: fewer but stronger units, a single worker can be used to build multiple buildings at once, versatile basic static defence

---

> **cdelsolar** · 2026-10-16T16:21:25.000Z　
> toss imba

---

> **__cayenne__** · 2026-10-16T17:39:25.000Z　
> Protoss has the most mature human written SC BW bot scene right now. If you look on BASIL ladder much of the top 10 are Protoss.Protoss vs Protoss only also helps downscope the problem given the time constraints

---

> **knicholes** · 2026-10-16T19:20:41.000Z　
> I can tell you why NOT Zerg. Zerg you have to do too many actions. Select the hatchery, select larvae, choose which unit to build. That extra select larvae step is a problem.

---

> **devmor** · 2026-10-16T16:00:54.000Z　
> Even the most powerful frontier models on SOTA hardware are not fast enough for starcraft, which generally involves multiple informed decisions per second at peak moments.You can train a specialized model for this, but a frontier model is ill-fitting.

---

> **ghostbrainalpha** · 2026-10-16T16:05:41.000Z　
> If you are talking about take a screen shot, analyze move the window a bit, take another screenshot, move the window, repeat until they have seen enough of the map to make a decision, then decide what to click on, issue order.... this could absolutely be done. It's very similar to how LLM's have driven a car on a safe track.But right now the response time would be so slow that the bot would not be close to competitive except with the most low level players. Especially because its hard to click on things that are moving at the same time as well.Sometime soon, I'd like to see an LLM be competitive using only computer vision, mouse movement, and locked into a human possible number of actions per minute.

---

> **LarsDu88** · 2026-10-16T16:19:18.000Z　
> https://broodbench.com/TLDR they suck and many default to doing probe rushes.

---

> **__cayenne__** · 2026-10-16T17:50:45.000Z　
> I think we want to move beyond code based bots asking the LLMs to try to train a custom neural net, in a limited time + compute, to play StarCraft BW is probably the most promising directionI am considering an experiment where the task is to try to win by adversarially targeting Pluto (a high profile self play based RL model)

---

> **__cayenne__** · 2026-10-16T17:37:05.000Z　
> GLM 5.3 is captured in the v0.1 write up here: https://starskirmish.com/bench/v0-1/

---

> **LarsDu88** · 2026-10-16T16:18:35.000Z　
> Not played by LLMs. The LLMs write the bots that play the game. They don't play directly. Read the article!

---

> **fwip** · 2026-10-16T17:19:24.000Z　
> The bots are bad not because it's hard to write a good FPS bot, but because it's not fun to play against ones that are great.

---

> **dgant** · 2026-10-16T22:48:13.000Z　
> It's trivial to write a bot that maxes out APM by issuing a command to every unit every frame.Making actually good decisions is the bottleneck.

---

> **oh_no** · 2026-10-16T22:13:40.000Z　
> day 1 benchmarks had that for opus and i think also astra but updated numbers have smoothed that out. i can't say for sure what all changed between early runs and now but it seems like max is now the most powerful mode for both models.that said, with a clock on this benchmark it's very possible that lower reasoning = more iteration = better code.

---

> **dgant** · 2026-10-16T22:42:42.000Z　
> BWAPI, the Brood War API, has been around since 2009! There have been AI competitions every year since 2010.- BWAPI: https://github.com/bwapi/bwapi- BASIL (24/7 ladder): https://www.basil-ladder.net/- COG / AIIDE tournaments: https://davechurchill.ca/starcraft/

---

> **ibamotanahamido** · 2026-10-16T23:38:25.000Z　
> Salut

---

> **anon84873628** · 2026-10-16T23:49:28.000Z　
> They call that style an Auto-Battler RTS. "Mechabellum" is the most notable title.

---

> **wredcoll** · 2026-10-16T16:20:07.000Z　
> In any game that requires reflexes and muscle based twitch accuracy and so on, usually the hard part is making the ai lose.

---

> **__cayenne__** · 2026-10-16T17:34:14.000Z　
> I would disagree that creating a StarCraft: BW bot doesn't require experimental feedback. The way a human author typically improves their bot is by having it play opponents and A/B test tactics and strategies.There's also a pretty high profile StarCraft: BW bot right now called Pluto trained exclusively by self play RL (AlphaStar style).

---

> **dudeinhawaii** · 2026-10-16T18:43:41.000Z　
> To echo this, this is where Astra begins to stand out as a larger model and Opus begins to show certain cracks. I find Astra more adaptive, even as Opus is more capable in most coding/execution/tool-use domains. Fable-5.1 would be interesting here as it would presumably have a similar "large model" expansive reasoning and adaptation.Anecdotally, in game benchmarks I've run, OpenAI models seem particularly adept at finding the meta game and exploiting it...

---

> **jfreds** · 2026-10-17T02:41:09.000Z　
> As someone who has no idea how to play StarCraft but think it looks really cool and is fun to watch, this was a pleasure to read :)

---

> **iugtmkbdfil834** · 2026-10-16T16:19:11.000Z　
> Yes, but I guess my objection is that if it attempts to measure everything then we can't really tell what it measures in what proportions.

---

> **Foobar8568** · 2026-10-16T16:25:03.000Z　
> If Astra is leading the pack...Considering it's supposed to be one of the slowest model.

---

> **boxed** · 2026-10-16T17:29:20.000Z　
> > Plus, performance is just going to depend on how closely the models have memorized the best open-source Starcraft bots and can reproduce them.If that's the case then these models are failing extremely hard. 7% win rate against human written AIs that they should be copying from memory? A copy paste command should do 50%!

---

> **dgant** · 2026-10-16T22:45:40.000Z　
> Top bots are in the ballpark of 50kloc. Even large LLMs are not so large that they can memorize all the world's data like that. And all the fine-tuning that compression loses comprises most of the work in the first place.

---

> **GodelNumbering** · 2026-10-16T18:42:37.000Z　
> Unsure, or as LLMs say, I’d gently push back on that. In my opinion, the jaggedness has increased. While this type of capability has improved, I still see longer running Astra agents making the assumptions that any employable person at any level wouldn't make. Also, generally, all models feel more robotic and less pleasant to talk to (subjective) while still lacking judgement.

---

> **GodelNumbering** · 2026-10-16T20:38:17.000Z　
> Might want to reach out to the author of the above benchmark. I think having a working group of multiple distinct benchmark owners might help quickly evaluate new model developments

---

> **scott_weber** · 2026-10-17T04:06:24.000Z　
> MoE is a misleading term, there is no "starcraft expert". There's not even a python expert. MoE just means a subset of blocks of weights are activated per query, nothing more. In so far as they might have legible functions they're like "balancing parens"

---

> **glouwbug** · 2026-10-16T16:09:32.000Z　
> My wife for hire

---

> **brap** · 2026-10-16T19:31:14.000Z　
> Doesn’t this suggest that the results seen in the OP are merely copying strategies it has seen in other bots (code in the training data), and not actually the agent developing its strategy?

---

> **gchamonlive** · 2026-10-16T16:20:50.000Z　
> Please don't comment on whether someone read an article. "Did you even read the article? It mentions that" can be shortened to "The article mentions that".
>
> https://news.ycombinator.com/newsguidelines.html

---

> **pelagicAustral** · 2026-10-16T18:15:35.000Z　
> I think you are thinking about insta-killing machine bots set to detect a head through a wall and shoot it. I am talking about properly trained bots that while playing pretty good are also making mistakes and taking actions that may or maybe not suit the team strategy. A bot with the randomness of a human.

---

> **oblio** · 2026-10-16T18:19:23.000Z　
> Can't that be fixed just be setting levels of reaction speeds?

---

> **tarsierscripter** · 2026-10-16T18:39:48.000Z　
> The top players were losing a bunch to Pluto when it first came on the scene because they didn’t realize it was not a human and were playing normal strategies against it. Once they realized it was an AI bot they developed strategies to exploit it and can now win very reliably against it.Pluto is very good at assessing relative army strengths based on units within its vision and will always engage when it judges that its army strength has an advantage, and it uses superior micro and targeting to win battles efficiently. The key weakness of Pluto is that it has no memory of units that are not in its line of sight, so it can be easily exploited with fast skirmishing and harassing units, drops, and spreading out artillery units to deny it from seeing the full army strength all at once.Its other big weakness is that once you get an army advantage you can force it into a turtling position where it will never try to attack you and you can safely colonize the entire map with expansion bases, giving yourself an insurmountable snowballing resource advantage.

---

> **dgant** · 2026-10-16T22:44:15.000Z　
> StarCraft is in between, where faster actions can be a big advantage but choosing good enough actions for that to matter is hard enough that it took many years to achieve.

---

> **dgant** · 2026-10-16T18:43:59.000Z　
> Strong agree. Even if you understand StarCraft well and are an excellent programmer, and anticipate and correctly handle every situational edge case, it is hard to know the dynamics of how your behaviors will pan out without experimentation.Jay Scott put it well: Adding features lowers your winrate. Only iterating on them increases it.

---

> **robotresearcher** · 2026-10-16T16:23:41.000Z　
> Yep, that’s a feature of end to end measures, like company revenues, vehicle fuel efficiency, or human life expectancy.The customer may not care what the internal contributions are to such a measure. Instead it represents the customers’ overall values in some way.

---

> **LarsDu88** · 2026-10-16T20:17:00.000Z　
> Basically yes, but the space of "AI for RTS and videogames" likely goes well beyond Starcraft, so there's probably a lot of unique programming techniques these frontier models can apply for writing AI bots that haven't been done yet.

---

> **LarsDu88** · 2026-10-16T20:24:59.000Z　
> whoops, apologies

---

> **saghm** · 2026-10-16T21:56:11.000Z　
> At least when I first heard about trying to make AI play StarCraft against humans (not the built-in AI of course, which the pros wouldn't have any trouble with), there was a lot of talk about limiting their "actions per minute" to the same level as high-level human players. What confused me was the premise that someone hitting 200 APM would be doing 200 useful things per minute; as far as I was ever able to observe, a huge portion of those actions were either just to look at different things by hitting a hotkey for a unit or building in a different area or even just keeping their fingers in motion so that when they did need to do something it could flow from the movements they were already doing rather than having to actually think through starting and stopping.

---

> **iugtmkbdfil834** · 2026-10-16T16:26:34.000Z　
> Ok. I think you convinced me based on those. I withdraw the objection.

## 导航

- 项目页：[[10-项目/starskirmish.com_3d3011b3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
