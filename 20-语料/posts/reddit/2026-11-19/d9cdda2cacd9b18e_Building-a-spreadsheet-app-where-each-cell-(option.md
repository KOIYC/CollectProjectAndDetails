---
type: "corpus"
item_id: "d9cdda2cacd9b18e"
title: "Building a spreadsheet app where each cell (optionally) being a terminal / coding agent is a first class property"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1xre6fl/building_a_spreadsheet_app_where_each_cell/"
project_url: "https://github.com/sshah03/recalc"
author: "0xcontext"
published_at: "2026-11-09T08:55:53+08:00"
captured_at: "2026-11-19T09:44:24+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 11, "upvote_ratio": 1}
comments_count: 9
comments_total: 11
discovered_via: "reddit:14d+settle10"
---

# Building a spreadsheet app where each cell (optionally) being a terminal / coding agent is a first class property

> [!info] 一句话导读
> https://reddit.com/link/1xre6fl/video/kuobaorijh0i1/player

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1xre6fl/building_a_spreadsheet_app_where_each_cell/>
> 指标：得分=3 · 评论=11 · 赞踩比=1
> 作者：0xcontext　|　发布：2026-11-09T08:55:53+08:00
> 项目链接：<https://github.com/sshah03/recalc>
> 采集：2026-11-19T09:44:24+08:00　|　id：`d9cdda2cacd9b18e`

## 正文

https://reddit.com/link/1xre6fl/video/kuobaorijh0i1/player

[https://github.com/sshah03/recalc](https://github.com/sshah03/recalc)

Since spreadsheets are so versatile, really looking for feedback on where people would want this to go, in a way that can be useful to them, or what use cases they see themselves using it for in its current iteration that I can make more seamless.

I can provide some context on why it was useful for me / why I built it. I was using Claude to help me build benchmark sets, and found pouring through CSVs / MD files of the results a bit tiresome, so I decided to build a spreadsheet app for myself that's driven by Claude Code, and where each cell can be its own Agent if you want (and can later be opened up and continued in a full terminal if needed as its own session).

You can use it as a standard spreadsheet, or use a cell as a shell command / agent. Having built a startup for using AI in tax work, I also realized it can be very powerful for tax work, legal work, etc... so I built in some examples for running that, though I'm not sure how many people in those professions use claude code.

The video is just a demo of me building "FDA Bench" using recalc, pick FDA approval cases past the model cutoff dates, and seeing if an AI harness (without web searches) could've successfully predicted, based on all the info submitted to the FDA, whether the submission would pass FDA approval or not. Fable was right 75% of the time in this small sample size. Just a fun little exercise to show off some of what it can do.

*Note: Since it's just terminal sessions glued together, it works with your existing plans. The sessions talk to each other with an MCP server running in the back.*

## 评论（9/11）

> **0xcontext**（1 分） · 2026-11-09T08:57:00+08:00　
> https://reddit.com/link/1xre6fl/video/sb0qw72ljh0i1/player
>
> In case the video doesn't work in the main post.

---

> **Brufacee**（3 分） · 2026-11-09T08:57:48+08:00　
> The cell-as-agent idea is interesting, but the FDA benchmark and tax/legal examples point to very different buyers. I would start with the benchmark analysis pain you actually had and show one before/after: scattered CSVs and notes in, repeatable result table out. Then ask a few people who build evals whether they would use it weekly. Who is the first user you want to win?

---

> **0xcontext**（2 分） · 2026-11-09T09:01:01+08:00　
> That's a good point and idea. The reality is I'm not sure. I built this for myself then decided to offer it up for free and I'm curious who it would help most, and I'm trying to figure that out. It's very valuable for me, but I assume benchmarkers and people obsesses with building evals is a relatively niche community. I provided Tax/Legal examples because I started a startup in that space and realized a spreadsheet with AI as a first party tool could actually handle much of what people charge SaaS subscriptions for with a basic claude/gpt subscription ...
>
> Given the nature of Spreadsheets being a playgorund for so much different kind of work I guess I'm having trouble figuring out the ideal initial use case, so I'm just looking for feedback.

---

> **Ill_Fun5415**（2 分） · 2026-11-09T09:32:14+08:00　
> The part I care about is where the workflow stops for inspection. A tool can look impressive in one pass, but the real trust comes from seeing the diff, the log, and the rollback point before it keeps going.

---

> **0xcontext**（1 分） · 2026-11-09T09:35:22+08:00　
> Thus far, I haven't injected my specific own prompts into controlling this, just an MCP server with instructions that Claude Code / Codex would be aware of and it's ultimately up to their judgement on when this is. So as the models improve, or the prompting improves, what you're looking for improves.
>
> However, that's a good point, if I'm presenting that as a feature, I could do more to ensure that's handled well.

---

> **Brufacee**（2 分） · 2026-11-09T09:46:55+08:00　
> That makes sense. I’d keep it broad as a tool, but pick one example for the first landing page. The eval workflow is the one you already know is valuable, so a couple of benchmarkers trying the same template would give you real usage data. You can still show tax and legal examples after people understand the basic idea.

---

> **Zestyclose_Cow1807**（3 分） · 2026-11-09T20:41:17+08:00　
> yeah the tax and legal crowd feels like a massive leap when the core mechanic is basically terminal sessions.

---

> **Ill_Fun5415**（1 分） · 2026-11-09T21:31:19+08:00　
> The check I would trust is the one tied to the actual diff. If the patch cannot point to the test or log that changed, I would stay cautious.

---

> **Brufacee**（1 分） · 2026-11-10T09:08:10+08:00　
> Yes, I would start with people who already work in terminals and move results into spreadsheets. Less of a behaviour change, and they can judge whether it saves them time.

## 关联链接

- https://reddit.com/link/1xre6fl/video/kuobaorijh0i1/player

## 导航

- 项目页：[[10-项目/github.com_08c6391f]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
