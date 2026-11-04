---
type: "corpus"
item_id: "3084076c6db4518b"
title: "Show HN: Kiri – a tiny container runtime for macOS, Windows and Rust"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50357807"
project_url: "https://runkiri.com/"
author: "libracoder"
published_at: "2026-11-03T20:35:51Z"
captured_at: "2026-11-04T09:51:43+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - hn_show
  - author_libracoder
  - story_50357807
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Kiri – a tiny container runtime for macOS, Windows and Rust

> [!info] 一句话导读
> New 0.1.17 Mac · Windows

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50357807>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：libracoder　|　发布：2026-11-03T20:35:51Z
> 项目链接：<https://runkiri.com/>
> 采集：2026-11-04T09:51:43+08:00　|　id：`3084076c6db4518b`

## 正文

Skip to content
Beta
Docs
Blog
Community
Releases
Star
Download
New 0.1.17 Mac · Windows · Linux written in Rust
8× faster than Docker.
Share your localhost publicly with one click.
Built from scratch in Rust, not on top of Docker's parts. Kiri runs Docker containers with one daemon. The docker CLI, Compose and the Docker API work as they do today.
The 8×: docker run takes 22 ms on Kiri and 178 ms on Docker Desktop (152 ms on Colima, 279 ms on OrbStack), every engine on 2 CPUs and 8 GB.
CPU and memory · 10 containers running
CPU Memory
Kiri
OrbStack
Colima
Docker Desktop
Sample One Apple-silicon Mac, one runtime at a time. Measured numbers replace these soon. Benchmarks →
Download for Mac
 Watch the race
Free, and in beta on Mac, Windows and Linux. Something broken or annoying? Tell us with Feedback in Kiri's window, and we fix it.
Kiri
Containers Linux VM running
Live web.runkiri.cloud web is shared · 14 visits today Copy link
web nginx:alpine 47 MB Live
db postgres:17 438 MB Up 2 min
api node:22 1.1 GB Up 2 min
redis redis:7 117 MB Exited
Kubernetes 9 pods ready
Works with what
 you already use
docker
 docker compose
 docker buildx
 Docker Engine API
 Docker Hub
 OCI images
 ghcr.io
 Dockerfiles
 docker
 docker compose
 docker buildx
 Docker Engine API
 Docker Hub
 OCI images
 ghcr.io
 Dockerfiles
What's in it
Everything you'd reach for Docker Desktop for.
Containers were the start. Kiri now builds and scans images, runs Kubernetes and whole Linux machines, and puts any container on the internet with one click.
Containers and Compose
Every docker command you use, Compose projects grouped in the window, and a page for each container with live logs, a shell and its files.
Images from Docker Hub
Search Docker Hub from the window and watch each layer pull. amd64 images run through Rosetta.
Builds, with a scan
docker build through BuildKit, a Builds view of every build, and a vulnerability scan of each image on its own page.
Kubernetes
kiri k8s start gives you a k3s cluster in about 20 seconds, with Pods and Services in the window. kind runs too.
Linux machines
kiri machine create dev --distro ubuntu : your user, sudo, and your Mac folders at the same paths.
Share
A public link for any container on runkiri.cloud , from the window or kiri share web . More .
Names and HTTPS
Apps open at web.kiri.local , Compose services at api.myapp.kiri.local , with HTTPS from Kiri's own narrow certificate authority.
Light on your Mac
Unused memory goes back while it runs, and the VM sleeps after a minute idle. The daemon stays around 15 MB; waking takes 0.15 s.
Move over in one go
Bring your images, volumes and containers from OrbStack or Docker Desktop, then switch docker to Kiri from the window.
Prefer the terminal?
The commands you already type.
With Kiri open, the ordinary docker command runs on Kiri, and kiri adds what Docker doesn't have: a name for every container, Kubernetes, Linux machines and a public link.
kiri run , kiri ps work like their docker twins.
web.kiri.localhost reaches a container by name, no port to remember.
kiri k8s start and kiri machine create for a cluster or a Linux box.
kiri share web puts it on the internet.
~ zsh
$ kiri run --rm alpine echo "kiri" prints kiri.
 $ kiri run -d --name web nginx prints a container ID.
 $ kiri ps lists the running web container.
 $ curl http://web.kiri.localhost reaches it by name, with no port to remember.
 $ docker ps shows the same container, because Kiri answers the Docker API.
 $ kiri share web gives it a public link at web.runkiri.cloud.
Illustrative session. With Kiri open, the ordinary docker command runs on Kiri.
Kiri Share
Send anyone a link to a container.
Press Share on a running container and it answers at a public address on runkiri.cloud , over HTTPS, until you press Disconnect. Show a client the branch you're on, test a webhook, or open your app on your phone.
Keep your name. Reserve myapp.runkiri.cloud and it's yours next time too.
Every computer, one list. Shares from your other Macs and PCs show up too, coloured by the machine they run on.
Visitors are warned. The first visit to a share shows a Kiri warning page before it opens, so a link can't pass itself off as your bank. View the warning page →
All about Kiri Share →
Live
 https://web.runkiri.cloud
 Copy
