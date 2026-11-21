---
type: "corpus"
item_id: "989a9c761df638b8"
title: "Show HN: Factuio – A factory TUI game written in Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50585876"
project_url: "https://github.com/ja7er/factuio"
author: "merlin_sh"
published_at: "2026-11-21T04:15:03Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-21"
tags:
  - 语料
  - hn_show
  - author_merlin_sh
  - story_50585876
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Factuio – A factory TUI game written in Rust

> [!info] 一句话导读
> License: GNU General Public License v3.0

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50585876>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：merlin_sh　|　发布：2026-11-21T04:15:03Z
> 项目链接：<https://github.com/ja7er/factuio>
> 采集：2026-11-21T14:45:01+08:00　|　id：`989a9c761df638b8`

## 正文

# ja7er/factuio

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: GNU General Public License v3.0
- Homepage: https://factuio.com
- Default branch: main
- Created: 2026-11-15T02:47:58Z

## Languages

- Rust

## Top Contributors

- claude (14 contributions)
- ja7er (14 contributions)

---

## README

 A factory-automation game for your terminal, written in Rust with ratatui.

Start with a handful of buildings on a procedurally generated map. Mine ore, smelt it,
move it around on conveyors, arms and rail carts, explore beyond the fog, craft parts,
research new technology, and finally build the **Uplink array** and feed it 20 relay modules
to win. New to it? Pick **Tutorial** under New game. An original soundtrack, synthesized live
as you play, keeps you company (`J` turns it off).

A mid-game factory: conveyor lines feeding fabricators that make cogs and coils

## Install and run

Download a prebuilt binary for Linux, macOS or Windows from the
Releases page, unpack it and run `factuio`.
On macOS, if Gatekeeper blocks the unsigned binary, run `xattr -d com.apple.quarantine factuio`.

Or build from source with a recent Rust toolchain (edition 2024, Rust 1.85+):

```sh
cargo run --release
```

Options:

```
--new             start a new game immediately
--continue        load the save file immediately
--seed <N>        world seed for a new game
--scenario <ID>   start a scenario: standard, tutorial, far-fields, lean, sprint
--save <PATH>     save file location (default: ~/.factuio/save.json)
--ascii           ASCII-only glyphs (for terminals without Unicode arrows)
--256             force 256-colour mode (macOS Terminal.app, older terminals)
--truecolor       force 24-bit colour
--no-music        keep the music off this session
--export-music <DIR>
                  write the soundtrack to DIR as WAV files and exit
```

A terminal of at least 100×30 is recommended. Colours are 24-bit when your terminal
advertises it through `COLORTERM`; otherwise they fall back to the 256-colour palette.

## Screenshots

| | |
| --- | --- |
| Title screen | Starter base: diggers feeding kilns, arms moving ingots into crates |
| Title screen | A starter base: diggers feeding kilns, arms unloading into crates |
| Crafting and inventory | Research tree |
| Hand crafting, with missing intermediates made automatically | The research tree |
| Inspecting a fabricator | Production statistics |
| Inspecting a fabricator | Production statistics, with the last ten minutes of each item |

## Controls

| Key | Action |
| --- | --- |
| Arrows / WASD | Move the cursor (Shift or capital WASD: 8 tiles) |
| 1–9, 0 | Select a building from the hotbar |
| b | Building list (press 1–0 there to assign hotbar slots) |
| Space / Enter | Place the selected building, or inspect what's under the cursor |
| r | Rotate the building you're placing (or the one under the cursor) |
| v | Paint mode: moving the cursor keeps building; conveyors follow your path |
| q | Clear selection / pick the building under the cursor (fabricators keep their recipe) |
| x / Delete | Pick up a building and everything inside it |
| u | Undo the last build or pick-up (a paint stroke, drag or paste is one step) |
| z | Select an area, then `x` to pick it all up or `y` to copy it as a blueprint |
| e | Inspect: `t` take, `i` insert, `f` add 10 fuel, `r` recipe or rotate |
| m | Mine the ore under the cursor by hand |
| c / i / Tab | Crafting and inventory (`Enter` 1, `f` 5, `F` max, `x` cancel) |
| t | Research tree (`Enter` research or queue, `n` switch now, `x` clear queue, `Tab` tree or list) |
| g | Production statistics (rates over the last minute, and a 10-minute sparkline per item) |
| l | Message log |
| n | Jump to the next building with a problem |
| M | Map overview |
| o | Power coverage overlay |
| p / f | Pause / 4× fast-forward |
| J | Music on or off (volume: ←/→ on Music in the Esc menu) |
| F5 / F9 | Quick save / quick load the current slot (asks first) |
| Esc | Menu (save to or load one of 5 slots, colour-blind palette, music, quit) |
| ? | Help |

**Mouse:** left click places or inspects, left drag lays buildings along the path (or selects an
area when nothing is selected), right click or drag picks up, the wheel scrolls, and the hotbar
is clickable.

**Upgrading in place:** placing an express conveyor, swift or filter arm, electric bore or arc
furnace over its basic version swaps it, and the old one goes back to your inventory.

