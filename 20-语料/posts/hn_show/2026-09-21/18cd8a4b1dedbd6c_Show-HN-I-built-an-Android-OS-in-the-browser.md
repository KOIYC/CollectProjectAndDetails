---
type: "corpus"
item_id: "18cd8a4b1dedbd6c"
title: "Show HN: I built an Android OS in the browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48332983"
project_url: "https://mobilegym.dev/"
author: "haozaz"
published_at: "2026-05-30T05:40:24Z"
captured_at: "2026-09-21T02:52:54+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_haozaz
  - story_48332983
  - show_hn
metrics: {"points": 28, "comments": 7, "engagement_velocity": 28}
comments_count: 7
comments_total: 7
discovered_via: "hn:show_hn:144d"
---

# Show HN: I built an Android OS in the browser

> [!info] 一句话导读
> Back Swipe in from left or right edge

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48332983>
> 指标：点赞=28 · 评论=7 · engagement_velocity=28
> 作者：haozaz　|　发布：2026-05-30T05:40:24Z
> 项目链接：<https://mobilegym.dev/>
> 采集：2026-09-21T02:52:54+08:00　|　id：`18cd8a4b1dedbd6c`

## 正文

Skip to paper
MobileGym
 Live demo
EN
arXiv
Star
Power off
Click to start
State Builder
中
Gestures
 or click
Back Swipe in from left or right edge
Home Swipe up from bottom edge
Recents Swipe up & hold mid-screen
Switch pages Swipe or drag horizontally on the desktop
Step 0
 idle
Retry
0 steps
State Builder · Live Injection
Patch runtime state without restarting the device
Snapshot · time-travel · inject cross-app data while the simulator keeps running.
Session
Language
Device
WeChat
Alipay
SMS
12306
Weather
Reset
 Save
 Restore
Reset clears the simulator and reloads a fresh session. Saved snapshots stay in this browser.
Reset simulator
Snapshot name
Save snapshot
Snapshot
 No snapshots yet
Restore snapshot
 Delete snapshot
Sets the simulated phone's language. Also clears per-app overrides (Alipay, Bilibili, RedBook, Map) so every app follows the new system locale.
中文
 Simplified Chinese
English
 United States
Apply language
Time
 Battery
 Location
Mode
Real
 Simulated
Flow
 Flow
Device time
Apply time
Battery
Status
Unplugged
 Charging
 Fast charge
Battery saver
Off
 On
Apply battery
Preset
Beijing
 Shanghai
 Guangzhou
 Shenzhen
 Hangzhou
 Chengdu
 Wuhan
 Nanjing
 New York
 London
 Tokyo
 Custom coordinates
Latitude
Longitude
Apply location
Message
 Contact
Chat
 陈静
Message time
Incoming message
 今晚 7 点开会，记得带材料。
Insert message
New contact
WeChat ID
Avatar
Signature
Add contact
Balance
 Bill
Account balance
Set balance
Bill amount
Type
Expense
 Income
Bill title
Note
Add bill
Contact
 SMS
Contact name
Phone
Save contact
SMS sender
Message content
 您的验证码是 482913，用于 MobileGym 场景演示，请勿泄露。
Receive SMS
Ticket order
Train
Status
Paid
 Unpaid
 Cancelled
From station
To station
Date
Depart
Arrive
Passenger
Price
Seat type
商务座
 一等座
 二等座
 高级软卧
 软卧
 硬卧
 软座
 硬座
 无座
Seat
Add ticket/order
Conditions
Patches the located page's current weather. Switch city via the Device → Location panel.
Condition
晴 (Sunny)
 多云 (Partly cloudy)
 阴 (Overcast)
 小雨 (Light rain)
 大雨 (Heavy rain)
 雷阵雨 (Thunderstorm)
 小雪 (Light snow)
 雾 (Fog)
 霾 (Haze)
Temp °C
High °C
Low °C
AQI (0–500)
Apply weather
Power on the phone, then apply a scenario.
One setState patch per action · persists across reloads
Scroll to read paper
Live Agent AI Agent
 Type a task, then Run.
Run
 Stop
WeChat · Boss
 Bilibili · Like Video
Model & agent
Use the built-in demo model, or connect your own OpenAI-compatible vision endpoint.
Agent
Endpoint
 Base URL
 Model
 API key
