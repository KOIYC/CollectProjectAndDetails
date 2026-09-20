---
type: "corpus"
item_id: "871f748510d821aa"
title: "Show HN: Floe – an open-source plugin for sample libraries – CLAP/VST3/AU"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49507908"
project_url: "https://floe.audio/"
author: "windell"
published_at: "2026-08-31T10:11:39Z"
captured_at: "2026-09-21T02:56:48+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_windell
  - story_49507908
  - show_hn
metrics: {"points": 22, "comments": 16, "engagement_velocity": 22}
comments_count: 16
comments_total: 16
discovered_via: "hn:show_hn:52d"
---

# Show HN: Floe – an open-source plugin for sample libraries – CLAP/VST3/AU

> [!info] 一句话导读
> I'm Sam, I make sample libraries (as FrozenPlain). These sample libraries run inside Floe, my audio plugin for Linux, macOS and Windows. It's designed for music…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49507908>
> 指标：点赞=22 · 评论=16 · engagement_velocity=22
> 作者：windell　|　发布：2026-08-31T10:11:39Z
> 项目链接：<https://floe.audio/>
> 采集：2026-09-21T02:56:48+08:00　|　id：`871f748510d821aa`

## 正文

I'm Sam, I make sample libraries (as FrozenPlain). These sample libraries run inside Floe, my audio plugin for Linux, macOS and Windows. It's designed for musicians, composers and producers - typically people involved with film/TV/game scoring or ambient music. I open-sourced it primarily because I'm very fond of this philosophy and I want to open the door for serving a wider audience than just my own libraries.It's totally free, no sign-ups. You'll need a DAW. To try it:
- Download and install Floe: https://floe.audio
- Download your choice of free packages: https:floe.audio/packages#community-packages or https://www.frozenplain.com/product/music-box-suite-free
- Install the packages using Floe's 'Install Package' button. https://floe.audio/docs/installation/install-packagesI'm curious about HN's thoughts regarding the open-source nature, directions I could take for expanding the audience, and the Lua based sample-library it has (https://floe.audio/docs/develop/develop-libraries). Thanks.

## 评论（16/16）

> **nasso_dev** · 2026-08-31T14:07:51.000Z　
> i couldn't find any information about it but i still see an AGENTS.md file at the root of the source tree so: how much AI was used in the making of this? how was it used?

---

> **rglover** · 2026-08-31T17:55:17.000Z　
> Is this essentially "roll your own VST plugin" or something else?

---

> **gamegod** · 2026-08-31T18:35:10.000Z　
> This looks great. Maybe a Kontakt killer? There's definitely a niche for something like this. It's good cross-promotion for your sound libraries too.

---

> **atmanactive** · 2026-08-31T18:38:47.000Z　
> Is the plug in portable? In a sense: can I run it from any path, or does it require operating system's well known hard coded paths?

---

> **nylonstrung** · 2026-08-31T21:36:14.000Z　
> This looks great, I'll be excited to see this progressively become pure Zig and drop C++Would be great to have something like Kontakt without all the cruft

---

> **SyneRyder** · 2026-09-01T07:34:16.000Z　
> Looks pretty good from the web page! How does this differ from Decent Sampler though? There's probably obvious differences but I haven't had a chance to dive into figuring that out for myself.You should see if you can get a mention on the Sonic State / Sonic Talk podcast. Especially if you can get on episode with Yoad Nevo (the guy behind so many of the Waves plugins), or Ty Unwin and his Kontakt-based composing for the BBC. They'd probably have good constructive feedback while giving you a mention. I think Sonic Talk use Decent Sampler for their sample libraries for members, but maybe this will convince them to switch to Floe?

---

> **Patrickkkkkkkk** · 2026-09-01T17:23:47.000Z　
> whos this actually for? , your icp to be precise
> What would make the next 90 days a success for you?

---

> **windell** · 2026-08-31T14:37:52.000Z　
> Since early 2026 it's mixed AI and handwritten. Before that it was mostly written by hand. Quite a lot of the code goes back to 2018 even. Typically, I do back and forth with Claude Code agents on new features and bug fixes, reading and editing code along with it.

