---
type: "corpus"
item_id: "10f7e8382b8fb53a"
title: "Prismedia - A all in one media library and management app"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1w3fbfk/prismedia_a_all_in_one_media_library_and/"
project_url: "https://github.com/pauljoda/Prismedia"
author: "Pauljoda"
published_at: "2026-08-31T22:23:58+08:00"
captured_at: "2026-09-21T03:04:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (AI)
metrics: {"score": 14, "comments": 24, "upvote_ratio": 0.63}
comments_count: 31
comments_total: 31
discovered_via: "reddit:52d+settle3"
---

# Prismedia - A all in one media library and management app

> [!info] 一句话导读
> Over the last year, I've been building Prismedia. Previously, the app was called Obscura, and was actually a Stash alternative, and bits of that are still prese…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1w3fbfk/prismedia_a_all_in_one_media_library_and/>
> 指标：得分=14 · 评论=24 · 赞踩比=0.63
> 作者：Pauljoda　|　发布：2026-08-31T22:23:58+08:00
> 项目链接：<https://github.com/pauljoda/Prismedia>
> 采集：2026-09-21T03:04:52+08:00　|　id：`10f7e8382b8fb53a`

## 正文

Over the last year, I've been building Prismedia. Previously, the app was called Obscura, and was actually a Stash alternative, and bits of that are still present, but the focus has changed drastically.

Essentially, I found I had a whole fleet of apps in my "arrs stack", that all did the same thing, but for different media. So for my own personal use, I created an app that attempts to standardize what these interactions look like.

The core principle is that every media format follows the same "Entity" class, from a data science perspective it actually maps out really well that almost all logic from display to management can be shared, with media specific capabilities augmenting that.

That is what makes this app possible, everything from the core media management, scanning, identifyication via metadata providers, requesting, is all done via the same core platform.

Then, when it makes sense, first class endpoints are added for things like playback, reading, and listening.

The app covers alot of ground, so I'll just list some of the highlights, I enoucrange you to browse the site, source code, and try it out.

* Connect your Prowlarr and downloading clients to automatically track, monitor, and request content. Think the radarr/sonarr/lidarr stack but all integrated, and using the same logic. It even supports soul seek to assist with music sourcing, and when downloading, it will actually probe the files before and after to ensure it is a good match, or upgrade before merging it in.
* View all your content from one interface, from eBooks, comics, audio, movies/tv with rich playback for videos and subtitles, eBooks and audiobook syncing to allow switching between methods of consuming with shared progress, and dedicated audio player
* Identify content already existing using metadata plugins like TMDB, MusicBrainz, OpenLibrary
* Multi user to allow household members access, while delegating which libraries they can see
* NSFW libraries and individual media, to allow filtering of NSFW content, either blocking users from seeing it at all, or using a toggle to quickly hide and view the content. Stash scraper/plugins can be installed and wrapped to identify videos (no StashDB or PornDB, but plugins can be installed in app)
* Progress tracking, stats, and history to see what you've been consuming
* Apple native apps to leverage the native codecs on tvOS, macOS, and iOS for quick and seamless playback of even high quality files

This project was created for a need I have, to have all my media in one rich platform, that treats them all as equals. I liked radarr/sonarr and Jellyfin, but it felt disjointed, and the apps not rich. Jellyfin has a native client, but I felt it was lacking, and audio playback is again in a separate third party app. Prismedia has a native first party app, with all that for free (currently in TestFlight since apple has taken over 2 weeks to even approve the first build).

I post now as I feel the app is in a good release state, it has evolved alot over the last year, but I feel we are now solid, performant, and I challenge you to compare to Kavita, Jellyfin, and the other tools you use. This can be used beside those tools for you to evaluate, simply point at the same directories to scan and it will build out the library in it's own database.

