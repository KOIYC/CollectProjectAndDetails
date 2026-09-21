---
type: "project"
title: "Show HN: Three genlocked RP2350B make a console – 3k sprite pixels per line)"
project_url: "https://papydeck.eu/"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_papyDoctor
  - story_49778008
  - show_hn
lang: "en"
---

# Show HN: Three genlocked RP2350B make a console – 3k sprite pixels per line)

> [!info] 一句话导读
> papyDeck — A little console you can open

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://papydeck.eu/>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_papyDoctor, story_49778008, show_hn
> 最新指标：点赞=11 · 评论=7 · engagement_velocity=11

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=11 · 评论=7 · engagement_velocity=11 | [[20-语料/posts/hn_show/2026-09-21/2ad3dccd182284db_Show-HN-Three-genlocked-RP2350B-make-a-console-–-3]] |

## 摘要正文

papyDeck — A little console you can open  # A little console you can open  papyDeck plays like an arcade machine and opens like a text editor. Every game on it is a Lua script you can read, change, and rewrite — including the ones somebody else wrote.  640×480 at 60 Hz over HDMI  3 000 sprite pixels per scanline  6 Cortex-M33 cores  60 mm square board  ## The game is the source  There is no locked cartridge and no compiled blob. A game is a folder on the micro-SD card: a `main.lua`, its art, and nothing else. Change a number, save, and the game runs differently on the next frame.  The virtual machine is sandboxed — no filesystem, no OS calls, no arbitrary loading — so a bad script gives you an error message with a line number instead of a dead console. The same core also runs in a browser simulator, bit for bit: what you see there is what the board shows — open it above, read a tutorial’s source, change a number and run it again.  ``` -- A sprite that follows the D-pad. That is the whole program. gfx.bundle()                       -- the game's art, from its folder local ship = gfx.id("game/ship") local x, y = 320, 240  function _update()   local p = pad.get()              -- any g…
