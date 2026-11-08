---
type: "corpus"
item_id: "92e06ff497ebb12d"
title: "Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50406292"
project_url: "https://github.com/hedgerow-dev/coldframe"
author: "hedgerow-dev"
published_at: "2026-11-07T17:27:30Z"
captured_at: "2026-11-08T12:50:31+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - hn_show
  - author_hedgerow-dev
  - story_50406292
  - show_hn
  - front_page
metrics: {"points": 207, "comments": 44, "engagement_velocity": 207}
comments_count: 44
comments_total: 44
discovered_via: "hn:show_hn:3d"
---

# Show HN: Coldframe, a honeypot that poses as a supermarket fridge controller

> [!info] 一句话导读
> I built Coldframe, a honeypot that pretends to be a supermarket refrigeration controller. Inspired by the events on industrial fridge installations in the past …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50406292>
> 指标：点赞=207 · 评论=44 · engagement_velocity=207
> 作者：hedgerow-dev　|　发布：2026-11-07T17:27:30Z
> 项目链接：<https://github.com/hedgerow-dev/coldframe>
> 采集：2026-11-08T12:50:31+08:00　|　id：`92e06ff497ebb12d`

## 正文

I built Coldframe, a honeypot that pretends to be a supermarket refrigeration controller. Inspired by the events on industrial fridge installations in the past weeks, I wanted to see what people would try against a convincing fake.To learn more about this I built a honeypot that resembled perfectly the Danfoss AK-SM 800A and Dixell XWEB interfaces. Both of them are recognized on Shodan as real ones (an not as honeypots). It’s one Python file using only the standard library, and it builds on eppser/danfoss-ak-sm-decoy and public research by Synacktiv, Claroty and Ironhackers.Things that were fun to get right:- Matching real units. I used Shodan records of real devices to match header order, page titles, certificate fields and TLS versions. The Danfoss persona sends nginx headers in the same order as a real AK-SM 800A. The Dixell persona sends no Server header and pads its page to exactly 8,202 bytes.- Recognising exploit attempts. It recognises CVE-2025-41450, the Danfoss “code of the day” login bypass, and records whether the submitted code is correct for today. It also tags attempts targeting three other Danfoss CVEs and the XWEB vulnerabilities.- Letting them in. Default logins open a fake store dashboard with defrost buttons, so you see the second move, not just the first. Nothing behind it is real.Two instances have been live for a day. So far they’ve only seen generic scanners and Shodan’s crawler, which is called refrigerator.census.shodan.io.Feedback welcome, especially from anyone who has seen these devices in the field!

## 评论（44/44）

> **xrd** · 2026-11-07T17:41:50.000Z　
> Wait, I recall reading the threads about someone speculating there was a hack. Some people suggested it could just be that a large percentage of refrigeration units received a software update at the same time which resembled a hack.Is there a definitive story that someone actually did hack these units on a grand scale?

---

> **supriyo-biswas** · 2026-11-07T18:03:08.000Z　
> I would be very skeptical of anyone relying on Shodan data. At one point I was trying to write honeypots myself by replicating wifi cameras, but almost all the ones on the internet I found were honeypots of some sort, and the ones that weren't were already hacked and had their web pages replaced. In retrospect it would have probably been better to get a vulnerable device myself and probe it.If I were you, I would probably ensure that the fridges you used have residential or commercial (aka non-DC) IP addresses. Maybe Shodan uses this data for their "honeypot" label, my experience was some time ago so no idea though.

---

> **IshKebab** · 2026-11-07T18:05:05.000Z　
> The hilarious thing about this is that there was an initial hack, and then like a month later another one that was equally successful. Who could have possibly seen that coming lol.> Default logins open a fake store dashboard with defrost buttons, so you see the second move, not just the first.I think we're past the point where it's reasonable to expect people to not use AI for code, but their prose still sucks balls. You should at least write your submission here yourself, come on.

---

