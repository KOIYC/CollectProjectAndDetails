---
type: "corpus"
item_id: "b620df7d166b2bc1"
title: "Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49705442"
project_url: "https://github.com/JamesRyanATX/fcbnerd"
author: "fretlessjazz"
published_at: "2026-09-14T23:01:36Z"
captured_at: "2026-09-20T09:38:53+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-14"
tags:
  - 语料
  - hn_show
  - author_fretlessjazz
  - story_49705442
  - show_hn
metrics: {"points": 85, "comments": 21, "engagement_velocity": 85}
comments_count: 21
comments_total: 21
discovered_via: "hn:show_hn:90d"
---

# Show HN: Macros with a Behringer FCB1010 MIDI Pedalboard in macOS

> [!info] 一句话导读
> JamesRyanATX/fcbnerd

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49705442>
> 指标：点赞=85 · 评论=21 · engagement_velocity=85
> 作者：fretlessjazz　|　发布：2026-09-14T23:01:36Z
> 项目链接：<https://github.com/JamesRyanATX/fcbnerd>
> 采集：2026-09-20T09:38:53+08:00　|　id：`b620df7d166b2bc1`

## 正文

# JamesRyanATX/fcbnerd

Do things with a Behringer FCB1010 MIDI pedalboard in MacOS

- Stars: 62
- Forks: 1
- Watchers: 62
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-14T21:33:23Z

## Languages

- Swift

## Topics

- fcb1010
- macos
- midi

## Top Contributors

- JamesRyanATX (13 contributions)

---

## README

# fcbnerd

Cartoon: a developer leans back from a wide monitor with a coffee, stomping a footswitch on a MIDI pedalboard while a dog sleeps nearby.

Use a MIDI foot controller as an extra keyboard for your Mac. `fcbnerd`
connects to your MIDI sources and either runs a shell command when a
footswitch or pedal sends a message you've bound, or prints one JSON object
per line for every message so another program can decide what a stomp
means.

```console
$ fcbnerd -q --bind '1:20:127=open ~/Downloads' --bind 'pc:1:0=say hello'
```

Or stream everything for another program to handle:

```console
$ fcbnerd
{"type":"connected","source":"UM-ONE","time":"2026-09-14T20:01:00.120Z"}
{"type":"pc","channel":1,"program":0,"source":"UM-ONE","time":"2026-09-14T20:01:02.345Z"}
{"type":"cc","channel":1,"controller":30,"value":84,"source":"UM-ONE","time":"2026-09-14T20:01:03.910Z"}
```

Built for the Behringer FCB1010, but nothing in it is FCB1010-specific: any
CoreMIDI source works.

## Why a command-line tool instead of an app

Anything that acts on your Mac, like pressing keys or running scripts, needs
permissions that sandboxed apps can't get, and every user wants a different
set of actions anyway. `fcbnerd` only reads MIDI, which needs no permissions.
The actions belong to your shell, or to a tool that already has the access,
such as Hammerspoon or Keyboard Maestro.

## Install

```sh
brew trust --tap jamesryanatx/tap   # Homebrew 7+ won't load third-party taps until you trust them
brew install JamesRyanATX/tap/fcbnerd
```

Or from source without Homebrew (Xcode or the Swift toolchain, macOS 13+):

```sh
swift build -c release
cp .build/release/fcbnerd /usr/local/bin/
```

## Usage

```
fcbnerd [listen] [--source NAME] [--format json|text] [--bind BINDING]... [--quiet] [--shell PATH]
fcbnerd list [--format json|text]
fcbnerd simulate
```

- **`listen`** (default) connects to every MIDI source, or only those whose
 name contains `--source`, and streams events until interrupted. It follows
 hotplug: unplug the interface mid-set and plug it back in, and the stream
 carries on with `disconnected` / `connected` lines.
- **`list`** prints the sources available right now.
- **`simulate`** publishes a virtual MIDI source named `fcbnerd simulator`
 that plays synthetic presses, a pedal sweep and a sysex message on a loop.
 Run it in one terminal and `fcbnerd` in another to build a consumer with no
 pedal attached.
