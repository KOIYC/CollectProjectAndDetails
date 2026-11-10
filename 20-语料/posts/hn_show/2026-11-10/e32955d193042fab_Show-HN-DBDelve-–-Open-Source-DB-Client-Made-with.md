---
type: "corpus"
item_id: "e32955d193042fab"
title: "Show HN: DBDelve – Open-Source DB Client Made with Rust and GPUI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50427934"
project_url: "https://github.com/ShayanAbbas1/dbdelve"
author: "shayan_abbas"
published_at: "2026-11-09T16:36:38Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_shayan_abbas
  - story_50427934
  - show_hn
  - front_page
metrics: {"points": 94, "comments": 33, "engagement_velocity": 94}
comments_count: 33
comments_total: 33
discovered_via: "hn:show_hn:3d"
---

# Show HN: DBDelve – Open-Source DB Client Made with Rust and GPUI

> [!info] 一句话导读
> Hi HN, I’m Shayan and a few months ago I started building a DB Client DBDelve with a focus on performance and just making something that feels good to use (in t…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50427934>
> 指标：点赞=94 · 评论=33 · engagement_velocity=94
> 作者：shayan_abbas　|　发布：2026-11-09T16:36:38Z
> 项目链接：<https://github.com/ShayanAbbas1/dbdelve>
> 采集：2026-11-10T09:49:42+08:00　|　id：`e32955d193042fab`

## 正文

Hi HN, I’m Shayan and a few months ago I started building a DB Client DBDelve with a focus on performance and just making something that feels good to use (in the spirit of Zed, Ghostty, and other tools that just feel pleasant to use).For my workflow I’ve always looked for performance, especially since some time ago I had a really outdated machine and any kind of bloat was really noticeable, I remember using DBeaver and it just crashing on me multiple times, I also had to use postGIS which just made it worse. I migrated all my essential dev tools to use the ones with performance in mind (Zed, Ghostty etc) but the only thing that was missing was DB Client. The main choices everyone has are DBeaver which is a memory hog and an overkill for most of the tasks imo. The other options like Datagrid, Beekeeper, TablePlus are either electron based so bloated and memory hogs or paid and closed-source.DBDelve 0.3.6 against DBeaver 25.3.1 on the same Postgres table, median of 5 runs each (2026-10-11, M1 Pro, 32 GB). Times are from the action to the rows rendered. DBDelve DBeaver
 Launch 1.1 s 5.2 s
 Idle memory 133 MB 606 MB
 1,000-row query 0.21 s 1.96 s
 1M rows, time 56 s 208 s
 1M rows, memory [1] 4.9 GB 17 GB

[1] The whole 1M-row, 100-column table pulled into memory on purpose, with the row limit off. Not a normal use case; DBeaver's heap limit had to be raised manually for the benchmark.Scrolling perf with 1 million rows loaded with 100 columns each: https://youtu.be/V2MOhJYFqIEIt has most of the features most devs would need for 90% of their workflow plus some more I thought would be a nice touch:
Readonly, read-write and Full Access modes
Glass themes (If you’re into them, I am)
Keyboard focused with every keybinding customizable
Organization of connections into projectsMe and some other folks have been daily driving it for more than a month now and most good feedback comes on it having a really simple UI to navigate, very stable for its age and the performance of course. I’m also sharing here because those people tell me this has potential to grow so I’m trying my hand at distributing it.Just want to give a huge shoutout here to the Zed team for GPUI, it's a breeze to work with if you just get through them not updating the crate officially on crates.io but the community has found the solutions for it, you just have to dig deep for it. It performs extremely well and just the HTML-like structure of it, makes it easy to understand for someone from a web dev background and agents are very good at writing it too. GPUI component also solves a lot of problems with having a good component library we can use. I think for anyone starting a GPUI project now, GPUI-kit makes a lot of sense, it just bundles GPUI, GPUI-component together and has some optimizations adding retained mode which is experimental but could provide a lot of benefit, so think all things considered it should be the default way.The major optimization I did was just lowering the memory overhead by using packed rows which reduced the memory usage by 40% on large datasets (8.1GB to 4.9GB on a 4GB table loaded in app), everything else came bundled in with Rust and GPUI mostly or they just made it very easy.Limitations:
It's not signed and notarized, identity verification from apple's side has been a nightmare but it should be signed soon.
Don’t expect feature parity with more mature clients for now, the general direction of this right now is the zed way of adding features in but after making sure the core workflows are done with a high quality.Do give it a try, you can import your connections from dbeaver and tableplus.https://github.com/ShayanAbbas1/dbdelve

## 评论（33/33）

> **written-beyond** · 2026-11-09T17:56:05.000Z　
> What about beekeeper studio?

---

> **edstarch** · 2026-11-09T18:13:43.000Z　
> >it's a breeze to work with if you just get through them not updating the crate officially on crates.io but the community has found the solutions for it, you just have to dig deep for itwhat does this mean?the ui does look very nice

---

> **dofm** · 2026-11-09T18:13:46.000Z　
> Oh this is good news — I have been looking for a fuss-free cross-platform alternative to MySQL Workbench to recommend for a data product for some time.(Workbench is a pain but it was capable, off-the-shelf and was possible to document it once, more or less, for multiple platforms; I did not actually hate using it. But alas it is old now)I will surely test this out; good luck with it.

---

> **exaroth** · 2026-11-09T18:34:07.000Z　
> Whats the advantage of this over something like dbx (https://github.com/t8y2/dbx)?

---

> **mikenikles** · 2026-11-09T18:47:14.000Z　
> > No feature is ever going behind a paywall.How do you sustain continuous development of the project beyond the next two weekends?

---

> **edem** · 2026-11-09T19:04:52.000Z　
> I'm sick and tired of this "rewrite everything in rust ai slop movement

---

> **mrgoldenbrown** · 2026-11-09T19:26:57.000Z　
> What dbs does it support? I won't drop datagrip until I can access oracle, SQL server and postgres.

---

> **logdahl** · 2026-11-09T19:38:02.000Z　
> Thanks for working on this! All db clients I've used have felt very bloated and I relate to your experience of crashes. I will definitely try this out!

---

> **mamcx** · 2026-11-09T19:46:13.000Z　
> One thing missing in all the GUI clients I know for Postgres's is being able to work with composite types and filtering them like `(IMT, 1)`. Similar as edit things like this, arrays, json, etc

---

> **written-beyond** · 2026-11-09T21:34:16.000Z　
> How intelligent is the query editor? If you've used DataGrip you'll see it's nothing short of a god send. Their Intellisense is really something else.But I absolutely hate opening DataGrip it feels like you're trying to start a crank car from the 40's.

---

> **brumbelow** · 2026-11-09T21:44:48.000Z　
> Thanks for sharing I will give this a try this week. The improved memory impact compared to Dbeaver is too good to resist.

---

> **godockly** · 2026-11-09T21:58:33.000Z　
> I really like it !

---

> **upmostly** · 2026-11-09T22:02:29.000Z　
> What does it have over a hyper-modern DB client like DB Pro?[1] https://dbpro.app

---

> **olive-n** · 2026-11-09T22:14:31.000Z　
> Looks nice, though it does not open .sqlite files on Windows, when they are somewhere in the WSL filesystem. But neither does DBeaver. dbx opens them just fine though.

---

> **gmmachine** · 2026-11-09T22:30:55.000Z　
> This feels more like a proof of concept than anything else.I'd like an AI agent plugin to help with my SQL queries?

---

> **waterTanuki** · 2026-11-10T00:08:22.000Z　
> > I wanted something which is performant, modern and consumes little ram. The existing DB clients are either filled with bloat (Electron and JVM) or paid. This is an alternative to them.There are many, many existing DB clients. Some of them already written in GPUI and free/open source:https://github.com/0xErwin1/dbflux

---

> **shayan_abbas** · 2026-11-09T18:00:14.000Z　
> For the import connections feature? I can add that in, when I added the feature most people were coming from dbeaver and tableplus so just stuck to that.

---

> **shayan_abbas** · 2026-11-09T18:35:32.000Z　
> Basically finding which distribution to go with, there is gpui-ce, gpui-pre because the zed team last updated their crate more than a year ago so people publish it by their own. I have found gpui kit to be the best since it adds a retained mode too I want to ultimately play around with

---

> **shayan_abbas** · 2026-11-09T18:38:02.000Z　
> Thanks man!! Would love some feedback when you try it out

---

> **shayan_abbas** · 2026-11-09T18:37:15.000Z　
> DBX is great but it uses tauri, it is better than using jvm and electron but still doesn't provide the performance gains GPUI does or any other native framework would do.

---

> **shayan_abbas** · 2026-11-09T18:55:08.000Z　
> Voluntary sponsors is the plan for now, I've been fairly consistent with the development for the last few months so I'm fairly confident this won't be abandoned. However, I would love to create a community around it and get some consistent contributors.

---

> **logdahl** · 2026-11-09T19:36:39.000Z　
> I hear you, although I must say I'm very interested in trying this out. It doesn't look like slop, and honestly all db clients I've used have somehow felt inredibly sloppy.

---

> **fhn** · 2026-11-09T21:46:38.000Z　
> I know righ!? Python slop is the best slop

---

> **shayan_abbas** · 2026-11-09T19:34:44.000Z　
> Supports SQL server and postgres natively, oracle through odbc. So yes, all of them

---

> **MrDrMcCoy** · 2026-11-09T20:55:54.000Z　
> Sounds like a worthy Issue/PR ;)

---

> **shayan_abbas** · 2026-11-09T21:21:04.000Z　
> Try it out, filtering and editing already works for composite types :)

