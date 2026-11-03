---
type: "corpus"
item_id: "a31b3b7224a8d286"
title: "Show HN: Subvocal – Talk to your computer without making noise"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50340088"
project_url: "https://subvocal.company/"
author: "aarushyadav"
published_at: "2026-11-02T17:16:17Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_aarushyadav
  - story_50340088
  - show_hn
  - front_page
metrics: {"points": 546, "comments": 296, "engagement_velocity": 546}
comments_count: 296
comments_total: 296
discovered_via: "hn:show_hn:3d"
---

# Show HN: Subvocal – Talk to your computer without making noise

> [!info] 一句话导读
> Hi HN, we're Aarush and Arnav from The Subvocal Company (YC F26) (https://subvocal.company/). We’re building smart glasses that let you talk to your computer wi…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50340088>
> 指标：点赞=546 · 评论=296 · engagement_velocity=546
> 作者：aarushyadav　|　发布：2026-11-02T17:16:17Z
> 项目链接：<https://subvocal.company/>
> 采集：2026-11-03T09:40:36+08:00　|　id：`a31b3b7224a8d286`

## 正文

Hi HN, we're Aarush and Arnav from The Subvocal Company (YC F26) (https://subvocal.company/). We’re building smart glasses that let you talk to your computer without talking out loud. You can mouth words silently and discreetly and the glasses decode them to text at the speed of speech.Here's a video of Dave from YC trying it out: https://www.youtube.com/watch?v=9QdX1eObVYI(Edit: you don't actually have to move your lips or even open your mouth for this to work! Since the RF can see inside your mouth the system can be fine tuned on "internal speech". This isn't the automatic tongue movements that occur when "thinking" words to yourself, but more like mouthing with your lips closed. It's a bit weird to do, but with practice, we have been able to get it down pretty well.)Arnav and I were studying CS at Georgia Tech at the beginning of the year, with no experience in silent speech or sensing. We were both AI-native builders and power users of Wispr Flow. What bugged us was not being able to use these tools in the library (or an office) or in public. At Stanford’s TreeHacks in February, we decided to build the most technically ridiculous thing we could think of. We’d read about AlterEgo, a silent speech system out of MIT’s Media Lab, and wanted to recreate it in 36 hours. We built a crude prototype, sticking EMG electrodes onto my face:https://drive.google.com/file/d/1mwhv5HZMz3UTevdrgwS5O7g2jWV...We got it to kind of work at a letter level in a very janky way. It wasn’t good enough to win the hackathon, but convinced us to go all in. The first time I typed a sentence without anyone noticing, I felt the magic of the technology.We quickly realized EMG (reading muscle electrical signals) wouldn’t work:- Signal changes due to sweat- Electrical interference- Placement variability- Most importantly, no one wants to stick electrodes onto their face!!So we switched to RF and built the glasses you see now. They emit radio waves, similar to Bluetooth, that pass through your face. As they cross the tongue, lips and soft palate, they’re modulated by silent mouthing. We train foundation models on this data to decode these perturbations to text.Despite prior academic research, getting this to work was a huge engineering challenge. First we built an extremely low noise RF sensing stack. Then we had to place antennas so their fields overlapped maximally with the articulators. Our first attempt on glasses failed completely, so we reverted to old habits and taped antennas on our face:https://drive.google.com/file/d/1ks0dS0eZiTV9EqSFsyB_w5BBjpc...Since taping antennas consistently in the same spot and angle was hard, we created this weird but effective head rig to hold them in place:https://drive.google.com/file/d/1rhzNFpdDzr7oHk0isFY70dkoV4C...This worked, but obviously wasn’t a product yet. So we worked deep in simulations to design glasses that could hold the antennas.That evolved into our design now, with antennas embedded within the frames. Once we established there was a signal, the next hurdle was cross-user generalization. Everyone’s facial anatomy, and hence RF signal patterns, are vastly different. We tried algorithmic workarounds but realized the only lever was to massively scale pretraining data.So that’s what we did. We set up booths in our office and paid people to read prompts wearing our glasses, to pretrain our models on. This produced a beautiful scaling curve, with errors falling quickly as we scaled our dataset and cross-user performance becoming genuinely compelling (as you see in the video above; Dave only had a short 20-sentence calibration).We always heard about building things from first principles but never understood it before this. We tried tackling it top down but completely failed. Only when we broke each component (the antenna, electronics, ML) down to its fundamentals to understand and optimize it did we get it to work really well.Over the next few months we’re continuing R&D to turn our prototype glasses into the slick product on our website and ship in Q1 2027. We’re also scaling up our dataset to improve performance on edge cases.For anyone who loves voice dictation but hates using it around people, we’ve opened preorders for our first batch of 500 units, with a $200 discount off the final price. Allocation is running out quickly, so get yours at https://subvocal.co/preorder!

## 评论（296/296）

> **hmokiguess** · 2026-11-02T17:30:59.000Z　
> EDIT: I find talking in that manner in a public setup to be awkward and unpleasant, maybe that's just me.That said, I think the idea of having a private walkie-talkie that connects on its own frequency for large crowded spaces to be very cool

---

> **theturtletalks** · 2026-11-02T17:31:53.000Z　
> Someone built an open-source version of this, but it’s far from polished:https://github.com/joeblau/subvoxThere was this really interesting one where it reads your lips:https://github.com/amywork777/lipflowI’m using these to build my own so I can work in co-working spaces, planes, and libraries. Though moving my mouth with no words might draw some eyes.

---

> **s3graham** · 2026-11-02T17:32:04.000Z　
> Neat! I don't like talking to my computer (audibly or not), but that's a cool demo.I wonder if we could eventually end up with a "throat muscle" version where people learn to talk a new way without having to move the visible mouth muscles too.

---

> **mcbishop** · 2026-11-02T17:33:01.000Z　
> I've thought about learning sign language in order to communicate with the computer in a not-super-annoying way. Your solution... much more realistic. Cheers.

---

> **paisawalla** · 2026-11-02T17:33:23.000Z　
> How have the glasses been received? I don't understand why they're required, is it only to have a consistent mount point for the radar sensor, relative to the face? Have you thought about a throat mic?

---

> **fowlie** · 2026-11-02T17:33:35.000Z　
> Talk about over engineering a problem! If typing speed is an issue guess what, humans can train themselves to type really fast on a keyboard.

---

> **thisisauserid** · 2026-11-02T17:34:42.000Z　
> I'm more looking for the Jane from Speaker for the Dead version. In-ear device that can hear and feel the subvocalization.

---

> **PebblesRox** · 2026-11-02T17:37:07.000Z　
> Very cool! I was curious to hear the details of how it worked but couldn’t find them on your landing page. I’m glad to see them here and you might want to include them more prominently on the page itself. I didn’t even realize it was a pair of glasses til I read the above.

---

> **OhMeadhbh** · 2026-11-02T17:38:31.000Z　
> Spent 30 seconds scrolling down to try to figure out what this is. Eventually clicked away from the site because it was taking too long to get to the point. I'm sure it's great and I understand it's something to do with glasses and subvocalizations, but consider a one sentence contextualization at the top of the page.

---

> **jstummbillig** · 2026-11-02T17:38:43.000Z　
> Category: A product, that's obviously super useful, as long as it will work.

---

> **tomhow** · 2026-11-02T17:40:37.000Z　
> I'm curious about whether this could be done with the hardware mounted on top of the laptop screen or on a stand on the desk, rather than the glasses form factor. Have you explored this?

---

> **adamsmark** · 2026-11-02T17:42:14.000Z　
> I use the Vekta. I tried whispering and it doesn't feel right.Throat mics don't work at all - see reviews online.This is a different approach, so I am cautiously optimistic.

---

> **TechSquidTV** · 2026-11-02T17:43:06.000Z　
> I would be fairly interested if this works without opening my mouth. Like, if you can nail _micro_ tongue movements, it would feel pretty close to thought.

---

> **popap** · 2026-11-02T17:46:46.000Z　
> That is fascinating. How do the radio waves get modulated? Do you think it is possible to use this technique for spying technology, with remote transmitters and receivers intersecting a person's facial anatomy to pick up the details of even a whispered or muttered conversation?

---

> **ciefa** · 2026-11-02T17:48:51.000Z　
> God do I hate websites that make you scroll to go through an animation, why do people still do this

---

> **hippycruncher22** · 2026-11-02T17:49:09.000Z　
> What's wrong with human connection and speaking. :( I feel like the isolation of this modern world is lame.

---

> **ideasphere** · 2026-11-02T17:52:36.000Z　
> Just scroll normally!

---

> **johnhamlin** · 2026-11-02T17:53:14.000Z　
> With so many people singing the praises of voice to text, I keep thinking about how most sci-fi futures feature subvocalization as a prerec for that kind of adoption. Always love to see sci-fi come to life!

---

> **bluegatty** · 2026-11-02T17:54:40.000Z　
> Why do you hurt communicating your very cool product with an annoying and counter intuitive scroll experience?And after some time I could not figure out what this is?Put this part: " building smart glasses that let you talk to your computer without talking out loud. You can mouth words silently and discreetly and the glasses decode them to text at the speed of speech."right at the top and maybe show someone actually doing that instead of hiding behind cryptic marketing.Also, the product looks great.Get your words out of the way 'say what it is'.Very amazing tech though

---

> **avree** · 2026-11-02T17:55:44.000Z　
> Do most people talk faster than they can type? It's the opposite for me - I also read aloud slower than I can read in my head.

---

> **mirmor23** · 2026-11-02T17:59:12.000Z　
> The tech sounds cool, but my guess is this product might work for anyone whose text to command ratio is very high. If the formatting and commanding are the main tasks, then this product would be more of a distraction for a fast typist.Regarding the website, you should lead with product, its details, rather than founders shown in 360 degrees from various vantage points. It is distracting and frankly irritating.

---

> **sourpanda** · 2026-11-02T17:59:38.000Z　
> I think this is incredibly cool and straight out of a sci-fi novel! I think this is phenomenal for accessibility and for hands-free computing in general. I also agree with other comments that the website should have more detail on how it works, such as what you included in the post body. Amazing work guys!

---

