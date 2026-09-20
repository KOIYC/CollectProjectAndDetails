---
type: "corpus"
item_id: "b35906d02c027fc5"
title: "Show HN: Automated Sanborn map georeferencing, with a Chicago map viewer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49502236"
project_url: "https://autogeoref.com/"
author: "chicagopluto"
published_at: "2026-08-30T20:02:40Z"
captured_at: "2026-09-21T03:11:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_chicagopluto
  - story_49502236
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:52d"
---

# Show HN: Automated Sanborn map georeferencing, with a Chicago map viewer

> [!info] 一句话导读
> Drag the round handle to swipe · click a district below to fly there

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49502236>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：chicagopluto　|　发布：2026-08-30T20:02:40Z
> 项目链接：<https://autogeoref.com/>
> 采集：2026-09-21T03:11:28+08:00　|　id：`b35906d02c027fc5`

## 正文

loading…
☰
–
Atlas opacity 100%
Drag the round handle to swipe · click a district below to fly there
Go
Copy a link to this view
Districts on file · 0
‹ Back
 Next ›
 Leave the story
How this map was made
 Source on GitHub ↗
Sources

## 评论（1/1）

> **chicagopluto** · 2026-08-30T20:03:24.000Z　
> Repo is here (https://github.com/matt-hendrick/autogeoref). This markdown writeup (https://github.com/matt-hendrick/autogeoref/blob/main/WHY.md) has a longer explainer of why I made this + some reflections on developing it with coding agents. Additional context on this project is below.---Sanborn fire insurance maps are used by researchers to see how cities and places have changed over time. While some have been digitized as PDFs, only a subset of those have been georeferenced to a specific location. That lack of georeferencing makes the process of using Sanborn maps cumbersome and slow, and it impedes researchers who use georeferenced Sanborn maps as inputs. This tooling aims to help with that.How it works: a multi-modal model processes an image of a Sanborn map sheet and extracts street names, rail line names, and house numbers as JSON. That JSON is fed to a deterministic pipeline, which attempts to match it to the correct streets or rail lines in the current city and then performs many layers of validation.As far as I am aware, the best performing automated approach to this prior to now placed 14% of sheets, using an object detection model (https://www.tandfonline.com/doi/full/10.1080/15420353.2025.2...). This approach places more than 70%, and those placements generally score well against manual human placements: median difference of 5.5 m, with only 11% more than 15 m different. The output generally looks decent on a map.- ~75% of sheets across the 77 Chicago volumes I have run- Placement rate varies a lot by volume, from 2% to 97% (2% for a volume of grain elevators in Chicago)- 64% on a Cleveland volume, run with Chicago-tuned settingsIt is not perfect. Some sheets are slightly misaligned, some boundaries between sheets are jagged, and sometimes sheets are placed incorrectly. It (unsurprisingly) struggles where the city grid has changed significantly since the map was drawn (highways destroying neighborhoods, water being filled in, streets removed) and on sheets that are mostly parks or water. It works best on clean grids.Ideally as open source models improve, this will be possible to run locally. I tried Qwen 3.5, Gemma 4, Minicpm-v4.5 but those did not perform well on this task. It currently supports the OpenAI/Anthropic APIs or shelling out to Claude Code/Codex/OpenCode. I was able to process the available, digitized Chicago volumes within a month using a Claude Code ($200) and OpenAI ($100) subscription.A small town is cheap to run. `https://github.com/matt-hendrick/autogeoref/tree/main/config...` is a single 14-sheet 1948 volume for Staunton, IL. For that small town, the pipeline placed 11 of 12 sheets with 19 model calls.Adam Cox's OldInsuranceMaps.net is where the human placements I score against come from and his site is the best way for people to contribute to the community. I view autogeoref as a possible assistive tool for researchers who want a way to speed up their georeferencing.

## 导航

- 项目页：[[10-项目/autogeoref.com_0de106dd]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
