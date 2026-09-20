---
type: "corpus"
item_id: "b6a5a0f6057541b4"
title: "Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49711544"
project_url: "https://github.com/arnegiacomo/fugleramme"
author: "arnemunthekaas"
published_at: "2026-09-15T12:31:10Z"
captured_at: "2026-09-21T01:40:47+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_arnemunthekaas
  - story_49711544
  - show_hn
metrics: {"points": 2355, "comments": 259, "engagement_velocity": 2355}
comments_count: 245
comments_total: 259
discovered_via: "hn:show_hn:90d"
---

# Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

> [!info] 一句话导读
> arnegiacomo/fugleramme

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49711544>
> 指标：点赞=2355 · 评论=259 · engagement_velocity=2355
> 作者：arnemunthekaas　|　发布：2026-09-15T12:31:10Z
> 项目链接：<https://github.com/arnegiacomo/fugleramme>
> 采集：2026-09-21T01:40:47+08:00　|　id：`b6a5a0f6057541b4`

## 正文

# arnegiacomo/fugleramme

E-ink bird frame for Raspberry Pi - real-time bird detection by audio using BirdNET-Go

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 5
- License: MIT License
- Default branch: main
- Created: 2026-07-08T19:01:49Z

## Languages

- Python
- Shell

## Topics

- bird-detection
- birding
- birdnet
- birdnet-go
- birdwatching
- e-ink
- inky-impression
- kiosk-software
- machine-learning
- raspberry-pi

## Top Contributors

- arnegiacomo (46 contributions)

---

## README

# fugleramme
E-ink bird frame for Raspberry Pi - real-time bird detection by audio.

Built on top of BirdNET-Go, which runs
the mic and the BirdNET classifier and owns all detection config. Fugleramme reads
its detections and renders the recently-seen birds as a collage on an Inky-Impression e-ink panel, and serves the same view as a web kiosk.

## Art

The birds are cut-outs from historic, public-domain natural-history drawings,
hand-curated for this project. Each detected species is matched to its
illustration, background-removed, and packed onto a textured paper page - larger
birds toward the centre, sized by real body mass. Species with no illustration
are currently left off, and an empty window shows a bare perch.

| No detections | A few visitors | A full garden |
| :---: | :---: | :---: |
| No birds detected | A few garden birds | Many garden birds |

## Run locally

```bash
uv sync                                       # set up venv
uv run python -m fugleramme.seed --count 40   # seed db (no BirdNET-Go in dev)
uv run fugleramme-frame                       # start service on :8080
uv run fugleramme-dev                         # same as above with hot-reload
```

Open the kiosk (no SPI-panel needed):

```bash
open -na "Google Chrome" --args --kiosk --app=http://localhost:8080/
```

## Run on a Raspberry Pi

Clone the repo on the Pi and run the idempotent one-command bootstrap:

```bash
./setup.sh          # add -y to auto-accept dependency installs (uv, docker, etc...)
```

It installs any missing deps, brings up BirdNET-Go (container + mic), and enables
the frame as a systemd service that pushes to the Inky panel and serves the kiosk
on `:8080`. Details: `detector/README.md`.

Want to update? Just pull and run ./setup.sh again

## License

- Code (`wikimedia-scrape/`, application code): MIT - see `LICENSE`.
- Bird images (`assets/birds/`): CC BY-SA 4.0 - see
 `assets/birds/ATTRIBUTION.md`.
- Bird sizes (`assets/bird_sizes.csv`): body mass from AVONET (Tobias et al.
 2022, Ecology Letters, doi:10.1111/ele.13898),
 CC BY 4.0.

## 评论（245/259）

> **arnemunthekaas** · 2026-09-15T12:31:25.000Z　
> Author here. A mic listens to the sounds in my garden, BirdNET-Go (an open-source BirdNET classifier) detects birds by sound, and the e-ink frame draws a real 1800s natural-history illustration of each one as it hears them. Here’s a live web-demo from my garden in Bergen, Norway: https://fugleramme.arnegiacomo.devA few things that might be interesting:- The screen only redraws when the set of birds changes, and dithers the collage down to six colours for the e-ink display.- Bigger birds sit toward the centre, scaled by real body mass.- 800+ cutouts across 400+ species, each cut from a real public domain plate. All art is historic and human-made. Coverage is currently best for the Nordics, Britain and Germany (but other parts of the world are in the works).- Runs fully local on a Raspberry Pi or your homelab (yes, even the classifier runs great on a RPI)The e-ink panel is optional and it can run web-only in a container against a BirdNET-Go you already have.Happy to answer any questions!

---

> **firmretention** · 2026-09-15T13:08:44.000Z　
> This is such a cool idea and I want to build one. I wish I had this kind of creativity. I can do the hardware/software side, but great ideas elude me.

---

> **mungoman2** · 2026-09-15T13:10:46.000Z　
> Now this is why I come here!Amazing thing, will replicate.

---

> **jiwidi** · 2026-09-15T13:11:31.000Z　
> Isnt this a fork* of https://x.com/WarnerTeddy/status/2060018688645115964?https://github.com/Twarner491/AvianVisitorshttps://theodore.net/projects/AvianVisitors/Or maybe im missing to see is the same author? It went viral a few months ago

---

> **fnands** · 2026-09-15T13:25:16.000Z　
> Very cool!I wish E-ink displays were a bit more affordable. The 13 inch one is £229.50.
> Does anyone know why they are still so expensive, at least at large sizes?

---

> **bronlund** · 2026-09-15T13:28:49.000Z　
> Artig! :)

---

> **practicalsystem** · 2026-09-15T13:32:16.000Z　
> oh I need to build this for my mom she would love it!

---

> **misetech** · 2026-09-15T13:38:47.000Z　
> I would like to build something which can do the exact opposite. Sounds from illustrations.

---

> **nsbk** · 2026-09-15T13:40:10.000Z　
> Very cool, but IMO not mentioning https://theodore.net/projects/AvianVisitors/ as an inspiration is a very ugly move from the author

---

> **RGS1811** · 2026-09-15T13:42:12.000Z　
> This is one of the most wonderful uses of AI I've seen in a while.

---

> **meteyor** · 2026-09-15T13:49:00.000Z　
> I love this! I have a forest garden with lots of birds. I so want to try this project asap!

---

> **lvl256** · 2026-09-15T14:00:19.000Z　
> What would be cool is if you can put AI to identify individual birds. They all have different calls/voices, though largely indistinguishable to human ears. And you can name them and see when they come for a visit.

---

> **scottndecker** · 2026-09-15T14:06:13.000Z　
> Why isn't this a thing on Amazon I can buy?

---

> **qarl** · 2026-09-15T14:07:50.000Z　
> I love this new era of AI powered creativity. I expect we're just getting started.

---

> **bix6** · 2026-09-15T14:09:49.000Z　
> super stylin’

---

> **dmitrij** · 2026-09-15T14:10:59.000Z　
> We could also leave fake images aside, go outside and try to watch the birds ourselves. Maybe even let the camera inside, just looking with our own eyes. Real nature. No intermediate.

---

> **gigantino** · 2026-09-15T14:19:21.000Z　
> Now could you make one for urban noises? (e.g. traffic, trash truck, drunk guys at 3AM etc)

---

> **poutrathor** · 2026-09-15T14:23:47.000Z　
> My granny is almost deaf and I will test the idea for her, for she loves birds

---

> **reedlaw** · 2026-09-15T14:23:55.000Z　
> Frigate, the IP camera security system, also does bird classification: https://docs.frigate.video/configuration/bird_classification...

---

> **gabzofar** · 2026-09-15T14:24:36.000Z　
> That's a blatant copy of https://theodore.net/projects/AvianVisitors/, please.

---

