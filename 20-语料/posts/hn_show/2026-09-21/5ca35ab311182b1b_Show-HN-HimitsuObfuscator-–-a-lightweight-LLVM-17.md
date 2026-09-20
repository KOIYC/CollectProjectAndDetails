---
type: "corpus"
item_id: "5ca35ab311182b1b"
title: "Show HN: HimitsuObfuscator – a lightweight LLVM-17 obfuscator for any Linux"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49109917"
project_url: "https://github.com/HimitsuShell/HimitsuObfuscator"
author: "mushstory"
published_at: "2026-07-30T13:43:43Z"
captured_at: "2026-09-21T03:11:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-30"
tags:
  - 语料
  - hn_show
  - author_mushstory
  - story_49109917
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: HimitsuObfuscator – a lightweight LLVM-17 obfuscator for any Linux

> [!info] 一句话导读
> HimitsuShell/HimitsuObfuscator

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49109917>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：mushstory　|　发布：2026-07-30T13:43:43Z
> 项目链接：<https://github.com/HimitsuShell/HimitsuObfuscator>
> 采集：2026-09-21T03:11:18+08:00　|　id：`5ca35ab311182b1b`

## 正文

# HimitsuShell/HimitsuObfuscator

a lightweight llvm-17 obfuscator for any linux

- Stars: 3
- Forks: 1
- Watchers: 3
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-07-27T00:58:18Z

## Languages

- AppleScript
- C
- C++
- CMake
- CSS
- Emacs Lisp
- JavaScript
- Perl
- Python
- Roff
- Ruby
- Shell

## Topics

- compiler
- himitsushell
- linux
- llvm
- musl
- obfuscator
- obfuscator-llvm
- security

## Top Contributors

- MushStory (10 contributions)

---

## README

## HimitsuObfuscator
A lightweight LLVM-17 obfuscator for any Linux.

 Block Flow Graph (Ghidra)

## Usage
```shell
# download and extract obfuscator
curl -LO https://github.com/HimitsuShell/HimitsuObfuscator/releases/download/v1.2.0_0/himitsu_obfuscator_v1.2.0_0.tar
tar -xvf himitsu_obfuscator_v1.2.0_0.tar

vim main.c
-----------------------------
#include <stdio.h>
int main() {
  printf("Hello World!\n");
  return 0;
}
-----------------------------

# builds a binary that runs on any linux (static musl)
sudo apt-get install -y build-essential
./compiler/bin/x86_64-unknown-linux-musl-clang -flto -fuse-ld=lld -mllvm -sobf -mllvm -sub -static main.c -o main
./main
```

### Obfuscation Options
```shell
- bcf         # Bogus Control Flow (Warning: Significantly increases build time and binary size.)
  - bcf_prob  # Probability (1–100, default: 70)
  - bcf_loop  # Number of Iterations (default: 2)
- sub         # Instruction Substitution (add/and/sub/or/xor)
  - sub_loop  # Number of Iterations (default: 1)
- sobf        # String Encryption
- split       # Basic Block Splitting
  - split_num # Number of Splits (default: 3)
- ibr         # Indirect Branches
- icall       # Indirect Calls
- igv         # Indirect Global Variable
```

### System Requirements
- **OS:** Ubuntu 24.04
- **CPU:** x86_64 (Intel/AMD), 2.5 GHz or higher *(6 cores / 12 threads recommended)*
- **Memory:** 16 GB RAM
- **Storage:** 10 GB available space (SSD/NVMe)

### Supported Platforms
- **Linux x86_64 (static musl)**
- Linux ARM64 (Coming Soon)
- Linux ARMv7 (Planned)
- Linux RISC-V 64 (Planned)

## Maintenance (Requires Ubuntu)
```shell
curl -LO https://github.com/HimitsuShell/Himitsu/releases/download/v1.2.0/himitsu_core_v1.2.0.tar.gz

docker load -i himitsu_core_v1.2.0.tar.gz                  # Load docker image
docker run --name himitsu_core -d -it himitsu_core:v1.2.0  # Run container
sudo docker cp himitsu_core:/var/work/compiler/. .         # Copy comiler
sudo chown -R $USER:$USER .                                # Remove root permission
rm -rf himitsu_core_v1.2.0.tar.gz

rm -rf checksums.txt
find . -not -path './.git/*' -type f -exec file {} + | grep -E 'ELF|ar archive' | cut -d: -f1 | sed 's|^\./||' > .gitignore
git ls-files -c -o -i --exclude-standard | while read -r f; do
  sha256sum "$f" >> checksums.txt
  sudo rm -rf "$f"
done

git add .
git commit -m "commit message"
git push origin dev

# github release
sudo docker cp himitsu_core:/var/work/compiler .
sudo chown -R $USER:$USER .
tar -cvf himitsu_obfuscator_v1.2.0_0.tar ./compiler
```

## Discussions
Questions, bug reports, feature requests, and general discussions are welcome.
You can also contact us at hjyun@mushsw.com.

## License
MIT License

# Mojo0869/ABSL

## 关联链接

- https://github.com/HimitsuShell/Himitsu/releases/download/v1.2.0/himitsu_core_v1.2.0.tar.gz
- https://github.com/HimitsuShell/HimitsuObfuscator/releases/download/v1.2.0_0/himitsu_obfuscator_v1.2.0_0.tar

## 导航

- 项目页：[[10-项目/github.com_acf32f64]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