> **gh5000** · 2026-11-02T17:59:43.000Z　
> Cue the resurgence of lip reading-based espionage. Imagining having to scan the room for people watching subvocalizers. Will subvocalizers start holding up a clipboard over their face a la NFL coaches?

---

> **proee** · 2026-11-02T18:00:49.000Z　
> There is a product by Subtle called Voicebuds that allows for super silent dictation. Looks like the product is not available for purchase yet, but I would prefer to have earbuds over glasses.https://www.subtle.co

---

> **settsu** · 2026-11-02T18:01:30.000Z　
> FYI, the subvocal.company site is unscrollable with a mouse wheel in WebKit browsers on Mac (Safari, DDG, Kagi Orion), though the touchpad will work. No issues elsewhere (Mac non-WebKit, Win11, Ubuntu)

---

> **joshstrange** · 2026-11-02T18:03:35.000Z　
> Super excited to see more products in this area. I talk to my computer the majority of the time now, and I can do that because I work from home. If I were on public transportation or in an office, it would be much more difficult. It's been interesting to watch the Overton window, if you will, shift for people talking _to_ their phones. Now, the majority of my family will use voice to text on their phone whereas I remember just a few years ago, if not even just a year ago, it was made fun of.

---

> **sixtyj** · 2026-11-02T18:04:38.000Z　
> There is a long way from a prototype to production. Remember Google Glasses, Oculus, Meta Rayban, Apple Vision Pro?All of them are visionary and we would think that ppl gonna like them…Well… ordinary people want boring tech.This will be similar with whispering to glasses… Visionaries will like it… and return to missionary (boring) s*x (I hope that I don’t get a ban.)Myself, I would buy these glasses immediately. But I would hate them as well as I would think I am insane (who wants to talk to yourself?).Edit: Dang replied. I wish all the best to the team behind “whisper glasses”. It is amazing. Connect it with ElevenLabs and you rule the world. (Previous: It wasn’t meant a hate speech.)

---

> **sschueller** · 2026-11-02T18:06:40.000Z　
> So it's a pair of glasses that can transcribe when you mouth words silently? I still don't know how it works, they say no cameras and it works with noise so I assume sort sort of reverse bone conducting?

---

> **smokel** · 2026-11-02T18:07:41.000Z　
> Are there any health risks with this method?Edit: mostly concerned about RF near my eyes for 8 hours a day.

---

> **replete** · 2026-11-02T18:08:05.000Z　
> Infuriating website UX, you really must add the scrollbar back. Apple do shiny things like this but they know you can't get rid of the scrollbar and piss people off trying to look at information

---

> **polartx** · 2026-11-02T18:10:05.000Z　
> Reminds me of the Leap Motion I preordered

---

> **skilning** · 2026-11-02T18:11:02.000Z　
> Does the model require internet access, or is it running entirely locally?

---

> **mrtesthah** · 2026-11-02T18:12:45.000Z　
> Apple recently a purchased a company with seemingly equivalent technical capabilities:https://www.cnet.com/tech/services-and-software/apple-qai-ac...Hope you guys are well-positioned patent-wise.

---

> **capl** · 2026-11-02T18:13:01.000Z　
> Watched the demo video… and if this is satire: incredibly well executed

---

> **kenferry** · 2026-11-02T18:15:50.000Z　
> This is very cool, but oddly, the site is TOO focused on the user problem being solved to the extent that it feels like snake oil. The issue is that this is contrary to people's experience of what is possible, so without discussing WHY you can do this, it looks like a scam or vaporware.

---

> **collabs** · 2026-11-02T18:16:31.000Z　
> I am so glad to see an unpolished early look and an honest evaluation of about five percent error rate in the YouTube video. The really cool stuff will be the applications on top of `subvocal` though at least in my opinion.So this could take "noise canceling" to a whole new level if you could somehow "speak" across a loud bar or across the world, for that matter. Being integrated into something like Signal or similar end to end encrypted platform would be interesting as well.

---

> **clkao** · 2026-11-02T18:17:25.000Z　
> this is super cool. I did some digging about current research on avsr using video and lip point cloud movement a while back. found projects like https://github.com/amanvirparhar/chaplin but this seems more promising!

---

> **json_hero** · 2026-11-02T18:17:35.000Z　
> Should really just be like a leap motion device on the desk, glasses are so gimmicky and aren't gonna fly for people with prescriptions (a large set of people in-front of computers all day)

---

> **monkeydust** · 2026-11-02T18:17:38.000Z　
> One of the coolest things I have recently seen but would love some details. It also got me thinking a about this recent Neuralink post.https://neuralink.com/updates/72-hour-voice-hackathon/

---

> **kmoser** · 2026-11-02T18:23:42.000Z　
> You can have a silent conversation with someone else wearing the device? This does not bode well for casinos.

---

> **MPSimmons** · 2026-11-02T18:25:44.000Z　
> This is super cool. I think it's the first piece of additional hardware I've even considered pre-ordering.

---

> **lukko** · 2026-11-02T18:26:00.000Z　
> Great work!Really like seeing the early prototypes here, and would love to see more on how the RF tech works on the website.Are you able to patent it?

---

> **dogscatstrees** · 2026-11-02T18:30:21.000Z　
> Let's go! Love the idea. Like the analog to bone conduction earbuds. Just please don't turn into WisprFlow where they route the voice metadata, unbeknownst to many, to a third party partner who stores and mines it for who-knows-what.
> Good luck fellas.

---

> **jdironman** · 2026-11-02T18:35:25.000Z　
> What I would really like is a washable "cyber suit". Mock or turtle neck (for the voice / STT capture / control), EEG sensors, breathing rate, blood pressure, gestures via arm motion sensors,). Removable rechargeable battery module to wash the torso / shirt slap it on a clean one. For EEG it would have to be pretty compressed though, so not sure it would be comfortable enough to wear to sleep? maybe only an internal harness needs to be that compressed. not sure. I'm tired of wearing a Fitbit, or glasses, or these different things people have to look at, keep up with, break easy etc.

---

> **mmaths** · 2026-11-02T18:35:58.000Z　
> I wonder if in a couple of years we gonna have some teeth implant that will capture sounds to our devices.

---

> **popupeyecare** · 2026-11-02T18:38:25.000Z　
> Preordered!Can we use RF for other medical applications? As an anesthesiologist, we do nerve blocks before surgeries or for pain. One rough indicator that it's working is muscle paralysis. Also similar for botox.Very interested.

---

> **howunfortunate** · 2026-11-02T18:39:45.000Z　
> This is:1. Insanely cool2. Gives me serious "whispering earring" vibes. Imagine having a full on conversation with an AI via subvocalization and listening with ear bud to guide you throughout the day. https://gwern.net/doc/fiction/science-fiction/2012-10-03-yva...

---

> **contingencies** · 2026-11-02T18:40:49.000Z　
> Much respect for actual innovation. I hope you get filthy rich.From your comments it seems to reach this point you tried at least open source lip reading software, IMUs, variant antenna mounting strategies, various frequencies, and then gathered training data. You articulated strongly why the product is desirable and why the failed modes were dead-ends. I hope you can deliver on your pre-orders and are able to scale and/or sell the IP for a strong exit.

---

> **airbreather** · 2026-11-02T18:41:57.000Z　
> Website is shit, "how it works" tells you nothing much useful about how it works, and I assume there is some custom hardware (as described in the post above) but nowhere on the website I could see this actually said, and therefore zero indication of the size of the interface electronics etc etc

---

> **vessenes** · 2026-11-02T18:42:32.000Z　
> Just preordered -- glasses request: there's no way to say it nicely, I have a big nose. With a high bridge. Many glasses are really tough to get properly placed; may I request you not give up on the pads w/metal adjusters that you have in the product photos? Don't let a designer take them away from you, us folks not one standard deviation from 'normal' noses will thank you.Second, how tough is this signal processing? Will it be done on-glasses, or through an app? Third, what's the equivalent of a wake word for these? I'm reminded of the Apple Vision Pro radar to see if your fingers are clicking. I could imagine a lot of modalities where I want to just start talking and have things happen, and a lot where I don't want the glasses to pick it up. Fourth, I think a cool voice change demo would be rad -- not sure what latency is like, but if you could get it end to end under like 250ms you could probably have someone exaggerate the mouth movements and pipe out audio of them talking like someone else. Which would be another really cool demo.Super cool. You're going to be working 80 hour weeks for the next year, I'm excited to see what you put out!

---

> **0x4e** · 2026-11-02T18:44:53.000Z　
> For the ones thinking this is great, have you actually tried to talk without making sounds?I don't think it is an intuitive action at all and I became self-conscious about not making a sound rather than talking like I normally would.I suppose it would require some "getting used to."Regardless, I think it is a cool idea and a real problem. Sometimes I don't want to type nor talk out loud so I find myself whispering at my phone like I'm telling it a dirty secret.--As I'm writing this, I think this kind of product might not hit the market for consumers, but I'm seeing this used by Flock like companies to spy on people's speech, so kudos on making machine lip reading a thing!

---

> **growt** · 2026-11-02T18:46:47.000Z　
> If the tech is mostly in the glasses temples, I would prefer to have something that attaches to my existing glasses. I have prescription glasses and a big head, tried the Even G2 smart glasses and the available frames set just too small for me

---

> **csh0** · 2026-11-02T18:49:12.000Z　
> Very cool. I suspect you guys will get scooped up by a bigger player working on smart glasses soon.

---

> **vibranium** · 2026-11-02T18:51:08.000Z　
> “Foundation models” I feel like this has lost all meaning? Can’t you just say “we train models on this data”?

---

> **willwade** · 2026-11-02T18:52:24.000Z　
> Theres a LOT of people working on this.. Cornell have been putting students on this task for about 5 years.. Lots of fun different ways of doing it. Interesting you went the radar from glasses route.. I wish you well. Yet to see a product apart from the odd lip reading ML project that makes it into a product..

---

> **desireco42** · 2026-11-02T18:59:41.000Z　
> This is such a weird thing that I can't wait to try it out. I don't know, like it's so crazy that it has to be good

---

> **alexgoodhart** · 2026-11-02T19:01:53.000Z　
> Q1 2027- unlikely

---

