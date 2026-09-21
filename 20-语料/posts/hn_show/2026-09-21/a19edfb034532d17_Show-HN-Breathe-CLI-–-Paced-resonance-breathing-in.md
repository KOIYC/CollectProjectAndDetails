---
type: "corpus"
item_id: "a19edfb034532d17"
title: "Show HN: Breathe CLI – Paced resonance breathing in the macOS terminal"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48340315"
project_url: "https://github.com/marekkowalczyk/breathe-cli"
author: "marekkowalczyk"
published_at: "2026-05-30T20:30:53Z"
captured_at: "2026-09-21T09:55:22+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_marekkowalczyk
  - story_48340315
  - show_hn
metrics: {"points": 132, "comments": 55, "engagement_velocity": 132}
comments_count: 54
comments_total: 55
discovered_via: "hn:show_hn:144d"
---

# Show HN: Breathe CLI – Paced resonance breathing in the macOS terminal

> [!info] 一句话导读
> I built a terminal app that paces slow breathing at 6 breaths per minute for vagal tone training. It's a single Python file, stdlib only, no dependencies — just…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48340315>
> 指标：点赞=132 · 评论=55 · engagement_velocity=132
> 作者：marekkowalczyk　|　发布：2026-05-30T20:30:53Z
> 项目链接：<https://github.com/marekkowalczyk/breathe-cli>
> 采集：2026-09-21T09:55:22+08:00　|　id：`a19edfb034532d17`

## 正文

I built a terminal app that paces slow breathing at 6 breaths per minute for vagal tone training. It's a single Python file, stdlib only, no dependencies — just run breathe and follow the bar.I'm a cardiology patient (HFrEF). Slow breathing at resonance frequency is one of the few non-pharmacological interventions shown to improve cardiac vagal tone and baroreflex sensitivity (Bernardi et al., Circulation 2002; Lancet 1998). I wanted a frictionless daily habit tool — no app store, no account, no subscription, just open terminal and go.Design constraints, all grounded in the clinical literature:- No breath retention — Valsalva risk in cardiac patients- No rapid breathing — minimum 8-second cycles- Exhale ≤ 2x inhale — no evidence for extreme ratios- Immediate exit, always — q or Ctrl+C restores the terminal even on crashThe README includes a resonance frequency measurement protocol for anyone with a chest-strap HRV monitor who wants to find their individual optimum instead of using the 6 bpm default.macOS only (uses afplay for audio cues). MIT licensed.pip install breathe-cliorbrew tap marekkowalczyk/breathe && brew install breathe.

## 评论（54/55）

> **chrisvenum** · 2026-05-31T08:02:26.000Z　
> Terminally breathing

---

> **iammjm** · 2026-05-31T09:07:21.000Z　
> Very nice. I have no heart issues but have been experimenting with extended breathing/longer exhales to calm down my sympathetic nervous system. I believe intentional breathing is a big, mostly underutilized tool all of us have to be generally more relaxed and healthier and also to calm ourselves down in stressful situations

---

> **darcien** · 2026-05-31T09:24:52.000Z　
> This reminds me of another HRV training from few years back shared here.- https://news.ycombinator.com/item?id=37538028- https://github.com/kieranabrennan/every-breath-you-take

---

> **skeledrew** · 2026-05-31T10:51:23.000Z　
> Looks interesting. And it's pure Python with no 3p packages. Pretty trivial to support other OSes: make that audio player invocation configurable.

---

> **mpeg** · 2026-05-31T12:24:08.000Z　
> This is cool, I have SVT and usually am able to stop an episode if I do slow breathing like that; although sometimes if that doesn’t work the modified reverse valsalva manoeuvre does it every time.

---

> **Ruslan1095** · 2026-05-31T12:29:34.000Z　
> Nice work on the zero-dependency approach. I'm building a similar tool for Windows (voice-to-text) and the "no account, just run" philosophy resonates — friction kills daily habits.

---

> **mistrial9** · 2026-05-31T12:54:37.000Z　
> this book is somewhat usefulhttps://archive.org/details/etaq_light-on-pranayama-b-k-s-iy...

---

> **mark_l_watson** · 2026-05-31T12:58:02.000Z　
> I love the zero dependency implementation. I do this style of breathing during specific time periods of practicing Qi Gong. I will try your script when I get to my laptop. Thanks.

---

> **samrivera** · 2026-05-31T14:30:11.000Z　
> 37 days into quitting smoking and breathing exercises have been a huge help for the craving spikes. a simple terminal tool for paced breathing actually makes a lot of sense - when the craving hits at 3pm and youre staring at a screen anyway, having it right there in the terminal is way less friction than pulling out a phone app. starred.

---

> **glaslong** · 2026-05-31T15:48:44.000Z　
> does it have modes for Hamon or Total Concentration breathing?

---

> **yong076** · 2026-05-31T16:39:06.000Z　
> wow this repo is peaceful

