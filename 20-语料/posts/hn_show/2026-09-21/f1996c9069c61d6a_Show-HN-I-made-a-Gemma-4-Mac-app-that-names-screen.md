---
type: "corpus"
item_id: "f1996c9069c61d6a"
title: "Show HN: I made a Gemma 4 Mac app that names screenshots with local AI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48342306"
project_url: "https://snapname.app/"
author: "joas_coder"
published_at: "2026-05-31T01:40:56Z"
captured_at: "2026-09-21T01:43:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - hn_show
  - author_joas_coder
  - story_48342306
  - show_hn
metrics: {"points": 7, "comments": 6, "engagement_velocity": 7}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:144d"
---

# Show HN: I made a Gemma 4 Mac app that names screenshots with local AI

> [!info] 一句话导读
> I made my first macOS utility app that ships with a bundled Gemma 4 model, specifically the Gemma E4B one. It made my app DMG have 5.3 GB in size, but I think i…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48342306>
> 指标：点赞=7 · 评论=6 · engagement_velocity=7
> 作者：joas_coder　|　发布：2026-05-31T01:40:56Z
> 项目链接：<https://snapname.app/>
> 采集：2026-09-21T01:43:07+08:00　|　id：`f1996c9069c61d6a`

## 正文

I made my first macOS utility app that ships with a bundled Gemma 4 model, specifically the Gemma E4B one. It made my app DMG have 5.3 GB in size, but I think it is a small size for the power that this free local model can provide.It runs fine on CPU, but can also run on Apple Silicon GPU, although I did not notice any performance improvements with GPU (tested on a M5 chip).I think these local lightweight and multimodal models will open multiple possibilities for new software tools where privacy is essential.

## 评论（6/6）

> **joas_coder** · 2026-05-31T01:42:58.000Z　
> For anyone who wants to see the workflow before downloading the large app bundle, here’s a short demo:
> https://www.youtube.com/watch?v=QIt2H_CUYBM

---

> **robgough** · 2026-05-31T02:48:11.000Z　
> As clever as this is, it seems like the names are fairly straightforward (as you'd want!) – did you try using the on-device Apple Foundation model at all? That's actually pretty powerful for a use case like this, and if you're happy to require the user has Apple Intelligence turned on already, your shipped app can end up being tiny. The biggest concern for an app like this is how much RAM you end up using trying to run it. Especially if we end up with lots of different apps all doing the same thing.Being able to super-power apps with on-device models is a lot of fun. I recently did the same building my own dictation app using small local models, and I still can't believe how effective it is. The download is just 20mb, though it will download parakeet ~475mb for audio, but can use the on-device model as the second-pass LLM and works pretty well (though better models are available to download and use e.g. Llama 3.2 4bit and Qwen 2.5 7B 4bit)I'm currently building a little tool for a professional photographer friend to go through and classify images in their photoshoots, so I can build a searchable db for them to quickly find very specific images in the future. I simply don't think it would have been possible for me to build a tool like that just a couple years ago at any price.

---

> **treelover** · 2026-05-31T05:19:52.000Z　
> Nice use of local AI!

---

> **joas_coder** · 2026-05-31T14:22:46.000Z　
> And a quick YouTube short video on how to put the app on auto-pilot so that you don't have to do anything to have your screenshots receive meaningful names: https://youtube.com/shorts/8bxhBgJvp7M

---

> **joas_coder** · 2026-05-31T11:23:22.000Z　
> Thanks for the feedback. I did not know my Mac had an on-device Apple Foundation model. Is it multimodal? I'll be checking it out and comparing it with Google Gemma 4. I thought Apple was out of the AI model race.The idea is to ship more powerful lightweight free models as they become available. I'm looking forward to Gemma 5!> The biggest concern for an app like this is how much RAM you end up using trying to run itYou are totally right. A new feature for a future version would be to turn off the model when the app is idle. And only launch it next time the user takes a screenshot. It is a trade-off between latency to generate the names and memory RAM.

---

> **robgough** · 2026-05-31T15:20:49.000Z　
> It's not as powerful as Gemma 4, but I think they likened it to GPT-3. It's perfectly capable of looking at images and classifying them at the level you'll need for this app. And it runs everything on the Apple Neural engines, so decently quick. Of course, this assumes that your users are using Apple Silicon processors, I believe that's the limitation – and they must have enabled Apple Intelligence which downloads the model at that point.

## 导航

- 项目页：[[10-项目/snapname.app_8296a2d0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
