---
type: "corpus"
item_id: "d9f5344f664206df"
title: "We Need to Talk About How Gross Modern Web Design Has Become (And How We Built an AI to Catch It)"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/dj29/we-need-to-talk-about-how-gross-modern-web-design-has-become-and-how-we-built-an-ai-to-catch-it-5gin"
project_url: "https://github.com/Tarkash-Labs"
author: "Dhruv Jani"
published_at: "2026-10-30T11:35:31Z"
captured_at: "2026-11-07T09:46:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-04"
pub_day: "2026-10-30"
tags:
  - 语料
  - devto
  - discuss
  - showdev
  - webdev
  - gemini
metrics: {"reactions": 93, "comments": 38, "reading_time": 4}
comments_count: 38
comments_total: 38
discovered_via: "devto:showdev"
---

# We Need to Talk About How Gross Modern Web Design Has Become (And How We Built an AI to Catch It)

> [!info] 一句话导读
> Let me paint a picture I know you’ve experienced recently.

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/dj29/we-need-to-talk-about-how-gross-modern-web-design-has-become-and-how-we-built-an-ai-to-catch-it-5gin>
> 指标：reactions=93 · 评论=38 · reading_time=4
> 作者：Dhruv Jani　|　发布：2026-10-30T11:35:31Z
> 项目链接：<https://github.com/Tarkash-Labs>
> 采集：2026-11-07T09:46:31+08:00　|　id：`d9f5344f664206df`

## 正文

Let me paint a picture I know you’ve experienced recently.

You’re trying to book a flight, buy concert tickets, or just download a simple PDF converter. Suddenly, the website turns into an absolute warzone:

🚨 *"ONLY 2 SEATS LEFT AT THIS PRICE!"*
⏳ A blood-red countdown timer ticks down from 05:00.
🟢 Three massive, glowing "DOWNLOAD NOW" buttons appear, and you *know* two of them will install malware.
🥺 And when you try to close the popup? The only button says, *"No thanks, I'd rather pay full price and be miserable."*

**We call this "marketing." But let’s be honest: it’s just deceptive engineering.**

These are **Dark Patterns**—UI/UX choices intentionally designed to trick, guilt, or force you into doing things you didn't want to do. And honestly? It’s getting gross. As developers, we build the web. We shouldn't be okay with the web actively manipulating its users.

