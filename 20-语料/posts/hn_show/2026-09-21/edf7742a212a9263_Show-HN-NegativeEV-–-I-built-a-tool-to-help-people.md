---
type: "corpus"
item_id: "edf7742a212a9263"
title: "Show HN: NegativeEV – I built a tool to help people see how bad their bets are"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49113999"
project_url: "https://negativeev.com/"
author: "qkwrv"
published_at: "2026-07-30T18:45:26Z"
captured_at: "2026-09-21T03:11:13+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_qkwrv
  - story_49113999
  - show_hn
metrics: {"points": 6, "comments": 5, "engagement_velocity": 6}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:83d"
---

# Show HN: NegativeEV – I built a tool to help people see how bad their bets are

> [!info] 一句话导读
> NegativeEV — Bet Checker

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49113999>
> 指标：点赞=6 · 评论=5 · engagement_velocity=6
> 作者：qkwrv　|　发布：2026-07-30T18:45:26Z
> 项目链接：<https://negativeev.com/>
> 采集：2026-09-21T03:11:13+08:00　|　id：`edf7742a212a9263`

## 正文

Check a bet
About
How it works
Research
Questions
Parlay calculator
For AI agents
NegativeEV — Bet Checker
Paste a bet and NegativeEV checks it against thousands of simulated games to tell you whether the price is good, bad, or fair.
How it works:
Submit a bet — type it, or upload a screenshot of a bet slip.
 NegativeEV matches it to today's slate and grades every leg against simulated outcome distributions from full play-by-play game simulations.
 The verdict explains why the price is good or bad, not just a number.
Notes:
Sports covered right now: MLB, WNBA, PGA, and ATP. Markets include moneylines, run lines, spreads, totals, and player props (hits, home runs, strikeouts, points, rebounds, and more), plus parlays built from them. The per-sport list is on the how-it-works page below.
 Checks are metered: 10 free checks a day; signing in makes checks unlimited, with a per-hour pace cap.
 Bets on games that have already started are still checked, against the simulations from before first pitch — the read is a pre-game projection, and it names the game that started. It stops once that slate re-simulates.
What do people ask about NegativeEV?
Does NegativeEV give out picks?
No. It grades bets that are brought to it. There is no pick list, no play of the day, and no scan of the board for value — a bet has to be pasted in before there is anything to say about it.
What does a check cost?
Nothing. Ten checks a day without an account; signing in removes the daily cap and replaces it with a per-hour pace limit.
How does it decide a price is bad?
Every check runs the actual game thousands of times, play by play, and counts how often the bet would have won. That simulated win rate is compared with the probability the sportsbook's price implies. When the book's number is the higher one, the price is bad.
Which sports and markets can it check?
MLB, WNBA, PGA, and ATP. Markets include moneylines, run lines, spreads, totals and player props, plus parlays built from them. The per-sport list is on the how-it-works page.
Can an AI agent use it directly?
Yes. There is an MCP server at https://negativeev.com/mcp , every public page has a markdown form, and the discovery documents are listed at the end of this page.
Is it betting advice?
No. It reports what the simulations say about a price. Nothing on the site is advice, and no result is guaranteed.
What else is on the site?
Check a bet: https://negativeev.com/
 Parlay calculator (payout, combined odds, implied chance): https://negativeev.com/parlay-calculator
 Parlay payout chart (every leg count against every common price): https://negativeev.com/parlay-calculator/payout-chart
 About: https://negativeev.com/about
 Research (measurements on real betting markets): https://negativeev.com/research
 How it works: https://negativeev.com/about/how-it-works
 What expected value (EV) is: https://negativeev.com/about/expected-value
 What "negative EV" means: https://negativeev.com/about/negative-ev
 Are home run props a good bet: https://negativeev.com/about/home-run-props
 Are player prop bets a good bet: https://negativeev.com/about/player-props
 Are strikeout props a good bet: https://negativeev.com/about/strikeout-props
 Should you bet favorites or underdogs: https://negativeev.com/about/favorites-underdogs
 Are boosted bets actually a good deal: https://negativeev.com/about/boosts
 What the sportsbook's rake is: https://negativeev.com/about/vig
 Are moneyline bets a good bet: https://negativeev.com/about/moneyline
 How betting odds work: https://negativeev.com/about/odds
 What line shopping is: https://negativeev.com/about/line-shopping
 How sim-grading works: https://negativeev.com/about/sim-grading
 How accurate betting simulators are: https://negativeev.com/about/sim-accuracy
 How to check a parlay's EV: https://negativeev.com/about/parlay-ev
 Is betting the over a good bet: https://negativeev.com/about/totals
 Is the run line a good bet: https://negativeev.com/about/run-lines
 Is the run line better than the moneyline: https://negativeev.com/about/run-line-vs-moneyline
 Should you tail picks from X: https://negativeev.com/about/tailing-picks
 Are tennis match odds a good bet: https://negativeev.com/about/atp-match-odds
 Are parlays worth it: https://negativeev.com/about/parlays
 The X bot (@shoulditail): https://negativeev.com/about/x-bot
 For AI agents: https://negativeev.com/about/for-agents
 Contact: https://negativeev.com/contact
 Privacy: https://negativeev.com/privacy
 Terms of Use: https://negativeev.com/terms
