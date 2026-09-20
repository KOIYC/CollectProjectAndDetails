---
type: "corpus"
item_id: "eba81e1a3971fe8e"
title: "[ Removed by moderator ]"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1wi48hv/ghee_an_ios_and_android_companion_app_for/"
project_url: "https://apps.apple.com/us/app/ghee-for-mealie-recipes/id6758328014"
author: "Fresh-Knowledge-8571"
published_at: "2026-09-17T01:43:35+08:00"
captured_at: "2026-09-20T09:41:45+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Wednesday Exceptions
metrics: {"score": 38, "comments": 35, "upvote_ratio": 0.81}
comments_count: 37
comments_total: 37
discovered_via: "reddit:7d+settle3"
topic: AI 工具/Agent
archived: true
archived_at: "2026-09-20T10:02:36+08:00"
archive_reason: "排除:标题"
---

# [ Removed by moderator ]

- **来源**：Reddit 独立开发版块　|　**kind**：post
- **原帖**：https://www.reddit.com/r/selfhosted/comments/1wi48hv/ghee_an_ios_and_android_companion_app_for/
- **指标**：得分=38 · 评论=35 · 赞踩比=0.81
- **作者**：Fresh-Knowledge-8571　|　**发布**：2026-09-17T01:43:35+08:00
- **项目链接**：https://apps.apple.com/us/app/ghee-for-mealie-recipes/id6758328014
- **采集**：2026-09-20T09:41:45+08:00　|　**id**：`eba81e1a3971fe8e`

## 正文

If you run Mealie, this is a phone app for it. iPhone, iPad, Android, built with Flutter.

I built it because the mobile browser experience never clicked for my family, especially shopping lists at the grocery store. Before Mealie we were on Cozi. Its ads and sync problems are what pushed me into self-hosting in the first place. Ghee has been on both stores since April. My spouse and I use it every day, whether we are cooking or shopping.

Mealie's web UI works on a phone. What it cannot do is work without the server: lose signal at the store or on the road and your recipes and lists are gone. Ghee keeps them on the device. Viewing lists offline and the first 15 offline recipes are free. Checking items off offline and storing more recipes are paid on-device features, details below. Everything your Mealie server already does is free in the app.

Since 1.9.0, lists you have opened stay on screen when the signal drops. They are saved on the phone, so they open on a cold start with no connection, with a note showing when they were last updated. That part is free. Pro adds the offline write path: check-offs queue on the phone and sync back to your server when the connection returns.

Ghee connects over HTTPS or plain HTTP, works behind a reverse proxy, trusts a self-signed cert with one tap on first connect. Login is username and password, an API token, or OIDC, tested with Authentik and Pocket ID. Native-app OIDC login needed support in Mealie itself, so I contributed it. It landed in Mealie v3.23 and made passkey providers like Pocket ID work. Everything else works from Mealie v2.0 up. The request timeout is configurable for slow connections and VPNs.

Your recipes and lists go to your Mealie server and nowhere else. Crash reports go to Firebase Crashlytics so I can fix crashes. They carry the stack trace, device and app version, no user ID. Usage analytics are off unless you turn them on.

Free covers recipes, meal plans, shopping lists, cook mode, editing, import. Pro covers the on-device work beyond the free allowance above. Unlimited recipes on the device, the whole library in one tap, checking off shopping list items while offline. $9.99 one-time or $4.99 a year. The app is closed source and holds none of your data. Recipes and lists live in your Mealie server. Delete the app and nothing is lost.



