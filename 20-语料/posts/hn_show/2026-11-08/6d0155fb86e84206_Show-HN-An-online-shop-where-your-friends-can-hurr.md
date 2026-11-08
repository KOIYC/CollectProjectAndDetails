---
type: "corpus"
item_id: "6d0155fb86e84206"
title: "Show HN: An online shop where your friends can hurry the courier"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50403954"
project_url: "https://dopaminechic.com/"
author: "AmsterErdo"
published_at: "2026-11-07T12:25:04Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_AmsterErdo
  - story_50403954
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: An online shop where your friends can hurry the courier

> [!info] 一句话导读
> I built an emulator of a flash-sale fashion outlet with no registration and fake checkout that never takes money. You can browse items that are on sale, watch i…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50403954>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：AmsterErdo　|　发布：2026-11-07T12:25:04Z
> 项目链接：<https://dopaminechic.com/>
> 采集：2026-11-08T12:50:31+08:00　|　id：`6d0155fb86e84206`

## 正文

I built an emulator of a flash-sale fashion outlet with no registration and fake checkout that never takes money. You can browse items that are on sale, watch in real time as they go out of stock one by one, and get notified when they are back on sale (possibly with different prices).Every order placed on the website gets “tracking” which fails on the delivery day with one of 50 available reasons (for example, “a raccoon in the Newark depot has claimed your parcel; animal control reports that it seems happy there”). But you can also share the tracking with your friends, and they can hurry the courier; the more hurries, the more spectacularly it fails, until your parcel lands in the Svalbard seed vault, the North Pole, the International Space Station or some such place.The complete shop contents (campaigns, prices, item availability and stock levels) are computed from the current time with a fixed seed (FNV-1a for hashing, mulberry32 as the PRNG). I wrote the mechanism first in JS and then ported to PHP (for the website) and Flutter (for the mobile app); a test ran over several thousand random time points to verify they are identical. The Flutter app uses its own generator because it can work offline - no contact with the website is necessary.Item images are generated with OpenAI API, except models in swimsuits. OpenAI refused a lot of swimsuit image prompts, so I had to switch to Gemini for these as Gemini has no qualms about this kind of content.Does this kind of site feel like shopping to you? Or more like a game or something to do together with friends?

## 评论（2/2）

> **mohitgupta_in** · 2026-11-07T12:54:20.000Z　
> Basically it felt like shopping to me but can be done while sitting with friends together! it's actually a dopamine booster

---

> **AmsterErdo** · 2026-11-07T13:35:16.000Z　
> Thank you for your feedback! Do you think it could replace real shopping as a dopamine booster?

## 导航

- 项目页：[[10-项目/dopaminechic.com_a4a09c1d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
