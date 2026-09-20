---
type: "corpus"
item_id: "a48a11c46f2affc7"
title: "Show HN: Helios – what plug-in solar could generate for any address in Britain"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48334949"
project_url: "https://helios.southlondonscientific.com/"
author: "ruaraidh"
published_at: "2026-05-30T11:08:37Z"
captured_at: "2026-09-21T01:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_ruaraidh
  - story_48334949
  - show_hn
metrics: {"points": 126, "comments": 44, "engagement_velocity": 126}
comments_count: 44
comments_total: 44
discovered_via: "hn:show_hn:144d"
---

# Show HN: Helios – what plug-in solar could generate for any address in Britain

> [!info] 一句话导读
> Plug-in solar panels (no electrician needed) have just become legal in the UK and will go on sale soon. Helios estimates how much electricity a typical installa…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48334949>
> 指标：点赞=126 · 评论=44 · engagement_velocity=126
> 作者：ruaraidh　|　发布：2026-05-30T11:08:37Z
> 项目链接：<https://helios.southlondonscientific.com/>
> 采集：2026-09-21T01:43:31+08:00　|　id：`a48a11c46f2affc7`

## 正文

Plug-in solar panels (no electrician needed) have just become legal in the UK and will go on sale soon. Helios estimates how much electricity a typical installation could generate at a given address and what that's worth against your tariff.It uses UK government LIDAR data to reflect the actual skyline, so it knows whether there's a building or a hill blocking the sun.Caveats:
- Outside LIDAR coverage (most of Scotland and Wales) it falls back to a synthetic horizon (less accurate).
- Trees and recent developments (post-2022 or so) may not be in the data, and some address placements could be off (geocoding via OSM).Feedback on the shading model especially welcome.

## 评论（44/44）

> **GordonS** · 2026-05-30T12:21:51.000Z　
> This is really nice! Would be great if it could handle regular rooftop solar calculations too.

---

> **redfloatplane** · 2026-05-30T12:32:02.000Z　
> Huh, TIL about the National LIDAR Programme: https://www.data.gov.uk/dataset/f0db0249-f17b-4036-9e65-3091...Very interesting stuff and quite a large undertaking! I'm often impressed by the quality of the UK's open data.

---

> **ltrg** · 2026-05-30T13:24:01.000Z　
> Really cool stuff. Nitpick: it failed to grab an OSM ID for my house and fell back to postcode centroid, but then still reported LIDAR-derived shading at quite high precision.I'm wondering if it should fall back to a more general shading approach when no OSM building footprint is available, to avoid false precision? My street has a gap in the houses on the other side from mine, so picking the right location matters for the calculation.You could also try Inspire Index polygons instead of OSM? These correspond to actual lease/freehold boundaries.

---

> **realty_geek** · 2026-05-30T14:15:53.000Z　
> Nice. I'm working on a project called homestocompare to help people house-hunting in the UK.Would be nice to add this as an extra data point when comparing. Are you open to collaborating at all?

---

> **domh** · 2026-05-30T15:02:22.000Z　
> Would be good to be able to select multiple points on the compass and have it tell me the best place for it (front and back garden)

---

> **ifh-hn** · 2026-05-30T15:28:22.000Z　
> > Worth it. The kit pays for itself in 7.1 years; over 20 years it's good for about £1,095 net.This is my issue with this sort of thing. Am I going to have this kit in 7 years? Or would I upgrade to better stuff at the technology improves?

---

> **toomuchtodo** · 2026-05-30T15:29:01.000Z　
> Great work. Is it possible to use this dataset to calculate total plug in solar potential within the geographic constraint?

---

> **dnlzro** · 2026-05-30T16:18:52.000Z　
> This is a great use of open data!Please consider making the source code available. I’d love to make something similar for your friends across the pond (in Canada).

---

> **IshKebab** · 2026-05-30T16:38:07.000Z　
> What if I already have solar, can I add this?Also do you actually need a balcony or can you hang these out of a window somehow? Very few houses in the UK have balconies.

---

> **ErroneousBosh** · 2026-05-30T17:47:55.000Z　
> "Any address in Britain""Caveats: - Outside LIDAR coverage (most of Scotland and Wales) it falls back to a synthetic horizon (less accurate)"So, "any address in the most of the southern half of Britain"?