- **`--format text`** prints aligned columns for eyeballing, including a
 `bind=` pattern for each message you can bind. Scripts should use the
 default JSON; the text layout may change.
- **`--bind`** runs a command when a message matches; see below.
- **`--quiet`** stops printing events, leaving only the bound commands.
- **`--shell PATH`** picks the shell that runs bound commands (default
 `/bin/sh`).

Status messages go to stderr; stdout carries only events. Each line is
flushed as soon as it's written, so pipes see events immediately.

## Binding commands

First find out what your pedal sends. Run `fcbnerd -f text` and press the
switch:

```console
$ fcbnerd -f text
16:30:41.115  pc                channel=1 program=7  bind=pc:1:7  [USB MIDI Interface]
16:30:41.115  cc                channel=1 controller=20 value=127  bind=1:20:127  [USB MIDI Interface]
```

Then bind a command to that pattern:

```sh
fcbnerd --bind '1:20:127=open ~/Downloads'
```

A binding is `PATTERN=COMMAND`. Everything after the first `=` is the command,
so it can contain `=` and `:` itself. Use `--bind` as many times as you like.
Every binding that matches a message starts, in the order given, and they run
at the same time.

| Pattern | Matches |
|---|---|
| `CHANNEL:CONTROLLER:VALUE` | Control change, e.g. `1:20:127`. `cc:1:20:127` also works. |
| `pc:CHANNEL:PROGRAM` | Program change, e.g. `pc:1:7`. |

Any number can be `*`: `1:30:*` is every value of controller 30 on channel 1,
which is how you bind an expression pedal.

Commands run in the background through `/bin/sh -c`, or the shell you give
with `--shell`. Their stdin is `/dev/null`. Their stdout goes to fcbnerd's
stderr, so it can't corrupt the event stream; with `--quiet` it goes to
stdout. They see these environment variables:

| Variable | |
|---|---|
| `MIDI_TYPE` | `cc` or `pc` |
| `MIDI_CHANNEL` | 1–16 |
| `MIDI_CONTROLLER`, `MIDI_VALUE` | For `cc` |
| `MIDI_PROGRAM` | For `pc` |
| `MIDI_SOURCE` | MIDI source name |

```sh
# Expression pedal sets output volume
fcbnerd -q --bind '1:30:*=osascript -e "set volume output volume $((MIDI_VALUE * 100 / 127))"'
```

Every stomp runs the command, so two quick presses run it twice even if the
first run hasn't finished. That also means every matching message starts a
shell. Keep broad patterns like `*:*:127` or `pc:*:*` away from noisy devices.

Pedal sweeps are the exception. A sweep sends dozens of values a second, so
for a binding with a `*` value, only one copy of the command runs at a time
for each control (channel and controller). While it runs, fcbnerd keeps only
that control's newest value and runs it next, which keeps the shell count down
and still ends on the pedal's final position. If a command is still running
after 5 seconds, fcbnerd says so on stderr.

A command that exits non-zero gets its binding and exit status printed to
stderr. Stopping fcbnerd (Ctrl+C, `kill`, closing the terminal, or a closed
stdout) sends SIGTERM to any command still running, including processes it
started.

### Shell functions

Functions and aliases from your interactive shell aren't loaded in `sh -c`.
In bash, export a function to make it visible (macOS's `/bin/sh` is bash, so
the default shell sees it):

```bash
greet() { say "preset $MIDI_PROGRAM"; }
export -f greet
fcbnerd -q --bind 'pc:1:*=greet'
```

zsh can't export functions. Put them in a file and source it with zsh:
`--shell /bin/zsh --bind 'pc:1:*=source ~/.fcbnerd.zsh && greet'`.

### On/off switches

The FCB1010 sends nothing when you let go of a switch (see
FCB1010 notes), so a binding fires on the press only. For
on/off behavior, keep the state in the command, for example by toggling a
file in `/tmp`.

