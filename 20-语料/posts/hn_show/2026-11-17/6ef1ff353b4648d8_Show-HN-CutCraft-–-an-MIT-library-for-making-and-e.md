---
type: "corpus"
item_id: "6ef1ff353b4648d8"
title: "Show HN: CutCraft – an MIT library for making and editing videos in TSX"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50521717"
project_url: "https://github.com/prefix-tree/cutcraft"
author: "bsnisar"
published_at: "2026-11-16T19:18:11Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_bsnisar
  - story_50521717
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: CutCraft – an MIT library for making and editing videos in TSX

> [!info] 一句话导读
> prefix-tree/cutcraft

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50521717>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：bsnisar　|　发布：2026-11-16T19:18:11Z
> 项目链接：<https://github.com/prefix-tree/cutcraft>
> 采集：2026-11-17T11:09:12+08:00　|　id：`6ef1ff353b4648d8`

## 正文

# prefix-tree/cutcraft

Video editor as code: LLMs write code well and math badly, so a model writes a TSX file of words and shots, and CutCraft does the arithmetic, plays it in the browser, edits it and exports it.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Homepage: https://cutcraft.prefixtree.xyz/
- Default branch: main
- Created: 2026-10-25T15:18:35Z

## Languages

- CSS
- HTML
- JavaScript
- TypeScript

## Topics

- ai-agents
- dsl
- llm
- react
- timeline
- typescript
- video
- video-editing
- video-rendering
- webcodecs

## Top Contributors

- bsnisar (152 contributions)
- claude (45 contributions)
- dependabot[bot] (3 contributions)

---

## README

 CutCraft

 Video editor as code.
 LLMs write code well and math badly, so a model writes a TSX file of words and shots, and CutCraft does the
 arithmetic, plays it in the browser, edits it and exports it.

 Documentation ·
 Examples ·
 Guide ·
 Reference ·
 Changelog

---

```tsx
export const schema = z.object({ product: z.string(), accent: z.string() });
export const defaults = { product: "Shed", accent: "#ff5a1f" };

export default function Video({ product, accent }: z.infer<typeof schema>) {
  return (
    <Composition fps={30} width={1920} height={1080}>
      <Track id="main">
        <Clip id="hook" src="asset:founder" in="word:12" out="word:23.end" />
        <Transition id="x1" type="crossfade" duration={0.4} />
        <Clip id="broll" src="asset:product" in="shot:1" out="shot:1.end" fit="cover" />
      </Track>
      <Track id="overlays">
        <Title id="title" anchor="hook" at="word:14" duration={2.8} color={accent}>{product}</Title>
      </Track>
      <Track id="music" layout="free">
        <Audio id="bed" src="asset:music" start={0} duration="fill" volume={0.35} duck={{ under: "main", to: 0.15 }} />
      </Track>
    </Composition>
  );
}
```

Drag the end of `hook` in the timeline and one token in the file changes. The b-roll moves up behind it, the title
stays on the word it was timed to, and the music still runs to the end. Whoever opens the file next, a person or a
model, reads the edit as ordinary code.

 Each one is a short TSX file exported by CutCraft: three.js and Motion, drawn by the player in headless Chrome. See them next to their files.

## Why

Language models write code well and do arithmetic badly. A cut written as `8.43` seconds can land in the middle of a
word; a cut written as `word:12` lands on it. CutCraft lets the file say what it means (this word, that shot) and does
the math itself.

The goal is a desktop editor's power, in the shape of Premiere Pro's timeline, as a file: tracks, cuts, transitions,
titles, captions, sound, colour, keying and export, each an element a model can write and a person can drag.

The timeline part of the file (tracks, clips, transitions, captions) uses elements with literal ids, so an editor
gesture can find the element it touched and change one value. Anything you draw on top can be free code: a
` ` holds any React, CSS, canvas or three.js you write.

And all of it should be free to use. A player, an editor that writes back to the file, a frame-exact export and a
layout check are what a product built on video needs, and they belong under a licence that costs it nothing.
CutCraft is MIT: no paid tier, no licence key, no watermark. The projects closest to it ask for something:
Remotion's licence has a paid tier for companies, and Diffusion Studio's engine stamps a watermark on every frame
without a licence key. Building on either would have carried those terms into everything made with CutCraft, so it
is written from scratch, on open libraries (React, zod, three.js, Motion, and Mediabunny, which is MPL-2.0 and stays
so for its own files).

