---
type: "project"
title: "Show HN: Tui2web – use any TUI on the web"
project_url: "https://tui2web.com/"
first_seen: "2026-09-26T09:41:08+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_czhu12
  - story_49846613
  - show_hn
lang: "en"
---

# Show HN: Tui2web – use any TUI on the web

> [!info] 一句话导读
> I built this utility because there have been a ton of times I started a claude session and then wanted to go for a walk, or a coffee break, while thinking about…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://tui2web.com/>
> 首次收录：2026-09-26T09:41:08+08:00
> 来源渠道：HN Show HN
> 标签：author_czhu12, story_49846613, show_hn
> 最新指标：点赞=7 · 评论=2 · engagement_velocity=7

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:41:08+08:00 | HN Show HN | 点赞=7 · 评论=2 · engagement_velocity=7 | [[20-语料/posts/hn_show/2026-09-26/a9af4066c1445932_Show-HN-Tui2web-–-use-any-TUI-on-the-web]] |

## 摘要正文

I built this utility because there have been a ton of times I started a claude session and then wanted to go for a walk, or a coffee break, while thinking about whatever I was working on, and keep prompting the agent.I used a hacky VPS + Termius setup while I was backpacking / nomading across Europe and Asia, which allowed me to be modestly productive, but connections kept dropping, and the transfer of files, context, etc from my laptop to VPS was annoying.tui2web basically mirrors any terminal UI application (claude, opencode, omp, even bash or vim) to the web. I know claude and codex (?) has remote sessions, but I never managed to get it working and none of the other open source harnesses do, and they all require way too much setup on my phone when I already have a mobile browser I quite like.All traffic runs through a relay I'm hosting and providing for free. I was using this for a few days myself before it became too sketchy to run this through public internet, so I added first class Tailscale support.I think the security is definitely top of mind. Anything on public internet feels prey at this point, curious to hear if anyone has any feedback to make this more locked down.
