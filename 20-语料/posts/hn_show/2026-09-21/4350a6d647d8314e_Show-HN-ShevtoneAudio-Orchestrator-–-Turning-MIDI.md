---
type: "corpus"
item_id: "4350a6d647d8314e"
title: "Show HN: ShevtoneAudio Orchestrator – Turning MIDI into Full Orchestration"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49497791"
project_url: "https://orchestra.shevtoneaudio.com/"
author: "MusicAlexandrov"
published_at: "2026-08-30T11:36:46Z"
captured_at: "2026-09-21T02:57:27+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_MusicAlexandrov
  - story_49497791
  - show_hn
metrics: {"points": 6, "comments": 4, "engagement_velocity": 6}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:52d"
---

# Show HN: ShevtoneAudio Orchestrator – Turning MIDI into Full Orchestration

> [!info] 一句话导读
> I'm Bor Shev, a composer and developer. Over the past two years I've been developing ShevtoneAudio Orchestrator.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49497791>
> 指标：点赞=6 · 评论=4 · engagement_velocity=6
> 作者：MusicAlexandrov　|　发布：2026-08-30T11:36:46Z
> 项目链接：<https://orchestra.shevtoneaudio.com/>
> 采集：2026-09-21T02:57:27+08:00　|　id：`4350a6d647d8314e`

## 正文

Hi HN,
I'm Bor Shev, a composer and developer. Over the past two years I've been developing ShevtoneAudio Orchestrator.
The idea is simple: instead of generating a finished piece of music and replacing the composer, Orchestrator takes the composer's own MIDI and develops it into a full orchestration.
It analyzes the musical material — harmony, melody, rhythm, dynamics, structure and orchestral density — and creates an arrangement across strings, brass, percussion and other sections.
The important part is that the result remains editable MIDI. The composer keeps control and can continue working with everything inside their DAW.
I believe this approach could be a breakthrough in AI-assisted composition: AI as an orchestration tool rather than a replacement for the musician.
I'm especially interested in feedback from developers, composers and people working with music technology. Feel free to tear the idea apart — I'd genuinely like to know what you think.
I'm also running a limited launch offer for Orchestrator at $149.
Demo / product:
orchestra.shevtoneaudio.com
Thanks for taking a look!
— Bor Shev
ShevtoneAudio

## 评论（4/4）

> **Rochus** · 2026-08-30T12:07:24.000Z　
> Looks interesting. But I couldn't find any practical examples or tutorials so far. Any hints? Is there a description somewhere how it is implemented, i.e. what technical concepts are used to analyze the Midi, understand the music well enough, and then invent a credible orchestration?

---

