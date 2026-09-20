---
type: "corpus"
item_id: "702aaafdb9b3c32a"
title: "Show HN: Golang binaries built for your users depending on their arch and system"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47962828"
project_url: "https://goblin.run/"
author: "aliezsid"
published_at: "2026-04-30T14:13:33Z"
captured_at: "2026-09-21T02:52:24+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_aliezsid
  - story_47962828
  - show_hn
metrics: {"points": 8, "comments": 7, "engagement_velocity": 8}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:174d"
---

# Show HN: Golang binaries built for your users depending on their arch and system

> [!info] 一句话导读
> this.hits = hitsCount.count

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47962828>
> 指标：点赞=8 · 评论=7 · engagement_velocity=8
> 作者：aliezsid　|　发布：2026-04-30T14:13:33Z
> 项目链接：<https://goblin.run/>
> 采集：2026-09-21T02:52:24+08:00　|　id：`702aaafdb9b3c32a`

## 正文

d.json());
 this.hits = hitsCount.count
 },
 }"
 >
 Skip to main content
Goblin
Report Bugs / Issues
Star us on GitHub
Golang binaries in a curl, built by
 goblins
Install Go binaries—without Go.
curl -sf http://goblin.run/github.com/rakyll/hey | sh
{
 $data.copied = true
 setTimeout(() => { $data.copied = false }, 1500)
 $clipboard('curl -sf http://goblin.run/github.com/rakyll/hey | sh')
 }"
 class="flex items-center justify-center transition-all rounded shadow w-7 h-7 cursor-copy bg-base text-subtle hover:text-text hover:shadow-md"
 >
Get Started
If you get value from using Goblin, please consider
 donating . This helps cover server costs and supports my open source work.
Usage
Install package with optional @version and options :
curl -sf http://goblin.run/[@version] | [...options] sh
API
package - Complete module path
github.com/barelyhuman/commitlog
gopkg.in/yaml.v2
version - Exact or partial version range, optionally prefixed with "v"
# Install the latest version

# Install v1.2.3
@v1.2.3
# Install v3.x.x
@v3
Options
Control Goblin's behavior with environment variables
PREFIX - Change installation location (default: /usr/local/bin )
# Install to /tmp
... | PREFIX=/tmp sh
OUT - Rename the resulting binary (default:  )
# Export Windows executable
... | OUT=example.exe sh
CMD_PATH - Path to the binary package (default: "")
# Export Windows executable
... | CMD_PATH="/cmd/example" sh
Examples
Install the latest version:
curl -sf http://goblin.run/github.com/rakyll/hey | sh
Specify package version:
curl -sf http://goblin.run/github.com/barelyhuman/statico@v0.0.7 | sh
Or use commit hashes:
curl -sf http://goblin.run/github.com/barelyhuman/commitlog@bba8d7a63d622e4f12dbea9722b647cd985be8ad | sh
Use alternative sources:
curl -sf http://goblin.run/golang.org/x/tools/godoc | sh
Specify nested packages
Note: nested package expect the path to be a package main file with a main
call. If you use something like spf13/cobra then check the 2nd example.
curl -sf http://goblin.run/vito/bass/cmd/bass | sh
curl -sf http://goblin.run/gnorm.org/gnorm | CMD_PATH="/cli" PREFIX=./bin sh
How does it work?
Each request resolves the needed tags and versions from
proxy.golang.org . If no module is found, you can try
replacing the version with a commit hash on supported platforms, e.g. GitHub.
The response of this request is a Golang binary compiled for the requested
operating system, architecture, package version, and the binary's name—using Go (current supported version can be checked on the source repo )
Example response
http://goblin.run/binary/github.com/rakyll/hey?os=darwin&arch=amd64&version=v0.1.3&out=hey
Note: compilation is limited to 200 seconds due to timeout restrictions.
View source on GitHub
0 hits

## 评论（7/7）

> **fractorial** · 2026-05-03T02:37:38.000Z　
> I cannot fathom why anyone would want this.

---

> **ivere27** · 2026-05-03T02:56:41.000Z　
> so, it's kinda build server, building golang sources in remote server?
> then, download the built binary?
> it seems to be useful for normal enduser I guess

---

> **guessmyname** · 2026-05-03T03:43:06.000Z　
> Oh, this web service is going to be such a nice target for hackers waiting to infect everyone who dares download random binaries. Centralizing “builds on demand” like this creates a pretty juicy supply-chain target. If the service gets popped, you’ve got a one-stop shop for shipping compromised binaries to every arch/OS combo. Convenient idea, but I’d only trust it with strong guarantees: reproducible builds, signed artifacts tied to commits, and a way to verify locally. Otherwise it’s basically “go install URL” with extra steps.

---

> **oefrha** · 2026-05-03T04:15:18.000Z　
> If you're in the market for this kind of thin convenience wrapper you might as well just vibe code a .goreleaser.yaml, .github/workflows/releases.yml and an install.sh. Takes a couple minutes, and you don't need to face angry users when this service is hacked/turns evil/shuts down. (Before anyone protests vibe coding, you're doing less due diligence by using this.)

---

> **duskwuff** · 2026-05-03T04:20:08.000Z　
> > The response of this request is a Golang binary compiled for the requested
> operating system, architecture, package version, and the binary's name—using Go
> 1.17.xUh... Go 1.17 is almost five years old. (The current version is 1.26.) Why is this service using an ancient version of Go?

---

> **gbraad** · 2026-05-03T03:10:35.000Z　
> It is mostly indicative of another underlying issue, like glibc versions or so. But this also leads to weird situations with reproducibility for QE/error reporting. One of the reasons I also hated some distro wanting to devendor and use distro dependencies. This all makes it harder to have a consistent support matrix.

---

> **fractorial** · 2026-05-03T04:29:29.000Z　
> Precisely; Go is by no means perfect, but if you want to throw away its security efforts, by all means use goblin.runI’ll take vibe shooting myself in the foot over lying to myself any day.

## 关联链接

- http://goblin.run/
- http://goblin.run/binary/github.com/rakyll/hey?os=darwin&arch=amd64&version=v0.1.3&out=hey
- http://goblin.run/github.com/barelyhuman/commitlog@bba8d7a63d622e4f12dbea9722b647cd985be8ad
- http://goblin.run/github.com/barelyhuman/statico@v0.0.7
- http://goblin.run/github.com/rakyll/hey
- http://goblin.run/gnorm.org/gnorm
- http://goblin.run/golang.org/x/tools/godoc
- http://goblin.run/vito/bass/cmd/bass

## 导航

- 项目页：[[10-项目/goblin.run_23945c84]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
