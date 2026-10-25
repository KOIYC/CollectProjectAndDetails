---
type: "corpus"
item_id: "1bd81c72d3a06c4a"
title: "Zync SSH workspace: SSH workspace for desktop (Windows, macOS, Linux): terminal, SFTP, port forwarding, custom themes Release [2.35.1]"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6nes4/zync_ssh_workspace_ssh_workspace_for_desktop/"
project_url: "https://github.com/zync-sh/zync"
author: "FDgajju22"
published_at: "2026-10-15T22:39:18+08:00"
captured_at: "2026-10-25T23:28:44+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (AI)
metrics: {"score": 21, "comments": 35, "upvote_ratio": 0.6666666666666666}
comments_count: 36
comments_total: 36
discovered_via: "reddit:14d+settle10"
---

# Zync SSH workspace: SSH workspace for desktop (Windows, macOS, Linux): terminal, SFTP, port forwarding, custom themes Release [2.35.1]

> [!info] 一句话导读
> I've been working on Zync, a desktop SSH workspace for Windows, macOS and Linux.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6nes4/zync_ssh_workspace_ssh_workspace_for_desktop/>
> 指标：得分=21 · 评论=35 · 赞踩比=0.6666666666666666
> 作者：FDgajju22　|　发布：2026-10-15T22:39:18+08:00
> 项目链接：<https://github.com/zync-sh/zync>
> 采集：2026-10-25T23:28:44+08:00　|　id：`1bd81c72d3a06c4a`

## 正文

Hi folks,

I've been working on Zync, a desktop SSH workspace for Windows, macOS and Linux.

