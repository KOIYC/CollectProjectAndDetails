---
type: "corpus"
item_id: "b05ceac2f48e2142"
title: "rehan-remade/universal-modder"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/rehan-remade/universal-modder"
project_url: "https://github.com/rehan-remade/universal-modder"
author: "rehan-remade"
published_at: "2026-09-30T05:00:35Z"
captured_at: "2026-10-10T10:00:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-09-30"
tags:
  - 语料
  - github_new
  - Python
  - created:>2026-09-26
metrics: {"stars": 6061, "forks": 575, "open_issues": 50}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# rehan-remade/universal-modder

> [!info] 一句话导读
> <img src="docs/media/banner.png" alt="universal-modder: mod any game. Point any AI coding agent at the PC games you own. Publish your mods, remix other people's…

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/rehan-remade/universal-modder>
> 指标：stars=6061 · forks=575 · open_issues=50
> 作者：rehan-remade　|　发布：2026-09-30T05:00:35Z
> 项目链接：<https://github.com/rehan-remade/universal-modder>
> 采集：2026-10-10T10:00:54+08:00　|　id：`b05ceac2f48e2142`

## 正文

Skills, tools and a shared knowledge base that let any AI coding agent mod almost any PC game you own.
  The agent finds the game, works out the engine and the route, reads the real code, builds the mod, makes art, 3D and sound
  with fal, tests it in the running game, cuts the video, and writes down what it learned for the next agent.

Coming next: the mod hub. Publish your mods, remix other people's, and make new ones.

## Install

Pick your agent. Each gets the same skills (Agent Skills format), the fal MCP server, and the `um` CLI.

| Agent | Install |
|---|---|
| **Claude Code** | `/plugin marketplace add rehan-remade/universal-modder``/plugin install universal-modder@universal-modder` |
| **Codex** | `codex plugin marketplace add rehan-remade/universal-modder``codex plugin add universal-modder@universal-modder` |
| **Gemini CLI** | `gemini extensions install https://github.com/rehan-remade/universal-modder` |
| **VS Code / Copilot** | Enable `chat.plugins.enabled`, run **Chat: Install Plugin From Source**, and enter this repo's URL |
| **Cursor** | Cursor Marketplace, or clone (Cursor reads `AGENTS.md` and `.cursor/mcp.json`) |
| **OpenCode** | Clone and run `opencode` inside it (`opencode.json` adds the skills and the fal MCP server) |
| **Skills only**(any agent) | `npx skills add https://github.com/rehan-remade/universal-modder` |
| **Anything else** | `git clone https://github.com/rehan-remade/universal-modder` and start your agent inside it |

Inside a clone, each agent finds the skills where it looks for them: `.agents/skills` (Codex, Gemini CLI,
Copilot, Cursor, OpenCode) and `.claude/skills` (Claude Code) are copies of `skills/`. Instructions are in
`AGENTS.md`, which `CLAUDE.md` and `GEMINI.md` point to. MCP config is in `.mcp.json`, `.codex/config.toml`,
`.cursor/mcp.json`, `.vscode/mcp.json` and `opencode.json` (which also points OpenCode at `skills/`).

