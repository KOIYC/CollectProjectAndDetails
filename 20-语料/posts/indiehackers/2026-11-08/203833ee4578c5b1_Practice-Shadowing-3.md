---
type: "corpus"
item_id: "203833ee4578c5b1"
title: "Practice Shadowing 3"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/practice-shadowing-3"
project_url: "https://practiceshadowing.com/"
captured_at: "2026-11-08T12:54:09+08:00"
lang: "en"
kind: "project"
topic: "开发者工具"
shard: "2026-11-08"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Practice Shadowing 3

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/practice-shadowing-3>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://practiceshadowing.com/>
> 采集：2026-11-08T12:54:09+08:00　|　id：`203833ee4578c5b1`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Vibe Coding Tools Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
Practice Shadowing
 English shadowing practice that waits for you
Visit Website
Practice Shadowing English shadowing practice that waits for you
 Post 1
 Website
November 7, 2026
 Show IH: Shadowing app for English learners
Hi IH, I'm the maker of Practice Shadowing ( https://practiceshadowing.com ). It launched on 18 October and is free while I find out whether people use it.
 What it does?
 Shadowing means repeating what a speaker says straight after them. Most players make you pause by hand. This one plays one sentence, waits until you have finished saying it, then goes on. The words you say light up as you speak, and you can play your attempt next to the speaker's. Sample clips at three levels need no account. With a free account you can use your own audio, a podcast or a YouTube video with captions. The screens are in English and Vietnamese, because my first market is Vietnamese learners of English.
 What building it taught me?
 Knowing when someone has finished speaking is the whole product. Early on the app talked over people, for example when they stopped for breath. It took ten separate fixes and tests that replay real sentences with simulated learners, pauses and room echo. A pause of about 1.2 seconds mid-sentence still ends a turn, and I'm still tuning that.
On Android, the browser's speech recognition hears nothing while the page is recording. So phones stream their recording to a speech model on Cloudflare, and computers use the browser's own recognition.
Brave has the speech recognition API but not Google's service behind it, so it fails with a network error. It now falls back to the same stream as phones.
Synthetic voices lie. The first version of the word highlighting passed every test with macOS voices, and my own voice found it awful. Every voice feature now gets a test with a real person before release.
The stack is small on purpose: one Cloudflare Worker serves the site and the API, the front end is plain JavaScript modules with no bundler, and the data sits in Cloudflare's SQLite (D1).
Where it is?
 Two weeks in. A small Google Ads test in Vietnam has been running since late October. [Optional: a number or two, such as visitors so far and how many practised a sentence.] No revenue yet.
 What I'd love feedback on:
 Does the waiting feel right with your voice and your microphone?
Is it clear on the first visit what to do?
If you have built something for language learners: where did your first users come from, apart from ads?
Andrew Williams
5 Upvotes
Comment
About
 Shadowing means repeating what a speaker says straight after them, copying their sounds and rhythm. It is a well-known way to practise speaking, but with an ordinary player you keep stopping and rewinding by hand.
People
 Andrew Williams Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 关联链接

- https://practiceshadowing.com

## 导航

- 项目页：[[10-项目/Practice-Shadowing-3_e53e3244]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
