---
type: "corpus"
item_id: "1e4d2128bd4e6fdb"
title: "zortos293/Lichii"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/zortos293/Lichii"
project_url: "https://github.com/zortos293/Lichii"
author: "zortos293"
published_at: "2026-10-31T14:17:26Z"
captured_at: "2026-11-11T13:39:40+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-11"
pub_day: "2026-10-31"
tags:
  - 语料
  - github_new
  - C++
  - created:>2026-10-28
metrics: {"stars": 8258, "forks": 1334, "open_issues": 644}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# zortos293/Lichii

> [!info] 一句话导读
> SPDX-FileCopyrightText: Copyright 2025 Eden Emulator Project

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/zortos293/Lichii>
> 指标：stars=8258 · forks=1334 · open_issues=644
> 作者：zortos293　|　发布：2026-10-31T14:17:26Z
> 项目链接：<https://github.com/zortos293/Lichii>
> 采集：2026-11-11T13:39:40+08:00　|　id：`1e4d2128bd4e6fdb`

## 正文

<!--
# SPDX-FileCopyrightText: Copyright 2025 Eden Emulator Project
# SPDX-License-Identifier: GPL-3.0-or-later

# SPDX-FileCopyrightText: 2018 yuzu Emulator Project
# SPDX-License-Identifier: GPL-2.0-or-later
-->

⚠️ Lichii has no official website ⚠️

> [!CAUTION]
> **Lichii has no official website.** The only site run by this project is the **game compatibility website, [lichii.zortos.me](https://lichii.zortos.me)**, for compatibility reports only. Download Lichii **only** from this repository's [releases page](https://github.com/zortos293/Lichii/releases). Any other "Lichii" website or download (such as lichii.org) is not ours and may contain malware ([#545](https://github.com/zortos293/Lichii/issues/545)).

# Lichii

Lichii is an experimental, open-source Nintendo Switch and Switch 2 emulator written in C++. It builds on Eglantine, Eden, yuzu and Sudachi, preserving their contributions while developing this fork's game compatibility and renderer fixes.

This is an independent fork, not an official release of those upstream projects. Lichii is not affiliated with Nintendo.

Visit the [Lichii game compatibility website](https://lichii.zortos.me) to find games and compare community compatibility reports.

## Downloads and setup

Download Lichii only from this repository's [releases page](https://github.com/zortos293/Lichii/releases). Lichii has no other download site: archives offered elsewhere, such as lichii.org, are not built by this project, and one has been reported to install malware ([#545](https://github.com/zortos293/Lichii/issues/545)).

On Windows, extract the entire build archive and run **lichii.exe**. Only use games and system files you have legally obtained. Games, keys and firmware are not included.

### Existing saves and settings

Lichii uses its own profile: `%APPDATA%\lichii` on Windows, and the `lichii` directories under `$XDG_DATA_HOME`, `$XDG_CONFIG_HOME` and `$XDG_CACHE_HOME` on Linux and macOS. Without XDG overrides, these are `~/.local/share/lichii`, `~/.config/lichii` and `~/.cache/lichii`. An existing portable `user/` directory still takes priority and is not imported or changed by the wizard.

On the first non-portable GUI launch, Lichii offers to import Eden and other detected emulator profiles. Back up `%APPDATA%\eden` first on Windows, or the old data, config and cache directories on Unix, and close the source emulator. Choose **Keep Old Data** to copy without changing the source, then check your saves and relaunch. Existing destination data is retained in backup directories rather than merged. Move also retains a source backup until you remove it yourself; Link deliberately shares settings and saves. Paths outside the imported data root remain shared and unchanged. An interrupted import offers recovery on the next launch. `eden-cli`, including `--help` and `--version`, refuses to initialize configuration until you import or explicitly choose **Start fresh** in the GUI.

## Compatibility and issue reports

Compatibility and performance vary by game, hardware and driver. Rendering errors, stutters and crashes remain possible. Passing automated tests does not establish that a game renders correctly, and this project makes no universal frame-rate guarantee.

Browse [community compatibility reports](https://lichii.zortos.me/reports) for results with each player's build and setup.

Desktop reporting requires a build containing [PR #303](https://github.com/zortos293/Lichii/pull/303) and is not available in build 88. In builds that include it, play and stop a Switch 2 game, then right-click that game and choose **Submit compatibility report**. Only the latest session in the current Lichii process is eligible.

Confirm the matching website catalog entry and review the editable machine, game, setup, and enabled add-on details prefilled where available. Check the public preview and give explicit consent before submitting. Nothing uploads automatically, and the native v1 reporter does not read or upload logs or files.

When [reporting an issue](https://github.com/zortos293/Eglantine/issues), include:

- The exact build, game version, CPU, GPU and driver version.
- Relevant settings and steps to reproduce the problem.
- A screenshot and the log from the affected session, after checking it for personal information.

Do not upload game files, keys, firmware or private account information.

## Building and contributing

See the [build guide](docs/Build.md), [user documentation](docs/user/README.md) and [coding guidelines](docs/Coding.md). Some inherited documentation and internal build target names still use upstream names. The GUI build target remains `yuzu`; its output is `lichii.exe` on Windows and `lichii` on other desktop platforms.

Keep changes focused and distinguish code-level checks from actual gameplay testing.

## Artwork
Art created by YOB (yobslab)
The supplied Lichii logo, icon and library artwork are in [dist/branding](dist/branding). Windows, Linux and macOS icon resources are generated from that artwork by [Generate-LichiiIcons.ps1](tools/Generate-LichiiIcons.ps1).

## Support Lichii

Lichii is free and stays free. If you want to help, you can donate in crypto. Donations help pay for the AI tools and build machines used to develop this open-source project faster.

**Solana (SOL)**
```text
JepEjfyWjGjhJvHSrqj52KtLjcbbbmUh1iGqerYBF4w
```

**Ethereum (ETH)**
```text
0x055ABa1b80Bc35C836Ce7E9F47c2b3d6C75b5534
```

**Bitcoin (BTC)**
```text
bc1qcvxdpf4qvdhqp8ee4s355cjmxrzsphsdwpl8w4
```

**BNB Smart Chain (BNB)**
```text
0x055ABa1b80Bc35C836Ce7E9F47c2b3d6C75b5534
```

**Polygon**
```text
0x055ABa1b80Bc35C836Ce7E9F47c2b3d6C75b5534
```

Send each coin on its matching network. Coins sent on the wrong network can't be recovered.

> [!NOTE]
> Donations are voluntary gifts and are non-refundable. A donation does not buy any product, service, perk, early access, exclusive build, priority support or say in the project. Every release stays free and public for everyone.

## Credits and license

Lichii inherits the work of the Eglantine, Eden, yuzu and Sudachi projects and their contributors, including Eglantine's original developer Camille LaVey. Original copyright notices and third-party licenses are retained.

See [LICENSE.txt](LICENSE.txt) and the source files for applicable license terms.

## 关联链接

- https://github.com/zortos293/Eglantine/issues
- https://github.com/zortos293/Lichii/issues/545
- https://github.com/zortos293/Lichii/pull/303
- https://github.com/zortos293/Lichii/releases
- https://lichii.zortos.me
- https://lichii.zortos.me/reports

## 导航

- 项目页：[[10-项目/github.com_1e4d2128]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
