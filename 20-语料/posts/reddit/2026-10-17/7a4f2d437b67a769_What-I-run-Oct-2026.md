---
type: "corpus"
item_id: "7a4f2d437b67a769"
title: "What I run - Oct 2026"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1wzngic/what_i_run_oct_2026/"
project_url: "https://codeberg.org/forgejo/forgejo"
author: "EatMoreBananaPudding"
published_at: "2026-10-07T12:32:37+08:00"
captured_at: "2026-10-17T13:37:02+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-07"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Wednesday Exceptions
metrics: {"score": 312, "comments": 66, "upvote_ratio": 0.93}
comments_count: 70
comments_total: 70
discovered_via: "reddit:14d+settle10"
---

# What I run - Oct 2026

> [!info] 一句话导读
> I just want to introduce myself and tell you all about my homelab. It's all pretty high-level, feel free to ask me about anything here.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1wzngic/what_i_run_oct_2026/>
> 指标：得分=312 · 评论=66 · 赞踩比=0.93
> 作者：EatMoreBananaPudding　|　发布：2026-10-07T12:32:37+08:00
> 项目链接：<https://codeberg.org/forgejo/forgejo>
> 采集：2026-10-17T13:37:02+08:00　|　id：`7a4f2d437b67a769`

## 正文

Helllooo everyone!

I just want to introduce myself and tell you all about my homelab. It's all pretty high-level, feel free to ask me about anything here.

# About me

I’m just someone that absolutely loves technology. Software and systems are mostly where my heart lies, I’ve been working in IT for about 19 years. I have been homelabbing and self-hosting since about 2005. It started with game servers then learning how to become a sys admin, then wanting control over my data, and now I just want to explore different technology stacks and new software.

My homelab is a bit of a mix of running services for my family and a testing ground for learning new technology.

# Quick and dirty

My entire homelab is Proxmox as the hypervisor, debian VMs to run Docker and Komodo. Forgejo  deploys my containers on Komodo. Docker labels control Traefik and exposure.

6 hosts (3 “production” and 3 test lab) and \~147 containers.

|Hostname|CPU|RAM|Storage|Used For|
|:-|:-|:-|:-|:-|
|Jupiter|i7-9800X|128GB|122TB|App + Storage|
|Saturn|i9-13900K|64GB|3TB|Home Assistant + Dev + DNS (Secondary)|
|Mars|N150|16GB|500GB|Router + DNS (Primary)|
|Neptune|2x Xeon Silver 4214R|1.5TB|24TB|Testing + DR|
|Uranus|2x Xeon Silver 4214R|1.5TB|24TB|Testing|
|Pluto|2x Xeon Silver 4214R|1.5TB|24TB|Testing|

# Jupiter

My main server, pretty much what I would consider "production" in my house. I pretty much throw everything on this whether it's just for shits and giggles or actually useful. I try out every remotely interesting self-hostable application there is, so this list changes constantly,

It was running Unraid until a few weeks ago, but it has finally fallen inline with the rest of my environment with Proxmox and a debian VM.

I see people ask "Do you actually use any of this?" when people run a bunch of software, so I've split it into what I actually use and what just kind of exists.

**What actually gets used**

Most of these are actually used on a daily or weekly basis.

