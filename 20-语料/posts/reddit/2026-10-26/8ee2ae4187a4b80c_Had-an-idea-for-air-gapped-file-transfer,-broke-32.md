---
type: "corpus"
item_id: "8ee2ae4187a4b80c"
title: "Had an idea for air-gapped file transfer, broke 32+ Mbps"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SideProject/comments/1x73m5k/had_an_idea_for_airgapped_file_transfer_broke_32/"
project_url: "https://fosslabs.dev/"
author: "failingapbio"
published_at: "2026-10-16T09:40:45+08:00"
captured_at: "2026-10-26T09:43:44+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/SideProject
metrics: {"score": 9, "comments": 6, "upvote_ratio": 0.8461538461538461}
comments_count: 6
comments_total: 6
discovered_via: "reddit:14d+settle10"
---

# Had an idea for air-gapped file transfer, broke 32+ Mbps

> [!info] 一句话导读
> Hi everyone! I was looking at optical file transfer and saw that Decimen was rather ineffective. Firstly, it's QR-based system really seemed to be designed for …

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SideProject/comments/1x73m5k/had_an_idea_for_airgapped_file_transfer_broke_32/>
> 指标：得分=9 · 评论=6 · 赞踩比=0.8461538461538461
> 作者：failingapbio　|　发布：2026-10-16T09:40:45+08:00
> 项目链接：<https://fosslabs.dev/>
> 采集：2026-10-26T09:43:44+08:00　|　id：`8ee2ae4187a4b80c`

## 正文

Hi everyone! I was looking at optical file transfer and saw that Decimen was rather ineffective. Firstly, it's QR-based system really seemed to be designed for paper, where binary design is necessary to  prevent ink smudging. On a screen, binary is ineffecient, although luminance makes sense. I looked at a lot of research papers and eventually found this:I saw that OFDM was the logical improvement off QR codes, as it used actual signal processing and luminance instead of binary black-and-white QR. So I decided to base my system off FOCUS. For fast decoding, I also wanted it to be GPU based rather than CPU based, and to deal with frame desync well.

[https://vs.inf.ethz.ch/publ/papers/soeroesg-mobisys2016-Focus.pdf](https://vs.inf.ethz.ch/publ/papers/soeroesg-mobisys2016-Focus.pdf) After that, I stripped the FOCUS finders (the original finders were ugly and wasted a lot of space) and came up with a custom, compact ring. the ring has around 15 bits of information distributed via Reed Solomon along the giant ring. A GPU can easily decode the ring's RS it by brute forcing the maximum likelihood of each of the 32,768 codewords.

To balance between range and maximizing speed, i created 4 different ring sizes; 32, 64, 128, and 256. Initially I wanted to stick with the browser; however, the browser is woefully inefficient in webcam tuning. After maxing the settings, we were still at 700 KB/s; better than Decimen but hardly a knockout blow. I couldn't switch to 60fps without it oscillating wildly between 1.3 MB/s to 0 MB/s when out of phase. So I decided to focus on a native android instead. LIZARD is a format; decoders can choose how to decode it.

A weak web decoder doesn't prevent me from making a strong native decoder; the format is the same, while a fountain code called Wirehair allows slow and fast speeds to both exist. Initially, Claude tried to port the OpenCV based finder to Vulkan. Branchy work is not great on a GPU, which struggles with warp divergence, so I scrapped that. However, AI inference is perfect for a GPU. As I had an RTX 4090, I asked it to make a generator, open pytorch, and train a custom, 50k parameter AI finder that uses the grayscale image and finds four corners. The CPU based OpenCV finder helped create training frames solutions for the GPU, which was given high levels of noise and perspective distortion in order to make it harder to detect than phones. I kept training it till the GPU version defeated the CPU in finding accuracy. After a few hours, had fully trained a custom 3-layer CNN that found the code easily in 1.5 ms on the GPU.

Next, I faced a massive issue: camera/frame desync. This was the bane of optical camera communication, with many resarch papers trying to defeat this with barcodes. The difference between my code and a QR: half of a FOCUS image can decode, meaning that if part of another frame was captures, some of it could decode. Additionally, android's native Camera2 API allows you to defeat this problem completely. it allows you to control the delays between frames. As a result, I decided to embed pilot signals in the image. Every four frames, it cycles through these four pilots.

0 0
1 0
0 1
1 1

This created a way to estimate how much of the last frame and future frame was on it. As it had two variables and two unknown frames, it was solvable; as a result, the camera knew how far off it was each frame. Then, it was able to adjust the time accordingly, keeping the rates stable at 60FPS. Voila! I had solved the hardest problem in OCC.

Speed: 0.7→1.4-1.6 MB/s

i returned an idea that I scrapped on web due to lag; 2:1 multiplexing. there is no reason why 2 square codes wouldn't store more; 1920x960 is far better than 1080x1080 in size. The change i did that made it viable; I did not try for a complex 2:1 mode, but simply multiplexed two frames side by side; two 960x960 squares.  At this point the improvement of LIZARD went smoothly.

Speed: 0.4-1.6→2.1 MB/s

There were three final levers, but they were mundane. Firstly, I disabled the ISP edge enhancement and other cosmetic optimizations that were terrible for keeping signal. Then, i made the error correction levels higher for outer frequencies and lower for inner frequencies. I also added another LDPC rate. After that, I replaced the 96-module ring with the 256-module ring. That massively increased the area of signal. I used random old school monitors and they still got a similar rate. What phone did I use? S26 ultra. 1.5x zoom . 105 degree lens. 1080p, 60fps. it seems like the lens settings were far more influential than any monitor i used.I hope you liked my system! lmk what your thoughts are.

Speed: 2.1→4.1 MB/s

Note: the high speeds only exist reliably on Android.
Try it here!: [https://fosslabs.dev/](https://fosslabs.dev/)

## 评论（6/6）

> **QuanTradin**（1 分） · 2026-10-16T10:27:10+08:00　
> 32 Mbps through a webcam is wild. moving the ring decode to the GPU instead of fighting browser webcam tuning makes sense, 700 KB/s was never going to move much.

---

> **No-Narwhal5412**（1 分） · 2026-10-18T11:29:30+08:00　
> github

---

> **failingapbio**（1 分） · 2026-10-18T12:48:41+08:00　
> [https://github.com/FNWTalon/LIZARD](https://github.com/FNWTalon/LIZARD)

---

> **No-Narwhal5412**（1 分） · 2026-10-18T14:08:20+08:00　
> dayumm sonn

---

> **Drenlin**（1 分） · 2026-10-19T13:43:07+08:00　
> ...does it still count as an "air gap" if you've technically established a direct digital connection?
>
> This is sick though, well done my guy.

---

> **failingapbio**（1 分） · 2026-10-19T13:47:53+08:00　
> it is 100% one way and has 0 ACK's. so yes

## 关联链接

- https://vs.inf.ethz.ch/publ/papers/soeroesg-mobisys2016-Focus.pdf

## 导航

- 项目页：[[10-项目/fosslabs.dev_7f4bc7ec]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
