---
type: "corpus"
item_id: "d57b28639c8f2770"
title: "I checked what ChatGPT, Claude and Google tell buyers about 17 SaaS prices. 3 got a flat-out wrong price, and some errors came from the companies' own docs"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1xdpvp2/i_checked_what_chatgpt_claude_and_google_tell/"
project_url: "https://pricingcited.com/"
author: "leonagano"
published_at: "2026-10-24T04:58:13+08:00"
captured_at: "2026-11-03T09:42:03+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-10-24"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 6, "comments": 10, "upvote_ratio": 1}
comments_count: 10
comments_total: 10
discovered_via: "reddit:14d+settle10"
---

# I checked what ChatGPT, Claude and Google tell buyers about 17 SaaS prices. 3 got a flat-out wrong price, and some errors came from the companies' own docs

> [!info] 一句话导读
> More buyers ask AI "how much does X cost?" before they visit the pricing page. I wanted to know how often the answer is wrong, so I tested it.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1xdpvp2/i_checked_what_chatgpt_claude_and_google_tell/>
> 指标：得分=6 · 评论=10 · 赞踩比=1
> 作者：leonagano　|　发布：2026-10-24T04:58:13+08:00
> 项目链接：<https://pricingcited.com/>
> 采集：2026-11-03T09:42:03+08:00　|　id：`d57b28639c8f2770`

## 正文

More buyers ask AI "how much does X cost?" before they visit the pricing page. I wanted to know how often the answer is wrong, so I tested it.

**Setup**

* 17 products: Notion, Cursor, beehiiv, MailerLite, Kommo, Webflow, n8n, Activepieces, Turso, WP Rocket, Plausible, Fathom, Tally, Kit, Carrd, Senja, Simple Analytics. 10 of them changed pricing in 2025 or 2026.
* 3 engines: ChatGPT (free, logged in), Claude with web search, Google AI Mode.
* One prompt for all: "How much does X cost? List each plan and its monthly price, and cite your sources."
* Every answer checked against the official pricing page on the same day.

**Results**

* 37 of 44 answers matched the official page exactly.
* ChatGPT: 13 of 17 fully right. Claude: 16 of 17. Google AI Mode: 8 of 10; for the other 7 it showed only links.
* 3 of 17 companies got a wrong price from at least one engine. 5 had some issue.
* Cursor changed its plans 11 days before the test, and all three engines had the new prices. Honestly better than I expected.

**Where it went wrong**

1. **Renamed plans.** beehiiv switched to Free/Lite/Pro on Oct 1. ChatGPT still described the old Launch/Scale/Max plans.
2. **Monthly vs yearly.** ChatGPT gave Kit's yearly rates ($33/$66) as the monthly price; monthly is $39/$79. Many pricing pages open on the yearly toggle. I misread two of them myself while building the answer key.
3. **Old review sites.** When Google skipped the official page, it quoted Simple Analytics' retired Starter and Business plans from third-party sites.
4. **The companies' own docs.** Kommo's knowledge base still shows an old $15 price. Kit's Help Center doesn't match its pricing page. Activepieces' pricing page contradicts itself on Free plan credits.

That last one surprised me most. AI isn't only reading your pricing page; it reads your help center too, and repeats whatever it finds there.

**If you run a SaaS**

* After a price change, ask ChatGPT, Claude and Google what you cost. Ask again a week later.
* Put the billing period next to every price.
* Search your help center and blog for old plan names and prices.
* Ask the review sites that list you to update.

**Caveats:** one run per product, from Brazil, free ChatGPT, small sample. AI answers vary between runs, so treat this as a snapshot.

