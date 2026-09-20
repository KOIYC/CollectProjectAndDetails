---
type: "corpus"
item_id: "5f63721e2407444c"
title: "[Trading Strategy Optimizer] - My first paying customer found a bug that made the product impossible to activate"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1wifs4c/trading_strategy_optimizer_my_first_paying/"
project_url: "https://chromewebstore.google.com/detail/trading-strategy-optimize/pjgikffklocmefghdipdiidfebgbklon"
author: "PreparationOk3910"
published_at: "2026-09-17T09:14:43+08:00"
captured_at: "2026-09-21T03:18:40+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-09-17"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 3, "comments": 13, "upvote_ratio": 0.67}
comments_count: 10
comments_total: 13
discovered_via: "reddit:7d+settle3"
---

# [Trading Strategy Optimizer] - My first paying customer found a bug that made the product impossible to activate

> [!info] 一句话导读
> Chrome extension for traders. Free tier, $10.89/mo for the pro features. Shipped it, got the first subscriber, and within hours he emailed to say the licence ke…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1wifs4c/trading_strategy_optimizer_my_first_paying/>
> 指标：得分=3 · 评论=13 · 赞踩比=0.67
> 作者：PreparationOk3910　|　发布：2026-09-17T09:14:43+08:00
> 项目链接：<https://chromewebstore.google.com/detail/trading-strategy-optimize/pjgikffklocmefghdipdiidfebgbklon>
> 采集：2026-09-21T03:18:40+08:00　|　id：`5f63721e2407444c`

## 正文

Chrome extension for traders. Free tier, $10.89/mo for the pro features. Shipped it, got the first subscriber, and within hours he emailed to say the licence key field would not accept a paste.

Not "was buggy". Would not accept a paste at all. A 36-character key that nobody is going to type by hand. The product was, functionally, unactivatable for anyone who did not happen to type it out.

Why it happened: my panel is injected into TradingView, which listens for keyboard events globally because it has chart shortcuts on most letter keys. I already had a guard stopping keyboard events from escaping my panel — keydown, keypress, keyup, beforeinput, input. Paste is not in that list, because paste is not a keyboard event. TradingView cancels clipboard events at the document level so it can paste drawings onto a chart, and my input never saw the key.

Six test suites. 130-odd assertions. Every one of them passed, because I had tested typing.

Three things I took from it:

1. I tested the mechanism and not the gesture. Nobody types a licence key. The test that mattered was "can a human get the key from the email into the box", and I never wrote it.

2. One customer found in hours what I would not have found in a month. There is no substitute.

3. Shipping the fix the same day turned the worst possible first-customer experience into the reason he is still a customer.

The fix is a window-capture clipboard listener that performs the insert itself, and the test suite now has ten assertions for paste specifically, including one that checks a key wrapped across two lines in an email rejoins correctly.

Three-minute demo if you would rather see it than read about it: https://youtu.be/-gUqxCZSI7I

Free on the Chrome Web Store if you use TradingView: https://chromewebstore.google.com/detail/trading-strategy-optimize/pjgikffklocmefghdipdiidfebgbklon

## 评论（10/13）

> **Any_Welder_9701**（1 分） · 2026-09-17T09:18:14+08:00　
> every suite typing the key could hide the real activation issue. are you testing the actual email flow or only the input? basically every customer will use that gesture

---

> **West_Inevitable_2281**（1 分） · 2026-09-17T09:26:00+08:00　
> The same-day recovery was good, but the next question is whether this was one visible bug or part of a larger activation gap. Are you tracking the full path from license issued to key accepted to first successful optimization?

---

> **QuanTradin**（1 分） · 2026-09-17T09:29:30+08:00　
> The thing that makes this class of bug so reliable is that you are permanently in the activated state on your own machine. The licence path is the one road every paying customer walks exactly once, and the one you personally never walk again after week one.
>
> Worth checking drag and drop text and browser autofill on that same field while you are in there. Same document level cancel, same silent nothing.

---

> **PreparationOk3910**（1 分） · 2026-09-17T13:16:11+08:00　
> That is the sharpest version of it. Being permanently in the activated state on your own machine means the one road every paying customer walks exactly once is the one road you never walk again after week one, and no amount of testing fixes that on its own.
>
> You were right to point at drag and drop. I went and checked after reading this and it had the same hole, with the same silent nothing. It is fixed now and covered so it cannot come back, going out in the next release. Autofill on that field I am still working through properly rather than assuming either way.
>
> So thank you, sincerely. That is the second time this thing has been caught by someone who is not me, and this time it cost nothing.

---

> **PreparationOk3910**（1 分） · 2026-09-17T13:16:53+08:00　
> Honest answer: no, and you have put your finger on the uncomfortable part.
>
> There is no analytics in the product at all, and that is deliberate. It sits on people's charts next to their positions and I did not want to be another thing quietly watching that. The cost of the decision is exactly what you are describing: I can see that a licence validates, and after that it goes dark. Whether someone then got a run to complete, or opened it once and gave up, I have no idea.
>
> Which means I genuinely cannot tell the difference right now between one visible bug that is now fixed and a wider activation gap where this was just the part loud enough to email me about. Not a satisfying answer, but it is the true one.
>
> Working out how to close that gap without turning the thing into a telemetry product is now sitting above features on my list. If you have seen anyone do that well I would take the pointer.

---

> **PreparationOk3910**（1 分） · 2026-09-17T13:18:01+08:00　
> Only the input, which is exactly why it got through. I had proved the field could receive characters and never once proved that a person could get the key out of their inbox and into it. Those feel like the same test right up until the moment they are not.
>
> That is the bit I would pass on to anyone building something similar: test the gesture your customer will actually make, not the mechanism underneath it. The mechanism is the easy half and it is the half that gets the coverage, because it is the half you can write an assertion for without thinking about a human being.
>
> The email flow is in the tests now. I am working back through the rest of the path on the same basis, on the assumption that if one gesture went untested there are probably others.

---

> **revelationnow**（1 分） · 2026-09-17T14:58:17+08:00　
> Is this whole subreddit just AI talking to AI?

---

> **West_Inevitable_2281**（1 分） · 2026-09-17T17:47:29+08:00　
> You can close that gap without tracking behavior broadly. I would record only a few product-owned events: license validated, first optimization started, optimization completed, and first result saved or exported. Tie them to a random install ID, collect no chart or position data, and state exactly what is collected. That should separate setup failure from activation without turning the product into surveillance.

---

> **QuanTradin**（1 分） · 2026-09-17T22:35:57+08:00　
> Glad it was cheap this time. Sitting on the autofill one is the right call, that field behaves differently across browsers and guessing will just cost you a second bug.

---

> **PreparationOk3910**（1 分） · 2026-09-18T20:01:02+08:00　
> not really I'm here in flesh and blod

## 关联链接

- https://youtu.be/-gUqxCZSI7I

## 导航

- 项目页：[[10-项目/chromewebstore.google.com_0401cf94]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