Parameters
Save
 Reset
Paper · 2026
MobileGym : A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research
Dingbang Wu 1,* ,
 Rui Hao 1,* ,
 Haiyang Wang 2 ,
 Shuzhe Wu ,
 Han Xiao 3 ,
 Zhenghong Li 1 ,
 Bojiang Zhou 1 ,
 Zheng Ju 1 ,
 Zichen Liu 1 ,
 Lue Fan 1,†,‡ ,
 Zhaoxiang Zhang 1,†
1 Institute of Automation, Chinese Academy of Sciences ·
 2 Peking University ·
 3 The Chinese University of Hong Kong
[email protected] ,
 [email protected]
* Equal contribution.
 † Corresponding authors.
 ‡ Project lead.
arXiv
Code
BibTeX
Live demo
TL;DR
MobileGym is a verifiable and highly parallel simulation platform for mobile GUI agent research — the first to make online RL training and deterministic evaluation feasible on real-world daily apps , long a structural blind spot of real-device pipelines. It covers 28 mobile apps (12 daily + 16 system) in the browser. Across the released validation suite, programmatic state judges show no false accept/reject cases over 416 parameterized task templates (vs. 10.2% misjudgment when the same real-device trajectories are scored by a VLM), giving a clean RL reward signal; structured state replication (∼400 MB per browser instance) makes single-machine batch-parallel GRPO cheap. Sim-to-Real : GRPO fine-tuning of Qwen3-VL-4B lifts overall simulation SR by +12.8 pt (9.4%→22.2%); on the 59-task real-device-runnable signal-bucket subset, the +42.8 pt simulation gain is preserved as +40.7 pt on the real device — 95.1% retention .
28
Apps simulated
 12 daily + 16 system
416
Parameterized task templates
 256 test + 160 train
0
False accept/reject
 released checks vs. 10.2% VLM judge error
+40.7 pt
Real-device gain
 Qwen3-VL-4B trained on sim
Inside the Sandbox: 28 Apps
Each app is a faithful in-browser re-implementation in React/TypeScript, with Android-style task stacks, Intent routing, ContentProviders, and permission flows. Hover a row to pause.
Daily
 12
WeChat
Alipay
RedNote
Bilibili
Railway
Maps
Reddit
X
Spotify
eBay
WeRead
Meeting
WeChat
Alipay
RedNote
Bilibili
Railway
Maps
Reddit
X
Spotify
eBay
WeRead
Meeting
System
 16
Launcher
Settings
Phone
Messages
Calendar
Clock
Weather
Gallery
Calculator
Calc (AOSP)
Compass
Notes
Files
Themes
Browser
AnswerSheet
Launcher
Settings
Phone
Messages
Calendar
Clock
Weather
Gallery
Calculator
Calc (AOSP)
Compass
Notes
Files
Themes
Browser
AnswerSheet
All registered via manifest auto-discovery — adding a new app needs zero changes to the OS or benchmark layer. ~3–4 person-days per daily app, <1 day per system app.
Why daily apps stay out of reach
Real-world apps are
 unreadable ,
 unresettable ,
 and unforgiving .
That's why benchmarks quietly avoid WeChat, Alipay, and 12306 — and why online RL on the apps users actually live in has barely been attempted at scale. Three structural walls in the real-device pipeline:
01
Can't read it
The screen is a summary, not the record
Did the transfer go to the right "Mom" — or the other contact with the same nickname? Did the cart settle on the SKU the user wanted, or the lookalike variant? Is the post actually live on the server, or stuck as a local draft? adb and the accessibility tree see what's on screen — never the encrypted DBs, in-memory caches, or server records behind it.
VLM fallback
 10.2% misjudgment