I'm turning this into a tool, PricingCited, that runs the check on your own pricing page: is it cited, and is the price right? If you want yours checked, it's [**here**](https://pricingcited.com)

Happy to share the full per-company breakdown. Has anyone here caught AI quoting the wrong price for your product?

# Method, caveats and full results

We ran one test on Oct 23, 2026: 17 products, 3 engines, 51 queries. Every engine got the same prompt: "How much does {product} cost? List each plan and its monthly price, and cite your sources." For Carrd and WP Rocket, which bill yearly, the prompt asked for "its price".

* **Products.** 10 changed their pricing in 2025 or 2026. The other 7 are indie tools with stable pricing.
* **Engines.** ChatGPT (free, logged in, default mode), Google AI Mode, and Claude with web search. Perplexity was dropped after its sign-up wall blocked anonymous queries.
* **Cited** means the product's own pricing page, docs or help center appeared among the sources.
* **Correct** means no price claim contradicted the official page. A minor error is a wrong currency, a mislabeled row, or a labeled estimate that was off.

**Caveats.** One prompt and one run per product, from a single location (Brazil), on a small sample. AI answers vary from run to run, so treat these figures as a snapshot, not a rate.

**Products with an issue**

* **beehiiv** (changed). ChatGPT: wrong, old plan names. Google: links only. Claude: minor, monthly estimate off.
* **Kit** (indie). ChatGPT: wrong, yearly shown as monthly. Google: right, own page not cited. Claude: right.
* **Simple Analytics** (indie). ChatGPT: minor, £ instead of $. Google: wrong, retired plans, own page not cited. Claude: right.
* **MailerLite** (changed). ChatGPT: right. Google: minor, tier row mislabeled. Claude: right, own page not cited.
* **Turso** (changed). ChatGPT: minor, yearly rates under a monthly header. Google: links only. Claude: right.

**Right on every engine that answered**

* All three engines answered: Cursor, Fathom, Kommo (ChatGPT gave Brazil regional prices), Notion, Senja, Tally, WP Rocket.
* Google gave links only, ChatGPT and Claude right: Activepieces, Carrd, n8n, Plausible, Webflow.

By group, the 10 changed products had 1 wrong price across 25 scored answers. The 7 indie products had 2 across 19. The sample is too small to say pricing changes cause more errors.

## 评论（10/10）

> **BusinessStrategist**（1 分） · 2026-10-24T05:18:13+08:00　
> Many websites are blocking scrapers. Many websites hint at a price indirectly.
>
> Many websites just plain lie.
>
> The digital marketing goal of the website is to connect, engage, and get you on their "buyer journey map."

---

> **Acrobatic-Call1082**（1 分） · 2026-10-24T05:20:27+08:00　
> That last point about AI pulling from help centers is the real takeaway here. Most companies obsess over the pricing page but forget their knowledge base has three different price points scattered across outdated articles.
>
> I've noticed Claude tends to cite things more consistently than ChatGPT, which sometimes just pulls numbers out of thin air and presents them like gospel. The Kit monthly vs yearly thing is such an easy trap too, especially since most pricing pages default to annual billing with a tiny toggle somewhere.
>
> Actually surprised Google AI Mode even attempted answers for most of these, usually it just throws up its hands and shows a search snippet. That 8 out of 10 rate is higher than what I typically see.
>
> Your tool idea is clever, wonder if you could automate checking against help center docs too, since that's where a lot of the ghost prices live.

---

> **Beichler-Queku**（1 分） · 2026-10-24T07:18:45+08:00　
> did you notice if the pages with client-side rendered pricing tables fared worse than static html? wondering if some of these models are only falling back to third-party review sites because they cant parse the main pricing page properly.

---

> **leonagano**（1 分） · 2026-10-24T07:43:50+08:00　
> I've seen some people commenting about help centres. I think it would be good to check against it too, then, cross-check help centres and pricing pages
>
> I'll do it, for sure
>
> On Google, I overstated it: on the same base as the others it’s 8/17, not 8/10, since it gave links only for 7. Amended the post

---

> **leonagano**（1 分） · 2026-10-24T07:50:34+08:00　
> Some do. But most of the errors here weren’t companies hiding prices. They were companies with clear prices whose own old docs, or old review sites, still said something else. That part is fixable.

---

> **leonagano**（1 分） · 2026-10-24T07:53:01+08:00　
> That';s a good question. I don't know but will keep an eye on it

---

> **BusinessStrategist**（1 分） · 2026-10-24T13:30:33+08:00　
> A "smoke screen" is a "smoke screen."
>
> SaaS products and services are generally in continuous evolution.
>
> And many offer many options so that solutions can be tailored to specific needs.
>
> The "chief decider (the person releasing the funds" will more often than not makes the decision to buy if the investment brings in at least 2x the price + the cost of making any necessary changes in work methods.
>
> And the SaaS sales professional will have to SHOW the the decider as well as the user, and any influencers of the merits of your "compelling" offer.
>
> If you state a "fixed" price then you basically lose a large number of prospects who would buy if they were shown the specifics of how this tool would impact their "specific" business.
>
> So AI is basically reporting on the "smoke screens" and not on any solid market information.

---

> **tonecast_team**（1 分） · 2026-10-24T14:15:05+08:00　
> The help-center finding generalises, and the per-engine split explains the "Claude more consistent than ChatGPT" impression. In a citation dataset we collected on the same questions, Claude cited sources in 90% of answers and ChatGPT in 55%, and ChatGPT's 55% was exactly the share of answers where it decided to run a web search at all. The other 45% came from training data, which is where a retired plan name or a $15 that was true two years ago survives long after every page has been fixed. So "ask again a week later" works for the engines that searched; for the memory answers the only fix is being described consistently everywhere the next model will read, help center and review sites included.
>
> The monthly/yearly confusion is worth its own line in any price check: pages that open on the yearly toggle produce a wrong answer that is technically on the page.

---

> **sone94**（1 分） · 2026-10-24T22:46:36+08:00　
> Two additions to your checklist for SaaS owners. First, check robots.txt and your CDN/WAF rules: OAI-SearchBot (ChatGPT search) and GPTBot (training) are separate crawlers with separate rules, and plenty of sites blocked OAI-SearchBot by accident via generic 'AI bot' rulesets, which removes them from citations entirely no matter how clean the pricing page is. Second, check Bing indexing for your pricing page and docs. In a Pavado/BuzzStream study roughly 87% of ChatGPT's web citations overlapped Bing's top results, so a page Bing hasn't indexed or refreshes slowly can stay stale in ChatGPT even after you fix it. Your wrong-price cases all traced to stale text somewhere; these two checks cover the cases where the engine never saw the fresh page at all.

---

> **OracoreAI**（1 分） · 2026-10-30T21:38:38+08:00　
> I'd rather see monthly and annual prices side by side than behind a toggle. Give the humans a fighting chance too.

## 关联链接

- https://pricingcited.com

## 导航

- 项目页：[[10-项目/pricingcited.com_cf504ff4]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
