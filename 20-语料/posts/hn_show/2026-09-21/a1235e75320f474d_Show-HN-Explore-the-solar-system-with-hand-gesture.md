---
type: "corpus"
item_id: "a1235e75320f474d"
title: "Show HN: Explore the solar system with hand gestures in a browser"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49496660"
project_url: "https://github.com/HUANGCHIHHUNGLeo/solar-atlas-gesture"
author: "cortexosmain"
published_at: "2026-08-30T07:58:09Z"
captured_at: "2026-09-21T03:11:33+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_cortexosmain
  - story_49496660
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Explore the solar system with hand gestures in a browser

> [!info] 一句话导读
> HUANGCHIHHUNGLeo/solar-atlas-gesture

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49496660>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：cortexosmain　|　发布：2026-08-30T07:58:09Z
> 项目链接：<https://github.com/HUANGCHIHHUNGLeo/solar-atlas-gesture>
> 采集：2026-09-21T03:11:33+08:00　|　id：`a1235e75320f474d`

## 正文

# HUANGCHIHHUNGLeo/solar-atlas-gesture

Explore the Solar System with hand gestures in your browser. MediaPipe hand tracking + Three.js, NASA data, bilingual EN/中文. The gesture layer still has real problems — help optimize it.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-08-30T01:22:09Z

## Languages

- HTML

## Top Contributors

- HUANGCHIHHUNGLeo (2 contributions)

---

## README

# Solar Atlas — Gesture-Controlled Solar System
# 太陽系手勢資料庫

Explore the Solar System — and the scales beyond it — by waving your hand in front of your webcam. No controller, no mouse required: an open palm swipe spins the view, a pinch zooms, and pointing at a planet flies you there and opens its NASA data card.

用鏡頭捕捉手部動作，撥動、捏合就能探索太陽系與更大尺度的宇宙。不用滑鼠、不用手把：張開手掌撥動＝轉視角，捏合＝縮放，指向天體＝飛過去讀它的 NASA 資料卡。

Everything runs in the browser. No server, no build step, no data leaves your machine — the camera stream is processed locally by MediaPipe and never uploaded.

全部在瀏覽器裡跑。沒有後端、不用編譯，影像完全在本機由 MediaPipe 處理，不會上傳到任何地方。

---

## Why this exists / 為什麼做這個

**The goal is simple: let people get to know the planets by pushing them around with their hands.** Reading a table of orbital periods is forgettable. Spinning Saturn with your palm, pinching until the whole Solar System collapses into one dot among the nearby stars, and then flying into the TRAPPIST-1 system — that sticks.

**目的很單純：讓人可以透過撥動去認識太陽系的行星。** 看一張公轉週期表很快就忘了；但用手掌把土星轉起來、捏合到整個太陽系縮成鄰近恆星裡的一個點、再飛進 TRAPPIST-1 星系——這個會記得住。

**But the gesture control still has a lot of technical problems, and that is exactly why this is open source. I would like everyone to think about it together and help make it better.**

**但手勢控制系統還有許多技術問題，這也正是它開源的原因。希望大家集思廣益，一起把它優化。**

### Known problems / 已知問題

These are real, reproducible, and unsolved. Pull requests and ideas on any of them are very welcome.

以下每一條都是真實、可重現、還沒解決的問題。針對任何一條的 PR 或想法都非常歡迎。

| # | Problem | 問題 |
|---|---------|------|
| 1 | **Tracking stability.** Landmark jitter still leaks through the One Euro Filter. Tightening the filter adds lag; loosening it adds shake. The cutoff constants are hand-tuned, not derived. | **手勢穩定度。** 關節點抖動仍會穿過 1€ 濾波器。調緊就有延遲，調鬆就會抖，濾波參數是手調的、沒有理論根據。 |
| 2 | **Fast swipes and hand withdrawal are misread.** A quick flick can be dropped between frames, and pulling the hand out of frame sometimes injects a phantom velocity burst instead of stopping. | **快揮與收手誤判。** 太快的撥動會在幀之間漏掉；把手收出畫面時，有時不是停下來，而是被注入一股假的速度。 |
| 3 | **Pinch-to-zoom sensitivity varies per person.** Hand size, finger length and camera distance all change what "pinch distance" means. The normalization is crude. | **捏合縮放靈敏度因人而異。** 手掌大小、手指長度、離鏡頭距離都會改變「捏合距離」的意義，目前的正規化很粗糙。 |
| 4 | **Lighting and camera quality dominate results.** Backlight, warm indoor light or a cheap webcam degrade detection far more than any parameter tuning helps. | **不同光線與鏡頭品質差異極大。** 逆光、暖色室內燈、便宜的視訊鏡頭造成的劣化，遠大於調參數能救回來的幅度。 |
| 5 | **Mobile performance and heat.** Continuous inference plus WebGL drains battery and throttles after a few minutes on phones. | **手機效能與發熱。** 持續推論加上 WebGL 很耗電，手機跑幾分鐘後會降頻。 |
| 6 | **One-hand / two-hand switching is abrupt.** Going from a one-hand rotate to a two-hand scale (and back) can snap the view. | **單手／雙手切換不順。** 從單手轉視角切到雙手縮放（或切回來）時，畫面會跳一下。 |
| 7 | **No haptic feedback.** Air buttons rely on a dwell timer, so there is no way to feel whether you actually pressed something. Dwell too short = accidental fires, too long = feels broken. | **沒有觸覺回饋。** 隔空按鈕靠停留計時觸發，使用者感覺不到自己到底按到沒有。停留太短會誤觸，太長又覺得壞掉。 |
| 8 | **Pointing vs. fist is a heuristic.** An extended index finger is excluded from the fist test, but half-open hands still sit in an ambiguous zone. | **指向與握拳靠啟發式判斷。** 食指伸直會被排除在握拳判定外，但半開的手仍落在模糊地帶。 |

