---
type: "corpus"
item_id: "d4bd3cad1d5b8971"
title: "Show HN: Beat – a to-do list that completes its own tasks"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50551356"
project_url: "https://gobeat.ai/auth/login"
author: "brdo"
published_at: "2026-11-18T20:01:45Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_brdo
  - story_50551356
  - show_hn
metrics: {"points": 12, "comments": 5, "engagement_velocity": 12}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:3d"
---

# Show HN: Beat – a to-do list that completes its own tasks

> [!info] 一句话导读
> videos security learn more

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50551356>
> 指标：点赞=12 · 评论=5 · engagement_velocity=12
> 作者：brdo　|　发布：2026-11-18T20:01:45Z
> 项目链接：<https://gobeat.ai/auth/login>
> 采集：2026-11-19T09:43:31+08:00　|　id：`d4bd3cad1d5b8971`

## 正文

Beat BETA by CXAI
 videos security learn more
 An AI agent for the work that waits on you
 Everything waiting on you, already drafted.
 Beat connects to the tools you already use, finds what needs you, and drafts the next step. You approve, and it's done.
 Today: PR reviews, ticket questions and meeting follow-ups across Jira, GitHub, Slack and your notetaker.
 Play Beat drafting a PR review, approved and posted to GitHub.
Sign in to Beat
 Sign in with Google or
Email Password Sign in Forgot your password? Ask the person who invited you.
 Free during the beta. Paid plans start January 1, 2027. We ask for honest feedback in a short weekly check-in.
 1 Sign in with Google
 2 Connect GitHub, Jira, Slack, Granola or Google Meet. Only the ones you want; all of them take a few minutes.
 3 Drafts appear in your queue as work lands on you
 Your workspace admin approves Beat once per tool. By signing in you agree to the privacy policy .
Security
 Before you connect anything
 Nothing posts without you Every review, ticket, comment and Slack message waits for your approval.
 We never store your code It's read transiently for the review, then dropped.
 Not used for training Your data doesn't train AI models. Encrypted in transit and at rest.
 Your queue is yours Your manager can't see what you approve or dismiss.
Prompt injection can't act through Beat: the worst a hidden instruction in a PR can do is change a draft you read first. Hosted by
 CXAI on Google Cloud. Full security details
 Proof
 Recorded by the engineers who build it
 code review · real PR
 BugBot passed it twice. Beat found the bug. Why our engineering team replaced Cursor BugBot with Beat.
 watch
 meeting to action
 The meeting ended. The tickets exist. Right board, right assignee, and a comment instead of a duplicate when the ticket already exists.
 watch
 privacy
 How Beat handles your code See exactly what Beat accesses in GitHub, and why none of it is kept.
 watch
More: Copilot vs. BugBot vs. Beat on the same PR · Jira ticket analyzer · Why Beat beats a personal agent setup
 Questions
 Quick answers
 Does Beat act on its own? No. Every draft waits in your queue until you approve, edit or dismiss it.
Why not just use Claude or ChatGPT? Keep using them; we do. They answer when you ask and bring the context. Beat starts before you ask, the moment a ticket is assigned, a PR opens or a meeting ends, and it works the same way for everyone on your team.
Do I need my whole team on it? No. It's useful on your own from day one, and it compounds when your team joins: what you approve lands in the next person's queue.
Does Beat write code? No. It reviews pull requests and drafts tickets, comments and messages. Your coding assistant writes the code.
What does it cost? Free during the beta. Paid plans start January 1, 2027, and beta users hear about pricing first.
More questions answered at cxapp.com/beat .
 Beat is a product of CXAI (Nasdaq: CXAI) cxapp.com/beat privacy © 2026 CXApp, Inc.

## 评论（5/5）

> **brdo** · 2026-11-18T20:01:53.000Z　
> Hi HN, I’m Brendan.We were originally building a completely different product (an office workplace app: desk booking, food ordering, etc.) and built Beat internally to keep up with our own work. It ended up being the thing we used most. What we actually cared about was whether our work got done on time, and whether we were the ones blocking the team. So I figured you guys might like using it as well.Beat starts working the moment something is assigned to you and gets put in your to-do. It handles your PRs, meeting notes, Jira tickets, and you just approve.The code review tools we tried either missed real defects or overclaimed false positives, so I've really been focusing on providing high quality code reviews on every single commit, not just commit diff, but running against entire repos, and I would really love if you guys would try it out and give me some feedback on how it feels.It’s a totally free beta, open to anyone with a Google account.

---

> **saaaaaam** · 2026-11-18T22:39:05.000Z　
> I’m curious why you think anyone would trust this obviously vibe coded app to the point they share data with it? That’s a genuine question. I read this completely incomprehensible but of text about security and thought “absolutely not”.> Prompt injection can't act through Beat: the worst a hidden instruction in a PR can do is change a draft you read first. Hosted by CXAI on Google Cloud. Full security detailsLike, what does that even mean? That is not any sort of English as she is wrote.Edit: Good grief. You are apparently a nasdaq listed company. What on earth? (Albeit it one that peaked at $692.50 a share in 2023 and is now trading at $1.25 a share…)

---

> **brdo** · 2026-11-18T23:14:54.000Z　
> Great point Sam, I sent the "vibed" feedback to our UI person hahaBut it's a great point on data and privacy and it's one that I am personally proud of. We do NOT store any data, we do not train, we do not sell, we don't distribute any data. We are a fully SOC II compliant company. I'm an old-school dev, so I understand where you're coming from entirely.It's good to know that the wording is not clear, the wording WAS almost entirely vibed. We have been building this product to help build our core products, and didn't particularly care about messaging, or coherence, so I do appreciate the feedback and will work on changing that.The point on hidden instructions is about "open" agents and their ability to do things outside of the intended instruction. Beat does NOT behave like a traditional "open" agent, it simply CAN'T run outside of it's intended scope.Yes, we are a nasdaq listed company. This is not our core product. Like I mentioned this is an internal tool, that we have found to be very useful, so I decided to see if others would find value in it.

---

> **nathancahill** · 2026-11-19T00:07:47.000Z　
> "UI person"

---

> **brdo** · 2026-11-19T00:33:22.000Z　
> LOL! It's true... Figma and allIf you're referring to the login page, then that makes sense. That's what I was saying was just vibed for this. The actual app looks nothing like the login.Do you think the actual app is vibed? Or did you mean the login page? Would appreciate the feedback

## 导航

- 项目页：[[10-项目/gobeat.ai_3441281c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
