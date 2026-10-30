---
type: "corpus"
item_id: "94cfdc73cdf2098c"
title: "Show HN: Overtone – Transcribe, correct and cut captions for any screen shape"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50293115"
project_url: "https://github.com/lonthq/overtone-captions"
author: "rvanderlinden"
published_at: "2026-10-29T17:48:17Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_rvanderlinden
  - story_50293115
  - show_hn
metrics: {"points": 37, "comments": 2, "engagement_velocity": 37}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Overtone – Transcribe, correct and cut captions for any screen shape

> [!info] 一句话导读
> Hi HN, I'm Ruud, co-founder of Lont. We turn company emails into personalized videos.Video captions cost us manual work twice: fixing misheard words, then fixin…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50293115>
> 指标：点赞=37 · 评论=2 · engagement_velocity=37
> 作者：rvanderlinden　|　发布：2026-10-29T17:48:17Z
> 项目链接：<https://github.com/lonthq/overtone-captions>
> 采集：2026-10-30T09:46:09+08:00　|　id：`94cfdc73cdf2098c`

## 正文

Hi HN, I'm Ruud, co-founder of Lont. We turn company emails into personalized videos.Video captions cost us manual work twice: fixing misheard words, then fixing layout, like lines ending on “the”.Overtone uses multiple models to listen to the audio: gpt-transcribe, Azure STT, and Elevenlabs Scribe. When they return conflicting results, Overtone sends small clips to the models again, and then lets an LLM decide what was actually said.The LLM is like a human doing a sanity check on the transcription model. Humans would easily recognize a word to be different based on context. The LLM basically does the same, using an optional context prompt + its world knowledge. Because of this the Word Error Rate (WER) on many test files is lower when using Overtone, compared to just using a model without it.Sure, the cost is higher because we use up to 3 different STT models + an LLM, but it still removes mistakes, reducing the time needed to fix captions to a minimum, and reducing the chance you'll miss something. For us it's worth it. For ultra high volume use cases it may not be.The rules-based cutter nicely cuts the transcript into captions that look good, depending on screen size: 16:9 is different from 9:16, and the Overtone Format we created supports any type really. Pauses become breaks, captions are grouped per speaker, and names/numbers are never spread out over multiple captions.How to add these captions to your videos? A videojs plugin can do this automatically, so you don't burn in your captions. The plugin lets you cycle between styled captions, plain captions, and off. You can burn them into an MP4 file with overtone burn.Quickly try it out just the cutter? Try: npx overtone-captions recut yoursub.srt

Transcribing audio with API keys works too. Use --dry-run to show a cost estimate before you send.We open-sourced this first version (MIT) because we believe many people can benefit from this, especially if your captions just need to be good. There's plenty of room to improve though, so we've made it easy to help contribute to add style packs, languages, and providers/models.You can find a demo at: https://overtone.lont.ai/Find the code and benchmarks here: https://github.com/lonthq/overtone-captions

## 评论（2/2）

> **kulahan** · 2026-10-29T21:25:09.000Z　
> I have no idea what’s going on, but modern subtitles are suddenly TRASH. All kinds of misheard words, it really feels like they removed all human oversight, or reduced it so significantly it’s just impossible to actually read it all for whatever crew works on this.I only glanced through capabilities, so apologies if I simply missed this, but I am begging you to ensure there is some kind of system for translating foreign text on screen - most ideally, in a slightly differentiated font.So often someone is walking by a sign in some other language, and their comments on it are translated, but the sign is not! I just watched Sai on Netflix, and it changes to a bright red screen with white text near the end of most episodes. I think it’s introducing the credits but I have no idea. It was just 30 seconds of Japanese text.

---

> **rvanderlinden** · 2026-10-29T21:50:20.000Z　
> Misheard words is something that Overtone fixes. But it can't fix all, in some cases audio mix and pronunciation are so bad that it's genuinely hard even for a human in their native language to understand. Music also messes up speech-to-text models.Unfortunately translation of (on-screen) text wasn't built into Overtone. This is something both Netflix and Disney are very aware of, and they already create multiple visual versions of content. On both platforms you can trigger a different visual language version by changing your UI language. Disney movies are most known for this: https://www.youtube.com/watch?v=FxzL7UYyAegThey use the IMF format to transport content with "overlays" for different languages. In those languages certain frames are swapped out for a translated version. So that an EXIT sign is seamlessly translated to a SALIDA sign in Spanish for example.Simpler way to do this is forced narrative captions. They are basically a separate captions track to only translate stuff like the on-screen sign you mention. This is combined with regular captions. Netflix turns them on by default I believe, and on Apple TV+ it's called "auto" captions.The core problem is that AI isn't yet able to do everything. There's a race to the bottom going on for translation companies and things won't get better until AI gets better probably. Companies like Netflix and Disney still spend good money to get high-quality captions, but smaller ones don't unfortunately. Best thing for you to do might be to message the provider so they at least know that people are unhappy.

## 关联链接

- https://overtone.lont.ai/Find

## 导航

- 项目页：[[10-项目/github.com_645f5018]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
