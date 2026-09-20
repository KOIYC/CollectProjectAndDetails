---
type: "corpus"
item_id: "ad43ad57e4d9e61a"
title: "Show HN: Secure-by-default Ollama Docker image with built-in auth, only ~70MB"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47962141"
project_url: "https://github.com/hwdsl2/docker-ollama"
author: "hwdsl2"
published_at: "2026-04-30T13:29:58Z"
captured_at: "2026-09-21T02:52:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_hwdsl2
  - story_47962141
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Secure-by-default Ollama Docker image with built-in auth, only ~70MB

> [!info] 一句话导读
> hwdsl2/docker-ollama

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47962141>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：hwdsl2　|　发布：2026-04-30T13:29:58Z
> 项目链接：<https://github.com/hwdsl2/docker-ollama>
> 采集：2026-09-21T02:52:25+08:00　|　id：`ad43ad57e4d9e61a`

## 正文

# hwdsl2/docker-ollama

Docker image to run an Ollama local LLM server. Secure by default, all API requests require a Bearer token (auto-generated on first start). OpenAI-compatible API. Supports first-start model pre-pull, NVIDIA GPU (CUDA) acceleration, and persistent model storage. Multi-arch: amd64, arm64.

- Stars: 10
- Forks: 0
- Watchers: 10
- Open issues: 1
- License: Other
- Homepage: https://hub.docker.com/r/hwdsl2/ollama-server
- Default branch: main
- Created: 2026-04-29T12:46:45Z

## Languages

- Dockerfile
- Shell

## Topics

- ai
- authentication
- cuda
- deep-learning
- docker
- docker-compose
- docker-image
- gpu
- inference
- langchain
- large-language-models
- linux
- llm
- local-ai
- local-llm
- ollama
- openai
- openai-compatible
- private-ai
- self-hosted

## Top Contributors

- hwdsl2 (55 contributions)

---

## README

English | 简体中文 | 繁體中文 | Русский

# Ollama on Docker

Build Status  Docker Pulls  License: MIT

Part of the Self-Hosted AI Stack — deploy a complete self-hosted AI stack with a single command.

Docker image to run an Ollama local LLM server. Provides Ollama's OpenAI-compatible `/v1` API subset for running large language models locally. Based on Debian Trixie (slim). Designed to be simple, private, and secure by default.

> 📘 **New book:** The Self-Hosted AI Builder’s Guide — learn how to deploy this service as part of a complete, secure-by-default private AI stack.

**Features:**

- **Secure by default** — all API requests require a Bearer token (auto-generated on first start)
- Auto-generates an API key on first start, stored in the persistent volume
- First-start model pre-pull via `OLLAMA_MODELS` environment variable
- Model management via a helper script (`ollama_manage`)
- OpenAI-compatible `/v1` API subset — point compatible OpenAI SDK and app workflows at your local server with a one-line change
- Caddy reverse proxy enforces Bearer token auth on all API requests (except `/` health check)
- NVIDIA GPU (CUDA) acceleration for faster inference (`:cuda` image tag)
- Automatically built and published via GitHub Actions
- Persistent model storage via a Docker volume
- Lightweight image (~75MB); multi-arch: `linux/amd64`, `linux/arm64`

**Also available:**

- Related AI services: Whisper, Kokoro, Embeddings, LiteLLM, Docling, MCP Gateway

## Community

- 📬 Subscribe for project updates (1–2 emails/month) — get free AI and VPN deployment guides (PDF)
- 💬 Join the r/selfhostedstack community for discussions and showcases
- ⭐ Star the repository if you find it useful — it helps others discover it

 Self-hosted VPN & networking projects

- Setup IPsec VPN
- IPsec VPN on Docker
- WireGuard
- OpenVPN
- Headscale

## Security note

~175,000 Ollama servers were found publicly exposed without authentication (source). A bare Ollama install binds to all interfaces with no auth by default. This image enforces **Bearer token authentication on all API requests** via a built-in auth proxy, so unauthorized access is blocked even if the port is accidentally exposed.

## Quick start

**Step 1.** Start the Ollama server:

```bash
docker run \
    --name ollama \
    --restart=always \
    -v ollama-data:/var/lib/ollama \
    -p 11434:11434/tcp \
    -d hwdsl2/ollama-server
```

On first start, an API key is auto-generated and displayed in the container logs. All API requests require this key.

