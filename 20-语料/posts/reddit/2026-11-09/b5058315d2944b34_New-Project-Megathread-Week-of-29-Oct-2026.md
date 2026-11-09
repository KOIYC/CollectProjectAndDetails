---
type: "corpus"
item_id: "b5058315d2944b34"
title: "New Project Megathread - Week of 29 Oct 2026"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xiz2ik/new_project_megathread_week_of_29_oct_2026/"
author: "AutoModerator"
published_at: "2026-10-30T07:01:09+08:00"
captured_at: "2026-11-09T09:41:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-10-30"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - New Project Megathread
metrics: {"score": 40, "comments": 256, "upvote_ratio": 0.9347826086956522}
comments_count: 192
comments_total: 256
discovered_via: "reddit:14d+settle10"
---

# New Project Megathread - Week of 29 Oct 2026

> [!info] 一句话导读
> Welcome to the **New Project Megathread!**

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xiz2ik/new_project_megathread_week_of_29_oct_2026/>
> 指标：得分=40 · 评论=256 · 赞踩比=0.9347826086956522
> 作者：AutoModerator　|　发布：2026-10-30T07:01:09+08:00
> 项目链接：—
> 采集：2026-11-09T09:41:26+08:00　|　id：`b5058315d2944b34`

## 正文

Welcome to the **New Project Megathread!**

This weekly thread is the new official home for sharing your new projects (younger than three months) with the community.

To keep the subreddit feed from being overwhelmed (particularly with the rapid influx of AI-generated projects) all new projects can only be posted here.

**How this thread works:**

* **A new thread will be posted every Friday.**
* **You can post here ANY day of the week.** You do not have to wait until Friday to share your new project.
* **Standalone new project posts will be removed** and the author will be redirected to the current week's megathread.

