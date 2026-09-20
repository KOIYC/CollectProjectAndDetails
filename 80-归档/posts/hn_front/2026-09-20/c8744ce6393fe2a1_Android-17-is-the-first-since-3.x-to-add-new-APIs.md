---
type: "corpus"
item_id: "c8744ce6393fe2a1"
title: "Android 17 is the first since 3.x to add new APIs without releasing to the AOSP"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49758736"
project_url: "https://grapheneos.social/@GrapheneOS/117282080803799576"
author: "theanonymousone"
published_at: "2026-09-18T19:03:09Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_theanonymousone
  - story_49758736
  - front_page
metrics: {"points": 1050, "comments": 609, "engagement_velocity": 1050}
comments_count: 605
comments_total: 605
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# Android 17 is the first since 3.x to add new APIs without releasing to the AOSP

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49758736
- **指标**：点赞=1050 · 评论=609 · engagement_velocity=1050
- **作者**：theanonymousone　|　**发布**：2026-09-18T19:03:09Z
- **项目链接**：https://grapheneos.social/@GrapheneOS/117282080803799576
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`c8744ce6393fe2a1`

## 正文

Published: 2026-09-16

GrapheneOS: "Android 17 QPR1 is the first r…" - GrapheneOS Mastodon

#### Administered by:

admin

@admin

GrapheneOS

@GrapheneOS@grapheneos.social

Android 17 QPR1 is the first release since Android Honeycomb (3.x) adding new APIs for app developers without a release to the Android Open Source Project. The new APIs are currently exclusive to the Pixel OS and aren't available to other Android OEMs.

https:// developer.android.com/sdk/api_ diff/37.1/changes

developer.android.com API Differences between 37 and 37.1 JDiff is a Javadoc doclet which generates an HTML report of all the packages, classes, constructors, methods, and fields which have been removed, added or changed in any way, including their documentation, when two APIs are compared.

Sep 16, 2026, 02:15 PM·· Web 30 boosts· 2 quotes· 63 favorites

GrapheneOS

@GrapheneOS

11h

Non-Google Android OEMs and AOSP-based projects can ship yearly and QPR2 releases. There are also security backports to those releases. Security preview access is needed to ship patches without months of delay. We've had that since before our Motorola partnership via another OEM.

GrapheneOS

@GrapheneOS

11h

We already ported our code to Android 17 QPR1 since before it was released on September 15th but don't have permission to release it yet. We're working on backporting Pixel firmware, kernel drivers, userspace drivers and HALs from Android 17 QPR1 to Android 17 for now instead.

GrapheneOS

@GrapheneOS

11h

Pixel Update Bulletin for September 2026 has additional patches to standard Android platform components used by non-Pixel devices. These patches are relevant to non-Pixel devices but haven't been made available via the September 2026 Android Security Bulletin or preview patches.

GrapheneOS

@GrapheneOS

11h

Google should not be gatekeeping security patches to the standard Android platform code from Android OEMs but that's what they've started doing. Other OEMs will get these patches in December 2026 via Android 17 QPR2. We can ship them early by reverse engineering the code instead.

GrapheneOS

@GrapheneOS

11h

It would be interesting to know if Google's legal team is aware they're giving Pixels months of early access to new Android features and bug fixes including certain important security patches. Pixels being given this competitive edge over Google's OEM partners is very dubious.

GrapheneOS

@GrapheneOS

11h

Google is also once again failing to comply with our GPL source requests for weeks. We requested CD1A.260905.001.A1 sources on September 1st and were only provided access today. The kernel build IDs are the same for 17 QPR1 Beta 9 and 17 QPR1 so we have that already at least.

GrapheneOS

@GrapheneOS

11h

We could have shipped an Android 17 QPR1 update already since our port was completed. Instead, we have to deal with ongoing pain until Android 17 QPR2 is released in December 2026. This will not be an issue for Motorola since we'll have official firmware and driver code provided.

GrapheneOS

@GrapheneOS

11h

Pixels are now significantly harder to support than many other devices. One of the only advantages of Pixels is now a disadvantage instead. They're still the best fit for us due to the updates and security features but it burns time we want to spend on privacy and security work.

GrapheneOS

@GrapheneOS

10h

It will be far easier for us to support upcoming Motorola devices than Pixels. Qualcomm will hopefully expand MTE support beyond the highest end flagship SoC soon so we can expand to more than flagships. Pixel 11 didn't remove it from hardware, only firmware, so that's good news.

Daniël

@danieldk@mastodon.social

11h

@ GrapheneOS Are these APIs used for features that are only available in Pixel OS to differentiate it?

I assume that they will be pushed to AOSP as Android 17 QPR2?

@GrapheneOS

11h

@ danieldk No, these are standard Android APIs included since Android 17 QPR1. These will be available through AOSP and other OEMs via Android 17 QPR2 in December 2026. It's currently exclusive to Pixels because it was released as part of Android 17 QPR1 since QPR1 and QPR3 releases are now Pixel exclusive since Android 16.

This is simply the first time they've added APIs in a QPR1 or QPR3 release following no longer releasing QPR1 and QPR3 to AOSP after the release of Android 16.

ṫẎℭỚ◎ᾔ ṫ◎ℳ

@TycoonTom@infosec.exchange

11h

@ GrapheneOS @ danieldk 🤔 👌🏼 👍🏼

 0

Boost or quote

outst☆r

@outstar@mastodon.social

11h

@ GrapheneOS I assume this is not good news?

Maya

@skyblitz@ieji.de

11h

@ GrapheneOS yep google locking down android even more.

would not suprise me they kill AOSP altogether in some years

Albi 🇵🇱 

@Albi@furry.engineer

10h

@ GrapheneOS Is Motorola willing to be as open as google was with Pixels, or do they see it as an opportunity for good press?

Fazal Majid

@fazalmajid@vivaldi.net

5h

@ GrapheneOS will Motorola’s folding phones be included?

Solomon Schuler

@sschuler@mastodon.social

8h *

@ GrapheneOS logistically speaking, how would graphene operate for locked Motorola phones? Have you found a work around for that?

UninterestedNerd

@UninterestedNerd@mastodon.social

7h *

@ sschuler @ GrapheneOS if a phone has been locked to a carrier at any point in it's lifetime, 9 times out of 10, the bootloader is permanently locked. There's nothing the gos team can do about that. There are exceptions which are rare, but carriers almost always permanently lock the bootloaders on phones they sell you. Some older phones have firmware cracks to re-unlock it, but that's also a rare occurrence with modern phones.

taraxippos

@taraxippos@mstdn.business

10h

@ GrapheneOS are you already planning to drop the support for pixel phones?

GrapheneOS

@GrapheneOS

9h

@ taraxippos No, and we still plan to support the Pixel 11 series as long as it gets fully functional MTE support.

emon

@emon@masto.top

10h

@ GrapheneOS maybe a good thing in the end. It quite bothered me to buy a google phone to get a degoogled and secured phone.

tofudude 🌱

@tofudude@veganism.social

10h

@ GrapheneOS > Pixel 11 didn't remove it from hardware, only firmware, so that's good news. So performance could be okay if you tinker around with the firmware?

GrapheneOS

@GrapheneOS

@ tofudude Performance appears to be fine for MTE on the Pixel 11. We don't know which it was completely removed from firmware and disabled at launch. It's added back to firmware but still disabled in Android 17 QPR2 Beta 4 which was released after our initial thread about it. We used that to enable it and test it. It passes all our tests and other standard tests. We benchmarked it and the performance is fine. There may be cases where it has higher overhead but the faster CPUs make up for it.

10h

@ GrapheneOS I really hate Google more and more. Unfortuntaly because they do that, I bought a pixel because i care about my privacy and security, and now I would have to either buy a motorola phone in like 1-2 years because google stops letting us install custom roms... I am not saying i don't like motorola, they are making great phones but yeah... wish you the best in the project and the collab with motorola

Elias Adler

@sapash@privacysafe.social

9h

@ EUCommission 

Worth checking : a potential abusive anti-competitive practice from Google.

Neil Van Dyke

@neilvandyke@mastodon.online

10h

@ GrapheneOS Is it even worse than merely contractual or regulatory?

With today's AI-powered rapid reverse-engineering, isn't releasing a security fix tantamount to disclosing the vulnerability to threat actors?

If so, doesn't availability of fixes for only some affected Android devices constitute irresponsible/negligent/malicious disclosure for the rest?

GrapheneOS

@GrapheneOS

10h

@ neilvandyke 

> With today's AI-powered rapid reverse-engineering, isn't releasing a security fix tantamount to disclosing the vulnerability to threat actors?

Yes, and we can reverse engineer it ourselves to ship it before December 2026 s

# Saving another 100TB of RAM with math (and Rust) | Cloudflare Blog

## 评论（605/605）

**ahmd-sh** · 2026-09-18T19:39:25.000Z：

i despise where Google is going with this. it's a duopoly in the smartphone OS space and we need (for lack of a better analogy, spare the technicals) open-source distros like we have with Linux on desktop.Graphene is reaching that status for me every day and i'm looking forward to switching to it as my daily driver.

**VCFundedGenYer** · 2026-09-18T19:43:50.000Z：

Android has been so thoroughly disappointing through the years. Started as a great open free form alternative to iOS, to becoming the very thing it sought to combat.

**wps** · 2026-09-18T19:45:10.000Z：

The amount of roadblocks Google is putting up for GrapheneOS is just ridiculous. None of their decisions make any sense, from the delayed source patches upstream, to the embargos, attestation issues, etc. Google simply regrets android being open source.

**petcat** · 2026-09-18T19:52:26.000Z：

Does anyone contribute to AOSP besides Google? Does Google actually accept any patches into "upstream" and ultimately into their own commercial distro?

**vkaku** · 2026-09-18T19:57:25.000Z：

Many developers will likely be developing at Android 16 APIs only. Will rely on Aptoide+AOSP exclusively. This is likely the timeline we'll see a decline in Play Store and Pixel usage.

**Ajedi32** · 2026-09-18T19:59:10.000Z：

Important details further down: https://grapheneos.social/@GrapheneOS/117282129725629495So it seems like the problem isn't that the new API is Pixel exclusive, but that the first and third quarterly release patches each year are Pixel exclusive?

**Velocifyer** · 2026-09-18T20:04:28.000Z：

This is confirming my belies that Google is trying to block OEMs that don't pay them to be part of GMS, with the goal of eventually being the only android phone maker.

**xnx** · 2026-09-18T20:06:43.000Z：

The world needs a Steam Phone.

**hagbard_c** · 2026-09-18T20:15:40.000Z：

Fine, whatever but no Android 17-derived Google-free AOSP distribution for me if these APIs are in any way essential to the functioning of the device or required by one or more of the government/bank-mandated applications which are sometimes needed. If they are in any way related to some Google service I don't care since I don't use those anyway.

**barbazoo** · 2026-09-18T20:15:47.000Z：

I'm on GrapheneOS and I will never go back to Google Android or iOS. The amount of control you get is just liberating. I hope Google doesn't crush them.

**natterangell** · 2026-09-18T20:19:27.000Z：

I get the sense Android is going the way of MacOS and Darwin. At some point Google will release something non-free end users experience as an absolutely integral part of OS, and it won't be possible to continue as an equivalent alternative. AOSP will still be free and underlying the whole thing, but slowly rot away as anything more than a code base.

**IronWolve** · 2026-09-18T20:19:35.000Z：

I'm going to guess that google is afraid of the age of AI, they should be, those API's will be reverse engineered pretty quick. Lots of bad actors will using AI.We live in a time, if you want to build an android app, you easily can, but installing will be harder due to google concerns.

**largbae** · 2026-09-18T20:23:44.000Z：

Alright AI maximalists, what's the estimated token budget to remove the Google dependency?GrapheneOS has the bootable AOSP and will have Google-alternative device support.We probably need an equivalent to Play Services, app signing/porting/publishing tools.With these in hand could we talk Valve into providing the scalable alternative to the play store?

**Onavo** · 2026-09-18T20:29:19.000Z：

So...if you vibe code API shims Google can't sue your right? It would be clean room implementation by definition.

**teekert** · 2026-09-18T20:29:40.000Z：

Installed GrapheneOS on my Pixel 10 yesterday, only used the stock rom to start the installer... Am feeling a little unconfortable due to this situation: [0]. Hope this gets better. Really feeling the dislike for Google on this one.[0]: https://news.ycombinator.com/item?id=49741510

**exabrial** · 2026-09-18T20:30:02.000Z：

Someone please make a linux-based, using proper cgroups/containers for app isolation, where programs are one of: regular JVM ByteCode, or WASM. APIs follow a JEP-style Process with multiple incubators until we got it right.

**bri3d** · 2026-09-18T20:34:04.000Z：

So, the real thing that's happening here is:* Google drop "real" Android source-code updates to OEMs _and_ the public every half.* But they ship four Pixel updates, including documentation + SDKs.* Now they added new APIs in a Pixel-only update.* Google also drop security update backports to "trusted" OEMs monthly (which GrapheneOS have had access to for years).So, there are now Pixel-exclusive app features on the Pixel SDK version which isn't available to OEMs - but, it's highly unlikely any app developer would actually depend on these new APIs, since Pixel marketshare is tiny to begin with. This in essence just makes Pixels a weird beta-testing device for what will come out a quarter later to "normal" devices, which is sort of an odd business decision, but also a weird thing to get really mad about, in my opinion (I do see what GrapheneOS are trying to do, with having OEMs saber-rattle about not getting features on the same cadence as Pixels, it just doesn't resonate very loudly for me).However, the API headline seems to bury a deeper lede; in the thread, GrapheneOS also claim that the quarterly Pixel releases contain security content which is not appearing in the monthly backports. This is quite bad and very sloppy if true, since the Pixel releases can easily be patch-diffed and exploits backed out of them. I'd be interested in seeing this enumerated in more depth.

**shevy-java** · 2026-09-18T20:39:33.000Z：

One can not simply trust Google. While I personally like the MIT licence more, I think it is time that the GPL or variants of it (Affero etc...) get used a lot more. It worked very well with the Linux kernel. Corporations keep on abusing this.

**dingdong2026** · 2026-09-18T20:39:39.000Z：

Google is a cancer on humanity.

**ironqcold** · 2026-09-18T21:14:46.000Z：

Google is increasingly locking down Android. I wouldn't be surprised if they killed off AOSP entirely in a few years...

**palata** · 2026-09-18T21:20:23.000Z：

Google managing to get worse every day.

**claudiojulio** · 2026-09-18T21:28:53.000Z：

Forget Android. The future is Plasma Mobile.

**matheusmoreira** · 2026-09-18T21:54:25.000Z：

I wonder how low Google will sink next time.Respect for the GrapheneOS for pushing through regardless, even if they have to reverse engineer stuff. Can't wait to buy their phone.

**jokoon** · 2026-09-18T22:28:27.000Z：

I mean, even if android is/was open source, it was always fastidious to build a de-googled android image for a phone model.Of course it's not great for their business model. Not to mention, no more trustworthy app distribution.I don't see the EU really being able to forcing them to de-google android phones.I am also curious how much those phones would cost, BTW, since the cost calculation to release such an OS would be a bit complicated.

**jauntywundrkind** · 2026-09-18T22:38:20.000Z：

Worth reminding folks that the EU DMA Act is forcing Google to start unlocking some of their APIs, such as the AI services AI. Right now a bunch of the apis for digital assistants/chat stuff are kind of proprietary, and this is demanding interoperation. August 1, 2027 is the deadline for most of this (but open access to hotword listening capabilities is slated for Aug 1, 2028).https://digital-markets-act.ec.europa.eu/developer-portal/in...Side note, that API here is HID. USB HID is so cool. There's so much stuff in this spec! Chargers and batteries can both communicate all kinds of status, which, well, afaik no one does, there's all kinds of sensors. It's this ancient spec that has so much, and weirdly is just so far ahead of where we are. More HID on Android will be great. Wish they'd played with others to make this so though!

**HumblyTossed** · 2026-09-18T23:22:04.000Z：

GrapheneOS scares them.

**QuantumGood** · 2026-09-19T00:06:23.000Z：

AOSP = "Android Open Source Project"

**publlus_enigma** · 2026-09-19T00:17:29.000Z：

As someone who went through similar challenges with Google making it impossibly hard for BlackBerry to provide an Android runtime on BBOS10, and now running GrapheneOS, I trust Google exactly zero to do the right thing by any open source project it stewards. Combined with their other practices, and lack of ongoing support for their commercial offerings, means that my perception of them is irreparably damaged and I minimise my usage of their products as much as practicably possible.

**charcircuit** · 2026-09-19T00:59:53.000Z：

Thank god that AI is progressing well enough that agents can figure out most of the changes and do the reverse engineering to get this stuff, but it's introducing a lot of inefficiency to the ecosystem that doesn't change the final outcome.

**DrewADesign** · 2026-09-19T01:10:04.000Z：

Look at that dev productivity go! The continually softening job market means c-suites everywhere care less than ever about their company’s image among developers. They’re surely thrilled to stop pretending to give a shit about anything beyond the next few quarters’ stock prices and their bonuses.

**rustcleaner** · 2026-09-19T01:14:14.000Z：

Android is irrelevant to me, there is only GrapheneOS.Go bankrupt, Alphabet!

**Ritewut** · 2026-09-19T02:29:40.000Z：

I would love to know what alternative phone OSes exist. I would happily throw money and my engineering weight behind a promising project.

**hacker_homie** · 2026-09-19T03:49:10.000Z：

I'm so glad we stopped microsoft from shipping a browser with their OS in the 90s, <sarcasm/>.Regulate them! that is the only way.Their should be a path for an AOSP build to be just as privileged as a google signed build.

**fithisux** · 2026-09-19T03:57:39.000Z：

Google is a for profit company. It does what it needs to stay profitable.
Are the actions of Google moral? No!Governments are paid out to not intervene. They should have stepped in decades ago. They should have made Google to release source code and interoperate with public services. They already make profit from their services.

**soleil-colza** · 2026-09-19T04:54:44.000Z：

Feels like the "Pixel = reference implementation of AOSP" relationship is starting to erode.

**m4rtink** · 2026-09-19T07:36:53.000Z：

Android really going for the gutter recently.

**linzhangrun** · 2026-09-19T07:55:40.000Z：

How surprising.

**cton** · 2026-09-19T08:29:58.000Z：

Out of curiosity, do closed APIs mean OEMs can’t fuck them up or at least limit how much they can?

**VerifiedReports** · 2026-09-19T09:58:15.000Z：

The fraud of Android just gets worse.The great "open-source" OS that was supposed to free us all from vendor and telco tyranny has... not.

**solarkraft** · 2026-09-19T10:45:04.000Z：

I jumped ship to iOS a few years ago. Android is a strictly worse experience on all accounts with clear ambitions to be just as unfree as iOS, so there is just no point.

**tomaskafka** · 2026-09-19T11:09:32.000Z：

Embrace, extend, extinguish, and old playbook.

**tyrabound** · 2026-09-19T11:09:48.000Z：

Ah, the classic con job is starting to close its cycle. Get who-knows-how-many-millions-of-dollars of free work and thought, and then when the free labor has finally elevated you above it and your power is overwhelming, you simply just crush the gullible peasants beneath you and act like they never existed.People thought they were part of some collaborative, good of the world type effort, when the reality is that there were always ulterior and hidden motives to manipulate and exploit that gullible and rather foolish nature of Americans in particular; a foolishness that has long, if not always existed in the genuine American core character, but at the very least was cultivated and even selected for a long time ago.How do you motivate people in modern times to do free labor for you as the parasitic ruling class without the threat or resort to violence? You of course trick them into believing that what they are doing or support makes them a good boy, regardless of all the evidence and proof to the contrary.

**LelouBil** · 2026-09-19T11:25:24.000Z：

Still waiting on the Motorolas with grapheneOS support to ditch my 7 years old phone.

**pino83** · 2026-09-19T11:42:23.000Z：

The next cat and mouse game you are going to lose.

**saidnooneever** · 2026-09-19T11:52:37.000Z：

its kind of amusing in a wag degoggling requires pretty much a phone from google :') by the comments on those post. bit unrelated to this post ofc but thought and wondered if they do that on purpose and how far these devices really get reverse engineered to see if they are actually de-googled down to the chips. just having a different OS doesnt have to mean anything in that regard if the entire device is owned by them -_-.especially since its radio and thats not too easy to determine if a device is or isnt sending weird stuff. (dont come with the lte or wifi sniffers or such things. u'd need thorough spectrum analysis during operations on a quite broad spectrum too to rule that out. the antennae in the devices can produce a lot of types of signals... or do they decap the chips and reverse those to see whats in it? i doubt it would be possible at the right scale but theres options i guess.people in certain regions/ high assurance security work roles will do this to hundreds of devices that are identical to try and determine if a supplier is compromised or not. order a full batch, take em all apart. taking x-rays, dissolving chips package, etching layers one by one, taking pictures with electron microscopes etc, probing bond wires in the packages as they run etc etc.somehow i dont see some OS creator do all of this, but ofc i could be very wrong :). interested to find out why people think google while with a different OS is truly de-googled or if they kinda just hope for the best...

**TeMPOraL** · 2026-09-19T12:37:50.000Z：

Graphene OS is the odd one, I don't know what to make of it. It seems to be the only entrant in the mobile OS space that has a remote chance to work as alternative OS for daily use - but it's optimizing directly for the philosophy opposite to what I hoped it would be, I.e. it's focusing on privacy and security. Which AIUI means also securing the device against its owner, much like the big players do.I hoped we'll get an OS more amenable to opening up the device, exposing its capabilities to the owner, but alas, I fear there is no way for an OS to survive in this space unless it acts the same way the Big Two do. As it is, I can't help to think that Graphene is just the same as Google and Apple: just another security-maximizing vendor owning your computer.

**jauntywundrkind** · 2026-09-19T14:53:59.000Z：

Oh! These are HID! I wonder if this is for Pixel, or if this is something they had to shoehorn in fast to make Chromebooks work?

**varispeed** · 2026-09-19T15:42:16.000Z：

At this point there is no point buying into Android if it becomes the same walled garden as iOS.

**cromka** · 2026-09-19T15:47:39.000Z：

I don't get why this is a discussion around Open Source, they also seem to have f*caked over other OEMs? Can't imagine Samsung will be OK with it.

**mahboi** · 2026-09-19T16:01:56.000Z：

