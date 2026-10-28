---
type: "corpus"
item_id: "257ee7043d31f170"
title: "Your DEV posts have a beautiful new share card ✨"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/devteam/your-dev-posts-have-a-beautiful-new-share-card-4be8"
project_url: "https://github.com/forem/forem/pull/19826"
author: "Jess Lee"
published_at: "2026-10-27T16:44:29Z"
captured_at: "2026-10-28T09:44:18+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - devto
  - devto
  - showdev
  - opensource
  - design
metrics: {"reactions": 53, "comments": 9, "reading_time": 2}
comments_count: 9
comments_total: 9
discovered_via: "devto:showdev"
---

# Your DEV posts have a beautiful new share card ✨

> [!info] 一句话导读
> The image that shows up when you share a DEV post just got a brand-new look!

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/devteam/your-dev-posts-have-a-beautiful-new-share-card-4be8>
> 指标：reactions=53 · 评论=9 · reading_time=2
> 作者：Jess Lee　|　发布：2026-10-27T16:44:29Z
> 项目链接：<https://github.com/forem/forem/pull/19826>
> 采集：2026-10-28T09:44:18+08:00　|　id：`257ee7043d31f170`

## 正文

The image that shows up when you share a DEV post just got a brand-new look!

I got to work on [forem/forem#24071](https://github.com/forem/forem/pull/24071) last week and I'm so excited to see it live in production:

{% github https://github.com/forem/forem/pull/24071 %}

## Meet the new card

![before and after](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ntvzj7cvzioc0ipgrkju.png)

Every post now gets a quote card. It pulls the opening of your post and sets it inside a little browser-window frame over a gradient. Below that sits your profile pic, name, publish date, and reading time.

Most places that unfurl a link already show its title, so I wanted to remove the redundancy. It shows the first lines of your post instead. That's where your voice is, and now it's the first thing people see when your post is shared!

Color comes from your profile's brand color if you've set one. If not, the card uses one of our four palettes, so a page full of shared posts feels varied and bright.

## One image, everywhere

There's one image, and it unfurls anywhere your link gets shared. It's sized with roomy top and bottom margins, so even when a platform (ahem, X) lays its own label over the image, your name and details stay clear.

## A few extra touches

While we were in there, we polished a few more things:

- Names with `@` or `%` display cleanly, without stray backslashes.
- Names in stylized Unicode (𝓯𝓪𝓷𝓬𝔂 𝓽𝓮𝔁𝓽 like this) render properly.
- The image refreshes when your reading time or opening quote changes, so it stays current after you edit.

Thank you to [Ben](https://dev.to/ben) for the review and merge!

## A little history

Back in 2018, Ben wrote about how DEV generated social images in the first place:

{% link https://dev.to/ben/how-devto-dynamically-generates-social-images--2c2n %}

In August 2023, Ben moved generation in-house with ImageMagick ([#19949](https://github.com/forem/forem/pull/19826)). It was a great cost savings to host every post's card ourselves, on our own infrastructure, instead of handing it to a third-party service. Everything in this redesign builds on that foundation.

## Go see yours

Share one of your posts (without a cover image) and take a look at your new card. Tag us ([@thepracticaldev](https://x.com/thepracticaldev)) or me ([@jessleenyc](https://x.com/jessleenyc)) on X so I can admire it. If anything looks off, like a name that renders strangely or a quote that cuts off in a weird spot, let me know in the comments!

## 评论（9/9）

> **Jess Lee** · 2026-10-27T16:48:46Z　
> 😐😐😐😐😐😐

---

> **Jess Lee** · 2026-10-27T16:53:58Z　
> 😀😀😀😀😀😀

---

> **Giorgi Kobaidze** · 2026-10-27T16:55:19Z　
> I love this! Great job, team!

---

> **FrancisTRᴅᴇᴠ** · 2026-10-27T17:02:57Z　
> So pretty card displays!

---

> **nyaomaru** · 2026-10-27T17:07:08Z　
> This is such a nice improvement! 😸✨
>
> The new share card looks much cleaner, and showing the opening lines instead of repeating the title makes a lot of sense.
>
> I really like this update! 😸

---

> **𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 ** · 2026-10-27T18:02:31Z　
> Awesome 🥰

---

> **Odinaka Robert Nnamani** · 2026-10-27T18:07:46Z　
> Quoting the opening line instead of repeating the title is a nice touch. The byline getting covered was an odd bug to ship with.

---

> **Thomas Bonnet** · 2026-10-27T20:32:42Z　
> oooh that super fresh, awesome!

---

> **Emily Woods** · 2026-10-27T21:09:43Z　
> The quote selection rules are the part I'd keep beside the visual examples. An intro that starts with inline code or a link would make an interesting fixture: I'd want the card to read naturally after formatting disappears, while still attributing only my own words. Could the editor eventually show the selected excerpt before I share? That would make awkward cuts easier to catch.

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ntvzj7cvzioc0ipgrkju.png
- https://dev.to/ben
- https://dev.to/ben/how-devto-dynamically-generates-social-images--2c2n
- https://github.com/forem/forem/pull/24071
- https://x.com/jessleenyc
- https://x.com/thepracticaldev

## 导航

- 项目页：[[10-项目/github.com_069d229a]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
