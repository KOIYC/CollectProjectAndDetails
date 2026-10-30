---
type: "corpus"
item_id: "eac01b4af689c91d"
title: "Show HN: Auto Dismiss Mac OS \"Allow <app> to find devices on local networks?\""
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50294506"
project_url: "https://github.com/johncassil/dontallow"
author: "johncassil"
published_at: "2026-10-29T19:27:44Z"
captured_at: "2026-10-30T09:46:09+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-30"
pub_day: "2026-10-29"
tags:
  - 语料
  - hn_show
  - author_johncassil
  - story_50294506
  - show_hn
  - front_page
metrics: {"points": 100, "comments": 76, "engagement_velocity": 100}
comments_count: 76
comments_total: 76
discovered_via: "hn:show_hn:3d"
---

# Show HN: Auto Dismiss Mac OS "Allow <app> to find devices on local networks?"

> [!info] 一句话导读
> This popup has been a constant gripe of mine for years. I almost NEVER want to allow this permission and there is no system setting to disable it globally and p…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50294506>
> 指标：点赞=100 · 评论=76 · engagement_velocity=100
> 作者：johncassil　|　发布：2026-10-29T19:27:44Z
> 项目链接：<https://github.com/johncassil/dontallow>
> 采集：2026-10-30T09:46:09+08:00　|　id：`eac01b4af689c91d`

## 正文

This popup has been a constant gripe of mine for years. I almost NEVER want to allow this permission and there is no system setting to disable it globally and prevent the popup from interrupting your typing, etc. This tiny swift app I built will autoclose it in 1/4th of a second and leave behind a little notification that it did so. Would love to hear feedback!

## 评论（76/76）

> **poszlem** · 2026-10-29T19:39:25.000Z　
> Yes. Thank you. This is such a simple thing that should be a part of the operating system, and in the ideal world it would be. This is the perfect problem for the LLM to solve, because the reason it does't exist in the system is a decision by some stupid PM at Apple, and not an actual system constraint.

---

> **browningstreet** · 2026-10-29T19:40:04.000Z　
> Thanks. It’s macOS' own cookie banner and dick bar.It’s weird they haven’t just made this a menu flag…

---

> **LoganDark** · 2026-10-29T19:43:12.000Z　
> "One Swift file" except it's two Swift files

---

> **HughParry** · 2026-10-29T19:47:06.000Z　
> side note but what is the consensus on figuring out whether small brew packages like this one are malicious?I'm sure this one probably isn't, but I have no clue how I would know whether it is without reviewing the source code myself (or pointing an agent at it etc)

---

> **john_strinlai** · 2026-10-29T19:47:23.000Z　
> this is exactly the type of app that makes me excited to see what the future will hold with ai. any regular joe or jane can now realistically solve many of their small annoyances with little effort and no experience.(not saying this is ai or not, i have no idea, just speaking generally)

---

> **nottorp** · 2026-10-29T20:00:32.000Z　
> Hmm another gripe of mine. Mac OS's vnc brings a popup that steals your focus when someone connects to the machine while you're physically in front of it.I know it's well intentioned but I have this weird setup where I am almost constantly keeping vnc on from my laptop to my desktop. And the mbpro randomly wakes up to do whatever, even when not used, which reactivates the vnc connection, which pops up a warning on my desktop, which steals my focus.Anyone knows a way to disable that? Possibly just for connections from a specific other machine.Edit: as for this app, I think the OS only asks once for a new app? I don't remember being asked a second time even when denying it.I could also whine a bit about "this app wants to access files on a removable volume" since my desktop has a thunderbolt ssd plugged in for extra space...

---

> **InsideOutSanta** · 2026-10-29T20:09:03.000Z　
> Can I have the opposite, a tool that automatically clicks on "allow"? I installed the app, it's fine.

---

> **ShinyLeftPad** · 2026-10-29T20:19:15.000Z　
> Have a problem with pesky permissions dialogs from sandboxed apps? This unsandboxed unverified app that requests Accessibility permissions, to the rescue!

---

> **jshier** · 2026-10-29T20:28:41.000Z　
> I'd rather something tell me exactly why this popped up in the first place, as every new OS version seems to introduce more triggers. I have apps that now pop this up when I quit, which doesn't make much sense.

---

> **tobi_bsf** · 2026-10-29T20:30:05.000Z　
> Says a lot about the state of Mac OS.

