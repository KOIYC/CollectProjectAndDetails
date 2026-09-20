---
type: "corpus"
item_id: "9ea03a8929cc550d"
title: "Show HN: Reintroducing Micro: A Personal Assistant for Everyone"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49741792"
project_url: "https://micro.mu/blog/post?id=1789656583547416701"
author: "asim"
published_at: "2026-09-17T14:57:51Z"
captured_at: "2026-09-20T09:36:51+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_asim
  - story_49741792
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Reintroducing Micro: A Personal Assistant for Everyone

> [!info] 一句话导读
> Published: 2026-09-17

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49741792>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：asim　|　发布：2026-09-17T14:57:51Z
> 项目链接：<https://micro.mu/blog/post?id=1789656583547416701>
> 采集：2026-09-20T09:36:51+08:00　|　id：`9ea03a8929cc550d`

## 正文

Published: 2026-09-17

Reintroducing Micro: A Personal Assistant for Everyone | Micro

# Reintroducing Micro: A Personal Assistant for Everyone

17 September 2026 Asim

Updated 17 September 2026

Ten years ago, I introduced Micro as an open source microservices toolkit.

I’d seen microservices work at the company I was working at. They let teams develop services independently, but each team still needed the same infrastructure for discovery, communication and handling failures. Micro provided those building blocks so developers could get on with writing their software.

The name came from the work. Go Micro was a microservices framework for Go. When it became a toolkit, we dropped the Go.

I wanted to build technology that people anywhere could use. Google and GitHub were reference points for that ambition. Micro’s starting point was developers, because that was the work I understood and the problem I could address.

Over the following decade, I worked on frameworks, cloud hosting and APIs. More recently, I brought a set of services together into a personal server. It could handle mail, store notes, schedule reminders and retrieve information.

Each service had its own interface. As I added services, the product became harder to use. There were too many pages, and too much of the underlying structure was exposed to the user.

The services were useful. The interface needed to change.

Micro is now a personal assistant, available at micro.mu. You describe what you need, and the assistant uses the services to carry out the request.

You can ask a question, discuss something, save a note or set a reminder. The web interface provides a conversation and access to what you’ve saved or scheduled. You can also reach the assistant by email.

The purpose is to reduce the work involved in using these tools. An email may contain a commitment you need to follow up on. A discussion may produce a decision worth keeping. A morning brief can help you prepare for the day. These are ordinary tasks, but they take time and are easy to lose track of.

There are further capabilities I want to add. For a trip, the assistant should be able to check availability and return a few places to stay. I can then choose and make the booking. For an MOT, it should be able to look up the expiry date, remember the vehicle registration and set a reminder when asked.

Those requests have limits. Looking for accommodation does not authorise a booking. Access to an email account does not justify reading its entire history. The assistant should carry out the instruction it was given and make clear when it cannot.

Privacy remains unfinished work. Micro uses cloud-hosted models, and information retrieved by its tools can be sent to those models. Self-hosting does not prevent that. We need controls over what is retrieved, what is retained and what is used for background work. Those controls need to be enforced in the software.

The aim is for Micro to be usable by people who have no reason to know what a microservice or an API is. That is what “for everyone” means here. The hosted service removes the need to install and operate it. The underlying runtime remains open source.

The architecture still owes a lot to the Unix approach: small tools with defined responsibilities, composed to do useful work. The assistant provides another way to use them.

There is more to do before V2 is finished. Accepted requests need to survive a lost connection or server restart. Reminders need to arrive when expected. Saved work needs to be easy to find, and access to personal data needs clear limits.

That is the current focus. Micro is available at micro.mu.

# hyper-serve/video-uploader

## 导航

- 项目页：[[10-项目/micro.mu_a8c5f686]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
