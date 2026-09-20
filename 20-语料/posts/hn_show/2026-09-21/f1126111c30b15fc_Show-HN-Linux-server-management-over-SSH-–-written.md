---
type: "corpus"
item_id: "f1126111c30b15fc"
title: "Show HN: Linux server management over SSH – written in Rust and Tauri"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49509679"
project_url: "https://serverbox.stupidlabs.lol/"
author: "freakynit"
published_at: "2026-08-31T13:39:43Z"
captured_at: "2026-09-21T03:11:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_freakynit
  - story_49509679
  - show_hn
metrics: {"points": 49, "comments": 52, "engagement_velocity": 49}
comments_count: 52
comments_total: 52
discovered_via: "hn:show_hn:52d"
---

# Show HN: Linux server management over SSH – written in Rust and Tauri

> [!info] 一句话导读
> Lightweight app for Linux server management over SSH.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49509679>
> 指标：点赞=49 · 评论=52 · engagement_velocity=49
> 作者：freakynit　|　发布：2026-08-31T13:39:43Z
> 项目链接：<https://serverbox.stupidlabs.lol/>
> 采集：2026-09-21T03:11:22+08:00　|　id：`f1126111c30b15fc`

## 正文

S Serverbox
Features
 Download
 FAQ
 GitHub
Download
Lightweight app for Linux server management over SSH.
Written in Rust+Tauri , Serverbox uses SSH to give you live dashboards, a real terminal,
 file management, Docker, services, cron, users and firewalls. Connect over the credentials
 you already have. Install nothing on your servers.
Download Serverbox ↓
 See what it does
The server overview — every machine's vitals the moment you connect.
∅ Agentless by design Nothing to install, update or babysit on your servers.
🔒 Your secrets stay local Credentials live in an encrypted vault on your machine.
🐧 Respects your distro Debian, Ubuntu, Fedora, RHEL, openSUSE, Arch, Alpine and friends.
🧘 Built for calm ops Fast, readable UI — no beep-and-flash hacker aesthetics.
Features
Everything you do over SSH today — with a face on it.
Serverbox speaks plain SSH to your machines. Whatever works in your terminal works in Serverbox, presented as tools you can actually click.
Connect & organize
▦ Multi-server workspace
 Save as many servers as you need. Group them, tag them, mark favorites, and find anything instantly with server search — including your own private notes for each machine.
❐ Browser-style tabs
 Open multiple workspaces side by side, drag to reorder, rename tabs, and keep several tabs on the same server for different tasks. Terminal sessions stay alive while you switch.
⇄ Bastions & jump hosts
 Reach machines behind bastions with full jump-host chaining. Every hop authenticates independently and verifies host keys, so nested networks just work.
🔑 Password or key auth
 Use passwords or private keys. Serverbox discovers your existing SSH keys and can import hosts straight from your ~/.ssh/config — no re-typing what you already have.
🔐 Encrypted credential vault
 Passwords, passphrases and sudo secrets are encrypted locally behind a master password. Resetting it is explicit and clearly warned as unrecoverable — by design.
✓ Host-key verification
 Server fingerprints are reviewed on first contact and re-checked on every connection. A changed key is never silently accepted.
Monitor & understand
◉ Live server overview
 CPU, memory, swap, disks, network interfaces, uptime and load — a clean snapshot of every box the moment you connect.
≔ Processes
 See what's eating CPU and RAM, sort and search, then stop a runaway process gracefully — or force-kill it when it won't listen.
⚙ Services
 Start, stop, restart, reload, enable or disable services, with logs and details one click away. Works with systemd — and without it.
▤ Disk usage explorer
 Find what's filling the disk: largest files and folders, per-mount usage, inode pressure, container disk usage, and a breakdown of log directories.
☰ Unified logs
 Journals, system logs, container logs, Compose services or any raw file — one viewer with search, severity filters and live streaming you can pause.
⇋ Network view
 Listening ports and active connections at a glance, so you always know what a server is exposing and who it's talking to.
