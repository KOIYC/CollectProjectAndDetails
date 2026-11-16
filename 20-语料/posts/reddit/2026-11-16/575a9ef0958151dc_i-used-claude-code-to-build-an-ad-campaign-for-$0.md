---
type: "corpus"
item_id: "575a9ef0958151dc"
title: "i used claude code to build an ad campaign for $0.46"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xotxmj/i_used_claude_code_to_build_an_ad_campaign_for_046/"
author: "Fun-Meaning-6474"
published_at: "2026-11-06T04:51:46+08:00"
captured_at: "2026-11-16T10:01:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-06"
tags:
  - 语料
  - reddit
  - r/EntrepreneurRideAlong
  - Resources & Tools
metrics: {"score": 78, "comments": 26, "upvote_ratio": 0.9642857142857143}
comments_count: 24
comments_total: 26
discovered_via: "reddit:14d+settle10"
---

# i used claude code to build an ad campaign for $0.46

> [!info] 一句话导读
> i have a small business and i used to create ads myself. i'd look up the keywords through google keywords, look up what my competitors were doing, and try to cr…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xotxmj/i_used_claude_code_to_build_an_ad_campaign_for_046/>
> 指标：得分=78 · 评论=26 · 赞踩比=0.9642857142857143
> 作者：Fun-Meaning-6474　|　发布：2026-11-06T04:51:46+08:00
> 项目链接：—
> 采集：2026-11-16T10:01:55+08:00　|　id：`575a9ef0958151dc`

## 正文

i have a small business and i used to create ads myself. i'd look up the keywords through google keywords, look up what my competitors were doing, and try to create it myself. I used to look up keywords through google keywords but ended up running google ads campaigns that weren't giving me any clients.

So i went looking for tools. found Semrush as the first option and decided to try it. got the cheapest version but it was super limited, i felt like i was giving money out for nothing. it would always tell me that i needed to upgrade. i just didn't have the budget for it, so i quit.

i also have a claude code pro subscription, and i know people use it for business optimizations, so i tried doing it with it. but it didn't have access to the any ad tools, so it couldn't give me much:

The keywords in first claude output was:

|Ad group|Keywords|
|:-|:-|
|Mobile detailing|mobile car detailing, mobile auto detailing killeen, mobile detailing near me, car detailing that comes to you|
|Interior|interior car detailing, car carpet cleaning, pet hair removal car, seat stain removal|
|Truck/SUV|truck detailing killeen, suv detailing, lifted truck wash|
|Engine/tires|engine bay cleaning, engine detailing|
|Premium|paint correction killeen, ceramic coating killeen, car scratch removal|
|City ads|the same set with Harker Heights, Copperas Cove, Temple, Belton, Salado|

i wanted to see if there are ways to do it better with claude code, and i found an mcp that promised to build an optimized ad campaign for under $1. i was kinda skeptical but decided to give it a try.

spoiler: it actually did, for $0.46 total.

here's what i gave it as a prompt:

>“connect aiml api mcp (that’s the mcp i used) and create an optimized ad campaign for my company \[i pasted my website link\]

>create an optimized ad campaign for my company
>
>\[my company website\]

Claude code already had access to my google ads account.

i was curious about what it did, so i asked what it used. attaching a claude code output:

**Search campaign**

|Step|Tool|Calls|Cost|
|:-|:-|:-|:-|
|Check the landing page|`dataforseo/onpage-content-parsing`, `dataforseo/onpage-lighthouse`|1 each|$0.007|
|Get keyword ideas from the site|`dataforseo/keywords-google-ads-keywords-for-site`|1|$0.117|
|Get keyword ideas from 20 seed terms|`dataforseo/keywords-google-ads-keywords-for-keywords`|1|$0.117|
|Find rival advertisers|`dataforseo/serp-google-ads-advertisers`|6|$0.009|
|Pull their ads|`dataforseo/serp-google-ads-search`|6|$0.009|
|Check which ads show on live searches|`litescrape/google-ads`|10|$0.002|
|Sort keywords into buyers, other brands and junk|`typesafe/jev-router`|2–4|\~$0.05|
|Forecast clicks and cost|`dataforseo/keywords-google-ads-ad-traffic`|1|$0.117|
|Write ad groups, ads and negative keywords|`typesafe/jev-router`|1|\~$0.03|
|Total|||≈ $0.46|

so it went to my website with the Data for Seo tool, analyzed it, pulled keywords, found my competitors’ ads, used Litescrape to see which ads would pop up in search results, pulled and sorted the keywords to check which ones would bring me clients, forecasted clicks and click costs, then wrote ads and sorted them out to pick the ones that are supposed to work best.

