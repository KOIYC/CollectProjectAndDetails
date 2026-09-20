---
type: "corpus"
item_id: "945f405cee60ac14"
title: "Show HN: Gander, an Android file viewer that asks for no permissions"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49119425"
project_url: "https://github.com/mokshablr/gander"
author: "mokshablr"
published_at: "2026-07-31T05:45:13Z"
captured_at: "2026-09-21T02:55:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_mokshablr
  - story_49119425
  - show_hn
metrics: {"points": 211, "comments": 79, "engagement_velocity": 211}
comments_count: 79
comments_total: 79
discovered_via: "hn:show_hn:83d"
---

# Show HN: Gander, an Android file viewer that asks for no permissions

> [!info] 一句话导读
> Hi HN,I built an Android file viewer that opens PDF, Word, Excel, PowerPoint, images, video, audio, Markdown and code, and asks for no permissions at all.I have…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49119425>
> 指标：点赞=211 · 评论=79 · engagement_velocity=211
> 作者：mokshablr　|　发布：2026-07-31T05:45:13Z
> 项目链接：<https://github.com/mokshablr/gander>
> 采集：2026-09-21T02:55:18+08:00　|　id：`945f405cee60ac14`

## 正文

Hi HN,I built an Android file viewer that opens PDF, Word, Excel, PowerPoint, images, video, audio, Markdown and code, and asks for no permissions at all.I have always been uneasy about opening files people send me. On Android you either install a 400 MB office suite and sign in or use a small free viewer that wants storage access and ends up uploading your file to a server to render it. Also the hassle of having to download different apps for different file formats was really annoying.Gander holds no permissions, not even INTERNET so the OS itself guarantees the file cannot leave the phone.PDFs use Pdfium, media uses Media3, and Office formats are rendered by bundled JS libraries in a WebView and so no request goes to any server.It is a viewer only. Complex PowerPoint decks come out approximately right, spreadsheet charts are not drawn, and old binary .doc and .ppt are unsupported. I'll work on it as issues come up :PIt is 14 MB, MIT licensed and uploaded on Github releases.Do try it! I would love some feedback especially on files that render badly or need new support.

## 评论（79/79）

> **Mobeen0119** · 2026-07-31T05:53:22.000Z　
> Since everything is offline, what ended up being the hardest format to support while keeping rendering faithful?

---

> **TekMol** · 2026-07-31T07:15:58.000Z　
> This is interesting.I thought granting internet access to apps is not avoidable on Android.When an app does not request internet, is it really guaranteed that it cannot talk to the outside world? Or is it having other avenues like opening a browser or some other component with a custom url or something?Update: I just asked Gemini, and it does not look good:An Android app without the INTERNET permission is not guaranteed to be isolated from the outside world. While it cannot make direct network connections itself, it can use several other mechanisms to transmit data externally:Intent-Based Communication (The Browser) An app can launch an explicit or implicit Intent to hand data over to another app that does have internet access.That means the app can open a system browser using a URL containing the data it wants to transmit.It can also load a Chrome Custom Tab inside its own UI task, passing data through the URL string.There is also Inter-Process Communication: If two apps from the same developer share a User ID (sharedUserId), they run in the same process and share all permissions, including internet access.There is also the concept of Content Providers: Content Providers allow apps to share data. An offline app can write data into a shared database or a public Content Provider. A secondary, online-enabled app can then read that database and upload the contents.

---

> **sgc** · 2026-07-31T07:25:12.000Z　
> Can you add odt, ods, etc support? I use libreoffice viewer but it would be nice to reduce the number of apps on my device.

---

> **dheerajvs** · 2026-07-31T07:25:13.000Z　
> Tried it and I love it. Good work!
> Have you considered hosting it on F-Droid?

---

> **HelloUsername** · 2026-07-31T07:35:43.000Z　
> Seems nice, will check it out. I liked this one as well: "Little File Explorer – File Manager for Android 1.0 and above" 28.dec.2023 https://news.ycombinator.com/item?id=38789958

---

> **tim-projects** · 2026-07-31T08:09:53.000Z　
> Sounds great! You'll just need your social security or passport id sent to google to install and use it... sobs

---

> **ziagham** · 2026-07-31T08:13:14.000Z　
> Nice idea

---

> **adamddev1** · 2026-07-31T08:52:23.000Z　
> This looks great. It seems crazy how we got to this point where this is a revolutionary, unique product.