So, my team at [Tarkash Labs](https://github.com/Tarkash-Labs) decided to fight back. We built a cognitive visual shield to catch these patterns in real-time.

Meet **OmniGuard AI**.

{% youtube vR4NOdhGkRE %}
*(Watch the 1-minute demo above to see it catch fake timers and hidden fees live!)*

---

### 🛡️ How OmniGuard Works (The Tech Stack)

The problem with most ad-blockers or privacy extensions is that they rely on static blocklists or CSS selectors. But modern dark patterns are dynamic. They are disguised as regular DOM elements.

To catch them, we needed a tool that could *see* the web exactly how a human sees it.

We built OmniGuard as a Manifest V3 Chrome Extension powered by a **FastAPI backend** and **Gemini 3.7 Flash**.

Here is the exact flow:

**1. The "Eyes" (React 18 + Vite Extension):**
When you click "Scan" (or enable auto-scan on scroll), the extension captures an ephemeral, highly compressed screenshot of your active viewport.

**2. The "Brain" (FastAPI + Gemini 3.7 Flash):**
The image is sent to our stateless FastAPI backend. We use Gemini 3.7 Flash’s multimodal capabilities to analyze the visual context of the page. It doesn't just read the code; it understands *how the UI looks*.

**3. The "Shield" (Shadow DOM Injection):**
If Gemini detects a dark pattern, the backend streams the exact coordinates back to the extension. We then inject a **Shadow DOM** layer over the page, drawing glowing red bounding boxes precisely over the deceptive elements—completely isolating our CSS from the host page's styles.

---

### 🕵️‍♂️ The 6 Villains We Hunt

OmniGuard is currently configured to detect six specific categories of visual deception. Here is how it catches them in the wild:

**1. Disguised Clicks**
Buttons masquerading as something else (like fake downloads that lead to ads or malware).
![OmniGuard catching disguised clicks](https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/disguised-clicks.png)

**2. Confirmshaming**
Guilt-loaded opt-out language designed to make you feel bad for not subscribing.
![OmniGuard catching Confirmshaming](https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/confirmshaming.png)

**3. Urgency Traps**
Fake countdowns and artificial scarcity messages.
![OmniGuard catching urgency traps](https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/urgency-trap.png)

**4. Hidden Costs (Drip Pricing)**
Fees and excluded taxes that magically appear at the very end of a checkout journey.
![OmniGuard catching hidden costs](https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/hidden-costs.png)

**5. Sneak into Basket**
Unwanted software bundles or insurances silently pre-checked during a download or checkout.
![OmniGuard catching sneak into basket](https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/sneak-into-basket.png)

**6. Forced Continuity**
"Free trials" that hide their aggressive auto-renewal terms in the fine print.
![OmniGuard catching forced continuity](https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/forced-continuity.png)

---

### 🔒 Zero-DB Privacy Architecture

One of the biggest challenges of building an AI extension that takes screenshots of your browser is **privacy**. We knew from day one that if we were building a tool to protect users, we couldn't compromise their data to do it.

That’s why the OmniGuard backend is **100% stateless**. It uses a zero-DB architecture. The viewport screenshot exists only in memory for the milliseconds it takes Gemini to process it, and is then immediately destroyed. Nothing is ever saved, logged, or stored.

---

### 💻 Try It Yourself (Open Source)

We’ve open-sourced the entire project. If you want to see how we handled Manifest V3 tab capturing, or how we prompted Gemini Flash for UI coordinate mapping, you can check out the repo here:

{% github Tarkash-Labs/OmniGuard %}

Massive shoutout to my teammates **Yug Vasava** (Lead Dev) and **Avadh Vaishnani** (Lead QA) for helping bring this to life.

### 👇 Now, I need to know...

We are constantly trying to improve the AI's detection capabilities.

**What is the most unethical, infuriating, or downright gross dark pattern you’ve seen a company use recently?**

Drop it in the comments below so we can train OmniGuard to catch it! 🚀

## 评论（38/38）

> **Dhruv Jani** · 2026-10-30T11:38:52Z　
> One thing that stood out while building OmniGuard was how easily deceptive elements can blend into an otherwise normal-looking webpage.
>
> A countdown timer, a misleading button, or a tiny pre-selected checkbox might not look like much on its own, but these little design decisions can completely change what a user ends up doing.
>
> We built OmniGuard to make these tricks easier to spot, but I'm sure there are plenty of dark patterns we haven't thought of yet.
>
> What's one website or app experience that made you feel genuinely tricked? I'd love to hear some real examples! 👀

---

> **UnitBuilds** · 2026-10-30T11:43:13Z　
> Another tip for anyone dealing with ads, use AdGuard (the green shield), honestly the best blocker imo.

---

> **Dhruv Jani** · 2026-10-30T11:54:22Z　
> For me the best thing is "Brave" browser, never disappoints!😂

---

> **UnitBuilds** · 2026-10-30T11:55:46Z　
> On android, firefox, with ublock origin, works really well too.

---

> **Dhruv Jani** · 2026-10-30T11:58:58Z　
> I'll try them!
>
> Have A Great Day!

---

> **UnitBuilds** · 2026-10-30T11:59:34Z　
> Likewise!

---

> **Yug Vasava** · 2026-10-30T12:30:16Z　
> Bro, very early for this post. This project was made just yesterday!

---

> **Dhruv Jani** · 2026-10-30T12:31:03Z　
> Yeah, my bad I had this draft since weeks but I don't know I forgot to publish it!😅

---

> **Alex Shev** · 2026-10-30T12:34:37Z　
> A design critic is more helpful when it identifies the violated user task, not only the visual pattern. “This contrast makes the primary action hard to find on mobile” gives a team something to test and repair; “this looks bad” does not. The evaluation set should include real flows and accessibility constraints, not just screenshots.

---

> **FrancisTRᴅᴇᴠ** · 2026-10-30T14:12:54Z　
> The one thing I learned is that you can actually get Malware without having to click the ad. It got to the point where even the FBI themselves recommend users to use an ad-blocker because of this. Although it's not widespread and only targets high profile users, it's scary to think about that it's even possible to begin with and crazy how it's not patched.
>
> Here is a video that explains it.
>
> Otherwise, good stuff :)

---

> **Dhruv Jani** · 2026-10-30T14:17:41Z　
> Its True!
>
> Today my dad told me that if you get any msg from X guy, don't open it!
>
> Apparently his whatsapp profile got hacked and sent malicious .apk files to a lot of contacts.
>
> Its pretty common in my part of the world.
>
> I actually haven't tried any ad blockers, I just use brave for streaming or spotify, so as to avoid pop ups and ads.
>
> But I'll definitely try one!

---

> **Luke Bennett** · 2026-11-04T06:42:00Z　
> Thanks

---

> **Shikha Shukla** · 2026-10-30T17:57:21Z　
> Great topic of discussion

---

