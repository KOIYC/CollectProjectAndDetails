---
type: "corpus"
item_id: "dcbaaebc384e2084"
title: "Show HN: psi, a 6.4 MB cross-platform portable coding agent in ANSI C & Lua"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50415406"
project_url: "https://psicode.ai/"
author: "siraben"
published_at: "2026-11-08T17:48:19Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_siraben
  - story_50415406
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: psi, a 6.4 MB cross-platform portable coding agent in ANSI C & Lua

> [!info] 一句话导读
> Portability Gallery Docs

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50415406>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：siraben　|　发布：2026-11-08T17:48:19Z
> 项目链接：<https://psicode.ai/>
> 采集：2026-11-09T09:39:29+08:00　|　id：`dcbaaebc384e2084`

## 正文

Skip to content
ψ psi
Portability Gallery Docs
GitHub
The portable coding agent.
6.4 MB portable binary. Written in ANSI C and Lua. Runs on Linux, macOS, Windows, Haiku, and more. Auditable, MIT.
Get started Read the source
Haiku Explore the demo
AT HOME ON Linux macOS Windows FreeBSD OpenBSD Haiku and beyond
From the terminal, for the terminal
 See psi at work.
Small tasks. A running agent.
Edit code
 Live theme
 Add a command
 Explore psi
Play the demo
Find a bug, fix the function, and run it to verify the result.
 Download .cast Download MP4
Play the demo
Change the running agent’s theme with a Lua extension.
 Download .cast Download MP4
Play the demo
Write a Lua extension, reload it, and use the new command.
 Download .cast Download MP4
Play the demo
Follow a slash command through psi’s own source code.
 Download .cast Download MP4
Less between you
and the work.
A coding agent should be a tool you can understand, carry with you, and change. psi starts with a small C core and puts the high-level behavior in Lua.
 The agent loop, terminal interface, tools, and providers are all open to inspection. Keep the parts you need. Build the parts you’re missing.
 Explore the architecture
Choose your model.
 Anthropic, OpenAI Codex, OpenRouter, or local models with Ollama. Resume a session with a different provider.
 Keep your context.
 Branch a conversation, explore another approach, and return. Sessions are append-only JSONL with a full tree.
 Work your way.
 An interactive TUI, a simple REPL, one-shot prompts, and Lua evaluation. At your keyboard or in your scripts.
Open to inspection
 Dependencies, in the open.
What stays with psi, and what builds it.
Connections come from its software bills of materials.
Runtime Build
 Dependency map Linux · x86_64
 13 packages / 21 connections
Select a package to follow its connections. Expand a package for its license and dependencies.
 psi 0.2.0
 Runtime 7 direct argtable 3.3.1 Package license metadata: BSD-3-Clause
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
cjson 1.7.19 Package license metadata: MIT
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
curl 8.22.0 Package license metadata: curl
 3 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
mbedtls 3.6.7 Package license metadata: Apache-2.0, GPL-2.0-or-later
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
nss-cacert 3.126 Package license metadata: MPL-2.0
glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
libedit 20260508-3.1 Package license metadata: BSD-3-Clause
 2 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
ncurses 6.6 Package license metadata: MIT
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
lua 5.5.0 Package license metadata: MIT
 2 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
ncurses 6.6 Package license metadata: MIT
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
nss-cacert 3.126 Package license metadata: MPL-2.0
psi 0.2.0
 Build-only inputs 9 direct bash 5.3p15 Package license metadata: GPL-3.0-or-later
cjson 1.7.19 Package license metadata: MIT
gcc-wrapper 15.3.0 Package license metadata: GPL-3.0-or-later
gnumake 4.4.1 Package license metadata: GPL-3.0-or-later
libedit 20260508-3.1 Package license metadata: BSD-3-Clause
nss-cacert 3.126 Package license metadata: MPL-2.0
pkg-config-wrapper 0.29.2 Package license metadata: GPL-2.0-or-later
stdenv-linux 26.05pre-git Package license metadata: MIT
zlib 1.3.2 Package license metadata: Zlib
psi 0.2.0
 Runtime 7 direct argtable 3.3.1 Package license metadata: BSD-3-Clause
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
cjson 1.7.19 Package license metadata: MIT
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
curl 8.22.0 Package license metadata: curl
 3 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
mbedtls 3.6.7 Package license metadata: Apache-2.0, GPL-2.0-or-later
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
nss-cacert 3.126 Package license metadata: MPL-2.0
glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
libedit 20260508-3.1 Package license metadata: BSD-3-Clause
 2 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
ncurses 6.6 Package license metadata: MIT
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
lua 5.5.0 Package license metadata: MIT
 2 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
ncurses 6.6 Package license metadata: MIT
 1 dependencies glibc 2.42-84 Package license metadata: LGPL-2.0-or-later
 2 dependencies libidn2 2.3.8 Package license metadata: GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 1 dependencies libunistring 1.4.2 Package license metadata: LGPL-3.0-or-later
