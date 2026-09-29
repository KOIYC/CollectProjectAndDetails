---
type: "corpus"
item_id: "4e6666dd9a8c0b4e"
title: "Risks of Cloudflared / WARP vs WireGuard for Personal Web Server"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1wjw0i4/risks_of_cloudflared_warp_vs_wireguard_for/"
author: "f00dl3"
published_at: "2026-09-19T01:06:58+08:00"
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
  - Webserver
metrics: {"score": 4, "comments": 16, "upvote_ratio": 0.71}
comments_count: 18
comments_total: 18
discovered_via: "reddit:14d+settle10"
---

# Risks of Cloudflared / WARP vs WireGuard for Personal Web Server

> [!info] 一句话导读
> I up until about 2 years ago used SSH keys for remote access to my personal web server/home environment. 2 years ago, I bought a Unifi Dream Router 7 and with t…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1wjw0i4/risks_of_cloudflared_warp_vs_wireguard_for/>
> 指标：得分=4 · 评论=16 · 赞踩比=0.71
> 作者：f00dl3　|　发布：2026-09-19T01:06:58+08:00
> 项目链接：—
> 采集：2026-09-29T09:43:45+08:00　|　id：`4e6666dd9a8c0b4e`

## 正文

I up until about 2 years ago used SSH keys for remote access to my personal web server/home environment. 2 years ago, I bought a Unifi Dream Router 7 and with that router, it has a built-in WireGuard client, so I started using VPN a lot more.

The VPN is great, does what I want, allows access from pretty much everywhere - but it has one small snag: I recently switched from T-Mobile to Visible+ Pro - and with that, I'm trying to reduce intense data use a bit so they don't cut me off. I'm hopping on WiFi networks a lot more now.

I'm finding some WiFi networks such as certain hospital guest networks block Wireguard and among other things Kalshi.  I researched this some, and came to the conclusion that setting up Cloudflared on my server with WARP access should in theory fix this problem - have not tested the specific use case yet - but it works for everything else pretty much seamlessly - apps I wrote for my phone communicate just fine with my private SSL cert / domain name I have mapped to 192 168 1 2.

The user security seems straight forward - actually better in some cases. If for example due to recent laws in the US want to uninstall any reference of my VPN before traveling internationally, I can easily remove the app and then re-install it w/ my GMail account instead of having to try to regenerate a WireGuard.conf file. A lot easier to set up. More modern - I gather most of corporate America is moving away from VPNs and moving towards ZeroTrust such as Z-Scaler or Cloudflare One - so knowing this tech makes me know more for my career.

The only risk I see - is that there is a slight risk Cloudflare can decrypt the traffic / shows it passing at their ingress/egress points. But since I don't have TLS inspection on - I'm not sure how much the decrypt risk is. Since my personal web server has a purchased SSL cert - it's probably encrypted just as good as anything else / the VPN keys, etc. Unless SSL encryption is very weak, I'm not too concerned about that. Any real server commands I run would be ran over SSH through the Cloudflared tunnel, so those would be encrypted too. I can't think of any instance where interactions are not encrypted in some form through the tunnel.

If anything, it should make me less likely to be port scanned as my public IP is not showing up as UDP traffic on various WiFi networks now.

Thoughts? Would you do this? Would you not? Concerns?

I'm kind of at a 50/50 point right now on if I want to do one or the other all the time going forwards. Cloudflared is a LOT easier logistically to manage. But it's not my VPN. But at the same time, someone who really wanted to hack in and read the traffic - in some ways they could more easily take over my router than Cloudflare's servers.

## 评论（18/18）

> **asimovs-auditor**（1 分） · 2026-09-19T01:07:07+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **f00dl3**（1 分） · 2026-09-19T01:09:23+08:00　
> I did not use AI at all to create this post.

---

> **saara_83**（1 分） · 2026-09-19T01:19:09+08:00　
> Cloudflared with an access policy is fine for this and it does solve the captive portal blocking problem, WARP just rides 443 so hospital guest wifi rarely touches it. The decrypt worry is mostly a non issue as long as you keep TLS end to end and dont terminate at their edge, they see the tunnel not the payload. Two real gotchas: your origin is now only as safe as your cloudflared token, so lock the tunnel down to one hostname and put access in front of anything sensitive. And test SSH over it before you commit, interactive sessions can feel laggy compared to wireguard.
>
> What are you using for access control, just the free zero trust tier?

