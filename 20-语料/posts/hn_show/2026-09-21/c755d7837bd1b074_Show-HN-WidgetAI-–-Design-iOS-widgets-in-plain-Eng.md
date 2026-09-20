---
type: "corpus"
item_id: "c755d7837bd1b074"
title: "Show HN: WidgetAI – Design iOS widgets in plain English, no Xcode"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48729514"
project_url: "https://getwidgetai.com/"
author: "bring-shrubbery"
published_at: "2026-06-30T07:21:58Z"
captured_at: "2026-09-21T01:45:17+08:00"
lang: "en"
kind: "post"
topic: "移动 App"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_bring-shrubbery
  - story_48729514
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:113d"
---

# Show HN: WidgetAI – Design iOS widgets in plain English, no Xcode

> [!info] 一句话导读
> Making a custom iOS widget normally means Xcode and WidgetKit. WidgetAI lets you just describe one in chat ("battery as a heatmap grid"), tweak it in plain lang…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48729514>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：bring-shrubbery　|　发布：2026-06-30T07:21:58Z
> 项目链接：<https://getwidgetai.com/>
> 采集：2026-09-21T01:45:17+08:00　|　id：`c755d7837bd1b074`

## 正文

Making a custom iOS widget normally means Xcode and WidgetKit. WidgetAI lets you just describe one in chat ("battery as a heatmap grid"), tweak it in plain language, and ship it to your home screen.Live on the App Store now (iPhone/iPad; Android on the way). Would love feedback on what widgets you'd actually want on your home screen.

## 评论（2/2）

> **jorisw** · 2026-06-30T08:18:47.000Z　
> Feel like having 'AI' in any product name won't age well, as AI will soon be (if it not already is) implied as part of any software product.Kind of like saying "check my mobile website", "make me a responsive web design", or "order your food online". Everything is already mobile, responsive, online.The fact that AI enables you to offer the functionality, doesn't mean it needs mentioning. 'AI' may already have negative connotations in the target audience of your app, as it currently does with many consumers.Some more feedback:- Needed to follow the link on your website to the App Store. A search didn't reveal it.- Sign in screen says Welcome Back though it's the first time installing- What do I actually need to sign for?- The on boarding lets me choose from 3 random objectives. I don't need a weather widget, daily motivation widget, or whatever the third option was. I was expecting the area above the 3 buttons to be a text input field. Being limited to these 3, I'm dropping out of using this app. This also betrays the tagline "Tell WidgetAI what you want".- If I were to use a widget maker, I'd want to do it from my Mac, as I'd be looking to create an API client to my broker for more accurate market updates than what the (strangely best in class) Yahoo Finance widget offers me. Boring use case, I know, but basically any API client type use case would interest me, as many apps fail to ship with widgets of their own.

---

> **bring-shrubbery** · 2026-06-30T14:30:34.000Z　
> Thanks for feedback! I'll fix most of these issues.The mac version is available btw, it's actually better than iOS one :D I'll add a link to it on the website, but you can actually just find it on AppStore.Regarding sign in - the LLM that composes widgets is running on the server side, so we need accounts for attribution and rate-limiting. The widget layout is stored on the server side on your account too. No personal data is stored btw, they are just bindings, so if you say "my location" it just stores a binding to "currentLocation".We do have ability to add custom API btw, I'll write up a guide for how to do that. That's kinda how the Claude uptime widget template works.EDIT: Also if there are any public APIs that you'd have in mind, let me know and I'll add them to work out of the box!

## 导航

- 项目页：[[10-项目/getwidgetai.com_47a4ddf8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`移动 App`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