To find past New Project Megathreads just use the [search](https://www.reddit.com/r/selfhosted/search/?q="New%20Project%20Megathread%20-"&type=posts&sort=new).

# Posting a New Project

We recommend to use the following template (or include this information) in your top-level comment:

* **Project Name:**
* **Repo/Website Link:** (GitHub, GitLab, Codeberg, etc.)
* **Description:** (What does it do? What problem does it solve? What features are included? How is it beneficial for users who may try it?)
* **Deployment:** (App must be released and available for users to download/try. App must have some minimal form of documentation explaining how to install or use your app. Is there a Docker image? Docker-compose example? How can I selfhost the app?)
* **AI Involvement:** (Please be transparent.)

Please keep our rules on self promotion in mind as well.

Cheers,

## 评论（192/256）

> **Protectator**（11 分） · 2026-10-30T07:02:48+08:00　
> **Project Name:** Natel, the contact editor your CardDAV server is missing
>
> **Demo:** [https://demo.natel.app/contacts](https://demo.natel.app/contacts) (no sign-up, fake contacts)
> **Website Link:** [https://natel.app](https://natel.app)
> **Code (MIT License):** [https://github.com/KewinDousse/natel](https://github.com/KewinDousse/natel)
>
> **Description:** When I moved my contacts from Google to Radicale, I could no longer edit them in a browser. Radicale and Baïkal don't include a contact editor, and InfCloud hasn't had a release since 2015. So I built Natel to edit the contacts already on the server.
>
> https://i.redd.it/jmumz6z3mhyh1.png
>
> **Features:** search, photos, groups, multiple address books, .vcf import/export, mobile layout.
>
> The priority is not breaking existing contacts. Natel keeps the fields it doesn't edit when it saves, and if a contact changed on another device in the meantime, it shows a conflict instead of overwriting it. It's in beta, so export your address books first.
>
> **Testing:** end-to-end tests run in CI against Radicale, Baïkal and Xandikos. I also tested it by hand with DAVx5 on Android and with an iPhone. Nextcloud is not tested.
>
> **Deployment:** one Docker container (amd64 and arm64, around 16 MB of RAM idle), configured with CARDDAV\_URL. There's a Compose example in the README.
>
> \- No database: contacts stay on your server.
>
> \- You log in with your CardDAV credentials. The password is kept in memory for the session only.
>
> \- At most once a day while the app is in use, Natel reads a static file on GitHub Pages to check for a new release. Nothing about your contacts or accounts is sent. You can disable it in the config.
>
> **AI Involvement:** While I chose the tech stack and guide the overall architecture, AI agents (mostly Claude Code, some Codex) write almost all of the code. I review the structure, but I only read the code itself when an agent asks me about it. The tests focus on the risky parts: vCard round trips, conflicts, and end-to-end runs on the three servers. This comment was drafted with AI help.
>
> Feedback from Radicale, Baïkal or Xandikos users is welcome, especially on setup and missing features.

---

> **dutiful_joseph**（2 分） · 2026-10-30T07:08:05+08:00　
> That conflict handling is a nice touch, nothing worse than syncing and finding half your contacts got nuked by a stale edit. Been looking for something lightweight to fill that browser gap ever since I ditched Google Contacts. Giving the demo a spin now.

---

> **Protectator**（1 分） · 2026-10-30T07:30:25+08:00　
> Thanks! Yeah, I hate finding out I've lost edits... I needed one central place to work on my contacts that I could trust.
>
> I still have a few rough edges to fix and more testing to do, but I'd like it to fit more setups than just mine, so I'm curious how it goes on yours if you end up trying it.

---

> **buldezir**（3 分） · 2026-10-30T07:36:08+08:00　
> Project Name: Lemmary
>
> **Repo/Website Link**: [https://github.com/buldezir/lemmary](https://github.com/buldezir/lemmary) [https://lemmary.app/](https://lemmary.app/)
>
> **Description**: self-hosted document archive with OCR, AI tagging and AI search. October update. Try it without installing anything: [https://demo.lemmary.app](https://demo.lemmary.app)
>
> Core feature, that stands out from paperless-ngx and other similar projects:
>
> * Deep Research lets you ask questions about your whole archive, like "how much did I pay for car insurance since 2022" or "Search web for tax return guidance/law and find me all purchases applicable for tax refund". It finds the right documents, reads them, adds up the numbers and links every figure back to its document. Chats are saved and you can come back to them later.
>
> **Deployment:** one docker container (\~40mb ram idle) [https://lemmary.app/docs/self\_hosting.html](https://lemmary.app/docs/self_hosting.html)
>
> **AI Involvement:** agent writes code, i review and test everything manually (in addition to e2e/unit test suite)

---

> **GuardouApp**（10 分） · 2026-10-30T07:55:25+08:00　
> **Project Name**: Guardou!
>
> **Repo/Website Link**: [guardou.app](https://guardou.app) / [Github](https://github.com/GuardouApp/Guardou)
>
> **Description:** Google Drive Alternative. Simple file storage designed for non-technical users. SSO and Sharing Supported.
>
> https://i.redd.it/uzlbuc8yshyh1.png
>
> **Deployment:** docker-compose file. Mobile support only through browser at the moment, no apps.
>
> **AI Involvement:** I’m a professional software engineer, AI was used to speed up development.
> Prompts are not given on a macro level “build feature X”, instead they are: “add column X table Y”.
> Stack, dependencies, feature behavior, etc, are decided by me, the structure and initial APIs were made by hand so the agent had a reference to follow. Ai builds the code but does not decide anything.
> The server side uses C# which is the language I know the most. The frontend uses Flutter, which I don’t have experience, but decided to use in order to have shared frontend code to web and mobile apps in the future.
> Docs, UI/UX, are made by hand.

---

> **Alternative_One_4804**（2 分） · 2026-10-30T07:56:45+08:00　
> **Project Name:** OpenTodo
> **Repo/Website Link:**
> GitHub: [https://github.com/OpenTodoApp/OpenTodo](https://github.com/OpenTodoApp/OpenTodo)
> Website and docs: [https://open-todo.app](https://open-todo.app/)
> Live demo (no sign-up, resets nightly): [https://demo.open-todo.app](https://demo.open-todo.app/)
>
> **Description:**
> OpenTodo is a self-hosted, local-first task manager, an open-source alternative to Todoist, TickTick and Things. Your tasks live on your own server. Every device keeps a full copy, so it works offline and syncs when it reconnects. It's AGPL-3.0, has no telemetry, and has no paid tier, ever, including the mobile apps.
>
> **What's included**:
> Quick add in plain language ("Call Sarah next Wed at 3pm #work every 2 weeks"), in six languages
> Projects, sections, sub-projects, subtasks, labels, a filter language and saved views
> List, board, calendar (day, week, month) and timeline views
> Due dates, deadlines, start dates, Someday and This Evening; recurring tasks, habits with streaks, and reminders through web push, ntfy, Gotify, Pushover or a webhook
> Sharing projects with family or a small team, mentions, comments, workspaces, and public links for a shopping list
> A weekly review, focus mode, time tracking, custom fields and automation rules
> CalDAV, two-way calendar sync (CalDAV and Google), calendar feeds, email to task, GitHub and GitLab issue import, an Obsidian-compatible Markdown vault, a REST API, a CLI and an MCP server
> Optional end-to-end encryption, passkeys, 2FA, SSO (OIDC), and audit logs
> Importers for Todoist, TickTick, Things, Microsoft To Do and others, plus CSV
>
> **Who it's for**:
> people who want the polish of a commercial task app without a subscription or their data on someone else's servers. One person can host it for a whole household.
>
> **Deployment:**
> **Status:** released and in active use. The current version is 0.16.0.
> **Docker image:** ghcr.io/opentodoapp/opentodo for amd64 and arm64. A distroless image, about 13 MB to download.
> docker run -d -p 8080:8080 -v opentodo-data:/data ghcr.io/opentodoapp/opentodo:stable
> Open [http://localhost:8080](http://localhost:8080/); the first visit creates your account. No configuration is needed and there are no mandatory env vars. It runs on a Raspberry Pi.
>
> **Other ways to install:** Docker Compose, plain binaries, and guides or templates for Coolify, Unraid, Umbrel, CasaOS, Synology, TrueNAS, Portainer, Dokploy, Cosmos, Runtipi, Helm and more.
>
> **Documentation:** self-hosting docs at [https://open-todo.app/docs](https://open-todo.app/docs) (reverse proxy, backups, SMTP, SSO, upgrades).
>
> **Apps:**
> a PWA you install from the browser;
> an Android app (APK on GitHub releases; Google Play in closed testing);
> an iOS shell you can build yourself (App Store planned).
>
> **Roadmap to 1.0:** [https://open-todo.app/blog/the-road-to-1-0/](https://open-todo.app/blog/the-road-to-1-0/)
>
> **AI Involvement:**
> I'll be fully transparent: OpenTodo is built with heavy use of AI coding tools (Claude Code). I decide what gets built, the product design and the architecture. Every behaviour change starts as a written spec (OpenSpec) that I review, and the AI writes most of the code against it. Quality comes from the process, not from trust in the model:
> every PR runs the full CI: Go and web test suites, Playwright end-to-end tests, CodeQL, gosec, fuzzing, accessibility and visual checks;
> security-sensitive areas have had dedicated audit passes;
> the specs, tests and history are all public in the repo, so you can judge for yourself.

---

> **TacoRaider08**（-5 分） · 2026-10-30T08:29:27+08:00　
> if ur still reading books without visualization in 2026, ur falling behind...
>
> I built Picta using Magic Hour's API, which creates insane scenes for whatever you're reading. try it out at picta-jet.vercel.app, see how I built it at github.com/defAaron/picta, and check out Magic Hour AI at magichour.ai
>
> https://i.redd.it/6p6unzok1iyh1.jpeg

---

> **codectl**（1 分） · 2026-10-30T08:32:24+08:00　
> * **Project Name:** Reelsaw
> * **Repo/Website Link:** [https://github.com/osbytes/reelsaw](https://github.com/osbytes/reelsaw)
> * **Description:** Long video's in - viral vertical clips out. On your own hardware.
>    * Clip editor preview matching actual render
>    * Clean transcripts with entity recognition, disfluency flagging, and self-improvement
>    * Burned-in caption blurring that respects game UI / HUD and split layout
>    * Sophisticated frame/layout selection UltraFace 1.2MB ONNX 4fps picks layout per segment
>    * Research backed clip selection map -> pool -> rank - chunked transcript at long pauses with 20% overlap
>    * Resilient/resumable processing stages with each stage incrementally storing outputs (particularly important for local models)
>    * Fully local AI models (also support any external provider) across clip selection and transcription with operator dashboard to hot-swap at runtime
>    * Asset overlays (images, gifs, audio), intro/outro, and templates
>    * MCP so an agent can drive any action (works locally too)
> * **Deployment:**
>    * docker compose [https://github.com/osbytes/reelsaw/tree/main/deploy](https://github.com/osbytes/reelsaw/tree/main/deploy)
>    * one-line install script to run docker compose based on available specs
>       * [https://reelsaw.com/#install](https://reelsaw.com/#install)
>       * \`curl -fsSL [https://raw.githubusercontent.com/osbytes/reelsaw/main/deploy/install.sh](https://raw.githubusercontent.com/osbytes/reelsaw/main/deploy/install.sh) | bash\`
> * **AI Involvement:** Mostly agent-driven development with code review on core modules and lots of manual and automated testing
>
> https://i.redd.it/mp9o34fu1iyh1.png

---

> **CrispyBegs**（3 分） · 2026-10-30T08:37:21+08:00　
> >*if ur still reading books without visualization in 2026, ur falling behind...*
>
> is this tongue in cheek?

---

> **Yoshiofthewire**（2 分） · 2026-10-30T08:57:11+08:00　
> **Project**: Ky Suite
> **Website**: [https://busnes.app](https://busnes.app)
> **Code (MIT License)**: [https://github.com/Busnes-app](https://github.com/Busnes-app)
> **Promo Video**: [Ky in 75 Seconds](https://www.youtube.com/watch?v=qSSwMnZTTrw)
>
> **Description:** I've been building a set of self-hosted apps called Ky: KyPost (webmail and conatcts on top of your existing IMAP, or self hosted server with pass through Cloudflare or AWS), KyIdentity (an OIDC provider with passkeys and phone push), KyDNS, KyCalendar, KyNotes, KyDrive, KyMessaging (Powered by Element / Matrix), a Docker/K8s console and monitoring. Ten small, separate containers. Together they share one login and one encrypted backup.
>
> Mail, sign-in and DNS run my own house every day. The other seven are installed on real hardware and pass their tests, but nobody except me has used them. That's the problem.
>
> I'm looking for a handful of people with a spare box or VPS who will install one or two apps and tell me where it went wrong. Bugs, confusing docs, "why would anyone do it this way": all useful. Every app has its own README, or you can let KyQuickStart AI do the install: it drives Claude Code, Codex, Gemini CLI or opencode over SSH and reports every place a README was wrong.
>
> There are also two Android apps, KyPost (mail) and KyAuth (sign-in approvals and one-time codes), for Android 12 and up. If you want to test those, DM me the email of your Google account and I'll add you to the Play testing track.  iOS and Linux Mobile Apps are in development.
>
> * MIT licensed, no paid tier, no analytics or tracking
> * **I use AI coding tools heavily**; every app has tests in CI, and the security page says what is and isn't proven
> * What each app protects, and what it doesn't: [https://busnes.app/security.html](https://busnes.app/security.html)
> * Repos: [https://github.com/Busnes-app](https://github.com/Busnes-app)
> * Questions: [https://github.com/Busnes-app/.github/discussions](https://github.com/Busnes-app/.github/discussions)
>
> Comment or DM if you're up for it, or just open an issue on whichever repo broke. Launch is planned for Mid November.
>
> Honestly Statement: AI was used heavily in the creation of these applications.  All applications were written to support open standards including SMTP, IMAP, WebDAV, CalDAV, CardDAV, GPG using existing libraries wherever possible.

---

> **Freeuser001**（-1 分） · 2026-10-30T09:28:53+08:00　
> Hi everyone! I'm one of the developers behind Kryspal Media.
>
> We're a small team of movie and TV nerds who ran Jellyfin and Emby at home for years. We love browsing our collections as a wall of posters, but as our libraries grew, UI performance tanked and we kept reaching for external tools just to handle the basics. So we built the server we wanted for ourselves: fast on massive libraries, and drop-in compatible with the third-party client apps people already use with Emby and Jellyfin.
>
> **Upfront disclaimer: The core server is closed source, and the free tier is fully usable without artificial nag screens.**
>
> **Project Name:** Kryspal Media
>
> **Status:** Production-ready, under active development (v0.9.13)
>
> **Repo/Website Link:** [Official Site & Docs](https://media.kryspal.net/) · [GitHub Repo](https://github.com/kryspal/kryspal-media) (for issues, discussions, and open-source plugins; the core server is closed source) · [Live Demo](https://demo.kryspal.net/?lang=en) (no signup required)
>
> **Description:** A high-performance self-hosted media server built for large libraries.
>
> - **Massive libraries stay fast:** Backed by PostgreSQL. Browsing, sorting, and filtering a real library of ~200,000 titles is up to 30× faster than Emby.*
> - **Your favorite players already work:** Drop-in compatibility with Infuse, SenPlayer, VidHub, and other third-party clients built for
> Emby or Jellyfin.
> - **Migrate from Emby or Jellyfin:** Import your existing libraries, users, metadata, and watch history.
>
> **Source & Licensing:**
> - **Closed source core:** The server itself is closedugin SDK (Apache-2.0) and several official plugins are open on GitHub.
> - **Truly usable Free Tier:** No license key, no onliits. Includes 3 users, 6 devices, and 3 concurrentstreams, complete with the web player, 3rd-party client support, Emby/Jellyfin migration, WebDAV libraries, and webhooks. For a standard
> home setup, the free tier is the whole product.
> - **Optional PRO & MAX tiers:** Built for larger households and power users. Unlocks more users/devices/streams, plus extras like
> intro/outro skipping, subtitle downloads, parental coinks to your own cloud storage. Lifetime licenses are$99 (PRO) and $119 (MAX). You can grab a 14-day PRO trial on the site with just an email.
>
> *Benchmark note: Measured on the same NAS against Emby 4.10 using a real library of ~200,000 titles (browsing, sorting, and
> filtering only; search excluded).
>
> **Deployment:**
> Available as multi-arch Docker images (`x86_64` and `ARM64`) on [Docker Hub](https://hub.docker.com/r/kryspal/kryspalmedia). It runs as
> a clean two-container stack (Kryspal Server + Postgremum 2 GB RAM (4 GB recommended).
>
> You can grab the standard `docker-compose.yml` from o//media.kryspal.net/docs/install/), or spin it upusing our helper script (which simply generates the compose file and starts the stack; feel free to inspect the script first):
>
>     curl -fsSL https://media.kryspal.net/install.sh | bash -s -- --media /path/to/media
>
> **AI Involvement:** AI assistants write most of the code; we design it, review it and test it, and we dogfood it daily on our own hservers.
>                                                                                                                                    ---
>                                                                                                                                    **What we'd love feedback on:**
> We're especially looking for feedback on the installation flow, the Emby/Jellyfin migration tool, and any edge-case bugs with your favorite third-party players.
>
> We're also building native mobile clients! If you wanndroid app via Google Play's closed beta, you can join here: [Kryspal Android Testers Group](https://groups.google.com/g/kryspal-android-testers).

---

> **Key_Pace_2496**（1 分） · 2026-10-30T09:31:19+08:00　
> Just what the slop machine needed, more automation!

---

> **Key_Pace_2496**（3 分） · 2026-10-30T09:35:25+08:00　
> Bruh, when you read a book the visualization happens in your head lmao.

---

> **codectl**（0 分） · 2026-10-30T09:43:50+08:00　
> The platform incentives around short-form media aren't going away, but right now creators either have to pay expensive cloud SaaS tools or spend hours on repetitive editing just to distribute their own work.
>
> Reelsaw is open-source, local-first software meant to automate the tedious post-production mechanics for human-made content, not turn out synthetic AI filler.

---

> **RealSirJoe**（4 分） · 2026-10-30T09:44:17+08:00　
> **Project Name:** Relinos
>
> **Description:** An open-source, self-hosted web scraping API.
>
> Relinos uses real browsers, allowing it to render JavaScript-heavy websites, perform interactions, and handle challenging websites that simpler scrapers struggle with.
>
> Some of its features:
>
> * **Browser automation:** Navigate websites, click elements, fill forms, scroll, and interact with pages.
> * **Concurrent execution:** Run multiple browser sessions and scraping requests concurrently.
> * **Structured data extraction:** Extract data using new format "xpathschema" and return structured JSON.
> * **Reusable interactions:** Save, import, export, and share browser routines and extractions.
> * **Self-hosted:** Run everything locally, with no external scraping service required.
> * **Language-independent:** Control everything through a simple HTTP API.
>
> I've also included several ready-to-use demonstration routines for Google Search, Google Maps, YouTube, DuckDuckGo, eBay, and Skyscanner.
>
> Relinos is built with Python and PyDoll.
>
> I'm currently looking for feedback from developers who work with web scraping or browser automation. I'd be particularly interested in hearing about limitations, missing features, or practical use cases.
>
> GitHub: [https://github.com/realsirjoe/relinos](https://github.com/realsirjoe/relinos)
>
> **Deployment:** Linux or OSX ( install script )
>
> **AI Involvement:** None

---

> **DMeschiari**（1 分） · 2026-10-30T10:05:48+08:00　
> **Project Name**: CineLocal
>
> **Repo/Website Link**: [https://github.com/odanielmeschiari/cinelocal](https://github.com/odanielmeschiari/cinelocal)
>
> **Description:**
>
> CineLocal is a free, ad-free desktop app to organize and watch your personal movie and series collection. It is offline-first: the internet is only used to download posters and metadata for new titles (and subtitles, if you set an OpenSubtitles key).
>
> To get started, just select your collection folder and add your free TMDB API key so it can fetch the metadata. Features include:
>
> \- A fast, clean poster grid to browse your library, with adjustable poster size
>
> \- Automatic TMDB-based filters (genres, years, etc.), filtered/advanced search and sorting
>
> \- Favorites, watchlist and custom lists/collections
>
> \- Built-in player (libVLC) with "Continue watching"
>
> \- A "For you" section, added recently, with personalized recommendations based on the movies you liked, added to your watchlist and rated
>
> The goal is to give you a streaming experience for the files you already own, without accounts, subscriptions or cloud services.
>
> **Deployment:**
>
> It is a desktop app (so no Docker/self-hosting needed). It is released and ready to download for Linux and Windows:
>
> \- **Windows 10/11**: installer (\`.exe\`) or portable \`.zip\`
>
> \- **Linux (Mint/Ubuntu/Debian x86\_64):** \`.deb\` or portable \`.tar.gz\`
>
> The built-in player is already included, so no Python or VLC installation is required. Installation steps, uninstall instructions and a full usage guide are in the README: [https://github.com/odanielmeschiari/cinelocal](https://github.com/odanielmeschiari/cinelocal) (releases are under the "Releases" page).
>
> **AI Involvement**: I wrote the core of the app myself, all the design patterns, ideas, organization, improvements, and used AI to implement.
>
> I'm posting here to get real-world feedback. If you try it, I'd love to hear any bugs, suggestions or feature ideas, and I'll gladly work on them. I'm also considering making the project open source if the community is interested.
>
> https://i.redd.it/m8pohf7tiiyh1.png

---

> **ramair02**（3 分） · 2026-10-30T10:19:17+08:00　
> https://i.redd.it/3h9pez15liyh1.png
>
> If you keep YouTube channels in Plex (Pinchflat, ytdl-sub, TubeArchivist etc.), you know the poster situation is rough. YouTube doesn’t have posters. Channels have a square avatar and a super-wide banner, and neither fits Plex’s 2:3 poster shape. You end up with stretched avatars, random video thumbnails, or nothing at all, and every show in the library looks different.
>
> So I built YouTube Poster Creator. Paste a channel link and it gives you a movie-style poster in one consistent house style, so the whole library looks like a set (screenshot above is my actual library).
>
> How it works
>
> * Reads the channel. It pulls the channel’s description and its recent and most-viewed videos from the YouTube API. If the channel is already in your Plex library, it also reads your episode titles. Gemini (with Google Search) writes:
>    * a short category;
>    * a one-line tagline that says what the channel actually is, not “Reviews. Tests. Adventures.”;
>    * a 2–3 sentence summary for Plex;
>    * an accent colour that matches the channel’s branding.
> * Paints a background with no text. The AI only makes the artwork, a cinematic film-still look that uses the channel’s popular videos for subject and mood. Image models are bad at text (typos, random fonts, weird borders), so they never touch the words.
> * Sets the type. Name, category, tagline and colour go on through a fixed template (Anton + Oswald fonts), rendered at 1000×1500. Every poster gets identical layout and typography, and long names shrink to fit.
> * Sends it to Plex (optional). One click uploads the poster to the matching show, can set the summary too, and locks both so a metadata refresh doesn’t undo them. It saves your old poster first.
>
> You can edit any of the text and re-render instantly for free, ask for new artwork with your own scene description, or upload your own photos. I used shots of my car on track for my own channel.
>
> How it was made
>
> The first version was built with Gemini. This latest version was built with Claude (Claude Code). Claude fixed the original after Google retired the image model it used, then redesigned it around the “AI paints, template types” approach and added the Plex integration. It also wrote the documentation.
>
> Setup
>
> * Runs as a Docker container (Next.js, with headless Chromium inside for rendering). docker compose up -d --build and open port 3002.
> * You need a YouTube Data API key (free) and a Gemini API key. Image generation needs a paid Gemini tier, but it’s one image per poster, and editing text afterwards costs nothing.
> * Plex URL + token are optional; without them it just makes posters you can download.
> * There’s also a pair of Python batch scripts if you want to do a whole library at once and review a contact sheet before uploading.
>
> Things to know
>
> * There’s no login, so keep it on your LAN or behind your reverse proxy’s auth.
> * No real faces: people only show up as silhouettes or from behind. That’s deliberate, both to avoid weird likenesses and to keep the set consistent.
> * The AI writes the summaries but is told never to guess host names. Still give them a quick read before sending to Plex.
> * It’s for personal libraries. The channel names and content belong to their creators.
>
> Repo + docs: [https://github.com/ramair02/youtube-poster-creator](https://github.com/ramair02/youtube-poster-creator)
>
> AI was used in three ways:
>
> Building the code: I didn’t hand-write this app.
>
> * Version 1: built earlier this year with Google’s Gemini (via Antigravity).
> * Version 2 (this one): built with Claude Code. Claude wrote and fixed the code, including the redesign, the Plex upload, the batch scripts and the docs in the repo.
> * My part: I decided what it should do and how the posters should look. I tested it on my own library and reviewed every poster before it went into Plex. That’s the library in the screenshot.
>
> What the app does with AI when it runs: it calls Google’s Gemini API with your own key to:
>
> * write each channel’s category, tagline and summary from the channel’s YouTube data;
> * paint the background art.
>
> The AI never draws any text. All the words are added by a fixed template, so the posters stay consistent and free of typos. Everything else is ordinary code, including the YouTube and Plex calls, the layout and the rendering.
>
> This post: drafted with Claude’s help, then edited by me.
>
> It’s free and open source, with no paid tier or tracking.

---

> **CosmicThing2**（2 分） · 2026-10-30T10:23:09+08:00　
> **Project Name:** Pinchtube
> **Repo:** [https://github.com/CosmicThing2/PinchTub](https://github.com/CosmicThing2/PinchTube)e
>
> **Description:** Host your own YouTube - Pinchflat + Pinchtube
> **AI Involvement:** Claude Code Opus 5.5 was used for developing the project.
>
> (Sorry posted last week too but it was right at the end of the week)
>
> Hello all, after many years of frustration with YouTube and getting further and further into self hosting, I decided to create my own replacement! I've been using Pinchflat for a while and it works great to download YouTube content, but the question then becomes how to actually display and browse all those videos you've got.
>
> For a year now I've been just using Jellyfin. I love Jellyfin and use it for my Movies, Series and Music so it seemed a natural fit. However I've found that YouTube content just doesn't really work well and it kept frustrating me. Some channels upload very frequently, daily or more, and many have gigantic descriptions which quickly becomes a mess. Navigating through all the folders and channels one by one to find videos is also annoying especially on a phone. I ended up spending time writing scripts to try and sort the formatting, descriptions, move videos around etc, just so I could browse them easily in Jellyfin.
>
> So I decided to create my own solution! Pinchtube works alongside Pinchflat (or Pinchflat-NGX) to display all your downloaded videos in a very familiar interface! It has all the features you'd expect and works exactly as you're used to.
>
> * No ads, no algorithm telling you what to watch, no social media rubbish, no arguments in the comments
> * Customisable home page, move rows around or disable them, each channel can be controlled moved or toggled, dark and light modes
> * Playlists, play queue, theater mode, sponsorblock marking or skipping, multiple users with permission access to different channels
> * Quality and transcoding from 4k down to 360p and also an Audio-only mode for saving your mobile data (great for listening to a queue in the car)
> * Designed for desktop or phone use, layout should be immediately familiar
>
> This is a first release and I'm actively looking for feedback and improvements. Especially on Nvidia and Intel platforms as I can't test on those. Tell me what you like, what you dislike, be kind! Please see the Github for more information and the docker compose file: [https://github.com/CosmicThing2/PinchTube](https://github.com/CosmicThing2/PinchTube)
>
> (Note that while Pinchflat isn't technically required, you need to set up the paths/permissions/files correctly, I wouldn't recommend doing it all manually although it is possible!)
>
> Thank you!
>
> https://i.redd.it/lkepdz5lliyh1.png

---

> **CosmicThing2**（2 分） · 2026-10-30T10:26:03+08:00　
> I like it, looks clean! Will give it a go thanks

---

> **Parrotman805**（2 分） · 2026-10-30T11:45:25+08:00　
> **Project Name:** Tagarr
>
> **Repo/Website Link:** [https://github.com/OwenWright8/tagarr](https://github.com/OwenWright8/tagarr)
>
> **Description:**
>
> me, my gf and my brother share one jellyfin library. i didnt want to see her shows and she didnt want to see mine, but some stuff we both watch so that needs to show for both of us. i was doing it with jellyfin tags + parental controls but tagging by hand was a pain and stuff kept getting missed, then it just doesnt show up for anyone
>
> tagarr connects to jellyfin and seerr and does the tagging for you:
>
> * whatever you request in seerr gets tagged with your name when it shows up in jellyfin
> * if 2 people request the same thing it gets both tags so it shows for both
> * shows everything thats untagged so nothing gets lost, plus an optional rule to auto assign stuff nobody requested
> * suggests tags based on what people have actually watched
> * sets each jellyfin user to only see their own tag right from the app (and warns you if someone can still see everything)
> * seasonal stuff, like halloween movies only show oct 1 to nov 1 then hide again. it can keep a jellyfin collection for them that hides too, with your own cover
> * puts back tags if a metadata refresh wipes them
> * homepage (gethomepage) widget
> * tells you in the app when theres an update
>
> if you already tag stuff by hand it picks up your existing tags, it doesnt mess with them
>
> **Deployment:**
>
> one docker container, amd64 + arm64 (works on a pi). image is on ghcr
>
>     services:
>       tagarr:
>         image: ghcr.io/owenwright8/tagarr:latest
>         container_name: tagarr
>         restart: unless-stopped
>         volumes:
>           - tagarr-data:/data
>         ports:
>           - "8686:8686"
>
>     volumes:
>       tagarr-data:
>
> then `docker compose up -d`, open port 8686 and the setup walks you through connecting jellyfin + seerr and adding people. the readme has the full setup, how the hiding works, updating, backups and a faq
>
> needs jellyfin 10.9+ for the “allow items with tags” setting. seerr is optional but its what makes requests tag themselves
>
> **AI Involvement:**
>
> most of the code was written by claude (claude code), with me directing it, testing it on my own server and reporting bugs back. it has automated tests and ci, but its still new and has mostly only run on my setup, so there might be bugs on setups different from mine. issues and feedback welcome

---

> **dellarb**（4 分） · 2026-10-30T11:59:26+08:00　
> **Project Name:** Mammoth Mail
>
> **Repo:** [**https://github.com/dellarb/mammothmail**](https://github.com/dellarb/mammothmail)
>
> **Description:** Self hosted email for agents & automations - BYO domain or connectors for Gmail, Outlook & IMAP inboxes.
>
> **Human approved sending** option - Give agents Assistant permission API key and they can read and draft emails but sending triggers a notice to you the human to review and click approve before the email is sent (enforced in code not prompting).
>
> Fully integrated **Hermes Agent connector**  \- just 5 lines of variables in your Hermes agent .env to add real-time email delivery and email based chat with Hermes agent (no more polling or imap). Experimental openclaw connector in development to do the same.
>
> https://i.redd.it/txwy7xg31jyh1.png
>
> Broad provider support - *Receive via:* direct SMTP to port 25, Cloudflare, Mailgun, Postmark, Resend or zero account setup MX relay option via Tusk MX. *Send via:* Direct MX, SMTP, Brevo, Mailgun, Resend.
>
> *Recommended config for own domain is; send via Brevo (free tier 300 emails a day) receive via Cloudflare if you are happy exposing inbound ports, or Tusk MX (free relay by me) if you prefer to not have ports facing public internet.*
>
> **Deployment:** Single docker container image on GHCR with docker compose quickstart in readme. AGPL-3.0
>
> **AI Involvement:** I design the architecture, features and workflows, with extensive use of AI coding agents for implementation and testing.
>
> I'd particularly appreciate feedback from anyone running self-hosted agents or email automations. Interested in what integrations or controls people would actually find useful.

---

> **swottuzees80**（1 分） · 2026-10-30T12:32:14+08:00　
> when a conflict comes up, does it let you merge individual fields or do you just pick which version of the whole vCard to keep

---

> **antonreshetov**（5 分） · 2026-10-30T12:35:17+08:00　
> **Project Name:** Torsher
> **Repo/Website Link:** [https://github.com/torsher-app/torsher](https://github.com/torsher-app/torsher) · [https://torsher.app](https://torsher.app)
>
> https://i.redd.it/4iwh1jx3ajyh1.jpeg
>
> **Description:** A self-hosted media center that starts from the TV. Wiring up Jellyfin and the \*arr apps took me a lot of evenings: API keys, paths that have to match inside every container, download categories, five interfaces. Torsher is one container that does the downloading, the library and the TV interface itself.
>
> * TV showcase with a TMDB catalog, profiles and remote navigation; apps for LG webOS and Android TV, or any browser
> * Playback starts while the file downloads, only a few minutes ahead ([how that works](https://dev.to/antonreshetov/playing-a-torrent-while-it-downloads-how-i-got-start-time-from-41-s-to-8-s-hlc))
> * A library Jellyfin, Plex and Kodi can read too; folders you already have are added read-only
> * Follow a series and new episodes arrive on their own
> * On-the-fly transcoding (VAAPI, NVENC or CPU) when a TV can't play a file
> * Any Torznab indexer, for example Prowlarr or Jackett; no content and no sources included
> * AGPL-3.0, no telemetry
>
> **Deployment:** One Docker image for amd64 and arm64: `ghcr.io/torsher-app/torsher` (also `torsherapp/torsher` on Docker Hub). A `docker-compose.yml` comes with every release, and there's an Unraid Community Applications template. Install guide: [https://torsher.app/docs/install/docker-compose](https://torsher.app/docs/install/docker-compose). The TV apps (LG `.ipk`, Android TV `.apk`) are in the [release](https://github.com/torsher-app/torsher/releases/latest).
>
> **AI Involvement:** I use AI tools while building it, like most developers now. I design it, review every change and test it on real hardware: an N150 mini PC and an LG C4.
>
> I'm looking for people with NAS boxes, ARM boards, older LG TVs and real Android TV devices to tell me what breaks.

---

> **yonto_player**（1 分） · 2026-10-30T12:42:06+08:00　
> Project Name: Yonto Player
>
> Repo/Website Link: https://player.yonto.app (closed-source apps, the plugin SDK is MIT: https://github.com/yonto-app/yonto-player-plugins)
>
> Description: An Android TV / Google TV (and Android phone) player for the stuff you already host. It plays from Jellyfin, Plex and Emby, or straight from an SMB / WebDAV share or a USB drive with no media server at all, and builds a poster library from the file names. You set a server up by scanning a QR code with your phone instead of typing on the remote. It handles DTS/TrueHD, Blu-ray/DVD ISOs, skip intro/credits, and casting. It's a client, so it provides no content. Free with one source, Pro is a one-time payment, no account, no ads.
>
> Deployment: It's an app, not a server, so there's nothing to host. Install the APK through the Downloader app with code 9188303 (or player.yonto.app/tv), docs at player.yonto.app/docs. There's a built-in demo library of open films so you can try it before adding anything.
>
> AI Involvement: Yes, quite a lot. It's built solo with AI coding tools, and this comment was drafted with AI help too. Happy to answer anything about how, and I'd really like to know what's missing for your setup.

---

> **satyajugran**（2 分） · 2026-10-30T13:08:36+08:00　
> **Project Name:** NodeStack
>
> **Repo/Website Link:**
>
> * GitHub: [https://github.com/satya-jugran/nodestack](https://github.com/satya-jugran/nodestack)
> * Documentation: [https://satya-jugran.github.io/nodestack/](https://satya-jugran.github.io/nodestack/)
> * License: MIT (100% Free & Open Source)
>
> **Screenshots & Previews:**
>
> * [Admin Dashboard UI](https://github.com/user-attachments/assets/46aec2a7-b6ad-4cda-be3c-785a2f7f6e5d)
> * [Architectural Comparison Matrix (NodeStack vs PocketBase vs Supabase)](https://raw.githubusercontent.com/satya-jugran/nodestack/master/assets/comparison-matrix.png)
> * [20-Second Demo Preview Video](https://github.com/user-attachments/assets/70eb11fa-9b68-4eb6-930d-ac367ebc4565)
>
> https://i.redd.it/7wwdy6wnfkyh1.png
>
> **Description:**
> NodeStack is a self-hosted, single-process backend platform designed for minimal-resource servers (\~40–80 MB idle RAM on a $5 VPS or Raspberry Pi) with zero external database daemons, no Python/C++ build dependencies, and no Docker required.
>
> *Problem it solves:*
> PocketBase is beloved in the self-hosted community for single-process simplicity, but writing custom lifecycle hooks or business logic requires writing Go. NodeStack brings that same single-process architecture to **TypeScript and Node 24 LTS**, allowing you to write hooks and extensions with full access to the npm ecosystem.
>
> *Key Features:*
>
> * **Instant REST CRUD & SSE Realtime**: Auto-generated REST endpoints and Server-Sent Events change streams.
> * **Atomic Snapshots & Rollbacks:** Create point-in-time schema/data checkpoints with drift detection.
> * **Zero-Compilation Embedded SQLite**: WAL mode powered by Node 24's native `node:sqlite`.
> * **Native SQLite FTS5 Full-Text Search**: Built-in BM25 relevance scoring and snippet excerpts.
> * **Safe Serverless Lambdas:** Isolated QuickJS-Wasm runtime with an Anti-SSRF network firewall and built-in CodeMirror web IDE.
> * **Live HTTP TypeScript Generator:** Zero-config end-to-end types via `GET /_/types.d.ts` or CLI typegen.
> * **Single-Process Multi-Application Platform**: Host unlimited isolated tenant applications within a single running process.
> * **Auth & Storage**: JWT, OAuth2 PKCE (Apple/Google/GitHub), and multipart file uploads.
> * **Interactive OpenAPI Docs:** Automatic interactive API testing playground via Scalar & Swagger at `/_/docs`.
>
> **Deployment:**
> NodeStack is released, published on npm, and ready for deployment:
>
> *Instant CLI (No clone / zero install)*:
>
>     npx @nodestackapp/server start
>
> Others ways:
>
> 1. Production Dockerfile: Multi-stage Alpine build included in repo.
> 2. *Pre-compiled Standalone Binaries*: Windows, Linux, and macOS standalone executables available on GitHub Releases (upcoming release).
> 3. *1-Click Cloud Previews*: Available for GitHub Codespaces and Railway.
>
> **AI Involvement:**
> Core architecture, single-process system design, and database schema implementation authored by developer. LLM tooling was utilized as a pair-programmer for unit testing coverage, TypeScript type inference, and documentation formatting.

---

> **meow-thai**（3 分） · 2026-10-30T14:03:41+08:00　
> **Project:** Community Cloud
> **Github:** [https://github.com/Mellow-Technology/community-cloud](https://github.com/Mellow-Technology/community-cloud)
> **Website:** [https://community-cloud.technology](https://community-cloud.technology)
>
> **Description:** I'm a long time engineer and infrastructure person and I've always had one gripe with running things, is that it's either on the expensive side with cloud services or an absolute drag to run our own services. For that I created Community Cloud, it's a minimal Kubernetes distribution that makes it easy to run anything you like on any hardware that you have available.
>
> We have a built-in operator (Cirrus) that can automatically pull updated containers from Gitlab, and a built-in interface (Meteorologist) for managing all of the built in features. We're also bundling software that can be used to run your next vibe-coded app business or any project you might have going.
>
> **Deployment:** We have an easy to use command line installer that installs Kubernetes, configures everything including networking, storage, and everything else needed to run. All that's needed is a computer (or set of computers) running Debian flavored Linux distros.
>
> **AI Involvement:** I'm a long time engineer, Claude writes a lot of the code but all of the architecture, patterns, and ideas are mine. I read through everything and have a deep understanding of how everything works and fits together.

---

> **YkGxPu6AI3iLRxGsOyub**（2 分） · 2026-10-30T14:36:38+08:00　
> Looks great. I really love the library + "streamio" functionally in one app.
> I have almost the same setup as you but my family is Apple TV junkies. However I can sideload from FlareStore if you ever run into trouble releasing in on App Store.
>
> Following your project!

---

> **antonreshetov**（1 分） · 2026-10-30T14:44:52+08:00　
> Thanks. Apple TV is planned: the idea is that Torsher answers as a Jellyfin-compatible server, so Swiftfin and Infuse work with it as they are. Until then the player can hand you a direct link to the file, and Infuse opens it as a network stream: [https://torsher.app/docs/tv/other-devices](https://torsher.app/docs/tv/other-devices)
>
> Noted on FlareStore, good to know there's a way around the App Store if it ever comes to that.

---

> **hillel369**（1 分） · 2026-10-30T15:02:38+08:00　
> **Stackapella**: a web app for learning and recording vocal harmony, now self-hostable
>
> * **What it is:** learn one part of a song with a guide voice, then record each part over the others until you've sung every voice yourself. Courses from a first note to four-part harmony, and choir groups.
> * **Repo:** [https://github.com/stackapella/stackapella](https://github.com/stackapella/stackapella) (Attribution Assurance License)
> * **Self-hosting guide:** [https://stackapella.com/selfhost?ref=reddit-selfhosted](https://stackapella.com/selfhost?ref=reddit-selfhosted), and DEVELOPING.md in the repo for the full setup.
> * **What it needs:**
>    * PHP 8.3 or 8.4 with Composer, and MySQL 8.4 (MySQL only);
>    * ffmpeg;
>    * HTTPS, since the browser only gives the microphone to a secure page;
>    * S3-compatible storage (Spaces, S3, R2 or MinIO);
>    * mail;
>    * two background processes, the scheduler and a worker.
> * Our own site runs on 1 vCPU and 1 GB for the web.
> * **What you get with SELF\_HOSTED=true:**
>    * every paid feature for every account, with no licence key and no plans;
>    * your own legal pages and contact addresses;
>    * `php artisan app:doctor`, which checks your setup and says how to fix what's wrong.
> * **What isn't included:**
>    * the recorded singers' voices (your guides use the synthesized voice);
>    * the native apps;
>    * the marketing site.
> * The songs and courses are CC BY-SA 4.0, in their own repo, and the install fetches them with one command.
> * **What it phones home:** nothing. There's no analytics and no licence check. Your server only talks to your storage, your mail, and any optional service you add keys for.
> * **AI involvement:** built with AI coding agents, with every change reviewed and tested by me.

---

> **Protectator**（1 分） · 2026-10-30T15:59:23+08:00　
> Today it works a bit differently: in simple cases, like editing a phone number while another client adds a birthday, Natel can keep both changes. That requires confirmation, but those independent changes could be merged automatically. We'd only  ask you to intervene when we can't safely combine the edits.
>
> As for choosing which changes to keep in more complicated cases, I've tried a few ways to let you accept individual edits and discard others, but none felt as intuitive as just editing the final values directly in the form. So that's what I've kept for now. I may revisit this in the future.

---

> **ClassyLion**（1 分） · 2026-10-30T16:06:27+08:00　
> **Project Name:** momentarr
>
> **Repo:** [https://github.com/drumandbytes/momentarr](https://github.com/drumandbytes/momentarr)
>
> **Description:** A caching, serialising proxy that sits in front of FlareSolverr/Byparr. If your Prowlarr indexers are behind Cloudflare, every search launches a browser to re-solve the challenge even though the `cf_clearance` cookie from the last solve is still valid. With a few indexers that means slow searches and an OOM-killed solver. momentarr speaks the same `/v1` API, so Prowlarr just points at it instead of the solver.
>
> * Reuses the clearance cookie per site and replays it over plain HTTP. Measured on my setup: repeat requests went from 6-13 s to \~0.1 s.
> * Queues solves so only one browser runs at a time (`BACKEND_CONCURRENCY`, default 1). A burst of searches against one site costs a single solve.
> * Works with Byparr, FlareSolverr or whatever solver comes next: swap `BACKEND_URL`.
>
> Limits: it must share the solver’s egress IP, and sites that bind the clearance to the browser’s TLS fingerprint still need a solve every time (you keep the queue, not the speed-up). The README has the measurements and a “when it doesn’t help” section.
>
> **Deployment:** Docker image [`ghcr.io/drumandbytes/momentarr`](http://ghcr.io/drumandbytes/momentarr) (static Go binary, `FROM scratch`, \~10 MB, runs as UID 1000, read-only root fs OK). Easiest is to share the solver’s network namespace so they have the same IP:
>
>     services:
>       byparr:
>         image: ghcr.io/thephaseless/byparr:latest
>         environment:
>           PORT: "8192"
>         ports:
>           - "8191:8191"   # momentarr's port, published here
>       momentarr:
>         image: ghcr.io/drumandbytes/momentarr:latest
>         network_mode: "service:byparr"
>         environment:
>           BACKEND_URL: http://127.0.0.1:8192
>
> Then point Prowlarr’s FlareSolverr proxy at `http://<host>:8191` and set its request timeout to \~120 s. On Unraid it’s in Community Apps (search “momentarr”; set Backend URL to your solver’s IP:port). Go, stdlib only, MIT.
>
> **AI Involvement:** Built with an AI coding assistant (Claude). I designed it, review every change and test it, and it runs in my own homelab behind Prowlarr.

---

> **anitamaxwynnn69**（1 分） · 2026-10-30T16:17:11+08:00　
> **Project Name:** [www.overtchat.com](http://www.overtchat.com/)
>
> **Repo/Website Link:** [https://github.com/yoloyash/overtchat](https://github.com/yoloyash/overtchat)
>
> **Description:** A lightweight self-hosted chat client, alt to Open WebUI. I built it because my partner and family use ChatGPT but don't care about privacy. I already self-host vLLM on 8x 3090s and wanted a polished, private alternative they could actually use. OWUI is too heavy and complex for non-technical users. overtchat is chat-first with built in tts/stt/search, no rag/plugins/agentic bloat, no external api keys. Free native [Android](https://play.google.com/store/apps/details?id=com.overtchat.mobile) and [iOS](https://apps.apple.com/app/overtchat/id6812165221) Apps, plus a [desktop app](https://github.com/yoloyash/overtchat/releases/tag/desktop-v0.2.0) for macOS (Apple Silicon/Intel) and Linux (AppImage/Deb/RPM). MIT licensed, no telemetry, no analytics.Also supports AI agents now (codex/claude code/omp)
>
> **Deployment:** curl -fsSL [https://overtchat.com/install](https://overtchat.com/install) | sh
>
> **AI Involvement:** Yes, definitely vibe coded.
>
> Would love to have some feedback :)

---

> **HSinghHira**（1 分） · 2026-10-30T17:00:18+08:00　
> Love it. I have already created an app for Zima OS, Casa OS & Homeio

---

> **YkGxPu6AI3iLRxGsOyub**（1 分） · 2026-10-30T17:00:50+08:00　
> Thats great to hear. Jellyfin + Infuse is my current setup but it's extremly appealin to just 'press play' into something you want to watch.

---

> **CatalinMihaiSafta**（2 分） · 2026-10-30T17:16:26+08:00　
> https://i.redd.it/5t8fdfjerkyh1.png
>
> **Project Name:** LCARS
>
> **Repo/Demo/Blog Link:** [Repo](https://github.com/saftacatalinmihai/lcars) , [Demo](https://public.mihai-safta.dev/lcars-demo/index.html) , [Blog post](https://blog.mihaisafta.com/posts/lcars_journal/?utm_source=reddit&utm_medium=social&utm_campaign=lcars_journal&utm_content=r_selfhosted)
>
> **Description:** A self-hosted personal journal inspired by the Star Trek LCARS computer interface.
> One static binary (Linux x86\_64/arm64), one SQLite file, \`lcars init\` and run. A web console, a CLI, CalDAV for tasks, import/export from other notes apps, and a walkable 3D ship to pin jounral entries on walls and much more. MIT. Demo in the browser on made-up data.
>
> **AI Involvement:** Yes on the frontend - full vibe coded, not on the backend (not as much). Built with AI agents (Claude Code).

---

> **ZookeepergameLevel73**（2 分） · 2026-10-30T17:46:14+08:00　
> **Project** **Name**: Scrollback
>
> **Repo/Website Link**: https://github.com/ppolydoras/scrollback (browser demo: https://ppolydoras.github.io/scrollback/)
>
> **Description**: A feed shaped like social media where every post is a real historical event from Wikipedia's "On this day" pages. It replaces some scrolling with something you learn from. Full-screen posts, likes, saves, a daily streak and quizzes on what you read. It learns which eras and topics you stay on. It reads posts aloud with Piper, fully offline, with a hands-free mode. One user, no accounts, no telemetry.
>
> **Deployment**: Docker image for amd64 and arm64 (ghcr.io/ppolydoras/scrollback) and a compose file in the repo. Install and Docker instructions are in the README. Everything lives in one SQLite file in a volume. You can also run it with plain Python 3.10+ and no dependencies. There is no login, so keep it on your LAN and set SCROLLBACK\_ALLOWED\_HOSTS to the name you reach it by.
>
> **AI Involvement**: Most of the code was written with Claude. I decided the features and the design. I use it daily. The app itself uses no AI unless you switch on the optional storyteller (Claude, OpenAI or a local model through Ollama).

---

> **cappuccin000**（3 分） · 2026-10-30T17:54:44+08:00　
> **Project Name:** claude-relay
>
> **Repo/Website Link:** [https://github.com/anandhakrishnanaji/claude-relay](https://github.com/anandhakrishnanaji/claude-relay) (write-up: [https://www.anandhakris.com/posts/introducing-claude-relay/](https://www.anandhakris.com/posts/introducing-claude-relay/))
>
> **Description:** A small FastAPI server that runs Claude Code behind OpenAI and Anthropic compatible endpoints (`/v1/chat/completions` and `/v1/messages`, both streaming). I built it to test my own OpenAI/Anthropic SDK apps against a real model on my machine during development: you point the app's base URL at `http://localhost:8000/v1` and it runs unchanged. Your system prompt replaces Claude Code's own, so it behaves like a plain chat model.
>
> Defaults I cared about for self-hosting:
>
> * Claude's Bash/Read/Write tools are off. They only turn on if the server sets `ALLOW_TOOLS=true` *and* the request sends `"enable_tools": true`, so text in a prompt can't run commands on your box.
> * CORS allows no origins, and a Host allow-list blocks DNS rebinding.
> * Requests don't load your `~/.claude` settings, skills or plugins.
> * Auth via Anthropic API key, Bedrock or Vertex. Claude Code's own login also works if it's just you testing your own code locally; the README has a section on what Anthropic's terms allow.
>
> Known limits: no OpenAI function calling, sampling params like temperature are ignored, and it's slower than the raw API since requests go through Claude Code's agent loop.
>
> **Deployment:** Released on PyPI (MIT). Quickest way to run it is `uvx claude-relay-server` (no separate Node install, since the Agent SDK bundles the Claude Code CLI). For running it permanently there's a script that sets it up as a systemd user service, and a Dockerfile that builds a non-root image. Install, config and usage are covered in the README.
>
> **AI Involvement:** Built with heavy help from Claude Code: it wrote a large share of the code and docs, and I designed it, reviewed the changes, and tested it. This post was also drafted with AI help.

---

> **LeadershipCool21**（1 分） · 2026-10-30T18:10:20+08:00　
> **Project Name:** coachd
>
> **Repo/Website Link:** [https://github.com/stefiix92/coachd](https://github.com/stefiix92/coachd)
>
> **Description:** I'm a runner and DevOps engineer, and I got tired of manually feeding my Garmin data into AI conversations and then recreating suggested workouts on my watch. So I built coachd — a self-hosted gateway that connects Garmin to AI agents through MCP.
>
> It pulls activities, sleep, HRV, Body Battery, and other metrics from Garmin, making them accessible to AI clients like Claude, ChatGPT, or local models. Agents can also store training goals, remember context between conversations, and propose structured workouts.
>
> The part I particularly wanted: workouts require my approval via passkey (Face ID/fingerprint) before they're delivered to my Garmin watch. After training, the recorded data is available to the agent for review.
>
> No built-in LLM, no chat UI, no AI subscription required by coachd. Bring your own agent.
>
> Written in Go, SQLite for storage, Docker-based, runs on Raspberry Pi or any Linux server. AGPLv3 licensed.
>
> There's also a demo mode with fictional Garmin data, so you can try it without owning a Garmin or providing an API key.
>
> **Deployment:** Docker Compose — [https://stefiix92.github.io/coachd/docs/install/](https://stefiix92.github.io/coachd/docs/install/)
>
> **Demo:** [https://stefiix92.github.io/coachd/docs/install/demo/](https://stefiix92.github.io/coachd/docs/install/demo/)
>
> **AI Involvement:** The project integrates with AI agents via MCP but doesn't run its own LLM. \[Add a sentence about whether you used AI coding tools during development.\]
>
> Still early and built for my own training, so expect some rough edges. Would love feedback, especially on the architecture, security, and deployment experience.

---

> **pagerwho1**（1 分） · 2026-10-30T18:22:54+08:00　
> https://i.redd.it/kg2aenhezkyh1.png
>
> \*\*Project Name:\*\* PagerWho
>
> \*\*Repo/Website Link:\*\*
>
> \- GitHub: [https://github.com/Pager-Who/PagerWho](https://github.com/Pager-Who/PagerWho)
>
> \- Hosted version: [https://pagerwho.com/](https://pagerwho.com/)
>
> \- Documentation: [https://pagerwho.com/docs](https://pagerwho.com/docs)
>
> \*\*Description:\*\*
>
> PagerWho is an open-source, self-hosted incident response and on-call management platform.
>
> I built it for teams that need alert ingestion, on-call scheduling, and escalation workflows without depending entirely on a hosted incident-management provider.
>
> Current features include:
>
> \- Webhook alert ingestion and deduplication
>
> \- Incident acknowledgement, resolution, and timelines
>
> \- Primary and secondary on-call rotations
>
> \- Temporary on-call overrides
>
> \- Multi-step escalation policies
>
> \- Slack, email, SMS, and phone notifications
>
> \- Event-driven workflow automation
>
> \- Project roles, audit logs, and operational diagnostics
>
> \*\*Deployment:\*\*
>
> The complete evaluation stack includes PostgreSQL, migrations, demo data, the API, worker, and web application.
>
> From the repository root:
>
> \`docker compose up --build -d --wait\`
>
> Then open \`http://localhost:8080\` and use the demo credentials in the README.
>
> The seeded project includes a service, on-call rotations, an escalation policy, and incidents in multiple states, so the UI is not empty on first launch.
>
> The root Compose stack is intended for local evaluation. Separate production deployment documentation is included in the repository.
>
> \*\*AI Involvement:\*\*
>
> AI-assisted tools were used during development for implementation, testing, documentation, and code review. I reviewed and validated the resulting changes, and the repository includes linting, type checks, unit tests, integration checks, and Playwright end-to-end tests in CI.
>
> This is an early release, so I would especially appreciate feedback on the Docker setup, self-hosting documentation, missing incident-response features, and anything that would make PagerWho easier to operate.

---

> **Angelsomething**（1 分） · 2026-10-30T19:29:49+08:00　
> **Project Name:** Tally
>
> **Repo/Website Link:** [https://github.com/tinkermesomething/tally](https://github.com/tinkermesomething/tally)
>
> **Description:** Self-hosted personal/household EU/UK focused budget app. I'd been using a spreadsheet for years; tried actual-budget and a couple others, they kept missing the mark for what I actually needed, so I built my own.
>
> OIDC-only auth, multi-user, each account's data in its own encrypted SQLite DB file;  nobody, including an admin, can read another account's data without their key.
>
> https://i.redd.it/pyv3c0kjblyh1.png
>
> **Features:**
>
> * Budget grid: categories (with sub-category rollups) × months, planned vs. actually spent, carries unspent money forward automatically
> * Debt ledger: per-person running balance from loan/repayment entries, not a cell you overwrite by hand
> * Savings buckets with goal tracking, net worth tracking, recurring bills with auto-populate
> * Reports: budgeted vs. spent, trend, variance, exportable to PDF
> * Bank sync via GoCardless Bank Account Data, with CSV import for everything else
> * Optional household view: share specific categories/income into a combined grid without exposing anyone's full account
> * Token-authenticated API for scripts/agents
> * Available (ish) in English, German, French, Italian, Polish, Portuguese - I'm still working on the translation.
>
> **What it isn't, on purpose:**
>
> * EU/UK only for automatic bank sync as GoCardless only reaches the EU/UK Open Banking network. Everywhere else, that's what CSV import is for.
> * Not a business/accounting tool since there is no invoicing, no tax reporting, no double-entry bookkeeping. Personal/household budgeting only.
> * OIDC only, built and tested against pocket-id specifically. Should work with Authentik/Authelia/Keycloak (standard OIDC flow underneath) but unverified.
>
> **Deployment:** Released, Docker-only. One container, pre-built multi-arch image on GHCR. docker-compose example and full setup steps in the README, including the OIDC config and the bootstrap-admin env var. No separate "demo";  self-host it to try it.
>
> **AI Involvement:** Built with Claude Code. I'm a working devops engineer and designed/reviewed/tested every change myself, but the code itself is largely AI-written. I use this daily for my own budget and will keep maintaining it for as long as I do.
>
> This is personal use project and I hope you find it useful :)

---

> **Suspicious_Life_4309**（0 分） · 2026-10-30T19:49:02+08:00　
> **Project Name: FrameBridge 0.3.4**
>
> Hi, I’m Gerardo. I developed FrameBridge with ChatGPT to administer my own home Linux network, and I’m sharing it to get feedback from other homelab users.
>
> **Repo / Website**
>
> * Source: [https://github.com/gerabh1128/framebridge](https://github.com/gerabh1128/framebridge)
> * Website: [https://framebridge.betancourt.one/](https://framebridge.betancourt.one/)
> * Downloads and installation: [https://framebridge.betancourt.one/download/](https://framebridge.betancourt.one/download/)
> * Documentation: [https://framebridge.betancourt.one/docs/](https://framebridge.betancourt.one/docs/)
>
> **Description**
>
> FrameBridge connects a central Linux gateway and enrolled computers to a ChatGPT conversation through MCP. It provides remote command execution, persistent Bash terminals, system and service inspection, and optional graphical control of compatible X11 desktops.
>
> The intended use is one administrator managing computers they own. Network administration is the main purpose; desktop access is an additional tool.
>
> The tools run on your Linux machines, but **ChatGPT remains a cloud service**. Command output and screenshots returned to the conversation are sent through that connection. This is not a fully local AI system.
>
> **Deployment**
>
> Version 0.3.4 is released with native `.deb` packages and signed APT repositories for **Debian 13, Ubuntu 24.04 and Linux Mint 22.x, on amd64**.
>
> Installation uses the package matching your distribution. Connection setup starts with `fb connect` in a normal terminal and requires your own compatible ChatGPT/MCP access, tunnel connection details and manual browser approval. The download page and documentation explain package verification and setup.
>
> I use it on my own physical computers and have tested signed APT upgrades and startup across three corresponding Linux VM profiles. Other distributions, architectures and Wayland graphical control are outside this release’s validated scope.
>
> FrameBridge’s original code is licensed under **GPL-3.0-only**.
>
> **AI Involvement**
>
> ChatGPT was used extensively for programming, tests and documentation, and helped draft this English comment. I supplied the original idea, directed the project and tested it on my equipment. This is an independent project, with no OpenAI endorsement.
>
> I’d welcome feedback on installation, connection reliability, permission boundaries and whether the workflow is useful in your homelab. Questions here are welcome; reproducible problems and suggestions can also go to GitHub Issues:
>
> [https://github.com/gerabh1128/framebridge/issues](https://github.com/gerabh1128/framebridge/issues)

---

> **exoenjoi**（1 分） · 2026-10-30T20:29:58+08:00　
> Happy to share my project I started a few weeks ago !
>
> **Project Name**: Cross-Seed Companion (CSC)
>
> **Repo/Website Link**: [https://github.com/exoenjoi/cross-seed-companion](https://github.com/exoenjoi/cross-seed-companion)
>
> **Description**: [cross-seed](https://www.cross-seed.org/) has no UI. CSC gives it one:
>
> * Indexer sync: pushes your Prowlarr indexers into cross-seed’s config.js, with a diff preview, confirmation and automatic backup. Optionally excludes public trackers or tagged indexers.
> * Actions: one-click cross-seed jobs (search, inject, RSS, cleanup…) and targeted searches by infoHash/path. Custom actions can be defined in YAML.
> * Live logs: real-time log stream with filters and rotated-log history.
> * Added torrents: what cross-seed actually injected, grouped across trackers, with stats.
>
> No SSH, no Docker socket and no shell execution: just HTTP APIs and a bind mount. There’s no built-in auth, so keep it behind an authenticating reverse proxy or on your LAN/VPN.
>
> **Deployment**: Single Docker image on GHCR (ghcr.io/exoenjoi/cross-seed-companion) with a compose example in the repo. It runs on the same host as cross-seed, and config is done via env vars (documented in the README).
>
> **AI Involvement:** Openly AI-assisted, built with Claude Code.
>
> Feedback and code review are welcome.
>
> MIT licensed.

---

> **salihcantekin**（1 分） · 2026-10-30T20:31:38+08:00　
> **Project Name:** Ruvio
>
> **Repo/Website Link:** [https://github.com/salihcantekin/ruvio](https://github.com/salihcantekin/ruvio) · [https://ruviodb.com](https://ruviodb.com)
>
> **Description:** A Redis-protocol key-value server written in Rust. redis-cli and existing clients connect, so apps that want a Redis-style cache or queue can use it. It also has built-in commands for locks, rate limits and delayed jobs, an operator web UI for browsing keys and users, and backups/restores through `ruvio-ctl` It doesn't implement every Redis command, so check the supported list on the site against your app first.
>
> **Deployment:** Docker image for amd64 and arm64, plus release binaries. Persistence is chosen at startup (memory, snapshot, everysec, always).
>
>     docker run --rm -p 6379:6379 -e RUVIO_REQUIREPASS=change-me -e RUVIO_DURABILITY=everysec -v ruvio-data:/data salihcantekin/ruvio:linux
>
> **AI Involvement:** I design and review everything myself; a lot of the code, tests and docs were written with Claude Code, and the repo's [CLAUDE.md](http://CLAUDE.md) shows the rules it works under.

---

> **bitfuzz**（2 分） · 2026-10-30T20:48:01+08:00　
> **Project Name:** Gryffi (Community Edition)
>
> **Repo/Website Link:** [https://github.com/lloydstellar/gryffi](https://github.com/lloydstellar/gryffi) (docs: https://docs.gryffi.com)
>
> https://i.redd.it/6xdymlx3plyh1.png
>
> **Description:**
>
> I'm Erik, a Linux admin from the Netherlands. I ran Linux servers for a Dutch municipality for twenty years and used open source software there wherever I could. I also have ADHD and dyslexia and I have dificulty finishing a boring company handbook: So I built Gryffi!
>
> Gryffi turns manuals, policies and onboarding documents into short journeys: one small step per screen, with a photo of the building, a quiz, a form or a question to an AI guide that answers from your own documents. Participants open a magic link, no account or password. Read-aloud and a dyslexia font are built in, so it also works for colleagues who struggle with long text.
>
> It has run as a hosted SaaS for eight months alreadt on my domain with around 40 companies. This week I finally released the Community Edition: the full product for one organization, AGPL-3.0, no limits on users or journeys etc.
>
> **Deployment:**
>
> What you need:
>
> * Ubuntu 22.04+ or Debian 12+, amd64 or arm64, 2 GB RAM
> * Your own SMTP server for the magic links
> * AI is optional. Any OpenAI-compatible API works, including Ollama or vLLM on your own hardware. Without AI, everything except the AI guides, the journey wizard and translation still works
>
> Install:
>
>       curl -fsSL https://get.gryffi.com | sudo bash
>
> The script shows what it will do before it changes anything. Rather read it first or run it behind your own reverse proxy? The docs cover both. It runs with Docker Compose, the images are on ghcr.io (amd64 and arm64) and the compose.yml is in every release if you want to set it up by hand.
>
> It's version 0.9 of de community edition, so I like to hear if you break it
>
> **AI Involvement:**
>
> I'm a sysadmin, not a full-time developer, and I use Claude to help me with coding. I code myself, but i am not very fast. So it is not fully vibe coded, but also not fully human made only. I test every change myself, it runs in production for over 8 months now and every release goes through automated checks and secret and vulnerability scans. The AI features in Gryffi itself are optional and work with local models too

---

> **GT1030_Swapper**（2 分） · 2026-10-30T21:11:59+08:00　
> * **Project Name:** job application tracker
> * **Repo/Website Link:** [https://github.com/waddington/job-application-tracker](https://github.com/waddington/job-application-tracker)
> * **Description:** A tool for tracking your job applications right from first chats with recruiters whree they mention several roles, all the way through application and offer process. Keep track of calls, interviews, notes, descriptions, links, files, etc. Also get some insights between different resume/CV versions. Keep track of recruiters, who you've messaged, who you're waiting on a reply from, who to chase, etc.
> * **Deployment:** Clone the repo, use \`uv\` to run it as its a python project
> * **AI Involvement:** All vibe coded, but I'm a SWE and I'm actively using this and working through bugs and new features
>
> I'd love some feedback, or contributions! Also would greatly appreciate a star on GH

---

> **OutsideSelect2776**（1 分） · 2026-10-30T21:36:08+08:00　
> **Project Name:** Overlook, a status page for your homelab
>
> **Repo/Website Link:** [https://github.com/bnlqn/overlook](https://github.com/bnlqn/overlook) (MIT).
> Demo with a made-up homelab: [https://bnlqn.github.io/overlook/](https://bnlqn.github.io/overlook/)
>
> Overlook's overview of a made-up homelab: one problem, Standby DNS didn't answer, so Network is degraded; today's figures; and the four areas with their last 30 check results
>
> https://i.redd.it/s6y1o2dwxlyh1.png
>
> **Description:** I wanted one page that tells me whether anything in my homelab is broken. I also wanted it to look a certain way, so I designed it myself. Overlook reads the tools you already run and puts the problems at the top (whatever Gatus or Uptime Kuma is already alerting on), then shows servers, network, storage and apps as up, degraded or down, with a few numbers for today and what happened this week.
>
> It reads 25 tools so far, including Proxmox, Docker, UniFi, AdGuard, Pi-hole, Immich, Jellyfin, Home Assistant and the arrs. It only reads, keeps no database, and the keys never reach the browser. The layout is fixed, so there's nothing to arrange.
>
> I run it on my own setup, a Proxmox box with Home Assistant, Immich, the arrs and the rest, where it reads 15 sources.
>
> **Deployment:** Released, v0.3.0. It's one container, `ghcr.io/bnlqn/overlook`, for amd64 and arm64, or a single binary from the releases if you'd rather run it in an LXC or on a Pi. The README has a compose file and the quick start, and `overlook.example.yaml` shows every source with comments. Keys come from the environment, so the config holds no secrets and is mounted read-only.
>
> **AI Involvement:** I'm a software architect and use Claude Code for speed. It does the typing; I make every decision, review every change and art-direct the UI.
>
> Feedback welcome, especially on which tool you'd want it to read next.

---

> **vanmiku**（1 分） · 2026-10-30T21:46:52+08:00　
> **Project Name:** mydash
>
> **Repo/Website Link:** https://github.com/vanmiku/mydash
>
> **Description:** If you use Claude Code or Codex, they produce plans, reports, screenshots, HTML prototypes and Office files that end up as paths in a terminal. mydash collects them: the agent runs `mydash publish`, and a small Node server on your own machine renders them (Markdown with Mermaid, PDF, Word/Excel/PowerPoint previews, HTML, images), grouped by project, with versions, unread state, search and comments. Agents can also send approval forms and to-do lists, and Claude Code's choice questions and permission prompts show up there too, so you can answer from your phone.
>
> Self-hosting details:
>
> - Listens on 127.0.0.1 only. Reach it through `tailscale serve`, its own Tailscale node (http://mydash/), or on your LAN with an access code. Public addresses are refused.
> - Published HTML and SVG run on a separate port, so their scripts can't touch the workbench; workbench pages carry a CSP.
> - Data is plain files under ~/.mydash/data, easy to back up. Unchanged files are hard-linked between versions.
> - Notifications through Bark, ntfy, Telegram, Pushover, team chat bots, email or web push.
>
> **Deployment:** Released as v0.1.0, MIT. Needs Node.js 20+ on macOS, Linux or Windows; runs as a launchd / systemd / Startup-folder service (on macOS it can start at boot before anyone logs in). No Docker image, since it has to run next to the agent. Install by pasting one line into Claude Code or Codex ("Install mydash for me by following https://github.com/vanmiku/mydash/blob/main/INSTALL.md"), or run `./setup.sh install` yourself; README and INSTALL.md cover both.
>
> **AI Involvement:** Built largely with Claude Code, with me writing the requirements, deciding the design and reviewing it. Then reviewed and tested: 500+ end-to-end checks on macOS and Linux, install tests on Windows in CI.

---

> **WorriedAd9268**（1 分） · 2026-10-30T21:52:49+08:00　
> Project Name: GitHub User Check
>
> Repo/Website: https://github.com/Daxesh-Italiya/github-user-check
>
> Description:
>
> Managing GitHub access becomes complicated when you're running a service-based company with multiple projects, personal repositories, and GitHub organizations.
>
> Developers often have access to multiple organizations and repositories. When someone leaves the company, auditing and removing their access everywhere can become a time-consuming manual process.
>
> I built this tool to simplify that process.
>
> Key features:
>
> - Scan multiple GitHub personal accounts and organizations.
> - Get a consolidated view of users and their repository access.
> - See how many organizations and repositories each user can access.
> - Audit user access across multiple accounts from one dashboard.
> - Remove a user's access across multiple organizations and repositories in bulk.
>
> The goal is to make GitHub access auditing and employee offboarding easier, especially for teams managing multiple projects and organizations.
>
> Deployment: Self-hosted. Check the GitHub repository for installation and setup instructions.
>
> AI Involvement: I used AI to help draft this Reddit post. The project itself is built to solve a real operational problem I experienced while managing multiple development projects.

---

> **PromiseGrouchy6758**（1 分） · 2026-10-30T22:15:02+08:00　
> Name: Sales Coach
> Repo: github.com/Sales-Coach (https://github.com/Yz613/Sales-Coach) (MIT)
> Description: The open source gong alternative to help your sales team crush their goals without paying a ton of money. I basically built this because I didn't have enough time to manage my sales team and do everything else I was doing, being part of a startup. This helped me kind of understand each rep, how they were doing based on their sales calls. It would grade each one, and I was able to copy the voice of our sales coach consultant, and based on how he answered a bunch of questions before we launched, build an AI copy of him that scored each call for my sales reps the same way he would.It also gave me, the manager, direct copy-paste talking points to give to my sales reps that the coach would have given. I then added a bunch of things like integrations from CRMs and other tools. Those are built the same way Gong uses them, but I think as customers have different ideas about how to better use them, those will probably change.
>
> Read-only demo with four fictional calls, no signup: refreshqueue.com/demo
>
> Deployment: docker compose up --build, then open localhost:3000/app/calls. Local mode runs on SQLite and needs no account or API keys. A built-in rules engine scores pasted transcripts. For model-based scoring, point it at a local model server with a standard chat-completions endpoint (plus a local transcription endpoint), or use your own provider key. Full steps are in SELF-HOST.md.
>
> AI Involvement: Scoring and coaching can optionally use a model (local or your own key), and the default rules engine uses none.
>
> Development: The post was written by me and the code was written by AI
>
> I built it. Feedback on the self-host path is very welcome, especially anything that broke.

---

> **NexeraV**（1 分） · 2026-10-30T22:17:49+08:00　
> Project Name: Nexera Property Manager
>
> Repo/Website Link: https://github.com/nexerav/nexera-property-manager (live demo at https://demo.nexerav.com, login demo / demo-nexera, resets nightly)
>
> Description: A free, self-hosted property manager for small landlords. I'm a landlord in South Africa and built it to replace spreadsheets and pricey SaaS for my own rentals. It tracks tenants and leases, rent and invoices, expenses, maintenance and monthly P&L, and your data stays on your own server.
>
> Deployment:  It runs with Docker Compose, and the README has install and usage steps (clone the repo, then run \`docker compose up -d\`). It's a Flask/Python app with JSON file storage, licensed AGPL-3.0.
>
> AI Involvement:  It was built with heavy help from AI coding agents. I designed it, tested it and use it for my own properties.
>
> Feedback welcome!

---

> **HiimKami**（1 分） · 2026-10-30T22:51:10+08:00　
> Project Name: Uptimy Agent
> Link: [https://github.com/uptimy/agent](https://github.com/uptimy/agent)
>
> Description: Open source (Apache-2.0) agent that runs inside your Kubernetes, Docker or Railway setup and monitors what outside checks can't reach, like internal services and workers. Optionally, it can connect to the cloud Uptimy so users can get notified if their cluster goes down or to sync monitors for uptime reports... All available for free.
>
> Deployment: Runs in Kubernetes, Docker or Railway.
>
> AI Involvement: I am a Software Engineer and I use AI on a daily basis

---

> **justcinek**（1 分） · 2026-10-30T23:21:24+08:00　
> # Switchboard: a local-only web app to run and supervise AI coding agents, reachable from my phone over my own Tailscale (no relay, no account)
>
> https://i.redd.it/9fvcpqkngmyh1.png
>
> Hey [r/selfhosted](/r/selfhosted/)! I wanted to share with you solution that I made initially for myself, but it grew to something that I think some of you can use :) I usually have somewhere between 10 and 20 coding agents (Claude Code, Codex, OpenCode) running at the same time across a desktop and a laptop, and the real problem became noticing which one has been sitting there waiting for me since 10:14. I didn't want a third-party relay or someone's cloud in the middle of my code and sessions, so I built my own thing and open-sourced it. Reasoning? I know there's plenty of tools like that already, but I just thought it would be fun to write something on my own :)
>
> What it does:
>
> * One queue, **Needs you**, for everything any agent is waiting on: questions as buttons, permission prompts, stopped steps. One click, with undo.
> * A board of what's working / ready for review / done, a worktree per agent, and Jira epics as steps that start on their own in order.
> * Several logins per engine, switched automatically when one hits its usage limit.
>
> The self-hosted part, which is why I'm posting here:
>
> * It binds to [**127.0.0.1**](http://127.0.0.1) **only**. Other computers pair over **Tailscale**(a separate listener on the tailnet IP, per-peer tokens), and paired computers share one Needs-you queue.
> * Phones pair with a QR code through `tailscale serve`, install as an app, and get push notifications. Each phone has its own revocable credential.
> * **No account, no telemetry.** The only outbound calls it makes itself are GitHub update checks and, if you turn them on, web push through the browser vendor.
> * Runs as a per-user service on macOS (launchd), Linux (systemd) and Windows (Task Scheduler), and updates itself with checksum verification. From my phone I can even update the other computers when I forget one.
> * Logins never travel between machines. API keys an agent asks for are stored in the keychain of the machine the agent runs on.
>
> Honest caveat: it doesn't host a model (at least not as of now). It runs the **unmodified**`claude` / `codex` / `opencode` CLIs with your own logins, so the agents' own traffic still goes to those providers (or to a local model if you point OpenCode at one). Switchboard runs and supervises them.
>
> Try it (Node 24+, git, and at least one of those CLIs signed in):
>
>     npx /switchboard
>
> or `curl -fsSL` [`https://raw.githubusercontent.com/MarcinGadomski94/switchboard/master/install.sh`](https://raw.githubusercontent.com/MarcinGadomski94/switchboard/master/install.sh)`| sh` (no sudo, checks the SHA-256; Windows has a PowerShell one-liner). Then open [http://127.0.0.1:13001](http://127.0.0.1:13001/).
>
> Security notes: [https://github.com/MarcinGadomski94/switchboard/blob/master/docs/security.md](https://github.com/MarcinGadomski94/switchboard/blob/master/docs/security.md) Repo (MIT): [https://github.com/MarcinGadomski94/switchboard](https://github.com/MarcinGadomski94/switchboard) The longer story of why I built it: [https://dev.to/marcingadomski94/how-i-run-many-claude-code-agents-at-once-without-losing-track-60](https://dev.to/marcingadomski94/how-i-run-many-claude-code-agents-at-once-without-losing-track-60)
>
> Give it a shot ! Would love to hear some feedback :)
>
> Full disclosure: I'm the author, and a big part of the code was written by Claude Code agents that I directed and reviewed (fittingly, inside Switchboard itself). Critique very welcome!

---

> **d4diaz**（1 分） · 2026-10-30T23:49:27+08:00　
> **PublicLocal: a self-hosted ngrok alternative (one Go binary, wildcard HTTPS, MIT)**
>
> I wanted ngrok-style [`https://myapp.mydomain.com`](https://myapp.mydomain.com) links without an account or a monthly bill, on a VPS I already pay for. So I built PublicLocal.
>
> On your server:
>
>     publiclocal server --domain tunnel.example.com --tokens "$(openssl rand -hex 24)"
>
> On your laptop:
>
>     publiclocal http --subdomain myapp 3000
>     # Forwarding https://myapp.tunnel.example.com -> localhost:3000
>
> What it does:
>
> * HTTPS on subdomains with automatic Let's Encrypt certs (or one wildcard cert via Cloudflare DNS)
> * Raw TCP tunnels too (SSH, Postgres, game servers)
> * Works behind NAT/CGNAT: the client makes a single outbound connection, multiplexed with yamux
> * WebSockets and streaming, token auth, auto-reconnect that keeps the same link
> * systemd unit and Docker image; about $5/month of VPS is plenty
>
> There's also a free public instance at [publiclocal.app](http://publiclocal.app) if you just want to try it, with limits (24h links, HTTP only, a browser warning page) to keep abuse down.
>
> Repo: [https://github.com/sevenoways/publiclocal](https://github.com/sevenoways/publiclocal)
>
> It's young, so I'd love feedback from people who run frp or cloudflared today: what would make you switch, and what's missing?

---

> **Theratchetnclank**（1 分） · 2026-10-31T00:18:56+08:00　
> **Project Name:** BingeSync
>
> **Repo/Website Link:** [https://github.com/dnewsholme/BingeSync](https://github.com/dnewsholme/BingeSync)
>
> **Description:**  It's self hosted [trakt.tv](http://trakt.tv) alternative logging watch history from plext/jellyfin/emby.
>
> Logs watch history per user to a database, and enriches with metadata from TMDB or TVDB, supports only OIDC for login/user management. Allows easy cleanup of watched tv series and films with integration to radarr/sonarr. It has mobile support and supports being installed as a progressive web app. It also supports [trakt.tv](http://trakt.tv) import by importing the zip from a [trakt.tv](http://trakt.tv) export.
>
> I created it because the available options were limited, didn't like Yamtrack it seemed to mess up imports and log watches from other users. Media tracker had similar issues and [trakt.tv](http://trakt.tv) hiked it's subscription price by a lot!
>
> **Deployment:** Docker container deployment. Instructions on the github page.
>
> **AI Involvement:** Coded using Antigravity and Gemini, but i am a developer in my role at work so it had a robust set of unit and e2e tests to ensure functionality. Code is reviewed and analysed for security.
>
> https://i.redd.it/avc0h4uqqmyh1.png

---

> **MattMose**（1 分） · 2026-10-31T00:27:13+08:00　
> **Project Name:** Hapimatic
>
> **Repo/Website Link:** https://github.com/SolidPD/hapimatic-core
> and https://hapimatic.com/install
>
> **Demo:** a 4-minute tour of the product, no sound: https://youtu.be/CWw3NQhVC1c
>
> **Talk:** 30 minutes, at Drexel University on October 21: https://youtu.be/FA4J1-CL8w4
>
> **Description:** You get the same modern, responsive app interface on your phone, tablet, and desktop, so when a session asks for approval you can answer it from wherever you are. Every session is a peer of every other: see it, message it, or spawn it, on any machine you own or any VM you run. For Claude Code and Codex, server restarts, crashes, reboots, API outages, and rate limits do not end a session. Each session gets its own worktree, and the complete record of every session stays saved on your node.
>
> Harnesses supported at launch: Claude Code, Codex, Gemini CLI, and OpenCode.
>
> **Deployment:** It installs with one command on 64-bit Linux (x86-64 or ARM64) with systemd, and the Install page and the documentation cover the setup.
>
> **AI Involvement:** Claude Code wrote almost all of the code; I made the design decisions and reviewed every change.
>
> **Current limits:** macOS is planned, and Gemini CLI and OpenCode sessions do not persist through a restart of the Hapimatic background service.
>
> **Compared to similar tools:** what Hapimatic does differently is keep Claude Code and Codex sessions alive across restarts and reboots, and run every session as a peer you can reach from any of your devices.
>
> The core is free and open source (AGPL). Paid add-ons (Issue Workflow, Project Manager, Hardware Bench) and hosted VMs are planned; nothing paid is required to run it.

---

> **Eyusd**（1 分） · 2026-10-31T00:55:31+08:00　
> **Project Name**: murmur, a self-hosted hub that keeps a team's AI coding agents in touch
>
> **Repo Link**: [https://github.com/EledoneAi/murmur](https://github.com/EledoneAi/murmur) (Apache-2.0)
>
> **Description**: When several people on a team run coding agents (Claude Code, Codex, Cursor, OpenCode, Copilot CLI, Gemini CLI), each agent works blind to the others: it doesn't know what they're working on, what they've decided, or what they've already figured out. murmur lets the agents see what every other agent is doing, message each other and their people, and ask each other questions. When an agent is about to edit a file someone else's agent is changing, it's told who, once, so the two talk first. There's a console in the terminal and a team page on the hub. There's no central service and nothing reports back to us: code, diffs, prompts and transcripts stay on the laptops. The hub sees what each agent is doing (its name, branch, conversation title, the paths of files it changes) and the messages; docs/privacy.md lists all of it.
>
> **Deployment**: each laptop installs the CLI (Homebrew, or a single binary from the releases) and runs a small daemon. The hub is one Go binary or container image (ghcr.io/eledoneai/murmur-hub) on sqlite, Postgres or Firestore, with recipes for Docker Compose, Kubernetes, Fly, Railway, Render, AWS, Azure, Cloud Run and systemd. People sign in through your own identity provider (any OIDC provider, Google or GitHub). You can try the hub locally with the one docker run line in the README, or skip it with murmur solo, which runs the hub inside the daemon on 127.0.0.1. Self-hosting and configuration docs are in the repo.
>
> **AI Involvement**: most of the code was written with coding agents, mostly Claude Code, several at once, which is how we ran into the problem in the first place. Our team uses it every day.

---

> **CheeseOnFries**（7 分） · 2026-10-31T01:00:59+08:00　
> **Project Name:** Fairweather
>
> **Repo/Website Link:** [https://github.com/john-overton/fairweather](https://github.com/john-overton/fairweather) · live at [https://openglades.com/fairweather](https://openglades.com/fairweather)
>
> https://i.redd.it/j2jp2qrfymyh1.png
>
> **Description:**
>
> A personal, ad-free weather app (installable PWA) with no accounts and no tracking.
>
> * **Now:** current conditions from the nearest NWS weather stations rather than a model guess, plus wind, humidity, pressure trend, UV, air quality, sunrise/sunset, and rain over the past 24 hours.
> * **Hourly:** 24-hour chart blending the NWS forecast with the NBM, HRRR, and ECMWF models, adjusted toward the latest station reading.
> * **Radar:** past 2/6/24 hours plus up to 18 hours of HRRR forecast, in reflectivity or precipitation type (rain/snow/mix, decoded from NOAA MRMS), covering the lower 48, Alaska, Hawaii, and Puerto Rico. Forecast frames are clearly marked as model output.
> * **Push notifications** without an account: NWS alerts for your saved places, "rain in the next hour," and an optional morning brief, with quiet hours.
> * Works offline with the last forecast, and comes with 11 color themes in light and dark.
> * Your saved places and settings live in your browser. The server only stores push subscriptions (SQLite).
>
> All weather data comes from free public sources (NWS, Open-Meteo, the Iowa Environmental Mesonet, NOAA MRMS on AWS), so there are no weather API keys to buy.
>
> It's built around the National Weather Service, so it covers all 50 states, Puerto Rico, and the U.S. Virgin Islands. Elsewhere it falls back to model-only forecasts (no station readings, alerts, or radar).
>
> **Deployment:**
>
> It's a Next.js app that runs as a Node service behind nginx at \`/fairweather\` so it nestles cleanly behind whatever selfhosted domain you use. It includes job templates with a crontab for alerts and the radar cache. \`docs/DEPLOYMENT.md\` covers install, the systemd unit, the nginx block, and cron. The repo includes the systemd unit and nginx config.
>
> * Needs Node 20 to 25 and nginx (or another reverse proxy).
> * A free Mapbox token is needed for the radar map; everything else works without one.
> * Push notifications need VAPID keys (one command, documented).
>
> **No Docker image yet.** PRs are welcome, fork it to your desire.
>
> It runs comfortably on a small VPS (1 CPU, 2 GB).
>
> MIT Licensed.
>
> **AI Involvement:**
>
> Heavy. I wrote the spec and design. Opus 5.5 wrote most of the code and the deployment setup from it, with me directing, testing on my phone for bugs and changes.

---

> **dannyded**（3 分） · 2026-10-31T01:42:32+08:00　
> Name: BoothWall
>
> Repo: https://github.com/boothwall/boothwall-oss
>
> Description: A live photo wall for events. Guests scan a QR code and send a photo from their phone, the host approves it, and it shows up on a TV (there's a native Fire TV app) or in any browser on a laptop or projector. I put it together as a demo for next.app devCon in Berlin and open-sourced it afterwards. MIT.
>
> Deployment: \`pnpm demo --lan\` runs the whole thing on your own machine, no accounts, and phones on the same Wi-Fi can upload. For a real event it deploys to Cloudflare Workers (R2, D1, one Durable Object per wall). Honest caveat for this sub: there's no non-Cloudflare production path yet. If someone wants to help with a plain Node + SQLite + disk backend, I'd love that.
>
> AI Involvement: Code's mine, the demo photos are AI-generated.

---

> **sch1z0maniac**（1 分） · 2026-10-31T01:51:50+08:00　
> **Project Name:** odysseus-homelab
>
> **Repo:** https://github.com/MarufPulok/odysseus-homelab (MIT)
>
> **Description:** The setup and scripts I use to run an old laptop (Ryzen 5 3500U, 16 GB, no dGPU, Manjaro) as an always-on assistant around [Odysseus](https://github.com/odysseus-dev/odysseus). Odysseus gives me chat, calendar, todos and notes. This repo is everything around it:
>
> * Base box setup: Docker, Ollama bound only to the docker bridge, Tailscale serve (not funnel, nothing public), ufw default deny, btrfs + Timeshift snapshots before updates
> * Small Python jobs on systemd user timers, stdlib only. Site watchdog with down/recovered alerts, a daily brief, meeting prep 10 to 20 min before a call, phone capture through ntfy (text becomes a todo with a reminder, a link becomes a summary doc), a weekly release digest for repos you follow, nightly SQLite-safe backups of the Odysseus data
> * Background jobs use qwen3 4B on the Vega 8 iGPU through Ollama's Vulkan backend. About 8 tok/s, which is fine for cron stuff, and private text never leaves the box
> * One shared helper file (config, ntfy, local model, Odysseus API, state), so a new job is around 20 lines. There's a worked example in the README
>
> A couple of jobs (Slack DMs to todos, a Notion board to calendar) use your own browser session because I'm a guest in those workspaces and can't add an app. They're optional and marked that way, check your workspace rules before using them.
>
> **Deployment:** It's scripts, not a container. A root setup script for Arch/Manjaro, a compose override plus the .env values for Odysseus, then copy config.example.toml and run install-timers.sh with the jobs you want. Steps are in the README. Needs Python 3.11+.
>
> **AI Involvement:** Most of the code was written with Claude Code. I picked what each job does and have been running and debugging it on my own laptop since Oct 25. Along the way I found a bug in Odysseus that blocked agent chats from reading the calendar and sent a fix upstream (PR #6889, still open).

---

> **zajca**（1 分） · 2026-10-31T02:17:46+08:00　
> Project Name: pohunek
>
> Repo/Website: https://github.com/zajca/pohunek · https://pohunek.dev
>
> Description: A small daemon you run on your own machines to keep coding agent sessions (Claude Code, Codex, Hermes Agent) alive. Sessions survive SSH disconnects and daemon restarts, and from my laptop I see all sessions across all machines in one list, with each one marked as working, waiting for approval or idle. Each session can get its own git worktree. The CLI has JSON output, so another agent can start and manage sessions too. I run it on a few PCs at home plus a VPS, connected over Tailscale or NetBird. No account, no cloud, MIT licence.
>
> Deployment: Linux x86_64 (release archives with an install script for the user service) and macOS on Apple Silicon (brew install zajca/pohunek/pohunek). No Docker image, because it needs to run next to your agents and repos on the host. Install docs: https://pohunek.dev/install/
>
> AI Involvement: Built mostly with Claude and partly Codex, with me planning and reviewing. English isn't my first language and AI helped with grammar in this comment too.

---

> **sekiro65**（1 分） · 2026-10-31T03:16:01+08:00　
> **Project Name: OCHA**
> **Repo/Website Link:** [**https://github.com/sekiro65/ocha**](https://github.com/sekiro65/ocha)
> **Description :**
> OCHA is built on [Explo](https://github.com/LumePart/Explo) by LumePart. Explo finds the tracks your ListenBrainz or Spotify discovery playlists are missing and builds those playlists in Jellyfin or Navidrome. What I added is a Telegram music bot as a download source.
>
> I listen to a lot of regional music, and Soulseek barely has any of it. Telegram music bots usually do, so OCHA can download from them as well as from yt-dlp and slskd, and you can switch between them in settings.
>
> I also fixed the matching so it copes with “(radio edit)”, featured-artist spellings and transliterated titles. Downloads get tagged from MusicBrainz by Beets and filed as Artist/Album/Track, with a small plugin that keeps collabs under the main artist in Jellyfin. You can request a single song from the web panel on your phone by typing `Artist – Song` or pasting a Spotify or YouTube link, and each playlist can run on its own schedule.
>
> It runs in one Docker container. Clone the repo, copy `.env.example` to `.env` and run `docker compose up -d`. The setup guide takes about 15 minutes, and the Telegram guide covers the API ID, sign-in and rate limits.
>
> It’s early, so I’d like to hear about bugs and ideas. Screenshots are in the README.
>
> and yes it is developed with the help of claude and other AIs

---

> **Fit-Reaction242**（1 分） · 2026-10-31T03:22:27+08:00　
> **Spawnpoint**, a self-hosted Minecraft panel (alpha)
>
> Repo: [https://github.com/vayungodara/spawnpoint](https://github.com/vayungodara/spawnpoint)
>
> Site and tour: [https://spawnpoint.vayun.net](https://spawnpoint.vayun.net)
>
> I made it for the modded server I host for my friends. I wanted it fast and uncluttered, more like a good app than an admin console. On my Linux server one start reached health OK in 0.56 s, and the panel used about 60 MB with the game servers stopped (panel only, Minecraft not included).
>
> What it does: mods and plugins from Modrinth and CurseForge, new servers from modpacks, backups, world slots, a config editor and a file manager. Every mod change is tested on a copy first (a server boot, then a real client joining a throwaway server), and nothing goes live until I approve the review sheet. AutoModpack then syncs that exact pack to friends, and there's an undo for pack changes.
>
> Deployment: a curl install script on Linux and macOS, or a manual build on Windows. It needs Node 22+ and Python 3, and Java downloads on first use. A small supervisor runs as a systemd user unit, LaunchAgent or Windows service and owns the Java processes, so the game keeps running if the panel restarts. The web UI is on port 25570 behind a PIN. Keep it on your LAN or a VPN. If you already run Crafty Controller it can work next to it.
>
> Status: alpha. Locked revisions cover Fabric 1.21.1, Forge 1.20.1 and NeoForge 1.21.1 so far. Keep backups.
>
> **AI involvement:** moderate. AI coding agents wrote some of the code while I handled direction, design, feature decisions and approvals, and tested changes on real Crafty and Fabric/Forge/NeoForge servers. Models: Claude Code with Claude Fable 5 for the August build, then opus 4.8-5.5 until late October. On 28 to 30 October, agents in Amp (ampcode.com, an AI coding tool): its Ultra mode for the main work and its medium mode (OpenAI GPT-6.1 Sol) for research and small tasks, plus some Claude Code with Claude Opus 5.5. Since 30 October, Claude Code with Claude Opus 5.5. OpenAI GPT-6 Astra separately reviewed risky changes.

---

> **NoFutureKid**（1 分） · 2026-10-31T03:34:15+08:00　
> **Project:** TasmoFleet
>
> **Link:** [https://github.com/nofuturekid/tasmofleet](https://github.com/nofuturekid/tasmofleet) (AGPL-3.0, Docker, one Go binary with SQLite)
>
> **Demo:** [https://nofuturekid.github.io/tasmofleet/](https://nofuturekid.github.io/tasmofleet/) (real UI, simulated fleet, actions disabled)
>
> **What it is:** a self-hosted manager for Tasmota devices: config backups with diff and restore, a settings policy with a compliance view, bulk firmware updates with a guard against wrong chip families, live state over MQTT, fleet-wide commands. An alternative to TasmoAdmin. OIDC or local accounts. Images on ghcr.io and Docker Hub, an Unraid template exists, and it is listed in the official Tasmota docs under Upgrading, External Programs.
>
> **For whom:** people with more than a handful of Tasmota devices who want backups, drift detection and safe bulk updates in one place.
>
> **New in 0.20.0:** devices that TasmoFleet cannot reach over HTTP (other VLAN, SetOption128, web password issues) are now managed over MQTT if they are on the broker: console, settings, policy, config backup and firmware updates (including staged ESP8266 updates). The path is chosen per device from what is reachable, and the device page shows which path is used and why. HTTP stays the first choice. Restore over MQTT follows in 0.21.0.
>
> **What it does not do:** it does not replace Home Assistant, does not manage non-Tasmota devices, and does not send Status 0. MQTT backups need the device's MQTT password. Pre-1.0, so expect rough edges.
>
> **AI Involvement:** Heavily AI-assisted. I design the features and write the issues, Claude Code writes most of the code, tests and docs, and I review the changes and run releases on my own fleet of about 30 Tasmota devices. It is pre-1.0 and has one maintainer.
>
> Release notes: [https://github.com/nofuturekid/tasmofleet/releases/tag/v0.20.0](https://github.com/nofuturekid/tasmofleet/releases/tag/v0.20.0)

---

> **Few-Consideration-17**（1 分） · 2026-10-31T03:36:07+08:00　
> FOQB: Free, Open Quality Bookkeeping
>
> [https://github.com/parkfour/foqb.git](https://github.com/parkfour/foqb.git)
>
> demo site at [https://foqb.parkfour.com](https://foqb.parkfour.com) \- resets every six hours.
>
> I got tired of subscription pricing and feature paywalls on tools like QuickBooks and Wave, so I built FOQB.  It runs our household books and our small LLC's finances.  It is completely free and I don't plan on adding any paid features.
>
> **Core Highlights:**
>
> * **True Double-Entry:** Full chart of accounts, journal entries, and core reporting (P&L, Balance Sheet, Trial Balance, Cash Flows, General Ledger).
> * **Live Bank Feeds:** Connect via Plaid or SimpleFIN (or use local PDF/CSV statement imports if you don’t want external API connections).
> * **Business + Household in One:** Set up organizations as businesses or households. Household mode talks in categories rather than debits/credits, handles net worth, and includes a "Between Your Books" tool to handle owner draws or personal-card business expenses cleanly.
> * **Device-Side Receipt Processing:** The receipt scanning plugin parses bills and receipts locally in your browser/device—no media is sent to third-party cloud OCR endpoints.
> * **Offline PWA:** Journal entries can be queued offline and posted once reconnected.
>
> **Deployment:** The full stack runs locally at around 250 MB of idle memory. You can spin it up via Docker with the included quickstart:
>
> Bash
>
>     git clone https://github.com/parkfour/foqb.git && cd foqb
>     ./quickstart.sh
>
> This generates fresh secrets in `docker/.env`, brings up the full local stack (Next.js, Supabase Postgres, GoTrue auth, PostgREST, and Caddy proxy) via Docker Compose, runs migrations, and opens port `8090`.
>
> \*(If you prefer a zero-maintenance serverless setup, it can also be deployed to Vercel + Supabase free tiers).\*Deployment:
> The full stack runs locally at around 250 MB of idle memory. You can spin it up via Docker with the included quickstart:
> This generates fresh secrets in docker/.env, brings up the full local stack (Next.js, Supabase Postgres, GoTrue auth, PostgREST, and Caddy proxy) via Docker Compose, runs migrations, and opens port 8090.(If you prefer a zero-maintenance serverless setup, it can also be deployed to Vercel + Supabase free tiers).
>
> AI Involvement: I used Claude and antigravity as AI coding assistants throughout development to help write and iterate on the code. Every module has been architected with strict Row Level Security (RLS), verified against double-entry standards, and backed by a comprehensive Vitest test suite covering unit, component, and database integration tests.

---

> **Mori37**（0 分） · 2026-10-31T03:39:51+08:00　
> **Project Name:** AnimeArr, an anime-first \*arr (beta)
>
> **Repo/Website Link:** [https://github.com/MoriTranslates/animearr](https://github.com/MoriTranslates/animearr) (GPL-3.0, Docker, screenshots in the README)
>
> **Description:**
> I've run Sonarr for anime for years and kept fighting the same things: fansub numbering, absolute episodes, season packs that don't say "S01", and above all files that turn out to have no English subs (or only signs, or a dub when I wanted the original audio). AnimeArr is a library manager just for anime. It works next to Sonarr/Radarr/Prowlarr, or takes your anime over from them.
>
> * Anime numbering from AniList + AniDB + Anime-Lists (no TheXEM): absolute episodes, split cours, season packs.
> * Every download is probed with ffprobe before import: full subs in your language, the right audio, not a sample. Wrong files (a series batch posing as a movie, a dub without the original audio) are blocklisted and the next release is tried.
> * Replace season: swaps a messy season for one good pack, one verified episode at a time, and shows whether a pack beats what you have (TV < WEB-DL < Blu-ray < remux).
> * Dual-audio upgrades for shows you watch dubbed and subbed.
> * A ▶ Trailer button to check a show's art style before adding it (it only plays the official trailer; nothing is downloaded).
> * A plain-language "why" on every grab and skip, with an undo log, a seasonal calendar, and an installable phone app.
>
> **What it doesn't do (yet):** it doesn't re-audit files imported before AnimeArr took over a show (a library audit is planned for 0.9.1). No quality profiles or custom formats, no Sonarr-compatible API for Overseerr/Bazarr, no Jellyfin/Emby yet.
>
> **Deployment:** Docker image on ghcr.io (amd64 + arm64), with docker compose, docker run, and an Unraid template. PUID/PGID/UMASK/TZ are supported. It starts in practice mode (dry run). The default login (captain / morebooty) only works from your home network until you change it, so change it on first run, and don't port-forward it directly. SECURITY.md explains why.
>
> **AI Involvement:** Heavy. I design the features, decide what ships and test every change daily on my own library. Claude Code (Claude Opus 5.5) writes most of the code, tests and docs. Before this beta it went through separate AI review passes for security, UX and accessibility; the security pass found no critical or high issues, and the smaller ones were fixed before release. 359 automated tests. It's a beta with one maintainer, so keep backups and please file issues.

---

> **SpaceDoodle2008**（2 分） · 2026-10-31T04:40:00+08:00　
> Are you planning to improve the design? Could make use of a makeover. I'm tired of AI-generated designs, unfortunately.

---

> **SpaceDoodle2008**（1 分） · 2026-10-31T04:41:36+08:00　
> How do you circumvent getting blocked by them? They can easily find out what you're doing since you're blocking its native tools. Opencode, as far as I know, already blocks requests coming from clients similar to your setup here.

---

> **iamhasani**（1 分） · 2026-10-31T04:45:29+08:00　
> Project Name:
>  OpsDeck — an AI agent harness for infrastructure
>
> Repo:
>  https://github.com/vahidid/opsdeck
>
> I built OpsDeck because I wanted an AI agent to help with my servers, but I was always concerned about giving it too much access.
>
> Even a simple request like “find out why this service is down” meant giving the agent a way onto the server, explaining which host to check, and telling it where to find the logs. For deployments, I had to explain my setup and the steps again. I wanted the agent to be able to do the work without handing it unrestricted access or repeating all that context each time.
>
> So I built the harness I wanted, and I now use OpsDeck to manage my own infrastructure day to day.
> You connect an AI model or agent to OpsDeck.
>  It gives that agent tools to work with your hosts, networks and services: SSH through VPNs and jump hosts, Docker and Compose, Kubernetes, logs and metrics, databases, Ansible, DNS, certificates and deployments.
>
> Workspaces hold the infrastructure context, docs and runbooks; an encrypted local vault holds credentials.
> The agent can use those tools to investigate an issue, propose a change, carry it out after approval, and check the result.
>
>  For example, I can ask why a service returns 502. It can inspect the containers and logs, show me the proposed fix, then apply and verify it if I approve. Actions are recorded in an audit journal.
> OpsDeck can run its own agent with a model you configure, or expose its infrastructure tools over MCP to an agent you already use, such as Claude Code or Codex.
>
> Deployment:
>  OpsDeck runs locally as a desktop app for Linux, macOS and Windows, or with
> opsdeck serve
>  and a browser UI. Downloads, screenshots and setup instructions are in the repo. I’ve tested it most on Linux; the macOS and Windows builds have had less real-world use and aren’t code-signed yet.
>
> AI involvement:
>  The code was written entirely with Claude. I used Codex to test it for security issues. AI is also central to the product itself: OpsDeck is a harness that gives an agent infrastructure tools and puts approval controls around its actions.
>
> If you manage your own servers, I’d value your feedback: what access or approval controls would you need before letting an agent handle an infrastructure task?

---

> **jackiebrown1978a**（2 分） · 2026-10-31T04:45:30+08:00　
> This is great. Do you know if it happens to work with emby?  I have the same problem you just solved!

---

> **BatStrange818**（2 分） · 2026-10-31T05:00:57+08:00　
> **Project Name:** Catflops
>
> **Repo/Website Link:**  [**https://github.com/robertziel/catflops\_fleet**](https://github.com/robertziel/catflops_fleet) (Apache-2.0, beta)
>
> I’ve had a hard time finding a good panel to manage local inference across a fleet of several boxes. I wanted to turn a model on or off on a given machine, benchmark it, and actually see what’s happening under the hood: GPU, memory, bandwidth, queue, per-request decode. So I started building my own dashboard, with the engines inside it.
>
> Today I wondered if it might be useful to anyone else, so I published it.
>
> What it does right now:
>
> * **One endpoint for all the boxes.** Speaks both OpenAI and Anthropic APIs, so Claude Code and anything OpenAI-compatible just point at it.
> * **Start/stop models from the panel**, including tensor-parallel across two boxes over SSH (I run two DGX Sparks plus a 5090 box). It estimates memory before starting, so you don’t find out at load time.
> * **Works with vLLM, SGLang and TensorFold**, with the setup per hardware type kept in config, not code.
> * **Under the hood view:** live tok/s, prefill, queue, KV, modeled memory bandwidth and compute per box. GPU cards whose fans spin with load, and a per-box “flight recorder” with an hour of power, temps, clocks, network and containers.
> * **Benchmark swarms** to tune seats, context and prefill budget against real throughput.
> * **Power on/off** for the boxes (wake-on-LAN and shutdown).
>
> There’s no auth built in. It binds to localhost, and you put your own proxy in front.
>
> I’ve got lots of ideas for improving it:
>
> * **Task queueing:** I already built this well in another project (broker\_parrot), so the plan is to merge that broker engine in here.
> * **Easy customisation,** so anyone can shape their own setup with Claude: their own design, layout and custom widgets. There are already layout templates and drag-and-drop in the panel, but I’d like to take it much further.
> * More hardware types and engines.
>
> I’ll add these over time, but doing them properly takes a while. If it’s useful to you, or you’d want something specific, let me know.
>
> https://i.redd.it/2mdv1fx45oyh1.png

---

> **CheeseOnFries**（2 分） · 2026-10-31T05:14:36+08:00　
> I don't, I wanted a basic weather app without ads.  Feel free to fork to your hearts content.

---

> **Parrotman805**（2 分） · 2026-10-31T06:25:07+08:00　
> I’m pretty sure I can get it working with emby! I’ll give it a go and update you

---

> **OurHeroAndy**（2 分） · 2026-10-31T06:51:08+08:00　
> I love that I am not the only person who had this idea after getting sick of the mess that was the available weather apps.
>
> What sort of guidelines were you focused on in the creation of this?
>
> For me my key motivation was finding out what hours of the day were best for going for a bike ride (based on AQI, UV, and expected wind speed). I'm interested in what you wanted bring to your version.

---

> **CheeseOnFries**（1 分） · 2026-10-31T07:14:10+08:00　
> I'm pretty basic honestly.  I just wanted the functionality from the weather channel website without 800 ads or paying for their stupid app.
>
> NWS runs public API's and there is so much available you can just tap into.  This contains AQI, Windspeed, and UV.
>
> I just added alerts to the radar too.  So you can actually see the area impacted.
>
> https://i.redd.it/75q30rr1toyh1.png

---

> **Ok-Comparison2155**（1 分） · 2026-10-31T07:19:50+08:00　
> Name: PVArr
>
> Repo: [https://github.com/jlesterak/pvarr](https://github.com/jlesterak/pvarr)
>
> AI: Entirely vibecoded with Claude.
>
> Deployment: Docker compose with examples
>
> Description:
>
> I wanted to record live sports that come as web HLS streams, not over a tuner, and without any subscriptions, ever. If you've streamed from these sites, you'll know they are always crashing and never great quality. If I wanted a recording I'd have to babysit the whole time.
>
> So I had Claude build PVArr!
>
> - **Failover:** give it up to three links to the same event. When one dies or freezes, it moves to the next one on its own, and it keeps cycling back round instead of giving up.
> - **One file, one timeline:** every switch appends to the same recording with the clock carried on, so it plays and seeks properly. Watch it in MPV/VLC while it's still recording. When it finishes, it remuxes to MP4 with no transcode.
> - **Paste and go:** paste the stream url, the page that hosts it, or the stream aggregator page. PVArr finds the stream and starts recording.
> - **Automatic Events:** if you have an event page, *Find 3 streams* tests its links, ranks them by how well they actually deliver, and fills the slots with the best ones. *Read game* fills in the teams and start time, so you can schedule it and go to bed.
> - **Schedules:** one-shot start and end times. They survive container restarts.
> - **Events Page:** Have a go-to site? Paste in the Events page and PVArr will attempt to pull every single game being offered.
> - **Media server:** a virtual HDHomeRun / M3U tuner with an XMLTV guide, so a recording in progress shows up as a live channel.
> - **Optional:** comskip chapter marks with per-recording ad stats, Apprise notifications (ntfy, Gotify, Discord and so on), and offline team/league autocomplete for tidy filenames.
>
> **How it's different from what's already out there:**
>
> - **Dispatcharr:** if you have an IPTV provider playlist (M3U/Xtream), use Dispatcharr. It's the better tool for that, and it already does DVR and failover. PVArr is for when you have a *web page* instead of a playlist: it works out the headers and token itself, fetches a fresh token on every failover, and keeps one continuous file. No database, no accounts.
> - **DVarr:** Dispatcharr for sports. Again if that's your setup, it's the better fit.
> - **Streamlink / yt-dlp:** great grabbers, but one source at a time. When that source dies, the recording dies (or retries the same dead link). No UI, no schedule, no tuner. PVArr uses yt-dlp as a helper.
> - **Threadfin / xTeVe:** they give Plex a tuner, but they don't record and don't fail over. In PVArr the tuner is a side feature.
> - **Sportarr:** grabs finished releases after the event. PVArr records it *live*, while it's on.
>
> No database, no accounts, no telemetry, no license, no subscriptions ever. It only contacts the URLs you give it. Runs on Linux amd64 (massive 1.1gb image), with `PUID`/`PGID`/`TZ` set like any \*arr container. It has no login, so keep it on your LAN.

---

> **zorcererr**（1 分） · 2026-10-31T07:27:35+08:00　
> ￼​Project Name: Heddohon
>
> Repo/Website Link: https://github.com/zorcerer/heddohon (screenshots and a tour at https://heddohon.app)
>
> Description: Heddohon is a web music player you host in front of the Navidrome, Subsonic or Jellyfin server you already run
>
> What sets it apart from other players?
>
> •	⁠Your music server stays private. The browser only talks to Heddohon, which fetches the audio and metadata itself. You only expose Heddohon and the music server needs no public address. Sign-in goes straight to your media server, so there are no extra accounts you have to manage. Admin users are automatically synced from the music server.
> •	⁠Listen together, like a Spotify Jam. Send a link and everyone who opens it can hear what you're playing,  in their own browser and without an account. Friends with an account on your server can add to the shared queue
> •	⁠Share a song, album or playlist with anyone. The link plays the original file until it expires or as soon as you withdraw it. (Please only share music you're allowed to share)
> •	⁠Your listening stats stay on your server. Top artists and albums, the hours you listen, what you played on this day in earlier years, and daily mixes made from your history are all taken care of by Heddohon, including heatmaps and more coming soon
> •	⁠One player across devices. The queue and settings follow your account, and one browser can control another. Desktop apps are available for Linux and Windows, and an experimental Android app as well
>
> Also included:
>
> •	⁠Original files up to FLAC 24/192 with no resampling, or transcoding to MP3/Opus/AAC per account. (DSD/DSF gets transcoded automatically)
> •	⁠Crossfade, ReplayGain, a sleep timer, and a 10-band EQ with AutoEq headphone corrections
> •	⁠Synced lyrics, instant mixes and internet radio
> •	⁠Casting to Chromecast and AirPlay
> •	⁠Scrobbling to Last.fm and ListenBrainz (Users can set this themselves and have it synced automatically to Navidrome, so they never have to share their credentials with the admin)
> •	⁠A keyboard command line (Ctrl+K: play Spirited Away) and multiple themes
> •	⁠A built-in MCP included, so any AI agent can create playlists and browse.
>
> Deployment:
>
> curl -LO https://github.com/zorcerer/heddohon/releases/latest/download/docker-compose.yml
> docker compose up -d
> docker compose logs heddohon
>
> The log prints a setup code. Open http://:3000 and the setup page asks for your music server's address, generates the secret and saves everything. More elaborate documentation is available here
>
> For unraid users, the app can be downloaded from the CA.
>
> AI Involvement:
>
> Written with agentic assistance from Claude. The code and security posture have been reviewed by me and by multiple AI-assisted audits, documented in SECURITY.md
> I believe that transparency is important, especially in AI coded applications, so every finding is well documented there.

---

> **dudeski_robinson**（2 分） · 2026-10-31T08:57:15+08:00　
> **LibrePaper: a free, open source collaborative writing platform (LaTeX, Typst, Markdown, HTML)**
>
> Hi all,
>
> First, A little about me: I'm an academic who has been maintaining open source software for over 15 years. I also work with far away co-authors all the time, and I care a lot about the tools I use. Over the years, I've been pretty frustrated with existing collaborative writing platforms. Sooo... drum roll... I'm happy to introduce LibrePaper, yet another Overleaf replacement!
>
> LibrePaper is a collaborative writing platform that runs either in the browser, or in a (cross-platform) desktop app. It is open source (MIT) and completely free (no feature gates). You can use it for free at [librepaper.org](https://librepaper.org), or you can host it on your own server (ex: using ready-made docker images).
>
> **Cheap to run**
>
> The key design decision behind LibrePaper is that it compiles documents client-side, in your browser, using WebAssembly. The server only has to store and syncs your files; it never runs LaTeX itself. In practice, this means that:
>
> * A small server can run librepaper.org for everyone, for free, at low cost to me.
> * There are no compile queues or timeouts on a shared build server, since your own machine does the work.
> * Running an instance of LibrePaper on your own server is easy and cheap. This can be useful, for example, if your team works with private data.
>
> **LibrePaper has all the features**
>
> Writing:
>
> * LaTeX, Typst, Markdown or HTML.
> * Quarto computational notebooks (desktop app only).
> * Templates and insertions.
> * Autocompletion, symbol and math palettes.
> * Spelling and grammar.
> * Vim or Emacs keybindings, several colour themes, and dark mode.
> * BibTeX and Zotero.
> * PDF and HTML rendering.
> * Visual mode
>
> Collaboration and review:
>
> * Several people can edit the same document with live updates.
> * Comment threads.
> * Track changes.
> * Chat
> * Share links with access "roles"
> * Version history.
> * Projects tags and favorites.
>
> AI agents (optional):
>
> * Bring your own agent. No need for a new subscription. Just connect your existing Claude Code, Codex, Pi or opencode to a project.
> * Agents leave comments and tracked changes that you review like a coauthor's.
> * Agent tokens with access constraints.
>
> File sync and backup:
>
> * Download any project as ordinary files.
> * Git sync works through two CLI commands and a GitHub Action, so web coauthors have nothing to install.
> * The desktop app can download scheduled local ZIP backups of every project you can open.
>
> **Try it**
>
> * Hosted instance: [https://librepaper.org](https://librepaper.org) (sign in with GitHub or Google)
> * Source: [https://github.com/LibrePaper/librepaper](https://github.com/LibrePaper/librepaper)
>
> **Development**
>
> For transparency, I must say that this is the first project of this scale where I make heavy use of LLMs in development. As I said in intro, I've been doing open source the "traditional way" for a long time, so this is a big change for me. I've been working hard to make sure the app isn't pure slop, either under the hood or in the user interaction. I want the interface to look nice, functional, and minimalist. And I care about details.
>
> But LibrePaper is still young, so bug reports and feature requests are very welcome! Don't hesitate to post it here or on github.

---

> **vijaykes**（1 分） · 2026-10-31T11:01:43+08:00　
> Does it Also have captcha solving?

---

> **Saving-Singer101**（1 分） · 2026-10-31T12:14:28+08:00　
> Project Name: OnCallAlert
>
> Repo/Website Link: https://www.oncallalert.dev
>
> Description: A self-hosted, VPC-native incident management and AI triage engine built to solve three problems in infrastructure monitoring: per-seat pricing penalties that punish growing teams, alert fatigue from contextless 3:00 AM pages, and the security risk of handing production cluster credentials over to third-party cloud SaaS tools. It ingests standard monitoring webhooks (Prometheus, Datadog, Grafana), manages on-call escalation schedules, and optionally runs a local AI investigation loop inside your network via MCP to attach a 45-second root-cause summary directly to the alert before waking you up.
>
>  Deployment: Deployed as a single compiled Go binary alongside an optional headless Python sidecar via a single ⁠docker-compose.yml⁠.
>
> (Note: Currently in early-access waitlist while finalizing Apple's iOS "Critical Alerts" entitlement for DND/mute-switch bypass; Docker images and deployment docs go live immediately upon App Store clearance).
>
>  AI Involvement: Two levels of transparency here:
> 1. Product: Includes an optional, air-gapped Python/LangGraph sidecar (forked from Apache 2.0 Aurora) that uses your own LLM keys or local Ollama models to query logs/metrics strictly in read-only mode.
> 2. Development: Core routing engine is written in Go; AI coding assistants were used for UI scaffolding and boilerplate.

---

> **bishakhghosh_**（1 分） · 2026-10-31T13:42:07+08:00　
> but if i need to host it then it reduces the "ease of use" of tunneling isn't it? can you provide something like a single ssh command to connect? like what [pinggy.io](http://pinggy.io) does ?

---

> **ceph12**（2 分） · 2026-10-31T16:42:25+08:00　
> **mailrelay: a self-hosted SMTP server that turns incoming email into webhooks**
>
> A lot of the stuff I care about only tells me things by email: bank alerts, receipts, shipping updates, monitoring alerts. I built mailrelay to push those into my self-hosted apps instead of my inbox.
>
> Point an MX record or a forwarding rule at it, set up rules in the web UI (match on sender, subject, body or headers), and it POSTs the matching emails to your webhooks. I use it for bank alerts → Firefly III, receipts → Paperless-ngx, alerts → ntfy, and shipping emails → Home Assistant.
>
> * single Go binary or Docker image, SQLite storage
> * checks SPF/DKIM/DMARC
> * retries failed webhooks in the background
> * web UI shows every email, every webhook attempt and its response, with one-click replay
> * optional templates to shape the payload for Slack, ntfy and others
>
> Quickstart is one docker compose file, and you can send it a test email with plain `curl`.
>
> Repo: [https://github.com/gowthamgts/mailrelay](https://github.com/gowthamgts/mailrelay)
>
> Feedback welcome, it’s still early.

---

> **dasimers**（1 分） · 2026-10-31T16:43:22+08:00　
> This is going to be oddly specific but I'm looking to scrape product catalogues for prices and compare them for my business, does it handle login screens that have the catalogues hidden behind them, also does it have any anti ai features such as randomisation in time spent on the page, forced slowdown to stop forced 403 errors which are in place to stop scraping or anything like that?

---

> **paq85**（1 分） · 2026-10-31T17:43:46+08:00　
> **Project Name:** LLM Server Cost Calculator - 3 GPU presets, your $/kWh vs a cloud API (free, no sign-up, AppDoesIt)
>
> **Repo/Website Link:** https://appdoesit.com/apps/llm-cost-calculator/
>
> **Description:**
> Built it for the "is self-hosting an LLM even worth it on my electricity rate?" question. Pick a GPU preset (RTX 4070 Ti Super 500 W, RTX 5090 900 W, or RTX 5090 eco 650 W) or enter your own power + tok/s, set your $/kWh and workload, and it prices self-hosting against the same workload at a reference cloud API ($0.25/1M input, $0.02/1M cached, $1.20/1M output).
>
> At the defaults (500 W, $0.30/kWh, a continuous 60k input / 50k cached / 2k output workload at 90% uptime) the local box costs $3.24/day and $97.20/month, while the same workload at the reference API is $272.54/month - the local box wins by $175.34/month (64%). The RTX 5090 preset saves $484.63/month (73%). Cached tokens count at 1/100 the time of uncached, so the KV-cache line is in the math, not hand-waved.
>
> It runs in your browser: nothing is uploaded, no account, nothing to install. The pricing dataset behind it (llm-pricing.json) is open data. Try it by yourself :)
>
> **Deployment:** Nothing to deploy - it's a browser tool. Open the link, pick a preset, adjust your $/kWh, done.
>
> **AI Involvement:** The app is plain client-side arithmetic, no AI in it at runtime. The code was written with AI-assisted coding, and this post's copy is AI-drafted in the owner's voice, owner-reviewed.

---

> **d4diaz**（1 分） · 2026-10-31T19:30:10+08:00　
> >You don’t need to host anything. The free server at [publiclocal.app](http://publiclocal.app) is the default, and self-hosting is only there for people who want their own domain or no limits.
> >
> >And fair point on the SSH command, so I added it. Any OpenSSH client works, nothing to install:
> >
> >
> >
> >The link and a live request feed show up in the SSH window, Ctrl+C ends it, and port 443 gets through most firewalls. SSH links are anonymous and stop when you disconnect, with the same warning page and limits as the client. The host key fingerprint is on [https://publiclocal.app/docs#ssh](https://publiclocal.app/docs#ssh) if you want to check it on first connect. Passwords, visit limits, the request inspector and links that keep their address across restarts still need the small client.

---

> **lolina123**（1 分） · 2026-10-31T19:57:21+08:00　
> **Project:** OpsCrew
>
> **GitHub:** [https://github.com/softzer0/opscrew](https://github.com/softzer0/opscrew)
>
> I've been working on an open-source CLI that automates deploying applications to your own servers.
>
> It analyzes an existing GitHub repository, suggests a deployment configuration, generates the necessary Docker and infrastructure files, and sets up HTTPS, CI/CD, firewall rules, and deployment verification.
>
> Currently supports deployment to Hetzner Cloud, existing VPS servers, Portainer, and local Docker, among other targets.
>
> The main goals are:
>
> * No vendor lock-in: you own the servers and configuration.
> * Reproducible deployments using OpenTofu/Terraform.
> * Approval before infrastructure changes.
> * Optional AI assistance rather than mandatory AI usage.
> * Support for multiple apps on an existing server.
>
> **Status:** Alpha. Real deployments tested on Hetzner and existing infrastructure; other targets need more testing.
>
> **License:** Apache-2.0 core, with separately licensed FSL enterprise components.
>
> I'm interested in feedback from people running their own VPS or Portainer environments, particularly around deployment reliability, security defaults, and anything missing from the self-hosting workflow.

---

> **habihi_Shahaha**（1 分） · 2026-10-31T20:40:29+08:00　
> I built a lightweight, Customizable, FOSS e-reader
>
> [Flax reader](https://github.com/AgastyaShenoy/flax-reader) \- It's main aim is to be lightweight (Built entirely on rust, Kotlin for UI on android), customizable, accessible and make it easy to find books from sources.
>
> This was initially meant to be an AO3 only app, but eventually decided to shift to a full fledged, any e-book reading app, seeing the lack of lightweight options, and other reasons.
>
> https://i.redd.it/a1holotjpsyh1.png
>
> Search books from popular sites like AO3, Project Gutenberg, Standard Ebooks, Space Battles etc within the app and import them to your library, or bring your own books by importing them from settings!

---

> **nurlennart**（1 分） · 2026-10-31T21:26:27+08:00　
> I’ve been working on a small remote connection manager called Relay.
>
> GitHub: [https://github.com/nurlennart/relay](https://github.com/nurlennart/relay)
>
> I wanted something to manage my RDP and SSH connections without subscriptions, accounts, Electron, or a bunch of features I’d never use.
>
> There are already plenty of good FOSS alternatives, but none quite matched what I was looking for, so I figured I’d build my own.
>
> It’s written in Rust with egui, and the focus is on keeping it fast, lightweight and straightforward. It supports RDP, SSH, SFTP, tabs, split views and shared connection libraries.
>
> I figured it might be useful to people running multiple servers or managing a homelab who just want one place for their connections.
>
> AI has been used during development, mostly for implementation, debugging and code reviews. I’ve relied on it quite a bit, but I make the design decisions and review and test the results myself.
>
> It’s still a work in progress, and I’d genuinely appreciate some feedback. Especially from anyone running Linux or macOS, since those are harder for me to test thoroughly.
>
> Cheers!

---

> **KernelKunt**（1 分） · 2026-10-31T21:37:24+08:00　
> > Tasmo
>
> Hi
>
> I've been testing your application, and it's absolutely brilliant!
> Thanks for this project! It truly is a godsend!

---

> **NoFutureKid**（2 分） · 2026-10-31T21:39:17+08:00　
> Thanks a lot, really glad it's useful! If you run into anything odd or miss a feature, an issue on GitHub is the best way to reach me: https://github.com/nofuturekid/tasmofleet/issues. Since today there's also an arm64 image if you want to run it on a Pi.

---

> **Dry_Eggplant6329**（0 分） · 2026-10-31T21:52:25+08:00　
> **Project Name:** jolitz
>
> **Repo/Website Link:** [https://github.com/superlab-by-supbrt/jolitz](https://github.com/superlab-by-supbrt/jolitz)
>
> **Description:** jolitz turns a terminal AI agent (Claude Code or OpenCode) into a careful sysadmin for your servers over SSH. You type "/var is full on web1, what's eating it?" and it looks first. Before it changes anything it asks, backs up the file and tells you how to undo it, and it logs every change on the host and locally. It runs on Linux, FreeBSD, NetBSD, AIX and macOS.
>
> It's a fork of heinzel by Stefan Wintermeyer. Parts of heinzel moved into a paid Pro version, so I forked it to keep everything free under MIT. On top I added:
>
> * AIX support
> * an overview page from local memory: EOL dates, changes per host, open to-dos, config drift between servers
> * a guard hook that blocks the really destructive stuff in every permission mode: mkfs, partition tables, boot loaders, sshd\_config, sudoers, and sending env or keys to an outside URL
> * a marker that flags prompt injection in server output (banners, logs) before the model reads it
> * an optional team hub
>
> It's a backstop, not a sandbox. The docs say where it stops.
>
> **Deployment:** The tool itself runs on your workstation, not as a service: `git clone`, `cd jolitz`, `claude`. You need Claude Code (or OpenCode), jq and SSH keys to your servers. `bin/jolitz-doctor` checks the setup. The optional team hub is the self-hosted part. It's a single static Go binary with SQLite by default or PostgreSQL, and there's a systemd unit in the docs. Prebuilt binaries are attached to every release (linux amd64/arm64, freebsd, darwin), with SHA256 sums. jolitz can set the hub up for you over SSH via a skill. There's no Docker image yet. The hub never runs commands on hosts and never stores SSH keys or tokens in clear.
>
> **AI Involvement:** Built with Claude (Claude Code) and reviewed by me. The guard has a test matrix with 1500+ cases that runs on Linux, busybox and Windows in CI. The product itself is a rule set for an AI agent, so yes, it's AI all the way down, with a human approving every command.
>
> https://i.redd.it/toxbbvhp5tyh1.png

---

> **MediumJackfruit4263**（1 分） · 2026-10-31T23:58:48+08:00　
> Project Name: Sara (MIT licensed)
>
> Repo/Website Link: [https://github.com/farena-ai/sara](https://github.com/farena-ai/sara)
>
> Description: I’m building Sara as a self-hosted AI companion that can also help with real coding work. It combines editable persistent memory and a customizable personality with project workspaces, file editing, Git, and running tests. You choose the model: local through Ollama, vLLM or llama.cpp, or a supported cloud provider.
>
> I’m looking for developers willing to install it and tell me what breaks, especially installation problems, local-model performance, and coding workflow reliability. Bug reports, security feedback and contributions are welcome.
>
> Deployment: Run the server with Node 24+ or use the Docker Compose setup in the repository. The Compose file includes an optional Ollama profile. Start with the README and docs/INSTALL.md. You supply the hardware and model; cloud model usage can cost money.
>
> AI Involvement: I’m developing Sara with Claude, with Codex also contributing to computer-use features. This announcement was drafted with AI assistance. Sara itself uses the model you configure.
>
> Limitations: This is a young project, and model quality affects results. Please use a disposable workspace when testing coding or automation tasks.

---

> **NoFutureKid**（2 分） · 2026-11-01T01:04:54+08:00　
> Update: TasmoFleet now ships a multi-arch image, so it runs on a Raspberry Pi 4/5 (linux/arm64) as well. The backup decoder is included on both architectures.
>
> \- docker pull nofuturekid/tasmofleet:latest (or ghcr.io/nofuturekid/tasmofleet:latest)
>
> \- Release notes: [https://github.com/nofuturekid/tasmofleet/releases/tag/v0.24.0](https://github.com/nofuturekid/tasmofleet/releases/tag/v0.24.0)

---

> **yowmamasita**（2 分） · 2026-11-01T01:14:35+08:00　
> **Project Name:** rex
>
> **Repo/Website Link:** https://github.com/debridmediamanager/rex and https://rex.debridmediamanager.com
>
> **Description:** A media server for the official Plex apps that owns no files. Your movies and shows stay on any web server, a debrid service or a Usenet provider, and every Plex app plays them from there. Nothing is downloaded and nothing is scanned, so a title appears as soon as its source tells rex about it. Several sources fill the same Movies and TV Shows libraries. Remote playback in Plex Web and converting video work on free Plex accounts. A converted 1080p film starts in about 2 seconds on a small Intel GPU, and rex fixes the timing of a subtitle that's out of sync. There's an 88 second video here: https://drive.google.com/file/d/1SE-btkmoVH4iixL6rauCv5HgipKzw7WK/view
>
> **Deployment:** Nightly builds for Linux, macOS and Windows are on the releases page, or you can build it with Rust. The setup guide covers Windows, running it as a service and updates: https://github.com/debridmediamanager/rex/blob/main/docs/setup.md
>
> **AI Involvement:** I built it with a lot of help from AI coding agents.
>
> It's free for personal use (PolyForm Noncommercial) and the source is public.

---

> **Malfhas**（1 分） · 2026-11-01T01:24:06+08:00　
> **Project Name:** Humble Planning
>
> **Repo/Website Link:** [https://github.com/Malfhas/HumblePlanning](https://github.com/Malfhas/HumblePlanning) (website: [https://humbleplanning.com](https://humbleplanning.com))
>
> **Description:** Scheduling for field teams: people, projects, vehicles and equipment share one real-time grid, with day and hour views. I managed field projects for years with spreadsheets and phone calls; this is the tool I wanted then.
>
> * Drag and drop, half-days, recurring tasks that skip public holidays
> * Roles with scopes: everything, a business unit, a team, or one's own work
> * Project labour budgets; workload, occupancy and margin statistics
> * PDF, Excel and CSV exports; personal iCal feeds
> * Notifications by e-mail, push, SMS or WhatsApp
> * English, French, Spanish and German
> * Two-factor authentication, self-hosted captcha (ALTCHA), audit trail with restore
> * Optional AI: a built-in assistant that prepares changes the user must approve, and an MCP server for Claude, ChatGPT or any MCP client (OAuth, the user's own permissions). No API key, no AI.
>
> Demo: [https://demo.humbleplanning.app](https://demo.humbleplanning.app) (login `humbledemo`, password `humblepass`). The sample company is French; switch the interface to English from the language menu. Data resets every night; administration, e-mails and AI are turned off.
>
> **Deployment:** v1.0.1 is released, under the AGPL-3.0. Multi-arch Docker images (amd64, arm64) are published on GHCR (`ghcr.io/malfhas/humble-planning`), and an installer sets everything up with Docker Compose in one command:
>
>     curl -fsSL https://raw.githubusercontent.com/Malfhas/HumblePlanning/main/install.sh | sudo bash
>
> It installs Docker if needed (Ubuntu/Debian; any distro with Docker 24+ and Compose 2.20+), PostgreSQL 18 and, optionally, Caddy with automatic HTTPS, or it runs behind your existing reverse proxy. A `humble-planning` command handles status, logs, backups and updates; each update backs up the database first and rolls back automatically if anything fails. Install guide: [https://github.com/Malfhas/HumblePlanning/blob/main/docs/installation.md](https://github.com/Malfhas/HumblePlanning/blob/main/docs/installation.md)
>
> **AI Involvement:** I built Humble Planning with the help of AI coding assistants, which wrote much of the code under my direction. Product decisions, architecture and the review of every change are mine; every change goes through type checking, automated tests and linting in CI before it is merged, and I ran a security review before the 1.0 release. The README states this openly. The app's own AI features are optional and off without an API key.
>
> Feedback on the installer and the docs is very welcome.
>
> https://i.redd.it/me6646f87uyh1.png

---

> **lucahex**（1 分） · 2026-11-01T01:26:57+08:00　
> **Kowan**: a free self-hosted Docker manager for many hosts
>
> **What it does:** One web UI (plus CLI and an MCP server for AI assistants) to manage Docker and Swarm across many hosts. Each host runs a small agent that dials out, so hosts behind NAT just work. It handles compose stacks from compose or git, with revisions and rollback. It shows which workloads have newer images and updates them with health checks and automatic rollback. It also has searchable retained logs, CPU/memory history, uptime checks with a status page, alerts, PR previews, a built-in registry, vulnerability scans, volume backups, teams, SSO and an audit log. It works from your phone too (PWA). MIT licensed, no paid tier.
>
> **How to install:** One `docker run` for the server, one for each agent: [https://kowan.io/docs/installation/](https://kowan.io/docs/installation/)
>
> **AI involvement:** Built with heavy use of an AI coding assistant (Claude Code), under my direction and review; \~1,300 backend and \~550 frontend tests run in CI on every change.
>
> GitHub: [https://github.com/kowan-lab/kowan](https://github.com/kowan-lab/kowan) · Docs: [https://kowan.io/docs/](https://kowan.io/docs/)
>
> Feedback welcome, especially from Portainer/Komodo/Dockge users: what would you need to switch?
>
> https://i.redd.it/v9ga7ebx7uyh1.png

---

> **harshdoshi1**（1 分） · 2026-11-01T02:03:22+08:00　
> **Project Name:** Polysite
>
> **Repo/Website Link:** [https://github.com/polysites/polysite](https://github.com/polysites/polysite) and [https://polysites.github.io/polysite/](https://polysites.github.io/polysite/)
>
> **Description:** A CMS that runs many websites from one install. Each site keeps its own domain, theme, content and team, and an editor on one site can’t see or change another. The request’s domain picks the site. A hands-on tour gets two completely different sites running on a laptop in about ten minutes: [https://polysites.github.io/blog/ten-sites-one-install/](https://polysites.github.io/blog/ten-sites-one-install/)
>
> * Roles are edited in the admin with no code: tick what a role may do (create, read, update, delete, publish, unpublish, clone to another site), save. Anything not ticked is denied.
> * Themes are plain Nuxt-layer folders, and the first match wins: site theme, then parent theme, then core fallback. Ten finished example themes are included (spa, café, consultancy, shop, blog, portfolio, CV, conference, charity, help centre).
> * Block-based pages with Live Preview at phone, tablet and desktop widths, version history, and scheduled publishing.
> * Plugins for petition forms, events with RSVP and waiting lists, search, news, several languages per site, signed webhooks and a WordPress importer.
> * Petition forms allow one signature per person. In my lab test on one machine, 3,457 went in and 3,457 were stored, with none lost.
>
> **Deployment:** Docker Compose with Nuxt 4, Payload 3, PostgreSQL 16 and Caddy (automatic HTTPS). You need Docker and Git, ports 80, 443, 3000, 3001 and 5432 free, and about 5 GB of disk:
>
>     git clone https://github.com/polysites/polysite.git && cd polysite
>     git clone https://github.com/polysites/polysite-themes.git themes
>     git clone https://github.com/polysites/polysite-plugins.git plugins
>     cp .env.example .env
>     docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
>
> Then open [http://polysite.localhost/admin](http://polysite.localhost/admin). That is the hot-reload dev stack, so use a laptop or throwaway VM. For production, the deploy script backs up first, migrates, switches one service at a time and rolls back if a health check fails. Backups run nightly and are test-restored weekly. No telemetry.
>
> **AI Involvement:** I built it together with Claude, an AI coding assistant. The automated tests, real-stack checks and a public Known Issues log are the record of what was checked.
>
> It’s in beta and has had no independent security review yet. It is source-available, not open source: free for your own sites, and client work needs an agreement with me. Bug reports are welcome.

---

> **L_i_n_k0666**（1 分） · 2026-11-01T02:49:34+08:00　
> CodeRail: a self-hosted remote control for AI coding agents (Claude Code / Codex)
>
> What it replaces: hosted "agent in the cloud" setups. Your code, agent logins and history stay on machines you own.
>
> What it does:
>
> \- See and steer the agent sessions running on your computers from any browser or phone (installable PWA): chat, approvals, terminals, files, git, a browser.
>
> \- Approval requests arrive as push notifications (Web Push with your own VAPID keys).
>
> \- Multiple users on one deployment, with roles (Owner / Operator / Viewer), invite-only accounts and an audit log.
>
> Self-hosting details:
>
> \- One Docker container (Bun + SQLite). Everything it keeps is in ./data, so backing up that folder backs up everything.
>
> \- Plain HTTP on :8080. Put Caddy, Traefik or a tunnel in front for HTTPS (set TRUST\_PROXY=1).
>
> \- Computers connect outbound only, through a small bridge (Linux install script, or a signed Mac menu bar app). No inbound ports on your dev machines.
>
> \- It never holds AI keys: each computer runs its own \`claude\` / \`codex\` CLI with its own login.
>
> \- Permissions are checked on the server and again on each computer.
>
> \- Not end-to-end encrypted: the server stores session history, so host it somewhere you trust.
>
> Quick start:
>
> git clone [https://github.com/wiva-hq/CodeRail](https://github.com/wiva-hq/CodeRail) && cd CodeRail
>
> cp .env.example .env    # set SETUP\_TOKEN
>
> docker compose up -d --build
>
> Then create the first admin at https://your-site/setup.
>
> Apache 2.0. Docs: [https://docs.coderail.codes](https://docs.coderail.codes)
>
> Repo: [https://github.com/wiva-hq/CodeRail](https://github.com/wiva-hq/CodeRail)
>
> Feedback on the deployment story is welcome, especially from anyone running it behind Traefik or a Cloudflare tunnel.

---

> **elizabethbenson1969**（1 分） · 2026-11-01T03:32:55+08:00　
> **Project Name:** Folio Scan Studio
>
> **Repo/Website Link:** [https://github.com/kmmukut/folio-scan-studio](https://github.com/kmmukut/folio-scan-studio)
>
> **Description:**
>
> Folio gives printers and scanners you already own a modern web interface. It runs as one container on a Pi, a mini PC or an existing server, and you use it from a browser on any device on your network. No cloud account, no telemetry. A lot of this hardware gets retired only because the vendor's software stopped being updated, and the project's motto is "replace obsolete software, not functioning hardware."
>
> * **Scanning:** flatbed or feeder into multipage documents, with manual duplex and blank-page removal. Crop, rotate, straighten and reorder without touching the original.
> * **PDFs:** export with optional OCR, or send straight to Paperless-ngx or a NAS folder.
> * **Printing:** built-in CUPS with drivers for thousands of models, set up from the browser. Type a device's IP and Folio asks it how it prints and scans, then fills in the forms. Print options come from what each printer reports.
> * **AirPrint and AirScan:** iPhones print to your printers, and Macs scan from your scanners with no driver, even if the scanner only speaks WSD.
> * **Sharing:** accounts with private documents, print-only accounts, monthly page limits, print statistics, optional guest printing, and email invites and low-toner alerts over SMTP.
>
> https://i.redd.it/98ult8gutuyh1.png
>
> More screenshots are in the README.
>
> **What's been tested:** I use it daily on an x86-64 Docker host with a Samsung M2885FW (network mono laser MFP). It also runs on a Pi 4 (2 GB) with scanning, printing and iPhone AirPrint working, at about 380 MB of memory for the whole Pi (measured on 0.20.1). A Mac has scanned through AirScan with Image Capture.
>
> **What hasn't:** USB printers and scanners, because I don't own any, and AirScan on Windows and Android. That Samsung is also the only printer/scanner on the tested list so far, so reports from other hardware would help most, whether it works or not. Folio writes the report for you (Devices → Hardware report).
>
> **Deployment:**
>
> Docker Compose, with amd64 and arm64 images on GHCR and Docker Hub. Full is about 400 MB to download. Lite is about 315 MB and leaves out OCR and automatic straightening suggestions. No external database.
>
>     mkdir folio && cd folio
>     curl -fsSLO https://raw.githubusercontent.com/kmmukut/folio-scan-studio/main/compose.yaml
>     curl -fsSL https://raw.githubusercontent.com/kmmukut/folio-scan-studio/main/.env.example -o .env
>     docker compose up -d
>
> Then open `http://<host>:8870` within 15 minutes to create the admin account. AirPrint and AirScan are opt-in: they need a port published and the host's Avahi folder mounted. The [deployment guide](https://github.com/kmmukut/folio-scan-studio/blob/main/docs/DEPLOYMENT.md) covers that, plus Portainer, reverse proxies and backups. Licensed AGPL-3.0, and still a 0.x beta.
>
> **AI Involvement:**
>
> Heavy. Initial developments are mine, but after version 0.0.9, Nearly all of the code, tests and docs were written by AI, mainly Claude Code, and every commit carries its co-author line. I decide what gets built and test it on my own printer, scanner, Pi, Mac and iPhone. I also had ChatGPT review the code, and the real problems it found were fixed in 0.22.1. Every release runs the 300+ test suite inside both editions on amd64 and arm64 before it's published.

---

> **FaultyPhaser**（3 分） · 2026-11-01T03:34:38+08:00　
> # Stewarrd - A new way to manage seerr requests
>
> Traditional request systems have a very real limitation. They do nothing more than rate limit content that gets added to the server. There is no release valve. No way to easily determine what is no longer needed so it can be deleted. To solve this problem, I created Stewarrd.
>
> Stewarrd introduces a new way to manage content. When users request content, they become its steward at the cost of credits. The only way to get credits back is by releasing them to the public unclaimed pool where other users can claim it for themselves. At the end of the month (or whenever else the admin decides), content in the unclaimed pool can be assumed safe to delete.
>
> *Before the details below, lets get one thing out of the way. Yes, this is completely vibe coded. I won't claim otherwise.*
>
> * **Requests cost credits** (configurable per movie / per TV season), and the requester becomes the steward. If they can't afford it, the request is declined automatically.
> * **Owners release media when they're done watching** and get their credits back. Released items go to a public "Leaving soon/Unclaimed" list.
> * **Anyone can claim a "Leaving soon" item** for credits to keep it around.
> * **At month end, unclaimed items go into an admin report.** Nothing is deleted automatically. You confirm each purge, and only then does it remove the files through Radarr/Sonarr.
> * **TV is tracked per season**, so one person finishing a show doesn't remove seasons someone else is watching.
>
> **Other bits:**
>
> * Plex sign-in, limited to your existing Seerr users
> * Admin dashboard: assign media, per-user credit allowances, pricing, integrity check with a dry run
> * Kometa endpoints for a "Leaving soon" collection in Plex
> * Optional UI injected into Seerr via your reverse proxy (balance, claim/release buttons, a cost notice on requests)
> * Docker image (amd64/arm64) runs as non-root with a read-only filesystem and no media mounts
>
> # Please read before trying it:
>
> * **It's an alpha.** I've been using the whole workflow on my own server, including purges, and it works as I expect. But I'm the only one who has tested it, and the database format may still change.
> * **It writes to Seerr.** The webhook approves/declines requests. With the opt-in \`SEERR\_SYNC=1\` it also deletes and creates Seerr requests. \*\*Back up Seerr and Stewarrd's data first.\*\* The README explains exactly what it changes.
>
> GitHub: [https://github.com/FaultyPhaser/stewarrd](https://github.com/FaultyPhaser/stewarrd)
> Image: \`ghcr.io/faultyphaser/stewarrd:alpha\`
> License: GPL-3.0
>
> This is my first public project, so feedback, bug reports and "this setup broke it" reports are all very welcome, either here or as GitHub issues. I'd especially like to hear from people running Jellyseerr, Unraid, or reverse proxies other than Nginx Proxy Manager.

---

> **KernelKunt**（1 分） · 2026-11-01T05:17:40+08:00　
> I know there is one, I'm the one who asked for it 😅
> The hard part will be to fit your app into my homelab and make it work within my ansible workflow, especially the part with the ota server, this should be fun

---

> **Infamous_You7977**（1 分） · 2026-11-01T05:48:12+08:00　
> Project Name: Sentinel
>
> Repo/Website Link: https://github.com/jondean213-pixel/quietos-sentinel
>
> Description: Sentinel is the inbound check for a self-hosted agent, companion to QuietOS. QuietOS governs what my agent does — it approves or denies before anything runs. Sentinel governs what the world says TO the agent. World content is data, never orders. It's inspected before the brain sees it. If it looks like an outside instruction, Sentinel holds it, shows the owner the exact content, and the owner's tap releases it or kills it. If unsure, it fails closed. Benefit: an agent that reads the web, email, or pasted content can't be quietly steered by something planted in that content.
>
> Deployment: Released as a Python package, PyPI quietos-sentinel 0.1.0, bench suite 34/34. Install and use is documented in the repo README. No Docker image — it's a library/package, not a container app, and not a phone app version yet. It's not live protecting Gemma on my phone yet, and four holes are still open I'm closing next — synonym tricks, leetspeak, exfiltration carried in a summary, and non-English overrides.
>
> AI Involvement: Transparent — this post was drafted by my AI assistant Roman in my voice from my own notes, and I reviewed and posted it myself. The project is my own build, AI tools helped with drafting and building, design, decisions, and proof are mine.

---

> **Ok_Incident222**（1 分） · 2026-11-01T06:41:11+08:00　
> **Project Name:** Market Terminal
>
> **Repo/Website Link:** https://github.com/vladbondarenko97/market-terminal (MIT)
>
> **Description:** A market data stack for one person, on one box. A Python pipeline runs three times a trading day, pulls from Yahoo, FRED, EIA, CFTC, CBOE, FINRA, the NY Fed, Treasury and CME, stores every raw response in SQLite and commits one immutable snapshot per run. A Flask terminal shows it: a market stress index with daily history back to 1930, dealer gamma levels for SPY, volatility forecasts, silver and energy data. Alerts go to your phone through ntfy. An MCP server and a chat console on a local 9B model (Qwen3.5-9B on MLX) answer questions from the stored data. On Friday the stress index crossed into "stress" in the last run of the day, and the push reached my phone about ten minutes before the close.
>
> **Deployment:** No Docker yet. It's a Python venv and a launchd schedule on macOS (`./setup.sh`), and I run it on a Mac mini behind Caddy and Tailscale. The tests and an offline demo run work on Linux with no keys: `main_pipeline.py run --offline`. The terminal has no login, so keep it on a private network. Docs: docs/operations.md.
>
> **AI Involvement:** Built with Claude Code over a few months, under a rules file (AGENTS.md) the agents have to follow. 502 offline tests run in CI. A second model audited the whole project, and the fixes are in the git history.

---

> **maxwolt**（1 分） · 2026-11-01T06:48:41+08:00　
> Looks cool, though it’s not for my use case since I already have a stack configured. But if I were setting up a new server, I’d definitely give it a try. Keep going ;)
>
> P.S. Consider adding more screenshots, and maybe a demo so people can try the whole stack and the apps before installing.

---

> **UJGA**（1 分） · 2026-11-01T06:53:46+08:00　
> * **Project Name:** Hangar
> * **Repo/Website Link:** [github.com/PresWiFi/hangar](https://github.com/PresWiFi/hangar)
> * **Description:**
>
> Hangar is a self-hosted web UI for Claude Code and OpenAI's Codex CLI. Every session runs in tmux, so closing the browser doesn't kill it, and you can pick it back up from your laptop, phone, or tablet over your LAN or Tailscale. It works with your Claude or ChatGPT plan (no API keys) or local models through Ollama.
>
> The layout is modeled on Open WebUI, with sessions in a sidebar, each with a live terminal and a readable transcript.
>
> * Resume or fork any past session, with optional auto-restore after a restart
> * Usage dashboard for Claude and ChatGPT plan limits and token activity
> * Phone-friendly key bar and compose box
> * GitHub sign-in, so sessions can clone, pull, and push without SSH keys
> * Per-session file uploads and downloads
> * Optional SSO (Authentik, Entra ID, Google, Keycloak, any OIDC provider)
>
> Security heads up: anyone who signs in gets a shell on the host, so use a long password (or SSO) and keep it on your LAN or Tailscale. Don't port forward it.
>
> * **Deployment:**
>
> Docker Compose, with a setup guide in the [README](https://github.com/PresWiFi/hangar#docker). First start gives you a one-time setup code in the logs, then you link your accounts in the browser. There's no prebuilt image yet, so it builds locally. There's also a [Proxmox LXC script](https://github.com/PresWiFi/hangar#proxmox-ve), a Tailscale sidecar with HTTPS, Windows via WSL, and a no-Docker option. MIT licensed.
>
> * **AI Involvement:**
>
> Heavy. Claude Code wrote most of the code. I came up with the idea and directed how it works. Since it hands out a shell, I'd appreciate anyone looking over the auth, SSO, and terminal handling.

---

> **BalloonWheelie**（1 分） · 2026-11-01T10:55:25+08:00　
> Project Name: muster
>
> Repo/Website Link: [https://github.com/ZacxDev/muster](https://github.com/ZacxDev/muster) (MIT)
>
> Description: I run several coding agents (Claude Code, Codex, shells) in tmux on two machines. muster mirrors every tmux window on each machine to a web app on my phone. Claude Code sessions read as a chat; anything else shows as a live terminal. An agent can ask me a question through an MCP tool and wait: I get a push notification and answer by tapping or by voice. Viewing is read-only by default; typing from the phone is opt-in per machine.
>
> Deployment: One Go server plus Postgres via Docker Compose. Each GitHub release ships a docker-compose.yml and an env.example, and the images are on GHCR (amd64 and arm64). A small agent on each machine dials out to the server over your own Tailscale network, so muster opens no port on the machines. [INSTALL.md](http://INSTALL.md) walks through setup (or paste one line into Claude Code and it follows the guide), and \`muster doctor\` checks the result. Linux is the main target; macOS hosts are experimental.
>
> AI Involvement: Claude Code wrote nearly all of the code under my direction, since Sept 21. Every change is made on its own branch with tests, and a separate review agent audits the PR before I merge.

---

> **RealSirJoe**（1 分） · 2026-11-01T14:20:05+08:00　
> > Relinos
>
> currently not but planned. You may follow the github repo for updates

---

> **RealSirJoe**（1 分） · 2026-11-01T14:25:18+08:00　
> Yes, it can perform any interaction you would perform in a real browser. It can login and after that collect products. It does randomize types and clicks. Because it runs a real browser on your os its harder to detect ( passes cloudflare ).
>
> How many products are you trying to collect? Send me a pm with the site and I can look if relinos is the right fit for what you are trying to achieve.

---

> **Nexxus421**（0 分） · 2026-11-01T15:10:07+08:00　
> **Project Name:** Dirl
>
> **Repo/Website Link:** https://github.com/nexus421/Dirl
>
> **Description:**
>
> Dirl is a small self-hosted web SSH client for one person or a small team. I built it because tools like Termix grew too fast for my taste: many features, many small bugs, a lot to trust with the keys to everything. Dirl does one thing and tries to stay small enough to review alone. Screenshots are in the README.
>
> - Browser terminal (xterm.js) with snippets in folders. Variables like `{{Container}}` are asked for before the command is sent
> - SFTP file manager, up to two jump hosts, host key pinning with a hard block on changes
> - Status per host: reachability, SSH round trip, CPU, RAM, disks, load, failed services, reboot needed
> - Actions mode for phones: snippets, Enter and Cancel instead of the on-screen keyboard
> - Everything is managed in the browser, the config file only holds what is needed before login
>
> Since it holds your SSH keys, security got most of the attention:
>
> - Login only through your OpenID Connect provider (PKCE, confidential client)
> - Hosts, keys and snippets live in a vault encrypted with AES-256-GCM, the key derived with Argon2id from your passphrase. After a restart Dirl stays sealed until you unlock it
> - Generated `authorized_keys` lines with `restrict` and `from=`, an audit log, a strict CSP without inline scripts
> - SSH connections only while a Dirl page is open, nothing runs in the background
>
> **Deployment:**
>
> - Docker image `ghcr.io/nexus421/dirl` (amd64 and arm64) with an example compose file: read-only, no capabilities, no swap, port only on 127.0.0.1
> - Or a single fat JAR on Java 21 with a hardened systemd unit, attached to every release
> - You bring your reverse proxy for TLS and your OIDC provider. Pocket ID is tested, others should work, feedback welcome
> - Docs for usage, configuration, deployment and the security model: https://github.com/nexus421/Dirl/tree/master/docs
> - I run it in production myself (Incus LXC behind a reverse proxy). Every build runs tests against real OpenSSH servers and a full first start of the Docker image
>
> **AI Involvement:**
>
> Dirl is written with AI. Code, tests and docs were created with Claude by Anthropic, directed, tested and reviewed by me. The design decisions are mine and documented in the repo.
>
> Feedback is very welcome, especially on the security model and on OIDC providers other than Pocket ID.

---

> **Applekim4S**（2 分） · 2026-11-01T15:28:33+08:00　
> https://i.redd.it/wi5d07exdyyh1.jpeg
>
> *A quick note: English isn’t my native language, so I used AI to help me write and polish this post. I apologize if some parts sound a little unnatural or AI-generated. The project and experiences I’m sharing are my own.*
>
> **Project Name:** Luma Music
> **Repository:** https://github.com/GimGyumin/Luma-Music
> **Description**
> Hi everyone!
> I’m a high school student from South Korea, and I’ve been developing an open-source music player called **Luma Music** since August 2026.
> I’ve always wanted to enjoy my self-hosted Navidrome music library with the same kind of beautiful, polished, and native experience that Apple Music offers.
> That’s what I’m trying to build with Luma Music.
> Rather than just creating another music player, my goal is to make listening to music from your own server feel as seamless and enjoyable as using a native Apple app.
> Luma Music is based on the open-source Cassette project, which I’ve been extending and improving with new features, UI refinements, playback optimizations, and stability fixes.
> **Key features:**
> **Apple Music-inspired experience:** A native, artwork-focused interface with smooth transitions and animations.
> **Self-hosted music support:** Connect to Navidrome, OpenSubsonic-compatible servers, and supported Jellyfin libraries.
> **High-quality playback:** Lossless audio, gapless playback, crossfade, and ReplayGain.
> **Synchronized lyrics:** Line-by-line and karaoke-style highlighting, smooth scrolling, and optional translations.
> **Offline listening:** Download music from your server for offline playback.
> **Apple ecosystem integration:** Siri, Shortcuts, Spotlight search, widgets, and system playback controls.
> **Network reliability:** Adaptive streaming, caching, and playback recovery for unstable connections.
> **Deployment / Installation**
> Luma Music is a native client application, not a self-hosted server. You’ll need an existing compatible music server.
> **Supported platforms:**
> iPhone: iOS 18.6 or later
> iPad: iPadOS 18.6 or later
> Mac: macOS 15.6 or later
> The first release candidate, **Luma Music 1.0 RC1**, is available on GitHub.
> For iPhone and iPad, the app is currently distributed as an IPA and requires sideloading through a compatible tool such as SideStore or AltStore.
> Installation instructions and compatibility information are available in the repository’s README.
> **Download:** https://github.com/GimGyumin/Luma-Music/releases
> **AI Involvement**
> I want to be transparent about AI involvement.
> I’ve used AI coding assistants extensively throughout development, including writing code, debugging, refactoring, optimization, and testing support.
> I direct the project, make design and feature decisions, review the results, and test the application on real devices.
> This has also been a learning experience for me as a student exploring software development.
> **Feedback I’m Looking For**
> Luma Music is currently at the release candidate stage, and I’m looking for early users who can help identify issues before the stable 1.0 release.
> I’m especially interested in feedback on:
> **Synchronized lyrics:** Do the lyrics stay accurately synchronized? Are scrolling and karaoke-style animations smooth?
> **Playback stability:** Have you experienced unexpected restarts, interruptions, or issues when switching tracks?
> **Unstable networks:** How well does playback recover when switching between Wi-Fi and cellular data or when the connection becomes unreliable?
> **Gapless playback:** Are transitions between tracks seamless, especially on live albums?
> **UI performance:** Do album transitions, scrolling, and navigation feel smooth?
> **Server compatibility:** Does everything work correctly with your Navidrome or OpenSubsonic setup?
> Even a short report about what works well or what doesn’t would be extremely helpful.
> You can report bugs, suggest features, or share feedback through GitHub Issues and Discussions.
> **GitHub:** https://github.com/GimGyumin/Luma-Music
> Thank you for checking out my project! I’d really appreciate any feedback from the self-hosting community.

---

> **Accomplished_Walk243**（1 分） · 2026-11-01T19:40:20+08:00　
> **Project Name:**
> ArtCraft Hub
>
> **Repo/Website Link:**
> [https://github.com/GeorgeArgyrakis/artcraft-hub](https://github.com/GeorgeArgyrakis/artcraft-hub)
> *(Inspired by* [*artcraft-in-a-box*](https://github.com/sbuchweitz/artcraft-in-a-box) *by sbuchweitz)*
>
> **Description:**
> ArtCraft Hub is an all-in-one, self-hosted dashboard and automated release synchronizer for the Storyteller/ArtCraft suite of WebAssembly creative tools (PhotoCraft, VectorCraft, CADCraft, SoundCraft, PDFCraft, and more).
>
> Running client-side WebAssembly creative tools locally usually requires manually downloading releases, configuring web server MIME types (`application/wasm`), and setting up strict cross-origin isolation headers (`Cross-Origin-Embedder-Policy` and `Cross-Origin-Opener-Policy`) required for `SharedArrayBuffer` multi-threading. ArtCraft Hub solves this by packaging everything into a single lightweight container.
>
> Key features include:
>
> * **Unified Hub Dashboard:** Single interface with instant search (`/`), category filters, and pinned favorite apps.
> * **Dual Themes:** Switch between an editorial cream/ink "ArtCraft" style and a modern dark "Glass" style.
> * **Automated Sync Engine:** Background cron automatically fetches, unpacks, and validates new releases directly from GitHub.
> * **In-App Version Switching:** Roll back or switch between installed versions on the fly.
> * **Pre-configured Caddy Server:** Zero-config reverse proxy handling WASM compression, caching, and isolation headers out of the box.
>
> **Deployment:**
> ArtCraft Hub is released as a ready-to-run container on GitHub Container Registry (`ghcr.io/georgeargyrakis/artcraft-hub:latest`). Full setup instructions and configuration examples are available in the repository README.
>
> Quick `docker-compose.yml`:
>
>     yamlservices:
>       artcraft-hub:
>         image: ghcr.io/georgeargyrakis/artcraft-hub:latest
>         container_name: artcraft-hub
>         restart: unless-stopped
>         ports:
>           - "8080:80"
>         volumes:
>           - artcraft-data:/data
>           - artcraft-config:/config
>         environment:
>           - SYNC_CRON=0 0 * * *
>           - TZ=UTC
>     volumes:
>       artcraft-data:
>       artcraft-config:
>
> Run with `docker compose up -d` and open `http://localhost:8080`.
>
> **AI Involvement:**
> This project is entirely "vibe-coded" using AI pair-programming (Antigravity with Claude & Gemini models) to implement the dashboard frontend, shell automation scripts, Caddy reverse-proxy configuration, and Docker workflows.

---

> **Weak-Minimum-6781**（1 分） · 2026-11-01T19:59:57+08:00　
> **I built a free, self-hosted email alias service that runs entirely on Cloudflare Workers (one-click deploy)**
>
> I wanted SimpleLogin-style aliases without paying or running a server, so I built aliasflare.
>
> - Catch-all on your own domain: any new address auto-creates an alias
> - Forwards to your real inbox with the sender rewritten, so your address stays hidden
> - Reply from your normal inbox and it goes out as the alias
> - Pulls OTP codes into the subject line, strips tracking pixels
> - Stores only metadata in D1, never message bodies
> - Web dashboard, REST API, and an MCP endpoint so AI agents can create aliases and read codes
> - Receiving/forwarding is free on Workers + D1 + Email Routing; replying from an alias uses Resend's free tier (or Cloudflare Email Sending on Workers Paid).
>
> Repo (Deploy-to-Cloudflare button + two Email Routing settings, ~5 min):
> https://github.com/charleswei118/aliasflare
>
> Feedback welcome, especially on deliverability and what you'd want next.

---

> **ImL1s**（1 分） · 2026-11-01T21:08:16+08:00　
> **Project Name:** synology-nas-cli
>
> **Repo:** [GitHub](https://github.com/akari-sora/synology-nas-cli)
>
> **Description:** A CLI and stdio MCP server for Synology DSM 7, written during the C3RB3R (.L0CK3D) ransomware wave. `nas incident` reads the NAS and reports PASS, WARN or FAIL against Synology's advisories (DSM build, SA-26:14 packages, firewall, QuickConnect, port forwarding, AutoBlock, SMB, admin account, snapshots). `nas incident fix` shows a plan, asks, applies it and reads every setting back. `nas alert-deploy` puts a 10 minute check on the NAS that posts to a webhook, and there are 15 MCP tools if you want an agent to drive it. It does not decrypt already encrypted files; the rescue step only works while the encryptor is still running and the NAS has not been rebooted. The SA-26:14 table doesn't have the newer DSM 6.2 to 7.1 package builds yet.
>
> **Deployment:** Python 3.8+, no dependencies. `git clone` and run `./bin/nas`, or `pip install` the v1.0.0 release; it also runs on the NAS itself. No Docker image. MIT, not affiliated with Synology.
>
> **AI Involvement:** Most of the code was written with AI coding agents under my direction. I designed the checks against Synology's advisories and reviewed the changes myself.

---

> **Nasty_Dev_12**（1 分） · 2026-11-02T00:58:38+08:00　
> * **Project Name:** FlightAlert
> * **Repo/Website Link:** [GitHub Repo](https://github.com/RanuK12/flight-alert-public) · [Live Dashboard](https://flightalert.ranuk.dev/)
> * **Description:** An open-source, lightweight flight price tracker and Telegram alert bot. Instead of letting flight aggregators spam your email inbox with stale digests or tracking cookies, FlightAlert lets you set maximum fare thresholds on specific routes (e.g. BUE ⇄ MAD < $950 USD). The background crawler polls flight rates with exponential backoff/jitter, stores hot fares in an in-memory TTL ring-buffer cache (<35ms lookups), deduplicates alerts across a 12-hour cooldown window, and pings Telegram directly the moment a real fare drops below your line.
> * **Deployment:** Packaged in a multi-stage Docker container (`Dockerfile` included in repo). Built on Node.js 22 LTS with an idle RAM footprint under ~65 MB and zero heavy ORMs. Can be spun up in 2 minutes via `docker build -t flight-alert .` and `docker run -p 3000:3000 --env-file .env flight-alert`, with built-in `/health` endpoints and graceful SIGTERM/SIGINT shutdown.
> * **AI Involvement:** None. The core runtime is 100% deterministic (scheduled API polling, TTL cache eviction, mathematical price delta checks, and Telegraf bot commands).

---

> **MadZombie83**（2 分） · 2026-11-02T02:36:44+08:00　
> **Project Name:** Carribrary
>
> **Repository:** [https://github.com/MadZombie83/Carribrary](https://github.com/MadZombie83/Carribrary)
>
> **Description:**
>
> I've been developing Carribrary, a self-hosted library management system originally built for my wife's physical book collection.
>
> It's designed for managing real books, not just ebook files or reading lists.
>
> Features include ISBN cataloging, CSV imports, physical-copy tracking, borrower accounts, lending history, library cards, optional self-checkout, and browser-based kiosks.
>
> Libraries can customize their branding, and borrowers can access their library through a web browser.
>
> **Deployment:**
>
> The current preview provides installers for Windows, Linux (Flatpak), and Raspberry Pi ARM64 (DEB). It requires a host computer or server, with other devices connecting through the browser.
>
> **Licensing:**
>
> The core software is free to use. The repository is publicly visible, but Carribrary is proprietary, source-available software, not open-source.
>
> **AI involvement:**
>
> I used Codex and AI-assisted development tools while building Carribrary. I'm continuing to test and refine the software.
>
> **Status:**
>
> Public preview release. I'd particularly appreciate feedback on installation, physical-book circulation, and cross-device usability.
>
> https://i.redd.it/jw7wn19cp1zh1.png
>
> Release: [https://github.com/MadZombie83/Carribrary/releases/tag/v2.0.53-preview](https://github.com/MadZombie83/Carribrary/releases/tag/v2.0.53-preview)

---

> **Important_Pomelo_407**（1 分） · 2026-11-02T03:25:16+08:00　
> Created a demo for you using OpenDemo https://github.com/yasirwhite/OpenDemo.
>
> I opened a PR and added it to your README too: https://github.com/bnlqn/overlook/pull/99.
>
> https://github.com/yasirwhite/OpenDemo/releases/download/showcase-media/overlook-demo.mp4

---

> **cappuccin000**（1 分） · 2026-11-02T15:50:33+08:00　
> We don't circumvent anything. The relay doesn't spoof Claude Code or reuse OAuth tokens in a custom client, which is what got OpenCode blocked. It runs the official Claude Agent SDK, which runs the real Claude Code binary. Tool restrictions are the SDK's own `allowed_tools`/`disallowed_tools` options, not a disguise.
>
> The supported setup is an `ANTHROPIC_API_KEY`, and that's fully within Anthropic's terms. You can also point it at your own `claude login` subscription for personal use. Anthropic's Feb 2026 docs say subscription OAuth is meant for Claude Code and Claude.ai, and anything you'd ship or share should use an API key. If you use a subscription, that's between you and Anthropic's terms. We won't add tricks to dodge enforcement.

---

> **No-Biscotti-5452**（1 分） · 2026-11-02T18:51:14+08:00　
> Project Name: FlashRoute
>
> Repository: https://github.com/uiautodev/flashroute
>
> Description:
>
> FlashRoute is a compact self-hosted AI gateway with a built-in chat console. It aggregates DeepSeek, OpenRouter, BigModel, Anthropic and any OpenAI-compatible endpoint behind one OpenAI-compatible API, so your apps and agents talk to a single base URL instead of one per provider.
>
> What is in it:
> - Ordered route aliases with automatic fallback on 429 / 5xx / network errors; a target that gets rate-limited cools down for 60s before it is retried
> - Per-provider HTTP / HTTPS / SOCKS5 proxies, each independently testable
> - OpenAI-compatible /v1/chat/completions and /v1/responses, plus Anthropic /v1/messages with streaming
> - Reversible redaction: regex rules swap API keys, emails and private keys for same-length random values before a request reaches a provider, then restore them in the reply
> - Built-in chat UI, usage stats, sk-fr- client keys, and one-click setup for Claude Code / Codex / OpenCode / Pi
>
> Deployment:
>
> Single Go binary with the SvelteKit frontend embedded, MIT licensed. No Docker image yet: grab a release binary, or run npx flashroute. It serves http://localhost:8080 by default and stores data in ~/.config/flashroute (config.yaml, stats.yaml, SQLite). An optional Wails desktop build exists too. Install and usage docs, including flags for custom ports, data dir and remote auth, are in the README.
>
> AI Involvement:
>
> Developed by me with AI coding agents (mostly Claude Code) assisting parts of the implementation and docs. The project sends no telemetry; the redaction feature exists specifically so that provider keys and secrets do not leave your machine in plain text.

---

> **NassLab**（2 分） · 2026-11-02T19:20:21+08:00　
> https://i.redd.it/prdrk95ao6zh1.png
>
> APOGEE — screenshot of Orion with IAU (International Astronomical Union) constellation boundaries.
>
> Project Name: APOGEE
>
> Repo: [https://github.com/Nx-Nass/APOGEE](https://github.com/Nx-Nass/APOGEE)
>
> Description: A small sky atlas for exploring stars, nebulae, pulsars, supernova remnants and black holes. It runs offline from one HTML file, and I'm still polishing it.
>
> Deployment: Download index.html and open it locally, or serve that file from any static web server. No backend, database, account or Docker setup is needed; the required catalogues are embedded.
>
> AI involvement: I used AI coding assistance during development, and I'm continuing to review and refine the result.

---

> **wouek**（2 分） · 2026-11-02T20:50:48+08:00　
> * **Project Name:** CartVibe
> * **Links:** [GitHub](https://github.com/wouekk/cartvibe) · [Live Demo & Site](https://cartvibe.app/) (resets, nothing saved)
> * **Description:** A self-hosted vibe-coded family app for live-syncing shopping lists, receipt scanning, and household budgeting (groceries, bills, leisure) built for my own use. It's a fork of ReceiptWrangler which was a bit too complex for my personal use.
>    * **Shopping & Receipts:** Live-synced lists across phones, recipe imports, and photo/PDF receipt extraction with exact-cent math validation.
>    * **Budget & Extras:** Monthly goals, impulse-buy tracking (off-list items), Open Food Facts barcode scanner (Nutri-Score/NOVA), warranty reminders, multi-currency, 5 languages (I checked English and Polish by hand), and PWA install.
>    * **Optional AI:** Works 100% manually. You can bring your own key (Claude, Gemini, OpenAI, or local via Ollama/LM Studio) for receipt OCR and item health/category tagging. Retries if offline; costs <$0.01/receipt.
> * **Deployment:** [`ghcr.io/wouekk/cartvibe:latest`](http://ghcr.io/wouekk/cartvibe:latest) (Go API + nginx + SQLite in one container, plus Valkey). Needs just a compose file and two `.env` keys.  I've asked Claude to provide guides in the README and checked or Synology and VPS (Caddy/Litestream/restic).
> * **AI Involvement:** High, and I'd rather be upfront about it. This is a fork of [Receipt Wrangler](https://github.com/Receipt-Wrangler/receipt-wrangler) (AGPL-3.0, credit to Noah Hall & contributors) that I  modified (or rather completely reworked) using Claude Code for my own household (first release Oct 21, 2026). I run it daily on my Synology NAS and tested changes manually.
> *  It started as a hobby project using my Claude Pro trial, I ended up staying up until 3AM just watching Claude code for me and juggling limits. After 3 days I decided to get Max (you can see it by the number of Commits)
>
> Please feel free to use it and log any issues / request via Github I would greatly appreciate your feedback. Currently working on iOS app - hoping to monetize it in the future. SelfHosted stays free for eternity.

---

> **Awkward-Maize154**（1 分） · 2026-11-02T21:08:06+08:00　
> https://i.redd.it/5b6qkewe77zh1.png
>
> Project Name: PleiadesOrchestra
>
> Repo/Website Link: [https://github.com/francyfox/PleiadesOrchestra](https://github.com/francyfox/PleiadesOrchestra) · [https://pleiades.shalotts.site](https://pleiades.shalotts.site)
>
> Description:
>
> AI GOAP orchestrator (LLM + decision models) working with WebMCP/MCP. Use a webcomponent widget (framework agnostic solution) for your ecommerce shop website and connect to pleiades channel by token. The purpose of the widget is not to provide consultation, but rather to facilitate interaction with the website such as searching, comparing, analyzing, and so on. The project also enables commerce by providing restricted access to various channels. Use local models or openrouter provider. Includes an admin panel with a trace of every request and per-model costs
>
> Deployment:
>
> One command, Docker image [ghcr.io/francyfox/pleiades:](http://ghcr.io/francyfox/pleiades:)
>
> curl -fsSL [https://raw.githubusercontent.com/francyfox/PleiadesOrchestra/master/scripts/install.sh](https://raw.githubusercontent.com/francyfox/PleiadesOrchestra/master/scripts/install.sh) | bash
>
> Base stack 94 RAM idle. Working on Bun/Elysia/SvelteKit
>
> Docs: [https://pleiades.shalotts.site/docs/](https://pleiades.shalotts.site/docs/)
>
> License: AGPLv3
>
> AI Involvement:
>
> Runtime uses LLMs by design. Developed with heavy help from Claude Code. I own the architecture and review/test. Its proof of concept, so in the future i planning use less AI for this project. I dont have much time, webmcp announced in this mounth
>
> Status: Not ready for production. Active development

---

> **IntrepidListen5737**（0 分） · 2026-11-02T21:35:31+08:00　
> Project Name: Alexandria
>
> English README: [https://github.com/CatalpaShore/Alexandria/blob/master/README.en.md](https://github.com/CatalpaShore/Alexandria/blob/master/README.en.md)
>
> Demo: [https://catalpashore.github.io/Alexandria/](https://catalpashore.github.io/Alexandria/)
>
> I built Alexandria to organize and watch my own 18+ media collection, and decided to open-source it.
>
> You can add local folders or already-mounted NAS storage, scan existing files and sidecar metadata, browse the library, and play videos with subtitles. It also has playlists, viewing history, highlights, and a viewing desk for picking something to watch.
>
> It reads NFO and JSON metadata and supports external text subtitles such as SRT, ASS, SSA, and VTT. Playback compatibility depends on your browser and FFmpeg; image-based subtitles aren't supported yet.
>
> Deployment: Run from source or use the Docker Compose setup in the README. The online demo is read-only and uses non-adult films and mock viewing records. The project doesn't provide adult videos or download sources.
>
> AI involvement: I used Codex to help with development and testing. Codex also helped write this comment.
>
> I'd especially appreciate feedback on importing an existing library, playback, subtitles, and anything that makes the setup confusing.

---

> **TheRealTRexUK**（1 分） · 2026-11-02T21:53:27+08:00　
> Project Name: **Starboard**
>
> Repo/Website Link: [https://github.com/TheMightyTRex/starboard](https://github.com/TheMightyTRex/starboard)
>
> **Description:**
> Starboard is a lightweight dashboard for small home media servers. It shows every app on your server and whether it is running, and brings the day-to-day jobs of an \*arr stack into one place.
>
> The problem it solves: most dashboards either just show links, or use a lot of memory for what they do. Starboard uses about 20 MB of memory and almost no processor time while idle, so the server’s power goes to your apps. It is Python’s standard library and plain HTML, CSS and JavaScript: no database, no Node, no framework. Every piece of background work has a switch, and each setting says what it costs.
>
> https://i.redd.it/ieneetlqf7zh1.png
>
> **Features:**
>
> * Every app on one page, with whether it is running, its version and how fast it answers
> * Search Sonarr, Radarr, Lidarr and Readarr at once, and add what you find
> * Downloads from qBittorrent and SABnzbd, with speeds and your VPN’s state (Gluetun)
> * Download hours: downloads run only between the hours you set, with Pause and Resume
> * Coming up as a list or a calendar, with posters
> * Requests from Seerr, Jellyseerr or Overseerr, with Approve and Decline
> * Updates for each app’s container, with Update all
> * Storage charts: your pool by type (TV, films, books and more) with free space, each drive in the pool, space used over time with a forecast of when it fills, and the biggest series and films
> * System pages: overview, disk health with temperatures, monitor, network, and backup and restore
> * Alerts to ntfy, Gotify or a webhook when an app stops, a disk has a problem or space runs low, plus uptime history and a weekly summary
> * Jellyfin extras: free Live TV channels and guides, watch history import from Plex, Emby or another Jellyfin, and defaults for every user
> * Search for new apps: finds apps on your server and adds them, reading their API keys for you if you allow Docker access
> * Install apps: set up a media server in groups (Movies, TV, Music, Ebooks, Audiobooks, Comics and more). It writes a Compose file and shows it to you before anything starts
> * A set-up guide after install, an upgrade guide that asks only about what is new, and release notes in the app
> * Performance presets (Small server, Balanced, Everything)
> * Security: one password, rate limits on sign-in, checked host names, and API keys that never reach the browser
> * Accessible: built to WCAG 2.2 AA, with light and dark themes, larger text, high contrast and reduced motion. Works on phones
>
> **Coming soon:**
>
> * Migrate listening progress from Plex, Jellyfin or another Audiobookshelf into Audiobookshelf
> * Copying download clients, tags and naming from an existing Sonarr, Radarr or Lidarr into new ones
> * Pillow made optional, for 32-bit Raspberry Pi
> * How it helps: if you run a handful of apps on a small box, a NAS or an old PC, you get one place to see what is up, what is downloading and how full your disks are, without adding another heavy service.
>
> **Deployment:**
>
> Released as v0.5.3 (MIT licence). The README covers installing, updating, security and every setting.
>
> There is a Docker image for amd64 and arm64: ghcr.io/themightytrex/starboard. The arm64 build is for a Raspberry Pi 4 or 5 on a 64-bit system, though I have not tried it on a Pi myself yet. The repo has a ready-to-use Compose file, compose.image.yaml:
>
> `mkdir -p data`
>
> `docker compose -f compose.image.yaml up -d`
>
> `docker logs starboard # the one-time setup code`
>
> Then open http://:8095. The Compose file explains the optional extras (Docker access for updating apps, folders for the storage charts) as comments you can uncomment.
>
> Or install from source with the installer, which explains each step and asks before giving Starboard any access to your computer. Every kind of access is optional; say no and only that part is missing:
>
> `git clone` [`https://github.com/TheMightyTRex/starboard.git`](https://github.com/TheMightyTRex/starboard.git)
>
> `cd starboard`
>
> `./install.sh`
>
> Updating is docker compose pull for the image, or ./update.sh for the installer, which backs up your settings and goes back to the previous version if the new one does not start.
>
> **AI Involvement:**
>
> I planned out what I wanted to do and created a component library and design system to ensure it met my requirements. I created user Journys I needed and issues I wanted to solve. This was added to a task list for claude.
>
> Most of the code was written with Claude Code (Anthropic’s AI coding tool), working from my direction: I decided what it should do and how it should look, reviewed the changes, and tested every release on my own server before it went out. The security review was also AI-assisted: an independent review pass plus attacks on a throwaway copy, with the findings and fixes written up in the repo’s changelog. I am happy to answer questions about any part of it.

---

> **TheRealTRexUK**（1 分） · 2026-11-02T21:54:01+08:00　
> I am trying to automate and simplify an \*arr install for some friends and family. While there are other dashboard type apps, this one allows me to add and do things I want.
> [https://github.com/TheMightyTRex/starboard](https://github.com/TheMightyTRex/starboard)
>
> I have had a version of it running on my own server for a few months along with Homarr to see what I used the most. I ended up removing Homarr. Its set up for a Jellyfin stack but a migration from plex and other systems.
>
> I thought I would tidy it up, work on the UX and user flows and see if anyone else was interested.
>
> There are three main aims (one is not really of interest to others)
>
> * Add the items I wanted to a dashboard for small servers and make it as simple as possible.
> * Create a backup that would allow me to restore everything apart from media.
> * Keep its memory and cpu usage to a minimum.
>
> I am planning on using this for others so will be keep up to date (it will save me a load of hassle with family).

---

> **TheRealTRexUK**（1 分） · 2026-11-02T21:58:54+08:00　
> https://i.redd.it/d6m6edxpg7zh1.png

---

> **TheRealTRexUK**（1 分） · 2026-11-02T21:59:08+08:00　
> https://i.redd.it/dralcthrg7zh1.png

---

> **JakeHotdog**（1 分） · 2026-11-02T22:03:19+08:00　
> https://i.redd.it/ck5xo4mjh7zh1.png
>
> **Kvitok: self-hosted helpdesk with an AI agent that works with your backend’s data and proposes actions an operator approves**
>
> I built Kvitok for large real projects that get hundreds of support tickets a day. Our operators handled every one of them by hand: they looked the customer up in the admin panel, figured out what went wrong, found someone who could sort out a loyalty program issue, and so on.
>
> In Kvitok the agent finds the customer in your backend over a small HTTP protocol, reads their orders or receipts, drafts a reply and proposes actions like crediting points or issuing a coupon. The operator can talk to the agent right in the ticket and approves what makes sense, then the backend executes it. Nothing runs until a person approves it.
>
> Out of the box Kvitok knows nothing about your business, so one installation can serve a shop, a loyalty program and an internal tool, each in its own workspace. Your backend implements six signed endpoints and publishes a manifest: what data the agent can read, what actions it can propose, playbooks for typical requests and the domain knowledge it needs. The support team writes the policy (tone, what not to promise, when to hand over to a human), departments and routing rules in the UI. If you use Claude Code, there’s a plugin that studies your backend and sets all of this up for you.
>
> It runs in Docker Compose with Postgres and Redis and works with any OpenAI-compatible endpoint, including Ollama and vLLM. The demo stack comes with a fake LLM and a simulated coffee shop backend, so you can try it without an API key. The core is AGPL-3.0 and the protocol is MIT.
>
> If you handle customer support and could use something like this, I’d like to hear what you think, especially what’s missing.
>
> [https://github.com/Rogue85/kvitok](https://github.com/Rogue85/kvitok)

---

> **Fair-Bottle2749**（3 分） · 2026-11-02T22:32:50+08:00　
> **Project Name:** BeforeUp
>
> **Repo:** [https://github.com/BreezeDelegate/beforeup](https://github.com/BreezeDelegate/beforeup)
>
> I've been working on a small Docker Compose tool called BeforeUp and thought some people here might find it useful.
>
> The idea is pretty simple: check a Compose project before deploying it, without actually starting or modifying anything.
>
> It looks for things like ports already in use, missing bind mount paths, disk space warnings and differences between your Compose file and what's already running.
>
> One thing that came up during testing was that Compose can accept a configuration even when something goes wrong at startup.
>
> For example, certain combinations of `restart: always` and `deploy.restart_policy` can silently leave a container with its restart policy set to `no`. I reproduced this with Compose 5.5.0 through 5.6.1, and the latest BeforeUp release (0.4.4) now warns about it.
>
> **Installation:** It's a local Linux CLI, not another service or dashboard to host. There are `.deb` packages and portable Linux binaries in the GitHub releases.
>
> After installing it, you can run:
>
> `beforeup check -f compose.yaml`
>
> There's also a `compare` command for checking proposed changes against an existing stack. Nothing gets deployed or modified.
>
> **AI involvement:** I used AI assistance during development. The project is open source, and the release has been tested with Go regression tests, race checks and actual Docker Compose scenarios. I'm not claiming it's been tested on every setup.
>
> It's still a fairly new project, so I'd be especially interested in hearing from people running different homelab configurations.
>
> If you give it a try, I'd love to know whether it catches anything useful, produces noisy warnings or misses something obvious.
>
> https://i.redd.it/8yid7i9qm7zh1.png

---

> **Crafty_Respect4928**（1 分） · 2026-11-02T23:52:22+08:00　
> **Project Name:** NeatRead- knowledge contents platform
>
> **Website:** [https://neatread.net](https://neatread.net)
>
> **Description:**
>
> I'm the solo founder of NeatRead, a new project I've been building and hosting over the past two months.
>
> The idea behind NeatRead is simple: create a place where independent writers and knowledge creators can publish and share their work, while giving readers an easier way to discover useful content.
>
> Some of the things I'm working on:
>
> * **Topic-based discovery:** Organize content into categories so readers can discover things they're interested in.
> * **Free and paid content:** Let creators decide whether their articles are free or available to paying readers.
> * **Independent publishing:** Give creators another place to share their knowledge without relying entirely on social media algorithms.
> * **Reader experience:** Keep the platform focused on reading and discovering valuable content.
>
> I'm building NeatRead because I think there's room for a simpler publishing platform that connects independent creators with readers.
>
> It's still an early-stage project, and I'm actively improving it.
>
> I'd particularly appreciate feedback on:
>
> * Does the concept solve a problem you have as a reader or creator?
> * What features would make you want to use a platform like this?
> * What would make you choose it over Medium or other publishing platforms?
>
> I'm the person behind this project, so I'm happy to answer questions and discuss the technical and product decisions behind it.
>
> Thanks for checking it out!
>
> **Website:** [https://neatread.net](https://neatread.net)

---

> **Virtual_Bike_8782**（1 分） · 2026-11-03T02:42:56+08:00　
> **Project Name:** Ridealong
>
> **Repo/Website Link:** https://github.com/Christian-Gennari/ridealong
>
> **Description:**
>
> A real, logged-in browser for AI agents that runs on your own server. A live viewer lets you watch what they do and take over when they need you.
>
> I built it because my coding agents (Claude Code, Codex) kept getting stuck on anything without an API: dashboards, admin panels, anything behind a login. Headless browsers can't get past 2FA, and you can't see what they're doing. Ridealong runs Brave in a locked-down container with its own profile, so logins persist, and any MCP client can drive it.
>
> * **Live viewer:** watch every agent session from any device, including your phone.
> * **Handover:** when an agent hits a 2FA code or a CAPTCHA, the viewer shows a full-screen "Your turn" (plus push or ntfy). You do that step, press Hand back, and the agent carries on.
> * **Parallel sessions:** each agent gets its own tab.
> * **Site rules:** list sites (bank, registrar...) where agents must ask before clicking or typing.
> * **Any MCP client:** Claude Code, Codex, Cursor, Antigravity CLI, Hermes, or anything else that speaks MCP.
>
> **Deployment:**
>
> Linux + Docker:
>
>     git clone https://github.com/Christian-Gennari/ridealong
>     cd ridealong
>     ./ridealong up
>
> That pulls a prebuilt image (~350 MB, `ghcr.io/christian-gennari/ridealong`), prints your viewer link and connects the MCP clients it finds. The viewer stays on localhost by default. It picks up Tailscale automatically, and otherwise you reach it over an SSH tunnel. The README covers the rest, including the security trade-offs. It's your logged-in browser, so please read that part.
>
> **Where it's at:** I've used it daily for a few days and it already works well for me, but I've only tested it on my own Ubuntu 24.04 box. I'm looking for people who'd actually use something like this to try it, break it and tell me what's missing. If you'd like to help build it, you're very welcome.

---

> **Last-Bad-9788**（1 分） · 2026-11-03T05:12:31+08:00　
> **Project Name:** Simplixity
>
> **Repo:** [https://github.com/stneric/simplixity](https://github.com/stneric/simplixity)
>
> **Description:**
> A self-hosted research assistant, similar in spirit to Perplexity, but built around trust. You ask a question, it searches through your own SearXNG instance, reads the pages and writes an answer where every claim cites a numbered source. A second pass then checks each cited sentence against its source and marks it as supported, partly supported or not supported. Quotes and numbers are also compared with the source text directly. It's still an LLM and won't always be right, but it tells you when a claim isn't backed by its source.
> Also included: OpenRouter, Groq or fully local models (Ollama / LM Studio), a science lens (PubMed, arXiv, OpenAlex…), a literature workflow with BibTeX export, chat with your PDFs with page-level citations, and a transparency footer showing which models ran and which search engines answered or refused (plus a nerd mode with token usage).
>
> **Deployment:**
> Docker Compose (app, Redis, SearXNG). Clone, copy .env.example, set your API key and SearXNG secret, docker compose up -d. Quickstart and docs are in the README. AGPL-3.0, BYOK.
> Known limitation: on a VPS some search engines throw CAPTCHAs at datacenter IPs. On a home network or behind a residential proxy that's much less of an issue.
>
> **AI Involvement:**
> I used claude code mainly for writing tests and ui work. The underlying architecture is prototyped by me and coded by hand. Claude fixed any issues I made and added comments for better readability. All in all, claude made the project “public ready”.
>
> Feedback is very welcome, especially cases where the citation check gets it wrong.

---

> **SnooOwls5452**（1 分） · 2026-11-03T05:34:37+08:00　
> \*\*Project Name:\*\* Athene Reader
>
> https://i.redd.it/dsj52jrxp9zh1.png
>
> \*\*Repo/Website Link:\*\* [https://theadipost.com/athene/](https://theadipost.com/athene/) (guides: [https://theadipost.com/athene/docs/](https://theadipost.com/athene/docs/))
>
> \*\*Description:\*\*
>
> Hey everyone! After months of searching, i never found a beautiful, feature packed reader that actually worked with my calibre server. Everything out there fell short of my expectations, so I made one for myself. Then I decided to share it for **free** and \[posted it on r/ebooks\]([https://www.reddit.com/r/ebooks/comments/1wwrgce/i\_built\_a\_calibre\_ebook\_app\_for\_myself\_and\_want/](https://www.reddit.com/r/ebooks/comments/1wwrgce/i_built_a_calibre_ebook_app_for_myself_and_want/)). People asked for Android, page curl, French and Italian voices, the app in other languages and Kobo sync, and over the last month I built all of it. It's still just me working on it, and your feedback is what's been shaping it.
>
> If you self host your books you're probably already running calibre's content server or calibre-web. It's pretty much Plex for ebooks. The one thing that's always been missing is a really good app to read from it on your phone, and that's what I want Athene to be. The best calibre client out there.
>
> What it does with calibre:
>
> \- Connects to calibre's content server or calibre-web, login and plain http on your home network both work
>
> \- Browse by author, series, tags or A-Z with covers, and download one book or a whole bunch at once
>
> \- Highlights and notes sync both ways with calibre's content server
>
> \- Your reading progress goes into a calibre column you pick, and books get marked read when you finish
>
> \- Your calibre tags and series show up in the app
>
> It also works with the rest of your setup:
>
> \- Any OPDS catalog
>
> \- KOReader sync with any KOSync server. If you want highlights and notes synced too, I made a small server for it, athene-sync (Docker, AGPL): [https://github.com/adityasreedhar/athene-sync](https://github.com/adityasreedhar/athene-sync)
>
> \- Ask the Owl questions about the page you're on with your own Ollama server (or an API key)
>
> And the reading side: highlight, type or draw notes, all your notes in one Notebook, read aloud with a natural voice, any paper color and any Google Font, and much more.
>
> No account, no ads, no in app purchases and no tracking. Your books stay on your phone unless you send them to your own server. Just so you know, the app itself isn't open source, only the sync server is.
>
> \*\*Deployment:\*\* Nothing to host for the app, just download it:
>
> \- iPhone/iPad: [https://apps.apple.com/app/id6811711454](https://apps.apple.com/app/id6811711454)
>
> \- Android: [https://play.google.com/store/apps/details?id=com.aditya.athene](https://play.google.com/store/apps/details?id=com.aditya.athene)
>
> Then point it at your calibre server, OPDS feed, KOSync server or Ollama. The guides link above walks you through each one.
>
> \*\*AI Involvement:\*\* - How I utilized a hybrid approach in development?
>
> * Me: high level spec planning, system implementation, integrating sync, UI/UX design - attention to little details
> * Claude: Research on how to integrate sync and calibre connection, stress testing, edge case testing, assisting with bug fixing, code review
>
> Would love to hear what you think and what you'd want it to connect to next, thank you!

---

> **Important_Pomelo_407**（1 分） · 2026-11-03T06:05:47+08:00　
> Created a demo for you using OpenDemo https://github.com/yasirwhite/OpenDemo.
>
> I opened a PR and added it to your README too: https://github.com/LibrePaper/librepaper/pull/88.
>
> https://github.com/yasirwhite/OpenDemo/releases/download/showcase-media/librepaper-demo.mp4

---

> **Mattyhuunter**（2 分） · 2026-11-03T06:58:59+08:00　
> **Project Name:** pvewarden
>
> **Code:** [https://github.com/matousfiser/pvewarden](https://github.com/matousfiser/pvewarden)
>
> I kept forgetting to update the VMs and containers in my Proxmox homelab, so I made pvewarden. It’s an MCP server that lets an AI assistant check for updates and install them or reboot the guest. In its Proxmox-backed setup, updates take a snapshot first by default.
>
> In the standard setup, it uses a pool-limited Proxmox API token and a restricted per-guest SSH key. The AI assistant only gets a fixed set of MCP tools through pvewarden, not a general shell. I’ve only tested it on my own PVE 9 setup so far, so I’d be curious if it works for anyone else.
>
> **It’s early-stage, so please try it only on a non-critical setup.**
>
> **AI disclosure:** I designed the architecture and how it should work; Claude and Codex did the coding.

---

> **supachalupaa**（2 分） · 2026-11-03T08:43:38+08:00　
> Project Name: PulsHealth
>
> Repo/Website Link:
>
> [https://github.com/PulsHealth/pulshealth](https://github.com/PulsHealth/pulshealth)
>
> [https://pulshealth.com](https://pulshealth.com)
>
> Description:
>
> Hey, I’m Sean, the solo developer behind PulsHealth. I wanted to use my Apple Health data in hobby projects, but getting it out of my phone and keeping it updated was a pain. So I built an open-source iPhone app and backend to sync it to a server I control.
>
> The backend uses PostgreSQL with TimescaleDB. Once your data is there, you can query it with SQL, build Grafana dashboards, access it through a read-only API, or use it in whatever project you want.
>
> Deployment:
>
> Run the self-hosted Docker stack and pair your phone. Setup instructions: [https://github.com/PulsHealth/pulshealth/blob/main/docs/setup.md](https://github.com/PulsHealth/pulshealth/blob/main/docs/setup.md)
>
> You can build the iOS app yourself or use the App Store version linked on the website. The self-hosted backend is currently pre-release (0.x).
>
> If you try it, I’d love to hear how setup went. And if you build something with your data, please share it!

---

> **Sensitive_Volume5296**（2 分） · 2026-11-03T09:37:52+08:00　
> Project Name: MiniDeck
>
> Repo/Website Link: [https://github.com/zakijss/MiniDeck](https://github.com/zakijss/MiniDeck)
>
> Description: Open-source apps that turn a Miyoo Mini Plus (a small Linux handheld running Onion OS) into a pocket client for your self-hosted services. I wanted a glanceable view of my servers that isn't my phone. The ones that talk to self-hosted services:
>
> \- MiniRack: live CPU, memory, disks and temperatures from Glances (one machine) or a Beszel hub (all of them), and why a machine is down.
>
> \- MiniTape: a Navidrome / Subsonic player. Caches whole songs on the SD card so a Wi-Fi drop doesn't cut the song, keeps playing in the menu, synced lyrics, scrobbles to Navidrome, [Last.fm](http://Last.fm) and ListenBrainz.
>
> \- MiniScale: a Tailscale client for the device, so the other apps reach your servers away from home without opening ports.
>
> \- MiniPulse: a speed test against Cloudflare or your own LibreSpeed server.
>
> \- MiniRadar: devices on your network, and Wake-on-LAN.
>
> There's also an app store (MiniMart) that checks every download against a pinned SHA-256 and updates everything with one press. Logins and keys are encrypted on the card with a per-device key. MIT licence, written in Go, no telemetry.
>
> Deployment: Released and ready to download from GitHub Releases. Nothing new to host: the apps run on the handheld and connect to services you already run (Glances, Beszel, Navidrome or any Subsonic server, LibreSpeed, Tailscale). To install, unzip [minideck-all.zip](http://minideck-all.zip) from the latest release onto the SD card, or install just MiniMart and add the rest from inside it. Each app's README covers setup, and each app asks for its server address on first launch, so there are no config files to edit. Needs a Miyoo Mini Plus with Onion OS 4.4 and Wi-Fi. No Docker image, since nothing runs server-side.
>
> AI Involvement: About 70% of the code was written with AI (Claude). I designed the apps, reviewed the code and tested every release on my own Mini Plus. Every app has unit tests and runs CI on each change.
>
> https://i.redd.it/fm5r75x4xazh1.jpeg

---

> **mrtdlgc**（1 分） · 2026-11-03T10:04:37+08:00　
> **Project Name:** Subtitle Foundry
>
> **Repo:** https://github.com/mrtdlgc/subtitle-foundry — AGPL-3.0-only.
>
> **Description:** A self-hostable subtitle workbench with configurable transcription, alignment, context-aware translation and video/waveform review. Start with local media, a YouTube URL or existing subtitles. Review and edit the output, persist corrections and export SRT/ASS. Matching checkpoints let you reuse completed processing stages.
>
> I'm the developer and a former translator/subtitler/interpreter. I'm not making money from this, and I'll keep maintaining it. The purpose is to help films and other material reach a global audience when usable subtitles would otherwise be missing. It brings state-of-the-art (SOTA) speech and language tools into a modular workflow; I haven't published a comparative benchmark for the complete pipeline.
>
> **Deployment:** The repo includes a Dockerfile, Compose configuration and a deployment guide. Build locally with Docker Compose, persist /data, and configure APP_PASSWORD and PUBLIC_ORIGIN. For local browser access, add a Compose override publishing 127.0.0.1:3000:3000; the base Compose service doesn't publish a host port. For a VPS, use the deployment guide's reverse-proxy/HTTPS setup. The default cloud workflow doesn't require a GPU. The source and guides are available now; I recommend checking a short clip before queuing a film.
>
> **What is local vs cloud:** You host the application and its job/correction storage. Local-file playback and waveform work stay in the browser; extracted audio/subtitles can be sent for processing. The default ASR route is cloud ElevenLabs Scribe v2, and the translation connections use cloud models. This is not a fully offline pipeline. Optional local ASR exists, but the default image does not include the optional ML stack. Provider charges/allowances are separate from the free app.
>
> Personal installs can use their own Codex/Claude Code/Grok Build subscription connections where available, or explicit API credentials. A shared hosted service uses per-user credentials; it should not share the operator's subscription login.
>
> **AI involvement:** I used Codex while building the project, and this comment was drafted with Codex assistance. ASR and LLM translation are also product features. My film testing has mainly used ElevenLabs plus Codex for Turkish-to-English and Ukrainian-to-English; other provider combinations have not all had equivalent film testing.
>
> Installation and provider documentation are linked from the README.

---

> **GetSerafin**（1 分） · 2026-11-03T14:09:53+08:00　
> # Just wanted to share my new iOS client I have been working on for a couple months, would love any feedback or support
>
> I love Jellyfin, let me start with that. I used to be a big Plex supporter and then gradually it just went down the drain. Jellyfin may lack the polish of Plex but it is genuinely the best way to host your own media once you get it set up correctly. My love of self hosting slowly transformed into a desire to help contribute back to the community that I have assimilated into over the last 2 years of my life.
>
> All of this being said I just wanted to post here to share a passion project of mine I have been working on for a couple months that is finally available on the iOS App Store. That being Serafin, a brand new Jellyfin client that is designed to feel exactly like an Apple-made application, not a janky third party application, while BEING FREE. These paid for clients, "premium" clients piss me off, why tf are you trying to make money off of something that was always free in the first place...
>
> I plan on maintaining this application for years to come, and want to give back to the community the best I can. I don't ever plan on monetizing any aspect of this and truly do want to make this the best possible Apple native Jellyfin client I can. I have fully open sourced my code linked here (please don't judge my Claude usage it makes programming significantly easier, but I get the hate believe me): [https://github.com/timsullivan2019/serafin](https://github.com/timsullivan2019/serafin)
>
> The app is barebones for now since I wanted to focus on getting the design language right, but I have a roadmap where I plan to add many more features to genuinely make this the best possible client such as:
>
> * Downloads (just waiting for App Store approval for offline play update as we speak)
> * Jellyseerr / Seerr request support directly in app
> * Automatic switching between a server's local and remote address
> * Music with CarPlay, Live TV, SyncPlay, widgets, remote control of other sessions
> * Dolby Vision profile 7, DTS and TrueHD decoded on device, ASS subtitle rendering
> * A stable, fully featured open-source Apple TV client
>
> I want to do all this and make sure it is free for everyone forever. I just genuinely want to make the best application possible for the Apple ecosystem Jellyfin community. Serafin is 100% coded in Swift and forever will be. If you want to join the community feel free to download my app at the link here: [https://apps.apple.com/us/app/serafin-for-jellyfin/id6818960899](https://apps.apple.com/us/app/serafin-for-jellyfin/id6818960899)
>
> Also too thank u to everyone on this subreddit, I have learned so much about self hosting and a lot of it comes from here <3

---

> **ElderHare**（2 分） · 2026-11-03T15:23:11+08:00　
> **Project Name:** Reelix
>
> **Repo/Website Link:**  [https://www.github.com/demonzoned/Reelix](https://www.github.com/demonzoned/Reelix)
>
> **Description:**
>
> Reelix is a single self-hosted app that replaces Radarr, Sonarr, Prowlarr, Readarr, Lidarr and Jellyseerr. It's one Rust binary with one database, one login, one web UI and one API, so there are no API keys to wire between apps and nothing to keep in sync.
>
> https://i.redd.it/9mm8cui0nczh1.png
>
> \- Library management: movies, TV, ebooks, audiobooks and music, with monitoring, search, automatic grabs, imports, renaming and hardlinks.
>
> \- Indexers: Torznab, Newznab and Cardigann-style YAML definitions, with FlareSolverr support. Reelix can also serve all its indexers to other apps as one combined indexer.
>
> \- Download clients: qBittorrent, Transmission, Deluge, rTorrent, SABnzbd, NZBGet and blackhole folders, plus direct Spotify and YouTube downloads.
>
> \- Requests: a discovery and request portal with approvals and quotas. Users can sign in with Plex, Jellyfin, Emby or OIDC.
>
> \- Integrations: Plex, Jellyfin, Emby, Audiobookshelf, Kavita and Navidrome, plus notifications to Discord, Telegram, ntfy and others.
>
> \- Migration: a one-click importer from an existing \*arr stack, and \*arr-compatible APIs so Homepage, Bazarr, LunaSea and Recyclarr keep working.
>
> **Deployment:** Version 0.4.0 is released, with prebuilt binaries for Windows and Linux on GitHub Releases (https://github.com/demonzoned/Reelix/releases) and a Docker image at ghcr.io/demonzoned/reelix:latest. The README has a docker-compose example, setup steps for Windows, Linux and building from source, and a first-run guide. Docker setup is a single container with one /data mount (so hardlinks work) and port 7700.
>
> * **AI Involvement:** Heavy.  Claude is a collaborator on the project.  AI did the coding work for me.

---

> **PawLawArt**（1 分） · 2026-11-03T15:32:59+08:00　
> https://i.redd.it/rqce7ywepczh1.jpeg
>
> Built an open-source async standup app you can self-host (Docker, AGPL-3.0)
>
> Our team's standups kept landing at a bad hour for someone, so I built a self-hosted tool to skip the live call entirely.
>
> **How it works:**
>
> 1. Each person records a \~2-minute video/audio update when their day starts (or types it).
> 2. The audio is transcribed, and an LLM extracts **Yesterday / Today / Blockers**.
> 3. It remembers your previous update, ticks off completed tasks, and tags mentioned teammates.
> 4. The team reads or watches the check-ins asynchronously in their own morning.
>
> **Self-Hosting & Tech Stack:**
>
> * Single `docker-compose` setup: Postgres, MinIO (video/audio storage), Node/App engine, lightweight scheduler for reminders, Caddy for HTTPS, and automated daily DB backups.
> * **AGPL-3.0 License** — All features unlocked out of the box, zero telemetry, no license keys, no limits.
>
> **Current Caveats (v0.1):**
>
> * **Auth:** Magic links currently route through Resend (or Google OAuth). Plain SMTP is not implemented yet.
> * **AI Provider:** Uses Groq (Whisper + Llama) for transcription and drafting. Without an API key, video uploads still work and team members type check-ins manually. Local Whisper is on the roadmap (the provider is interface-driven).
> * **Privacy & Architecture:** Media files upload directly from the browser into your MinIO bucket (bypassing the app server). Transcripts and summaries are encrypted at rest in Postgres.
>
> *Full Disclosure:* A significant chunk of the codebase was generated with Claude Code (visible in the Git history). I review, test, and run everything myself, but I prefer full transparency.
>
> * **GitHub:**[https://github.com/codeaz-org/asincly](https://github.com/codeaz-org/asincly)
> * **Setup Guide:** `docs/DEPLOYMENT.md` inside the repo (includes a hosted demo link if you just want to test the UI).
>
> **A question for team leads & devs:** Would your team actually record quick 2-minute videos, or would everyone inevitably default to typing? That’s the core assumption I’m looking to validate.

---

> **umur-yavuz**（1 分） · 2026-11-03T18:39:19+08:00　
> https://i.redd.it/w2f9o780mdzh1.jpeg

---

> **umur-yavuz**（1 分） · 2026-11-03T18:39:27+08:00　
> https://i.redd.it/flk5dgr1mdzh1.jpeg

---

> **yusufyildiz86**（1 分） · 2026-11-03T18:43:20+08:00　
> Project Name: whichphp
>
> Repo/Website Link: [https://github.com/yusufyildiz34/whichphp](https://github.com/yusufyildiz34/whichphp)
>
> (daily index: https://yusufyildiz34.github.io/whichphp/)
>
> Description: Checks whether the PHP inside a container image is actually patched for PHP2Shell (CVE-2026-109618 and CVE-2026-109619), without running the image. If you run Nextcloud, WordPress, Joomla, MediaWiki or anything else PHP-based in a container, the October 21 fixes only reach you if the tag you pull was rebuilt and you recreated the container. php -v doesn't settle it: distros like Ubuntu backport the fix without changing the version, and the official php images build PHP from source, which some scanners don't see. whichphp reads the image with Syft, matches with Grype, and adds the PHP-specific rules (distro and packager backports, EOL branches, the session.upload\_progress setting), with the evidence for every verdict. There's also a daily index of 90 popular PHP app image tags with an Atom feed per tag. Right now 21 of them still ship pre-fix PHP, mostly EOL releases and images nobody maintains anymore.
>
> Deployment: It's a CLI, not a service. Install it with "go install github.com/yusufyildiz34/whichphp/cmd/whichphp@latest" or grab a release binary (checksums and signed build provenance included). It needs Syft and Grype on your PATH. Then run "whichphp image ". There's also a GitHub Action for CI and a "whichphp cluster" mode for Kubernetes. The README covers install and usage.

---

> **TheRealTRexUK**（1 分） · 2026-11-03T19:07:21+08:00　
> **Project Name:** Snaglist
> **Repo/Website:** [https://github.com/TheMightyTRex/snaglist](https://github.com/TheMightyTRex/snaglist)
>
> https://i.redd.it/7jw4sv7jqdzh1.png
>
> Hey, I thought I would share this. I have been doing some work on a few apps for my own use and found that it could be annoying sometimes to describe issues with UX and functionality and having to dive into the inspect element to get what I want.
> This was also a nightmare where friends were trying to describe things.
>
> I created a quick "Report an issue" item to add to websites - there is no reason it couldn't be adapted for other things.
>
> [](https://preview.redd.it/rraj3104qdzh1.png?width=1280&format=png&auto=webp&s=d1541c5fc97da9170cdf2300011d28234f621856)
>
> **Description:**
> Feedback for any website or app. People report bugs and UX problems, suggest features and improvements, record a series of steps, or check a page for accessibility problems. Each report is tagged with the page and the part of it, carries the technical details needed to act on it, and keeps no personal information.
>
> A snag list is a list of the small faults to fix before a job is finished. Snaglist adds a Send feedback button to your site. People choose what to send, show one thing on the page or record what they do, answer a few questions, check exactly what will be sent, and send it as a GitHub issue, an email or a post to your own server.
>
> **Deployment:**
> [Try the demo](https://themightytrex.github.io/snaglist/) · [Set it up for your site](https://themightytrex.github.io/snaglist/configure.html) · [Help centre](https://github.com/TheMightyTRex/snaglist/blob/main/docs/README.md) · [Prompts for AI assistants](https://github.com/TheMightyTRex/snaglist/blob/main/docs/AI-PROMPTS.md)
>
> * One file, no libraries: about 100 KB, or 33 KB when your server compresses it. No build step.
> * Simple to add and to remove: one script tag, or the [set-up tool](https://themightytrex.github.io/snaglist/configure.html) writes the code and one prompt for your AI assistant. Removing it leaves nothing behind.
> * Anonymous by design: never what people type, no cookies, no query strings; emails, phone numbers, addresses and keys are replaced. People are shown the whole report before it goes, and can take parts out.
> * Accessible: keyboard first, 44px targets, a visible focus ring, reduced motion, forced colours, and it follows the page's text size. Light by default, or dark, or the same as the device.
> * Any language: British or US English built in; give your own text for any other language.
>
> I thought it might be useful for people when testing, especially with others.
> [https://github.com/TheMightyTRex/snaglist](https://github.com/TheMightyTRex/snaglist)
>
> AI: This was designed for people who use AI to help get feedback and record issues easier. Its part of my Content Design system [https://themightytrex.github.io/design-system/gallery.html](https://themightytrex.github.io/design-system/gallery.html)

---

> **TheRealTRexUK**（1 分） · 2026-11-03T19:14:03+08:00　
> u/ElderHare  Hey, what is the general memory and cpu usage? Have you done any security checks on it? What features are missing compared to a full stack?
>
>  I am building a way to deploy an \*arr stack easily as a few friends have asked me about it - I want it to be as simple to manage as possible for servers with low power and one or two users. I would be interested in looking as it as a choice for deployment.
> [https://github.com/TheMightyTRex/starboard](https://github.com/TheMightyTRex/starboard)

---

> **Curious_Ad9388**（1 分） · 2026-11-03T20:29:38+08:00　
> **Project Name:** kite
>
> **Repo/Website Link:** [https://github.com/SiraBet/kite](https://github.com/SiraBet/kite)
>
> **Description:**
>
> https://i.redd.it/5h8rnq3j5ezh1.png
>
> A self-hosted patch manager for Linux and Windows that takes a snapshot of every machine before patching it. I got tired of patching my homelab with a mix of Ansible playbooks and hope, so I built a small web console to do it properly.
>
> * **Snapshot before every run:** uses Proxmox snapshots or dnf history, with one-click restore if something breaks.
> * **No SSH, no inbound ports:** a small agent on each machine checks in with the controller and does the work locally.
> * **Linux and Windows:** RHEL, Rocky, Alma, Oracle, Debian, Ubuntu, and Windows Server through Windows Update.
> * **Fleet tools:** schedules, update holds and pins, Docker Compose updates, a Proxmox topology map, and an audit log of every run.
> * **Optional tickets and approvals**, off by default.
>
> **Deployment:**
>
> The controller runs as a single Docker Compose stack with a SQLite database:
>
>     git clone https://github.com/SiraBet/kite.git
>     cd kite/controller && docker compose up -d
>
> Then enrol each machine from **Fleet → Enroll** in the console: a one-line command for Linux, or an installer for Windows.
>
> * Needs Docker with the Compose plugin. A non-Docker install is also documented.
> * Proxmox is optional. Without it, Linux rollback uses dnf history.
>
> This is 1.0, so feedback and bug reports are very welcome. I’d especially like to hear how it does on setups other than mine. PRs welcome.
>
> **AI Involvement:**
>
> A lot. AI wrote nearly all of the code. I directed it, tested it on my own homelab, and fed back bugs and changes.

---

> **Regrave**（1 分） · 2026-11-03T20:58:18+08:00　
> Project name: Aperture
>
> Website: https://aperture.sh/
>
> Description: I'm Regrave, Aperture's maintainer. It's a hosted control panel for game servers on your own Linux machine. You can give friends separate browser logins and permissions for a specific server instead of sharing SSH. The panel and optional gameplay relay are free and intended to stay free; optional off-site backups are the only planned paid feature.
>
> Deployment: The panel itself isn't self-hostable. You connect your own Ubuntu 22.04/24.04 or Debian 12/13 machine using official Calagopus Wings and Docker. Installation needs root or sudo, and linking the host grants Aperture privileged management access. It won't replace active Wings. For this public beta, a spare VM and a new Paper world are the smallest trial. [Setup requirements](https://aperture.sh/docs) and [actual panel screenshots](https://aperture.sh/?website=1#panel) are available before signup.
>
> AI involvement: Substantial use for Aperture-specific implementation, debugging, tests and documentation. Calagopus is the upstream panel.

---

> **Phoenix_Tech_MSP**（1 分） · 2026-11-04T00:04:23+08:00　
> \*\*\[Phoenix-Nexus\] Self-hosted ITAM + lightweight CMDB for SMBs\*\*
>
> \- \*\*What it is:\*\* A lightweight open-source (AGPL-3.0) platform combining IT Asset Management, configuration items (CMDB), and license tracking (SAM) designed for SMBs tired of spreadsheet chaos.
>
> \- \*\*Features:\*\* Hardware check-in/out, QR label printing, single-direction CMDB sync, renewal alerts, trilingual UI (EN/FR/NL).
>
> \- \*\*Status:\*\* Public Alpha (v0.1.0). Local-first / Docker Compose.
>
> \- \*\*GitHub:\*\* [https://github.com/PhoenixTechMSP/phoenix-nexus](https://github.com/PhoenixTechMSP/phoenix-nexus)
>
> \- \*\*Live Demo:\*\* [https://demo.phoenix-tech.be](https://demo.phoenix-tech.be) (demo credentials pre-filled, nightly DB reset)
>
> Feedback and feature suggestions welcome!

---

> **HeronObvious5452**（1 分） · 2026-11-04T00:21:19+08:00　
> Project Name: **k-lani-link**
>
> Repo/Website Link:  [https://github.com/MarvKalani/k-lani-link](https://github.com/MarvKalani/k-lani-link)
>
> **Description:**
>
> I built k-lani-link: An encrypted bridge to use your self hosted private AI models from almost anywhere
>
> Public cloud AI is often banned on confidential client work, and corporate firewalls block custom ports and SSH tunnels.
>
> I built k-lani-link to solve this. It is an encrypted bridge connecting your self hosted AI on your work PC directly to where you need it (home GPU, lab server, or cloud VM) using permitted HTTPS and WebRTC with end-to-end encryption.
>
> Key points:
>
> * Tool-agnostic: Works with any OpenAI-compatible client (Cline, OpenCode, Cursor, scripts).
> * Backend-agnostic: Routes to any engine (Ollama, vLLM, Basalt, llama.cpp). Switch models on the fly without dropping the tunnel.
> * Privacy & Security: Written in Rust. Docker isolation via Unix sockets, no telemetry, zero prompt logging.
> * Pricing: Free for production under $100k annual revenue, or €4.99 one-time. No subscriptions.
>
> Links:
>
> * GitHub: [https://github.com/MarvKalani/k-lani-link](https://github.com/MarvKalani/k-lani-link)
> * Video Demo: [https://youtu.be/i1AlVccsPgk](https://youtu.be/i1AlVccsPgk)
>
> **Deployment:**
>
> Portable binaries are available for Windows, macOS, and Linux, alongside the Docker setup. Feedback and questions are welcome!
>
> **AI Involvement:** Yes fo course, Claude Opus 5.5 extra high, Gpt6 Astra, Gpt6.1 Sol Max
>
> https://i.redd.it/sqmcvk84bfzh1.jpeg

---

> **HeronObvious5452**（1 分） · 2026-11-04T00:22:20+08:00　
> For anyone wondering about the relay architecture and privacy:
>
> You don't have to rely on a central server. You can **bring your own relay**:
>
> * **PHP / WordPress:** A single lightweight PHP script (`deploy/php-relay`) you can drop onto any cheap web space or existing WordPress site.
> * **Cloudflare Worker:** Serverless relay deployment via `deploy/cloudflare-relay`.
> * **Self-hosted Rust relay:** A standalone binary you can run on your own VPS.
>
> Even when falling back to HTTPS through a relay, the traffic remains end-to-end encrypted between your two machines—the relay only carries ciphertext and has no access to prompts or responses.
>
> If you have questions about the WebRTC ICE negotiation, proxy setups, or Docker socket isolation, let me know!

---

> **MiserableComputer161**（1 分） · 2026-11-04T00:45:03+08:00　
> >**PLAID: a self-hosted Plex replacement, no account, watch together built in**
> >
> >I got tired of Plex: a [plex.tv](http://plex.tv) account just to watch my own files, and remote streaming now behind a paid pass. Jellyfin is great, but I wanted one thing neither does well: watching a movie *together* with friends, each on their own screen. So I’m building PLAID, solo, MIT licensed. It’s early (alpha), so expect rough edges.
> >
> >**What works today**
> >
> >
> >
> >**Coming next: Plaid Party.** The server holds the clock, each person gets a stream for their device (4K on the TV, 720p on a phone), and drift is fixed by nudging playback speed instead of jumping. Chat, reactions, guests join from a link with a first name.
> >
> >**Built with AI, on purpose.** I write it with Claude Code and I’m open about it. Every feature goes through a written intent, spec and plan (public in `sdlc/`), and CI installs the real `.deb` in a systemd container and plays a file end to end. Judge the code yourself.
> >
> >**Looking for testers and contributors** (Android / Android TV, library sharing, anything on the roadmap).
> >
> >Repo: [https://github.com/gh-prim/plaid](https://github.com/gh-prim/plaid) · Site: [https://getplaid.tv](https://getplaid.tv)

---

> **finesseserver**（1 分） · 2026-11-04T01:45:35+08:00　
> **Project Name:** Finesse
>
> **Repo/Website Link:** https://github.com/CoffeeCC/finesse (Discord for help and feedback: https://discord.gg/G4RfBMytJg)
>
> **Description:**
> Finesse is a free, MIT-licensed app that sets up a whole home media server in one go: Jellyfin, Sonarr, Radarr, Lidarr and Prowlarr, already wired together, plus its own request page. The idea is search, add, watch. Someone at home searches for a show, adds it, and it shows up ready to play, without you having to be the household IT department.
>
> I built it because every time I set up Jellyfin and the arr stack for family, the setup itself was the hard part: getting paths, API keys and download clients to agree with each other. Finesse does that part and keeps the stack updated afterwards. If you already run Jellyfin or the arrs, there's an adopt mode so you don't have to start over.
>
> It's a front end and installer, not a content source. It ships with no content and no indexers. Current release is v3.2.7 (native Windows installer still, no Docker Desktop).
>
> **Deployment:**
> - Windows: a normal installer, no Docker Desktop or WSL needed: https://github.com/CoffeeCC/finesse/releases/latest/download/FinesseSetup.exe
> - Linux (x86-64 or ARM64): `curl -fsSL https://raw.githubusercontent.com/CoffeeCC/finesse/master/install.sh | bash`
> - Docs are in /docs in the repo.
>
> **AI Involvement:** Yes, so here it is plainly. I used AI coding assistants heavily for writing and refactoring code, debugging and drafting docs. I review, test and run everything myself and fix the bugs when they turn up. The mascot (Nessa), her voice and art, and the music in the promo videos are AI-generated. No AI runs inside Finesse, and none of your data goes to an AI service.
>
> Feedback I'd really like: anything that broke on your hardware, and anywhere setup confused you.

---

> **ElderHare**（2 分） · 2026-11-04T01:59:37+08:00　
> On a fresh install, it's about 150MB of ram.  There is some caching that happens with larger libraries so it can grow depending on what the server is doing.  CPU usage is low.  I am actually unaware of any features that are missing outright, although some are not implemented as cleanly as the stack yet.  For example, webhook embeds in discord.  There are admittedly some things likely missing as I am not as familiar with Readarr and Lidarr.  There are also features here that are not available in the stack (Spotify and YouTube direct downloading, for example...setup in 5 minutes as another example)
>
> I think your friends are perfect candidates for this program.  I'd love to chat with you more, you should join [https://discord.gg/z74FHj6BDJ](https://discord.gg/z74FHj6BDJ) if you are able so we can see what features you might be looking for that I may not have.  Your project looks interesting as well and I think it can interface with mine through the API.

---

> **jwilcox99**（1 分） · 2026-11-04T04:12:45+08:00　
> **Project Name:** Migratarr
>
> **Repo/Website Link:** [https://github.com/jwilcox99/Migratarr](https://github.com/jwilcox99/Migratarr)
>
> **Description:** Migratarr decides which disk each Radarr/Sonarr title should live on, then moves it, but only after you approve. It scores every movie and series on how hard it would be to get again, whether it streams on a service you pay for (TMDB), and how your household watches it in Jellyfin, then sorts titles into categories (Common / Library / Rare / Archive) that you map to disks. The point is to keep hard-to-replace titles on the disks you trust most without moving thousands of folders by hand, and without sacrificing storage space to redundancy systems. Nothing moves on its own:
>
> * Every run is a frozen plan you review in the web UI. Approvals are tied to that exact plan.
> * Every move re-checks Radarr/Sonarr and hashes the files first.
> * Same-disk moves are renames that never overwrite. Cross-disk moves copy, verify, then delete the source.
> * Every step is journaled. 0.2.0 adds a LAN login and scheduled plans with Discord, webhook or email notifications.
> * Linux only. Moves between disks on the same machine are experimental.
>
> **Deployment:** Docker image [`ghcr.io/jwilcox99/migratarr:latest`](http://ghcr.io/jwilcox99/migratarr:latest) (amd64/arm64), set up like Radarr/Sonarr with `PUID`/`PGID` and `/config`, and no Docker socket needed. There’s a compose example with Radarr, Sonarr and Jellyfin in `examples/docker/compose.yaml`, and a guide in `docs/docker.md`. Or `pipx install migratarr`. A setup wizard runs in the browser, and `migratarr demo` shows a plan on a made-up library offline.
>
> **AI Involvement:** I have no coding background so much of the code, testing, and docs were created and implemented by Claude and a bit of ChatGPT. I created the project from a hole I saw in my automation stack and developed the design and safety rules myself. I have reviewed and merged all changes, and tested all code on my personal media serve and fresh Ubuntu/Debian VMs prior to release. All documentation is available for review in the public repository.

---

> **Fr6ags**（2 分） · 2026-11-04T04:46:28+08:00　
> Project Name: mangashelf
>
> Repo Link: [https://github.com/EldinBegano/mangashelf](https://github.com/EldinBegano/mangashelf)
>
> Website Link: [https://eldinbegano.github.io/mangashelf/](https://eldinbegano.github.io/mangashelf/)
>
> Link to Addon: [https://addons.mozilla.org/en-US/firefox/addon/mangashelf/](https://addons.mozilla.org/en-US/firefox/addon/mangashelf/)
>
> Description:
>
> A browser extension (Firefox and Chrome, MIT) that saves manga chapters as CBZ files with full ComicInfo.xml, so they drop straight into a Kavita or Komga library. It isn't a server itself: it fills the folder your self-hosted reader already watches.
>
> Key points:
>
> \- MangaDex support: series, volume, chapter, title, writer/artist, scanlation group, genres, tags, summary, age rating and language go into ComicInfo.xml, with the right-to-left hint for Japanese manga
>
> \- Image picker for other sites that preselects the chapter's pages
>
> \- Save as CBZ, ZIP or a plain folder of numbered images
>
> \- Folder templates such as {series}/{chapter}, so each series gets its own folder; tokens can be zero-padded ({number:000})
>
> \- Downloads keep running after the popup closes; failed pages can be retried
>
> \- No account, no ads, no tracking, no data sent anywhere except the site you're on
>
> Deployment:
>
> \- Firefox: install from Firefox Add-ons (https://addons.mozilla.org/firefox/addon/mangashelf/), updates automatically
>
> \- Floorp / LibreWolf: Firefox Add-ons, or the .xpi from GitHub releases (updates itself from GitHub)
>
> \- Chrome / Brave / Edge: download the zip from GitHub releases and load it unpacked (not on the Chrome Web Store yet)
>
> \- Kavita / Komga: in mangashelf's settings choose CBZ and set the folder template to {series}/{chapter}, then point a library at Downloads/mangashelf. If the server runs on another machine, share or sync that folder.
>
> \- From source: npm ci && npm run build (Node.js 22+)
>
> AI Involvement: Yes, Claude rewrote my original project into an extension for easier use, I designed the features and reviewed the changes and tested it on real sites.

---

> **ChubbinNubbin**（1 分） · 2026-11-04T06:12:53+08:00　
> Project Name: mustra - self-hosted fleet management for Linux, macOS and Windows
>
> Repo: [https://github.com/mustra-dev/mustra](https://github.com/mustra-dev/mustra)
>
> Description: A Go agent on each machine, one Docker Compose stack on your server. Ask
>
> the whole fleet a question (\`get os from all machines with online equals
>
> true\`), then patch, deploy or fix the machines that answer.
>
> Deployment:
>
> \- Software and patch deployment in rings, with maintenance windows
>
> \- Vulnerabilities from OSV, ranked by CISA KEV and EPSS
>
> \- CIS compliance checks, file integrity monitoring, audit log
>
> \- Agents connect outbound only. No telemetry, no licence check, AGPL-3.0
>
> \`git clone [https://github.com/mustra-dev/mustra.git](https://github.com/mustra-dev/mustra.git) && cd mustra && make quickstart\`
>
> AI involvement: Mostly Vibe Coded
>
> It's 1.0, so bug reports are very welcome!!

---

> **derekleeth**（1 分） · 2026-11-04T09:33:15+08:00　
> **Project Name:** TerminalLynx
>
> **Repo/Website Link:** [https://terminallynx.com](https://terminallynx.com) (Docs: [https://terminallynx.com/docs](https://terminallynx.com/docs))
>
> **Description:** A local-first SSH connection manager built with Rust and Tauri to give you a **cloud-like experience without the cloud**. Instead of syncing your server inventory and SSH keys through a vendor's cloud—or hosting a central sync server that goes down when your homelab is the box you need to fix—your devices and shared team vaults sync directly peer-to-peer over QUIC (`iroh`) using Ed25519 keys in your OS keychain.
>
> Includes an embedded SSH terminal, SFTP file browser, ProxyJump, `-L`/`-R`/`-D` SOCKS5 port forwarding, `key:value` tags (`site:homelab`, `role:docker`) for dynamic grouping instead of rigid folders, and serverless shared vaults with RBAC.
>
> **Deployment:** No backend server or Docker container to maintain. Install the native desktop app on Windows, macOS, or Linux (`.deb`/`.rpm`/`.AppImage`), pair devices with a one-time code, and sync directly over LAN (mDNS) or Tailscale/WireGuard. Free tier includes 25 connections and 3 synced devices.
>
> **AI Involvement:** Architecture, crypto, and SQLite HLC sync specs were designed by hand in Markdown plans (`project_plan.md` / `implementation_plan.md`); Claude Code assisted with Rust/Tauri/React implementation against those specs.
>
> https://i.redd.it/dizabfs22izh1.png

---

> **corn-sandwich**（1 分） · 2026-11-04T09:53:57+08:00　
> Any plans to add slskd support?  Im hanging onto lidarr by a thread with a plugin to tie into slskd but im itching for a different option.

---

> **masiha97**（1 分） · 2026-11-04T13:10:40+08:00　
> \*\*Project:\*\* edge-mouse
>
> \*\*Repo:\*\* [https://github.com/movahedi-ca/edge-mouse](https://github.com/movahedi-ca/edge-mouse) (MIT)
>
> \*\*Description:\*\* A Rust crate that runs the whole computer-use click loop on your own machine instead of shipping screenshots to somebody's API. It reads the page's accessibility tree, finds the button, moves the cursor with Fitts-law timing, then verifies with a pixel hash that something actually changed. Journaled to SQLite so a crash resumes instead of replaying. There's a neural net in there that never shipped: I had 532 training rows and it needed around five thousand, so the boring old BM25 ranker won. Warm click resolves in \~0.009ms, full loop \~10.8ms against a 150ms budget, on a dual-core Chromebook VM. If it needs a GPU, it's not local-first. The honest part: it can't do what a vision model does. Ambiguous target or weird canvas UI, it escalates instead of guessing. Nothing under 12 pixels, it refuses rather than miss. X11/Linux only, no Mac port.
>
> \*\*Deployment:\*\* It's a library, not a service. Clone and cargo build; nothing phones home, nothing to host.
>
> \*\*AI involvement:\*\* Built with heavy AI assistance in an agentic coding session; reviewed, tested, and benchmarked by me.
>
> What would you actually automate locally if the click loop were trustworthy?

---

> **slunatecqo**（1 分） · 2026-11-04T16:57:23+08:00　
> **Project Name:** Cadditor
>
> **Repo/Website Link:**
> GitLab: [https://gitlab.com/friml/cadditor](https://gitlab.com/friml/cadditor)
> Live demo: [https://cadditor-e46d19.gitlab.io/](https://cadditor-e46d19.gitlab.io/)
>
> **Description:**
> I run Caddy in my homelab and one of the reasons I like it is that the Caddyfile syntax is already simple.
>
> For me, the configuration format itself was never the problem. The friction was everything around making a small change: SSH into the server, edit the file, format it, verify it and reload Caddy.
>
> I looked at existing Caddy web UIs, but most of them solve a much broader problem with dashboards, health monitoring, metrics, form-based configuration or multi-instance management.
>
> For my use case, I wanted the opposite: keep the Caddyfile as the source of truth and only make editing and applying it more convenient.
>
> So I built **Cadditor**, a deliberately small self-hosted web editor for the actual Caddyfile.
>
> It provides:
>
> * Caddyfile syntax highlighting
> * code folding
> * indicators for changed lines
> * formatting before apply
> * configuration verification
> * safe Caddy reload only after verification succeeds
>
> There is no database and no alternative configuration format to keep synchronized.
>
> Cadditor is served by Caddy itself and uses a lightweight CGI backend through `fcgiwrap`. It does not require Docker or a Node.js runtime on the server.
>
> I originally built it for my own homelab, but I am happy with how it turned out and decided to publish it. If you use Caddy in a similar way, I would be interested in feedback.
>
> The live demo uses the real frontend, but because it runs on GitLab Pages it does not actually execute Caddy formatting, validation or reload.
>
> **Deployment:**
> Cadditor is intended for an existing Caddy installation.
>
> Installation is handled by a shell installer. The installer can also update an existing installation, and the included uninstaller removes Cadditor again without taking ownership of the user's Caddyfile.
>
> Installation instructions and requirements are documented in the GitLab repository:
>
> [https://gitlab.com/friml/cadditor](https://gitlab.com/friml/cadditor)
>
> **AI Involvement:**
> I used AI as a development assistant for architecture discussions, implementation support, code review and documentation. I made the product and architecture decisions, reviewed and tested the resulting changes, and maintain the project myself.

---

> **guliguligagaga**（1 分） · 2026-11-04T17:56:26+08:00　
> **Project Name**: sopedu-dns
>
> **Repo/Website Link**: [https://github.com/dkhalizov/sopedu-dns](https://github.com/dkhalizov/sopedu-dns)
>
> **Description**: A network-wide ad blocker in one small binary. It blocks ads and trackers from hosts and adblock-style lists (CNAME-cloaked trackers included), caches answers and forwards the rest over DNS-over-HTTPS. It also has local names like [nas.home.arpa](http://nas.home.arpa), a per-device filter bypass, a read-only web UI with a live query log, and Prometheus metrics. Config is one TOML file that reloads on change.
>
> I benchmarked it on my two-node k3s cluster. Each server got one CPU core and 512 MiB, and every blocker loaded the same four lists (744k rules):
>
> |Server|UDP queries/s|Memory at end of run|
> |:-|:-|:-|
> |sopedu-dns|94.1k|18.9 MiB|
> |Blocky|16.4k|87.2 MiB|
> |Pi-hole|4.1k|234.1 MiB|
> |AdGuard Home|stopped answering (hit its 512 MiB limit)|509.8 MiB|
> |Unbound, no lists|64.6k|26.2 MiB|
> |dnsmasq, no lists|27.5k|10.2 MiB|
>
> The query stream was my own home traffic.
>
> Not there yet: DHCP, DNSSEC validation, logins, and an encrypted listener for clients (DoT is likely next).
>
> **Deployment**: v1.0.0 is out. Linux binaries (x86\_64, aarch64), a Docker image at [ghcr.io/dkhalizov/sopedu-dns](http://ghcr.io/dkhalizov/sopedu-dns), `cargo install --locked sopedu-dns`, and a Kubernetes manifest. The README has a quick start.
>
> Copy config.example.toml from the repo first: the image's own config has no blocklists. Root is only there to bind port 53, and every other capability is dropped.
>
> **AI Involvement**: AI coding agents wrote the code. I directed it, reviewed it and decided what to test: an RFC conformance harness, fuzzing and reviews by separate model instances. It's my home DNS now

---

> **sysoppl**（1 分） · 2026-11-04T20:08:30+08:00　
> \*\*Project Name:\*\* Calendar CE (Calendar Community Edition)
>
> \*\*Repo/Website Link:\*\* [https://github.com/sysoppl/Calendar-CE](https://github.com/sysoppl/Calendar-CE)
>
> \*\*Description:\*\*
>
> A calendar and task manager for the browser and Android that keeps everything \*\*on your device\*\* or on \*\*your own CalDAV server\*\* (Nextcloud, Radicale, Baïkal, Fastmail, iCloud, [mailbox.org](http://mailbox.org), Posteo, Synology and others). No account, no cloud, no analytics. It's for people who run a CalDAV server, or want to, and miss a clean front end that feels the same in the browser and on a phone, with tasks next to events, without running a whole groupware suite.
>
> \- Day, week, month, year and agenda views, plus a custom view of 2 to 7 days. Drag to create, move and resize events
>
> \- Recurring events with "this event / this and future / all events" edits, Yes/Maybe/No replies to invitations, and a Join button for Zoom, Teams, Jitsi and Webex links
>
> \- Tasks with subtasks, priorities, due dates and reminders, and a quick add that understands "Call Anna tomorrow"
>
> \- Several CalDAV accounts side by side with incremental sync (RFC 6578), and a "Move my data" wizard between the device and a server that checks every item before anything is deleted
>
> \- \`.ics\` import and export, \`webcal://\` subscriptions, public holidays for 19 countries computed on the device
>
> \- Birthdays and anniversaries that show the years ("Anna's birthday (36)"), and hidden events that keep a title off the screen
>
> \- 5 themes, your own accent colour, 12 bundled fonts, 10 interface languages, keyboard shortcuts and undo for every change
>
> \- Android app with a native CalDAV client and reminders that fire while the app is closed
>
> Not there yet: no contacts (CardDAV), no CalDAV servers that only accept OAuth (so no Google Calendar), no iOS app.
>
> Full disclosure: I also run a paid hosted edition (E2EE Calendar) that adds end-to-end encrypted sync between devices. The community edition is the same app without that cloud, and the local and CalDAV features are the same in both. You can try the app without signing up on the hosted site: [https://calendar.patryk.pro](https://calendar.patryk.pro) (choose "On this device").
>
> \*\*Deployment:\*\*
>
> Released as 1.11.1 under AGPL-3.0. Every release is a ready-made Docker image for amd64 and arm64, \`ghcr.io/sysoppl/calendar-ce\` (tags \`1.11.1\`, \`1.11\`, \`1\`, \`latest\`), built by GitHub Actions with an SBOM and provenance. With the compose file from the repo:
>
> mkdir calendar && cd calendar
>
> curl -fsSLO [https://raw.githubusercontent.com/sysoppl/Calendar-CE/main/docker-compose.yml](https://raw.githubusercontent.com/sysoppl/Calendar-CE/main/docker-compose.yml)
>
> docker compose up -d
>
> Then open http://localhost:8787. There's nothing to persist: the data lives in the browser or on your CalDAV server.
>
> The container is a small Node server with no dependencies that serves the app and a DAV proxy, because browsers can't reach most CalDAV servers directly (CORS). The proxy stores nothing and contacts no server until you allowlist it (\`CALENDAR\_PROXY\_ALLOW\`), rate-limits per client and never logs paths or credentials. The container runs read-only as a non-root user with all capabilities dropped. The compose file also has an optional Radicale demo to try it with.
>
> The README covers every setting, a server setup with HTTPS (Caddy and nginx examples), updating, \`docker run\`, building the image yourself and running without Docker (Node 24 with a systemd unit). The Android app is built from source with Gradle for now.
>
> \*\*AI Involvement:\*\*
>
> A lot. I build this with an AI coding assistant (Claude Code), which does much of the implementation: code, tests, documentation, the CI and Docker setup, and security and licence reviews. I decide what gets built and how it should behave, and nothing ships without passing the test suite: every push runs about 1,570 web and server unit tests and 120 Android unit tests in CI. The 8 interface languages besides English and Polish are machine-translated, so corrections from native speakers are very welcome.

---

> **QuickShibMoon**（0 分） · 2026-11-04T23:45:04+08:00　
> * **Project Name:** VodMax
> * **Repo/Website Link:** [https://github.com/silirim/VodMax](https://github.com/silirim/VodMax)
> * **Description:** A self-hosted server for live TV, movies and series from your playlists (M3U, Xtream Codes, Stalker) and your own media folders. With the server you can also turn on an optional AI assistant, running on a local model (Ollama, or a small built-in one) or with your own API key: you write "something light for tonight" or "record every match of my team" and it picks from what's on TV and in your library, or sets up the recording rule. I'm a tinkerer, and I built it because nothing fit my setup: Jellyfin is great for files but live TV with very large playlists never felt right to me, and the playlist players I tried kept progress and favourites on one device. VodMax isn't meant to replace them, it's an alternative that puts the two together: Free and open source (AGPL-3.0), no paid tier. Meant for playlists you're entitled to use; it doesn't include or point to any content.
>
> https://i.redd.it/7u8iammvhmzh1.png
>
>    * live TV first: channel numbers, P+/P−, guide grid, pause and rewind, catch-up, recordings (also by rule, and watchable while still recording)
>    * stays fast with hundreds of thousands of titles, one card per title, one search and one "continue watching" for playlists and local folders
>    * playlist traffic only through a VPN (built-in WireGuard or the router's), on by default; credentials encrypted, no telemetry
>    * works alongside what you have: HDHomeRun tuner for Plex/Jellyfin/Emby, M3U + XMLTV export for TiviMate/Kodi/VLC
>    * apps for the browser, Android / Android TV / Fire TV and LG webOS; profiles, kids profiles, OIDC login
> * **Deployment:** released (v0.6.5). Docker image [`ghcr.io/silirim/vodmax`](http://ghcr.io/silirim/vodmax) (amd64, arm64, armv7, ffmpeg included), with a docker-compose file in the repo, or a single Go binary with a systemd unit. Step-by-step install guide for server, Android, Android TV, Fire TV and LG: [https://github.com/silirim/VodMax/blob/main/docs/install.md](https://github.com/silirim/VodMax/blob/main/docs/install.md)
> * **AI Involvement:** most of the code is written by an AI coding assistant (Claude Code), and every commit says so. I decide what VodMax does and how it behaves, write down every design choice, test it every day at home and decide what gets released. It's very young (first commit end of October, one person), so Android TV, Fire TV and Raspberry Pi are built but not tested on real hardware yet.

---

> **Organic_Explorer1186**（1 分） · 2026-11-05T00:05:56+08:00　
> **Project Name:** Poster
>
> **Repo/Website Link:** [https://github.com/imdangro/poster-app](https://github.com/imdangro/poster-app) · [https://posterapp.pl/en/](https://posterapp.pl/en/) · 3-minute demo: [https://youtu.be/A\_UTiVYir-4](https://youtu.be/A_UTiVYir-4)
>
> **Description:** Self-hosted social media automation that runs 24/7 on a NAS or any Docker host. It takes over the repetitive part of running a topic-focused social profile – without a SaaS subscription and without handing your accounts and API keys to someone else's cloud.
>
> * Follows news on your topic (RSS, Google News, X profiles) and skips what it already posted
> * An LLM (Gemini's free tier, or a local model via Ollama / any OpenAI-compatible API) picks the best story and writes the posts; images come from the source article (or it posts a link) – no AI-generated images
> * Drafts arrive in Telegram with ✅/❌; one tap publishes to X and Facebook; a failed platform can be retried without double posts
> * "New post": write once, AI adapts it per platform; schedule, history and alerts – everything set up in a web panel
> * Keys, accounts and history stay on your machine, no telemetry (note: X's API bills posting per post; the panel shows an estimated cost)
> * The free LITE edition is AGPL (one bot, X + Facebook); a paid one-time PRO license adds more bots and platforms (Instagram, Threads, Bluesky, a Telegram channel, TikTok) and scheduling with a calendar
>
> **Deployment:** Docker Compose – the official n8n Community Edition image plus a small Node.js panel built from the repo's Dockerfile. One-command install, which also sets up Docker on a clean Ubuntu/Debian server: `curl -fsSL https://posterapp.pl/install.sh | sudo bash` (plain bash – feel free to read it first). The README covers manual install, updates (`scripts/update.sh`) and connecting each platform, in English and Polish.
>
> **AI Involvement:** Built with heavy use of an AI coding assistant (Claude Code) – most of the code, tests and docs were written with it under my direction: I decide on the features and the design, test it and run it on my own NAS. Every change goes through automated tests (including end-to-end tests with mocked platform APIs) and CI. In the app itself, the LLM only writes post text.

---

> **Crazy-Ad6853**（1 分） · 2026-11-05T01:33:21+08:00　
> tts-server-proxy — turn any Android phone into a TTS engine powered by your own self-hosted Qwen3-TTS server. It installs as a real Android system TTS engine (Settings → Text-to-speech output), so every app — readers, assistants, accessibility tools — speaks with your self-hosted voices over an OpenAI-compatible /v1/audio/speech endpoint. No cloud, no telemetry: your text goes only to your server. Open source (MIT), APK in the repo: [https://github.com/manu69x/tts-server-proxy](https://github.com/manu69x/tts-server-proxy)

---

> **igor_kasyanchuk**（1 分） · 2026-11-05T02:11:55+08:00　
> **Project Name:** DiffNotes
>
> **Repo/Website Link:** [github.com/igorkasyanchuk/diffnotes](https://github.com/igorkasyanchuk/diffnotes) (site: [diffnotes.dev](https://diffnotes.dev/), demo: [diffnotes.dev/demo](https://diffnotes.dev/demo))
>
> **Description:** When a coding agent like Claude Code, Codex or Cursor writes a PR, the diff shows what changed but not why. With DiffNotes, the agent uploads short plain-language notes, screenshots and small HTML demos tied to the exact lines it changed, and a Chrome extension shows them inline in the PR diff on GitHub, GitLab or Bitbucket. Nothing is posted to the PR, so there are no bot comments and no noise for teammates who don't use it, and your code context stays on your own server. It's free and MIT-licensed.
>
> **Deployment:** It runs as a single Docker container (`ghcr.io/igorkasyanchuk/diffnotes`) with one persistent volume at `/data`. There's a `docker-compose.yml`: set `PUBLIC_URL` and `ADMIN_EMAIL`, run `docker compose up -d`, and read the first admin password from the logs. There are also templates for Coolify (which diffnotes.dev itself runs on), Render, Fly.io and Railway. Docs: [deploy guide](https://github.com/igorkasyanchuk/diffnotes/blob/main/docs/deploy.md) and [install & config](https://github.com/igorkasyanchuk/diffnotes/blob/main/docs/install.md).
>
> **AI Involvement:** The project is built for AI coding agents, and I built it with AI assistance (Claude Code / Codex), with design, review and testing done by me. I've maintained Rails open source for years, about 7,500 stars total.

---

> **vkiezz**（1 分） · 2026-11-05T03:19:35+08:00　
> I made ai-triage (https://github.com/visheshgubrani/ai-triage) for the PDFs that show up in an inbox and need to be entered somewhere else. It can read from Gmail or take uploads. It gives you the original next to the fields it filled in, and you can fix anything that looks off before approving it.
>
> It’s MIT licensed and runs with Docker Compose. The demo has fake invoices and saved responses, so you can bring it up without an API key. For your own files, you can point it at a local model or use a hosted one.
>
> Claude and Codex helped with development.

---

> **Anon_0365Admin**（1 分） · 2026-11-05T03:41:47+08:00　
> Project Name: Playdarr
>
> I needed something to simplify the watch together experience for me and the boys and girls in Discord, and in today's day and age... creating applications isn't too difficult. I am a Systems Admin, so I understand Infrastructure, IAM, automation, etc. However, I am by no means a developer. Figured I would share this here, has made discord Movie Nights/Watching Sports Games together a breeze!
>
> Think of this like any of the other \*arr suites, this requires you to setup a Plex server, HDHomeRun for Live TV. Jellyfin support MAYBE if there is enough interest, but I don't use Jellyfin myself so am not concerned about it currently.
>
> **What it does**
>
> * **Synced playback.** Play, pause and seek apply to everyone. Viewers who drift are nudged back with small speed changes, not constant seeking, so the audio doesn’t stutter. There’s a host-only “force resync” for when someone falls behind.
> * **Guests don’t need a Plex account.** An invite link plus a display name is enough. A guest’s access is scoped to that one room and what it’s playing.
> * **Your Plex token never reaches the browser.** All HLS traffic goes through Playdarr’s proxy, and Plex stays on your LAN.
> * **Live TV with an HDHomeRun.** Every room gets a rolling one-hour DVR, so the host can pause, rewind or jump back to live while everyone follows. **Split view** puts up to 4 channels on screen, and each viewer picks which one they hear. (Sunday football, anyone?)
> * **Watch nights:** schedule a night (one-off, weekly or biweekly) with an invite and calendar file, and get Discord webhook reminders before it starts.
> * **Movie vote:** everyone swipes yes/no on a random deck from your library, and the room’s favorite wins.
> * **Chat that’s actually usable:** replies, reactions, GIFs, image uploads, mute, a word filter, and pop-out chat.
> * **Fun extras:** floating emoji reactions, a film-leader countdown with beeps, and timed intermissions with the poster on screen.
> * **Always-on rooms** that never close, for example a standing Live TV channel people can drop into.
> * **An admin panel** for the server owner, plus most settings editable in the UI.
>
> **The couch: Android TV / Google TV app**
>
> There’s also a [native Android TV app](https://github.com/tf-anguskong/Playdarr-AndroidTV), tested on an NVIDIA Shield TV Pro. It’s a sideloaded APK, not in the Play Store. It joins rooms in sync with everyone in the browser, and it was the part I had the most fun with:
>
> * Plex users sign in with a [plex.tv/link](http://plex.tv/link) code.
> * Guests scan a QR code on the TV with their phone and paste the invite link. No typing with the remote, and no server to set up first.
> * The TV checks the link really points to a Playdarr server and shows you the domain before it joins anything.
>
> **Setup**
>
> Docker Compose. Point it at your Plex server’s LAN address and give it a Plex token and a session secret. It runs fine behind a reverse proxy. There’s an Admin Guide in the repo covering setup, the admin panel, Live TV, webhooks, backups and troubleshooting.
>
> **Transparency**
>
> This was **vibe coded**: built almost entirely through conversational prompting with Claude. It works, and I use it, but it hasn’t had a professional security audit (other than an Opus 5.5 review, lol). Read the Security Notes page in the wiki before you expose it to the internet, and treat it like any hobby project. Issues and PRs are very welcome.
>
> **Links**
>
> * Server: [https://github.com/tf-anguskong/Playdarr](https://github.com/tf-anguskong/Playdarr)
> * Android TV app: [https://github.com/tf-anguskong/Playdarr-AndroidTV](https://github.com/tf-anguskong/Playdarr-AndroidTV)

---

> **ElderHare**（1 分） · 2026-11-05T04:16:07+08:00　
> Out of all the apps that Reelix covers in the stack, the worst support is for the Lidarr and Readarr equivalencies.  I will look into the slskd support, I am not too familiar with it honestly but on first peruse, it definitely seems interesting and could be a good integration to Reelix

---

> **dxnxax**（1 分） · 2026-11-05T05:41:45+08:00　
> **Project Name:** Vigo
>
> **Website:** https://vigo.alexander4.io
>
> **Repo:** https://github.com/daniel-alexander4/vigo
>
> **Description:** Vigo is a configuration management tool, in the same space as Puppet, Ansible and Salt. You describe how your machines should look in YAML files (packages, files, services, users, firewall rules, cron jobs, containers), and a small agent on each machine pulls that state from your server and applies it. Agents only change what has drifted, so a run that finds nothing to fix changes nothing. They report results back to a web dashboard that shows which machines are converged, which have drifted and which are offline.
>
> All traffic between agents and the server is mutual TLS, and every agent request is signed. Secrets stay encrypted on the server and are never written into config or sent to machines that don't need them. Agents keep working from their last config when the server is down. Beyond config management it includes inventory, CVE and risk scoring, compliance reports (CIS, SOC 2, HIPAA, PCI and others), ad-hoc tasks and workflows, and browser SSH/RDP to any machine without opening inbound ports on it.
>
> The server is Go with SQLite, and the agent is a single Rust binary for Linux, macOS, the BSDs, illumos and Windows. Nothing phones home, and there's no account or license key. It's Apache-2.0. I run it on my home lab fleet.
>
> **Deployment:** The server runs in Docker with docker compose. Tagged releases are on GitHub. There's no prebuilt image yet, so the first step builds it from source (about 20 minutes the first time). The README Quickstart covers it: build the image, seed /srv/vigo, run docker compose up -d, and the dashboard is at https://localhost:8443. Each machine enrolls with one command, curl -sSfk https://:8443/bootstrap | sudo sh, which installs the agent as a native service. Docs live in docs/ in the repo, including a getting-started series under docs/start/.
>
> **AI Involvement:** I designed the system and made the architecture and security decisions; Claude wrote much of the code under my direction. Every change goes through tests and review, and I run it on my own machines.

---

> **dxnxax**（1 分） · 2026-11-05T05:45:25+08:00　
> **Project Name:** Hespera
>
> **Website:** https://hespera.alexander4.io
>
> **Repo:** https://github.com/daniel-alexander4/hespera
>
> **Description:** Hespera is a media app for your music, TV, movies, photos, books and audiobooks, with automatic metadata matching. It's one Go binary with SQLite: no accounts, no telemetry, and outside services are only used to fetch metadata.
>
> Music is matched against MusicBrainz, with cover art, artist bios, synced lyrics, playlists, instant mixes, duplicate detection and a tag editor that writes back to your files. TV and movies are matched against TMDB. They direct play when the browser can handle the file and use seekable on-demand HLS transcoding when it can't. You also get subtitles, skip-intro detected by audio fingerprinting, scrub thumbnails, Up Next and resume. Photos get an EXIF timeline. Books (EPUB, CBZ, PDF) open in a built-in reader, and audiobooks (m4b) get chapters, variable speed and resume. A file watcher picks up new media, and the app can detect and losslessly repair broken containers. The whole UI works with arrow keys or a TV remote.
>
> **Deployment:** It's a single binary for Linux, macOS and Windows (amd64 and arm64), plus .deb packages, all on the GitHub releases page. ffmpeg is needed for TV and movie playback. By default it runs as a desktop app window on one machine. To serve your household, run server mode (HESPERA_NO_BROWSER=1, with HESPERA_LISTEN=:8080 to listen beyond loopback); the .deb ships a systemd unit for this, disabled until you enable it. There's no Docker image. Install and run instructions are in the README.
>
> **AI Involvement:** I built Hespera with help from Claude Code (Anthropic's coding assistant). I designed the app and directed and reviewed the work, and Claude wrote part of the code. I use it every day on my own library.

---

> **Fickle_Foundation_41**（1 分） · 2026-11-05T05:46:53+08:00　
> **AwaitIO**: internal tools / admin screens as TypeScript functions, served by your own Node process.
>
> Upfront, so nobody feels misled: it's a library you build your own back office with, not an app you `docker run`. You need to write TypeScript. I'm posting it here because the whole point is that nothing leaves your server.
>
> - **One process.** The same Node server runs your tool code, serves the UI and keeps the state. No second service, no worker, no hosted control plane.
> - **No database, nothing on disk.** Users are a list in your config with scrypt password hashes. Runs live in memory, so a restart ends the ones in progress.
> - **No telemetry**, nothing phones home. The browser talks only to your server.
> - **A plain server, no serverless.** It runs wherever Node runs: a VPS, a box at home, your laptop for a team of one.
> - **Private by default.** Binds to `127.0.0.1` unless you set a host, `/health` for your monitoring, `basePath` if it shares a domain behind your reverse proxy.
>
> What a tool looks like:
>
> ```ts
> const email = await io.input.email("User email");
> const user = await db.user.findUniqueOrThrow({ where: { email } });
> await db.user.update({ where: { id: user.id }, data: { emailVerified: true } });
> ```
>
> Each `await io.…` shows a form in the browser and waits for the answer.
>
> License, since it matters here: the source is public but it's **source-available, not OSI open source**. Free for up to 3 users, commercial use included. I built it because Interval, which I used for this from 2022, lost its hosted version, and running its server next to every app was the part I wanted gone.
>
> Code and docs: [GitHub](https://github.com/awaitio/awaitio). I'm the author, ask me anything.

---

> **NorwegianFootDude**（1 分） · 2026-11-05T12:59:12+08:00　
> Nice, would you consider developing an Android APK alternative soon?

---

> **walterblackkk**（0 分） · 2026-11-05T14:17:59+08:00　
> ezVaultwarden - A script to get your own Vaultwarden instance up and running in seconds.
>
> With options to expose via Tailscale or with your own domain and HTTPS.
>
> https://github.com/mfat/ezVaultwarden

---

> **SpecialistTap9708**（1 分） · 2026-11-05T15:46:54+08:00　
> **Project Name**: FreePdfEditorOnline
> **Website:** [https://mswsal.github.io/FreePdfEditorOnline/](https://mswsal.github.io/FreePdfEditorOnline/)
> **Repo**: [https://github.com/MSWSal/FreePdfEditorOnline](https://github.com/MSWSal/FreePdfEditorOnline)
>
> **Description** : Created to give user to **remove pages and sign the pdf**. Simple as that.
> No logins, just come and do your work.
>
> I decided to give it a go because if we are in a hurry, we don't have enough time to login and do unwanted stuff.
>
> Documents wont be saved. So NO PRIVACY VIOLATION ISSUES.
>
> ***\*\*feel free to suggest new features. Or Fork and implement.***
>
> **Deployment:**  Deployed on Github pages. Open source. Code can be viewed in above REPO link. [https://mswsal.github.io/FreePdfEditorOnline/](https://mswsal.github.io/FreePdfEditorOnline/)
> Or just clone it and run 'index.html'
>
> **AI Involvement: Used Claude code for development.** Orchestrated the whole process, tested and hosted by myself.

---

> **Agreeable-Elk9265**（1 分） · 2026-11-05T18:11:21+08:00　
> https://i.redd.it/7bsftf0rqrzh1.png
>
> **Repo:** [github.com/rdvnit/TesPlay](https://github.com/rdvnit/TesPlay)
>
> **What it does**
> TesPlay is a self-hosted web app that brings all your media together in one interface, designed for the Tesla browser but works on any device with a browser. You host it yourself, it's completely free, and there's no subscription.
>
> **Features**
>
> * Plex: browse libraries, watchlist, progress sync
> * IPTV: live TV with EPG (Xtream Codes or M3U)
> * YouTube, Stremio addons (no torrents/DRM), Google Drive, internet radio
> * Phone as remote: pair via QR, log in from your phone, send videos or HLS links to the screen, upload files from your phone
> * Profiles, My List, watch history, per-library access for family members
> * Own player (TesPlayer) with WebCodecs, HLS and MPEG-TS support, no lag or audio sync issues on older Intel Tesla's
>
> **Why I built it**
> Nothing existed that combined all of this into one app for the Tesla browser. Paid alternatives exist, but this is free and self-hosted.
>
> **Deployment**
> Docker Compose or Node 22+ with SQLite. Runs on Mac, Linux and Raspberry Pi (tested on a Pi 4). Optional Cloudflare Tunnel/Access profile. HTTPS required. Full install docs in the README.
>
> **Tested on**
> Model 3 (2019/2021 Intel, 2023 AMD), Model Y LR 2023, Model 3/Y Performance 2026. Built for parked use and passengers.

---

> **ElderHare**（2 分） · 2026-11-05T18:28:14+08:00　
> After looking into this more, I am going to add support for it.

---

> **DirectionUnique5773**（1 分） · 2026-11-05T19:32:20+08:00　
> * **Project Name:** Indexlume
> * **Repo/Website Link:** GitHub: [https://github.com/junaidtariq48/indexlume](https://github.com/junaidtariq48/indexlume) Website and documentation: [https://indexlume.oryxsol.com/](https://indexlume.oryxsol.com/)
> * **Description:** Indexlume is an Apache-2.0-licensed, self-hosted operations platform for Typesense. It provides one interface for connecting source data, shaping search documents, operating indexing jobs and safely testing relevance changes. Current capabilities include: Indexlume is independent and is not an official Typesense product. Typesense remains separately licensed under GPL-3.0.
>    * PostgreSQL and file-based data sources
>    * Multi-table relational projections
>    * Collection and indexing-job management
>    * Incremental indexing, reconciliation, retries and job history
>    * Relevance Studio with synonyms and curation rules
>    * Golden-query relevance regression tests
>    * Versioned relevance publishing and rollback
>    * Search Studio and request analytics
>    * Workspace roles, API keys and audit history
>    * Encrypted connector credentials
>    * Backup, restore and key-rotation tooling
>    * Bundled or external Typesense connections
> * **Deployment:** Indexlume currently supports a single-machine Docker Compose deployment. Users can clone the repository, generate local secrets and start the application stack using the documented Docker Compose workflow. Installation guide: [https://indexlume.oryxsol.com/docs/installation/](https://indexlume.oryxsol.com/docs/installation/) The current deployment target is intended for self-managed environments. Operators remain responsible for networking, TLS, backups, upgrades and capacity planning.
> * **AI Involvement:** AI-assisted tools were used during parts of coding, design implementation, testing, documentation and review. I personally directed the product, made the architectural and licensing decisions, reviewed the changes, ran the tests and maintain the releases. The repository includes documented limitations, security checks, licensing information and reproducible validation steps.
>
> I would appreciate feedback on the installation experience, relevance-testing workflow, security model and which data source would be most valuable next.

---

> **aofu_dev**（1 分） · 2026-11-05T22:04:58+08:00　
> Project Name: dotme
>
> Repo: [https://github.com/AFFFPupu/dotme](https://github.com/AFFFPupu/dotme)
>
> Description: Self-hosted preferences for AI agents. Your prefs live as Markdown in a private GitHub repo you own. A small Cloudflare Worker (free plan) serves them over MCP with OAuth. Claude Code, Codex and similar clients read them at session start. Agents cannot write directly. They propose a change with evidence, and nothing is saved until you approve (passkey on phone or in-client). Each approval is a git commit.
>
> Deployment: Cloudflare Worker on the free plan. Follow [INSTALL.md](http://INSTALL.md) (data repo, GitHub token, Worker, passkeys). MIT, no hosted SaaS, no account with me.
>
> AI involvement: Built with Claude Code. The product is for AI agents. Claude Code, Codex, [claude.ai](http://claude.ai) and Grok Bot are tested.
>
> Looking for cold-install reports: tell me which [INSTALL.md](http://INSTALL.md) step fails first.

---

> **kaaiman12**（1 分） · 2026-11-05T22:41:12+08:00　
> **Project Name:** Bucketlistr
>
> **Repo/Website Link:** [https://github.com/Kaaiman1214/Bucketlistr](https://github.com/Kaaiman1214/Bucketlistr)
>
> **Description:** Bucketlistr is a self-hosted, open source, web-based bucket list for keeping track of everything you still want to do in life. Your list is publicly visible to anyone who visits, but only you can edit it once logged in, so you can share your goals without worrying about others changing them. Features:
>
> Bucket list items:
>
> Items with optional descriptions, status, and completion date, all shown on a single homepage.
>
> Categories:
>
> Organize your goals by type, such as locations, career goals, or experiences.
>
> Photos:
>
> Photo carousels for each item. The first image in the carousel is used as the preview image on the homepage.
>
> Checklists:
>
> Turn items into checklists with a progress bar and completion percentage, which is useful for multi-part goals like “Visit 50 countries” or “Watch the top 100 IMDb movies”.
>
> Search:
>
> Quickly find items once your list gets large.
>
> Public to view, private to edit:
>
> Visitors see the main page, and only you can create and edit items after logging in.
>
> Flags:
>
> Show flags for items that involve a country or region, including places not recognized by the UN, such as Cornwall, Transnistria, or Kosovo.
>
> https://i.redd.it/6bnjhzqy2tzh1.png
>
> **Deployment:**
>
> Bucketlistr can be self-hosted with Docker or run directly with Python. Docker: On any system with Docker installed, run:
>
>   docker run -d --name bucketlistr -p 5000:5000 \\
>
>   \-v bucketlist-data:/data --restart unless-stopped \\
>
>   [ghcr.io/kds1215/bucketlistr:latest](http://ghcr.io/kds1215/bucketlistr:latest)
>
> The app will then be available on port 5000
>
> Without Docker:
>
>   git clone [https://github.com/Kaaiman1214/Bucketlistr.git](https://github.com/Kaaiman1214/Bucketlistr.git)
>
>   cd Bucketlistr
>
>   python -m venv venv
>
>   source venv/bin/activate
>
>   pip install -r requirements.txt
>
>   python [main.py](http://main.py)
>
> **AI Involvement:**
>
> The basic web application, database, and user creation are based on a Tech With Tim’s tutorial video. The further features were written by me with the help of Claude, as my coding skills are still developing.
>
> Looking for feedback and points of improvement moving forward

---

> **cryalcin**（1 分） · 2026-11-05T23:23:47+08:00　
> **Project Name**: Monline - self hosted subscription and payment tracking
>
> **Repo / Documentation**: [https://github.com/caglaryalcin/Monline](https://github.com/caglaryalcin/Monline)
>
> **Description**:
>
> Hi everyone! I’m the developer of Monline, a free, open-source app for tracking subscriptions, recurring payments, and budgets on your own server.
>
> It helps you keep track of renewal dates, upcoming charges, and actual payment history, with a calendar and spending summaries in one place.
>
> ***- Stable(1.x)***
>
> Features available in the stable release include:
>
> *  Flexible billing cycles, automatic service logos, and scheduled subscription price changes.
> * A payment calendar with paid/pending tracking, one-off payments, and movable payment dates.
> *  Monthly, quarterly, six-month, and yearly budget views.
> *  Multiple currencies, categories, payment methods, and payment reminders.
> *  Separate user accounts and selective subscription sharing with view or edit permissions.
> *  Two-factor authentication and OIDC sign-in.
> *  Account exports and full instance backups.
> *  A mobile-friendly interface with multiple languages and light/dark themes.
>
>  ***- Beta(2.0)***
>
> *   A spreadsheet-style income and expense view with monthly entries, notes, tags, and copy/paste support.
> *   Loan and installment tracking.
> *   Bill planning with estimated future costs.
> *   PDF statement import and reconciliation, with subscription detection and calendar integration for supported bank formats.
> *   Salary tracking and comparison charts.
> *   Expanded dashboard charts covering subscriptions, bills, loans, and recorded payments.
> *   Excel exports with formulas and charts, plus scheduled exports to a NAS through SMB or a mounted server folder.
> *   A dedicated monthly finance view for smaller screens.
>
> These features are still in beta. I’d especially appreciate feedback on the finance worksheet, statement matching, and loan/installment workflows.
>
> **Deployment**:
>
> Docker Compose, with stable images available on Docker Hub and GHCR for AMD64 and ARM64. It uses SQLite, so there’s no separate database server to configure.
>
> The stable Docker image is *caglaryalcin/monline:latest*. For the 2.0 beta, use *caglaryalcin/monline:beta*. Installation instructions and screenshots are in the README. The project is licensed under GPL-3.0.
>
> **AI Involvement**:
>
> AI coding assistants are used in the development workflow.

---

> **corn-sandwich**（1 分） · 2026-11-06T00:34:31+08:00　
> Sweet, im looking forward to trying it.  Currently using Mediarium but it doesn't support slskd.  I want away from the arrs

---

> **Intelligent-Row-5244**（1 分） · 2026-11-06T00:58:37+08:00　
> \* Project Name: Sampler Hub (companion to Opera, an open-source AI assistant)
>
> \* Repo/Website Link: https://github.com/MaestroAI-Company/sampler-hub , https://maestroai.company/sampler/
>
> \* Description: A small self-hosted server that keeps your devices in sync for Opera (Android, Windows, macOS, Linux), our open-source AI assistant. Install it on a computer you own and pair your phone/desktop with a QR code. No account, no third-party server in the middle.
>
>   \- Sync: conversations, messages, images and settings move between devices, end-to-end encrypted (the hub stores profiles but cannot read them).
>
>   \- Shared models: use the Ollama, LM Studio and llama.cpp models running on the hub's machine from every paired device. The hub can also download and run llama.cpp models itself.
>
>   \- Profiles: one hub for a household, each profile with its own password and backup.
>
>   \- MCP servers can be installed on the hub and used from every device.
>
>   \- Admin screen with paired devices and live CPU/memory charts.
>
>   It is useful if you already run local models (Ollama etc.) and want to use them from your phone without sending anything to a cloud. License: AGPL-3.0.
>
> \* Deployment: Released (v0.12.0). Native binary, no Docker image at the moment.
>
>   \- Linux (x86\_64/arm64) and macOS: curl -fsSL [https://github.com/MaestroAI-Company/sampler-hub/releases/latest/download/install.sh](https://github.com/MaestroAI-Company/sampler-hub/releases/latest/download/install.sh) | sh (verifies SHA256SUMS, installs to \~/.local/bin, registers a systemd user service / launchd agent).
>
>   \- Windows: installer from the latest release.
>
>   \- Then run "sampler-hub pair" to print a QR code and pair a device.
>
>   Install and pairing guide: [https://maestroai.company/docs/install/hub/](https://maestroai.company/docs/install/hub/)
>
> \* AI Involvement: I designed the architecture I review and test everything myself and a colleague did the visual design. I used AI coding assistants to help with the implementation (code, docs and tests). The project is open source (AGPL-3.0), so you can read exactly what it does.

---

> **pintto65**（1 分） · 2026-11-06T01:03:20+08:00　
> Project Name: Browser Mate (beta, Chrome desktop, MV3)
>
> Repo/Website Link: https://browsermate.app/?lang=en — docs at https://docs.browsermate.app. The source is in a private repo for now; the beta build is an unlisted Chrome Web Store item.
>
> Description: Disclosure first, because the rule here is clear: this is not a container and there is no docker-compose in this comment. What is self-hosted is the model endpoint. The client is a Chrome extension with no server behind it.
>
> That combination is the reason I am posting here. Most browser agents are a thin client over someone's cloud: the DOM, including logged-in pages, goes to their infrastructure. This one has no infrastructure to send it to. Point it at Ollama (http://localhost:11434/v1/chat/completions, key empty) or at LM Studio through the Custom OpenAI-compatible provider, and the only network hop for inference is your own machine.
>
> What it does: a side panel in Chrome. You give it a task; the model proposes tool calls; the extension executes them in the browser you are already logged into — click, type in non-sensitive fields, extract text, scroll, wait, navigate, tabs, screenshots. No account, no telemetry, no third-party analytics in the extension or on the site.
>
> Safety, since an agent holding your session is the real risk: page text is untrusted data; password, card and file-upload fields are never filled by the agent (it hands the turn back to you); destructive or outbound actions hit a confirmation gate; an approved click is bound to a SHA-256 fingerprint of the exact button, so a last-second DOM swap cancels it; every turn ends with a redacted, signed receipt.
>
> Honest limits: "local" is not "offline" — inference is local, but the extension may still fetch public model catalogs and exchange rates for cost estimates, and the privacy page says so. The agent is only as good as the model's tool calling: a chat-only model will not drive it and text-only models cannot take screenshots. Heavy SPAs, canvas UIs, cross-origin frames and anti-bot flows break it, and it pauses for human handoff rather than guessing. Screenshots can contain sensitive data even when the fields are protected. Default settings ship with "Allow all" on and per-category confirmations off; turn on prompt-injection protection and confirmations in Settings → Security before running it on anything real.
>
> Deployment: nothing to pull. It is a Chrome extension (desktop, MV3): an unlisted Chrome Web Store item, access by request at https://browsermate.app/?lang=en, install link arrives by email. The docs cover the Ollama endpoint, the LM Studio setup and each security setting. Free during the beta; €1/month afterwards, announced two weeks ahead, local data preserved.
>
> AI Involvement: total, and not hidden. The product is an AI agent by design — it bundles no model of its own and uses yours. AI coding assistants were also used while building it, and the safety layer, test suite and changelog are kept in the open docs, with a redacted receipt for every turn so any claim here can be checked rather than taken on trust.
>
> There is also a simulator at https://browsermate.app/demo/ that shows five prompt-injection scenarios without installing anything, if you would rather judge the security design before the agent.
>
> What I want out of this thread is failure reports from people already running an Ollama server: which model and size, and where the tool-calling loop stalls. If a mod thinks this belongs elsewhere, say so and I will move it.

---

> **Independent_Bat_6201**（1 分） · 2026-11-06T01:25:05+08:00　
> A tailnet tends to grow past what you can hold in your head. A home server, a couple of Pis, a VPS, a laptop, a phone. Bield is a container or a single binary that joins the tailnet as its own node and puts all of them on one page. For each machine you see whether it's up, how traffic gets to it, CPU, memory, disk and network with up to 90 days of history, and its containers. Admins can open a terminal, browse files and restart a container from the same page.
>
> There's no password. Bield asks Tailscale, or Headscale, which user each connection comes from, and that is the login. Admins and read-only viewers are tailnet users.
>
> There's also a systemd install script, and release archives for Linux and macOS on amd64 and arm64.
>
> What it does:
>
> \- Lists every device on the tailnet with its route and round-trip time, with no agent installed.
>
> \- Charts CPU, memory and network per machine. A small bash agent reports for machines other than the one Bield runs on, and you can read it before you run it.
>
> \- Website, port and DNS checks, a ping of every device, and alerts to ntfy, Telegram, email, Discord, Slack or any webhook.
>
> \- Shows containers with logs and live stats, and can start, stop and restart them. It can't create, exec or prune, on purpose.
>
> \- Terminals that keep running in tmux after you close the tab, and a file manager that edits and previews.
>
> Running cost, from a 4 vCPU VPS: 12 machines use 0.4% of a core and 59 MB. 200 machines with 90 days of history use about 3% of a core, 129 MB and a 580 MB database.
>
> Privacy. There are no analytics and no update check. What leaves the machine is the Tailscale node talking to Tailscale, which also uploads its logs unless you set \`TS\_NO\_LOGS\_NO\_SUPPORT=true\`, three default checks against 1.1.1.1, cloudflare.com and google.com until you delete them, and whatever notification channels you add.
>
> How it compares. Beszel is lighter and more mature if all you want is metrics. Uptime Kuma is the one for status pages and for watching from outside your network. Portainer deploys containers, which Bield doesn't. Bield is narrower than all three: one page for a small tailnet, with the tailnet as the login, and terminals and files next to the health data. They run fine alongside it.
>
> To try it without a tailnet, \`./bield serve --demo\` from a release archive gives you a made-up one with 12 machines. You can also click through the same demo in your browser without installing anything: [https://manasseh-fikadu.github.io/bield/](https://manasseh-fikadu.github.io/bield/)
>
> Repo: [https://github.com/manasseh-fikadu/bield](https://github.com/manasseh-fikadu/bield)
>
> Docs: [https://manasseh-fikadu.github.io/bield/docs/](https://manasseh-fikadu.github.io/bield/docs/)
>
> I'll answer anything here. Bug reports and "this is the wrong way to do X" are both welcome.

---

> **kroovy**（1 分） · 2026-11-06T01:40:47+08:00　
> I love the idea of this but it would never fly in my group.

---

> **brkfun**（1 分） · 2026-11-06T02:01:51+08:00　
> **Project Name:** RunR
>
> **Repo/Website Link:** https://github.com/BRF-Tech/runr (site: https://runr.sh, live demo: https://demo.runr.sh)
>
> **Description:** A self-hosted serverless platform on Kubernetes and Knative, MIT licensed. Write a function in the browser, `git push` a project or bring a container image or a Wasm module; RunR builds it and runs it on your own clusters with scale-to-zero. Every change is a version you can roll back with the configuration it ran with; dev/staging/production environments; blue-green and canary rollouts; each project type of a region under runc, gVisor or Kata Containers; Postgres, Redis and S3 bindings; RBAC, SSO, audit log; multi-tenancy as an optional module.
>
> **Deployment:** Helm chart with one required value (`domain`), or Docker Compose on one host, air-gapped included. First public release 2026-10-18, current 0.6.5. Docs: https://runr.sh/docs/
>
> **AI Involvement:** Architecture, decisions and review by the maintainer; most of the code, backend and UI, written with Claude Code under that direction. 4,500+ PHP tests and 1,700+ UI tests run in CI, plus Kind end-to-end suites before each release.

---

> **BeneficialConcern996**（1 分） · 2026-11-06T02:32:04+08:00　
> Project Name: ManaWG - a shared-flat organizer (Apache-2.0)
>
> Repo: https://github.com/Abuarchiv/manawg
> Self-hosting guide: https://github.com/Abuarchiv/manawg/blob/main/docs/self-hosting.md
>
> Description: I'm Abdi Tube, the creator of ManaWG. It combines shared expenses, a cleaning rota and a shopping list for people living together. It runs in the browser as a PWA, in English and German. This is my own project, not an independent recommendation.
>
> Deployment: Docker Compose runs the app, PostgreSQL, Supabase Auth/Storage and Caddy on your own machine; a Supabase cloud account is not needed for the Docker setup. Release v0.1.1 is available. The documented local quick start is:
>
> git clone https://github.com/Abuarchiv/manawg.git
> cd manawg
> ./docker/setup.sh
> docker compose up -d
>
> Local sign-in emails go to Mailpit at localhost:8025. A public instance needs HTTPS and real SMTP. Registration is open to anyone who can reach the instance, so restrict access at your proxy/VPN if it is only for your household. Start with a throwaway instance and test data, not real financial records.
>
> AI involvement: AI coding assistants (Opus 5.5) Total are used in development.
>
> I'd particularly value first-install feedback: which documented step becomes confusing, and can two willing housemates find and use the same shopping item or cleaning task? No payment, ratings or positive feedback required.
>
> Abdi Tube

---

> **Easy_Leave_5784**（1 分） · 2026-11-06T04:05:51+08:00　
> **Project Name: Blackmagic cam remote**
>
> **Repo Link:** [https://github.com/skeplys83/blackmagic-cam-remote](https://github.com/skeplys83/blackmagic-cam-remote)
>
> **Description:** Remote-control the Blackmagic Camera app on an Android phone from any browser. It features live view with overlays and sound, camera controls, recording format, presets, recordings and phone health.
>
> **Deployment:**
>
>     docker pull ghcr.io/skeplys83/blackmagic-cam-remote:sha-5f0ac9b
>
> https://i.redd.it/j5ov7dw8ouzh1.png

---

> **Zestyclose-Ad1369**（1 分） · 2026-11-06T05:04:30+08:00　
> **Project Name:** mycontext
>
> **Repo/Website Link:** [https://github.com/bencoleman24/mycontext](https://github.com/bencoleman24/mycontext)
>
> **Description:** A local environment to collect, manage, and own your personal data.
>
> Most AI assistants today keep their memory of you on their own servers. That makes it harder to switch providers, and gives them a lot of control over your data. I think this gets worse as AI becomes more integrated with our day to day life, so I wanted a personal collection of data that I fully own.
>
> mycontext keeps that data in plain files on your machine. It includes:
>
> * a local web UI for collecting and managing it. Currently it has sections for profile, habits, journal, notes, files
> * an MCP server, so AI apps like ChatGPT, Claude, Cursor, and Gemini can read and write the data directly
> * plain JSON files you can read without this app, and export as Markdown, JSON, or CSV
>
> Your data stays on your machine: no telemetry, no cloud sync, no external network calls there’s a test that fails the build if any are added.
>
> It’s basically a simple local platform for data collection + can be interchangeably hooked up to AI if that’s something you’re interested in.
>
> **Deployment:** MIT, Node 20/22/24. No Docker image yet, you clone it and run two npm commands. The README covers setup, with docs/ for the MCP tools, HTTP API and data model. It’s v0.1.0, no tagged release yet.
>
> **AI Involvement:** Heavy! I decided what it should do and how it should work, and I reviewed and tested everything, Claude wrote most of the code.

---

> **Alpercino_FX**（1 分） · 2026-11-06T05:46:09+08:00　
> Project Name: Jellymesh
>
> Repo/Website Link: https://github.com/AlpercinoFX/Jellymesh-a-jellyfin-p2p-mesh
>
> Description:
>
> Motivation: I wanted to watch high-bitrate movies in maximum quality with multiple friends at the same time. Residential home internet upload speeds aren't fast enough when several people pull streams at once, and I didn't want to ruin the picture with aggressive transcoding.
> How it works: Viewers watching the same stream seed buffered video chunks directly to each other via WebRTC, dramatically cutting down the strain on the server's uplink. Clients are automatically grouped into peer "swarms" based on matching audio language and quality settings so they only share identical chunks. It also features an in-player HUD for each viewer and a localhost live topology monitor to visualize bandwidth offload in real time.
> Caveats: Currently works on desktop Chromium browsers (Chrome, Edge, Brave, etc.) rather than native smart TV apps due to browser script injection and WebRTC requirements. The server host should access Jellyfin locally via LAN/localhost so their own browser doesn't seed back out over the home connection.
> Deployment:
> The project is available directly on GitHub with full documentation in the README. It includes automated 1-click batch and PowerShell scripts (install-p2p.bat, start-all.bat) that detect your Jellyfin install, inject the client hooks, run a zero-dependency local Node.js signaling tracker (port 8000), launch the live monitor (port 8001), and configure Caddy as the reverse proxy. An update-recovery script is included to restore hooks after Jellyfin server updates.
>
> AI Involvement:
> The entire codebase and architecture (the WebRTC scripts, tracker daemon, UI components, and batch installers) were generated using AI under my direction. I did all the real-world deployment, manual testing across multiple peer clients, debugging, and verification to make sure the mesh network actually functions and offloads bandwidth as intended.

---

> **devaliuz**（1 分） · 2026-11-06T06:14:52+08:00　
> Ich hatte vor ein paar Monaten eine ähnliche Idee. Vielleicht inspiriert dich meine Lösung ja zu weiteren Features:
>
> https://github.com/LupusMalusDeviant/Pagebound

---

> **bloody7up**（1 分） · 2026-11-06T06:52:15+08:00　
> https://i.redd.it/vstg24mlivzh1.jpeg
>
> **Project Name:** Kava — a Netflix-style reader for your self-hosted comics and books
>
> **Description:** I wanted my comic library to feel like browsing Netflix on my iPad. **Kava** gives your Kavita, Komga, OPDS, or SMB library a cover-first home screen with recommendations and a Continue Reading row, so you can find something to read or jump back into a book.
>
> **Deployment:** [Download Kava from the App Store](https://apps.apple.com/us/app/kava-comic-reader/id6817441940) on iPhone or iPad (18 or later), then add your existing server or NAS share in the app. Kava connects directly, with no extra backend or Kava account required. One server connection is free, and Kava Pro adds multiple connections.
>
> **AI Involvement:** I built Kava with an AI-native coding workflow, using AI to help write and iterate on the app’s code throughout development. I also used ChatGPT to help draft this comment.

## 关联链接

- https://www.reddit.com/r/selfhosted/search/?q=

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
