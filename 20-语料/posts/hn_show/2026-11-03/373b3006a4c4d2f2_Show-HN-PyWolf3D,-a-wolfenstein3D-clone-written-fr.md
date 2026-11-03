---
type: "corpus"
item_id: "373b3006a4c4d2f2"
title: "Show HN: PyWolf3D, a wolfenstein3D clone written from scratch in Python"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50338891"
project_url: "https://github.com/atifcodesalot/pyWolf3D"
author: "BSPtree"
published_at: "2026-11-02T16:09:13Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_BSPtree
  - story_50338891
  - show_hn
metrics: {"points": 16, "comments": 2, "engagement_velocity": 16}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: PyWolf3D, a wolfenstein3D clone written from scratch in Python

> [!info] 一句话导读
> atifcodesalot/pyWolf3D

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50338891>
> 指标：点赞=16 · 评论=2 · engagement_velocity=16
> 作者：BSPtree　|　发布：2026-11-02T16:09:13Z
> 项目链接：<https://github.com/atifcodesalot/pyWolf3D>
> 采集：2026-11-03T09:40:36+08:00　|　id：`373b3006a4c4d2f2`

## 正文

# atifcodesalot/pyWolf3D

a wolfenstein 3D clone in python, pygame

- Stars: 9
- Forks: 0
- Watchers: 9
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-01T14:41:13Z

## Languages

- Python

## Topics

- python3
- raycasting
- wolfenstein-3d

## Top Contributors

- atifcodesalot (309 contributions)

---

## README

# pyWolf3D

https://github.com/user-attachments/assets/8f8b9bce-8b39-4466-87e9-77726cfd09f6

Please excuse my mouse sounds in the demo :sweat_smile:

## What is pyWolf3D?

PYWOLF3D is a Wolfenstein 3D engine, game clone written from scratch in pygame, Python.

## Why?

I am a huge Doom and Wolfenstein fan so I just decided to rewrite one of the originals myself :sunglasses:. It was mostly for fun and learning.

## Code authorship

All code present in this project was written by me, without AI code generation or coding agents. AI tools were used for discussion, research, and help locating existing game assets and resources. The implementation, including map parsing, rendering, actor behavior, and game logic is entirely my own work. But don't take my word for it: https://isvibecoded.com/.

## Some screenshots

## How to play?

### Episode 1 shareware version

To play the shareware version of episode 1, simply clone this repository:

```
git clone https://github.com/atifcodesalot/pyWolf3D
```

change the directory to the root of the project:

```
cd pyWolf3D
```

Then install the required packages;

For `Windows`:

```
py -m pip install -r requirements.txt
```

For `Unix`:

```
python3 -m pip install -r requirements.txt
```

Then run;

For `Windows`:

```
py -m wolfenstein3D
```

For `Unix`:

```
python3 -m wolfenstein3D
```

### Original Maps

You can now play all 6 episodes, but they complete, except mecha hitler boss, (but will be completed in the near future).
If want to play all of the episodes, you will need to drop the game files: `GAMEMAPS.WL6`, `MAPHEAD.WL6`, `AUIDOT.WL6` and `AUIDOHED.WL6` from your purchased installation into the `./wolfenstein3D/assets/maps` folder, I also wrote a simple script to
detect it automatically if you have a steam installation of the game.

## Info on the project

I tried to keep this clone as accurate as possible (compared to the original)
but some things are probably different. The damage model and actor behaviour are mostly similar, but your bullets pass through enemies in this version, for example.
The clone currently supports playing the original 6 episodes but it is incomplete as mentioned. It extracts the original maps from the shareware version files `MAPHEAD.WL1` and `MAPTEMP.WL6` and music from `AUIDOT.WL6` and `AUIDOHED.WL6` files. If you want to play the original episodes, as previously stated, you will need to drop the `GAMEMAPS.WL6`, `MAPHEAD.WL6`, `AUIDOT.WL6` and `AUIDOHED.WL6` from your
purchased installation, into the `./wolfenstein3D/assets/maps` folder.

### Technical stuff

#### Rendering

The game employs a raycaster just like the original for rendering, there is no actual rasterization.
The default amount of rays cast are 160 and
the default fov is 54 degrees. You can play around with it.
It is simple and reusable.

The maps are 64 to 64 grids and the raycaster uses the DDA algorithm to
find collisions with the non empty tiles. The special cases are doors and pushwalls,
which the raycaster handles explicitly.

Sprites, projectiles are rendered via perspective projection.

#### Sound

The sound engine is responsible for attenuation and directional sound.
Directional sound is achieved by panning the audio via hardcoded configurations.
The sound propagation is done via the preprocessed area tiles.
Some of the sound effects (and music), like treasure pickup, were actually synthesized during runtime
in the original, this version uses .wav files for all sound effects.

#### Music
Music are actually synthesized during runtime using an OPL emulator using `AUIDOT` and `AUIDOHED` files!
The justification is that I can't just redistribute the non-shareware music with this repo, which is under copyright law.
So you drop the files that you already got and the music files are created on the fly!

## Credits

- Code: All of the components, WL1, WL6 file parsing, rendering, sound and game logic were implemented by me, as mentioned; AI wasn't used in anyway for code generation.
- Sprites, sounds: The sprites, sounds of the original were obtained from the internet, sometimes via LLM's (some sprites are relatively obscure \[like fake hitler or mecha hitler sprites\])
- Pacman sprites from Ultimecia

## Resources

- game engine black book Wolf3D is an awesome book
 and I have read it extensively during the development of this clone. Chase state chains, sprite rendering, sound propagation and many other aspects, I understood from this book and enjoyed its every page, it truly is awesome.
- https://www.spriters-resource.com/ms_dos/wolfenstein3d/ for the original sprites.
- https://sounds.spriters-resource.com/ms_dos/wolfenstein3d for general sound effects.
- https://forum.zdoom.org/viewtopic.php?t=46658 this forum post for adlib sound effects in .wav format.

## Features yet to be implemented

- Floor finish screen (working on it)
- Projectiles, more episode sprites and texture support (working on it, almost done)
- Episode 1 ending animation
- Spear of Destiny
- Multiplayer deathmatch

## Bugs

I have been working on this for some time now, so I decided to just put it out there before it was
well... perfect. There are some non game-breaking (in my opinion :D) bugs that I am aware of and will fix it in the future. If you notice any, let me know though.

# election-vibe

## 评论（2/2）

> **ScreenWardenApp** · 2026-11-03T00:35:49.000Z　
> Wow, this takes me back. I'm curious how much time you have in this?

---

> **antman** · 2026-11-03T01:13:00.000Z　
> From the project page “All code present in this project was written by me, without AI code generation or coding agents”

## 关联链接

- https://forum.zdoom.org/viewtopic.php?t=46658
- https://github.com/user-attachments/assets/8f8b9bce-8b39-4466-87e9-77726cfd09f6
- https://isvibecoded.com/.
- https://sounds.spriters-resource.com/ms_dos/wolfenstein3d
- https://www.spriters-resource.com/ms_dos/wolfenstein3d/

## 导航

- 项目页：[[10-项目/github.com_22030db8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