> **uzbit** · 2026-11-02T19:01:58.000Z　
> Really neat tech! Just curious, how much did you leverage AI during the development? This seems like the type of neat tech that we should expect more and more from wielding our new tools well.

---

> **ipsum2** · 2026-11-02T19:05:41.000Z　
> If you're selling a physical product, using AI to model your product seems like a really bad idea. You have no idea if the product actually fits on their faces.Calling it early - this is a scam. There's no way they're going to deliver that product, in that form factor, by Q1 2027.

---

> **sMarsIntruder** · 2026-11-02T19:06:53.000Z　
> Really cool piece of tech!
> Languages supported rn? English only?

---

> **rdiddly** · 2026-11-02T19:08:38.000Z　
> Pretty cool! My only wish is that all this kind of work didn't gravitate toward glasses or assume glasses are the default thing-on-your-face now. 3/4 of humans don't wear them, and even some of us blind bats hate them enough that we endure the hassle of contact lenses!

---

> **uhutiik** · 2026-11-02T19:11:18.000Z　
> This is so dumb

---

> **d1sxeyes** · 2026-11-02T19:11:55.000Z　
> One thing you might consider is actually telling people what it is on the homepage. Took me a fair bit of work to understand that this is effectively a pair of smart glasses.Maybe I could have figured that out from the video but for folks who can’t watch the video it’s quite hard to discover what you’re building.

---

> **ipsum2** · 2026-11-02T19:14:35.000Z　
> All of the images, including the glasses, are AI generated.Anyone who preorders - you are getting scammed.Pangram: https://www.pangram.com/history/images/614ffe91-8ba9-4d3c-b1...

---

> **catoc** · 2026-11-02T19:16:18.000Z　
> Fantastic!Just preordered.What languages do you support? (English is fine, but any others?)

---

> **columk** · 2026-11-02T19:22:31.000Z　
> I think these have a place but I can't say the same for most other new AI communication devices. Creeper glasses, pins, watches, desktop units etc. I want to be able to speak and hear from my agents at all times but why would I want a new device when I already wear earbuds? New products are being designed to pick up low murmuring/whispering, like the Subtle earbuds, but I assume most earbuds will be designed this way in future.

---

> **joshdavham** · 2026-11-02T19:23:31.000Z　
> Are there any associated benchmarks with this? Like how accurate is this technology for different types of facial structures, sentences or languages?

---

> **retromario** · 2026-11-02T19:26:00.000Z　
> This is amazing, brilliant idea and nice execution. Are you concerned about Meta or any other established smart glasses players potentially copying such an idea?

---

> **BrokenCogs** · 2026-11-02T19:26:36.000Z　
> If no one wants to dictate to their phones or computers in public, surely they don't want to do this (looking like they are talking without making any noise) in public?

---

> **SkyPuncher** · 2026-11-02T19:53:51.000Z　
> Based on my understanding of the technology, this also means you can effectively dictate in loud environments. Correct?I find that I need this most often when I'm doing yard work, running equipment, or cleaning out the garage. Audio based microphones pick up so much noise.

---

> **outlore** · 2026-11-02T20:04:13.000Z　
> Can someone comment on the AirPods tweet making the rounds (i.e. the subvocal killer)? I am excited by Subvocal, but am wondering how much bespoke hardware is actually required?

---

> **aerhardt** · 2026-11-02T20:04:51.000Z　
> I have this problem and I was wondering how it would be solved. For now I can cope because I mostly work from home but I’ll keep track of you guys. Best of luck!

---

> **mrandish** · 2026-11-02T20:12:12.000Z　
> > "you don't actually have to move your lips or even open your mouth for this to work ... It's a bit weird to do"In the video Dave just finished the training mode and is silently moving his lips, which seems pretty natural to me. I just spent a minute trying to do 'internal speech' (as many elements of speech as possible with lips closed). It does feel weird and seems like internal speech is probably providing a fair bit less signal for the system to sense (in both signal freq and amplitude). I realized I can't guess at how much articulation is 'enough' without feedback.Based on that I'm guessing adapting to internal speech might follow a bit different path than silent speech, which seems more like 'just do what you already do silently'. Extrapolating, I expect training internal speech might involve more real-time feedback to help the user find the right degree and kind of articulation.I realize you're still in the prototype phase but I assume an increasing number of people are getting multiple longer sessions. Do new users advance from silent to internal speech quickly and stay there? I'd be surprised as, intuitively, 'Silent -> Internal' seems like a bigger step than 'Normal -> Silent'.Separately, if I was using it daily, I can imagine wanting to evolve a kind of micro-expression shorthand for 'Yes', 'No', 'Pause' and 'Stop', since two humans naturally evolve similar non-verbal queues over time. Vocalizing words is flexible and expressive but not efficient. It would seem odd if an intelligent, adaptive 'invisible friend' living on my face for years didn't adapt to me and me to it. Are you guys thinking in those directions for the future?

---

> **postscape** · 2026-11-02T20:14:34.000Z　
> I remember seeing AlterEgo a few years ago and thinking it was so cool (obviously was missing voice agents to make it really cook)Was just thinking this could be applicable for people with some disabilities tied to an actual voice agent and speaker. Or even in foreign countries where you talk and respond in the foreign language instead of waiting for an additional translation layer.

---

> **93po** · 2026-11-02T20:24:59.000Z　
> Super cool! love this

---

> **makmanalp** · 2026-11-02T20:31:59.000Z　
> This is also neat thing to have with people struggling with typing (RSI, injuries, disabilities) but want to do more than just dictation, eg Talon Voice. A common problem with voice commands and dictation alone is that people find they're hurting their vocal chords pretty quickly. Neat.

---

> **tallanvor** · 2026-11-02T20:32:25.000Z　
> First, I absolutely hate having to scroll and scroll and scroll and scroll to try and figure out what's going on.Second, I read this:"The current prototypes already decode open-ended silent speech in real time, and accuracy continues to improve as we collect more data and train larger models. Like any input method, it can occasionally get something wrong, so the product is designed to use context and easy corrections rather than pretending errors never happen."And I have to ask, does this mean everything I vocalize is being sent to an unknown server to be analyzed, potentially read by a person, and then used to train your model further? Because that's clearly not going to fly for either me or my employer. You need to be crystal clear what information people are potentially sharing with you before they purchase your devices.

---

> **ergocoder** · 2026-11-02T20:36:29.000Z　
> When I first saw their promotional video, I thought it was a meme video with the dude mumbling to typing.

---

> **nathias** · 2026-11-02T20:47:30.000Z　
> I knew subvocalization would be the main way to talk to ais as soon as I read it in Alistair Reynolds books. I hope it could be done without any mouth movement by just microgestures soon.

---

> **genxy** · 2026-11-02T20:49:28.000Z　
> Google wanted to put this tech into its phone, but then was convinced it was a bad idea due to privacy invasion. It could for instance correlate sexual arousal with any phone interaction (video chat, youtube, display ads, etc), giving google and advertisers the ability to make custom targeted ads for specific users, as it would "know your type".Where does inference occur? Does it work offline?

---

> **ggsp** · 2026-11-02T20:57:27.000Z　
> Very cool tech! Q1 27 is… Ambitious. Good luck with it, we need new interfaces for AI!

---

> **mpeg** · 2026-11-02T20:58:36.000Z　
> I'd love to preorder, but there's nothing in the site that tells me whether you will ship internationally. I guess not for this first batch?

---

> **aantix** · 2026-11-02T20:58:45.000Z　
> Are the full glasses really needed?Feels like there could be a small device attached to each arm of a pair of glasses?

---

> **atulvi** · 2026-11-02T21:15:10.000Z　
> This is it! I was thinking about this a few weeks ago. None of the big tech gets this. If this works, damn, that's the future wearable I want. But why glasses? can you do this equally well with a earphone form factor?

---

> **girvo** · 2026-11-02T21:24:30.000Z　
> This is a super cool product and I am legit excited for itBut I find the idea that talking is faster than typing utterly wild, I can type faster than I can think!

---

> **khimaros** · 2026-11-02T21:24:36.000Z　
> this does not appear to be https://en.wikipedia.org/wiki/Subvocal_recognition

---

> **snitty** · 2026-11-02T21:28:18.000Z　
> Will I need a subscription to use them? If so, how much will it cost?

---

> **cpan22** · 2026-11-02T21:35:12.000Z　
> this is one of the first product demos I've seen in a while where I thought to myself "this could actually solve a big problem of mine". really looking forward to this one!

---

> **HoldOnAMinute** · 2026-11-02T21:42:25.000Z　
> Pham Nuwen approves of this human-computer interface

---

> **zabaki** · 2026-11-02T21:45:42.000Z　
> Great for stroke victims who gets paralysis.
> Which languages wil be supported?

---

> **matt3210** · 2026-11-02T22:01:43.000Z　
> Radar straight to the face, nice. Needs medical approval IMO

---

> **xnx** · 2026-11-02T22:05:19.000Z　
> Sounds cool. Do you have patents on this?

---

> **vakili** · 2026-11-02T22:18:57.000Z　
> Vox [0] is an alternative device with similar aims, worn as a pendant instead of glasses.[0] https://www.augmental.tech/vox

---

