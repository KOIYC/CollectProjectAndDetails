---
type: "corpus"
item_id: "01ac7fc8bb28a481"
title: "A Builder in CDMX: Flu Edition"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/earlgreyhot1701d/a-builder-in-cdmx-flu-edition-167"
project_url: "https://claude.ai/"
author: "Earl Grey"
published_at: "2026-11-08T01:45:07Z"
captured_at: "2026-11-11T13:40:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-11"
pub_day: "2026-11-08"
tags:
  - 语料
  - devto
  - ai
  - webdev
  - buildinpublic
  - showdev
metrics: {"reactions": 31, "comments": 20, "reading_time": 9}
comments_count: 20
comments_total: 20
discovered_via: "devto:buildinpublic"
---

# A Builder in CDMX: Flu Edition

> [!info] 一句话导读
> I built my sick wife a digital bell. She pressed the one button I left blank.*

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/earlgreyhot1701d/a-builder-in-cdmx-flu-edition-167>
> 指标：reactions=31 · 评论=20 · reading_time=9
> 作者：Earl Grey　|　发布：2026-11-08T01:45:07Z
> 项目链接：<https://claude.ai/>
> 采集：2026-11-11T13:40:39+08:00　|　id：`01ac7fc8bb28a481`

## 正文

*I built my sick wife a digital bell. She pressed the one button I left blank.*

> **TL;DR:** I caught the flu in Oaxaca and I still have it. By Mexico City, my wife had it too. From a tired Chromebook, I directed Claude to build her a sick-day bell: a page of big papel picado buttons where tapping "Té, por favor" opens a text to me, already written. No IDE, no terminal: Claude pushed it to GitHub straight from the chat, and it took under an hour from idea to her first tap. Her first tap went somewhere I didn't plan for.

