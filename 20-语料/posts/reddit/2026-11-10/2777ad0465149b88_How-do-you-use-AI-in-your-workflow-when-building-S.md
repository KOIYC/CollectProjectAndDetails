---
type: "corpus"
item_id: "2777ad0465149b88"
title: "How do you use AI in your workflow when building SaaS?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xjqz81/how_do_you_use_ai_in_your_workflow_when_building/"
author: "Finite8_"
published_at: "2026-10-31T04:49:09+08:00"
captured_at: "2026-11-10T09:52:20+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-10-31"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 3, "comments": 15, "upvote_ratio": 0.6666666666666666}
comments_count: 13
comments_total: 15
discovered_via: "reddit:14d+settle10"
---

# How do you use AI in your workflow when building SaaS?

> [!info] 一句话导读
> Hi, I'm not very knowledged in AI tools besides using chatbots like Claude and Chat GPT to generate some code or debug. I would like to know what are the ways a…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xjqz81/how_do_you_use_ai_in_your_workflow_when_building/>
> 指标：得分=3 · 评论=15 · 赞踩比=0.6666666666666666
> 作者：Finite8_　|　发布：2026-10-31T04:49:09+08:00
> 项目链接：—
> 采集：2026-11-10T09:52:20+08:00　|　id：`2777ad0465149b88`

## 正文

Hi, I'm not very knowledged in AI tools besides using chatbots like Claude and Chat GPT to generate some code or debug. I would like to know what are the ways and tools you use and which ones are a must to learn especially regarding AI agents or things that speed up your work.

[](https://www.reddit.com/submit/?source_id=t3_1xjqyyq&composer_entry=crosspost_prompt)

## 评论（13/15）

> **Brufacee**（1 分） · 2026-10-31T04:52:11+08:00　
> I'd start with one repeatable task before setting up agents. For SaaS marketing, feed in real customer calls or support messages and use AI to group objections, draft a few ad or landing-page angles, then check every claim against what users actually said. That saves time without letting a chatbot invent your positioning.

---

> **patryk_builds**（1 分） · 2026-10-31T05:04:23+08:00　
> Biggest jump for me was going from chatbot to an agent that works directly in the project folder (claude code in my case). it reads the code, runs the tests, fixes what breaks, and you review instead of copy-pasting.Two things that made it actually work:A plan file in the repo with stages and checkboxes. the agent reads it at the start of every session, so it never loses track of where you are.A rules file [CLAUDE.md](http://CLAUDE.md) or similar stack, conventions, "never put keys in code", "run tests before saying done". saves you repeating yourself every time.The skill worth learning isn't prompting, it's reviewing. the agent is fast, but you still need to tell when it built the wrong thing

---

> **Own_Tension2711**（0 分） · 2026-10-31T05:13:14+08:00　
> Gotta say, pinning down one repeatable task first is the move. Everyone jumps straight to agents but half the time they're optimizing a process that doesn't even exist yet.
>
> I did something similar with customer support tickets, just fed them through to spot patterns in the complaints. Cut my debugging time way down since I knew exactly what kept breaking before users even reported it.

---

> **lazyEmperer**（1 分） · 2026-10-31T05:22:34+08:00　
> The jump from pasting code into a chatbot to running Claude Code in the terminal was the biggest change for me. It reads the whole repo, runs the tests and fixes what breaks, so I describe a feature and review the diff instead of copying snippets back and forth
>
> Skip the agent frameworks for now, they mostly add setup without saving much time early on

---

> **Finite8_**（0 分） · 2026-10-31T05:32:41+08:00　
> can you do it with the free tier?

---

> **Finite8_**（0 分） · 2026-10-31T05:35:26+08:00　
> does claude do that with the free tier?

---

> **Huge_Pool7424**（2 分） · 2026-10-31T05:35:59+08:00　
> a lot of the cli tools have free tiers but you'll hit the limits fast on a real repo. cheap api keys with a spend cap are usually the better way to start.

---

> **Brufacee**（0 分） · 2026-10-31T06:05:59+08:00　
> That's a useful example. Did the raw ticket text surface the pattern, or did you have to group tickets by feature first?

---

> **Musa_S2**（0 分） · 2026-10-31T07:12:22+08:00　
> the biggest jump for me was moving from pasting code into a chatbot to using a tool that works inside the project, like claude code or cursor. it can read your whole codebase, so it stops guessing
>
> a few things that help: keep a short notes file in the repo explaining how the project is set up, give it small tasks instead of “build this whole feature,” and always read what it wrote before you accept it
>
> for agents, i’d learn one tool properly before adding more. what are you building right now?

---

> **Finite8_**（0 分） · 2026-10-31T07:42:42+08:00　
> For now I'm just learning but I wanted to understand what I should focuse more since AI can already do a lot.

---

> **Big_Measurement9248**（2 分） · 2026-10-31T11:20:14+08:00　
> others covered claude code, which is the right first step. couple things that made it click for me:
>
> - keep a short rules file in the repo (CLAUDE.md or cursor rules) with your stack, folder layout and the stuff it keeps getting wrong. saves repeating yourself every session
> - ask for small changes and actually read every diff. if you can't explain what it changed, don't merge it
> - when something breaks paste the real error and the file, not a description of it
> - use it outside code too. changelogs, replying to support emails, turning user feedback into a list of issues
>
> i wouldn't bother learning agent frameworks yet. get good at one coding agent first

---

> **AutoModerator**（1 分） · 2026-10-31T18:51:59+08:00　
> Low-Effort/AI content is auto-removed.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **Musa_S2**（1 分） · 2026-11-02T09:13:40+08:00　
> To be honest a lot of the things you can do involve looking at your day-to-day life and determining what you think can be automated or done differently using AI. I know that sounds very vague but I always try to build with AI towards a real use case instead of just learning the tool.
>
> I'd make demos for actual problems and have a real target for what the build needs to be based on. I say start with a tiny version that works and add to it, and test it on really messy data early because that's where most things are going to break. Don't wait for it to look good. Don't wait for the perfect kind of thing. Just ship the rough version and fix it from there

## 关联链接

- https://www.reddit.com/submit/?source_id=t3_1xjqyyq&composer_entry=crosspost_prompt

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
