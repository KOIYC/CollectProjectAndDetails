---
type: "corpus"
item_id: "6230eed53cd86fa4"
title: "Show HN: Forwarder.cc – Static-site forms sent to your inbox, pay per message"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50108386"
project_url: "https://forwarder.cc/"
author: "calyhre"
published_at: "2026-10-15T18:47:47Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_calyhre
  - story_50108386
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Forwarder.cc – Static-site forms sent to your inbox, pay per message

> [!info] 一句话导读
> TL;DR: 12 years ago I built a service that forwards simple HTML forms to an email address. I've been procrastinating on finishing it ever since, until today. Yo…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50108386>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：calyhre　|　发布：2026-10-15T18:47:47Z
> 项目链接：<https://forwarder.cc/>
> 采集：2026-10-16T09:35:18+08:00　|　id：`6230eed53cd86fa4`

## 正文

TL;DR: 12 years ago I built a service that forwards simple HTML forms to an email address. I've been procrastinating on finishing it ever since, until today. You point your form at it and every submission lands in your inbox. It runs on credits, 1 credit = 1 message, no subscription. Perfect for static websites.—Hey folks, back around 2014, alongside my job as a software engineer, I was building a lot of static websites for my own clients, mostly small businesses that just wanted a simple site. To avoid headaches, I went fully static, often hosted on GitHub Pages and similar.But most clients also wanted a contact form, and a form needs a server running somewhere. I had my own weekend-hacked service for this, which literally just forwarded the form to the client's email.I didn't invent anything here: one service I particularly remember was FormKeep by thoughtbot, that I really liked.So I started building my own, mostly because I loved losing myself in side projects like this, and also because I was a cheap ass and thought I could do something similar for less, and without a subscription.By 2016 I had done about 90% of what I'm showing you today. I called it "The Great Forwarder". Everything was ready: backend, frontend, hosting, Stripe, landing page. I even had a designer friend help with the design (sorry, Valentin, if I've botched it since). Then I started another project, which took off right away and took all my attention for a while. Fun fact: that project has been using this service ever since, and almost every message ever sent through it came from there.So for years, I kept Forwarder.cc up to date, upgrading libraries and trying new ones: axios, got, Redux, Zustand, create-react-app, webpack, Vite… It became my laboratory for everything I wanted to explore, while always staying up and maintained (again, for my own use only).The only thing that ever held me back from launching it was a missing help center, and, more honestly, the fear of putting it in front of people.So today's the day: after 12 years of procrastination, I finally finished the help center.I know there are a ton of similar services nowadays, but anyway, what do you think of that help center?

## 导航

- 项目页：[[10-项目/forwarder.cc_29252c6c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