## Output

`fcbnerd listen` prints one JSON object per line. Every object has `type`,
`source` (the MIDI source's display name) and `time` (when fcbnerd received
the message: ISO 8601, UTC, milliseconds). Channels are 1–16; note,
controller, program, velocity and pressure values are the raw 0–127 MIDI
values.

| `type` | Extra fields | Notes |
|---|---|---|
| `pc` | `channel`, `program` | Program change. `program` is 0-based on the wire. |
| `cc` | `channel`, `controller`, `value` | Control change: switches and expression pedals. |
| `note_on` | `channel`, `note`, `velocity` | |
| `note_off` | `channel`, `note`, `velocity` | Also emitted for note-on with velocity 0. |
| `poly_pressure` | `channel`, `note`, `pressure` | |
| `channel_pressure` | `channel`, `pressure` | |
| `pitch_bend` | `channel`, `value` | 0–16383, center 8192. |
| `sysex` | `length`, `data` | `data` is lowercase hex including the `f0`…`f7` framing; `length` counts those bytes. |
| `connected` | | A source appeared and is being listened to. Always precedes that source's events. |
| `disconnected` | | A source went away. A message already in flight may still follow it. |

System real-time messages (MIDI clock and so on) and system common messages
(song position, MTC) are not emitted. New event types or fields may be added
in future versions; existing ones won't change meaning. Consumers should
ignore types and fields they don't recognize.

Read the stream promptly. If a consumer stops reading, fcbnerd queues events
in memory and delivers them all when reading resumes, so a stalled consumer
will act on a burst of stale presses.

`fcbnerd list --format json` prints a different shape, one line per source:
`{"type":"source","name":"UM-ONE","id":-1234567}`. `id` is the CoreMIDI
unique ID.

## Example

`examples/developer.sh` is a complete, commented
setup for software engineers. Run it with `DRY_RUN=1` first to see what each
switch would do.

| Control | Action |
|---|---|
| Switch 1 | Open your home folder in Finder |
| Switch 2 | Open Mail |
| Switch 3 | Open iTerm |
| Switch 4 | New Chrome window, starting at the profile picker |
| Switch 5 | Open Claude |
| Switch 6 | Mute or unmute the microphone |
| Switch 7 | Screenshot an area or window to the clipboard |
| Switch 8 | Close the active Chrome tab |
| Switch 9 | Quit the active application |
| Switch 10 | Lock the screen |
| Expression pedal A | Output volume |
| Expression pedal B | Spotify or Music volume |

### Shell and jq

Program 0 switches to the next Space, and program 1 to the previous one. This
needs more than one Space, the "Move left/right a space" shortcuts
enabled (the default) in System Settings → Keyboard → Keyboard Shortcuts →
Mission Control, and for your terminal app both Accessibility permission and
Automation permission to control System Events. macOS asks for the Automation
permission the first time.

```sh
fcbnerd | jq --unbuffered -r 'select(.type == "pc") | .program' |
while read -r program; do
  case "$program" in
    0) osascript -e 'tell application "System Events" to key code 124 using control down' ;;
    1) osascript -e 'tell application "System Events" to key code 123 using control down' ;;
  esac
done
```

### Hammerspoon

Program 0 toggles play/pause, and an expression pedal on CC 30 sets the output
volume. Output can arrive in
partial chunks, so buffer until a newline. The path is for Apple Silicon;
Homebrew on Intel installs to `/usr/local/bin`.

```lua
local buffer = ""
fcbnerd = hs.task.new("/opt/homebrew/bin/fcbnerd", nil, function(_, stdout, _)
  buffer = buffer .. stdout
  for line in buffer:gmatch("([^\n]*)\n") do
    local event = hs.json.decode(line)
    if event and event.type == "pc" and event.program == 0 then
      hs.eventtap.event.newSystemKeyEvent("PLAY", true):post()
      hs.eventtap.event.newSystemKeyEvent("PLAY", false):post()
    elseif event and event.type == "cc" and event.controller == 30 then
      hs.audiodevice.defaultOutputDevice():setVolume(event.value / 127 * 100)
    end
  end
  buffer = buffer:match("[^\n]*$")
  return true
end)
fcbnerd:start()
```

