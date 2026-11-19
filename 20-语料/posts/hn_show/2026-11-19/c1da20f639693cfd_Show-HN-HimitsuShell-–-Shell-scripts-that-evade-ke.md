---
type: "corpus"
item_id: "c1da20f639693cfd"
title: "Show HN: HimitsuShell – Shell scripts that evade kernel tracing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50551093"
project_url: "https://github.com/HimitsuShell/HimitsuShell"
author: "mushstory"
published_at: "2026-11-18T19:42:15Z"
captured_at: "2026-11-19T09:43:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_mushstory
  - story_50551093
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: HimitsuShell – Shell scripts that evade kernel tracing

> [!info] 一句话导读
> HimitsuShell/HimitsuShell

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50551093>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mushstory　|　发布：2026-11-18T19:42:15Z
> 项目链接：<https://github.com/HimitsuShell/HimitsuShell>
> 采集：2026-11-19T09:43:31+08:00　|　id：`c1da20f639693cfd`

## 正文

# HimitsuShell/HimitsuShell

shell script protector (obfuscation, embedded interpreter, anti-tamper, DRM) - linux, IoT

- Stars: 9
- Forks: 3
- Watchers: 9
- Open issues: 0
- License: Other
- Homepage: https://himitsushell.com/
- Default branch: main
- Created: 2026-02-28T12:35:14Z

## Languages

- Shell

## Topics

- bash
- compiler
- drm
- embedded-linux
- encryption
- iot
- llvm
- musl
- obfuscator
- protection
- shc
- shell
- shell-script

## Top Contributors

- MushStory (25 contributions)

---

## README

**README:** English | 中文 | 日本語

# HimitsuShell
Protects shell scripts from leaks, tampering, and unauthorized use.

Converts shell scripts into static binaries with an embedded interpreter, obfuscation, and anti-debug protections (shc alternative).

 Block Flow Graph (Ghidra)

## Usage
```shell
# 1. download and load docker image
curl -LO https://github.com/HimitsuShell/Himitsu/releases/download/v1.2.0/himitsu_core_v1.2.0.tar.gz
docker load -i himitsu_core_v1.2.0.tar.gz

# 2. start container
docker run --name himitsu_core -d -it himitsu_core:v1.2.0

# 3. upload your shell script (must be named launcher.sh)
docker cp launcher.sh himitsu_core:/var/work/

# 4. build and download binary (10–20 seconds)
docker exec himitsu_core /var/work/compile.sh
docker cp himitsu_core:/var/work/safeLauncher .
```

#### Obfuscation Options (LLVM-based)
```shell
# obfuscation options
- bcf         # bogus control flow (warning: significantly increases build time and binary size.)
  - bcf_prob  # probability (1–100, default: 70)
  - bcf_loop  # number of iterations (default: 2)
- sub         # instruction substitution (add/and/sub/or/xor)
  - sub_loop  # number of iterations (default: 1)
- sobf        # string encryption
- split       # basic block splitting
  - split_num # number of splits (default: 3)
- ibr         # indirect branches
- icall       # indirect calls
- igv         # indirect global variable

# default options
sobf, icall, ibr, igv, sub

# how to customize
modify /var/work/compile.sh inside the `himitsu_core` container.
```

#### System Requirements
- **CPU:** x86_64 (Intel/AMD), 2.5 GHz or higher *(6 cores / 12 threads recommended)*
- **Memory:** 16 GB RAM
- **Storage:** 10 GB available space (SSD/NVMe)

#### Supported Platforms
- **Linux x86_64 (static musl)**
- Linux ARM64 (Coming Soon)
- Linux ARMv7 (Planned)
- Linux RISC-V 64 (Planned)

## Features
- **OS-Level Logging & Hooking Protection**
 Executes shell scripts using its own embedded shell interpreter instead of the system shell (e.g., `/bin/bash`). Shell scripts are not exposed even by OS-level logging and hooking (`auditd`, `bpftrace`).

- **String & Constant Encryption**
 All strings and constants in the binary are encrypted, making static analysis more difficult (e.g., `IDA`, `Ghidra`).

- **Debugger Detection**
 Continuously detects debuggers during execution, making dynamic analysis more difficult (e.g., `gdb`, `ptrace`, `strace`).