> **munch-o-man** · 2026-08-31T06:33:15.000Z　
> no offense, because I'm very interested in learning more about this since I am a software engineer who's degree is from a music conservatory and has nothing to do with software. BUT....nobody knows who you are or what this does, literally nobody is going to pay you money for an ambiguous black box that theoretically knows how to do music arrangements (how do we know it even does that? What logic does it use for arrangements? Are different orchestral/symphonic instruments correctly gated on their performance range and limitation of execution? How does it handle harmony? What do I get back? 4 part harmony? Is it going to sound like Johann Fux species counterpoint or is it capable of non-rule-based harmonic decisions? Is it going to just shit out stupid atonal shit that isn't creative or useful and only survives because it is "supposed" to sound like shit? When in reality Schoenberg and Berg could get away with it, most composers can't. Does it understand diads, triads, and extended harmony (7th, 9th, 11th, 13th chords and why you would notate one as such)....and since I always check this on music software (and it is almost 100% always wrong) and can't since you didn't share code here....does this shit understand enharmonic equivalents and why a c#m chord is spelled c# e g# and why even though it sounds the same it would be stunningly wrong to write it as db e ab?Am I wrong is thinking that what you are creating is essentially a way to hand the computer a leadsheet and get back a complete notated arrangement for a given set of instruments?If I am reading your description correctly, this honestly has very little to do with midi and is entirely a project about doing arrangements of an input piece and it starting and getting rendered back out as midi is irrelevant. You advertise doing harmonic analysis and without being able to see the rules/logic you use to accomplish that I can't really say if this is useful....it could be anything from some crap that makes everything a I IV V church-song progression to doing schenkerian analysis of the harmonies, progressions, and larger over-arching tonal progression. Nobody is going to pay you $150 for software that they can't even verify how it works when you are dealing with such a niche target audience (assuming you mean actual composers and not just minor arpeggios with the harpsichord effect and a drum beat lol.Just so people reading this can get a better idea of what you are trying to advertise sell....what happens if I give it one hand of a simple Bach invention? What if I hack through a chord-melody version of 'Yesterdays' by Jerome Kern? Can it orchestrate me a big band version based on my right hand hacking out the melody and my left hand hacking out the i-ii-V-i and II-V-I cycles?I apologize for being a bit harsh and hitting on a lot of shit....but when people post a webpage front for a blackbox application with a signup and payment plan and don't even share the code I assume they aren't in it for the 'hacking' and the 'show' and more in it for the 'pay me' and the 'now' and that the software will generally be shit.but in all seriousness, if you say something as complex as that it analyzes harmony and harmonic structure and then orchestrates/scores it you need to give proof of how and what rules it is using and how I can explain to it that I want it to sound like baroque 4th species counterpoint or I want it to sound like (mostly ewww) 12 tone music like schoenberg, or if I want it orchestrated in a Classical/Romantic period style (even that is generous as if they are the same and Brahms and Chopin and Haydn sound the same)or perhaps a jazz style.......point being, you provided no code, no breakdown of how something as complicated as harmonic arrangement and orchestration (both harmonic and instrumental) is implemented and what sort of results one should expect.If it is just a fun project then that is totally fucking awesome and I'd love to see it and help if I could...but then you shouldn't be hiding the code and thinking somebody is going to pay you $150 which is absolutely not going to happen for a black box claiming to do something more complex than I think most people here understand.As somebody with a very high level education in music who has been doing software engineering for almost two decades and has thought about shit like this at great length.....I doubt you have created something useful to a real musician....if I am wrong, which I would love to be....then please tell me you have gotten actually trained musicians that are professionals (your friend that is 'really good at guitar' but can't read music and has never played publicly with other musicians doesn't count) or that you are a trained musician yourself and actually understand how this works. If you don't know what a Neapolitan chord is or what that roman numeral shit I typed was or the chord spelling shit I typed was then hit me up....I can help.

---

> **munch-o-man** · 2026-08-31T06:43:15.000Z　
> I just want to add that I apologize for coming off harsh....there is almost zero music composition software that can do what you are advertising here and not be complete shit at it. It isn't a dig on you. It is just that people think music analysis is a LOT simpler than it actually is and that harmonic analysis is super easy and obvious and we all just took year years of music theory at a 4 year music conservatory because counting to 12 is hard. If you don't get the counting to 12 joke it just proves my point.Having said that, I'd love to help hack on some music software so if you aren't just trying to get easy money on blackbox software and actually care about music and software hit me up on discord: afreidah.but seriously, if you want people to take a look post a github and write software we can run ourselves after clone. If I have to create some third party account so some dickhole has my info and then have to push my data (music) through their servers I honestly have very little interest because there is absolutely no reason why the software you described should be a fucking saas service instead of something I can run locally unless your motives have less to do with functionality and more to do with something else...I love music and software, hit me up if you need/want help on the software or the music side.

---

> **munch-o-man** · 2026-08-31T06:52:34.000Z　
> is there such thing as 'un-editable midi'? You input midi and it outputs transformed midi.I really hope you didn't just build a generic web frontend that pipes a midi file into an llm with "criteria" like 'make it cinematic' and it generates a new midi file and you think that is worth $150.who is the target user for this?

## 导航

- 项目页：[[10-项目/orchestra.shevtoneaudio.com_d94bb00f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