If you have a better filter, a better gesture state machine, a calibration step, or simply a different idea — open an issue or a PR.

如果你有更好的濾波器、更好的手勢狀態機、校正流程，或只是想到不一樣的做法——開 issue 或 PR 都可以。

---

## Running it / 怎麼跑

The camera API requires a secure context, so **`https://` or `localhost` is mandatory** — opening `index.html` directly with `file://` will not get camera access.

鏡頭 API 需要安全環境，所以**一定要 `https://` 或 `localhost`**，直接用 `file://` 開檔案是拿不到鏡頭的。

```bash
git clone https://github.com/HUANGCHIHHUNGLeo/solar-atlas-gesture.git
cd solar-atlas-gesture

# any static server works — pick one
python3 -m http.server 8000
# or
npx serve .
```

Then open and press **ENABLE CAMERA**. The first load fetches the ~7.8 MB hand landmark model from the local `vendor/` folder.

接著開 ，按 **啟用鏡頭**。第一次載入會從本機 `vendor/` 讀約 7.8 MB 的手部模型。

**The page is fully usable without a camera too** — mouse drag / wheel and touch pinch do everything gestures do. Language is switched with the button in the top-left corner and remembered in `localStorage`. Add `?debug` to the URL for a live overlay of inference time, pinch velocity and gesture state — useful when tuning the parameters above.

**沒有鏡頭也能完整使用**——滑鼠拖曳／滾輪、觸控捏合可以做到手勢能做的所有事。語言用左上角按鈕切換，選擇會記在 `localStorage`。網址加 `?debug` 會顯示推論時間、捏合速度與手勢狀態的即時面板，調上面那些參數時很有用。

### Gestures / 手勢

| Gesture | Action | 動作 |
|---|---|---|
| Open palm swipe | Rotate the view (with momentum) | 撥動轉視角（有慣性） |
| Pinch (thumb + index) | Zoom in / out | 縮放 |
| Zoom out to the limit | Step out one scale | 縮到底＝跳上一個尺度 |
| Zoom in to the limit | Step in one scale | 放大到頂＝回下一個尺度 |
| Point at a body | Highlight, then fly to it and open its data card | 指向天體＝高亮，再飛過去開資料卡 |
| Point and dwell on a side button | Press it in mid-air | 指著側邊按鈕停留＝隔空按下 |

---

## Scales / 尺度層

Zooming all the way out moves up a level, so the whole thing is one continuous zoom from a moon to the Local Group.

一路縮小就會往上跳一層，從一顆衛星到本星系群是一條連續的縮放線。

1. **Solar System** — 8 planets with real textures, 9 major moons, 2 dwarf planets, orbit lines, auto tour
2. **Nearby stars** — 12 stars within ~41 ly, positioned by real distance (directions are illustrative)
3. **Exoplanet system** — fly into a star and see its confirmed planets
4. **Milky Way** — top-down illustrative view with the Sun marked on the Orion Arm
5. **Local Group** — the Milky Way, the Magellanic Clouds, M31 and M33

Layers 4 and 5 are explicitly labelled as illustrative: the structure is an artistic reconstruction and the marker positions are not true sky directions.

第 4、5 層明確標示為示意圖：結構是藝術重繪，亮點位置不是真實方位。

---

## Architecture / 技術架構

Single self-contained HTML file. No framework, no bundler, no npm install.

單一自足的 HTML 檔案，沒有框架、沒有打包工具、不用 npm install。

```
index.html      the whole app: data layer, Three.js scenes, i18n, gesture layer
three.min.js    Three.js (MIT)
tex/            planet textures (Solar System Scope, CC BY 4.0)
vendor/         MediaPipe Tasks Vision + hand landmark model + One Euro Filter
```

