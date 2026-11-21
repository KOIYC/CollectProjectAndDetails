---
type: "corpus"
item_id: "b753fa1c4e0e3c8b"
title: "What a self-hosted dashboard looks like on 31.5 inches of colour e-ink"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xtaf06/what_a_selfhosted_dashboard_looks_like_on_315/"
project_url: "https://docs.tesserae.ink/"
author: "xDaftTurtle"
published_at: "2026-11-11T14:18:43+08:00"
captured_at: "2026-11-21T14:46:47+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-11"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Wednesday Exceptions
metrics: {"score": 2669, "comments": 150, "upvote_ratio": 0.9826086956521739}
comments_count: 149
comments_total: 150
discovered_via: "reddit:14d+settle10"
---

# What a self-hosted dashboard looks like on 31.5 inches of colour e-ink

> [!info] 一句话导读
> I maintain Tesserae, a self-hosted server for e-ink dashboards. You compose a dashboard in the browser, the server renders it headless, and it pushes the frame …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xtaf06/what_a_selfhosted_dashboard_looks_like_on_315/>
> 指标：得分=2669 · 评论=150 · 赞踩比=0.9826086956521739
> 作者：xDaftTurtle　|　发布：2026-11-11T14:18:43+08:00
> 项目链接：<https://docs.tesserae.ink/>
> 采集：2026-11-21T14:46:47+08:00　|　id：`b753fa1c4e0e3c8b`

## 正文

I maintain Tesserae, a self-hosted server for e-ink dashboards. You compose a dashboard in the browser, the server renders it headless, and it pushes the frame to your panels. It's AGPL-3.0, runs as a Docker container or Home Assistant add-on, and needs no account.

The frame is a Fraimic Large Canvas, a 31.5" colour e-ink display. Two dashboards are in rotation on it:

1. The project's own numbers for the last 30 days: 606 active installs (up from 342), 1,020 stars, and 92 merged pull requests, 68 of them from 8 outside contributors.
2. My GitHub profile: contribution graph, streak, top repos and recent activity.

On the install numbers: they come from telemetry that is off by default. You're asked once at setup, and it only sends an anonymous count. If you leave it off, the server never contacts me.

I didn't lay these out by hand. Tesserae has an MCP server, so I described what I wanted and an AI agent built both through it. Each one is still just a page of HTML/CSS/JS fed by a few data sources, so you can write or edit them yourself too, for your own repos or homelab. It also runs on much cheaper panels: TRMNL, Seeed reTerminal, Inky Frame, and old Kindles.

