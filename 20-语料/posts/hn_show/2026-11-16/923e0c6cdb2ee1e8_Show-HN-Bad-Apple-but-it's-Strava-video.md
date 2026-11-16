---
type: "corpus"
item_id: "923e0c6cdb2ee1e8"
title: "Show HN: Bad Apple but it's Strava [video]"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50509386"
project_url: "https://github.com/kevinlinxc/badapple-stravaHappy"
author: "kevinlinxc"
published_at: "2026-11-15T18:32:23Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_kevinlinxc
  - story_50509386
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Bad Apple but it's Strava [video]

> [!info] 一句话导读
> Hi HN!Here to show off a project that took 18 months, 7KLOC, and more importantly, 194 kilometres of walking! In a nutshell, I wanted to make the famous silhoue…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50509386>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：kevinlinxc　|　发布：2026-11-15T18:32:23Z
> 项目链接：<https://github.com/kevinlinxc/badapple-stravaHappy>
> 采集：2026-11-16T10:00:05+08:00　|　id：`923e0c6cdb2ee1e8`

## 正文

Hi HN!Here to show off a project that took 18 months, 7KLOC, and more importantly, 194 kilometres of walking! In a nutshell, I wanted to make the famous silhouette animation “Bad Apple” with Strava, which is an exercise tracking app that visualizes where you walk/run on a map. To use the earth as my canvas, I had to do a lot of coding in the prep work to plan where I would walk for each frame of the animation. As I explain in the video, my problem solving/coding steps were something like this:- split video into frames, determine a good framerate- detect contours with OpenCV for each frame. Since frames are very diverse, I had to start with some heuristics for choosing contours and ultimately make a GUI to manually curate all 438 of them (e.g. some frames had many small contours while others had a few important ones, and the video is constantly inverting colours). Output of this work was an intermediate json list of x,y coordinates representing the path along contours- convert these cartesian coordinates into the Universal Transverse Mercator coordinate system, which represents the earth in a cartesian system (as opposed to GPS which doesn’t lend to adding relative distances in degrees very well)- convert UTM to GPS using a package, then to the GPX file format which is universally accepted- Import GPX files into an app that shows where I am and where I need to walk (I used Gaia GPS). Then I turned on Strava in the background and walked for ~18 months until this was done.I also had to make a bunch of custom software to visualize these walks and make montages of them, like a script to pull polylines from the Strava API, a custom polyline renderer, a script to censor my strava activities a bit, and much more. I’m so proud of this work, it feels like it stands out in a sea of code-only bad apple projects that have become easier to automate with AI, and I hope it can go down as one of the greats in the bad apple colossus of work!Video: https://youtu.be/HxdQawDIlnU
GitHub: https://github.com/kevinlinxc/badapple-stravaHappy to answer any questions!

## 关联链接

- https://youtu.be/HxdQawDIlnU

## 导航

- 项目页：[[10-项目/github.com_057db8c7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
