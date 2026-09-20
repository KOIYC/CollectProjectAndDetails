---
type: "corpus"
item_id: "c6ea6d9d02534258"
title: "Show HN: Put an AI agent on a FaceTime audio/video call (open source, WebRTC)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49728749"
project_url: "https://github.com/cherthq/chert-facetime-opensource"
author: "garygao"
published_at: "2026-09-16T15:41:02Z"
captured_at: "2026-09-20T14:04:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_garygao
  - story_49728749
  - show_hn
metrics: {"points": 3, "comments": 2, "engagement_velocity": 3}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Put an AI agent on a FaceTime audio/video call (open source, WebRTC)

> [!info] 一句话导读
> cherthq/chert-facetime-opensource

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49728749>
> 指标：点赞=3 · 评论=2 · engagement_velocity=3
> 作者：garygao　|　发布：2026-09-16T15:41:02Z
> 项目链接：<https://github.com/cherthq/chert-facetime-opensource>
> 采集：2026-09-20T14:04:01+08:00　|　id：`c6ea6d9d02534258`

## 正文

# cherthq/chert-facetime-opensource

An open-source SDK for deploying real-time video agents to FaceTime in seconds

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: Apache License 2.0
- Default branch: main
- Created: 2026-09-10T14:02:53Z

## Languages

- JavaScript

## Top Contributors

- garygao333 (10 contributions)

---

## README

 Chert FaceTime Opensource

 An open-source CLI/SDK for deploying real-time video agents to FaceTime

Chert FaceTime Opensource lets any builder put their AI agent on a live FaceTime call with a simple CLI/SDK. You own the agent's code, personality, voice, model, and avatar, and run it locally or deploy it yourself through services such as LiveKit. The connector runs on your computer and carries audio and video between FaceTime and a LiveKit room. It starts the connection without requiring you to build or host your agent through Chert.

> [!NOTE]
> For managed outbound calling, incoming call monitoring and acceptance, and media bridging through an API, use Chert's managed FaceTime service.

## Demo

Watch a LiveKit agent connect to FaceTime through the Chert CLI.

https://github.com/user-attachments/assets/1fde265d-5e53-4d98-be87-b64ea07eeeff

## How to use

**Before you start:** you need Node.js 22.22+, Google Chrome, a running LiveKit agent, and an iPhone to create a FaceTime link and admit the browser guest. For video, your agent must publish a video track as well as audio. Keep your computer running during the call.

The intended flow is:

1. Run or deploy your own LiveKit agent.
2. Have that agent join a LiveKit room.
3. Give the connector access to the same room and identify the agent participant.
4. Join the FaceTime link in Chrome and admit the browser guest on your iPhone.
5. Talk to your agent through FaceTime.

Your model keys stay with your agent. The connector only needs a short-lived room token. You do not need our optional starter agent or its OpenAI setup to bring your own.

### CLI: run it from your terminal

```sh
npx @trychert/facetime-opensource
```

Enter these details when prompted:

```text
LiveKit server URL: wss://your-project.livekit.cloud
Room token: [hidden]
Agent participant identity: your-agent
FaceTime link: [hidden]
```

The token must allow joining, publishing, and subscribing to the agent's room, expire within one hour, and use a different participant identity from the agent. Use the agent's exact room participant identity, not its deployment name.

Chrome opens automatically. Click **Join**, admit the guest on your iPhone, then press **Enter** in the terminal to connect LiveKit. Press **Enter**, **Ctrl+C**, or **Stop test** to stop the connector. Your independently hosted agent's lifecycle stays under your control.

### SDK: use it in your code

```sh
npm install @trychert/facetime-opensource
```

In a Node.js `.mjs` file, load the connection details from your private environment configuration:

```js
import { FaceTimeGuest } from '@trychert/facetime-opensource';
import { createInterface } from 'node:readline/promises';

const terminal = createInterface({ input: process.stdin, output: process.stdout });
let guest;
try {
  guest = await FaceTimeGuest.open({
    faceTimeLink: process.env.FACETIME_LINK,
    livekitUrl: process.env.LIVEKIT_URL,
    roomToken: process.env.LIVEKIT_ROOM_TOKEN,
    agentIdentity: 'your-agent',
  });
  await terminal.question('Join in Chrome and admit on your iPhone, then press Enter.');
  await guest.connect();
  terminal.close();
  await guest.closed; // Click Stop test in Chrome when finished.
} finally {
  terminal.close();
  await guest?.close();
}
```

The SDK opens Chrome on your computer. Call `connect()` after admission and `close()` to stop. Keep real tokens and FaceTime links out of committed code. Installing the package alone does not start the connector or your agent.

## How this works

The connector has **four core files**:

| File | Simple explanation |
| --- | --- |
| `src/sdk.mjs` | **Starts and stops the browser setup.** Opens the FaceTime tab and local connector tab. |
| `src/media.mjs` | **Supplies the agent's video and speech** instead of your webcam and microphone, and receives the caller's audio. |
| `src/hop.mjs` | **Connects the two tabs.** Carries media between them because FaceTime blocks direct LiveKit connections. |
| `src/livekit.mjs` | **Connects to the agent's room.** Sends caller audio into LiveKit and receives the agent's speech and video. |

Your voice travels from FaceTime through the connector to your agent's LiveKit room. The agent's speech and video travel back along the same path. The CLI is a terminal interface to this same SDK. Your agent runs separately.

**Status:** experimental, with a successful live conversation on the tested Mac. The updated local CLI passed a supervised FaceTime call with agent audio and video, alongside offline SDK and media checks. Longer-call reliability, other platforms, and other agents remain unverified. This is an unofficial project, not an Apple-supported integration.

See the detailed guide for the optional starter agent, configuration, tests, and development background. Licensed under Apache-2.0.

---

Built by Chert Technologies Inc.

# Zigpoll - Survey & Feedback Platform

## 评论（2/2）

> **Natashash23** · 2026-09-17T10:42:25.000Z　
> Nice content definetely would give a try

---

> **garygao** · 2026-09-17T16:02:21.000Z　
> Thanks! Let me know what you build with it/if you have any suggestions or feedback!

## 关联链接

- https://github.com/user-attachments/assets/1fde265d-5e53-4d98-be87-b64ea07eeeff

## 导航

- 项目页：[[10-项目/github.com_41c4215e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
