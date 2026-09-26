---
type: "corpus"
item_id: "6a9bbfe7cec25c14"
title: "Selfhosting a public site - first timer"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1ujnhnj/selfhosting_a_public_site_first_timer/"
author: "emaG_eh7"
published_at: "2026-06-30T20:13:03+08:00"
captured_at: "2026-09-26T10:02:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 12, "comments": 30, "upvote_ratio": 0.75}
comments_count: 28
comments_total: 30
discovered_via: "reddit:113d+settle3"
---

# Selfhosting a public site - first timer

> [!info] 一句话导读
> My partner and I are eloping soonish and want to have a basic website for friends and family to view things like date, registry, pictures, etc. Since the elopem…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1ujnhnj/selfhosting_a_public_site_first_timer/>
> 指标：得分=12 · 评论=30 · 赞踩比=0.75
> 作者：emaG_eh7　|　发布：2026-06-30T20:13:03+08:00
> 项目链接：—
> 采集：2026-09-26T10:02:06+08:00　|　id：`6a9bbfe7cec25c14`

## 正文

My partner and I are eloping soonish and want to have a basic website for friends and family to view things like date, registry, pictures, etc. Since the elopement is just us, it hosts a bit more than a basic wedding site so that guests can see blog style posts and comment on things, but I don't think anything is too complex. Thinking I can get the basic site up with AI support fairly easily.

The scarier part (for me) is making it accessible for those friends and family to reach. I'm relatively new to selfhosting in general, and certainly never made something publicly accessible from my network. The only obvious thing to me is to isolate the site in its own proxmox VM, but beyond that I'm not totally sure. I think a VLAN is probably correct - but I'm not sure my current hardware (unmanaged switches and Asus Zenwifi router) properly support them. Maybe firewall stuff is an appropriate substitute, and I'll just have to spend some time learning how to set that up?

What else should I be thinking of here? I could potentially host on a pi (3b+) that I have sitting around doing nothing, if hardware isolation provides something that proxmox VM doesn't.

ChatGPT mentioned Cloudflare Tunnels and Access for better security, which generally made sense to me. If there is a reasonable alternative though, I'd be interested. Some folks that we expect will be interested in actually seeing the website and posts lean pretty far from "tech-savvy," to the point that we think submitting an email and using a one time passcode might be a big blocker for them. Not totally opposed to the idea if its the best option, though.

I realize that there are existing providers for this sort of thing, but I'm looking in to selfhosting because they take a portion of any donations made through the registry, and the sites are often a bit rigid in terms of customization, which my partner was bummed about. We'll still fallback to that if we have to, but looking into selfhosting for a bit seemed reasonable. Plus, I was excited about the opportunity to learn more about how to make things publicly accessible in a safe and secure way.

## 评论（28/30）

> **asimovs-auditor**（1 分） · 2026-06-30T20:13:13+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **emaG_eh7**（1 分） · 2026-06-30T20:15:10+08:00　
> No AI in the making of this post, just a bit of initial research done with it's aid.

---

> **darce_helmet**（12 分） · 2026-06-30T20:19:57+08:00　
> cloud flare tunnel is a good option. i would just get a cheap vps for a month and host it there.

---

> **pd1zzle**（1 分） · 2026-06-30T20:21:49+08:00　
> Step 0 would be owning a domain, which is not clear from your post. Do you have a domain?
>
> Cloudflare tunnels are the no brainer option - basically a wireguard connection to cloudflares edge. No IP exposure for you, no port exposing either, no need to sort out firewall on the router (exceptto isolate devices, possibly). Close the tunnel, network is locked down. You would need to at least utilize CF as your nameservers, they could be registrar as well.
>
> technically you don't need a domain, you could route people to your IP... but that's not really the best setup

---

> **Wasted-Friendship**（1 分） · 2026-06-30T20:22:27+08:00　
> I did the same. Pay for a website. Less hassle. Post a qr to a Venmo or PayPal.
>
> Otherwise, get a cheap NUC, put it in its own VLAN. Only expose port 80 or 443, depending on how secure. Run Apache. Keep it up to date.

---

> **Educational_Board_51**（-3 分） · 2026-06-30T20:22:55+08:00　
> Agree with this!

---

> **Stumbows**（5 分） · 2026-06-30T20:24:38+08:00　
> I self host a basic website. It runs on debian for the OS, then Astro and NGINX for serving the site. Cloudflared with a tunnel from CloudFlare. Have to have your own domain. But it works flawless. Runs ultra light and is super easy to update.

---

> **These-Apple8817**（2 分） · 2026-06-30T20:25:15+08:00　
> Frankly... Just get a cheap VPS.. cheapest ones cost like 5 bucks a month or something like that. That way you aren't risking your own network.. Although if you still wanna do it completely self-hosted, like the other guy said, Cloudflare Tunnels is a good option.. Hell, even if you don't use Tunnels, you should still use Cloudflare so you can get bit of extra protection against malicious people, you don't wanna be that guy who gets their own network DDOS'd to oblivion because they didn't bother adding any security to their self-hosted website...
>
> Also.. If you are comfortable, there is one more option which is Cloudflare Pages / Workers but you would need to be comfortable writing your own website in framework like Astro for example. That option is completely free for hobbyists etc, all you would need is a domain.

