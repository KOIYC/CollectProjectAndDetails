---
type: "corpus"
item_id: "d628e1d2e1d68091"
title: "What is the current goto for mesh networking?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w3g2ns/what_is_the_current_goto_for_mesh_networking/"
author: "RiffyDivine2"
published_at: "2026-08-31T22:51:22+08:00"
captured_at: "2026-09-21T03:05:15+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - VPN
metrics: {"score": 7, "comments": 18, "upvote_ratio": 0.74}
comments_count: 19
comments_total: 19
discovered_via: "reddit:52d+settle3"
---

# What is the current goto for mesh networking?

> [!info] 一句话导读
> Good morning, I wanted to ask and see what everyone else is using? I was using netbird but the lack of multiport forwarding for game servers is becoming an issu…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1w3g2ns/what_is_the_current_goto_for_mesh_networking/>
> 指标：得分=7 · 评论=18 · 赞踩比=0.74
> 作者：RiffyDivine2　|　发布：2026-08-31T22:51:22+08:00
> 项目链接：—
> 采集：2026-09-21T03:05:15+08:00　|　id：`d628e1d2e1d68091`

## 正文

Good morning, I wanted to ask and see what everyone else is using? I was using netbird but the lack of multiport forwarding for game servers is becoming an issue. So, I was going to go back to pangolin, but my friends still want a mesh network between our four machines.

## 评论（19/19）

> **asimovs-auditor**（1 分） · 2026-08-31T22:51:38+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **RiffyDivine2**（1 分） · 2026-08-31T22:54:12+08:00　
> I didn't. Which is why it's going to clearly read like someone still waking up.

---

> **thelittlewhite**（1 分） · 2026-08-31T23:03:26+08:00　
> Pangolin can now do that as well if I am not mistaking.

---

> **IC3P3**（1 分） · 2026-08-31T23:04:15+08:00　
> I'm using Headscale. It's not the simplest setup, netbird might be the better choice, but it's what I came up with. Biggest problem for my automatic setup script is that I can't automate the adding process as IPs are only sequential or random and the keys for adding new devices can only be created after first boot (plus the Headscale node does not automatically have the client)

---

> **mbecks**（4 分） · 2026-08-31T23:07:16+08:00　
> I’m not totally sure what you mean, you can configure the NetBird connections to allow access to multiple ports

---

> **Wenir**（2 分） · 2026-08-31T23:14:55+08:00　
> What is multiport forwarding?

---

> **DentalStairway**（1 分） · 2026-08-31T23:52:05+08:00　
> I set up tailscale on my machines and never looked back, but for gaming servers the nat traversal can be hit or miss sometimes. Have you checked what pangolin does with mesh these days? Last time I used it was more for reverse proxy stuff, not full mesh between machines.

---

> **Top-Scar7769**（1 分） · 2026-08-31T23:54:49+08:00　
> for just 4 machines and gaming id honestly try headscale over netbird again or pangolin
>
> headscale gives you a self hosted control plane but you still use the official tailscale clients, so you get proper multiport forwarding and subnet routing that actually works well for game servers, without netbirds limitations you already ran into
>
> if you want fully open source top to bottom instead, netbird has actually been improving multiport/port range support in recent updates, might be worth checking their latest release notes before writing it off completely, could be less of an issue now than when you first hit it
>
> pangolin is solid too but its really built more for exposing services publicly through a reverse proxy setup, not true peer to peer mesh between friends machines, so it might feel like a workaround rather than the right tool for what you actually want
>
> for 4 people just wanting a straightforward mesh with game server ports working properly, id lean headscale, closest to "just works" without netbirds forwarding headache

---

> **samsonsin**（2 分） · 2026-08-31T23:57:24+08:00　
> No clue what you're talking about here tbh. The netbird interface operates as a layer 3 only LAN + some custom routing rules on top of wireguard. There's no inherent limitation of ports and what not (unless you're talking about something like integrated reverse proxy or something similar, which is entirely unnecessary in your case).

---

> **RiffyDivine2**（1 分） · 2026-09-01T00:12:07+08:00　
> Can it, then that makes this easy choice.

---

> **RiffyDivine2**（1 分） · 2026-09-01T00:13:51+08:00　
> When a server needs ports say 7900 to 7910, I should have said port range I know.

---

> **vik_ftsky**（1 分） · 2026-09-01T00:23:29+08:00　
> Are you talking about the reverse proxy?

---

> **RiffyDivine2**（1 分） · 2026-09-01T00:43:47+08:00　
> I must be overlooking something then because when I try to setup a game server that needs a range of ports you can only proxy one and not a range. Is there a way to do it?

---

> **mbecks**（5 分） · 2026-09-01T00:48:43+08:00　
> If by proxy you mean NetBirds reverse proxy, you might not need to use the proxy. In the UI, make a policy that gives peers access to the host the game server runs on directly, choose TCP type, then right there in ports section you can input a range of ports.

---

> **thelittlewhite**（1 分） · 2026-09-01T00:57:01+08:00　
> I think that's what you are looking for, right ?
> https://docs.pangolin.net/manage/resources/public/raw-resources

---

> **RiffyDivine2**（1 分） · 2026-09-01T01:53:45+08:00　
> Yes, sorry. I want to be able to host the game servers at home behind the vps IP but was just wondering what people use for mesh networking.

---

> **StillLoading_**（2 分） · 2026-09-01T02:40:51+08:00　
> If all machines run the client you don't need the reverse proxy, just create a policy to allow access to the game server peer & ports.
>
> If you want to allow access from the public internet thats a different story. Currently you can only open multiple ports by creating multiple service mappings.

---

> **tylian**（1 分） · 2026-09-01T17:38:43+08:00　
> Ah, tunneling. I don't know of any that let you do ranges because they're semantically the same as just opening a new server on every port in the range.
>
> Can't say they don't exist, but if they do it'll just be the same as adding an entry for every port.

---

> **Last-Car-6128**（1 分） · 2026-09-04T09:52:26+08:00　
> Mostly wireguard / wg-easy.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
