---
type: "corpus"
item_id: "1b56bcf552cdfb48"
title: "Show HN: Kew, A distraction-free terminal music player, now on Windows"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48725477"
project_url: "https://github.com/ravachol/kew"
author: "ravachol"
published_at: "2026-06-29T21:26:11Z"
captured_at: "2026-09-21T03:11:02+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_ravachol
  - story_48725477
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Kew, A distraction-free terminal music player, now on Windows

> [!info] 一句话导读
> A Terminal Music Player

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48725477>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ravachol　|　发布：2026-06-29T21:26:11Z
> 项目链接：<https://github.com/ravachol/kew>
> 采集：2026-09-21T03:11:02+08:00　|　id：`1b56bcf552cdfb48`

## 正文

# ravachol/kew

A Terminal Music Player

- Stars: 2768
- Forks: 92
- Watchers: 2768
- Open issues: 0
- License: GNU General Public License v2.0
- Homepage: https://ko-fi.com/ravachol
- Default branch: main
- Created: 2023-05-17T05:29:52Z

## Languages

- C
- C++
- Makefile
- Nix
- Objective-C
- Shell

## Topics

- audio-player
- command-line
- kew
- linux
- macos
- music
- music-player
- player
- terminal

## Top Contributors

- ravachol (1831 contributions)
- Chromium-3-Oxide (108 contributions)
- petoem (23 contributions)
- DNEGEL3125 (17 contributions)
- mechatour (9 contributions)
- ronit1996 (9 contributions)
- werdahias (9 contributions)
- feng1st (5 contributions)
- Welpyes (5 contributions)
- episvr (4 contributions)

---

## README

License

**English** | 简体中文

kew (/kjuː/) is a terminal music player.

## Features

 * Search a music library with partial titles from the command-line.
 * Creates a playlist automatically based on matched song, album or artist.
 * Private, no data is collected by kew*.
 * Music without distractions or algorithmic manipulation.
 * Full color covers in sixel-capable terminals.
 * Visualizer with various settings.
 * Edit the playlist by adding, removing and reordering songs.
 * Gapless playback.
 * Explore the library and enqueue files or folders.
 * Search your music library and add to the queue.
 * Supports MP3, FLAC, MPEG-4/M4A (AAC), OPUS, OGG, Webm, WAV and AIFF audio.
 * Supports desktop events through MPRIS.
 * Supports lyrics through .lrc files, embedded SYLT (Mp3) or Vorbis comments (Flac,Ogg,Opus).
 * Supports replay gain.
 * Use themes or colors derived from covers.

 *kew displays it's status in Discord by default, but this can be disabled both in Discord and in the kew config file kewrc.

 ## ⚠️ This repository has moved to Codeberg!
Active development and issue tracking now happens at Codeberg.
Please open new issues and pull requests there.

## Installing

Install through your package manager or homebrew (macOS). If you can't find it on your distro, or you want the bleeding edge, follow the Manual Installation Instructions.

For NixOS, there is an official package but also a Nix Flake that is tied to the latest commit.

For Artix it's available in the artist repository.

For Fedora there is an unofficial repo.

## Usage

kew creates a playlist with the contents of the first directory or file whose name matches the arguments you provide in the command-line.

```bash
kew cure great
```

This creates and starts playing a playlist with 'The cure greatest hits' if it's in your music library.

It works best when your music library is organized this way:

artist folder->album folder(s)->track(s).

### Example commands

```
kew (starting kew with no arguments opens the library view where you can choose what to play)

kew all (plays all songs, up to 50 000, in your library, shuffled)

kew albums (plays all albums, up to 2000, randomly one after the other)

kew moonlight son (finds and plays moonlight sonata)

kew moon (finds and plays moonlight sonata)

kew beet (finds and plays all music files under "beethoven" directory)

kew dir <album name> (sometimes, if names collide, it's necessary to specify it's a directory you want)

kew song <song> (or a song)

kew play "/home/joe/Musik/Fridge - (2007) The Sun/" (Plays this album, location can be anywhere)

kew play "/home/joe/Musik/moonlight sonata.flac" (Plays moonlight sonata, location can be anywhere)

kew play <album path> <album path> <song path> (play can take multiple album paths or song paths and add them all into temporary playlist)

kew list <playlist> (or a playlist)

kew theme midnight (sets the 'midnight.theme' theme).

kew shuffle <album name> (shuffles the playlist. shuffle needs to come first.)

kew artistA:artistB:artistC (plays all three artists, shuffled)

kew --help, -? or -h

kew --version or -v

kew --nocover

kew --noui (completely hides the UI)

kew -q <song>, --quitonstop (exits after finishing playing the playlist)

kew -e <song>, --exact (specifies you want an exact (but not case sensitive) match, of for instance an album)

kew . loads kew favorites.m3u

kew path "/home/joe/Musik/" (changes the path)

 ```

### Key Bindings

#### Basic

* Enter to play or enqueue/dequeue.
* Space, p or right mouse to play or pause.
* Use + (or =), - keys to adjust the volume.
* Use ←, → or h, l keys to switch tracks.
* Alt+s to stop.
* F2 or Shift+z (macOS/Android) to show/hide playlist view.
* F3 or Shift+x (macOS/Android) to show/hide library view.
* F4 or Shift+c (macOS/Android) to show/hide track view.
* F5 or Shift+v (macOS/Android) to show/hide search view.
* F6 or Shift+b (macOS/Android) to show/hide key bindings view.
* i to cycle colors derived from kewrc, theme or track cover.
* t to cycle themes.
* Backspace to clear the playlist.
* Delete to remove a single playlist entry.
* r to cycle repeat settings (repeat, repeat list, off).
* s to shuffle the playlist.

