---
type: "corpus"
item_id: "5e0314b99eeb7250"
title: "Building the site was easy, with Claude Code, but getting people to use it is not!"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xepvdm/building_the_site_was_easy_with_claude_code_but/"
author: "Global_Silver2025"
published_at: "2026-10-25T09:48:20+08:00"
captured_at: "2026-11-04T09:52:56+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-04"
pub_day: "2026-10-25"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 5, "comments": 19, "upvote_ratio": 0.8571428571428571}
comments_count: 18
comments_total: 19
discovered_via: "reddit:14d+settle10"
---

# Building the site was easy, with Claude Code, but getting people to use it is not!

> [!info] 一句话导读
> Ever since my friend showed me Claude Code about five months ago, I have been trying it out for multiple projects. I created some Apple II assembly programs; th…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xepvdm/building_the_site_was_easy_with_claude_code_but/>
> 指标：得分=5 · 评论=19 · 赞踩比=0.8571428571428571
> 作者：Global_Silver2025　|　发布：2026-10-25T09:48:20+08:00
> 项目链接：—
> 采集：2026-11-04T09:52:56+08:00　|　id：`5e0314b99eeb7250`

## 正文

Ever since my friend showed me Claude Code about five months ago, I have been trying it out for multiple projects. I created some Apple II assembly programs; that was pretty neat. He asked me to try making a website from scratch. I also had it re-create the functionality of Adobe Encore, the cancelled DVD authoring program, and it works great. I also found out that Handbrake is open source, so I asked it to expand the size of the chapter name boxes, and it did so in about five minutes.

So I've been learning about DNS, about using a linux machine in my home office to host websites (and how to get a static IP address from a home small business account). I have the server hooked up to the local network, and Claude Code access it directly. I don't have to pay for a data center or webhost to hold my experiments, and copying files, even gigantic ones, takes seconds or minutes instead of hours. All I had to do was install Ubuntu Server, and Claude Code did the rest, from Docker, to setting up a nightly backup to our warehouse computer, to showing me how to switch the DNS to the warehouse computer if the other one goes down. It keeps the two servers copied, so I don't have to manually do it.

My friend has asked me to do some website work for him, and I've also been doing work on my own websites. I've come up with some ideas, some are live right now and other ones are built but not deployed yet.

We have check writing software, and I learned how to get the Microsoft Store to host it for us. We have an electronic invite site about to start up. I've built my own game generator site, for PDFs parents and teachers can download and use. I've just started an online streaming company for businesses, using my own AI generated music.

I've also made a "groups" website, where small groups (10 or fewer) of people can have a private discussion group. I've had Claude Code build it so I can't see what anyone posts, unless I'm a member of that group. But I did learn that there is a service, PhotoDNA, that scans uploads for illegal images, so I've had to sign up for that through Microsoft (still waiting for acceptance). There are a lot of behind-the-scenes set up that I never knew before when you're hosting other people's uploads. There's a whole warrant/subpoena proces I knew nothing about, so I had Claude Code make it so I could just enter a username and a post ID, and it would grab the post, zip it up with encryption and a checksum, and send it to any email address I give it. That way I don't (or want to) see what was posted. Like Sgt. Shultz, "I See Nothing!"

None of my sites have any users yet. That's the hardest part. With everyone now having access to AI, websites really have to be exceptional (or connected to a famous person) for people to use them regularly. All of my websites have that "AI look", but they are all constructed through careful planning.

I've also become much more precise in how I ask Claude Code to work. The prompts you give can sometimes be misconstrued if you write it in an awkward way. Plus, I'm not the greatest typist, so it takes me a while to proofread my prompts so a misspelling doesn't cause undue delay.

And I just found out today that Stripe can give you an AI key to let the AI do the work for you, setting up your subscriptions and products on the site properly, and making sure the checkout process works properly. The Stripe website is very confusing to me, so having the AI work with it helps tremendously.

If anyone has questions, I'm open to any part of the process I've done so far. Thank you.

