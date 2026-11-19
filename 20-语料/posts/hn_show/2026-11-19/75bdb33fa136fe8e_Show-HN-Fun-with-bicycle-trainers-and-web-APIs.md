---
type: "corpus"
item_id: "75bdb33fa136fe8e"
title: "Show HN: Fun with bicycle trainers and web APIs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50550607"
project_url: "https://joelriley.com/fun-with-trainers"
author: "okayestjoel"
published_at: "2026-11-18T19:05:49Z"
captured_at: "2026-11-19T09:56:08+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_okayestjoel
  - story_50550607
  - show_hn
metrics: {"points": 7, "comments": 3, "engagement_velocity": 7}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Fun with bicycle trainers and web APIs

> [!info] 一句话导读
> a personal webpage of little consequence

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50550607>
> 指标：点赞=7 · 评论=3 · engagement_velocity=7
> 作者：okayestjoel　|　发布：2026-11-18T19:05:49Z
> 项目链接：<https://joelriley.com/fun-with-trainers>
> 采集：2026-11-19T09:56:08+08:00　|　id：`75bdb33fa136fe8e`

## 正文

Joel Riley
a personal webpage of little consequence
Fun with bicycle trainers and web APIs
November 18, 2026
Try the web app: YouTube Hamster Wheel
I'm a casual cyclist, though on days when the weather is poor, I use my indoor bicycle smart trainer, a Wahoo Kickr Core. It works well enough when paired with an app like Zwift. Zwift lets you go on virtual rides, measuring your speed based on trainer power output.
Unfortunately for a casual cyclist and an even less frequent trainer user, the Zwift $20/month subscription requirement is a steep ask. This got me thinking, could we create a simple web app that connects to the Wahoo device that gamifies the experience without the steep prices?
The Wahoo Kickr Core, like many smart trainers, conforms to the Cycling Power Service Bluetooth specification. Paired with the Web Bluetooth API , you can make simple web apps to create interesting experiences with your trainer.
Simplified TypeScript code to connect to a smart trainer and calculate speed and distance.
const CYCLING_POWER_SERVICE = 0x1818 ;
 const CYCLING_POWER_MEASUREMENT = 0x2a63 ;
 const wheelCircumferenceM = 2.105 ; // 700x25c tire
let prevWheelRevs : number | null = null ;
 let prevWheelTime : number | null = null ;
const device = await navigator . bluetooth . requestDevice ( {
 filters : [ { services : [ CYCLING_POWER_SERVICE ] } ] ,
 } ) ;
 const server = await device . gatt . connect ( ) ;
 const service = await server . getPrimaryService ( CYCLING_POWER_SERVICE ) ;
const measurement = await service . getCharacteristic ( CYCLING_POWER_MEASUREMENT ) ;
 await measurement . startNotifications ( ) ;
measurement . addEventListener ( 'characteristicvaluechanged' , ( event : Event ) => {
 const value = ( event . target as BluetoothRemoteGATTCharacteristic ) . value ;
 const flags = value . getUint16 ( 0 , true ) ;
// Read values specified in section 3.75 in the GATT Specification Supplement.
 const powerW = Math . max ( 0 , value . getInt16 ( 2 , true ) ) ;
let offset = 4 ;
 // Skip pedal power balance and accumulated torque fields
 if ( flags & 0x01 ) offset += 1 ;
 if ( flags & 0x04 ) offset += 2 ;
if ( flags & 0x10 ) {
 // Wheel Revolution Data is a struct
 const wheelRevs = value . getUint32 ( offset , true ) ;
 const wheelTime = value . getUint16 ( offset + 4 , true ) ;
// Skip the first reading, and repeats of the same event time while the wheel is stopped
 if ( prevWheelRevs !== null && prevWheelTime !== null && wheelTime !== prevWheelTime ) {
 // Wheel event time is in 1/2048s units
 let timeDelta = wheelTime - prevWheelTime ;
 if ( timeDelta < 0 ) timeDelta += 65536 ; // Account for uint16 wrapping
 // Cumulative wheel revolutions never roll over, but can decrease (e.g. reset by another app)
 const revsDelta = Math . max ( 0 , wheelRevs - prevWheelRevs ) ;
// Calculate distance and speed based on wheel circumference and revolutions over time
 const distanceM = revsDelta * wheelCircumferenceM ;
 const speedKph = ( distanceM / ( timeDelta / 2048 ) ) * 3.6 ;
 }
prevWheelRevs = wheelRevs ;
 prevWheelTime = wheelTime ;
 }
 } ) ;
 As a proof of concept, I created the YouTube Hamster Wheel , a simple web app that connects to a smart trainer with the Web Bluetooth API, and uses its calculated speed to "power" a YouTube video; the faster you pedal, the faster the YouTube video plays. Pedal too slow, and the video plays in slow motion, and pedal faster than your target speed and the video will start playing at higher and higher speeds.
A major limitation of the Web Bluetooth API: it only works on Chromium-based browsers , no Safari or Firefox. This eliminates iPads as a possibility, which are probably the most common screen/device to pair with a smart trainer. In my setup, I use a Samsung Galaxy Tab S7+ tablet, which serves as the control interface, which then mirrors to an external monitor to provide a larger display.
It's a simple idea, but it is surprisingly effective for short exercise sessions, where I can cycle for 15-20 minutes while watching YouTube videos I would otherwise feel guilty wasting my time with.
You can play around with the experiment at YouTube Hamster Wheel . Note, I have only tested on my Wahoo Kickr Core (old version), so no guarantees it works for anything else.
← Back to all posts
© Joel Riley
This site does not collect personal information or use cookies.
Plausible, a privacy-friendly tracking tool, is used to monitor general website traffic.

## 评论（3/3）

> **dieselgate** · 2026-11-18T21:39:56.000Z　
> Is anyone able to explain the cycling power service and other vars? It equals “0x1818” and I’m trying to understand what these mean. Did a web search for this value and a separate site (0) shows up talking about crank/power values. Is this part of a larger standardized unit system?
> The partial conclusion I’ve arrived at is these are unsigned 16 bit values in hex form but unsure if this is accurate.(0) https://devzone.nordicsemi.com/f/nordic-q-a/9479/cumulative-...

---

> **okayestjoel** · 2026-11-18T21:59:25.000Z　
> You can find the 0x1818 identifier in the Bluetooth Assigned Numbers Document, along with other services:
> https://www.bluetooth.com/specifications/assigned-numbers/The GATT Specification Supplement (3.75) contains details on the data format:
> https://btprodspecificationrefs.blob.core.windows.net/gatt-s...I have a pretty narrow understanding of the Bluetooth spec as a whole, though hopefully that sheds some light on this specific use.

---

> **dieselgate** · 2026-11-18T22:10:31.000Z　
> That's incredibly interesting and glad I asked, thanks for the response.
> Edit: the hamster video is additionally great!

## 导航

- 项目页：[[10-项目/joelriley.com_96922dad]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
