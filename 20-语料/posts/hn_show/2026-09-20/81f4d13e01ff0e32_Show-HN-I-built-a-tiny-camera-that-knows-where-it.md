---
type: "corpus"
item_id: "81f4d13e01ff0e32"
title: "Show HN: I built a tiny camera that knows where it is"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712254"
project_url: "https://mightycamera.com/story"
author: "asadm"
published_at: "2026-09-15T13:30:14Z"
captured_at: "2026-09-20T14:06:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_asadm
  - story_49712254
  - show_hn
metrics: {"points": 5, "comments": 4, "engagement_velocity": 5}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:90d"
---

# Show HN: I built a tiny camera that knows where it is

> [!info] 一句话导读
> I built a tiny camera that knows where it is

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712254>
> 指标：点赞=5 · 评论=4 · engagement_velocity=5
> 作者：asadm　|　发布：2026-09-15T13:30:14Z
> 项目链接：<https://mightycamera.com/story>
> 采集：2026-09-20T14:06:34+08:00　|　id：`81f4d13e01ff0e32`

## 正文

I built a tiny camera that knows where it is | Mighty

# I built a tiny camera that knows where it is

> Onboard SLAM in a 10g camera. Twenty months from first prototype to shipping hardware.

Asad Memon · October 2024–July 2026 · From first prototypes to Batch 1

The production board: camera, IMU, and compute in one package.

I wanted SLAM for my hobby robot without adding a companion computer. The challenge was fitting visual-inertial odometry and loop closure onto a tiny, low-power camera board—and getting it to run in real time within the available compute and memory.

That became Mighty. It runs the estimation onboard and outputs position and orientation over USB or UART, so even an Arduino-based robot can consume the result. The finished board weighs 10g and produces pose at 20Hz.

My first ESP32 prototype could track image features, but the estimator hit a memory wall. Getting from that prototype to a shipping SLAM camera took twenty months of estimator optimization, hardware revisions, calibration work, and testing.

## Position relative to what?

Mighty estimates motion relative to a local coordinate frame established when tracking starts. It gives your robot a position in meters and an orientation in that frame. It does not give you a latitude and longitude or remember its location across restarts. The pose guide describes the coordinate conventions and output fields.

Visual-inertial odometry, or VIO, combines features tracked through camera images with the IMU's motion measurements. Small errors accumulate along the way. Loop closure recognizes a previously visited place and uses that information to correct the estimated path. It depends on finding a reliable visual match, so a revisit does not guarantee a correction.

The practical goal was to make that estimation the sensor's job. The robot's computer could consume the result and get on with the rest of the robot.

I came into this as a software person. I had never designed a PCB or shipped hardware. I hired help with the PCB design and guided the overall system, learning what I had missed each time another revision arrived.

## The tracker fit. The estimator didn't.

October 2024–March 2025

Uploading a few design files to JLCPCB and getting assembled boards back a couple of weeks later felt like cheating. My first board combined an ESP32-S3, a camera, and an IMU. Then I discovered the reversed camera connector. Getting a board manufactured was easy. Getting the right board manufactured was apparently a separate skill.

Rev0.2 was smaller, and the sensors worked. I could stream images and inertial data over Wi-Fi and start experimenting with the vision code.

I wrote SIMD code to speed up feature tracking and got it to roughly 15 frames per second. That was encouraging: the ESP32 could follow features through an image sequence. But feature tracking was only the front end. The backend still had to turn those observations and the IMU measurements into a motion estimate, and memory became the wall I couldn't get past.

I also missed Linux. Developing and debugging this on ESP-IDF was becoming a substantial part of the work. I went looking for a cheap Linux SoC that would give the estimator room to run.

Rev0.1 · Camera connector, backwards.

Rev0.2 · The sensors worked; memory was the next wall.

## Adding a processor, then deleting one

June–October 2025

Rockchip's RV1103 caught my attention: about $4 a chip at the time, a 1.2GHz Cortex-A7, NEON, and a small NPU. It was in the same price range as an ESP32-S3 module, but offered a Linux environment and a different set of constraints.

NEON mattered immediately. Eigen and OpenCV already supported it, so I could use an existing optimized math stack instead of doing all the low-level work myself. By July, I had the complete VIO pipeline running with a 10fps camera and 200Hz IMU. This time the estimator was running too.

To avoid rewriting the sensor drivers, my first Rockchip board kept the ESP32 as a sensor hub. That saved some software work and gave me a two-processor board to deal with. The following revision removed the ESP32: Rockchip, camera, IMU.

There were less architectural lessons along the way. The oscillator on one revision didn't work, and we had to rework the board with an active replacement. I had not known that oscillator tuning was about to become my problem. Hardware was very good at assigning me new subjects to learn.

By October, the optimized VIO was running at roughly 15Hz on the single ARMv7 core. The NPU would come into the later place-recognition experiment; the core motion estimator ran on the CPU.

Getting the estimator to run in real time meant carefully managing memory and optimizing the visual and inertial processing for the available hardware.

Board revisions along the way, including the move from a separate sensor hub to one processor.

## Coming back to a different starting point

October 2025–February 2026

The board could keep up with me walking around. It could also disagree with me about where the walk ended. Returning to the same physical spot made the accumulated drift very obvious.

I tried loop closure next. A model on the NPU handled place recognition, and I added loop closure and bundle adjustment to correct the path. In November, I could run a few loops around my apartment and watch the corrected trajectory return toward the starting point.

The clips below show those two stages. In the first, watch the accumulated drift. In the second, compare the unoptimized trajectory with the corrected one as I revisit a place. It was a working prototype, not a feature that would automatically make it into Batch 1.

October 2025: the on-device VIO keeps up with the walk, but the estimated path accumulates drift.

