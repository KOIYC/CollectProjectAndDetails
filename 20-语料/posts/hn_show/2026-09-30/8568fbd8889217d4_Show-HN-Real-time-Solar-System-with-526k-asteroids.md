---
type: "corpus"
item_id: "8568fbd8889217d4"
title: "Show HN: Real-time Solar System with 526k asteroids and all tracked satellites"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49898778"
project_url: "https://space.bl2.net/"
author: "wanick"
published_at: "2026-09-29T19:08:01Z"
captured_at: "2026-09-30T18:57:49+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_wanick
  - story_49898778
  - show_hn
  - front_page
metrics: {"points": 258, "comments": 61, "engagement_velocity": 258}
comments_count: 64
comments_total: 64
discovered_via: "hn:show_hn:3d"
---

# Show HN: Real-time Solar System with 526k asteroids and all tracked satellites

> [!info] 一句话导读
> Космос сейчас ▶ демо

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49898778>
> 指标：点赞=258 · 评论=61 · engagement_velocity=258
> 作者：wanick　|　发布：2026-09-29T19:08:01Z
> 项目链接：<https://space.bl2.net/>
> 采集：2026-09-30T18:57:49+08:00　|　id：`8568fbd8889217d4`

## 正文

Космос сейчас ▶ демо
Загружаю…
🌍 Земля ☀️ Вся система 🔄 Вращать с Землёй ✂ Короткие пути все ничего
Тяни — вращать, колесо — приблизить, клик — карточка и орбита, двойной клик — лететь к телу. WASD — полёт, R/F — вверх/вниз, Q/E и стрелки — поворот, Shift — быстрее. Клик по названию группы — подсветить, 👁 — орбиты
Сейчас
 UTC Перейти Сейчас
− +
✕
Данные обновились ( ) Обновить страницу

## 评论（64/64）

> **jairofdez** · 2026-09-29T19:10:30.000Z　
> great project!!!!

---

> **java-man** · 2026-09-29T19:29:56.000Z　
> Super! Not easy to select or center on a planet though.

---

> **wanick** · 2026-09-29T19:38:15.000Z　
> Author here. It's a browser view of the Solar System at real scale, with its current state, plus the objects around Earth from the CelesTrak catalog.Data: CelesTrak TLEs (SGP4), asteroids and comets from JPL SBDB, spacecraft positions from JPL Horizons. Updated daily.Rendering is WebGL2, orbit propagation runs in web workers. The asteroid set (~30 MB) loads in the background.The time slider runs forwards and backwards; satellites appear and disappear by launch date.

---

> **eutropia** · 2026-09-29T20:53:16.000Z　
> What's with those giant blobs of asteroids offset in jupiter's orbit by like 60deg on either side?

---

> **einpoklum** · 2026-09-29T21:08:58.000Z　
> Wow, speedy and convenient! Well done!Some insights:* There is sooo much space debris! Dead sattelites and rocket bodies* Starlink put up a hell of lot of satellites, too.* There is a pretty dense sphere of items around the earth at geo-stationary orbit, a bit like a mantle; but most of all in a circle on that sphere.

---

> **VladDanGeorgesc** · 2026-09-29T21:17:46.000Z　
> Very interesting!

---

> **nugzbunny** · 2026-09-29T21:59:38.000Z　
> This is amazing. Well done. How long did it take to make?

---

> **1shooner** · 2026-09-29T22:08:21.000Z　
> Almost 1 in 3 tracked spacecraft is Starlink, is that accurate?

---

> **nephihaha** · 2026-09-29T22:39:35.000Z　
> Quite incredible how much manmade crap there is up there, and much of it probably useless, and a potential problem for the satellites which are of actual use.

---

> **mcv** · 2026-09-29T22:44:59.000Z　
> There are way more asteroids near the Earth than I thought.

---

> **karim79** · 2026-09-29T23:18:56.000Z　
> Beautiful site. I love how tranquil the scene becomes when satellites and spacecraft is unchecked. Thanks for that SpaceX (and others).

---

> **climech** · 2026-09-30T00:20:45.000Z　
> Just spent a little time following Europa Clipper, it will fly by Earth very soon! If you zoom out from Earth, it's already pretty close. This will be its second gravity assist after Mars. Very cool site!