> **Emily Woods** · 2026-10-30T22:00:29Z　
> The fake timer example makes me want a separate uncertain result. From one screenshot I can see urgency language, but I can’t tell whether the deadline is genuine or whether the timer resets on another visit. Would you consider showing the visual evidence and confidence beside the warning, instead of treating both cases as equally established?

---

> **Dhruv Jani** · 2026-10-31T04:15:49Z　
> Actually to be completely honest, I'd consider it, but thing is this was a one day hackathon project and we've not tried anything different, better edge cases.
>
> But I'll definitely look into this if I go back to this project!
>
> Thanks! Have A Great Day!

---

> **mp3sss** · 2026-10-31T01:50:16Z　
> Dark patterns live in desktop installers too — the fake 'download now' buttons and pre-checked bundle offers show up in Electron apps and their update prompts, where there's no DOM to inspect, only pixels, so a visual approach like this is exactly the right shape. Pairing the detector with an on-device model would close the screenshot-privacy gap even further at the cost of some latency. And the Shadow DOM injection is a nice detail — it keeps host-page CSS from bleeding into your overlay.

---

> **Aliza Ali** · 2026-10-31T12:49:26Z　
> Fake countdowns are the one category you can catch without any model: reload the page in a fresh session, and if the timer snaps back to 05:00, it was never real. Pairing cheap deterministic checks like that with the multimodal pass would cut API calls and give users hard evidence instead of a judgment call. Confirmshaming is the one I'd most love to see flagged. "No thanks, I hate saving money" buttons need to go.

---

> **Oleksandr** · 2026-10-31T15:28:19Z　
> The worst one I've seen recently: a 'free' PDF converter that let you upload, process, and preview the file — and then demanded a subscription to download it. The preview was the trap. That's a variant of forced continuity that I'd love to see OmniGuard catch.

---

> **Eric McWay** · 2026-10-31T17:44:43Z　
> The flip side of this that I keep noticing: the pages I actually trust are the ones that show their work. I was looking at a Key West water page earlier today — 81.3°F, observed 1:12 PM EDT, the station named right next to the number, next high tide at 3:46 PM, and a plain Coastal Flood Advisory banner instead of a popup. No countdown, no guilt-trip dismiss button, nothing pre-checked. It made me realize how much of the gross stuff here is really about hiding provenance: if a page won't tell you when a number was measured or where it came from, that's already a small dark pattern, even before the fake timers show up. The example I had open: Key West water temperature & tides
>
> Disclosure: this comment was written with AI assistance.

---

> **Julian Neagu** · 2026-11-01T09:08:23Z　
> Dark patterns in checkout flows are the worst, especially when the extra cost only shows up at the final step. I'd be curious how well this catches things that only appear after a few clicks, not just in the current viewport.

---

> **Wahee Al-Jabir** · 2026-11-02T12:22:57Z　
> Would be nice if a AI was made to de-slopify AI generated code to make appealing UI.

---

> **jacob foster** · 2026-11-02T16:43:02Z　
> This is a great example of how AI can make the web more user-friendly. Dark patterns don't just hurt user trust; they also damage the overall user experience. I really like the idea of using visual AI to identify deceptive design elements in real time. Technology should help users make informed decisions, not manipulate them. Great work!

---

> **Shubham Chaudhary** · 2026-11-02T17:54:38Z　
> While reading through this, my first concern was about privacy and whether the extension captures the entire screen or potentially sensitive information. I was relieved to see that you've addressed this by limiting screenshots to the active viewport and using a stateless, zero-database architecture.
>
> That said, one thing I'd be curious about is how screenshot data is handled during transmission and by Gemini itself. Even if your backend doesn't store anything, the screenshots could potentially contain sensitive information visible in the viewport. Clarity around API-side data retention, logging, and processing would make the privacy story even stronger.
>
> Also, I find the distinction between traditional ad blockers and AI-powered visual detection particularly interesting. Tools like Brave already do a great job with trackers and malicious content, but detecting psychological manipulation at the UI level is a different challenge altogether.
>
> Really interesting project! Great work by the team. 👏

---

> **Sachin Guru** · 2026-11-03T16:35:00Z　
> I enjoyed reading your thoughts on how modern web design has changed over time. A clean and user-friendly design makes a big difference in how people interact with websites. Technology is evolving rapidly, and understanding digital tools is becoming increasingly important across industries. I have also been exploring a learn how business technology and software solutions help organizations improve their operations

---

> **Sachin Guru** · 2026-11-03T16:37:19Z　
> I enjoyed reading your thoughts on how modern web design has changed over time. A clean and user-friendly design makes a big difference in how people interact with websites. Technology is evolving rapidly, and understanding digital tools is becoming increasingly important across industries. I have also been exploring a fita.in/sap-course-in-coimbatore earn how business technology and software solutions help organizations improve their operations.

