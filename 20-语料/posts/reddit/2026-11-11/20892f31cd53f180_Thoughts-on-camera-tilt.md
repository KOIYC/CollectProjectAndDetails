---
type: "corpus"
item_id: "20892f31cd53f180"
title: "Thoughts on camera tilt?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1xkth37/thoughts_on_camera_tilt/"
project_url: "https://v.redd.it/45lwje5obxyh1"
author: "RyanSweeney987"
published_at: "2026-11-01T11:56:13+08:00"
captured_at: "2026-11-11T13:38:49+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-11"
pub_day: "2026-11-01"
tags:
  - 语料
  - reddit
  - r/indiedev
  - Feedback?
metrics: {"score": 4, "comments": 17, "upvote_ratio": 0.8333333333333334}
comments_count: 17
comments_total: 17
discovered_via: "reddit:14d+settle10"
---

# Thoughts on camera tilt?

> [!info] 一句话导读
> Looking for feedback on the camera tilt.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1xkth37/thoughts_on_camera_tilt/>
> 指标：得分=4 · 评论=17 · 赞踩比=0.8333333333333334
> 作者：RyanSweeney987　|　发布：2026-11-01T11:56:13+08:00
> 项目链接：<https://v.redd.it/45lwje5obxyh1>
> 采集：2026-11-11T13:38:49+08:00　|　id：`20892f31cd53f180`

## 正文

Looking for feedback on the camera tilt.

The idea was to give a slight tilt so you can see in the direction you're aiming at better.

The first iteration gave me motion sickness and this is what I currently have but I also got used to it quickly so I'm wondering how people feel from seeing it with the video.

## 评论（17/17）

> **RyanSweeney987**（1 分） · 2026-11-01T11:59:57+08:00　
> Also if anyone wants to keep an eye on the progress of this, I post on X: [https://x.com/sweenus987](https://x.com/sweenus987) and YouTube [https://www.youtube.com/playlist?list=PLUQ2YEWoloPw](https://www.youtube.com/playlist?list=PLUQ2YEWoloPw)

---

> **ChadSexman**（10 分） · 2026-11-01T12:03:16+08:00　
> I don’t see any tactile advantage and find it kind of nauseating.
>
> Adding: I think it might be a neat way to introduce a boss, or point the user towards an objective, but aiming feels like too much.

---

> **HalfCertified_**（6 分） · 2026-11-01T12:04:00+08:00　
> I dislike it

---

> **TrenchWarsDev**（3 分） · 2026-11-01T12:09:09+08:00　
> Since the nausea is your main risk, I'd try a camera offset toward the aim point (a bit of look-ahead) instead of rotating the whole view, because rotation is what usually triggers motion sickness. If you keep some tilt, make it small, smooth it with a spring so it never snaps, and add an off toggle or an intensity slider. Also have a few people who get queasy easily try it, since you've already adapted and can't judge it fresh anymore.

---

> **DayTimeInteractive**（3 分） · 2026-11-01T12:14:13+08:00　
> tilt on its own made me a bit queasy in the clip, but the aim read is better for height. what's the lerp time on it right now, like does it snap back in a few frames when you stop aiming?

---

> **RyanSweeney987**（1 分） · 2026-11-01T12:20:03+08:00　
> It's based on mouse distance and angle from the player, lerp time is 2.5s with up to 10 degrees of angle change.
>
> That said, based on the feedback so far, if I wanted to use it for aiming, it makes sense to keep it as for a specific situation, like a point of interest but for combat I'm wondering if it could work as an "aim down sights" type effect where aim speed is much, much slower and I could add more accurate height based aiming rather than just hitting a 2D circle.
>
> I'm glad I asked how people felt lol

---

> **No-Opinion-5425**（2 分） · 2026-11-01T12:39:40+08:00　
> It’s crazy effective at emulating the motion sickness I get from free walking in VR. I don’t like it at all.

---

> **_curious_george__**（2 分） · 2026-11-01T15:54:34+08:00　
> In its current incarnation, it’s disorienting. I’m not sure you’ll be able to tune that away?
>
> But I wonder if with further refinement this could be some other mechanic? A downside to using a weapon that’s too heavy, or a drunk state etc.

---

> **DayTimeInteractive**（1 分） · 2026-11-01T16:11:35+08:00　
> 2.5s is way slower than I guessed, that explains the drift I felt. as an aim down sights thing, would you cut it to like 4 or 5 degrees so the height read stays but it swings less?

---

> **ExoticRole2355**（2 分） · 2026-11-01T17:29:37+08:00　
> This style reminds me of classic platformers."

---

> **Fretsome**（2 分） · 2026-11-01T17:32:09+08:00　
> I'm not disoriented or nauseated at all and kind of like it. But obviously, if it nauseates others... Don't do it

---

> **aPOPblops**（2 分） · 2026-11-01T18:04:34+08:00　
> Hate it, sorry

---

> **RyanSweeney987**（2 分） · 2026-11-01T22:25:31+08:00　
> I was thinking maybe trying a more aggressive angle but have it so if you're doing "aim down sights", you can't look around or move nearly as fast, not sure.
>
> Part of me is also wondering maybe locking in the tilt so that it can only happen if the player is looking in the same direction as they're moving, or not moving at all or something like that.
>
> I'll experiment with the idea a little bit more but thankfully it's just one line code to comment to disable lol

---

> **DayTimeInteractive**（2 分） · 2026-11-02T03:56:37+08:00　
> locking it to when you're moving the same way you're aiming sounds safer, but doesn't that kill it for strafing shots where the tilt would help most?

---

> **RyanSweeney987**（1 分） · 2026-11-02T06:18:09+08:00　
> I didn't think of that at the time I commented but yeah it would

---

> **Seninut**（1 分） · 2026-11-02T21:03:28+08:00　
> Your player is not on the same z axis as the map. Maybe you should fix that first?

---

> **RyanSweeney987**（1 分） · 2026-11-02T22:07:18+08:00　
> Not sure what you mean by that but the feet of the t-posed pawn are on the floor of the map

## 导航

- 项目页：[[10-项目/v.redd.it_e439ae7d]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
