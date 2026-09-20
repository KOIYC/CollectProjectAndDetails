---
type: "corpus"
item_id: "44cb7c954aebefc3"
title: "Show HN: Play subway surfer inside your Claude Code terminal"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49730274"
project_url: "https://github.com/lucastononro/cc-subway"
author: "ltononro"
published_at: "2026-09-16T17:29:40Z"
captured_at: "2026-09-20T14:03:55+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_ltononro
  - story_49730274
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Play subway surfer inside your Claude Code terminal

> [!info] 一句话导读
> lucastononro/cc-subway

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49730274>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：ltononro　|　发布：2026-09-16T17:29:40Z
> 项目链接：<https://github.com/lucastononro/cc-subway>
> 采集：2026-09-20T14:03:55+08:00　|　id：`44cb7c954aebefc3`

## 正文

# lucastononro/cc-subway

Subway runner in a pane on the right of Claude Code, playable while Claude works. A Claude Mod built on function hooks.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-16T13:55:16Z

## Languages

- TypeScript

---

## README

# cc-subway

An endless runner in a pane on the right of the Claude Code transcript, for the minutes Claude spends working.

Run `/subway`. A pane opens beside the transcript with three lanes of track running toward a night skyline. Click the picture, then ← → to change lane, ↑ to jump the low barriers, ↓ to roll under the high ones, and change lane to dodge the trains. Coins score ten. When Claude finishes the turn the game pauses and says so, so you never miss a reply. Playing costs no tokens: the plugin answers every key itself, without asking the model.

Running /subway in Claude Code: the pane opens on the right, a run to a crash, a prompt to Claude, the game pausing when the answer lands, and a second run

Mid-run: the runner in the left lane, a coin and a high barrier ahead, the skyline behind

The picture is drawn at one pixel per column and two per row, with the `▀` half block coloured front and back, twenty frames a second: a gradient sky with stars and a moon, a skyline that drifts by more slowly than the track, rails converging to a vanishing point, sleepers scrolling at the game's speed, trains with lit windows, and a runner with a run cycle, a jump arc and a roll.

The plugin is built on Claude Code **function hooks** ("Claude Mods"): TypeScript that runs inside Claude Code's own process, instead of shell-command hooks. They are in early access, so they need the environment variable the quick start sets, and the API can change between Claude Code releases.

## Requirements

- Claude Code 2.1.269 or later, with `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` set. The quick start shows where.
- An interactive terminal session. Nothing draws in `claude -p`, the desktop app or mobile.
- A terminal that reports the mouse. One click is what gives the board the keyboard.
- For the pane to dock **on the right**: the fullscreen layout, which is the default outside tmux, and a terminal at least **110 columns** wide. Narrower, or on the main screen, the same pane sits inline above the prompt.
- A terminal font with the `▀` half block. Modern terminals are fine.

## Quick start

1. Turn function hooks on. Add this to `~/.claude/settings.json` (create the file if it does not exist, or merge the `env` key into what is there). Without it the plugin installs fine but does nothing.

   ```json
   {
     "env": {
       "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS": "1"
     }
   }
   ```

 For a single session instead, prefix the command: `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude`.

2. Install from GitHub. The repo is its own marketplace:

   ```sh
   claude plugin marketplace add lucastononro/cc-subway
   claude plugin install cc-subway@cc-subway
   ```

3. Start `claude` and run `/subway`. The pane opens on the right.

 The pane just opened: the empty track, and CLICK HERE TO RUN across the middle

4. **Click the picture**, then use the arrows. The click gives the game the keyboard; until then your keys go to the prompt.

5. Press **Esc** to give the keyboard back to the prompt. `/subway` again, `/subway stop`, or ctrl+x x closes the pane.

If `/subway` is an unknown command, see Troubleshooting.

To remove it:

```sh
claude plugin uninstall cc-subway
claude plugin marketplace remove cc-subway
```

To try it without installing, or to hack on it, clone and load it for one session:

```sh
git clone https://github.com/lucastononro/cc-subway
cd cc-subway
claude --plugin-dir .
```

The repo's own `.claude/settings.json` sets the variable for sessions started inside the folder.

## Controls

| | |
|---|---|
| ← →, or `a` `d` | change lane |
| ↑, `w`, Space, Enter | jump: clears a yellow low barrier |
| ↓, `s` | roll: passes under a purple high barrier |
| click | left third of the picture moves left, right third moves right, the middle jumps |
| `p` | pause |
| `r` | start again |
| Esc | keyboard back to the prompt; the game keeps running |

