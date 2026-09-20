---
type: "corpus"
item_id: "a24e136b3e12c856"
title: "Show HN: Murmell – Collaborative cloud canvas for coding agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49499167"
project_url: "https://murmell.com/"
author: "Mossab22"
published_at: "2026-08-30T14:51:05Z"
captured_at: "2026-09-21T02:57:20+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_Mossab22
  - story_49499167
  - show_hn
metrics: {"points": 8, "comments": 3, "engagement_velocity": 8}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:52d"
---

# Show HN: Murmell – Collaborative cloud canvas for coding agents

> [!info] 一句话导读
> Hey HN!I'm Moss'Ab. Murmell (https://murmell.com) is an infinite canvas where coding agents run together in the cloud instead of on your laptop.It's like Google…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49499167>
> 指标：点赞=8 · 评论=3 · engagement_velocity=8
> 作者：Mossab22　|　发布：2026-08-30T14:51:05Z
> 项目链接：<https://murmell.com/>
> 采集：2026-09-21T02:57:20+08:00　|　id：`a24e136b3e12c856`

## 正文

Hey HN!I'm Moss'Ab. Murmell (https://murmell.com) is an infinite canvas where coding agents run together in the cloud instead of on your laptop.It's like Google Docs, except the other editors are you, your teammates, and a set of agents all working in the same canvas.Short demo: https://app.murmell.com/demoThe idea came out of a YC hackathon. We were trying to build the thing under extrem pressure, deploying at the very last minute, but with several agents working in parallel, all the branches collided. Everything broke at the worst
possible moment and we spent the end of it untangling instead of building. We didn't win.Murmell is the thing I wished we'd had that day:
one place where the agents and the people can see each other work,
on machines that don't belong to any one laptop.Each canvas gets its own machine in the cloud. Close your laptop and the agents keep going; open it again anywhere, or have a teammate open the same canvas by sending him the link, and you're inside the same session rather than a copy
of it. The work stays exactly where you left it : same branches, same dev server still running, so an agent picks up mid-task instead of starting from scratch.And you can literally collaborate with your team like google docs, it's se same system, read of edit link, they connect they can type on your terminal, you can see their mouse, wich terminal they're typing in.
And you can interact wich each other sessions, it's pretty useful instead of sharing a screen, copying a prompt, etc.The hardest part was building the cloud infrastructure, trying to make it scalable, and to manage the sessions to make the best experience possible: when the VM shuts down, it snapshots everything and restores everything when you come back, even the conversation with your terminal, it's stored with a system that i built like obsidian wich also make you save a little bit of tokens.So the answer to that hackathon is file claiming. Before an agent works on something, it claims the paths, it's an exclusive lease with a TTL, so nothing stays locked forever because an agent died mid-task. And if another agent asking for the same file gets denied, the denial tells it who holds it, how long is left, and to either pick other work in its scope or message the holder (the agents can communicate through the board)A watcher classifies every write, so if anything writes inside someone else's claim it shows up on the canvas as a
collision right then, instead of as a merge conflict you discover an hour later. And when an agent is done, it can hand its claim to the next one.And agents never hold your provider keys either, they get a token, and a proxy on the container's loopback swaps it for the real key on the way out, which makes a leaked token worthless outside that container.Murmell is paid. I've put prices at 50% off for now, because it's still not where I want to take it yet.
It is fully usable though: I develop Murmell with Murmell, every day (and tbh it's save soooo much time to us with my cofounder)And to be fully transparent with the actual prices it costs us much than we are earning but the goal is to collect feedback to make Murmell as good as possibleFor context: I'm 19, a 4th year computer engineering student, and I've been on this for about three and a half months, day and night. I discovered claude code after my father showed me first Windsurf (today Devin) for a python homework in 2024, and i think i never went somewhere without my laptop since then lol.So feel free to comment or to give feedback, or even subscribe to support the project :)

## 评论（3/3）

> **Ashutosh2007** · 2026-08-30T14:58:18.000Z　
> Great project

---

> **axuanchifan** · 2026-09-02T03:59:38.000Z　
> Interesting

---

> **Mossab22** · 2026-08-30T15:00:11.000Z　
> Thank you :)

## 关联链接

- https://app.murmell.com/demoThe
- https://murmell.com

## 导航

- 项目页：[[10-项目/murmell.com_1d79dcc8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
