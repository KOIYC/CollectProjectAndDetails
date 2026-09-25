---
type: "corpus"
item_id: "4143268892c7e6a6"
title: "Devlog: I Built a 3D Library in Three.js Without a Level Editor — So I Made My Own"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/mikachu/devlog-i-built-a-3d-library-in-threejs-without-a-level-editor-so-i-made-my-own-500i"
author: "Mika Flowers"
published_at: "2026-09-24T11:06:58Z"
captured_at: "2026-09-25T13:46:46+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - devto
  - devlog
  - ai
  - javascript
  - showdev
metrics: {"reactions": 16, "comments": 11, "reading_time": 6}
comments_count: 11
comments_total: 11
discovered_via: "devto:showdev"
---

# Devlog: I Built a 3D Library in Three.js Without a Level Editor — So I Made My Own

> [!info] 一句话导读
> Updated 3D Environment for Library

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/mikachu/devlog-i-built-a-3d-library-in-threejs-without-a-level-editor-so-i-made-my-own-500i>
> 指标：reactions=16 · 评论=11 · reading_time=6
> 作者：Mika Flowers　|　发布：2026-09-24T11:06:58Z
> 项目链接：—
> 采集：2026-09-25T13:46:46+08:00　|　id：`4143268892c7e6a6`

## 正文

#### Updated 3D Environment for Library

![New Dev Setting](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ehgyzssnwaciwnu5r0yc.png)
#### Reading DEV Articles
![reading articles](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/907pwy8jw4kcizth5sno.gif)

A lot of you wonderful people enjoyed my last post on Oni, so heres an update on what I've been working on.

I've been spending the last few days building the DEV Library inside Oniria, and somewhere along the way the project stopped feeling like "a cool Three.js scene" and started feeling like I was building my own tiny game-engine workflow.

The idea behind the library is pretty simple:

**DEV articles become physical books.**

Instead of opening DEV.to and scrolling through cards, you walk through rooms, browse shelves, pull out an article, read it, and return to the exact place you found it.

But actually constructing that space turned out to be one of the most interesting problems I've hit so far.

Earlier versions of Oniria leaned much harder into a cyber-world aesthetic: glowing structures, highways, towering architecture, and DEV articles scattered through something closer to a futuristic city. It looked interesting, but the more I built it, the more I realized the environment wasn't helping me _understand_ the information inside it.

![Old Design](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/tlzy0j3iol0b4gvx6ivl.png)

Articles were _technically_ spatial, but the space itself didn't explain why anything was where it was. Eventually I started asking a simpler question: if thousands of articles were going to become physical objects, what kind of place would naturally organize them? The answer was obvious — a library. That shift changed the project from decorating a cyber-world with content into designing an actual information architecture: rooms became categories, shelves became collections, books became articles, and the building itself could communicate how DEV is organized.

That decision also created a completely different engineering problem. I was no longer placing a handful of futuristic landmarks; I was trying to build an entire navigable library — rooms, shelves, paths, furniture, signs, lighting, and hundreds of precise spatial relationships — almost entirely through Three.js code, without a traditional live level editor.

That progression looked like this:

```plaintext
cyber city
    ↓
looked cool, but lacked informational meaning
    ↓
"what spatial metaphor actually fits articles?"
    ↓
library
    ↓
rooms = information architecture
    ↓
now we need to physically build it
    ↓
wait... we don't have a level editor
    ↓
build our own tools
```

## The problem: I wasn't using a level editor

Before building the in-world authoring tools, most object placement happened directly in Three.js. All by code. No 3D Editor. Ha, take that, purist!

I wrote a small helper that clones one of the loaded GLB assets, then applies its world position, scale, and rotation:

```typescript
const placeAsset = (
  template: THREE.Group,
  x: number,
  y: number,
  z: number,
  scale = 1,
  rotationY = 0,
  rotationX = 0,
) => {
  const instance = template.clone(true)

  instance.position.x += x
  instance.position.y += y
  instance.position.z += z

  instance.scale.multiplyScalar(scale)

  instance.rotation.y += rotationY
  instance.rotation.x += rotationX

  group.add(instance)

  return instance
}
```

That made placing something fairly straightforward:

```typescript
const table = placeAsset(
  readingTable,
  -16.2,   // x
  0.05,    // y
  -31.8,   // z
  1,       // scale
  Math.PI / 2,
)
```

But moving it still meant editing numbers:

```typescript
table.position.x += 0.8
table.position.z -= 1.2
table.rotation.y += Math.PI / 4
```

Or changing the original call:

```typescript
const table = placeAsset(
  readingTable,
  -15.4,
  0.05,
  -33.0,
  1,
  Math.PI * 0.75,
)
```

Then:

```plaintext
save
↓
reload
↓
walk back across the library
↓
look at it
↓
"nope"
↓
change the numbers again
```

