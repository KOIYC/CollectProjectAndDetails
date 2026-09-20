---
type: "corpus"
item_id: "f92d0aac5b7fbf6e"
title: "Show HN: Keep Mac awake while your agent works even with screen off, lid closed"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47962415"
project_url: "https://github.com/ObservedObserver/Macchiato"
author: "loa_observer"
published_at: "2026-04-30T13:46:39Z"
captured_at: "2026-09-21T02:52:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_loa_observer
  - story_47962415
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Keep Mac awake while your agent works even with screen off, lid closed

> [!info] 一句话导读
> ObservedObserver/Macchiato

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47962415>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：loa_observer　|　发布：2026-04-30T13:46:39Z
> 项目链接：<https://github.com/ObservedObserver/Macchiato>
> 采集：2026-09-21T02:52:25+08:00　|　id：`f92d0aac5b7fbf6e`

## 正文

# ObservedObserver/Macchiato

Keep your Mac awake while your code agent works — even with screen off, lid closed

- Stars: 26
- Forks: 0
- Watchers: 26
- Open issues: 2
- License: Apache License 2.0
- Default branch: main
- Created: 2026-04-30T13:00:32Z

## Languages

- Shell
- Swift

## Top Contributors

- ObservedObserver (8 contributions)

---

## README

 Macchiato

 A tiny macOS menu bar utility that keeps your Mac awake with one button.

## What It Solves

Mac-chiato is built for people who leave long-running work on their Mac: coding agents, local automation, builds, data jobs, model runs, downloads, and anything else that should keep going while you step away.

screenshot

When you need to close your computer, you should be able to close it normally. No leaving the lid slightly open, no changing system settings by hand, and no wondering whether the agent that was halfway through a task got interrupted.

Macchiato gives you a single menu bar switch:

- **On:** keep the Mac awake, including lid-closed use.
- **Off:** restore normal macOS sleep behavior.

## How To Use

1. Launch **Macchiato**.
2. Click the menu bar icon.
3. Turn on **Keep Awake** before starting or leaving a long-running task.
4. Close the lid whenever you need to move, pause, or put the Mac aside.
5. Turn **Keep Awake** off when you want macOS to sleep normally again.

The first time Macchiato enables lid-closed sleep control, macOS may ask you to approve **Macchiato Helper** in System Settings. After that approval, the regular on/off switch should work without asking for administrator credentials every time.

## Good For

- Agents that continue working while you are away from the keyboard.
- Local development servers, builds, test runs, and scripts.
- Long downloads, syncs, exports, or processing jobs.
- Any moment where you want to close the MacBook without babysitting the lid.

For long sessions, keep an eye on battery and heat, especially if the Mac is closed and not plugged in.

## If Something Goes Wrong

If Macchiato is force-quit or crashes while enabled, you can manually restore normal sleep behavior:

```sh
sudo pmset -a disablesleep 0
```

## Development

Macchiato uses an IOKit `PreventUserIdleSystemSleep` assertion plus macOS' `pmset disablesleep` setting. The app ships a privileged LaunchDaemon helper, installed through `SMAppService`, so the system-level `pmset` work is approved once instead of prompting on every toggle.

Internal distribution uses the project's private signing flow. Release builds must not include debug signing entitlements such as `get-task-allow`, and the app and embedded helper must be signed consistently before packaging the DMG. Users approve/trust the internal build through macOS, then Macchiato registers the helper through `SMAppService`.

Build locally:

```sh
xcodebuild -project Macchiato.xcodeproj -scheme Macchiato -configuration Debug build
```

Build the internal distribution DMG:

```sh
scripts/build-dmg.sh
```

Additional `xcodebuild` build settings can be passed through when needed by the internal signing flow.

The `Macchiato` target depends on `Macchiato Power Helper` and embeds the helper executable plus its launchd plist into:

```text
Macchiato.app/Contents/MacOS/app.macchiato.Macchiato.PowerHelper
Macchiato.app/Contents/Library/LaunchDaemons/app.macchiato.Macchiato.PowerHelper.plist
```

## Verify The Assertion

Launch the app, turn on **Keep Awake**, then run:

```sh
pmset -g assertions | grep Macchiato
```

You should see a `PreventUserIdleSystemSleep` assertion named `Macchiato is keeping your Mac awake`.

You can also verify the lid-closed sleep setting:

```sh
pmset -g live | grep SleepDisabled
```

## Local Sleep Logging Test

The repo includes two local scripts for manual acceptance testing:

```sh
scripts/sleep-log-runner.sh --scenario lid-closed-off
scripts/sleep-log-runner.sh --scenario keep-awake-on
scripts/analyze-sleep-log.sh sleep-test-logs/*.csv
```

Suggested flow:

1. Ensure Macchiato is off, start `scripts/sleep-log-runner.sh --scenario lid-closed-off`, close the lid or otherwise trigger the sleep condition, wait 10 minutes, reopen the Mac, then stop the logger with Ctrl+C.
2. Turn on **Keep Awake**, start `scripts/sleep-log-runner.sh --scenario keep-awake-on`, repeat the 10 minute window, reopen the Mac, then stop the logger.
3. Run `scripts/analyze-sleep-log.sh sleep-test-logs/*.csv`.

The analyzer reports sample count, wall time, maximum timestamp gap, whether the Macchiato power assertion was observed, and how many samples saw `SleepDisabled=1`. A large gap means the logger stopped running during the test window, which usually indicates sleep.

# hwdsl2/docker-ollama

## 导航

- 项目页：[[10-项目/github.com_8f538c72]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