#### Advanced

* u to update the library.
* m show full page lyrics in track view. See Lyrics
* v to toggle the visualizer.
* b to toggle album covers drawn in ascii or as a normal image.
* n to toggle notifications.
* a to seek back. keep pressed for a longer duration, it executes the seek when you release the key.
* d to seek forward. keep pressed for a longer duration, it executes the seek when you release the key.
* x to save the currently loaded playlist to a m3u file in your music folder.
* Tab to switch to next view.
* Shift+Tab to switch to previous view.

* f, g to move songs up or down the playlist.
* number + G or Enter to go to specific song number in the playlist.
*. to add currently playing song to kew favorites.m3u (run with "kew .").
* Esc to quit.

## Configuration

Linux: ~/.config/kew/

macOS: ~/Library/Preferences/kew/

Key bindings can be added like this:

bind = +, volUp, +5%

If you have an old install of kew, delete the kewrc file to make this style of bindings appear.

kew state (for settings that can be changed in-app) is kept in ~/.config/kew/kewstaterc.

If you change a setting in-app it will be tracked by kewstaterc and not kewrc.

kewrc is never changed by kew with the exception of when you run kew path.

If you delete your kewrc a new default one will be generated. You wont get newer config options listed in your config file unless you do this.

## Themes

Press t to cycle available themes.

To set a theme from the command-line, run:

```bash
kew theme <themename> (ie 'kew theme midnight')
```

Put themes in \~/.config/kew/themes (\~/Library/Preferences/kew/themes on macOS).

Do not edit the included themes as they are managed by kew. Instead make a copy with a different name and edit that.

Try the theme editor (by @bholroyd): https://bholroyd.github.io/Kew-tip/.

## Visulizations / Chroma

Starting with kew 4.0, you can add visualizations to kew by installing Chroma, an app by another developer.

You'll need to install a specific commit, which is the latest one that works.

How to install Chroma:

```
git clone https://github.com/yuri-xyz/chroma.git

cd chroma

git checkout fb00b6e

cargo install --path .
```

Enable and cycle through the visualizations by pressing c in track view.

Disable by pressing b.

This works by kew being fed frames from Chroma and does not add bloat to kew.

### Configuration

You can customize Chroma's behavior in your `kewrc` file:

- `chromaPath`: Path to a custom Chroma preset file. If set, this preset will be used instead of the built-in ones.
- `chromaDevice`: Specify the audio device for Chroma to capture from (e.g., `PipeWire Sound Server`). Use `chroma --list-audio-devices` to find available devices.

```ini
[chroma]
chromaPath=/path/to/your/custom.preset
chromaDevice=PipeWire Sound Server
```

## If Colors or Graphics Look Wrong

Cycle i until they look right.

Press v to turn off visualizer.

Press b for ASCII covers.

A terminal emulator that can handle TrueColor and sixels is recommended. See Sixels in Terminal.

## Lyrics

Lyrics can be read from a provided .lrc file that matches the audio file in name and content, from Vorbis comment metadata or from SYLT embedded tags on mp3 files.

Timestamped lyrics will be shown automatically in track view. Press m show full page lyrics.

## Playlists

To load a playlist: type kew list

To export a playlist, press x. This will save a file in your music path with the name of the first song in the queue.

There is also a favorites playlist function:

Add current song: press.

To load 'kew list fav': kew .

## Scrobbling

kew's private and offline nature means we don't support Scrobbling/last.fm directly. Instead tools such as PanoScrobbler are recommended. See: https://github.com/kawaiiDango/pano-scrobbler.

## License

Licensed under GPL. See LICENSE for more information.

## Star History

Github Stars: GitHub stars

Codeberg Stars: Codeberg stars

## Attributions

 Attributions

kew makes use of the following great open source projects:

Chafa by Hans Petter Jansson - https://hpjansson.org/chafa/

Chroma by yuri-xyz - https://github.com/yuri-xyz/chroma

TagLib by TagLib Team - https://taglib.org/

Faad2 by fabian_deb, knik, menno - https://sourceforge.net/projects/faac/

FFTW by Matteo Frigo and Steven G. Johnson - https://www.fftw.org/

Libopus by Opus - https://opus-codec.org/

Libvorbis by Xiph.org - https://xiph.org/

Miniaudio by David Reid - https://github.com/mackron/miniaudio

Minimp4 by Lieff - https://github.com/lieff/minimp4

Nestegg by Mozilla - https://github.com/mozilla/nestegg

Img_To_Txt by Danny Burrows - https://github.com/danny-burrows/img_to_txt

TermBox2 (adapted for input handling only) - By nsf and Adam Saponara https://github.com/termbox/termbox2

## Authors

See AUTHORS.

## Contact

Comments? Suggestions? Send mail to kew-player@proton.me.

# GuglielmoCerri/khazad

## 关联链接

- https://bholroyd.github.io/Kew-tip/.
- https://github.com/danny-burrows/img_to_txt
- https://github.com/kawaiiDango/pano-scrobbler.
- https://github.com/lieff/minimp4
- https://github.com/mackron/miniaudio
- https://github.com/mozilla/nestegg
- https://github.com/termbox/termbox2
- https://github.com/yuri-xyz/chroma
- https://github.com/yuri-xyz/chroma.git
- https://hpjansson.org/chafa/
- https://ko-fi.com/ravachol
- https://opus-codec.org/
- https://sourceforge.net/projects/faac/
- https://taglib.org/
- https://www.fftw.org/
- https://xiph.org/

## 导航

- 项目页：[[10-项目/github.com_34fa23f3]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
