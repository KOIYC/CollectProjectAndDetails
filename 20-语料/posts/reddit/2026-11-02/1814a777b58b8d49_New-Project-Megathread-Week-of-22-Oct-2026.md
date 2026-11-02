---
type: "corpus"
item_id: "1814a777b58b8d49"
title: "New Project Megathread - Week of 22 Oct 2026"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xcw6eb/new_project_megathread_week_of_22_oct_2026/"
author: "AutoModerator"
published_at: "2026-10-23T06:01:08+08:00"
captured_at: "2026-11-02T09:38:59+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-10-23"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - New Project Megathread
metrics: {"score": 39, "comments": 231, "upvote_ratio": 0.9333333333333333}
comments_count: 152
comments_total: 231
discovered_via: "reddit:14d+settle10"
---

# New Project Megathread - Week of 22 Oct 2026

> [!info] 一句话导读
> Welcome to the **New Project Megathread!**

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xcw6eb/new_project_megathread_week_of_22_oct_2026/>
> 指标：得分=39 · 评论=231 · 赞踩比=0.9333333333333333
> 作者：AutoModerator　|　发布：2026-10-23T06:01:08+08:00
> 项目链接：—
> 采集：2026-11-02T09:38:59+08:00　|　id：`1814a777b58b8d49`

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

## 评论（152/231）