---

> **est** · 2026-07-31T08:59:34.000Z　
> This is super cool.> Requirements: JDK 17+ and the Android SDK (platform 35).Bummer. I am stuck with Android 14 for the moment.

---

> **noja** · 2026-07-31T10:16:24.000Z　
> This is a great idea - but doesn't Android inject network permission into all apks? It did in the past.

---

> **nextaccountic** · 2026-07-31T10:32:37.000Z　
> Could you publish to a store? Either/or Google Play or F-Droid

---

> **ashish004** · 2026-07-31T10:46:31.000Z　
> This is cool!

---

> **chrisjj** · 2026-07-31T10:47:42.000Z　
> Well done!> A tiny, open source, fully offline file viewer for Android that opens PDF, Word,Perhaps correct Word to DOCX. Word is not just DOCX and DOCX is not just Word. This user needs DOC viewing and would be disappointed having installed this app.I wish you every success with this.

---

> **chesscoachx** · 2026-07-31T10:52:47.000Z　
> Great. You built an excellent tool to solve a real-world problem: being able to open files on the fly without granting internet access and without having to install 400 MB bloated suites that track everything.

---

> **freedomben** · 2026-07-31T11:08:41.000Z　
> Great work! A tool like this is sorely needed.How is accessibility? Do PDFs work with screenreaders for example?

---

> **collabs** · 2026-07-31T11:14:20.000Z　
> Two things I really like:1. Markdown loads as preview2. Plain text files wrap instead of scrolling to the rightGood job and thank you for sharing

---

> **mathfailure** · 2026-07-31T11:21:17.000Z　
> I don't understand the comments to this post. Don't people use firewalls anymore to limit internet access only to the apps really needing it?

---

> **aand16** · 2026-07-31T12:12:40.000Z　
> Please add signature to readme so users can verify before installing with Obtainium eg:5B:5C:F6:4A:94:23:7C:D5:F0:E0:85:76:00:38:BC:1C:EB:DF:18:DA:BA:5C:B3:EA:CA:7C:15:9F:22:A7:E2:4B

---

> **carloslfu** · 2026-07-31T13:05:41.000Z　
> this is cool! It's amazing that it's still such a pain to do something like this with built-in Android app.

---

> **atmanactive** · 2026-07-31T13:10:21.000Z　
> Thanks for sharing. Could it be possible to add optional force-dark mode for documents as well? The feature list mentioned dark mode, but that's for app's own UI. The really awesome feature would be to be able to invert the document colors so that the document itself is shown in dark mode. Thanks.

---

> **array4277** · 2026-07-31T13:39:35.000Z　
> The app is pleasingly very responsive. I don't think I've used anything else on Android that lets me open and close PDFs rapidly without getting bogged down. Nice!

---

> **getpokedagain** · 2026-07-31T15:53:06.000Z　
> Going to test this out. I've been very happy to see the number of new apps being developed to be installed on android via obtanium and away from the Google app store. I assume it's llms enabling folks to get quick apps out.

---

> **celsoazevedo** · 2026-07-31T16:37:46.000Z　
> Can this open .rtf files?I know it's old, but I still receive them from time to time.

---

> **nubinetwork** · 2026-08-01T04:41:26.000Z　
> How does this work? I was under the impression that newer android sdk versions required permissions to access the filesystem... if you're using an older sdk, I can't really imagine the app working for longer than a year.

---

> **maxzhdev** · 2026-08-03T05:07:18.000Z　
> Useful application. I hope the author will upload it to the store and pass Google verification

---

> **quickdeer** · 2026-08-09T12:06:16.000Z　
> This sounds great and I would like to try it on my iPhone. Will you be developing an IOS version?

---

> **vrighter** · 2026-07-31T07:11:40.000Z　
> Why would rendering a document need internet access?

---

> **mokshablr** · 2026-07-31T11:26:00.000Z　
> pptx by a mile. A slide is absolutely positioned shapes with a whole layout inheritance thing going on so the JS renderer ends up reimplementing a whole layout engine, and it gets you to "approximately right" and stops there. Charts I gave up on.docx was annoying in a different way. Bullets came out as junk characters for a while and I couldnt work out why. I then found that Word writes them as private use area codepoints in the Symbol font so unless you have that exact font you get some junk. I just map them back to unicode after the render.xlsx was the easy one, SheetJS does the hard part.On faithful though none of this is faithful the way LibreOffice is. Its more that "you can read the document and it looks roughly right" which is what I wanted out of an app of 14MB.