> **sarjann** · 2026-11-02T22:24:40.000Z　
> Is the idea to add a display element like even g2? Seems like this is half of what could be a good product.Being able to work on a commute and code (looking at the glasses's screen) would be a killer application.

---

> **hybrid_study** · 2026-11-02T22:33:01.000Z　
> Big deal. The HAL9000 did this back in 1968.

---

> **ktosobcy** · 2026-11-02T22:39:22.000Z　
> Is it English-only?

---

> **oever** · 2026-11-02T22:48:37.000Z　
> Combined with TTS, this can give a voice to people with certain types of mutism.

---

> **aftbit** · 2026-11-02T22:51:47.000Z　
> Can this be made to work offline, without a cloud server? I wouldn't want my words to be passed through an API, but run locally on device. I don't mind buying fast GPUs for this.

---

> **apparent** · 2026-11-02T23:02:45.000Z　
> Isn't a "Show HN" supposed to be reserved for things that people can experiment with and give feedback on? This doesn't seem sufficiently interactive, and the sales pitch at the end seems odd for a Show HN, at least to me.

---

> **demo4567** · 2026-11-02T23:09:15.000Z　
> Yes.1. I need my existing glasses.
> 2. It needs to work offline.Otherwise this is a no-go

---

> **randomImmigrant** · 2026-11-02T23:15:43.000Z　
> Really cool. I’m especially drawn to this as the time from thought to mouthing the words is so much faster than speaking out loud, for me.But I’d be concerned both about battery life, and the long term health consequences of having an RF chip so close to my eyes/brain. Have you explored these aspects much?

---

> **levocardia** · 2026-11-02T23:24:28.000Z　
> This is so cool. EEG headband next, so I can talk to my computer just by thinking?

---

> **singpolyma3** · 2026-11-02T23:55:26.000Z　
> Shipping to Canada expected?

---

> **UnfitFootprint** · 2026-11-02T23:57:37.000Z　
> I wonder how well this works on folks with accents. Just thinking of Australian pronunciations which lack a lot of the US annunciation - translating perhaps to less muscle movement and more noise.

---

> **raver1975** · 2026-11-03T00:09:18.000Z　
> Will they give me cancer of the face?

---

> **queenkjuul** · 2026-11-03T00:13:50.000Z　
> I can't with these sites that so aggressively hijack scrolling. Counterintuitive and frustrating to use.

---

> **kaonwarb** · 2026-11-03T00:20:59.000Z　
> Cool tech. Typo note: "Ask your AI assitants anything you want."

---

> **sudosteph** · 2026-11-03T00:29:54.000Z　
> Nice! I'm so glad to see founders playing with possibilities for the interface here. And also seems a lot easier than my idea to wear a downward facing camera and train a model that can read finger-spelling.

---

> **ninjahawk1** · 2026-11-03T00:39:58.000Z　
> I saw this as a YC startup a while back. It crossed my mind earlier today. I do think this is going to be an interesting direction to go in and I could see it becoming as normal as buying a mouse or keyboard.

---

> **serf** · 2026-11-03T00:49:04.000Z　
> putting the 'Due Today' price in a larger font and hiding the total smaller, under that price is sneaky.Big companies do it too, but my feedback has little chance of reaching their ears.

---

> **edmundsauto** · 2026-11-03T01:17:57.000Z　
> Very cool, this is how Ender communicates with his AI in Xenocide and Speaker for the Dead.I would have preordered but your accuracy FAQ is terrible. It amounts to “it’s really bad now so we won’t give a number, we hope to improve it”. If you were 90%+ with the same promise I would have paid earlyAccuracy is the sales objection. Your website does a terrible job addressing that.

---

> **itomato** · 2026-11-03T01:24:46.000Z　
> Why the eyeglass form factor? As people have mentioned, fitting eyewear is no joke. Not everyone has a face for RayBans.Why not simpler, more discreet electrode pads? Get nifty with flex PCB and wearables instead of another "Smart Glasses".Sweatband, tiara, smart crown, halo.. No crowding here.

---

> **dang** · 2026-11-02T17:31:20.000Z　
> > I like it but I don't want it, I'm not sure, it feels weird and cringy."Please don't post shallow dismissals, especially of other people's work. A good critical comment teaches us something."https://news.ycombinator.com/newsguidelines.htmlp.s. Especially please don't do this when a thread is brand new. Such comments are the easiest to post, and therefore the quickest to appear, but by posting them, you steer the discussion straight away from the curious, thoughtful conversation we want here. Threads are extremely sensitive to initial conditions, so this is important.

---

> **willio58** · 2026-11-02T17:35:18.000Z　
> > There was this really interesting one where it reads your lipsThis is what I thought the original post was about. The glasses you have to wear is where that lost me.If we could get lip-reading via your computer/phone camera down perfectly, that's the real win. Making people wear your goofy frames is where you lose a massive portion of people. Nobody wants to look like Zuckerberg lol

---

> **aarushyadav** · 2026-11-02T17:38:40.000Z　
> Yup we worked with IMUs as well when we started this. They measure aggregated face motion, so cannot distinguish between fine phonetic classes, only broad words. The open source demo got to a 5 word classifier, I believe. We tried a lot to make IMUs work too, in various form factors, but the signal doesn't contain enough information for open ended decoding beyond classifying between a few words. We would have loved to be able to just push software!

---

> **melvinmelih** · 2026-11-02T17:37:03.000Z　
> Great idea, if only we could use our hands and fingers to input information into the computer

---

> **kennywinker** · 2026-11-02T17:53:31.000Z　
> It looked like there was a throat mic in the first shot... it seems counterintuitive that you'd get better performance out of lidar on face muscles than on a throat mic.

---

> **waltbosz** · 2026-11-02T17:49:17.000Z　
> I think the problem to solve here is repetitive stress injury caused by typing

---

> **rootusrootus** · 2026-11-02T17:56:35.000Z　
> They are claiming 200+ wpm on a prototype. Half that speed would put you in the top tier of typists, and the number of people that get anywhere close to 200 is vanishingly small.

---

> **stubish** · 2026-11-03T00:59:50.000Z　
> I can't type while simultaneously using another control like a mouse, joystick, tablet. I guess I could overengineer the problem by growing more arms. And even that doesn't solve the problem of mouse pointers having to constantly jump between UI elements and a canvas because they can only be in one place at a time.I look forward to your typing speed tutorials for arthritis sufferers.

---

> **40four** · 2026-11-02T18:20:52.000Z　
> I had to look it up, I forgot he communicated with her through sub-vocalizations. I remember the jewel earpiece, but in my head he just communicated through thoughts or something.Good reference! That series of books Is one of my all time favorites.

---

> **frenchie4111** · 2026-11-02T18:23:11.000Z　
> First, this my favorite book of all time so I love seeing it shouted outSecond, I agree with exactly this. Something shaped like an AirPod

---

> **vessenes** · 2026-11-02T18:46:19.000Z　
> I mean we're getting pretty close here -- you could have these + your AirPods in transparency mode up and you're not far off. Also Claude won't currently ice you out for going dark, unlike Jane.

---

> **PebblesRox** · 2026-11-02T17:39:19.000Z　
> E.g. your FAQ says it doesn’t use cameras but does not say what it does use. And when I got to the footer and clicked the “how it works” link, it seemingly took me back to the top of the page I had just read.

---

> **LatencyKills** · 2026-11-02T17:55:49.000Z　
> I was just trying to help a vibe coder and immediately noticed that their README.md was over 2,000 lines long. I asked, "Why is your readme so long?" and their response was, "This is just a really complicated application."The app essentially manages a bunch of TODO items written in markdown.

---

> **aarushyadav** · 2026-11-02T17:56:55.000Z　
> Yup that makes sense. Thanks for the feedback, we'll make some changes shortly!

---

> **jasonlotito** · 2026-11-02T18:01:19.000Z　
> > Talk without talking.
> > Input text at the speed of speech, silently and invisibly.I understood from just this. But the demo video impressed even further.> Spent 30 seconds scrolling down to try to figure out what this is.Did you try reading the site? Or maybe doing something other than just scrolling?Does it need some form of subway surfer to get you to pay attention?> Eventually clicked away from the site because it was taking too long to get to the point.So yeah... subway surfer. This generation is cooked.

---

> **aarushyadav** · 2026-11-02T17:46:44.000Z　
> Yes, we have! The same kind of RF doesn't work in that form, since it is attenuated strongly over that big of a distance. But the other interesting alternative we tried it mmWave radar, RF at about 60 GHz, the same band as 5G. This is much more similar to conventional radar, in that it would bounce off the face rather than passing through it like our current system. We found a few problems with this:
> 1. It faced the same issue as cameras. mmWave radar has a very low penetration in tissue, so it basically just bounced off the mouth. This only let us see visemes, which aren't enough to get to a low error rate as complete phonetic decoding can.
> 2. While mmWave radar can detect skin movement as small as a few microns via Doppler shift (given it's small wavelength), its spatial resolution with most systems is quite low. For example, it can tell that something moved 2 microns but within a 5cm x 5cm block. This coarse information makes it very hard to decodeThat's why we weren't able to make something that can mount to your laptop. We're trying to make a necklace form factor at some point in the future though, but can't give a date on this!

---

> **aarushyadav** · 2026-11-02T17:48:51.000Z　
> It actually can! Since the RF can see inside your mouth the system doesn't inherently need lip movements and can be fine tuned on what we call "internal speech". Note that this isn't the automatic tongue movements that occur when "thinking" words to yourself, but it's rather like mouthing with your lips closed. We don't often lead with this since it's weird for many people to do, but with a bit of practice, we have been able to get it down pretty well.

---

> **hk__2** · 2026-11-02T18:00:23.000Z　
> But how would you distinguish all the sounds that don’t require any tongue movement, like (most of?) the vowels?

---

> **aarushyadav** · 2026-11-02T17:51:02.000Z　
> Most probably not possible to do this remotely, since this kind of RF needs to be transmitted through the face, and if you transmit them from too far away very few of them will actually take a path that goes through the face and comes back to your receiver.They get modulated since your mouth is a complex dielectric environment. Tissue, water, and air have different dielectric constants (different permittivity to RF) and the motion of the muscles in this medium leads to interactions with the waves that fill it, changing their phase and amplitude as they propagate.

---

> **cebert** · 2026-11-02T18:00:23.000Z　
> It is frustrating and makes me close a lot of sites

---

> **uhutiik** · 2026-11-02T19:13:47.000Z　
> Because they don’t even understand their own product well enough to communicate the benefits

---

> **doctorhandshake** · 2026-11-02T17:52:09.000Z　
> This is a little like replying to a show HN for a new kind of stylus input device with “what’s wrong with pen and paper”

---

> **temp123477** · 2026-11-02T17:54:13.000Z　
> This is more a keyboard killer than a dinner party killer.

---

> **ShinTakuya** · 2026-11-02T17:55:04.000Z　
> I can see this being useful on public transport where you don't want to bother people while taking notes verbally. It's not all about avoiding connection.

---

> **augment_me** · 2026-11-02T17:56:45.000Z　
> Maybe you don't want strangers around you hearing you say "Hey Claude wish my grandma happy birthday" as it's not yet morally okay to delegate such social tasks to the models

---

> **barbazoo** · 2026-11-02T18:24:41.000Z　
> There is no human connection typing words into a box, that's seems like what it's mostly replacing. Talking to your email client, talking to your AI agent. Lots of us are much faster speaking than typing and especially with AI, it doesn't matter a whole lot in my experience how polished the output is, the benefit from ending up with a lot more text because one can just talk freely is very beneficial.

---

> **aarushyadav** · 2026-11-02T17:59:17.000Z　
> That makes sense. We will implement that!

---

> **aarushyadav** · 2026-11-02T18:00:56.000Z　
> Most people type at 40-50 WPM. Developers can often type at 70-100 WPM. Meanwhile, most people can talk at 120-200 WPM. Beyond just speed, we've found with many people that talking things out tends to flow more naturally, since it's often a lower friction action so people don't "sanitize" the text in their head before outputting it. Leads to better prompts quite often :)

---

> **xbar** · 2026-11-02T18:02:27.000Z　
> Most people talk faster than they can type. 80 wpm voice chat is easy for everyone. 80 wpm typing filters out most typists.

---

> **Zambyte** · 2026-11-02T18:05:35.000Z　
> I'm not reading aloud most of the time that I'm talking.

---

> **egeozcan** · 2026-11-02T18:05:42.000Z　
> Yes, I'd estimate the vast majority of people speak faster they can type. Not sure about the thinking part because I usually have 20 threads going parallel in my head and can't imagine what normal thinking would be like.

---

> **sspiff** · 2026-11-02T18:08:14.000Z　
> I'm the same. I also can think ahead / along much better while typing. When I'm talking I'm just talking, not thinking as much.But I guess thinking is going out of style anyway.That said, I know a lot of people prefer talking to their computer, especially when their computer is a phone. So there is definitely a place for stuff like this.

---

> **wongarsu** · 2026-11-02T18:14:22.000Z　
> While sitting at the desk, I type about as fast as I talk. While unloading the dishwasher I'm a much faster talker than typer

---

> **ronyeh** · 2026-11-02T18:31:26.000Z　
> On my phone, I do. I still like to tap with my thumbs, but my iPhone keyboard sucks so when I need to type a lot, I’d rather dictate.

---

> **SkyPuncher** · 2026-11-02T19:45:23.000Z　
> I talk faster, but beyond the speed, I find it allows me to explain things to the LLM much more naturally.

---

> **themanmaran** · 2026-11-02T18:12:29.000Z　
> Yea in one of the further Ender's Game novels they talk about this tech a lot for characters silently mumbling to the AI.

---

> **ElijahLynn** · 2026-11-02T18:41:48.000Z　
> I second that. I've been talking and talking to my phone and AI even more and more since it keeps getting better and is generally pretty accurate these days. And there are times when I end up typing because of environmental reasons.This is just really groundbreaking and I know the research has been out there for a little while but to actually implement is a whole nother ball game.I think the use cases for this will expand as the product ships and gets out there!

---

> **_jholland** · 2026-11-02T18:45:10.000Z　
> Agree, incredibly cool, and I could definitely see myself using one, but it does give off slightly dystopian vibes, making me think of the speakwrite in 1984:"In the long, windowless hall, with its double row of cubicles and its endless rustle of papers and hum of voices murmuring into speakwrites, there were quite a dozen people whom Winston did not even know by name"

---

> **80fj0348i** · 2026-11-02T18:17:29.000Z　
> That's already been a problem ever since people figured out you can recover voice from watching the subpixel vibration of objects within a room. (Video: https://www.youtube.com/watch?v=eUzB0L0mSCI)There is a reason secure activity happens within secured rooms built to a specific standard https://en.wikipedia.org/wiki/Sensitive_compartmented_inform...

---

> **0x4e** · 2026-11-02T18:54:15.000Z　
> Thought of the same! Cue George Orwell facepalming in his grave.

---

> **aarushyadav** · 2026-11-02T18:38:38.000Z　
> Yup those are pretty cool too! How do you feel about quiet whispering vs completely silent? Genuinely curious we haven't asked too many people

---

> **aarushyadav** · 2026-11-02T18:13:08.000Z　
> Looking into it

---

> **dang** · 2026-11-02T18:09:07.000Z　
> (Don't worry, we're not going to ban you.)A tasteless sex reference is one thing, but shallow-curmudgeonly dismissal of new work is the real sin here!

---

> **polyterative** · 2026-11-02T18:07:49.000Z　
> Says right in the description that they are using radio

---

> **jedberg** · 2026-11-02T18:34:57.000Z　
> The whole paragraph above explains it. Radio through your head.

---

> **hirako2000** · 2026-11-02T18:11:57.000Z　
> Sensorimotor debility is a thing.
> This gadget surely won't help with it.

---

> **HIP_HOP** · 2026-11-02T18:12:09.000Z　
> Yeah, so a recent study discovered that talking silently makes other people harder to hear you so they think they have problem hearing.

---

> **aarushyadav** · 2026-11-02T18:34:28.000Z　
> No, the RF is very low power and can safely be active on your face for long periods. We've done a lot of investigation and verification with safety. While doing R&D the first 2 months we collected hundreds of hours of data on ourselves with various configurations, so we made sure it was safe before :)Also, the RF transmission only activates when you're actively dictating.

---

> **aarushyadav** · 2026-11-02T18:37:46.000Z　
> Yes, it requires internet access

---

> **aarushyadav** · 2026-11-02T18:39:27.000Z　
> Yup, Q.ai is different tech and we have our IP :)They use speckle patterns of a laser shone onto the skin, which is sensitive down to tens of nanometers. Pretty cool tech

---

> **aarushyadav** · 2026-11-02T18:39:58.000Z　
> It's not :)

---

> **aarushyadav** · 2026-11-02T18:31:56.000Z　
> Fair feedback, will take into account. Looking to change up the site quite a bit soon!

---

> **aarushyadav** · 2026-11-02T18:29:31.000Z　
> Yep, I agree. Noise cancellation is a feature we want to release at some point in the future. Using the RF to denoise a very noisy audio signal which has you speaking in it. And we'll release an SDK as well a few months after shipping to build stuff on top of it!

---

> **TZubiri** · 2026-11-02T22:57:31.000Z　
> >The really cool stuff will be the applications on top of `subvocal` though at least in my opinion.It seems that so far they envision this to be an input device for existing computing devices rather than as a computing device with its own OS and apps.. at least for now

---

> **xur17** · 2026-11-02T18:29:08.000Z　
> People with prescriptions can just get versions with prescriptions in them (this is a thing for "smart" glasses already).

---

> **philsnow** · 2026-11-02T18:35:13.000Z　
> half of the other people in the office in the video are wearing prescription glasses

---

> **darkstar999** · 2026-11-02T18:42:24.000Z　
> A casino would have no problem seeing mouth movement.

---

> **stronglikedan** · 2026-11-02T19:15:09.000Z　
> > This does not bode well for casinos.For about 15 minutes until they figure out what's going on, take those folks out back and "convince" them to spill the beans on how it work, then come up with a way to detect and prevent it moving forward.

---

> **intrasight** · 2026-11-02T18:29:58.000Z　
> I did research in this space about eight years ago. Our approach was to look at deformations in the ear canal. Rumor has it that Apple AirPods will have sensors in the ear canal. I was hoping to use those sensors with our app, but it looks like Apple is not going to provide access to the raw sensor data. I expected Apple is going to support subvocal speech pretty soon.

---

> **aarushyadav** · 2026-11-02T18:34:53.000Z　
> Of course! Privacy is important!

---

> **aarushyadav** · 2026-11-02T18:49:02.000Z　
> Not sure, but definitely sounds interesting! I do know there was one company trying to use mmWave RF to track patient vitals like breathing patterns and heart rate without having anything hooked up to / touching them

---

> **aarushyadav** · 2026-11-02T19:07:25.000Z　
> The glasses will have open ear speakers similar to meta glasses! We plan to make our own agent harness and connect it native with the glasses. I have meta glasses but rarely use the AI since it's weird to talk out loud to ask it things when I'm out. This is how we want to solve it

---

> **skinfaxi** · 2026-11-02T20:36:04.000Z　
> Might not even need buds. I have watched movies on XReal glasses with the sound fairly loud to me next to other people and they didn't notice a thing (I asked them to be sure).

---

> **zoeysmithe** · 2026-11-02T22:32:57.000Z　
> I feel like this reflects the movie Her (2013). This solves the input problem better than speaking out in public, especially on a crowded train.I do think seeing an email on a smartglasses lens is better than hearing it read to you. So I can see this as just an input device, but the outputs don't have to be sound back to you.I'm guessing they are situating themselves to be bought or at least licensed out to the big smartglasses players.

---

> **aarushyadav** · 2026-11-02T19:01:47.000Z　
> Yep, we have been quite set on nose pads to keep them comfortable. I will keep you updated with the designs!The decoding is done via a companion app on your laptop or phone in the cloud, but end to end latency is still quite fast, under 500ms usually.To begin with we don't plan to have a wake word, but rather a trigger key on your connected device that you're entering text into (pressing Alt for example), similar to Wispr Flow. We're doing some R&D into the silent speech equivalent of voice activity detection, so we have a low power basic RF detection always-on, not enough to decode speech from but enough to detect rough movement, and when it detects speech-like activity beginning to start we can trigger full sensing within tens of ms. This would likely ship as a software update a few months after shipping, though.The voice change demo is something I've thought about actually, but we never got around to doing. Might film it soon :)

