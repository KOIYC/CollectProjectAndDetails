---
type: "corpus"
item_id: "3cd86e6c41d69843"
title: "Show HN: LFM3 Video Chat"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50280966"
project_url: "https://github.com/skorotkiewicz/lfm3-chat"
author: "modinfo"
published_at: "2026-10-28T21:12:30Z"
captured_at: "2026-10-29T20:41:52+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-29"
pub_day: "2026-10-28"
tags:
  - 语料
  - hn_show
  - author_modinfo
  - story_50280966
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: LFM3 Video Chat

> [!info] 一句话导读
> skorotkiewicz/lfm3-chat

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50280966>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：modinfo　|　发布：2026-10-28T21:12:30Z
> 项目链接：<https://github.com/skorotkiewicz/lfm3-chat>
> 采集：2026-10-29T20:41:52+08:00　|　id：`3cd86e6c41d69843`

## 正文

# skorotkiewicz/lfm3-chat

LFM3 video chat

- Stars: 0
- Forks: 1
- Watchers: 0
- Open issues: 0
- Default branch: onnx
- Created: 2026-10-28T20:40:18Z

## Languages

- CSS
- HTML
- JavaScript
- Python

## Top Contributors

- skorotkiewicz (11 contributions)

---

## README

# LFM3 video chat

Talk to LFM3-Omni-2B through your
microphone and camera. The model replies with text and audio, and you can
interrupt it by speaking or pressing a button.

Start the server and open http://localhost:8000 on the same computer.
Camera and microphone access on localhost works without SSL certificates.

An ONNX version is available in `src-onnx/`, with a separate
uv environment. Use `q4` for CPU or `q4f16` for NVIDIA GPU. It supports the same
camera, voice, and interruption controls without installing PyTorch.

To download ONNX weights separately, use the bundle download commands.

## Get started

You need uv and a microphone. The project uses Python
3.12. Run these commands from the project folder on the computer hosting the model.

Install the dependencies:

```bash
uv sync
```

Already downloaded the model? Skip the next command and use your existing folder
with `--model`. Otherwise, download it once:

```bash
uv run hf download LiquidAI/LFM3-Omni-2B --local-dir resources/models/lfm3-omni-2b
```

Start the chat, replacing the model path if needed:

```bash
uv run serve --model resources/models/lfm3-omni-2b
```

Open http://localhost:8000 on the same computer. HTTPS is not needed for localhost.
The server uses existing model files by default; `--download` allows it to fetch
missing files. If your model is already in the Hugging Face cache, you can omit
`--model`.

## Have a conversation

1. Click **Start conversation** and allow microphone and camera access.
2. Speak, then pause for a reply. Audio plays as the model generates it.
3. Speak over a reply to interrupt it, or click **Interrupt & speak**. Headphones
 help prevent speaker echo from causing unwanted interruptions.
4. Open **Conversation settings** to turn camera sharing or hands-free speech on
 or off, or adjust the microphone threshold.
5. Click **End** to stop the camera and microphone. **Start fresh** clears the
 conversation history.

The assistant begins answering after your turn ends. It does not generate an
answer while you are still speaking.

## Pause to think with Smart Turn

Smart Turn v3.2 helps distinguish a thinking pause from the end of a sentence.
To enable it and download any missing model files on the first run:

```bash
uv run serve \
  --model resources/models/lfm3-omni-2b \
  --turn-detector smart --download
```

After that, omit `--download`. The default `auto` setting uses Smart Turn when it
is available locally and falls back to silence detection otherwise. You can
choose silence detection explicitly with `--turn-detector silence`.

Smart Turn runs on the CPU. It gives you time to continue an unfinished thought,
with a short silence timeout so the conversation does not stay waiting forever.
You can always press **Send** to finish your turn immediately.

Its model is kept in `resources/models/smart-turn-v3/`. Keep that folder to reuse
the download. Deleting it removes the local model copy. For an existing ONNX file,
use `--turn-model /path/to/smart-turn-v3.2-cpu.onnx`.

## Connect from another device

To connect from another device, use HTTPS for camera and microphone access.
Start the server with `--host 0.0.0.0` to accept local network connections.
This setup is optional; local use on http://localhost:8000 needs no certificate.

Use a certificate trusted by the connecting device. For development, you can
create a self-signed certificate. Replace ` ` below with your server's
LAN address before running the command:

```bash
openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout key.pem -out cert.pem -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1,IP:<server-ip>"
chmod 600 key.pem
```

Then run:

```bash
uv run serve \
  --model resources/models/lfm3-omni-2b \
  --host 0.0.0.0 --port 8000 \
  --ssl-certfile cert.pem \
  --ssl-keyfile key.pem
```

Trust the certificate on the connecting device, then open
https://:8000/ there. The browser automatically uses a secure WebSocket
for audio and video frames. If the page cannot connect, check that the server's
firewall allows your chosen port.

Both certificate flags are required together. `cert.pem` and `key.pem` are
ignored by Git. Keep the private key private.

## Development checks and preview

Run the local tests:

```bash
uv run pytest
node --test tests/test-turn-gate.cjs
```

Preview the interface without loading LFM3 weights:

```bash
uv run --python 3.12 tests/live_fixture.py --port 8001
```

Open http://localhost:8001. The preview is labelled and uses fixed text, synthetic
audio, and scripted turn decisions. It demonstrates the interface and interaction
flow, not the model's response quality or speed.

To check loading and inference of the real Smart Turn model:

```bash
uv run --python 3.12 tests/check_smart_turn.py
```

This check downloads the classifier if missing and tests it on silence. It does
not measure accuracy on real speech. On their first run, `uv` may also install the
check scripts' Python dependencies.

Both scripts are saved under `tests/`. Downloaded model assets are kept under
`resources/`, which is ignored by Git. Your own LFM3 folder can be anywhere; pass
its path with `--model`.

# kavachlabs/kavach

## 评论（1/1）

> **inom155** · 2026-10-28T22:31:16.000Z　
> Honestly, I was very impressed with this. I did find the latency was quite high, so I tried to tune it to use MLX on Mac GPUs, and it's so much faster. Very cool either way, we're getting close to a full AI interactive tool that's offline and private!https://github.com/skorotkiewicz/lfm3-chat/pull/1

## 关联链接

- http://localhost:8000
- http://localhost:8001.
- https://:8000/

## 导航

- 项目页：[[10-项目/github.com_02379030]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