A red train blocks the lane whatever you do: change lane. Coins are worth ten, every row travelled one. The track speeds up as you go. Only one lane is blocked on any row, so there is always somewhere to go.

Crashed into a train: the frame turns red and the status line says the score

## Playing while Claude works

Send your prompt, then open the game. When the turn finishes, the picture dims, a banner says `● Claude is done` across the track, and the status line turns yellow. Press a key or click to carry on, or Esc to go and read the reply.

Claude has answered: the picture dims and a yellow banner says Claude is done

The best score is kept in the plugin's store across sessions, and a new best shows a toast.

## How it works

- `hooks/register.tsx` is the hooks module. `session.start` registers `/subway`; `command.run` opens the pane with `$.ui.open({ id: 'subway' })`; `ui.render` for `{ component: 'Pane', requestId: 'subway' }` draws the board as a `Client` element sized to the pane's `bodyColumns` and `scroll.bodyRows`; `turn.complete` bumps a counter the board reads to pause; `ui.message` keeps the best score in `$.store`.
- `hooks/board.tsx` is the surface module: it runs on the drawing thread with its own frame clock, keys and mouse. It ticks the rules ten times a second, paints the scene twenty times a second with the `▀` half block (foreground for the top pixel, background for the bottom), folding runs of colour when a row would exceed the engine's node budget, and posts the score back when a round ends.
- `hooks/scene.ts` paints the picture into a buffer of hex-coloured pixels: the sky, the skyline, the perspective track, the things on it scaled by distance, the runner and its poses, the crash flash. Pure, so it renders headless in tests.
- `hooks/game.ts` holds the rules as pure functions: lanes, the jump and roll timers, spawning, collisions, speed.

Two rules for the board file: never name a local variable `h`, because every JSX tag compiles to a call of `h`; and write the `Client` module path as a string literal, because the engine reads it off the source.

## Develop

```sh
bun test                                             # the rules and the scene; PREVIEW=1 prints ASCII frames
bunx --bun oxlint@1.83.0 hooks tests --deny-warnings # dead code and correctness, no config file
claude plugin validate .claude-plugin/plugin.json    # lists the hooked events, $ calls and surface modules
claude plugin validate .                             # checks the marketplace manifest
```

Type checking needs the early-access types: open a Claude Code session in this folder with function hooks on, run `/plugin-types` (it writes the git-ignored `.claude/types/`), then `bunx -p typescript tsc -p .`. If bun is not installed, `npx -y bun@1 test` works.

Edits hot-reload into a running session. If a reload fails partway, the transcript says so; restart the session.

The gif and the screenshots are captured from a real session in a 150 by 42 terminal, driven through tmux: `docs/capture/record.sh` opens the session, plays a scripted run, sends Claude a one-word prompt so the pause shows, grabs frames with `tmux capture-pane -e`, and renders them with agg.

## Troubleshooting

- **`/subway` is an unknown command.** Function hooks are off. Check `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` is set in `~/.claude/settings.json` under `env`, and that the plugin is loaded with `/plugins`.
- **The pane opened above the prompt, not on the right.** The terminal is under 110 columns, or Claude Code is on the main-screen layout (tmux, or `CLAUDE_CODE_NO_FLICKER=0`). Widen the terminal; the pane moves on the next open.
- **Keys go to the prompt instead of the game.** Click the picture first. Esc hands the keyboard back to the prompt.
- **Nothing happens when you click.** Your terminal does not report the mouse, and the board cannot get the keyboard without a click.
- **The picture is small.** It follows the pane: a wider terminal and a taller pane give a bigger picture, up to 72 columns by 30 rows.
- **The picture is replaced by one line naming the plugin and the module.** The board threw an error or ran over its time budget and was unmounted. Run `/subway stop` and open it again. If it repeats, start Claude with `--debug-file /tmp/cc-subway.log` and search the log for `cc-subway`.

## Limits

- Twenty frames a second, so it feels coarse next to a real console.
- The game only gets the keyboard after a click, and never gets Esc, which always returns to the prompt.
- A headless `claude -p` run, the desktop app and mobile never draw the pane.
- The best score lives in the plugin's store on this machine.

A clone of the genre, not affiliated with or endorsed by SYBO.

## License

MIT. See LICENSE.

# devladpopov/aixm-parser

## 评论（2/2）

> **Kerode0** · 2026-09-16T17:30:25.000Z　
> great work dude

---

> **ltononro** · 2026-09-16T17:34:52.000Z　
> not really lol, just a practical joke.
> but it opens my mind for some interesting applications within claude code!

## 导航

- 项目页：[[10-项目/github.com_ffc7745a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
