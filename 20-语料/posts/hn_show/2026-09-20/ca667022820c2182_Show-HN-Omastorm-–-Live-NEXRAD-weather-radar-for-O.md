---
type: "corpus"
item_id: "ca667022820c2182"
title: "Show HN: Omastorm – Live NEXRAD weather radar for Omarchy"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49724718"
project_url: "https://github.com/wesleygrimes/omastorm"
author: "wesgrimes"
published_at: "2026-09-16T11:01:01Z"
captured_at: "2026-09-20T09:37:04+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_wesgrimes
  - story_49724718
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Omastorm – Live NEXRAD weather radar for Omarchy

> [!info] 一句话导读
> wesleygrimes/omastorm

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49724718>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：wesgrimes　|　发布：2026-09-16T11:01:01Z
> 项目链接：<https://github.com/wesleygrimes/omastorm>
> 采集：2026-09-20T09:37:04+08:00　|　id：`ca667022820c2182`

## 正文

# wesleygrimes/omastorm

An Omarchy-native NEXRAD radar viewer built with Rust and Quickshell.

- Stars: 117
- Forks: 33
- Watchers: 117
- Open issues: 25
- License: MIT License
- Homepage: https://omastorm.com
- Default branch: main
- Created: 2026-09-04T22:46:29Z

## Languages

- GLSL
- HTML
- JavaScript
- Python
- QML
- Rust
- Shell

## Topics

- hyprland
- linux
- nexrad
- noaa
- omarchy
- omarchy-plugin
- qml
- quickshell
- radar
- rust
- wayland
- weather
- weather-radar

## Top Contributors

- wesleygrimes (70 contributions)
- allcontributors[bot] (3 contributions)
- shieldsworks (2 contributions)
- airtwo (1 contributions)
- nixfred (1 contributions)
- TheFifeDawg (1 contributions)
- nmorton13 (1 contributions)
- scottjones (1 contributions)

---

## README

# Omastorm

Live NEXRAD radar in your Omarchy bar. Beta.

A radar that lives next to the clock. The popover is the station nearest you
and the actual scan time. Click the map (or press Enter) for the full window:
every dish in the network, the sweep at native resolution, a two-hour loop
you can play and scrub, drawn in your Omarchy theme.

This page is the user guide: install, first run, and everyday use. How the
code is built lives in CONTRIBUTING.md.

## Install

Omarchy 4 on x86_64 and aarch64.

```sh
omarchy plugin add https://github.com/wesleygrimes/omastorm.git --enable
```

That clones the plugin, asks which bar section to use, and on first open
downloads the pinned engine from GitHub Releases, checks its sha256, and
installs it under `~/.local/share/omastorm/bin`. Configuration, remembered
view, and cached scans stay in Omastorm's own directories.

Optional: a Hyprland key to toggle the window. Add one line to
`~/.config/hypr/bindings.lua`. Omastorm never writes that file:

```lua
o.bind("SUPER + SHIFT + R", "Omastorm", "omarchy shell shell toggle com.omastorm.radar '{}'")
```

Optional: list it in the app launcher:

```sh
bash ~/.config/omarchy/plugins/com.omastorm.radar/scripts/write-desktop-entry.sh
```

## First run

Open the popover from the bar. If Omarchy weather already has a city, the
map opens there. If not, you get a choice: pick a place, or use an
approximate location.

Choose your location

**Use approximate location** is one click. It asks wttr.in
to guess your city from the public IP of that request. Nothing is sent until
you click; there is no GPS and no background tracking. A VPN or CGNAT may
land you at the ISP instead of your house. Choose manually if the guess is
wrong.

The view is remembered. Next time you open the popover, you are back where
you left off.

## What you are looking at

NEXRAD is NOAA's network of weather radars. Each dish spins, sends a pulse,
and measures how much bounced back. Omastorm shows **reflectivity** on the
lowest tilt: the beam that stays closest to the ground.

Color is **dBZ**, not a rain rate and not a warning. Stronger return, warmer
color. The legend under the map is that scale.

A bright blob is often rain or snow. The same beam also sees:

- insects, birds, and bats (especially on clear evenings)
- dust, smoke, and sea spray
- ground clutter and buildings near the dish
- anomalous propagation, when the beam bends and paints the ground far away
- wind farms, towers, and military chaff

Measured returns under 5 dBZ (the usual biological clutter and haze) are
hidden by default; the legend says so. Press `w` to show them.

This is not a forecast, and it is not the NWS warning stack. It is the sweep
that dish published, with the scan time on the stamp.

## The window

Drag to pan, scroll to zoom. The map and the radar are independent: panning
moves the camera; the dish is whichever station the map is following, unless
you lock it.

Click the station name for nearby dishes. The padlock pins that radar so
panning will not hand off; it turns yellow when the camera sits outside that
dish's rings. `n` picks the nearest radar and leaves the camera where it is.

The number under the product line is how stale the frame on screen is. The
stamp above the timeline is when that sweep was observed. **LIVE** is the
feed; the light beside it goes yellow when data is stale (ten minutes) and
red when the station or the bucket is unreachable. Cached frames stay.

A scale bar on the map is ground distance, in kilometres or miles from your
locale.

## Search

`/` (or `s`) is one field. Type a city, a site id, or paste coordinates.

A **city** centres the map there, unlocks, and selects the nearest radar.

Search a city

A **site** (`KTLX`, `tlx`) locks that dish and centres on it. Clicking the
station title opens the same card on the nearest dishes.

Search a radar site