---

> **j45** · 2026-11-03T01:17:05.000Z　
> Adjustable nose pads and spring loaded arms are priceless. So are hybrid metal/plastic frame that offer the best of both worlds.

---

> **sudb** · 2026-11-02T19:44:37.000Z　
> There's already open-source stuff [1][2] out there that can lipread video to transcribe text, but the word error rate is pretty high (and it may not be physically possible to get this down without doing something like subvocal and having other sensors near your face).1. https://github.com/mpc001/auto_avsr
> 2. https://github.com/amywork777/lipflow

---

> **literallyanythi** · 2026-11-02T19:52:39.000Z　
> Have you never talked / mouthed without making sounds? Never even as a kid when something made you mad and you paced around the room think-saying shower thoughts to get back at that person? Even as an adult I probably mouth a sentence or two e.g. "What the fuck is this" when looking at AI output 3-5 times a weekIt does feel a little weird to do it voluntarily when not emotional, but that'll be solved as soon as Claude fucks something up :)

---

> **natsucks** · 2026-11-02T22:42:26.000Z　
> hah yeah i tried this out as an exercise and i found it very annoying to keep up. it feels quite unnatural.

---

> **desireco42** · 2026-11-02T19:03:49.000Z　
> What you said 100%, we are brainiacs overhere so our CPU is large