Website: [https://zync.thesudoer.in](https://zync.thesudoer.in/)
GitHub: [https://github.com/zync-sh/zync](https://github.com/zync-sh/zync)

Zync is built for the everyday work of connecting to servers, checking logs, and moving files, without constantly switching tools:

* Terminal, SFTP browser, and port forwarding in one window
* Credentials stored locally in an encrypted vault, no account, no cloud sync
* Local shells and remote SSH sessions share the same workspace
* Jump hosts, SSH config import, and visual port forwarding (local, remote, SOCKS)
* Snippets, command palette, and session restore, pick up where you left off
* Optional encrypted backup to your own Google Drive
* A plugin marketplace for themes and plugins
* Runs fully on your desktop, light on resources

**Recent update (v2.35.1): make the workspace your own:**

* Custom color themes, including import/export of theme JSON files
* Renameable tabs and dockable panes
* A side navigation bar you can toggle
* Keyboard shortcuts are easier to discover and edit, including bindings that work while the terminal is focused

Update in action: [https://pub-f5d307b0347348988dccc997da10756a.r2.dev/2.35.1.mp4](https://pub-f5d307b0347348988dccc997da10756a.r2.dev/2.35.1.mp4)

Release notes: [https://github.com/zync-sh/zync/releases/tag/v2.35.1](https://github.com/zync-sh/zync/releases/tag/v2.35.1)

One transparency note: AI tools helped write parts of the code, but all design decisions, architecture, and code reviews go through me.

Would love feedback, especially from folks managing a bunch of homelab boxes.

## 评论（36/36）

> **asimovs-auditor**（1 分） · 2026-10-15T22:39:28+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **FDgajju22**（1 分） · 2026-10-15T22:53:11+08:00　
> AI tools helped write code,, things like boilerplate, utility functions, and drafting text. Every PR and change goes through my own review and testing before it ships. nothing lands in the app that I haven't verified myself.

---

> **rivolity**（12 分） · 2026-10-15T23:09:18+08:00　
> What is the diff with Termix ?

---

> **FDgajju22**（-9 分） · 2026-10-15T23:28:41+08:00　
> There’s definitely overlap: both offer SSH, file management, tunnels and plugins. Termix has a broader server-management focus, including self-hosted access, users, roles and sharing, alongside standalone desktop use.
>
> Zync focuses on a personal desktop workspace local terminals and SSH together, with particular attention to:
> Keyboard-driven workflows: editable primary and secondary shortcuts, conflict detection, and terminal-first or Zync-first priority.
> Workspace flexibility: rename, pin and organize tabs, split related views, or dock a pane while switching other tabs.
> Customization: interface colors, theme JSON import/export, navigation placement, and optional toolbar/status-bar controls.
>
> The goal is to make everyday SSH work comfortable without constantly reaching for menus or switching tools. Core use needs no account or Zync server, and encrypted Google Drive backup is optional.
>
> I haven’t personally used Termix yet, so I can’t give a fair hands-on comparison. The points above describe what I’m focusing on with Zync. I’ll definitely give it a try. you’re welcome to try Zync too, Thanks for mentioning it!

---

> **rivolity**（1 分） · 2026-10-15T23:51:44+08:00　
> Sorry dude, but if you haven't even used Termix yet, don't reach for Claude to vibe-code something similar without understanding what you're trying to compete with.
>
> I'm not against vibe coding, but what you're saying doesn't sound grounded in actual hands-on experience. 🪨
>
> We all have Docker on our machines, and Termix itself can be self-hosted locally via Docker. It takes just a few minutes to spin it up, so there's really no excuse not to try it before making comparisons.
>
> Use it, understand its strengths and weaknesses, identify what's missing, and then explain what Zync does differently and why someone should choose it over Termix.
>
> Right now, you're listing features as differentiators without having even tried the alternative. That's not a solid technical comparison; it's just assumptions.
>
> Build something because you understand the problem and have a clear vision of how to solve it better, not just because Claude can generate the code.

---

> **FDgajju22**（-1 分） · 2026-10-16T00:09:25+08:00　
> I wasn’t presenting a hands-on review or claiming Zync is better than Termix. You asked what the difference was, so I described Zync’s focus and explicitly said I haven’t used Termix.
>
> I’ve been building Zync for around 10 months, based on my experience with Termius, PuTTY and MobaXterm. I wanted core use without a login, local credential storage and optional encrypted backup to my own Google Drive. That’s the reason behind the project, not recreating Termix.
>
> I agree that overlapping features aren’t necessarily differentiators, and I could have worded that more clearly. But not having tried every alternative doesn’t mean the project lacks a purpose.

---

> **Bfox135**（-12 分） · 2026-10-16T00:46:46+08:00　
> What the hell kinda response is this? Get your head out of your ass. What's worse is this is an AI written response and you are judging him for coding with AI? Get a life dude.

---

> **Bfox135**（-10 分） · 2026-10-16T00:52:40+08:00　
> https://preview.redd.it/gqibzuqavnvh1.png?width=899&format=png&auto=webp&s=c0bfa61f4a18f082fd44edad942f584a793a9cbd
>
> PS. Not looking good for vibe coded termix.

---

> **rivolity**（3 分） · 2026-10-16T01:15:32+08:00　
> My friend you are new to this I think 💬 . . . .

---

> **Antony__24**（1 分） · 2026-10-16T02:48:32+08:00　
> Wonderful, really good job man!!!

---

> **FDgajju22**（1 分） · 2026-10-16T03:02:39+08:00　
> Thanks, really appreciate it
> If you get a chance to try zync, I’d love to hear your feedback :)

---

> **Antony__24**（0 分） · 2026-10-16T03:03:38+08:00　
> Tomorrow I’ll try it, now is night in Italy…

---

> **FDgajju22**（1 分） · 2026-10-16T03:12:11+08:00　
> Sure , no rush at all
> Good night...

---

> **tcfjr**（1 分） · 2026-10-16T06:40:30+08:00　
> Looks good.  I've been using OmnySSH and it works really well, but I'll give this a try.

---

> **greatcalzone**（2 分） · 2026-10-16T06:56:43+08:00　
> Just because you can't fathom typing four paragraphs by hand, doesn't mean  others have the same problem.
>
> I agree that some people have an over-reliance on AI these days, but what's even more infuriating are the people that go around and scream "AI!!!!!!!!!1111" to any text post over two sentences.
>
> I would much rather see more long and thoughtful posts that **could** be AI instead of this dogshit sentiment everywhere.

---

> **fernandops**（1 分） · 2026-10-16T07:04:04+08:00　
> With renameable tabs, keep the actual hostname and user visible somewhere that a custom label can’t hide. “Logs” could be a shell on staging or production. A persistent production badge or host label next to the prompt would help when several sessions are open.

---

> **FDgajju22**（1 分） · 2026-10-16T11:50:49+08:00　
> Good point, Renaming a tab shouldn’t hide which server you’re connected to. I’ll look into keeping the hostname and user clearly visible and adding an environment badge to help distinguish staging from production. Thanks for the suggestion

---

> **FDgajju22**（1 分） · 2026-10-16T12:02:04+08:00　
> Appreciate you giving Zync a try, and I’d love to hear what you think!

---

> **vortige-sven**（1 分） · 2026-10-16T15:18:40+08:00　
> I like it but what I straight up saw in a demo of yours: When pressing key combinations to open your sidebar, you should not send those combinations to the terminal. (e.g. \^b (ctrl+b)).

---

> **Joncallim**（1 分） · 2026-10-16T15:29:24+08:00　
> Do port forwards reconnect when you restore a workspace too? It’d be handy to see which ones reconnected and which need attention.

---

> **vortige-sven**（1 分） · 2026-10-16T15:56:21+08:00　
> I don't know Termix and the demo doesn't really answer what I think.
>
> Isn't Termix browser based and this app here a desktop app that you don't need to host somewhere?

---

> **vortige-sven**（2 分） · 2026-10-16T16:37:49+08:00　
> I just tested it and stopped quite quickly because I can't really use it for I use a CA for authorization. The server trusts my certificates through TrustedUserCAKeys.
>
> Example:
>
>     Host ssh.example.com
>         User testuser
>         IdentityFile ~/.ssh/id_ed25519
>         CertificateFile ~/.ssh/id_ed25519-cert.pub
>         IdentitiesOnly yes
>
> Doesn't work with Zync as you do not use the `CertificateFile`.  Thus my server denies me.

---

> **FDgajju22**（2 分） · 2026-10-16T16:59:26+08:00　
> Thanks for spotting that, The demo was recorded before the shortcut routing fix. Zync supports Terminal-first and Zync-first modes, but when an app shortcut is handled, it should never also reach the terminal. That protection is in 2.35.1. If you still see it there, please let me know!

---

> **FDgajju22**（1 分） · 2026-10-16T17:06:40+08:00　
> Yes, you need to Check this **Auto-start when connection opens** for each forward you want to start automatically. After restoring your workspace and reconnecting to the host, those forwards will start automatically. You can check their status in the Port Forwarding pane
>
> https://preview.redd.it/1ivaisauosvh1.png?width=592&format=png&auto=webp&s=15fc04bd6b5a4c24ef2938880c7a2fbb48bda6e1

---

> **FDgajju22**（0 分） · 2026-10-16T17:12:45+08:00　
> Thanks for testing and sharing your config! right, Zync currently reads **IdentityFile**  but doesn’t use **CertificateFile** or present the signed certificate during authentication. Your CA-based setup isn’t supported yet. This needs work in both config import and authentication. I’ll look into adding it. Thanks for highlighting the gap

---

> **vortige-sven**（1 分） · 2026-10-16T17:17:09+08:00　
> You're welcome. Best of luck!

---

> **zunjae**（0 分） · 2026-10-16T20:21:59+08:00　
> Needs more useless green circles

---

> **Joncallim**（1 分） · 2026-10-16T22:17:02+08:00　
> Nice, that covers both. Thanks for the screenshot too!

---

> **Anxious-Neni3500**（1 分） · 2026-10-17T13:57:51+08:00　
> This really seems like AI everything lmao, even the replies OP gives

---

> **HyperWinX**（1 分） · 2026-10-17T15:04:18+08:00　
> Tiktok attention span got you, huh?

---

> **HyperWinX**（1 分） · 2026-10-17T15:04:45+08:00　
> Yeah, and Linux kernel is completely vibecoded, it has kernel panics too...

---

> **Bfox135**（2 分） · 2026-10-18T00:04:41+08:00　
> That was straight after install from the .MSI
> If a program can't even properly I install and work in first boot on a system running bare minimum security, there's something not polished about that software. Most of the time because of vibe coding.

---

> **FDgajju22**（2 分） · 2026-10-22T19:57:30+08:00　
> Hey, Zync v2.37.0 now supports OpenSSH user certificate,
> Thanks again for highlighting this, If you get a chance to try it, I would love to hear whether it works with your setup
>
> https://preview.redd.it/dqzgzbbqc0xh1.png?width=584&format=png&auto=webp&s=5bb3b7dabd11559751e1054017544e28ca3897c1
>
> It also supports importing `CertificateFile` alongside `IdentityFile` from `~/.ssh/config`

---

> **vortige-sven**（2 分） · 2026-10-22T20:11:23+08:00　
> Awesome! Thank you for your update! Will try it out later

---

> **vortige-sven**（1 分） · 2026-10-23T00:12:55+08:00　
> Jup, works! One thing I'd appreciate is an "up" button in the file explorer. So when I go into a folder I don't have to navigate through changing the path.

---

> **FDgajju22**（1 分） · 2026-10-23T01:58:01+08:00　
> Great to hear the certificates work,
> You can already go to the parent folder with **Alt + ↑**, or click a parent folder in the breadcrumb bar. Arrow keys navigate files, and **Enter** opens the selected folder, also with the file list focused, you can also start typing to filter files without clicking the search bar. I’ve tried to make navigation keyboard-friendly.
>
> There isn’t a dedicated **Up** button yet, but I’d noticed this too and already have it on my upcoming improvements list.

## 关联链接

- https://github.com/zync-sh/zync/releases/tag/v2.35.1
- https://pub-f5d307b0347348988dccc997da10756a.r2.dev/2.35.1.mp4
- https://zync.thesudoer.in
- https://zync.thesudoer.in/

## 导航

- 项目页：[[10-项目/github.com_58dd29e2]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
