---
type: "corpus"
item_id: "c39c83e2e0446881"
title: "Show HN: Curvytron 2, I rewrote my browser party game, 10 years later"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733433"
project_url: "https://curvytron2.com/"
author: "tom32i"
published_at: "2026-06-30T14:45:19Z"
captured_at: "2026-09-21T01:44:27+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_tom32i
  - story_48733433
  - show_hn
metrics: {"points": 15, "comments": 5, "engagement_velocity": 15}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:113d"
---

# Show HN: Curvytron 2, I rewrote my browser party game, 10 years later

> [!info] 一句话导读
> Hi everyone, french web dev here,About 10 years ago I did a little party game in the browser inspired by Achtung die Kurve genre, it reached HN (https://news.yc…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733433>
> 指标：点赞=15 · 评论=5 · engagement_velocity=15
> 作者：tom32i　|　发布：2026-06-30T14:45:19Z
> 项目链接：<https://curvytron2.com/>
> 采集：2026-09-21T01:44:27+08:00　|　id：`c39c83e2e0446881`

## 正文

Hi everyone, french web dev here,About 10 years ago I did a little party game in the browser inspired by Achtung die Kurve genre, it reached HN (https://news.ycombinator.com/item?id=9494619) and everything went crazy, it's still largely played in open-spaces all over the world today.This past year, I've been working on a sequel: https://curvytron2.com is live.Same goal as the first one: challenge myself, perfect my skills, have fun and give back to the internet community the best way I know; by just putting a free little fun game out there. No ads, no tracking, no business plan.A decade of professional web development and hours of GMTK have raised my expectations and this time I aimed for:- a good looking top-down 3D view with improved gameplay and real game juice: I learn Three.JS and WebGL for this project, worked on the camera movements, screen shake, sound design, gameplay feedback and I'm proud of the portal-like effect of the bonus that allows you to peak and cross over to the other side of the map.
- a solid 100fps server simulation (in Go) serving clients with a really bandwidth efficient netcode (it's binary websocket instead of plain JSON and I open-sourced it: https://github.com/Tom32i/netcode).
- Instant reconnection, at any time: I had this requirement from day one, in the first curvytron losing connexion meant dropping out of the game permanently. Not anymore. You can just refresh the page mid-game and keep playing, try it yourself.The game runs in any desktop and mobile browser and supports gamepads
I've put up servers in US and Europe to offer a good ping to as much players as I can afford at the moment.I still maintain and host the first game to keep the original experience live.I'd love to get feedback from HN, and don't hesitate to stress-test the game of course!I'll be around to answer questions and discuss if you're interested.
Cheers!

## 评论（5/5）

> **tedavis** · 2026-07-01T08:32:20.000Z　
> This is excellent! What was the biggest challenge you found while developing the sequel?

---

> **andai** · 2026-07-02T00:42:40.000Z　
> Nice! The game is fun.How did you handle the reconnection?

---

> **ashxel** · 2026-07-02T14:31:30.000Z　
> Wow, didn't expect to see this. Maybe something is in the air - I've been working on a similar project [0] out of a nostalgia for the "Curve Fever 2" era. I'm actually familiar with your first game, and this one is very fun and polished too, particularly the effects and the UI. Mine is a bit raw at the moment but quite functional. You get dropped in to a shared room of classic "survival," but I've also spent a lot of time making wonkier mode like CTF, zone control, etc. It's a bit of Achtung die Kurve meets Halo 3.But - we are both very aligned on the "no ads/tracking/monetization" aspect, which I appreciate. best of luck to a fellow curvelike developer.[0] https://recurvegame.com/

---

> **tom32i** · 2026-07-01T11:09:44.000Z　
> It was clearly dynamic "trail" geometry:in curvytron your trail grows behind you as you go, so on each frame most of active players trail "capsule" 3D geometries have changed.I started by blindly recalculate every geometry on every frame, work well enough for a time but I think you can see the optimisation problem coming...On each frame the trail gets only 1 new point and the rest of its points (dozens) has not changed, yet you recalculate every segment vertices (and normals, etc) for every point, just to add one new segment at the end and finally add the half-sphere cap.
> And this is done by Three.js: so by the CPU, not in GPU yet.What I did was write a dynamic capsule geometry, with pre-allocated geometry buffer and the capacity to add 1 point at each frame by just filling the missing vertices, normals, etc fo the point. Resulting in a massing performance improvement.Side note: when the player stop "drawing" and leave a hole behind, the detached trail become inactive and just stop being re-computed at each frame.

---

> **tom32i** · 2026-07-02T05:53:28.000Z　
> Thanks!Reconnection relies on two mechanisms:Server side — Secured client identification:
> When you connect to the game, the server forges and sends you a unique secure token. If you lose connection, your client and player data on the server aren't removed but just "parked" into an offline list of clients. Your player is left without a pilot for a moment. As soon as you reconnect with a valid token, the server is able to restore your client and plug you back into your player's controls. You're back in the game!Client side — Ubiquitous game data:
> For reconnection to work on the player's end, I also need every client arriving in the middle of a game to get the exact same state as a client that connected from the start. This means sending every connecting client all the meaningful data about the current game: state, player positions, speed, size, ongoing bonus positions and timings, etc. I designed the game with this requirement from the very start: each new feature must follow this pattern, and the client must support building the game's world on the fly from this data.

## 关联链接

- https://curvytron2.com
- https://github.com/Tom32i/netcode
- https://news.ycombinator.com/item?id=9494619

## 导航

- 项目页：[[10-项目/curvytron2.com_15d16734]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
