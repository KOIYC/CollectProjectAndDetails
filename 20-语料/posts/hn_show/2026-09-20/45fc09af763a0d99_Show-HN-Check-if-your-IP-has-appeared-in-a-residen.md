---
type: "corpus"
item_id: "45fc09af763a0d99"
title: "Show HN: Check if your IP has appeared in a residential proxy network"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49713037"
project_url: "https://haveibeenproxied.com/"
author: "microcode"
published_at: "2026-09-15T14:24:47Z"
captured_at: "2026-09-20T09:38:32+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_microcode
  - story_49713037
  - show_hn
metrics: {"points": 75, "comments": 48, "engagement_velocity": 75}
comments_count: 48
comments_total: 48
discovered_via: "hn:show_hn:90d"
---

# Show HN: Check if your IP has appeared in a residential proxy network

> [!info] 一句话导读
> Have I Been Proxied? - Check your IP reputation

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49713037>
> 指标：点赞=75 · 评论=48 · engagement_velocity=75
> 作者：microcode　|　发布：2026-09-15T14:24:47Z
> 项目链接：<https://haveibeenproxied.com/>
> 采集：2026-09-20T09:38:32+08:00　|　id：`45fc09af763a0d99`

## 正文

Have I Been Proxied? - Check your IP reputation

# Have I been proxied?

Find out in one click.

Check whether your public IP has been observed in a residential proxy network, and understand what to do next.

We check the public IP address your browser is connecting from. Nothing is installed, and we do not scan your devices.

## Your connection. Someone else's traffic.

Residential proxy networks route internet traffic through IP addresses tied to real household connections. Apps, browser extensions, VPNs, smart TVs, or other connected devices can make your home network part of a proxy network without your knowledge.

We check for signs that a proxy service has used your internet connection to send other people's traffic. If we find any, we'll explain what we found and suggest which apps and devices to check.

1. 01

### Check your public IP

Start with the public IP your browser is using.
2. 02

### See what we have observed

See whether your IP has been observed in a residential proxy network.
3. 03

### Know what to investigate next

If activity is found, get guidance on where to look and what to do next.

## The intelligence behind the check.

Have I Been Proxied is powered by Spur Intelligence, which helps security and fraud teams identify residential proxies, VPNs, anonymization infrastructure, and other hidden network activity across enterprise websites and applications.

# daniel-sc/contextveil

## 评论（48/48）

> **toomuchtodo** · 2026-09-15T14:44:20.000Z　
> Needs an API to query other IPs beyond one's own.

---

> **varispeed** · 2026-09-15T16:34:17.000Z　
> I am on mobile network and it fails to consider this as a factor that other people who might receive this IP could be having a proxy.

---

> **stogot** · 2026-09-15T16:51:13.000Z　
> It says I was observed on a couple areas, but not sure what to do with that information. It would be great if thi tool provided links to guides to discover more.

---

> **rckoepke** · 2026-09-15T17:10:45.000Z　
> In my testing, Synthient's tool[0] and offerings have performed very well for this kind of service. Synthient have also achieved impressive proven success against malicious botnets[1].0: https://synthient.com/context/ip/1: https://www.wsj.com/tech/kimwolf-hack-residential-proxy-netw... / https://archive.ph/SpKVn

---

> **xyst** · 2026-09-15T17:12:36.000Z　
> Seems it only detects ipv4. Any plan to support scanning ipv6 /56 range?

---