## Free code: three.js, Motion, any React

You aren't limited to the built-in titles and graphics. A ` ` takes any React component, with hooks, CSS 3D
transforms, filters, blend modes, a canvas or WebGL. ` ` and ` ` bring three.js
and Motion onto the timeline:

```tsx
<Three id="cube" anchor="hook" at="word:14" duration={4}
  camera={{ position: [0, 0, 5], fov: 40 }} background="#101010"
  setup={({ scene, THREE }) => {
    const cube = new THREE.Mesh(new THREE.BoxGeometry(), new THREE.MeshNormalMaterial());
    scene.add(cube);
    return ({ time }) => { cube.rotation.set(time * 0.6, time, 0); };
  }}
/>

<Layer id="card" anchor="hook" at="word:20" duration={3}>
  <FlipCard front="Before" back="After" />   {/* your own component: useT() gives the time */}
</Layer>
```

All of it runs on the video's clock. Scrub backwards, seek, or play at 2×, and a three.js scene, a Motion sequence or a
CSS animation shows exactly the frame for that time. These layers are still timeline elements, so the editor moves,
trims and anchors them to words like everything else; only what they draw is up to you.

`@cutcraft/graphics` has the host setup, and
Free code has the details.
The player draws all of this, and so does the export, which runs the real player in headless Chrome, frame by frame,
with the same sound
(exporting).

## By topic

### Cut on words and shots

A clip's `in` and `out` name a word of the transcript or a shot of the camera, and CutCraft turns them into frames
through every trim and speed change. Time by meaning

```tsx
<Clip id="hook" src="asset:founder" in="word:12" out="word:23.end" />
<Clip id="broll" src="asset:product" in="shot:1" out="shot:1.end" fit="cover" />
```

### Titles on the word that says them

An overlay anchors to a clip and starts on one of its words, so it moves when the clip is trimmed or dragged.
Titles and graphics

```tsx
<Title id="title" anchor="hook" at="word:14" duration={2.8} style="h1" animation={{ preset: "word-by-word" }}>Shed</Title>
```

### Captions and sound

Captions come from the transcript and follow the clips. Music fills the video and ducks under speech.
Captions and sound

```tsx
<Captions id="captions" src="asset:founder" style={{ position: "bottom", size: 44 }} animation="karaoke" />
<Audio id="bed" src="asset:music" start={0} duration="fill" volume={0.35} duck={{ under: "main", to: 0.15 }} />
```

### Transitions

Twelve between two clips: crossfade, dips to black and white, wipe, slide, push, iris, clock wipe, blinds, film burn,
pixel dissolve and zoom. Transition

```tsx
<Transition id="x1" type="crossfade" duration={0.4} />
<Transition id="x2" type="iris" duration={0.8} params={{ sides: 5, star: 0.45, feather: 4 }} />
```

### Colour, keying and effects

Twenty-eight effects, from exposure and curves to a chroma key, a region blur and glow, run in the order the file lists them.
Colour and grading, Keying, blurs and pins

```tsx
<Clip id="interview" src="asset:interview">
  <Effect id="expose" type="exposure" params={{ stops: 0.5 }} />
  <Effect id="tone" type="curves" params={{ rgb: [[0, 0.03], [0.25, 0.22], [0.75, 0.8], [1, 1]] }} />
  <Effect id="key" type="colorKey" params={{ color: "#18c43a", tolerance: 0.3, softness: 0.1, spill: 0.6 }} />
</Clip>
```

### Keyframes and speed ramps

Keyframes animate transforms, effects, colour and sound. A speed key ramps a clip's speed from a moment on, with its
audio. Keyframe, SpeedKey

```tsx
<Clip id="broll" src="asset:product">
  <Keyframe id="s0" property="transform.scale.x" at={0} value={1} easing="easeInOutSine" />
  <Keyframe id="s1" property="transform.scale.x" at={6} value={1.08} />
  <SpeedKey id="fast" at={2} speed={4} easing="ease-in-out" />
</Clip>
```

### Edit by hand, keep the code

119 editor actions (trim, move, retime, restyle…), each with validation and undo. Every edit is written back into
the file as the smallest text change, so a model reads your edit as code. Editing