**Repo:** [https://github.com/dmellok/tesserae](https://github.com/dmellok/tesserae)

**Docs:** [https://docs.tesserae.ink](https://docs.tesserae.ink)

## 评论（149/150）

> **asimovs-auditor**（1 分） · 2026-11-11T14:19:03+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **xDaftTurtle**（16 分） · 2026-11-11T14:20:51+08:00　
> Three places:
>
> **The dashboards in the photos.** Both were built by an AI agent (Claude) through Tesserae's MCP server. I described what I wanted and it wrote the HTML/CSS/JS for each page. The data on them is real, pulled from the GitHub API and the project's opt-in telemetry.
>
> **The project.** Tesserae is developed with AI assistance. I use Claude Code for a lot of the implementation, and I review, test on real hardware, and merge everything myself. The architecture and design decisions are mine, and it also has human contributors: 68 of the last 92 merged PRs came from 8 outside contributors.
>
> **This post.** I drafted the text with Claude and edited it.

---

> **Shadow_s_Bane**（8 分） · 2026-11-11T14:35:43+08:00　
> What's the display

---

> **xDaftTurtle**（10 分） · 2026-11-11T14:36:46+08:00　
> This is the Fraimic Large Canvas

---

> **Shadow_s_Bane**（6 分） · 2026-11-11T14:43:01+08:00　
> Thanks, it’s very nice but quite pricy

---

> **KSOYARO**（14 分） · 2026-11-11T14:43:23+08:00　
> 1K+$ for the display. Hail naaaah
>
> It looks really good not gonna lie but 1 grand is way too much

---

> **xDaftTurtle**（4 分） · 2026-11-11T14:45:46+08:00　
> I'm fairly lucky that this was a sample for development. but if you're in the market for an e-ink panel this size it's fairly reasonable.

---

> **coachLOCKEY**（3 分） · 2026-11-11T14:48:22+08:00　
> Indeed it is pricy. I wonder if there are cheaper alternative displays, maybe in a different scale.
>
> But it look really nice!

---

> **xDaftTurtle**（5 分） · 2026-11-11T14:58:25+08:00　
> Ohh there definitely are. but this is my new toy :)
>
> Look into the Seeed reTerminal range. All are compatible with Tesserae and are great products.

---

> **Icannotfindnow**（5 分） · 2026-11-11T15:00:57+08:00　
> I thought for that size it is pretty fair price.  Over 13" e-ink kinda jumps in price pretty rapidly.

---

> **sowhatidoit**（58 分） · 2026-11-11T15:06:41+08:00　
> Nice work!
> Any alternarive, cheaper e-ink displays you recommend?

---

> **RogerRamjet999**（18 分） · 2026-11-11T15:08:04+08:00　
> It's a cool idea, but few people are gonna be willing to part with $1,000+ for an eink display.  Out of curiosity I looked at Amazon and found their cheapest 32 inch 4K monitor, it's $160.  Pair that with a presence sensor so it only turns on the screen when you're around and you could have the same as the OP's setup, but for about $200.

---

> **q-admin007**（2 分） · 2026-11-11T15:10:59+08:00　
> Epic and clearly high end.

---

> **xDaftTurtle**（42 分） · 2026-11-11T15:16:53+08:00　
> Yes! I highly recommend the Seeed reTerminal range. They’re all fully supported in Tesserae

---

> **xDaftTurtle**（25 分） · 2026-11-11T15:17:49+08:00　
> You’re not wrong… but there’s something special about an eink display that you just need to experience.

---

> **RogerRamjet999**（5 分） · 2026-11-11T15:38:39+08:00　
> Hey, if you got $1,000 to spare, more power to ya, I was just giving an option to the folks in the cheap seats (which unfortunately includes me).

---

> **starkruzr**（2 分） · 2026-11-11T15:41:19+08:00　
> there are little ones for under $100 fwiw.

---

> **coachLOCKEY**（2 分） · 2026-11-11T15:41:43+08:00　
> Thanks mate - those look like a great start! I think I’ll give it a try

---

> **makanimike**（12 分） · 2026-11-11T15:44:22+08:00　
> You say that like the project itself doesn't already offer affordable options.

---

> **xMaku**（487 分） · 2026-11-11T15:44:28+08:00　
> For a tech guy - oh yeah looks amazing.
> For a regular person - why did you print excel sheet and framed it? : D

---

> **nekokun**（2 分） · 2026-11-11T16:09:20+08:00　
> That or a new car, love it

---

> **MrDrummer25**（1 分） · 2026-11-11T16:39:20+08:00　
> Do eInk displays typically have touch input? Both this and the Seeed one you mentioned

---

> **Xiaopai2**（3 分） · 2026-11-11T16:42:14+08:00　
> How do they compare to Pimoroni's Inky Impression/Inky Frame displays?

---

> **hollywoodhandshook**（10 分） · 2026-11-11T16:42:40+08:00　
> this is so cool, thank you for sharing, and sorry for all the dour lemonheads who keep criticizing you about e-ink display costs, as if thats your fault, AND as if you didn't also suggest quite cheap alternatives.

---

> **MrDrummer25**（2 分） · 2026-11-11T16:55:10+08:00　
> I kinda want to build a live dashboard using this. Thank you for sharing!

---

> **xDaftTurtle**（2 分） · 2026-11-11T17:05:44+08:00　
> Give it a go! I’m always open to feedback.

---

> **hollywoodhandshook**（1 分） · 2026-11-11T17:06:27+08:00　
> BTW am i correct in understanding that if one uses the reTerminal E1001 and the [hosted flasher](https://docs.tesserae.ink/quickstart/seeed-unified/) I dont need to install a self-hosted copy at all and just use the flasher and 'server' to do it?

---

> **xDaftTurtle**（3 分） · 2026-11-11T17:06:31+08:00　
> Some do but honestly with the refresh rate it’s not always the best experience. Look into the reTerminal E1003

---

> **xDaftTurtle**（7 分） · 2026-11-11T17:08:19+08:00　
> Thank you. I’ve come to expect it. I know the price can be polarising but yes there are plenty of options out there.

---

> **MrDrummer25**（2 分） · 2026-11-11T17:08:44+08:00　
> Seems like the Seeed ones are out of stock anywhere I look hah. Looking at the E1002 or E1003, based on size.
>
> And what device would connect to the display? Arduino, or like, USB that is passed through to a VM the same as a Sonoff dongle into HA?

---

> **xDaftTurtle**（5 分） · 2026-11-11T17:12:51+08:00　
> The Pimoroni range is great and as of recently fully supported in Tesserae. The main difference is that the reTerminals are ready to go finished products whereas the Pimoroni boards give you the option to build your own frame/enclosure. Both are good.

---

> **xDaftTurtle**（2 分） · 2026-11-11T17:14:20+08:00　
> I am working on a hosted version (Tesserae cloud) and yes that would be correct, you’d flash the same firmware and point it to cloud.

---

> **rawdikrik**（4 分） · 2026-11-11T17:35:22+08:00　
> This is the dream, but damn that price.

---

> **FatherPaulStone**（72 分） · 2026-11-11T17:37:09+08:00　
> This gave me chuckle. Thank you for making my. day brighter internet stranger.
>
> 100% correct though.

---

> **niksonrt**（11 分） · 2026-11-11T19:00:22+08:00　
> A monitor that glows is a different object. The point of e-ink on a wall is that it doesn't light the room and doesn't ask for attention, which is exactly why nobody leaves a 32 inch LCD running a dashboard in the living room.

---

> **xDaftTurtle**（10 分） · 2026-11-11T19:31:56+08:00　
> This is e-ink haha. 31.5” spectra 6

---

> **xDaftTurtle**（2 分） · 2026-11-11T19:33:23+08:00　
> the displays are esp32 based so they connect to the server via wifi

---

> **MrDrummer25**（1 分） · 2026-11-11T19:47:50+08:00　
> Only wifi? I'd rather direct (my internal homelab network has no AP)

---

> **Discipline_Cautious1**（1 分） · 2026-11-11T19:49:00+08:00　
> >This is e-ink haha. 31.5” spectra 6
>
> 31.5 ?

---

> **xDaftTurtle**（2 分） · 2026-11-11T19:49:21+08:00　
> You could do Bluetooth if that makes it any more appealing (via OpenDispaly)

---

> **xDaftTurtle**（2 分） · 2026-11-11T19:51:13+08:00　
> https://www.eink.com/product/detail/EL315TW1

---

> **Discipline_Cautious1**（1 分） · 2026-11-11T19:54:07+08:00　
> Too rich for my blod.

---

> **Hakunin_Fallout**（5 分） · 2026-11-11T19:54:15+08:00　
> I don't think you need a dashboard, given you're supposed to read it.

---

> **nahnahnahthatsnotme**（0 分） · 2026-11-11T19:55:53+08:00　
> i was go in to buy the blotch https://blotch.app
>
> but i found too expensive- are there any similar to this? where i can send data remotely to keep an updated calendar etc.

---

> **xDaftTurtle**（1 分） · 2026-11-11T19:59:50+08:00　
> Tesserae.ink + any listed display

---

> **toughtacos**（9 分） · 2026-11-11T20:04:29+08:00　
> Did you find a price? I couldn’t find a price in my mobile browser at least. Maybe the website ran a check on me and decided I couldn’t afford it :P

---

> **TheGloomyWoodpecker**（-3 分） · 2026-11-11T20:14:01+08:00　
> Awesome! Just today I was telling my friend what I’m missing from my self hosting stack is an AI slop SaaS solution.

---

> **sibalicious**（56 分） · 2026-11-11T20:17:45+08:00　
> This project looks interesting, but please do a human pass over the documentation. The claudeisms are suffocating.

---

> **Thebandroid**（35 分） · 2026-11-11T20:19:27+08:00　
> as a regular, tech guy person: you spent how much on display no one else in the house will look at after the first sympathetic "wow".

---

> **xDaftTurtle**（3 分） · 2026-11-11T20:19:55+08:00　
> Wow. What a coincidence!
>
> I built it so I could gift frames to non techy people and they wouldn't need to worry about managing a server. You are not the demographic it’s built for.

---

> **xDaftTurtle**（15 分） · 2026-11-11T20:22:34+08:00　
> Thanks for the feedback. I think the next phase will be refining the docs. Things have moved so fast that I’ve only been able to vet them once.

---

> **immutate**（7 分） · 2026-11-11T20:25:42+08:00　
> Yeah, I couldn’t find one either, and I know at this point that if the price is hidden then it’s too expensive for me.

---

> **MrDrummer25**（1 分） · 2026-11-11T20:30:30+08:00　
> Hmm ok, I'll take a look

---

> **codex_41**（14 分） · 2026-11-11T21:03:53+08:00　
> $1300
>
> https://fraimic.com/products/large-canvas
>
> Really cool, not $1300 cool

---

> **Im_A_Praetorian**（1 分） · 2026-11-11T21:27:35+08:00　
> If telemetry is opt-in, how do you build the bridge from 606 > 1010 to 2020?

---

> **the_lamou**（1 分） · 2026-11-11T21:48:54+08:00　
> You're mostly not. Most people just have no idea what a dashboard is for or how to build one effectively.
>
> If you're constantly reading a dashboard, you're doing it wrong.

---

> **Hakunin_Fallout**（4 分） · 2026-11-11T21:52:13+08:00　
> Lmao, as a person creating financial and project dashboards, I'm amazed

---

> **cbunn81**（2 分） · 2026-11-11T21:57:01+08:00　
> Do you know of anything in between the two?
>
> I'm thinking of a project for a wall-mounted dashboard. It doesn't need color or the fancy framing of the Fraimic, but I would like it to be large.

---

> **the_lamou**（1 分） · 2026-11-11T21:59:14+08:00　
> As a person getting paid a lot of money to fix terrible dashboards for 15 years now, I can confidently say that every dashboard you've ever built can be replaced with a pager.

---

> **Hakunin_Fallout**（0 分） · 2026-11-11T22:00:22+08:00　
> https://i.redd.it/7wwd4qu6pz0i1.jpeg

---

> **CosmicSeafarer**（2 分） · 2026-11-11T22:12:06+08:00　
> What’s the refresh time for color on this?

---

> **Silly-Fall-393**（2 分） · 2026-11-11T22:29:36+08:00　
> gorgeous but ridiculous price point

---

> **TheTruthSpoker101**（1 分） · 2026-11-11T22:33:45+08:00　
> This is a dreamlike dashboard, a beautiful framed dashboard

---

> **RXrenesis8**（5 分） · 2026-11-11T22:41:27+08:00　
> Sometimes dashboards are about trends and not just up/down/outages.

---

> **Hour_Bit_5183**（1 分） · 2026-11-11T22:51:26+08:00　
> That's sex!! I love it

---

> **KwyjiboTheGringo**（-1 分） · 2026-11-11T22:54:04+08:00　
> I don't see why something with dynamic backlighting isn't just as good.  For me, e-ink is good for low-energy use, and for sparing my eyes during extending reading sessions.
>
> It's not 32 inches, but I have a 10 inch tablet on the wall that I use to control music and display the weather or a security camera feed.  I lock the screen at night when the room is dark, but during the day it just blends in at this point.  E-ink seems kind of gimmicky for anything besides reading e-books/comics.
>
> Also, large digital calendars are a thing now.  If people are willing to accept those, then I think a dashboard on the same screen would be fine.

---

> **squired**（2 分） · 2026-11-11T22:57:52+08:00　
> I love that display! Any advice on identifying suitable/excellent displays? This is very relevant to my interests. Ideally, I'd love a large color one with touch, for an interactive family calendar I've been building. I'm not particularly price sensitive. I figure you've likely been down that screen rabbit hole already?
>
> Brilliant work and thank you kindly for sharing your efforts!

---

> **DifficultTrick**（17 分） · 2026-11-11T23:13:58+08:00　
> Try the [unslop skill](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md)

---

> **Fickle-Owl666**（6 分） · 2026-11-12T00:07:12+08:00　
> My family uses our display daily, many times a day, it's almost always in use. Maybe add useful things for people?

---

> **zwck**（2 分） · 2026-11-12T00:10:15+08:00　
> so there is tessera and tesserae bookmarked.

---

> **veverkap**（3 分） · 2026-11-12T01:00:15+08:00　
> Wow. That's sell a kidney cool which is too cool.

---

> **the_lamou**（3 分） · 2026-11-12T01:46:47+08:00　
> Sure. That's a page or other notification.
>
> And even then, most people don't understand that a "trend" captured at a spot in time is just a static metric. So really you're looking for the second derivative (rate of change of slope/acceleration) and 3rd derivative (rate of change of acceleration/jerk). Those are actionable.
>
> Slope is actionable over time, too, but it doesn't need to be checked frequently because you should already know the slope from the last time you checked it and by virtue of not having any acceleration or jerk alarms go off.

---

> **bloodguard**（2 分） · 2026-11-12T01:48:15+08:00　
> I think I'd get more excited if the price for these things was a bit more reasonable.    The CEO of my company bought about $150K worth of e-ink "art" display panels and fancy frames for his house.
>
> Running joke around here is that when his wife leaves the house they all go from Monet to PornHub with a click of his phone.

---

> **the_lamou**（1 分） · 2026-11-12T01:48:18+08:00　
> Sorry for all the useless busywork you do, bro. Though I assume you don't realize it's busywork, which I'm also sorry for, albeit for different reasons.

---

> **PropheticStoner**（2 分） · 2026-11-12T01:56:32+08:00　
> super cool

---

> **xDaftTurtle**（4 分） · 2026-11-12T02:35:39+08:00　
> The next size down from this display is the 13.3” spectra 6.
>
> A few options
>
> \- Seeed reTerminal E1004
> \- Seeed EE02
> \- Pimoroni Inky Impression 13.3”

---

> **toughtacos**（4 分） · 2026-11-12T02:57:27+08:00　
> Nnnngh...
>
> This is like a thing I've been waiting for for DECADES.
>
> I think they are absolutely $1,300 cool. Just not... *my* $1,300 cool, if that makes sense.
>
> Fuck, they are really cool though.

---

> **redcomp12**（1 分） · 2026-11-12T03:14:49+08:00　
> Integration for example to usplash, or similar with images gallery, its exists?

---

> **xDaftTurtle**（2 分） · 2026-11-12T03:16:21+08:00　
> Yep! Unsplash (with api key), apple photos, google photos, immich… the big names are there

---

> **oposhumano**（2 分） · 2026-11-12T03:20:45+08:00　
> Looks beautiful, but that price tag though, ooof, too much money for my lowly brazillian pockets.

---

> **tcn33**（1 分） · 2026-11-12T03:33:25+08:00　
> Any go-to Australian retailers you recommend?

---

> **Sierpy**（1 分） · 2026-11-12T03:38:38+08:00　
> What makes a dashboard necessary? And what makes one useless?

---

> **redcomp12**（1 分） · 2026-11-12T03:59:59+08:00　
> And if fraimic push update? Not relevant? How you implement the use of its voice on touch with generate ai photoes?

---

> **xDaftTurtle**（1 分） · 2026-11-12T04:04:35+08:00　
> This implementation uses their own sanctioned API so It should be stable.
> The Original Fraimic Functionality is untouched and works as expected.

---

> **xDaftTurtle**（1 分） · 2026-11-12T04:05:35+08:00　
> Not for the Fraimic itself or really any e-ink displays now that I think about it.
> Seeed seem to do okay shipping from their CN warehouse.

---

> **redcomp12**（1 分） · 2026-11-12T04:18:35+08:00　
> How its blend with you os? Where the ai generated images save? I can still reach my frame via fraimic.app url? Its can mix schedules with tesserea?

---

> **mfdali**（3 分） · 2026-11-12T04:23:35+08:00　
> Do you use an e-ink display?

---

> **xDaftTurtle**（1 分） · 2026-11-12T04:27:11+08:00　
> The fraimic works exactly as it always does so yep, you can still reach it via fraimic.app. I'm still working through scheduling etc and I hope to make some changes to the API that would allow it.

---

> **FarToe1**（3 分） · 2026-11-12T04:27:20+08:00　
> I spent a couple of evenings with Tessarae last week with a CYD and it's everything this guy says.
>
> Perhaps a little fiddly to get it hooked into HA and the first screen onboarded, but once up and you get a grasp on how it works, it's truly amazing. The webui is slick, full featured and fun to use. Changes are pushed to the screens over the air in a few seconds and just work. The ability to add multiple screens and switch between them, and the different styles and panels you can use, even on a the most basic screen - a CYD - is amazing. I've previously spent a long time getting even a basic fixed screen going, and this was faster and infinitely more adjustable.
>
> This has every mark of being one of the gold standard Home Assistant tools and I applaud the work that's gone into it.

---

> **Fickle-Owl666**（-6 分） · 2026-11-12T04:31:10+08:00　
> Not sure why that would be relevant in any way

---

> **mfdali**（7 分） · 2026-11-12T04:38:44+08:00　
> Because e-ink is expensive and the comment you replied to was talking about the cost too. I agree that an interactive display, e-ink or otherwise, can be nice and I have a few plans too, but e-ink in general is expensive and this one specifically is over 700 dollars

---

> **teckcypher**（2 分） · 2026-11-12T05:01:54+08:00　
> For a sec, I thought you made a display to show you the progress on your hdd defrag. Interesting but how many times do you defrag your drive?

---

> **Fickle-Owl666**（-4 分） · 2026-11-12T05:12:57+08:00　
> My comment obviously had nothing to do with the cost, and was about the part of the comment about getting use out of it. No, I didn't spend as much, but if I chose to it would still be used as much as it is, so the cost is irrelevant...

---

> **DoomBot5**（2 分） · 2026-11-12T05:20:56+08:00　
> Definitely a fan of the project. There are still a few gaps here and there, but Claude has been able to figure out a lot of those for me. The built in mcp server support was a nice touch.

---

> **kernald31**（11 分） · 2026-11-12T06:11:52+08:00　
> The irony of the readme having obvious signs of being written by Claude is strong.

---

> **nbnicholas**（2 分） · 2026-11-12T06:37:46+08:00　
> This is gorgeous. Huge fan.
>
> Have you tried it on other e-ink displays or settled on Fraimic? I love it either way. Found my fall project!

---

> **No_Corner805**（4 分） · 2026-11-12T06:45:34+08:00　
> How much did the display cost you?

---

> **xDaftTurtle**（5 分） · 2026-11-12T06:47:59+08:00　
> So I received this unit at no cost for development purposes. The Fraimic Large Canvas retails for around $1300.

---

> **xDaftTurtle**（2 分） · 2026-11-12T06:51:00+08:00　
> So full disclosure, this unit was sent to me as a sample for development. Having it in hand though I can see it's a quality product and I would recommend it. I'm hoping to get some changes into the API to make compatibility a little better.

---

> **xDaftTurtle**（1 分） · 2026-11-12T06:51:52+08:00　
> Please feel free to open issues on GitHub if there's something missing or a feature you'd like. :)
> Thank you.

---

> **xDaftTurtle**（1 分） · 2026-11-12T06:55:15+08:00　
> Thank you! I appreciate the feedback :)

