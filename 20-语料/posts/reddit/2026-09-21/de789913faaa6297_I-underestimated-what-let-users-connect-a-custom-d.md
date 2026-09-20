---
type: "corpus"
item_id: "de789913faaa6297"
title: "I underestimated what \"let users connect a custom domain\" actually takes. Sharing what I learned."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/indiehackers/comments/1tsu4f7/i_underestimated_what_let_users_connect_a_custom/"
author: "Jonathan_Geiger"
published_at: "2026-05-31T20:33:26+08:00"
captured_at: "2026-09-21T03:01:10+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-05-31"
tags:
  - 语料
  - reddit
  - r/indiehackers
  - Sharing story/journey/experience
metrics: {"score": 15, "comments": 47, "upvote_ratio": 0.800000011920929}
comments_count: 56
comments_total: 56
discovered_via: "reddit:144d+settle3"
---

# I underestimated what "let users connect a custom domain" actually takes. Sharing what I learned.

> [!info] 一句话导读
> A friend asked me last week how hard it would be to add custom domains to his SaaS. I told him "two weeks." He's now two months in and not done.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/indiehackers/comments/1tsu4f7/i_underestimated_what_let_users_connect_a_custom/>
> 指标：得分=15 · 评论=47 · 赞踩比=0.800000011920929
> 作者：Jonathan_Geiger　|　发布：2026-05-31T20:33:26+08:00
> 项目链接：—
> 采集：2026-09-21T03:01:10+08:00　|　id：`de789913faaa6297`

## 正文

A friend asked me last week how hard it would be to add custom domains to his SaaS. I told him "two weeks." He's now two months in and not done.

This is the post I wish I'd had three years ago when I made the same mistake at my own company.

What you actually have to build, in rough order of how soon it bites:

- **Multi-tenant TLS termination.** A cert per customer hostname. Let's Encrypt has rate limits (50 new certs per registered domain per week, 5 duplicate certs per week, 300 pending authz). Hit them once and customer onboarding goes dark for days.
- **An ACME on-demand flow.** Issuing certs ahead of time means knowing every customer hostname in advance. Issuing on first SNI hit means an "ask the control plane if this hostname is legit" loop before LE issues — otherwise an attacker can DoS your rate limit.
- **DNS validation.** Customers paste a hostname, you give them a CNAME, you poll until it resolves. Cloudflare caches your NXDOMAIN for 30 minutes. Public resolvers don't. You learn this at 2am.
- **Renewal.** ACME certs are 90 days. You need a renewal worker, retries, backoff, and per-customer failure alerts (because renewals will fail).
- **DNS drift.** Customer flips on Cloudflare proxy 60 days after going live. Your renewal silently breaks. Cert expires. You don't notice until support pings about a 404.
- **Edge routing.** The customer's hostname hits your edge, you look up which tenant owns it, you reverse-proxy. Latency budget is now critical because every customer request pays this hop.
- **A monitoring fleet.** At 50 customers you can cron-check each one. At 5,000 you can't. You build sampling. You build alert ladders (30/7/1 day expiry). You build DNS drift detection. You add a Slack channel called #domains-on-fire.

Each of those is a small project. Together they're a quarter of engineering, then ongoing care forever.

I built this all myself the first time. Sold the SaaS, joined another company, watched the team there go through the same arc. Eventually built **Domainee .dev** so I'd stop watching engineers do this from scratch every other year.

If you're at the start of this and your gut says "two weeks," at least double the list above before you commit. The platform engineering eats more time than the user-facing feature.

What did the rest of you learn the hard way?

## 评论（56/56）

> **stackscope**（1 分） · 2026-05-31T20:51:49+08:00　
> for another project of mine I went through the same-ish motions, if you got the time and energy setup domainconnect as well, it's great ux for customers and makes dns setup for the end user with certain providers i.e cloudflare a breeze

---

> **TimelyRepeat4517**（0 分） · 2026-05-31T21:34:30+08:00　
> The "two weeks" estimation trap is universal. The feature itself is two weeks,the edge cases, the failure modes, the monitoring,the 2am incidents, that's the other two months.
>
> My version of this with Flowara: "I'll just add invoice generation, should be straightforward." Three months later after handling tax rounding, multi-currency, EU VAT rules, PDF layout edge cases across paper sizes, and template system.
>
> The lesson I keep relearning: estimate the happy path, then multiply by 3 for the unhappy paths, then add another 50% for the things you didn't know you didn't know.
>
> What made you decide to productize Domainee after selling the first SaaS rather than just documenting the pattern?

---

