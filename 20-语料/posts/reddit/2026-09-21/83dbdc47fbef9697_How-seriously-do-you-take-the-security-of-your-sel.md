---
type: "corpus"
item_id: "83dbdc47fbef9697"
title: "How seriously do you take the security of your self-hosted apps?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w3bu10/how_seriously_do_you_take_the_security_of_your/"
project_url: "https://afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global"
author: "Familiar-Ability6383"
published_at: "2026-08-31T20:06:28+08:00"
captured_at: "2026-09-21T03:04:16+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 706, "comments": 163, "upvote_ratio": 0.97}
comments_count: 169
comments_total: 169
discovered_via: "reddit:52d+settle3"
---

# How seriously do you take the security of your self-hosted apps?

> [!info] 一句话导读
> source: [https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global](https://www.afp.gov.au/news-centr…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1w3bu10/how_seriously_do_you_take_the_security_of_your/>
> 指标：得分=706 · 评论=163 · 赞踩比=0.97
> 作者：Familiar-Ability6383　|　发布：2026-08-31T20:06:28+08:00
> 项目链接：<https://afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global>
> 采集：2026-09-21T03:04:16+08:00　|　id：`83dbdc47fbef9697`

## 正文

source: [https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global](https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global)

Most self-hosting security advice is just about the basics - don't expose ports directly to the internet and use containers for basic isolation

Beyond that what level of security do you actually enforce? Do you monitor what your apps are doing in the background, like tracking outbound network traffic or checking file access on the host? When updating, do you just let it auto-pull or read the release notes for breaking changes or inspect source code and dependencies before updating?

## 评论（169/169）

> **asimovs-auditor**（1 分） · 2026-08-31T20:06:40+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Familiar-Ability6383**（36 分） · 2026-08-31T20:07:59+08:00　
> AI is not used in the creation of this post

---

> **ProfessionalDish**（114 分） · 2026-08-31T20:12:13+08:00　
> always read the release notes; someone made the effort to write them thus I can invest a few minutes to read them. Also gives you enough warning if they change naming like blocklist/blacklist.
>
> If the app doesn't needs internet access it won't have internet access.

---

> **Brian-Puccio**（-6 分） · 2026-08-31T20:12:33+08:00　
> What libraries did they publish that people used?

---

> **TCB13sQuotes**（-4 分） · 2026-08-31T20:13:52+08:00　
> This is why I only host simple stuff like Filebrowser and Syncthing and not Nextcloud. Also the same reason why I install stuff myself / don't use rancom containers/compose files.
>
> You can never audit the entire code base of NC for example and you can't keep up with all the updates. Better run simpler things you can understand with the time you've.

---

> **AnderssonPeter**（20 分） · 2026-08-31T20:14:22+08:00　
> Just curious, how do you host your apps and how do you block them from getting internet access?

---

> **nightcrawler2164**（38 分） · 2026-08-31T20:15:00+08:00　
> Firewall rules on your gateway/router

---

> **ProfessionalDish**（3 分） · 2026-08-31T20:15:30+08:00　
> Mostly docker.

---

> **MrHaxx1**（10 分） · 2026-08-31T20:17:41+08:00　
> Have audited the code base of Filebrowser and Syncthing?
>
> And are you auditing the diffs for every update?

---

> **AnderssonPeter**（9 分） · 2026-08-31T20:17:53+08:00　
> So each app has its own ip?

---

> **nononoko**（54 分） · 2026-08-31T20:18:21+08:00　
> DMZ for external services. Network segregation. Firewall rules both at the network level and on the hosts. VM's for hosting anything and everything in containers, nothing on the bare metal host.

---

> **Medium_Chemist_4032**（28 分） · 2026-08-31T20:19:23+08:00　
> I take it very moderately serious.
>
> To the extent, I had to remove a gitea cpu miner from one VM. Supposedly the exploit is less than 2 weeks old

---

> **Icy-Foundation-7878**（8 分） · 2026-08-31T20:20:50+08:00　
> To be honest, not as seriously as I should. My main thing is that I’m not a valuable enough target ya know.

---

> **TCB13sQuotes**（5 分） · 2026-08-31T20:20:59+08:00　
> Filebrowser, yes, I even have my own version with a few tweaks / integration with specific low level functions of my NAS. Syncthing from time to time.
>
> Even if you don't the code, the bare minimum is to understand what it install and how it installs with - what's the configuration etc. Most people are running generic containers with configurations that they don't need just because it was easier.

---

> **RealMiten**（27 分） · 2026-08-31T20:21:55+08:00　
> Private IP, yes.

---

> **dontgetaddicted**（0 分） · 2026-08-31T20:22:01+08:00　
> Same. Security via being effectively useless and poor.

---

> **nightcrawler2164**（25 分） · 2026-08-31T20:22:40+08:00　
> Here’s my setup - I have my home lab services on their own VLAN. Anything and everything on that VLAN is by default blocked from WAN. Any service that needs external connectivity does so through a reverse proxy that’s hosted on a separate DMZ VLAN. This reverse proxy can’t directly initiate connections to the home lab VLAN but can receive and process requests.
>
> All my apt updates on the network are also done locally though a cache mirror I have on the DMZ. 95% of The home lab services I host don’t talk to the internet, period. Even the ones that do, it’s through SSL and behind a reverse proxy/2FA.

---

> **76zzz29**（4 分） · 2026-08-31T20:23:08+08:00　
> If set up properly, yes. May it be because of actualy be a diferent hardware of because they are separated on diferent network machine on the software level (exemples: Virtual Machine, Docker, sandbox,...).

---

> **These-Apple8817**（419 分） · 2026-08-31T20:24:36+08:00　
> Would have been nice if t hey had actually mentioned what was compromised

---

> **Mission_Rice3045**（1 分） · 2026-08-31T20:25:32+08:00　
> You own them.

---

> **joshguy1425**（93 分） · 2026-08-31T20:27:20+08:00　
> This is why I invested heavily in a segmented network and each service goes in its own LXC container or VM with limited network access.
>
> - Every service goes in its own LXC container or VM
> - Secrets are encrypted with a container-specific key
> - All containers/VMs have default drop policies for network traffic
> - All allowed traffic is tightly scoped
> - All database users are tightly scoped and use service-specific creds
> - The network is broken into multiple
> VLANs with riskier services isolated from critical core infrastructure
> - All services ship logs to a centralized logging server
>
> Container escape is still possible in theory, but the goal is to minimize the possible damage if something malicious gets in or tries to break out, and to ensure something malicious can’t completely hide all evidence.

---

> **nonlinear_nyc**（11 分） · 2026-08-31T20:28:11+08:00　
> I can only imagine how compromised are closed source apps

---

> **therealmrbob**（49 分） · 2026-08-31T20:29:52+08:00　
> Reading release notes doesn’t tell you if someone hides malicious code in the app. lol

---

> **-Django**（216 分） · 2026-08-31T20:31:12+08:00　
> Trivy, checkmarx, litellm, and some more since it involved npm credential theft. I found a decent list here: [https://corgea.com/research/teampcp-fbi-flash-trivy-kics-litellm-telnyx-july-2026](https://corgea.com/research/teampcp-fbi-flash-trivy-kics-litellm-telnyx-july-2026) but you can also search "TeamPCP CanisterWorm" for more info about the attack

---

> **ProfessionalDish**（25 分） · 2026-08-31T20:31:40+08:00　
> I know we're on reddit and we generally can't read, but it's still a question OP asked.

---

> **mdskllz420**（-10 分） · 2026-08-31T20:31:47+08:00　
> что
>
> как вы вообще это обнаружили?

---

> **therealmrbob**（10 分） · 2026-08-31T20:32:29+08:00　
> Hahaha my bad, totally just read the headline then went to the comments. My bad.

---

> **clintkev251**（3 分） · 2026-08-31T20:32:50+08:00　
> I think I take it pretty seriously. Every container running as non-root, having isolated volumes and no broad access to the host or data from other containers, network policies scope the traffic they're allowed to send to the bare minimum (which would likely block something like this), and releases pinned to digests and managed manually so I at least have the opportunity to catch a weird update.

---

> **computermaster704**（3 分） · 2026-08-31T20:33:16+08:00　
> Since the hack hit a open source dependency and infected it unless you're auditing all updates it could hit you since that's the new target with open source malware because if you can hit the right dependency you basically just hacked half the planet

---

> **ProfessionalDish**（9 分） · 2026-08-31T20:34:26+08:00　
> all fine, I can't deny that it happened to me too lol.

---

> **These-Apple8817**（23 分） · 2026-08-31T20:39:10+08:00　
> Thanks. Never heard any of those tbh although the list is probably far longer than that

---

> **ChubbyWabbit**（8 分） · 2026-08-31T20:40:12+08:00　
> Security can be a double edged sword when self hosting. As yes, I want to have the absolute security when it comes to things I host on my home servers, but the issue lies in the diminishing returns. It is a lot of headache to implement and can break a lot of stuff depending on how you do it. Like FIPS 140-3, & STIG hardening are things I would deem unnecessary unless your home security posture requires it.
>
> I have a bare minimum standard I implement on all of my hosts & containers:
>
> * Set up root w/ password + first admin user. Secure root password in safe for emergencies.
> * Basic hardening such as ensuring unneeded services are not running. Easiest way of doing this is installing a minimal server install instead of the full server & add things as needed.
> * Installing Fail2Ban & ClamAV on each host. Protects against brute force attacks & clamav can do scheduled scans and on-demand scanning.
> * Using podman instead of docker, as podman is daemonless & can be run rootless. It is a little extra work to get everything running smooth, but it is well worth it.
> * Keeping all hosts & services on a separate VLAN from user vlans. Also implement host & vlan firewalls.
> * Stand up a Wazah server & connect endpoints | Optional, depending if you want to monitor everything.
> * Always test new applications in an isolated environment before bringing it into the production space. Read release notes, etc.
>
> There is even more security layers I want to implement, but it just adds more stuff to manage.

---

> **Medium_Chemist_4032**（13 分） · 2026-08-31T20:40:22+08:00　
> I walk by that host every day and recently noticed... "Is it overheating?"
>
> `$ top` *scratches head*, hmmm... `codex`... `/permisions`  \-> "Full Access" and `Can you investigate the process, which is eating the whole cpu, the funny named one?`

---

> **Dangerous-Report8517**（13 分） · 2026-08-31T20:40:43+08:00　
> Sure but the fact that OP posted the article pretty strongly implies that malicious code is a big part of their threat model (which would include supply chain attacks in addition to malicious devs), while developers weakening their own security openly is probably not

---

> **quiteCryptic**（22 分） · 2026-08-31T20:42:01+08:00　
> I know some people don't want to hear it but this is another nice task for AI
>
> Before you run something, clone the repo and have AI check it for anything that seems obviously malicious or any kind of external communication it might try to do
>
> Maybe not for widely used things like sonarr, but for less common services at least
>
> edit to add: technically you should build your own container from source as well, but it starts to get into the too big of a hassle to do all this category. Hmm, it could be a use case for making an AI skill for pulling updates, checking change logs for breaking changes, rebuilding the container, and then deploying it.

---

> **Dangerous-Report8517**（5 分） · 2026-08-31T20:43:02+08:00　
> Not very useful when the example given is supply side compromise, which doesn't discriminate by target value

---

> **dontgetaddicted**（3 分） · 2026-08-31T20:46:57+08:00　
> Yeah, I really meant it in jest.

---

> **JohnHue**（1 分） · 2026-08-31T20:48:29+08:00　
> Ideally, unprivileged containers in proxmox, proper password/crediential management, split networks.
>
> In reality, I'm not taking it seriously enough and I do have unprivileged containers and my network infrastructure leaves a lot to be desired.

---

> **Personal-Time-9993**（1 分） · 2026-08-31T20:49:00+08:00　
> No, each app has its own port(s) which you can create rules for.  The IP remains the same between different apps generally.  Exceptions could be vpn tunnels for example, which is something you would have set up intentionally.

---

> **bedroompurgatory**（2 分） · 2026-08-31T20:55:33+08:00　
> It does if they were kind enough to hack the release notes too, just to be all neighbourly

---

> **Feriman22**（1 分） · 2026-08-31T20:56:49+08:00　
> I take care of security so serious.
>
> Always updated system and packages. Using non-usual ports. Use random generated usernames and 50 character long passwords. SSH login only with key auth. Root ssh login disabled. Docker containers have minimum rights. Monitoring everything and alerting immedietly if something strange happened. Fail2ban activated.

---

> **IsolatedNetworkNode**（2 分） · 2026-08-31T20:59:50+08:00　
> I prefer open source applications that have end to end encryption feature even though it is my server and my hardware.
>
> In the event one application is compromised and they gain RCE on my server, presumably my data from my other apps would be safe since the keys were never on the server.

---

> **Dnomyar96**（20 分） · 2026-08-31T21:02:59+08:00　
> I do the basics, but don't bother beyond that. There's nothing really valuable on my server. The only thing I paid a bit more attention to is NextCloud, since that has my photos and other files. But if somebody gains acces to my JellyFin or AudioBookshelf, I really don't care.

---

> **Glebun**（6 分） · 2026-08-31T21:07:30+08:00　
> ports are for incoming connections. doesn't affect internet access

---

> **-ThreeHeadedMonkey-**（0 分） · 2026-08-31T21:08:36+08:00　
> I dont check code but I isolate as well as I can. I.e proxmox, most apps in it's own vlan and its own VM etc. And a shitton of unifi firewall rules.
>
> I'm not quite there yet but it's working well for me so far.

---

> **Personal-Time-9993**（1 分） · 2026-08-31T21:09:02+08:00　
> True, I was focused on the “how do you host your apps” part.  It was really a two part question that I neglected half of.  My bad.

---

> **pqu**（13 分） · 2026-08-31T21:09:23+08:00　
> I’ve discovered most of my performance bugs by hearing the fans spin on one of the nodes, even with all my metrics and alerting

---

> **Familiar-Ability6383**（2 分） · 2026-08-31T21:10:23+08:00　
> Maybe I'm just paranoid, but monetary loss is only one part of the issue. What if criminals and extremist organizations get access to personal and sensitive info? They could blackmail or impersonate the victims

---

> **MasterChiefmas**（2 分） · 2026-08-31T21:12:51+08:00　
> > Beyond that what level of security do you actually enforce?
>
> Mainly, monitoring activity of the apps for suspicious behavior. Pay some attention to subreddits/githubs/tech news for alerts about anything you deploy. AI could be helpful for that.
>
> Supply chain attacks like that are difficult for the individual to detect. You have to become like a bank and vet every app, and you'd have to review the code for them all once, and then review diffs from then on yourself, before ever deploying an update.
>
> At some point, you will likely have to trust _someone_ else is doing, or has done that work. IMO, a supply chain attack is insurmountable for the individual to really protect against. The scale is just too large when you consider all of the parts involved for even simple deployments yourself, assuming you even have the programming background to be able to audit code.

---

> **Run-OpenBSD**（0 分） · 2026-08-31T21:13:18+08:00　
> I would trust a junkie off the street more than I'd trust any microsoft product

---

> **Difficult896**（3 分） · 2026-08-31T21:13:44+08:00　
> What models do you use? Are cheap models sufficient in your experience?

---

> **Hefty_Acanthaceae348**（1 分） · 2026-08-31T21:18:27+08:00　
> I'd say I take it quite seriously, but my homelab isn't all that secure yet. I have sso and such, and iac which would allow me to easily wipe everything and rebuild, but I still have a flat network, haven't implemented mtls handshakes accross servers. At the moment I'm tweaking things to make arp spoofing either impossible or useless, but there are so many threat models.
>
> It just takes time.

---

> **cybekRT**（-1 分） · 2026-08-31T21:19:31+08:00　
> Are they really telling the truth about adding the "inclusive" language? I thought that they are usually hiding it under unrelated changes or misleading phrases.

---

> **Bonsailinse**（42 分） · 2026-08-31T21:24:05+08:00　
> I take the security of my infrastructure very seriously, but if they hit me with a supply-chain-attack I’m pretty much screwed.

---

> **ProfessionalDish**（1 分） · 2026-08-31T21:24:46+08:00　
> Didn't had a single instance where it was hidden or sneaky, always announced like any other change in naming conventions. Maybe your bubble is a bit biased towards the right, but politics shouldn't be the focus on this sub.

---

> **StabilityFetish**（1 分） · 2026-08-31T21:28:28+08:00　
> I have several container hosts, based on rootful/rootless and internet vs local only, vs no outbound. That lets you block the entire VM's IP from the internet. You'll still have to proxy OS and container updates though

---

> **Aevaris_**（2 分） · 2026-08-31T21:30:27+08:00　
> I'd say moderately. All apps running in docker containers. The host they run on has only read only access to my broader network. It has a workstation specific password and service account specific to it. It only has access to files it needs to (such as my media). Block SSH and RDP.
>
> From an external perspective, im a little lax. I don't firewall in or out traffic (I might one day when I have some time to build a proper firewall). HTTP proxy so I only open port 443 inbound. Cloudflare proxy what I can. I do not use an inbound VPN because the pros vs cons don't weigh out for me.

---

> **elh0mbre**（2 分） · 2026-08-31T21:30:58+08:00　
> Do you read the source code of every app you install to make sure its not doing what these guys were doing?

---

> **Feriman22**（1 分） · 2026-08-31T21:37:53+08:00　
> What?

---

> **eternalityLP**（2 分） · 2026-08-31T21:38:58+08:00　
> I don't monitor, but I make sure everything is isolated and every app only has access to the stuff they actually need to run.

---

> **joshguy1425**（24 分） · 2026-08-31T21:40:00+08:00　
> The way I think about this isn’t just “do I care if they get my
>  Jellyfin data” but “would I care if a hacker could silently live on the system hosting Jellyfin and attempt to access other parts of my network?” or even more problematic “would I care if someone used my Jellyfin server as a proxy to route their illegal activities?”

---

> **joshguy1425**（10 分） · 2026-08-31T21:45:04+08:00　
> I think it’s worth rethinking how valuable you are.
>
> Most of us aren’t valuable enough to worry about something like a zero day RCE where the attacker is burning a valuable exploit to get get in.
>
> But supply chain attacks aren’t the same thing. They don’t discriminate based on target value, and once they’ve established a foothold in your network, they can now use you as a member of a botnet, as a proxy for illicit network traffic, etc.

---

> **DylanfromSales**（2 分） · 2026-08-31T21:51:22+08:00　
> The FBI was first on the scene because they had insider knowledge of the exact malicious code

---

> **retro_grave**（25 分） · 2026-08-31T22:01:46+08:00　
> Trivy is an interesting one. Do they report CWEs against themselves? Looks like the affected images were deleted (good), but AFAIK I hadn't seen anything from Trivy yet about it. Maybe I'm not on the right channels.
>
> **edit** Ah they had this sorted out back in March: https://github.com/aquasecurity/trivy/discussions/10462. Very interesting timeline!

---

> **ConTully**（4 分） · 2026-08-31T22:02:42+08:00　
> Only one that sounds familiar is Trivy which is built into a pretty popular docker management application called [Dockhand](https://github.com/Finsys/dockhand). I wonder what thay means for it's users.

---

> **userXinos**（2 分） · 2026-08-31T22:14:57+08:00　
> a separate vm on fedora coreOS for applications. In addition to the fact that it is an immutable system, there is also has selinux, which is not possible to do in lxc. Next: podman rootless - containers have isolated networks, and only one network has access to the Internet, resource limitation in the systemd units interface (native podman feature)

---

> **quiteCryptic**（3 分） · 2026-08-31T22:22:32+08:00　
> Honestly I just already pay for chatgpt for various uses, so I just use codex. Don't have the hardware to run any decent local models.

---

> **Mo_Dice**（13 分） · 2026-08-31T22:31:04+08:00　
> > since it involved npm credential theft
>
> The three categories of modern malicious code:
>
> * npm supply chain
> * AI fuckery
> * actually something else

---

> **_cdk**（-6 分） · 2026-08-31T22:39:32+08:00　
> ahh yes, i love me a false sense of security in place of actual security.

---

> **basheworking**（2 分） · 2026-08-31T22:41:06+08:00　
> It's ok if your phone, your computer, your tv, your watch, your glasses, your thermostat, your vacuum cleaner, your refrigerator, your stove, your washer and dryer collect personal info but we draw the line at open source software. -The FBI

---

> **ProfessionalDish**（11 分） · 2026-08-31T22:41:07+08:00　
> or even just "would I care if the data/service gets deleted?" and the answer is yes most of the time unfortunately.

---

> **noobtastic31373**（15 分） · 2026-08-31T23:02:35+08:00　
> That doesn't really address OPs question for monitoring or vetting the software in your VM/ container. Segmentation doesn't lower the likelihood of you deploying malicious code, just is ability to communicate.

---

> **FanClubof5**（11 分） · 2026-08-31T23:07:08+08:00　
> It was pulled down in less than 24 hours iirc and you had to have been running a scan with a hardcoded version number for the image. Its one of the reasons why sha pinning your docker containers is a great idea.

---

> **fmtheilig**（1 分） · 2026-08-31T23:09:17+08:00　
> My public facing VMs are DISA hardened to about 80%. They are also on a DMZ VLAN.

---

> **phlooo**（139 分） · 2026-08-31T23:10:43+08:00　
> It's always npm

---

> **FanClubof5**（13 分） · 2026-08-31T23:11:53+08:00　
> Supply chain attacks wont be impacted by anything you just said. This is one of the huge challenges with the interconnected web of open source dependencies out there. The best mitigation is to slow down updates so they are hopefully discovered before you download them but also not slow down updates enough that you are impacted by security issues.
>
> Defense in depth and layers of security are also important. A compromised docker container can do a lot less if you have a full security hardening setup, monitoring, and network security implemented.

---

> **NoDistrict1529**（1 分） · 2026-08-31T23:12:20+08:00　
> This is a huge reason I use random password everywhere, even internal.

---

> **LooseEthernet**（4 分） · 2026-08-31T23:15:00+08:00　
> i mostly just hope i'm not interesting enough to be a target lol. if the house burns down i'll just buy more hard drives

---

> **derprondo**（22 分） · 2026-08-31T23:16:46+08:00　
> These are tools very commonly used by enterprises in CI/CD pipelines, thus they're refereed to as supply chain attacks.

---

> **basicKitsch**（1 分） · 2026-08-31T23:17:10+08:00　
> vlan service isolation based on threat potential and needs (don't need my chinesey iot vacuum on my personal network. security cameras on their own, etc and defined egress routes for almost all of it.
>
> i don't worry about mTLS or encrypted traffic inside my personal vlan for ease of use by the family and i don't let things network out that absolutely should not.

---

> **ILikeBubblyWater**（9 分） · 2026-08-31T23:19:30+08:00　
> This thread will be biased because people that are paranoid and knowledgeable will be upvotes and are happy to participate. Those who run default install scripts and yolo shit will not. I bet most people do not care about supply chain attacks or even know what they are

---

> **quiteCryptic**（2 分） · 2026-08-31T23:20:39+08:00　
> Yep that's a fair point, perhaps they could at least be checked to see if they are commonly used dependencies and not something niche. Won't save you, even popular stuff could have compromises but its at least likely not something malicious made by the owner of the app

---

> **ILikeBubblyWater**（1 分） · 2026-08-31T23:20:41+08:00　
> How do you read release notes of an obscure 4th level down npm package that has been injected with malicious code.
>
> Reading release notes does jack shit against supply chain attacks

---

> **ILikeBubblyWater**（1 分） · 2026-08-31T23:23:11+08:00　
> 20 bucks in codex gets you pretty far

---

> **Glebun**（0 分） · 2026-08-31T23:27:26+08:00　
> Not sure what you mean - HTTPS is 443.

---

> **cardboard-kansio**（9 分） · 2026-08-31T23:33:07+08:00　
> On the DMZ level, YOLO.
>
> On the VLAN level, YOLO.
>
> In the host level, the onion principle (host, VM, docker, drop caps, etc). Harden where possible.
>
> On the individual level, auto-update for non-critical containers. Update my own projects as and when. Update critical infra quarterly (manually) - this means reverse proxy, auth layer, VPN etc, avoiding zero-day vulns which there have been too many of recently.
>
> Everything else, YOLO. I mean, if I'm self-hosting then it's a hobby, not a job. Worst case scenario I'm pulling the (physical) plug and reinstalling everything from scratch.

---

> **Youknowimtheman**（7 分） · 2026-08-31T23:35:01+08:00　
> Trivy and Checkmarx are widely used security tools. LiteLLM is everywhere for AI under the hood.
>
> The reason it hit so many projects was because popping these projects that hundreds of thousands of projects indirectly rely on has an enormous blast radius. That's the sinister part of supply chain attacks. That one project with a solo maintainer can get attacked and hit millions of devices.

---

> **TonyBlairsDildo**（5 分） · 2026-08-31T23:57:22+08:00　
> Would you care if your home NAS was hijacked and used to host CSAM?

---

> **meowmixmotherfucker**（1 分） · 2026-09-01T00:00:52+08:00　
> I mean, as seriously as I can.
>
> I check repos for weird activity (to the extent it’s possible for one person…), try to use apps with good reputations, read up as best I can before implanting, and subscribe to various security warning services to get notified of issues…
>
> I don’t know that there is a silver bullet for this, it’s kind of part of the work/risk of self hosting. Little things are hopefully easily caught but major stuff like Log4J… that got industry leaders globally, companies and agencies with dedicated security teams - we can’t really compete with that.
>
> It sucks but it’s part of the game. Keep your scanners, definitions, and logging up to date and act on critical notifications quickly. Wherever possible, encrypt the hell out of your data just in case…

---

> **ParkingPsychology**（-2 分） · 2026-09-01T00:12:55+08:00　
> >When updating, do you just let it auto-pull or read the release notes for breaking changes or inspect source code and dependencies before updating?
>
> Before installing I get an AI to do a security review and I pick the product that's most maintained and has the highest security profile.
>
> I pin to versions, not "latest" and then once a week or once per two weeks, I get an AI to run a check on new version releases and do a security review on the changes before updating.
>
> I have my environment documented with runbooks and configs, all pushed to private git as well, where the instructions are on what level of security is needed per application tier, that's all also AI generated.
>
> You can get quite far and secure in a few days with a $20 a month AI subscription.

---

> **theRealBassist**（3 分） · 2026-09-01T00:19:34+08:00　
> Doing the cache mirror is something I'd like to get around to eventually. My goal would also be to mirror docker containers locally, but we'll see how much I get to lol

---

> **djpiperson**（1 分） · 2026-09-01T00:32:54+08:00　
> At this point it almost seems wise to use an AI to audit FOSS for you.

---

> **surftrend**（1 分） · 2026-09-01T00:38:52+08:00　
> Internet-facing gets MFA, updates, backups, and logs. LAN-only gets convenience, but still no default passwords.

---

> **lqstuart**（1 分） · 2026-09-01T00:43:37+08:00　
> The above is referring to TeamPCP. They harvested those credentials through GHA. Risky Business has some good coverage on it. Moral of the story is pin your GHA modules through SHA hash, not version. Kind of orthogonal to self-hosting, but the general advice stays the same--rotate credentials, keep stuff up to date, and just show even mild interest in not getting your shit hacked, and you'll be fine. Credential harvesting is a crime of opportunity.

---

> **Digital_Voodoo**（1 分） · 2026-09-01T00:51:00+08:00　
> Disabled Trivy for security scan in Dockhand since the March incident, and haven't re-enabled it since. Grype only for now.

---

> **Nerrawnam**（1 分） · 2026-09-01T01:40:31+08:00　
> I use Arch BTW! 🙄

---

> **_EveryDay**（65 分） · 2026-09-01T02:38:29+08:00　
> Sometimes I use a different password for a container ¯\\\_(ツ)\_/¯

---

> **CoolUsername396**（23 分） · 2026-09-01T02:53:49+08:00　
> Passw0rd

---

> **Aus_pugs**（1 分） · 2026-09-01T02:55:49+08:00　
> Here is a better question, How seriously do you take the security of your cloud hosted apps.
>
> In my experience, people who self host, review logs, and failed login attempts more often, in the cloud, you often can not even see the logs, or if you can, IT staff often dont review, as they are out of side out of mind.  I recently moved a number of my domains from a "Hosted provider" inhouse, and after reviewing the logs, I noted a number of ips that have been brute forcing email logins.  The old provider did not give me access to mail failed login logs, and they clearly did not take any action when there was failed logins.  Since the move, and implementing bans for failed logins with fail2ban, the number of brute force attempts has decreased considerable. I assume the script kiddies have moved on to other "low hanging fruit" and put my domains in the too hard basket.

---

> **ColoradoPhotog**（11 分） · 2026-09-01T02:59:19+08:00　
> And therein lies why supply-chain is what so many threat actors are targeting. In a lot of instances, by the time its detected, it has existed in environments long enough to do plenty of damage. We're living in unique times, and we grapple with this in Enterprise Sec a lot.
>
> I hear people make recommendations to stay "x versions behind" upstream, as well as other supposed mitigations. I guess that works if the exploit is exceptionally recent, but we've seen some instances where supply-chain was poisoned for months or more at a time.  Wild.

---

> **Aus_pugs**（0 分） · 2026-09-01T03:00:26+08:00　
> I am pretty sure this is linked to  TeamPCP

---

> **fuckingredditman**（1 分） · 2026-09-01T03:14:39+08:00　
> you could go a step further and not use any prebuilt binaries and have an LLM run a git diff and then build form source and check all dependencies on each update, but that's way beyond any selfhosting usecase i would say. just mentioning it because IMO it would be possible. that way you could go pretty deep.

---

> **buzzbuzz17**（1 分） · 2026-09-01T03:15:25+08:00　
> More seriously than some, not nearly as seriously as I should

---

> **scriptmonkey420**（59 分） · 2026-09-01T03:41:44+08:00　
> Has been for the past 17 years. They never really seem to bother to fix the glaringly bad issues their platform has.

---

> **gurgle528**（2 分） · 2026-09-01T03:42:02+08:00　
> The sad thing is even in that situation your network is still valuable. Companies (free VPNs are notorious for this) and criminals alike can use it to run bots through your residential IP address to try and get around bot checks. Over time this can lead to your legitimate traffic being flagged

---

> **PassiveLemon**（5 分） · 2026-09-01T03:46:06+08:00　
> I have personal interests in cybersecurity so of course I try to harden what I can. I’ll try to give a general overview of my setup.
> Networking:
> \- I have a .com and a .net. The .net is basically just my own namespace for networking and the .com is for public stuff.
> \- This is split into 3 levels, private (local only), tailscale (local + tailscale), and public. Each level uses IP range whitelists.
> \- Containers are behind Traefik RP and are only accessible over HTTPS. HTTP is always upgraded to HTTPS.
> \- Services exposed over a subdomain are certified by wildcard so my subdomains can’t easily be found.
> \- Containers default to the private level, I have to specifically choose to use the tailscale or public level.
> \- Containers have no access to other containers by default. If they need networking to another, it’s done through an encrypted bridge network shared between only those containers. This helps prevent one container from hijacking another.
>
> Containers:
> \- All of my images are pinned and hashed, I update them with Renovate every so often, they do not automatically update.
> \- I subscribe to GitHub release notifications for the services I use to keep up with changes and note down anything that may cause breakages in the future. This is kind of fatiguing though because some repositories love to push multiple releases a day. Renovate can show the changelog history so I may stop watching releases.
> \- All containers have resource limits and user/group permissions if possible. I would give rootless Docker a try but some things just don’t play nicely with it.
> \- Anything that needs the Docker socket will use a socket proxy with minimal capabilities.
> \- I generally try to avoid anything relatively obscure or heavily vibe-coded.
>
> Repository:
> \- Secrets are never hardcoded (unless there is absolutely no other way), they are stored and imported from an encrypted .env file.
> \- My entire stack (compose files, secrets, configs) is tracked in git and secrets are encrypted with Age. Secrets include stuff like API keys, usernames/passwords, domains, etc. I use this repository on two machines so keeping the secrets encrypted in one place is very convenient.
>
> There are some more minor things that I don’t feel like including, what I mentioned is probably 99% of the work I put into security.
>
> There’s also split-horizon DNS, auto-renewing certificates, deployment scripts, and documentation. Various things that make stuff easier.
>
> Of course, it’s a bit overkill at the moment because I am the only user and nothing is currently exposed publicly but why not. I still have some things I’ve considered, like Fail2Ban/Crowdsec, Authentik, and Headscale

---

> **AbooMinister**（3 分） · 2026-09-01T03:46:13+08:00　
> what should they do?

---

> **Same-Imagination4712**（83 分） · 2026-09-01T04:30:05+08:00　
> **‘No way to prevent this,’ says only package manager where this regularly happens.**

---

> **d03j**（7 分） · 2026-09-01T04:36:59+08:00　
> https://breachnews.com/threat-actors/teampcp/
>
> August 2026: Australian authorities arrest and charge 2 alleged TeamPCP participants following a joint AFP, FBI and Western Australia Police investigation into global software supply chain attacks
>
> August 2026: CloudSEK reports that the TeamPCP-linked LiteLLM supply chain attack may have impacted more than 2,500 organizations through compromised developer environments
>
> July 2026: FBI issues a FLASH advisory detailing TeamPCP malware, software supply chain attacks, extortion activity, and defensive guidance for organizations
>
> May 2026: Allegedly lists GitHub internal source code and approximately 4,000 private repositories for sale
>
> May 2026: OpenAI confirms an internal breach linked to the Mini Shai-Hulud supply chain campaign
>
> May 2026: Claims sale of Mistral AI repositories and internal source code
>
> May 2026: Lightning AI repositories allegedly leaked following the PyTorch Lightning compromise
>
> April 2026: Bitwarden CLI compromised through a software supply chain attack
>
> April 2026: European Commission breach publicly linked to TeamPCP activity
>
> April 2026: Mercor compromised in a supply chain campaign targeting AI infrastructure
>
> March 2026: Trivy, Checkmarx KICS, LiteLLM, and the Telnyx Python SDK compromised in large-scale software supply chain attacks
>
> https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global

---

> **Subsector3990**（0 分） · 2026-09-01T04:37:49+08:00　
> congrats, you've now piped the malware and prompt injection surface directly into your AI agent who has the ability to fuck up your machine even more

---

> **joemckie**（19 分） · 2026-09-01T04:49:02+08:00　
> “Passw1rd”

---

> **d03j**（-1 分） · 2026-09-01T04:56:06+08:00　
> >I hear people make recommendations to stay "x versions behind" upstream, as well as other supposed mitigations
>
> I never heard a security professional recommend anything other than always patch. Staying behind might protect you against a potential 0 day,while guaranteeing you're vulnerable to anything identified, documented and patched. Generally speaking the further back you stay, the longer the list o exploits to be used against you.

---

> **d03j**（1 分） · 2026-09-01T05:00:09+08:00　
> Can you help me understand how auditing open source code, no matter how unrealistic, won't help mitigate supply chain attacks?

---

> **d03j**（1 分） · 2026-09-01T05:01:35+08:00　
> FYI - I believe one of the systems compromised by these guys was a selfhosted LLM :)

---

> **d03j**（1 分） · 2026-09-01T05:05:29+08:00　
> I assumed they meant auditing the code and all its dependencies.

---

> **codeedog**（2 分） · 2026-09-01T05:06:49+08:00　
> This is mostly what I do, but with FreeBSD jails.

---

> **d03j**（1 分） · 2026-09-01T05:10:28+08:00　
> Or use your equipment to further their means and one day you find your homelab confiscated and yourself in a basement somewhere trying to explain how you had nothing to do with X attack, running an exit node to something, part of C&C network, whatever :)

---

> **h3r4ld**（2 分） · 2026-09-01T05:14:58+08:00　
> That, and honestly adding inclusive language *really* shouldn't be seen as a major change in need of reporting - more like fixing a typo.

---

> **d03j**（1 分） · 2026-09-01T05:15:16+08:00　
> >Every container running as non-root, having isolated volumes and no broad access to the host or data from other containers, network policies scope the traffic they're allowed to send to the bare minimum (which would likely block something like this)
>
> are you using podman? If so, how are managing the network policies. I do everything else but have yet to look at hardening my containers' networks, e.g. disabling outbound connections.

---

> **clintkev251**（1 分） · 2026-09-01T05:20:57+08:00　
> I'm using Kubernetes

---

> **Spawny2**（1 分） · 2026-09-01T05:37:50+08:00　
> I make choices that limit my needs to take it seriously.
>
> I'll lock down egress (and ingress) to only what's necessary.
> I don't really expose anything to internet unless it's absolutely necessary, and anything I expose, I make sure I'm only exposing exactly what's necessary and not a path more.
>
> VMs and various isolations that exist.
> The same goes for creds: An app only gets precisely which creds are necessary to run, and those creds are often issued specific for the app.
>
> Writing this out, I know it may sound like a lot on paper, but when it's a normalized process in your head, it's not that much. (There are so many more things one can do) I've structured my self-hosting stuff such that the default state is nothing, and I add things as needed. This makes it so I minimize what things I need to take seriously vs trusting that nobody is going to commit something malicious to every open source project I take on.

---

> **Spawny2**（1 分） · 2026-09-01T05:45:49+08:00　
> I guess, to add, I do have logs for all of this (ingress, egress, per app, per container, etc) and I do audit them from time to time, I also have a notification system for when certain projects have a new release.
> ... but I don't rely on that.
>
> Active (even automated) monitoring turns it into a full-time job and I DONT want to take my work home with me.
>
> If there is a decision I have to make and the decision means keeping things secure will require me to keep on top of everything, I decide that it's not worth it.
>
> Ex: Apps that require Internet access to pull a file down from some arbitray endpoint for the UI or something get a dummy endpoint, or they don't get used because they just aren't worth it.

---

> **pastelfemby**（1 分） · 2026-09-01T05:49:44+08:00　
> Reminder gvisor/runsc and kata containers exist, and are a great way to further isolate containerized workloads in k8s, podman and docker in a fairly plug and play manner.
>
> And yes, gvisor does worth with nvidia gpus.

---

> **Glittering_Client36**（1 分） · 2026-09-01T05:52:18+08:00　
> Two approaches:
> - Use complex apps and isolate everything: subnets, strict firewall rules, unique credential sets, VMs and containers.
> - Use dead simple apps with as tiny codebase as possible and reduce your attack surface. Less external dependencies you have => less possibilities for supply chain attacks; as a bonus, you can realistically audit source code before hosting the project (try doing that with nextcloud or other bloatware).

---

> **Glittering_Client36**（1 分） · 2026-09-01T05:58:59+08:00　
> A counterargument would be RedHat porting relevant security patches to frozen old software versions. Less behavior changes = less probability for new vulnerabilities.
>
> Unfortunately, it's reserved for large corporations who can pay for a team doing it full time.

---

> **Glittering_Client36**（2 分） · 2026-09-01T06:04:07+08:00　
> You'd have to audit every single update of every single dependency, including ones written in languages with manual memory management. Memory bugs can be deceptively hard to spot.

---

> **nononoko**（1 分） · 2026-09-01T06:10:21+08:00　
> I disagree. He asked beyond _ don't expose ports directly to the internet and use containers for basic isolation_ what else do you do.
>
> >Beyond that what level of security do you actually enforce? Do you monitor what your apps are doing in the background, like tracking outbound network traffic (...)
>
> And while the latter part of the question was about vetting the software etc, the former (what I quoted) was very much about networking. And no obviously segmentation does not lower the likelihood of deploying malicious code captain obvious. That's not the point. It limits the blast radius. With the amount of deps in modern code other than vuln scanning images and try to obtain SBOMs there is not much more you can do than monitor and limit access.

---

> **EncryptedPlays**（14 分） · 2026-09-01T06:33:54+08:00　
> i like this rendition of the statement lol

---

> **d03j**（1 分） · 2026-09-01T07:04:26+08:00　
> counterargument or agreement? if an "end of life" software is still receiving security updates, you're still patching. :)

---

> **d03j**（1 分） · 2026-09-01T07:09:57+08:00　
> I agree, unless you have good reason to trust all dependencies, if you're not auditing everything, you can't really trust it.
>
> I just assumed if you are going to ask an LLM to audit some piece of code, you'd make it look at everything.

---

> **Glittering_Client36**（0 分） · 2026-09-01T07:13:28+08:00　
> Yes but the point was that updating to a newer software versions usually introduces new security bugs, as they aren't entirely separated from security fixes.

---

> **lue3099**（4 分） · 2026-09-01T07:48:37+08:00　
> Literally what other packages managers and repo maintainers do.

---

> **ThunderDaniel**（2 分） · 2026-09-01T08:47:59+08:00　
> Definitely am one of those in the quiet "eh" majority/minority
>
> I don't expose any ports on my router, I keep my containers up to date, and I YOLO the rest of my shit. I only run the basic-ass Jellyfin/Arr/Whatever run-of-the-mill stuff that most everyone else does, and I learn along the way and hope that the smarty pants in this subreddit can give more wisdow beyond the normie level self-hosting knowledge I have

---

> **felix1429**（0 分） · 2026-09-01T09:13:33+08:00　
> Who said it always has to be?

---

> **AbooMinister**（4 分） · 2026-09-01T09:13:53+08:00　
> what do they do? supply chain security is not an npm exclusive issue.

---

> **lue3099**（0 分） · 2026-09-01T09:17:11+08:00　
> The volume of supply chain attacks is a npm issue. Whilst others have their moments, it not to the level of npm.

---

> **AbooMinister**（1 分） · 2026-09-01T09:17:34+08:00　
> how do we stop volume?

---

> **AbooMinister**（1 分） · 2026-09-01T09:19:50+08:00　
> for what it's worth there's quite a bit of supply chain attacks in other packaging ecosystems as well (PyPI, for example). any packaging ecosystem with that significant of a user base is prone to it, and it's a difficult problem to solve.

---

> **lue3099**（-3 分） · 2026-09-01T09:22:20+08:00　
> Dude are you obtuse.
> Look at the rules say that debian or fedora require.
>
> You need to be verified maintainer to be able to upload.
>
> Npm pypi etc all have very lax rules.
>
> Another example is arch aur, vs arch Pacman repos.

---

> **lue3099**（-1 分） · 2026-09-01T09:23:41+08:00　
> Pypi sure. But literally any other packaging medium handles this better.

---

> **AbooMinister**（5 分） · 2026-09-01T09:29:41+08:00　
> we can have a respectful discussion like adults, can't we?
>
> the issue here is a fundamental difference in both scale and philosophy. The package repositories for Debian are much *much* smaller than what exists for PyPI or NPM, and packages are manually reviewed/vetted by the maintainers. This isn't feasible for programming language package registries because there isn't enough manpower to vet the sheer degree of packages that go in, and it's not a "walled garden" philosophy--it's self service. Also, for programming languages, you can have packages update several times within a day, and a project can contain thousands of deeply nested dependencies, which makes manual verification pretty much impossible. repositories for operating systems just don't work that way, so it's much easier to manually verify them.

---

> **AbooMinister**（5 分） · 2026-09-01T09:32:07+08:00　
> It's also worth noting that operating system packages have centralized maintainer. most language ecosystems don't, because you aren't publishing a package to be integrated into a language, you're just releasing it for the world to use. For operating systems, when a package is accepted into a repository, it becomes "part" of that operating system and the maintainers become responsible for vetting it. If there was this degree of friction for programming language packages, adoption would be slow and nearly impossible.

---

> **AbooMinister**（2 分） · 2026-09-01T09:32:45+08:00　
> not really. the difference here is between operating systems and programming languages, which are fundamentally different environments (the same problem exists for pretty much every single programming language package ecosystem)

---

> **AbooMinister**（1 分） · 2026-09-01T09:36:19+08:00　
> there *are* reasonable solutions for this (I think what nixpkgs do can be a good does, and perhaps enforcing packages be signed by the maintainer would be good), but none of those solutions are doing what "other packaging mediums do" (which from what I understand, you're just referring to operating system package registries)

---

> **parzival-space**（1 分） · 2026-09-01T09:47:47+08:00　
> Somewhat serious I guess. Apart from the obvious things like a correctly setup firewall and separate blank, I also run Snyk to scan my containers for possible vulnerabilities. I let renovate bot update my cluster deployments and every time an update is found automated checks will get executed to ensure the deployment update is stable enough before it even gets deployed.

---

> **lue3099**（-6 分） · 2026-09-01T09:52:28+08:00　
> Ding ding ding. You now get it.
>
> Have the packages (librarys or distributed source) be maintained by a trusted like a os repository.
>
> Also os repositories contain code library's and source (glibc etc). So saying OS's are different than language repositories is nonsense.
>
> I'm not gonna bother reading your other replies. They are nonsense

---

> **Mega3000aka**（12 分） · 2026-09-01T10:45:44+08:00　
> https://preview.redd.it/c8du7hr3otmh1.jpeg?width=1080&format=pjpg&auto=webp&s=fc0711f5fa1e050fb6875372092623d7627f1021

---

> **AbooMinister**（7 分） · 2026-09-01T10:52:05+08:00　
> idk why you're so upset, aren't we trying to come to a mutual understanding here? there's no need to be condescending, or for you to ask like a teenager.
>
> that said, I've done OSS work for organizations that do supply chain security for programming language package repositories. these institutions just don't have the manpower for it to work (and also, I don't think we *should* have a central authority, because that undermines a lot of what helps make a language ecosystem flourish. there are other, alternative situations that can be explored)

---

> **feng_sg**（1 分） · 2026-09-01T11:03:16+08:00　
> Nobody here is talking about egress filtering. You can lock down every inbound port and still get owned because your containers can call out to whatever they want. A compromised npm dependency or a malicious container image update just phones home and you never see it. Put each app on its own docker network with iptables rules that only allow the specific upstream IPs it needs. Anything else gets dropped and logged.

---

> **lue3099**（1 分） · 2026-09-01T11:11:12+08:00　
> It will have to be a compromise.
>
> We either have a flourishing ecosystem with many participants, which will inherently incur risk.
>
> Or we have a central body that is accountable for the security of what is released in the repos, that incurs delay and formalities.
>
> In practice they are antithetical to each other. I don't see how you can have bleeding edge, when participants release as they wish and maintain good security posture.

---

> **FlashyBattle976**（3 分） · 2026-09-01T11:52:30+08:00　
> Homelabs like that become redirectors for Volt and Salt Typhoon. Even if you don't host important information a clean residential IP in country is very important.

---

> **noodle_slurper**（1 分） · 2026-09-01T12:04:48+08:00　
> Passw2rd

---

> **ivanjxx**（1 分） · 2026-09-01T12:50:11+08:00　
> no auto updates

---

> **terribilus**（1 分） · 2026-09-01T13:20:06+08:00　
> Not seriously enough that I care if I lose the credentials, so I don't use credentials I care about.

---

> **fuckingredditman**（1 分） · 2026-09-01T13:57:17+08:00　
> Nope, litellm is basically just a proxy. LLM inference isn't done in hugely complex codebases anymore, it's a few centralized ones with a pretty shallow dep tree and weights don't contain runnable code anymore either. Biggest vectors are the tools in between like agent harness and coding agent clis. Those need decent sandboxes imo

---

> **d03j**（2 分） · 2026-09-01T15:32:48+08:00　
> Yes it does, but I think there is a near consensus that the risk of 0 days is usually lower than staying unpatched. It's not just a matter of the number of exploits but also of how many people knows them. Both increase with time.

---

> **d03j**（1 分） · 2026-09-01T15:35:22+08:00　
> didn't know that. thanks

---

> **PAjudic**（0 分） · 2026-09-01T16:19:14+08:00　
> Yeah, that’s the scary part. Supply chain attacks make “I only expose a reverse proxy” feel way less reassuring

---

> **Full_Tooth_a**（1 分） · 2026-09-01T17:35:50+08:00　
> I'd treat updates as a deployment problem. I'm not going to reliably catch malicious code by reading release notes. Pinning the image digest, reviewing dependency and lockfile changes, and watching for new outbound destinations feels more practical. I'd also keep the previous image and a tested backup handy. These steps can't prove an update is clean, but they can limit the damage from a compromised release.

---

> **TheGamerForeverGFE**（1 分） · 2026-09-01T21:41:15+08:00　
> Well, for one, I don't use npm

---

> **justinh29**（1 分） · 2026-09-02T02:15:45+08:00　
> https://github.com/justinholmes/secure-homelab

---

> **MrJelly007**（1 分） · 2026-09-02T05:17:15+08:00　
> I'm thinking of doing more research into securing my self hosted stuff, as I only just started and I'm very new to all of this.
>
> So far, I've got jellyfin, immich, motioneye, home assistant and a few other things running in docker on my Linux mint machine. No ports are open on my router, and I use tailscale for remote access.
>
> I think that's mostly fine? Maybe there's something important I'm missing lol.

---

> **Shadowarchcat**（1 分） · 2026-09-02T16:55:23+08:00　
> Additionally while you personally may not be a high value target ‚content‘ can be valuable. And most of your devices have cameras.

---

> **Citrus4176**（1 分） · 2026-09-02T19:21:00+08:00　
> How do you do the following?
>
> 1. Restrict a container from accessing the internet.
> 2. Encrypt traffic on the bridge network between containers.
> 3. Have containers use encrypted env variables.
> 4. Use a socket proxy.

---

> **PassiveLemon**（1 分） · 2026-09-02T21:25:22+08:00　
> 1. Set the containers network\_mode to none
> 2. Set the encrypted property to true in the network declaration
> 3. Unencrypted the variables at deployment, place them next to each compose file, up the stack, remove the variables
> 4. Depends on the proxy you use, some you connect to the proxy socket with tcp, others expose a linux socket that you can mount into your container

---

> **mandong**（1 分） · 2026-09-02T23:40:54+08:00　
> Nginx?

---

> **-kl0wn-**（1 分） · 2026-09-03T15:48:36+08:00　
> You can also point an agent at the code base and tests and get it to evaluate the quality of the code along with look for anything suss.

---

> **Last-Car-6128**（1 分） · 2026-09-04T06:58:09+08:00　
> I generally try to minimize the services I am hosting, and am wary of the risks associated with each application. Specifically, I have servers that run very trusted things, like nginx / other apt install packages, and servers with less trusted things, storing data on the servers according to how secure I think the system is.

---

> **nmunrod002**（1 分） · 2026-09-04T22:09:31+08:00　
> Honestly? Layered — and I've made peace with the fact that I can't audit every dependency; nobody realistically can. What I actually do:
>
> Egress is the underrated one. Everyone firewalls *inbound* and forgets *outbound*. Anything that doesn't need the internet goes on a Docker network with no egress, or gets blocked at the host firewall. If a compromised container can't phone home or exfiltrate, half the supply-chain scenarios die right there. For visibility, pointing your apps at a DNS sinkhole (Pi-hole/AdGuard) shows you what they're actually trying to reach — eye-opening the first time.
>
> Isolation. Containers are the floor, not the ceiling: rootless where you can, drop capabilities, read-only rootfs, a dedicated user per stack, nothing bound to [0.0.0.0](http://0.0.0.0) that doesn't need to be. Reverse proxy + SSO (Authelia/Authentik) in front of anything with a login.
>
> Exposure. Biggest single win: don't expose anything to the internet at all. VPN-only (Tailscale/WireGuard) for remote access — an app only reachable over the VPN has a fraction of the attack surface.
>
> Updates / supply chain. The honest answer: I don't read the source before updating, it's not realistic at homelab scale. Instead I pin versions (never blind `:latest`), skim the changelog, and *wait a few days* on big releases so someone else hits the landmines first. The biggest lever is just running **fewer things** — every app and dependency is attack surface. Boring, well-maintained projects over the shiny new thing.
>
> TL;DR: assume you can't fully trust the code, so cage it — no egress, no internet exposure, least privilege — and keep the surface small.

## 关联链接

- https://www.afp.gov.au/news-centre/media-release/two-wa-men-charged-following-afp-fbi-wapf-disruption-alleged-global

## 导航

- 项目页：[[10-项目/afp.gov.au_05ea9191]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
