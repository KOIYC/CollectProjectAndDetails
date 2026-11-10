---
type: "corpus"
item_id: "e8c8607079b778f1"
title: "Show HN: Every satellite that passed over any place this week, and its photos"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50428907"
project_url: "https://watched.earth/"
author: "a585gupt"
published_at: "2026-11-09T17:51:31Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_a585gupt
  - story_50428907
  - show_hn
  - front_page
metrics: {"points": 228, "comments": 42, "engagement_velocity": 228}
comments_count: 42
comments_total: 42
discovered_via: "hn:show_hn:3d"
---

# Show HN: Every satellite that passed over any place this week, and its photos

> [!info] 一句话导读
> hey HN, i built this because i wanted to know what had actually photographed my street.type in any place and it finds every satellite that passed over it in the…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50428907>
> 指标：点赞=228 · 评论=42 · engagement_velocity=228
> 作者：a585gupt　|　发布：2026-11-09T17:51:31Z
> 项目链接：<https://watched.earth/>
> 采集：2026-11-10T09:49:42+08:00　|　id：`e8c8607079b778f1`

## 正文

hey HN, i built this because i wanted to know what had actually photographed my street.type in any place and it finds every satellite that passed over it in the last 7 days (SGP4 on the CelesTrak catalog, runs in your browser in about half a second), then pulls the real Sentinel-2 / Landsat / NASA images from those passes.some fun bits:
- the pass search can't skip a pass. checked it against a brute force on poles, the antimeridian and tiny swaths: 0 missed
- all ~17k objects in orbit are drawn on the GPU, solving Kepler's equation every frame
- Sentinel-2 timestamps are often 5-10 min off from when the sat actually crosses your spot, which was a fun one to figure outit only says "watched" if a real image exists, and it doesn't store your location.code: https://github.com/dev-Armaan/satelliteswould love feedback, especially on what data sources to add

## 评论（42/42）

> **sixtyj** · 2026-11-09T17:56:03.000Z　
> I have seen a lot of sites with satellites’ overviews… I work in geospatial.This site is really good one as you can see exact image taken by a satellite.Well done.

---

> **jttnr** · 2026-11-09T18:59:34.000Z　
> That looks really nice. I especially like the view showing the satellite flying overhead and the line marking the scanned area.

---

> **wnissen** · 2026-11-09T19:28:22.000Z　
> This is great for planning backpacking trips. I have been using Copernicus but you have a lot more and it's much easier to access. Very nice!

---

> **nico** · 2026-11-09T19:47:39.000Z　
> This is very cool, and a bit creepy too, but mostly coolReally liked the UX, even on a small phone screen it was easy to use. I enjoyed the big typing cursor, it was a unique surprise (almost 100% of text form inputs have either a very small vertical line cursor, or nothing at all - the big cursor feels refreshing)

---

> **Zeetah** · 2026-11-09T19:54:21.000Z　
> Love the fly overs, and the interface. Just beautiful.

---

> **gizajob** · 2026-11-09T19:54:22.000Z　
> Awesome page. Thanks for building.

---

> **JeppyG** · 2026-11-09T19:56:21.000Z　
> Very cool. Was this inspired by the latest season of cyberpunk? In case you and Capri need to escape onto a satellite. XD

---

> **bketelsen** · 2026-11-09T19:56:30.000Z　
> Great user interface - animations are such a nice touch.

---

> **jfsebastian** · 2026-11-09T20:08:10.000Z　
> Pretty damn cool and super smooth. Thanks op!

---

> **hxorr** · 2026-11-09T20:30:42.000Z　
> Can you get high res images, or are they typically not made public?Very cool tool

---

> **HoldOnAMinute** · 2026-11-09T20:38:45.000Z　
> I don't say this lightly: This may be the best combination of style and substance I have ever seen.

---

> **creeble** · 2026-11-09T20:57:13.000Z　
> Um, wow. Amazing UI.This photo of the SF Bay this morning is a great representation of the fog that settles in over the area:https://www.watched.earth/s/3zg2u78u

---

> **award_** · 2026-11-09T21:02:38.000Z　
> This is not only a very cool idea, but also fantastic execution! Great work and very neat!

---

> **zahirbmirza** · 2026-11-09T21:12:24.000Z　
> oooh. so fun.I imagine, that there is someone with access to this sort of thing, with live imagery from any satellite they click on, in 8k.

