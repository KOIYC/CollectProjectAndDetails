---
type: "corpus"
item_id: "26fcdd58fb4a47f0"
title: "Jellyfin Remote Access with Whitelisted Dynamic IPs"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1wjvub1/jellyfin_remote_access_with_whitelisted_dynamic/"
author: "BroadStBully35"
published_at: "2026-09-19T01:00:47+08:00"
captured_at: "2026-09-29T09:43:45+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-29"
pub_day: "2026-09-19"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 10, "comments": 29, "upvote_ratio": 0.73}
comments_count: 29
comments_total: 29
discovered_via: "reddit:14d+settle10"
---

# Jellyfin Remote Access with Whitelisted Dynamic IPs

> [!info] 一句话导读
> I've been scouring the internet for a way to implement this, but I haven't been able to find it. Most of the recommendations simply say to use tailscale/VPS/etc…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1wjvub1/jellyfin_remote_access_with_whitelisted_dynamic/>
> 指标：得分=10 · 评论=29 · 赞踩比=0.73
> 作者：BroadStBully35　|　发布：2026-09-19T01:00:47+08:00
> 项目链接：—
> 采集：2026-09-29T09:43:45+08:00　|　id：`26fcdd58fb4a47f0`

## 正文

I've been scouring the internet for a way to implement this, but I haven't been able to find it. Most of the recommendations simply say to use tailscale/VPS/etc, but I'm not interested in anything that prevents Jellyfin from being accessed remotely from a smart TV / streaming stick. Networking has never been a particular strength of mine, so I've been doing a lot of learning lately, but I have an idea of what I'm trying to accomplish that doesn't seem like it should be as difficult as I'm finding it to be (famous last words, I know).

Since Jellyfin doesn't natively support MFA, and the plugins that could enable it won't be able to run natively everywhere, my "brilliant" plan is to have to following setup:

1. Head to my domain remotely from a smartphone/laptop, log in with MFA
2. Whitelist the IP the request came from for a set time period
3. Allow normal login to Jellyfin on the smart TV

I'm sure there are a ton of flaws in my plan that I can't see, or maybe it just isn't possible to implement. But it feels like that's a pretty good way to protect my server, no? I don't want to use Cloudflare Tunnels and violate their ToS, and I don't want anyone to be able to access Jellyfin without first authenticating with the server. I'm open to any ideas that could accomplish this!

(Running TrueNas Community / everything in dockge)

## 评论（29/29）

> **asimovs-auditor**（1 分） · 2026-09-19T01:00:59+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **BroadStBully35**（1 分） · 2026-09-19T01:01:59+08:00　
> No generative AI has been used in the creation of my post/project, everything has been done by me or by scouring forums myself.

---