My [last post in this series](https://dev.to/earlgreyhot1701d/a-builder-in-new-orleans-when-your-vibecoded-app-comes-on-vacation-f57) ended with "Oaxaca is next." It was. I just didn't plan on leaving it with a fever.

So here's the setup. We're on vacation in Mexico. I got sick in Oaxaca a few days ago. We made it to Mexico City, and then it was E's turn. I'm still sick. Now she is too. So she's in bed, and I'm the one pushing through, upright enough to fetch things.

I was proud of one thing on this trip. I didn't touch my Chromebook until day 8. I was going for an all-time record. Then E got sick, and she was napping, and, well. I couldn't help myself. Okay, I could have. I didn't want to.

What I had: an HP Chromebook 11a with a MediaTek Kompanio 500 processor and 4 GB of memory, 1.44 GB of it free. A keyboard I kept fighting. It's an 11-inch layout after years on my 17-inch laptop at home and my work keyboard, so my fingers kept landing where the keys used to be. My messages to Claude that night included "spik ebut" and "ato home." It read them anyway. A few hours. What I didn't have: my usual setup, or any energy for a real project.

Because E was sick in bed, I thought she might need a bell: the little one you ring to ask for tea or a blanket when you don't have the energy to call out. Neither of us packed one, so I built her a digital one, hosted on GitHub Pages ([here's the repo](https://github.com/earlgreyhot1701D/necesito)). Same job, fewer jingles.

I asked [Claude](https://claude.ai) (Opus 5.5) what we could build. It gave me three options. A play-test spike for my [Kiroween](https://kiroween.devpost.com) typing game, which the bad keyboard would turn into free user research. A small sick-day page for E. Or a pure vacation toy.

It recommended the spike. I picked the page for her, because it was lovely and the spike could wait.

The Chromebook turned out not to matter. Claude works in a cloud workspace, so the heavy lifting happened there. When I checked the laptop afterward, its CPU was sitting at 5%.

![Infographic titled A small Chromebook, a full build. Left side, What I had: an HP Chromebook 11a, budget and school-class; a MediaTek Kompanio 500 processor, entry-level, from 2019; 4 GB of memory with 1.44 GB free, tight; battery at 84% health after 38 cycles, good; CPU at 5% right after the build, barely awake. Two bars show CPU at 5% of 100% and memory at 2.56 of 4 GB, 64%. Right side, What I still shipped: under 1 hour from idea to her first tap, 1 live page on GitHub Pages, 7 buttons in 2 languages, 0 phone numbers in the code. Footnote: one ChromeOS Diagnostics reading on Nov 7 2026, right after the build, not a benchmark, the build ran in the cloud.](https://raw.githubusercontent.com/earlgreyhot1701D/necesito/main/assets/article/chromebook-check.png)

The memory was mostly spoken for. The processor was barely awake. My job was the same as always: direct, decide, say no to things. On that keyboard, saying no was about all I could type anyway.

Under an hour later, my phone buzzed. The first text from her new bell was blank.

## She rang the blank one

E had opened the page, skipped past the tea, the water, the blanket, and the soup, and tapped the one button with nothing written on it: **Otra cosa**, something else. Her Messages app opened, empty, pointed at me. She wasn't sure what to do with it. So she went back and tapped tea.

That one came through with a little steaming cup: 🍵 *Té, por favor (Tea, please).*

Same page, same person, two very different taps. I'll come back to the blank one. First, how it got built.

## Five questions, zero typing

I asked Claude to interview me about what E should see. It asked one question at a time, each with options I could tap instead of type.

| Question | What I picked |
|---|---|
| Which buttons? | Tea, water or juice, extra blanket, come sit with me, a blank "something else" |
| Any more? | Soup or something to eat, lights down and quiet |
| Look and feel? | Bakery warm, then papel picado (more on that below) |
| Pictures? | Big emoji, small words |
| What's at the top? | A Spanish touch: *¿Qué necesitas, mi amor?* |

That interview is the whole spec. Seven buttons and a greeting. I didn't write a PRD for this one, and I'm at peace with that.

## A button is just a link

Each button is a plain link in the format iPhones accept for texts: `sms:NUMBER&body=TEXT`. Tap it and Messages opens with the number and the message filled in.

![E's request page on a phone screen. A row of pink, teal, orange, green, purple, and yellow papel picado flags runs across the top. Below it, the heading reads ¿Qué necesitas, mi amor?, then Toca un botón y yo te lo traigo, with the English line What do you need, my love? Tap a button and I'll bring it. Six large buttons in two columns, each with a big emoji, a Spanish label, and a smaller English label: Té, por favor / Tea, please; Agua o jugo / Water or juice; Otra cobija / Extra blanket; Sopita o algo de comer / Soup or a snack; Luz baja y silencio / Lights down, quiet; Ven a sentarte conmigo / Come sit with me.](https://raw.githubusercontent.com/earlgreyhot1701D/necesito/main/assets/article/necesito-page.png)

*[See the screenshot full size](https://raw.githubusercontent.com/earlgreyhot1701D/necesito/main/assets/article/necesito-page.png), or browse the code in the [necesito repo](https://github.com/earlgreyhot1701D/necesito).*

She still has to press send. A web page can't send a text on its own, and I'm glad it can't. That one tap is a small price for a page that can't text anyone without her knowing.

The text that lands on my phone is the notification. No app for me, no server, nothing to keep running while we're both sick.

## Spanish first, with training wheels

We don't speak Spanish. But we're in Mexico City, and *¿Qué necesitas, mi amor?* is a much better thing to see from bed than "Request Form."

So the page went Spanish first, with a small English line under every label so she always knows what she's tapping. The texts come through in both: *🛌 Otra cobija, por favor (Extra blanket).*

The first theme was bakery warm, a nod to her bakery. Then I asked to explore Mexican palettes, and we landed on papel picado: rosa mexicano, turquoise, orange, lime, purple, and marigold, with a string of cut-paper flags across the top.

The flags are pure CSS. On the first pass, the cutouts were arranged so each flag looked like a little smiling ghost. Claude rearranged the holes into a flower pattern. Now they look like papel picado instead of a haunted bunting.

## Toe pick.

Claude filled in my number so the buttons had somewhere to send. Then we made a public GitHub repo, because free GitHub Pages wants one. Then it hit me, and I typed "TOE PICK!"

(If you know, you know. *The Cutting Edge*, 1992. The hockey player. The figure skater. The fall.)

My phone number was sitting in two files and the commit history of a public repo. It got there by me saying yes to each step without seeing where they added up.

The fix Claude proposed: take the number out of the code entirely and put it in the link instead, after the `#`.

```plaintext
https://earlgreyhot1701d.github.io/necesito/#5551234567
```

The part after the `#` is called the fragment, and browsers keep it to themselves. They don't send it to the server ([RFC 3986, section 3.5](https://www.rfc-editor.org/rfc/rfc3986#section-3.5)), so GitHub never sees it. A few lines of script on the page read it, accept it only if it's 10 to 15 digits and nothing else, and build the buttons from it. A link with no number, or junk instead of digits, turns the buttons off and shows a note asking her to get the link again.

Then Claude wiped the history down to one clean commit and force-pushed it. One honest caveat: GitHub can keep an old commit reachable for a while to anyone with its exact address. Nobody had it, the repo was minutes old, and I can live with that.

The trade-off: the number lives in the link, so anyone she forwards the link to can see it. She's not forwarding it. She's resting.

## No IDE. Just a chat.

This is the part I keep thinking about.

My usual build has handoffs. Claude writes the spec, [Kiro](https://kiro.dev) builds it in an IDE, I review and decide. Tonight there was no handoff. I never opened an editor or a terminal. Nothing got installed on the Chromebook.

Once I created the empty repo and approved access, Claude cloned it, wrote the files, took screenshots to check its own work, committed, and pushed to GitHub. All of it happened in the same chat where it was asking me about tea. Every commit in the repo came from that conversation. !!!!!!!!!!!!!!!!!!!!!!!!!!!

There were two things it couldn't do, and I like knowing where the edges are. It couldn't create the repo for me, and it couldn't turn on [GitHub Pages](https://docs.github.com/en/pages), because that part of the GitHub API is blocked from its side. So I clicked those, about a minute of work, and Claude did everything else.

That split felt right. I owned the account decisions. The agent did the typing I couldn't.

The extras came after:

| File | Job |
|---|---|
| `og.png` | Social card, so iMessage shows the papel picado preview instead of a bare link |
| `apple-touch-icon.png` | A tea-cup flag icon for the browser tab |
| `robots.txt` | Keeps search engines out. It opens with "Shh. Someone's resting." |
| `humans.txt` | Credits. E's role: "resting. Tapping buttons. Getting better." |

## Why the blank one stays

Back to that empty text.

The blank button was a choice, not a gap. Sometimes what you need isn't on the list, and the person in bed should still get a way to ask. But a blank text with no prompt left her unsure what she was supposed to do next. The pre-written buttons worked on the first try, with the cute emoji and everything.

So v2 gets one change: **Otra cosa** opens with *Necesito... (I need...)* already typed, so the cursor lands in a sentence instead of a void. That's it. Not refactoring anything else from a sick bed.

## What it can't do

- Send the text for her. She presses send, every time.
- Work on Android as written. The link format is iPhone-first; Android usually wants `?body=` instead of `&body=`. Untested there.
- Hide the number from anyone who has the link.
- Tell her I read it. It's a request button, not a pager.
- Work without a signal. If Messages can't send, the page can't either.

## Try it

{% github earlgreyhot1701D/necesito %}

Fork it, edit the button list in `build.js`, run `node build.js`, turn on Pages, and text your person the link with your number after the `#`. A 10-digit US number gets `+1` added; anywhere else, use the full number with country code, digits only.

How long it took, by the clock on my messages (Mexico City time):

| Time | What happened |
|---|---|
| 6:04 PM | "What can we build?" |
| 6:13 PM | Interview starts |
| 6:17 PM | First version |
| 6:22 PM | All Spanish, English helper added |
| 6:27 PM | Papel picado |
| 6:30 PM | Repo created |
| 6:33 PM | TOE PICK |
| 6:38 PM | Number out of the code, history wiped |
| ~6:50 PM | The patient has used it |

This is the third stop in the *A Builder in...* series. In [Paris](https://dev.to/earlgreyhot1701d/a-builder-in-paris-do-devs-dream-of-electrique-chats-3hd9), I learned that stepping away from my desk doesn't mean I stop building. In [New Orleans](https://dev.to/earlgreyhot1701d/a-builder-in-new-orleans-when-your-vibecoded-app-comes-on-vacation-f57), an app I'd already built came on the trip with us. Mexico City is the first time the app got built on the trip, for one person, for one sick week.

The goal on every trip is the same: close the laptop, let the internet go on without me, and leave the FOMO at home. It’s never easy. This time I made it to day 8. Next time, day 9.

---

Quick context if you are new here. I work in the California courts, running court operations for the county. I started building with AI in July 2025 and I have been learning in public ever since. I do not write the code. I direct, the agents generate, I validate and decide. I build the [Clew Suite](https://clewlabs.org), a set of civic tech tools for making complex systems easier to inspect. That is the lens I am writing from.

Built and written with AI assistance in November 2026. Claude (Opus 5.5) wrote the code, pushed the repo, and assisted in draftingdthis post from our build session. I directed, decided, and edited.

AI Assisted. Human Approved. Powered by NLP.

## 评论（20/20）

> **OneLifeVibe** · 2026-11-08T02:07:48Z　
> The blank-button detail is the part that sticks: she skipped every labelled request and tapped "Otra cosa" first, which says a lot about how an open field beats a menu when someone is unwell. The v2 fix is neat too — prefilling "Necesito..." so the cursor lands in a sentence instead of a void, rather than adding more buttons. And the fragment trick for the phone number is a good trade-off to name honestly: keeping the number out of the repo and the commit history, while accepting that anyone holding the link can see it. Hope you both feel better soon.

---

> **Earl Grey** · 2026-11-08T05:17:08Z　
> Thank you so much! That blank button surprised me too, and it taught me more than the other six combined. Starting the sentence for her felt like the smallest fix that would make the biggest difference. And thanks for calling out the phone number trade-off, it was the part I most wanted to be honest about. We’re both on the mend, slowly. 🍵

---

> **Sina Rezaei** · 2026-11-08T06:10:31Z　
> One small edge case worth considering: SMS encoding. Those emoji buttons are cute, but a single emoji can switch the entire message from GSM-7 to UCS-2, dropping the single-segment limit from 160 to 70 characters. It doesn't matter much for these short requests, but it's something to watch if you ever add dynamic messages or longer custom requests. Unicode has a hidden cost here.

---

> **Earl Grey** · 2026-11-08T16:39:04Z　
> Ooh, I love this one, thank you! I had no idea one emoji could cut the limit from 160 to 70. I checked, and the longest pre-written text is 54 characters, so they all squeak in under one message. But you’re right about where it bites: “Otra cosa” is open-ended, and v2 starts it with “Necesito...” so she can keep typing. That’s exactly where a long request could split. Adding it to the v2 notes. Unicode has a hidden cost is going on a sticky note.

---

> **Renhua Wei** · 2026-11-09T02:56:18Z　
> The quieter cost behind the emoji: GSM 03.38 has no á, í, ó or ú (è é ù ì ò and the tilde set — ñ, ¿, ¡ — are all in the table), so "Necesito más ayuda" is UCS-2 at 70 while "Necesito mas ayuda" still fits 160; the accent, not the emoji, flips a Spanish body. Same budget, second charge: { } [ ] ~ ^ \ | € are escape pairs at 2 septets each, so a pasted snippet caps at 80 characters with no emoji in sight. The check is one assertion — keep the 128-char table plus those 9 escapes in a test and assert set(body) <= GSM7 | EXT for every prewritten string; "Otra cosa" is 9 septets and safe, "días" is not.

---

> **Earl Grey** · 2026-11-09T04:09:30Z　
> This is exactly why I love posting builds. I’ll be honest: this was above my head at first. For me, the app either worked or it didn’t, and I trusted what I was told. I had no idea that one accent, “más” instead of “mas,” could quietly cut a text from 160 characters to 70. Your comment sent me digging into what the app is doing under the hood, and that’s the part I’ll carry into the next build. Your test idea is in the v2 notes now. Gracias. 🍵

---

> **Renhua Wei** · 2026-11-09T04:32:40Z　
> Glad it's in the notes, and one sharpening: the 54-character bodies were never the risk. UCS-2 only costs you at the boundary, so a 54-char body fits one part either way. The accent bites when a body crosses 70, and then again on concatenation, where the UDH eats a header: GSM-7 drops 160 to 153 septets per part, UCS-2 drops 70 to 67 UTF-16 units. That is the number that surprises people at 300 characters.
>
> So the assertion is not "is it GSM-7", it is "does every canned body fit one part", run against the real table instead of a guess at it:
>
> GSM7 = "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà"
> ESC = "\f^{}\\[~]|€"
>
> def parts(s):
>  if any(c not in GSM7 and c not in ESC for c in s):
>  n, one, multi = len(s.encode("utf-16-be")) // 2, 70, 67
>  else:
>  n, one, multi = len(s) + sum(s.count(c) for c in ESC), 160, 153
>  return 1 if n <= one else -(-n // multi)
>
> assert all(parts(b) == 1 for b in canned)
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> With that in the send path you don't have to cap the v2 free-text field to keep it single-part. Count the parts before sending and label it, "Necesito... (1 of 2)" is a friendlier failure than a silent split.

---

> **Earl Grey** · 2026-11-09T04:52:56Z　
> Thank you for coming back to sharpen this! I had to break this one down piece by piece, and here’s what I took away: my short texts were never the problem. The real question is whether a message stays in one piece, because long texts get split, and each piece loses a few characters to a hidden label. I love the “(1 of 2)” idea too. A label beats a silent split. It’s all in the v2 notes now: github.com/earlgreyhot1701D/necesi.... Gracias for teaching in the comments. 🍵

---

> **Renhua Wei** · 2026-11-09T05:06:05Z　
> Right, the split is the whole story, and the wire hands you an exact number instead of a guess. One concatenation header eats 6 octets out of the 140-octet TPDU, so every part except the last carries floor((160*7 - 48)/7) = 153 septets, and the tail gets the full 160. That is why 306 characters still ships as two parts and 307 does not.
>
> One more line for the v2 notes: the escape set. { } [ ] ~ ^ \ | and the euro sign cost two septets each, so a single literal ~ sitting inside a 154-septet body pushes it to 155 and silently bills a third part. Check it by counting parts, not characters — run the longest real template through the encoder at length minus one, at length, and at length plus one, and see whether the part count steps at the same place the character count does. When they disagree by exactly one part, it is an escape, not a length problem.

---

> **Sina Rezaei** · 2026-11-09T05:25:39Z　
> That's a really good takeaway. I especially like the "1 of 2" idea because a silent split is much worse than knowing exactly what you're sending.
>
> One thing I'd add for v2: make sure the segment counter uses the actual encoding rules rather than just JavaScript's string length. UTF-16 code units, GSM-7 extension characters, and concatenated SMS headers can all affect the final count. Getting that right before sending saves a lot of confusion later.
>
> Looking forward to seeing how you implement it!

---

> **Renhua Wei** · 2026-11-09T05:38:26Z　
> Agreed, and the trap is that there are two rulers and the branch decides which one you are holding. The moment one character falls outside GSM 03.38 the whole body is UCS-2, so the ruler becomes UTF-16 code units: str.length, not Array.from(s).length. An emoji is 2 units there, so code-point counting undercounts it exactly when it matters. Inside GSM-7 it is septets, and the extension table (^ { } \ [ ] ~ | €) costs 2 each, so character length lies in the other direction.
>
> Two test vectors I would pin in CI, both exact: 80 x '€' is 160 septets and ships as 1 part, 81 is 162 and ships as 2; 17 x '😀' is 34 UTF-16 units and ships as 1 part, 36 is 72 units and ships as 2. If the counter disagrees with either one, the ruler is wrong, not the message.
>
> Worth returning the assumed encoding alongside the count, too. A 2-part UCS-2 message and a 1-part GSM-7 one look identical once you only keep the number, and that is the case you will be debugging at 2am.

---

> **Earl Grey** · 2026-11-09T14:49:38Z　
> Y’all turned my sick-day bell into an SMS masterclass and I’m here for it. I collected all of it in the v2 notes: count the real pieces, test the tricky characters right at the edge, and show which rules the counter used. github.com/earlgreyhot1701D/necesi.... Gracias, everyone. 🍵

---

> **Renhua Wei** · 2026-11-09T15:16:21Z　
> Those three v2 rules are the whole game: count the real pieces, test at the edge, keep the ruleset next to the counter. If the counter throws something odd right at a boundary, ping me on GitHub — same handle, @dafili.

---

> **Earl Grey** · 2026-11-10T20:45:59Z　
> Thank you!

---

> **Kürşat Yılmaz** · 2026-11-09T00:32:26Z　
> The obsession with wrapping remote APIs into multi-layered agent abstractions is creating massive hidden latency and failure cascades in production.
>
> If you profile real-world workloads, bare-metal local inference (via direct C++ / llama.cpp or vLLM bindings) consistently beats fragile cloud wrappers on both predictability and cost. Tooling should eliminate abstraction penalties, not compound them.

---

> **Earl Grey** · 2026-11-09T04:02:13Z　
> Fair point for AI-heavy apps! This one’s the opposite end: no AI at runtime at all, just one HTML page and a text link. The only “inference” is E deciding between tea and soup. 🍵

---

> **Alex Shev** · 2026-11-09T17:46:27Z　
> Building on constrained hardware exposes which parts of a workflow are actually essential. Publishing the bootstrapping path—editor, auth, build, deploy, and recovery from a lost connection—would make this a useful reproducibility guide for other builders working with limited machines.

---

> **Earl Grey** · 2026-11-10T20:29:33Z　
> This comment made my day. You’re right, the small machine showed me what’s essential: no editor, no installs, just a browser, a GitHub account, and a chat that could build and push. My everyday laptop is a lot more powerful, and for a lot of builders, a setup like my travel one is the whole kit. So I’m taking you up on it: a step-by-step guide to the bootstrapping path, including the costs and what a 4 GB machine can’t do. Thank you for the idea. 🙌 🚀

---

> **Alex Shev** · 2026-11-10T20:48:42Z　
> That guide will be genuinely useful. I’d make the 4 GB constraints concrete with a capability table: baseline browser tabs, build memory, swap behavior, and recovery time after a failed deploy. The value is not proving that everyone should work this way—it is showing the smallest setup that still preserves a reliable feedback loop.

---

> **Earl Grey** · 2026-11-11T02:45:58Z　
> Thank you, Alex. Your comment turned into a whole post. Here it is: dev.to/earlgreyhot1701d/a-small-la...
>
> I built the capability table you suggested: baseline tabs, memory during a build, where it starts to slow, and recovery time after a failed deploy. I broke a deploy on purpose, and the fix took 44 seconds. The one I didn’t measure directly was swap. The Chromebook never got close enough to its limit for me to see it kick in, so I left it out rather than guess.

## 关联链接

- https://claude.ai
- https://clewlabs.org
- https://dev.to/earlgreyhot1701d/a-builder-in-new-orleans-when-your-vibecoded-app-comes-on-vacation-f57
- https://dev.to/earlgreyhot1701d/a-builder-in-paris-do-devs-dream-of-electrique-chats-3hd9
- https://docs.github.com/en/pages
- https://earlgreyhot1701d.github.io/necesito/#5551234567
- https://github.com/earlgreyhot1701D/necesito
- https://kiro.dev
- https://kiroween.devpost.com
- https://raw.githubusercontent.com/earlgreyhot1701D/necesito/main/assets/article/chromebook-check.png
- https://raw.githubusercontent.com/earlgreyhot1701D/necesito/main/assets/article/necesito-page.png
- https://www.rfc-editor.org/rfc/rfc3986#section-3.5

## 导航

- 项目页：[[10-项目/claude.ai_8701e897]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