This news in particular seems similar to the other Android phonemakers like Samsung. They have their own custom Android forks that aren't open source. Maybe Google is wearing two hats here, Android and Pixel?But if Pixels are getting early access to security patches too, that's more like one hat.

**julio2445** · 2026-09-19T18:11:25.000Z：

Jsjsjsksk

**jonesn11** · 2026-09-19T18:24:16.000Z：

Android 17 is swagged out lol

**pojntfx** · 2026-09-18T19:44:21.000Z：

GrapheneOS is pretty neat, https://postmarketos.org/ is also pretty damn polished out of the box these days. I'd argue the "mobile desktop Linux systems" are actually a bit more polished than Graphene, esp. when it comes to default apps (no AOSP abandonware dialer, contacts etc. apps to fight with, it's all just maintained, responsive GNOME/KDE apps)

**kenhwang** · 2026-09-18T19:52:54.000Z：

I just wish Graphene had better support for non-Google hardware.

**b112** · 2026-09-18T19:54:42.000Z：

If Google doesn't smarten up, it will no longer be in control of Android.Oracle was a mighty powerhouse when it bought MySQL, StarOffice, and more. It lost defacto control of all of them, due to its stupidity. In the world of open source, the tighter you hold on, the less likely you'll retain control.And yet, here we are, with Google playing games.Google, a note: there are far more relying upon Android than you, and now there are forced alternative stores in the mix. If Samsung and everyone else said "sorry Google', or even a large majority, you're out. Gone. Nada.They can now fork, and force old Android to have their new fancy pants 'Play' store too.Google is also getting more and more pushy with Chrome. What if everyone depending upon that backend, shrugs and says "Sorry Google, we're hard-forking Chrome and we'll all maintain it".

**austinthetaco** · 2026-09-18T20:07:28.000Z：

i so desperately wish we were still in the days of manufacturers making their own OS. It's why I moved to iphone: when the hardware company makes the software and vice-versa the integration is much better and less error-prone/bloated. It never made sense to me for android to be shoehorned into thousands of devices, instead of a fork being made and for thorough OS rework to happen to support the device.

**aftbit** · 2026-09-18T20:10:57.000Z：

Graphene has been my daily driver for the past year or so. The only thing I miss is the ability to do contactless payments. Otherwise, it's been awesome. I don't run any games nor do I care about any of the AI features. YMMV.

**josteink** · 2026-09-18T19:45:42.000Z：

If Android wants to be the inferior not-open-source mobile OS, why would I not just buy an iPhone instead then?It’s closed too, sure, but at least it’s more consistent.

**fgonzag** · 2026-09-18T21:29:18.000Z：

I had never considered using lineageos and the like, but honestly the writing is on the wall. Google is going straight into a closed AI device.I'm going to start donating to a few free android distros I guess, I'm probably going to be trying them sooner rather than later, and without AOSP support the dev burden is going to be much higher, and it probably means they'll end up diverging and incompatible at some point (not in both directions, lineage will probably always have to have Android app support)

**monomania** · 2026-09-18T19:50:36.000Z：

There's a non-zero chance that three-letter agencies are lobbying for at least some of this.

**bebeirjd848r** · 2026-09-18T19:53:35.000Z：

GrapheneOS does not even register on Google scale! It does not
 even manufacture its own devices!Bigger problem is HarmonyOS and similar devices, compatible with Android. Opensource threat from china!And no NSA backdoors or honeypots!

**7734128** · 2026-09-18T19:54:56.000Z：

It's not a regret. Android would never have been popular in the first place if it had not been open source. If phone makers had been able to anticipate how much the demons at Google would be able to lock down the Android then they would never had used the OS back in ~2009.

**Retr0id** · 2026-09-18T19:58:54.000Z：

Google is also seriously dropping the ball in terms of security. The CVE-2026-43499 root LPE (aka ghostlock) is still unpatched across all Pixel devices, on the latest """security""" update, despite weaponized exploits being public for months.

**jeroenhd** · 2026-09-18T20:17:50.000Z：

The thread states that Google is putting out patches that affect other Android vendors too.They're not treating GrapheneOS very differently from other vendors, except that Graphene isn't relevant enough to sign a contract with because they don't make phones (or money, really).Google should be putting out the code and patches like they used to, but the constant badgering of Google on this issue feels off. I don't see anyone complaining that Samsung isn't supporting their security-focused fork enough, or complain that Apple is delaying the bootloader unlock process by a day.Despite their very worst, selfish intentions, Google is the very best vendor of commercial open source software. While Google's open source project collapses, there's plenty of space for other vendors to step in.We should bemoan Google's fall from grace, but only because they're on the way to becoming just as bad as every vendor but Librem if they keep this up another decade.

**alightsoul** · 2026-09-18T20:22:02.000Z：

It's a net loss. Less data and in their view makes development harder.

**curiousgal** · 2026-09-18T20:30:44.000Z：

> GoogleCan we just stop saying "Google" as if it's same faceless org? No, it's not Google, one or two asshole execs are behind this policy.

**godelski** · 2026-09-18T20:32:21.000Z：

I hope people remember this when advocating for chromium. Just because it is open source doesn't mean they don't control it. We need to start the long process of hard forking now or turn to alternatives like Firefox as a new foundation. > Google simply regrets android being open source.

Android wouldn't be what it is if it wasn't open source. With all the work from outside Google. The same is true chrome.But they won't learn that on their own. They are breaking the deals. So we move. We force their hand

**dimaaan** · 2026-09-18T20:40:11.000Z：

And don't forget about Manifest V2/uBlock Origin removal!

**yndoendo** · 2026-09-18T21:07:06.000Z：

It makes perfect sense when you apply the Friedman doctrine to their actions. [0]Google is a lawn mower, stop anthropologizing them. This goes the same with Apple, Microsoft, Meta, Amazon, ...[0] https://en.wikipedia.org/wiki/Friedman_doctrine

**bossyTeacher** · 2026-09-18T23:06:28.000Z：

> None of their decisions make any sense,Of course, it does. Google is no longer afraid to spit on open source. People happy to use Chromium features better remember this. You are renting everything and your landlord will soon come demanding it back.

**rkagerer** · 2026-09-18T23:26:47.000Z：

Yeah I have trouble accepting it's pure coincidence this occurs just as GrapheneOS is starting to gain some noticeable traction.

**karlgkk** · 2026-09-19T00:44:11.000Z：

> None of their decisions make any senseIt only doesn’t make sense if you’re assuming conspiracy.It makes a lot more sense if you assume they just don’t give a shit.

**mitxela** · 2026-09-19T00:51:42.000Z：

When you realize that keeping people on proprietary mobile OSes is a matter of national security it makes more sense. The USA spares no expense for national security.

**_blk** · 2026-09-19T01:09:17.000Z：

It's not that it doesn't make sense, you just said it, they regret - well maybe not regret since they'd never made it without, but they now want to reverse a decision they feel needs to be overhauled.
I always thought they'll replace Linux with Fuchsia but that hasn't happened and it's not like they couldn't have done it.

**Telaneo** · 2026-09-19T02:11:38.000Z：

I'm convinced Android being open source is just an accident of history. It's been somewhat useful for Google to be able to ride on that goodwill, but they're not actually invested in open source beyond the ways it directly benefits them (or at least they haven't been in the last 10 years). Thus they're happy to throw the baby out with the bathwater if they believe they need the bathtub for anything that will earn them 0.1 cent more than that baby would.

**taneq** · 2026-09-19T02:23:01.000Z：

If someone’s (or some company’s) decisions don’t make sense to you, you don’t understand their motivations.

**surajrmal** · 2026-09-19T03:34:24.000Z：

There was a split world for a long time even before the more recent changes because of the need to hide secret new features or products from the general public. It was always a tricky arrangement. They just decided one day that there wasn't a lot of folks contributing that lacked access to the private repos, so they might as well just switch all development to occur in that place. Honestly, it's somewhat rationale. If there was a significant number of folks contributing to Android without such access I'm sure that wouldn't have happened. We didn't lose as much as folks think we did given the code drops from the private repos still happened even previously.

**varenc** · 2026-09-19T03:36:58.000Z：

> Google simply regrets android being open source.Could Google backtrack on this if they wanted? If they suddenly decided to stop releasing public code updates, what would they be violating? I can guess: Anti-trust maybe. probable at least contractual commitments Or is there some stronger forcing function?

**binkHN** · 2026-09-19T05:08:46.000Z：

They want to be like Apple here and lock things down. Remember SMS? The ubiquitous text messaging protocol that had an API that developers could access? Now, the latest standard, RCS, is locked down with no API and behaves just like iMessage. Ring any bells?

**sporkland** · 2026-09-19T05:33:56.000Z：

As an outsider in a hyper competitive commercial space like mobile os (apple, android) which part makes you think it's active obstruction and not just moving fast and trying to keep up, get ahead, etc and they want the open source side but it's a lower priority?

**zx8080** · 2026-09-19T08:05:31.000Z：

> None of their decisions make any sense ..What? Google is advertisement business. Not a software house. They sell ads. It all makes sense to build a walled garden. They are effectively a monopoly for half of the personal devices _in the world_. And they _will_ return their investments into the opensource. By locking Android and Chrome and showing ads to everyone.Like the old days shitty TV, full of ads.

**zx8080** · 2026-09-19T08:39:22.000Z：

> Google simply regrets android being open source.

No, they are benefitting from it! They gained some trust and removed competition from the horizon. Now they are locking the platform down to do what their business is about: displaying ads.

**mrbluecoat** · 2026-09-19T14:22:19.000Z：

> Pixels are now significantly harder to support than many other devices. ... It will be far easier for us to support upcoming Motorola devices than Pixels.The Motorola transition can't come soon enough, IMHO

**illiac786** · 2026-09-19T14:51:46.000Z：

Well, based on your last sentence these decisions very much make sense.But I agree with the other comments out there. It will get ugly and they will loose. I am convinced there many heavy weights just waiting for the right time to hit google hard on this. While I don’t know all of them and don’t like the ones I think I know, I will sing and dance when it’ll happen.And no, Apple is no better.

**nzeid** · 2026-09-18T20:00:04.000Z：

The phrasing of your first question is ironic given GrapheneOS has upstreamed a ton of their security hardening.You're probably asking if they're able contribute anymore?

**justdeko** · 2026-09-18T20:49:31.000Z：

quite a few manufacturers do, specifically in the automotive sphere and ofc samsung etc.in terms of accepting, unless it's stuff like bugfixes to core mechanisms, not really.

**DaSHacka** · 2026-09-18T20:10:39.000Z：

You vastly overestimate how many people care (developers included) outside of FOSS and HN circles.Nothing will happen, as it never does.

**tiagod** · 2026-09-18T20:13:21.000Z：

Pixel market share is and always has been absolutely tiny, and the people that care about this are a rounding error.

**grapheneos** · 2026-09-18T20:11:07.000Z：

QPR1 and QPR3 are now Pixel exclusive since Android 16. That means the new APIs for app developers added in Android 17 QPR1 are Pixel exclusive until Android 17 QPR2. There hasn't been a case of new APIs for apps not being open source or not being available to every OEM since Android Honeycomb (3.x).

**Insimwytim** · 2026-09-18T20:18:13.000Z：

No, these are standard Android APIs included since Android 17 QPR1. These will be available through AOSP and other OEMs via Android 17 QPR2 in December 2026. It's currently exclusive to Pixels because it was released as part of Android 17 QPR1 since QPR1 and QPR3 releases are now Pixel exclusive since Android 16.
 This is simply the first time they've added APIs in a QPR1 or QPR3 release following no longer releasing QPR1 and QPR3 to AOSP after the release of Android 16.

**fsflover** · 2026-09-18T20:13:09.000Z：

If you mean GNU/Linux phones, they already exist and can be used as daily drivers by technical people. Sent from my Librem 5.

**crossroadsguy** · 2026-09-19T03:21:11.000Z：

It sure needs a large enough push from one of few big companies (with their explicit backing) that can bring businesses to support other app store(s). But imho that has to happen in a way that it doesn't create a need to write and publish apps in yet another language to yet another platform. Because if businesses have to do that as well that will be a good way to ensuring it becomes a DoA effort.I've a feeling companies like Meta, Amazon, Steam are well placed to do this (esp. Meta and Steam). But not sure it will be helpful to them in any way, besides they'd want to ensure their own control and locks.

**fschuett** · 2026-09-19T08:57:31.000Z：

Does the Brax Phone fit?

**alt227** · 2026-09-19T17:50:11.000Z：

They already are.

**z3ratul163071** · 2026-09-18T20:33:49.000Z：

exactly

**IshKebab** · 2026-09-18T20:35:51.000Z：

A lot. But I don't think you can do it with just tokens. Android without the Play store and Google Play Services is just not very useful (in the West anyway).

**alightsoul** · 2026-09-18T20:44:05.000Z：

The token budget isn't to remove Google it's to create drivers for individual phone hardware, which phone and chip manufacturers keep closed source. Also it would be used to find exploits to unlock permanently locked bootloaders

**the_real_cher** · 2026-09-18T20:57:43.000Z：

What's the token budget to build a new phone OS?

**aesh2Xa1** · 2026-09-18T20:58:30.000Z：

GrapheneOS accepts donations and, to my knowledge, they spend it in hiring full time engineers.They have replacement portions for Play Services already (attestation, an app store, and location), but it'd be interesting if they also offered something for push notifications.If you have it to give you can spend your budget on a donation and fund the effort directly.

**throe939r** · 2026-09-18T21:03:30.000Z：

Buy HarmonyOS device. No google jumk, android compatible os, fdroid works, years of security updates from maker, and 40% lower price.As a personal device it works pretty well. For ssh terminal and reading markdown, it has by far best display.

**cecexacjrgec** · 2026-09-18T22:16:30.000Z：

If only Graphene had a better marketing team. It pains me to say this but it is the absolute truth: the public does not know Graphene and does not care about Graphene. Even it’s name is absolutely awful. This is like the Linux distro hell: “you should use BingaBoingoKonohaOS_v34 or Peppermint_Cinn4monR0ll with the OutOfThisWorld DE, but steer clear of the Pancake package manager, use openMsPacMan with GrassFaceWhazzit frontend instead.” How is anyone (as in not us, the tech nerds) supposed to reason about this?Things will keep as is for as long as they keep making these OSs FOR the tech nerds.Downvote me all you want. You know it’s true. An OS made for nerds and by nerds will never reach mainstream and will not, ever, move the needle anywhere. Tech is no longer a hobbyist’s game.

**nextaccountic** · 2026-09-19T02:34:36.000Z：

The trouble is that banking apps will not work if you degoogle your phone. GrapheneOS was an attempt to make this sort of thing work, in a phone OS more secure than stock AndroidBut to be honest, many banking apps randomly stop working with GrapheneOS anyway. So if you see this...https://privsec.dev/posts/android/banking-applications-compa...https://github.com/PrivSec-dev/banking-apps-compat-reportAnd check the issues, it's unpredictable whether a bank will continue to work with GrapheneOSSo.. if you accept GrapheneOS might not be reliable for this use case, and decide have two phones (one just for banking stuff, another for.. using), then degoogling is fine.Only thing is that the banking device probably needs to be a phone (or tablet I guess), I don't think you can emulate a real device good enough for it to work on something like Waydroid

**crossroadsguy** · 2026-09-19T03:16:34.000Z：

The answer to this is - the real world comes knocking. Govt, banking, investment, grocery, transport, even some mainstream social/communication apps, all stop working - yeah, kinda cold turkey. And if your, or someone else's, answer to them is: ".. well then don't use those apps.. or maybe in mobile or desktop browser.. " (this is usually the tone on those "privacy" guide forums), then yeah it will work and can be done in hours theoretically, or days max :)

**spydum** · 2026-09-19T17:56:08.000Z：

I think you could actually look at this via the OPPOSITE lense:
OpenSource was good for companies before, because they got free code/bugfix/labor, which would have been expensive to produce themselves.Now with LLM and agentic factories pumping out bugfixes/code, does the equation on opensource still look attractive to a for-profit company? Why give away that sweet source code?

**MrDrMcCoy** · 2026-09-19T00:15:20.000Z：

Oracle enters the chat

**NateEag** · 2026-09-19T15:55:31.000Z：

There's a crucial distinction between "can't sue you" and "would likely lose the case".You need to have enough money to actually survive the lawsuit, even if it's a slam-dunk to win (and they almost never are).

**microtonal** · 2026-09-18T20:59:23.000Z：

https://grapheneos.org/releases#2026091700Fixes/updates the modem firmware.

**grapheneos** · 2026-09-19T18:07:23.000Z：

It was shipped in the latest GrapheneOS release. It's currently in the Alpha channel due to reports of carrier compatibility issues for calls which are fixed in today's release. Today's release should be able to reach Beta in a couple hours and then Stable in under 24 hours.

**NetMageSCW** · 2026-09-19T18:56:46.000Z：

Feel free!

**fluidcruft** · 2026-09-18T20:54:53.000Z：

I don't really see what the Pixel-only early API releases achieve except for allowing developers to work on Pixels ahead of time, but Pixels are such a small sliver of the universe that it basically just gives Google a leg up, I would assume. And if you're on Graphene why would you care about Google's beta edge apps?

**teekert** · 2026-09-18T21:34:37.000Z：

The rattling is because of the security patches of course.

**mdwrigh2** · 2026-09-18T22:25:02.000Z：

> * Google drop "real" Android source-code updates to OEMs _and_ the public every half.All of the major OEM shave access to the internal source with a _very_ small delay. OEMs don't ship these intermediate releases because they choose not to, not because Google witholds the source for them.

**boredhedgehog** · 2026-09-19T16:43:32.000Z：

> which is sort of an odd business decisionIt's probably no decision at all, but merely poor coordination between separate departments.Once a bureaucracy surpasses a certain size, odd side effects accumulate on their own, and the growing number of people affected by them seek to cast blame where no purpose ever existed.

**grapheneos** · 2026-09-19T18:12:19.000Z：

GPL is not working for getting us access to what we need. Google often takes weeks or even months to respond to our GPL source requests. Other companies are far worse. What good is it to us if companies can introduce arbitrary delays for months or even years?There are permissively licensed alternatives to most copyleft projects and they're increasingly the better options. You aren't going to reverse that by licensing niche projects as copyleft. Companies wanting to avoid copyleft can make permissively licensed replacements more easily than ever.

**mitxela** · 2026-09-19T01:09:10.000Z：

Google is just one symptom of late stage capitalism.

**izacus** · 2026-09-19T07:03:05.000Z：

Why do you so desperately want to use their software then?This whole topic is basically people demanding that Google continues giving them their code for free for their operating system.If it's really such a cancer, why whine and demand the continued work then?

**d3Xt3r** · 2026-09-18T22:00:25.000Z：

Agreed. Linux is the future, fk Android. GrapheneOS should stop wasting their efforts on Android, when they could've contributed towards PostmarketOS or similar, or even made their own distro. Working on Android is a complete and utter waste of time and effort.

**MrDrMcCoy** · 2026-09-19T00:14:07.000Z：

I desperately want to use it, but it runs on precisely no decent hardware as far as I can tell. My attempts to get it working on the fxtec and furiphones failed miserably.

**mitxela** · 2026-09-19T01:29:37.000Z：

All FOSS consumer operating systems suck. We only tolerate them because they are FOSS.

**zb3** · 2026-09-18T22:15:09.000Z：

> I wonder how low Google will sink next time.Oh, the possibilities are endless and they're just getting started. Besides stopping releases of AOSP completely they could also mandate that any "certified" Android device should not allow bootloader unlocking (albeit OEMs will disallow that anyway)..

**dingaling** · 2026-09-19T06:00:41.000Z：

> Can't wait to buy their phone.Good phrasing. It's certainly not _your_ phone, you're just an untrusted user who is extended the privilege of using it.

**izacus** · 2026-09-19T07:04:44.000Z：

EU was very clear that closing down the OS (Apple) is how they avoid fines with their latest rulings. They punished Google for open sourcing the OS and left Apple get away free with explicit explanation that closed OS doesn't need to adhere to same rules.So yeah, don't expect EU to defend you here.

**seb1204** · 2026-09-19T10:29:44.000Z：

Hm, I have little interest in Google's AI API and more in a streamlined flow of security updates and not an obscure prolonged waiting time.

**dingaling** · 2026-09-19T06:03:21.000Z：

There are about 3.9 billion Android phones currently in use globally. I don't think a niche fork with 0.00025 billion users will worry them.

**GranPC** · 2026-09-19T19:37:19.000Z：

Did you work on BB10?

**fithisux** · 2026-09-19T10:41:22.000Z：

They have partnerships with almost everyone. That is why they can win.Still I am mostly interested about GrapheneOS or a RaspberryPi5 with an Android 17 build.But they seem to even own the RAM market.

**jeroenhd** · 2026-09-19T08:48:48.000Z：

Sailfish has a Linux-based OS with some Android compatibility.Ubuntu Touch has left behind UBPorts which uses Android's hardware layer to provide a usable UI on existing Android devices.There's the Librem phone with an open source stack, though its hardware doesn't come close to a cheap Android phone these days.There are projects like PostmarketOS which work to get mainline Linux on phones. From there, you can run Linux on phones through desktop environments such as Phosh and Plasma Mobile which are touch optimized.FirefoxOS died but was forked into KaiOS, though the modern iteration of KaiOS is an Android fork.Samsung has TizenOS but I don't think any phones run it anymore. It's probably the closest equivalent to Android in the way it has been developed.If you want to throw money at something, Sailfish may be the project to keep an eye on. All the other volunteer-run operating systems are worth donating to, of course, but Sailfish is actually trying to be a real third option rather than an open source proof of concept or alternative for shitty vendors stopping updates.

**d3Xt3r** · 2026-09-19T09:03:09.000Z：

Plenty. The ones you want to donate to are postmarketOS, Alpine Linux (the distro postmarketOS is based on) and Plasma Mobile (the main DE used by postmarketOS and other distros like Mobian).In terms of usability, SailfishOS is the most usable, but it has some proprietary components and is commercially backed by Jolla, so there's no need to donate to them. I do encourage you to buy their devices if you can though. Speaking of devices, Furilabs and Volla also make practical, decent spec Linux phones (based on Debian and Ubuntu Touch), so they're worth checking out as well.

**dethos** · 2026-09-19T09:50:01.000Z：

