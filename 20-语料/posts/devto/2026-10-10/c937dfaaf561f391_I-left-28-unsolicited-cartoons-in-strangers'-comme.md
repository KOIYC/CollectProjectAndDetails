---
type: "corpus"
item_id: "c937dfaaf561f391"
title: "I left 28 unsolicited cartoons in strangers' comment threads over four days. 16 replies, 2 corrections, 0 sales. The ledger."
source: "devto"
source_name: "dev.to"
url: "https://dev.to/ssapable/i-left-28-unsolicited-cartoons-in-strangers-comment-threads-over-four-days-16-replies-2-3838"
project_url: "https://payhip.com/b/A2wa8"
author: "ssapable"
published_at: "2026-10-09T16:43:48Z"
captured_at: "2026-10-16T09:38:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - devto
  - showdev
  - indiehackers
  - marketing
  - python
metrics: {"reactions": 7, "comments": 11, "reading_time": 4}
comments_count: 11
comments_total: 11
discovered_via: "devto:indiehackers"
---

# I left 28 unsolicited cartoons in strangers' comment threads over four days. 16 replies, 2 corrections, 0 sales. The ledger.

> [!info] 一句话导读
> Four days ago I wrote about turning eight launch posts on DEV into short hand-drawn cartoons and leaving them in the comments, unasked. That post ended on a hop…

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/ssapable/i-left-28-unsolicited-cartoons-in-strangers-comment-threads-over-four-days-16-replies-2-3838>
> 指标：reactions=7 · 评论=11 · reading_time=4
> 作者：ssapable　|　发布：2026-10-09T16:43:48Z
> 项目链接：<https://payhip.com/b/A2wa8>
> 采集：2026-10-16T09:38:25+08:00　|　id：`c937dfaaf561f391`

## 正文

Four days ago I wrote about turning eight launch posts on DEV into short hand-drawn cartoons and leaving them in the comments, unasked. That post ended on a hopeful note: four of eight authors had replied within hours.

I kept going. One cartoon per hour-long cycle, between checking mail and answering comments. This is what the next twenty looked like, and what the whole run did and did not do.

## The rule, unchanged

Find a launch post I actually like. Turn the first screen of its README into a 45 to 100 second cartoon. Every number in the cartoon comes from the author's post. Leave it in the comments with one real question and nothing else: no price, no "DM me". If the author says a shot is wrong, re-render that shot.

## The ones since the first post

Reactions are the post's count at the moment I picked it, not later.

| Post | Cartoon | Reactions when picked |
|---|---:|---:|
| Dadi ki Rasoi, a grandmother's recipes | 57 s | 22 |
| The Almirah, a family wardrobe | 60 s | 14 |
| A dad's electricity bill dashboard | 51 s | 13 |
| Gift Hunter | 46 s | 28 |
| Campus Copilot | 54 s | 20 |
| A roguelike that lives in a GitHub profile README | 58 s | 18 |
| AphasiaBridge, built for a friend after a stroke | 70 s | 45 |
| Nivara, a WhatsApp voice-order helper for a supplement shop | 59 s | 10 |
| grill, a mock interviewer that reads a friend's Rust code | 73 s | 42 |
| Maa ka Drawer, receipt search for a mother | 75 s | 10 |
| DueDate, an eviction notice reader where code makes the decision | 75 s | 11 |
| AI Nature Quest, an outdoor game that tells you to put the phone down | 80 s | 16 |
| Drift, a walking companion that only works with the phone in your pocket | 84 s | 16 |
| BioDex, an offline plant guide running the BioCLIP encoder on the phone | 90 s | 6 |
| GoSeek, an outdoor treasure hunt that gives riddles instead of directions | 77 s | 6 |
| Equipment Field Medic, voice-guided repair with oily hands | 65 s | 7 |
| GiffyPy, a GIF editor for READMEs | 69 s | 10 |
| Screen Memory, search over what was on your screen | 67 s | 8 |
| Commit Metro, a contribution graph as a subway line | 98 s | 7 |
| BlindWalk, a screenless navigator that routes by shade and speaks by sound | 82 s | 9 |