---

> **skissane** · 2026-10-29T20:52:40.000Z　
> The big problem with these permission dialogs, is their lack of technical detail about what the app is actually trying to do which triggers them.How do I know whether to say "Allow" or "Disallow" when it gives me no idea what either option actually means in concrete?

---

> **mschuster91** · 2026-10-29T20:55:40.000Z　
> > Chromium browsers (Chrome, Brave, Edge, Island, Arc) copy their own app bundle into a random temp folder at launch so the code signature survives in-place updates. macOS keys the Local Network decision to that random path, so the next launch looks like a brand-new app.OH DEAR GOD that explains so much other cursed behavior, including the "do you want to allow google chrome helper to show notifications" always reappearing. or teams. or anything that does autoupdates.> Nothing on a typical Mac needs this permission except a printer or scanner utility, a media server, or a LAN-discovery tool, and those you answer once and they're done.This is wrong. Browsers and media players need it because that is how multicast discovery for stuff like Chromecast works. Spotify, same thing. And Steam plus virtually all games with LAN multiplay for the same reason. Did I note already that Steam also has an autoupdater and so does Spotify and... argh.Apple really needs to fix the very first point, preferably in a way that doesn't force app developers to ship a "helper" binary.(Side note: it might even be the case that opening the file picker may be enough, if you got network-discoverable paths in your Finder Locations sidebar, but i'm too tired to test that one out...)

---

> **dingdingdang** · 2026-10-29T22:43:16.000Z　
> This is the sort of classic MacOS situation that has mandated the use of Hammerspoon scripts and the like for more than a decade by now (this is not a sectarian point btw, Windows requires winutil just the same according to my optics)

---

> **tonymet** · 2026-10-29T23:56:19.000Z　
> Permissions consent prompts are broken. they are far too coarse, and out of context. The customer is forced to consent without knowing the scope or what will break.A better experience would be an async consent screen, with placeholder content and calls to action until permission is granted.For example, a network ping scanner could show placeholder host names & status until the user clicks to allow access.The operating system could easily stub the sensitive APIs with placeholder content and a flag indicating the content is false. So even legacy apps could work.

---

> **crazygringo** · 2026-10-30T00:35:05.000Z　
> Amazing. I'd LOVE for you to expand it, to also auto-dismiss "Foo.app would like to access data from other apps."Adobe programs ask for this every time they start, and Claude Code randomly asks me this daily out of nowhere. It doesn't matter how many times I click "Don't Allow", it never gets remembered. (But of course if I ever mistakenly click "Allow" even once, that gets remembered for eternity and I never get asked again...)

---

> **klodolph** · 2026-10-29T19:44:24.000Z　
> It’s just a choice of which key to use. I don’t think it was some decision made with this intent, I think it is just the unexpected result of a decision.

---

> **johncassil** · 2026-10-29T20:08:34.000Z　
> I maintain that Steve Jobs would have taken the engineers to task over this poor UX.

---

> **hmokiguess** · 2026-10-29T19:56:31.000Z　
> One bunch of Swift

---

> **johncassil** · 2026-10-29T20:07:08.000Z　
> oof, it was originally one, forgot about the refactor lol

---

> **sigmoid10** · 2026-10-29T19:50:21.000Z　
> Basically the question for any executable code (or even just any data) that you let on your machine and which did not go through independent vetting processes. The question you need to ask is if the benefit (getting rid of an annoying popup) is worth the risk of a distribution method that is trivial to compromise.

---

> **hmokiguess** · 2026-10-29T19:55:41.000Z　
> so we are back at choosing where we draw the line and you picked this one to get us going

---

> **johncassil** · 2026-10-29T20:07:54.000Z　
> Good question -- I have been pointing claude at repos for security reviews before I install stuff now for exactly this reason.

---

> **poszlem** · 2026-10-29T20:12:35.000Z　
> That's why I like small, open source projects like this one. I don't have to figure out if it's malicious. I just fork it, then ask claude to review the code, then run my own fork.

---

> **ASalazarMX** · 2026-10-29T20:33:27.000Z　
> Even if they're not malicious, there's no guarantee that they won't become malicious in the future. Prefer living off the land, and install only the very essential extras.

---

> **scosman** · 2026-10-29T19:51:36.000Z　
> Yes! I got annoyed that I had to manually close old finder/preview windows, so I OSSd an app that closes any stale window. There have been commercial apps in this space a decade, but none worked how I wanted (per window not per app, config each app separately). So I just made it with Claude using some spare tokens at the end of the week. You can customize anything to be the way you like it now.https://github.com/scosman/Squeegee

---

> **johncassil** · 2026-10-29T20:21:55.000Z　
> https://forums.macrumors.com/threads/repeated-allow-google-c...You can see other people with tens of instances of the same app in the settings for this

---

> **johncassil** · 2026-10-29T20:16:30.000Z　
> I assume that is a quick fork and publish, but seems scary lol

---

> **mostlysimilar** · 2026-10-29T20:17:28.000Z　
> Sometimes you need to use a particular piece of software but don't want all of its functionality. You're allowed to want some but not all.

---

> **nobleach** · 2026-10-29T20:48:37.000Z　
> So you're kinda looking for a "I want to allow this software to do whatever it wants - I accept all risks?" button? And with each new update you're re-evaluate?

---

> **Qerub** · 2026-10-29T21:53:53.000Z　
> You can allow-list certain IP address ranges to not need the local network permission and I believe that should stop the popup from appearing (but I'm not sure). See https://developer.apple.com/documentation/technotes/tn3179-u... for more information, TL;DR: sudo defaults write com.apple.network.local-network AllowedEthernetLocalNetworkAddresses -array "169.254.0.0/16"
>  sudo defaults write com.apple.network.local-network AllowedWiFiLocalNetworkAddresses -array "169.254.0.0/16"

---

> **seemaze** · 2026-10-29T21:29:23.000Z　
> It's a couple hundred lines of code. You could just, like, read it.

---

> **ryandrake** · 2026-10-29T22:34:22.000Z　
> Ideally, every API to call a function that provides the developer "dangerous" access to your system, should give the developer a text string argument to explain/justify to the user why it's needed. Then, instead of a confusing "Do you want this app to use Bluetooth?" pop-up with zero context, you let the developer convince the user.

---

> **bigwheels** · 2026-10-29T20:31:31.000Z　
> Did Apple hire some of the folks who created Windows 11? How else can this trend be explained :)

---

> **OptionOfT** · 2026-10-29T21:40:41.000Z　
> Well, usually the answer is no, and then when something breaks the app will tell me.Which reminds me. Why does the CVS app need access to Bluetooth?

---

> **joshuat** · 2026-10-29T22:18:26.000Z　
> This also happened on iOS when they began to prompt users before apps could access the clipboard. I built an app that would handle the inbound redirect automatically if you had a relevant URL in your clipboard - did this for years with many users happy with the feature.Then it started prompting users before allowing them to paste, and then the claims of privacy violations began to come in.If instead I were able to specify what was happening in the prompt rather than iOS giving users an ambiguous statement, or even provide a detection pattern, it wouldn't have been nearly as bad.I feel like this really harms security and privacy awareness by flooding the field with unimportant prompts/warnings to the degree that a real issue is similarly ignored because it is assumed to just be noise.

---

> **johncassil** · 2026-10-29T22:43:37.000Z　
> Even for chromecast and spotify I never want or use these features, and if I am not turning such a feature on I never want to be asked about a permission related to it, as a user. If I am turning a feature on or I am trying to use chromecast, THAT is the time to prompt me about it

---

> **bluehex** · 2026-10-30T00:09:14.000Z　
> The permission keying off of a temp folder feels so broken. I don't know whether Google / Chrome deserves the blame for the weird hack of running an app from a place the user never specified or Apple the OS for making such a hack necessary and not giving the permission system a way to understand the canonical user installed app as the source of the request.

---

> **hurfdurf** · 2026-10-29T23:02:28.000Z　
> Swifties are everywhere

---

> **ShinyLeftPad** · 2026-10-29T20:21:45.000Z　
> It's so funny to read these, as if countless examples didn't prove that llms don't actually distinguish between your instructions and the data they read at your request.Do you think a malicious repo author won't think of hiding a suitable prompt within?

---

> **johncassil** · 2026-10-29T20:11:01.000Z　
> This particular item never been a problem for me because I incessantly close everything after I am done with it but it is super cool that we can ask AI to dig into the weeds for us now and fix our annoyances -- or even search repos online where someone else had and fixed this problem

---

> **eastbound** · 2026-10-29T20:11:03.000Z　
> The first app I will do is Spotlight. Its insistence on finding everything across the universe except applications is tiring.We're getting free from our software!

---

> **ASalazarMX** · 2026-10-29T20:31:04.000Z　
> I don't know what Apple is looking for. The iPhone ships with a Weather app preinstalled, you allow it to your location so it can warn of severe weather, and several weeks later "OMG WEATHER APP IS USING YOUR LOCATION!!11!".Same with MDM agents. Ours are installed automatically as part of the Apple Business Manager configuration, we manually grant them precise location in the background, and months later "HEY USER, WANNA BLOCK LOCATION FROM 'MDM SERVICE'?".Edit: To avoid replying to the two following comments with the same reply, my gripe is not about the notification, that's a good thing; my gripe is with their implementation, which seems very in tune with Apple's way of complying with regulations. There are definitely many user-friendly ways to handle privacy compared to seemingly random notifications.

---

> **InsideOutSanta** · 2026-10-29T20:34:22.000Z　
> I didn't say you weren't. I'm asking for myself, not for you.

---

> **prepend** · 2026-10-29T20:53:03.000Z　
> Yeah. That’s how installing an exe has worked for a long time.

---

> **InsideOutSanta** · 2026-10-29T21:16:03.000Z　
> > So you're kinda looking for a "I want to allow this software to do whatever it wants - I accept all risks?" button?Yes.> And with each new update you're re-evaluate?No. Hope that helps.

---

> **ryandrake** · 2026-10-29T22:17:14.000Z　
> Some people like to live dangerously!

---

> **danpalmer** · 2026-10-30T00:17:40.000Z　
> "I want to allow the software to talk to devices on my local network", not "whatever it wants".I've never had a case of this where the access was malicious, and devices on my network have security controls. For me this popup is exceptionally low value.

---

> **ShinyLeftPad** · 2026-10-29T21:34:49.000Z　
> Well I don't have the problem it's trying to solve so I don't need to. But among people who install it, how many will? And remember to do it again before every upgrade?

---

> **thiht** · 2026-10-30T00:20:18.000Z　
> Agree with that, I like the idea of permissions for specific things like this but it’s way to hard to know what’s actually being asked and why.

---

> **ChromeUltron** · 2026-10-30T00:45:47.000Z　
> Yes they are hiring H1Bs at the same level as the rest of F_GMAN

---

> **kotaKat** · 2026-10-29T21:57:03.000Z　
> Oh! There's actually good reason!If you have an Extracare card, in some markets, you can self-unlock the locked display cabinets with the CVS app (because they have your identity via the ExtraCare card which adds inherent trust).It's powered by the Invue smartlock platform. https://invue.com/smart-lockshttps://abc7ny.com/post/cvs-testing-new-nyc-shoppers-open-ca...

---

> **ryandrake** · 2026-10-29T22:31:02.000Z　
> I think the visibility of these dialogs serves as a warning to the user--but they should do a better job directing the user's attention to where the threat is. If the user is getting annoyed at all these pop-ups, he should direct this annoyance at the developer who is (in all likelihood) asking for access to more of the user's computer than he needs.The fact that there are so many popups should mean apps are reaching for access to your system way beyond what they should be. It shouldn't mean Apple needs to get rid of the pop-ups.

---

> **dd8601fn** · 2026-10-29T22:50:47.000Z　
> > If instead I were able to specify what was happening in the prompt rather than iOS giving users an ambiguous statementNo. They’re correct, there.The app developer should not get to provide the message text for a prompt like that.A secondary note somewhere in less than ten words, maybe, where it explicitly warns that the statement may be false.

---

> **internet2000** · 2026-10-29T23:36:54.000Z　
> Counterpoint: do not read my clipboard without any action on my side, dude!

---

> **QuadmasterXLII** · 2026-10-30T00:50:08.000Z　
> as a user with an itchy delete app finger, this is exactly why i like apple.

---

> **NavinF** · 2026-10-29T20:31:00.000Z　
> > countless examplesShow me just one where a frontier model got prompt injected when checking if code if malicious.FWIW I can do this, but I bet you can't.

---

> **LoganDark** · 2026-10-29T21:00:26.000Z　
> Sometimes I am shocked by how blind Spotlight is. I will have something in my applications folder with a straightforward name -- say, Steam.app -- and it will keep picking the shortcut generated by CrossOver for the Windows version of Steam, that is nested inside a bunch of subfolders. Wtf? I ended up renaming the CrossOver version to WinSteam so it stops prefix-matching.

---

> **VCFundedGenYer** · 2026-10-29T20:33:08.000Z　
> That was due to antitrust pressure such that they did not self-prefer their own apps.

---

> **sam1714** · 2026-10-29T20:33:20.000Z　
> The first scenario is due to anti-trust complaints forcing Apple to treat their pre-installed apps identically to third-party ones. (Also why you can "delete" system apps.)

---

> **bdavbdav** · 2026-10-29T20:36:59.000Z　
> Doubly annoying as it asks for the widget separately.

---

> **mostlysimilar** · 2026-10-29T20:49:20.000Z　
> Okay, to me it reads like a lazy swipe. You seem to be aware of the power of AI to build you whatever you want, so why ask this question like this? It seems like you're just trying to tell people they should fully trust the software they install.

---

> **reaperducer** · 2026-10-29T21:22:28.000Z　
> You're installing exes on macOS? You've got bigger problems than dialog boxes.

---

> **vorpalhex** · 2026-10-30T00:34:35.000Z　
> Honestly it can drain my crypto wallet or whatever as long MacOS stops doing an imitation of Windows Vista with a billion security pop ups.

---

> **ButlerianJihad** · 2026-10-29T22:00:57.000Z　
> Ah, are you telling us that while people were outraged about rampant theft and pointing to all the locked-up merchandise as emblematic of the corporate response to rampant theft, even while there wasn't enough staff to unlock the cabinets... but the lockups are also a way to entice customers to install the app, sign up for an account, and enable Bluetooth all the time?https://youtu.be/zS9U3Gc832Y?si=BmVOHE6ahKLbw82c

---

> **johncassil** · 2026-10-29T22:39:30.000Z　
> Regardless, apple should definitely not send popups unless an app is being engaged with.

---

> **mook** · 2026-10-29T23:16:22.000Z　
> I get the pop-up semi-frequently from Chrome. I don't think complaining to Google has ever helped with anything; but then it's not like complaining to Apple has a better track record.Yes, I don't know why the OS isn't tracking the pop-up by bundle id or anything. It's not like I changed my mind the last dozen times…

---

> **i386** · 2026-10-29T23:56:34.000Z　
> This is the correct answer.

---

> **ShinyLeftPad** · 2026-10-29T20:35:32.000Z　
> Here's prompt injection via a harness for example: https://www.promptarmor.com/resources/google-antigravity-exf...took me about 30 seconds to find. there's tons of them. of course it's an arms race, the models get better the harnesses get better the attackers get better but again: for the model itself, your prompt and third party data it reads are the same thing (input). as long as it is true, the attack will always be possible.

---

> **cowlevel** · 2026-10-30T00:15:30.000Z　
> You'd think that would force them to make the third party app experience as good as the first party app experience. Instead, they did the opposite...

---

> **cwmoore** · 2026-10-29T20:50:21.000Z　
> So many smart people and yet such a stupid timeline.
> Usability psychology is well documented.

---

> **InsideOutSanta** · 2026-10-29T21:16:38.000Z　
> No, I'm very obviously not, and the only lazy swipe was your response.

---

> **daveidol** · 2026-10-29T23:45:43.000Z　
> C'mon they meant 'executable' more broadly, not literally a '.exe' Windows program.

---

> **mjdiloreto** · 2026-10-29T22:04:15.000Z　
> Are you telling us we're being increasingly policed by technology?Yes! This is part of the Flockification of everything.

---

> **kotaKat** · 2026-10-29T22:09:53.000Z　
> I mean, I didn't go to the worse version. Step right up to the little display, enter your phone number, smile for the camera, and the case unlocks magically!https://indyme.com/solutions/freedom-caseThe CV footage just adds that extra comfortable feeling, doesn't it?https://indyme.com/hubfs/E6A61CF7-E252-4994-91E1-0FC0E88781F...It's "freedom" for "honest shoppers"!

---

> **aesthesia** · 2026-10-30T00:30:40.000Z　
> Seems like this is a signal that they in fact take the privacy concerns seriously?

---

> **gs17** · 2026-10-29T22:58:34.000Z　
> Even better, they have a model called the "Freedom Cage"!

## 导航

- 项目页：[[10-项目/github.com_3fc7476d]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