## 评论（18/19）

> **Wooden_Rip173**（2 分） · 2026-10-25T10:04:16+08:00　
> getting the tech stack humming is the fun part, the marketing side is a whole different beast
>
> the groups site with the blind admin setup is interesting, most platforms pretend they can't see your stuff but you know they're data mining everything. actually building in that separation is rare
>
> what's the game generator site do exactly? like mad libs style or more structured

---

> **Global_Silver2025**（1 分） · 2026-10-25T10:13:49+08:00　
> As someone who values MY privacy, I also value other peoples'. I also don't like advertisements and tracking, so I don't want them on a website I create. We don't even have passwords, just direct links for people to sign in, so no one can find a private group if they don't have that link, and if the link gets leaked, the group admin can click a button and a new link is generated. When they log in once, it saves it for 60 days from the last login, so if they go to the main page and the cookie is present on their computer, it immediately goes into their list of groups.
>
> The game generator makes downloadable PDFs of word search, Sudoku, chess, trivia quiz, cryptogram, etc. Games that people put together into books they sell on Amazon KDP, and parents and teachers use for their students/children.

---

> **Unusual_Bridge4527**（3 分） · 2026-10-25T10:16:02+08:00　
> Five minutes to resize the Handbrake chapter name boxes. I've been squinting at those boxes for years assuming they were just like that and nobody could do anything about it. The Adobe Encore rebuild is objectively the cooler project but Handbrake is the only one of these I'd ever touch.

---

> **Global_Silver2025**（1 分） · 2026-10-25T10:22:05+08:00　
> Claude told me:
>
> The three changes, all in ChaptersView.xaml:
>
> \* The chapter list no longer scrolls sideways (ScrollViewer.HorizontalScrollBarVisibility="Disabled"), so each row is only as wide as the visible list.
>
> \* The chapter name column changed from Width="166" to Width="\*", so it fills the rest of each row.
>
> \* The chapter name box now has MinWidth="150".
>
> Then it went and made the changes and created my own version. It was a simple change that I've been frustrated with for years. I had to have Visual Studio, though.

---

> **QuanTradin**（1 分） · 2026-10-25T10:26:44+08:00　
> a home server with nightly backups to a second box is more ops than most people on a paid webhost ever set up. for users, pick one site and go find people who already have that problem. the check writing software has the clearest buyer of everything you listed.

---

> **emberlanes1**（2 分） · 2026-10-25T10:41:43+08:00　
> the shift from coding to distribution is brutal when you actually enjoy the technical part

---

> **Perception9611**（2 分） · 2026-10-25T10:57:34+08:00　
> totally agree on picking one. The OP has like six projects listed and that's the real problem, not the tech. Claude Code makes building so fast that you keep spinning up new things instead of sitting with the uncomfortable part of actually finding users for one of them.

---

> **paulsonfanboy134**（0 分） · 2026-10-25T12:00:53+08:00　
> Can people stop posting the same stuff lol

---

