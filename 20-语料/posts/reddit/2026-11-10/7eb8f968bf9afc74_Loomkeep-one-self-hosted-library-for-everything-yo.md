---
type: "corpus"
item_id: "7eb8f968bf9afc74"
title: "Loomkeep: one self-hosted library for everything you watch, read, play and listen to"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xjtxmo/loomkeep_one_selfhosted_library_for_everything/"
project_url: "https://docs.loomkeep.app/self-hosting"
author: "loomkeep_dev"
published_at: "2026-10-31T06:52:22+08:00"
captured_at: "2026-11-10T09:52:27+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-10-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (AI)
metrics: {"score": 9, "comments": 13, "upvote_ratio": 0.6216216216216216}
comments_count: 11
comments_total: 13
discovered_via: "reddit:14d+settle10"
---

# Loomkeep: one self-hosted library for everything you watch, read, play and listen to

> [!info] 一句话导读
> https://i.redd.it/42t933vbqoyh1.png

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xjtxmo/loomkeep_one_selfhosted_library_for_everything/>
> 指标：得分=9 · 评论=13 · 赞踩比=0.6216216216216216
> 作者：loomkeep_dev　|　发布：2026-10-31T06:52:22+08:00
> 项目链接：<https://docs.loomkeep.app/self-hosting>
> 采集：2026-11-10T09:52:27+08:00　|　id：`7eb8f968bf9afc74`

## 正文

https://i.redd.it/42t933vbqoyh1.png

My series and movies lived in TV Time, my books in Goodreads, my games in Infinite Backlog. When TV Time shut down I decided to build a replacement I'd own, and it grew into **Loomkeep**: one library for everything you watch, read, play and listen to, that you can run on your own server.

**What it tracks**

* Series, films and anime (TMDB, AniList)
* Games (IGDB), books (Open Library), music in beta (MusicBrainz)
* Board games and podcasts are next on the roadmap

**Why you might like it**

* Every episode, rewatch, play session and reread is dated: your history is real, your stats are honest
* Bring your past: imports from TV Time, Trakt, Simkl, Letterboxd, IMDb, MyAnimeList, AniList, Steam, Goodreads, StoryGraph and Babelio
* Read-only public API with personal keys, iCal calendar and feed links
* Social features, achievements and sign-ups are switches you control
* Installable on your phone (PWA, plus an Android app)

**Self-hosting**

* Two Docker images (api + web) and Postgres: `docker compose up -d`
* Free TMDB and IGDB API keys for the catalogs
* Guide for HTTPS, backups, upgrades and optional services (monitoring, error tracking, SSO): [https://docs.loomkeep.app/self-hosting/](https://docs.loomkeep.app/self-hosting/)

**How it's built**

I build it with AI assistance (Claude Code). I review and own every change, and the repo runs CI, tests and security scans (CodeQL, Trivy, ZAP) in the open.

It's AGPL-3.0, made by one person, no ads, no tracking. If you'd rather try before installing, there's a free instance at [https://loomkeep.app](https://loomkeep.app/).

**Code:** [**https://github.com/Logan2234/loomkeep**](https://github.com/Logan2234/loomkeep)

Loomkeep is still a young project, built and maintained by me alone in my spare time. I'm actively working on it, fixing issues, improving existing features and deciding what to build next based on actual user feedback. I'm not looking for people to simply give it a star: I'd genuinely love to hear what's confusing, what's missing, what doesn't work, or what would make you want to use it regularly.

## 评论（11/13）

> **asimovs-auditor**（1 分） · 2026-10-31T06:52:34+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **loomkeep_dev**（-3 分） · 2026-10-31T07:05:32+08:00　
> AI was used for the project: I'm a software engineer and I build Loomkeep with AI coding agents (Claude Code), which writes a large part of the code, tests and docs, and also helped with the visual design.
>
> What comes from me: the idea (I wanted a TV Time replacement I'd own, covering all my media), the product decisions and roadmap, the architecture, and which features ship and how they should behave. I review the changes, do the manual testing myself, and run and maintain the production instance at loomkeep.app.
>
> Every change goes through CI: tests, CodeQL, Trivy and ZAP. Commits made with an agent are marked as co-authored in the Git history, so you can check it yourself.

---

> **archdukemovies**（5 分） · 2026-10-31T09:28:43+08:00　
> This might be good to use as a backup for when letterboxd gets sold

---

> **AliyasDandani_64**（0 分） · 2026-10-31T09:35:25+08:00　
> Nice scope. one thing id think about early is how you want to handle the "everything app" perception problem, because people tend to trust specialized trackers more even when the all-in-one is technically better. might be worth leading with whichever media type is strongest right now

---

> **pagem**（2 分） · 2026-10-31T12:01:37+08:00　
> Wondering if this automatically pulls what i have watched, listened to or read from other services I might be using like Jellyfin, Navidrome or Bookorbit?

---

> **psychedelic_tech**（10 分） · 2026-10-31T18:18:35+08:00　
> ai;dr

---

> **PreMedinDread**（0 分） · 2026-10-31T18:23:55+08:00　
> How does this compare to floppy?

---

> **loomkeep_dev**（2 分） · 2026-10-31T18:29:08+08:00　
> Hey! Not yet, but this feature is already present on the roadmap! 😉 Out of curiosity, which one would be your highest priority to connect first?

---

> **loomkeep_dev**（-1 分） · 2026-10-31T18:48:51+08:00　
> Hello and thanks!
>
> You are absolutely right, this is quite a challenge indeed.
>
> I'll be honest: I focused my efforts on the movies / series domain first, as it started as a TV Time replacement.
>
> But as a person who loves to make lists, save, and rate things, I quickly came up with the idea to make it an "all-in-one" app.
>
> This is why I'm focusing a lot on modularity:
> - Whether you use the hosted app or you self-host it, you can activate or deactivate any domain (TV, book, game, music, ...) to declutter unnecessary items.
> - Self-hosters can deactivate all social features if not needed.
> - Same for gamification features (levels, achievements, leaderboards, ...).
> - The dashboard is fully customizable, as I assumed I could never make the perfect dashboard for everyone.
> - And a ton of settings to complement all this customization.

---

> **loomkeep_dev**（-1 分） · 2026-10-31T19:15:01+08:00　
> Honest answer: Floppy has years of history behind it, while Loomkeep is only a few months old, so expect it to be less mature in places. Floppy also covers more media types today. I’m focusing on films, series, anime, books and video games. Music is in beta for now, and podcasts and board games will come one day. Plex and Jellyfin integration is already on the roadmap.
>
> Where I think Loomkeep stands out:
>
> * Official hosted instance at [loomkeep.app](http://loomkeep.app) if you don’t want to run a server, and you can still self-host it (AGPL).
> * Android app that also connects to your own self-hosted instance. (Push notifications only work on the hosted instance for now.)
> * Social features: friends, reviews, shared lists and chat. Optional when you self-host.
> * Gamification: XP, levels and achievements, for those who enjoy that. Optional when you self-host.
>
> I haven’t used Floppy much, so correct me if I’m selling it short.

---

> **pagem**（2 分） · 2026-11-01T14:08:46+08:00　
> For me it would be Jellyfin no question :)

## 关联链接

- https://docs.loomkeep.app/self-hosting/
- https://github.com/Logan2234/loomkeep
- https://github.com/Logan2234/loomkeep**
- https://i.redd.it/42t933vbqoyh1.png
- https://loomkeep.app
- https://loomkeep.app/

## 导航

- 项目页：[[10-项目/docs.loomkeep.app_8157fcd4]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
