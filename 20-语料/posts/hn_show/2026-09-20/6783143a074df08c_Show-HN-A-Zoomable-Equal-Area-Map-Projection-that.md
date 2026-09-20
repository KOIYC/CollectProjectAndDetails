---
type: "corpus"
item_id: "6783143a074df08c"
title: "Show HN: A Zoomable Equal-Area Map Projection that interpolates to Mercator"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49710096"
project_url: "https://benjoffe.com/map"
author: "benjoffe"
published_at: "2026-09-15T09:58:15Z"
captured_at: "2026-09-20T09:37:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_benjoffe
  - story_49710096
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: A Zoomable Equal-Area Map Projection that interpolates to Mercator

> [!info] 一句话导读
> A New Equal-Area Map for Interactive Computer Use

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49710096>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：benjoffe　|　发布：2026-09-15T09:58:15Z
> 项目链接：<https://benjoffe.com/map>
> 采集：2026-09-20T09:37:30+08:00　|　id：`6783143a074df08c`

## 正文

Author: Ben Joffe

A New Equal-Area Map for Interactive Computer Use

## Seamlessly transitioning to Mercator upon zoom (and some new compromise cylindrical maps)

15 September 2026

Recently the UN passed the non-binding "Correct the Map" resolution which encourages the use of the Equal Earth projection in place of Mercator (which represents country-sizes disproportionately).

The Mercator projection is well suited to zoomable/navigation maps due to being "conformal", meaning it represents directions accurately. At a global scale Equal Earth may look pretty good, but it's not what web and mobile based apps typically require.

I present an alternative. The map below is equal-area at a global scale, and upon zoom, it transitions seamlessly to the Mercator projection. It is defined by an unusually simple math formula. The hybrid nature of the map is baked into the very design.

Note: the transition states are compromise map projections. It is equal area only at the global scale, and conformal only once zoomed in.

In my view most countries improve in appearance in the zoomed-out mode compared to Equal Earth. An obvious exception is Northern Europe when centred, however I encourage you to pan the map so Europe is on the edge and then compare. See the side-by-side screenshots for more specific examples.

## The Formula Deep link

Before discussing the map in more detail, a quick high level overview of the math:

Forward:

$y=tanh−1⁡(sin⁡(lat)⋅a)⋅1a$

$x=lon⋅k$

Inverse:

$lat=sin−1⁡(tanh⁡(y⋅a)⋅1a)$

$lon=xk$

Where:

$a=A=49$

$b=45$

$k=K=b(1−a2sin2⁡(lat))$

A proof that this produces an equal area map is presented in Annexure A - Equal Area Proof.

In order to transition to the Mercator projection:

- Let

$z$

 be a variable that scales with zoom from

$0$

(global view) to

$1$

(when it completes the transition to Mercator).
- Let

$a=lerp(A,1,z)$

 .
- Let

$k=lerp(K,1,z)$

 .

That's it! A simple closed-form function in the forward and inverse directions. By comparison, Equal Earth has many fitted constants and requires Newton's formula to iterate the inverse. (see the definition on Wikipedia) .

Not only does it transition to Mercator, but if you let

$x=lon$

 and

$a→0$

 then it becomes the Lambert cylindrical equal-area projection !

$lima → 0 tanh−1(sin(lat)⋅a)⋅1a=sin(lat)$

I.e. the pure cylindrical version of this formula interpolates equal-area and conformal cylindrical maps. This lends it to generate some very nifty compromise cylindrical projections which will be outlined later.

#### United States and Central America

Being off to the side, it is difficult to represent USA and Mexico without distortion. Slightly less skew occurs in the new map compared to Equal Earth.

#### Australia and New Zealand

Also off to the side, it is difficult to represent Australia and particularly New Zealand without distortion. Slightly less skew occurs in the new map compared to Equal Earth.

#### Japan and Korea

North East Asia suffers from the same skew problem, which is distorted less in the new map style.

#### Africa

Equatorial continents like Africa have slightly less vertical stretch compared to Equal Earth:

#### South America

South America is a bit more of a mixed-bag. I would argue that the continent on the whole looks better in the new map, while Argentina and Chile have a more natural shape in Equal Earth down in the south.

#### Europe

Europe is the main exception to the trend above (when considering only reasonably populated land masses). It appears quite good in the standard Equal Earth map projection.

