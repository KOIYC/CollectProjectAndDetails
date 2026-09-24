---
type: "corpus"
item_id: "07b433d88007f468"
title: "Show HN: Foremerge – Catch intent conflicts between parallel coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49789356"
project_url: "https://github.com/naw103/foremerge"
author: "naw103"
published_at: "2026-09-21T16:22:06Z"
captured_at: "2026-09-22T14:15:46+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_naw103
  - story_49789356
  - show_hn
metrics: {"points": 40, "comments": 11, "engagement_velocity": 40}
comments_count: 11
comments_total: 11
discovered_via: "hn:show_hn:3d"
---

# Show HN: Foremerge – Catch intent conflicts between parallel coding agents

> [!info] 一句话导读
> At, GPTree, we run several coding agents across our team on one repo using parallel worktrees. Apart from wasted time reviewing and fixing conflicts at PR time,…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49789356>
> 指标：点赞=40 · 评论=11 · engagement_velocity=40
> 作者：naw103　|　发布：2026-09-21T16:22:06Z
> 项目链接：<https://github.com/naw103/foremerge>
> 采集：2026-09-22T14:15:46+08:00　|　id：`07b433d88007f468`

## 正文

At, GPTree, we run several coding agents across our team on one repo using parallel worktrees. Apart from wasted time reviewing and fixing conflicts at PR time, the failures that hurt the most are when multiple plans or tickets cause architecture changes that cannot both be true. Ex. one agent replaces a class while another one is in the process of extending it. Git only notices if the resulting patches happen to touch the same lines and the review only catches it if they are familiar with both tickets.Foremerge is a local "git like" coordination layer that sits above git (ie. does not interact with or change the way git and worktrees function), Before editing each agent publishes an intent and the scopes it will change, with the operation it plans to complete on each one. foremerge intent publish --agent "$A" \
 --summary "Replace PaymentService with StripePaymentService" \
 --scope symbol:PaymentService=replace
 foremerge intent publish --agent "$B" \
 --summary "Add PayPal support to PaymentService" \
 --scope symbol:PaymentService=extend

The publish by the 2nd agent returns a HIGH destructive_vs_additive finding before writing any code. Agents keep their own worktrees and the shared state is one SQLite file in gits common direectory. No hooks, no merge drivers, nothing rewrites your history.It ships as one Rust binary with a CLI and MCP server with 18 tools and `foremerge setup all` wires it into Claude Code, Codex and Cursor. Because the protocol has nothing provider specific, a Claude agent and a Codex agent coordinate through the same store. Before any work is accepted, Foremerge runs a named check that you configured against the exact git state of the change. An agent that says tests pass is recorded but it dosnt satisfy the acceptance gate without running the check itself.Detection is deterministic, no judge model reading your code. HIGH conflicts are only asserted for declared operations, ie. matches inferred from prose cap out below high. Claims are advisory leases, not locks so two agents can still hold the same scope without deadlock. The open source version is single matching and so not a distributed consensus.We have tested this up to 98 parallel agents all working on the same repo with zero conflicts (was supposed to be 100 but 2 agents failed to run due to resource limitations)I replayed 76 intents on my own agents from a build last week in the order they happened. The sample had exactly 1 conflict (which was flagged) and the review found a blind spot where one agent claimed scope by class name and the other claimed it by an internal method. We are working on fixing that for the next release.Setup is a 30s install by pasting the quickstart instructions from the readme.md into your agent or manually:
`curl -fsSL https://foremerge.com/install.sh | sh` or `cargo install
--locked foremerge`, then `foremerge init && foremerge setup all` in a repo.
Apache-2.0.The feedback I want most is which conflicts between your agents plans would you actually want flagged and which would you tollerate as noise?Repo here: https://github.com/naw103/foremerge
Website: https://foremerge.comMore information on the problems this solves: https://foremerge.com/blog/

## 评论（11/11）

> **SrslyJosh** · 2026-09-22T00:19:55.000Z　
> [flagged]

---

> **ttoinou** · 2026-09-22T00:36:21.000Z　
> I'm curious to know what's everyone custom solution to this problem ? Before AI and with AI.It was already a problem for me before agentic AI coding : multiple developers can work on overlapping code and you always need someone to merge everything properly. Even if the overlap is very small it does add a burden to development. Not an issue anymore in 95% of cases if that person uses AI to solve conflicts, but now that "others developers" are swarm of AI agents, this problem isn't trivial to solve.

---