02
Can't reset it
No way back to step zero
Task state lives in encrypted local DBs, in-memory caches, and the cloud. AVD file snapshots reach none of it. GRPO needs N rollouts from one identical state — impossible if you can't restore it even once.
No parallel rollouts
03
Can't undo it
Actions touch the real world
A transfer moves real money. Account deletion is permanent. A "test" message reaches a real friend. You can't roll a real device through millions of training trajectories — at any price.
Payment · ticketing skipped
And it gets worse. GUI agents — and the VLM judges that grade them — observe the world as discrete screenshots sampled at intervals, not continuous video. A success toast captured at exactly the wrong frame turns a failed transfer into a passing test; a half-rendered loading spinner can swing the verdict either way. The screen isn't just a summary — it's an unreliable witness .
One Mechanism, Three Answers
MobileGym answers all three with the same primitive: the entire environment is structured JSON . State is
 readable (judges inspect the structure directly — no VLM, no screenshots),
 writable (snapshot, fork, and restore in milliseconds; hundreds of identical rollouts on one machine), and
 consequence-free (every transfer, deletion, and purchase lives in a sandbox). Payment, ticketing, and account management — long skipped by real-device pipelines — become benchmarkable and trainable.
System Architecture
The whole stack runs in a single browser tab on top of React + TypeScript + Vite. The figure below shows what MobileGym covers and how each phone view is produced.
Headline Results
Leaderboard on MobileGym-Bench (test set, 256 tasks)
We evaluate 9 representative agents on the test set. L1-L4 are diagnostic strata calibrated jointly on the reference panel's mean SR and PR; L1 is relatively saturated, while L4 captures frontier-level tasks. SR is overall Success Rate.
Model
 L1
 (20)
 L2
 (73)
 L3
 (83)
 L4
 (80)
 SR
Proprietary models
Gemini 3.1 Pro
 97.5
 83.6
 63.3
 21.9
58.8
Doubao-Seed-2.0-Pro
 100.0
 93.2
 48.2
 6.2
52.0
Qwen3.6-Plus
 100.0
 78.1
 44.6
 3.8
45.7
Open-source GUI-specialized models
AutoGLM-Phone-9B
 86.2
 33.6
 9.6
 1.9
20.0
UI-TARS-1.5-7B
 77.5
 21.9
 3.0
 1.6
13.8
UI-Venus-1.5-8B
 85.0
 21.9
 6.0
 1.9
15.4
GUI-Owl-1.5-8B-Think
 76.2
 26.0
 4.2
 1.2
15.1
Step-GUI-4B
 83.8
 17.8
 2.4
 1.6
12.9
Open-source generalist models
Qwen3-VL-4B
 71.2
 12.3
 0.6
 0.3
9.4
Even Gemini 3.1 Pro reaches only 21.9 on L4, indicating substantial remaining headroom for future mobile GUI agents. Difficulty bins are calibrated jointly on the reference panel's mean SR and PR; calibration excludes Qwen3-VL-4B and its fine-tuned variants.
Sim-to-Real Transfer: +42.8 pt → +40.7 pt
Reinforcement-fine-tuning Qwen3-VL-4B with GRPO on a single 3×RTX Pro 6000 node (10 training steps, 96 parallel browser instances) lifts overall simulation SR from 9.4% → 22.2% (+12.8 pt). On the 59-task real-device-runnable signal-bucket subset, simulation SR rises from 33.9% → 76.7% (+42.8 pt) and the real-device pass rate rises from 32.2% → 72.9% (+40.7 pt) — a 95.1% retention of the simulation gain:
Bucket
 n
 Base
 Trained (after GRPO)
Sim
 Real
 Sim
 Real
Uplift
 23
 2.2%
 17.4%
 80.7%
 73.9%
Stable-pass
 18
 95.8%
 61.1%
 95.8%
 94.4%
Mid
 18
 12.5%
 22.2%
 52.6%
 50.0%
Total
 59
 33.9%
 32.2%
 76.7%
 72.9%
Δ retention sim → real: 95.1% — gains preserved on real device
The gains are not only aggregate: the trained model also recovers from an out-of-distribution real-device constraint. On Reddit_CreatePostToCommunity , the real-device community requires a flair tag on every post — a constraint the simulator does not enforce . The base model loops on a greyed-out "Post" button for the full 60-step budget; the trained model, after two failed clicks, notices the asterisk on the flair selector, picks a flair, and submits successfully.
Base
Trained
The flair-required behavior is unique to the real-device community and is absent from the simulator's training distribution. Recovery is driven by visual reasoning over the greyed button + asterisk cue, a concrete example of the behavior that online RL on a controllable substrate can induce. Full trace and verbatim think-trace in the paper appendix.
Order-of-Magnitude Efficiency
Single-instance, headless, measured against a Docker AndroidWorld setup (no KVM). MobileGym uses roughly one-tenth the memory and less than one-hundredth the disk footprint of the emulator baseline. Its structured JSON state can be restored and forked directly, which enables GRPO-style same-initial-state parallel sampling at single-machine scale.
Memory / instance
∼400 MB
 vs
 ∼4.5 GB