Terminal & files
❯ A real terminal
 A proper interactive terminal with tabs, copy/paste, sudo and reconnect. Sessions survive hiccups and wait for you, not the other way around.
⌘ Saved commands
 Keep your frequently-typed commands one click away — restart recipes, health checks, log greps — per server or across them.
🗂 File manager
 Browse, upload, download, edit and organize files with permissions and ownership visible. Big transfers can be cancelled mid-flight — cleanly, without leaving half-written files behind.
✎ Quick edits
 Open a config file, fix a line, save it back — no vi gymnastics required (though the terminal is always there if you miss them).
🕳 SSH tunnels
 Save and run local, remote and SOCKS5 tunnels as first-class citizens. Tunnels are tightly bound to their server connection and stop when its credentials or connectivity change.
🗒 Server notes
 "Reset MySQL via runbook #4", "billing box — don't reboot". Notes live with each server profile and show up in search when you need them.
Containers & Compose
🐳 Container control
 Containers, images, volumes and networks with live resource usage. Start, stop, inspect, pull and create — across Docker and Podman.
❯ Container shells
 Jump straight into a running container with a dedicated shell. Shell-less and minimal images are detected and handled honestly instead of failing cryptically.
⧉ Docker Compose projects
 Your Compose projects are discovered automatically: services, dependencies, environment variable names, scaling, rebuilds and pulls — with logs per service.
▥ Container logs & stats
 Follow container output live, filter by severity, and watch CPU and memory per container — all in the same log viewer as everything else.
Administration
⏰ Cron manager
 Add, edit, pause and delete your cron jobs with human-readable schedules and next-run previews. System cron files are shown read-only, so nothing gets clobbered.
📦 Package management
 Full package management on Debian and Ubuntu: search, inspect, update, install, remove and upgrade. Update and security status is understood across the other major distro families too.
👥 Users & groups
 Create and manage users and groups, change shells and memberships, lock accounts, and reset passwords — with clear warnings where it matters.
🛡 Firewall management
 See your UFW or firewalld rules and make guarded changes. Risky actions require explicit confirmation, and your SSH port is your responsibility — Serverbox reminds you.
🗝 Authorized keys
 Review and manage a server's authorized SSH keys with fingerprints, and get lockout warnings before you lock yourself out.
⚕ Health & maintenance
 Pending updates, security posture, reboot requirements and runtime versions — with sensible one-click maintenance actions for the routine stuff.
Works with what you run
🐧 Every major distro family
 Debian/Ubuntu, Fedora/RHEL, openSUSE/SUSE, Arch and Alpine are understood on their own terms — Serverbox adapts to each system's available tools.
📦 Minimal & containerized hosts
 Tiny VMs, LXC containers and stripped-down boxes stay usable. Anything unavailable is explained plainly, never a cryptic error code.
🧭 Honest about limits
 If a server doesn't have systemd, Docker, or a package manager, those tools stay out of your way. What you see is what the machine can actually do.
Download
Free. Native. Six ways.
Serverbox runs on your desktop and manages your servers over SSH. Pick your platform — no account, no telemetry wall, no upsell.
macOS
Intel & Apple Silicon
Apple Silicon .dmg .tar.gz
Intel .dmg .tar.gz
Windows
x86_64 & ARM64
x86_64 .exe .msi
ARM64 .exe .msi
Linux
x86_64 & ARM64
x86_64 .AppImage .deb .rpm
ARM64 .AppImage .deb .rpm
Important · before you install
 Security warnings are expected for this release.
Serverbox is not code-signed yet (the macOS build is ad-hoc signed). Your browser or operating
 system may therefore show a warning even when the download completed correctly. Don't worry —
 the app is safe. Just make sure to download Serverbox from this official website only.
On Windows
Your browser may say the file is not commonly downloaded; choose Keep or
 Download anyway . If Windows SmartScreen says it protected your PC or does not
 recognize the publisher, choose More info , then Run anyway .
On macOS
macOS may say Serverbox is “damaged,” is from an unidentified developer, or cannot be
 verified. After downloading:
Move Serverbox to your Applications folder.
Open Applications in Finder, right-click Serverbox, and choose Open .
Choose Open again in the warning dialog.
You normally need to approve it only once for that installed copy.
FAQ
Fair questions.
Do I need to install anything on my servers?
 No. Serverbox is fully agentless — it manages everything over the SSH connection you already use. If you can SSH into a box, Serverbox can manage it.
Where are my passwords and keys stored?
 On your machine, in an encrypted local vault protected by a master password. Nothing is uploaded, synced or phoned home.
Which Linux distributions are supported?
 Debian, Ubuntu, Fedora, RHEL, openSUSE, SUSE, Arch and Alpine — including minimal and containerized systems. Serverbox detects what each host actually offers and adapts, instead of assuming everything is Debian with systemd.
Can I reach servers behind a bastion?
 Yes. Pick another saved server as a bastion, and chains of jump hosts work too — every hop with its own credentials and host-key verification.
Does it work with Docker and Podman?
 Both. Containers, images, volumes, networks, exec shells, logs and resource usage — plus automatic discovery of Docker Compose projects across the Compose plugin, standalone Compose and Podman Compose.
Is Serverbox free?
 Yes. It's an indie project — download it, use it, manage your fleet.
S
 Serverbox
 — the desktop control panel for Linux servers.
Features
 Download
 FAQ
 GitHub
 [email protected]

## 评论（52/52）

> **ahriad** · 2026-08-31T14:50:08.000Z　
> This is exactly the gap I needed filled, a proper desktop panel that manages my Linux servers over SSH without installing anything on them.Is it open source?

---

> **e12e** · 2026-08-31T14:58:30.000Z　
> Potentially interesting - of it is at a minimum source-availble - preferably FOSS?I assume it is vibe-coded, so would need a pretty thorough review before considering using it.License and source availability not being on the page/faq suggest this is just a hobby project, I guess?

---

> **seemaze** · 2026-08-31T14:58:52.000Z　
> What's the business model - and what guarantees are provided that Serverbox[0] won't rug pull after a seed round from Dillon-Edwards[1]?[0]https://stupidlabs.lol[1]https://clownpenisf.art

---

> **gguingff** · 2026-08-31T15:02:29.000Z　
> yikes, no thanks.

---

> **ramon156** · 2026-08-31T15:04:58.000Z　
> Looks like TRUENAS if it was single-prompted. Also how will it know what my server runs if I install nothing on it? will my server just expose all information? I'm a bit confused why this was a design choice.

---

> **_def** · 2026-08-31T15:20:43.000Z　
> Is this shipping wasm openssh or how does it work?edit: nvm, for some reason I thought it runs in the browser.

---

> **kushalpandya** · 2026-08-31T15:37:21.000Z　
> The macOS installer is not notarized, and while adding an exception in Gatekeeper exists, not everyone would be willing to do that, especially currently when even the app source is unavailable.

---

> **whalesalad** · 2026-08-31T15:45:07.000Z　
> All of these "written in rust" ai-slop tools lately. Means absolutely nothing, really.

---

> **vablings** · 2026-08-31T15:46:19.000Z　
> Pretty cool for those who are not running something like TrueNAS/FreeNAS/Proxmox. But then the question is why are you not. Even for MacOS im pretty sure you can glue up a raw bare metal box to Proxmox these days with Proxmox Datacenter Manager

---

> **ealhad** · 2026-08-31T15:46:44.000Z　
> I mean yeah sure, I'll give SSH access to a blackbox.
> "Don't worry — the app is safe."

---

> **hn_submit** · 2026-08-31T16:00:02.000Z　
> It's free but not open-source?

---

> **ubittibu** · 2026-08-31T16:00:36.000Z　
> Every time I connect to my server I receive a Delivery Status Notification (Failure) email from my gmail address as if it tries to use my phpmailer to send an email to testing@example.comedit: the email comes from my website, when I connect a new user is created in my website with random name and that email address..DOESN’T SEEM SAFE AT ALL!

