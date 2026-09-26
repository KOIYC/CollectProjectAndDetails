---
type: "corpus"
item_id: "a9af4066c1445932"
title: "Show HN: Tui2web – use any TUI on the web"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49846613"
project_url: "https://tui2web.com/"
author: "czhu12"
published_at: "2026-09-25T16:22:08Z"
captured_at: "2026-09-26T09:41:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-26"
pub_day: "2026-09-25"
tags:
  - 语料
  - hn_show
  - author_czhu12
  - story_49846613
  - show_hn
metrics: {"points": 7, "comments": 2, "engagement_velocity": 7}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Tui2web – use any TUI on the web

> [!info] 一句话导读
> I built this utility because there have been a ton of times I started a claude session and then wanted to go for a walk, or a coffee break, while thinking about…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49846613>
> 指标：点赞=7 · 评论=2 · engagement_velocity=7
> 作者：czhu12　|　发布：2026-09-25T16:22:08Z
> 项目链接：<https://tui2web.com/>
> 采集：2026-09-26T09:41:08+08:00　|　id：`a9af4066c1445932`

## 正文

I built this utility because there have been a ton of times I started a claude session and then wanted to go for a walk, or a coffee break, while thinking about whatever I was working on, and keep prompting the agent.I used a hacky VPS + Termius setup while I was backpacking / nomading across Europe and Asia, which allowed me to be modestly productive, but connections kept dropping, and the transfer of files, context, etc from my laptop to VPS was annoying.tui2web basically mirrors any terminal UI application (claude, opencode, omp, even bash or vim) to the web. I know claude and codex (?) has remote sessions, but I never managed to get it working and none of the other open source harnesses do, and they all require way too much setup on my phone when I already have a mobile browser I quite like.All traffic runs through a relay I'm hosting and providing for free. I was using this for a few days myself before it became too sketchy to run this through public internet, so I added first class Tailscale support.I think the security is definitely top of mind. Anything on public internet feels prey at this point, curious to hear if anyone has any feedback to make this more locked down.

## 评论（2/2）

> **knighthacker** · 2026-09-25T17:34:23.000Z　
> Nice. That need was one of my initial inspirations for AQ as well. The VPS plus dropped-connections part of your story is very familiar. Two things mattered most when I worked on this same problem:first, persistence has to live server-side (tmux or equivalent), so the browser tab is only a view and never the owner of the session; if the tab dying can kill work, mobile use stays fragile.Second, on your security question: the relay path sees every keystroke and whatever secrets scroll through the terminal, so I'd frame it as custody rather than transport. Keep credentials only on the executing machine, make any shareable view a short-lived, token-scoped link with an explicit revoke, and treat Tailscale-first as the default rather than the fallback.Disclosure: I'm building AQ (aq.dev), which lives in this same problem space (agent sessions that keep running after you close the laptop, joinable from a browser), so I've spent a lot of time on exactly these two questions. We compared the options, including the plain VM plus tmux route, here: https://aq.dev/guides/keep-claude-code-running-after-closing...

---

> **dang** · 2026-09-26T00:01:25.000Z　
> Can you please not post AI-generated or AI-edited comments to HN? It's not allowed here - see https://news.ycombinator.com/newsguidelines.html#generated and https://news.ycombinator.com/item?id=47340079.Of course, it's impossible to know for sure what was LLM processed or not, but some of your posts (like this one) have been getting classified that way.

## 导航

- 项目页：[[10-项目/tui2web.com_7c824d9c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