---

> **emaG_eh7**（2 分） · 2026-06-30T20:26:58+08:00　
> I don't have a domain yet, but I'm also not too worried about buying one and getting that setup. Consequences around security are much more severe if that's not solid!

---

> **emaG_eh7**（1 分） · 2026-06-30T20:27:45+08:00　
> Ah, that's a good call! I think my partner is pretty excited about the idea of making it exactly as envisioned now, but will definitely plan on that if we can't make selfhosting work.

---

> **Omagasohe**（3 分） · 2026-06-30T20:32:07+08:00　
> Get a vps, less then $1 a month...
>
> https://lowendbox.com/blog/1-vps-1-usd-vps-per-month/
>
> I wouldnt want anything critical on one, but for what you want to do its not bad.
>
> Pair with a .top domain from porkbun and your under $20 and a safe home network..

---

> **pd1zzle**（2 分） · 2026-06-30T20:35:51+08:00　
> well, in a sense a domain is some level of security if done right.
>
> Cloudflare at least has a number of edge security options such as traffic filtering, region blocking that can help offload some responsibility from you. They also offer proxied DNS records which means your IP is never returned for nameserver requests and in theory could remain hidden if you manage your server headers properly.
>
> But to go back to the security part, I have caddy on a separate machine running a reverse proxy. It obtains a wildcard certificate from let's encrypt (no exposure of what is or is not a valid subdomain - small level of obscurity), crowdsec (banning/blocking of bad actors and traffic patterns), fail2ban (repeated auth failures, probing etc banning). I also have the network gateway set up to only accept incoming from CF IPs (using the proxy mode) and region block everything outside the US.
>
> Some of this is totally overkill it also was not super hard to set up. if you did a tunnel, you'd probably still want the general security stuff for banning/detecting bad traffic but you can skip the ip stuff.
>
> Also just to prepare you, when you open this you'll probably get like 50,000 port scans in the first few hours. Unless you just left the machine wide open, it's fine and expected.

---

> **Express-Cartoonist39**（0 分） · 2026-06-30T20:36:26+08:00　
> Proxmox, Cyberpanel with built in firewall..Ur golden.. If you want email hit up ur provider to sync hostnames and you then get ur own email send freedom...

---

> **StockSalamander3512**（-1 分） · 2026-06-30T20:38:10+08:00　
> Go with Cloudflare, you can buy your domain there, and it’ll be secure.  RAID Owl on YouTube has a really good tutorial.

---

> **Positive-Abalone-387**（1 分） · 2026-06-30T20:47:36+08:00　
> I can help u with building website and hosting it ket me know if u need any help

---

> **bencos18**（1 分） · 2026-06-30T20:53:08+08:00　
> similar here pretty much
>
> my blog is running behind ngnix proxy manager and q cloudflare tunnel

---

> **GolemancerVekk**（1 分） · 2026-06-30T21:08:56+08:00　
> This stuff is way overkill for selfhosting.
>
> I mean you could, if you already have your own server or a VPS and you're selfhosting apps. But even then I'd just selfhost a CMS privately and export the resulting static website to a CDN like bunny.net. Low cost, they take care of security and availability and everything for you, impossible to hack since it's just the HTML and images.
>
> Don't expose a selfhosted CMS, even through Cloudflare tunnels, CF tunnels are not the security that you think they are.
>
> Best option would be to get on a CMS service like get a wordpress website, build your site there and give people the address and call it a day.
>
> Pricing varies greatly, from 1$/mo for a CDN like Bunny, to $4/mo for Wordpress online, $10/mo for a VPS, $15/mo for Squarespace etc.
>
> You're going to keep this thing up for a year tops then you'll archive it for yourself and that's it, plan accordingly. I mean I wouldn't start buying hardware specifically for this if I were you.

---