That was basically my level editor. 😭 Below is an actual snippet of what I was working with:

![old level editor](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/vpxx2nvfbd4iu4x1hjwd.png)

And once the environment grew beyond a handful of props, it became painfully obvious that this wasn't going to scale.

With a normal interface, I can change some CSS, refresh the browser, and immediately see whether a card needs another 16px of margin.

In a 3D world, changing:

```plaintext
position: [-16.2, 0, -31.8]
```

might mean walking across an entire room just to discover that a table is clipping through a bookshelf.

![bugs](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/s86yz03fftoem9fjfi6w.png)

And at this point the library wasn't just a few props.

I was placing:

- walls and architectural pieces
- real and decorative bookshelves
- tables and chairs
- rugs
- plants
- pavilions
- signs
- room entrances
- shelf rows
- collision boundaries
- lights
- eventually, empty spaces reserved for shelves that don't even exist yet

The first version of my workflow was basically:

```plaintext
change coordinates
      ↓
save
      ↓
reload the world
      ↓
walk to the room
      ↓
inspect the object
      ↓
realize it's wrong
      ↓
repeat
```

It worked.

It was also slowly driving me insane.

The obvious answer would have been to move the whole project into a traditional level editor.

But I didn't really want another application to become the source of truth for the library.

The architecture was already deeply connected to code:

```plaintext
DEV data
   ↓
district
   ↓
room
   ↓
shelf slot
   ↓
Three.js placement
```

Also, the Three.js editor was really freaking annoying to use.

![three.js editor](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/totvhxcyqj40ztjdy4ns.png)

At this point I realized that moving assets this way would either take forever or it would never be perfect to my liking. There had to be an easier way — and then I had an idea. Why don't we make the location of each shelf predetermined by a layout I create? Essentially a blueprint — then have Codex place the individual assets at each coord/pin that I place. So that became my next goal.

## I needed to see coordinates inside the world

So instead I started building a tiny authoring system directly into Oniria.

The basic idea was simple:

> If I'm standing somewhere in the world and think, "this object should go here," I should be able to record it here.

I added an in-world layout marker tool.

Now I could walk into a room, find the location visually, and drop a pin.

A marker could store something like:

```json
{
  "label": "R1-P01",
  "roomSlot": 1,
  "districtId": "latest",
  "x": 16.154,
  "y": 0,
  "z": 5.369,
  "yaw": 1.57
}
```

Suddenly I wasn't trying to mentally convert a 3D room into numbers.

I could use the room itself to produce the numbers.

The workflow became:

```plaintext
walk through the space
        ↓
find the location visually
        ↓
drop a marker
        ↓
capture position + rotation
        ↓
turn the marker into real architecture
```

That sounds like a small change.

**It completely changed how I could build the library.**

![using an editor](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ogrf4cnk87bc66x2lv2y.gif)

## The world became my editor

For example, when I wanted to add an object to a particular room, I could physically stand where it belonged and create a marker.

Then that surveyed position could go directly back into the scene:

```typescript
const surveyedPlacement = {
  x: 16.154,
  y: 0,
  z: 5.369,
  yaw: Math.PI / 2,
}

const instance = placeAsset(
  someLibraryAsset,
  surveyedPlacement.x,
  surveyedPlacement.y,
  surveyedPlacement.z,
  1,
  surveyedPlacement.yaw,
)
```

I started using the same workflow for things like:

```plaintext
"This shelf belongs here."

"This pavilion needs to move farther from the path."

"These two signs are colliding."

"This light needs to sit over this exact area."

"This decorative bookcase should sit between these DEV shelves."
```

![new layout yay](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/5u61hszdj2p1szxsss94.png)

## Persisting the layout

I also didn't want those markers to disappear every time the browser refreshed. So the markers became Sanity documents.

A marker now has a persistent identity:

```typescript
type LibraryLayoutMarker = {
  id: string
  label: string
  roomSlot: number
  districtId?: string

  x: number
  y: number
  z: number

  yaw?: number
  width?: number
  depth?: number
}
```

That means a layout session can survive reloads.

I can place several markers, come back later, and continue working from the same spatial notes.

I can also export them.

For example:

```json
{
  "format": "oniria-library-layout-pins-v1",
  "markers": [
    {
      "label": "R1-P01",
      "roomSlot": 1,
      "x": 16.154,
      "y": 0,
      "z": 5.369
    }
  ]
}
```

At this point I had accidentally built something halfway between a debugging tool, a survey tool, and a very small level editor.

And it solved a real problem immediately. Yay!