> **1WeekNotice**（11 分） · 2026-09-19T01:12:15+08:00　
> Note this comment is dismissive. I'm not trying to be rude/ mean. Just being blunt.
>
> >Most of the recommendations simply say to use tailscale/VPS/etc, but I'm not interested in anything that prevents Jellyfin from being accessed remotely from a smart TV / streaming stick.
>
> Don't compromise security because of smart TVs. Streaming stick support Tailscale/ Tailscale have apps for streaming sticks.
>
> Also smart TV are horrible. Have to seen the latest smart TV News
>
> Note: streaming sticks aren't better as they also have ACR but they are a bit better then smart TVs. Plenty of post of alternative living room watching mentions but they aren't as non technical friendly
>
> - [LG TV listening/ recording everything you say and watching your screen all the time](https://youtu.be/6IFVTcM28KA?si=y-KxGSJ4CbnZamIj)
> - [it's not just LG TVs](https://youtu.be/IvFu343KNek?si=dnh8RYKXUhaD2L8z)
>
> > my "brilliant" plan is to have to following setup:
>
> You came up with a complicated solution because you / your clients are smart TVs. It's not worth it
>
> Hope that helps

---

> **Lau-ie**（1 分） · 2026-09-19T01:30:24+08:00　
> Best security setup I've found short of wg is traefik with country level bans + crowdsec with log watcher. Also setup your jellyfin so remote logins can't access setting and sensible ip van settings.Make sure a compromised jellyfin is isolated in a sandbox.
>
> Still, not advisable. Use tailscale or wireguard.

---

> **czocherek**（0 分） · 2026-09-19T01:31:13+08:00　
> Try https://github.com/FarisZR/knocker

---

> **ComprehensiveLuck125**（1 分） · 2026-09-19T01:33:35+08:00　
> It is **temporary IP allowlisting after MFA authentication** or **Just-In-Time network access**.
>
> Possible with pfSense+ / HAProxy / Authentik.
> So you would have a firewall rule with empty Alias and then, upon Authentik auth you add ip address to Alias. However there is nothing to clean (expire) ip address after say 24 hours. So you need something partially custom still (or you can have a cron that purges alias daily at 3:00 AM which will give you max 24h).
>
> Ps. Pfsense+ has REST APIs, but maybe you will workaround with regular pfsense.

---

> **Only-Stable3973**（0 分） · 2026-09-19T01:36:16+08:00　
> Just spin up a reverse proxy and problem solved.

---

> **BroadStBully35**（6 分） · 2026-09-19T01:40:06+08:00　
> Fair, I appreciate the response, just wanted to clarify that I had already read through many pages of people suggesting those solutions and wanted to see what other options there were.
>
> I am aware of (at least some of) the various downsides to smart tvs / streaming sticks, but considering that's where I want to stream to, I want to at least explore what it would take for it to be possible. When the problem is "how can I get this to work on a smart tv" and the answers I could find were "just use a streaming stick/mini pc that supports tailscale", I wanted to get what an actual answer would look like before giving up. Even if the solution is complicated, if it's complicated to set up and not-so-complicated to use, that's fine by me.

---

> **1WeekNotice**（2 分） · 2026-09-19T02:02:48+08:00　
> >Fair, I wasn't trying to be dismissive, just wanted to clarify that I had already read through many pages of people suggesting those solutions and wanted to see what other options there were.
>
> To clarify. I was stating that my comment was going to be dismissive of your solution/ post. Where I'm not trying to be mean. Just being blunt. Your post is fine 🙂
>
> >When the problem is "how can I get this to work on a smart tv" and the answers I could find were "just use a streaming stick/mini pc that supports tailscale"
>
> Totally get that and I think this has a bigger meaning to it. A lot of people state to use streaming sticks/ mini PC that use Tailscale because they don't want to compromise there security and they want an easy to manage solution.
>
> Time is money and people rather use something that works and is known to be secure VS trying to re invent the wheel.
>
> But with that being said, if you want to try a different solution then by all means. You can maybe use authentic as the middle for MFA. There maybe solutions for smart TVs providing a code then you need to authenticate?
>
> Sorry if this comment is not helpful. I actually don't know the best security method for your situation.
>
> Hopefully others can help

---

> **Snek--**（8 分） · 2026-09-19T02:14:26+08:00　
> Its absolutely fine running jellyfin behind a reverse proxy if you know what you are doing.
>
> Also, if your goal is maximum compatibility with Dolby Vision/HDR, DTS and Dolby Atmos a streaming stick or box, especially fire TV, is almost your only option.

---

> **moltenice09**（4 分） · 2026-09-19T02:23:30+08:00　
> In addition to what others have said, using a reverse proxy like Caddy, use an obscure domain name that can't be guessed, have it get a wildcard let's encrypt certificate, and run it on an obscure port number. Security through obscurity is not the best idea, but it does help when added on top of other forms of security.

---

> **1WeekNotice**（8 分） · 2026-09-19T02:26:28+08:00　
> >Its absolutely fine running jellyfin behind a reverse proxy if you know what you are doing.
>
> We need to be specific here if OP is new to the topic.
>
> Reverse proxy alone doesn't add much security. All it does is provide a single entry point for multiple services.
>
> But having that signal point of entry enabled other security measures such as
>
> - TLS
> - MFA (what OP wants)
> - geo blocking/ whitelist (what OP wants)
> - fail2ban/ CrowdSec to block malicious IPs
> - etc
>
> So OP did mention some of these topics. They just didn't mention using a reverse proxy as their entry point. And it seems they want to lock this down as much as they can. That why they mention MFA and whitelist a single IP
>
> Basically wireguard would be the best option for them but Tailscale doesn't support smart TVs/ I don't know if smart TV even want Tailscale on their app store.
>
> So to your point, a reverse proxy with added components will be fine. They want MFA and maybe authentic can handle that

---

> **Ill_Leader_7104**（2 分） · 2026-09-19T02:31:16+08:00　
> have you considered that multiple people behind the same carrier NAT will share an IP? so whitelisting one person's IP might accidentally let in others on the same network. not a huge risk but worth knowing about, especially with mobile carriers

---

> **certuna**（4 分） · 2026-09-19T02:32:32+08:00　
> If your remote client connects over IPv6, you’ll have to whitelist the /64, as each phone (and LAN) uses a whole subnet, not individual /128 addresses.
>
> If your remote client is on IPv4, it will almost certainly connect via CG-NAT, so through provider NAT gateways using a pool of different IP addresses, where sessions are dynamically routed over. You’ll likely have to whitelist the whole /24, not an individual /32 address.

---

> **GolemancerVekk**（2 分） · 2026-09-19T03:00:39+08:00　
> [I think this might be what you want.](https://github.com/zuavra/nginx-ip-whitelister) It's literally an IP whitelister that works as a forward auth for Caddy and Nginx.
>
> Other comments have already mentioned why this is probably not a great idea and the link also goes into detail, so I won't. 🙂

---

> **Anusien**（1 分） · 2026-09-19T03:12:50+08:00　
> Just put the streaming sick on a network whose router running tailscale

---

> **Fazl**（5 分） · 2026-09-19T04:38:00+08:00　
> If you are getting a certificate for your domain then that domain is made public via the CA's transparency logs.

---

> **Fazl**（1 分） · 2026-09-19T04:43:29+08:00　
> Another method to solve this with tailscale is to setup it up on your router, if you have one capable, and have tailscale setup routing. Then you would just access the instance directly and your TV would not need to know anything extra.

---

> **BroadStBully35**（1 分） · 2026-09-19T04:51:03+08:00　
> I did consider that for the dynamic IPs at home, I did not consider the public/mobile connection part of it... Thanks for pointing that out.

---

> **BroadStBully35**（2 分） · 2026-09-19T04:59:43+08:00　
> I had seen enough about fail2ban and CrowdSec to know I should use them.  I was planning to use a reverse proxy, but that was more because it seemed like the best way to do this rather than being the way I wanted to. Ideally I could just plug in the domain and authenticate in Jellyfin, but sadly I'm not that naïve lol.
>
> Maybe the reverse proxy and recommended security measures would be good enough, but I'd much rather be safe than sorry, so I wanted to explore what adding MFA would look like. I'm not tied to that as the solution, but my I didn't love the idea of being limited by tailscale's connection limits when a domain is $5 a year and is (theoretically) more convenient for my use case (smart TVs)

---

> **shrimpdiddle**（0 分） · 2026-09-19T05:01:26+08:00　
> Use Nginx Proxy Manager with a subdomain for access. Add access rule. Done.

---

> **Snek--**（3 分） · 2026-09-19T05:31:28+08:00　
> If you dont use a VPN, which is in fact a pain in the ass for other users, a reverse proxy is the only resonable way to go, and is also strongly recommended in the jellyfin docs.
>
> I didnt state a proxy should be your only security measure, i simply dont like telling people, even if they are inexperienced, that VPN or MFA is the only sensible option.
>
> Before you call me irresponsible please take a few seconds to think about the threat model for the average selfhoster.
>
> u/BroadStBully35, to be absolutely clear, I DONT recommend this, i just want to say its not always inherently insecure to expose stuff without security measures that would render a service unusable for some people.
>
> IT Infrastructure is my hobby and job, thats why I am fairly confident running a similiar stack for myself and others. You can absolutely learn enough by yourself in a reasonable timeframe to pull something like this off, but thats only for you to decide.
>
> This is an example i believe to be a reasonable compromise between security and usability IF you understand the implications:
>
> -Jellyfin behind a reverse proxy like nginx, caddy, traefik,... with a valid cert for subdomain
> -Port forwarding via firewall only to proxy
> -NEVER expose any management interface
> -geoblock
> -secure passwords with at least 12-16 characters
> -admin access only from local subnet
> -account lockout after repeated wrong password attempts
> -monitoring/notifications for login attempts, availability, CPU/Disk usage
> -DNS blocklist for known maleware hosts
> -Network segmentation(DMZ for server)
> -basic security principals, including but NOT limited to: security updates asap, key based ssh only - no login for root, minimum needed privileges, backups, logging,...
>
> optional, but recommended:
> -IPS/fail2ban/crowdsec on FW and/or proxy
> -MFA at least for everything only you use
> -non-standard Port, this is not meant as security by obscurity but to reduce background noise from the internet
>
> IT Infrastructure is my hobby and job, thats why I am fairly confident running a similiar stack
>
> If you understand how and why you do this you should be able to assess for yourself if you want to go for it.

---

> **Jeeebs**（2 分） · 2026-09-19T06:51:38+08:00　
> I was theorising a similar solution a few months ago, and came up against this issue. The CGNAT is likely not an issue if someone gets their home broadband whitelisted. You're not massively increasing attack vector as it's likely to only engage with only 5-50 other home connections.
>
> ...but the issue is mobile. The mobile IPs are widely shared, maybe 1000 users. Who knows how they are provisioned? Geographically? Optimised based on required ports?

---

> **Drenlin**（1 分） · 2026-09-19T07:01:18+08:00　
> Could you not just set up a DDNS service on your laptop and have your home server ping it periodically to find the current IP it needs to whitelist?
>
> Could do one per device even.

---

> **Apprehensive-Fig9348**（-1 分） · 2026-09-19T07:11:32+08:00　
> Why do you make it so complicated? Use NGINX and point it to your Jellyfin ip. Problem solved. I use it so my kids can watch anything anywhere. The security issues are blown way out of proportion. You are not Jason Bourne.

---

> **moltenice09**（1 分） · 2026-09-19T08:03:39+08:00　
> Ah, sorry. I meant making the hostname difficult to guess, and using a wildcard certificate so it doesn't show up in that transparency log.

---

> **ThomasWildeTech**（1 分） · 2026-09-19T12:58:09+08:00　
> A lot or replies saying just have a reverse proxy and don't worry about security but you can certainly do a lot more to secure your Jellyfin server.
>
> To answer your question directly with dynamic whitelisting, this is something you can accomplish with a reverse proxy and an auth proxy with a webhook. I published a tutorial of how to do this with pangolin + authentik.
>
> https://youtu.be/1uHPC6309_g
>
> So a user signs into your sso portal on authentik on their phone in their home, user is part of a group which shoots a webhook to pangolin to whitelist their current IP to pangolin. You can feel good seeing your grafana logs of your reverse proxy being totally clean. User's IP changes, they sign back into authentik, and they're whitelisted IP is updated.
>
> If you still want to keep your access logs totally clean without having to do dynamic IP whitelisting, simply do ASN whitelisting. Bots are probing your server from datacenter ASNs, not residential isps. Get your buddy's ASN from ipinfo, whitelist it, and they're good to go.  You should still use a log monitor like crowdsec or fail2ban when you publicly expose a service, and you can easily reduce the blast radius by running it in docker and/or in a VM in Proxmox. If you don't want to expose your IP, get a pay as you go account on Oracle, select a always free ampere instance, install a pangolin tunnel to your server with crowdsec and ASN whitelisting built in. Note also that there's some great ASN blacklists for known datacenters, I built a small ASN auth proxy for traefik that's easy to configure with published datacenter ASNs (https://github.com/Wildium/geo-asn-auth).
>
> Cheers!

---

> **casparne**（1 分） · 2026-09-19T19:25:29+08:00　
> Maybe using Traefik with a plugin like "Traefik IP Whitelist Shaper" (https://plugins.traefik.io/plugins/681de04ce4f1c0f6442c2667/ip-whitelist-shaper) might work?

---

> **True_Researcher_2990**（2 分） · 2026-09-20T10:32:56+08:00　
> My approach is a page behind a cloudflare tunnel that supports social logins for family. Once logged in they click a button to whitelist their device IP. This posts to a node service that then updates my vps firewall rules to allow both ipv4 and ipv6, as well as storing the IPs in a db. I also have a cron job that periodically checks whitelisted IP addresses and removes those older than 24 hours.
>
> That vps tunnels back into my Jellyfin server at home.
>
> There are some drawbacks:
> 1. I'm relying on family to not use it on public WiFi
> 2. Ipv6 only works on the device with Jellyfin so requires a browser on that device to whitelist
> 3. Mobile connections constantly switch IP for me, so I tend to use something like tailscale when out and about. My family will just re whitelist the ip though if it happens to them.
>
> The setup works for me and my family though. Yes it could be more secure and it has a few moving parts but it does what it needs to without exposing my home IP.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