I've been saying that for a while. We need a viable third option.But it is not easy, and it takes a huge amount of effort. As others have said, theres SailfishOS, Ubuntu Touch, PostmarketOS and a few others.I'm not sure which one is in a better position to become that third alternative we need, but this year I'm experimenting with all of them on different devices, to try to understand where they stand."posted from an Ubuntu Touch mobile device"

**sixothree** · 2026-09-19T05:37:45.000Z：

They just walked away from an antitrust case with what can only be considered a huge win for them. I don't think regulating them is going to happen any time soon.

**NetMageSCW** · 2026-09-19T18:48:55.000Z：

Not everything is antitrust and regulation is always the worst choice.

**TiredOfLife** · 2026-09-19T05:48:23.000Z：

Pixel never was a reference aosp. You are thinkin of nexus.

**mahboi** · 2026-09-19T16:25:23.000Z：

Samsung would be hypocritical to complain about proprietary extensions to Android.

**spijdar** · 2026-09-18T19:55:53.000Z：

I want to believe this, but it's hard for me to take this at face value. It's been about 4 years since I've run pmOS, so my experience IS very out of date, but I also have a hard time believing that the experience has radically changed in the meantime.The short is that yes the GNOME/KDE apps do often look more impressive, but they suffer the same sort of malaise which seems to have infected Linux desktops sometime since Eternal September, and between the sporadic crashing and "this doesn't feel right", it's really hard for me to accept "It's more polished than AOSP!".pmOS's installation page opening with a warning: Make sure you read state of postmarketOS before installing postmarketOS. 

Which leads to a page that opens with: The goal is to make postmarketOS usable for everyone, but we are not there yet. Usability and most importantly stability issues need to be worked out first. If you are looking for an OS that is as usable as iOS or Android, this project is currently not for you.

Does not do a lot to dissuade my skepticism. I know you said the apps specifically, but even there, it's like... I dunno.

**cobertos** · 2026-09-18T19:58:25.000Z：

I tried getting it to run on a Pixel 3a and struggled for hours, eventually gave up (albeit I tried running it with Wayland and Niri which seems less tried-and-true).

**MrDrMcCoy** · 2026-09-19T00:17:04.000Z：

PMOS doesn't run with full support and performance on any decent hardware. Would love to be proven wrong.

**fungi** · 2026-09-19T01:42:54.000Z：

2nd vote for postmarket. have put it on an old tablet i pulled out of ewaste and it is excellent.there is clearly no future for android for anyone wanting an open and spyware free platform. its time to invest out efforts elsewhere.

**grapheneos** · 2026-09-19T18:17:26.000Z：

GrapheneOS provides drastically better usability, robustness, overall functional and app compatibility. Privacy and security are also drastically better in AOSP and especially GrapheneOS than that desktop Linux software stack ported to mobile.All of the default apps in GrapheneOS are being rapidly overhauled or replaced. It wasn't a priority due to the incredibly good open source app ecosystem with many existing alternatives available. There isn't a similarly high quality open source mobile app ecosystem available there.

**armadyl** · 2026-09-18T19:54:42.000Z：

More like OEMs need to take security more seriously and add in the capable hardware and commit to firmware updates long term.

**vkaku** · 2026-09-18T19:59:05.000Z：

Those Razr phone updates need to start landing sooner ....

**subscribed** · 2026-09-18T20:00:03.000Z：

They can't due to the shortcomings of the hardware (why develop a hardened os to the grossly insecure hardware) or the vendor (no/slow updates, etc).Anyone is free to fork, add the desired hardware support and flash.(that's aside of some Moto flagships in 2027)

**anonzzzies** · 2026-09-18T20:04:23.000Z：

> Oracle was a mighty powerhouseIt definitly still is. We run Postgres when we host our banking / financial stuff, but when we talk with banks and say that, they demand Oracle not that 'open source amateur stuff'. We have a version of our software for Oracle (and MSSQL) as well so no biggy, but still, we always try if we know it's not a complete immediate kill (which it will be if we put it in our documentation as only option). Oracle is still everywhere at the big guys.

**linuxftw** · 2026-09-18T20:09:51.000Z：

Google's Android customers are phone OEMs. The major ones seem to like how things are going. Until Samsung and whomever start the OpenHandset Foundation or some such and fork Android, there's never going to be the Mariadb of Android.

**tredre3** · 2026-09-18T20:10:03.000Z：

> it will no longer be in control of AndroidWho will step up to maintain it? Keep in mind that it has to be somebody that every other OEM trust. In other words it would likely have to be an alliance of manufacturers. And they'd inevitably treat OEMs outside the alliance poorly and we'd be back to the current situation, but worse.

**murderfs** · 2026-09-18T20:10:49.000Z：

> If Samsung and everyone else said "sorry Google', or even a large majority, you're out. Gone. Nada.The OEMs are incapable of writing a competent operating system, and don't particularly care to.> Google is also getting more and more pushy with Chrome. What if everyone depending upon that backend, shrugs and says "Sorry Google, we're hard-forking Chrome and we'll all maintain it".With what maintainers?https://chrome-commit-tracker.arthursonzogni.com/organizatio...

**wvenable** · 2026-09-18T23:57:43.000Z：

I don't think so. Google's customers are phone OEMs and as long as they are happy, things will continue as is. The precedents here are Microsoft with Windows and maybe Apple with iOS.Anything Oracle doesn't have much relevance. They were not really interested in growing any marketshare of those products for anyone.

**qlte** · 2026-09-19T00:24:02.000Z：

Google and Samsung have a closer relationship than ever these days, with cross-branded Google features even featured in advertisements for the last couple Galaxy models which would have been unthinkable back in 2012 or so.They have their private own agreements with Google to secure whatever access they need to maintain their OneUI fork and are not the one making any public complaints. Samsung did have a love/hate relationship with Google that was openly simmering with resentment during the early years of Android but those days are long past.Samsung already includes their own Galaxy store alongside the Play Store on all their devices, and have for 10+ years. But during that time have actually moved the opposite direction from your hypothetical fork scenario and both companies clearly view their current relationship as mutually beneficial.Even though GrapheneOS and Samsung both maintain their own Android fork their views on AOSP/Google are not aligned.

**qlte** · 2026-09-18T23:53:44.000Z：

That is definitely not how I remember the feature phone era. The OS was an afterthought seemingly whipped together a couple months before the device hit the shelves and nothing was ever consistent even across recent models from the same manufacturer.Back then the primary goal was checkboxes for the carrier to advertise and UI/UX was a distant second priority at most. Sometimes an advertised feature would just flat out be unusable (such as MP3 players), but good luck waiting for any kind of update because by then those developers had already been reassigned to the next handset model they promised to carriers.Also, Samsung extensively customizes their OneUI fork of Android, with its own UI look and feel that evolves independently from Android based on their own priorities. Plus Samsung's Android maintains hundreds of features that either don't exist at all on AOSP/Pixels or later get folded into mainline Android.(Including the little known killer app suite "Good Lock" available on Samsung's Galaxy store which gives power users an almost obscene amount of additional niche options and customizations that would give UX minimalist designers at Google or Apple a heart attack)But despite how different Pixel vs. OneUI look and feel, I can use the exact same apps whether on a Pixel or Galaxy or $100 trash phone. Interoperability is very easy to take for granted and Android app ecosystem is (still) paradise compared to the lowest common denominator J2ME "app" era of the 2000s.

**dlahoda** · 2026-09-18T20:23:21.000Z：

for some people contactless payments are essential for their lifes

**edent** · 2026-09-18T20:32:01.000Z：

Contactless payments do work on Graphene - but only with the Curve app. It also requires the card-holder to be from the UK or EU.

**pimeys** · 2026-09-18T19:48:38.000Z：

Android has free and open artificial pancreas that is still easy to install and keeps us with complex type 1 diabetes alive.Google may just want to kill us and Apple don't even let this kind of software exist without massive hurdles...

**subscribed** · 2026-09-18T20:05:02.000Z：

Because it's much worse (for me).However at this point, as a GrapheneOS user if I couldn't use it for any reason I'll go to iOS (even though I used it for a couple of years and I've been fed up).

**add-sub-mul-div** · 2026-09-18T20:29:49.000Z：

Because (1) you'd be rewarding the entity that originated and normalized the loss of freedom that Google much later adopted, and (2) as Apple restricts more freedoms you'll still be able to enjoy them on Android for a few more years as Google remains (comparatively) more user friendly.

**mitxela** · 2026-09-19T01:08:28.000Z：

Because it still allows installing apps with some hoops, and iOS doesn't allow it at all.

**jasonfarnon** · 2026-09-18T23:06:27.000Z：

Yeah. Which doesn't mean Google isn't happy to comply for its own profit motivations.

**subscribed** · 2026-09-18T20:09:36.000Z：

If the hardware security is on par with iPhone / pixel 8+, then sure.Otherwise there's no need for NSA backdoors (as Cellebrite matrix shows) :)

**ChickeNES** · 2026-09-18T20:15:26.000Z：

Sure, let's just trade the NSA for the CCP, no issues there.

**mitxela** · 2026-09-19T01:03:00.000Z：

GrapheneOS does, however, register on the FBI's radar because a lot of criminals know to use it, and the FBI can't crack it.

**mrpippy** · 2026-09-18T20:00:24.000Z：

That’s possible (never underestimate the bad decision-making of phone makers), but what would they have done instead? Windows Mobile 6 was the only licensable alternative, but it was a known quantity and obviously a generation behind Android and iOS.

**thevillagechief** · 2026-09-18T20:03:17.000Z：

I don't think this is actually true. Phone makers seem happy to have the platform locked down even further. They're putting even more roadblocks, as evidenced by most of them making bootloaders unlockable.

**sublinear** · 2026-09-18T20:09:11.000Z：

No, everyone knew what they were getting into with Android. It wasn't taken lightly by the power users of the time either. I still have a phone somewhere with Ubuntu Touch on it. I really was hoping that would be my phone OS by now. Not that Canonical isn't capable of similar, but that it would bring about acceptance of Linux phones.I think we're all more surprised by how long it took for Google to make these bad moves. For a period of time in the 2010s we actually started thinking maybe Google was alright.

**alightsoul** · 2026-09-18T20:37:51.000Z：

Phone manufacturers had Symbian which became open source

**ikiris** · 2026-09-19T04:05:10.000Z：

It didn't become a major regret really until the antitrust treated android as a competitive space and iphone separate. That decision led to a lot of wtf and tactics changing. Because the platform had been made open it was then an issue of tying vs if it had just been closed like apple there wouldn't have been an issue was a pretty stupid take if you ever want to see an open platform again.

**jeroenhd** · 2026-09-18T20:10:39.000Z：

I just ran https://github.com/CakesTwix/Android-CVE-2026-43499 on my Pixel 9 Pro and it seems to have been patched. I did get a system update not long ago, though.

**lenerdenator** · 2026-09-18T20:11:54.000Z：

There's "dropping the ball" and then there's "not reaching out your glove to catch it to begin with".It'd be interesting to see which one is happening here.

**grapheneos** · 2026-09-18T20:33:07.000Z：

Pixels used to have far better updates than any other Android devices but they stopped improving it years ago. It should have kept improving because it's not at all adequate. They need to be able to release OS updates more than once per month and it shouldn't take months for patches to make it into the OS. It currently takes them at least around 2 months to get even the most urgent patches into the OS. They could fix emergency calls being broken if the patch was made around 3 weeks before an OS release, but that's about as quick as they can go. It's not at all adequate for security and is a complete joke compared to Chromium's release cycle. They can get an emergency Chrome update released within a couple days. They should at least be able to do it for the Pixel OS in a week.GrapheneOS is often around 4 to 6 months ahead on merging Linux kernel LTS releases. We used to handle this ourselves but switched to the Android GKI LTS branch maintained by Greg KH. Unfortunately, it was often struggling to keep up even before the absolutely massive increase in Linux kernel security patches this year. AI models have rapidly accelerated vulnerability discovery and it's an ongoing crisis for the Linux kernel. We want to be on the latest LTS revision within days and want to be using the latest LTS branch within months of it being released. We're not at all happy with how Android is handling things and plan to fix that ourselves. We'll get things back to how they should be.We also ship all the AOSP userspace patches months before Pixels due to shipping all of the security preview patches as soon as possible. There are sometimes minor regressions but we find and fix them ourselves downstream. The security preview system has a terrible design especially considering that frontier AI models can reverse engineer the patches. There should at least only be a source embargo for around 24 to 72 hours rather than pretending as if it can work with the patches available 2 to 6 months in advance.

**microtonal** · 2026-09-19T05:51:15.000Z：

Librem seems as bad as a typical Android OEM. Maybe I'm looking at the wrong repository, but the barely seem to update driver firmware?https://source.puri.sm/Librem5/fw/firmware-librem5-nonfreehttps://source.puri.sm/Librem5/arm-trusted-firmwareI hope I'm looking in the wrong place.

**SahAssar** · 2026-09-19T00:04:15.000Z：

The org takes responsibility. If you want to additionally name & blame an exec feel free.

**nomel** · 2026-09-18T20:34:34.000Z：

> So we move. We force their handWhat do you have in mind?

**the_real_cher** · 2026-09-18T20:56:34.000Z：

LOL "start" using Firefox. I've been using Firefox for half a decade. There's zero I miss about Chrome.

**StilesCrisis** · 2026-09-18T21:19:22.000Z：

Hard forking doesn't solve the problem of closed source.If the goal of a hard fork is "the community will invest equal resources that Google does today" then you wildly underestimate how many engineers work on Chrome.

**saghm** · 2026-09-18T21:32:58.000Z：

> But they won't learn that on their ownI think they're fully aware of this. They just don't care, because the goal of "get market share super high" has been reached, so now they have no need for it to continue being open.I don't disagree about what that means we should do; I just don't think we should assume they're being naive here. It's like writing a program to play chess; you should select your move assuming the opponent is smart and will make the optimal counterplay rather than assuming weakness, and then if they end up being less smart than that, you're still in a good place.

**awakeasleep** · 2026-09-18T21:42:29.000Z：

The “we” in your post is interesting to me. Who do you mean? Individuals?

**cecexacjrgec** · 2026-09-18T21:43:44.000Z：

> or turn to alternatives like Firefox as a new foundation.With the way Firefox is heading, that might not be the best idea. Nowadays Mozilla seem more focused on riding the AI-hype wave than actually making an excellent browser people want to actually use.

**arcanemachiner** · 2026-09-18T22:15:12.000Z：

> Android wouldn't be what it is if it wasn't open source.Yes, and now that they've achieved market saturation, it's time to pull up the ladder.Thanks for all the free work, suckers!

**jauntywundrkind** · 2026-09-18T22:29:16.000Z：

It's sad we lost ChromeOS. They got Linux, they got open source, they didn't make so so so many unforced errors.Now that the chromebooks are also Android, it feels like the slide is only going to grow ever more fearsome.

**charcircuit** · 2026-09-19T01:04:34.000Z：

There are already several different forks of Chromium and they are able to make their own decisions on points where they want to differentiate from upstream or other browsers in the market.

**Henchman21** · 2026-09-19T01:18:21.000Z：

Ahem. Ladybird.

**xmprt** · 2026-09-19T01:34:53.000Z：

Google is starting to turn into early 2000s / late 90s Oracle.

**suprjami** · 2026-09-19T03:34:33.000Z：

> or turn to alternatives like FirefoxImplying I ever left Firefox in the first place.

**DANmode** · 2026-09-19T03:59:06.000Z：

> Just because it is open source doesn't mean they don't control itJust point out how that hurts security or privacy and we’re with you!

**throwaway27448** · 2026-09-19T04:02:46.000Z：

> advocating for chromium.Advocating for chromium to do what?

**rs_rs_rs_rs_rs** · 2026-09-19T06:41:04.000Z：

Who's we?

**p0w3n3d** · 2026-09-19T06:58:23.000Z：

So we move. We force their hand

How?

**dmacedo** · 2026-09-19T07:31:45.000Z：

I would say its even more proactive than support other projects.
It is becoming clearer that every single technically competent member of the friends or family is now required to educate and proactively change devices.Remember this upcoming Christmas that the ye oldie tradition of fixing PCs clearing awful exploiting phone apps (and cancelling subscriptions) should also include the "fix my browser" again, instead of Internet Explorer being replaced by Chrome, our collective duties is to replace Chrome with Firefox, plus its useful extensions to block ads and improve the web experience removing trackers etc.Your call to arms today is to ensure all your tech colleagues join the movement, and then we can see Google's management views on "market growth"; they forget they made Chrome, we sold it - its our fault we forgot the "infinite growth of shareholder value"...

**duskdozer** · 2026-09-19T09:41:15.000Z：

What's the licensing on AOSP? Everything I look for points to Google-owned things. Is it a GPL/similar that Google is actually legally required to share its changes?

**drooopy** · 2026-09-19T12:16:16.000Z：

I wish that a consortium of Android phone makers would/could "LibreOffice" Android.

**leni536** · 2026-09-19T12:34:29.000Z：

Reminder to think twice when signing CLAs when contributing to these big company open source projects.

**httgp** · 2026-09-19T13:47:14.000Z：

Heavily rooting for Ladybird.

**faust201** · 2026-09-19T14:07:45.000Z：

> I hope people remember this when advocating for chromium. Just because it is open source doesn't mean they don't control it. We need to start the long process of hard forking now or turn to alternatives like Firefox as a new foundation.This is correct but rarely in practiced.During firefox DRM/HTML5 issue, I know many people from Free software foundation Europe absolutely telling in their blogs, talks etc please stop Mozilla from implementing this DRM or that... but finally when I spoke to these in private they told --- ya, whatever - I need to see this series in netflix etc- so I have another device with chrome etc to watch it. (Indeed Firefox did implement it)This behavior is the reason average Joe gives up...

**thisislife2** · 2026-09-19T18:13:29.000Z：