> **flobin**（1 分） · 2026-06-30T21:20:22+08:00　
> If you don’t want to use cloudflare tunnels, you could do something similar with this setup.
>
> Get your domain name, and add a CNAME record that points to Gcore. Gcore then pulls from your home server.
>
> If you have a static IP, you would be done. But you probably don’t.
>
> So get dedyn.io (dynDNS) subdomain through [deSEC](https://desec.io/). Then set up a cronjob that makes your home server connect to it via curl so that dynDNS always has the right IP. Then make Gcore pull from that.
>
> You can then even set up your firewall to only allow ports 443 and 80 to Gcore.
>
> If it sounds complicated, then that’s because it is. But it’s doable and doesn’t expose your home wifi IP / ports to the entire internet. It also avoids using Cloudflare.
>
> If anybody has any tips regarding this setup, I’d love to hear.

---

> **_hhhnnnggg_**（2 分） · 2026-06-30T21:48:02+08:00　
> I'd say, you can use a magic link for authentication. The site asks your friend to use a preregistered email, then they will receive an email with the magic link to log in. You will need to get some way to maintain the session, usually JWT.

---

> **emaG_eh7**（1 分） · 2026-06-30T21:54:28+08:00　
> Nice, this looks ideal. Totally fine with throwing a few dollars at it to keep my mind at ease. I'll have to read more on it to fully understand it I think, but seems like cloudflared runs on the VPS for the security stuff and then tailscale is used for it to reach my selfhosted stuff and serve it to users? There's probably some additional benefits of static IP/routing stuff but guessing that mainly comes for free with the VPS and cloudflare.
>
> This also seems great because when we are the only ones using the site to remember things (like, literally 2 days after the wedding realistically), I should be able to just disconnect the VPS and access it on my LAN like anything else I have locally, right?
>
> Curious if this approach would also allow me to keep admin controls (posting pictures etc) available only on LAN as well?

---

> **emaG_eh7**（1 分） · 2026-06-30T21:56:16+08:00　
> This is a super basic site - static pages, a few pictures, the ability to post a comment. Tunnels seems perfectly suited to it.

---

> **emaG_eh7**（1 分） · 2026-06-30T22:06:58+08:00　
> Yeah, absolutely. It feels a little overkill but given how simple the site is I'm definitely considering hosting it on separate hardware (pi) for a little extra security. Still on the same network as everything though so not sure that provides much value if someone finds a way to attack.

---

> **horizon_games**（2 分） · 2026-06-30T22:26:07+08:00　
> I think you're overthinking this. Wedding registry/pics/comments are a common platform you could just sign up for and use for a couple months. Rolling your own will be more work than you expect.
>
> But you covered that in the end, so I guess rip it. A Pi 3b+ will be more than enough. Put a solid Linux distro on it, put UFW and Fail2Ban, move SSH to a different port, do basic Nginx hardening. I'd skip any fancy auth and just do Basic HTTP Auth with a single account and tell people the password over email when you send them the site.
>
> I wouldn't hassle with payment processing as that's an entire ball of wax and easy to mess up, especially letting AI lead the way.

---

> **AcksYouaSyn**（1 分） · 2026-06-30T23:15:28+08:00　
> Cloudflare workers / pages is a free option for hosting a simple static site. The domain name is your only cost in this setup.

---

> **JoeB-**（1 分） · 2026-06-30T23:24:56+08:00　
> I agree with the others suggesting a Virtual Private Server (VPS).  A VPS can be inexpensive and will protect your home network.  For example, a [Digital Ocean Droplets (cloud VMs)](https://www.digitalocean.com/pricing/droplets) start at a flat rate of $4 USD per month, have a static public IP address, and can be deployed in seconds.  These are monthly, so no contracts or need to pay annually.
>
> A VPS essentially is like a Proxmox virtual machine at home, except it is hosted with a public IP.  You'll still be self-hosting from a software perspective.  At Digital Ocean, you can get a vanilla Linux server with a distribution of your choice (Fedora, Debian, Ubuntu, etc.), and can elect to have some apps (e.g. Wordpress,  LAMP, Node.js, etc.) preinstalled.  Uploading your own custom image (raw, qcow2, etc.) is an option as well, so you can develop and test at home (in a Proxmox VM?) before uploading.
>
> I strongly recommend against exposing your home network to the Internet unless you know exactly what you are doing and are prepared to monitor activity.

---

> **darce_helmet**（2 分） · 2026-06-30T23:36:25+08:00　
> you dont need to mess with tailscale or tunnels. just do everythign on the VPS.

---

> **chiasmatic_nucleus**（2 分） · 2026-07-01T22:16:24+08:00　
> For something like this, just throw the static files on Netlify's (or cloudflare pages, or github pages) free static hosting, point your domain at it, bam job done no risk

---

> **looshi99**（1 分） · 2026-07-04T09:02:37+08:00　
> If you're even remotely concerned, host the entire thing on the VPS. If you don't mind getting a vps for a few months, just host the full shebang on the VPS. It's not super unsafe to host it yourself if you are careful and know what you're doing, but even if you're just not confident the price of a small VPS for a 3-4 months probably could be less than $5-10 (haven't looked, but certainly less than $15), which is a reasonable price for peace of mind and not having to configure very much on your own. There's also the fact that if this is important to you and your future spouse, the hardware cannot fail on the VPS. If you are careful with your data (basically don't delete it yourself) it cannot be lost, where as that may require more work if you're hosting it on something like a USB or sd card on a rpi or other not-the-most-reliable hardware. Obviously this can be managed, but potentially another stress point.
>
> If your desire is to self-host for the sake of self-hosting, I can understand that but know that there is always risk as soon as you expose any service to the internet. Ensuring your services are up to date, you have a router with a well set up firewall doing SPI in place, and that you have something in place to ban repeated connection attempts (things like fail2ban, crowdsec, etc), will get you to where I wouldn't be worried about it, though. You could also do a VPN like tailscale, but in practice I think you should be able to secure a web server (especially if you use a reverse proxy and/or dmz) so guests don't have to go to the trouble of dealing with a VPN. Since I presume this would be important to you both, make sure you have an adequate backup strategy.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
