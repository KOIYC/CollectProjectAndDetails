---
type: "corpus"
item_id: "cc62be64eb4a0707"
title: "What's your current AI setup?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wg75vs/whats_your_current_ai_setup/"
author: "chasingfreedomm"
published_at: "2026-09-14T23:49:39+08:00"
captured_at: "2026-09-24T23:59:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-24"
pub_day: "2026-09-14"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 5, "comments": 12, "upvote_ratio": 1}
comments_count: 20
comments_total: 20
discovered_via: "reddit:14d+settle10"
---

# What's your current AI setup?

> [!info] 一句话导读
> Since the AI hype I only casually kept myself up to date. I was of the opinion that instead of trying out all the tools and finding the best method I could just…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wg75vs/whats_your_current_ai_setup/>
> 指标：得分=5 · 评论=12 · 赞踩比=1
> 作者：chasingfreedomm　|　发布：2026-09-14T23:49:39+08:00
> 项目链接：—
> 采集：2026-09-24T23:59:03+08:00　|　id：`cc62be64eb4a0707`

## 正文

Since the AI hype I only casually kept myself up to date. I was of the opinion that instead of trying out all the tools and finding the best method I could just focus on the result I wanted and build it with what I know. I still hold that opinion to some degree, but AI is a much larger part of my developing experience now and I feel like I could be much more efficient. So I would like to know what setups are out there. Is there an industry standard? I currently just use the Cursor IDE. I plan with Claude and execute with Grok and review all of the code. I think I am missing out on stuff like Skills, MCP, using multiple agents at once...

## 评论（20/20）

> **TRO_KIK**（2 分） · 2026-09-15T00:34:22+08:00　
> The popular CLI clients are all very, very good. I'm easily well inside the top 1% of AI users and nearly all of my development uses out-of-the-box features. I just put a very basic, very high level outline of my project in [CLAUDE.md](http://CLAUDE.md) (and configure Codex to use that for its AGENTS.md) and ask for stuff. Moderatly parallel, usually at least active 5 sessions. They all have scripts where they can loop against reviewers until reasonably clean.
>
> Only really custom bit I have is a Discord bot with full AWS read access plus some reasonable standard ops. Granted it does a lot, one @ can take a bug through analysis, fix, coverage, live testing, review loop, and PR in my inbox + fix in staging. But it's really nothing the local clients can't do.

---

> **rasmus_98**（2 分） · 2026-09-15T00:37:16+08:00　
> The thing you're missing isn't more models, it's context. I keep a repo level CLAUDE.md with our stack and conventions, plus a short spec file per feature, and that beats any model swap. MCP only pays off when it touches something real like your DB or staging logs, otherwise it's just another config to maintain. Skip multi agent for now, most setups I've seen burn tokens arguing with themselves.

---

> **AutoModerator**（1 分） · 2026-09-15T01:04:06+08:00　
> Your comment was removed. Links in comments require to gain karma first in r/SaaS. Earn sub karma by commenting helpfully first.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

---

> **Cloutro**（2 分） · 2026-09-15T03:12:08+08:00　
> The biggest problem with running several agents isn’t choosing the models; it’s preventing each one from becoming a separate silo.
>
> I’d optimize for shared context: humans and agents should be able to see the same task discussion, ping the right participant, inspect what happened, and approve the next action without copying context between five tools. Otherwise the coordination cost eats the productivity gain.

---

> **kagein12**（2 分） · 2026-09-15T06:23:21+08:00　
> You already have a plan/build/review loop. I'd add tools around whichever part feels slow, rather than rebuild the whole setup. If you're repeatedly copying information into the chat, a direct connection to that source might be the useful next step.

---

> **EnoughHoning**（2 分） · 2026-09-15T09:40:01+08:00　
> Cursor plus MCP covers most of it, and skills help once your prompts repeat. For mapping the workflow itself, I just use Venngage and move on.

---

> **chasingfreedomm**（1 分） · 2026-09-15T15:51:46+08:00　
> What do you connect with MCP? What is Vennage?

---

> **chasingfreedomm**（1 分） · 2026-09-15T15:53:21+08:00　
> Could you explain in detail how the 5 parallel sessions work? I usually work on one issue with one session and I wouldn‘t even know how and where I can use another agent

---

> **chasingfreedomm**（1 分） · 2026-09-15T15:57:11+08:00　
> How exactly do you work with the spec files?

---

> **TRO_KIK**（2 分） · 2026-09-15T22:20:27+08:00　
> Second terminal tab, git worktree, symlinking any gitignored stuff into each.

---

> **chasingfreedomm**（1 分） · 2026-09-16T16:17:11+08:00　
> Thanks!

---

> **No_Stretch433**（0 分） · 2026-09-17T01:29:58+08:00　
> Claude, OpenClaw, Google for nano banana🍌, brave api for search. And forge magery to sleep well

---

> **rasmus_98**（2 分） · 2026-09-17T09:19:21+08:00　
> I write them by hand before touching code, one file per feature, kept in the repo next to the code so the model reads it on every pass. It states the goal, the files involved and what done looks like. Half the value is me thinking it through, the model just stops guessing.

---

> **chasingfreedomm**（1 分） · 2026-09-17T16:15:39+08:00　
> That’s an interesting approach I haven’t heard about yet. Thanks for the insight!

---

> **Common_Dream9420**（1 分） · 2026-09-20T09:24:44+08:00　
> Claude Code plus Cursor is where I landed after trying a bunch of combinations. Claude Code handles the longer reasoning tasks and anything where I need it to hold context across files, Cursor fills in the day-to-day autocomplete and quick edits. MCP is worth looking into but honestly the ROI depends on what you're building, don't add it just to add it. The multi-agent stuff is still pretty rough in practice unless you have clear task boundaries. Biggest unlock for me wasn't the tools, it was getting better at writing tight specs before handing anything to the agent.

---

> **chasingfreedomm**（1 分） · 2026-09-20T22:19:43+08:00　
> This was basically also my setup and I think I will just stick with it. After reading all the comments it seems that much of the hype is not worth it.

---

> **Common_Dream9420**（1 分） · 2026-09-20T22:22:17+08:00　
> Curios what are you building h with agents !!

---

> **chasingfreedomm**（0 分） · 2026-09-20T23:41:14+08:00　
> Just yesterday my project went live: [SponsorZone](https://sponsorzone.dev)

---

> **Common_Dream9420**（1 分） · 2026-09-20T23:49:09+08:00　
> how does it work? are you using agents to act/execute/decide? if yes how are you validating them?

---

> **chasingfreedomm**（0 分） · 2026-09-21T00:49:08+08:00　
> There is no active agent involvement in the live product. I purely used them to build the project and now to market it. My workflow was mostly planning out with Claude and executing with Grok. Then i would review the code and commit. For UI stuff I sometimes skip the review and for risky endpoints I make sure to understand it fully. I also did a security check on the entire project before going live using this skill: [https://gist.github.com/logicx24/2a491f29bf662d3e04fe1713b1757729#file-vibecoder-review-md](https://gist.github.com/logicx24/2a491f29bf662d3e04fe1713b1757729#file-vibecoder-review-md)

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
