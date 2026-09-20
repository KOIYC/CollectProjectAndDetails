---
type: "corpus"
item_id: "430139e24f9ef639"
title: "Which AI builder have you actually used to ship a project?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/EntrepreneurRideAlong/comments/1w3arbs/which_ai_builder_have_you_actually_used_to_ship_a/"
author: "Crypton228"
published_at: "2026-08-31T19:16:40+08:00"
captured_at: "2026-09-21T03:05:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/EntrepreneurRideAlong
  - Seeking Advice
metrics: {"score": 3, "comments": 15, "upvote_ratio": 1}
comments_count: 20
comments_total: 20
discovered_via: "reddit:52d+settle3"
---

# Which AI builder have you actually used to ship a project?

> [!info] 一句话导读
> I've been curious about how founders are actually using AI builders beyond quick prototypes.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/EntrepreneurRideAlong/comments/1w3arbs/which_ai_builder_have_you_actually_used_to_ship_a/>
> 指标：得分=3 · 评论=15 · 赞踩比=1
> 作者：Crypton228　|　发布：2026-08-31T19:16:40+08:00
> 项目链接：—
> 采集：2026-09-21T03:05:38+08:00　|　id：`430139e24f9ef639`

## 正文

I've been curious about how founders are actually using AI builders beyond quick prototypes.

If you've used Lovable, v0, Bolt, or Replit Agent to build something real, which one did you use?

What were you building, and did the project actually make it to a usable or launched state?

I'm especially interested in hearing from people who have shipped something with one of these rather than just experimented with it for a few hours.

## 评论（20/20）

> **External-Bite-3436**（1 分） · 2026-08-31T19:26:02+08:00　
> used replit agent for a client dashboard that pulls data from a few sheets and shows basic charts, nothing crazy but it's live and they use it every week
>
> the first version took like two afternoons, most of the time was fixing how it handled edge cases not the actual building
>
> curious if anyone has shipped something customer-facing with bolt, that one feels more frontend-focused to me

---

> **Crypton228**（1 分） · 2026-08-31T19:46:28+08:00　
> What happened to the project after you shipped the first version? Did you keep iterating on it in Replit Agent?

---

> **Bitter_Regular7406**（1 分） · 2026-08-31T20:19:02+08:00　
> used bolt for muvi's landing page, got it to a shippable state in like a day but then spent another week fixing weird css bugs it introduced lol

---

> **lucien_han**（1 分） · 2026-08-31T21:26:52+08:00　
> Used Codex, WorkBuddy, AnyCap and Spira.ai. Not exactly the same category as Lovable/Bolt, but my takeaway has been: the first demo is the easy part now.
>
> The real test is what happens when you come back on day 2 and need to change the logic, fix edge cases, or understand what the agent actually did.
> Codex has been my pick when I care about control and maintainability. WorkBuddy makes more sense to me for multi-step/agentic workflows. AnyCap/Spira I use more on the creative production side.
>
> I’ll take “boring but debuggable” over “holy shit it built it in 20 minutes” every time.
>
> Would love to know which of these builders people are still happy with a month after shipping.

---

> **Crypton228**（1 分） · 2026-08-31T21:52:33+08:00　
> If you went back to one of them today, what would have to be different?

---

> **kadesh1274**（1 分） · 2026-08-31T21:59:37+08:00　
> I returned to development after roughly 20 years and used GitHub Copilot to build and launch a real production website.
>
> It’s a corporate-accountability database built with Next.js, Supabase and Vercel, containing thousands of company profiles, evidence records, scoring, moderation, search and dynamic pages.
>
> Copilot has been surprisingly capable, especially when I give it a small, tightly scoped task with clear acceptance criteria and required tests. It has helped me build features, write SQL, fix routing problems and improve SEO.
>
> But I would not trust it unsupervised. Broad prompts often produce changes that are much larger than necessary, and a fix in one area can quietly break something elsewhere. I now insist on narrow pull requests, focused tests, type-checking and preview validation before merging anything.
>
> My conclusion is that AI can absolutely help a non-current developer ship a real product—but it does not remove the need to understand the system, review the diff and test the result. The first implementation is usually the easy part. Maintaining and safely changing it is the real test.

---

> **Ilheet-Matas**（1 分） · 2026-09-01T00:19:32+08:00　
> Built a quick lead scraper with Claude's API last month - honestly shocked how little code I actually had to write myself. Tried a couple no-code AI builders first but they felt too locked-in for what I needed.

---

> **Competitive_Tune_590**（1 分） · 2026-09-01T01:53:23+08:00　
> if you end up shipping something with one of those, getting it listed in a directory like launchpact can help with seo and backlinks — might be worth a look once it's live.

---

> **Dizzy_Plate2448**（1 分） · 2026-09-01T09:28:17+08:00　
> Personally use Claude to ship most things. Already have it set up - and for me it's quick and simple enough to use.

---

> **lucien_han**（1 分） · 2026-09-01T13:14:18+08:00　
> Honestly, I’d go back if it could survive week 3, not just win minute 20.
>
> Most AI builders are insanely good at the honeymoon phase: “holy shit, it built my app.”
>
> Then you ask it to change one thing two weeks later and suddenly it’s renovating the kitchen, deleting a wall, and forgetting why the bathroom exists.
>
> What I’d want: persistent project memory, clear diffs, reliable rollback, and much better respect for existing architecture.
>
> I don’t need more magic. I need fewer surprise renovations.

---

> **akl773**（2 分） · 2026-09-01T18:43:54+08:00　
> Bolt for a landing page, then Claude for anything with a database behind it. What caught me both times was the schema, first one wrote the tables with no foreign keys at all and I only found out when deleting a customer left their orders sitting there.

---

> **Crypton228**（1 分） · 2026-09-01T21:56:16+08:00　
> Was the wall a feature it did not have, or the code it was producing?

---

> **lucien_han**（1 分） · 2026-09-01T22:34:56+08:00　
> Mostly the code.
>
> I’m fine with it adding a wall if I asked for a wall. What drives me insane is asking it to repaint the wall and coming back to find the kitchen has moved.
>
> That’s basically been my experience with a lot of AI builders 😂

---

> **JGoillot**（2 分） · 2026-09-02T15:44:17+08:00　
> I think it's a scoping issue: try to bill the extra time you spend communicating. Also try to communicate the progress every day so he's fully awre of everything that's being done. And make them pay more if they want it done faster.

---

> **Crypton228**（1 分） · 2026-09-03T00:30:54+08:00　
> Did you export the code from those builders, or did you start the project again with Claude?

---

> **Crypton228**（1 分） · 2026-09-03T00:31:29+08:00　
> What did you move to afterwards, and did that actually solve the problem?

---

> **Crypton228**（2 分） · 2026-09-03T00:31:40+08:00　
> Do you still use Claude for anything smaller, or mostly for shipping full projects?

---

> **Dizzy_Plate2448**（1 分） · 2026-09-03T05:53:04+08:00　
> I use Claude for both full and small projects. It's already integrated into my workflow so it's most convenient for me, and I find it to be beyond capable for most tasks.

---

> **akl773**（2 分） · 2026-09-03T16:55:02+08:00　
> Didn't move off it, just stopped letting it design the schema. I write the tables and the constraints myself first and let Claude build against them. Foreign keys have been fine since, what still slips through is a unique constraint across two columns.

---

> **stealthagents**（1 分） · 2026-09-09T02:54:51+08:00　
> Used Replit Agent to build a small personal finance tool that tracks expenses and suggests budget cuts. It ended up being pretty functional, and I even launched it on Product Hunt. The collaboration features were a game changer for tweaking things with friends during development.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