---

> **sheept** · 2026-07-31T07:41:53.000Z　
> I guess that makes sense. Since most non-privacy-focused Android distributions don't let users turn off the internet permission, keeping the permission secure likely ceased to be a priority.The full list of bypasses is likely much larger because it doesn't fall in the scope of bug bounties.

---

> **marak830** · 2026-07-31T08:14:07.000Z　
> Christ that's depressing.I'm assuming that all works even with application sandboxing (1) or am I mis-reading how that is applied to applications.Man I need to move my movement to GrapheneOS up to be sooner.(1) https://source.android.com/docs/security/app-sandbox

---

> **nottorp** · 2026-07-31T08:23:50.000Z　
> You're aware that the only really secure computing device has no way to connect to a network and is under armed guard?Edit: also that LLMs are tuned for "engagement" not for answers like "it's secure enough, move along"?

---

> **andyjohnson0** · 2026-07-31T10:20:33.000Z　
> This is all very true, unfortunately. Google designed Android as a an OS for internet appliances. They're not interested in local-only apps working on local files.But I think the OP is to be complimented for what they've built and their intention in making it local-only. I've long felt that apps that *genuinely" respect privacy are one of the few areas of opportunity still left in the mobile space. I wish there were more develpers building things like this.

---

> **chrisjj** · 2026-07-31T10:35:04.000Z　
> > If two apps from the same developer share a User ID (sharedUserId), they run in the same process and share all permissionsGood grief. What a huge vulnerability. Is there some benefit that justifies this?

---

> **inigyou** · 2026-07-31T10:38:13.000Z　
> GrapheneOS asks for internet permission when you install any app.

---

> **yonatan8070** · 2026-07-31T10:52:18.000Z　
> > That means the app can open a system browser using a URL containing the data it wants to transmit.This can be mitigated by using an app like URLCheck [1], which you set as your default browser, and it shows and lets you edit the URL being opened before handing it off to your real browser. It also has neat features like choosing to open in incognito (if you use Firefox) and automatically removing tracking parameters.[1] https://f-droid.org/packages/com.trianguloy.urlchecker

---

> **mokshablr** · 2026-07-31T11:14:29.000Z　
> Yeah fair I was too flat in the post... No INTERNET means my process can't reach the network. It doesn't stop an app passing data to something that can, so your list is right.It's not a guarantee then, it's just a lot less to check. There's no silent route out so all that's left is what the app chooses to send via intents and Gander sends two, both when you tap something ("Share" and "Show in file manager")Nothing anywhere builds a URL out of the file contents. No browser launch, no Custom Tabs and no shared user ID. The only content provider is closed to other apps. The one time a file goes anywhere is when you hit Share and pick the app, and what it gets is read access to that one file.In case you grep it there's an https:// in ViewerActivity.kt. That's the local virtual host WebViewAssetLoader serves the bundled renderers from, it never leaves the process.

---

> **well_ackshually** · 2026-07-31T12:13:47.000Z　
> "I just asked Gemini, and it turns out that Mossad can steal my data anyways".- An app without the INTERNET permission will crash the moment you try to access the internet. It's like a rite of passage of every android developer with every new project, you forgot the permission.- Launching an Intent is EXTREMELY visible. It opens a full on browser. It's limited to a GET with a dedicated URL, so what are they going to do, stuff your data in query params ?- Even in the case of another app being installed that would silently receive this intent and not pop an activity, you need a different app. It cannot be an activity added by the same package.- Loading a Chrome Custom Tab opens a whole ass browser in front of you, think you're going to miss it ?- Shared user IDs also require two different app installations and you cannot declare multiple. You also cannot have sharedUserId if you do not sign the apps with the same key. you cannot sharedUserId with Facebook, you need once again a dedicated app installation.- A ContentProvider needs a dedicated permission on the writing app AND on the reading app, which is once again very visible.I'll add more to your list: an app can request to write a file inside your downloads folder, and another one can show a popup asking you to open it! And if someone shows up with a hammer at your door, he can also hit your fingers really hard to make you tell him the data.Android apps are, by default, very well isolated. INTERNET is a permission like any other, just not surfaced as a dangerous one (like permanent access to your background location would be), or a runtime one (like access to your current location while the app is in foreground)

