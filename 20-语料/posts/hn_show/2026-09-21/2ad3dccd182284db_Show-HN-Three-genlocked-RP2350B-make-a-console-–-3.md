---
type: "corpus"
item_id: "2ad3dccd182284db"
title: "Show HN: Three genlocked RP2350B make a console – 3k sprite pixels per line)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49778008"
project_url: "https://papydeck.eu/"
author: "papyDoctor"
published_at: "2026-09-20T17:37:06Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_papyDoctor
  - story_49778008
  - show_hn
metrics: {"points": 11, "comments": 7, "engagement_velocity": 11}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:3d"
---

# Show HN: Three genlocked RP2350B make a console – 3k sprite pixels per line)

> [!info] 一句话导读
> papyDeck — A little console you can open

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49778008>
> 指标：点赞=11 · 评论=7 · engagement_velocity=11
> 作者：papyDoctor　|　发布：2026-09-20T17:37:06Z
> 项目链接：<https://papydeck.eu/>
> 采集：2026-09-21T09:44:03+08:00　|　id：`2ad3dccd182284db`

## 正文

papyDeck — A little console you can open

# A little console you can open

papyDeck plays like an arcade machine and opens like a text editor. Every game on it is a Lua script you can read, change, and rewrite — including the ones somebody else wrote.

640×480 at 60 Hz over HDMI

3 000 sprite pixels per scanline

6 Cortex-M33 cores

60 mm square board

## The game is the source

There is no locked cartridge and no compiled blob. A game is a folder on the micro-SD card: a `main.lua`, its art, and nothing else. Change a number, save, and the game runs differently on the next frame.

The virtual machine is sandboxed — no filesystem, no OS calls, no arbitrary loading — so a bad script gives you an error message with a line number instead of a dead console. The same core also runs in a browser simulator, bit for bit: what you see there is what the board shows — open it above, read a tutorial’s source, change a number and run it again.

```
-- A sprite that follows the D-pad. That is the whole program.
gfx.bundle()                       -- the game's art, from its folder
local ship = gfx.id("game/ship")
local x, y = 320, 240

function _update()
  local p = pad.get()              -- any gamepad
  if p & pad.LEFT  ~= 0 then x = x - 2 end
  if p & pad.RIGHT ~= 0 then x = x + 2 end
  if p & pad.UP    ~= 0 then y = y - 2 end
  if p & pad.DOWN  ~= 0 then y = y + 2 end
end

function _draw()
  gfx.sprite(ship, x, y)
end

```

## See it run

Two games, each recorded twice: in the browser simulator, then on the board itself over HDMI. Same Lua, same art, same engine — that is the whole point of the simulator, and the only honest way to show it is side by side. Sound is on.

- In the simulator ▶ shmup youtube.com ↗
- In the simulator ▶ platformer youtube.com ↗
- On the console ▶ shmup youtube.com ↗
- On the console ▶ platformer youtube.com ↗

### Write your own

Lua on board, a sandboxed VM, and errors that print a line number instead of taking the console down. No toolchain, no cross-compiler, no cable: write it, copy the folder to the card, play.

### Play what others wrote

Games are plain folders. The console lists the published games, fetches one over Wi-Fi onto its card, and you can open the source right after — see exactly how the trick was done.

### Open by licence, public soon

Hardware under CERN-OHL-P, firmware under MIT: the licences are chosen and their notices are already in the tree. The repositories are still private while the V1 board lands — when they open, the schematic, the board and every line of firmware are yours to read, fork and manufacture.

### Real arcade guts

Three genlocked RP2350B, six cores, 3 000 opaque sprite-pixels per scanline measured on the board — roughly twice a Neo Geo — plus a scrolling tile background, over plain HDMI, with no tearing by construction.

## Where the project stands

The V1 alpha board arrived on 26 August 2026 and has been on the bench since. Running today: HDMI out from the three genlocked chips, sprites and a scrolling tile background, games loaded from the micro-SD card, Bluetooth gamepads, Wi-Fi, published games downloaded straight onto the card from the console’s own menu, four-channel music and sampled effects out of the headphone jack, and the console updating its own four firmwares over the air. A browser simulator runs the same core as the board, with tutorials you can read and clone. Still open: HDMI audio, the verified leaderboard, and the V1 board itself — a voltage supervisor and a secure element are going on it.

Nothing here is for sale, and there is no release date. The pages below are the honest version: measured figures, decisions with their reasons, and the parts that are still open.

- ## Firmware

Software architecture, the protocol between the cores, porting notes.
- ## Hardware

The board, its design decisions, the 3D model.

# ZIZKA-AI-SL/ZizkaDB

## 评论（7/7）

> **tliltocatl** · 2026-09-20T18:50:48.000Z　
> Love the idea, hate the presentation. Also, wasn't able to find the simulator link, is the simulator not publicly accessible?Also, one friendly tip - if you are EU-based and plan to sell the hardware, drop the ESP32/wireless. Yes, that would mean no wireless pads, but it will make regulatory compliance a lot easier. Maybe replace with a breakout socket (not sure if that is allowed).

---

> **Retr0id** · 2026-09-20T19:11:25.000Z　
> So, why are there 3 of them? I can make several guesses but I don't see any concise answers on the page.

---

> **Retr0id** · 2026-09-20T19:09:09.000Z　
> Isn't the appeal of those esp32 modules that they're already compliant, as a module? Or do you still need the product as a whole to be compliant?

---

> **papyDoctor** · 2026-09-20T19:38:11.000Z　
> Yes there is a link on the homepage.About the ESP, the module is FCC compliant with its number written on it.

---

> **tliltocatl** · 2026-09-20T19:22:31.000Z　
> > Or do you still need the product as a whole to be compliant?I'm not 100% sure, but I've been thru a round on RED (on a full-custom device) and much of it involved security and authentication within application software. RED basically boils down to "we are fucking tired of your little plastic shit running botnets, the customer are clueless, so fix it if you want to sell it".So actual code review and running tests in front of the auditors, basically everything short of a pentest, not just RF PHY stuff. So my gut feeling is that while you can skip the stuff related to RF PHY if you use an off-the-shelf module, the rest will is still be on you.Based on quick googling the certifiers agree with me (but again, that's not same as as a court saying that's true): https://compliancetesting.com/ce-certification-for-espressif...

---

> **ranger_danger** · 2026-09-20T20:14:40.000Z　
> https://emcfastpass.com/fcc-rules-kits-subassemblies/

---

> **tliltocatl** · 2026-09-20T19:43:28.000Z　
> > the module is FCC compliant with its number written on it.Just like I'm telling in the sibling comment - IANAL but that's probably not enough for EU. RED cares not just about RF PHY, but also for example if you can ran a FOTA update, and if you do, is the key secure enough. So module being compliant simplifies things, but your device might still require a cert as a whole. Again IANAL, this is based on my experience with certifying a full-custom device.

## 导航

- 项目页：[[10-项目/papydeck.eu_6563af10]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