Since Europe is so high in latitude, in order to get Europe looking good, one must sacrifice the appearance of other countries by introducing a high degree of curvature. In my view, Europe is already "lucky" in that it overlaps the prime meridian, so putting extra emphasis on a good-looking Europe at the expense of other countries feels a little lopsided.

The points above hold only for a static map. Once the map is rotatable, a high curvature becomes a disadvantage. The images below show how the flatter, lower-skew layout creates a more recognisable Europe when panned to the edge:

Equal Earth

Equal Earth

## Why These Constants (a & b) Deep link

There are two constants chosen in the formula:

$a=49$

 and

$b=45$

. These have been selected from trial and error as values that, in my subjective opinion, look the best. Others may certainly disagree, especially perhaps preferring a smaller value of

$a$

. Any chosen values will retain the equal-area property.

Below is a sense of how each constant moves the map. The middle column of each row is the value actually used; the columns either side show it nudged down and up.

$a=3.59=0.3888...$

$a=49=0.444...$

$b=45=0.8$

$b=4.55=0.9$

## Compromise Cylindrical Projections Deep link

As noted previously, the general formula for latitude in the new map interpolates equal-area and conformal cylindrical maps.

Here is the same interactive map presented at the start of this article, but instead of an equal-area map, it is a compromise cylindrical projection which tweens to the Mercator upon zoom.

The map above uses the exact same formula as the equal-area one, but with no horizontal axis distortion, only the value of a is tweaked as the zoom-level changes.

To see how this `a` variable behaves, in the UI below the compromise-cylindrical parameter

$a$

 is exposed directly: drag the slider, or scroll/wheel over the map itself. The map is a fixed square — as

$a$

 approaches 1 the poles simply run off the top and bottom edge, landing on a square, pole-truncated Mercator at the limit.

I would like to call out two specific aspect ratios as being interesting to me, shown below. They can each be compared to similar map projections of the same aspect ratio:

### Domino (2:1)

a = 0.882251819...

### Golden Rectangle (Φ:1)

Aspect-Adaptive Miller

a = 0.951505567...*Aspect-Adaptive Miller is the version of the "Compact Miller Cylindrical" in cases where the aspect ratio is not 1:0.6.

The new map style wastes considerably less space on the Arctic and Antarctic regions. Only around 0.3% of the globe lies north of Greenland, yet most compromise cylindrical projections dedicate 3–5% screen space to it; doing so helps Norway and Iceland look a little more natural. Greenland looks a little flatter on top, but if you've ever looked at Greenland on an actual globe, you'll see that none of these maps represent it well. A conic or polar azimuthal map is required for reasonable representation of Greenland.

## Formulas for the Ellipsoid Deep link

The formulas presented are modelled for a spherical Earth, just as is the case for "Web Mercator". Maps that model the ellipsoidal Earth can be easily supported by tweening from authalic latitude to conformal latitude prior to projection.

I plan to expand on the mathematical properties of this projection in a future blog post.

## How and why I made this Deep link

Map projection design is certainly a niche hobby. Too mathematical to be of interest to many map nerds. Too constrained and ugly to be of interest to many mathematicians.

Well, the thing that led to this rabbit hole was actually me just wanting a nice 2:1 aspect ratio map for the world, that showed country shapes well. I was surprised that I could not find any such map projection to meet my needs.

The simulation to the right is the content that I wanted that 2:1 map for. It is a representation of how a boat travelling west, circling the world roughly once every 37 days, will keep an identical clock to a person on Mars. This visualisation was intended for use in my article about time on Mars, however I never ended up including it as I ended up making that page static so it could be shared as a PDF.

When searching for the math that would create this look I wanted, it was clear to me that it needed to be similar to Mercator near the equator, and similar to an equal-area map near the poles.

After looking at the definition of the Mercator projection, I could see it was usually defined in terms of log and tan, but one definition usually further down the list stood out to me: the `atanh sin x` version. This definition is perfect because within it lies the function for equal area: `sin x`. Scaling this function down, and then back up again (after atanh), is a fairly simple way to create this tweening function.

## Novelty Deep link

This is certainly not the first aspect-adaptive map projection, in fact one of the examples above referred to "Aspect-Adaptive Miller", which can also adapt to various aspect ratios. What I think is novel is the combination of algorithmic simplicity and aesthetic result.

