---
type: "corpus"
item_id: "4b8ab7ba580104f5"
title: "Show HN: Ifso.io – Personal finance simulator with no sign up required"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49776910"
project_url: "https://ifso.io/try"
author: "timer_interrupt"
published_at: "2026-09-20T15:37:30Z"
captured_at: "2026-09-21T09:44:03+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-09-20"
tags:
  - 语料
  - hn_show
  - author_timer_interrupt
  - story_49776910
  - show_hn
metrics: {"points": 7, "comments": 0, "engagement_velocity": 7}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Ifso.io – Personal finance simulator with no sign up required

> [!info] 一句话导读
> Hey all!I've been building Ifso.io, it's a personal finance simulator that lets you configure and play out life decisions.The main philosophy that I built Ifso …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49776910>
> 指标：点赞=7 · 评论=0 · engagement_velocity=7
> 作者：timer_interrupt　|　发布：2026-09-20T15:37:30Z
> 项目链接：<https://ifso.io/try>
> 采集：2026-09-21T09:44:03+08:00　|　id：`4b8ab7ba580104f5`

## 正文

Hey all!I've been building Ifso.io, it's a personal finance simulator that lets you configure and play out life decisions.The main philosophy that I built Ifso around is decision-making. I personally wanted to see what it would look like if I made some key financial decisions (ex: what would it look like if I paid extra on my mortgage principal for just a few years versus putting that money into taxable investments). The existing tools were a bit frustrating however, I felt like I wanted to just tell the simulators "here's what I want to do, how does it end up for me?", but none of the tools really allowed for that. They felt a bit over-complicated for something that I felt should be a bit more straightforward, which is why I ended up building Ifso out.You start off with entering where your finances are right now, and you configure your plan by listing out your various decisions to see how it all plays out and if your financial plan works or not.The list of decisions you can make could include the more obvious things like retiring, buying a home, upgrading your car, etc. You can also simulate what it's like to convert a property into a rental or retiring early and relying on your taxable accounts to carry you to retirement age. I also wanted to make it easy to turn certain "knobs", so if you want to update your income, retirement or investment contributions, extra principal payments, etc, you can easily do so by just updating the contribution numbers for a given year and the simulator carries it forward from that point onwards.Behind the scenes the simulation engine runs through all of the math for you, this includes income taxes, capital gains taxes if you withdraw from a taxable account, retirement account withdrawals, loan amortization schedules (and how extra principal payments might change that), and so on. You can also run Monte Carlo simulations to stress test plans, and create multiple scenarios to compare them side by side.One of the pieces of feedback I'd received is that people wished they could just use it and try it out without needing to sign up. I made the app usable without any sign in, it ends up storing your plan config locally within your browser and is fully usable. If you do want to have your plan persist across devices (or be resilient to any browser resets), you can always sign in for free if you'd like.My goal is to create an easy to use interface, and have all of the complexity be handled for you. To that end, if there's ever any UX improvement I could make or if there's any other features that would be helpful to have, let me know and I'd be happy to look into it!

## 导航

- 项目页：[[10-项目/ifso.io_4e8fceac]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