---

> **chfritz** · 2026-11-02T19:52:34.000Z　
> +100 on this! My choice of glasses (and prescription) has nothing to do with my choice of how to talk to my computer. Don't risk failure just because you make them depend on each other.

---

> **hansonkd** · 2026-11-02T22:05:10.000Z　
> I concur!

---

> **zoeysmithe** · 2026-11-02T22:29:21.000Z　
> This isn't any different than getting your lenses put in a VR set. The price of new lenses from an online glasses store isn't too bad, especially if you can afford $500 smart glasses, and now you don't have to worry about a big bulky thing that may fall off your existing glasses.

---

> **aarushyadav** · 2026-11-03T00:34:22.000Z　
> We did consider that, but it's a bit hard to fit all the electronics well and distribute the antennas optimally and keep that consistent across people and glasses. Best to have a predictable deice we can engineer to the needs of this application!

---

> **MarcelOlsz** · 2026-11-02T18:54:02.000Z　
> I'm waiting for throat tape a la that one paper where whatever you say in your head translates to micro movements in your throat/jaw or something like that.

---

> **aarushyadav** · 2026-11-02T19:21:53.000Z　
> English only right now, plan to add support for others after shipping

---

> **ciaranmca** · 2026-11-02T19:20:19.000Z　
> 100%, I didn’t watch video or hit reserve button so didn’t realise this was a pair of glasses until I read the text on the HN post

---

> **joshdavham** · 2026-11-02T19:21:56.000Z　
> +1 to this

---

> **Tryk** · 2026-11-02T22:53:11.000Z　
> For some reason, this is 80% of github repos I come across as well. I really wonder how this can be such a blind spot.Could it be a simple lack of empathy?

---

> **AStrangeMorrow** · 2026-11-02T19:18:46.000Z　
> I mean the whole website / linked page is filled with AI generated images. Which is one thing. But very basic, obviously AI generated ones, which makes it worse. At least for me it doesn’t inspire confidence.

---

> **dang** · 2026-11-02T19:19:30.000Z　
> They're taking pre-orders. Obviously the product doesn't exist yet. The tech is real.You can like or dislike generated images (if that's what they are—I haven't looked) but this post has nothing to do with scamming anyone, and given the wealth of technical information in the thread, including a video showing the product under development, it seems like a weird claim to arrive at.

---

> **aarushyadav** · 2026-11-03T00:32:40.000Z　
> Yep. You can either just dictate silently and we can transcribe, or another feature we will likely push out as a software update is where you can speak out loud and the RF signal is used to fully and almost perfectly denoise the audio of you speaking.

---

> **pedalpete** · 2026-11-02T21:30:14.000Z　
> For those not familiar with AlterEgo - https://www.alterego.io/
> I'm not sure if they are still active or not, but it looks like their last social media post was also their first from just over a year ago.

---

> **agf** · 2026-11-03T00:22:20.000Z　
> It must be because eventually they're planning for them to be augmented reality glasses -- being both the input and output device is such a natural extension of this, they must have thought of it.

---

> **aarushyadav** · 2026-11-03T00:30:45.000Z　
> Glasses are a great way to provide output back, via an AR display, and also offer more real estate to fit the electronics and antennas in.

---

> **ethanpil** · 2026-11-02T21:32:40.000Z　
> Same question. Where will my data go? Mac support? Linux? Windows? Lots of unanswered questions...

---

> **vfosnar** · 2026-11-02T21:32:56.000Z　
> And can I connect them to a custom server if I wanted to / how locked down will be the sw running on them?

---

> **cluckindan** · 2026-11-02T23:10:57.000Z　
> Or people with laryngeal cancer, people who temporarily/permanently lost their voice, people in extremely noisy environments, people who need to stay quiet while communicating (military/surveillance/hunting)

---

> **aarushyadav** · 2026-11-03T00:29:39.000Z　
> When we launch, no, it will be cloud inference, but will be processed with encryption in hardware isolation and only retained and used for anonymized training with your consent. At some point in the future we may make models available for local inference though.

---

> **RonanSoleste** · 2026-11-02T23:30:04.000Z　
> That. And i can speak English but its not my main language.
> Without it working on other languages just as well its a solid never for me.

---

> **Tanath** · 2026-11-02T23:54:33.000Z　
> Non-ionizing RF radiation is safe and can't do anything to you, except maybe warm you up a bit.

---

> **hmokiguess** · 2026-11-02T17:32:36.000Z　
> Apologies, I edited, can you tell me if my edit is ok? EDIT: happy to delete and repost my edit instead too

---

> **aarushyadav** · 2026-11-02T17:41:50.000Z　
> Lip reading is one of the other modalities we tried as well beyond IMU, EMG and RF! We worked a lot on fine tuning Auto-AVSR, one of the most commonly used open source lipreading models. It's very enticing to work on, since it gets to about 17% word error rate, which looks good enough that you would think working on it further would get it down to product quality, but we found there's an information-theoretic limit on the modality. Speech has 40 phonemes, but only about 12 to 15 visemes (externally visually separable phonetic states). For example P and B look very similar from a camera. This causes the scaling laws on lipreading to flatten out at an error that's too high to be product ready but just low enough to make for a good demo. Our original plan was actually to ship a lipreading software to see if people would want this behavior, but we realized you couldn't make lipreading work!

---

> **aarushyadav** · 2026-11-02T18:18:19.000Z　
> No throat mic, the first image uses EMG (muscle electrical signal) sensors. A throat mic only works if you're still actually whispering (not fully silent) and is also a weird form factor for a consumer device, which is why we didn't go with it!

---

> **bronxpockfabz** · 2026-11-02T17:50:54.000Z　
> In this case, I think the problem to solve is ergonomic issues with the keyboards used for typing

---

> **hk__2** · 2026-11-02T18:05:37.000Z　
> It depends on what you’re typing. If you’re coding, it’s probably faster to type `{}[]();|` or 2,450,712 than to say it.

---

