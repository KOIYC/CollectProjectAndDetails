---
type: "corpus"
item_id: "4478bd2febdae7e3"
title: "How I count assistant visits that arrive with no referrer"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1whe4i0/how_i_count_assistant_visits_that_arrive_with_no/"
author: "Kyryll_Bracemore"
published_at: "2026-09-16T05:53:22+08:00"
captured_at: "2026-09-26T09:42:55+08:00"
lang: "en"
kind: "post"
topic: SaaS/B2B
shard: "2026-09-26"
pub_day: "2026-09-16"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 5, "comments": 15, "upvote_ratio": 1}
comments_count: 23
comments_total: 23
discovered_via: "reddit:14d+settle10"
---

# How I count assistant visits that arrive with no referrer

> [!info] 一句话导读
> I count deep entries with no referrer as their own line in the report.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1whe4i0/how_i_count_assistant_visits_that_arrive_with_no/>
> 指标：得分=5 · 评论=15 · 赞踩比=1
> 作者：Kyryll_Bracemore　|　发布：2026-09-16T05:53:22+08:00
> 项目链接：—
> 采集：2026-09-26T09:42:55+08:00　|　id：`4478bd2febdae7e3`

## 正文

I count deep entries with no referrer as their own line in the report.

Here's how. I take two lists of pages. The first list comes from the report and holds every page that got direct entries this month. The second list holds the pages that answer questions about our category. I keep the pages that sit on both lists.

Nobody types a deep URL for a blog post from memory. So if that page also answers a category question, the visit most likely came from an assistant that didn't pass a referrer.

Then I cut the short visits by time on page. A visit of a few seconds is a bot most of the time.

That last step isn't mine. A founder ran this on his own site after we talked about it, and he came back with numbers. His direct deep entries lasted seconds. The visits he could tie to an assistant lasted minutes. So he started cutting the list by time on page, and now I do the same. One site, seven pages, his own method. So it's a hint, and I wouldn't build a benchmark on it.

It's rough. It's still better than a zero sitting in the report where a real channel should be.

Which pages show up in your report with no referrer at all?

## 评论（23/23）

> **AllenHere112**（1 分） · 2026-09-16T06:01:47+08:00　
> Your time cut will throw away the visits you're trying to find. Duration in most reports is the gap between two pageview hits, so a session that lands on a deep page, reads it and closes the tab logs a few seconds no matter how long the person stayed. One-page sessions are the normal shape of a visit that started with a question.
>
> I'd cut on events instead. What do those single-hit sessions do on your seven pages, and do any of them end in a signup?

---

> **Kyryll_Bracemore**（1 分） · 2026-09-16T07:03:48+08:00　
> You're right about the gap between two hits. I'm checking now to see if the report sends engagement events. Without them, my time cut measures the session shape. Those seven pages aren't mine. Their owner has the same report. His numbers may show the same shape.
> You said you'd cut on events instead. Which event fires early enough to keep a session that only ever sends one hit?

---

> **Easy_Stick9324**（1 分） · 2026-09-16T07:28:11+08:00　
> The overlap is a useful lead, but multi-minute dwell time is still a weak filter since referrers get stripped by apps, privacy tools, and redirects, so I’d label these “unattributed assistant

---

> **Kyryll_Bracemore**（1 分） · 2026-09-16T08:11:23+08:00　
> I rename this row in the records without a source. I compare the percentage of visitors without a referrer on the home page and on internal pages. Privacy tools remove the referrer everywhere in the same way. Assistant traffic is found only on question pages.
> You said referrers get stripped by apps, privacy tools, and redirects. Does that share look the same on your home page and on deep pages?

---

> **Different_Drawer_637**（1 分） · 2026-09-16T08:34:45+08:00　
> imo the weakest link here is assuming nobody types deep URLs. bookmarks and saved links in notes apps hit the same way, no referrer attached. might be worth checking if returning visitors skew the numbers before treating it all as assistant traffic

---

> **Kyryll_Bracemore**（1 分） · 2026-09-16T08:37:26+08:00　
> I split the list into new visitors and returning visitors. I keep only the new visitors. Bookmarks are in the returning group. This split works in any report. You said it might be worth checking if returning visitors skew the numbers. What share of your no-referrer deep entries are new visitors?

---

> **Ok_Gur_9033**（1 分） · 2026-09-16T08:46:58+08:00　
> I would check the supply side before trusting the overlap. I run the category queries against the engines myself and log whether my pages come back. ChatGPT has not retrieved mine once across six tested queries, Perplexity did on four of six. A page no engine ever cites is not the one sending you assistant traffic.

---

> **Kyryll_Bracemore**（2 分） · 2026-09-16T08:53:13+08:00　
> I log the citations for each page separately. I keep pages that have at least one citation. I compare this list with the no-referrer list. The overlap gives me my answer. Perplexity did on four of six

---

> **Ok_Gur_9033**（1 分） · 2026-09-16T09:28:30+08:00　
> Worth checking how stable that citation list is. One of my posts read absent on one run and came back as source two of seven a week later. I could not reproduce the first query exactly, so I would not call it a clean flip, but it was enough that I stopped treating the cited set as fixed.

---

> **Kyryll_Bracemore**（2 分） · 2026-09-16T13:03:25+08:00　
> I store each query verbatim in a single file. I rerun the same file every week. I count the number of hits for each page. This approach replaces my previous “yes or no” method. You said you could not reproduce the first query exactly. Do you keep the wording of each query saved anywhere?

---