after running all that, it set up the whole campaign in my google ads account and asked for my ok to launch it.

i also asked which keywords it used, and it gave me this list, CPC included:

claude code outputs:

**Recommended keywords**

**Tier 1: core, most of the budget**

|Keyword|TX searches/mo|CPC|
|:-|:-|:-|
|mobile detailing near me|5,400|$3.98|
|mobile car detailing / mobile auto detailing|2,900 each|$5.48|
|car detailing near me|27,100|$3.03|
|auto detailing near me|6,600|$2.59|
|car detailing killeen (and “killeen tx” variants)|320|$2.33|
|car detailing temple tx|170|$1.86|
|interior car detailing|1,300|$3.78|
|interior detailing near me|590|$4.05|

Many “car detailing near me” searchers want a shop, not a mobile service. Put “mobile” and “we come to you” in the ad copy to filter them, and watch the search terms report closely.

**Tier 2: cheaper and useful**

|Keyword|TX searches/mo|CPC|
|:-|:-|:-|
|truck detailing (low competition)|210|$3.05|
|engine bay cleaning|720|$1.30|
|car wash and detail|2,400|$1.96|
|mobile car wash / mobile car wash near me|1,600 / 1,000|$2.68 / $2.38|
|car detailing prices|720|$1.58|
|mobile detailing cost|720|$1.58|
|how much is car detailing|390|$1.27|

The price-shopper terms are cheap, but they only work once your site shows prices.

**Tier 3: test with a small budget, only if you really offer it**

|Keyword|TX searches/mo|CPC|
|:-|:-|:-|
|paint correction near me|1,000|$3.53|
|paint correction|1,300|$4.42|
|ceramic coating near me|2,900|$8.28|

if you want to try it:

* give claude access to your website and google ads account. mine was already connected through my browser.
* use the prompt above. i'd also ask it to check the tool prices first
* check the keywords, ads and budget before anything goes live. ask it to show you the data behind its suggestions too.

that $0.46 covered putting the campaign together. whether it brings in clients is the next thing to measure.

anyone else tried using claude code for google ads for their own business? how did it go?

## 评论（24/26）

> **10DollarSecret**（7 分） · 2026-11-06T05:27:46+08:00　
> Thanks for spending the time to add all the details.

---

> **AutoModerator**（1 分） · 2026-11-06T06:15:27+08:00　
> Your [comment](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xotxmj/i_used_claude_code_to_build_an_ad_campaign_for_046/19s74hpvex5mo/) in /r/EntrepreneurRideAlong was automatically removed because it contained a URL or a markdown link.
>
> To keep our community focused and prevent spam, we do not allow URLs or links (including Reddit internal links) in comments at this time.
> If you believe this removal was a mistake, please [contact the moderators](https://www.reddit.com/message/compose?to=/r/EntrepreneurRideAlong).
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/EntrepreneurRideAlong) if you have any questions or concerns.*

---

> **smashballoonjoel**（2 分） · 2026-11-06T06:20:08+08:00　
> I haven't tried this specific approach but I might do something like it! Thanks for the inspiration and I'll check back in if I try it + how it goes.

---

> **Alarmed_Turnip_7023**（1 分） · 2026-11-06T06:25:12+08:00　
> Salado has like 2,000 people, I don't think anyone there is googling "ceramic coating". Killeen is basically Fort Hood though, so half your market is a 19 year old with a Charger at 24% APR who wants the engine bay spotless for the inspection

---

> **Fun-Meaning-6474**（4 分） · 2026-11-06T06:40:55+08:00　
> you are welcome!! I am open to questions!

---

> **Fun-Meaning-6474**（2 分） · 2026-11-06T06:41:32+08:00　
> share your experience. i will be glad to hear any new use cases of optimization

---

> **Royal-Somewhere-8918**（3 分） · 2026-11-06T07:28:43+08:00　
> Cheap to set up, but the real test is cost per booking. Are you tracking which keyword actually turns into a job, or just clicks for now?

---

> **Pink_Sky_8102**（1 分） · 2026-11-06T08:01:37+08:00　
> That’s actually a pretty interesting use of claude code. The $0.46 part is cool. I’d be really curious to see the results after a few weeks though. Building the campaign cheaply is one thing, but whether those keywords actually turn into booked customers is the part that matters.

---

> **TannerPines**（4 分） · 2026-11-06T11:46:38+08:00　
> But did it work? Did your conversions go up?

---

