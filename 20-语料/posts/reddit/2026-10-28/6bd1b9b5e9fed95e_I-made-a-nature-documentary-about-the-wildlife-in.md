---
type: "corpus"
item_id: "6bd1b9b5e9fed95e"
title: "I made a nature documentary about the wildlife in League of Legends. Here's the first minute."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1x8pv3n/i_made_a_nature_documentary_about_the_wildlife_in/"
project_url: "https://v.redd.it/9flbu557h4wh1"
author: "JuandisimoDeluxe"
published_at: "2026-10-18T08:44:06+08:00"
captured_at: "2026-10-28T09:40:48+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-10-28"
pub_day: "2026-10-18"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 4, "upvote_ratio": 1}
comments_count: 2
comments_total: 4
discovered_via: "reddit:14d+settle10"
---

# I made a nature documentary about the wildlife in League of Legends. Here's the first minute.

> [!info] 一句话导读
> Episode 1 is about Teemo, but it opens with a tour of the map's wildlife before the players show up and ruin it. I write it like a real nature doc, and the narr…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1x8pv3n/i_made_a_nature_documentary_about_the_wildlife_in/>
> 指标：得分=3 · 评论=4 · 赞踩比=1
> 作者：JuandisimoDeluxe　|　发布：2026-10-18T08:44:06+08:00
> 项目链接：<https://v.redd.it/9flbu557h4wh1>
> 采集：2026-10-28T09:40:48+08:00　|　id：`6bd1b9b5e9fed95e`

## 正文

Episode 1 is about Teemo, but it opens with a tour of the map's wildlife before the players show up and ruin it. I write it like a real nature doc, and the narrator keeps a straight face the whole time.

I pulled the map, the champions, the monsters and their animations out of the game's files and rebuilt them in three.js, so I can put the camera anywhere. A script renders every frame in a headless browser and pipes it into ffmpeg.

One episode out so far. The two bugs that cost me the most time were the river reeds glowing white (wrong color space) and the whole map coming out mirrored.

If you've never played League, does it still land? That's the part I can't judge.

Full episode (8 min): https://youtu.be/Bp5MTn4-rco

## 评论（2/4）

> **Fit-Corner2382**（1 分） · 2026-10-18T08:57:20+08:00　
> Treating champion kits like animal behavior is the part that actually sells the documentary.
>
> I keep wondering how much of the minute is in-engine capture versus graded plates, because the pacing feels tighter than raw spectator cam usually allows.

---

> **JuandisimoDeluxe**（1 分） · 2026-10-18T09:33:14+08:00　
> none of it is capture actually, there’s no game running at all. i pulled the map, models and animations out of the game files and rebuilt the scene in three.js, so every shot is a camera move i placed by hand and timed to the narration line. that’s why it’s tighter than spectator cam: the cuts are written to the jokes, not found in footage
>
> the grade’s in the renderer too. a sun with soft shadows, a rim light, bloom, a split-tone grade, and the god rays are riot’s own particle textures. then it renders frame by frame straight to video
>
> and yeah the kits-as-behavior thing is the whole bit, glad it reads

## 关联链接

- https://youtu.be/Bp5MTn4-rco

## 导航

- 项目页：[[10-项目/v.redd.it_ae6310bb]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
