---
type: "corpus"
item_id: "aa28e1db960de83d"
title: "Steam Game Finder: Filter by User Ratings, Review Count, and Include/Exclude Tags"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1xflhmt/steam_game_finder_filter_by_user_ratings_review/"
project_url: "https://playframe-roan.vercel.app/"
author: "Key_Rhubarb7973"
published_at: "2026-10-26T10:55:11+08:00"
captured_at: "2026-11-05T11:22:32+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-05"
pub_day: "2026-10-26"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 2, "upvote_ratio": 1}
comments_count: 2
comments_total: 2
discovered_via: "reddit:14d+settle10"
---

# Steam Game Finder: Filter by User Ratings, Review Count, and Include/Exclude Tags

> [!info] 一句话导读
> Steam Game Finder: Filter by User Ratings, Review Count, and Tags

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1xflhmt/steam_game_finder_filter_by_user_ratings_review/>
> 指标：得分=3 · 评论=2 · 赞踩比=1
> 作者：Key_Rhubarb7973　|　发布：2026-10-26T10:55:11+08:00
> 项目链接：<https://playframe-roan.vercel.app/>
> 采集：2026-11-05T11:22:32+08:00　|　id：`aa28e1db960de83d`

## 正文

# Steam Game Finder: Filter by User Ratings, Review Count, and Tags

Hey everyone!

A friend and I recently built a Steam game finder called **Playframe**, and we'd love to get some feedback!

It started as a small hobby project to solve a problem we kept running into while browsing Steam: finding games that match very specific preferences.

For example, let's say I want an RPG with Turn-Based Combat, an Overwhelmingly Positive rating, at least 1,000 reviews, but no Roguelike elements.

Sounds simple enough, right?

Steam does let you include and exclude tags, but things get tricky when you want to combine those filters with specific review ratings and review counts.

So we thought, why not just build something that lets us search for games exactly the way we want?

After some tinkering, we ended up with our first prototype: **Playframe**.

**Here's what it currently supports:**

* **Filter by Steam review ratings:** Select one or multiple rating categories, such as Overwhelmingly Positive, Very Positive, Mixed, etc., along with a minimum number of reviews.
* **Filter by genres, features, themes, Steam tags, and content descriptors:** Both Include and Exclude are supported. Included filters use AND logic, meaning games must match every selected condition. Excluded tags and categories are filtered out.
* **Even the more... cultured Steam tags:** Yes, we included the spicy/NSFW ones too. I won't pretend they weren't part of our original motivation. 😏
* **Sort results:** By best rated, worst rated, most reviewed, or newest releases.
* **Grid and list views:** Browse games with descriptions and screenshots. Clicking a game takes you directly to its official Steam store page.
* **Mobile-friendly:** Works on phones too, and you can share links that preserve your selected filters.

Our database currently contains around **128,238 games and 429 Steam tags**.

**For anyone curious about the data:**

* Game data comes from Steam Store Search and Steam's app data, accessed through steamcmd.net.
* Review counts come from SteamSpy.
* Ratings are calculated using SteamDB's published formula.

Since this is just a hobby project between two friends, we're keeping costs as low as possible and currently hosting everything on Vercel's free tier.

It's still an early prototype, so the database might not be completely up to date, and there are probably bugs we haven't discovered yet.

**Here's the link:** [https://playframe-roan.vercel.app/](https://playframe-roan.vercel.app/)

We originally built Playframe just to make our own game hunting easier, but figured other people might find it useful too.

If anyone has a few minutes to give it a try, we'd genuinely appreciate some feedback:

* Are the filters intuitive? Is there anything you'd like us to add or improve?
* Have you run into any bugs or unexpected search results?

Positive or negative, any feedback would help us improve the project.

We're also curious how everyone else discovers games on Steam. Do you run into similar frustrations with its search filters, or do you have a better way of finding games that match your tastes?

Thanks for reading! Hopefully, Playframe helps you discover a few hidden gems that Steam has been keeping from you. 😄

*Disclaimer: Playframe is an independent project and is not affiliated with Valve or Steam.*

## 评论（2/2）

> **Spiritual-Yak-9689**（2 分） · 2026-10-26T11:04:50+08:00　
> this is actually pretty useful, steam search is a mess when you want to narrow things down properly

---

> **stealthagents**（1 分） · 2026-10-30T05:20:31+08:00　
> Totally agree, Steam's search can be a wild ride. Finding exactly what you want feels like a treasure hunt sometimes. Playframe sounds like a game changer for anyone who’s tired of scrolling through endless titles just to find that perfect match.

## 导航

- 项目页：[[10-项目/playframe-roan.vercel.app_3d4fb9fd]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
