---
type: "corpus"
item_id: "6fc1d9c064d6c003"
title: "Show HN: A little physical breakout clone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49123821"
project_url: "https://brontosaurusrex.github.io/physical/v7"
author: "brontosaurusrex"
published_at: "2026-07-31T14:43:13Z"
captured_at: "2026-09-21T02:55:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_brontosaurusrex
  - story_49123821
  - show_hn
metrics: {"points": 19, "comments": 15, "engagement_velocity": 19}
comments_count: 15
comments_total: 15
discovered_via: "hn:show_hn:83d"
---

# Show HN: A little physical breakout clone

> [!info] 一句话导读
> Idea: How about a 5 minute game I can play in my browser and it's actually fun to play.Controls: Mouse or keyboard (left/right, left alt/right alt or A/D), spac…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49123821>
> 指标：点赞=19 · 评论=15 · engagement_velocity=19
> 作者：brontosaurusrex　|　发布：2026-07-31T14:43:13Z
> 项目链接：<https://brontosaurusrex.github.io/physical/v7>
> 采集：2026-09-21T02:55:02+08:00　|　id：`6fc1d9c064d6c003`

## 正文

Idea: How about a 5 minute game I can play in my browser and it's actually fun to play.Controls: Mouse or keyboard (left/right, left alt/right alt or A/D), space and esc are pause toggle. Page up / Page Down are next or previous level (if already unlocked).Cheats: Z toggles zapper, M toggles magnets.Debug stuff: I, P, E keys are toggles for various stuff (E lets you change some aspects of physics engine).Game is maybe playable on mobile devices, there is a menu on top right, and then click the circle to select type of control.Physical engine is decoupled from refresh rate and runs at 240 Hz.Fully vibe coded (deepseek, chatgpt), levels are human made with some amount of love.

## 评论（15/15）

> **pixel_popping** · 2026-07-31T18:50:50.000Z　
> Website not loading (stuck on plausible.io) fyi.

---

> **tanseydavid** · 2026-07-31T23:40:32.000Z　
> I really like the many variations from the original that you have added (the physics like spin and anti-gravity).These surprises made it far-more-interesting to play than I expected.

---

> **brontosaurusrex** · 2026-08-04T12:58:41.000Z　
> The new beta brings some ornamental debris and slightly worse fps:
> https://brontosaurusrex.github.io/physical/v8beta/(f to show fps, shift+f to reset lowest fps)

---

> **dgerken** · 2026-08-05T01:13:56.000Z　
> Kinda fun

---

> **thenthenthen** · 2026-08-05T01:53:39.000Z　
> Its a bit hard to play on ios, the controls only work in the playable area, so your finger blocks the action. On iOS there is a ‘bar’ at the bottom of the screen when in landscape mode, interfering (visually) with the paddle/parallel

---

> **robovs** · 2026-08-05T06:32:28.000Z　
> This is oddly satisfying! What's are the triggers for the different types of physics?

---

> **chromadon** · 2026-08-05T07:36:34.000Z　
> I selected tilt controls and it doesn’t respond to any motion. The “fullscreen” button doesn’t do anything resulting in a tiny game window.It’s a shame because I love breakout!

---

> **alucardo** · 2026-08-05T20:41:32.000Z　
> Nice! played through the 28 levels.About the mouse control: many times i failed because my cursor went outside the viewport and the paddle stopped moving. So i got to keep the mouse inside the game area, which is kinda annoying visually too. Even in fullscreen there are borders where the cursor can fall and die.Another feedback: the ball bounces a bit too vertically on block corners, it seems it could bounce a bit more diagonally.And i found the big-blocks levels a bit difficult because it was hard to send the ball at the top of the screen.Thank you, i had fun :)

---

> **brontosaurusrex** · 2026-08-01T08:08:12.000Z　
> Counter will be disabled in the near future, thanks for feedback.According to the plausible we got staggering 82 hits since yesterday. Roughly 50% desktop and 50% mobile, with average time on page 1 minute and 24 seconds.

---

> **brontosaurusrex** · 2026-08-01T08:07:19.000Z　
> Thanks for feedback.

---

> **brontosaurusrex** · 2026-08-05T07:37:32.000Z　
> There is a triple dot menu at the top, and then click the ball and it should present with 4 different type of mobile controllers (one being tilt for example). p.s. I haven't tested the game on mobile devices much, I haven't tested iOS at all.

---

> **brontosaurusrex** · 2026-08-05T07:28:45.000Z　
> There is 3 types of bricks (common, magical and unbreakable), the ones with 'magical' powers will trigger different 'power-ups'.

---

> **brontosaurusrex** · 2026-08-05T08:39:50.000Z　
> Thanks for feedback, it appears I need DeviceOrientationEvent.requestPermission() call before the game can tilt (Maybe in next version), and I can't force a true programmatic fullscreen mode using standard JavaScript code on iOS 13 and newer.

---

> **brontosaurusrex** · 2026-08-06T06:38:08.000Z　
> Thanks for feedback. I'll see what I can do with cursor getting out of the play window, would cursor lock be a solution? (click once to lock, click twice to unlock).Yeah the physics, this is ~ 5th internal version already, there were more pronounced corner angles at some point, but it got unplayable.Big block levels; The idea is to encourage the player to find two bounce solutions, where first bounce is spinned and 2nd would be to 'correctly' translate that spin into upward speed.

---

> **thenthenthen** · 2026-08-05T08:16:38.000Z　
> iOS is a pain. Things like sensor data need to be activated in a certain order (like.. before other events etc). The tilt doenst work on iOS (you should get a dialog box that requests access).

## 导航

- 项目页：[[10-项目/brontosaurusrex.github.io_f027a094]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