---

> **exe34** · 2026-07-31T15:21:58.000Z　
> I use a rooted phone and afwall+ which uses the underlying Linux firewall. There's also the mobile and WiFi data permissions you can change manually.

---

> **reorder9695** · 2026-07-31T18:16:15.000Z　
> AOSP allows the internet permission to be denied per app (hence LineageOS and Graphene exposing it), it's just most OEMs ROMs don't expose it, you can draw your own conclusions from that.

---

> **rrvsh** · 2026-08-01T04:57:19.000Z　
> Why post AI-generated answers? Anyone reading your comment could do the same.

---

> **mokshablr** · 2026-07-31T12:51:35.000Z　
> ods actually already works.. it goes through the same SheetJS path as xlsx and csv. But your question made me check properly and there's a bug... I never registered the OpenDocument mime type so Gander wont show up in the "open with" list when you tap a .ods. Opening it from inside the app works fine.Fixed in the manifest just now, it'll be in the next build.odt and odp dont work at all. odt is a fair ask.. its the same shape of problem as docx so it's doable. Less sure about odp though.. the pptx renderer is already the weakest part of this.And yeah, fewer apps on the phone was pretty much the whole reason I started building this.

---

> **clort** · 2026-07-31T08:50:31.000Z　
> That is listed in the Roadmap section right at the end of the README.md file

---

> **netfortius** · 2026-07-31T10:41:51.000Z　
> Obtainium works just fine with the github source

---

> **notpushkin** · 2026-07-31T09:02:14.000Z　
> Which is also weird considering most of formats are just opened in a WebView with a respective JS-based viewer. Surely it can be backported?

---

> **shscs911** · 2026-07-31T09:06:07.000Z　
> Just installed it in my Android 10 phone and it works.

---

> **mokshablr** · 2026-07-31T11:34:22.000Z　
> Sorry, that's on my README. That line is under "Build from source" so it's what you need to compile it, not to run it. minSdk is 26, so Android 8 and up.Android 14 is well past the floor, you're good to go!

---

> **chrisjj** · 2026-07-31T10:49:12.000Z　
> Seconded.

---

> **mokshablr** · 2026-07-31T21:30:27.000Z　
> Fair enough, fixed that in the README.

---

> **weberer** · 2026-07-31T13:59:49.000Z　
> Thanks, Claude

---

> **mokshablr** · 2026-08-03T04:00:51.000Z　
> Thanks for trying it out!

---

> **rationalist** · 2026-07-31T11:41:18.000Z　
> No, most people do not.

---

> **PennRobotics** · 2026-07-31T12:16:41.000Z　
> I had the goal to eliminate annoying ads in some apps that I use. I deleted the user data for those apps and also applied restrictions so they could no longer access internet. Ads still showed up.I mostly stopped using these types of apps and switched to F-Droid alternatives.

---

> **atmanactive** · 2026-07-31T13:05:26.000Z　
> Could you please recommend a comfortable personal firewall app for Android?

---

> **fg137** · 2026-07-31T13:18:33.000Z　
> Firewalls are already a pain for desktop OS. They are basically unusable on mobile for normal users.

---

> **mokshablr** · 2026-07-31T18:20:33.000Z　
> Added, it's in the README under Install now. Thanks for bringing that up!

---

> **Anamon** · 2026-08-02T09:47:33.000Z　
> It's explained in the readme. Granting access to folders on the file system is a process independent from permissions.This is from the Android documentation[1]:"Because the user is involved in selecting the files or directories that your app can access, this mechanism doesn't require any system permissions […]"[1] https://developer.android.com/training/data-storage/shared/d...

---

> **Chilinot** · 2026-07-31T07:22:10.000Z　
> PDFs can do all sorts of shenanigans, such as bundle executable javascript that runs when the file is opened.

---

> **chrisjj** · 2026-07-31T10:43:04.000Z　
> Apart from exfiltration, no reason at all.

---

> **well_ackshually** · 2026-07-31T12:15:25.000Z　
> permission.INTERNET has _never_ been a dangerous permission on android.

---