## FCB1010 notes

Things about the pedal that consumers need to handle:

- A press sends one message and letting go sends nothing. On/off behavior
 (first press "on", second "off") has to be tracked by the consumer.
- The factory presets send different CC numbers from the same switch
 depending on which preset is active. Run `fcbnerd -f text`, press each
 switch you plan to use, and note what it sends.
- Pressing a switch also re-sends that preset's expression-pedal values, so
 not every `cc` on a pedal's controller means the foot moved.
- The expression pedals don't reach the full 0–127 range. Part of the travel
 sends nothing and the sweep covers roughly two-thirds of the values, so
 rescale to the range you actually see.
- The pedal has 5-pin DIN MIDI only. You need a USB MIDI interface, which
 shows up as the `source` name.

## Development

```sh
swift build
swift test                                 # decoder, formatter and binding tests
.build/debug/fcbnerd simulate &            # fake pedal
.build/debug/fcbnerd --format text         # watch it
```

`Sources/FCBNerdCore` decodes CoreMIDI's Universal MIDI Packets, formats
output and parses bindings. It has no CoreMIDI dependency, so its tests run
without hardware.
`Sources/fcbnerd` is the CLI: CoreMIDI connections, hotplug and the
simulator.

To release, bump `version` in `Sources/fcbnerd/main.swift`, commit, and push a
matching tag:

```sh
git tag -a v1.2.3 -m "fcbnerd 1.2.3" && git push origin v1.2.3
```

The release workflow tests, publishes a
GitHub Release with a universal binary, and updates the formula in
JamesRyanATX/homebrew-tap.

## License

MIT

# Nowdex — AI agent usage on Mac, iPhone & iPad

## 评论（21/21）

> **_def** · 2026-09-15T00:46:42.000Z　
> I always thought using something like this for debugger shortcuts could be fun

---

> **NewJazz** · 2026-09-15T00:48:03.000Z　
> This is dope. Would love to bring it to linux

---

