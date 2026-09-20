---
type: "project"
title: "Show HN: HimitsuObfuscator – a lightweight LLVM-17 obfuscator for any Linux"
project_url: "https://github.com/HimitsuShell/HimitsuObfuscator"
first_seen: "2026-09-21T03:11:18+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mushstory
  - story_49109917
  - show_hn
lang: "en"
---

# Show HN: HimitsuObfuscator – a lightweight LLVM-17 obfuscator for any Linux

> [!info] 一句话导读
> HimitsuShell/HimitsuObfuscator

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/HimitsuShell/HimitsuObfuscator>
> 首次收录：2026-09-21T03:11:18+08:00
> 来源渠道：HN Show HN
> 标签：author_mushstory, story_49109917, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/5ca35ab311182b1b_Show-HN-HimitsuObfuscator-–-a-lightweight-LLVM-17]] |
| 2026-09-21T03:11:18+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/5ca35ab311182b1b_Show-HN-HimitsuObfuscator-–-a-lightweight-LLVM-17]] |

## 摘要正文

# HimitsuShell/HimitsuObfuscator  a lightweight llvm-17 obfuscator for any linux  - Stars: 3 - Forks: 1 - Watchers: 3 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-07-27T00:58:18Z  ## Languages  - AppleScript - C - C++ - CMake - CSS - Emacs Lisp - JavaScript - Perl - Python - Roff - Ruby - Shell  ## Topics  - compiler - himitsushell - linux - llvm - musl - obfuscator - obfuscator-llvm - security  ## Top Contributors  - MushStory (10 contributions)  ---  ## README  ## HimitsuObfuscator A lightweight LLVM-17 obfuscator for any Linux.   Block Flow Graph (Ghidra)  ## Usage ```shell # download and extract obfuscator curl -LO https://github.com/HimitsuShell/HimitsuObfuscator/releases/download/v1.2.0_0/himitsu_obfuscator_v1.2.0_0.tar tar -xvf himitsu_obfuscator_v1.2.0_0.tar  vim main.c ----------------------------- #include <stdio.h> int main() {   printf("Hello World!\n");   return 0; } -----------------------------  # builds a binary that runs on any linux (static musl) sudo apt-get install -y build-essential ./compiler/bin/x86_64-unknown-linux-musl-clang -flto -fuse-ld=lld -mllvm -sobf -mllvm -sub -static main.c -o main ./main ```  ### Obfuscation Optio…
