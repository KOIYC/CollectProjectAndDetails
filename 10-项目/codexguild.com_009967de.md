---
type: "project"
title: "I got tired of researching which skills and MCP servers to give my coding agent, so I built a tool that picks them from your project's stack (free tier)"
project_url: "https://codexguild.com/"
first_seen: "2026-10-27T23:48:00+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SaaS
lang: "en"
---

# I got tired of researching which skills and MCP servers to give my coding agent, so I built a tool that picks them from your project's stack (free tier)

> [!info] 一句话导读
> https://i.redd.it/fz9uf8i801wh1.png

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://codexguild.com/>
> 首次收录：2026-10-27T23:48:00+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SaaS
> 最新指标：得分=3 · 评论=4 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:48:00+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=4 · 赞踩比=1 | [[20-语料/posts/reddit/2026-10-27/a196727df3b5bc1f_I-got-tired-of-researching-which-skills-and-MCP-se]] |

## 摘要正文

https://i.redd.it/fz9uf8i801wh1.png  Every coding agent (Claude Code, Codex, Kimi, Gemini CLI…) has the same two problems:  1. Its training data stops at a cutoff, so it confidently uses APIs that were renamed or removed since. 2. There are thousands of skills and MCP servers out there, and figuring out which ones are worth adding (and which ones are safe) is a research project of its own.  [**CodexGuild**](https://codexguild.com/) reads your project's dependencies (names and versions only, never your code) and gives your agent:  * what changed in \*your\* stack since its training cutoff (releases, breaking changes, removed APIs) * skills and MCP servers that fit your project, all security-scanned before they're recommended * known fixes when it hits an error, and a check against hallucinated or malicious packages before it installs anything  It plugs in as an MCP server, and setup takes a couple of minutes.  **Does it actually help?** We measured it: same agent (Claude Code + Sonnet), same 20 real tasks, two rounds, no web access for anyone.  * Tasks solved: \*\*38% → 83%\*\* on the free tier * Tasks about changes newer than the model's training: \*\*5/26 → 25/26\*\* * Cost per so…