---

> **ahmazroot** · 2026-05-31T16:57:05.000Z　
> Not every project needs agents, workflows, and LLM integrations. Sometimes a focused tool is exactly what's needed.

---

> **thoughtpeddler** · 2026-05-31T19:02:54.000Z　
> Very cool project. Is this similar to the Apple Watch ‘mindful minutes’ breathing feature? I assume it’s based on the same research as is cited in this project’s repo?

---

> **leotryhard** · 2026-05-31T21:22:46.000Z　
> 0 deps + afplay combo is the right move for this. Was wondering why not AVAudioPlayer until I saw the cycle lengths, overkill for 8s tempo.

---

> **lavaman131** · 2026-05-31T21:34:37.000Z　
> This is nice. I like that it treats breathing like a small terminal ritual instead of turning it into a whole wellness app.

---

> **luckykiddie** · 2026-06-01T01:26:36.000Z　
> Just tries the 4-7-8 method days before. Why not support breathe holds?

---

> **mindhash** · 2026-06-01T05:13:20.000Z　
> Going to try this. I have a breathing clock gif as default page on my browser. I use it while I am passive in meetings.
> Resonant breathing has been great for me for IBS

---

> **ezez2** · 2026-06-01T06:59:04.000Z　
> This reminds me of this project: https://github.com/e6a5/zenta

---

> **ajithhyd** · 2026-06-01T10:01:09.000Z　
> Could add a pomodoro timer in the mix lol

---

> **rendx** · 2026-06-01T10:52:17.000Z　
> Interesting. I tried it for a bit over a minute (8 cycles), but then I had to stop. I get really dizzy unless I take breathing breaks after outbreaths. Will try again to see where this goes, thanks! Really like the simplicity.

---

> **radsj** · 2026-06-01T23:02:59.000Z　
> Awesome. While we are on this topic, here is something I built for myself while getting bored in zoom meetings (or even in-person meetings): https://avrhut.com/resonant-breathe-bar/Based on breathing pattern you set, and a dot in the menu bar shrinking or expanding. No telemetry or ads and completely free.

---

> **marekkowalczyk** · 2026-06-02T16:41:50.000Z　
> v1.9 is out — now works on Windows 11 too (contributed by @SHJordan in PR #3). pip install --upgrade breathe-cli to update.

---

> **marekkowalczyk** · 2026-05-31T19:25:07.000Z　
> Hah! Nice catch. I should have thought of this name myself.Try the app and share your feedback.

---

> **marekkowalczyk** · 2026-05-31T19:36:10.000Z　
> Good point. I can't see a reason not to regulate your nervous system. Give the app a try and share your feedback.

---

> **spieden** · 2026-05-31T17:49:04.000Z　
> I've been running this a bit with a Polar chest strap heart monitor. I'm thinking about forking it to add some audio cues so that I can have it running in the background while I work and try to keep my heart variability up. I find that I tense up when I'm intent on the work which leads to a lot of problems. I'm hoping having something like this app that uses audio cues for breathing but only comes on when my heart variability drops into the red could get me into a continuous state of low sympathetic nervous system activation while working, which is very much not the norm for me for historical reasons.The author of this tool eventually created a heart rate monitoring hardware product and an app to go with it to do HRV training. I think `every-breath-you-take` may have been an early prototype that he generously open sourced(?)

---

> **marekkowalczyk** · 2026-05-31T19:30:29.000Z　
> Indeed related! I don't have a Polar but the app looks nice; starred for future review / inspiration. Thank you.Try `breathe` and share your feedback!

---

> **marekkowalczyk** · 2026-05-31T19:16:40.000Z　
> Thank you for noticing. Yes, I will include other OSes in a future version; I just wanted to release ASAP after squashing some weird bugs.Give it a try and share your feedback.

---

> **marekkowalczyk** · 2026-05-31T19:35:25.000Z　
> I'm wondering if the protocols that I have included with the app could be helpful in your situation. I'm curious of your feedback on the app.

---

> **marekkowalczyk** · 2026-05-31T19:28:09.000Z　
> Looking at your comment and at other comments as well I think this approach is the new black, deservedly (is that even a word?). Try the app and share your feedback.

---

> **marekkowalczyk** · 2026-05-31T19:24:25.000Z　
> Thank you for sharing — downloaded. I'll comb it for relevant info for the next sprint. Meanwhile, try the app and share your feedback!

---

> **marekkowalczyk** · 2026-05-31T19:19:10.000Z　
> Thank you for noticing my effort. Do give it a try and please report your experience. I'm open to feedback.

---

> **Obscurity4340** · 2026-05-31T17:08:23.000Z　
> I've long wondered if a big unsung part of smoking is the way it gets normally high-strung, fast moving and shallow breathers to slow down and inhale deeply for 3-5 mins at a time. They might not get that kind of air any other way

---

> **marekkowalczyk** · 2026-05-31T19:14:47.000Z　
> I've never thought of this kind of a use case but I'm happy you see some value in trying out `breathe`. I'm curious of your feedback after you've worked with it for some time.

---

> **marekkowalczyk** · 2026-05-31T19:26:39.000Z　
> Not at this point. I developed it with the Market of One in mind — for myself. But I'm open to requests that will broaden the scope of modes for other users. I just don't want to invest time into speculative development. Try the app as-is and share your feedback.

---

> **marekkowalczyk** · 2026-05-31T19:25:21.000Z　
> What do you mean?

---

> **marekkowalczyk** · 2026-05-31T19:18:13.000Z　
> Exactly that kind of thinking was my idea for the app. A UNIX-like approach to solving a personal problem for the market of one :)I'm tired of accounts and subscriptions. Give it a try and share your feedback!

