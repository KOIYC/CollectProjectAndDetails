---
type: "corpus"
item_id: "fc8c73609327e27b"
title: "Show HN: Learn to beatmatch on Winamp-skinned decks (vibe-coded, desktop only)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50325252"
project_url: "https://bit-cheer.com/"
author: "fi3"
published_at: "2026-11-01T13:02:20Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_fi3
  - story_50325252
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Learn to beatmatch on Winamp-skinned decks (vibe-coded, desktop only)

> [!info] 一句话导读
> IntroGiven all the token resets in the last few weeks, I decided to try building a fully vibe, and

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50325252>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：fi3　|　发布：2026-11-01T13:02:20Z
> 项目链接：<https://bit-cheer.com/>
> 采集：2026-11-02T09:37:22+08:00　|　id：`fc8c73609327e27b`

## 正文

## IntroGiven all the token resets in the last few weeks, I decided to try building a fully vibe, and
fully one-shotted project (one prompt per feature/bug fix, no reviews, neither human nor indipendent
agents, only the ones the agent itself spawns).That's how bit-cheer https://bit-cheer.com was born, a tool for learning beatmatching that I really
wish I had when I started with turntables.
The idea is absolutely not new, and if you want to learn beatmatching and want something much more
tested and still free, I recommend https://www.beatmatch.pro/.I needed a somewhat challenging task to see how far I could get with this 100% vibe, one-shotted
approach, and I liked the somewhat nostalgic idea of using early 2000s graphics, so bit-cheer reuses
Winamp's graphics and elements and can "wear" any Winamp skin.## No mobileThe app was intentionally designed not to support mobile. I didn't feel like going crazy trying to
make Winamp skins work on mobile, and it most likely never will support it.## Technical detailsThe web app is written in Elm (with a bit of js, mainly for plumbing and skin rendering) and uses an
audio engine written in Rust and compiled to WASM. That's all I know. (I had to ask the agent what
it uses npm and js for, and it used for what I was more or less expecting)What I didn't expect is that, for some reason, it decided not to use elm-test, so the score matcher,
which according to the agent needs unit tests, is written entirely in JS. Two other unexpected
things are (1) the Comfort/HD feature, which does pixel enhancement and is pretty CPU-heavy, is in
js even though Rust/WASM was an option, and (2) the Vite and Elm dependencies are not up to date.These are the only three issues that came out of a very quick review (literally a handful of
questions to the agent). Everything else was done purely as a "user", meaning using the app and
giving my feedback to the agent.Most of the skin rendering was done by Claude with Opus 5.5 Max, while most of the audio engine was
done by Astra 6 Ultra. The FE is 50/50.I find that what I got is a very good result, considering that I give the agent only few high level
instructions and then only used the app and reported bug and asked for features.## The webappThe webapp offers 5 modes:* Foundation: you need to match 2 different kicks, and you can see the BPM of each track.* Loop builder: you need to match 2 complete loops (many instruments, not just a kick), and you
 can see the BPM (you can build your own loops as well).* By ear: same as loop builder, but BPMs are hidden.* Star mode: same as by ear, but BPMs are not constant and you need to keep the tracks aligned.* Pro decks: you can play actual music, 40 CC tracks or tracks you load from your PC. You can
 enable star mode here as well to keep things more interesting.In any mode, you have a coach that will rate your run.It also offer an 8 lesson learning path an hardwar mixed support (still not tested) and, of course,
the skin studio.## Links* bit-cheer: https://bit-cheer.com/* youtube: https://www.youtube.com/watch?v=SLSok7xQwCY* github: https://github.com/Fi3/bit-cheer/* twit: https://x.com/dev_sv2/status/2116874582044881332

## 关联链接

- https://bit-cheer.com
- https://bit-cheer.com/*
- https://github.com/Fi3/bit-cheer/*
- https://www.beatmatch.pro/.I
- https://www.youtube.com/watch?v=SLSok7xQwCY*
- https://x.com/dev_sv2/status/2116874582044881332

## 导航

- 项目页：[[10-项目/bit-cheer.com_eb89c7de]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