As for AI usage, I did mark this as using AI, but this post (clearly since it probably isn't as coherent as I'd like), and the application were designed, validated, and reviewed by me. These days, I do feel software development is moving to AI assisted, and I've been coding for over 15 years, have a degree in computer science, and worked in large companies. The code isn't just generated and shipped, the design and actualy structure of the app is all exactly as I would write it by hand, but AI has allowed me to develop this while still having a full time job. I use the app every day, I listen to my music on it, have read through books with audiobook interop, watch our tv shows and movies on it, request new content, and for me it fits exactly what I've always wanted.

I hope you feel the same, but if you're happy with your current stack by all means continue to use it, and if you have feedback, please let me know as I'd be happy to look into it.

\- Website: [https://pauljoda.github.io/Prismedia/](https://pauljoda.github.io/Prismedia/)

\- Source: [https://github.com/pauljoda/Prismedia](https://github.com/pauljoda/Prismedia)

\- TestFlight: [https://testflight.apple.com/join/c9bgDxr7](https://testflight.apple.com/join/c9bgDxr7)

## 评论（31/31）

> **asimovs-auditor**（1 分） · 2026-08-31T22:24:11+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Pauljoda**（2 分） · 2026-08-31T22:25:32+08:00　
> It was noted in the post body, but here it is again:
>
> As for AI usage, I did mark this as using AI, but this post (clearly since it probably isn't as coherent as I'd like), and the application were designed, validated, and reviewed by me. These days, I do feel software development is moving to AI assisted, and I've been coding for over 15 years, have a degree in computer science, and worked in large companies. The code isn't just generated and shipped, the design and actualy structure of the app is all exactly as I would write it by hand, but AI has allowed me to develop this while still having a full time job. I use the app every day, I listen to my music on it, have read through books with audiobook interop, watch our tv shows and movies on it, request new content, and for me it fits exactly what I've always wanted.

---

> **SamTanna**（2 分） · 2026-08-31T22:44:46+08:00　
> Any plans for Roku?

---

> **Pauljoda**（1 分） · 2026-08-31T22:52:22+08:00　
> There are no plans, but the web app supports casting via AirPlay and Google Cast, so it can play on most things that way, the point of the apple native apps was to leverage the native encoding to not have to transcode on the server, and Roku still uses the server for alot of the preparation so it isn't that different from just casting. Perhaps down the road, but currently not unfortunately

---

> **lucasshiva**（1 分） · 2026-09-01T04:08:01+08:00　
> >Essentially, I found I had a whole fleet of apps in my "arrs stack", that all did the same thing, but for different media. So for my own personal use, I created an app that attempts to standardize what these interactions look like.
>
> A week ago I came to same decision: build my own service to merge 3 others. It's funny that I almost went C# too, but at the end I decided to use Kotlin for two reasons: Android app and Mihon extensions support.
>
> As for the UI, I'm still playing around with both Vue and Svelte, but I'm certainly not planning to build my own design system like you did lol.
>
> Anyway, Prismedia looks nice. You did a great job on the UI. I'm going to be checking it out later, and I'm definitely going to look at the code for some inspiration. Best of luck on the project!

---

> **Pauljoda**（1 分） · 2026-09-01T04:13:56+08:00　
> Happy you like it! I come S from c# and love it so I had to make the server dotnet and c#, it just fits how I think.
>
> As for the frontend, I did some tests with react (mainly since its so mature), and a couple others before I found svelte and really liked it, so I worked with it and have come to find it pairs well with c# headspace.
>
> Feel free to look through, copy, or whatever you want. I made it open for anyone to take and use if they want to adjust or improve. Happy to answer any questions that you have or reasons for the decisions I made etc.

---

> **lucasshiva**（1 分） · 2026-09-01T04:28:09+08:00　
> I'd prefer to be using C# on the backend too, but Kotlin is simply a better fit for what I have in mind.
>
> But for the frontend I might go with Vue. I like Svelte, but I almost went with React for the same reasons: maturity and ecosystem. Vue seems like a good mix of ecosystem and performance though, and something called Vapor mode is coming out pretty soon, which will make it even more performant.
>
> Anyways, I'll definitely be asking you some questions at some point. Our projects differ a little though. It seems like you own all the content, while I'm trying to interop with the existing services. For instance, all my ebooks come from Calibre - I don't want to import everything into my own service and lose all the metadata I've accumulated throughout the years. The same is true for mangas - years and years of Tachiyomi and Mihon. So I'll be doing my best to ensure that while my server owns the content, it should integrate directly with these other services for importing content and metadata.
>
> Once I'm free I'll spin up a Prismedia container and check it out. I also have to take a more detailed look at code to see how you're handling auth, db, and stuff related to books since it's where our domain overlaps. Good job on the project once again!

---

> **Korazu_**（1 分） · 2026-09-01T04:42:37+08:00　
> This looks interesting to me and will have to put it on my list of apps to check out. GL

---

> **MrLAGreen**（1 分） · 2026-09-01T06:05:40+08:00　
> looks and sounds like a great app.  i have recently had to redo my server so i will take a peek at your app.  few questions for you...
>
> 1. any android app in the future? i noticed that testflight is just for ios devices.
>
> 2. i do need to do a separate media folder line in docker yaml file for each type of media (music/movies/books) or do i just point it at the general media folder with the various folders of media in it?
>
> 3. i have my jellyfin mapped into my kodi for music/movies/tv will yours be able to do the same?
>
> lookin forward to your app...

---

> **Pauljoda**（1 分） · 2026-09-01T06:46:54+08:00　
> 1.	Currently no, one day when I have a proper device ton test on I’d like to
> 2.	no you can point to root and pick sub folders by library
> 3.	not sure I understand but if it’s a folder of music/tv/movies yes

---

> **MrLAGreen**（1 分） · 2026-09-01T06:52:12+08:00　
> 1 ok cool
>
> 2 very good
>
> 3 theres a kodi add on for jf...

---

> **Pauljoda**（2 分） · 2026-09-01T06:54:06+08:00　
> If you’re saying use Prismedia on kodi then no not currently, but the web all supports casting and the PWA is good

---

> **MrLAGreen**（1 分） · 2026-09-01T10:07:16+08:00　
> you should warn folks about that initial scan... i only included one media folder of movies and for the last 3 hours it has been scanning and keeping the cpu busy.  now i know i have a large folder of 3k+  but im also not exactly sure of what settings i may or may not have activated. just an fyi...

---

> **Pauljoda**（1 分） · 2026-09-01T10:11:02+08:00　
> Interesting, it should be according pinning the cup, it’ll use some but shouldn’t use the majority of it, it monitors cpu pressure and tries to keep from locking you up.
>
> What kind of utilization are you seeing? I will say the ffmpeg probe and trickplay generation can be heavy, especially on high quality video or long movies

---

> **MrLAGreen**（1 分） · 2026-09-01T10:13:21+08:00　
> what is the trickplay generation?

---

> **Pauljoda**（1 分） · 2026-09-01T10:15:28+08:00　
> The trickplay is essentially a series of stills used for the film strip scrubber, as well as the timeline preview thumbnail

---

> **PineappleGod**（1 分） · 2026-09-01T18:18:46+08:00　
> I'm testing the server. It is not able to identify movies that have dots (.) between names such as: 10.Clovefield.Lane. all of them come back unidentified. Also is there a way to import video files from a download folder by either moving them or doing atomic moves?
>
> I have a library of about 2000 movies and several thousand tv episodes. Doing a manual identification is not possible.

---

> **PineappleGod**（1 分） · 2026-09-01T18:24:02+08:00　
> Also clicking accept and next on identification gives api error: API 400: Bad Request - nothing is saved. Nothing shows up in docker logs. Please provide let the search remove all the regularly used expressions for the files. Also it could just read if there is a .nfo file or an .srr with the video file to get all the info.
> Or is this one of those things where you need to use sometime like filebot to rename all files in a certain for it to work at all? Which is not what I want.

---

> **Pauljoda**（1 分） · 2026-09-01T19:40:11+08:00　
> Periods on the name shouldn’t be causing this issue, but I’ll take a look.
>
> As for nfo and files like that, as long as the files exist beside the media file with the same file name, it will import them during the scan, might not show right away if doing a large scan, but it does pull that info in.
>
> As for imports, currently the idea is the app scans things in place, and doesn’t modify files, it tracks metadata in its own directory, the reason being the files need to be in a structured folder to be able to distinguish what it is. There would be no way to tell a tv show from a movie if you just send it a list of files, so the folder structure is important. Is there a reason you’d want to import files and do that move on disk instead of scanning where they are?

---

> **Pauljoda**（1 分） · 2026-09-01T20:11:21+08:00　
> Also, in settings there is a toggle to enable automatic identification during scans, you can see the confidence threshold as well, and it won’t pick when there are multiple results with exact matches (such as Spider Man since that has many identical results, but it does do a couple things to try and guess which one like season count etc, but movies in particular can be hard to differentiate and may require manual).
>
> Most things will be auto identified though

---

> **majora2007**（1 分） · 2026-09-01T21:46:20+08:00　
> You should look at Kavita to gain some perspective in how to maintain your existing metadata. It's a mature project that has some good insights you can learn from for your application (C# backend).

---

> **lucasshiva**（1 分） · 2026-09-01T23:05:18+08:00　
> I do know Kavita, but I don't think it supports the level of integration that I'm looking for.
>
> In short, the goal is to import my existing libraries into my own service, leaving all metadata intact. For books, this means building my own `calibre-web` essentially. Not only I want to support all of Calibre's default columns, but I also want to support some user-defined custom columns. For example, I have a true/false column to mark books as read or not read. When I import a Calibre library into my service, it should recognize that column and automatically mark some books as read or completed.
>
> I appreciate the Kavita shoutout though. Their metadata guide explains quite nicely everything a local file needs to have in order to be parsed correctly, so I'll make sure to support that too when it comes to local content.

---

> **majora2007**（1 分） · 2026-09-01T23:30:38+08:00　
> I'm not saying you should use it, I'm saying you should look at it's source as a reference for when you start your project, since it's already been battle tested in the wild west of epubs and does support some calibre tags.
>
> Yeah, you want a custom software for your needs. Makes sense if you have an established system in place.

---

> **lucasshiva**（1 分） · 2026-09-02T00:14:43+08:00　
> I'll definitely check out the source, thanks!

---

> **ysengrin101**（1 分） · 2026-09-03T04:55:47+08:00　
> Hello, I'm testing it via docker on synology. Works fine and it could evolve into something big. It's nice looking and clean. Right now it has very nice features that's why I;m looking forward to see more to come. I have a few questions/requests.
>
> 1. All my movies were automatically categorized under Videos. I used identify with tmdb plugin and all metadata matches the movie but it's still in videos. How to put these to Movies? I saw that folder need to be named a movies but right now I don't want to mess with renaming because jellyfin is still my main tool. Hopefully it will change!
>
> 2. During identify queue once choosing Accept or Accept and Next I have error API 400: Bad Request. My tmdb api seems to be fine. Going to next in queue works fine and after review of all selected media it saves metadata.
>
> 3. Is it possible to apply auto-match metadata? or accept proposed one from candidates list without opening full info page? In most of the cases it should be enough as we probably know poster. I know that there could be more mismatches but it could be easier to solve only them manually. In my case accepting 6 movies takes too much time considering the library of 100 movies it's a downgrade :/
>
> 4. Will you add other subtitles provider for example opensubtitles.org?
>
> 5. Last but not least - it's missing in all local libraries - is it a chance to add gamma correction to video? I'm watching movies mostly on projector and movies are darker than on monitor. Brightness is not helping much because it brighten also highlights which is not desired. Also some older movies can be a bit darker or some random series like well known last season GoT episode - which is almost dark -> it's an issue on monitors also -> only gamma correction is the way to solve the issue. It's probably my biggest request for a feature.

---

> **Pauljoda**（1 分） · 2026-09-03T05:06:18+08:00　
> Thanks for the feedback, I'll try to answer as best I can
>
> 1. Check [https://pauljoda.github.io/Prismedia/docs/library/videos](https://pauljoda.github.io/Prismedia/docs/library/videos), essentially you should point it to the root of the folder that contains video type files. For it to be considered a movie, the file must be the only video file in a folder, so "Avatar/Avatar.mov" or something like that. The reason is for series, if there are more than one, it becomes a series. If you point to a folder that is all the movies next to each other, with no folder to separate them, they will be flagged as videos. As long as you point the library root the same as Jellyfin, the structures should be very close and usually map 1:1
>
> 2. I'm not sure what could be causing that, might need to pin down a behavior you can desribe that replicates it so I can see what is going on, if you can tell me exact steps to replicate I can see what is happening
>
> 3. Yes, I should make the setting better but there is a setting in the metadata section at the bottom to enable auto identify, you can then set which plugins, media types, and confidence is allowed and then next library scan it will attempt to automatically identify things. Usually will match most things
>
> 4. It isn't well tested, but currently open subtitles but the .com domain, is .org a separate thing? I'm not super familiar with those so apologies if that isn't as well tested
>
> 5. For the web player, that might be something I can look into, gets a bit stranger with the native players but I can play around with it

---

> **ysengrin101**（1 分） · 2026-09-05T06:01:18+08:00　
> Thanks for a detailed reply.
> 1. Ok need to dive deeper into manual page.
> 2. Will it be better to send it via git as an issue?
> 4. I don’t know relation between org and com sites but somehow org sometimes has better subs basing on my own experience.
> 5. If you use a macOS then Iina player is worth checking out - for me it’s probably the best one because of visual and features - there is a nice video eq to adjust gamma and other parameters.

---

> **ysengrin101**（1 分） · 2026-09-05T06:17:37+08:00　
> Thanks for a detailed reply.
>
> 1.	⁠Ok need to dive deeper into manual page.
> 2.	⁠Will it be better to send it via git as an issue?
> 3.	⁠I don’t know relation between org and com sites but somehow org sometimes has better subs basing on my own experience.
> 4.	⁠If you use a macOS then Iina player is worth checking out - for me it’s probably the best one because of visual and features - there is a nice video eq to adjust gamma and other parameters.

---

> **Pauljoda**（1 分） · 2026-09-05T06:30:17+08:00　
> GitHub issues would be preferred for reports of errors.
>
> I’ll look at the other image adjustment things, might not be right away but I’ll keep it on my tracker

---

> **awayfromhomeuk**（1 分） · 2026-09-09T21:08:42+08:00　
> running it on a trial, so i can dump a whole stack if i manage to get it sorted. If i point it to my downloads folder as well as library media folders, will it hardlink what i already have or will it copy/move/rename my files?

---

> **Pauljoda**（1 分） · 2026-09-09T21:15:04+08:00　
> Adding your existing downloads and media folders as watched libraries will catalog the supported files where they already are. It won’t automatically hardlink files between those folders or move/rename your existing files.
>
> For downloads managed through Prismedia, each acquisition profile has an Import mode setting: Move, Hardlink, or Copy. Move is the default. Hardlink avoids duplicating the data when downloads and the library share a filesystem; otherwise it falls back to copying. Moving or renaming existing library files is a separate Organize action.

## 关联链接

- https://pauljoda.github.io/Prismedia/
- https://testflight.apple.com/join/c9bgDxr7

## 导航

- 项目页：[[10-项目/github.com_c0383749]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
