---
type: "corpus"
item_id: "7d0c0577b0cd3036"
title: "My iOS app froze for testers and I only found out because I pulled crash files off a phone by hand. So I added Sentry, very carefully"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xh7ke2/my_ios_app_froze_for_testers_and_i_only_found_out/"
project_url: "https://apps.apple.com/app/id6775021634"
author: "AlternativeOk1991"
published_at: "2026-10-28T06:56:55+08:00"
captured_at: "2026-11-07T09:44:39+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-07"
pub_day: "2026-10-28"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 3, "comments": 7, "upvote_ratio": 1}
comments_count: 6
comments_total: 7
discovered_via: "reddit:14d+settle10"
---

# My iOS app froze for testers and I only found out because I pulled crash files off a phone by hand. So I added Sentry, very carefully

> [!info] 一句话导读
> I'm building Echo, a small iOS app that shows you one old photo from your own camera roll every day. The whole pitch is that your photos stay on your phone. So …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xh7ke2/my_ios_app_froze_for_testers_and_i_only_found_out/>
> 指标：得分=3 · 评论=7 · 赞踩比=1
> 作者：AlternativeOk1991　|　发布：2026-10-28T06:56:55+08:00
> 项目链接：<https://apps.apple.com/app/id6775021634>
> 采集：2026-11-07T09:44:39+08:00　|　id：`7d0c0577b0cd3036`

## 正文

I'm building Echo, a small iOS app that shows you one old photo from your own camera roll every day. The whole pitch is that your photos stay on your phone. So for months I had zero crash reporting, on purpose.

Then version 1.41 started freezing on testers. The system watchdog was killing the app and I had no idea. I only found it because I got the .ips crash files off a test phone by hand and read them.

That was the push to add Sentry. What I actually configured, in case it helps anyone with a privacy-heavy app:

- **No screenshots.** The screen is literally people's photos.
- **No view hierarchy.** Labels can contain their notes and place names.
- **No session replay, no performance tracing, no IP, no email.**
- **Scrubbing before send.** File paths, photo IDs and locations are stripped from every event.
- **One anonymous ID across tools.** The user id is the same anonymous ID RevenueCat uses, so a crash can be matched to a purchase problem without knowing who anyone is.
- **A remote kill switch.** A feature flag can turn Sentry off without shipping an update.
- **The free plan is enough.** It gives 5k errors a month, and I capped the DSN at 300 events an hour.
- **dSYMs upload automatically.** It's part of the release lane, so watchdog kills and hangs come back symbolicated.

The funny part came a few weeks later. My CI runs on my own Mac, and every simulator test run was reporting into Sentry, PostHog and RevenueCat as if it were a real person. My dashboards were mostly me. Version 1.46 now detects XCTest, CI and the simulator and keeps all three quiet.

Curious how other people handle crash reporting when the screen itself is the private data. Do you just turn screenshots off, or skip crash tools entirely?

(App is here if anyone wants to see what we're protecting: https://apps.apple.com/app/id6775021634)

## 评论（6/7）

> **QuanTradin**（1 分） · 2026-10-28T08:34:59+08:00　
> I'd copy the remote kill switch first. a privacy promise you can only honour by shipping an update is not one you fully control. the scrubbing list is good too, though file paths leak through stack trace frames as well as event fields, worth checking those get the same treatment.

---

> **AlternativeOk1991**（1 分） · 2026-10-28T09:09:10+08:00　
> Good catch, and you're right on both. I checked: the scrubber currently covers the message, exception values, tags, breadcrumbs and contexts, but not stack frames. For native Swift crashes the frames are mostly symbols plus the app binary's path, so memory file names shouldn't show up there. But "shouldn't" isn't a test. Frames are going into the redactor and the test suite. Thanks, this is exactly the kind of review I was hoping for.

---

> **QuanTradin**（1 分） · 2026-10-28T09:33:07+08:00　
> frames are the safe part, swift symbols carry the function name and labels, not the argument. where a memory file name actually rides in is an NSError from a failed read, userInfo has the full path and it lands in the exception text. one fixture that throws a real file-not-found on a fake memory file proves the scrubber on the path you'll hit.

---

> **AlternativeOk1991**（1 分） · 2026-10-28T10:02:37+08:00　
> That's the right place to look. What's there today: exception values go through the same redactor (/var/..., /Users/..., file:// paths and media file names become ), non-fatal reports send only domain, code and a message the developer wrote (never localizedDescription), and contexts outside a small allowlist are dropped, so userInfo shouldn't survive either. But the tests only feed in string patterns. A fixture that throws a real NSFileReadNoSuchFileError on a fake memory path and asserts the final event is clean is a much better test, so I'm adding exactly that. Thanks for the push.

---

> **QuanTradin**（1 分） · 2026-10-28T10:30:33+08:00　
> then the gap is the test input, not the redactor. one test that opens a missing file for real, catches the NSError and asserts on the serialized event instead of on the string you handed it, and the allowlist either holds or it doesn't. nothing to add past that, this is a good writeup.

---

> **AlternativeOk1991**（1 分） · 2026-10-28T10:51:56+08:00　
> Agreed, a real missing-file read asserted on the serialized event is the right test, so that's the one I'm adding. Thanks for pushing on this, it caught a real gap.

## 导航

- 项目页：[[10-项目/apps.apple.com_a3c5058a]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
