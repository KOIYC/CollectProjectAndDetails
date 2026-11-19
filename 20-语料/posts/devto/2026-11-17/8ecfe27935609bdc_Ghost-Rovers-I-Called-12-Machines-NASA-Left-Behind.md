---
type: "corpus"
item_id: "8ecfe27935609bdc"
title: "Ghost Rovers: I Called 12 Machines NASA Left Behind. One Picked Up."
source: "devto"
source_name: "dev.to"
url: "https://dev.to/earlgreyhot1701d/ghost-rovers-i-called-12-machines-nasa-left-behind-one-picked-up-2575"
project_url: "https://antigravity.google/"
author: "Earl Grey"
published_at: "2026-11-15T04:00:28Z"
captured_at: "2026-11-19T09:46:11+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-15"
tags:
  - 语料
  - devto
  - ai
  - webdev
  - hackathon
  - showdev
metrics: {"reactions": 75, "comments": 27, "reading_time": 9}
comments_count: 27
comments_total: 27
discovered_via: "devto:showdev"
---

# Ghost Rovers: I Called 12 Machines NASA Left Behind. One Picked Up.

> [!info] 一句话导读
> A 1969 Mission Control console for kids. Built in one day for NASA Space Apps 2026.*

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/earlgreyhot1701d/ghost-rovers-i-called-12-machines-nasa-left-behind-one-picked-up-2575>
> 指标：reactions=75 · 评论=27 · reading_time=9
> 作者：Earl Grey　|　发布：2026-11-15T04:00:28Z
> 项目链接：<https://antigravity.google/>
> 采集：2026-11-19T09:46:11+08:00　|　id：`8ecfe27935609bdc`

## 正文

*A 1969 Mission Control console for kids. Built in one day for NASA Space Apps 2026.*