---

> **overfits_ai** · 2026-05-30T17:57:37.000Z　
> This is a really interesting project! The use of LIDAR data to account for actual building shadows is a clever approach. I'd be curious to see how this compares to commercial solar assessment tools in terms of accuracy. The UK's move to legalize plug-in solar is great for residential adoption.

---

> **pinkgolem** · 2026-05-30T18:19:41.000Z　
> I am just surprised about the cost?Kits in Germany are 300€ without a battery.

---

> **mattlondon** · 2026-05-30T20:07:55.000Z　
> Nice.It would be nice to be able to pick the precise location on the map (house number appears not to work).Also "ground floor" seems to say 1.5m off of the floor? I would like to tweak those values for e.g. panels on the floor in a garden.

---

> **benj111** · 2026-05-31T09:32:26.000Z　
> What are the costs of the installation based on? I haven't been able to find any for sale?

---

> **syedofc** · 2026-05-31T11:29:18.000Z　
> This is a nice example of making sustainability practical rather than abstract. Showing potential generation at an address level makes the decision much easier for non-experts.A lot of climate tech needs this kind of interface: not just “this is good,” but “this is what it could mean for your specific situation.”

---

> **ruaraidh** · 2026-05-30T12:24:41.000Z　
> Thanks! Should be doable, I just got excited by the new shiny thing first.

---

> **kilroy123** · 2026-05-30T13:01:02.000Z　
> I noticed this as well! Very interesting.

---

> **cowsandmilk** · 2026-05-30T17:51:19.000Z　
> > I'm often impressed by the quality of the UK's open data.The ordnance survey not being open data is a bad look though.

---

> **ruaraidh** · 2026-05-30T13:27:19.000Z　
> Thanks - I didn't know about Inspire Index, I'll check it out. I tend to agree about false precision. My first instinct was to use the synthetic horizon for addresses in that group, but I think that's over positive. A range might be better (if a bit more complex)?

---

> **ruaraidh** · 2026-05-30T14:25:15.000Z　
> Absolutely! I have some other datasets that might be useful too (e.g. air quality). Drop me a line: ruaraidh[at]southlondonscientific.com :)

---

> **simonjgreen** · 2026-05-30T14:51:12.000Z　
> Let me know if you’d like access to alt net availability data

---

> **ruaraidh** · 2026-05-30T15:28:57.000Z　
> Good idea. I want to add specific options for different mounting locations (sheds etc) as well.

---

> **toomuchtodo** · 2026-05-30T15:29:46.000Z　
> Depends on your energy requirements and future technology and energy costs. At the moment, one should value this outlay as a fixed income equivalent investment [1].The panels have a ~25 year warranty though [2] (at which point, they should still produce ~80% of rated output), so it’s entirely possible to just leave them in place. At a certain age (~55-60), these are the last PV panels you’ll need to buy, as they’ll potentially outlive you (assuming developed country life expectancy).[1] https://magnifina.com/articles/rooftop-solar-yield/[2] https://www.energysage.com/solar/solar-panel-warranties/

---

> **pjc50** · 2026-05-30T16:33:19.000Z　
> Why would you replace it if doing so is uneconomic?Panel lifetime is very high. The scope for efficiency improvement is not huge (unless there is a cost breakthrough in multi band photon capture). It's not a car, phone, or computer. It's more like the rest of the house electric infrastructure.I had my rooftop solar over 10 years ago and basically intend to leave it until some maintenance issue forces action.(Also, the kit secondhand value is hard to determine but far from zero; 30-50% maybe?)

---

> **IshKebab** · 2026-05-30T16:36:27.000Z　
> The technology is unlikely to improve meaningfully in 7 years. And you'd only upgrade if it was a financial improvement so it makes complete sense to give an estimate based on keeping it for 20 years.I don't see what your issue is.

---