> **darvo31** · 2026-09-15T14:25:01.000Z　
> Love the aesthetic of 1800s illustrations combined with modern tech. Wonder if it ever misidentifies a squirrel.

---

> **joshstrange** · 2026-09-15T14:28:46.000Z　
> e-ink is so much fun, especially when combined with ESP32 or BTLE boards. I currently have 4 around my house displaying book quotes that I've highlighted in KOReader and they bring me joy each time I see them. They are simple and do one thing very well.I just got and setup a BTLE e-ink driver the other day and according to my calculations it will last _years_ on a single charge (2000mAh) even with multiple refreshes per day (crazy compared to the Wifi ones). Year+ lifetime completely changes the calculus for where to put these IMHO.I'm considering designing a multiple-screen "art" piece to hang on my wall and playing around with various ideas (on both content and design).LLMs + 3D Printer + e-ink is my new favorite hobby.

---

> **pnw** · 2026-09-15T14:35:19.000Z　
> Cool project! I set up an e-ink frame with this recently as a gift and it's been so much fun creating themed collections.https://github.com/defl/hokku_epaper

---

> **its_ajseven** · 2026-09-15T14:38:50.000Z　
> Cool Project!! I like it

---

> **Chuckles64** · 2026-09-15T14:42:18.000Z　
> What a cool idea. I might have to give this one a try. I've got Raspberry's coming out the wazoo.

---

> **_somu_** · 2026-09-15T14:50:16.000Z　
> So cool, I'm going to try building one myself!

---

> **MiloLeo** · 2026-09-15T14:50:47.000Z　
> This is such a cool project. My mom would absolutely love this if I made it as a gift. This may be a good project.

---

> **abletonlive** · 2026-09-15T14:52:05.000Z　
> incredible creativity and inspiring. thanks for sharing this !

---

> **ninefathom** · 2026-09-15T15:19:51.000Z　
> While I love this idea generally, the scope of the use of generative AI for artwork is too vague for my comfort.The README.md mentions that "no art is AI-generated, though some has been retouched with AI." Superficially, that sounds mild. Some of the other closely-related projects, however, use different verbiage, or none at all.For those of us with ethical concerns around generative AI application to artwork, much more detail may be needed before we could decide if this was appropriate for us.

---

> **jarek83** · 2026-09-15T15:42:07.000Z　
> Cool project!On a side note. How do people deal with all the ugly mess birds cause in such settings? I'd love to have such thing but seeing all the white stuff on glass door does not really feel fun to me overall.

---

> **rogerb** · 2026-09-15T15:43:14.000Z　
> Super fun project!

---

> **thesurlydev** · 2026-09-15T15:45:06.000Z　
> Very cool!I can't help wonder what this would look like for humans. Imagine, set one of these up at a party and it has the means to identify anyone on the invite list. When it hears the person it displays a photo, brief bio, and relationship status.

---

> **hugoj0s3** · 2026-09-15T15:47:32.000Z　
> intresting!

---

> **mandycult** · 2026-09-15T16:02:43.000Z　
> This is the sweetest thing I've seen in a long time :')

---

> **pokerpatioteam** · 2026-09-15T16:11:43.000Z　
> cool project!

---

> **sailfast** · 2026-09-15T16:14:53.000Z　
> I just happen to have an extra Pi and an e-ink display sitting around and I LOVE this idea. Going to try it on my screened in porch - we typically get 10-20 Merlin detections on a decent day so this could be fun!

---

> **physhster** · 2026-09-15T16:18:55.000Z　
> All I'd get is pigeons and seagulls...

---

> **hodder** · 2026-09-15T16:19:34.000Z　
> Amazing. Best post I've seen on HN in ages.

---

> **theturtletalks** · 2026-09-15T16:21:27.000Z　
> So many bird projects recently and I think it’s all thanks to this project[0]It seems IP over Avian Carriers is finally within reach!0. https://github.com/tphakala/birdnet-go

---

> **divbzero** · 2026-09-15T16:33:05.000Z　
> Any sufficiently advanced technology is indistinguishable from magic.

---

> **amelius** · 2026-09-15T16:41:31.000Z　
> What is the energy label of this frame?

---

> **mrbombastic** · 2026-09-15T16:49:12.000Z　
> this is so cool :) thinking about some remixes already with maritime traffic and tides

---

> **agcat** · 2026-09-15T16:53:03.000Z　
> Most whimsical application of local ai so far

---

> **divbzero** · 2026-09-15T16:54:29.000Z　
> The underlying classifier, BirdNET, is a traditional neural network and not an LLM:https://doi.org/10.1016/j.ecoinf.2021.101236

---

> **thomasfl** · 2026-09-15T17:19:41.000Z　
> As a fellow Norwegian I must say that this is pure art by the developer Arne Munthe-Kaas.

---

> **CobrastanJorji** · 2026-09-15T17:25:20.000Z　
> I love it.

---

> **albertgoeswoof** · 2026-09-15T17:47:49.000Z　
> I built one of these that shows the hacker news front page, nyt front page, my most listened to album of the last 7 days etc.Refreshes every hourBattery lasts a few monthsEsp32 and a colour eink panel, same as this one I think

---

> **jadbox** · 2026-09-15T19:34:04.000Z　
> This is the coolest thing on HN that I've seen in a minute. The whole thing is a perfect blend of ideas with the end result of something that feels... magical. Honestly this is the highest inspiration to me as a builder as I just want to create magical experiences, even if they are just small oddities.

---

> **lloydatkinson** · 2026-09-15T20:04:11.000Z　
> This is amazing. I want to build this. Curious about the authors “full garden” link, surely he doesn’t get that many birds in such a small space of time in his garden, unless he lives next to a park I suppose?

---

> **torcete** · 2026-09-15T20:07:12.000Z　
> People are so creative.

---

> **zero0529** · 2026-09-15T20:10:32.000Z　
> I was thinking about building this for a while and now i don't have too, insane. Thanks!

---

> **TomJansen** · 2026-09-15T20:39:48.000Z　
> This project is super cool! But the price of the e-ink board is quite steep

---

> **andatki** · 2026-09-15T20:43:32.000Z　
> Bryce Shivers and Lisa Eversman would definitely have this in their boutique. Put a Bird on It!

---

> **bilsbie** · 2026-09-15T20:46:44.000Z　
> This could totally be a commercial product. I picture it being sold with a bird feeder. Maybe it uses a camera on the feeder.Then have the screen look like a biologists notebook where he sketches the bird and writes a few notes about the time and its behavior.

---

> **manuelisimo** · 2026-09-15T20:58:28.000Z　
> I am buying an e-ink display just to try this!

---

> **thuruv** · 2026-09-15T21:07:16.000Z　
> This is an excellent execution and refreshing to see the thought process behind it. Kudos. the ideas such as these, gonna keep us swim sane and specifically extending far beyond the 9-5 is no longer sideProject category but refreshingly needed one.

---

> **smnplk** · 2026-09-15T21:07:55.000Z　
> Needs to also have an alarm clock waking you with this
> https://www.youtube.com/watch?v=-4J1zyrW_VQ&list=RD-4J1zyrW_... :)

---

> **catapart** · 2026-09-15T21:10:07.000Z　
> Awesome! It's really cool that it uses public domain images as the inspiration, too. And even cooler that you link to the places where you got those public domain images.

---

> **worklifepanda** · 2026-09-15T21:16:21.000Z　
> this is very creative, really cool idea!

---

> **simonjgreen** · 2026-09-15T21:20:50.000Z　
> I've been leveraging Birdnet-2.4 as well, but also ultrasonic-pass and activity-v1 to do broader detection with an ecological targeted microphone. This means I can capture not just bird sounds but also bats and some insects, and acoustic events such as jets and cars.Applying heterodyne transformations to the bat recordings makes them audible which is fascinating, especially when you catch them in a feeding frenzy.Similar intent with an indoor display, although nowhere near as beautiful as OPs eink display here. I'm more aiming for a real-time ticker, but this design is wonderful. I'm quite inspired by it!I've been working on this in the background for a few months, if anyone is interested repo with screenshots is here: https://github.com/simonjgreen/OpenObservatory

