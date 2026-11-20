---
type: "corpus"
item_id: "853ac5a24adf27a9"
title: "Migrating from Proton & Google, what should I self-host next?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xs7z7z/migrating_from_proton_google_what_should_i/"
author: "iLikeVideoGamesAndYT"
published_at: "2026-11-10T07:56:49+08:00"
captured_at: "2026-11-20T09:47:05+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-11-20"
pub_day: "2026-11-10"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 33, "comments": 42, "upvote_ratio": 0.8367346938775511}
comments_count: 40
comments_total: 42
discovered_via: "reddit:14d+settle10"
---

# Migrating from Proton & Google, what should I self-host next?

> [!info] 一句话导读
> TLDR; I'm looking for recommendations on what to self-host next, as well as Linux and Android client suggestions to go with whatever you suggest. I'm moving awa…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xs7z7z/migrating_from_proton_google_what_should_i/>
> 指标：得分=33 · 评论=42 · 赞踩比=0.8367346938775511
> 作者：iLikeVideoGamesAndYT　|　发布：2026-11-10T07:56:49+08:00
> 项目链接：—
> 采集：2026-11-20T09:47:05+08:00　|　id：`853ac5a24adf27a9`

## 正文

TLDR; I'm looking for recommendations on what to self-host next, as well as Linux and Android client suggestions to go with whatever you suggest. I'm moving away from Proton and still de-googling but I'm mostly just in this for the fun of self-hosting, so I don't have a specific service in mind. See bottom for hardware details.

I'm looking to migrate from Proton after the recent controversy, and since I'm interested in self-hosting my own stuff, I want to self-host whatever I can. I'm also still in the process of de-googling. Because of this, I'm more interested in self-hosting utility services that Google and Proton provide, such as email, calendar, and drive. I've already set up an email and calendar server (via Stalwart) and a private network drive (very basic, no web UI and only accessible from my home network). I use WireGuard to tunnel my email traffic through my VPS with minimal system resources (from Vultr, not self-hosted) to hide my public IP.

The question is, I'm not sure what services I actually want to self-host next. My primary reason for doing it is not to migrate from any service in particular (even though that is part of it), it's more just because I'm interested in the self-hosting part alone. The Proton controversy is just the catalyst that made me decide to start self-hosting more.

I'm also open to suggestions for clients to use these self-hosted services. For example, I spent a great deal of time looking for the right email clients that worked on Linux and/or Android that have little to no telemetry, have modern UI, allow Gmail, Outlook, and IMAP inboxes, and support E2E encryption. For whatever service you suggest I self-host, I'm open to suggestions for Linux/Android clients to use with it.

Some useful info about what I'll be hosting on:

OS: Fedora Linux 43 (open to changing distros, this used to be my daily driver, so I'd need to figure out what files to save first)

RAM: 16 GB

Disk: 512 GB SSD

CPU: 12th Gen Intel Core i5-1235U @ 4.40 GHz

GPU: Intel Iris Xe Graphics @ 1.20 GHz (integrated)

NPU: None

Keep in mind that this is hosted at my house, so if the service I host requires 24/7 internet connectivity without interruption, it may be a problem since my WiFi does go down briefly every once in a while.

Where applicable, I would like the option to use encryption and any other high-privacy options.

## 评论（40/42）

> **asimovs-auditor**（1 分） · 2026-11-10T07:56:59+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **iLikeVideoGamesAndYT**（0 分） · 2026-11-10T08:00:34+08:00　
> None of my post content is AI generated but I asked AI for advice on better structuring my post to make it more clear.

---

> **butdattruetho**（19 分） · 2026-11-10T08:14:36+08:00　
> Self hosting email is a massive waste of time.
> I self hosted my emails for 12+ years, and managed mail solutions for SMB for a decade. Since migrating my emails to Proton a few years ago it just works. Zero pain. The only reason I would have to migrate away is if they break encryption or use my email metadata to train AI models.
>
> My most productive self-hosted solution was n8n. I had so many automations hooked up through it when I used to be a contractor

---

> **BlazingZebra16215**（19 分） · 2026-11-10T08:15:30+08:00　
> Try self-hosting a Nextcloud instance.

---

> **Wally-Gator-1**（2 分） · 2026-11-10T08:23:56+08:00　
> A password manager (Vaultwarden) is a must have.

---

> **ouoxbykwm**（2 分） · 2026-11-10T08:39:44+08:00　
> Given you've already got email, calendar and a private drive running, my next project would be backups rather than another app: Restic or Borg to a local USB disk plus an encrypted off-site copy, then do a test restore. With the Wi-Fi interruptions you mentioned, configure retries and make sure a failed run is visible, since a green dashboard isn't a substitute for checking the data. That gives you a safer base for experimenting with another service later.

---

> **Only-Stable3973**（1 分） · 2026-11-10T08:47:16+08:00　
> For me I am running things that I use, when I first started it was fun to run everything under the sun but mainly at the moment I run Traefik and Socket-Proxy, Jellyfin I use Filebrowser-Quantum all the time and Picoshare because it's so simple and just works, and of course Wireguard. The rest is my \*R-Stack that I do use. There are other thinks like HomePage and Notediscover great tools.

---

> **Fair-Soil-6267**（2 分） · 2026-11-10T08:51:59+08:00　
> I have mailcow on a vm in my house that points to a VPs with postfix. I have it able tk get through Google and working on Microsoft.

---

> **winner_68**（3 分） · 2026-11-10T09:26:55+08:00　
> I went through a similar move last year and the thing I wish I had done first was sort out backups before adding anything new. I kept email where it was and focused on the stuff that actually hurt to lose. For photos I ended up on Immich in Docker, it handles the phone backup part really well and the face search is good enough that I stopped missing Google Photos. For files I use Syncthing between my laptop and the server rather than a full Nextcloud install, mostly because on a small box Nextcloud felt heavy for what I needed and Syncthing just quietly keeps folders in sync. I run both behind WireGuard like you already do, so nothing is exposed directly. The one habit that saved me was setting up a simple restic backup to an external drive before I migrated anything, then testing a restore of a few photos. It is boring work but migrating twice because something went wrong is worse.

---

> **brock0124**（3 分） · 2026-11-10T09:35:05+08:00　
> To each their own, but I wouldn’t consider it a waste of time if you’re semi-technical and do it for the love of the game. If you send your outbound through a relay, you cut out 90% of the pain in running an email server. Especially if you’re only doing it for yourself and/or your immediate family.
>
> Sure, you’re still reliant on a 3rd party to send your mail, but you don’t have the prying eyes of  Google/apple/ training their AI models on your inbox and snooping/selling all your data.
>
> I’ve run my own email server for a couple years now and haven’t had any headaches after first getting setup.

---

> **brock0124**（3 分） · 2026-11-10T09:37:25+08:00　
> Checkout Bulwark for your mail client. It’s basically a sister app for Stalwart and leverages all the benefits of JMAP. They’ve got a slick webmail and mobile/desktop apps in beta. Not sure if it allows adding external IMAP accounts tho.

---

> **RestOk6290**（1 分） · 2026-11-10T10:07:50+08:00　
> i have one too and i don't see nothing better.

---

> **FifenC0ugar**（3 分） · 2026-11-10T12:29:21+08:00　
> Nextcloud kept having issues with updates (I'm on unraid). I switched to filerun

---

> **svill**（2 分） · 2026-11-10T12:43:53+08:00　
> Howdy! Can you expand on the relay aspect? Which one do you use? Any pointers or tutorials you followed to get yours up and running? Thanks in advance!

---

> **caskater47**（0 分） · 2026-11-10T13:10:28+08:00　
> Shameless plug here, but you should check out my latest open source project [rapidmx.io](http://rapidmx.io) . It's a full scale comms platform that offers fully secure and private email/calendar/contacts/tasks, video conferencing, and more. It supports end-to-end and zero-access encryption just like Proton Mail but you have full control and host it yourself. It's super easy to setup and the web client is fairly robust and stable already. I'm working on a native app with support all major OS.

---

> **TitanfallMech**（0 分） · 2026-11-10T13:24:40+08:00　
> Self-hosting is exciting!

---

> **7StandArrow**（0 分） · 2026-11-10T13:53:26+08:00　
> Self-hosting is a journey!

---

> **anydragon_anyons**（3 分） · 2026-11-10T14:01:15+08:00　
> Not who you asked, but I use AWS SES as the outbound relay for my side project's domain (receiving is Cloudflare Email Routing). Things I'd tell anyone setting it up:
>
> \- You start in the SES sandbox: verified recipients only, 200/day. Getting out took 1-2 business days, and the request is mostly about how you handle bounces, so set up bounce handling first.
>
> \- If your DNS is on Cloudflare, keep the DKIM CNAMEs grey-cloud (DNS only). Proxying them breaks DKIM silently.
>
> \- Use a subdomain for MAIL FROM, otherwise it fights with your receiving MX.
>
> \- Skip the SES "get started" wizard. It can publish records to Route53 for you, which quietly adds a hosted zone you pay for monthly.
>
> Once DNS checked out, domain verification took about 15 minutes for me.

---

> **HeftyCrab**（2 分） · 2026-11-10T14:16:41+08:00　
> One of the best things Ive self hosted is Syncthing. You set it up once then it just runs for years without an issue.

---

> **OktayAcikalin**（4 分） · 2026-11-10T15:06:07+08:00　
> Huh OP has Fedora. I have Fedora server edition and nextcloud AIO runs, backups and updates perfectly fine. 🤷🏻‍♂️

---

> **Shotokant**（1 分） · 2026-11-10T16:44:26+08:00　
> I heard it was problematic. I tried opencloud. Happy with it so far. I've abandoned Onedrive fully now.

---

> **Admirable-Site-7273**（5 分） · 2026-11-10T16:48:39+08:00　
> What is the recent proton controversy ?

---

> **btc_maxi100**（2 分） · 2026-11-10T17:56:52+08:00　
> Stalwart

---

> **mikkel1156**（9 分） · 2026-11-10T20:08:38+08:00　
> Statements that they are AI first and security second.

---

> **iLikeVideoGamesAndYT**（10 分） · 2026-11-10T20:31:06+08:00　
> That and the censorship in their subreddit. And also the way it was revealed how they're AI over security. The CEO called taking extra time for pen testing BS and "looser thinking"

---

> **brock0124**（2 分） · 2026-11-10T21:41:10+08:00　
> I use Smtp2Go free tier. It’s super easy to setup and they’ve got great docs for getting started!

---

> **Wynnbuck1**（1 分） · 2026-11-10T22:29:32+08:00　
> Can you guys elaborate on this? I get mail cow but for the postfix do you need to open ports with postfix or can I use like my nord vpn? Is that what you mean by VPs? Because postfix is open source self hosted. Thanks!

---

> **supersr71**（1 分） · 2026-11-10T23:34:09+08:00　
> https://i.redd.it/kuuyvwne0t0i1.png
>
> Nextcloud would be a good choice.
>
> I set up my private cloud and you could have a trial with the temporary user:
>
> test01/Cfguser001

---

> **Dhanni-Asmus**（1 分） · 2026-11-11T01:02:13+08:00　
> if youre already running email and calendar, contacts via CardDAV and a notes server are the obvious missing pieces from that ecosystem. Just make sure whatever client apps you pick have solid offline caching since your home connection drops occasionally

---

> **InternetTheGreat**（1 分） · 2026-11-11T04:08:29+08:00　
> Ich Miete ein vps bei netcup. Darauf läuft mein mailcow und ein paar weitere Dienste und Seiten. Habe ebenfalls von Proton gewechselt. Einfach, weil vps günstiger ist, als die subscription. Und ich diese eigentlich nur wegen meiner Arbeit bei Bund hauptsächlich damals benutzt habe. Nun habe ich über 7 Domains, die auch einen Mailpostfach benötigen, die ich nicht so einfach und günstig bei Proton anbinden konnte.
> Deshalb bin ich auf mailcow umgestiegen. Ein paar skripte und rsync mit heim nas machen mein Backup aus.

---

> **CitronSpirited9681**（1 分） · 2026-11-11T05:56:31+08:00　
> since you're already running mail through a vps, i'd put anything new behind wireguard instead of opening more ports, and get a backup of the mail and the drive going that you've actually tested restoring. not the fun answer but it's the stuff that hurts when it goes wrong.

---

> **CokeAndChill**（1 分） · 2026-11-11T06:11:56+08:00　
> Isn’t AI killing it at security? The Linux kernel is a punching bag for every other cybersecurity model…

---

> **mikkel1156**（5 分） · 2026-11-11T06:32:43+08:00　
> Just didn't sound like AI is being used in a more practical manner, but more CEO saying "pump out new features fast, speed is what matters". So to me it is just kinda the signal it sends.

---

> **Street_Love8169**（1 分） · 2026-11-11T10:13:17+08:00　
> I use proton, wasn't aware of these problems. I might be looking as well.

---

> **alexwbaule**（1 分） · 2026-11-11T19:59:58+08:00　
> Since you already have WireGuard, most of this can stay private and only reachable through the tunnel. For the Android side, Syncthing (the Syncthing-Fork build) is great for file sync with your server and doesn't need a web UI. Immich covers photo backup with a decent Android app, and Vaultwarden works with the normal Bitwarden clients if you haven't moved passwords yet. For your Stalwart calendar and contacts, DAVx5 handles CalDAV/CardDAV on Android. If you want to browse the drive, Material Files can open SFTP and WebDAV shares directly.

---

> **Fair-Soil-6267**（1 分） · 2026-11-12T00:14:29+08:00　
> So I have my mailcow vm on proxmox I tie into my vps running postfix via Tailscale and I have postfix be the front end for receiving and sending mail and I had to add forwarder records on mailcow to know where to look

---

> **Comfortable-Duty7143**（1 分） · 2026-11-13T15:39:35+08:00　
> what are people using to keep self hosted services from getting hammered by scanners and bots when they’re exposed for remote access? my home setup is pretty basic and I’d rather not deal with constant connections attempts

---

> **tplusx**（1 分） · 2026-11-14T17:36:47+08:00　
> How many features could they possibly pump out before running out of ideas? Is it forever? What happens when they reach the end of their roadmap?

---

> **Fearless-Camera-8975**（1 分） · 2026-11-14T20:46:43+08:00　
> Tailscale keeps everything off the public internet entirely,but if you need to expose stuff,putting it behind zenshield or a reverse proxy with fail2ban cuts on the noise.

---

> **potato-truncheon**（1 分） · 2026-11-16T21:51:36+08:00　
> Try opencloud.
> Actually - first thing you must do is think about how you will approach backups, redundancy and configuration management (and backup).  You will want to set yourself up so that you can restore things when they go wrong or fail.  Mistakes will be made (it's normal).  Where will you store credentials? Code/config?
> Where will you back up off site? On? Do you have family that will need at your data if anything happens to you?
>
> You won't have all the answers as you start (well, you might - I didn't!) but gotta keep thinking about this as you start to build things out.
>
> Personally, I'm hosting opencloud (switched from nextcloud), immich, audiobookshelf, calibre-web automated, authentik, bichon, caddy, etc...  And running on Proxmox with a truenas vm and a Ubuntu docker vm (for isolation).  Dockhand makes things a lot easier.
>
> Lots of rclone to pull my outside cloud files into my own control.
> And restic to push to offsite backup.
>
> (As for email, it's the very last thing I would ever consider hosting, if at all.  Too much at stake and too much to go wrong with difficult recovery options.)

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
