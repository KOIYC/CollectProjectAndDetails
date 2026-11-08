---
type: "corpus"
item_id: "de3e888bc64d7a75"
title: "My journey after six months... and my thoughts.."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xi306l/my_journey_after_six_months_and_my_thoughts/"
author: "rickymilby"
published_at: "2026-10-29T06:43:31+08:00"
captured_at: "2026-11-08T12:52:13+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-10-29"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Personal Dashboard
metrics: {"score": 306, "comments": 53, "upvote_ratio": 0.9346590909090909}
comments_count: 52
comments_total: 53
discovered_via: "reddit:14d+settle10"
---

# My journey after six months... and my thoughts..

> [!info] 一句话导读
> This has been quite the learning experience for me. I knew absolutely nothing at the start of this, although I had a pretty good background understanding of com…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xi306l/my_journey_after_six_months_and_my_thoughts/>
> 指标：得分=306 · 评论=53 · 赞踩比=0.9346590909090909
> 作者：rickymilby　|　发布：2026-10-29T06:43:31+08:00
> 项目链接：—
> 采集：2026-11-08T12:52:13+08:00　|　id：`de3e888bc64d7a75`

## 正文

This has been quite the learning experience for me. I knew absolutely nothing at the start of this, although I had a pretty good background understanding of computers in general, but only with Windows machines. I just knew I wanted to take back control of my data.

I installed TrueNAS on an old i7 3770k system with 32GB of DDR3 RAM.

At first, I (heavily) used AI to help me with installing community apps, navigating the file system and permissions because I just didn't understand it. As I went, I learned more and more and went well beyond where I expected to stop.

Fast forward to now, I have a pretty good understanding of Linux and Docker in general. I ditched Windows on two other machines in favor of CachyOS and Ubuntu, and I am using those other two machines to run services complementing my server stack.

**My thoughts:**

* Docker is amazing. I am in constant awe of the capabilities that Docker has and really how easy it is to use once you understand how it works.
* Don't expose your services to the internet if you can help it. I have Ubiquiti hardware so everything is utilized via VPN when I am away from home.
* Physical disks will fail. I lost two drives during this time. One showed bad sectors after maybe 3 months, and its replacement was DoA. Luckily, I did not lose any data, but I do offsite backups to Backblaze weekly, my app pool is mirrored to another disk inside the server as well as pushed via rsync weekly to my CachyOS and Ubuntu systems.
* Learn how to use the shell and shell commands.
* Problems with things are permissions related 99% of the time.
* The "arr" stack is amazing. It's like magic.

Thanks for reading.

## 评论（52/53）

> **asimovs-auditor**（1 分） · 2026-10-29T06:43:41+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **rickymilby**（7 分） · 2026-10-29T06:44:44+08:00　
> AI was not used in the creation of this post. I occasionally use AI to help troubleshoot problems I have with services.

---

> **phoenixoverbrooklyn**（2 分） · 2026-10-29T06:53:44+08:00　
> How difficult was setting up Jitsi Meet?

---

> **rickymilby**（3 分） · 2026-10-29T06:56:34+08:00　
> Medium difficulty. I kept having problems with getting disconnected from the meetings immediately after joining. I had to play around with the environmental variables in the compose a bunch. Once they were correct, no issues. I am pretty impressed with Jitsi overall, the video and audio quality are very good.

---

> **Agreeable_System_785**（4 分） · 2026-10-29T07:07:22+08:00　
> Cool journey. Which apps are irreplaceable for you and why?
> Can you give like a top 3 or 5 of things that you can definitely not go without any more?

---

> **rickymilby**（12 分） · 2026-10-29T07:16:22+08:00　
> I would say Immich due to the fact that I have so many photos that I would have to pay for storage from Google if I didn't have it, plus, I don't want google having my photos.
>
> Paperless-ngx, helps me keep my documents organized rather than thrown in a drawer in a mess.
>
> The arr apps, makes media acquisition easy, although I could get everything manually if I really had to.
>
> Dockhand is pretty wonderful as well.

---

> **Asuma01**（1 分） · 2026-10-29T07:40:52+08:00　
> No Nextcloud?

---

> **rickymilby**（5 分） · 2026-10-29T08:02:05+08:00　
> Considered Nextcloud early on but did some reading about it and was a bit intimidated by it.
>
> I would feel comfortable deploying it now. Would certainly combine a couple services into one platform.

---

> **Asuma01**（4 分） · 2026-10-29T08:12:37+08:00　
> Just started my homelab server project and Nextcloud was one of the apps I was most excited for! As an absolute Linux newb I didn't find it very hard to setup. I just had an AI help me walk through the install.