> **derefr** · 2026-11-02T18:05:15.000Z　
> For some reason AI coding agents seem to think a README should be a Product Requirements Document (PRD).I think it's because most projects don't have any settled place (or at least, any place that lives inside the project's source-code repo) to record PRD-like information.But because AI coding agents really do benefit from having PRD-like info (i.e. a hierarchical breakdown of the "intended what" and "intended how" of the system that "should" exist in the repo, kept updated to reflect changing ideas about those intentions), they really want to record that type of info somewhere, so they can then reference it.AI coding agents don't seem to have any "taste" (or maybe "confidence"?) when it comes to asserting that even if you don't already have a separate PRD-like file in the repo, you should have one, if you want the agent to do its job well, and so it would request you to let it create one (or just automatically do it.) Instead, they just shrug and cram the PRD stuff into whatever structure you do already have. Which, if you're starting fresh with a greenfield project, is usually just a README.(I hypothesize that if you tell an AI coding agent to use Behavior-Driven Development [BDD] on a greenfield project, it'll probably lean toward maintaining its PRD-like info in the form of BDD test cases. Haven't tried this experiment yet; would be interested to know the outcome!)

---

> **dist-epoch** · 2026-11-02T17:50:26.000Z　
> What about something like a baseball cap instead of glasses? Or some sort of head band?

---

> **dang** · 2026-11-02T17:56:14.000Z　
> Wow that's fascinating. I've added that bit to your text above - I hope that's ok! It answers what was emerging as a sort of mini-FAQ.Edit: the more that I think about it the cooler and more important this feature seems!

---

> **2d975cf6** · 2026-11-02T18:17:42.000Z　
> I've been trying to manifest a product like this for a year or two, ever since I really learned what silent speech was (related, but a different speech inference method - the other month I read a paper about using cracks in a graphene nanomesh to deduce words[0]) - this sounds awesome! However, like another commenter[1] said, the glasses are where you lose people IMO. Consider a chic necklace or choker? :-)[0]: https://doi.org/10.1038/s41467-025-68228-9[1]: https://news.ycombinator.com/item?id=50340401

---

> **aarushyadav** · 2026-11-02T18:08:18.000Z　
> There's subtle changes in internal speech muscles as well often for those kinds of movements, and where it does seem ambiguous language context is usually enough to distinguish

---

> **jefftk** · 2026-11-02T18:54:12.000Z　
> Vowels definitely require tongue movement! Leave your mouth closed and whisper "a-e-i-o-u" and you can feel your tongue moving.Vowels change the shape of your mouth's cavity to change which frequencies to emphasize ("formants") and we hear the differences in vowels by analyzing those formant patterns.

---

> **qwertygnu** · 2026-11-02T18:05:05.000Z　
> Your example proves their point perfectly. You shouldn't delegate wishing your grandma happy birthday to a fucking AI agent. And you should feel ashamed for doing so. And you should feel the social pressure to hide that fact if you do resort to it.While this tech doesn't feel quite as dystopian as most recent AI innovations, I do think it is a further step in the direction of human disconnection.

---

> **233mhz** · 2026-11-02T18:15:49.000Z　
> Aha what a loser thing to do, I personally have a fleet of 347 agents running 24/7 talking to my parents, siblings, grandparents, friends, asking them how they're doing and wishing them a happy birthday when the time comes. I can finally focus on the important things!

---

> **internet_points** · 2026-11-02T18:29:28.000Z　
> Haha, I can't tell if this is a parody or not

---

> **achandra03** · 2026-11-02T18:11:04.000Z　
> > talking things out tends to flow more naturally,I've found the opposite. Typing feels much more "deliberate", and of course you can hit backspace but you can't un-speak a word. With prompting, I've found that, in general, speaking leads to lower-quality results than typing.

---

> **chicagobuss** · 2026-11-02T18:23:33.000Z　
> When I try talking for prompting my coding agents, I'm always severely disappointed with the specificity of the prompt. It's just much easier for me to "talk about" coding specifics with a keyboard than it is for me to speak about them, for some reason.I suspect this has to do with the nature of the work you're doing; I dunno, just count me firmly in the camp of people who only rarely feel like I can express a thought sufficiently for coding agents with their voice.

---

> **LorenPechtel** · 2026-11-02T18:28:57.000Z　
> Yeah, we have a lot of experience with typing while our eyes and mind are occupied elsewhere. But I've noticed the years have slowed my typing.

---

> **briandw** · 2026-11-02T18:34:07.000Z　
> I'm dyslexic and while I can type fairly quickly it's always a struggle to get the spelling and typing mistakes fixed. Talking is a much more natural way to express myself. The frustration of not being able to spell the word that I want doesn't exist. Mis-transcription errors are of course an issue, but those are getting fewer and fewer.

---

> **kqp** · 2026-11-02T18:44:15.000Z　
> Also, speech is probably bottlenecked by speed of thought, not making the sounds. I recall some study showing that data rate is pretty consistent between languages, despite wpm varying significantly due to language verbosity. You can try it yourself: try to quickly repeat “one two three four five” then try to read a paragraph out loud as quickly as you can, I bet you can feel the first strain your muscles and the second your brain, and I bet the first blows your typing wpm out of the water.

---

> **heurist** · 2026-11-02T19:13:03.000Z　
> Hard to paste in 2k words of context when you're talking. I don't think voice is the solution for most people who need to communicate heavily with AI.

---

> **1shooner** · 2026-11-02T19:53:58.000Z　
> But what you're calling 'talking things out' I consider to be forming thoughts. I want to do that myself upstream of the LLM. I don't want to pay per token for my half-baked stream of consciousness.

---

> **mrngld** · 2026-11-02T18:19:49.000Z　
> This has been an interesting thing for me to watch as it's such a case of people having widely different experiences. I'm sure people that didn't grow up on a keyboard like me can probably talk quicker than they type, but even aside from me being a fairly good typist my speech is held up by being a bit more halting, a bit more of backtracking on word choice, sometimes not quite the same 'voice' of writing as I'm aiming for, all of which obliterates any speed advantage it'd have for me.But happy to see people get more options.This reminds me of Eternity's End by Jeffrey Carver and the implants they had. Released in 2000 but the more time goes on the more the neural implant technology is coming about. To be fair I think Enders Game had similar tech to detect subvocal speech like this product.

---

> **lstodd** · 2026-11-02T18:20:02.000Z　
> Writing also filters the useless crap that is spoken but is not worth writing down.

---

> **rickydroll** · 2026-11-02T18:10:40.000Z　
> You need to train yourself to speak written speech. When you do that, the thought processes behind typing your words activate, and your language use changes.

---

> **joshgachnang** · 2026-11-02T18:36:11.000Z　
> Ahhhh exactly! I've wanted this since I was a kid and read those books.

---

> **spiderice** · 2026-11-02T19:34:34.000Z　
> CMD+F EnderThat's exactly where my mind went. Something I've wanted ever since I read that book a couple decades ago.

---

> **flanbiscuit** · 2026-11-02T23:24:24.000Z　
> I had forgotten about that!My first thoughts was Cory Doctorow's Down and Out in the Magic Kingdom. They call is "subvocal" or "subvocalizing" in the novel as well. Not saying he came up with the term though, just pointing it out.You can read the whole thing for free on his website:
> https://craphound.com/down/Cory_Doctorow_-_Down_and_Out_in_t...

---

> **garrettgarcia** · 2026-11-02T23:33:48.000Z　
> I've been wanting to have a subvocal interface to a voice assistant ever since reading about Ender talking to the AI Jane as a kid. After Alexa came out, I encouraged my employer to develop the technology, but they didn't. I'm so happy to see people are working on this finally! Scott Card was a prophet.

---

> **wumms** · 2026-11-02T19:08:09.000Z　
> For me: whispering = evolution, silent = revolution. I'd like to see some studies demonstrating its safety.

---

> **aarushyadav** · 2026-11-02T19:10:10.000Z　
> this should be fixed now!

---

> **sixtyj** · 2026-11-02T18:26:15.000Z　
> This wasn’t meant as a hate. Sorry if it sound so. I really like them, I would buy them. Immediately. Sign me in.But I think (and see) that people prefer boring tech. Whisper glasses is amazing. But most people will probably find it creepy. (Pareto applied.). I hope I am wrong. These guys are like from sci-fi.

---

> **conductr** · 2026-11-02T18:34:36.000Z　
> Can, but as a new product it is going to limit their adoption rate by some pretty significant amount.

---

> **spiderice** · 2026-11-02T19:39:28.000Z　
> You've been watching too many movies. Casino's are going to risk getting shut down in 2026 to "convince" random people of anything.

---

> **georgemcbay** · 2026-11-02T21:26:41.000Z　
> Casinos (real ones, anyway, not talking about illegal secret game rooms) don't really beat people up anymore.That said, this also won't be a problem for casinos. They have very advanced anti-cheating systems these days.The corporate casino security teams will know about this before it becomes widely available and will institute policies to lifetime ban anyone they detect using this tech, which they will fairly easily be able to do because of how much automated surveillance there is in any real casino.In any case, there are way more subtle signaling mechanisms people can use (but probably also get caught using) to collaborate that don't involve someone suspiciously silent talking right in front of a dealer.

---

> **aarushyadav** · 2026-11-02T18:45:39.000Z　
> From my understanding decoding via ear deformation requires the mouthing to be quite exaggerated. I am also looking forward to Apple launching it soon though, hopefully it gets more people excited and aware about the category at least

---

> **genxy** · 2026-11-02T20:51:43.000Z　
> > own agent harnessI would not use this, I only want to use the glasses as an IO device. You must provide the ability to use the glasses as a regular BT headset.

---

> **vessenes** · 2026-11-02T19:05:12.000Z　
> Super cool. For a cool voice change demo we'll allow a gb200 over low latency wifi :) elevenlabs has deals with a number of professional actors and voice actors for licensed uses, seems like you could probably find an ethical and cool co-brand opportunity in there.Have fun building this! It's worth doing.

---

> **IHLayman** · 2026-11-02T20:25:39.000Z　
> Wait. You are taking the RF response, sending it up to the cloud to interpret, and then sending the result back? Hard pass from me, sorry. Cool tech, but I don’t want my internal thoughts anywhere near the cloud. Also, this would mean I couldn’t use something like this on the subway when the phone signal goes out intermittently, right?

---

> **ComputerGuru** · 2026-11-02T22:02:12.000Z　
> I just want to say 500ms isn’t fast.

---

> **OJFord** · 2026-11-02T23:55:00.000Z　
> Yeah it is, because now the typing glasses are an appliance, not just your regular glasses. This makes sense for VR headsets, but it's a large part of how popular Google Glass is today.GP is saying their choice of the glasses they want to wear all day every day is nothing to do with their choice to have something transcribe words they mouth, the latter shouldn't decide or significantly restrict the former.

---

> **ipsum2** · 2026-11-02T19:22:46.000Z　
> Et tu, dang?You don't see how this is misleading or fradulent (i.e. definition of a scam) in any way? A realistic image of someone wearing the glasses that don't exist yet, without disclosing it?

---

> **lern_too_spel** · 2026-11-03T01:14:22.000Z　
> Headphones are also a great way to provide output back, and people are already used to wearing headphones in environments where speaking to their device doesn't make sense. You can put antennas in a boom, and nobody would bat an eye because many headphones already have boom mics.

---

> **sexy_seedbox** · 2026-11-03T00:23:57.000Z　
> I'm not sure this works for Cantonese or other tonal languages.

---

> **randomImmigrant** · 2026-11-03T00:27:38.000Z　
> Yeah and warming up my eye/brain isn’t a pretty thought. Head impacts brain function, and the last thing I want is a part of my brain getting more sustained heat than the rest.

---

> **dang** · 2026-11-02T17:35:37.000Z　
> It's better. I've turned off the flag.

---

> **zie** · 2026-11-02T17:56:12.000Z　
> Any deaf/HoH person who has tried to do lipreading could have told you all of this too.Good luck on the project!

---

> **theturtletalks** · 2026-11-02T18:07:01.000Z　
> Now that is insightful! The demo definitely fooled me and even the first repo requires you to train the model.Lip reading AI would be pretty big since privacy would probably go out the window.

---

> **altcognito** · 2026-11-02T18:33:14.000Z　
> Why not a pencil in the ear or something you can put in a shirt pocket? Or even earbuds?

---

> **tmsh** · 2026-11-02T18:50:20.000Z　
> but can't a decision model or some other model deduce "P" or "B" based on the context (i.e., previous words said)?reminds me of tesla fsd v. waymo. may be a market for both? i.e., camera-only or camera + specific hardware.

---

> **paisawalla** · 2026-11-02T19:22:03.000Z　
> I'll defer to your expertise on what people find weird, but it seems like you should be able to have a throat-based device that could hide under a shirt collar. I have the Meta Ray Bans and even though I love the functionality, I don't care for the bulky frames. And those are designed by Ray Ban, meaning they're presumably at the upper end of what can be done stylishly.

---

> **assumed_throwaw** · 2026-11-02T18:34:02.000Z　
> I have some news for you about typing code by hand...

---

> **LatencyKills** · 2026-11-02T18:13:28.000Z　
> That is exactly what happened in this case; the readme was the PRD.Throughout the document Claude kept claiming that issues were "mitigated but not fixed". They were essentially bandaid fixes for things it couldn't figure out. When I pointed this out to the author he said, "Well Claude thinks it works."I wonder what happens to software when enough people try to ship projects like this.

---

> **aarushyadav** · 2026-11-02T17:51:20.000Z　
> Exploring that too as a next product, but probably a while down the line!

---

> **hk__2** · 2026-11-02T18:08:47.000Z　
> Well you both prove each other’s point ;)

---

> **augment_me** · 2026-11-02T19:50:16.000Z　
> As long as the ROI from social relationships(inheritance, friendship favors, dating/mating potential, etc) can be upheld using less effort, such as language models, its a no-brainer and you lose out to competition if you don't do it.