~11×
lighter
Disk footprint
∼50 MB
 vs
 ∼20 GB
~400×
smaller
Cold start
∼3 s
 vs
 ∼78 s
~26×
faster
Headless / single instance, measured against Docker AndroidWorld (no KVM); see paper Appendix for measurement details.
Citation
@misc{wu2026mobilegymverifiablehighlyparallel,
 title={MobileGym: A Verifiable and Highly Parallel Simulation Platform for Mobile GUI Agent Research},
 author={Dingbang Wu and Rui Hao and Haiyang Wang and Shuzhe Wu and Han Xiao and Zhenghong Li and Bojiang Zhou and Zheng Ju and Zichen Liu and Lue Fan and Zhaoxiang Zhang},
 year={2026},
 eprint={2605.26114},
 archivePrefix={arXiv},
 primaryClass={cs.AI},
 url={https://arxiv.org/abs/2605.26114}
}
 Copy
github.com/Purewhiter/mobilegym
visits: …
Page template by the authors.

## 评论（7/7）

> **haozaz** · 2026-05-31T08:22:31.000Z　
> opensource ： https://github.com/Purewhiter/mobilegym

---

> **haozaz** · 2026-05-31T08:30:03.000Z　
> After burning through tens of billions of tokens, I built an Android-like OS that runs entirely in the browserThe title is a bit clickbaity, but it is not that far from what actually happened.Over the past few months, we built MobileGym: a fully browser-based, Android-like simulation environment implemented in TypeScript + React.It currently includes 28 simulated apps, including WeChat, Alipay, Xiaohongshu/RED, bilibili, X, Reddit, WeChat Read, China Railway 12306, Tencent Meeting, Spotify, and eBay, plus system apps such as Home, Settings, Contacts, Messages, Photos, Calendar, Files, and Browser.The system supports Xiaomi theme packs and custom widgets. We also reimplemented a number of Android-like system mechanisms directly in the browser, including the Activity stack, Intents, gesture navigation, back handling, and soft keyboard behavior.MobileGym was originally built for GUI agent research, but it is also open for anyone who wants to play with it, study Android-like UI/system mechanisms, or fork the code and build something else on top of it.Online demo: https://mobilegym.dev
> GitHub: https://github.com/Purewhiter/mobilegymFeaturesLightweight and highly concurrent
> A single MobileGym instance uses only around 400 MB of memory, compared with roughly 4–10 GB for a typical Android emulator. A single server can run hundreds or even thousands of environment instances in parallel.416 task templates
> The task templates are parameterized, so they can generate an effectively unlimited number of task instances. Evaluation is deterministic and finishes in milliseconds, without relying on LLM-as-a-judge.Sim-to-real transfer that actually works
> In our tests, models trained with GRPO-style reinforcement learning in the simulated environment transferred more than 95% of their gains to real devices.Easy to extend
> MobileGym is designed to be extensible. Adding a new app only requires creating a folder and a manifest file. Adding a new task only requires writing a Python class, and the shortest tasks can be implemented in as little as three lines of code.Fully sandboxed, with no real-world consequences
> MobileGym does not connect to real services, transfer real money, or send real messages. You can safely click around without worrying about side effects.Although the project started as infrastructure for GUI agent training and evaluation, it ended up becoming a fairly complete browser-based Android-like playground.

---

> **dogukan1636** · 2026-05-31T11:04:10.000Z　
> greate job

---

> **matty1911** · 2026-05-31T12:26:36.000Z　
> look nice but why

---

> **haorui123** · 2026-05-31T08:39:46.000Z　
> cool

---

> **haozaz** · 2026-05-31T13:46:07.000Z　
> Thank you!

---

> **haozaz** · 2026-05-31T13:46:13.000Z　
> Thank you!

## 关联链接

- https://arxiv.org/abs/2605.26114}

## 导航

- 项目页：[[10-项目/mobilegym.dev_aa985d6a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