> **brk** · 2026-05-30T17:30:15.000Z　
> These calculations often fail to account for present vs future value of money.If you’re financing the system you have no big cash outlay, but returns are further out, possibly never when accounting for the useful like of the system.With cash up front all the returns are yours, but they are much lower than what that cash would net you in an average investment.The financial math on small solar systems can be complex. If the system is sufficient to provide power to major appliances in a power outage (assuming you have a power outage risk in your area), it can make more sense to tie money up in these systems.

---

> **ErroneousBosh** · 2026-05-30T17:46:22.000Z　
> I got the exact same values.I'd like it if it would actually show me how much sun it thinks I'd get at the postcode I put in. I've got about a third of an acre of garden in a 6 acre field to play with, before I start having to dig up roads. I can afford to be quite free and easy with placement ;-)

---

> **dafrie** · 2026-05-30T20:10:20.000Z　
> Notice that the pricing will come down. In Germany (where the market is mature), I can buy a 2kWp system for 500-600 EUR. Then your payback time basically halves...

---

> **harel** · 2026-05-30T20:21:51.000Z　
> To me, 7.5 years is not worth it. and the 1K in 20 years is nothing. This should be the standard and it should be free. Until then we'll keep paying through the nose for energy...

---

> **ruaraidh** · 2026-05-30T16:11:38.000Z　
> Oh, that's such a good idea! I suppose the challenge is knowing where there are installable surfaces are (or at least making defensible guesses). I'm going to have a go at this...

---

> **jimnotgym** · 2026-05-30T16:53:12.000Z　
> You can put it on the ground if you like

---

> **gib444** · 2026-05-30T18:28:23.000Z　
> Surprised which way? Too cheap? Too expensive? Surprised things differ in price by country?

---

> **spockz** · 2026-05-30T20:36:39.000Z　
> Be wary of these people: https://helioscope.aurorasolar.com/

---

> **danw1979** · 2026-05-30T18:54:07.000Z　
> I’ll add the UKHO Admiralty marine charts to this list too.

---

> **redfloatplane** · 2026-05-30T19:43:00.000Z　
> Indeed. Taillte Ireland's (Ordnance Survey Ireland's) detailed cartographic data is also not open (including historic data - maps from the 1820s and 1920s!) and it's really a huge pain in the ass. On the other hand, OSM is in pretty good shape at least for topographic information. I've used it to make hiking maps here and nobody's died - as far as I know.As a side note, I was one of the initial developers of the Irish national open data portal. Earlier today I had Claude look for similar LIDAR data for Ireland and I saw it pull from the site I built a dozen years ago and I was unreasonably pleased with myself :)

---

> **realty_geek** · 2026-05-30T17:09:00.000Z　
> Great, thanks - I'll drop you a line.

---

> **realty_geek** · 2026-05-30T17:18:26.000Z　
> Sorry, not sure what you mean by "alt net availability"

---

> **ifh-hn** · 2026-05-30T23:26:26.000Z　
> Then you are unlikely to be the person I'd be taking advice from.

---

> **Hamuko** · 2026-05-30T20:50:13.000Z　
> Maybe you guys wouldn't be paying through the nose for energy if you had more solar.

---

> **pinkgolem** · 2026-05-31T05:23:46.000Z　
> To expensive, 2x of a factor between countrys side by side is massive.Esp. As the 300€ are more of an go to your nearest diy store and buy one, there are better deals out there.Here is one for 239 effectively, including hanging hardware & everything you need.https://www.mydealz.de/share-deal-from-app/2787366

---

> **IshKebab** · 2026-05-31T06:21:46.000Z　
> Let me rephrase: the thing that you said clearly isn't an issue so it doesn't make sense for you to have an issue with their advice.

---

> **blitzar** · 2026-05-31T07:16:21.000Z　
> It wouldn't be England if the sun shone.

---

> **harel** · 2026-05-31T22:07:09.000Z　
> Not on those terms. Nobody wants to pay through the nose and see a return in a decade. We wouldn't be paying through the nose if we used our own gas instead of importing it. Crazy idea, I know...

---

> **gib444** · 2026-05-31T10:51:12.000Z　
> Thanks for clarifying. Lots of vague comments here recentlyWe don't call it "rip off Britain" for nothing. A great many things are a rip off

## 导航

- 项目页：[[10-项目/helios.southlondonscientific.com_3377986c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
