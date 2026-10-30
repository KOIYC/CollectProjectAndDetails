---
type: "project"
title: "Show HN: Artificer by Nua: Frontier robotics task evaluation in 4B parameters"
project_url: "https://usenua.com/blog/artificer"
first_seen: "2026-10-30T09:46:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_SunnyWan
  - story_50296436
  - show_hn
lang: "en"
---

# Show HN: Artificer by Nua: Frontier robotics task evaluation in 4B parameters

> [!info] 一句话导读
> We’re happy to introduce Artificer, our first robotics decision model for evaluating robot task progress and success.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://usenua.com/blog/artificer>
> 首次收录：2026-10-30T09:46:09+08:00
> 来源渠道：HN Show HN
> 标签：author_SunnyWan, story_50296436, show_hn
> 最新指标：点赞=5 · 评论=2 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-30T09:46:09+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-10-30/c891b7ae1999c822_Show-HN-Artificer-by-Nua-Frontier-robotics-task-ev]] |

## 摘要正文

We’re happy to introduce Artificer, our first robotics decision model for evaluating robot task progress and success. The problem Robot systems need feedback during training, evaluation, and deployment. An arm might grasp the right object, but place it in the wrong bin. A robot might’ve only completed part of its task before it stopped. Assessing these outcomes from video often requires manual review or brittle, handcrafted objectives. Though frontier models do well in evaluation, they are expensive and slow. Artificer is a 4B parameter model that estimates task completion and progress, at the frontier level, from a task description and video. During deployment, these estimates provide feedback to a robot controller to help decide whether to continue an attempt, retry, or move to the next task.Know a robotics team working on task evaluation or success detection? We'd appreciate an introduction! For the robotics founders: we’d love to test Artificer on your task videos! Would love to chat more in the comments or over email! sunny@trynua.dev