---

> **tarpump** · 2026-11-09T22:13:27.000Z　
> Really cool, and beautiful UX.For data sources, it would be cool to add Sentinel-1 since SAR sees through clouds, plus the Umbra and Capella open data archives for some high-res passes.

---

> **lol8675309** · 2026-11-09T22:37:03.000Z　
> Super broken at the moment - or I'm impatient

---

> **animal_spirits** · 2026-11-09T22:40:35.000Z　
> Welldone! very fun to play with

---

> **Eridanus2** · 2026-11-09T22:45:28.000Z　
> The relevant launch video trailer on your X page is really well produced. How did you go about constructing it?

---

> **anonymous908213** · 2026-11-09T22:50:15.000Z　
> People who prompt an LLM to generate without proper capitalization in order to deceive more people into thinking the text is genuine deserve a special place in hell. Always with the inauthentic feedback CTA, too. This should be killed off HN for flagrantly violating the rules against LLM-generated text, and yet everyone upvotes it.

---

> **dingaling** · 2026-11-09T23:05:00.000Z　
> > type in any place and it finds every satellite that passed over it_Most_ satellites. However, nothing associated with the NRO is in the public TLE catalog.

---

> **bradknowles** · 2026-11-09T23:30:22.000Z　
> Trying to type in the location field is almost impossible. There is something way off in the way the block cursor reacts to character spacing compared to the text in that field.

---

> **janoelze** · 2026-11-09T23:37:47.000Z　
> and built in three days! https://github.com/dev-Armaan/satellites

---

> **a585gupt** · 2026-11-09T18:00:59.000Z　
> thanks a lot!!

---

> **a585gupt** · 2026-11-09T18:59:56.000Z　
> thanks!!

---

> **mxuribe** · 2026-11-09T20:23:05.000Z　
> Yeah, that was so cool; like something right out of a call sci-fi movie or show!

---

> **a585gupt** · 2026-11-09T19:50:44.000Z　
> thanks, glad to hear it!

---

> **a585gupt** · 2026-11-09T19:55:40.000Z　
> thanks so much!

---

> **a585gupt** · 2026-11-09T19:55:32.000Z　
> thanks a lot!

---

> **a585gupt** · 2026-11-09T19:57:44.000Z　
> haha thanks!

---

> **a585gupt** · 2026-11-09T19:57:28.000Z　
> thanks!!

---

> **a585gupt** · 2026-11-09T20:17:22.000Z　
> thanks!!

---

> **a585gupt** · 2026-11-09T20:35:41.000Z　
> for most places in the world ~10m/px is the best public image res, some lower (ex. rural areas) and some higher, am working on sourcing higher res for the areas where it's available tho

---

> **a585gupt** · 2026-11-09T20:46:14.000Z　
> thanks! stoked to hear it!

---

> **dyauspitr** · 2026-11-09T20:49:27.000Z　
> This is almost certainly Claude but I agree with both style and substance on this post.

---

> **Loughla** · 2026-11-09T21:48:13.000Z　
> Seriously though. I actually enjoyed using this. Good job to OP even if it's AI.

---

> **a585gupt** · 2026-11-09T20:58:58.000Z　
> awesome! thanks for sharing!

---

> **a585gupt** · 2026-11-09T21:09:08.000Z　
> thanks a lot!

---

> **a585gupt** · 2026-11-09T21:33:53.000Z　
> yeah def some generals who use stuff that mogs this

---

> **a585gupt** · 2026-11-09T22:14:39.000Z　
> Thanks for the sources, will look into them!

---

> **unrented7977** · 2026-11-09T22:57:55.000Z　
> The nonsensical "I brute force checked it" paragraph is 100% Claude. Nobody writes like that, and no human ever includes this level of irrelevant reassuring detail.

---

> **moecables** · 2026-11-09T22:58:58.000Z　
> can't believe this is a prompt someone would pass in, my last check if someone was human was their lack of proper grammar

---

> **post-it** · 2026-11-09T22:15:18.000Z　
> I think this is a great counterexample to AI sites that suck. It's not the Claudisms and the borders-and-pills that make them suck, because this has all that but is fantastic.

## 关联链接

- https://github.com/dev-Armaan/satelliteswould

## 导航

- 项目页：[[10-项目/watched.earth_f9bcde1a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