> **Cultural-Mixture1949**（1 分） · 2026-05-31T21:45:14+08:00　
> "Custom domains are a feature" vs "custom domains are an ongoing operational responsibility" is probably the biggest takeaway here.
>
> The initial implementation gets all the attention, but renewals, DNS drift, and monitoring are where the real maintenance cost shows up.

---

> **SlowPotential6082**（1 分） · 2026-05-31T22:03:08+08:00　
> Been down this exact rabbit hole and you missed the biggest gotcha - DNS propagation debugging becomes your full time job. Half your support tickets will be "my domain isnt working" when they pointed their CNAME to the wrong thing or their TTL is set to 24 hours.

---

> **GearTakes**（2 分） · 2026-05-31T22:09:52+08:00　
> Thanks, bot.

---

> **GearTakes**（7 分） · 2026-05-31T22:10:47+08:00　
> "Chatgpt, create a random "helpful" post so I can spam my domain. Just make something up."

---

> **Jonathan_Geiger**（-2 分） · 2026-05-31T22:12:07+08:00　
> AI wrapper lol
>
> It’s no even an ai product

---

> **Cultural-Mixture1949**（-1 分） · 2026-05-31T22:15:44+08:00　
> No I am not brother but was funny just new to reddit

---

> **GearTakes**（5 分） · 2026-05-31T22:28:46+08:00　
> No, you are not. But the first post obviously was. Stop pretending it wasn't. It was 100% AI written.

---

> **crossoverXYZ**（3 分） · 2026-05-31T22:38:16+08:00　
> yeah the indie path is rough sometimes but lessons stick. keep going

---

> **Common_Dream9420**（-1 分） · 2026-05-31T22:47:28+08:00　
> the DNS drift one is brutal because it's completely silent. customer makes a config change on their end, your renewal breaks, and you have no idea until the cert expires 60 days later and someone's site goes red. we ended up building a daily drift checker just for that.
>
> the rate limit thing also hits different the first time. 50 certs/week sounds like a lot until you have a launch day.

---

> **Badsharishit**（2 分） · 2026-05-31T22:56:20+08:00　
> This is one of those features that sounds like a weekend project until you realize you're accidentally building a mini platform engineering team.

---

> **Badsharishit**（1 分） · 2026-05-31T22:56:54+08:00　
> "Estimate the happy path, then multiply by 3 for the unhappy paths" might be one of the most accurate rules in software engineering. Haha

---

> **imagiself**（1 分） · 2026-05-31T23:13:22+08:00　
> Working on PeerPush, an indie product directory built so AI assistants and LLMs can discover and recommend products through structured data, around DR 74.

---

> **Much-Wallaby-5129**（1 分） · 2026-05-31T23:30:08+08:00　
> custom domains are one of those features where the demo lies. the happy path is simple, but the product is really renewals, bad DNS, customer misconfiguration, cert expiry, and support at the worst possible time. the lesson for me is to price it like operational responsibility, not like a settings-page toggle.

---

> **_ishikaranka_**（2 分） · 2026-06-01T00:00:57+08:00　
> Honestly this perfectly explains why experienced engineers underestimate infrastructure work Real complexity usually appears after the feature already seems finished.

---

> **remyartemis**（1 分） · 2026-06-01T00:06:53+08:00　
> Multi-tenant TLS can be a nightmare if you try to tackle it as a one-off project. We found ourselves creating an entire DevOps pipeline just to handle certificates and renewals, thinking it would be a quick add-on. While Let's Encrypt helps save money, maintenance is where it really gets challenging. The DNS drift issue surprised us, and an automated alert system for DNS changes would've been a lifesaver. Don't underestimate the ongoing grind of monitoring and support. I've shared more details at compoundry.co if you’re interested.

---

