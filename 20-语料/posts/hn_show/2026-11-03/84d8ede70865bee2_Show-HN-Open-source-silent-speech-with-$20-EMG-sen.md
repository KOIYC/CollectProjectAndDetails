---
type: "corpus"
item_id: "84d8ede70865bee2"
title: "Show HN: Open-source silent speech with $20 EMG sensors and a webcam"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50340631"
project_url: "https://github.com/thaimtl/Silent-Voice"
author: "gottaguo"
published_at: "2026-11-02T17:48:03Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_gottaguo
  - story_50340631
  - show_hn
metrics: {"points": 4, "comments": 5, "engagement_velocity": 4}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:3d"
---

# Show HN: Open-source silent speech with $20 EMG sensors and a webcam

> [!info] 一句话导读
> Show HN: Open-source silent speech with $20 EMG sensors and a webcam

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50340631>
> 指标：点赞=4 · 评论=5 · engagement_velocity=4
> 作者：gottaguo　|　发布：2026-11-02T17:48:03Z
> 项目链接：<https://github.com/thaimtl/Silent-Voice>
> 采集：2026-11-03T09:40:36+08:00　|　id：`84d8ede70865bee2`

## 正文

Show HN: Open-source silent speech with $20 EMG sensors and a webcam

## 评论（5/5）

> **gottaguo** · 2026-11-02T17:48:03.000Z　
> Hi HN, Frank here. We placed second overall at Cal Hacks 13.0 (700+ projects), four of us from McGill.Over 200,000 people are diagnosed with throat cancer each year, and for many, the surgery removes their voice box. More than half a million people are already living without one.Their lips, tongue and jaw still move in the same way, but with nothing there to create any sound, they lose the ability to speak forever.In 36 hours we built Silent Voice to give them their voice back.With four different AI systems working together, Austin held a full phone call without making a sound, and the caller heard him in his own voice.• Muscles: we built a sensor rig using four surface EMG pads ($20 each) to measure the electrical activity in his face 1,000 times a second, and used a neural network (SVR-1) we'd trained to infer the movement of his tongue and jaw (which a camera can't see)• Lips: Auto-AVSR is a lip-reading technique which only works on complete video. We rebuilt it to work in real-time, re-reading Austin's sentence 10 times a second• Face: computer vision tracks his expressions and carries his emotion through the voice• Context: Claude uses both sides of the conversation to predict what Austin may say, and compensates for common confusions such as 'bills' and 'pills'SVR-1 is ~45M params, 12 transformer layers on top of 3 conv blocks, pretrained on Berkeley's 19h silent speech set then fine tuned on ~70 min of Austin. With only our 4 pads it picks the right sentence out of 10 lip look-alikes 72.3% of the time, Berkeley's released model gets 27.7% (theirs was trained on 8 pads though).I led the voice pipeline. Standard techniques rely on complete input, but we were only receiving individual words as Austin formed them. Waiting for a complete sentence meant callers were subjected to 4.9 seconds of dead air, whilst sending single words sounded like a robot reading a list.So I re-engineered the entire streaming layer into Cartesia, delivering complete (though brief) phrases in step with Austin's natural pauses, and cut the silence added by the model after each phrase (around half a second) down to a more natural (i.e. human) breath. His expression can also shift the emotion mid-sentence.As a result, callers were hearing Austin 0.6 seconds after his lips began to move, in real-time.It's a prototype, Austin is healthy and no patients have tried it yet. Code is open source, the demo is on the Devpost: https://devpost.com/software/silent-voice-s1f74pIf you've had (or know someone who's had) a laryngectomy, or work with them as a speech therapist, I'd love to hear from you.

---

> **drop_star** · 2026-11-02T18:02:27.000Z　
> very cool

---

> **thaifrommtl** · 2026-11-02T18:55:12.000Z　
> so proud we had achieved this in 36 hours!! i hear YC has a startup that does something kinda similar too

---

> **austinkomachi** · 2026-11-02T19:33:50.000Z　
> It was amazing working with you Frank. So incredibly happy that we took home the big W.

---

> **gottaguo** · 2026-11-02T18:38:10.000Z　
> thanks! the part i'm proudest of is the voice latency, we went from 4.9s of dead air to 0.6s. happy to go into how if anyone's curious

## 导航

- 项目页：[[10-项目/github.com_703344b0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
