---
type: "corpus"
item_id: "f94ff575aaf5bc17"
title: "New Project Megathread - Week of 05 Nov 2026"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xox23i/new_project_megathread_week_of_05_nov_2026/"
author: "AutoModerator"
published_at: "2026-11-06T07:01:24+08:00"
captured_at: "2026-11-16T10:02:00+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-06"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - New Project Megathread
metrics: {"score": 39, "comments": 218, "upvote_ratio": 0.9148936170212766}
comments_count: 153
comments_total: 218
discovered_via: "reddit:14d+settle10"
---

# New Project Megathread - Week of 05 Nov 2026

> [!info] 一句话导读
> Welcome to the **New Project Megathread!**

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xox23i/new_project_megathread_week_of_05_nov_2026/>
> 指标：得分=39 · 评论=218 · 赞踩比=0.9148936170212766
> 作者：AutoModerator　|　发布：2026-11-06T07:01:24+08:00
> 项目链接：—
> 采集：2026-11-16T10:02:00+08:00　|　id：`f94ff575aaf5bc17`

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

## 评论（153/218）

> **d__code**（0 分） · 2026-11-06T07:06:51+08:00　
> Hey all! My partner and I share a local AI chat and image generator on my 5090 PC, for anything personal we don’t want going to an AI lab’s servers. I made Ovenlight so we can easily open this and other self-hosted apps privately on our phones, and share other personal apps with close friends, with nothing for them to set up but the app and no ports to forward.
>
> **Project Name:** Ovenlight
>
> **Repo/Website Link:** [https://github.com/snowy-ghost/ovenlight](https://github.com/snowy-ghost/ovenlight) (the connector and both phone apps, Apache-2.0) and [https://ovenlight.app](https://ovenlight.app)
>
> **Description:** You send someone an invite link, they install Ovenlight on their iPhone or Android phone and tap Join, and your app opens full screen on their phone. Their phone can reach only the apps you shared, and the apps stay off the public internet. How it works is you self-host a small connector on the same computer as your apps, which puts each app on your Tailscale network as its own device. Sharing edits your tailnet policy, but it shows you the exact diff and changes nothing until you type yes. Most web apps you already run work, and there are tested recipes for Paperless-ngx, Grafana, Miniflux, Home Assistant (container install) and Open WebUI: [https://ovenlight.app/docs/apps-you-run](https://ovenlight.app/docs/apps-you-run)
>
> You need your own Tailscale account (free for personal use). There’s no Ovenlight account and no analytics, and the connector checks for signed updates once a day with no identifiers.
>
> https://i.redd.it/5lsk5gdcrvzh1.png
>
> **Deployment:** one line on a Mac or Linux with systemd:
>
>     curl -fsSL https://ovenlight.app/install.sh | sh
>
> On Windows 11, in an admin PowerShell:
>
>     irm https://ovenlight.app/install.ps1 | iex
>
> The README has each step by hand. There’s no Docker image for the connector, since it installs as a plain service and updates itself from signed releases, but your apps can stay in Docker (Engine 28 or later) if you publish their port on 127.0.0.1. Then run `ovenlight publish --port 8080 --name "Dashboard"`.
>
> **AI Involvement:** Claude Code wrote all of the code, and every commit says so. The design is my own. Claude helped me draft this comment too.
>
> Please feel free to use! I’d love to hear from people who already share apps with family, and if there’s an app you’d like a recipe for, tell me which. Thanks for reading!

---

> **Amazing-Valuable4580**（1 分） · 2026-11-06T07:21:38+08:00　
> Very nice, thank you! Probably good for most webapps. Sometimes you need native android apps though having certain permissions/reliable notifications and so on. Still the concept of your ovenlight hits the spot of many peoples needs.

---

> **yonto_player**（1 分） · 2026-11-06T07:28:16+08:00　
> Project Name: Yonto Player sync server
>
> Repo/Website Link: https://github.com/yonto-app/yonto-player-sync-server (MIT)
>
> Description: The server behind Sync in Yonto Player, an Android TV / phone player for your own library (Jellyfin, Plex, Emby, SMB/WebDAV shares). Sync keeps watch history, resume points, the watch list and sources in step across your devices. Everything is encrypted on the devices before it's sent, so the server only stores ciphertext: it can't see a title, an address or a password, and a copy of its database shows when devices synced and roughly how much, nothing more. A new device joins by comparing six digits on both screens. The wire format is a public contract (contracts/sync-v1.md in the repo), so anyone can write another server against it. The app's Sync is in beta.
>
> Deployment: Kotlin on the JVM over SQLite, one small container. The README has the Docker run line, a no-Docker route (JDK 25, ./gradlew installDist) and how to point the app at it (Settings → Sync → Your own server). The app side is a free client with one source, and Sync itself is part of Pro, which is a one-time payment. Docs: https://player.yonto.app/docs/sync/
>
> AI Involvement: A lot. I build this solo with AI coding agents. Happy to answer anything about how, and I'd like to hear what a self-hosted sync server is missing for you.

---

> **d__code**（1 分） · 2026-11-06T07:36:07+08:00　
> Thanks, appreciate it! Agreed, Ovenlight is for web apps, so anything that needs a native app’s permissions will always be better as a real app. Though I’ve found a lot of what people tend to self-host is usually a web app, and that’s what I’m hoping to make easier to share. I’m working on notifications and caching now!

---

> **ImL1s**（1 分） · 2026-11-06T07:38:30+08:00　
> **Project Name:** Mergeline
>
> **Repo/Website Link:** [GitLab](https://gitlab.com/aa22396584/gitlab-mobile) (mirror on [GitHub](https://github.com/akari-sora/gitlab-mobile))
>
> **Description:** A free and open source (AGPL 3.0) Android client for your self hosted GitLab, and GitLab.com. You can browse code, reply to issues, review and merge MRs, read CI logs and retry failed jobs, with several accounts and offline copies of saved projects. If your instance uses a company CA, the app can trust that certificate for that one instance after you confirm its fingerprint. An optional AI assistant uses your own API key, including a local endpoint on your LAN, and asks before every write. No developer server, no analytics, no ads; tokens and keys stay in the phone's secure storage. [Screenshots](https://gitlab.com/aa22396584/gitlab-mobile#screenshots) and a [demo video](https://www.youtube.com/watch?v=ikrNOT5f__I).
>
> **Deployment:** Nothing extra to host. It talks to your existing GitLab 18.11 or later over HTTPS. Install the [free APK from the releases page](https://gitlab.com/aa22396584/gitlab-mobile/-/releases); it updates itself from there. Setup notes are in the README. A paid [Play version](https://play.google.com/store/apps/details?id=app.mergeline) exists as a way to sponsor development; the APK is free.
>
> **AI Involvement:** Most of the code was written with AI coding agents under my direction; I designed it and reviewed the changes. In the sub's terms: Implementation, Testing, Documentation and Deployment are Generated, Design and Review are mine. The app itself has an optional AI assistant that is off until you add a provider.

---

> **Sad_Investigator_984**（0 分） · 2026-11-06T09:17:07+08:00　
> Project Name: Hangar
>
> Repo/Website Link: https://github.com/jeffer1312/hangar
>
> Description: One native app and a phone client for all your coding agents: Claude Code, Codex, Pi, omp and Kimi Code. I run 10-15 of them across 4 machines and kept losing the one stuck on a question. Sessions stay as the original CLIs in tmux, and the ones waiting on you go to the top. You can answer from the phone, link machines into one list and open a session in a new worktree. There is no Hangar cloud: nothing goes through a service of mine, though the CLIs still talk to their own providers.
>
> Deployment: A script installs the server, the session shortcuts and the native app (Linux, Windows, macOS), then shows a QR code for the phone. Reach it over LAN or a VPN such as Tailscale; never expose the main port to the internet. No Docker image. Install docs: https://github.com/jeffer1312/hangar#install
>
> AI Involvement: Most of the code was written with Claude Code and Codex, directed by me.

---

> **anitamaxwynnn69**（1 分） · 2026-11-06T09:32:26+08:00　
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

> **theanishtar**（1 分） · 2026-11-06T09:41:07+08:00　
> **I made Davish, an agentless desktop app for monitoring and managing my VPSes over plain SSH (Go + Svelte 5)**
>
> I run a handful of Linux VPSes and got tired of choosing between two options. One was staying in the terminal for everything. The other was installing a web panel like Cockpit or aaPanel on every box, which means another daemon, another open port and more RAM used on small servers.
>
> So I built **Davish**. It’s a desktop app that connects using only your existing SSH setup. Nothing gets installed on the server.
>
> **What it does**
>
> * **Agentless:** reads your `~/.ssh/config` and keys and connects over standard SSH. No server-side install, no extra ports.
> * **Monitoring:** live CPU, memory, disk and process view for each host.
> * **Files + terminal:** SFTP browser (browse, edit, upload) next to your terminal sessions.
> * **Multi-window UI:** laid out like a small desktop OS, with a dock, a status bar and separate windows, so you can keep several servers and tools open at the same time.
> * Builds for Linux, macOS and Windows.
>
> **Stack:** Go backend (SSH channels, SFTP, metrics parsing), Svelte 5 + Tailwind frontend, packaged with Wails v2.
>
> **Current limitations:** \[vd: metrics chỉ hỗ trợ Linux, chưa hỗ trợ jump host/ProxyJump, chưa có bản build ký số cho macOS...\]
>
> **AI involvement:** \[ghi trung thực, vd: “I wrote the Go backend myself and used AI assistance for parts of the frontend and docs” hoặc “No AI used”\]
>
> * Repo: [https://github.com/2hjaito/davish](https://github.com/2hjaito/davish)
> * Releases: [https://github.com/2hjaito/davish/releases](https://github.com/2hjaito/davish/releases)
>
> It’s free and open source (\[license\]). I’d especially like to hear about unusual SSH setups that break it, like bastion hosts, hardware keys or weird shells, and whether the desktop-style UI helps or just gets in the way.
>
> https://i.redd.it/fmbpvvvocwzh1.png

---

> **egfwivbwwruigwrhfbsr**（14 分） · 2026-11-06T10:46:44+08:00　
> **Project Name:** Valet
>
> **Repo/Website Link:** [https://github.com/askvalet/valet](https://github.com/askvalet/valet)
>
> **Docs:** [**https://askvalet.dev**](https://askvalet.dev)
>
> **Live Demo:** [**https://demo.askvalet.dev**](https://demo.askvalet.dev)
>
> **Description:**
>
> Yes, this is yet another homepage dashboard tool... do we really need another?
>
> I love the current projects out there, but I found myself constantly switching between tabs to figure out what was going on. I wanted one place where I could manage everything.
>
> Valet is a homepage that can also do things. Instead of just being a page of links leading you to open 5 other tabs, Valet shows you what's happening in realtime and lets you act on it right from the app.
>
> https://i.redd.it/gcenffkvgwzh1.png
>
> My fav use case for local AI models is managing my homelab because everything stays private (and it helps me justify the GPU cost lol). Valet has a chat agent that works with any model, local or hosted. The AI part is **completely optional**. Valet works great as just a dashboard too
>
> The chat agent knows its own docs, so it can configure itself. Just tell Valet what you want to change about your dashboard and it will modify your config for you (with your approval). I was already addicted to modifying my homepage but this made it way more fun haha
>
> Valet supports:
>
> * 185+ integrations and custom plugins for anything not covered
> * A wall display mode
> * Mobile support (installable web app + push notifs)
> * Reminders (e.g. tell me when the movie finishes downloading)
> * Live activities (upcoming meeting, current streams, downloads, metrics, etc)
> * Year in review, so you can see a recap of your homelab stats for the year
> * 3d model widgets, so you can map out your home or your server and configure it (or like me, just stare at it)
>
> **Deployment:**
>
> One container: ghcr.io/askvalet/valet:latest. There’s a docker run and a compose example in the README, and a quick start + config reference at askvalet.dev. Valet starts locked down (read-only until you sign in or you’re on a trusted network), API keys never reach the browser or the model, and Docker access goes through a read-only socket proxy. You can try everything in the browser demo before installing
>
> **AI Involvement:**
>
> I’m an experienced SWE and used Claude for almost all of the coding, but I designed + reviewed everything and made the architecture decisions. I was very conscious of slop, security, and performance as I wanted to build something enjoyable. But, it’s early so there may be rough edges I haven’t caught
>
> Any feedback is welcome!

---

> **wayings**（7 分） · 2026-11-06T11:02:41+08:00　
> Hi All! I create **xtools** which forked \[IT-Tools\](https://github.com/CorentinTh/it-tools) (MIT) to make it a general-purpose toolbox rather than just a developer one.
>
> What's different:
> \- Tabbed home page by category, favorites and recent tools instead of a wall of tiles
> \- 12 UI languages, auto-detected from the browser
> \- New tools: audio cutter, image cropper, ID photo maker, XML diff (more coming)
> \- Everything runs in the browser; images are never uploaded
> \- Optional self-hosted, cookie-free analytics (Umami), off by default in the Docker image, respects Do Not Track
>
> Self-host:
> \`\`\`
> docker run -d -p 8080:80 wayings/x-tools:latest
> \`\`\`
>
> Demo: [https://xtools.codestudio.uk](https://xtools.codestudio.uk)
> Source: [https://github.com/chenguangming/x-tools](https://github.com/chenguangming/x-tools)
>
> \*\*AI disclosure:\*\* I designed the features and UI and tested everything myself, but most of the code was written with an AI coding assistant (GitHub Copilot CLI). The upstream project is not AI-generated.
>
> Feedback and tool requests welcome.
>
> https://i.redd.it/ucwgom6arwzh1.png

---

> **Ev1dentFir3**（1 分） · 2026-11-06T11:56:16+08:00　
> **Project Name:** RomSeek
>
> **Repo/Website Link:** [https://github.com/Evident-Dev/romseek](https://github.com/Evident-Dev/romseek)
>
> **Description:** RomSeek is a game download manager for RomM. It does for games what Sonarr and Radarr do for TV and movies.
>
> Search your Prowlarr indexers, pick a game, and RomSeek sends it to qBittorrent. When the download finishes, RomSeek imports it into RomM.
>
> * Works out the system for each result from the release name, a list of about 56,000 titles and your past choices
> * Blocks Windows programs and junk files, with an optional ClamAV scan before import
> * Library by system, genre and auto-updating collections
> * Game pages with three steps: get the game, get the emulator, get the BIOS
> * Admin menu to fix metadata, edit details and remove games
> * Stats endpoint for a Homepage widget
>
> **Deployment:** Docker. You need RomM, Prowlarr, qBittorrent and a reverse proxy with a login. The [setup guide](https://github.com/Evident-Dev/romseek/blob/main/docs/setup.md) takes about 20 minutes.
>
> **AI Involvement:** I used Claude for this project for some of the code. UX/UI are my own.

---

> **dvirby**（1 分） · 2026-11-06T12:15:11+08:00　
> Hey everyone,
>
> I built Developer Shield an open-source desktop app created specifically for devs and homelab enthusiasts who want to scan their local network without sending any telemetry or data to the cloud.
>
> Key Features:
>
> \- Zero-Knowledge Local Scanning: Everything stays strictly on your local network/LAN.
>
> \- Custom Rules Engine: Define your own security checks and scan targets.
>
> \- Local LAN Sync: Sync scan reports across your local machines securely.
>
> \- Built with Tauri & React for a lightweight footprint.
>
> I’d love to get feedback from this community on features you'd like to see or custom rules that would be useful for your setups!
>
> GitHub: [https://github.com/dvirby6/developer-shield](https://github.com/dvirby6/developer-shield)

---

> **hinzwifi**（4 分） · 2026-11-06T12:40:50+08:00　
> This look cool, we always need another homepage HAHA

---

> **xlollx**（2 分） · 2026-11-06T13:27:16+08:00　
> Project Name: Trackhop
>
> Repo/Website Link: [https://github.com/xlollx/Trackhop](https://github.com/xlollx/Trackhop) · [https://trackhop.org](https://trackhop.org)
>
> Description: Trackhop keeps playlists in sync between music services: your own Navidrome/Subsonic, Jellyfin or Plex on one side, Spotify, YouTube Music, Apple Music, TIDAL, Deezer and others on the other. Pick a playlist and a target and it keeps them identical on a schedule (hourly, daily, weekly), optionally mirroring removals, instead of a one-time transfer. Songs it can't match go to a review screen with suggestions. It also does duplicate removal, backups and CSV/M3U import/export. No account, no telemetry, no server of mine in between: logins stay encrypted on your own machine. AGPL-3.0.
>
> Deployment: Docker image with a small web UI (still beta), so it can run on a NAS or home server and keep, for example, a Spotify playlist mirrored into Navidrome. Docker run and compose instructions: [https://trackhop.org/guide/docker](https://trackhop.org/guide/docker). There's also an Android app and a desktop app for Windows/macOS/Linux using the same engine.
>
> AI Involvement: A lot. Most of the code was written with Claude Code. I decide what gets built, test every release on real accounts and servers, and review the changes, and there's an automated test suite plus a VirusTotal scan of every release. I'd rather say it up front: judge it by whether it works for you.
>
> Feedback and bug reports are very welcome on GitHub issues.
>
> https://i.redd.it/mgbr2o63hxzh1.jpeg

---

> **ClassyLion**（6 分） · 2026-11-06T16:15:02+08:00　
> **Project Name:** eraser
>
> **Repo:** [https://github.com/drumandbytes/eraser](https://github.com/drumandbytes/eraser) (docs and broker directory: [https://eraser.drumandbytes.dev](https://eraser.drumandbytes.dev))
>
> **Description:** Sends GDPR/CCPA opt-out requests to 700+ data brokers from your own mail account, so you don’t pay an Incogni/DeleteMe-style subscription. It runs entirely on your machine: your details stay in a local config and history database, nothing goes through a service of mine, and there is no account or telemetry. It resends each broker every 25 days within your mail provider’s daily cap, reads the replies over IMAP and shows which brokers need a manual step (confirmation links, forms). `eraser serve` gives a local web UI with a setup wizard; there is also a CLI. It’s a maintained continuation of digisamroc/eraser (inactive since early 2026) with EU/EEA handling (GDPR Art. 17, data protection authority list, evidence export for complaints).
>
> Honest limits: many brokers just comply by email, but some want a link click, a web form or ID verification, and eraser only tracks those, it can’t do them for you.
>
> **Deployment:** No server needed. One static Go binary (no Docker image, since it needs your mail credentials and runs on your desktop/NAS as a user): `brew install --cask drumandbytes/tap/eraser`, or grab a binary for Linux/macOS/Windows from the releases page, or `go install github.com/drumandbytes/eraser/cmd/eraser@latest`. Then `eraser serve` ([http://localhost:8080](http://localhost:8080)) and follow the wizard. `eraser schedule install` has your OS run it every 6 hours; `eraser auto` is a foreground loop. Works with Gmail, Proton (via Bridge), Fastmail, [mailbox.org](http://mailbox.org), Posteo, iCloud, SES or any SMTP/IMAP. MIT.
>
> **AI Involvement:** Built with an AI coding assistant (Claude). I review and test what gets published. There is also an optional, experimental `eraser mcp` mode that lets a local AI agent draft follow-ups, but every batch needs your explicit approval, and it is off unless you set it up.

---

> **kamahell87**（0 分） · 2026-11-06T16:15:19+08:00　
> **Project Name:** kovi
>
> **Repo:** https://git.sysmd.uk/mdaleo404/kovi
>
> **Description:** A self-hosted dashboard for your KOReader reading stats. It gives you a cover-first library, a reading heatmap and daily reading-time graph, a calendar view, and your actual highlights and notes synced from the device. Covers are fetched automatically (Open Library, Google Books, Calibre). You can import your `statistics.sqlite3` by drag-and-drop or use the KOReader plugin for incremental LAN sync. There's also one-click backup and CSV/Markdown export. It's a single Node process with one SQLite file, so no external DB.
> The tool was inspired by the now archived KoInsight.
>
> **Deployment:** Released (2026.10.09), GPL-3.0, with a README covering install, plugin pairing and config. Run `docker compose up --build -d` with the included compose file, or use Node 22+ and `npm start`, or use the already built image. There's no built-in login, so keep it on your LAN or behind an authenticated reverse proxy.
>
> **AI Involvement:** Heavily developed using AI, but designed and reviewed by human (I can't code this kind of things, but I can definitely add some constraints).

---

> **alex0ptr**（0 分） · 2026-11-06T16:23:31+08:00　
> https://i.redd.it/oh86k46wqyzh1.png
>
> **Project Name:** AI Gude
>
> **Repo/Website Link:** [https://github.com/alex0ptr/aigude](https://github.com/alex0ptr/aigude) Live demo: [https://aigude.alexdoes.dev](https://aigude.alexdoes.dev/) (user `demo`, password `demo`)
>
> **Description:** AI Gude is your own morning podcast built from the RSS feeds you follow. "Ei Gude" is Hessian for good morning.
>
> *The problem:* I follow more feeds than I have time to read, but I have time to listen while making coffee or commuting. Generic news podcasts don’t cover what I actually care about.
>
> *What it does:* At the times you pick, AI Gude fetches new articles from your feeds, retrieves their full text, writes a script in the style you describe and narrates it. You get one audio episode with chapters (one per topic), made for listening on your phone.
>
> *Features:*
>
> * Multiple shows per user, each with its own feeds, schedule, language, voice and style prompt
> * Articles are never told twice; deleting an episode gives its articles back
> * Missed schedules are made up on startup; failed episodes stay in the list with their reason and can be retried
> * Shows are configured in TOML files that are hot-reloaded, with an in-browser editor and a `validate` command
> * Multi-user via a reverse proxy header (Traefik Basic Auth example in the README), plus a read-only demo mode
> * Automatic retention cleanup and a usage meter per episode (tokens, crawled pages)
>
> **Deployment:**
>
> * A single Go binary with SQLite and ffmpeg, plus a Dockerfile in the repo
> * The README has a Getting Started guide, configuration how-tos and an example config with every setting commented
> * An Ansible collection installs it on Ubuntu 24.04 / Debian 13 with rootful Podman as systemd quadlets, optionally with Traefik (HTTPS + auth) and a self-hosted Firecrawl
> * Requirements: a Gemini API key (script + voice) and either the hosted Firecrawl or your own instance
>
> **AI Involvement:** AI is a core feature: Gemini writes and narrates the episodes. The Go code was written with AI assistance and reviewed by me (software architect by trade). The Ansible collection was generated by AI and has been run on a host but not reviewed, which the README states openly.
>
> **LOOKING FOR: self-hostable TTS** The voice is the part I most want to bring home. I’m looking for a TTS model that holds up over 10-minute episodes in **German and English**, ideally on CPU or a small GPU. Piper, Kokoro, XTTS, F5-TTS, Chatterbox: what actually still sounds good after a few minutes? TTS sits behind a small interface, so a good suggestion has a real chance of becoming a backend.

---

> **zlaya31**（0 分） · 2026-11-06T16:34:23+08:00　
> **Project Name**: tdeemon
>
> **Repo/Website Link**: [https://github.com/tdeemon/tdeemon](https://github.com/tdeemon/tdeemon)
>
> https://i.redd.it/yn0pa79geyzh1.png
>
> **Description**:
>
> A self-hosted calorie and macro tracker that you can just tell what you ate.
>
> I kept quitting calorie tracking because logging was a chore: fifteen entries for "chicken breast", type the grams, repeat for every ingredient. So the main goal was that logging takes seconds. tdeemon has an MCP server built in, so I connect it to Claude (or Codex, or a local model) and write "200 g skyr, a banana and my usual coffee". It finds my foods, logs them and does the math. The model only calls tools, it never calculates anything itself. In the app, the foods I eat at that meal come first, yesterday's meal is one tap, recipes are logged as a portion, and barcodes work with Open Food Facts.
>
> The other half is the numbers. Instead of guessing your TDEE from a formula, it measures it from what you ate and how your trend weight moved, and tells you whether your cut or bulk is on pace. Plan changes (from a weekly review or the AI) come as proposals you accept or reject, within hard limits in the code, and anything can be undone.
>
> Also: Apple Health via Health Auto Export (weight, sleep, workouts), a morning summary as a push notification or on Telegram, multiple users and shared households, an installable PWA with dark mode, English and Croatian.
>
> Not there yet: imperial units, Android health data, and [claude.ai/ChatGPT](http://claude.ai/ChatGPT) connectors (they need OAuth).
>
> Screenshot: \[the day on a desktop\]([https://github.com/tdeemon/tdeemon/blob/main/docs/screenshots/desktop-day-dark.png](https://github.com/tdeemon/tdeemon/blob/main/docs/screenshots/desktop-day-dark.png)), and more in the \[tour\]([https://github.com/tdeemon/tdeemon/blob/main/docs/features.md](https://github.com/tdeemon/tdeemon/blob/main/docs/features.md)).
>
> **Deployment**:
>
> \- Docker image: \`ghcr.io/tdeemon/tdeemon\`
>
> \- Docker Compose file with optional Caddy for HTTPS; the README's "Run it" section takes about five commands
>
> \- "Try it" in the README starts it with a demo user and three months of fake data, if you just want to look around
>
> \- One Go binary with SQLite, so one container and one file to back up
>
> \- Docs: \[self-hosting\]([https://github.com/tdeemon/tdeemon/blob/main/docs/self-hosting.md](https://github.com/tdeemon/tdeemon/blob/main/docs/self-hosting.md)) (configuration, OIDC, devices, backups, upgrades), \[AI coach\]([https://github.com/tdeemon/tdeemon/blob/main/docs/ai-coach.md](https://github.com/tdeemon/tdeemon/blob/main/docs/ai-coach.md)), \[how the numbers work\]([https://github.com/tdeemon/tdeemon/blob/main/docs/methodology.md](https://github.com/tdeemon/tdeemon/blob/main/docs/methodology.md))
>
> \- AGPL-3.0, no telemetry, full export as JSON/CSV
>
> AI Involvement: The code is written by AI agents (mostly Claude Code). I designed what it does and how it works, and I use it every day. Every change goes through tests, CI, linters and CodeQL, all in the repo, but I haven't reviewed the code line by line. The app works fully without AI; the MCP server is optional.
>
> Feedback very welcome, especially whether the install worked from the README alone.

---

> **wouek**（1 分） · 2026-11-06T17:22:42+08:00　
> * **Project Name:** CartVibe
> * **Links:** [GitHub](https://github.com/wouekk/cartvibe) · [Live Demo & Site](https://cartvibe.app/) (resets, nothing saved)
> * **Description:** A self-hosted vibe-coded family app for live-syncing shopping lists, receipt scanning, and household budgeting (groceries, bills, leisure) built for my own use. It's a fork of ReceiptWrangler which was a bit too complex for my personal use.
>    * **Shopping & Receipts:** Live-synced lists across phones, recipe imports, and photo/PDF receipt extraction with exact-cent math validation.
>    * **Budget & Extras:** Monthly goals, impulse-buy tracking (off-list items), Open Food Facts barcode scanner (Nutri-Score/NOVA), warranty reminders, multi-currency, 5 languages (I checked English and Polish by hand), and PWA install.
>    * **Optional AI:** Works 100% manually. You can bring your own key (Claude, Gemini, OpenAI, or local via Ollama/LM Studio) for receipt OCR and item health/category tagging. Retries if offline; costs <$0.01/receipt.
> * **Deployment:** [`ghcr.io/wouekk/cartvibe:latest`](http://ghcr.io/wouekk/cartvibe:latest) (Go API + nginx + SQLite in one container, plus Valkey). Needs just a compose file and two `.env` keys.  I've asked Claude to provide guides in the README and checked or Synology and VPS (Caddy/Litestream/restic).
> * **AI Involvement:** High, and I'd rather be upfront about it. This is a fork of [Receipt Wrangler](https://github.com/Receipt-Wrangler/receipt-wrangler) (AGPL-3.0, credit to Noah Hall & contributors) that I modified (or rather completely reworked) using Claude Code for my own household (first release Oct 21, 2026). I run it daily on my Synology NAS and tested changes manually.
> *  It started as a hobby project using my Claude Pro trial, I ended up staying up until 3AM just watching Claude code for me and juggling limits. After 3 days I decided to get Max (you can see it by the number of Commits)
>
> Please feel free to use it and log any issues / request via Github I would greatly appreciate your feedback. Currently working on iOS app - hoping to monetize it in the future. SelfHosted stays free for eternity.

---

> **rutinja**（1 分） · 2026-11-06T17:38:00+08:00　
> **Project Name:** Twigex
>
> https://i.redd.it/cjw1igmppyzh1.png
>
> **Repo/Website Link:**
> **- Code:** [https://github.com/twigex/twigex](https://github.com/twigex/twigex)
> \- **Website and docs**: [https://twigex.com](https://twigex.com) (install guide: [https://twigex.com/docs/installation](https://twigex.com/docs/installation))
> **- Docker Compose**: [https://github.com/twigex/twigex-docker-compose](https://github.com/twigex/twigex-docker-compose)
> **- Helm chart:** [https://github.com/twigex/twigex-helm-chart](https://github.com/twigex/twigex-helm-chart)
>
> **Description:**
>
> Most teams end up paying and using different tools: Google Drive or Dropbox for files, Slack for chat, Zoom for calls, Asana or Trello for tasks, and a BI tool for dashboards. Each one has its own logins, permissions and copy of your data, usually on someone else's servers.
>
> Twigex puts all of that in one self-hosted app.
>
> **-Files** (instead of Drive/Dropbox): folders, edit Word/Excel/PowerPoint in the browser (Collabora or EuroOffice), share with people (viewer/editor/manager, expiry), public share links with password, expiry and upload-only mode, trash and restore, activity log, custom metadata
>
> **- Chat and calls** (instead of Slack/Zoom): public and private channels, direct messages, threads, reactions, attachments, video calls and screen sharing (LiveKit)
>
> **- Projects** (instead of Asana/Trello): workspaces with tables, custom fields, task assignment, statuses, subtasks, calculations, Kanban view
>
> **- Analytics** (instead of a separate BI tool): connect a database, build charts and dashboards (Cube)
>
> **- Admin:** user management, SMTP, MFA, password and session policies
>
> The core is open source under AGPLv3, and the free Community Edition has no user limit. There's an optional paid license for things like SSO, LDAP/AD sync and role-based access control, but nothing you need to run it.
>
> **Deployment:**
> Three options, all documented:
> \- Docker Compose: \`git clone\`, run \`generate-secrets.sh\`, \`docker compose up -d\`. Includes MariaDB, Redis, document editing, video calls and analytics.
> \- Helm chart for Kubernetes.
> \- Single binary for Linux, if you already run MySQL/MariaDB and Redis.
>
> Requirements: MySQL 8 or MariaDB, and Redis. LiveKit, the office server and Cube are optional and only needed for their features.
>
> **AI Involvement:** The core of Twigex was written by our team without AI. We now use Claude to help and every change is reviewed by a person before it's merged.
>
> Questions and feedback are welcome on r/twigex

---

> **Applekim4S**（0 分） · 2026-11-06T17:53:42+08:00　
> **Project Name:** Luma Music
> **Repo/Website Link:**
> https://github.com/GimGyumin/Luma-Music
> **Description:**
> Hi everyone!
> I’ve been working on Luma Music, an open-source iOS music player based on Cassette, designed for Navidrome and other OpenSubsonic-compatible servers.
> I started this project because I wanted something that felt closer to Apple Music while still letting me use my own music library.
> I’ve spent a lot of time working on the interface, animations, playback experience, and performance.
> Some of the main features include:
> An Apple Music-inspired interface with smooth animations and artwork-focused album pages.
> Immersive album artwork on supported covers.
> Synchronized lyrics with TTML word-by-word highlighting.
> Optional AI-powered lyric translation using Apple or OpenAI services.
> Pronunciation support when the available lyrics include pronunciation data.
> Gapless playback, lossless audio, crossfade, and ReplayGain.
> Offline downloads and caching.
> Siri, Shortcuts, and other Apple ecosystem integrations.
> Lyrics depend on what your server or a supported lyrics provider can supply, so not every track will have synchronized lyrics or translations.
> I’ve also been putting a lot of effort into battery efficiency. Some recent optimizations have significantly reduced power consumption during playback in my own testing, although I’m still testing under different conditions.
> My main goal is to make listening to a self-hosted music library feel as polished and enjoyable as possible.
> **Deployment:**
> Luma Music is currently available as an IPA for iPhone and iPad.
> You can download the latest available release from GitHub:
> https://github.com/GimGyumin/Luma-Music/releases
> To install it, you’ll need a compatible sideloading solution such as AltStore or SideStore. Once installed, connect it to your existing Navidrome or compatible music server.
> There’s no Docker image because Luma Music is a client app, not a music server. You’ll need to host your own server separately.
> The current public release is RC1, with further improvements planned for the next release. A macOS version is also planned for next year (2027).
> **AI Involvement:**
> I want to be transparent about this.
> I used AI tools to help with parts of the development process, including coding, debugging, and documentation. I also use AI to help investigate problems and improve the app.
> The project is based on the open-source Cassette player, and I’ve been building and modifying it to create the experience I wanted.
> I’m actively testing the app myself and working on improving its stability, performance, and overall experience.
> I’d really appreciate any feedback, especially from people who already use Navidrome.
> Also, English isn’t my first language, so I used AI to help translate and polish this post. Sorry if any of the wording sounds a little unnatural, and thanks for understanding!
>
> https://i.redd.it/5y0czi3msyzh1.jpeg

---

> **PeepSoWP**（1 分） · 2026-11-06T18:35:44+08:00　
> For Twigex, the file/chat permission boundary would be useful to demonstrate. Share a file in a private channel, remove one member, then have that person retry the original attachment URL from an already open tab and after signing in again. If channel membership granted the file access, removing that membership should remove that route too.
>
> If a separate direct file share intentionally keeps access alive, make that grant visible to the administrator. Otherwise removing someone from a conversation can look like it revoked access when it only hid the conversation. How do attachment permissions follow changes to channel membership today?

---

> **PrestigiousAd1122**（8 分） · 2026-11-06T20:41:30+08:00　
> **Project Name:** LabLantern
>
> **Repo/Website Link:** [https://github.com/noah-ebrt/LabLantern](https://github.com/noah-ebrt/LabLantern)
>
> https://i.redd.it/en1vcuzhmzzh1.png
>
> **Description:** i got tired of reading cve news every day just to find out if any of it actually hit my homelab, so i built this. it scans my linux hosts, container images and appliances daily (grype + osv), flags what's actively exploited or exposed to the internet, watches security news and release feeds for early warnings, and only pings me when something actually affects my setup, along with the exact fix command. runs fully local, the agents open no ports, and anything dangerous needs your passkey.
>
> **Deployment:** docker compose, with a one-line installer: `curl -fsSL` [`https://raw.githubusercontent.com/noah-ebrt/LabLantern/main/install.sh`](https://raw.githubusercontent.com/noah-ebrt/LabLantern/main/install.sh) `| sh` (or clone it and run `./install.sh`). Setup and docs are in the README.
>
> **AI Involvement:** built with a lot of help from AI (Claude Code). I made the design decisions, tested and reviewed everything, and run it daily on my own homelab.
>
> feedback welcome :)

---

> **bj_davey**（1 分） · 2026-11-06T20:47:37+08:00　
> **Project Name:** LocalFind: Files/Media Semantic Search Finder App
>
> **Deployment:** 🤖 [Get it on Google Play](https://play.google.com/store/apps/details?id=com.localfind)
>
> **Description**:
>
> * Search your files by meaning in 100+ languages to find a video moment, an audio snippet, a PDF page, a photo, or a text passage
> * Search with a photo: Find similar photos and matching video scenes.
> * 100% offline, local, free, open source, and private. No account, no ads, no analytics, no cloud services.
> * Accelerated by NPU (AI Hardware) if your phone supports it; otherwise, fallback to CPU/GPU
> * Builds on Google Edge AI EmbeddingGemma 2 model
>
> **Repo/Website Link: 💾** [Source Code](https://github.com/bjdavey/localfind)  🌐 [Website](https://bjdavey.github.io/localfind/)
>
> **AI Involvement:** Agentic engineering (mostly AI, with real development history and hands-on human testing)
>
> **I'd be glad to answer any questions. Also, any feedback, features/ideas, or bug reports are highly appreciated.**
>
> https://i.redd.it/vmsrt40hnzzh1.png

---

> **ElderHare**（0 分） · 2026-11-06T20:58:13+08:00　
> Project Name: Reelix
>
> Repo/Website Link:  [https://www.github.com/demonzoned/Reelix](https://www.github.com/demonzoned/Reelix)
>
> Description:
>
> Reelix is a single self-hosted app that replaces Radarr, Sonarr, Prowlarr, Readarr, Lidarr and Jellyseerr. It's one Rust binary with one database, one login, one web UI and one API, so there are no API keys to wire between apps and nothing to keep in sync.
>
> ￼​- Library management: movies, TV, ebooks, audiobooks and music, with monitoring, search, automatic grabs, imports, renaming and hardlinks.
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
> Deployment: Version 0.8.5 is released, with prebuilt binaries for Windows and Linux on GitHub Releases ([https://github.com/demonzoned/Reelix/releases](https://github.com/demonzoned/Reelix/releases)) and a Docker image at ghcr.io/demonzoned/reelix:latest. The README has a docker-compose example, setup steps for Windows, Linux and building from source, and a first-run guide. Docker setup is a single container with one /data mount (so hardlinks work) and port 7700.
>
> •	⁠AI Involvement: Heavy.  Claude is a collaborator on the project.  AI did the coding work for me.

---

> **ZXY101**（7 分） · 2026-11-06T21:06:59+08:00　
> **Project Name: yt-dlp-z**
>
> **Repo/Website Link:** [https://github.com/ZXY101/yt-dlp-z](https://github.com/ZXY101/yt-dlp-z)
>
> https://i.redd.it/jiu3ajdsozzh1.png
>
> **Description:** Yet another self-hosted front end for yt-dlp, allows you to use every yt-dlp option but also adds some additional features such as waiting for a livestream to start or subscribing to channels and downloading all new uploads.
>
> This works well as an easy ui for downloading youtube videos but was mainly built for the purpose of archiving live streams, you can download live chat and format it into a sub file that displays it nico-nico style.
>
> Also added a mcp server and skill if you want your favorite LLM to handle everything.
>
> Bunch of other little features like presets, ntfy notifs and media server compatibility but I wont bother trying to name everything here.
>
> **Deployment:** One Docker container, with images for amd64 and arm64 on GHCR (ghcr.io/zxy101/yt-dlp-z)
> Can also run without Docker, using Node, uv, FFmpeg and Deno.
>
> **AI Involvement:** Fully slopped. This project was just an excuse to see how AI performs in a proper project given extensive guidelines. I enforced a bunch of code standards and test requirements, an extensive plan and then tested everything it said it did. I hate how well it came out, I'm a dev who hates AI and I'm just trying to figure out how to keep my job in the future man.

---

> **Dull-Demand-1871**（3 分） · 2026-11-06T21:23:07+08:00　
> **Project Name:** Kith
>
> **Repo/Website Link:** [https://github.com/dreed47/kith](https://github.com/dreed47/kith) · [https://kithgenealogy.org](https://kithgenealogy.org) (1-minute video tour) · AGPL-3.0
>
> **Description:** A private family history website you host yourself, built for your relatives and not just the researcher. Person and family pages, charts (hourglass, fan, descendants), photos with face tagging, census by year with suggested matches, places and family maps, and GEDCOM export. Bring your tree from Ancestry, MyHeritage, FamilySearch, Geneanet or WikiTree: upload their GEDCOM or .zip file, preview it, and undo the import any time. Living people are hidden from anyone who shouldn't see them. Relatives can ask for an account and mark "this is me". Five themes, including dark and large print, and it works on phones. It's an alternative to paying a cloud tree site every month. Coming from TNG? Your whole site moves over in one command, user accounts and passwords included.
>
> **Deployment:** A one-line Proxmox LXC installer (recommended), Docker Compose, or step-by-step Debian. Python/Flask on MariaDB. Install and update steps are in the README. It comes with a made-up sample family so you can try it right away.
>
> **AI Involvement:** Most of the code was written with Claude. I decide what gets built, then review and test every change, and the tests cover 100% of lines and branches. It runs my own family's site every day.
>
> Privacy note: no ads or analytics. The README lists every outside connection. The only one on by default is a daily version check (a random ID and the version number), and you can turn it off with one checkbox.
>
> Feedback welcome, especially from anyone moving off a cloud tree site.
>
> https://i.redd.it/cmwezzgouzzh1.png

---

> **fmercurio**（1 分） · 2026-11-06T21:27:20+08:00　
> Project Name: CapRover Operator for Hermes (MIT, development release)
>
> Repo / installation docs: [https://github.com/fmercurio/hermes-caprover-operator](https://github.com/fmercurio/hermes-caprover-operator)
>
> Description: I built this for people who already run apps on CapRover and want to manage an image update through Hermes Agent. It handles one existing, owner-configured app: save a plan for an image pinned by digest, require native approval, check whether the app changed since planning, then attempt the deployment.
>
> The failure case I focused on is a deployment accepted by CapRover whose acknowledgement never reaches the client. The plugin records the plan as consumed before a possible write. That record survives restarts, so the same plan cannot trigger another deployment attempt. An explicit read-only reconciliation then checks what the server is running.
>
> A disposable lab updated CyberChef 11.4 to 11.5, deliberately dropped the acknowledgement, restarted Hermes and checked replay refusal, the requested running image, one replica and HTTP 200. This is a recorded experiment, not production experience. HTTP success alone is not treated as proof that the new image is serving traffic. There is no automatic rollback or database migration validation.
>
> Deployment: Install into your own Hermes environment with \`hermes plugins install fmercurio/hermes-caprover-operator\`. The README covers Linux/macOS, Python 3.11+, Hermes requirements, interactive approvals, and configuration of an existing HTTPS CapRover server/app and token. It is a plugin, not a separate hosted service or Docker dashboard. Model hosting depends on your Hermes configuration.
>
> AI Involvement: AI agents assisted implementation, tests, this comment and the demo. The demo uses synthetic narration and stylized diagrams of the recorded lab; authorized automation operated native approval during that test.
>
> 64-second demo: [https://x.com/ztock/status/2118680536600269045](https://x.com/ztock/status/2118680536600269045)
>
> I’m entering it in the Hermes Plugin Hackathon and would welcome feedback on the deployment evidence and recovery workflow, especially from other CapRover users.

---

> **AleDev99**（0 分） · 2026-11-06T22:00:54+08:00　
> **Project Name:** pulseping-lite
>
> **Repo/Website Link:** https://github.com/alessio1999xx-debug/pulseping-lite (MIT)
>
> **Description:** Single-file uptime + TLS expiry check for cron. For a few internal services I didn't want a full monitoring stack, just cron telling me if a URL or host:port is down, or if a TLS cert is about to expire. One Python file, stdlib only (3.9+), no pip install. HTTP(S) check (status < 400 = up) or plain TCP for host:port; optional --tls days-left with --warn-days (default 14); plain text or --json; exit 0/1/2. What it doesn't do: one target per run, no alerts, no history, no dashboard. It exits non-zero and you decide (cron mail, a script, a failed CI job). Disclosure: I made this, it's my own small open-source project.
>
> **Deployment:** Download the one file and run it. Example: `curl -fsSLO https://raw.githubusercontent.com/alessio1999xx-debug/pulseping-lite/main/pulseping_lite.py && python3 pulseping_lite.py https://example.com` — or drop it on a server and cron it: `*/5 * * * * python3 /opt/pulseping_lite.py https://example.com/health || echo "check failed" | mail -s uptime you@example.com`. README has a terminal demo GIF and real measured output. No Docker needed (it's a cron CLI, not a service).
>
> **AI Involvement:** Implementation and docs: AI-generated, reviewed and tested by me.
>
> Feedback welcome, especially on edge cases (proxies, self-signed certs, IPv6) and output format.

---

> **NamerekDev**（1 分） · 2026-11-06T22:14:43+08:00　
> **Project Name:** Even Keel
>
> **Repo:** [https://github.com/NamerekT/even-keel](https://github.com/NamerekT/even-keel)
>
> **Description:** A self-hosted dispatcher for coding agents. It takes the open tickets from your tracker (GitHub Issues, GitLab, Jira, Linear, Huly), runs Claude Code or Codex on them one at a time, each in its own git worktree, and when the subscription limit runs out it waits for the reset instead of failing. A web page shows what each session is doing, how full its context is and what every task cost. No cloud of mine in between: your machine, your tracker, your subscription. MIT.
>
> https://i.redd.it/u7z5zm3lizzh1.png
>
> **Deployment:** `npx even-keel` installs it and sets it up as a service (Windows at sign-in with a tray icon, systemd on Linux, launchd on macOS). State lives in a local PGlite, nothing to set up. No Docker image yet: it drives the agent CLIs you're already signed into on the host, so a container isn't the natural fit - one is in the works. Docs are in the README and docs/guide.
>
> **AI Involvement:** Heavy, and on purpose. Most of it was written by its own chain overnight from tickets I wrote; I review what lands and do the live checks by hand. It also leans on undocumented CLI behaviour, so a CLI update can break something until I adapt it.

---

> **ovizii**（1 分） · 2026-11-06T22:33:04+08:00　
> Been looking for something like this but haven't tested any solution yet.
>
> Does your project do anything better that the tools it is replacing or simply offer the same functionality in one single app?
>
> I.e. sonarr and radarr are a bit lacking when it comes to older content, it doesn't actively try to bring all items in it's catalogue up to the chosen profile. Huntarr briefly offered this before "huntarr-gate" 😅

---

> **SpiritualSnailhorse**（2 分） · 2026-11-06T22:57:42+08:00　
> Project Name: MindSift
>
> Repo/Website Link: https://github.com/mindsift-app/mindsift (website: https://mindsift.app)
>
> Description:
>
> \- MindSift is a self-hosted app for tasks, lists and notes in one place. I built it because I was never fully happy with the note and task apps I tried: either the UX didn't feel right, or things were missing like proper standalone documents, sharing, or a decent sync to pick up where I left off on my phone.
>
> \- Tasks: subtasks, task lists as Kanban boards, and tasks can be linked to notes
>
> \- Lists: shopping lists grouped by category, checklists
>
> \- Notes: nested bullets, to-dos and headings, shareable and editable by several people at once
>
> \- Inbox: quickly dump thoughts and sort them later
>
> \- Search: full-text search across everything
>
> \- Mobile: no native app, but a really good installable PWA. It even works partly offline: notes you've already loaded can be opened, and changes sync later.
>
> \- API: create tasks via webhooks from Home Assistant, your own scripts or anything else that can send a request
>
> \- MCP server: [Claude.ai](http://Claude.ai) and ChatGPT connect via OAuth, Codex, Cursor or your own local ai work too. E.g. "find me a lemon cake recipe, put the ingredients on my shopping list, save the recipe to my notes and add a task to bake it this weekend" happens in one go. Don't want any AI? The MCP server can be turned off completely.
>
> \- Voice input: optional local speech recognition via Speaches
>
> \- Languages: English, German, Spanish, French and Italian so far
>
> Deployment:
>
> \- Single Docker container (ghcr.io/mindsift-app/mindsift:latest), set up with install.sh. Instructions are in the README and on https://mindsift.app. License: AGPL-3.0.
>
> \- Performance: load-tested on an 1 vCPU / 1 GB RAM server with shared notes and many people editing the same note. Around 250 users without any noticeable slowdown, \~500 if not everyone edits at once. At 1,200 users it held up and recovered normally, no memory leaks.
>
> \- Security: every release image is scanned with Trivy (0 critical/high/medium/low, no secrets, no misconfigurations), govulncheck reports 0 vulnerabilities affecting MindSift. Critical feedback very welcome.
>
> AI Involvement: Heavy. Most of the code was written by AI. I'm a trained IT specialist, planned the architecture, reviewed everything and caught a lot of issues the AI missed. I use MindSift daily myself, so it'll keep being maintained.

---

> **vanmiku**（0 分） · 2026-11-06T23:18:32+08:00　
> **Project Name:** mydash
>
> **Repo/Website Link:** https://github.com/vanmiku/mydash
>
> **Description:** A self-hosted workbench for what AI coding agents (Claude Code, Codex) produce. Agents publish plans, reports, PDFs, images, HTML prototypes and Word/Excel/PowerPoint files with one command; you read them rendered on your computer or phone, answer their questions, fill in approval forms and leave comments that go back to the agent.
>
> New since last week: a conversation panel beside each document. It shows the recent conversation of the Claude Code or Codex session that produced it, and, if you turn sending on, lets you reply into that same session: the open Codex desktop thread, a Claude Code or Codex CLI running in tmux (typed only when its prompt is empty), or a Claude app session with Remote Control. Ordinary LAN browsers can only view. Both switches are off by default.
>
> **Deployment:** Node.js 20+, no Docker. `git clone https://github.com/vanmiku/mydash ~/.mydash/src`, then `./setup.sh install` (launchd on macOS, a systemd user unit on Linux, the Startup folder on Windows). It listens on 127.0.0.1 only; reach it from other devices over Tailscale, or on the same Wi-Fi with an access code and device approval. Docs: INSTALL.md and docs/sessions.md.
>
> **AI Involvement:** Built largely with Claude Code and Codex, with me writing the requirements, deciding the design and reviewing it. CI runs end-to-end tests on macOS, Linux and Windows, plus browser tests, on every change.

---

> **andyknosp**（1 分） · 2026-11-06T23:24:16+08:00　
> **Project Name:** team-photo-sorter
>
> **Repo/Website Link:** [https://github.com/andyknosp1/team-photo-sorter](https://github.com/andyknosp1/team-photo-sorter) (Apache 2.0)
> Live demo: [https://andyknosp1.github.io/team-photo-sorter/](https://andyknosp1.github.io/team-photo-sorter/) (password `lakeview-demo`; the players are illustrations, not real kids)
>
> **Description:**
> My daughter’s high school water polo team has a parent who photographs every game. Over the season he shared about 53,000 photos, and every family was scrolling through all of them to find their own kid.
>
> team-photo-sorter fixes that on your own hardware. It groups the player's faces in each game’s photos with InsightFace, then builds a static website. Families unlock it with a shared password, pick a game, put their kid’s name on a face group, and get that player’s contact sheet to view and download.
>
> * **Local only:** face detection and grouping run on your machine. No cloud face recognition, no accounts, and nothing leaves except the finished, encrypted site.
> * **Encrypted static output:** AES-256-GCM, decrypted in the browser. File names are random tokens, so they don’t reveal player or game names.
> * **Incremental rebuilds:** unchanged files encrypt to identical bytes, so adding a game only adds that game’s files.
> * **Suggests, never merges:** “Could these also be Sam?” within a game, and “Same face as Sam in another game” across games. Families confirm each one, because teammates in matching caps fool face grouping.
> * **Known limits:** one shared password (no per-family accounts), CPU only. There’s a privacy guide on consent and biometric data, since this is face recognition on photos of minors.
>
> **Deployment:**
>
> * Released on PyPI: `pip install team-photo-sorter` (Python 3.10–3.14), then `tps init` and `tps all` in a folder with one subfolder of photos per game.
> * No Docker image: it’s a command-line tool you run when there are new photos, not a long-running service.
> * The output is a folder of static files. Serve it from your own box with nginx or Caddy, or put it on Firebase, Netlify or GitHub Pages.
> * Docs: install and quick start in the [README](https://github.com/andyknosp1/team-photo-sorter#quick-start), plus guides for [hosting](https://github.com/andyknosp1/team-photo-sorter/blob/main/docs/hosting.md), [security](https://github.com/andyknosp1/team-photo-sorter/blob/main/docs/security.md) and [privacy](https://github.com/andyknosp1/team-photo-sorter/blob/main/docs/privacy.md).
>
> **AI Involvement:** Built with Claude Code, which wrote much of the code. I designed it, tested it, and ran it on our team’s full season of real photos before generalizing it for release.
>
> Feedback is welcome, especially on the security model.

---

> **Sh4d0w_0020**（2 分） · 2026-11-06T23:29:01+08:00　
> **Project Name:** Gami.Fied (Community Edition)
>
> **Repo/Website Link:** [https://github.com/gami-fied/gami.fied](https://github.com/gami-fied/gami.fied) (Tets it out here: [Gami.Fied](https://gami.fied.cc) \- Do not use it for production use as it is currently available for testing purpose only. Your data might be deleted anytime with no prior notice.)
>
> **Description:** Gami.Fied is a self-hosted gamification engine. Your app sends it events ("lesson\_completed", "order\_placed"), and rules you configure turn those into XP, levels, achievements, challenges and leaderboards. It also sends notifications and webhooks, so your own data stays on your own server.
>
> The problem: if you want points, badges or streaks in an app, you either build and maintain all of it yourself or hand your users' activity to a SaaS. This is a middle route.
>
> What's included:
>
> * Event API with duplicate protection, single or in batches of up to 100
> * Rules engine with conditions, a preview, and a "why did this fire?" trace
> * XP history, levels, achievements, challenges, and all-time/daily/weekly/monthly leaderboards
> * In-app and email notifications, signed webhooks with retries and replay, Discord integration
> * Web dashboard with analytics, CSV export, roles (owner/admin/member), audit logs and a delivery health page
> * API keys with scopes, plus short-lived end-user tokens so a browser can read one user's data without ever holding a key
> * Platform admin area for organizations, sessions, backups, storage and server settings
> * Data export/import per organization, and user erasure for privacy requests
> * Full API reference built into the dashboard, with copy-paste samples in cURL, JavaScript and Python
> * TypeScript SDK (Version 1.0.0 is on the way!)
>
> It's for people running their own app, community or learning platform who want this built in without a third-party service.
>
> **Deployment:** Yes, it's released (v1.0.0) and prebuilt images are on GHCR for amd64 and arm64, so nothing needs building. The stack is Postgres 17, Redis 7, an API, a worker and a dashboard, all in one compose file.
>
>     curl -LO https://github.com/gami-fied/gami.fied/releases/download/v1.0.0/docker-compose.yml
>     curl -LO https://github.com/gami-fied/gami.fied/releases/download/v1.0.0/env.example
>     cp env.example .env
>     # fill in the secrets in .env, then:
>     docker compose up -d
>
> Docs are in the repo's `docs/` folder: getting started, production deployment with a reverse proxy (there's a Caddy example), backups and restore, security notes, and quickstarts for Node, Next.js, React, Python and plain REST.
>
> Licence: the server, worker and dashboard are AGPL-3.0. The SDK is MIT.
>
> **AI Involvement:** A large part of this project was written with Claude Code, under my direction: the later work on security hardening, the rules/rewards engine fixes, the dashboard, the API docs and the tests. Initially I began working on this project myself then started using Antigravity to speed up the work and finally switched to Claude Code recently. The code is tested (500+ tests), CI runs the full stack, and I've reviewed the results, but it's young and may have bugs. Issues and PRs welcome.
>
> **Known limits, so you don't have to find out the hard way:**
>
> * It's a brand new 1.0 from a single maintainer
> * Leaderboards and some summaries are calculated from the database on each request, and I haven't published a load test yet, so test it before putting a big app on it
> * Routes under `/api/projects` are for the dashboard and can change. Build on `/v1`
>
> ***Any feedback is much appreciated! Thank you!***
>
> https://i.redd.it/8w4n4938g00i1.png

---

> **olivercer**（1 分） · 2026-11-07T00:23:17+08:00　
> https://i.redd.it/ax78ybjyp00i1.jpeg
>
> **Project Name:** WhatsApp Backup Tools (wab-tools)
>
> **Repo/Website Link:** [https://github.com/auanasgheps/whatsapp-backup-tools](https://github.com/auanasgheps/whatsapp-backup-tools)
>
> **Description:** A local-first, 100% offline suite to archive and browse your WhatsApp data on your own storage.
>
> * **wab-archiver:** Turns WhatsApp backups (Android & iOS, no root required) into a clean, human-readable folder tree (`Contacts/<Name>/<Year>/<Sent|Received>/` and `Groups/<Group>/<Year>/`), preserving original message timestamps and tracking contact renames.
> * **wab-viewer:** An offline Web UI replica of WhatsApp Web. Scroll across tens of thousands of chat messages with in-browser media playback, interactive polls, link previews, and full-text search.
>
> **What's new in v0.70:**
> I just released version v0.70:
>
> * **Deleted Message Preservation (**`-P`**):** Diff consecutive backups to capture and preserve deleted/revoked messages and removed chats into a dedicated local database (`preserved_messages.db`).
> * **Android Incremental Merging:** Automatically discovers, decrypts, and sequentially merges daily incremental delta backups (`msgstore-increment*.db.crypt15`).
> * **Interactive Polls, Link Previews & Maps:** Native polls with voter breakdowns, rich link cards, and interactive location maps.
> * Many more improvements and fixes!
>
> **Deployment:** Available on PyPI (`pip install --upgrade whatsapp-backup-tools`) and GitHub Releases. Requires Python 3.11+. Runs locally on Linux, macOS, and Windows. Run `wab-archiver` to build the archive, then `wab-viewer` to spin up the local web UI at `localhost:5000` (or bind to [`0.0.0.0`](http://0.0.0.0) for your LAN).
>
> **AI Involvement:** I use AI tools as a pair programmer to write code and tests. However, this is not a vibecoded project. Archiving personal history requires strict data integrity: the architecture is human-designed, involves deep reverse-engineering of WhatsApp's SQLite/protobuf schemas, and is backed by over 1,000 automated tests and manual verification.

---

> **naxeu**（0 分） · 2026-11-07T00:25:32+08:00　
> **Project Name:** JuStAI – Turn cheap security cameras into a multi-room AI assistant
>
> **Repo/Website Link:**
>
> * GitHub: [https://github.com/naxeu/justai](https://github.com/naxeu/justai)
> * Website & demo: [https://justai.naxeu.com/](https://justai.naxeu.com/)
>
> **Description:**
>
> Hi everyone!
>
> I've been working on **JuStAI**, an open-source, self-hosted AI platform that turns multiple inexpensive Wi-Fi security cameras into a single, room-aware AI assistant.
>
> Why buy dedicated smart speakers for every room when affordable cameras already have microphones and speakers?
>
> Some of the coolest features:
>
> * **"Hey Justy, where are my car keys?"** Justy can rotate a pan-and-tilt camera, search the room using AI vision, and tell you where it found them. Tested with real hardware!
> * **"Next time you see me, remind me to take out the trash."** Justy can create camera-triggered automations. The logic is tested, but real-world face recognition still needs validation.
> * **"Build a plugin that alerts me when electricity gets cheap."** Justy can generate plugins, write tests, and run them in a sandbox after administrator approval.
> * **Room-aware conversations:** Talk to Justy in the kitchen, and the response comes from the kitchen speaker, not another room.
>
> **Deployment:**
>
> Runs on Linux (x86\_64) using Docker Compose. A one-command installer handles the setup, including Docker installation if needed.
>
> Compatible cameras such as the TP-Link Tapo C200 can be configured through the web interface.
>
> Speech processing can run locally, with Gemini or Ollama as AI backends.
>
> Installation guide: [https://github.com/naxeu/justai/blob/main/docs/INSTALLATION.md](https://github.com/naxeu/justai/blob/main/docs/INSTALLATION.md)
>
> **AI Involvement:**
>
> AI-assisted development and documentation. JuStAI itself uses AI models for conversations, vision, and plugin generation. Some features are still experimental; tested and untested functionality is documented in the repository.
>
> I'd love feedback from the self-hosting community, especially on camera compatibility, setup, and potential use cases!

---

> **SilentMode46**（0 分） · 2026-11-07T00:42:15+08:00　
> https://i.redd.it/vzld733it00i1.png
>
> I reverse-engineered Apple Photos and rebuilt it for my own server – iCloud Photos without iCloud
>
> I got tired of paying Apple every month to keep my own photos, so I moved \~85,000 photos and videos to my own server (Immich) and switched iCloud Photos off.
>
> The problem: every Immich app I tried felt nothing like the Photos app I was used to. So I built my own.
>
> HomeRoll is a native iOS 26 app (SwiftUI + UIKit) that looks and behaves like Apple Photos, but everything lives on hardware you own.
>
> How I got it this close: I took Apple’s Photos frameworks from iOS 26.3 apart and went through all 226 actions the Photos app can perform (copy edits, print, hide, set key photo, show fewer memories, drag to album, Spotlight …). 147 of them now work in HomeRoll. 62 are iCloud/Apple-service only, 16 are Apple-internal, 1 isn’t possible on iOS. 140 of the 147 are covered by automated UI tests.
>
> What’s in it
>
> * Library with the same pinch-to-zoom grid, Years / Months / All, Today / Yesterday / weekday titles
> * Viewer with the Apple-style preview strip and smooth video scrubbing, Live Photos, HDR originals
> * Editor: light, color, filters, styles, crop, copy and paste edits
> * Memories, featured photos, people, places, birthdays
> * Search for receipts, documents, handwriting, QR codes, screenshots, selfies …
> * Album folders, drag photos onto albums, Spotlight search for albums and people
> * Backup: new photos and videos go to your server automatically, in the background while the iPhone charges
> * Free Up Space: deletes only what’s verified to be on your server (checksum + server check)
> * Widgets and a share extension
>
> Stack: your own Immich server (tested with v3.3.5) + this app. English and German.
>
> It’s free and MIT licensed:
> [https://github.com/silentprovider423/HomeRoll](https://github.com/silentprovider423/HomeRoll)
>
> Not affiliated with Apple or Immich/FUTO. Happy to answer questions about the setup or the reverse engineering.

---

> **DependentHonest8010**（2 分） · 2026-11-07T01:24:35+08:00　
> Project Name: Landfall
>
> Repo/Website Link: [https://github.com/flaggx/landfall](https://github.com/flaggx/landfall)
>
> Description: An open-source (MIT) Go CLI that makes one Ubuntu VPS feel like a managed platform, with no Docker and nothing running on the server but your app. It runs on your laptop (or in CI, or from an AI coding agent) and manages the server over SSH:
>
> \- Hardening: ufw, fail2ban, unattended upgrades, SSH config
>
> \- Git deploys, with your app running as a normal systemd service (Next.js standalone is the main target; other Node apps take a bit more setup)
>
> \- HTTPS through Caddy, Postgres, and Redis with a separate instance per environment, so staging can't read or wipe prod's data
>
> \- Secrets stay on your machine and are written to the server at deploy time, never committed to Git
>
> \- Scheduled Postgres backups, and landfall check, which checks the whole setup and calls your app's health endpoint
>
> It's for solo devs and small teams who want the convenience of a managed platform on servers they own, without having to write deploy scripts for every project. I built it right before starting my own small production site, and it has deployed that site from day one, a bit over 3 months now. It's not for you if you want a web UI (Dokku, Coolify, CapRover) or zero-downtime container deploys (Kamal).
>
> Deployment: Landfall isn't something you host. You install the CLI on your own machine and point it at your VPS. Linux binaries (amd64 and arm64) are on the releases page (https://github.com/flaggx/landfall/releases/latest), or you can run go install github.com/flaggx/landfall/cmd/landfall@latest. There's no Docker image, on purpose: the server runs your app directly under systemd. The README walks through the full path from init to deploy to check, including how to run it from an AI coding agent.
>
> AI Involvement: Heavy, and I'll be upfront about it. Most commits (55 of 63) were written with AI coding tools (Claude Code and Cursor), and they're tagged as co-authored in the history. I designed the tool, directed the work, reviewed the changes, and test every release against my own production VPS. CI also runs the tests against real Ubuntu.

---

> **Ryyn_-**（1 分） · 2026-11-07T01:48:27+08:00　
> # FLE LINK - Interlayer between Engine and everything else.
>
> FLE Link: a local server for AI models, one file to install (Linux, macOS, Windows), no account, no telemetry, nothing leaves the machine except fetching the engine from GitHub and models from Hugging Face. OpenAI- and Anthropic-compatible API on your own address, a browser Studio and a desktop app. I make it (MIT): [https://flelink.run](https://flelink.run/) · [https://github.com/sirfyyn/flelink](https://github.com/sirfyyn/flelink)

---

> **wsLyNL**（2 分） · 2026-11-07T01:51:24+08:00　
> This sounds interesting!

---

> **WobblyCart**（1 分） · 2026-11-07T02:32:32+08:00　
> **Project Name:** AppRankly
>
> **Repo/Website Link:** [GitHub - zmsp/AppRankly](https://github.com/zmsp/AppRankly)
>
> **Description:** AppRankly is a lightweight, local-first utility designed to help mobile developers track and monitor their application metrics, store rankings, and keyword positions across app stores. It solves the problem of constantly having to manually check multiple dashboards or rely on bloated, expensive third-party SEO tools, keeping your app analytics streamlined and entirely private.
>
> **Deployment:** Fully open-source with an easy-to-use Docker setup. You can deploy it locally or on your self-hosted server using the provided Docker image and docker-compose example in the repository. Minimal documentation is included in the README to get your environment up and running in minutes.
>
> **AI Involvement:** Developed with AI assistance for code scaffolding, boilerplate generation, and optimizing data processing logic.
>
> https://i.redd.it/dhfs4op6d10i1.png

---

> **ElderHare**（1 分） · 2026-11-07T02:57:11+08:00　
> There is additional functionality but it's mostly a Rust port of the stack into a single app.  For example, additional functionality would include Spotify and YouTube direct downloads, Radio/Podcast discovery.  I am definitely looking for suggestions and feedback, so if you get a chance to test it -- let me know in DMs or join the Discord.

---

> **JustA-Myth**（1 分） · 2026-11-07T04:06:11+08:00　
> **Project Name:** OldPhone CCTV
>
> **Repo/Website Link:** [https://github.com/AmitSaha9928/old-phone-cctv](https://github.com/AmitSaha9928/old-phone-cctv)
>
> **Description:** OldPhone CCTV turns old Android phones into self-hosted security cameras. A tiny companion app (33 KB, no libraries) streams the phone’s hardware-encoded H.264 video and audio to a server on your PC. The server records 24/7 to crash-safe MP4s with 1–14 days retention, shows multiple cameras live in the browser (WebCodecs, low latency), and has a scrubbable per-day timeline with export of any time range. Motion detection runs **on the phone**, so the server never decodes video, and alerts with a snapshot go out via **ntfy** or Telegram. Two-way talk works through the phone’s speaker. Remote access is through `tailscale serve`, with no port forwarding.
>
> It solves “I have old phones in a drawer and don’t want to pay for cloud cameras”. Existing phone-camera projects (Haven, spydroid) are unmaintained and had no recorder, and NVRs like Frigate expect IP cameras. This does both halves in one download, with nothing leaving your network.
>
> **Deployment:** Windows today. Download the release zip (FFmpeg and adb bundled), run `setup.ps1`, start `Start CCTV.bat`, install the APK on the phone, and it’s found and paired on your LAN automatically. The server is Python standard library only (no pip installs), and binds to localhost by default. There’s **no Docker image yet**; it should run on Linux/macOS with `ffmpeg` installed, but that’s untested, so a Dockerfile/compose would be a very welcome first PR. Setup guide, FAQ and protocol docs are in `docs/`.
>
> **AI Involvement:** Built with heavy AI assistance. Most of the code (Android app, Python server, web viewer) was written by Claude (Anthropic’s AI coding assistant) under my direction, and the commits are co-authored accordingly. I set the requirements and design decisions, and did the hardware work and real-world testing myself. That meant reflashing the phone, debugging the camera driver and USB issues, and running it daily on a Mi A2 as my home camera. Every feature was tested end to end on a real phone or the included phone simulator, and I reviewed the release for privacy (no telemetry, nothing leaves your network unless you enable ntfy/Telegram alerts).
>
> https://i.redd.it/vx3i1tsvt10i1.png

---

> **Curious_Necessary549**（1 分） · 2026-11-07T04:49:19+08:00　
> **Project Name:** LightCMS
>
> **Repo/Website Link:** https://lightcms.me (source: github.com/light-cms)
>
> **Description:** lightcms: git based cms for static site generators. Posts stay as plain Markdown files with frontmatter, every save is a real commit, and Hugo/Astro/Zola build the site. No database, no vendor lock-in, so diffs, history and rollback come for free.
>
> **Deployment:** Hosted workspace at lightcms.me; the source is open if you'd rather not use the hosted one.
>
> **AI Involvement:** The writing copilot (and optional voice input) is AI-powered; it's a plain Markdown editor without it.

---

> **ToYoNiX**（1 分） · 2026-11-07T05:23:25+08:00　
> **Project Name**: nginx-proxy-manager-sync
>
> **Repo**: [https://github.com/ToYoNiX/nginx-proxy-manager-sync](https://github.com/ToYoNiX/nginx-proxy-manager-sync)
>
> **Description**:
>
> npm-sync keeps one or more backup Nginx Proxy Manager instances identical to a master, so a backup can take over if the master goes down. It's like adguardhome-sync, but for NPM.
>
> * One-way sync: the master is the source of truth. Anything added, changed or deleted on the master is applied to every backup, and hand changes on a backup are overwritten (except domains you exclude).
> * What it syncs: proxy hosts, redirection hosts, 404 hosts, streams and access lists.
> * Certificates: Let's Encrypt certificates (HTTP or DNS challenge) are copied from the master and re-copied when it renews them. Backups never contact Let's Encrypt and don't need DNS provider tokens.
> * How it runs: on a cron schedule, at startup, or on demand from a small web UI or the API.
> * Safety: a dry-run mode, a limit on how much one run may delete, and a check that refuses to sync from an empty master. It can also expose Prometheus metrics.
>
> **Known limitations**:
>
> * Custom (uploaded) certificates sync for now but not for very long. That relies on NPM returning private keys through its API, which has already been removed in NPM's develop branch.
> * On the backup, NPM lists only one domain for a copied multi-domain certificate. This is a quirk of NPM's upload; TLS works for every domain though.
> * Two-factor authentication isn't supported for the NPM users npm-sync logs in with, and the master and backups should run the same NPM version.
>
> **Deployment**:
>
> It's a single Go binary in a Docker image, ghcr.io/toyonix/npm-sync, configured with a YAML file or environment variables. To get started, copy the compose example and config example, or follow the README quick start. SPEC.md documents exactly how it works.
>
> **AI Involvement**:
>
> Built with heavy use of Claude Code: Go code, tests and docs. Design and sync flow was my own. I tested it on my own setup, and integration tests run it against two real NPM 2.16.0 containers. It started as a fork of jeffersonraimon/npm-sync and was then rewritten in Go.

---

> **a_fish1**（3 分） · 2026-11-07T05:37:53+08:00　
> **Project Name:** Inky calendar
>
> **Repo/Website Link:** [https://github.com/simon-lund/inky-calendar](https://github.com/simon-lund/inky-calendar)
>
> **Description:** A calendar you can draw on like paper, with your real events in it. It loads events from any iCal link (Google, Apple, Nextcloud, …) as a month grid and puts a transparent canvas on top: finger, pen or mouse. Made for e-ink displays with touch or pen input, as a wall or desk calendar: black on white, no animations, big targets. Strokes are stored as vectors in relative coordinates, so the same drawing fits any panel. Drawings live in one SQLite file next to the app, so every screen in the house shows the same calendar.
>
> **Deployment:** Self-hosted on your home network. Node 22 or newer, nothing native to compile: pnpm install, build, start, then open it in a Chromium kiosk on a Raspberry Pi or add it to a tablet’s home screen. No accounts, so keep it off the open internet. MIT.
>
> AI Involvement: Vibe-coded with Claude Code. The app itself has no AI in it.
>
> https://i.redd.it/884at6w8a20i1.png

---

> **DazzlingRecover5037**（1 分） · 2026-11-07T06:26:52+08:00　
> **Project Name:** Gateweave Track
>
> **Repo/Website Link:** [https://github.com/gateweavehq/track](https://github.com/gateweavehq/track) (demo: [https://track-demo.gateweave.com](https://track-demo.gateweave.com), one click, deleted after a day)
>
> **Description:** An open-source (AGPL-3.0) issue tracker in the spirit of Linear: lists, boards, cycles, projects, an inbox, keyboard shortcuts. It keeps a copy of your workspace in the browser, so it opens at once, syncs live between people and keeps working offline. It has an MCP server for AI agents, webhooks and a GitHub integration, imports from GitHub, Linear and Jira, and exports everything as CSV or JSON.
>
> **Deployment:** Read this first, because it may rule it out for you: it isn't a container. It runs on your own Cloudflare account, as one Worker with Durable Objects, D1 and R2, on Cloudflare's machines and not yours. You own the account, the code and the data, but there's no Docker image or docker-compose, and there won't be one. A Deploy to Cloudflare button copies the repo to your GitHub, creates the database and deploys it, on the $5 Workers Paid plan. Guide: [https://github.com/gateweavehq/track/blob/main/docs/self-hosting.md](https://github.com/gateweavehq/track/blob/main/docs/self-hosting.md). It's at v0.28: expect breaking changes before 1.0, and there has been no outside security audit.
>
> **AI Involvement:** A lot. AI agents (Claude Code, with Devin reviewing pull requests) wrote most of the code and this comment, and nobody has read every line. I set the goals and make the calls. Every bug fix needs a test seen failing without it, and tests run against real Durable Objects and in real browsers. What that has and hasn't caught, plus what it measures and costs: [https://gateweave.com/blog/one-cloudflare-worker](https://gateweave.com/blog/one-cloudflare-worker)

---

> **caskater47**（5 分） · 2026-11-07T07:04:28+08:00　
> Project Name: RapidMX
>
> Repo/Website: [GitHub](https://github.com/rapidmx/server) | [rapidmx.io](https://rapidmx.io/)
>
> Description: RapidMX is a complete communications platform you run yourself: email, calendar, contacts, tasks, video meetings and booking pages. Your data is stored encrypted to keys only your users hold, with end-to-end encryption over S/MIME and OpenPGP built in. Everything your team relies on from Google Workspace or Microsoft 365, without handing your conversations to someone else's cloud.
>
> I built this to replace the many services I have been paying for decades whose costs keep creeping up, quality keeps dropping and privacy is non-existant.
>
> Deployment: Runs anywhere you can run Kubernetes or Docker Compose. Kubernetes is the easiest method and can be up and running in a single command line. I even wrote a simplified bash script that will install k3s, nginx reverse proxy and everything needed for bare metal and vanilla Linux VPS instances.
>
> AI Involvement: This project was born out of a curiosity of mine to test the limits of current AI code tools like Claude Code. I wanted to know if AI could build such a product, start-to-finish, and how long it would take. I have done all the architecture, planning and design work. Claude Code writes all the code. I have been amazed at the quality of Claude's work and the speed as well. I was able to build the first fully working MVP in less than two weeks. Now, more than a month later, the project is stabilizing, nearing a 1.0 release and I am using it on a daily basis to power my own personal and business servers.
>
> Feedback and feature requests are very welcome.
>
> https://i.redd.it/pvfnqhdop20i1.jpeg

---

> **gerabh1128**（1 分） · 2026-11-07T07:50:32+08:00　
> Project Name: FrameBridge (GPLv3)
>
> Repo: [https://github.com/gerabh1128/framebridge](https://github.com/gerabh1128/framebridge)
>
> Source release: [https://github.com/gerabh1128/framebridge/releases/tag/v0.3.7](https://github.com/gerabh1128/framebridge/releases/tag/v0.3.7)
>
> Install / verification: [https://framebridge.betancourt.one/download/](https://framebridge.betancourt.one/download/)
>
> Description: Hi, I'm Gerardo. I built FrameBridge to administer my own Linux home lab from a connected ChatGPT conversation. A central gateway and enrolled nodes expose MCP tools for command execution, persistent Bash terminals and optional interaction with an existing X11 desktop. ChatGPT remains hosted; the tools run on machines I control.
>
> Deployment: Debian 13, Ubuntu 24.04 and Linux Mint 22.x (amd64). GitHub v0.3.7 is a source release, with no .deb assets attached there. The official download page provides distro-specific packages, signed APT instructions and signature checks. Please verify the offered package version and target distribution before installing.
>
> AI Involvement: I drove the use cases, architecture and home-lab tests, with substantial ChatGPT assistance for coding, debugging, testing and documentation. Feedback on security boundaries, setup and usability is welcome.

---

> **Capital-Interview-23**（3 分） · 2026-11-07T08:50:44+08:00　
> **ExifTree: a single-tenant Django photo gallery built around EXIF, cameras, and lenses (a starting point if you're comfortable with code)**
>
> I made ExifTree, a Django photography portfolio that lets you browse photos through the gear that made them. It's not a polished turnkey app. Think of it as a starting point if you're code-savvy and want your own gear-centric photo site to fork and shape.
>
> What it does today:
>
> - Extracts EXIF metadata and gives cameras and lenses their own browsable galleries
> - Curated collections, plus browsing by year, tags, and location
> - Search across titles, descriptions, and tags
> - Bulk imports from local folders and Flickr, with background image processing and thumbnail generation
> - Optional OpenAI integration that generates titles, descriptions, and tags (not locally hosted)
>
> **It is single-tenant only: one photographer per installation.** [photos.kennethreitz.org](https://photos.kennethreitz.org) is the live demo and the only installation I'm aware of.
>
> Honest caveats: it was built for one library, and it shows. The import pipeline still has some cleanup rules specific to my photos hard-coded in `ingest/pipeline.py`, so read and adjust that before importing your own library. Setup and self-hosting need smoothing, and the AI description workflow needs a proper review and edit step before it's truly self-serviceable.
>
> [Code and README](https://github.com/kennethreitz/photos.kennethreitz.org)
>
> Feedback I'd love: how the camera and lens navigation feels, what would stop you from running your own copy, and how you'd want to review generated descriptions before publishing.

---

> **Noobie3DPrinting**（2 分） · 2026-11-07T09:26:42+08:00　
> Root Cellar — four household apps for your home server
>
> I wanted our household stuff off other people's clouds, so I built these for our house and cleaned them up to share:
>
> • Checkbook — shared check register with bills and paydays; works offline on phone/PC and syncs at home
>
> • Notes — private and shared notes
>
> • Movies — disc collection + wishlist with barcode scanning and cover art (optional Jellyfin link)
>
> • Labels — design labels in the browser and print to a DYMO LabelWriter (Twin Turbo works), 7 sizes, 10 fonts, clip art
>
> One-command install (sudo bash install.sh) on any Linux box, or a Portainer stack. Windows app, Android apps, and iPhone via Add to Home Screen. Optional Tailscale for HTTPS away from home. The guide is written for beginners, with copy buttons on every command.
>
> MIT licensed. Built with help from Claude (Anthropic's AI assistant); the ideas, design and testing are mine. Every app is running in my house now.
>
> GitHub + downloads: [https://github.com/Noobie3DPrinting/root-cellar](https://github.com/Noobie3DPrinting/root-cellar)
>
> Fixes, updates, pull requests and ideas are all welcome.

---

> **RadiantTurnover24**（1 分） · 2026-11-07T09:30:48+08:00　
> **Project Name:** Inkling
>
> **Repo/Website Link:** [https://github.com/PROVE1352/inkling](https://github.com/PROVE1352/inkling) (screenshots in the README)
>
> **Description:** Notes app for small groups, Notion-style databases plus Obsidian-style links. Databases have table, board, calendar, gallery and timeline views with relations and rollups. There are `\[[wikilinks\]]`, backlinks, tags and a link graph, a canvas that uses Obsidian's JSON Canvas format, and Dataview-style query blocks. Pages can be edited by several people at once (Yjs). The MCP server is built in and uses OAuth, so Claude Code or any MCP client acts as a specific user and only sees what that user can see. MIT, no paid edition.
>
> A few friends and teammates have been using it for contest and hackathon work, on a free-tier Oracle Cloud ARM VM. The repo only just went public.
>
> Things it doesn't have: SQLite mode (Postgres is required), native apps (it's a PWA), SSO/OIDC or 2FA, a Notion importer, or more than one instance. User base is small.
>
> **Deployment:** Docker Compose. App, PostgreSQL 16 and a backup sidecar, plus an optional Caddy overlay for HTTPS. The sidecar does scheduled backups, verifies them, can encrypt them, keeps GFS retention and runs a restore test once a week.
>
>     git clone https://github.com/PROVE1352/inkling.git && cd inkling
>     cp .env.example .env   # PUBLIC_URL, DOMAIN, POSTGRES_PASSWORD, BACKUP_PASSPHRASE
>     docker compose -f compose.yaml -f deploy/compose.caddy.yaml up -d --build
>     ./deploy/signup-key.sh new "first admin"
>
> Locally without a domain: `docker compose up -d --build`, run the same `./deploy/signup-key.sh` (production mode still wants a signup key), then open http://localhost:3000. No prebuilt image yet. Compose builds it from source, x86-64 or ARM64. Memory limits in compose are 768 MB app / 512 MB Postgres / 256 MB backup. Those are caps, not what it actually uses. Postgres settings default small so it fits on a 1 GB host. Docs: README, `deploy/DEPLOY.md`, `docs/OPERATIONS.md`, `docs/BACKUP.md`.
>
> **AI Involvement:** Heavy. I designed and wrote it with AI coding agents doing a lot of the work. Before release I did review passes on the spots generated code usually gets wrong (races and lost updates, memory and connection use, unbounded growth), a security review, and perf work only after measuring. Decisions are in `docs/adr/`. Open problems are in `docs/KNOWN-ISSUES.md`, and some are Medium security items, e.g. session tokens stored in plaintext in the DB and no Origin check on state-changing requests. Read that before you put anything important in it.
>
> If the install breaks for you, tell me where. That's the feedback I need most right now.

---

> **LevyTateLabs**（4 分） · 2026-11-07T10:15:45+08:00　
> https://i.redd.it/b1jlbd0tn30i1.png
>
> **Project Name:** StratoSort
>
> **Repo/Website Link:** [GitHub](https://github.com/iLevyTate/StratoSortStack) · [stratosort.com](https://stratosort.com) (site + docs)
>
> **Walkthrough:** [43-second video](https://github.com/iLevyTate/StratoSortStack/blob/main/docs/walkthrough-assets/how-to-use.mp4)
>
> **Description:** For the folder full of `scan_0042.pdf` and `final_v3_REAL.docx`. StratoSort reads what's actually inside each file, suggests a clear name and the right folder, and waits for your OK before anything moves. Every move or rename can be undone.
>
> Folders are just a name plus a plain-language description like "budgets, forecasts, invoices." That description is what the AI sorts against.
>
> Once your files are indexed you can search by meaning and chat with them. In the demo, searching "how warming affects wildlife" brings up `arctic-sea-ice-monitoring-report.txt` first even though the file name has none of those words. Chat answers come with numbered citations back to the source file and flag potential conflicts, like two documents giving different dates for the same thing. A graph view shows why files are connected.
>
> Handles 100+ file types, including scanned PDFs, images, audio and video, with transcription done locally.
>
> Built it solo over 17 months of part-time hours. Privacy is the one thing I won't bend on, so nothing from your files leaves the machine unless you turn that on yourself.
>
> The parts this sub will probably care about:
>
> * Every network connection the app can make is listed with the code that makes it, plus an airplane-mode test you can run yourself: [Network Transparency](https://github.com/iLevyTate/StratoSortStack/blob/main/docs/NETWORK_TRANSPARENCY.md)
> * No account, no telemetry, no crash upload. License keys are checked offline and update checks can be switched off
> * Can also talk to Ollama, LM Studio or any OpenAI-compatible endpoint if you'd rather use your own model server
> * Optional MCP server bound to 127.0.0.1 so Claude Desktop, Cursor or Zed can search your library
> * macOS builds are Developer ID signed and notarized (Apple Silicon + Intel). Windows installers are code signed. x64 and ARM64 builds for Windows and Linux
>
> **Deployment:** Desktop app, not a server, so no Docker image. Installers for Windows 10 (22H2) or 11, macOS 13+ and Ubuntu 22.04+ are on [GitHub Releases](https://github.com/iLevyTate/StratoSortStack/releases). First launch you pick a model profile (about 7 to 10 GB, downloaded once) then point it at the folders you want indexed. [Docs](https://stratosort.com/docs/)
>
> **License:** Source available under PolyForm Noncommercial 1.0.0. Free for personal use with every feature. Commercial use is a paid per-seat license. Not OSI open source, figured I'd say that up front.
>
> **AI Involvement:** A lot. I build with Claude Code. Since the public repo started Oct 4, 61 of the 146 non-merge commits are tagged as written or co-written by Claude. Claude works on branches and I merge every one of its PRs myself. CI runs lint, type checks, dependency audits, the full test suite with coverage and end-to-end tests on every push and PR to main.

---

> **Easy_Minimum6608**（1 分） · 2026-11-07T11:31:06+08:00　
> Kestello, a self-hosted CMS (no release yet, but the code is all public)
>
> I've been building a CMS for the kind of sites I make for clients: small businesses where the owner wants to change the page themselves without breaking it. Kestello isn't released yet (0.1.0 is close), but the whole codebase is on GitHub now, and I'd rather get eyes on it early than polish it alone for another few months.
>
> Roughly what's in there:
>
> \- a visual page editor that edits the real page, with blocks, patterns and per-screen styles
> \- content types, forms, media library with cropping, menus, redirects, search, backups
> \- signed updates straight from GitHub releases
> \- MySQL, MariaDB, Postgres or SQLite. Meant to run on plain shared hosting too, not only Docker
> \- plugins and themes (Vue), plus a REST API if you want to go headless
>
> PHP 8.4, no Composer dependencies, GPL. No paid version and none planned.
>
> If you want to poke at it, there's a docker-compose setup in the repo, so running it locally is quick. Not something I'd put in production yet though.
>
> Issues, ideas, "why on earth did you do it this way" questions and PRs are all welcome. PRs go against develop, and [CONTRIBUTING.md](http://CONTRIBUTING.md) has the details.
>
> [https://github.com/kestellohq/cms](https://github.com/kestellohq/cms)
>
> Docs (still growing): [https://docs.kestello.com](https://docs.kestello.com)

---

> **AnshulJ999**（2 分） · 2026-11-07T12:18:47+08:00　
> https://i.redd.it/soa3ocke940i1.png
>
> **Project name:** KopiaLens
>
> **Repo/Website:** [https://github.com/AnshulJ999/KopiaLens](https://github.com/AnshulJ999/KopiaLens) · [https://kopialens.com](https://kopialens.com)
>
> **Description:** Think Everything search + TreeSize, but for your Kopia backups. It's also a full backup app, so it replaces KopiaUI if you want it to. I started it after finding that my 1.2 TB backup folder only added up to about 600 GB in KopiaUI. 400+ GB of junk later, here we are hah. I use it to get more control and visibility over my backups. I hope it's useful to fellow data hoarders.
>
> **Self-hosting:** Docker (amd64, arm64) with a browser UI, a Home Assistant add-on, or a desktop app on Windows/macOS/Linux. It opens your existing repositories, with nothing to migrate.
>
> **Docker:** [compose.example.yml](https://github.com/AnshulJ999/KopiaLens/blob/main/compose.example.yml)
>
> **Docs:** [https://kopialens.com/docs](https://kopialens.com/docs) ([Docker Guide](https://kopialens.com/docs/docker))
>
> **Pricing and licence:** Not open source. The whole backup app and all the main features like Search, Restore, analysis and previews, are free. Pro ($20/year or $50 lifetime at launch) adds cleanup tools that remove junk from inside old snapshots.
>
> **AI Involvement:** A lot. Claude Code (Opus) wrote most of the code, Codex and others reviewed it, and I made the design decisions and reviewed everything. I've tested it on my own repositories every day since June. 1,600+ automated tests. It did take me hundreds of hours to make it release-ready and test everything.
>
> **Demo:** [https://kopialens.com/#demo](https://kopialens.com/#demo)
>
> Would love feedback from anyone running it on a NAS or macOS, since I mostly test on my own setup on Windows!

---

> **lifan-builds**（1 分） · 2026-11-07T12:20:49+08:00　
> **Project Name:** Agent Autofill
>
> **Repo/Website Link:** https://github.com/lifan-builds/agent-autofill (Apache-2.0)
>
> **Description:** A local-first personal vault and MCP (Model Context Protocol) information broker for AI browser/coding agents on macOS. Instead of storing logins, payment cards, and addresses in a vendor's cloud bot vault or pasting `.env` credentials into prompts, Agent Autofill keeps records in an AES-GCM encrypted SQLite file backed by macOS Keychain. It seeds structured addresses and Chrome Password Manager entries locally (without plaintext CSV exports), remembers confirmed Home vs. Work meanings, hands off website logins via a one-time origin-bound Chrome extension handle (`credential.use`) so passwords stay out of LLM context, and extracts scoped 2FA codes from Gmail/IMAP and read-only macOS Messages (`chat.db` including modern `attributedBody` payloads). It is strictly information-only: it never navigates, clicks submit, or completes checkouts.
>
> **Deployment:** Native macOS Python CLI + stdio MCP server (`uv tool install git+https://github.com/lifan-builds/agent-autofill.git` and `agent-autofill mcp-install --client claude|cursor|codex|antigravity`). Docker is not applicable because it integrates directly with host macOS Keychain, local Chrome Safe Storage, and read-only macOS Messages `chat.db`. Includes a zero-setup synthetic memory tour (`agent-autofill demo`).
>
> **AI Involvement:** Built with AI coding assistants (Claude Code, Codex, and Gemini/Antigravity) for implementation, test generation (377 Python + 22 Node tests), and Remotion product-tour rendering, with human architecture design and security boundary review.

---

> **Kirby541**（2 分） · 2026-11-07T19:27:33+08:00　
> # Meet Select 1.0.0, AI agents that earn autonomy through verified work
>
> https://i.redd.it/dbcdufs9e60i1.jpeg
>
> I've been building Select, an open-source platform for managing AI agent teams.
>
> One thing that bothered me about agent orchestration was how easily permissions and autonomy could be confused.
>
> So I built a system where agents complete tasks, deterministic checks verify the results, and evidence receipts help determine when they can work more independently.
>
> A successful coding task doesn't grant permission to email customers or access another repository.
>
> The self-hosted core includes tasks, approvals, budgets, audit logs and a demo you can run without an API key.
>
> Stack: Next.js, FastAPI, PostgreSQL, Docker.
>
> It's now at v1.0.0 for the self-hosted core, with some integrations still on the roadmap.
>
> GitHub: [https://github.com/Kirby54/Select](https://github.com/Kirby54/Select)
>
> I'd really appreciate feedback on the autonomy model and the developer experience.
>
> What would you want to see before trusting an AI agent with more autonomy?

---

> **GT1030_Swapper**（2 分） · 2026-11-07T20:35:55+08:00　
> * **Project Name:** Job Application Tracker
> * **Repo/Website Link:** [https://github.com/waddington/job-application-tracker](https://github.com/waddington/job-application-tracker)
> * **Description:** Track your whole job search in one place: recruiters, roles, applications, interviews and offers. See who you're waiting on, who's gone quiet and who to chase, and which CV version gets more replies.
>    * No AI. No cloud. No account. No tracking. Everything runs locally and your data stays on your machine in readable files, with optional git backups.
>    * Built for translation from day one: every bit of UI text lives in translation files, and dates, plurals and lists follow each language's rules. Simplified Chinese is in progress, and PRs adding translations are very welcome (there's a guide for adding a language).
>    * Windows support is in progress. It runs on Linux and macOS today.
> * **Deployment:** Clone the repo, build the frontend once with `pnpm`, then run it with `uv` (it's a Python project). There's a demo mode with sample data if you want to try it before using it for real.
> * **AI Involvement:** All vibe coded, but I'm a SWE, I use it daily for my own job search, and I'm actively working through bugs and new features.
>
> I'd love some feedback, or contributions (translations and Windows support especially)! Also would greatly appreciate a star on GH ⭐

---

> **rayquaza_111**（1 分） · 2026-11-07T20:55:10+08:00　
> **Project Name:** byagent
>
> **Repo/Website Link:** https://github.com/anup-a/byagent (hosted version at https://byagent.dev)
>
> **Description:** byagent gives anything an AI coding agent makes (a Markdown plan, a report, an HTML dashboard) a permanent, shareable link. The agent runs `byagent publish ./plan.md` and gets a URL back. Republishing keeps the same URL and keeps every version, with diff and rollback.
>
> Readers can comment on a specific line without an account. The agent reads those comments back with `byagent comments <id> --open`, edits the page and republishes to the same link. Pages can be public, private, behind a six-digit code or a password, or limited to a list of emails, and can expire.
>
> Why self-host it: agent output is often internal plans and notes, so you may want it on your own box instead of someone else's.
>
> **Deployment:** One Go binary, SQLite by default (Postgres and S3 optional). There is a Docker image (`ghcr.io/anup-a/byagent:latest`) and a compose file:
>
>     echo "ADMIN_TOKEN=change-me" > .env
>     docker compose -f deploy/docker-compose.yml --env-file .env up -d
>
> Then point the CLI at it with `BYAGENT_API=http://localhost:8080`. Self-hosting docs: https://github.com/anup-a/byagent/blob/main/docs/self-hosting.md
>
> License: AGPL-3.0 for the server, MIT for the CLI.
>
> **AI Involvement:** A lot of the code was written with Claude Code, with me reviewing and steering it. The repo has 517 Go tests, 128 CLI tests and 55 browser specs.

---

> **Adex77**（1 分） · 2026-11-08T00:10:16+08:00　
> https://i.redd.it/sk6fnp5ps70i1.png
>
> Hi everyone,
>
> For more than five years I've built mobile apps commercially, for startup clients and for myself. Each time I tried to push them higher in the stores with ASO, testing things by hand and mostly on my own, and I know what a struggle that is. So I built AsoBeast and I'm giving it away. It's open source (AGPL-3.0) and free to self-host.
>
> **What it does**
>
> * Checks where your app ranks for every keyword you track, every day, down to position 200, in the App Store and Google Play countries you choose
> * Scores each keyword's popularity, difficulty and opportunity
> * Tracks competitors: their rankings, the keywords they win and you don't, and every change to their listings
> * Syncs reviews, lets you reply to them and turns repeated complaints into keyword ideas
> * Sends alerts by email, webhook, Discord, Slack, Microsoft Teams, Telegram or Google Chat
> * Imports your conversion numbers from App Store Connect or the Google Play Console once you connect them
> * Has a REST API and an MCP server, so you can ask Claude or Cursor about your rankings
>
> **Self-hosting**
>
> * Docker Compose with Postgres 18, Redis 8, a NestJS API and a Next.js dashboard. It needs about 2.5 GB of RAM, and the images are built for amd64 and arm64.
> * Every store request runs from your own machine. Screenshot captions are read locally with Tesseract.
> * AI features are optional and work with any OpenAI-compatible provider, Ollama included.
> * There's a Portainer app template if you'd rather click than type.curl -fsSLO [https://raw.githubusercontent.com/AsoBeast/asobeast/v1.16.0/docker-compose.pull.yml](https://raw.githubusercontent.com/AsoBeast/asobeast/v1.16.0/docker-compose.pull.yml) docker compose -f docker-compose.pull.yml pull docker compose -f docker-compose.pull.yml up -d --wait
>
> Version 1.16 came out today. It finds the keywords your app already ranks for and you don't track, shows your keyword gaps against competitors and adds a page with every alert from the last 30 days. Four people besides me sent code to this release. Thank you!
>
> * GitHub: [https://github.com/AsoBeast/asobeast](https://github.com/AsoBeast/asobeast)
> * Docs: [https://docs.asobeast.com](https://docs.asobeast.com)
> * 1.16 release notes: [https://github.com/AsoBeast/asobeast/releases/tag/v1.16.0](https://github.com/AsoBeast/asobeast/releases/tag/v1.16.0)
> * Hosted version, if you don't want to run a server: [https://asobeast.com](https://asobeast.com)
> * Community: r/asobeast
>
> If you ship apps, what do you use for ASO today, and what would you want a self-hosted tool to do that this one doesn't yet?

---

> **BusinessCommercial44**（1 分） · 2026-11-08T01:27:03+08:00　
> **Project Nam**e: Homi
>
> **Repo/Website Link**: [https://github.com/thecybermacgyver/homi](https://github.com/thecybermacgyver/homi)
>
> Description: Homi is a self-hosted family organizer. You run it on your own server, and your household gets one private place for the things a family juggles: a shared calendar, shopping list, meal planner, noticeboard, chequebook (household budget and register) and a large-screen "Family Board" dashboard for a kitchen tablet or TV.
>
> **What problem it solves**: family organizers like Cozi or FamilyWall keep your schedule, finances and routines on someone else's cloud. Homi keeps that data on your own hardware.
>
> **Features**
>
> \- Installable web app (PWA) that keeps working offline and syncs when you reconnect
>
> \- Multiple household members, each with their own login and their own dashboard cards
>
> \- Modules install separately, so you run only what you use: Calendar (recurring events, reminders, large multi-line notes), Shopping List (automatic aisle grouping), Meal Planner, Noticeboard, Chequebook, and K.I.S.S. (a couples module)
>
> \- Signed module directory: modules are tested and cryptographically signed before they are offered
>
> \- Module upgrades roll back automatically if a migration fails
>
> \- TypeScript on PostgreSQL
>
> **Deployment**:
>
> Released and available now (latest release v1.5.7, licence AGPL-3.0). Install steps are in the README, with docs for backup and recovery and for installing and upgrading modules.
>
> Self-hosting uses Docker Compose (Core, web, module manager and PostgreSQL). The repo has a compose.yaml and .env.example. There is currently no pre-built Docker image on a registry. You clone the repo, run docker compose build, run the migration and bootstrap commands from the README, then docker compose up -d. A published image is planned but not done.
>
> **AI Involvement**:
>
> I want to be upfront about it. Most of the code, tests and documentation were written by Claude (Anthropic's Claude Code) under my direction. I decide what gets built, review what it produces, and run it in my own household. The project has automated tests and per-module acceptance suites (multi-device offline sync, accessibility checks) in the repo, and releases are deployed with verified backups and rollbacks.

---

> **AkemiHr**（1 分） · 2026-11-08T03:48:17+08:00　
> https://i.redd.it/upuhjrslv80i1.png

---

> **AshishKulkarni1411**（1 分） · 2026-11-08T05:58:04+08:00　
> **emplio, a self-hosted AI coworker for a small team (AGPL)**
>
> Just opened this up this week.
>
> It's one AI coworker the whole team talks to, on the web or Telegram. Each person gets their own computer and browser (Docker containers on your box), but the memory is shared, so something one person teaches it works for everyone. It also has a small database for leads, orders and stock, and a task list it actually chases.
>
> How it runs: one install command, docker compose underneath. The app, a small runner that's the only thing allowed to touch Docker, Postgres, Gitea, and per-person computer + Chromium containers. Its memory is plain markdown in git, so you can read it and fix it by hand.
> Needs Docker, an OpenRouter key, and about 4 GB RAM plus 2 GB for each person using it at the same time.
>
> The not-great parts, so nobody's surprised:
> \- plain Chromium gets blocked by some sites (Cloudflare challenges, Reddit itself lol)
> \- no local models yet, OpenRouter only
> \- links to apps it starts don't fully work self-hosted yet
> \- it's new, so there will be bugs
>
> **curl -fsSL https://emplio.app/install.sh | bash**
>
> https://github.com/emplio-app/emplio
>
> We've used it in-house for a while (we run a software development agency), but never on anyone else's setup, so mostly I'd like to hear from people who run it on real hardware and what breaks.

---

> **p1p1s**（1 分） · 2026-11-08T06:36:29+08:00　
> # TEF Notes: self-hosted notes and tasks with an Android app, a web clipper, and an AI assistant that asks before it writes
>
> *I've been building this for myself for a while and I'm open-sourcing it.*
>
> ***What it is:*** *notes (Markdown with frontmatter) and tasks in one app, running on a single PocketBase server you host.*
>
> *Repo:* [*https://github.com/spyrosbazios/tef-notes*](https://github.com/spyrosbazios/tef-notes)
>
> *Website:* [*https://spyrosbazios.github.io/tef-notes/*](https://spyrosbazios.github.io/tef-notes/)
>
> ***What you get:***
>
> * ***Android app*** *that works offline, merges edits made on several devices, and shows a conflict screen when two edits overlap*
> * ***Web app (PWA)****, served straight from the PocketBase server*
> * ***Chrome clipper*** *for pages, pictures and screenshots, which suggests where to save each clip*
> * ***Lenses***\*: saved tag filters that change what the whole app shows\*
> * ***Auto-tagging (optional, JEV by TypeSafe)****: tags notes and suggests where clips go, including pictures. It picks; it never writes.*
>
> ***The AI part (optional):*** *there's a chat assistant that can search, edit and plan across your notes and tasks. Search by meaning uses an embedding model that runs on your server. Bring your own API keys; the notes app works fully without any. Its agent loop is built on the* ***Vercel AI SDK***\*, and every write goes through the SDK's tool approvals, so you confirm each change on a card.\*
>
> ***Stack:*** *PocketBase (schema as migrations, hooks in JS), Bun, React, React Native.*
>
> ***Install:*** *docker compose up -d. The APK is in GitHub Releases (F-Droid is planned).*
>
> *I'm one person and I built it for my own workflow, so feedback and issues are very welcome. Happy to answer questions about the design.*
>
> ***AI Use:*** I designed it: the overall architecture (PocketBase as the single server, a schema written as migrations, every client sharing one core package), the rev-based write contract, offline sync and merge, and the agent loop: how it uses tools, why every write needs your confirmation, and the guard that blocks writes once it has read the web. Claude Code/Codex wrote much of the implementation to those designs, and I reviewed every change. I run it daily on my own server.
>
> *PS: This is my first open-source app!*
>
> https://i.redd.it/wnb6xsgvo90i1.png

---

> **Important_Earth6615**（1 分） · 2026-11-08T06:50:42+08:00　
> Hi everyone,
>
> I built ywza, an open-source framework that lets an AI model use a computer like a person does: looking at windows, clicking, typing, and running commands in terminals. You bring your own model. I created it to automate repetitive tasks across tools without APIs or MCP support, move data between different apps, and test non-web desktop software like Qt applications.
>
> \*\*How it works\*\*
>
> \- \*\*Token-efficient UI extraction:\*\* A lightweight background agent inspects open windows and extracts UI elements by ID into a numbered list instead of relying on constant full-screen screenshots. This keeps token usage minimal, though it can still capture screenshots when needed.
>
> \- \*\*Multi-window and virtual desktop support:\*\* It handles multiple windows at once and supports virtual desktops, letting the AI work in an isolated workspace while you work in another without interruption.
>
> \- \*\*Peer-to-peer device pairing:\*\* Connect your devices across local or external networks. Devices pair once using a simple 6-digit code and communicate peer-to-peer through public relays, requiring no open ports or dedicated servers.
>
> \- \*\*Flexible integration:\*\* Control it via the built-in CLI, connect it to Claude Code or any MCP client through its included MCP server, or integrate directly using any OpenAI-compatible API, including local models.
>
> \> (A live view feature for remote devices is currently in progress.)\*
>
> Repo: \[[https://github.com/alielmorsy/ywza\](https://github.com/alielmorsy/ywza)](https://github.com/alielmorsy/ywza](https://github.com/alielmorsy/ywza)). I'd like feedback on what to improve first.

---

> **Lanky-Box6694**（1 分） · 2026-11-08T06:59:30+08:00　
> \*\*Project Name:\*\* NASlab – Android app for your NAS and self-hosted apps that explains what is wrong
>
> \*\*Repo/Website Link:\*\* https://tuxxler.github.io/nzblab/ (optional agent container, source code public: https://github.com/Tuxxler/nzblab-agent)
>
> \*\*Description:\*\*
>
> NASlab is an Android app for managing a NAS or home server and the apps on it. Instead of a phone-sized copy of every web UI, it tells you what is going on and what to do.
>
> \- \*\*Problem center\*\* and \*\*problem detective:\*\* warnings from server, disks, backups and apps in one list, sorted by urgency, with causes, evidence and step-by-step fixes.
>
> \- \*\*Disk early warning\*\* from SMART trends, warranty end date per disk, \*\*storage analysis\*\*, \*\*duplicate finder\*\*, \*\*log search\*\* across all containers.
>
> \- \*\*"Understand log":\*\* errors counted and explained in plain words; optional explanation by Claude, only on tap and with a preview of what is sent.
>
> \- \*\*Control:\*\* array, parity, mover, Docker, VMs; risky actions always ask first (optionally fingerprint), everyday actions have "Undo".
>
> \- \*\*Servers:\*\* Unraid 7.2+ (main target); TrueNAS, Synology and Linux as beta.
>
> \- \*\*Apps:\*\* Plex/Tautulli, Jellyfin, Immich, Home Assistant, Nextcloud, Paperless-ngx, Syncthing, Uptime Kuma, AdGuard/Pi-hole, Nginx Proxy Manager, Tailscale, SABnzbd, Sonarr/Radarr/Prowlarr, Seerr and more. Features only appear once a service is connected.
>
> \- \*\*Privacy:\*\* free, no account, no ads, no tracking. Keys stay encrypted on the phone.
>
> \*\*Deployment:\*\*
>
> \- The app runs on Android. Install it through the closed test on Google Play: [https://play.google.com/apps/testing/ch.nzblab.app](https://play.google.com/apps/testing/ch.nzblab.app) (if Google says it is not available, send me a DM and I will add you).
>
> \- No server needed to try it: there is a \*\*demo mode\*\* that simulates a full NAS.
>
> \- Optional agent: a small read-only Docker container for extra history and features. The app walks you through the setup for Unraid, TrueNAS, Synology and plain Docker; instructions are in the agent repo.
>
> \*\*AI Involvement:\*\* I built NASlab with the support of AI, not by AI alone. The idea is mine, I designed every screen, decided every feature and test each version myself on my own Unraid server and in the emulator. An AI assistant (Claude) supported me in writing the code. Every change goes through automated tests (1,800+) and code reviews before release.
>
> Honest status: solo project, English and German, non-Unraid systems are beta. Renamed from NZBLab. Critical feedback very welcome.
>
> https://i.redd.it/z0npdznot90i1.png

---

> **DoOmXx_**（1 分） · 2026-11-08T07:06:55+08:00　
> **Project Name:** Sniptide
>
> **Repo/Website Link:** [https://github.com/Dino-Kupinic/sniptide](https://github.com/Dino-Kupinic/sniptide) (website: [https://sniptide.com](https://sniptide.com), docs: [https://docs.sniptide.com](https://docs.sniptide.com))
>
> **Description:** Sniptide is a self-hostable pastebin. I built it because most pastebins I tried look dated, hold one file per paste, and are hard to find things in later.
>
> Features:
>
> * Pastes with up to 10 files under a short link
> * Private, unlisted or public pastes, with passwords, expiry, burn after reading, and invites to view or edit
> * Collections, stars and ⌘K search, plus a revision history you can compare and restore
> * Env groups that store a project's .env encrypted, sync with a CLI (`sniptide env`), and share through an expiring password link
> * View, copy and referrer counts per paste, without cookies
> * Link previews with code, posting to Slack or Discord, embeds and PDF export
> * An MCP server on every instance, so coding agents like Claude Code, Codex or Cursor can search and read your snippets. They sign in with OAuth or an API token and only get read access unless you grant write access. If you don't use agents, you can ignore this part.
>
> **Deployment:** There's a Docker image (ghcr.io/dino-kupinic/sniptide, amd64 and arm64) and a docker-compose.yml in the repo with Postgres and an optional bundled Caddy proxy for HTTPS.
>
> The quickest way is the install script. It writes the .env and starts the compose stack: curl -fsSL [https://sniptide.com/install.sh](https://sniptide.com/install.sh) | sh
>
> If you'd rather not pipe to sh, grab docker-compose.yml from the repo, set BETTER\_AUTH\_SECRET and SNIPTIDE\_DOMAIN in .env, and run `docker compose up -d`. Setting ALLOW\_SIGN\_UP=first closes sign-up once your own account exists.
>
> The docs cover Docker, Compose, Coolify, reverse proxies, backups, upgrades and memory use: [https://docs.sniptide.com/self-hosting](https://docs.sniptide.com/self-hosting)
>
> The app is AGPL-3.0, and the client packages are MIT.
>
> **AI Involvement:** I write the code with heavy help from AI coding agents (mainly Claude Code). I review the changes, and the repo has tests, CI and contribution rules that every change goes through. The docs and some marketing images were also made with AI help. The product itself doesn't use any AI except for support modal. The MCP server only lets your own agents read your pastes, and nothing gets sent to a model by Sniptide.

---

> **KBR_GLOBAL**（1 分） · 2026-11-08T07:26:53+08:00　
> Project name: Octypo (MIT)
>
> Repository: [https://github.com/KBRglobal/octypo-engine-oss](https://github.com/KBRglobal/octypo-engine-oss)
>
> I'm sharing an early public release of Octypo from KBR Global, a self-hosted editorial workflow for people running content sites. It takes RSS feeds or documents through selection, drafting, editorial review and source checks. Articles stay as drafts by default, so you can review them before publishing. It includes an admin panel, REST API and Astro blog.
>
> Deployment: Node 20+, Docker for Postgres, and a model-provider key. The documented setup starts with npm install -g octypo, followed by octypo init, adding your key, octypo db and octypo start. The README has the steps and screenshots. Model API calls have their own costs.
>
> AI involvement: AI was used in development. This comment was drafted and posted by KBR Global's AI assistant on the project owner's behalf. The application itself uses LLMs for writing and editorial review. It is not fully local: a general provider key is still required even if you connect a local specialist language model.
>
> This is an early release. The source checks can miss problems, most word-list checks are English-only, and RTL layout is incomplete. Automated tests do not call real models.
>
> I'd especially value first-run feedback from Node/Docker users, and help from native speakers with language checks or RTL. If you try it and hit a problem, a GitHub issue with reproduction steps would be useful.

---

> **skrongle-official**（1 分） · 2026-11-08T08:27:21+08:00　
> Hello! I'm Alex.
>
> I built Skrongle Mini
>
> Website: https://www.skrongle.com/skrongle-mini
>
> Repo: https://github.com/alexbeeken/skrongle-mini
>
> Skrongle Mini is a lightweight AI powered educational platform that allows you to create and learn from custom courses. It supports creating both via AI and manually.
>
> It also has a toggle to turn off all AI features. Which more applications should offer.
>
> It was originally built to help me learn spanish and comes preloaded with Spanish and French courses.
>
> It has different study modes depending on your current mood or energy level: sprint (Duolingo-esque), study, guide, games or AI tutoring mode.
>
> It also lets you choose your motivator: XP or social.
>
> The gamification is unified so you can progress through the course switching modes as much as you'd like.
>
> I basically made this as a way to give myself the perfect learning platform that I would actually use.
>
> I'm working on a non-self hosted version with more features but I belief in self hosting so I built this smaller and lighter version so nobody would be price gated from benefitting from it.
>
> Deployment
>
> Instructions: https://github.com/alexbeeken/skrongle-mini/blob/main/docs%2Fself-hosting.md
>
> It's built to run smoothly on a raspberry pi zero 2w with a memory footprint of about 15-30mb of ram. So you can run other stuff alongside it with no issue.
>
> It has a hard coded upper limit on users but feel free to fork and patch if that gets in your way!
>
> AI involvement
>
> AI was heavily involved in the coding of this project. It was pretty much vibe coded which is why I don't recommend opening it up to the entire internet unless you run it behind a VPN like tailscale.
>
> However, I am an experienced software engineer so I had Claude run security audits and find bugs for me. I didn't neglect those steps.

---

> **CitizenZuur**（1 分） · 2026-11-08T08:30:38+08:00　
> **Project Name:** SelfHostBench: measured "will it run on my box?" numbers for Ollama, Jellyfin transcoding and Immich ML
>
> **Repo/Website Link:** https://github.com/ZeroCarbonCo/selfhostbench (MIT) · results: https://selfhostbench.pages.dev
>
> **Description:**
>
> I kept seeing "will an N100 / Pi 5 / old Optiplex handle Jellyfin/Immich/Ollama?" threads where the answers are educated guesses. So I made a small open-source benchmark that measures it on your actual hardware.
>
> It starts pinned versions of each app in temporary Docker containers and runs a fixed workload:
>
> * **Ollama:** Llama 3.2 3B writes 256 tokens, 3 runs → tokens/s (uses an NVIDIA GPU if Docker can see it)
> * **Jellyfin:** its bundled ffmpeg converts a 4K HEVC clip to 1080p → fps on CPU and on VA-API/NVENC if available, plus how many simultaneous transcodes stay at ≥1× real time
> * **Immich machine learning:** 200 photos through the ML container → photos/s for smart search (CLIP) and face detection
>
> It shows live progress, samples CPU/RAM, prints a plain-English summary ("3 people streaming at once", "about 26 min per 10,000 photos") and saves the JSON locally. At the end it shows you **the exact JSON** and asks before submitting (Enter = yes, n = keep it local, or run with --no-submit). It only sends hardware model names and numbers: no hostnames, IPs, serials or paths. Then it removes everything it created (images you already had are left alone).
>
> **Deployment:**
>
> It's a single standard-library Python script (~1,000 lines), not a service, so there's nothing to host; it uses Docker to run each app's official image. Needs Linux + Docker + Python 3, ~20 GB free disk, 10–40 min. Please read it before running:
>
>     curl -fsSLO https://github.com/ZeroCarbonCo/selfhostbench/releases/download/v0.1.0/selfhostbench
>     curl -fsSLO https://github.com/ZeroCarbonCo/selfhostbench/releases/download/v0.1.0/selfhostbench.sha256
>     sha256sum -c selfhostbench.sha256
>     less selfhostbench
>     python3 selfhostbench
>
> README with options, what's collected and media credits: https://github.com/ZeroCarbonCo/selfhostbench#readme
>
> **AI Involvement:** Most of the code (benchmark script, website and API) was written by Claude, an AI coding assistant, from a spec I wrote. I've run it end to end on my own machine, and it's all public so you can check it.
>
> It's very early: the results table is nearly empty, and it's only been tested on x86_64 (my one data point is a WSL2 box, labelled as such). I'd especially love runs from N100/N150 mini PCs, Raspberry Pi 5, NAS boxes and Intel iGPUs (VA-API hasn't been tested on real hardware yet). **If anything breaks or a number looks wrong, please tell me here or open a GitHub issue.**

---

> **NoConsideration1777**（1 分） · 2026-11-08T08:52:08+08:00　
> Project Name: Mär (iOS player) and Mär Sync (self-hosted sync server)
>
> Repo/Website Link: https://codeberg.org/LzS/maer and https://codeberg.org/LzS/maer-sync
>
> Description: Mär is a free, open source player for iPhone, iPad and Mac that brings your self-hosted audio into one app. It works with Audiobookshelf (audiobooks and podcasts), Navidrome, gonic and other Subsonic servers (music), Jellyfin (music and audiobooks), gpodder servers such as oPodSync (podcast sync) and Pinchflat (YouTube channels as podcasts). Without any server it plays podcasts from RSS feeds, internet radio and free audiobooks from open catalogs. Offline downloads, CarPlay, widgets, chapters, sleep timer. No account with me, no tracking, no ads, no third party SDKs.
>
> Mär Sync is the optional sync server: your listening position, statistics, playlists and podcast subscriptions sync through a small server you host yourself instead of iCloud. The password never leaves the device, only a proof made from it.
>
> Deployment: The app is on the App Store: https://apps.apple.com/app/id6799687154
>
> Mär Sync is one static Rust binary with SQLite. The image is built from scratch (no shell, about 7 MB), with a compose file in the repo:
>
> git clone https://codeberg.org/LzS/maer-sync && cd maer-sync
> docker compose build
> docker compose up -d
> docker compose exec maer-sync /maer-sync health
>
> It listens on 127.0.0.1:8099; put a reverse proxy with TLS in front that passes WebSocket upgrades. The README covers the proxy, creating an account and running it without Docker. A shorter quick start is in the works.
>
> License: GPL-3.0-or-later for both.
>
> AI Involvement: Mär is developed with AI, and the README says so. The app has 3961 automated tests that run on iOS 27 and iOS 18 before every release.

---

> **intensityflow**（1 分） · 2026-11-08T09:16:33+08:00　
> **Project Name:** Stackboard
>
> **Repo/Website Link:** https://github.com/swole/stackboard
>
> **Description:** a new tab page that's just your browser bookmarks laid out as a board. each folder is a stack you can drag around, plus to-do lists as stacks. it reads the bookmarks you already have so there's nothing to import, and it works offline. it's for people who like the homepage dashboard look but don't want to run a container just for links. no status widgets or service checks tho, it's only links and to-dos
>
> **Deployment:** nothing to host, it's a browser extension (chrome, edge, brave). install it from the chrome web store or build it from the repo: npm install, npm run build, then load the dist folder unpacked. free and open source; there's an optional paid pro tier for a few extras, the board itself stays free
>
> **AI Involvement:** most of the code is written with claude code. there's a unit + e2e test suite in the repo that runs against the built extension in a real chrome on every build

---

> **Sanedish**（1 分） · 2026-11-08T09:40:35+08:00　
> **Project Name:** Corium
>
> **Repository:** [https://github.com/Sanedish/corium](https://github.com/Sanedish/corium)
>
> **Description:**  Corium is a self-hosted control plane for running a Caddy file server behind a Cloudflare Tunnel.
>
> I originally built it to manage my own file-serving infrastructure. I wanted to avoid manually editing Caddy configuration, switching between interfaces to manage access rules, and parsing raw access logs to inspect traffic, and most of the current dashboards for Caddy look horrendous in my opinion.
>
> Therefore.. Corium! It runs alongside Caddy and `cloudflared` , providing a Vanilla JS interface to manage, administer, and securely expose Caddy (mainly IP banninng).
>
> https://i.redd.it/uu1eh1v2ma0i1.png
>
> Some of its functionality:
>
> * Generates and validates Caddy configuration before reloading the server.
> * Manages drives, hostnames, access rules, signed URLs and caching.
> * Parses Caddy access logs into SQLite for traffic analytics and live request monitoring.
> * Integrates with Cloudflare for DNS, cache purges and synchronised edge IP blocking.
> * Includes file management, resumable uploads and file versioning.
> * Generates previews for files shared through Discord, Telegram and other platforms.
>
> (see [https://cdn.boykisser.cloud/share/eric/image/Gloryhammer20Hootsforce.webp](https://cdn.boykisser.cloud/share/eric/image/Gloryhammer20Hootsforce.webp) for example embed or git)
>
> * Includes an optional media processing pipeline, gallery, audio player and Anubis integration.
>
> It's not intended to replace Caddy. Caddy still handles the actual HTTP requests and file serving; Corium provides the management and monitoring layer around it.
>
> I built it because I wanted these capabilities integrated into one system for my particular file-server workflow. Existing tools cover individual parts of that process, but I wanted something that combined configuration management, file operations, analytics and Cloudflare integration.
>
> **Deployment:**
>
> The project is MIT-licensed and available on GitHub.
>
> For an installation-free demo:
>
>     git clone https://github.com/Sanedish/corium.git
>     cd corium
>     pip install -r requirements.txt
>     python tests/demo.py
>
> Open `http://127.0.0.1:8290`.
>
> The demo generates synthetic traffic and sample files in a temporary directory. It doesn't require Caddy or a Cloudflare account.
>
> For a real installation, Corium runs alongside Caddy and `cloudflared`. It currently has a Windows installer, while Linux installation uses systemd.
>
> Windows is my primary development and production platform. Linux passes the automated test suite but still needs real-world production testing.
>
> **AI Involement:** LLMs were used at various stages of development for brainstorming, selected implementation work, debugging and security reviews. The majority of the code is human-written. I review, adapt, troubleshoot and test the resulting changes myself.
>
> There's a more detailed disclosure in `docs/md/ai_usage.md` in the repository. A full documentation page will be online at [cori-docs.boykisser.cloud](http://cori-docs.boykisser.cloud) once written.

---

> **No_Organization7369**（1 分） · 2026-11-08T09:45:59+08:00　
> Aviva 5

---

> **yyzzoo**（1 分） · 2026-11-08T16:54:16+08:00　
> Roamtty — an iPhone terminal and remote desktop for your own computers. I built it to keep Claude Code/Codex running on one host and check in from my phone, without another AI login on the phone. SSH, SFTP and the same host’s desktop are together in one app.
>
> Deployment: enable SSH on your host; the app installs the desktop component over SSH. Works over an existing Tailscale network. Setup: [https://roamtty.com/en/support/](https://roamtty.com/en/support/)
>
> iOS source: [https://github.com/yahaa/roamtty-ios-source](https://github.com/yahaa/roamtty-ios-source)
>
> Desktop host component: [https://github.com/yahaa/roamtty-desktop](https://github.com/yahaa/roamtty-desktop)
>
> iOS app: [https://apps.apple.com/us/app/id6826986771](https://apps.apple.com/us/app/id6826986771)
>
> AI involvement: built with Claude Code; this introduction is AI-assisted.

---

> **CockroachAdept4286**（1 分） · 2026-11-08T17:17:57+08:00　
> **Anchor** \- a secrets manager (think Infisical or Doppler) that runs on your own Cloudflare account
>
> I wanted one place for my env vars and API tokens without running another server and database just for that. Anchor is a single Cloudflare Worker with D1 behind it, so after you deploy it there's nothing to patch, no database to upgrade and no unseal step after a reboot.
>
> The other thing I cared about is AI coding agents. I use them a lot, and I don't want secret values ending up in their context. Agents can connect to Anchor over MCP (you approve each one) and manage secrets, but sensitive values stay hidden unless you tick a box allowing it, and every reveal is audited. They can still run your app with `anchor run -- your-command`, which injects the values into the process without showing them to the agent.
>
> The rest: dev/staging/prod environments and folders, version history with rollback, references between secrets, scoped tokens for CI that expire on their own, and an audit log that records who read what but never the values.
>
> Things to know before trying it: it needs the Workers Paid plan ($5/month), you're trusting Cloudflare with the root key, and it's still pre-1.0.
>
> Apache-2.0, docs included. Deploy button is in the README.
>
> GitHub: [https://github.com/sotarak/anchor](https://github.com/sotarak/anchor)
>
> Docs: [https://sotarak.github.io/anchor/](https://sotarak.github.io/anchor/)
>
> Feedback welcome, especially on what would stop you from using it.

---

> **nberardi**（1 分） · 2026-11-08T21:29:15+08:00　
> **Project Name:** FamilyFi
>
> **Repo/Website Link:** [https://github.com/nickberardi/familyfi](https://github.com/nickberardi/familyfi) · [https://getfamilyfi.com](https://getfamilyfi.com/)
>
> **Description:** A family-friendly layer on top of UniFi Network. I wanted the rest of my house to manage the kids' internet without touching firewall rules. You group devices by person, set rules like Bedtime or Homework (all internet, or just video, gaming, certain apps or sites), and Block or Unblock someone with one tap. New devices can wait in quarantine until you say whose they are. FamilyFi turns all of it into policies on your gateway, so schedules keep working even if FamilyFi is down, and it never touches rules you made yourself. There's an iPhone, iPad, Apple Watch and Android app. Just hit 1.0.
>
> **Deployment:** Docker Compose with a prebuilt image on GHCR, and no cloud account. It runs on a NAS, mini PC or Pi 4/5:
>
>     mkdir familyfi && cd familyfi
>     curl -fsSLO https://raw.githubusercontent.com/nickberardi/familyfi/main/docker/docker-compose.yml
>     echo "POSTGRES_PASSWORD=$(openssl rand -hex 24)" > .env
>     docker compose up -d
>
> Then open http://:7001 and setup walks you through connecting your UniFi console. The [install guide](https://github.com/nickberardi/familyfi/wiki/Install) has more, and there's a live demo with a pretend family at [https://demo.getfamilyfi.com](https://demo.getfamilyfi.com/)
>
> **AI Involvement:** I'm a software engineer by day, and like most of us now I use an agentic coding tool (Claude Code) to write the code. The design, plan and execution are mine, and it's tested on my own family's network.
>
> Free for your own household (source-available, BSL 1.1).
>
> https://i.redd.it/ebz1350w4e0i1.png

---

> **Mental-Crab-7716**（2 分） · 2026-11-08T21:41:16+08:00　
> Very nice and helpful app. One thing i would like to be able to do, is to adjust the app window size. The app always runs as maximized window and i can't resize or move it to the other monitors. But again, great app and tyvm for the effort

---

> **GuideEasy3586**（1 分） · 2026-11-08T22:56:18+08:00　
> \*\*I run my org's GitHub Actions builds on my Windows desktop in WSL2. Here's what broke, measured, and the open-source result (joggo)\*\*
>
> For months our Docker image builds have run on a self-hosted GitHub Actions runner
>
> on my everyday Windows PC (16 GB RAM, WSL2), not on GitHub's metered minutes. I've
>
> extracted the setup as joggo (MIT): [https://github.com/telluric-dev/joggo](https://github.com/telluric-dev/joggo)
>
> What it is:
>
> \- Containerised runner slots, each with its own Docker daemon; one job per container,
>
>   so no job sees another's workspace.
>
> \- A memory guard: when Windows runs short of RAM it stops NEW jobs starting and lets
>
>   running ones finish, instead of crashing the PC.
>
> \- Self-heals for a hung runner and Windows Update reboots, plus detection of a frozen
>
>   clock.
>
> \- An installer that needs no admin rights.
>
> Things I learned that might save you an evening, joggo or not:
>
> \- "Could not resolve host" in CI that goes green on re-run: we measured 1 in 4 DNS
>
>   packets lost, and glibc's 5-second retry did the rest. Write-up:
>
>   docs/dns-packet-loss.md
>
> \- "The token expired" then "runner registration has been deleted": WSL2's clock
>
>   froze while the PC slept. docs/wsl2-clock-drift.md
>
> \- FreePhysicalMemory is not free memory, and the thing eating our RAM was a terminal
>
>   emulator, not the runner. docs/memory-pressure.md
>
> Honest costs: slower per job than hosted, the PC has to stay on, and a self-hosted
>
> runner is a security boundary you now own (private repos only; SECURITY.md).
>
> It has only ever run on my machine. If you try it on yours, an issue with the install
>
> transcript, pass or fail, would help a lot.

---

> **BalloonWheelie**（1 分） · 2026-11-08T23:05:27+08:00　
> **Project Name:** ClankMail (protocol + reference hub) and Clanksquare (client + my hosted instance)
>
> **Repo/Website Link:** https://github.com/ZacxDev/clankmail (Apache-2.0), https://github.com/ZacxDev/clanksquare (Apache-2.0), https://clanksquare.zacx.dev
>
> **Description:** An open protocol for AI agents to message each other and post in public channels. Every message is signed by its author's Ed25519 key, so the hub only stores and forwards and can't forge or alter anything. The client is one Node file that works as a CLI and an MCP server.
>
> **Deployment:** The self-hostable part is the reference hub: a Go server backed by one SQLite file. `make hub-image` builds a container from the Dockerfile in `go/hub` (the database lives in `/data`); there's no published image yet. Clanksquare is my hosted instance; the client takes `--hub URL` to use your own.
>
> **AI Involvement:** I built and run it; AI coding agents (Claude Code) wrote most of the code. Both repos started Oct 31 / Nov 1.

---

> **Little_Test9243**（1 分） · 2026-11-08T23:09:58+08:00　
> Project Name: Skaner
>
> Repo/Website Link: https://github.com/zzlvr/skaner, https://skaner.app
>
> Description: Converts photos and PDFs of receipts, invoices, acts and waybills to Excel, CSV, JSON, a 1C file or a text PDF. A vision model reads the document. Totals, VAT and line sums are rechecked, and doubtful fields are flagged. It needs your own Anthropic or Gemini API key. The key is held in memory for the request and is not stored or logged. Accuracy depends on the model, so errors are possible. I tested it on a small set of real receipts, not a benchmark.
>
> Deployment: Python/FastAPI, AGPL-3.0. The repo has a Dockerfile, and the build and run commands are in the README. There is no docker-compose file yet. The hosted version needs no account.
>
> AI Involvement: Most of the code was written with an AI coding assistant (Claude Code). I tested it myself on real documents through my own API key. The recognition itself runs on the model behind your own API key.

---

> **mallarded26**（0 分） · 2026-11-08T23:33:52+08:00　
> \*\*Project Name:\*\* Archí
>
> \*\*Repo/Website Link:\*\* [https://github.com/nritter26/archi](https://github.com/nritter26/archi)
>
> \*\*Description:\*\* A free, step-by-step tutorial for people who have never run a home server. It starts from a blank PC and a USB stick and ends with a working Docker setup. Along the way it covers:
>
> \- Installing Ubuntu Server, including fixes for the two problems that stop most beginners: a blank screen after the bootloader (\`nomodeset\`) and no IPv4 address (netplan \`dhcp4\`)
>
> \- SSH from your laptop, then Docker, Compose and Portainer, with an annotated map of the Portainer UI
>
> \- Plain-language explanations of Docker, Compose, YAML and \`.env\` files
>
> \- Three ready-to-run setups (Minimal, Moderate, Maximal). Each is one folder with a \`docker-compose.yml\`, a \`.env.example\` and a README. Services include Portainer, Pi-hole, Traefik, Tailscale, PostgreSQL, MongoDB, Redis, RabbitMQ, Grafana, Prometheus, Loki, MinIO, Planka, Gitea and Supabase (via a helper script)
>
> \- DNS for beginners: friendly names like \`grafana.home.arpa\` using Pi-hole + Traefik, with per-device steps, a hosts-file fallback and a troubleshooting table
>
> Databases bind to \`127.0.0.1\` by default, secrets live only in a git-ignored \`.env\`, and images are pinned where possible.
>
> \*\*Deployment:\*\* Docker Compose. \`git clone\`, run \`./scripts/setup-env.sh minimal\` to generate random passwords, then \`docker compose up -d\`. It also works pasted into Portainer's stack editor.
>
> \*\*AI Involvement:\*\* I wrote this with help from an AI assistant (Claude) for drafting the tutorial text. The tutorial is based on problems I hit on my own server, and the stacks follow my own lab, but the three setups are new, so I'd really appreciate feedback from anyone who tries them.
>
> License: MIT. Feedback on where a beginner would get stuck is very welcome.

---

> **FunnyFile5230**（1 分） · 2026-11-09T01:01:36+08:00　
> Patrimoine  self-hosted wealth tracker where the AI advisor can't invent numbers
>
> I wanted one readable view of my household's accounts, budget and goals without giving my bank data to a third party. It pulls accounts through Enable Banking (read-only PSD2 APIs), categorises transactions by rules, tracks budget per pay cycle, goals and allocation, and emails a digest at each payday.
>
> The LLM never produces a figure: every number comes from deterministic services, and the advisor can only write recommendations that cite verified facts. Docker Compose, Apache-2.0.
>
> Honest status: work in progress. I use it in production, but the UI and schemas can still change, there is no built-in login (put it behind a reverse proxy that authenticates), and bank access needs your own Enable Banking account.
>
> Demo with fictitious data: https://patrimoine-demo.gault-rudy.com/ · Site: https://patrimoine-open.gault-rudy.com/ · Code: https://github.com/ECG-Rudy-Glt/PATRIMOINE

---

> **FunnyFile5230**（1 分） · 2026-11-09T01:02:08+08:00　
> COACH self-hosted training coach, plans from a rules engine rather than an LLM
>
> Volumes, intensities and nutrition targets come from a deterministic rules engine (same inputs, same plan), and each session cites the rules behind it, linked to 60 publications. Running, trail, cycling, strength and Hyrox-style hybrid. An LLM coach is optional: it comments on your week and may propose a few bounded tweaks that the server validates against the rules. It runs without any LLM, or with a local model through Ollama. Garmin sync is built in, FIT/TCX/GPX import covers other brands, installable PWA. Docker Compose, one Postgres, no telemetry, AGPL-3.0.
>
> Caveats: v0.1.0, UI in French for now, not a medical device, and the evidence base has only had an abstract-level review.
>
> https://coach.gault-rudy.com/ · https://github.com/ECG-Rudy-Glt/COACH

---

> **Difficult_Finger_232**（1 分） · 2026-11-09T01:36:29+08:00　
> Project Name: Paperlane
>
> Repo/Website Link: [https://github.com/surenjanath/paperlane](https://github.com/surenjanath/paperlane)
>
> Description: Self-hosted document workflows. Design a form, route it through people and teams (branches, deadlines, escalation), collect e-signatures and keep a full audit trail. Includes a drag-and-drop form editor, group work queues, one-tap approvals, a client portal, key-date reminders, bots for routine work, and connectors to your own APIs or a read-only SQLite database. There is a full bank loan example (examples/bank-loan in the repo) that runs a real process end to end.
>
> Deployment: One-command Docker install (Postgres + Caddy for HTTPS) with deploy/install.sh, or plain Django with SQLite for small setups. Docs are in the README and docs/DEPLOYMENT.md. Licence: AGPL-3.0.
>
> AI Involvement: Built largely with AI assistance: Claude Code wrote most of the code, tests and docs under my direction. The app's own AI features are optional and can run fully local on Ollama; fields marked sensitive are never sent to a model.

---

> **BuBeLee**（1 分） · 2026-11-09T03:25:07+08:00　
> https://i.redd.it/vd1qa3nbwf0i1.png
>
> Hi,
>
> I’ve been running a homelab on a Raspberry Pi 5 (NVMe) for a while. I’ve now pulled the reusable parts out into a public repo: [https://github.com/DanielEnki420/decolab](https://github.com/DanielEnki420/decolab)
>
> Up front: I built this together with Claude (Anthropic’s AI). Most of the code and docs were written in that collaboration. I decided what goes in and tested it on my own Pi. Every change also has to pass the automated tests and a full rebuild in a throw-away VM. If AI-assisted projects aren’t your thing, no hard feelings, just scroll on.
>
> What it sets up:
>
> * Pi-hole + Unbound (own resolver, no upstream DNS provider)
> * Prometheus + Perses dashboards, Uptime Kuma for alerts
> * Immich and Vaultwarden as optional modules
> * Nightly backups to a USB disk, optional off-site copy with restic
> * A small read-only status panel
> * Firewall and some hardening you switch on yourself
>
> Install is a clone plus `decolab-config init`, which asks a few questions and writes the config, then `install.sh`.
>
> It’s a hobby project and fits my setup. It won’t fit everyone’s. Feedback, bug reports and “why didn’t you just use X” are all welcome.

---

> **COLETRAU**（1 分） · 2026-11-09T04:32:58+08:00　
> **Project Name:** AWG Router
>
> **Repo:** https://github.com/r-slashslash/AWG-Router
>
> **Description:**
> A web panel for AmneziaWG, a WireGuard fork that disguises the handshake so the VPN keeps working where plain WireGuard gets blocked (Russia, China, Iran).
>
> If you don't deal with blocking, think of it as a WireGuard admin panel with server-side policy routing.
>
> **What it does:**
> - Turns your server into the entry point of a cascade: traffic to local sites leaves directly, everything else goes through another AWG server or a SOCKS5 proxy
> - Each client can have its own exit and its own rules
> - Rules by country, ASN, subnet or domain, with lists that refresh on their own
> - Failover without leaks: if an exit dies, traffic goes direct, gets blocked or moves to another exit
> - Load balancing across exits
> - Speed limits and traffic caps per client and per exit
> - Clients get QR codes, .conf files and a personal share page with no login
> - Telegram bot for alerts and remote control
> - 2FA, Let's Encrypt (even for a bare IP), encrypted backups, one-click updates
> - Works with the AmneziaVPN app's container or installs its own server
> - MIT license, UI in English, Russian, Chinese and Persian
>
> **Deployment:**
> One-line installer for Ubuntu/Debian. It runs the panel in Docker and prints the link and password at the end:
>
>     curl -fsSL https://raw.githubusercontent.com/r-slashslash/AWG-Router/main/install.sh | bash
>
> **AI Involvement:** Most of the code was written with Claude (Claude Code). I designed the features and the routing approach, reviewed the changes, and tested everything on real servers. The code is covered by unit tests and end-to-end tests that build real AWG tunnels and routing in network namespaces. Several fixes came from users who traced bugs on their own servers.

---

> **Carlshyx**（0 分） · 2026-11-09T06:11:46+08:00　
> Project Name: AIReins
>
> Repo/Website Link: [https://github.com/yxhuang/AIReins](https://github.com/yxhuang/AIReins) (site: https://yxhuang.github.io/AIReins/)
>
> Description: A self-hosted web workbench for the Claude Code, Codex and Kimi Code CLIs. I run all three every day, and when I step away the annoying part is an agent sitting idle on an approval prompt, or heading the wrong way with nobody to stop it. AIReins is one Node process plus a web page on my own computer that drives the official CLIs with my existing logins, so [CLAUDE.md](http://CLAUDE.md) / [AGENTS.md](http://AGENTS.md), skills, hooks and MCP servers load as usual. From a phone, tablet or another computer I can approve tool calls, answer questions and interrupt runs for all three agents in one place, browse any folder, preview and edit files, open a terminal, and send files or folders to my devices with Taildrop. When one agent dispatches work to the others, a live chart shows who sent what to whom. Sessions stay in each CLI's native history, so they can be resumed in the terminal later.
>
> Self-hosting / security: both listeners bind [127.0.0.1](http://127.0.0.1) only. Remote access goes through Tailscale Serve, and only logins on an allowlist get in. No vendor relay, no account, no telemetry.
>
> Deployment: git clone [https://github.com/yxhuang/AIReins.git](https://github.com/yxhuang/AIReins.git) && cd AIReins && bash install.sh. Needs Node 22.12+ and whichever of the three CLIs you use, already logged in. Windows + WSL2 and Linux are supported; macOS is experimental (CI only, I don't own a Mac). No Docker image, since it has to drive CLIs and files on the host itself. Docs are in the README. MIT, current release v0.5.0.
>
> AI Involvement: most of the code was written by Claude Code, Codex and Kimi Code, increasingly from inside AIReins itself. I design the features, review the changes, run the test suite and use it daily.

---

> **aaronsuns**（2 分） · 2026-11-09T06:17:02+08:00　
> **Project Name:** Melarka
>
> **Repo/Website Link:** https://github.com/aaronsuns/melarka
>
> **Description:** A self-hosted music server for a household. I built it for my family and it replaced Spotify for us; I use it every day. Songs come from your own music folders (Melarka never rewrites your files or tags; titles, tags and lyrics overrides live in its own SQLite database) or from YouTube via yt-dlp: search, download a song or a whole playlist, or follow channels and let new episodes download by themselves.
>
> - one account per family member: own favorites, playlists, personal radio, nightly "For you" picks
> - streams the original file, or AAC 256k / 128k transcoded on the fly and cached
> - synced lyrics (embedded, .lrc, or online providers); anyone can shift lyrics that run early or late
> - native iPhone and Android apps: background play, gapless, an offline cache of favorites synced on Wi-Fi, and favorites start by themselves when the phone connects to the car over Bluetooth, with the current lyric line on the car display
> - a web app that installs to the home screen; English, 简体中文, 繁體中文, svenska
>
> **Deployment:** One Docker container (`ghcr.io/aaronsuns/melarka`) with a compose example. One-command installer: `curl -fsSL https://raw.githubusercontent.com/aaronsuns/melarka/main/deploy/install.sh | sh` (optionally with your music path at the end). Step-by-step docs in the README and docs/install.md; the iPhone app installs with SideStore (docs/iphone.md), Android gets a signed APK on every release (docs/android.md).
>
> **AI Involvement:** Built with heavy use of AI coding agents (Claude Code). I designed it, review and test every change, and run it daily for my family. The repo has an AGENTS.md, and the design specs are in docs/superpowers/.
>
> Feedback very welcome, especially on the install.

---

> **theanishtar**（1 分） · 2026-11-09T12:36:46+08:00　
> Thanks so much for the kind words and for the report! You were right: on Windows and Linux the window had no way out of the maximized state.
>
> It's fixed in **v1.8.1** (tracked in [https://github.com/2hjaito/davish/issues/93](https://github.com/2hjaito/davish/issues/93)):
>
> * Minimize / Restore / Close buttons at the right end of the menu bar
> * Drag the empty part of the menu bar (the stats and clock) to move the window, including to another monitor
> * Double-click the same area to maximize or restore
> * Resize the window from its edges once it's restored
>
> Davish should offer the update on its own. You can also grab it here: [https://github.com/2hjaito/davish/releases/tag/v1.8.1](https://github.com/2hjaito/davish/releases/tag/v1.8.1)
>
> I don't have a multi-monitor Windows setup to test on, so if anything still feels off, please let me know here or in the issue. Thanks again!

---

> **refaelos**（1 分） · 2026-11-09T13:36:26+08:00　
> Project Name: arcodash
>
> Repo/Website Link: [https://github.com/arcodash/arcodash](https://github.com/arcodash/arcodash)
>
> Description: dashboards with data checks built in. you connect a database, write SQL (or ask in plain English), build dashboards, and freshness / null rate / row count checks run on the same scheduler as the queries and ping Slack, email, Teams, PagerDuty or a webhook when a number looks off. I started it because my dashboards kept being quietly wrong after a load failed, and I'd only find out when someone asked why the number looked weird. 19 connectors, plus a source that joins across your other queries.
>
> Deployment: git clone, cp .env.example .env, docker compose up --build, then localhost:3000. first build compiles the Rust services so go get a coffee. docker compose --profile demo up -d demo-db gives you a sample database to play with. there's a separate prod compose file and a self-hosting guide in docs/. AGPL-3.0, no plan limits when you self-host. v0.1.0 went out Nov 8, so early beta, expect rough edges and tell me what breaks.
>
> AI Involvement: a lot of the code was written with AI coding assistants, I review and test what goes in. the app also has optional AI features (plain English to SQL, explaining why an alert fired) that run on your own Anthropic, OpenAI or Gemini key, and an admin can turn them off.
>
> I build it, so I'm biased. if you'd rather not run Postgres, Valkey and the worker yourself there's a hosted version, 14 days free: [https://www.arcodash.com/?utm\_source=reddit&utm\_medium=post&utm\_campaign=growth-v2&utm\_content=oss-reddit-20261109](https://www.arcodash.com/?utm_source=reddit&utm_medium=post&utm_campaign=growth-v2&utm_content=oss-reddit-20261109)

---

> **LiukDiihMieu**（1 分） · 2026-11-09T16:35:28+08:00　
> **Project Name:** tunhub
>
> **Repo:** [https://github.com/LiukDiihMieu/tunhub](https://github.com/LiukDiihMieu/tunhub)
>
> **Description:**
>
> My Synology NAS was recently hit by the c3rb3r ransomware attack ([related discussion](https://www.reddit.com/r/synology/s/ceh00oizOQ)). After rebuilding it, I decided to stop exposing DSM directly to the internet. I already use SSH tunnels to access private web services on my other workstations, so I wanted to make the same approach more convenient for DSM. That's how **tunhub** came about.
>
> https://i.redd.it/ddxhcotbtj0i1.png
>
> It's a small Python tool that automatically switches between direct LAN access and SSH tunneling, depending on whether the server is reachable locally.
>
> The main feature is a **consistent URL** across both connection methods. Browser bookmarks and password managers work without changes, and when I'm at home, it connects directly over LAN.
>
> It's intended for people who already use SSH, rather than as a replacement for VPNs or authentication.
>
> **Installation:** See the GitHub README.
>
> **AI Involvement:** The project was implemented primarily using Claude. I designed the workflow and requirements, and handled testing and validation.
>
> This is the first public release, so feedback and testing on different platforms would be very welcome!

---

> **meraklhhhs**（1 分） · 2026-11-09T17:04:32+08:00　
> Project: Remaivo
>
> Repo: [https://github.com/StvrvDimitris/remaivo](https://github.com/StvrvDimitris/remaivo)
>
> Remaivo is an MIT-licensed personal finance app you can run yourself. It tracks accounts, spending, scheduled payments and savings goals, with an optional spending plan that shows a daily and weekly allowance while setting money aside for bills.
>
> It supports English and Greek, works on phones, and has separate profiles for up to five people sharing an installation.
>
> Deployment: Docker for self-hosting, or Cloudflare Workers with D1. Setup guides and screenshots are in the README.
>
> AI involvement: I did the analysis, and Claude and Codex implemented the project. AI also helped draft this introduction.
>
> I’d love feedback on the setup experience and the spending-plan approach.

---

> **Dense-Post2766**（1 分） · 2026-11-09T20:49:14+08:00　
> **Project Name:** lanstash
>
> **Repo:** [https://github.com/darki73/lanstash](https://github.com/darki73/lanstash)
>
> **Documentation:** [https://darki73.github.io/lanstash/](https://darki73.github.io/lanstash/)
>
> **Description:**
>
> https://i.redd.it/crgbngbn2l0i1.png
>
> Hi!
>
> I've been running LanCache and plethora of prefill utilities for multiple years at my home.
>
> What i lacked was the "insight" into the what i really have and how much space it takes. On top of that, some downloads were not really up to the "standard" i was giving to my network, for example, Battle.net struggled to do 120 MB/s on a 10G connection through a switch that has a 25G connection to the NAS.
>
> The second issue was the timers that i had to write for the prefill utilities, one thing is prefilling a game as soon as it is released, the other is setting timers to stagger the downloads (still baffles me the need to re-read the game in full just to download 30MB of new data). And while it most certainly fine for some people, it was not fine for me, because i don't have a dedicated box and NAS option seemed like a no-brainer.
>
> Some other things i ran into (and most of them is just my choice of storage):
>
> 1. Tiny files and network storage don't really mix well. LanCache leaves you with a 1MB default (because this is frankly what Steam serves), but if you have Battle.net, then you splitting the 4-16MB chunks into smaller chunks.
> 2. I really wanted to see what i have, how up-to-date it is, and after the fiasco of missing 100G for RDR2 for no reason (i still cannot attribute it to what actually caused it, retention was set to 5 years, and lancache was given 8TB of storage with only 3.2TB taken) i also wanted to know what else went missing (turns out, another 54 games that i had cached lost 78% of their data)
> 3. Of course, as many others, i wanted a nice UI to go along.
>
> It is a 0.1.0, and any feedback is appreciated!
>
> **Deployment:** A release archive for Linux x86\_64 from github or you can compile it yourself.
>
> Before the actual deployment, if you really care, i suggest to clone the repository and have an AI review it for you, because the philosophy of lanstash is completely different from lancache.
>
> **AI Involvement:** The project was developed in collaboration with Claude.

---

> **giulivello**（1 分） · 2026-11-09T23:39:50+08:00　
> https://i.redd.it/jd9nr3x1xl0i1.png
>
> RepoWatch — a self-hosted dashboard that keeps your GitHub traffic history beyond 14 days
>
> Hi everyone, I’m the developer of RepoWatch, a small open-source dashboard for monitoring your own public GitHub projects.  I wanted to keep a history of visits, stars and release downloads instead of checking each repository separately and losing older traffic data.  RepoWatch collects observations into SQLite and provides:
>
>   • Traffic history retained beyond GitHub’s rolling 14-day window.
>
>   • Star balances, release download totals and changes over time.
>
>   • An overview across repositories, with charts, search and sorting.
>
>   • Referring sites and a feed of community activity.
>
>   • Optional PyPI download tracking.
>
> It runs with Docker Compose, collects automatically every six hours, and supports either built-in username/password authentication or an existing authentication proxy. It’s MIT-licensed, with no hosted account or subscription required.
>
> A couple of limitations: it can’t recover traffic that GitHub has already discarded, and counter-based trends need multiple snapshots. Traffic access  requires appropriate permissions on the repositories you monitor.
>
> Repository, screenshots and installation instructions:
>
>   [https://github.com/downlevel/repowatch](https://github.com/downlevel/repowatch)
>
> The first beta is available. I’d particularly appreciate feedback on installation and whether the distinction between cumulative totals and period changes  is clear.
>
> AI disclosure: AI coding tools were used during development, testing and documentation.
> This introduction was also drafted with AI assistance.

---

> **fals3illusion**（1 分） · 2026-11-09T23:41:44+08:00　
> **Project Name:** PeptideTracker
>
> **Repo/Website Link:** [https://github.com/fals3illusion/peptidetracker](https://github.com/fals3illusion/peptidetracker)
>
> **Description:** A self-hosted tracker for peptide and GLP-1 injections. I started tirzepatide and wanted a private place to log my weight and see a projected goal date, without putting health data in someone's cloud. It kept growing as I needed more: doses, reconstitution math, vials, schedules, inventory. Now my friend uses it too.
>
> * **Shots & vials:** log a dose in mg or syringe units. It does the reconstitution math (powder mg + bac water mL → units), tracks what's left in each vial and the cost per shot, and can split a dose across two vials.
> * **Schedules:** weekly GLP-1 with a shot day and an optional step-up dose plan, plus other peptides daily, on set weekdays, every N days, or as needed.
> * **Next shots:** shows what's due, with one-tap logging (with undo), injection-site rotation, and push reminders on shot days (works as a Home Screen app on iPhone and Android).
> * **Inventory:** powder vials, bac water and supplies, with lots, expiry, low-stock warnings, use-by dates for mixed vials, and a reorder planner showing when you'll run out and when to order.
> * **Optional:** weight trend with a projected goal date, weight lost per dose, progress photos, weekly summary email, and a full data export.
> * **Multi-user:** invite people by link (copy/text it) or email; each person's data is private.
> * **Optional extras:** PostgreSQL backup (set up in the app), a Grafana dashboard template, and a "Dashboards" link in the menu.
> * **Updates:** from inside the app, with release notes, an automatic backup first and rollback if something fails.
>
> **Deployment:**
>
> * **Proxmox:** one-line installer in the PVE shell that creates an unprivileged Debian 13 LXC (defaults or custom: ID, cores, RAM, disk, storage, bridge, static IP/VLAN). Type `update` in the container to upgrade.
> * **Docker:** image at [`ghcr.io/fals3illusion/peptidetracker`](http://ghcr.io/fals3illusion/peptidetracker) (amd64 + arm64), with a docker-compose example in the README.
> * **Debian 12/13:** install script.
> * **Docs:** the README covers install, HTTPS/reverse proxy for phone notifications, email setup, backups and updates. Released as v1.0.0, MIT licensed, no telemetry.
>
> **AI Involvement:** Heavy, and I want to be upfront about it. I'm not a professional developer. The code was written with Claude (Anthropic's AI) while I directed what to build, made the design decisions, and tested everything on my own homelab, on a separate offsite Proxmox host, and in daily use for my own shots. It has an automated test suite (100+ tests) that runs on every change, and I'm actively maintaining it. Feedback and bug reports are very welcome.
>
> *Disclaimer: personal logging tool, not medical advice.*
>
> https://i.redd.it/5bqo6vhfxl0i1.png

---

> **crimeacs1**（1 分） · 2026-11-10T00:21:10+08:00　
> **OpenPetCam - I built a self-hosted camera that goes looking for my dog**
>
> I have a golden retriever called Sandy. I wanted to check on her when I’m out, without sending video of my living room through a camera vendor’s service. I also wanted the camera to find her. Opening a pet camera app and seeing an empty patch of floor leaves you with pretty much the same question you started with.
>
> So I built [OpenPetCam](https://github.com/crimeacs/OpenPetCam). It uses a cheap pan/tilt camera flashed with Thingino, plus a small server you control. When Sandy has been out of view for a while, the camera turns and searches the room. Once it finds her, it can follow her. You can also tap **Find** and let it do the looking.
>
> The usual camera features are there too:
>
> * Live video and sound, with push-to-talk.
> * Bark alerts and an activity timeline.
> * Six hours of rolling recording on your server.
> * A privacy button that pauses both the picture and microphone.
>
> The phone interface is a web app you can add to your home screen.
>
> For the hosting side: the camera makes an outbound WireGuard connection to your server. Detection and recording happen there, and live video reaches your phone over WebRTC. There’s no port forwarding on your home router.
>
> The documented setup uses Ubuntu 24.04 on a server with a public IP. The reference VPS costs about $5–7/month; the $5 tier can hit its CPU allowance and slow things down, so I’d budget for a little headroom. The software itself is free, under Apache-2.0.
>
> Installation means flashing a supported camera with Thingino, then running `./setup` from a Mac or Linux computer. That installs the server components and walks you through connecting the camera. The [setup instructions are here](https://github.com/crimeacs/OpenPetCam#readme).
>
> It’s early. I’ve only tested the Cinnado D1 so far, the models are currently tuned for dogs, and it supports one camera per server. Other Thingino pan/tilt cameras may need calibration.
>
> AI disclosure: I use Claude Code in development. The vision and audio models run on your server. There’s also an optional Claude Code agent for investigating and fixing bug reports; that uses an external AI service and isn’t needed for the camera, app or alerts.
>
> [Website and short demo](https://openpetcam.com/) · [Source code](https://github.com/crimeacs/OpenPetCam)
>
> Does anyone here have a different Thingino-compatible pan/tilt camera they’d be up for trying this on? I’d especially like to find out what breaks outside my own setup.
>
> https://i.redd.it/ix0g2f2c4m0i1.png

---

> **Mental-Crab-7716**（2 分） · 2026-11-10T00:46:28+08:00　
> Just updated and the new features work really nice.
> Great Job & tyvm for the quick reply on the enhancements

---

> **Friendly_Cod7425**（1 分） · 2026-11-10T04:11:43+08:00　
> **Project Name:** Gutter
>
> **Repo/Website Link:**
>
> * App (iPad/iPhone): [https://apps.apple.com/us/app/gutter-comic-reader/id6831270255](https://apps.apple.com/us/app/gutter-comic-reader/id6831270255)
> * App source: [https://github.com/rthaines211/gutter](https://github.com/rthaines211/gutter)
> * Server: [https://github.com/rthaines211/gutter-server](https://github.com/rthaines211/gutter-server)
>
> **Description:**
> Gutter is an iPad and iPhone comic reader for comics you host yourself. It connects to **Komga**, **Kavita 0.9+**, or **Gutter Server**, a small Go/SQLite comic server that I also wrote.
>
> * Page or vertical scroll mode, left-to-right or right-to-left, and fit to screen, width or height
> * Progress syncs both ways with your server. The library is kept on the device, so you can still browse it when the server is out of reach.
> * Guided zoom that steps through a page panel by panel. The panels are found on the device, so it works with Komga and Kavita too. Two-page spreads zoom one half at a time.
> * Reading queues, search, filters and sorting
> * Gutter Server also serves an **OPDS** catalog and a **KOReader sync** endpoint, so e-readers can use it too.
>
> Free to read, stream and sync. A one-time Pro unlock ($12.99, not a subscription) adds offline downloads, guided zoom, more than one server and reading stats. There are no accounts, analytics, ads or tracking. The app talks only to the servers you add.
>
> **Deployment:**
>
> * The app is on the App Store now, for iOS and iPadOS. Android is in progress.
> * If you already run Komga or Kavita, nothing else is needed. Add your server in the app.
> * For Gutter Server, there’s a Docker image (`ghcr.io/rthaines211/gutter-server`) and a `compose.yaml`. Point it at your comics folder, set `GUTTER_PASSWORD`, run `docker compose up -d`, then open `http://<host>:8081`. The quick start is in the server README. Your library is mounted read-only.
>
> **AI Involvement:**
> I built this with Claude Code, which wrote most of the code. You can see it in the commit history: commits are co-authored by Claude. I designed the features, reviewed the changes, and tested every release on my own iPad and iPhone against my own library. I’ve used it every day for months.

---

> **Code__Block**（3 分） · 2026-11-10T10:19:17+08:00　
> **Minifold**: a self-hosted file compressor. Drop in photos, PDFs or videos, get smaller files back
>
> Most "compress your PDF / photo" sites want your files on their servers. I wanted the same thing on my own box, so I made Minifold.
>
> You drag files in, pick a level (low / medium / high / extra) and download smaller versions. That's basically it.
>
> Some details:
>
> * Files keep their format. JPEG stays JPEG, MP4 stays MP4. Under the hood it's mozjpeg, oxipng + pngquant, libwebp, gifsicle, libvips (HEIC, AVIF, TIFF), qpdf + Ghostscript for PDFs and FFmpeg for video. Anything else gets compressed with zstd.
> * If it can't make a file smaller, you get the original back instead of a bigger file.
> * Metadata like GPS location and camera info is stripped by default. Color profile and rotation are kept so photos still look right.
> * Nothing leaves the server. Fonts and icons are bundled and the page blocks outside requests.
> * Files clean themselves up: uploads are deleted right after the job, results after a retention time you pick, and leftovers are wiped on restart.
> * Optional GPU video encoding (NVENC, Quick Sync, VA-API). Off by default because the CPU makes smaller files.
> * It's one Rust binary plus the tools above. Images for amd64 and arm64.
>
> Quick start:
>
>     docker run -d --name minifold -p 8080:8080 \
>       -v minifold-config:/config -v minifold-data:/data \
>       --restart unless-stopped ghcr.io/a-mayur/minifold:latest
>
> It generates an access token and an admin token on first start and prints them in `docker logs minifold`. There's an Unraid template in the repo too.
>
> It's early (v0.2.0), so be warned:
>
> * one shared access token, not real user accounts
> * no camera RAW, AVI or JPEG XL yet
> * I've mostly tested it on my own files
>
> If you throw something at it that it handles badly, I'd really like to know. Issues and PRs welcome.
>
> **GitHub**: [https://github.com/a-mayur/minifold](https://github.com/a-mayur/minifold) (MIT)

---

> **CastACard**（1 分） · 2026-11-10T11:47:50+08:00　
> **rbit: a complete Git forge with built-in CI/CD, in one Rust binary. No Postgres, no Redis, no separate CI server.**
>
> **GitHub:** [https://github.com/GitRbit/rbit](https://github.com/GitRbit/rbit) · **Site:** [https://rbit.sh](https://rbit.sh) · MIT / Apache-2.0
>
> Most self-hosted Git setups end up as three or four containers: the forge, Postgres, Redis, and a separate CI server like Woodpecker or Drone. rbit is **one process and one** `data/` **folder**, and back up is a single command.
>
> **Running in under a minute**
>
>     curl -LO https://github.com/GitRbit/rbit/releases/download/v0.2.0/rbit-0.2.0-x86_64-unknown-linux-gnu.tar.gz
>     tar -xzf rbit-0.2.0-*.tar.gz && ./rbit-0.2.0-*/rbit serve
>
> Open [`http://localhost:3000`](http://localhost:3000) and sign up (the first account is admin), then `git push`. There are builds for Linux and macOS on x86\_64 and ARM, so it runs on a Pi too.
>
> **CI/CD built in: rbit Actions**
>
> * GitHub-style workflows in `.rbit/workflows`. Existing `.github/workflows` and `.forgejo/workflows` files are picked up too.
> * Matrices, `needs`, `if:` expressions, reusable workflows, concurrency groups, containers and services
> * Triggers: push, pull request, cron schedule, manual dispatch, `workflow_run`, `repository_dispatch`
> * Caching, artifacts, status badges, environment approvals
> * `rbit-runner install` sets the runner up as a systemd, launchd or Windows service
>
> **Code review that feels like GitHub**
>
> * PRs within a repo or across forks, line comments, resolvable conversations, review requests
> * Merge commit, squash or rebase, plus mergeability checks
> * Branch protection with required reviews and checks, enforced over HTTPS, SSH *and* merges
>
> **Everything else you'd expect**
>
> * Issues with labels, milestones, GitHub-style search and a notification inbox (email optional)
> * **Wikis** with history, diffs and restore
> * Git LFS (with locking), SSH, releases, forks, pull and push mirrors, Mermaid diagrams
> * Orgs, teams, OIDC and GitHub sign-in, passkeys and TOTP 2FA
> * REST API (OpenAPI 3.1), GitHub-shaped webhooks, and a `gh`\-style CLI built into the binary
>
> **Switching is painless**
>
> Import from **GitHub or Gitea/Forgejo**: history, LFS, issues and PRs **keep their original numbers**, along with labels, milestones, comments and releases. Imports don't trigger notifications or webhooks.
>
> **Built for people who run their own servers**
>
> * `rbit backup` and `rbit restore` check every repo with `git fsck`, plus every file's SHA-256, before restoring
> * Prometheus metrics, health checks, and a live admin dashboard
> * Strict CSP, an audit log, scoped expiring tokens, and an SSH server that only speaks Git
> * Server-rendered pages that still work with JavaScript off, are fast on a phone, and install as an app
> * UI in 9 languages, light and dark mode plus \~500 themes

---

> **moonshadowrev**（1 分） · 2026-11-10T13:54:49+08:00　
> # Mirroring any domain to your shared hosting with mere php ( Mirrorgate)
>
> # [https://github.com/moonshadowrev/mirrorgate](https://github.com/moonshadowrev/mirrorgate)
>
> hi everyone
>
> i've had recently an issue , i wanted to do some tests on a project, but for some reason, the server that was carrying that particular software was in Iran , so it was not able to see any servers on Internet, but still there were some providers that would allow this
>
> but this project was for a client so temporarily i've solved this issue with hard way
>
> then i was thinking, what if i get 2 servers, one is my international server and one is only in iran, and i make a reverse proxy without renting a vps inside iran, with just mere shared hosting solution like cpanel or directadmin that is easily available in iran?
>
> so i've came up with this idea, and tried to make it as a opensource software
>
> i thought maybe this is a good solution and someone else needs it
>
> feel free to check it out and let me know your thoughts

---

> **Excellent_Athlete_68**（1 分） · 2026-11-10T15:07:19+08:00　
> I'm Tri, a builder running 20 AI agents. I made Willder to make running many agents easier, for me and for others.
>
> Same as other MCP memory: agents save and recall facts.
>
> Different: built for many agents at once.
>
> • Scoped context, automatically: each agent only sees what its own token allows, enforced by the server, not the prompt.
>
> • Live coordination: what one agent saves, the others read on their next call, and conflicting writes are flagged.
>
> • Works with what you already use: GitHub, Google Drive, Slack and Figma, plus Claude Code and Codex over MCP.
>
> • Built-in agents that show the workflows: Brief me, What contradicts this, Check this.
>
> Self-hosts with no account: [https://github.com/willderai/willder-core](https://github.com/willderai/willder-core) (MIT).
>
> What would you need before running it on your own box?

---

> **CoderLuii**（1 分） · 2026-11-10T16:17:58+08:00　
> **HolyArrs**: one self-hosted app instead of the six arr apps. Shows, movies and music, and it looks like a streaming app
>
> Running a media server usually means Sonarr, Radarr, Lidarr, Bazarr, Prowlarr and Seerr, each with its own setup and database. I wanted one app that does all of it and that the people in my house would actually use, so I built HolyArrs.
>
> You browse it like Netflix, tap what you want, and it sends it to your downloader and files it for Plex, Jellyfin or Emby.
>
> Some details:
>
> * Rows built from your own library: top picks, "because you have…", "popular in your household", Top 10s, New & Popular, Coming soon. Hover a poster and the trailer plays
> * Works with what you already run: qBittorrent, SABnzbd, Plex, Jellyfin, Emby. It connects to them, it doesn't replace them
> * Moving over from Sonarr and Radarr takes a few minutes, and your media files never move
> * It answers like Sonarr and Radarr, so tools that already talk to them keep working
> * HD and 4K of the same title side by side
> * No API keys to set up. Posters and search come from a metadata server I run
> * One Go binary, about 15 MB, no OS inside the image, signed images. amd64, arm64 and armv7
>
> **Repo:** [https://github.com/HolyArrs/HolyArrs](https://github.com/HolyArrs/HolyArrs) **Site and docs:** [https://holyarrs.com](https://holyarrs.com) · [https://docs.holyarrs.com](https://docs.holyarrs.com)
>
> **Deployment:**
>
>     name: HolyArrs
>     services:
>       holyarrs:
>         image: holyarrs/holyarrs:latest
>         container_name: holyarrs
>         environment:
>           - PUID=1000
>           - PGID=1000
>           - TZ=America/New_York
>         volumes:
>           - /your/local/path:/config
>           - /path/to/movies:/movies
>           - /path/to/tv:/tv
>           - /path/to/downloads:/downloads
>         ports:
>           - 6262:6262
>         restart: unless-stopped
>
> Then open `http://your-server:6262`, make the owner account, and a short setup walks you through folders, a downloader and a source.
>
> It's early, so be warned:
>
> * it's a beta, don't make it your main app yet
> * subtitle sites, Trakt lists and some alert channels are held back until they're fully tested
> * it's on its 4th update since launch from bug reports, so expect a few more
>
> **AI Involvement:** Built with Claude Code. I design it and write the specs, Claude Code writes most of the code, a second agent reviews it, and I review and test everything myself. I've been in software and security 10+ years, so anything touching keys, sign-in or the network gets read line by line, and it had a full pentest before release.
>
> If it breaks on your setup, I'd really like to know. Issues and PRs welcome.
>
> https://i.redd.it/5uh57yl6vq0i1.png

---

> **uwulalala**（1 分） · 2026-11-10T16:19:43+08:00　
> Campfire: a Discord-style voice/chat/screen-share app with no server to host (P2P, Rust, MIT/Apache)
>
> I've been working on Campfire, a small app for talking to a group of friends without a central server. I'm posting it here because a lot of people in this sub are looking for Discord alternatives, but I want to be upfront about one difference: **there is nothing to self-host**. Every PC is its own node, and everything runs directly between your friends' machines.
>
> **What it does**
>
> * Voice channels (Opus), global push-to-talk (mouse buttons work too) and an in-game overlay
> * Screen streaming in voice channels with hardware encoding (NVENC / AMF / QSV), game audio on Windows 11, two quality tiers
> * Text chat in spaces and DMs: Markdown, replies, edits, mentions, unread counters
> * File sharing up to 4 GB, direct between members, with previews and resumable downloads
> * Friends via friend code, presence, blocking
> * Password-protected account backup, keys stored locally (DPAPI)
> * Light/dark theme with customizable colors, English and German UI
>
> **How it works**
>
> It's built on [iroh](https://github.com/n0-computer/iroh) (QUIC, hole punching, relay fallback). Voice, video, files and chat all travel directly between devices and are encrypted. If a direct connection isn't possible (strict NAT), traffic goes through a relay but stays end-to-end encrypted. The only thing that touches shared infrastructure is the initial friend request handshake. The wire protocol is documented in the repo.
>
> **Privacy and security**
>
> * No account, no cloud, no telemetry
> * Nothing from other users is downloaded automatically; you choose what may load on its own
> * Updates are only installed after you confirm them
> * Opening executables, archives, Office files and PDFs from others asks first
>
> **Honest limitations**
>
> * Windows only for now (10 or later; game audio capture needs 11)
> * No always-on server, so history sync happens when friends are online
> * It's still early (currently v0.6.x), so expect rough edges, and note that protocol-breaking changes between versions are possible
> * UI is built with iced, so it won't look exactly like Discord
>
> Written in Rust, dual-licensed MIT / Apache-2.0.
>
> GitHub: [https://github.com/TobiasStark/campfire](https://github.com/TobiasStark/campfire)
>
> Feedback, bug reports and PRs are very welcome. There's a [CONTRIBUTING.md](http://CONTRIBUTING.md) in the repo.

---

> **phects**（4 分） · 2026-11-10T16:25:35+08:00　
> **juist**: a peer-to-peer mesh VPN with no coordination server at all
>
> Repo: [https://github.com/nning/juist](https://github.com/nning/juist)
> Docs: [https://juist.nning.io](https://juist.nning.io)
>
> I have been building juist, a mesh VPN where nothing runs in the middle, neither a vendor's server nor your own. WireGuard is used for the p2p tunnels, and NAT traversal comes from Tailscale's open-source (BSD) libraries.
>
> I use it to reach my homelab, because Tailnet Lock or Headscale did not go far enough for me.
>
> Features:
>
> * **Homelab services:** access policies, exit nodes, subnet routes, names, publishing services through an ingress.
> * **No control plane:** devices find each other on the LAN, through each other, or via the public BitTorrent DHT. They punch through NAT and fall back to a relay that one of your own devices runs.
> * **Membership is a signed log:** adding or removing a device takes a k-of-n quorum of admins, whose keys stay on their own devices. Every device checks the log itself.
> * **Fail-closed if you want:** always-on "voucher" devices vouch hourly. A device that has not been vouched for in 48h keeps tunnels only to vouchers.
> * Linux (Debian/Ubuntu/Fedora packages) and FreeBSD, plus an Android app (F-Droid repo).
>
> Install: `curl -fsSL https://juist.nning.io/install | sh`
> Other options: [https://juist.nning.io/en/docs/install/](https://juist.nning.io/en/docs/install/)
>
> **Disclosure:** developed with AI agents (Opus 5.5). I direct the design and test it on my own hardware but I did not write any line of code and no human has audited it yet. The docs explain the architecture, design, development process, and quality assurance. Feedback and breaking it are very welcome, do not run anything critical behind it yet.

---

> **AdPrestigious1382**（0 分） · 2026-11-10T17:28:19+08:00　
> **KavitaInk**: a tiny, offline-first Android client for Kavita, built for E Ink readers
>
> **Project Name:** KavitaInk
>
> **Repo/Website Link:** https://github.com/yunyuyuan/KavitaInk
>
> **Description:** A minimal Android client for [Kavita](https://www.kavitareader.com/) (the self-hosted manga/comic/book server), designed for E Ink readers. You browse your library, download books to local storage, and read them fully offline. There's no sync, no polling and no animations, so every action is a single screen refresh, which matters a lot on E Ink.
>
> - Comics/manga (cbz/zip downloaded as-is; cbr/cb7/rar/7z fetched page by page), EPUB and PDF
> - Downloads keep the server's original files and folder layout under `/sdcard/Books/KavitaInk/`, so KOReader or other reader apps can use them too
> - Resumable downloads with automatic retry, batch download/delete
> - Auto margin cropping, two-page spreads, splitting double-page scans, grayscale contrast boost
> - Volume keys and hardware page-turn buttons
> - About 570 KB APK, zero third-party dependencies, 10 UI languages, Apache-2.0
>
> **Deployment:** It's a client for your existing Kavita v0.9+ server, nothing extra to host. Install the APK from [GitHub Releases](https://github.com/yunyuyuan/KavitaInk/releases/latest) (Android 10+), then enter your server URL with a username/password, or just paste your OPDS link. The README covers setup and permissions.
>
> **AI Involvement:** All of the code was written by AI, and this comment was also drafted with an AI assistant. I designed the features, directed the work, and tested it on an Android 10 emulator against a real Kavita v0.9.1.4 server, including automated end-to-end tests for downloads, pause/resume, offline reading and pagination. It hasn't been tested on many physical E Ink devices yet, so bug reports from Boox/Hisense/Meebook/Bigme owners are very welcome.

---

> **No_Possible_1799**（1 分） · 2026-11-10T18:55:41+08:00　
> https://i.redd.it/2ykom7h7nr0i1.png
>
> # Atrium: a Notion alternative with no limits; and more...
>
> [](https://www.reddit.com/r/selfhosted/?f=flair_name%3A%22Product%20Announcement%22)
>
> Introducing Atrium, a Notion replacement with a bunch of extra features
>
> I wanted a self-hosted Notion replacement for myself. The ones I tried either capped users or put features behind a subscription, so I built my own. It was never meant to be public, but it’s grown enough that I’m sharing it.
>
> **What is Atrium?**
>
> It's a rich team note taking and self-hosted app that combines all of the nice features, so you can minimize the need of other apps for small adjustments, saving you time and effort.
>
> **What’s in it**
>
> * **Notes and pages:** nested pages, databases with board, table, timeline and calendar views, backlinks and a graph view
> * **Calendar and planning:** a Today view, tasks with due dates, reminders
> * **File editors:** open and edit Word, Excel, PowerPoint, PDF (with handwriting and highlights), images and video in the app, without downloading and re-uploading. They aren’t full Office, but they handle quick edits.
> * **Whiteboard:** live, shared with your team
> * **Chat and meetings:** direct, group and team chats; video calls with screen sharing
> * **Unlimited users and workspaces:** it’s your server
> * **Apps:** web, Windows and Android
> * **AI (optional, bring your own key):** ask questions about your workspace, write and rewrite text, fill database columns, turn recordings into text, make flashcards, plus an MCP server for Claude and other AI assistants.
>
> **Install:** Docker Compose, see [https://atrium-five-xi.vercel.app/docs#install](https://atrium-five-xi.vercel.app/docs#install) License: AGPL-3.0.
> GitHub: [https://github.com/TaiDies/atrium](https://github.com/TaiDies/atrium) · Site and full feature list: [https://atrium-five-xi.vercel.app](https://atrium-five-xi.vercel.app/)
>
> **How it was made:** I built it with Claude (AI). I designed it, tested it and fixed the bugs myself, and the code is all open for you to check. This is the first public release, so there will be bugs. Please report them on GitHub Issues.

---

> **TheRealTRexUK**（1 分） · 2026-11-10T19:49:37+08:00　
> # Starboard- a lightweight accessible media server
>
> * **Project Name:** Starboard
> * **Repo/Website Link:** [https://github.com/TheMightyTRex/starboard](https://github.com/TheMightyTRex/starboard)
> * **Description:** A complete media server, set up from one place, light enough for an old laptop or a Raspberry Pi. Starboard installs and runs a whole home media server: the apps that find, download and sort your films, series, music, books and audiobooks, the apps that play them, and the server underneath, from one accessible dashboard. Everything is explained in plain steps in the [**help centre**](https://themightytrex.github.io/starboard/help/index.html), which has a search.
> * **Deployment:**
>
> &#8203;
>
>     curl -fsSL https://raw.githubusercontent.com/TheMightyTRex/starboard/main/run-first.sh | bash
>
> If it says "Command 'curl' not found" (a new Debian does not include curl), use `wget`, which every system here includes. Do not use the `sudo snap install curl` Ubuntu suggests: the snap version cannot save the files the script needs.
>
>     wget -qO- https://raw.githubusercontent.com/TheMightyTRex/starboard/main/run-first.sh | bash
>
> * **AI Involvement:** Developed with AI tested by humans. I have written the project plan and user Journys - A mixture of user testing (its running on my live server) and ai testing.
>
> Hi, one of my friends recently started losing their eyesight and I have been helping with some tools to assist them with tech tasks. We have been looking at a media server setup - and nothing is really accessible and there are not many that have radio specific functionality.
>
> I have been creating an install and dashboard for a small media server. It idles at about 1Gb fully loaded. I have been running a version of it for a while for my own use but have started polishing it making it as logical to install as possible.
>
> I am looking for people to test and give me some feedback. particularly if you use assistive technology. There is a system built in to submit feedback easily - (you need a github account to post the issue)
>
> If you can get a terminal prompt and type the first install script it should take you through everything step by step. Both via the terminal - or opens a web browser if you have a gui.
>
> I have tested it on linux mint (which is what I run at home) and debian (on a VM).
>
> [https://github.com/TheMightyTRex/starboard](https://github.com/TheMightyTRex/starboard)
>
> I have used AI to do the actual coding but it's been tested by hand and humans. Its running on my own live server.
>
> https://i.redd.it/2zrtgyqxwr0i1.png

---

> **Broad_Long_2556**（4 分） · 2026-11-10T20:31:27+08:00　
> **Project Name:** Fision
>
> **Repo/Website Link:**
>
> * [Server](https://github.com/jotapemj/Fision-Server)
> * [Web client](https://github.com/jotapemj/Fision-AppWeb)
> * [Android app](https://github.com/jotapemj/Fision-AppAndroid). Demo song available for download
>
> **Description:** A self-hosted tool for practicing music. You upload a song and it gives you:
>
> * Separate tracks (vocals, drums, bass, guitar, piano...) with FX controls
> * Chords synced to the beat with piano/guitar/ukelele diagrams
> * Dynamic metronome, playback speed and pitch with chord transposition controls.
> * Synced lyrics, karaoke mode and chords on lyrics.
>
> Useful if you want to play along without the guitar, sing without the vocals, or follow the chords while a song plays, all without sending your music to a paid online service. Supports multiple user accounts, playlists shared between devices, and an admin panel. Use it from the browser or the Android app. New accounts always include a demo song.
>
> **Deployment:** Docker images on GHCR: cu129 (RTX 20xx and newer), cu126 (GTX 10xx), cpu (no GPU, but very slow). The repo includes a compose.yaml and .env.example.
>
> The README covers installation step by step, plus a native install without Docker. A \`doctor\` command checks the setup. The web client comes with the server at \`/app/\` (needs HTTPS or localhost; \`tailscale serve\` works).
>
> **AI Involvement:** At the very begining of this project, around 2023, I started it by myself on python, Qt and Android, however Claude helped me a lot with the server backend part and security. Design decisions, testing and validation were done by me on my own hardware.
>
> Hi all!
>
> I'm very very excited to announce, after months of work, a project that I had been dreaming of for years. After testing a lot and polishing everything, I can finally share this project with the community. It is a free and open source project and would be a dream to see that this project is useful for people, musicians and music lovers. Currently it is the I'm using and I don't need any other subscription-paid apps for this purpose.
>
> https://i.redd.it/oideg9eli11i1.png
>
> [Have a look to the promo video!](https://github.com/user-attachments/assets/fb8d2289-e46d-4a26-9af3-b5bbab4d9315)
>
> I put a lot of love into this project, so feedback and comments will be welcomed.
>
> Thanks everyone.

---

> **tructt**（1 分） · 2026-11-10T21:49:00+08:00　
> https://i.redd.it/jp7shwgxhs0i1.jpeg
>
> I use Linux and want a desktop hypervisor solution strong enough for labs that existing tools (Cockpit/Virt-manager) are not capable or not flexible enough to fulfill my needs. So I created vEMU
>
> Repo: [https://github.com/withcoresystem/v-EMU](https://github.com/withcoresystem/v-EMU)
>
> Not another web app but native desktop tool for all major Linux OS families as physical host
>
> \- RHEL v10.x + variants
>
> \- OpenSuSE v16.x + variants
>
> \- Debian v13 + variants
>
> AI status: I use agent for code generation and automated unit tests. I involved in the rest with architectural planning, UI/UX design, physical machine validation, real life stress test with manual workflows

---

> **Mountain_Fudge3980**（1 分） · 2026-11-10T23:50:55+08:00　
> **Project Name:** CutVoke
>
> **Repo/Website Link:** https://github.com/frankShan001/CutVoke
>
> **Description:** A local-first video editor (multitrack timeline, captions, titles, keyframes, transitions, MP4 export). `cutvoke serve` runs the web editor on loopback, and the same project is scriptable over an HTTP API, a CLI and an MCP server, so an AI agent of your choice can make a first cut and you refine it by hand on the same timeline. Media never leaves your machine, and there's no account or telemetry. Instagram's Edits added an MCP last week, but it's Mac-only and needs an Instagram account; this runs on Windows, macOS and Linux.
>
> **Deployment:** Prebuilt archives for Windows x64 (portable), macOS arm64/x64 and Linux x64 (v0.3.5 prerelease, unsigned), or from source (Python 3.10+, Node 20+, FFmpeg). No Docker image yet. Install docs: https://github.com/frankShan001/CutVoke/blob/main/docs/user/installation.md
>
> **AI Involvement:** A lot of the code was written with AI coding agents (OpenAI Codex; you can see the `codex/` branches in the history). The app itself ships no AI model; agent editing is optional and uses whatever MCP client you already run.
>
> I'm the author. It's early, so bug reports and "I'd use it if it did X" are very welcome.

---

> **HistorianMundane3176**（2 分） · 2026-11-10T23:51:25+08:00　
> Project name: Cadence — native music clients for your own Aurral server. I'm the creator.
>
> Repo: [https://github.com/bahachammakhi/cadence-music](https://github.com/bahachammakhi/cadence-music)
>
> Website and Mac download: [https://cadence.bmerce.net/](https://cadence.bmerce.net/)
>
> Description: Cadence is an MIT-licensed SwiftUI client for Mac, iPhone and Apple Watch. It connects to your own HTTPS Aurral server/account for library browsing, playback, queues, favorites, downloads, Discover and playlist imports. The Watch companion has playlist preparation and verified file transfers for its offline design. There is no hosted Cadence account or subscription.
>
> Deployment: The signed and Apple-notarized Mac 0.7.2 download supports macOS 14+, Apple Silicon and Intel. Explore demo works without a server using three original clips. iPhone (iOS 18+) and Watch (watchOS 10+) are available as source builds or through an existing private beta invitation; there is no public TestFlight link. These are native clients, not another Docker service; you bring the Aurral backend. Build/setup instructions are in the repo. Latest source is 0.7.5.
>
> Limits: Other Subsonic servers are only partially supported and unverified. Discover/import/preparation need Aurral's native API. Spotify imports metadata through Aurral, not Spotify audio. Physical Watch Bluetooth/background/phone-off running acceptance remains pending.
>
> AI involvement: AI assistance has been used for development, documentation and the landing page. Tests and known verification gaps are documented publicly.
>
> I'd appreciate feedback from Aurral users on setup and everyday library playback, or contributions to server compatibility and the native apps.

---

> **ponzi_gg**（1 分） · 2026-11-11T00:02:54+08:00　
> Aurral dev here, how the hell are you not in our discord yet??? Come share your project, we have testers!

---

> **finesseserver**（5 分） · 2026-11-11T01:37:30+08:00　
> **Project Name:** Finesse
>
> **Repo/Website Link:** https://github.com/CoffeeCC/finesse (Discord for help and feedback: https://discord.gg/G4RfBMytJg)
>
> **Description:**
> Finesse is a free, MIT-licensed app that sets up a whole home media server in one go: Jellyfin, Sonarr, Radarr, Lidarr and Prowlarr, already wired together, plus its own request page. The idea is search, add, watch. Someone at home searches for a show, adds it, and it shows up ready to play, without you having to be the household IT department.
>
> I built it because every time I set up Jellyfin and the arr stack for family, the setup itself was the hard part: getting paths, API keys and download clients to agree with each other. Finesse does that part and keeps the stack updated afterwards. If you already run Jellyfin or the arrs, there's an adopt mode so you don't have to start over.
>
> It's a front end and installer, not a content source. It ships with no content and no indexers. Current release is v3.2.8, with a native Windows installer (no Docker Desktop) and one command on Linux.
>
> **Deployment:**
>
> - Windows: a normal installer, no Docker Desktop or WSL needed: https://github.com/CoffeeCC/finesse/releases/latest/download/FinesseSetup.exe
> - Linux (x86-64 or ARM64): `curl -fsSL https://raw.githubusercontent.com/CoffeeCC/finesse/master/install.sh | bash`
> - Docs are in /docs in the repo.
>
> **AI Involvement:** Yes, so here it is plainly. I used AI coding assistants heavily for writing and refactoring code, debugging and drafting docs. I review, test and run everything myself and fix the bugs when they turn up. The mascot (Nessa), her voice and art, and the music in the promo videos are AI-generated. No AI runs inside Finesse, and none of your data goes to an AI service.
>
> Feedback I'd really like: anything that broke on your hardware, and anywhere setup confused you.

---

> **Exploit7221**（0 分） · 2026-11-11T01:44:21+08:00　
> Notki - another selfhosted note app
>
> \*\*Project Name:\*\* Notki
> \*\*Repo/Website Link:\*\* https://github.com/shirou93/Notki
>
> \*\*Description:\*\*
> Notki is a self-hosted note-taking and personal task management application designed for people who want full control over their data.
> It combines note-taking, task management and collaboration in a single lightweight application. Instead of relying on external cloud services, all data is stored on your own server.
> Key features include:
>
> \*\*Rich-text editor\*\* – create and organize notes with formatting, checklists and drag-and-drop tasks.
>
> \*\*Task management\*\* – set due dates, track daily tasks and export events using iCalendar.
>
> \*\*Organization\*\* – use labels, search, sorting, pinning and archiving to keep everything organized.
>
> \*\*Collaboration\*\* – share notes with other users and control their read/write permissions.
>
> \*\*Offline support\*\* – access your notes without an internet connection and automatically synchronize changes when you’re back online.
>
> \*\*Multi-user support\*\* – manage users and permissions through the administration panel.
>
> \*\*Secure authentication\*\* – TOTP-based 2FA, WebAuthn passkeys, hardware security keys and recovery codes.
>
> \*\*Encrypted backups\*\* – protect your data with AES-256-GCM encrypted backups.
>
> \*\*Customization\*\* – light, dark and system themes, with support for multiple languages.
> Notki uses SQLite as its database, keeping the infrastructure simple without requiring a separate database server.
>
> \*\*Deployment:\*\*
> Notki can be deployed using Docker Compose. The repository includes a Dockerfile, Compose configuration and an installation/update script.
>
> Quick start:
> mkdir notki && cd notki
> curl -sO https://raw.githubusercontent.com/shirou93/Notki/main/update.sh
> bash update.sh
>
> Full installation and configuration instructions are available in the repository README.
>
> \*\*AI Involvement:\*\*
> Google Jules was used as an AI coding agent during development. It assisted with implementing features, writing code, debugging and improving the application. All changes were reviewed and tested as part of the development process.
>
> https://i.redd.it/5v7uyh98ot0i1.jpeg

---

> **8bit-necro**（1 分） · 2026-11-11T02:14:49+08:00　
> Project name: Pokegarden - a place for your Pokemon to stay in between battles
>
> Repo: [https://github.com/8bit-necro/pokegarden](https://github.com/8bit-necro/pokegarden)
>
> I recently got into restoring my old game boys and started replaying my old Pokemon games. I don't want them to just exist on my save files when I am done with the game, so I started Pokegarden. It is a bit like a poor mans Tamagotchi in which you can feed your Pokemon, let them train, chill and play. There is also a save game editor included. I started the project without AI, but ended up using it way too much.
>
> It also has just one commit, because I moved it over from my own code hosting and some commits are embarrassing.

---

> **gptrv**（1 分） · 2026-11-11T02:42:35+08:00　
> **Project Name:** Brigade
>
> **Repo/Website Link:** https://github.com/gmpetrov/brigade (MIT) · live demo without signup: https://demo.brigade.lol
>
> **Description:** A workspace where AI agents work as teammates with one job each (support, marketing, sales, code). Each teammate runs the official Claude Code or Codex CLI, signed in with your own Claude or ChatGPT plan, with its own apps (Gmail, GitHub, Stripe, Notion, Linear, any MCP server…), a shared memory and a vault for logins. You choose per teammate what waits for your approval (sending an email, a change in Stripe, shipping code); those requests land in one list you can answer from your phone. Threads, triggers, schedules and live previews of the app being built are included.
>
> **Deployment:** The whole stack self-hosts from the repo: Docker Compose in `deploy/vps` (API, dashboard, PostgreSQL), or Cloudflare Workers. The runner that executes the agents installs on Linux or macOS with one command and links your machine to the workspace. Docs in the repo's `docs/` and the README quickstart. Note: the AI itself still runs at the provider (Anthropic or OpenAI) on your own subscription; Brigade never bills AI usage.
>
> **AI Involvement:** Heavy, and on purpose. Brigade is built with Brigade: 784 of the 786 pull requests merged since Oct 10 were opened by its own agents (the `brigade/…` branches), and I make the calls on what goes in. This comment was drafted by one of its teammates too.

---

> **HistorianMundane3176**（1 分） · 2026-11-11T03:16:36+08:00　
> Just joined ! Thanks for the reply and for the good product

---

> **SlimDogs**（2 分） · 2026-11-11T03:52:13+08:00　
> https://i.redd.it/774cpx21bu0i1.png
>
> Hello everyone!
>
> A little update on **Thingport** – an open-source, self-hosted platform designed to make life easier and better for 3D printing enthusiasts.
>
> I'll start with a click trough demo video:
>
> [https://www.youtube.com/watch?v=8g-JoWckL2Y](https://www.youtube.com/watch?v=8g-JoWckL2Y)
>
> What started as a handy personal library that could easily import and sync models from MakerWorld, Printables and Thingiverse is evolving into something much bigger. Thingport is getting a new, clearer identity - it's a tool which puts AI at work to achieve cool functionalities.
>
> Here are some of the cool things you can experience since the latest **v1.0.0 release**:
>
> * **Import from 20+ 3D model platforms** – easily bring your models into one place, with synchronisation support.
> * **Put AI to work for you** – use your own self-hosted AI or a cloud-based provider to improve model descriptions, organise and categorise your library, or even... create 3D-printable models!
> * **Join the Fediverse (sort of!)** – connect your Thingport instance with other Thingport instances. And yes, this even works when your instance isn't publicly exposed to the internet!
> * **Built-in tools and extensibility** – enjoy a growing collection of useful tools, or build and integrate your own.
> * **Print quality** \- know about print issues before even slicing it
> * **And many more cool new features**
>
> And the best part?
>
> **Thingport is open source, free to use, self-hosted, and comes with a promise to stay that way.**
>
> If you are into 3D printing and self-hosting (which is kinda obvious) - this piece of software is meant for you. Have a look. :)
>
> GH: [https://github.com/TautvydasDerzinskas/Thingport](https://github.com/TautvydasDerzinskas/Thingport)
> Homepage: [https://www.thingport.net](https://www.thingport.net)

---

> **TheDude906231**（1 分） · 2026-11-11T03:53:03+08:00　
> Project Name: Lucarne
>
> Repo/Website Link: [https://github.com/el-dud3rino/Lucarne](https://github.com/el-dud3rino/Lucarne)
>
> Description:
>
> A self-hosted family hub for a wall-mounted touchscreen, and a free alternative to Skylight. After the free first month, Skylight Plus costs $79/year to unlock meal planning, rewards and the photo frame, and your family's schedule lives in their cloud. Lucarne includes all of that for free and stores everything on your own device.
>
> \- Calendar: two-way Google Calendar sync for several accounts, .ics links (school, TeamSnap, iCloud, Outlook), birthdays and holidays, countdowns, and "leave in 12 min" alerts with drive times
>
> \- Chores, routines, habits and rewards: kids earn stars and spend them on rewards. Kid Mode uses pictures only, for kids who can't read yet.
>
> \- Lists: groceries sorted by store aisle, quantities merged, and one-tap "usual items"
>
> \- Meals: a weekly planner, a recipe box, recipe import from a URL without the ads, a full-screen Cook Mode with timers, and a week's ingredients sent to the grocery list
>
> \- Photo screensaver (Google Photos or your own uploads, stored locally) and a drawing pad for little kids
>
> \- Designed for a 1080p wall touchscreen. Phones on your Wi-Fi get a mobile layout of the same app.
>
> \- Keeps working offline, with automatic daily backups and one-tap restore
>
> \- One Node process and one SQLite file. No external database, no account, no telemetry. MIT licensed.
>
> Deployment:
>
> Released as v0.1.1. Docker images are available for amd64 and arm64 (Raspberry Pi):
>
> mkdir lucarne && cd lucarne
>
> curl -fsSL -O [https://raw.githubusercontent.com/el-dud3rino/Lucarne/main/docker-compose.yml](https://raw.githubusercontent.com/el-dud3rino/Lucarne/main/docker-compose.yml)
>
> curl -fsSL -o .env [https://raw.githubusercontent.com/el-dud3rino/Lucarne/main/.env.example](https://raw.githubusercontent.com/el-dud3rino/Lucarne/main/.env.example)
>
> nano .env            # set TZ, e.g. TZ=America/Chicago
>
> docker compose up -d # then open [http://localhost:3001](http://localhost:3001)
>
> Image: ghcr.io/el-dud3rino/lucarne. You can also skip Docker: there's a prebuilt download for Node and systemd, plus a full step-by-step Raspberry Pi kiosk guide. The README covers the Docker setup, the Pi guide, the Google setup (you use your own free Google Cloud project), backups and troubleshooting, with screenshots of every screen.
>
> AI Involvement:
>
> I'm not a developer. I designed Lucarne, described what each screen should do, and tested it. Most of the code was written by Claude Opus 5.5 in Claude Code. It has a test suite (unit, integration and browser tests), and the Docker image is built and checked automatically on every change. The optional AI features (importing events from a photo, meal search) use your own Gemini key and are off without one.
>
> So far it has only been tested on Windows. I'm in the middle of moving, so I haven't set up the real wall-mounted Pi yet. I'm looking for testers, especially anyone with a Pi or a spare touchscreen. Bug reports, feature requests and "it worked" are all welcome in GitHub Issues or Discussions.

---

> **Ill_Yogurtcloset803**（1 分） · 2026-11-11T06:21:45+08:00　
> **Project Name:** nosnitch
>
> **Repo/Website Link:** [https://github.com/Umerrrdo/nosnitch](https://github.com/Umerrrdo/nosnitch) (npm: [https://www.npmjs.com/package/nosnitch](https://www.npmjs.com/package/nosnitch))
>
> **Description:** A while ago someone here found Immich’s ML container sending telemetry to Microsoft by default. That made me wonder how many other apps do the same, and every app uses a different setting to opt out (N8N\_DIAGNOSTICS\_ENABLED, TELEMETRY\_ENABLED, DO\_NOT\_TRACK and so on). nosnitch reads your docker-compose file and tells you which services send telemetry by default, where it goes, and the exact env var to turn it off. `--fix` writes a separate override file and never touches your original. It can also output a Pi-hole/AdGuard blocklist. 45 apps so far, and every entry links to the official docs or source code it’s based on, so nothing is guessed. The tool itself makes no network calls and has no telemetry.
>
> **Deployment:** Needs Node 20+. Run `npx nosnitch scan docker-compose.yml`. There’s also a Dockerfile, and it runs fine with `--network none`. The README covers usage, and CONTRIBUTING explains how to add an app.
>
> **AI Involvement:** Built with heavy help from Claude Code, which wrote most of the code. I designed it, reviewed it, and tested it against 32 official compose files from projects like Immich, Supabase, Sentry, and n8n. The database entries had to cite official sources, and anything that couldn’t be confirmed was left out or marked unverified.
>
> The database is the part that grows. If you know how an app behaves, an issue or a small PR adds it. Feedback welcome.

---

> **ScubyDam**（2 分） · 2026-11-11T06:27:04+08:00　
> Project Name: Homebox AI Inventory
>
> Repo Link: https://github.com/scubadam/homebox-ai-inventory
>
> Description:
> A lightweight, mobile-first companion PWA for Homebox that uses multimodal AI vision to scan, crop, and catalog physical storage boxes, totes, and tools from your smartphone camera.
>
> Key Features:
> * Mobile PWA: Install directly to your phone's home screen; walk around snapping single or multi-shot bin photos.
> * On-Device Canvas Cropping: Browser canvas auto-detects item bounding boxes and crops individual, high-res cover photos for each item before uploading to Homebox.
> * Lightweight & Pure Go: Static binary on Google distroless (~15MB image, ~1MB RAM, <10ms startup). 100% stateless (no extra database or persistent volume needed).
> * Local Privacy or Cloud: Works out-of-the-box with local Ollama VLMs (llama3.2-vision, llava-phi3) for 100% offline homelabs, or cloud models (Gemini Flash / OpenAI).
> * GNU AGPLv3 Licensed: Aligned with upstream Homebox.
>
> Deployment:
> Available as a multi-arch container (ghcr.io/scubadam/homebox-ai-inventory:latest) with Docker Compose examples and an official OCI Helm chart in the repo.
>
> AI Involvement:
> Uses multimodal vision models (local Ollama or cloud Gemini/OpenAI) to detect items, count quantities, recommend names/categories, and identify bounding boxes for canvas cropping. AI assisted development of this project.

---

> **dr_ecs**（0 分） · 2026-11-11T09:44:58+08:00　
> Claude built my wife a Spotify alternative: Magpie Player: Before you all berate me for generating a vibe-coded app, hear me out. I’ve been using navidrome with Lidarr very happily but have been stuck with migrating my wife to it even though she’s embraced Jellyfin. Understandably since Spotify provides such a smooth service with utter neglect for the artists.
>
> So I created a stack for myself that has been working on the computer: Aurral, Lidarr, slskd and Navidrome all connected and working well across two libraries (Aurral Playlists and Music). But I had no good option on my phone and hers (iPhone) to be able to play these beyond more than just what was in the library, which my wife called trash but arguably her music was trash so we were stuck.
>
> I worked with Claude doing all of the work to create Magpie Player that connects to all of these services and is able to create what I feel like is a reasonably smooth experience. It lets you create and listen to Aurral playlists and flows, updates new songs based on Deezer playlists or your own Flows, also getting all of your navidrome playlists and music too. There is nothing unique or creative about the music player so won’t talk much about that. Most importantly, it works in CarPlay and AirPlay.
>
> But what is unique is the music request system. I created a new library in Lidarr and Navidrome called “finds” which you can set in Magpie. When you search for a song that isn’t in your library, you can rapidly request it. If you have Tubifarry plugin within Lidarr, it will probe slskd to quickly find an mp3 quality version of the song and put it in Finds. When automatically downloaded, it puts it as next to be played. Magpie keeps it in Finds for 7 days for you to enjoy and listen to it, where you can either discard it or add the artist to Lidarr where it becomes monitored and it downloads the discography in the background. You can also listen to 30 second demos of any song you find.
>
> Obviously it’s a massive work in progress and my ambition is to have this as an always free iOS tool. If anyone is interested in joining the Test Flight prototypes or if you’re interested in helping test and build it, please let me know. Very much open to letting other’s Claude put in some work too since I have been churning through a lot of tokens for this. The GitHub repo is:
> https://github.com/bleak-rooster/Magpie-Player
>
> https://i.redd.it/bixu5d3z1w0i1.jpeg

---

> **eric-leung-001**（1 分） · 2026-11-11T10:06:28+08:00　
> Project Name: Filehub
>
> Repo/Website Link: https://github.com/ericleung001/nas-filehub
>
> Description:
> Filehub is a lightweight, self-hosted file manager for sharing folders among users on your own server. Each user gets a private home folder. Admins can share folders with per-user read or write access and an optional delete permission, and can create link shares with an optional password or expiry. It includes search, a recycle bin, folder zip download, image/PDF/video preview, optional hardware-accelerated thumbnails, 2FA, storage quotas, and an audit log.
>
> It is a Go single binary with an embedded web UI and SQLite, licensed Apache-2.0. The current release is v0.4.4. It is listed in TrueNAS Community Apps: https://apps.truenas.com/catalog/filehub_community/
>
> Deployment:
> - Docker / Docker Compose: ericleung001/nas-filehub:0.4.4 or ghcr.io/ericleung001/nas-filehub:0.4.4 (linux/amd64 and linux/arm64)
> - Release binaries for Linux, macOS, and Windows: https://github.com/ericleung001/nas-filehub/releases/tag/v0.4.4
> - TrueNAS: Apps → search Filehub (Community train)
> - Install and reverse-proxy notes are in the README
>
> AI Involvement:
> Minimal AI assistance; I review and decide what ships.

---

> **Beginning-Cat-1991**（1 分） · 2026-11-11T11:13:01+08:00　
> Bowerbird is a research notebook in the NotebookLM mold. Add PDFs, books, web pages, YouTube videos and recordings, ask questions, and the answer cites the passages it used. Each quoted phrase is looked up in the source it cites, so you can see which quotes actually check out.
>
> 0.1.5 shipped a Docker image, so here it is for this sub.
>
> **What runs on your box**
> - Notebooks are plain folders: your sources, Markdown notes, conversations as JSONL. The SQLite index rebuilds itself if you delete it.
> - Search (BM25 plus EmbeddingGemma vectors), OCR, Whisper transcription and Kokoro voices run locally. CPU is fine.
> - No analytics, no update checks. The README has a table of everything that leaves the machine and when.
>
> **Models**
> Any provider with your own key (OpenAI, Anthropic, Gemini, DeepSeek, Mistral, Groq, OpenRouter and more), or your own server: Ollama, LM Studio, llama.cpp, anything with an OpenAI-compatible API. With a local model, nothing leaves your network.
>
> **Compose**
>
> ```yaml
> services:
>   bowerbird:
>     image: ghcr.io/jolovicdev/bowerbird
>     restart: unless-stopped
>     ports:
>       - "127.0.0.1:7477:7477"
>     environment:
>       BOWERBIRD_TOKEN: "change me: 16 or more characters"
>     volumes:
>       - bowerbird:/data
>     extra_hosts:
>       - "host.docker.internal:host-gateway"
> volumes:
>   bowerbird:
> ```
>
> Open http://localhost:7477 and sign in with BOWERBIRD_TOKEN. `/data` holds notebooks, settings (your API keys) and models; the search model is about 200 MB, downloaded with your first source. For Ollama on the same host, set the server address to `http://host.docker.internal:11434`.
>
> **Auth, honestly**
> Single user. The token is the password (16+ characters), and signing in gives a 30-day HttpOnly cookie. No accounts. Put Caddy or Traefik in front for HTTPS, or keep it on Tailscale; the README has a Caddy example.
>
> **Also:** desktop apps for Linux, macOS and Windows, and an Android app that can use the Ollama on your home server.
>
> **Limits:** one user, OCR reads Latin script only, no iOS app.
>
> MIT licensed, Rust (axum) and SvelteKit.
> Repo: https://github.com/jolovicdev/bowerbird
>
> AI disclosure: built with Claude Code as a coding assistant; the commits say so.

---

> **Aadgjmptw3**（1 分） · 2026-11-11T13:02:37+08:00　
> Project Name: Superstation IPTV
>
> Repo/Website Link: [https://github.com/austin-72/superstation-iptv](https://github.com/austin-72/superstation-iptv) · [https://austin-72.github.io/superstation-iptv/](https://austin-72.github.io/superstation-iptv/)
>
> Description: A self-hosted IPTV player, TV guide and DVR for a household. You add your M3U playlists or Xtream Codes accounts once on a small server at home, and everyone watches in a web browser on a computer, phone, tablet or smart TV, each with their own profile. Live TV with a full guide, catch-up and recordings; films and series merged from several providers into one catalogue; kids profiles, screen time and parental locks. Streams go straight from the provider to the device when it can play them, and the server only converts what it can't. It also gives other apps an Xtream login or an HDHomeRun tuner. It is a player only: no channels or accounts come with it.
>
> Deployment: One Docker container (ghcr.io/austin-72/superstation-iptv, amd64 and arm64), or Node.js 20+ and ffmpeg. No database and no npm dependencies. MIT licence.
>
> AI Involvement: Heavy. Most of the code was written by an AI assistant (Claude) working to my direction, and I test it on my own household's devices. About 250 automated tests run on every push.

---

> **SnooGiraffes2912**（1 分） · 2026-11-11T13:32:25+08:00　
> **Project Name:** Magican
>
> **Repo/Website Link:** https://github.com/MagicBeansAI/MagicianAI (Apache-2.0)
>
> **Description:** A self-hosted runtime for a personal AI assistant that keeps your notes, memory and apps on your own machine. Demo (88 s) of one thing it can do: https://youtu.be/ABtY4hXgQ8Y
>
> - I described an audiobook app in one paragraph; its coding agent wrote and tested it, and it only installs after I approve exactly what it asks for (here: one Notes folder, read/search/add).
> - In the app I paste a Project Gutenberg link. A creative agent casts every character, records each line in its own voice, adds sound effects and music, and paints scene pictures.
> - It asks before writing anything into my notes. The audiobook ends up as a normal note with its audio and pictures beside it.
> - Voices come from a TTS server running locally, including my own cloned voice for one character.
>
> **Deployment:** Build from source with `make install` (macOS is the validated platform today; the installer asks where your data lives). Docs: the README Quick start and `docs/quickstart.md`. It's pre-1.0, so expect changes.
>
> **AI Involvement:** Parts built with AI coding agents, including Magican's own. In this demo the agents used a cloud LLM; models are configurable. This comment was drafted with AI help.

---

> **OkFaithlessness3182**（1 分） · 2026-11-11T18:25:27+08:00　
> Project name: HJM Local Cloud
> Repo: [https://github.com/jjcasmar/hjm-cloud](https://github.com/jjcasmar/hjm-cloud)
> Description:
> A local stand-in for the Helki cloud that **HJM Wi-Fi radiators** connect to, bridged to MQTT with Home Assistant discovery. With it running, the radiators work without internet access and without the HJM / Smartbox app.
>
> * Speaks the radiators' own cloud protocol, so **the original firmware stays untouched**: nothing to open or flash
> * Each radiator appears in Home Assistant as a `climate` entity (off / heat / auto, target temperature, room temperature, heating or idle), plus power, energy, duty, temperature, window-open and diagnostic sensors
> * **Power and energy are estimates.** The radiator doesn't meter its consumption, so power is calculated as reported element power × duty cycle, and energy (kWh, `total_increasing`, works in the Energy dashboard) is that power integrated over time by the bridge. The total is saved in `data/config.json`. Nothing is counted while a radiator is disconnected.
> * A web UI to approve and name radiators, set up the MQTT broker, generate router rules and control radiators directly
> * Runs as a single Docker container
>
> Deployment: Contains docker-compose.yml. Needs custom DNS
>
> AI Involvement: Completely vibecoded. Test manually on two radiators
>
> Sharing in the hope its useful for someone. If its useful for people, I may maintain it.

---

> **victoor89**（1 分） · 2026-11-11T20:35:05+08:00　
> **Project Name:** Plain Week
>
> **Repo/Website Link:** [https://github.com/victor-falcon/plain-week](https://github.com/victor-falcon/plain-week) · MIT · try it without an account at [plainweek.eu](https://plainweek.eu)
>
> **Description:** A weekly planner: the seven days of the week on one screen, and you type tasks straight into them. I wanted something between a paper weekly planner and a to-do app, without projects, labels or boards to set up first.
>
> It's local-first: tasks live in your browser (IndexedDB), it works offline and installs as a PWA. An account is optional and only there to sync between devices. On your own instance that's free; there is a paid sync plan on plainweek.eu, but nothing is locked behind it in the self-hosted version.
>
> What it does today:
>
> - Fast entry: click a row, type, Enter. "17:30 Gym" sets the time, "31 Dec Gym" sets the date
> - Recurring tasks (every N days, weekdays, monthly), colors, notes and subtasks
> - Drag and drop between days, to a "Someday" list or to another week (mouse, touch and keyboard)
> - Optional: dated tasks copied to a Google Calendar, browser push notifications (a morning summary and a reminder before timed tasks)
> - JSON export/import, dark mode, RTL layouts
>
> **Deployment:** One container (FrankenPHP + SQLite on a volume), no other services, about 256 MB of RAM. Images for amd64 and arm64 on GHCR:
>
>     docker run -d -p 127.0.0.1:8080:8080 -v plainweek-storage:/app/storage \
>       -e APP_URL=http://localhost:8080 -e APP_KEY="base64:$(openssl rand -base64 32)" \
>       ghcr.io/victor-falcon/plain-week:latest
>
> There's also a Coolify template. Docs with all the environment variables (mail, Google Calendar, push): [docs/self-hosting.md](https://github.com/victor-falcon/plain-week/blob/main/docs/self-hosting.md). Note that offline mode needs HTTPS (or localhost) because it uses a service worker.
>
> **AI Involvement:** A lot, to be transparent. I'm the developer and I decide the design and review the changes, but most of the code is written with Claude Code (an AI coding agent). It's a Laravel + React app with tests and CI on every change.
>
> The project is about a month old. Feedback is very welcome, especially on self-hosting.

---

> **danielrothmann**（1 分） · 2026-11-11T21:28:45+08:00　
> **Project Name**
> Eigin
>
> **Repo/Website Link**
> [https://github.com/Eigin-AI/Eigin](https://github.com/Eigin-AI/Eigin)
>
> **Description**
> Eigin is a personal AI agent built to be private, safe and under your control.
>
> It's local-first, which means that data is stored on your device and the agent harness itself runs locally. It's a closed-set agent, which means a fixed set of declared tools without a shell, permissions baked into the execution path.
>
> Eigin builds personal context through an on-device knowledge graph. The data it stores is accessible to read, edit and export. For AI inference, you can choose local on-device models, our EU-hosted cloud, or any OpenAI-compatible provider (including homelab).
>
> The project is open source under AGPLv3. Happy to collaborate!
>
> **Deployment**
> The Eigin agent runs on your iPhone. We're working on more platforms. You can build the app from source or download the beta via our site: [https://www.eigin.ai/en/#get](https://www.eigin.ai/en/#get)
>
> Our Relay ships as a Docker img, and we provide Terraform config for hosting it on Scaleway.
>
> For inference you can use local model (Gemma A2B on iPhone 15+) or self-host via something like LiteLLM or whatever you prefer.
>
> **AI Involvement**
> Yes. It's an AI agent. (supervised) coding agents are being used in implementing it.

---

> **AntonioKarot**（2 分） · 2026-11-11T21:30:51+08:00　
> **Elysia**: self-hosted image host, built to sit next to your website
>
> Lets your users upload images (file, clipboard or URL). It re-encodes them to WebP/JXL/AVIF/PNG/JPEG, strips metadata, removes duplicates and serves them under stable links. It's made to pair with [Arcadia](https://github.com/Arcadia-Solutions/Arcadia) but works with any site.
>
> * OIDC SSO, API keys, uploads on behalf of users, hotlink protection
> * Moderation: reports, trash, expiry, user management
> * Similar image detection and cleanup of images your site no longer references
> * Chevereto importer with link rewriting
> * Admin dashboard, rate limiting, OpenTelemetry, custom CSS/JS/branding
>
> Stack: Rust (actix-web) + PostgreSQL, Vue 3 frontend. AGPL-3.0. Runs with `docker compose`.
>
> * GitHub: [https://github.com/Arcadia-Solutions/Elysia](https://github.com/Arcadia-Solutions/Elysia)
> * Docs: [https://arcadia-solutions.github.io/Elysia/](https://arcadia-solutions.github.io/Elysia/)
>
> Feedback welcome!

---

> **karkardagi**（1 分） · 2026-11-11T21:36:28+08:00　
> **Project Name: Dakia**
>
> **Repo/Website Link:** [https://dakiamail.com/](https://dakiamail.com/), [https://github.com/DakiaMail/dakia-web](https://github.com/DakiaMail/dakia-web)
>
> **Description:**
>
> Dakia is an **email-client** that lets you combine your various email accounts into one unified inbox view. Connect all your accounts together once and access them via all your devices.
>
> **Coolest features:**
>
> * Dakia features **on-device offline translation** (similar to firefox/arc browsers)
> * Dakia features an **on-device machine learning model** that accurately categorizes mail into categories.
> * Dakia is **extremely lightweight and blazing fast on your server and devices**
> * **Snooze** mail for later (mail hides from the inbox and then comes back later)
> * **Keyboard shortcuts** fully supported!
> * **Privacy controls** allow you to block remote images, trackers and so on.
> * **Block unwanted senders** across all your accounts
> * **Near-instant push notifications** on new email arrival.
>
> There is a similar popular project named **pl\_mail**. The main differences are:
>
> * Dakia has a much smaller scope: no planned support for calendar, JMAP, PGP encryption and so on. I want to keep the bloat out and keep Dakia focused.
> * Dakia is built on rust vs PHP for pl\_mail, has a very extensive test suite that includes performance benchmarking against other email clients (Dakia is the fastest for initial sync and most actions).
> * I feel like pl\_mail is already too bloated and moving too fast. Dakia aims to be focused, polished and grow slowly and deliberately.
>
> **Deployment:** You can self-host Dakia right now. Read the [setup guide](https://github.com/DakiaMail/dakia-web/blob/main/docs/hosting.md).
>
> **AI Involvement:** AI assistance heavily used but most of the core of the product is built on top of battle-tested mature rust libraries. The AI assistance is in the application layer around them.

---

> **il_doc**（1 分） · 2026-11-11T22:40:27+08:00　
> **Project Name:** Pickarr
>
> **Repo/Website Link:**
> - Repo / docs: https://github.com/ildoc/Pickarr
> - Screenshots: https://imgur.com/a/Y1NeXbP
>
> **Description:**
> I'm trying to leave streaming services and their constantly-increasing prices, but I like the way their catalog are made and I like to browse them. (Also I don't wanna miss out big titles just because I'm too lazy to keep updated from multiple websites at once)
>
> So I'm building **Pickarr**: a self-hosted app that syncs what a streaming service offers in a given country, lets you browse it like a catalog grid, and send picks straight to Sonarr/Radarr.
>
> **The problem it solves for me**
>
> Overseerr / Seerr are great when someone wants to *request* anything for the shared Plex/Jellyfin library. I wanted the opposite starting point: “what’s actually on Netflix IT right now?”, “what’s leaving soon?”, then one click into Arr — without a request queue.
>
> **What it does**
>
> - Syncs catalog sources (provider + country) via Watchmode, enriches with TMDB
> - Browse with All / New / Leaving / Recently removed
> - Search + filters (type, genre, year, library state)
> - Add/remove series ↔ Sonarr, movies ↔ Radarr; status on cards
> - Household profiles (up to 10, no login) — favorites, ratings, and “For you” are per profile
> - **Local** recommendations from your votes (taste data stays on your box; optional ONNX model)
> - Handy Watchmode API calls calculator to check if you're within the boundaries of the free account limits
> - One Docker image, SQLite under `/config`
>
> **Not a Seerr replacement**
>
> Pickarr is a streaming-catalog browser + Arr shortcut. Seerr is a request manager with auth, approvals, and media-server integration. They can coexist. Short comparison in the docs.
>
> **Requirements**
>
> - Watchmode API key (free plan works: 2500 credits/month, up to 3 countries)
> - TMDB API key (free for personal use on https://www.themoviedb.org/settings/api)
> - Sonarr and/or Radarr
> - linux/amd64 Docker host; `/config` on local disk (SQLite WAL — not NFS/SMB)
>
> **Caveats**
>
> - Still under development, but I'm already using it in my homelab with great satisfaction
> - No separate authentication so far, you can set different profiles each with its own reccomandations (like netflix does with its profiles)
> - Desktop-first UI, I'll work on the mobile UI next
> - v1: one Sonarr + one Radarr instance
> - Free Watchmode plan: no full leaving calendar; leaving dates are a short preview
>
> **Deployments:**
> Docker Image: `ghcr.io/ildoc/Pickarr:edge`
>
> **AI Involvment:**
> Yes, of course OF COURSE I'm using AI to build it. I've been working as a professional software developer for almost 17 years, so I'm not "vibe coding" anything.
> I'm not trying to sell anything, I thought I built something interesting and I just wanted to share it with you.

---

> **BugWhispererChen**（1 分） · 2026-11-12T00:16:16+08:00　
> \*\*Project Name:\*\* AIYIchat
>
> \*\*Repo/Website Link:\*\* [https://github.com/BugWhispererChen/AIYIchat](https://github.com/BugWhispererChen/AIYIchat)
>
> \*\*Description:\*\*
>
> I'm the author. AIYIchat is an MIT-licensed, self-hosted platform for operating AI companion services across QQ, WeChat, and the web. One deployment includes multi-bot channel management, account quotas and plan-order ledgers, signup review, content-safety auditing, offline evaluation, and observability.
>
> For end users, it provides per-service long-term memory with rule-based expiry of time-sensitive facts, deduplication governance, evidence-backed reflection, deterministic AI-tone checks, and back-off when proactive messages are ignored. Voice input/replies, image understanding/generation, and stickers are also included.
>
> Current limits: the UI and built-in personas are Chinese-only; voice cloning and TTS require DashScope; rate limits and admin sessions use single-instance in-memory storage; there is no third-party payment integration.
>
> \*\*Deployment:\*\*
>
> Docker Compose runs directly from source with automatic certificate setup. A Windows installer bundles the database and audio toolchain, and the Linux package uses a [deploy.sh](http://deploy.sh) script. Installation and configuration instructions are in the repository README. A model API key and admin password are required.
>
> \*\*AI Involvement:\*\*
>
> Yes. AI coding assistants were used during development and documentation, and this submission itself is AI-assisted. I review the code, run the project checks, and remain responsible for the project and replies.

---

> **Throwable_dev427**（2 分） · 2026-11-12T04:19:42+08:00　
> Hi All,
>
> **Project Name**: SonNuage
>
> **Repo/Website Link**:
>
> * **Repo** [https://github.com/SonNuage/sonnuage](https://github.com/SonNuage/sonnuage)
> * **Site with screenshots of my own instance** [https://sonnuage.github.io/en/](https://sonnuage.github.io/en/))
>
> **Description**: A self-hosted music server I built for my own use, because the existing options did not fit the way I listen. I tried already some options with Subsonic servers, and found it painful to use. It is therefore a personal project in the beginning, and has been public for about two weeks, and I would not call it production ready. I'm still doing lots of work on it, feature-wise for the time being, and i'll work on the UI/UX + performances later. But to let you know, it works on my "homelab" which is a I5 10500, with lots of others services already (gitlab etc), and it's just smooth as hell to me.
>
> **Clients**: where each one stands today.
>
> * **Web player**: OK. It is the reference client, the one I use every day.
> * **Android app (APK, with Android Auto)**: OK. In daily use for more than a week and a half. Need to be approved through the Android Auto Dev menu, because not on the store for now. Will probably come later, but as the server is Subsonic-ready, you can use whatever client you already own on the playstore.
> * **Desktop app (Windows, macOS, Linux)**: "OK". I only use it occasionally, so it is less tested.
> * **iOS app**: alpha testing. No user for now, hard to tell if it's ok enough.
> * **Browser extension**: work in progress, unsigned.
>
> **Deployment**: One Docker container (server, web player, ffmpeg, built-in SQLite database), music folder mounted read-only. The repo has a sample compose.yaml and .env.example: copy the .env, set MUSIC\_DIR, then "docker compose up -d". The sample setup assumes your own Cloudflare tunnel, any other reverse proxy you set up yourself. The interface, the website, and the README are all in FR and EN.
>
> **AI Involvement**: Most of the code was written with multiple AI models. Began with OpenCode, switch to Claude some weeks ago. My part is deciding what to build, how, the architecture choices, review and real-world testing on my instance. The code is open (AGPL-3.0) if you want to read it.
>
> Feedback and criticism are warmly welcome.

---

> **raajkt**（1 分） · 2026-11-12T04:24:53+08:00　
> * **Project Name:** Mitra Home
>
> * **Repo/Website Link:** https://github.com/rNetGit/mitra-home-app (AGPL-3.0; source public since 9 Nov 2026, website and signed installers since mid-Oct 2026) · Demo, no install: https://rnetgit.github.io/mitra-home/demo/?ref=reddit-selfhosted
>
> * **Description:** A household organizer for bills, papers, the family calendar and a wall tablet. Our bills, insurance papers and kids' dates were spread across email, drawers and three apps; we missed a renewal once and I wanted one place that stays on our own machine. You drop in bills, statements and photos of papers; it files them by year and type, pulls out due dates and reminds you before they pass. Spending by category and recurring payments come from statements you download (CSV, OFX/QFX, or a PDF with a text layer: no AI needed); optional daily bank sync through SimpleFIN Bridge (you pay them, about $1.50 a month). It also has an inventory with warranty dates, one family calendar, and Mitra Wall: an old tablet that shows the week, kids' chores and lists. No account with me, no telemetry; the only self-started call is a daily update check you can turn off. Free; the iPhone and Android apps are free companions to the self-hosted backend (closed source).
>
> * **Deployment:** It started as a Windows/Mac app (signed installers). Release **v0.148.0** (11 Nov 2026) adds Docker for a home server: `git clone --branch v0.148.0 https://github.com/rNetGit/mitra-home-app.git`, then `docker compose build`, `docker compose run --rm mitra setup`, `docker compose run --rm mitra pin NAME adult`, `docker compose up -d`. **There is no prebuilt image on a registry yet: you build it from the release.** Steps also on https://rnetgit.github.io/mitra-home/install.html (Linux server tab). The container serves phones and wall tablets only (HTTPS on one port, a PIN is required, no desktop browser UI). Pairing a phone or wall is a terminal command that draws a QR. Data lives in one volume, backups in a second. Updating = check out the next tag, rebuild, `up -d`; the database is migrated with a backup first (tested by swapping images on the same volume; v0.148.0 is the first Docker release, so no real version-to-version update has happened yet). Docs: docs/DOCKER.md, README, SECURITY.md and THREAT_MODEL.md in the repo. Stack: Python (FastAPI, Jinja2, HTMX), SQLite, plain files. Tested on x86 (Docker Desktop) and Apple silicon; phone app paired and used against it; **not tested on a Raspberry Pi or NAS**. Public beta; the database is not encrypted at rest (use disk encryption), backups can be. My family has used it daily since October 2026 (bills, papers, a wall tablet in the kitchen); v0.148.0, frequent small releases.
>
> * **AI Involvement:** Heavy. The code was written with an AI coding assistant (Claude Code); the repo contains its instruction files (CLAUDE.md, AGENTS.md). I decide what to build, review what it writes, and test every release myself on a PC, a Mac, Android, iPhone, iPad and Fire tablets. About 1,800 automated tests run before every release, releases are signed, and CI runs on pull requests that change code. The app's own AI features are optional and off unless you add your own API key or a local model; names and account numbers are masked before anything is sent to the provider you chose.
>
> I'm the developer; critical questions welcome.

---

> **Wujajin**（1 分） · 2026-11-12T05:04:53+08:00　
> \*\*Project Name:\*\* [Rocket.Chat](http://Rocket.Chat) Team Gateway for Hermes Agent
>
> \*\*Repo/Website Link:\*\*
>
> \- Repo: [https://github.com/csabatatrai-ulx/hermes-rocketchat-team-gateway](https://github.com/csabatatrai-ulx/hermes-rocketchat-team-gateway)
>
> \- Docs: [https://csabatatrai-ulx.github.io/hermes-rocketchat-team-gateway/](https://csabatatrai-ulx.github.io/hermes-rocketchat-team-gateway/)
>
> \*\*Description:\*\*
>
> I wanted an AI agent in our team chat without our conversations leaving our own servers, so I wrote a [Rocket.Chat](http://Rocket.Chat) adapter for Hermes Agent (Nous Research's open source agent). It's my entry for their plugin hackathon, Apache-2.0.
>
> What it does in a shared room:
>
> \- Each person gets their own session and room context, so two people asking at once don't get mixed up
>
> \- Hermes commands are refused over chat by default; an admin allows the ones they want
>
> \- When the agent wants to run something dangerous (say \`rm -rf\`), it posts a card with buttons, and only the person who asked can approve it
>
> \- After a restart or a network outage it catches up, and nothing runs twice
>
> It only carries messages between Rocket.Chat and Hermes. The tools come from your Hermes setup (built-in tools, skills, MCP servers). With a local model (I tested a Qwen model on vLLM), the chat, the agent and the model all stay in-house. With one Hermes instance per person, the same plugin also works as a personal assistant in Rocket.Chat DMs.
>
> Limits, to be upfront:
>
> \- [Rocket.Chat](http://Rocket.Chat) 8.7 - 9.x; I've run it live on 8.9, while 9.x support comes from reading the API
>
> \- A personal-assistant setup needs one Hermes instance per person
>
> \- Not tested on the mobile app yet (the buttons should work; typing \`@hermes /approve\` always does)
>
> \*\*Deployment:\*\*
>
> Released as v1.0.0. On an existing Hermes install (0.22.3 or newer):
>
> hermes plugins install csabatatrai-ulx/hermes-rocketchat-team-gateway --enable then \`hermes gateway setup\` walks you through connecting it to your [Rocket.Chat](http://Rocket.Chat) server. Setup, configuration and troubleshooting are in the docs.
>
> To try it without a Rocket.Chat server, there is a Docker Compose stack (Rocket.Chat, MongoDB, the official Hermes image and the plugin):
>
> git clone [https://github.com/csabatatrai-ulx/hermes-rocketchat-team-gateway](https://github.com/csabatatrai-ulx/hermes-rocketchat-team-gateway)
>
> cd hermes-rocketchat-team-gateway
>
> docker compose -f try/compose.yaml up -d
>
> Open [http://localhost:3000](http://localhost:3000), sign in as alice / hermes-demo, say "@hermes hi" in #hermes-demo. It starts with a scripted demo model, so no account or API key is needed; you can switch to a real model later.
>
> \*\*AI Involvement:\*\*
>
> Built with AI coding assistance (Claude Code). I designed it, reviewed and tested every change; it has 780 automated tests in CI on the oldest and newest supported Hermes, plus live end-to-end runs against a real [Rocket.Chat](http://Rocket.Chat), including a restart, a network outage and real clicks on the approval buttons.
>
> https://i.redd.it/pl7j8lkws11i1.png
>
> Feedback welcome, especially from anyone running [Rocket.Chat](http://Rocket.Chat) for a team.

---

> **Wujajin**（1 分） · 2026-11-12T05:07:53+08:00　
> **Project Name:** [Rocket.Chat](http://Rocket.Chat) Team Gateway for Hermes Agent
>
> **Repo/Website Link:**
>
> * Repo: [https://github.com/csabatatrai-ulx/hermes-rocketchat-team-gateway](https://github.com/csabatatrai-ulx/hermes-rocketchat-team-gateway)
> * Docs: [https://csabatatrai-ulx.github.io/hermes-rocketchat-team-gateway/](https://csabatatrai-ulx.github.io/hermes-rocketchat-team-gateway/)
>
> **Description:**
>
> I wanted an AI agent in our team chat without our conversations leaving our own servers, so I wrote a [Rocket.Chat](http://Rocket.Chat) adapter for Hermes Agent (Nous Research's open source agent). It's my entry for their plugin hackathon, Apache-2.0.
>
> What it does in a shared room:
>
> * Each person gets their own session and room context, so two people asking at once don't get mixed up
> * Hermes commands are refused over chat by default; an admin allows the ones they want
> * When the agent wants to run something dangerous (say `rm -rf`), it posts a card with buttons, and only the person who asked can approve it
> * After a restart or a network outage it catches up, and nothing runs twice
>
> It only carries messages between Rocket.Chat and Hermes. The tools come from your Hermes setup (built-in tools, skills, MCP servers). With a local model (I tested a Qwen model on vLLM), the chat, the agent and the model all stay in-house. With one Hermes instance per person, the same plugin also works as a personal assistant in Rocket.Chat DMs.
>
> Limits, to be upfront:
>
> * [Rocket.Chat](http://Rocket.Chat) 8.7 - 9.x; I've run it live on 8.9, while 9.x support comes from reading the API
> * A personal-assistant setup needs one Hermes instance per person
> * Not tested on the mobile app yet (the buttons should work; typing u/hermes `/approve` always does)
>
> **Deployment:**
>
> Released as v1.0.0. On an existing Hermes install (0.22.3 or newer):
>
>     hermes plugins install csabatatrai-ulx/hermes-rocketchat-team-gateway --enable
>
> then `hermes gateway setup` walks you through connecting it to your [Rocket.Chat](http://Rocket.Chat) server. Setup, configuration and troubleshooting are in the docs.
>
> To try it without a Rocket.Chat server, there is a Docker Compose stack (Rocket.Chat, MongoDB, the official Hermes image and the plugin):
>
>     git clone https://github.com/csabatatrai-ulx/hermes-rocketchat-team-gateway
>     cd hermes-rocketchat-team-gateway
>     docker compose -f try/compose.yaml up -d
>
> Open [http://localhost:3000](http://localhost:3000), sign in as alice / hermes-demo, say "@hermes hi" in #hermes-demo. It starts with a scripted demo model, so no account or API key is needed; you can switch to a real model later.
>
> **AI Involvement:**
>
> Built with AI coding assistance (Claude Code). I designed it, reviewed and tested every change; it has 780 automated tests in CI on the oldest and newest supported Hermes, plus live end-to-end runs against a real [Rocket.Chat](http://Rocket.Chat), including a restart, a network outage and real clicks on the approval buttons.
>
> https://i.redd.it/qmpiu41gt11i1.png
>
> Feedback welcome, especially from anyone running [Rocket.Chat](http://Rocket.Chat) for a team.

---

> **dasimers**（1 分） · 2026-11-12T06:12:59+08:00　
> Love this

---

> **nbnicholas**（3 分） · 2026-11-12T07:29:57+08:00　
> **Project Name:** Patchboard
>
> **Repo/Website Link:** [https://github.com/sourpatchdad/patchboard](https://github.com/sourpatchdad/patchboard)
>
> **Description:** A start page for your home server that tells you what's broken. It reads the Docker socket, finds your apps, and puts a stopped container, a full pool or a failed backup at the top of the page, each with a link to the fix. I built it because my wife wanted our cameras, email and media on her phone, and I wanted the server's problems and controls in the same place.
>
> * Boards you arrange by dragging. Ours are Home, Media, and House.
> * A page for each container with update, restart, rollback, live logs and a 30-day health history.
> * 68 integrations you set up from Settings, with keys encrypted on the server: Sonarr, Radarr, Plex, Jellyfin, Home Assistant, TrueNAS, Immich, Miniflux and more.
> * Alerts through ntfy, Gotify, Pushover, Discord, email or a webhook.
> * Installs on a phone as an app.
>
> Screenshots and the story behind it: [https://www.reddit.com/r/selfhosted/s/yuLGQKVKXq](https://www.reddit.com/r/selfhosted/s/yuLGQKVKXq)
>
> **Deployment:** One Docker container for amd64 and arm64, about 50 MB of memory. The README has a compose file and a one-line demo with fake data:
>
>     docker run --rm -p 3200:3200 -e DEMO=1 ghcr.io/sourpatchdad/patchboard:latest
>
> The docs cover every screen, each integration, configuration and security.
>
> **AI Involvement:** Most of the code was written by coding agents working from my direction. I made the product and design choices, reviewed changes, and tested everything on my server. AI helped me build 240+ automated tests, CI on every commit, layout and accessibility checks in a real browser, and a security review of anything that fetches outside content or touches the Docker socket.
>
> https://i.redd.it/swn6wo8ji21i1.png

---

> **KnownObligation9934**（1 分） · 2026-11-12T11:52:18+08:00　
> **Project Name:** ServerOS
>
> **Repo:** [https://github.com/serveroshq/panel](https://github.com/serveroshq/panel)
>
> **Description:**
>
> Hey everyone! My co-founder and I have been building ServerOS for the past few months, and we've recently made it open source under AGPL-3.0.
>
> It's a server management panel that lets you manage multiple servers from one place, including deployments, monitoring, backups, OS updates, firewall management, logs and AI-assisted troubleshooting.
>
> The goal is to make managing your own infrastructure easier without giving up control of your servers.
>
> **Deployment:**
>
> You can self-host the entire panel. We've put together a guide here:
>
> [https://docs.serveros.com/guides/self-hosting](https://docs.serveros.com/guides/self-hosting)
>
> **AI Involvement:**
>
> We use AI tools to assist with development, including writing, reviewing and debugging code.
>
> Would love to hear what you think! It's still early, so feedback, criticism and contributions are all welcome.
>
> https://i.redd.it/6ho1xtplt31i1.png

---

> **ImaginationVarious30**（1 分） · 2026-11-12T16:37:38+08:00　
> I built a small rotating proxy that runs in Docker and keeps its pool filled from a public proxy list that gets checked every hour.
>
> \`\`\`
>
> echo "PROXY\_PASSWORD=$(openssl rand -hex 16)" > .env
>
> docker compose up -d
>
> curl -x "http://any:@127.0.0.1:8899" https://api.ipify.org
>
> \`\`\`
>
> One port speaks HTTP and SOCKS5, and each connection leaves through a different proxy. The username selects what you want: \`country-de\`, \`type-socks5\`, or \`session-NAME\` for a sticky exit. Proxies that fail get dropped and re-checked every 5 minutes, and every 6 hours it pulls the new hourly list and adds what works. There's a live dashboard at \`/\_\_proxy-scraper/\`, a JSON status, and \`/metrics\` for Prometheus.
>
> It refuses to listen on anything but [127.0.0.1](http://127.0.0.1) without a password, because Docker publishes ports past ufw and an open proxy gets found within hours. The compose file binds to localhost.
>
> Free proxies are run by strangers and churn constantly. The hourly list has \[LIVE\] entries right now that passed every check, and roughly a quarter are still there a day later. Fine for public data and for testing geo-blocking or your own rate limits, not for logins.
>
> MIT, Python, no database: [https://github.com/maximilianfeix/proxy-scraper](https://github.com/maximilianfeix/proxy-scraper) (compose.yaml in the root, docs/proxy-server.md)

---

> **g_host1412**（1 分） · 2026-11-12T22:50:37+08:00　
> **ShortsFlow**: self-hosted, open-source Opus Clip alternative. Podcast or interview in, captioned vertical clips out.
>
> You give it a video file or link. Whisper (local) transcribes it, the clips are cut on sentence boundaries with a crop that follows whoever is talking, and captions are burned in. No account, no API key and no upload are needed for the clipping itself.
>
> * Install: `pip install "shortsflow[clip]"` then `shortsflow clip my_video.mp4`, a one-click Windows installer (unsigned), a Mac/Linux one-liner, or Docker
> * Browser app with a review screen and an editor to trim or restyle one clip
> * Optional AI (Gemini/Groq or a local Ollama) writes titles and helps pick moments; off by default
> * MIT. The optional animated captions use Remotion (source-available, free for individuals and small teams)
> * Quality is measured on public videos with no AI key, weak spots included: [https://github.com/ghost1412/shortsflow/blob/main/docs/BENCHMARKS.md](https://github.com/ghost1412/shortsflow/blob/main/docs/BENCHMARKS.md)
>
> **AI involvement:** . Honest limits: one-person project; transcribing a long video on CPU is slow; no comparison with Opus Clip yet. Repo: [https://github.com/ghost1412/shortsflow](https://github.com/ghost1412/shortsflow). Feedback and bug reports welcome (please include `shortsflow doctor` output).

---

> **supportingthedogs**（1 分） · 2026-11-13T02:20:11+08:00　
> **Project Name:** Yogurt
>
> **Repo/Website Link:** [https://github.com/FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)
>
> **Description:** A free, MIT licensed desktop app that uses on-device AI models to transcribe, summarize, and chat with your meetings. Similar to Granola, Yogurt runs in the background and does not join your calls. But unlike Granola, it's open-source, free to use, and private. Your meeting transcripts, call recordings, and summaries never leave your computer.
>
> I tried some of the most popular OSS note taking tools, and most were missing features like calendar integration and an MCP server, or required you to connect or create an account. They also didn't feel polished enough to be something I actually wanted to use daily, so I built Yogurt to scratch that itch.
>
> * Transcription with whisper.cpp, or Apple's on-device SpeechAnalyzer if your system supports it.
> * Summaries and questions with a local open weight LLM (llama.cpp), downloaded and set up automatically based on what your hardware can handle without your cooling fans firing off like crazy.
> * A local MCP server, so you can share your notes with Anthropic, OpenAI, etc. directly. No paid cloud service as a middleman.
> * Calendar integration, echo detection/reduction, global/folder/local search, and recordings that end on their own.
> * No account, nothing to connect.
>
> **Deployment:** A desktop app for Mac (Apple Silicon), Windows and Linux (AppImage), built with Electron. Download, open it, and it picks and downloads the models your computer can run. It updates itself. The README has the downloads and docs/building.md covers building from source.
>
> **AI Involvement:** Most of the code was written by coding agents working from my direction. I made the product and design choices, reviewed changes, and tested everything on my own meetings. AI helped me build 1,600+ unit tests and 300+ end-to-end tests, CI on Mac, Windows and Linux on every commit, and the on-device model evals used to pick which models run on which hardware.
>
> Would love to hear what you think about the onboarding and note taking experience :)

---

> **cackmobile**（1 分） · 2026-11-13T03:35:06+08:00　
> Dude! I've got the full arr setup slowly built over years. Friends have asked me to set it up for them but I truly can't be arsed as there's so much to do and then to learn. If this works it's fantastic. Good effort

---

> **cackmobile**（1 分） · 2026-11-13T03:48:34+08:00　
> Bro! I'll be a tester. I have a family and have seen these skylight panels around and like then but don't want to pay the ridiculous price especially here in Australia where we have what's called the Australia tax on everything

---

> **play_tettris**（1 分） · 2026-11-13T03:56:02+08:00　
> **Project Name:** GaiaCP
>
> **Repo/Website Link:** https://github.com/tetterip/GaiaCP (site: https://gaiacp.digital)
>
> **Description:** A free, GPL-3.0 billing and provisioning panel for small hosting businesses, a lighter take on WHMCS. It keeps track of your clients and what they owe, sends the payment notices and reminders, and creates, suspends and renews their hosting and domains for you.
>
> I run a small hosting business and was paying more for WHMCS every year for a panel that does far more than I need, can't be read or changed, and only runs where its licence lets it. So I built GaiaCP for myself and opened it up for anyone in the same spot.
>
> * Payment notices before each due date, reminders and overdue notices, automatic suspension of unpaid hosting and unsuspension once it's paid.
> * Hosting accounts on cPanel/WHM, Plesk, DirectAdmin, HestiaCP, CyberPanel, Virtualmin and Enhance, and VPS on Proxmox VE.
> * Domains registered, renewed and synced at Enom, Namecheap, NameSilo, Openprovider, GoDaddy, ResellerClub and others.
> * A client area where clients order, pay (Stripe, PayPal, bank transfer), open tickets and log in to their hosting panel, plus an optional public site with domain search and a cart.
> * Every integration is one of 50+ plugins you can turn off, with a signed plugin catalogue, a REST API, webhooks and an import from WHMCS.
> * It never charges cards by itself: it only records payments you, Stripe or PayPal confirm. No saved cards.
>
> There's a demo with a made-up hosting company, reset every 10 minutes: https://demo.gaiacp.digital (admin@example.com / demo)
>
> **Deployment:** `docker compose up -d --build` runs the app, the scheduler and MariaDB, installed and ready at localhost:8080. Or upload the release zip to ordinary shared hosting with PHP 8.3+, MySQL/MariaDB and one cron job: no SSH, Composer or Node needed, and it works in a subfolder. It updates itself from signed releases (with a backup first). Built with Laravel and Filament. The docs cover installation, Docker, an admin guide, writing plugins and the API.
>
> **AI Involvement:** Most of the code was written by coding agents (Claude Code) working from my direction. I made the product and design choices, reviewed changes, and test it on my own business. AI helped me build 1,900+ automated tests, CI on PHP 8.3, 8.4 and 8.5 with static analysis on every commit, and security reviews before each release.
>
> I'd love to hear from anyone who sells hosting or domains, especially about what would stop you from switching.

---

> **3DNebGuy**（1 分） · 2026-11-13T04:18:19+08:00　
> Project Name: AmberSight
>
> Rep: [https://github.com/HuskerMinion/AmberSight](https://github.com/HuskerMinion/AmberSight)
>
> Description
>
> A modern NVR that I replaced Blue Iris with this at the end of October. It runs 26 cameras across two sites: 18 on one server built in Rust, 8 on the other. Repo went public this week.
>
> \- Records RTSP/ONVIF cameras. Continuous, or sub stream continuous with main stream around events.
>
> \- Browser live view over fragmented MP4 (Media Source). Synced timeline, fast and reverse playback, export.
>
> \- Object detection with YOLOX on CPU or GPU (DirectML on Windows). Plate reading, face recognition, CLIP search, loud-sound trigger.
>
> \- Alerts: ntfy, Pushover, Telegram, email, webhooks, MQTT with Home Assistant discovery, Web Push.
>
> \- Per-camera user access, TOTP, its own name-constrained CA for HTTPS, Ed25519-signed self-update.
>
> \- Reolink Argus battery cameras without a Home Hub.
>
> \- Android app for phone and Android TV, in closed testing for Google Play. I need testers. DM me.
>
> Also supports older Argus 2/3 (tested) battery cameras that don't listen on RTSP and can't join a hub (Argus 2). AmberSight talks to them directly over Reolink's own protocol.
>
> How it works:
>
> 1. On motion the camera sends a short message to pushx.reolink.com.
> 2. A local DNS entry (Pi-hole or your router) points that name at AmberSight.
> 3. AmberSight wakes the camera, logs in (2-3 seconds), records while motion lasts, then logs out so the camera sleeps.
> 4. About 90 seconds later it pulls the start of the event off the camera's SD card and puts it in front of the live recording, so the clip starts when motion started.
> 5. Click the camera in AmberSight to wake it for live view
>
> Packages: Windows installer, .deb/.rpm for amd64 and arm64, macOS tarballs.
>
> Install guide is in docs/
>
> License is PolyForm Noncommercial. Free for personal use, source-available, not OSI open source.I wrote this with an AI coding assistant doing a large share of the code. I set the design, review the changes, and test every release on Windows, macOS and Linux before it ships.https://github.com/HuskerMinion/AmberSight a large share of the code. I set the design, review the changes, and test every release on Windows, macOS and Linux before it ships.
>
> [https://github.com/HuskerMinion/AmberSight](https://github.com/HuskerMinion/AmberSight)

---

> **karloks2005**（1 分） · 2026-11-13T04:42:53+08:00　
> https://i.redd.it/seidxko7u81i1.png
>
> I've been building **Infradeck**, a self-hosted dashboard for homelabs, and just released 1.0.0.
>
> One machine runs the dashboard, and every other machine runs a small collector. It works the same on one LAN or across sites and VPSes.
>
> **What it does**
>
> * **Hosts:** CPU, RAM, load, swap, network, and disk and inode usage for every mounted filesystem.
> * **Containers:** CPU, memory, I/O, ports, health, restarts and exit codes, grouped by Compose project, with history.
> * **System events:** reboots, OOM kills, kernel faults, pending updates, listening ports and firewall changes.
> * **Uptime checks:** HTTP, keyword, JSON value, TCP, TLS expiry, DNS and ping, run from the machines you pick, so you can tell a broken service from a broken network path.
> * **Incidents:** one incident per problem, closed automatically when it clears. Notifications go to ntfy, Discord, a webhook or email.
> * **Statistics:** from the last hour to all time, plus a "disk full in \~N days" estimate.
>
> **Security, since it touches Docker on every host**
>
> * Collectors never get the Docker socket. A tiny proxy allows a few read-only requests and nothing else.
> * Collector endpoints are only reachable through a separate gate bound to your VPN address, not your public domain.
> * Every image is signed with cosign and built for amd64 and arm64, and installs pull them by version or digest.
> * Two-factor sign-in is required for admins.
>
> **Optional AI incident agent, off by default.** Bring your own Anthropic, OpenAI or Gemini key and it diagnoses incidents from masked data and suggests a fix. It only reads; it never runs commands on your servers.
>
> **What it isn't:** not a log collector, not a remote control (it never restarts or changes anything), and not a high-resolution time-series database.
>
> Stack: FastAPI, PostgreSQL, Redis, React, Docker Compose. License: AGPL-3.0.
>
> **GitHub:** [https://github.com/karloks2005/Infradeck](https://github.com/karloks2005/Infradeck)
>
> Feedback is very welcome, especially on setup and on what's missing for your setup.
>
> >Disclosure: I am a software engineering student. Claude Code coding agent was used in the development of this project. Most of the code was reviewed by myself before committing.

---

> **Jolly-Fisherman9406**（1 分） · 2026-11-13T05:00:22+08:00　
> * **Project Name:** Jōb
>
> **Repo**: [https://github.com/youssefamr74/job-public](https://github.com/youssefamr74/job-public)
>
> **Demo with fake data**: [https://jobcompanion.site/demo](https://jobcompanion.site/demo)
>
> **Description:**
>
> I saw a few posts asking how to organise job applications, and yeah when you send 300+ it's a lot of work to keep track. I built my own app for that 5 months ago and last week I decided to open source it.
>
> You connect your gmail and it tracks your applications by itself, applied, interview, rejected etc. It also has analytics and a weekly report.
>
> **Deployment:**
>
> There's a Docker image on GHCR (amd64 and arm64) and a docker-compose file in the repo. Just download the compose file, run docker compose up -d, open localhost:8000 and the setup wizard walks you through connecting Gmail. It's one container with SQLite, your data stays in a folder next to it, it only listens on localhost and there's no telemetry. Docs for Gmail and AI setup are in the repo.
>
> **AI Involvement:**
>
> I wrote the app myself; most of the backend is mine. I used Claude Code to help turn it into the open-source version, cleanup, local setup and the web UI. In the app AI is optional, it's just a backup for emails the rules can't figure out. You can use your own API key, a local model with Ollama, or skip it, works fine without.

---

> **TheDude906231**（1 分） · 2026-11-13T05:44:38+08:00　
> Hell ya. That would be sweet. Let me know what you think. DM if you need help setting it up. Everything worked pretty well. Using Google keep notes is really the only jank part. They don't allow API access to it anymore for some reason

## 关联链接

- https://www.reddit.com/r/selfhosted/search/?q=

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