And this is also why I advocate for xGPL for open source projects. FSF's GNU Public Licenses are the only open source licenses (that I am aware of) that envisioned a users "right to repair" decades ago. This is enforced by ensuring that any source code licensed and distributed under xGPL, has to remain open source. If even a part of the source code is licensed under GPL, and used in any project, you cannot close source it easily. Other permissive licenses, like MIT, BSD or Apache, for example, don't guarantee the open source nature of the product that is licensed under it as it allows anyone to also use the code and distribute it without the source code.(This is also why we should be be vary, and quite sceptical of, Canonical's new Rust-based port of GNU CoreUtils too. Apparently, Canonical plans to replace GNU CoreUtil completely in Ubuntu with this port. The original GNU Coreutils are licensed under the GPL, but the Rust based ports are not. This means that Canonical will now have the ability to stop distributing the source code of its CoreUtils port in future Ubuntu Oses).

**graemep** · 2026-09-19T18:25:11.000Z：

The important bits of Chromium are LGPL licensed,originally a fork of other people's code. Google cannot close it as easily.

**m-p-3** · 2026-09-19T18:29:43.000Z：

> or turn to alternatives like FirefoxI never left. The only thing I don't like is that I can't directly donate to fund Firefox, only towards the Mozilla Foundation in general.

**mikeweiss** · 2026-09-18T21:33:02.000Z：

Agree. The only time a company does something in the public interest is when it believes doing so would ultimately benefit the shareholders. Everything is a business decision.

**wwiinn** · 2026-09-19T13:46:40.000Z：

You conveniently forgot the OG, oracle.

**NetMageSCW** · 2026-09-19T18:32:43.000Z：

LOL at “noticeable traction”.

**Ritewut** · 2026-09-19T02:27:36.000Z：

It's like PC parts being modular. IBMs greatest mistake and the industry wants to make sure it never happens again.

**ikiris** · 2026-09-19T03:58:59.000Z：

Its more a reflection of the vastly different internal culture of the time (and different executive leadership).When Patrick Pichette left and Sundar became CEO both led to massive culture shifts.

**fh973** · 2026-09-19T12:11:31.000Z：

Please remind us which exciting features Android graced us with in the last say 3 years?

**izacus** · 2026-09-18T20:24:40.000Z：

Can you link to patches or commits they upstteamed? I'm not aware Google ever accepted any.

**iAMkenough** · 2026-09-18T21:23:10.000Z：

Seems like that's anti-competitive behavior, holding back security updates except for Google's own stock users.https://grapheneos.social/@GrapheneOS/117282190165630051> It would be interesting to know if Google's legal team is aware they're giving Pixels months of early access to new Android features and bug fixes including certain important security patches. Pixels being given this competitive edge over Google's OEM partners is very dubious.

**xnx** · 2026-09-18T20:16:37.000Z：

Yes, but a popular one that's usable by regular people and with a very wealthy organization behind it.

**hagbard_c** · 2026-09-18T20:21:03.000Z：

They exist but they need more polish and support from device vendors to be a viable alternative to the duopoly. It should be just as easy for the average phone buyer to get and use a 'Linux phone' as it is to get an Android or fruit phone. This is more or less true now for Linux distributions no matter what the naysayers keep on repeating, the next step is to make it true for mobile devices. There will still be naysayers but... who cares? Let them listen to themselves in their echo chambers like they've been doing w.r.t. 'Linux on the desktop'.

**MrDrMcCoy** · 2026-09-19T00:10:44.000Z：

Wake me when they get modern hardware.

**xnx** · 2026-09-19T15:15:21.000Z：

Facebook tried doing a phone in 2013: https://en.wikipedia.org/wiki/HTC_FirstAmazon did one in 2014: https://en.wikipedia.org/wiki/Fire_Phone

**mitxela** · 2026-09-19T01:05:52.000Z：

Which is why Grapheme runs them in a sandbox. You can too.

**MrDrMcCoy** · 2026-09-19T00:06:09.000Z：

GrapheneOS won't be interested in other hardware support, since the only devices that meet their hardware security standards are Pixels and the upcoming Motorola phone.

**layer8** · 2026-09-19T18:35:49.000Z：

It doesn’t really matter if most app providers won’t be porting their apps to the new phone OS.

**ninjasmosa** · 2026-09-18T23:58:35.000Z：

I believe GrapheneOS talked about hosting their own unifiedpush server and baking it into the OS not long ago

**zb3** · 2026-09-18T21:14:21.000Z：

HarmonyOS kernel (HongMeng) is not only closed source but also encrypted. Those devices do not allow you to unlock the bootloader or install apps not signed by them (albeit I don't know how that works for emulator apps, a signed Android emulator could possibly allow arbitrary apks).Huawei made a big mistake by not fully open sourcing HarmonyOS, you can't flash OpenHarmony so it doesn't count.

**fwip** · 2026-09-18T21:15:50.000Z：

That's Huawei's Android fork, right? Is it available on devices outside of China? I'm not seeing an obvious place to buy a device running it.

**colordrops** · 2026-09-18T21:25:42.000Z：

LOL an OS controlled by the Chinese government?

**jraph** · 2026-09-18T23:30:49.000Z：

What's particularly bad about the names of Graphene, Mint and Cinnamon? Especially compared to Android and iOS!!

**mitxela** · 2026-09-19T01:06:28.000Z：

It's the OS every drug dealer uses and the government can't break it. In privacy circles you can't get better marketing than that.

**Biganon** · 2026-09-19T13:12:51.000Z：

> How is anyone (as in not us, the tech nerds) supposed to reason about this?People have more than enough brain power to reason about this. "There are several distributions, I recommend this one" is not exactly rocket science.We really need to stop treating people like they have an IQ of 30 and only 5 minutes of free time per day, or we'll never defeat Google et al that purposefully maintain us in this belief.

**annex-winged-cr** · 2026-09-19T13:42:23.000Z：

Well, Motorola's next flagship is shipping with GrapheneOS, so we'll see.And I don't see how the name "GrapheneOS" is any worse than "Android". Really, the biggest barriers to adoption are:- No phones come with it pre-installed (yet)- They only work with Pixel phones (for now)- Some apps like certain banking apps don't work

**alt227** · 2026-09-19T17:47:07.000Z：

> An OS made for nerds and by nerds will never reach mainstreamBy your own definition, is it meant to make the mainstream?

**gonight** · 2026-09-19T05:30:55.000Z：

My bank can support my phone or accept that I'm going to come waste their time in person, I'm not backing down here.

**muvlon** · 2026-09-19T11:12:38.000Z：

Yes, if the banking app refuses to run on Graphene, you can forget about Waydroid completely. Hell will freeze over before Waydroid passes play integrity.

**hobo123** · 2026-09-19T13:22:28.000Z：

Literally insane that banks will allow you to do banking on ancient phones with an unpatched Android full of CVEs, but won't allow you banking on a modern ungoogled OS.

**LarryDarrell** · 2026-09-19T14:34:51.000Z：

This is what I ended up doing. I have LineageOS running on a Moto G. For banking, I have a tablet.I didn't want two phones, because it just seems so silly. The tablet, based on it's larger size, at least offers things that another phone cannot.

**smolder** · 2026-09-19T15:29:11.000Z：

My phone is not that old but it stopped getting OS updates and I stopped considering it a way to do anything banking related when my bank declared that my phone OS was too old to run the app.

**teekert** · 2026-09-18T21:09:49.000Z：

Ah that's great news! Do you know how to force an upgrade?

**teekert** · 2026-09-19T19:19:49.000Z：

Great work! Thanx!!

**grapheneos** · 2026-09-18T21:22:14.000Z：

Exclusive access to QPR1 and QPR3 releases gives Pixels an unfair advantage over other Android OEMs. They get an extra 2 major updates per year. Introducing new APIs for third party app developers as part of these updates means third party apps will now run best on the Pixel OS. Google apps already run best on the Pixel OS due to many exclusive features. It's Google's standard overall approach to propping up parts of their business with their monopolies in other markets. It's not legal.

**bri3d** · 2026-09-18T22:58:27.000Z：

Oh! I had thought they stopped at the same time they closed off AOSP commits - that makes this entire rabble-rousing effort _exceptionally_ silly, then; I can't see the angle GrapheneOS are trying to push at all in that case (like, I get their side of the _concern_, but "Google are shipping features to Pixels that you don't get" becomes... quite a poor argument indeed in that scenario).

**bri3d** · 2026-09-19T18:41:14.000Z：

I felt compelled to reply to this because I agree with it so strongly (which is also why I phrased my initial post as "sort of odd" rather than "some evil anti-consumer monopoly volcano lair conspiracy"); so many corporate oddity theories are easily caused by dysfunction that I wonder how many of their proponents have ever really been exposed to a corporate job.

**fithisux** · 2026-09-19T04:05:35.000Z：

100%Capitalism is transforming to feudalism.

**kuschku** · 2026-09-19T07:21:42.000Z：

That's always been the deal: they can build their OS on the work of many volunteers, and we in turn can build our projects on top of the OS.Google is trying to take from the community potluck without giving anything back.

**microtonal** · 2026-09-19T06:03:10.000Z：

Yes, let's abandon a very mature OS that is still open source, has millions of apps, and billions of users by one one that was designed for desktops, with a security posture fitting the 90s, virtually no phone apps unless you emulate said very mature OS, and which will have all the same problems with remote attestation, etc. </s>

**well_ackshually** · 2026-09-19T10:35:14.000Z：

The future is an inappropriate OS with catastrophic battery management, zero software available, no sandboxing or proper security measures, and the oh so stable kernel ABI & Gnome APIs to develop for, yep yep yep.

**ysnp** · 2026-09-19T11:13:03.000Z：

For what it is worth, GrapheneOS have expressed interest in a new base OS with an Android compatibility/virtualisation layer, but they do not have the resources to build it themselves and a suitable open source one does not already exist for them to leverage.

**armadyl** · 2026-09-19T16:07:15.000Z：

Yes ditching a secure OS for one that can easily be pwned by police / ICE / DHS with ease (especially in a time in the US when they’re doing this more and more) when AOSP can just be hard forked users. Thanks for the input, government agent.

**d3Xt3r** · 2026-09-19T09:12:20.000Z：

I disagree. Linux (especially a top-notch distro like CachyOS or Aurora) is quantitatively and qualitatively superior to Windows in several aspects (performance, filesystem features, workload-specific kernel tuning, DE customisation etc). Several benchmarks out there that can show you the performance edge Linux has over Windows. Plus there are several features completely missing from Windows, like atomic updates, immutability, not to mention all the cool features found in filesystems like btrfs. Of course, Windows has some benefits too, but making a sweeping blank statement like "All FOSS consumer operating systems suck" is very egregious and insulting to the all volunteers around the world, who continue to work tirelessly to make FOSS better every single day.

**matheusmoreira** · 2026-09-19T14:09:18.000Z：

Isn't GrapheneOS rootable?

**HumblyTossed** · 2026-09-19T17:30:57.000Z：

k

**grapheneos** · 2026-09-19T18:25:43.000Z：

GrapheneOS provides drastically better usability, robustness, overall functional and app compatibility. Privacy and security are also drastically better in AOSP and especially GrapheneOS than that desktop Linux software stack ported to mobile.All of the default apps in GrapheneOS are being rapidly overhauled or replaced. It wasn't a priority due to the incredibly good open source app ecosystem with many existing alternatives available. There isn't a similarly large and high quality open source mobile app ecosystem available for what's being promoted.

**brnt** · 2026-09-18T20:14:33.000Z：

I recently installed pmos on two 3a's and it was as simple as a Lineage image. Works well too!

**grapheneos** · 2026-09-19T18:26:52.000Z：

GrapheneOS provides drastically better usability, robustness, overall functional and app compatibility. Privacy and security are also drastically better in AOSP and especially GrapheneOS than that desktop Linux software stack ported to mobile.All of the default apps in GrapheneOS are being rapidly overhauled or replaced. It wasn't a priority due to the incredibly good open source app ecosystem with many existing alternatives available. There isn't a similarly large and high quality open source mobile app ecosystem available for what's being promoted.Pixel 3a will lack firmware updates regardless of what you put on it. Having serious unpatched vulnerabilities for radios and other firmware is considered acceptable for desktop operating systems but definitely not by us.

**grapheneos** · 2026-09-19T18:28:26.000Z：

GrapheneOS provides drastically better usability, robustness, overall functional and app compatibility. Privacy and security are also drastically better in AOSP and especially GrapheneOS than that desktop Linux software stack ported to mobile.All of the default apps in GrapheneOS are being rapidly overhauled or replaced. It wasn't a priority due to the incredibly good open source app ecosystem with many existing alternatives available. There isn't a similarly large and high quality open source mobile app ecosystem available for what's being promoted.

**grapheneos** · 2026-09-19T18:18:32.000Z：

GrapheneOS provides drastically better usability, robustness, overall functional and app compatibility. Privacy and security are also drastically better in AOSP and especially GrapheneOS than that desktop Linux software stack ported to mobile.All of the default apps in GrapheneOS are being rapidly overhauled or replaced. It wasn't a priority due to the incredibly good open source app ecosystem with many existing alternatives available. There isn't a similarly large and high quality open source mobile app ecosystem available for what's being promoted.

**NetMageSCW** · 2026-09-19T19:02:36.000Z：

“rapidly” - how long has it been?

**dessimus** · 2026-09-18T20:28:42.000Z：

Unless there is a real market advantage to it, they won't. Consumers prove over and over again they are willing to trade security to save a few dollars. Furthermore, why commit to providing hardware and software support for a device to last 5+ years, when ~25% of Americans report damaging their device each year[0]. Most of a device's population will have been replaced in 3 years.[0]: https://www.claimsjournal.com/news/national/2024/03/15/32248...

**tcfhgj** · 2026-09-19T00:44:58.000Z：

they can, but don't want to

**mrlonglong** · 2026-09-18T20:08:40.000Z：

Are they still forbidding benchmarking the Oracle database in their T&Cs? I laugh. Such litigious losers.Postgres ftw. Long may it eat their lunch.

**LooseMarmoset** · 2026-09-18T20:55:05.000Z：

as someone who is associated with “the big guys”, I can tell you this is changing.Our Oracle license licensing went up so dramatically that the team I work with is moving some very large databases to postgres from Oracle because it doesn’t make financial sense anymore.now, if we could only stop eating at the trough of Broadcom…

**cyberax** · 2026-09-18T21:26:42.000Z：

I'm advising a startup doing software for banks, and the overall attitude of their clients is: "We want to get away from the #&I$*@&^#$ Oracle, but we're stuck for now".Oracle used to be a must-have because it was one of the few products that could handle transactions on a scale of a bank, with all the requirements for backups, redundancy, etc.A fun anecdote. Back in 2000, I was present at negotiations (as a note-taker) where database vendors were bidding for a project for a factory control system. Vendors submitted benchmark results for various DB sizes up to 40Gb, and Oracle's rep hautingly said something like: "Our minimal size for benchmarks is 80Gb, so here are our results for that size".And this was a _lot_ for that time. Now? It's so ridiculously tiny that you can host it on a smartwatch. So why would you pay Oracle?

**eppp** · 2026-09-18T20:28:32.000Z：

That seems a little excessive.

**anonym29** · 2026-09-18T20:35:49.000Z：

One poses an active, unchecked threat to the constitutional rights of US citizens, has a chartered mission to subvert and undermine the very field of cryptography itself - going so far as to bribe standards bodies to adopt backdoored algorithms (using taxpayer funds to do so), has plotted to mass-violate the constitutional rights of their own citizens and lie about it to the national legislature (which they carried out successfully, committing perjury in the process and facing zero consequences for it), secretly cooperates with the criminal justice system via parallel construction to target nonviolent, law-abiding political activists with fabricated criminal charges as retaliation for politically disfavored speech, while the other is about 6500 miles away, has negligible presence in / reach into the US, and is generally unconcerned with the domestic political activities of US citizens.

**pmlnr** · 2026-09-18T20:05:58.000Z：

Maemo.

**thomasahle** · 2026-09-18T20:12:44.000Z：

Also Bada

**SoftTalker** · 2026-09-18T20:23:23.000Z：

Windows Phone was pretty nice, too bad Microsoft didn't follow their DOS and Windows strategy of getting it preinstalled on every consumer PC sold. There was really only the Nokia Lumia line that I recall, but everyone I knew who had one loved it.

**LTL_FTC** · 2026-09-18T20:28:37.000Z：

WebOS was pretty cool (Palm). But I’m not sure if Palm would have licensed it. Lg ended up with it.

**edent** · 2026-09-18T20:35:17.000Z：

Symbian and LiMo were both available at the time. It is hard to say they were good alternatives though. Windows 7 - even with the weight of Microsoft behind it - wasn't able to attract enough hardware manufacturers.

**cyberax** · 2026-09-18T21:12:14.000Z：

There were several credible competitors: WebOS, Symbian, Maemo/MeeGo, Palm OS 6, and of course Windows Mobile. But they required cooperating with a single vendor and/or a lot of work to adapt.Android won because it was available "right now" and easy to hack. Vendors could get a BSP (Board Support Package) from a chip manufacturer, slap Android userspace on top of it, and ship a phone within half a year. It was a glorious mess for a while.Google then slowly tightened the reins and made the ecosystem more ordered.

**ardacinar** · 2026-09-18T20:12:33.000Z：

They're happy that it is locked down. They're not happy that they're not the ones doing the locking down.

**lenerdenator** · 2026-09-18T20:21:58.000Z：

This is what lots of people forget.Android is not a Linux desktop or server distro. It is not about you getting to put what you want on the hardware you bought for free.Operating systems are hellaciously expensive to maintain and that only gets worse in markets with rapid hardware improvements, as the smartphone market was up until maybe the late 2010s. Google is not a charity. SV did not come into national prominence for making investors $0. There is no money in giving maybe one in one-hundred smartphone users (and that's being generous) a bunch of code, for free, so that they can put it on their gizmo and talk to their nerd friends at their hacker meetup.When they pitched Android as "open", they meant that carriers and device makers could load it up with all of the revenue-enhancing bloat that they wanted. In return, Google got a device that would let them hoover up all of the data they could ever want in order to build better ad service profiles for those using the devices. That is, after all, their business.For a while, this could coexist with us screwing around with a real-life tricorder. At some point, though, the free stuff turned into a revenue opportunity that had to be exploited. And so, it will be.

**alightsoul** · 2026-09-18T20:40:21.000Z：

Any discussion about this is shut down. I just read an article https://www.bbc.com/news/articles/ckqxvy98x578o 
In the UK according to the BBC, politicians are pressing Samsung and apple to make stolen phones bricks. Samsung in response said that they have implemented several security features for this purpose. I think Samsung considers removing OEM unlocking a security feature according to the bootloader unlock hall of shame.Intel used to do the same with their anti theft technology aka Intel theft deterrent on their classmate PCs, so students had to enter unlock codes from an IT admin every 3 months or every say 200 boots to prevent the computer from being locked at the bios level preventing it from booting an OS, and there was an update which disabled that functionality permanently. And you would be warned when you had around 50 boots left to get the unlock code.

**tosti** · 2026-09-18T20:48:07.000Z：

Making the bootloaders unlockable is a good thing.

**reedciccio** · 2026-09-18T20:30:15.000Z：

It wasn't Canonical's limitation. Mozilla can confirm: the barriers to enter the phone manufacturing market are immense. Samsung, Ericsson, Sony, LG, etc, all had solid control of the deals with the network operators worldwide. It's a highly regulated market, you can't get in without Verizon, att, Vodafone etc to let you in. Canonical, Open Moko, Mozilla... Didn't have the strength to push through. Google and Apple did.

**wwiinn** · 2026-09-19T13:44:36.000Z：

And was burned to the ground by a trojan horse from microsoft.

**Retr0id** · 2026-09-18T20:25:28.000Z：

Try https://github.com/alex193a/Root-My-Pixel, worked on my 9a as of a few days ago (the version table in the readme is stale). I haven't checked the September update yet though (installing it now, to check).Edit: September update for 8a has a kernel build from July. I believe it's still vulnerable but the exploit will need its offsets adjusting etc.

**cyberax** · 2026-09-18T21:14:33.000Z：

I'd love to use GrapheneOS on less secure devices, just for the sake of Google autonomy rather than privacy.

**PaulCarrack** · 2026-09-18T20:37:20.000Z：

> We need to start the long process of hard forking now or turn to alternatives like Firefox as a new foundation.

**shevy-java** · 2026-09-18T20:40:32.000Z：

Well, it is time to realise that GPL and similar variants, are better
in the long term. I like MIT too, but GPL worked so much better for the
linux kernel. Google and others abuse the ecosystem of open source 
contributors here.

**JumpCrisscross** · 2026-09-18T21:08:30.000Z：

Donate to Ladybird https://ladybird.org/

**saghm** · 2026-09-18T21:33:41.000Z：

I'm reading your comment on Firefox. You can probably read mine and write a reply on it too!

**OtomotO** · 2026-09-18T21:03:26.000Z：

LOL half a decade.I've been using it for more than 20 years.I don't know why either of use loled though

**drnick1** · 2026-09-18T21:32:15.000Z：

Some of us have been using it for two decades more or less.

**weikju** · 2026-09-18T23:51:22.000Z：

Rather than being smug, I’ll say awesome! The best time to start using Firefox is yesterday. The second best time is now.IOW:Don’t threaten to stop using Google Chrome if they do one more evil thing. Start now.

**hobo123** · 2026-09-19T12:16:11.000Z：

Reminder that by now the Android version is also quite usable (typing this from FF). Just install Ublock origin.

**Forgeties79** · 2026-09-18T21:35:20.000Z：

But the open source project wouldn’t need to invest as much as Google does. There are all kinds of features and things they are working on that the general public really does not care about.

**redeeman** · 2026-09-18T22:49:18.000Z：

but perhaps we dont need several gigabytes compressed code to have a browser. perhaps what google have been doing is an utter abomination?

**ocdtrekkie** · 2026-09-19T00:40:54.000Z：

The bigger problem is wasting developer effort contributing to Google's platform. The real secret behind Android being "open" (sorta) is that while almost nobody runs AOSP, Google has tricked a bunch of fools into working on Android forks instead of building a real competitor.Playing at their table is a losing game, the house always wins.

**floxy** · 2026-09-19T01:31:54.000Z：

>wildly underestimate how many engineers work on Chrome.It is completely insane how many people work on Chrome. It seems like it is time to deprecate web browsers and do something different. Like you get a frame-buffer to draw on with something like a wasm vm. Web pages get replaced by programs (which they essentially are anyway). Get rid of 99.9% of the cruft that has accumulated over the decades in browsers. If you want to have some of that cruft, that is a library you have to send.

**seb1204** · 2026-09-19T01:38:04.000Z：

Not denying than many engineers work on Chrome just wondering how many of them work on Chrome features that are anti pattern, reducing privacy, improving information collection or tracking or against users interest in broad.

**MiroslavPokorny** · 2026-09-19T04:50:25.000Z：

Can anyone actually share 1 - 3 examples where a hard fork of a living os project has actually succeeded ?If AMZN couldnt make their fire whatever it was called fork of Android really grow, what chance has the community got ?

**lokar** · 2026-09-19T01:19:53.000Z：

I think this is true, but I also believe the original people who built it are not the people in charge now.

**echelon** · 2026-09-19T02:42:49.000Z：

We haven't had antitrust enforcement for 25 years. It's high time we did.Google needs to be broken up.

**godelski** · 2026-09-19T03:12:13.000Z：

Tbh I don't think fighting open source is Google's best play. I think it is in their own best interest to keep it fully open. It is free labor by those who are most passionate. It gives strong signals at what people want, this direction you develop. It strengthens security as more people try to test it. It means people work on forks rather than alternatives. All this is true even with a monopolistic market share.So yes, I do think they are being naïve. The stance is myopic. It is only a good move in the short term, and barely even that. It is under the false belief that we operate in a zero sum game.

**brookst** · 2026-09-19T12:51:03.000Z：

Every time the HN crowd rediscovers that companies make business strategy choices rather than immutable principled philosophical decisions, the angst and dismay are really something.When Android launched, making it open source (ish) was the right competitive decision. It got phone makers and carriers on board and accelerated the ecosystem’s development. Today it being open source (kinda) is a met negative for Google. So, yeah, they’re changing that.Well-run companies aren’t zealots. They adapt to changing conditions. If a company’s actions happen to align with your personal preferences today, it doesn’t mean you’ve found a lifelong philosophical soulmate. Ditto if a company’s actions run counter to what you want today. Either can and will change, and there’s nothing morally concerning either way.

**stuaxo** · 2026-09-18T21:45:28.000Z：

It's not really a "both sides" thing given the scale difference between what Google is up to and that.

**II2II** · 2026-09-18T22:13:01.000Z：

It is sad to see Firefox riding various hype trains over the years, but I can't really blame them. Miss the wrong train, and you fall behind and may not be able to catch up. Miss the train to nowhere, and you are only wasting resources.As for the excellent browser that people want, that raises the question of what people want. There are likely as many answers as people.

**josephg** · 2026-09-18T22:36:30.000Z：

Mozilla definitely wastes a bunch of money building features I don’t want. But underneath it all, Firefox is still an excellent web browser. You just occasionally have to disable “pocket” or “gadgets” or something.

**bryanlarsen** · 2026-09-18T23:00:59.000Z：

Is Firefox or Mozilla perfect? Heck no. But we're not comparing Mozilla against pre-IBM Red Hat or Ben & Jerry's or whatever your concept of the ideal corporate citizen is. We're comparing Mozilla against Google. That's a very low bar that Mozilla clears with ease, especially if you're criteria includes shoving AI down your throat.

**jdjfnfjdjjeh** · 2026-09-19T00:39:24.000Z：

Mozilla gets 100M a year from Google ??? No fucking way they are biting the hand that feeds.

**seb1204** · 2026-09-19T01:35:29.000Z：

Where is the form, forum or spot in general where one can tell Mozilla?

**spydum** · 2026-09-19T01:12:18.000Z：

Don't worry, we will fork and just repeat the pattern with new names! See you next time!

**mahboi** · 2026-09-19T15:55:24.000Z：

Google started making proprietary APIs for their Pixel on their non-open version of Android. Even if they stopped contributing to the open Android, what ladder did they pull up? The open Android is still there.

**simondotau** · 2026-09-19T15:03:42.000Z：

I’m a web developer and I have never dailied Chrome or a Chromium descendant. Firefox for daily, Safari for the occasional cross-check.

**toxik** · 2026-09-19T18:26:45.000Z：

And you just know Canonical thinks this is feasible because they can just copyright wash it with an LLM. "Write GNU coreutils in rust" is all you need to say.

**NetMageSCW** · 2026-09-19T08:06:45.000Z：

When IBM tried that with PS/2 it didn’t go so well.

**PhilippGille** · 2026-09-18T21:08:37.000Z：

https://grapheneos.org/faq#upstreamhttps://android-review.googlesource.com/q/status:merged+auth...

**NetMageSCW** · 2026-09-19T18:50:21.000Z：

That might be valid (but not really) if those other OEMs actually didn’t delay the features and bug fixes themselves.

**lanfeust6** · 2026-09-18T20:21:32.000Z：

I miss my blackberry

**fsflover** · 2026-09-18T20:23:04.000Z：

This can be achieved if more people support the effort. If you expect megacorps to offer you a device respecting your freedom, think again.

**TheBicPen** · 2026-09-18T23:15:15.000Z：

Why GNU? I get the appeal of Linux, but Android has that angle covered. What makes GNU a better userspace than Android for phone use? I actually think the Andoid userspace is very good for what it is. If Google's influence were magically removed, Android would be more or less the ideal OS, at least for me.

**etatester** · 2026-09-19T05:21:38.000Z：

How do you expect things to be popular without a company with self-interest? Producing a linux phone that people want requires immense capital, they're not just spending that and then releasing as open source forever.By the time the product becomes "popular", it's then just one more platform that needs to follow investor interest and laws.

**pizzaiolo** · 2026-09-19T11:29:01.000Z：

Wake up, babe: https://forgejo.catcrafts.net/Catcrafts/fp6-img

**fsflover** · 2026-09-19T13:00:56.000Z：

https://news.ycombinator.com/item?id=45312326

**palata** · 2026-09-18T21:27:17.000Z：

I think it started like this, but it no longer is the case.I feel like Huawei missed a gigantic opportunity there: forking AOSP may have gotten them traction. I would totally buy a Huawei device if it could run GrapheneOS, and I wouldn't mind if GrapheneOS was based on Huawei's fork rather than Google's.

**largbae** · 2026-09-18T22:11:49.000Z：

As long as it's OSS, you could always fork it back l.

**cecexacjrgec** · 2026-09-19T08:17:47.000Z：

On their own? Nothing.But Graphene doesn’t mean anything to the general public. People aren’t buying “an iOS device”, they are buying iPhones. People aren’t buying “an Android phone”, they are buying “a Samsung/Galaxy” or a “Pixel”.Mind you, when I say people, I mean the general population. Not those actually interested in these subjects.My point is: people don’t care about these specifics, people care about having a frictionless experience (or as close to frictionless as possible). Having to explain what Graphene even is is friction enough for most people to not even bother listening to your explanation.

**cecexacjrgec** · 2026-09-19T08:30:17.000Z：

If only privacy circles were big enough to matter.

**skorp01** · 2026-09-19T19:35:57.000Z：

It is not the OS "used by drug dealers". The vast majority of criminals use the stock OS on whichever device they purchase. It is pure make believe to think that people are installing any alternate OSes to commit crimes.There is also no statistics resulting from surveys, studies, reports, etc., that would indicate such a conclusion about user demographics.

**ocdtrekkie** · 2026-09-19T15:31:39.000Z：

Google will destroy any OEM which ships an Android fork out of the box. Google only permits alternative ROMs as long as they are niche and keep developers distracted from creating real competition.

**grapheneos** · 2026-09-19T19:33:06.000Z：

People can buy Pixels with GrapheneOS preinstalled from a bunch of companies despite it not being shipped that way from the factory.Pixels are currently the only devices providing the required updates and hardware security features. There will be at least one Motorola flagship with GrapheneOS support in 2027 meeting the same requirements. It will expand to more Motorola devices from there. iOS only runs on iPhones but that's hardly a barrier to adoption for it. Pixels aren't quite broadly available enough and it will take time before we can support lower end Motorola devices in the same price range as an 'a' series Pixel.The vast majority of Android apps do work. Banking apps are a special case where around 10% don't work due to banning using a non-Google-certified OS. Most banking apps definitely work on GrapheneOS.

**ysnp** · 2026-09-19T18:06:48.000Z：

GrapheneOS is not made for nerds, it is made for normal people.

**samus** · 2026-09-19T10:43:29.000Z：

Many banks nowadays charge higher fees for teller service.

**moffkalast** · 2026-09-19T17:17:55.000Z：

It's not about security, it's about lazyness. These are the people who still employ Cobol devs cause they don't want to migrate off existing mainframes. I've yet to see a banking app that was not an objective trainwreck.

**fph** · 2026-09-18T21:30:42.000Z：

It's in the alpha channel for now, you have to join the alpha channel to get it immediately (at your risk).

**fluidcruft** · 2026-09-18T21:33:27.000Z：

I honestly don't think anyone would care. They have a "leg up" for what 3 months every 3 months?Nobody buys a Pixel because of this minute software advantage.Maybe get Motorola or Samsung to support security updates for six years and get back to Pixel users.

**microtonal** · 2026-09-19T05:56:57.000Z：

The whole security embargo things seems incredibly stupid. OEMs are always too late rolling out security patches. So Google thought, "let's create an embargo of months so that the OEMs have time to integrate the patches". Anyone could see it coming that nothing would change and the OEMs would still wait until the very last moment.So now everybody is off worse. Not only are OEMs still slow with security updates, while CVEs float around for months among those within the know (or reverse engineering skills) for months.

**mitxela** · 2026-09-19T12:53:58.000Z：

Has transformed. Landlords are literally feudalism, and so is the mobile phone duopoly now that mobile phones aren't optional. So are the banks now that banks aren't optional.

**jeroenhd** · 2026-09-19T08:36:49.000Z：

The community is providing Google with nothing. A fraction of a sliver of market share running GrapheneOS isn't going to make Google care.The community potluck has been replaced with a Google Play-shaped stock exchange over a decade ago.

**d3Xt3r** · 2026-09-19T09:49:29.000Z：

Yes, I'm sure the billions of people will read the advice of a random commentor on a niche site and throw away all their handsets running a "very mature OS" and cause a crisis. </s>

**d3Xt3r** · 2026-09-19T10:39:02.000Z：

The future is an inappropriate OS which spies on you and harvests your data, gets more and more locked down with every release restricting user freedom, and prioritises corporate interests over end user interest, yep yep yep.

**d3Xt3r** · 2026-09-19T16:39:13.000Z：

Yes, indeed AOSP is trivial to hard fork and maintain independently of Google, which is why so many maintained hard forks of AOSP exists... right, right? Thank for the input, world's most brilliant coder.

**mitxela** · 2026-09-19T12:51:59.000Z：

Notice that I said "consumer". You have listed server features, developer features and nerd features.

**grapheneos** · 2026-09-19T19:20:59.000Z：

We hired 3 experienced app developers a few months ago. That's now our app development team working on overhauling these apps. They've already replaced the entire Messaging app user interface with a new modern Compose UI. Messaging v13 is currently in the Alpha channel and v14 is on the way with a bunch of additional fixes needed for it to reach Beta and Stable. Multiple other apps including Contacts are well into the same overhaul process.

**armadyl** · 2026-09-18T20:41:34.000Z：

Yeah unfortunately this is the case. Privacy and security in general are things most average consumers don’t necessarily care for, and especially don’t care for when it provides inconveniences. Even in more tech enthusiast crowds you see this reflected most obviously in people wanting to use Firefox over any Chromium variant of a browser.Not to mention to reach GOS’ requirements the cost of the phone would have to significantly increase which I imagine only hurts Android phones even more for no real gain since GOS users are minuscule overall.And the long term support is definitely not the norm yeah. It’s pretty much just Apple and Google doing it for their own devices. Motorola will be a newcomer to this concept with GOS. But we can only wait and see if they actually stick to it, given their track record prior to the collaboration.Google probably got away with it cause they made the chips and security chips themselves. I read something like Tensor costing $70 vs. a Qualcomm chip with MTE costing $250.But even with of all this, it wouldn’t make sense for GOS to spend it’s limited resources developing for a less secure platform when appropriate target devices exist (they mentioned something to this effect a few days ago on reddit too): https://www.reddit.com/r/GrapheneOS/comments/1wifsiq/comment...

**subscribed** · 2026-09-19T02:40:08.000Z：

OK, I'm confused, explain how they can deliver comparable security on a hardware that does not offer the same capabilities, from a vendor who doesn't provide patches.You say they can. How?

**anonzzzies** · 2026-09-18T21:00:33.000Z：

I hope so, I see some changes; far less than many seem to think here though.

**anonzzzies** · 2026-09-19T08:27:42.000Z：

Agreed, I had the same talks around 2000 but at the time it was still very much mssql/db2/oracle for 'real companies'. Yet i'm still surprised how much pushback we get, especially in Asian countries (India) but we do get it, a lot. And we have conversations with financial partners in the US as they advice our VCs; those calls go the same way 'ah, you are using that hipster open source stuff, yeah we don't do that here'.

**ChickeNES** · 2026-09-18T21:33:58.000Z：

> has negligible presence in / reach into the US, and is generally unconcerned with the domestic political activities of US citizens.lmao

**075326899532** · 2026-09-18T22:29:46.000Z：

+ 3 social credits, comrade

**Cider9986** · 2026-09-18T23:34:16.000Z：

I agree–it's absurd to be more concerned about spying of China on American citizens than the spying of our own government. While allies of the US are problematic because of however many eyes.Not particularly relevant but the lawful spying implemented in the telecommunications system by our own government has been abused by Chinese hackers as well.

**michaelmior** · 2026-09-18T20:09:32.000Z：

I remember using a Maemo device circa 2009. I recall overall really liking the OS.

**dpark** · 2026-09-18T20:51:19.000Z：

Windows Phone 7 didn’t ship until 2 years after Android. 2 more years later Windows Phone 8 was released and it was a legitimate option but just too late.Pre-7 was just not an operating system that anyone except the geekiest of geeks wanted to use.

**hobo123** · 2026-09-19T12:21:14.000Z：

I remember trying phones in stores (shortly before Windows phone died). On Android you'd touch the phone and get instant reactions, on Windows you'd touch and wait for a slow woosh animation, until a few seconds later a text only app would finally launch. embarrassing.

**ezst** · 2026-09-19T04:47:00.000Z：

Not even wearing rose tinted glasses right now, for having daily driven them back in the days, maemo and then WebOS had touch ergonomics and multitasking abilities which took Android/iOS decades to incompletely mimic. Maemo/Nokia N900's design principle seems to have been "let's provide the user with desktop-level productivity tools, and shrink the desktop into their pocket", the package was massive for the era's standards, but is tiny for today's, and those dumb-down/low density ergonomics we have now give us less capabilities for more screen estate and weight (even something like an iPod pro is a "dumb" content consumption device in comparison). WebOS on the other hand was not about "producing/delivering on the go" so much as it was about getting your digital must haves (booking an appointment, updating a contact details, moving a meeting, ...) done and out of the way with just a couple key presses and finger flips as so distract as little as possible from the present. Only some advanced Android launchers get close, but it's never the focused, well polished and distraction-free experience it was back then (and for the same reason, Android/iOS are addictive content delivery vehicules meant to sink your eyeballs and time as to sell you stuff or collect and merchandise your data).I'm interested and wishing to see a future mobile OS that does not pander to the "attention economy" like Android/iOS are, but with billions now addicted and trapped by it, I'm realistic that it won't be an overnight success.

**pjmlp** · 2026-09-19T03:50:12.000Z：

They can easily go back 30 years ago, when each one had their own proprietary in-house OS, using current Android as baseline, or something BSD like PlayStation.

**TeMPOraL** · 2026-09-18T23:11:08.000Z：

> For a while, this could coexist with us screwing around with a real-life tricorder.Wish I could upvote you twice for that line alone. It perfectly sums up what I always wanted Android to be. Alas, the closer we are to this in hardware, the further away we are getting in software.

**mitxela** · 2026-09-19T00:58:01.000Z：

Especially Android, which is an ever-growing pile of spaghetti almost as bad as Windows.

**alightsoul** · 2026-09-18T23:01:55.000Z：

It could be disabled from the bios somehow if you knew the bios password or the bios could be reflashed with a programming Clip directly on the bios flash chip itself.

**mitxela** · 2026-09-19T00:57:27.000Z：

Normally you have to unlock the phone before unlocking the bootloader, and that is the protection.

**alightsoul** · 2026-09-19T03:19:00.000Z：

Normally the codes would be downloaded automatically from a server but sometimes the server would go down due to negligence because it would be owned by the school and well, student's laptops would start getting locked and they would have to go to a specific office somewhere in the city to get an unlock code from the it admin

**0x1ch** · 2026-09-18T20:52:15.000Z：

I think OP misspoke. He probably meant that they're not able to be unlocked by the consumers, usually.

**numpad0** · 2026-09-18T21:46:44.000Z：

It's operators that have grips on manufacturers. Phone OEMs don't make any without the sales networks and financing structures of cellular carriers.This is to extent that some carriers still insist that they design phones and phone manufacturers are just factories. People need to understand that power dynamic before blaming those "mere factories" for not making Linux phones.There has to be like an SVP of SoandSo Wireless pushing like three pillar approach of iOS, Android and Linux. Otherwise the pitch decks for any alternative phones just go straight to trash(or into a motorized shredder if it is still physical).

**mitxela** · 2026-09-19T00:59:24.000Z：

Worst case we can buy phones and physically replace their Application Processors with liberated ones.

**NetMageSCW** · 2026-09-19T18:25:26.000Z：

Apple didn’t initially - they shopped around before they found a small carrier (Cingular) willing to accept their demands. Their popularity forced all the other carriers to gradually come around.

**NetMageSCW** · 2026-09-19T18:27:04.000Z：

Or was so bad compared to the others that it was no longer viable.

**Cider9986** · 2026-09-18T21:31:01.000Z：

GrapheneOS's goal is privacy for the world and that's achieved through secure devices. You can get a phone specifically for GrapheneOS just as you choose a new device when you're buying a new one. Soon there will be two different phone brands which you can install it on. There's already an estimated 500,000 users with Pixel exclusivity.https://grapheneos.social/@GrapheneOS/117249893761790371

**drnick1** · 2026-09-18T21:39:22.000Z：

Same thing here, I use Graphene for the sake of user control. All the security features and hardening of the Pixel phones and of the OS are good to have, but they not the main reason.

**grapheneos** · 2026-09-18T21:47:57.000Z：

GrapheneOS will be available on Motorola devices meeting all of our requirements for updates and security features in 2027. It will be starting out on a high end flagship and expanding down from there as devices improve to meet our requirements. We aren't going to support devices unable to provide a reasonable level of security.

**mitxela** · 2026-09-19T01:00:09.000Z：

You can dot his but it won't be Graphene but something else, like LineageOS. As long as Graphene's selling point is extreme privacy and not just more privacy, it will be this way.

**luqtas** · 2026-09-18T21:22:51.000Z：

oh yes sure. just like we can shift the population into installing Debian into their machines so we also deter M$ and Apple abuse /s

**microtonal** · 2026-09-18T20:48:05.000Z：

You mean the Linux kernel that the GrapheneOS project has to request every update for and then has to wait up to weeks to get a Google Drive link?The GPL is worth nothing if nobody is enforcing it aggressively.

**jm4** · 2026-09-18T21:19:29.000Z：

They have their own problems. They may be "open source", but they don't accept contributions. I'm skeptical it will ever become more than a hobby project.

**takeda** · 2026-09-18T23:31:35.000Z：

It's on BSD license, Google or someone else can again Embrace, Extend, Extinguish.

**soraminazuki** · 2026-09-19T03:21:24.000Z：

Handing even a slight control over the web to an all-out white replacement theorist is somehow even worse than the status quo. Ladybird is run by the kind of person I'd never want to financially contribute to.- https://nitter.example/awesomekling/status/19693500085383702... (archive: https://web.archive.org/web/20250920103645/https://twitter.c...)- https://nitter.example/awesomekling/status/18745182953508374... (archive: https://web.archive.org/web/20250101180923/https://twitter.c...)- https://nitter.example/awesomekling/status/19712877382689095... (archive: https://web.archive.org/web/20250925185636/https://twitter.c...)- https://nitter.example/awesomekling/status/19671787088520972... (archive: https://web.archive.org/web/20250914104847/https://twitter.c...)

**godelski** · 2026-09-19T03:19:12.000Z：

That's crazy! I'm commenting from Firefox! What a crazy world! How is this even possible?!

**vsviridov** · 2026-09-18T21:11:14.000Z：

LOL, I've been using it since Netscape Navigator 3.0 Gold, via Mozilla M3 (SeaMonkey tech preview), Phoenix, Firebird, and then finally Firefox :D

**usrnm** · 2026-09-18T21:11:17.000Z：

I've been using it since the time it was called Netscape Navigator. Just sayin'

**paulryanrogers** · 2026-09-18T23:06:27.000Z：

> But the open source project wouldn’t need to invest as much as Google does.Not at first. Yet over time the work increases as one must differ more and more from Chrome. I believe that's why so many forks are giving up on Manifest V2.

**RunSet** · 2026-09-19T12:21:46.000Z：

Chrome attained its user base not by merit but by paying third party Windows installers to bundle it.

**atomicnumber3** · 2026-09-18T23:03:57.000Z：

This is cool until Google doesn't load in your free browser.

**mitxela** · 2026-09-19T00:52:38.000Z：

Windows only isn't still 90% market share because of Wine, then Proton.

**charcircuit** · 2026-09-19T01:12:52.000Z：

The developer effort is not wasted because it's open source. Anyone can fork it at any time. None of it can be thrown away from humanity, wasting it.The reason why no one runs AOSP is because the phone market rewards differentiation. Each phone manufacture wants to build their own experience and building on top of AOSP is how they do so.Is it really a losing game? Building a new OS from scratch is not worth it. Why throw away an entire app catalog for your device? Consumers want access to existing app catalogs when buying a phone. If anything is a losing game it's building a new mobile operating system over forking Android as a base.

**kjs3** · 2026-09-19T01:54:29.000Z：

Or go the other way and make web pages not programs at all, like they originally were. Unfortunately, just communicating information isn't cool, doesn't monetize, and certainly doesn't get clicks.

**AnthonyMouse** · 2026-09-19T03:33:17.000Z：

> Like you get a frame-buffer to draw on with something like a wasm vm. Web pages get replaced by programs (which they essentially are anyway).The biggest thing standing in the way of this is actually Apple, since they don't allow competing browser engines or equivalent so you can't make something like this for iOS whatsoever.

**sp332** · 2026-09-19T11:42:00.000Z：

This kills accessibility. You wouldn't even be able to select text unless the page implemented that feature itself. Screen readers would have nothing to work with. No high-contrast mode, no translation, no changing the font size, no reader mode........

**StilesCrisis** · 2026-09-19T02:49:55.000Z：

You can just look at the commit stream and see for yourself. Despite community pearl-clutching, 99% of the work is just good old fashioned software engineering.

**hex-m** · 2026-09-19T05:36:47.000Z：

OwnCloud -> Nextcloud, OpenOffice -> LibreOffice, Elasicsearch -> OpenSearch, privacyIDEA -> eduMFA

**AnssiH** · 2026-09-19T10:32:57.000Z：

The big ones that come to mind that were not already mentioned are MySQL => MariaDB, XFree86 => X.org.

**microtonal** · 2026-09-19T12:18:23.000Z：

386BSD -> FreeBSDNetBSD -> OpenBSDTo some extent I would argue that Linux is a spiritual fork of Minix and Unix.But I think it’s also worth pointing out that these were in vastly different times where a single person or a small group of people could maintain an OS. An OS or browser is vastly more complex now.

**pjmlp** · 2026-09-19T03:36:55.000Z：

Like most projects, anyone that thinks Linux or Steam will stay as they are when the generation that started it all is gone, is in for a surprise.

**necovek** · 2026-09-19T04:41:18.000Z：

MS was never broken up.

**girvo** · 2026-09-19T10:49:29.000Z：

Its still crazy to me that a judge effectively said "yes you're a monopoly, but it's too hard to break you up so we won't bother"... I'm being glib, but only slightly.

**pjmlp** · 2026-09-19T03:35:41.000Z：

Most successful open source projects have devs being paid by big corporations, including Linux itself, which only really took off in the 2000's when companies like IBM started caring.Also in the last century most software was commercial, and thanks to business friendly licenses we are back to demos, PD, Shareware and co, only with new names for a younger generation.Google will do just fine.

**datacruncher01** · 2026-09-19T07:13:38.000Z：

Google learned that it's exactly not in in their best interest when they lost their court case against Epic a few years ago which is why they are shifting focus away from open source and moving towards Apple's walled garden approach. If they had locked down their platform similarly as Apple did, Epic would probably have lost it's case for similar reasons.Granted, we know Android would not be where it is today without open source contributions.

**dzonga** · 2026-09-19T13:12:20.000Z：

companies aren't human beings with morals.companies exist for the sole reason to make money - not to make the world better - that's a side effect.but unfortunately a lot of people wanna see the world as they wish it to be, not the way it is.

**omgwtfbyobbq** · 2026-09-19T18:35:46.000Z：

I think this is a different situation than what you're describing. It's one thing when a company acts in their own interests, their communications are consistent with that, you observe that, and align with them (or don't).It's another when they say they're going to do one thing, you align with them, and then they do another later. That's generally frowned upon morally because it's considered to be deceptive/untruthful.It's not surprising, but that doesn't mean people should be ok with it, especially when other businesses get by fine making more ethical business choices, or at least avoid outright lying for their own benefit.

**cecexacjrgec** · 2026-09-18T21:49:59.000Z：

No one is forcing Mozilla’s hand (afaik) and no one is actually thinking “if Firefox had a chatbot that might convince me to move over”. Youre right that it is not a “both sides” thing, its a “Mozilla thing”. Through and through.

**cecexacjrgec** · 2026-09-18T22:25:37.000Z：

Yeah. It’s a tough balance to achieve but that’s the situation we’re in right now so Mozilla really ought to step up (and I totally wish they would).My biggest pain point at the moment (entirely subjective mind you) is not even the AI nonsense, but how disjointed and alien the Firefox UX and general feel is to Apple platforms (what I use, at the moment). I don’t want Firefox to mirror Safari 1:1 but I do want the Firefox UI and UX to feel polished, well thought out and thoroughly in line with system HIG specs—given that I spend a lot of time in a browser, it shouldn’t feel like a stranger in a strange land amidst my other desktop applications.Aggressive UI improvements would go a long way to restore some faith in the incandescent fox‘ mission—at least for me.

**epihelix** · 2026-09-19T04:18:27.000Z：

I don't understand this - what is wrong with Firefox these days? It does everything I need, and very few things I don't want.Very puzzled why there isn't more love for Firefox, even on HN.

**mitxela** · 2026-09-19T00:53:40.000Z：

I'm not sure Mozilla clears it. Zen or Librewolf or PaleMoon clears it.

**pjmlp** · 2026-09-19T03:47:00.000Z：

Firefox is no longer part of most browser compatibility matrices, what ease?

**throwaway27448** · 2026-09-19T04:03:58.000Z：

Either way we're still stuck with it.

**EbNar** · 2026-09-19T05:04:44.000Z：

Closer to 500M, actually.

**suprjami** · 2026-09-19T03:36:25.000Z：

The next board meeting, after buying at least 51% of the shares.

**pjmlp** · 2026-09-19T03:45:41.000Z：

GNU generation is over 50 nowadays, and newer don't really get open source as we used to.I mean, FOSDEM full of Apple laptops on the corridors, the message was really lost.

**layer8** · 2026-09-19T18:31:51.000Z：

Apple seems to be having more success.

**HJain13** · 2026-09-19T04:44:41.000Z：

Nothing in last 5 years; and if we ignore the last one, Nothing in almost 9-10 years. I am not sure how much weight it holds. Now if that's on Google on not accepting stuff that's different matter

**xethos** · 2026-09-19T02:21:28.000Z：

It's not the same, it does not run BBOS10, and de-Googled LineageOS will have to do for now (for me).But at least we can get updated internals for the Q20 (and soon the Passport). It'll be the closest we can get to carrying a BlackBerry for some time, if ever, and I'm happy enough with mine that I picked up a spare mainboardhttps://zinwa.com/

**altermetax** · 2026-09-19T02:54:52.000Z：

It's not GNU itself that's appealing, it's the fact that it's not controlled by a company.

**LelouBil** · 2026-09-19T11:27:07.000Z：

Valve is kinda doing that with SteamOS ? It's primarily made for their own hardware, but they also use work time to add features for installs on non valve hardware, and all of their components are open source.

**mitxela** · 2026-09-19T01:07:22.000Z：

Why would China allow the domestic sale of a device that could run GrapheneOS?

**colordrops** · 2026-09-19T01:46:50.000Z：

It's not.

**jraph** · 2026-09-19T10:36:15.000Z：

> People aren’t buying “an iOS device”, they are buying iPhoneWell, they kinda do. Apps are available on Android and iOS. They are not "available on Android, iPhone, iPad and Apple watch". iOS is actually used and recognized by the general public.

**alt227** · 2026-09-19T17:48:40.000Z：

I still dont get your point, its designed for the security audience and it has a very good reputation there. Its not aimed at normal people, by your own admission they wont even understand what it does and why they would want it. So why are you talking it down for not reaching more normal people?

**grapheneos** · 2026-09-19T19:38:36.000Z：

Samsung is already largely free from Google's egregiously anti-competitive licensing rules for Google Mobile Services. Why do you think it's going to survive for the rest? It's already unsustainable to have different rules for the largest OEM and that's without even taking into account future court victories similar to what happened in South Korea.

**NetMageSCW** · 2026-09-19T18:45:07.000Z：

You don’t know any normal people, do you?

**sgc** · 2026-09-19T13:38:44.000Z：

I went in to cash a check at a bank a few years ago and they made a huge show of it, taking over half an hour and various employees for a couple hundred dollars. They will absolutely win if they want to. A large organization can easily create more friction than an individual can bear.

**alt227** · 2026-09-19T17:44:43.000Z：

> cause they don't want to migrate off existing mainframesDont confuse intent with laziness, running on cobol genuinely gives them many advantages.

**grapheneos** · 2026-09-18T21:55:35.000Z：

Pixel 9a and earlier were officially sold as Android Open Source Project reference devices. Google made a commitment to providing 7 years of updates from launch for 8th/9th gen Pixels. Google then arbitrarily declared they were no longer AOSP reference devices with the release of Android 16 and stopped providing those updates. Many people bought Pixels due to this and it wasn't fulfilled. GrapheneOS has been able to continue support with a massive amount of work including reverse engineering, but other operating systems haven't been as successful and mostly haven't even moved to Android 17 yet or supported 10th gen Pixels.There are currently around 400k to 600k active Pixels with GrapheneOS. There have been far more than that when including the past devices our users have purchased. Pixels are a small segment of the overall market and that's substantial. If you add in people on other operating systems such as LineageOS then there are even more people using Pixels with another OS. A significant portion of people who bought Pixels did so because they were AOSP reference devices.Samsung provides 7 years of support with monthly updates for their flagship devices. Unlike the Pixel OS, Samsung ships a lot of the security preview patches early.Motorola Signature (2026) has 7 years of support. The upcoming successor to it is the first non-Pixel meeting all of the update and hardware security feature requirements for GrapheneOS.Pixel 11 currently doesn't meet our security requirements due to at least temporary lack of MTE support which may get added in Android 17 QPR2. The upcoming Motorola device is also going to be using a 6.18 kernel at launch rather than 6.12. We would have launched Pixel 11 series support already if they met our security requirements. It's likely they will down the road but it's not clear why they omitted firmware and software support for a major security feature at launch. It's the firmware part which impacts us.

**teekert** · 2026-09-19T05:44:57.000Z：

Thats a long time for a critical security patch to land (like this one [0], although it looks like it has been fixed now, at least in their alpha channel, which is annoying (not their fault) because we really need this patch).[0] https://news.ycombinator.com/item?id=4974151

**bri3d** · 2026-09-19T16:31:54.000Z：

Patch embargoes are a debate as old as security.I think the overall source embargo is rational _until_ fixes appear in a released binary build. Otherwise there's an integration/QA/rollout window where a source patch is public while the binary patch is unavailable to anyone, including attackers, which is undesirable. In "full" open source this has always been a time-suck mental gymnastics exercise around hidden mailing lists and obfuscated commit messages (which probably aren't useful in the LLM era anyway). It makes sense for Google to avoid engaging with that given they don't need to; I think it would be fully logical for them to perform source drops gated on the rollout cadence to the first available binary release channel.I fully agree the slower-than-Pixel "vendor lead time" windows are really detrimental. Once the binary patch is out, the source patch and disclosure is effectively out too; those extra windows just let OEMs continue to be lazy as a matter of policy (which they love to do regardless) while exploits are already available.

**kuschku** · 2026-09-19T08:57:31.000Z：

Google also made that argument, and further argued that they could do it better.Which is why they planned to replace the entire kernel and services with zircon and fuchsia, and a new Android runtime ontop.Guess what, turns out Google actually does need the community contributions of the Linux and Java projects.

**armadyl** · 2026-09-19T17:07:43.000Z：

This is partially pointing out that every time these discussions invariably come up, nobody addresses the cognitive dissonance of ideologues claiming that the benefit of open source like Linux and Firefox is that “the community can hard fork it and maintain a free version”Yet somehow this same logic somehow becomes invalid when any open source software made by Google is brought up.If Linux was targeted for mobile devices, there would inevitably be wasted effort reinventing the wheel just to match the feature set of Android when there’s already a suitable base to start community work from.

**d3Xt3r** · 2026-09-19T17:11:11.000Z：

Consumers also use and benefit from those features, even if they're not directly aware of it. For instance, my mom, a non-nerd who lives overseas, uses an immutable and atomic distro, which has the benefit of never breaking. Since she lives far away, it is important that her PC has that sort of stability, especially since she uses it to edit and submit important documents and emails, and ocassionally print and scan stuff. The features found in the filesystem (btrfs) further contributes to this guarantee - such as CoW, which gives her distro the ability to take instant atomic snapshots of the drive and boot from them via the boot menu; data and metadata checksumming which detects silent corruption; self healing via background scrub etc.Her PC is also 13+ years old (an old Dell Optiplex 9020), which is unsuitable for running any supported versions of Windows. The high -performance, efficient and low-memory-usage nature of Linux makes it possible for her to complete productivity tasks even on such old hardware.There are also non-nerds benefiting from Linux on low-end gaming devices such as the Steam Deck, or the countless number of emulators such as the Anbernic RG35XX Series, Miyoo Mini etc. Linux is the reason that such humble hardware is feasible for gaming.

**tredre3** · 2026-09-19T04:00:30.000Z：

The hardware capability that GrapheneOS loves to use as a shield to deny support for other devices is the ability to use custom AVB keys. Without custom keys you can't relock the bootloader after installing a custom OS on most phones. The consequences of having an unlocked bootloader are that you are susceptible to an evil maid attack.This is a real threat, but the reality is that the average person is more likely to be hacked/spied on from the software side, which Graphene would protect you from as effectively as it does on Pixel.

**cyberax** · 2026-09-19T09:19:47.000Z：

Hint: a lot of time, the real answer is "kickbacks". Find a commercial Postgres provider (EnterpriseDB) and partner with them.

**SoftTalker** · 2026-09-18T21:23:01.000Z：

Yeah I guess Apple set too high a bar and MS was caught flatfooted (again) and was too far behind.

**hurfdurf** · 2026-09-19T08:19:03.000Z：

Not doing any OS upgrades from 7 to 8 and only very few from 8.x to 10 certainly didn't help either.

**m4rtink** · 2026-09-19T07:55:31.000Z：

Sailfish OS exists as a continuation of the Maemo project, even shipped their own phone recently.

**sirjaz** · 2026-09-19T02:51:08.000Z：

I'd say Android is already worse. It uses more ram and resources to run smoothly than Windows does. Especially now that Microsoft is actively trying to speed up Windows 11 and make it use less resources.

**alightsoul** · 2026-09-19T03:04:59.000Z：

I would think they are guessing most people's passwords are weak or something. Like a screen pattern is weak, can be broken in just 300k attempts or maybe less because people use the same patterns and people can't be bothered to use passphrases.

**aboardRat4** · 2026-09-19T00:52:08.000Z：

>It's operators that have grips on manufacturersOnly in the USA.

**NetMageSCW** · 2026-09-19T18:26:15.000Z：

No, not really. It would be easier to build one from scratch.

**cesarb** · 2026-09-18T22:56:33.000Z：

> GrapheneOS's goal is privacy for the world and that's achieved through secure devices.Perfect is the enemy of good. What's better for privacy, an old but inexpensive smartphone running Android 11, or the same smartphone running an up-to-date third-party rebuild of Android 16 or newer with as many privacy-improving bells and whistles as the hardware can support?> Soon there will be two different phone brands which you can install it on....will they be available in my country (Brazil)? I don't think I've ever seen a Google Pixel phone in person.

**ysnp** · 2026-09-19T10:53:41.000Z：

What if GrapheneOS believe that privacy/security is what gives users real abuse-resistant agency and control over what happens on their device with their data?

**rrgok** · 2026-09-19T10:38:06.000Z：

Why? Just release Graphene without those security requirements. It must be a user's choice and responsibility. You sound exactly the people you fight against.You understand that just having a firewall is a big step for security?

**drnick1** · 2026-09-19T06:15:42.000Z：

There is no such thing as extreme privacy; it isn't something any phone can provide, especially if you are going to rely on third party software and services like email and instant messengers where the likes of Google and Facebook are dominant players. Even behind a VPN, Vanadium is fingerprintable by commercial trackers like fingerprint.com. Short of disabling Javascript, browsers leak enough information to basically follow anyone around the internet.

**Rohansi** · 2026-09-18T22:14:19.000Z：

It's so much easier to switch browsers than platform/OS. Unless you have an iPhone or iPad.

**olyjohn** · 2026-09-18T23:17:06.000Z：

We did it before. Thanks to Firefox we broke the IE6 monopoly even on Windows.

**godelski** · 2026-09-19T03:18:14.000Z：

You act like it hasn't been done before.Also, switching browsers is trivial. I do it on my parents' machines and they don't notice

**dvdkon** · 2026-09-18T21:42:09.000Z：

The GPL is the only reason they even get that. More enforcement would certainly be good, but it's not like the GPL is worthless without a legal team backing you up.

**nomel** · 2026-09-18T21:47:25.000Z：

Could you quote the part of the GPL that they're not adhering to (which you seem to be implying), in this situation?

**mitxela** · 2026-09-19T00:55:40.000Z：

Yes, as opposed to the Fuchsia kernel where they wouldn't even get that. We're lucky Google is institutionally incapable of creating things.

**tech234a** · 2026-09-18T21:33:18.000Z：

Commit activity actually increased after they blocked external contributions in June: https://github.com/LadybirdBrowser/ladybird/graphs/commit-ac...

**ragnese** · 2026-09-18T22:03:40.000Z：

Is not accepting contributions the only/biggest issue you have with the project? I'm honestly becoming more and more okay with the "cathedral" style of open source. Depending on the project, catering to "the community" can lead a loss of focus, lack of a cohesive "vision" or scope, and just generally trying to be everything to everyone without the resources to maintain a giant beast.With something like a browser (engine), I'm totally okay with someone saying "I'm an expert and I'm trying something with my own vision/priorities. I don't want input from random people that I have to spend time evaluating."

**bigstrat2003** · 2026-09-19T04:49:31.000Z：

That is not possible. Google, or anyone else, can make a fork of the project. But they can't take away the original from the commons.

**GalaxyNova** · 2026-09-19T07:53:02.000Z：

I don't think he said anything factually incorrect though?

**hobo123** · 2026-09-19T12:11:04.000Z：

Where in those comments is the "white replacement theorist"?

**nunodonato** · 2026-09-18T21:36:15.000Z：

Mosaic :P

**cecexacjrgec** · 2026-09-18T21:48:09.000Z：

Me too. Too bad I had to abandon it because Mozilla seem more focused on making AI-nonsense than a browser nowadays. No, Firefox, you don’t need AI features. You do need a better UI. You do need smoother scrolling. You do need privacy focus (which automatically means you do not need AI features). You do need to feel like you belong on the platform you’re installed on and not wish everything were Linux. You do need better designers that understand UX is not just “add controls everywhere”.

**epihelix** · 2026-09-19T04:26:41.000Z：

Oh, those great days when the competition was NCSA Mosaic.A simpler, better time. I miss it :(

**fragmede** · 2026-09-18T21:23:07.000Z：

Shit, remember Mosaic? Gopher?

**nunodonato** · 2026-09-18T21:36:47.000Z：

Loved netscape navigator! That entire suite with mail, website builder (composer?)

**Forgeties79** · 2026-09-18T23:23:49.000Z：

Differentiating isn’t as important as not engaging in Google‘s heinous practices

**charcircuit** · 2026-09-19T01:08:40.000Z：

Forks are giving up on mv2 because it's not as important as the people online say it is. If mv2 was what would cause a browser to gain market share they would keep maintaining it, but if the market is not rewarding browsers with mv2 then it does not make sense to maintain.

**wwiinn** · 2026-09-19T13:39:37.000Z：

Forcing it down users’ throats at the world’s most popular website might have helped. Slightly.

**cosmic_cheese** · 2026-09-19T13:52:17.000Z：

Yep. Google has been incredibly aggressive in promoting Chrome over the years, including practices similar to those Microsoft gets lampooned for doing the same with Edge.The thing is that most of this is invisible to people who already live within Google’s bubble which is probably why they don’t get called out for it. The promotion is visible mostly to those of us who don’t, and it gets irritating.

**izacus** · 2026-09-19T15:03:31.000Z：

This is complete nonsense, it's a post hoc copium where you're trying to dishonestly rewrite history from your personal hatered.Chrome was better than competition pretty much all its lifetime and there's plenty of historic articles to prove it, no matter how much your emotions refuse to accept the history.

**bossyTeacher** · 2026-09-18T23:07:21.000Z：

Then, you use this: https://duckduckgo.com/Actually, use it now.

**takeda** · 2026-09-18T23:14:10.000Z：

Actually it is still cool if they don't.Because of their enshitification we do have alternatives that were developed.At this point the their only services I'm using are Maps, Translate and Keep Notes and it is mostly due to lazyiness as all of those already have alternatives.Edit: forgot about YouTube, which is ironic, because that one is a toughest one because the value comes from creators, but I'm doing my part and using GrayJay[1] so I can follow them if they switch their platform.[1] https://grayjay.app/

**ocdtrekkie** · 2026-09-19T01:24:58.000Z：

Neither Wine nor Proton run on Windows. Building Android emulators for Linux: Worth your time. Building Android knockoffs which claim to remove the Google from Google's operating system? Foolishness.

**pjmlp** · 2026-09-19T03:39:03.000Z：

More like thanks to Apple, in what concerns desktop computing.

**ocdtrekkie** · 2026-09-19T01:26:49.000Z：

If you are not working to destroy Android, you are supporting it. You might feel happy about your custom ROM nonsense and how it protects your privacy, but that just means you're selfish, because nearly everyone will still be trapped on Google's version.Technologists need to aggressively reject solutions which don't spread freedom to ordinary users as well.

**fragmede** · 2026-09-19T01:32:38.000Z：

It wasn't worth it, but it's 2026, not 1991, when Linus first released Linux. AI can shit out a new OS, given enough tokens, and a VM/compatibility layer would let you run Android apps until native ports became available. The question is why would you want to do that? Computers are vastly more capable than they were when the Linux kernel was originally designed, and the needs of programs and their permissions have changed as well. https://xkcd.com/1200/ While throwing away all the learnings and starting from scratch are usually not justified, sometimes it is the right choice, if enough things have changed. Should GPS location, fine grained or coarse, and related permissions, be a part of the OS kernel or a user space daemon that other processes can query or some other thing? That wasn't a question when Linux was created but should be a core consideration for a replacement system that was created today, along with a myriad of other modern day questions that didn't exist back then. I don't think it's a loosing game, and I don't have the resources to make one myself, but I do think that the world's materially changed enough to justify it.

**fragmede** · 2026-09-19T01:34:54.000Z：

It wasn't worth it, but it's 2026, not 1991, when Linus first released Linux. AI can shit out a new OS, given enough tokens, and a VM/compatibility layer would let you run Android apps until native ports became available. The question is why would you want to do that? Computers are vastly more capable than they were when the Linux kernel was originally designed, and the needs of programs and their permissions have changed as well. https://xkcd.com/1200/ While throwing away all the learnings and starting from scratch are usually not justified, sometimes it is the right choice, if enough things have changed. Should GPS location, fine grained or coarse, and related permissions, be a part of the OS kernel or a user space daemon that other processes can query or some other thing? That wasn't a question when Linux was created but should be a core consideration for a replacement system that was created today, along with a myriad of other modern day questions that didn't exist back then. I don't think it's a loosing game, and I don't have the resources to make one myself, but I do think that the world's materially changed enough to justify building a new one from scratch.AI generating code changes the game significantly, though there are issues with that. A new OS would have taken several millions and multiple teams, but can now be done for far less. The problem is hardware to run it on. Who'd pay $2,000 for a shittier phone with less features when a $500 used one with GrapheneOS is right there? So the market, (in)efficiently, hasn't come up with a new phone OS. Not because it isn't warranted, but because the free market isn't a perfect system.

**realusername** · 2026-09-19T02:44:37.000Z：

> The reason why no one runs AOSP is because the phone market rewards differentiation.No, the reason is that AOSP doesn't even include a functional keyboard nor a functional call manager nowadays.AOSP apps were abandonned around Android 11, you can't just keep them as is for real users, it looks amateur.Even the open-source ROMs came to the same conclusion eventually and developed their own.

**AnthonyMouse** · 2026-09-19T04:03:06.000Z：

> The reason why no one runs AOSP is because the phone market rewards differentiation.This is what empire-building middle managers say to rationalize their boondoggles, but in actual fact most customers can't even tell the difference between two different vendors' Android skins, definitely can't tell the difference before they buy one, and the way they actually differentiate phones is on real hardware differences that show up in the specs like the camera or performance.The hardware company's idiosyncratic fork of the software is irrelevant at best and annoyingly irregular in the common case.

**swiftcoder** · 2026-09-19T11:25:27.000Z：

> The developer effort is not wasted because it's open source. Anyone can fork it at any timeAssuming you can get a hardware vendor to support your fork.Android has always been a weird blend of proprietary BSPs wedged together with the core AOSP project - we used to have an entire team whose full-time job was merging the Qualcomm BSP into our AOSP fork. At the time you didn't even get access to that BSP without inking a deal with QCOM...

**mapontosevenths** · 2026-09-19T05:13:08.000Z：

The biggest mistake the web ever made was leaving it up to to the website to choose how content renders.It should be the users choice how their browser renders, it's their damn browser. Instead, browsers are built to follow standards that mostly favor the developers preferences above those of the person who actually own the device rendering it.The modern web is user hostile by design.

**miki123211** · 2026-09-19T10:43:00.000Z：

Users want an app platform that 1) works on every device, 2) is 1-click (no app installation / management, click a link and go), and 3) has advanced capabilities which let them easily do the task at hand.Think "an interactive visualisation for choosing a seat when buying a concert ticket." That's not a "traditional" webpage, should work on whatever device the user is currently on (so native is unsuitable), and shouldn't require the user to install anything.People clearly want web pages to be exactly this; we're on iteration #3 of the idea now. Iterations 1 and 2 were Java Applets and Flash, not necessarily in that order, and they were massively popular despite their shortcomings. Clearly, if we somehow deprecated the web as it is now (which is an utterly ridiculous idea, which makes me really curious what comments like yours are exactly trying to achieve here), as long as we keep it an open standard, users will choose browsers which offer this capability in some form. We should appreciate that the current iteration is an open standard which anybody is free to implement, instead of some proprietary blob that you need to license from Oracle or Adobe.

**floxy** · 2026-09-19T05:13:37.000Z：

Apple can create a clone for their wall-garden when they want to catch up to the times.

**nottorp** · 2026-09-19T10:08:16.000Z：

Pretty sure wasm works on Safari since I've ran my own code like that...

**TeMPOraL** · 2026-09-19T12:54:24.000Z：

Unfortunately none of the things you listed are what page vendors want you to have. They'd very much prefer you didn't. On the web, they're just too hard to prevent, so most don't bother.

**MiroslavPokorny** · 2026-09-19T07:45:27.000Z：

https://en.wikipedia.org/wiki/Apache_OpenOfficeDifficulties maintaining a sufficient number of contributors to keep the project viable have persisted for several years. In January 2015, the project reported a lack of active developers and code contributions.[49] There have been continual problems providing timely fixes to security vulnerabilities since 2015.[50][51][52][53] In September 2016, OpenOffice's project management committee chair Dennis Hamilton began a discussion of possibly discontinuing the project, after the Apache board had put them on monthly reporting due to the project's ongoing problems handling security issues.[54][55][56]Sounds like AOO is effectively dead, so this example is a fail to my challenge.OpenSearch & ElasticSearch both seem alive, as well as OC & NC.Neither https://github.com/privacyidea/privacyidea or https://github.com/eduMFA/eduMFA say either is a fork of the other.I think you failed to share 3, 2 seem to valid examples of my challenge but the other 2 are questionable.

**bunderbunder** · 2026-09-19T12:52:16.000Z：

Network effects were also nowhere near as strong as they are now.BSD is a killer example of that point, too. Using a BSD Unix got to be pretty difficult after Linux containers became hegemonic.

**m4rtink** · 2026-09-19T07:39:29.000Z：

So do M$ as well ?

**izacus** · 2026-09-19T12:15:09.000Z：

Start with Apple which actually has a monopoly on mobile devices in USA and let's go from there then.You do care about the market and aren't just angry because a corp doesn't listen to your orders, right? RIGHT?

**spockz** · 2026-09-19T06:33:25.000Z：

I don’t get the hate for business licenses.I’ve seen many open source contributors deflated because they wanted to share their code/solutions with other individuals and the world to learn from only to have their work sold as a service by a big cloud vendor without seeing something back for it. Or maybe even getting more work back to support the cloud vendor for free.So I’m not surprised at all that licenses that allow commercial use up to a point and above that require seperate license or contributions back. It is still open source in a lot of ways. Can still be part of other open source distributions that themselves make no profit etc. And only companies that are more than able to pay must pay something.

**b112** · 2026-09-19T08:59:45.000Z：

which only really took off in the 2000's when companies like IBM started caring.Correlation is not causation.What I lived through, was Linux taking off like a juggernaut, and IBM embracing it as a result. Large corps came along for the ride, they didn't drive it and at best paid for some gas.DEVs being paid is simply what it is. The entire scsi/sata stack was originally re-authored by 3ware for example.Why?To sell stuff, and the guy was an advocate too.It's always been this way, under the great wonder of the GPL, blessed be it.

**lmz** · 2026-09-19T15:17:59.000Z：

> Granted, we know Android would not be where it is today without open source contributions.But the parts of Android that are majority outside developed is still available as the Linux kernel. I have my doubts that the uniquely Android bits of the userland and system services have many outside contributions.

**mahboi** · 2026-09-19T15:48:51.000Z：

I forgot about this. Epic lost the same kind of suit against Apple. That's hilarious.

**ashkankiani** · 2026-09-19T13:35:30.000Z：

And if I asked people to name companies which retain a good public perception of being not entirely profit driven, the ones that would most likely come to mind are ones like Costco, where there's someone who is setting the tone and not leaving it to the committee of free market/investors to decide the fate of the company. I wonder if there are parallels here to other similar economic models, hmm...

**tancop** · 2026-09-19T16:27:17.000Z：

Not every business owner is a profit obsessed psycho. Most multinational CEOs are but you can find good people at every level. The "only exist to make money" thing starts when you let in shareholders, but a company can stay ethical as long as they put up strong barriers before taking outside investment.A lot of people get the wrong impression from reading Dodge Brothers and think companies are legally required to put profit first. What really happened is Friedman and Reagan planted the idea of shareholder supremacy, convinced schools to teach it and now generations of business majors think it's a sacred truth they have to enforce anywhere they go. Never let a MBA take over.

**throw0101a** · 2026-09-19T18:05:10.000Z：

> companies aren't human beings with morals.Companies are not sentient beings in themselves: they are made up of human beings with wills. If the human being(s) make moral choices the result will be companies that do moral actions.> companies exist for the sole reason to make money - not to make the world better - that's a side effect.That is one interpretation on the purpose of companies (and a relatively recent one):* https://en.wikipedia.org/wiki/Friedman_doctrineThere are others:* “Profits are to business as breathing is to life. Breathing is essential to life, but is not the purpose for living. Similarly, profits are essential for the existence of the corporation, but they are not the reason for its existence.” ― Charles A. O'Reilly, Lead and Disrupt: How to Solve the Innovator's Dilemma, https://en.wikipedia.org/wiki/Charles_A._O%27Reilly_III* “On the face of it, shareholder value is the dumbest idea in the world. Shareholder value is a result, not a strategy...your main constituencies are your employees, your customers and your products.”[72] — https://en.wikipedia.org/wiki/Jack_Welch#PoliticsOr going back a few decades:> In 1949 General Foods’ president Clarence Francis told Congress that he had a “three-way responsibility to the American consumer, to our associates in this business, and to the 68,000 [stockholders in General Foods]. We . . . would serve (the company’s) interests badly by shifting the fruits of the enterprise too heavily toward any one of those groups.” Two years later, the president of Standard Oil of New Jersey claimed that managers needed “to conduct the affairs of the enterprise in such a way as to maintain an equitable and working balance among the claims of the various directly interested groups—stockholders, employees, customers, and the public at large.” So widespread were such views that, in 1959, one writer in the Harvard Business Review complained that it was no longer “fashionable for the corporation to take gleeful pride in making money.” Instead, he complained, it was typical “for the corporation to show that it is a great innovator; more specifically, a great public benefactor; and, very particularly, that it exists ‘to serve the public’.”* https://law.temple.edu/10q/purpose-corporation-brief-history...> American corporate law has long drawn a bright line between for-profit and non-profit corporations. In recent years, hybrid or social enterprises have increasingly put this bright-line distinction to the test. This Article asks what we can learn about the purpose of the American business corporation by examining its history and development in the United States in its formative period from roughly 1780-1860. This brief history of corporate purpose suggests that the duty to maximize profits in the for-profit corporation is a relatively recent development. Historically, the American business corporation grew out of an earlier form of corporation that was neither for-profit nor nonprofit in today’s parlance but rather, served a multitude of municipal, religious, charitable, educational, and eventually business purposes in early nineteenth-century New England. The purposes of early American business corporations—rather than maximization of profit to private shareholders— were often overtly public, involving development of local transportation, finance, and other much-needed economic infrastructure. With the rise of factory-based manufacturing, railroads, and other capital-intensive industries in the middle decades of the nineteenth century and the advent of general incorporation statutes, the purpose of the American business corporation shifted fundamentally from public to private. By 1860, the stage was set for the modern firm.* https://repository.law.umich.edu/mbelr/vol9/iss1/2/

**mitxela** · 2026-09-19T00:54:26.000Z：

Some people are thinking "Firefox doesn't have a chatbot so I'll use chrome" though

**josephg** · 2026-09-18T22:37:56.000Z：

What aspects feel foreign on macOS? The Firefox preferences for sure. Anything else?

**takeda** · 2026-09-18T23:25:33.000Z：

Maybe I'm not enough of an Apple fanboy but using work provided mac with firefox for 15 years I never noticed UI being disjointed from the system any more than Chrome.

**II2II** · 2026-09-19T01:55:47.000Z：

Behaving like a native application also has tradeoffs. If you're only working on one platform, then sure you will want it to behave like a native application. If you're working on multiple platforms, chances are that you're going to value consistency. And while macOS users prefer their UI, the same can be said of Linux and Windows users. Guess which one is going to win out there.

**throwaway27448** · 2026-09-19T04:04:30.000Z：

> Firefox is no longer part of most browser compatibility matrices, what ease?What would be the point of a browser compatibility matrix then?

**hurfdurf** · 2026-09-19T08:04:30.000Z：

~$585 million in 2024 (86% of total revenue) https://stateof.mozilla.org/pdf/Mozilla%20Fdn%202024%20-%20A...Mentioned as "one customer" in the PDF.

**izacus** · 2026-09-19T06:59:54.000Z：

Most of it is one liner config changes too, not much of actual code.

**ysnp** · 2026-09-19T09:45:44.000Z：

What about issue tracker discussions, mailing list discussions, security vulnerability reports etc.?

**degamad** · 2026-09-19T14:15:35.000Z：

While it's not exactly blackberry-alike, a hopefully soon-to-be-released option is the clicks communicator[0] phone. I just ordered their bluetooth keyboard attachment for androids/iphones with magsafe backs, but if it's any good, I may shell out for their phone as well.I was also a backer for the Mecha Comet[1] earlier in the year, which I'm hopeful about, although that's a couple of steps away from a daily driver phone at this stage, I guess.I never owned a blackberry, but for me, the ultimate winner would be for someone to copy or licence the layout and form of the dopod838pro[2] (a.k.a. HTC Hermes 100) and pop some newer internals in it... If I had 100 million dollars, that's what I'd be doing...[0] https://www.clicks.tech/en[1] https://www.kickstarter.com/projects/mecha-systems/mecha-com...[2] https://kaitech.hk/2006/10/dopod-838pro-htc-hermes/

**palata** · 2026-09-19T09:00:48.000Z：

Why not?

**ysnp** · 2026-09-19T11:05:45.000Z：

Historically, some very large Android OEMs based in China and selling in China also provided bootloader unlocking support in their devices including Xiaomi https://github.com/zenfyrdev/bootloader-unlock-wall-of-shame... and Oppo https://github.com/zenfyrdev/bootloader-unlock-wall-of-shame...It doesn't have anything directly to do with GrapheneOS, and would have enabled custom OS support of any Android distribution.

**exjejfjeifj** · 2026-09-19T16:23:50.000Z：

> They are not “available on Android, iPhone, iPad and Apple Watch”.No. They are available on the “Play Store” and the “App Store”. OSs are rarely mentioned. Store tags only feature store logos and store names, for device specific ones you get the device itself. The OS remains irrelevant in this scenario.

**NetMageSCW** · 2026-09-19T18:47:06.000Z：

This was literally a comment:>GrapheneOS is not made for nerds, it is made for normal people.

**alt227** · 2026-09-19T17:45:58.000Z：

Thats their issue that they want to pay several staff half an hours wage for cashing a cheque. I would have been enjoying every second of the farce.

**cecexacjrgec** · 2026-09-18T22:08:37.000Z：

> Many people bought Pixels due to this and it wasn't fulfilled.Did they though? Or is this just conjecture? Because, honestly, Pixels are not even available worldwide so a few AOSP enthusiasts dropping off and going to Graphene hardly seems concerning for the mighty G.AOSP reference was a tagline for a few nerds that still wanted the Nexus devices of yore, but it was clear from day one that Google wanted their Pixel phones to be their iPhones.

**fluidcruft** · 2026-09-19T01:14:52.000Z：

I'm pretty sure the commitment has always been is for security updates, not for the latest OS.My first phone was a Motorola that shipped with Eclair. Froyo had already been released and Motorola had a release date for Froyo scheduled in their website. They changed their mind. I don't trust Motorola one iota. Google has never lied to me they way they Motorola has. Good luck.

**NetMageSCW** · 2026-09-19T18:37:53.000Z：

“many people”? Almost no one cared when they bought Pixel is more like it.Many people bought Pixel because they saw it in a store or online. A few people bought Pixel because it was supposed to represent the leading edge of Android and it still does. Almost no one bought Pixel for AOSP reasons or even know what AOSP is.

**fluidcruft** · 2026-09-19T13:43:19.000Z：

That link has nothing to do with android or google or graphene or security patches whatsoever.

**izacus** · 2026-09-19T11:13:57.000Z：

What community contributions? Linux is mostly corporately developed with Google being one of the major contributors.Google also fully maintains the ART VM running on Android - despite Oracle, the owner and developer of Java - famously wanting a piece of it.What community contributions are you talking about there? Where does this myth come from?

**subscribed** · 2026-09-19T10:59:36.000Z：

So you're saying that being unable to prove the provenance of the image (whether it's original or not), becoming immediately exposed to downgrade attack, to someone injecting malware to /sys and you being unable to detect it.... That's not a big deal?:)Well, go for it, fork and "provide support" to the hardware hostile to non-stock OS, be a hero :)