**Coordinates** are latitude then longitude, decimal degrees, comma or space,
the way a maps link looks. Invalid range is named on the card; the layout
does not jump.

Paste coordinates

Coordinates out of range

## My location

The map-marker at the top-left of the map, or `m`, jumps to the same
approximate IP location as first run. Zoom stays. The radar unlocks and
follows. Archived sessions never locate.

If the lookup fails, the camera stays put and a short overlay appears on the
map. It is not a new row of chrome.

Approximate location failed

## The loop

A station you arrive at fetches recent scans so there is something to play
within a few seconds. The cache then grows toward **60 frames / two hours**.
Older scans drop out. Space loops them; `[` `]` steps; Home and End jump.

NOAA publishes Level II via the Open Data program on AWS.
A full volume takes about four to seven minutes (faster in severe weather,
slower in clear air). While a volume is in progress the engine reads live
chunks, so the sweep can paint as the antenna turns. If no new chunk arrives
for 90 seconds it rediscovers the latest volume; cached frames stay.

## Look

Three treatments sample the same gate and palette. They only change how each
3 px cell is painted. Glyphs is the default; `1` `2` `3` switch.

| Key | Treatment | Look |
| --- | --- | --- |
| `1` | Pixels | Solid blocks. The most literal picture of each gate. |
| `2` | Glyphs | A denser mark as the return strengthens. |
| `3` | Stipple | Soft squares that grow with intensity; more map shows through. |

Pixels, Glyphs, and Stipple

Chrome follows the Omarchy theme. Radar color comes only from the sweep.

`?` lists every key. They are all rebindable.

| Key | Action |
| --- | --- |
| `h` `j` `k` `l` or arrows | Pan |
| `+` `-` | Zoom |
| `0` | Reset to the configured or weather location |
| `/` or `s` | Search |
| `n` | Nearest radar (camera stays) |
| `Shift+L` | Lock the station |
| `m` | My location |
| Space | Play / pause the loop |
| `[` `]` | Step a frame |
| Home / End | Oldest or newest frame |
| `1` `2` `3` | Pixels, Glyphs, Stipple |
| `w` | Show weak returns |
| `?` | This map |
| Esc | Close |

## Preferences

`~/.config/omastorm/config.toml` is what you mean to keep. The last map
center, zoom, and UI radar lock are saved separately in
`~/.local/state/omastorm/state.json`. Panning never rewrites config.

```toml
# Optional: always open here. Omit both to remember the last map position.
center_lat = 36.23708
center_lon = -79.97948
# locked_radar = "KFCX"  # optional; coordinates do not lock a radar

treatment = "GLYPHS"  # PIXELS, GLYPHS, or STIPPLE at launch
weak_floor = 5        # dBZ; false draws every measured return

[keys]
pan_left = "h Left"
zoom_in = "+ ="
```

A bad value is named in the status slot and that setting stays on its
default. Keys are Qt sequences; an empty string unbinds. The `1` `2` `3` and
`w` keys change treatment and the weak-return floor for the session without
writing the file.

## Update

```sh
omarchy plugin update com.omastorm.radar
omarchy restart shell
```

Until the restart, the shell keeps running what it loaded at login, old
engine pin included. Omastorm notices the new files and says so; clicking
that notice in the popover restarts the shell.

## If something is wrong

If expand or the keybind does nothing after an update, restart the shell.

The engine is one daemon per login. Its log is
`$XDG_RUNTIME_DIR/omastorm/engine.log` (usually `/run/user/ /omastorm/`).
If the engine could not be installed, the reason is `bootstrap.log` in the
same directory; opening the popover again retries.

```sh
~/.local/share/omastorm/bin/omastorm-engine stop
```

The next popover or window starts it again.

This is a beta. Bugs, rough edges, and ideas go to
GitHub issues. For a
failure, use the
bug report template
and attach the last screenful of `engine.log` (and `bootstrap.log` if the
engine never installed). Include Omarchy version, plugin commit, and GPU as
the template asks.

## Remove

```sh
omarchy plugin remove com.omastorm.radar
~/.local/share/omastorm/bin/omastorm-engine stop
rm -rf ~/.local/share/omastorm ~/.cache/omastorm ~/.local/state/omastorm
rm -rf ~/.config/omastorm                            # keep this to reinstall later
rm -f ~/.local/share/applications/omastorm.desktop   # if you added the launcher entry
```

Then delete the `o.bind` line if you added one.

## Data

Radar: NOAA NEXRAD Level II via the NOAA Open Data program on AWS. Basemap: ©
OpenStreetMap contributors, ODbL,
tiles by OpenFreeMap; Natural Earth, public domain.
Location search: GeoNames,
CC BY 4.0.
Approximate location: wttr.in.
Code: MIT, see LICENSE.

## Contributing

Setup, checks, and pull requests are in CONTRIBUTING.md.
Read DESIGN.md before proposing a product change. Open work
that is ready for a first patch is labeled
`good first issue`
and `help wanted`.

## Contributors

Thanks to these people
(emoji key):

 Wes Grimes 💻 📖 🚧
 Scott Jones 💻
 Casey Shields 🚇 💻
 Chance Griffin 💻
 Michael Pfeifer 💻
 Fred Nix 💻
 Nathan Morton 💻

 javi ⚠️ 👀
 Ryan Robitaille 💻
 gw7523 💻 🐛
 Yaniert Pascual 📓
 Michael Yockey 🐛

This project follows the all-contributors specification.

## 关联链接

- https://github.com/wesleygrimes/omastorm.git
- https://omastorm.com

## 导航

- 项目页：[[10-项目/github.com_7d659c5a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