> **ranger_danger** · 2026-09-15T17:37:11.000Z　
> Keep in mind these databases can be wildly inaccurate and basically impossible to prove them wrong (you can't prove a negative).I've seen this (and verified with others) with other sites like iknowwhatyoudownload.com where they allege your connection downloaded something very illegal (like CSAM) even though you know for certain it never happened and you haven't been hacked.

---

> **TZubiri** · 2026-09-15T18:09:54.000Z　
> very nice.Can we use it in other IPs? (without having to issue the request from that IP)

---

> **jasonvorhe** · 2026-09-15T18:30:39.000Z　
> This would probably false positive every CGNAT IP, or am I misunderstanding something?

---

> **koutakun** · 2026-09-15T20:56:24.000Z　
> Would be great if it told me how recently it was detected. I have a dynamic IP from my ISP and it could very well be someone else's device 3 days or 3 months ago.

---

> **hollow-moe** · 2026-09-15T21:49:21.000Z　
> My public IP is shared with some 150 people in a student dorm, and the result is negative which I find very unlikely.

---

> **babooka** · 2026-09-15T22:16:35.000Z　
> this company Spur recently got millions in funding and their pricing seems to be directed at large companies. Who's buying these absolutely non-actionable IP databases? Do corporate buyers not understand you can't just block someone because they share the IP with someone else who downloaded a dodgy app?

---

> **hansufati** · 2026-09-15T22:37:23.000Z　
> wow my comment with a blog post about a better approach to detect residential proxies got... removed! Not sure about HN internals, do moderators do that or is this OP using several accounts to downvote contrarian comments?

---

> **negura** · 2026-09-16T05:09:45.000Z　
> How exactly do they obtain this data? Residential proxy providers don't publish their IP list (you connect to one of their servers which then tunnels your traffic to the residential exit point). Plus there are tons of such providers.In any case, residential proxies are a godsend. Because most of the everyday services like web shops, govt information portals, even personal blogs sometimes are blocking access usings captchas.EDIT: they write this on their marketing copy [0]:> The Spur platform identifies traffic originating from residential proxy networks by analyzing service fingerprints, ASN ownership, and behavioral indicators.Sounds like guesswork that results in a ton of false positives. And the more innocent IPs are blocked by platforms on the basis of this data, the more the demand increases for residential proxies, from users who need access to essential services. Talk of creating the problem and then selling the "solution".[0] https://spur.us/platform/residential-proxy-detection

---

> **reincoder** · 2026-09-16T08:45:18.000Z　
> I work for IPinfo. We offer a residential proxy detection service, which you can check at ipinfo.io/my.We had a previous discussion about surfacing visitor IP address resproxy status explicitly. Should we have some sort of badge or a more explicit alert to show if a site visitor's IP address is part of a residential proxy network?Even though it is great for demonstrating the product's value, it is kind of a low-tier value. What can a user actually do when they realize their IP address is part of a residential proxy pool?The first issue is that residential proxy SDK infiltration is massive. If you start connecting to different IP addresses and constantly check your IP address on our website, you will often see that many of those IP addresses were, at some point, part of a residential proxy pool. We provide frequency information showing how many times an IP address was observed in a residential proxy pool, with a default observation period of 7 days.Then there is the question of what a user can actually do about it. If it is a controlled IT environment with paranoid IT admins, sure, they can actively monitor traffic and identify why their IPs are showing up in residential proxy pools. They can attempt to do something about it. But it is not easy even then.Residential proxy SDKs can simply be baked into almost any smartphone or smartphone-derived OS that allows app installation through marketplaces. So, many residential networks are already cooked (because of android TVs). Moderate-scale NAT connections almost always see residential proxy flags, as do public Wi-Fi hotspot IPs, which we also detect.Identifying the apps that are generating background network traffic is quite hard. You need some level of DNS monitoring or a network sniffer. Alternatively, you need router-level firewall software.These SDKs are not always sending high-volume, constant traffic that makes them easy to detect. If you see a 100% residential proxy flag for your IP address, then they probably are. But in many cases, the traffic is intermittent and much harder to identify.Nobody has an answer to what I should do when I see my IP address in a residential proxy pool. It has been accepted in spirit as a "consented malware" for the last few years. It is undetectable and extremely hard to remove because the SDK has been baked into apps themselves.

---

> **imalexandru** · 2026-09-16T10:50:50.000Z　
> what if i have an always rotating ip?

---

> **idoescompooters** · 2026-09-19T01:03:21.000Z　
> Spur.us is how you can show that these "Residential VPN IPs" are easily identifiable. All of StarVPN's residential IPs are traced back to them easily.

---

> **microcode** · 2026-09-15T14:45:45.000Z　
> Try https://spur.us/context/ where  is the IP you want to query :)

---

> **Aurornis** · 2026-09-15T16:46:24.000Z　
> If the IP address you're using has been detected as a residential proxy, it doesn't matter. It's going to be flagged on lists for a long time.Being able to check is helpful.

---

> **specproc** · 2026-09-15T18:09:01.000Z　
> Yeah, clicked from my mobile network without thinking and nearly jumped out my skin.

---

> **TZubiri** · 2026-09-15T18:11:54.000Z　
> But whether your IP address is being used as a residential proxy is already important information. It answers the question (is this IP address low quality?)Although I'll grant that it would be interesting to know if your devices are running the proxy, but you'll need an exeuctable tool for that, not a per-ip network tool.

---

> **microcode** · 2026-09-15T16:54:50.000Z　
> Which proxy network(s) did you get tagged in?

---

> **mahboi** · 2026-09-15T19:03:21.000Z　
> Do they show proof of the positive if you show up in there?

---

> **microcode** · 2026-09-15T18:11:14.000Z　
> Yes. You can use https://spur.us/context/ where the IP is the one you want to lookup.

---

> **gonzalohm** · 2026-09-15T18:59:35.000Z　
> I think CGNAT is a type of residential proxy.Hidden from the user and provided by the ISP

---

> **poppafuze** · 2026-09-15T19:30:58.000Z　
> Yes, it did and it does.

---

> **numpad0** · 2026-09-16T02:23:35.000Z　
> I think "residential proxy" in this context is "AI scraping bot/pay Netflix at Indian price VPN exit node", not just an IP with NAT on outside.If there were people under the same CGNAT with someone running one of those exit nodes, then that's not a false positive.

---

> **microcode** · 2026-09-15T23:26:12.000Z　
> The TTL for our data is 2-3 days so you can be fairly confident that it is up to date.

---

> **horsawlarway** · 2026-09-16T00:44:32.000Z　
> Depends quite a bit on your university.Some are quite good at limiting connections, monitoring devices, and contacting students for suspicious traffic.

---

> **microcode** · 2026-09-15T22:56:00.000Z　
> Spur's residential proxy data is not intended to be used as a blacklist. We recommend using it as enrichment alongside other signals, not blocking an IP just because it was associated with proxy activity.More on why here: https://spur.us/blog/i-dont-like-big-gateways-and-i-cannot-l...

---

> **Avamander** · 2026-09-16T00:50:45.000Z　
> I know that SpamHaus is using this dataset as a large (at times sole) contributor to their blocklists. So corporate buyers are doing exactly what you describe, albeit indirectly.Lack of any IoCs also makes it hard to refute or remedy. Plus I think it paints even Tor relay nodes with the same brush as malicious proxies.Truly kafkaesque if you start getting restricted and nobody tells you why or even knows what to tell you because the sources have all been mixed and obscured.

---

> **Symbiote** · 2026-09-16T06:16:45.000Z　
> I think it was down voted as it looks like self promotion

---

> **Avamander** · 2026-09-16T10:39:50.000Z　
> I don't think they have false positives to the extent you're saying. It's not as much guesswork as you think.

---

> **juros** · 2026-09-16T10:32:51.000Z　
> there was a blog post linked on this thread explaining how proxy IP lists (spur, synthient, ipinfo et al) have little actionable value and introducing an alternative real-time approach to detection.But it got flagged/downvoted into removal (twice!). Someone here has lots of HN accounts and doesn't tolerate free competition.Disclaimer: I'm the founder and main researcher of the "flagged" company.

---

> **toomuchtodo** · 2026-09-15T14:48:12.000Z　
> Thanks! Do you plan on a paid plan? Would you be able to provide methodology under NDA if needed?(cyber consultant, have people who might use this for enrichment in security stacks)

---

> **TacticalCoder** · 2026-09-15T17:04:57.000Z　
> > If the IP address you're using has been detected as a residential proxy, it doesn't matter. It's going to be flagged on lists for a long time.Flagged and then... What exactly?If people who have a smart TV have their smart TV participate in a residential proxy, then it's billions of IP getting "flagged".What's the use of flagging those?When every IP is flagged, none is.

---

> **microcode** · 2026-09-15T18:14:22.000Z　
> I added a warning that should help with this now.

---

> **regenschutz** · 2026-09-15T20:32:51.000Z　
> There really isn't any proof that they can show, since iknowwhatyoudownload legally aren't allowed to download anything that you're seeding (since that would be considered piracy).IIRC, they only show the filename, last-seen timestamp and user agent. I can't verify it though since their website seems to be down?

---

> **mahboi** · 2026-09-15T19:02:45.000Z　
> CGNAT isn't a residential proxy

---

> **koutakun** · 2026-09-15T23:34:54.000Z　
> That's cool, but I get a new IP every 12 hours so it's still not enough to determine if I'm part of a botnet or I just got stuck with someone else's poisoned IP

---

> **babooka** · 2026-09-15T23:15:39.000Z　
> thanks, that was exactly my point. Residential proxy signal's value is almost 0 but this product moves in the "I solve it all for you" price range.

---

> **Avamander** · 2026-09-16T00:47:42.000Z　
> SpamHaus is using it as a large contributor to their blocklists, at times as the sole signal, just so you know.

---

> **juros** · 2026-09-16T10:38:33.000Z　
> all links currently on this thread are self promotion, OP included. They just own more HN accounts to vote unwanted comments away ¯\_(ツ)_/¯

---

> **reincoder** · 2026-09-16T11:29:03.000Z　
> I have been part of this community for over a decade, and in my experience the mods do take flagging and voting irregularities seriously when they are reported. If you believe there is manipulation happening on your posts, that is worth raising directly with them, since they have visibility we do not.---On the broader point, we process 3 trillion requests last year, have more than 80 employees, and run a dedicated privacy engineering team led by an ex-cybersecurity company founder. We invest in research on new detection methods and stay closely engaged with the developer community. If there are specific gaps you see in our product, I would be glad to hear them and discuss.---Whether any dataset, including residential proxy IP data, is valuable depends heavily on the application. Treating a dataset as invalid because it does not fit one particular model can lead to decisions on shaky ground.We are regarded as one of the more if not the most accurate IP geolocation providers, and we spend considerable effort on education, solutions architecture, and documentation so customers understand what our data can and cannot support. For example, IP geolocation, even at highest level of accuracy, is not a person identifier. It will never be a 1:1 replacement of GPS geolocation.Many of the largest companies in AI, anti-bot, fingerprinting, KYC, and CDN spaces use our data. If anti-bot systems and CAPTCHAs were fully reliable on their own, there would be less need for additional signals like residential proxy data. We do not assign a score or label an IP as good or bad. That judgment sits with the customer's own threat or analytics model.Residential proxy IPs are, by and large, mostly used in web scraping operations of many different forms. If a company sees a moderate to high amount of traffic mimicking human behavior, it can struggle to tell bot traffic apart from real users. Anti-bot mechanisms can help, but they add friction to the user experience, and they are not cheap to run at scale.Residential proxy detection data is one of the easiest zero-knowledge ways to gather intelligence. There is no need for users to solve a puzzle or for multi-page traversal to collect fingerprint data. All that is needed is the IP address.Our residential proxy data customers tend to be on the more sophisticated side of cybersecurity. Suggesting that this data is a silver bullet for all their security needs would not reflect well on their expertise or ours. We present the data as is, and from there we work with customers on the right solution for their case.

---

> **TZubiri** · 2026-09-15T18:15:08.000Z　
> +1Some info on methodology would be necessary for a paid plan for two purposes, one to audit that the quality of the methodology and the signal is good (it's not hallucinated or checking few sources).But also to make sure it doesn't clash with other signals if used in conjunction with other sources of tool (if I have another signal, I want to know whether they are redundant or complementary, to avoid interpreting two positives as independently verified.

---

> **ranger_danger** · 2026-09-15T17:38:08.000Z　
> I assume that eventually the flag will just become meaningless and there will be other methods of verification in use by then... because cutting off a huge chunk of your customers just isn't good business.But for now I'm already cut off from half the internet due to endless crimeflare captcha loops... I just don't visit those sites anymore because I literally can't.

---

> **TZubiri** · 2026-09-15T18:28:31.000Z　
> >If people who have a smart TV have their smart TV participate in a residential proxy, then it's billions of IP getting "flagged".There's a non-trivial quantity error here that makes the argument of a majority qualitatively incorrect.It's not billions of IPs that are being used in residential proxies, it's not all smart TVs.There needs to be a vulnerability and hacked devices OR there needs to be a very low quality and shady vendor that is offering products at too cheap prices and needs to make ends meet in order to compete at that price. Probably chinese.This would be in the range of 1 to 100 million smart TVs. sorry for the wide range, but definitely not 1Billion or every TV.So to the extent that the ratio of infected to non infected IPs is low, then providers can block the infected ones to a great effect.

---

> **mahboi** · 2026-09-15T19:04:25.000Z　
> Mine isn't flagged. Not gonna set up a smart TV.

---

> **Symbiote** · 2026-09-15T18:57:07.000Z　
> Bright Data claim to have 400 million IPs.https://brightdata.com/proxy-types/residential-proxies

## 导航

- 项目页：[[10-项目/haveibeenproxied.com_23001e3f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
