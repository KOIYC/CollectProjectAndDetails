---
type: "corpus"
item_id: "4eed1e56f2ced86f"
title: "What's currently the best Music Discovery system yall are using with Navidrome?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xrzjyr/whats_currently_the_best_music_discovery_system/"
author: "PETEthePyrotechnic"
published_at: "2026-11-10T02:29:41+08:00"
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
  - Self Help
metrics: {"score": 58, "comments": 25, "upvote_ratio": 0.9393939393939394}
comments_count: 26
comments_total: 26
discovered_via: "reddit:14d+settle10"
---

# What's currently the best Music Discovery system yall are using with Navidrome?

> [!info] 一句话导读
> I'm working on transitioning from Spotify to self-hosting and I'm hoping to retain some kind of music discovery method. Are there any iOS apps that support last…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xrzjyr/whats_currently_the_best_music_discovery_system/>
> 指标：得分=58 · 评论=25 · 赞踩比=0.9393939393939394
> 作者：PETEthePyrotechnic　|　发布：2026-11-10T02:29:41+08:00
> 项目链接：—
> 采集：2026-11-20T09:47:05+08:00　|　id：`4eed1e56f2ced86f`

## 正文

I'm working on transitioning from Spotify to self-hosting and I'm hoping to retain some kind of music discovery method. Are there any iOS apps that support last.fm/musicbrainz integration, or am I misunderstanding how the pipeline works for these systems? I've been looking at Lidarr and Aurral, but I'm not sure how that incporporates into using navidrome. Any advice and reccomendations are appreciated, I'm still learning a lot about all of this!

## 评论（26/26）

> **asimovs-auditor**（1 分） · 2026-11-10T02:29:50+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **PETEthePyrotechnic**（3 分） · 2026-11-10T02:38:59+08:00　
> I didn't use AI at all, screw that noise

---

> **naomi_trail**（6 分） · 2026-11-10T02:46:38+08:00　
> I have used last.FM for a couple decades now. There are two main ways to scrobble your navidrome listening. You can have an app on your phone that will watch for any music listening activity on your phone independent of navidrome. This is good if you have several music sources on your phone. You can also enable scrobbling server side so that any time your stream from navidrome it will scrobble what you are listening to. There are directions to do this in the navidrome docs. The instructions aren't great so you can DM me if you need help setting that up

---

> **mrsandman326**（7 分） · 2026-11-10T02:50:33+08:00　
> I recommend DroppedNeedle (includes Lidarr and slskd) with last.fm, youtube API or listenBrainz and streaming to Jellyfin, Plex, Navidrome or any iOS/Android app li Substreamer.
> All integrations I mentioned are supported natively.

---

> **Jetama11**（17 分） · 2026-11-10T02:51:30+08:00　
> Aurral is pretty impressive in this regard, and it just links to your last.fm or listenbrainz.
>
> Just about every recommendation software I’ve seen relies on one of the two scrobblers.
>
> But also, if you go on either one you can do the same thing, it just takes longer. Listenbrainz will literally make recommendation playlists for you, and last.fm has a thing called neighbors which will show you other people that listen to similar music to you.

---

> **Important_Mammoth_69**（4 分） · 2026-11-10T03:04:54+08:00　
> same im using dropped needle and its ok, vibe coded buggy as hell. but the best solution we have right now.

---

