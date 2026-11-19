---
type: "corpus"
item_id: "ba796d11cdc4c453"
title: "A Small Laptop Is a Full Build Kit: Bootstrapping with a Chromebook, Claude, and GitHub"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/earlgreyhot1701d/a-small-laptop-is-a-full-build-kit-bootstrapping-with-a-chromebook-claude-and-github-4j16"
project_url: "https://claude.ai/"
author: "Earl Grey"
published_at: "2026-11-11T02:41:57Z"
captured_at: "2026-11-19T09:56:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-11"
tags:
  - 语料
  - devto
  - ai
  - beginners
  - buildinpublic
  - claude
metrics: {"reactions": 26, "comments": 9, "reading_time": 18}
comments_count: 9
comments_total: 9
discovered_via: "devto:buildinpublic"
---

# A Small Laptop Is a Full Build Kit: Bootstrapping with a Chromebook, Claude, and GitHub

> [!info] 一句话导读
> A small laptop is a full build kit. Here's how far mine went.*

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/earlgreyhot1701d/a-small-laptop-is-a-full-build-kit-bootstrapping-with-a-chromebook-claude-and-github-4j16>
> 指标：reactions=26 · 评论=9 · reading_time=18
> 作者：Earl Grey　|　发布：2026-11-11T02:41:57Z
> 项目链接：<https://claude.ai/>
> 采集：2026-11-19T09:56:22+08:00　|　id：`ba796d11cdc4c453`

## 正文

*A small laptop is a full build kit. Here's how far mine went.*

> **TL;DR:** A reader suggested I publish the full bootstrapping path behind an app I built on a 4 GB Chromebook: editor, auth, build, deploy, and recovery. So I did, and then I pushed the same little laptop through three more builds and a few stress tests to see where it would break. The Chromebook never broke a sweat. Through five rounds, a broken deploy, and a 44-second fix, its CPU stayed between 5% and 15%.

The comment landed while I was still answering replies on my last post.