**Note:** For internet-facing deployments, using a reverse proxy to add HTTPS is **strongly recommended**. In that case, also replace `-p 11434:11434/tcp` with `-p 127.0.0.1:11434:11434/tcp` in the `docker run` command above, to prevent direct access to the unencrypted port.

**Step 2.** Get the API key:

```bash
# View the key in the container logs
docker logs ollama

# Or retrieve it for use in scripts
API_KEY=$(docker exec ollama ollama_manage --getkey)
```

The API key is displayed in a box labeled **Ollama API key**. To display it again at any time:

```bash
docker exec ollama ollama_manage --showkey
```

**Step 3.** Pull a model:

```bash
docker exec ollama ollama_manage --pull llama3.2:3b
```

**Tip:** To pull one or more models automatically on first start, set `OLLAMA_MODELS` before running the container:

```bash
docker run \
    --name ollama \
    --restart=always \
    -v ollama-data:/var/lib/ollama \
    -p 11434:11434/tcp \
    -e OLLAMA_MODELS=llama3.2:3b \
    -d hwdsl2/ollama-server
```

Or add `OLLAMA_MODELS=llama3.2:3b` to your `ollama.env` file (see Environment variables).

**Step 4.** Test with the API:

```bash
API_KEY=$(docker exec ollama ollama_manage --getkey)

# List models
curl http://localhost:11434/api/tags \
  -H "Authorization: Bearer $API_KEY"

# Chat completion (streaming)
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"model": "llama3.2:3b", "messages": [{"role": "user", "content": "Hello!"}]}'
```

**Note:** The `docker exec` management commands (`ollama_manage`) do not require the API key.

To learn more about how to use this image, read the sections below.

## Requirements

- A Linux server (local or cloud) with Docker installed
- Sufficient disk space for models (3B models ≈ 2GB, 7B models ≈ 4–5GB, 14B+ models ≈ 8–10GB+)
- Sufficient RAM to run models (3B models ≈ 2–4GB, 7B models ≈ 6–8GB, 14B+ models ≈ 12–16GB+)
- TCP port 11434 (or your configured port) accessible

**For GPU acceleration (`:cuda` image):**

- NVIDIA GPU with CUDA support
- NVIDIA driver 575.57.08+ (Linux) or 576.57+ (Windows) installed on the host
- NVIDIA Container Toolkit installed
- The `:cuda` image supports `linux/amd64` only

## Download

Get the trusted build from the Docker Hub registry:

```bash
docker pull hwdsl2/ollama-server
```

For GPU support:

```bash
docker pull hwdsl2/ollama-server:cuda
```

Alternatively, you may download from Quay.io:

```bash
docker pull quay.io/hwdsl2/ollama-server
docker image tag quay.io/hwdsl2/ollama-server hwdsl2/ollama-server
```

Supported platforms: `linux/amd64` and `linux/arm64`. The `:cuda` tag supports `linux/amd64` only.

## Environment variables

All variables are optional. If not set, secure defaults are used automatically.

This Docker image uses the following variables, that can be declared in an `env` file (see example):

| Variable | Description | Default |
|---|---|---|
| `OLLAMA_API_KEY` | API key for authenticating requests (auto-generated if not set) | Auto-generated |
| `OLLAMA_PORT` | TCP port for the API (1–65535) | `11434` |
| `OLLAMA_HOST` | Hostname or IP shown in startup info and `--showkey` output | Auto-detected |
| `OLLAMA_DEBUG` | Set to `1` to enable verbose debug logging | *(not set)* |
| `OLLAMA_MODELS` | Comma-separated models to pull on first start, e.g. `llama3.2:3b,qwen2.5:7b` | *(not set)* |
| `OLLAMA_MAX_LOADED_MODELS` | Max models kept loaded in memory simultaneously | *(Ollama default)* |
| `OLLAMA_NUM_PARALLEL` | Number of parallel request slots per model | *(Ollama default)* |
| `OLLAMA_CONTEXT_LENGTH` | Default context window size in tokens | *(Ollama default)* |
| `OLLAMA_DISABLE_USAGE_COUNTS` | Set to `1` to disable anonymous aggregate usage counts. | *(not set)* |

**Note:** In your `env` file, you may enclose values in single quotes, e.g. `VAR='value'`. Do not add spaces around `=`. If you change `OLLAMA_PORT`, update the `-p` flag in the `docker run` command accordingly.

Example using an `env` file:

```bash
cp ollama.env.example ollama.env
# Edit ollama.env and set your values, then:
docker run \
    --name ollama \
    --restart=always \
    -v ollama-data:/var/lib/ollama \
    -v ./ollama.env:/ollama.env:ro \
    -p 11434:11434/tcp \
    -d hwdsl2/ollama-server
```

## Model management

Use `docker exec` to manage models with the `ollama_manage` helper script. Models are stored in the Docker volume and persist across container restarts.

**List downloaded models:**

```bash
docker exec ollama ollama_manage --listmodels
```

**Pull a model:**

```bash
# Small, fast models (recommended for getting started)
docker exec ollama ollama_manage --pull llama3.2:3b
docker exec ollama ollama_manage --pull qwen2.5:7b

# Larger models (require more RAM/VRAM)
docker exec ollama ollama_manage --pull mistral:7b
docker exec ollama ollama_manage --pull phi4:14b
docker exec ollama ollama_manage --pull gemma3:12b
```

**Remove a model:**

```bash
docker exec ollama ollama_manage --remove llama3.2:3b
```

**Show running models and memory usage:**

```bash
docker exec ollama ollama_manage --status
```

**Update all models** (re-pulls latest versions):

```bash
docker exec ollama ollama_manage --update
```

**Show the API key:**

```bash
docker exec ollama ollama_manage --showkey
```

**Get the API key** (machine-readable, for use in scripts):

```bash
API_KEY=$(docker exec ollama ollama_manage --getkey)
```

**Pull models on first start** using the `OLLAMA_MODELS` variable in your `env` file:

```
OLLAMA_MODELS=llama3.2:3b,qwen2.5:7b
```

## Using the API

All API requests require a Bearer token. Retrieve the API key first:

```bash
API_KEY=$(docker exec ollama ollama_manage --getkey)
```

**Ollama API:**

```bash
# List models
curl http://localhost:11434/api/tags \
  -H "Authorization: Bearer $API_KEY"

# Generate (streaming)
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"model": "llama3.2:3b", "prompt": "Why is the sky blue?"}'

# Chat completion (streaming)
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"model": "llama3.2:3b", "messages": [{"role": "user", "content": "Hello!"}]}'
```

**OpenAI-compatible API** (Ollama `/v1` subset; works with compatible OpenAI SDK and app workflows):

```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"model": "llama3.2:3b", "messages": [{"role": "user", "content": "Hello!"}]}'
```

**Python (OpenAI SDK):**

```python
from openai import OpenAI

client = OpenAI(
    api_key="<your-api-key>",
    base_url="http://localhost:11434/v1",
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

## Persistent data

All server data is stored in the Docker volume (`/var/lib/ollama` inside the container):

```
/var/lib/ollama/
├── models/           # Downloaded model files
├── .api_key          # API key (auto-generated, or synced from OLLAMA_API_KEY)
├── .initialized      # First-run marker
├── .port             # Saved port (used by ollama_manage)
└── .Caddyfile        # Generated Caddy config (auth proxy)
```

Back up the Docker volume to preserve your models and API key.

## Using docker-compose

```bash
cp ollama.env.example ollama.env
# Edit ollama.env and set your values, then:
docker compose up -d
docker logs ollama
```

Example `docker-compose.yml` (already included):

```yaml
services:
  ollama:
    image: hwdsl2/ollama-server
    container_name: ollama
    restart: always
    ports:
      - "11434:11434/tcp"  # For a host-based reverse proxy, change to "127.0.0.1:11434:11434/tcp"
    volumes:
      - ollama-data:/var/lib/ollama
      - ./ollama.env:/ollama.env:ro

volumes:
  ollama-data:
    name: ollama-data
