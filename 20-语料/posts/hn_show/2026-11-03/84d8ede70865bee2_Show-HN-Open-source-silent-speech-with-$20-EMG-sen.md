---
type: "corpus"
item_id: "84d8ede70865bee2"
title: "Show HN: Open-source silent speech with $20 EMG sensors and a webcam"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50340631"
project_url: "https://github.com/thaimtl/Silent-Voice"
author: "gottaguo"
published_at: "2026-11-02T17:48:03Z"
captured_at: "2026-11-04T10:05:48+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_gottaguo
  - story_50340631
  - show_hn
metrics: {"points": 4, "comments": 5, "engagement_velocity": 4}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:3d"
---

# Show HN: Open-source silent speech with $20 EMG sensors and a webcam

> [!info] 一句话导读
> thaimtl/Silent-Voice

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50340631>
> 指标：点赞=4 · 评论=5 · engagement_velocity=4
> 作者：gottaguo　|　发布：2026-11-02T17:48:03Z
> 项目链接：<https://github.com/thaimtl/Silent-Voice>
> 采集：2026-11-04T10:05:48+08:00　|　id：`84d8ede70865bee2`

## 正文

# thaimtl/Silent-Voice

Silent speech for people who lost their voice box. Cal Hacks 13.0.

- Stars: 8
- Forks: 2
- Watchers: 8
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-10-24T01:16:57Z

## Languages

- Batchfile
- C++
- CSS
- HTML
- JavaScript
- Python
- Shell

## Top Contributors

- thaimtl (73 contributions)
- AustinKol (50 contributions)
- evanliuuu (11 contributions)
- FrankWoah (6 contributions)

---

## README

# Silent Voice

Silent Voice gives a voice back to people who lost their voice box.
You mouth the words without a sound, and Silent Voice speaks them in your own voice while you're still mouthing, even on a phone call.

We built it at Cal Hacks 13.0, where it placed 2nd overall and won Cartesia's voice AI challenge.
The story of the weekend is in Thai's writeup.

## Who it's for

A laryngectomy removes the voice box, usually after throat cancer.
People keep their lips, tongue, and jaw, so the words are still there, only the sound is gone.
Many of them speak through an electrolarynx, a handheld buzzer that sounds robotic and ties up a hand.
We think they deserve a voice that sounds like them, keeps up with a real conversation, and works on an ordinary phone call, and that's what we're building.

Our demo speaker is Austin, who's healthy, and no patients take part in the demo.

## How it works

Silent Voice has one mode, open mouth, no sound, in real time.
Three readers work together, because each one sees what the others can't.
Every 100 ms one joint search combines them and locks in each word as soon as they're confident enough.

- The camera reads the lips and does most of the work.
 It also reads the facial expression, which sets the voice's emotion.
- The EMG model reads the electrical signals of the face muscles, so it sees the tongue and jaw that no camera can.
 It settles words that look alike on the lips ("bat", "mat", "pat"), proposes its own guesses, and keeps going when the face is hard to see.
- Claude follows the whole conversation, both sides.
 It predicts likely words before you start mouthing and repairs look-alike mistakes ("bills" → "pills" after a question about medicine).
 It only swaps look-alike words and never adds ideas.
- Cartesia speaks each word in your cloned voice as soon as it locks, without waiting for the end of the sentence.
- When the system can't tell what you said, it shows "Please repeat" instead of guessing.

Read on for the details.

- docs/REALTIME_PIPELINE.md explains how the whole system works.
- docs/SVR1_SPEC.md specifies the EMG model, SVR-1.
- docs/TEAM_TASKS_AND_INTERFACES.md covers who builds what.
- HARDWARE.md describes the rig, and RECORDING.md the recording sessions.
- DEMO.md runs the demo: one launcher starts everything in order (`Launch Silent Voice.bat`).

## What we demo

The demo is two minutes, live, at our table.

1. Austin calls the judge standing in front of us, through Twilio.
 The judge talks normally, and their words appear in the captions.