**Tunnels:** place a tunnel belt, then a second one up to five tiles further along facing the same
way. The second becomes the exit and items travel underground between them, past buildings and
crossing belts. Inspect either end (`e`) and press `v` to swap entrance and exit by hand.

**Blueprints:** copy an area with `z` … `y`, then `Enter` places it at the cursor, `r` rotates
it and `Esc` drops it.

**Rails:** lay rails with paint mode (`v`) or a drag; they join up with the rails and depots next
to them. Put a rail cart on a depot from the build list (`b`). Inspect a depot and press `v` to
switch it between loading and unloading carts. `x` on a cart picks it up with its cargo.

The game autosaves every five minutes, and when you press Ctrl+C or close the terminal,
to a separate `save.autosave.json`, so it never overwrites a save you made yourself.
**Continue** picks whichever save is newest. Every save also keeps the previous file as `.bak`.

### Settings

`~/.factuio/settings.json` (next to your save) is created on first run:

```json
{
  "mouse": true,
  "palette": "default",
  "ascii": false,
  "autosave_minutes": 5,
  "music": true,
  "music_volume": 70,
  "keys": { "mine": "k" }
}
```

`palette` is `"default"` or `"colorblind"`, which swaps the red/green signals (working,
problems, datapacks) for blue/orange ones; the pause menu switches it too. `keys` remaps
play-screen actions: `rotate`, `paint`, `pick`, `remove`, `inspect`, `mine`,
`build_menu`, `craft`, `research`, `stats`, `log`, `power_overlay`, `pause`, `fast`,
`select_area`, `undo`, `next_alert`, `minimap`, `music`. Set `autosave_minutes` to 0 to turn
autosave off, and `mouse` to false to keep your terminal's own text selection. `music` and
`music_volume` (0 to 100) are what `J` and the pause menu change.

### Music

The game plays six original pieces, about 13 minutes in all, one after another:

| Track | Mood |
| --- | --- |
| Morning Shift | Harp, flute and celesta on a bright morning, F major |
| Ore and Ember | Slow, spacious piano under the stars, D major |
| Conveyor Waltz | A waltz for strings, flute and piano, A minor with a C major middle |
| Night Grid | Night shift: pulsing sequencer, drums and a slow synth melody, E minor |
| Kingdom of Cogs | A modal folk march for recorder, lute and drum, D Dorian |
| Terminal Dreams | Chiptune: square lead, fast arpeggios and noise drums, C minor |

Nothing is a recording. The notes are written in `src/music/score.rs` and played by a small
synthesizer (`src/music/synth.rs`: plucked strings, FM bells, a piano, bowed strings, chip
waves, drums, and a reverb) on its own thread. On Linux the game loads ALSA when the music
starts, so it still runs, silently, where there is no sound system (over SSH, for example).
macOS and Windows use the system's default output.

The same tracks, rendered, are in `music/` as OGG and MP3 files.

## How it plays

**New game.** Choose what to play:

| Scenario | What's different |
| --- | --- |
| Free play | A new random world (or `--seed N`) |
| Tutorial | A guided first hour: a card on the map walks you through mining, smelting, belts, power, arms and research |
| Far fields | No malachite or quartz near spawn; the nearest is 50–60 tiles out in the fog. Starts with rails, depots, a cart and a survey mast |
| Lean ores | The starter patches hold a third of the usual ore |
| Sprint | Make 60 Beta datapacks in fabricators, against the clock |

Challenges use the same map for everyone, and keep their own best times in `records.json`.

**Resources.** Four ores spawn near the start, with richer patches further out:
ferrite, malachite, lignite (fuel) and quartz. The further from spawn, the richer the patch.

**Exploring.** The map is 320×240 tiles and starts out hidden beyond the area around spawn.
Every building reveals a few tiles around itself (pylons more), so building outward explores, and
a powered survey mast (Surveying) reveals up to 50 tiles around itself. You can only build where
you've explored.

**Rail carts.** For ore that's too far to belt (Railways): rails, depots that store 800 items, and
carts that carry 400 at 8 tiles a second. A cart visits the depots on its track in turn, so two
depots make a shuttle. At a loading depot it leaves when full, when nothing has arrived for five
seconds, or after thirty; at an unloading depot it empties out first.

**Production chain.**

```
ferrite ──kiln──▶ iron ingot ──▶ cog, conveyor, crate ...
malachite ─kiln─▶ copper ingot ─▶ copper coil ─▶ logic chip
quartz ──kiln──▶ glass ─────────▶ lens (Optics)
iron ingot ×5 ─kiln─▶ steel beam (Metallurgy) ─▶ motor (Motors)
chip + lens + coil ─▶ processor (Computing)
water (pump) + lignite ─chem plant─▶ resin (Chemistry) ─▶ battery (Energy storage)
processor + battery + resin ─▶ delta datapack (Field theory)
processor + motor + steel ─▶ relay module ─▶ Uplink array ★
```