App Store: [https://apps.apple.com/us/app/ghee-for-mealie-recipes/id6758328014](https://apps.apple.com/us/app/ghee-for-mealie-recipes/id6758328014)

Google Play: [https://play.google.com/store/apps/details?id=casa.dsen.ghee](https://play.google.com/store/apps/details?id=casa.dsen.ghee)



Custom-header auth for Pangolin or Cloudflare Access is not supported yet. What does your Mealie sit behind? Authelia, Authentik, Pocket ID, Cloudflare Access, Pangolin, Tailscale, plain LAN? I would like to know which setups I am missing.

## 评论（37/37）

**asimovs-auditor**（1 分） · 2026-09-17T01:43:44+08:00：

Thanks for posting to r/selfhosted. Your post has been temporarily removed. Please reply to this comment explaining how AI was used in the creation of your post/project. Once you reply, your post will be automatically approved. To learn more about why this is required, please see our [pinned post](https://www.reddit.com/r/selfhosted/comments/1sey9ch/quarter_2_update_revisiting_rules_again/).

**Fresh-Knowledge-8571**（3 分） · 2026-09-17T01:45:49+08:00：

Yes. I started this on my own last November with Flutter. I learned Flutter years ago and used it in some other hobby projects. At work, as a senior software engineer we have been using LLMs more and more every day. I started using these tools at home too, not to vibe stuff up but to gain typing speed without giving up proper human review and guidance. Every change to the app is steered by me and thoroughly tested, and re-tested over and over, until it feels polished. I never trust Claude blindly. All testing is on my real devices. I have switched between Android and iPhone over the years, so I have accumulated some older ones. I am also invested in the Mealie ecosystem and contributed the native OIDC login changes which are merged and released in v3.23 (https://github.com/mealie-recipes/mealie/pull/7804). This post was drafted with the same tool, my language and thoughts cleaned for readability.

**JackDaxter**（12 分） · 2026-09-17T01:53:38+08:00：

Oh that's a cool approach to extend an existing app! I've been creating my own named [Cuicuit](https://cuicuit.laclau.dev) 🐥, open source & self-hostable too, fully free. I'd say cuicuit focuses on an efficient UX to quickly get done with shopping.

**Kitchen_Employee833**（3 分） · 2026-09-17T02:54:13+08:00：

This looks awesome. Gonna check it out for sure

**Fresh-Knowledge-8571**（2 分） · 2026-09-17T03:22:16+08:00：

Thanks! What did you do in Cuicuit to make shopping quick? Always looking for ideas

**diazeriksen07**（5 分） · 2026-09-17T04:43:33+08:00：

The name Ghee sounds like it was originally for Tandoor :p

**Fresh-Knowledge-8571**（1 分） · 2026-09-17T05:28:43+08:00：

No, no Tandoor involved. It started as "buttermealie" when it was just for my family. I dropped the "mealie" so it would have its own name and "butter" became "ghee"

**No_Programmer5755**（3 分） · 2026-09-17T06:01:33+08:00：

curious about the OIDC contribution upstream, thats a solid way to build goodwill with an open source project while also unblocking your own app. does the offline queue handle conflict resolution if someone else modifies the list while youre offline?

**dkillers303**（3 分） · 2026-09-17T06:08:19+08:00：

It’s open source, go look

**mklatsky**（2 分） · 2026-09-17T06:32:22+08:00：

Checking it out and I have to say- it looks beautiful so far.

**mklatsky**（2 分） · 2026-09-17T06:33:27+08:00：

I’m going to have to look at this too. I think I have become an app hoarder. I love checking out new apps(whether truly new or just new to me). A

**AnyColorIWant**（1 分） · 2026-09-17T07:09:14+08:00：

This shits all over MealieSwift and Meshi.

**Fresh-Knowledge-8571**（1 分） · 2026-09-17T07:48:44+08:00：

Yes, the new OIDC endpoints unblock any mobile client, not just Ghee. I think haveing several companion apps out there is actually a plus, everyone can pick the one they like and fits their needs.

On the offline queue - it only carries the checked flag per item. On reconnect the app does 2 things - 1) refreshes the list and 2) applies each queued check (or uncheck) to the server current copy of that item, so names, quantities and other items are untouched. If someone toggled the same item while you were out, your offline toggle lands last and wins. If the item was deleted while offline, the toggle is not needed at all.

**Fresh-Knowledge-8571**（1 分） · 2026-09-17T07:54:09+08:00：

Thank you so much! This is my first app and I really wanted to keep it simple and clean. Shopping lists are actually inspired by Cozi app that we migrated off of.

**Fresh-Knowledge-8571**（1 分） · 2026-09-17T07:57:53+08:00：

Thanks!

**iiRooko**（2 分） · 2026-09-17T09:38:05+08:00：

Been using this for about 2 weeks. Great app!

**Command-Forsaken**（2 分） · 2026-09-17T11:11:32+08:00：

Nice. 👍

**Command-Forsaken**（2 分） · 2026-09-17T11:13:07+08:00：

Grabbed the app to have record. If I could only give my wife to use a phone app like Mealie instead of texting me recipes all the time…

**silkyclouds**（2 分） · 2026-09-17T13:35:25+08:00：

Heps are you on discord? I’ve worked on my own private app for the same reasons and will give a try to circuit today as it seems to check the boxes regarding my family needs. But I rather have a place to discuss the features ;)

**JackDaxter**（1 分） · 2026-09-17T16:39:20+08:00：

Oh cool, if you're interested we could join efforts! Would love to build a community to decide on the next features together, happy to chat on [Discord](https://discord.gg/guQDECXK7)!

**JackDaxter**（1 分） · 2026-09-17T16:40:18+08:00：

Thanks a lot! 🐥 If you have any ideas, happy to improve cuicuit with you by chatting on [Discord](https://discord.gg/guQDECXK7)!

**JackDaxter**（1 分） · 2026-09-17T16:41:39+08:00：

In addition to being fun, you really help new apps become useful to more people, thanks 😊 Happy to discuss improvements on [Discord](https://discord.gg/guQDECXK7)!

**igmyeongui**（2 分） · 2026-09-17T19:54:59+08:00：

Does it work on iPad as well?

Also Mealie is quite bad for automating the receipt scanning and I’ve switched to Norish.

It would be nice if your client was able to support multiple apps like Norish and Cuicuit.

**LeafyTurnipTop**（2 分） · 2026-09-17T21:42:18+08:00：

Hey, looking good! I'll definitely try it out.

Would it be possible that mealie URLs opened the correct recipe in the app?

**Fresh-Knowledge-8571**（1 分） · 2026-09-17T23:13:47+08:00：

Thank you!

**Fresh-Knowledge-8571**（1 分） · 2026-09-17T23:46:42+08:00：

Appreciate it. If she ever gets curious, a second user on your Mealie server is all it takes.

**Fresh-Knowledge-8571**（1 分） · 2026-09-18T00:21:44+08:00：

Yes, iPhone and iPad both.  
  
Ghee hands the link to your Mealie server, so it's only as good as Mealie's scraper, though recent versions of Mealie added a FlareSolverr fallback that helps with sites that block it. I haven't looked at scanning inside the app yet. If more people want it, please let me know here. I build what gets asked for most. Other backends are a stretch for now since the whole app is built around Mealie's ecosystem.

**Fresh-Knowledge-8571**（2 分） · 2026-09-18T01:03:03+08:00：

Thanks! For URLs - not from outside the app today.

Links inside a recipe already open in Ghee but a link in a browser still goes to the web page. iOS and Android only hand web links to an app for domains it declares when it's built. Every self-hosted server has its own domain/IP. A Share action could do it, so you share the link to Ghee and it opens the recipe. If more people want it, please tell me here.

**igmyeongui**（2 分） · 2026-09-18T02:13:13+08:00：

Norish isn’t built around the Mealie ecosystem though. They’re using a much more advanced receipt scraper. At first they had one as much as bad as the Mealie one but they recently switched to an official receipt scraper. It works really well now. I still have Mealie installed but it’s way behind speaking of the interface and scraping. 

You should give Norish a chance and I’m certain you’ll think about switching too. 

If your mobile client is compatible with many API backends you could probably make some great money. You can have a free tier and a paid tier with lifetime and monthly subscription. I like encouraging devs who makes clients for iOS in my case. I’ll gladly pay 20$ if it works great. But honestly right now the PWA of Norish is excellent. It’s only not using the official iOS navigation which feels less like an official app.  

I wish you good luck!

**LoganJFisher**（2 分） · 2026-09-18T02:54:43+08:00：

The app looks great, but some photos, which load just fine in Mealie, are refusing to load in this app. I'm not sure, off the top of my head, if these images might be a different image file type than the others, but I can't imagine I used anything unusual. This may be something to look into.

**Fresh-Knowledge-8571**（1 分） · 2026-09-18T05:19:06+08:00：

Thanks for the details! I'm keeping Ghee focused on Mealie (for now) but I'm interested in digging into how Norish handles recipe scraping.

**Fresh-Knowledge-8571**（1 分） · 2026-09-18T05:24:51+08:00：

Thanks for flagging this.  
  
Is it the recipe list, the recipe page, or both? Also, is it the same recipes every time? If you send it through "Contact Developer" in "Account" tab, the email fills in your app and OS version for me as well. Your Mealie version and how those photos were added would help too.

**LoganJFisher**（2 分） · 2026-09-18T05:45:20+08:00：

Mealie was on v3.14.0. I've now updated it to 3.27.0, and the issue is gone. Sorry for not checking that first. Perhaps that gives you something to note about the minimum version for proper compatibility though.

**Fresh-Knowledge-8571**（1 分） · 2026-09-18T12:25:06+08:00：

I was digging into this a bit more and stumbled upon this PR - https://github.com/mealie-recipes/mealie/pull/8276. It sounds exactly what you were experiencing. 

There are 2 concepts - the DB image field that keeps the image refs and the actual saved image on disk. Before that PR, DB was "allowed" to drift, so sometimes image refs were lost. The old Mealie Web UI always requested the image by recipe ID and fell back to a placeholder on "not found", so a lost ref never mattered there - this is why you saw no issues in Web. Ghee trusts the DB ref instead, and since that PR the Web UI does the same, which is why the PR also ships a migration that rebuilds the refs from the files on disk. 

Long story short - this is patched in Mealie and your move to the latest version ran that migration and corrected DB.

**igmyeongui**（2 分） · 2026-09-18T13:00:54+08:00：

Honestly Mealie should just trash their scraper and use that scraping library and add Ai. It just works. BTW you can quickly deploy Norish for testing and import your whole mealie in few clicks.

**cuntywunty69**（1 分） · 2026-09-19T10:39:55+08:00：

Installed today after saving the post for a while. Looks pretty good mate. I have my Mealie set up with reverse proxy, so I can access all my recipes away from home anyway. I reckon I'll get Pro anyway to support your work. Good stuff mate 👍

**Fresh-Knowledge-8571**（1 分） · 2026-09-19T11:17:58+08:00：

Thanks, glad it works well with your setup. Really appreciate the support.

## 关联链接

- https://play.google.com/store/apps/details?id=casa.dsen.ghee

## 导航

- 项目页：[[80-归档/项目/apps.apple.com_dc4ce706]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
