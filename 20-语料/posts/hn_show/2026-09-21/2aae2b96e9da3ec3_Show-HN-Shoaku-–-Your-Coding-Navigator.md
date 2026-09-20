---
type: "corpus"
item_id: "2aae2b96e9da3ec3"
title: "Show HN: Shoaku – Your Coding Navigator"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48733144"
project_url: "https://github.com/seachicken/intellij-shoaku"
author: "seachicken"
published_at: "2026-06-30T14:24:33Z"
captured_at: "2026-09-21T01:44:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_seachicken
  - story_48733144
  - show_hn
metrics: {"points": 4, "comments": 4, "engagement_velocity": 4}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:113d"
---

# Show HN: Shoaku – Your Coding Navigator

> [!info] 一句话导读
> AI Agents like Codex and Claude are incredibly powerful and have drastically sped up implementation.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48733144>
> 指标：点赞=4 · 评论=4 · engagement_velocity=4
> 作者：seachicken　|　发布：2026-06-30T14:24:33Z
> 项目链接：<https://github.com/seachicken/intellij-shoaku>
> 采集：2026-09-21T01:44:31+08:00　|　id：`2aae2b96e9da3ec3`

## 正文

AI Agents like Codex and Claude are incredibly powerful and have drastically sped up implementation.
However, I noticed a strange side effect: I began to lose confidence in my own coding.
I submitted a pull request after the AI completed the implementation. It looked good, but during code review, I was asked, "Why did you implement it this way?" I grew increasingly embarrassed because I couldn't immediately explain the complex code.
Previously, I built confidence by understanding the design through reading and writing code, which was enjoyable, but now I've lost that.This coding assistant helps users understand their thought process and coding progress, with the AI acting solely as a guide and not writing code on its own. To still leverage the AI agent's autonomous implementation capabilities, a separate AI thread runs in the background in a temporary working directory, providing highly accurate navigation assistance to the user.The AI's responses are still a bit strange at times, but if this concept resonates with you, please share your feedback. As a solo creator, I find that very encouraging. Thank you.

## 评论（4/4）

> **omarmium12** · 2026-06-30T15:06:34.000Z　
> Thanks, will be checking it out, I certainly have noticed that my coding skills have drastically become weaker as the ai becomes more capable and agentic.

---

> **pmb_developer** · 2026-06-30T15:22:56.000Z　
> Interesting concept. How do you make sure the “navigator” helps the user understand the reasoning instead of becoming another layer of AI-generated abstraction?

---

> **seachicken** · 2026-06-30T21:38:00.000Z　
> Exactly. Gradually, I find myself wanting to rely on AI even for simple tasks since it’s actually getting better at writing good code. As a result, our dependence on agents is increasing. I think there's a lot we can learn from writing the code ourselves.

---

> **seachicken** · 2026-06-30T21:04:43.000Z　
> That's an important point. In Shoaku, humans break down the task using a target Markdown file, and the AI focuses solely on assisting with the current task. When humans write code, the AI also provides support for that line (sending operation events via LSP). I want it to be like pair programming, where we create things together. I feel like recent agents are creating things far beyond what humans want, so human understanding is being put on the back burner.

## 导航

- 项目页：[[10-项目/github.com_781031d8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
