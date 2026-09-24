---
type: "corpus"
item_id: "b1ebc2391b947fa0"
title: "I built a browser-based digital logic simulator that actually simulates the circuit"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1wk8hes/i_built_a_browserbased_digital_logic_simulator/"
project_url: "https://v.redd.it/yjyxicqrc3qh1"
author: "Ok_Wishbone_2544"
published_at: "2026-09-19T09:22:49+08:00"
captured_at: "2026-09-22T12:54:39+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-09-22"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 6, "comments": 4, "upvote_ratio": 1}
comments_count: 4
comments_total: 4
discovered_via: "reddit:7d+settle3"
---

# I built a browser-based digital logic simulator that actually simulates the circuit

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1wk8hes/i_built_a_browserbased_digital_logic_simulator/>
> 指标：得分=6 · 评论=4 · 赞踩比=1
> 作者：Ok_Wishbone_2544　|　发布：2026-09-19T09:22:49+08:00
> 项目链接：<https://v.redd.it/yjyxicqrc3qh1>
> 采集：2026-09-22T12:54:39+08:00　|　id：`b1ebc2391b947fa0`

## 评论（4/4）

> **Constant_Neck_9711**（2 分） · 2026-09-19T09:29:31+08:00　
> the 'actually simulates' is doing a lot of heavy lifting there. Logisim says the same and then your clocked flip flop oscillates into the void. I lost a whole weekend in college building a 4 bit adder in it and never once got the carry to behave

---

> **QuanTradin**（2 分） · 2026-09-19T10:29:51+08:00　
> four valued signals are the right call, X and Z staying visible instead of collapsing to false is most of the value.
>
> on determinism, simultaneity is what bites. two events landing on the same simulated nanosecond need a total ordering rule, not a queue that happens to pop them in registration order today.

---

> **Ok_Wishbone_2544**（1 分） · 2026-09-19T12:11:57+08:00　
> Agreed, and that's the rule; the queue orders the heap by (time, sequence), where sequence is a monotonic counter defined at push time. So a tie has one answer rather than "today's answer".
> So, the total order buys reproducibility rather than resolution.
>
> But, the fragile turns out to be the upstream; sequence is assigned at push time, so push order has to be deterministic too, and that lies on sorting the document keys during netlist construction.
>
> You can check this example: https://logits.nexul.in/preview/example/d_Qz7nRvKa3LmE

---

> **Pretend_Key_3980**（1 分） · 2026-09-19T14:41:59+08:00　
> Sounds like you had quite the frustrating experience with Logisim. It's always a bummer when things don’t work out as expected, especially after spending so much time on them.

## 导航

- 项目页：[[10-项目/v.redd.it_d38ff4d7]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