> **Ok_Gur_9033**（1 分） · 2026-09-16T14:45:14+08:00　
> I do save the wording. It just does not survive a rerun. Mine goes in a dated log, 69 entries, one prose paragraph per check. I pulled the distinct queries out of it today and got about 24. Only one has ever been rerun the same way four times.
>
> The rest drifted. The same intent is sitting in there under four wordings: best AI agents for ecommerce support, then the same with 2026 on the end, then with customer in the middle. That is four result sets I logged as one. Your single file is the part I got wrong.

---

> **Kyryll_Bracemore**（2 分） · 2026-09-16T16:49:14+08:00　
> I group the queries by intent. I choose one phrasing for each intent. That phrasing remains fixed. I log the other phrasings as variants under the same intent.
>
> You said you pulled the distinct queries out of it today and got about 24. How many separate intents are those 24 actually?

---

> **Ok_Gur_9033**（1 分） · 2026-09-16T20:35:54+08:00　
> I grouped them. Once I drop the fragments I was double counting it is 21 distinct wordings, and they collapse to 15 intents. Only four of those intents carry more than one wording. The ecommerce agents one holds four by itself and the other three are simple pairs. So 11 of the 15 were already a single phrasing and were never the problem. My drift is concentrated in one intent, not spread across the log.

---

> **Kyryll_Bracemore**（2 分） · 2026-09-16T23:01:11+08:00　
> I repeat the same phrasing on the same day every month. I save the answer under that date. I compare the two answers for each phrasing. The other wordings are excluded from the comparison. You said your focus is on a single intent. Which of those four wordings do you keep as the fixed one?

---

> **Ok_Gur_9033**（1 分） · 2026-09-17T14:46:40+08:00　
> Two of those four are not mine to fix. I typed two of them. The other two came out of Bing Webmaster's grounding query table, which reports the wording real people actually used. The 2026 one sits in there at 11 citations and 55 percent share. I never chose it and I cannot hold it still, because next month that table reports whatever got asked next.
>
> So the fixed one is best AI agents for ecommerce support, nothing on the end. It is the only one of the four I have put to three engines on the same day. The platform reported half of the intent stays a variant list I read, not a query I rerun.

---

> **Kyryll_Bracemore**（1 分） · 2026-09-17T20:57:29+08:00　
> Every month, I save the entire list of options. I compare the new list with the old one. New phrasings indicate a new intent to me.
>
> I don't review this list again.
>
> You said that half of the intents remain on the list of options you reviewed. Which phrasings from this month's list weren't on last month's list?

---

> **Ok_Gur_9033**（1 分） · 2026-09-20T17:41:33+08:00　
> I cannot answer that yet, and the gap is mine. I have one snapshot of that list, 14 distinct queries from late August, and nothing from September to diff it against. I have been treating a single pull as a series.
>
> What the snapshot does show: AI multilingual support agents US ecommerce sits at 75 citations and 30 percent share. The intent I have been calling my main one carries 11. The bigger query was in the file the whole time and I never worked it.

---

> **Kyryll_Bracemore**（2 分） · 2026-09-20T18:39:23+08:00　
> I choose the query with the most citations.
>
> I'm reading our page for that query. ← Copy-paste, do not translate
>
> I write a new page for it. You said: "The bigger query was in the file the whole time."
>
> Which page on your site answers that query today?

---

> **Ok_Gur_9033**（1 分） · 2026-09-20T18:46:03+08:00　
> Two pages, and neither one answers it.
>
> The multilingual guide uses that word eleven times and the word ecommerce zero times. The ecommerce support guide runs the other way, fifteen mentions of ecommerce and twelve of support agent, multilingual zero. Neither says US anywhere.
>
> So the query carrying the most citations I have is being answered by two halves that never reference each other. I had been reading that citation count as a page winning. Looks more like it gets picked because nothing closer exists.
>
> When you hit one of those, do you write the new page or rewrite whichever existing page is closest?

---

> **Kyryll_Bracemore**（2 分） · 2026-09-20T18:48:25+08:00　
> I keep both old pages unchanged.
>
> I'm writing one new page for the entire query.
>
> I add links from the new page to both old ones. You said: "it gets picked because nothing closer exists."
>
> Which of those two pages carries the citations now?

---

> **Ok_Gur_9033**（1 分） · 2026-09-20T18:52:01+08:00　
> Neither, as far as my own data can actually prove, and that is the part worth saying.
>
> The 75 citations come out of Bing's grounding query table. That table lists queries and citation counts and never names a URL. My per page citation counts come from Search Console's AI features, a different provider entirely. The two numbers were never joined, and I had been reading them as one measurement.
>
> Looking at the page side, neither of the two pages I named to you is even in it. The top five are best-ai-agents-ecommerce-support at 84, nearshore-saas-development-guide at 47, mvp-development-cost at 45, digital-process-automation at 41, ai-agent-development at 35.
>
> So the new page you are describing would be built on a link I cannot demonstrate. How do you tie a query in one provider's report to a URL in another one's?

---

> **Kyryll_Bracemore**（2 分） · 2026-09-21T03:47:15+08:00　
> I keep two reports separate. I'm running that query myself and saving the URL it references.
>
> I write down this URL next to the query. You said: "The two numbers were never joined."
>
> Which URL does the assistant cite when you run that query yourself?

---

> **AutoModerator**（1 分） · 2026-09-21T03:59:36+08:00　
> Your comment was removed. Links in comments require to gain karma first in r/SaaS. Earn sub karma by commenting helpfully first.
>
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/SaaS) if you have any questions or concerns.*

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`SaaS/B2B`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