web nginx · 8080 This Mac
api myapp-api · 3000 This Mac
docs astro · 4321 Office PC
Disconnect 3 shares on your account
Getting started
From download to a public link in four steps.
Step 1
Install
Open the disk image and drag Kiri to Applications . It sets up docker for you.
Download for Mac
Step 2
Pull an image
Search Docker Hub in Images and press Pull, or:
docker pull nginx
Step 3
Run a container
Press Run and give it a port. It starts in milliseconds.
docker run -p 80:80 nginx
Step 4
Share
Press Share on the container for a public link, or:
kiri share 80
Compare
Same command, three routes.
OrbStack and Docker Desktop pass every container start through five programs, each with its own socket. Kiri passes it through one daemon that calls the kernel itself. Same docker command on all three.
docker run --rm alpine true
10× slower
 Real time
Run again
OrbStack Measured 0 ms
Five hops. One shim process stays resident for every running container.
Docker Desktop Measured 0 ms
The same five hops, and a shim per running container.
Kiri Measured 0 ms
One daemon creates namespaces, cgroups and mounts itself. Nothing per container is left running. Most of this time is the docker CLI starting up. Through the Docker API, a whole container lifecycle takes 3.1 ms.
Medians from one full run on one Apple Silicon Mac, every engine limited to 2 CPUs and 8 GB, all three through the same docker CLI with Docker's default bridge networking. Stops are drawn evenly; only the totals are figures. Windows has its own race .
Full benchmarks: p99s, the Docker API path and every raw figure →
How it works
One small VM. One daemon. A socket between them.
On macOS, Kiri boots a single Linux VM through Apple's Virtualization.framework, with a custom kernel and a small Rust init as PID 1. The host and guest talk over vsock. Inside, the Kiri daemon creates each container with clone3 . On Linux the same daemon runs on your own kernel with no VM at all, and on Windows it runs inside WSL2.
One VM, one daemon See the numbers →
Boot once
 One VM serves every container. Cold boot to ready takes 112 ms , down from 810 ms on a stock kernel.
Talk directly
 Requests cross one vsock channel into the VM, not a chain of Unix sockets. A round trip takes guest vsock round trip p50">31 µs .
Leave nothing behind
 No process stays per container. OrbStack keeps a shim for each one: 143 running containers held 1.13 GB in shims on our test Mac.
Measured on one Apple Silicon Mac. Method and raw numbers are on the benchmarks page .
The app
A native app, not a web wrapper.
AppKit and the system WebKit on the Mac, Win32 and WebView2 on Windows, so no Electron and no bundled browser. Manage containers, images, volumes, networks and Compose projects, with live stats, logs, a terminal and files for each container. Running apps open by name at myapp.kiri.local . On the Mac it brings your images and volumes over from OrbStack or Docker Desktop, and lives in the menu bar.
Mac One minimal Linux VM through Virtualization.framework
Windows Inside WSL2, with the Docker API on a named pipe (beta)
Linux Native, no VM at all: the daemon calls clone3 on your kernel
‹ ›
 Docker
Containers 5
Images 7
Volumes 3
Networks 3
Builds
Kubernetes On
Pods 9
Services 4
Kiri
Share
Settings
Linux VM Running
Running 4
CPUs 23% · 2
Memory 657 MB / 4 GB
Kubernetes On · :6444
Stop
Containers 4 running · 5
Filter
Live web.runkiri.cloud web is shared · 14 visits today Copy link
Name Image State Created Actions
web
 nginx:alpine
 Up 2 min
 2 min ago
 Live ···
api
 node:22
 Up 2 min
 2 min ago
 Share ···
db
 postgres:17
 Up 2 min
 2 min ago
 Share ···
worker
 python:3.13
 Up 40 s
 1 min ago
 Share ···
redis
 redis:7
 Exited (0)
 1 h ago
 Start ···
Kiri 0.1.17
Linux VM running
 · 4 of 5 running
 · 657 MB of 4 GB
 · docker → default
 · Feedback
Download
Kiri for Mac is out.
Every number on this page was measured on it. Kiri sets up a kiri docker context and brings its own docker , Compose and buildx, so there's nothing else to install. Coming from OrbStack or Docker Desktop? Kiri brings your images and volumes over.
Download for Mac All platforms
Then, in a new terminal:
$ docker run --rm hello-world
 Same docker and docker compose you use today.
0.1.17 · Apple silicon · macOS 14+
A small, fast container runtime for Mac, Windows and Linux. Written in Rust.
Docs
Community
Compare
How it works
Mac
Windows
Linux
Share
Benchmarks
Releases
Raw results
Blog
© 2026 the Kiri contributors. Docker is a trademark of Docker, Inc. OrbStack and other names belong to their owners and are used only to describe measurements.

## 关联链接

- http://web.kiri.localhost
- https://web.runkiri.cloud

## 导航

- 项目页：[[10-项目/runkiri.com_6e99cd2a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
