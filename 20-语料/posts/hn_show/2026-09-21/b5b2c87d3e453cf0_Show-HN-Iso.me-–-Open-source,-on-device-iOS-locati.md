---
type: "corpus"
item_id: "b5b2c87d3e453cf0"
title: "Show HN: Iso.me – Open-source, on-device iOS location tracker"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47963067"
project_url: "https://github.com/CodyBontecou/isome"
author: "codybontecou"
published_at: "2026-04-30T14:29:00Z"
captured_at: "2026-09-21T02:52:24+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_codybontecou
  - story_47963067
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Iso.me – Open-source, on-device iOS location tracker

> [!info] 一句话导读
> Source code of the iso.me iOS app

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47963067>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：codybontecou　|　发布：2026-04-30T14:29:00Z
> 项目链接：<https://github.com/CodyBontecou/isome>
> 采集：2026-09-21T02:52:24+08:00　|　id：`b5b2c87d3e453cf0`

## 正文

# CodyBontecou/isome

Source code of the iso.me iOS app

- Stars: 17
- Forks: 5
- Watchers: 17
- Open issues: 5
- License: GNU Affero General Public License v3.0
- Homepage: https://apps.apple.com/us/app/iso-me/id6761960794
- Default branch: main
- Created: 2025-12-29T03:01:23Z

## Languages

- HTML
- JavaScript
- Python
- Shell
- Swift
- TypeScript

## Top Contributors

- CodyBontecou (141 contributions)

---

## README

# iso.me

> **Open source, privacy-first iOS location tracking — your data stays on your device.**

License: AGPL v3
Platform
Swift

iso.me is a location tracking app for iOS and watchOS. It automatically records the places you visit throughout the day, tracks routes with continuous GPS logging, and **keeps every byte of your data on-device**. No accounts. No cloud sync. No third-party dependencies. No analytics. Just you, your phone, and your history.

**🌐 isome.isolated.tech** · **📲 Download on the App Store** · **🛠 Contribute** · **💬 Discussions** · **👥 Discord** · **⭐ Star this repo**

## Screenshots

| Capture every visit | Keep it on-device | Export your history |
|---|---|---|
| Map view with visit pins | Settings showing on-device tracking | Export format picker — JSON, CSV, Markdown |

## Features

### Visit Detection
Automatic background detection of places you arrive at and depart from, powered by `CLLocationManager` visit monitoring. Each visit is reverse-geocoded to show a human-readable address and location name.

### Continuous Tracking
High-accuracy GPS tracking that records your exact path. Configurable distance filter (5m-200m) and auto-off timer (30 min to never). Tracked points include altitude, speed, and accuracy metadata.

### Live Activities
Real-time tracking status on the lock screen and Dynamic Island. Shows current location, distance traveled, points recorded, and remaining auto-off time.

### Export & Import
Export visits and location points as JSON, CSV, or Markdown. Choose a date range, time-of-day window, and per-format field toggles, and either condense everything into a single file or split the export into **one file per day** for easier downstream slicing. Customize filenames and dated subfolders with tokens (for example, Markdown can use `{year}/{year}-{month}/Daily Track - {date}.md`). Optionally set a default export folder for one-tap saves and schedule a daily auto-export. Scheduled exports use a routing-only APNs worker to wake the app near your selected time; your location records, files, folder paths, and filename templates stay on-device. Import previously exported data back into the app. Export is the one paid feature — see Pricing.

Exports drop in cleanly to the iso.me Maps Obsidian plugin, which renders visits, routes, heatmaps, and outliers as Leaflet maps inline in your notes — point a code block at a single condensed export, a folder of per-day files, or a filename glob.

### Watch App
Companion watchOS app showing today's visit count, distance traveled, and tracking status. Syncs with the main app via shared App Groups.

### Widgets
iOS lock screen widget via Live Activities and watchOS complications for quick tracking status.

## Pricing

Tracking is free and unlimited — visits, continuous routes, watch app, Live Activities, widgets. No subscription, no ads, no usage caps.

The one paid feature is **export**: a one-time **$9.99** unlock for JSON, CSV, and Markdown export of your visits and location points. Lifetime, no recurring charge.

The split is on purpose: tracking is the commodity, but a clean, lossless export of your full history is the part that's worth paying for once. It also keeps the privacy promise free at the door — you never have to pay to keep your data on your device.

## Tech Stack

- **Language:** Swift 5
- **UI:** SwiftUI
- **Data:** SwiftData
- **Minimum iOS:** 17.0
- **Minimum watchOS:** 10.0
- **Dependencies:** None (all native Apple frameworks)

### Frameworks Used