> **Competitive_Tune_590**（1 分） · 2026-10-25T12:23:27+08:00　
> building is the easy part, getting users is the real challenge. i used ghostlaunch (https://ghostlaunch.so) to test a similar idea. they build a landing page and find people already asking for a fix, so you get real data on whether anyone cares before you go deeper. might help you figure out which project to focus on.

---

> **GoodMinimum4645**（2 分） · 2026-10-25T12:28:09+08:00　
> this is the real trap with AI coding tools. the dopamine hit from shipping something new is way stronger than the slow grind of finding users, so you end up with six half-marketed projects instead of one that actually has traction. pick the one with the clearest buyer and force yourself to stop building for a month.

---

> **cocoabuilder**（1 分） · 2026-10-25T16:16:39+08:00　
> Picking one project is the right instinct, but I would pick it by distribution and risk, not by which one is most interesting to build. A project only gets its first users if you can already name the first ten people and say where they already look for help — otherwise you are building a second project to solve the same distribution problem.
>
> On that test, the check-writing software looks strongest, because it has an identifiable buyer and a store channel through the Microsoft Store, rather than a general audience you have to find from scratch. The game generator has a searchable need — a teacher who needs a worksheet for tomorrow — but that is also a crowded search, so it would need a very specific angle, such as one type of puzzle for one age group, to stand out. The groups site is the one I would not start with, despite the privacy work: hosting other people's private discussions brings moderation, abuse and legal-process responsibilities that are much harder to carry with zero users and no tested process, however well the blind-admin design is built.
>
> A practical pause that has helped me: stop building for a fortnight and write down, for the one project you choose, ten named people or groups you could actually contact this week, what job each of them needs done in one sitting, and what you will watch to know they got it. If you cannot fill that list, that project is not ready to be the one — no matter how good the hosting setup behind it is. The home server and nightly backups are impressive work, but users will never see them; they will only see whether the first thing they try works.
>
> Which of these projects has people you could reach this week without building anything new first? That answer is usually the project to focus on.

---

> **QuanTradin**（2 分） · 2026-10-25T20:29:22+08:00　
> yep, six half launched things is the classic Claude Code trap. building got cheap, finding the first ten users didn't.

---

> **blazarious**（1 分） · 2026-10-25T21:16:54+08:00　
> So, anyone who gets their hands on the link can join the group? Or do you erify email addresses or something like that?
>
> Also, how can you not see what’s posted? Is it stored encrypted and you don’t have access to the key? How can you then send out the post to anyone else via email as you said when you don’t have access?

---

> **Global_Silver2025**（1 分） · 2026-10-27T23:02:13+08:00　
> We also thought the check-writing software would be the most-useful, and most-sought-after. We finished that one first, and had it up and running while we ran ads for it. We haven't received a single subscriber. Our background music service for businesses now has about fifteen subscribers in the first two weeks, and we haven't ran any ads at all for it, since we're still building it out.

---

> **cocoabuilder**（2 分） · 2026-10-28T01:01:11+08:00　
> That update flips the earlier test, so follow the paying signal. Pause further ad spend on the check-writing software until you understand why it did not convert — that result may be a distribution or audience problem rather than proof the product is unwanted. The more useful lead is the music service: find out how those fifteen found it and what job they hired it for, because that channel is the one to build on. The music service is where paying users already are, so the concrete next step is talking to those fifteen and tracing their route in.

---

> **investigatormaker**（1 分） · 2026-10-28T09:20:22+08:00　
> Of everything you listed, I'd pick the game generator for PDFs first. Parents and teachers already look for printables, so a finished PDF you made, posted where they trade them, gives people something to use before they ever see a site. The trade-off is that spreading across several sites gives you several thin tests, while one site gives you a clear read on what people click. The private groups site is the hardest cold start, since a group needs members before it is worth joining.
>
> I make ThreadFox.
>
> We find relevant Reddit conversations and post for your business. We'll post 3 replies free first, no card; then the $79 Pilot covers seven days and up to 50 posts and replies. No automatic renewal.
>
> [https://threadfox.vip/p/ejr1z/managed](https://threadfox.vip/p/ejr1z/managed)
>
> Which of your sites would you want in front of people first?

---

> **Global_Silver2025**（1 分） · 2026-11-01T00:29:44+08:00　
> Interestingly, I just received an email from the Microsoft Store and they say there were 65 installs of the check-writing software in September; but we've had zero subscriptions.
>
> I've sent out emails to the subscribers of the music service. Hopefully they will answer.

---

> **cocoabuilder**（1 分） · 2026-11-01T01:00:59+08:00　
> That 65 to zero gap is the more useful signal now. Before writing it off, I would separate discovery from activation: do you know whether those installs ever opened the software, and whether the subscription step was reached at all? If most never got past first run, the problem is onboarding, not demand. If they used it and still did not subscribe, the price or the first paid step needs the work. Keep that separate from the music service — its subscribers are a different test, and mixing the two will blur what each number is telling you.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