> **imagiself**（0 分） · 2026-06-01T00:08:36+08:00　
> [https://peerpush.net](https://peerpush.net) is designed so that technical SaaS products like [compoundry.co](http://compoundry.co) can be discovered and mentioned by AI assistants through structured data.

---

> **amperdev**（1 分） · 2026-06-01T01:30:14+08:00　
> I think this is definitely where modern builders come up against the unfortunate truth of modern infrastructure. The tech world wasn't designed for the build-fast-launch-fast paradigm (although it is ever-trending more and more in that direction), and with good reason, but it means sometimes there are enormous hurdles to jump.

---

> **altoidbreeezy**（3 分） · 2026-06-01T04:28:36+08:00　
> Thanks LLM, very cool!

---

> **Jonathan_Geiger**（1 分） · 2026-06-01T04:29:16+08:00　
> No problem LLM, thanks!

---

> **altoidbreeezy**（1 分） · 2026-06-01T04:32:04+08:00　
> Let me know if you need any other post ideas — just say the word!

---

> **Jonathan_Geiger**（2 分） · 2026-06-01T04:33:17+08:00　
> Sure
> Go ahead, why not

---

> **International_Lack45**（3 分） · 2026-06-01T05:07:14+08:00　
> This list is painfully accurate. I built the same thing
> recently for my own static hosting platform, and you
> nailed every trap.
>
> The one that bit me hardest was exactly your DNS drift
> point. A customer flips on Cloudflare proxy weeks after
> going live, the orange cloud hijacks the connection, and
> on-demand TLS silently can't validate anymore. Everything
> looks fine until the cert expires and you get the 404
> ping. I now monitor for proxied records specifically
> because of this.
>
> One thing that saved me a ton of the work you described :
> I went with Caddy and its on-demand TLS instead of
> orchestrating ACME myself. You point it at an "ask
> endpoint" that confirms whether a hostname is a legit
> tenant before it issues, which handles your DoS / rate
> limit concern out of the box. Renewals, retries, and
> cert storage are all handled by Caddy too, which means I
> never had to build the renewal worker, the retry logic,
> or the storage layer you described. It doesn't solve the
> DNS validation or monitoring parts, but it removes a
> huge chunk of the cert lifecycle work.

---

> **punky-beansnrice**（2 分） · 2026-06-01T08:05:34+08:00　
> the DNS drift one bit me. customer turned on cloudflare proxy months later, renewal silently failed, cert expired on a sunday. now i alert on cert age + on the CNAME target changing

---

> **BarnacleBoy7**（2 分） · 2026-06-01T09:31:26+08:00　
> One thing I’ve learned building my own app is that the “simple feature” estimate is almost always wrong. The visible part looks like a weekend project, but then you find all the edge cases, maintenance, and support work hiding underneath it.
>
> I’ve started assuming every feature will take at least 2–3x longer than my first estimate.

---

> **mufenglabs**（2 分） · 2026-06-01T11:05:19+08:00　
> Nothing teaches humility like a feature estimate that starts with “this should be easy”

---

> **Otherwise_Economy576**（2 分） · 2026-06-01T13:10:46+08:00　
> custom domains are a classic iceberg — DNS verification, apex vs www, SSL provisioning, tenant routing, and 'why is my site still on your subdomain' support tickets.
>
> ship with CNAME-only first (www.customer.com → your app), document TTL wait times in UI, and defer apex/ALIAS until you have revenue to justify the edge cases.
>
> are you multi-tenant on one cert or per-customer certs?

---

> **Jonathan_Geiger**（1 分） · 2026-06-01T15:35:50+08:00　
> multi tenant 😄
>
> we give you or you saas the option to support custom domains for oyur users (like white lable)

---

> **frank_be**（2 分） · 2026-06-01T19:07:14+08:00　
> Wait till you learn about how AAAA wildcards can bite you 😄

---

> **Jonathan_Geiger**（1 分） · 2026-06-01T19:37:12+08:00　
> Already did 😅

---

> **quietoddsreader**（1 分） · 2026-06-01T20:56:26+08:00　
> this is one of those features that sounds tiny until you have to operate it. i've seen the same thing happen with auth, billing, and permissions. the implementation isn't usually the hard part, it's all the edge cases you inherit forever.

---

> **Sad_Data_7194**（1 分） · 2026-06-01T23:57:52+08:00　
> This is the most accurate post I've read on this. I'd add two items that bit us and that I don't see in your list:
>
> Wildcard vs per-hostname cert strategy. We started with per-hostname because it seemed "cleaner" and the wildcard cert option felt like a security smell. In practice the per-hostname approach has hidden cost: every new customer triggers a control-plane round trip and a brief window where the hostname is unprovisioned. Wildcard for paying tiers and per-hostname for the "bring your own domain" case ended up being the right balance, and we sleep much better.
>
> The CNAME at apex is the other trap. AWS CloudFront and several CDN providers can't do CNAME at the root domain — only subdomains. So your customer wants their SaaS at `acme.com` and you need to give them a workaround. ALIAS/ANAME records on Route53 or Cloudflare's CNAME flattening solve this but now you've coupled your onboarding to a specific DNS provider. We ended up writing a small explainer doc and eating the support cost, but the more elegant answer is to bake apex support into the cert issuance flow and accept the complexity.
>
> One thing I'd push back on: Let's Encrypt rate limits are a feature, not a bug. The 50/week hard cap is what makes a poorly-written renewal loop fail fast in dev instead of getting you banned silently in prod. I'd rather hit the rate limit and know.
>
> The 2am Cloudflare NXDOMAIN caching thing — we have a Slack channel called #dns-isnt-real where this exact class of issue lives. The 30-minute negative cache is a deliberate CF design choice, not a bug, and you have to design around it. Most DNS debugging at 2am is the negative cache.
>
> If your friend is going to be in this for a while, the cheapest investment is a fake customer onboarding test that runs cert acquisition end-to-end on every deploy. Caught more bugs for us than any other test we have.

---

> **danonino80**（1 分） · 2026-06-02T00:00:37+08:00　
> This is one of those features that looks trivial from the outside and turns into an entire infrastructure product once you start building it. Great reminder that the hardest part of SaaS is often the invisible operational complexity, not the UI customers see.

---

> **alvarotrigo**（2 分） · 2026-06-02T00:06:38+08:00　
> I just implemented this very recently in my own website editor.  But I managed to keep it way simpler by using Clouflare and registering their domain instead.
>
> What you said is 100% true, if the customer keeps DNS at their own registrar and you run your own ACME client. That's where the pain lives.
>
>  But flip the model and most of it evaporates: instead of taking the customer's existing domain, register it for them and delegate the whole zone to Cloudflare via nameservers. Once you control the registrar + NS + hand the zone to Cloudflare:
>
> \- TLS, cert issuance, LE rate limits, renewals = Cloudflare's problem. Zero cert code in my app.
>
> \- DNS validation polling = gone. Cloudflare auto-validates a zone it controls.
>
> \- DNS drift = the customer never touches DNS, so nothing drifts.
>
>  You're not free, you've just swapped which limits you hit (Cloudflare's zones/API limits instead of LE's) plus registrar orchestration. My real 2 am risks aren't certs. They're the register→ zone→ NS pipeline having no clean rollback, and someone moving nameservers off Cloudflare and silently killing DNS+TLS.
>
> So: control the domain and Cloudflare is that platform engineering. Customer brings their own and keeps DNS? Yeah, double your estimate for sure!

---

> **Overall_Weakness_433**（2 分） · 2026-06-02T02:02:23+08:00　
> The one that surprised me was how much of the problem isn't certificates at all, it's state management.
>
> The first few customers are easy. Then someone changes DNS, enables a proxy, points the wrong record, or leaves a stale CNAME behind, and suddenly you're debugging infrastructure you don't control. Even keeping domain ownership separate through something like dynadot doesn't save you from the support side of that.
>
> A lot of SaaS features look simple because the UI is a textbox and a Save button. The engineering work hiding behind that textbox is usually the real product.

---

> **SalaryDeep1034**（2 分） · 2026-06-02T02:06:20+08:00　
> Interesting

---

> **Ogbaudu**（2 分） · 2026-06-02T02:33:41+08:00　
> Wow you’ve really gone through a lot of progress. What I’m learning the hard way is marketing my product. I believe it’s a need I’m filling, but I know nothing about marketing. I’m finding out now that family and friends are most of the people that won’t believe in your startup which makes it harder, because they are the people they say should be sold on your product before anyone else. Thank you for sharing this information.

---

> **Jonathan_Geiger**（1 分） · 2026-06-02T03:12:56+08:00　
> Happy that it helped (:

---

> **imagiself**（1 分） · 2026-06-02T03:34:12+08:00　
> Since you're navigating the marketing learning curve, have you looked at [https://peerpush.net](https://peerpush.net) for visibility, as it's structured for AI assistant retrieval and connects makers with an indie audience looking to discover new tools?

---

> **Ogbaudu**（1 分） · 2026-06-02T03:40:40+08:00　
> I’m just hearing about it for the first time. I’ll take a look at it. Thanks

---

> **HarjjotSinghh**（1 分） · 2026-06-02T07:09:01+08:00　
> This is painfully accurate. We shipped custom domains and every bullet here drew blood. A few hard-won additions for anyone attempting it:
>
> - Use on-demand TLS (Caddy does this beautifully) instead of pre-issuing, but gate it with an allowlist check on the SNI hostname or you've built an open cert-minting endpoint that'll get you rate-limited into oblivion by bots probing your IP.
> - The verification UX is the real product, not the certs. Users fat-finger DNS constantly. Show live "we see your CNAME / we don't yet" polling, not a "click to verify" button that just fails silently.
> - Apex domains are a trap (no CNAME at root). You'll end up telling users to use a CNAME flattening / ALIAS record or a www redirect.
> - Cache the negative results. Hammering DNS on every page load gets you throttled.
>
> Honestly the whole thing is a great example of why "it works" and "it's a feature you can hand to non-technical customers" are months apart. That gap is basically why I work on Moonshift (moonshift.io), it takes the idea and handles the build + deploy + the boring infra like this. Great writeup, saved it.

---

> **MrPffwawa**（1 分） · 2026-06-02T11:34:17+08:00　
> this hits hard lol. i built a whatsapp chatbot for local businesses and told the client "2 weeks to go live." took me a month because of shit i never planned for — session persistence, QR code expiry, device fingerprinting. the actual chatbot logic was done in 3 days. everything else was infrastructure nobody talks about. lesson learned: the product is never the hard part, the plumbing is

---

> **ResidentHovercraft91**（2 分） · 2026-06-02T13:16:56+08:00　
> did it a bit faster in appdonia.com
> yes, all things mentioned needs to be adressed, but with AI, ai think did it in few hours

---

> **Jonathan_Geiger**（1 分） · 2026-06-02T13:50:04+08:00　
> Nice man
> I wanted to support multiple product of ours with a lot of users
>
> So built it as an infra for adding custom domains feature for every SaaS and product we’ll have on the future, and made it available for others

---

> **imagiself**（1 分） · 2026-06-02T14:12:10+08:00　
> Appdonia fits the indie SaaS format at [https://peerpush.net](https://peerpush.net), which is structured so AI assistants and human builders can discover and retrieve technical products like yours.

---

> **crashburn65**（1 分） · 2026-06-02T15:19:33+08:00　
> NXDOMAIN negative caching is such a painful thing. Was bitten by it many times.
>
> When allowing your customers to CNAME to your service, please make sure that the CNAME target is already active and propagated before letting your user see it to update it. Else its going to be a painful wait where you cannot do anything but just run the clock down.

---

> **SnooWords4529**（1 分） · 2026-06-02T19:15:39+08:00　
> the dns validation ux piece is where this blew up for us too tbh. we underestimated how many customers would set A records instead of CNAME or point to the wrong target entirely, then open a ticket saying "its broken" with zero context. ended up building a pre-check flow that tests the DNS config before attempting cert issuance which saved us from burning rate limits on misconfigured domains. fwiw the observability layer you mentioned is non-negotiable, silent cert expiry killed us once and that was enough.

---

> **ExamInstinct**（1 分） · 2026-06-02T22:51:10+08:00　
> The "two weeks" → two months arc is painfully accurate for almost any infra feature that touches certs and DNS. The DNS drift point is the kind of thing you only learn by getting burned. Saving this!

---

> **Hadevs12**（1 分） · 2026-06-03T09:13:20+08:00　
> This is one of those features where the UI looks tiny but the operational surface area is huge. The part I would add is customer education: most support tickets are not really about TLS, they are about users not knowing what their DNS provider is doing. A good setup wizard should show exactly what record is expected, what value is currently resolving, and what state it is in. That alone turns a scary support thread into a self-serve flow. Also worth having a boring fallback: if custom domain is broken, keep the default app subdomain alive so the customer is never fully down.

---

> **MediumCustomer3882**（1 分） · 2026-06-03T15:10:32+08:00　
> Mine was the database decision. "We'll start with Postgres, figure out the rest later" sounds right on day one. three months in, everything that wanted to be a document, a file, or a cache is a table with workarounds - and the migration is too expensive to actually run. The decisions that feel like configuration are actually architecture.

---

> **LeaderAtLeading**（1 分） · 2026-06-03T22:20:24+08:00　
> Custom domains are always two months, never two weeks. DNS, SSL, and cert renewal get everyone.

---

> **Hadevs12**（1 分） · 2026-06-04T13:15:29+08:00　
> this is one of those features where the ui looks tiny but the trust surface is huge.
>
> users hear "custom domain" and think branding. founders implement it and discover dns edge cases, ssl weirdness, propagation delays, support burden, and all the ways a simple setup can feel broken.
>
> it's a good reminder that some features are not product work, they are ongoing reliability work.

---

> **Aggressive-Food-249**（1 分） · 2026-06-07T12:54:41+08:00　
> cool

---

> **PrestigiousGas1490**（1 分） · 2026-06-07T14:13:06+08:00　
> The cert renewal piece is what gets people the most. It feels fine until 90 days later when everything quietly breaks and no one knows why. Good write-up, the DNS drift one especially is something most people won't see coming.

---

> **pavelperminov**（1 分） · 2026-06-09T02:15:44+08:00　
> \> 2–3x longer than my first estimate
> that is almost always true, and will be that way.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