---

> **edstarch** · 2026-11-09T18:47:21.000Z　
> ok got itjust had a quick google too because gpui is on my “to check out some time” list and the situation honestly does not inspire confidenceit seems like everyone and their dog has their own vibe coded gpui flavor and the choice is between making your own vibe coded gpui flavor instead of your desired project vs building your project on quicksandi feel like the problem is that (putting together a website, making a bunch of commits, getting people interested) was at some point a sign of a base level of commitmentnow that the cost of that is zero it’s difficult to say whether a “community edition” actually has any community which will still be there next quarteroh well sorry for the rant good on you for making it work clearly it is possible

---

> **dubcanada** · 2026-11-09T18:46:00.000Z　
> So your main sell on DBDelve is performance?

---

> **mbreese** · 2026-11-09T18:51:23.000Z　
> Performance is a hard sell when most of the time is going to be spend waiting on the DB for queries, isn't it? (compared to dbx - anything in Java is going to naturally be larger for this).Or are you thinking of performance in terms of UX when browsing the result-sets?But, congrats on the project. It looks great. I can't wait to try it.

---

> **dofm** · 2026-11-09T20:21:01.000Z　
> I agree.For me, and for customers I want to document things for, it has come down to MySQL Workbench on the free/open source side of things.I want to support multiple platforms without having to fundamentally document multiple strategies.Most DB tools feel like they will go the way of PostgreSQL or Insomnia — get slowly burdened with cloud facilities and then a bait-and-switch means you need a login somewhere.I would much rather be able to talk about clients that do fewer tasks but do them well, but DB clients do seem to be prime enshittification territory for some reason.

---

> **shayan_abbas** · 2026-11-09T18:51:44.000Z　
> Yes, and UX. Doing the fundamental things but doing them really well. I like zed's approach where they were slow to add features and weren't/aren't at feature parity with VSCode but the point was to get out of the way for most of your workflows. I'm basically going with the same idea in mind.

---

> **shayan_abbas** · 2026-11-09T18:59:53.000Z　
> Yes, the slow queries stay but there are some differences:Same result set where other clients can crash, this scrolls smoothly so you can naturally load a bigger result set in the app than other clients would allow you to,
> It paints the UI considerably faster than DBeaver on my benchmarks, thats after the query has run.
> Memory footprint for the same result is considerably lower.Basically, your db client can slow you down even after you have waited for queries so this will fix that.

---

> **dofm** · 2026-11-10T00:18:16.000Z　
> s/Postgresql/Postman/ obviously.Brain concept leakage there. I meant all those apps that start off with a simple purpose and end up with an enterprise cloud plan.

## 关联链接

- https://youtu.be/V2MOhJYFqIEIt

## 导航

- 项目页：[[10-项目/github.com_a074e602]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