> **_kb** · 2026-09-15T02:51:07.000Z　
> This is like vim pedal (https://github.com/foxweb/vim-pedal) on steroids. I love it.

---

> **tristanMatthias** · 2026-09-15T02:58:12.000Z　
> I have one of these! And I almost made this exact thing myself! Love this thank you. PS would love a little UI for this if there isn't one already

---

> **ashtuchkin** · 2026-09-15T03:03:29.000Z　
> Love it! Trying to use it with my nanoPAD2 and it only outputs `note_on` and `note_off` events. Can we bind on these? Example output:22:56:38.740 note_on channel=1 note=36 velocity=89 [nanoPAD2 PAD]

---

> **aguynamedben** · 2026-09-15T03:20:00.000Z　
> This would be sick for video game keybinds!

---

> **rahulmax** · 2026-09-15T05:47:42.000Z　
> Love this! In the photography community, we had MIDI2LR (MIDI to Lightroom) (https://rsjaffe.github.io/MIDI2LR/)I used Behringer Xtouch Mini mapped to Lightroom. This allows tactile controls, and also lets you keep your eyes on the photo being edited, instead of the constant back and forth between the controls and the photo.

---

> **scottyeager** · 2026-09-15T06:25:18.000Z　
> I picked up a couple of foot pedals built to control manual transcription software from thrift stores. That was years ago and I hacked them to control music software instead. Then one day I got Nvidia's Parakeet model running locally and was sold on automatic transcription in an instant. So in an ironic twist, I started using one of my spare transcription pedals to do transcription by wiring it up to a harness for Parakeet. It's great and the setup is basically trivial to create these days on Linux with a bit of help from an agent.

---

> **simongray** · 2026-09-15T06:49:49.000Z　
> Other than the novelty of being able to press buttons with your feet, why is this useful?If you lack special buttons, you could also just buy a bigger keyboard (or a MIDI controller that sits on the table).

---

> **webprofusion** · 2026-09-15T08:02:45.000Z　
> Funny I just built a custom midi controller firmware and configuration manager app for the Line 6 Pod GO (which is traditionally not a full midi controller):https://www.reddit.com/r/Line6podgo/comments/1wgo1tr/pod_go_...

---

> **exceptione** · 2026-09-15T08:14:17.000Z　
> As an organ player, I sometimes dream of having a full midi pedal under my desk. Would be an easy way to get some extra exercise. The problem though is that I don't think such a thing is compatible with a comfy office chair. The polished wood of an organ bench isn't comfortable but it allows for mobility.

---

> **ddmf** · 2026-09-15T08:16:14.000Z　
> I used a usb foot pedal with three switches for playing world of warcraft - originally bought it for PTT but realised how useful it was and ended up using it for the speed boost spell and the big damage cooldown.This takes it to the next level!

---

> **quietlathe** · 2026-09-15T09:24:36.000Z　
> Remember setting up my FCB1010 for guitar effects back in the day. Using it for macOS macros is such a clever pivot!

---

> **DylanMerigaud** · 2026-09-15T09:52:32.000Z　
> Looks solid, best of luck with it.

---

> **c-hendricks** · 2026-09-15T14:50:27.000Z　
> Love my FCB1010. Absolute beast that's no worse for wear after 20 years and countless moves.

---

> **edwardbonnett** · 2026-09-15T19:02:57.000Z　
> quite tempted to use this to start and stop game recordings

---

> **wyre** · 2026-09-15T01:33:23.000Z　
> Repo is 2,500loc, all-in, according to SCC. Should be really easy to point your favorite coding agent at the repo and have it one or two shot something similiar in the language of your choice.

---

> **tetraodonpuffer** · 2026-09-15T01:59:40.000Z　
> I have something like this in linux using a novation launchcontrol, it's quite straightforward using aseqdump, say I use the buttons to switch desktops, I have this launched as part of my session and always in background. While developing this I just printed $line to see what aseqdump sent to figure out the regexes while IFS=' ' read -r line; do
>  if [[ "$line" == *"client"*"Launch Control"\* ]]; then
>  device=$(echo "$line" | cut -d' ' -f2)
>  fi
>  done < <(aconnect -i)
>
>  aseqdump -p ${device::-1} | while IFS=' ' read -r line; do
>  if [[ "$line" == *"Note on"* ]]; then
>  note=$(echo "$line" | grep -o "note [0-9]*" | cut -d' ' -f2)
>  if [ "$note" == "9" ]; then
>  wmctrl -s 8
>  fi
>  elif [[ "$line" == *"Control change"*"127" ]]; then
>  note=$(echo "$line" | grep -o "controller [0-9]*" | cut -d' ' -f2)
>  if [ "$note" == "114" ]; then
>  # some macro
>  fi
>  fi
>  done

---

> **aguynamedben** · 2026-09-15T03:19:46.000Z　
> Sir, Emacs pedals came way earlier, we needed to avoid "Emacs pinky"!

---

> **Bad_CRC** · 2026-09-15T07:45:08.000Z　
> Darktable also supports Midi controls, I played with it with a korg nano kontrol back in the day.

---

> **alexfoo** · 2026-09-15T10:39:22.000Z　
> You can keep your hands on the keyboard. Some people find having to move them away from their usual home place breaks their flow.Sure there are things like an Elgato StreamDeck that you can do similar things with but they still require you to move a hand from the keyboard.I suppose it is similar to using voice control things like Alexa. Setting a timer by hand in the kitchen isn’t exactly hard but it is so much more convenient to do it by voice if your hands are covered in raw chicken juice or the like.

## 导航

- 项目页：[[10-项目/github.com_d8eab146]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