> **csande17** · 2026-07-31T09:57:49.000Z　
> Yeah, Android's sandbox deals with low-level file access and socket APIs and stuff. But Android also, intentionally, allows apps to expose their data and functionality to other apps via the higher-level "intent" system.Apps get to choose what permissions are needed to access their intents, so under Android's security model, really it's Chrome's fault (or whatever browser the user has installed) for exposing an intent that allows apps that don't have the INTERNET permission to exfoltrate data.Similarly, apps are also allowed to collude to share data with each other if they want; that's how stuff like Google Play Services works.

---

> **TekMol** · 2026-07-31T10:02:23.000Z　
> As I understand it, this "Application Sandbox" is to prevent app A seeing what app B is doing.The problem here is a different one: The user granting an app access to their files and then having no way to prevent that app from sending that data to the developer of the app.

---

> **j16sdiz** · 2026-07-31T10:55:30.000Z　
> First, `sharedUserId` is opt-in.You need something like that for plugin / extension like system.Third, it is being deprecated. and people are screaming "bad google" "android is no longer free!"

---

> **well_ackshually** · 2026-07-31T12:18:11.000Z　
> Literally there for more protection. Split your app into different apps, each handling a component. Want a banking app, without access to registering your card for NFC payments ? Split the app.sharedUserIds cannot be applied blindly, they need the app to be signed with the same key, both need to declare their sharedUserId to be the same, etc.

---

> **chrisjj** · 2026-07-31T10:48:31.000Z　
> Even an app that does not want internet?

---

> **zombot** · 2026-07-31T10:50:51.000Z　
> Can you deny it and is the situation the same as on Android?

---

> **rrvsh** · 2026-08-01T04:58:30.000Z　
> It's insane that after four years of these tools being ubiquitous people still defer to them for their own critical thinking

---

> **hod6654** · 2026-08-01T04:36:27.000Z　
> How is the rooted experience these days? Do you deal with broken (banking) apps all the time?

---

> **xigoi** · 2026-08-01T08:10:34.000Z　
> F-Droid makes it much easier to discover apps.

---

> **ies7** · 2026-07-31T15:07:17.000Z　
> Rethink: dns + firewall + vpn

---

> **mathfailure** · 2026-08-08T23:39:04.000Z　
> AFWall+, of course.

---

> **nubinetwork** · 2026-08-02T11:31:00.000Z　
> I don't get why everyone went doomer a few years ago when they were implementing the newer apis then... /shrug

---

> **echoangle** · 2026-07-31T08:29:07.000Z　
> You don’t need internet to run JS though. And the JS seems to be pretty sandboxed in normal viewers too, so a pdf file shouldn’t make network requests on its own. As long as there is no iframe-like content I don’t see how rendering a document would ever need network.

---

> **vrighter** · 2026-08-03T08:32:04.000Z　
> if that document really does need internet access to be rendered (unlikely) then it can use the internet connection one would have used to upload the file in the first place.

---

> **murderfs** · 2026-07-31T10:17:12.000Z　
> > Apps get to choose what permissions are needed to access their intents, so under Android's security model, really it's Chrome's fault (or whatever browser the user has installed) for exposing an intent that allows apps that don't have the INTERNET permission to exfoltrate data.You might as well blame the phone for not being encased in concrete and thrown into a well. You might not want your text message application to have the internet permission, but you'd certainly want to be able to open links from it.

---

> **chrisjj** · 2026-08-01T09:13:32.000Z　
> > First, `sharedUserId` is opt-in.By the user?> You need something like that for plugin / extension like system.Plugin/extension != app.

---

> **drunner** · 2026-07-31T11:11:42.000Z　
> I don't see that as an option, but I'm not a GrapheneOS power user.

---

> **drupe** · 2026-07-31T11:20:43.000Z　
> No, it only asks if the app requests the internet permission.

---

> **drunner** · 2026-07-31T11:12:54.000Z　
> You can on graphene. It's not uncommon to use Google keyboard this way for example.

---

> **exe34** · 2026-08-01T07:35:21.000Z　
> I don't use banking apps, my banks have websites that work. Last time I tried to add my bank card to the Google wallet, it worked for a few days and then stopped. I've had a few apps that refuse to run but then worked fine with magisk.For me, root on my own devices is a matter of principle. If an app doesn't work, then I don't want it. In the future I might carry a gimped android device for essential things like train apps if I have to, but then it won't be the device I actually carry in my pocket, it'll be in my bag. Mobile computing is for me.

## 导航

- 项目页：[[10-项目/github.com_bfe531c0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