---

> **DoomBot5**（2 分） · 2026-11-12T07:06:01+08:00　
> I believe Claude flagged a couple licensing issues with what I've done which makes upstreaming those changes more complicated. That being said, I've combined a chunk of your code with a chunk of the seeed code then built a library for deploying it via ESPHome. That allows me to add features that don't need to be a part of Tesserae, but I still want from my devices.

---

> **the_lamou**（1 分） · 2026-11-12T07:07:42+08:00　
> An alert should tell you if there's something you need to look at. A dashboard should tell you what you're looking and and what may have changed to require you to look at it. An investigation tells you how to fix it and how to prevent it happening again.
>
> If a dashboard doesn't immediately tell you why you're looking at it and what you should do next, you probably don't need it.
>
> My go-to rule for information display is something I've always called the **rule of six**:
> 1. **Six seconds** to understand the still state of the system you're dashboarding.
> 2. **Six words** or less to explain any metric and why it's important.
> 3. **Six elements** or less on any screen.

---

> **No_Corner805**（7 分） · 2026-11-12T07:35:34+08:00　
> Can I have one for development purposes?

---

> **PaperTowelBear**（1 分） · 2026-11-12T08:51:34+08:00　
> What kind of things do you all use on it? I've been wondering if getting one would be worth it or not.