**dpark** · 2026-09-18T22:09:26.000Z：

I don’t have visibility into what happened with the Windows Phone team, but Android from what I understand saw immediately that they needed to follow Apple’s lead and pivoted (originally they were building something closer to a BlackBerry). The Windows Phone team either didn’t believe they need to pivot initially or they just took too long to do so.Windows Phone is a case study of missed opportunity.

**ezst** · 2026-09-19T08:07:24.000Z：

Yup, I would love to try it in-hands (I looked it up on emulator many years ago, and that was frankly underwhelming). I'm also not sure about their open source situation, which was the premise of this thread.

**mitxela** · 2026-09-19T03:22:31.000Z：

That's a different axis from spaghettiness.

**free652** · 2026-09-19T04:24:02.000Z：

Haha and not true. You would need to provide objectively more than your experience. And for an example clicking on Android Contacts would be instant vs load time in Windows 11 (the one i have).

**mitxela** · 2026-09-19T03:30:59.000Z：

A screen pattern is a different way to enter a PIN with no duplicate digits. Both PINs and patterns rely upon the security processor to resist bruteforces.

**tancop** · 2026-09-19T17:02:01.000Z：

PIN and patterns are secure because the security module enforces rate limits, you can't brute force effectively if every attempt after the first 10 takes a minute. Biometrics can be even better against brute force (more possible combinations) but they are vulnerable to cloning.With a 6 digit code cracking it will take close to a year on average. With your screen pattern example it's around 100 days. That's more than enough time for the owner to notice and turn on anti theft features. Maybe even for the police to find and return the phone.

