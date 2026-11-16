---
type: "project"
title: "Show HN: Bad Apple but it's Strava [video]"
project_url: "https://github.com/kevinlinxc/badapple-stravaHappy"
first_seen: "2026-11-16T10:00:05+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_kevinlinxc
  - story_50509386
  - show_hn
lang: "en"
---

# Show HN: Bad Apple but it's Strava [video]

> [!info] 一句话导读
> Hi HN!Here to show off a project that took 18 months, 7KLOC, and more importantly, 194 kilometres of walking! In a nutshell, I wanted to make the famous silhoue…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/kevinlinxc/badapple-stravaHappy>
> 首次收录：2026-11-16T10:00:05+08:00
> 来源渠道：HN Show HN
> 标签：author_kevinlinxc, story_50509386, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:00:05+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-16/923e0c6cdb2ee1e8_Show-HN-Bad-Apple-but-it's-Strava-video]] |

## 摘要正文

Hi HN!Here to show off a project that took 18 months, 7KLOC, and more importantly, 194 kilometres of walking! In a nutshell, I wanted to make the famous silhouette animation “Bad Apple” with Strava, which is an exercise tracking app that visualizes where you walk/run on a map. To use the earth as my canvas, I had to do a lot of coding in the prep work to plan where I would walk for each frame of the animation. As I explain in the video, my problem solving/coding steps were something like this:- split video into frames, determine a good framerate- detect contours with OpenCV for each frame. Since frames are very diverse, I had to start with some heuristics for choosing contours and ultimately make a GUI to manually curate all 438 of them (e.g. some frames had many small contours while others had a few important ones, and the video is constantly inverting colours). Output of this work was an intermediate json list of x,y coordinates representing the path along contours- convert these cartesian coordinates into the Universal Transverse Mercator coordinate system, which represents the earth in a cartesian system (as opposed to GPS which doesn’t lend to adding relative distances in degr…
