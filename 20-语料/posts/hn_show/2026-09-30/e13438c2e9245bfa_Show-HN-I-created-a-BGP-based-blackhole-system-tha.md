---
type: "corpus"
item_id: "e13438c2e9245bfa"
title: "Show HN: I created a BGP-based blackhole system that you can set up in minutes"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49902803"
project_url: "https://setecastronomyinc.com/shield"
author: "jkalbfeld"
published_at: "2026-09-30T00:28:29Z"
captured_at: "2026-09-30T18:57:07+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-30"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_jkalbfeld
  - story_49902803
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: I created a BGP-based blackhole system that you can set up in minutes

> [!info] 一句话导读
> Setec Astronomy , Inc.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49902803>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：jkalbfeld　|　发布：2026-09-30T00:28:29Z
> 项目链接：<https://setecastronomyinc.com/shield>
> 采集：2026-09-30T18:57:07+08:00　|　id：`e13438c2e9245bfa`

## 正文

Setec Astronomy , Inc.
Home
Products
Services & Pricing
Live Threat Map
Resources
API Docs
fail2ban Setup Guide
Blog
Daily Briefing
About
Contact
Log In
Sign Up
Portal
BGP Blackholing · RTBH
 Stop connection-based attacks before they hit your network.
Large ISPs and enterprise networks block attacks the same way: dropping malicious
 traffic upstream, before it ever reaches you, not after. Normally that takes a
 transit contract and a network engineering team. Shield brings that same real-time
 threat intelligence to a single router for $59/month.
$59 /mo
14-day free trial • No card required • Live in minutes, no waiting on a human
Start Free Trial
 Continue with PeeringDB
 How It Works
No card required to start — your session reverts automatically after 14 days unless you add a plan.
No, you don't need to be multihomed. One router with a private ASN and a tunnel to a SATIS PoP is enough — multihoming only matters for announcing routes to the wider internet, not for receiving and acting on our blackhole feed.
We operate our own BGP network (AS23026), built for exactly this — collecting and blackholing threats — not a SaaS reselling someone else's feed. Same infrastructure that already runs our own network.
You don't need to already be BGP peering with anyone. Any router that's configurable and speaks BGP is eligible — pfSense, OpenWrt, VyOS, BIRD/FRR on Linux, or enterprise gear. We issue you a free private ASN and you peer directly with us over the tunnel; there's no existing relationship with an upstream ISP or transit provider required.
Real-time, shared threat intelligence — not just your own blocklist. Attacks other peers on the network have already seen get blocked for you too, live.
Shield (Lifetime) — $9,995 once, never billed again
Full Shield tier, paid one time. Limited to the first 15 organizations —
Claim Lifetime Deal
Real-Time, Shared Threat Intelligence
Not just your own blocklist — a live feed of attacks other peers on the network have already seen, delivered automatically as BGP routes your router blocks in real time. Also available via API (2,000 req/day) if you want to pull it yourself.
GRE or WireGuard Tunnel + Your Own BGP Session
GRE or WireGuard tunnel to a SATIS BGP PoP (Los Angeles, Dallas, or Buffalo), one session, one severity threshold you control.
Private ASN, No Multihoming
A free private ASN (64512–65534) and a router that speaks BGP is enough. No transit diversity, no LOA paperwork.
Auto-Approved
No admin review queue. Request a session, get your config, be live — typically minutes, not days.
How It Works
From signup to live blackholing in one sitting
1
Start Your Free Trial
Sign up — no card required. Your account starts free; the live BGP session comes from step 2.
2
Request Your BGP Session
From the portal, request peering — live immediately, no waiting on a human to review it and no card on file.
3
Download Your Config
A GRE or WireGuard tunnel config plus a copy-paste BGP peer block, generated for your router's OS — Cisco IOS/IOS-XE, Juniper JunOS, OpenWrt, pfSense/OPNsense, VyOS, OpenBSD, or Linux+BIRD/FRR.
4
Traffic Gets Dropped Upstream
Once peered, malicious IPs above your chosen severity threshold get blackholed — dropped before they reach your network, not after.
What You Actually Need
A router that speaks BGP — BGP is the protocol networks use to tell each other how to route traffic, and it's what lets Shield block attacks upstream instead of at your firewall. Config generated for Cisco IOS/IOS-XE, Juniper JunOS, OpenWrt, pfSense/OPNsense, VyOS, OpenBSD, or Linux running BIRD or FRR. Homelab or enterprise, if it does standard BGP, we'll get you a config.
A private ASN (64512–65534) — think of it as an ID number for your network. Free, no RIR paperwork, generate one yourself in seconds.
That's it — one router, one ASN, and you're peering
You don't need an existing BGP feed, either.
 SATIS can be your first BGP session, not an add-on to one you already have. If all you're running today is static routes, that's fine — the requirement is that your platform can run a BGP daemon, not that you're already using it for anything.
Questions
What is RTBH / BGP blackholing, actually?
Remote-Triggered Black Hole routing: your router announces a more-specific route for a malicious source IP with a special community tag, telling upstream routers to silently drop traffic to/from it — before it ever reaches your network. It's the same technique large ISPs use as part of their mitigation stack, applied to a single-router network. On its own it's very effective against connection-completing attacks — brute force, exploit attempts, C2 callbacks. It doesn't stop a volumetric flood (a UDP or SYN flood, reflection/amplification) unless you also enable uRPF / reverse-path filtering on your own router, which we document but don't configure for you.
Do I need to be multihomed to peer with SATIS?
No. A single router with a private ASN and a GRE or WireGuard tunnel to a SATIS BGP PoP is enough. Multihoming and public ASNs matter for announcing your own routes to the wider internet — they're not required just to receive and act on our blackhole feed.
I'm on a residential or small-business ISP connection (Spectrum, Comcast, etc.) with their router — can I still use this?
Yes, as long as you put your own BGP-capable router behind it. Most residential/business ISP gateways support bridge mode, which hands your public IP straight through to your own router — the cleanest setup. Without bridge mode, your own router still works behind the ISP's box (double-NAT'd); the tunnel to SATIS is outbound-initiated, and consumer/business ISPs don't typically block that. Either way, works equally well for a homelab, a small business office, or a home network — the requirement is the router you put behind your connection, not who your ISP is.
What happens after the 14-day trial?
Nothing charges automatically — there's no card on file. If you haven't added a plan, your BGP session is revoked and your account reverts to Community; you'll get a countdown email as the trial winds down so it's never a surprise. Add Shield anytime from the portal, self-service, to keep it running — no phone call or support ticket needed.
How is this different from Professional or Enterprise?
Shield is purpose-built for RTBH: one BGP session, one GRE/WireGuard tunnel, focused entirely on blackholing. Need real-time SSE streaming or more sessions? Professional and Enterprise build on the same peering, with a 14-day trial on Professional. Upgrading from the portal takes one click whenever you're ready.
Stop the Next Attack Upstream
Auto-approved BGP blackholing, live in minutes.
Start Free Trial
 Continue with PeeringDB
14 days free, no card • $59/mo only if you add a plan • Cancel anytime, self-service
No card required to start — your session reverts automatically after 14 days unless you add a plan.
Setec Astronomy, Inc.
Blockchain-based real-time threat intelligence.
AS23026 • IPv6 Native
"Too Many Secrets"
Product
Services
API Docs
Email Security
Dashboard
Company
About
Blog
Contact
Investors
Partner Program
Connect
Contact
Portal
© 2026 Setec Astronomy, Inc. All rights reserved.
setecastronomyinc.com

## 导航

- 项目页：[[10-项目/setecastronomyinc.com_59900ac5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
