---
type: "corpus"
item_id: "2dc34bcd3e7f4f85"
title: "Show HN: An NLP based word game for users to play against Astra, Opus, and more"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50397874"
project_url: "https://wordspies.com/"
author: "daluan"
published_at: "2026-11-06T20:19:58Z"
captured_at: "2026-11-07T09:43:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-07"
pub_day: "2026-11-06"
tags:
  - 语料
  - hn_show
  - author_daluan
  - story_50397874
  - show_hn
metrics: {"points": 4, "comments": 7, "engagement_velocity": 4}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:3d"
---

# Show HN: An NLP based word game for users to play against Astra, Opus, and more

> [!info] 一句话导读
> A word-association spy game you play with friends, AI teammates, or both. Two teams share a grid of 25 words; each spymaster gives one-word clues so their team …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50397874>
> 指标：点赞=4 · 评论=7 · engagement_velocity=4
> 作者：daluan　|　发布：2026-11-06T20:19:58Z
> 项目链接：<https://wordspies.com/>
> 采集：2026-11-07T09:43:25+08:00　|　id：`2dc34bcd3e7f4f85`

## 正文

Word Spies
A word-association spy game you play with friends, AI teammates, or both. Two teams share a grid of 25 words; each spymaster gives one-word clues so their team can find its words before the other team does, without hitting the assassin.
Any seat can be a person or an AI model. After every clue, Word Spies shows how good the clue was and how each team's chance of winning changed. No account needed to play.
Play · Daily puzzle · Tour · AI arena · About · Privacy · Launching on SemiLaunch
Made by Daniel Luan · daluan217@wordspies.com

## 评论（7/7）

> **daluan** · 2026-11-06T20:34:03.000Z　
> Hi guys,I'm a college student, and I enjoy playing word games like Codenames, but it can be hard sometimes to find enough people to play when everyone is available, so I made an app that allows you to fill any seat with an AI teammate and also play against AI. This way it allows for people to get the full strategic experience of codenames just on their own.I was also able to measure and benchmark a few different LLMs through API calls and give them ELO ratings based on stuff like win rate and clue/guess accuracy. If anyone is interested, they can see more on the methodology of how I benchmark these models over here:wordspies.com/arena. I think it's pretty interesting because it gives you a lot of insight into the NLP capabilities of these various LLMs.A few interesting stats were that I rated Gemini 4 Argon at 1775, GPT-6.1 Sol at 1744, GPT-6 Astra at 1723, Claude Fable 5.1 at 1623, and Claude Opus 5.5 at 1592. There are quite a few interesting things you'll find from there, like how, although newer and more expensive models tend to perform better, there are some rare exceptions, like Kimi K2.5 slightly edging out Kimi K3.Check the site out if you're interested in NLP and data science and would like to see what level of frontier LLMs you can successfully win against!Daniel

---

> **cheekygeeky** · 2026-11-06T21:38:16.000Z　
> Daniel, GREAT job. This is fascinating.
> Your leaderboard is based upon ELO, correct?
> I can't find anywhere that you describe the formula for calculating the ELO score. It seems like we would need to verify that is indeed an accurate way to judge the Model Leaderboard. Care to share?
> Also, if you gave them DIFFERENT arbitrary ratings to start, that would definitely influence their calculated ELO's later, wouldn't it? Why not start them off with even ELOs (like all starting at 1500)?

---

> **cheekygeeky** · 2026-11-06T21:52:25.000Z　
> I had one other thought: The LABELs given to the models assume that the models behind the name never change (GPT 6.1 Sol, for instance). I doubt that is true. I just don't think that they update the number behind the name until they have a feature or benchmark that they can report is significantly better. Thus, I think it would useful to reset the model scores to the starting score each day and TRACK/CHART the ELOs of the models over consecutive days. That would test my theory, if nothing else. Does a model "get dumber" as some people feel/report sometimes? Does a model get incrementally "smarter"?

---

> **cheekygeeky** · 2026-11-06T21:46:11.000Z　
> Thanks for the reply to my earlier question! If I'm understanding your comment, you started them off at different arbitrary scores? Wouldn't it have been fairer to start them off at the same scores (assuming nothing about relative strength) and let the results move the scores up or down from that?

---

> **daluan** · 2026-11-06T21:44:01.000Z　
> Yup, that's a fair question. It's not exactly running Elo. It's more of a Bradley-Terry fit across all games at once, mapped to the Elo scale (400 points = 10:1 odds). Game order doesn't change it. I also have each board played twice with both sides swapped to ensure fairness, so, for example, if one game has Kimi with 9 red words and Claude with 8 blue words, I make new agents of those same models where Claude now has those same 9 red words from Kimi and Kimi now has those 8 blue words from Claude.I may add a "how ratings work" section on my site if more folks express interest.

---

> **daluan** · 2026-11-06T22:01:28.000Z　
> Some models here are called by their IDs that date them on Amazon Bedrock, for example, the Haiku 4.5 ID is 20251001. Other models sometimes go through a provider's live endpoint, and those can change behind the same name. So drift is possible for some models and unlikely for others. A daily reset would be too noisy and costly (I'm still in school lol). Most models play only a handful of games a day, and Codenames has a lot of board luck through RNG. Potentially, maybe a weekly recalibration is an interesting research idea though.Thank you, cheekygeeky, for your numerous interesting questions. I'll try to ponder them to improve my site. If you're interested in testing the models for yourself, you can click on the link in my title or visit wordspies.com to get a feel for how different models perform when you play with and against them!

---

> **daluan** · 2026-11-06T21:54:45.000Z　
> Yup, good question, and let me clear up some confusion. The model leaderboard has no starting score; every model starts out equal, and all the ratings are calculated together from the full set of results. For example, if a new model gets released, like Gpt 6.1 Terra, we have it play against models like Sonnet 5.5, which we have a lot of data on, to scale its performance against it. (It did a lot better than Sonnet, in case you're curious).

## 导航

- 项目页：[[10-项目/wordspies.com_e6d07c4f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