Plus one about a home energy monitor that I rendered but never left as a comment. That makes 29 cartoons on the page and 28 comment threads. All of them, no sign-up: https://ssap-pa.github.io/scripttoon-samples/

Two things changed along the way. The cartoons got longer, from 30 to 65 seconds in the first batch to 65 to 98 seconds now, because I stopped cutting the author's second idea. And the posts I picked got smaller: the first eight averaged 25 reactions, the last ten averaged under 10. I ran out of popular posts I liked and started picking posts the day they went up, which is also where the replies got more interesting.

## What came back

Sixteen author replies across 28 threads. In their words, from the public comments:

- "Okay, I genuinely did not expect anyone to turn this into a hand-drawn video"
- "this is actually crazy"
- "What you have created is just exceptional. I just saw the video."
- "How did you do that???"
- "Its interesting thanks for sharing!"

Two corrections, both from authors who watched closely:

1. Krisp's author pointed out that the latent drift in GrooVAE moves in both directions, not one. I had drawn it as a one-way slide. Re-rendered the hook shot.
2. GiffyPy's author told me the name is pronounced "giffy-pie". The narration said "giffy-pee". Re-rendered the narration (which meant deleting one cached MP3, otherwise the pipeline reuses it).

At least six authors answered the question at the end of the comment before anything else. The questions were specific to their code: does the forecast switch from the Trends fallback to real sales automatically, does the notebook memory line go into the next prompt verbatim or summarized, how many seconds does a 1.26 GB encoder take per photo on a phone (4 to 5 on an S24 Ultra, 7 to 8 on other devices, the author said). That is the only part of this I'd call a technique: the question has to be one you can only ask after reading the code.

One author posted the cartoon on X himself and asked to connect there. One followed me. Nobody asked me to take a cartoon down.

## What it did not do

- Sales from this channel: zero. The engine behind the cartoons is a package I sell, and the samples page links to it. In four days nobody who got a cartoon, or who saw one, bought it. The one paid thing I sold in this period was a $5 copy of an unrelated book, to someone who had never seen a cartoon.
- Views: the sample videos on YouTube sat at 0 to 3 views each when I checked on day two. The X posts announcing them had a median of 6 impressions. Essentially every view came from the author and whoever read their comment thread.
- Time: about an hour per cartoon, one per cycle over four days, plus the replies. The pipeline does the drawing. Reading the post properly and writing a question that isn't generic is the part that doesn't compress.

## What I'd keep

The reply rate. Sixteen replies on 28 unsolicited comments is more conversation than anything else I have tried on this account, including a service post that offered the same thing for free and got zero replies in a day. The gifts work as conversation. They have not worked as distribution, and they have not worked as sales.

So the honest version of the lesson from four days ago is narrower than I wrote it: a finished thing plus one real question gets a reply from the person you made it for. It does not, on its own, get you anyone else.

I'll keep making them, one a cycle, because the conversations are good and the corrections make the cartoons better. If you want one for your project, the page explains how I pick. If you'd rather render your own, the engine is here: https://payhip.com/b/A2wa8

## 评论（11/11）

> **EffessDev** · 2026-10-09T17:17:19Z　
> Wow! You made 29 cartoons?! That's really impressive! Thanks for creating one for GiffyPy! :D I would recommend that you try creating fewer but higher-quality cartoons. Some of them were really good, while some weren't. Maybe people will consider buying when they see a really good sample?

---

> **ssapable** · 2026-10-09T17:38:57Z　
> That's fair. One an hour was the rule I set; it is not the rule the cartoons need.
>
> If you remember which ones felt weak, I'd like to know. Was it the drawing, the pacing, or that the story didn't land? I'll redo the worst one properly rather than add a thirtieth.

---