---

> **rickymilby**（2 分） · 2026-10-29T08:24:54+08:00　
> I may look into it. Thanks!

---

> **TerraTrax**（9 分） · 2026-10-29T09:20:24+08:00　
> And people say AI will make us dumber. Its a fantastic teacher!

---

> **wazam**（2 分） · 2026-10-29T10:50:40+08:00　
> Nice dash. Noticed you’re using the icon from the archived filebrowser/filebrowser, check out the maintained fork “filebrowser quantumn” at gtsteffaniak/filebrowser if you’re not already running it. Cheers

---

> **TheMarketingNerd**（2 分） · 2026-10-29T11:27:22+08:00　
> > I would say Immich due to the fact that I have so many photos that I would have to pay for storage from Google if I didn't have it, plus, I don't want google having my photos.
>
> Is protecting all this covered in your Backblaze? I have a lot of data and a very haphazard backup process that I'm trying to get straightened out in a more painless way...

---

> **Only-Stable3973**（7 分） · 2026-10-29T13:19:56+08:00　
> Agreed, nothing like a good media stack, running KDE Neon, Traefik, Socket-Proxy...etc.
>
> [https://picoshare.devai.duckdns.org/-7JejZ4MNKk](https://picoshare.devai.duckdns.org/-7JejZ4MNKk)

---

> **Much-Delivery7127**（32 分） · 2026-10-29T13:20:42+08:00　
> The brain seeks the path of least resistance. Children who use AI may never learn to rely on their own intelligence instead of an artificial one. It will make us dumber slowly through our laziness

---

> **Much-Delivery7127**（6 分） · 2026-10-29T13:23:43+08:00　
> We are also neural networks; we just learn more slowly.

---

> **LastActivity2557**（1 分） · 2026-10-29T13:28:57+08:00　
> Dashbord name?

---

> **HomeOfficeOS_**（-1 分） · 2026-10-29T13:59:39+08:00　
> Are you open to trying this local-first/local-only financial planning app I've built? It's available for windows/macos-ios/linux/android I'd love some feedback actually :\]

---

> **Kelenoise**（2 分） · 2026-10-29T14:03:27+08:00　
> Looks like homepage ([https://gethomepage.dev/](https://gethomepage.dev/))

---

> **Straight-Truck2577**（4 分） · 2026-10-29T18:38:50+08:00　
> This argument gets thrown around a lot and people seem to forget that the same argument was made for calculators, computers, the internet, the list goes on. The data doesn't agree. The people that see these things as tools turn them into multipliers, not replacements for learning.

---

> **Much-Delivery7127**（7 分） · 2026-10-29T18:55:21+08:00　
> I understand all these points and agree with them. However, I see something else happening, and I notice changes in my own behavior. I’ve looked into how it works, and it’s weird to me how people can trust it that much. I hope we can find a way not to lose ourselves. Maybe we need to explain to children how it all works so that they approach it with a healthy dose of skepticism…much like how my parents once showed me how movies are made (before that, I used to watch them without any critical thinking at all).

---

> **Straight-Truck2577**（2 分） · 2026-10-29T19:11:27+08:00　
> Yep that's always been the way, before calculators many more people were able to multiply 2 digit numbers in their heads, than after, because they had to do so routinely. But having them is generally a net positive. It doesn't mean we stopped teaching kids multiplication without one in school. I get that this is an oversimplified example and I'm absolutely not dumb enough not to see the negatives of algorithms designed to draw attention, or that this is all guaranteed to work out for the best, but I also don't think that it's helpful to react to new technology as something that's fundamentally bad.

---

> **TerraTrax**（-1 分） · 2026-10-29T19:18:58+08:00　
> Do you really think people trust it that much? My experience is that people do treat AI answers with skepticism, perhaps erring to the side of caution. All you need to do is use it for awhile in your life and you'll get a feel for the things you can and cannot delegate to it (not unlike a human or a pet).
>
> I think like anything there is a learning curve and AI will be a net positive. If humans are ever to chop the work week down to 30 hours, AI will be a part of that.

---

> **Ill-Painter-1211**（9 分） · 2026-10-29T19:53:03+08:00　
> Oh wow. After setting up my own backend to run my freelance business with AI, next step will be something like this as well. This is motivating and I am looking forward to a steep learning curve myself. Keep on going mate!

---

> **rickymilby**（3 分） · 2026-10-29T20:03:37+08:00　
> Yes, my photos are backed up to Backblaze. They charge $6.95/TB/mo.

---

> **TerraTrax**（1 分） · 2026-10-29T20:45:04+08:00　
> I hear what you are saying, but this is an oversimplification of cognitive processes. People act to achieve a desired outcome. If your goal in life is to drive a bus and play video games, I'd rather you know how to use AI to help you manage your finances than learn algebra just so you can forget and not use it to manage your finances.

---

> **PowerVP**（4 分） · 2026-10-29T21:12:53+08:00　
> Based on what my friends who are teachers are saying, lots of kids do trust it that much. They have as much life experience or working knowledge so they have no frame of reference as to what sounds right or not.
>
> What I've essentially heard is that the gap between the best students (who use it as intended) and the worst students (who use it to replace their work) is widening. It's a force multiplier and since it's harder to have kids repeat grades or classes, there's no real incentive for the ones that use it to replace their work to do anything different

---

> **Watcher_of_Stars**（1 分） · 2026-10-29T21:43:39+08:00　
> Nice setup!
>
> p.s. Curious, did you use port forwarding for this one? I've only ever used Tailscale so far. How's your experience with it?

---

> **Only-Stable3973**（3 分） · 2026-10-29T22:54:39+08:00　
> Yes, I have port 80, 443...technically if you use dns01 you only need 443 open that is required for traefik. I have wireguard on a different box that is routed through traefik.

---

> **TheMarketingNerd**（2 分） · 2026-10-29T23:38:57+08:00　
> So you're using that version not the "personal computer back up" product?

---

> **ImpressionDepression**（1 分） · 2026-10-30T00:22:39+08:00　
> I mean not wrong but also I have so little interest in spending time formatting yamls that I'm happy to let claude take the wheel on that so I can do literally anything else

---

> **Eno_gamer10**（1 分） · 2026-10-30T00:27:53+08:00　
> I looooove your background, where can I find it ?

---

> **rickymilby**（2 分） · 2026-10-30T00:44:50+08:00　
> That is Gargantuan from the movie Interstellar.

---

> **rickymilby**（2 分） · 2026-10-30T01:05:37+08:00　
> Not sure what you mean by "personal computer back up" product.
>
> Backblaze B2 offers B2 Cloud Storage Buckets. That is what I use.
>
> I made a cloud sync task in TrueNAS to handle the backup.
>
> https://i.redd.it/t3v6fxhdufyh1.png

---

> **TheMarketingNerd**（3 分） · 2026-10-30T01:19:48+08:00　
> Gotcha, it seems like they have two different products. B2, and this one: https://www.backblaze.com/cloud-backup/personal
>
> It offers unlimited storage but the catch is I think everything has to be on your computer available to scan once every 30 days essentially. And it's not a 2 way street where it would serve any of that data, just a 1 way street backup.
>
> I was considering this one just for backup, but if you're using the cloud storage to serve anything or for apps then the B2 Cloud Storage is probably best for your use.

---

> **Old_Rock_9457**（2 分） · 2026-10-30T05:26:15+08:00　
> Happy to see AudioMuse-AI in your dashboard !

---

> **rickymilby**（2 分） · 2026-10-30T05:32:22+08:00　
> I set it up recently, took almost 2 days to run the analysis.
>
> Today was the first day I was able to play a similar tracks playlist and I'll be damned, it was nearly perfect.

---

> **Old_Rock_9457**（1 分） · 2026-10-30T06:01:05+08:00　
> I’m working to solve the nearly!
>
> Don’t miss that just today a new release is out with also a new release of the plugin (either Navidrome and Jellyfin). In the configuration of the plugin you can chose to override the instantmix functionality with different AudioMuse-AI functionality and today I just added DCLAP (the index of Text Search that now work also for By song search).
>
> The idea is that there isn’t one size that fit all, and I leave users to discover their size! Also I’m very proud of DCLAP because is a model I trained (by distillation) myself.

---

> **ValuableSleep9175**（1 分） · 2026-10-30T11:46:42+08:00　
> Yes.
> I connected gpt to my server cluster.  Now I just asked for things and it does it.
> Want a home page, I just tell it where to make the lxc and what IP to static and boom home page....
>
> I learn some stuff, but yeah it does 95% of the work now.

---

> **grip0matic**（1 分） · 2026-10-30T20:03:41+08:00　
> I want to genuinely ask. What would people do with what I have?
>
> I have this:
>
> - HP L13216-001
>
> - Power Supply 500W
>
> - Chipset Intel C246
>
> - Intel i7-8700 3,2
>
> - Intel UHD Graphics 630
>
> - Ram 32Gb DDR4 3600
>
> - WD SN530 256 GB 2230 (2 of them)
>
> - Hitachi HGST Ultrastar 3Tb (4 of them)
>
> I have it all there because I don't know if I should use TrueNAS or Proxmox. I want to selfhost a few things and the HDDs may change from those 3Tb to Toshiba MG06 10Tb in the future. I have a little DAS that I bought time ago, it sounded better than it is, still I have a lot of stuff in there and the thing survived a fire. But using data through USB is not that good.
> I am a bit obsessive with stuff, so I do want to try stuff but at the same time I don't, I really want to go for one thing and set it and with time improve certain stuff. But I am paralyzed at the idea of start to install things and find that I was wrong and maybe other thing was better suited for what I want.
>
> I just want to run things locally, the arr things, pihole, some very specific media, maybe a minecraft server because my gf gets bored, and emulation... I think.

---

> **reeetgio**（0 分） · 2026-10-31T02:30:27+08:00　
> Exactly, it really depends on how you use it. As a tool for explaining things and filling knowledge gaps, it can be incredibly useful

---

> **rickymilby**（2 分） · 2026-10-31T03:25:29+08:00　
> You have better hardware than I do. I am running 65 docker containers on a TrueNAS host. I didn't go the Proxmox route because I don't have enough overhead for virtual machines.
>
> The 3TB drives you have would be perfect for a RAID Z1 or possibly a RAID Z2 depending on how much storage space you want/need. If you plan on adding additional drives later using a HBA, I recommend Z2 as that gives you two drives worth of parity rather than Z1's one drive of parity.
>
> I started with four 10TB drives in Z2 and have since expanded the pool to six.

---

> **grip0matic**（1 分） · 2026-10-31T03:39:12+08:00　
> A HBA it's basically mandatory. I am a bit limited by the power supply and where to put more disks. Thank you for the comment, I am a bit more on the side of truenas, it feels way less intimidating than any other thing.

---

> **rickymilby**（1 分） · 2026-10-31T03:42:07+08:00　
> If you add a couple more disks, I would get a higher capacity PSU. and yeah, I had to get a different case to accommodate all my drives. I have the six HDD's, three SSDs, and an M.2.  I also have an old 2080ti in there. I think my PSU is 850 and that is probably overkill but I had it laying around.
>
> Good luck!

---

> **Significant-Turn6641**（2 分） · 2026-10-31T08:34:39+08:00　
> Calculators have made people significantly worse at arithmetic because you simply never learn tricks or patterns that make calculations easier.
>
> A similar thing will happen with AI. People never have to sit down and brainstorm or troubleshoot, so they simply never learn those skills.

---

> **Straight-Truck2577**（1 分） · 2026-10-31T09:02:11+08:00　
> *some people. Humans are inherently curious. We wouldn't be where we are if that weren't true. Twenty years ago old men were shaking their fists making the same arguments about having unlimited access to information on the internet "you don't even have to go to the library and read through 100 books to find the answer you're looking for, It's going to make you dumber". Funnily enough progress keeps happening. The intelligent and curious will continue to be intelligent and curious and the lazy will continue to take shortcuts.

---

> **Significant-Turn6641**（3 分） · 2026-11-01T00:39:06+08:00　
> Tools replace things. Calculators replaced the need for most to do complicated arithmetic. I don't think anyone can argue against that.
>
> The internet has changed how we get information. There's countless examples of perfectly capable students at good universities that cannot read to a proficient level. Why? Because it's not a skill that's needed for most.
>
> The difference between these technologies and AI is that the technologies you've mentioned seek to replace some small menial task (e.g. arithmetic, cataloging, etc.). AI seeks to replace them all.

---

> **Brief-Drawing-1434**（1 分） · 2026-11-01T01:41:28+08:00　
> what Ubiquiti stuff do you have?

---

> **rickymilby**（2 分） · 2026-11-01T02:09:59+08:00　
> UDR7, and a couple of U7 Pro Max APs for WiFi coverage.

---

> **HinkleMcKrinkle_**（1 分） · 2026-11-02T07:51:47+08:00　
> If you haven’t looked into it yet, check out [r/PangolinReverseProxy](r/PangolinReverseProxy) for exposing your web services externally. It gives you cloud flare like tunnels for exposing web based services. It’ll keep you from having to forward any ports externally from your LAN. I pay maybe 25-30 bucks a year for a small vps with nerdrack to host it. It seems safer than exposing ports from my LAN. They also introduced peer-to-peer networking like Tailscale within the last year or so. Really cool project and super easy to set up.

---

> **asumm33rs**（1 分） · 2026-11-04T07:59:07+08:00　
> What is that?

---

> **Successful-Future265**（1 分） · 2026-11-05T05:53:57+08:00　
> Replace Joplin with trilium notes

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