November 2025 prototype: compare the unoptimized and corrected paths when I revisit the starting area.

I also explored stereo cameras, depth, and a larger Rockchip platform. Each opened up more possibilities, along with more hardware and integration work. By February, I paused that branch and returned to the original goal: a small, inexpensive, low-power VIO board.

That decision narrowed the first release to VIO, calibration, testing, and tooling. Loop closure followed as a beta firmware feature after launch.

## The browser became part of the hardware

December 2025–April 2026

While I was improving tracking, another problem became hard to ignore: someone other than me needed to use the thing. “Power in, pose out” was a poor description if the next instruction was to assemble a development environment.

I wanted to reduce setup friction for users: plug in the board and handle firmware updates and calibration from a browser, without installing a local toolchain. Flashing came first. I wrapped Rockchip's rkdeveloptool in WebAssembly and used WebUSB to flash from Chromium. I also brought ADB into the browser. Together with OTA updates and the calibration workflow, this let users update and calibrate Mighty through the browser.

Calibration needed the same treatment. Camera and IMU measurements have to agree well enough for the estimator to combine them. Kalibr could do the calibration, but setting it up was its own project. I put it behind a guided browser workflow: record the calibration motion, run the calibration, inspect the results.

Finally, Mighty served its own web UI over USB Ethernet. You could see the pose, record a dataset, and change settings from a browser. Those recordings also gave me a way to investigate tracking problems after the original motion was over.

Flashing Rockchip firmware through WebUSB, with rkdeveloptool compiled to WebAssembly.

Recording camera and IMU calibration data through a guided browser workflow for Kalibr.

## One working board wasn't a production process

April–July 2026

The earlier stacked design used an off-the-shelf camera module. Putting the global-shutter sensor directly on the final PCB simplified assembly and reduced cost. I added multi-camera synchronization support and worked on making calibration and QC repeatable across boards.

Testing also left the apartment. I mounted Mighty on a $20 toy drone for a short circular flight in the backyard, with some minimal vibration damping. This took the tracking experiment from handheld walks to a flying platform.

The final PCB integrates the camera sensor directly, simplifying assembly.

Mighty on a $20 toy drone during a short circular flight in the backyard.

For Batch 1, assembly, calibration, QC, and packing became an actual sequence we could repeat. Friends came over to help. After months of revisions and experiments, we were handling boards that were going to leave the room and be used by other people.

Friends helping with Batch 1: assembly, calibration, QC, and packing.

## How well does it work?

The recordings above show development milestones. They are not a ground-truth accuracy benchmark for the current firmware. A corrected path ending near its starting point does not establish that every position along the path was accurate.

| Condition | What to expect |
| --- | --- |
| Normal tracking | 20Hz position and orientation output, using a global-shutter camera and 800Hz IMU. Output rate is separate from position accuracy. |
| Revisiting a place | Beta loop closure can reduce drift after a reliable match. It is disabled by default. |
| Continuously exploring new indoor space | The documented loop-closure history horizon is roughly 20–25 minutes under tested conditions. It varies with scene and motion; revisiting known routes can allow longer sessions. |
| Darkness, blank walls, or motion blur | Too little usable visual detail can interrupt tracking. Applications should monitor VIO state and pose confidence. |
| Strong vibration | Mounting and vibration isolation matter when using the board on a moving platform. See the vibration guide for setup advice. |
| Restarting VIO | A new session starts. Persistent mapping and localization across sessions are planned. |

The loop-closure guide explains its useful horizon and corrections. The pose guide explains when translation is held or unavailable; confidence describes pose usability, not a guarantee of global accuracy. For a vibrating platform, start with the vibration guide.

## Using the board and reading the code

The board includes the camera, IMU, onboard estimator, and its own web UI. The getting-started guide walks through connecting over USB and starting tracking. Browser flashing uses WebUSB in Chromium; the SDK quick starts cover integration into your own application.

The Mighty Protocol repository contains the SDKs, wire protocol, and examples for Python, JavaScript, C++, and ROS 2 under the Apache 2.0 license. That repository covers communication and integration; it does not contain the board's VIO firmware or PCB design files. The story above also relies on tools such as Linux, OpenCV, Eigen, rkdeveloptool, and Kalibr.

Boards are available to order with a currently listed lead time of 1–3 weeks. The product page has the hardware specifications and ordering links for current regional pricing and shipping details.

## Getting Batch 1 out the door

The goal stayed fairly constant. My understanding of the work required to reach it did not. I started by trying to fit an algorithm into a camera. By the time we packed the first batch, I had also learned how much had to fit around it.

Alhamdulillah. I’m grateful for the chance to do this work, for the people who helped get these boards out the door, and for the customers and early supporters who took a chance on Mighty.

The original experiments, failures, and demos are in the engineering logs. For the board itself, see Mighty Camera and the documentation. For questions or project discussions, join us on Discord.

# kottos-ai/llmbridge

## 评论（4/4）

> **drfunk** · 2026-09-15T14:46:17.000Z　
> "The camera knows where it is at all times. It knows this because it knows where it isn't. By subtracting where it is from where it isn't, or where it isn't from where it is (whichever is greater), it obtains a difference, or deviation."

---

> **nicad** · 2026-09-15T19:38:34.000Z　
> This being closed source is sad. I get the aspect of wanting to earn money, but closed source code maintained by a few people at a hobby level puts an upper ceiling of the quality. I would love to buy this if the code was actually open source

---

> **asadm** · 2026-09-15T16:35:48.000Z　
> hah neat reference.

---

> **kaffekaka** · 2026-09-15T19:02:41.000Z　
> This came instantly to the mind.

## 导航

- 项目页：[[10-项目/mightycamera.com_fa72267f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