---

> **rewgs** · 2026-08-31T16:07:55.000Z　
> Clearly vibe-coded. Hard pass.

---

> **omidmash** · 2026-08-31T16:20:47.000Z　
> Are you guys really letting a (as of now) non FOSS, presumably vibecoded app have access to your servers, presumably as root, as most people don't follow best practices?

---

> **marcosscriven** · 2026-08-31T16:27:06.000Z　
> You have a never ending stream of show HN. It becomes meaningless.Show HN: Linux server management over SSH – written in Rust and Tauri2 hoursShow HN: The wanderer – cozy weekend game with no objective14 daysShow HN: Feature-packed 6MB Rust+Tauri free bookmarking app16 daysShow HN: HN-jobs aggregator – updated in real-time27 daysShow HN: One no-subscriptions online search for all your agent needs30 daysShow HN: 100% Free Indian Railways API35 daysShow HN: Xkcd Search45 daysShow HN: A calculator CLI to help your agents perform calculations accurately55 daysShow HN: Hacker-News Jobs57 daysShow HN: Hacker-News Buddies58 daysShow HN: HTTPS://HN-Jobs.com59 daysShow HN: JerrySniffs – MCP Server (and API’s) for web and social media search75 daysShow HN: Give This Markdown to Your Coding Agent Before Publishing to NPM3 monthsShow HN: Nano-RAG – Agentic multi-hog retrieval without graph database3 monthsShow HN: Chat with UFO Files3 months

---

> **Kuyawa** · 2026-08-31T16:40:18.000Z　
> Beautiful, I have a fetish for beautiful software so here goes my upvote ^I believe more Rust/Tauri apps will flood the market as that's the best combo right now for desktop apps in universal knowledge reusability for those who come from the web world HTML, CSS, JS. Simplicity and portablilityJust downloaded it and at 8MB is a thing of joy to see apps small again

---

> **thenews** · 2026-08-31T17:14:54.000Z　
> OMG cool app, let me share my ip and cert

---

> **sgt** · 2026-08-31T17:15:30.000Z　
> Only problem of course is that it's unlikely that this even exists in 5 years.

---

> **m4xp** · 2026-08-31T19:37:30.000Z　
> Man as someone thar was on the verge of going all in on programming is so demoralizing to see how easy it is to release pure SLOP nowdays

---

> **sharts** · 2026-09-01T05:54:41.000Z　
> lost me at tauri

---

> **freakynit** · 2026-09-02T06:33:49.000Z　
> Source code: https://github.com/freakynit/serverbox-app

---

> **freakynit** · 2026-08-31T15:06:06.000Z　
> Thank you...Source code will be released day after tomorrow. I will add a comment in this thread itself, as well as update the site with a link to Github.

---

> **freakynit** · 2026-08-31T15:05:52.000Z　
> Source code will be released day after tomorrow. I will add a comment in this thread itself, as well as update the site with a link to Github.

---

> **freakynit** · 2026-08-31T15:04:45.000Z　
> No financial incentive in mind or planned... I was building it for myself... then, spent a few days extra polishing it so others can use it as well.

---

> **freakynit** · 2026-08-31T15:12:11.000Z　
> I just heard of TrueNAS for the first time in my life... So, checked google images.. there is some similarity for sure.It detects the server OS "after SSH authentication" by running a small POSIX-shell probe.It will not automatically expose "all information". It can access only what the SSH account can access.

---

> **freakynit** · 2026-08-31T15:55:15.000Z　
> Apple charges $99/year to be able to notarize a app. Plus, it has one years long bug that any random Apple developer account can get stuck in, and then, you just can't get it notarized. Have a look at this thread: https://github.com/electron/notarize/issues/205I do agree that notarizing it would make installing much easier.Also, source code is coming day after tomorrow.

---

> **freakynit** · 2026-08-31T15:55:37.000Z　
> Source code will be released day after tomorrow. I will add a comment in this thread itself, as well as update the site with a link to Github.

---

