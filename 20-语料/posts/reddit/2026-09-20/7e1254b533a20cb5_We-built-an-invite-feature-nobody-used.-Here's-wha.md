---
type: "corpus"
item_id: "7e1254b533a20cb5"
title: "We built an invite feature nobody used. Here's what the data actually showed."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1wi6n3d/we_built_an_invite_feature_nobody_used_heres_what/"
author: "Natural-Interest6950"
published_at: "2026-09-17T03:08:30+08:00"
captured_at: "2026-09-20T14:13:50+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 4, "comments": 9, "upvote_ratio": 0.84}
comments_count: 9
comments_total: 9
discovered_via: "reddit:7d+settle3"
---

# We built an invite feature nobody used. Here's what the data actually showed.

> [!info] 一句话导读
> A few months into running DueTrace (an app for tracking money owed between two people), we assumed our "invite a friend" feature was working fine. It wasn't. Wh…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1wi6n3d/we_built_an_invite_feature_nobody_used_heres_what/>
> 指标：得分=4 · 评论=9 · 赞踩比=0.84
> 作者：Natural-Interest6950　|　发布：2026-09-17T03:08:30+08:00
> 项目链接：—
> 采集：2026-09-20T14:13:50+08:00　|　id：`7e1254b533a20cb5`

## 正文

A few months into running DueTrace (an app for tracking money owed between two people), we assumed our "invite a friend" feature was working fine. It wasn't. When we finally pulled the numbers: 6 invite attempts, ever. 0% conversion.

We went digging instead of guessing. Turned out the problem wasn't the copy or the incentive, it was structural: 3 out of 4 ways users could search for a contact simply didn't create anything if that person wasn't already registered. The feature looked like it worked. It didn't actually do anything for most of the paths users took.

Small thing, but it reframed how we think about "nobody's using this feature" complaints, usually it's not that people don't want it, it's that something quieter is broken in a way you won't see without looking at real usage data.

Happy to go into more detail if useful, or take feedback if anyone's dealt with something similar.

(DueTrace, if anyone's curious: duetrace.com)

## 评论（9/9）

> **QuanTradin**（1 分） · 2026-09-17T03:30:15+08:00　
> 6 attempts ever is not a conversion problem, it is a plumbing problem, and those two get confused constantly. everybody reaches for the copy and the incentive first because those are the things you can change in an afternoon.
>
> three of four search paths silently doing nothing is also the kind of bug that never shows up in an error rate. it succeeded. it just succeeded at nothing.

---

> **ai_ztn**（1 分） · 2026-09-17T04:00:40+08:00　
> That 0% conversion is useful because it narrows the question from "do users want invites?" to "what job did we ask the invite to do?"
>
> I'd separate three events: the recipient already has an account, the recipient creates one, and the recipient completes the shared workflow. The copy can be fine while the handoff is still dead if the recipient cannot do anything until they register.
>
> The next test I'd run is a task-specific invite from inside the moment where collaboration is already necessary, with a recipient path that shows the exact shared item before asking for signup.
>
> Did the three successful sends come from a different workflow or user cohort?

---

> **Natural-Interest6950**（1 分） · 2026-09-17T04:21:33+08:00　
> When a user enters the app, they can search for another party using four methods:
>
> 1. Contacts
>
> 2. Phone number
>
> 3. duetrace ID
>
> 4. Email
>
> Invitations were sent only when the first option was used.

---

> **ai_ztn**（1 分） · 2026-09-17T05:26:34+08:00　
> That makes the 0% number much more useful. The invite path is only being exercised when someone searches through Contacts, so the other three search methods may be hiding the real activation gap.
>
> I'd instrument those four paths separately, then compare successful recipient actions, not just sends. If phone, ID, and email are common paths, the first fix may be making the invitation step explicit after search instead of treating Contacts as the only collaboration trigger.
>
> Do the other three paths stop before a user record is created, or do they find the person but never show an invite action?

---

> **Natural-Interest6950**（1 分） · 2026-09-17T08:00:52+08:00　
> They stop before a record is created. Phone number, ID, and email all do a lookup against existing users only. If there's no match, the search just returns "not found" and the flow ends right there, no invite action ever surfaces. Contacts is the only path that falls through to a "send invite" state when the match fails.
>
> So you're right that it's a lookup-vs-invite distinction, not a copy problem. We're planning to change the other three paths to fall through the same way Contacts does when the lookup comes up empty, rather than treating "not found" as a dead end. Appreciate you pushing on this, it's a clearer way to frame the fix than how we were thinking about it.

---

> **Grouchy-End-4439**（1 分） · 2026-09-17T08:08:26+08:00　
> yeah this tracks. the default assumption is always "users dont want it" when usually its just broken in a way that doesnt surface errors. do you have any kind of alerting now for features with near-zero completion rates?

---

> **ai_ztn**（1 分） · 2026-09-17T08:35:11+08:00　
> That fall-through change is the right fix. Once phone, ID, and email stop dying at "not found," you'll finally be measuring whether people want invites, not whether three of four doors were locked.
>
> The number I'd watch next is not invites sent. It is how many of those newly opened paths produce a second action from the invited person within a day or two.
>
> If Contacts was the only path that worked, it may also have been the path with more context (a name from the address book, a real relationship). Matching Contacts conversion on phone/email would mean you mostly had a plumbing bug. A big gap would mean the Contacts path was carrying trust or intent the other paths do not, and the product question starts there instead of at copy.

---

> **Natural-Interest6950**（1 分） · 2026-09-18T02:12:37+08:00　
> Good distinction, and honestly we don't know yet which side it'll land on. Once the fall-through ships we'll be watching exactly that: second-action rate from phone/ID/email invites vs Contacts, not just send counts. If it matches Contacts, it was plumbing. If it doesn't, that's a more interesting problem about what makes an invite feel legitimate to the recipient. Will report back either way.

---

> **Natural-Interest6950**（1 分） · 2026-09-18T02:13:03+08:00　
> Honestly, no, and that's exactly how this stayed invisible for months. We had event logging but nothing watching for "this funnel step is basically at zero." We're adding a simple threshold alert now, if a feature's completion rate drops under some floor for X days straight, someone gets pinged instead of it just sitting quiet in a dashboard nobody checks weekly.

## 导航

- 项目页：[[10-项目/We-built-an-invite-feature-nobody-used.-Here's-w_7e1254b5]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