> **ttoinou** · 2026-09-22T00:37:10.000Z　
> Before editing each agent publishes an intent and the scopes it will change, with the operation it plans to complete on each one.
>
> But we don't know in advance what we will need to change in our current task. And even if we did, there are always side effects.

---

> **wilsprouse** · 2026-09-22T00:48:51.000Z　
> This is awesome. I think the current version control mechanisms are meant for humans, not agents. I'm still trying to think of a scenario where an agent needs to see a git diff. I think something like this could be the future of version control in an agent first world

---

> **naw103** · 2026-09-22T01:45:52.000Z　
> Here are some questions I normally get asked:What does an agent do with it?
> The agents publish intents and scopes of what they are about to change (at the start and right before they make the change if its something different). Foremerge returns a signal of related work already in progress on different worktrees (even across different branches or in the same worktree) and the agents/humans who are working on it. Agents can then negotiate on the solution prior to writing any code or generating any conflicts and Foremerge runs an acceptance check (defined by a human) prior to commit.Why advisory claims instead of locks?
> Once a repo gets busy locks turn into a queue and deadlocks. A lock that the agent cant see the reason for is the worse case scenario so the hard gate is at the acceptance not the start.What are the gaps?
> Ultimately Foremerge is deterministic (does not use any judge model) so it can detect some false positives and negatives though we see that very infrequently and worst case it would have likely of been missed anyway without Foremerge. Acceptance also dosnt currently compare the actual diff by default and there are no push notificiations so the earlier agent only learns about the conflict on its next status check (both of these are on the roadmap for the next version)There are more questions and answers here: https://foremerge.com/blog/31-questions-coordinating-paralle...

---

> **adityamishra241** · 2026-09-22T05:33:04.000Z　
> This is interesting. How do you decide whether a detected conflict is actually worth stopping the agent for? I imagine some overlapping changes could still be perfectly fine.

---

> **naw103** · 2026-09-22T01:15:39.000Z　
> I think before AI was writing most of the code and with small teams the solution was probably just ownership and talking (and meetings about meetings). Things moved at a pace where it was more possible to have someone oversee this, though I agree on larger teams it has always been a problem. I think Foremerge solves that too even without agents but the manual overhead outweighs more of the cost that it does with agents.
> Even if you can use AI to resolve the conflicts at PR time, you need the right context and you've already burned through tokens building and now even more fixing. Scale that across 10's or 100's of agents and you have a mess of each one running in its own direction.
> The custom solution for us became one worktree per task, and before an agent writes a line of code they lease/commit their intent and scope into an immutable log and verify drift as the acceptance check...thats now Foremerge

---

> **naw103** · 2026-09-22T01:23:43.000Z　
> You're right when the agent starts with a plan and no file list and the files only exist after edit, but the way I designed Foremerge to work, it works anyway. The initial intent does not have to be complete, it just has to be right about any destructive parts. That is why Foremerge works by declaring intent as prose, not as a file list or methods. The agents them selves determine if something conflicts based on the signals Foremerge returns. It only asserts a HIGH warning on declared scope and only a HIGH signal blocks acceptance (to avoid false possitives based on prose alone). The declaration can change at any point and the auto installed skills into the agents encourage such (the initial intent is released by the agent and the new intent is committed)

---

> **naw103** · 2026-09-22T01:07:43.000Z　
> Thanks! It' become a critical part of our development flow at GPTree since I built it back in Jan. So much so thats the reason I decided to open source it. I don't neccessarily see it as a replacement for version control, the diff is still doing most of the work at the point that really matters but Foremerge prevents those conflicts before you get to that point. Declared intent is what the agent thinks it will do and the diff is what it actually did, and the changeset being accepted currently depends on that diff.
> Where I definitely agree with you though is that not human or agent should be discovering a conflict by finding it in a diff. Its too late by that point and its the layer that git dosnt solve.

---

> **ttoinou** · 2026-09-22T01:47:34.000Z　
> I doubt this can really be deterministic, but maybe this is where Jev models can be useful

---

> **naw103** · 2026-09-22T02:03:00.000Z　
> You might be surprised, it works exceptionally well. If you decide to give it a shot and run into any issue feel free to reach out to me with any feedback.... and Jev is a sore point for me right now lol we have been training our own decision intelligence model, Corgen, for the last year and a half. We're already using it in GPTree but havn't released it to the public yet. Im actually in the process of running it against JevBench right now to see how it stacks up.

## 关联链接

- https://foremerge.com/blog/
- https://foremerge.com/install.sh
- https://foremerge.comMore

## 导航

- 项目页：[[10-项目/github.com_74913b77]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