**numpad0** · 2026-09-19T05:12:09.000Z：

In quite many more countries than just USA. A lot of people would still buy phones through carriers even where they come unlocked.

**Cider9986** · 2026-09-18T23:22:50.000Z：

Are all of these unsuitable [0]?Not sure if you have any experience with eBay. I looked it up and people had problems selling to Brazil [1] but there are various listings that offer to ship. So maybe not a great option.KaBuM!, Intec Store, Performance Solutions all charge significantly more with a 10a being more than double than from Google.Motorola officially sells the Signature in Brazil [2] at the same price or cheaper than in the UK. It will be supported by GrapheneOS in 2027 on the 2027 version. From then on, hopefully Qualcomm brings MTE to the non-flagship chips and Motorola and GrapheneOS support budget or midrange devices.>perfect is the enemy of goodI don't consider that relevant when users deserve ≥ security than an iPhone. GrapheneOS is not purpose-built to avoid big-tech's services although it does that more completely than any other alternative mobile operating system, the focus is privacy.GrapheneOS on the state of privacy and security for their ethos: https://x.com/GrapheneOS/status/2044440381803069778[0] https://www.ebay.com/sch/i.html?_nkw=google+pixel+9[1] https://reddit.com/r/Ebay/comments/1d92pyn/https://community.ebay.com/forum/shipping-57923/topic/diffic...[2] https://www.motorola.com.br/smartphone-motorola-signature/p?...