[Alex Shev](https://dev.to/alexshev), creator of [Terminal Skills](https://terminalskills.io/), a free, open-source library of skills that extend AI coding agents like Claude Code, wrote that building on constrained hardware shows which parts of a workflow are essential, and that publishing the bootstrapping path would make a useful guide for other builders working with limited machines.

That comment changed how I saw the whole thing. I built that app because my wife was sick and this little laptop was what I had with me. I usually build on a bigger one. I never thought of what I did as a guide. Alex's idea helped me see it could be one: if a small laptop is what someone has to build with, the exact steps I took might be what they need. So this post is that guide, step by step. I wrote it on the same laptop: an HP Chromebook 11a with 4 GB of memory.

## The kit

| Part | What I used | Cost |
|---|---|---|
| Laptop | HP Chromebook 11a: MediaTek Kompanio 500 processor, 4 GB of memory | Already owned |
| Browser | Chrome, which comes with ChromeOS | Free |
| Code host and website | [GitHub](https://github.com) and [GitHub Pages](https://docs.github.com/en/pages) | Free |
| AI that builds | [Claude](https://claude.ai), working in a cloud workspace from the chat | Paid plan. More in "What it costs." |

That's the whole list. Nothing installed on the laptop.

Here's everything this post covers, in 46 seconds. Claude recorded it, and Round 4 explains how.

![A 46-second silent tour, shown as a GIF. It opens on the 4 GB and a Dream landing page, then shows Necesito's bilingual buttons being tapped, the 3D papel picado flags being spun and zoomed, and the bootstrapping path diagram stepping forward with the Wi-Fi dropped and brought back, before returning to the landing page.](https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/4gb-tour.gif)

## Round 1: You can ship a live app with no editor

Round 1 already happened. A few days ago, on vacation in Mexico City, my wife got sick and I built her a digital bell from the Chromebook: a page of big buttons where tapping "Té, por favor" opens a text to me, already written. The full story is in [A Builder in CDMX: Flu Edition](https://dev.to/earlgreyhot1701d/a-builder-in-cdmx-flu-edition-167). Here's the bootstrapping path Alex suggested I write up.

![Necesito in action, shown as a GIF. A bilingual page titled ¿Qué necesitas, mi amor? with a papel picado banner across the top and big pastel buttons: Té, por favor; Agua o jugo; Otra cobija; Sopita o algo de comer; Luz baja y silencio; Ven a sentarte conmigo; and Otra cosa. Two buttons get tapped, then the page scrolls to the English explainer at the bottom. Recorded with a demo number.](https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-1-necesito.gif)

### Editor: there wasn't one

I never opened an editor or a terminal. I described what I wanted in the Claude chat, answered a few multiple-choice questions about buttons and colors, and Claude wrote the code in its cloud workspace. The chat was the editor.

### Auth: one account, one approval

I created an empty repository on GitHub, the same way anyone does at github.com/new. Then I approved Claude's access to that one repository. That was the only sign-in step.

### Build: on someone else's computer

Claude cloned the repository, wrote the files, took screenshots to check its own work, committed, and pushed. All of it ran in Claude's cloud workspace, not on my laptop. When I checked the Chromebook right after, here's what it showed:

| Reading | Number |
|---|---|
| CPU in use | 5% |
| Memory free | 1.44 GB of 4 GB |

![Infographic titled A small Chromebook, a full build. Left side, What I had: an HP Chromebook 11a, budget and school-class; a MediaTek Kompanio 500 processor, entry-level, from 2019; 4 GB of memory with 1.44 GB free, tight; battery at 84% health after 38 cycles, good; CPU at 5% right after the build, barely awake. Right side, What I still shipped: under 1 hour from idea to her first tap, 1 live page on GitHub Pages, 7 buttons in 2 languages, 0 phone numbers in the code. Footnote: one ChromeOS Diagnostics reading, right after the build, not a benchmark.](https://raw.githubusercontent.com/earlgreyhot1701D/necesito/main/assets/article/chromebook-check.png)

### Deploy: three clicks

Claude couldn't turn on GitHub Pages from its side, so I did: Settings, Pages, deploy from the main branch, Save. A minute later the app had a public address. The [repo is here](https://github.com/earlgreyhot1701D/necesito) if you want to see every file.

### Recovery: when something goes wrong

Two kinds of trouble came up. My Wi-Fi dropped once during this build, and nothing seemed lost (Round 5 has the honest version of that story). And later I broke a deploy on purpose to time the fix (it's in the capability table). Short version: the work lives in the cloud and on GitHub, not on the laptop, so a hiccup on the laptop doesn't undo it.

### Try it yourself

1. Create a free GitHub account.
2. Make an empty repository at github.com/new. Check "Add a README file."
3. In a Claude chat, describe the small thing you want to build. Ask Claude to interview you one question at a time.
4. When Claude asks for access to your repository, approve that one repository.
5. When the files are pushed, turn on Pages: Settings, Pages, main branch, Save.
6. Open your link.
This uses Claude Code, which comes with Claude's Pro and Max plans, not the free plan. More in "What it costs." I did all of this in the Claude app, so the approval screen may look a little different wherever you use it.

## Round 2: You can make interactive 3D, and your laptop can draw it

Round 2 was a callback to Round 1: strings of papel picado flags in 3D, swaying in the wind across a dusk sky. You can drag to spin it, pinch or scroll to zoom, and when you let go it slowly turns on its own.

![Papel picado in 3D, shown as a GIF. Strings of bright pink, turquoise, orange, lime, purple, and yellow cut-paper flags sway against a purple dusk sky with warm string lights and a few stars, while the scene slowly turns.](https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-2-3d.gif)

Try it: [Papel picado, in 3D](https://earlgreyhot1701d.github.io/4gb-and-a-dream/round-2-3d/). The [code is here](https://github.com/earlgreyhot1701D/4gb-and-a-dream).

This round tested the laptop differently. Building it happened in the cloud, like Round 1. But drawing 3D happens on the device you're looking at, many times a second. So for the first time, the Chromebook had real work to do.

### One library, no 3D tools

The whole scene is one HTML file and one library, [three.js](https://threejs.org), which draws 3D in the browser. The flags are flat squares with a cut-paper pattern painted on, and their ripple is plain math run every frame. No 3D modeling software, nothing installed.

### Hardening the design

The first version worked. Then I asked Claude, as a design partner, what it would change. It suggested four things, and I said yes to all four:

| Change | Why |
|---|---|
| A live frame-rate meter in the corner | It shows, in real time, how smoothly this laptop is drawing the scene. The page becomes its own evidence. |
| Keyboard controls: arrow keys spin, + and − zoom | The first version only worked with a mouse or a finger |
| Warm string lights and a few stars | The flags looked flat. Small glowing bulbs added depth and that plaza-at-night feeling. |
| Pause when the tab is hidden, and cap sharpness on high-res screens | Keeps it light on a 4 GB machine |

Testing it caught one more: the instructions at the bottom disappeared the first time I clicked, so a reader who looked away lost them. Now they stay on screen.

It also told me what to skip: shadows and a 3D ground. They look great, and they're the most expensive things to draw. On a small laptop, I think the best design choices are the ones that leave things out.

### What the Chromebook showed

I opened the scene from [the live page](https://earlgreyhot1701d.github.io/4gb-and-a-dream/) and put it side by side with ChromeOS Diagnostics, so both stayed on screen. That mattered: the scene pauses when its tab is hidden, so my first reading, with Diagnostics covering it, caught the scene resting instead of working.

| Reading | Round 1 (after the build) | Round 2 (flags moving) |
|---|---|---|
| Frame rate | not measured | 60 frames per second |
| CPU in use | 5% | 15% |
| Memory free | 1.44 GB of 4 GB | 1.68 GB of 4 GB |
| Temperature | 37°C | 41°C |

Sixty frames per second is as smooth as most laptop screens can show. Drawing 3D tripled the CPU, from 5% to 15%, and the laptop still had most of its power to spare. One reading each, not a benchmark.

## Round 3: You can make animated diagrams to explain your work

Round 3 is the bootstrapping path itself, drawn as a diagram you can play. Six steps run from the laptop to a live link, and each is colored by where it happens: on the laptop, in Claude's cloud workspace, or on GitHub.

![The bootstrapping path diagram, shown as a GIF. On a navy grid, a glowing turquoise thread moves down six numbered steps on parchment cards: Describe it, Decide it, Build it, Push it, Ship it, See it. The page scrolls to each step as it lights up, then the What if the Wi-Fi drops? button cuts the line and brings it back.](https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-3-diagram.gif)

Try it: [The bootstrapping path](https://earlgreyhot1701d.github.io/4gb-and-a-dream/round-3-diagram/).

The diagram makes the article's main point visible. Of the six steps, only two happen on the laptop: describing what you want, and opening the link at the end. Everything in between happens somewhere else.

| Step | Where it runs | Who does it |
|---|---|---|
| Describe it | On the laptop | Me |
| Decide it | In the cloud | Claude asks, I pick |
| Build it | In the cloud | Claude |
| Push it | On GitHub | Claude, after I approve one repo |
| Ship it | On GitHub | Me, three clicks |
| See it | On the laptop | Me |

It has one button I'm especially fond of: **What if the Wi-Fi drops?** Press it, and the link between the laptop and the cloud breaks into an orange dashed line while the thread keeps going. My Wi-Fi dropped once while I was building Round 1, and Round 5 says what I know about it.

### The back and forth

The first version was not the one you see. I tested each version on the Chromebook, told Claude what felt off in plain words, and Claude changed it and pushed again. Here's the whole loop, in order:

| Version | What I noticed on the Chromebook | What changed |
|---|---|---|
| 1 | It animated, but nothing showed the path or which step came next. | A glowing thread now unspools to the current step, with a spark at its tip. Steps behind it fill in, and steps ahead stay dim. |
| 1 | It used the same papel picado colors as Necesito. | It switched to my [Clew Labs](https://clewlabs.org) colors. The thread fits the brand: a clew is the ball of thread Ariadne used to find her way out of the labyrinth. |
| 2 | On the small screen, the current step fell below the fold. | The page now scrolls to each step, and the buttons and caption stay pinned at the top. |
| 3 | Autoplay kept going while I was trying to read. | Any click, tap, or scroll stops it. **Replay** starts the walkthrough over when you're ready. |
| 3 | A button called "Drop the Wi-Fi" didn't explain itself. | It's now a question: **What if the Wi-Fi drops?** |
| 5 | It scrolled to the next step before I finished reading. | Each step now holds for 6 seconds, and the scroll glides instead of jumping. |

Six versions in about twenty minutes, all from the same chat. To me, that's the feedback loop Alex was asking about. Each fix took one sentence from me and one push from Claude, and the laptop never did more than show me the result.

No libraries this time: plain HTML, CSS, and a little JavaScript. It also starts paused if your device asks for reduced motion, and a screen reader reads each caption as the steps change.

### What the Chromebook showed

Same method as Round 2: the diagram playing on the right, Diagnostics on the left.

| Reading | Baseline (4 tabs, nothing animating) | Round 2 (3D) | Round 3 (diagram playing) |
|---|---|---|---|
| CPU in use | 5% | 15% | 6% |
| Memory free | 1.64 GB of 4 GB | 1.68 GB of 4 GB | 1.68 GB of 4 GB |
| Temperature | 37°C | 41°C | 38°C |

The diagram barely registered: 6%, one point above resting. The processor was running at 0.91 GHz, about half its top speed, which usually means it has little to do. In my test, a plain page with a little motion cost the laptop almost nothing. One reading each, not a benchmark.

![Chromebook screen split in two. On the left, ChromeOS Diagnostics shows the MediaTek Kompanio 500 at 6% CPU usage, 38 degrees C, running at 0.910 GHz, with 1.68 GB of 4.00 GB of memory available. On the right, the bootstrapping path diagram is playing in Chrome, with step 04, Push it, highlighted under a caption that reads: On GitHub, you approve one repo, and Claude pushes every commit from the chat.](https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-3-side-by-side.png)

## Round 4: You can make a demo video without video software

**[Watch the tour](https://earlgreyhot1701d.github.io/4gb-and-a-dream/round-4-video/)** · [Recording script](https://github.com/earlgreyhot1701D/4gb-and-a-dream/blob/main/scripts/record_tour.py)

I asked for a tour of the whole kit, Necesito included. No screen recorder, no editor, nothing installed on the Chromebook.

Claude wrote a script that opens a browser in its cloud workspace, clicks through every round, and records what it sees. Then ffmpeg, a command-line video tool, turned the recording into an MP4. The laptop's only job was to play the result.

The tour GIF at the top of this post is this round.

What the video does and doesn't show:

| Choice | Why |
|---|---|
| Recorded from the repo files | Claude's workspace can't reach github.io. They're the same files GitHub Pages serves. |
| Necesito uses a demo number | My real number doesn't go in a video. |
| The tap stops at the button | A browser can't film Messages opening on an iPhone. |
| The 3D frame-rate meter is hidden | It would show the recording machine's speed, not the Chromebook's. |

### What the Chromebook showed

Same method: the video playing on the right, Diagnostics on the left.

| Reading | Baseline | Round 2 (3D) | Round 3 (diagram) | Round 4 (video playing) |
|---|---|---|---|---|
| CPU in use | 5% | 15% | 6% | 7% |
| Memory free | 1.64 GB of 4 GB | 1.68 GB of 4 GB | 1.68 GB of 4 GB | 1.40 GB of 4 GB |
| Temperature | 37°C | 41°C | 38°C | 35°C |

Playing the video cost about the same as the diagram. The interesting part to me: the video shows the 3D flags, but here the laptop is only playing back pictures, not drawing them. That's half the CPU of Round 2. Memory was lower because I had more tabs open this time. One reading each, not a benchmark.

![Chromebook screen split in two. On the left, ChromeOS Diagnostics shows the MediaTek Kompanio 500 at 7% CPU usage, 35 degrees C, running at 1.417 GHz, with 1.40 GB of 4.00 GB of memory available. On the right, the Round 4 tour page is playing in Chrome at 0:14 of 0:46, showing the papel picado flags in 3D.](https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-4-side-by-side.png)

## Round 5: A dropped connection, and what I can't tell you

My Wi-Fi dropped at some point during the Necesito build. I know it happened. I don't remember when. We were either brainstorming or Claude was reworking something I'd asked for.

I didn't write it down, because nothing seemed wrong. When the connection came back, the chat picked up where it left off, and I kept going.

While writing this post, I asked Claude to look back through the chat for the drop. It couldn't find one. No repeated messages, no cut-off replies, no "are you still there?" The chat doesn't record times, so a pause leaves no gap to spot.

Here's my honest read. The build runs in Claude's cloud workspace, not on the laptop, so the laptop losing Wi-Fi doesn't stop the work. It just stops me from seeing it for a minute. That's my understanding of how it works, not something I tested.

If you want proof instead of a memory, it's an easy test to run yourself: start a build, turn off your Wi-Fi for a minute, turn it back on, and see what's waiting.

## The capability table

Alex came back with a sharper ask: make the 4 GB limits concrete. In his words, the point isn't proving everyone should work this way. It's showing the smallest setup that still preserves a reliable feedback loop. So I measured it.

| Capability | What I did | Result |
|---|---|---|
| Baseline browser tabs | Memory free with 4 tabs open (a Claude chat, the project page, Gmail, and my dev.to dashboard) plus Diagnostics, nothing animating | 1.64 GB of 4 GB free, CPU at 5% |
| Memory during a build | Diagnostics while Claude pushed the fix and GitHub rebuilt the site | 1.51 GB of 4 GB free, CPU at 6% |
| Where it starts to slow | Worked a normal afternoon on this post, then checked Chrome's Task Manager | I didn't hit it. 4 tabs plus extensions, and nothing felt slow. |
| Recovery after a failed deploy | Claude pushed a file that breaks GitHub's site build on purpose. When I said "fix it," we timed until the deploy turned green. | 44 seconds. The live site never went down. |

Here's what each tab was using, from Chrome's Task Manager (Search + Esc on a Chromebook):

| Tab | Memory |
|---|---|
| The Claude chat where I'm building all of this | about 283 MB |
| Gmail | about 185 MB |
| The GitHub repo | about 98 MB |
| The Round 3 diagram | about 32 MB |

About that failed deploy: GitHub caught the broken file 31 seconds after the push, and the live page stayed on the last good version the whole time. Then I typed two words, "fix it," and 44 seconds later the deploy was green. I didn't open GitHub, read an error log, or touch a file. On this setup, recovery is a sentence. One caveat: Claude knew exactly what it broke, so this is a best case. A real mystery bug would take longer.

![Chromebook screen split in two. On the left, ChromeOS Diagnostics shows the MediaTek Kompanio 500 at 6% CPU usage, 37 degrees C, running at 0.793 GHz, with 1.51 GB of 4.00 GB of memory available. On the right, GitHub Actions for the 4gb-and-a-dream repo shows the fix deploy queued at the top, and below it the failed deploy from 3 minutes earlier with a red X, which took 31 seconds.](https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/recovery-test-side-by-side.png)

The heaviest thing on my laptop wasn't anything I built. It was the chat I built it in, and that chat is a long one: every round in this post happened in it. Everything I made used less than the tools I made it with.

## What it costs

| Part | Cost |
|---|---|
| The Chromebook | Already owned |
| GitHub and GitHub Pages | Free |
| Claude Pro, the cheapest plan with Claude Code | $20 a month, or $17 a month billed yearly |
| Claude Max, what I use | $100 a month |

Prices are from [Claude's pricing page](https://claude.com/pricing) as of November 2026.

I want to be clear about one thing: I built all of this on Max. I haven't tested whether this much work fits inside Pro's usage limits. Something the size of Round 1, one small app, feels like it should. Five rounds back to back might not. If you try it on Pro, I'd love to hear how far you got.

## What a 4 GB laptop can't do

This setup works because the heavy lifting happens somewhere else. That's also its limit. Here's what I'd still want a bigger machine for:

| Can't do (or didn't try) | Why |
|---|---|
| Work offline | Every step runs in the cloud or on GitHub. No internet, no build. |
| Run AI models on the laptop | 4 GB of memory isn't close to enough for a local model. |
| Heavy local tools | Things like Docker, phone emulators, or big compiles want more memory than this. I didn't try them. |
| Skip the GitHub clicks | Claude couldn't turn on GitHub Pages from its side. I clicked Settings, Pages, Save myself. |
| Test on the real live site from Claude's side | Claude's workspace couldn't reach github.io, so it tested the repo files. I checked the live site on the Chromebook. |

None of these stopped me. They're the edges I found, and they're worth knowing before you start.

## A deeper dive

For anyone curious about what's under the hood, here's the technical layer under the rounds.

**The stack.** Static HTML, CSS, and plain JavaScript on GitHub Pages. One library in the whole kit: three.js r128 from a CDN, for Round 2. No build server, no framework, no bundler. Necesito has a tiny Node script (`build.js`) that writes `index.html`, run in Claude's workspace, not on the laptop.

**A secret that never touches the repo.** Necesito needs my phone number, but the number isn't in any file. It rides in the link after the `#`, which browsers never send to the server. The page reads it, accepts digits only, and builds the text links:

```js
var raw = (location.hash || "").replace("#", "");
var ok = /^[0-9]{10,15}$/.test(raw);
var phone = raw.length === 10 ? "+1" + raw : "+" + raw;
// iOS format: sms:NUMBER&body=TEXT
button.setAttribute("href", "sms:" + phone + "&body=" + body);
```

Anything that isn't 10 to 15 digits turns the buttons off. Before this, the number was in the first commit, so I rewrote the history to one clean commit. Worth doing early, while the repo is minutes old.

**Keeping 3D light on a small device.** Two settings did most of the work in Round 2:

```js
// Cap sharpness: high-res screens can't multiply the pixel count past 1.5x
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
 
// Stop drawing when the tab is hidden, so a background tab costs nothing
document.addEventListener("visibilitychange", function () {
  if (document.hidden) { running = false; cancelAnimationFrame(rafId); }
  else if (!running) { running = true; rafId = requestAnimationFrame(tick); }
});
```

The second one also explains my first bad reading: with Diagnostics covering the tab, the scene had paused itself.

**How the failed deploy failed.** GitHub Pages runs Jekyll unless the repo has a `.nojekyll` file. Claude pushed a Markdown file with an unclosed Liquid tag (`{% raw %}{% if broken %}{% endraw %}`), and the Pages build failed in 31 seconds. GitHub kept serving the last good build, so the live site never went down. Deleting the file and pushing fixed it in 44 seconds.

**The demo video.** Playwright drives headless Chromium through each page and records it, then ffmpeg encodes the MP4. Fonts and three.js are routed to local copies so the recording doesn't depend on the network. The [script is in the repo](https://github.com/earlgreyhot1701D/4gb-and-a-dream/blob/main/scripts/record_tour.py).

**The limits to know up front:**

- **Static only.** GitHub Pages can't run a server, hold a database, or keep API keys secret. Anything that needs one of those needs a different host.
- **Public repo.** Free Pages needs a public repo, so everything in it is visible, history included.
- **Small samples.** Every number in this post is one Diagnostics reading, not a benchmark. Treat them as a sense of scale.

## Your setup, step by step

Everything from every round, in order:

1. **Get the accounts.** A free GitHub account and a Claude plan that includes Claude Code (Pro or Max).
2. **Make an empty repo.** Go to github.com/new, name it, check "Add a README file," and create it.
3. **Describe what you want in the Claude chat.** Ask Claude to interview you one question at a time. Answer in plain words.
4. **Approve one repo.** When Claude asks for access, approve only the repo you just made.
5. **Look at what it built.** Open it on your laptop. Say what feels off in one sentence. Repeat until it's right.
6. **Turn on Pages.** Settings, Pages, deploy from the main branch, Save. Wait about a minute.
7. **Open your link and check it on the real device.** Not just the preview.
8. **If a deploy breaks, say so.** Tell Claude what you see. Mine was fixed in 44 seconds.
9. **Keep Diagnostics handy.** On a Chromebook it's in the launcher. Side by side with your page, it shows what your laptop is really doing.
10. **Write down what goes wrong when it happens.** I didn't, and my Wi-Fi drop became a story I can't fully tell.

---

Thanks to [Alex Shev](https://dev.to/alexshev) for the idea for this post, and for helping me see that what I built on vacation could be useful to someone else. If you build with AI coding agents, his [Terminal Skills](https://terminalskills.io/) is worth a look.

---

Quick context if you are new here. I work in the California courts, running court operations for the county. I started building with AI in July 2025 and I have been learning in public ever since. I do not write the code. I direct, the agents generate, I validate and decide. I build the [Clew Suite](https://clewlabs.org), a set of civic tech tools for making complex systems easier to inspect. That is the lens I am writing from.

Built and written with AI assistance in November 2026, on a Chromebook. Claude (Opus 5.5) wrote the code and drafted this post from our build sessions. I directed, decided, and edited. Check the source before you quote me.

AI Assisted. Human Approved. Powered by NLP.

## 评论（9/9）

> **SkepAgent** · 2026-11-11T02:46:50Z　
> The side-by-side Diagnostics readings are what make this convincing for me — 60fps at 15% CPU on a 4GB Chromebook is a real number, not a vibe. I also liked the honest limits section, especially that the failed deploy took 44 seconds to fix and the live site never went down. The "write down what goes wrong when it happens" rule is the one I'll steal; undocumented outages always turn into stories you can't verify later.

---

> **Earl Grey** · 2026-11-11T04:41:22Z　
> Thank you! The side-by-side came from a mistake. My first Round 2 reading caught the scene resting, because Diagnostics was covering the tab and the 3D had paused itself. Once both were on screen at the same time, I could actually show my work.
>
> Helping people is the main reason I wrote this post, and that really made my day. Next time, a Wi-Fi-adjacent moment will be part of the story!

---

> **OneLifeVibe** · 2026-11-11T06:12:16Z　
> The side-by-side Diagnostics readings are what sold me on this — 60fps at 15% CPU on a 4 GB Chromebook makes the "full build kit" claim concrete instead of aspirational. I also liked the honesty about the limits: the 44-second failed-deploy recovery shows the safety net works, while the unrecorded Wi-Fi drop is a useful reminder that a cloud build's weakest link is the connection, not the laptop. The detail about keeping the phone number out of the repo and in the URL hash was a smart, practical touch. Did the 1.5x pixel-ratio cap noticeably change how the 3D scene looked, or was it invisible in practice?

---

> **Earl Grey** · 2026-11-11T15:52:37Z　
> Thank you! It was invisible in practice. My Chromebook’s screen is 1366×768, so the cap probably never even kicked in on my laptop. Where it matters is on phones and high-res screens, which can draw 2x or 3x the pixels. The cap keeps those from doing extra work nobody would notice.
>
> And yes, the connection is the weak link, not the laptop. That Wi-Fi drop taught me that. I’m glad the phone number detail was useful too!

---

> **Paul Lovelace** · 2026-11-11T18:38:16Z　
> The bit about Alex's comment changing how you saw the whole thing — that's the real story here, not the Chromebook. Constrained hardware just forces the question every builder should ask anyway: which parts of this workflow are actually essential? 60fps at 15% CPU on a 4 GB machine is a great number, but the 'describe what you want, answer one question at a time' flow is the part I'd steal first. Also: building your wife a digital bell while she was sick, then turning it into a guide — that's a good origin story for a post.

---

> **Earl Grey** · 2026-11-12T02:17:05Z　
> Thank you! Alex’s comment was definitely a big part of it. I built the digital bell because my wife was sick and I had a little laptop with me. I didn’t think of it as a guide until his comment helped me see it could help someone.
>
> And yes, steal the one-question-at-a-time flow! It came from me asking Claude to interview me instead of me trying to write out everything up front. It’s the easiest way I’ve found to get from an idea to something real.

---

> **Oleksandr** · 2026-11-12T05:02:19Z　
> "Everything I made used less than the tools I made it with" is a genuinely important observation — the chat window is now the heaviest app on the machine, and nobody plans for that.
>
> The 44-second fix after a deliberately broken deploy is the metric that matters most. On a 4 GB laptop, the question isn't whether it can compile, it's whether it can recover without leaving the chair.

---

> **Earl Grey** · 2026-11-13T00:37:57Z　
> Thank you! That line surprised me too. I went in expecting the 3D scene to be the heaviest thing, and it was the chat.
>
> “Recover without leaving the chair” is a great way to put it. One caveat I’d add: Claude knew exactly what it broke, so 44 seconds is a best case. A mystery bug would take longer. But the part that held up was that the live site never went down while I waited.

---

> **Oleksandr** · 2026-11-13T05:18:47Z　
> Exactly — a mystery bug is a completely different beast. But the fact that the live site stayed up during the whole fix means the recovery path was designed well, not just lucky. That's the part worth stealing.

## 关联链接

- https://claude.ai
- https://claude.com/pricing
- https://clewlabs.org
- https://dev.to/alexshev
- https://dev.to/earlgreyhot1701d/a-builder-in-cdmx-flu-edition-167
- https://docs.github.com/en/pages
- https://earlgreyhot1701d.github.io/4gb-and-a-dream/
- https://earlgreyhot1701d.github.io/4gb-and-a-dream/round-2-3d/
- https://earlgreyhot1701d.github.io/4gb-and-a-dream/round-3-diagram/
- https://earlgreyhot1701d.github.io/4gb-and-a-dream/round-4-video/
- https://github.com
- https://github.com/earlgreyhot1701D/4gb-and-a-dream
- https://github.com/earlgreyhot1701D/4gb-and-a-dream/blob/main/scripts/record_tour.py
- https://github.com/earlgreyhot1701D/necesito
- https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/4gb-tour.gif
- https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/recovery-test-side-by-side.png
- https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-1-necesito.gif
- https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-2-3d.gif
- https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-3-diagram.gif
- https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-3-side-by-side.png
- https://raw.githubusercontent.com/earlgreyhot1701D/4gb-and-a-dream/main/assets/article/round-4-side-by-side.png
- https://raw.githubusercontent.com/earlgreyhot1701D/necesito/main/assets/article/chromebook-check.png
- https://terminalskills.io/
- https://threejs.org

## 导航

- 项目页：[[10-项目/claude.ai_8701e897]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