```

**Note:** For internet-facing deployments, using a reverse proxy to add HTTPS is **strongly recommended**. In that case, also change `"11434:11434/tcp"` to `"127.0.0.1:11434:11434/tcp"` in `docker-compose.yml`, to prevent direct access to the unencrypted port.

### GPU acceleration (CUDA)

Use `docker-compose.cuda.yml` to run with NVIDIA GPU support:

```bash
docker compose -f docker-compose.cuda.yml up -d
```

**Requirements:** NVIDIA GPU, NVIDIA driver 575.57.08+ (Linux) or 576.57+ (Windows), and the NVIDIA Container Toolkit installed on the host. The `:cuda` image is `linux/amd64` only.

## Using a reverse proxy

For internet-facing deployments, place a reverse proxy in front of Ollama to handle HTTPS termination. The server works without HTTPS on a local or trusted network, but HTTPS is recommended when the API endpoint is exposed to the internet.

Use one of the following addresses to reach the Ollama container from your reverse proxy:

- **`ollama:11434`** — if your reverse proxy runs as a container in the **same Docker network** as Ollama (e.g. defined in the same `docker-compose.yml`).
- **`127.0.0.1:11434`** — if your reverse proxy runs **on the host** and port `11434` is published (the default `docker-compose.yml` publishes it).

**Note:** The `Authorization: Bearer` header passes through reverse proxies automatically — no special configuration needed.

**Example with Caddy (Docker image)** (automatic TLS via Let's Encrypt, reverse proxy in the same Docker network):

`Caddyfile`:
```
ollama.example.com {
  reverse_proxy ollama:11434
}
```

**Example with nginx** (reverse proxy on the host):

```nginx
server {
    listen 443 ssl;
    server_name ollama.example.com;

    ssl_certificate     /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass         http://127.0.0.1:11434;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
        proxy_http_version 1.1;       # required for streaming responses
        proxy_read_timeout 300s;
        proxy_buffering    off;
    }
}
```

After setting up a reverse proxy, set `OLLAMA_HOST=ollama.example.com` in your `env` file so that the correct endpoint URL is shown in the startup logs and `ollama_manage --showkey` output.

## Update Docker image

To update the Docker image and container:

```bash
docker pull hwdsl2/ollama-server
docker rm -f ollama
# Then re-run the docker run command from Quick start with the same volume.
```

Your downloaded models are preserved in the `ollama-data` volume.

## Using with other AI services

Ollama can be used as the local LLM service in a broader self-hosted AI setup.

For full and lightweight Docker Compose stacks, manual `docker run` examples, and voice/RAG/MCP pipeline examples with Kokoro, Embeddings, LiteLLM, Ollama, Docling, and MCP Gateway, see Self-Hosted AI Stack.

**Connect Ollama to LiteLLM:**

```bash
# In docker-litellm, add Ollama as a model provider:
docker exec litellm litellm_manage \
  --addmodel ollama/llama3.2:3b \
  --base-url http://ollama:11434
```

## Usage counts

This image uses public GitHub release asset download counts for anonymous, aggregate usage counts. Counts are approximate and are not unique users or active installs. The image does not send a telemetry payload or use a private collector. It only attempts the best-effort count after the server starts successfully with a mounted `/var/lib/ollama` volume, and again when that persistent install first runs a different image build. To opt out, set `OLLAMA_DISABLE_USAGE_COUNTS=1`.

## Technical details

- Base image: `debian:trixie-slim` for `:latest`; `nvidia/cuda` for `:cuda`
- Image size: ~75MB (CPU) / ~1.7GB (CUDA)
- Ollama: latest release, installed as a static binary
- Auth proxy: Caddy (always active, enforces Bearer token auth)
- Data directory: `/var/lib/ollama` (Docker volume)
- Model storage: `/var/lib/ollama/models` inside the volume
- Ollama API: `http://localhost:11434` (or your configured port)
- OpenAI-compatible API: `http://localhost:11434/v1`

## License

**Note:** The software components inside the pre-built image (such as Ollama, Caddy, and their dependencies) are under the respective licenses chosen by their respective copyright holders. As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.

Copyright (C) 2026 Lin Song
This work is licensed under the MIT License.

**Ollama** is Copyright (C) 2023 Ollama, and is distributed under the MIT License.

**Caddy** is Copyright (C) 2015 Matthew Holt and The Caddy Authors, and is distributed under the Apache License 2.0.

This project is an independent Docker setup for Ollama and is not affiliated with, endorsed by, or sponsored by Ollama.

# Claude Code Security | Architectural Review Inside Your IDE | Trent AI

## 关联链接

- http://127.0.0.1:11434;
- http://localhost:11434/api/chat
- http://localhost:11434/api/generate
- http://localhost:11434/api/tags
- http://localhost:11434/v1
- http://localhost:11434/v1/chat/completions
- http://localhost:11434/v1`
- http://localhost:11434`
- http://ollama:11434
- https://hub.docker.com/r/hwdsl2/ollama-server

## 导航

- 项目页：[[10-项目/github.com_4ba04dfe]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
