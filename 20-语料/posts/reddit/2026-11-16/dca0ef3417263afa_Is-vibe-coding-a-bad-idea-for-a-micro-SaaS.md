---
type: "corpus"
item_id: "dca0ef3417263afa"
title: "Is vibe-coding a bad idea for a micro SaaS?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xooolw/is_vibecoding_a_bad_idea_for_a_micro_saas/"
author: "Ecstatic_Comfort_139"
published_at: "2026-11-06T01:29:05+08:00"
captured_at: "2026-11-16T10:01:50+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-16"
pub_day: "2026-11-06"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 5, "comments": 15, "upvote_ratio": 1}
comments_count: 13
comments_total: 15
discovered_via: "reddit:14d+settle10"
---

# Is vibe-coding a bad idea for a micro SaaS?

> [!info] 一句话导读
> Let's say I have a problem to solve, but I'm still in the learning phase of coding. Should I perfect my coding skills before even starting to make the tool, or …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xooolw/is_vibecoding_a_bad_idea_for_a_micro_saas/>
> 指标：得分=5 · 评论=15 · 赞踩比=1
> 作者：Ecstatic_Comfort_139　|　发布：2026-11-06T01:29:05+08:00
> 项目链接：—
> 采集：2026-11-16T10:01:50+08:00　|　id：`dca0ef3417263afa`

## 正文

Let's say I have a problem to solve, but I'm still in the learning phase of coding. Should I perfect my coding skills before even starting to make the tool, or should I just vibe-code it? Also, let's say I have raw JS and HTML files. How does that convert from scripts to a final product, and where do I start "marketing" it for free?

## 评论（13/15）

> **kamscruz**（2 分） · 2026-11-06T01:59:18+08:00　
> Not a bad idea if you are a techie and understand everything going on behind the scene.

---

> **angelocastellani**（1 分） · 2026-11-06T02:11:04+08:00　
> Don't wait to perfect the coding, vibe-code a rough version and put it in front of a few real users first, since that tells you if anyone cares. For free marketing, find the 3 or 4 places where people already complain about the problem (subreddits, forums, Facebook groups) and answer questions there helpfully. When someone describes exactly the pain you solve, then mention the tool. Get a couple of devs to review security and data handling before you charge anyone though.

---

> **AttitudePossible5733**（1 分） · 2026-11-06T02:30:32+08:00　
> Vibe-coding is fine for a micro SaaS as long as you can read what it gives you, so keep learning on the side but don't wait to be good before you start. Build the smallest version that solves one problem and get it in front of people. Going from raw JS and HTML files to a real product mostly means putting them on a host like Vercel or Netlify, pointing a domain at it, and if you need logins or saved data, using a managed backend like Supabase instead of hand-rolling auth. For free marketing, find the places where people already complain about that exact problem and just help them there first.

---

> **PopKoren**（1 分） · 2026-11-06T03:41:42+08:00　
> Learning by shipping is fine if you assume the AI left holes. Keep credentials off the browser, enforce tenancy in code or policies, and log in as someone else before you advertise the product anywhere. My checker Rowly reports what guests can still open on that production site: https://rowly.me

---

> **Vast-Hunt-9484**（1 分） · 2026-11-06T04:18:46+08:00　
> raw html and browser js can already be a finished product if the job happens entirely on the user's device. the next step is static hosting, not necessarily adding accounts, a database and subscriptions. pick one input and one useful output, publish that version, then watch a few people try it with their own data. if it needs a secret api key or shared data, that part belongs on a server, not in the js you send to everyone's browser.

---

> **Loose-End-8741**（1 分） · 2026-11-06T06:24:12+08:00　
> It's all about the time frame:
> To START -> good idea
> To scale 10k+ active users -> meh
>
> It also depend on who are your clients, I work with corporate clients.
> An Vibe coded stuff don't pass security audits

---

> **EverydayLentils**（1 分） · 2026-11-06T10:32:15+08:00　
> Vibe code, but ask a lot of questions why Claude is doing certain things one way or what the tradeoffs to what was chosen.  You can just learn as you go with Claude.  As for marketing... good f-ing luck.  There is so much software being released now, it's hard to get anything noticed.

---

> **freedomchaserr**（1 分） · 2026-11-06T18:18:41+08:00　
> I think you shouldn't code by hand. This is a dying skill in many fields in my opinion. The current capabilities of AI are enough for most use cases and they are only getting better. You should focus on accurately analyzing and working out your requirements. Then you should understand the architecture of your product and the processes that bring it to life. Throughout the development you can heavily leverage AI to learn. My general workflow looks like this:
> 1. Work out requirements/features (This could be anything btw. security, load, just a feature of your app...)
> 2. Ask AI to implement it for me
> 3. Ask AI to review and understand the code it just created

---

> **No-Track-3259**（1 分） · 2026-11-06T18:20:42+08:00　
> I don't understand why people still hate vibe-coding. You should use computing or programming or advanced programming instead of this word and it will sound much more natural and much more valuable.
>
> The same like 30 years ago, there was a big difference between people who had their personal computer and knew how to handle and use PC mouse and the others who didn't know what is it...
>
> **so, use vibecoding as you use computer mouse - everywehere you want, the difference will be what you can do with this tool - the final outcome**

---

> **powleads**（1 分） · 2026-11-06T20:03:49+08:00　
> vibe-coding raw html and js files is totally fine to start. you can just throw it on vercel or netlify in two minutes. as for marketing, skip the broad socials early on and just find the exact 3 or 4 places where people complain about that specific problem. what feature are you building first?

---

> **Moniqu_Erickson**（1 分） · 2026-11-06T20:07:25+08:00　
> vibe coding is fine to validate an MVP, but don't wait to master programming before building. push those static JS/HTML files to vercel or netlify for free hosting, connect a simple backend like supabase if you need auth or a DB, and start free marketing on Reddit or X by sharing your build process in niche subreddits where your users hang out

---

> **TCKreddituser**（1 分） · 2026-11-07T00:51:12+08:00　
> In my opinion, vibe coding is best for people who already have a good understanding of coding. If you build an entire product through vibe coding without having a solid coding foundation, you'll eventually struggle when something breaks or needs fixing because you won't fully understand what's happening behind the scenes. But with that said, I also think vibe coding is perfectly fine for building a rough version of your idea, especially if it helps you stay motivated and actually get started. As for turning raw HTML and JS files into an actual product, you can start by hosting them using platforms like Vercel, Netlify, or GitHub Pages. These platforms let you deploy your code and make it accessible through a public URL. From there, you can connect a custom domain, add a backend or database if your product needs one. You don't need to have everything figured out from day one. Start with a working version and improve it as you go. For marketing, you can start by sharing your product on platforms like Reddit, Twitter, Indie Hackers, Product Hunt, and relevant Facebook or Discord communities. You can also create a simple landing page to showcase your product and easily share it with potential users. Some good options for that are Framer, Tiinyhost, and Lovable.

---

> **synthwave_saas**（1 分） · 2026-11-07T01:36:02+08:00　
> Vibe coding can't replace programming fundamentals, but it can get you reading a lot of code quickly and build a feel for how the pieces fit together. It also lowers the barrier to starting, which makes learning more fun. I'd use it to prototype, then understand the important code before adding authentication, payments, or real user data.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