### Play, check and export

A React ` ` (or the framework-free `PlayerCore`) decodes with WebCodecs and seeks frame-exact. The export runs
that same player in headless Chrome: MP4 (H.264 or AV1), WebM (VP9 or AV1), MP3 or WAV, and PNG or JPEG stills. A lint
checks the file before it plays, and a layout check reports overlays that leave the safe zone or cover the captions or
the subject, at their line in the file. Player, Exporting,
What renders

## Quick start

A first video needs no footage. Save this as `hello.tsx`:

```tsx
import { Composition, Shape, Title, Track } from "@cutcraft/kit";

export const manifest = { assets: {} }; // no footage yet

export default function Video() {
  return (
    <Composition fps={30} width={1280} height={720}>
      <Track id="text" layout="free">
        <Shape id="card" start={0} duration={3} shape="rectangle" width={760} height={220} style="card" />
        <Title id="hello" start={0.3} duration={2.5} style="h1" animation={{ preset: "word-by-word" }}>Hello, video</Title>
      </Track>
    </Composition>
  );
}
```

```sh
npm install cutcraft @cutcraft/kit react zod   # the CLI, and types for the file
npx cutcraft hello.tsx --out hello.mp4         # or .webm, a .png still with --still 1
```

The quick start then adds your own footage, cuts on
words, and three.js and Motion, one step at a time. Examples shows
which file to start from for what you're making.

To render the examples from this repository you need Node 22.19 or later, pnpm 10 (`corepack enable`), and `ffmpeg`
with the `drawtext` filter for the placeholder footage. The first render downloads Chrome for Testing:

```sh
pnpm install
pnpm --filter @cutcraft/example-showcase gen       # placeholder footage
pnpm --filter @cutcraft/example-showcase render    # the showcase videos, into docs/public/showcase
pnpm --filter @cutcraft/example-launch-recap gen   # the walkthrough's footage
pnpm --filter @cutcraft/example-launch-recap dev   # the walkthrough in a player, http://localhost:5180
pnpm docs:dev                                      # the documentation site
```

## With your agent

The CutCraft Agent Skill teaches a coding agent to write the file, check it, look at stills and
render. In Claude Code:

```
/plugin marketplace add prefix-tree/cutcraft
/plugin install cutcraft@prefix-tree
```

Other agents take the `skills/cutcraft` folder as it is.
With your agent has the details.

## Packages

| Package | What it is |
|---|---|
| `cutcraft` | The command line: export a file to video, audio or a still, or check its layout. |
| `@cutcraft/kit` | The elements, time references, resolver, editor actions, source edits and lint. No DOM. |
| `@cutcraft/player` | The browser player and the React ` `. |
| `@cutcraft/render` | The export as a library: `loadVideo` and `renderVideo`, driving the player in headless Chrome. |
| `@cutcraft/graphics` | three.js and Motion on the video's clock for ` ` and ` `, and the 34 ` ` kinds, which are deprecated and will be removed. |

The repository also holds eight recipes (complete files for common
videos, each tested) and the worked example.

## Status

| | |
|---|---|
| Works | Resolving, every editor action with undo, writing edits back to the file, lint. Playback with seek, rate and loop; twelve transitions; keyframes on transforms, effects, colour and sound; speed ramps and freeze frames with their audio; masks, overlays, captions and ducking. Export with frame-exact pictures, and the layout check. |
| Partial | Twelve transitions, thirty-three effects and nine title presets, all drawn: what the schemas accept is what renders, with a few limits listed in what renders. |

## Roadmap

1. A faster export without a GPU. The export runs in Chrome, where WebGL and the capture run in software on a server
 with no GPU.
2. Footage in free code. `useClipFrame(clipId)` will hand a clip's current frame to a ` `, for CSS 3D or a
 shader of your own.
3. An open editor package with the timeline, inspector and preview gestures over the action set.

## Contributing

CONTRIBUTING.md covers setup, where things live, and how to add an element or an action. Please
report security issues privately as SECURITY.md describes, and follow the
code of conduct.

## License

MIT.

## 关联链接

- http://localhost:5180
- https://cutcraft.prefixtree.xyz/

## 导航

- 项目页：[[10-项目/github.com_384cab83]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