What can an agent read directly?
Developer documentation: https://negativeev.com/docs
 Agent guide: https://negativeev.com/AGENTS.md
 LLM site overview: https://negativeev.com/llms.txt
 OpenAPI 3.1: https://negativeev.com/openapi.json
 API catalog: https://negativeev.com/.well-known/api-catalog
 AI catalog: https://negativeev.com/.well-known/ai-catalog.json
 agents.json: https://negativeev.com/.well-known/agents.json
 Authentication guide (agents): https://negativeev.com/auth.md
 MCP server: https://negativeev.com/mcp (card: https://negativeev.com/.well-known/mcp/server-card.json )
 A2A endpoint: https://negativeev.com/a2a (card: https://negativeev.com/.well-known/agent-card.json )
 Agent skills: https://negativeev.com/.well-known/agent-skills/index.json
 Sitemap: https://negativeev.com/sitemap.xml
How do I check a bet?
Submit the bet as plain text — teams or players, market, line, and price. A
multi-leg parlay in one line is graded leg by leg.
Bet to check
Check this bet
About
Contact
Docs
Privacy
Terms
llms.txt
AGENTS.md
API catalog
NegativeEV is informational sports simulation and analysis, not betting advice, and no result is guaranteed. 21+ where required. Gambling problem? Call or text 1-800-GAMBLER.

## 评论（5/5）

> **qkwrv** · 2026-07-30T18:46:58.000Z　
> I know I say it in the title, but I want to be very clear up front: the predominant output of this tool is "don't place this bet."Betting apps want you to bet. If they sense you are tired of losing and might leave, they'll entice you with deposit bonuses, boosted odds and protected picks. There are even people, you see them self-promoting all over X, who sell access to "good" bets. Obviously, they don't refund you if you lose. What the market needed was a way to cut through the noise and the boosted odds and the FOMO and just tell you, based on historical data and known circumstances (weather, recent form), whether this is a good bet.NegativeEV is really two completely different pieces of software: the model and simulation engine and then the frontend and grading logic that sits on top of it. That first piece was far and away the hardest. I'm an enterprise software developer by profession, not a data scientist, so my path to what I consider a very solid model and architecture was full of really, really wrong turns.I started with Major League Baseball. The way it works now is it takes a decade of pitch-by-pitch historical data, comprising about 450 data points in each row (I put in a ton of historical priors), and it builds a PyTorch model targeting the exact pitch result: strike, ball, foul, single, double, etc. The simulator (built in Rust) then takes that model (converted to ONNX) and simulates an entire baseball game. I also have models for pitching changes and position-player substitutions. The end result of a simulation is one "realistic" baseball game, box score and all. Then I do that 5,000 times. Those are the simulations that I use to calculate "fair value" when evaluating someone's proposed wager. If anyone is curious why I bother with the ONNX conversion, it's so the Rust simulator can run the model itself, with no Python in the loop. I'm doing almost all of this on my personal desktop, with some use of Modal to magically spin up VMs when I really want things to fly (Modal is awesome, btw).I knew I had to make this as frictionless as possible for users, since no app would ever want to integrate with me. So I have what I'm referring to as two frontends: I have negativeev.com, and then I have a bot on X. Users can tag @shoulditail under any tweeted-out wager, and my bot will consult the simulation results and return the Expected Value of the bet. Again, it's mostly negative.For negativeev.com, I tried to model the frontend after the chat-interface frontends we're so used to now thanks to LLMs. Not that users can chat. More that I needed it to be able to handle any form in which the user wants to communicate their bet. The easiest is pasted screenshots. On mobile, this is really easy. But users could also just type "Aaron Judge over 0.5 home runs +150", and we'll parse that out and give you what we think is the EV.I also, on a whim, put an MCP server around it. I'm skeptical it will ever get used, but my thought was how cool would it be if LLMs could reach out to it when users asked if such-and-such play was a good wager that day. Not that LLMs should get into the business of supporting gambling, but at the very least they could consult my backend and come back with some insight into why a bet is probably not a good idea (and maybe just ignore it if it was returned as positive EV).So there you have it. This is my first time ever releasing something into the wild like this. There's far more to the story and far more tech details I'd be happy to talk about.

