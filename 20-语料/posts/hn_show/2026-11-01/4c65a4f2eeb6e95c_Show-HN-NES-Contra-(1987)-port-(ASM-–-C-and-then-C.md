---
type: "corpus"
item_id: "4c65a4f2eeb6e95c"
title: "Show HN: NES Contra (1987) port (ASM –> C and then C –> WebAssembly)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50319169"
project_url: "https://epoyraz.github.io/nes-contra-us"
author: "tevlon"
published_at: "2026-10-31T19:18:48Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_tevlon
  - story_50319169
  - show_hn
  - front_page
metrics: {"points": 50, "comments": 31, "engagement_velocity": 50}
comments_count: 31
comments_total: 31
discovered_via: "hn:show_hn:3d"
---

# Show HN: NES Contra (1987) port (ASM –> C and then C –> WebAssembly)

> [!info] 一句话导读
> Based on vermiceli's annotated disassembly of Contra: https://github.com/vermiceli/nes-contra-us. Thanks for the great work.I ported it in two steps. First to C…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50319169>
> 指标：点赞=50 · 评论=31 · engagement_velocity=50
> 作者：tevlon　|　发布：2026-10-31T19:18:48Z
> 项目链接：<https://epoyraz.github.io/nes-contra-us>
> 采集：2026-11-01T09:38:09+08:00　|　id：`4c65a4f2eeb6e95c`

## 正文

Based on vermiceli's annotated disassembly of Contra: https://github.com/vermiceli/nes-contra-us. Thanks for the great work.I ported it in two steps. First to C: the game logic is translated routine by routine from the 6502 assembly, and checked frame by frame against the original in the Mesen emulator. Then the C code to WebAssembly so it runs in the browser.The cherry on top: online multiplayer, so two players can play co-op over the internet.Source: https://github.com/epoyraz/nes-contra-us

## 评论（31/31）

> **BSPtree** · 2026-10-31T19:49:49.000Z　
> Cool, how did you build the multiplayer mode? And how much AI was used?

---

> **gwbas1c** · 2026-10-31T20:19:04.000Z　
> One of the things that I'm curious about: How easy / hard is it to use the same NES game with higher resolution / color graphics, and sample-based sound?Are there any emulators out there that let you swap in higher resolution assets so a game can be freshened without a complete port?

---

> **einpoklum** · 2026-10-31T20:32:40.000Z　
> Most of the keys aren't working for me in Firefox though :-(

---

> **raldi** · 2026-10-31T21:07:23.000Z　
> But the Japanese Contra was so much better! https://www.youtube.com/shorts/CiXzONyCDW0

---

> **Dwedit** · 2026-10-31T21:50:48.000Z　
> All that work and then somehow transposing the A and B keys at the very end.

---

> **shinryudbz** · 2026-10-31T22:01:54.000Z　
> Is the audio not supposed to work? I was hoping to hear the legendary tracks!

---

> **gosen** · 2026-10-31T22:04:58.000Z　
> thanks for bringing back my childhood memories!

---

> **egonschiele** · 2026-10-31T22:20:28.000Z　
> Contra is my favorite game of all time so this is a real treat, and the co-op idea is fantastic. Not to be greedy, but how hard would it be to add music? :)

---

> **pxx** · 2026-10-31T22:59:21.000Z　
> No controller support?

---

> **msephton** · 2026-10-31T23:57:42.000Z　
> A couple months ago I wrote about this kind of transcompilation hop-skip-jump: https://news.ycombinator.com/item?id=49643284I used it to get games written in Lua running on SNES and in my own language/engine running on Dreamcast, Wii, Web and more.

---

> **jasonlotito** · 2026-11-01T00:02:38.000Z　
> Whenever I see a game that uses the arrow keys and doesn't offer WASD as well, I can't help but see a game written by a non-gamer. I consider these fundamentals, and a shibboleth of whether I should care.

---

> **pmarreck** · 2026-11-01T01:16:41.000Z　
> Where's the sound? You can likely ask AI to emulate the sound hardware with WASM!

---

> **erictheguy** · 2026-11-01T01:32:07.000Z　
> Nostalgic!! Took me a few tries to beat the first level haha

---

> **tevlon** · 2026-10-31T21:00:28.000Z　
> For the Multiplayer part: It's deterministic lockstep. Both browsers run the same C core (compiled to WebAssembly), and the only thing sent over the network is each player's button bitmask per frame. Local input is delayed by 4 frames (~67 ms), which hides normal internet latency; if the other player's input for a frame hasn't arrived yet, the game waits for it. Every 2 seconds both sides compare a hash of the game RAM to catch desyncs. Transport is a WebRTC data channel via PeerJS (its free cloud server handles matchmaking with a room code), with Google's STUN server for NAT traversal and Metered's free-tier TURN relay as a fallback when a direct connection isn't possible.For AI usage: It was all done by Claude/Codex, but it wasn't that straight forward. First: i started in April and the models weren't good enough and would make errors. You could see those immediately in glitches. Then, i spent some time in building a harness and collect telemetry data in Mesen. Once, i had that: i just played the game in the emulator and asked Claude Opus 5.5 to use this as verification. The rest was smooth.

---

> **esikich** · 2026-10-31T22:17:52.000Z　
> 100% AI I'm sure. I played around with this kind of thing a month or so ago and Codex had no problems mashing games up from just the ROMs. In about 30 minutes I had the contra guys running through SMB 1 shooting enemies.

---