> **anitamaxwynnn69**（1 分） · 2026-10-23T06:10:34+08:00　
> **Project Name:** [www.overtchat.com](http://www.overtchat.com)
>
> **Repo/Website Link:** [https://github.com/yoloyash/overtchat](https://github.com/yoloyash/overtchat)
>
> **Description:** A lightweight self-hosted chat client, alt to Open WebUI. I built it because my partner and family use ChatGPT but don't care about privacy. I already self-host vLLM on 8x 3090s and wanted a polished, private alternative they could actually use. OWUI is too heavy and complex for non-technical users. overtchat is chat-first with built in tts/stt/search, no rag/plugins/agentic bloat, no external api keys. Free native [Android](https://play.google.com/store/apps/details?id=com.overtchat.mobile) and [iOS](https://apps.apple.com/app/overtchat/id6812165221) Apps, plus a [desktop app](https://github.com/yoloyash/overtchat/releases/tag/desktop-v0.2.0) for macOS (Apple Silicon/Intel) and Linux (AppImage/Deb/RPM). MIT licensed, no telemetry, no analytics.
>
> **Deployment:** curl -fsSL [https://overtchat.com/install](https://overtchat.com/install) | sh
>
> **AI Involvement:** Yes, definitely vibe coded.
>
> Would love to have some feedback :)

---

> **Alternative_One_4804**（3 分） · 2026-10-23T06:23:42+08:00　
> **Project Name:** OpenTodo
>
> **Repo/Website Link:** [https://github.com/pixari/OpenTodo](https://github.com/pixari/OpenTodo) \- [https://open-todo.app](https://open-todo.app) \- demo (no sign-up): [https://demo.open-todo.app](https://demo.open-todo.app)
>
> **Description:** A task manager you host yourself, for people who want something like Todoist or TickTick without the subscription and without their tasks living on someone else's server.
>
> I started it for myself and open sourced it. Then a lot of you wrote to me here with the same problem and the same wishes, and many people started testing it, opening issues and telling me what was missing. Most of what's in it now came from those conversations, so thank you.
>
> https://i.redd.it/zss7x760h3xh1.png
>
> **What it does:**
>
> \- Local-first: the app works offline and syncs between your devices when it can reach your server
>
> \- Quick add in plain language ("call mum friday 6pm p1 #home"), projects, sections, boards, labels, filters, repeating tasks, reminders
>
> \- Today, Upcoming, a Plan view, a weekly review, time tracking
>
> \- Workspaces and sharing, comments, task pages to hand one task to someone without an account
>
> \- CalDAV (tested with Thunderbird and todoman), a CLI, an MCP server, webhooks
>
> \- Import from Todoist, TickTick, Things, Google Tasks, Trello, Asana, Microsoft To Do and more
>
> \- Optional end-to-end encryption
>
> \- No telemetry, no third-party calls except optional maps (which go through your server)
>
> **Deployment:** One container, SQLite, no other services: "docker run -d -p 8080:8080 -v opentodo-data:/data ghcr.io/pixari/opentodo:stable"
>
> Open [http://localhost:8080](http://localhost:8080) and the first visit creates your account.
>
> There's a Compose file, plain binaries, and guides for Unraid, CasaOS, TrueNAS, Umbrel, Runtipi, Coolify, Synology, Helm and others: [https://open-todo.app/docs/](https://open-todo.app/docs/)
>
> AGPL-3.0.
>
> **AI Involvement:**
>
> A lot, and I want to be upfront about it. Most of the code is written by AI coding agents (Claude Code). My part is deciding what gets built and how it should behave: every feature starts as a written spec I review, and the agents implement it against that spec, with tests and CI gates (unit, end-to-end, accessibility, visual regression) that have to pass before anything merges. I read the specs and the results, test it myself, and I'm the one answering issues. I'm happy to talk about how that workflow works, and if something looks off in the code, please tell me.

---

> **Gully5931**（6 分） · 2026-10-23T06:46:26+08:00　
> Project Name: Hold My Docs (HMD)
>
> https://i.redd.it/0i87ar0gsaxh1.png
>
> ​Repo/Website Link:
>
> \- GitHub: [https://github.com/soollabs/holdmydocs](https://github.com/soollabs/holdmydocs)
> \- Docs: [https://hmd.sool.dev](https://hmd.sool.dev)
>
> Read only demo: [https://demo.hmd.sool.dev](https://demo.hmd.sool.dev)
>
> \> User: demo
> \> Password: a-long-secure-password
>
> Description:
>
> I've been building a self-hosted wiki that stores pages as Markdown files in a regular Git repository. Every save creates a commit, so you get version history without having to know Git yourself.
>
> I originally built it for my homelab notes and runbooks. I wanted something that didn't need a database and wouldn't lock my documentation into a particular application.
>
> It's grown beyond that. I now use it for company documentation, sharing knowledge between local LLMs running on different machines, and publishing HMD's own documentation as a static site.
>
> Features include:
>
> \- ⁠Git history, diffs, revert and optional remote sync
> \- ⁠Conflict detection that preserves your draft if another user or agent edits the same page
> \- ⁠Markdown editor, wiki-links, backlinks, Mermaid and attachments
> \- ⁠Full-text search, with optional PDF/Office indexing via Apache Tika
> \- ⁠Namespaces with separate visibility, navigation and appearance
> \- ⁠Local authentication, OIDC and scoped access tokens
> \- ⁠MCP server for AI agents with configurable permissions
> \- ⁠Static site export and read-only repository browsing
>
> It's still early-stage, so expect some rough edges. Git sync only fast-forwards; diverged histories need to be resolved manually.
>
> Deployment:
>
> Written in Go and MIT licensed. Runs as a single binary or through Docker Compose. Installation instructions are in the documentation linked above.
>
> AI Involvement:
>
> I've been a DevOps engineer for the last 8 years, and made a fair amount of open source projects that were relatively simple. This is my first using various different models across OpenRouter, generally for tests and doing repeated testing of changes across different UI screens, which has allowed me to extend the scope of what I can use this app for. it's useful to me, maybe you might find a use for it.
>
> I'd be interested in feedback, particularly from anyone already keeping their documentation in Git.

---

> **tertiaryprotein-3D**（14 分） · 2026-10-23T06:54:47+08:00　
> * **Project Name: DMKaraoke**
> * **Repo/Website Link:**
>
> Repo: [https://github.com/vttc08/demucs-karaoke-app](https://github.com/vttc08/demucs-karaoke-app)
>
> Documentation: [https://vttc08.github.io/demucs-karaoke-app/](https://vttc08.github.io/demucs-karaoke-app/)
>
> * **Description:** (What does it do? What problem does it solve? What features are included? How is it beneficial for users who may try it?)
>
> DMKaraoke is a lightweight web application for home karaoke. It uses machine learning to separate vocals and create word-by-word synced lyrics. The application is completely free, with no advertisements and zero cloud subscription fees. It creates karaoke on your own device.
>
> YouTube is a good for karaoke but not every song has a karaoke uploaded, especially for foreign content. This app uses Demucs for vocal separation, and WhisperX for lyrics alignment.
>
> I wanted to create something way back in 2022, when some friend purchased a C$600 karaoke player device with Android hardware worth of C$50. This project could bring karaoke accessible to people, all you need is a mp3 or  YouTube video and the lyrics, and you can build immersive karaoke experience with customized lyrics, immersive music videos and your own branding. And any device with a web browser can playback these packages.
>
> https://i.redd.it/m1kqlheam3xh1.png
>
> * **Deployment:**
>
> The app consists of the main app and Demucs service, the separation allows the main app to run on a potato while the Demucs ML heavy services stay on a personal gaming PC with GPU that only start when its needed.
>
> The documentation include deployment instruction: [https://vttc08.github.io/demucs-karaoke-app/getting-started/overview/](https://vttc08.github.io/demucs-karaoke-app/getting-started/overview/) include using Docker, Linux, Windows for the main app. For the Demucs service, since I have a Windows PC with Nvidia, the documentation also covers that.
>
> * **AI Involvement:**
>
> The MVP and many features were developed on the SkyTrain (Vancouver metro transit) on a phone and dev server because I wanted something productive to do for those 3 hours every day; given these circumstances, AI was heavily used to create it. I did test the application extensively, and reviewed using a desktop computer as well. I come up with idea, architecture, how I want the flow to work and examples in ffmpeg, Jupyter, Python function usage, and I ask AI to write the code and integrate it with the web app.

---

> **LilPranxis**（2 分） · 2026-10-23T07:44:55+08:00　
> https://i.redd.it/ofsw97k8v3xh1.png
>
> Project Name: Vasta
>
> Repo/Website Link: [https://github.com/ariedotme/vasta](https://github.com/ariedotme/vasta) (AGPL-3.0)
>
> Description:
>
> Self-hosted ocal-first app for notes, tasks, calendar, etc, inspired by Capacities. I liked Capacities but it wasn't everything I needed, and I wanted to self-host it. I built it for me and my girlfriend, people got interested so I open-sourced it.
>
> \- Objects with types (Books, People, Tasks, Meetings or any type you create), each with its own properties, relations and views (table, board, gallery, list…)
>
> \- Daily notes, and a Today page with the agenda, the note and the day's habits
>
> \- A command bar where one line creates things: /Task Ask Lena about companion planting assignee:lena due:fri
>
> \- Habits with streaks and a year grid; optional food tracking (off by default)
>
> \- Shared spaces with sprints, assignees, comments with @ mentions, and notifications (ntfy, Telegram or desktop)
>
> \- Capture from a Telegram bot, a browser extension or a small HTTP API into an inbox
>
> \- iCal calendar subscriptions shown together with your dated stuff
>
> \- Works offline: the browser (or desktop app) keeps a SQLite replica (WASM, in OPFS) and syncs when you're back
>
> \- MCP server and a CLI. No LLM keys or AI features inside the app
>
> \- Desktop app (Tauri) for macOS, Windows and Linux, with quick capture on a global shortcut and auto-updates
>
> \- Importer from Capacities
>
> Stack: Node + Hono, Vue 3 + TipTap + Yjs, sqlite-wasm, Tauri.
>
> Deployment:
>
> One Docker container, image [ghcr.io/ariedotme/vasta](http://ghcr.io/ariedotme/vasta)
>
>         mkdir vasta && cd vasta
>         curl -o compose.yml https://raw.githubusercontent.com/ariedotme/vasta/main/compose.example.yml
>         curl -o .env https://raw.githubusercontent.com/ariedotme/vasta/main/.env.example
>         docker compose up -d
>         docker compose logs vasta   # the setup code for the first account
>
> Then open [http://127.0.0.1:5174](http://127.0.0.1:5174) and make the first account with the setup code.
>
> Other people join with invite links. Data is SQLite, media go on disk or in any S3-compatible bucket (I use Garage). There's a built-in backup command. docs/deploy.md covers HTTPS with a reverse proxy, backups, upgrades and media buckets. Desktop apps are on the releases page.
>
> The Windows and Linux desktop builds are new and I haven't tested them myself yet (checklists in issues #29 and #30 if you want to help).
>
> AI Involvement:
>
> I used AI (Claude Code and Codex) a lot to write the code, and I reviewed it as much as my free time allowed. There's a test suite, browser checks and a sync convergence test, but not every line was read by a human. The app itself has no AI features or LLM keys; it only exposes an MCP endpoint and a CLI if you want to point your own agent at it.

---

> **NewtonLawAbider**（4 分） · 2026-10-23T07:46:27+08:00　
> 8x 3090s.. are you rich?

---

> **anitamaxwynnn69**（2 分） · 2026-10-23T07:51:43+08:00　
> Does this zip-tied wire rack look like the work of a rich man? :')
>
> https://i.redd.it/be5v5clgw3xh1.jpeg

---

> **paimonsoror**（2 分） · 2026-10-23T08:16:49+08:00　
> **Project Name:** Telltale DNS
>
> **Repo/Website Link:** [https://github.com/paimonsoror/telltaledns](https://github.com/paimonsoror/telltaledns) , [https://paimonsoror.github.io/telltaledns/index.html](https://paimonsoror.github.io/telltaledns/index.html)
>
> **Description:** A small, fast DNS resolver and ad blocker for your home network that explains every answer. Per-device and per-VLAN rules, encrypted DNS both ways, and one cluster across a Raspberry Pi and Kubernetes, all in one Rust binary with the web UI built in
>
> **Problem it solves**: I wanted the home DNS experience that Pi-hole and Technitium made popular (both are big inspirations), plus three things for my own setup:
>
> 1. \*\*Why it happened:\*\* every answer explained down to the list and the line.
> 2. \*\*One cluster:\*\* a Pi and my k3s cluster on one configuration, so DNS keeps answering while either one restarts.
> 3. \*\*GitOps:\*\* a configuration I can keep in Git and review like code.
>
> **Deployment:**
>
> \- \*\*Docker:\*\* image for amd64, arm64, and armv7 (about 13 MiB), plus a Docker Compose bundle for a Raspberry Pi.
>
> \- \*\*Native Linux:\*\* an install script with systemd and \`self-update\`.
>
> \- \*\*Kubernetes 1.26+:\*\* a Helm chart (OCI), either one pod or a controller plus stateless resolver pods.
>
> **Requirements:**  Linux. On Kubernetes, a LoadBalancer (MetalLB, Cilium, kube-vip) or \`hostNetwork\`, so it sees real client IPs.
>
> **Status:** pre-1.0. The latest release is v0.6.0, and main is 0.7.0-edge. Config keys and APIs can still change between releases, so read the release notes before upgrading.
>
> **Documentation**:  a getting-started page, ten task guides (manage settings your way, build a cluster, run on Kubernetes, blocking, VLANs, encrypted DNS, safe changes, monitoring, sign-in, upgrades and backups), a configuration and Helm reference, and the OpenAPI document.
>
> **Verified live**: it runs my home network as one cluster, on a Raspberry Pi 4 and a k3s homelab with two resolver pods. About 58 MiB of RAM on the Pi with \~1.7M blocklist rules. Cache answers take \~25–50 µs inside the server, and the bench harness does roughly 500k cached queries/s on a 4-worker x86 VM.
>
> **AI** **Involvement**: Heavily AI-assisted. The spec, code, tests, and docs were written with Claude Code (Anthropic), working to my direction and review, from a written specification with requirement IDs traced through the code and tests. Every change goes through the test suite before it reaches my network. Commits carry a Co-Authored-By: Claude trailer.

---

> **NewtonLawAbider**（2 分） · 2026-10-23T08:17:05+08:00　
> I love it. AI powerhouse and space heater all in one. How loud is it?

---

> **jeffyclassify**（0 分） · 2026-10-23T08:21:25+08:00　
> **Project Name**: lossy-git 👻
>
> **Repo/Website Link**: [https://github.com/nicobrenner/lossy-git](https://github.com/nicobrenner/lossy-git)
>
> **Description**: Version control where the storage medium is a neural network. You commit files into it and it tries to memorize them. You checkout and it reconstructs them from memory. Sometimes it remembers everything. Sometimes it doesn't. 850x storage expansion over the original file. By every conceivable metric, the worst version control system ever built
>
> A second neural network trains on the first one's mistakes and tries to fix them, like a spell-checker for a brain that can't quite remember your code
>
> **Deployment**: pip install torch numpy and run lgit init. No Docker needed, it's a single Python script. There's also an interactive web demo if you want to see it mangle files without installing anything: [https://nicobrenner.github.io/lossy-git/demo.html](https://nicobrenner.github.io/lossy-git/demo.html)
>
> **AI Involvement**: The project IS the AI. The neural network is the storage engine. I also used Claude to help build it
>
> I hope you have fun with this project that explores the concepts of AI, version control and transient/lossy storage 🤗 All feedback is welcome

---

> **vladgladi**（2 分） · 2026-10-23T08:37:01+08:00　
> **Project Name:** personal-coach-kit
>
> **Repo/Website Link:** https://github.com/devladpopov/personal-coach-kit (demo with a fictional profile: https://personal-coach-kit.pages.dev)
>
> **Description:** An AI personal trainer and nutritionist you run yourself. Since May I have trained with a program an LLM wrote for me, inside a small tracker I built around it. When a friend asked for the same thing, I set the whole kit up for them in one day, so I moved everything personal into data files and published it as a template.
>
> - `node coach.mjs init` asks ~25 questions: goal, stats, days and minutes, equipment, injuries, food dislikes, the store you actually shop at and a weekly budget.
> - `node coach.mjs generate` sends one prompt file plus your answers to the model you choose: Claude, OpenAI, Gemini, any OpenAI-compatible endpoint, or Ollama locally. The answer is validated (7 days, sets/reps/rest, menus, shopping list); if the model breaks the format, it gets the error list and one retry.
> - No API key? `node coach.mjs prompt`, paste it into any chat, then `node coach.mjs import answer.txt`.
> - The tracker: per-set reps and weight with "last time" hints, a rest timer that starts when you tick a set, interval timer for cardio, meal plan with a shopping checklist, weight chart and workout history.
>
> **Deployment:** Node 18+, zero npm dependencies, MIT. `node coach.mjs build` gives you a static site (HTML/JS/JSON, no backend), so any static host or a local folder works. Your log lives in the browser's localStorage with JSON export. The build only publishes your first name, never weight, injuries or diet, and `data/` is git-ignored. Optional Telegram bot, no dependencies, long polling, so no public IP needed: morning plan and menu, reminder before training, evening check-in, Saturday shopping list, Sunday weigh-in. Setup steps are in the README.
>
> **AI Involvement:** Heavy, and it is the point of the project. The program and meal plan are generated by an LLM, and most of the code was written with Claude Code. I designed the flow and the prompt's rules and have used the tracker myself since May.
>
> Not medical advice. I would love feedback on the prompt's safety rules.

---

> **anitamaxwynnn69**（1 分） · 2026-10-23T08:37:54+08:00　
> Not at all. It's in my walk in closet. I've to go thru my washroom to reach there. So the noise is very low in my bedroom. The heat gets a little annoying at times though ngl. Wasn't very fun in the summers, but it's pretty good now.

---

> **ConsiderationBig1668**（1 分） · 2026-10-23T09:48:42+08:00　
> **Project:** Stackdome
>
> **Website:** [https://stackdome.com/](https://stackdome.com/)
>
> **Repo:** [https://github.com/Stackdome/Stackdome](https://github.com/Stackdome/Stackdome)
>
> **Description:**
>
> Since Railway getting pwned is getting all the attention right now, I thought now is a good time to showcase what we've been building.
>
> Stackdome is a self hosted platform as a service. The idea is to have simplicity of platforms like Railway and Render, but with the ability to run everything on infrastructure you control.
>
> With Stackdome, you can deploy an application from GitHub, connect multiple services visually, add a managed database, create preview environments, and roll back the entire application if a release breaks.
>
> Features:
>
> * First class support for multi-service applications, shown on a canvas in the UI (inspired by Railway). You can edit, wire up, and create resources from the canvas.
> * First class support for multiple clusters. Stackdome acts as the hub and places workloads across clusters (hub and spoke).
> * Self hostable, from a small VPS to a large cluster.
> * Managed Postgres with WAL archiving, HA, backups, and PITR (CNPG underneath).
> * A release system for the whole stack. A release targets everything, and you can roll it back if something breaks.
> * Source to image, with an in cluster registry (Zot).
> * Disposable preview environments, which can also be multi-service.
> * Declarative apps via a Stackfile, deployed with the CLI.
>
> Basically, the idea is to package the tooling in the CNCF/cloud-native ecosystem into an opinionated platform, so that developers can get a well engineered platform without learning Kubernetes YAMLology or a dozen other projects from the CNCF landscape.
>
> **Deployment:**
>
> This is a self hosted platform. You can use this command to setup Stackdome on a bare linux server:
>
>     curl -fsSL https://get.stackdome.com/install.sh | sudo sh
>
> We wanted to make not only deployment within the platform easy, but of the platform too.
> So we've been experimenting with agentic onboarding.
>
> You can copy paste this prompt onto your agentic tool and it will take care of the rest:
>
>     Fetch https://agents.stackdome.com and follow the instructions
>
> It will do the necessary work to install the required agentic skill and our CLI, which the agent can use to do everything you can do with Stackdome, without the UI.
>
> You can choose to point it to a remote server you own (where it will install stackdome with the curl command shared above) or opt to use our [cloud](http://cloud.stackdome.com/) (No credit card required).
>
> The agent then examines if there exists a project in context, works out how its services fit together, prepares the deployment, waits for it to become healthy and returns the public URL.
> If something fails, it can inspect the build and application logs and help fix it.
>
> It is all documented here: [https://docs.stackdome.com/self-host/install](https://docs.stackdome.com/self-host/install)
>
> **AI involvement:**
> This kickstarted back in 2024 as a hobby project by my friend, who works with cloud native technologies and wanted to bring all that robust goodness and guardrails in an accessible manner to the general developers space. The whole core of the project is written without any AI involvement at all.
>
> I pitched in b/w whenever I could to help build the UI for the application and had used AI to build the frontend. I'm a full stack engineer but align myself mostly towards the backend, design and css work dont come easy to me. I had used claude design to create a design system and incorporated it across the product. Honestly, using AI has really accelerated our development to be able to put the whole of it together well.
>
> Do checkout this project, let us know what you think of it ! Any feedback would be appreciated.

---

> **Anonymislim**（1 分） · 2026-10-23T09:52:16+08:00　
> Marcan - self-hosted DMARC report processing (for multiple Domains / Customers)
>
> https://i.redd.it/m4dso8mxh4xh1.png
>
> [https://marcan.kaitiaki.tech](https://marcan.kaitiaki.tech)
> [https://github.com/mavgit1/marcan-dmarc](https://github.com/mavgit1/marcan-dmarc)
>
> I wanted a single binary container for this. Rust, web UI embedded, SQLite, nothing else to run. It fetches the aggregate reports from an IMAP mailbox (read-only), parses them, recomputes SPF/DKIM alignment itself and tries to separate forwarded mail and lists from real failures. Also does live DNS checks for SPF, DKIM, DMARC, MTA-STS, TLS-RPT, BIMI, and shows when a domain is ready to go from p=none to quarantine/reject.
>
> The other gap I saw: there is no simple self-hostable tool for one operator, or a small team, looking after domains for several clients. So there are clients as a grouping, a monthly email per client, and alerts. Both experimental.
>
> Aggregate reports only, no forensic. Microsoft 365 with password login doesn’t work.
>
> Security model: the app has no auth of its own, the reverse proxy decides who gets in. If the proxy is secure, the app is. I wouldn’t trust myself or an AI to write a 100% secure login, so I didn’t.
>
> docker run --rm -p 127.0.0.1:8080:8080 -v marcan-data:/data [ghcr.io/mavgit1/marcan:latest](http://ghcr.io/mavgit1/marcan:latest)
>
> Compose examples with caddy/authelia/oauth2-proxy in the docs.
>
> License: AGPL plus one condition. If you run it for clients you have to tell them it’s free software, or buy an operator license that removes that duty. For your own domains it’s just AGPL. No features behind payment. I might change it to pure AGPLv3 depending, I dislike the "open-core" model tough, thus the license decision above.
>
> 0.3.1, beta, one developer, 42 domains in my own instance. Large parts written with AI assistance, I review everything, fmt/clippy/tests/audit on every commit.

---

> **Anonymislim**（1 分） · 2026-10-23T09:55:18+08:00　
> the high percentage numbers u can see on some values are due to adding more and more domains over the course of testing it; thus earlier "timespans" had significantly less of certain traffic
>
> also some real discoveries allready:
> \- found one customer sending failing mail en masse from IOT device due to missconfiguraiton
> \- multiple config issues and a DKIM failure that someone caused after a DNS migraiton

---

> **YakoStarwolf**（6 分） · 2026-10-23T12:49:13+08:00　
> Hey everyone 👋
>
> We've just released **TutorLoom**, a learning management system you can run on your own servers. It's built for two kinds of teams: companies running onboarding and skills training, and colleges and training institutes teaching their students.
>
> **What it does**
>
> * **Batches with deadlines:** group learners with their own start and end dates, with reminders 15, 7 and 2 days before the deadline
> * **Course builder:** levels and chapters with videos, documents, tasks and quizzes, and steps that unlock in order
> * **Grading with feedback:** trainers score submissions out of 100, write feedback, and approve the work or send it back
> * **Progress tracking:** from a whole batch down to one learner, with export
> * **Bulk upload:** add trainers and learners from CSV or Excel
> * **Mobile app:** a Flutter learner app for Android and iOS
> * **Points and levels**, plus branded emails
>
> **Self-hosting**
>
>     git clone https://github.com/pacewisdomhq/TutorLoom.git && cd TutorLoom
>     docker compose up --build
>
> That brings up PostgreSQL, Redis, the API, a Celery worker and the web app. Learner data stays on your servers.
>
> **Stack:** Django 6 + DRF, React 19 + TypeScript, Flutter, PostgreSQL, Redis, Celery
>
> **Open core, upfront:** the Community edition is free under Apache 2.0, and you can use it commercially. We also sell an Enterprise edition, which adds:
>
> * a Super Admin console for multiple offices or campuses
> * timed assessments with a coding judge in 7 languages
> * certificates with public verification
> * coding interviews where candidates don't need an account
> * Google and Microsoft sign-in
> * audit logs
>
> Enterprise is how we fund the project.
>
> **Links**
>
> * 💻 GitHub: [https://github.com/pacewisdomhq/TutorLoom](https://github.com/pacewisdomhq/TutorLoom)
> * 🌐 Website and docs: [https://tutorloom.io](https://tutorloom.io/)
> * 🚀 Product Hunt: [https://www.producthunt.com/products/tutorloom?launch=tutorloom](https://www.producthunt.com/products/tutorloom?launch=tutorloom)
>
> I'd really value feedback from this community, especially on the setup experience and on what you'd need before running it for real. Happy to answer questions about the stack, backups or deployment. Issues and PRs are welcome too.

---

> **AndrewTheLadybugMan**（1 分） · 2026-10-23T13:30:45+08:00　
> **Project Name:**
>
> WPL7 - Self-hosted WordPress/PHP powerhouse
>
> https://i.redd.it/9ebt0hnxk5xh1.jpeg
>
> **Repo/Website Link:**
>
> [**https://github.com/andyfo/wpl7**](https://github.com/andyfo/wpl7)
>
> [**https://wpl7.com/**](https://wpl7.com/)
>
> **Description:**
>
> WPL7 is a free & open-source server app that turns your VPS into your own web hosting platform. Basically, you become your own web hosting company after running one installation command.
>
> The primary target is WordPress hosting, because I use WP a lot, but support for any PHP-based website is coming soon.
>
> What you get: a nice GUI, per-website Docker containers, PHP updates, backups, multi-server setup for geo-based hosting, email sending, database management, (S)FTP, SSH, web FTP, and security features including a firewall, rate limiting, blocking/unblocking, vulnerability alerts and malware scanning. For WordPress, you also get bulk plugin management, installation recipes, etc.
>
> You can import existing websites with a built-in migration plugin, or connect external websites to use features like automated backups, bulk management, vulnerability reporting and MCP.
>
> The coolest feature is by far the built-in MCP that lets you manage your servers and the whole website fleet with AI. Some examples of what you can ask it to do:
>
> * “Update all plugins with vulnerabilities. Back up and screenshot each affected website, run the updates, then recheck each website.”
> * “Create a landing page for this project on my website.”
> * “Create a new dev website with a web shop based on these requirements and Figma design.”
> * “Client X asks me to make these changes: … Implement what's clear, ask me about what's not clear, and pull context from our CRM if needed.”
>
> Especially with an additional AI tool that knows how to build websites properly, like WP Godmode, the power level is pretty insane.
>
> **Deployment:**
>
> Available now to self-host on your own VPS with one installation command. Websites run in individual Docker containers, and you manage everything through the web GUI or MCP.
>
> Install docs: [https://wpl7.com/docs/get-started/installation/](https://wpl7.com/docs/get-started/installation/)
>
> **AI Involvement:**
>
> I am building this with AI, using a multi-model review-based feedback loop. Plus my own 20+ years of experience as a “traditional” developer. 😄
>
> AI is also an optional part of using WPL7: connect Claude, Codex or ChatGPT through the built-in MCP to manage and build your website fleet.

---

> **Jackpison**（1 分） · 2026-10-23T13:38:57+08:00　
> I've been building **Homebase Hub**, a self-hosted start page and personal workspace, and it's now public under GPL-3.0.
>
> It's one site with one login. The pages are:
>
> * **Home**: a start page with rotating background photos
> * **Links**: bookmarks in tabs and categories, with icons saved on your server
> * **Info**: notes in boxes, or as one document with an outline
> * **Cards** and **Tasks**: a searchable table, and due dates with repeats and prices
> * **Tools**: 36 small utilities that run in the browser (images, PDFs, OCR, QR codes, and more)
>
> What I cared about:
>
> * **No database.** Data is in a folder on your hosting, closed to browsers. The data files are PHP files that answer 404 even on servers that ignore `.htaccess`.
> * **Encryption where you choose.** Tabs can be encrypted with a passphrase, and the keys are made in your browser.
> * **Updates you can undo.** Updates come from GitHub releases or a zip. Each is checked first, needs your password to apply, and can be rolled back.
>
> It needs PHP 8.3 or newer, and it runs on ordinary shared hosting (I've been testing on cPanel-style hosting).
>
> Honest caveats: the releases aren't signed, so the checksum only proves a download wasn't damaged. Some parts I've only tested on my own setup. Feedback on what breaks on your hosting would help a lot.
>
> Repo: [https://github.com/Jackpison/Homebase-Hub](https://github.com/Jackpison/Homebase-Hub)
> Website and guide (PDF): [https://jackpison.github.io/Homebase-Hub/](https://jackpison.github.io/Homebase-Hub/)
>
> Happy to answer questions, and I'd especially like to hear how it fits next to Homepage, Homarr or Dashy.
>
> https://i.redd.it/4t823pjdm5xh1.png

---

> **AivaStack**（1 分） · 2026-10-23T14:01:10+08:00　
> \*\*SignUnder: self-hostable C2PA signing, watermarking and verification for AI-generated images (Apache-2.0)\*\*
>
> [https://github.com/AivaStack/signunder](https://github.com/AivaStack/signunder)
>
> I opened the code on Tuesday. If you run an image generator (ComfyUI behind a site, a small SaaS, an internal tool), it puts Content Credentials on the output and lets anyone check later whether an image came from you.
>
> \`git clone\`, then \`make up\`, starts four containers: the .NET API, a Rust signer (c2pa-rs), a Python watermark worker and Postgres. It signs with a development key that is committed to the repo on purpose.
>
> What you get:
>
> \- a C2PA manifest saying the image was AI-generated
>
> \- an invisible TrustMark watermark, so the image can still be matched after a platform strips the metadata
>
> \- a PDQ fingerprint as a fallback
>
> \- a registry and a verify endpoint: upload an image and find out whether it's one of yours
>
> The limits:
>
> \- Dev-key output shows as "unrecognised" in Content Credentials viewers. Recognised signing needs your own key in a KMS or HSM and a certificate from a CA on the C2PA trust list; no code can supply that. The signer speaks Google Cloud KMS.
>
> \- The watermark survives recompression and resizing in our tests, but a 25% crop lost it on two of four photos. The fingerprint doesn't survive crops either.
>
> \- The worker loads a model: about 920 MB marking a 1920×1920 image, so give it 1–2 GB of RAM.
>
> \- Images only (JPEG, PNG, WebP).
>
> I'm the developer and there's a hosted version too. Most of the code was written with Claude Code; every design decision is in \`docs/adr/\`. How the pieces fit: [https://signunder.com/how-it-works/under-the-hood](https://signunder.com/how-it-works/under-the-hood)

---

> **vallic**（1 分） · 2026-10-23T14:27:51+08:00　
> https://i.redd.it/8ssn0cuxu5xh1.png
>
> **MorphGate - an SSH client for desktop (Linux, MacOS, Windows), Android and iOS (in review), with end-to-end encrypted sync you can self-host.**
>
> There is business companion service, but it's not required to use. You can use the app without any account. You can selfhost your own server - there is reference for sync server in the repo, and docs how you can self host - all links below
>
> **Features**
>
> 🏠 the sync server is open source (AGPL-3.0): one program and a SQLite file, with a Docker Compose example that puts Caddy in front
>
> 🔐 end-to-end encrypted: the server never sees a hostname, password or key, only your email, devices and team members
>
> 🆓 no plans or billing on your own server: teams, shared vaults, OIDC single sign-on and SCIM all work
>
> 🔑 every host key is pinned on first connect, and a changed key blocks the connection
>
> 🛡️ each host can get its own WireGuard or OpenVPN tunnel, inside the app: no TUN device, no routes, no root, and overlapping subnets are fine
>
> 🔌 AnyConnect, GlobalProtect and Fortinet through openconnect on Linux and macOS
>
> 🪜 jump host chains, each hop checked against its own host key
>
> 🔀 local, remote and SOCKS port forwarding, saved in the vault
>
> 📁 SFTP: a two-pane file browser with drag and drop
>
> 🗝️ keys in 1Password, Bitwarden, KeePassXC or any SSH agent, plus OpenSSH certificates
>
> 📥 import from \~/.ssh/config, PuTTY, a CSV (Termius' template) or Royal TS
>
> ☁️ hosts from AWS, Google Cloud, Azure, Hetzner Cloud, DigitalOcean, or a JSON feed you publish
>
> 👥 teams: shared vaults, fingerprint-checked members, key rotation when someone leaves
>
> 🪟 split panes with broadcast, snippets and tmux attach
>
> 🎞️ encrypted session logs you can replay or save as .cast
>
> 📜 an open protocol (OpenAPI spec), and vault-conform to test any sync server against it
>
> 🙈 no telemetry, analytics or crash reporting, and no account needed
>
> 💻 Linux, macOS, Windows and Android, with iOS next; the app is free and open source too (MPL-2.0)
>
> **Self-hosted limitation - even you can build it if you need it**
>
> ⚠️ not yet on the self-hosted server: two-step verification, sending email (you pass invite codes on yourself), SAML,  account page and rate limiting
>
> ⚠️ has no web UI
>
> **Q/A**
>
> **1. "why isn't the hosted one (morphgate.com) open?"** \- it's a separate implementation of the same open protocol. You can check a server with vault-conform, and moving between servers is documented.
>
> **2. "did AI being used at this project"** \- yes, used Claude and Claude design.
>
> **3. Why did you built it** \- I had bare version (written in Go) and been running in my homelab, decided to build it out fully as proper app
>
> **4. Is this promotion for business companion server** \- no. As stated in Github repo, you can support project by using one of our two services if you want to. The main app will always be free and open source regardless of the business service.
>
> **Links**
>
> 🐙 Source code (app MPL-2.0, server AGPL-3.0): [https://github.com/Vallic/MorphGate](https://github.com/Vallic/MorphGate)
>
> 📖 Self-hosting guide (Docker Compose with Caddy, SSO, SCIM, backups): [https://morphgate.com/docs/self-hosting](https://morphgate.com/docs/self-hosting)
>
> 🖥️ The reference sync server: [https://github.com/Vallic/MorphGate/tree/main/server](https://github.com/Vallic/MorphGate/tree/main/server)
>
> 📜 OpenAPI spec of the sync protocol: [https://github.com/Vallic/MorphGate/blob/main/spec/openapi.yaml](https://github.com/Vallic/MorphGate/blob/main/spec/openapi.yaml)
>
> 🔐 Sync and crypto spec: [https://github.com/Vallic/MorphGate/blob/main/docs/sync-crypto-spec.md](https://github.com/Vallic/MorphGate/blob/main/docs/sync-crypto-spec.md)

---

> **Cold-Conclusion-6511**（3 分） · 2026-10-23T15:13:02+08:00　
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

> **Alive-Breath7596**（0 分） · 2026-10-23T15:13:13+08:00　
> **Project Name:**  **Spile**
>
> **Repository:** [https://github.com/spilecms/spile](https://github.com/spilecms/spile)
>
> **Description:**
>
> Spile is an open-source, self-hosted headless CMS that brings blog publishing, product documentation, and newsletter management into a single platform with one dashboard and one API.
>
> Teams often rely on separate services for each content type, such as Ghost for blogs, GitBook for documentation, and Mailchimp for newsletters. Managing these tools separately adds operational complexity, increases costs, and spreads content across disconnected systems. Spile brings these workflows together in one deployable application that teams can host on their own infrastructure and fully control.
>
> **key Features**
>
> * **Rich content editing:** Block-based editor for creating and managing articles and documentation.
> * **Structured documentation:** Dedicated documentation projects with hierarchical page trees, code groups, callouts, and API reference blocks.
> * **Newsletter management:** Subscriber management and built-in newsletter sending.
> * **Full-text search:** Built-in content search with deep links to individual headings.
> * **Developer-friendly API:** REST API with an Open API specification, allowing teams to build their own frontends and integrate Spile into existing applications.
> * **Webhook integration:** HMAC-signed webhooks for secure event delivery and cache invalidation.
> * **Flexible media storage:** Support for local disk and S3-compatible object storage.
> * **Simple deployment:** A single Go binary with the dashboard embedded, backed by SQLite. No separate database server or Node.js runtime is required.
>
> **Deployment:**
>
> Spile is designed to be straightforward to self-host, with Docker Compose as the recommended deployment method.
>
> Docker Compose
>
>     git clone https://github.com/spilecms/spile.git
>     cd spile
>     docker compose up -d
>
> Docker
>
>     docker run -d \
>       --name spile \
>       -p 8080:8080 \
>       -v spile_data:/data \
>       -e APP_ENV=production \
>       -e SESSION_SECRET="$(openssl rand -base64 48)" \
>       ghcr.io/spilecms/spile:latest
>
> Standalone binaries are also available through the GitHub Releases page.
>
> For configuration details, API usage, and additional deployment instructions, see the [project README](https://github.com/spilecms/spile).
>
> **Ai Involvement:**
>
> I used AI tools as coding assistants for pair programming, exploring implementation approaches, and accelerating repetitive boilerplate. I remain responsible for the project's concept, architecture, technical decisions, and overall direction. AI assisted with development, but Spile's design and engineering direction are mine.

---

> **jamesgarside**（1 分） · 2026-10-23T16:48:59+08:00　
> **Project name:** Hangar
>
> **Repo / website:** [https://github.com/hangar-hub/hangar](https://github.com/hangar-hub/hangar) · [https://hangar.page](https://hangar.page) · demo: [https://demo.hangar.page](https://demo.hangar.page)
>
> https://i.redd.it/dca7exstj6xh1.png
>
> **Description:**
>
> A self-hosted hub for your models and datasets, compatible with the Hugging Face Hub API.
>
> I got fed up of every machine on my network downloading the same 20 GB of weights from huggingface.co, and of models I rely on changing or vanishing upstream. So Hangar pulls a model once, keeps it on your own disk, and serves it to whatever you already use:
>
> * Set `HF_ENDPOINT` and `huggingface_hub`, `transformers`, `datasets` and vLLM work unchanged
> * `ollama pull` and LM Studio straight from it
> * `git clone`
> * with git-lfs, with the upstream history and Commit SHAs kept, so anything pinned to a Commit still resolves
> * Pull just the quantisation, Config or Split you want instead of the whole repo
> * Upload your own models with `huggingface_hub` or `git push`
> * Web UI with a GGUF viewer and a Dataset Viewer
> * Feed an air-ga
> * pped install from another one
>
> One container with SQLite to get going, or replicas over Postgres and S3 if you want it bigger. There's a Helm chart, Compose examples, OIDC sign-in and OpenTelemetry.
>
>     docker run -d --name hangar -p 8080:8080 -v hangar:/var/lib/hangar \
>       -e HANGAR_SERVER_PUBLIC_URL=http://localhost:8080 \
>       ghcr.io/hangar-hub/hangar:1.3.0
>
> **Licence:** Elastic License 2.0, so source-available rather than open source. Free to self-host, including at work. The one thing you can't do is sell it as a hosted service.
>
> **AI involvement:** I wrote the spec and design, coding agents wrote most of the code, and every change goes through CI, including compatibility suites that run the real \`huggingface\_hub\`, git, Ollama and vLLM clients against it."
>
> Happy to answer anything, and keen to hear what's missing.

---

> **Wild_Half_5990**（0 分） · 2026-10-23T16:55:46+08:00　
> I actually came across your GitHub repo through ChatGPT before you posted it here on Reddit, and I thought I'd give it a try on my Debian box running on Proxmox. I'm really glad I did because I absolutely love it!
>
> Really impressive work, especially considering the amount of content, the offline audio, and all the privacy-focused features you've put into it. I particularly appreciate that it's self-hosted, runs locally, and doesn't rely on external services or subscriptions. That's exactly the kind of project that makes the self-hosting community so great.
>
> The fact that you built something genuinely useful for your family and decided to share it with the rest of us deserves a lot of credit. Thanks for giving back to the community, and keep up the great work!

---

> **Resident-Scheme9093**（-1 分） · 2026-10-23T16:58:24+08:00　
> I’m really glad Anzo is useful for you.

---

> **RepresentativeYam464**（0 分） · 2026-10-23T17:19:58+08:00　
> Project Name: Cinderpaw
>
> Repo/Website Link: [https://github.com/bloom500/cinderpaw](https://github.com/bloom500/cinderpaw) (site: [https://www.cinderpaw.dev](https://www.cinderpaw.dev/))
>
> Description: An open-source (Apache 2.0) AI agent that runs on your own computer and does real work: it reads and writes your files, uses a browser you can watch, makes documents, PDFs and spreadsheets, and can answer for you on Telegram, Discord, Slack or WhatsApp. It works with a local GGUF model through llama.cpp or with any cloud provider key.
>
> * What stays with you: with a local model, your conversations never leave your machine. With a cloud model, calls go straight to the provider you picked; no account, no server of mine in between. The runtime listens only on [127.0.0.1](http://127.0.0.1), behind a token. Memory is a local database with a Forget button on every fact. Before it posts anything, it shows you the exact text and waits for your yes.
> * Self-improvement (opt-in): turn on Dreams and, while you're away, it tests changes to its own setup and keeps only what measures better. Off by default, with a spend cap you set. I call it "the RSI agent" because that's where it's going; I'm measuring it with sealed experiments before I claim it works.
> * Telemetry, all of it: an install count once at the end of setup (version + OS + one optional word for where you heard about it, no ID; the box is ticked by default, untick it and nothing is sent). A daily usage summary that is off unless you turn it on (per model: provider, task counts and outcomes, error types, duration ranges, tokens, cost, tool calls, retries, fallbacks, thumbs up/down; never your messages, file names, links, keys or exact times; a random code that changes monthly; every summary is written to \~/.cinderpaw/telemetry-sent.jsonl before it leaves). Bug reports only when you press send. An update check at startup with its own off switch. Full text: [PROMISES.md](http://PROMISES.md), promise 4.
>
> Deployment:
>
> * Desktop app for Windows, macOS and Linux (.exe/.dmg/.deb/.rpm). Not code-signed yet, so SmartScreen and Gatekeeper warn on first run.
> * Headless / server: npm install -g cinderpaw-agent, then cinderpaw gateway start runs it as a background service with a local HTTP API. A systemd setup is described in docs/HEADLESS.md. On Linux you can also build it from source (install.sh --from-source).
> * One-command install: scripts/install.sh / install.ps1 in the repo. Installs into \~/.cinderpaw with no admin rights and checks the download's SHA-256.
> * No Docker image yet.
> * Docs: the README's Install section and docs/HEADLESS.md.
>
> AI Involvement: Almost all of the code is written by AI coding agents (mostly Claude Code) under my direction; I'm not a programmer by training. I design it, test everything by hand and decide what ships, and every change runs the test suite on Windows, macOS and Linux in CI. Solo, no investors.
>
> # What would you need to see before you'd let an agent like this run on your own box all day?

---

> **deepakprakash**（1 分） · 2026-10-23T18:12:03+08:00　
> Project Name: Mesopod
>
> Repo/Website Link: [https://mesopod.com/homelab/](https://mesopod.com/homelab/)
>
> Description:
>
> Mesopod is a control plane application that lets you run and manage self-hosted apps, on your own machine, without any technical background or knowledge. It's completely free for personal use.
>
> **With Mesopod:**
>
> * you can deploy any app from the catalog in virtually one-click
> * each deployed app gets:
>    * a unique url like **appname..mesopod.app** that is accessible **only within your network**. You can use tailscale or your own VPN setup to access it from outside
>    * a fully **valid SSL certificate** for the domain that is completely managed and renewed automatically
>    * ability to **restrict access** to only yourself or users you choose with Mesopod's auth (similar to Cloudflare access)
>    * **app health monitoring** that automatically restarts apps when unhealthy, degraded, etc; also view resource usage and logs in real time.
>    * **network isolation** from other apps by default; access to other apps can be enabled directly from the UI
>    * one-click **app updates**
> * selectively **mount directories** from your host and make it accessible to apps at deploy time (eg: media directory for Jellyfin or Plex)
> * app config directories that are directly accessible on your machine for backups, direct edits, etc
> * encrypted application secrets management
> * wireguard **VPN** support for apps that need it, such as transmission
>
> **Under the hood**
>
> * **a small Kubernetes cluster (k3s):** When you connect a machine, the installer creates a k3s cluster. You never need to touch it, and everything Mesopod creates is a plain Kubernetes object you can inspect with standard tooling. You need to be quite technical for this, though.
> * **the cluster connects to Mesopod:** A small agent, the outpost, running within the cluster dials out to us; nothing on your machine listens for us.
> * **Mesopod manages the server from there:** It tells the outpost which apps to run and how, keeps watch on their health, and sends the update when you click. The outpost keeps the apps running on its own whether or not it can reach us.
> * all storage, networking, traffic and app health monitoring are **local**: so none of those go through the platform and continue to operate even if platform is down: ie, it is designed to be as zero-trust as possible while offering a great user experience
>
> **Coming soon**
>
> * custom app deployments
> * application health alerting
> * fully automated application updates
> * app bundling
> * custom domains
>
> **Background**
>
> I've been self-hosting for four years now (thanks to many of you here!) and even though I'm as technical as they come, it has been quite challenging to have a clean setup, keep the apps updated and running. A few months ago, I visited a semi-technical relative who was very interested in running a media server and even though we tried, it was impossible for him to setup anything more than Jellyfin before being completely overwhelmed with the technical complexity.
>
> Following that, I wanted to build a platform that can hopefully bring self-hosting to everyone. Mesopod is the result of a lot work since then - there is a ridiculous amount of engineering that has gone into building it. I sincerely hope it can help bring the wonderful world of self-hosting to many more.
>
> All my apps have been running on it for more than a month and I would love to invite a few of you for a beta and feedback (signup at [https://mesopod.com/homelab/](https://mesopod.com/homelab/)).

---

> **GT1030_Swapper**（3 分） · 2026-10-23T20:53:53+08:00　
> **Project Name:** Job Application Tracker
>
> **Repo/Website Link:** [GitHub](https://github.com/waddington/job-application-tracker) · [Website](https://waddington.github.io/job-application-tracker/) · Apache-2.0
>
> **Description:**
>
> I'm job hunting as a software engineer, and I kept losing track of things. A recruiter pitches three roles on a call and then goes quiet, and I can't remember which CV I sent where. Spreadsheets got messy, and I didn't want my whole job search sitting in Huntr or Teal's cloud. So I built a tracker that runs locally.
>
> The main bits:
>
> * **Recruiters:** agencies, contacts, calls, and the roles they pitched, so you can decide on each one (apply / interested / pass)
> * **Applications:** Kanban board, interview rounds, offers side by side, notes, files and emails
> * **Next actions:** who you owe a reply, who owes you one, what's gone quiet
> * **Ghosting:** mark someone as ghosted, and see how long each recruiter usually takes to reply, so you can tell slow from gone
> * **Insights:** funnel Sankey, conversion per stage, and an A/B test of your CV versions (with a proper significance test, so 3 vs 1 doesn't fool you)
>
> Everything lives in a plain folder: SQLite, a JSONL export, Markdown notes and your files. If that folder is a git repo, the app commits snapshots as you go, so you get history and can push it to a private remote as a backup. No accounts, no telemetry.
>
> **Deployment:**
>
> Version 0.1.0, and I use it every day. No Docker image yet. It runs from source and serves on localhost. You need Python 3.12+ with uv, Node 22.12+ with pnpm (only to build the UI), and git. Works on Linux and macOS.
>
>     git clone https://github.com/waddington/job-application-tracker.git
>     cd job-application-tracker
>     uv sync
>     pnpm --dir frontend install && pnpm --dir frontend build
>     uv run python scripts/seed_demo.py /tmp/jat-demo   # optional demo data
>     uv run jat --data-dir /tmp/jat-demo serve          # http://127.0.0.1:8770
>
> There's an [install guide](https://github.com/waddington/job-application-tracker/blob/main/docs/guide/install.md) and a [user guide](https://github.com/waddington/job-application-tracker/tree/main/docs/guide). There's no auth, so don't expose it to the internet.
>
> **AI Involvement:**
>
> Heavily AI-assisted. I designed it and directed the work, and Claude Code wrote most of the code. Every change went through tests and an automated review before merging, and the git history shows this openly.
>
> Feedback and issues are very welcome, especially if you're job hunting too.

---

> **swarmagent**（1 分） · 2026-10-23T21:13:32+08:00　
> Swarm: self-hosted runner for AI agents (Apache 2.0)
>
> Disclosure: I work on it.
>
> Swarm runs AI agents on your own Linux box, and you drive it from the AI you already use (Claude Code, Codex, ChatGPT) over MCP: "fix the failing tests in my repo", "check my site every morning at 8", and so on. Each job works on its own git branch, nothing lands in your folder until you merge, and you can add schedules, a reviewer step, and per-folder containers that hold API keys as stand-ins.
>
> Self-hosting details:
>
> \- Ubuntu 24.04 x86\_64, one-line install, about a minute, no Docker needed (containers are optional)
>
> \- runs as services on [127.0.0.1](http://127.0.0.1) only, under its own system user
>
> \- models are NOT local: you bring a ChatGPT plan, a Claude plan (via Claude Code) or an API key (OpenAI, Anthropic, Google, OpenRouter, Fireworks)
>
> \- telemetry: one anonymous install ping when a new instance is first created (a one-way ID, nothing else); SWARM\_DISABLE\_MINT\_REPORT=1 turns it off. Details are in the README.
>
> We just benchmarked how far a tiny box goes: on a 1 GB, $6/month Google e2-micro, 100 agents at once finish in 23 s (was 42 s before we fixed our save locks), 150 in 51 s with no swap, and all 200 finish at full load:
>
> [https://swarmagent.dev/resources/benchmarks/e2-micro-200-agents/](https://swarmagent.dev/resources/benchmarks/e2-micro-200-agents/)
>
> Repo: [https://github.com/swarm-agent/swarm](https://github.com/swarm-agent/swarm)

---

> **VanillaOk4593**（1 分） · 2026-10-23T21:28:38+08:00　
> **Project Name**: AgenticOS
>
> **Repo/Website Link**: https://github.com/vstorm-co/agenticos (docs: https://vstorm-co.github.io/agenticos/)
>
> **Description:** An open-source (Apache 2.0) workspace a team runs on its own server to build and share AI agents. Since our entry on 7 October it reached 1.0 and then 1.6: a team and its agents now share one live project chat with the same files and instructions, MCP connections can hold calls for a person's approval (all of them, or every tool the server doesn't mark read-only), and agents can hand coding work to Claude Code or Codex in a sandbox. I maintain it at Vstorm and I'm looking for a few people to try it and tell me what's missing.
>
> **Deployment:** Docker Compose with PostgreSQL (pgvector). Models: your own through Ollama or vLLM, a hosted provider with your key, or each person's own ChatGPT plan. Install guide: [https://vstorm-co.github.io/agenticos/install/](https://vstorm-co.github.io/agenticos/install/)
>
> **AI Involvement:** Much of the code is written with AI coding agents (Claude Code, Codex). I design the architecture, review every change, and CI runs the tests, with a 100% coverage gate on the platform core.

---

> **MeYaj1111**（1 分） · 2026-10-23T21:50:17+08:00　
> Repo/Website: https://github.com/jammin1911/jcar
>
> Live demo (sample data, resets every morning): https://jcardemo.maiurro.ca
>
> jCar is a self-hosted web app for tracking vehicle fuel, service and expenses. I built it after nearly 12 years of tracking my and my wife's cars in a paid Android app (which will not be named) that became worse and worse over time, and moved my whole history over: 11 vehicles, 900+ fill-ups, nearly $50,000 in spending. Several friends who are long time users of the same paid app have imported their history and switched to jCar as well, and we've all been using it exclusively for months.
>
> It tracks fuel-ups, services, expenses and notes with optional photos, plus statistics, charts and predictions, a per-vehicle parts list for quick reference, and vehicle sharing by invite. Imports from aCar, Fuelio, Fuelly CSV, Drivvo, Spritmonitor, Motostat, Fuel Log and generic CSV, exports to CSV and full JSON. Auto Fill (optional, off by default) photographs a receipt or the pump and fills the record in for you, using any OpenAI compatible endpoint you configure, including local models.
>
> The UI is kind of intentionally done in a dated style: it mimics the app it replaces but also keeps touches to a minimum when entering records, and is built for page-load speed.
>
> I know there are some fantastic alternatives available, but after trying all of them I was not able to find one to replace my favorite features in the paid app I had been using.
>
> Deployment: one small Docker container with a SQLite database, everything in a single ./data folder, docker-compose example in the repo. Set ORIGIN in .env, docker compose up -d, sign in as admin (blank password) on first sign-in and it walks you through creating the admin account. MIT license.
>
> AI Disclosure: Every feature and decision by me. Most of the code was written by various AI coding tools working from my specs, with me reviewing, testing and fixing as it went.  On the hosted version (not linked here) I maintain the server infrastructure with zero AI usage and 20+ years of admin experience.
>
> Very open to feedback and suggestions.

---

> **MammothInterview1025**（-1 分） · 2026-10-23T23:47:07+08:00　
> **Project Name:** Atrium
>
> Repo & docs: [https://github.com/atriumchat/atrium](https://github.com/atriumchat/atrium)
> Website Link: [https://www.atriumcalls.app/en/?utm\_source=reddit](https://www.atriumcalls.app/en/?utm_source=reddit)
> ***Demo****:* [https://app.demo.atriumcalls.app](https://app.demo.atriumcalls.app) (no sign-up, wipes every night at 04:00 utc)
>
> **Description**:
>
> got banned from discord this week. not for anything i posted: i was recording a tutorial for atrium's "move from discord" feature, made a fresh test account, and it got banned for "fraud or abuse" before i'd done anything with it. which is roughly why atrium exists: it's what i've been building for my own friends so the place we talk every evening isn't someone else's account system.
>
> **fair question:** why another one, when there's already matrix, mumble, teamspeak, rocket.chat? because most of them are built by and for people who already self-host, and assume someone in the group is the it person. atrium is for regular people. one friend rents a cheap vps from inside the desktop app (ip and password, no terminal), everyone else clicks a link and lands in a layout they already know from discord. nothing new to learn. every group runs its own server and there's no central atrium service, so there's no shared database to leak and nobody who can ban your account or your server.
>
> https://i.redd.it/zwxtyk3jm8xh1.png
>
> **it's a private discord for one group:**
>
> \- text channels, voice rooms (each with its own chat), dms and group calls, screen share with audio, camera, push-to-talk, noise suppression (rnnoise)
>
> \- invite-only. sign-up is a nickname and a password, no email or phone
>
> \- move from discord: paste a server template link, get the same channels and categories. messages stay on discord
>
> \- desktop app for mac and windows, web client for everything else (works on phones, no native apps yet)
>
> \- fastapi + python-socketio + sqlite in one process, livekit as the sfu, caddy in front. about 120 mb of ram for the whole stack
>
> \- calls fall back to turn on 443 when udp is blocked on a network. nightly backups, one-command restore
>
> **not there yet:** native mobile apps, roles beyond admin, bots, e2ee.
>
> **Deployment**:
>
> **docker compose** with prebuilt images (ghcr.io), set up by one script on a fresh ubuntu/debian vps:
>
>     curl -fsSL https://github.com/atriumchat/atrium/releases/latest/download/install.sh | sh
>
> took **63 seconds** on a 1 gb vps when i ran it end to end today. no terminal? the desktop app does the same install with just the vps ip and root password and gives you a free dedyn.io name. the password isn't stored; after the install the app's ssh key is pinned to a small script that can only do status, update, backup and logs. install guide: https://github.com/atriumchat/atrium/blob/main/docs/install.md
>
> **AI Involvement:** a lot of the code was written with an ai coding assistant (claude). i decide what gets built, review the changes, and run it on our own server every day. the installer gets tested end to end on throwaway vpses.
>
> if you try it, tell me where it **got annoying**. the install is the part i'm still sanding down.

---

> **New_Mess_7522**（1 分） · 2026-10-24T00:17:41+08:00　
> **Project Name:** One
>
> **Repo/Website Link:** https://github.com/Donnadieu/one (MIT). Release: https://github.com/Donnadieu/one/releases/tag/v0.6.0
>
> **Description:**
> One is a personal AI assistant for Mac, made for people who have never opened a terminal. I built it for myself and a few friends who wanted what agents like Hermes can do but were never going to touch API keys or config files.
>
> You press one button and it walks you through setup out loud:
>
> - pick the AI you already pay for (ChatGPT, Claude or OpenRouter) and sign in
> - give the assistant a name
> - it builds its memory ("My Brain") as plain Markdown files on your Mac, with an optional copy to iCloud Drive
> - you choose what it can reach. It only touches the folders you give it.
>
> After that you just talk to it. It always asks a plain yes or no before anything involving money, sending, posting or deleting. Replies are formatted, some questions come with tap-to-answer choices, it can do tasks in your browser, and it remembers past conversations.
>
> Self-hosting angle: the assistant, its memory and its permissions all live on your own machine. Nothing runs on a server of mine, because I don't have one. To be clear, the model itself is whatever cloud provider you sign in with, so your prompts go to them.
>
> Not there yet: Gmail and Calendar connections, anything outside the Mac, and code signing.
>
> **Deployment:**
> It's a native Mac app, not a Docker image. Apple Silicon, macOS 14+. Download One.dmg from the GitHub release. It's an unsigned test build, so the first time you open it you need System Settings > Privacy & Security > Open Anyway. On first launch it installs its own private copy of its engine (Hermes Agent by Nous Research) in ~/Library/Application Support/One and doesn't change your shell files or any other install. The README covers setup and how it's built (one SwiftUI file plus a build script).
>
> **AI Involvement:**
> The app is an AI assistant, so it uses whatever model you connect. I also wrote a lot of the code with AI coding agents. I set the direction, test every build on my own Mac, and review what goes in. It's early and I'm one person, not a company.
>
> I'm looking for feedback and contributors, especially people who can help with signing/notarization or who have a non-technical relative willing to try setup and tell me where it gets confusing.

---

> **Key_Cap_8111**（3 分） · 2026-10-24T00:46:16+08:00　
> ***Project Name:*** *CreatorOS Studio*
>
> ***Repo/Website Link:*** *https://github.com/thePloggy/CreatorOS-Studio (Apache-2.0). 2-min demo: https://youtu.be/axHdAXHv3Kk*
>
> ***Description:*** *A* *self-hosted* *AI* *photo/video* *studio* *for* *your* *own* *NVIDIA* *GPU.* *Write* *a* *one-line* *brief* *and* *get* *photos,* *short* *clips* *with* *sound* *and* *an* *auto-edited* *reel.* *It* *also* *does* *25* *one-click* *camera* *moves* *and* *effects* *on* *any* *photo,* *re-shoots* *a* *clip* *from* *a* *new* *camera* *angle,* *makes* *a* *talking* *avatar* *from* *one* *photo* *and* *a* *voice,* *and* *has* *brush* *retouch* *on* *photo* *and* *video* *plus* *a* *timeline* *editor.* *I* *built* *it* *because* *I* *was* *tired* *of* *paying* *per* *render* *on* *hosted* *AI* *video* *apps* *and* *getting* *SFW* *prompts* *refused.* *Everything* *runs* *locally* *with* *open-weights* *models* *only* *(Wan,* *LTX-2.5,* *Krea* *2,* *FLUX.2* *Klein),* *driven* *through* *ComfyUI,* *with* *Ollama* *for* *the* *text* *steps.* *No* *cloud* *account,* *no* *credits.*
>
> *-* *Stack:* *Node* *(Fastify)* *+* *SQLite* *(node:sqlite),* *React* *front* *end,* *desktop* *and* *mobile* *web* *UI* *(EN/FR).*
>
> *-* *Library* *with* *review,* *folders,* *trash* *with* *restore,* *and* *full* *provenance* *for* *every* *render* *(recipe,* *seed,* *LoRAs,* *prompt).*
>
> *-* *Diagnostics* *page:* *GPU/VRAM,* *ComfyUI* *link* *watchdog,* *missing* *nodes* *and* *models* *per* *recipe.*
>
> \- *You* *can* *import* *your* *own* *ComfyUI* *workflows* *(API* *format)* *in* *Settings.*
>
> *-* *If* *you* *expose* *it:* *owner* *key* *for* *admin* *actions,* *per-visitor* *rate* *limits* *and* *queue* *cap,* *optional* *ntfy* *notifications.*
>
> ***Deployment:*** *No* *Docker* *image* *yet.* *It's* *a* *bare-metal* *install,* *because* *it* *drives* *a* *local* *ComfyUI* *on* *the* *GPU.* *git* *clone,* *then* *npm* *run* *setup (an* *interactive* *wizard* *that* *checks* *Node/ffmpeg/Python/NVIDIA,* *finds* *or* *installs* *ComfyUI,* *installs* *the* *node* *packs* *and* *downloads* *the* *models* *for* *the* *features* *you* *pick,* *asking* *before* *every* *write),* *then* *npm* *ci* *&&* *npm* *run* *build* *&&* *npm* *start.*
>
> *Configuration* *is* *through* *environment* *variables,* *documented* *in* *the* *README.* *It* *needs* *a* *beefy* *NVIDIA* *card:* *it* *was* *built* *on* *32* *GB, and* *video* *recipes are sized for it.*
>
> ***AI Involvement:*** *Heavy. Most of the code was written with Claude Code, with me directing, reviewing and testing. I use it every day for my own production. The images and videos it produces are AI-generated by design, with open-weights models running* *locally.*

---

> **WeakTrifle3475**（1 分） · 2026-10-24T00:57:59+08:00　
> https://i.redd.it/fpgt8yliz8xh1.jpeg
>
> Soundbox
>
> [https://github.com/HamSanders/soundbox](https://github.com/HamSanders/soundbox) (site and docs: [https://hamsanders.github.io/soundbox/](https://hamsanders.github.io/soundbox/))
>
> A self-hosted, local Suno / ElevenLabs alternative. It generates sound effects, music (instrumental or sung from lyrics) and speech, including voice cloning, from open-weight models on your own hardware. The problem it solves: every open audio model ships as its own research repo with its own Python stack, and you find out the licence last. Soundbox runs them all through audio.cpp, a single native C++ binary, so there's no Python to install or maintain, and it shows each model's licence and commercial terms before you download it.
>
> Features: one library for everything you generate (prompt, model and seed kept with every take), swap models from a dropdown, a multi-track studio, stem splitting, a local HTTP API, an MCP server so coding agents like Claude Code can use it, and optional OpenTelemetry export. Everything lives in \~/.soundbox: one SQLite file, a folder of WAVs and the model weights. No account, nothing uploaded, works offline once the weights are downloaded. MIT licensed.
>
> \*\*Deployment:\*\* Released and downloadable now: [https://github.com/HamSanders/soundbox/releases](https://github.com/HamSanders/soundbox/releases)
>
> \- Docker: \`docker compose up -d --build\` runs the server and web UI headless with the audio.cpp runtime inside. CPU by default; \`docker-compose.cuda.yml\` adds CUDA. Data and model weights are separate volumes. The CUDA image builds but I haven't tested it on a GPU host yet, so reports are welcome.
>
> \- It has no auth of its own. The compose file publishes it on [127.0.0.1](http://127.0.0.1) only. To reach it from elsewhere, put it behind your reverse proxy and set SOUNDBOX\_ALLOWED\_HOSTS.
>
> \- Also Windows and macOS installers, or run from source on Linux.
>
> \- Install docs, including the Docker section: [https://github.com/HamSanders/soundbox/blob/main/docs/INSTALL.md](https://github.com/HamSanders/soundbox/blob/main/docs/INSTALL.md)

---

> **Nice_Log5165**（3 分） · 2026-10-24T01:04:40+08:00　
> # I built a self-hosted 2D pixel-art "Bot Office" where 5 AI agents live, write code, run QA, and stream their thoughts to Discord
>
> [](https://www.reddit.com/r/selfhosted/?f=flair_name%3A%22Chat%20System%22)
>
> I wanted more than a basic chat window for multi-agent workflows, so I built a self-hosted 2D pixel-art office where 5 specialized AI agents run a software studio together.
>
> **Meet the Staff:**
>
> * **Nash (Team Lead):** Coordinates tasks and delegates work across the team.
> * **Otto & Lucas (Devs):** Handle backend tasks, pull live APIs, and keep deployments clean.
> * **Diago (Build Engineer):** Polishes HTML/CSS and manages build pipelines.
> * **Mateus (QA Reviewer):** Spins up headless Chromium to test mobile layouts and catches bugs.
>
> They even stream their live work, office conversations, and inner thoughts straight into Discord webhooks.
>
> Come check out the office and see how they run things: [**https://discord.gg/bcrP2J8A**](https://discord.gg/bcrP2J8A)
>
> **Please come give me ideas!!!!!**
>
> https://i.redd.it/vnyv522q09xh1.png

---

> **Nice_Log5165**（2 分） · 2026-10-24T01:06:01+08:00　
> Hiya, AI was used a lot in this one, and it’s an AI project at its core. I came up with the idea and the design and I make the decisions, but most of the code was written by Claude (Anthropic’s AI) while I directed it and tested everything on my own Proxmox server. The “bots” in the office are real Claude Code sessions doing tasks in their own workspaces. Their chats and daily plans are generated by Google Gemini’s free tier. The pixel art is not AI: it’s LimeZu’s paid Modern Interiors, Office and Exteriors packs from [itch.io](http://itch.io/), used under their license. It all runs locally in an LXC container, and nothing is exposed to the internet.

---

> **Silver-Barracuda-621**（1 分） · 2026-10-24T01:53:10+08:00　
> I’ve spent a while working in product/application security, and one thing always bugged me: most supply-chain tools scan dependencies *after* `npm install` or `pip install` has already run — by which point the install scripts have executed. The decision happens too late.
>
> So I built **DepGate**, an open-source dependency gateway. It’s a single proxy + policy engine that sits in front of npm, PyPI, Maven, Go modules, NuGet, Cargo, Composer and RubyGems. Your devs and CI point their package managers at DepGate instead of the public registry. It fetches the package, checks it against a malware feed and your policies, and either serves it or returns a 403 naming the exact policy and reason.
>
> What it does:
>
> * **Known malware never downloads** — every request is checked against a synced feed of 200k+ malicious packages before any policy runs.
> * **Readable policies** — block by CVSS/EPSS, license, release age, release type, OpenSSF Scorecard, or package name. One rule per policy, stated in a sentence.
> * **Monitor mode** — run a new policy against real traffic first and see exactly what it would break before you enforce it.
> * **Dependency-confusion protection** — internal names are served only from internal registries, never a public look-alike.
> * **Decision Ledger** — every block is recorded with the reason and who asked, down to the CI job.
> * **Self-hosted, one Docker image** (Postgres + Redis), runs air-gapped, and can sit in front of or behind Artifactory/Nexus.
>
> It’s basically meant to be the open-source answer to the commercial “repository firewall” products, with a lot fewer moving parts. TypeScript end to end, MIT licensed.
>
> Repo (quick start + docs): [https://github.com/secmods/depgate](https://github.com/secmods/depgate)
>
> Still early and I’m actively building — would genuinely appreciate feedback, criticism of the approach, or feature requests. Heuristic detection of never-before-seen malware is on the roadmap. Happy to answer anything in the comments.
>
> https://i.redd.it/7cce5ipd99xh1.png

---

> **Real_Source_7528**（1 分） · 2026-10-24T02:53:27+08:00　
> Project Name: Gatearr — an Emby/Jellyfin account portal (v0.4.0 public beta)
>
> Repo / screenshots / setup: [https://github.com/HeklaLab/gatearr](https://github.com/HeklaLab/gatearr)
>
> Description:
>
> I’m building Gatearr because sharing a media server with family and friends also means resetting passwords, repeating permission changes and explaining how to connect each device. The aim is to give users one front door while keeping account management in the administrator’s control.
>
> Gatearr is free and open source (MIT). Users sign in with their existing Emby/Jellyfin account, manage their account, reset a forgotten password by email and follow device connection guides. Admins can manage groups, supported native permissions and library access, with a review of differences before adding members.
>
> The portal has a visual builder, three light/dark theme presets, optional Seerr request/quota widgets, Tracearr viewing statistics and personal library updates. v0.4.0 also adds a multilingual installer and locally bundled Cap CAPTCHA for sign-in/recovery; no cloud CAPTCHA account is needed.
>
> Deployment:
>
> One Gatearr application container, SQLite and persistent /data, with Docker images for AMD64/ARM64 and a Compose package. An existing Emby/Jellyfin server is required; SMTP enables invitations/recovery, and the other integrations are optional. Use your existing HTTPS reverse proxy for public access.
>
> Release: [https://github.com/HeklaLab/gatearr/releases/tag/v0.4.0](https://github.com/HeklaLab/gatearr/releases/tag/v0.4.0)
>
> AI Involvement:
>
> Substantial: Codex has been used for implementation, tests and UI iteration, under my requirements and hands-on demo testing. Automated tests and Docker CI are in place, but they are not an independent security audit. This is an early beta; back up data and test permission changes with a limited account.
>
> I’d particularly value feedback on the installation experience and group/permission workflow from people managing multiple media users. What would make this useful in your setup?

---

> **Sea-Regular-2316**（1 分） · 2026-10-24T02:54:01+08:00　
> * **Project Name:** Heirloom Gallery – Private Media Archive
> * **Repo/Website Link:** [https://wordpress.org/plugins/heirloom-gallery/](https://wordpress.org/plugins/heirloom-gallery/)
> * **Description:** Heirloom Gallery is a self-hosted WordPress plugin for organizing, preserving, and sharing your photo collections with complete privacy. Your photos stay on your server. No cloud uploads, no data collection, no tracking.
> * **Deployment:** v1.0.0 released recently after months of development. Wordpress users can download the plugin or find "Heirloom Gallery" in the plugins repository. Documentation available at [https://wpheirloom.com/gallery/docs/](https://wpheirloom.com/gallery/docs/)
> * **AI Involvement:** Copilot assistance in architecture and organization decisions
>
> This plugin was specifically designed for galleries to be managed with multiple users collaborating in an easy to use way. Turn boxes of old photos into a collaborative gallery you control on your own server!
>
> **\*\* Wordpress users \*\***
> I'd love to hear any feedback you may have. Come to the [plugin website](https://wpheirloom.com/) for more info and drop me a line if you have questions.
>
> https://i.redd.it/64vag8aij9xh1.png

---

> **Accra101**（2 分） · 2026-10-24T03:18:07+08:00　
> https://i.redd.it/qtiigntun9xh1.png
>
> * Project Name: RasBeacon (update: v0.2.0)
> * Repo/Website Link: [https://github.com/aazam476/RasBeacon](https://github.com/aazam476/RasBeacon)
> * Description:
>
> Last week, I posted RasBeacon, a travel router OS for the Raspberry Pi: it runs its own hotspot and connects to Wi-Fi (even ones on WPA-Enterprise) or Ethernet for you. v0.2.0 is out. It’s mostly security fixes and bug fixes, plus a bunch of extra features. Full release notes are on the release page; here are the highlights.
>
> Security (from a review of v0.1.0, each fix now has a test):
>
> * Logins sent all at once could get around the password-guessing limit.
> * RasBeacon now only answers under its own names, so a web page can’t reach the settings through DNS rebinding.
> * A hotel network could get code to run in RasBeacon’s page through its login page’s address.
> * Plugin passwords stay out of logs and the diagnostics report.
> * Plugins can no longer reach each other.
> * A plugin can’t take over another plugin’s image.
> * The clock is never set from plain HTTP a hotel network could fake.
>
> What’s new:
>
> * WPA-Enterprise networks no longer need the CA certificate or server name: RasBeacon trusts the login server on the first connection and refuses a different one later, like your phone does. The certificate fields are still there under Advanced.
> * WPA3-only hotspot, an allow list of devices that may join, and a limit on how many can join at once.
> * The channel list only shows channels your country allows.
> * DNS servers are used in the order you type them.
> * The kill switch now really cuts the internet while the VPN is off. VPN profiles can be renamed.
> * The data limit works without a metered connection.
> * Rename RasBeacon (it answers at `<name>.lan`), shut it down from the UI, and change the admin password.
> * Scheduled update checks, with notifications to ntfy.
> * If you’re a few versions behind, it offers the newest update you can install, one step at a time.
> * Backups can keep just your settings, your plugins’ data, or everything (so a restore works offline), and they’re smaller (zstd).
> * Generated HTTPS certificates last 820 days, because iPhones and Macs refuse longer ones. Expect your browser to ask about the certificate again once.
>
> Fixes include:
>
> * a self-check that repairs the hotspot when it drops out of its network bridge;
> * saving the guest network no longer restarts your plugins;
> * large backups and uploads no longer get cut off after 30 minutes;
> * plugin pages no longer freeze;
> * plenty of smaller ones.
>
> \---
>
> * Deployment: If you are new to RasBeacon, download and flash the latest release to your Pi’s SD card and boot. Updating from v0.1.0 needs one extra step. v0.1.0 installs the update file, but can't restart into it: its restart command fails on the systemd in current Raspberry Pi OS, so the page keeps saying "restarting". To finish, either:
>    * turn on SSH (SSH page), log in as \`root\` and run \`systemctl reboot --reboot-argument="0 tryboot"\`. RasBeacon restarts into v0.2.0, and keeps it after a minute of running normally;
>    * or back up your settings, flash the v0.2.0 image and restore the backup.
> * AI Involvement: Same as before: I'm in my third year of undergrad in computer science, and I used AI extensively to build this. I'm upfront about that because I think AI-assisted development is where software is heading, and I wanted a project that would teach me to do it well, so I can work fast and still trust what I ship. To me, the difference between vibe coding and real coding comes down to understanding your work and being proud of it, whether or not AI helped write it. I firmly believe RasBeacon fits those two criteria.

---

> **giga_pingu**（1 分） · 2026-10-24T03:32:53+08:00　
> # Sammlarr: a beefed-up version of the Import Lists
>
> For the past few months, I've have been working on a side project of mine, Sammlarr:
>
> [https://github.com/daerup/Sammlarr](https://github.com/daerup/Sammlarr)
>
> In short, Sammlarr is a beefed-up version of the Import Lists already in Sonarr and Radarr, with finer control. Each list gets its own filters, sorting, schedule and limit, taking the top N titles or N at random. A preview shows what it would add, ratings from different sources are combined into one, and titles that drop off the list can be removed automatically.
>
> Currently the Lists can either be added to the Arrs directly, or to a Plex watchlist.
>
> I started working on sammlarr because the people I am sharing my Plex library with were complaining about, how nothing new gets added to the server, while in turn no one was requesting stuff, you know how it is. With sammlarr I want to create a steady (moderate) stream of new media, while also removing previously added ones as to not bloat my library.
>
> AI Disclaimer:
> Throughout development I used AI, specifically Claude Code. I work as a Software Engineer myself  though, so if there are any whack design decisions, that’s most probably on me :)
>
> Please give it a shot and let me know if there is something you are currently missing or if you are encountering issues :)
>
> https://i.redd.it/nwjq0ht6r9xh1.png

---

> **Many-Chemist-4056**（1 分） · 2026-10-24T03:42:54+08:00　
> After a few years of self-hosting across several boxes, I kept losing track of what runs where, which stack talks to which database, and whether last night's backup actually ran. My "documentation" was always out of date, so I built something that reads it from the servers themselves, and I've made it \*\*open source (MIT)\*\*.
>
> **ServChart** draws a live, zoomable map of all your Docker hosts: hosts → Compose stacks (and the folder they live in) → containers, networks and published ports.
>
> \- **Lines come from real traffic**, not config files. The agent sees which containers actually connect to each other, on the same host and across hosts. Point at a container to see what it calls (blue) and what calls it (green).
>
> \- **Health at a glance:** CPU, RAM and disk per server, per-container resources, backup status (works with any backup tool via a tiny status file), certificate expiry and newer image versions.
>
> \- **A printable report** with findings (full disks, failed backups, expiring certs, outdated images) and CSV exports.
>
> How it works: one small agent per host (Python standard library only, \~13 MB RAM, \~0% CPU on my servers) reads the Docker API and **pushes outbound** to the hub every 60 s, so there are no ports to open and it works behind NAT and on cloud VMs. The hub is Django + React in a single container, SQLite by default.
>
> Security, since it touches the Docker socket: the agent only sends GET requests, never reads environment variables or container commands, redacts secret-looking labels, and the hub re-checks every report against an allow-list. Traffic observation and log viewing are opt-in. You can put a read-only socket proxy in front if you prefer.
>
> It's early (v0.4) but I run it daily on 6 servers. It isn't a container manager: it sits alongside Portainer/Dockge, Homepage, Beszel etc. and answers "what is connected to what, and is it healthy?"
>
> Try it with fictional demo data in two minutes: set \`SERVCHART\_DEMO: "1"\` in the compose file.
>
> **GitHub**: [https://github.com/opticodev/servchart](https://github.com/opticodev/servchart)
>
> **I'd really appreciate your feedback**. What's missing, what's confusing, what would make this useful for your setup? I'm especially interested in setups I can't test myself: Unraid, Synology, TrueNAS, Podman, Raspberry Pi/ARM. Bug reports, "the map looks wrong here" screenshots (with the demo data or your names blurred) and ideas are all welcome as \[issues\](https://github.com/opticodev/servchart/issues) or in \[Discussions\](https://github.com/opticodev/servchart/discussions).
>
> https://i.redd.it/iqh5epyxs9xh1.png
>
> **Contributions are very welcome too**, from docs and install guides for your platform to code. There are some \[good first issues\](https://github.com/opticodev/servchart/labels/good%20first%20issue) to start with, and \[CONTRIBUTING.md\](https://github.com/opticodev/servchart/blob/main/CONTRIBUTING.md) explains the setup and the few safety rules (the agent stays read-only and dependency-free). Stars help others find it, but honest feedback helps more. Thanks!

---

> **Frosty-Concern-297**（1 分） · 2026-10-24T04:16:34+08:00　
> i built warden, an open source self-hosted auth service in go with jwt, mfa and service-to-service authentication. it also comes with a typescript sdk for web, react native and node.js.
>
> feel free to try it if you need something like this. any feedback is appreciated :)
>
> warden: [https://github.com/fatihacan1/Warden](https://github.com/fatihacan1/Warden)
>
> typescript sdk: [https://github.com/fatihacan1/warden-js](https://github.com/fatihacan1/warden-js)

---

> **RammerOfProgs**（2 分） · 2026-10-24T04:27:54+08:00　
> # I built pmmux (port map multiplexer) to shove my homelab services through a single mapped port
>
> pmmux has been out there for a while, but I haven’t really talked about it publicly.
>
> It started as a simple port-mapping utility. Then I wanted to shove a bunch of different services through the single mapped port I had from my VPN provider, so it grew into a protocol-aware multiplexer and reverse proxy. But it also works as a pluggable reverse proxy without using port mapping at all.
>
> I’ve been running several instances as the primary front-ends for homelab services for nearly a year, and it’s been really solid so far.
>
> It can:
>
> * Route connections sharing a listening port to different backends based on the traffic, with support for TCP and UDP.
> * Change backends, listeners, and port mappings while it’s running through the management API or optional web UI, without restarting to reload a config.
> * Add protocols, routing strategies, and other functionality through plugins. HTTP proxying, TLS, and certificate automation are extensions too.
> * Run standalone, as a Windows service, or as a systemd service.
>
> This may be a little niche, and there are more established tools that do some, but not all, of what pmmux does. But I’m really proud of it, so if anyone wants to check it out, I’d love to hear what you think.
>
> [GitHub](https://github.com/lennykean/pmmux)
>
> AI disclosure: Mostly meat-coded, but I had a lot of help from AI on things like documentation and reviewing my code and some of the plugins.

---

> **skaldanalytics**（1 分） · 2026-10-24T05:00:41+08:00　
> **Project Name:** Skald
>
> **Repo/Website Link:** https://github.com/spcaeo/skald (site: https://skaldanalytics.com, live demo: https://spcaeo.github.io/skald)
>
> **Description:** Web analytics built from the access log your nginx, Apache or Caddy server already writes, so there's no JavaScript tag and no cookie banner. Every request gets sorted into people, AI assistants (ChatGPT-User, Claude, Perplexity fetching a page live), AI training crawlers, search bots and scanners. Fake GPTBot/Googlebot hits are checked against the published IP ranges. Because it reads the log, it also counts visitors with ad blockers or JS off, and it shows the ChatGPT referrals that GA4 lumped into "Direct" when ChatGPT links lost their UTM tag in mid-October. There's also a scanner view: on Oct 21 one probe made 150 requests in 14 seconds hunting AI API keys and .env files (write-up: https://skaldanalytics.com/security/ai-key-thief/).
>
> **Deployment:** One `docker run` with your log directory mounted read-only, or plain Python (standard library only, data in SQLite). Install docs: https://skaldanalytics.com/install/ and in the README.
>
> **License:** Elastic License 2.0, so it's source-available and free to self-host, but not OSI open source. Wanted to say that up front.
>
> **AI Involvement:** Built with a lot of AI coding assistance. I review and test what ships, and the numbers in the write-up come straight from a real server log.
>
> Happy to answer questions or take feature requests.

---

> **devilsdiligence**（1 分） · 2026-10-24T06:43:58+08:00　
> # Two free GLPI plugins: Markdown editor + global search (works on 10, 11 and 12)
>
> We run all our team docs out of the GLPI KB, so I built the two things I always wanted:
>
> **Minimal Effort Markdown**: a Markdown toggle on every editor (KB, tickets, followups, tasks, solutions). It does GFM tables and code blocks, Obsidian/GitHub callouts, and copy buttons on code blocks. It keeps your original markdown when you reopen something. Zero external requests, so it's fine for air-gapped setups. It's a fork of hellrazorx64's plugin, heavily rewritten.
> https://github.com/mebessusn/glpi-memarkdown
>
> **Global Search**: one search bar across tickets, problems, changes (including followups and tasks) and the KB, with highlighted snippets. It respects GLPI permissions, so users only see what they could already open.
> https://github.com/mebessusn/glpi-globalsearch
>
> Tested on 10.0.28, 11.0.11 and 12.0.0. Bug reports and ideas welcome.

---

> **Vast-Signal8965**（1 分） · 2026-10-24T07:24:17+08:00　
> **Project Name:** Money
>
> **Repo/Website Link:** [https://github.com/Muffy0906/firefly-money](https://github.com/Muffy0906/firefly-money)
>
> Live demo (runs in your browser with made-up data): [https://muffy0906.github.io/firefly-money/](https://muffy0906.github.io/firefly-money/)
>
> https://i.redd.it/gfu8lw57jbxh1.png
>
> **Description:** A fast, phone-friendly web frontend for [Firefly III](https://www.firefly-iii.org/). I love Firefly as a finance engine but wanted something quicker for everyday use, especially on my phone. Money runs next to your Firefly server and uses its API, so nothing in Firefly changes and you can stop using it any time.
>
> * Customizable Overview: net worth over time, spending insights, budgets with pace, and safe to spend until payday
> * Quick add in plain words (`coffee 5.40 amex yesterday`), refunds that come off spending, and payee totals with logos
> * Subscription finder, forecast with what-ifs, savings goal pace and a loan payoff planner
> * Phone-first PWA that also uses the full screen on desktop, with 11 themes
>
> **Deployment:** One Docker image, [`ghcr.io/muffy0906/firefly-money`](http://ghcr.io/muffy0906/firefly-money) (amd64 and arm64), with a docker-compose example and an `.env` in the README. It’s also in the TrueNAS community catalog, and there’s an Unraid template. You give it your Firefly URL and a Personal Access Token. The token stays in the container and never reaches the browser.
>
> **AI Involvement:** Built with heavy AI assistance (Claude). I directed, reviewed and tested it against my own Firefly server, and the README says this too. It’s MIT, so please read the code and report anything that looks off.

---

> **Fit_Put8562**（1 分） · 2026-10-24T09:14:34+08:00　
> Slow and Steady/side project which does reading actsactswhile I sleep
>
> My 2011 laptop shuts down cleanly — which is the trap, because a clean shutdown looks deliberate. The logs said actsOktoberfestOktoberfest critical / HARDWARE PROTECTION. The CPU was fine (41-45C); the drives were at 102-120C.
>
> So I moved the reading to a free cloud tier. Open-weight model on disk, no API key, no cloud. It reads everything overnight and leaves a two-line brief per item in the morning.
>
> Live demo: [https://92.5.41.244:8000/overnight/](https://92.5.41.244:8000/overnight/)
>
> Code: [https://github.com/Reggiebro/overnight](https://github.com/Reggiebro/overnight)
>
> Article: [https://dev.to/reggiebro/i-built-an-agent-that-reads-so-i-dont-have-t](https://dev.to/reggiebro/i-built-an-agent-that-reads-so-i-dont-have-t)
>
> Hacktoberfest Week 3 entry. Theme: Slow and Steady — build something that rewards laziness. This one does the reading while I'm asleep.

---

> **peppeg**（3 分） · 2026-10-24T11:59:17+08:00　
> Project Name: WatchSense
>
> Repo/Website Link: [https://github.com/peppeg/watchsense](https://github.com/peppeg/watchsense)
>
> https://i.redd.it/psr2xcyg9cxh1.jpeg
>
> Description: Every streaming service I use knows only a slice of me: Netflix knows my Netflix history, Prime knows my Prime history, Stremio knows the rest. So their suggestions stay inside their own catalog. WatchSense merges your viewing history from Netflix, Prime Video, Stremio and Trakt into one viewer identity: what you like, what you really love, what you dropped. It then asks an LLM for recommendations across platforms. The For you tab can filter them by genre. Give a series a 👍 and its page gets tailored picks: the LLM combines what's specific about that show with your whole profile, which works much better than the usual "you might also like". It's your data, too: you can export your whole cross-platform history (CSV) or your full viewer profile (JSON) anytime. The UI is in English and Italian.
>
> My impartial judge was my wife, who doesn't care about tech or AI at all: if she didn't lose patience, I was on the right track. Lately she's found a few series she'd never heard of and loved them, so maybe it wasn't all for nothing 😄
>
> Deployment: Docker Compose (single container, one SQLite file); docker-compose.yml and .env.example in the repo, or plain Node.js. You need a free TMDB API key and an OpenAI-compatible LLM endpoint, cloud or local (Ollama, LM Studio…). It works best with history from more than one source.
>
> AI Involvement: Built with heavy use of AI coding tools (Claude Code). I designed the features, made the product decisions, tested it daily on my own library and reviewed what went in.

---

> **derekleeth**（3 分） · 2026-10-24T12:03:47+08:00　
> Project Name: TerminalLynx
>
> Website: [https://terminallynx.com](https://terminallynx.com)
>
> Description:
>
> TerminalLynx is a desktop SSH client and connection manager for Windows, macOS and Linux. It syncs connections and credentials directly between your own devices, with no account and no cloud storage.
>
> Sync is device to device. To add a device, you enter a one-time pairing code shown on a device you already have. From then on, devices find each other automatically on the LAN, or connect by address over a mesh VPN such as Tailscale, ZeroTier or WireGuard. Each connection is encrypted end to end and authenticated by the devices' own keys, and every change is signed by the device that made it. A change usually reaches your other devices within a few seconds. Devices that were offline catch up when they reconnect. Edits made on two devices at once are merged field by field, so changing a host's port on one machine and its name on another keeps both changes. Changes also pass through other devices, so a laptop and a desktop that are never online at the same time still stay in sync. Networking is off until you enable it.
>
> Connections are organized with tags instead of folders. Tags can be key:value pairs (for example env:prod or role:db), you can group the list by any tag key, and saved searches can be pinned to the sidebar. A command palette (Ctrl+K) supports fuzzy search and filters such as env:prod -tag:legacy.
>
> The built-in client supports jump hosts, key and agent authentication, port forwarding, SFTP and host key verification. You can import from MobaXterm (folders become tags) and \~/.ssh/config, and export back to \~/.ssh/config or JSON.
>
> Deployment:
>
> It is a desktop application, so there is no server or Docker image. Installers for Windows, macOS (Apple Silicon and Intel) and Linux (AppImage, deb, rpm) are on the website, along with installation notes. Builds are not code-signed yet, so expect a SmartScreen or Gatekeeper warning on first launch.
>
> Licensing:
>
> TerminalLynx is closed source. Don’t hate. The idea for this came to me at work so I designed this to be used at the enterprise level but I was excited and actually surprised I actually got the P2P networking working as well as I did so I wanted to make the free version still useful at home. I hit my limit with MobaXterm on the free plan at home with just a small number of containers in Proxmox so I moved to Terminus at home but wanted something that had no cloud involved but also synced between my laptop and desktop. So I made the free tier for personal use and it includes 25 connections, 25 credentials and 3 synced devices which I’m hoping is enough for a home lab. If not, I’ll tweak it.
>
> AI Involvement:
>
> I designed the architecture and features. I personally went through the torture of deploying the infrastructure running the site, db, downloads (S3), and store front. Most of the implementation was written with Claude Opus 5.5, and I reviewed and tested what it produced. I am a 15+ year C# and later a Python backend programmer. I did this in Python several weeks ago and it sucked. I did it in Rust, and it was a game changer. But I suck at Rust and I needed massive help.
>
> It's been out for over 2 weeks but I think the post limit was 3 so I think I’m good there but didn’t want to make anything public until I tested the crap out of it at home and work.
>
> Feedback is welcome. Also, free testing is welcome.

---

> **lewis-barrett**（1 分） · 2026-10-24T13:32:16+08:00　
> Vistoda — open-source Home Assistant panel + per-vendor Rust apps for Ring Intercom, Blink and EZVIZ: live view, two-way audio, local recordings with NFS backup, credentials isolated per vendor app. Cloud-dependent by necessity (these vendors have no local API). MIT, AI-assisted (disclosed). https://github.com/luigibarretta/vistoda-home-assistant

---

> **glukase**（2 分） · 2026-10-24T13:57:11+08:00　
> Project: Prepperpoint
> Website/download and installation guide: [https://www.prepperpoint.se/](https://www.prepperpoint.se/)
>
> I am building a Debian-based offline household server, distributed as an image for a USB stick or external disk/SSD. Boot a compatible x86-64 PC and it automatically starts a Wi-Fi hotspot and shares its resources. The computer itself works as a terminal; phones and tablets use the portal through a browser. The goal is to avoid configuring each underlying service manually. Hotspot support depends on the Wi-Fi adapter.
>
> • Offline library: Wikipedia, WikiMed and other ZIM collections via Kiwix.
> • Offline maps: locally stored map material.
> • Supply inventory: food, water, barcode scanning and expiry dates.
> • Nutrition planning: calorie and nutrient calculations.
> • Local AI: optional models running on the PC.
> • Documents and media: your own PDFs, manuals and files.
> • Encrypted document vault: private documents stored locally.
> • Encryption tools: encrypt and decrypt messages.
> • Local message board: communication between connected users.
> • Offline cloning: copy the system to another suitable drive.
>
> Deployment: a complete bootable system image, rather than a Docker container. My reference hardware is an i5-6300U laptop with 8 GB RAM; this is a tested example, not a formal minimum. Content must be downloaded ahead of time and the server needs power. AI answers can be wrong; the library remains directly accessible without AI.
>
> Disclosure: I run the project. Codex, Claude and DeepSeek have been used extensively over about five months. Private use is free; the intended commercial model includes paid organisational use. There is no public source release I can point to yet, so I am not describing the image as open source.
>
> I would appreciate feedback on first boot, hotspot compatibility and whether this prepared environment is useful compared with assembling the services yourself.
>
> Demo video: [https://www.reddit.com/r/Kiwix/comments/1xcjss1/i\_built\_a\_complete\_offline\_preparedness\_server/](https://www.reddit.com/r/Kiwix/comments/1xcjss1/i_built_a_complete_offline_preparedness_server/)

---

> **Colo3D**（1 分） · 2026-10-24T16:05:50+08:00　
> https://i.redd.it/0km2ccqihdxh1.png
>
> **Project Name:** Scriptorium
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

> **PhantomDiata**（3 分） · 2026-10-24T19:06:00+08:00　
> https://i.redd.it/5u1jfswpeexh1.png
>
> **Project Name:** Parley
>
> **Repo/Website Link:** [https://github.com/Hankanman/Parley](https://github.com/Hankanman/Parley) · [https://meetparley.app](https://meetparley.app) (MIT)
>
> **Description:** A private meeting recorder for Linux. I wanted something like Otter or Granola that doesn’t upload my calls anywhere. Parley captures mic and system audio from PipeWire, so it works with Meet, Zoom, Teams or anything else, and no bot joins the call. It transcribes live with Whisper (CUDA, Vulkan or CPU) and labels speakers, recognising voices you’ve named before. It writes summaries, decisions and action items, and you can ask questions across all your meetings, with answers that cite the meeting and timestamp. The LLM is a built-in llama.cpp model, **your own Ollama server**, or any OpenAI-compatible endpoint. There’s no account and no telemetry. It’s a single native Rust app (GPUI and SQLite, no Electron), and it also ships an MCP server over your local meeting database.
>
> **Deployment:** It’s a desktop app, not a server. Install it with a one liner, which installs an AppImage without root, or download the AppImage from Releases. It needs x86\_64, glibc 2.39+ and PipeWire. Docs: [https://meetparley.app/docs/](https://meetparley.app/docs/)
>
> **AI Involvement:** I designed it and make the decisions, and I wrote much of the code with Claude Code. I review and test every change. The app itself runs AI models (Whisper, and an LLM for summaries), locally by default.

---

> **Alternative-Suit5541**（3 分） · 2026-10-24T22:30:35+08:00　
> Not sure if it fits here.. but yeah
>
> Headset and mice battery level indicator for windows.
>
> Wanted to get rid of synapse and steelseries software.
>
> A small battery level indicator for windows.
>
> https://github.com/Q-efx/peripheral-battery-tray

---

> **Aggressive-Swing-931**（1 分） · 2026-10-24T22:51:36+08:00　
> **Project Name:** Network Topology Scanner
>
> **Repo/Website Link:** https://github.com/danielsm107/network-topology-scanner (MIT)
>
> **Description:**
> Scans your LAN with nmap and draws a map of it. Most scanners give you a list of IPs or a star with everything hanging off "the network". If you give this one SNMP access (v2c or v3) to your router/switches, it reads their ARP, MAC and LLDP tables and draws the *real* tree instead: which host is on which switch port or AP, with the port names on both ends of each link. Without SNMP it falls back to the star.
>
> - Host discovery in two phases (ping scan, then a full scan of live hosts only), vendor from the MAC, and a device category (router, NAS, camera, printer, IoT…)
> - Flags risky open ports (Telnet, SMB, RDP, FTP, VNC)
> - Stores every scan in SQLite and diffs it against the previous one: new/missing hosts, ports that opened or closed
> - CSV export, an interactive HTML graph from the CLI, and a local web UI (Streamlit) with flat and isometric views ([GIF](https://raw.githubusercontent.com/danielsm107/network-topology-scanner/main/docs/screenshots/topologia.gif))
> - LLDP-MIB works with any vendor; I've tested it against my MikroTik
>
> Known limitations: the category is a keyword heuristic on the vendor name, MAC/vendor only works on your own L2 segment, and switches/APs all show up as "router" for now (telling them apart with LLDP capabilities is next).
>
> **Deployment:**
> Multi-arch Docker image (amd64/arm64) on GHCR. It runs nmap as a non-root user and only needs `NET_RAW` + `NET_ADMIN`, no `--privileged`:
> ```
>     docker run --rm --network host --cap-add NET_RAW --cap-add NET_ADMIN \
>         -v topology-data:/data ghcr.io/danielsm107/topology-scanner 192.168.1.0/24 --fast
> ```
> There's a [compose.yaml](https://github.com/danielsm107/network-topology-scanner/blob/main/compose.yaml) for the web UI. It only listens on 127.0.0.1 because the UI has no auth. Also on PyPI: `pip install "topology-scanner[web,snmp]"` (needs nmap). Install, usage, SNMP setup and Docker notes are in the README. `--network host` means Linux only; Docker Desktop can't reach your LAN at layer 2.
>
> **AI Involvement:**
> Built with heavy help from an AI coding assistant (Claude Code). I'm a junior sysadmin learning Python, and I used this project to learn. I decided the features and design, reviewed the changes, and tested it against my own network. Everything goes through tests (pytest, no real network needed) and CI with lint, a container build and a Trivy scan.
>
> Feedback welcome, especially if you have non-MikroTik gear to test LLDP against.

---

> **Adex77**（1 分） · 2026-10-24T22:56:45+08:00　
> https://i.redd.it/qs7hkexpifxh1.png
>
> **Project Name:** AsoBeast
>
> **Repo/Website Link:** [https://github.com/AsoBeast/asobeast](https://github.com/AsoBeast/asobeast) (AGPL-3.0), docs at [https://docs.asobeast.com](https://docs.asobeast.com/)
>
> **Description:** If you have an app on the App Store or Google Play, AsoBeast tracks where it ranks in store search for the keywords you pick. It checks once a day, down to position 200, in any country, and the same search records every competitor on that page. It keeps the history, plus listing changes, reviews and popularity and difficulty scores.
>
> I built it because the ASO tools I tried charged per app or per keyword, and I didn't like a vendor holding my keyword list. Here the store requests go out from your own server at a slow rate (15 a minute to Apple), the keywords stay in your own Postgres, there's no telemetry, and email, webhooks, OpenAI and Apple Ads stay off until you set them up. There's a hosted version too, but no open core, so self-hosting gets every feature.
>
> **Deployment:** Docker Compose with four containers: Postgres 18, Redis 8, the API and the web app. Images are on GHCR for amd64 and arm64. It needs about 2 GB of RAM, 5 GB of disk and two env vars:
>
>     curl -fsSLO https://raw.githubusercontent.com/AsoBeast/asobeast/main/docker-compose.pull.yml
>     printf 'POSTGRES_PASSWORD=%s\nAUTH_SECRET=%s\n' "$(openssl rand -hex 32)" "$(openssl rand -hex 32)" > .env
>     docker compose -f docker-compose.pull.yml up -d --wait
>
> Then open [http://localhost:3001](http://localhost:3001/) and create the owner account. Use Chrome or Firefox until it's behind TLS, because Safari drops the session cookie over plain HTTP.
>
> If you try it, I'd love to know where the setup got stuck, especially on arm64.

---

> **PuzzleheadedBreak871**（1 分） · 2026-10-25T00:40:31+08:00　
> https://i.redd.it/jhz6616g1gxh1.jpeg
>
> Project Name: PocketDev
>
> **Repo:** [https://github.com/sujan0629/pocket-dev](https://github.com/sujan0629/pocket-dev)
>
> **Description:**
>
> I started building this because I kept running into the same problem every day: needing to check or change something in a project from my phone, then having to get back to my computer anyway.
>
> PocketDev is a native mobile workspace that connects to your own computer or a self-hosted execution worker. You can browse and edit files, sync projects, use an interactive terminal, and review or commit changes through Git.
>
> It’s built with React Native/Expo, NestJS, PostgreSQL, and Redis/BullMQ. Terminal sessions stream over WebSockets.
>
> **Deployment:**
>
> It’s currently a self-hosted working prototype. You run the API and the relevant execution services yourself, with PostgreSQL and Redis. The included Docker Compose file starts the database and Redis; the remaining services run separately.
>
> The mobile app requires a custom development build. Screenshots, setup instructions, architecture details, and current limitations are in the README.
>
> **AI involvement:**
>
> AI assistance has been used for documentation and setup tooling, including preparing this write-up. The app also supports optional terminal-output explanations using an imported GGUF model on the phone. Command execution still uses your connected computer or worker.
>
> I’d appreciate feedback on the setup and mobile workflow, especially terminal controls, file editing, and Git. What would make this useful with your own setup?

---

> **DEMORALIZ3D**（2 分） · 2026-10-25T02:44:28+08:00　
> Project Name: Audio Hub
>
> Repo/Website Link: [https://github.com/DEMORALIZ3D/audiohub](https://github.com/DEMORALIZ3D/audiohub)
>
> Description: It's a sovereign, self-hosted, music streaming ecosystem and personal cloud audio server. High-fidelity streaming, multi-device synchronized handoff, real-time collaborative rooms, 3D vinyl visualizers, Apple-style Cover Flow crate digging, custom DSP audio engines, 100% offline QR sharing, and infinite hybrid catalog discovery. You can use your existing library or search and play directly from YouTube like a typical streaming experience.
>
> Deployment: full instructions in GitHub readme. Docker with docker-compose
>
> Al Involvement: Yes - Entirely, Google Gemini flash 3.8, Various skills and MCPs. Plus lots of manual intervention for things like code cleanup and guidance.
>
> looking for support via GH stars it's my first official "open source" project.
>
> https://i.redd.it/n3hcw48ongxh1.png

---

> **aerobeek**（1 分） · 2026-10-25T02:45:40+08:00　
> https://i.redd.it/w6cmblmnngxh1.png
>
> I got sick of **not being able to easily read the files my SES saves to my catchall s3 bucket** folder. So I created this FOSS terminal reader tool.
>
> It's super simple and works great for me, so I thought I'd share:
>
> [https://github.com/spdrman/reSES](https://github.com/spdrman/reSES)
>
> Press 'i' inside your folder that is your '"inbox", and it'll remember for next time you open reses. If you open an email file and want to see the html version of it in a browser (as I often do), just press 'h'. Press 'r' to refresh, or just 'q' and re-run the 'reses' command in your terminal.

---

> **vdubbin74**（2 分） · 2026-10-25T04:02:26+08:00　
> **Project Name:** WavWiz (0.4.9 Beta)
>
> **Repo/Website Link:**
> [https://github.com/vdubbin74/WavWiz](https://github.com/vdubbin74/WavWiz)
> [https://wavwiz.com](https://wavwiz.com)
>
> **Description:**
> Full disclosure: I'm the developer. I'm a hobbyist who builds his own speakers and runs an always-on Windows home server with my music on it. I wanted the speakers I already own around the house to play together without echoing, so I made WavWiz. It's free and MIT licensed, with nothing to buy.
>
> The server runs on the Windows PC and streams to every speaker against a shared clock, with drift correction (similar in spirit to Snapcast). Other Windows PCs run WavWiz Player. Phones, tablets and Macs open the server's page in a browser and play as a speaker, with no app to install.
>
> **What it does:**
> • Zones can play their own music, or link up to play the same thing. Each speaker sits in any zone.
> • A per-device delay (0–1000 ms) for Bluetooth and Wi-Fi lag, set by ear or measured with a PC microphone
> • A Master Volume mixer with every zone and speaker in one window
> • Jukebox mode (beta): guests scan a QR code and add songs from their phones, on the speakers you pick
> • Streaming at 24-bit/48 kHz, or 24-bit/96 kHz for players that support it
> • AirPlay and Spotify Connect receivers, so you can cast from your phone to one zone or to every zone. Spotify needs your own Premium; it's an unofficial client and off by default.
> • A phone page that works as a full-screen remote
> • Library from local folders or NAS shares, internet radio, and a 10-band EQ per speaker
> • No cloud account, no analytics, no telemetry, and it doesn't open ports to the internet. Album covers and artist photos are looked up online, and you can turn that off.
>
> **Deployment:**
> One installer for 64-bit Windows 10 (1809 or newer) or Windows 11. Install the Server on the always-on PC and the Player on PCs with speakers. Setup is covered in the README and docs/FIRST-RUN.md. There's no Docker image; the server is Windows-only. If your setup is Linux, Snapcast with Music Assistant is great.
>
> **AI Involvement:**
> AI coding agents wrote the code. I came up with the idea, wrote the spec, made the design decisions, and I test every build on my own setup at home. I'd rather say that plainly up front.
>
> **Beta notes:**
> • The installer isn't code-signed yet, so Windows SmartScreen will warn. The SHA-256 is on the release page.
> • Known issue: while the Jukebox runs, its speakers also show under Unassigned in Devices.
> • Smart-TV browsers and phone-mic calibration on iPhone are still in testing (use a PC mic).
>
> I'd appreciate feedback: does setup make sense, how does it sound on your network, and what would stop you from running it? Bugs go to GitHub Issues. I'll be around to answer questions.
>
> https://i.redd.it/zsi2q3gd0hxh1.jpeg

---

> **xconspirisist**（2 分） · 2026-10-25T08:10:00+08:00　
> https://i.redd.it/2me9z3pp8ixh1.png
>
> **Repo & Website:** [**https://github.com/jamesread/BiscuitTin**](https://github.com/jamesread/BiscuitTin)
>
> **Docs:** [**https://jamesread.github.io/BiscuitTin/**](https://jamesread.github.io/BiscuitTin/)
>
> **AI Involvement**: Vibe Coded (I declare "Level 4 out of 5" in the README). I'm a dev with 20 years experience.
>
> **Deployment:** Linux flatpak on the GitHub release
>
> BiscuitTin is a fullscreen launcher for desktop apps, like retroarch, jellyfin, or similar on media center PCs. It supports gamepads, keyboards, or remote control via your phone. I wanted this to be able to switch between steam big picture mode, retroarch and jellyfin on my media center PC.
>
> I wrote OliveTin (almost entirely by hand, over many years!) - which quite a few people in this community seem to use for running backgorund apps and scripts. I'm a developer with 20 years experience, but this evening I vibe coded BiscuitTin for my TV.
>
> Like OliveTin, it is entirely free, open source and no-nonsense. There's a discord server in the README if you'd like to get in contact. Thanks for your time!

---

> **Old-Conference-3730**（1 分） · 2026-10-25T11:56:30+08:00　
> \*\*Project Name:\*\* Ovis
>
> \*\*Repo/Website Link:\*\* https://github.com/devswha/ovis · https://ovis.sh/
>
> \*\*Description:\*\* Self-hosted browser and phone (PWA) client for herdr. Turns Claude Code / Codex (and other) agent panes into chat + live terminal, with approval cards, push alerts, worktrees, and SSH remotes. Keeps agents in herdr; no hosted relay required for the default path. Free/MIT. I’m the author.
>
> \*\*Deployment:\*\* \`curl -fsSL https://ovis.sh/install.sh | sh\` on Linux (glibc) or macOS. Needs herdr 0.9.0+ and Bun 1.4+. Docs in the repo and on ovis.sh; demo at https://ovis.sh/demo/. Not Alpine/musl.
>
> \*\*AI Involvement:\*\* The app is a UI for coding agents (Claude Code, Codex, etc.). Some implementation work used coding agents; I review and ship what goes out.

---

> **FineZombie4599**（1 分） · 2026-10-25T16:18:25+08:00　
> **Project Name:** MeshCentral Mobile (0.7.2, public preview)
>
> **Repo/Website Link:** https://github.com/papajon123/meshcentral-android
>
> **Description:** A native Android client for your own MeshCentral server. The MeshCentral web panel works in a mobile browser, but it is built for a desktop screen; this app is built for touch.
>
> - Remote desktop with touch and trackpad modes, keyboard, clipboard text and monitor switching
> - Terminal, files, SSH and SFTP through the server relays; two sessions at once
> - Share files from any Android app straight to a folder on a computer, verified by SHA-256
> - Up to 20 server profiles, favourites, search, app lock with PIN or biometrics
> - Works with a stock MeshCentral server; an optional server plugin adds allowlisted diagnostics jobs and polling notifications (no FCM)
> - Apache 2.0, no ads, analytics or telemetry; credentials stay in Android Keystore
>
> **Deployment:** Nothing new to host: it connects to the MeshCentral server you already run. Signed APK in GitHub Releases (Android 8+); the README covers setup, the optional plugin and known limitations. Obtainium works with the repo URL (enable pre-releases).
>
> **AI Involvement:** Substantial. Much of the code, tests and documentation was written with AI coding agents under my direction; I review the changes and release only after the unit, lint and emulator test suites (Android 8 and 15) pass. Translations are machine-produced, as the README says.
>
> Looking for testers with real phones and Windows agents; device reports are very welcome.

---

> **OppositePangolin8091**（1 分） · 2026-10-25T18:56:32+08:00　
> Server Dashboard - lightweight self-hosted dashboard
>
> https://i.redd.it/4x69eykvglxh1.png
>
> \- App tiles with server-side online/offline checks
>
> \- Live CPU / RAM / disk, Docker panel (start / stop / restart)
>
> \- Proxmox VE widget: host stats + all your VMs/LXCs, with a read-only API token
>
> \- Widgets: Jellyfin, Plex, qBittorrent, Sonarr, Radarr
>
> \- Install with Docker Compose, or without Docker in one command (systemd - great in a Proxmox LXC)
>
> Node.js + plain HTML/JS, no build step, no database. UI is in French for now (translations welcome).
>
> Transparency: built with a lot of help from an AI coding assistant (Claude Code). I review and test every change on my own Proxmox server, and the repo has CI that runs a real install and a Docker build on each push.
>
> Feedback and widget ideas welcome - there's a public roadmap and "good first issues".
>
> [https://github.com/Circule-studio/server-dashboard](https://github.com/Circule-studio/server-dashboard)

---

> **Everlier**（1 分） · 2026-10-25T20:16:44+08:00　
> Project name: TraceQuest. I'm the developer.
>
> Repo: [https://github.com/viktor-com/tracequest](https://github.com/viktor-com/tracequest) (MIT)
>
> Description: A local web app and CLI for searching and inspecting coding-agent sessions from Claude Code, Codex, Cursor, OpenCode and others. It shows messages, tool output, errors, retries, timing and token usage. The self-hosting use case is a read-only hub that copies sessions from multiple machines over SSH, so you can search your laptop and remote dev boxes in one place. Analysis runs locally with no model calls or telemetry.
>
> Deployment: Node.js 22.5+ and git. Clone the repo, run npm install, then npm run demo for bundled sample sessions or npm start for your own logs. The hub deployment guide in the repo covers SSH/rsync collection and configuration. The server defaults to localhost and has no built-in login, so put remote access behind an authenticating proxy or a private network.
>
> AI involvement: AI-assisted development. The session browser and failure analysis do not require an LLM. This comment was drafted with AI assistance.
>
> I'd appreciate feedback on hub setup and collecting sessions from several machines.

---

> **OurHeroAndy**（1 分） · 2026-10-25T22:05:31+08:00　
> I've been using this for a few days and I got no complaints. It is simple and easy to access on my phone, so I have been like it so far. My biggest issue with to-do apps I've tried is that they always seem to be at extremes for what I want (no info and no organization, or entirely too much info and organization). This app seems to find a really nice middle ground for me.

---

> **guidomax**（1 分） · 2026-10-25T22:11:33+08:00　
> **Project Name**: Lalabase (your project brain)
>
> **Repo/Website Links**:
>
> * GitHub: [https://github.com/lalabase/lalabase](https://github.com/lalabase/lalabase)
> * Demo (no login required, resets nightly): [https://demo.lalabase.com](https://demo.lalabase.com/)
> * Self-Hosting Docs: [https://lalabase.com/docs/en/self-hosting/getting-started/overview](https://lalabase.com/docs/en/self-hosting/getting-started/overview)
>
> **Description**:
>
> * Ticketing, time tracking, docs, and meetings tailored for agencies and freelancers working with clients.
> * Completely replaces the usual messy mix of a ticket tool, wiki, time tracker, and random spreadsheets.
> * AI is completely off by default. If you want it, you choose your own provider or even run a local model in your own network (via an OpenAI-compatible endpoint). For this crowd, that is easily the biggest selling point.
> * Comes with an MCP server and REST API.
> * Clients get their own dedicated login, and roles dictate exactly what they get to see.
>
> **Deployment**:
>
> * Docker Compose: Just grab `compose.yml` \+ `.env.docker.example`, then run `bin/rails lalabase:setup`.
> * What you need: 2 vCPU, 4 GB RAM, 20 GB disk space.
> * Current release: 2026.10.1 (Oct 21).
> * License: AGPL-3.0-only. Zero paywalled features when you self-host.
>
> **AI Involvement**:
>
> * Here is what separates it from typical "vibe-coded" projects: it’s been running in production with actual clients for a year. We enforce architectural boundaries via guardian specs in our CI (`spec/architecture/`), run Brakeman for security scans, and a real human checks every single merge.

---

> **MohammadRafieefard**（1 分） · 2026-10-25T22:25:16+08:00　
> **Project Name:** OpenCord
>
> **Repo/Website Link:** [https://github.com/mrafieefard/opencord/tree/canary](https://github.com/mrafieefard/opencord/tree/canary) (check out the canary branch)
>
> **Description:**
> Back in my restricted country, Discord was blocked and we had to use VPNs and proxies to access it, which brought us to the point that we couldn't play games anymore because of the lag and high latency. So we switched to TeamSpeak. After I moved to another country, I came across an idea: what if I mix TeamSpeak and Discord?
>
> For people who haven't used TeamSpeak: you run a server, users type in its IP and start talking. There's no login, and your client session is an encrypted hash, so people can add you as a contact and recognize you on other servers. But it has no pfp, message database, or smth like that, so everything depends on the client's end.
>
> OpenCord takes advantage of that identity model and combines it with Discord-style features:
>
> * **No accounts:** clients provide an encrypted hash to the server and everyone has their own unique fingerprint
> * **Servers store messages, channels, permissions, etc.** and act as a relay between users
> * **E2EE messages:** the server can't read what users send each other
> * **Built-in music player** using Lavalink. It translates Lavalink music packets into the voice, users can change the volume or mute it, and you can bind a key to toggle the music mute for the moment you are clutching
> * **Built-in Cloudflare Tunnel linking**, so you don't need to worry about configuring reverse proxies and tunnels or opening ports on your router
> * **Screen sharing, camera, and soundboards**
> * **File uploads** stored on the disk or in an S3 bucket
> * **Lightweight client:** Rust core with a Flutter interface (no Chromium). Flutter renders directly with the Skia engine, which makes it 4 times more efficient than Discord
> * **Lightweight server:** Rust backend; based on my benchmarks, it can run on a 512MB RAM server and hold up to 100 people
>
> **Planned:** separating the voice server and main server binaries, so people can use public voice servers and make servers multi-regional for people across the world. With public voice servers, you can self-host the main server behind Cloudflare Tunnel without opening any ports.
>
> **Deployment:**
> The server can be deployed on Windows, macOS, and Linux, and also with Docker (Docker Compose or the generated image). Installation instructions are in the repo: \[ADD LINK TO README / DOCS SECTION\]
>
> **AI Involvement:** The architecture was done by me, but the implementation was done via AI since Rust gives me a headache if I want to write it by hand

---

> **boubouble82**（1 分） · 2026-10-25T22:44:08+08:00　
> \*\*Project Name:\*\* writebook-railway – one-click Railway template for Writebook
>
> \*\*Repo/Website Link:\*\* https://github.com/jean82290/writebook-railway (template page: https://railway.com/deploy/writebook)
>
> \*\*Description:\*\*
>
> Writebook is the free, MIT-licensed app from 37signals for publishing books, manuals and documentation on the web: Markdown pages, chapters, full-page pictures, public or invite-only books, search, custom domain. My project is not Writebook itself but a deployment template that makes the official image run properly on Railway in one click. Out of the box, the image has three problems there, which the template fixes:
>
> \- Volume permissions: Railway mounts volumes as root, but Writebook runs as uid 1000 and can't write its SQLite database. The entrypoint fixes ownership, then drops privileges.
>
> \- Memory: web and job process counts follow the host's CPU count (the whole Railway machine). They're capped at 1 each, so it idles at about 220 MB (roughly $2–3/month).
>
> \- First-run takeover: on a fresh install, the first visitor becomes admin. The template creates your admin account on first boot from your email, with a generated password.
>
> Users fill in a single field (their email), and everything else is generated: password, secret key, volume, HTTPS domain, health check.
>
> \*\*Deployment:\*\*
>
> \- One-click on Railway: [https://railway.com/deploy/writebook](https://railway.com/deploy/writebook)
>
> \- It's a thin Dockerfile on top of the official, unmodified image [ghcr.io/basecamp/writebook](http://ghcr.io/basecamp/writebook) (pinned to 1.2.4). To upgrade, change WRITEBOOK\_VERSION and redeploy.
>
> \- The README documents every variable, upgrades and custom domains.
>
> \- To self-host on your own server instead, use the official image directly as documented upstream (https://github.com/basecamp/writebook): mount a volume at /rails/storage and set SSL\_DOMAIN or DISABLE\_SSL. The wrapper is aimed at Railway and I've only tested it there.
>
> \*\*AI Involvement:\*\*
>
> The Dockerfile, entrypoint script and README were written with Claude (Anthropic's AI assistant). I tested a full deployment end to end on Railway: build, automatic admin creation, health check, and logging in to the app.
>
> \*\*Disclosure:\*\* I'm the template author, and Railway pays template authors a share of the usage from deployments. Not affiliated with 37signals.

---

> **tiagomdr**（2 分） · 2026-10-25T23:47:10+08:00　
> Apple TV?
>
> This sort of functionality is what I’m missing from the current arr and similar stacks. A central panel for discovery/management

---

> **claude4242**（1 分） · 2026-10-25T23:53:11+08:00　
> **Project Name:** Tangsible
>
> **Repo:** [https://github.com/claude42/tangsible/](https://github.com/claude42/tangsible/)
>
> **Description:**
>
> I'm an avid self-hoster, and Ansible is one of my go-to tools for managing my infrastructure. But working directly with playbooks and roles can be a bit cumbersome, especially when debugging things. That's why I started building Tangsible - a terminal UI for people who work directly with Ansible playbooks and roles.
>
> It started as a better way to watch playbooks run, but has grown into a toolbox for the whole development and debugging workflow:
>
> * Interactive playbook debugging
> * Inspecting tasks, hosts, variables and execution results
> * Debugging Jinja2 templates
> * Rerunning selected tasks, hosts or roles
> * Editing and encrypting Ansible Vault variables
>
> **Deployment:**
>
> * Single binary plus an accompanying ansible-plugin, no further dependencies apart from ansible-core
> * Download source and make install or
> * Download the binary and use [install.sh](http://install.sh) or
> * Just use curl -fsSL [https://gettangsible.aw.net/](https://gettangsible.aw.net/) | sh
>
> **AI involvement:**
>
> Build almost exclusively with the help of Claude Code.

---

> **peppeg**（1 分） · 2026-10-26T00:18:15+08:00　
> Thanks, that's exactly the gap I was trying to fill!
>
> Apple TV+ is the tricky one: Apple doesn't show your viewing history on the web, so there's nothing to sync from. Apple's privacy export (privacy.apple.com → "Request a copy of your data") might contain TV activity, but honestly I've never seen one, so I don't know what's in it.
>
> If you'd be up for helping, you could request it (Apple takes a few days) and open an issue on GitHub (https://github.com/peppeg/watchsense/issues) with:
> \- the list of file/folder names in the zip (just names),
> \- if something looks like TV viewing history, its column headers and 2–3 sample rows. Feel free to blank out the titles.
>
> Please don't send the whole zip, it contains a lot of unrelated personal data.
>
> If the data is usable, I'll add an Apple TV import the same way Prime works today (CSV upload). In the meantime, if you track Apple TV with Trakt, WatchSense can already import that.

---

> **big_hole_energy**（1 分） · 2026-10-26T00:25:25+08:00　
> [https://github.com/theabbie/ntfy-auth-gate](https://github.com/theabbie/ntfy-auth-gate)
>
> Approve API requests from your phone with ntfy, as a drop-in middleware for node servers

---

> **MathLT**（1 分） · 2026-10-26T01:12:41+08:00　
> # Snug
>
> **A cozy, self-hosted tracker for the TV series you're watching.** Where you are (S02E05), what's next, what airs soon. One tap to mark an episode watched.
>
> Link: [https://github.com/mathieuletyrant/snug](https://github.com/mathieuletyrant/snug)
>
> # Features
>
> **Track**
>
> * 🛋️ **Home**: *Ready to watch* and *Upcoming*, one tap ✓ for the next episode (with undo)
> * 🆕 **New mode**: freshly aired episodes first
> * 📺 **Statuses**: Watchlist, Watching, Saving up (wait for a full season or N episodes), Paused, Completed, Dropped
> * 📊 **Progress** per season, time left to watch
> * ⭐ **Ratings** out of 10, per series and per season
> * 🙈 **Spoiler shield**: unwatched episode titles hidden until tapped
>
> **Connect**
>
> * 🪼 **Jellyfin**: watched episodes tracked automatically, webhook history
> * 🔔 **Push notifications**: new episode out, episode watched in Jellyfin (iPhone: Home Screen app over HTTPS)
> * 🤖 **AI assistant** (MCP): Claude manages your library, imports your TV Time / Trakt history
> * 📡 **Sonarr**: your Watchlist as a Custom List, so it gets downloaded
> * 🎬 **Spotarr**: a series from a shared reel lands on your Watchlist
> * 📅 **Calendar**: iCal feed of upcoming episodes
> * 📥 **Import**: CSV ([template](https://github.com/mathieuletyrant/snug/blob/main/apps/web/public/snug-import-template.csv)) or JSON export
>
> **App**
>
> * 🌍 English or French, TMDB data in your language
> * 📱 PWA: installable, offline, mobile-first
> * 🔐 Accounts: the first one is admin, sign-up closed after
> * ⚡ Bun + SQLite, home in \~20 ms for 190 series

---

> **Alternative_One_4804**（2 分） · 2026-10-26T01:34:09+08:00　
> Thanks, that's really nice to hear. Keeping it simple by default, with the heavier stuff tucked away until you want it, is exactly the goal. If anything bugs you, tell me!

---

> **KivoFGGaming976**（1 分） · 2026-10-26T02:49:12+08:00　
> Project Name: OMNI TV
>
> Repo/Website Link: [https://github.com/Rashica07/omni-tv](https://github.com/Rashica07/omni-tv)
>
> Description:
>
> OMNI TV is a lightweight, open-source launcher and software layer for Android TVs, built with older, low-memory devices in mind while also supporting more modern hardware.
>
> I started this because my Vestel TV has around 900 MB of RAM, and its stock launcher was slow and cluttered with ads. I wanted something that felt more like a proper TV operating system without replacing Android TV itself.
>
> Current features include:
>
> * Lightweight launcher: Written in Java, approximately 0.7 MB.
> * Control Center: Accessible using the INFO button on the remote.
> * Assistant: Typed and voice input.
> * System notices: Device-related notifications.
> * OMNI Cinema: A self-hosted movie library with posters and playback resume, powered by a small Python server that serves media from a local folder.
> * Additional apps: Including Weather and other components built with Kotlin.
>
> The project is free and licensed under Apache-2.0, with no ads or tracking. The README documents external services and hosts the software communicates with.
>
> I've tested it on three TVs so far. I'm especially interested in feedback from people running Android TV on older hardware, TVs with limited RAM, and devices from manufacturers other than Vestel.
>
> Deployment: The launcher runs on Android TV. The Cinema server can be hosted on another machine on your local network. Installation instructions and requirements are documented in the repository.
>
> AI Involvement: \[Briefly describe which parts, if any, were developed with AI assistance and how you used it. Be specific and transparent.\]
>
> I'd appreciate compatibility reports, bug reports, and contributions from anyone interested in lightweight Android TV software.
>
> https://i.redd.it/ketouq18tnxh1.jpeg

---

> **Leading_Advance_8600**（1 分） · 2026-10-26T04:19:02+08:00　
> Diffinery (Apache-2.0): a git forge with pull requests, reviews, a merge queue, issues, releases, a container registry and GitHub Actions-compatible CI.
>
> Upfront: it's self-hosted on your own Cloudflare account, not on your own hardware. It runs only on Cloudflare (Workers, Durable Objects, R2, D1, Containers), so nothing to patch or scale, but also no Docker image for your homelab. Self-hosted runners do run jobs on any machine you control.
>
> \- Your .github/workflows files run unchanged, marketplace actions included
> \- Each CI job gets a fresh 4 vCPU container that exists only while the job runs
> \- Passkey sign-in, invite-only accounts, push protection, audit log
> \- Imports repositories from GitHub with issues, PRs and releases
>
> Docs: https://diffinery.com/docs/self-hosting/deploy
> Source: https://github.com/codician-team/diffinery

---

> **New_Dimension_3767**（0 分） · 2026-10-26T05:33:09+08:00　
> Project Name: Aegis-WAF
>
> Repo/Website Link: [https://github.com/nextgridit-team/Aegis-WAF](https://github.com/nextgridit-team/Aegis-WAF)
>
> Description:
>
> Aegis-WAF is a single-binary, Go-based security proxy and WAF designed to sit in front of self-hosted APIs, LLM gateways (Ollama, LiteLLM, Open WebUI), and web services. It provides low-overhead request inspection to block OWASP threats, malicious payloads, and prompt injections with negligible latency.
>
> It includes a built-in Model Context Protocol (MCP) server and pre-packaged agent skill. This allows AI agents (like Claude Code, Hermes, or local runners) to query security telemetry, evaluate false positives, and adjust rules or whitelists programmatically within defined policy boundaries.
>
> Deployment:
>
> Aegis-WAF is fully released and can be run directly as a compiled Go binary or deployed via Docker/Docker-Compose. The GitHub repository includes quickstart instructions, sample docker-compose.yml configurations, and documentation for setting up the native MCP server.
>
> AI Involvement:
>
> Written in Go using native standard library and lightweight proxy primitives. AI was used as an assistive tool during development for code optimization, documentation, and drafting the bundled MCP skill instructions.

---

> **AdFew177**（1 分） · 2026-10-26T06:36:04+08:00　
> Hi r/selfhosted!
>
> For a long time, self-hosting an IP PBX meant dealing with outdated interfaces, complicated setups, or proprietary software with restrictive licensing. I wanted a modern, fast, and completely free solution that works out-of-the-box on a clean Linux server.
>
> So I built **AiPBX** — a full-featured, open-source Unified Communications platform and PBX management portal built on top of Asterisk 22.
>
> ### 🌟 What makes it different?
> - **1-Command Turnkey Install:** Sets up Ubuntu 26.04 LTS, Asterisk 22, PJSIP, Nginx, Apache, MariaDB, coturn (TURN/STUN), SSL certificates, and firewall in ~15 minutes.
> - **WebRTC In-Browser Softphone:** Make and receive crystal-clear audio/video calls directly from the web portal without installing any softphone client.
> - **Native Companion Apps:**
>   - **Android:** Fully native Kotlin app with push wake-up, background service, and full PBX control (now live on [Google Play](https://play.google.com/store/apps/details?id=com.mhrgl.AiPBX)).
>   - **iOS:** SwiftUI with CallKit support.
> - **Real-Time Team Chat:** Built-in Go WebSocket daemon (`aipbx-chat`) for 1-to-1 / group chats, file/photo sharing, presence, and read receipts.
> - **AI & Cloud Speech:** Local/cloud AI assistant for dialplan automation and Cloud TTS (Google, Polly, Azure, OpenAI, ElevenLabs).
> - **Enterprise Telephony:** Trunks, IVR, Queues, Call Center metrics, T.38 virtual fax, call recordings (with auto MP3 conversion), and Yealink/Grandstream/Fanvil auto-provisioning.
> - **100% Self-Hosted & Privacy First:** Zero telemetry, no vendor lock-in, MIT licensed. All data and call records remain strictly on your own hardware.
>
> ---
>
> ### 🔗 Links & Resources
> - **GitHub Repository:** [https://github.com/mahirgul/AiPBX](https://github.com/mahirgul/AiPBX)
> - **Website & Docs:** [https://aipbx.bid](https://aipbx.bid)
> - **Video Walkthrough (YouTube):**
>   - [Menu Tour (10 min)](https://www.youtube.com/watch?v=xU0BYN6AKE4)
>   - [Step-by-step Installation](https://www.youtube.com/watch?v=lH1-k_z5jFE)
> - **Android App:** [Google Play Store](https://play.google.com/store/apps/details?id=com.mhrgl.AiPBX)
>
> ### 💬 Looking for Community Feedback
> I’ve been pouring a ton of work into this to make self-hosted telephony modern and accessible again. I’d love to hear your thoughts, feedback, bug reports, or feature requests!
>
> Let me know what you think or if you have any questions about the architecture!

---

> **UJGA**（2 分） · 2026-10-26T06:49:42+08:00　
> * **Project Name:** Hangar
> * **Repo/Website Link:** [github.com/PresWiFi/hangar](https://github.com/PresWiFi/hangar)
> * **Description:**
>
> Hangar is a self-hosted web UI for Claude Code. Every session runs in tmux, so closing the browser doesn't kill it, and you can pick it back up from your laptop, phone, or tablet over your LAN or Tailscale.
>
> I built it because I wanted an easy way to keep sessions going while I'm away from my desktop. The layout is modeled on Open WebUI, with sessions in a sidebar, each with a live terminal and a readable transcript.
>
> * Resume or fork any past session, with optional auto-restore after a container restart
> * Phone-friendly key bar and compose box
> * Dashboard with Claude plan usage and token activity
> * Per-session file uploads and downloads
> * Pins, archive, renames, and notes
>
> https://i.redd.it/6u7o2tu30pxh1.png
>
> **Security heads up:** anyone who logs in gets a shell on the host, so use a long password and keep it on your LAN or Tailscale. Don't port forward it.
>
> * **Deployment:**
>
> Docker Compose, with a setup guide in the [README](https://github.com/PresWiFi/hangar#quick-start-docker). You need Docker and Claude Code already signed in on the host. There's no prebuilt image yet, so it builds locally. The README also covers a Tailscale sidecar with HTTPS, Windows via WSL, and running without Docker. MIT licensed.
>
> * **AI Involvement:**
>
> Heavy. Claude Code wrote most of the code. I came up with the idea and directed how it works. Since it hands out a shell, I'd appreciate anyone looking over the auth and terminal handling.

---

> **OffBrandPadawan**（1 分） · 2026-10-26T08:46:45+08:00　
> **PeriodiCool**: *a self-hosted magazine manager that works alongside the \*arr suite* (beta, vibecoded, feedback welcome)
>
> I wanted something that does for magazines what the \*arr apps do for TV and movies, couldn’t find one, and I don’t code well, so I vibecoded it with Claude.
>
> **What it does:**
>
> * You add the magazines you read.
> * It works out which issues should exist.
> * It watches your indexers (Prowlarr, Newznab, Torznab) for new and back issues.
> * It sends them to your download client (SABnzbd, NZBGet, qBittorrent, Transmission, Deluge, rTorrent, or a blackhole folder).
> * It files them in your library under clean names.
>
> It also has:
>
> * a web UI with a cassette-futurism look;
> * a library scan with a full preview before anything moves (it never deletes your files);
> * interactive search that shows why each release was accepted or rejected;
> * webhooks and a REST API.
>
> **Beta, honestly:**
>
> * It runs on my Unraid server with Prowlarr and SABnzbd.
> * The other download clients are written to their documented APIs but nobody has tried them on a real setup yet.
> * Back up /config before updating.
>
> **Who did what:** I decided what it should do and how it looks, drew the mockups and the icon, and test every release on my server. Claude wrote most of the code, the 1,500+ tests and the docs.
>
> **Want to help?** Fork it, change it, make it yours, send a PR, open an issue, or tell me it’s trash. All of it helps.
>
> * GitHub: [https://github.com/electrichobo/periodicool](https://github.com/electrichobo/periodicool)
> * Unraid: Community Apps (once approved), or the template in the repo
> * Docker: [`ghcr.io/electrichobo/periodicool`](http://ghcr.io/electrichobo/periodicool)
>
> It ships no content and no indexers; you bring your own.

---

> **cosmicmonster3080**（1 分） · 2026-10-26T08:54:35+08:00　
> **Project Name:** artifact-inbox
>
> **Repo/Website Link:** [https://github.com/mrlo/artifact-inbox](https://github.com/mrlo/artifact-inbox)
>
> **Description:**
> A self-hosted inbox for the documents your AI agents produce.
>
> I run several agents (a chat bot, a coding agent, a research agent, scheduled jobs). They all generate real work like reports, comparisons and drafts, and each one leaves it somewhere different: a chat thread, a desktop app, a file on a server. Long reports get lost in scrollback and never get read. artifact-inbox gives them all one place to drop things, and gives you a proper interface to read them in.
>
> * Agents push PDF, markdown, HTML or text over **MCP** (`/mcp`) or **REST** (`/api/push`) with a bearer token
> * Web UI with unread/done, categories with counts, "mark all done", and the source agent plus a short summary on every item
> * Real PDF viewer, sanitised markdown, sandboxed interactive HTML (a pushed checklist keeps its ticks), plain text
> * Dark mode, works on a phone
> * Agents can set themselves up: point one at [`https://your-host/install`](https://your-host/install) and it configures its MCP connection and installs a skill that tells it when to push something and when to just answer in chat
>
> It isn't a read-it-later app like Wallabag or Readeck. Those save web pages you find. This is a write endpoint for things your agents create.
>
> **Deployment:**
> Released as v0.1.0, MIT licensed. There's a multi-arch (amd64/arm64) Docker image on GHCR and a docker-compose file in the repo:
>
>     git clone https://github.com/mrlo/artifact-inbox && cd artifact-inbox
>     cp .env.example .env     # set INBOX_API_TOKEN (openssl rand -hex 32) and INBOX_UI_PASSWORD
>     mkdir -p data && sudo chown 1000:1000 data
>     docker compose up -d     # UI on http://127.0.0.1:8000
>
> One container, Python + SQLite, about 256 MB of RAM. The UI has optional built-in basic auth, or you can leave that off and put it behind your own SSO proxy; there's a Traefik example in the repo. The README, a user guide and a deployment guide are all in the repo. The compose file binds to localhost by default.
>
> Known limitations: a single shared token (no per-agent tokens or multi-user), basic auth has no lockout, and the UI shows only the newest 500 items.
>
> **AI Involvement:**
> Heavy. I designed the idea and the behaviour, and I run it daily on my own server, but most of the code, tests and docs were written by AI coding agents (Claude) working from my direction, and I reviewed and tested the results. It has a test suite (13 tests) and CI, and the security measures (HTML sandboxing, sanitising, SSRF checks) were deliberately built and tested, but treat it like any young project: read the code before you trust it with anything sensitive. Feedback and PRs welcome.

---

> **Sirajmuneer**（1 分） · 2026-10-26T14:13:13+08:00　
> Project Name:indoor map solution (spatial map)
> Description:Open-source indoor mapping software: turn floor plans (PDF/DWG) into live 3D indoor maps and digital twins with RFID, BLE and IoT sensor data, dashboards and reports. Self-hosted with Docker.
>
> Live 3D viewer — every floor, rack, bin, area and 3D model on a real map, with live data from your systems coloured and labelled by your own rules. Share read-only links with chosen floors, layers and filters.
>
> Facility editor — import floor plans (PDF, DWG, images) and draw areas, walls, doors, stairs, lifts, racks, markers, labels and 3D models, with snapping, bulk editing, undo/redo and keyboard shortcuts.
>
> Reports & dashboards — a report builder with KPIs, charts, tables and filters, ready-made reports for every facility and data table, and a full-map layout that auto-refreshes.
>
> Github link:https://github.com/Siraj-zaki/spatial-map

---

> **OpenComplaint524**（1 分） · 2026-10-26T14:47:42+08:00　
> • Project Name:
>
> Lumina AI (Autonomous Multi-Agent Quantitative Hedge Fund Studio)
>
> • Repo/Website Link:
>
> [https://github.com/ramuza0113-sketch/lumina-ai-hedge-fund](https://github.com/ramuza0113-sketch/lumina-ai-hedge-fund)
>
> • Description:
>
> An open-source autonomous quantitative hedge fund system designed to run entirely on self-hosted hardware.
>
> Trading strategies, execution logic, and portfolio balances are deeply sensitive financial data that shouldn't be shipped to third-party cloud agents or subscription SaaS. Lumina decouples qualitative agent debates (Macro, Value, Technical, Sentiment) from deterministic numeric math.
>
> All quantitative factor extraction (Qlib Alpha158) and time-series forecasting (Google TimesFM) run strictly outside LLM context in pure local Python/NumPy. It features a hardcoded CRO (Chief Risk Officer) daemon with unilateral veto power to block risky orders deterministically, an independent 10-second fast monitoring sentinel, and an interactive Streamlit UI with 3D causal knowledge graph visualization.
>
> • Deployment:
>
> Fully documented in the repository. We provide a 1-click Docker Compose setup (\`docker compose up --build\`). The entire pipeline runs smoothly on consumer hardware with CPU-only support (no expensive GPU required). Compatible with local Ollama / GGUF models or lightweight APIs.
>
> • AI Involvement:
>
> Transparently used in two ways:
>
> 1. The qualitative hypothesis debate layer inside the application uses LangGraph with local LLMs.
>
> 2. Since English is not my native language, I used an LLM to help polish the English documentation and this post.

---

> **Putrid-Ad-3724**（3 分） · 2026-10-26T16:30:19+08:00　
> steuy: kostenlose, selbst gehostete Buchhaltung für Kleinunternehmer (Rechnungen, Mahnungen, Belege, EÜR). Quelloffen und Anfängerfreundlich
>
> Ich habe **steuy** gebaut, eine selbst gehostete Buchhaltungssoftware für Kleinunternehmer (§ 19 UStG, EÜR). Rechnungen, Angebote, Mahnungen, Belege (auch direkt vom Scanner) und die Werte für die Anlage EÜR. Läuft per Docker auf 1 GB RAM, ohne Cloud und ohne Abo.
>
> Demo ohne Anmeldung: [https://steuy.philsit.de](https://steuy.philsit.de/) Code: [https://github.com/faolan-exe/Steuy](https://github.com/faolan-exe/Steuy)
>
> Ehrlich: Das ist **Vibecoding**. Idee und Konzept von mir, die Umsetzung mit Claude (KI), dazu \~980 Tests und eine CI. Keine Steuerberatung, Nutzung auf eigene Gefahr. Lizenz: quelloffen (PolyForm Shield), aber keine OSI-Open-Source-Lizenz.
>
> Feedback willkommen: Was fehlt euch als Kleingewerbe zuerst?
>
> I built steuy, a self-hosted accounting app for German small businesses (§ 19 UStG, simple cash-basis "EÜR"): quotes, invoices, dunning, receipts (incl. scan-to-folder from a network scanner) and the figures for the annual tax form. Docker, runs on 1 GB RAM, no cloud, no subscription. UI is German only.
>
> Demo (no login, resets every 15 min): https://steuy.philsit.de Source: https://github.com/faolan-exe/Steuy
>
> Disclosure: this is vibe-coded. Idea and domain decisions are mine, the implementation was built with an AI assistant (Claude), backed by \~980 tests and CI. Not tax advice. License is PolyForm Shield (source-available, not OSI open source).
>
> Feedback welcome.
>
> https://i.redd.it/e17hgg9ovrxh1.png

---

> **CrispyBegs**（1 分） · 2026-10-26T17:53:17+08:00　
> ok, i've been waiting for a magazine arr for years so will def try this out to get fashion mags for my wife. I think it would ideally also have the ability to direct download from sources like [https://www.magsguru.com/s/vogue/](https://www.magsguru.com/s/vogue/) or [https://magazinelib.com/?s=british+vogue](https://magazinelib.com/?s=british+vogue), as torrents & usenet aren't always great for many publications.
>
> the book downloaders like shelfarr have direct download options alongside prowlarr / torrent / usenet and I'd say i fall back to DD more than 50% of the time

---

> **coaster35**（1 分） · 2026-10-26T20:05:04+08:00　
> **Plevi TA (Tube Archivist)**
>
> Plevi TA is a tvOS/iOS client for Tube Archivist.
>
> **AI Involvement:** I am a software engineer and this is a side project to my main job so Claude are being used in development. I am the architect and I review and test the code. If this is an issue for you, this project is not for you.
>
> This project was started mainly because I was missing a Tube Archivist tvOS client. The name of the app comes from a navidrome/plex music app I am developing in parallel called Plevi, and Plevi TA is just an extension of that naming scheme.
>
> Pricing: Free with no in app purchases. Not everything needs to be a subscription.
>
> **Github:** [https://github.com/upfarm-development/PleviTA](https://github.com/upfarm-development/PleviTA)
>
> **TestFlight:** [https://testflight.apple.com/join/bBVGzREd](https://testflight.apple.com/join/bBVGzREd)
>
> So, what can the app do:
>
> \- Continue Watching: a row on top that sorts the videos you're currently watching by last viewed date.
>
> \- It has a custom player with built-in AV1 and VP9 support. It uses the native player for h264 and switches over to the custom player for formats unsupported by the native player. AV1/VP9 4K playback will not be smooth on current apple tv hardware because it lacks hardware encoding. 1080p works fine.
>
> \- Downloads on iOS.
>
> \- You can pin your favorite channels and playlists to the home screen
>
> \- The video page shows up next for videos who are part of a playlist + similar videos, description, file details and comments.
>
> \- Sponsor block support online and offline.

---

> **Cleeq**（1 分） · 2026-10-26T20:10:21+08:00　
> I would be interested in Logitech, if possible.  My wife uses a G435 headset that doesn't seem to want to report its battery life through any logitech means.  It sure does have a low battery warning though, which is annoying and wont go away until charged.  Your app makes me wonder if its possible through self hosted means.

---

> **Alternative-Suit5541**（1 分） · 2026-10-26T20:16:14+08:00　
> You mean as a website? I don't think so, not all usb hardware can communicate through the browser.

---

> **pmihaylov**（1 分） · 2026-10-26T20:18:42+08:00　
> Hey folks,
>
> wanted to share a nice little side project I've been working on:
>
> [useshards.com](http://useshards.com/)
>
> It's a self-hosted sandbox manager you can deploy in your home lab or VPS. I was looking for something like this because I wanted to setup some long-running agent workloads but I didn't want to use a cloud-hosted sandbox provider for this.
>
> Now I have a couple of agents running on my Mac Mini and I'm thinking of buying a bigger linux server so I can setup more sandboxes and workloads!
>
> Shard supports all the core capabilities modern sandboxes support - start/stop/pause/resume/fork
>
> It supports multiple runtimes, so you can pick what isolation level you're comfortable with based on your workloads. Pick firecracker if you want a full Micro VM or go with Sysbox if you're comfortable with using containers.
>
> Of course, this is all free and open-source, repo is here:
>
> [https://github.com/presmihaylov/shard](https://github.com/presmihaylov/shard)
>
> Would love to hear your feedback and thoughts and learn if this is something of interest to the community here as well?

---

> **antonreshetov**（1 分） · 2026-10-26T21:00:24+08:00　
> **Torsher 1.0** — a self-hosted media center in one Docker container, built for the TV first.
>
> https://i.redd.it/6yqlbp4w7txh1.png
>
> I got tired of running Jellyfin, Sonarr, Radarr, a torrent client and a request app as five apps with five databases, so I built one process that does those jobs, with a TV interface that starts from a catalog, not from files.
>
> * Pick a title on the TV, hit Watch, playback starts while it downloads (only a few minutes ahead, not the whole file)
> * Keep moves it into a library Jellyfin, Plex and Kodi can read; on one volume it's a hard link and keeps seeding
> * Follow a series and new episodes arrive on their own, same voice-over all season
> * LG webOS app (Developer Mode for now, submitted to the LG Content Store) and any browser
> * VAAPI / NVENC / CPU conversion when the TV can't play a file
> * Bring any Torznab indexer (Prowlarr, Jackett); no sources included, no telemetry
>
> amd64 + arm64, AGPL-3.0, one developer. Looking for people with NAS boxes, ARM boards and older LG TVs to tell me what breaks.
>
> GitHub: [https://github.com/torsher-app/torsher](https://github.com/torsher-app/torsher) · Docs: [https://torsher.app](https://torsher.app)

---

> **laurivosandi**（1 分） · 2026-10-26T21:30:43+08:00　
> [https://github.com/codemowers/slopify/](https://github.com/codemowers/slopify/)
>
> Tested with 100k library, it just works. Software renaissance is here :D

---

> **reppoch**（1 分） · 2026-10-26T21:49:07+08:00　
> **Project Name: GrimTorrenter**
>
> **Repo/Website Link:** [https://github.com/raistlen-grim/grim-torrenter](https://github.com/raistlen-grim/grim-torrenter)
>
> **Description:**
>
> Hi all, this is a self-hosted BitTorrent client with a web UI, shipped as a single Docker container. I wrote the BitTorrent protocol from scratch in Java (with Quarkus and an Angular UI) rather than wrapping libtorrent or another existing client.
>
> I have been a Java developer for over 20 years and Angular dev since Angular v2. I've always wanted to know how torrents work and this is the AI-assisted end result.
>
> This is a general-purpose BitTorrent client intended for sharing content you have the right to distribute, such as Linux ISOs, open-source software and Creative Commons media; you are responsible for complying with the copyright laws where you live.
>
> **Features:**
>
> * Add torrents by .torrent file, magnet link, drag and drop, or a watch folder
> * Peer discovery via HTTP/UDP trackers, DHT, peer exchange and local discovery
> * TCP and µTP, protocol encryption, incoming connections
> * Per-file priorities and skipping, labels and filtering, seeding limits (ratio and time)
> * Global and per-torrent speed limits, with a daily schedule
> * IP blocklist and SOCKS5 proxy support (with the proxy on, anything that would bypass it is turned off)
> * Live web UI: torrent list with multi-select and keyboard shortcuts, a details panel (files, peers, trackers, pieces), an event log
> * A Health page that checks folder permissions, incoming connectivity and tracker reachability, and tells you how to fix whatever fails
> * Optional password protection, and a REST API plus WebSocket feed (the UI itself is built on them)
> * Runs as non-root with PUID/PGID, and has a documented setup for running behind gluetun
>
> This is an early test build (0.9.8), not a finished product. It's IPv4 and BitTorrent v1 only, with no UPnP and no HTTPS (put it behind a reverse proxy). Private trackers that whitelist clients won't recognise it. The README has a full "Known limitations" section. Bug reports and feedback are very welcome.
>
> **Deployment:**
>
> There's a multi-arch image (amd64 and arm64) at [ghcr.io/raistlen-grim/grim-torrenter](http://ghcr.io/raistlen-grim/grim-torrenter), so there's nothing to build. The README has a docker run example, a docker-compose example, a gluetun VPN example, reverse-proxy notes, and upgrade steps. Quick version:
>
>     services:
>       grimtorrenter:
>         image: ghcr.io/raistlen-grim/grim-torrenter:latest
>         restart: unless-stopped
>         environment:
>           PUID: "1000"
>           PGID: "1000"
>           GRIMTORRENTER_LISTEN_PORT: "6881"
>         ports:
>           - "8080:8080"
>           - "6881:6881/tcp"
>           - "6881:6881/udp"
>         volumes:
>           - ./data/downloads:/app/downloads
>           - ./data/config:/app/config
>           - ./data/watch:/app/watch
>
> Create the three data folders before starting it, then open [http://localhost:8080](http://localhost:8080)
>
> Set a password (Settings → Security) before exposing it beyond your LAN.
>
> Licensed AGPL-3.0.
>
> **AI Involvement:**
>
> This was built with substantial help from an AI coding assistant (Claude Code), and the repo's [CLAUDE.md](http://CLAUDE.md) files reflect that. All of the architecture and design decisions were made in collaboration with Claude and are recorded one per file in design\_docs/. I reviewed every change before committing it, and I ran and tested the builds myself. Much of the code was written by Claude.

---

> **NoUnityRickSanchez**（1 分） · 2026-10-27T00:06:31+08:00　
> Project name: The Last Pantry
> Website Link: [https://github.com/ddmunhoz/tlp](https://github.com/ddmunhoz/tlp)
>
> Description: Hey all. As part of my prepping I wanted real numbers on my pantry: how many days of food and water do we actually have? I looked for software that could tell me and found nothing I liked, so I built one.
>
> \- Scan a barcode with your phone and the item is added, with nutrition pulled from Open Food Facts
>
> \- Set up your household (adults, kids, daily needs) and it tells you days of food, water and nutrition on the shelves
>
> \- Shelves, tags, expiry tracking, meal plans and a full activity log
>
> \- Runs self-hosted on your laptop or home server, one Docker container, no cloud, no accounts. Your data stays in a plain CSV and SQLite file
>
> Free and open source. Take a look and tell me what you think. Missing something? Open an issue on GitHub and I'll see about getting it in.
>
> https://i.redd.it/nn68gdj35uxh1.png

---

> **TianMC**（2 分） · 2026-10-27T00:18:21+08:00　
> **Project Name:** Lyvune
>
> **Repository:** [https://github.com/Tian-MC/lyvune](https://github.com/Tian-MC/lyvune)
>
> **First release:** [https://github.com/Tian-MC/lyvune/releases/tag/v0.1.0-alpha.1](https://github.com/Tian-MC/lyvune/releases/tag/v0.1.0-alpha.1)
>
> Hey everyone!
>
> I've just released the first public alpha of **Lyvune**, a self-hosted music server based on Navidrome.
>
> I started working on it because I wanted a different listening experience, especially when it comes to synchronized lyrics and Japanese music.
>
> It eventually turned into a much bigger project than I originally planned.
>
> Here's what it offers:
>
> * A redesigned web interface with two themes, including an OLED-friendly one.
> * Word-by-word karaoke when the lyrics source provides actual word timing.
> * Romanization for Japanese, Chinese, Korean, Greek, Cyrillic and Arabic.
> * A lyrics engine with multiple providers, manual overrides and optional `.lyrics.json` sidecar storage.
> * Subsonic/OpenSubsonic compatibility.
> * No telemetry by default.
>
> **Deployment:**
>
> The first alpha is available as a Docker image for both AMD64 and ARM64:
>
> [`ghcr.io/tian-mc/lyvune:0.1.0-alpha.1`](http://ghcr.io/tian-mc/lyvune:0.1.0-alpha.1)
>
> There's a Docker Compose setup and installation guide in the repository.
>
> Both architectures passed the automated Docker tests, and I also verified a fresh anonymous installation. ARM64 hasn't been tested on a physical Raspberry Pi or NAS yet.
>
> **AI Involvement:**
>
> I used Claude Code extensively throughout development. I directed the project, made the architecture and design decisions, and used AI assistance for implementation, debugging, testing and documentation. I don't want to pretend it was all handwritten.
>
> **A few things worth mentioning:**
>
> This is still a very early alpha. There will be bugs and rough edges, and database migrations from Navidrome aren't automatically reversible, so please test with a backup.
>
> It's released under GPLv3, with the original Navidrome attribution preserved.
>
> I'd genuinely appreciate feedback, especially from anyone running a NAS or an ARM64 device.
>
> Thanks for checking it out! 💚

---

> **Ok-Director4174**（1 分） · 2026-10-27T00:59:20+08:00　
> **Project Name:** Kokon
>
> **Repo/Website Link:** [GitHub](https://github.com/GabrieleLozupone/kokon) · [Self-hosting guide](https://kokon.app/self-hosted/) · [Demo video](https://youtu.be/XnC_7P2_cww)
>
> https://i.redd.it/e58rv33aeuxh1.jpeg
>
> **Description:** Kokon is an open-source photo editor that runs on your own GPU. You pick a photo, describe the change ("make it sunset", "remove the people in the back", "put him on a surfboard") and the image model does the edit locally. Every edit is kept as a version, so you can go back or branch off.
>
> Version 0.11 adds a browser interface, so you can keep Kokon on the machine with the GPU and use it from your phone, tablet or laptop. The phone layout was designed for touch, not squeezed from the desktop one. Projects and images stay on your server; nothing goes to a cloud service.
>
> **Deployment:**
>
> * Docker image `ghcr.io/gabrielelozupone/kokon` with a compose file. NVIDIA GPUs only for now (AMD/Intel via Vulkan is planned once I can test it).
> * The first start downloads the model files once into a persistent volume.
> * Browser access is password-protected (lockout after 5 wrong tries). For access away from home, use Tailscale or another VPN rather than exposing it.
> * 12 GB of VRAM recommended; an 8 GB preset exists but is beta.
> * There are also desktop apps for Windows, macOS and Linux if you'd rather not run a server.
> * Guide: [https://kokon.app/self-hosted/](https://kokon.app/self-hosted/)
>
> **License:** the app is AGPL-3.0. The bundled model (Qwen-Image 2.1) has its own non-commercial license.
>
> **AI Involvement:** I wrote much of the code with an AI coding assistant (Claude Code). I design, review and test every change myself, on my own hardware. The photos in the screenshots were made and edited with Kokon itself.
>
> Feedback on the Docker setup and the phone interface is very welcome.

---

> **sanda15**（1 分） · 2026-10-27T01:09:42+08:00　
> Project Name: VPS Pilot
>
> Repo/Website Link: [https://github.com/sanda0/vps\_pilot](https://github.com/sanda0/vps_pilot) and [https://vpspilot.dev](https://vpspilot.dev)
>
> Description:
> A self-hosted dashboard for the few Linux VPSs a freelancer or small team looks after. One hub, one small agent per server, no external database or cloud account.
>
> Works today: live and historical CPU, memory, disk and network charts, online/offline status, alerts to Discord, Slack or email, and running project commands with live output and an audit log.
>
> Commands are declared in a config.vpspilot.json on each server. The hub only sends the command name, never a command string, so even a compromised hub can’t run anything you didn’t write there. Agents enroll with a one-time token and connect over TLS 1.3.
>
> It doesn’t do deploys, containers or an open shell. Coming next: log tailing, backups and cron jobs.
>
> Deployment: the hub is a single Go binary with SQLite and the dashboard embedded, and the agent is a static Rust binary installed as a systemd service with one command from the dashboard. Prebuilt for linux amd64/arm64. No Docker image yet. Docs: [https://vpspilot.dev/docs/quick-start/](https://vpspilot.dev/docs/quick-start/)
>
> AI Involvement: I designed the architecture, protocol and security model and wrote the specs. AI coding agents (Claude Code) write the code from those specs. I review the changes, and CI runs tests and linters on every PR.

---

> **No-Asparagus-9709**（1 分） · 2026-10-27T01:56:26+08:00　
> Project Name: webos-console-home
>
> Repo/Website Link: [https://github.com/testtrader1993/webos-console-home](https://github.com/testtrader1993/webos-console-home)
>
> Description: A replacement home screen for LG webOS TVs without the ads and preinstalled apps: large tiles for an HDMI input (game console), a second input, settings and TV off. The self-hosted part is a small Python daemon (aiowebostv) that runs on a home server, starts the launcher when the TV turns on, exposes /off, /screenoff and /health over HTTP for the TV off button, and keeps LG Developer Mode from expiring via cron.
>
> Deployment: The launcher installs through LG's official Developer Mode with the webOS CLI (no root). The daemon runs in a Python venv with a systemd user unit; configuration through environment variables. Step-by-step instructions in the README. No Docker image yet.
>
> AI Involvement: Most of the code was written with an AI coding assistant. I tested it on my own TV (LG 55UP77006LB, webOS 6.5).

---

> **BigParty7725**（1 分） · 2026-10-27T02:39:30+08:00　
> Project Name: Talvio (its account and relay server)
>
> Repo/Website Link: https://github.com/ishangautam7/Talvio (server in /server) · https://talvio.sentramind.dev
>
> Description: Talvio is a desktop voice app (dictation into any app, an assistant that answers out loud, voice commands) with a phone companion. The self-hostable part is the account server: Bun + TypeScript + SQLite, no runtime dependencies. It keeps accounts and devices, relays phone to PC messages without reading them (it never stores a recording or a transcript), hands out TURN credentials for the live window view, and can optionally serve an OpenAI-compatible endpoint so your own users get a capped amount of AI usage on your keys.
>
> Deployment: Dockerfile in /server, or bun run start. The server README covers every env var and running it behind a Cloudflare tunnel. The desktop app is a Windows installer plus an Android APK from the website; macOS and Linux build from source for now.
>
> AI Involvement: a lot of the code was written with an AI coding assistant, then reviewed and tested (2k+ Rust tests on the app, 200+ on the server).

---

> **Substantial_Life2414**（1 分） · 2026-10-27T03:07:36+08:00　
> looks good 👍 i’ll give it a shot

---

> **Competitive-Number94**（1 分） · 2026-10-27T03:55:51+08:00　
> \*\*IMAGEX.AI (Album Agent)\*\* – Open-source, local-first web media extractor, gallery, and video manager with LAN access and Ollama integration (v5.2.0).
>
> Combines batch web image/video extraction directly with a local multi-tab gallery and video library:
> \* \*\*Batch Web Media Extraction:\*\* Custom domain patterns, visual Set-of-Marks (SoM) pattern teaching, concurrency limits, retries, and a Spotify-style mini-dock for background jobs.
> \* \*\*Built-in Gallery & Video Player:\*\* Lightbox viewing, contact sheets, slideshows, and native video playback.
> \* \*\*Smart Filtering & Deduplication:\*\* Organize into albums and folders, filter by resolution, tags, or fuzzy color palettes, and clean up duplicate files.
> \* \*\*Optional Local AI (Ollama):\*\* Connects to local Ollama models (llama3.2, qwen2.5, etc.) for CoPilot assistance and tagging.
> \* \*\*LAN Access:\*\* Browse and stream your media library across devices on your local network.
>
> GitHub: https://github.com/imagex-ai/album-agent

---

> **depak_7**（1 分） · 2026-10-27T04:19:33+08:00　
> # stop paying for hosted agent sandboxes you can run coding agents on machines you already own with forgerun. open source, every task gets its own sandbox.
>
>  *I wanted cloud-style coding agents (give it a task, close the tab, come back to a diff) without paying a sandbox service or sending my repo and API keys to someone else's cloud. So I built* ***forgerun***\*, and it\*  *runs on a VM I already pay for.*
>
> *Repo -* [*https://github.com/depak7/forgerun*](https://github.com/depak7/forgerun) *(star it)*
>
> ***What it does***
>
> *- You pick a repo, an agent (Claude Code, Cursor CLI or OpenCode) and a task in a web UI.*
>
> *- Every turn runs in its own sandbox: a microVM, or gVisor on VMs without KVM (most cheap cloud VMs).*
>
> *- It keeps working on the server after you close the tab. You review the diff, then push it as one commit on a branch, and optionally open a PR. Nothing reaches GitHub until you push.*
>
> *- Follow-ups continue in the same session, so the agent remembers the conversation.*
>
> *- Each repo gets snapshotted with its dependencies installed, so the next task starts warm. On expressjs/express that took setup from 26.8s to \~2.8s.*
>
> ***The part I cared about most:*** *for Claude Code and OpenCode, the real key never enters the sandbox. The agent only sees a placeholder, and a proxy on the host swaps in the real key only for that agent's own API.*
>
> *Claude Code works with your own Pro/Max subscription via claude setup-token.*
>
>  ***Install*** *(Linux, or an Apple Silicon Mac):*
>
> `curl -fsSL` [`https://raw.githubusercontent.com/depak7/forgerun/main/install.sh`](https://raw.githubusercontent.com/depak7/forgerun/main/install.sh) `| sh`
>
> *It installs what's missing, builds it, runs it as a service, and asks whether this machine is "everything" (web UI, Postgres and sandboxes) or just a worker for a server elsewhere. forgerun doctor tells you what's wrong if something isn't.*
>
> ***Honest limitations***
>
> *- It's early, so expect rough edges.*
>
> *- On Linux, microVMs need KVM. Without it, it falls back to gVisor, which isolates well but isn't a VM.*
>
> *- On a Mac, Apple Silicon only.*
>
> *Three agents for now (Claude,Opencode,Cursor , Codex coming soon).*
>
> *I'd love feedback, especially from anyone running agents on their own hardware: what's missing, what breaks.*
>
> *If it's useful to you,* ***a star on GitHub really helps*** *a small project get found. ⭐*

---

> **Anxious_Delivery_632**（1 分） · 2026-10-27T05:55:16+08:00　
> **Project Name**: tailhome
>
> **Repo Link**: [https://github.com/mickey/tailhome](https://github.com/mickey/tailhome) (MIT)
>
> https://i.redd.it/vbp9kdcbvvxh1.png
>
> **Description**: A start page for your tailnet that builds itself. I got tired of keeping a list of my Tailscale apps in a dashboard config, so tailhome reads the tailnet instead. It lists your Tailscale Services, and apps on their own tailnet device (TSDProxy v2, tsbridge, ScaleTail, \`tailscale serve\`) that answer HTTPS on port 443. Publish an app and it appears on the next refresh, with an icon and a health dot. Postgres, SSH and other non-web Services become rows that copy their connection string.
>
> It is a launcher, not a dashboard: no widgets or stats. If you use Homepage or Glance, keep them; tailhome can feed them its list. It does not read Docker labels, scan port ranges or look behind reverse proxies, so \`nas:8080\` only shows up once you publish it.
>
> Pre-1.0, one maintainer, I run it daily.
>
> **Deployment**: One \~12 MB container (linux amd64/arm64/armv7) or a binary. It joins your tailnet itself, so the host needs no Tailscale, no open ports and no Docker socket. With MagicDNS and HTTPS Certificates on:
>
> `docker run -d --name tailhome --restart unless-stopped -v tailhome-data:/data` [`ghcr.io/mickey/tailhome:latest`](http://ghcr.io/mickey/tailhome:latest)
>
> Open the login link in \`docker logs tailhome\`, then \`http://home/\` from any tailnet device. Compose file and docs: [https://github.com/mickey/tailhome#quick-start](https://github.com/mickey/tailhome#quick-start)
>
> **AI Involvement**: Written largely with AI coding agents; I designed it, reviewed the changes and test it on my own tailnet daily.

---

> **chickpea8765**（1 分） · 2026-10-27T06:11:48+08:00　
> Project Name: MealieCart
>
> Repo/Website Link: [https://okiedokiedata.com/fun-stuff/mealiecart](https://okiedokiedata.com/fun-stuff/mealiecart) (help + privacy policy).
>
> App Store: https://apps.apple.com/us/app/mealiecart/id6825056537. It's closed source, so there's no public repo.
>
> Description:
>
> I run Mealie at home, and the weekly Walmart order was the one part of meal planning that was still manual, so I built an iPhone/iPad/Mac app for it.
>
> \- Connects to your own Mealie server with an API token (tested on Mealie 3.28). It talks straight to your server, so LAN, reverse proxy or Tailscale all work. There's no MealieCart account and no server of mine in the middle.
>
> \- Shows the recipes on your Mealie shopping list or meal plan.
>
> \- You link each ingredient to the exact Walmart product once (brand, size, count). After that it's remembered every time that recipe comes back.
>
> \- One tap fills your Walmart cart using Walmart's official add-to-cart link. It never checks out.
>
> \- Skips your pantry staples, takes pack counts from the recipe ("2 cans" = 2), and "Done shopping" checks the items off your Mealie list.
>
> \- Links sync between your devices through your own iCloud. No ads, no analytics, no tracking.
>
> \- Kroger and its family of stores (Ralphs, Fred Meyer, King Soopers and others) is coming in the next update.
>
> $1.99 one time. No subscription, no in-app purchases.
>
> \*\*Deployment:\*\*
>
> MealieCart is a client app, so there's nothing extra to host: it uses the Mealie server you already run (or a hosted one). Install it from the App Store (iOS/iPadOS 17+ or an Apple silicon Mac). In Mealie, create an API token (Profile → API Tokens), then in MealieCart go to Settings, enter your Mealie address and the token, and pick your shopping list. Step-by-step quick start and help: https://okiedokiedata.com/fun-stuff/mealiecart. You also need a US walmart.com account.
>
> \*\*AI Involvement:\*\* Most of the code was written with AI coding tools (Claude Code and OpenAI Codex) under my direction. I designed the features and tested it on my own Mealie server with my real Walmart cart. Not affiliated with Mealie or Walmart.

---

> **mos3abof**（2 分） · 2026-10-27T06:53:21+08:00　
> # Introducing CareerHunt 🎯: An open-source, self-hostable job application tracker
>
> Link: [https://careerhunt.app](https://careerhunt.app)
>
> Hey r/selfhosted!
>
> I've been a long-time lurker here, and I'm excited to finally share something of my own: **CareerHunt**, an open-source job application tracker you can self-host and keep under your control.
>
> The idea came, as it usually does, because I am looking for a job and wanted a simple way to keep track of applications, interviews, contacts, notes, and progress without handing my career history over to yet another SaaS platform. I couldn't quite find what I wanted, so I built a little app and deployed it on my local Kubernetes cluster. Problem solved, right?
>
> Well, my brain had other plans. 😅
>
> What followed was a few weeks of hyperfocus, one rabbit hole after the other, and multi-layered scope creep:
>
> * **A design system:** I built and open-sourced a geometric design system for my software venture, Arabesque Labs.
> * **A rebrand:** The tracker grew into a proper project, so I gave it a name and a home: CareerHunt.
> * **Custom documentation:** I love Docusaurus, but now that I have a design system, I couldn't just use it as is, right?! I ended up building a custom theme and even remixing the Docusaurus dinosaur using geometric patterns! 😅
> * **Bonus side quests:** A UI refresh for my open-source browser extension and a new theme for my personal website.
>
> Somewhere along the way, this stopped being just a tool for my own homelab and became something I wanted to share, in the hope that it might make someone's life a little bit better!
>
> # So, what is CareerHunt?
>
> CareerHunt helps you manage your job search in one place, from applications and interview stages to the notes and details you'd otherwise scatter across spreadsheets, documents, and browser tabs.
>
> **The idea is simple: your job search, on your own infrastructure, with your data under your control.**
>
> # ✨ Features
>
> * 📊 **Application pipeline:** Keep track of applications as they move through stages such as Applied, Interviewing, Offer, and Rejected.
> * 📝 **Application details:** Organize job descriptions, notes, contact information, salary details, and other information in one place.
> * 🔒 **Self-hosted and privacy-first:** Keep your job search data on infrastructure you control, rather than relying on a third-party hosted service.
> * 🎨 **A custom UI:** A clean interface built with an open-source geometric design system.
> * 🐳 **Flexible deployment:** Run it with Docker Compose or deploy it to Kubernetes.
>
> And a lot of little stuff that I hope you will like.
>
> # 🔗 Links
>
> * **Website:** [https://careerhunt.app/](https://careerhunt.app/)
> * **Source code:** [https://github.com/ArabesqueLabs/hunt](https://github.com/ArabesqueLabs/hunt)
> * **Quick start guide:** [https://careerhunt.app/docs/quick-start/](https://careerhunt.app/docs/quick-start/)
> * **Design system:** [https://design.arabesquelabs.com](https://design.arabesquelabs.com)
>
> # 🛠️ Self-hosting
>
> The project is designed with self-hosting in mind, with Docker Compose and Kubernetes deployment options documented in the quick-start guide. I'd especially love feedback from people who run their own services: what's missing, what could be simpler, and what would make this something you'd actually use?
>
> # 🚧 Early days; feedback welcome!
>
> This is an early release, and there's still plenty I'd like to improve. But I figured it was better to get it out there, learn from real users, and improve it in the open than to keep polishing it forever.
>
> If you're job hunting, maintaining a homelab, or just enjoy trying out open-source projects, I'd love for you to give CareerHunt a spin.
>
> Bug reports, feature requests, contributions, constructive criticism, jokes, memes, rants, or any type of feedback really, are all welcome. ❤️
>
> Hopefully, it makes someone's job hunt a little less chaotic!
>
> # Edit: AI Involvement
>
> I have used Claude heavily during these rabbit holes. However, I do intend to rewrite the rust backend from scratch for fun, practice, and learnings.

---

> **Sad_Investigator_984**（1 分） · 2026-10-27T07:22:57+08:00　
> **Project Name:** Hangar
>
> **Repo/Website Link:** https://github.com/jeffer1312/hangar · https://hangar.dev.br
>
> **Description:** A self-hosted control room for AI coding agents (Claude Code, Codex, Pi, Kimi Code). I usually have a lot of agent sessions running across a couple of machines and kept losing track of which one was stuck waiting on me.
>
> Hangar doesn't reimplement any agent: each session is the original CLI running in tmux, with your own skills, hooks and accounts. It reads the agents' structured transcripts and turns every session into a live chat, on the desktop and on your phone:
>
> * permission prompts and questions arrive as cards you can answer from the phone
> * the real terminal is right under the conversation when you need it
> * sessions that need you float to the top of the list
> * sessions can message each other and pair on a shared contract
> * token and cost estimates per day and project
>
> Nothing leaves your machines. Access is over your LAN or Tailscale; there is no cloud service in between.
>
> **Deployment:** Native desktop app releases for Linux (.deb, .rpm, tar.gz), Windows and macOS on GitHub. On Linux and Windows the app offers to install the server for you. From the terminal: `curl -fsSL https://raw.githubusercontent.com/jeffer1312/hangar/main/bootstrap.sh | bash` (there's a PowerShell one for Windows). The installer sets up the server and ends with a QR code to open it on your phone as an installable web app. Docs are the README and docs/USAGE.md in the repo. No Docker image: it has to run on the host, next to your agents and tmux.
>
> **AI Involvement:** Heavily AI-assisted. I design, test and review everything, and most of the code was written by Claude Code and Codex sessions, many of them driven through Hangar itself. MIT licensed.

---

> **Straky04**（1 分） · 2026-10-27T08:03:50+08:00　
> **Project name:** Romdex
>
> **Repo link:** Available on GitHub [https://github.com/Str4ky/romdex](https://github.com/Str4ky/romdex)
>
> **Description:**
> I always wanted a way to store my legally dumped ROMs in a nice web interface
> with the ability to download its files (game, updates, content) when needed without
> any complex user interface, useless features or functions such as emulators launcher.
>
> So that's why I build this app to do exactly like that.
>
> **What this can do**:
>
> * View games in a card layout
> * Order games by console
> * Search for games
> * Download game files
> * Steamgrid integration
> * Custom graphical assets
>
> **Deployment:** Available on Docker Hub [https://hub.docker.com/r/straky/romdex](https://hub.docker.com/r/straky/romdex)
>
> **AI involvement:** Most code was human written but AI was used to refacto small functions or help me understand how Docker works (this is my first project posted on Docker Hub). Everything else is human made (UI, logo, graphical assets, readme, etc...)

---

> **alberto-romano03**（1 分） · 2026-10-27T16:44:41+08:00　
> **shelfit-app: a self-hosted TV Time alternative**
>
> **Project Name:** shelfit-app
> **Repo:** [https://github.com/alberto-romano03/shelfit-app](https://github.com/alberto-romano03/shelfit-app)
> **Website:** [https://alberto-romano03.github.io/shelfit-app/](https://alberto-romano03.github.io/shelfit-app/)
> **Description:** A self-hosted PWA for tracking and rating the movies and shows your household owns and watches, styled like a 1990s video-rental shop. One instance serves one household. Everyone picks their profile on a Netflix-style screen and has a private library behind their own password. It pulls metadata and artwork from TMDB (free API key required), tracks per-episode progress, ratings, watch stats and discs you own, and works offline once installed on your phone. Optional extras: Kodi playback and sync, [Fanart.tv](http://Fanart.tv) artwork, and importing your history from a TV Time export. The frontend is vanilla JS with no framework, and there are only five runtime dependencies. It runs best on mobile screens.
> **Deployment:** Docker Compose. Backend is Node 22 + Fastify, with all data in a single SQLite file under `data/`. Setup guides in the README: localhost/LAN only, or Tailscale + Caddy for HTTPS (needed for PWA install and push notifications on your phone).
> **License:** MIT (the bundled third-party assets keep their own licenses).
> **AI Involvement:** Built entirely with AI assistance, then tested and reviewed on a real deployment. Details in the README’s AI disclaimer.
>
> Feedback, bug reports and feature requests are very welcome. 🧡
>
> https://i.redd.it/d1fylhnzczxh1.jpeg

---

> **Accomplished-Bend589**（2 分） · 2026-10-27T19:12:35+08:00　
> **Project Name:** NetRiva
>
> **Website:** https://net-riva.com (download: https://net-riva.com/download/, docs: https://net-riva.com/docs/)
>
> **Description:** A network monitor you run on your own machine. It's one program for Windows or Linux, amd64 and arm64, so a Raspberry Pi 4/5 works. There's no database server and no cloud account; device lists, configs, credentials and logs stay on your box. It covers what usually takes several tools:
>
> * **Discovery and a live map** – ARP, SNMP and LLDP/CDP, drawn over your own floor plan with traffic moving along the links
> * **Monitoring** – ping, latency and loss, SNMP v2c/v3 interface counters, HTTP/TLS/TCP service checks
> * **Syslog receiver** – with its own page and retention you set
> * **Config backup for switches and firewalls** – over SSH (full config.xml on pfSense/OPNsense), alert on any change, show the diff, restore with a dry run
> * **Scheduled health checks** – certificate expiry, disk space, config drift, backup verification
> * **Alerts** – Slack, Discord, Teams, email, webhooks and ntfy
> * **Reports** – availability/SLA, interface utilisation and config changes as CSV or PDF
> * **AI assistant (beta, off by default)** – use your own API key, or a local Ollama so nothing leaves your network. It runs read-only commands on your switches and firewalls; config changes need your approval.
>
> **Deployment:** Windows installer or portable zip; Linux .deb and .rpm packages that install a systemd service, or a single binary. No Docker image yet. Install guide: https://net-riva.com/docs/ – everything it sends out is listed at https://net-riva.com/privacy/, and it can run air-gapped.
>
> **Price:** closed source and paid, yearly licences from $49 (10 devices). The 14-day free trial has every feature and needs no card.
>
> **Testers wanted:** I'm looking for 5–10 people to run it on a real network for about a week and fill in a short feedback form. Testers get a free unlimited lifetime licence: https://net-riva.com/testers/vy77f5mz7gnh/
>
> **AI Involvement:** I'm the developer. Much of the code was written with AI help (Claude), and all of it was reviewed and tested. The Windows installer isn't code-signed yet, so SmartScreen will warn you.

---

> **Accomplished-Bend589**（1 分） · 2026-10-27T19:24:17+08:00　
> https://i.redd.it/ofhizfsnvzxh1.png

---

> **Sad_Equivalent1511**（2 分） · 2026-10-27T20:27:10+08:00　
> https://i.redd.it/ahghawrg60yh1.png
>
> **Project Name: Vox Cordis**
> **Repo/Website Link:** [GitHub Repository](https://github.com/Nucume/VoxCordis)
> **Description:** Vox Cordis is a *vibe-coded* Application for self-hosting AI Companions locally with a file system on your own Computer. It allows also the usage of API Keys. The project is meant to maximize more privacy, especially with AI Companions.
> Current Features include: Chat, Images and Memory (You can write with it, it can generate images and has a setup to reinforce memories a bit better.), Skill Loading (Prompts that the AI will prioritize when generating messages.), Reminders/Automations (Tasks you can schedule for your AI) and a relatively customizable appearance. It's an OpenSource Hobby Project.
> **Deployment:** You can download the newest Installation for Win/Linux on the [GitHub Releases](https://github.com/Nucume/VoxCordis/releases). It has an In-Built automatic updater. The installer is not code-signed yet, so SmartScreen may warn the first time ("More info" → "Run anyway").
> **Price:** Free. Entirely.
> **Testers Wanted:** We would appreciate people trying it to find errors and bugs with it. Any feedback is welcome to help us improve it.
> **AI Involvement:** This is mainly made with Claude Code (AI). We are directing it with heavy instructing and as detailed as possible to make this work. Everything is documented on the GitHub.

---

> **MasterOfAutomation**（1 分） · 2026-10-27T21:16:24+08:00　
> - **Project Name:** Deckhand
> - **Repo:** https://github.com/CristianMori/DeckHand
> - **Description:** A self-hosted agentic development framework for running Claude Code and Codex sessions, plus plain terminals, across your own machines. You manage everything from one web UI that works on a phone too, and it chimes whenever any session on any machine is waiting for you. Machines on your network discover each other, so there's no cloud service and no accounts. Sessions can talk to each other, hand off tasks, and move between machines.
> - **Deployment:** On each machine, git clone the repo, run `npm install`, and start it. The README has the full steps, a config reference, and the security model. It runs on Windows and Linux. There's no Docker image yet.
> - **AI Involvement:** Claude wrote it from my specs: the architecture document, functional specs, and a detailed specification. I edited several functions, hand-typed the interface, and refactored some of the base architecture. Since then it's been a continuous improvement cycle between the two of us.
>
> I'm the author, and happy to answer questions.

---

> **ne0x86**（1 分） · 2026-10-27T22:58:38+08:00　
> **Project Name:** lastcall
>
> **Repo/Website Link:** https://github.com/ne0x86/lastcall (Apache-2.0)
>
> **Description:**
>
> AI subscriptions (Claude Pro/Max/Team, ChatGPT Plus/Pro/Business) have weekly limits that reset, and whatever you
> don't use before the reset is gone. lastcall watches those limits. When a reset is close and capacity is left, it
> spends it on your GitHub repositories:
>
> - **Audits:** four reviewers (bugs, security, hygiene, performance) read the code, and a judge checks every
>   finding against the code and drops the noise.
> - **Fixes:** small pull requests, each the smallest fix with a regression test. lastcall (not the agent) reruns
>   your tests in a clean container and scans the change for secrets before it pushes.
> - **Decisions:** what it shouldn't decide alone goes to one issue for you.
> - **Optional extras:** tests for behaviour nothing checks, dependency upgrades that need code changes,
>   improvement plans where you tick the ideas you want built, and issues you label `lastcall`.
> - **Production errors:** it can read your errors from Sentry/GlitchTip, from your containers' logs or from Loki,
>   so audits look for their causes first.
> - **Your own quota comes first:** it keeps a reserve for you (10% of each week by default), stops before any
>   paid usage, and never merges anything without your approval.
>
> It drives the official, unmodified CLIs (Claude Code, Codex) with your own login. It can also spend an API key
> with a monthly budget, or a local model on Ollama at the hours you choose. With a local model, no model provider
> sees your code.
>
> Security was the main design constraint:
>
> - every agent step runs in a throwaway, unprivileged container with no capabilities;
> - the only way out is an egress proxy with a short allowlist: no LAN, no GitHub;
> - agents never hold GitHub credentials, and lastcall pushes through your own private GitHub App;
> - only a small supervisor with no network has the Docker socket.
>
> There's a FAQ covering quota, provider terms, prompt injection, the Docker socket and how to remove it:
> https://github.com/ne0x86/lastcall#-faq
>
> **Deployment:**
>
> Docker Compose with published images (amd64 and arm64, on ghcr.io); nothing to install on the host:
>
>     git clone --branch stable https://github.com/ne0x86/lastcall && cd lastcall
>     docker compose up -d
>     docker compose logs lastcall   # the one-time setup code
>
> Then open http://127.0.0.1:8080 and follow the Getting started card:
>
> 1. Create your GitHub App in one click.
> 2. Add your accounts.
> 3. Pick your projects.
>
> The web UI has no JavaScript and works fine on a phone, in English and Spanish. The README covers running it on a
> server (SSH tunnel, LAN, or HTTPS behind a reverse proxy) and updating with a single `git pull`. It needs Docker 26
> or later. It's tested on Linux and on Windows with Docker Desktop; macOS should work but is untested. It works
> with GitHub only for now.
>
> **AI Involvement:**
>
> Heavy, and on purpose, given what the tool does. Most of the code was written with Claude Code, with me deciding
> the design, testing every step on my own server and reviewing the changes. To keep it honest:
>
> - the test suite (about 830 tests) runs on every PR, including sandbox tests against the real containers;
> - adversarial review rounds checked the code, the security model and the docs before releases;
> - the README and FAQ were checked claim by claim against the code.
>
> Issues and criticism are welcome.

---

> **ComprehensiveKale373**（1 分） · 2026-10-27T23:08:28+08:00　
> NanoCrew – open-source, self-hosted alternative to Grok Bot (v0.1, MIT)
>
> [https://github.com/shivasaini04/nanocrew](https://github.com/shivasaini04/nanocrew)
>
> A crew of AI agents that runs on your own machine with Docker Compose. It started as a fork of Gavriel's NanoClaw.
>
> \- Every agent cycle runs in its own container (shell, files, headless browser, Python), not on your host
>
> \- Approvals inbox for sensitive actions; cron, webhook and chat triggers; hand-offs between agents
>
> \- LiteLLM gateway: Anthropic, DeepSeek, Gemini, Groq, OpenRouter and others, with fallback and daily spend caps
>
> \- SQLite storage, no cloud account needed beyond an LLM API key
>
> It's early: the first image build needs about 20 GB of free disk, and the first container start on Windows can be slow. I'd love to hear what breaks on your setup.

---

> **WillingnessBetter956**（1 分） · 2026-10-27T23:22:43+08:00　
> **Project Name:** Bindizr
>
> **Repo/Website Link:**
>
> * [https://github.com/kweonminsung/bindizr](https://github.com/kweonminsung/bindizr)
> * [https://kweonminsung.github.io/bindizr/](https://kweonminsung.github.io/bindizr/)
>
> **Description:**
>
> The project has been public since 2025, and I'm sharing its first stable release.
>
> I'm the author of Bindizr, a Rust control plane that holds zone data in one database and serves AXFR/IXFR transfers to BIND, Knot DNS, and other authoritative secondaries. Different DNS implementations can use the same management layer while answering client queries directly.
>
> Catalog zones provision and remove zones on supporting secondaries. Changes are versioned by SOA serial, with diffs and rollback. API/CLI changes, nsupdate, and Kubernetes ExternalDNS feed the same zone data; API tokens and TSIG keys have permissions scoped to zones, record names, and types. It also supports DNSSEC signing and parent DS checks.
>
> A separate web UI is available at [https://github.com/kweonminsung/bindizr-ui](https://github.com/kweonminsung/bindizr-ui).
>
> https://i.redd.it/3m2bwdx421yh1.png
>
> **Deployment:**
>
> SQLite, PostgreSQL, or MySQL. The repository includes a Docker Compose example with PostgreSQL and two BIND secondaries. The web UI is run separately; both repositories include setup instructions.
>
> **AI Involvement:**
>
> AI tools have been used during development and to help draft this post.
>
> After several rounds of fixes and improvements, I've recently released 0.1.0.

---

> **apn44**（1 分） · 2026-10-27T23:24:51+08:00　
> **Project Name:** DLPrevent
>
> **Repo/Website Link:** [https://github.com/dlprevent-dev/dlprevent](https://github.com/dlprevent-dev/dlprevent)
>
> **Description:**
> Hey everyone, I’m Mike 👋 I’ve been building DLPrevent, a lean, self-hosted data-loss detection tool written in Rust 🦀
>
> The idea came from reading way too many breach reports. Most of them weren’t fancy hacks. Someone just copied company files to a private account, and nobody noticed for months. The commercial DLP tools are pricey, heavy and usually cloud-only, so I built something small you can run yourself.
>
> How it works: you pick the folders you care about. When a program reads from one of them and then sends data out (a browser upload, a USB stick, dragging a file into an AI chat), you get an alert. It shows the user, the process, the files and the destination.
>
> * Agents for macOS, Windows and Linux, all in Rust and very light (\~20 MB RAM on Windows)
> * Central dashboard with alerts, rules, syslog forwarding, SSO, 2FA and passkeys
> * “Strict” folders: only destinations you allow, and optionally the sending program gets cut off the network
> * Agents also work standalone, no server needed
> * Apache 2.0. There’s a paid enterprise edition for larger orgs (four-eyes approval, longer retention), but everything in the repo stays free.
>
> It’s not magic, though. Nobody can stop someone from taking a photo of a screen. The README has an honest section on what it catches and what it doesn’t.
>
> Screenshot: [https://github.com/dlprevent-dev/dlprevent/blob/main/docs/images/dashboard.png](https://github.com/dlprevent-dev/dlprevent/blob/main/docs/images/dashboard.png)
>
> **Deployment:**
>
> * Central server: Docker Compose (Postgres 18 + server) or a `.deb` with systemd. A small box is enough (2 cores / 4 GB for \~200 agents).
> * Agents: installers for macOS, Windows and Linux. You enroll them from the dashboard.
> * Docs: [INSTALL.md](https://github.com/dlprevent-dev/dlprevent/blob/main/docs/INSTALL.md) and [SERVER.md](https://github.com/dlprevent-dev/dlprevent/blob/main/docs/SERVER.md)
> * Current release: v0.2.0, so it’s still early. Feedback is very welcome!
>
> **AI Involvement:**
> I used Claude Code for helping writing the code. The idea, architecture, design decisions and testing in my own Windows/AD lab are mine, and I review what goes in.

---

> **CosmicThing2**（2 分） · 2026-10-27T23:25:09+08:00　
> **Project Name:** Pinchtube
> **Repo:** [https://github.com/CosmicThing2/PinchTube](https://github.com/CosmicThing2/PinchTube)
>
> **Description:** Host your own YouTube - Pinchflat + Pinchtube
> **AI Involvement:** Claude Code Opus 5.5 was used for developing the project.
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
> https://i.redd.it/qe6vfd2i21yh1.png

---

> **finesseserver**（1 分） · 2026-10-28T00:22:21+08:00　
> **Project Name:** Finesse
>
> **Repo/Website Link:** https://github.com/CoffeeCC/finesse (Discord: https://discord.gg/G4RfBMytJg)
>
> **Description:** Finesse is a free, open-source app that sets up a whole home media server for you. It installs and wires together Jellyfin, Sonarr, Radarr, Lidarr, Prowlarr and its own request page. The idea is "search, add, watch": you search for a movie or show on the request page, add it, and it shows up to watch in Jellyfin. The goal is to skip the hours of connecting apps and API keys by hand. It does not install Bazarr or Jellyseerr.
>
> **Deployment:** Linux: one command (in the README). Windows: one installer. Both are on the repo, with install docs. Mac and TV apps are planned, but there's no timeline yet.
>
> **AI Involvement:** The code is AI-assisted, but I review and test it. The mascot voice and art are AI-generated.
>
> Happy to answer questions or take feedback here or on Discord.

---

> **CheeseOnFries**（1 分） · 2026-10-28T00:27:57+08:00　
> **Project Name:** Fairweather
>
> **Repo/Website Link:** [https://github.com/john-overton/fairweather](https://github.com/john-overton/fairweather) · live at [https://openglades.com/fairweather](https://openglades.com/fairweather)
>
> https://i.redd.it/yazsza9md1yh1.png
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
> It's a Next.js app that runs as a Node service behind nginx at \`/fairweather\` so it nestles cleanly behind whatever selfhosted domain you use.  It includes job templates with a crontab for alerts and the radar cache. \`docs/DEPLOYMENT.md\` covers install, the systemd unit, the nginx block, and cron. The repo includes the systemd unit and nginx config.
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

> **LJ_LongWing**（0 分） · 2026-10-28T00:33:30+08:00　
> Plex Library Auditor: find what nobody watches in your Plex library, and what's missing from your collections
>
> GitHub: https://github.com/ljlongwing/plex-library-auditor · MIT · Docker image on ghcr.io
>
> My Plex server kept filling up with stuff nobody had touched in years, and Plex itself doesn't make that easy to see. So I built a small web app (Streamlit + SQLite) that pulls your library into a local cache and lets you sort it out:
>
> \- Library Audit: every movie and show with size, resolution, rating, collections and last-watched date. A rule builder finds things like "unwatched, added over 6 months ago, bigger than 10 GB".
>
> \- Series Auditor: uses TMDB to show the collections and series you only partly own (e.g. 2 of 3 movies).
>
> \- Cleanup: delete straight from the app. If Radarr/Sonarr is connected, it unmonitors the item there so it doesn't come back. Everything deleted goes into an audit log with the space freed.
>
> \- Logs in with [plex.tv](http://plex.tv) OAuth. Tokens and API keys are never sent back to the browser.
>
> It's single-user and acts with your Plex owner token, so keep it on your LAN or behind an auth proxy. There's an optional APP\_PASSWORD lock.
>
> Setup: docker compose up -d, open :8501, and log in with Plex. There's also a Portainer stack option in the README.
>
> AI disclosure: a lot of the code was written with Claude Code (an AI coding assistant), with me directing, reviewing and testing it on my own server. It has a pytest suite that runs in CI on every PR.
>
> Feedback, issues and PRs welcome.

---

> **ImX99**（1 分） · 2026-10-28T01:25:40+08:00　
> **Project Name:** Printr
>
> **Repo/Website Link**:
>
> * [https://github.com/XNinety9/Printr](https://github.com/XNinety9/Printr)
> * docs and examples: [https://xninety9.github.io/Printr/](https://xninety9.github.io/Printr/)
>
> **Description**:
>
> Printr turns a thermal receipt printer (Epson TM-T88V, other 80 mm ESC/POS printers over USB or the network) into a family gadget. You build tickets from 56 blocks (weather, sudoku, riddles, word search, news, shopping list, birthdays, notes with a photo…), print them from your phone or schedule them, like a morning brief at 7:30 on weekdays.
>
> It's a single Rust binary with a small web app: family accounts, live preview, schedules, history, and a queue that keeps tickets when the printer is off or out of paper. It plays well with the rest of the house: Home Assistant (MQTT discovery, plus a community integration), Node-RED, and a plain HTTP API.
>
> Almost everything runs locally or uses free, keyless APIs. AI is optional: a few blocks (bedtime story, recipes, word of the day) can use Claude, or any compatible endpoint including a local model, and everything else works without it. Version 2.0 is about running it without a terminal: first-run wizard, settings in the app, backup and restore, signed automatic updates.
>
> **Deployment:**
>
> Released (v2.0.0), with docs in English and French.
>
> * Docker: a Dockerfile and compose.yaml ship in each release archive (next to the binary): `docker compose up -d --build`. The container sees /dev for the USB printer, runs as an unprivileged user, and Home Assistant/MQTT work from there.
> * Any Linux with systemd: `curl -fsSL` [`https://xninety9.github.io/Printr/install.sh`](https://xninety9.github.io/Printr/install.sh) `| bash` (checks the release signature, installs a hardened systemd service).
> * Raspberry Pi: a ready-to-flash image (also listable in Raspberry Pi Imager). With no network, the printer prints a QR code to join a setup hotspot and pick your Wi-Fi from the phone. Prebuilt binaries for aarch64, armv7, armv6 and x86\_64.
>
> **AI Involvement:**
>
> Built with heavy use of Claude Code (Anthropic's coding assistant): most of the code was written by it under my direction. I design the features, review the changes, and test everything on the real printer and Pis. Separately, the app itself can optionally call Claude for a few text blocks, as described above.
>
> https://i.redd.it/yrzlts54o1yh1.png

---

> **Relevant_Mousse_9117**（1 分） · 2026-10-28T01:42:29+08:00　
> \*\*mcp-warden\*\*: a local credential broker for AI coding agents (Claude Code, Cursor, Codex, any MCP client)
>
> Agents get scoped actions instead of keys. You define presets: an HTTP base URL with allowed methods and paths, SSH commands by regex, named SQL queries. mcp-warden validates each call, injects the secret from the OS keychain and returns only the result. A prompt-injected "delete the prod repo" is refused before the key is even read.
>
> \- No cloud, no account, no telemetry, no update check. A single binary (about 15 MB on Linux) and an append-only SQLite audit log.
>
> \- Approval per preset: a native dialog on macOS/Windows, a desktop notification on Linux, or Approve/Deny buttons in Telegram. \`mcp-warden lock\` is a kill switch for every running agent session.
>
> \- \`mcp-warden scan\` finds plaintext keys in MCP client configs and \`.env\` files without printing them; \`mcp-warden import\` moves them into the keychain.
>
> \- Apache-2.0. Prebuilt binaries for macOS and Linux, or \`cargo install --locked mcp-warden\`.
>
> Repo: [https://github.com/ermoluk/mcp-warden](https://github.com/ermoluk/mcp-warden)
>
> \*\*mcp-warden\*\*: a local credential broker for AI coding agents (Claude Code, Cursor, Codex, any MCP client)
>
> AI disclosure: some of the code was written with Claude Code.

---

> **requ1tas**（1 分） · 2026-10-28T02:58:05+08:00　
> **Project Name:** OpenWebPrint
>
> **Repository:** [https://github.com/Florian-Cullmann/openwebprint](https://github.com/Florian-Cullmann/openwebprint)
>
> Hey everyone!
>
> I've always found it frustrating how printing and scanning still involves outdated interfaces, manufacturer-specific software, and unnecessary complexity.
>
> So I started building **OpenWebPrint**, a free, open-source, self-hosted web application that lets you manage printers and scanners directly from your browser.
>
> The idea is simple: one modern interface for printing and scanning, without relying on yet another manufacturer app or cloud service.
>
> **What it currently supports:**
>
> * Automatic discovery of compatible network printers and scanners
> * Printing PDFs and images with options like duplex, color, paper size, and copies
> * Scanning documents with previews, cropping, rotation, and PDF export
> * Print job management and device status
> * Optional user accounts and authentication
> * A hardware-free demo mode for trying the interface
>
> **Tech stack:** React, TypeScript, Node.js, SQLite, CUPS, and SANE.
>
> **Deployment:** Docker Compose or a native installer for Linux and macOS. Installation instructions are available in the repository.
>
> The project is currently in its first public beta (v0.1.0-beta.1). The core printing and scanning integrations are implemented, but real-world hardware compatibility still needs more testing. Windows isn't supported yet.
>
> **AI involvement:** I've used AI-assisted development tools during development. I guide the architecture and implementation, and review and test the results.
>
> I'm sharing this because I'd genuinely love to get feedback from people who run their own printers and scanners at home.
>
> Especially interested in hearing:
>
> * What printer/scanner models are you using?
> * Would something like this be useful in your self-hosted setup?
> * What would you expect from a tool like this before installing it?
>
> Bug reports, suggestions, and contributions are very welcome.
>
> Thanks for checking it out!

---

> **Wonderful-One8824**（1 分） · 2026-10-28T04:53:43+08:00　
> **Project Name:** XGView
>
> **Repo/Website Link:** [https://github.com/xhbl/xgview](https://github.com/xhbl/xgview)
>
> **Description:** A live camera wall for self-hosted cameras. Self-hosted NVRs like Frigate are headless, so there's no "walk into the room and see every camera" screen like old hardware NVRs had. XGView draws one on whatever screen you have. It only displays; your NVR keeps doing recording, detection and storage.
>
> **Sources:** Frigate API, go2rtc, Synology Surveillance Station, ONVIF, or manual RTSP/MJPEG/MSE
>
> * Frigate import pairs main/sub streams automatically; RTSP with MSE fallback when RTSP isn't reachable (e.g. behind a reverse proxy)
> * Sub streams in the grid, main stream only on zoom or pin; VAAPI hardware decoding
> * Layouts 1x1 to 4x4 plus mixed, camera groups, DPAD remote friendly
> * No account, no cloud, no telemetry, one JSON config, MIT license
>
> **Deployment:** Native app, no Docker image needed. Downloads for Android (APK, arm64, 8.1+), Windows, Linux and macOS: [https://github.com/xhbl/xgview/releases/latest](https://github.com/xhbl/xgview/releases/latest) . Docs are in the README (install per platform, getting started, troubleshooting): [https://github.com/xhbl/xgview#readme](https://github.com/xhbl/xgview#readme) . For a dedicated screen on Linux, there's a documented kiosk setup (minimal Debian 13 + Xorg + openbox, systemd unit at boot, Docker for Frigate on the same box) with a setup script: [https://github.com/xhbl/xgview/blob/master/docs/DEBIAN-KIOSK.md](https://github.com/xhbl/xgview/blob/master/docs/DEBIAN-KIOSK.md)
>
> **AI Involvement:** Solo project, developed with AI assistance under my direction and testing. Please review the code before using it in sensitive setups.
>
> Feedback welcome, especially on different hardware and camera/NVR setups.

---

> **Wonderful-One8824**（1 分） · 2026-10-28T05:01:47+08:00　
> https://i.redd.it/26nznp3oq2yh1.jpeg

---

> **Commercial-Rush-9843**（1 分） · 2026-10-28T06:19:05+08:00　
> Project Name: SSHyar
>
> Repo/Website Link: https://github.com/mh314k/sshyar
>
> Description:
> SSHyar is a day-to-day SSH desktop app designed to eliminate the need for juggling multiple tools. It combines a modern SSH terminal, SFTP file manager, and optional in-app panels for Docker, Nginx, and systemd.
> Key problem solved: It operates with a zero remote footprint. You don't need to install agents on your host just to peek at a container log or restart a service. It also features a local encrypted vault and per-profile plugin management, making it perfect for managing multiple client setups.
>
> Deployment:
> It is a desktop application available for Windows and Linux. You can download the latest binaries directly from the GitHub Releases page (MSI/EXE for Windows, AppImage/deb for Linux).
> Note: While this is a desktop client (not a web app), it is built for self-hosters and sysadmins to connect securely to their self-hosted infrastructure. Installation and setup docs are available in the README.
>
> AI Involvement:
> Minimal. AI was only used as an assistant for code refactoring and writing some documentation, but the core architecture and logic are fully human-developed.

---

> **Vivid_Promise1700**（1 分） · 2026-10-28T07:07:09+08:00　
> **Project:** Plenio Music Production System & Player
>
> **Website:** [https://github.com/jplenio/Plenio-Music-Production-System](https://github.com/jplenio/Plenio-Music-Production-System)
>
> **Description:** The music player for your ComfyUI songs now works on phones, can start ComfyUI by itself, and lets party guests react.
>
> Plenio is a free, open-source music production system for ComfyUI (YuE2, MiniMax Music 3) with its own music player. 1.3.2 is mostly about the player:
>
> **On every screen.** Phones get a tab bar, a slim player you swipe (next/previous, up for Now playing), filters and menus as bottom sheets, and Now playing that fits the screen. Tablets get a drawer. "Add to Home screen" opens it like an app. Measured on an iPhone 13: the first song now shows without scrolling (it was at 1398 px before).
>
> **Fast with big libraries.** With 2,969 songs: the library goes compressed (9.6 MB → 1.0 MB), the folders are read in the background, cards get small covers, and a keystroke in the search takes 61–81 ms (was 125–147 ms).
>
> Songs without opening a workflow. "Make a song" has presets (Best quality = HQ mastering + cover art + best of 3 takes for the lyrics; Party – fast; Quick sketch; Three takes …) and "How many" (up to 4 takes of a song, or 4 songs at once). If ComfyUI isn't running, the player starts it in the background when a song is ordered and can stop it after idle minutes.
>
> **Parties.** Guests already could see the live playlist and order songs on their phones. Now they react (🔥❤️🎉👏💃😂), the reactions float up the big screen, and Live Play counts them per song. "Up next" shows the following song in a song's last seconds.
>
> **For the workflow crowd.** Every template now opens with a "Models · what goes where" note: every file with link, size and licence, the folder tree, and what to choose for 8–24 GB of VRAM.
>
> **For developers.** Song API 1.1 (downloads, ?wait, filters) with a full guide, every field, OpenAPI and examples.
>
> Three new tutorials: the player, party songs, and the Song API.
>
> GitHub: [https://github.com/jplenio/Plenio-Music-Production-System](https://github.com/jplenio/Plenio-Music-Production-System)
> Tutorials: [https://www.youtube.com/playlist?list=PLAFqTtP59fgE](https://www.youtube.com/playlist?list=PLAFqTtP59fgE)
>
> Everything runs locally. I am the author. Happy to answer questions. 😊🎶😎
>
> https://i.redd.it/ntq3t1x1d3yh1.png

---

> **CrispyBegs**（1 分） · 2026-10-28T09:03:01+08:00　
> can i point this at my RomM library without having to change the whole folder structure so this can see it all?

---

> **Straky04**（1 分） · 2026-10-28T09:30:27+08:00　
> Not really at the moment and idk if I ever will support it. The folder structure is quite the same but console folders needs to have an exact name so the app can recognize them. And I also split games, updates, encrypted/decrypted games, demo, etc... into their own folder so you know what to download. The purpose of this isn't about emulation as I said in the message but more of a collection/downloading purposes. I will see in the future to support RomM but idk how the download user interface will work with that
>
> RomM folder structure is like this
>
>     library
>       gba
>         roms
>           game 1.gba
>           game 2.gba
>
> Romdex folder structure is more like this
>
>     library
>       Game Boy Advanced
>         Game 1
>           game
>             game 1.gba
>         Game 2
>           game
>             game 2.gba
>
> The purpose of Romdex to put games PER folder is for example you have a Nintnedo 3DS game it will be like this with multiple formats
>
>     library
>       Nintendo 3DS
>         Game
>           game
>             game.3ds
>             game.cia
>
> And the app will allow you to either download the game in 3ds or cia format

---

> **mstfyvtrl**（1 分） · 2026-10-28T09:40:02+08:00　
> **CineVault** \- [https://github.com/mustafayevt/CineVault](https://github.com/mustafayevt/CineVault) (Apache-2.0)
>
> what it is: a free desktop app (windows, linux beta, mac coming) for tidying up a movie/tv collection before your media server scans it. scan → scrape from TMDB (with a confidence % so you see the shaky matches) → rename with your own templates, with a preview and undo. writes Kodi/Jellyfin/Emby NFO + artwork, does tv shows, and has a drives page for moving titles between drives with a verified copy.
>
> who it's for: people with their library on a NAS or a bunch of external drives who want clean folder names and metadata any server picks up.
>
> install: MSI / setup exe / portable zip on windows, AppImage / deb / rpm on linux. no docker, it's a desktop app. needs your own free TMDB key (setup screen walks you through it).
>
> AI involvement: I used AI coding tools for parts of the code. the design, decisions and testing are mine.
>
> site: [https://mustafayevt.github.io/CineVault/](https://mustafayevt.github.io/CineVault/) tell me where it breaks on your naming conventions 🙏

---

> **manziosee**（1 分） · 2026-10-28T16:38:16+08:00　
> **Project Name:** Atlas
>
> **Repo/Website Link:** [https://github.com/manziosee/atlas](https://github.com/manziosee/atlas) (a live demo and dashboard are linked in the README)
>
> **Description:** Atlas is a leaderless service-discovery system written in Go. Nodes find each other through SWIM-style gossip, with no central database and no leader, and the cluster notices a dead node within seconds. Each node keeps its own SQLite replica of the service registry, so lookups are always answered locally.
>
> Features: HTTP, TCP and gRPC health checks, TTL heartbeats, graceful draining, HTTP and gRPC APIs, DNS discovery (A/AAAA/SRV), a live event stream, an embedded dashboard, a Go client with built-in load balancing, a Python client, and AES-256-GCM encrypted gossip. Prometheus metrics and a Grafana dashboard are included.
>
> It’s useful if you run services across several machines or sites and want discovery without running Consul or etcd.
>
> **Deployment:** Docker Compose is the quickest way:
> `git clone` [`https://github.com/manziosee/atlas`](https://github.com/manziosee/atlas) `&& cd atlas`
> `./scripts/gen-secrets.sh`
> `docker compose up --build -d`
> This starts a 3-node cluster with Prometheus and Grafana. A Kubernetes (Kustomize) setup, a [Fly.io](http://Fly.io) config and a Dockerfile are also in the repo. The README walks through registering a service and watching failover, and the API is described in an OpenAPI spec.
>
> **AI Involvement:** I designed the architecture and wrote the core protocol logic myself. I used AI assistants (Claude) for debugging and documentation. I reviewed and tested everything it produced, including with the chaos tests and the 1,000-node simulation in CI.
>
> It’s a learning project, and I’d welcome feedback, especially on what should happen to a record whose owner is partitioned away and then comes back.

---

> **Global-Tap-3406**（1 分） · 2026-10-28T17:58:21+08:00　
> Project Name: Orlok
>
> Repo/Website Link: [https://github.com/rylos/orlok](https://github.com/rylos/orlok) · [https://orlok.xyz](https://orlok.xyz)
>
> https://i.redd.it/3sr1xho6l6yh1.png
>
> Description: Self-hosted virtual colleagues: AI agents that read your office wiki before answering and work on your real servers, only with the autonomy you give them. Example: "The intranet is slow again, can you check web-01?" → the agent finds stuck nginx workers, recognizes the issue from a wiki page, and waits for your approval before restarting anything (allow once / always allow / deny).
>
> Current features:
>
> • Wiki that grows as you work: import from Obsidian, Notion or Joplin (passwords and keys stripped), PDFs and scans read with local OCR, a nightly review flags contradictions and stale pages
>
> • Real operations: Linux over SSH, Windows over WinRM or OpenSSH, multi-step plans approved as a whole or step by step
>
> • Guardrails: commands are parsed, not regex-matched; "always allow" covers one command type and can be revoked; the agent acts with the requesting user's own encrypted credentials, from an isolated runner container
>
> • Any model: Anthropic, OpenAI, compatible APIs or Ollama fully offline; wiki embeddings run locally; per-call cost tracking and monthly limits
>
> • Web, installable phone app and Telegram; append-only audit log (CSV/JSONL export)
>
> Deployment: Docker Compose: git clone, set a few keys in .env, docker compose up, then a first-run wizard. Guide: [https://orlok.xyz/docs/installation](https://orlok.xyz/docs/installation)
>
> Price: Free for personal and non-commercial use and for evaluation. Source-available under BSL 1.1 (each version becomes Apache 2.0 after 4 years); production use for a company needs a commercial license.
>
> Testers Wanted: Yes, especially homelabbers and small IT teams. I'd love to hear what would make you trust (or never trust) an agent on your servers.
>
> AI Involvement: The product is built around AI agents, and development is AI-assisted (Claude Code), with every change reviewed and tested by us.

---

> **Impossible-Lake-2839**（1 分） · 2026-10-28T18:52:24+08:00　
> Project Name: OpenProspect
> Repo/Website Link: [https://github.com/Bhanuteja005/openprospect](https://github.com/Bhanuteja005/openprospect)
> Description: A self-hosted prospecting workflow for freelancers and small agencies. It discovers potential clients, checks websites for concrete issues, verifies contact addresses, scores leads, syncs a CRM, and tracks replies and opt-outs. Outbound campaigns start as drafts.
> Deployment: MIT-licensed Python 3.11+ project with documented install scripts and Docker Compose services. The README includes Windows, Linux/macOS, and server setup steps.
> AI Involvement: The job track optionally uses Claude Code to draft individualized emails; the lead track can optionally use Ollama for first lines. The repo does not document development-time AI usage.
> Feedback welcome on setup and self-hosting tradeoffs.

---

> **chickpea8765**（1 分） · 2026-10-28T22:13:51+08:00　
> \*\*Project Name:\*\* Ladle for Mealie (formerly MealieCart)
>
> \*\*Repo/Website Link:\*\* https://okiedokiedata.com/fun-stuff/ladle (help, setup and privacy policy). App Store: https://apps.apple.com/app/id6825056537
>
> \*\*Description:\*\* A native iPhone, iPad and Mac app for your self-hosted Mealie (the open-source recipe manager). It started as MealieCart, which turns the recipes on your Mealie shopping list into a filled Walmart or Kroger cart. People asked for a full Mealie app, so it now does everything:
>
> \- Search and browse your recipes, favorites and ratings
>
> \- Cook mode with big text, screen kept on, and step timers that ring when the app is closed
>
> \- Scale servings (even unparsed recipes)
>
> \- Weekly meal plan, and add the whole week to a shopping list in one tap
>
> \- Shopping lists by aisle that update live across your household
>
> \- Save recipes from Safari's share sheet
>
> \- Invite household members with a QR code; they create their account in the app
>
> \- Admin screens: people, households, groups, backups, server info
>
> \- Link ingredients to exact Walmart/Kroger products once, then fill your cart in one tap (you check out yourself)
>
> \- No accounts, ads or tracking. It talks only to your own Mealie (plus Walmart/Kroger if you use the cart)
>
> \*\*Deployment:\*\* It's a client app, so there's nothing new to host. You need your own Mealie 2.0+ server (Docker, Home Assistant add-on, NAS, etc. — see mealie.io). Install Ladle from the App Store, enter your Mealie address, and sign in with your password, single sign-on (OIDC) or an API token. Works on your home network or over the internet. A built-in sample kitchen lets you try it without a server. Setup and FAQ are on the website link above.
>
> \*\*AI Involvement:\*\* Built with a lot of help from AI (Claude Code wrote much of the code). I designed it, directed it, and tested it daily against my own Mealie and real grocery orders.

---

> **sector_clear_**（1 分） · 2026-10-28T22:23:51+08:00　
> **Project Name:** Cograph
>
> **Repo/Website Link:** [https://github.com/mikekonan/cograph](https://github.com/mikekonan/cograph), docs at [https://cograph.cc](https://cograph.cc)
>
> **Description:**
>
> I got tired of watching Claude Code grep through the same repos at the start of every session, so I built Cograph. Yes, it's another MCP thing. The web UI works fine for humans too.
>
> You point it at a Git repo and it builds a code graph with tree-sitter, so you can see who calls what. It also indexes the code and docs for search, and writes a wiki for the repo where every claim links back to real source lines. If the model can't point to the code behind a claim, the claim doesn't go in.
>
> It re-indexes on every sync, so the wiki doesn't rot the way hand-written docs do. Agents get all of it through an MCP server and pull a few relevant snippets instead of reading whole files.
>
> Everything sits in one Postgres with pgvector, no extra vector DB or graph DB to babysit. For the LLM side any OpenAI-compatible endpoint works, so with a local vLLM or LM Studio your code stays on your network.
>
> Stuff you should know before trying it:
>
> * Only Python, Go, TypeScript and JavaScript get a real graph. Go is the only one I've run on real repos, the others just have unit tests. Other languages get skipped, though docs are indexed in any repo.
> * You need an embedding model even if you never touch the wiki, and it has to be 1536-dim.
> * It's pre-1.0, so pin your image tags.
> * The FAQ has the full list of known gaps: [https://cograph.cc/faq](https://cograph.cc/faq)
>
> **Deployment:**
>
> Docker Compose, which starts backend, worker, web, Postgres and Redis:
>
>     git clone https://github.com/mikekonan/cograph.git
>     cd cograph
>     docker compose up --build
>     docker compose exec backend cat /app/.cograph/bootstrap.token
>
> Open http://localhost:8080/setup, paste the token and create the admin. Then go to Admin > LLM runtime and assign an embedding model. People skip this step and indexing dies at the embed stage.
>
> There's a Helm chart too, and prebuilt images on ghcr.io. Setup guide: [https://cograph.cc/quickstart](https://cograph.cc/quickstart)
>
> **AI Involvement:** Built with Claude Code as the main coding tool. I decide what goes in and test it on real repos.
>
> Feedback welcome, especially from anyone who gets through the setup.

---

> **tommy-yy**（1 分） · 2026-10-28T22:30:20+08:00　
> **I made a small self-hosted, open-source habit tracker**
>
> I wanted a habit tracker that runs on my home server and doesn’t need an account somewhere else, so I built one (with Claude's help. I have a master's degree in computer science, I designed, reviewed and test the app on my own server). It’s a single Docker container, about 20-30 MB of RAM when idle, data in one folder.
>
> You can do daily habits, chosen weekdays or “3x a week”, plan pauses for holidays, skip a sick day without breaking the streak, and look at stats for any period. It works as a PWA on the phone, light and dark theme, English only for now. Export and import is a custom JSON file.
>
> Setup is a compose file with an admin email and password, then put it behind your reverse proxy. No telemetry, nothing leaves your server.
>
> **GitHub Repo:** [https://github.com/petrjancar/habits](https://github.com/petrjancar/habits)
>
> **Docker Image:** [ghcr.io/petrjancar/habits:2](http://ghcr.io/petrjancar/habits:2)
>
> It’s MIT licensed.
>
> If you give it a try, thank you! Tell me what you’d change, here in the comments or as a GitHub issue. :)
>
> https://i.redd.it/ft8c4wnqx7yh1.png

---

> **vishr**（1 分） · 2026-10-28T22:50:49+08:00　
> **Project Name:** Fanout – Self-hosted OpenTelemetry backend in one binary (traces, logs, metrics)
>
> **Repo/Website Link:**
>
> * GitHub: [https://github.com/labstack/fanout](https://github.com/labstack/fanout)
> * Docs: [https://fanout.run](https://fanout.run/)
>
> **Description:**
>
> I built Fanout because I wanted traces, logs, and metrics for my services in one process and one data directory, without operating separate storage services.
>
> Key features:
>
> * OTLP/gRPC and OTLP/HTTP ingestion on the same port, authenticated with an ingest token
> * Local Parquet storage with embedded DuckDB for queries
> * Preview dashboards, alerts, and MCP tools for external AI agents
> * Optional built-in AI chat using a configured Anthropic or OpenAI provider and API key
>
> In an ingest-only benchmark, Fanout v2026.10.8-alpha accepted 415,859 mixed telemetry items/s over 303.5 seconds on 8 dedicated vCPUs and 32 GB RAM. The workload used synthetic, highly compressible telemetrygen data generated from a separate host. This is not a production throughput claim.
>
> Benchmark methodology: [https://fanout.run/explanation/performance](https://fanout.run/explanation/performance)
>
> **Deployment:**
>
>     docker run -p 7520:7520 \
>       -v fanout-data:/var/lib/fanout/data \
>       -e FANOUT_AUTH_CODE_SECRET=$(openssl rand -hex 32) \
>       labstack/fanout:latest
>
> Open the setup URL printed by the container, create the first administrator, and save the ingest token shown once.
>
> **Project status:** Apache-2.0, alpha, single-node. Storage formats and user-facing contracts may change without migration paths.
>
> **AI Involvement:**
>
> Built with help from AI coding agents (Claude and Codex).
>
> I'd appreciate feedback from people running OpenTelemetry in homelabs or small deployments, especially where Fanout breaks with your data or what's missing for your use case.

---

> **benno93**（3 分） · 2026-10-28T23:29:08+08:00　
> Project Name: strava-dawarich-sync
>
> Repo/Website Link: [https://github.com/benno93/strava-dawarich-sync](https://github.com/benno93/strava-dawarich-sync)
>
> Description: Automatically imports your Strava activities into your self-hosted Dawarich(https://github.com/Freika/dawarich) instance, so runs and rides show up in your location history without manual GPX exports.
>
> \- First run imports your entire Strava history, then checks for new activities every hour
>
> \- Every activity with GPS (runs, rides, hikes, …); treadmill/indoor/strength are skipped
>
> \- No duplicates: local state file plus a check against existing \`strava\_<id>.gpx\` imports in Dawarich, so even a lost state doesn't cause double imports
>
> \- Handles Strava's rate limits on its own (pauses, then continues)
>
> \- Configurable look-back window catches activities your watch uploads days later
>
> \- Uses Dawarich's official import API; each activity appears as a normal import you can inspect or delete in the UI
>
> My own first run: 722 activities imported, 147 skipped (no GPS), 0 errors.
>
> Deployment: Docker Compose. Clone the repo, fill in \`.env\` (Strava API app credentials + Dawarich API key), authorize Strava once with \`docker compose run --rm strava-sync python authorize.py\`, then \`docker compose up -d --build\`. The README (English + German) walks through every step with a "how success looks" check plus troubleshooting. Each user creates their own Strava API app; data only flows Strava → your server → your Dawarich. MIT licensed.
>
> AI Involvement: Code, tests and README were written with Claude (AI) based on my requirements. I reviewed it and run it on my own Dawarich instance; there are 11 automated tests against mocked Strava/Dawarich APIs running in CI.

---

> **apoorvqwerty**（1 分） · 2026-10-29T00:03:51+08:00　
> **Project Name:** Ferry
>
> **Repo/Website Link:** https://ferryrss.com (closed source; App Store: https://apps.apple.com/app/id6799505775)
>
> **Description:** An RSS client for iPhone, iPad and Mac that syncs with your own FreshRSS server. Under each headline it shows how many of your feeds carried the same story, and it can rank by that, so the story ten of your sources ran sits above the newest post. With FreshRSS the app talks to your server directly and keeps your credentials in the keychain. My server only receives anonymous usage counts and the addresses of the feeds you follow, with no account or identifier attached (privacy policy: https://ferryrss.com/privacy). Also OPML import and export, offline full text, smart folders, Spotlight search and widgets. You can use it without a server too, reading on the device. Free, with an optional Plus subscription.
>
> **Deployment:** Nothing new to host. Install from the App Store, choose FreshRSS when you set up an account, and enter the root address of your FreshRSS install with your username and API password (the Google Reader API has to be enabled in FreshRSS). On the App Store since 8 Oct.
>
> Feedback very welcome, especially from FreshRSS users.

---

> **JoNike**（1 分） · 2026-10-29T03:30:33+08:00　
> **Project Name**: Channel Club
>
> **Repo**: https://github.com/jo-nike/channel_club
>
> **Description**: It's basically a UI for dispatcharr and ersatztv using plex SSO. Mainly a way for me to watch the hockey game in sync'ed with my friends (who already have access to my Plex) without crazy ads. Plus the classic TV experience via ersatztv channels.
>
> **Deployment**: Docker, you can set your variables or you can use the app wizard. `docker run -d --name channel-club -p 8334:8334 -v channel-club-data:/data --restart unless-stopped jonnike/channel-club:latest`
>
> **AI Involvement**: Used all around. I made a first version of this about a year ago with minimal AI usage and it's own streaming (no dispatcharr) but everything was rewrote using AI and Spec Driven Development. I am a professional software developer in my day-to-day life that also uses AI.

---

> **mmamphis**（1 分） · 2026-10-29T03:47:37+08:00　
> **Project Name:** NodeGuard
>
> **Repo/Website Link:** [https://github.com/mamphis/NodeGuard-Docs](https://github.com/mamphis/NodeGuard-Docs) (documentation and Docker Compose setup). Main repository: \[to be added once confirmed public\]
>
> https://i.redd.it/vrprrxeci9yh1.png
>
> **Description:** NodeGuard is a lightweight, self-hosted web app to manage the servers in your home network from one place. It solves the problem of checking several machines one by one.
>
> Features included:
>
> * Agent overview with status, certificate, OS, tags and hardware usage (CPU, memory, drives)
> * Run and schedule Bash scripts on Linux agents, targeted by tag or per server, with results on one page
> * Log viewer, file manager, process and service management on agents (confirmation of the exact views pending)
> * Alerts for disconnected agents, disk usage and CPU/memory thresholds, sent by e-mail or webhook
> * Availability statistics and CSV/JSON exports
> * Single sign-on via OIDC (Authentik, Keycloak, Authelia and others), with password login as fallback
>
> Not supported yet: Windows agents, software inventory, detection of missing security updates.
>
> It is useful for anyone with a few Linux servers at home who wants one overview and scheduled scripts without setting up a larger tool. I'm looking for a few beta testers with one to three Linux machines. Feedback and bug reports are very welcome.
>
> **Deployment:** The server runs as a Docker Compose stack (Nuxt web app and PostgreSQL). The Docker Compose file and an `.env` example are in the docs repository, and the quick start guide covers the install in about 10 minutes. The agent is one self-contained .NET binary per Linux machine, installed with a one-line script from the server. Plain HTTP on the LAN works without a certificate. Setup guides are in English ([quick start](https://github.com/mamphis/NodeGuard-Docs/blob/master/quick-start.en.md), [OIDC](https://github.com/mamphis/NodeGuard-Docs/blob/master/oidc.en.md)) and German.
>
> **AI Involvement:** Parts of the code and the documentation were written with the help of Claude (Anthropic). I reviewed and test the changes. Also im running this in my homelab as well.

---

> **Wzkiie**（2 分） · 2026-10-29T04:25:40+08:00　
> **Project Name:** Tonalo
> **Repo/Website Link:** [https://github.com/Wzkiie/tonalo](https://github.com/Wzkiie/tonalo)
> **Description:** A free, open-source client for Navidrome (self-hosted music server). There are two apps: one for LG webOS TVs (5+, made for the remote and Magic Remote) and one for iPhone (iOS 17+, with Apple Watch app). Features: synced lyrics, endless radio, crossfade, offline downloads on iPhone, several profiles on one TV. No ads, no tracking, no account except your own server. MIT licensed.
> **Deployment:** It's a client, so you need your own Navidrome server. The iPhone app is in public beta via TestFlight: [https://testflight.apple.com/join/vKkNhNZJ](https://testflight.apple.com/join/vKkNhNZJ). Setup is described in the README. Since it's a beta, I'm looking for testers. Bugs and ideas are best as a GitHub issue.
> **AI Involvement:** A good part of the code was written together with an AI coding assistant. I tested everything on a real LG OLED and iPhone, and all code is public.
>
> https://i.redd.it/b7y0z8v5p9yh1.jpeg

---

> **zhoorta**（1 分） · 2026-10-29T06:42:31+08:00　
> https://i.redd.it/d7mt3hk9dayh1.jpeg
>
> **Project Name**: Waydesk
>
> **Repo/Website Link:**  https://waydesk.dev · Source (MIT or Apache-2.0): https://github.com/zhoorta/waydesk
>
> **Project Description**: A multi-user Linux desktop over RDP for Debian 13 and Ubuntu 26.04. Every account gets its own sway desktop (shell, dock, apps, kept alive between connections), reachable from the Windows App, mstsc or FreeRDP, so there is nothing to install on the client. One \`apt install\`, then \`waydesk-setup-admin\`.
>
> **Features included**:
>
> \- **A desktop per account**: sway session with a shell, a dock, a file manager and a terminal, kept alive between connections, over standard RDP (Windows App on macOS, mstsc, FreeRDP).
> \- **Isolation and limits**: each session runs as the account itself in its own systemd slice, with memory, swap, CPU-weight and task limits per account. A new session is refused when the machine is full; compressed swap (zram) is set up for you.
> \- **Access control**: the RDP port is closed until you open it (\`waydesk-admin access local|lan|vpn|custom\`). Logins are rate-limited, only members of \`waydesk-users\` may log in, never root.
> \- **Built-in WireGuard VPN**: \`waydesk-admin vpn init\`, then \`vpn add NAME\` (one key per device, QR code for phones).
> \- **Certificate**s: self-signed by default, or a local certificate authority you import once (\`cert local-ca\`).
> \- **Tuned for screens and bad links**: H.264 screen-content mode, a picture that follows the link from 300 kbit/s to 10 Mbit/s, TCP BBR, and the pointer drawn by the client so it has no delay.
> \- **Optional GPU**: the desktop is drawn on the GPU and encoded by VAAPI (Intel/AMD) or NVENC (NVIDIA), with a fallback to software if anything fails. \`waydesk-admin status\` shows what each session uses.
> \- **Admin tools**: \`waydesk-admin\` for users, sessions, limits, status (\`--watch\`, \`--json\`), access, certificates and the VPN.
> \- **Applications**: Wayland and X11 apps (XWayland), Flathub, and \`waydesk-setup\` for browsers, office, developer and creative apps. The keyboard layout follows the client, including a Mac's keys through the Windows App.
>
> Measured on my own servers: 7 to 8 idle users with Chromium, Calc and VS Code fit on 8 GB; 24 active users on a 64 GB machine without a GPU. Early, one-person software: no second factor (use a tunnel or the VPN), internal security reviews only.
>
> **Deployment**: A native apt package from a signed repository on a bare-metal server or VM (Debian 13 or Ubuntu 26.04). No Docker image: sessions use systemd, logind and PAM. systemd services: \`waydesk\` (network daemon, no privileges), \`waydesk-helper\` (small root helper), \`waydesk-session@UID\` (one per logged-in account). The RDP port (TCP 3389) is closed to the network by default (127.0.0.1; use an SSH tunnel, or \`waydesk-admin access lan|vpn\`); with the built-in VPN, UDP 51820 is the only port to open. Settings in \`/etc/default/waydesk\`; \`apt upgrade\` updates it.
>
> **AI involvement**: Most of the code, the documentation and the website were written with Claude (Anthropic, via Claude Code), working from my direction. I decide what gets built, review the changes, and test them on real servers. I'm also running it in my homelab.
>
> Feedback on the security model and on what you'd need before running it for a team is most welcome.

---

> **Free_Sympathy_1377**（1 分） · 2026-10-29T11:32:01+08:00　
> Project Name: DockShift
>
> Repo/Website Link: [https://dockshift.org/](https://dockshift.org/)
>
> Description: A fast, zero-backend, pure client-side bi-directional converter between docker run commands and docker-compose.yml configurations. Existing tools often only support one-way conversion (run -> compose) or transmit environment configurations to a remote server. DockShift solves this by running 100% in-browser via Vanilla JS AST parsing, ensuring sensitive credentials and volume mappings never leave your machine. It also supports viewing the JSON AST tree and generating AI Prompt Skills for Cursor/Claude.
>
> Deployment: Web app hosted on Cloudflare Pages, completely client-side and free. You can use it instantly in any modern browser without installation: [https://dockshift.org/](https://dockshift.org/) (Dedicated standalone views at /run-to-compose/ and /compose-to-run/).
>
> AI Involvement: The core AST parsing and bidirectional conversion engine is written in pure native JavaScript without AI runtime dependencies. Built-in features include an AI Prompt template generator to help users ask LLMs to optimize their Compose stacks.

---

> **G0ldBull3tZ**（2 分） · 2026-10-29T18:52:15+08:00　
> Hey r/selfhosted! 👋
>
> Like many of you, I love **Watcharr** for tracking movies, TV shows, and video games without relying on third-party cloud trackers. However, as my backlog and homelab grew, I really wanted deeper video game tracking, faster navigation, visual analytics, and native mobile gesture controls.
>
> # 🤖 Full Transparency: Built & Pair-Programmed with AI
>
> To be completely upfront: **I built this enhanced fork using modern AI coding agents.**
> I guided the architecture, defined the feature specifications, and supervised every step, while AI assisted in implementing the Go backend routines, Svelte 5 frontend components, and comprehensive test suites (`go test` / `go vet` passes 100%). Every database schema change and API endpoint was strictly verified to ensure **100% backward compatibility** with upstream Watcharr.
>
> 👉 **GitHub Repository:** [https://github.com/GoldBull3t/Watcharr](https://github.com/GoldBull3t/Watcharr)
> 🐳 **Docker Image:** [`ghcr.io/goldbull3t/watcharr:latest`](http://ghcr.io/goldbull3t/watcharr:latest)
>
> # 🚀 What's New & Why Check Out this Fork?
>
> # 🎮 Gaming 2.0 Tracker
>
> * **Hours Played Counter:** Stepper buttons (±1h\\pm 1\\text{h}±1h, ±5h\\pm 5\\text{h}±5h) or direct manual entry.
> * **Platform Tagging:** PC, PlayStation, Xbox, Switch, Steam Deck, Retro, etc.
> * **4 Completion Modes:** Track *Main Story*, *Main + Extras*, *100% Completionist*, or *Dropped*.
> * **Time-to-Beat (HLTB) Progress Bar:** Real-time visual comparison of your hours played vs. community averages.
>
> # 🎛️ Modern & Streamlined Command Bar
>
> * Restructured status tabs down to the 4 essential states (`All`, `Watching`, `Planned`, `Completed`) with a compact `+ More ▾` dropdown for secondary states.
> * **✨ Discover Menu:** Unified dropdown for *Watch Together*, *Franchises / Sagas*, and the new *Smart Roulette*.
> * Auto-expanding library search input with debounced querying.
> * Reduced bar width requirement from \~1530px down to \~860px (zero horizontal clipping).
>
> # 🎬 1-Click Quick Trailers
>
> * Play official trailers directly in a clean, non-intrusive modal lightbox (`youtube-nocookie.com`) right from any poster hover or tap without navigating to the details page.
>
> # 📊 Visual Analytics & "Watcharr Wrapped"
>
> * **Lifetime Highlight Card:** Total days/hours watched, gaming hours logged, completed titles, and average score.
> * **Milestone Badges:** Dynamic achievements (*Active Cinephile*, *Binge Master*, *Veteran Gamer*, *Discerning Critic*, *Master Collector*).
> * **Interactive SVG Donut Chart:** Zero-dependency genre distribution breakdown with slice hover inspection.
> * **Top Studios & Game Developers:** Track your most-watched networks (HBO, Netflix, etc.) and favorite game creators (Nintendo, FromSoftware, etc.).
>
> # 📱 Mobile PWA Gestures & Haptics
>
> * **Swipe Right** on any card →\\rightarrow→ Instantly mark as **Completed** (with green badge & tactile haptic vibration).
> * **Swipe Left** on any card →\\rightarrow→ Instantly queue to **Planned** (with blue badge & tactile haptic vibration).
> * Direction-aware detection so normal vertical scrolling is never interrupted.
>
> # 📺 "Up Next" Rail & Smart Roulette
>
> * **Up Next Rail:** 16:9 widescreen still backdrop rail showing the exact next unwatched episode across all your in-progress series with 1-click watched toggles.
> * **Smart Watchlist Roulette:** Interactive picker to randomly draw something from your backlog filtered by duration (≤90min\\le 90\\text{min}≤90min, ≤120min\\le 120\\text{min}≤120min), media type, or rating.
> * **Cancellation & Cliffhanger Warnings:** Badges warning you if a show was cancelled abruptly.
>
> # ⚡ Extreme Backend Performance & Zero-Downtime Backups
>
> * **Ultra-Low Memory:** Idles at just **\~23 MB of RAM** under Docker.
> * **Multi-Database:** Native support for PostgreSQL, MySQL, or calibrated SQLite (WAL mode + 16MB memory cache).
> * **Automated Gzip Backups:** Configurable background scheduler (12h, 24h, 7 days) with automated retention policies and 1-click restore.
> * **Homelab Integrations:** Outbound webhooks (Discord, Slack, Home Assistant, Ntfy), Overseerr / Jellyseerr 1-click requests, and native Emby webhook ingestion.
>
> # 🛡️ 100% Drop-In Replacement (Zero Migration Headaches)
>
> All database entities, JSON endpoints, and API contracts are identical to upstream Watcharr. If you are already running Watcharr, simply update your Docker image tag to:
>
>     yamlservices:
>       watcharr:
>         image: ghcr.io/goldbull3t/watcharr:latest
>         container_name: watcharr
>         restart: unless-stopped
>         ports:
>           - "3077:3077"
>         volumes:
>           - ./data:/data
>
> # 💬 Community & Feedback
>
> Since this was developed with AI assistance, I would especially love your feedback, code reviews, or bug reports to see how well it runs in different homelab environments!
>
> Check out the repo, give it a star ⭐ if you find it useful, and feel free to open an issue or discussion on GitHub:
> 👉 [**https://github.com/GoldBull3t/Watcharr**](https://github.com/GoldBull3t/Watcharr)

---

> **JohnPerformante**（1 分） · 2026-10-29T18:56:22+08:00　
> * **Project Name:** Obelisk
>
> **Repo/Website Link:** [https://github.com/amrelsawalhi/obelisk](https://github.com/amrelsawalhi/obelisk)
>
> **Description:** Obelisk is an open-source, all-in-one local data platform and control plane designed to run a complete modern data stack on a single machine, VM, or home server with zero cloud dependencies and no egress bills.
>
> * **The Problem:** Modern data workflows usually require stitching together 4–6 different cloud SaaS tools (Fivetran, Snowflake/Databricks, dbt Cloud, Airflow, Hex) or hosting heavy, memory-hungry distributed clusters (Spark, Trino) that overwhelm a homelab.
> * **What it does:** Obelisk ingests data from your databases, stores it as local Snappy Parquet files, and queries it in-process using DuckDB. It packages ingestion, transformation, orchestration, and exploratory notebooks into a single, cohesive web UI.
> * **Key Features:**
>    * **In-process DuckDB OLAP:** Vectorized SQL executed directly over local Parquet files.
>    * **DuckLake Table Format:** ACID transactions and table catalog backed by an embedded SQLite metadata store (`catalog.sqlite`) with snapshot history and time-travel.
>    * **Cross-Source Federation:** Attaches live external databases (PostgreSQL, MySQL, MongoDB) and HTTP REST/CSV feeds dynamically so you can join external databases directly with lakehouse Parquet in one query.
>    * **Visual DAG Orchestrator:** Canvas for wiring Python scripts, dbt runs, raw SQL, and sub-pipelines with conditional edges (`success`, `failure`, `skipped`) and retry policies.
>    * **dbt Studio:** In-browser Jinja SQL editing, compiled query preview, DAG model lineage, and 50-row instant data previews.
>    * **Reactive Notebooks:** Integrated Marimo notebooks saved directly to git as plain `.py` files and powered by the built-in `obelisk` Python SDK.
>    * **Scripts Studio:** Environment for authoring and running Python tasks and data quality gates with live streaming logs.
>    * **Hardware-Aware:** Built-in memory caps per concurrency slot, spill-to-disk guards for queries, and container management.
> * **Benefit to Users:** Complete data privacy and sovereignty, zero SaaS subscriptions, single-binary speed on NVMe drives, and the ability to process multi-million-row analytical workloads without a cluster.
>
> **Deployment:** Obelisk is released in public beta and available on GitHub with documentation in the [`README.md`](http://README.md) and `docs/configuration.md`.
>
> * **Single-command local launch:**
>    * Windows: `run_obelisk.bat`
>    * Linux / macOS / WSL: `bash run_obelisk.sh`
> * **Docker:** A complete `docker-compose.yml` is included in the root directory for self-hosted container deployments (runs API on `:8000`, UI on `:5173`, with optional Caddy gateway on `:80`).
>
> **AI Involvement:** Heavy. The vast majority of the frontend (React/Tailwind) and backend (FastAPI/DuckDB integration) code was written by AI. I designed the architecture, tested the workflows against real databases, and debugged the edge cases, but AI wrote most of the actual code.

---

> **aarondyck**（1 分） · 2026-10-29T23:06:35+08:00　
> * **Project Name:** Smart Transcode
> * **Repo/Website Link:** [https://smart-transcode.aarondyck.ca](https://smart-transcode.aarondyck.ca/) (downloads, documentation and screenshots). Support and issues: [https://github.com/aarondyck/smarttranscode](https://github.com/aarondyck/smarttranscode). That repository holds no source code: the project is source-available, not open source.
> * **Description:** Smart Transcode shrinks a video and audio library from a web page, using your GPU (NVIDIA NVENC, Intel Quick Sync / VA-API, AMD VA-API) or the CPU. It solves the problem of a library full of files that are bigger than they need to be.
>    * Video: a folder tree where you tick files, see the estimated saving and press Convert. Encodes to HEVC (default), H.264 or AV1. Files that are already efficient are skipped, every result is verified before it replaces the original, and a file that comes out larger is discarded.
>    * Audio: convert tracks to AAC, E-AC-3, Opus, FLAC and others, and drop the tracks you don't want. Select by language, track number or name pattern, leave certain codecs untouched, and use a Save Space Wizard. Optional `.orig` backups for audio.
>    * A real queue (pause, resume, add to a running queue), History with before and after sizes, a Savings Explorer, optional folder watching with named profiles, Sonarr/Radarr integration, optional multi-user login.
>    * One service and one web page, with no plugins or flows to build. It is a focused alternative to general-purpose tools like Tdarr and Unmanic. No telemetry; its only outside connections are to Sonarr and Radarr, if you set them up.
>    * Free for personal and internal use. Closed licence, but the Python and JavaScript source is readable.
> * **Deployment:** Released as version 1.0 with documentation for each method at [https://smart-transcode.aarondyck.ca/install](https://smart-transcode.aarondyck.ca/install).
>    * Docker: image `aarondyck/smart-transcode` on Docker Hub, with ready-made compose files for NVIDIA, Intel, AMD and CPU-only, and PUID/PGID support.
>    * Podman: documented, with its own guide for GPU passthrough and rootless permissions.
>    * Linux service: a downloadable package with an installer (`sudo ./install.sh --media /srv/media`), running as a systemd unit.
>    * Please note that I've only tested the Linux service on real hardware. The Docker and Podman paths are built and documented but not yet run on real hardware, so I'm looking for testers and feedback.
> * **AI Involvement:** Generative AI was used to assist in the development of this application. The front end is entirely AI. Polish and bug fixes by Claude Code.

---

> **saiyam-jain-dev**（1 分） · 2026-10-30T00:08:47+08:00　
> Project: Paper PDF - 100% Local-First Vector PDF Reader and In-Place Editor
>
> Live Demo: [https://saiyam-jain-dev.github.io/pdf-reader-viewer-rea/](https://saiyam-jain-dev.github.io/pdf-reader-viewer-rea/)
>
> GitHub (MIT): [https://github.com/saiyam-jain-dev/pdf-reader-viewer-rea](https://github.com/saiyam-jain-dev/pdf-reader-viewer-rea)
>
> Why I built it:
>
> I got tired of online PDF tools charging subscriptions, requiring signups, and uploading sensitive legal, financial, and personal documents to remote cloud servers just to edit a few lines of text.
>
> Paper PDF is completely local-first and client-side. Your documents are parsed and edited entirely inside browser memory and never touch any remote backend. Because it is a purely static web app, you can easily host it on your own server (Nginx, Caddy, Apache, or a simple Docker container).
>
> Key Features:
>
> \- In-place vector text editing: Preserves existing font families, weights, colors, and coordinates directly on the vector canvas so edits look native.
>
> \- Client-side OCR: Integrated Tesseract.js via WebAssembly to parse scanned docs directly on your machine with zero server compute.
>
> \- 100% Private: Works completely offline once loaded with zero telemetry or network calls.
>
> \- Lossless vector export: Clean PDF generation without rasterization, compression loss, or watermarks.
>
> \- Signatures and Annotations: Place signatures, highlights, and annotations directly on the pages.
>
> Tech Stack:
>
> React 18, Vite, PDF.js, pdf-lib, Tesseract.js (Wasm).
>
> I would love to get feedback from the self-hosted community on rendering performance, font handling, and whether you would like an official lightweight Dockerfile/image for running this on your home servers!

---

> **lorenzoao1995**（1 分） · 2026-10-30T00:41:15+08:00　
> **Project Name: Amberwave**
>
> **Repo/Website Link:** [https://github.com/lfrank95/amberwave](https://github.com/lfrank95/amberwave) (AGPL-3.0 · public beta 0.9.1-beta.1)
>
> **Description:**
>
> One app instead of five: your music library, bit-perfect playback, effects, VST3, per-channel routing and remote control – no virtual cables, no driver hacks. My goal is to make listening to music on your PC an \*experience\* again, away from minimalist UIs where the album covers are the only colour on screen.
>
> \- Self-hosted server + installable web app (PWA) + Windows client with bit-perfect WASAPI/ASIO output
>
> \- Every device can remote-control every other one (phone → PC, PC → living-room client); DLNA/UPnP and Google Cast output
>
> \- MusicBrainz matching with editions and full credits (producers, session musicians), AcoustID for untagged files
>
> \- At home the original files, on the go Opus streaming – via Cloudflare Tunnel, Tailscale or your own reverse proxy
>
> \- Family accounts with approval and expiry, shared playlists, radios, gapless playback, loudness normalisation
>
> \- Effects rack (tube, transformer, tape, room reverb/5.1 upmix, EQ), VST3 plug-ins, output routing matrix with per-channel EQ
>
> \- Your music folder is read-only by default; no telemetry
>
> DSP effects, VST3, ASIO and the routing matrix are planned as paid Pro features later – during the beta everything is free for everyone.
>
> **Deployment:**
>
> Docker Compose (app + MariaDB), image \`ghcr.io/lfrank95/amberwave:beta\` (amd64). Step-by-step guides for Unraid (Compose Manager), Synology and plain Docker in the README; a setup assistant handles database, admin account and the first scan. Windows installer under Releases (not code-signed yet). An all-in-one container for Unraid Community Apps is next.
>
> **AI Involvement:**
>
> I'm an audio/PA guy, not a programmer. Amberwave was built with heavy AI assistance (Claude): I designed the features, made the decisions and tested everything on my own setup and hardware; most of the code was written by AI. An independent AI security review was done before the beta.
>
> Feedback very welcome – bugs on GitHub, ideas and questions in r/Amberwave. Screenshots are in the README.

---

> **zhoorta**（1 分） · 2026-10-30T02:44:36+08:00　
> Update: I wrote up the capacity and GPU measurements behind this. Up to 24 active users on one server, with and without a GPU. The short version is that memory decides how many fit, and the GPU cut CPU use but didn't fit more people: [https://dev.to/zhoorta/does-a-gpu-let-you-fit-more-users-on-a-shared-linux-desktop-server-i-measured-it-4k7f](https://dev.to/zhoorta/does-a-gpu-let-you-fit-more-users-on-a-shared-linux-desktop-server-i-measured-it-4k7f)
>
> If you try Waydesk on your own hardware and your numbers differ, I'd like to hear. The testing checklist is here: [https://github.com/zhoorta/waydesk/issues/1](https://github.com/zhoorta/waydesk/issues/1)

## 关联链接

- https://www.reddit.com/r/selfhosted/search/?q=

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