**microtonal** · 2026-09-19T05:45:49.000Z：

What's better for privacy, an old but inexpensive smartphone running Android 11, or the same smartphone running an up-to-date third-party rebuild of Android 16 or newerI see your point, but it would be very misleading, since the phone would still have a lot of known holes. Only the OS would get updated, typically not the drivers, driver firmware, possibly not the kernel. The phone would still be easily compromised through all the known RCEs. So you tie up non-profit projects in a lot of extra work to get an improvement that does not really matter.This is a mess created by the OEMs and they will continue to create this mess until people will stop buying from OEMs that only give lip service to security updates (roll out Android Security Bulletins to show a high patch level, while in reality the phone the phone has many known CVEs).

**grapheneos** · 2026-09-19T17:50:52.000Z：

The purpose of GrapheneOS isn't providing a less bad operating system for insecure devices which still lacks anything close to reasonable security patches and protections. It would not be possible to provide the core GrapheneOS feature set on those devices. More importantly, they'd have many years of missing firmware, kernel, driver and HAL updates. Those are among the most important security updates and would not be available in practice. That would not be GrapheneOS and is not the purpose of GrapheneOS.

**ysnp** · 2026-09-19T10:49:05.000Z：

GrapheneOS is permissively licensed so that people can do exactly that (and fork for different hardware platforms) if they want to. It is a donation-supported open source project with a small team, and it is not a crime or moral failing for them to put those resources into doing the best that they can, instead of spreading themselves thin on something they cannot be motivated or proud of.

**grapheneos** · 2026-09-19T17:30:54.000Z：

Diverting a massive amount of resources to devices where we can never provide decent updates and our core security features doesn't interest us. It would reduce the privacy, security, usability, app compatibility and robustness of GrapheneOS for users on the officially supported devices. It would also result in many people getting insecure devices. Many people would get those devices and then realize they made a poor decision later. We already see this happen with devices approaching end-of-life and already have to put significant work into avoiding people getting those.

**mitxela** · 2026-09-19T12:54:37.000Z：

How much do you know about Graphene? It literally disables JavaScript JIT for security.

**mitxela** · 2026-09-19T00:54:58.000Z：

How did that happen, anyway? Tabs? What's the next killer feature after tabs? Maybe sync?

**microtonal** · 2026-09-19T05:36:38.000Z：

There has been a long discussion about this a while ago on HN when these delays came up. The relevant blurb:Accompany it with a written offer, valid for at least three years, to give any third party, for a charge no more than your cost of physically performing source distribution, a complete machine-readable copy of the corresponding source code, to be distributed under the terms of Sections 1 and 2 above on a medium customarily used for software interchange; or,Many people argued that 'customarily used for software interchange' is worded-as is to always be relevant to the times when the license is applied and that providing access to a Git repository is customary nowadays. In fact:- The upstream Linux tree is distributed through Git.- The relevant Pixel kernel sources used to be distributed through Git.IANAL, so I am not sure how this part of the license will hold up in court, but the spirit is clear. Providing a Google Drive link is not customarily used for software interchange.Also, I think it is fairly clear that the procedure is put in place to make everyone's life difficult, given that the relevant source used to be distributed through Git.

**seb1204** · 2026-09-18T23:26:48.000Z：

Yes I can relate to this. Picking good, valuable feedback out of the noise has become a chore.

**akho** · 2026-09-19T10:18:42.000Z：

This post is _about_ how that is both possible and common.Only GPL is somewhat immune, because Stallman was always right.

**soraminazuki** · 2026-09-19T08:29:01.000Z：

And yet again comes someone pretending as if unhinged far right rants embracing racism and white victimhood is some sort of objective truth seeking. It's unfortunate that this has become so normalized here.

**soraminazuki** · 2026-09-19T12:51:38.000Z：

> White males are actively discriminated againstThe words are unambiguous and not up for debate.

**josephg** · 2026-09-18T22:44:02.000Z：

Huh? What ai features? Firefox seems largely the same as it did a few years ago.I’m not doubting they added some ai junk somewhere. But whatever they did seems very easy to ignore.

**takeda** · 2026-09-18T23:36:24.000Z：

I'm assuming you use Lynx now then? Because I don't think you would be using Chrome or its clone if that's where you draw the line?

**mrkstu** · 2026-09-18T21:38:43.000Z：

Any fellow CompuServe users around???

**armadyl** · 2026-09-19T02:08:35.000Z：

Seriously. The average person in real life has no idea what MV2 or MV3 is. And despite what people here would have you believe uBlock Origin Lite works nearly as good as uBO and is generally indistinguishable from its MV2 counterpart. A casual user wold not be able to tell the difference, nor do they care.

**Forgeties79** · 2026-09-19T13:02:34.000Z：

That’s overly simplistic and glosses over the actual objections to mv3.

**Forgeties79** · 2026-09-19T16:57:26.000Z：

You can argue the merits of a product without personally attacking people.

**jchoksi** · 2026-09-18T23:18:56.000Z：

https://lite.duckduckgo.com/lite

**drnick1** · 2026-09-19T04:11:42.000Z：

This. Also, use OSM for maps and run your own SMTP server, if you can. Nobody should need Google.

**atomicnumber3** · 2026-09-19T05:00:49.000Z：

This works for nerds, but not for grandma who can't even describe what she's doing without using the word "google".

**mitxela** · 2026-09-19T01:30:27.000Z：

ReactOS was also a good idea.

**xmprt** · 2026-09-19T01:45:44.000Z：

Valve is working on supporting apks for their new VR operating system. If this goes anything like Proton then I'm hopeful for the future of Android without Google.

**mitxela** · 2026-09-19T02:33:17.000Z：

Reimplementing Windows was a huge task. If the windows source code was available, why wouldn't you begin with a copy-paste?

**pjmlp** · 2026-09-19T03:42:41.000Z：

You mean proprietary AI can do that, running on big corp servers.

**bigstrat2003** · 2026-09-19T04:51:08.000Z：

LLMs can't even get much simpler programs right without humans holding their hand, let alone an OS. The odds of an LLM just banging out an OS are nil.

**charcircuit** · 2026-09-19T05:17:04.000Z：

Why bother building a compatibility layer when you can just start with Android and start promoting your LLM from there?

**charcircuit** · 2026-09-19T05:14:55.000Z：

>the reason is that AOSP doesn't even include a functional keyboard nor a functional call manager nowadaysNo one was using those apps so it didn't make sense to spend time on them.

**miki123211** · 2026-09-19T10:49:20.000Z：

> the way they actually differentiate phones is on real hardware differences that show up in the specsYou forgot about one thing they care about above all others — cost.And the easiest way to keep costs down is through "alternative revenue streams", which involve your own tracking, your own app bundling deals and your own App Store, which you're pushing on users constantly. And if you do that, you may as well get the branding win from doing the custom skin too.

**Xirdus** · 2026-09-19T08:39:57.000Z：

If a web browser allows images, then the website always has full control over how content renders. It's the default. HTML and related standards are trying to persuade developers to cede some of that control in the name of accessibility, user choice, searchability, device compatibility etc. that all-image websites lack. But this can only succeed if the developers still can do everything they want to. If they can't, then they'll fall back to images and everyone loses.

**za_creature** · 2026-09-19T12:58:47.000Z：

> Users want an app platform that...So do hackers. A big chunk of the open standards revolve around sandboxing malicious code, and given the amount of tracking happening anyway, fail at it.

**NetMageSCW** · 2026-09-19T07:58:30.000Z：

Those times will never happen.

**sp332** · 2026-09-19T13:10:53.000Z：

