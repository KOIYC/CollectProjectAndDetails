---
type: "corpus"
item_id: "a196727df3b5bc1f"
title: "I got tired of researching which skills and MCP servers to give my coding agent, so I built a tool that picks them from your project's stack (free tier)"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1x89r72/i_got_tired_of_researching_which_skills_and_mcp/"
project_url: "https://codexguild.com/"
author: "lemamali12"
published_at: "2026-10-17T21:03:44+08:00"
captured_at: "2026-10-27T23:48:00+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-17"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 3, "comments": 4, "upvote_ratio": 1}
comments_count: 4
comments_total: 4
discovered_via: "reddit:14d+settle10"
---

# I got tired of researching which skills and MCP servers to give my coding agent, so I built a tool that picks them from your project's stack (free tier)

> [!info] 一句话导读
> https://i.redd.it/fz9uf8i801wh1.png

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1x89r72/i_got_tired_of_researching_which_skills_and_mcp/>
> 指标：得分=3 · 评论=4 · 赞踩比=1
> 作者：lemamali12　|　发布：2026-10-17T21:03:44+08:00
> 项目链接：<https://codexguild.com/>
> 采集：2026-10-27T23:48:00+08:00　|　id：`a196727df3b5bc1f`

## 正文

https://i.redd.it/fz9uf8i801wh1.png

Every coding agent (Claude Code, Codex, Kimi, Gemini CLI…) has the same two problems:

1. Its training data stops at a cutoff, so it confidently uses APIs that were renamed or removed since.
2. There are thousands of skills and MCP servers out there, and figuring out which ones are worth adding (and which ones are safe) is a research project of its own.

[**CodexGuild**](https://codexguild.com/) reads your project's dependencies (names and versions only, never your code) and gives your agent:

* what changed in \*your\* stack since its training cutoff (releases, breaking changes, removed APIs)
* skills and MCP servers that fit your project, all security-scanned before they're recommended
* known fixes when it hits an error, and a check against hallucinated or malicious packages before it installs anything

It plugs in as an MCP server, and setup takes a couple of minutes.

**Does it actually help?** We measured it: same agent (Claude Code + Sonnet), same 20 real tasks, two rounds, no web access for anyone.

* Tasks solved: \*\*38% → 83%\*\* on the free tier
* Tasks about changes newer than the model's training: \*\*5/26 → 25/26\*\*
* Cost per solved task: \*\*$0.112 → $0.071\*\* (\~37% cheaper)

Methodology and per-task results: [https://codexguild.com/docs/benchmark](https://codexguild.com/docs/benchmark)

Free tier, no card: [https://codexguild.com](https://codexguild.com/)

I'd really like feedback, especially on which harness you use and what your agent keeps getting wrong.

## 评论（4/4）

> **CutDry6295**（1 分） · 2026-10-17T21:35:31+08:00　
> The benchmark is the part I would inspect before installing a recommendation server. The post says 20 real tasks, but the newer-than-cutoff result is 5/26 → 25/26; are those 26 separate cases or subtasks? Publishing the task list, baseline tools, repeated-run variance, and the rules behind “security-scanned” would make the 38% → 83% claim easier to evaluate. For each recommended MCP server, I would also want its requested permissions visible before an agent enables it.

---

> **lemamali12**（1 分） · 2026-10-17T21:47:51+08:00　
> Those 26 are separate cases, and yes, for each MCP or skill that we suggest to your coding agent, coding agent will ask you if you sure to install it before making any changes :)

---

> **Turkesh-Jaeckle**（1 分） · 2026-10-17T21:58:23+08:00　
> nice framing but the cost per solved task metric feels a bit misleading, since unsolved tasks still cost tokens. would be good to show total cost across all 20 tasks for both runs too

---

> **lemamali12**（1 分） · 2026-10-17T22:05:21+08:00　
> Thanks man
> Aha, yeah unsloved tasks also cost tokens, and we only show costs per tokens. Will keep that in mind and do one more round of testing and showcase full results

## 关联链接

- https://codexguild.com
- https://codexguild.com/docs/benchmark
- https://i.redd.it/fz9uf8i801wh1.png

## 导航

- 项目页：[[10-项目/codexguild.com_009967de]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
