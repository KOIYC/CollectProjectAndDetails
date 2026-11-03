---
type: "project"
title: "Show HN: Jenesis, Java builds 18% faster, rebuilds up to 88% faster"
project_url: "https://jenesis.build/why/tool"
first_seen: "2026-11-03T09:54:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_raphw
  - story_50340526
  - show_hn
lang: "en"
---

# Show HN: Jenesis, Java builds 18% faster, rebuilds up to 88% faster

> [!info] 一句话导读
> Jenesis - you already wrote the build script

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://jenesis.build/why/tool>
> 首次收录：2026-11-03T09:54:09+08:00
> 来源渠道：HN Show HN
> 标签：author_raphw, story_50340526, show_hn
> 最新指标：点赞=5 · 评论=0 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-03T09:40:36+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-11-03/c1b28be166767cee_Show-HN-Jenesis,-Java-builds-18%-faster,-rebuilds]] |
| 2026-11-03T09:54:09+08:00 | HN Show HN | 点赞=5 · 评论=0 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-11-03/c1b28be166767cee_Show-HN-Jenesis,-Java-builds-18%-faster,-rebuilds]] |

## 摘要正文

Jenesis - you already wrote the build script  # You already wrote the build script.   Java builds have grown verbose. A `pom.xml`, a `build.gradle.kts` or a `BUILD.bazel` restates what the code already says - its name, its dependencies, its main class - and grows a block of configuration for every step beyond the defaults, until the build is a second program to maintain beside the first. Jenesis reads the build from the code instead: `module-info.java` names what the project requires, and its Javadoc carries any metadata. There is nothing else to write, and no build tool to download.   Not moving to modules yet? Jenesis builds the `pom.xml` you already have, on the class path as Maven does, and the speed and the checks come with it: `pin` records the version and SHA-256 checksum of every dependency in a comment of the `pom.xml`, which Maven ignores, and a build that downloads other bytes fails. Every build timed below is built from its `pom.xml`.   module-info.java pom.xml  ``` $ curl -fsSL https://get.jenesis.build | bash $ cat sources/module-info.java /**  * @jenesis.release 25  * @jenesis.main demo.app.Main  */ module demo.app {     requires org.slf4j;     requires com.fasterxml…