---

> **tintor** · 2026-09-30T00:25:27.000Z　
> Celestia did all of this and more. 10+ years ago.https://celestiaproject.space/

---

> **blindflag** · 2026-09-30T00:54:39.000Z　
> I love this; also runs surprisingly smoothly (at least in browser; didn't check mobile). Also beautiful and hypnotic in motion. What's the next step that you want to take to develop it (not that there needs to be one)?

---

> **mncharity** · 2026-09-30T01:16:17.000Z　
> Fun: 116 d/s with Earth/etc selected, gives a Sun "orbiting" the Earth/etc effect.Bug: ISO DEB at 17 min/s looked normal, but at 2.8 h/s it became a solid-ish (lots of crossing lines) red ellipsoid on the opposite side of the Earth. Upon returning to 17 min/s, it snapped back, after some delay. Current-ish Chromium on linux/X11.Feat: Pressing ESC deselects.Feat: Perhaps spacebar could pause/unpause time? To avoid fiddly "note current time ratio by counting arrows or hovering, then click pause. Afterward, click the right place to restore time ratio".UX: Would you believe I wrote a Feat for 'add a "Now" button to date popup', not "seeing" the current button? Hmm, perhaps move it between date and time ratio?UX: Just now for me, upon page load, nothing is moving and the Earth seems a black ball (night over Africa, with night lights obscured by satellite dots). So I could spend several minutes exploring, without being both close enough and oriented to notice there's a texture map. Perhaps start positioned over the terminator (interestingly pretty) and with scaled time (interestingly moving; demos motion; draws attention to time zoom. Maybe 17 min/s?).Issue: The planets maps are true-ish color, modulo intensity and shadow. The Sun is... not. Given that "the Sun is some color other than white" is so pervasive a misconception, reinforcing it seems... sigh. Can I interest you in a white field with a few pretty sunspots? Perhaps with limb darkening and tint?

---

> **noosphr** · 2026-09-30T01:25:24.000Z　
> Thank you, this is terrifying.

---

> **subtlesoftware** · 2026-09-30T01:28:34.000Z　
> Turning on asteroids is a jump scare

---

> **sebmellen** · 2026-09-30T01:38:00.000Z　
> Oh man, it seems like my asteroid (Minor Planet 31689 - Sebmellen [0]) is missing.[0]: https://www.wikidata.org/wiki/Q6711174[1]: https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=20031...

---

> **sans_souse** · 2026-09-30T03:26:21.000Z　
> I hate to be the one to come here with a feature request but can you guys hurry up with the Universe already?

---

> **r0b05** · 2026-09-30T04:53:13.000Z　
> Amazing! I had no idea there were so many satellites, especially Starlink ones.

---

> **rtmkrptn** · 2026-09-30T05:47:40.000Z　
> I love how smooth it is! Amazing work

---

> **DylanMerigaud** · 2026-09-30T06:00:33.000Z　
> Real scale makes asteroids hard to see without magnification.

---

> **ComodoHacker** · 2026-09-30T06:42:12.000Z　
> Thanks for the great work!Tracking ISS orbit combined with live feed [0] is amazing.0. https://www.youtube.com/watch?v=fO9e9jnhYK8

---

> **FlowingRiver** · 2026-09-30T06:47:34.000Z　
> Brilliant project and very well done.That aside, it is just astounding that even a moderate laptop just plows through this as thought it is nothing.I remember doing orbital calculations on a 486DX with about 30 objects at just barely 30fps thanks to the FPU. That was pretty good for me. Without the FPU you would get maybe 2FPS. Now, you can just throw a half million around at 60fps+ in a web browser. Crazy!

---

> **mentalgear** · 2026-09-30T07:21:59.000Z　
> A good showcase how easy it is now for LLMs to build these visualizations when the data is structured and available publicly - with the structured and publicly available parts being the main gatekeepers.

---

> **ratox** · 2026-09-30T07:31:20.000Z　
> It would be nice to have a fun feature where we could vote for the most coolest asteroid. In a bracket way so we can see actual fandom battles.Silly? Definitely, but who said the internet needs to be only ad-feeds-related stuff.Anyway, nice work mate!

---

> **dmos62** · 2026-09-30T07:42:26.000Z　
> Tangential, how do you identify what is a satellite in the night sky? They're not shown on Sky Map, the app I use.

---

> **BraamV** · 2026-09-30T08:53:07.000Z　
> This is great! Seeing it like this brings it home, space is getting congested, and Starlink rules.

---

> **GnosiWorks** · 2026-09-30T09:41:24.000Z　
> 526k objects and it still feels smooth. are you culling by distance or doing something smarter on the gpu side?

---

> **dunlin** · 2026-09-30T09:58:58.000Z　
> Always wanted to see the asteroid belt's true density visualized; this really puts it into perspective. Impressive work keeping everything performant.

---

> **jurakovic** · 2026-09-30T10:01:59.000Z　
> No github repo? :(

---

> **Vivek-KY** · 2026-09-30T10:23:58.000Z　
> its really good, appreciate it

---

> **antonyragleap** · 2026-09-30T10:41:39.000Z　
> This is beautiful — handling 526k asteroids in real-time is insane. Is this Canvas or WebGL under the hood?

---

> **boxed** · 2026-09-29T21:58:09.000Z　
> A way to zoom that is faster than mouse wheel would be nice. Takes forever to zoom out a long way!

---

> **____tom____** · 2026-09-29T22:14:16.000Z　
> > It's a browser view of the Solar System at real scaleIs it really? I don't think you could see the satellites, if they weren't drawn at 1000x scale. I am wrong?At real scale, i would expect to not see anything.

---

> **ddahlen** · 2026-09-30T00:56:54.000Z　
> How are you sourcing the spacecraft positions from JPL? Are you just grabbing a huge list of state vectors?My old day job was to compute asteroid positions for NASA telescopes, if you are interested in orbit prop you may be interested in:
> https://github.com/dahlend/keteI made an asteroid only version of yours earlier this year, where it does full orbit propagation in workers:
> https://dahlend.github.io/ketev/

---

> **schiffern** · 2026-09-30T08:35:10.000Z　
> >satellites appear and disappear by launch date
>
> This uses the modern TLE propagated backwards in time (vs using historical TLEs), correct?

---

> **laylower** · 2026-09-30T10:20:52.000Z　
> Importantly, how are we doing in terms of coverage? Are we seeing the sky enough and clearly enough to have a few years worth of warning before we get dinosaur-ed?I figured the experts here would care to express an opinion.

---

> **dvh** · 2026-09-29T21:07:18.000Z　
> https://en.wikipedia.org/wiki/Trojan_(celestial_body)

---

> **dylan604** · 2026-09-29T22:17:10.000Z　
> Everyone talks about the ringed planets, but I've never seen Earth mentioned of having a ring. I've also never seen mentioned that the rings were not man made as a qualifier. Yet, there it is, very clearly visible when zoomed out.One of the things that I noticed was how far away Parker was from the sun. I know it has a crazy orbit, but seeing it at a scale reference just emphasizes how its orbit is complicated.Also, checking out the platforms around L2. Euclid and JWST are no where near each other which again, just emphasizes how much space there is in...space.

---

> **fnordprefect** · 2026-09-29T22:14:47.000Z　
> Seconded. Great work.

---

> **wanick** · 2026-09-29T22:46:11.000Z　
> Thanks! It's a byproduct of another project, so hard to say exactly. A few evenings.

---

> **Sayrus** · 2026-09-29T22:26:48.000Z　
> Even more than that. Of the 35k tracked "Satellites and spacecraft", more than 12k are debris bringing Starlink to 1 in 2. If you look only at Active known satellites, around 2 in 3.From Starlink's page on Wikipedia: "Starlink accounts for approximately 75% of all active maneuverable satellites in Earth orbit"

---

> **gus_massa** · 2026-09-29T22:30:32.000Z　
> Probably correct. Random link from 2023 (~50%) https://www.springco.co.uk/what-do-satellite-constellations-...

---

> **schiffern** · 2026-09-30T03:35:16.000Z　
> It is often pointed out that SpaceX wouldn't exist without NASA, so let's not forget to thank NASA too.

---

> **euler2100** · 2026-09-30T03:38:52.000Z　
> On a browser?

---

> **bbor** · 2026-09-30T04:08:36.000Z　
> Surely we can make room for cool stuff like this without implying that they're stealing or oblivious? The audiences are completely oblivious, and this one combines a stuff in a unique way (and I've seen/loved these kind of sites ever since finding out satellites are in freefall).Not to mention that it's been in beta since at least 2016, seems mostly defunct, and the download page looks like this: https://sourceforge.net/projects/celestia/ Also, AFAICT, it didn't cover satellites at all.

---

> **dddw** · 2026-09-30T06:02:55.000Z　
> You found it? Nice

---

> **derpyzza** · 2026-09-30T10:27:01.000Z　
> i mean... is it? i don't think the author mentioned using an LLM anywhere on this post

---

> **wanick** · 2026-09-30T09:53:57.000Z　
> No culling. The vertex shader solves Kepler's equation for every asteroid each frame, the CPU barely touches them.

---

> **wanick** · 2026-09-30T10:32:34.000Z　
> Not yet, maybe later.

---

> **Oarch** · 2026-09-29T22:00:31.000Z　
> Being able to zoom on mobile at all would be great.
> And a way to close all of the overlay panels!

---

> **jsphweid** · 2026-09-29T22:41:20.000Z　
> I think it's pretty obvious the satellites aren't drawn to scale, given they don't change in size when zooming in/out.

---

> **blindflag** · 2026-09-30T00:51:49.000Z　
> I assumed they meant that relative distance from Earth or orbit is to scale, not that the size of the dots was to scale, but I could be wrong

---

> **bbor** · 2026-09-30T04:02:59.000Z　
> Those are just UX elements -- indeed, no satellite other than maaaaaybe the ISS could be seen here. For one thing, anything in LEO would seem to be moving so darn fast that it'd be disorienting.I imagine there's various similar problems -- Saturn's rings not having the exact right pattern, asteroids not matching their real shape, all the planets being perfect spheres, etc. But I think this resoundingly meets the bar for "a view of the Solar System". Maps and territories and all that, y'know? A quick sketch in a textbook can also be a "a view" while containing far less detail.

---

> **wanick** · 2026-09-30T08:45:02.000Z　
> Yes, state vectors from the Horizons API for each spacecraft, refreshed daily. Thanks for the kete link, I'll take a look.

---

> **zamadatix** · 2026-09-30T01:16:07.000Z　
> Jupiter's rings, which are thin enough we didn't really notice until we sent a spacecraft there, have ~5,000,000,000,000 tons of material (plus or minus several orders of magnitude). The total mass we have ever launched to orbit is a good portion less than 100,000 tons and the vast majority of that is not found in the https://en.wikipedia.org/wiki/Geostationary_ringThe only reason it appears like a ring here is the marker for each satellite or piece of debris is the size of a large city.

---

> **dddw** · 2026-09-30T06:05:02.000Z　
> And NASA wouldn't exist without the USSR...? 8-/

---

> **Vivek-KY** · 2026-09-30T10:29:24.000Z　
> no ,you have to download,just checked..

---

> **defrost** · 2026-09-30T04:17:11.000Z　
> > and the download page looks like this: https://sourceforge.net/projects/celestia/The page that states "Please do not download Celestia from this repository. This repository has been abandoned, and the new source and website are here and here, respectively." for the past four years ?Try: https://celestiaproject.space/download.html and https://github.com/CelestiaProject/Celestia for version 1.6.4Both Celestia and Stellarium have "open data" file formats that come "standard" with downloads and "extra" from community forums - ie all manner of real and SciFi movie/novel objects can be added with name, bitmaps, orbits, etc.

---

> **stavros** · 2026-09-30T06:25:15.000Z　
> No, it's still missing.

---

> **wanick** · 2026-09-29T23:47:54.000Z　
> Thanks, I've already fixed it.

---

> **philipwhiuk** · 2026-09-30T10:22:44.000Z　
> But this is a fundamental problem with using it as a 'space is crowded' argument.

---

> **philipwhiuk** · 2026-09-30T10:21:50.000Z　
> > For one thing, anything in LEO would seem to be moving so darn fast that it'd be disorienting.They take ~90 minutes to orbit - it's not that quick. The satellites are actually moving at the right speed.

## 导航

- 项目页：[[10-项目/space.bl2.net_21009051]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