* [Authentik](https://github.com/goauthentik/authentik) \- SSO/identity
* [Excalidraw](https://github.com/excalidraw/excalidraw) \- Whiteboard
* FamFeed - Private Social Media
* [Forgejo](https://codeberg.org/forgejo/forgejo) \- Git hosting
* [Glance](https://github.com/glanceapp/glance) \- Dashboard
* [Guacamole](https://github.com/apache/guacamole-client) \- Remote access
* [Immich](https://github.com/immich-app/immich) \- Photo library
* [Karakeep](https://github.com/karakeep-app/karakeep) \- Bookmarks
* [Mealie](https://github.com/mealie-recipes/mealie) \- Recipes
* [ntfy](https://github.com/binwiederhier/ntfy) \- Push notifications
* [NZBGet](https://github.com/nzbgetcom/nzbget) \- Usenet downloader
* [Open WebUI](https://github.com/open-webui/open-webui) \- AI chat
* [OpenHands](https://github.com/OpenHands/OpenHands) \- AI agents
* [Outline](https://github.com/outline/outline) \- Wiki
* [Penpot](https://github.com/penpot/penpot) \- Design tool
* [Plex](https://www.plex.tv) \- Media server
* [PrivateBin](https://github.com/PrivateBin/PrivateBin) \- Encrypted pastebin
* [Seerr](https://github.com/seerr-team/seerr) \- Media requests
* [Windmill](https://github.com/windmill-labs/windmill) \- Workflow automation

**Used, just not directly**

* [Grafana](https://github.com/grafana/grafana) \- Dashboards
* [Jellyfin](https://github.com/jellyfin/jellyfin) \- Media server
* [NetBox](https://github.com/netbox-community/netbox) \- IPAM/DCIM
* [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) \- Document management
* [Prowlarr](https://github.com/Prowlarr/Prowlarr) \- Indexer manager
* [Radarr](https://github.com/Radarr/Radarr) \- Movie management
* [ReadMeABook](https://github.com/kikootwo/ReadMeABook) \- Audiobook requests
* [SABnzbd](https://github.com/sabnzbd/sabnzbd) \- Usenet downloader
* [Sonarr](https://github.com/Sonarr/Sonarr) \- TV management
* [Tautulli](https://github.com/Tautulli/Tautulli) \- Plex stats
* [Tunarr](https://github.com/chrisbenincasa/tunarr) \- Live TV channels

**For that rare moment**

* [Audiobookshelf](https://github.com/advplyr/audiobookshelf) \- Audiobook server
* [BentoPDF](https://github.com/alam00000/bentopdf) \- PDF tools
* [ByteStash](https://github.com/jordan-dalby/ByteStash) \- Code snippets
* [IT-Tools](https://github.com/CorentinTh/it-tools) \- Dev utilities

**Infrastructure Apps**

If I'm logging into one of these directly, something is broken. lol

* [Backrest](https://github.com/garethgeorge/backrest) \- Backups
* [Beszel](https://github.com/henrygd/beszel) \- Monitoring
* [CrowdSec](https://github.com/crowdsecurity/crowdsec) \- Intrusion prevention
* [Dozzle](https://github.com/amir20/dozzle) \- Log viewer
* [Komodo](https://github.com/moghtech/komodo) \- Container management
* [Node Exporter](https://github.com/prometheus/node_exporter) \- Host metrics
* [Traefik](https://github.com/traefik/traefik) \- Reverse proxy
* [Umami](https://github.com/umami-software/umami) \- Web analytics
* [UniFi Network Application](https://github.com/linuxserver/docker-unifi-network-application) \- Network controller
* [VersityGW](https://github.com/versity/versitygw) \- S3 gateway
* [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) \- Metrics database
* [Wazuh](https://github.com/wazuh/wazuh) \- SIEM

**I should probably tear them down**.

* [Actual Budget](https://github.com/actualbudget/actual) \- Budgeting
* [Aurral](https://github.com/lklynet/aurral) \- Music discovery
* [LazyLibrarian](https://gitlab.com/LazyLibrarian/LazyLibrarian) \- Book management
* [Lidarr](https://github.com/Lidarr/Lidarr) \- Music management
* [Navidrome](https://github.com/navidrome/navidrome) \- Music streaming

# Saturn

This box was originally just to spin up VMs and test different applications, VMs, or build an environment to teach something to some of my junior. It was the first Proxmox box in the environment and after using it for a while I ended up switching all computers over to Proxmox.

Now it runs Home Assistant, secondary DNS, and some VMs that I use for Dev and AI agent work.

* [Home Assistant](https://github.com/home-assistant/core) \- Home automation
* [Music Assistant](https://github.com/music-assistant/server) \- Multi-room audio
* [Technitium DNS](https://github.com/TechnitiumSoftware/DnsServer) \- DNS (secondary)
* [Z-Wave JS UI](https://github.com/zwave-js/zwave-js-ui) \- Z-Wave controller
* [Eclipse Mosquitto](https://github.com/eclipse/mosquitto) \- MQTT broker
* [Faster Whisper](https://github.com/rhasspy/wyoming-faster-whisper) \- Speech-to-text
* [Piper](https://github.com/rhasspy/piper) \- Text-to-speech
* [Nanit](https://github.com/indiefan/home_assistant_nanit) \- Baby monitor
* [Node Exporter](https://github.com/prometheus/node_exporter) \- Host metrics
* [Backrest](https://github.com/garethgeorge/backrest) \- Backups
* [Beszel Agent](https://github.com/henrygd/beszel) \- Monitoring agent

# Mars

This is a little Beelink EQ14 that has dual 2.5 Gbps NICs and I purchased it specifically to be a dedicated router/firewall.

* [OPNsense](https://github.com/opnsense/core) \- Router/firewall
* [Technitium DNS](https://github.com/TechnitiumSoftware/DnsServer) \- DNS (primary)
* [Cloudflare DDNS](https://github.com/favonia/cloudflare-ddns) \- Dynamic DNS
* [Tailscale](https://github.com/tailscale/tailscale) \- VPN exit-node
* [Node Exporter](https://github.com/prometheus/node_exporter) \- Host metrics
* [Backrest](https://github.com/garethgeorge/backrest) \- Backups
* [Beszel Agent](https://github.com/henrygd/beszel) \- Monitoring agent

# Uranus, Neptune, and Pluto

Relatively new hosts that are taking the simulation workloads I was running alongside production. They run Proxmox as well. I have OpenTofu and Ansible playbooks that spin up "scenarios" or my DR bubble. I am currently focused on OpenStack, Kubernetes, and other business simulation environments.

# Current Goals

**DR / Rebuild**

Currently I am working on being able to rebuild and/or restore my entire homelab from a single script. The idea is if Jupiter, Saturn, or Mars have a catastrophic failure I can point the script to my new host and it will build it out, let me select which services to restore and hopefully be back up and running in a few hours.

**Security Monitoring**

I spent a chunk of the past year learning SIEM and how to tune alerts in Wazuh. Thankfully I work very closely with my InfoSec team at work so I had a helping hand, plus Claude being able to fill in some of the gaps. I am trying to get a Claude-based agent to do a lot of the triage and so far it is janky but works pretty well. My next step is to allow this agent to gather telemetry around whether or not the alert coming in is related to me. The idea is that between my remote sessions, where my phone is, and a few other details the agent will build a confidence score for how likely it is me accidentally generating the alert. It will then ping me to get confirmation, if I respond with "Not me" then it will go through some steps to either kill acces**s.**

I am also working on various apps and automations around my families needs, mostly our private social media.

Ask me anything!

## 评论（70/70）

> **asimovs-auditor**（1 分） · 2026-10-07T12:32:57+08:00　
> Thanks for posting to r/selfhosted. Your post has been temporarily removed. Please reply to this comment explaining how AI was used in the creation of your post/project. Once you reply, your post will be automatically approved. To learn more about why this is required, please see our [pinned post](https://www.reddit.com/r/selfhosted/comments/1sey9ch/quarter_2_update_revisiting_rules_again/).

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T12:34:16+08:00　
> No AI was used to write this post.
> AI was used for some of the diagram stencils.

---

> **Morkai**（60 分） · 2026-10-07T12:44:14+08:00　
> Yes i too run almost 5TB of RAM as a hobby project... 👀

---

> **EatMoreBananaPudding**（3 分） · 2026-10-07T12:52:47+08:00　
> LOL! Yea, it's a bit excessive and I really should get rid of some of it honestly.

---

> **Morkai**（16 分） · 2026-10-07T12:53:55+08:00　
> I'll take that burden off you, step right this way.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T13:04:19+08:00　
> I'd trade it for a GPU in a heartbeat. lol!
>
> The bulk of it is ECC RAM and the systems are too hot and power hungry to run all the time.

---

> **darkjoker213**（0 分） · 2026-10-07T13:08:40+08:00　
> Once again, fantastic read ! Thank you for sharing. I’m already taking some notes to improve my setup!

---

> **EatMoreBananaPudding**（2 分） · 2026-10-07T13:11:07+08:00　
> Thank you!! If there is any part of this you would like a deep dive on let me know.

---

> **pericoXVI**（8 分） · 2026-10-07T14:06:15+08:00　
> You are the 5h cause of high RAM prices rn...

---

> **Radicalism**（3 分） · 2026-10-07T14:23:16+08:00　
> Very nice!
> I was wondering, in a setup like this, how do you work with non-443 traffic? I assume traefik is not running in the same container as all apps.
>
> Specifically I am looking how to setup ssh for my gitserver. DNS would route git.mydomain.com to my traefik instance, but I would want git ssh access through forgejo@git.mydomain.com/repo.git to end up at my git container. How would you handle this, by having your proxy also forward ssh traffic, or something else?

---

> **dowath**（3 分） · 2026-10-07T14:39:02+08:00　
> Oh dang, planet names is so much cooler than my naming system...
> \[MY NAME\] + \[TECH WORD\] + \[1000-9000\]

---

> **tweek91330**（3 分） · 2026-10-07T15:13:54+08:00　
> Wow, i don't wanna pay your electric bill.
>
> Good setup, i'd like to have something like that to play with but i'm a cheap man, i'm consolidating everything on one server.
>
> I'd sell most of it if i were you (those juicy 1.5tb ram servers would make quite a bit honestly).

---

> **tyda1957**（2 分） · 2026-10-07T15:20:07+08:00　
> Hah, same exact node names as I have. Im deploying pluto as my 4th later today though.

---

> **dodovt**（10 分） · 2026-10-07T15:32:08+08:00　
> I once too hosted a multitude of applications but nowadays it's mostly a media server (plex+arrs+zurg+rclone+realdebrid), paperlessngx, traefik + crowdsec + authelia, ntfy, vaultwarden, obsidian livesync, frigate, actual budget and backrest.
>
> And I mostly don't use the media server anymore.
>
> Posting it made me realize I still have too much and I should downgrade even more to stuff I actually use, not something that I "may use one day again".
>
> After my hype of having a homelab passed, I just stopped using most things.

---

> **csgeek-coder**（2 分） · 2026-10-07T15:53:08+08:00　
> That's what too many apps I need to support in my free time. I don't think I'm responsible for this many things at work and they're paying me.
>
> Backups and restore patterns and making sure it all works would make me anxious.

---

> **donfrezano**（8 分） · 2026-10-07T16:10:13+08:00　
> Amazing. Side note, what do you use to generate those diagrams?

---

> **QT31416**（4 分） · 2026-10-07T16:11:18+08:00　
> I have the same naming scheme, planets!
>
> Mercury is my fastest machine, doing most of my analytics and data science work, hosting my code server and rstudio server.
>
> Venus and Earth are twins, 2 proxmox nodes in a high availability cluster, they run most of my home lab/prod and home automation stuff.
>
> Mars is my "2nd home", hosting my NAS and media server.
>
> Jupiter, a raspberry pi booting off of an SSD (ironically the smallest machine),  is the proxmox high availability Qdevice master, and it hosts my Zigbee2MQTT so it connects to my Zigbee devices. Jupiter's moons are my IOT devices and there are many, just like the planet Jupiter's moons.
>
> I'm also looking at getting a mini PC with multiple ethernet ports for my infosec server. I plan on installing OPNsense, then feed a mirrored trunk port to it for IDS purposes, and also Wazuh for my SIEM. I don't know if this is a good idea or not. How difficult was it to deploy Wazuh and get it to a point where you felt you were 80% set? i.e., it's usable and you're somewhat confident to rely on it.

---

> **DazednConfucioused**（7 分） · 2026-10-07T16:20:07+08:00　
> Why don’t you use your apps though?
>
> Do you jsut not watch movies/shows these days?
>
> I still use a lot of my stuff like paperless in particular.
>
> I also keep vaultwarden. Never use it but I back up my passwords there.  JUST in case I lose my Apple account or something catastrophic.

---

> **EnRoueLibre**（4 分） · 2026-10-07T16:28:25+08:00　
> Okay, this is a huge waste of resources... A major lack of optimization, in my opinion.
>
>  I run more than half of these services on an Intel N100 mini PC with 16 GB of RAM running FreeBSD.
>
> Also I was looking for the "FamFeed" githbub repository ... But I can't find it. Can it be selfhosted ?! I just found the website where you can sign up , but no link to any git repo ...

---

> **forwardslashroot**（2 分） · 2026-10-07T16:55:36+08:00　
> How did you setup the Restic server? Are you using the rest-server by any change?

---

> **ITGuytech**（2 分） · 2026-10-07T17:03:38+08:00　
> Hey, what did you use to make the physical design in the third pic?

---

> **averycleanslate**（1 分） · 2026-10-07T17:17:11+08:00　
> daaaaaang, that's ... impressive. :O

---

> **Fakman**（3 分） · 2026-10-07T18:10:49+08:00　
> Why was your same post deleted few days ago by moderator?

---

> **EatMoreBananaPudding**（6 分） · 2026-10-07T19:18:50+08:00　
> Thank you, I used Excalidraw for these!

---

> **EatMoreBananaPudding**（5 分） · 2026-10-07T19:21:03+08:00　
> It wasn't Wednesday and I flaired it as personal dashboard, so it violated rule 5.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T19:21:14+08:00　
> Thank you!

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T19:24:34+08:00　
> I used Excalidraw!

---

> **EatMoreBananaPudding**（0 分） · 2026-10-07T19:32:51+08:00　
> If it was just the services listed, then yea an absolute waste.
>
> It used to be a single server, just Jupiter. At that time it pretty much just ran maxed out on RAM 24/7. It was running the above services all by itself. Plus my scenario lab, Dev VMs, and daily drivers.
>
> I ended getting Saturn so that I could split the scenario lab to different hardware and stop straining Jupiter.
>
> Mars came in when I wanted to have my own router.
>
> The FamFeed listed in my post is a private app for just my family. Its a whole lot of vibe code, so I'm not willing to post it publicly.
> Not affiliated with the one you can find on Google, sorry about that.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T19:34:42+08:00　
> I am using [backrest](https://garethgeorge.github.io/backrest/) and the [multihost sync](https://garethgeorge.github.io/backrest/docs/multihost) feature across the nodes.
>
> It works very well and I highly recommend it!

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T19:39:23+08:00　
> That's amazing. I didn't realize so many also had this naming scheme, I love it!
>
> For Wazuh, it took me a while, but I didn't have a lot of time to dedicate towards it. And in hindsight I would have started with a single application that was not very noisy so I could learn without drowning.
>
> I probably spent 2-3 hours a week on it for a month or 2, but I still tweak it today. Just more help via Claude to be honest, then I share some of my ruling with my SIEM team at work to make sure I'm not shooting myself in the foot.

---

> **MFKDGAF**（2 分） · 2026-10-07T19:40:28+08:00　
> How is Jellyfin not used directly?
>
> I understand the others in that section like Radarr is used from Seer.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T19:45:33+08:00　
> Thankfully these services are 99% hands off at this point.
>
> Backup and restores for my critical services are automated via Ansible and OpenTofu. The playbook runs, I log in, confirm the app is functional and data exists.
>
> Minor updates are handled by Renovate and majors are sent to an agent to check breaking changes against my configuration. I just click "Merge" from my phone. If it was all manual I would reduce. Lol!
>
> I manage a portion of the IT team at work so I'm slowly drifting away from the technical and use my homelab to stay sharp.. ish.

---

> **EatMoreBananaPudding**（2 分） · 2026-10-07T19:50:22+08:00　
> I can understand that. I tell my juniors at work to start small only expand when you actually need the service.
>
> I just really enjoy it, its my main hobby and my learning ground so I'm not sure if it will ever dwindle down.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T19:55:37+08:00　
> The homelab adds a minimum of $80 every month. Not great, but not horrendous.
>
> The bulky nodes are pretty much on during the weekend only and shut down otherwise. They idle at about $25 a month.
>
> I will likely sell or gift the bulky nodes as time goes on, but at the moment it is too fun to play with. Lol!

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T20:00:13+08:00　
> Tailscale mostly for any none 443 service.
>
> But for git I use HTTPS only and so do the others that utilize my Forgejo instance. SSH is not exposed on that container
>
> If you go the SSH router over the internet, which I just wouldn't if you have alternatives, make sure password based login is disabled and you are only using keys. If it is just you though I would highly recommend a VPN instead.

---

> **PaperPull**（1 分） · 2026-10-07T20:01:37+08:00　
> Check out PaperPull since you're using Paperless-ngx. I made a self-hosted version. You can easily download years of statements / receipts from major providers and then have the downloaded files go straight into your consume folder. [https://github.com/rheeloaded/paperpull/](https://github.com/rheeloaded/paperpull/) . Let me know what you think about it.

---

> **Objectivespeculation**（8 分） · 2026-10-07T21:09:34+08:00　
> the pain and sufferings some people have

---

> **nemo_chan**（6 分） · 2026-10-07T21:14:04+08:00　
> Your DR/rebuild goal is probably the most interesting part of this setup to me.
>
> Coming from DevOps, I’ve found that rebuilding the infrastructure is usually the easy part. The harder question is how much state you can actually recover, and whether the restore process has ever been tested from scratch.
>
> For a homelab I’d almost treat it like a small disaster recovery exercise: assume one of the Proxmox hosts disappears completely, rebuild onto a clean machine, restore only the essential services, and see what breaks.
>
> If you can do that without relying on anything that existed on the failed host, you’ve got something much more valuable than just backups.

---

> **QT31416**（2 分） · 2026-10-07T21:40:13+08:00　
> Feeding 1 application to Wazuh does sound like a good idea as a start. I'll try that.
>
> I guess having an infosec or SIEM team at work would be a big help. Wish we had that. Hah.
>
> Thanks for the tips!

---

> **csgeek-coder**（2 分） · 2026-10-07T21:57:41+08:00　
> So my home lab is either A. Apps that are neat, but I don't care if they break or B. This is critical and will really suck if it breaks.
>
> For anything in the B camp I really should have:
>
>   \- Backup at the very least
>   \- A restore path to get it back in case it all breaks.
>   \- Monitoring to know when things are breaking.
>
> That's too many things in your list to cause me to drop everything to fix cause it'll cause legit problems if I don't have access to my passwords, taxes I was going to file tomorrow, etc.
>
> That being said, it's a damn impressive setup. So props on that. I'm curious where you're using Tofu vs ansible though. My setup at this point is dropping k3s and using Argo to manage it. This does assume every app I run needs to have a docker container or like tandoor, I ended up writing a helm chart to support it.

---

> **Radicalism**（2 分） · 2026-10-07T21:59:20+08:00　
> I'm certainly not planning on exposing SSH over internet, but doesn't the problem exist also locally? Or are you internally DNSing your non-443 services directly to the service?
>
> In my case: I have a single reverse proxy, internally/on VPN also, where I terminate SSL using my single `*.domain.com` cert. So I would rather not attach my Forgejo instance (or other non-443) reverse proxy directly to that service and have to handle cert renewal there. But that means that also internally my SSH traffic arrives at my reverse proxy and not at Forgejo.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T22:05:24+08:00　
> I agree, rebuilding the infrastructure was quick and easy.
>
> I have all of my services in a tiered classification via tags in Komodo and Netbox. I can confidently say that I can rebuild and restore my most critical applications in an automated fashion.
>
> This past weekend I finalized pointing Tofu and Ansible at a blank Debian VM and running my DR playbook recreates the critical services and restores the data.
>
> I just need to expand it to a few more.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T22:57:08+08:00　
> Plex is the main thing used in my house, although my wife has been using Jellyfin more.
>
> My family has a variety of devices so the UX polish in Plex makes it easier for them. I also have some automations around Plex already so that needs to be rebuilt.
>
> As for VM structure it is fairly flat.
>
> **Jupiter**
> A singular massive VM named Callisto running all of it's own services at the moment. It was a lift and shift from Unraid to Debian and my data drives are all on a HBA so I passed the entire HBA to the VM rather than doing MergeFS and SnapRAID directly on Proxmox.
>
> This will eventually get split into VMs by criticality rather than service  type. Callisto itself will become purely storage with NFS, SMB and S3.
>
> **Saturn**
> I have some separation here.
> Rhea - DNS
> Dione - HomeAssistant + companions
> Titan - AI Agent VM
> Tethys - My daily drive for dev and management
>
> **Mars**
> Phobos - DNS
> Deimos - Router/Firewall

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T23:08:40+08:00　
> Yea I'm pretty much in the same boat. I tag my services by criticality to my life and keeping the homelab running. So my most critical services get a full 3-2-1 style backup, step-by-step rebuild log, and now have playbooks for rebuilding and restoring.
>
> Tofu and Ansible started more for my training/testing lab rather than managing my "production" homelab itself. I was building and tearing down scenario cases constantly so I use them to build out isolated networks and VMs. For my personal services though, Tofu manages rebuilding the VMs and Ansible configures them. I haven't finished this fully yet, but the idea is being able to point to a fresh physical host and let it rebuild then restore the services.
>
> I will likely move to K8s but I need to clean up and get all the spaghetti in a row first.
>
> I have a whole lot of alerting and monitoring in place and with some custom MCPs I am able to manage, troubleshoot, and deploy 95% of the environment with an AI agent doing the actual work. Human in the loop via NTFY or Forgejo.

---

> **OutrageousMobile9098**（4 分） · 2026-10-07T23:17:56+08:00　
> Self Hosted Final Boss

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T23:25:42+08:00　
> Internally and externally I point \`\*.domain.com\` to Traefik on Jupiter.
>
> For me this means \`git.domain.com\` points to 192.168.1.100
> Forgejo sits in a container network that can only speak to Traefik so SSH would not make it to it. But I could add it to another bridge and use \`ports\` in compose to expose 22 to LAN at \`192.168.1.100\` because it sits on the same host as Traefik.
>
> Then regardless of the traffic type \`git.domain.com\` would route appropriately.
>
> For services that are on a different host I set an explicit A record. And Technitium uses the most specific record when responding to a query.
>
> Does that make sense?
> DNS does not care about which port you are connecting on so it is just ensuring that the specific port you need to use sits on the IP that DNS is going to point to.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-07T23:27:15+08:00　
> lmao! There are people with WAY more services running.. they just lurk here instead of posting. As I have for years.

---

> **AfterEffexts**（2 分） · 2026-10-08T01:28:34+08:00　
> that’s a whole it dep dafq

---

> **Radicalism**（2 分） · 2026-10-08T03:54:27+08:00　
> Yeah makes total sense, thanks!
>
> The challenge in my case is that the proxy and gitserver are currently *not* on the same host as each other, so opening 22 on LAN on my git host would not work. I was hoping maybe you were in the same situation, since DNS is obviously not the solution here :)

---

> **EatMoreBananaPudding**（1 分） · 2026-10-08T05:08:29+08:00　
> Would you be comfortable putting traefik on the other node and using a subdomain?
>
> [https://github.com/jittering/traefik-kop](https://github.com/jittering/traefik-kop) is an option I am looking at, but it still requires the web port be exposed to LAN.

---

> **psychedelic_tech**（3 分） · 2026-10-08T05:48:38+08:00　
> thats a bot

---

> **EatMoreBananaPudding**（1 分） · 2026-10-08T06:08:32+08:00　
> ಠ_ಠ

---

> **nemo_chan**（1 分） · 2026-10-08T08:05:46+08:00　
> Are you talking to me? I'm not a robot.

---

> **nemo_chan**（1 分） · 2026-10-08T08:11:36+08:00　
> https://preview.redd.it/t14ztj49y4uh1.jpeg?width=1179&format=pjpg&auto=webp&s=6f87e6fd09bf5d9a1c3bed74e95918852c08cf92
>
> I've been using pve for about ten years.

---

> **Open-Adhesiveness-86**（1 分） · 2026-10-08T08:20:39+08:00　
> for the ssh case you want a traefik TCP entrypoint on 2222 (or 22 if the host sshd is moved) with a catch-all HostSNI(`*`) router, since plain ssh has no SNI and anything else won't match. forgejo also needs SSH_PORT and SSH_DOMAIN set to the external values in app.ini, otherwise the clone URLs it shows point at the wrong port and people just get connection refused.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-08T08:32:33+08:00　
> Oooh what app is that?

---

> **csgeek-coder**（2 分） · 2026-10-08T09:57:05+08:00　
> The biggest weakness I've seen in ansible that I LOVE in TF/Tofu is the state support. I was running everything through ansible a while back and had some bit rot around those playbooks. Especially the "cleanup" playbooks that were intended to undo an operation. The install playbook moved forward and the cleanup never got updated.
>
> There's also Crossplane if you want to drown in K8s manifests. It's basically TF/Ansible running in a K8s cluster. You manage a K8s from a k8. It's YAML everywhere.

---

> **EatMoreBananaPudding**（1 分） · 2026-10-08T10:32:55+08:00　
> I'll have to double check my cleanup playbooks now.
>
> As for AI, I already know at some point in my day job I will be asked to implement some sort of agent to manage infrastructure or support a team using agents to manage. I want to make sure I understand how to set it up appropriately and where its limitations are.
>
> I can drop into my main agent and pretty much tell it to do anything at this point in my homelab. But I put in an absolute ridiculous amount of time building processes, documentation and safeguards.
>
> The frontier models do pretty good already, but the others have some catching up to do.

---

> **nemo_chan**（1 分） · 2026-10-08T10:59:30+08:00　
> Yomo （IOS App）

---

> **toluwanimiarawomo**（1 分） · 2026-10-08T13:44:57+08:00　
> Hello! great to find your post. I saw the word "Aurral" in my dream, and i have really been curous about knowing what it means. please can you explain what "Aurral" does

---

> **dodovt**（0 分） · 2026-10-08T16:35:26+08:00　
> I watch some shows from there, but netflix is way easier and instant, and we get netflix for free with our ISP subscription. We only realistically use it when something isn't on netflix. But me and my wife are mostly switching to playing videogames together instead of just watching movies/shows together.

---

> **DazednConfucioused**（1 分） · 2026-10-08T16:41:03+08:00　
> Ah fair enough. Free Netflix is pretty nice lol.
>
> My media server has built up over the years to the point where at least on a personal basis it is better than Netflix.
>
> Has more shows I actually watch. Obviously discovery is still a bitch but with the whole arr suite set up whenever I see a new show mentioned it’s trivial to add and download the shows

---

> **dodovt**（1 分） · 2026-10-08T17:49:43+08:00　
> yeah i had a full storageless setup with real debrid, arrs, zurg, rclone, it worked very nice and almost instantly, netflix-like sensation, but we have a samsung TV and any samsung TV apps are terrible

---

> **psychedelic_tech**（1 分） · 2026-10-08T18:17:16+08:00　
> you use AI to write responses.

---

> **Radicalism**（1 分） · 2026-10-08T23:27:23+08:00　
> Comfortable sure, only thing I'd be giving up is to keep all my ssl termination (and certs) centralised on a single proxy. But I guess that's where I'll just have to make a choice

---

> **revive_the_cookie**（1 分） · 2026-10-11T00:53:38+08:00　
> What is that It-Tools Service? Is it the one by CorentinTh?

---

> **EatMoreBananaPudding**（1 分） · 2026-10-11T20:30:59+08:00　
> Yes it is.
>
> It has a ton of tools in it! You don't need to host it, but I do anyway.
>
> https://it-tools.tech/

---

> **revive_the_cookie**（1 分） · 2026-10-11T20:31:33+08:00　
> Oh ok. I heard it stopped development so thought you might be using a fork. Thanks!

---

> **Ill_Midnight7718**（1 分） · 2026-10-12T13:16:05+08:00　
> I’m also exploring self-hosting, and I like how you’ve separated your production and testing environments. Using Proxmox with Docker makes a lot of sense for managing different services. How has Komodo been working for you with container deployments?

---

> **NoIAmBard**（1 分） · 2026-10-13T13:41:09+08:00　
> can i run this off my raspberry pi?  asking for a friend

## 关联链接

- https://github.com/CorentinTh/it-tools
- https://github.com/Lidarr/Lidarr
- https://github.com/OpenHands/OpenHands
- https://github.com/PrivateBin/PrivateBin
- https://github.com/Prowlarr/Prowlarr
- https://github.com/Radarr/Radarr
- https://github.com/Sonarr/Sonarr
- https://github.com/Tautulli/Tautulli
- https://github.com/TechnitiumSoftware/DnsServer
- https://github.com/VictoriaMetrics/VictoriaMetrics
- https://github.com/actualbudget/actual
- https://github.com/advplyr/audiobookshelf
- https://github.com/alam00000/bentopdf
- https://github.com/amir20/dozzle
- https://github.com/apache/guacamole-client
- https://github.com/binwiederhier/ntfy
- https://github.com/chrisbenincasa/tunarr
- https://github.com/crowdsecurity/crowdsec
- https://github.com/eclipse/mosquitto
- https://github.com/excalidraw/excalidraw
- https://github.com/favonia/cloudflare-ddns
- https://github.com/garethgeorge/backrest
- https://github.com/glanceapp/glance
- https://github.com/goauthentik/authentik
- https://github.com/grafana/grafana

## 导航

- 项目页：[[10-项目/codeberg.org_6f36b9fc]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
