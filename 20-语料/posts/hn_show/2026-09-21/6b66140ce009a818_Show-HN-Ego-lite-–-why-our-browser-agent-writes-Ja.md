---
type: "corpus"
item_id: "6b66140ce009a818"
title: "Show HN: Ego lite – why our browser agent writes JavaScript not CLI commands"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48337671"
project_url: "https://github.com/CitroLabs/ego-lite"
author: "Nicole9"
published_at: "2026-05-30T16:03:19Z"
captured_at: "2026-09-21T02:52:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_Nicole9
  - story_48337671
  - show_hn
metrics: {"points": 12, "comments": 8, "engagement_velocity": 12}
comments_count: 8
comments_total: 8
discovered_via: "hn:show_hn:144d"
---

# Show HN: Ego lite – why our browser agent writes JavaScript not CLI commands

> [!info] 一句话导读
> The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, with…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48337671>
> 指标：点赞=12 · 评论=8 · engagement_velocity=12
> 作者：Nicole9　|　发布：2026-05-30T16:03:19Z
> 项目链接：<https://github.com/CitroLabs/ego-lite>
> 采集：2026-09-21T02:52:53+08:00　|　id：`6b66140ce009a818`

## 正文

# citrolabs/ego-lite

The fastest browser for AI agents to run browser automation, built for sharing your logged-in browser state with your AI agents, like Codex or Claude Code, without disturbing you. Zero cost, zero config.

- Stars: 12598
- Forks: 656
- Watchers: 12598
- Open issues: 124
- License: MIT License
- Homepage: https://lite.ego.app
- Default branch: main
- Created: 2026-04-16T12:51:09Z

## Languages

- CSS
- HTML
- JavaScript
- Shell
- Standard ML
- TypeScript

## Topics

- agent-skills
- ai-agent
- automation
- browser
- browser-automation
- claude-code
- codex
- hermes-agent
- skills
- skills-sh

## Top Contributors

- section9-lab (108 contributions)
- WUXM5 (104 contributions)
- braxtonROSE4 (12 contributions)
- aute (10 contributions)
- qddegtya (9 contributions)
- yarin-zhang (3 contributions)

---

## README

**The fastest browser for AI agents to run browser automation**

ego (lite) is a browser where you and your AI agents work in parallel. Your agents run multiple browser tasks in their own Spaces while your tabs stay yours, and tasks complete faster on fewer tokens.

Existing tools like browser-use and agent-browser are browser automation frameworks: they need a separate browser to drive, logins never carry cleanly, and you and the agent end up fighting for the same tabs. ego lite is one browser designed from the start for the two of you to share. No extra setup, and the agent can always reach your real logins and tabs through `ego-browser`.

## Demo

https://github.com/user-attachments/assets/ffe7954b-58ee-411e-b35d-ec30c58a08bc

## Quick Start

ego lite runs on macOS today. Windows and Linux are on the roadmap.

### 1. Install

Pick whichever fits your flow.

**1.1 Download the macOS app**

Click to download, then open it to install. Either way, ego lite adds the `ego-browser` skill to every agent's skills directory on your machine.

**1.2 Add the skill with npx**

Install just the `ego-browser` skill:

```bash
npx skills add citrolabs/ego-lite
```

The first time your agent runs a browser task, it walks you through installing the ego lite app.

**1.3 Let your agent set it up**

Paste this into your agent:

```
Set up ego lite for me: https://github.com/citrolabs/ego-lite

Read `skills/ego-browser/references/install.md` and follow the steps to install ego lite.
```

On first launch, ego lite asks one question, whether to migrate your Chrome data. Say yes and your agent inherits your existing logins, cookies, extensions, and bookmarks.

### 2. Run your first task

In your agent CLI, type `/ego-browser` followed by a space, then describe what you want in plain language:

```
ego-browser follow @ego_agent on x.com for me
```

The agent picks up the `ego-browser` skill, opens the page in its own Space, reads a Snapshot, acts on the page, and reports back, all while your own tabs stay untouched.

Your browsing data stays on your device. ego lite only records whether you opted into Chrome migration during setup.

## Highlight of ego lite

| Feature | What it does |
|---|---|
| **Code base, not CLI base, for faster runs with fewer tokens on complex tasks** | The capabilities ego lite exposes to the agent are wrapped as JavaScript functions the agent calls directly. The agent gets to do what it does best: write code, composing a multi-step task into a single output instead of getting stuck in a "call two commands, look at the result, call two more commands" loop. Compared to the conventional CLI approach, complex workflows finish up to 2.5× faster with higher task success rates and far fewer tool calls per task. |
| **A dedicated Space for every agent** | ego lite gives each agent its own fully isolated Space. You browse up front, your agent works in the background, and they don't get in each other's way. You can see which Space has an agent running at any moment, and take it over or stop it whenever you want. |
| **Your agents multitask in Spaces, parallel workspaces inside the same browser** | Each Space gets its own AI agent or its own task, all running at the same time. Claude Code enriching 10 leads in 10 parallel Spaces. Codex scraping 5 competitor sites in 5 more. They don't collide or steal your tabs. Your mouse stays where you left it. |
| **The strongest page Snapshot on the market** | Thanks to kernel-level customization, ego lite produces the highest-quality page snapshots, the view text models rely on to "see" and act on a webpage. It reliably handles tough cases like deeply nested iframes, exactly where other approaches consistently break down. |
| **Any agent can drive it through `ego-browser`** | `ego-browser` is the connection layer between any agent CLI (Claude Code, Codex, Cursor, or a custom one) and ego lite. It exposes the browser as a set of in-page JavaScript tools: snapshot, fill, click, wait, navigate, capture. The agent writes a JavaScript snippet calling those tools, and `ego-browser` runs it on the page in one pass. |
| **Experience accumulation that makes your agent faster the more you use it** *(coming soon)* | Most of an agent's time on browser tasks goes to trial and error. ego lite's official Skill distills every successful action into reusable tools and workflows, so similar tasks down the line run up to 5x faster. |

