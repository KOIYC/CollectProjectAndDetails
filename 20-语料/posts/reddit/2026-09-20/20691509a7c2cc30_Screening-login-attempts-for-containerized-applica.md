---
type: "corpus"
item_id: "20691509a7c2cc30"
title: "Screening login attempts for containerized applications"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1whh7zz/screening_login_attempts_for_containerized/"
author: "GigaHertz8771"
published_at: "2026-09-16T08:00:49+08:00"
captured_at: "2026-09-20T14:14:31+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 4, "comments": 8, "upvote_ratio": 0.7}
comments_count: 10
comments_total: 10
discovered_via: "reddit:7d+settle3"
---

# Screening login attempts for containerized applications

> [!info] 一句话导读
> Forgive me for what may be a newby question, but I have a web application - in this case Jellyfin, that I host for myself and some family and friends. I current…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1whh7zz/screening_login_attempts_for_containerized/>
> 指标：得分=4 · 评论=8 · 赞踩比=0.7
> 作者：GigaHertz8771　|　发布：2026-09-16T08:00:49+08:00
> 项目链接：—
> 采集：2026-09-20T14:14:31+08:00　|　id：`20691509a7c2cc30`

## 正文

Hello everyone,

Forgive me for what may be a newby question, but I have a web application - in this case Jellyfin, that I host for myself and some family and friends. I currently have Jellyfin running in a Docker container, and Nginx running on the host machine serving it.

I've done a decent job hardening the configuration for both, but I'd still like to use fail2ban to autoban IPs that fail logins. The issue I'm having here is that Jellyfin's logs only show internal Docker network IPs, and so all activity reported in the logs only shows as some address in the 172.16.0.0/12 subnet. Nginx doesn't have any of its own user authentication set up, so sniffing the Nginx logs yields no results, and thus no bans.

So my question is:

Is there a way to have jellyfin detect source IPs from behind NAT so that I can actually create a fail2ban filter that works, or is this a larger misconfiguration problem that would require me to restructure how I've built this server?

I'm fairly new to hosting and would greatly appreciate some guidance here. Thanks :)

## 评论（10/10）

> **asimovs-auditor**（1 分） · 2026-09-16T08:01:10+08:00　
> Thanks for posting to r/selfhosted. Your post has been temporarily removed. Please reply to this comment explaining how AI was used in the creation of your post/project. Once you reply, your post will be automatically approved. To learn more about why this is required, please see our [pinned post](https://www.reddit.com/r/selfhosted/comments/1sey9ch/quarter_2_update_revisiting_rules_again/).

---

> **GigaHertz8771**（1 分） · 2026-09-16T08:02:40+08:00　
> AI was not used at any point in this post, nor in the configuration and deployment of the server being referred to by the post. I am a firm believer in snooping forums until I find what I need, and only posting as a last resort.

---

> **youknowwhyimhere758**（3 分） · 2026-09-16T08:25:06+08:00　
> Reading the docs:
>
> >
> When traffic is forwarded through a reverse proxy, Jellyfin sees the proxy’s IP address rather than the client’s. This introduces potential security risks and can also break compatibility, since Jellyfin will not be able to differentiate between local and remote connections. Therefore, if set up incorrectly, all limitations for external access will not work.
> Therefore,
>
> the IP address(es) of your reverse proxy must be configured under “Known Proxies”
>
> in Jellyfin’s Network settings. This allows Jellyfin to respect the
>
> X-Forwarded-For
> ,
>
> X-Forwarded-Proto
> , and
>
> X-Forwarded-Host
> headers and use the associated value as the source IP address. By default, Jellyfin will discard all forwarded-for headers that do not originate from a "known Proxy". This is so that malicious devices will not be able to hide their IP address by providing a forwarded-for header.
> This assumes that the reverse proxy is set up to include this header, which is not always the case by default. If issues with source IP forwarding appear, this should be checked.

---

> **GigaHertz8771**（0 分） · 2026-09-16T08:26:18+08:00　
> Thank you! I'll look into this

---

> **Onoitsu2**（7 分） · 2026-09-16T08:26:25+08:00　
> I want to say it is due in part to the way NGINX is proxying the request, you need to pass the proper headers, so Jellyfin can see where the request came from properly.
>
>     server {
>         listen 443 ssl;
>         server_name jellyfin.yourdomain.com;
>
>         location / {
>             proxy_pass http://:8096;
>
>             # Core headers needed to pass the Real IP
>             proxy_set_header Host $host;
>             proxy_set_header X-Real-IP $remote_addr;
>             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
>             proxy_set_header X-Forwarded-Proto $scheme;
>             proxy_set_header X-Forwarded-Host $host;
>
>             # Disable buffering for smooth media streaming performance
>             proxy_buffering off;
>         }
>     }
>
> In Jellyfin go to Administration > Dashboard > Networking
> Scroll down to the Known Proxies field.
> Input the IP address of your Nginx container.
>
> It should now show you the REAL IP of the connection being proxied to your Jellyfin.

---

> **GigaHertz8771**（2 分） · 2026-09-16T08:27:08+08:00　
> Thank you!

---

> **mattsteg43**（2 分） · 2026-09-16T08:29:16+08:00　
> If you set your known proxies correctly and your proxy sets the correct headers it will just work.

---

> **FewBrain208**（2 分） · 2026-09-16T23:14:31+08:00　
> nice catch on the known proxies list. one thing to keep in mind is that if you ever change your container networking setup the gateway address can shift, so its worth checking that if bans suddenly stop working down the road

---

> **transendingAI**（2 分） · 2026-09-18T04:30:29+08:00　
> A reverse proxy can pass the original client address to Jellyfin in a forwarded header. Check both parts of that setup: Nginx needs to send the client address, and Jellyfin needs to trust the Nginx proxy through its Known Proxies setting.
>
> Trust only the address Jellyfin sees for your Nginx proxy. Trusting arbitrary clients' forwarded headers would let them supply a false address.
>
> Before enabling bans, make one failed login from an external connection and confirm that Jellyfin's log records that connection's public IP. Then test that the fail2ban action actually blocks requests through Nginx. Correct log matching and effective firewall blocking are separate things to verify.

---

> **GigaHertz8771**（1 分） · 2026-09-18T04:36:42+08:00　
> Thanks for commenting. Thankfully, I resolved this issue the other day. Nginx has the proper configuration in its headers, and Jellyfin points to the proper Docker gateway. Fail2ban now works as expected after some firewall setup.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
