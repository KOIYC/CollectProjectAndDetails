---
type: "corpus"
item_id: "420b5df095dd657b"
title: "Show HN: Jev drives a browser – HN login and search in 8s for half a cent"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50181149"
project_url: "https://jev-browser.rovira.sh/"
author: "zurfyx"
published_at: "2026-10-21T14:01:57Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_zurfyx
  - story_50181149
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jev drives a browser – HN login and search in 8s for half a cent

> [!info] 一句话导读
> I put this repo and site together as an educational reference for folks getting started with Jev / OpenAI Decisions API.This demonstrates how Jev can drive a br…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50181149>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：zurfyx　|　发布：2026-10-21T14:01:57Z
> 项目链接：<https://jev-browser.rovira.sh/>
> 采集：2026-10-22T09:46:18+08:00　|　id：`420b5df095dd657b`

## 正文

I put this repo and site together as an educational reference for folks getting started with Jev / OpenAI Decisions API.This demonstrates how Jev can drive a browser (the idea being extract it into a skills file). On every step the page's controls are extracted into a table, and Jev picks an operation and a target, with a probability for every option.Try the HN login replay (https://jev-browser.rovira.sh/#hackernews-login), Amazon (https://jev-browser.rovira.sh/#amazon-cart), or run it live with your own key.Interesting bits:
- Jev mean response time is 250ms (123–495 ms on the HN run).
- Jev never sees the DOM, only a table of controls extracted from it ahead of time. It's in some ways, similar to the accessibility tree that good LLM browser skills use now.
- Jev can't generate text (in a good way) so this need to be provided ahead of time, either by you or a complementary LLM.
- Each step is stateless and costs a few thousand input tokens, under a tenth of a cent.Repo (three files, no dependencies): https://github.com/zurfyx/jev-browser-skill

## 关联链接

- https://github.com/zurfyx/jev-browser-skill
- https://jev-browser.rovira.sh/#amazon-cart
- https://jev-browser.rovira.sh/#hackernews-login

## 导航

- 项目页：[[10-项目/jev-browser.rovira.sh_225af11b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