---

> **base698** · 2026-09-15T22:35:46.000Z　
> You should partner with Cornell Ornithology.

---

> **westoque** · 2026-09-15T22:51:54.000Z　
> ok. a similar idea, you should put a camera outside your door and do the same for passing dogs.

---

> **zzato** · 2026-09-15T22:57:35.000Z　
> coolest implementation of ai application case that i ve seens last months

---

> **yiro13** · 2026-09-16T00:03:23.000Z　
> Impressive, reminds me of this project https://theodore.net/projects/AvianVisitors/ I guess the author was inspired from there

---

> **chris_armstrong** · 2026-09-16T00:20:35.000Z　
> breaking this by putting it in earshot of a lyrebird

---

> **forcemajeure** · 2026-09-16T01:08:07.000Z　
> This is amazing, well done! It would be a great travel piece

---

> **staub** · 2026-09-16T01:17:46.000Z　
> Any easy way to get started on your own version of this without needing a mic would be to pull birds seen nearby using the eBird API and pairing scientific names. Won't be as accurate as a backyard mic, but will give you a direction to start.Also if you have old e-ink device laying around, you can likely setup BYOD with TRMNL (or just buy one https://trmnl.com/) and send the bird images as a private plugin

---

> **water-drummer** · 2026-09-16T03:39:00.000Z　
> Reminds me of Arthur's jounal

---

> **brenainn** · 2026-09-16T05:53:40.000Z　
> I would love to build one as a gift but would need to get it working for Australian birds.

---