---

> **jryle70** · 2026-11-02T23:41:17.000Z　
> Are you saying you've never texted happy birthday to anyone? or people doing so should be ashamed? or it's ok to type the message on the phone but not saying it?

---

> **cogythea** · 2026-11-02T18:13:48.000Z　
> The bit before your quote was> with many peopleNot everyone. I, at least, definitely overthink what I type, and while I end up with nice-ish sentences in my prompts it takes a lot longer than a train of thought that the AI parses correctly most of the time anyway.

---

> **walthamstow** · 2026-11-02T19:03:43.000Z　
> I was surprised to find after using dictation heavily all year that I actually talk a load of rubbish when I'm speaking, using all kinds of cliches and fillers and saying way more than was needed.

---

> **gavinray** · 2026-11-02T20:17:39.000Z　
> My spouse and I have a rule that if we think a discussion is going to be emotionally charged, we have it over text in different rooms.It sounds autistic, but writing and reading allow you to be much more precise, careful, and deliberate with your words and helps reduce impulsive outbursts.This has worked really well for us, as crazy as it sounds.

---

> **sadilek** · 2026-11-02T20:22:40.000Z　
> I guess it depends on how close to the code you want to work. I find that I lately talk only about the features and UX and can leave the coding details completely to the agent. That might not work in every project, but I suspect it might work more often than people think because it's hard to adapt to the quickly increasing capabilities of LLMs.I think a good habit is: Try to make the agent fail at least once a week with a too ambitious request. This got surprisingly hard lately :)

---

> **1dom** · 2026-11-02T18:25:17.000Z　
> > This has been an interesting thing for me to watch as it's such a case of people having widely different experiences.Same. I'm often told I talk too fast, but I feel I communicate slowly because a lot of my fast speech involves halting and backtracking and such.I can easily type 100WPM+, but I trivially blast out a few paragraphs of perfectly adequate text in a few seconds and then spend a few minutes re-editing it.

---

> **jbs789** · 2026-11-02T18:16:58.000Z　
> How?

---

> **lstodd** · 2026-11-02T18:18:00.000Z　
> Why bother when old ways work _and_ there is no benefit? Or name one.

---

> **1dom** · 2026-11-02T18:21:14.000Z　
> As a person who often talks far too fast and incoherently, but types generally fast and legibly, I had never recognised or even considered this, but it seems helpful. Thanks.

---

> **viraptor** · 2026-11-02T22:11:26.000Z　
> If I remember the details correctly, the AI-like entity optimised the communication to subvocal, but his wife felt disconnected, noticed him turned away in bed whispering to the AI.There's some lesson there...

---

> **settsu** · 2026-11-02T19:14:54.000Z　
> Confirmed!

---

> **dang** · 2026-11-02T19:30:46.000Z　
> I appreciate the kind reply!A comment like the GP quickly pattern-matches as snark and dismissal because those are so common on the internet. In other words, if you don't intend your comment that way, you need to do something to disambiguate this. Your follow-up comment does this nicely.The reason this happens is that we all tend to take our intent for granted and forget that it exists in our head and isn't accessible to others unless we make it explicit. https://hn.algolia.com/?dateRange=all&page=0&prefix=true&que...This also leads to a fascinating (to me at least!) phenomenon where the reply to a moderation comment (i.e. your follow-up here) makes explicit the thought which the commenter meant to communicate. What's fascinating is how different this is from what they originally posted. I call this the rebound effect. https://hn.algolia.com/?dateRange=all&page=0&prefix=true&que...

---

> **aarushyadav** · 2026-11-03T00:31:51.000Z　
> Fair enough! We take data security and privacy very seriously and have built many safeguards to prevent even us from accessing the raw data in the cloud. At some point in the future we hope to launch local inference models too!

---

> **aarushyadav** · 2026-11-03T00:30:06.000Z　
> Yes, this is the unoptimized speed while we are in development. We are working hard to make it much faster for production!

---

> **thaeli** · 2026-11-03T00:33:08.000Z　
> Yeah, my glasses are a substantial part of my personal style and I'd be sad to have to go back to something generic looking. It's been a minus with other smart glasses as well.Also I need to wear safety glasses with side shields frequently and would really rather be able to integrate there. Particularly relevant here since that's also in noisy environments where regular speech recognition struggles.

---

> **dang** · 2026-11-02T19:24:04.000Z　
> Scam in this context would mean selling people a product or technology that won't ever exist. This is the opposite of that.

---

> **mpeg** · 2026-11-02T21:00:21.000Z　
> That's every product launch ever... if it's not been built yet, you're always looking at a render/photoshop/fake

---

> **LoganDark** · 2026-11-03T00:43:33.000Z　
> I think you vastly overestimate how much heating would be at play here. There was a youtuber that cracked open a microwave and put himself and some other things directly by the magnetron while it was running. It turns out that without the metal box bouncing the microwaves back over and over, they're already way less effective, and I highly doubt that smart glasses would emit even a tenth of the power of a microwave.https://www.youtube.com/watch?v=3hBRxwQXmCQ

---

> **aarushyadav** · 2026-11-02T19:09:17.000Z　
> Not well enough! You can get to 15-20%ish WER but going beyond that doesn't seem feasible with the info available from a camera, even with a great language model

---

> **kennywinker** · 2026-11-02T21:41:59.000Z　
> > Meta Ray Bans and even though I love the functionalityWhich functionality do you love? Is it the nonconsensual recording? Or maybe the giving away your own privacy and the privacy of everyone around you to one of history's least-trustworthy companies?

---

> **Lerc** · 2026-11-02T18:06:46.000Z　
> How about a cap with a propellor on it that spins when receiving words :)

---

> **achandra03** · 2026-11-02T19:54:57.000Z　
> Yes, of course I wasn't trying to speak for everyone. Just my personal experience :)

---

> **dr_hooo** · 2026-11-02T19:24:49.000Z　
> Same experience. Faster, but also much more filler.

---

> **achandra03** · 2026-11-02T19:54:18.000Z　
> Yes, I feel very similar. Maybe it's just that my verbal intelligence is lower than average but it feels that the signal to noise ratio is much lower when I speak off the cuff vs when I type.

---

> **esseph** · 2026-11-02T21:25:24.000Z　
> > My spouse and I have a rule that if we think a discussion is going to be emotionally charged, we have it over text in different rooms.I've done this myself with my wife and I.> It sounds autisticWell, I'm autistic, and she has a very high traumatic intelligence. She reads my body language, expressions, movements more than what I say, and those are very easy to misinterpret or overinterpret. And she says things... but it's not actually what she means. By us writing/typing things out, we're able to communicate without stray signals creating noise.

---

> **rickydroll** · 2026-11-02T19:44:18.000Z　
> One approach is reading your and other people's written speech out loud. Pay attention to where it feels awkward; for me, that was the direction I needed to practice. A trick that I use currently to reinforce speaking written speech is using Grammarly to make corrections, which I try to internalize.Another trick is don't correct words and letters. Say the sentence you really meant to say. It is not uncommon for me to say a thought or a concept two, three, four times in a row as I'm wrestling with what the language should be on the written page.

---

> **Infiniti20** · 2026-11-02T23:57:12.000Z　
> Which of the books is this? I only ever read the first

---

> **throwaway27448** · 2026-11-03T01:06:56.000Z　
> The politics of using technology in social circumstances is an emphasis for sure. I'm specifically thinking of Olhado recording Marcão's physical abuse of Novinha with his bionic eye.

---

> **sixtyj** · 2026-11-02T20:03:51.000Z　
> You are absolutely right. After 30 years on the internet I should have known it.Nobody knows you are a dog. And… don’t make jokes as everybody reads them in different ways…

---

> **snackbroken** · 2026-11-03T01:13:12.000Z　
> Respectfully, talk is cheap. Every company says they take security and privacy seriously even after their database has been breached and their customers' plaintext passwords and credit card details have become public information.If you were actually serious about prioritizing privacy above securing an ongoing service relationship you would ship local inference as the default and only (possibly later) offer a cloud service as an optional add-on for those who want/need it.

---

> **ipsum2** · 2026-11-02T19:24:53.000Z　
> If they don't deliver the product in the image they've shown, Q1 2027, will you admit its a scam then? What would it take?It's absolutely clear that if they're using AI generated images, they haven't even gotten a physical design of the product they're trying to sell.

---

> **tmsh** · 2026-11-02T22:29:19.000Z　
> Cool thanks for the reply. And congrats on the launch here.

---

> **viraptor** · 2026-11-03T00:43:10.000Z　
> It's from Xenocide. It was between Ender and Novinha.

---

> **dang** · 2026-11-02T19:42:15.000Z　
> You're condemning them for spending all their time making the product work instead of...focusing on their website? Bit strange to call someone a scammer for doing the opposite of what scammers do.

---

> **floren** · 2026-11-02T21:12:40.000Z　
> On the other side of it, I've been following Brilliant Labs' Halo smartglasses since they were announced last summer, with a shipping date of "November 2025"... which soon became "Q4 2025", then every two weeks since then has been another delay. As of October we finally confirmed that nearly a dozen people had received units.So yeah, I don't think it's unwarranted to be skeptical when somebody shows an AI render and says "we'll ship this within 6 months".

---

> **ipsum2** · 2026-11-02T21:35:21.000Z　
> let's circle back q2 2027 when these glasses are delivered to you.

---

> **jryle70** · 2026-11-02T23:46:06.000Z　
> Skepticism about shipping date is normal, especially for something novel and hard. Calling people fraud without evidence is just bad.

---

> **ipsum2** · 2026-11-03T00:55:08.000Z　
> AI generated imagery of their product, without disclosure is not evidence?

## 关联链接

- https://drive.google.com/file/d/1ks0dS0eZiTV9EqSFsyB_w5BBjpc...Since
- https://drive.google.com/file/d/1mwhv5HZMz3UTevdrgwS5O7g2jWV...We
- https://drive.google.com/file/d/1rhzNFpdDzr7oHk0isFY70dkoV4C...This
- https://subvocal.co/preorder!
- https://www.youtube.com/watch?v=9QdX1eObVYI(Edit:

## 导航

- 项目页：[[10-项目/subvocal.company_de6b8c76]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
