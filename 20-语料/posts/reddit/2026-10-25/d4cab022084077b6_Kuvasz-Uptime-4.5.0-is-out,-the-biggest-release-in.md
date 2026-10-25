---
type: "corpus"
item_id: "d4cab022084077b6"
title: "Kuvasz Uptime 4.5.0 is out, the biggest release in a while"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6o5dn/kuvasz_uptime_450_is_out_the_biggest_release_in_a/"
project_url: "https://demo.kuvasz-uptime.dev/"
author: "csirkezuza"
published_at: "2026-10-15T23:06:40+08:00"
captured_at: "2026-10-25T23:28:44+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-15"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Release (AI)
metrics: {"score": 52, "comments": 33, "upvote_ratio": 0.8513513513513513}
comments_count: 33
comments_total: 33
discovered_via: "reddit:14d+settle10"
---

# Kuvasz Uptime 4.5.0 is out, the biggest release in a while

> [!info] 一句话导读
> https://i.redd.it/uqrf0ttmbnvh1.png

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6o5dn/kuvasz_uptime_450_is_out_the_biggest_release_in_a/>
> 指标：得分=52 · 评论=33 · 赞踩比=0.8513513513513513
> 作者：csirkezuza　|　发布：2026-10-15T23:06:40+08:00
> 项目链接：<https://demo.kuvasz-uptime.dev/>
> 采集：2026-10-25T23:28:44+08:00　|　id：`d4cab022084077b6`

## 正文

https://i.redd.it/uqrf0ttmbnvh1.png

Hey there,

first of all:

*Kuvasz* is an open-source, self-hostable monitoring solution (HTTP, TCP, DNS, push, Docker and ICMP) with status pages, webhooks, an MCP server and IAC support, a great alternative to UptimeRobot or Kuma.

**How AI was used in the project**: I started working on it in 2020 and I didn't use any LLM up until this May (version 3.8.0). Since then I use Claude Code in a quite "old-fashioned" way: I commit everything by hand after carefully reviewing every change on the project. The pre-existing quality gates of the project are also very strict to make slop even harder to introduce.

