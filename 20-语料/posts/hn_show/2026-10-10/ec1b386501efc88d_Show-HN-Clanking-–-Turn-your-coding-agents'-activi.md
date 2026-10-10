---
type: "corpus"
item_id: "ec1b386501efc88d"
title: "Show HN: Clanking – Turn your coding agents' activity into a subtle soundscape"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50027932"
project_url: "https://github.com/chrchr/clanking"
author: "chrchr"
published_at: "2026-10-09T23:40:47Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_chrchr
  - story_50027932
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Clanking – Turn your coding agents' activity into a subtle soundscape

> [!info] 一句话导读
> Turn agent activity into a quiet soundscape.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50027932>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：chrchr　|　发布：2026-10-09T23:40:47Z
> 项目链接：<https://github.com/chrchr/clanking>
> 采集：2026-10-10T09:53:50+08:00　|　id：`ec1b386501efc88d`

## 正文

# chrchr/clanking

Turn agent activity into a quiet soundscape.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-10-09T20:19:52Z

## Languages

- Dockerfile
- Go
- Makefile
- Shell

## Top Contributors

- chrchr (104 contributions)

---

## README

# What's that *Clanking* sound?

For machines called "clankers", LLM agents sure don't make much noise.
Are they *too* quiet? Yes! But not anymore.

Clanking turns your LLM agents' activity into a subtle soundscape. It
signals when an agent is working, waiting for input, or in another state.
Clanking plays cues from many agents at once and harmonizes them into a
happy chorus of chattering clankers.

## Demo

https://github.com/user-attachments/assets/437b30b0-3852-4670-b634-daad4949b651

## Design

Coding agent hooks invoke the Clanking CLI, which reads each hook
event and plays a sound cue. For tool calls, it plays a short tick on
one of several notes to signal that the agent is active. Other sounds
indicate that the agent is outputting a response, waiting for input or
permission, has finished, or has encountered an error.

Clanking runs as a daemon that starts on its first invocation, and the
CLI sends messages to the background task on subsequent invocations.
Sounds are quantized to sixteenth notes at the configured tempo, which
defaults to 120 BPM. During high activity, Clanking switches to
thirty-second notes. The program synthesizes the sounds.

Clanking uses stereo position to help you distinguish agent sessions.
It positions each session according to the agent's working directory,
so clanks from different sessions seem to come from different places.

You can configure the tempo and root note from the command line or
Clanking's GTK 4 UI.

## Installation

Clanking requires a Unix-like system with PipeWire and the `pw-cat`
utility. It has an optional GTK 4 user interface for configuration.
Clanking is vibe-coded in Go and requires a Go toolchain and GTK 4
development libraries to build.

On a Unix-like system with the required dependencies and an XDG-style
desktop (such as GNOME or KDE), `make install` installs `clanking`,
`clanking-ui`, a desktop file, and an icon in your home directory.

The included `Containerfile` lets you build Clanking without installing
all the development dependencies on your system. The `podman-make`
script builds and runs the container. Adapting it for Docker is left as
an exercise for the reader or the reader's coding agent.

## Configure your Coding Agents

With `clanking` and `pw-cat` in your `$PATH` on a system with PipeWire,
you can configure your coding agent to invoke Clanking.

For Claude, install the Clanking plugin from this repository's marketplace:

```text
/plugin install clanking --marketplace chrchr/clanking
```

For Codex, add this repository as a plugin marketplace:

```sh
codex plugin marketplace add chrchr/clanking
codex plugin add clanking@clanking
```

Restart Codex, then run `/hooks`. Trust the Clanking hooks.

## Inspo

* [Peep (The Network Auralizer): Monitoring Your Network With Sound][peep]
 by Michael Gilfix and Prof. Alva Couch, Tufts University.

* Star Trek: The Next Generation.
 The voice-interactive computer in the "Star Trek" franchise uses
 nonverbal sounds to signal that it is doing something.

* Earcons (Wikipedia). "An earcon is a
 brief, distinctive sound that represents a specific event or conveys other
 information."

## Copyright

Copyright © 2026 by Robert Church

[peep]: https://www.usenix.org/legacy/publications/library/proceedings/lisa2000/full_papers/gilfix/gilfix_html/index.html

# Programming Language Wars

## 关联链接

- https://github.com/user-attachments/assets/437b30b0-3852-4670-b634-daad4949b651
- https://www.usenix.org/legacy/publications/library/proceedings/lisa2000/full_papers/gilfix/gilfix_html/index.html

## 导航

- 项目页：[[10-项目/github.com_b8f3d5d0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