---

> **JustinHoMi**（9 分） · 2026-11-12T09:48:07+08:00　
> Good Lord I’ve bought cars for less than that.
>
> .
>
> .
>
> .
>
> .
>
> .
>
> .
>
> .
>
> .
>
> .
>
> .
>
> I didn’t say they were nice cars.

---

> **apetalous42**（1 分） · 2026-11-12T10:15:52+08:00　
> I am a professional software engineer, I also would like one for development purposes.

---

> **secondgamedev**（2 分） · 2026-11-12T10:20:28+08:00　
> The screen is beautiful! I also bought a small one (not as beautiful) for my raspberry pi for my own personal home project.

---

> **orcus**（2 分） · 2026-11-12T10:30:49+08:00　
> What's the vector display looking thing above the nixie tube?

---

> **xDaftTurtle**（0 分） · 2026-11-12T11:28:01+08:00　
> [more info on it](https://www.reddit.com/r/nixie/s/wDKBjTvUKg)

---

> **nosyrbllewe**（4 分） · 2026-11-12T11:54:37+08:00　
> I have always thought it would be cool to have an e-ink display dashboard, but the screens are way too expensive. In most cases, an LCD screen is still much cheaper even when you account for electricity costs of running it 24/7 for several years.

---

> **Driky**（49 分） · 2026-11-12T12:51:39+08:00　
> Can’t wait for those big e-ink display to become affordable. No matter that I have the cash for one, I can’t defend 1,2K$ for a dashboard 😭😭

---

> **lwrun**（1 分） · 2026-11-12T12:53:35+08:00　
> If you mean what they linked, that's a [SKILL](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) file specifically meant for agents to use.

---

> **kernald31**（7 分） · 2026-11-12T12:55:12+08:00　
> I know and understand what it is. But either they haven't used that skill to write their own readme, or it's doing a terrible job.

---

> **elelem-123**（6 分） · 2026-11-12T13:32:09+08:00　
> They are not available, either

---

> **No_Corner805**（1 分） · 2026-11-12T13:43:59+08:00　
> Professional DevOps / Network engineer saying, "Hi."

---

> **redcomp12**（1 分） · 2026-11-12T15:03:03+08:00　
> Great, i will dig into it
> what about eink of inky Pinoroni? Same?

---

> **xDaftTurtle**（1 分） · 2026-11-12T15:12:14+08:00　
> The Seeed and Inky devices have a lot more features for now.

---

> **ppkprashanth**（2 分） · 2026-11-12T15:33:15+08:00　
> This is so cool. I was looking for what ever is a big size color e-ink display that I can display dashboard or artwork onto and switch it up as I feel it.
>
> Have been really thinking about DIY n selfhosting vs turn key solutions like switchbot art frame or blooming canvas etc.
>
> What are your thoughts on this. I would prefer a lot less bezel but this is so much nicer than a LCD display and the signage portion looks super enticing.

---

> **henrik_r**（1 分） · 2026-11-12T16:02:07+08:00　
> Does someone know which e-ink displays are most suited to display photography? We are looking to replace our old Philips LCD photo frame, and we like the idea of it being more similar to a printed version, but I worry a bit wrt to available colour space and rastering/resolution. They look amazing with  drawn graphics, but I cannot seem to find good examples of what a photo would look like at a decent viewing distance. I would also obviously prefer for it not needing a paid for cloud service. Either local storage or point it to a docker or vm that I spin up locally at home. Any tips appreciated, we are ready to sink a bit into this as long as the quality is good and they ship to Europe

---

> **xDaftTurtle**（3 分） · 2026-11-12T16:19:42+08:00　
> Pretty much every colour e-ink photo frame right now uses the same panel tech, Spectra 6, so apart from size and resolution the colours look about the same across brands. The 6 is the number of ink colours it has. Everything else is made by dithering those six to approximate the target colour.
>
> In practice that means you can see the dither pattern up close, but at normal viewing distance (a metre or so) it blends and looks a lot like a matte print. Colours are more muted than an LCD, so don't expect the punch of your Philips, but photos with good contrast look great.
>
> The one lever you do have is calibration. paperlesspaper make the Open Paper L and have spent a considerable amount of time tuning colours. I'd look at a frame from them, as they're also based in Europe.
>
> You can use their offline firmware, or flash my Tesserae build for it, which has the same tuned colour profiles. Tesserae is self-hosted (runs in Docker on your own network), so no cloud or subscription.

---

> **that_one_guy_2123**（1 分） · 2026-11-12T17:35:54+08:00　
> I'm curious about the refresh rate of the dashboard, is it a full refresh? Or a partial refresh. What's the interval like?

---

> **cbunn81**（1 分） · 2026-11-12T20:21:29+08:00　
> Thanks for the details. But I'm not looking for smaller. I like the size of the Fraimic one, but I don't need color or the framing which seems to be targeted at art display use cases.
>
> Basically, I want a large, monochrome e-paper display, preferably without the big flashing reloads that some e-paper displays have, since that would be quite distracting when hanging on the wall of a living room. My goal is to have a dashboard of things like weather, date, calendar events, etc. But viewable from across the room. I haven't been able to find anything that fits these goals yet.

---

> **Teh_Nap**（2 分） · 2026-11-12T20:25:43+08:00　
> Wow nice, wonder where I can get one of these displays.
>
> > 1100$
>
> Well, nope.

---

> **xDaftTurtle**（1 分） · 2026-11-12T20:33:37+08:00　
> User /u/MINTimpala was selling some that might fit your criteria. I’m not sure if he has any left.

---

> **MINTimpala**（2 分） · 2026-11-12T20:34:59+08:00　
> Indeed i do. I have 42 inch non-touch and touchscreen E Ink displays. Daft thank you for the name drop

---

> **cbunn81**（1 分） · 2026-11-12T21:56:48+08:00　
> Oh, cool. What kind of displays are they? Do you have specs? Where are you located?

---

> **MINTimpala**（2 分） · 2026-11-12T22:07:51+08:00　
> Im in nyc/nj but i can ship really quickly!
>
> Heres the [link](https://www.avalue.com/en/product/Digital-Paper/Public-Display-Solution/EPD-42T) to the touch screen(epd 42s)  - and the epd42s sid is just a non touch model

---

> **cbunn81**（2 分） · 2026-11-12T23:16:24+08:00　
> It looks interesting, though I wonder about power. One reason I'd like to use e-paper over the easier and cheaper LCD panel route is that many displays use so little power, you can run them from a small USB power bank. This one lists having a DB power adapter, so it sounds like it might need a constant connection.
>
> Also, do you ship internationally? I'm in Japan.

---

> **MINTimpala**（1 分） · 2026-11-12T23:18:40+08:00　
> Yes - a power adapter is necessary. Although I’m not sure, perhaps you can find something I don’t know about.
>
> As far as shipping to Japan, I can absolutely but ofcourse we must consider import taxes/clearance fees etc :) message me?

---

> **PixelProne**（1 分） · 2026-11-13T01:22:10+08:00　
> How much are you selling them for? I'd be interested in snagging one for a project.

---

> **redcomp12**（2 分） · 2026-11-13T02:07:04+08:00　
> This is the same?
>
> https://tessera-maxgramser.on-forge.com

---

> **xDaftTurtle**（1 分） · 2026-11-13T02:12:27+08:00　
> It’s a seperate project with a similar name. Tessera targets lcd and tessera**e.ink** targets e-ink.

---

> **Open-Adhesiveness-86**（2 分） · 2026-11-13T05:41:28+08:00　
> Cheap-ish route is a Waveshare panel plus an ESP32 driver board: a 7.5" mono is around $50, the 7.3" 7-colour ACeP is maybe $70. Just know the colour ones take 15-30 seconds to refresh and flash through every colour while doing it, so they're fine for a once-an-hour dashboard and awful for anything live. Old Kindles are the other cheap trick if you can jailbreak one.

---

> **_Cinnabar_**（3 分） · 2026-11-13T08:05:32+08:00　
> that's perfect, my reterminal should arrive this week 🥳
>
> only the 7.3" version, but I don't need to show a lot :)

---

> **Thebandroid**（2 分） · 2026-11-13T18:41:12+08:00　
> At most a calendar. The family does not care about the health of the zfs array

---

> **Tall-Barber-3157**（1 分） · 2026-11-14T01:07:38+08:00　
> Darf ich fragen wieviel das Teil an Stromverbrauch hat?

---

> **tismo74**（2 分） · 2026-11-14T02:29:29+08:00　
> These things need to come down in price

---

> **moss_leap**（4 分） · 2026-11-14T05:21:16+08:00　
> Anthony here, founder of Fraimic. Yes they are, where are you trying to ship to?

---

> **moss_leap**（2 分） · 2026-11-14T05:22:54+08:00　
> Anthony here, founder of Fraimic. We are launching in ANZ next month! Keep your eyes out

---

> **SomethingSharper**（1 分） · 2026-11-14T07:42:48+08:00　
> This is super cool, FYI I went to buy a frame with your affiliate code and it did not work. I hope this comment doesn't get removed, I tried to find a way to DM you but could not

---

> **xDaftTurtle**（1 分） · 2026-11-14T07:53:31+08:00　
> Thanks for the heads up! I’ve just sent you a dm

---

> **elelem-123**（3 分） · 2026-11-14T07:55:56+08:00　
> Website says sold out.
>
> Fraimic Smart E Ink Canvas
> Large Canvas
> 94 reviews
> Regular price €1.196,95 EUR
> Sold out
> Shipping calculated at checkout.
>
> Display your favorite art, personal photos, or create something entirely new with your voice.

---

> **moss_leap**（0 分） · 2026-11-14T08:00:45+08:00　
> Where are you trying to ship to?

---

> **elelem-123**（4 分） · 2026-11-14T08:02:40+08:00　
> I am not. This is what the website shows on the product page. I didn't add it to my cart and I'm not trying to buy. I'm taking about the product listing. Maybe I'm on a wrong website. I don't know. https://fraimic.com/products/large-canvas

---

> **Doraemond**（2 分） · 2026-11-16T10:20:58+08:00　
> Nice, I have some kindle unused laying around

---

> **Fantastic-Extent-587**（1 分） · 2026-11-17T14:27:00+08:00　
> Good one,
> But you need to think of UX, like who can regularly read that small text in a dashboard.

---

> **tusioly**（1 分） · 2026-11-17T21:18:35+08:00　
> With some tinkering i guess you could put that on a EMDX32 Panel these were the cheapest i could find and are made by samsung. I would guess they use that exact panel. Got mine for 600€

---

> **Strata38**（1 分） · 2026-11-18T13:55:29+08:00　
> didnt someone do this with those lululemon mirrors that failed? they're surprisingly cheap i think

## 关联链接

- https://docs.tesserae.ink
- https://github.com/dmellok/tesserae

## 导航

- 项目页：[[10-项目/docs.tesserae.ink_391efd16]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
