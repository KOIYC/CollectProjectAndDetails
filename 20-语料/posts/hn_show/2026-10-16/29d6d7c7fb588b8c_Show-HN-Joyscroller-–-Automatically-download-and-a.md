---
type: "corpus"
item_id: "29d6d7c7fb588b8c"
title: "Show HN: Joyscroller – Automatically download and archive your liked videos"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50105490"
project_url: "https://github.com/sergiotapia/joyscroller"
author: "sergiotapia"
published_at: "2026-10-15T15:53:34Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_sergiotapia
  - story_50105490
  - show_hn
metrics: {"points": 2, "comments": 6, "engagement_velocity": 2}
comments_count: 6
comments_total: 6
discovered_via: "hn:show_hn:3d"
---

# Show HN: Joyscroller – Automatically download and archive your liked videos

> [!info] 一句话导读
> sergiotapia/joyscroller

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50105490>
> 指标：点赞=2 · 评论=6 · engagement_velocity=2
> 作者：sergiotapia　|　发布：2026-10-15T15:53:34Z
> 项目链接：<https://github.com/sergiotapia/joyscroller>
> 采集：2026-10-16T09:35:18+08:00　|　id：`29d6d7c7fb588b8c`

## 正文

# sergiotapia/joyscroller

Automatically download and archive your liked youtube, tiktok and instagram videos.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 7
- License: MIT License
- Default branch: master
- Created: 2026-10-13T01:13:41Z

## Languages

- CSS
- JavaScript
- Just
- Python
- Rust

## Top Contributors

- sergiotapia (32 contributions)

---

## README

# Joyscroller

Joyscroller's pages: the list of likes, a search typed in and its results sorted by length, a YouTube video playing, and a TikTok photo post's slideshow

Automatically download the videos you like on TikTok, YouTube and Instagram, and keep them forever.

You've liked thousands of videos. Some get deleted, some go private, and the rest sink to the bottom of a feed you'll never scroll back through. Joyscroller saves a copy of each one to your own computer, so the videos you loved are still yours long after the app moves on.

- **Everything you've liked, in one place.** Your YouTube likes, TikTok likes and Instagram saves, side by side in one library you can browse and watch.
- **The best quality there is.** Each video is saved at the highest quality the platform offers, with its real sound. TikTok photo slideshows are saved too, images and music included.
- **Neatly organized.** Videos land in plain folders, sorted by platform and by the day you liked them, each named after its title. No mystery file names, and nothing locked inside an app.
- **Nothing to set up.** Joyscroller signs in with the browser you already use. No accounts to connect, no passwords to type, no API keys.
- **It keeps up on its own.** Leave it running and new likes show up in your library within minutes of tapping the heart.
- **Private by design.** It all runs on your computer. Your likes and videos never go anywhere else.

## How to get it and run it

You need Linux and Brave, signed in to YouTube, TikTok and Instagram.

1. Download the latest `joyscroller-…-linux-x86_64.tar.gz` from Releases (`aarch64` if your computer has an ARM chip).
2. Unpack it wherever you'd like to keep your videos, and start it:

   ```sh
   tar -xzf joyscroller-*-linux-x86_64.tar.gz
   cd joyscroller-*-linux-x86_64
   ./joyscroller
   ```

3. Open **http://127.0.0.1:4774** and watch your likes roll in.

Keep it running to stay up to date, and press Ctrl-C to stop it. Your library is saved right next to the app: `joyscroller.db` and a `downloads` folder. Move the folder and your library moves with it.

The first time it starts, Joyscroller fetches the helpers it downloads videos with (yt-dlp, plus ffmpeg and bun if you don't already have them) into a `tools` folder beside it, and keeps them up to date. There's nothing else to install.

### Building from source

With Rust installed:

```sh
git clone https://github.com/sergiotapia/joyscroller.git
cd joyscroller
cargo run --release
```

Built this way, your library is saved in the `data` folder inside `joyscroller`.

## Developers

```sh
cargo run
```

Then open **http://127.0.0.1:4774**. That runs against your real archive in `data/`. To experiment without touching it, run a copy of the app from a throwaway folder, which keeps its own database, downloads and tools there:

```sh
mkdir -p /tmp/joyscroller-dev && cp target/debug/joyscroller /tmp/joyscroller-dev/ && /tmp/joyscroller-dev/joyscroller
```

The debugging subcommands (`likes`, `sync`, `download`, `cookies`) are listed in AGENTS.md. They use the app's own yt-dlp and ffmpeg once it has fetched them, and otherwise whatever is on your `PATH`.

Pushing a version tag builds and publishes a release (see .github/workflows/release.yml). Run `just precommit` before every commit. CONTRIBUTING.md has the conventions, and AGENTS.md has the architecture and data model.

## License

MIT.

# skyblanket/swift-render

## 评论（6/6）

> **toomuchtodo** · 2026-10-15T16:50:51.000Z　
> Great work! Would you be willing to support as a feature request uploading to an AT Proto PDS such as https://vlpds.jazco.dev/ after the download is successful? Does it save static images or image carousels as well?

---

> **sergiotapia** · 2026-10-15T17:12:23.000Z　
> I'll look into that sure!RE photos: It saves tiktok slideshows with the audio and familiar controls appear for those. It doesn't save liked photos from Instagram no, but it should! I'll make it happen.https://github.com/sergiotapia/joyscroller/issues/14https://github.com/sergiotapia/joyscroller/issues/15

---

> **sergiotapia** · 2026-10-15T20:49:15.000Z　
> This is live now, Joyscroller now downloads Instagram pics, slideshows and videos you've liked or favorited. Slideshow audios too! Feels really nice

---

> **toomuchtodo** · 2026-10-15T20:51:27.000Z　
> Hero, tip jar where?

---

> **sergiotapia** · 2026-10-15T20:54:15.000Z　
> You're very welcome! No need for a tip just share the app with friends so I get more bug reports!

---

> **toomuchtodo** · 2026-10-15T20:58:13.000Z　
> I will share the good work, thank you again.

## 关联链接

- http://127.0.0.1:4774**
- http://127.0.0.1:4774**.
- https://github.com/sergiotapia/joyscroller.git

## 导航

- 项目页：[[10-项目/github.com_356f9785]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