I think that must be false. Serving the page as a static image was possible from the early days of the web, but vendors (mostly!) moved away from that as features like web fonts became available. I guess Flash was the big remaining exception. And remember Java applets? But even now as rendering to a canvas is possible, enabling animation and interactivity without necessarily including accessibility, websites are mostly not doing that. Accessibility is good for business. And sometimes it's legally required.

**Kubuxu** · 2026-09-19T08:01:06.000Z：

AOO became a thing after LibreOffice essentially won.
Before that it was OpenOffice.org owned by oracle, forked into LibreOffice in 2010, with LibreOffice getting significant traction and Oracle throwing in the towel and donating OO to Apache Foundation in 2011.

**AnssiH** · 2026-09-19T10:26:20.000Z：

LibreOffice was forked from OpenOffice.org in 2010, way before the difficulties of Apache OpenOffice (which didn't even exist back then).

**notpushkin** · 2026-09-19T14:34:38.000Z：

> Sounds like AOO is effectively dead, so this example is a fail to my challenge.You didn’t ask for examples where both projects are alive!

**bunderbunder** · 2026-09-19T12:47:27.000Z：

You would have a heck of a job convincing a court that 60% domestic market share in a two competitor market constitutes a monopoly.

**mahboi** · 2026-09-19T16:23:32.000Z：

Wow, Apple really made the right business choice only catering to people who don't care about any of this. Google set different expectations, and it already bit them with Epic.

**fauigerzigerk** · 2026-09-19T09:27:55.000Z：

It's a good idea if it actually works. Are enough commercial users paying up so that these projects get some serious funding?If companies avoid using software governed by such licenses then the overall impact is negative in my opinion, because it will lead to competing and diverging clean room clones that just split the community and the ecosystem.

**pjmlp** · 2026-09-19T14:42:56.000Z：

It was so relevant that even Wikipedia discusses this, we were using Solaris, HP-UX and Aix for actual production deployments. Linux was our MP3 server.

**dzonga** · 2026-09-19T14:16:41.000Z：

companies like Costco, Patagonia etc are rare why ? because deliberate actions & care have been taken to go against the grain of what a company should do.just like the USA at it's founding - deliberate actions were taken etc that were counter to the normal. & going against the wind takes a lot of energy.at a certain point in time - you run out of energy or you've to keep keep reinvesting to not run out otherwise barbarians are knocking down at the gate.

**tracerbulletx** · 2026-09-19T18:58:04.000Z：

Being "a profit obsessed psycho" might help some people rise to positions of power, but I think the stronger point is that a corporation is an emergent superorganism with its own identity above the individual human level, without a psychology, that operates on its own principles of self preservation based on the incentives of the environment it operates in and that individual choices result in a gestalt of behaviors that no one person really has full control over even though they are part of it and what they do does affect the overall outcome, like a cell and organs making up an animal.

**wolrah** · 2026-09-19T02:50:15.000Z：

Really? How many people can that possibly be, and how many of those would a reasonably sane developer actually want?If your competition is attracting the worst kind of users, do you really want to get in their way?

**rockskon** · 2026-09-19T03:03:06.000Z：

Are any of those people not investors?

**weikju** · 2026-09-18T23:48:48.000Z：

Tab close buttons are on the right (windows style) instead of on the left (macOS style), for one.

**cecexacjrgec** · 2026-09-19T08:33:41.000Z：

> Maybe I'm not enough of an Apple fanboyMaybe you’re too preoccupied trying to discredit valid criticism as “fanboyism” to realise how important UI and UX are for products such as browsers.Besides, Chrome itself is already an absolute mess of conflicting and downright distasteful UX choices and patterns. Firefox seems to be stuck in the past but Chrome seems to actively DESPISE being available on Mac.

**pjmlp** · 2026-09-19T04:48:16.000Z：

Compatibility between market relevant browsers.Which for the large majority of companies means Chrome and Safari nowadays.Thanks to Apple's stance on iOS, otherwise it would be only Chrome, as younger generations apparently never got the IE history lesson.

**jdjfnfjdjjeh** · 2026-09-19T08:18:34.000Z：

Lol yeah off by a factor of 6 but yeah no fucking way still standsEdit: spelling

**ricardobayes** · 2026-09-19T14:12:00.000Z：

An interesting read. If I'm reading page 20 right, they hold over 1 billion worth of investments? I've seen smaller hedge funds.

**mitxela** · 2026-09-19T12:52:41.000Z：

Because it's a totalitarian state that does not tolerate dissent? It's the same reason North Korea requires all devices to be bootloader locked to RedStarOS, but weaker.

**mitxela** · 2026-09-19T12:53:10.000Z：

Xiaomi claims to provide unlocking, but doesn't actually. I don't know about Oppo.

**NetMageSCW** · 2026-09-19T18:43:43.000Z：

Your time must not be valuable to you, which is a very limited perspective.

**samus** · 2026-09-19T19:04:21.000Z：

You don't understand. They will make you pay for it by charging a handling fee. How about $10 flat per transaction?

**teekert** · 2026-09-19T05:45:40.000Z：

I did

**grapheneos** · 2026-09-19T17:26:17.000Z：

Android's official documented listed Pixels as the Android Open Source Project reference devices until the release of Android 16. It also promised 5-7 years of support from launch.Pixels are sold in 33 countries across North America, Europe, Asia and Oceania. A substantial portion of the Pixel userbase is using other operating systems. 400k to 600k active GrapheneOS users on Pixels is a significant amount based on how many Pixels are sold. It's only one of the alternate operating systems people are using. It's not only a few users as you're claiming.

**grapheneos** · 2026-09-19T16:59:02.000Z：

No, there's a clear commitment to 5-7 years of major OS updates in addition to security updates. Both commitments have been broken for the Pixel 6 through Pixel 9a. Those were sold as Android Open Source Project (AOSP) reference devices but had the updates to it prematurely cut off with Android 16. Pixel 10 and later weren't sold as AOSP reference devices so there was no commitment to providing it, but that's not the case for the earlier devices.

**teekert** · 2026-09-19T14:24:05.000Z：

Oops, a 0 was dropped: https://news.ycombinator.com/item?id=49741510

**kuschku** · 2026-09-19T11:53:49.000Z：

> What community contributions? Linux is mostly corporately developed with Google being one of the major contributors.Linux has a lot of corporate contributors, but it's been a long standing problem that many of these only add new features that their new pet project needs. Long-term maintenace and improvements is often done by volunteers, and many important subsystems rely entirely on volunteer work.This was also famously an issue with e.g. AMD's GPU driver, which was appreciated as it allowed a mainstream GPU to be fully supported with an in-kernel driver, but the disadvantage that now volunteers had to maintain hundredthousands of LOC of code, most of which was autogenerated hardware interfaces with little documentation, which made refactoring and cleanup work almost impossible.> Google also fully maintains the ART VM running on Android - despite Oracle, the owner and developer of Java - famously wanting a piece of it.Had you followed the release notes, you'd have noticed that that hasn't been the case since Android 8 Oreo, when the entire Java standard library on Android was switched from Apache Harmony to OpenJDK. That's why Android was finally able to move beyond Java 7 and introduce modern functionality, fix the broken NIO implementation, and add JSR-310 Date and Time fuctions, just to mention a few of the improvements since then.These have been developed by the Java community, including corporations and individual contributors.

**tcfhgj** · 2026-09-19T16:16:51.000Z：

hostile to non-stock OS - where are you getting this from?

**TeMPOraL** · 2026-09-19T09:27:02.000Z：

Did you try to scroll the list tho?(Did they fix that whole "store contacts in a linked list" problem in Android already?)

**cesarb** · 2026-09-19T02:28:13.000Z：

> Are all of these unsuitable [0]? [...] I looked it up and people had problems selling to Brazil [1] but there are various listings that offer to ship.Do these phones have ANATEL certification? Because if they don't, they will be rejected by customs. It's not simply a case of the item being held until you pay a 60% import tax.

**grapheneos** · 2026-09-19T17:46:17.000Z：

Android Security Bulletins do list a tiny subset of firmware, Linux kernel, driver and HAL patches so they do require at least very minimal updates to those. Most non-Google-certified operating systems are setting an inaccurate Android security patch level by ignoring the non-AOSP portion of the patches. GrapheneOS doesn't do that but most of the other AOSP-based projects not being certified by Google are doing it. OEMs were caught doing it too but it's not clear if it was intentional in most cases as it is with the alternate operating systems.Android Security Bulletins set a very low bar since the AOSP patches are available to ship by OEMs 2-6 months prior to the bulletin being published. It's also only High/Critical severity patches being listed. Due to a recent policy change, it's also officially only a subset of the patches for AOSP. That's visible through the Android platform components having patches in the Pixel Update Bulletin for September 2026 despite those being applicable to other operating systems. It's because they no longer want to backport all High and Critical severity patches due to the high volume of issues discovered by AI models. It's similar to how they stopped backporting any Low and Moderate severity patches years ago due to high volume.

**grahamburger** · 2026-09-19T01:33:07.000Z：

Haven't all the major browsers had sync for ages? I've been using Firefox's built-in sync for so long I don't even remember what it was like without it.

**epihelix** · 2026-09-19T04:24:26.000Z：

Adblock, I would have thought. And Google can't compete in this space, by their very nature.This is the message that Firefox needs to push: Hate ads? Use Firefox.

**hobo123** · 2026-09-19T13:27:03.000Z：

I'm assuming he was talking about a specific situation where discrimination occurred? Anyway that's two completely different things.

**simondotau** · 2026-09-19T15:19:24.000Z：

“Not up for debate” is a much scarier string of words than anything that guy has said.

**olyjohn** · 2026-09-18T23:18:48.000Z：

Its just an excuse people use to keep using thier beloved shiny brand.

**nottorp** · 2026-09-19T10:11:42.000Z：

Indistinguishable because ad blocking still works at the visible end of the spectrum.Under the hood, what the MV2 uBlock can do and Lite can't is at the least stripping tracking parameters from links and block 3rd party trackers that are cloaked in a subdomain of the originating site.

**Forgeties79** · 2026-09-19T12:16:46.000Z：

You’re right it doesn’t impact most people’s decisions but m2 and m3’s differences are quite substantial and meaningful.

**izacus** · 2026-09-19T17:59:02.000Z：

The only personal insult to everyone here is such blatant lying and rewriting of history. And it's telling about the bottom barrel culture of the internet that you're angrier about having someone called out as a liar they are instead of actual lies.We were there and we didn't install Chrome via some made up toolbar installer, but because it was significantly better than what Mozilla and Internet Explorer offered.

**hobo123** · 2026-09-19T12:05:11.000Z：

Sadly, the to me most important parts of Maps are live navigation and live traffic status. I'm assuming you can't get those with osm (yet).The actual maps are much better in osm than in Google.

**skinfaxi** · 2026-09-19T06:58:21.000Z：

Nerds with grandmas can manage grandma's DNS or better yet set up MDM (I'm serious).

**wwiinn** · 2026-09-19T13:37:16.000Z：

A lot of react os helped wine/proton. It’s still was a good idea.

**pjmlp** · 2026-09-19T03:40:02.000Z：

Gamedevs would still target Android, just like they target Windows, letting Valve run after them.Android is even more of tragedy, given how all relevant NDK game development APIs are also available on GNU/Linux.

**thepasch** · 2026-09-19T09:48:43.000Z：

What proprietary AI running on big corp servers was 6 months ago is now runnable on owned bare metal compute, and there's no reason to believe this trajectory won't continue for the foreseeable future.

**troupo** · 2026-09-19T06:02:57.000Z：

So.. The market didn't actually support differentiation?

**realusername** · 2026-09-19T16:51:22.000Z：

They were used quite a lot at the time, outside of the usual Samsung/HTC, a lot of OEM didn't bother to make their own full app suite, nowadays it's necessary though

**Sophira** · 2026-09-19T12:22:32.000Z：

This is true.A lot of websites back in the 90s were just made up of images that were clickable using image maps. It was not a fun time.I get what the parent comment is saying, though, and it's why I use Gemini (the protocol[0], not the AI). It doesn't align with corporate interests, but for now I consider that a good thing.[0] https://geminiprotocol.net/

**microtonal** · 2026-09-19T12:23:33.000Z：

Yep, in the old days, a lot of websites used image maps (so that clicking a part of the image would go to another page).

**TeMPOraL** · 2026-09-19T13:18:42.000Z：

Software accessibility is bad for business - that's why it has to be legally mandated. There's no firm difference between "accessible", particularly to screen readers, and "amenable to end-user automation", and the latter is anathema to businesses.As for the styling and fonts - it's all a bunch of low-key trade-offs here. The businesses want to exercise total control over the end-user experience, for sales/marketing and branding reasons. At the same time, going off the beaten path quickly makes development costs skyrocket.Flash was a good choice back when all visitors were using a PC and there were like 3 different screen resolutions to choose from. Once laptops gained popularity, this started to shift, then pre-iPhone mobile briefly became consideration, and Flash stopped being sufficient; then iPhone came out, killed Flash, and started an era where every visitor has a different screen than the previous one. "Responsible web" became the cheapest option, and you can see its evolution as a trajectory towards giving more and more control over experience to developers, and less and less to the users.

**mahboi** · 2026-09-19T16:21:53.000Z：

Then how is Google a monopoly at 40%?

**spockz** · 2026-09-19T14:34:59.000Z：

I agree it would be bad if it leads to a lot of replication and that is even easier in this age of LLMs. But has it been shown that this will happen?

**b112** · 2026-09-19T15:06:18.000Z：

Meanwhile every startup in SV was using Linux, Facebook was using Linux, Google, and everyone in between. This was early 2000. It had immense momentum without big boys like IBM coming in (and IBM was massive compared to Google or Facebook of that day).

**mitxela** · 2026-09-19T03:23:42.000Z：

Yes you want more users not less. This is business 101. Even business 000. Customers good.

**odo1242** · 2026-09-19T01:26:21.000Z：

I mean, it’s the same on every browser except Safari

**cecexacjrgec** · 2026-09-19T08:11:15.000Z：

Not only that, but general colours are system-like but offputtingly different (dark theme is different from Mac dark theme just enough to be unsettling). Spacing (padding, margins, etc) is uneven on a lot of options, toggles and fields. Swipe back/forth being a simple arrow on the corner of the screen instead of full page swipe (like Safari) in the year of our lord 2026 is a complete disgrace (yes, chrome does this too, yes chrome also sucks). Press CMD+F and just watch as a search bar that hasn’t been updated to modern visuals in about 20 years pops up at the bottom. Pretty much everything around Firefox feels like a random collection of Windows and Linux behavioural patterns mashed together like a digital Frankenstein monster.And despite what many people here like to think: these things matter. UX improvements compound exponentially, and so do UX problems. Firefox has an opportunity here to be a first-class citizen on every OS it runs on. It has the opportunity to be the browser that respects your OS choices no matter what, but alas, Firefox seems rather content carrying its “ah yeah I remember using it back in ‘06” reputation.Firefox is not a bad browser by any means, but it feels like Firefox is the browser equivalent of the “how do you do fellow kids” meme. An out-of-time experience pretending to blend in under the guise of “AI”.

**wwiinn** · 2026-09-19T13:41:09.000Z：

They still produced Firefox OS for mobile phones.

**cecexacjrgec** · 2026-09-19T08:02:34.000Z：

> a few AOSP enthusiasts dropping off> I didPrecisely my point.

**EbNar** · 2026-09-19T05:07:31.000Z：

Considering that Firefox by itself doesn't block anything without extensions, that seemingly less than 10% of users use extensions and that tgere5are already quite a few snappier browsers that block ads by default...

**mitxela** · 2026-09-19T12:56:16.000Z：

Ooh, I think you're right. Even better if it can bypass more annoyances, cookie popups, captchas and (if legal) paywalls. Maybe it should have Libredirect built in. It could be a user agent, instead of a site owner agent.

**drnick1** · 2026-09-19T15:56:15.000Z：

OsmAnd does have live navigation as far as I understand it (turn-by-turn directions), but no live traffic status, because for that you a lot of drivers willing to surrender their location/sensor data. Anything "live" cannot be privacy respecting. I never found live traffic information particularly worthwhile to be honest.

**pjmlp** · 2026-09-19T14:46:08.000Z：

With a proprietary local stack, provided one can actually afford the hardware.

**izacus** · 2026-09-19T12:17:44.000Z：

The marked used all the different apps available from both OEMs and on Play Store.Don't be a prick.

**sp332** · 2026-09-19T13:44:13.000Z：

I'm fine with it being legally enforced. The point is, web site owners mostly wouldn't move to "a frame-buffer to draw on with something like a wasm vm".

**LocalH** · 2026-09-19T16:57:04.000Z：

That’s not the metric under which Google is seen as a monopoly, and you know it.It’s search. And ads.

**bunderbunder** · 2026-09-19T18:58:28.000Z：

It isn’t, and nobody said it is. The ruling in question did not find that Google had a mobile OS monopoly. It found that they had monopolies in both the ad server and ad exchange markets, and was using them to reinforce each other in an anticompetitive way.

**pjmlp** · 2026-09-19T16:17:21.000Z：

Really? Every single one?You must have a good source of information for such a statement.Do you want examples why Solaris was selling so well before the .com crash?

**lstodd** · 2026-09-19T17:54:23.000Z：

FreeBSD 4 was big in early 2000s.

**fragmede** · 2026-09-19T03:44:53.000Z：

Business 101 is to make sales! Users sometimes represent sales, but not always. That may be business 201 though.

**cecexacjrgec** · 2026-09-19T05:21:36.000Z：

Just because everybody does it wrong doesn’t make it right.

**weikju** · 2026-09-19T06:15:09.000Z：

Orion also does it right.Every other browser aren’t using macOS native UI therefore are wrong in this environment. But right on their own in being the same everywhere.

**II2II** · 2026-09-19T13:41:28.000Z：

Most of those are subjective details and vary from platform to platform. Fine adjustments for each platform isn't guaranteed to attract many people to Firefox either. After all, the UI/UX of Firefox is good even if it isn't excellent. Factors such as convenience (e.g. familiarity or being pre-installed) are likely bigger factors. That said, I will grant you that things like the visibility of the find bar is poor.It is also worth noting that the macOS UI/UX isn't anywhere near perfect. It is a hodgepodge of design decisions that go back to the origin of OS X or, in a few cases, the origin of the Macintosh iitself. Padding and margins may help achieve visual balance, but it's Windows management paradigm is an absolute functional mess.

**LoganDark** · 2026-09-19T10:39:46.000Z：

This is literally gaslighting; using someone's opinion as proof that nobody else holds it.

**tancop** · 2026-09-19T16:47:58.000Z：

Maybe it's time to give up privacy absolutism and add strictly opt in live data features.That reminds me, place reviews using ATProto. Kinda surprised that no map client jumped on that when it's the exact thing you need to replace a centralized service. A lot of people use Google Maps to find businesses more than directions.

**TeMPOraL** · 2026-09-19T13:58:53.000Z：

Not until it's convenient enough, then yes.Otherwise, explain Flutter.

**b112** · 2026-09-19T16:50:38.000Z：

There are several 'early 2000s' after the .com crash. Linux growth was phenomenal, and as tends to happen with growth, starts with smaller market share.There is no conflict in "linux was growing without the big boys' and 'it started with small market share'.And yes, you can find exceptions to the rule, although regardless, do you see me saying "exclusively"? What does someone using Solaris, have to do with Linux only growing due to external help?

**b112** · 2026-09-19T19:27:41.000Z：

Yes, yet it was. There were the BSDs, some more popular than others. A lot of the time, especially back in the earlier days, stuff was more regional.There certainly were mailing lists, usenet, forums, all of an all-encompasing scope. But there were also very local user groups, and pockets of wildly more and less usage depending upon region. The Internet was young, and many made decisions predicated upon what they saw around them.The best way to be sure you had support, was a local healthy community of hackers around.

**mitxela** · 2026-09-19T12:56:40.000Z：

This is about market share of a nonprofit - it's users.

**cecexacjrgec** · 2026-09-19T08:23:59.000Z：

Unfortunately “being the same everywhere” only works if your application is distinctive enough in functionality that it can’t be anything else but itself. Firefox is just a browser. Safari is also a browser. Chrome is also a browser. And none of these apps are more important or relevant than the operating system they are working under.If my OS says windows and tabs close on the left, then I expect every single app to be a good platform citizen and not make me relearn default controls just to operate simple functions. Windows and tabs close on the left. End of story.

**exjejfjeifj** · 2026-09-19T16:27:54.000Z：

Your argument boils down to “but Mac’s HIG isn’t perfect and UX/UI criticism is nitpicking”. OP is right though, UI/UX matters and despite Mac’s HIG being a mess, it is the Mac’s mess and users expect a Mac-like mess, Firefox should not be taking things into its own hands either way.

**izacus** · 2026-09-19T11:06:33.000Z：

No, this isn't what gaslighting is or means.

**exjejfjeifj** · 2026-09-19T16:24:32.000Z：

It quite literally isn’t.

**exjejfjeifj** · 2026-09-19T16:29:04.000Z：

Precisely their point: users don’t necessarily mean sales, but they MIGHT bring in donors.

**II2II** · 2026-09-19T18:07:01.000Z：

Maybe I shouldn't have included that second paragraph, since that's not my point. The second paragraph was more of an expression of frustration with how elements of the Apple user base regard macOS as the pinnacle of user interfaces and how everyone places an extremely high importance upon even minor elements.Then again: while I believe bad UI/UX is a thing, I don't think there is an ideal. Different people think in different terms, or have different preferences. Some forms of interaction are better in one domain than another. There are undoubtedly many other reasons.As for Firefox taking things into their own hands, that's the developer's decision. I have already given two reasons why that may be the case (users may expect consistency across platforms, and it may require too much effort for too little return).

**LoganDark** · 2026-09-19T11:11:39.000Z：

Saying that holding a particular opinion makes you irrelevant is not gaslighting? It's not nice to respond to a frustrated developer by saying they don't exist. It feels comparable to saying someone's concerns are not real, which does amount to gaslighting to me.

**fluidcruft** · 2026-09-19T13:41:51.000Z：

Gaslighting is making a person question the validity of their own true memories.

**NetMageSCW** · 2026-09-19T18:40:59.000Z：

No one says graphene os doesn’t exist, or the developers don’t exist, just that their opinions don’t matter because they are a miniscule fraction of the market. 2% of active devices drives no decisions at Google.