> **ponzi_gg**（8 分） · 2026-11-10T03:21:52+08:00　
> [Aurral.org](http://Aurral.org) ♡

---

> **Total_Wolverine1754**（2 分） · 2026-11-10T03:22:37+08:00　
> small distinction: musicbrainz is the metadata database; listenbrainz is the listening-history/discovery service. for ios, substreamer can send plays to your navidrome server, and navidrome can forward them to listenbrainz from your personal settings, so the phone app doesn't need a separate direct integration.
>
> one current catch with the listenbrainz recommendations above: its homepage is warning that statistics and weekly playlists are unstable. i'd get playback and scrobbling working first rather than treat a missing weekly playlist as a broken navidrome setup.

---

> **mrsandman326**（2 分） · 2026-11-10T03:25:56+08:00　
> Yeah I find sometimes full PC frozen because I have DroppedNeedle tab opened… it is a mess in terms of performance but still worth as it is very powerful and keep services centralised.

---

> **Angelsomething**（3 分） · 2026-11-10T03:45:44+08:00　
> Combo of diggarr and sonobarr atm.

---

> **ImpressionDepression**（3 分） · 2026-11-10T04:06:21+08:00　
> Aurral has been the best for me and doesn't rely on Lidarr.
>
> the tl;dr is you add your existing library to aurral, it scans for artists so you can view/download stuff from there. Then it downloads things to a directory, you add directory to navidrome, remove your previous, it handles it via hardlink.
>
> I use it with slskd, deemix, and sabnzbd + listenbrainz/last.fm.

---

> **kernald31**（2 分） · 2026-11-10T04:29:53+08:00　
> Can you somehow have it download files to some sort of staging area, to be imported to your main library by e.g. beets?

---

> **ImpressionDepression**（1 分） · 2026-11-10T04:40:39+08:00　
> Should be possible, could have it download to a folder then use beets to move to your main that it sees as read-only.
>
> Tbh depends on what you're using beets for. Could always just have it run afterwards to fix tagging and whatever but IIRC aurral uses musicbrainz for that anyway so might be an extra step

---

> **ponzi_gg**（1 分） · 2026-11-10T05:00:09+08:00　
> it has pretty extensive webhooks for managing anything like that

---

> **Jetama11**（1 分） · 2026-11-10T05:06:50+08:00　
> How do you have aurral setup w/o lidarr? I had to use nightly and do some hacked up solution.

---

> **MrLAGreen**（2 分） · 2026-11-10T05:07:15+08:00　
> i dont agree... DN wanted to rescan and approve an already established ibrary as if it had never been input into a system before. to me that was/is double unnecessary work, especialy if you have a large ibrary aready.
>
> id stick with soulbeet and slskd after its initial scan its on point and it works pretty straight forward. no lidarr or anything else to deal with...

---

> **ImpressionDepression**（1 分） · 2026-11-10T05:13:28+08:00　
> just added deemix/slskd and prowlarr/sabnzbd and seems to work fine. downloads stuff to a folder, navidrome sees folder, thats about it.

---

> **ponzi_gg**（1 分） · 2026-11-10T05:19:33+08:00　
> sounds like an old build. its all native now and runs very smoothly.

---

> **Due-Mine-4097**（1 分） · 2026-11-10T14:57:03+08:00　
> How does this compare to Explo?

---

> **guar47**（2 分） · 2026-11-10T20:28:53+08:00　
> This. I am using [last.fm](http://last.fm) from Navidrome (on-server scrobbling) + YouTube Music app (via Pear client) scrobbling for rare times I listen there. Last.fm home page gives pretty nice recs. It might help that I've been using last.fm since 2010. But I still tempted to try separate solutions like Aurral.
>
> PS Not related to OP question, but human-curated recs are underrated (newsletters + youtubers for me).

---

> **HistorianMundane3176**（1 分） · 2026-11-11T00:09:37+08:00　
> Since you mentioned Aurral, one distinction that may help is the server's discovery setup versus the playback client.
>
> Disclosure: I'm the creator of Cadence, an MIT-licensed native SwiftUI client for Aurral. Its Discover screen consumes Aurral's native API; external provider configuration stays on the server. Cadence also has local library mixes, but it does not directly connect [last.fm](http://last.fm) or MusicBrainz accounts. Generic Navidrome/Subsonic compatibility is unverified, so I wouldn't recommend it as a verified solution to that part of your setup.
>
> If you end up choosing Aurral, Cadence may be useful on the client side: there's a signed/notarized Mac download, and iPhone source is available. iPhone currently requires a source build or an existing private beta invitation; there is no public TestFlight link.
>
> I've put the source, setup instructions and current limits in this week's designated New Project Megathread: [https://www.reddit.com/r/selfhosted/comments/1xox23i/comment/19sfki4jmc8yo/](https://www.reddit.com/r/selfhosted/comments/1xox23i/comment/19sfki4jmc8yo/)
>
> Development has used AI assistance; testing and known gaps are documented. Happy to clarify the client side if that's useful.

---

> **Dhanni-Asmus**（1 分） · 2026-11-11T02:27:46+08:00　
> the mobile app usually doesn't do the heavy lifting for discovery. most setups have the server log your listening history, and a background service uses that data to automatically fetch similar artists into the media directory.

---

> **PETEthePyrotechnic**（2 分） · 2026-11-11T02:44:49+08:00　
> Ngl man this reads exactly like claude

---

> **Rich_Carpet1615**（1 分） · 2026-11-11T08:50:36+08:00　
> I generally want recommendations based on my library,  rather than listening history - though this does mean I must rely on positive signals only. Anyway I had Claude Code build me a workflow where my library is cycled through and ListenBrainz is used to find similar artists. It then uses ytdlp to find an album not in my library.

---

> **mrsandman326**（1 分） · 2026-11-11T16:03:11+08:00　
> Maybe I'm misunderstanding your situation, but when you first install DN it has to build its database to know what is in your disk. Also depending which managing profile you choose it will rename files to follow the desired pattern or just caching the files. In my experience, DN didn't do anything until I set the music folder.

---

> **MrLAGreen**（1 分） · 2026-11-14T15:56:15+08:00　
> it did find my music and then it wanted me to "approve" each folder(artist, album) as if it wasnt already cleaned up and ready to go.  i have maybe 500gb of music. didnt feel like having to rebuild the wheel all over again. ND found it and was ready to go out the box...

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
