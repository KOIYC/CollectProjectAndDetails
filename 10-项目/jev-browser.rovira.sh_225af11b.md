---
type: "project"
title: "Show HN: Jev drives a browser – HN login and search in 8s for half a cent"
project_url: "https://jev-browser.rovira.sh/"
first_seen: "2026-10-22T09:46:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_zurfyx
  - story_50181149
  - show_hn
lang: "en"
---

# Show HN: Jev drives a browser – HN login and search in 8s for half a cent

> [!info] 一句话导读
> I put this repo and site together as an educational reference for folks getting started with Jev / OpenAI Decisions API.This demonstrates how Jev can drive a br…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://jev-browser.rovira.sh/>
> 首次收录：2026-10-22T09:46:18+08:00
> 来源渠道：HN Show HN
> 标签：author_zurfyx, story_50181149, show_hn
> 最新指标：点赞=4 · 评论=0 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:46:18+08:00 | HN Show HN | 点赞=4 · 评论=0 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-10-22/420b5df095dd657b_Show-HN-Jev-drives-a-browser-–-HN-login-and-search]] |

## 摘要正文

I put this repo and site together as an educational reference for folks getting started with Jev / OpenAI Decisions API.This demonstrates how Jev can drive a browser (the idea being extract it into a skills file). On every step the page's controls are extracted into a table, and Jev picks an operation and a target, with a probability for every option.Try the HN login replay (https://jev-browser.rovira.sh/#hackernews-login), Amazon (https://jev-browser.rovira.sh/#amazon-cart), or run it live with your own key.Interesting bits: - Jev mean response time is 250ms (123–495 ms on the HN run). - Jev never sees the DOM, only a table of controls extracted from it ahead of time. It's in some ways, similar to the accessibility tree that good LLM browser skills use now. - Jev can't generate text (in a good way) so this need to be provided ahead of time, either by you or a complementary LLM. - Each step is stateless and costs a few thousand input tokens, under a tenth of a cent.Repo (three files, no dependencies): https://github.com/zurfyx/jev-browser-skill