---

> **selipso**（2 分） · 2026-09-19T01:20:03+08:00　
> My concern between these two was that Cloudflare is built for application traffic. Their ToS don’t allow you to transfer large files or host game servers. Wireguard doesn’t care because it’s an open protocol. Put something like fail2ban or crowdsec in front of your VM and it’s more freedom.

---

> **f00dl3**（1 分） · 2026-09-19T01:22:52+08:00　
> yeah free tier just default setup wizard now - email address (only my email)

---

> **f00dl3**（1 分） · 2026-09-19T01:23:48+08:00　
> From what I read is that their Cloudflared tunnel product does not care how much bandwidth you send over the tunnel. They only care about users - i.e. just me (1) user - they shouldn't care. I can transmit 20 TB over the tunnel in a month and from what I read, they wouldn't blink an eye.
>
> And why would you host a game server over a tunnel? Isn't the point of that for public to play on it? I would personally open a router port instead for that.

---

> **John_Mason**（1 分） · 2026-09-19T05:09:53+08:00　
> I recently switched to NetBird for a similar experience. They have both VPN and authenticated reverse proxy functionality (like Cloudflared). I can use their VPN most of the time, but if I’m traveling and encountering restrictive WiFi networks, I can go into the cloud portal and enable public reverse proxy (still requires auth) for certain services.

---

> **shrimpdiddle**（0 分） · 2026-09-19T06:17:57+08:00　
> > I'm finding some WiFi networks such as certain hospital guest networks block Wireguard
>
> Run WireGuard on other common ports... ex, 443, 8443, ...

---

> **shrimpdiddle**（1 分） · 2026-09-19T06:19:44+08:00　
> IIRC, 100 MB cap. So files must be chunked to stay within that cap.

---

> **f00dl3**（1 分） · 2026-09-19T07:01:11+08:00　
> No, a 10 GB SFTP upload will not fail due to file size limits on a Cloudflare WARP-to-Tunnel connection.While Cloudflare is famous for its 100 MB HTTP request body upload limit on Free/Pro plans, that restriction strictly applies to standard web traffic routed through the Cloudflare CDN/Proxy layer. When using the Cloudflare WARP client to connect directly to an internal server via Cloudflare Tunnel (Arbitrary TCP/Port 22), the traffic bypasses the HTTP stack entirely. Cloudflare imposes no file size limitations on raw TCP tunnel traffic.
>
> ^ per Google

---

> **SaleWide9505**（1 分） · 2026-09-19T09:35:55+08:00　
> What made you switch from T-Mobile to visible?

---

> **f00dl3**（1 分） · 2026-09-19T09:41:35+08:00　
> Auto Pay policies

---

> **SaleWide9505**（1 分） · 2026-09-19T09:50:33+08:00　
> What does that mean? The reason I ask is because you said you were trying to cut down on data usage plus I also went from a $100 T-Mobile plan to Visible. Eventually I left visible and got a computers 4 people sim. It gives me unlimited data for $15 a month on T-Mobile network. I get the same exact speeds and everything.

---

> **f00dl3**（-1 分） · 2026-09-19T09:55:54+08:00　
> First they stopped allowing you to do auto pay by credit card. So I used a bank account. Always built a 3-4 month credit up. Then a month or two ago, the T-Life app stopped allowing paying more than your bill amount. So that was the final straw.

---

> **saara_83**（1 分） · 2026-09-19T11:25:32+08:00　
> That works but the default wizard leaves the app wide open to any path under that hostname. Add a self hosted app in access and scope it to the exact path you need, otherwise one leaked link bypasses the whole thing. Email OTP is fine for one user, just set the session to something short.

---

> **f00dl3**（1 分） · 2026-09-19T11:37:16+08:00　
> What do you mean? If my intent is a VPN replacement, I want full access to everything on my network. So that's kind of a feature, not a bug.

---

> **f00dl3**（1 分） · 2026-09-21T08:33:38+08:00　
> wireguard forces udp though - unless you can make wireguard use tcp?

---

> **f00dl3**（1 分） · 2026-09-21T08:34:10+08:00　
> To confirm this I transfered a 20 GB file no issue

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