| Framework | Purpose |
|-----------|---------|
| CoreLocation | Visit monitoring, GPS tracking, geocoding |
| CoreMotion | Activity detection (driving, walking, cycling) |
| SwiftData | On-device persistence for visits and location points |
| ActivityKit | Live Activities on lock screen and Dynamic Island |
| WidgetKit | Home screen and watch widgets |
| StoreKit 2 | In-app purchase (lifetime unlock) |
| MapKit | Map visualization and route display |
| Combine | Reactive state management |

## Project Structure

```
IsoMe/
  Models/
    Visit.swift                    # Visit data model (coordinates, times, address)
    LocationPoint.swift            # Continuous tracking point model
    LocationActivityAttributes.swift  # Live Activity state
  Services/
    LocationManager.swift          # Core location tracking logic
    ActivityDetectionManager.swift # CoreMotion activity detection
    LiveActivityManager.swift      # Live Activity lifecycle
    GeocodingService.swift         # Reverse geocoding with caching
    StoreManager.swift             # In-app purchase management
    LogManager.swift               # Crash and debug logging
  ViewModels/
    LocationViewModel.swift        # Data coordination between UI and services
  Views/
    ContentView.swift              # Root view with onboarding and tab navigation
    TrackingView.swift             # Tracking controls
    MapView.swift                  # Map with visit pins
    SessionPathMapView.swift       # Route path visualization
    SettingsView.swift             # Preferences, export, import, data management
    VisitDetailView.swift          # Individual visit details
    PaywallView.swift              # Pro upgrade screen
    LogViewerView.swift            # Debug log viewer
  Utilities/
    ExportService.swift            # JSON/CSV/Markdown export
    ImportService.swift            # Data import parsing
    ExportFolderManager.swift      # Default export folder management
    DistanceFormatter.swift        # Metric/imperial formatting
    TEDesign.swift                 # Design tokens and typography
  IsoMeApp.swift                   # App entry point
  AppDelegate.swift                # Background launch handling

IsoMeWidget/                       # iOS widget and Live Activity extension
IsoMeWatch/                        # watchOS companion app
IsoMeWatchWidget/                  # watchOS widget extension
Shared/                            # Shared code (App Group data sync)
```

## Build Targets

| Target | Bundle ID | Platform |
|--------|-----------|----------|
| IsoMe | `com.bontecou.isome` | iOS |
| IsoMeWidgetExtension | `com.bontecou.isome.Widget` | iOS |
| IsoMeWatch | `com.bontecou.isome.watchkitapp` | watchOS |
| IsoMeWatchWidgetExtension | `com.bontecou.isome.watchkitapp.Widget` | watchOS |

## Setup

1. Open `IsoMe.xcodeproj` in Xcode 15+
2. Select the **IsoMe** scheme
3. Set your development team for all four targets
4. Configure the App Group entitlement (`group.com.bontecou.isome`) for your team
5. Build and run on a physical device (location features require real hardware)

## Testing

Run the app unit tests with:

```bash
xcodebuild test -project IsoMe.xcodeproj -scheme IsoMe -destination 'platform=iOS Simulator,name=iPhone 17'
```

Export round-trip coverage lives in `IsoMeTests/ExportRoundTripTests.swift`. It uses inline representative visit and route-point fixtures, renders JSON, CSV, Markdown, GeoJSON, GPX, OwnTracks, and Overland through `ExportService.render`, then parses each payload back into normalized records while asserting the emitted schema keys. OwnTracks and Overland are points-only protocols, so their cases verify route points and explicitly assert that visits are not emitted.

### Required Permissions

The app requests the following permissions at runtime:

- **Location (Always)** - Background visit detection and tracking
- **Location (When in Use)** - Foreground location display
- **Motion & Fitness** - Activity detection for auto-start feature

### Entitlements

- App Groups (`group.com.bontecou.isome`) - Shared data between app, widgets, and watch
- Background Modes: Location updates
- Live Activities support

## URL Scheme

The app registers the `isome://` URL scheme. Currently supports:

- `isome://stop` - Stops continuous tracking (used by Live Activity)

## Contributing

Contributions are welcome — bug reports, feature ideas, and pull requests. See CONTRIBUTING.md for the full setup guide (Xcode, signing, TestFlight) and a list of good first issues.

If you want to chat about the project, design decisions, or what to build next, jump into GitHub Discussions.

## License

iso.me is licensed under the GNU Affero General Public License v3.0. The AGPL ensures that any modified version of iso.me — including ones run as a hosted service — must also be open source. This protects the privacy-first promise: nobody can take iso.me, bolt on tracking, and ship it as a closed product.

# srinathsankara/agent-recall-ai

## 关联链接

- https://apps.apple.com/us/app/iso-me/id6761960794

## 导航

- 项目页：[[10-项目/github.com_c1e93160]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