> **freakynit** · 2026-08-31T16:07:41.000Z　
> Source code will be released day after tomorrow. I will add a comment in this thread itself, as well as update the site with a link to Github.

---

> **dewey** · 2026-08-31T16:24:10.000Z　
> Most people already run software like that on their computer, even if it's just your coding harness that could just as easily run ssh and use your keys in ~/.ssh to connect to your servers. In my case I'd get a permission prompt from 1Password as I have my keys in there, but with all the prompts that a modern macOS throws at you the chances of it getting approved mistakenly are not zero.I'd not run OPs software either though.

---

> **marcosscriven** · 2026-08-31T16:27:44.000Z　
> Absolutely not.

---

> **edoceo** · 2026-08-31T16:31:03.000Z　
> Nope, cfEngine FTW!

---

> **ahriad** · 2026-08-31T16:35:54.000Z　
> I only tested it on WSL locally, there is bo way im connecting it to a live server without seeing the sourcecode.

---

> **hoppp** · 2026-08-31T16:40:58.000Z　
> It's from stupidlabs.lol
> Made for stupid people?

---

> **Arrowmaster** · 2026-08-31T16:54:28.000Z　
> The choice of Tauri for a Linux app using AppImage is a dead giveaway they have no clue what they are doing.

---

> **freakynit** · 2026-08-31T16:38:30.000Z　
> I do. I love to build things, though these things are not that meaningful yet as I want them to be. Most of these (except last 3 and that 'A calculator CLI...') are being actively used by many.But I should not have shared a single `show hn` more than once.. that I will take care of going ahead.

---

> **hoppp** · 2026-08-31T16:43:26.000Z　
> So its pretty much abandoneware?

---

> **Arrowmaster** · 2026-08-31T17:00:56.000Z　
> Won't happen until Tauri can treat Linux as a first class platform. Which they cannot do because of architectural design and library choices.

---

> **ahriad** · 2026-08-31T15:18:30.000Z　
> Thank you, I tried it, so far working great. One small thing I hit: when I tried connecting to a server I'd never connected to before, it refused at first with no clear error. I had to SSH in from my terminal once to accept the host key signature, and then it worked fine. Minor, but thought I'd pass it along. Great work!

---

> **seemaze** · 2026-08-31T16:51:28.000Z　
> Thanks for the reply, did not expect a response.The initial inquiry was not in good faith, but a satirical critique of the project domain.

---

> **Arrowmaster** · 2026-08-31T16:56:40.000Z　
> Why not make this post the day after tomorrow then instead of today?

---

> **glitchcrab** · 2026-08-31T16:48:09.000Z　
> Anyone who gives an LLM unfettered access to their ssh keys/agent socket deserves what they get IMO. I sandbox Claude with my own bubblewrap-based script which denies it access to anything I deem unnecessary.

---

> **hn92726819** · 2026-08-31T18:16:42.000Z　
> Can you expand on that? The point of an appimage is so you don't have any dependencies or linking errors. Rust can still link to libraries, so that doesn't seem to be a weird pattern to me.Electron appimage would be weird though since it does all its bundling by itself

---

> **marcosscriven** · 2026-08-31T16:47:21.000Z　
> I think what I have trouble with is the lack of awareness. Anyone and everyone can do this now. It’s great. I do so myself at home, for myself.But what are you (and millions of others) actually adding here?

---

> **bigstrat2003** · 2026-08-31T17:15:37.000Z　
> If you truly love to build things, then actually build them, don't vibe code them.

---

> **Kuyawa** · 2026-08-31T19:25:50.000Z　
> Is there any webview control ready to use in linux? When I say Tauri it's just the webview control, used as a cargo package as "wry" in macos. I don't care about the framework itself, just the webview control. If that's the case then Rust/(stripped down WebView) is all we need to be honestEdit: Looks like the same "wry" package can be used in linuxhttps://github.com/tauri-apps/wry

---

> **freakynit** · 2026-08-31T15:21:46.000Z　
> Thank you for testing. I'll fix the issue.. tomorrow.. too tired as of now.

---

