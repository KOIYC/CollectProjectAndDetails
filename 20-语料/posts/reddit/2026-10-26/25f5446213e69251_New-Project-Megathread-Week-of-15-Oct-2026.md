---
type: "corpus"
item_id: "25f5446213e69251"
title: "New Project Megathread - Week of 15 Oct 2026"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6ywou/new_project_megathread_week_of_15_oct_2026/"
author: "AutoModerator"
published_at: "2026-10-16T06:01:02+08:00"
captured_at: "2026-10-26T09:43:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - New Project Megathread
metrics: {"score": 54, "comments": 259, "upvote_ratio": 1}
comments_count: 198
comments_total: 259
discovered_via: "reddit:14d+settle10"
---

# New Project Megathread - Week of 15 Oct 2026

> [!info] 一句话导读
> Welcome to the **New Project Megathread!**

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6ywou/new_project_megathread_week_of_15_oct_2026/>
> 指标：得分=54 · 评论=259 · 赞踩比=1
> 作者：AutoModerator　|　发布：2026-10-16T06:01:02+08:00
> 项目链接：—
> 采集：2026-10-26T09:43:54+08:00　|　id：`25f5446213e69251`

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

## 评论（198/259）

> **akspad**（3 分） · 2026-10-16T06:27:54+08:00　
> **Project Name:** Newsletter to Podcast
>
> **Repo:** [https://github.com/akspad/newsletter-to-podcast](https://github.com/akspad/newsletter-to-podcast)
> **Audio demo:** [https://akspad.github.io/newsletter-to-podcast/](https://akspad.github.io/newsletter-to-podcast/)
> **License:** MIT
>
> **Description:**
>
> Newsletter to Podcast is an open-source Python tool that **turns newsletters and blogs into an RSS podcast feed!** You can pick the sources, generate audio, and subscribe to the resulting feed in a podcast app that supports custom RSS (I use Castbox).
>
> The project supports full article narration as well as spoken summaries. Full narration uses Edge TTS and needs no API key; summaries use Gemini and require your own key (though the free limit is quite generous)! You can set a maximum episode length and longer full readings split into numbered parts at natural text boundaries.
>
> There’s a prerecorded sample on the demo page, and a simple command in the README that fetches an original sample article and generates fresh audio without an API key. The package can run locally or on a schedule in your own GitHub repository using GitHub Actions!
>
> **Deployment:**
>
> Run it locally with Python 3.12+ or use the included GitHub Actions workflow (recommended, and setup instructions are in the GitHub README). You host the generated MP3s and RSS feed wherever your podcast app can reach them.
>
> Speech generation uses Microsoft’s online Edge TTS service (which is unofficial and can break or be throttled sporadically...) Optional summaries send article text to Gemini to be summarized. GitHub Pages publishing is available, but makes the generated feed and audio public (I use this since it's free hosting)!
>
> **AI Involvement:**
>
> I painstakingly steered AI to help creating this tool! In the application itself, article summaries use AI (Gemini) but are optional. Full narration skips the summarization step and uses text-to-speech directly.
>
> **Motivation:**
>
> I wanted to turn some of my favorite newsletters into podcasts (like Seth’s Blog and A Learning A Day) and couldn’t find a free and simple solution that already existed. Let me know what you think!

---

> **Obvious_Limit_361**（10 分） · 2026-10-16T06:29:33+08:00　
> my plant naming system has gotten completely out of hand and now i'm tempted to name a server rack after a fern just to see what happens
>
> been lurking here for ages and half these projects make me feel like i'm running a kindergarten while y'all are out here building spaceships

---

> **akspad**（4 分） · 2026-10-16T06:32:54+08:00　
> Can't have spaceships without kindergarten tho!

---

> **FabricatorCH**（5 分） · 2026-10-16T06:33:42+08:00　
> * **Project Name: Stop Bots**
> * **Repo/Website Link:** [https://github.com/ivankovic/stop-bots#stop-bots](https://github.com/ivankovic/stop-bots#stop-bots)
> * **Description:** A TUI and a CLI that help you configure your server to stop bad bots without hiding behind a CDN. It is a fancy UI for your existing web server (nginx or Apache) and your firewall (nftables or iptables). For those of us that don't want to hide behind Cloudflare and give one company the keys to all kingdoms.
> * **Deployment:** `cargo install stop-bots`if you have Rust. Debian package is available [https://github.com/ivankovic/stop-bots#install](https://github.com/ivankovic/stop-bots#install) if you would prefer to go that way.
> * **AI Involvement**: Yes. My AI use policy aligns more or less with Linus Torvalds and Uncle Bob Martin.
>
> I have been self-hosting for years, but I have been "family hosting" for the last 2 years. I have to support non-technical users with various hardware, so some of my services really can't just be hidden behind a VPN.
>
> I built this little TUI app to help me beef up the security of my server. I don't know about you, but I have seen a massive increase in attacks since about May/June this year. The Internet is becoming a scary place, and firewall + WAP management is a good first line of defense.
>
> One thing I would highly recommend any self-hosters that don't host any public content, i.e. anyone "family hosting", is to use the Geoblock Allowlist and just block the rest of the world. If in addition to that you also enable the "Humans only" switch, you will be significantly more likely to survive unscathed when those scary Internet wide CVEs come along. In my case, the attack volume goes from 15 000 a week to just 525, a 30x reduction.

---

> **fernandops**（2 分） · 2026-10-16T07:02:24+08:00　
> What happens if the scheduled run fails halfway through a long article? Keeping the finished parts and retrying only the missing ones would be useful with a TTS service that can throttle. The feed should only list an episode once its audio is ready, so the podcast app doesn’t pick up a broken download.

---

> **fernandops**（5 分） · 2026-10-16T07:02:58+08:00　
> A preview of the exact firewall and web server changes would help here, especially for people running it over SSH. Show what gets added or removed, and let them save the current configuration before applying it. A “what changed?” view would also make troubleshooting a blocked family member much easier.

---

> **kryoseu**（6 分） · 2026-10-16T07:07:26+08:00　
> **Project Name:** WyrmRSS - A self-hosted RSS reader and aggregator for web and mobile, also available as a desktop app.
>
> **Repo/Website Link:**  https://github.com/kryoseu/WyrmRSS.
> Live demo (shared, mostly read-only, resets daily): [https://demo.wyrmrss.com](https://demo.wyrmrss.com)
>
> **Description:** It's a self-hosted RSS/Atom reader and aggregator for web and mobile, with an optional native desktop app. I've been building it for 5 months now. I'm a software dev with 10 years of experience who's building this as a hobby project. I wanted something simple to host, and good for following both blogs and YouTube channels in one place, with features I like built-in, without the need of extensions and add-ons.
>
> **Features**:
>
> \- *Feed discovery*: paste a blog homepage or a YouTube channel URL and Wyrm finds the feed.
>
> \- *YouTube support*: subscribe to channels and watch videos inline in the reader.
>
> \- *Per-feed display modes*: River (home timeline), Feed only, or Radar (a quiet grid you check when there's nothing else to read).
>
> \- *Folders with unread counts*, preserved through OPML import/export.
>
> \- *Per-feed filters*: exclude entries by URL, title or content, e.g. url:/shorts to drop YouTube Shorts.
>
> \- *Read Later and Archive*. Archived posts are kept even if the feed is deleted.
>
> \- *Webhooks for new posts*: Discord, Slack or a custom template.
>
> \- *Full-text search* across post titles and descriptions.
>
> \- *Runtime settings in the UI*, no restart needed: poll interval, HTTP timeouts and retries, page size, mark-as-read mode and delay, and automatic deletion of old posts.
>
> \- *Mobile-friendly PWA* with a tab bar and card or title-only layouts.
>
> \- *Optional API key* to lock down the instance.
>
> \- *Read mark delay*.
>
> \- ***Keyboard shortcuts*** on next release.
>
> **Stack**: Rust (actix-web, Diesel, Tokio) and PostgreSQL on the backend, React on the frontend. The desktop app is Tauri with an embedded SQLite database, so there's no server or database to set up. GPL-3.0. Fully free and open-source.
>
> **Deployment**:
>
> \- Docker Compose:  guide and compose file: [docs/installation/docker.md](https://github.com/kryoseu/WyrmRSS/blob/main/docs/installation/docker.md).
>
> \- Kubernetes: manifests in [docs/templates/kubernetes.yaml](https://github.com/kryoseu/WyrmRSS/blob/main/docs/templates/kubernetes.yaml).
>
> \- Desktop app for macOS, Windows and Linux: [docs/installation/desktop.md](https://github.com/kryoseu/WyrmRSS/blob/main/docs/installation/desktop.md).
>
> \- From source: [docs/installation/source.md](https://github.com/kryoseu/WyrmRSS/blob/main/docs/installation/source.md).
>
> **AI Involvement**:
>
> The backend is mostly hand-written. I did rely more on LLM for the frontend as it's not my strongest area. However I have carefully reviewed and am confident in everything I've pushed to the repo. I'm a Software Engineer with over 10 years of experienced, I have worked at AWS and now I work at Mozilla. This is a hobby project.
>
> I have put a lot of time and energy into this project and have been working and maintaining it for 5 months now. By no means I consider this AI slop.
>
> The logo was designed and created by a tattoo artist from Brazil. His profile is on the repo's [README](https://github.com/kryoseu/WyrmRSS/blob/main/README.md).

---

> **FabricatorCH**（1 分） · 2026-10-16T07:11:39+08:00　
> It displays a preview before applying and will automatically do its hardest to stop you from locking yourself out over ssh.

---

> **3loodhound**（3 分） · 2026-10-16T07:13:00+08:00　
> \*\*Project Name:\*\* CloudRcade
>
> \*\*Repo/Website Link:\*\* https://github.com/jacoknapp/cloudrcade
>
> \*\*Description:\*\* A self-hosted fork of webRcade for playing your own game library directly in a browser. Emulation runs on your device, while your server hosts the application and game files. Features include Nextcloud/Dropbox save sync, customizable touch controls, automatic ROM scanning, Recently Played, and offline caching for supported games.
>
> \*\*Supported consoles and handhelds:\*\*
>
> \- \*\*Nintendo:\*\* NES/Famicom, SNES/Super Famicom, Nintendo 64, GameCube, Game Boy, Game Boy Color, Game Boy Advance, Nintendo DS, Nintendo 3DS, Virtual Boy, and Pokémon Mini.
> \- \*\*Sony:\*\* PlayStation, PSP, and PlayStation 2 (experimental beta).
> \- \*\*Sega:\*\* SG-1000, Master System, Genesis/Mega Drive, Sega CD/Mega-CD, Game Gear, and Saturn (experimental).
> \- \*\*Atari:\*\* 2600, 5200, 7800, and Lynx.
> \- \*\*NEC:\*\* PC Engine/TurboGrafx-16, PC Engine CD/TurboGrafx-CD, SuperGrafx, and PC-FX.
> \- \*\*SNK:\*\* Neo Geo, Neo Geo CD, Neo Geo Pocket, and Neo Geo Pocket Color.
> \- \*\*Bandai:\*\* WonderSwan and WonderSwan Color.
> \- \*\*Others:\*\* 3DO, ColecoVision, Bally Astrocade, and Philips CD-i.
>
> Also includes arcade support through FinalBurn Neo, computer emulation, and game engines such as Doom, Quake, and ScummVM. Some inherited systems require custom webRcade feeds or experimental settings; automatic folder scanning currently covers a subset.
>
> GameCube and PS2 require hardware WebGPU. Compatibility and performance vary by game and device. You supply your own games and any required BIOS files or keys. Credit to webRcade and the upstream emulator projects.
>
> \*\*Deployment:\*\* Docker images through GHCR, with a Docker Compose example and setup documentation in the repository. Main releases support AMD64 and ARM64; the PS2 beta image is AMD64-only. Requires an HTTPS gateway, persistent configuration storage, and your ROM folders.
>
> \*\*AI Involvement:\*\* Honestly a lot

---

> **anitamaxwynnn69**（3 分） · 2026-10-16T09:13:30+08:00　
> **Project Name:** [www.overtchat.com](http://www.overtchat.com)
>
> **Repo/Website Link:** [https://github.com/yoloyash/overtchat](https://github.com/yoloyash/overtchat)
>
> **Description:** A lightweight self-hosted chat client, alt to Open WebUI. I built it because my partner and family use ChatGPT but don't care about privacy. I already self-host vLLM on 8x 3090s and wanted a polished, private alternative they could actually use. OWUI is too heavy and complex for non-technical users. overtchat is chat-first with built in tts/stt/search, no rag/plugins/agentic bloat, no external api keys. Free native [Android](https://play.google.com/store/apps/details?id=com.overtchat.mobile) and [iOS](https://apps.apple.com/app/overtchat/id6812165221) Apps, plus a [desktop app](https://github.com/yoloyash/overtchat/releases/tag/desktop-v0.2.0) for macOS (Apple Silicon/Intel) and Linux (AppImage/Deb/RPM). MIT licensed, no telemetry, no analytics.
>
> **Deployment:** One `docker compose up` and you're in. \~1 GB RAM. Docs at [https://github.com/yoloyash/overtchat/blob/main/docs/deploy.md](https://github.com/yoloyash/overtchat/blob/main/docs/deploy.md)
>
> **AI Involvement:** Yes, definitely vibe coded.
>
> Would love to have some feedback :)

---

> **AldyErnesto**（1 分） · 2026-10-16T09:27:12+08:00　
> Project Name: Shotstash
>
> Repo/Website Link:
>
> GitHub: [https://github.com/Aldyernesto/shotstash](https://github.com/Aldyernesto/shotstash)
>
> Docs: [https://aldyernesto.github.io/shotstash/](https://aldyernesto.github.io/shotstash/)
>
> Read-only demo (resets nightly): [https://demostash.aldyernesto.my.id](https://demostash.aldyernesto.my.id)
>
> Description:
>
> A self-hosted media cloud for people who shoot video for work, alone or in a small team. It turns a PC, NAS or spare drive into a place to keep footage and hand it to clients. It is not a phone photo backup (Immich does that well) and not a heavy enterprise DAM.
>
> \- Projects and sections, search, grid and list views
>
> \- Resumable chunked uploads in the browser that survive bad Wi-Fi and reloads, checksum-verified, with duplicate detection
>
> \- A viewer that keeps portrait video portrait
>
> \- Share links per file, section or project, public or with an access code, with ZIP download
>
> \- Roles (admin, crew, editor, viewer) with account approval
>
> \- Storage on a local disk, a NAS mount or any S3-compatible bucket (MinIO, R2, AWS and others)
>
> \- An optional worker contract for proxies, transcription or scene detection; a 720p proxy worker is included
>
> MIT licensed, no paid tier, no telemetry.
>
> Deployment:
>
> Docker Compose with published images (amd64 and arm64), so nothing builds on your machine. One command:
>
> git clone [https://github.com/Aldyernesto/shotstash.git](https://github.com/Aldyernesto/shotstash.git) && cd shotstash && sh docker/init.sh && docker compose up -d
>
> The init script checks your machine and writes .env with random secrets. The app, PostgreSQL, Dragonfly and the worker run in Compose, and only the app port is published. About 2 GB of RAM. Install, configuration, backup/restore and the API are documented in the docs above.
>
> AI Involvement:
>
> I used AI coding assistants a lot while building it, the way you'd use a fast pair programmer. I review and own every change I merge, and every change goes through CI: about 370 tests plus end-to-end suites for per-role authorization, resumable uploads, backup and restore, and the worker contract. The code started as a media system a small team uses daily before I extracted it into this repo.
>
> Feedback on what breaks, or what you'd want a worker to do, is very welcome.

---

> **kitsunetrail**（3 分） · 2026-10-16T09:39:49+08:00　
> **Project Name:** KestreLynx
>
> **Repo/Website Link:** [https://github.com/kitsunetrail/kestrelynx](https://github.com/kitsunetrail/kestrelynx)
>
> **Description:**
>
> I shared this project here before under the name StackWatch. Since then I've renamed it and added new features, so I'd like to introduce it again.
>
> Dealing with vulnerabilities takes time: checking the impact, looking for fixed versions, and doing the updates.
> KestreLynx regularly scans the images used by your running containers with Trivy, and for vulnerabilities that have a fixed version, it creates the update as a GitHub pull request.
> Each PR includes a comparison of Trivy scans before and after the update, so you can see which vulnerabilities it resolves before you merge.
> Scan results are prioritized with CISA KEV and EPSS and sent to Slack or a webhook.
>
> Fix PRs are an experimental feature (disabled by default). Current support:
>
> * Environment: Docker Compose
> * Images: tags of published images, Dockerfile base images
> * Language packages: npm, pnpm, pip, uv
> * Git hosting: GitHub
>
> I plan to keep extending support to Kubernetes and other languages.
>
> **Deployment:**
>
> Multi-arch Docker images are published on GHCR, and you can set it up with Docker Compose.
> See the README for the steps:
>
> [https://github.com/kitsunetrail/kestrelynx#quick-start-docker](https://github.com/kitsunetrail/kestrelynx#quick-start-docker)
>
> **AI Involvement:**
>
> I write and review the design and implementation plan documents together with AI, and the implementation is done by AI.
> I've been running it on my own production VPS since June 2026. I test it myself, and bugs I find are also fixed by AI.

---

> **SC-Admin567**（0 分） · 2026-10-16T09:54:33+08:00　
> I built a self-hosted tool that keeps your GitHub traffic/release stats forever (GitHub only keeps 14 days).
>
> https://preview.redd.it/5jp17crujqvh1.png?width=1028&format=png&auto=webp&s=aa1b3053c17de9f44c6162c0f7a7f7033f6ef36e
>
> GitHub's own traffic API (Application Programming Interface) (clones,
>
> views, referrers, popular content) only retains a rolling 14-day
>
> window — once it ages out, it's gone for good, even for your own
>
> public repos.
>
> I built GitPerennial to fix that. It runs entirely on your own machine,
>
> polls the GitHub API on a schedule using your own personal access token
>
> (PAT), and keeps a permanent local history in SQLite (a lightweight,
>
> file-based database). Nothing leaves your computer except the API
>
> calls to GitHub itself — no third-party server sees your token or your
>
> data.
>
> What it does:
>
> \- Tracks clones, views, referrers, popular content, release downloads,
>
> and issue metrics over time (not just the 14-day window GitHub gives you)
>
> \- Track repos across more than one GitHub account or org — new in
>
> v1.1.0, add a PAT per account/org and it automatically uses the
>
> right one per repo
>
> \- Gap detection — if your machine is off when a poll was due, it tells
>
> you exactly why a day is missing and self-heals automatically once
>
> you're back online
>
> \- Local dashboard in your browser, CSV (Comma-Separated Values) export,
>
> printable reports
>
> \- Native installers for Windows, macOS (Apple Silicon), and two Linux
>
> families: .deb (Debian/Ubuntu/Mint, tested on Ubuntu 24.04-based Linux
>
> Mint) and .rpm (Fedora, tested on Fedora 44 with KDE and GNOME)
>
> Licensing: free tier tracks 1 repo forever at full depth, no time limit.
>
> A one-time purchase unlocks unlimited repos — no subscription.
>
> It's closed-source (the repo has docs + installers only), but genuinely
>
> self-hosted — I don't want to run a SaaS (Software as a Service) or
>
> hold anyone's GitHub token.
>
> Repo/docs: [https://github.com/SC-Admin567/GitPerennial](https://github.com/SC-Admin567/GitPerennial)
>
> Happy to answer questions about the architecture, the licensing model,
>
> or anything else.

---

> **en3r0**（1 分） · 2026-10-16T10:44:01+08:00　
> **Project Name**: trilium-tui
>
> **Repo/Website Link**: [https://github.com/en3r0/trilium-tui](https://github.com/en3r0/trilium-tui)
>
> **Description**: A terminal client for Trilium Next. It keeps a local copy of your notes and syncs with your Trilium server in the background, using the same protocol as the official desktop app, so it is instant and keeps working when the server is down. You can edit formatted notes in place (tables, lists, note links, inline pictures), search with Trilium's full query syntax, and script everything with the bundled \`trilium-cli\`. For those of us who live in a terminal and don't want a browser tab open just to jot something down.
>
> **Deployment**: Prebuilt Linux binaries (x86\_64 and aarch64) are on the releases page: https://github.com/en3r0/trilium-tui/releases/tag/v0.1.0. Download, unpack, run \`./install.sh\`. No Rust or OpenSSL needed. Or build from source with Rust: \`git clone https://github.com/en3r0/trilium-tui && cd trilium-tui && packaging/install.sh\`. To try it without a server: \`trilium-tui --new\`.
>
> **AI Involvement**: Yes. Most of the code was written with Claude Code, working from my direction. I enjoy getting to make the design decisions and the major direction choices.
>
> https://preview.redd.it/co0cq6p9sqvh1.png?width=1600&format=png&auto=webp&s=9065a19c5f97fc4d1e40817a748babd2dacc178a
>
> Trilium Next (https://github.com/TriliumNext/Notes) is the one self-hosted app I use every day. Its a web app, but I really enjoy the terminal, so I built this in Rust to get at my notes with raw speed.
>
> It keeps a local SQLite copy of your notes and syncs in the background. Edits made offline are pushed when the server is back. The editor only rewrites the paragraph you touch, so the rest of a note is saved byte for byte.
>
> Since it writes to your server, a few things to know: it is v0.1.0, Linux only for now, and I tested it against Trilium v0.106.0. It makes a daily local backup and keeps unsaved text if a save ever fails, but please take a Trilium backup before your first sync. AGPL-3.0, no telemetry.
>
> More detailed write-up: [https://dustinmontgomery.com/blog/trilium-tui/](https://dustinmontgomery.com/blog/trilium-tui/)
>
> Feedback and bug reports are welcome.

---

> **East_Watercress_3764**（1 分） · 2026-10-16T11:53:36+08:00　
> **Project Name:** Syntrabase
>
> **Repo/Website Link:** [https://github.com/Animeki004/Syntrabase](https://github.com/Animeki004/Syntrabase)
>
> **Description:**
>
> I've been building Syntrabase, an open-source, self-hosted alternative to Firebase, powered by PostgreSQL, Fastify, and TypeScript.
>
> The goal is to give developers a Firebase-like backend experience while keeping full control over their own infrastructure.
>
> It includes a document database, authentication, security rules, file storage, realtime updates, and developer SDKs, along with a web-based Developer Console and Super Admin panel.
>
> The project is still evolving, and I'm working on improving its reliability, security, and ease of deployment. I'd love to hear feedback, suggestions, and contributions from the community.
>
> **Deployment:**
>
> * **Deployment options:** Docker and Coolify.
> * **Setup:** Clone the GitHub repository and follow the README for configuration and deployment instructions.
> * **Status:** Open source and under active development.
>
> **AI Involvement:**
>
> Syntrabase is a vibe-coded project, with AI generating most of the code. I've used AI extensively to build features, debug issues, and work on the overall architecture. I'm continuing to test, review, and improve the application as it evolves.
>
> The project is open source, and I'd appreciate honest feedback from the self-hosting community on what works, what needs improvement, and what features would be useful.

---

> **Astravor**（8 分） · 2026-10-16T12:44:31+08:00　
> Project Name: Zim Pro
>
> Repo/Website Link: [https://github.com/magicstack-llp/zim-pro](https://github.com/magicstack-llp/zim-pro)
>
> Description:
> Zim Pro is a self-hosted, offline AI knowledge base built on ZIM files (offline Wikipedia, Stack Exchange, DevDocs, iFixit and the rest of the Kiwix catalog). It replaces kiwix-serve and keeps the same /content/ URLs.
>
> The problem it solves: kiwix-serve is great for reading, but you can't ask your library questions, keeping books updated is manual, and other AI tools can't use it. Zim Pro does all three.
>
> Features:
> \- Read and full-text search every book, or search across the whole library at once
> \- Ask AI: answers written from your books, with numbered clickable citations and the images/videos from the source pages. Works with any OpenAI-compatible API (Ollama, LM Studio, llama.cpp, vLLM, OpenAI, Gemini, OpenRouter, etc.)
> \- Fully offline with a local model. Internet is only used to download/update books, plus web search if you turn it on (off by default)
> \- Built-in MCP server (HTTP or stdio), so Claude and other LLM apps can search and read your library. Per-app API keys that can be revoked
> \- Auto-updates from the Kiwix catalog with a per-book policy (automatic, ask first, or pinned). Multi-connection downloads that are checksummed and resume after a crash
> \- Create your own ZIMs from websites (respects robots.txt, sitemaps, rate limits) and from PDF, EPUB, MOBI and AZW3 books
> \- Turn RSS/Atom feeds into ZIMs, synced on a schedule and fetching only new articles
> \- Any article as Markdown
> \- Mobile-friendly and installable as a PWA
>
> Who benefits: anyone who keeps an offline library for preppers, homelabs, travel or air-gapped setups, and anyone running local LLMs who wants grounded, cited answers instead of hallucinations.
>
> Deployment:
> \- Docker image: ghcr.io/magicstack-llp/zim-pro (amd64 + arm64)
> \- docker-compose examples in the README, plus ready-made compose files in docker/ for optional extras (Gluetun VPN, FlareSolverr captcha solver, Zimit browser capture)
> \- Also available as a standalone Linux binary (x86-64/arm64) from Releases, or with pip install zim-pro / uvx zim-pro
> \- The README covers install, configuration (env vars), Ask AI, MCP setup and security notes
>
> Quick start:
> mkdir -p zims state
> docker run -d --name zim-pro --restart unless-stopped \\
> \--user "$(id -u):$(id -g)" -p 8083:8080 \\
> \-v "$PWD/zims:/data" -v "$PWD/state:/state" \\
> \--add-host host.docker.internal:host-gateway \\
> ghcr.io/magicstack-llp/zim-pro:latest
> Then open http://localhost:8083
>
> AI Involvement:
> Developed with Claude.
> ￼
> ￼

---

> **busters1**（1 分） · 2026-10-16T13:44:34+08:00　
> **Project Name:** Oxynote
>
> **Repo:** [https://github.com/oxynote/oxynote](https://github.com/oxynote/oxynote)
>
> **Description:**
>
> With Oxynote, your notes and your graphs stop drifting apart. The explanation and the live chart live on the same page, so when you open it a year from now, you see what the system is doing now next to why you set it up that way. Anyone you share the page with sees the same chart, with no Grafana account and no second login. It works with Prometheus, Postgres, MySQL, and MariaDB.
>
> In a homelab that looks like: "the NAS pool threshold sits at 85% because scrubs need headroom", with the real disk usage graph right under that sentence. A year from now you'll know why you picked 85.
>
> Other notable features:
>
> \- Reviews. Mark a page reviewable and edits go into a draft. The diff understands blocks, so a changed query, a renamed field, and a reworded sentence all show up in one view. Approve, merge, and optionally lock main.
>
> \- Pages that alert you when they go stale. A page can watch a GitHub file, a container image, or a URL, and its maintainers get a ping when that changes.
>
> \- Live editing with comments you can pin to a word, a diagram line, or a chart.
>
> \- Stripe-style API docs for your own services: request on the right, fields on the left, and a latency chart next to them if you want one.
>
> \- Optional assistant with your own model (Ollama works), plus an MCP server.
>
> What it isn't: a general notes app. It's built for documenting systems, the stuff you run and need to explain later.
>
> Deployment: one container with the database built in, amd64 and arm64.
>
>     docker run -d --name oxynote -p 8080:8080 \
>     -v oxynote_data:/oxynote/data ghcr.io/oxynote/oxynote:latest
>
> **AI Involvement:** Yes, I use AI coding agents for much of the implementation. What keeps it from turning into slop is how I've always run my projects: strict linters, a test-coverage gate that fails the build, and an opinionated style guide the agents must follow (it's in the repo as AGENTS.md). I review every change before it lands (using plannotator).
>
> How do you document your homelab today? A notes app, a git repo, or the setup that lives only in your head? I'm curious what would make a tool like this worth switching for.

---

> **logz_erroneous**（4 分） · 2026-10-16T13:46:18+08:00　
> **Project Name:** Quomodo
>
> **Repo/Website Link:** [https://github.com/LoganRupe/quomodo](https://github.com/LoganRupe/quomodo)
>
> **Description:** A hard fork of Komodo for people running podman instead of Docker. Komodo is great, but it's built around docker compose. I wanted the same git-driven deploys and web UI with podman quadlets as the deploy unit, and rootless as a first-class option.
>
> A stack is a directory of `.container` / `.pod` / `.build` files in git. A push (GitHub, Forgejo, Gitea or GitLab webhook) installs it on the target host, reloads systemd, and restarts only the units whose files changed. Change one line in `gitea.container` and only gitea restarts; everything else keeps its uptime. A redeploy also starts any unit that failed. The video at the top of the readme shows the loop.
>
> What I couldn't get elsewhere:
>
> * **Rootless, one agent per user.** Start the agent as a user and it deploys that user's rootless quadlets with `systemctl --user`. Each user agent is its own server in the UI, so you can give every stack its own service user. No root process holds the connection to Core, so a compromised Core reaches that user, not the host. A root agent is still there for anything that needs ports below 1024.
> * **Stable user namespaces.** Every pod gets a fixed 65536-id slice of the subordinate range, written as `UIDMap=`/`GIDMap=`. A redeploy never moves the container's root uid, so volume files don't turn into `nobody`. `:idmap` fixes the same symptom, and it still works here, but slices also keep each stack on its own host ids and work on NFS, where idmapped mounts don't.
> * **No secrets at rest.** `\[[NAME\]]` in a stack file is read from Vaultwarden/Bitwarden at deploy time and created as a podman secret. Nothing resolved lands in the database or in the unit files.
> * **Agents only dial out**, over wss. No inbound port on your hosts.
>
> Alerts go to Slack, Discord, ntfy, Pushover or a webhook. Login is local, OIDC or API keys.
>
> **Deployment:** Core (UI + API + mongo) runs as a podman pod. The quadlet files are in `example/quomodo-core`, and the image is `ghcr.io/loganrupe/quomodo` (amd64 and arm64). The agent is a single binary on the releases page for x86\_64 and aarch64. You need podman 5.0+, systemd, and TLS in front of Core; a rootless agent also needs linger and subuids for its user. Install guide: [https://github.com/LoganRupe/quomodo/blob/main/docs/install.md](https://github.com/LoganRupe/quomodo/blob/main/docs/install.md)
>
> There's no docker or compose support (removed on purpose) and no migration from Komodo, so stacks have to be rewritten as quadlets. It's 0.x and runs my home lab: 42 agents on 14 machines, most of them rootless.
>
> **AI Involvement:** A lot. Komodo is the base, and that's years of upstream work by its author. My fork changes were written mostly with Claude Code. I designed them, reviewed them and run them on my own hosts every day, and there's an end-to-end test that deploys real root and rootless quadlets in a systemd container. Komodo's author is happy with the fork as long as it credits Komodo, which the readme does in its first line.

---

> **olivercer**（13 分） · 2026-10-16T14:16:06+08:00　
> https://preview.redd.it/d0srb85nurvh1.png?width=1375&format=png&auto=webp&s=433c2d0b6f5667d9a948b63203e7318945b770ef
>
> * **Project Name**: WhatsApp Backup Tools (wab-tools)
> * **Repo/Website Link**: https://github.com/auanasgheps/whatsapp-backup-tools
> * **Description**:A local-first, 100% offline suite to archive and browse your WhatsApp data on your own storage.
>
> * **wab-archiver**: Turns unstructured WhatsApp backups (Android & iOS, no root required) into a clean, human-readable folder tree: Contacts//// and Groups///, preserving original message timestamps and tracking contact renames.
> * **wab-viewer**: An offline Web UI replica of WhatsApp Web. Scroll across tens of thousands of chat messages, in-browser media player, and full-text search.
>
> This is a project I envisioned about 10 years ago, and honestly, I always thought somebody else would build it before me!
>
> * **Deployment**:Available on PyPI (pip install whatsapp-backup-tools) and GitHub Releases. Requires Python 3.11+.Runs locally on Linux, macOS, and Windows. Run wab-archiver to build the archive, then wab-viewer to spin up the local web UI at localhost:5000.
> * **AI Involvement**:Transparently: I used AI tools as a pair programmer to write code and tests.However, this is **not a vibecoded project**. Archiving personal history requires strict data integrity: the architecture is entirely human-designed, involves deep reverse-engineering of WhatsApp's SQLite/protobuf formats; is backed by **over 570 automated tests** (unit, integration, and headless browser tests) and manual validation as well.

---

> **cypello**（2 分） · 2026-10-16T15:18:57+08:00　
> **Project Name:** EasyPDM
>
> **Repo/Website Link:** https://github.com/pawelcel/EasyPDM (MIT)
>
> **Description:** A lightweight, self-hosted PDM (product data management) system for CAD files. It solves the "`bracket_v3_FINAL_FOR_REAL.SLDPRT` on a shared drive – which one is current?" problem for small engineering teams.
>
> - Unique auto-assigned part/assembly numbers, statuses (in progress → under review → released), revisions with change comments, full history
> - Instant BOM per assembly, CSV export (full or aggregated)
> - Item locking – nobody (admins included) can overwrite what you're working on
> - Shared material and manufacturer catalogs, search across the whole database
> - FreeCAD and SolidWorks macros: Upload/Download straight from the CAD program (downloading an assembly pulls the whole component tree)
> - Per-project access, admin/user roles, PL/EN/DE UI, light/dark theme
>
> Intended to run on your LAN, not exposed to the internet.
>
> **Deployment:** Docker (Dockerfile + docker-compose in the repo): `git clone https://github.com/pawelcel/EasyPDM.git && cd EasyPDM && ./install-easypdm-docker.sh`.
> Also a native Linux install script (systemd service, installs PostgreSQL if missing) and a Windows installer on the Releases page.
> PostgreSQL backend. README + TECHNICAL.md cover installation, updating and uninstalling. Default login is admin/admin, so change it right after the first login.
>
> **AI Involvement:** The whole codebase was written by Claude from my requirements and descriptions. I'm a mechanical design engineer, so I defined the functionality, data model and workflows and use it in my own work, but I did not write the code by hand. This is also stated in the README. It's a young project, so expect rough edges, and feedback is very welcome.
>
> Video walkthrough: https://www.youtube.com/watch?v=ZwAWCJN9tWg

---

> **Alternative_One_4804**（0 分） · 2026-10-16T15:32:07+08:00　
> # I’m thinking of offering a hosted OpenTodo for free, with every feature and no subscription. Weird idea?
>
> I’m having so much fun building OpenTodo. Honestly, I wanted something like it for a long time: a task app that’s completely free, open source, and runs on my own server, where nobody can paywall my tasks or shut the app down.
>
> Self-hosting stays at the heart of it. That won’t change.
>
> But I keep coming back to a slightly weird idea. Not everyone has a server, or wants one. Plenty of open-source projects offer a hosted version, but almost always as the paid part. I’d like to offer one too, but for free:
>
> * every feature, with no “Pro” tier,
> * no subscription,
> * the same code you can run yourself, so you can export your tasks and move to your own server at any time,
> * end-to-end encryption available, as it already is when you self-host.
>
> The obvious question is who pays for the servers. I can personally pay for the first 100-200 users probably, but then my first thought is donations, with the running costs published openly so everyone can see what it takes.
> But I’m honestly not sure that’s enough, and I don’t want to make a promise I can’t keep.
>
> What I’m unsure about:
>
> * **What if donations don’t cover it?** Would a waiting list or storage limits be fair, as long as every feature stays?
> * **Trust.** Would you put your tasks on a free service run by one person? What would you need: a promise of plenty of notice and a full export if it ever closes, encryption, something else?
> * Attachments, webhooks and email to task are what spammers love on free services. Would stricter limits on those be acceptable?
>
> So, what do you think?
>
> Do you know projects that did this well, or that got it badly wrong?
>
> Nothing is decided. If your answer is “keep it self-hosted and don’t spread yourself thin”, I’d like to hear that too.
>
> If you haven’t seen OpenTodo yet: [website](https://open-todo.app) \- [demo](https://demo.open-todo.app) (no sign-up) · [GitHub](https://github.com/pixari/opentodo)

---

> **Then_Elephant_9697**（1 分） · 2026-10-16T16:15:40+08:00　
> **FlowForge**: open-source workflow automation (an n8n / Zapier alternative) that runs on plain PHP shared hosting
>
> I run small-business automations for clients who only have cPanel or Hostinger hosting, where n8n doesn't fit (no Node, no Docker, no long-running processes). So I built one that needs only PHP 8.2, MySQL and a single cron job.
>
> * Visual canvas with triggers, If/Else and filters, plus a step debugger that keeps every step's input and output
> * 1,690 app integrations (each app is a JSON manifest, so adding one takes no code), plus an HTTP step for anything else
> * AI builder: describe a workflow and it builds it. Bring your own key: OpenAI, Claude, Gemini, DeepSeek, or any OpenAI-compatible endpoint, including Ollama
> * Missing app? The AI adds it from the service's API, or you import its OpenAPI file
> * Automatic retries from the failed step, so nothing is sent twice. Steps can retry, keep going on failure, or be turned off
> * Optional AI voice agents (Vapi / ElevenLabs) for phone answering and bookings
> * MCP server, so Claude Code or Cursor can build and run workflows
> * One-click updates from GitHub releases, with backup and rollback
>
> License: AGPL-3.0, no paid tier and no limits.
>
> Repo: [https://github.com/DeveloperSarim/FlowForge](https://github.com/DeveloperSarim/FlowForge) Docs and screenshots: [https://developersarim.github.io/FlowForge/](https://developersarim.github.io/FlowForge/)
>
> It's young (first public release this month), so feedback and bug reports are very welcome. I'm the developer.
>
> https://preview.redd.it/bp7jlsryfsvh1.png?width=590&format=png&auto=webp&s=845502ee0aacaad649514d3c992f0239479c5436

---

> **maurek_99**（2 分） · 2026-10-16T16:44:24+08:00　
> So uuuh, hello, yesterday i made a post releasing a new theme for feishin based on [Fluentshin](https://github.com/ZortexSenpai/fluentshin) by [u/ZortexSenpai](https://github.com/ZortexSenpai). And it was good, but i thought, i can make it even better, so me and gemini lost our minds trying to improve it even more, and now i can proudly say, this is probably the definitive edition of the theme, so feel free to download it and test it for yourselves [Spotifeishin](https://github.com/maurek99/spotifeishin)

---

> **HiimKami**（1 分） · 2026-10-16T17:38:14+08:00　
> **Project Name:** Uptimy Agent
>
> **Link:** [github.com/uptimy/agent](https://github.com/uptimy/agent)
>
> **What it is:** I build Uptimy, a hosted service that monitors websites, APIs and cron jobs from several regions and runs incidents and public status pages. The agent is the open-source, self-hosted monitoring piece, written in Go and licensed Apache-2.0, and it's the better fit if you'd rather run everything yourself. No account needed, everything works standalone.
>
> It covers HTTP, Postgres, MySQL and Redis (real logins and queries, not just an open port), ping, TCP, DNS, TLS expiry, and heartbeats for cron jobs and backups. It has a public status page with incidents and maintenance windows, alerts to email, Slack, Discord, Telegram, ntfy, PagerDuty, webhooks and 30+ more through Shoutrrr, plus 2FA, viewer roles and Prometheus metrics.
>
> A few things that might matter here:
>
> - **It's light:** a 9 MB image with embedded SQLite. It idles at 8 MiB of memory and uses 25 MiB with 350 monitors (benchmark against Uptime Kuma is in the repo)
> - **Coming from Uptime Kuma?** Upload your `kuma.db` and pick what to import: monitors, notifications and status page groups carry over
> - **Kubernetes:** label a Service, Ingress or Deployment with `upti.my/monitor: "true"` and it's monitored within 30 seconds. CronJobs are tracked from their Jobs, no ping needed
> - **Monitors as code:** define them in YAML, or click them together in the UI
>
> **Deployment:**
>
> Docker:
>
>     docker run -d --name uptimy-agent -p 8080:8080 -v uptimy-agent:/data ghcr.io/uptimy/agent
>
> Open http://localhost:8080 and sign in as `admin` with the password printed in `docker logs uptimy-agent`. There's also a `docker-compose.yml` in the repo, a signed Helm chart (`helm install uptimy-agent oci://ghcr.io/uptimy/charts/uptimy-agent`) and a one-click Railway template. All config options are in the README.
>
> **AI Involvement:** I use AI as a coding assistant. It helps with boilerplate, tests, and the UI. Architecture, the check engine and security-sensitive parts (auth, 2FA, credential handling) are designed and reviewed by me. Everything goes through CI with tests and linting before release.
>
> Happy to answer questions or go into how any part of it works.

---

> **Suitable_Awareness58**（1 分） · 2026-10-16T18:32:36+08:00　
> Open source small tts
> loudness-tts is a small text-to-speech server you run yourself. It speaks OpenAI's /v1/audio/speech API, so anything that supports OpenAI TTS can use it by changing the base URL.
>
>     docker run -d --name loudness-tts -p 8880:8880 -v loudness-tts:/data ghcr.io/loudness-ai/loudness-tts
>
> \- CPU only: about 20x faster than real time with medium voices on a laptop; one synthesis at a time by default, more with --workers
>
> \- 1,683 open voices in 31 locales, each downloaded once from its publisher and checked against its checksum; then it works fully offline (LOUDNESS\_TTS\_OFFLINE=1)
>
> \- no telemetry, text is never logged or stored; optional API key (--api-key) and CORS
>
> \- MP3, Opus, AAC, FLAC (FFmpeg is in the image), WAV, or streamed PCM
>
> \- /v1/tts returns JSON with the audio, word timings and SRT/VTT subtitles
>
> \- preload languages at start: -e LOUDNESS\_TTS\_PRELOAD="en-US de-DE"
>
> Install guide (Python, JavaScript, Docker): [https://loudness.ai/developers/guides/install-loudness-tts/](https://loudness.ai/developers/guides/install-loudness-tts/)
>  (GPL-3.0): [https://github.com/Loudness-ai/loudness-tts](https://github.com/Loudness-ai/loudness-tts)
>
> Source
> Browser demo: [https://huggingface.co/spaces/Loudness-ai/text-to-speech-browser](https://huggingface.co/spaces/Loudness-ai/text-to-speech-browser)
>
> The image is amd64 and arm64, so it runs on a Raspberry Pi 5 class machine too (slower). Feedback welcome.

---

> **ChrisTheLama**（8 分） · 2026-10-16T18:48:52+08:00　
> https://preview.redd.it/ye04eobt6tvh1.png?width=2880&format=png&auto=webp&s=6c8ff17d34bac1936542a985bb6dde9f47e6aad6
>
> **Project Name:** Game Vault
>
> **Repo/Website Link:** [https://github.com/botchris/game-vault](https://github.com/botchris/game-vault)
>
> **Description:** A self-hosted catalog of every game you own (store libraries, Humble keys and physical discs), used from any browser. I own games across Steam, Epic, GOG, [Battle.net](http://Battle.net), EA, Ubisoft, Xbox and PlayStation, plus a pile of unredeemed Humble keys and shelves of discs, and could never answer *“do I already own this?”* before buying. Game Vault puts every copy of every game in one place:
>
> * **Store libraries imported and kept up to date:** Steam, Epic, GOG, Battle.net, EA app, Ubisoft Connect, Xbox, PlayStation, Amazon, itch.io. **Humble Bundle keys** come in with their redeem deadlines.
> * **Physical games:** scan barcodes with your phone. 118 systems (NES and Mega Drive to Switch 2, classic computers), with region, condition, edition and shelf, plus second-hand value from CeX and eBay.
> * **Keys:** unredeemed, expiring soon, and the ones you don’t need because you already own the game.
> * **Home page:** deals on games you *don’t* own (IsThereAnyDeal) and upcoming releases in your series (IGDB). A browser extension marks what you own on Steam, GOG, Humble and Fanatical pages.
> * **Notifications** (Telegram, ntfy, webhooks), box art and metadata, custom fields, CSV import/export.
>
> Store access: most stores have no official library API, so it signs in the way their own apps or open-source launchers (Heroic, Legendary, Playnite) do, and **only reads**. Fanatical and SteamGridDB forbid automated access, so they are off until you accept the risk. Store sessions are stored unencrypted in the database, so keep the volume private (`SECURITY.md` explains the access model). Source-available license (PolyForm Noncommercial), not OSI open source. One-person hobby project, beta, English and Spanish UI.
>
> **Deployment:** one Docker image (amd64/arm64), SQLite, no external services needed:
>
> `docker run -d -p 8080:8080 -v game-vault-data:/config botchrishub/game-vault`
>
> There is a `compose.yaml` in the repo, and binaries for Linux, macOS and Windows can be built from source. The README covers installing, connecting stores and scanning discs; docs/technical.md has the details.
>
> **AI Involvement:** Built with heavy help from Claude Code: it wrote most of the code. I’m a software engineer with 20+ years of experience and set the architecture and the rules it works within: hexagonal architecture with DDD, the plugin model for stores and providers, the security model, testing standards (every external integration tested against a fake server reproducing the real API) and coding conventions. I write or approve the design specs, review the changes and use it daily on my own collection; everything goes through lint, tests and CI. The repo’s [`CLAUDE.md`](http://CLAUDE.md) and design docs are public, so you can see how it is built.
>
> Feedback welcome: which stores or systems are missing for you?

---

> **rubixstudios**（1 分） · 2026-10-16T19:03:01+08:00　
> https://preview.redd.it/6stqixpa9tvh1.png?width=1912&format=png&auto=webp&s=c2659735ba5d0faf7bef99e2e3c78adf72763015
>
> **Project Name:** Registry Console
> **Repo/Website Link:** [https://github.com/rubixvi/registry-console](https://github.com/rubixvi/registry-console)
>
> **Description:**
>
> Provides an interface for self hosted and remote registries.
>
> Also analysis of images, tags and repo stored in your own enviroment. Connects to Trivy scans to analyse CVEs and vulnerabilities affecting the image. Project is in active development and debugging, documentation will be improved upon.
>
> **Deployment:**
>
> Deploment can be performed using the docker-compose.yaml image, however feel free to reach out if you have issues. Example Dokploy deployment.
>
> **AI Involvement:**
>
> Yes, with human oversight, review, adjustments and cleanup.

---

> **CrispyBegs**（4 分） · 2026-10-16T19:34:47+08:00　
> it would be nice to have a docker / compose installation option for this

---

> **olivercer**（3 分） · 2026-10-16T19:44:28+08:00　
> At some point in the future the viewer will definitely get a docker distribution.
>
> I'm prioritizing the development of features, I have some cool ones coming!

---

> **CloudZH_app**（0 分） · 2026-10-16T19:58:54+08:00　
> https://i.redd.it/xxkipadsjtvh1.png
>
> **Project Name:** CloudZH
>
> **Repo/Website Link:** [https://cloudzh.app](https://cloudzh.app) (docs, live demo, changelog, roadmap). It's closed source, so there's no public repo.
>
> **Description:**
>
> CloudZH is a dashboard that installs, connects and looks after the apps on your own Linux home server. I built it because I was spending more evenings maintaining my media server than actually using it.
>
> * 90+ apps in the App Store (Plex, Jellyfin, Sonarr, Radarr, Prowlarr, SABnzbd, qBittorrent, Immich, Vaultwarden, Paperless-ngx and more), every install in a live console
> * Apps wire themselves after each install: Prowlarr → Sonarr/Radarr → download client → Plex, one shared data tree with hardlinks
> * System Health checks disks, updates, certificates, backups and network, and fixes the safe problems on its own (fixed, tested repairs, never free-form commands)
> * Accounts for friends and family with their own rights: they get the media library and requests, not Sonarr's settings
> * Passkeys, 2FA, WireGuard with QR codes, firewall with bans, one Caddy reverse proxy with a wildcard cert
> * Encrypted backups (second disk, NAS, S3 or cloud storage) and updates that roll back automatically
> * Everything also from the CLI (`zh`), UI in 6 languages
>
> Security model: the dashboard is a dependency-free Node app running unprivileged in a hardened container. Anything that needs root goes through a small systemd agent over a Unix socket with a fixed list of commands.
>
> Full disclosure: I'm the developer and it's a paid product, one license per server with unlimited users. Standard is $3/month or $30/year, Pro $5/month or $50/year. The apps it installs are the normal open-source apps with their data in plain folders, and if a license runs out, nothing is deleted: your apps keep running, only updates and new installs pause.
>
> **Deployment:** Released and available now. Ubuntu Server 24.04 (recommended), 22.04 or Debian 12/13, on x86\_64 or ARM64 (Raspberry Pi 5 works), also as a Proxmox VM; Windows via WSL2 is in beta. One install command, the rest happens in the browser. Every app runs in Docker Compose.
>
> Live demo with fake data, no signup: [https://cloudzh.app/demo](https://cloudzh.app/demo)
>
> **AI Involvement:** Yes, as a tool. I come from systems engineering and IT infrastructure, so the architecture, the security model and every product decision are mine. Claude did a good part of the implementation and code review under my direction, and every release gets tested on my own servers before it ships. CloudZH itself has an optional assistant that only runs with your own API key, with fixed tools only: no shell, no files, no secrets.
>
> Launch: free Pro months for the first testers while they last: [https://cloudzh.app/promotions/launch](https://cloudzh.app/promotions/launch)
>
> Videos: [https://cloudzh.app/docs/videos/](https://cloudzh.app/docs/videos/) · Discord: [https://cloudzh.app/discord](https://cloudzh.app/discord)
>
> Honest feedback very welcome, especially if anything on the website is unclear.

---

> **cosmic_m0nkey**（9 分） · 2026-10-16T20:17:08+08:00　
> **Project Name:** Yarrtube
>
> **Repo/Website Link:** [https://github.com/sergigp/yarrtube](https://github.com/sergigp/yarrtube)
>
> **Description:**
>
> I paid for YouTube Premium for years so my kids wouldn't see ads, but it never fixed the real problem: the algorithm deciding what they watch next. So I built Yarrtube. You track the YouTube channels and playlists you trust, and it downloads new videos as they're published. Nothing is recommended, and nothing plays next that you didn't choose.
>
> * Track public playlists and entire channels; new videos are downloaded automatically
> * Set video quality and a video limit per channel
> * Minimal web player for desktop and mobile
> * Works with Plex, Jellyfin and Kodi. In Plex, each channel and playlist shows up as a TV show
> * Built on top of yt-dlp, which ships inside the image
> * Written in Rust, with a single SQLite database. Lightweight enough to run next to the rest of your media stack
>
> **Deployment:**
>
> Requirements: Docker and a free YouTube Data API v3 key.
>
>     docker run -d \
>       --name yarrtube \
>       -e YOUTUBE_API_KEY=your-api-key-here \
>       -e YARRTUBE_DB_PATH=/config/yarrtube.db \
>       -e PUID=1000 \
>       -e PGID=1000 \
>       -p 8080:8080 \
>       -v /path/on/host/config:/config \
>       -v /path/on/host/videos:/videos \
>       ghcr.io/sergigp/yarrtube:latest
>
> There are Docker Compose examples and the full configuration in the repo: [https://github.com/sergigp/yarrtube/blob/main/doc/INSTALLATION.md](https://github.com/sergigp/yarrtube/blob/main/doc/INSTALLATION.md)
>
> **AI Involvement:**
>
> Most of the code is written with Claude Code, using spec-driven development with OpenSpec: every change starts as a proposal, design and task list that I review before any code is written. I'm an experienced backend engineer, and the project follows DDD, hexagonal architecture and an event-driven design. Those conventions, plus enforced TDD, live in a skill the agent has to follow.
>
> If you're interested in how it's built: [https://github.com/sergigp/yarrtube/blob/main/doc/ARCHITECTURE.md](https://github.com/sergigp/yarrtube/blob/main/doc/ARCHITECTURE.md)
>
> Feedback is very welcome, especially from Jellyfin and Kodi users, since I mostly use it with Plex
>
> https://preview.redd.it/wtjc23amntvh1.jpeg?width=600&format=pjpg&auto=webp&s=f0a27d51f54071d1e90c42fd9e89f00de7309268

---

> **TheOneCABAL**（4 分） · 2026-10-16T20:26:10+08:00　
> This is a neat project but I thought that another project has changed their UI suddenly
>
> https://github.com/Phalcode/gamevault-app

---

> **OG_Vezh**（1 分） · 2026-10-16T20:32:46+08:00　
> https://preview.redd.it/xicpn3puptvh1.png?width=2880&format=png&auto=webp&s=aeeba01f1b8343afa1887efd3f2a88b32d100de7
>
> **Project Name:** CloudZH
>
> **Repo/Website Link:** [https://cloudzh.app](https://cloudzh.app) (docs, live demo, changelog, roadmap). It's closed source, so there's no public repo.
>
> **Description:**
>
> CloudZH is a dashboard that installs, connects and looks after the apps on your own Linux home server. I built it because I was spending more evenings maintaining my media server than actually using it.
>
> * 90+ apps in the App Store (Plex, Jellyfin, Sonarr, Radarr, Prowlarr, SABnzbd, qBittorrent, Immich, Vaultwarden, Paperless-ngx and more), every install in a live console
> * Apps wire themselves after each install: Prowlarr → Sonarr/Radarr → download client → Plex, one shared data tree with hardlinks
> * System Health checks disks, updates, certificates, backups and network, and fixes the safe problems on its own (fixed, tested repairs, never free-form commands)
> * Accounts for friends and family with their own rights: they get the media library and requests, not Sonarr's settings
> * Passkeys, 2FA, WireGuard with QR codes, firewall with bans, one Caddy reverse proxy with a wildcard cert
> * Encrypted backups (second disk, NAS, S3 or cloud storage) and updates that roll back automatically
> * Everything also from the CLI (`zh`), UI in 6 languages
>
> Security model: the dashboard is a dependency-free Node app running unprivileged in a hardened container. Anything that needs root goes through a small systemd agent over a Unix socket with a fixed list of commands.
>
> Full disclosure: I'm the developer and it's a paid product, one license per server with unlimited users.
>
> The apps it installs are the normal open-source apps with their data in plain folders, and if a license runs out, nothing is deleted: your apps keep running, only updates and new installs pause.
>
> **Deployment:** Released and available now. Ubuntu Server 24.04 (recommended), 22.04 or Debian 12/13, on x86\_64 or ARM64 (Raspberry Pi 5 works), also as a Proxmox VM; Windows via WSL2 is in beta. One install command, the rest happens in the browser. Every app runs in Docker Compose.
>
> Live demo with data, no signup: [https://cloudzh.app/demo](https://cloudzh.app/demo)
>
> **AI Involvement:** Yes, as a tool. I come from systems engineering and IT infrastructure, so the architecture, the security model and every product decision are mine. Claude did a good part of the implementation and code review under my direction, and every release gets tested on my own servers before it ships. CloudZH itself has an optional assistant that only runs with your own API key, with fixed tools only: no shell, no files, no secrets.
>
> Videos: [https://cloudzh.app/docs/videos/](https://cloudzh.app/docs/videos/) · Discord: [https://cloudzh.app/discord](https://cloudzh.app/discord)
>
> Honest feedback very welcome, especially if anything on the website is unclear.

---

> **miku_claus**（3 分） · 2026-10-16T20:41:46+08:00　
> \*\*Project Name:\*\* Total Connect
>
> \*\*Repo/Website Link:\*\*
>
> \- GitHub: [https://github.com/M5Devs/Total-Connect](https://github.com/M5Devs/Total-Connect)
>
> \- Latest Release (v0.1.0): [https://github.com/M5Devs/Total-Connect/releases/tag/v0.1.0](https://github.com/M5Devs/Total-Connect/releases/tag/v0.1.0)
>
> \*\*Description:\*\*
>
> Total Connect is a modern, lightweight, open-source (GPLv3) file manager, transfer engine, and cloud client built in Go. It blends the dual-pane keyboard productivity of Total Commander with the universal storage capabilities of \`rclone\`.
>
> \*Why I built it & the problem it solves:\*
>
> FileZilla has an aging UI and paywalls essential cloud protocols (S3, Google Drive, OneDrive) behind a commercial Pro license. Meanwhile, managing remote files from headless servers or mobile browsers without GUI forwarding is still frustrating. Total Connect solves this with a unified single-binary tool supporting three interfaces:
>
> \- \*\*Interactive Dual-Pane TUI:\*\* Built with Charmbracelet (\`bubbletea\`, \`lipgloss\`) featuring classic F-key bindings (F5/F6/F8), multi-selection with \`Space\`, inline rename (\`F2\`), bookmarks, and live visual progress bars.
>
> \- \*\*Headless Web Daemon (\`tc-server\`):\*\* Zero-dependency embedded web server featuring a modern Fluent/Files UI and a touch-first mobile experience (tabs, swipe gestures, and ZArchiver-style contextual menus).
>
> \- \*\*Universal Storage via Rclone:\*\* Natively imports \`rclone\` Go libraries (no subprocess/CLI parsing overhead) supporting 50+ backends: FTP, SFTP, S3/MinIO, WebDAV, Nextcloud, Mega, Google Drive, Dropbox, etc.
>
> \- \*\*Atomic Operations:\*\* True server-side atomic moves without naive copy-then-delete data risks.
>
> \*\*Deployment:\*\*
>
> Total Connect compiles into standalone, zero-dependency static binaries for \*\*Linux, macOS, and Windows\*\* (\`amd64\` and \`arm64\`), available on the GitHub Releases page.
>
> \- \*\*TUI Mode:\*\* Simply download \`tc-tui\` and run \`./tc-tui\` inside any terminal or SSH session.
>
> \- \*\*Web Daemon Mode (Self-Hosting):\*\* Run \`./tc-server --port 8080 --host 0.0.0.0\` (optionally set \`--auth user:password\` for protection). You can run it on a Raspberry Pi, VPS, local machine, or even Google Colab, and expose it through a reverse proxy or Cloudflare Tunnel to manage cloud-to-cloud transfers directly from your phone.
>
> \*\*AI Involvement:\*\*
>
> I am the software architect behind the product vision, feature design, and system architecture. The implementation, refactoring, and test suites were built collaboratively using autonomous AI coding agents (\*\*Google Jules\*\* for repository-level coding/PR generation, with architectural reviews assisted by \*\*Claude\*\*). All code is fully tested with native Go unit tests, builds cleanly, and is 100% open-source under GPLv3.
>
> https://preview.redd.it/oxj2wiagrtvh1.png?width=1280&format=png&auto=webp&s=fd0dacc107339ef873440b6b7d05d3b5c6e45c01

---

> **AdvancedDrink8920**（6 分） · 2026-10-16T21:37:42+08:00　
> **Project Name:** Passticulous
>
> **Repo/Website Link:** [https://github.com/andrewsederholm/passticulous](https://github.com/andrewsederholm/passticulous)
>
> [https://passticulous.com](https://passticulous.com)
>
> **Description:**
> \- Passticulous is a selfhostable password generator. Whats unique about it is you can get very **fine-tuned** with the password format you want. Let me give you an example here:
> I like my passwords in a format of  and the first letter being capital. With passticulous, you can tell it exactly that. I want it in this format, with these symbols, etc.
> \- You can also have it repeat that. So it can be:
> \- You can also have it repeat the symbols. Theres alot of customizability and alterations.
> \- You can use it at [passticulous.com](http://passticulous.com) if you want. If you dont want to selfhost it. Completely free, no limits, nothing is saved on the server, everything is in the browser session on your end. I do not see what is generated and do not store any generated passwords.
>
> Deployment: Docker compose.
> \- Navigate to the folder you want to run it out of
> \- Run this command:
>
>     git clone https://github.com/andrewsederholm/passticulous.git
>     cd passticulous
>     docker compose up -d
>
> AI Involvement: YES.
> I have zero coding background or formal dev experience, my actual day job is in IT and hobby is automotive. This entire project was built using AI (specifically Claude in the terminal).
>
> This software was built using AI without manual security verification. It is provided "as is", without warranty of any kind. You host this project entirely at your own risk, and the author is not responsible for any security incidents, losses, or system compromises.

---

> **chazwhiz**（2 分） · 2026-10-16T21:40:34+08:00　
> I posted this a couple weeks ago but I think it was too late in the thread, plus I've continued to modify it.  Just curious if there's any interest in this?  It is absolutely vibe-coded slop I made for myself because I couldn't find a tool that did what I wanted, but I was considering throwing it on github in case anyone else wants it.
>
> Basically it's like a self-hosted Frinkiac for your own media.  It uses subtitles to search and can export gifs or mp4s with whatever text you want, placed and formatted as you want.
>
> https://preview.redd.it/sc1sqiwk1uvh1.png?width=2000&format=png&auto=webp&s=7bd5e8770a0847aa4e9c99c439c04a9a3f0e4cdb

---

> **TheZoltan**（2 分） · 2026-10-16T21:51:15+08:00　
> This looks pretty cool.

---

> **zorcererr**（2 分） · 2026-10-16T22:08:04+08:00　
> https://preview.redd.it/6tfj29wz3uvh1.jpeg?width=2560&format=pjpg&auto=webp&s=7000ea7403d4a1ad36931c5e1a3fae7f861a637c
>
> **Project Name:** Heddohon
>
> **Repo/Website Link:** [https://github.com/zorcerer/heddohon](https://github.com/zorcerer/heddohon) (screenshots and a tour at [https://heddohon.app](https://heddohon.app))
>
> **Description:** Heddohon is a web music player you host in front of the Navidrome, Subsonic or Jellyfin server you already run
>
> What sets it apart from other players?
>
> * **Your music server stays private.** The browser only talks to Heddohon, which fetches the audio and metadata itself. You only expose Heddohon and the music server needs no public address. Sign-in goes straight to your media server, so there are no extra accounts you have to manage. Admin users are automatically synced from the music server.
> * **Listen together, like a Spotify Jam.** Send a link and everyone who opens it can hear what you're playing,  in their own browser and without an account. Friends with an account on your server can add to the shared queue
> * **Share a song, album or playlist with anyone.** The link plays the original file until it expires or as soon as you withdraw it. (Please only share music you're allowed to share)
> * **Your listening stats stay on your server.** Top artists and albums, the hours you listen, what you played on this day in earlier years, and daily mixes made from your history are all taken care of by Heddohon, including heatmaps and more coming soon
> * **One player across devices.** The queue and settings follow your account, and one browser can control another. Desktop apps are available for Linux and Windows, and an experimental Android app as well
>
> *Also included:*
>
> * Original files up to FLAC 24/192 with no resampling, or transcoding to MP3/Opus/AAC per account. (DSD/DSF gets transcoded automatically)
> * Crossfade, ReplayGain, a sleep timer, and a 10-band EQ with AutoEq headphone corrections
> * Synced lyrics, instant mixes and internet radio
> * Casting to Chromecast and AirPlay
> * Scrobbling to [Last.fm](http://Last.fm) and ListenBrainz (Users can set this themselves and have it synced automatically to Navidrome, so they never have to share their credentials with the admin)
> * A keyboard command line (Ctrl+K: `play Spirited Away`) and multiple themes
> * A built-in MCP included, so any AI agent can create playlists and browse.
>
> **Deployment:**
>
>     curl -LO https://github.com/zorcerer/heddohon/releases/latest/download/docker-compose.yml
>     docker compose up -d
>     docker compose logs heddohon
>
> The log prints a setup code. Open `http://<server>:3000` and the setup page asks for your music server's address, generates the secret and saves everything. More elaborate documentation is available [here](https://github.com/zorcerer/heddohon/blob/main/SETUP.md)
>
> For unraid users, the app can be downloaded from the [CA](https://ca.unraid.net/apps/heddohon-0bp7lm80vkr69w).
>
> **AI Involvement:**
>
> Written with agentic assistance from Claude. The code and security posture have been reviewed by me and by multiple AI-assisted audits, documented in [SECURITY.md](https://github.com/zorcerer/heddohon/blob/main/SECURITY.md)
> I believe that transparency is important, especially in AI coded applications, so every finding is well documented there.

---

> **zorcererr**（1 分） · 2026-10-16T22:19:10+08:00　
> The plan is to create an application that can do it all, without the need for seperate applications or plugins. Issues are opened according to what's planned, if you think something is missing, please open an issue and I'll get to it!

---

> **Ill_Leader_7104**（2 分） · 2026-10-16T22:27:31+08:00　
> 570 tests for a personal project is wild tbh, respect for not just vibecoding it

---

> **Basicallysteve**（1 分） · 2026-10-16T22:49:18+08:00　
> Your app is buggy garbage and no one should put their personal data on your hosted website.

---

> **Alternative_One_4804**（2 分） · 2026-10-16T22:50:45+08:00　
> Thank you for your constructive feedback.
> By the way, there isn't a hosted website where to put data on.

---

> **kintope**（0 分） · 2026-10-16T22:56:31+08:00　
> **Agila: a finished, MIT-licensed self-hosted kanban with Docker install and no user caps (formerly Easy Kanban)**
>
> About a year ago I posted Easy Kanban here, a small kanban app I built because I couldn't find one I liked. I've since renamed it Agila, and it's finished rather than a beta.
>
> What you get:
>
> - A Docker Compose install in a few minutes, with a [video walkthrough](https://www.youtube.com/watch?v=MfRvOfrM7lk) and a [production deployment guide](https://github.com/drenlia-inc/agila/blob/main/DOCKER.md#part-1--production-deployment)
> - Kanban, List, Gantt and Calendar views of the same board, with real-time updates
> - Roles and per-board membership, with local accounts or Google/GitHub/Microsoft 365 SSO
> - WIP limits, sprints with burndown, and webhooks to Slack, Mattermost, Teams and Telegram
>
> Self-hosting is free with no limits: no user caps, no locked features.
>
> AI disclosure: I built the original with bolt.new and Cursor, and I still use AI tools heavily while developing it. I review, test and maintain it myself.
>
> - Site/demo: https://agila.dev
> - Repo: https://github.com/drenlia-inc/agila
> - Old thread: https://www.reddit.com/r/selfhosted/comments/1mq8ypz/
>
> Feedback welcome, especially from anyone using Planka, Wekan or Vikunja who's missing something.

---

> **Basicallysteve**（0 分） · 2026-10-16T22:56:34+08:00　
> Then you make want to edit the title of your comment.
> "I’m thinking of offering a hosted OpenTodo for free, with every feature and no subscription"
> That means you want to offer free accounts to people on a site you host.

---

> **Alternative_One_4804**（0 分） · 2026-10-16T22:58:18+08:00　
> This is the option I am considering, but there isn't yet a solution ready.

---

> **Basicallysteve**（1 分） · 2026-10-16T23:00:19+08:00　
> Ok, I'm encouraging people not to use that then.
>
> Also, for constructive feedback. If you click the checkboxes on the demo's lists, those don't work.

---

> **Alternative_One_4804**（1 分） · 2026-10-16T23:06:53+08:00　
> It's a very young project in its beta phase.
> And the checkbox are working.
>
> I'd be very grateful if you would like to open issues on github :)

---

> **Holiday_Agency_9324**（1 分） · 2026-10-16T23:19:18+08:00　
> **Project Name:** SculkHeart
>
> **Repo/Website Link:** [https://github.com/OrkenSab/SculkHeart](https://github.com/OrkenSab/SculkHeart)
>
> **Description:** I built a Minecraft server in Zig because I was tired of needing Java to host one
>
> \~3800 lines of Zig 0.13. Full login path: VarInt codec, NBT tree + parser + serializer + SNBT, RSA-2048 encrypt/decrypt by hand with std.math.big, AES-CFB8 socket layer, Mojang session verify over std.http, TOML config with validation.
>
> Thread per client, arena per connection reset after each packet. Compression via std.compress.zlib, with a decompression-bomb guard on data\_length before allocating.
>
> The annoying part wasn't crypto, it was matching vanilla packet IDs and chunk format for 774 until a real client stopped kicking me. E2E tests are a Python headless client doing handshake->login->config->play->keepalive, plus a mocked Mojang session server.
>
> https://preview.redd.it/0yzs76ckjuvh1.png?width=1918&format=png&auto=webp&s=070444f349e384e9ce41686a7b8fcb763e47d656

---

> **olivercer**（1 分） · 2026-10-16T23:20:04+08:00　
> Thanks, just increased it to 600+ lol
>
> LLMs are still fairly dumb. If you don't have a full test suite they drive you insane, attempting fixing something they break something else.

---

> **Accra101**（11 分） · 2026-10-17T00:32:43+08:00　
> https://preview.redd.it/6ir5kmm9uuvh1.png?width=2400&format=png&auto=webp&s=be7232abed6095e320eb07029c49914d65fcbaa5
>
> * **Project Name:** RasBeacon
> * **Repo/Website Link:** [https://github.com/aazam476/RasBeacon](https://github.com/aazam476/RasBeacon)
> * **Description:**
>
> I've been working on RasBeacon, a travel router OS for the Raspberry Pi. You flash it to an SD card, boot the Pi, and it sets up its own Wi-Fi hotspot. Your devices connect to the Pi, and the Pi connects to a Wi-Fi network of your choosing, or uses Ethernet as its uplink.
>
> Why I made it: my uni uses eduroam, and I didn't want to install the uni's setup software on all my devices to get on it, because let's be honest, I don't think anyone wants their uni tracking what they do. Cellular reception in my buildings is also bad because they're all made out of brick and concrete. I tried using travel router alternatives like PiFi, but they don't support WPA-Enterprise, which eduroam requires. So I decided to build my own. Once that worked, I kept going and added a plugin system so it could be a proper travel router, not just an eduroam bridge.
>
> What it does so far:
>
> * Private hotspot, plus an optional guest network that can't see your other devices. There's a QR code for the password so people can join quickly.
> * Connects to an uplink via Ethernet or Wi-Fi, including WPA-Enterprise networks such as eduroam. Each saved network gets its own random MAC address.
> * Detects hotel and airport login pages. You can sign in from a browser inside RasBeacon instead of on one of your devices.
> * WireGuard VPN with a kill switch. You can save multiple profiles, and IPv6 goes through the tunnel, too.
> * DNS over HTTPS. You can also set your own DNS servers while the VPN is on.
> * Name your devices and see how much data each one uses. You can set a limit for metered connections, like a phone hotspot.
> * Signed A/B updates, encrypted settings backups, and a built-in speed test using Cloudflare.
> * A web UI over (optional) HTTPS that works on a phone or a desktop.
>
> It also has plugins. They're Podman containers that you install from a signed custom .rba file or from a catalog. Each plugin is firewalled off your network; its internet traffic goes out only through the VPN, and you can see what it's requesting before you install it. There are three plugins right now: AdGuard Home, Samba, and fan/power button support for the Argon ONE V2 case. There's a template repo if you want to package something yourself, and you can use the plugin template repo to host your own catalog.
>
> Supported boards: Pi 5, Pi 4, Pi 3B/3B+, and Zero 2 W.
>
> It's an early version (v0.1.0). Builds and tests run in CI. I'm testing on a Pi 4, but I don't have access to the other boards right now because they're backordered. I might get a Pi Zero 2 W around January. Bug reports and feedback are welcome, and so are opinions on which plugins would be worth adding.
>
> * **Deployment:** Download and flash the latest release to your RPI's SD card and boot!
> * **AI Involvement:** I'm in my third year of undergrad in computer science, and I used AI extensively to build this. I'm upfront about that because I think AI-assisted development is where software is heading, and I wanted a project that would teach me to do it well, so I can work fast and still trust what I ship. To me, the difference between vibe coding and real coding comes down to understanding your work and being proud of it, whether or not AI helped write it. I firmly believe RasBeacon fits those two criteria.

---

> **Bearfin03**（3 分） · 2026-10-17T01:13:58+08:00　
> * **Project Name:** Bearfin
> * **Repo/Website Link:** [https://github.com/bearreacts03-pixel/bearfin-releases](https://github.com/bearreacts03-pixel/bearfin-releases) (downloads and release notes) and [https://support.bearreacts.com](https://support.bearreacts.com/) (docs, FAQ, privacy policy)
> * **Description:** A Jellyfin client for Android phones, iPhone/iPad and Apple TV, built because no existing client did what I wanted. It started as a Swiftfin fork and is now its own app written from scratch. Pre-rolls: point it at a library of intro clips and it plays a couple before every movie, like trailers at the theater, with no server plugin. Skip Intro and a credits countdown to the next episode, using Intro Skipper or chapter names, or times you mark yourself from the player. Its own video player that plays most files directly and hands the rest to Jellyfin to transcode; DTS and TrueHD come across as lossless FLAC so Apple devices can play them. Theme songs via Themerr, Live TV and recordings if you have a tuner, and a music tab for Navidrome or any Subsonic server, with CarPlay, so movies and music are in one app. It only talks to your server: no analytics, no accounts, no third-party services. Closed source. Not affiliated with the Jellyfin project.
> * **Deployment:** Nothing to self-host; it’s a client for the Jellyfin server you already run. Android APK: [https://github.com/bearreacts03-pixel/bearfin-releases/releases/latest](https://github.com/bearreacts03-pixel/bearfin-releases/releases/latest). iPhone/iPad via TestFlight: [https://testflight.apple.com/join/Sb4kd5Cj](https://testflight.apple.com/join/Sb4kd5Cj). Apple TV joins the same TestFlight link when Apple finishes reviewing it. Setup and FAQ at [https://support.bearreacts.com](https://support.bearreacts.com/). Enter your server address and Jellyfin login, or use Quick Connect.
> * **AI Involvement:** Yes. I designed it and tested every piece on my own server, devices and family for a couple of months, and I used Claude as a coding assistant throughout. The pre-roll logic, player behavior and licensing decisions are mine; a lot of the typing isn’t.

---

> **frkeyz**（5 分） · 2026-10-17T02:20:52+08:00　
> https://preview.redd.it/zrzv9x3sfvvh1.png?width=2000&format=png&auto=webp&s=786e99c5a2280355d3acb3fcf9a3060dca7e10c7
>
> **Project Name:** inkdoor
>
> **Repo/Website Link:** [https://github.com/frkey/inkdoor](https://github.com/frkey/inkdoor)
>
> **Description:**
>
> I work from home, and my family had no way of knowing when I was on a call. Someone would open the door mid-meeting to ask about dinner, the kids would come in to show me something, and I'd be muting myself while waving "not now".
>
> So now an old jailbroken Kindle hangs on my office door and shows whether I'm in a meeting, straight from my calendars. A small server on my LAN reads the calendars, draws the screen, and the Kindle downloads it.
>
> * Big "IN A MEETING" / "FREE" you can read from across the hall, plus until when and what's next
> * Today's agenda with the gaps between meetings, and tasks due today (TickTick)
> * "KNOCK FIRST" when it can't be sure. A calendar failing to load never turns into "Free"
> * The status flips a few seconds after a meeting starts, not on a fixed timer
> * Any ICS link: Outlook, Google, or a Nextcloud/Radicale server on your network
> * Web admin to add calendars, test links, pick your Kindle model and preview the door
> * Every Kindle the current jailbreaks support, from the 2012 Paperwhite to the Scribe
> * LAN only. Nothing leaves your network except fetching your calendars, and the links stay on the server
> * English and Brazilian Portuguese, MIT licensed
>
> **Deployment:**
>
> No Docker image yet. It runs as a systemd service:
>
> * Proxmox: one command creates an unprivileged LXC container and installs everything inside
> * Debian/Ubuntu: [`install.sh`](http://install.sh) sets it up as a sandboxed systemd service (running it again updates)
> * Anywhere with Python 3.10+: `pip install` from the repo and `inkdoor serve`
> * Kindle: the admin generates a zip with the scripts already pointing at your server. KPM works too, for updates without a cable
>
> Docs for the server, the Kindle setup, calendar links and troubleshooting are in the repo, in English and Portuguese. First release is v1.0.0.
>
> **AI Involvement:**
>
> Built with a lot of help from Claude Code. I decided what it does and how it should behave, and I tested it on my own Kindle and Proxmox box. Claude wrote most of the code, the tests and the docs. Every change went through the test suite (pytest and ShellCheck in CI) and a review pass before I merged it.
>
> Mine is a Paperwhite 10th gen, so if you try it on another model, I'd really like to know whether the image fills the screen.

---

> **sergedc**（1 分） · 2026-10-17T02:22:03+08:00　
> Excellent for kids!
>
> For adult: Then you never discover something new?
> What I really would like is: when I watch extreme right video the next one is automatically extreme left and vice versa. If I watch about alien on earth the next one automatically about debunking alien on earth. Etc.
> Basically the next video's sole objective is critical thinking.

---

> **Srules**（3 分） · 2026-10-17T02:31:38+08:00　
> https://preview.redd.it/hfimop3khvvh1.png?width=1600&format=png&auto=webp&s=5b934150a799fac6864a611aa7d1457150e57f96
>
> **Project Name:** Brushfall: a free, self-hosted family MMO
>
> **Price:** free. No ads, no in-game purchases, no subscription, and nothing locked behind a paywall.
>
> **Repo/Website Link:** [github.com/Twelve47Studios/brushfall\_release](https://github.com/Twelve47Studios/brushfall_release) (downloads, docs and wiki)
>
> **Try it first (free):** a public demo server is open at [brushfall.twelve47studios.com](https://brushfall.twelve47studios.com/?invite=5QV8PB38). The link includes an open invite, and the server may be wiped.
>
> **More screenshots:** [setup from one command (GIF)](https://raw.githubusercontent.com/Twelve47Studios/brushfall_release/main/assets/setup.gif) · [the admin panel](https://raw.githubusercontent.com/Twelve47Studios/brushfall_release/main/assets/screenshots/studio-desk.png)
>
> **Description:** I had the idea for this game after trying, unsuccessfully, to convince my wife to play WoW forever. So I created a game (with generous help from AI) that has the depth of an MMO that I want, but with a lot of features and assistance for players new to the genre. You can put on or take off the training wheels at any time.
>
> My wife is fairly anti-AI, so I wanted every asset in the game to be one that players can make their own. An integrated illustration studio lets anyone redo any texture, and it clearly shows the 2D-to-3D mapping. Each piece needs approval from a "Framer" before everyone in the world sees it.
>
> The game currently has a max level of 20, a dungeon at level 9 and a raid at level 18, with a world boss in the mix as well. For kids there are a few variations of what I call "Sprout" mode. They can have access to a selection of abilities, plus plenty of quality-of-life features to make the experience approachable, like auto-joining your party and auto-following when idle.
>
> * **Gameplay:** classes with tank, healer and damage roles, talents, quests, crafting and trading
> * **Play on any device:** it's tested and playable in the browser on phones, iPads and computers, with touch, keyboard and mouse, or a controller. Nothing to install from an app store: it's a PWA, so you can add it to your home screen and it opens like an app.
> * **Parent controls per child:** chat level (full, filtered, quick phrases only, or off), daily play time, quiet hours, and who can invite them to a party
>
> My hope is that a few people will try out the public demo server and spin up their own.
>
> **Deployment:**
>
> * **Docker:** a one-line setup script for macOS, Linux and Raspberry Pi (`setup.sh`) or Windows (`setup.ps1`). It makes the folder, picks a free port, starts the container and prints a one-time code for the admin panel. There are no files to edit. A plain `docker-compose.yml` and `.env` are available if you'd rather do it by hand.
> * **Without Docker:** self-contained downloads for Windows, Mac (Apple chip and Intel), Linux and Raspberry Pi 4/5, with nothing else to install
> * **Running it:** the whole world lives in one data folder with automatic backups. Sign-ups are approval or invite only, managed from a web admin panel.
> * **Playing outside your home:** Tailscale Funnel or Cloudflare Tunnel (setup has a `--share` flag), or a VPS with Caddy
> * **Docs:** [Quick Start, per-OS guides and a kid-safety guide](https://github.com/Twelve47Studios/brushfall_release/wiki)
>
> **License:** free for personal and family hosting. No ads, no purchases, and nothing is sent anywhere except a check for new versions. It's **closed source**: you get a ready-to-run server, not the code. Early access, so expect rough edges.
>
> **AI Involvement:** a lot.
>
> * **Code and writing:** most of the code, and much of the in-game writing (quests, dialogue, item text), was written with Claude Code. I designed, directed, reviewed and tested it, with automated and manual playthroughs (with a family of 4, 2 uncles, and 1 cousin) and a seeded test world.
> * **Art:** drawn by code (procedural SVG), with no image generators, and every piece can be repainted by players in the in-game studio.
> * **Voices:** the read-aloud voices are Piper neural text-to-speech.
>
> Hope this brings you and your family some joy.
>
> \-Nicholas

---

> **desirevolution75**（1 分） · 2026-10-17T02:44:09+08:00　
> https://preview.redd.it/gx4sqknsjvvh1.png?width=2880&format=png&auto=webp&s=48827dfbaf3113da1fc895f6ea24caa699527dd6
>
> * **Project Name: Wisp**
> * **Repo/Website Link:** [https://github.com/desirevolution/wisp](https://github.com/desirevolution/wisp)
> * **Description:** A lightweight, self-hosted WhatsApp companion with a responsive web UI, messaging, media sharing, push notifications, and MQTT integration.
> * **Deployment:** 21 mb Docker image. Use the included compose.yml.
> * **AI Involvement:** yes

---

> **byjacki**（2 分） · 2026-10-17T02:58:28+08:00　
> Project Name: WhereAreMyTokens
>
> Repo/Website Link: [https://github.com/Gerijacki/WhereAreMyTokens](https://github.com/Gerijacki/WhereAreMyTokens?utm_source=chatgpt.com)
>
> Description:
>
> A self-hosted dashboard for Claude Code usage. Claude Code (Anthropic's coding assistant) stores every session as JSONL files in `~/.claude/projects`. WhereAreMyTokens mounts that folder read-only, imports it into its own database (so the history survives Claude Code deleting old transcripts) and shows:
>
> * Usage and API-equivalent cost per project, session and prompt, and what kind of work it went to.
> * How well the prompt cache works, and why it gets rebuilt.
> * 5-hour usage blocks with burn rate, budgets with ntfy/Discord/Slack alerts, and how the usage compares with the price of the subscription.
> * Patterns that waste tokens, each with a ready-to-paste fix (a skill, a hook, a [CLAUDE.md](http://CLAUDE.md) section, a permissions list), and how much the fix saved once applied.
>
> It's useful mainly on a Pro or Max subscription, where there's no per-token bill to look at. Costs are API-equivalent estimates, not real charges.
>
> Deployment:
>
> Docker images for amd64 and arm64 on GHCR. A single container with SQLite:
>
>     docker run -d --name wamt -p 8787:8787 \
>       -v ~/.claude/projects:/data/claude:ro -v wamt-data:/data/wamt \
>       ghcr.io/gerijacki/wherearemytokens
>
> Or Postgres with the `docker-compose.yml` in the repo.
>
> A demo on synthetic data:
>
>     docker run --rm -p 8788:8787 ghcr.io/gerijacki/wherearemytokens demo
>
> The README covers configuration, password or reverse-proxy authentication (Authelia, oauth2-proxy…), a multi-machine agent, Prometheus `/metrics` and an OpenTelemetry receiver. Nothing is sent anywhere unless you configure the agent or alerts. MIT licensed.
>
> AI Involvement:
>
> Built with Claude Code as the main coding tool: a large part of the code was written with AI assistance, and I designed the features, reviewed the changes and tested them (unit tests, end-to-end tests in the browser, and CI on both SQLite and Postgres). The project analyzes Claude Code usage, so dogfooding it was part of the point.
>
> https://preview.redd.it/qflj0kkkmvvh1.png?width=1280&format=png&auto=webp&s=01713f9876cf66f64ec935600ade1ef6a2e9a9a0

---

> **theasset_**（0 分） · 2026-10-17T04:04:47+08:00　
> * **Project Name:** RetireNavigator Studio (featuring Navigator Essentials)
> * **Repo/Website Link:** [https://retirenavigatorstudio.com](https://retirenavigatorstudio.com) (Discussion & architecture notes: r/RetireNavigatorStudio)
> * **Description:** An **offline-first**, client-side retirement decumulation and tax-planning platform built around an **Always-Free core tier (Navigator Essentials)** for self-directed DIY planners. Most commercial financial tools lock your plans behind recurring subscriptions, mandate external bank logins via scrapers (Plaid/Yodlee), and store personal balance sheets on remote cloud servers. RetireNavigator runs 100% locally in-browser: personal assets, cash flows, and tax calculations are persisted in local IndexedDB and never leave your machine.
>    * *Always-Free Core (Navigator Essentials):* A permanent, fully functional personal planning engine with lifetime access to deterministic Monte Carlo projections, asset allocation, and baseline spending curves. No account registration, no credit cards, no trial expirations, no email collection, and zero tracking pixels.
>    * *Analytical Depth:* 17 advanced modeling modules (Roth Conversion Studio, 9x9 Social Security matrix, Gross-to-Taxable ledgers with statutory 2026 brackets and 2-year IRMAA lookbacks, true brokerage cost-basis tracking, dynamic net-portfolio guardrails, and Web Worker-driven Monte Carlo simulations).
> * **Deployment:** Currently runs as an offline-first Progressive Web App / client-side SPA (built with Vite, React, Tailwind, and Dexie/IndexedDB). All compute (solvers, backtests, Monte Carlo) executes strictly client-side. Once static assets are cached, it operates completely air-gapped without making outbound external API calls. Service worker update polling can be explicitly toggled off in settings for strict air-gapping.
> * **AI Involvement:** Zero AI or LLMs are involved in the calculation or financial projection engines. All tax waterfalls, withdrawal sequencing, Monte Carlo passes, and solver bisections are 100% deterministic code to prevent hallucinations on compound 30-year projections.
>
> (A standalone static Docker container for local homelab hosting is on the immediate roadmap.)
>
> https://preview.redd.it/idk6edv7yvvh1.png?width=1993&format=png&auto=webp&s=f192147adbe9814ef50629f90fb82254d593dcc8

---

> **mattisism**（4 分） · 2026-10-17T04:06:44+08:00　
> https://preview.redd.it/jaow9ym1tvvh1.png?width=1600&format=png&auto=webp&s=28e61abbaa2448bb89b7c027acebbaf0b176fba0
>
> **Project Name:** Maki
>
> **Repo/Website Link:** [https://github.com/OrbitMPGH/Maki](https://github.com/OrbitMPGH/Maki)
>
> **Description:** I wanted an all-in-one solution similar to the \*arr stack but for Manga management. I couldn't find any that quite hit all my needs. Therefore, Claude and I built "Maki", a self-hosted manga manager and reader.
>
> You add a series once, and Maki keeps it complete. It watches manga sites on a schedule, picks the best source for each series, downloads new chapters, and writes plain CBZ files with ComicInfo.xml. If you use Kavita, it fits next to it, because the same folder works in Kavita, KOReader, Panels, Chunky, and Mihon (over OPDS). You can also read in Maki’s own reader.
>
> * **Start where the anime ended.** Connect AniList or MyAnimeList, and Maki reads your anime list. For a series with an adaptation, it works out the manga chapter where your finished seasons stop, marks everything before it as watched, and points you at the next chapter. Watched chapters are kept separate from read ones, so they don’t inflate your stats.
> * **Recommendations from your own library.** Embeddings run locally on your server over the MangaBaka catalog. You get “Readers like you” and a “Your Taste” view of your reading behavior, grouped interests, and how your taste has moved over time. Hide titles, dismiss them, or mark them already read to keep improving the results. If you connect AniList or MAL, your anime list also works as a weak taste signal.
> * **Stats.** Per-series read counts, activity over time, reading time, levels, streaks, and achievements, plus a yearly Rewind.
> * **35 built-in sources in over a dozen languages.** Optional Suwayomi support adds its extensions, and torrents work through Prowlarr or Jackett. You can also easily import manga you already have.
> * **Automatic monitoring and a download queue**, with FlareSolverr support for Cloudflare-protected sites.
> * **Scrobbling** to AniList, MyAnimeList, Kitsu and MangaBaka, whether you read in Maki, over OPDS or in Kavita.
> * **And a lot more.** Multiple users with per-folder access, 2FA, OIDC single sign-on, notifications (Discord, Telegram, ntfy), one-click backups, and a REST API.
>
> **Deployment:** Docker (amd64 and arm64) `ghcr.io/orbitmpgh/maki:latest` and Unraid (search “Maki” in the Apps tab)
>
> **AI Involvement:** Maki is almost entirely AI-slop-built, developed with Anthropic's latest Claude models. I know plenty of people who, for very valid reasons, tend to avoid AI-made apps, and I've therefore been very transparent about the use of AI in Maki's development. If you despise AI applications, then Maki is not for you. Otherwise, I would love it if you gave it a try. I am very open to feedback. Open an issue or create a discussion post on GitHub.

---

> **Toastienergy**（2 分） · 2026-10-17T04:41:24+08:00　
> Try TypeType, also had recommendations just added

---

> **szcz0t3czka**（4 分） · 2026-10-17T04:52:28+08:00　
> **Project Name:** AdGuard Atlas
>
> **Repo/Website Link:** [https://github.com/marska/adguard-atlas](https://github.com/marska/adguard-atlas) (live demo with synthetic traffic: [https://atlas-demo.tty0.app](https://atlas-demo.tty0.app))
>
> **Description:**
>
> A live world map of your network's DNS queries, fed from AdGuard Home's query log. Every query becomes an arc from home to the country/city its answer resolves to; blocked, local and unanswered queries pulse at home. Around the map: a live feed, counters for the last 15 minutes (queries, blocked share, top countries, domains, devices) and filters by device, class, instance or text. Click a country or a marker to see which devices and domains go there.
>
> Useful if you've ever wondered where your smart TV, phone or "dumb" plug actually phones home, and it looks nice on a wall display.
>
> \- Read-only towards AdGuard Home: it only ever calls \`GET /control/querylog\`.
>
> \- Fully local page: world map and fonts are bundled, no tile servers, CDNs or analytics, strict CSP. AdGuard credentials never reach the browser.
>
> \- GeoIP (DB-IP City Lite) is baked into the image at build time; MaxMind GeoLite2 can be mounted instead.
>
> \- Supports multiple AdGuard Home instances on one map.
>
> **Deployment:**
>
> Single Docker image (\`ghcr.io/marska/adguard-atlas\`), runs non-root with a read-only root filesystem and no capabilities. A reference \`docker-compose.yml\` and a full configuration table are in the README. Try it without AdGuard Home in demo mode:
>
> \> docker run --rm -p 8080:8080 -e DEMO=true [ghcr.io/marska/adguard-atlas:latest](http://ghcr.io/marska/adguard-atlas:latest)
>
> **AI Involvement:** Built with Claude Code as the main coding tool: a large part of the code was written with AI assistance. I designed the features, reviewed every change and tested it: unit tests (vitest, including a fake AdGuard Home), hands-on testing in the browser, and CI that builds the hardened container, smoke-tests and scans it before publishing.
>
> https://preview.redd.it/ety7body6wvh1.png?width=2552&format=png&auto=webp&s=8ed7e21f9c8cdf7899f8bfac6c023fc915dcaf01

---

> **cosmic_m0nkey**（1 分） · 2026-10-17T04:55:55+08:00　
> Thanks mate! By now i usually navigate the youtube recomendarions and I add stuff to playlists that are synced. I also already follow a bunch of channels. For me is working fine for now.

---

> **kishkisan**（1 分） · 2026-10-17T05:14:59+08:00　
> I built this project with inspiration from UltraRAG for searching collections of books and papers, to help me with research, writing and reading through a medium-sized corpus.
>
> The intention is to utilise it as a RA (retrieval with no answer generation), but kept the name as rag anyway. I intend to add an optional answer generation in the future, but I want to avoid AI generation and running into problems of plagiarism, but want to be able to utilise AI nonetheless.
>
> Right now, research-rag returns passages with source locations so you can read them in context and check the original. The search is both lexical and semantic, and runs completely locally on CPU.
>
> The implementation supports PDF, EPUB and MOBI, and works through a browser, CLI or MCP agent. No account or hosted model service needed.
>
> It currently supports Linux. Screenshots, installation and details are in the README:
>
> [https://github.com/AhmedKishki/research-rag](https://github.com/AhmedKishki/research-rag)
>
> Would appreciate feedback from anyone working with their own research library.

---

> **akspad**（1 分） · 2026-10-17T05:18:12+08:00　
> Good point! We don't publish broken downloads (phew) and only publish after every part of a long article is ready. What we don't do is keep the parts that succeeded and finished - we instead retry from scratch. Will push this improvement, thank you!!

---

> **chrysogonus_dev**（1 分） · 2026-10-17T05:37:05+08:00　
> **Project Name: Prompt Maker Studio**
>
> Hey everyone! 👋
>
> I'm the solo developer behind **Prompt Maker Studio**, a free, open-source, self-hostable application for managing, reusing, and improving AI prompts.
>
> I originally built it because I kept losing track of useful prompts, experimenting with different versions, and struggling to figure out whether my changes actually improved the results.
>
> **What it does:**
>
> * Organize prompts with folders, search, and favorites
> * Create reusable templates with variables
> * Track versions and restore previous prompts
> * Refine prompts with AI-assisted suggestions
> * Evaluate prompts using reusable test cases and compare results
> * Access your prompt library through an MCP server, including integration with ChatGPT
> * Bring your own LLM provider, including local models through Ollama and vLLM
>
> **Self-hosting:**
>
> The application runs with Docker Compose and uses SQLite.
>
>     git clone https://github.com/chrysogonus/prompt-maker-studio.git
>     cd prompt-maker-studio
>     make setup
>     make up
>
> The core prompt management features work without an AI provider. AI-powered features require a configured provider.
>
> **Tech stack:** Next.js, FastAPI, SQLite, Docker
>
> **License:** Apache 2.0
>
> **GitHub:** [https://github.com/chrysogonus/prompt-maker-studio](https://github.com/chrysogonus/prompt-maker-studio)
>
> **Live demo:** [https://neadlab.com](https://neadlab.com/)
>
> **AI involvement:** \[Add a brief, accurate description of how you used AI coding tools during development.\]
>
> **Looking for feedback!**
>
> This is still an early-stage project, and I'm currently trying to find my first real users.
>
> I'd genuinely appreciate it if some of you could try self-hosting it and share your experience.
>
> I'm particularly interested in:
>
> * Was the installation straightforward?
> * Are there features you'd expect from a self-hosted prompt manager that are missing?
> * Would you actually use something like this instead of plain Markdown files or Obsidian?
>
> I'm actively maintaining the project and happy to improve it based on real feedback. I can't promise to implement everything, but I'll take suggestions seriously.
>
> Thanks for checking it out! :)

---

> **r20**（2 分） · 2026-10-17T06:26:03+08:00　
> Looking good.  Really like the feed discovery feature.

---

> **kryoseu**（1 分） · 2026-10-17T07:15:22+08:00　
> Thanks for giving it a go!

---

> **Solid_Violinist_1163**（1 分） · 2026-10-17T08:06:41+08:00　
> **Project Name:** Conector
>
> **Repo/Website Link:** https://github.com/Secra-Solutions/Conector (MIT)
>
> **Description:**
>
> Conector is a self-hosted MCP gateway for AI agents. You run it on your own box, connect your apps once in a web panel (OAuth sign-in or an API key), and every agent you use (Claude Code, Codex, Cursor, Gemini CLI, Copilot, goose, OpenCode and others) reaches those apps through one MCP endpoint, with its own token.
>
> The point for self-hosters: the credentials stay on your server, not in a vendor's cloud and not copied into the config of every agent on every machine.
>
> - Credentials are encrypted with AES-256-GCM. The key is a file in your data volume, so back up the volume.
> - Each agent gets its own token (stored as a SHA-256 hash), limited to the apps you choose, and revocable.
> - Every tool call and every panel change goes to an audit log. Payloads and credentials are never logged.
> - It binds to 127.0.0.1 by default, accepts only known Host headers (against DNS rebinding), and the panel loads no external scripts, fonts or images. No telemetry.
> - Users and roles (admin/member), invitation links, personal and shared connections. It never sends email: links are printed or shown in the panel.
>
> The catalog has about 1,180 apps, but to be clear about what that means: every app gets a generic authenticated `<app>_request` tool for its API, and only 165 apps have hand-written tools on top. Most entries are "an API your agent can call with a stored credential", not a polished integration.
>
> Self-hosted apps are the weak spot right now. Gitea, GitLab, n8n, Grafana, Mattermost, ntfy and Outline are in, and Linkding just arrived as our first community contribution. Home Assistant, Immich, Paperless-ngx, Jellyfin, Nextcloud, Proxmox VE, Forgejo, Sonarr/Radarr, Mealie, Miniflux, Karakeep, BookStack and Audiobookshelf are not yet. Each one has a "good first issue" with a link to its API docs. An app is a small data object (base URL, auth, a test call, help text), so adding one is a good first PR.
>
> **Deployment:**
>
>     docker run -d --name conector -p 127.0.0.1:8790:8790 \
>       -v conector-data:/data ghcr.io/secra-solutions/conector
>     docker logs conector   # prints a one-time link to create the admin account
>
> Or `npx conector start` with Node.js 22+ (data goes to `~/.conector`). Images for amd64 and arm64 (`latest`, `X.Y.Z`, `edge`), and a docker-compose.yml in the repo. For remote access, put an HTTPS reverse proxy or tunnel in front (Caddy, nginx, Cloudflare Tunnel…) and set `CONECTOR_PUBLIC_URL` and `CONECTOR_TRUST_PROXY=1`. The README covers configuration, the security model and how to add an app.
>
> Known limits in this v0.1:
>
> - URLs of self-hosted instances must be `https://`, except localhost. A plain-HTTP LAN address like `http://192.168.1.20:8123` is rejected. Should we allow plain HTTP for private addresses as an opt-in?
> - Tokens are scoped per app, not per operation (no read-only tokens yet).
> - Storage is one JSON file. Fine for a person or a small team. No HA.
> - "One-click" OAuth needs an admin to register an OAuth app with each provider once.
>
> **AI Involvement:** A lot, so to be upfront: most of the code and the app definitions were written by AI (Claude Code) under our direction, and we used it to help draft this comment too. Every app definition goes through a validator that calls the real API with fake credentials and expects a 401/403, and there are unit and end-to-end tests. We're the Secra Solutions team, a cybersecurity company in Spain, and this is our first open-source project.
>
> Feedback welcome, especially: which self-hosted apps you'd connect first, and anything in the security model you'd change.

---

> **simonchai**（1 分） · 2026-10-17T08:16:01+08:00　
> Project: Tasks–To Do Sync
> Repo: https://github.com/simonchai-tw/tasks-todo-sync
> Website: https://simonchai-tw.github.io/tasks-todo-sync/
> Description: Two-way sync between Google Tasks and Microsoft To Do — titles, notes, due dates + times/reminders, completion, lists, subtasks, moves and deletions, both directions. Runs in your own Google Apps Script project; no third-party server ever sees your tasks. v1.0.0 stable, 549 automated tests passing.
> Deployment: self-hosted in your own Google Apps Script project; Windows users get a one-click exe installer. Documented on the project website.
> AI disclosure: built with AI-assisted coding.

---

> **albert_wl**（5 分） · 2026-10-17T08:19:56+08:00　
> Project Name: Forkshelf
>
> Repo/Website Link: https://forkshelf.com
>
> Description: It's a directory of open source projects you can self-host instead of paying for team tools. There are 45 pages, one per paid tool (Notion, Jira, Slack, Google Analytics and so on). Each page lists projects by GitHub stars, with the licence and last commit date pulled from the public GitHub API, and the fetch date shown on the page. A project only counts as open source on the site if it has an OSI-approved licence, a commit in the last 12 months and a repo that isn't archived. Source-available stuff like Outline is still listed, with a label, but doesn't count. No account, no newsletter.
>
> Deployment: Nothing to install, it's just a website. Every project links to its own repo and install docs so you can check it at the source.
>
> Money: eight of the comparison pages (Firebase vs PocketBase is one) have a Railway referral link marked "Paid link". I'm planning sponsor slots on the list pages. They'll be labelled Sponsored and won't change the lists. None are live yet. Maintainers can pay for a priority review (US$49, or US$29 for the first 10 paid reviews, offer ends 31 Jan 2027). That only changes how soon a tool gets reviewed. Free reviews take about 2 to 4 weeks.
>
> AI Involvement: The page text was drafted with AI tools, then edited and fact-checked. Star counts, licences and dates come from the GitHub API.
>
> If you spot a wrong licence or a project that shouldn't count, tell me and I'll fix it.

---

> **MasterHung2**（0 分） · 2026-10-17T10:04:09+08:00　
> \*\*Agentown – a self-hosted company of AI agents with real permissions and a 3D office\*\*
>
> GitHub: https://github.com/wanatabe-yuu/agentown (MIT) · Docs: https://agentown.site/docs/
> 40-second demo is at the top of the README.
>
> Most multi-agent setups give every agent the same powers and hope the prompt keeps them in line. In Agentown, each agent is a lasting employee: it has a job, a manager, a desk, a workspace that survives restarts, and permissions the server enforces. A title like "CEO" grants nothing by itself.
>
> \*\*What it does\*\*
> \- The CEO hires from job templates it was allowed. Leads hand out work, and workers send it up for review.
> \- When an agent needs something its permissions don't cover, it asks its lead or you. You approve once, or grant it for good. Everything allowed \*and\* denied goes into an audit log.
> \- Agents get real computers: a pod with Chromium, a terminal and ffmpeg. You can watch the screen live and take over.
> \- Bring your own keys: Anthropic, OpenAI, Gemini, OpenRouter or any OpenAI-compatible endpoint (so local models work too). Keys stay on the server, and agents call models through a broker that never hands them the key.
> \- The whole org is one YAML "world": departments, jobs, the first agents and a 3D office you can walk through and edit. There are starter worlds (café, factory, hospital, lab, video studio), and you can share your own from a GitHub repo.
>
> \*\*Self-hosting details\*\*
> \- Ubuntu 24.04 x86\_64, one command: \`curl -fsSL https://agentown.site/install.sh | sudo bash\`. You can also download the installer from the release page and read it first.
> \- Releases are signed with Sigstore. The installer verifies the signature and checksums before it installs anything.
> \- It runs on k3s + PostgreSQL. Each team is one pod with Pod Security "restricted", NetworkPolicies, quotas, and an admission policy that refuses any pod not shaped like an Agentown runtime. The server uses a limited ServiceAccount, not cluster-admin.
> \- A Go CLI (\`agentownctl\`) can set up several VMs over SSH from your laptop.
> \- Backups: \`agentownctl backup\`. Re-running the installer upgrades in place.
> \- The UI comes in 12 languages.
>
> \*\*Honest limits\*\*
> \- Pre-1.0 (v0.5.1). Running many agents costs real API tokens.
> \- The Docker driver is for development only. Use k3s for real use.
> \- Agents on k3s may only reach public HTTPS (port 443) by default.
>
> \*\*AI disclosure:\*\* I built it with heavy help from Claude Code. The design, permission model and testing are mine, and the server has \~330 automated tests.
>
> Feedback very welcome, especially on the permission model, and on what you'd want agents to be able to ask you for.

---

> **Builvio**（2 分） · 2026-10-17T15:05:19+08:00　
> I made this for finding local deals to flip. It searches Craigslist, Kijiji, eBay, OfferUp and Facebook Marketplace every few minutes and pings your phone the moment something good shows up, so you can be the first to message the seller. [https://github.com/Crepe950/flipwatch](https://github.com/Crepe950/flipwatch) Let me know what you think.

---

> **sogidirned**（1 分） · 2026-10-17T15:29:01+08:00　
> That for Pi-hole would be very nice.

---

> **Itchy_Ad_2562**（1 分） · 2026-10-17T19:46:59+08:00　
> **K8s AI Agent Orchestrator**
>
> https://preview.redd.it/1fvpu9mxk0wh1.png?width=3516&format=png&auto=webp&s=17b0497b5857a45e3b1020c0e5dd96cdc0b9bfa4
>
> **Project Name:** ainsel
>
> **Repo/Website Link:** [https://github.com/ainsel-project/ainsel](https://github.com/ainsel-project/ainsel)
>
> Hello everyone,
>
> I built **ainsel** — an orchestrator that runs my AI agents as workloads in my home K8s cluster instead of loose processes on my machine. Agents get sandboxed, credentials stay in the cluster, and I can swap models, providers or skills per agent on a whim.
>
> **How it works:** you set up an agent with a persona, skills and tools, then bind it to events via webhooks. An agent with GitHub tools + a reviewer persona reviews your PRs. Swap the tools and persona a bit, register it to different events and the same setup becomes a developer that e.g. picks up labeled issues and opens PRs. Any platform with webhooks and a MCP is a no-brainer to integrate — for things that have neither, like my Matrix chat server, you can add a small bridge.
>
> To make ainsel even easier to integrate it comes with its own MCP. Like this I control it from my machine. Otherwise all these steps to manage the agents in the UI would become pretty cumbersome.
>
> Right now I'm using it integrate AI in all my small projects here at home. It runs in my cluster and uses LLMs from my Nvidia Spark. You can see the agents working in the GitHub ainsel repository as well, though they won't respond to anyone except myself due to the set event filter criteria, so you don't need to try ;-)
>
> I think it's super cool, maybe you like it too :-)

---

> **Rich_Ambassador1945**（1 分） · 2026-10-17T20:32:27+08:00　
> **Project Name:** MeshCenter 1.11.0 - Self-hosted Meshtastic Web Interface
>
> **Description:**
>
> Hi everyone!
>
> I've been developing MeshCenter, an open-source web application for managing and monitoring Meshtastic networks.
>
> The latest version adds Docker support, allowing the application to run on a NAS or Linux server instead of requiring a dedicated Raspberry Pi.
>
> I've tested it on my Synology DS920+ using a Meshtastic radio connected remotely over TCP.
>
> Features include:
>
> * Messaging and node monitoring
> * Network maps and telemetry
> * Browser-based management
> * Automatic reconnection after TCP interruptions
>
> **Deployment:**
>
> Docker Compose on x86-64 Linux or compatible NAS devices. Currently, one active TCP-connected radio is supported per instance.
>
> **AI Involvement:** AI-assisted development, including coding and testing.
>
> I'm sharing this to get technical feedback, especially from people running Meshtastic on NAS devices or home servers.
>
> Would remote TCP radio connectivity be useful in your setup? What features or improvements would you prioritize?

---

> **SlimDogs**（1 分） · 2026-10-17T21:04:34+08:00　
> https://preview.redd.it/4cbinx9j01wh1.png?width=2800&format=png&auto=webp&s=c5760b3b400bf2038707b3e52a402dfe41529682
>
> * **Project Name:** Thingport v1.0.0 🎉
> * **Repo/Website Link:**
>    * Website: [https://thingport.net](https://thingport.net/)
>    * GitHub: [https://github.com/TautvydasDerzinskas/Thingport](https://github.com/TautvydasDerzinskas/Thingport)
> * **Description:** Thingport is a self-hosted 3D model library that helps you keep your 3D printing collection organized, accessible, and under your control. If you're into 3D printing, you probably collect bookmarks across platforms like MakerWorld, Printables, and Thingiverse. But models can disappear when authors remove them, newer versions aren't always better than the originals, and accessing your collection isn't always possible when you're offline. **Thingport aims to solve these problems by bringing your 3D model collection into one place that you control.** Key features include:
>    * **Provider synchronization:** Import and sync collections between Thingport and supported providers. Automatically import new models as you bookmark them on external platforms.
>    * **Browser extension:** Officially published for Chrome, Firefox, and Microsoft Edge, making it easier to bring models into your library.
>    * **AI-powered categorization:** Organize existing uncategorized models, including models imported from an older collection.
>    * **AI-assisted descriptions:** Improve model descriptions to make your library easier to browse and navigate.
>    * **OIDC authentication:** Support integration with identity providers for convenient sign-in.
>    * **Self-hosted and private:** Keep your library on your own infrastructure, with access to your collection even when you're offline, subject to what you've already downloaded.
> * One of my main priorities throughout development has been UI/UX. I want Thingport to feel polished and intuitive, rather than just being another functional database of 3D models. I believe its user experience and provider synchronization are two of its strongest points.
> * **Deployment:** Thingport is released as **v1.0.0** and is intended to be self-hosted. The project provides Docker-based deployment, making it suitable for running on your own server or home lab. Check the [GitHub repository](https://github.com/TautvydasDerzinskas/Thingport) for installation instructions, Docker configuration, and setup documentation. You can also visit the [project website](https://thingport.net/) to learn more.
> * **AI Involvement:** Claude has been used extensively during development, including assistance with implementation and coding. I'm transparent about using AI, but I don't see AI-assisted development as a reason to dismiss a project. I've invested significant time in reviewing and refining the code, working on the architecture, and improving the implementation. Code quality and maintainability matter to me just as much as the user experience. AI is a tool, not a substitute for engineering judgment. The goal has always been to build something genuinely useful, well-designed, and worth maintaining.

---

> **wsLyNL**（1 分） · 2026-10-17T21:27:36+08:00　
> This really looks cool

---

> **cassiozen**（1 分） · 2026-10-17T22:02:45+08:00　
> https://preview.redd.it/rzkaxz1i91wh1.png?width=1536&format=png&auto=webp&s=9970aeb07389440f0f3eea57802b45033ac59786
>
> **notesd**
>
> **Repo**: [https://github.com/cassiozen/notesd](https://github.com/cassiozen/notesd)
>
> **Description:** Self hosted notes with native, offline-first apps.
> I couldn't find a "simple" hosted notes app, so I made one. (By simple I mean: Not a second-brain, multi-object record system; It's not Notion/Obsidian.)
>
> Features organization via tags; full-text search; encrypted/locked notes.
>
> **Deployment:**
>
> * Server is a single binary (run it as a systemd service and you're good to go) Check the [Hosting docs](https://github.com/cassiozen/notesd/blob/main/docs/hosting.md).
> * Mobile Apps are not on App Stores yet - Android can be installed by downloading from the [releases](https://github.com/cassiozen/notesd/releases/latest) page, but iPhone app needs a Mac with XCode.
>
> **AI Involvement:** Used Claude Code - but everything was manually tested and approved.

---

> **afk-sapien**（4 分） · 2026-10-18T00:25:20+08:00　
> Project Name: PokeSim (0.5.0)
>
> https://preview.redd.it/sfvlasooy1wh1.png?width=792&format=png&auto=webp&s=744ed0a34bcb02d376a75a339735f7ec9b1c4577
>
> Repo/Website Link: [https://github.com/afk-sapien/PokeSim](https://github.com/afk-sapien/PokeSim)
>
> Description: PokeSim plays Pokémon by itself while you watch in your browser, or you can take control and play manually. It started with Red and Blue and now plays Yellow, Gold, Silver, and Crystal too. Leave it running and come back to new catches, evolutions, badges, League wins, and lots of ridiculous nicknames!  Watch at normal speed or up to 50x (now faster thanks to a new Rust-based emulator). Run several games at once, and they'll trade with each other in the in-game Cable Club, even across generations through the Time Capsule. It has a live view, a journal with screenshots, a Pokédex, a PC browser, and optional notifications through ntfy, Discord, or Telegram. You bring your own ROM(s).
>
> Long-term games (I have some 10,000+ hour games running) are enabled through a step-based reset of one-off items and Pokémon (optional). Left alone, the player controller will try to beat the game, complete the Pokédex, then obtain a high-DV, shiny living Pokédex.
>
> Deployment: A Docker image on GHCR and a compose file in the release. Also a Python install.
>
> AI Involvement: Code was hallucinated with Claude Code / Codex. The player inside the app uses no AI. It's plain rule-based logic (basically a complex state machine) and runs offline. Tested with over 100,000 hours of playtime.
>
> Also working on a spin-off project to see how well AI models can play Pokémon Red and Blue: [https://afk-sapien.github.io/pokebench/](https://afk-sapien.github.io/pokebench/)

---

> **bulutarkan**（1 分） · 2026-10-18T01:03:44+08:00　
> **Project:** Mac MCP
>
> **Repo:** https://github.com/bulutarkan/mac-mcp (MIT)
>
> I built this because I wanted to keep using ChatGPT/Claude for the thinking part without handing my Mac over to a remote desktop service. Mac MCP runs on your own machine. It gives MCP clients access to local files, terminal commands, native macOS apps, and Safari/Chrome tabs. Browser work can happen in the background instead of yanking focus away from what I'm doing.
>
> Recent additions include scheduled agent/script tasks with run reports, a local folder knowledge index with source/page references and on-device OCR for scanned PDFs, and permission profiles with approvals for risky actions. There's a native menu bar app so you can see what the agent is actually doing.
>
> **Deployment:** It's a macOS app plus a local Python MCP server, not a Docker container or a cloud-hosted agent. There's a downloadable package for Apple Silicon on macOS 14+, or an installer for macOS 13+. Setup and limitations are in the repo. The server and local index run on your Mac; if you connect a cloud AI client, content sent to that client still goes to its provider. It isn't a sandbox.
>
> **AI involvement:** I use coding agents while building and testing the project. I'm the maintainer, and the project itself is the tool layer, not a model.
>
> I'm curious how self-hosters feel about this split: local execution and local permissions, but the option to use a hosted model for reasoning. Is the provider boundary a dealbreaker, or does keeping execution on your own machine still have value?

---

> **AlyxVeldin**（1 分） · 2026-10-18T02:28:40+08:00　
> **Project Name:** VlmSpellchecker
>
> **Repo/Website Link:**
> GitHub: https://github.com/Veldin/vlm-spellchecker
> Demo: https://veldin.com/vlm-spellchecker/
>
> **Description:**
>
> I've been working on a spellchecker plugin for TinyMCE called [VlmSpellchecker](https://github.com/Veldin/vlm-spellchecker).
>
> The idea came from a separate project of mine, [Wiki Language Models](https://github.com/Veldin/wiki-language-models), which generates statistical language models from Wikipedia dumps.
>
> I created that project because I wanted a basic, old-fashioned spelling correction and word prediction tool that doesn't use AI to try to interpret what you're writing and return some AI-generated response instead of simply pointing out your typos.
>
> VlmSpellchecker is a small client project built around those models that aims to do just that.
>
> It's a JavaScript plugin for TinyMCE that uses a locally hosted binary dictionary to identify unknown and uncommon words, suggest corrections, and replace words directly in the editor.
>
> What it currently does:
>
> - Marks unknown words with a red dotted underline.
> - Marks uncommon words with an orange dotted underline.
> - Provides spelling suggestions through the context menu.
> - Preserves capitalization when applying corrections.
>
> What it doesn't do:
>
> - Require an external spelling API or cloud spellchecking service.
>
> I've also got a small demo running that uses a Dutch dictionary generated from Wikipedia data:
>
> **[--> Demo <--](https://veldin.com/vlm-spellchecker/)**
>
> **Deployment:**
>
> The plugin can be hosted on your own server alongside its JavaScript modules and dictionary file. It is tested with TinyMCE's open-source GPL version.
>
> The demo is available to try directly in your browser.
>
> **AI Involvement:**
>
> I used some AI intergrated tools in my IDE (Visual Studio) but no direct generation of entire files.

---

> **lwh-x**（1 分） · 2026-10-18T03:32:58+08:00　
> Project Name: Tessera
>
> Repo/Website Link: [https://github.com/Limatura/tessera](https://github.com/Limatura/tessera)
>
> Docs: [https://tessera-docs-three.vercel.app](https://tessera-docs-three.vercel.app)
>
> Description:
>
> Tessera is a file and note sharing server that cleans up after itself. You upload a file, folder, code snippet or link, get a short code and a URL back, and the share is deleted once it expires or has been downloaded as many times as you allowed. Sending doesn't need an account unless you want that.
>
> We used FileCodeBox before this. It's built around anonymous pickup codes, and we kept wanting things it didn't have when we looked: syntax highlighting and previews for code, images, SVG and Mermaid, user accounts with roles and quotas, OIDC login, uploads that go straight to an S3 bucket, and encrypting on the client. So we wrote our own. We use it every day, so it will keep getting fixed.
>
> What's different:
>
> \- accounts are optional, but there if you want them: invite-only or closed sign-up, OIDC, GitHub, Discord, roles, per-account quotas
>
> \- with S3/GCS, uploads go straight to the bucket and plain downloads are redirected there, so big files never pass through your server
>
> \- SQLite, PostgreSQL or MySQL, so it can run on more than one machine
>
> \- storage: local disk, S3-compatible, Azure Blob, GCS, WebDAV. Add several from the admin panel, no restart
>
> \- CLI: \`tessera send report.pdf --expires 24\`, and --encrypt seals the file on your machine. The key lives after the # in the link, so the server never sees it
>
> \- syntax highlighting, image/SVG/Mermaid previews, link preview cards in chat apps
>
> \- optional malware scanning on upload
>
> \- one-time shares are counted in a single conditional DB update, so two people racing for the same share can't both get it
>
> \- OpenAPI spec generated from the server code and checked in CI
>
> Also: expiry, download limits, passwords, folders as one archive, UI in English, Traditional Chinese and Japanese.
>
> It's a single Rust binary and it streams uploads and downloads, so memory use doesn't grow with file size.
>
> Rough edges: it's v0.1.0-rc.1, so not 1.0 yet. The GCS backend has no tests. WebDAV only handles small files. Anonymous uploads are on by default, so read the public example config before you put it on the internet. Back up your database before upgrading, downgrades aren't supported.
>
> Deployment:
>
> Docker image: [ghcr.io/limatura/tessera:0.1.0-rc.1](http://ghcr.io/limatura/tessera:0.1.0-rc.1)
>
> Or clone the repo and run \`docker compose up -d\`, then open port 12923. The admin password is printed once in the log: \`docker compose logs tessera | grep password\`
>
> There are example env files for a personal and a public instance, and a systemd unit file.
>
> AI Involvement:
>
> We wrote this post ourselves. AI only proofread it, because English isn't our first language. The code was written with AI tools; a human decides the architecture, reviews the code and does the testing. The agent config files are in the repo (AGENTS.md, .claude/, .codex/) if you want to see how. The app itself doesn't use any AI.
>
> Feedback and issues are welcome, especially what's missing compared to what you use now.

---

> **seasl187**（2 分） · 2026-10-18T03:38:55+08:00　
> **Project Name:** carMaint
>
> **Repo/Website Link:**
> Repo: [https://github.com/seals187/carmaint](https://github.com/seals187/carmaint)
> Live demo: [https://cm-demo.seals187.com](https://cm-demo.seals187.com), login `demo` / `demodemo`, resets every 30 min
>
> **Description:**
> A lightweight, self-hosted maintenance log for your vehicles. Track services, repairs, inspections and costs per car, with photos and receipts, all in one place instead of a glovebox folder and a spreadsheet.
>
> * Multi-user: each user only sees their own vehicles
> * JSON backup and import per user
> * English, German and Spanish UI; EUR, CHF or USD
> * Plain HTML/CSS/JS on PocketBase/SQLite, no external services
>
> **Deployment:**
> Single Docker container (`ghcr.io/seals187/carmaint`) for amd64, arm64 and armv7. Grab `docker-compose.yml` and `.env.example` from the repo, set `ADMIN_PASSWORD`, then `docker compose up -d`. Works behind Caddy, Traefik or nginx.
>
> **License:** AGPL-3.0
>
> **AI Involvement:** Vibe-coded with Claude Code as the main coding tool; most of the code was written with AI assistance. I designed the features, directed the implementation and tested every change by hand, including the Docker setup behind a reverse proxy.
>
> https://preview.redd.it/7e0b3rkqy2wh1.png?width=3200&format=png&auto=webp&s=5940e96746bf7ce500fa202803cb980eccad7eda

---

> **ihatenosebleedz**（1 分） · 2026-10-18T04:03:16+08:00　
> Like many of you, I run Navidrome to stream my personal music library. One thing that always annoyed me was how much work it took to add new music. If I found an album while I was out or someone sent me an Apple Music link, I'd have to save it for later or SSH into my server and run a downloader manually.
>
> So I built MusicLab, an iOS app that makes the whole process a lot easier. I can share an album, song, or playlist from Apple Music, tap a Shortcut, and let my server handle the rest.
>
> # How it works
>
> 1. Find a song, album, or playlist in Apple Music.
> 2. Share it using the MusicLab iOS Shortcut.
> 3. MusicLab adds it to the download queue, where I can see progress, download speed, and ETA.
> 4. Once the download finishes, the music gets organized into my library and picked up by Navidrome.
>
> # Features
>
> * Live download queue with progress, speeds, decryption progress, and estimated completion times
> * Playlist downloads with .m3u8 files that preserve track order
> * Multiple library destinations
> * Self-hosted backend that works over LAN or Tailscale
> * Native iOS app built entirely on Linux using Swift Package Manager and xtool, without a Mac or Xcode
> * Prebuilt .ipa releases for sideloading
>
> The backend uses Node.js, Express, and SQLite, with amdl handling the downloads.
>
> # Links
>
> * GitHub: [https://github.com/ihatenosebleedz/MusicLab](https://github.com/ihatenosebleedz/MusicLab)
> * Setup guide: [https://github.com/ihatenosebleedz/MusicLab/blob/master/docs/SETUP\_GUIDE.md](https://github.com/ihatenosebleedz/MusicLab/blob/master/docs/SETUP_GUIDE.md)
> * iOS Shortcut: [https://www.icloud.com/shortcuts/15de06d0d8034d8c850174ff9e0ebea5](https://www.icloud.com/shortcuts/15de06d0d8034d8c850174ff9e0ebea5)
>
> It's free and open source under the MIT license.
>
> I'm still working on it, so I'd love to hear suggestions for features or improvements. If you have an idea, feel free to open a GitHub issue and I'll see what I can do!
>
> Feedback is welcome! :3

---

> **False_Act4214**（1 分） · 2026-10-18T05:11:21+08:00　
> Our teams adopted Claude Code, Codex, Copilot and a handful of homegrown agents in about a month. Then someone asked a simple question nobody could answer: *which of these can read customer data and also send things outside the company?*
>
> So I built **Control Tower**, a gateway you run yourself. Point the agents and coding assistants at it (one base URL, or roll it out to laptops with Jamf or Intune), and it draws everything they reach on a live map: models, MCP tool servers, HTTP APIs, and calls it sees going *around* it.
>
> What's in the video, all from a running demo deployment:
>
> * **The live map:** agents on the left, models and tools on the right, traffic between them.
> * **Trace an agent:** everything one agent reaches, how often, and what it costs.
> * **The matrix:** every agent against every destination, and which connections no gate can stop.
> * **Trust classes:** systems drawn as nested rings, from production and customer data out to the public internet. It flags each agent that can reach restricted data *and* send outside the company, and one click puts a gate on exactly that path.
> * **Coverage:** each team's traffic split into gated, through the gateway with no gate, and around it.
>
> Gates do more than draw: block a path, mask secrets and personal data, or hold a call until a person approves it (Claude Code and Claude Desktop show "waiting for approval" in the conversation).
>
> **Self-hosting details**
>
> * One Docker container. SQLite by default, Postgres and Redis if you want several instances. A Helm chart too.
> * Your prompts and data stay on your infrastructure. It calls your model providers and tools, plus a once-a-day check for new versions that sends only the version number (`CT_UPDATE_CHECK=off` turns it off).
> * Updates back the database up first and can be rolled back.
>
> &#8203;
>
>     docker run -p 4000:4000 -v ct-data:/data ghcr.io/joshmaster2165/controltower
>
> Set `CT_DEMO=1` and you get the demo fleet from the video, so the map is busy within a minute.
>
> **License, to be upfront:** the core (gateway, map, gates, approvals, inventory) is Apache-2.0. Enterprise features (SSO/SCIM, the audit log, multi-region and a few others) live in a separate `ee/` directory under the Elastic License 2.0.
>
> **Limits:** it can only enforce what goes through it. Traffic it only *sees* (reported by an SDK or OpenTelemetry) is drawn dashed and can't be gated until you route it through.
>
> I'd love feedback, especially from anyone running agents at work: what would you want to see on the map that isn't there?
>
> GitHub: [https://github.com/joshmaster2165/controltower](https://github.com/joshmaster2165/controltower) Docs: [https://agentcontroltower.app/docs/](https://agentcontroltower.app/docs/)

---

> **dawgwashere_**（1 分） · 2026-10-18T05:50:40+08:00　
> **Project Name:** maitake
>
> **Repo:** [https://github.com/sobakintech/maitake](https://github.com/sobakintech/maitake)
>
> **Description:** A self-hosted gateway that serves your Claude and ChatGPT/Codex subscriptions as OpenAI- and Anthropic-compatible APIs. I switched from CLIProxyAPI because I wanted proper per-user keys (allowed models, rate limits, expiry) and a dashboard instead of editing YAML. It also tracks quota live for every account, handles failover between accounts, and has a read-only quota page your users can check with their own key.
>
> **Deployment:** Docker image for amd64 and arm64, with a docker-compose.yml in the repo. You run `docker compose up -d`, take the setup token from the logs, and create the admin account. Everything else is set up from the dashboard, and data is stored in SQLite.
>
> **AI Involvement:** Design and product decisions are mine. Most of the implementation was written with Claude Code and Codex, then reviewed by me and tested against my own accounts.
>
> https://preview.redd.it/0osluhuam3wh1.png?width=1456&format=png&auto=webp&s=67265ce00aaf7294433020e95bdaac747d33ffdc

---

> **chechyotka**（1 分） · 2026-10-18T06:06:23+08:00　
> hello, working on Syncgo [https://github.com/syncgo/syncgo](https://github.com/syncgo/syncgo)
>
> SyncGo is a Golang implementation of PGSync for continuously synchronizing changes from PostgreSQL to Elasticsearch or OpenSearch
>
> U can use standalone binary or docker image
>
> Please check project, test if u are interested, and of course u can create issues and contribute to project

---

> **RUSTOFUS**（1 分） · 2026-10-18T07:11:08+08:00　
> **Project Name**: Drexius Terminal
>
> **Repo/Website Link**: GitHub: [https://github.com/DreyDreamer17/drexius-terminal](https://github.com/DreyDreamer17/drexius-terminal)
>
> **Live Web Preview**: [https://dreydreamer17.github.io/drexius-terminal/](https://dreydreamer17.github.io/drexius-terminal/)
>
> **Releases**: [https://github.com/DreyDreamer17/drexius-terminal/releases/tag/v0.1.0-beta.1](https://github.com/DreyDreamer17/drexius-terminal/releases/tag/v0.1.0-beta.1)
>
> **Description**: Drexius Terminal is a local-first, privacy-focused open-source terminal workspace and Termius alternative built with Tauri 2 (Rust), React 19, and xterm.js 6.
>
> **The Problem It Solves**: Most modern graphical SSH and SFTP clients have either moved to aggressive SaaS subscription models ($10 to $20 per month) requiring your credentials and hosts to live in someone else's cloud, or are built on heavy Electron runtimes that consume 300MB to 1GB of RAM. We wanted a snappy, zero-subscription client where server keys, credentials, and configurations remain completely in the user's control.
>
> **Key Features:**
>
> * Local-First and Encrypted: All hosts, keys, and snippets are stored locally in an AES-256 SQLCipher database derived with Argon2id. Zero telemetry, no account required, with an Emergency Recovery Key.
> * Terminal Workspace: Multi-pane splits (grid, vertical, horizontal), tabs, OSC-7 directory tracking, broadcast input across sessions, and session auto-resume.
> * Protocol Support: SSH with TOFU host-key verification, graphical SFTP tree and file editor, hardware Serial UART, and local PTY shells.
> * Zero-Knowledge Sync: Self-hostable sync relay and direct encrypted LAN pairing to sync between your PC and phone without touching proprietary cloud servers.
> * Mobile Shell (Android): Universal APK with touch scrolling in mouse-aware TUIs (htop, lazygit, OpenCode), and accessory keypad (CTRL, ALT, ESC, TAB).
> * Lightweight: Built with a native Rust backend via Tauri 2, keeping the memory footprint around 60MB RAM instead of Electron's hundreds of megabytes.
>
> **Deployment:** Clients: Pre-compiled binaries for the Public Beta (v0.1.0-beta.1) are available immediately on GitHub Releases:
>
> * Linux (.AppImage, .deb, .rpm)
> * Android (.apk universal multi-ABI)
> * Windows (.exe installer, .msi)
> * macOS (.dmg, .app.tar.gz for Apple Silicon and Intel)
>
> Self-Hosting Sync: The repo includes the zero-knowledge sync relay server (drexius-relay) which can be compiled via Cargo or run on any Linux VPS or home server to sync multiple devices without cloud intermediaries. Complete build and installation documentation is in the repository README.
>
> AI Involvement: AI coding assistants were used to speed up boilerplate generation, TypeScript interface definitions, and regex parsing. All core architecture, Rust security layers (SQLCipher and Argon2id integration), xterm touch coordinate translation, protocol bridges, and release packaging were manually planned, implemented, reviewed, and verified with unit tests and builds.
>
> https://preview.redd.it/97vv006b14wh1.png?width=2880&format=png&auto=webp&s=fff5cb5ed647e1764b5993e8b6a42e70442826b2

---

> **Mikasa0xdev**（1 分） · 2026-10-18T07:44:10+08:00　
> * **Project Name:** Openspline
> * **Repo:** [https://github.com/openspline/openspline](https://github.com/openspline/openspline)
> * **Description:**  Openspline is an open source avatar layer to existing voice AI agents. Just select an image and you can create a realtime talking avatar with lipsynced video generated locally on your GPU. You can integrate any existing voice AI agent in 5 lines of code. The lite model can generate 90+ FPS on an NVIDIA RTX4090 gpu. While it is still in very early stage, but the results look very promising.
> * **Deployment:** Can be hosted locally on an NVIDIA GPU with a single curl command (explained in github readme), and integrated with existing voice ai in 5 lines of code.
> * **AI Involvement:** Codex was used to support coding.

---

> **PaulichP**（1 分） · 2026-10-18T08:25:09+08:00　
> https://preview.redd.it/xczll7z6d4wh1.png?width=2880&format=png&auto=webp&s=674792c169c7355fe2228940775c786fe452d7a4
>
> * **Project Name:** Portunus
> * **Repo/Website Link:** [https://github.com/Portunus-org/Portunus](https://github.com/Portunus-org/Portunus)
> * **Description:** A small self-hosted panel for sing-box. I made it for my own server that my family and friends use. It's one container (about 93 MB, uses around 15 MB of RAM), sets up VLESS Reality, Hysteria2, TUIC, Trojan or Shadowsocks with a wizard, and handles clients with limits and subscriptions. You can add more servers with failover and route traffic by lists. By default the panel only listens on localhost, so you open it through an SSH tunnel.
> * **Deployment:** Docker Compose, amd64 and arm64. Install is three commands in the README, more in docs/DEPLOY.md.
> * **AI Involvement:** I used an AI coding assistant. Every change is reviewed by me, and the code is checked for vulnerabilities with security scanners before each release. I also run it on my own servers.

---

> **Sean0926**（1 分） · 2026-10-18T08:59:18+08:00　
> https://preview.redd.it/xli1fm9lk4wh1.png?width=1200&format=png&auto=webp&s=7a8a62ff97a3542750e10966460225fa02dae847
>
> * **Project Name**: HomelabScribe
> * **Repo/Website Link**: [https://github.com/HoneyBearTech/homelabscribe](https://github.com/HoneyBearTech/homelabscribe) and [https://homelabscribe.com](https://homelabscribe.com)
> * **Description**: Documentation for your homelab that writes itself. It scans your Docker hosts (and Proxmox) and writes Markdown: a page per service and per host, an overview, and a "what changed" log. Run it again and the docs update, while anything you wrote in a page's Notes section is kept exactly as you left it. The output works in an Obsidian vault or a Git repo. It is read-only (Docker through a read-only socket proxy, Proxmox through an audit-only token), has no telemetry or update checks, and records env var names, never values. It recognizes about 80 common self-hosted apps, reads Nginx Proxy Manager to show each service's real address, and lets you describe things a scanner can't see, like a Pi-hole on a Raspberry Pi. The core is AGPL-3.0 and free for one Docker host. Pro adds multiple hosts, Proxmox, a break-glass guide for family, topology diagrams, scheduled runs and Discord/ntfy alerts. Pro is a $2.99 lifetime license that I sell. I'm the only developer.
> * **Deployment**: Docker image (ghcr.io/honeybeartech/homelabscribe, also honeybeartech/homelabscribe on Docker Hub, releases signed with Sigstore) or pipx install homelabscribe. A docker-compose example with a read-only socket proxy is in the repo (docker-compose.example.yml), and the README covers install. To try it with no setup, run homelabscribe demo for a made-up lab.
> * **AI Involvement**: I use an AI coding assistant for much of the development: code, tests, docs and CI. I review every change before it merges. All changes go through a pull request, and CI runs the tests, CodeQL, dependency review and secret scanning on each one, plus fuzzing on the parsers. I also run it daily on my own lab (5 Docker hosts, a 2-node Proxmox cluster, Nginx Proxy Manager).
> * Looking for 5 beta testers: I'd like five people to try Pro. You get a free lifetime key in return for honest feedback on your own lab. It has only run on mine so far, so I expect it to meet setups I haven't seen. Reply here with what you run if interested.

---

> **stormthepalacegates**（1 分） · 2026-10-18T09:21:31+08:00　
> **Project Name:** embalm
>
> **Repo/Website Link:** https://git.thromb.us/eve/embalm (MIT)
>
> **Screenshot:** https://files.catbox.moe/wus3xn.png (demo data)
>
> **Description:** embalm watches SoundCloud profiles, YouTube channels (Videos and Releases), Bandcamp artists and anything else yt-dlp can list, and saves every upload as the original file, untouched. When an artist deletes or privates something you follow, it emails you and keeps your copy, marked as deleted. I built it because tracks I liked kept vanishing from SoundCloud with no trace.
>
> - Downloaders are pluggable: the bundled cobalt, your own cobalt, yt-dlp, or any command you give it
> - Web UI with a player, per-profile views and a settings page over `.env`
> - Optional password login; meant to run on your LAN or tailnet
>
> **Deployment:** `git clone`, then `docker compose up -d`. Install, config and downloader options are in the README. It also runs without Docker on plain Node.
>
> **AI Involvement:** written with AI assistance (Claude); I run it daily on my own server.

---

> **kyrnveil**（1 分） · 2026-10-18T11:09:14+08:00　
> **Project Name: FilterHelm**
>
> **Repo/Website Link:** [https://github.com/nulthara/filterhelm](https://github.com/nulthara/filterhelm)
>
> **The Problem it solves:** I run multiple Pi-hole instances on my network for redundancy. I was having issues with configuration drift between the instances; either missed configuration, or inconsistencies between the instances. This helps to identify that drift in one spot.
>
> **Description:**
>
> FilterHelm can compare blocklists, local DNS entries, and basic settings across multiple Pi-hole instances, helping identify the differences and providing a way to resolve them.
>
> It also supports managing those configurations directly. Changes are intentionally limited to one Pi-hole instance at a time to ensure instance changes are isolated.
>
> There is also some basic functionality for query inspection and backup and status monitoring.
>
> **Deployment:** Docker image is available at [ghcr.io/nulthara/filterhelm](http://ghcr.io/nulthara/filterhelm), and has attestation by a SPDX SBOM.  The Repo has example instructions as well: [https://github.com/nulthara/filterhelm#run-the-published-image](https://github.com/nulthara/filterhelm#run-the-published-image)  Providing a sample compose is on my list.
>
> **AI Involvement:** I’ve used AI-assisted development tools throughout the project, with a human-in-the-loop approach to implementation and decision making. I defined the high level feature requirements, leveraged Claude to iterate over the design, and Codex to provide the programming.
>
> https://preview.redd.it/9cxmkvtp65wh1.png?width=1736&format=png&auto=webp&s=f5c175b80841e79f3db534c9bcfa8709cf8b0045

---

> **Top_Cup7031**（2 分） · 2026-10-18T11:25:59+08:00　
> **Project Name:** usajobs-monitor
>
> **Repo/Website Link:** [https://github.com/amv2/usajobs-monitor](https://github.com/amv2/usajobs-monitor) (MIT, v0.1.0)
>
> **Description:** A cron-friendly CLI that watches the US federal jobs API (USAJOBS) and sends you only the postings worth opening. It started as a personal script I ran three times a week for my own federal job search. I've cleaned it up and released it for anyone else who's job hunting, or helping someone who is.
>
> The problem it solves: the USAJOBS site search is keyword-based, so you get swamped with jobs you can't apply to. This filters on the structured fields instead:
>
> * Appointment type, pay plan, job series, excluded series, and whole-word title terms.
> * Hiring path and eligibility (public, status, excepted service, special authorities). Anything that depends on a special authority is flagged VERIFY ELIGIBILITY instead of being assumed.
> * GS grade + locality pay floors from bundled 2026 OPM pay tables.
> * Tracks NEW and CLOSING SOON across runs, and keeps a near-miss list showing the one check each job failed.
> * Delivers a digest to **ntfy**, Discord or Slack webhooks, or any SMTP server, with a per-channel send ledger so retries never double-send. Reports come as DOCX/XLSX/HTML/CSV.
>
> **Deployment:**
>
> * Released and installable now (`git clone`, then `pip install -e .`, then `usajobs-monitor init` for a setup wizard). The README covers install, config and scheduling.
> * No server, database or web UI. Run it from the Docker scheduler, cron, a systemd timer, launchd or Task Scheduler. Config is a TOML profile (you can keep several), and history is flat JSON.
> * Secrets come from env vars or the OS keychain. Secrets in the config file are rejected.
> * Each run builds in its own folder and only publishes after validation, so a failed run never clobbers the last good report.
> * Outbound traffic goes only to the USAJOBS API (free key required) and the delivery targets you configure. No telemetry.
> * **Docker:** a Dockerfile and `compose.example.yaml` are included. `docker compose up -d` runs one long-lived container with a built-in scheduler (days, times and TZ set by env vars), so no host cron is needed. Data lives in a `./data` volume, and the container runs as non-root.
> * Or run it as a plain Python 3.11+ package, tested on 3.11 to 3.14 on Linux and Windows (I run it on macOS), or with the optional GitHub Actions workflow if you don't have an always-on box.
>
> **AI Involvement:** Significant, and I want to be upfront about it. I wrote the original script. I then used Claude to generalize it into a package, write the tests (293) and docs, and add the delivery channels, keychain support, and setup wizard. I reviewed the changes, and before release I ran it live side by side with my original script and the results matched. There's also an *optional* AI feature for resume fit notes; it's off by default and can use a local model instead of an API.
>
> Not affiliated with OPM or USAJOBS.

---

> **National-Type-2096**（1 分） · 2026-10-18T11:55:03+08:00　
> Project Name: InkognitoPDF
>
> Repo/Website Link: [https://github.com/damofer/inkognitopdf](https://github.com/damofer/inkognitopdf) (Apache-2.0) · hosted demo: [https://inkognitopdf.com](https://inkognitopdf.com)
>
> Description: A PDF editor and document scanner that does all the processing in the browser. I built it because every free PDF tool I tried wanted me to upload contracts, IDs and bank statements to someone else's server. Here the files never leave the device, so self-hosting it is just serving static files.
>
> What it does:
>
> * Edit existing text keeping the original font, add text, images and whiteout.
> * Scan with the phone camera: edge detection, perspective correction, black-and-white "photocopy" mode, ID-card mode, and OCR (English and Spanish).
> * Sign: drawn, typed, or PAdES digital signatures with your own certificate; several signers in order.
> * Forms, annotations, merge, split, compress, passwords.
> * True redaction (removes the content underneath), automatic detection of personal data, and a "privacy X-ray" that shows what a PDF hides (metadata, invisible text, attachments, JavaScript, old versions inside incrementally saved files) and saves a clean copy.
> * Compare two versions of a PDF. UI in English and Spanish.
>
> Deployment:
>
> * Docker: docker build -t inkognitopdf . then docker run -d -p 8080:80 inkognitopdf. It's a multi-stage build that compiles the site with Node and serves it with nginx, with the same routes and cache headers as the hosted version.
> * Without Docker: npm install && npm run build, then serve dist/ with nginx, Caddy or anything static. The landing page is at / and the app at /app/; add one rewrite so /app/\* falls back to /app/index.html.
> * No backend, database, workers or API keys. The container only serves files.
> * Put it behind HTTPS (your reverse proxy is fine): browsers only allow the camera and the offline service worker in a secure context.
> * Installable as a PWA and works offline once loaded.
> * Outbound traffic: none on your own domain. The optional, consent-based analytics only load on the official domain. No telemetry otherwise.
>
> AI Involvement: Significant, and I want to be upfront about it. I designed the product and wrote the specs, and most of the code was written with Claude. I reviewed the changes, and every feature ships with unit and end-to-end tests (several hundred), plus manual testing on desktop and Android before release.
>
> https://preview.redd.it/syyb88i5f5wh1.jpeg?width=720&format=pjpg&auto=webp&s=83a652538edc4184f6d171be4cfa2d044def328a

---

> **lwh-x**（1 分） · 2026-10-18T12:14:42+08:00　
> https://preview.redd.it/x5y0shwni5wh1.png?width=1219&format=png&auto=webp&s=7a6df191b03e15acf5b3ab70e63da497f8eff9ec
>
> Project Name: Tessera
>
> Repo/Website Link: [https://github.com/Limatura/tessera](https://github.com/Limatura/tessera)
>
> Docs: [https://tessera-docs-three.vercel.app](https://tessera-docs-three.vercel.app)
>
> Description:
>
> Tessera is a file and note sharing server that cleans up after itself. You upload a file, folder, code snippet or link, get a short code and a URL back, and the share is deleted once it expires or has been downloaded as many times as you allowed. Sending doesn't need an account unless you want that.
>
> We used FileCodeBox before this. It's built around anonymous pickup codes, and we kept wanting things it didn't have when we looked: syntax highlighting and previews for code, images, SVG and Mermaid, user accounts with roles and quotas, OIDC login, uploads that go straight to an S3 bucket, and encrypting on the client. So we wrote our own. We use it every day, so it will keep getting fixed.
>
> What's different:
>
> \- accounts are optional, but there if you want them: invite-only or closed sign-up, OIDC, GitHub, Discord, roles, per-account quotas
>
> \- with S3/GCS, uploads go straight to the bucket and plain downloads are redirected there, so big files never pass through your server
>
> \- SQLite, PostgreSQL or MySQL, so it can run on more than one machine
>
> \- storage: local disk, S3-compatible, Azure Blob, GCS, WebDAV. Add several from the admin panel, no restart
>
> \- CLI: \`tessera send report.pdf --expires 24\`, and --encrypt seals the file on your machine. The key lives after the # in the link, so the server never sees it
>
> \- syntax highlighting, image/SVG/Mermaid previews, link preview cards in chat apps
>
> \- optional malware scanning on upload
>
> \- one-time shares are counted in a single conditional DB update, so two people racing for the same share can't both get it
>
> \- OpenAPI spec generated from the server code and checked in CI
>
> Also: expiry, download limits, passwords, folders as one archive, UI in English, Traditional Chinese and Japanese.
>
> It's a single Rust binary and it streams uploads and downloads, so memory use doesn't grow with file size.
>
> Rough edges: it's v0.1.0-rc.1, so not 1.0 yet. The GCS backend has no tests. WebDAV only handles small files. Anonymous uploads are on by default, so read the public example config before you put it on the internet. Back up your database before upgrading, downgrades aren't supported.
>
> Deployment:
>
> Docker image: [ghcr.io/limatura/tessera:0.1.0-rc.1](http://ghcr.io/limatura/tessera:0.1.0-rc.1)
>
> Or clone the repo and run \`docker compose up -d\`, then open port 12923. The admin password is printed once in the log: \`docker compose logs tessera | grep password\`
>
> There are example env files for a personal and a public instance, and a systemd unit file.
>
> AI Involvement:
>
> We wrote this post ourselves. AI only proofread it, because English isn't our first language. The code was written with AI tools; a human decides the architecture, reviews the code and does the testing. The agent config files are in the repo (AGENTS.md, .claude/, .codex/) if you want to see how. The app itself doesn't use any AI.
>
> Feedback and issues are welcome, especially what's missing compared to what you use now.

---

> **novica**（1 分） · 2026-10-18T16:38:03+08:00　
> **Project Name:** competence
>
> **Repo/Website Link:** [**https://github.com/novica/competence**](https://github.com/novica/competence)
>
> **Description:** Some time ago I was asked to come up with a plan to uspkill coworkers. I tried strarting that by mapping skills first. I used an Excel sheet I created based on [Implementing a Skills Matrix Across Data Teams](https://medium.com/@andy-sawyer/implementing-a-skills-matrix-across-data-teams-58675755e20d). But as the exce become more and more comlicated to maintain, espeacially over time and versions, I tried moving it all to a locally run FastAPI.
>
> **Deployment**: run with uvx
>
> **AI Involvement:** Yes.

---

> **MasterOnion_**（1 分） · 2026-10-18T17:18:41+08:00　
> **Project Name:** UniFi Protect Archive UI
>
> **Repo**: https://github.com/dree007/unifi-protect-archive-ui
>
> **Description**: For those of you who have some Unifi Protect Equipment and have the Continuous Archiving setting enabled might relate to my problem here - there‘re hundreds of archived clips but no way to simply display them properly.
>
> It always bothered me to have the possibility to continuously archive all Protect clips (I.e. onto a NAS), but not having the proper frontend to access those files.
> All these thousands of clips in a weird and search-unfriendly structure…
> So I made one - dedicated to viewing your Protect Archives
>
> **Deployment**: Easy-peasy via Docker-compose
>
> **AI Involvement**: Yep
>
> https://preview.redd.it/3xp83jp017wh1.jpeg?width=887&format=pjpg&auto=webp&s=c4ddd3f2773c033364ece156fcd537cbc9d9cc3f

---

> **Equivalent-Pen-5054**（1 分） · 2026-10-18T18:36:22+08:00　
> * **Project Name: minecraft-k8s**
> * **Repo/Website Link:** [https://codeberg.org/meik99/minecraft-k8s](https://codeberg.org/meik99/minecraft-k8s)
> * **Description:** It's a Kubernetes Operator that can manage minecraft server instances. It also comes with a webui so your friends can simply create a new server on your hardware if they are registered with your IdP (I use casdoor myself).
> * **Deployment:** Currently I have the images needed on my private registry, so you will have to build them yourself first to deploy them. Since it is an operator, you also have to have a Kubernetes cluster available to run it.
> * **AI Involvement:** I am going to copy paste the same disclaimer I have on the repository README as well:
>
> I am a senior software and systems engineer and use AI mainly as advisor not really as developer. With the exception of things I just can't be arsed to do. The following list itemizes the things an AI has written to a larger degree than I have and an explanation:
>
> * CSS Color tokens: My prompt was basically "Create some css color tokens that fit a Minecraft theme" I didn't care enough to write `--color-<gemstone>` over and over again. It's also better to keep the darkmode tokens in sync than me
> * The API endpoints in the operator and the Services for the website I wrote the initial GET and POST request, then let it implement the other CRUD operations. REST calls are so much boilerblate that I decided an AI is cents well spent
> * The kubernetes resource building within the operator code.return &appsv1.Deployment { Metadata:, Spec: }  Pretty much boiler plate as well, not really an engineering challenge
> * Some of the css classes. Most of them I have written myself, I think the status pill I generated. I believe when going through the source it will be pretty obvious which are generated and which are not. I personally hardly use letter spacing or numerical font weight, so that is probably a good indicator.
> * The oidc flow in the website. It's a well known well documentation protocol I have implemented dozens of times and just didn't have the patience to implement it yet again because it usually generates well. Once I implement other login options I will likely have to rewrite it anyway to fit with them. For now, it is also generated.
>
> Actually now that I am writing this I might have gone a bit overboard with AI usage... Well, the project is pretty basic and has a lot of refactoring and features still coming. I will try to do more myself going forward.
>
> To go on a tangent, this is what I currently have on my personal roadmap:
>
> * More login options (which will also require a DB) Username-password at least, so people don't need and IdP for minecraft
> * Proper RBAC Currently, logged in users can see the instance of everyone else as well
> * Better UX when managing servers I am currently not even sure the console streaming works (probably not) Also, a user shouldn't have to now what cpu requests and limits are. I want to replace that with a predefined list of player count that translates to requests and limits
> * Maybe some admin stuff? Like limiting specific users to a max player count and so on.

---

> **by-neo**（1 分） · 2026-10-18T19:14:22+08:00　
> https://preview.redd.it/zv00bv5dl7wh1.png?width=1080&format=png&auto=webp&s=21033d996f5b8d0d629a1d79e4a5089929ebcc73
>
> \*\*Project Name:\*\* Linkstow
>
> \*\*Repo/Website Link:\*\* [https://github.com/by-architect/KarakeepMobile](https://github.com/by-architect/KarakeepMobile)
>
> \*\*Description:\*\*
>
> Linkstow is an open-source Android client for Karakeep, the self-hosted "bookmark everything" app. It's an unofficial, community app, not affiliated with Karakeep.
>
> I wanted a faster way to go through my Karakeep bookmarks on my phone, treating archived as "read" so my lists work like an inbox. Main features:
>
> \- Works with any Karakeep server: self-hosted (including LAN \`http://\` and private certificates) or Karakeep Cloud
>
> \- Sign in with email + password, or an API key (for SSO-only servers)
>
> \- Custom request headers for servers behind Cloudflare Access, Authelia or another auth proxy
>
> \- Your password is never stored; it's exchanged for an API key kept in secure storage
>
> \- Lists and tags in a side menu, with unread/total counts on each
>
> \- Add links, notes and images; sort by date, title or website
>
> \- Search with Karakeep's query language
>
> \- In-app viewer with Karakeep's Reader view; swipe to the next bookmark
>
> \- Custom swipe actions on cards (archiv, delete), with undo on everything
>
> \- GPL-3.0, no ads, no tracking
>
> \*\*Deployment:\*\*
>
> It's a client app, so there's nothing ting Karakeep server (developed against
>
> 0.33.x). Install it from:
>
> \- Google Play: [https://play.google.com/store/apps/details?id=com.byarchitect.linkstow](https://play.google.com/store/apps/details?id=com.byarchitect.linkstow)
>
> \- My F-Droid repository: https://fdroidfingerprint=50941BDAC56B056A520ABFA3FC7DAAB789DEE5B83B295DA54A1961C7BC8A91C9
>
> \- It has been accepted into the main F-Droid repo and should show up there soon.
>
> Setup and build instructions are in the README. Enter your server address, sign in, done.
>
> \*\*AI Involvement:\*\*
>
> I used Claude Code (Anthropic's AI codiuilding it: writing and refactoringcode, tests, release scripts and store listings. I set the direction, designed the features, reviewed the changes and tested the app on real devierver.

---

> **scubanarc**（1 分） · 2026-10-18T22:35:34+08:00　
> Site works well, I definitely learned a few new things.
>
> I find the burgundy on green color theme to be hard on my eyes.

---

> **frozen_stark**（1 分） · 2026-10-18T22:37:18+08:00　
> Hey everyone! I built NetHub – a free, open-source Windows 11 tool to detect CGNAT (RFC 6598 100.64.0.0/10) vs Public IP and 1-click UPnP port forward for local game servers (Minecraft, Palworld, CS2, RDP) without router passwords.
>
> Includes both a CLI and a local Web UI on localhost:8080!
>
> GitHub: [https://github.com/Frozen-starTony/nethub](https://github.com/Frozen-starTony/nethub)
>
> Releases (.exe): [https://github.com/Frozen-starTony/nethub/releases/latest](https://github.com/Frozen-starTony/nethub/releases/latest)

---

> **Plus-Storage**（1 分） · 2026-10-18T23:28:58+08:00　
> https://preview.redd.it/hvk8ia33v8wh1.png?width=493&format=png&auto=webp&s=7bac9ae86a4eca96d41897907dd2eb3bd8c135d2
>
> **Project Name:** Music Butler
>
> **Repo/Website Link:** [`https://github.com/BoiMat/Music-Butler`](https://github.com/BoiMat/Music-Butler)
>
> **Description:**
>
> An AI librarian for a self-hosted music library. You ask for songs in a chat, in whatever mangled form you remember them ("yo no lo se eriice, joezi cola, leave before you love me marshmello"), and a minute later they are on your phone with the correct artist credits, album, year, square cover art and time-synced lyrics.
>
> The problem it solves is: getting music in, tagging it properly, and keeping the library growing without turning into a second job.
>
> * **Add songs by name**, one or many per message. Duplicates and near-duplicate artist spellings are caught before anything downloads.
> * **Import a whole Spotify playlist** (Exportify CSV) in the background. Each song is matched by artist, title and ±3 s length; anything uncertain is reported rather than guessed, and the playlist appears in your player under its own name.
> * **Weekly discovery**: new songs from the radios of what you liked or rated highly, at least 5 by artists new to you, collected in a *Discover Weekly* playlist. Songs leave the library when you rate them 1 star.
> * **Weekly audit**: retries missing lyrics as LRCLIB grows, fills missing release years, flags things like songwriters wrongly credited as track artists.
> * Both weekly jobs report in chat and justify themselves ("because you like …").
>
> The agent is not a security boundary: it gets exactly one command (`butler.sh`), never a shell and never Docker.
>
> **Deployment:**
>
> Docker Compose. Navidrome uses its official image; a small tools container (yt-dlp, ffmpeg, mutagen) is built locally:
>
>     git clone https://github.com/BoiMat/Music-Butler.git
>     cd Music-Butler
>     ./scripts/setup.sh --start
>     docker compose --profile tools build downloader
>
> Then any Subsonic client (I use Tempo/Tempus on Android). For the agent, the bundled local one needs no API key or account (`ollama pull qwen2.5:7b && python3 scripts/agent.py`); if you already use Claude Code, Codex or Hermes, there are skills in `skills/`. README covers the quickstart, `docs/REFERENCE.md` the request format, fix-up commands, discovery rules and backups, `docs/VALIDATION.md` what was actually tested. Containers run read-only, non-root, no capabilities; Navidrome binds to loopback; downloads are restricted to an allowlist of hosts; backups are encrypted restic snapshots. Linux is the main target, macOS with Docker Desktop works.
>
> Caveat: songs come from YouTube (Music) and the Internet Archive through yt-dlp. Whether you may download a given recording depends on where you live and the source's terms. It is a personal library tool, not a sharing service.
>
> **AI Involvement:**
>
> *At runtime, by design:* the whole point is that an LLM agent drives the library. It runs against a local Ollama model, or against Claude Code / Codex / Hermes if you already use one. Nothing is sent anywhere if you use the local model.
>
> *In development:* I wrote it with heavy use of Claude Code. What I would offer against the "AI slop" worry is the boring evidence: it has been running daily on my own library since late September (\~400 releases now), there are 90 tests in the container suite plus host-side tests, the docs are written rather than generated, and the security boundary around [`butler.sh`](http://butler.sh), removal only by 1 star, and refusing to guess on uncertain playlist matches rather than silently importing the wrong song. Most of the last month has gone into the failures that only show up in real use: Italian CSV headers, missing release years, a 403 retry, playlist reports that were too noisy to read.
>
> Happy to answer anything, and genuinely curious what people would want an agent to do with their library that this does not.

---

> **Ethno_Synth**（1 分） · 2026-10-19T03:02:03+08:00　
> https://preview.redd.it/fb6jlssnu9wh1.jpeg?width=1080&format=pjpg&auto=webp&s=624fd3b40e7d0f00cd48da17130d2cf7405196e0
>
> **Project Name**: Molfar Vertep
>
> **Repo/Website Link**: [https://github.com/MolfarWav/Molfar.Vertep](https://github.com/MolfarWav/Molfar.Vertep)
>
> **Description**: Self-hosted app for AI roleplay (story chats with characters you create or import). It runs on your machine and connects to almost any model. I built it because most frontends assume big cloud models, so this one is tuned for small and free models: short prompts, visible token counts, memory kept as chapters instead of full chat history. First release 11 Oct 2026, current v1.2.3. Free, AGPL-3.0.
>
> **What it connects to:**
>
> * OpenRouter (including free models), Anthropic and ChatGPT subscriptions, DeepSeek, Moonshot, NanoGPT
> * Any OpenAI-compatible server
> * Local servers: llama.cpp, vLLM, LM Studio
>
> **What it does:**
>
> * One-on-one and group chats (group narrator mode voices the whole scene in one reply)
> * Long memory: scene notes after each reply, chapters per scene, character temper, linked chats that pass a short backstory instead of full history
> * Prompt inspector: shows every part of each request with its token counts, any part can be switched off for one chat
> * Card, lorebook and preset editors; card translate and structure helpers
> *  Card imports: Chub, RisuRealm, CharaVault, Wyvern, Pygmalion, JannyAI, or a pasted link
> *  Image generation: OpenRouter, NanoGPT, local ComfyUI / Forge / AUTOMATIC1111 (LoRAs, sampler, Danbooru tags for anime checkpoints)
> * Built-in helper (Molfar) that edits cards, lorebooks, presets and app code with you, and can draw avatars and backgrounds straight into the card
> * Manual phone-to-desktop sync, no background uploads
>
> **Deployment**: v1.2.3 is released and ready to download. Windows: Molfar-Vertep.bat launcher (start, update, rollback menu). Binaries for Windows, macOS and Linux plus an Android APK on each GitHub release page.
>
> Docker: [ghcr.io/molfarwav/molfar-vertep](http://ghcr.io/molfarwav/molfar-vertep) (:latest and version tags).
>
> Docs: README and CHANGELOG in the repo, plus how-to-get-it notes on every release. No account needed.
>
> Your data stays on your machine; sync runs only when you press Push / Pull, through your own Google Drive folder or a folder you choose (USB stick, Syncthing).
>
> **AI Involvement**: Solo dev project. I plan and test every change by hand on real chats; AI coding help drafts code which I review. Release notes are written by me.

---

> **ItsPwn**（1 分） · 2026-10-19T03:19:47+08:00　
> I would love this for OLX and Vinted which are popular in europe fyi.
>
> This is a great addition

---

> **KaneD2082**（1 分） · 2026-10-19T03:49:58+08:00　
> \*\*Project Name:\*\* Patch or Pass
>
> \*\*Repo/Website Link:\*\* https://patchorpass.beehiiv.com
>
> \*\*Description:\*\* A free weekly email that answers one question for self-hosters: "Is anything I run being actively exploited right now?" Every Wednesday it pulls the CISA Known Exploited Vulnerabilities list and FIRST EPSS scores, filters them down to common homelab and small-office gear (Proxmox, TrueNAS, UniFi, pfSense, Synology, QNAP, Windows, firewalls, VPNs), and marks each item Patch now, Batch, or Watch, with the fixed version and a link to the vendor advisory. Most weeks that's a handful of items instead of a 200-CVE dump. If none of the usual homelab gear is affected, it says so, so you can skip patching that week.
>
> \*\*Deployment:\*\* Not an app, so there's nothing to install. It's a free newsletter you can read on the web or by email, and you can unsubscribe anytime. Past issues are on the site, and here's Issue #0: https://patchorpass.beehiiv.com/p/patch-or-pass-0
>
> \*\*AI Involvement:\*\* I use an AI assistant to pull the KEV and EPSS data. Each fix is checked against the official vendor advisory. No made-up CVEs or scores.
>
> Tell me what gear you run and I'll add it to the filter list.

---

> **fi_nding_a_way**（2 分） · 2026-10-19T03:55:47+08:00　
> https://preview.redd.it/eiz2il8n6awh1.png?width=554&format=png&auto=webp&s=1ab83a1a5266b22b168bfa02390bf7bf76b495fb
>
> **Project name:** Count Dracula
>
> **Repo / Website Link:** [https://github.com/selfhosters-cc/count-dracula](https://github.com/selfhosters-cc/count-dracula)
>
> Free hosted version available here: [https://countdracula.cc/](https://countdracula.cc/)
>
> **Description:**
>
> Each year I track how many trick-or-treaters come to our door, and last year I made a huge counter on an old fridge box and displayed it where all the parents could see it, and I broke up the counts into half-hour blocks.  Surprisingly, this was of big interest to many of the parents that stopped.
>
> So for this year I built Count Dracula which lets me track the number of kids showing up on my phone (optionally including costume types) and a large counter is shown on a TV in my garage, and I also plan to project it onto my garage door.
>
> **AI Involvement:** Totally vibe-coded. I've been building software for decades, this was a fun weekend project with Claude.  Used Matt Pocock's wayfinder heavily to plan and build.
>
> **How it works:**
>
> Helpers at the door tap each kid in on their phones (one big button, or a costume tile). A TV facing the porch counts them live: confetti for every kid, a race against last year's night as a ghost line, a costume leaderboard, a headstone every 50th kid, and secret golden-ticket numbers that win a prize.
>
> No analytics, no ads.
>
> The hosted version has a map feature so you can see activity from other houses around your neighbourhood and the world (opt-in only).
>
> I'd love feedback, especially from anyone who's tried to count their own trick-or-treaters before.

---

> **LeonardoIz**（1 分） · 2026-10-19T04:17:06+08:00　
> https://preview.redd.it/0wf49pjiaawh1.png?width=2560&format=png&auto=webp&s=375dffd92aa957ce19650cd4ccfee765a6d074a5
>
> **Project Name:** Artifax
>
> **Repo/Website Link:** [https://github.com/LeonardoIz/artifax](https://github.com/LeonardoIz/artifax) (MIT)
>
> **Description:**
>
> Lately I've been using Claude a lot to take class notes, and I wanted somewhere to store them and share them with friends. I found Postplan and liked the idea, but wanted something simpler to self-host without Postgres or S3, so I built my own.
>
> Artifax is a small place where you or your agents upload HTML pages, images, PDFs, logs or any other file with curl and get back a stable link. Each artifact can be public (listed on the home page), unlisted (anyone with the link) or private (admin only), and there's a small admin panel with previews and API tokens. Each instance also serves an agent skill at /skill, with its own URL already filled in, so Claude Code and similar agents know how to publish to it.
>
> **Deployment:** It's a single Go binary with SQLite and files on disk, so there are no external services and a backup is just copying one directory. There's a Docker image for amd64 and arm64 that runs as non-root on a read-only filesystem, plus a compose file and prebuilt binaries in the releases. Login works with any OIDC provider (Authelia, Authentik, Keycloak…) using group-based access, or with a single email and password.
>
> **AI Involvement:** It was developed with AI assistance (Claude Code). I made the design decisions and reviewed and tested everything, but most of the code was written with AI help.
>
> Feedback is very welcome, especially on the security model and anything that's awkward to deploy.

---

> **SensaiOpti**（2 分） · 2026-10-19T04:22:41+08:00　
> This looks interesting, but I'm not sure I'd really get much use out of it aside from a simple, singular run. Still, I'm happy to help test if you're looking for more places to test it.
>
> Regardless of that, I do think I'mma fire up the free version and see how it looks at my lab. I don't do anything super fancy, I'm just shit at documentation and this could help make it easier. :-)

---

> **sandmik**（1 分） · 2026-10-19T04:49:04+08:00　
> **Portunus** — a self-hosted password manager with no database. Your encrypted vault is a single file in your own Google Drive
>
> **Repo**: [https://github.com/ralphv/portunus](https://github.com/ralphv/portunus)
>
> Hey r/selfhosted, I built **Portunus**, a self-hosted, zero-knowledge password/secrets manager with a private storage model: there is no database. Your entire vault is a single encrypted file that lives in *your own* Google Drive, the server just brokers OAuth and proxies Drive calls. How it works:
>
> **Everything is encrypted in the browser** (Argon2id + XChaCha20-Poly1305) before it touches the network. The server never sees plaintext or your master password.
>
> **Unlock requires password** ***and*** **a keyfile**. A leaked password alone can't brute-force the vault, and the keyfile alone is useless too.
>
> **Single stateless Docker image** (Next.js standalone, non-root). Sessions are encrypted JWT cookies; state lives in the Drive file. `docker compose up -d` and you're running. You need to create a google project first though,  (free Cloud project, \~10 min, documented in the README)
>
> Password-manager UX: search, quick-copy, generator, auto-lock with a visible countdown, re-auth on save, conflict detection on concurrent writes.
>
> Drive access is scoped to `drive.file` \-> the app only ever sees files it created.
>
> AGPL-3.0, TypeScript/Next.js.
>
> Happy to answer questions — and genuinely curious what people think of Drive-as-backend vs. running a real DB.
>
> **You own your data!**
>
> https://preview.redd.it/mx0e50c6gawh1.png?width=1498&format=png&auto=webp&s=94dd1b2352861f43e5bf2c711820925cd56b63ff

---

> **deepakprakash**（1 分） · 2026-10-19T05:18:53+08:00　
> **Project Name:** Mesopod
>
> **Repo/Website Link:** [https://mesopod.com/homelab/](https://mesopod.com/homelab/)
>
> **Description:** Mesopod brings self-hosting to everyone.
>
> I've been self-hosting for four years now and even though I'm as technical as they come, it has been quite challenging to have a clean setup, keep the apps updated and running. A few months ago, I visited a semi-technical relative who was very interested in running a media server and even though we tried, it was impossible for him to setup anything more than Plex before being completely overwhelmed with the technical complexity.
>
> Following that, I decided to build a platform that brings self-hosting to everyone - a single command server setup, followed by one click deployment of any app in our catalog. Apps keep running, even after they crash and updates are single click (automatic coming soon). Every app gets a unique url with fully valid HTTPs, completely managed by us. All the apps and data stay on your machine and traffic is fully restricted to your network; ie, we don't see any of it.
>
> So it is a bit meta compared to most of the apps posted (I hope that is okay).
>
> **Deployment:**
>
> Mesopod is in closed beta – once logged in, installation is a single script that you run; the script installs a small kubernetes cluster (k3s) that connects to the platform. App installation then is a single click.
>
> Feedback is very welcome and I would love to onboard the first few users personally.
>
> **AI Involvement:** AI has been used significantly for producing code, extensive tests and security assessment. FWIW, I have 20+ years experience working at deep tech companies and I was most recently CTO/cofounder at a women's health startup that is now a scale-up. I'm obsessive about quality, robustness and security and coding agents have been a boon to enforce them.

---

> **Barmazoid**（1 分） · 2026-10-19T06:16:06+08:00　
> Project Name: Plombir Git
>
> Repo: [https://github.com/Nettechnologys/plombir-git](https://github.com/Nettechnologys/plombir-git)
>
> Description: A self-hosted Git forge in the Gitea/Forgejo space — repos, issues, PRs with code review, CI, wiki, package registries — one Rust server process plus a static SvelteKit UI. What's different: AI agents are first-class but limited participants. Any user can create a bot account they own; its tokens can be narrowed to named repos and named MCP tools and kept off protected branches; a bot's approval never counts toward required approvals; CI for a fork PR runs only after a person approves its exact head commit. MCP is built into the server, and every tool call lands in the audit log. Runs a subset of Gitea Actions workflows. Our small production instance idles at \~258 MB RSS.
>
> Deployment: v0.2.0 (released Oct 17): Linux x86\_64/aarch64 archives, multi-arch image [ghcr.io/nettechnologys/plombir-git:v0.2.0](http://ghcr.io/nettechnologys/plombir-git:v0.2.0), and a compose bundle pinned to the image digest. Setup is in README and deploy/README.md.
>
> AI Involvement: Heavy, so saying it upfront: the code is written by AI coding agents; I decide what to build and review it. Every push passes fmt/clippy/docs-as-errors plus \~80 contract checks; \~3,400 tests. Fork of IronForge (see NOTICE), AGPL-3.0.
>
> Early project, so blunt feedback is welcome — especially from people running Gitea/Forgejo today.

---

> **LieTop7965**（1 分） · 2026-10-19T06:34:16+08:00　
> project name: kimo
>
> repo/website link: https://github.com/naman-sharma12345/kimo - https://getkimo.tech
>
> description: free, open-source (MIT) video editor with no GUI. it's meant to be driven by AI coding agents (Codex/Cursor/OpenCode-style) through an MCP client/transport you choose - the agent calls tool endpoints to cut, trim, set keyframes, add titles and captions, adjust colour grade, work with audio, and export. the agent can also ask kimo to render a single frame so it can check its own work before committing a timeline. it's a single ~15 MB CPU-only Rust binary, runs on a 2 GB box, no GPU needed. i built it while in college - it's early and a few edges are still rough (the captioning pipeline is the part i'm watching most closely). license is MIT and the repo can be forked. would really appreciate people trying it and telling me what breaks rather than me guessing.
>
> deployment:g.
>
> deploym repo can be forked. would really appreciate people trying it and telling me what breaks rather than me guessing.
> deployment: one binary, no dependencies beyond whatever the host has for running compiled code. grab the release from the GitHub repo and point your agent's MCP transport at it. i've been running it on a 2 GB VM with nothing else meaningful on the machine.
> AI Involvement: i used AI assistants while writing the rust (drafting modules, reviewing, and chasing compiler hints) and for bits of the MCP schema, but the architecture decisions, the tool-calling design, and the final integration are mine. you bring your own model via whatever MCP client you use — you choose the model.

---

> **meatball4802**（1 分） · 2026-10-19T08:42:35+08:00　
> Project Name: Printer Pal
>
> Repo/Website Link: [https://github.com/meatball4801/printer-pal](https://github.com/meatball4801/printer-pal)
>
> [https://meatball4801.com/apps/](https://meatball4801.com/apps/)
>
> [https://testflight.apple.com/join/xzWMyf4J](https://testflight.apple.com/join/xzWMyf4J) \- Printer-Pal
>
> Printer Pal Camera (for a spare iPhone/iPad): [https://testflight.apple.com/join/7pjeUe2D](https://testflight.apple.com/join/7pjeUe2D)
>
> Description:
>
> Printer Pal lets you watch your 3D printer from your iPhone or iPad, entirely on your own network. There's no account, no cloud, no subscription, and no server of mine involved; video goes straight from the camera to your phone over an encrypted connection.
>
> The problem it solves: most printer camera setups either depend on a vendor cloud, need port forwarding or a reverse proxy to view from a phone, or take over the camera your OctoPrint/Klipper Pi already uses.
>
> Features:
>
> \- Use a Raspberry Pi with a Pi camera or USB webcam, or share the camera an existing OctoPrint/Klipper (crowsnest, mjpg-streamer) setup already runs, without changing it.
>
> \- Or turn an old iPhone/iPad (iOS 15+) into the camera with the companion app.
>
> \- Pairing by QR code: each camera generates its own key and self-signed certificate, and the app pins that exact certificate. Only paired phones can view.
>
> \- The Pi companion only accepts connections from its attached local network (its own nftables table, UFW-aware) and never touches your router.
>
> \- Live view with zoom, full screen, rotation, snapshots, auto-reconnect, and a built-in connection check.
>
> \- Bambu Lab status through the Pi (progress, layers, temps, AMS) over the printer's local MQTT, read-only, no Bambu Cloud. (Experimental.)
>
> \- Optional remote viewing through your own Tailscale network; still no relay or third-party server from me.
>
> Deployment:
>
> \- iOS apps: free beta on TestFlight. Printer Pal: https://testflight.apple.com/join/xzWMyf4J. Printer Pal Camera (for a spare iPhone/iPad): https://testflight.apple.com/join/7pjeUe2D
>
> \- Pi companion: install with one command on Raspberry Pi OS or another Debian-based system with systemd (OctoPi and MainsailOS work):
>
>   curl -fsSL [https://github.com/meatball4801/printer-pal/releases/latest/download/install.sh](https://github.com/meatball4801/printer-pal/releases/latest/download/install.sh) | bash
>
>   It verifies the installer's checksum, detects your camera, sets up a systemd service, and shows a pairing QR. The app can also do the install for you over SSH. Update by re-running it; remove with "sudo print-monitor uninstall --confirm".
>
> \- No Docker image: the companion needs direct access to the camera hardware, systemd, and the host firewall, so it runs as a native service on the Pi. There's nothing else to host; the phone talks to the Pi directly.
>
> \- Docs: install guide, security notes, Bambu setup, and Tailscale guide in the repo (companion/README.md and friends), plus a tester guide (TESTING.md).
>
> AI Involvement:
>
> I used AI coding assistant (Claude) to help with part of writing and reviewing code. I designed the project, directed the work, and tested it on my own hardware (Pi 4, Pi Camera v2, Bambu A1, iPhone).

---

> **george_graves**（1 分） · 2026-10-19T09:28:58+08:00　
> Wait a second I thought you said you spent 4 years in school working on this but now you're saying that coated with AI jeez I'm I'm absolutely shocked

---

> **albert_wl**（1 分） · 2026-10-19T10:26:35+08:00　
> Thanks, glad you found a few new ones. Fair point on the colours, I'll take a look at the contrast. It's meant to be dark green on off-white, so which page looked burgundy to you? And were you using a dark mode extension or browser setting?

---

> **withmagi**（1 分） · 2026-10-19T10:56:06+08:00　
> **Project:** Uptime
>
> **Link:** https://justevery.com/uptime
>
> **Repo:** https://github.com/just-every/run-uptime
>
> **Description:** Uptime is a free, MIT-licensed monitor for websites and APIs. A single failed check never raises an alarm. It shows Degraded, then Failing only after an independent check confirms it, and a gap with no check shows as Unknown, never healthy.
>
> **Deployment:** Runs on your own computer or in your own Cloudflare account (a Worker, a D1 database and Cron). Locally: `npx -y @runeditrun/rer dev just-every/run-uptime`. It starts the app, a private runner and a practice target, makes you the owner and prints a sign-in link; keep that link private. The first start can take several minutes. A hosted install needs a mail provider (SendGrid, Resend or Cloudflare) with a verified sender.
>
> **AI involvement:** Coding agents write the code against a written product contract and tests. AI helped draft this comment.
>
> I'm James and I make Uptime at Just Every. A good first test: take the practice target down and watch Uptime count failed checks before it opens an incident.
>
> If you try it, which step in the first run needs a clearer explanation?

---

> **scubanarc**（1 分） · 2026-10-19T12:20:10+08:00　
> You caught me, I'm using Dark Reader!
>
> It looks fine if I disable the extension.

---

> **Dry_Truck3934**（1 分） · 2026-10-19T13:20:59+08:00　
> **Project Name**: Vaultiq
>
> **Repo/Website Link**: [https://github.com/rustiqz/Vaultiq](https://github.com/rustiqz/Vaultiq)
>
> **Description**: A zero-knowledge password manager I built for fun and for my own use. It has a Firefox/Chrome extension, an Android app, and an optional sync server you host yourself. The server only ever
> stores ciphertext, accounts are invite-only, and each device authenticates separately. There’s also a “never sync” local-only mode for people who don’t want a server at all.
>
> **Features so far**: autofill and a save prompt (including a real Android AutofillService), login/card/identity/authenticator/secure note items, TOTP codes, PIN and fingerprint unlock, encrypted backup and
> restore, and import from CSV, Bitwarden JSON and Proton Pass JSON. The crypto is Argon2id + XChaCha20-Poly1305 in one Rust core shared by every client.
>
> It’s early and not audited, so I’m not suggesting anyone put a real vault in it. What I’d like is feedback on the design and ideas for what to improve first. I’d also like to hear whether multi-user on one
> server is useful, or whether single-user is the normal case here.
>
> **Deployment**: There are no prebuilt downloads yet; I’m setting up CI/CD for releases. For now the server runs from the repo’s docker-compose.yml (Postgres, the Vaultiq server and Caddy), and the extension and
> Android app are built from source. The README has the steps, and there’s a longer guide in the guide/ folder. The first-run registration token is printed in the server logs, and an admin CLI handles
> invites and revoking devices.
>
> **AI Involvement**: A large share of the code was written with Claude Code. I directed the work: I set the project rules and scope, decided what to build and what to leave out (for example, no recovery or escrow flow and no breach checking), supplied the designs the apps follow, tested the Android app on a physical device, and approved every commit.

---

> **Electronic-Suit-5995**（1 分） · 2026-10-19T14:53:54+08:00　
> **Project Name:** AirDrop-LLM 📡🤖
>
> **Repo/Website Link:** [github.com/Mohit-jpg-dot/AirDrop-LLM](http://github.com/Mohit-jpg-dot/AirDrop-LLM)
>
> **Description:**
> I got completely tired of hitting the 16GB RAM wall on my laptop trying to run large AI coding models locally. The mainstream narrative is that you either have to buy a $4,000 workstation or pay monthly cloud API fees just to use smart developer models.
>
> I built AirDrop-LLM to bypass this completely. It is a zero-dependency, local-only system background daemon that lets you pool the RAM and GPU compute of whatever mismatched laptops you and your friends have lying around (like an M-series Mac and a Windows gaming rig) over a direct, offline smartphone hotspot network.
>
> Instead of forcing one machine to host a giant model, the system shards the model's weight layers sequentially across your devices. Your laptop processes the first chunk of the AI's logic, packages the intermediate data over high-speed networks, and your friend's graphics card handles the rest.
>
> * **No Disk Space? No Problem:** Massive models can take up over 500GB. AirDrop-LLM streams, caches, and executes just one single model layer group over the local air-mesh at a time, completely bypassing your physical hard drive storage boundaries.
> * **Drop-In IDE Gateway:** It exposes an offline reverse-proxy port (`http://localhost:9995/v1`) that completely emulates cloud API specifications. You can point Cursor, Aider, OpenHands, or [Continue.dev](http://Continue.dev) straight to it, type any random text into the API key field, and code fluidly inside your favorite editor using your combined hardware pool completely offline.
> * **Fault-Tolerant & Safe:** If a friend walks away and drops the Wi-Fi connection mid-sentence, it won't crash your project. The daemon automatically breaks the network loop and hot-swaps execution back to a tiny model running purely on your own laptop RAM to keep your coding velocity smooth.
> * **Cyberpunk TUI Dashboard:** Features a monochromatic retro management HUD that logs real-time ASCII memory matrices and peer link bandwidth diagnostics natively.
>
> **Deployment:**
> The application is fully released, open-source under the MIT license, and available to install globally via npm:
>
> bash
>
>     # One-click installation
>     npm install -g airdrop-llm
>
>     # Turn on the master core daemon
>     airdrop start
>
> Use code with caution.
>
> Full documentation detailing multi-node setup configurations, hardware synthesis recommender matrices, and editor connection paths is live directly on the repository landing page.
>
> **AI Involvement:**
> I used advanced LLM coding assistants to accelerate writing the low-level asynchronous network serialization layers, data compression routines, and local socket bindings in the background daemon.

---

> **Subject-Baseball-254**（1 分） · 2026-10-19T16:41:06+08:00　
> **L3T IPAM – a lightweight self-hosted IPAM for home networks (single container, JSON storage, optional read-only UniFi sync)**
>
> I needed a place to document IPs and hosts that is lighter than NetBox or phpIPAM, so I built one.
>
> * Address grid per network: static, reserved, DHCP lease, free, and with UniFi also online and undocumented devices
> * Overview with usage per network, next free address and an issues list (static IP in the DHCP range, duplicates, overlapping subnets …)
> * Optional UniFi sync, read-only, with a review step before anything is applied
> * Users and roles, built-in login with lockout and CSRF protection, meant for use behind a reverse proxy or Cloudflare Tunnel
> * English and German, dark mode, works on the phone
> * No database: plain JSON files and daily backups
> * One container for amd64 and arm64: `ghcr.io/l3t-io/ipam:2`. The log shows a one-time setup code for the first admin account
>
> Screenshots and a compose example are in the README: [https://github.com/l3t-io/ipam](https://github.com/l3t-io/ipam) (MIT) AI disclosure: written largely with Claude Code. I designed and tested it and run it at home. 135 automated tests are in the repo.
>
> Happy to hear what's missing.
>
> https://preview.redd.it/ct0729w8zdwh1.png?width=1416&format=png&auto=webp&s=73fc9640a917f098c48f97d24406a4189356f941

---

> **DemonPhoenix007**（1 分） · 2026-10-19T18:00:58+08:00　
> # A fully documented guide to a self-hosted media server setup.
>
> Hey everyone!
>
> I've been working on a **self-hosted automated media server**, and over time, I started documenting pretty much everything involved in setting it up, configuring it, maintaining it, and troubleshooting it.
>
> I've now organized all those notes into a GitHub repository, and I wanted to share it here in case it helps someone who's interested in getting into **homelabbing, self-hosting, Docker, or Linux system administration**.
>
> **GitHub Repository:** [https://github.com/Angadveer185/self-hosted-media-server](https://github.com/Angadveer185/self-hosted-media-server)
>
> # 🏠 What did I build?
>
> The project is a Docker-based media server running on Ubuntu, with several services working together to automate media management and provide a centralized media library.
>
> Here's a quick overview of the stack:
>
> * **Jellyfin:** Self-hosted media streaming and library management.
> * **Jellyseerr:** Media discovery and request management.
> * **Radarr:** Movie library management and automation.
> * **Sonarr:** TV series management and automation.
> * **Bazarr:** Subtitle management and automation.
> * **Prowlarr:** Centralized indexer management and integration with the media automation services.
> * **qBittorrent:** Download client.
> * **Gluetun + ProtonVPN:** VPN connectivity for services configured to use the VPN network.
> * **Portainer:** Web-based Docker container management.
> * **Cloudflare Tunnel:** Remote access to selected services without directly opening inbound ports on my router.
> * **Tailscale:** Private remote access to the server and SSH.
> * **Discord notifications:** Notifications from the different services to keep track of important events.
>
> Docker Compose brings the services together, while persistent configuration directories keep application data separate from the containers themselves.
>
> I also put together backup scripts and operational notes to make the setup easier to maintain.
>
> The goal was to build something functional, but also understand how the different pieces fit together instead of simply copying a Compose file and hoping everything works.
>
> # 📚 What's in the GitHub repository?
>
> I've organized the notes into sections covering the core setup, individual applications, networking, maintenance, and optional services.
>
> Some of the topics covered include:
>
> # 1. Core setup
>
> * Installing and setting up Docker on Ubuntu.
> * Understanding Docker containers, networks, volumes, and Compose.
> * Organizing configuration files, downloads, and media directories.
> * Managing persistent application data.
>
> # 2. Media automation
>
> * Installing and configuring Prowlarr.
> * Connecting Radarr and Sonarr to the download client.
> * Configuring qBittorrent.
> * Setting up Bazarr for subtitle management.
> * Connecting Jellyfin and Jellyseerr.
> * Understanding how the different services communicate with one another.
>
> # 3. Networking and remote access
>
> * Configuring Gluetun with ProtonVPN.
> * Understanding how VPN networking affects containers.
> * Setting up Cloudflare Tunnel for selected remote-access use cases.
> * Using Tailscale for private access and SSH.
> * Understanding Docker service names, internal ports, and network connectivity.
>
> # 4. Backups and maintenance
>
> * Organizing server configuration backups.
> * Creating and managing backup archives.
> * Automating backups and retaining a limited number of recent copies.
> * Using Docker Compose to manage services.
> * Checking container health, inspecting logs, and troubleshooting common problems.
>
> # 5. Notifications and operational details
>
> * Configuring Discord notifications across the supported applications.
> * Keeping track of important events.
> * Documenting useful Linux and Docker commands for everyday administration.
>
> I've tried to make the documentation structured and reusable, so it can serve as a reference rather than a one-time installation guide.
>
> # 🎯 Why did I document everything?
>
> When you're starting out with self-hosting, it's easy to find individual tutorials for individual applications.
>
> The difficult part is often understanding how everything connects.
>
> Why can't one container reach another? Why does a download client work on its own but fail when connected through a VPN? Why do paths need to match across multiple containers? What happens when a container is recreated? How do you back up the configuration so you don't have to rebuild everything from scratch?
>
> These are the kinds of questions that make a multi-service setup challenging, especially when you're still learning Linux, Docker, networking, and system administration.
>
> I wanted to turn what I learned into something organized that I could refer back to myself and that other people could learn from too.
>
> This is also a way for me to keep improving the setup instead of letting it become an undocumented collection of containers.
>
> # 👨‍💻 Who might find this useful?
>
> I think this repository could be useful if you're:
>
> * Completely new to homelabbing or self-hosting.
> * Learning Docker and Docker Compose.
> * Experimenting with Linux server administration.
> * Trying to build your own media server.
> * Curious about VPN networking, private remote access, and service integration.
> * Looking for examples of how to organize a multi-container project.
> * Building your own setup and wanting a reference for troubleshooting and maintenance.
>
> You don't need to reproduce my entire setup. You can use the documentation to understand individual services and adapt the relevant parts to your own environment.
>
> # 💬 Feedback is welcome!
>
> This is a personal project, and I'm still learning. There are always better ways to organize things, improve security, simplify configurations, or make documentation clearer.
>
> If you take a look, I'd genuinely appreciate feedback, corrections, and suggestions for improvements.
>
> If you're just starting out, I hope it helps you avoid a few of the rabbit holes I went down along the way.
>
> **Repository:** [https://github.com/Angadveer185/self-hosted-media-server](https://github.com/Angadveer185/self-hosted-media-server)
>
> Thanks for reading, and happy homelabbing! 🐧

---

> **Arancool3000**（1 分） · 2026-10-19T20:51:14+08:00　
> **Project Name:** Kevin
>
> **Repo:** https://github.com/arancool3000/kevin-assistant (MIT)
>
> **Description:** A voice assistant for the Raspberry Pi that you extend by talking to it. Wire up an LED, a relay or a sensor, say "Hey Kevin, I've connected an LED to GPIO 17, make a skill that turns it on and off", and it writes the skill. The settings page shows the exact code (or a diff) and what it can reach before anything installs, and approval is tied to that code by a hash. Each skill can be switched off or rolled back on its own.
>
> **Deployment:** Runs on your own Pi 5 (or Pi 4, 2 GB+) with a USB speakerphone. One-line installer on Pi OS Lite, or a Windows app that writes the SD card for you. Docs in the repo. No Docker image yet. To be upfront for this sub: the wake word runs locally, but the conversation itself uses Google's Gemini Live API, so it isn't fully offline.
>
> **AI Involvement:** Built with a lot of help from AI coding tools, and the conversation side is an LLM. Feedback on the install from fresh Pis is what I need most.

---

> **andypalmi**（1 分） · 2026-10-19T22:07:12+08:00　
> **amicu: Terraform for your own LLMs, on your own hardware**
>
> Open-source CLI for self-hosting LLMs as code. Describe the model, hardware and runtime in one HCL file:
>
> \- plan checks it fits in memory
>
> \- apply runs it as a background service with an OpenAI-compatible endpoint
>
> \- destroy cleans up
>
> macOS, Linux, Windows (llama.cpp; vLLM on Linux GPUs). Can also move the same deployment to Modal or RunPod, but nothing leaves your machine unless you choose that. Single Rust binary, AGPL-3.0. Early, feedback welcome.
>
> Repo: [https://github.com/andypalmi/amicu](https://github.com/andypalmi/amicu)
>
> Docs and install: [https://amicu.dev](https://amicu.dev)
>
> https://preview.redd.it/rk057ghdlfwh1.png?width=1920&format=png&auto=webp&s=f48404ca5346eaa13dbba791ed4db7c7a64c5724

---

> **Anshu6666**（1 分） · 2026-10-19T22:28:39+08:00　
> **Project Name:** DeepTrade
>
> **Repo/Website Link:** https://github.com/Anshu666666/deepTrade
>
> **Description:** A conversational market research + broker execution assistant for Indian markets (Upstox). You chat with a Telegram bot: the agent runs deep research (Exa for live web/news, Valyu for filings and earnings transcripts), writes a structured analysis, then drafts the order with live LTP. Nothing executes until you tap Confirm - the LLM never has execution authority over real money. It solves the juggling problem (broker app + news sites + terminal in 4 tabs) while keeping a hard human-in-the-loop gate.
>
> **Deployment:** Python 3.10+, FastAPI, aiogram, Postgres for checkpoints. Clone, pip install -r requirements.txt, configure .env (guide in setup_instructions.md), python main.py. You bring your own Upstox app credentials, Telegram bot token and OpenRouter key. No Docker yet - that is the biggest gap and is on the roadmap. Sandbox mode gives a 10 lakh INR paper ledger on live prices so you can try it without risking money.
>
> **AI Involvement:** Transparent: an LLM (model-agnostic via OpenRouter) running as a DeepAgents/LangGraph supervisor does the research synthesis and order drafting. Every action is gated behind an explicit confirmation button, secrets stay in encrypted local SQLite on your machine, and the code is MIT licensed. Built with heavy AI coding assistance, reviewed and architected by me.

---

> **Mother-Side6477**（1 分） · 2026-10-19T23:31:11+08:00　
> # OneMemory – self-hosted shared memory for all your AI agents (Docker one-liner)
>
> Hey all, I'm the builder. I made OneMemoryMCP because I was running multiple AI coding agents and they neveer knew what eachother was doing. Also my Mobile version never knew what I just started creating on my PC. So I started cooking this up. I made it with Claude and Muse
>
> What it is: a self-hosted memory server (MCP) that any agent can read/write. Spin it up with:
>
> docker run -d -p 3000:3000 calasdan/onememory. [https://github.com/calasdan-sketch/onememory](https://github.com/calasdan-sketch/onememory)
>
> Features:
>
> \- Namespaces per project/agent
>
> \- Scoped tokens (read/write/admin per namespace)
>
> \- Revisions + backup export/import
>
> \- Injection-on-read guard
>
> \- Web dashboard + CLI
>
> It's MIT licensed, 491 tests passing. The skill is also listed on Agensi if you want the plug-and-play version.
>
> Happy to answer questions...what would make this actually useful in your mix? Anything I can do to improve it?

---

> **jeffyclassify**（1 分） · 2026-10-20T00:14:01+08:00　
> https://preview.redd.it/r7xgmjly7gwh1.png?width=1200&format=png&auto=webp&s=517f63ccd6c236214369a3d21467c17f698d8cc6
>
> **Project Name**: Jeffy
>
> **Repo/Website Link**: [https://github.com/nicobrenner/jeffy](https://github.com/nicobrenner/jeffy)
>
> **Description**: Open-source text classifiers that run on CPU. 70 pretrained tasks (sentiment, spam, intent, topics, toxicity, etc), \~15ms per classification, deterministic output. Also has 51 multilingual classifiers covering 51 languages. No GPU, no external API calls, no signup needed. Just **shipped an n8n community node** too, so you can replace the default Text Classifier node: [https://jeffyclassify.com/blog/n8n-jeffy/](https://jeffyclassify.com/blog/n8n-jeffy/)
>
> **Deployment**: pip install jeffy-classify && jeffy serve --port 8400. That's it. Runs on any machine with Python 3.10+. No Docker image yet but it's a single pip install with no external dependencies beyond PyTorch
>
> **AI Involvement**: The classifier training code and benchmarks were developed with Claude. The blog post and landing page were built with Claude Code. The core architecture (BGE-large embeddings + logistic regression) and all training data are open source

---

> **tyommik**（1 分） · 2026-10-20T00:21:44+08:00　
> https://preview.redd.it/45pgwrix8gwh1.png?width=1280&format=png&auto=webp&s=2c8c7157101b5b6243da7b47e7ed3f9085600ffe
>
> **Project Name: Glosano**
>
> **Repo/Website Link**: [https://github.com/Glosano/glosano](https://github.com/Glosano/glosano) (MIT)
>
> **Description:**
>  A self-hosted, LingQ-style app for learning languages by reading content you actually want to read. Import \`.txt\` / \`.md\` files, YouTube videos with captions in the language you learn, or web pages via a Chrome/Firefox extension. In the interactive reader every word is coloured by how well you know it; click one for a Wiktionary definition, grammar tags and an optional in-context AI translation. Save words and phrases and review them with spaced repetition. It solves the "years of my vocabulary live in someone else's subscription service" problem: your library, vocabulary and progress stay on your server.
>
> \- 10 learning languages (EN, RU, PT, ES, FR, DE, Simplified Chinese, JA, AR, HI), interface in 9.
>
> \- Multi-user: one instance for a family or a small group, private or shared lessons.
>
> \- Wiktionary dictionaries (Kaikki.org, CC-BY-SA) imported into your own Postgres, lookups stay local.
>
> \- AI is optional: in-context translation and a chat about the paragraphs you're reading, through any OpenAI-compatible endpoint, including local Ollama / LM Studio / vLLM. Everything else works without it. No telemetry.
>
> \- JSON export and account deletion for every user.
>
> **Deployment:** Docker Compose (app, worker, Postgres, Redis), 1 vCPU / 2 GB RAM minimum. There's no prebuilt image yet: you clone the repo and run \`docker compose build\`, which takes a few minutes. The self-hosting guide walks from an empty Linux server to an HTTPS instance in about 30 minutes, covering Caddy/nginx, the first admin, dictionaries, AI providers, updates and backups: https://github.com/Glosano/glosano/blob/main/docs/self-hosting.md. It's an MVP: no admin panel yet (CLI instead), desktop browser first.
>
> **AI Involvement**: The code was written with use of AI coding assistants under my direction. I wrote the product spec and every product and architecture decision, and reviewed and tested the changes; the backend and frontend have automated test suites. Inside the app, AI is used only for optional features: in-context translation and a chat about the text you're reading. Both disappear when AI is turned off.
>
> Feedback on the install guide is very welcome!

---

> **RammerOfProgs**（1 分） · 2026-10-20T00:51:53+08:00　
> I’ve spent the last year or so building Magpie, a self-hosted platform for acquiring and managing movies, TV, music, and books in one place. I started it to address my frustrations with the \*arr suite.
>
> A few things that make it different:
>
> * Multiple deployment options, including multi-node clusters, Docker/Kubernetes, Windows services, and systemd, with support for SQLite, PostgreSQL, and SQL Server.
> * Multiple accounts with RBAC. You can give friends and family a limited login so they can browse and add content, or more permissions to manage and administer the server.
> * Mobile-friendly out of the box, with a responsive layout, an installable PWA, and support for multiple themes.
> * Very extensible. Most features ship as plugins, with the ability to add even more functionality, including new content types and third-party integrations.
> * Extensive telemetry can be captured via OpenTelemetry (OTEL).
> * Acquisition logic is totally different from the \*arr tools. Stuck downloads, stale downloads, and random unexplained failures have always been some of my biggest frustrations. After running Magpie as my \*arr replacement for months with fairly high activity, I can confidently say those frustrations have been addressed for me.
>
> Current integrations include Jellyfin, qBittorrent, and Cardigann, along with metadata providers TMDb, TVmaze, MusicBrainz, Open Library, and Wikidata. I’m adding more integrations, and I also plan to release an \*arr migration tool soon.
>
> On AI involvement: most of the core was built without any AI at all. I’ve slowly adopted AI tooling into my workflows over the last year. On Magpie, it’s mostly been for adding new plugins, helping with front-end code, and unit tests and docs. More details are in my [AI disclosure](https://github.com/magpie-media-platform/magpie/blob/develop/AI_POLICY.md#ai-is-welcome-here).
>
> I’d love for people to give it a try and tell me what works, what doesn’t, and what’s missing.
>
> [GitHub](https://github.com/magpie-media-platform/magpie)
> [Installation guides](https://github.com/magpie-media-platform/magpie/blob/develop/docs/installation/README.md) · [Quick start](https://github.com/magpie-media-platform/magpie/blob/develop/docs/quick-start.md)

---

> **dasimers**（1 分） · 2026-10-20T01:01:53+08:00　
> As my kid gets older this is going to be invaluable for making sure she doesn't watch things out of scope of her age. Great job!

---

> **lwh-x**（1 分） · 2026-10-20T01:16:47+08:00　
> https://preview.redd.it/c86ynn49jgwh1.png?width=1280&format=png&auto=webp&s=8991fe19b2b3679ded4cc89e6b85a8192b323389
>
> Project Name: Tessera
>
> Repo/Website Link: [https://github.com/Limatura/tessera](https://github.com/Limatura/tessera)
>
> Docs: [https://tessera-docs-three.vercel.app](https://tessera-docs-three.vercel.app)
>
> Description:
>
> Tessera is a file and note sharing server that cleans up after itself. You upload a file, folder, code snippet or link, get a short code and a URL back, and the share is deleted once it expires or has been downloaded as many times as you allowed. Sending doesn't need an account unless you want that.
>
> We used FileCodeBox before this. It's built around anonymous pickup codes, and we kept wanting things it didn't have when we looked: syntax highlighting and previews for code, images, SVG and Mermaid, user accounts with roles and quotas, OIDC login, uploads that go straight to an S3 bucket, and encrypting on the client. So we wrote our own. We use it every day, so it will keep getting fixed.
>
> What's different:
>
> \- accounts are optional, but there if you want them: invite-only or closed sign-up, OIDC, GitHub, Discord, roles, per-account quotas
>
> \- with S3/GCS, uploads go straight to the bucket and plain downloads are redirected there, so big files never pass through your server
>
> \- SQLite, PostgreSQL or MySQL, so it can run on more than one machine
>
> \- storage: local disk, S3-compatible, Azure Blob, GCS, WebDAV. Add several from the admin panel, no restart
>
> \- CLI: \`tessera send report.pdf --expires 24\`, and --encrypt seals the file on your machine. The key lives after the # in the link, so the server never sees it
>
> \- syntax highlighting, image/SVG/Mermaid previews, link preview cards in chat apps
>
> \- optional malware scanning on upload
>
> \- one-time shares are counted in a single conditional DB update, so two people racing for the same share can't both get it
>
> \- OpenAPI spec generated from the server code and checked in CI
>
> Also: expiry, download limits, passwords, folders as one archive, UI in English, Traditional Chinese and Japanese.
>
> It's a single Rust binary and it streams uploads and downloads, so memory use doesn't grow with file size.
>
> Rough edges: it's v0.1.0-rc.1, so not 1.0 yet. The GCS backend has no tests. WebDAV only handles small files. Anonymous uploads are on by default, so read the public example config before you put it on the internet. Back up your database before upgrading, downgrades aren't supported.
>
> Deployment:
>
> Docker image: [ghcr.io/limatura/tessera:latest](http://ghcr.io/limatura/tessera:latest)
>
> Or clone the repo and run \`docker compose up -d\`, then open port 12923. The admin password is printed once in the log: \`docker compose logs tessera | grep password\`
>
> There are example env files for a personal and a public instance, and a systemd unit file.
>
> AI Involvement:
>
> We wrote this post ourselves. AI only proofread it, because English isn't our first language. The code was written with AI tools; a human decides the architecture, reviews the code and does the testing. The agent config files are in the repo (AGENTS.md, .claude/, .codex/) if you want to see how. The app itself doesn't use any AI.
>
> Feedback and issues are welcome, especially what's missing compared to what you use now.

---

> **Andrii_Dre**（1 分） · 2026-10-20T01:36:34+08:00　
> **health-os** — self-hosted personal health record that AI assistants can query through guarded tools
>
> - **What:** labs (PDF/photo), Garmin, Apple Health, home blood pressure, a food log with 41 nutrients, meds and diagnoses in one Postgres database on your machine. Any MCP client (local model or cloud assistant) reads and updates it through a fixed set of tools.
> - **Why it's different:** extracted values wait in a review queue until you approve them; critical lab values and safety checks are plain code with tests, not model judgement; the AI reads approved data through a read-only DB login.
> - **Try it:** a demo with a fictional patient, `cd demo && docker compose up -d --build`
> - **License:** AGPL-3.0
> - **Repo:** https://github.com/andronaft/health-os
>
> It's young (first public release end of September), so I'm mostly after feedback: which imports would you need (Withings, Oura, Health Connect, FHIR exports)? How do you get phone data into a self-hosted DB without a cloud in between? What would stop you from running it?

---

> **Colo3D**（1 分） · 2026-10-20T01:47:54+08:00　
> **Project Name:** Scriptorium
>
> https://preview.redd.it/m3f97xdnogwh1.png?width=2400&format=png&auto=webp&s=eca7365788c04be93207679d8f9be8ec9f39cd00
>
> **Repo:** [https://github.com/MrColoo/scriptorium-library](https://github.com/MrColoo/scriptorium-library)
>
> **Description:**
>
> **A self-hosted ebook library that tends itself, and that you actually enjoy opening.**
>
> Drop a book into a folder. Scriptorium imports it, converts it (KEPUB for Kobo, EPUB for everything else), fetches cover and metadata, catches duplicates, fixes EPUBs that Send-to-Kindle would reject, and puts it on your Kobo by the next sync. You don’t touch Calibre and you don’t plug in a cable.
>
> It’s built on [Calibre-Web-Automated](https://github.com/crocodilestick/Calibre-Web-Automated), whose automation is excellent. What bothered me was the interface, so I rebuilt the whole front end page by page:
>
> * **Kobo-first**: guided sync setup, shelves become Kobo collections, and a *Continue reading* row on the home page shows your progress and the time left in each book, fed by your device
> * **Personal styles**: every user can give the library their own look, with 11 ready-made themes, a “Surprise me” button or a hand-tuned palette with a live preview. The default stays clean and neutral
> * **Built for phones**: a real mobile layout with bottom navigation, not a shrunken desktop
> * **New readers**: EPUB with themes and typography settings, comics, PDF and text, plus an audiobook player that remembers where you stopped
> * **Hardened**: strict Content-Security-Policy with no inline scripts, CSRF on every action, a forced password change on first login, and regression tests for the fixes
> * KOReader sync, OPDS, email to eReader, multi-user with LDAP/OAuth/OIDC, smart shelves, 28 languages
>
> **Already running CWA?** It’s an image swap. Same data, same volumes, same env vars, no database changes, and you can switch back.
>
> **Deployment:**
>
>     mkdir scriptorium && cd scriptorium
>     curl -O https://raw.githubusercontent.com/MrColoo/scriptorium-library/main/docker-compose.yml
>     docker compose up -d
>
> Open `:8083` and log in with `admin` / `admin123`; it makes you pick a new password right away. The image is on GHCR (amd64 and arm64). Docs for Kobo, KOReader, reverse proxies and NFS/SMB are in the repo.
>
> **AI Involvement:** Most of the new front end (templates, CSS, JS), the docs and the tests were written with an AI coding assistant (Claude Code), with me directing the design, reviewing the changes and testing everything on my own library and Kobo. The backend, which does the automation and sync, is Calibre-Web-Automated’s, and I kept it as close to upstream as possible so fixes can flow both ways. Feedback, bug reports and PRs are very welcome.

---

> **cosmic_m0nkey**（1 分） · 2026-10-20T03:48:10+08:00　
> glad you liked it :) if you miss any feature let me know!

---

> **Unreal_Menace**（0 分） · 2026-10-20T03:54:15+08:00　
> **Project Name:** Tsuzuki
>
> **Repo/Website Link:** [https://tsuzukiapp.com](https://tsuzukiapp.com) (closed-source for now)
>
> **Description:**
>
> I read web novels daily, and on iPhone that meant a pile of browser tabs and losing my place whenever a site went down. So I built Tsuzuki, a reader that keeps it all in one library.
>
> * Reads Calibre, Kavita, Komga or any OPDS server, at home by IP or remotely over https
> * Password-protected servers work (Basic and Digest), with the password kept in the iOS Keychain
> * Offline downloads, EPUB import, free Gutenberg and Standard Ebooks catalogs
> * No account, no analytics, optional Face ID lock
>
> **Deployment:** iPhone app, nothing to host. Point it at your OPDS address. Public beta: [https://testflight.apple.com/join/UY1zBs2J](https://testflight.apple.com/join/UY1zBs2J). Setup help: [https://tsuzukiapp.com/help/](https://tsuzukiapp.com/help/)
>
> **AI Involvement:** Most of the code was written with Claude Code. I set the design and rules in a written decision log, reviewed every change, and tested each feature on my own iPhone. It also went through a full code audit before the beta.
>
> Feedback welcome, especially from Calibre-with-password, Calibre-Web and Komga users.

---

> **Register_Defiant**（1 分） · 2026-10-20T04:08:57+08:00　
> I recently worked on **Noema**, an open-source, self-hosted productivity workspace designed to bring notes, documents, databases, and project management together in one place.
>
> The idea is to create a flexible workspace where users can manage their work while maintaining control over their own data.
>
> 🔥 **Some of its main features:**
>
> * 📝 Rich-text document editing with blocks, tables, equations, and more
> * 🗃️ Databases with 7 views: Table, Board, List, Gallery, Calendar, Timeline, and Chart
> * 📊 Project management with tickets, milestones, and sprint tracking
> * 🤖 AI-powered writing, summarization, and workspace Q&A
> * 🤝 Collaboration features, including comments, sharing, and permissions
> * 🖥️ Web app and installable Windows desktop app
> * 🔐 Self-hosting for greater control over your data
>
> 🛠️ **Tech stack:** Next.js, React, TypeScript, Tailwind CSS, Prisma, PostgreSQL, TipTap, and Tauri.
>
> The project is open source under the MIT license, and it was built in just **4 days with the help of AI-assisted development using OpenCode**.
>
> 🔗 GitHub: [https://github.com/Guembri01/noema](https://github.com/Guembri01/noema)
>
> This was an interesting experiment in rapid development and exploring how AI coding tools can help bring a project to life.
>
> I'm sharing it here to get some honest feedback from the community.
>
> **What do you think about building full-featured applications with AI coding tools? And what would you build in 4 days?**
>
> I'd love to hear your thoughts! 🚀
>
> https://preview.redd.it/7bsaqp9zdhwh1.png?width=1920&format=png&auto=webp&s=0c1d02226fb67659c91b33df56c866fb0884ed94

---

> **luisalcaraz_telara**（1 分） · 2026-10-20T04:25:10+08:00　
> **Project:** TAP Runtime, built at Telara. This is an update to the local agent tool runtime I shared in an earlier project megathread.
>
> **Repository and license:** https://github.com/Telara-Labs/TAP-Runtime (MIT)
>
> **What's new:** Saved primitives can call other primitives pinned by version and digest, and each child runs with its own access declarations and approvals. There are now Go, C++ and Rust examples next to Bash, Python, JavaScript and TypeScript, and the runner supports WASI components.
>
> **Installation:** `npm install -g @telaralabs/tap`, then `tap setup`. npm now downloads only the runner for your platform, about 13 MB. Old interpreter and compiled caches get cleaned up automatically, and `tap cache prune` clears them on demand.
>
> **What runs locally and what reaches out:** The runtime, your primitives and history discovery all run on your machine, with no Telara account or registry involved. Tool calls use whatever provider connections they're bound to. Interpreters download the first time they're used, and WASI Preview 3 downloads a pinned official wasmtime build when a package needs it. Docker Sandbox Kit export writes config files only.
>
> **Client support:** Claude Code and Codex CLI are the supported paths. The README lists the others.
>
> **Affiliation and AI involvement:** I work on TAP at Telara. We use AI assistance in development and used it drafting this post. People review the code and packages they run.

---

> **frivensolutions**（3 分） · 2026-10-20T05:41:34+08:00　
> **Project**: Simple IPTV Manager
>
> **Website**: [https://github.com/FrivenSolutions/simple-iptv-manager](https://github.com/FrivenSolutions/simple-iptv-manager)
>
> **Description**:
>
> * Cost.  Free.
> * Output.  Outputs one or more M3U, XML, XStream for one or multiple users.
> * Simple filtering.  Easily includes or exclude based off starts with, ends with, contains, regex criteria.  See the results live of the filters.  Override any category you want.  Provider changes categories, the filter criteria gets applied every update.
> * Sources.  Multiple inputs including HDHomeRun tuners
> * Local tuner.  Parsing EPG from HDHomeRun, no need for an external EPG and channel mapping required
> * Cleaning up.  Tidy up channel names, group names, add suffix or prefix to provider categories
> * Remove empty channels.  Hide channels that don't have events based off channel name or guide, completely customizable at the top level or in each category.  For example, if the guide is, "No Event Today" or "Offline", that channel can be hidden from the playlist.
> * Movies and series.  Filter just like channels
> * Stream modes.  Stream as direct, redirect or proxy.  Proxy allows users to see what users are streaming what channels on dashboard.
> * Watch channels in browser.
> * Jellyfin support.  Jellyfin supports categories, e.g. Sports, News, Movies, which the app can assign to a category.
> * Password protected, two factor authentication, Homepage widget compatible, backup and restore
> * Lightweight Node.js with SQLite and no external database.  Install with Docker or Proxmox.
>
> **Deployment**: Docker and Proxmox instructions on the site readme
>
> **AI Involvement**: Written with significant help from Claude Code.  Been small group testing with success.

---

> **PinGUY**（0 分） · 2026-10-20T06:01:53+08:00　
> I've been building something called **Rhizome Stack** for my own use and finally got it into a state where other people can actually poke at it.
>
> GitHub: [https://github.com/pinguy/rhizome-stack](https://github.com/pinguy/rhizome-stack)
>
> The basic idea is fairly simple: I wanted one local AI environment rather than half a dozen separate tools that don't really know about each other.
>
> Rhizome uses **OpenClaw as the agent/orchestration layer and Open WebUI as the front end**, then adds the glue around them for things like memory, skills, retrieval, speech, code execution and local media generation.
>
> The part that ended up taking most of the work wasn't getting any individual model running. That bit is relatively easy now. It was making the whole lot behave like **one system**.
>
> For example, my main GPU only has so much VRAM. If I'm chatting with a local model and then ask it to generate an image, music or video, Rhizome can hand the GPU over rather than expecting everything to live in VRAM simultaneously:
>
> **chat model → unload → start ComfyUI/backend → generate → attach result directly into the Open WebUI conversation → free backend → resume chat**
>
> So an ordinary chat can generate a Qwen image, MiniMax song or WAN video and keep the PNG/MP3/MP4 as part of the saved conversation.
>
> Other optional bits currently include:
>
> - semantic memory / importing documents and chat history
> - agent skills
> - Chatterbox-Nano TTS + faster-whisper STT
> - Podman-backed Jupyter/code interpreter
> - MiniLM retrieval
> - GLiNER + a bounded local worker
> - Qwen image generation/editing
> - MiniMax Music 3
> - WAN text/image-to-video
> - local Ollama models or hosted providers
>
> It's **local-first rather than local-only**. I wanted to be able to swap models and services without rebuilding the rest of the system around whichever model happens to be fashionable this month.
>
> It's also very deliberately owner-operated. Credentials, chats, memory, voice references and model weights aren't baked into releases, and the installer has dry-run paths rather than silently doing a load of magic behind your back.
>
> Current status is **0.1.0-alpha.15 candidate**. The release exporter currently produces a verified **227-file manifest**, with automated regression, privacy and checksum checks. The last round fixed the remaining findings from an independent audit.
>
> **It is still alpha.** Clean native Linux/WSL2 installs and some live GPU/Open WebUI paths still need wider acceptance testing, so I wouldn't stick it on a machine you absolutely cannot afford to tinker with. The known limitations are documented in the repo.
>
> One other thing worth being transparent about: this has been built with **heavy AI-assisted development**. I do the architecture, requirements, testing, integration and the final calls; agents now do a fair chunk of the implementation work. That's actually part of why the project exists — I've been interested in what happens when the AI environment you're building can increasingly help build and maintain itself.
>
> I'm running it because I actually wanted this setup, rather than because I was trying to create another "one-click AI platform".
>
> If anyone here is running a similar local stack, particularly on constrained hardware, I'd be interested in what you've done differently and where you think I've made bad assumptions.
>
> **Repo:** [https://github.com/pinguy/rhizome-stack](https://github.com/pinguy/rhizome-stack)

---

> **TheGreatWooSini**（1 分） · 2026-10-20T09:22:07+08:00　
> * **Project Name:** WooSarr (or WoosArr)
> * **Repo/Website Link:** [https://github.com/WoosArr/woosarr](https://github.com/WoosArr/woosarr)
> * **Description:** WooSarr (or WoosArr) (no affiliation with the \*Arr apps we know and love) is a Plex user library management system, and Discord bot.
>
> You can manage user libraries manually through the web interface (Mass adding of libraries to users!!), or use Discord roles to manage library access dynamically.  WooSarr can create the roles or use existing roles (such as ones used by a Patreon integration or other role management bots).
>
> It also has an invite to plex feature, to streamline the Discord -> Plex workflow.
>
> Finally, it has a Discord /request command pipeline to Seerr, because I was already linking Plex accounts, and quite literally my Requestrr server fell down as I was building this, and the current Requestrr is the 3rd repo I've had to deal with for a request bot, I said, "Why the heck not?" (Sorry VaultRequestrr, I didn't know you existed until later.  You look excellent.) This integration uses your Discord->Plex linked accounts to identify who requested a show or movie.
>
> * **Deployment:** It's built for Docker and UnRAID deployment
> * **AI Involvement:** It's 100% vibe-coded, so if you hate that, don't use it. I'm not a web dev. And I definitely couldn't have built this for the $2 that it cost**.**
>
> https://preview.redd.it/lv3ioepmxiwh1.png?width=1440&format=png&auto=webp&s=0e8a947fd32785bf2c384bcfb5d363298537856b

---

> **Cold-Conclusion-6511**（1 分） · 2026-10-20T09:32:18+08:00　
> **Spanlight**: open-source LLM observability on one Postgres.
>
> **Website**: [https://spanlight.dev](https://spanlight.dev/)
>
> Records every LLM call your app makes (prompt, reply, latency, tokens, cost, errors), grouped into traces and sessions. One Docker image plus one Postgres database, nothing else to run. Core is MIT.
>
> * Trace explorer, sessions as a chat, cost per call from a versioned price table. An unknown price shows as unknown, never $0.
> * Daily check against the provider's bill (needs an Anthropic or OpenAI admin key, or a CSV).
> * Budgets that alert, or block gateway calls (checked every 60 seconds, so a soft limit).
> * The Doctor: 15 fixed rules that flag retry storms, truncated outputs, tool loops, cost and latency spikes and more, with evidence and a fix. The rules use no language model.
> * Optional gateway: change your OpenAI or Anthropic client's `base_url`; adds retries, fallbacks, rate limits and a cache. Needs your provider key stored in Spanlight.
> * Ways in: Python SDK (PyPI 0.2.1) or any OpenTelemetry exporter over OTLP/HTTP.
>
> Try it:
>
>     git clone https://github.com/dheerajkarwasra/spanlight.git
>     cd spanlight
>     cp deploy/.env.example deploy/.env    # fill in POSTGRES_PASSWORD, APP_DB_PASSWORD and SECRET_KEY
>     docker compose -f deploy/compose.yaml --env-file deploy/.env up -d
>
> Then open [http://localhost:8080](http://localhost:8080/)
> Docs: [https://spanlight.dev/docs/](https://spanlight.dev/docs/)
>
> **AI involvement:** I’m a solo developer. I designed the architecture and review and test every change; I used Claude Code to write the code.
>
> Please try it and tell me what you liked, what you disliked, what was confusing, what broke, and what is missing for your use case. GitHub Issues and Discussions are both welcome. Every report gets a reply.
>
> Repo: [https://github.com/dheerajkarwasra/spanlight](https://github.com/dheerajkarwasra/spanlight)

---

> **Temporary-Career-360**（1 分） · 2026-10-20T13:57:24+08:00　
> Marchand Studio
>
> One desktop app for local and cloud AI: chat, a coding agent, image generation, and a built-in school that trains your own local AI using Claude, Grok or any model as the teacher. Works on AMD and NVIDIA. Free for non-commercial use.
>
> Repo and installer: [https://github.com/ilusixn/Marchand/releases/tag/v0.1.0](https://github.com/ilusixn/Marchand/releases/tag/v0.1.0)
>
> https://preview.redd.it/fvqxnfuyakwh1.png?width=1920&format=png&auto=webp&s=953b03c76bd7f680fc0dd6a3cc4a2cd4b9d844a8

---

> **hackslashX**（1 分） · 2026-10-20T18:54:52+08:00　
> **Project Name:** Fanoos
>
> **Repo/Website Link:** [https://github.com/hcx-labs/fanoos](https://github.com/hcx-labs/fanoos)
>
> **Description:**
>
> * Fanoos is a self-hosted video client that puts your YouTube subscriptions and your Crunchyroll watchlist in one chronological feed. There are no recommendations, no ads and no tracking. It's for people who want to keep up with the channels and shows they follow without the algorithm, and without Google seeing what they watch.
> * One merged feed from every linked account, across services. You can link several YouTube and Crunchyroll accounts.
> * YouTube is watched signed out through your own server. Video, thumbnails and avatars are all proxied, so your browser never contacts Google. It includes SponsorBlock, Return YouTube Dislike and DeArrow, and the player can stream H.264, VP9 or AV1.
> * Crunchyroll (optional, needs Premium): DRM playback in your own browser, with every dub, styled subtitles and intro skipping. It uses an unofficial API, which is against Crunchyroll's terms, so use it at your own risk with your own account.
> * Your own Fanoos account: passkeys, password or OIDC single sign-on (Authentik, Keycloak, Authelia and others). History, positions, Watch later and preferences sync across devices.
> * Extras: continue watching across services, a release calendar, watch-time analytics, and light and dark themes.
>
> **Deployment:**
>
> * Docker images for linux/amd64 and linux/arm64 are published to GHCR: fanoos-core, fanoos-youtube and fanoos-crunchyroll.
> * A compose.yaml and compose.env.example are in the repo. Copy the env file, fill in the secrets and Google OAuth details, then run docker compose up -d.
> * The README covers setup, Google OAuth configuration, OIDC, and what to do if YouTube blocks your VPS's IP address (routing through Control D or a proxy).
> * It can also run without Docker (Node 24, Deno, Redis) with npm run dev.
> * License: AGPL-3.0.
>
> **AI Involvement:**
>
> Fanoos was built with heavy use of Claude Code. Most of the code was written by AI under my direction, then reviewed and tested by me. Please keep that in mind when deciding whether to run it.
>
> https://preview.redd.it/uye4l28vrlwh1.png?width=2880&format=png&auto=webp&s=94fbe78d842c45bcb2adb8d4d135f65a581f6fff

---

> **milankowww**（1 分） · 2026-10-20T19:01:18+08:00　
> **Project Name:** MailIntel
>
> **Repo/Website Link:** [https://github.com/milankowww/mailintel](https://github.com/milankowww/mailintel)
>
> **Description:** MailIntel is a self-hosted application for **secure local AI email triage, summaries, and search**. I built it to help me keep up with messages across existing IMAP and Exchange EWS mailboxes. It **summarizes** and **prioritizes** individual messages, **groups** them by interests and topics, provides **daily/weekly/monthly summaries**, and **answers questions** with links to supporting messages.
>
> Why? Many people use agentic AI to process their email. That is risky: emails contain untrusted text that can manipulate an agent, and mailbox permissions can turn a mistaken interpretation into a sent message, deleted correspondence, or leaked information. MailIntel’s central principle is to keep AI mistakes confined to analysis: even if the AI gets something wrong or follows instructions hidden in an email, it cannot send, delete, or change your messages. Its connectors only ever **read**, they can't edit or compose; model outputs become summaries, classifications, and answers but are never executed. Full control over your correspondence stays with you.
>
> You can use a small local model that fits in a few gigabytes of memory, keeping inference on your own infrastructure, or a cloud-based frontier model if you accept sharing submitted email content with its provider. Ollama and OpenAI-compatible endpoints are supported. MailIntel is open source under EUPL-1.2, with screenshots and a user guide in the repository.
>
> **Deployment:** The repository includes a Dockerfile and Docker Compose configuration that build and run the application with PostgreSQL and pgvector. You provide mailbox access and a reachable model service for text generation and embeddings; Ollama and OpenAI-compatible endpoints are supported. The README includes installation commands, screenshots, and links to an illustrated user guide. It is designed for a private installation with a shared access token.
>
> **AI Involvement:** AI tools have been used for development, documentation, and code review. The application uses language models for email analysis, summaries, and search, together with embeddings for retrieval and topic grouping. You choose the models and providers, especially including local small ones. Local inference keeps processing on your infrastructure; cloud inference sends the submitted email content to the selected provider.

---

> **Fancy_Fix_2605**（1 分） · 2026-10-20T19:30:40+08:00　
> **Project Name:** Termoso - self-hosted, zero-knowledge SSH client for desktop, Android and iOS (an open-source alternative to Termius, including the team and enterprise features)
>
> **Repo/Website Link:** https://github.com/termoso/termoso | https://termoso.dev | docs: https://docs.termoso.dev
>
> **Description:**
> Termoso is an SSH/SFTP client with its own sync server that you run yourself. The design goal is simple: the server never holds anything it could read. Hosts, keys, passwords, snippets and port-forwarding rules are encrypted on the device, team vaults are sealed to each member's public key, and sign-in is OPAQUE, so even the password never reaches the server. A compromised or subpoenaed server yields ciphertext.
>
> **Clients.** Linux (x86_64/aarch64), Windows, macOS (Apple Silicon/Intel) - Rust core with a Tauri shell; Android - Kotlin/Compose over the same Rust core; iOS - SwiftUI (sideloaded). All of them work offline without a server. Protocols: SSH, Mosh, Telnet, serial, SFTP, WebDAV. Terminal: Termius-style key panel on mobile, autocomplete, snippets with variables and multi-target run, tabs/splits, local/remote/dynamic port forwarding, jump hosts, SOCKS/HTTP proxies, FIDO2 security keys, SSH certificates, agent forwarding, session recording, two-pane SFTP. Android additionally runs a real Alpine/Ubuntu userland (proot) for a local shell.
>
> **Server.** One container (amd64/arm64) + Postgres, Redis and an S3-compatible store for client-encrypted session logs. Accounts, devices, MFA (TOTP, passkeys, e-mail, backup codes), recovery keys, device approval, encrypted sync with conflict handling, realtime push, a Termius-compatible REST bridge for automation, Prometheus metrics, multi-replica HA, backup/restore tooling.
>
> **Teams and the enterprise:**
> - roles with per-permission matrix and custom roles; per-host/group ACL inside a vault (hidden / connect-only / read / edit);
> - team policies: mandatory 2FA, session lifetime, keys-only-in-team-vaults, device approval, IP allow-list, mandatory session recording with retention;
> - audit log with retention, export and webhooks/SIEM delivery; GDPR export and scheduled deletion;
> - SSO via OIDC/SAML with per-team identity providers, home-realm discovery, JIT provisioning and SSO-only mode; SCIM 2.0;
> - just-in-time access requests with approval and automatic expiry; key/password rotation jobs; corporate mode (every account joins a home team, personal vaults can be disabled);
> - admin console for the server operator: users, teams, policies, background jobs, server settings.
>
> **Supply chain.** Every release ships CycloneDX and SPDX SBOMs and Sigstore attestations; CI runs integration tests against real Postgres/Redis/S3/SMTP, `cargo deny` and `npm audit`. AGPL-3.0.
>
> **Not there yet.** iOS is sideload-only (AltStore/SideStore source is included) and has fewer features than desktop/Android; macOS builds are ad-hoc signed (right-click -> Open on first launch).
>
> **Deployment:**
> ```
> git clone https://github.com/termoso/termoso && cd termoso/deploy
> cp .env.example .env    # public URL + master key
> docker compose up -d    # or the Podman Quadlet units in deploy/quadlet
> ```
> Guide (Compose and Quadlet, Caddy TLS profile, backups, HA): https://github.com/termoso/termoso/blob/main/docs/SELF_HOSTING.md. Clients via winget, Homebrew, apt/dnf repos, AppImage, APK and ipa: https://termoso.dev/#download. A hosted instance (app.termoso.dev) is available for trying the apps before deploying.
>
> **AI Involvement:** Yes, as a tool. Architecture, the cryptographic and sync model, the security design and all product decisions are mine; a substantial part of the code and documentation was written with AI assistance and is reviewed and tested before release (integration tests against real services, clippy with -D warnings, cargo deny, SBOM and signed attestations).

---

> **New-Gear-7252**（1 分） · 2026-10-20T21:47:04+08:00　
> https://preview.redd.it/deeajxi3nmwh1.png?width=2720&format=png&auto=webp&s=967527350bc3b17709e4a55e8ead9b5046d4f09b
>
> **Project Name:** Hotly (hotly-os)
>
> **Repo/Website Link:** [https://github.com/designAtHotly/hotly-os](https://github.com/designAtHotly/hotly-os)
>
> **Description:**
> A self-hosted paid inbox for one person. You share one link; people pay to send you a note (priced by length, $5 / $10 / $15 by default, all configurable) or subscribe weekly, and you reply from one inbox when you have time. Payments go straight to your own Stripe account; nothing passes through us.
>
> **The problem it solves:** people with an audience (creators, coaches, consultants) get more DMs than they can answer, and the ones that matter get buried. A price on the message filters the noise and pays for the time spent replying.
>
> **Features:**
>
> \* Paid one-time notes and weekly subscriptions, prices set by the owner
> \* One inbox with needs-reply / all / blocked views
> \* Replies can carry a photo or video, free or paid to unlock
> \* People writing in don't create accounts (cookie after Checkout, email recovery
> \* A small free community page: you post a prompt, people reply
> \* One person per install, on purpose: one Stripe account, one inbox, simple data model
>
> **Deployment:**
>
> \* Docker Compose: Postgres 18, Go API, Next.js, Garage (private S3-style media), Caddy (automatic TLS)
> \* Installer pinned to a release tag (v0.1.6), or \`cp .env.example .env\` and \`docker compose up --build\`
> \* Try it locally first: \`./scripts/install.sh --local\` runs everything with external services skipped
> \* No prebuilt images yet: it builds on the box, so plan for 2 vCPU / 4 GB (build peaks \~2.7 GB, idle a few hundred MB)
> \* Needs your own Stripe (payments), Firebase (owner's Google sign-in only) and SendGrid (three emails). It boots without them. Generic OIDC and SMTP would be better; PRs welcome
> \* Docs: README (with a GIF of the whole flow) and docs/operations.md for production, backups and upgrades
> \* Apache 2.0
>
> **AI Involvement:**
> A good part of the code, the tests and the docs was written with an AI coding assistant. The team reviews and runs everything, and CI runs the Go tests and type checks on every PR and release tag.
>
> Feedback very welcome, especially: is the README clear if you've never seen the project, and what would stop you from running it? **Hotly (hotly-os)**
>
> **Repo/Website Link:** [https://github.com/designAtHotly/hotly-os](https://github.com/designAtHotly/hotly-os)

---

> **SegFault0x00000**（1 分） · 2026-10-20T22:26:50+08:00　
> **Project Name:** Kept
>
> **Repo/Website Link:** [https://github.com/keptinventory/kept](https://github.com/keptinventory/kept) \- [https://keptinventory.info](https://keptinventory.info)
>
> **Description:** A self-hosted home inventory: what you own, where it is, and what’s due. I like Homebox, but I wanted more, so it’s an alternative that imports your Homebox data.
>
> * 3D map of your place (floors, rooms, shelves, boxes). Tap anything to see what’s in it.
> * QR labels for boxes and shelves; scan one to see the contents.
> * Reminders for warranties, services, loans and low stock, through ntfy, Telegram, email and more.
> * Installs on your phone as a PWA and works offline.
> * Optional AI that reads receipts and labels for you to confirm. Works with local models via anything OpenAI-compatible (Ollama etc.).
> * Home Assistant and Paperless-ngx integrations, CSV and Homebox import.
>
> **Deployment:** Docker image on GHCR, with Docker Compose or a Helm chart.
>
> * Compose: [https://keptinventory.info/install/compose/](https://keptinventory.info/install/compose/)
> * Kubernetes/Helm: [https://keptinventory.info/install/kubernetes/](https://keptinventory.info/install/kubernetes/)
> * Try it without installing: [https://keptinventory.info/try/kept/](https://keptinventory.info/try/kept/)
>
> **AI Involvement:** Built with heavy use of AI coding assistants. I design and direct the work, review the code, and test every release; the code itself is largely AI-written.
>
> https://preview.redd.it/bpmrrwfttmwh1.jpeg?width=1552&format=pjpg&auto=webp&s=e8ba050da6e77e02e6955d13afb0fa6b108dc048

---

> **chadMueller**（1 分） · 2026-10-20T22:35:00+08:00　
> **Project Name:** Nostalgex
>
> **Repo/Website Link:** [https://github.com/chadMueller/Nostalgex](https://github.com/chadMueller/Nostalgex) (site: [https://www.nostalgex.app/?utm\_source=reddit&utm\_medium=social&utm\_campaign=launch\_oct26\_r\_selfhosted\_megathread](https://www.nostalgex.app/?utm_source=reddit&utm_medium=social&utm_campaign=launch_oct26_r_selfhosted_megathread))
>
> https://preview.redd.it/ledpf04fvmwh1.png?width=3178&format=png&auto=webp&s=79916318f56a9f8bf422256b0424d5f9001bf2b0
>
> **Description:** Nostalgex turns your own Plex, Jellyfin or Emby library into 130+ live channels with a retro cable style grid guide, so you can flip channels instead of scrolling a library. There's nothing to install on your media server and no account. You sign in and the channels are already playing. It runs as an Apple TV app (tvOS 18+) and a web tuner. The self hosted tuner exists because browsers block an https site from reaching a plain http server on your LAN, so if your Jellyfin or Emby is at [http://192.168.x.x:8096](http://192.168.x.x:8096) you can run the tuner next to it over plain http. 1.0.3 came out this morning: no more burned in subtitles on Jellyfin and Emby, and TIS THE SEASON grows to eight holiday channels. Free and MIT licensed.
>
> **Deployment:** Released and available now. Docker image for amd64 and arm64, about 27 MB, nginx serving static files, non root, works read only. No database or backend.
>
>     docker run -d --name nostalgex -p 8080:8080 --restart unless-stopped ghcr.io/chadmueller/nostalgex:latest
>
> Then open http://YOUR-SERVER-IP:8080 and connect your server. A compose example and setup docs are here: [https://www.nostalgex.app/self-host?utm\_source=reddit&utm\_medium=social&utm\_campaign=launch\_oct26\_r\_selfhosted\_megathread](https://www.nostalgex.app/self-host?utm_source=reddit&utm_medium=social&utm_campaign=launch_oct26_r_selfhosted_megathread). Set NOSTALGEX\_ENRICHMENT=off and it talks only to your media server. Image tags are 1.0.3, 1.0 and latest. Apple TV app: [https://apps.apple.com/app/apple-store/id6762563534?pt=128802261&ct=launch\_oct26\_r\_selfhosted\_megathread&mt=8](https://apps.apple.com/app/apple-store/id6762563534?pt=128802261&ct=launch_oct26_r_selfhosted_megathread&mt=8)
>
> **AI Involvement:** AI was used heavily. I'm a product designer, not a career developer, so most of the code was written with Claude (via Cursor) from my specs, and AI helped with the docs and some of the copy. The design, channel lineups, features and decisions are mine, I test every build on my own Apple TV and servers, and the full source is public on GitHub.

---

> **reloopcrm**（1 分） · 2026-10-20T23:37:08+08:00　
> **Project Name:** Reloop CRM
>
> **Repo/Website Link:** https://github.com/reloopcrm/reloop
>
> **Description:** I'm the developer. Reloop is a CRM that connects to your mailbox (IMAP, Google or Microsoft 365), reads the history and builds contacts, companies and a timeline from it. Its main screen is a "win back" list: former customers ranked by what happened in your mail, with every point shown as its own line, for example "1 open conversation: an inquiry or offer nobody closed". It asks only for read access to your mailbox and never sends mail. When it drafts a follow-up, the Send button opens your own mail client. New in 0.22: a read-only MCP server, so you can connect ChatGPT, Claude or Claude Code to your own instance and let it draft mails from your CRM data.
>
> On my own mailbox it read 13,821 conversations. 64.5 percent of the ones it assessed had no business value, and 178 former customers came out as worth a call.
>
> **Deployment:** Released (v0.22.0, tagged), AGPL-3.0, Docker Compose. One command on a Linux server:
>
>     curl -fsSL https://reloopcrm.com/install.sh | sh
>
> It asks for a domain, an email and a password, generates the secrets, pins the newest release and starts Postgres, API, web app and agent. Images for amd64 and arm64. Guide: [docs/self-host.md](https://github.com/reloopcrm/reloop/blob/main/docs/self-host.md). 8 GB of RAM recommended: the agent alone used 3.6 to 3.9 GB under load during a big import. Without an AI key it runs as a normal CRM.
>
> **AI Involvement:** Most of the code was written by AI coding agents that I directed, reviewed and tested. CI runs type checks, lint and the integration tests on every pull request. The product itself uses an LLM to read mail, but only with a key you add (OpenRouter, OpenAI or Anthropic) and only with the provider you choose.

---

> **Unfair_Fall_4527**（1 分） · 2026-10-20T23:53:47+08:00　
> **Project Name:** Tabularia
>
> **Repo/Website Link:** [https://github.com/JumpAsAService/Tabularia](https://github.com/JumpAsAService/Tabularia)
>
> **Description:** is a Selfhosted opensource (AGPL 3.0), no-code/low-code alternative to ETL Enterprise grade software for non-developers.
>
> My main goal is to let "Business Users"/"Non Technical users" capable in Data manipulation and Data Analysis (AI assisted or not) from lightweight flows to a Billion of rows without sampling. The application can scale up from a laptop using locally Polars (with lazy sinks), DuckDB or local Clickhouse (chdb), to a Company with a serious Data Warehouse using Clickhouse External (IAAS) or Google Bigquery (SAAS) as engines.
>
> I tried to challenge mainstream software bottlenecks or bad user experiences (like mandatory sampling on big tables or lack of capabilities that i faced in my experience) giving the choices and good performances. I tried also to replicate my beloved Airflow CeleryExecutor architecture of Apache Airflow managing the queue of requests with two separate worker groups (one for dev, one for scheduled flows).
>
>   \- Database and other sources: Postgre, MSSQ, Oracle, Trino, Clickhous, Uploaded files, Sharepoint, S3, HTTP requests.
>
>   \- RBAC and SSO integration (during my first deploy in a Company tweaked a bit the source code to address business requirements, so maybe some little changes are needed also in your case!). For structured companies with a security team there is also a Splunk emit (tested)
>
>   \- The application is also oriented to help non-technical users to find what they want with simple "Pivot" like interface or simple plots with Echart and a "Agent chat" with OpenAI compatible endpoints (so also VLLM for selfhosting) that do queries against datasources using the engine that you choose.
>
>   \- There are also a lot of other features like Openlineage integration (to track where data came from and go) External API Endpoint to interact with the application programmatically, HTTP Request datasources, main opensource databases...
>
> **Deployment:** to test the application there is a "docker compose up" without any setting needed, but if you want scale up there is also a Helm chart available and a detailed guide here [**https://jumpasaservice.github.io/Tabularia/docs**](https://jumpasaservice.github.io/Tabularia/docs) **(encryption and secure admin warmup mandatory for helm so follow the guide). Minimum Requirements 8 GBs of Ram and a bunch of minutes for bulding phase**
>
> **AI Involvement:** AI tools have been used for development, documentation, and code reviews. 3700 test in CI (anti regressions) and test on real databases (selfhosted or using external cloud resources).
>
> https://preview.redd.it/xq9c6rgk6nwh1.png?width=1438&format=png&auto=webp&s=e9f169c6f470795524116e2e17bf4b53e1d50e6c

---

> **Strong-Leg-9636**（1 分） · 2026-10-21T00:10:56+08:00　
> **Project Name:** VoxScribe
>
> **Repo/Website Link:** [https://github.com/ahmedhmam1994/voxscribe-ai-voice-dictation](https://github.com/ahmedhmam1994/voxscribe-ai-voice-dictation)
>
> **Description:** Offline voice dictation for Windows and Android, as a local replacement for cloud dictation services. Most dictation tools send your audio to someone else’s server. VoxScribe runs OpenAI’s Whisper fully on your own hardware: faster-whisper on Windows and sherpa-onnx on Android. You hold a hotkey in any app (or tap a floating button on the phone), talk, and the text is typed where your cursor is. There’s no account and no cloud processing, and once the model has downloaded it works with the network unplugged.
>
> It types with simulated keystrokes instead of the clipboard, refuses to type into password fields, and adjusts formatting to the app you’re in. A misheard sentence can be rerun on a bigger model with one key, and Android can transcribe audio and video files into text or SRT subtitles on the device. The core is MIT licensed and free with no limits.
>
> **Deployment:** It’s a desktop and mobile app, not a server, so there’s no Docker image. Windows has an installer on GitHub Releases and a Scoop bucket. Android has a signed APK on GitHub Releases. The README covers install, first run, hotkeys and model choices.
>
> **AI Involvement:** Developed with Claude Code as a coding assistant, and it’s credited as co-author on the commits. The design decisions, the testing on real microphones and phones, and the releases are all done by hand.

---

> **Martin_mpf**（1 分） · 2026-10-21T00:25:51+08:00　
> https://preview.redd.it/fbppwqi5fnwh1.png?width=2059&format=png&auto=webp&s=2c55da51f44d220002bf3f2517e38b1a5f5faaff
>
> **Project Name**: Gamelog
>
> **Repo/Website Link**: [https://github.com/mperezfo/Gamelog](https://github.com/mperezfo/Gamelog)
>
> **Description**:
>
> Self-hosted video game tracking website.
>
> For years I tracked the games I played in a Google Sheets spreadsheet. Later I moved to a Notion database. That was better, but it never quite fit the way I wanted to track things, and I prefer open source software anyway. I looked for an alternative and couldn't find one that worked 100% for me, so I built my own. I've been using it for a while and just released v1.3.0, so I'm making it public in case someone else finds it useful too.
>
> * A board with your games grouped by status (Wishlist, Pending, Playing, Played). You can drag them between columns.
> * Upcoming releases, plus a monthly calendar of release or play dates.
> * Stats over the years: average scores, and breakdowns by platform, genre, developer and publisher.
> * Fills in release date, platform, developers and publishers from IGDB, and finds covers on IGDB or SteamGridDB (optional, with your own API keys).
> * Search and filters.
> * Installable on your phone as a PWA, and it still opens read-only when offline.
> * Full export as a .zip (plain JSON plus images) that you can restore later.
> * Multiple accounts, each with its own private library.
>
> It has a Go backend, a React + TypeScript frontend and a MariaDB database, and it's MIT licensed.
>
> I built it around my own way of tracking games, so I can't promise to accept every feature request. Bug reports and fixes are very welcome, though. If you like the project but want it to work differently, feel free to fork it and change whatever you want.
>
> Deployment: A single Docker image (\`ghcr.io/mperezfo/gamelog\`) next to MariaDB. The README has a ready-to-use docker-compose example, and \`docs/self-hosting.md\` covers configuration, reverse proxies and the optional IGDB/SteamGridDB keys.
>
> AI Involvement: Most of the frontend and part of the backend were written with Claude. That said, I'm very picky about which changes I accept, and I review all the code before it goes in. In the end, this is an app I rely on myself. I get it if some of you don't want to use the app because it's partly made with AI, and that's totally fair.

---

> **finesseserver**（1 分） · 2026-10-21T00:29:33+08:00　
> **Project Name:** Finesse
>
> **Repo/Website Link:** https://github.com/CoffeeCC/finesse (Discord for help and feedback: https://discord.gg/G4RfBMytJg)
>
> **Description:**
> Finesse is a free, MIT-licensed app that sets up a whole home media server in one go: Jellyfin, Sonarr, Radarr, Lidarr and Prowlarr, already wired together, plus its own request page. The idea is search, add, watch. Someone at home searches for a show, adds it, and it shows up ready to play, without you having to be the household IT department.
>
> I built it because every time I set up Jellyfin and the arr stack for family, the setup itself was the hard part: getting paths, API keys and download clients to agree with each other. Finesse does that part and keeps the stack updated afterwards. If you already run Jellyfin or the arrs, there's an adopt mode so you don't have to start over.
>
> It's a front end and installer, not a content source. It ships with no content and no indexers.
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

> **dead_axmed**（1 分） · 2026-10-21T01:04:45+08:00　
> **Project Name:** Monolith — docs, projects and connected databases on your own server
>
> **Repo/Website Link:** [Source and releases](https://github.com/MaxJafar/monolith) · [Website, screenshots and guides](https://monolith-site-maxjafars-projects.vercel.app)
>
> **Description:** I'm a Monolith maintainer. It's a self-hosted personal workspace that brings documents, project actions, structured records, a calendar and a configurable daily dashboard together.
>
> One workflow to try: keep a personal project brief and research in Docs, plan its actions in Projects, then review dated work on the calendar and dashboard.
>
> What you can explore:
>
> * Nested pages, rich blocks, references, backlinks and inline database views.
> * Databases with typed properties, relations, saved filters, and table, board and calendar views.
> * Project boards, lists, timelines and Gantt views, plus Today and Upcoming action views.
> * Optional addons and widgets for shaping the workspace, and a separate MCP bridge/JSON CLI for external agent clients. The bridge starts in read mode; writes require deliberate enablement.
>
> The website shows existing product screenshots with synthetic example data.
>
> **Deployment:** [Download the Linux x64/ARM64 server images and matching setup kit](https://github.com/MaxJafar/monolith/releases/latest), then follow the [installation guide](https://github.com/MaxJafar/monolith/blob/main/release/INSTALL.md). Hosting requires Docker Engine, Docker Compose and an HTTPS reverse proxy. The browser client runs from your host; Windows and macOS clients connect to that same server. Desktop downloads do not include a server or database.
>
> **License and preview status:** This is a development preview. Source is available under [CC BY-NC-SA 4.0](https://github.com/MaxJafar/monolith/blob/main/LICENSE), with non-commercial limits and package-specific notices. Windows installers are unsigned and macOS is not notarized. General offline synchronization and simultaneous live document co-editing aren't promised.
>
> **AI Involvement:** AI generated most of the implementation under human direction. This introduction was also drafted with AI assistance.
>
> If you try it, I'd appreciate specific feedback on the setup instructions and the first project workflow: where does it become unclear or make you duplicate work?

---

> **Gully5931**（1 分） · 2026-10-21T05:00:49+08:00　
> **Project Name:** Hold My Docs (HMD)
>
> https://i.redd.it/fq3gw504sowh1.jpeg
>
> **Repo/Website Link:**
>
> * GitHub: [https://github.com/soollabs/holdmydocs](https://github.com/soollabs/holdmydocs)
> * Docs: [https://hmd.sool.dev](https://hmd.sool.dev/)
>
> **Description:**
>
> I've been building a self-hosted wiki that stores pages as Markdown files in a regular Git repository. Every save creates a commit, so you get version history without having to know Git yourself.
>
> I originally built it for my homelab notes and runbooks. I wanted something that didn't need a database and wouldn't lock my documentation into a particular application.
>
> It's grown beyond that. I now use it for company documentation, sharing knowledge between local LLMs running on different machines, and publishing HMD's own documentation as a static site.
>
> Features include:
>
> * Git history, diffs, revert and optional remote sync
> * Conflict detection that preserves your draft if another user or agent edits the same page
> * Markdown editor, wiki-links, backlinks, Mermaid and attachments
> * Full-text search, with optional PDF/Office indexing via Apache Tika
> * Namespaces with separate visibility, navigation and appearance
> * Local authentication, OIDC and scoped access tokens
> * MCP server for AI agents with configurable permissions
> * Static site export and read-only repository browsing
>
> It's still early-stage, so expect some rough edges. Git sync only fast-forwards; diverged histories need to be resolved manually.
>
> **Deployment:**
>
> Written in Go and MIT licensed. Runs as a single binary or through Docker Compose. Installation instructions are in the documentation linked above.
>
> **AI Involvement:**
>
> I've been a DevOps engineer for the last 8 years, and made a fair amount of open source projects that were relatively simple. This is my first using various different models across OpenRouter, generally for tests and doing repeated testing of changes across different UI screens, which has allowed me to extend the scope of what I can use this app for. it's useful to me, maybe you might find a use for it.
>
> I'd be interested in feedback, particularly from anyone already keeping their documentation in Git.

---

> **itsmemac43**（1 分） · 2026-10-21T05:16:54+08:00　
> **Project Name:** Agent Cairn
>
> **Repo/Website Link:** [https://github.com/itsmemac/AgentCairn](https://github.com/itsmemac/AgentCairn)
>
> **Description:** Shared, persistent memory for AI coding agents, running on your own box. I lost a project’s worth of context when my laptop died, and a fresh agent knew nothing. So agents now write what they learn to a Neo4j database you own: conventions, gotchas, decisions and the reasons behind them. A new session on any machine starts from a short briefing instead of re-reading the repo. Sessions are recorded as they happen, and before an agent stops it writes a handoff (done / in progress / next / blocked / tried and dropped), so another agent can pick up where the last one left off.
> There’s also a small web dashboard with a graph view, private projects, sharing, invite links and an audit log if more than one person uses it. A single user just runs it as is.
>
> **Deployment:** Docker, with one image (`ghcr.io/itsmemac/agentcairn`) and a Neo4j container. I run mine on Unraid, and there’s a guide for that in the docs. It uses plain Cypher, so it runs on Neo4j Community. Nothing makes outbound calls, and the server never calls an LLM. The agent does the writing, so there’s no API key. Connecting Claude Code is one line:
>
> `claude mcp add cairn --scope user -e CAIRN_URL=... -e CAIRN_TOKEN=... -- npx -y agentcairn mcp`.
>
> It works with any MCP-capable agent, but the hooks are for Claude Code. MIT licensed.
>
> **AI Involvement:** Most of the code, tests and docs were written by Claude Code, working from my design and direction. I decided what to build and how access control and handoffs should work, and I run it daily on my own NAS. I review and test it, including integration tests against a real database.
>
> It’s young (0.2.x), so I’d love bug reports and ideas. Happy to answer questions about the setup.
>
> https://i.redd.it/38war3w2vowh1.jpeg

---

> **sfn_alpha**（1 分） · 2026-10-21T06:23:36+08:00　
> **Project Name:** sfn-wiki-mirror
>
> **Repo/Website Link:** [https://github.com/SFN-ALPHA/sfn-wiki-mirror](https://github.com/SFN-ALPHA/sfn-wiki-mirror) (MIT)
>
> **Description:**
>
> A personal project I've been sinking evenings into: a self-hosted copy of English Wikipedia that local AI agents can search over MCP (or plain REST). It's not for browsing; Kiwix already does that well. It's passage search: an agent asks a question and gets the best paragraph from each matching article, plus a permalink to the exact revision it read.
>
> **Why:** I run local models and wanted them to look things up as often as they like, without hammering Wikipedia's API or sending every query to a third party. Also, honestly, I wanted to see if I could.
>
> What works today:
>
> * Monthly English Wikipedia snapshot from Wikimedia Enterprise (the free tier includes it), about 151 GB compressed
> * Parsed to plain text in SQLite: 7.2M articles cut into 41.6M passages of about 720 characters
> * Keyword search (BM25-style sparse vectors in Qdrant), live for a few days at about 27 ms per query on the LAN
> * MCP server with two read-only tools (`wiki_search`, `wiki_read`) plus a REST API, with a revocable key per client
> * The build runs beside the live index and swaps in when done, so search stays up during rebuilds
>
> What's happening right now: embedding all 41.6M passages with bge-m3 on my home Ollama cluster (1x RTX 3080 Ti and 3x RTX 3050, behind a router I wrote). It started at about 175 passages/s and is now about 215/s as it gets past the long early articles, so the whole run should take about 2⅓ days. The full corpus is roughly 7 to 10 billion tokens. On a cloud embedding API that would be weeks of rate limits and a bill every time I change how the text is cut; at home it costs electricity and fan noise. Vectors are float16 on disk (about 85 GB) with a binary-quantized copy in RAM (about 5 GB) for rescoring. The run checkpoints as it goes and verifies the checkpoint against Qdrant on restart, because a multi-day job will get interrupted at some point.
>
> Not done yet, being honest:
>
> * Hybrid search (fusing keyword and vector results) is next, once the vectors finish
> * Monthly updates that re-embed only changed passages are planned. The first real test is the November snapshot, so it's unproven
> * English only, plain text only, no images
> * It's a lot of box for what it is. If you just want offline Wikipedia, Kiwix with a ZIM file is far simpler, and I'd point most people there.
>
> **Deployment:**
>
> No Docker image, on purpose: the installer sets up a default-deny nftables firewall and separate users for the builder (can reach the internet, listens on nothing) and the server (listens, can't reach the internet), so it wants a dedicated box.
>
> * A dedicated Debian 12/13 LXC or VM (a Proxmox LXC is the tested path), 6 cores, 32 GB RAM advised (8 GB minimum for keyword-only)
> * About 550 GB of disk on a single drive, or 250 GB fast disk plus a NAS mount for the snapshots
> * A free Wikimedia Enterprise account
> * Clone the repo, set your LAN range in one env file, run `deploy/install.sh` (there's a `--dry-run`), then start the first build: about 30 minutes to install and about 14 hours for the first build
> * Semantic search (optional) needs an Ollama node with a GPU, or an Ollama-compatible cluster, running bge-m3
> * Connecting an agent is one command: `claude mcp add --transport http wikipedia http://<host>:8300/mcp --header "Authorization: Bearer <key>"`
>
> The README covers requirements and setup; docs/OPERATIONS.md walks through the install, updates and failure recovery; docs/MCP.md covers client setup. Expect rough edges: it grew around my own setup, though I've tried to make it installable by someone else.
>
> **AI Involvement:** Heavy, the entire project has been developed in VS Code using an orchestrator-agent workflow with Opus 5.5 and its agent delegates including mostly Sonnet 5.5. Most of the code and docs were written by Opus 5.5 and its delegates working under my direction. I chose what to build and how it should work, reviewed the changes, and run and test everything on my own hardware. The test suite (about 1,500 tests) runs in CI with no network or GPU.
>
> https://i.redd.it/f9s8560r6pwh1.png

---

> **sfn_alpha**（1 分） · 2026-10-21T06:27:03+08:00　
> Progress this evening, about 3 days left to vectorize all of English Wikipedia:
>
> `Oct 20 17:24:27 wikipedia-mirror python[43163]: 2026-10-20 17:24:27,195 INFO wiki_mirror.embed embed wikipedia_semantic_20261001: 881920 of 7245149 articles (12.2%), 8104736 passages; 229 passages/s over the last 60 s, 204 overall; about 3d 7h left`

---

> **omnichad**（1 分） · 2026-10-21T08:25:00+08:00　
> I'm still not very familiar with webrcade but this is the sort of thing I hope to set up soon for myself.  It looks like a lot of features like SSO currently rely on NextCloud, which I don't use.  But I do have an OIDC server set up (Keycloak).  It also sounds like game saves rely on cloud storage.  Is it possible to save per user saves direct to the server itself?
>
> It will be a while before I get around to trying to get something set up so this may be a lot further along by then.  But it looks really promising and I might be willing to learn a little Python to help get it matching up with what I want.

---

> **ruby-guy**（1 分） · 2026-10-21T09:02:05+08:00　
> Project Name: eze
> Repo: [https://github.com/ahyield/eze](https://github.com/ahyield/eze)
> Link: [https://eze.page](https://eze.page)
>
> Description:
> Drop in a folder of HTML and get back a private URL that only people in your organisation can open. No frameworks, pipelines or config files. Need data? Every site gets a database, realtime updates, file uploads, multiplayer rooms, AI and the viewer's identity through a tiny browser SDK, with nothing to set up.
>
> An open-source take on the idea behind Shopify's internal [Quick](https://shopify.engineering/quick) platform.

---

> **3loodhound**（1 分） · 2026-10-21T11:04:47+08:00　
> So auto-login with Nextcloud works through sso, but you can also just login to either Nextcloud or Dropbox in the settings without an sso proxy in front.  (Google Drive will come soon when I get around to it, trying to get Wii working at a decent speed and memory footprint first) I do recommend one though!
>
> as for why cloud storage, think of it this way. The emulator is actually running on your machine. Inside of your browser (meaning the computer processing the rom is your computer) by default they store in your computers cache. Everyone uses the same applications and code to run the same thing, and by linking it with cloud storage it allows each local instance to be able to have a unique place to save it without the application having to deal with any long term storage and unique authentication of users saves.

---

> **mtsm_**（1 分） · 2026-10-21T18:13:35+08:00　
> **Project Name:** Jotter
>
> **Repo/Website Link:** https://github.com/Muatasim-Aswad/jotter
>
> **Description:** I wanted one place to put a thought down without choosing a notebook or creating a document first, so I built a small scratchpad I've been using myself. It opens straight into writing, and the same text is available across my devices.
>
> It supports offline writing after the first online visit, syncs while the app is open and connected, and receives shared text and links on supported Android browsers. Conflicting edits need an explicit choice. There's one scratchpad, no note hierarchy or version history.
>
> **Deployment:** A published Linux amd64 container and Docker Compose file are available, with source-build instructions too. The backend uses Go and SQLite. There is no built-in login: run it behind a trusted private HTTPS access boundary.
>
> Setup: https://github.com/Muatasim-Aswad/jotter/blob/main/docs/deployment.md
>
> MIT licensed; screenshots are in the README. I'd appreciate feedback on the first-run setup and whether this small workflow is useful to anyone else.
>
> **AI Involvement:** AI-assisted development.

---

> **imlotso**（1 分） · 2026-10-21T18:34:13+08:00　
> **Project:** discourse-indexnow
>
> **GitHub:** [https://github.com/imlotso/discourse-indexnow](https://github.com/imlotso/discourse-indexnow)
>
> **Description:**
>
> Hey everyone! 👋
>
> I run a Discourse forum and wanted an easier way to notify search engines whenever new topics are published or updated, instead of just waiting for crawlers to find them.
>
> So I used an AI coding agent to develop **discourse-indexnow**, an open-source Discourse plugin that automates URL submissions through IndexNow.
>
> A few things it does:
>
> * Automatically submits new and updated public topics
> * Supports replies and multilingual topic URLs
> * Lets you bulk-submit older topics
> * Includes rate limiting, batching, and an admin dashboard
> * Filters out private and restricted content
>
> **Deployment:**
>
> It's free, MIT-licensed, and runs directly inside Discourse. Just install the plugin, rebuild your container, and configure it through the admin panel. No separate service needed.
>
> **Setup guide:** [https://www.sitetalk.net/t/topic/642](https://www.sitetalk.net/t/topic/642)
>
> **AI involvement:**
>
> This project was developed using an AI coding agent, which handled the code implementation. I provided the project requirements and direction. I'm sharing it openly so others can use it, review the code, and suggest improvements.
>
> I know IndexNow doesn't guarantee indexing or better rankings, but I figured this could be useful for other self-hosted forum owners.
>
> Would love to hear your thoughts! Is this something you'd use for your Discourse setup? Any features you'd like to see added?

---

> **Careless_Love_3213**（1 分） · 2026-10-21T18:59:35+08:00　
> Project Name: Frankensurf (my project, Apache-2.0)
>
> Repo: [https://github.com/yail259/frankensurf](https://github.com/yail259/frankensurf)
>
> Setup: [https://frankensurf.dev/docs/firecrawl-compatible/](https://frankensurf.dev/docs/firecrawl-compatible/)
>
> Description: A self-hosted web reader for AI tools. I built it after my agents kept treating bot checks and empty JavaScript pages as successful reads. It tries a cheap fetch first, checks whether the useful content came through, and tries a browser or another configured provider when it did not. If it runs out of options, it reports the failure.
>
> It exposes a Firecrawl-compatible API, so tools such as Open WebUI can use it through their existing Firecrawl settings. There is also a Python library, CLI and MCP server. The setup page covers the client settings and Docker networking gotchas.
>
> Deployment: Available on PyPI (pip install frankensurf, then frankensurf install) and as ghcr.io/yail259/frankensurf. The server listens on port 3002; set FRANKENSURF\_API\_KEY and point your client's Firecrawl base URL at the server.
>
> It is still an alpha. Browser fallbacks can use substantial RAM, difficult sites still fail, and home and datacentre connections produce different results. Paid providers are optional and need your keys. The server runs on your machine; external providers such as Jina Reader still send requests to their services when enabled.
>
> AI Involvement: Built with substantial AI assistance. This comment was also drafted with AI assistance.
>
> I'd be interested in which self-hosted client you use and which pages its current loader fails to read.

---

> **Maskio82**（1 分） · 2026-10-21T22:02:48+08:00　
> Ciao. Come funziona il sistema delle date?
> Il mio problema è che scarico la cartella di whatsapp, rimuovo le foto inutili, poi converto il nome in AAAAMMGG-HH.MM.SS per poi catalogarle nel mio archivio. Questo software fa in automatico questa operazione?

---

> **Recent_Knowledge_966**（1 分） · 2026-10-21T22:12:03+08:00　
> Project Name: Upstar
>
> Website: [https://upstar.dev/t/self-hosted](https://upstar.dev/t/self-hosted)
>
> Description: GitHub trending, but per topic. GitHub Trending is dominated by huge repos, so small self-hosted projects rarely show up. Upstar ranks repos inside each of 62 topics (Self-hosted, Homelab, Local LLMs, Emulation…) by stars gained relative to their size (gain ÷ √stars before), so a 300-star app that doubles in a week can beat a 50k-star one gaining 1k. This week in self-hosted, for example: openGym (gym tracker), rustrak (lightweight error tracking compatible with Sentry SDKs) and Arrmada (one app for all your media). Repos with fake-looking star patterns and malware lures are filtered out.
>
> Deployment: It's a hosted website, not something you self-host. I'm posting it as a tool for finding self-hosted projects. Free, no account needed to browse; you can sign in with GitHub (read-only) to follow topics and get a weekly email. How the ranking works: [https://upstar.dev/how-trending-works](https://upstar.dev/how-trending-works)
>
> AI Involvement: I built it with a lot of help from Claude Code, reviewing and deciding every change myself. The site also uses Claude Haiku to review suspicious repos (lures, spam). The rankings themselves are plain math on GitHub star data, no AI.
>
> I'm the author. Feedback very welcome, especially on what should or shouldn't count as "self-hosted" in the ranking.

---

> **M0Rf30**（1 分） · 2026-10-21T23:10:56+08:00　
> **OpenArtifact** — self-hosted artifact repository, AGPL-3.0
>
> One Go binary + PostgreSQL. Hosts packages for npm, PyPI, Maven, Docker/OCI, Helm, Debian, RPM, Go, Cargo, NuGet, RubyGems, Conda, Conan, Ivy, sbt and raw files, with a web UI.
>
> - RBAC, API tokens, OIDC/SAML SSO
> - Signed APT/RPM metadata
> - Vulnerability (OSV/Trivy/Grype), license and secret scanning, SBOMs
> - Storage: filesystem, S3, GCS, Azure, OCI
> - Webhooks, cleanup policies, quotas, audit log, backups
> - Optional MCP endpoint for AI agents
>
> Not there yet: proxy/remote and group repos (configurable, not served), import from Artifactory/Nexus.
>
> Why: I wanted something lighter than Artifactory/Nexus that covers the formats I actually ship.
>
> `docker compose -f docker/docker-compose.yml up -d --build`
>
> AI use: [AI USE]
>
> Feedback on formats and missing features welcome.

---

> **olivercer**（2 分） · 2026-10-21T23:31:32+08:00　
> Ciao, il sistema delle date funziona in questo modo:
>
> \- I media vengono organizzati per Contatto, poi per anno, infine per inviati e ricevuti. Quindi avrai una cartella chiamata "Francesco Rossi" e i media organizzati per ogni anno di attività, poi separati in inviati e ricevuti (appunto, `<Name>/<Year>/<Sent|Received>`)
>
> \- Per ogni file viene impostata la data e ora di creazione/modifica al momento dello scambio del file: in questo modo si eliminano le date errate che si creano durante lo spostamento/copia tra file system, e puoi ordinare i file per data di invio/ricezione senza doverli rinominare.
>
> Questo differisce leggermente dal tuo sistema di catalogazione, ma spero che ti torni comunque utile!
>
> Qui trovi una foto che mostra la struttura file, che ho usato in un altro post.
>
> https://preview.redd.it/vku29up3auwh1.png?width=2312&format=png&auto=webp&s=5fa2c057d8e601b0df286ae4c92172932f192a71

---

> **tombino104**（1 分） · 2026-10-22T00:14:29+08:00　
> **Progetto**: OS personale
>
> **Sito web**: [ https://github.com/tombino104/PersonalOS ](https://github.com/tombino104/PersonalOS)
>
> **Descrizione**:
>
> * **Check-in giornaliero.** Un tracker di abitudini gratuito e autogestito, costruito attorno a un check-in serale. Traccia le abitudini che hai effettivamente rispettato in sei aree della vita: fisica, disciplina, sociale, intellettuale, carriera e mentalità. Nel tempo, osserva la forma dei tuoi giorni.
> * **Niente gamification tossica.** Niente serie, ranghi, punti da inseguire o notifiche legate al tuo punteggio. Un giorno saltato è semplicemente vuoto, non un fallimento.
> * **Focalizzato sul comportamento.** Misura i comportamenti, non i risultati. Progettato per essere uno specchio, non un giudice.
> * **Completamente gratuito e open source.** Nessun piano a pagamento, pubblicità o costi nascosti. Licenziato sotto AGPL-3.0.
> * **Autogestito e leggero.** Funziona in un singolo contenitore utilizzando FastAPI, SQLite e Svelte. Progettato per umbrelOS e altri host Docker, con supporto per amd64 e arm64.
> * **I tuoi dati rimangono tuoi.** Tutti i dati sono memorizzati localmente in una cartella. Include backup giornalieri e ripristino da un archivio ZIP. Niente telemetria; nulla esce dal tuo dispositivo.
> * **Funzionalità integrate.** Include un calendario, un sistema di plugin (attualmente comprende un tracker dell'umore e una citazione quotidiana), temi chiari e scuri, lingue inglese e italiana, un'esperienza guidata al primo avvio e una guida utente.
>
> **Distribuzione**:
>
> * **umbrelOS**: App Store → Menu → Community App Stores → Aggiungi. Community App Store: [ https://github.com/tombino104/personalos-umbrel-store ](https://github.com/tombino104/personalos-umbrel-store)
> * **Docker**: Le istruzioni di installazione e il codice sorgente sono disponibili nel repository principale: [ https://github.com/tombino104/PersonalOS ](https://github.com/tombino104/PersonalOS)
>
> **Coinvolgimento dell'AI**:
>
> Costruito con aiuto di Claude Code. Il codice è revisionato e il progetto ha attualmente oltre 350 test e una pipeline CI.
>
> **Stato attuale e limitazioni**:
>
> * Fase di sviluppo iniziale (v0.12).
> * Disegnato per un singolo utente.
> * Non ancora disponibile nell'App Store ufficiale di Umbrel.
>
> **Feedback desiderato**:
>
> Apprezzerei particolarmente feedback sull'esperienza di installazione su umbrelOS, se il check-in serale sembra sereno e diretto, e quali plugin vorresti vedere aggiunti.
>
> Le schermate sono disponibili nel README. Problemi, idee e richieste di pull sono benvenute.
>
> https://preview.redd.it/nldv4rtyhuwh1.png?width=1440&format=png&auto=webp&s=29bbd2bc04cf8c7c39d434cb505f77dc97a52c71

---

> **raphaelmue**（1 分） · 2026-10-22T00:21:01+08:00　
> https://preview.redd.it/jbpp94pahuwh1.png?width=1440&format=png&auto=webp&s=09fc99f555504f188f09f43ba88c61e2cdc9f4fb
>
> **Project Name:** docktor
>
> **Website:** [https://getdocktor.dev](https://getdocktor.dev)
> **GitHub**: [https://github.com/docktor-app/docktor](https://github.com/docktor-app/docktor) (MIT licensed, no paid tier)
>
> **Description**:
> I’m a big fan of self-hosting, and my stack changes all the time. I try out new apps and move away from Big Tech services wherever I can. After a while I was spending more time on the boring operational stuff than on the apps themselves, so I built docktor to manage my Docker Compose stacks entirely from one place.
>
> I’ve used Portainer, Dockhand, Dockge and others. They’re great for managing containers. But I wanted a tool that covers the whole day-to-day work of running a self-hosted server, not just starting and stopping containers. I also wanted to bring my existing stacks into it without redeploying everything from scratch.
>
> What docktor does:
>
> * **Stacks:** paste a compose file, review the diff and deploy with live status. You can also start from a **template** repository.
> * **Brownfield import:** adopt or migrate Compose projects that are already running on the host.
> * **Updates:** see when a newer image is available and apply it whenever you choose.
> * **Backups & restore:** restic-based, scheduled or on demand, with a run history.
> * **Reverse proxy & TLS:** a domain per service with automatic Let’s Encrypt certificates, built in.
> * **Real health checks:** HTTP probes, uptime and incident history, disk usage and email alerts.
> * **Account security:** 2FA via authenticator app, recovery codes and sign-in limits.
>
> **What it’s** ***not*****:** docktor is deliberately built for **one Linux host**. If you run several hosts, Swarm or Kubernetes, Portainer or Komodo is a better fit.
>
> **Deployment**:
> docktor runs as two containers (the app plus a bundled Postgres) from a published image for amd64 and arm64. Grab the `docker-compose.yml` and `.env`, fill in the values and run `docker compose up -d`. More details are in the [documentation](https://getdocktor.dev/guide/get-started).
>
> Please note that docktor needs access to the Docker socket, which is effectively root on the host. Don’t expose port 3000 to the internet, and read the [security page](https://getdocktor.dev/security) before deploying.
>
> **AI Involvement**:
> Claude Code was used heavily in this project. I’m a full-time software engineer and made sure the architecture follows domain-driven design and an event-driven approach, rather than letting the AI decide the structure.
>
> Feedback, bug reports and feature ideas are very welcome. I’d especially like to hear what’s missing from your self-hosting workflow.

---

> **Maskio82**（1 分） · 2026-10-22T00:45:32+08:00　
> Io invece cercavo qualcosa di diverso, un app che pubblica gli annunci ovunque per me, così da non doverlo fare manualmente, sempre per l'Europa...

---

> **Dry_Quantity2691**（1 分） · 2026-10-22T01:02:51+08:00　
> **AltNet Relay: private messenger with groups and calls, on a P2P network (GPL v3)**
>
> Relay is a messenger for Windows and Linux with chats, groups, and voice and video calls. It runs on AltNet, a peer-to-peer network I built, so no company stores your conversations.
>
> * **What it does:** one-to-one chats, groups of up to 32, business workspaces of up to 50 with channels, and video meetings of up to 8
> * **Privacy:** messages are encrypted on your device before they leave it, and only the recipient can open them. No phone number needed. You sign up with an email and pick a handle. No ads, no tracking, and your data isn’t sold.
> * **Spam control:** a stranger can send at most 3 messages as a request, and calls only ring from accepted people
> * **Source and license:** [https://github.com/panmauk/AltNet-Relay](https://github.com/panmauk/AltNet-Relay), GPL v3
> * **Download:** [panmox.org](http://panmox.org)
>
> **Honest limits:** it’s an early release (launched Oct 16), there’s no phone app yet, the Windows installer is unsigned so Windows will warn you, and \[it hasn’t had an independent security audit, confirm\]. Message contents are encrypted, but \[metadata isn’t hidden: confirm what nodes can see\].
>
> I’m a solo dev, so feedback on the setup, docs and threat model helps a lot. Happy to answer questions here.

---

> **lwh-x**（1 分） · 2026-10-22T01:05:51+08:00　
> https://preview.redd.it/puemzih4ruwh1.png?width=1280&format=png&auto=webp&s=03c39117d7c09c19768b8991feb7f8bfe14a0802
>
> Project Name: Tessera
>
> Repo/Website Link: [https://github.com/Limatura/tessera](https://github.com/Limatura/tessera)
>
> Docs: [https://tessera-docs-three.vercel.app](https://tessera-docs-three.vercel.app)
>
> Description:
>
> Tessera is a file and note sharing server that cleans up after itself. You upload a file, folder, code snippet or link, get a short code and a URL back, and the share is deleted once it expires or has been downloaded as many times as you allowed. Sending doesn't need an account unless you want that.
>
> We used FileCodeBox before this. It's built around anonymous pickup codes, and we kept wanting things it didn't have when we looked: syntax highlighting and previews for code, images, SVG and Mermaid, user accounts with roles and quotas, OIDC login, uploads that go straight to an S3 bucket, and encrypting on the client. So we wrote our own. We use it every day, so it will keep getting fixed.
>
> What's different:
>
> \- accounts are optional, but there if you want them: invite-only or closed sign-up, OIDC, GitHub, Discord, roles, per-account quotas
>
> \- with S3/GCS, uploads go straight to the bucket and plain downloads are redirected there, so big files never pass through your server
>
> \- SQLite, PostgreSQL or MySQL, so it can run on more than one machine
>
> \- storage: local disk, S3-compatible, Azure Blob, GCS, WebDAV. Add several from the admin panel, no restart
>
> \- CLI: \`tessera send report.pdf --expires 24\`, and --encrypt seals the file on your machine. The key lives after the # in the link, so the server never sees it
>
> \- syntax highlighting, image/SVG/Mermaid previews, link preview cards in chat apps
>
> \- optional malware scanning on upload
>
> \- one-time shares are counted in a single conditional DB update, so two people racing for the same share can't both get it
>
> \- OpenAPI spec generated from the server code and checked in CI
>
> Also: expiry, download limits, passwords, folders as one archive, UI in English, Traditional Chinese and Japanese.
>
> It's a single Rust binary and it streams uploads and downloads, so memory use doesn't grow with file size.
>
> Rough edges: it's v0.1.0-rc.1, so not 1.0 yet. The GCS backend has no tests. WebDAV only handles small files. Anonymous uploads are on by default, so read the public example config before you put it on the internet. Back up your database before upgrading, downgrades aren't supported.
>
> Deployment:
>
> Docker image: [ghcr.io/limatura/tessera:latest](http://ghcr.io/limatura/tessera:latest)
>
> Or clone the repo and run \`docker compose up -d\`, then open port 12923. The admin password is printed once in the log: \`docker compose logs tessera | grep password\`
>
> There are example env files for a personal and a public instance, and a systemd unit file.
>
> AI Involvement:
>
> We wrote this post ourselves. AI only proofread it, because English isn't our first language. The code was written with AI tools; a human decides the architecture, reviews the code and does the testing. The agent config files are in the repo (AGENTS.md, .claude/, .codex/) if you want to see how. The app itself doesn't use any AI.
>
> Feedback and issues are welcome, especially what's missing compared to what you use now.

---

> **Free_Permit7170**（1 分） · 2026-10-22T01:42:04+08:00　
> # SkeletonKey: a self-hosted memory layer and agentic HQ for self-observation (self hosting sousveillance and identity maintenance)
>
> [](https://www.reddit.com/r/selfhosted/?f=flair_name%3A%22Wednesday%20Exceptions%22)
>
> App name: SkeletonKey
> GH repo: [https://github.com/CurePortal/SkeletonKey](https://github.com/CurePortal/SkeletonKey)
>
> Most self-hosted projects replace a service, but this one replaces a relationship: the one where someone else owns the whole picture of your life.
>
> Here's SkeletonKey. It’s a private, local-first system that keeps one record of my life — where I’ve been, what I’ve done, the places and people and documents that matter — and gives me the same kind of tools institutions use to build a picture of someone, pointed at myself, with my consent.
>
> Not to watch other people. The whole point is that the eye is mine. It's yours too, with source code openly available for audit and improvement.
>
> **The idea:**
>
> Surveillance is generally asymmetric: someone else gets the cameras, the databases, the analysts, and you get a privacy policy.
>
> **Sousveillance** is the inverse — you watch over yourself, for yourself, and the record belongs to you.
>
> I wanted a system that remembers my days without turning them into a feed, and that can answer “what was that place?” or “did I actually do that?” without sending my life to a vendor cloud.
>
> **What it actually does**
>
> \- A phone beacon. An Android app sends location, battery, and altitude to my own server. It can speak and listen on-device, and run a quiet ambient transcript when I turn that on.
>
> \- A journal that fills itself in. The system turns raw days into a timeline, then into short written recaps. I decide what stays; nothing is published or shared.
>
> \- A map that works offline. Local routing, place lookup, and elevation, so it still works when the signal doesn’t.
>
> \- A watcher, not a nag. It stays quiet unless something is actually wrong: lost signal, reconnect, a geofence, weather, a hazard. No news is good news.
>
> \- An assistant with hands. A local agent can read the record and the map, answer questions, and propose changes. It asks before writing anything. If it notices it’s missing a capability, it can propose a small extension — and waits for a yes before building it.
>
> \- One record. Timelines, places, people, documents, plans, money, and a field log, all in one local store I can export or delete.
>
> **What it is not**
>
> It is not a people-tracker, a social network, a family locator, or a way to build dossiers on anyone else. No ads, no telemetry, no account, no “Pro” tier. It is also not a guru or a replacement for your own judgment; it’s a tool for keeping your own picture straight.
>
> **The self-hosting reality**
>
> I run it on a Linux machine. The pieces are a desktop app, a small Node server, SQLite, and a phone app. Maps are offline (Valhalla), which is great until you see the disk usage. There’s no cloud account and no vendor service.
>
> **The honest hard part is the model.** The quality of the assistant is directly tied to the quality of the model. In my testing, frontier models — Mythos, Sol, DeepSeek 4.1 Flash — were the ones that could actually use the tools reliably. Small local models were not good enough for that job.
>
> **That creates a real trade-off:**
>
> \- Local model: everything stays on your hardware, works offline, but needs serious hardware and may be weaker at multi-step tool use.
>
> \- Cloud model: much stronger assistant, but the context it reads — the parts of your record, location, chat, attachments — leaves your machine and goes to that provider. That breaks the local-only promise in exchange for better processing.
>
> **Status and license**
>
> This is an alpha version, not a polished release. The license is source-available, copyleft-style, and non-commercial: personal and non-profit use is free, corporate/for-profit use and resale need a separate license, and forks/remixes must attribute and notify.
>
> *Developing this project was seen as an extension of the right to bear arms, ie; the citizens of a nation should have access to the same tools and weapons that their government does to protect themselves best against tyranny.*

---

> **Maskio82**（2 分） · 2026-10-22T01:46:53+08:00　
> Carina la tua app, se riesco farò una prova.

---

> **m_jayj**（1 分） · 2026-10-22T02:08:14+08:00　
> https://preview.redd.it/tkp8i1r91vwh1.png?width=1836&format=png&auto=webp&s=aff664c94ecde46a6a10326d2162be0e68ec89b1
>
> Project Name: lb-bot
>
> Repo: [https://github.com/illuminator69/lb-bot](https://github.com/illuminator69/lb-bot)
>
> Description: A self-hosted library gap-filler. If you have ever found music discography a pain in the ass after building your own music library, this will definitely be helpful. Lb-bot indexes your entire Navidrome music library against Musicbrainz and finds missing songs for albums that you have. It also indexes discographies of the artists you have, showing you the albums that you have and don't on one page. If you configure it with your slskd API, you will able to download the missing songs and albums that you do not yet have **straight from an album page**. It also gives you access to discovering new music through Deezer's charts and editor's picks.
>
> It has two companion apps - forks of Feishin and Navic - and a bridge that allows the clients to talk to the lb-bot API (it also enables cross-device controls). Navic is ready for testing, details on the features and how to set it up are here: [https://github.com/illuminator69/navic-gaps](https://github.com/illuminator69/navic-gaps)
>
> Deployment: instructions are at [https://github.com/illuminator69/lb-bot/blob/main/docs/DEPLOYMENT.md](https://github.com/illuminator69/lb-bot/blob/main/docs/DEPLOYMENT.md)
>
> AI Involvement: heavy. The project has been in the works for months and actively debugged. I am looking for people who would like to test it and help flesh it out because so far it has only been tested on my setup only.

---

> **Ahijah**（2 分） · 2026-10-22T02:28:59+08:00　
> **Project Name:** AHP Matrix
> **Repo:** [github.com/Xafloc/ahp-matrix](https://github.com/Xafloc/ahp-matrix)
> **Description:** A decision-making tool based on the Analytic Hierarchy Process. You compare options in pairs, it checks your judgments for consistency and flags contradictions, and a sensitivity view shows how stable the result is. It supports multiple judges, criteria hierarchies, and measured or rated criteria. It imports the Excel Priority Matrix template and exports to Excel/CSV.
> **Deployment:** A single binary (macOS/Linux/Windows) from the Releases page, or `brew install xafloc/tap/ahp-matrix`. Use `--host`, `--port`, and `--data-dir` to serve it on your LAN. Data is stored as plain .ahp.json files. No Docker image yet. Would one be useful?
> **AI Involvement:** Built with AI coding assistance; I designed and reviewed everything.
> **Feedback wanted:** whether a Docker image or multi-user mode would matter to you, and any rough edges on install.

---

> **Front-Necessary7090**（1 分） · 2026-10-22T03:17:45+08:00　
> Project Name: Resurrect
>
> Repo/Website Link: [https://github.com/JathinYanna04/Resurrect](https://github.com/JathinYanna04/Resurrect) (MIT)
>
> Description:
>
> My old Android tablet spent three years in a drawer. Now it runs Vaultwarden, AdGuard Home, ntfy, Syncthing, file sharing and nightly backups, all private over Tailscale with nothing exposed to the internet. Old phones make surprisingly good servers: low power, ARM64, and a built-in battery that works as a free UPS. The hard part is Android itself, which kills background apps, behaves oddly at boot, reuses process IDs and has no systemd. Resurrect packages everything I learned into an installer so any old Android device can do the same.
>
> \- "rez setup" detects the device's memory, storage, architecture and root status, then recommends a profile (Lite, Standard or Full). You can add or remove modules before anything installs
>
> \- 14 optional modules: Vaultwarden, AdGuard Home, ntfy, Tailscale, Cloudflare Tunnel (opt-in), copyparty, File Browser, Syncthing, backups, monitoring, Jellyfin (direct play), LLM-filtered smart alerts, and a battery charge cap
>
> \- No root needed. Without root, AdGuard runs on port 5335 with a small forwarder for your computer; root adds port 53 and the charge cap (pause at 80%, resume at 70%)
>
> \- Private by default: services listen locally and are reached over your tailnet, with logins on everything and Vaultwarden sign-ups closed after your account exists
>
> \- Every download is pinned to a version and checked against a SHA-256 checksum
>
> \- One lock-guarded boot script, so services never start twice, and process checks that survive Android reusing PIDs after a reboot
>
> \- Nightly backups with rotation, a weekly restore test, and an alert if copies stop leaving the device
>
> \- It never roots, flashes or reboots anything. Custom ROM and root steps are documented as optional, manual guides with warnings
>
> \- "--dry-run" on any command shows exactly what would happen without changing anything
>
> Rough edges: it's a pre-release (v0.1.1). Not yet tested on other real devices: Termux:Boot, Tailscale, Jellyfin, root features, and the Android 12+ phantom process killer. A container can't show real Android behaviour, so the docs list exactly what has and hasn't been verified.
>
> Deployment:
>
> It runs inside Termux on the device itself (Android 7+, arm64, armv7 or x86\_64). Install Termux and Termux:Boot from F-Droid or GitHub, not Google Play. Then either:
>
> \- One line: curl -fsSL [https://raw.githubusercontent.com/JathinYanna04/Resurrect/main/install.sh](https://raw.githubusercontent.com/JathinYanna04/Resurrect/main/install.sh) | bash
>
> \- Or clone the repo, read [install.sh](http://install.sh), and run it yourself
>
> \- Or non-interactive: ./install.sh --profile lite --modules vaultwarden,ntfy --yes
>
> No Docker, since it runs natively on the phone. The README covers requirements, profiles and post-install steps, and the docs cover troubleshooting, DNS, remote access, backups, security, rooting and writing your own module.
>
> AI Involvement:
>
> Built with heavy use of Claude Code. I worked out the setup by running it on my own tablet first, decided what to build, and reviewed and tested the changes. CI runs shellcheck, 78 bats tests and 25 Python tests, plus a full real install inside the official Termux Docker image (43/43 behaviour checks) on every push.
>
> Feedback wanted: if you have a spare phone, try it and run "rez device --report" (no serial numbers or addresses), then paste the output into a device report issue. Real-device reports are the most valuable thing right now. Stars and contributors are very welcome too!

---

> **seasl187**（2 分） · 2026-10-22T04:23:52+08:00　
> thx mister =) , I just release a new version with new design and new features

---

> **Repulsive-Eye-8197**（1 分） · 2026-10-22T05:35:38+08:00　
> **Project Name:** Aerini
>
> **Repo/Website Link:**
>
> * Website: [https://aerini.org](https://aerini.org)
> * GitHub: [https://github.com/Panchak2d/Aerini](https://github.com/Panchak2d/Aerini)
> * Documentation: [https://docs.aerini.org](https://docs.aerini.org)
>
> **Description:**
>
> Aerini is a local-first visual workflow engine built with Rust. It lets you build automation workflows by connecting nodes on a canvas, then run them on your own machine or on a server you control.
>
> It is designed for people who want visual automation without depending on a hosted service, as well as developers who want to integrate workflow execution into their own applications.
>
> Some of its features include:
>
> * **Local-first:** No account required, no cloud dependency, and no telemetry.
> * **Visual workflows:** Connect triggers, actions, integrations, and logic nodes to automate tasks.
> * **40 built-in nodes:** Covering triggers, core actions, files and storage, integrations, AI, logic, and utilities.
> * **Plugin system:** Extend Aerini with WebAssembly-based plugins that run in a sandbox.
> * **Local AI:** Connect to Ollama or other OpenAI-compatible servers running on your own machine or network.
> * **MCP support:** Use an MCP server to let compatible AI clients inspect, create, validate, and run workflows, subject to permissions.
> * **Server deployment:** Export workflows for headless execution using `aerini-server`.
> * **Embeddable engine:** Integrate the standalone Rust workflow engine into your own applications.
>
> **Deployment:**
>
> Aerini is publicly released and available for Windows x64, macOS Apple Silicon, and Linux x64/ARM64. It also has a Docker image for the headless server on Linux/AMD64.
>
> You can build workflows in the desktop application and deploy them to a server for unattended execution. Developers can also build Aerini from source or embed the engine in their own applications.
>
> * Downloads: [https://aerini.org](https://aerini.org)
> * Server deployment guide: [https://docs.aerini.org](https://docs.aerini.org)
> * Source code and build instructions: [https://github.com/Panchak2d/Aerini](https://github.com/Panchak2d/Aerini)
>
> **Current status:** Aerini is still in beta, so some bugs and rough edges remain. I've personally tested it on Linux, but I haven't been able to test it on Windows or macOS myself. Reports of issues on those platforms would be especially helpful.
>
> **AI Involvement:**
>
> Aerini includes AI features, including AI workflow nodes and an MCP server for AI clients. For AI assistance used in developing the project itself, I'll disclose the tools and how they were used separately to be transparent.
>
> https://preview.redd.it/ii23i1793wwh1.png?width=1920&format=png&auto=webp&s=659b8892de1b10481154cd14013fe4481be84a4e

---

> **DesignEddi**（1 分） · 2026-10-22T06:45:47+08:00　
> **Project Name:** Hesperan Bots
>
> **Repo/Website Link:** https://hesperan.com, setup guide at https://hesperan.com/bots/server. There's no repo link: it's free, but the source is currently not public.
>
> **Description:** Hi, I'm Eddie, the developer. Quick heads-up first: you need a free Hesperan account to download it. It's for the downloads and updates, and the relay for your devices away from home. Your bots, their data and settings run on your own computer or server, and so does a local model. If you pick a cloud model, the conversation goes to that provider, not to me. hesperan.com only handles your account, downloads and updates, plus an end-to-end encrypted relay so your phone or other devices can reach your bots away from home. At home or over Tailscale your devices talk to the server directly, and the relay only passes encrypted data along. There's no analytics or telemetry in the app.
>
> What it is: a team of AI bots that runs on a Linux box you own and keeps going when your laptop's off. I run it on my home server with my own Claude plan. Each bot has a job, its own model, a memory you can read and edit, and its own browser with a live view. On a server with KVM a bot can also get its own Linux VM, which only sees the internet if you allow it plus one shared folder, nothing on your LAN.
>
> The part I care about most is that it asks. Buying, paying, sending and deleting wait for your approval, spending money is off by default, and Stop everything kills every bot at once. You can loosen that per bot (Careful, Balanced or Hands-off), but money, contracts and deleting for good always ask.
>
> Routines run on a schedule or when something happens, like a new email, a calendar change, a Telegram message or a GitHub event. Bots can also work on code in their own copy of a repo, and you review the changes before anything lands.
>
> Models are set per bot: ChatGPT or Claude plan through the official Codex or Claude Code, installed on the server and signed in with your own account; API keys (OpenAI, Anthropic, OpenRouter, anything compatible); or Ollama on the box or somewhere on your network.
>
> **Deployment:**
> - 64-bit Linux, x86_64 or ARM64, 2 GB RAM (a Pi 5 works)
> - Docker with Compose: `docker compose up -d --build`
> - or Node.js 22.12+ with systemd: `sudo ./install.sh`
> - Data lives in one Docker volume or `/var/lib/hesperan-bots`; backup and restore commands are in the guide
> - Clients are the Mac and Windows apps, plus an iPhone app (TestFlight only) as a companion. Pairing is a one-time link and a 4-digit check
> - On Windows, SmartScreen warns once because the installer isn't code-signed yet: More info, then Run anyway
> - Updates are one click from the app (it rolls back if the new version doesn't start), or `./update.sh`
> - Away from home works without opening a port
>
> It's Early Access (1.3.6), so expect rough edges. The UI is English only, bot VMs need KVM (plenty of rented VPSes don't have it), and you can't move a Mac's bots to a server yet.
>
> **AI Involvement:** I develop it myself, with AI coding assistants. This post was drafted with AI help.
>
> I'd honestly appreciate critical feedback, especially on the account requirement and the relay. Here or at hello@hesperan.com.

---

> **Strong_Student1482**（1 分） · 2026-10-22T07:07:33+08:00　
> Project Name: Opifex
>
> Repo: [https://github.com/radioman18/opifex](https://github.com/radioman18/opifex)
>
> Description: A desktop AI agent builder that runs fully local. Chat with Oppy to design your agent, export structured plans, switch between Ollama/OpenAI/Anthropic. MIT-licensed, no cloud lock-in.
>
> AI Involvement: Built as a vibe-coding project.

---

> **Foreign_Plenty_3521**（1 分） · 2026-10-22T11:01:55+08:00　
> Project Name: ReadyLLM
> Repo: https://github.com/htobty/ReadyLLM (MIT)
> Description: Web UI for the GPU box you don't sit at: SSH targets, VRAM probing, one-click llama.cpp/vLLM/SGLang/ComfyUI install, live monitoring, auto-tuning that boots the server and medians 3 runs (80->110 tok/s on my 4090).
> Deployment: source only, no Docker yet. Would a docker-compose matter?
> AI Involvement: AI coding assistance; I direct, review and test.

---

> **SomeFosterKid**（1 分） · 2026-10-22T12:29:54+08:00　
> https://preview.redd.it/bvytfz765ywh1.png?width=1920&format=png&auto=webp&s=fee22eec18245879e660cd2923f3d1173980671f
>
> **Vemm: an open-source Plex client for Samsung TVs (Tizen 3.0+)**
>
> **My fork (includes all the changes below):** [https://github.com/somefosterkid/vemm](https://github.com/somefosterkid/vemm)
>
> **What it is**
>
> * An unofficial Plex client for Samsung Tizen TVs, by dragoshont.
> * Sideloaded with developer mode; no root needed.
> * Plays through the TV's built-in player: direct play, direct stream or Plex transcoding.
> * Profiles, Home, libraries, search and detail pages.
>
> **Improvements**
>
> * **Buffer settings:** a small minimum buffer (1 s, or 0.5 s), so streams start and seeks resume quickly. (configurable)
> * **Performance:** pictures load ahead of where you're scrolling, plus artwork and library caching for an instant Home on launch.(configurable in settings)
> * **Better seeking:** repeated presses combine into one jump instead of several
>
> **Additions**
>
> * **Theme engine:** Blue, Grey, Black and Pure Black (OLED) themes, with accent colours. WIP
> * **Playlist support**
> * **Built-in keyboard for search**
> * **Intro/credit skipping:** show a button or skip automatically, with per-show settings, similar to plex client.
> * **Seek preview thumbnails** while scrubbing.
> * **Remembers audio and subtitle choices** per show.
> * **Library navigation:** an A–Z jump bar, plus sort and filter.
>
> **Status:** submitted to the original project as pull requests (not merged yet).
>
> You can install it now as "Vemm Preview" from my releases page, either with TizenBrew Installer (enter `somefosterkid/vemm`) or with Apps2Samsung, or build and sideload it yourself using the instructions in the repo.
>
> Its definitely still rough in areas, with some bugs, quirks, and inconsistencies. Overall, its an incredible alternative to the plex client, which isn't great to begin with, and is pretty awful on older tvs. I developed on a 2018 Q6FN on Tizen 4.0.
>
> **Releases:** [https://github.com/somefosterkid/vemm/releases](https://github.com/somefosterkid/vemm/releases)
>
> **Original project:** [https://github.com/dragoshont/vemm](https://github.com/dragoshont/vemm)

---

> **No-Efficiency402**（1 分） · 2026-10-22T13:09:45+08:00　
> SerpApi's pricing page is where my budgets dies for my product's rank tracking
>
> Free tier: 250 searches a month. My project needed hundreds a day while I was d.ebugging. That was gone before the first week of the semester was over.
>
> Next tiers: $25/month for 1,000 searches. $75/month for 5,000. I'm eating instant noodles, not buying a SaaS subscription. Every alternative I looked at was another paid API with the same wall.
>
> I don't need enterprise SLAs or half a million searches a month. I need search results on my laptop while I build my thing, and I need the bill to stay at zero.
>
> So I built SERP Alter Ego. Self-hosted, SerpApi-compatible, MIT licensed, runs on your own machine..
>
> Point your existing SerpApi client at localhost instead of [serpapi.com](http://serpapi.com) and nothing else changes. Same parameters, same JSON response shape, api\_key gets accepted and ignored. Google Search, News, Shopping, Images and Finance.
>
> What I shoved in there:
>
> \- Strict TypeScript, parsers pinned against real captured Google pages. When Google changes their markup (they will), a verify script tells you which selector broke instead of silently returning nothing
>
> \- AI Overview extraction in SerpApi's ai\_overview format, citations included, and it clicks "Show more" before capturing so you get the full answer, not the clamped preview
>
> \- A web UI with search history, a raw HTML archive, and a live toggle between plain HTTP and a headless browser
>
> \- Rate limiting (one request per 2.5 seconds per host), caching, and a robots.txt policy that refuses disallowed paths by default. Flipping that switch is your decision
>
> The honest part, since you'll ask: yes, it scrapes Google. Your IP, your risk. Google will change their markup to mess with you, there's no login because it only binds to [127.0.0.1](http://127.0.0.1), and I make zero uptime promises. It's a student project that grew teeth, not a company.
>
> [https://github.com/themaainuser/SERP-Alter-Ego](https://github.com/themaainuser/SERP-Alter-Ego)
>
> Roast it what's good and bad I'll try to improve it. PRs open.

---

> **TonTuyau**（1 分） · 2026-10-22T15:18:20+08:00　
> Project Name: TonTuyau + Browser Extension LaPompe
> **TonTuyau Repo:** [**https://github.com/TonTuyau/TonTuyau**](https://github.com/TonTuyau/TonTuyau)
> **LaPompe Repo:** [**https://github.com/TonTuyau/LaPompe**](https://github.com/TonTuyau/LaPompe)
>
> **Description:**
> TonTuyau is a selfhostable YouTube-Like plateform that aim to replace TubeArchivist and stop using Jellyfin or Plex as a media center for it (Which can be quite heavy). It can get data from existing TubeArchivist instances to make the replacement way easier.
>
> I've made it to solve multiple problems existing in TubeArchivist. For Example not being able to see more than 10k videos, the lack of real structured page to watch the videos, having a proper way to monitor the channels, videos, their states, the mess I can easily be when you start backuping big channels.
>
> The application is splitted in two parts:
>
> Public pages:
> \- Anyone that could access to a TonTuyau instance will be provided with:
> \- a Homepage to see the most recent videos
> \- Pages for Shorts, Channels, videos and stream
>
> \- Clicking on a video will allow to watch it and its comments if they were backed up
>
> Admin pages:
> Dashboard:
> \- See stats of your instance to see, number of channels, videos, stream, shorts and gone medias
> \- A list of your channel with quick info about what they are containing
> \- A dashboard for each channel to refresh the metadata of itself and its videos as well as a way to download every videos of it
>
> Task:
> \- Run tasks to sync with YouTube, refresh every metadata of your instance, add video, channels, refresh their data
>
> Youtube Configuration:
> \- Check your cookie state
> \- version of the tools (yt-dlp and Deno)
> \- choose the release you want for yt-dlp
> \- configure backup and tasks behavior
>
> API Key:
> \- To allow you to generate a key for your LaPompe extension to backup directly from Youtube pages
>
> **Deployment:** There is a docker compose exemple to selfhost it, the images needed are all available on GHCR and the project is documented
>
> **AI Involvement:** I made it with Claude, I've taken decision on the project structure whiile being backed up by Claude. Claude wrote all the code, my job was to make as much decision as possible for the structure of the project while reviewing the code (Mainly the backend, i'm not a frontend developper).
>
> The goal is to make it better than it is actually, so criticize it, bash it, but constructively. I can't wait to see if people likes it

---

> **ErzenKing**（1 分） · 2026-10-22T17:01:06+08:00　
> Project Name: Overseer (maker here)
>
> Repo/Website: https://github.com/ErzenXz/overseer | https://overseer.sh
>
> Description: A free, MIT-licensed hub for running Claude Code, Codex, Gemini CLI and other ACP agents across your own computers from one browser. I built it to keep track of sessions spread across a laptop, desktop and servers: which are working, finished, or waiting for an approval. It brings output, instructions, diffs and approvals together, with scheduled prompts and live web previews as well.
>
> Deployment: The Go hub embeds the web UI. Pick an always-on computer, install using the Linux, macOS or Windows instructions in the repo, then open the printed URL and set a password. Use Machines → Add machine to connect other computers with the generated command. Workers connect out to the hub. Setup documentation is in the README and docs/guide.md; releases are available from the repository. For remote access use Tailscale, an authenticated tunnel or HTTPS.
>
> The agent runs on the chosen machine, which must remain awake. You bring your existing agent accounts; self-hosting Overseer does not make the underlying model providers local or free.
>
> AI Involvement: Development has been AI-assisted, and AI assisted with this introduction.
>
> I'd appreciate feedback on the installation docs and connecting a second machine, especially on small homelab setups.

---

> **United_Inspector_653**（1 分） · 2026-10-22T17:49:51+08:00　
> Project: Turbo Rumble
>
> I’ve made the source code public, so you can download it, tinker with it and host your own instance for noncommercial use.
>
> It’s a browser racing game for 2–8 players. Put the game on a computer or TV and use your phones as controllers. There’s drifting, rockets, mines and plenty of shared-screen chaos :) Keyboard controls and bots are available too.
>
> Code and setup instructions: [https://github.com/dziksu/turbo-rumble](https://github.com/dziksu/turbo-rumble)
>
> Or just jump in and play: [https://turborumble.rastwork.pl/](https://turborumble.rastwork.pl/)
>
> Deployment: A Dockerfile and Docker Compose example are included. I’m running the public instance on Coolify.
>
> AI involvement: AI coding tools were used extensively during development. The cinematic menu backgrounds are AI-generated; the gameplay screenshot in the README is actual gameplay.
>
> I’d love to hear how the phone controls feel, especially if you try it with friends.

---

> **Unhappy-Ad-4599**（1 分） · 2026-10-22T18:46:14+08:00　
> **Project Name:** Gately
>
> **Repo/Website Link:** https://github.com/wangwanjie/gately · https://gately.cn/en/ (docs in 10 languages)
>
> **Description:**
>
> I'm the author. Gately is an open-source (Apache-2.0) network gateway toolkit for home servers, NAS boxes and small VPSes, in a single Go binary with a Vue web UI. It's inspired by Lucky, a closed-source tool that's very popular among Chinese NAS users. I wanted the thing that holds my DNS API keys and certificate private keys to be auditable, so I wrote an open one.
>
> What it covers:
>
> - **DDNS**: Cloudflare, Route 53, Porkbun, OVH, Gandi, DuckDNS, dynv6, Namecheap, DynDNS2 (No-IP, Dynu…) and several Chinese providers; IPv4/IPv6, IP from URL/interface/command
> - **Reverse proxy / web server**: per-domain proxy, static sites, redirects, HTTPS + HTTP/3, WebSocket, load balancing and health checks, forward auth (Authelia), OIDC/GitHub/Google sign-in, shared users with TOTP and SSO across subdomains, IP allow/deny lists, GeoIP filtering, rate limiting, caching
> - **ACME certificates**: DNS-01 (wildcards) or HTTP-01, auto renewal, then push to other hosts over SSH or restart the Docker containers that use them
> - **Port forwarding** (TCP/UDP, ranges, failover, PROXY protocol) with **SNI routing**, so several services can share port 443
> - **WAF**: Coraza + OWASP CRS v4, with body-inspection limits so WebDAV/cloud drives still work behind it
> - **STUN traversal** for CGNAT/NAT1 setups, UPnP/NAT-PMP
> - Managed **Tailscale/Headscale, frp (client and server), Cloudflare Tunnel**
> - **Docker management**, web terminal (SSH/Telnet + SFTP), WebDAV/FTP, Wake-on-LAN, scheduled tasks, network diagnostics
> - Notifications (Telegram, ntfy, Gotify, Discord, Slack, email…), encrypted scheduled backups, audit log, config history with diff and one-click rollback
> - Passkeys, TOTP, read-only accounts, scoped API tokens with OpenAPI docs, Prometheus metrics + Grafana dashboard, `gately ctl` CLI and an MCP server (read-only by default)
> - Import from Lucky configs and from nginx configs (`nginx -T` output works)
>
> Privacy: no telemetry, no connections to any project server by default, every outbound address (IP lookup, STUN servers…) is visible and can be changed or turned off. Config is plain JSON, so you can keep it in git.
>
> On my own boxes it replaced haproxy + nginx: 90 SNI-routed domains, 27 proxied sites, 75 DDNS records. Benchmarks against that pair (same hardware, 2 cores) are in the README.
>
> **Deployment:**
>
> Docker image for amd64/arm64/armv7:
>
> ```
> docker run -d --name gately --network host \
>   -v ./gately-data:/etc/gately \
>   -v /var/run/docker.sock:/var/run/docker.sock \
>   ghcr.io/wangwanjie/gately:latest
> ```
>
> Then open `http://<host>:16680` (default `admin` / `gately.cn`, change it on first login). There's a Compose example in the repo. Releases also ship static binaries (Linux amd64/arm64/arm/mips/riscv64, macOS, Windows, FreeBSD), OpenWrt ipk/apk packages, fnOS app packages and a systemd unit. Artifacts are cosign-signed with SBOM and build provenance. Install guide: https://gately.cn/en/docs/guide/install
>
> **AI Involvement:** Heavy. Most of the code was written with an AI coding assistant (Claude Code) under my direction. I set the design and scope, review the changes, and test every release on my own servers (an fnOS NAS, a Hong Kong VPS that now runs Gately as its only edge proxy, and an OpenWrt router) before tagging it. The project is young (started in October 2026), so expect rough edges; issues and PRs are welcome.

---

> **oetiker**（1 分） · 2026-10-22T19:29:13+08:00　
> # Inkling: an open-source browser extension that checks spelling and grammar with your own LanguageTool server
>
> Since March, LanguageTool's browser extension is Premium-only: after a 14-day trial it stops underlining mistakes, and LanguageTool says generative AI made the free tier too expensive. The add-on itself has been closed source since 2019. The good part: the LanguageTool *server* is still open source (LGPL) and runs fine on a laptop or a small box.
>
> https://preview.redd.it/o0whevaz70xh1.png?width=1280&format=png&auto=webp&s=783e2888f900ceec3579f8ef1f775623ab7d11d8
>
> So I built **Inkling**, a Chrome and Firefox extension that talks only to the LanguageTool server you choose.
>
> **What it does**
>
> * Marks spelling and grammar mistakes as you type, with a suggestion card to fix them
> * Works in plain text fields, common rich-text editors and Google Docs
> * Language variants per language (de-CH, en-GB, pt-BR, ...), preferred languages, mother tongue, picky mode
> * Per-site on/off, a personal dictionary, ignore or disable rules
> * No account, no trial, no telemetry. Text goes to your server and nowhere else
> * Apache-2.0
>
> **Run a server**
>
>     podman run -d --name languagetool -p 8010:8010 docker.io/erikvl87/languagetool
>
> (docker works the same.) Then install Inkling, enter `http://localhost:8010` in the settings and click "Save and Test". One server on the LAN can serve a whole household or team.
>
> **Links**
>
> * Chrome Web Store: [https://chromewebstore.google.com/detail/inkling/lncfkjkgeoepkinifaggpblhpbenemej](https://chromewebstore.google.com/detail/inkling/lncfkjkgeoepkinifaggpblhpbenemej)
> * Firefox: [https://addons.mozilla.org/firefox/addon/inkling/](https://addons.mozilla.org/firefox/addon/inkling/)
> * Source: [https://github.com/oetiker/inkling](https://github.com/oetiker/inkling)
>
> **Credit where it is due:** Inkling is a fork of the browser extension of [Harper](https://github.com/Automattic/harper) by Automattic. Their team did the hard part: getting the marks to sit on the right words in all those editors. I swapped Harper's built-in English checker for LanguageTool, which adds German and the other LanguageTool languages. If you only write English, try Harper itself: it runs fully in the browser with no server at all.
>
> Bug reports and site compatibility issues are very welcome on GitHub. I am happy to answer questions here.

---

> **Actual_Tradition_990**（1 分） · 2026-10-22T19:48:14+08:00　
> \*\*Disclosure: my project.\*\* Free for your own wedding — not a trial.
>
> We wanted a wedding site without a per-guest paywall or our guest list sitting in someone else's database. So we built \*\*my-boda\*\*: RSVP with invite codes, guest admin with CSV export, schedule/venue/accommodation pages, registry info, five languages, and a private photo gallery where guests upload from their phones and you can export everything as a ZIP.
>
> You run it on a small VPS (\~€3–5/month) or even a Raspberry Pi with Docker. No tracking, no ads, no vendor holding your data. There's an interactive preview on the site before you install anything.
>
> It's source-available and free for non-commercial use; planners who charge for client weddings need a separate license.
>
> \- Preview: [https://my-boda.pages.dev](https://my-boda.pages.dev)
>
> \- Code/setup: [https://github.com/minidevelopments-web/my-boda](https://github.com/minidevelopments-web/my-boda)
>
> Happy to answer questions about setup or whether it fits your wedding.

---

> **Part-Forward**（1 分） · 2026-10-22T21:46:15+08:00　
> # I built an unofficial Android app for Multica, the self-hosted platform for people and AI agents
>
> * **Website and screenshots:** [https://1270011.github.io/multica-android-unofficial/](https://1270011.github.io/multica-android-unofficial/)
> * **Repo**: [https://github.com/1270011/multica-android-unofficial](https://github.com/1270011/multica-android-unofficial)
> * **APK + SHA-256**: [https://github.com/1270011/multica-android-unofficial/releases/tag/v1.0.0](https://github.com/1270011/multica-android-unofficial/releases/tag/v1.0.0)
>
> Hello everyone,
>
> I run Multica ([https://github.com/multica-ai/multica](https://github.com/multica-ai/multica)) on my own server. It's an issue tracker where people and AI coding agents work on the same issues. The upstream mobile app is iOS only, so I built an unofficial Android client.
>
> **\*\*What makes it relevant here\*\***
>
> * No backend of its own and no server address built in. You enter your server URL on first start and test the connection.
> * Notifications \*\*without Firebase / Google Play Services\*\*: an opt-in foreground service keeps one WebSocket to your own server. Nothing goes through a third-party push provider.
> * Private CAs work: certificates installed by the user on the phone are trusted, so no rebuild needed.
> * Optional Cloudflare Access service-token mode for servers behind Zero Trust; plain direct/VPN mode otherwise.
> * No camera, microphone, storage or overlay permissions. Tokens are stored in the Android Keystore.
>
> \*\*What you can do with it:\*\*
> Inbox with filters and bulk actions, Kanban board, issue detail and comments, issue chat, chat with agents, read-only agent run transcripts, projects, workspace switcher.
>
> \*\*Disclosure:\*\*
> Most of the code was written with AI coding agents (Claude Code), coordinated through Multica itself; I reviewed, tested and decided what ships.
>
> \*\*Honest status:\*\*
> This is v1.0.0, built quickly. It works and is usable, but it is not extensively end-to-end tested and it's rough at the edges. Known issues: offline indicator is sometimes wrong, Paste button can be hidden by the keyboard, inbox entries don't always scroll to the right spot, "Unknown Agent" in some issue-chat messages, ARM only, APK signature v2 only. Fixes plus filters/settings/management closer to the web app are planned for v2.0.0.  Tested against self-hosted Multica v0.6.1 (Multica Cloud untested). Same license as upstream (Multica License, Apache 2.0 + additional conditions). *\*\*Not affiliated with or endorsed by Multica / Index Labs.\*\**
>
> I'd love feedback from anyone self-hosting Multica, especially reverse-proxy or VPN setups I haven't tried.

---

> **johnschult**（1 分） · 2026-10-22T23:17:27+08:00　
> **Yagi: share your HDHomeRun with Plex/Jellyfin/Emby on other networks, no firewall tricks**
>
> https://preview.redd.it/z112ay49d1xh1.jpeg?width=1600&format=pjpg&auto=webp&s=15d822729d8b2070173d3f3bc77f48cac35163d0
>
> Ever tried to give a friend or family member’s media server access to your HDHomeRun? `lineup.json` hands out the tuner’s LAN IP, so it just doesn’t work across networks. Yagi sits in front of the tuner and rewrites that address. The remote server adds it like any other HDHomeRun (`host:port`) and needs no NAT or routing rules.
>
> You also get control over who uses it: an allowlist, tuners per viewer, a global cap, and tuners always kept free for you. Anyone over the limit gets a normal HTTP 503, so their software handles it. There’s a live dashboard showing who’s watching what, and 30 days of history. Notifications go to ntfy, Pushover or a webhook. An optional Tailscale-enabled image joins your tailnet as its own device, so nothing needs opening on your router.
>
> * **Repo:** [https://github.com/johnschult/yagi](https://github.com/johnschult/yagi)
> * **Screenshots:** [https://github.com/johnschult/yagi#readme](https://github.com/johnschult/yagi#readme)
> * **Deployment:** [`ghcr.io/johnschult/yagi:latest`](http://ghcr.io/johnschult/yagi:latest) (amd64/arm64), compose example and docs in the repo. MIT.
> * **AI Involvement:** Heavy. I’m a 25+ year software engineer and Claude Code writes nearly all the code, tests and docs under my direction and review. I run it on my own FLEX 4K.
>
> Early software, so please read the security docs before exposing it beyond a network you trust.

---

> **ProgrammingDev**（2 分） · 2026-10-22T23:31:49+08:00　
> **Entoli: an open-source agentic assistant with no server of ours in the middle (AGPL-3.0)**
>
> I got tired of AI assistants where your work goes to someone else's machine, gets processed under someone else's terms, and you take their word for what happened to it. So I built the opposite and spent my weekends polishing it into something I could hand to people.
>
> **What it is:** a general-purpose assistant that runs on your hardware. It calls the model endpoints *you* configure (OpenAI-style or Anthropic, self-hosting and Ollama work fine), and your keys stay yours. There is no server of ours in the path: the only thing you install is the app. Honest caveat for this crowd: your LLM calls still go wherever you point them, that part is up to you.
>
> **Why it exists:** one harness everyone can use for everything. Not a chat wrapper, an actual harness: projects, plans you approve before they run, artifacts you can explore in a built-in viewer, and multi-agent chat projects where you organize and direct several agents on one task.
>
> **What works today:**
>
> - Runs on Linux, Windows, macOS, Android, and iOS (In app review now for iOS)
> - Syncs your work between devices peer to peer, no sync server in the middle
> - Projects keep a job's chats, files, plans, and skills in one place
> - Skills and agents marketplace for the material you need to customize it
> - An optional verification-backed coding workspace that encodes agent-generated code as a mathematical model, searches it for vulnerabilities, and repairs what it finds (this part comes from my day job, I'm a PhD student in formal verification)
>
> **License and source:** AGPL-3.0, fully open. Read every line, fork it, tell me what's wrong with it.
>
> Site and downloads: [byterepair.io/products/entoli](https://byterepair.io/products/entoli)
>
> Happy to answer anything about the architecture, the sync, or the verification pipeline. The list of things I haven't thought of is probably longer than the list of things I have.

---

> **Low-Firefighter-4376**（1 分） · 2026-10-23T00:06:35+08:00　
> Project name: Statement Review — check bank-PDF rows before importing a CSV
>
> Website / free trial: [https://statement-review-trial-20261020.activesnow6.chatgpt.site/?sample=1](https://statement-review-trial-20261020.activesnow6.chatgpt.site/?sample=1)
>
> Description: For a digital bank statement when the CSV you need is unavailable. It extracts candidate rows, shows their original PDF references, lets you correct/include/exclude rows, and checks available balances and printed page counts. A matching closing balance can still hide an omitted debit and refund, so the original needs review. Saved reviews and CSV export are included in the free trial.
>
> Deployment: The hosted trial processes PDFs in your browser, with no document upload or account. A prepared local application ZIP, checksum and README are on the pricing page. It uses a bundled PDF reader and Python 3/static-server helper, with desktop Chrome 145+ required; the fictional workflow was checked in Chrome 155. The local ZIP requires a signed one-user licence, which is not included. This is proprietary software. The proposed local copy is US$19 once and uses the same engine as the free trial. Checkout is closed; scope and delivery timing must be confirmed before payment.
>
> Limits: one bank account, 10 MB / 20 pages, supported digital layouts. No scans/OCR, credit cards, bank connections or QuickBooks Desktop imports.
>
> A reproducible walkthrough imports six fictional rows into Actual Budget’s official demo: [https://statement-review-trial-20261020.activesnow6.chatgpt.site/actual-budget-csv-import](https://statement-review-trial-20261020.activesnow6.chatgpt.site/actual-budget-csv-import)
>
> This is a demo test, not a customer success claim.
>
> AI involvement: AI tools were used to build/test the software and write this post. Jason Ji owns the project.
>
> If you have a current supported statement to enter, try the sample first, then one authorised file locally. The useful result is whether the reviewed CSV reaches your destination’s import preview and where you got stuck. Please do not send financial records or screenshots.

---

> **this_is_SKS**（1 分） · 2026-10-23T01:26:15+08:00　
> * **Project Name:** Camera Planner
> * **Repo/Website Link:**
>    * Try it: [https://home-security-planner-nu.vercel.app](https://home-security-planner-nu.vercel.app)
>    * GitHub: [https://github.com/Sourabh06/home-security-planner](https://github.com/Sourabh06/home-security-planner)
> * **Description:**
>    * It helps users plan their home security
>       * Visualize via 2D(using a flat map) and 3D (on your own wall with the help of AR)
>       * Know about cameras and related information
>       * Plan budget and available cameras
> * **Deployment:** Simply serve the page on HTTPS.  More instructions on README file
> * **AI Involvement:** Heavily vibe coded application via Claude. Doesn't use any AI in its usage.
>
>  I’d love feedback, especially on how well it works on your device.

---

> **JMS1717**（1 分） · 2026-10-23T03:46:50+08:00　
> Ming Voice — A fully local AI voice assistant that responds in ~230ms
>
> I wanted something like Alexa or ChatGPT Voice, but completely local, incredibly fast, and actually capable of controlling my smart home. So I built it!
>
> Project Name: Ming Voice
>
> GitHub: https://github.com/JMS1717/ming-voice
>
> Description:
>
> Ming Voice is an open-source, real-time speech-to-speech assistant powered by inclusionAI's Ming-3.0-audio-tiny model. On my RX 7900 XTX, it starts speaking just ~230ms after I finish talking.
>
> Features include:
>
> - Natural conversations with interruptions and smart turn detection
> - Always-on listening with wake-word support
> - Home Assistant integration for lights, thermostats, media, vacuums, and more
> - Web search, weather, timers, reminders, and persistent memory
> - Hermes Agent integration for more complex tasks
> - Voice cloning and phone access over your local network
> - OpenAI-compatible API
>
> All speech processing and inference happen locally. Optional tools can access external services.
>
> Deployment:
>
> Available now for Linux and Windows 11 (WSL2), with automated one-command installers and setup instructions in the README. Requires a GPU with 16GB+ VRAM. AMD ROCm is supported, with experimental NVIDIA support. No Docker image currently.
>
> AI Involvement:
>
> Built with AI coding assistance, including Codex. The assistant itself uses the open-source Ming-3.0-audio-tiny model. Performance measurements are from testing on my own hardware.
>
> I'd love feedback, especially from anyone interested in testing on different GPUs or integrating it with their self-hosted setup!

---

> **FreeCanadian1**（1 分） · 2026-10-23T04:23:48+08:00　
> I run Homepage for my homelab and kept finding myself in services.yaml at 11pm trying to remember which fields a widget takes, whether I'd used `siteMonitor` or `ping`, and why an icon wasn't showing. So I made **Homepage Editor**: a small container that sits next to Homepage and edits the same config folder in place.
>
> It isn't a replacement dashboard. Homepage still renders everything exactly as before; this just edits the files underneath it, and you can drop back to hand-editing whenever you like.
>
> What it does:
>
> * **"Make it better" checkup:** broken icons, services Homepage has a live widget for that you aren't using, cards with no status check, dead links, duplicates, and API keys sitting in plain text. Most findings have a one-click fix.
> * **Widget helper:** a real form for any of Homepage's 155 service widgets, built from Homepage's own docs, with those docs shown next to the form.
> * **Icon picker** that searches Dashboard Icons, selfh.st, Material Design and Simple Icons, or takes an upload.
> * **Appearance tab:** themes, palettes, backgrounds and card styles, previewed live before anything is saved.
> * **Safe saves:** it merges into your existing YAML, so comments, ordering and commented-out blocks survive. Every save shows a diff first, invalid YAML is refused, and there's a backup before every write.
>
> Install is one compose file (prebuilt image, amd64 + arm64):
>
>     docker compose up -d
>
> GitHub (MIT): [https://github.com/jchisholm59/homepage-editor](https://github.com/jchisholm59/homepage-editor)
>
> It's built against Homepage v1.13.2. Bug reports and "it broke my config" stories are very welcome; that's exactly what I want to hear about before anyone else hits it.
>
> https://preview.redd.it/kb7r1lhbv2xh1.png?width=1600&format=png&auto=webp&s=9707fe0169851e825e3952f0276973ac645a9393

---

> **nick_ian**（1 分） · 2026-10-23T05:59:57+08:00　
> **Project Name:** boardCache
>
> **Repo/Website Link:** [https://boardcache.com](https://boardcache.com)
>
> **Description:** An infinite board for references, research, moodboards and plans. You pin anything on it, images, video, documents, notes, links, whole webpages, draw the connections between them, and see the whole picture. Structure comes when you want it: timelines, tier lists, trees, storyboards, task lists and evidence cases sit on the same canvas as the loose material. It is local-first. Boards live on your device and the app works offline; an account adds the parts that need a server.
>
> **Deployment:** Docker, Electron Desktop clients, hosted web app (https://github.com/boardcache/boardcache/releases).
>
> **AI Involvement:** Developed largely with Claude Opus and Fable models.

## 关联链接

- https://www.reddit.com/r/selfhosted/search/?q=

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