---

> **windell** · 2026-08-31T18:52:24.000Z　
> Not quite as generic as that. I suppose there's 2 types of users at the moment.Musicians who just want load up virtual instruments (whether that's 'real' instrument, or synthesised-based), play them, but then also use Floe's GUI to morph the sound into something different using layers, granular, FX, etc.Or alternatively, sample library developers who want to create a curated sample library package for musicians. They configure the sample library using Lua (and set a background image and icon) and create a bank of presets - and then musicians can load that packagr into their Floe instance.

---

> **windell** · 2026-08-31T19:02:40.000Z　
> It can run from any path so long as your plugin host or DAW is happy to load it from there (the plugin APIs define standard folders plugins should be installed to, but lots of host allow other paths).Once running it will try to create some directories in known locations on your OS for storing libraries, presets, preferences, etc. https://floe.audio/docs/reference/file-locations

---

> **windell** · 2026-09-01T12:52:53.000Z　
> Thank for the excellent suggestions! I'll definitely take a look.Perhaps the key difference is that Decent Sampler allows you to create a custom GUI for your sample library. Floe does not, it's a standard, complete set of parameters that explore into the realm of sample-based-synthesis moreso than just performing virtual instruments.I do wonder about offering an API for creating custom GUIs, but I'm unsure how it would interact with the existing firmly ingrained GUI. Maybe it would have to be a wrapper API mostly - allowing sample libraries to 'grab' into the existing set of parameters and expose and reconfigure them into custom elements.

---

> **atmanactive** · 2026-09-01T08:43:40.000Z　
> That's unfortunate. That means that in a multi room studio synchronization can't happen and each instance will drift and has to be set again and again. Here's a way how to resolve this (as implemented by Surge XT or any of the U-He): the software should infer its own runtime path and then test for the existence of a subdirectory "data" (for example). If the directory doesn't exist, then settings files are read and written to operating system's well known paths. But, if the directory does exist then all runtime files should be read and written from there.

---

> **windell** · 2026-09-01T12:45:29.000Z　
> Interesting, I'll take a look at the Surge source, they're a clever bunch. If you have a moment - I'd like to understand this use-case more. What do you mean multi room studio? Does a per-user installation help, vs an all-users installation?

---

> **atmanactive** · 2026-09-02T09:45:22.000Z　
> Historically, early VST plug-ins were fully portable. They were rarely communicating with the underlying file system and were leaving all state management to the host. This made a DAW and a VST library a single unit which could run from anywhere, including network attached shared drives. So, in a multi room studio of yesteryear or in a distributed band studio of modern times, only one setup was needed for all of the nodes. A studio engineer would prepare a DAW+VST directory, share it via network, and all studios would have exactly the same setup with exactly the same plug-ins, with exactly the same configuration without having to repeat the whole setup N times. Therefore, a musician/producer/engineer could work in any studio room without limitations or distractions. The leader in this field is Cockos Reaper which supports fully portable operation, plus full relative path expansion everywhere. In my experience, there are about ~3000 VST2/VST3/CLAP plug-ins in existence, running flawlessly for decades now. So, by saving the plug-in state to operating system's semi-hardcoded directories, your plugin stays non-portable, and instead of being a full part of the DAW setup, becomes an unmanageable mess that nobody wants to deal with.

---

> **windell** · 2026-09-04T15:21:17.000Z　
> Interesting! Thank you for the explanation. I wonder what file permission issues we might face trying to write adjacent to the plugin file. I'll see what Surge does.

---

> **atmanactive** · 2026-09-04T17:35:28.000Z　
> Sure. Just make sure to bubble the error up to the UI and no problemo. Recent portable software even includes a toggle in settings to dynamically let users decide which state store to use, like, for example, the excellent LinkLever.

## 关联链接

- https://floe.audio
- https://floe.audio/docs/develop/develop-libraries
- https://floe.audio/docs/installation/install-packagesI
- https://www.frozenplain.com/product/music-box-suite-free

## 导航

- 项目页：[[10-项目/floe.audio_57f117fc]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