> **freakynit** · 2026-09-01T10:19:49.000Z　
> My choice

---

> **dewey** · 2026-08-31T16:55:48.000Z　
> There's many ways to shoot yourself into the foot, most things that run in your userspace can do evil things and it's not an LLM exclusive feature. Any npm package you install on your machine can put you in danger already if it executes some scripts.

---

> **Arrowmaster** · 2026-08-31T20:11:14.000Z　
> Sure. Tauri tries to claim its lighter than Electron by not including a full web browser in its runtime and instead using the system renderer. But Linux doesn't have a universal system renderer like Windows and Mac does so it uses Webkit2Gtk on Linux. Libwebkit is an absolute mess of a library. It hardcodes the path to /usr which doesn't work in AppImages resulting in this[1] hack of a fix that replaces `/usr` with `././`. This problem isn't unique to Tauri as I have seen apps using Wails copy this same trick to package their AppImages.Now the problem with libwebkit goes even deeper because Tauri uses libwebkit2gtk-4.1 after moving away from 4.0. When you build an AppImage you want to do it on the oldest possible distro you want to support because it will be built against GLIBC of that distro release. Due to how most devs release apps now, that means they compile against an Ubuntu LTS release because Ubuntu is the only option with Github Actions[2]. The first LTS version of Ubuntu with 4.1 is 22.04, so now by default you can expect every Tauri (and also probably Wails) AppImage to be built against GLIBC 2.36. But theres a bug in the interaction of older libwebkit2gtk and newer freetype that happens when you use an AppImage built on Ubuntu 22.04 on a newer distro. It crashes when displaying an emoji character. Freetype is one of the libraries you cannot include in an AppImage but you must include libwebkit2gtk, the solution is to use a newer libwebkit2gtk but thats only available in Ubuntu 24.04 and bumps the GLIBC to 2.39. Do you see how much of a mess this usage of libwebkit2gtk in an AppImage turns out to be.And moving beyond that, the Tauri devs has an absolute disdain for the AppImage format and treat it as a 2nd class platform as you can see in this[3] PR where AppImage developers tell the Tauri devs to update to newer tools instead of mirroring the old obsolete broken tool that was taken down. This also meant that AppImages created by Tauri's build tools depended on libfuse2 being installed on the system while newer AppImages using the type2-runtime do not anymore. I believe Tauri has finally moved forward and stopped doing this recently. Electon is no better on this and electron-builder uses an outdated hardcoded tool that makes bad AppImages that depend on libfuse2 too.I do like the AppImage format, but I do not believe anything that uses libwebkit2gtk-4.1 is fit to be distributed as an AppImage at this time. This means that Tauri (and by extension probably Wails, and some of these other NOT Electron frameworks) are not fit to be truly called cross platform. It does look like Tauri was making progress on Flatpak documentation so app developers could have a second cross distro packaging method. Ideally I think any framework that wants to label itself as cross platform should make it easy to package both AppImage and Flatpak and not run into the above libwebkit2gtk issues.[1][2]This is not entirely true, you can use a docker image inside the Github Actions Ubuntu VM or a sysroot but that is beyond even most expereinced app devs to setup.[3]

---

> **freakynit** · 2026-08-31T17:33:41.000Z　
> this is not vibe-coded... this is ai-assisted... also, i love building things.. using whatever that lets me build more efficiently.

---

> **Arrowmaster** · 2026-08-31T20:29:12.000Z　
> The README for wry under Platform Considerations suggests its not actually implementing the webview but just a wrapper that uses the correct one for each platform. The usage of WebKitGTK IS the problem that makes it second class on linux. I talked about this more in https://news.ycombinator.com/item?id=49514323

---

> **hn92726819** · 2026-09-01T15:55:40.000Z　
> Thank you for the detailed reply. I just recently started playing with Tauri, so I was not aware. I also heard that gtkwebview is slow as dirt. Sounds like verso support can't come quick enough.

## 导航

- 项目页：[[10-项目/serverbox.stupidlabs.lol_a5f0dea9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
