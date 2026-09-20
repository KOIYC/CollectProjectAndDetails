---
type: "corpus"
item_id: "12f1b053d59676af"
title: "Show HN: A browser music sequencer: every note is a Petri-net transition firing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47963271"
project_url: "https://blog.stackdump.com/posts/petri-net-runtime"
author: "orksliver"
published_at: "2026-04-30T14:40:30Z"
captured_at: "2026-09-21T02:52:23+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_orksliver
  - story_47963271
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: A browser music sequencer: every note is a Petri-net transition firing

> [!info] 一句话导读
> A browser music sequencer where every note is a Petri-net transition firing

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47963271>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：orksliver　|　发布：2026-04-30T14:40:30Z
> 项目链接：<https://blog.stackdump.com/posts/petri-net-runtime>
> 采集：2026-09-21T02:52:23+08:00　|　id：`12f1b053d59676af`

## 正文

← Home
petri-nets
 music
 beats-bitwrap
A browser music sequencer where every note is a Petri-net transition firing
Live at beats.bitwrap.io . Source: github.com/stackdump/beats-bitwrap-io .
That picture is the runtime, not a render of it. Each cluster on the ring is a sub-net (kick, snare, hihat, bass, melody, plus four hit slots) with its A/B/C variants beside it; the spokes meeting at the centre are the connector places that compose the song. The audio engine is reading exactly this state to fire transitions — at any moment you're hearing one variant per slot, chosen from the denser structure on screen.
The thing I wanted to share isn't that we built a beat generator — there are plenty. It's the implementation choice underneath it: the sequencer is a Petri net executor . There is no separate timeline data structure, no event list, no "schedule note at tick N." A drum pattern is a ring of places with one token circulating; each transition fire is a note. Polyrhythm is two rings of different length sharing a tempo. Song structure is a control net that fires mute-track / unmute-track / activate-slot actions at section boundaries. Macros are short linear-chain control nets injected at runtime with a restore action on the terminal transition.
Once you commit to that, several properties fall out for free:
Deterministic by construction. Same (genre, seed) produces a byte-identical token-flow trace. We have a Go port of the JS composer that produces the same bytes; the parity test is in CI. This isn't "we test for determinism" — there isn't a non-deterministic codepath to begin with. The web worker drives the tick loop at 60000 / (BPM × PPQ) ms and the Petri net engine does the rest.
Share URLs are content-addressed. A track is a small JSON envelope ( @context + genre + seed + optional overrides), canonicalized, sha-256'd, encoded as a CIDv1 in base58btc. The URL is ?cid=z… . Same canonical bytes ⇒ same CID, always. Different bytes can't pretend to be an existing one. There's also a ?cid=…&z= form that inlines the gzipped envelope so the link works offline, from a local copy, or after the share store is purged. ~80 chars for the short form, ~1.5 kB for the self-contained form.
The visualizer is the runtime. Press M and the app turns into a Petri-net display: nine sub-nets in a ring, each showing the active variant for its slot, joined through central connector places. The visuals aren't reading the audio — they're reading the same place/transition state the audio engine is reading. Token particles pulse toward the composition core on each fire; per-panel flames ignite on every transition. It's the first time I've shipped a music tool where the thing on screen is literally the data structure making the sound.
Boring stack. No bundler, no npm install, no React. Vanilla ES modules, Tone.js from CDN, a single Go binary that serves the static files and the share store. Production has no audio renderer running — .webm renders are uploaded by listeners' browsers via PUT /audio/{cid}.webm (rate-limited, first-write-wins, hash-checked). The site doesn't transcode; it stores bytes other browsers produced.
No backend during playback. Once a share envelope arrives, every sound is generated in the listener's tab. The server's job is content addressing and feed indexing; the audio path is browser-only.
There's a /feed gallery, a Winamp-flavoured sidebar player, an Auto-DJ that picks random macros every N bars, and a regen mode that cross-fades into newly-generated tracks on a one-bar pre-render so the swap is a pointer flip with no clicks. Those are nice but they aren't the point — they're what falls out after you commit to the runtime model. The longer launch post with screenshots and details is at /posts/beats-launch-jambox .
We still haven't added a piano roll.
Things I'd be most curious to discuss:
Is "Petri net as canonical sequencer IR" a known pattern in computer music? I haven't seen it in the literature I've read; the closest neighbours feel like Max/MSP patcher graphs or SuperCollider proxy spaces, but those are dataflow, not place/transition.
The deterministic-by-construction angle: is anyone else doing music tooling where the share URL is the complete spec , not a pointer to a server-stored timeline?
For a content-addressed audio store: what would you do differently for serving .webm at scale beyond "stick a CDN in front"? The naive disk + nginx setup is fine until it isn't.
Code, generator, share-store sealing, and the Go/JS parity tests are all in the repo.
Discussion: Hacker News
← Home
 •
 All Posts
 •
 📖 Book
 ✏️ Edit
 •
 Follow
Published: 2026-04-30T00:00:00Z | Modified: 2026-04-30T00:00:00Z
×
 Follow on Mastodon
Follow

## 导航

- 项目页：[[10-项目/blog.stackdump.com_e1228169]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