> **redbell** · 2026-09-16T06:15:27.000Z　
> That's indeed a cool project and it's this kind of stuff that makes HN a unique corner in this digital world. I can classify this project with [1](Ranked #3 as the most upvoted Show HN of all time), [2](#4) and [3](#6) as non pure-software products that happen to also integrates hardware as well.The only thing I wish to be added is a short video showing the actual frame in action to express motion and sound so I can better feel it. While the provided image (hero.jpg) gives me a sense of the product, I just can't smell it yet. I visited https://fugleramme.arnegiacomo.dev/ hoping for a live feed but it seems just a static image.Kudos for the author and I hope we can see the next iteration!_______________1. I made an open-source laptop from scratch (https://news.ycombinator.com/item?id=42797260)2. I replaced a $120k bowling center system with $1,600 in ESP32s (https://news.ycombinator.com/item?id=48968606)3. A retro video game console I've been working on in my free time (https://news.ycombinator.com/item?id=19393279)

---

> **learner_yearner** · 2026-09-16T07:41:22.000Z　
> Wow! Every human mind is wonderful in its own way. It can come up with ideas that other minds can't even comprehend.

---

> **Lavanic** · 2026-09-16T07:44:24.000Z　
> cool proj

---

> **kris-memoket** · 2026-09-16T07:50:50.000Z　
> Really interesting!! Awesome work

---

> **mariusandra** · 2026-09-16T08:10:51.000Z　
> This is a very cool project!When I first heard of it (through a community member in discord), I wanted to see if I could replicate it on FrameOS (my software for running anything on an e-ink panel), and sure enough, I got quite close: https://scenes.frameos.net/s/bird-field-journalThis is obviously nowhere as complicated as OP's project, but I thought I'd just share that your project inspired me to build something similar too.

---

> **drum998** · 2026-09-16T08:28:36.000Z　
> Awesome! I'm in the middle of setting up a birdnet system for audio recognition, and this is the puzzle piece my project needs!

---

> **DylanMerigaud** · 2026-09-16T09:04:05.000Z　
> Nice launch, good luck out there.

---

> **gadders** · 2026-09-16T09:29:37.000Z　
> I'd buy this if I could.

---

> **techsystems** · 2026-09-16T10:09:04.000Z　
> Seems like a nice adjacent project to the magic mirror!

---

> **asdojasdosadsa** · 2026-09-16T10:24:53.000Z　
> This is amazing project, thanks for sharing

---

> **metchio** · 2026-09-16T10:25:27.000Z　
> this is amazing. really awesome

---

> **rtvn83** · 2026-09-16T11:37:08.000Z　
> This is amazing. I wonder if this could be connected to an LLM and render images of birds differently each time?

---

> **sigvef** · 2026-09-16T12:16:25.000Z　
> Came across the Samsung The Frame variant last month too! https://github.com/simenf/birdframe

---

> **simenf** · 2026-09-16T12:25:28.000Z　
> Cool project!For those of you that have a Samsung frame tv and no spare e ink screens:Inspired by AvianVisitors [1] I made a similar project [2] with an android app for bird detection using Perch, and then displays the birds detected during the last 24 hours with nice art on a samsung frame tv in "art mode".If you dont want to repurpose an old android device, my app also supports bird detections from birdnet-go and birdweather. It should be plug and play with this project.Have a look at
> [1] https://theodore.net/projects/AvianVisitors/
> [2] https://github.com/simenf/birdframe

---

> **edwardbonnett** · 2026-09-16T13:02:32.000Z　
> what's the most unusual bird it's picked up so far?

---

> **bilaly** · 2026-09-16T13:51:18.000Z　
> I am working on a voice-chat program and I implemented RNNoise this week. Most of the noise cancellation tools filter for just human voice. so bird noises that you want, may be gone when you are trying to delete the wind noise or something. And without any noise cancellation, It can be very hard to people who are living next to road or very noisy place.

---

> **ryzvonusef** · 2026-09-16T14:46:45.000Z　
> a bit of a noob in these field, so apologies for the question, but why bird.net and not the more comprehensive cornell merlin dataset?

---

> **jaackevans_** · 2026-09-16T16:13:30.000Z　
> damn this is one of best things I've seen in a while

---

> **pauleibye** · 2026-09-16T17:25:40.000Z　
> I think this is a cool idea but I would never want ai generated art on my wall.

---

> **sma3in** · 2026-09-16T20:37:23.000Z　
> well this is a AI put to great use! love it

---

> **TheGoodBarn** · 2026-09-16T21:15:04.000Z　
> This is insane.Going to google/search and stuff when I get home, but for my current living space it would be awesome if I could get a wireless mic to place outside and have this run on my Beelink SER8, and then over local network sync to my Apple TV and display the images kinda like a screensaver?

---

> **yipinwong** · 2026-09-16T21:54:06.000Z　
> Here is another "I love it" comment.Genuinely giving the OP props

---

> **jacksun788** · 2026-09-17T06:35:30.000Z　
> Cool project! Thanks

---

> **dirkc** · 2026-09-17T06:55:16.000Z　
> I love an e-ink display project!The one thing that always trips me up in projects like this is power delivery in a way that I'm happy with. I always end up having a USB cable looking awkward somewhere or being limited in where I put my project

---

> **sahn44** · 2026-09-17T12:44:46.000Z　
> I'm also in the BirdTech scene. I detect birds and automatically spray them with a sprinkler to keep away from our pool area.code: https://github.com/mattsahn/bird-awaywriteup: https://mattsahn.github.io/bird-away-blog/

---

> **sandworm101** · 2026-09-17T16:59:00.000Z　
> A neighbour of mine has five chickens... well HAD fier chickens. A hawk did away with #5 and damaged two more.. I wonder what this display would make of that series of frantic bird calls.

---

> **SirHackalot** · 2026-09-17T17:43:37.000Z　
> Very cool idea, but I wanna be the one drawing. Why would I outsource the fun part to the AI? Classification is useful, but the paintings are the fun part…

---

> **Wolfmans55** · 2026-09-17T20:20:41.000Z　
> I love these super creative software + hardware project ideas you don’t see too much of anymore!

---

> **PigeonD** · 2026-09-17T21:42:32.000Z　
> Love this so much, cant wait to try

---

> **techsystems** · 2026-09-19T12:43:56.000Z　
> A redditor adapted this idea for the Samsung Frame https://old.reddit.com/r/TheFrame/comments/1wkg3fq/listen_fo...

---

> **mittsquinter** · 2026-09-19T13:36:32.000Z　
> Would it be possible to tap the bird images and play audio? Their call, that is. It would be a great way to reinforce sight and sound.

---

> **samarkundal** · 2026-09-20T07:56:42.000Z　
> This is pretty cool and it's pure art.

---

> **smeej** · 2026-09-15T13:41:39.000Z　
> Do you have your image source available somewhere? I'm not going to build this same thing, but I'd love to add some prints of birds to my shelves and, not knowing much about birds, it would help to have a set of pictures I could look through and go, "Ooh! This one!" and learn about them. It'd be a good jumping on point!

---

> **onionisafruit** · 2026-09-15T13:45:28.000Z　
> If I were to make one of these as a Christmas present for somebody in Texas, and I wanted to contribute work toward good coverage for the area, how big of a time commitment would that be? It sounds like the kind of hobby work I could get into for a few months.

---

> **away0g** · 2026-09-15T13:40:08.000Z　
> are you setting yourself up to record ideas as they happen?

---

> **tencentshill** · 2026-09-15T13:13:57.000Z　
> This one seems to be more North European focused

---

> **carb** · 2026-09-15T13:21:18.000Z　
> I agree I would expect a reference. Another difference between this an AvianVisitors is the image sources. AvianVisitors is all AI generated with a consistent prompt, but OP's is using chiefly public domain images with retouching by AI as needed.

---

> **wccrawford** · 2026-09-15T13:23:44.000Z　
> The new one appears to use real art from real humans, instead of AI art that was fixed.And just because 2 things do the same job doesn't make one a "copy" of the other.

---

> **DavCreator** · 2026-09-15T13:30:51.000Z　
> https://xxcancel.com/WarnerTeddy/status/2060018688645115964

---

> **bradly** · 2026-09-15T14:09:48.000Z　
> Fwiw an eink display is fairly common tech in the birdiverse. I also have a project that is the same thing.

---

> **dang** · 2026-09-15T19:51:29.000Z　
> Thanks! That one was discussed a few months ago:Avian Visitors - https://news.ycombinator.com/item?id=48343424 - May 2026 (20 comments)I've put a link to the earlier project in the toptext above.

---

> **eckelhesten** · 2026-09-15T13:29:19.000Z　
> Patents and greed in a combination.

---

> **pjerem** · 2026-09-15T13:32:00.000Z　
> You have to distinguish the fake color e-ink that are used in mass consumer products which are actually black&white e-ink plus an LCD layer and are expensive, and the real color e-ink where each micro capsule embeds 3 to 5 different inks of different colors.The latest are pretty complex devices, very slow to refresh (hence why they are not used in your e-reader) and also very expensive. But the rendering is way much nicer because it’s real ink that is used to render the colors.

---

> **whiskers** · 2026-09-15T13:52:53.000Z　
> This project will work with a 7.3" display just as well - they are £79.50! https://shop.pimoroni.com/products/inky-impression?variant=5...Disclaimer: I am the CEO of Pimoroni :-)

---

> **shellfishgene** · 2026-09-15T17:07:08.000Z　
> You can sometimes find old Nooks for cheap and they can be rooted to display static images, but it's not elegant.

---

> **arnemunthekaas** · 2026-09-15T13:42:23.000Z　
> Duly noted, I'll reference this, as well as other similar projects in the readme. Thanks for the feedback

---

> **zubiaur** · 2026-09-15T15:19:40.000Z　
> I thought it was the same person. That is how close this project is.
> Inspiration may be too soft of a word.

---

> **dang** · 2026-09-15T19:19:05.000Z　
> Thanks! Discussed a few months ago:Avian Visitors - https://news.ycombinator.com/item?id=48343424 - May 2026 (20 comments)

---

> **telesilla** · 2026-09-15T13:44:18.000Z　
> I agree. It's such a pity Cats don't recognize images, would make for wonderful CatTV.

---

> **bt1a** · 2026-09-15T14:30:55.000Z　
> Something like fpcalc for soundbytes? Neat

---

> **world2vec** · 2026-09-15T14:13:49.000Z　
> I do recommend a decent pair of binoculars and the Merlin Bird ID app.

---

> **RobinL** · 2026-09-15T14:16:01.000Z　
> > Half the point of this project is showing off some amazing public-domain natural-history illustrations. Over 800 cut-outs covering more than 400 species, every one taken from a real plate and hand-curated for this project (no art is AI-generated, though some has been retouched with AI).

---

> **stetrain** · 2026-09-15T14:24:33.000Z　
> You can in fact both have an interesting bird-based art display in your home and also go outside and watch birds yourself. Neither precludes the other.

---

> **zabriel_goss** · 2026-09-15T14:30:42.000Z　
> An app like this would be used as augmentation rather than simulation.

---

> **stronglikedan** · 2026-09-15T14:42:35.000Z　
> Or both. Why limit yourself?

---

> **bottled_poe** · 2026-09-16T01:42:35.000Z　
> The next logical step is to have speakers for the backyard to simulate the wildlife that no longer exists.

---

> **lateatdesk** · 2026-09-15T21:14:23.000Z　
> If you try it with her, I'd love to hear what she makes of it.

---

> **originalvichy** · 2026-09-15T15:51:36.000Z　
> Thanks for sharing. Didn’t know about this project. Have you used it yourself? I’ve only experimented with Scrypted for fun, but Frigate sounds like I could operate birdsong analysis without a separate BirdNET container.

---

> **eichin** · 2026-09-15T16:59:22.000Z　
> I haven't tried with BirdNet, but Merlin doesn't seem to ever false-positive on chipmunks or squirrels (there's been a suggestion that it should explicitly recognize them, and maybe some frogs too, since they're "loud thing in the same register" and it frustrates people that haven't figured it out yet...)

---

> **buffet_overflow** · 2026-09-15T14:46:01.000Z　
> Years on a wall mounted eink screen sounds super interesting. What are you using for the power delivery/battery side of that setup?

---

> **tranceylc** · 2026-09-15T15:41:09.000Z　
> When it does run out, are you able to replace the battery? Or is it something way more painful than that?

---

> **mikepurvis** · 2026-09-15T20:02:41.000Z　
> Thanks for speaking to the battery question; I'm very interested in how to run this kind of thing (the display portion at least) cordlessly too, especially when lipo pouches in that range are so dirt cheap.

---

> **wallst07** · 2026-09-16T10:41:16.000Z　
> For hanging as art, just found this https://github.com/dmellok/el133-pico-driverUses a native C driver instead of python so you can run the display off a battery as it's more efficient.

---

> **dzhiurgis** · 2026-09-17T00:54:43.000Z　
> I want a Japanese woodprint inspired colour dashboard for my Home Assistant. I don't need it at all, but I want it so badly. Some sketches I did with chatgpt look amazing.Colour e-ink are kinda small tho. Something like samsung frame tv might be better option.

---

> **jonplackett** · 2026-09-15T15:50:32.000Z　
> I was thinking the exact same thing!

---

> **tencentshill** · 2026-09-15T16:16:34.000Z　
> Another dev offers it as a full product. OOS at the moment though.https://theodore.net/store/avian-visitors/

---

> **InexSquirrel** · 2026-09-16T00:33:27.000Z　
> Was thinking this too. My parents are both avid birders, and I think it would make a fun addition to the house.

---

> **hirako2000** · 2026-09-15T15:25:10.000Z　
> Could be for the montage. Is that unfair to say no AI generated the arts, but that AI put individual pieces together?

---

> **jrflo** · 2026-09-15T15:48:26.000Z　
> What is the ethical concern in this use case?

---

> **arnemunthekaas** · 2026-09-15T16:53:22.000Z　
> Author here: Fair, i could've been more explicit in my writing. Concretely:Every bird is a cutout from a real scanned 1800s plate (Gould, the von Wright
> brothers, Dresser...). The manifest (https://github.com/arnegiacomo/fugleramme/blob/main/assets/a...) links to each source, so you can compare them to the original scans. No bird has been prompt/diffusion generated, although I did use diffusion-based tools to remove birds from the perches (https://github.com/arnegiacomo/fugleramme/tree/main/assets/a...).Nothing at runtime uses AI either, at least in the sense of LLMs or diffusion. The collage is Pillow and numpy, and detection is BirdNET, which is a classifier, not a generative model.However I have used LLMs for code-related work, and for writing scripts for programatically editing the images, like cutting, contrast and colour corrections.

---

> **originalvichy** · 2026-09-15T15:47:15.000Z　
> What do you mean specifically? These birdsong analyzers are sensitive enough that they do not rely on setting up a feeder. It’s obviously dependent on where you live, but in the Nordics, living outside city centres is good enough for both background noise and birdsong from nearby trees/parks/forests. Privacy matters aside, setting a mic up on a balcony or window is enough. Another solution is feeding data from a cheap security camera with a mic through wifi. This way the camera can stay outside in different weather, it’s not super close to you actual living area and splitting audio from the RTSP stream should be relatively easy to be analyzed by BirdNET.

---

> **eichin** · 2026-09-15T16:52:25.000Z　
> Sounds like you've got birds crashing into the door? That's often something that can be improved (with stickers or hanging decorations) that make the glass more perceptible to the birds. (Another thing that sometimes helps is having bushes or shrubs, or even potted plants, in sight of the feeder - most small birds will use a "staging area" and fly somewhere nearby first, "check out the scene", and then fly to the feeder from there; it doesn't really control the activity, but it adds some options.)

---

> **bithammerthunde** · 2026-09-15T16:32:02.000Z　
> Link missing?

---

> **andai** · 2026-09-15T16:42:58.000Z　
> Chernobyl.

---

> **tuvix** · 2026-09-15T17:55:16.000Z　
> Are there any LLMs being widely used for audio classification? I know VLMs are being used a lot in image stuff.It always seems kind of silly to me to throw everything at an LLM. I know they’re huge and can automatically handle a huge number of tasks but something in me finds it wasteful when we could be creating easily trainable, cheap to run bespoke models for a lot of stuff

---

> **ada1981** · 2026-09-15T21:32:52.000Z　
> Curious if there is a similar project for dog barks.

---

> **rexxars** · 2026-09-15T22:28:07.000Z　
> Note that while the underlying birdnet-go project started as BirdNET only, it can now use Google Perch v2, BattyBirdNET (for bats!) and other models in the future. It's a really cool project!

---

> **cosmojg** · 2026-09-16T16:21:55.000Z　
> Why would anyone assume this uses an LLM? It classifies bird sounds, not human language. I don't mean this as an attack, I'm genuinely curious! This seemed obvious to me, and I want to know what line of thinking might lead one to believe that an LLM is the better (or more likely) tool for this job over a purpose-built classifier.

---

> **3abiton** · 2026-09-19T06:15:03.000Z　
> Few years ago, there was an android app (open source from fdroid) that basically provided the model and ability to listen and give you informafion about the birds. It was very fun during hikes with friends.

---

> **the_real_cher** · 2026-09-15T17:54:47.000Z　
> That sounds cool! Where did you get your color e-ink panel?

---

> **pelican0** · 2026-09-15T21:41:09.000Z　
> > This is the coolest thing on HN that I've seen in a minute.Off-topic, but what is up with the increased use of the phrase "in a minute", presumably to mean "in a long time", lately?I've only started encountering it in the past year.Did it get popularized by some celebrity, tv show, influencers, etc?

---

> **hmartin** · 2026-09-16T04:35:25.000Z　
> Agree, this was really a beautiful thing to see!

---

> **fock** · 2026-09-16T06:52:34.000Z　
> EDIT: no Ai for pictures - cool!

---

> **sydd** · 2026-09-16T08:10:59.000Z　
> Really cool, except the price. Around 500 Euro for the full thing... I miss the times you could make amazing things with a Pi under 100 Euro.

---

> **herrherrmann** · 2026-09-16T21:02:39.000Z　
> A similar product would be Birdbuddy (a birdfeeder with a camera and logging functionality), albeit very commercial and closed-source.

---

> **swaraj** · 2026-09-15T21:27:50.000Z　
> >I've been leveraging Birdnet-2.4 as well,I love HN

---

> **blacklion** · 2026-09-15T23:13:08.000Z　
> Do you use AudioMoth embedded mic?

---

> **ptoo** · 2026-09-15T23:03:33.000Z　
> [flagged]

---

> **throooooo** · 2026-09-16T01:40:16.000Z　
> The e-ink screens linked by OP are much more interesting from a color reproduction standpoint. TRMNL devices are either grayscale or 2 colors.

---

> **apexalpha** · 2026-09-16T06:06:31.000Z　
> Just release some imported European birds. What could go wrong?

---

> **coro_1** · 2026-09-16T17:54:55.000Z　
> Depends on the feel of the space you're working with, for me. A 8 x 10 bird sketch generator could work.

---

> **arnemunthekaas** · 2026-09-16T18:14:29.000Z　
> Author here: it's not AI-generated. All art is public domain and made by real people. This project doesn't run generative AI models.See https://github.com/arnegiacomo/fugleramme/blob/main/assets/a... for all the sources

---

> **nozzlegear** · 2026-09-17T16:01:39.000Z　
> Ha, I've thought about doing something like this but to keep my cats off the countertops in the kitchen!

---

> **arnemunthekaas** · 2026-09-15T13:43:27.000Z　
> Yeah, all art i attributed an linked in https://github.com/arnegiacomo/fugleramme/tree/main/assets/a.... Check the manifest for exact sources

---

> **arnemunthekaas** · 2026-09-15T14:44:27.000Z　
> Less than you'd think, because you likely wouldn't need full "Texas coverage", you mostly need the birds that actually show up. BirdNET filters by location, you'll likely need a couple of dozen. Over the summer I've had about 40 visitors where I live.Right now the coverage of North America is relatively sparse, but the interest has been high and I'm hoping for some contributions.Edit: For North America the most obvious source is Audubon's Birds of America, which is public domain and should provide a lot of coverage. This collection includes some beautiful plates.

---

> **jiwidi** · 2026-09-15T13:15:30.000Z　
> Its awful close with no attribution or mention of the original project, which should be the minimum i feel like.

---

> **jiwidi** · 2026-09-15T13:25:58.000Z　
> Yeah agreeI understand OP is continuing the work and improving it as he sees fit, but that in my mind is a fork and should aknowledge the initial work that sparked it.Maybe i'm wrong tho and this is completely parallel work! Waiting for OPs reply

---

> **jiwidi** · 2026-09-15T13:31:48.000Z　
> My mistake for calling it "copy", should have said fork maybe (?)They are awful close to still require a reference to the original project imo. They are achieving the same output (identify birds and display them in a frame display all hosted in a raspberry pi) with that twist to how to generate the art.

---

> **jdiff** · 2026-09-15T13:35:20.000Z　
> What is "the new one"? The old one used AI, and this one seems to as well.

---

> **blacklion** · 2026-09-15T23:18:24.000Z　
> They are used in book readers. Amazon Kindle Colorsoft, for example. Or I have android phone with such screen (though, not latest generation).Rather opposite: I never seen consumer products with two-layer displays.

---

> **fnands** · 2026-09-15T14:00:51.000Z　
> Yeah, the 4 and 7.3" prices are not bad, the jump to 13 is just large.
> That being said, the cost per area goes down, so it is also probably fair.

---

> **tencentshill** · 2026-09-15T16:24:18.000Z　
> For a product that is made for creators and DIY, AI generated imagery on the product photos doesn't feel right.

---

> **koryk** · 2026-09-16T00:09:30.000Z　
> I love the inky impression!I am using my 13 inch inky display for my own birdnet - I also posted this in another thread last week https://i.imgur.com/5XbM6bb.pngI also bought 3 more 4 inch ones. Here is the first deployment next to the fish tank - https://i.imgur.com/nj8nKrS.png - I like this because I can stuff an rtl sdr in that box too, so it picks up nearby radio sensors in addition to BT. Real nice project screen!I usually only refresh the image on the screen every few hours. I love how the image stays even with no power.

---

> **nsbk** · 2026-09-15T13:49:54.000Z　
> Fair! Also, I would love to build this myself as I'm moving out of the city and to the countryside soon.I'm based off Spain, so I'll be happy to contribute if I find missing Iberian and Mediterranean species, or if some cool feature idea comes up :)

---

> **dang** · 2026-09-15T19:19:49.000Z　
> Maybe for fairness we'll link to it from the toptext as well.

---

> **reedlaw** · 2026-09-16T10:58:31.000Z　
> I have Bird Classification enabled in the settings, but so far haven't seen any labelled (it's only been a few days). Similarly with Face Recognition, I've only seen false positives. It does reliably detect people though (300 tracked so far). I'll have to experiment with settings such as confidence score.

---

> **reedlaw** · 2026-09-17T11:40:15.000Z　
> Turns out Frigate uses visual classification only. Hard to trigger when birds are so small, unless they fly right up to the camera perhaps.

---

> **joshstrange** · 2026-09-15T15:30:08.000Z　
> Here are the parts I bought, I'm still getting it all setup (I have my pictures displaying, working on designing the 3D printed case now, and testing it all) but according to OpenDisplay's calculator [0] I can expect 3.4 years if I refresh the screen once every 4 hours (and currently I'm doing closer to once a day to mimic my ESP32s which need deep sleep and once-a-day refresh to get even month/months of battery on a charge).Screen: 7.5" Monochrome eInk / ePaper Display with 800x480 Pixels (https://www.seeedstudio.com/7-5-Monochrome-ePaper-Display-wi...)BTLE board: XIAO ePaper Display Board(nRF52840) - EN05 (https://www.seeedstudio.com/XIAO-ePaper-Display-Board-nRF528...)Battery: 3.7V 2000mAh - (https://www.amazon.com/dp/B0FR9GH966)Picture of it all assembled (no case yet): https://cs.joshstrange.com/zJFvGGPBThe image rendered to the screen is coming from a little service I wrote that renders a book quote it pulls from BookOrbit which syncs with KOReader (annotations, progress, etc). My plan is to set up one of these one each bookshelf/series rotating quotes I highlighted from the series.Here are 2 ESP32-based screens I have, the one on the left is a an all-in-one [1] and the one on the right I printed the case from the TRMNL DIY kit from SeeedStudio [2]: https://cs.joshstrange.com/knk4Ns2hRight now only the BTLE one is running OpenDisplay (the other two are semi-managed by HomeAssistant ESPHome) and all the devices are in HA for controlling them, though the ESP32's all deep-sleep for saving battery so I can can't "push" stuff to them like I can the BTLE one.[0] https://opendisplay.org/index.html#battery[1] https://www.seeedstudio.com/reTerminal-E1001-p-6534.html[2] https://www.seeedstudio.com/TRMNL-7-5-Inch-OG-DIY-Kit-p-6481...

---

> **joshstrange** · 2026-09-15T15:47:40.000Z　
> It's a rechargeable battery, I just plug the board in (USB-C) and it charges the battery.

---

> **joshstrange** · 2026-09-15T20:18:28.000Z　
> I might be misunderstanding your comment but the display is run/powered by the board so all you need to do is provide power to the board. For e-ink it uses no power to "hold" an image, only to write/refresh (sorry if I'm telling you something you already know!).So reiterate, with a 2000mAh lipo battery I should be able to drive the board _and_ the screen for over 3 years if I only refresh it at most once every 4 hours (with "push" capabilities, I don't have to deep-sleep the board to get that battery life). At least, that's what the calculator says, I _just_ got my hardware to play with and so I can't speak from experience. Unfortunately my board is not charging the battery so I need to get a replacement which will probably take a week or two to get here.

---

> **jarek83** · 2026-09-15T16:05:50.000Z　
> Well I specifically meant having a bird feeder on a window or glass door for a chance to watch them live closely. That's why I put it as a side note ;)You gave me few ideas for the analyzer setup too - thanks!

---

> **radiorental** · 2026-09-15T16:43:16.000Z　
> Complete guess but I wonder if it's the Merlin project?https://www.birds.cornell.edu/home/merlin/

---

> **shellfishgene** · 2026-09-15T17:03:49.000Z　
> Probably BirdNet, but Google also has an equivalent model now called Perch.
> https://birdnet.cornell.edu/

---

> **benob** · 2026-09-15T19:00:11.000Z　
> https://github.com/earthspecies/NatureLM-audio

---

> **lambda** · 2026-09-15T21:15:33.000Z　
> There are LLMs that support audio input, similar to those with vision support.From my testing of open weights LLMs with audio support, they basically are only trained to recognize audio as an alternative to text input, they treat audio as basically equivalent to a transcript, and can't recognize or distinguish things like music, accents, background sounds, etc.So they're only really good for transcribing or summarizing or using audio input in place of text input for prompts, but not anything that requires distinguishing any information about the audio that would not be present in a transcript.It can be tempting to try to use an LLM for a variety of tasks; kind of the whole thing about an LLM is that you don't have to do a separate complex training run for every task, but can just provide instructions in natural language. But it only works as far as what the training data covers, if the training basically always treated audio and a text transcript as equivalent, the model has nothing causing it to learn other relevant features of the audio. If there's enough bird call identification in the training data of an LLM, it might be able to do that, but I think multimodal training data tends to be much more limited than the text training corpus

---

> **radarsat1** · 2026-09-16T09:52:26.000Z　
> wav2vec or similar approaches are used a lot these days, which is basically BERT with audio inputs. Whether that counts as an LLM or not, I am not sure. It's a transformer architecture in any case.People will often reach for "easily trainable, cheap" solutions when they can; the reason people reach for Transformers and LLMs is because when you throw more data at them, they get better.

---

> **ninjalanternshk** · 2026-09-16T13:56:37.000Z　
> The harness that connects to a chatbot, API or voice interaction is the place to route requests to different systems. If you remember the early days of ChatGPT it explicitly said it was routing image generation to Dall-E after embellishing your request itself first.Determining which tool to use should be a lightweight operation but I’m not expert enough to understand exactly how much lighter than a full LLM call just to recognize it needs a different tool or model.

---

> **antonvs** · 2026-09-17T01:49:14.000Z　
> There’s still plenty of commercial work on specialized models, for the simple reason that they’re typically much cheaper to train and run.Many systems now use LLMs in conjunction with specialized models.

---

> **lacunary** · 2026-09-16T03:44:07.000Z　
> I wanted to say that seems like a stretch but then I often find myself visualizing my best guess at the appearance, including species, of an unknown dog. It seems like size of dog and pitch of bark are negatively correlated

---

> **pgreenwood** · 2026-09-17T05:45:52.000Z　
> Yes, here's the classifier:def get_species():
>  return 'Canis familiaris'

---

> **WolfeReader** · 2026-09-16T19:49:10.000Z　
> Most "Show HN" posts these days are vibe-coded garbage. It is a pleasant surprise to see one that isn't!

---

> **albertgoeswoof** · 2026-09-15T18:36:02.000Z　
> I got https://www.waveshare.com/13.3inch-e-paper-hat-plus-e.htm from Amazon, about 300 gbp

---

> **seanwessmith** · 2026-09-15T21:50:47.000Z　
> seems like you know what you're talking about 5k% increase starting in July this yearhttps://trends.google.com/explore?q=I%27ve%20seen%20in%20a%2...

---

> **scheme271** · 2026-09-15T22:58:31.000Z　
> It's been around in slang for a few years with a few variants, e.g. "I haven't seen her in a hot minute." I think it's just filtered into wider cultural vernacular.

---

> **palad1n** · 2026-09-15T23:28:25.000Z　
> Scarlett Johansson says, “See you in a minute" in Avengers: Endgame.

---

> **devindotcom** · 2026-09-15T23:40:04.000Z　
> it's been around. I more commonly see it as "been a minute!" when you see someone you haven't seen in a good while.

---

> **Carrok** · 2026-09-15T23:40:42.000Z　
> This phrase has been around for years, I know because it has always infuriated me.They took a well-defined unit of time, which is relatively short, and made it mean “some unknown but very long period of time”.So frustrating. /oldmanyellsatcloud

---

> **freehorse** · 2026-09-16T19:37:50.000Z　
> I had not heard it before (or if I did I did not interpret it correctly, eg if one told me "see you in a minute" I would interpret it as "see you in a bit".But there is this podcast discussing it in 2021, and it comes from black community slang from 70s (which is where most slang I encounter comes from). And these terms take a while to catch up usually, but it seems it was already circulating more broadly since 2000s.https://waywordradio.org/its-been-a-minute/

---

> **Larrikin** · 2026-09-17T15:37:16.000Z　
> It's been a phrase for decades.

---

> **puzzlingcaptcha** · 2026-09-16T08:32:02.000Z　
> That's the e-ink monopoly for you. Though you could probably use a slightly smaller b&w eink display with a second hand raspberry 4 to shave a lot from that number.

---

> **thepoet** · 2026-09-16T22:42:23.000Z　
> If you have a Kobo (~ US$ 120 or even less used) you can run this using Cobalt https://github.com/BandarLabs/Cobalt/tree/beta/apps/birds

---

> **eointierney** · 2026-09-15T23:00:54.000Z　
> Yep, when it's humans nerding it's awesome

---

> **simonjgreen** · 2026-09-16T05:05:27.000Z　
> That’s the one, in their outdoor casing

---

> **cluckindan** · 2026-09-15T23:10:43.000Z　
> German engineering at its finest.

---

> **dang** · 2026-09-15T23:43:47.000Z　
> Please don't do this here.

---

> **KaiserPro** · 2026-09-15T13:24:52.000Z　
> true, but we are assuming that the author is aware of the other repo

---

> **arnemunthekaas** · 2026-09-15T13:25:42.000Z　
> Original author here. Fair point, this project was one of my inspirations, but I chose to take a different approach. This uses public domain natural history art and builds on top of BirdNET-Go which is a popular way of self-hosting bird-detections. (This is really a BirdNET-Go companion, as it cannot run without).I've seen other similar projects pop up like https://github.com/veteranbv/inky-bird-frame and https://github.com/adamoberley/HABirdDashboard/tree/HABirdDa..., each with their own spin.

---

> **arnemunthekaas** · 2026-09-15T13:28:17.000Z　
> Hi, yeah I'm not basing any of my coding or feature-work on that project. My biggest source of inspiration is actually just a paper poster I have hanging on my wall https://www.axelthorenfeldt.com/news/wwf-verdens-naturfonds-.... I wanted to make a version of that, showing the actual birds in my garden.

---

> **martin-** · 2026-09-15T14:34:05.000Z　
> A fork implies that it builds upon code from another repository. I wouldn't use the word fork to mean "inspired by". I think it takes away from the effort that the author has put in. Anyone can create a fork of a project with the click of a button.

---

> **arnemunthekaas** · 2026-09-15T13:34:58.000Z　
> Author here: I'll take any feedback and critisism. I haven't based any of my work directly on his project, but will be referencing it as a similar one in the readme, as well as e.g. https://github.com/veteranbv/inky-bird-frame.

---

> **arnemunthekaas** · 2026-09-15T13:38:43.000Z　
> Author here: It doesn't, well at least not art-wise. All sources are attributed in https://github.com/arnegiacomo/fugleramme/blob/main/assets/a... and https://github.com/arnegiacomo/fugleramme/blob/main/assets/a...

---

> **stetrain** · 2026-09-15T14:22:55.000Z　
> From the link: "Half the point of this project is showing off some amazing public-domain natural-history illustrations. Over 800 cut-outs covering more than 400 species, every one taken from a real plate and hand-curated for this project (no art is AI-generated, though some has been retouched with AI)."

---

> **whiskers** · 2026-09-17T11:31:51.000Z　
> Cost per area is pretty much what drives all display pricing. :-)

---

> **arnemunthekaas** · 2026-09-15T14:38:46.000Z　
> I'm actually currently working on implementing Iberian species, and added some yesterday. There's another user also contributing with some beautiful Spanish birds. Feel free to contribute if you have some cool visitors in your garden!

---

> **realcul** · 2026-09-15T17:32:50.000Z　
> If I want a wifi e-ink connected display - curious what would you recommend.
> I want an e-ink display - that I can use as a sign/display board with wifi connectivity and remote administration.

---

> **mikepurvis** · 2026-09-16T01:24:09.000Z　
> Yeah no we're aligned; I have some raspis that I'm interested in doing long term battery stuff with (remote sensing and the like) and it definitely does seem like connectivity is the huge battery killer, like even if you wake up only periodically to take a reading or update an epaper display, the cost in battery just to negotiate a wifi connection and do tcpip and http things is awful.And then you're stuck with a device that can only be communicated with when it chooses to wake up, whereas with BLE it seems you can listen for a remote OTA wake much more cheaply.

---

> **originalvichy** · 2026-09-15T18:16:24.000Z　
> Yeah that’s definitely going to be messy. Based on your region, there should hopefully be generic security cams that can even work with a batter and solar. That combined with wifi if it can reach your house can hopefully steer the blast zone way further :D There’s a few TP-Link cameras on discount around 100€ that have 2k res. Feels a lot easier this way rather than taping together a weatherproof box for various components like the Pi and a mic. So far I’ve only used a plug-powered one since I have a IP-rated socket outside and the TP-link cam has a magnet for my wall. Hope you find a nice solution!

---

> **bix6** · 2026-09-15T20:06:17.000Z　
> More info please. Can I add this into birdnet go for more species detection?

---

> **sbrother** · 2026-09-16T04:07:29.000Z　
> Have you had any luck fine tuning one with musical data for classification or music-aware QA? I've been hacking on https://trebel.la/ which I would like to be a music practice companion, and the biggest missing feature is actually useful audio-based feedback pipeline.My current approach, not yet validated, is trying to generate training data from masterclass recordings on Youtube, and then fine tuning MOSS-audio on a bunch of those. But I'm interested if there are better models, or large training sets I don't know about.

---

> **tuvix** · 2026-09-16T15:46:27.000Z　
> For sure, I just know it’s tempting given the power of large transformers to throw things at an existing model.For instance, OCR is something that can be done locally with no access to a GPU but people (including me) still often use cloud hosted multi-modal large language models for it.

---

> **nozzlegear** · 2026-09-17T15:59:57.000Z　
> I think it's because bigger dogs have larger throats and a bigger "voice box," so to speak. They have more of the vocal folds than a small dog, plus they have a bigger chest and larger lungs to force more air through them.That's my bro-science understanding of it, anyway.

---

> **the_real_cher** · 2026-09-16T00:35:31.000Z　
> Thats cool thanks!

---

> **bezmi** · 2026-09-15T23:01:44.000Z　
> I think the trend is probably misleading. A popular youtuber may have released a video in August with a title containing "in a minute".

---

> **mrbombastic** · 2026-09-16T00:45:44.000Z　
> people have been saying "it's been a minute" to mean a long time since at least the 90s in NY

---

> **freehorse** · 2026-09-16T19:42:22.000Z　
> I say "see you in a minute" to mean "see you in a bit". What did Scarlett Johansson mean by that in that movie?

---

> **MichaelZuo** · 2026-09-19T15:09:47.000Z　
> To be fair even if they could build a 10x larger e-ink panel factory it’s uncertain if they could shave costs by more than maybe 40% to 50% per panel.And it’s very questionable whether there is genuinely 10x more latent annual demand for e-ink panels at that still not cheap price point.

---

> **abejfehr** · 2026-09-20T14:44:43.000Z　
> It seems like Kobo eReaders don't come with a mic.You could probably use an ESP32-S3-PhotoPainter (which comes with a mic) to do this for even cheaper: https://www.waveshare.com/esp32-s3-photopainter.htm

---

> **jiwidi** · 2026-09-15T13:29:25.000Z　
> That's fair, and I totally get wanting to give it your own spin.I still think it would be good to acknowledge the original project that sparked the idea, especially now that you've mentioned it was one of the inspirations.Definitely keep going with yours and evolve it further. That's how good projects grow. But for a healthy open source community, I think we should make a point of crediting the people whose work inspires us. Otherwise, over time, it can discourage people from sharing their projects publicly in the first place.

---

> **delichon** · 2026-09-15T13:31:15.000Z　
> I accuse you of having good taste.

---

> **p1anecrazy** · 2026-09-15T17:14:15.000Z　
> Please take my praise as well then :) what a wholesome project!

---

> **coinfused** · 2026-09-15T17:45:27.000Z　
> This is much appreciated! Thanks for making this decision

---

> **xgulfie** · 2026-09-15T19:57:42.000Z　
> Idk what "retouched with AI" means. Does it mean they used a segmentation model to cut out the shapes, or were they shoved through an imagegen and completely recreated?

---

> **joshstrange** · 2026-09-15T17:42:49.000Z　
> If you want a simple e-ink wifi screen I'd point you at the reTerminal e1001 [0] if that size works for you. It's the easiest to get started with. You can either keep it on power or use the deep sleep to get more from the battery. It really comes down to how often you want to update it.The BTLE boards have just crazy higher battery time with no need for deep sleep which is why I'm moving in that direction.~7.5" is the size I've been buying so far, the larger e-ink screens get pricey but I can't wait for a calendar-sized one to come down in price such that I can frame it and hang it on the wall. Lastly I'd avoid the color e-ink screens unless you know you need color, won't need to refresh it often, and it's not in your eye line. Color refreshes take way longer (~30s in my experience for a 5-6 color screen) and the flashing it has to do is obnoxious. Monocolor displays take <2s normally and a single flash. I got a color screen first because "why not?" and I got color, but the refresh was too annoying so now it refreshes once a day in a place that I'm not when it refreshes so I don't have to see it.I also recommend you check out OpenDisplay for what you will run on the device: https://opendisplay.org/index.html[0] https://www.seeedstudio.com/reTerminal-E1001-p-6534.html

---

> **shaklee3** · 2026-09-16T04:58:41.000Z　
> It only can last a couple weeks, so isn't really practical. Search for other e-ink calendar projects using the rpi zero

---

> **MisterMunchkin** · 2026-09-16T14:06:04.000Z　
> You're selling a music feedback app and it doesn't do the music feedback part yet?

---

> **lambda** · 2026-09-18T04:00:33.000Z　
> I have not. It's something that I've considered, but never actually have done it.

---

> **kulahan** · 2026-09-16T19:00:13.000Z　
> Yeah, I’ve been saying hot minutes for decades myself!

---

> **arnemunthekaas** · 2026-09-15T14:00:20.000Z　
> Thanks, I’ll do that, and ofc link to this beautiful poster I have that actually originally sparked the idea: https://www.axelthorenfeldt.com/news/wwf-verdens-naturfonds-...

---

> **arnemunthekaas** · 2026-09-15T14:56:08.000Z　
> Added, see README. Thanks for the feedback!

---

> **dzhiurgis** · 2026-09-17T00:58:50.000Z　
> At this point - does it even matter? AI photos are indistinguishable.

---

> **sbrother** · 2026-09-16T19:19:30.000Z　
> I'm not selling anything; I'm developing it live and there is a landing page, but there's no payment hooked up since like you said, it's not functional yet.

---

> **hnbad** · 2026-09-15T15:06:41.000Z　
> Contrary to the Great Man version of how we mostly talk about history, scientific discoveries, technological breakthroughs and such have historically often occurred multiple times in multiple places often in close proximity time-wise but otherwise completely unrelated to each other. This of course makes sense if you consider that history seems to be primarily driven by material conditions (e.g. steam engines were known to Ancient Greece but their usefulness for industry simply hadn't occurred to them because they lacked the prerequisites to make them useful and neither economic efficiency nor access to cheap labor were significant enough concerns - plus there was no patent system of course).I'll leave it up to you to decide whether one should expect the demographic of this website to be especially invested in the Great Man narrative but trying to convince them that two people can independently have similar-sounding ideas involving similar-but-different technology is probably an uphill battle. Just be glad you're not composing music for a living because there's literally an entire industry built around the idea that it's impossible for two people to come up with similar melodies without knowingly or unknowingly copying eachother and that it's very important that one of them (or rather the company they had to sign a deal with in order to make any money off their music at all) 100% owns that exact melody and should be paid by anyone who wants to use it.Next time you have an idea you should just file a patent tbh - the insistence on prior art invalidating the work seems to be quite similar but at least if you're granted a patent you can shake down "copycats" for money.

---

> **xgulfie** · 2026-09-17T01:15:49.000Z　
> It matters to me because it claims to be "real, hand-cut 1800s bird illustrations" which is the whole appeal of this to me

---

> **elictronic** · 2026-09-17T17:21:10.000Z　
> It's the first thing you see when opening the page.

---

> **dotancohen** · 2026-09-15T19:33:29.000Z　
> > Contrary to the Great Man version of how we mostly talk about history, scientific discoveries, technological breakthroughs and such have historically often occurred multiple times in multiple places often in close proximity time-wise but otherwise completely unrelated to each other.
>
> My favourite example of this is calculus, followed closely by heavier-than-air flight.

---

> **cyphar** · 2026-09-16T05:08:32.000Z　
> I think there is ample evidence that the Wright brothers were (unlike many other inventors) uniquely suited to solving the problem of heavier-than-air flight, as they solved several open problems that nobody was making progress on (the main ones being control authority, propeller designs, the scientific basis for wing designs, and the ability to test designs and practice without dying) -- they even discovered and solved previously-unknown problems (such as adverse yaw, something their contemporaries should've independently discovered if they were on the right track).A full rundown would be too long but [1] is a pretty good video going through the history of flight and how most of the other candidates for "first flyers" people bring up don't count and how it's difficult to argue that any of their contemporaries were even close to the Wrights.[1]: https://www.youtube.com/watch?v=EkpQAGQiv4Q

## 关联链接

- http://localhost:8080/

## 导航

- 项目页：[[10-项目/github.com_4e7ba9f5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
