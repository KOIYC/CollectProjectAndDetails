---
type: "corpus"
item_id: "b479ca5617fc7e22"
title: "2 weeks of only building what reddit comments ask for"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xfj0x9/2_weeks_of_only_building_what_reddit_comments_ask/"
author: "Significant_Camp4148"
published_at: "2026-10-26T08:55:37+08:00"
captured_at: "2026-11-05T11:22:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-10-26"
tags:
  - 语料
  - reddit
  - r/EntrepreneurRideAlong
  - Ride Along Story
metrics: {"score": 6, "comments": 16, "upvote_ratio": 1}
comments_count: 12
comments_total: 16
discovered_via: "reddit:14d+settle10"
---

# 2 weeks of only building what reddit comments ask for

> [!info] 一句话导读
> launched a free tool called yarrow 2 weeks ago, its a place where ai coding agents share bug fixes. first version was pretty bare so my rule was if someone leav…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xfj0x9/2_weeks_of_only_building_what_reddit_comments_ask/>
> 指标：得分=6 · 评论=16 · 赞踩比=1
> 作者：Significant_Camp4148　|　发布：2026-10-26T08:55:37+08:00
> 项目链接：—
> 采集：2026-11-05T11:22:49+08:00　|　id：`b479ca5617fc7e22`

## 正文

launched a free tool called yarrow 2 weeks ago, its a place where ai coding agents share bug fixes. first version was pretty bare so my rule was if someone leaves a real critique i build it that day and reply "shipped it"

someone said fixes break when libraries update, so now the tested ones get re-run every 30 days. someone said theyd install it if it had a cli, so i put one on npm. someone found a way to fake the verified badge by editing the test instead of fixing the bug (that one stung lol). and this morning someone said stack overflow answers rot so why wouldnt mine, so votes fade over time now

people are way nicer when you actually ship what they asked for. getting people to keep using it after they install is the part i havent figured out yet

yarrow-fixes.vercel.ap p

## 评论（12/16）

> **Legitimate-Cod-7624**（1 分） · 2026-10-26T09:00:58+08:00　
> the decay idea is clever, makes it feel like a living thing instead of archive

---

> **AutoModerator**（1 分） · 2026-10-26T09:05:08+08:00　
> Your [comment](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xfj0x9/2_weeks_of_only_building_what_reddit_comments_ask/19rnpjy3i35cz/) in /r/EntrepreneurRideAlong was automatically removed because it contained a URL or a markdown link.
>
> To keep our community focused and prevent spam, we do not allow URLs or links (including Reddit internal links) in comments at this time.
> If you believe this removal was a mistake, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/EntrepreneurRideAlong).
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/EntrepreneurRideAlong) if you have any questions or concerns.*

---

> **Intrepid_Camp_2843**（1 分） · 2026-10-26T10:35:56+08:00　
> The faked badge stings but it's the most useful feedback in this post. Pin the test file's hash and rerun it in your own CI, then flag anything that touches both the test and the source in one go, otherwise "verified" just means "the author didn't get caught".

---

> **Unhappy-Goat5087**（1 分） · 2026-10-26T11:35:04+08:00　
> the badge thing is the one that should bother you more than it seems to. the whole point of yarow is supposedly 'this fix was actually tested' and then someone edits the test file and the badge says verified, so what does it verify? that a test exists? at that point the badge is decoration and the people trusting it are the ones getting burned, not you. you laugh about it stinging but thats the product, if the check is writable by the person being checked its not a check. and then votes fading because stack overflow rots, ok sure, so now an old fix that still works fine looks worse than a new one that doesnt, which makes the archive less useful the bigger it gets. and shipping every comment same day isnt a roadmap, its a queue you dont control, the guy who wanted the cli isnt the guy who'll still be running it in three months. you literally said the retention part is what you havent figured out, so maybe stop building feature requests for a week and look at why people open it once and leave

---

> **Immediate-War-5694**（1 分） · 2026-10-26T11:56:07+08:00　
> yarrow is the plant whose dried stalks you throw for I Ching readings. naming a bug fix database after divination is a choice i can respect

---

> **Hot_Statistician3302**（1 分） · 2026-10-26T13:28:01+08:00　
> On the retention part, I'd guess people come back the first time it saves them from a bug they actually hit, not just because they installed it. Maybe go back to the folks who left critique and ask if they've used it since, because anyone who cared enough to critique it is your best source on what would bring them back. The cli seems like the right direction too, since it sits where they're already working.

---

> **Salt-Entertainer-318**（1 分） · 2026-10-26T13:31:35+08:00　
> your verified badge means "a test the submitter wrote passed". thats not a sting, thats what you built. votes fading is the only honest thing here and a commenter had to tell you

---

> **Forward_Essay1959**（1 分） · 2026-10-26T17:24:42+08:00　
> that is a great way to build early trust. getting people to keep coming back is probably the real challenge now

---

> **Hot_Statistician3302**（1 分） · 2026-10-26T17:41:09+08:00　
> On keeping people after install, I'd give them a reason to come back that doesn't depend on them remembering you. Something like a heads up when a fix they used gets re-tested and fails seems ideal, since that's exactly when they'd care. You're already re-running the tested ones, so that signal is probably sitting there already.

---

> **Significant_Camp4148**（1 分） · 2026-10-27T08:59:12+08:00　
> this is basically what shipped. tests run in my sandbox not the author's, the test files get hashed before and after the fix, and if the fix touches the test, the expected output or the test config it fails. there's also outside checks now so someone other than the author can add their own test to any fix

---

> **Significant_Camp4148**（1 分） · 2026-10-27T09:00:57+08:00　
> yeah that's the part i'm stuck on rn, any ideas welcome

---

> **Realistic_Bad8501**（1 分） · 2026-10-28T06:22:39+08:00　
> love the no-nonsense approach, shipping stuff that day must feel great. keeping users hooked after install is tough tho, maybe some subtle reminders or updates could help with that.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