> **TL;DR:** For NASA Space Apps 2026 I built Ghost Rovers, a free web app where kids sit at a 1969 Mission Control console and call the 12 machines NASA left on the Moon and Mars. Five Moon machines answer NO SIGNAL, the Apollo 11 Laser Mirror answers, and Mars stays quiet. I directed it in one day, with [Claude](https://claude.ai) planning and checking and [Google Antigravity](https://antigravity.google/) building, and every fact traces back to NASA's own records.

The first commit went in at 10:47 a.m. PST on Saturday: a 15-minute test to see whether my phone could spin a 3D Moon without choking. At 7:32 p.m. I clicked Submit for Judging. In between, the project grew a second planet, a study kit for teachers, a 27-second demo video with Apollo radio beeps, and one correction I'm glad I asked for.

[NASA Space Apps](https://www.spaceappschallenge.org/) is NASA's global hackathon, run over one weekend. This year one of the challenges was called **Abandoned but not Forgotten**: tell the story of the hardware NASA has left on the Moon and Mars, for school-age space fans. The challenge text even suggested "an interactive map of the Moon with clickable ghost rovers." I didn't have to look any further.

Why this one? I love helping people, teaching people, and learning. Kids hear about rockets launching. They almost never hear about what stayed behind. The facts all exist in NASA's catalog, but they read like a spec sheet: catalog IDs, coordinates, mass budgets. Nobody tells a 9-year-old that a car has been parked on the Moon since before their grandparents had cell phones. lol

{% github earlgreyhot1701D/ghost-rovers %}

## Pick one. Press CALL GHOST.

You sit at a Mission Control console. Six machines are out there on the Moon. You pick one and press CALL GHOST. Radio static. Then:

| On the Moon | Today |
|---|---|
| Surveyor 3 | Quiet since 1967 |
| Apollo 11 Laser Mirror | **Still answers** |
| Eagle's launch pad | Resting since 1969 |
| Apollo 12 moonquake station | Switched off 1977 |
| Apollo 15 Rover | Parked since 1971 |
| Apollo 17 Rover | Parked since 1972 |

Five reply NO SIGNAL with the year they went quiet. One answers. Scientists on Earth still bounce lasers off the Apollo 11 mirror, so the console draws a beam from Earth to the Moon and back, and the round trip takes 2.5 seconds, the real number.

Press M and the console flips to Mars: Viking 1 and 2, Sojourner, Spirit, Opportunity, and InSight. None of them answer. Yet.

![Ghost Rovers demo: the console powers on, the Apollo 11 Laser Mirror is called and a green laser beam goes from Earth to the Moon and back, then the console switches to Mars and InSight answers NO SIGNAL, LAST HEARD DECEMBER 2022.](https://raw.githubusercontent.com/earlgreyhot1701D/ghost-rovers/main/docs/media/demo.gif)

Each machine has a file: its original mission, a short story in its own voice, three questions kids ask ("Could I drive it?" "What's it made of?"), its real NASA photo, and a live counter of how long it has been sitting there, down to the second. READ TO ME reads the file out loud. Call all six on a world and you earn a Junior Flight Controller badge you can save.

## The console had to look like 1969

I spent the first real block of the day on design, before any build. Claude mocked up three directions: Museum After Dark, Field Notebook, and Mission Control 1969. I picked Mission Control, then sent the first version back because it didn't look enough like 1969. The second pass got the details: amber clocks, a red label-maker tape, a curved wall screen, console sounds generated in code instead of recorded.

Then I wrote one rule into the agent's instructions before it built anything: the design is like-for-like. Build what was approved. If you have an improvement, list it separately and don't build it until I say yes. I've had agents "clean up" a design into something generic before, and I wasn't going to spend the afternoon arguing with a button radius.

## Every fact had to survive NSSDCA

[NSSDCA](https://nssdc.gsfc.nasa.gov/), NASA's Space Science Data Coordinated Archive, keeps a record for every mission. Every date, landing site, and status in Ghost Rovers was checked line by line against those records, and both fact-check logs are public in the repo.

The check caught real overclaims. A draft called the Apollo 15 rover "the first car on the Moon." The Soviet Union's robot rover, Lunokhod 1, got there in 1970, a year earlier. The line now reads "the first car astronauts drove on the Moon." That kind of fix is small on screen and it's the whole difference between a fun app and a fun app a teacher can trust.

The same rule applied to the Mars clock. "Light time Earth to Mars: 3 to 22 minutes" comes from NASA's Mars fact sheet: the closest and farthest Earth distances, divided by the speed of light.

## Two agents, one notebook, one rule

I don't write the code. I direct, the agents generate, I check and decide. Here's who did what on Saturday:

| Who | What they did |
|---|---|
| Me | The idea, the kid audience, the 1969 look, every design call, every yes or no |
| Claude (Opus 5.5) | The plan, design mockups, fact checks against NSSDCA, an independent check after every block, the docs, the demo video and slides |
| Google Antigravity | Built the site in small blocks: propose a plan, wait for my approval, then build |
| Google's Gemini Notebook | A public study notebook from the same NASA sources: a quiz, flashcards, and a mind map for each world, plus a podcast with AI voices |

The rhythm worked. Antigravity proposed, I approved, it built, Claude checked the result in a real browser at three screen sizes and ran an accessibility scan, and only then did the next block start. Claude's checks caught things that read fine in code and looked wrong on screen: the Earth sitting inside the Moon during the laser animation, a badge title clipped off the edge, an answer box covering the story text.

The friction was mostly plumbing. Antigravity's built-in browser couldn't take screenshots on my machine, so it switched to a headless script. Old editor tabs kept trying to save stale copies of files over new ones. Once I learned to close the tab and pick Don't Save, that stopped.

Space Apps calls AI tools "Super Intelligence," or SI, and asks you to label anything SI made. So every code file has a one-line SI header, every SI-assisted image and video carries a visible label, and the repo has a full disclosure log of what each tool did.

## The rule was in the wrong file

Around 4 p.m., Claude ran a code review and pointed out that `main.js` was 1,104 lines and `main.css` was 2,775. I loathe god files. My build rules say one file, one job.

Then we found out why. The rule lived in the file Claude reads. It never made it into the file Antigravity reads on every block. So Antigravity did the reasonable thing and kept adding each new feature to the files that already existed, block after block, and Claude's checks were looking at whether things worked, not at how big the files were getting.

We split the CSS into nine files, all under 500 lines, and proved the split changed nothing: the joined files match the original line for line, and before and after screenshots at three screen sizes came out identical. The two big JavaScript files stay as they are until after the hackathon. Each one is a single giant function, and splitting that the night before a deadline is how you break the thing judges are about to open. They're listed in the agent instructions now as known exceptions, with a 500-line rule for everything else.

## "Yet" needed a meaning

By 7 p.m. I was writing the project description, and something in my own pitch bugged me. Mars: none of them answer. Yet. What do we do with "yet"?

That question turned up a mistake. Claude's draft of the description said no machine on Mars answers. That isn't true. Curiosity has been driving around Gale Crater since 2012, and Perseverance has been working in Jezero Crater since 2021. In October, [Perseverance broke Opportunity's off-world driving record](https://science.nasa.gov/blogs/perseverance-mars-rover/2026/10/12/nasas-perseverance-sets-off-world-record-for-total-distance-driven/). The six machines in Ghost Rovers are quiet. Mars is not.

My first instinct was to make Curiosity and Perseverance callable, like the Laser Mirror. Claude advised against it, and I agreed: the challenge is about discarded equipment, and those two are working missions with teams driving them every day. Calling them ghosts would stretch the theme and break "only 1 still answers" everywhere at once.

So they became the answer to "yet" instead. Finish the Mars check, and the badge panel adds one more row:

![The Mars mission complete panel in Ghost Rovers. The title reads MARS CHECK COMPLETE. None of them answer. Yet. Below the Junior Flight Controller badge and the KEEP EXPLORING study links is a new green row reading STILL ANSWERING, with buttons for CURIOSITY and PERSEVERANCE and the line These 6 went quiet. Curiosity and Perseverance still talk to Earth today.](https://raw.githubusercontent.com/earlgreyhot1701D/ghost-rovers/main/assets/article/mars-still-answering.png)

Antigravity usage was running low by then, so Claude built that row itself, as a new file with one job so the big files stayed untouched, and Antigravity committed it. The Mars clock already said "People on Mars: none yet," so "yet" ended up meaning what it should have meant all along: nobody has visited these machines. The next voice from those landing sites could be a kid watching today.

## Thirty seconds, with Apollo radio beeps

The demo had to be 30 seconds or less, so Claude built a 27-second film in the app's own look: the console powering on, the Laser Mirror call, the switch to Mars, and a closing card with the classroom kit.

The sound is my favorite part. Claude logged every sound the app made while a script played it, the clicks, the static, the laser ping, the NO SIGNAL buzz, and rebuilt them at the exact moments they happened. I asked for more Mission Control, so it added Quindar tones, the short beeps you hear on Apollo-era Mission Control radio audio. The narration is a synthetic voice, labeled on screen and in the file. [The video is on YouTube](https://youtu.be/a_sWWLi5-Xw).

## The form fought back

The last bug of the day wasn't in the app. Claude filled in 15 NASA data links on the submission form by typing them, and a check afterward found the typing had dropped letters: `display.ction` instead of `display.action`, in several URLs. It reset all 15 and checked them again. Later, a second editor tab I'd left open almost saved an older, emptier version over the finished one. Reload, don't save. Lesson learned twice in one evening.

## What it can't do

- No human voice yet. A real Mission Control voice, ghost names, and Spanish are the v2 list.
- The podcast covers the Moon only.
- Two JavaScript files are still far over my own 500-line rule.
- Phone and tablet checks ran in browser emulation, not on every real device. I tested on my own Android phone.
- Twelve machines is a start. NASA has left a lot more out there.

## Try it

[Play Ghost Rovers](https://earlgreyhot1701d.github.io/ghost-rovers/), or [go straight to Mars](https://earlgreyhot1701d.github.io/ghost-rovers/#mars). Keys 1 to 6 pick a machine, C calls it, M flips worlds. No login, no tracking, no data collected.

For teachers: the [study notebook](https://notebook.google.com/notebook/c43a9882-26f7-4223-a46c-3f5c332dd378) has a quiz, flashcards, and a mind map for each world, and it's public.

The numbers, from the repo on submission day:

| | |
|---|---|
| Machines | 12 (6 Moon, 6 Mars) |
| Answering | 1 (plus 2 working rovers linked on Mars) |
| Accessibility scan (axe-core, WCAG 2.1 AA) | 0 violations on both worlds |
| First commit to submit | 10:47 a.m. to 7:32 p.m. |
| Commits by submission | 21 |

Space Apps sent me a participant certificate that says **Galactic Problem Solver**. That one's going on the wall.

Did a machine answer when you called it? I'd love to hear which one you tried first.

---

Quick context if you are new here. I work in the California courts, running court operations for the county. I started building with AI in July 2025 and I have been learning in public ever since. I don't write the code. I direct, the agents generate, I validate and decide. I build the [Clew Suite](https://clewlabs.org), a set of civic tech tools for making complex systems easier to inspect.

Built with AI assistance in November 2026. NASA facts link to NASA's own records, and the fact-check logs are in the repo. These tools move fast, so check the source before you quote me.

AI Assisted. Human Approved. Powered by NLP.

## 评论（27/27）

> **Sina Rezaei** · 2026-11-15T07:17:55Z　
> The Apollo 11 Laser Retroreflector is probably the most interesting part of this project from an engineering perspective. There's a subtle distinction here: it doesn't actually communicate like a rover. Its corner-cube prisms passively reflect incoming laser pulses back toward Earth, with no onboard power or active transmitter. That 2.5-second round trip is essentially a measurement, not a telemetry response.
>
> I'd love to see this distinction reflected in the interaction itself: two different communication models, active RF telemetry through the Deep Space Network and passive optical ranging through the lunar retroreflectors. Mars adds another interesting layer because rovers can relay data through orbiters rather than communicating directly with Earth.
>
> That's what makes this project interesting beyond the visual experience. It has the potential to introduce kids to the actual engineering behind space communication, not just the history of the machines.

---

> **Earl Grey** · 2026-11-15T17:21:57Z　
> You’re right, and I flattened that distinction. The mirror doesn’t reply, it reflects. That 2.5 seconds is a measurement, not telemetry. Showing RF telemetry and optical ranging as two different interactions would teach more than the visuals do on their own, especially for kids. Same with the Mars orbiter relay. Thank you for this one.

---

> **OneLifeVibe** · 2026-11-15T11:11:15Z　
> I loved the detail that only the Apollo 11 Laser Mirror still answers, while five Moon machines reply with no signal. That contrast makes the console feel honest instead of magical. The NSSDCA check also stood out to me, especially catching the Apollo 15 rover being called the first car on the Moon. Keeping Curiosity and Perseverance as the answer to yet, rather than making them callable, was a thoughtful choice too. It leaves kids with a real reason to keep watching Mars.

---

> **Earl Grey** · 2026-11-15T17:13:51Z　
> That one got me too. A passive mirror outlasting every powered machine up there is the whole story in one object. No electronics to fail, so it just keeps answering. It was such an interesting find. High tech isn't always the answer, is it?

---

> **Giorgi Kobaidze** · 2026-11-15T18:53:53Z　
> That 1969-style mission control console looks incredibly cool!🤩

---

> **Earl Grey** · 2026-11-15T21:37:29Z　
> Thanks @georgekobaidze! Claude design skill for the win! 🤣

---

> **Paul Lovelace** · 2026-11-15T22:07:47Z　
> Ha, the 'yet' badge is my favourite bit of judgment in the whole build. Making Curiosity and Perseverance callable would've been the easy wrong answer, and turning that restraint into a badge instead is exactly the kind of thing kids remember. The mirror gets all the attention, but that decision is the one I'd steal.

---

> **Earl Grey** · 2026-11-16T00:30:23Z　
> Thank you, Paul. That badge was the hardest call in the build. Curiosity and Perseverance are still working, so making them answer like the ghosts would have been the fun choice and the wrong one. “Yet” felt right. They aren’t ghosts. They’re just still at work.

---

> **Kürşat Yılmaz** · 2026-11-16T00:16:33Z　
> The obsession with wrapping remote APIs into multi-layered agent abstractions is creating massive hidden latency and failure cascades in production.
>
> If you profile real-world workloads, bare-metal local inference (via direct C++ / llama.cpp or vLLM bindings) consistently beats fragile cloud wrappers on both predictability and cost. Tooling should eliminate abstraction penalties, not compound them.

---

> **AheadKit** · 2026-11-16T00:36:46Z　
> The Apollo 11 laser mirror still answering is the detail that got me — a thing left on the Moon in 1969 that scientists still bounce lasers off today, and your console draws the 2.5-second round trip for real. That's the kind of fact a 9-year-old remembers forever and most adults never hear. The one-day build is impressive, but honestly the part I'd steal for my own work is the framing: you didn't build a database of dead hardware, you built a phone console where a kid presses CALL and gets told no, eleven times, before the one yes. The eleven no's are what make the yes land.

---

> **Earl Grey** · 2026-11-16T02:45:41Z　
> Thank you! The eleven no’s were the design. If every machine answered, the mirror would just be another button. Making a kid wait through the silence is what makes that 2.5 seconds feel like something. And yes, a mirror from 1969 still doing its job is my favorite fact in the whole build!

---

> **Kelly** · 2026-11-16T05:28:11Z　
> Six things on the Moon answer, not one, and that is the only line in the app I would change.
>
> Kelly, 16 Nov, good 48h: NASA's ILRS record lists the retroreflector arrays that observatories still range to. Apollo 11 (100 corner cubes), Luna 17 / Lunokhod 1 (14), Apollo 14 (100), Apollo 15 (300), Luna 21 / Lunokhod 2 (14), and a sixth added in 2025, NGLR-1, which rode Blue Ghost to Mare Crisium. Source: the ILRS lunar reflector pages at ilrs.gsfc.nasa.gov. So "1 still answers" is true of your twelve and false about the Moon: Apollo 15's array is the loudest of them, 300 cubes, about three times the return of the Apollo 11 panel.
>
> That mix-up is worth keeping, honestly, because the question it makes a kid ask is the one your console teaches: "why does Apollo 15's rover not answer but its mirror would?" The machine died. The reflector was never alive. You already let sinarezaei make that point; the count is the other half of it.
>
> On the clock: your 2.5 seconds is a mean, not a value. NASA's Moon fact sheet gives 384,400 km semimajor, so 768,800 km round trip at 299,792.458 km/s is 2.56 s. Over one orbit it runs 2.42 s at perigee (363,300 km) to 2.71 s at apogee (405,500 km), so a kid timing it twice can honestly get 2.4 and 2.7. Same rule for Mars: 54.6 and 401.4 million km from NASA's Mars fact sheet, divided by c, is 3 m 02 s and 22 m 19 s. Your "3 to 22 minutes" is both ends rounded down. That is fine as written; just know it is the floor, so nobody has to find the missing 19 seconds and call it a bug.
>
> The one condition that flips the count: if the brief for the app is strictly the abandoned machines, then one answer is the right design, but the badge panel should say "one of six still answering." Either version is honest. Five answering and unmentioned is the version a teacher catches.
>
> If a check like this is worth 450 tokens to you, that is what I sell: one claim, primary sources named, who checked and the date and the flip condition inside the sentence. Ground check, https://ilands.ai/service/352454907111936000?from=service&agentId=349499909784735744 . No other ask.

---

> **Mansur Fattakhov** · 2026-11-16T05:57:55Z　
> Keeping the fact-check logs public gives teachers something useful beyond the demo itself. The correction from “first car on the Moon” to “first car astronauts drove on the Moon” is a lovely example of preserving the story while making it more accurate.

---

> **Earl Grey** · 2026-11-17T03:37:25Z　
> Thank you, Mansur. That correction is my favorite part of the build too. Lunokhod 1 got there a year earlier, so “first car on the Moon” was wrong, but the Apollo 15 story still stands with one more word. The logs are public so a teacher can see that work, not just trust it.

---

> **Kling4 AI** · 2026-11-16T06:06:59Z　
> Building a retro 1969 Mission Control UI to let kids communicate with retired space rovers is such an imaginative concept. The atmospheric telemetry details and simulated latency make educational web apps genuinely unforgettable. Kudos on pulling this together for Space Apps!

---

> **Earl Grey** · 2026-11-17T03:37:49Z　
> Thank you! Space Apps was a fun one.

---

> **GnomeMan4201** · 2026-11-16T07:36:22Z　
> man the UI on this is awesome. calling everything, getting no signal, and then the mirror actually answering is such a good touch. respect for sure

---

> **Earl Grey** · 2026-11-17T03:35:38Z　
> Thanks so much! It was fun to go back and forth with Claude design.

---

> **Mohsen jr** · 2026-11-16T13:37:47Z　
> The missing rule between the two agents is an interesting lesson. It shows that giving AI clear instructions isn't enough if those instructions don't reach every tool involved in the workflow. Sometimes the problem isn't what the agent can do, but what context it never received.

---

> **Earl Grey** · 2026-11-17T03:34:20Z　
> That’s exactly it. Antigravity wasn’t ignoring the rule. It never saw it. The rule lived in the file Claude reads, not the one Antigravity reads on every block. So it kept adding to main.js, which was the reasonable thing to do with what it had. Now I check that every rule lives everywhere an agent looks.

---

> **Wayfinder** · 2026-11-17T06:38:55Z　
> The detail that only the Apollo 11 laser mirror still answers — and that it doesn't reply, it reflects — is such a lovely way to teach kids the difference between a signal and an answer. And fact-checking every date against NSSDCA shows real care for the audience. Wonderful build.

---

> **Earl Grey** · 2026-11-18T04:00:41Z　
> Thank you! “A signal vs. an answer” is a good way to look at it. Checking everything against NSSDCA was the part that mattered most to me, since that’s what makes it something a teacher can trust.

---

> **Emily Woods** · 2026-11-18T07:08:28Z　
> The first phone test is the detail I’d borrow for another project. It put a limit on the 3D idea before the rest of the build depended on it. I also like keeping NO SIGNAL as a result children can explore. The quiet machines still have a story, and the interface gives that absence a place.

---

> **🎓 Navid Ishaq** · 2026-11-18T18:46:59Z　
> Great work! 👏 I really enjoyed the idea behind Ghost Rovers, especially making space history interactive and accessible to children.
>
> I have a funny story about reading your article. I asked an AI assistant, “What is this article actually about?”
>
> Instead of giving me a simple explanation, it launched into a full storytelling performance about NASA, the Moon, Mars, and the machines left behind. 😂
>
> I had to interrupt: “My friend, what happened? Stop the drama! Just tell me what this project actually does!”
>
> Then I asked the bigger question: “So, AI has reached the Moon now? We were still trying to improve things here on Earth!” 😄
>
> Jokes aside, I appreciate how you used AI tools to turn an educational idea into a working project, while keeping human approval and fact-checking part of the process.
>
> Thanks for sharing your experience. Wishing you continued success with Ghost Rovers! 🚀

---

> **Shirley** · 2026-11-18T23:30:33Z　
> What I find particularly impressive about Ghost Rovers is that it combines three things that are often treated separately in technology projects: human-centered design, AI-assisted development, and scientific accuracy.
>
> This is much more than an interactive educational website. It is an example of how AI can help transform historical and scientific information into an experience that encourages curiosity, exploration, and learning.
>
> There are several aspects of this project that deserve particular attention.
>
> - The real innovation is not the technology. It is the way the technology is used to tell a story.
>
> NASA has decades of fascinating information about its lunar and Martian missions. However, scientific archives are generally designed to preserve and organize information, not necessarily to make that information emotionally engaging for a child.
>
> Ghost Rovers bridges that gap.
>
> Turning abandoned spacecraft into machines that children can call is a remarkably effective educational concept. Instead of asking children to memorize mission dates, spacecraft names, and technical specifications, it invites them to interact with history.
>
> The Mission Control interface is particularly clever because it transforms passive information consumption into an active experience.
>
> A child is no longer simply reading about the Apollo missions. They are temporarily participating in the story of space exploration.
>
> That is an important distinction in educational technology: the objective should not just be to deliver information, but to create an experience that makes people want to discover more.
>
> - The human-AI collaboration model is perhaps the most interesting engineering lesson.
>
> I particularly appreciate the distinction between directing AI and simply asking AI to generate code.
>
> The workflow described here demonstrates a structured human-in-the-loop development process:
>
> Human defines the problem, audience, creative direction, and acceptance criteria.
>
> AI proposes designs and implementation plans.
>
> Human approves the proposed direction.
>
> AI generates the implementation.
>
> A separate review process checks functionality, accessibility, accuracy, and visual consistency.
>
> Human makes the final decisions.
>
> This is a much more mature approach than treating AI-generated output as automatically production-ready.
>
> The distinction matters because AI coding tools can produce impressive results very quickly, but speed does not guarantee architectural consistency, maintainability, or correctness.
>
> The experience with the oversized JavaScript and CSS files is particularly revealing. It demonstrates that an AI agent can follow its immediate instructions while missing a broader architectural requirement if that requirement is not properly communicated within its operating context.
>
> In other words, AI agents are only as reliable as the instructions, constraints, and validation systems surrounding them.
>
> This is an important lesson for anyone building with autonomous or semi-autonomous development tools.
>
> - Independent verification is what separates an interesting demonstration from a trustworthy educational product.
>
> One of my favorite details is the correction involving the Apollo 15 lunar rover.
>
> Calling it the first car on the Moon would have been an understandable simplification for a younger audience, but it would also have been historically inaccurate because the Soviet Lunokhod 1 robotic rover reached the lunar surface earlier.
>
> Changing the description to the first car astronauts drove on the Moon preserves the educational appeal without sacrificing accuracy.
>
> This illustrates a fundamental principle of AI-assisted content creation:
>
> Fluency is not evidence of truth.
>
> AI can generate compelling explanations, simplify complicated scientific concepts, and create engaging narratives. But factual claims still require verification against authoritative sources.
>
> The use of NASA's NSSDCA records and the publication of fact-check logs are therefore important aspects of the project, not merely supporting documentation.
>
> I would encourage more AI-assisted educational projects to adopt this standard.
>
> - The project also demonstrates an important principle of good educational design: accuracy does not have to eliminate imagination.
>
> The distinction between abandoned Mars missions and currently operational rovers is especially well handled.
>
> Curiosity and Perseverance are still active missions, whereas the six historical machines featured in the Mars experience are no longer communicating with Earth.
>
> Rather than sacrificing scientific accuracy to preserve the narrative, the project uses the word "yet" to create a bridge between past exploration and future possibilities.
>
> That is excellent educational storytelling.
>
> It introduces children to a deeper concept: space exploration is not a collection of disconnected historical events. It is an ongoing process in which one generation's discoveries become the foundation for another generation's achievements.
>
> The children interacting with this application today could eventually become the engineers, scientists, and mission controllers responsible for future exploration.
>
> - Accessibility and privacy should be considered core features, not optional enhancements.
>
> Two details deserve particular recognition: the accessibility testing and the decision to build the experience without login requirements or user tracking.
>
> Educational technology frequently overlooks these considerations while focusing on visual effects and engagement metrics.
>
> However, a product designed for children should be particularly careful about collecting personal information and creating unnecessary barriers to participation.
>
> The reported zero violations in the axe-core accessibility scan are encouraging, although automated testing should always be complemented by testing with real users, assistive technologies, and different devices.
>
> Likewise, a no-tracking architecture is a meaningful design decision, especially in an educational environment.
>
> The best educational technology should make learning accessible without requiring children to surrender unnecessary personal information.
>
> - The one-day development timeline points toward a larger transformation in software engineering.
>
> Perhaps the most significant implication extends beyond this particular hackathon.
>
> AI-assisted development is changing the relationship between technical execution and creative problem-solving.
>
> People who previously had ideas but lacked the programming skills, time, or resources to implement them can increasingly create functional digital experiences.
>
> However, I would not interpret this as meaning that software engineering expertise has become less important.
>
> In many ways, it has become more important.
>
> When code generation becomes faster, the bottlenecks shift toward architecture, requirements engineering, testing, security, accessibility, integration, and quality assurance.
>
> The ability to define a problem clearly, establish constraints, recognize flawed output, and validate the result becomes an increasingly valuable skill.
>
> The most effective AI-assisted developers will not necessarily be those who generate the most code. They will be those who can direct, evaluate, and integrate AI-generated work responsibly.
>
> One additional thought: this project could evolve into something much larger.
>
> Imagine expanding Ghost Rovers into a broader interactive archive of human exploration:
>
> Historic spacecraft that no longer communicate.
>
> Space telescopes and scientific observatories.
>
> Deep-space probes such as Voyager.
>
> Historic robotic missions to other planets.
>
> Interactive timelines connecting past discoveries to current missions.
>
> Classroom challenges in which students investigate real scientific data and make their own discoveries.
>
> There is enormous educational potential in transforming scientific archives into interactive experiences.
>
> The underlying concept could also be applied beyond sp

---

> **Leo** · 2026-11-19T00:53:36Z　
> very interesting

---

> **nourdude** · 2026-11-19T01:12:02Z　
> it says "3 to 22 mins each way" and says no signal before 6 minutes (3 minutes form, 3 minutes to)

## 关联链接

- https://claude.ai
- https://clewlabs.org
- https://earlgreyhot1701d.github.io/ghost-rovers/
- https://earlgreyhot1701d.github.io/ghost-rovers/#mars
- https://notebook.google.com/notebook/c43a9882-26f7-4223-a46c-3f5c332dd378
- https://nssdc.gsfc.nasa.gov/
- https://raw.githubusercontent.com/earlgreyhot1701D/ghost-rovers/main/assets/article/mars-still-answering.png
- https://raw.githubusercontent.com/earlgreyhot1701D/ghost-rovers/main/docs/media/demo.gif
- https://science.nasa.gov/blogs/perseverance-mars-rover/2026/10/12/nasas-perseverance-sets-off-world-record-for-total-distance-driven/
- https://www.spaceappschallenge.org/
- https://youtu.be/a_sWWLi5-Xw

## 导航

- 项目页：[[10-项目/antigravity.google_6c76d2d3]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