> **This-Ad-4174**（1 分） · 2026-11-06T16:29:58+08:00　
> You're paying for a click, not a customer. At $3 to $8 a click, a lot of your budget goes to people who are just browsing or comparing prices, and your own report says many searchers want a shop, not a mobile service.
>
> Use intent leads instead. They're the same people your ads are chasing, people already looking for your service, found for about a fifth of the cost. Look for people asking for a detailer in local groups, new car owners in your area, and businesses with vehicles, like dealerships, fleets and property managers.
>
> They already want what you sell, so they're much easier to close, and one fleet client can be worth more than 50 ad clicks. i did this, it works. ads are too expensive

---

> **Harmondale1337**（1 分） · 2026-11-06T16:44:12+08:00　
> Thanks for the full detail. Honestly I used to do it by myself via Claude because I wanted to keep this cheap as you (and it was, I was astonished by how you can create creatives this fast and with so much quality), but then I decided I will not try to save few bucks on a campaign management
>
> I found some sort of exotic tool for ad management (If I remember well it covers all the social platforms) named GetMCPAds, and since I’ve used it it truly manages my campaigns (not only reports, also alerts and guardrails) I think I’m paying something like 20 or 30$ per month and that’s enough for me as I’m not spending more than 1k/month in ads
>
> I think tho that you’re not in a competitive niche as I am, that’s why maybe it would not be as interesting for you than it is for me

---

> **Lazy-Eye2200**（1 分） · 2026-11-06T17:39:58+08:00　
> Congrats on getting it done for $0.46. I'd still treat the campaign as a guess until people respond to it. Cap it at $5 to $10 a day for the first week or so, and judge it by calls and quote requests, not clicks.

---

> **Fun-Meaning-6474**（1 分） · 2026-11-06T18:01:49+08:00　
> not yet. i wanna try to optimise that campaign with claude too and compare percent of shit no buyers keywords. the main hypothesis was comparing keywords via seo tools by intent like is there commercial SERP or educational

---

> **Fun-Meaning-6474**（2 分） · 2026-11-06T18:02:44+08:00　
> i can’t make decisions right now, i will optimise that campaign via claude and i wanna try aiml api jev decision model scoring buyers intent of my keywords

---

> **Lifenerd5**（1 分） · 2026-11-06T22:26:04+08:00　
> Saving for later to read

---

> **Royal-Somewhere-8918**（1 分） · 2026-11-07T07:21:46+08:00　
> makes sense. how do you tell a buyer keyword from just browsing though? like what would you check first, the search results or what people actually click?

---

> **y3rk3**（1 分） · 2026-11-07T15:03:15+08:00　
> check the clicks after the search first. the results page shows what people could want, but a buyer usually shows up as a click to a pricing page, a demo or a comparison, not just a read. keep a short list of the queries that bring those clicks, then see whether the same queries turn into sales. a keyword that brings reading but no clicks stays in the browsing pile.

---

> **Naaack**（2 分） · 2026-11-07T18:55:14+08:00　
> I mean, great? The 0.whatever you spent setting it up us irrelevant it you're going to be spending 3 - 8 USD per click and then your CAC ends up around 40, 50, 60.
>
> Until you know what that comes to the cost of the setup is irrelevant and this just reads like an MCP ad or promotion.

---

> **karateexplosion**（1 分） · 2026-11-08T02:37:09+08:00　
> I really appreciate you taking the time to write this up.

---

> **Royal-Somewhere-8918**（1 分） · 2026-11-08T07:22:31+08:00　
> yeah that makes sense, clicks to pricing/demo is a way cleaner signal than search volume alone. the short list idea is solid, keeps it simple

---

> **y3rk3**（1 分） · 2026-11-08T13:42:22+08:00　
> yeah search volume looks great on paper but a click through to the pricing page is someone actually shopping, which is way closer to a buyer. keep the list short though. the longer a keyword list gets the less anyone checks it and the more budget it quietly eats

---

> **Royal-Somewhere-8918**（1 分） · 2026-11-09T07:20:20+08:00　
> fair point, a long list just sits there unchecked. do you cap it at a number or just cut anything that hasn't brought a pricing click after a while?

---

> **y3rk3**（1 分） · 2026-11-09T13:41:32+08:00　
> set the rule before you start, not after. something like: if it has no click by the next time you review it, it goes. then review on a fixed day so the list cant just sit there.

---

> **Royal-Somewhere-8918**（1 分） · 2026-11-10T07:27:50+08:00　
> yeah, that's a clean rule. the fixed review day is the part i'd forget, without it the list just grows.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
