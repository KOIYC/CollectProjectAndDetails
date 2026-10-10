---
type: "corpus"
item_id: "b360726c4e4b3fc5"
title: "Show HN: CAD Studio – Describe a part, get parametric CAD you can print (macOS)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50026073"
project_url: "https://github.com/filippofinke/cad-studio"
author: "filippofinke"
published_at: "2026-10-09T20:18:08Z"
captured_at: "2026-10-10T09:53:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - hn_show
  - author_filippofinke
  - story_50026073
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: CAD Studio – Describe a part, get parametric CAD you can print (macOS)

> [!info] 一句话导读
> filippofinke/cad-studio

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50026073>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：filippofinke　|　发布：2026-10-09T20:18:08Z
> 项目链接：<https://github.com/filippofinke/cad-studio>
> 采集：2026-10-10T09:53:50+08:00　|　id：`b360726c4e4b3fc5`

## 正文

# filippofinke/cad-studio

📐 Describe a part, get a printable model: a native macOS CAD studio powered by Claude Code and build123d.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 1
- License: MIT License
- Homepage: https://filippofinke.github.io/cad-studio/
- Default branch: main
- Created: 2026-10-06T20:24:56Z

## Languages

- CSS
- HTML
- JavaScript
- Shell
- Swift

## Topics

- 3d-printing
- 3mf
- ai
- ai-agents
- anthropic
- build123d
- cad
- claude
- claude-code
- llm
- macos
- parametric-design
- python
- realitykit
- step
- stl
- swift
- swiftui
- technical-drawing

## Top Contributors

- filippofinke (85 contributions)
- github-actions[bot] (1 contributions)

---

## README

 CAD Studio

> Describe a part, get a printable model. A native macOS CAD studio powered by the coding agent on your Mac (Claude Code or Codex) and build123d.

Type "a print-in-place planetary gearbox with four colors, animated with real gear ratios" and CAD Studio has your coding agent write a parametric `model.py`, run it with build123d and hand you a 3D model, an ISO technical drawing and files ready for your slicer. Every change is a new version you can go back to.

 Website · ▶︎ Watch the narrated demo (MP4, with sound)

## Features

- [x] Chat with an agent that writes and fixes parametric build123d scripts for you
- [x] Live 3D viewer with orbit, zoom, pan, grid, wireframe and multi-color 3MF parts
- [x] Measure distances and cut sections through the model
- [x] Animate mechanisms with a physics simulation (masses, springs, friction) and per-frame collision checks
- [x] Multi-part models: assembled, exploded or print-plate view, show, hide or keep parts together
- [x] Print plate with every part oriented and laid out for printing (`plate.3mf`, opened in your slicer)
- [x] Floating parameter panel with sliders: tweak dimensions without calling the agent
- [x] ISO technical drawings (first-angle projection): assembly with parts list plus one sheet per part, as a multi-page PDF
- [x] Version history: jump back to any generation, chat and context included, and compare versions in 3D
- [x] Attach or paste (⌘V) reference images, sketches, PDFs and STEP/STL files to the chat
- [x] Export STEP, 3MF, STL, PDF drawing and `model.py` as one ZIP
- [x] Printer-aware design rules for FDM, multi-material, resin and SLS, in mm, cm, m or inches
- [x] Drag panels anywhere: chat left, right or at the bottom, layout saved per project
- [x] English, Italian, German and French

## Screenshots

Every screenshot below is from the same project: a print-in-place planetary gearbox, from the first launch to version 2.

**Set up once, then describe your part.** Pick your printer and units on first launch, create a project and type what you need.

| First launch | Describe the part |
| :---: | :---: |
| | |
| **The agent at work** | **The finished gearbox** |
| | |

**Parts, motion and drawings.** Explode the assembly, play the simulated motion and flip through the drawing sheets.

| Exploded view | Simulated motion |
| :---: | :---: |
| | |
| **Edit parameters without the agent** | **Measure distances** |
| | |
| **Section view** | **One sheet per part** |
| | |
| **Ask for a change: version 2** | **Compare with version 1** |
| | |
| **Chat on the right** | **Chat at the bottom** |
| | |

## Quick Start

Prerequisites

- macOS 15 or later
- Claude Code signed in (run `claude` once in Terminal), or Codex CLI signed in (`codex login`); pick one in **Settings → Agent**
- uv or Python 3.10–3.13, used to install build123d on first launch

Download

Grab `CADStudio.dmg` from the latest release and drag CAD Studio into Applications. The app isn't notarized, so the first time macOS blocks it: open **System Settings → Privacy & Security** and click **Open Anyway**, or run:

```bash
xattr -dr com.apple.quarantine "/Applications/CAD Studio.app"
```

Build from source (needs Xcode 16 or later)

```bash
git clone https://github.com/filippofinke/cad-studio.git
cd cad-studio
./build.sh --install
```

This builds a universal `CAD Studio.app`, copies it to `/Applications` and launches it. `./build.sh --dmg` builds `build/CADStudio.dmg`. You can also open `CADStudio.xcodeproj` and press ⌘R.

## How it works

Every project is a folder. CAD Studio runs the agent installed on your Mac in headless mode (`claude -p --output-format stream-json`, or `codex exec --json` in its workspace sandbox) inside that folder, with a CAD system prompt that asks for a single parametric `model.py`. The agent runs the script with a dedicated Python environment (`~/Library/Application Support/CAD Studio/venv`, with build123d, matplotlib and numpy) until it produces:

```
<Project>/
├── model.py              # parametric build123d script
├── references/           # images attached in the chat
├── output/
│   ├── model.3mf         # main model, with part colors
│   ├── model.stl
│   ├── model.step
│   ├── plate.3mf         # parts laid out ready to print
│   ├── schematic.svg / .png / .pdf   # page 1 + multi-page PDF
│   ├── schematic-2.svg …  # one sheet per part
│   ├── animation.json    # optional: simulated motion, values and collisions
│   └── manifest.json     # size, volume, parameters, warnings
└── .cadstudio/           # chat, session, logs and versions
```

The app streams the agent's text and tool calls into the chat, watches `output/` and reloads the 3D view and the drawing as soon as files change. Each successful generation is copied to `.cadstudio/versions/ /` together with the chat and a forked Claude session, so going back to a version also restores what the agent remembers.

## Notes

- Generations use your Claude Code or Codex plan. A simple part takes one to two minutes; a complex mechanism can take half an hour.
- By default the agent ignores your personal configuration (Claude Code hooks, plugins and MCP servers, Codex `config.toml`). Turn this off in **Settings → Advanced** if your login depends on them.
- **Settings → Agent → Restricted Bash** (Claude Code) limits the agent to the project's Python interpreter and read-only commands.
- Files are always in millimeters; the chosen unit is used in replies and drawings.

## Contributing

Open a pull request against `main` with a Conventional Commits title (`feat: …`, `fix: …`). PRs are squash-merged, and release-please turns them into a release PR that bumps the version and updates the changelog. Merging it publishes a GitHub release with the DMG attached.

## Author

👤 **Filippo Finke**

- Website: https://filippofinke.ch
- Twitter: @filippofinke
- GitHub: @filippofinke
- LinkedIn: @filippofinke

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2026 Filippo Finke.
This project is MIT licensed.

***

_Not affiliated with Anthropic._

# pullboard-dev/pullboard

## 关联链接

- https://filippofinke.ch
- https://filippofinke.github.io/cad-studio/
- https://github.com/filippofinke/cad-studio.git

## 导航

- 项目页：[[10-项目/github.com_728057da]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