## ego lite vs existing products

Most tools can automate a browser. The real questions are what browser the agent gets, whether you can keep working at the same time, and whether the tool is built for the agent you already use or a built-in one.

| Capability | ego lite | Browser-Use | agent-browser (Vercel) | ChatGPT Atlas | Perplexity Comet |
|---|:---:|:---:|:---:|:---:|:---:|
| Multitask in parallel | ✓ | — | — | — | — |
| Reusable skills | ✓ | — | — | — | — |
| Inherits Chrome's data | ✓ | — | — | ✓ | ✓ |
| Same browser, separate workspace | ✓ | — | — | — | — |
| Compressed semantic input | ✓ | — | ✓ | — | — |
| Controllable by external agents | ✓ | ✓ | ✓ | — | — |
| Data stored locally | ✓ | ✓ | ✓ | — | — |
| No login friction | ✓ | — | — | ✓ | ✓ |
| Daily-use browser | ✓ | — | — | ✓ | ✓ |
| Free | ✓ | ✓ | ✓ | — | — |

Two other categories try to solve the same problem. Browser automation frameworks like Browser-Use and Vercel's agent-browser are libraries the agent calls; they ship no browser of their own, so they need a separate one to drive and your logins rarely carry cleanly. AI browsers like ChatGPT Atlas and Perplexity Comet ship a built-in agent, and only that agent can drive the browser. ego lite is one browser, designed from the start for you and any agent you bring to share.

## Benchmarks

We benchmarked ego lite against Vercel's agent-browser on four complex browser automation tasks. ego lite finished each task up to 2.5× faster, with substantially fewer tokens. The harder the task, the bigger the gap. Check the comparison.

## Docs

Tutorials, the full tool reference, and integration guides live at lite.ego.app/document/.

## Community

- Discord, questions, setup help, and skill sharing
- GitHub Discussions, ideas and longer threads
- X/Twitter, updates and releases

## Star History

## License

The contents of this repository are released under the MIT License. The ego lite browser is a separate, free download.

## 评论（8/8）

> **braxton4** · 2026-05-30T16:25:59.000Z　
> smart move, when I was using agent browser,I have to watch it execute commands one by one, it’s really inefficient. using JS code to execute all commands at once is smart.

---

> **imJack** · 2026-05-30T16:30:46.000Z　
> This might be a niche use case, but I love using browser agents for web games.A browser that can run multiple agent-controlled sessions at the same time basically turns multiboxing from a chore into a one-click experience. My productivity may not improve, but my game progression definitely will.

---

> **haruharuha** · 2026-05-30T16:44:42.000Z　
> Just tried it out, the Space concept is exactly what I’ve wanted all along,which so straightforward: agent gets its own independent space but still holds my credentials. Browsers like Dia, which evolved from Arc (working on the workspace concept very early on), should have taken this route ages ago. What a missed opportunity that they didn't integrate it this way.

---

> **haruharuha** · 2026-05-30T16:51:48.000Z　
> I’ve been wanting to use browser automation to track private twitter accounts that I already follow, since the API obviously won't cut it. My main concern with this browser's automation features is account safety—how well does it mask itself? I'm worried it might trigger the platform's anti-bot detection and get my account flagged or banned :(

---

> **qddegtya** · 2026-05-30T16:28:08.000Z　
> Why javascript ?

---

> **qddegtya** · 2026-05-31T03:43:33.000Z　
> I've tried this with my own x scenario, it works fine.

---

> **braxton4** · 2026-05-30T16:34:03.000Z　
> I have read the repo, from what I can see is the thing used to connect the browser is writen in js, command and tool all stay in js makes the execution faster, make sense, but I m not sure, coz I haven’t read about their benchmark, could just a story lol

---

> **qddegtya** · 2026-05-30T16:42:18.000Z　
> Thanks bro, I'll check the repo by myself.My point is here: There are many popular AI-Friendly PL, eg. Python, Rust ...I also see many CDP-based framework which implemented by Python-Binding libs, They works very well.I think javascript is not the only option.

## 关联链接

- https://github.com/citrolabs/ego-lite
- https://github.com/user-attachments/assets/ffe7954b-58ee-411e-b35d-ec30c58a08bc
- https://lite.ego.app

## 导航

- 项目页：[[10-项目/github.com_5ede3609]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