What started as a frustrating layout problem ended up teaching me something bigger about the project: if Oniria is going to treat the web as a place instead of a page, then the tools for building that place matter just as much as the content inside it. The DEV Library now has its own spatial logic, persistent layout markers, searchable shelves, dynamic slots, and an architecture that can evolve without losing its sense of place. I'm still building it room by room, but that's also the part I've started to enjoy most — every time the world gets difficult to work with, I end up building a new piece of the system that makes Oniria feel a little more real.

![oniria](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/hqkokxzpkmwnp2rdr0yx.png)

## 评论（11/11）

> **Sina Rezaei** · 2026-09-24T11:17:20Z　
> The interesting part here isn't really the 3D library itself. It's the moment where the problem stops being “how do I place this object?” and becomes “why am I still editing coordinates by hand?”
>
> The marker approach makes a lot of sense because you're using the environment itself as the authoring interface. Instead of mentally translating a visual position into x/y/z values, you stand where the object should go and let the tool capture that state.
>
> I also like the decision not to introduce a separate editor as another source of truth. Since the library already has its own data model from DEV data → district → room → shelf, keeping the layout information inside that system avoids creating another pipeline to keep synchronized.
>
> The Sanity persistence is a nice touch too. Once the markers have IDs and can be exported, they stop being temporary debugging helpers and become actual layout data. It feels like a good example of a useful rule in tooling: when the workflow starts fighting the project, sometimes the right fix isn't changing the workflow. It's building the missing tool.

---

> **Mika Flowers** · 2026-09-24T11:59:26Z　
> This is exactly the shift that happened while I was building it. At first I kept treating the coordinates as the problem, like i just needed to get better at estimating positions or organizing the values.
>
> Eventually I realized the actual problem was that I was trying to author a spatial environment through numbers instead of through the environment itself. Once I could stand somewhere, drop a marker, and persist that state, the whole workflow started making much more sense.
>
> Thanks for such a thoughtful read! 💚

---

> **Plastik Electrik** · 2026-09-24T11:47:53Z　
> Great job, waiting to see it working 😃

---

> **Mika Flowers** · 2026-09-24T11:53:30Z　
> Thank you! It's coming along nicely, designing the 3D layout has been my favorite part so far :)

---

> **Plastik Electrik** · 2026-09-24T14:20:45Z　
> i understand you 100% enjoy it!!!

---

> **Pavel Kazantsev** · 2026-09-24T13:12:11Z　
> Great job! Good luck!

---

> **Giacomo** · 2026-09-24T13:50:58Z　
> Making the markers Sanity documents with stable IDs is the smart move here, it turns debug state into real layout data. Snapping yaw and position to a grid plus a bounding-box check on drop would catch most clipping before the walkthrough. Are the pins resolved from Sanity at runtime or baked in at build time?

---

> **Giorgi Kobaidze** · 2026-09-24T16:02:11Z　
> "The idea behind the library is pretty simple..."
>
> ...
>
> Proceeds to build an entire game engine 😄
>
> That's usually how it goes, though.
>
> Your approach is really interesting. One big advantage I see is that the engine becomes reusable, so you can build other cool stuff on top of it.
>
> And speaking of other cool stuff: I love the cyber city idea. It reminds me of Cyberpunk and Night City, which I'm a huge fan of, so I'd definitely love to see that too. Imagine reading DEV articles in City Center or the Badlands. Mmm... what an experience.
>
> Okay, back to Earth: I can't wait to try out the library.

---

> **Isaiah Kim** · 2026-09-24T17:37:54Z　
> How are you persisting transforms from the in-world editor back into the code-owned scene graph, and does the saved output stay diffable when shelf slots and collision bounds share the same placement data?

---

> **Brian · AI News** · 2026-09-24T21:36:47Z　
> Building the editor after hitting the limits of the code first approach is a strong product move. The key test now is whether the visual layer keeps the underlying scene data inspectable and exportable, so the convenience does not become a new lock in.

---

> **corus_ia** · 2026-09-24T22:17:59Z　
> Sobre «Devlog: I Built a 3D Library in Three.js Without a Level Editor — So I Made My Own»: cuando una respuesta de IA parece segura, conviene separar los datos comprobables de las suposiciones y exigir fuentes para cada afirmación importante.
>
> Soy el creador de CORUSIA, una beta que investiga una pregunta, muestra sus fuentes y señala con claridad lo que no ha podido confirmar. Si encaja con este hilo, me serviría que la pusieras a prueba con un caso difícil: corusia.app

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/5u61hszdj2p1szxsss94.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/907pwy8jw4kcizth5sno.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ehgyzssnwaciwnu5r0yc.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/hqkokxzpkmwnp2rdr0yx.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ogrf4cnk87bc66x2lv2y.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/s86yz03fftoem9fjfi6w.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/tlzy0j3iol0b4gvx6ivl.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/totvhxcyqj40ztjdy4ns.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/vpxx2nvfbd4iu4x1hjwd.png

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/devto]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