I was working on the latest release a lot, probably this is the biggest one since the project exists:
[https://kuvasz-uptime.dev/changelog/#4.5.0](https://kuvasz-uptime.dev/changelog/#4.5.0)

# A brand new dashboard (see the screenshot above)

The old one was quite ugly and also not so informative, so I rewrote it from scratch.

# Docker monitoring

Instead of checking a port, Docker monitors ask the daemon whether a container is actually running and healthy. They catch crash loops, OOM kills, paused containers and failing healthchecks, and the errors say what happened, e.g. "The container exited (137) after it was OOM killed". Restart counts and CPU/memory history are recorded too. The daemon can be local, behind a socket proxy, or remote over mTLS.

# Slack Bot integration with threading support

Every incident and maintenance window gets its own thread, so a flapping monitor no longer floods the channel. The first message always shows the **current** state (updated after a resolution) and details + notes are sent to the thread.

# Incidents, properly told

Each incident has a details page with a timeline: when it started, who was notified, the notes you added, and when it was resolved. Public notes also show up on status pages, next to the active and recently resolved incidents.

https://i.redd.it/grtj55hxbnvh1.png

# Also in this release:

* Configurable color schemes for the app and the status pages
* HTTP and TCP checks through HTTP or SOCKS5 proxies
* An opt-in connectivity check that pauses monitoring while the Kuvasz host itself is offline, so you don't get an incident storm
* An interactive install script for Docker Compose
* PostgreSQL over a unix socket, a more locked-down Helm chart, and a fix for shutdowns hanging while checks were failing

Live demo: [https://demo.kuvasz-uptime.dev](https://demo.kuvasz-uptime.dev) (user: `demo` | pass: `secureDemoPassword`)

GitHub: [https://github.com/kuvasz-uptime/kuvasz](https://github.com/kuvasz-uptime/kuvasz)

## 评论（33/33）

> **asimovs-auditor**（1 分） · 2026-10-15T23:06:50+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **csirkezuza**（2 分） · 2026-10-15T23:07:36+08:00　
> I started working on it in 2020 and I didn't use any LLM up until this May (version 3.8.0). Since then I use Claude Code in a quite "old-fashioned" way: I commit everything by hand after carefully reviewing every change on the project. The pre-existing quality gates of the project are also very strict to make slop even harder to introduce.

---

> **TornWebServices**（-9 分） · 2026-10-15T23:23:36+08:00　
> docker monitors that report why a container died instead of just that the port is closed, that saves a lot of guessing at 2am

---

> **ethansky**（5 分） · 2026-10-15T23:39:35+08:00　
> [Bot](https://arctic-shift.photon-reddit.com/search?fun=comments_search&author=TornWebServices&limit=10&sort=desc) ^

---

> **Resistant4375**（-1 分） · 2026-10-16T00:02:57+08:00　
> Yup. Always engagement bots everywhere when AI slop is posted.

---

> **csirkezuza**（1 分） · 2026-10-16T00:06:55+08:00　
> mate, you could elaborate on the "slop" part :)

---

> **FallenVain**（6 分） · 2026-10-16T01:41:44+08:00　
> Love the docker stuff, we now just need Kubernetes!

---

> **YmedBrei-67**（3 分） · 2026-10-16T04:16:39+08:00　
> tbh the connectivity check feature alone would save a lot of headaches. how does it determine the host is offline, just a dns/http check to a known endpoint?

---

> **fernandops**（4 分） · 2026-10-16T07:03:55+08:00　
> During the connectivity pause, does the status page show “monitoring unavailable” with the last successful check time? Leaving everything green could make a monitoring outage look like confirmed uptime. The gap would be useful to keep in the incident timeline too.

---

> **MFKDGAF**（-5 分） · 2026-10-16T08:27:00+08:00　
> How much AI was used in the making of the dashboard?
>
> This looks like a cool alternative to UK, but the dashboard is throwing me off. If feels heavily AI made but also very cluttered with all the different informational tiles.
>
> Is this dashboard fully customizable? Can you add/remove the tiles?

---

> **The_Troll_Gull**（2 分） · 2026-10-16T11:28:16+08:00　
> Can it support monitoring over 1900 devices??

---

> **csirkezuza**（4 分） · 2026-10-16T12:06:45+08:00　
> for a long time, the dashboard was a place that looked like a half-baked garbage, mostly because I'm no UI/UX designer (fullstack SWE with a backend/ops heavy focus), and also because Kuvasz started off as a simple HTTP-only uptime monitor. so what I did, after I realised that it could be better/nicer: I took a look at other tools (commercial, open-source both), noted down everything that I would like to personally see on such a dashboard, drew it on a paper, took a photo, looked up the relevant ui components from Tabler, and gave this to Claude as a spec (e.g. "this is the layout, these are the components, use the existing APIs/data to create a plan out of this").
> TBH, it sucked pretty hard with it, and I had to rewrite multiple things manually, because it was just too AI-ish, and too sloppy, so at the end I regret even starting working on it 😀
>
> TLDR: the tiles are not editable

---

> **csirkezuza**（2 分） · 2026-10-16T12:08:22+08:00　
> that's actually a good idea, I was thinking about recording the connectivitiy problems, and that's a logical use case of it

---

> **csirkezuza**（1 分） · 2026-10-16T12:09:12+08:00　
> a simple tcp lookup, by default to 1.1.1.1/8.8.8.8, but both the targets and the interval are fully configurable

---

> **csirkezuza**（3 分） · 2026-10-16T12:13:27+08:00　
> never tried that much TBH, but I can give it a spin with different scenarios. 300 monitors were the max that I benchmarked, with a fairly short check interval and that was handled without any problem. it uses Netty under the hood for the HTTP checks, which is very capable of handling extreme traffic both on the server and the client side, and the other checks are quite lightweight anyway. maybe ICMP is the riskiest at this scale because it uses the native ping under the hood by starting an actual OS process from the JVM. I'll create a benchmark

---

> **Joncallim**（1 分） · 2026-10-16T15:25:01+08:00　
> Does an open incident keep its Slack thread after a Kuvasz restart? It’d be handy to have the recovery message in the same thread.

---

> **csirkezuza**（1 分） · 2026-10-16T16:07:38+08:00　
> yes ofc

---

> **The_Troll_Gull**（2 分） · 2026-10-16T19:20:11+08:00　
> I have uptime kuma with 1918 devices being monitored. Surprised that Uptime kuma can handle it however it there is a 15 second lag when you reload the browser.

---

> **Cody212501**（0 分） · 2026-10-16T22:12:14+08:00　
> this looks quite promising, if I have time this weekend, I might create Helm templates and a setup guide for this

---

> **Joncallim**（1 分） · 2026-10-16T22:18:30+08:00　
> Great, thanks!

---

> **csirkezuza**（2 分） · 2026-10-16T23:58:37+08:00　
> it already has an official helm chart:
> https://kuvasz-uptime.dev/setup/helm-deployment/

---

> **csirkezuza**（1 分） · 2026-10-17T01:03:55+08:00　
> wow! and how much memory does it need to handle them? also, which type of monitors are they? i think their UI is using websockets everywhere, right? that might be the culprit why it wasn't so happy with such a huge amount of monitors :/
>
> I did a few exhaustive benchmarks btw, but I still need to formalize the results and iron out a few things, and then I'll add both the sizing guide to the docs and the benchmark suite to the repo for the sake of transparency.
>
> Long story short: it was able to handle 3000 monitors (mixed distribution of different monitor types and mixed check interval between 5 sec and 5 minutes) without any problem with a 1GB memory limit on the container (I also simulated 5 virtual users on the UI + API in parallel). These are the rough numbers:
>
> \- default settings, 768 MB limit on the container, 500 monitors
> \- \`-Xmx512M\` for the JVM and 1GB limit on the container, 3000 monitors
> \- \`-Xmx768M\` for the JVM and 1.5GB limit on the container, 5000 monitors
>
> It could have been pushed further, but I didn't see a point to do so, because at that point the UI will be the biggest bottleneck probably, but not in the same way as for Kuma. Kuvasz uses a quite old-school SSR (on purpose) and very minimal JavaScript magic on the frontend, which scales really well, however I was too lazy in the beginning and I didn't introduce pagination on the APIs from day one (I know, I know), so on the monitor list pages it just renders everything and then the tables are refreshed in place via HTMX. That works really well up until a few hundred monitors, but I'm pretty sure that it can cause some issues on slower clients above that. Anyway, it worth to try it I think, pagination both on the API and the UI is already on my list, independently from this topic.

---

> **csirkezuza**（1 分） · 2026-10-17T02:22:12+08:00　
> you mean deployment, or monitoring?

---

> **The_Troll_Gull**（2 分） · 2026-10-17T06:16:26+08:00　
> That’s pretty awesome. Um it’s a 2cpu 32gb azure server. We have a lot a remote assets we monitor. It never goes above 5gb of ram and cpu usage is able 30%. I honestly haven’t gave any attention to the outbound or inbound throughput. I may throw yours up in a vm and test it out over the weeekend.

---

> **csirkezuza**（2 分） · 2026-10-17T18:23:12+08:00　
> OK, I was to pessimistic, tried out the UI with 5K monitors, and it didn't even blink: [https://www.youtube.com/watch?v=84S3nNfVmcY](https://www.youtube.com/watch?v=84S3nNfVmcY)
> Details in the description of the video, but in short: it's the 1.5 GB memory setup, with only 1 CPU dedicated to the container on an Apple M1 Pro host (so the 1 CPU is probably beefier than the average ones, but the CPU is not the bottleneck anyway). Postgres is the stock postgres:18-alpine with 1 CPU and 1GB of memory limit (it peaked only around \~175 MB).

---

> **csirkezuza**（2 分） · 2026-10-17T19:06:03+08:00　
> Might be useful to imagine what Kuvasz is capable of when it comes to a large number of monitors (5000 monitors with 1.5 GB of memory): [https://kuvasz-uptime.dev/setup/sizing/](https://kuvasz-uptime.dev/setup/sizing/)

---

> **unspam-email**（2 分） · 2026-10-19T20:18:58+08:00　
> Asking the daemon instead of checking a port is the right call, since most people agree a TCP check misses crash loops and OOM kills. Our team runs Pulsetic for external checks, and container-level detail like this fills a real gap.

---

> **Roxelchen**（1 分） · 2026-10-20T04:25:24+08:00　
> does it support multiple users?

---

> **csirkezuza**（1 分） · 2026-10-20T13:27:42+08:00　
> currently only via your own OIDC provider

---

> **VestoMSlipher**（2 分） · 2026-10-20T15:48:38+08:00　
> This looks very interesting and I appreciate you checking if it scales for bigger fleets.
>
> May I presume if I wanted some disk monitoring I would need to use push monitors of some kind?

---

> **csirkezuza**（1 分） · 2026-10-20T16:53:44+08:00　
> I think so, yes. But which kind of disk monitoring do you mean exactly?

---

> **VestoMSlipher**（2 分） · 2026-10-21T04:27:40+08:00　
> Define a rule based on the state of a mount, of disk degradation, etc

---

> **csirkezuza**（1 分） · 2026-10-21T12:17:47+08:00　
> I'm using a similar personally, to check if a given external disk is mounted properly all the time, a cron job runs the check script and calls Kuvasz at the end on our home infra if everything was right

## 关联链接

- https://demo.kuvasz-uptime.dev
- https://github.com/kuvasz-uptime/kuvasz
- https://i.redd.it/grtj55hxbnvh1.png
- https://i.redd.it/uqrf0ttmbnvh1.png
- https://kuvasz-uptime.dev/changelog/#4.5.0

## 导航

- 项目页：[[10-项目/demo.kuvasz-uptime.dev_9028a67c]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