People have tried to create a more "tame" version of the Mercator projection by doing some kind of interpolation, whether that's interpolation of Mercator to Equirectangular (see Miller Cylindrical Projection ), or linear interpolation of Lambert cylindrical equal-area to Mercator (see Arden-Close Cylindrical (1947) ). Such interpolations usually leave the polar regions much larger than desired, leading to later "workarounds" like the "Compact Miller", which attempt to flatten the poles through specific mathematical tweaks layered on top.

A more flexible way of blending projections was outlined in Blending world map projections with Flex Projector (Jenny and Patterson, 2013). The tool discussed in the paper allows tweaking and blending map projections in realtime, a tool which was used by the same authors along with Bojan Šavrič to create the Equal Earth projection in 2018. Jenny also published a related but distinct paper on Adaptive Composite Map Projections .

Mapbox has had Adaptive Projections since 2021, allowing on-the-fly transitions between map projections.

Others have come up with ways to blend Lambert cylindrical equal-area and Mercator in mathematical non-linear ways. See Revolvable Indoor Panoramas Using a Rectified Azimuthal Projection (Fong, 2012). See the section: "A2.3 A Blended Cylindrical Map Projection". The formula presented in the paper is significantly more complex than the one presented here, and the paper states "the inverse equation for this projection is particularly gnarly".

The formula `atanh(sin(lat)a)/a` is so simple it's hard to imagine I'm the first to use it. I have dug through Snyder's seminal work "Map projections: A working manual", as well as his book "Flattening The Earth" and found no reference to this formula (as well as online search, and LLM queries). Nonetheless, I put this out in the world now, and if somebody knows of this formula being used in a prior map projection I would be happy to hear of it and update this page accordingly.

## Annexure A – Equal Area Proof Deep link

 for latitude and

$λ$

 for longitude. At

$z=0$

 (before the Mercator tween) the projection is:

$y=1atanh−1⁡(asin⁡φ),x=bλ(1−a2sin2⁡φ)$

A projection is equal area if every small patch of the sphere lands on the map with its area multiplied by the same constant. So take a tiny patch spanning

 of latitude and

$dλ$

 of longitude, and compare its area on the sphere with its area on the map.

### On the sphere

On a unit sphere the patch is

$dφ$

 tall, and

$cos⁡φdλ$

 wide, because circles of latitude shrink by

$cos⁡φ$

 towards the poles:

$sphere area=cos⁡φdφdλ$

### On the map

The limit of the shape on the map will be a rectangle or a parallelogram because the projection draws horizontal lines of latitude. Either shape's area can be obtained from width × height (vertical rise).

Width: Along a line of latitude,

$φ$

 is fixed and

$x$

 is simply

$λ$

 times a constant, so:

$width=b(1−a2sin2⁡φ)dλ$

Height:

$y$

 depends only on

$φ$

, so the height is

$dydφdφ$

. Using

$ddttanh−1⁡(t)=11−t2$

 and the chain rule:

$dydφ=1a⋅acos⁡φ1−a2sin2⁡φ=cos⁡φ1−a2sin2⁡φ$

$height=cos⁡φ1−a2sin2⁡φdφ$

Area: Width × Height; the

$(1−a2sin2⁡φ)$

 factors cancel:

$map area=b(1−a2sin2⁡φ)dλ⋅cos⁡φ1−a2sin2⁡φdφ=bcos⁡φdφdλ$

This is exactly

$b$

 times the area on the sphere, wherever the patch sits. So the projection is equal area, with a uniform scale factor of

Notice that

$a$

 cancelled out entirely: any value of

$a (0..1)$

 gives an equal area map. It controls the shape of the map, not its area properties.

## Next Time

This is just the first of several map related articles I will be publishing over the coming months. A future post will explore the geometric meaning of projecting a map this way, including how it can be applied to conic map projections, leading to maps that look a little like the one to the right. This is a custom map projection I have had on my law firm website (my day job) - National Probate and Estates Group. I suspect this is the only law firm in Australia with a custom map projection!

Notice how the lines of latitude are curved, but the states still appear nearly rectangular?

## 导航

- 项目页：[[10-项目/benjoffe.com_16c4d6f9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