> **Emjayen** · 2026-11-01T00:11:01.000Z　
> I think you know the answer to that; they poked and prodded their surrogate mommy to do their homework for them.

---

> **kekebo** · 2026-10-31T20:29:37.000Z　
> Idk about swapping assets but zsnes used to have a range of video filters that could improve the experience on a modern screen quite a bit.Edit: For SNES, not NES, my bad.

---

> **unleaded** · 2026-10-31T20:40:45.000Z　
> Mesen has texture packs. Don't know about sound, you'd have to reverse each game's sound driver first. https://vgmpf.com/Wiki/index.php?title=Famicom/NES_Sound_Dri...

---

> **BSPtree** · 2026-10-31T20:41:06.000Z　
> I would not think so, at least not in a meaningful way. That would require to edit the cartridge data thus the ROM, as all sprite data was contained within the cartridge. Sample based sound is impossible natively, as NES and older game consoles don't work with digital data but synthesizers. You could perhaps synthesize the music to WAV files and then enchance it. But then again, NES and thus its emulators have no way of playing digitized audio!

---

> **vunderba** · 2026-10-31T20:58:22.000Z　
> You might like 3dSen, which came out several years ago. It does some pretty crazy stuff, converting NES games into essentially 3D voxel environments.https://store.steampowered.com/app/1147940/3dSen_PC

---

> **tevlon** · 2026-10-31T20:53:00.000Z　
> i only testing in chrome. Will look into it!

---

> **anonymous908213** · 2026-11-01T00:06:33.000Z　
> While I'm not defending a slop port, I have to question your gamer credentials. Maybe by gamer you mean a Call of Duty player? WASD is traditional for FPS/TPS games that expect you to have one hand on the mouse. Most 2D games, and every emulator I've ever used, have never offered WASD.

---

> **waltbosz** · 2026-10-31T23:57:33.000Z　
> Can you elaborate on the process? Do you just provide it with the ROMs and it is able to pull apart the relevant sprites and code pieces, and recombine into a new ROM?

---

> **gwbas1c** · 2026-11-01T01:09:02.000Z　
> Yeah, its upscaler is nicer than the Switch and the mini SNES.

---

> **cowlevel** · 2026-10-31T20:44:53.000Z　
> The NES in particular is probably not too difficult to upscale, because the graphics data is stored on its own ROM chip (sometimes RAM) in a well structured layout. SMB1 just uses a ROM chip containing many tile graphics which the CPU code addresses by tile index. It would be really easy for an emulator to use the same tile indices to address any arbitrary set of tiles loaded from a PNG. Some games use RAM, which makes it harder as you'd have to index the PNG by hash or something.

---

> **pantelisk** · 2026-10-31T20:50:03.000Z　
> Compute motion vectors, faux depth, and add DLLS5 to it maybe? Could be pretty cool, or pretty horrific. Only one way to find out :)

---

> **kevin_thibedeau** · 2026-10-31T23:31:39.000Z　
> > Sample based sound is impossible natively, as NES and older game consoles don't work with digital dataThe NES supports PCM audio. It was notably implemented wrong in the title screen of Double Dribble and fixed with a patch that produces clearer audio after bit reversal into the correct encoding for the hardware:https://www.youtube.com/watch?v=Jli0RGpuZDg

---

> **tevlon** · 2026-10-31T21:01:34.000Z　
> whoa, that's cool. I didn't know about this. Thanks for sharing!

---

> **literallyanythi** · 2026-11-01T00:13:21.000Z　
> correct me if i'm wrong, gamer credential questioner, but WASD was immortalized by the id Software "win Carmack's ferrari" tournament. Before then EDSF was also popular because it gave you more keys on the left side for hotkeys.I do think you're objectively correct in your post, but I think what the grandparent meant was that "The author isn't actually interested in playing Contra on his website" which is why QoL stuff like that wasn't added and it "smells" like it should be there if you cared about playing on the thing you actually shared to HN.
> I know the first thing I would do would be to add wasd + mouse support to Contra, since the control scheme is the reason I don't try to play it. But at the same time I have never been interested in games that deliberately limit your controls as a form of difficulty (feels like a Japanese gamedev thing, from Resident Evil to Dark Souls)

---

> **justsomehnguy** · 2026-11-01T00:20:25.000Z　
> NB: WASD won because most (like 99%) of the keyboards did had (and I can bet cheap shit still have) some dead keys aka 'key ghosting' on ESDF.

---

> **literallyanythi** · 2026-11-01T00:32:28.000Z　
> You awoke negative-nostalgia to membrane keyboards where I remember I couldn't hold Shift + W + A at the same time in Minecraft as a kid so you're definitely right about bad keyboards, but I remember dead keys on WASD as well.
> I wasn't there, but the largest consensus seems to be that Quake popularized it, plain and simple. I'm sure other factors like what you mention helped it become the dominant layout as welledit: figured out why that nostalgia happened. I was revisiting an old flash game I liked [0] and people were complaining to the dev about this exact key ghosting issue to him when it wasn't his fault but a fault of their keyboards, and in the Newgrounds description he links to a forum post [1] elaborating on the issue[0] https://www.newgrounds.com/portal/view/547881[1] https://board.flashkit.com/board/showthread.php?789015-wont-...

## 关联链接

- https://github.com/epoyraz/nes-contra-us
- https://github.com/vermiceli/nes-contra-us.

## 导航

- 项目页：[[10-项目/epoyraz.github.io_f9b76a95]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
