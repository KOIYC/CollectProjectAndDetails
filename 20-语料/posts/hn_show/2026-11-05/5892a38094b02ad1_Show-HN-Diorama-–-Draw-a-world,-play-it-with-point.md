---
type: "corpus"
item_id: "5892a38094b02ad1"
title: "Show HN: Diorama – Draw a world, play it with point and click"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50371859"
project_url: "https://grzegorz.tanczyk.pl/diorama"
author: "fullstackwife"
published_at: "2026-11-04T21:31:51Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_fullstackwife
  - story_50371859
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Diorama – Draw a world, play it with point and click

> [!info] 一句话导读
> Meta AI Global Hackathon

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50371859>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：fullstackwife　|　发布：2026-11-04T21:31:51Z
> 项目链接：<https://grzegorz.tanczyk.pl/diorama>
> 采集：2026-11-05T11:21:45+08:00　|　id：`5892a38094b02ad1`

## 正文

Diorama
Sketch to world
 How it works
 Worlds
 Make your own
 GitHub
Meta AI Global Hackathon · 2026
 Draw it. Walk into it.
Diorama turns a sketch or a single sentence into a small paper diorama world you can play in the browser.
Scroll, and the painting comes apart
 or skip ahead and play Paper Boat Storm
One painting Muse Image painted this quay from a crayon sketch.
SAM 3.1 · depth SAM cuts it into paper cards. A depth map stands each card at its own distance.
A stage Now a hero can walk in, behind the lamp post and in front of the boat.
Paper Boat Storm Three sketches, one paragraph, one playable world. Play it
Sketch → world
 One drawing becomes one place.
Drag across each picture. On the left, the crayon sketch Diorama got as input. On the right, the place it built and you can walk in. Muse Spark reads what is on the sheet, plans the place around it, and Muse Image paints it in cut paper and cardboard.
sketch world
1 The stormy quay
 Lamp posts become glowing paper lamps, the zigzag waves become folded paper sea, and the three little boats bob on it.
sketch world
2 The mill and the waterfall
 Even the misspelt “mil wheel” made it. The rope bridge is walkable, the waterfall pours, and every fish is its own cut-out that swims.
sketch world
3 The lighthouse rock
 The keeper waits in the doorway, as drawn. The yellow crayon beam is now a real beam that sweeps over the storm.
Not a flat picture Every place arrives in pieces…
Cards, flats, water …and folds into a stage: the waterfall, the mill wheel, the rope bridge.
Alive Every fish is its own cut-out that swims. The water flows, the clouds drift.
The last place It pops up like a page in a book.
As drawn The keeper waits in the lighthouse door, just where the sketch had him.
The ending The girl brings him the paper boat. The beam sweeps over the storm.
How a world is built
 Meta's models make it. Code checks it is playable.
Models do the creative work. Code measures and checks every result, so what comes out can be played, not only looked at. Each step writes plain files, and a typical four-place world takes about 17 minutes and some 200 Meta model calls.
Muse Spark World and story
 Places, a cast, items, locks and endings, with every ending checked to be reachable.
Muse Spark · Muse Image Layout and paint
 A shaded plan sketch for each place, painted over by Muse. A critic marks what is wrong and only those regions get repainted.
SAM 3.1 Cut-outs
 Every thing and floor cut out of the painting. Things the hero can take are painted out of a clean plate.
Code · depth The stage
 Floor, scale, occlusion, stairs and light measured from masks and depth. Cards, far flats, water, rain.
Muse Image · 3D Cast
 The hero and characters painted, cut out, turned into 3D models and drawn back as sprites in the world's style.
Sound Sound and voices
 Ambience, footsteps, music, and a fitting voice for every character.
Code · bots Verify
 Every place is walked and used by a bot. A place that fails is repaired automatically or handed to the agent.
Meta models at work
Muse Spark
 Designs the world and story, reads the sketches, lays out each place, critiques paintings, names what to cut out, judges playthroughs.
Muse Image
 Paints each place over its plan sketch, repaints flagged regions, paints the cast, their walk and talk sheets, and the item icons.
SAM 3.1
 Cuts the painting into things, floors, stairs and water. The masks become the walk grid, occlusion and pick-ups.
Muse Voice Transcribe
 Hears an idea said aloud, and listens to every voiced line to catch a take that does not say it.
Muse Code
 The Studio's agent. Click a thing on the stage, say what should change, and it fixes the world with you.
Also used: Depth Anything V2 for shadows and parallax, ElevenLabs for voices and effects, MusicGen for music, TRELLIS for the characters' 3D models.
Morning
 The storm passes.
Here is the whole world in motion, 47 seconds of it, cut from the game itself.
The next morning
 The sea is calm again.
and the paper boat made it ↘
Worlds
 Walk in. No install, no sign-up.
Worlds built with Diorama, playable in the browser on a computer or a phone. Click to walk, click things to look, take and use them, talk to people.
Play now 3 places cut paper sound on
Paper Boat Storm
A stormy night by the sea. A girl in a yellow raincoat has folded a letter into a paper boat and must bring it to the old lighthouse keeper before the storm gets worse.
your world next?
 Send a sketch or a story on X and I'll build it with Diorama. New worlds land on this shelf.
Send it on X
How to use it
 Make your own world.
Diorama runs on your computer: a command-line tool and a Studio app in the browser. You need Node 22+ , ffmpeg and a Meta Model API key . ElevenLabs (sound) and Hugging Face (3D characters) keys are optional.
Set up
 In an empty folder. Nothing to clone or install: it checks this machine and asks for your keys, typed hidden and stored encrypted.
 mkdir my-worlds && cd my-worlds
npx -y @gtanczyk/diorama setup
Build in the Studio
 Describe a world in one sentence or drop in your sketches, watch it build place by place, then play it and fix what you want with the agent.
 npx -y @gtanczyk/diorama studio
Share it
 Export the world as a static web page for GitHub Pages, itch.io or any host. Your worlds are saved in ./worlds.
 npx -y @gtanczyk/diorama export
Diorama on GitHub
 Setup guide
Notes
About the sketches. No child drew the three storm sketches. They were generated with Muse Image to look like crayon drawings, then given to Diorama as input together with one paragraph of story. After the build, a few spots in the world were touched up by hand for the clip.
About the project. Diorama was written during the Meta AI Global Hackathon, from the kickoff on 26 October 2026. It runs locally as a command-line tool and a Studio app, and exports each world as a static web page.
Diorama · made by Grzegorz Tańczyk
 x.com/gtanczyk · github.com/gtanczyk/diorama
Sound on

## 导航

- 项目页：[[10-项目/grzegorz.tanczyk.pl_4b2ea17a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
