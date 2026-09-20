---
type: "project"
title: "Show HN: DAC – open-source dashboard as code tool for agents and humans"
project_url: "https://github.com/bruin-data/dac"
first_seen: "2026-09-21T01:41:53+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_karakanb
  - story_47949066
  - show_hn
lang: "en"
---

# Show HN: DAC – open-source dashboard as code tool for agents and humans

> [!info] 一句话导读
> Hi all, this is Burak.When agents became a reality one of the first things I wanted to do was to automate building dashboards. The first, and the most obvious, …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/bruin-data/dac>
> 首次收录：2026-09-21T01:41:53+08:00
> 来源渠道：HN Show HN
> 标签：author_karakanb, story_47949066, show_hn
> 最新指标：点赞=119 · 评论=35 · engagement_velocity=119

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:09:14+08:00 | HN Show HN | 点赞=119 · 评论=35 · engagement_velocity=119 | [[20-语料/posts/hn_show/2026-09-21/f69b1b037e399a5a_Show-HN-DAC-–-open-source-dashboard-as-code-tool-f]] |
| 2026-09-21T01:13:42+08:00 | HN Show HN | 点赞=119 · 评论=35 · engagement_velocity=119 | [[20-语料/posts/hn_show/2026-09-21/f69b1b037e399a5a_Show-HN-DAC-–-open-source-dashboard-as-code-tool-f]] |
| 2026-09-21T01:41:53+08:00 | HN Show HN | 点赞=119 · 评论=35 · engagement_velocity=119 | [[20-语料/posts/hn_show/2026-09-21/f69b1b037e399a5a_Show-HN-DAC-–-open-source-dashboard-as-code-tool-f]] |

## 摘要正文

Hi all, this is Burak.When agents became a reality one of the first things I wanted to do was to automate building dashboards. The first, and the most obvious, wall that I ran into was that a lot of the tools were just driven by UI. This meant that without the agents handling browser UIs and whatnot, it wasn't possible to have the agents do that. In addition, it would be impossible to review any of the changes the agent would make.The first instinct there is to get your agent to build a React app for the dashboard. This works beautifully for the happy path, but I quickly ran into other issues there: - every dashboard turns out to be different - have to implement a backend to centralize the query execution - there is no centralized mechanism to control the rules and standards around visualizations - there is no way to get a semantic layer working with the dashboards easilyIn the end, agents ended up reinventing the wheel for every new dashboard, even under the same project. Building a standardized, local project for these turned out to be building a BI tool from scratch.After trying these out, I asked myself: what if the dashboards were built for agents as the primary user?A product…
