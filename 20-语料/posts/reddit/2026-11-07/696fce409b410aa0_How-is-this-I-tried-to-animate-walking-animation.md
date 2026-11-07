---
type: "corpus"
item_id: "696fce409b410aa0"
title: "How is this? I tried to animate walking animation?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1xh9mhf/how_is_this_i_tried_to_animate_walking_animation/"
author: "Mr_nonimus"
published_at: "2026-10-28T08:24:25+08:00"
captured_at: "2026-11-07T09:44:43+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-11-07"
pub_day: "2026-10-28"
tags:
  - 语料
  - reddit
  - r/indiedev
  - GIF
metrics: {"score": 3, "comments": 9, "upvote_ratio": 0.7142857142857143}
comments_count: 9
comments_total: 9
discovered_via: "reddit:14d+settle10"
---

# How is this? I tried to animate walking animation?

> [!info] 一句话导读
> I'm now really that good at pixel art but its still the art I'm better at compared to the rest. Please feel free to suggest improvements :D

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1xh9mhf/how_is_this_i_tried_to_animate_walking_animation/>
> 指标：得分=3 · 评论=9 · 赞踩比=0.7142857142857143
> 作者：Mr_nonimus　|　发布：2026-10-28T08:24:25+08:00
> 项目链接：—
> 采集：2026-11-07T09:44:43+08:00　|　id：`696fce409b410aa0`

## 正文

I'm now really that good at pixel art but its still the art I'm better at compared to the rest. Please feel free to suggest improvements :D

## 评论（9/9）

> **43R42**（3 分） · 2026-10-28T09:04:56+08:00　
> By the way, it's very cool, it's a pity for the hands without changes

---

> **Mr_nonimus**（2 分） · 2026-10-28T09:10:35+08:00　
> I didn't animate hands yet cause I was thinking making a separate sprite for it, cause I'll have controls like picking up and things in my game so hands would need to be separate objects :D

---

> **buildingTamagofit**（2 分） · 2026-10-28T10:29:37+08:00　
> Nice start, the legs read well! Agree on the arms: swing them opposite to the legs (left arm forward with the right leg) and the whole thing comes alive. Then add a 1-pixel body bob, lowest at the contact pose and highest when the feet pass each other. If you want extra character, delay the head by a frame so it follows the body instead of moving rigidly with it.

---

> **Mr_nonimus**（1 分） · 2026-10-28T14:43:32+08:00　
> Got it about the head, but what is body bob?

---

> **unevensea**（2 分） · 2026-10-28T15:44:57+08:00　
> I like it's so far!
>
> I like the sway of the legs , when you work on the arms you might consider emulating that same sway motion in opposite directions to maintain the bounciness of the sprite and possible add a slight hip movement if possible.

---

> **ShortDude55**（2 分） · 2026-10-28T22:42:13+08:00　
> Very impressive! You nailed the poses.
>
> The thing I'm noticing is that the left leg appears in front of the right one, but looks like it should be behind at this angle, since the character is walking to the right.

---

> **Mr_nonimus**（2 分） · 2026-10-28T23:37:17+08:00　
> I noticed that too 😅. Fixed it, doing some more improvements will most the improved one in a few minutes.

---

> **Mr_nonimus**（1 分） · 2026-10-28T23:57:01+08:00　
> Guys! I posted a follow up post including all your improvements! Please check it out and suggest more improvement ideas if you have any :D

---

> **buildingTamagofit**（2 分） · 2026-10-29T11:16:31+08:00　
> Body bob is the whole body (head and torso) moving up and down a little as the character walks. When both feet are on the ground at the widest step (contact pose), the body is at its lowest. When one leg passes under the body (passing pose), the body is at its highest. So in your cycle you'd shift the torso and head down 1 pixel on the contact frames and back up on the passing frames, and leave the feet where they are.
>
> Without it the upper body slides along like it's on a rail. With it, the walk suddenly has weight.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