---

> **marekkowalczyk** · 2026-05-31T19:13:14.000Z　
> Thank you for your appreciation. I don't have an Apple Watch so it's hard to say. There isn't a ton of research on the subject — no Big Pharma sponsorship money in a breathing technique that you can't patent — so I suspect it's the same research.Give the app a try and share your feedback. Happy Breathing :)

---

> **marekkowalczyk** · 2026-06-01T20:21:01.000Z　
> Thank you for noticing my effort. I hope the app can help you. Would you like to share your experience here?

---

> **marekkowalczyk** · 2026-06-01T20:19:01.000Z　
> Thank you for noticing. You've really captured the idea of the app.

---

> **rippeltippel** · 2026-06-01T09:40:30.000Z　
> The readme says "This app deliberately does not support breath retention, rapid breathing, or any pattern not grounded in the slow-breathing clinical literature." Also links to relevant literature.

---

> **marekkowalczyk** · 2026-06-01T20:24:03.000Z　
> Thank you for asking. I've been building for a Market of One --- i.e. myself (heart failuer). Research shows breath holds are not recommended for my condition. Having said that, I realize this is not a universal guideline. I'm considering adding other modes besides heart failure-friendly ones. What are your use cases? Would you like to submit a feature request?

---

> **marekkowalczyk** · 2026-06-01T20:20:04.000Z　
> Thank you for your comment. I've never envisaged this kind of an application. Does it help you? Is there any research you can share or is it just anecdotal?

---

> **marekkowalczyk** · 2026-06-01T20:30:50.000Z　
> Thank you for bringing this to my attention. However the purpose here is medical for a Market of One (myself), not meditation. Give it a try and share your feedback.

---

> **marekkowalczyk** · 2026-06-01T20:28:31.000Z　
> Submit a Feature Request with a Why :)

---

> **rendx** · 2026-06-01T11:51:51.000Z　
> 11 cycles this time. Went a bit further into the dizziness, since I was more prepared for it this time. Unsure whether it makes sense to just stay with the dizziness as long as I can, or whether I should stop earlier. Probably either is fine as long as I am somewhat confident about it?

---

> **marekkowalczyk** · 2026-06-01T20:16:44.000Z　
> Thank you for sharing your experience. Try more shallow breathing rather than modifying the frequency/timing, which is the whole point of this approach :)

---

> **marekkowalczyk** · 2026-06-02T16:39:29.000Z　
> Looks nice! Thank you for sharing. It's nice to see that I'm not alone in my breatghing pursuits.I'm wondering if you tested my app. Care to share your feedback?

---

> **marekkowalczyk** · 2026-05-31T19:32:10.000Z　
> What you're referring to reminds me of the concept of Biofeedback.

---

> **marekkowalczyk** · 2026-05-31T19:34:06.000Z　
> In psychology there's the concept of Secondary Benefits — a behavior harmuful on the surface always has a Positive Intention behind it — otherwise an individual would not engage in it.

---

> **theshrike79** · 2026-06-04T10:22:30.000Z　
> A friend of mine managed to stop smoking with a wood cigarette.They just went wherever they normally went to smoke and took long breaths with the wood stick in their mouth.It was 90% about the ritual of going somewhere to just be, think, and breathe and 10% being addicted to nicotine.

---

> **marekkowalczyk** · 2026-06-01T20:27:54.000Z　
> This is true as I've created this app for a Market of One. Having said that, if there's sufficient interest I'm considering adding other breathing modes besides Heart-Failure-friendly ones. If interested, open a Feature Request.

---

> **marekkowalczyk** · 2026-06-01T20:18:07.000Z　
> Dizziness is certainly not the intended outcome; I don't get any. It's too much oxigen in your system. Ditto more shallow breathing.

---

> **spieden** · 2026-06-04T14:31:50.000Z　
> Yes, I think it's exactly this!

---

> **Obscurity4340** · 2026-06-04T02:09:41.000Z　
> For sure, I like Gabor Mate's focus also not necessarily on why the specific drug but why the hurt

## 导航

- 项目页：[[10-项目/github.com_181aa751]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