---

> **Sachin Guru** · 2026-11-03T16:39:29Z　
> I enjoyed reading your thoughts on how modern web design has changed over time. A clean and user-friendly design makes a big difference in how people interact with websites. Technology is evolving rapidly, and understanding digital tools is becoming increasingly important across industries. I have also been exploring a fita.in/sap-course-in-coimbatore to learn how business technology and software solutions help organizations improve their operations.

---

> **Pascal Thormeier** · 2026-11-03T12:29:07Z　
> Great piece of technology you people built there!
>
> What's the rate of false positives? For example, high-demand concert tickets: Let's say a very famous pop star comes to town and the local ticket vendor only allows tickets to be in the cart for ~10 minutes, so black market resellers don't hoard them to create artificial scarcity and inflate the price later on. Will such a countdown be flagged? Not saying that it's a good thing per se, it does create urgency, but it's actually a "necessary evil" to protect legitimate fans from illegitimate resellers and it actually does function as information to the user.
>
> Same goes for false negatives: A page that looks like it would have a working download button, because the page content implies a download and the button looks and feels legit enough to be the download button, although it's an ad - will this be flagged?
>
> Although you're not using a database, won't Google store these screenshots anyways when you send them to Gemini, or am I missing something? Or perhaps there's a way to redact certain parts of the screen beforehand?
>
> And now for the opinion part: The best way to get rid of these dark patterns is by having functioning consumer protection laws and actually fining the living heck out of companies that don't oblige. I know that such laws are next to impossible to install everywhere, let alone enforce, but I like to dream...

---

> **Dhruv Jani** · 2026-11-03T12:47:35Z　
> Actually Sir, it was built for a hackathon and we haven't added any features like this cause it was just 24 hours long.
>
> But yeah if we'll go back to this project again, we can definitely have a lot of good enhancements and features like you suggested.
>
> Current MVP just finds dark patterns on web page and flags it!
>
> Have A Great Day!

---

> **Pascal Thormeier** · 2026-11-03T12:57:09Z　
> No worries, even more impressive that you've managed to build it in 24 hours! Would love to see this flourish and get developed into a real product one day!
>
> Have a great day as well! :)

---

> **Mr Smithnen** · 2026-11-03T19:14:51Z　
> Yes, this is all too true 😆🙃

---

> **Levi** · 2026-11-04T04:42:46Z　
> Man, that looks awesome!

---

> **Mudassir Khan** · 2026-11-04T06:27:57Z　
> sending a viewport screenshot to a multimodal model instead of reading the DOM makes sense here, since dark patterns are mostly about visual weight and not markup. what i would worry about is latency on scroll: a round trip per viewport means the fake timer is gone or the page already shifted by the time the red box lands.
>
> we saw the same drift when overlaying boxes from stale coordinates on dynamic pages.
>
> are you mapping boxes back to DOM nodes after detection, and what does the false positive rate look like on legit urgency like real stock counts?

---

> **Jyanthi** · 2026-11-04T07:33:18Z　
> Brilliant initiative! The web should earn our trust, not manipulate us. Could tools like OmniGuard become the new standard for ethical design?

---

> **Dhruv Jani** · 2026-11-04T07:58:52Z　
> I don't think this will stop dark patterns on web pages but will definitely make people make aware!
>
> Have A Great Day!!

---

> **Jyanthi** · 2026-11-04T09:04:03Z　
> Absolutely! It may not eradicate dark patterns, but awareness is the first step towards resisting manipulation. The more informed users become, the harder it gets for deceptive design to succeed. Have a great day too!

---

> **Sunday Favour** · 2026-11-04T08:35:13Z　
> Amazing

---

> **Ingo Steinke, web developer** · 2026-11-04T10:49:42Z　
> Theoretically, this tool solves the problem at the wrong end, however it's the only end that end-users control. If such guards and blockers become widespread and popular, our industry's stakeholder must eventually adjust their priorities or audiences. Developers can then fix the root cause when they won't be pushed again and again to add misfeatures like obtrusive popovers to every other website and web app.

---

> **Tomasz** · 2026-11-05T20:13:08Z　
> Hi, how fast is one scan round-trip, and is auto-scan on scroll practical?

## 关联链接

- https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/confirmshaming.png
- https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/disguised-clicks.png
- https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/forced-continuity.png
- https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/hidden-costs.png
- https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/sneak-into-basket.png
- https://raw.githubusercontent.com/Tarkash-Labs/OmniGuard/main/assets/urgency-trap.png

## 导航

- 项目页：[[10-项目/github.com_1210d722]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
