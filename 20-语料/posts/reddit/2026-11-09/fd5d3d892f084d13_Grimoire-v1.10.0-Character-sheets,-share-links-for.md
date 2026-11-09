---
type: "corpus"
item_id: "fd5d3d892f084d13"
title: "Grimoire v1.10.0 - Character sheets, share links for your VTT, and six weeks of updates to the self-hosted TTRPG library"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xitik9/grimoire_v1100_character_sheets_share_links_for/"
project_url: "https://db.grimoirecodex.org/"
author: "Perfekthuntr"
published_at: "2026-10-30T03:24:09+08:00"
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
  - Release (AI)
metrics: {"score": 68, "comments": 24, "upvote_ratio": 0.9146341463414634}
comments_count: 23
comments_total: 24
discovered_via: "reddit:14d+settle10"
---

# Grimoire v1.10.0 - Character sheets, share links for your VTT, and six weeks of updates to the self-hosted TTRPG library

> [!info] 一句话导读
> When I posted v1.7.0 (I'm not on reddit a lot anymore, so apologies for the lack of updates here), I said Grimoire isn't becoming a VTT. The goal is to get your…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xitik9/grimoire_v1100_character_sheets_share_links_for/>
> 指标：得分=68 · 评论=24 · 赞踩比=0.9146341463414634
> 作者：Perfekthuntr　|　发布：2026-10-30T03:24:09+08:00
> 项目链接：<https://db.grimoirecodex.org/>
> 采集：2026-11-09T09:41:26+08:00　|　id：`fd5d3d892f084d13`

## 正文

When I posted v1.7.0 (I'm not on reddit a lot anymore, so apologies for the lack of updates here), I said Grimoire isn't becoming a VTT. The goal is to get your content into whichever VTT your table already uses. Six weeks and a few releases later, here's how that's going, plus everything else that snuck in along the way.

# What's new since 1.7 (which is my last update on Reddit)

* **Character sheets.** Install a sheet for your game from the community catalogue (D&D 5e 2024, Draw Steel, Pathfinder 2e & 1e, Call of Cthulhu 7e, Traveller, Cosmere, Dungeon Crawler Carl, Cairn, Basic Fantasy) or paste in your own. Modifiers, saves and totals work themselves out as you type, and picking a class or species fills in what it grants. You can import existing characters from D&D Beyond, Pathbuilder 2e, DiceCloud and Forge Steel. Content packs add searchable spells, classes and feats (5e SRD, Draw Steel, PF Player Core), and each campagn can carry its own house rules.
* **Built for the whole table.** Characters live in campaigns so the party can see each other's sheets. Players can let the GM edit theirs, and GMs can hand a pre-gen straight to a player. Sheets can also ship a phone layout, since that's where they'll actually get read. (David, I know you are just scrolling reddit, you're on deck and if you can't figure out what spell to cast in under 10 minutes, I'm gonna feed you to a Tarrasque)
* **Share links.** Get a public, revocable link to any book, map, token, audio track or 3D model, with optional expiry and password, plus a direct file URL you can drop into your VTT or Discord. Maps can also be set up for OTFBM, the renderer behind Avrae's `!map`.
* **Export from the reader.** Pull out a page range as a PDF or images, or cut a map, card or round token straight off the page. **Join pages** stitches a two-page map spread into one seamless image, and zoom now goes up to 800%.
* **The library keeps itself up to date.** Grimoire watches your folders and picks up added, moved or renamed files within seconds, with no rescan. Duplicates merge in one step and keep their tags, bookmarks and campaign links. Metadata can be read from the PDF/EPUB/comic file itself, or pulled from Grimoire Codex DB, a community database of TTRPG books and systems. (Oh yeah, did I mention that before, there is now an entire public DB to TTRPGs that is designed from the ground up to be easy to use and work with Grimoire)
* **Lighter and more secure.** It uses about half the memory (\~250 MB once scanned) and downloads about a fifth of the JavaScript on first load. Pages render in a separate process, so one cursed PDF can't take the server down with it. The container no longer runs as root, personal API keys have per-area permissions, and images are on GHCR as well as Docker Hub. I might use AI, but I am a developer
* Plus more I'm too lazy to fully type out here

**Already running Grimoire?** Skim the release notes of every release since your current version before you pull down the latest. A lot of security features have been added that may break some installs.

# New here?

Grimoire is a self-hosted home for your whole TTRPG collection that makes it easy to search, read, organise and share.

* **Share your library with your players.** (Except the Rogue. He already has your library, your battlemaps and your browsing history.)
* **Read from any device.** It installs as a PWA, and pages render on the server, so your phone gets images instead of choking on a 400-page PDF. Perfect for looking busy while the Warlock spends 30 minutes deciding what to cast before casting Eldritch Blast again.
* **Not just PDFs.** EPUB, DjVu, comic archives and plain text all open in the same reader. Your scanned zine from 1998 is welcome here.
* **Full-text search** across every page of every book. Find that one rule without knowing which book it's in. Essential when you hoard 40+ systems like I do.
* **Organised automagically.** Drop files in folders and the wizard I've bound into the code with blood magic works out the system and category. He's opinionated about folder structure, so there's an in-app file manager for when you'd rather not argue with him.
* **Campaign tracker** with wiki-style notes, player and guest invites, linked resources, and recurring schedules you can subscribe to from your calendar app. Scheduling remains the true BBEG.
* **Maps, tokens, audio and 3D models.** There's a token editor, a Universal VTT map editor for walls, doors and lights, and a soundboard with playlists and one-tap sound pads.
* **Community add-ons** for themes, note templates, character sheets and metadata scrapers.
* **Docker and OIDC out of the box,** because not every homelab sorcerer wants to build from source.

Website: [https://grimoirecodex.org](https://grimoirecodex.org)
Live demo: [https://demo.grimoirecodex.org](https://demo.grimoirecodex.org)
Docs: [https://docs.grimoirecodex.org](https://docs.grimoirecodex.org)
DB: [https://db.grimoirecodex.org](https://db.grimoirecodex.org)
GitHub: [https://github.com/hunter-read/grimoire](https://github.com/hunter-read/grimoire)

On AI: yes, I use it. I've been a software developer for a long time and hold this project to a high standard for security, responsiveness and code quality. AI is one tool among many for speeding up the boring parts, testing and catching my mistakes. Grimoire is a personal project I'm happy to share, and if AI involvement is a dealbreaker for you, that's your call. I build this project with a lot of love. Feedback is always welcome.

## 评论（23/24）

> **asimovs-auditor**（1 分） · 2026-10-30T03:24:19+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Perfekthuntr**（3 分） · 2026-10-30T03:27:21+08:00　
> AI is used to assist in the development of this project. This is a project built by a software engineer with a decade of experience, and AI is used to help write code, debug issues, and automate security scanning.

---

> **questionable_bert**（4 分） · 2026-10-30T03:43:02+08:00　
> the folder watching thing is slick, i've got a messy nas full of old d&d pdfs and it just picks them up without me having to think about it
>
> the character sheet catalogue is a nice touch too, saves me from building one from scratch for my pf2e group. and the share links finally mean i can stop emailing maps to my players like it's 2005

---

> **JMowery**（2 分） · 2026-10-30T04:09:56+08:00　
> Nice work! I'm not in a position to do D&D at the moment, but if I was, I would absolutely use this. Have a star and an upvote. :)

---

> **d5vour5r**（2 分） · 2026-10-30T05:27:43+08:00　
> Cool project, will check this out for sure

---

> **GhostR3lay**（2 分） · 2026-10-30T05:55:45+08:00　
> I thought some folks had mentioned this was a little heavy for their liking but if recent releases have slimmed it down a little bit that makes me a bit more interested in checking it out. The functionality of this gets me maybe a little bit closer to being able to migrate my FoundryVTT servers from Windows to Linux.

---

> **Afraid-Finish-1811**（2 分） · 2026-10-30T05:56:43+08:00　
> isolating the PDF rendering into a separate process is a really smart move, especially with how bloated and weirdly formatted some RPG books are. how does the folder watcher handle network shares where filesystem events can be pretty flaky?

---

> **Perfekthuntr**（1 分） · 2026-10-30T06:04:09+08:00　
> For network shares that might have inconsistent system events, there is still support for a scheduled rescan, so if for some reason those events fail to trigger an update in the application, a normal scheduled scan will

---

> **Perfekthuntr**（2 分） · 2026-10-30T06:08:54+08:00　
> It was a big push to improve performance, stability, and security over the last few releases, and I've made good progress in all three areas.

---

> **kftX_**（2 分） · 2026-10-30T06:28:01+08:00　
> Does it support PDFs from Monte Cook games now? I tried it when you announced 1.7.0 here and the PDFs didn’t render at all so it wasn’t really useful to me since I wanted it for Numenera and Old Gods.
>
> Cool project tho!

---

> **Perfekthuntr**（2 分） · 2026-10-30T06:42:35+08:00　
> I support PDFs from anywhere, though there have been improvements to OCR for mixed format PDFs which should improve support for a lot more files.
>
> If you are running into issues with a specific PDF, reach out with a GitHub issue or on discord and I can investigate further.

---

> **kftX_**（2 分） · 2026-10-30T06:44:31+08:00　
> I'll set it up tomorrow (late here now) and if I have issues, I'll make an issue on GitHub then! Cheers and thanks :D

---

> **reeetgio**（2 分） · 2026-10-30T11:48:09+08:00　
> The share links alone sound like a huge quality of life improvement. Folder watching is a nice bonus too

---

> **mxafi**（1 分） · 2026-10-30T18:24:45+08:00　
> Is this something that could support RuneQuest, specifically RQG? I could fork for the moment and slop something but would be interesting to hear your vision!

---

> **buttholemonkey**（2 分） · 2026-10-30T20:06:07+08:00　
> I'm really liking this idea, as some with hundreds of games in folders. This is an amazing way to organise them

---

> **Perfekthuntr**（2 分） · 2026-10-30T20:44:01+08:00　
> Grimoire is system agnostic, you can store 100 different systems PDFs. If you mean character sheets, then it's not currently built in, but you can request it on the community-add-ons repo by opening a gh issue.

---

> **RiffyDivine2**（2 分） · 2026-10-30T22:28:19+08:00　
> Well hot damn that is a lot of new toys. I was just using it to sort out my mess of rpg books but now it seems I can use it with VTT stuff is awesome.

---

> **kftX_**（2 分） · 2026-10-30T22:36:07+08:00　
> Just wanna follow up, did a quick test by dumping a Numenera PDF into the library and now it renders properly! Whatever didn't work then, does now.
>
> Thanks so much for replying too! Have a good weekend

---

> **swashbucklerjak**（1 分） · 2026-10-31T04:32:28+08:00　
> How does this do with really big libraries? I’ve got like 1500 pdfs and such.

---

> **Perfekthuntr**（1 分） · 2026-10-31T05:11:48+08:00　
> I am currently sitting at over 8000 PDFs across 350+ systems, 10,000 maps, 8000 tokens, 1000 audio files, and 500 3d models and it's still fast and responsive.

---

> **altgenetics**（1 分） · 2026-10-31T11:07:30+08:00　
> How are you feeling about ensuring this is accessible?
>
> I'm happy to contribute on this to ensure its accessible for blind folks using a screen reader + voice control users. But, it means keeping those structures as the visual styling gets iterated on.
>
> This is a hobby project so far, so I don't want to be the push blind guy. But I also can actually contribute.

---

> **Perfekthuntr**（1 分） · 2026-10-31T12:20:23+08:00　
> I actually really would love feedback or contributions in this regard. It's on my roadmap to improve, but security and performance have been the recent push.
>
> It's important to me that everyone is able to use the app.

---

> **altgenetics**（1 分） · 2026-11-01T00:14:30+08:00　
> Cool. I'm on leave for back surgery, and am so very bored. This is a good distraction. :D
> I'll take a look and create some issues, then you can prioritize and lemme know if you want me to put in a PR.

## 关联链接

- https://db.grimoirecodex.org
- https://demo.grimoirecodex.org
- https://docs.grimoirecodex.org
- https://github.com/hunter-read/grimoire
- https://grimoirecodex.org

## 导航

- 项目页：[[10-项目/db.grimoirecodex.org_1207f4a4]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
