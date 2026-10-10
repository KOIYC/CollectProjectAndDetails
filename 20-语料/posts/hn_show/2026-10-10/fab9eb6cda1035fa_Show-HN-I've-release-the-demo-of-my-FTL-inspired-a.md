---
type: "corpus"
item_id: "fab9eb6cda1035fa"
title: "Show HN: I've release the demo of my FTL-inspired autobattler game – Cosmo Cargo"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50020552"
project_url: "https://pixelnest.itch.io/cosmo-cargo"
author: "valryon"
published_at: "2026-10-09T13:50:56Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_valryon
  - story_50020552
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: I've release the demo of my FTL-inspired autobattler game – Cosmo Cargo

> [!info] 一句话导读
> Cosmo Cargo by Pixelnest Studio

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50020552>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：valryon　|　发布：2026-10-09T13:50:56Z
> 项目链接：<https://pixelnest.itch.io/cosmo-cargo>
> 采集：2026-10-10T09:53:50+08:00　|　id：`fab9eb6cda1035fa`

## 正文

Cosmo Cargo by Pixelnest Studio

# Cosmo Cargo

 Run game

Note from the devs : this is an early version of the game. Most assets, sounds and mechanics are not finals. You may encounter some bugs or get softlocked, sorry if that hap pen.

The galaxy is in danger! The fearsome Administrators are on a mission to organize the universe as they see fit, and destroy everything they consider disorderly.

But there's still hope! A rebel force is preparing to foil their plans.

Travel through different sectors and meet amazing aliens who can help you in your fight!

Items are essential! Buy, trade, find and steal all kinds of wacky items with powerful effects.

- Combine them aboard your ship to create new synergies, high-powered chain reactions, and satisfying combos.
- Upgrade them by collecting copies to unlock new effects.
- Expand your inventory by clearing cluttered slots to unlock even more possibilities.

Traveling alone is no fun, and there's room in the ship's cockpit... Why not recruit some new crew members?

These new characters can use their unique powers in combination with the ship's equipment for even more exciting combos.

The Administrators seek to eradicate disorder in the universe. Join the Rebels and help them defeat the minions of this fearsome organization.

Engage in epic space battles matching inventory against inventory.

Face increasingly tough (and weird) enemies using items collected throughout the sector.

Once the minions have been defeated, your final mission will be to defeat the Chief Administrator — so you'd better be prepared!

| Updated | 4 days ago |
| --- | --- |
| Status | In development |
| Platforms | HTML5, Windows, macOS, Linux |
| Publisher | Pixelnest Studio |
| Rating | Rated 4.9 out of 5 stars(11 total ratings) |
| Author | Pixelnest Studio |
| Genre | Strategy |
| Made with | Unity |
| Tags | Auto Battler, Deck Building, Roguelike, Roguelite, Sci-fi, Singleplayer |
| Average session | About a half-hour |
| Languages | English, French, Chinese (Simplified) |
| Inputs | Mouse |
| Links | Steam |
| Content | No generative AI was used |

cosmocargo-0.11.0-macOS (demo SNF).zip 154 MB

cosmocargo-0.11.0-linux (demo SNF).zip 146 MB

## Development log

- Demo Update - 0.11.0

 4 days ago
- Demo Update - 0.10.0

 17 days ago
- Demo Update - 0.9.4

 21 days ago
- Demo: Major Update! New content, new systems, major rework

 30 days ago
- Cosmo Cargo - web demo update

 Jun 12, 2026
- Cosmo Cargo - a new demo is available!

 May 28, 2026

## Comments

Skeppartorsk 206 days ago

The upgrade "Item on left side applies +1 charge to that item" doesn't do what it says at all. In fact what it actually does, is it increases the cooldown of the item itself by 1s, thus making it so that it will never ever trigger. I have 2x multicast soldering irons next to a Laser Turret with that upgrade. What should happen is that every time my Solder Irons trigger they should charge for 2s giving them 1s cd. What's actually happening is that my laser turret ends fights with 20s/6s CD and never goes off ever.

The crew member that gives +1 multicast to 2x1 items only gives the text that says the item has 2x multicast. It doesn't actually give multicast. They still only go off once.

A lot of other upgrades have similar issues where they just do not work at all, or you need to move the item for it to update and start working. Sometimes moving it only updates it to make it look like it works (adding multicast text and trigger fields) but the effect doesn't happen. The first time I gave my minigun +3 haste to random item it just perma-hasted all my items. The 2nd time, it never ever hasted anything.

Pixelnest Studio 205 days ago

Thanks for testing! Seems like you had a very cursed run, sorry for that. We'll investigate and fix those bugs. Cheers!

Skeppartorsk 205 days ago (3 edits)

Also enemy burn never ticks down. I was wondering how the early game burner that should at most ever be able to peak at ~14 burn was applying 30+ burn to me. It's cause the ticks don't do the -1 at all. So it just infinitely stacks burn (slowly).

Trying to sell +x damage modules to a shop that has weapons in it will instead buff all the weapons in that shop. Normally annoying, but could also be used to apply the same buff to like 4x weapons at the same time, and then buy them all buffed.

Scented Candle does nothing, my Soldering Iron still has 2 Burn with it in inventory, and if you have both Scented Candle and Meteor affecting the same burn item it sets that items burn to 0.

also bonus completely reasonable amounts of burn on final boss:

The ammo reload upgrade here doesn't work either. Never got +ammo from the two multicasters above it:

obliviondoll 207 days ago(+1)

This is fun so far. Hopefully when the full game is ready for launch, you publish it here too, not just Steam. Great work already though!

Pixelnest Studio 206 days ago(+1)

Thank you, glad you liked it!

Skeppartorsk 207 days ago(+1)

Virus vs. Virus just goes full infinite and whichever side has flat damage instantly kills the other side. Also virus in general is just incredibly overpowered.

Netsmile 210 days ago(+1)

I absolutely loved this. You guys are legends!

Pixelnest Studio 207 days ago

Thanks for your kind words!

rubyton 210 days ago (1 edit) (+1)

So much fun with the trigger chains. Well, that's until the endgame when the Death Ray appeared... with item upgrades preferring bonus haste the death ray fired almost immediately after combat start, the final boss didn't even last 2 seconds.

Pixelnest Studio 207 days ago

And so, you discovered the forbidden Deathray-justu, hope you had fun on-shoting everything!

De2nail 211 days ago(+1)

hold up.. more starship games? count me in

Pixelnest Studio 207 days ago

And you're welcome in!

DanielLC 211 days ago(+1)

I got one weapon that got more powerful every time you used ammo, and another that granted ammo to everything adjacent, and got a bunch of stuff with ammo, and everything went down fast.

Pixelnest Studio 207 days ago

Just pewpewpew those stupid Administrators!

Devlinr 213 days ago(+1)

Really enjoyed this, the builds are fun!

Pixelnest Studio 207 days ago

Thank you!

VerzatileDev 213 days ago(+1)

Looks coold, well done wih the game does remind me a lot of "FTL", and it has some core similairities though has a new modern approach to it and a lot of cool diferent vibes to go around with it, nice work1

Pixelnest Studio 213 days ago(+1)

Thanks <3

# athrael-soju/Narwhal

## 评论（1/1）

> **lemontheme** · 2026-10-09T14:56:08.000Z　
> Neat! My guess would have been Lonestar as the main inspiration. Autobattlers aren't my main genre. Even the much-loved He Is Coming bores me after half an hour, but I'll give this a whirl!

## 导航

- 项目页：[[10-项目/pixelnest.itch.io_54c449e7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