2. Austin mouths his side of the conversation.
 His words appear as he mouths and play into the call in his cloned voice while he's still going.
3. His facial expression sets the voice's emotion.
4. The dashboard shows the real latency, which reader settled each word, and what Claude changed.

## Stack

| Part | Tool |
|---|---|
| Live lip reading | Ours (`lipread/`), built on the open Auto-AVSR model. We turned a clip-by-clip reader into a live one that streams word guesses as Austin mouths, knows when he starts and stops, and feeds every guess into one joint search with the EMG model and Claude. |
| Face, mouth crop, expression | MediaPipe FaceLandmarker |
| Muscle signals | BioAmp EXG Pill boards and an Arduino Uno, see HARDWARE.md |
| EMG model | SVR-1, ours: PyTorch, pre-trained on Berkeley's silent speech data, fine-tuned on Austin |
| Context and repairs | Claude, through the Claude API |
| Voice clone and speech | Cartesia Sonic 3.6, Instant Voice Clone |
| The other person's speech to text | Cartesia Ink |
| Phone call | Twilio |
| Compute | One laptop, RTX 5060 |

## Code and data

All code lives in this repo.
Datasets, checkpoints, results, and Python environments live in a working directory outside it, and the code finds them through the environment variable `RECLAIM_WORKDIR` (datasets in `silent_speech/` and `data/`, plus `checkpoints/`, `benchmark_results/`, `recordings/`, `third_party/`).
Without it, the code expects data next to itself, which is how the cluster copy works.
Data folders are in `.gitignore`.

| Folder | What it is |
| --- | --- |
| `svr/` | SVR-1, the EMG model: model, training, fine-tuning, preprocessing (docs/SVR1_SPEC.md) |
| `fusion/` | The fusion process: the joint search over camera + EMG + Claude (`search.py`), the lock model (`lock.py`), on the bus (`run.py`), offline fitting and tests on the recordings (`offline.py`), and its language model: a conversational 4-gram with a cache of the call (`lm.py`, built by `build_lm.py`) |
| `bench/` | Benchmarks and their frozen test splits |
| `cluster/` | H100/H200 job scripts (PBS), smoke tests, runbook |
| `camera/` | Camera-only baselines (Auto-AVSR, BRAVEn, LipLearner) |
| `rig/` | EMG rig: Arduino firmware, serial reader, live hum filter, signal check, `emg.raw` publisher (`publish.py`) |
| `recorder/` | The recording app: camera + EMG + the session sentences (recorder/README.md) |
| `bus/` | The team bus: ZeroMQ wire format, the camera's topics (`__init__.py`) and every other endpoint and port (`team.py`); a fake camera (`stub.py`) and a typed stand-in for the judge (`type_judge.py`) for tests |
| `buslog/` | Logs every bus message to `$RECLAIM_WORKDIR/logs/` (`record.py`) and replays a session (`replay.py`) |
| `claude_service/` | The Claude service: predicts Austin's next words and repairs look-alikes (`brain.py`), on the bus (`service.py`) |
| `dashboard/` | The live dashboard judges watch, from Thai's Figma v5, fed by the bus (dashboard/README.md) |
| `demo/` | The demo launcher (`launch.py`, DEMO.md); `demo/dashboard/`: the captions dashboard prototype (demo/dashboard/README.md) |
| `call/` | The phone call: Twilio, Austin's cloned voice (Cartesia Sonic) and the judge's captions (Cartesia Ink) (call/README.md) |
| `figures/` | The SVR-1 architecture figure, the SVR-1 vs Gaddy & Klein results (`svr1_vs_gaddy_4ch*`), and the scripts that draw them |
| `tests/` | Smoke and unit tests |
| `docs/` | Plans and specs, Markdown with PDF copies |

## Known limitations

- This is a prototype, not a medical device.
- Lip reading gets about 1 in 5 words wrong even on normal speaking video, and silent mouthing is harder.
 The EMG model and Claude are there to close that gap.
- The EMG model is trained for one person (Austin), from three recording sessions, see RECORDING.md.
- The voice runs a little behind the lips, because a word is spoken only once it's confident enough to lock.