---

> **kiwibyproxy** · 2026-07-30T22:34:17.000Z　
> This is so much in its own bubble; I had to work through multiple pages including the about page, to get the vibes that this is probably about US Baseball sports bets? none of the examples on the front page made any sense to me, most pages are full of unexplained abbreviations but I also recognize im not the target audience. The basics could be more clear though.

---

> **janrakete** · 2026-07-30T20:21:06.000Z　
> It would be even better if your tool could predict every bet correctly. If everyone could win every bet, then the problem of gambling addicts and the companies that take advantage of them would be quickly solved.But your solution is cool, too.

---

> **qkwrv** · 2026-07-30T23:03:02.000Z　
> This is great feedback. Really appreciated.It is its own bubble, but there's a chance I've made that bubble way too small. My target market is actually casuals, not heavy users, since casuals are the ones most likely to gamble _less_ (which is really my goal with the whole app). So I'm going to take this to heart and think about how I can make it more obvious what it's for.Thank you!

---

> **qkwrv** · 2026-07-30T20:34:46.000Z　
> Funny enough, this was sort of my north star when developing it. I know it's an impossible dream or expectation (predicting sports is extremely hard), but it's very true that this tool is really only as useful as it is correct.My first iteration of the baseball model took this to an extreme. I broke down every single step from the pitcher deciding which pitch to throw to the pitcher deciding where to throw it to the pitcher throwing it at a certain speed in a certain spot, and on and on. It was something like 17 sequential PyTorch models. My directive to myself was to not care how much compute it would take to run, just get it to the most right version it could possibly go.Turns out just predicting the end result of each pitch is far more accurate than sequential modeling. I still to this day have a hard time believing it. But the results are pretty stark when I compare the two methods.Anyway, I really appreciate the kind words and for taking the time to check it out.

## 关联链接

- https://negativeev.com/.well-known/agent-card.json
- https://negativeev.com/.well-known/agent-skills/index.json
- https://negativeev.com/.well-known/agents.json
- https://negativeev.com/.well-known/ai-catalog.json
- https://negativeev.com/.well-known/api-catalog
- https://negativeev.com/.well-known/mcp/server-card.json
- https://negativeev.com/AGENTS.md
- https://negativeev.com/a2a
- https://negativeev.com/about
- https://negativeev.com/about/atp-match-odds
- https://negativeev.com/about/boosts
- https://negativeev.com/about/expected-value
- https://negativeev.com/about/favorites-underdogs
- https://negativeev.com/about/for-agents
- https://negativeev.com/about/home-run-props
- https://negativeev.com/about/how-it-works
- https://negativeev.com/about/line-shopping
- https://negativeev.com/about/moneyline
- https://negativeev.com/about/negative-ev
- https://negativeev.com/about/odds
- https://negativeev.com/about/parlay-ev
- https://negativeev.com/about/parlays
- https://negativeev.com/about/player-props
- https://negativeev.com/about/run-line-vs-moneyline
- https://negativeev.com/about/run-lines

## 导航

- 项目页：[[10-项目/negativeev.com_8425657a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
