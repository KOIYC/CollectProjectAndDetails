---
type: "corpus"
item_id: "02ab276b39463efa"
title: "I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/amananandrai/i-built-a-visual-system-design-reference-switch-any-architecture-between-aws-azure-gcp-open-55og"
project_url: "https://github.com/amananandrai/system-design-explainer"
author: "amananandrai"
published_at: "2026-11-02T20:40:43Z"
captured_at: "2026-11-16T10:03:09+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-02"
tags:
  - 语料
  - devto
  - systemdesign
  - webdev
  - opensource
  - showdev
metrics: {"reactions": 84, "comments": 11, "reading_time": 8}
comments_count: 11
comments_total: 11
discovered_via: "devto:showdev"
---

# I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source

> [!info] 一句话导读
> I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/amananandrai/i-built-a-visual-system-design-reference-switch-any-architecture-between-aws-azure-gcp-open-55og>
> 指标：reactions=84 · 评论=11 · reading_time=8
> 作者：amananandrai　|　发布：2026-11-02T20:40:43Z
> 项目链接：<https://github.com/amananandrai/system-design-explainer>
> 采集：2026-11-16T10:03:09+08:00　|　id：`02ab276b39463efa`

## 正文

# I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source

> 🔗 **Live site:** [system-design-explainer.vercel.app](https://system-design-explainer.vercel.app/)
> ⭐ **GitHub:** [amananandrai/system-design-explainer](https://github.com/amananandrai/system-design-explainer)

![System Design Explainer home page](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/omg41k9frmqynels17lx.png)

## 🧠 Why I Built This

![Before: 47 tabs of scattered diagrams. After: one map for every system](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/dj6vgaqrub37p3d8habe.png)

Like a lot of developers, I've spent hours reading system design articles, watching interview prep videos, and staring at static diagrams trying to understand *how YouTube actually handles an upload* or *how Uber matches a rider to a driver in real time*.

The problem I kept running into:

- Diagrams were **static** — you could see the boxes, but not how a request actually flows through them.
- Every diagram was tied to **one vendor's vocabulary**. An AWS diagram says "S3, SQS, DynamoDB", a GCP one says "Cloud Storage, Pub/Sub, Bigtable" — and translating between them in your head is tiring.
- My notes were scattered across bookmarks, Notion pages, and screenshots.

So I decided to build the reference I wished I had.

**This started as a personal project to learn and grow.** Building it forced me to actually understand each architecture well enough to draw it, break it into steps, and map every component across clouds. Somewhere along the way, I realised it could be just as useful for others preparing for interviews, designing real systems, or simply curious about how the apps they use every day work under the hood.

---

## 🚀 What Is System Design Explainer?

**System Design Explainer** is an interactive system design reference site where you can **visualise architectures of real-world systems** and **view the same architecture through different tool lenses** — a generic view, AWS, Google Cloud, Azure, or open-source tooling.

![YouTube architecture page with the diagram on the left and requirements on the right](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/lljlqu3v6k8sk5l8j2gx.png)

Every system page covers the requirements, APIs, capacity estimates, data model, request-flow walkthroughs, bottlenecks, scaling and extensions — all next to an auto-laid-out architecture diagram.

At the time of writing it has:

- 📦 **36 systems**
- 🧩 **36 components**
- 📚 **27 concepts**

---

## ✨ Key Features

### ☁️ 1. Switch Clouds in One Click

![Same architecture, new outfit: the same service mascot dressed up for Generic, AWS, GCP, Azure and Open source](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/mlt6o66ydr31stobidr0.png)

This is the feature I'm most excited about. Every architecture can be relabelled for:

- **Generic** (vendor-neutral building blocks)
- **AWS**
- **Google Cloud**
- **Azure**
- **Open source**

So the same "object storage → queue → worker → CDN" flow instantly becomes the matching services for whichever stack you work with. Here's the YouTube design switching between all five:

![YouTube architecture switching between Generic, AWS, GCP, Azure and Open source](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/8h6li1y8eu1icon8dnwu.gif)

Object storage becomes **Amazon S3**, **Cloud Storage**, **Azure Blob Storage** or **MinIO**; the event stream becomes **Amazon MSK**, **Pub/Sub**, **Azure Event Hubs** or **Apache Kafka** — same boxes, same arrows, different names. Great for interviews (where you're often asked to stay generic) *and* for real-world work (where you're usually tied to a specific cloud).

### ▶️ 2. Play Hop-by-Hop Walkthroughs

![A little envelope request hopping from Client to Load balancer to API gateway to Upload service to Object storage](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/qw0fxzcyrn075jv349wz.png)
Instead of just looking at a diagram, you can **follow a request step by step** — upload a video, book a seat, pay a merchant, create a short link. Each step highlights what's happening and which component is responsible, so you build intuition for the *flow*, not just the *layout*.

Here's what uploading a video to YouTube looks like:

![Walkthrough: uploading a video on YouTube, step by step](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/z9it50jdoq0pgl1s589r.gif)

And booking movie seats on BookMyShow (watch the seat hold and the idempotency key do their thing):

![Walkthrough: booking seats on BookMyShow](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/t7epj9ecxnvt27ggkufd.gif)

Walkthroughs work on every cloud too, so you can follow the exact same request through AWS, GCP or Azure services.

{% details 🎬 More walkthroughs (click to expand) %}

**Create a short link (URL shortener):**

![Walkthrough: creating a short link](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/swuukpnhbdm4p4s8v7v1.gif)

**Charge a card (payment gateway):**

![Walkthrough: charging a card through a payment gateway](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/fg0vfh9zloet077jdnic.gif)
**Request a ride (Uber, on AWS):**

![Walkthrough: requesting an Uber ride on AWS](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/uadk7ulqt36zeiueaijw.gif)

**Message an online friend (WhatsApp, on GCP):**

![Walkthrough: sending a WhatsApp message on GCP](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/21i8rnj268gd215lo8xy.gif)

**Payment declined → saga compensation (Amazon, on Azure):**

![Walkthrough: Amazon checkout with a declined payment and compensation on Azure](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/axtm8t59uy2m17rynvdr.gif)

{% enddetails %}

### 🔍 3. Inspect Components

Every building block (load balancers, caches, queues, databases, CDNs, etc.) has its own page covering:

- The options available per provider
- Common pitfalls
- Which systems on the site use it

![Components page: each building block mapped across AWS, GCP, Azure and open source](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/uwj6d2u1u2fc4wgwcrf7.png)
![In-memory cache component: when to use it, pitfalls and options by provider](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/t4n75kz3xvrh21gy0jtp.png)

### 📖 4. Learn the Patterns

![Cute mascots explaining caching, sharding, idempotency and fan-out](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/uin8z7e9u1y8vutyvzue.png)
Core concepts like **caching, sharding, fan-out, sagas, idempotency, consistent hashing, rate limiting, geospatial indexing, WebSockets, change data capture** and more are explained on their own — and linked back to the real designs where they're applied. Many concept pages even come with a small diagram you can step through.

![Idempotency concept page with a step-through example](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/qqugs5tde2b8i44oe49d.png)
### 🔎 Bonus: Search & Dark Mode

Hit `Ctrl K` to jump to any system, component or concept, and switch to dark mode for late-night interview prep.

![Search palette showing results for "pay"](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/4t4dznz1ies71a6dcts4.png)

![Uber architecture in dark mode](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/cbaa93wy4b2280lja072.png)
---

## 🗺️ Learning Paths

If you're not sure where to start, there are guided learning paths where each one builds on the patterns from the previous one. Your progress is saved in your browser.

![Learning paths: Foundations, Real-time systems, Media at scale, Money & bookings](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/4qvt2rky0r2p67c4cnoo.png)

| Level | Path | Systems |
|---|---|---|
| 🟢 Start here | **Foundations** | URL shortener → Pastebin → API rate limiter → Search autocomplete |
| 🟡 Intermediate | **Real-time systems** | WhatsApp → WebSockets at scale → Live sports scores → Uber |
| 🔴 Advanced | **Media at scale** | Instagram → Twitter / X → YouTube → Netflix |
| 🔴 Advanced | **Money & bookings** | BookMyShow → Amazon → Payment gateway → Buy now, pay later |

---

## 🏗️ Systems Covered

The catalogue is filterable by category, difficulty, and concept. Here's a snapshot:

![All systems catalogue with category, level and concept filters](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/nj7pb2ffkf1wz4mxm7jl.png)

- **Media & Social:** YouTube, Netflix, Instagram, Twitter / X, WhatsApp, Quora, LinkedIn, Live sports scores
- **Mobility & Logistics:** Uber, Google Maps, Zomato / food delivery, Porter, Car rental, Driver booking & fleet management
- **Commerce & Fintech:** Amazon, Payment gateway, Buy now pay later, Stock brokerage
- **Bookings & Marketplaces:** BookMyShow, MakeMyTrip, Airbnb, Airline reservations, NoBroker, Urban Company, Practo, AstroTalk, Meeting scheduler
- **Building Blocks:** URL shortener, Pastebin, API rate limiter, Search autocomplete, Web crawler, Dropbox, WebSockets at scale, Video calling (WebRTC), Redis Cluster

I deliberately included a mix of global giants *and* systems that are popular in India (BookMyShow, Zomato, NoBroker, Practo, Urban Company…) because those come up a lot in interviews here and are rarely covered elsewhere.

---

## 🎯 Who Is This For?

- 👩‍💻 **Interview preppers** — practise explaining designs end-to-end and see how patterns repeat across systems.
- 🏢 **Working engineers** — map a design you know in one cloud to another cloud's services.
- 🎓 **Students & beginners** — start with the Foundations path and build up gradually.
- 🤔 **The curious** — ever wondered what happens when you hit "Book" on a movie seat? Now you can watch it happen.

---

## 🛠️ How It's Built

- **Next.js** (static export) — the whole site is plain static files, deployed on Vercel
- **React Flow + ELK** — auto-laid-out, zoomable architecture diagrams
- **Tailwind CSS** — styling, including dark mode
- **Zod** — every system is a typed content file validated against a schema, so adding a new design is mostly writing data, not UI code

---

## 📈 What I Learned Building It

![Built to learn, shared to help: a mascot in a graduation cap watering a growing diagram plant](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/il2cs7yr8bywmp17souz.png)

Building this taught me far more than reading ever did:

- **You only really understand a system when you have to draw every hop.** Gaps in my knowledge showed up immediately when I tried to write a walkthrough.
- **Clouds are more similar than they look.** Once you map components across AWS, GCP, Azure and open source, the underlying patterns become obvious — the names are just different.
- **Patterns repeat everywhere.** Idempotency shows up in payments, bookings, and ride matching. Fan-out shows up in Twitter, Instagram, and LinkedIn. Seeing this visually made it click.

This project is very much still growing — and so am I.

---

## 🤝 Get Involved

![Come build it with me: star the repo, raise issues, send PRs, share ideas](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/tefw1v9smwtq2p2tgjbc.png)

This is a learning project, and I'd love for it to become a community resource. If you found it useful:

- ⭐ **Star the repo on GitHub** — it really helps more people discover it: [github.com/amananandrai/system-design-explainer](https://github.com/amananandrai/system-design-explainer)
- 💡 **Share suggestions** — which system should I add next? Drop it in the comments!
- 🐛 **Raise issues** — spotted an inaccurate diagram, a wrong cloud mapping, or a bug? Please [open an issue](https://github.com/amananandrai/system-design-explainer/issues).
- 🔧 **Raise PRs** — contributions are very welcome, whether it's a new system, a better walkthrough, a component fix, or a UI improvement.

Want to add a system? Create a file in `src/content/systems/`, register it in `systems/index.ts`, follow the schema in `src/types/schema.ts`, and run `npm run validate` to check it. To run it locally:

```bash
git clone https://github.com/amananandrai/system-design-explainer.git
cd system-design-explainer
npm install
npm run dev   # http://localhost:3000
```

---

## 🙌 Wrapping Up

👉 **Try it here:** [system-design-explainer.vercel.app](https://system-design-explainer.vercel.app/)
⭐ **Star it here:** [github.com/amananandrai/system-design-explainer](https://github.com/amananandrai/system-design-explainer)

I'd genuinely love to hear your feedback. Tell me in the comments which architecture you explored first — and which one you want to see next!

![Thanks for reading! The mascots bouncing with party hats](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/75tgpa7gkhkxetm5w4j0.gif)

Happy designing! 🚀

## 评论（11/11）

> **Ronak sarda** · 2026-11-03T02:41:15Z　
> Super helpful 🫡
>
> The details and workflows , clearly put up a lot of thinking 🔥

---

> **amananandrai** · 2026-11-03T02:43:43Z　
> Thanks a lot, you can suggest improvements in the Github repo.

---

> **Francisco Grandón** · 2026-11-03T04:56:36Z　
> Mapping request flows dynamically across AWS, Azure, and open-source equivalents makes the trade-offs far clearer than static block diagrams. The hardest part of multi-cloud parity is usually the divergence in managed queue semantics and consistency models. What was the most challenging primitive to map faithfully between cloud-managed services and open-source stacks?

---

> **Paul Lovelace** · 2026-11-03T19:29:14Z　
> The cloud-switch is the part I'd actually use — I can read a generic flow fine, it's the AWS-to-GCP translation in my head that gets tiring. What happens on the open-source lens when there's genuinely no equivalent, does the box just go blank or does it flag the gap?

---

> **Arslan Ahmad** · 2026-11-06T05:35:15Z　
> This solves a real problem. Candidates who think in vendor products ("we'll use SQS") often struggle when an interviewer pushes on fundamentals. Flipping the same architecture between AWS, Azure, GCP and open source forces you to see the role each component plays, not the brand name. The animated request flow is a nice touch too. Static diagrams hide the sequence, and the sequence is where the interesting failure modes live. Starred the repo.

---

> **amananandrai** · 2026-11-06T06:25:42Z　
> Thanks for your reply, please suggest some improvements as it is still in nascent phase.

---

> **gulnur** · 2026-11-06T08:33:15Z　
> How helpful it is☺️ Im definitely gonna check out the learning paths. Also i was wondering which tool do you use for animations? it looks great do

---

> **Crack Tech** · 2026-11-08T10:20:48Z　
> The switching part is what got me. From the interviewer's chair, most candidates can draw YouTube upload once they've seen a diagram. Then I change one thing — okay, now it's not S3, or uploads spike 10x — and the drawing falls apart because they memorised names, not the flow. What you're building trains the other muscle. If you know what each box is actually doing, the vendor word on top almost doesn't matter. You can rebuild it live, in whatever stack. That's a very different signal in the room, and honestly it's the part most prep skips.

---

> **AheadKit** · 2026-11-09T06:29:53Z　
> The cloud-switch is the feature I didn't know I needed until I saw the YouTube design flip between all five in one gif — same boxes, same arrows, S3 becomes Cloud Storage becomes Blob Storage becomes MinIO. That's the exact translation work I used to do in my head during interviews, badly. One suggestion: the BookMyShow walkthrough with the seat hold and the idempotency key is the one I'd put front and centre for interview prep, it's the closest thing on the site to a real interview question walking itself through. 36 systems is already a lot, but a "most asked in interviews" filter would make this the first tab I open before a system design round.

---

> **Mansur Fattakhov** · 2026-11-09T08:45:06Z　
> A walkthrough I'd like to see: the payment succeeds, but the response times out before the booking service receives it. Then follow the retry, the idempotency key, and what the customer sees while the outcome is uncertain. You already cover compensation after a declined payment; an unknown outcome would make a useful companion.

---

> **amananandrai** · 2026-11-12T15:43:49Z　
> I have changed the UI of the website, give your suggestions/opinions on it.

## 关联链接

- http://localhost:3000
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/21i8rnj268gd215lo8xy.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/4qvt2rky0r2p67c4cnoo.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/4t4dznz1ies71a6dcts4.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/75tgpa7gkhkxetm5w4j0.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/8h6li1y8eu1icon8dnwu.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/axtm8t59uy2m17rynvdr.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/cbaa93wy4b2280lja072.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/dj6vgaqrub37p3d8habe.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/fg0vfh9zloet077jdnic.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/il2cs7yr8bywmp17souz.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/lljlqu3v6k8sk5l8j2gx.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/mlt6o66ydr31stobidr0.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/nj7pb2ffkf1wz4mxm7jl.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/omg41k9frmqynels17lx.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/qqugs5tde2b8i44oe49d.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/qw0fxzcyrn075jv349wz.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/swuukpnhbdm4p4s8v7v1.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/t4n75kz3xvrh21gy0jtp.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/t7epj9ecxnvt27ggkufd.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/tefw1v9smwtq2p2tgjbc.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/uadk7ulqt36zeiueaijw.gif
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/uin8z7e9u1y8vutyvzue.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/uwj6d2u1u2fc4wgwcrf7.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/z9it50jdoq0pgl1s589r.gif

## 导航

- 项目页：[[10-项目/github.com_a6f45dbb]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
