---
type: "corpus"
item_id: "4935ec6ac33c599b"
title: "Finally launching my distributed computing backend"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xcynz7/finally_launching_my_distributed_computing_backend/"
project_url: "https://murmurcomputing.ai/"
author: "MurmurRunner"
published_at: "2026-10-23T07:50:43+08:00"
captured_at: "2026-11-02T09:38:58+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-10-23"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 4, "comments": 13, "upvote_ratio": 1}
comments_count: 12
comments_total: 13
discovered_via: "reddit:14d+settle10"
---

# Finally launching my distributed computing backend

> [!info] 一句话导读
> Finally launching a computing system that lets people and ai agents run computations on idle devices while minimizing the possibility of leaking or exposing int…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xcynz7/finally_launching_my_distributed_computing_backend/>
> 指标：得分=4 · 评论=13 · 赞踩比=1
> 作者：MurmurRunner　|　发布：2026-10-23T07:50:43+08:00
> 项目链接：<https://murmurcomputing.ai/>
> 采集：2026-11-02T09:38:58+08:00　|　id：`4935ec6ac33c599b`

## 正文

Hey all,

Finally launching a computing system that lets people and ai agents run computations on idle devices while minimizing the possibility of leaking or exposing intellectual property.

The whole point is to use what you own first and burst to cloud only when you need to.

We realized that everyone is using the same mathematical functions in writing code and programs (at least simulation and calculations) but where and how they use it, the structure, is the intellectual property.  So by breaking things down to simple math, the ip stays put but you can distribute the work.

Currently only on Mac, but will be releasing Windows, Linux, and Android soon.  We have various working versions of these but what want to apply a layer of polish first.

We will be implementing a cloud backend to burst to a cloud provider of your choosing and spin up spot instances to make sure things get done on time if and when there is a deadline and there isn't sufficient capacity on your cluster.

The current work is limited but in the coming weeks will be looking at improving performance and speed (just in time fusion for known kernels) so it runs like a greased pig.

Website is linked for the curious and Murmur is now registered on the mcp registry.

I appreciate any and all feedback!

## 评论（12/13）

> **QuanTradin**（2 分） · 2026-10-23T08:28:20+08:00　
> not sure breaking it down to simple math keeps the IP put. the order and shape of the calls a node sees can say a lot about what you're building, especially in simulation code where the kernel sequence basically is the method. worth spelling out what a node operator can infer, not only what they can't read.

---

> **MurmurRunner**（1 分） · 2026-10-23T08:37:39+08:00　
> Excellent point!  We saw that too when started to run some red team tests.  If an ai or person saw the op and the node number they were able to infer what they were working on so we had to strip out ordering to the point its just an op and a payload.

---

> **QuanTradin**（2 分） · 2026-10-23T08:42:41+08:00　
> stripping the order helps a lot. payload size and timing can still hint at what's running, so padding or batching to fixed sizes is probably the next thing your red team pokes at.

---

> **MurmurRunner**（1 分） · 2026-10-23T08:46:39+08:00　
> Oh dang, alright, more good points, thanks!  Also we noticed that some models (opus) was able to figure out we were running a mortgage calculation from a specific ratio we were using, so now we have to mask values as well.

---

> **Woiteck_Jardian**（1 分） · 2026-10-23T09:28:30+08:00　
> when you say kernel sequence, do you mean the literal call graph a single node reconstructs or more the timing pattern across the whole cluster?

---

> **QuanTradin**（2 分） · 2026-10-23T09:34:12+08:00　
> masking values makes sense. a model guessing a mortgage calc from one ratio is wild though, so hardcoded constants are probably the next leak after inputs. a 0.0041 sitting in the code says a lot on its own.

---

> **dbenc**（1 分） · 2026-10-30T07:04:59+08:00　
> what if the same attacker controls multiple nodes?

---

> **MurmurRunner**（1 分） · 2026-10-30T07:21:40+08:00　
> It's a fair point. I think we would have to assume every node is colluding unless it's a wholly different service and even then that is hand wavy. I think security versus speed becomes a knob to the user.

---

> **dbenc**（1 分） · 2026-10-30T07:27:45+08:00　
> why would i ever set the security knob "down"?

---

> **MurmurRunner**（1 分） · 2026-10-30T07:33:43+08:00　
> Lack of speed. Only true safety guarantee is to run on hardware you own and control. Cloud is no exception either. Hence why on prem and data sovereignty is a thing.

---

> **dbenc**（1 分） · 2026-10-30T07:36:24+08:00　
> you think cloud computing (like ec2 instances) is as unsafe as a murmur workload?

---

> **MurmurRunner**（1 分） · 2026-10-30T07:37:19+08:00　
> Goodness no. Or at least I hope not but it could be cheaper and a heck of a lot faster.

## 导航

- 项目页：[[10-项目/murmurcomputing.ai_4a33147f]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