- **Advanced Obfuscation Techniques**
 Features instruction substitution, indirect calls, indirect branches, basic block splitting, and bogus control flow.

- **License Verification (Planned)**
 Restricts shell script execution to users with a valid license key.

## Research & Security Analysis
#### Why not shc, ssc, etc.?
Known auto decompilation tools:
- UnSHc: https://github.com/yanncam/UnSHc
- unshell: https://github.com/Rem01Gaming/unshell

#### Compared to shc
| | HimitsuShell | shc |
|-|-|-|
| OS-Level Logging & Hooking Protection | ✓ | |
| Dynamic Library Hooking Protection | ✓ | |
| String & Constant Encryption | ✓ | |
| Debugger Detection | ✓ | ✓ |
| Advanced Obfuscation Techniques | ✓ | |

#### Articles
- How to Protect Source Code Inside Docker Images (DRM, Obfuscation)
- Shell Script-to-Binary Tools: shc vs. HimitsuShell
- shc Security Analysis: Structural Limitations of a Shell Script Compiler
- ssc Security Analysis: Structural Limitations of a Shell Script Compiler

## FAQ
- **Which Linux shells are supported?**
 Supports POSIX/LSB-compliant shells (e.g., /bin/sh).

- **Do Bash or Zsh scripts work?**
 They work, but errors can occur. We recommend testing before use.

- **Which shell commands are supported?**
 The commands listed below are built into the binary. Other commands also work, but they rely on the system shell and may be exposed to hooking or logging.

 basename bash blkdiscard blkid blockdev bunzip2 bzcat cal cat chattr chgrp chmod chown chroot chrt chvt cksum clear cmp comm count cp cpio crc32 cut date dd deallocvt devmem df dirname dmesg dnsdomainname dos2unix du echo egrep eject env expand factor fallocate false fgrep file find flock fmt fold free freeramdisk fsfreeze fstype fsync ftpget ftpput getconf getopt gpiodetect gpiofind gpioget gpioinfo gpioset grep groups gunzip halt hd head help hexedit host hostname httpd hwclock i2cdetect i2cdump i2cget i2cset i2ctransfer iconv id ifconfig inotifyd insmod install ionice iorenice iotop kill killall killall5 link linux32 ln logger login logname losetup ls lsattr lsmod lspci lsusb makedevs mcookie md5sum memeater microcom mix mkdir mkfifo mknod mkpasswd mkswap mktemp modinfo mount mountpoint mv nbd-client nbd-server nc netcat netstat nice nl nohup nologin nproc nsenter od oneit openvt partprobe paste patch pgrep pidof ping ping6 pivot_root pkill pmap poweroff printenv printf prlimit ps pwd pwdx pwgen readahead readelf readlink realpath reboot renice reset rev rfkill rm rmdir rmmod rtcwake sed seq setfattr setsid sh sha1sum sha224sum sha256sum sha384sum sha3sum sha512sum shred shuf sleep sntp sort split stat strings su swapoff swapon switch_root sync sysctl tac tail tar taskset tee test time timeout top touch true truncate ts tsort tty tunctl uclampset ulimit umount uname unicode uniq unix2dos unlink unshare uptime usleep uudecode uuencode uuidgen vconfig vmstat w watch watchdog wc wget which who whoami xargs xxd yes zcat

- **Can I use only the obfuscation engine?**
 Yes. See HimitsuObfuscator

## Discussions
Questions, bug reports, feature requests, and general discussions are welcome.
You can also contact us at hjyun@mushsw.com.

## License
HimitsuShell has a dual license model with a Community Edition for noncommercial use: Polyform Noncommercial 1.0.0.

With this license HimitsuShell is free to use for personal/noncommercial use, but will require a Commercial Edition to be used in a commercial business.

Commercial Edition can be purchased at himitsushell.com. For more details on our licensing, see our Terms of Service.

# skorotkiewicz/poptato

## 关联链接

- https://github.com/HimitsuShell/Himitsu/releases/download/v1.2.0/himitsu_core_v1.2.0.tar.gz
- https://github.com/Rem01Gaming/unshell
- https://github.com/yanncam/UnSHc
- https://himitsushell.com/

## 导航

- 项目页：[[10-项目/github.com_c91e6238]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