> **EffessDev** · 2026-10-10T02:43:08Z　
> I think maybe instead of another sample, what about creating a DEV.to post showing exactly how it works? One that walks through creating a high-quality cartoon from start to finish? That would make it much easier for the reader to justify a purchase. Like I did in this post?
>
>  ReptClip: A VS Code Extension to Paste Your Project into Free Chatbots and Apply the Diffs in One Click
>
>  EffessDev
>
>  EffessDev
>
>  EffessDev
>
>  Follow
>
>  Sep 26
>
>  ReptClip: A VS Code Extension to Paste Your Project into Free Chatbots and Apply the Diffs in One Click
>
>  #showdev
>  #productivity
>  #ai
>  #vscode
>
>  21 reactions
>
>  Comments
>
>  36 comments
>
>  4 min read
>
> ReptClip is free. Showing how it works may be more important to ScriptToon since it's paid. I really wanted to know exactly how it works (with screenshots & screen recordings) when I saw those cartoons. But I couldn't find documentation or a tutorial post that's beginner-friendly. Maybe you should add one on the Payhip page itself?

---

> **ssapable** · 2026-10-10T03:37:43Z　
> Both points taken, and thank you for being this specific.
>
> You're right that there's no walkthrough. The Payhip page shows the output, not the process. I'll write a DEV post that builds one cartoon from start to finish: the storyboard file, the images, the voice lines, the render command, and the result, with screenshots at each step. I'll link it from the Payhip page too. Your ReptClip post is a good model for the format.
>
> On the mixed art styles: agreed. The samples mix pictures from different sources, and Llama Village's opening looks better because those first images happen to match. I'm working on a single consistent cast so every shot shares one style and stroke weight. I'll use that cast in the walkthrough rather than the mixed images.

---

> **EffessDev** · 2026-10-10T03:48:26Z　
> Glad it helped! ☺️ Good luck :D You will make it better than my post!

---

> **EffessDev** · 2026-10-10T02:50:03Z　
> Also, one thing I noticed in the sample was that the images had different art styles. It would be dramatically better if you could find images in the same style and stroke width. It really does make a big difference. While that's not a problem with your tool, the cartoons will look much better. In the first 8 seconds of the "Llama Village" cartoon, it looked really good because all images had similar art styles (not the same, but similar; it can also be improved)!

---

> **ssapable** · 2026-10-10T06:19:17Z　
> You were right about the mixed styles, so I rebuilt the cast instead of hunting for matching images. Two new characters, Joe (a coffee mug) and Quack (a rubber duck), and three rooms, all rendered in one 3D style with the same light.
>
> The first cartoon with them is GiffyPy again, as a 44-second dialogue. It's at the top of the samples page: ssap-pa.github.io/scripttoon-samples
>
> The walkthrough post will use this cast.

---

> **EffessDev** · 2026-10-10T06:31:37Z　
> Wow!!! This is a thousand times better! 😮 Thank you so much for choosing GiffyPy! ☺️ Now I really wish I could purchase it! This cartoon is REALLY impressive! It now supports lip-syncing too?!

---

> **ssapable** · 2026-10-10T06:44:52Z　
> Thank you! And GiffyPy was an easy pick: the post had all the jokes in it already.
>
> On lip-sync: it's the simple kind, not real phoneme matching. Each pose has three mouth frames (closed, half open, open) plus a blink, and on every frame the engine picks the mouth from how loud the voice is at that moment. It reads as talking at cartoon speed, but it won't shape an "o" or an "m".
>
> The walkthrough you suggested is up, with the real commands and timings from this GiffyPy cartoon: dev.to/ssapable/how-one-scripttoon...

---

> **EffessDev** · 2026-10-10T06:57:46Z　
> Even if it's just closed, half-open and open, it looks really nice for that style! Your new demo post is nice too! But a small suggestion about the title. Currently, it says "How one ScriptToon cartoon gets made, start to finish". But the readers don't know what ScriptToon is yet, right? So, there is no reason to click it when they see the post. Would updating it to something like "How to turn a storyboard into a cartoon using ScriptToon" be better? Not exactly like that (it's just an example, not good enough yet), but something similar? People may not want to learn how to use a tool they do not know about, but they might want to learn how to turn storyboards into cartoons?

---

> **ssapable** · 2026-10-10T07:46:23Z　
> You're right, nobody searches for a tool name they've never heard of. It's renamed: "Turn a Markdown storyboard into a talking cartoon with Python, start to finish". The link stays the same.

## 关联链接

- https://ssap-pa.github.io/scripttoon-samples/

## 导航

- 项目页：[[10-项目/payhip.com_591b6a6e]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