> **hedgerow-dev** · 2026-11-07T18:51:25.000Z　
> One thing keeps coming back, (and it's the story of industries where security and patching is an afterthought).a supermarket has no security team.
> If a fridge controller needs patching, a VPN and a strong password to be safe, that work has to come from the vendor or installer by default.
> One would hope that all these come by default or as a feature on these devices. It could even be a selling feature and not part of an expensive maintenance contract. A supermarket manager cannot be expected to do this work.

---

> **hedgerow-dev** · 2026-11-07T18:52:20.000Z　
> An extra insight, there was some news of 'blood banks' also being targetted. This is possibly a stronger (painful) target. It would demorelize people that are donors.
> https://www.independent.co.uk/tech/security/blood-hack-fridg...

---

> **morkalork** · 2026-11-07T18:53:35.000Z　
> You'd probably have more luck posing as other industrial hardware like HVAC, lighting, controllers for the kinds of pumps or valves you'd find in chemical plants. That kind of stuff.

---

> **vkaku** · 2026-11-07T19:30:47.000Z　
> Me reading it be like:MFs be doing everything but pulling those fridges off the Internet. Given the amount of TOR nodes, IP addresses today, Honeypots mean nothing ....Of course, it's my unpopular opinion. :)

---

> **DANmode** · 2026-11-07T20:27:56.000Z　
> Super cool, especially showing your work as FOSS, but: why announce your honeypot before it’s fulfilled its intended purpose once?

---

> **gukov** · 2026-11-07T22:50:29.000Z　
> Not a headline I ever expected to read. 2026 has been a wild year.

---

> **amelius** · 2026-11-07T23:03:39.000Z　
> The interesting aspect of these attacks was that they seemed to have been done per country.

---

> **asdf88990** · 2026-11-08T00:05:00.000Z　
> Did you write this post with AI?- Letting them in. Default logins open a fake store dashboard with defrost buttons, so you see the second move, not just the first. Nothing behind it is real.Given the context, this reads like vomit.

---

> **Melatonic** · 2026-11-08T01:29:32.000Z　
> Very cool. Seems like this is the modern hacker version of "is your refrigerator running?"

---

> **eterm** · 2026-11-07T18:02:37.000Z　
> There have been (at least) two separate waves to this now, which makes the "innocent broken update" speculation much less likely?

---

> **Bengalilol** · 2026-11-07T18:02:39.000Z　
> Now, as of November 2026, it is confirmed as a hack.Confirmed exploits, many manufacturers, experts, …

---

> **raizer88** · 2026-11-07T18:05:54.000Z　
> This type of attack lasted few days in different countries, quite hard to believe the fridge manufacturer could keep pushing these updates after all the news around.

---

> **embedding-shape** · 2026-11-07T18:23:33.000Z　
> > Is there a definitive story that someone actually did hack these units on a grand scale?Given the scope here (see map at https://en.wikipedia.org/wiki/2026_French_supermarket_refrig...), it'd either be individual hackers getting inspired from their neighbor hackers, or one actor targeting European countries.Although seemingly the hack wasn't so sophisticated, maybe it's truly just some kids fucking around with what they see being open, and maybe just want to target European countries for the "lulz" or whatever, who knows.

---

> **jknoepfler** · 2026-11-07T18:40:26.000Z　
> Fwiw, the first thread I recall was a speculative blog post about commissary freezers for the US military: https://news.ycombinator.com/item?id=49508506

---

> **Muromec** · 2026-11-07T20:11:27.000Z　
> That's a known playbook. Stir up shit, then create an uplausible denial which will take experts some time to debunk. Once it's figured out the story was bs, put out another three. By the week end there is 10 narratives and nobody except the field experts is sure that it's the usual suspects doing the usual things, but nobody listens to those

---

> **hedgerow-dev** · 2026-11-07T18:21:46.000Z　
> At this point the honeypot I'm running is not marked as honeypot. Guess that it's a good sign?

---

> **hedgerow-dev** · 2026-11-07T18:25:34.000Z　
> I agree, I rushed this one a bit. Glad to share with the industry at least.

---

> **morkalork** · 2026-11-07T18:54:55.000Z　
> Crazy thing is, when the fridges in all those military bases were hacked people were initially in denial and the people noticing that it was just a little too coincidental to be happing simultaneously were called paranoid. Well who's paranoid now?

---

> **amenghra** · 2026-11-07T20:35:50.000Z　
> This is how it should work: supermarket wants to use high tech stuff such as connected fridges, they get a cyber insurance policy as part of all the other insurances they have. The insurer then has domain experts to figure out what the insured needs to do to meet a risk threshold (or they adjust fees accordingly).This model has worked fine for many other types of risks.

---

> **_kb** · 2026-11-08T03:02:50.000Z　
> That seems pretty location dependant. In Australia at least the two major supermarket chains are not insignificant (e.g. EBITDA ~$5 billion and ~$2.6 billion) and have large internal tech and cyber teams.I think this is more indicative of the plethora of technical debt and straight up technical negligence that's accompanied the past 10-15 years of internet connected everything. What's happening today is the predictable result of project based works funded by capex deploying assets (of all types) with no consideration of opex funding for the technology components.Just because a webserver is running in some physical device (fridge, camera, vacuum, washing machine, pump controller, lighting system, audiovisual equipment, access control system etc) does not magically exempt it from the same sort of ongoing sysadmin and maintenance you'd expect as a baseline for something running on standard compute. That applies equally to manufacturers publishing firmware, and the asset owners/service companies that have the responsibility to apply.

---

> **unglaublich** · 2026-11-07T18:57:45.000Z　
> Why would it, scarcity generally motivates

---

> **throwup238** · 2026-11-07T22:55:11.000Z　
> Plot twist: the hackers are members of the Van Helsing Society and the supermarkets were just a trial run in their war against the International Vampire Cabal.

---

> **hedgerow-dev** · 2026-11-07T18:57:16.000Z　
> New ideas are popping up. I started with fridges because of the recent attacks, but the code makes it easy to add personas. Electric car charing stations and coffee machines were my initial idea, but HVAC and building controllers are probably better ideas. Thanks!

---

> **hedgerow-dev** · 2026-11-07T19:33:38.000Z　
> Agreed, that's the real fix. The honeypot is just to see who's looking while they're still out there.

---

> **hedgerow-dev** · 2026-11-07T20:34:17.000Z　
> The more people that can deploy it, the higher the chance of discovering something about the attacks. Also this gave me an incentive to look deeper into the real software.

---

> **Crunchified** · 2026-11-07T23:46:18.000Z　
> It's been a wild year from a suburbanite perspective. There's still a long way to go before real wilderness is witnessed.

---

> **msephton** · 2026-11-07T22:19:57.000Z　
> Unless they push updates in waves, which is what most big rollouts do.

---

> **hedgerow-dev** · 2026-11-07T18:24:31.000Z　
> My view is that some companies installing this have not implemented any defense in depth and cut corners all around. Installing a firewall with a simple vpn service would probably have prevented lots of pain (unfrosting).
> In general we also see almost every security expert working at banks or other high paying companies and not for supermarkets.
> My feeling is that this 'niche' is probably interesting to spend some 'tokens' and time on.

---

> **hedgerow-dev** · 2026-11-07T18:27:22.000Z　
> It's most certainly a form or hybrid warfare. While being very easy to perform, it's still quite effective. Empty supermarkets and supply chains being disturbed.
> Hopefully this is a wakeup call for the industry.

---

> **wiml** · 2026-11-08T03:39:46.000Z　
> That's the first of four incidents I've seen in the news recently. As far as I know it's the one that could have been some other kind of correlated failure (bad update, calendar bug, whatever). We don't know much about it.After that were two separate supermarket events, which I think were both linked to the known Danfoss vulnerability (CVE-2025-41450); and most recently a blood bank event.

---

> **gruez** · 2026-11-08T02:23:24.000Z　
> Examples of this happening in the past?

---

> **supriyo-biswas** · 2026-11-07T18:28:31.000Z　
> What I meant is that I'd find some way of ensuring that I'd want to ensure that the responses you're serving up are real. If you are happy with what you have, we're good.

---

> **realty_geek** · 2026-11-07T19:42:23.000Z　
> TBH, I think at this point it is the "holier than thou" people pointing out every instance of slightly AI sounding text that are getting annoying.I was happy reading you post and I imagine there are many many more people like me than the grinch.

---

> **hedgerow-dev** · 2026-11-07T20:41:50.000Z　
> Many of these supermarkets are part of big brands but operate independently. I doubt cyber insurance is top of mind for those small owners

---

> **tough** · 2026-11-07T19:45:27.000Z　
> One could say blood is a fluid market that responds well to offer and demand

---

> **noir_lord** · 2026-11-07T18:40:02.000Z　
> > Hopefully this is a wakeup call for the industry.Would be nice but none of the other  events has been.It seems like something horrific is going to have to happen before this is taken as seriously by government and private orgs as it should have been, that seems to be how it works with other stuff historically.

---

> **hedgerow-dev** · 2026-11-07T18:43:17.000Z　
> Fair point and I agree, Shodan isn't the only source. For the reason, for Danfoos the login page comes straight from the firmware package that Danfoss publishes. It's byte for byte identical, so it hashes the same as thousands of real units. Dixell was matched against Shodan records, so that one is weaker, you’re right.The datacenter IP is the bigger tell. Real controllers sit on shop or ISP connections. Moving one decoy onto a residential line is on my list.Along the way I did some hunting for vulnerabilities on the Danfass units, quite interesting stuff actually.

---

> **hedgerow-dev** · 2026-11-07T19:48:17.000Z　
> Thanks! To be honest, using AI helps 'gettings things out' instead of shelving it because it's never perfect.

---

> **IshKebab** · 2026-11-07T21:01:36.000Z　
> > I think at this point it is the "holier than thou" people pointing out every instance of slightly AI sounding text that are getting annoying.I don't think it's unreasonable to spend literally 3 minutes writing your own submission. I'm not asking to rewrite every code comment.And it wasn't "slightly" AI sounding text. It's very obviously AI.

---

> **SoftTalker** · 2026-11-07T21:29:46.000Z　
> It will be soon. How many refrigerated cases of product can they afford to lose?

---

> **gruez** · 2026-11-08T02:22:36.000Z　
> Not to mention other ways cyberattacks can paralyze their business, eg. their POS system

## 导航

- 项目页：[[10-项目/github.com_75033d6b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
