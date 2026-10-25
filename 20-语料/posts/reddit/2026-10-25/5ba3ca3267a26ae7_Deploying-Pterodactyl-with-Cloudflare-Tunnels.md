---
type: "corpus"
item_id: "5ba3ca3267a26ae7"
title: "Deploying Pterodactyl with Cloudflare Tunnels"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6lb7a/deploying_pterodactyl_with_cloudflare_tunnels/"
author: "ExtentMother6358"
published_at: "2026-10-15T21:14:03+08:00"
captured_at: "2026-10-25T23:28:44+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 4, "comments": 15, "upvote_ratio": 0.75}
comments_count: 15
comments_total: 15
discovered_via: "reddit:14d+settle10"
---

# Deploying Pterodactyl with Cloudflare Tunnels

> [!info] 一句话导读
> I am trying to get pterodactyl setup on my server but cannot get past setting up the actual node. I'm having issues with the remote url, if I put in my subdomai…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6lb7a/deploying_pterodactyl_with_cloudflare_tunnels/>
> 指标：得分=4 · 评论=15 · 赞踩比=0.75
> 作者：ExtentMother6358　|　发布：2026-10-15T21:14:03+08:00
> 项目链接：—
> 采集：2026-10-25T23:28:44+08:00　|　id：`5ba3ca3267a26ae7`

## 正文

I am trying to get pterodactyl setup on my server but cannot get past setting up the actual node. I'm having issues with the remote url, if I put in my subdomain it sends a 302 html response instead of the expected json response. If i try to put in localhost I can get the "tls: failed to verify certificate | doesnt contain any IP SANs". I followed the pterodactyl documentation but could't get letsencrypt to work with cloudflare, so I found [this](https://www.youtube.com/watch?v=a3ZRc9-98qw) tutorial which sets up the certs with openssl. I do not know what I am doing wrong at this point and would appreciate any guides on how to set up pterodactyl with cloudflare.

## 评论（15/15）

> **asimovs-auditor**（1 分） · 2026-10-15T21:14:13+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **ExtentMother6358**（3 分） · 2026-10-15T21:15:04+08:00　
> No AI was used

---

> **tankerkiller125real**（2 分） · 2026-10-15T21:21:07+08:00　
> You can't put the nodes behind cloudflare at all, at the end of the day the node IPs are going to be exposed regardless given that Cloudflare won't pass anything other than HTTP/HTTPs unless your using Spectrum or one of their other various enterprise products.

---

> **ExtentMother6358**（1 分） · 2026-10-15T21:31:09+08:00　
> So what do people usually do then? I would like to use my domain name to access it that way a couple of close friend can access the game servers.

---

> **Own-Recognition5168**（1 分） · 2026-10-15T21:31:12+08:00　
> the 302 is cloudflare sending you to the login page instead of the API, you need to add a bypass rule in cloudflare for the /api path so it lets the plain HTTP through without any of the browser challenge or redirect nonsense
>
> for the TLS error with localhost, that's because the cert you made with openssl doesn't have localhost as a SAN so the wings daemon freaks out when it tries to verify itself. you can either regenerate the cert with localhost and [127.0.0.1](http://127.0.0.1) in the SAN list or just disable ssl verification in the wings config if you're only accessing it locally anyway
>
> most people run into this exact wall, the documentation really glosses over how cloudflare messes with the api handshake

---

> **whodoyouthinkyouare9**（1 分） · 2026-10-15T21:32:40+08:00　
> Cloudflare Tunnel is the issue here. Wings works better with a real hostname and valid TLS cert

---

> **ApprehensiveBrain863**（2 分） · 2026-10-15T21:36:46+08:00　
> You can put them behind cloudflare you just shouldn't proxy them I think they mean

---

> **CreepyHunterX**（2 分） · 2026-10-15T22:06:36+08:00　
> Use tailscale, give them access to machine with share. To allow via domain, create DNS only record on 100.x tailscale's adress. Also record are directing into private adress, so HTTP check 'Let's Encrypt' won't pass, but DNS-01 via API Cloudflare will pass.

---

> **ExtentMother6358**（1 分） · 2026-10-16T02:32:17+08:00　
> So I figured out one of the main issues was that I had cloudflare access so everytime wings tried to access my domain it was getting that page and crashing. Once I fixed that issue I got wings to run, however, I am now having issues with the panel connecting to the node. I believe it has something to do with my node subdomain but I'm not getting any significant error messages on my wings log or my web browser console. I am trying my hardest to keep it using cloudflare tunnels so I don't have to forward any ports but I guess that is very difficult.

---

> **Oweh-Vandame**（2 分） · 2026-10-16T06:16:20+08:00　
> are you running the panel and the node on the same machine? if so the node needs to reach the panel via the public url but thats going out through the tunnel and back in, which causes the 302. try setting it up so the node talks to the panel on the local network instead

---

> **GLachance9**（1 分） · 2026-10-16T07:20:55+08:00　
> I just love seeing the phrase 'Pterodactyl Deployed'

---

> **1100000011110**（1 分） · 2026-10-16T08:29:47+08:00　
> I use a free playit.gg tunnel, and then I have a redirect in my DNS records that points my personal domain to the URL generated by playit

---

> **ExtentMother6358**（2 分） · 2026-10-16T22:38:01+08:00　
> Yeah I got caught up in following the guides that I forgot to take a moment to think that having the panel go out to come right back for the node was part of the problem. I ended up wiping everything and starting a fresh install. Right now I am trying to figure out how I want make this work. Right now it's either just create a DNS record and port forward or configure everything with local ips and have a tunnel go to the panel. I'm sure the ladder will be difficult and not work but I would like to try and avoid forwarding ports.

---

> **NurseCatnip**（1 分） · 2026-10-19T04:19:14+08:00　
> I’m about to set mine up today. I have a domain through cloudfare too. I saw someone else suggest tailscale but seeing as my brother is gonna use it for him and his friends. I can’t just be giving EVERYONE tailscale access. Let me know how you intend to keep it secure. Cause I’m gonna have todo dns only no proxy through cloudfare pointing to my machine. Curious too cause I use nginx for my let’s encrypt. Not sure what else todo for security purposes.

---

> **ExtentMother6358**（2 分） · 2026-10-20T01:20:26+08:00　
> I ended up forwarding my ports just so I can get pterodactyl to work as intended. I tried multiple ways to get it to work with cloudflare tunnels but couldn't figure it out. As far as keeping it secure on the internet I would at the minimum turn on 2FA for all accounts in the settings. I only plan on making accounts for a couple of friends that I can trust.

## 关联链接

- https://www.youtube.com/watch?v=a3ZRc9-98qw

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