## Built on

- Digital Voicing of Silent Speech, Gaddy and Klein, UC Berkeley, 2020, for the electrode sites and pre-training data.
- Auto-AVSR, Ma et al., 2023, for lip reading.
- Lipflow, MIT license, for live mouth cropping with MediaPipe.

## Team

Thai (EMG hardware and the Claude service), Austin (EMG model and fusion, and the speaker in the demo), Frank (Cartesia voice, the Twilio call, and the captions dashboard), and Evan (real-time lip reading and facial emotion).

## License

Silent Voice is open source under the MIT license.
Bundled third-party files keep their own licenses, which are Mermaid (MIT, `docs/vendor/mermaid.LICENSE`), the Liberation Sans and Atkinson Hyperlegible Next fonts (SIL Open Font License 1.1), and MediaPipe's face mesh data (Apache-2.0).

# joebew42/aido

## 评论（5/5）

> **gottaguo** · 2026-11-02T17:48:03.000Z　
> Hi HN, Frank here. We placed second overall at Cal Hacks 13.0 (700+ projects), four of us from McGill.Over 200,000 people are diagnosed with throat cancer each year, and for many, the surgery removes their voice box. More than half a million people are already living without one.Their lips, tongue and jaw still move in the same way, but with nothing there to create any sound, they lose the ability to speak forever.In 36 hours we built Silent Voice to give them their voice back.With four different AI systems working together, Austin held a full phone call without making a sound, and the caller heard him in his own voice.• Muscles: we built a sensor rig using four surface EMG pads ($20 each) to measure the electrical activity in his face 1,000 times a second, and used a neural network (SVR-1) we'd trained to infer the movement of his tongue and jaw (which a camera can't see)• Lips: Auto-AVSR is a lip-reading technique which only works on complete video. We rebuilt it to work in real-time, re-reading Austin's sentence 10 times a second• Face: computer vision tracks his expressions and carries his emotion through the voice• Context: Claude uses both sides of the conversation to predict what Austin may say, and compensates for common confusions such as 'bills' and 'pills'SVR-1 is ~45M params, 12 transformer layers on top of 3 conv blocks, pretrained on Berkeley's 19h silent speech set then fine tuned on ~70 min of Austin. With only our 4 pads it picks the right sentence out of 10 lip look-alikes 72.3% of the time, Berkeley's released model gets 27.7% (theirs was trained on 8 pads though).I led the voice pipeline. Standard techniques rely on complete input, but we were only receiving individual words as Austin formed them. Waiting for a complete sentence meant callers were subjected to 4.9 seconds of dead air, whilst sending single words sounded like a robot reading a list.So I re-engineered the entire streaming layer into Cartesia, delivering complete (though brief) phrases in step with Austin's natural pauses, and cut the silence added by the model after each phrase (around half a second) down to a more natural (i.e. human) breath. His expression can also shift the emotion mid-sentence.As a result, callers were hearing Austin 0.6 seconds after his lips began to move, in real-time.It's a prototype, Austin is healthy and no patients have tried it yet. Code is open source, the demo is on the Devpost: https://devpost.com/software/silent-voice-s1f74pIf you've had (or know someone who's had) a laryngectomy, or work with them as a speech therapist, I'd love to hear from you.

---

> **drop_star** · 2026-11-02T18:02:27.000Z　
> very cool

---

> **thaifrommtl** · 2026-11-02T18:55:12.000Z　
> so proud we had achieved this in 36 hours!! i hear YC has a startup that does something kinda similar too

---

> **austinkomachi** · 2026-11-02T19:33:50.000Z　
> It was amazing working with you Frank. So incredibly happy that we took home the big W.

---

> **gottaguo** · 2026-11-02T18:38:10.000Z　
> thanks! the part i'm proudest of is the voice latency, we went from 4.9s of dead air to 0.6s. happy to go into how if anyone's curious

## 导航

- 项目页：[[10-项目/github.com_703344b0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