- **Hand tracking** — MediaPipe `HandLandmarker` in VIDEO mode, GPU delegate, up to 2 hands, 21 landmarks each.
- **Smoothing** — a One Euro Filter per tracked signal (palm x/y, hand x/y, pinch distance, thumb x/y). Separate constants for motion (`1.0 / 0.007`) and pinch (`1.5 / 0.25`), because pinch needs responsiveness where motion needs smoothness.
- **Gesture state machine** — hysteresis on every threshold (grab on at 0.40, off at 0.62; fist on at 1.2, off at 1.5) plus a 130 ms release grace period so a brief tracking loss does not cancel a swipe mid-flick.
- **Momentum** — an open-palm swipe injects velocity above a speed threshold only, so slow aiming movements do not spin the scene. Damped exponentially each frame.
- **Zoom** — pinch drives a critically-damped spring on scale, not a direct assignment, which is what makes the scale changes feel physical.
- **Multi-scale LOD** — each scale is built on entry and disposed on exit (the Solar System scene is cached because its textures are expensive). Crossing a scale boundary is triggered by the spring settling past a limit, with a 900 ms cooldown to stop it oscillating between levels.
- **Rendering** — Three.js `WebGLRenderer`, sRGB pipeline, a Milky Way skybox sphere, and a raycaster for picking. The focused body is centred by translating the scene group, not by moving the camera.
- **i18n** — one data set, two label sets. Numeric values are never duplicated between languages; only field names, descriptions and units are switched, so the English and Chinese cards can never disagree about a number.

---

## Data sources / 資料來源

All figures are from NASA and are shown with their source on every card. Fields NASA does not publish are left blank rather than filled in from elsewhere.

所有數值來自 NASA，每張卡片都標示來源。NASA 沒有公布的欄位一律留空，不從別處補。

- **Planets, moons, dwarf planets** — NASA NSSDC Planetary Fact Sheet
- **Phobos and Deimos** — NASA Science
- **Stars and exoplanets** — NASA Exoplanet Archive (TAP API, default parameter set), queried 2026-08-29
- English body names follow NASA naming (NSSDC and the NASA Exoplanet Archive); Chinese names follow common Traditional Chinese usage.

NASA does not endorse this project.

---

## Licenses / 授權

Source code: **MIT**.

**Textures are not MIT.** The planet and star maps in `tex/` are © Solar System Scope (INOVE) under CC BY 4.0 — free to use and modify, including commercially, **as long as attribution is kept**. The footer of the page carries that attribution; please keep it if you fork, redistribute, or deploy this.

**貼圖不是 MIT。** `tex/` 裡的行星與恆星貼圖版權屬 Solar System Scope (INOVE)，採 CC BY 4.0——可自由使用與修改（含商用），**但必須保留出處標註**。頁尾已經放了標註，fork、散布或部署時請保留。

Bundled libraries keep their own licenses: Three.js (MIT), MediaPipe Tasks Vision and the hand landmark model (Apache 2.0, © Google), One Euro Filter (BSD 3-Clause, © Inria). Full details in THIRD-PARTY-NOTICES.md.

---

## Contributing / 貢獻指南

The most valuable contributions are on the eight problems listed above. Concretely, these directions are wide open:

最有價值的貢獻是上面那八個問題。具體來說這些方向都還很空：

- **Filtering and prediction** — replace or complement the One Euro Filter (Kalman, adaptive cutoff, velocity prediction to hide latency).
- **Calibration** — a short first-run routine that measures the user's hand span and normalizes pinch distance to it.
- **Gesture state machine** — a cleaner model than nested thresholds; ideas for making fast swipes and hand withdrawal read correctly.
- **Feedback without haptics** — audio, visual progress, or a better dwell affordance so air buttons feel pressable.
- **Mobile** — lower inference rate when idle, resolution scaling, thermal-aware throttling.
- **Robustness** — behaviour under backlight and low light, and with low-quality webcams.
- **Accessibility** — full keyboard control, reduced-motion support, screen reader labels for the data cards.
- **Data and content** — more moons, more nearby stars, better illustrative layers — as long as every number keeps a NASA source and unknown fields stay blank.

### How to open an issue / 怎麼開 issue

For a gesture bug, please include: browser and OS, device (and whether it has a discrete GPU), camera model if you know it, lighting conditions, whether one or two hands were in frame, and the `?debug` overlay reading when it happened. A short screen recording is worth more than a paragraph.

回報手勢問題時請附上：瀏覽器與作業系統、裝置（有沒有獨顯）、鏡頭型號（知道的話）、光線狀況、當下畫面裡是單手還是雙手，以及發生當下 `?debug` 面板的數字。一小段螢幕錄影勝過一大段文字。

For a data correction, please link the NASA page you are citing.

回報資料錯誤時，請附上你引用的 NASA 頁面連結。

### Pull requests / PR

Keep it dependency-free and keep it in one file where it makes sense — the point of this project is that anyone can open `index.html` and read the whole thing top to bottom. If a change affects gesture feel, please say how you tested it and with how many different hands, because that is the part no amount of code review can verify.

請維持零依賴，能放在同一個檔案裡就放——這個專案的重點是任何人打開 `index.html` 都能從頭讀到尾。如果改動影響手感，請說明你怎麼測的、找了幾雙不同的手試——這部分是 code review 驗不出來的。

## 关联链接

- https://`
- https://github.com/HUANGCHIHHUNGLeo/solar-atlas-gesture.git

## 导航

- 项目页：[[10-项目/github.com_f47bedba]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
