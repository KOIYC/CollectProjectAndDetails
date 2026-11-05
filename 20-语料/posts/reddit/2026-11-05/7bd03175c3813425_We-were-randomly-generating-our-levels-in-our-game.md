---
type: "corpus"
item_id: "7bd03175c3813425"
title: "We were randomly generating our levels in our game and it made the game feel flat. So we made a godot level editor plugin to craft the levels!"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1xfimtn/we_were_randomly_generating_our_levels_in_our/"
author: "space_lizard_games"
published_at: "2026-10-26T08:37:00+08:00"
captured_at: "2026-11-05T11:22:58+08:00"
lang: "en"
kind: "post"
topic: "游戏"
shard: "2026-11-05"
pub_day: "2026-10-26"
tags:
  - 语料
  - reddit
  - r/indiedev
  - Postmortem
metrics: {"score": 4, "comments": 9, "upvote_ratio": 1}
comments_count: 9
comments_total: 9
discovered_via: "reddit:14d+settle10"
---

# We were randomly generating our levels in our game and it made the game feel flat. So we made a godot level editor plugin to craft the levels!

> [!info] 一句话导读
> We had a problem with our game, when we started creating our levels we went with the traditional rouge-like route of randomizing almost everything, including th…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1xfimtn/we_were_randomly_generating_our_levels_in_our/>
> 指标：得分=4 · 评论=9 · 赞踩比=1
> 作者：space_lizard_games　|　发布：2026-10-26T08:37:00+08:00
> 项目链接：—
> 采集：2026-11-05T11:22:58+08:00　|　id：`7bd03175c3813425`

## 正文

We had a problem with our game, when we started creating our levels we went with the traditional rouge-like route of randomizing almost everything, including the layout of the floors. I think a big problem for this in our game specifically (and potentially a lot of your games as well) was that it really doesn't NEED random layouts.

the floors having a random layout didn't really add anything to the gameplay and because we were generating these they most of the time just felt really flat and weird. We just kind of did it because in our minds it made sense to just randomly generate the floors so that it was a different "adventure" every time you started a new run.

In practice though it became increasingly more complex to

1) place furniture in a believable and natural way

2) avoid narrow corridors and furniture spawning inconsistently in some rooms vs others

3) getting it to feel like an actual nursing home and not just a randomly generated DOOM style level.

The one thing I wanted to share with you guys that we didn't realize was just how easy it was to get a level editor like this working as just a custom Godot plugin and it really lets us create these handcrafted levels without having to place each item directly in the scene itself unless we actually want/need too.

We made it to where this level editor pops out a level.tscn file that you can also go into directly and place props with the normal precision you would have by just placing them in a scene. Then if you go back to the editor and change the layout or something it keeps all those custom design elements you placed without overriding them.

Because we just took a couple days to make a tool that works for our specific use case I think this will add a lot more depth to our world without completely overloading our 2 person team with handcrafting levels instead of generating them.

Moral of the story making your own Godot plugins is pretty kewl and easier than you think.

Thanks for reading!

## 评论（9/9）

> **letskoya**（2 分） · 2026-10-26T08:48:26+08:00　
> Keeping hand-placed props when you regenerate sounds like the crucial bit. What happens if an edit removes the room a prop was in?

---

> **space_lizard_games**（2 分） · 2026-10-26T09:30:56+08:00　
> The rooms like the lunchrooms are prefab rooms that are their own scenes so if that room is removed all those props are. But currently if you remove the floor where an item is in the main over world area it kind of just floats in the either. That's a good point though it should delete those or  move them to the closest floor tile so we don't have nodes just floating around in the middle of nowhere.

---

> **WWEtrump**（0 分） · 2026-10-26T10:37:06+08:00　
> really respect that you admitted random layouts weren't adding anything, most people never question that default. did hand-built floors change how long your playtesters stuck around?

---

> **space_lizard_games**（2 分） · 2026-10-26T10:50:01+08:00　
> We are in the process of redoing all the levels by hand right now so we will have actual playtester feedback here in like a week or so. Fingers crossed lol

---

> **Chaibi_Alaa**（1 分） · 2026-10-26T17:41:22+08:00　
> We ended up in the same place for a city: real streets rebuilt by hand instead of a generated layout, because the generated blocks all started to feel alike. letskoya's point is the big one for me too. Does your editor let you mark some rooms as shuffleable, so a run can still swap a few of them, or is every floor now fully fixed?

---

> **letskoya**（1 分） · 2026-10-26T20:13:38+08:00　
> I'd lean toward marking those props as unplaced, rather than deleting them automatically. That way a layout change doesn't wipe out the hand-placed work.

---

> **space_lizard_games**（1 分） · 2026-10-26T22:37:48+08:00　
> Every floor is fixed now, but that's a good idea to mark like certain sections of it as still able to be randomized. we will give that a shot!

---

> **WWEtrump**（2 分） · 2026-10-27T08:25:20+08:00　
> hand made levels hit different, good luck with the playtest round! post the feedback when you get it, id love to see what people say

---

> **space_lizard_games**（1 分） · 2026-10-27T08:26:21+08:00　
> Will do!

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`游戏`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