**The `um` CLI.** Plugin installs and clones put it on PATH. Anywhere else:
```bash
uv tool install git+https://github.com/rehan-remade/universal-modder     # or: pipx install git+...
```
**For assets,** get a [fal API key](https://fal.ai/dashboard/keys). It powers both the fal MCP server and
`um fal` (for images without a key, `um comfy` uses a local ComfyUI server):
```bash
export FAL_KEY=...
```
You also need Git, Python 3.10+ and ffmpeg. `uv` is recommended. Blender is needed for 3D → sprite renders.
Windows games are driven natively or from WSL.

## Try it
> Mod Terraria: add a homing missile launcher and a tactical nuke that craters the world. Make the sprites with fal.

> Make a new civilization for Age of Empires II with a unique unit rendered from 3D.

> Put real Minecraft inside GTA V story mode. Minecraft's camera should follow GTA's, and its TNT should blow up GTA cars.

> Port the Warthog from my Halo install into Minecraft, with a gunner on the turret.

> What engine is `C:\Games\Foo`, and has anyone modded it before?

The agent starts with the **mod-any-game** skill and runs the same loop every time:
1. search the knowledge base;
2. recon, then pick a route;
3. set up a safe lab (saves backed up);
4. read the actual code;
5. build one working slice;
6. generate assets;
7. verify in the real game;
8. record;
9. package;
10. write a field note for the next agent.

## A knowledge base that AIs write for AIs
[`knowledge/`](knowledge/) holds **field notes**: how specific games were actually modded, decompiled and
reverse-engineered. Each note gives:
- the exact versions that worked;
- the route, and why;
- what the engine really does;
- how it was verified;
- the gotchas (symptom → cause → fix).

**Every agent that finishes a mod can open a pull request with its note**, so the next agent starts where it
left off instead of rediscovering the same traps.

```bash
um kb search "grand theft auto"                 # before you start: prior art (works outside the repo too)
um kb new --game "Hades II" --title "A new boon god" --from-scan hades --agent "Codex (gpt-6)"
um kb check knowledge/games/hades-ii/a-new-boon-god.md
um kb pr knowledge/games/hades-ii/a-new-boon-god.md --yes    # after your human says OK: branch, push, PR
```
Browse [`knowledge/INDEX.md`](knowledge/INDEX.md). Every game is welcome. Contribution rules, for humans and
AIs, are in [`CONTRIBUTING.md`](CONTRIBUTING.md): no game files, no decompiled dumps, no cheating other
players, and an honest status and verification.

A few notes from the community:
- [Portalcraft: real Minecraft inside Portal 2](knowledge/games/portal-2/portalcraft-minecraft-inside-portal-2.md)
- [Halo 3 weapons, Covenant, vehicles and maps ported into Minecraft](knowledge/games/halo-3-mcc/halo-3-weapons-covenant-vehicles-and-maps-ported-into-minecr.md)
- [Bloons TD 6 inside Minecraft, with the game's rules as a headless sim](knowledge/games/minecraft/bloons-td-6-in-minecraft.md)
- [A CS2-style conversion of Elden Ring offline, as a native Rust DLL](knowledge/games/elden-ring/cs2-conversion-of-elden-ring-offline-native-rust-dll-via-me3.md)

## What's inside

**Skills** (`skills/`, Agent Skills format)

  SkillWhat it does

    mod-any-gameThe whole loop, hard safety rules, and 12 engine playbooks: Unity, Unreal, .NET/XNA (Terraria, Stardew, Celeste), Godot, Source 1/2, Bethesda, Minecraft, AoE2/Genie, RE Engine/FromSoft/GTA/Cyberpunk/BG3, native C++, indie engines (GameMaker, RPG Maker, Ren'Py, Paradox, Doom, HTML5, LÖVE, Java), retro decomps
    game-reconPrior field notes, engine and version, managed or native, anti-cheat, loaders, save folders, community route → MODDING_PLAN.md
    game-research-websearchOpen-web research that survives dead forums: Wayback/archive.today, GitHub/code and Nexus/Workshop/Thunderstore APIs, Reddit/YouTube, login-gated handoff, screenshots as evidence
    reverse-engineeringILSpy / Cpp2IL / Vineflower / Ghidra and IDA over MCP / Cheat Engine / Frida / RenderDoc; reverse-engineer a file format and prove it with a round trip
    fal-assetsSprites with real transparency, consistent variants, pixel art, seamless textures, PBR maps, image-to-3D, auto-rigging, SFX, music, voice, cutscene video
    asset-pipelineArt → engine-exact frames: cutout, nearest-neighbour fit, palettes, sheets, team-colour masks, 3D → 8/16-heading sprites
    game-automationLaunch, screenshot (GPU-safe), click/type safely, windowed mode, crash-reporter cleanup, in-game agent bridges
    showcase-videoRecord the window with only the game's audio, pick moments, cut a styled video from an EDL
    mashup-modsGame inside a game: content ports, passthrough mods (worked example: Minecraft × GTA V), decomps as libraries, reimplementations
    publish-modLint, package per platform, credits, the post
    share-field-notesSearch the knowledge base, write your own note, open the PR

**The `um` CLI** (Python). Every command has `--help` with examples.

<!-- GitHub lets images in auto-width tables shrink to nothing: the widths and the no-break spaces keep the icons at 36 px. -->

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CommandWhat it does

    um scanFind Steam/Epic/Xbox installs; fingerprint engine and version, .NET vs native, anti-cheat, installed loaders, save folders, ranked routes
    um falsprite, image, edit, rmbg, pixelate, upscale, texture, pbr, model3d, rig, sfx, music, voice, video, run, search, schema, price. Plain REST, with a manifest of every generation
    um comfystatus, image (--sprite cuts it out), run (any workflow saved with Export (API)). Images from a local ComfyUI server, no API key
    um spritecutout, fit, pixelate, palette, sheet, slice, frames, team-mask, seamless, preview
    um render3dGLB → sprite frames from the game's camera (aoe2, iso8, trueiso, topdown, side, turntable) with Blender
    um winshot, record (gfxcapture + process-loopback audio), drive (input that only reaches the game), ps, kill, launch, reg
    um videocontact sheets, compile (EDL → titled, beat-cut video with music), mux, beats, first-frame
    um backupSnapshot, diff and restore save folders
    um publish checkBlocks shipping game files, decompiled code and leaked keys
    um kbThe knowledge base: search, show, new, check, index, sync, pr

Two no-build Windows tools ship inside the package (`um/ps1/`): WinDrive input and ProcLoopback game-only
audio, both PowerShell with embedded C#.

## Built with it
- **[examples/terraria-tmodloader](examples/terraria-tmodloader)**: *Fal Arsenal* for tModLoader.
  - Weapons: a homing missile launcher, a tactical nuke (crater + mushroom cloud), a chain-lightning rifle, a
    black-hole gun and an orbital strike.
  - Three new enemies and a two-phase Drone Mothership boss.
  - Every sprite came from fal.
- **[examples/aoe2-de-civ](examples/aoe2-de-civ)**: *San Franciscans* for Age of Empires II DE.
  - A new civilization with a Robotaxi unique unit and Delivery Drones, rendered from fal image-to-3D models
    at AoE2's camera angle.
  - A Transamerica Pyramid wonder.
  - A reverse-engineered `.sld` sprite writer.
- **[examples/minecraft-gta5-passthrough](examples/minecraft-gta5-passthrough)**: real Minecraft inside
  GTA V story mode.
  - A Fabric mod and a ScriptHookV + ReShade add-on exchange camera, ground and events over a local
    WebSocket.
  - Minecraft's colour + depth are depth-composited into GTA's frame.
  - Minecraft TNT, arrows and fireworks become GTA explosions and bullets, and Minecraft mobs fight the
    police.

Each has a field note with every non-obvious lesson: [knowledge/INDEX.md](knowledge/INDEX.md).

## Rules it follows
- **Any game you own: single-player, multiplayer, or servers you host.** It refuses to inject into online
  games with anti-cheat, write cheats against other players, or bypass anti-cheat, DRM or ownership checks.
- **It never ships game files or decompiled code.** Mods ship as code, your own assets, patches or
  converters.
- **It backs up before touching saves**, and kills processes by PID only.
- **It asks before** driving your mouse and keyboard, installing loaders into game folders, or publishing,
  PRs included.

Full reasoning: [`skills/mod-any-game/references/safety.md`](skills/mod-any-game/references/safety.md).

## Made a mod with it?
Put the badge on your mod's page:

```markdown
[![made with universal-modder](https://raw.githubusercontent.com/rehan-remade/universal-modder/main/docs/media/made-with-dark.svg)](https://github.com/rehan-remade/universal-modder)
```
Use `made-with-light.svg` on a light page.

## Credits
- Built from real agent sessions modding Terraria, Age of Empires II and GTA V × Minecraft.
- Assets: [fal](https://fal.ai) (GPT Image 2, Nano Banana 2, FLUX, Trellis 2, ElevenLabs...).
- Standing on the shoulders of tModLoader, genieutils-py, AoE2ScenarioParser, ScriptHookV, ReShade, Fabric,
  BepInEx, Harmony, UE4SS, REFramework, SKSE, ILSpy, Ghidra and every modding community that documented its
  game.
- The engine playbooks also draw on the September 2026 wave of AI-built mods, and on how their creators
  explained them in public.

MIT licensed. Brand type: Geist Pixel, Sometype Mono and Instrument Sans. Video titles: Space Grotesk and JetBrains Mono. All under the SIL OFL.

## Star history

## 关联链接

- https://fal.ai
- https://fal.ai/dashboard/keys
- https://github.com/rehan-remade/universal-modder/stargazers
- https://github.com/rehan-remade/universal-modder`
- https://raw.githubusercontent.com/rehan-remade/universal-modder/main/docs/media/made-with-dark.svg
- https://raw.githubusercontent.com/rehan-remade/universal-modder/star-chart/stars.svg

## 导航

- 项目页：[[10-项目/github.com_b05ceac2]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
