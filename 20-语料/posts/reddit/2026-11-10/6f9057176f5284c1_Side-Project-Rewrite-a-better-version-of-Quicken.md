---
type: "corpus"
item_id: "6f9057176f5284c1"
title: "Side Project: Rewrite a better version of Quicken."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1xjx5py/side_project_rewrite_a_better_version_of_quicken/"
author: "Aromatic_Original812"
published_at: "2026-10-31T09:15:40+08:00"
captured_at: "2026-11-10T09:51:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-10-31"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 5, "comments": 17, "upvote_ratio": 0.7272727272727273}
comments_count: 15
comments_total: 17
discovered_via: "reddit:14d+settle10"
---

# Side Project: Rewrite a better version of Quicken.

> [!info] 一句话导读
> Please hear me out: I have been using Quicken for decades and have not seen any significant improvement. If anything, it's become bloated, slow and at times unr…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1xjx5py/side_project_rewrite_a_better_version_of_quicken/>
> 指标：得分=5 · 评论=17 · 赞踩比=0.7272727272727273
> 作者：Aromatic_Original812　|　发布：2026-10-31T09:15:40+08:00
> 项目链接：—
> 采集：2026-11-10T09:51:55+08:00　|　id：`6f9057176f5284c1`

## 正文

Please hear me out: I have been using Quicken for decades and have not seen any significant improvement. If anything, it's become bloated, slow and at times unreliable in downloading transactions.

After seeing a single developer burning AI credits to rebuild Photoshop and it's kin, I am wondering **if there is a savior among us brave enough to attempt to write a simpler, better version of Quicken?**

I don't want to compete with Quicken -- this would be for an individual person alone and not to sell or compete with them.

My pet peeves with Quicken is that it is unreliable when downloading from multiple accounts and institutions. (The search and reporting feature is difficult to navigate especially if you have many transactions but I can live with the 1990s interface.)  I don't mind paying money for Quicken and will do so but i want something RELIABLE that does not mess up my existing transactions or assign incoming transactions to wrong accounts.

Quickbooks is so complicated for a non-accountant non-business owner like me. If anyone has a suggestion please DM me for an alternative on Windows.

Thanks

## 评论（15/17）

> **MattSenter**（3 分） · 2026-10-31T09:50:03+08:00　
> Oh man i've wanted to do this so much. Quicken is and has always been "just ok" IMO and could EASILY be supercharged by a refresh. The problem you are going to run into, though, is matching their connector library. You can build each pretty quickly with AI but you're still going to need to track them all down and build the appropriate scraper or get an official API key and become a client. You could do seed this by tracing Quicken's connections, but still...
>
> Guess what i'm saying is: GOOD LUCK! 🫡
> 😂

---

> **CaramelEmotional3092**（2 分） · 2026-10-31T10:16:34+08:00　
> I shouldn’t encourage this, and I’m not going to do it, but Do u have a copy of quicken? It’s likely a 48hr on Claude max to build a replacement -> still likely weeks for a solid project.
>
> I’ve got Claude driving one app via rdc and rebuilding a complete new version. So it opens files on one, rebuilds it in the new version, and ensures the output is identical.
>
> Claude won’t use exact icons it makes new ones but the menu layout look and feel can be almost exact.
>
> If you are going to do it, do it now. Others are reporting it’s already getting harder for them to steal games.

---

> **Aromatic_Original812**（2 分） · 2026-10-31T10:18:48+08:00　
> Actually, PLAID makes the bank connection somewhat easy. As I am not trying to sell the software, I will put it on github and the user can get their own free API key. This effort is to simplify my life not create a business to earn a few bucks. I hate spending what's left of my life to manage my meager funds.
>
> My concern is how to prompt for any errors in the software that's generated. Do you have any work experience with Claude or Gemini to tell me where to start?
>
> (I did try using AI to just download CSV or QIF files and then upload to my drive using a chrome/python extension but it failed miserably. )

---

> **Aromatic_Original812**（3 分） · 2026-10-31T10:22:31+08:00　
> I may get sued by them. So, no, I am not going to copy their crappy interface ;-) It did cross my mind tho.

---

> **MattSenter**（2 分） · 2026-10-31T10:27:55+08:00　
> Oh well that changes things a bit. If it's just for you, why pay for Plaid? You can totally make every connection you need, whether you use AI or not. I've done a lot of AI development, yes. The great disintermediator of big businesses like Plaid.

---

> **Vapor95-Store**（1 分） · 2026-10-31T10:29:01+08:00　
> I created a Quicken/Quickbooks style accounting program. Its called Neo-Capital. You can check it our and try it free for 14 days. It can import all types of files from Quickbooks and templates for everything else. The website is [Neocapital.app](http://Neocapital.app)

---

> **QuanTradin**（1 分） · 2026-10-31T10:30:11+08:00　
> the unreliable downloads mostly aren't Quicken's own code, it's the bank connection layer underneath, and any rewrite would sit on the same aggregators and break the same way. what a one-person rewrite could actually fix is the matching, so an incoming transaction never lands in the wrong account without asking you first.

---

> **Spirited_Substance32**（1 分） · 2026-10-31T10:33:43+08:00　
> Great idea and I'm assuming it's been tried to be done before. People you're reaching out to on here I'm assuming would usually just if they really needed it create their own.
>
> But that's only a small percentage of your potential customers.

---

> **lucidmatter**（1 分） · 2026-10-31T10:34:13+08:00　
> Next do TurboTax!

---

> **weedmylips1**（2 分） · 2026-10-31T10:51:38+08:00　
> There's already one. It's called freetaxusa.com

---

> **lucidmatter**（1 分） · 2026-10-31T11:05:07+08:00　
> Well, I guess we did it. Job well done everyone!

---

> **fourthwaiv**（1 分） · 2026-10-31T11:22:56+08:00　
> I've been working on an entire wealth management suite to manage my trading retirement accounts taxes everything.

---

> **fishyphotos**（1 分） · 2026-10-31T14:09:50+08:00　
> Have you looked into plaid pricing? I did in the past and i remember there being some type of limits for development api keys, and their prod connections are pretty expensive.

---

> **fishyphotos**（1 分） · 2026-10-31T14:11:46+08:00　
> i spread the good word about freetaxusa whenever i can. turbotax blows.

---

> **fishyphotos**（1 分） · 2026-10-31T14:14:35+08:00　
> What is it that is so good about quicken that other softwares don’t have? like tax prep or something ? (i’ve only tried quicken simplifi on mobile. )

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