xgcc 15.3.0 Package license metadata: GPL-3.0-or-later
nss-cacert 3.126 Package license metadata: MPL-2.0
Build-only inputs 9 direct bash 5.3p15 Package license metadata: GPL-3.0-or-later
cjson 1.7.19 Package license metadata: MIT
gcc-wrapper 15.3.0 Package license metadata: GPL-3.0-or-later
gnumake 4.4.1 Package license metadata: GPL-3.0-or-later
libedit 20260508-3.1 Package license metadata: BSD-3-Clause
nss-cacert 3.126 Package license metadata: MPL-2.0
pkg-config-wrapper 0.29.2 Package license metadata: GPL-2.0-or-later
stdenv-linux 26.05pre-git Package license metadata: MIT
zlib 1.3.2 Package license metadata: Zlib
Retained at runtime Build-time only A → B: A depends on B Show all connections
Package details
 Explore the graph
 Select any package.
 Select a node to see its version, package license metadata, and shown connections.
 Shown dependencies
 Shown dependents
Nix runtime closure + direct build inputs for .#default at 646098f . Other platforms and static builds differ. The full build closure contains 918 packages; the diagram shows runtime relationships and direct build-input relationships.
 Runtime SBOM Full build SBOM
Read the dependency list Shown packages and their visible relationships from the runtime and build SBOMs Package Version Shown dependencies License
 psi 0.2.0 argtable, bash, cjson, cjson, curl, gcc-wrapper, glibc, gnumake, libedit, libedit, lua, nss-cacert, nss-cacert, pkg-config-wrapper, stdenv-linux, zlib MIT
 argtable 3.3.1 glibc BSD-3-Clause
 cjson 1.7.19 glibc MIT
 curl 8.22.0 glibc, mbedtls, nss-cacert curl
 glibc 2.42-84 libidn2, xgcc LGPL-2.0-or-later
 libedit 20260508-3.1 glibc, ncurses BSD-3-Clause
 libidn2 2.3.8 libunistring GPL-2.0-or-later, GPL-3.0-or-later, LGPL-3.0-or-later
 libunistring 1.4.2 None recorded LGPL-3.0-or-later
 lua 5.5.0 glibc, ncurses MIT
 mbedtls 3.6.7 glibc Apache-2.0, GPL-2.0-or-later
 ncurses 6.6 glibc MIT
 nss-cacert 3.126 None recorded MPL-2.0
 xgcc 15.3.0 None recorded GPL-3.0-or-later
 bash 5.3p15 None recorded GPL-3.0-or-later
 cjson 1.7.19 None recorded MIT
 gcc-wrapper 15.3.0 None recorded GPL-3.0-or-later
 gnumake 4.4.1 None recorded GPL-3.0-or-later
 libedit 20260508-3.1 None recorded BSD-3-Clause
 nss-cacert 3.126 None recorded MPL-2.0
 pkg-config-wrapper 0.29.2 None recorded GPL-2.0-or-later
 stdenv-linux 26.05pre-git None recorded MIT
 zlib 1.3.2 None recorded Zlib
Portable by design.
 Down to the core.
 C89 and Lua are a deliberate choice. psi runs on familiar desktops and less-traveled systems, with a Cosmopolitan build that runs on Linux, macOS, and Windows.
 Read the portability notes
TESTED OPERATING SYSTEMS STATUS
 Linux Tested
 macOS Tested
 Windows Tested
 FreeBSD / OpenBSD Tested
 Haiku Tested
 Across i686, x86_64, aarch64, and riscv64 where available. See the porting notes for build details.
Compatibility
 Yes, it runs there.
Haiku Tiny Core Linux Linux TTY Windows
Haiku. A little code, a new window. A sakura tree and red vertical Japanese lettering in a native window.
Behind the port Watch the window open Download the native app source
Tiny Core Linux. A small place to think big. Tiny Core Linux 16.2, running the native static musl build.
Behind the port
Linux, straight from the console. Inspecting disks and explaining their layout directly from a Linux VM’s TTY.
Full resolution Watch the partition demo Download recording
Windows. The same agent, another home. The portable build running on Windows.
Full resolution
A little Lua.
A lot of possibility.
 Add a slash command. Register a tool. Subscribe to the agent lifecycle. Your extensions are ordinary Lua files, loaded straight from disk.
 Even the agent loop and terminal rendering live in Lua. Customization goes all the way down.
 Explore the extension API
 ~/.config/psi/extensions/hello.lua LUA
 -- A command, in a few lines.
 return function (psi)
 psi.commands.register( "greet" , function (rest)
 return psi.records.new_command_action(
 "print" , "hi, " .. (rest ~= "" and rest or "friend" )
 )
 end )
 end psi> /greet world hi, world
Small tool.
 Big range.
 Bring a model provider and a project.
psi brings the rest.
Run with Nix Build from source
 nix run github:siraben/psi Copy ⧉
 Requires Nix with flakes enabled.
git clone https://github.com/siraben/psi.git
cd psi
nix develop
make
./build/psi Copy ⧉
 Nix supplies the build dependencies. See the README for details.
Configure your provider before the first agent turn. Provider setup
Build with psi
ψ psi The portable coding agent.
 Source Documentation MIT license
 Built with C & Lua.

## 关联链接

- https://github.com/siraben/psi.git

## 导航

- 项目页：[[10-项目/psicode.ai_af61f600]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