**Power and terrain.** Days last six minutes: sun panels give full power by day, fade at dusk and
stop at night, so battery banks (Energy storage) earn their place. Pumps draw water from the
tile behind them for steam turbines (2400 kW, and 50% more energy from fuel than a generator) and
chem plants. Arc furnaces bake lignite into coke, which burns 2.5 times as long. Sifters pull
endless quartz out of sand, and landfill turns water into buildable sand.

**Modules.** Speed modules (+50% speed, +50% power) and productivity modules (a free batch every
ten, 15% slower) go into bores, sifters, arc furnaces, fabricators, chem plants and labs by hand.

**After the win.** Your winning time is saved in `~/.factuio/records.json`, with your best on that
seed and overall shown on the victory screen. The Uplink keeps transmitting: every milestone (40,
80, 160, …) makes each transmission take longer. Mining productivity and Servo tuning are endless
research, each level 10% faster and pricier than the last.

**Buildings.**

| Map | Building | Notes |
| --- | --- | --- |
| `D→` | Digger | Burns lignite, mines the 3×3 area under it, pushes ore ahead |
| `B→` | Electric bore | Electric, twice as fast (Electric mining) |
| `K` | Kiln | Burns lignite to smelt |
| `E` | Arc furnace | Electric, twice as fast (Arc smelting) |
| `→→` | Conveyor / express conveyor | Items ride on it, shown by their letter; side-loading works |
| `Y→` | Splitter | Shares items in turn between the belts ahead, left and right; skips any that are full (Belt routing) |
| `→∪` `∩→` | Tunnel belt | Entrance and exit, up to 4 tiles apart underground (Belt routing) |
| `ɑ→` | Arm / swift arm | Grabs from behind, drops ahead; only picks what the target can use |
| `ɑ→` | Long arm | Orange. Reaches two tiles each way, over whatever is in between (Logistics) |
| `ɑ→` | Filter arm | Purple. A swift arm that moves only the item you pick with `e` then `f` (Sorting) |
| `C` | Crate | Stores 800 items |
| `G` | Generator | Burns lignite for 900 kW |
| `P` | Pylon | Powers a 5×5 area and links to pylons up to 7 tiles away |
| `S` | Sun panel | Free 60 kW (Solar power) |
| `M` | Fabricator | Electric assembler for any crafting recipe (Fabrication) |
| `L` | Lab | Consumes datapacks for the current research |
| `U` | Uplink array | Win condition (Uplink theory) |
| `W→` | Pump | Place with water behind; 2 water/s ahead, no power (Hydraulics) |
| `T` | Steam turbine | Fuel + water for 2400 kW (Hydraulics) |
| `Q→` | Sifter | Electric, endless quartz from the sand under it (Sifting) |
| `H` | Chem plant | Electric assembler for resin and batteries (Chemistry) |
| `A` | Battery bank | Stores 20 MJ, up to 600 kW in or out (Energy storage) |
| `V` | Survey mast | Electric; reveals the map up to 50 tiles around it (Surveying) |
| `═╗` | Rail | Track for rail carts; joins the rails and depots beside it (Railways) |
| `R+` `R-` | Depot | Rail stop holding 800 items: carts load at `+`, unload at `-` (Railways) |
| `■` | Rail cart | Shuttles between depots with up to 400 items (Railways) |

**Power.** Each pylon network sums its generators and panels. When demand exceeds
supply every machine on that network slows down proportionally. The top bar shows demand
against supply over all networks (`⚡ 515 kW/1.8 MW`), turning yellow or red when a network
falls short, and how full the battery banks are.

**At a glance.** A building with a problem blinks a `!` on the map, and `n` jumps to it. Working
kilns glow and smoke, generators flicker, and arms swing what they carry across their tile.

**Research.** Twenty-five technologies use Alpha, Beta, Gamma and Delta datapacks, plus two
endless ones. Pick one with `t`, then keep your labs supplied. On a wide terminal the research
screen draws the tree tier by tier, picking out what the selected tech needs and leads to.

The sidebar always shows a **Goal** line telling you what to do next.

## Development

```sh
cargo test            # simulation, crafting, save/load, UI rendering, scripted playthroughs
cargo clippy --all-targets
```

The screenshots are rendered from the real UI: `FACTUIO_DUMP= cargo test dump_screens -- --ignored`
writes HTML snapshots of each screen (and the logo) that can be captured with any headless browser.

Code layout:

- `src/items.rs`: items, buildings, directions
- `src/recipes.rs`: recipes and the tech tree
- `src/world.rs`: map generation, fog of war and the tick simulation (belts, arms, miners, furnaces, fabricators, labs, power, rail carts)
- `src/game.rs`: player inventory, hand crafting, building actions, save/load
- `src/scenario.rs`: free play, the tutorial steps and the challenges
- `src/records.rs`: best times
- `src/app.rs`: screens and keyboard handling
- `src/ui.rs`: ratatui rendering
- `src/music/`: the soundtrack: score, synthesizer, and sound output
- `src/playtest.rs`: scripted playthroughs used by the tests

The simulation runs at 20 ticks per second and is deterministic for a given seed.

# TriHerm/voxstead

## 关联链接

- https://factuio.com

## 导航

- 项目页：[[10-项目/github.com_c5448aeb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
